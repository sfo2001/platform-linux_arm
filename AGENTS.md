# AGENTS.md — platform-linux_arm

AI coding assistant context for the `platform-linux_arm` PlatformIO platform.
Covers repository structure, board inventory, framework APIs, cross-compilation,
development workflow, and common gotchas.

---

## Project Overview

`platform-linux_arm` is a [PlatformIO](https://platformio.org) platform that enables
cross-compilation and deployment of C/C++ applications for Linux ARM single-board
computers (Raspberry Pi, Orange Pi, BeagleBone, Radxa, Khadas, Arduino Uno Q).

**Version:** 1.9.x | **License:** Apache 2.0

---

## Repository Structure

```text
platform-linux_arm/
├── platform.py              # PlatformIO platform entry point (Linux_armPlatform class)
├── platform_constants.py    # Architecture and toolchain prefix enums
├── boards/                  # Board definition JSON files (one per board)
├── builder/
│   ├── main.py              # Main SConscript: toolchain setup, upload, monitor, test handlers
│   ├── utils.py             # get_target_arch(), get_toolchain_prefix()
│   └── frameworks/          # One .py per framework (lgpio, libgpiod, arduino_bridge, …)
├── examples/                # 21 example projects (each is a standalone PlatformIO project)
├── scripts/                 # Setup scripts (setup-mraa-cross.sh, setup-lgpio-cross.sh, …)
├── tests/                   # Python unit tests (pytest) for builder scripts
│                            #   and C unit tests (CMake/ctest) for framework C code
│   └── stubs/               # C sysfs stubs for link-seam unit testing
└── docs/                    # Documentation (boards, frameworks, security, upload, etc.)
```

---

## Board Inventory

| Board ID | Name | Arch | Frameworks |
|----------|------|------|------------|
| `raspberrypi_1b` | Raspberry Pi 1 Model B | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_2b` | Raspberry Pi 2 Model B | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_3b` | Raspberry Pi 3 Model B | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_4b` | Raspberry Pi 4 Model B | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_5` | Raspberry Pi 5 | armv7\* | lgpio, libgpiod, wiringpi |
| `raspberrypi_400` | Raspberry Pi 400 | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_cm4` | Raspberry Pi CM4 | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_zero` | Raspberry Pi Zero | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `raspberrypi_zero2w` | Raspberry Pi Zero 2W | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `orangepi_zero` | Orange Pi Zero | armv7 | lgpio, libgpiod, pigpio, wiringpi |
| `beaglebone_black` | BeagleBone Black | armv7 | lgpio, libgpiod |
| `khadas_vim3` | Khadas VIM3 | aarch64 | lgpio, libgpiod |
| `radxa_rock3a` | Radxa Rock 3A | aarch64 | lgpio, libgpiod |
| `arduino_uno_q` | Arduino Uno Q | aarch64 | arduino-bridge |

\* Pi 5 defaults to armv7 cross-compile; override with `board_build.arch = aarch64` for native 64-bit.

**pigpio note:** Not supported on Raspberry Pi 5 (RP1 I/O controller incompatible).

---

## Frameworks

| Framework | Description | Use case |
|-----------|-------------|----------|
| `lgpio` | Modern GPIO via `/dev/gpiochipN` (kernel 4.8+) | All Pi models incl. Pi 5, recommended for new projects |
| `libgpiod` | Kernel GPIO character device library | Pi 5, non-RPi SBCs, modern alternative to lgpio |
| `wiringpi` | Classic RPi GPIO library | Legacy projects; unmaintained upstream |
| `pigpio` | RPi-only, daemon-based GPIO | Pi 1–4 only; NOT Pi 5 |
| `arduino-bridge` | MsgPack-RPC over Unix socket to STM32U585 MCU | Arduino Uno Q board only |
| *(none)* | Bare-metal: no framework, pure Linux C/C++ | Simple executables, no GPIO |

---

## Architecture Override

Any armv7 board can be cross-compiled as aarch64 (if the SoC is 64-bit capable)
by adding to `platformio.ini`:

```ini
board_build.arch = aarch64
```

This is how Pi 5 64-bit builds work: `board = raspberrypi_5` +
`board_build.arch = aarch64`.

---

## Builder API Patterns

Framework builders live in `builder/frameworks/`. Each is a Python SCons script.

**Accessing the environment:**

```python
from SCons.Script import DefaultEnvironment
env = DefaultEnvironment()
```

**Detecting target architecture:**

```python
from utils import get_target_arch
target_arch = get_target_arch(env)   # returns "armv7" or "aarch64"
is_aarch64 = target_arch == "aarch64"
```

**Reading board config:**

```python
board = env.BoardConfig()
mcu = board.get("build.mcu", "")
arch = board.get("build.arch", "armv7")
```

**Adding compile flags / libraries:**

```python
env.Append(
    CPPPATH=["/path/to/include"],
    LIBS=["lgpio"],
    LIBPATH=["/path/to/lib"],
    CCFLAGS=["-march=armv7-a"],
)
```

**Toolchain prefix** (`aarch64-linux-gnu-` or `arm-linux-gnueabihf-`) is set in
`builder/main.py` via `env.Replace(_BINPREFIX=prefix)`. Framework builders read
it via `env["_BINPREFIX"]`.

**Installed library paths** follow this convention:

- armv7: `~/.local/arm-linux-gnueabihf/`
- aarch64: `~/.local/aarch64-linux-gnu/`

---

## Cross-Compilation Setup

### Toolchains

```bash
# Linux (Ubuntu/Debian)
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf        # ARMv7
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu             # AArch64

# macOS (Homebrew)
brew tap messense/macos-cross-toolchains
brew install arm-unknown-linux-gnueabihf aarch64-unknown-linux-gnu
```

### Framework Libraries

**lgpio** (required for `lgpio` framework):

```bash
./scripts/setup-lgpio-cross.sh                                           # ARMv7
CROSS_PREFIX=aarch64-linux-gnu- INSTALL_DIR=$HOME/.local/aarch64-linux-gnu \
  ./scripts/setup-lgpio-cross.sh                                         # AArch64
```

**MRAA** (required for `arduino-bridge` framework):

```bash
# Recommended — auto-detects toolchain, from any arduino-bridge project directory:
pio run --target setup-mraa

# Or manually:
CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh           # AArch64
```

**libgpiod** (required for `libgpiod` framework):

```bash
./scripts/setup-libgpiod-cross.sh                                        # ARMv7/AArch64
```

---

## Development Workflow

### Building an example

```bash
cd examples/lgpio-blink
pio run                          # build default env
pio run -e raspberrypi_4b        # build specific env
pio run --target clean            # clean
```

### Running tests

```bash
# Python builder tests (from repo root)
pytest tests/

# With coverage
pytest tests/ --cov=builder --cov-report=term-missing
```

### Installing platform in dev mode (live edits)

```bash
pio pkg install --global --platform symlink://.
```

### Deploy to board

```bash
# In any example with upload config in platformio.ini:
pio run -e raspberrypi_4b_upload --target upload
```

---

## Testing

Python unit tests live in `tests/`. They test builder script logic without
running a full PlatformIO build. Run with `pytest`.

CI runs tests on ubuntu-latest, macos-latest, windows-latest with Python
3.10, 3.11, 3.12 (see `.github/workflows/tests.yml`).

Example builds are validated by `.github/workflows/examples.yml` across the
same OS matrix.

---

## Commit Conventions

Follows [Conventional Commits](https://www.conventionalcommits.org/).

**Format:** `<type>(<scope>): <subject>`

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

**Defined scopes** (use only these):

| Scope | When |
|-------|------|
| `arch` | 32-bit/64-bit architecture support |
| `boards` | Board definition JSON files |
| `ci` | GitHub Actions workflows |
| `config` | Platform config file support |
| `debug` | GDB/SSH remote debugging |
| `docs` | Documentation |
| `examples` | Example projects |
| `frameworks` | Framework support (generic) |
| `lgpio` | lgpio-specific changes |
| `libgpiod` | libgpiod-specific changes |
| `monitor` | SSH serial monitor |
| `onboarding` | First-run welcome and setup |
| `pigpio` | pigpio-specific changes |
| `platform` | Platform core changes |
| `scripts` | Build and setup scripts |
| `security` | Security hardening |
| `test` | Remote test execution |
| `toolchain` | Cross-compilation toolchain |
| `upload` | Remote deploy (scp/rsync/ssh) |
| `vscode` | VS Code integration |
| `wiringpi` | wiringpi-specific changes |
| `arduino-bridge` | arduino-bridge framework / Arduino Uno Q |

---

## CI Overview

| Workflow | Trigger | What it does |
|----------|---------|-------------|
| `examples.yml` | push, PR | Builds all 21 examples × {ubuntu, macos, windows} |
| `tests.yml` | push, PR | Python pytest × {ubuntu, macos, windows} × Python {3.10, 3.11, 3.12} |
| `release.yml` | tag push | Publishes platform package |

---

## Common Gotchas

**MRAA not found during arduino-bridge build**
Run `pio run --target setup-mraa` from the example directory (auto-detects toolchain).
Or manually: `CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh` from the repo root.

**Wrong architecture library picked**
`get_target_arch()` checks `board_build.arch` from `platformio.ini` before the board
default. Always set `board_build.arch = aarch64` explicitly when targeting 64-bit.

**pigpio on Pi 5**
pigpio does not work on Raspberry Pi 5. Use `lgpio` or `libgpiod` instead. The
`raspberrypi_5` board definition intentionally excludes pigpio from its framework list.

**lgpio missing on host**
lgpio is a target-side library. You cross-compile it once via `setup-lgpio-cross.sh`
and the builder picks it up from `~/.local/arm-linux-gnueabihf/` or
`~/.local/aarch64-linux-gnu/`.

**arduino-bridge runtime**
The compiled binary requires `arduino-router` daemon running on the Arduino Uno Q:
`systemctl status arduino-router`. The socket path defaults to
`/var/run/arduino-router.sock` (override: `ARDUINO_ROUTER_SOCKET` env var).

**Platform install for local dev**
After editing `platform.py` or builder scripts, no reinstall is needed if you
installed with `pio pkg install --global --platform symlink://.`.

---

## Key Documentation

- [`docs/boards/arduino_uno_q.md`](docs/boards/arduino_uno_q.md) — Arduino Uno Q full setup
- [`docs/UPLOAD.md`](docs/UPLOAD.md) — Remote deploy reference
- [`docs/SECURITY.md`](docs/SECURITY.md) — Security model and SSH hardening
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — Contribution guidelines and commit scopes
- [`examples/README.md`](examples/README.md) — Example index
