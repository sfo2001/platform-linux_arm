/**
 * arduino-bridge-blink — Arduino Uno Q example
 *
 * Demonstrates paired MCU sketch + Linux C++ program using custom RPC methods.
 * The MCU sketch (mcu_companion/ArduinoUnoQ_MraaCompanion.ino) registers
 * "gpio/mode", "gpio/write", and "aio/read" via Bridge.provide(). This Linux
 * program calls those methods via Bridge.call().
 *
 * ⚠️ Community Testing Notice: Method names and parameter formats have not been
 * validated on physical hardware. See TODO comments.
 *
 * Standard GPIO RPC contract defined in:
 *   docs/boards/arduino_uno_q.md
 */

#include <ArduinoBridge.h>
#include <cstdio>
#include <unistd.h>

// Pack a MsgPack map with the given key-value pairs
// Helper to reduce boilerplate in examples
static void pack_gpio_mode(msgpack::sbuffer& buf, int pin, const char* mode) {
    msgpack::packer<msgpack::sbuffer> pk(buf);
    pk.pack_map(2);
    pk.pack(std::string("pin"));  pk.pack(pin);
    pk.pack(std::string("mode")); pk.pack(std::string(mode));
}

static void pack_gpio_write(msgpack::sbuffer& buf, int pin, int value) {
    msgpack::packer<msgpack::sbuffer> pk(buf);
    pk.pack_map(2);
    pk.pack(std::string("pin"));   pk.pack(pin);
    pk.pack(std::string("value")); pk.pack(value);
}

static void pack_aio_read(msgpack::sbuffer& buf, int pin) {
    msgpack::packer<msgpack::sbuffer> pk(buf);
    pk.pack_map(1);
    pk.pack(std::string("pin")); pk.pack(pin);
}

int main() {
    printf("arduino-bridge-blink: Arduino Uno Q example\n");
    printf("Connecting to arduino-router...\n");

    if (!Bridge.connect()) {
        fprintf(stderr,
            "ERROR: Failed to connect to arduino-router socket.\n"
            "Verify the daemon is running: systemctl status arduino-router\n"
            "Socket path: /var/run/arduino-router.sock (override: ARDUINO_ROUTER_SOCKET)\n");
        return 1;
    }

    printf("Connected.\n\n");

    // Set D13 (built-in LED) to OUTPUT
    // TODO: verify method name "gpio/mode" matches MCU sketch registration
    {
        msgpack::sbuffer params;
        pack_gpio_mode(params, 13, "OUTPUT");
        try {
            Bridge.call("gpio/mode", params);
            printf("gpio/mode pin=13 mode=OUTPUT: OK\n");
        } catch (const ArduinoBridgeError& e) {
            fprintf(stderr, "gpio/mode error [%d]: %s\n", e.code, e.what());
            Bridge.disconnect();
            return 1;
        }
    }

    // Blink D13 five times
    // TODO: verify method name "gpio/write" matches MCU sketch registration
    printf("Blinking D13 five times...\n");
    for (int i = 0; i < 5; ++i) {
        try {
            {
                msgpack::sbuffer params;
                pack_gpio_write(params, 13, 1);
                Bridge.call("gpio/write", params);
                printf("  gpio/write pin=13 value=1 (LED ON)\n");
            }
            sleep(1);
            {
                msgpack::sbuffer params;
                pack_gpio_write(params, 13, 0);
                Bridge.call("gpio/write", params);
                printf("  gpio/write pin=13 value=0 (LED OFF)\n");
            }
            sleep(1);
        } catch (const std::exception& e) {
            fprintf(stderr, "gpio/write error (iteration %d): %s\n", i + 1, e.what());
            Bridge.disconnect();
            return 1;
        }
    }

    // Read analog pin A0
    // TODO: verify method name "aio/read" matches MCU sketch registration
    {
        msgpack::sbuffer params;
        pack_aio_read(params, 0);
        try {
            auto result = Bridge.call("aio/read", params);
            int val = result.get().as<int>();
            printf("\naio/read pin=A0 (pin=0): value=%d\n", val);
        } catch (const ArduinoBridgeError& e) {
            fprintf(stderr, "aio/read error [%d]: %s\n", e.code, e.what());
        }
    }

    Bridge.disconnect();
    printf("\nDone.\n");
    return 0;
}
