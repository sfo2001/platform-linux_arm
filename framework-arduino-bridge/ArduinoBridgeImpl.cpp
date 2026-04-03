/**
 * ArduinoBridgeImpl.cpp — MsgPack-RPC client implementation
 *
 * Implements Unix socket connection and MsgPack-RPC framing for
 * communication with the arduino-router daemon on the Arduino Uno Q.
 *
 * Wire format (MsgPack-RPC):
 *   REQUEST:      [0, msgid:uint32, method:str, params:any]
 *   RESPONSE:     [1, msgid:uint32, error:any|nil, result:any|nil]
 *   NOTIFICATION: [2, method:str, params:any]
 *
 * Framing: 4-byte big-endian length prefix before each MsgPack message.
 * The arduino-router (Go) uses the msgpack/v5 stream codec which is
 * self-delimiting, but we add explicit framing for robustness in partial-read
 * scenarios. // TODO: verify framing on hardware — router may use raw stream
 *
 * @see https://github.com/arduino/arduino-router
 * @see https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md
 */

// Suppress Boost dependency in msgpack-cxx headers (set by arduino_bridge.py via CPPDEFINES).
// Listed here explicitly so the file compiles standalone in IDEs without the PlatformIO env.
#ifndef MSGPACK_NO_BOOST
#define MSGPACK_NO_BOOST
#endif

#include "ArduinoBridge.h"

#include <arpa/inet.h>
#include <cerrno>
#include <cstdlib>
#include <cstring>
#include <stdexcept>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <vector>

// Global singleton instance
ArduinoBridgeClass Bridge;

static constexpr const char* ARDUINO_ROUTER_DEFAULT_SOCKET = "/var/run/arduino-router.sock";
static constexpr uint32_t MAX_RESPONSE_SIZE = 1024 * 1024; // 1 MB — max RPC message size
static constexpr size_t MAX_SOCKET_PATH = sizeof(sockaddr_un::sun_path) - 1; // 107 on Linux

bool ArduinoBridgeClass::connect(const char* socket_path) {
    if (_fd >= 0) return true;  // already connected

    if (!socket_path) {
        const char* env = std::getenv("ARDUINO_ROUTER_SOCKET");
        if (env) {
            // Validate: must be an absolute path within sockaddr_un.sun_path limit (107 bytes on Linux)
            size_t len = std::strlen(env);
            if (len == 0 || env[0] != '/' || len > MAX_SOCKET_PATH) {
                throw std::runtime_error(
                    "ARDUINO_ROUTER_SOCKET: invalid path (must be absolute, max "
                    + std::to_string(MAX_SOCKET_PATH) + " chars)");
            }
            _socket_path = env;
        } else {
            _socket_path = ARDUINO_ROUTER_DEFAULT_SOCKET;
        }
    } else {
        size_t len = std::strlen(socket_path);
        if (len == 0 || socket_path[0] != '/' || len > MAX_SOCKET_PATH) {
            throw std::runtime_error(
                "socket_path: invalid path (must be absolute, max "
                + std::to_string(MAX_SOCKET_PATH) + " chars)");
        }
        _socket_path = socket_path;
    }

    _fd = ::socket(AF_UNIX, SOCK_STREAM, 0);
    if (_fd < 0) return false;

    struct sockaddr_un addr{};
    addr.sun_family = AF_UNIX;
    std::strncpy(addr.sun_path, _socket_path.c_str(), sizeof(addr.sun_path) - 1);

    if (::connect(_fd, reinterpret_cast<struct sockaddr*>(&addr), sizeof(addr)) < 0) {
        ::close(_fd);
        _fd = -1;
        return false;
    }
    return true;
}

void ArduinoBridgeClass::disconnect() {
    if (_fd >= 0) {
        ::close(_fd);
        _fd = -1;
    }
}

bool ArduinoBridgeClass::_write_all(const void* data, size_t len) {
    const uint8_t* p = reinterpret_cast<const uint8_t*>(data);
    size_t remaining = len;
    while (remaining > 0) {
        ssize_t n = ::write(_fd, p, remaining);
        if (n <= 0) return false;
        p += n;
        remaining -= n;
    }
    return true;
}

bool ArduinoBridgeClass::_read_all(void* buf, size_t len) {
    uint8_t* p = reinterpret_cast<uint8_t*>(buf);
    size_t remaining = len;
    while (remaining > 0) {
        ssize_t n = ::read(_fd, p, remaining);
        if (n <= 0) return false;
        p += n;
        remaining -= n;
    }
    return true;
}

