/**
 * ArduinoUnoQ_MraaCompanion.ino — STM32U585 companion sketch
 *
 * Registers the standard GPIO RPC contract methods via Bridge.provide().
 * The Linux side (arduino-bridge-blink) calls these methods via Bridge.call().
 *
 * Flash this sketch to the STM32U585 MCU using the Arduino IDE or arduino-cli
 * targeting the "Arduino Uno Q (MCU)" board.
 *
 * ⚠️ Community Testing Notice: This sketch has not been validated on physical
 * hardware. The Arduino_RouterBridge library API is based on source analysis
 * of github.com/arduino/arduino-router. Please verify and report issues.
 *
 * Standard GPIO RPC contract:
 *   gpio/caps        — capability handshake (called by Linux at startup)
 *   gpio/mode        — set pin direction (OUTPUT / INPUT / INPUT_PULLUP / INPUT_PULLDOWN)
 *   gpio/write       — digital write (value: 0 or 1)
 *   gpio/read        — digital read  (returns 0 or 1)
 *   gpio/read_many   — batch digital read (returns array)
 *   aio/read         — analog read (returns 0-1023 or 0-4095)
 *   pwm/write        — PWM duty cycle (duty: 0.0-1.0)
 *
 * @see docs/boards/arduino_uno_q.md
 * @see https://github.com/arduino/arduino-router
 */

// TODO: verify the Arduino_RouterBridge library name and include path on hardware
#include <Arduino_RouterBridge.h>
#include <vector>

// ── gpio/caps handler ──────────────────────────────────────────────────────────
// Called once by Linux client at startup. Returns capability map.
// TODO: verify Bridge.provide() callback signature on hardware — actual param type may differ
void caps_handler() {
    // Return capability map indicating protocol_version and supported commands.
    // The exact response format must match ArduinoBridge.h expectations.
    // TODO: verify response serialization API with Arduino_RouterBridge library
    Bridge.respond({
        {"protocol_version", 1},
        {"pin_scheme", "arduino"},
        {"supported_commands", {"gpio/read", "gpio/write", "gpio/mode",
                                "gpio/read_many", "aio/read", "pwm/write"}},
        {"pin_modes", {"INPUT", "OUTPUT", "INPUT_PULLUP", "INPUT_PULLDOWN"}}
    });
}

// ── gpio/mode handler ─────────────────────────────────────────────────────────
// TODO: verify Bridge.provide() parameter parsing API on hardware
void gpio_mode_handler(int pin, String mode) {
    if (mode == "OUTPUT")         pinMode(pin, OUTPUT);
    else if (mode == "INPUT")     pinMode(pin, INPUT);
    else if (mode == "INPUT_PULLUP")   pinMode(pin, INPUT_PULLUP);
    else if (mode == "INPUT_PULLDOWN") pinMode(pin, INPUT_PULLDOWN);
    else { Bridge.error(102, "UnsupportedMode"); return; }
    Bridge.respond(true);
}

// ── gpio/write handler ────────────────────────────────────────────────────────
void gpio_write_handler(int pin, int value) {
    digitalWrite(pin, value ? HIGH : LOW);
    Bridge.respond(true);
}

// ── gpio/read handler ─────────────────────────────────────────────────────────
void gpio_read_handler(int pin) {
    Bridge.respond(digitalRead(pin));
}

// ── gpio/read_many handler ────────────────────────────────────────────────────
// TODO: verify array parameter parsing with Arduino_RouterBridge on hardware
void gpio_read_many_handler(int* pins, int count) {
    std::vector<int> results(count);
    for (int i = 0; i < count; i++) {
        results[i] = digitalRead(pins[i]);
    }
    Bridge.respond_array(results.data(), count);
}

// ── aio/read handler ──────────────────────────────────────────────────────────
void aio_read_handler(int pin) {
    Bridge.respond(analogRead(pin));
}

// ── pwm/write handler ─────────────────────────────────────────────────────────
void pwm_write_handler(int pin, float duty) {
    // Clamp duty to [0.0, 1.0] to prevent analogWrite out-of-range behavior
    if (duty < 0.0f) duty = 0.0f;
    if (duty > 1.0f) duty = 1.0f;
    analogWrite(pin, static_cast<int>(duty * 255.0f));
    Bridge.respond(true);
}

// ─────────────────────────────────────────────────────────────────────────────

void setup() {
    Bridge.begin();

    // TODO: verify Bridge.provide() API with Arduino_RouterBridge library on hardware
    Bridge.provide("gpio/caps",      caps_handler);
    Bridge.provide("gpio/mode",      gpio_mode_handler);
    Bridge.provide("gpio/write",     gpio_write_handler);
    Bridge.provide("gpio/read",      gpio_read_handler);
    Bridge.provide("gpio/read_many", gpio_read_many_handler);
    Bridge.provide("aio/read",       aio_read_handler);
    Bridge.provide("pwm/write",      pwm_write_handler);
}

void loop() {
    // Bridge.run() processes incoming RPC requests from the arduino-router
    // TODO: verify method name (may be Bridge.loop() or Bridge.process())
    Bridge.run();
}
