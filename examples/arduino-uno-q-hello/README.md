# Arduino Uno Q — Hello World (Bare-Metal AArch64)

This example demonstrates a bare-metal C application targeting the Arduino Uno Q's
application processor: a Qualcomm QRB2210 (4x Cortex-A53, AArch64). No GPIO framework
is used — this is a pure Linux userspace program.

> **Community Testing Notice:** This board port has not been validated on physical
> hardware. Please open an issue with your test results.

## About the Arduino Uno Q

The Arduino Uno Q is an Arduino form-factor board powered by a QRB2210 SoC running
Debian Linux AArch64. It has two sides:

- **Application processor (AArch64)** — runs Linux, this is where your PlatformIO code runs
- **MCU (STM32U585)** — handles real-time GPIO; reached via the `arduino-bridge` framework

This hello-world example targets the application processor only. For GPIO access, see
the [`arduino-bridge-blink`](../arduino-bridge-blink/) example.

## Hardware Requirements

- Arduino Uno Q
- SSH access to the board (Ethernet or Wi-Fi configured)

## System Requirements

Cross-compiler for AArch64 on your development machine:

```bash
# Linux (Ubuntu/Debian)
sudo apt install gcc-aarch64-linux-gnu

# macOS (Homebrew)
brew tap messense/macos-cross-toolchains
brew install aarch64-unknown-linux-gnu
```

## Building

```bash
# Build for Arduino Uno Q
pio run -e arduino_uno_q

# Clean build artifacts
pio run --target clean
```

The compiled binary is at `.pio/build/arduino_uno_q/program`.

## Running

Transfer the binary to the board and run it over SSH:

```bash
# Copy to board
scp .pio/build/arduino_uno_q/program user@uno-q-host:~/hello_uno_q

# Run on board
ssh user@uno-q-host ./hello_uno_q
```

Expected output:

```
Hello from Arduino Uno Q!
Board: Arduino Uno Q (QRB2210 AArch64)
MCU: Qualcomm QRB2210 (4x Cortex-A53 @ 2.0 GHz)
OS:  Debian Linux (AArch64)

Note: GPIO requires the arduino-router daemon and
      the arduino-bridge framework (Phase 2).
      See docs/boards/arduino_uno_q.md for details.
```

## Upload via PlatformIO

Uncomment and configure the upload section in `platformio.ini` to deploy directly:

```ini
upload_protocol = scp
upload_port = user@uno-q-host
upload_path = /tmp/hello_uno_q
upload_run_after = true
```

Then run:

```bash
pio run -e arduino_uno_q --target upload
```

## References

- [Arduino Uno Q board documentation](../../docs/boards/arduino_uno_q.md)
- [arduino-bridge-blink](../arduino-bridge-blink/) — GPIO example using the MCU