msgpack::object_handle ArduinoBridgeClass::call(const std::string& method,
                                                  msgpack::sbuffer& params) {
    if (_fd < 0) {
        throw std::runtime_error(
            "ArduinoBridge: not connected. Call Bridge.connect() first.");
    }

    uint32_t msgid = _next_msgid++;

    // Build REQUEST: [0, msgid, method, params]
    msgpack::sbuffer req_buf;
    msgpack::packer<msgpack::sbuffer> pk(req_buf);
    pk.pack_array(4);
    pk.pack(static_cast<uint8_t>(0));  // type = REQUEST
    pk.pack(msgid);
    pk.pack(method);
    // Append pre-packed params verbatim
    req_buf.write(params.data(), params.size());

    // Send with 4-byte big-endian length prefix
    // TODO: verify framing with arduino-router on hardware — may use raw stream
    if (req_buf.size() > MAX_RESPONSE_SIZE) {
        throw std::runtime_error(
            "ArduinoBridge: request too large (" +
            std::to_string(req_buf.size()) + " bytes, max " +
            std::to_string(MAX_RESPONSE_SIZE) + ")");
    }
    uint32_t req_len = htonl(static_cast<uint32_t>(req_buf.size()));
    if (!_write_all(&req_len, 4) || !_write_all(req_buf.data(), req_buf.size())) {
        throw std::runtime_error("ArduinoBridge: write failed: " +
                                 std::string(std::strerror(errno)));
    }

    // Read response: 4-byte length prefix + payload
    uint32_t resp_len_net;
    if (!_read_all(&resp_len_net, 4)) {
        throw std::runtime_error("ArduinoBridge: read length failed: " +
                                 std::string(std::strerror(errno)));
    }
    uint32_t resp_len = ntohl(resp_len_net);

    if (resp_len == 0 || resp_len > MAX_RESPONSE_SIZE) {
        throw std::runtime_error("ArduinoBridge: response size out of range: " +
                                 std::to_string(resp_len));
    }

    std::vector<char> resp_data(resp_len);
    if (!_read_all(resp_data.data(), resp_len)) {
        throw std::runtime_error("ArduinoBridge: read payload failed");
    }

    // Unpack RESPONSE: [1, msgid, error, result]
    msgpack::object_handle oh = msgpack::unpack(resp_data.data(), resp_len);
    msgpack::object resp_obj = oh.get();

    if (resp_obj.type != msgpack::type::ARRAY || resp_obj.via.array.size < 4) {
        throw std::runtime_error("ArduinoBridge: malformed response");
    }

    // Validate response msgid matches request msgid (guards against mismatched pipelined responses)
    // At this point we know type == ARRAY and size >= 4, so no outer guard needed.
    uint32_t resp_msgid;
    try {
        resp_msgid = resp_obj.via.array.ptr[1].as<uint32_t>();
    } catch (const msgpack::type_error&) {
        throw std::runtime_error("ArduinoBridge: response msgid field is not a uint32");
    }
    if (resp_msgid != msgid) {
        throw std::runtime_error(
            "ArduinoBridge: response msgid mismatch (sent " +
            std::to_string(msgid) + ", got " + std::to_string(resp_msgid) + ")");
    }

    // Check error slot (index 2)
    msgpack::object err_slot = resp_obj.via.array.ptr[2];
    if (err_slot.type != msgpack::type::NIL) {
        int code = 4;  // GenericError default
        std::string msg = "ArduinoBridge RPC error";
        if (err_slot.type == msgpack::type::ARRAY && err_slot.via.array.size >= 2) {
            code = err_slot.via.array.ptr[0].as<int>();
            msg  = err_slot.via.array.ptr[1].as<std::string>();
        }
        throw ArduinoBridgeError(code, msg);
    }

    // Return result slot (index 3) as a new owned handle
    msgpack::sbuffer result_buf;
    msgpack::pack(result_buf, resp_obj.via.array.ptr[3]);
    return msgpack::unpack(result_buf.data(), result_buf.size());
}

void ArduinoBridgeClass::provide(
    const std::string& method,
    std::function<void(msgpack::object const&, msgpack::sbuffer&)> callback) {
    _handlers[method] = std::move(callback);
}

#ifdef ARDUINO_BRIDGE_EXPERIMENTAL
int ArduinoBridgeClass::poll() {
    if (_fd < 0) return 0;

    // Non-blocking peek: check if data is available
    struct timeval tv{0, 0};
    fd_set rfds;
    FD_ZERO(&rfds);
    FD_SET(_fd, &rfds);

    int ready = ::select(_fd + 1, &rfds, nullptr, nullptr, &tv);
    if (ready <= 0) return 0;

    // Read one message (non-framed peek — read up to 65535 bytes)
    // TODO: implement proper streaming unpacker for production use
    std::vector<char> buf(65535);
    ssize_t n = ::read(_fd, buf.data(), buf.size());
    if (n <= 0) return 0;
    if (static_cast<uint32_t>(n) > MAX_RESPONSE_SIZE) return 0;  // forward-looking guard: current 65535-byte buf caps n below this

    // TODO: if framing (4-byte length prefix) is confirmed on hardware, poll() must
    // strip the prefix before calling msgpack::unpack(). Currently uses raw read,
    // matching the assumption that arduino-router uses a raw MsgPack stream here.
    // Verify against actual arduino-router behavior on hardware.

    // Known limitation: processes only the first MsgPack object in the buffer.
    // If multiple notifications arrive in a single read, subsequent objects are
    // discarded. Use a streaming unpacker (msgpack::unpacker) for production use.
    msgpack::object_handle oh = msgpack::unpack(buf.data(), n);
    msgpack::object obj = oh.get();

    // Expect NOTIFICATION: [2, method, params]
    if (obj.type != msgpack::type::ARRAY || obj.via.array.size < 3) return 0;
    if (obj.via.array.ptr[0].as<int>() != 2) return 0;

    std::string method_name = obj.via.array.ptr[1].as<std::string>();
    auto it = _handlers.find(method_name);
    if (it == _handlers.end()) return 0;

    msgpack::sbuffer result_buf;
    it->second(obj.via.array.ptr[2], result_buf);
    return 1;
}
#endif  // ARDUINO_BRIDGE_EXPERIMENTAL
