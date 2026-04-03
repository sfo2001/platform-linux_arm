/**
 * Unit tests for ArduinoBridge — path validation and MsgPack-RPC call/response.
 *
 * Compile and run:
 *   cmake -B build && cmake --build build --target test_arduino_bridge
 *   ./build/test_arduino_bridge
 *
 * Or via CTest: cmake --build build && ctest --test-dir build -V
 */
#ifndef MSGPACK_NO_BOOST
#define MSGPACK_NO_BOOST
#endif

#include "../framework-arduino-bridge/ArduinoBridge.h"

#include <arpa/inet.h>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <msgpack.hpp>
#include <sys/socket.h>
#include <sys/un.h>
#include <thread>
#include <unistd.h>
#include <vector>

// ── helpers ──────────────────────────────────────────────────────────────────

static std::string tmp_sock_path() {
    char tpl[] = "/tmp/test_arduino_bridge_XXXXXX";
    int fd = mkstemp(tpl);
    assert(fd >= 0);
    close(fd);
    unlink(tpl);
    return std::string(tpl);
}

// Write a MsgPack-RPC RESPONSE frame: [1, msgid, error|nil, result|nil]
static void write_response(int fd, uint32_t msgid, bool is_error,
                            const std::string& val) {
    msgpack::sbuffer buf;
    msgpack::packer<msgpack::sbuffer> pk(buf);
    pk.pack_array(4);
    pk.pack(1u);  // RESPONSE type
    pk.pack(msgid);
    if (is_error) {
        pk.pack_array(2);
        pk.pack(42);   // error code
        pk.pack(val);  // error message
        pk.pack_nil(); // nil result
    } else {
        pk.pack_nil(); // nil error
        pk.pack(val);  // result value
    }
    uint32_t len_net = htonl(static_cast<uint32_t>(buf.size()));
    write(fd, &len_net, 4);
    write(fd, buf.data(), buf.size());
}

// Bind + listen on a temp Unix socket path. Returns srv_fd (caller closes).
static int make_server(const std::string& path) {
    int fd = socket(AF_UNIX, SOCK_STREAM, 0);
    assert(fd >= 0);
    struct sockaddr_un addr{};
    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, path.c_str(), sizeof(addr.sun_path) - 1);
    assert(bind(fd, reinterpret_cast<struct sockaddr*>(&addr), sizeof(addr)) == 0);
    assert(listen(fd, 1) == 0);
    return fd;
}

// ── path validation tests (no socket required) ───────────────────────────────

void test_connect_empty_path_throws() {
    ArduinoBridgeClass b;
    bool threw = false;
    try { b.connect(""); } catch (const std::runtime_error&) { threw = true; }
    assert(threw && "connect(\"\") must throw std::runtime_error");
    std::cout << "PASS test_connect_empty_path_throws\n";
}

void test_connect_relative_path_throws() {
    ArduinoBridgeClass b;
    bool threw = false;
    try { b.connect("relative/path.sock"); }
    catch (const std::runtime_error&) { threw = true; }
    assert(threw && "connect(relative) must throw std::runtime_error");
    std::cout << "PASS test_connect_relative_path_throws\n";
}

void test_connect_overlong_path_throws() {
    // MAX_SOCKET_PATH is 107 on Linux; 200-char path exceeds it.
    ArduinoBridgeClass b;
    std::string long_path(200, 'x');
    long_path[0] = '/';  // make it absolute so only the length check fires
    bool threw = false;
    try { b.connect(long_path.c_str()); }
    catch (const std::runtime_error&) { threw = true; }
    assert(threw && "connect(overlong) must throw std::runtime_error");
    std::cout << "PASS test_connect_overlong_path_throws\n";
}

void test_connect_nonexistent_socket_returns_false() {
    // Valid absolute path but no server → connect() returns false, does not throw.
    ArduinoBridgeClass b;
    bool result = b.connect("/tmp/no_such_arduino_bridge_server.sock");
    assert(!result && "connect() to absent socket must return false");
    std::cout << "PASS test_connect_nonexistent_socket_returns_false\n";
}

// ── call/response round-trip tests (mock socket server) ──────────────────────

void test_call_roundtrip_returns_result() {
    std::string path = tmp_sock_path();
    int srv_fd = make_server(path);

    auto server = std::thread([&]() {
        int cli = accept(srv_fd, nullptr, nullptr);
        uint32_t len_net;
        read(cli, &len_net, 4);
        uint32_t len = ntohl(len_net);
        std::vector<char> buf(len);
        read(cli, buf.data(), len);
        auto oh = msgpack::unpack(buf.data(), len);
        uint32_t msgid = oh.get().via.array.ptr[1].as<uint32_t>();
        write_response(cli, msgid, false, "ok");
        close(cli);
    });

    ArduinoBridgeClass b;
    assert(b.connect(path.c_str()));
    msgpack::sbuffer params;
    msgpack::pack(params, std::string("param"));
    auto result = b.call("test/method", params);
    assert(result.get().as<std::string>() == "ok");
    b.disconnect();

    server.join();
    close(srv_fd);
    unlink(path.c_str());
    std::cout << "PASS test_call_roundtrip_returns_result\n";
}

