# GDB Configuration for PlatformIO Remote Debugging
# Copy this file to your project root as .gdbinit
#
# IMPORTANT: Add this line to ~/.config/gdb/gdbinit to allow auto-loading:
#   add-auto-load-safe-path /path/to/your/project/.gdbinit
#
# Or to allow all project .gdbinit files (less secure):
#   set auto-load safe-path /

# Suppress informational messages
set debuginfod enabled off

# Auto-source PlatformIO's .pioinit file
# PlatformIO creates .pioinit with debug commands but doesn't tell GDB to execute it
# This workaround automatically loads it when GDB starts
python
import os
import glob

# Find the most recent .piodebug cache directory
piodebug_dirs = glob.glob(os.path.expanduser('~/.platformio/.cache/.piodebug-*/'))
if piodebug_dirs:
    latest_dir = max(piodebug_dirs, key=os.path.getmtime)
    pioinit_file = os.path.join(latest_dir, '.pioinit')
    if os.path.exists(pioinit_file):
        gdb.execute(f'source {pioinit_file}')
        print(f'Loaded PlatformIO init script from {pioinit_file}')
    else:
        print(f'Warning: .pioinit not found in {latest_dir}')
else:
    print('Warning: No PlatformIO debug cache found. Run "pio debug" to initialize.')
end
