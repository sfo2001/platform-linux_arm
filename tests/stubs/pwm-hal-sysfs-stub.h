// SPDX-License-Identifier: Apache-2.0
/**
 * pwm-hal-sysfs-stub.h — Test stub control interface for pwm-hal sysfs seam.
 *
 * Include this in test files that need to control stub behaviour.
 */
#ifndef PWM_HAL_SYSFS_STUB_H
#define PWM_HAL_SYSFS_STUB_H

#include <stdbool.h>

/**
 * Reset all stub state.  Call at the start of every test case.
 */
void stub_reset(void);

/**
 * Configure the pin map returned by pwm_get_pin_map().
 *
 * @param is_pi5  true  → return Pi 5 map (GPIO 18 → chip 2, channel 0)
 *                false → return Pi 1-4 map (GPIO 18 → chip 0, channel 0)  [default]
 */
void stub_set_pi5(bool is_pi5);

/**
 * Simulate a delayed export response for testing the pwm_export() timeout path.
 *
 * When n_failures > 0, the next n_failures calls to pwm_is_exported() will
 * return false even after the channel has been written to export.  After
 * n_failures calls, pwm_is_exported() returns true normally.
 *
 * Reset to 0 by stub_reset().
 *
 * @param n_failures  Number of calls to return false before returning true.
 *                    Pass 0 to disable the delay (default).
 */
void stub_set_export_delay(int n_failures);

/**
 * Make the next pwm_sysfs_write() call whose path ends with path_suffix
 * return error_code instead of PWM_SUCCESS.
 * Only matches once — the match is consumed after one trigger.
 * Pass NULL to disable (default).
 * Reset to NULL by stub_reset().
 */
void stub_set_write_fail_on(const char *path_suffix, int error_code);

/**
 * Set write failure for path_suffix to fire after n_successes_before_fail
 * successful writes to that suffix.  Use for testing double-failure paths.
 *
 * After n_successes_before_fail matching writes succeed, the next matching
 * write returns error_code.  Only fires once — the trigger is consumed.
 * Pass NULL to disable (default).
 * Reset to NULL by stub_reset().
 */
void stub_set_write_fail_after(const char *path_suffix, int error_code,
                               int n_successes_before_fail);

#endif /* PWM_HAL_SYSFS_STUB_H */
