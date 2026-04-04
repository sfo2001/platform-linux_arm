---
name: Hardware Validation Report
about: Report test results on physical hardware (Arduino Uno Q, new boards, etc.)
title: 'hw-validation: '
labels: hardware-validation
assignees: ''
---

## Hardware Under Test

| Field | Value |
|-------|-------|
| **Board** | <!-- e.g. Arduino Uno Q / Raspberry Pi 5 --> |
| **Board revision / serial** | <!-- if known --> |
| **Platform version** | <!-- e.g. 1.9.0 --> |
| **Framework** | <!-- e.g. arduino-bridge / lgpio --> |
| **Example tested** | <!-- e.g. arduino-bridge-blink --> |

## Test Environment

| Field | Value |
|-------|-------|
| **Host OS** | <!-- Ubuntu 24.04 / macOS 15 --> |
| **Cross-toolchain** | <!-- e.g. aarch64-linux-gnu-gcc 13.x --> |
| **Firmware / OS on board** | <!-- e.g. Arduino Uno Q Debian image v1.0 --> |

## Results

<!-- Describe what worked, what didn't, and any unexpected behaviour. -->

| Test | Result | Notes |
|------|--------|-------|
| Build (cross-compile) | ✅ / ❌ | |
| Deploy | ✅ / ❌ | |
| Runtime — basic function | ✅ / ❌ | |
| Runtime — specific feature | ✅ / ❌ | |

## Arduino Uno Q Specific (if applicable)

<!-- Fill in the open validation TODOs from docs/boards/arduino_uno_q.md -->

| Item | Verified? | Correct Value / Notes |
|------|-----------|----------------------|
| `gpio/write` method name | | |
| `gpio/read` method name | | |
| `gpio/mode` method name | | |
| `Bridge.run()` / `loop()` / `process()` | | |
| MsgPack-RPC framing (4-byte length prefix) | | |

## Full Output / Logs

```
paste relevant output here
```

## Conclusion

<!-- Summary: does this board/example work as documented? What should change in docs or code? -->
