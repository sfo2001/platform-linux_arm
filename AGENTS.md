# AGENTS.md — platform-linux_arm

AI coding assistant context for the `platform-linux_arm` PlatformIO platform.
Covers repository structure, board inventory, framework APIs, cross-compilation,
development workflow, and common gotchas.

---

## Project Overview

`platform-linux_arm` is a [PlatformIO](https://platformio.org) platform that enables
cross-compilation and deployment of C/C++ applications for Linux ARM single-board
computers (Raspberry Pi, Orange Pi, BeagleBone, Radxa, Khadas, Arduino Uno Q).

**Version:** 2.0.x | **License:** Apache 2.0

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
│   ├── test_platform.py     # pytest: builder script unit tests (83 tests)
│   ├── test_pwm_hal.c       # ctest: PWM HAL C unit tests (61 tests, no hardware needed)
│   └── stubs/
│       ├── pwm-hal-sysfs-stub.c  # Link-seam stub — replaces /sys/class/pwm/ with in-memory table
│       └── pwm-hal-sysfs-stub.h  # Stub control API (stub_reset, stub_set_pi5, stub_set_export_delay)
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

### Agent-Driven Dev Loop

The `dev-loop` target chains build → upload → monitor in one command
with structured JSON output. Designed for AI agent iteration loops.

```bash
# Run complete dev loop
pio run --target dev-loop

# With specific environment
pio run -e raspberrypi_4b_upload --target dev-loop
```

**Configuration** in `platformio.ini`:

```ini
[env:raspberrypi_4b_upload]
platform = linux_arm
board = raspberrypi_4b
upload_protocol = scp
upload_port = pi@raspberrypi.local:/home/pi/myapp
dev_loop_monitor_timeout = 30   ; seconds (default: 30)
upload_run_command = ./myapp --flag  ; optional: custom remote command
```

> **Security:** `upload_run_command` is passed verbatim through the remote shell.
> Shell metacharacters (`;`, `&&`, `|`, backticks) in its value will execute arbitrary
> commands on the remote host. Only set values you authored — never derive this option
> from untrusted external input.

**Structured JSON output** — extract between `--- DEV_LOOP_RESULT ---` delimiters:

```json
{
  "schema_version": "1",
  "phases": {
    "build": { "status": "pass" },
    "upload": { "status": "pass", "error": null },
    "monitor": {
      "status": "pass",
      "exit_code": 0,
      "timed_out": false,
      "timeout_seconds": 30,
      "output": "Hello from ARM!\n"
    }
  },
  "overall_status": "pass",
  "failure_phase": null,
  "elapsed_seconds": 18.4,
  "timestamp_iso": "2026-04-05T14:23:11+02:00"
}
```

The JSON is also written to `.pio/build/<env>/dev-loop-result.json`.

**Agent parsing guidance:**

- Extract JSON between the two `--- DEV_LOOP_RESULT ---` lines
- Check `overall_status` first: `"pass"` or `"fail"`
- If `"fail"`, check `failure_phase` (`"upload"` or `"monitor"`)
- `phases.monitor.status` has three possible values: `"pass"`, `"fail"`, `"timeout"`
- `monitor.timed_out == true` means program ran for the full timeout; `status` will be `"timeout"` (not `"fail"`)
- If upload phase fails, `phases.monitor` is omitted (never ran)

**Error handling:**

- On SSH failure: `failure_phase` is `"upload"`, check `phases.upload.error`
- Do not retry faster than every 5 seconds (avoids SSH connection storms)
- The dev loop is idempotent — binary is overwritten on each upload

---

## Branch Workflow

`develop` and `main` are **protected branches**. Direct pushes are rejected.
CI must be green before any branch can merge into `develop`.

### Rules (no exceptions)

1. **Never commit directly to `develop` or `main`** — even for a one-liner.
2. **Never use `--no-verify`** — hook failures are signals, not noise. If a hook
   fails, fix the root cause. Bypassing it hides toolchain drift that will break CI.
3. **Verify toolchain parity before starting any work:**

   ```bash
   pre-commit run --all-files
   ```

   If this fails on a clean checkout, fix the toolchain mismatch first as a
   separate commit before making any product changes.
4. **Branch naming:** `fix/NNN-short-description`, `feat/NNN-short-description`,
   `chore/description`, `style/description` — where NNN is the issue number if one exists.
5. **CI must pass on the branch** before merging into `develop`.

### Workflow

```bash
git checkout develop && git pull
git checkout -b fix/119-pwm-init-sentinel    # branch off develop
pre-commit run --all-files                   # verify toolchain is clean
# ... make changes, commit (hooks must pass) ...
git push -u origin fix/119-pwm-init-sentinel
# wait for CI green, then merge
```

### Why this matters

A broken toolchain on `develop` (e.g. mismatched black line-length between
pre-commit and CI) is invisible until CI runs. Working through a branch means CI
catches the problem on the branch before develop is touched. A dirty develop
history is the cost of skipping this step.

---

## Testing

### Python Unit Tests

Python unit tests live in `tests/`. They test builder script logic without
running a full PlatformIO build. Run with `pytest`.

CI runs tests on ubuntu-latest, macos-latest, windows-latest with Python
3.10, 3.11, 3.12 (see `.github/workflows/tests.yml`).

### C Unit Tests (CMake)

The `framework-lgpio/pwm-hal` module has a C unit test suite (`tests/test_pwm_hal.c`)
that runs without Raspberry Pi hardware. A link-seam stub (`tests/stubs/pwm-hal-sysfs-stub.c`)
replaces all `/sys/class/pwm` I/O with in-memory state.

Build and run:

```bash
cmake -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

CI job: `cpp-tests` in `.github/workflows/examples.yml`.

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
| `dev-loop` | Dev-loop composite build/upload/monitor target |
| `docs` | Documentation |
| `examples` | Example projects |
| `frameworks` | Framework support (generic) |
| `lgpio` | lgpio-specific changes |
| `pwm-hal` | PWM HAL (`framework-lgpio/pwm-hal.c`) changes |
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
| `examples.yml` | push, PR | C unit tests (CMake/ctest, 61 tests, ubuntu-latest) |
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
