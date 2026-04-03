#include <stdio.h>

/*
 * Arduino Uno Q — bare-metal hello-world
 *
 * This program runs on the QRB2210 (Cortex-A53, AArch64) side of the
 * Arduino Uno Q. GPIO is NOT available from this side without the
 * arduino-router daemon and the arduino-bridge framework.
 *
 * ⚠️ Community Testing Notice: This port has not been validated on
 * physical hardware. Please open issues with test results.
 *
 * See docs/boards/arduino_uno_q.md for full documentation.
 */

int main(void) {
    printf("Hello from Arduino Uno Q!\n");

#if defined(ARDUINO_UNO_Q)
    printf("Board: Arduino Uno Q (QRB2210 AArch64)\n");
#else
    printf("Board: Unknown\n");
#endif

    printf("MCU: Qualcomm QRB2210 (4x Cortex-A53 @ 2.0 GHz)\n");
    printf("OS:  Debian Linux (AArch64)\n");
    printf("\n");
    printf("Note: GPIO requires the arduino-router daemon and\n");
    printf("      the arduino-bridge framework (Phase 2).\n");
    printf("      See docs/boards/arduino_uno_q.md for details.\n");

    return 0;
}
