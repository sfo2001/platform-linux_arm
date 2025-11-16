# Debugging Guide for platform-linux_arm

## Quick Start

**1. Copy template .gdbinit to your project:**
```bash
cp examples/template.gdbinit /path/to/your/project/.gdbinit
```

**2. Configure GDB to allow auto-loading (one-time setup):**
```bash
mkdir -p ~/.config/gdb
echo "add-auto-load-safe-path /path/to/your/project/.gdbinit" >> ~/.config/gdb/gdbinit
```

Or allow all projects (less secure but convenient):
```bash
echo "set auto-load safe-path /" >> ~/.config/gdb/gdbinit
```

**3. Start debugging:**
```bash
pio debug --environment your_env --interface=gdb
```

GDB will automatically connect to the remote target and stop at main!

## Why is .gdbinit Required?

PlatformIO creates a `.pioinit` file with debug initialization commands, but GDB only auto-loads files named `.gdbinit`. The `.gdbinit` file works around this limitation by automatically sourcing PlatformIO's `.pioinit` when GDB starts.

This is a known PlatformIO limitation - see the template `.gdbinit` for the workaround implementation.

## Manual Debugging (Advanced)

You can also debug manually using GDB directly:

```bash
gdb-multiarch .pio/build/your_env/program

# In GDB:
(gdb) target extended-remote | ssh -o StrictHostKeyChecking=no -T user@host "gdbserver - /remote/path/program"
(gdb) break main
(gdb) continue
```

## PlatformIO CLI Debugging

The `pio debug` command starts GDB correctly but may have asyncio stdin handling issues when run non-interactively (e.g., from scripts or with redirected stdin).

**Working configuration in platformio.ini:**

```ini
[env:raspberrypi_5]
platform = /home/stefan/devel/platform-linux_arm
framework = libgpiod
board = raspberrypi_5
board_build.arch = aarch64

; Build with debug symbols
build_flags =
    -O0           ; No optimization
    -g3           ; Maximum debug information
    -ggdb         ; GDB-specific debug formats

; Upload configuration
upload_protocol = scp
upload_port = retropi@retropi:/home/retropi/devel/

; Debug configuration
debug_tool = gdbserver-ssh
debug_port = retropi@retropi
debug_init_cmds =
    target extended-remote $DEBUG_PORT
    set remote exec-file /home/retropi/devel/program
    set sysroot /
```

**Key points:**
- `debug_init_cmds` MUST include `target extended-remote $DEBUG_PORT` as the first command
- `$DEBUG_PORT` is automatically substituted with the SSH pipe command
- Without the target command, GDB will try to run the program locally (causing "Exec format error")

## VS Code Debugging

VS Code debugging integration needs further testing. The `.vscode/launch.json` is auto-generated correctly, but the Remote Development setup (Windows → SSH to Linux) may require additional configuration.

## Common Warnings (Harmless)

### Build ID mismatch
```
Warning: Build ID mismatch between current exec-file ... and automatically determined exec-file ...
```
**Cause:** Local and remote binaries differ slightly (timestamps, build IDs).
**Impact:** Cosmetic only. Debugging works fine.
**Solution:** Upload fresh binary before debugging to eliminate this warning.

### File not found (Datei oder Verzeichnis nicht gefunden)
```
Warning: ../sysdeps/aarch64/dl-start.S:22: Datei oder Verzeichnis nicht gefunden
```
**Cause:** GDB trying to show source code for C library internals on remote system.
**Impact:** None. Your application source code works fine.
**Solution:** This is normal when debugging without remote system source packages.

### File transfers can be slow
```
Warning: File transfers from remote targets can be slow. Use "set sysroot" to access files locally instead.
```
**Cause:** GDB downloading library debug symbols from remote target.
**Impact:** Initial connection may be slower (one-time per session).
**Solution:** Add `set sysroot /` to debug_init_cmds (already included in examples).

### Debuginfod prompt
```
Enable debuginfod for this session? (y or [n])
```
**Cause:** GDB asking about auto-downloading debug symbols.
**Impact:** None if using template .gdbinit (it disables this).
**Solution:** Already handled by `set debuginfod enabled off` in template .gdbinit.

### Exit warning "Undefined pio_reset_run_target"
```
(gdb) quit
Warning! Undefined pio_reset_run_target command
Unknown monitor command.
```
**Cause:** GDB cleanup trying to execute PlatformIO reset command.
**Impact:** Cosmetic only. Clean exit after this message.
**Solution:** This is harmless and can be ignored.

## Troubleshooting

### "Exec format error" when running program
**Symptom:**
```
/bin/bash: cannot execute binary file: Exec format error
```
**Cause:** GDB is trying to run the ARM binary locally instead of on the remote target.
**Solution:**
1. Verify `.gdbinit` exists in project root
2. Check GDB allowed to load it (see Quick Start step 2)
3. Ensure `target extended-remote $DEBUG_PORT` is in `debug_init_cmds`

### GDB doesn't stop at main automatically
**Symptom:** GDB starts but doesn't execute .pioinit commands.
**Cause:** .gdbinit not being auto-loaded.
**Solution:**
```bash
# Check if safe-path is configured
gdb -q --batch -ex "show auto-load safe-path"

# Add your project to safe-path
echo "add-auto-load-safe-path $(pwd)/.gdbinit" >> ~/.config/gdb/gdbinit
```

### "The program is not being run"
**Symptom:** Typing `continue` shows "The program is not being run".
**Cause:** Not connected to remote target.
**Solution:** Manually source .pioinit:
```gdb
(gdb) source ~/.platformio/.cache/.piodebug-XXXXX/.pioinit
```
Then check .gdbinit configuration as above.

### AsyncIO PermissionError
**Symptom:**
```
PermissionError: [Errno 1] Operation not permitted
```
**Cause:** Python asyncio has issues with redirected/closed stdin.
**Impact:** Cosmetic only. Debugging still works.
**Solution:** Run `pio debug` from an interactive terminal, not from scripts with stdin redirection.

## VS Code Integration

The `.vscode/launch.json` is auto-generated by PlatformIO. Debugging in VS Code should work automatically once CLI debugging works.

**To debug in VS Code:**
1. Ensure `.gdbinit` is in project root
2. Press `Ctrl+Shift+D` (Debug view)
3. Select "PIO Debug" or "PIO Debug (without uploading)"
4. Press `F5` to start debugging

VS Code will use the same debug configuration as CLI, so all the fixes apply.

## Testing Matrix

Verified working configurations:
- ✅ CLI debugging on Linux (x86_64 → ARM remote)
- ⏳ VS Code debugging (pending user test)
- ⏳ Windows → Linux remote via SSH
- ⏳ Native ARM debugging

## Additional Resources

- [PlatformIO Debugging Documentation](https://docs.platformio.org/en/latest/plus/debugging.html)
- [GDB Remote Debugging](https://sourceware.org/gdb/current/onlinedocs/gdb/Remote-Debugging.html)
- Platform examples: `examples/` directory
