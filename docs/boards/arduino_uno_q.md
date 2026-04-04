# Arduino Uno Q

> **⚠️ Community Testing Notice**
> No Arduino Uno Q hardware is available to the maintainer. This port has not been
> validated on physical hardware. Community testing and feedback are essential before
> this port can be considered stable. Please open issues with test results, corrections,
> and firmware compatibility reports.

## Open Hardware Validation TODOs

The following items require validation on physical Arduino Uno Q hardware before
this port is considered stable. Community testers: please open an issue with results.

| Item | File | Status |
|------|------|--------|
| `Bridge.call("gpio/write", ...)` method name | `examples/arduino-bridge-blink/src/main.cpp` | Unverified — confirm matches MCU `Bridge.provide()` registration |
| `Bridge.call("gpio/read", ...)` method name | `examples/arduino-bridge-blink/src/main.cpp` | Unverified |
| `Bridge.call("gpio/mode", ...)` method name | `examples/arduino-bridge-blink/src/main.cpp` | Unverified |
| `Bridge.run()` vs `Bridge.loop()` vs `Bridge.process()` | `mcu_companion/ArduinoUnoQ_MraaCompanion.ino` | Unverified — check arduino-router API |
| MsgPack-RPC framing (4-byte length prefix) | `ArduinoBridgeImpl.cpp` / `ArduinoBridge.h:poll()` | Unverified — arduino-router may use raw stream |

## Hardware Overview

The Arduino Uno Q is a dual-chip board in the standard Arduino Uno form factor:

| Chip | Role | Architecture | OS / RTOS |
|------|------|-------------|-----------|
| Qualcomm QRB2210 (Dragonwing) | MPU — runs your Linux application | 4× ARM Cortex-A53 @ 2.0 GHz, AArch64 | Debian Linux |
| STMicroelectronics STM32U585 | MCU — owns all Arduino header pins | ARM Cortex-M33 | Zephyr RTOS |

**QRB2210 specs:** 2 GB or 4 GB LPDDR4, 16 GB eMMC, Wi-Fi 5, Bluetooth 5.1, USB-C.

## Why lgpio / libgpiod / pigpio / WiringPi Do NOT Work Here

> **lgpio, libgpiod, pigpio, and WiringPi are NOT supported on the Arduino Uno Q.**

All four frameworks operate by issuing `ioctl()` calls to Linux kernel GPIO character
devices (`/dev/gpiochip*`). On the Arduino Uno Q, **all Arduino header pins (D0–D13,
A0–A5) are owned by the STM32U585 MCU** — not by the QRB2210 Linux side. There are no
`/dev/gpiochip*` devices for the Arduino header pins on the Linux side. Calling lgpio
or libgpiod will fail at runtime with "device not found".

GPIO access from Linux requires the **arduino-router daemon** and the **arduino-bridge
framework** (see Phase 2 below).

## Runtime Dependency: arduino-router

The **arduino-router** daemon is required for any GPIO/PWM/ADC operations from Linux.
It is pre-installed on the stock Arduino Uno Q Debian image:

| Item | Value |
|------|-------|
| Package | `arduino-router` v0.8.0 |
| Binary | `/usr/bin/arduino-router` |
| Unix socket | `/var/run/arduino-router.sock` |
| Service | `arduino-router.service` (starts on boot) |
| Serial device | `/dev/ttyHS1` — **do not open from user code** |

Verify it is running:
```bash
systemctl status arduino-router
```

On custom images, install manually:
```bash
sudo apt install ./arduino-router_0.8.0-1_arm64.deb
```

