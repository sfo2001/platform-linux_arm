#!/bin/bash
# Setup script for lgpio cross-compilation
# This script builds lgpio from source for ARM and installs it locally

set -e

echo "=================================================="
echo "lgpio Cross-Compilation Setup"
echo "=================================================="
echo ""

# Check if cross-compiler is installed
if ! command -v arm-linux-gnueabihf-gcc &> /dev/null; then
    echo "❌ ERROR: ARM cross-compiler not found!"
    echo ""
    echo "Please install it first:"
    echo "  sudo apt install gcc-arm-linux-gnueabihf"
    echo ""
    exit 1
fi

echo "✓ ARM cross-compiler found: $(arm-linux-gnueabihf-gcc --version | head -1)"
echo ""

# Set paths
BUILD_DIR="${BUILD_DIR:-/tmp/lg-build}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/arm-linux-gnueabihf}"
CROSS_PREFIX="arm-linux-gnueabihf-"

echo "Build directory: $BUILD_DIR"
echo "Install directory: $INSTALL_DIR"
echo "Cross-compiler prefix: $CROSS_PREFIX"
echo ""

# Create build directory
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Clone or update lgpio repository
if [ -d "lg/.git" ]; then
    echo "Updating existing lg repository..."
    cd lg
    git pull
else
    echo "Cloning lg repository..."
    git clone https://github.com/joan2937/lg.git
    cd lg
fi

echo ""
echo "Building lgpio library for ARM..."
make CROSS_PREFIX="$CROSS_PREFIX" lib

echo ""
echo "Installing to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR/include"
mkdir -p "$INSTALL_DIR/lib"

# Install headers
cp -v lgpio.h rgpio.h "$INSTALL_DIR/include/"

# Install libraries
cp -v liblgpio.so* "$INSTALL_DIR/lib/" 2>/dev/null || true
cp -v librgpio.so* "$INSTALL_DIR/lib/" 2>/dev/null || true

# Create symlinks if needed
cd "$INSTALL_DIR/lib"
[ -f liblgpio.so.1 ] && ln -sf liblgpio.so.1 liblgpio.so
[ -f librgpio.so.1 ] && ln -sf librgpio.so.1 librgpio.so

echo ""
echo "=================================================="
echo "✓ lgpio cross-compilation setup complete!"
echo "=================================================="
echo ""
echo "Headers installed to: $INSTALL_DIR/include/"
echo "Libraries installed to: $INSTALL_DIR/lib/"
echo ""
echo "You can now build lgpio examples with PlatformIO:"
echo "  cd $(dirname $(dirname $(readlink -f $0)))"
echo "  source venv/bin/activate"
echo "  pio run -d examples/lgpio-blink"
echo ""