void test_call_error_response_throws_ArduinoBridgeError() {
    std::string path = tmp_sock_path();
    int srv_fd = make_server(path);

    auto server = std::thread([&]() {
        int cli = accept(srv_fd, nullptr, nullptr);
        uint32_t len_net;
        read(cli, &len_net, 4);
        uint32_t len = ntohl(len_net);
        std::vector<char> buf(len);
        read(cli, buf.data(), len);
        auto oh = msgpack::unpack(buf.data(), len);
        uint32_t msgid = oh.get().via.array.ptr[1].as<uint32_t>();
        write_response(cli, msgid, true, "method not found");
        close(cli);
    });

    ArduinoBridgeClass b;
    assert(b.connect(path.c_str()));
    msgpack::sbuffer params;
    msgpack::pack(params, std::string("param"));
    bool threw = false;
    int caught_code = 0;
    try {
        b.call("no/such/method", params);
    } catch (const ArduinoBridgeError& e) {
        threw = true;
        caught_code = e.code;
    }
    assert(threw && "error response must throw ArduinoBridgeError");
    assert(caught_code == 42 && "ArduinoBridgeError.code must be 42");
    b.disconnect();

    server.join();
    close(srv_fd);
    unlink(path.c_str());
    std::cout << "PASS test_call_error_response_throws_ArduinoBridgeError\n";
}

void test_call_msgid_mismatch_throws() {
    std::string path = tmp_sock_path();
    int srv_fd = make_server(path);

    // Server sends back wrong msgid (9999)
    auto server = std::thread([&]() {
        int cli = accept(srv_fd, nullptr, nullptr);
        uint32_t len_net;
        read(cli, &len_net, 4);
        uint32_t len = ntohl(len_net);
        std::vector<char> buf(len);
        read(cli, buf.data(), len);
        write_response(cli, 9999u, false, "spoofed");
        close(cli);
    });

    ArduinoBridgeClass b;
    assert(b.connect(path.c_str()));
    msgpack::sbuffer params;
    msgpack::pack(params, std::string("param"));
    bool threw = false;
    try {
        b.call("test/method", params);
    } catch (const std::runtime_error& e) {
        threw = true;
        assert(std::string(e.what()).find("mismatch") != std::string::npos);
    }
    assert(threw && "msgid mismatch must throw std::runtime_error containing 'mismatch'");
    b.disconnect();

    server.join();
    close(srv_fd);
    unlink(path.c_str());
    std::cout << "PASS test_call_msgid_mismatch_throws\n";
}

void test_call_malformed_response_throws() {
    std::string path = tmp_sock_path();
    int srv_fd = make_server(path);

    // Server sends a MsgPack integer (not an array) — malformed response
    auto server = std::thread([&]() {
        int cli = accept(srv_fd, nullptr, nullptr);
        uint32_t len_net;
        read(cli, &len_net, 4);
        uint32_t len = ntohl(len_net);
        std::vector<char> buf(len);
        read(cli, buf.data(), len);
        // Write a bare integer, not a [1, msgid, err, result] array
        msgpack::sbuffer bad;
        msgpack::pack(bad, 42u);
        uint32_t bad_len = htonl(static_cast<uint32_t>(bad.size()));
        write(cli, &bad_len, 4);
        write(cli, bad.data(), bad.size());
        close(cli);
    });

    ArduinoBridgeClass b;
    assert(b.connect(path.c_str()));
    msgpack::sbuffer params;
    msgpack::pack(params, std::string("param"));
    bool threw = false;
    try {
        b.call("test/method", params);
    } catch (const std::runtime_error&) {
        threw = true;
    }
    assert(threw && "malformed response must throw std::runtime_error");
    b.disconnect();

    server.join();
    close(srv_fd);
    unlink(path.c_str());
    std::cout << "PASS test_call_malformed_response_throws\n";
}

// ── main ─────────────────────────────────────────────────────────────────────

int main() {
    test_connect_empty_path_throws();
    test_connect_relative_path_throws();
    test_connect_overlong_path_throws();
    test_connect_nonexistent_socket_returns_false();
    test_call_roundtrip_returns_result();
    test_call_error_response_throws_ArduinoBridgeError();
    test_call_msgid_mismatch_throws();
    test_call_malformed_response_throws();
    std::cout << "\nAll C++ tests passed.\n";
    return 0;
}