> **Note on arduino-router internals:** The arduino-router source is available at
> [github.com/arduino/arduino-router](https://github.com/arduino/arduino-router).
> It is a pure MsgPack-RPC message broker — it defines no GPIO method names.
> All method names (e.g. `gpio/write`) are user-defined conventions agreed
> between MCU firmware and Linux client. See the GPIO RPC contract in
> [Architecture & Design Rationale](#architecture--design-rationale) section below.

## Pin Mapping (Arduino → STM32 GPIO)

All pins are **3.3 V logic**. A0 and A1 are NOT 5 V-tolerant.

| Arduino | STM32 | | Arduino | STM32 |
|---------|-------|-|---------|-------|
| D0 | PB7 | | D8 | PB4 |
| D1 | PB6 | | D9 | PB8 |
| D2 | PB3 | | D10 | PB9 |
| D3 | PB0 | | D11 | PB15 |
| D4 | PA12 | | D12 | PB14 |
| D5 | PA11 | | **D13** | **PB13** |
| D6 | PB1 | | A0/D14 | PA4 |
| D7 | PB2 | | A1/D15 | PA5 |
| | | | A2–A5 | PA6, PA7, PC1, PC0 |

---

## Phase 1 — Compile, Cross-Compile, and SSH Upload

Phase 1 enables building AArch64 Linux programs targeting the QRB2210 with no GPIO
framework. This is suitable for network services, data processing, and applications
that do not require direct GPIO access.

**Requires:** `aarch64-linux-gnu` cross-compiler
```bash
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
```

### platformio.ini (compile only)

```ini
[env:arduino_uno_q]
platform = linux_arm
board = arduino_uno_q
; No framework — bare-metal C/C++ application
```

### platformio.ini (compile + SSH upload)

```ini
[env:arduino_uno_q]
platform = linux_arm
board = arduino_uno_q
upload_protocol = scp
upload_port = user@uno-q-host
upload_path = /tmp/my_program
upload_run_after = true
```

Build and upload:
```bash
pio run -d . -t upload
```

---

## Phase 2 — arduino-bridge Framework

The **arduino-bridge** framework provides a C++ MsgPack-RPC client library that
communicates with MCU firmware via the arduino-router Unix socket.

**Architecture:**
```
Linux C++ (your code using Bridge.call())
      │
      │  Unix socket: /var/run/arduino-router.sock
      │  Protocol: MessagePack-RPC
      ▼
arduino-router daemon (Go, pre-installed)
      │
      │  SPI  /dev/ttyHS1
      ▼
STM32U585 MCU firmware
(Bridge.provide() registrations in your Arduino sketch)
```

### What the framework provides

The `ArduinoBridge` object gives your Linux C++ code two capabilities:

1. **`Bridge.call(method, params)`** — send a MsgPack-RPC request to the MCU and get the result back.
2. **`Bridge.provide(method, callback)`** — register a Linux-side method that the MCU can invoke.

### platformio.ini (Phase 2)

```ini
[env:arduino_uno_q]
platform = linux_arm
board = arduino_uno_q
framework = arduino-bridge
upload_protocol = scp
upload_port = user@uno-q-host
```

### Linux C++ example

```cpp
#include <ArduinoBridge.h>

int main() {
    // Connect to arduino-router (default: /var/run/arduino-router.sock)
    if (!Bridge.connect()) {
        fprintf(stderr, "Failed to connect to arduino-router\n");
        return 1;
    }

    // Call a custom method registered by MCU firmware
    // Method name must match Bridge.provide("gpio/write", ...) in your sketch
    msgpack::sbuffer params;
    msgpack::packer<msgpack::sbuffer> pk(params);
    pk.pack_map(2);
    pk.pack(std::string("pin"));   pk.pack(13);
    pk.pack(std::string("value")); pk.pack(1);

    // TODO: verify method name "gpio/write" matches your MCU sketch registration
    Bridge.call("gpio/write", params);

    Bridge.disconnect();
    return 0;
}
```

### Setup: cross-compile MRAA

The arduino-bridge framework requires MRAA to be cross-compiled for AArch64.

**Option A — PlatformIO target (recommended):**

```bash
# From any arduino-bridge example directory
pio run --target setup-mraa
```

Auto-detects the AArch64 toolchain prefix and installs to
`~/.local/aarch64-linux-gnu/`.

**Option B — Manual:**

```bash
# Ubuntu/Debian cross-compile host
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu cmake

CROSS_PREFIX=aarch64-linux-gnu- \
INSTALL_DIR=$HOME/.local/aarch64-linux-gnu \
./scripts/setup-mraa-cross.sh
```

### MCU Companion Sketch

Your STM32U585 sketch must register the method names that your Linux code calls.
There is no fixed registry of method names — you choose the names freely.

See `examples/arduino-bridge-blink/mcu_companion/ArduinoUnoQ_MraaCompanion.ino`
for a complete companion sketch implementing the GPIO RPC contract defined in
the [Architecture & Design Rationale](#architecture--design-rationale) section.

---

## GPIO RPC Contract

This platform defines the first standard GPIO RPC method name contract for the
Arduino Uno Q. MCU firmware that registers these names is compatible with Linux code
using the arduino-bridge framework.

| Method | Params (MsgPack map) | Returns |
|--------|----------------------|---------|
| `gpio/caps` | `{}` | capability map (call once at startup) |
| `gpio/mode` | `{"pin": N, "mode": "OUTPUT"\|"INPUT"\|"INPUT_PULLUP"\|"INPUT_PULLDOWN"}` | `true` |
| `gpio/write` | `{"pin": N, "value": 0\|1}` | `true` |
| `gpio/read` | `{"pin": N}` | `0\|1` |
| `gpio/read_many` | `{"pins": [N, ...]}` | `[0\|1, ...]` |
| `aio/read` | `{"pin": N}` | `int` (0–1023 or 0–4095) |
| `pwm/write` | `{"pin": N, "duty": 0.0–1.0}` | `true` |

> **Note:** These method names are a community convention. They require matching
> `Bridge.provide()` registrations in your MCU sketch. See the companion sketch in
> `examples/arduino-bridge-blink/mcu_companion/` for a reference implementation.

---

## Further Reading

- [Architecture & Design Rationale](#architecture--design-rationale) — dual-chip bridge design decisions (this document)
- arduino-router source: [github.com/arduino/arduino-router](https://github.com/arduino/arduino-router)
- MsgPack-RPC spec: [github.com/msgpack-rpc/msgpack-rpc](https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md)
- Zephyr board DTS: [zephyr/boards/arduino/uno_q](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_q/)

---

## Architecture & Design Rationale

### Why a Dual-Chip Bridge Instead of a Linux GPIO Framework

The Arduino Uno Q is fundamentally different from every other board in this platform.
On all other supported boards (Raspberry Pi, BeagleBone, Radxa, etc.), the application
processor directly owns the GPIO lines via `/dev/gpiochip*` — this is why lgpio,
libgpiod, pigpio, and WiringPi all work there. On the Uno Q, the Qualcomm QRB2210
(the Linux application processor) does **not** own the Arduino header pins. They are
physically wired to and owned by the STM32U585 MCU.

The only path from Linux to the Arduino header pins is through the MCU. The
arduino-router daemon on the QRB2210 maintains a persistent MsgPack-RPC connection to
the STM32 over an internal UART, exposing it as a Unix socket at
`/var/run/arduino-router.sock`. This architecture is Arduino's chosen design — it is
not a limitation of this platform port.

### Why MsgPack-RPC (Not gRPC, REST, or Raw Bytes)

The arduino-router protocol is MsgPack-RPC ([spec](https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md)).
The choice was made by the arduino-router project, not by this platform. Key properties:

- **Binary compact**: MsgPack is ~30% smaller than JSON; matters on MCU serial links
- **Schema-free**: MCU firmware registers arbitrary method names; no IDL or code generation
- **Self-framing**: MsgPack objects are self-delimiting; no length headers needed in principle
  (though this implementation adds a 4-byte length prefix for robustness — verify on hardware)
- **Bidirectional**: NOTIFICATION messages (type=2) allow MCU-initiated calls to Linux,
  enabling interrupt-driven GPIO notifications without polling

### Why This Framework Cannot Generalise Yet

The arduino-bridge framework is intentionally board-specific to the Arduino Uno Q. The
dual-chip bridge pattern (Linux MPU ↔ MCU via daemon ↔ Unix socket) could in principle
apply to other boards with a similar architecture. However, generalisation requires:

1. Confirmed hardware validation (see the Community Testing Notice at the top of this doc)
2. At least one other board using the same pattern to establish the abstraction boundary
3. Understanding the arduino-router protocol's framing behaviour on actual hardware
   (the 4-byte length prefix in `call()` vs. unframed read in `poll()` — see `ArduinoBridgeImpl.cpp`)

Until then, this framework remains `arduino_uno_q`-specific.

### Preprocessor Macros

The board definition sets two macros available in all arduino-bridge application code:

| Macro | Value | Use |
|-------|-------|-----|
| `ARDUINO_UNO_Q` | defined | Guard code to Uno Q builds: `#ifdef ARDUINO_UNO_Q` |
| `QUALCOMM_QRB2210` | defined | Guard code to QRB2210-specific behaviour |

### Experimental: `poll()` and Bidirectional Notifications

`ArduinoBridgeClass::poll()` is the MCU-to-Linux notification path. It is currently
gated behind `#ifdef ARDUINO_BRIDGE_EXPERIMENTAL` because:

- The framing protocol for notifications has not been confirmed on hardware
- The current implementation discards all-but-first notifications in a single read
- A proper streaming unpacker (`msgpack::unpacker`) is needed for production use

To use `poll()`, compile with `-DARDUINO_BRIDGE_EXPERIMENTAL`.
