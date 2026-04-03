#!/bin/bash
# Setup script for MRAA cross-compilation (Arduino Uno Q / arduino-bridge framework)
# Builds MRAA v2.2.0 from source for AArch64 and installs locally.
#
# Usage:
#   ./scripts/setup-mraa-cross.sh                          # AArch64 with defaults
#   CROSS_PREFIX=aarch64-unknown-linux-gnu- \              # macOS Homebrew toolchain
#   INSTALL_DIR=$HOME/.local/aarch64-linux-gnu \
#   ./scripts/setup-mraa-cross.sh
#
# Environment variables:
#   CROSS_PREFIX  Cross-compiler prefix (default: aarch64-linux-gnu-)
#   INSTALL_DIR   Install destination   (default: $HOME/.local/aarch64-linux-gnu)
#   BUILD_DIR     CMake build directory  (default: /tmp/mraa-build-aarch64)

set -e

echo "=================================================="
echo "MRAA Cross-Compilation Setup (Arduino Uno Q)"
echo "=================================================="
echo ""

# Resolve directories before any cd
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
CROSS_PREFIX="${CROSS_PREFIX:-aarch64-linux-gnu-}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/aarch64-linux-gnu}"
if [[ -z "${BUILD_DIR:-}" ]]; then
    BUILD_DIR="$(mktemp -d -t mraa-build-aarch64.XXXXXX)"
    trap 'rm -rf "$BUILD_DIR"' EXIT
fi
MRAA_VERSION="v2.2.0"
# Expected commit SHA for MRAA v2.2.0 — verified from https://github.com/eclipse/mraa/releases/tag/v2.2.0
# Run to verify: git ls-remote https://github.com/eclipse/mraa.git refs/tags/v2.2.0^{}
MRAA_EXPECTED_SHA="7786c7ded5c9ce7773890d0e3dc27632898fc6b1"

CROSS_CXX="${CROSS_PREFIX}g++"
CROSS_GCC="${CROSS_PREFIX}gcc"

# Check cross-compiler
if ! command -v "$CROSS_CXX" &>/dev/null; then
    echo "ERROR: Cross-compiler not found: $CROSS_CXX"
    echo ""
    echo "Install with:"
    echo "  sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu"
    echo "  (macOS: brew tap messense/macos-cross-toolchains && brew install aarch64-unknown-linux-gnu)"
    echo ""
    exit 1
fi

echo "Cross-compiler: $($CROSS_CXX --version | head -1)"
echo "Install dir:    $INSTALL_DIR"
echo "Build dir:      $BUILD_DIR"
echo ""

# Check cmake
if ! command -v cmake &>/dev/null; then
    echo "ERROR: cmake not found."
    echo "Install with:"
    echo "  sudo apt install cmake    (Ubuntu)"
    echo "  brew install cmake        (macOS)"
    echo ""
    exit 1
fi

echo "CMake: $(cmake --version | head -1)"
echo ""

# Clone or update MRAA
mkdir -p "$BUILD_DIR"
MRAA_SRC="$BUILD_DIR/mraa"

if [ -d "$MRAA_SRC/.git" ]; then
    echo "Updating existing MRAA repository..."
    cd "$MRAA_SRC"
    git fetch --tags
    git checkout "$MRAA_VERSION"
else
    echo "Cloning MRAA $MRAA_VERSION..."
    git clone --depth 1 --branch "$MRAA_VERSION" https://github.com/eclipse/mraa.git "$MRAA_SRC"
    cd "$MRAA_SRC"
fi

# Enforce expected commit SHA — fail fast if the tag has been moved
ACTUAL_SHA=$(git -C "$MRAA_SRC" rev-parse HEAD)
if [ "$ACTUAL_SHA" != "$MRAA_EXPECTED_SHA" ]; then
    echo "ERROR: MRAA SHA mismatch!"
    echo "  Expected: $MRAA_EXPECTED_SHA"
    echo "  Actual:   $ACTUAL_SHA"
    echo ""
    echo "The v2.2.0 tag may have been moved. Verify at:"
    echo "  https://github.com/eclipse/mraa/releases/tag/v2.2.0"
    echo ""
    echo "If the new SHA is intentional, update MRAA_EXPECTED_SHA in this script."
    exit 1
fi
echo "MRAA SHA verified: $ACTUAL_SHA"

echo ""

# Write CMake toolchain file
TOOLCHAIN_FILE="$BUILD_DIR/toolchain-aarch64.cmake"
cat > "$TOOLCHAIN_FILE" << EOF
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)
set(CMAKE_C_COMPILER   ${CROSS_GCC})
set(CMAKE_CXX_COMPILER ${CROSS_CXX})
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
EOF

# Configure
CMAKE_BUILD="$BUILD_DIR/build"
mkdir -p "$CMAKE_BUILD"
cd "$CMAKE_BUILD"

cmake "$MRAA_SRC" \
    -DCMAKE_TOOLCHAIN_FILE="$TOOLCHAIN_FILE" \
    -DCMAKE_INSTALL_PREFIX="$INSTALL_DIR" \
    -DJSONPLAT=OFF \
    -DBUILDSWIGPYTHON=OFF \
    -DBUILDSWIGNODE=OFF \
    -DFIRMATA=OFF \
    -DENABLEEXAMPLES=OFF \
    -DBUILDTESTS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DCMAKE_C_FLAGS="-fcommon"

echo ""
echo "Building MRAA..."
cmake --build . --parallel "$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 2)"

echo ""
echo "Installing to $INSTALL_DIR..."
cmake --install .

echo ""
echo "=================================================="
echo "MRAA cross-compilation complete!"
echo "=================================================="
echo ""
echo "Headers installed to: $INSTALL_DIR/include/mraa/"
echo "Library installed to: $INSTALL_DIR/lib/"
echo ""
echo "You can now build arduino-bridge examples with PlatformIO:"
echo "  cd $REPO_ROOT"
echo "  pio run -d examples/arduino-bridge-blink"
echo ""
