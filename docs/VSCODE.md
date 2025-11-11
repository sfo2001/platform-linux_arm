# VS Code Integration Guide

**Platform:** platform-linux_arm
**Last Updated:** 2025-11-11

This guide explains how to use Visual Studio Code with the platform-linux_arm PlatformIO platform for developing Linux ARM applications (including Raspberry Pi).

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [IntelliSense Configuration](#intellisense-configuration)
- [Debugging](#debugging)
- [Build Tasks](#build-tasks)
- [Troubleshooting](#troubleshooting)
- [Advanced Configuration](#advanced-configuration)

---

## Overview

The platform-linux_arm platform integrates seamlessly with VS Code through the **PlatformIO IDE extension**. Unlike some development environments, PlatformIO uses **automatic configuration generation** rather than static configuration files.

### How It Works

```
platformio.ini → PlatformIO Extension → VS Code Configuration
     ↓                    ↓                        ↓
  Board           Toolchain Paths          c_cpp_properties.json
  Flags           Include Paths            launch.json
  Framework       Debug Tools              tasks.json
```

**Key Points:**
- Configuration files (`.vscode/*.json`) are **auto-generated** when you open a project
- Manual edits to auto-generated files **may be overwritten** (by design)
- Platform-specific settings come from `platformio.ini`, board definitions, and the platform itself
- This is the **standard approach** used by all major PlatformIO platforms (ststm32, espressif32, etc.)

---

## Getting Started

### Prerequisites

1. **Install VS Code**
   ```bash
   # Download from https://code.visualstudio.com/
   # Or use package manager:
   sudo snap install code --classic  # Ubuntu/Debian
   ```

2. **Install PlatformIO IDE Extension**
   - Open VS Code
   - Press `Ctrl+Shift+X` (Extensions)
   - Search for "PlatformIO IDE"
   - Click Install
   - Restart VS Code

3. **Install Cross-Compilation Toolchain** (if building on non-ARM machine)
   ```bash
   # Ubuntu/Debian
   sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf gdb-multiarch

   # macOS
   brew install arm-linux-gnueabihf-binutils
   ```

### Create or Open a Project

**Option 1: Create New Project**
1. Click PlatformIO icon in sidebar
2. Click "New Project"
3. Name: `my-pi-project`
4. Board: Search for "Raspberry Pi" and select your model
5. Framework: Choose `wiringpi`, `lgpio`, or `none` (bare metal)
6. Click "Finish"

**Option 2: Open Existing Project**
1. `File → Open Folder`
2. Select folder containing `platformio.ini`
3. PlatformIO automatically detects and configures the project

**What Happens Automatically:**
- `.vscode/c_cpp_properties.json` is generated for IntelliSense
- `.vscode/extensions.json` recommends PlatformIO IDE
- Build tasks are configured
- Debug configurations are prepared

---

## IntelliSense Configuration

### How IntelliSense Works

IntelliSense (code completion, go-to-definition, error checking) is configured automatically based on your `platformio.ini` settings.

### Automatic Configuration

When you open a PlatformIO project, the extension:

1. **Detects your toolchain:**
   - Finds `arm-linux-gnueabihf-gcc` (cross-compilation)
   - Or uses system GCC (native ARM compilation)

2. **Extracts compiler settings:**
   - Include paths from framework packages
   - Defines/macros from `build_flags`
   - Compiler arguments from board definition

3. **Generates `c_cpp_properties.json`:**
   ```json
   {
     "configurations": [
       {
         "name": "PlatformIO",
         "includePath": [
           "${workspaceFolder}/include",
           "${workspaceFolder}/src",
           "${platformio.packages_dir}/framework-lgpio/include"
         ],
         "defines": [
           "RASPBERRYPI",
           "RASPBERRYPI4"
         ],
         "compilerPath": "/usr/bin/arm-linux-gnueabihf-gcc",
         "cStandard": "c11",
         "cppStandard": "c++17",
         "intelliSenseMode": "gcc-arm"
       }
     ]
   }
   ```

### Customizing IntelliSense via platformio.ini

**Add custom include paths:**
```ini
[env:raspberrypi_4b]
platform = linux_arm
board = raspberrypi_4b
framework = lgpio

; Custom include directories for IntelliSense
build_flags =
    -I/opt/custom/include
    -I${PROJECT_DIR}/external/headers
    -DCUSTOM_DEFINE=1
    -DDEBUG_MODE
```

**Add library dependencies:**
```ini
lib_deps =
    somelib@1.0.0
    https://github.com/user/library.git
```

**Change C/C++ standard:**
```ini
build_unflags = -std=gnu11
build_flags =
    -std=c17
    -std=c++20
```

### IntelliSense Modes

For ARM cross-compilation, the extension may use:
- `gcc-arm` - ARM GCC mode (recommended)
- `gcc-x64` - Generic GCC mode (fallback)
- `linux-gcc-arm` - Linux ARM GCC mode

**Setting is automatic** based on detected toolchain.

---

## Debugging

The platform-linux_arm platform provides **full remote debugging support** via GDB over SSH.

### Quick Start: Debug Workflow

1. **Configure platformio.ini:**
   ```ini
   [env:debug]
   platform = linux_arm
   board = raspberrypi_4b
   framework = lgpio

   ; Build with debug symbols
   build_type = debug
   build_flags = -O0 -g3 -ggdb

   ; Upload via SCP
   upload_protocol = scp
   upload_port = pi@raspberrypi.local:/home/pi/myapp

   ; Remote debugging
   debug_tool = gdbserver-ssh
   debug_port = pi@raspberrypi.local
   ```

2. **Build and Upload:**
   - Press `Ctrl+Alt+B` (Build)
   - Or click "Build" in PlatformIO toolbar
   - Upload: `Ctrl+Alt+U` or click "Upload"

3. **Start Debugging:**
   - Press `F5` or click "Start Debugging"
   - **PlatformIO automatically:**
     - Opens SSH connection to Raspberry Pi
     - Launches `gdbserver` on the target
     - Connects GDB to the remote server
     - Loads your program with debug symbols
     - Stops at `main()` or first breakpoint

### Debug Controls (VS Code)

| Action | Keyboard | Description |
|--------|----------|-------------|
| Continue | `F5` | Run until next breakpoint |
| Step Over | `F10` | Execute current line, skip function internals |
| Step Into | `F11` | Step into function calls |
| Step Out | `Shift+F11` | Return from current function |
| Restart | `Ctrl+Shift+F5` | Restart debugging session |
| Stop | `Shift+F5` | Stop debugging |

### Setting Breakpoints

1. **Line Breakpoint:**
   - Click in the left gutter next to line number
   - Red dot appears
   - Program pauses when reaching this line

2. **Conditional Breakpoint:**
   - Right-click in gutter
   - Choose "Add Conditional Breakpoint"
   - Enter condition: `i == 10` or `ptr != NULL`

3. **Function Breakpoint:**
   - Debug sidebar → Breakpoints section
   - Click "+" next to "Function Breakpoints"
   - Enter function name: `setup` or `loop`

### Debug Panels

**Variables Panel:**
- Automatically shows local variables
- Expands structures and arrays
- Updates as you step through code

**Watch Panel:**
- Add expressions to monitor: `sensor_value`, `counter * 2`, `&my_struct`
- Evaluates on every step
- Right-click variable → "Add to Watch"

**Call Stack Panel:**
- Shows function call hierarchy
- Click frames to inspect variables at different call levels
- See where execution came from

**Debug Console:**
- Execute GDB commands directly:
  ```
  -exec print my_variable
  -exec info registers
  -exec backtrace
  ```
- Evaluate expressions: Type variable names or expressions

### Debug Configuration (Advanced)

PlatformIO automatically generates `.vscode/launch.json`, but you can customize it:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "platformio-debug",
      "request": "launch",
      "name": "PIO Debug (debug)",
      "executable": ".pio/build/debug/program",
      "projectEnvName": "debug",
      "toolchainBinDir": "",
      "preLaunchTask": {
        "type": "PlatformIO",
        "task": "Pre-Debug"
      },
      "internalConsoleOptions": "openOnSessionStart"
    }
  ]
}
```

**Custom configurations are preserved** when the extension regenerates the file (PlatformIO Core 5.1.1+).

### Architecture-Specific Debugging

The platform automatically selects the correct GDB:

| Target Architecture | GDB Binary | Detected From |
|---------------------|------------|---------------|
| ARMv7 (32-bit) | `arm-linux-gnueabihf-gdb` | Board definition |
| AArch64 (64-bit) | `aarch64-linux-gnu-gdb` | Board definition |
| Native ARM | `gdb` (system) | Host detection |

**Examples:**
- Raspberry Pi 4 with 32-bit OS → `arm-linux-gnueabihf-gdb`
- Raspberry Pi 5 with 64-bit OS → `aarch64-linux-gnu-gdb`
- Building natively on Pi → system `gdb`

### See Also

- [DEBUGGING.md](DEBUGGING.md) - Comprehensive remote debugging guide
- [examples/remote-debugging/](../examples/remote-debugging/) - Working example project

---

## Build Tasks

PlatformIO provides integrated build tasks in VS Code.

### Access Tasks

**Via Menu:**
- `Terminal → Run Task → PlatformIO:`

**Via Command Palette:**
- Press `Ctrl+Shift+P`
- Type "Tasks: Run Task"
- Select PlatformIO task

**Via Keyboard Shortcuts:**
| Task | Shortcut | Description |
|------|----------|-------------|
| Build | `Ctrl+Alt+B` | Compile project |
| Upload | `Ctrl+Alt+U` | Upload to target |
| Clean | `Ctrl+Alt+C` | Remove build files |
| Test | `Ctrl+Alt+T` | Run unit tests |
| Serial Monitor | `Ctrl+Alt+S` | Open serial monitor |

### Available Tasks

```
PlatformIO: Build
PlatformIO: Upload
PlatformIO: Upload and Monitor
PlatformIO: Clean
PlatformIO: Test
PlatformIO: Upload using Programmer
PlatformIO: Check (static analysis)
PlatformIO: Pre-Debug (build with debug symbols)
```

### Task Configuration

Tasks are automatically configured, but you can create custom tasks in `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "PlatformIO",
      "task": "Build",
      "problemMatcher": ["$platformio"],
      "label": "PlatformIO: Build"
    },
    {
      "label": "Build and Upload to Pi",
      "type": "shell",
      "command": "pio",
      "args": [
        "run",
        "--target", "upload",
        "--environment", "raspberrypi_4b"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

---

## Troubleshooting

### IntelliSense Not Working

**Symptoms:**
- Red squiggly lines under valid code
- "Cannot find header file" errors
- No autocomplete suggestions
- Go-to-definition doesn't work

**Solutions:**

1. **Rebuild IntelliSense Index**
   - Open Command Palette: `Ctrl+Shift+P`
   - Run: `PlatformIO: Rebuild IntelliSense Index`
   - Wait for completion (status bar shows progress)
   - Restart VS Code if needed

2. **Check Toolchain Installation**
   ```bash
   # Verify cross-compiler is installed
   which arm-linux-gnueabihf-gcc
   arm-linux-gnueabihf-gcc --version

   # Verify GDB for debugging
   which arm-linux-gnueabihf-gdb
   ```

3. **Verify c_cpp_properties.json**
   - Open `.vscode/c_cpp_properties.json`
   - Check `compilerPath` points to valid compiler
   - Verify `includePath` contains your source directories
   - Ensure `defines` match your `platformio.ini` build_flags

4. **Check C/C++ Extension Configuration**
   - `File → Preferences → Settings`
   - Search: `C_Cpp.default.configurationProvider`
   - Should be: `platformio-ide` or `ms-vscode.cpptools`

5. **Force Regeneration**
   ```bash
   # Delete auto-generated file
   rm .vscode/c_cpp_properties.json

   # Reload VS Code window
   # Ctrl+Shift+P → "Developer: Reload Window"
   # File is regenerated automatically
   ```

### IntelliSense Shows Warnings on Host System

**Problem:**
Cross-compiling for ARM on x86_64 host may show IntelliSense warnings:
- "Unknown target CPU architecture"
- Different system headers
- Macro definition mismatches

**This is expected behavior.** Your code compiles correctly for ARM target even if IntelliSense shows warnings based on host architecture.

**Solutions:**

**Option 1: Accept Warnings (Recommended)**
- Code compiles correctly despite warnings
- Focus on build output, not IntelliSense warnings
- Test on actual target device

**Option 2: Native Compilation on Raspberry Pi**
- Run PlatformIO directly on Raspberry Pi
- IntelliSense uses native ARM toolchain
- No cross-compilation warnings

**Option 3: Suppress Specific Warnings**
Add to `platformio.ini`:
```ini
build_flags =
    -Wno-unknown-pragmas
    -Wno-attributes
```

### Debugging Won't Start

**Check SSH Connection:**
```bash
# Test SSH to target
ssh pi@raspberrypi.local

# Verify gdbserver is available on target
ssh pi@raspberrypi.local "which gdbserver"
```

**Check Debug Configuration:**
```ini
; Verify these are set correctly
debug_tool = gdbserver-ssh
debug_port = pi@raspberrypi.local  ; SSH connection string

; Must match upload configuration
upload_port = pi@raspberrypi.local:/path/to/program
```

**Common Issues:**

1. **"gdbserver not found"**
   ```bash
   # Install on Raspberry Pi
   ssh pi@raspberrypi.local
   sudo apt install gdbserver
   ```

2. **"Permission denied (publickey)"**
   - Setup SSH key authentication
   - Or add password: `debug_port = pi:password@raspberrypi.local`
   - See [DEBUGGING.md](DEBUGGING.md) for SSH setup

3. **"Cannot execute binary"**
   - Check architecture mismatch (32-bit vs 64-bit)
   - Verify cross-compiler matches target OS
   - Rebuild with correct board definition

4. **Breakpoints Not Hit**
   - Ensure `build_type = debug` is set
   - Add `-g3 -ggdb` to `build_flags`
   - Check optimization level: `-O0` (no optimization) for debugging

### Build Errors in VS Code

**Check Build Output:**
- Open Terminal panel: `Ctrl+` ` (backtick)
- Select "PlatformIO" from terminal dropdown
- Review compiler errors

**Common Issues:**

1. **"Toolchain not found"**
   ```bash
   # Install cross-compiler
   sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
   ```

2. **"Framework not found"**
   ```bash
   # Install platform packages
   pio pkg install --platform linux_arm
   ```

3. **Missing Dependencies:**
   ```ini
   # Add to platformio.ini
   lib_deps =
       required-library@^1.0.0
   ```

### Upload Fails

**Check Upload Configuration:**
```ini
upload_protocol = scp  ; or rsync, ssh
upload_port = pi@raspberrypi.local:/home/pi/myapp
upload_ssh_port = 22
upload_ssh_key = ~/.ssh/id_rsa
```

**Test Manually:**
```bash
# Test SCP transfer
scp .pio/build/raspberrypi_4b/program pi@raspberrypi.local:/home/pi/

# Test SSH execution
ssh pi@raspberrypi.local "chmod +x /home/pi/program && /home/pi/program"
```

See [UPLOAD.md](UPLOAD.md) for comprehensive upload troubleshooting.

### Extension Not Working

1. **Check PlatformIO Installation:**
   - Open PlatformIO sidebar
   - Click "PIO Home" → "Open"
   - Should show PlatformIO welcome screen

2. **Verify PlatformIO Core:**
   ```bash
   # Check installation
   pio --version

   # Should show: PlatformIO Core, version X.X.X
   ```

3. **Reinstall Extension:**
   - `Ctrl+Shift+X` (Extensions)
   - Find "PlatformIO IDE"
   - Click gear icon → Uninstall
   - Restart VS Code
   - Reinstall extension

4. **Check Extension Logs:**
   - `View → Output`
   - Select "PlatformIO" from dropdown
   - Look for error messages

---

## Advanced Configuration

### Multi-Environment Workflows

Manage different configurations for development, testing, and production:

```ini
; Development: Fast builds, debugging enabled
[env:dev]
platform = linux_arm
board = raspberrypi_4b
build_type = debug
build_flags = -O0 -g3 -DDEBUG_MODE
upload_port = pi@pi-dev.local:/home/pi/app
debug_tool = gdbserver-ssh
debug_port = pi@pi-dev.local

; Testing: Optimized with logging
[env:test]
platform = linux_arm
board = raspberrypi_4b
build_flags = -O2 -DLOGGING_ENABLED
upload_port = pi@pi-test.local:/home/pi/app

; Production: Fully optimized, no debug
[env:prod]
platform = linux_arm
board = raspberrypi_4b
build_type = release
build_flags = -O3 -DNDEBUG
upload_port = pi@pi-prod.local:/home/pi/app
```

**Switch environments:**
- Status bar (bottom) → Click current environment
- Or: PlatformIO sidebar → "Switch Environment"

### Custom IntelliSense Configuration

Preserve custom IntelliSense settings by adding them **separately** from the auto-generated PlatformIO configuration:

```json
{
  "configurations": [
    {
      "name": "PlatformIO",
      "// ... auto-generated content ...": ""
    },
    {
      "name": "Custom ARM",
      "includePath": [
        "${workspaceFolder}/**",
        "/opt/custom-libs/include"
      ],
      "defines": [
        "CUSTOM_BUILD",
        "VERSION=2"
      ],
      "compilerPath": "/usr/bin/arm-linux-gnueabihf-gcc",
      "cStandard": "c17",
      "cppStandard": "c++20",
      "intelliSenseMode": "gcc-arm"
    }
  ]
}
```

Select configuration in status bar: "C/C++: Custom ARM"

### Workspace Settings

Create workspace-specific settings in `.vscode/settings.json`:

```json
{
  "// Editor settings": "",
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,

  "// C/C++ settings": "",
  "C_Cpp.default.cStandard": "c11",
  "C_Cpp.default.cppStandard": "c++17",
  "C_Cpp.errorSquiggles": "enabled",

  "// PlatformIO settings": "",
  "platformio-ide.autoRebuildAutocompleteIndex": true,
  "platformio-ide.useBuiltinPIOCore": true,
  "platformio-ide.activateOnlyOnPlatformIOProject": true,

  "// File associations": "",
  "files.associations": {
    "*.h": "c",
    "*.c": "c",
    "platformio.ini": "ini"
  },

  "// Terminal": "",
  "terminal.integrated.env.linux": {
    "PLATFORMIO_FORCE_ANSI": "true"
  }
}
```

### Extension Recommendations

Create `.vscode/extensions.json` to recommend extensions:

```json
{
  "recommendations": [
    "platformio.platformio-ide",
    "ms-vscode.cpptools",
    "ms-vscode.cpptools-extension-pack",
    "streetsidesoftware.code-spell-checker",
    "eamodio.gitlens"
  ]
}
```

**Note:** PlatformIO may overwrite this file. To preserve custom recommendations, track the file in git and re-apply changes after updates.

### Remote Development (SSH to Raspberry Pi)

Develop directly on Raspberry Pi using VS Code Remote-SSH extension:

1. **Install Remote-SSH Extension:**
   - `Ctrl+Shift+X` → Search "Remote-SSH"
   - Install "Remote - SSH" by Microsoft

2. **Connect to Raspberry Pi:**
   - Press `F1`
   - Run: "Remote-SSH: Connect to Host"
   - Enter: `pi@raspberrypi.local`
   - New VS Code window opens on Pi

3. **Install PlatformIO on Pi:**
   ```bash
   # On Raspberry Pi
   curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/scripts/get-platformio.py -o get-platformio.py
   python3 get-platformio.py
   ```

4. **Open Project:**
   - `File → Open Folder` → Select project on Pi
   - PlatformIO uses **native compilation** (no cross-compile)
   - IntelliSense uses native ARM headers (no warnings)

**Benefits:**
- True native development environment
- IntelliSense matches target exactly
- Direct hardware access for testing
- No upload step needed (build and run locally)

### Git Integration

**Recommended .gitignore:**
```gitignore
# PlatformIO
.pio/
.vscode/
.pio-cache/

# Build artifacts
*.o
*.elf
*.hex
*.bin

# IDE
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/extensions.json

# Keep example configurations
!examples/*/.vscode/
```

**Commit platformio.ini:**
Always commit `platformio.ini` to version control - it's the source of truth for build configuration.

---

## Best Practices

### 1. Use platformio.ini for Configuration

**Don't manually edit** `.vscode/c_cpp_properties.json` - it will be regenerated.

**Do configure via** `platformio.ini`:
```ini
build_flags = -I/custom/path -DMY_DEFINE
lib_deps = somelib@1.0.0
```

### 2. Separate Environments for Different Workflows

```ini
[env:dev]
build_type = debug
debug_tool = gdbserver-ssh

[env:prod]
build_type = release
build_flags = -O3
```

### 3. Use Debugging Early and Often

Don't wait for bugs to start debugging:
- Use breakpoints to understand code flow
- Inspect variables to verify assumptions
- Step through complex logic interactively

### 4. Keep Extensions Updated

- PlatformIO IDE updates regularly
- C/C++ extension receives frequent improvements
- Check for updates: `Ctrl+Shift+X` → Click gear icon

### 5. Leverage IntelliSense

- Hover over functions to see documentation
- `Ctrl+Click` to go to definition
- `Shift+F12` to find all references
- `Ctrl+Space` for autocomplete

### 6. Monitor Build Output

- Don't ignore warnings
- Review linker messages
- Check binary size (important for embedded systems)

---

## Resources

### Official Documentation

- **PlatformIO IDE for VS Code:** https://docs.platformio.org/en/latest/integration/ide/vscode.html
- **PlatformIO Debugging:** https://docs.platformio.org/en/latest/plus/debugging.html
- **PlatformIO Remote Development:** https://docs.platformio.org/en/latest/tutorials/espressif32/arduino_debugging_unit_testing.html

### Platform-Specific Docs

- **[DEBUGGING.md](DEBUGGING.md)** - Remote debugging guide (GDB over SSH)
- **[UPLOAD.md](UPLOAD.md)** - Upload/deployment protocols
- **[LGPIO_SETUP.md](LGPIO_SETUP.md)** - GPIO framework setup
- **[README.md](../README.md)** - Platform overview

### Examples

- **[examples/remote-debugging/](../examples/remote-debugging/)** - Complete debugging example
- **[examples/remote-deployment/](../examples/remote-deployment/)** - Upload configuration examples
- **[examples/wiringpi-blink/](../examples/wiringpi-blink/)** - Simple LED blink with WiringPi

### Community

- **Issues:** https://github.com/platformio/platform-linux_arm/issues
- **PlatformIO Community:** https://community.platformio.org/
- **Raspberry Pi Forums:** https://forums.raspberrypi.com/

---

## Summary

VS Code integration with platform-linux_arm follows PlatformIO's **automatic configuration model**:

✅ **Configuration files are auto-generated** based on `platformio.ini`
✅ **IntelliSense works automatically** after installing the PlatformIO extension
✅ **Debugging is fully integrated** with GDB remote debugging over SSH
✅ **Build tasks are preconfigured** and accessible via shortcuts
✅ **Multi-environment workflows** supported out of the box

**Focus on your `platformio.ini` configuration** and let the PlatformIO extension handle VS Code integration.

For issues, see the [Troubleshooting](#troubleshooting) section or consult [DEBUGGING.md](DEBUGGING.md).

---

**Last Updated:** 2025-11-11
**Platform Version:** 1.6.0
