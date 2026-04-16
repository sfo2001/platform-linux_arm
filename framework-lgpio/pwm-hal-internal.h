// SPDX-License-Identifier: Apache-2.0
/**
 * pwm-hal-internal.h — Internal types and sysfs seam declarations for pwm-hal.
 *
 * This header is included by:
 *   - pwm-hal.c             (uses the seam and the typedef)
 *   - pwm-hal-sysfs.c       (provides the production implementations)
 *   - tests/stubs/          (provides the stub implementations)
 *   - tests/test_pwm_hal.c  (directly accesses pwm_reset_state_for_testing)
 */
#ifndef PWM_HAL_INTERNAL_H
#define PWM_HAL_INTERNAL_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

/* Shared constants used by pwm-hal.c and pwm-hal-sysfs.c */
#define PWM_SYSFS_BASE "/sys/class/pwm"
#define MAX_PATH_LEN   256

/**
 * Number of 10ms polling iterations in pwm_export() before declaring timeout.
 * Shared with tests/test_pwm_hal.c so T20 (test_export_timeout) stays in sync
 * with the loop bound — pass exactly PWM_EXPORT_RETRIES to stub_set_export_delay()
 * to trigger PWM_ERROR_IO reliably.
 */
#define PWM_EXPORT_RETRIES  10

/**
 * @brief GPIO pin to PWM chip/channel mapping
 *
 * Moved here from pwm-hal.c so stub and sysfs translation units share the type.
 */
typedef struct {
    int gpio_pin;    /**< GPIO pin number (BCM); -1 = sentinel */
    int pwm_chip;    /**< PWM chip number */
    int pwm_channel; /**< PWM channel (0 or 1) */
} pwm_pin_map_t;

/* GPIO-to-chip/channel pin maps — defined in pwm-hal.c (always linked). */
/* Both pwm-hal-sysfs.c (production) and stubs reference these. */
extern const pwm_pin_map_t g_pwm_pin_map_pi1_4[];
extern const pwm_pin_map_t g_pwm_pin_map_pi5[];

/**
 * Sysfs seam functions.
 * Production implementations live in pwm-hal-sysfs.c.
 * Test stub implementations live in tests/stubs/pwm-hal-sysfs-stub.c.
 */
int  pwm_sysfs_write(const char *path, const char *value);
/**
 * Read a sysfs attribute into value (max_len bytes, NUL-terminated).
 * Used by pwm_sample_hardware() to read live hardware state.
 * Stub and production implementations MUST provide this function as it is
 * part of the mandatory seam contract.
 */
int  pwm_sysfs_read(const char *path, char *value, size_t max_len);
/**
 * Sleep for the given number of milliseconds.  Production implementation calls
 * usleep(); the test stub is a no-op so unit tests run without real delays.
 */
void pwm_sysfs_sleep_ms(int ms);
bool pwm_is_exported(int chip, int channel);
const pwm_pin_map_t *pwm_get_pin_map(void);

/**
 * Test-only state reset.  Compiled only when -DUNIT_TESTING=1 is set (CMake
 * test target).  Resets g_pwm_channels and g_pwm_initialized so each test
 * starts from a clean slate without rebuilding.
 */
#ifdef UNIT_TESTING
void pwm_reset_state_for_testing(void);
/**
 * Fill all state slots with fictional entries to simulate slot exhaustion.
 * Use before calling pwm_init() to trigger the PWM_ERROR_HARDWARE path in
 * pwm_alloc_state().  See pwm-hal.c for implementation details.
 */
void pwm_fill_channels_for_testing(void);
#endif

#endif /* PWM_HAL_INTERNAL_H */
