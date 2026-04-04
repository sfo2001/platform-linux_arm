# Arduino Bridge Blink

This example demonstrates the `arduino-bridge` framework: a Linux C++ program on the
Arduino Uno Q's application processor (AArch64) controlling the MCU's GPIO via
MsgPack-RPC over a Unix socket.

> **Community Testing Notice:** The RPC method names (`gpio/mode`, `gpio/write`,
> `aio/read`) and parameter formats have not been validated on physical hardware.
> Please open an issue with your test results.

## What It Does

1. Connects to the `arduino-router` daemon running on the board
2. Sets MCU pin D13 (built-in LED) to OUTPUT mode via `gpio/mode`
3. Blinks D13 five times (1 second on, 1 second off) via `gpio/write`
4. Reads analog pin A0 via `aio/read`
5. Disconnects

The Linux host process calls MCU methods defined in the companion Arduino sketch
(`mcu_companion/ArduinoUnoQ_MraaCompanion.ino`). The two sides communicate over
`/var/run/arduino-router.sock`.

## Prerequisites

### Build-time (on development machine)

1. **MRAA cross-compiled for AArch64:**
   ```bash
   CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh
   ```
   See [CONTRIBUTING.md](../../CONTRIBUTING.md#5-set-up-mraa-for-cross-compilation-arduino-bridge-optional) for full setup.

2. **msgpack-cxx headers** (on the development machine):
   ```bash
   # Linux
   sudo apt install libmsgpack-cxx-dev

   # macOS
   brew install msgpack-cxx
   ```

### Runtime (on the Arduino Uno Q board)

1. **MCU companion sketch flashed** to the STM32U585:
   Flash `mcu_companion/ArduinoUnoQ_MraaCompanion.ino` using the Arduino IDE
   or Arduino CLI targeting the Arduino Uno Q MCU.

2. **`arduino-router` daemon running:**
   ```bash
   systemctl status arduino-router
   # If not running:
   systemctl start arduino-router
   ```

## Building

```bash
pio run -e arduino_uno_q

# Clean build artifacts
pio run --target clean
```

The compiled binary is at `.pio/build/arduino_uno_q/program`.

## Running

Transfer the binary to the board and run it:

```bash
# Copy to board
scp .pio/build/arduino_uno_q/program user@uno-q-host:~/bridge_blink

# Run on board
ssh user@uno-q-host ./bridge_blink
```

Expected output:

```
arduino-bridge-blink: Arduino Uno Q example
Connecting to arduino-router...
Connected.

gpio/mode pin=13 mode=OUTPUT: OK
Blinking D13 five times...
  gpio/write pin=13 value=1 (LED ON)
  gpio/write pin=13 value=0 (LED OFF)
  ...

aio/read pin=A0 (pin=0): value=512

Done.
```

## Upload via PlatformIO

Uncomment the upload section in `platformio.ini` to deploy directly:

```ini
upload_protocol = scp
upload_port = user@uno-q-host
upload_path = ~/bridge_blink
upload_run_after = true
```

Then run:

```bash
pio run -e arduino_uno_q --target upload
```

## Architecture

```
Development machine (x86_64 / macOS / Windows)
    └── pio run → cross-compile AArch64 binary

Arduino Uno Q (AArch64 Linux)
    ├── bridge_blink  ←→  /var/run/arduino-router.sock  ←→  arduino-router
    │   (this program)                                        (daemon)
    │                                                              │
    │                                                         STM32U585 MCU
    │                                                              │
    │                                                         D13 LED / A0 pin
    └── (GPIO controlled via MsgPack-RPC, not directly)
```

## Troubleshooting

**`Failed to connect to arduino-router socket`**
- Check the daemon: `systemctl status arduino-router`
- Check the socket: `ls -la /var/run/arduino-router.sock`
- Override socket path: `ARDUINO_ROUTER_SOCKET=/path/to/sock ./bridge_blink`

**`MRAA not found` during build**
- Run `CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh` from the repo root

## References

- [Arduino Uno Q board documentation](../../docs/boards/arduino_uno_q.md)
- [arduino-bridge framework](../../builder/frameworks/arduino_bridge.py)
- [Companion MCU sketch](mcu_companion/)
- [arduino-uno-q-hello](../arduino-uno-q-hello/) — bare-metal example without GPIO
