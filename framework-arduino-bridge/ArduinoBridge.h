/**
 * ArduinoBridge — MsgPack-RPC client for Arduino Uno Q
 *
 * Provides a C++ interface to call user-defined methods registered by MCU
 * firmware via the arduino-router Unix socket.
 *
 * Protocol: MessagePack-RPC over AF_UNIX SOCK_STREAM
 * Socket:   /var/run/arduino-router.sock (default)
 *
 * The arduino-router is a pure message broker. GPIO method names (e.g.
 * "gpio/write", "gpio/read") are user-defined strings agreed upon between
 * MCU firmware (Bridge.provide()) and Linux client (Bridge.call()).
 *
 * There is NO predefined registry of method names. See the GPIO RPC contract
 * in docs/boards/arduino_uno_q.md.
 *
 * Runtime dependency:
 *   arduino-router daemon must be running on the target.
 *   Verify: systemctl status arduino-router
 *
 * Usage:
 *   #include <ArduinoBridge.h>
 *
 *   Bridge.connect();
 *
 *   msgpack::sbuffer params;
 *   msgpack::packer<msgpack::sbuffer> pk(params);
 *   pk.pack_map(2);
 *   pk.pack(std::string("pin"));   pk.pack(13);
 *   pk.pack(std::string("value")); pk.pack(1);
 *
 *   // TODO: verify method name matches MCU sketch Bridge.provide() registration
 *   Bridge.call("gpio/write", params);
 *
 *   Bridge.disconnect();
 *
 * @see docs/boards/arduino_uno_q.md
 * @see https://github.com/arduino/arduino-router
 */

#pragma once

#include <cstdint>
#include <functional>
#include <stdexcept>
#include <string>
#include <unordered_map>

// Suppress Boost dependency in msgpack-cxx (set by arduino_bridge.py CPPDEFINES).
// Listed here so the header compiles correctly in IDEs without the PlatformIO env.
#ifndef MSGPACK_NO_BOOST
#define MSGPACK_NO_BOOST
#endif
#include <msgpack.hpp>

/**
 * @brief Error thrown when an RPC call returns an error response.
 */
class ArduinoBridgeError : public std::runtime_error {
public:
    int code;
    explicit ArduinoBridgeError(int c, const std::string& msg)
        : std::runtime_error(msg), code(c) {}
};

/**
 * @brief MsgPack-RPC client for the arduino-router Unix socket.
 *
 * The single global instance `Bridge` is available after including this header.
 */
class ArduinoBridgeClass {
public:
    /**
     * @brief Connect to the arduino-router Unix socket.
     *
     * @param socket_path Path to the Unix socket. Pass nullptr (default) to use
     *   the ARDUINO_ROUTER_SOCKET environment variable, or fall back to the
     *   default /var/run/arduino-router.sock.
     * @return true on success, false on failure (check errno).
     */
    bool connect(const char* socket_path = nullptr);

    /**
     * @brief Disconnect from the arduino-router Unix socket.
     */
    void disconnect();

    /**
     * @brief Return true if connected to the router socket.
     */
    bool is_connected() const { return _fd >= 0; }

    /**
     * @brief Call a method on MCU firmware via MsgPack-RPC.
     *
     * Sends REQUEST [0, msgid, method, params_buf] and waits for
     * RESPONSE [1, msgid, error, result].
     *
     * @param method  RPC method name (must match Bridge.provide() in MCU sketch).
     *   NOTE: method names are user-defined. Standard GPIO contract uses
     *   "gpio/write", "gpio/read", "gpio/mode", "aio/read", "pwm/write".
     *   // TODO: verify all method names used here against MCU firmware
     *
     * @param params  Pre-packed MsgPack map. Build with msgpack::packer<msgpack::sbuffer>.
     * @return        Handle to the result object (valid while handle is in scope).
     * @throws ArduinoBridgeError  if the response contains a non-null error slot.
     * @throws std::runtime_error  on connection or framing errors.
     */
    msgpack::object_handle call(const std::string& method, msgpack::sbuffer& params);

    /**
     * @brief Register a Linux-side method that the MCU can invoke.
     *
     * When a NOTIFICATION [2, method, params] arrives on the socket, the
     * registered callback is invoked synchronously. Call poll() in a loop
     * to dispatch incoming notifications.
     *
     * @param method   Method name to register.
     * @param callback Function(params_object, result_buffer). Write the MsgPack
     *                 result into result_buffer.
     */
    void provide(const std::string& method,
                 std::function<void(msgpack::object const&, msgpack::sbuffer&)> callback);

#ifdef ARDUINO_BRIDGE_EXPERIMENTAL
    /**
     * @brief Poll for incoming notifications (non-blocking, returns immediately).
     *
     * **EXPERIMENTAL** — Define `ARDUINO_BRIDGE_EXPERIMENTAL` to enable.
     *
     * Call in a loop to dispatch MCU-initiated method calls registered via
     * provide(). Only needed if you use provide().
     *
     * **Non-production limitation:** Uses a raw unframed read (not the 4-byte
     * length-prefix protocol used by call()). If multiple notifications arrive in
     * a single socket read, all objects after the first are silently discarded.
     * Do not use in production until hardware testing confirms the arduino-router
     * notification framing format and a streaming unpacker (msgpack::unpacker)
     * is implemented.
     *
     * @return Number of notifications dispatched (0 if none pending).
     */
    int poll();
#endif  // ARDUINO_BRIDGE_EXPERIMENTAL

private:
    int _fd = -1;
    uint32_t _next_msgid = 1;
    std::string _socket_path;
    std::unordered_map<std::string,
        std::function<void(msgpack::object const&, msgpack::sbuffer&)>> _handlers;

    bool _write_all(const void* data, size_t len);
    bool _read_all(void* buf, size_t len);
};

/**
 * @brief Global ArduinoBridge instance.
 *
 * Include <ArduinoBridge.h> and use Bridge.connect(), Bridge.call(), etc.
 */
extern ArduinoBridgeClass Bridge;
