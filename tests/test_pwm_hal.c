// SPDX-License-Identifier: Apache-2.0
/**
 * test_pwm_hal.c — Plain-C unit tests for framework-lgpio/pwm-hal.c
 *
 * Each test function:
 *   1. Calls stub_reset()              to clear stub export state
 *   2. Calls pwm_reset_state_for_testing() to clear HAL channel table
 *   3. Exercises one behaviour
 *   4. assert()s the expected result — terminates on failure with a diagnostic
 *   5. Prints "PASS <name>" on success
 *
 * Build with CMake target test_pwm_hal (see CMakeLists.txt).
 */

#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

#include "pwm-hal.h"
#include "pwm-hal-internal.h"
#include "pwm-hal-sysfs-stub.h"

/* ============================================================
 * Helper macro — print test name, call function, check result
 * ============================================================ */
static int g_tests_run = 0;
#define RUN(fn) do { fn(); g_tests_run++; printf("PASS %s\n", #fn); } while (0)

/* ============================================================
 * Test cases
 * ============================================================ */

/**
 * T1: pwm_init(18, 1000) returns PWM_SUCCESS.
 * GPIO 18 maps to chip 0, channel 0 on Pi 1-4 (default stub map).
 */
static void test_init_gpio18_succeeds(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(18, 1000);
    assert(result == PWM_SUCCESS);
}

/**
 * T2: pwm_init(13, 1000) returns PWM_SUCCESS.
 * GPIO 13 maps to chip 0, channel 1 — different channel than GPIO 18.
 */
static void test_init_gpio13_succeeds(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(13, 1000);
    assert(result == PWM_SUCCESS);
}

/**
 * T3: After init on GPIO 18 (chip 0, channel 0), init on GPIO 12 returns
 * PWM_ERROR_BUSY because GPIO 12 maps to the same chip 0, channel 0.
 */
static void test_init_conflict_gpio12_after_gpio18(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_init(12, 1000);
    assert(result == PWM_ERROR_BUSY);
}

/**
 * T4: Re-initialising the same pin does not return PWM_ERROR_BUSY.
 * The conflict check skips entries with gpio_pin == pin.
 */
static void test_reinit_same_pin_not_busy(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_init(18, 2000);
    assert(result == PWM_SUCCESS);
}

/**
 * T5: pwm_write(18, 50.0) before any pwm_init returns PWM_ERROR_NOT_EXPORTED.
 * pwm_find_state() returns NULL → NOT_EXPORTED.
 */
static void test_write_before_init_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_write(18, 50.0f);
    assert(result == PWM_ERROR_NOT_EXPORTED);
}

/**
 * T6: After pwm_deinit(18), GPIO 12 can be initialised on the same channel.
 * pwm_deinit frees the state slot; the conflict check no longer finds GPIO 18.
 */
static void test_deinit_releases_state(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    assert(pwm_deinit(18) == PWM_SUCCESS);

    int result = pwm_init(12, 1000);
    assert(result == PWM_SUCCESS);
}

/**
 * T7: pwm_pin_is_valid() correctly classifies pins.
 * GPIO 99 is not in either map; GPIO 18 is.
 */
static void test_pin_is_valid_rejects_invalid(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_pin_is_valid(99) == false);
    assert(pwm_pin_is_valid(18) == true);
}

/**
 * T8: pwm_init(18, 0) returns PWM_ERROR_INVALID_PARAM.
 * Frequency 0 is below PWM_MIN_FREQUENCY_HZ.
 */
static void test_init_invalid_freq(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(18, 0);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T9: With stub_set_pi5(true), GPIO 18 resolves to chip 2, channel 0.
 * Verifies that pwm_get_chip_channel honours the stub's pin map.
 */
static void test_pi5_pin_map(void) {
    stub_reset();
    stub_set_pi5(true);
    pwm_reset_state_for_testing();

    int chip = -1, channel = -1;
    int result = pwm_get_chip_channel(18, &chip, &channel);

    assert(result == PWM_SUCCESS);
    assert(chip    == 2);
    assert(channel == 0);
}

/**
 * T10: pwm_write(18, 50.0) after init returns PWM_SUCCESS.
 */
static void test_write_after_init_succeeds(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_write(18, 50.0f);
    assert(result == PWM_SUCCESS);
}

/**
 * T11: pwm_write(18, -1.0) returns PWM_ERROR_INVALID_PARAM.
 */
static void test_write_invalid_duty_low(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_write(18, -1.0f);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T12: pwm_write(18, 101.0) returns PWM_ERROR_INVALID_PARAM.
 */
static void test_write_invalid_duty_high(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_write(18, 101.0f);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T13: pwm_init(99, 1000) returns PWM_ERROR_INVALID_PIN.
 * GPIO 99 is not in the pin map.
 */
static void test_init_invalid_pin(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(99, 1000);
    assert(result == PWM_ERROR_INVALID_PIN);
}

/**
 * T14: pwm_set_frequency(18, 2000) after init returns PWM_SUCCESS and updates
 * shadow state — status.frequency_hz must reflect the new frequency.
 */
static void test_set_frequency_valid(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_set_frequency(18, 2000);
    assert(result == PWM_SUCCESS);
    pwm_status_t status;
    assert(pwm_get_status(18, &status) == PWM_SUCCESS);
    assert(status.frequency_hz == 2000);
}

/**
 * T15: pwm_set_polarity(18, PWM_POLARITY_NORMAL) after init returns PWM_SUCCESS.
 */
static void test_set_polarity_normal(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_set_polarity(18, PWM_POLARITY_NORMAL);
    assert(result == PWM_SUCCESS);
}

/**
 * T16: pwm_set_polarity(18, PWM_POLARITY_INVERTED) after init returns PWM_SUCCESS and
 * updates shadow state — status.polarity must reflect the new polarity value.
 */
static void test_set_polarity_inverted(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_set_polarity(18, PWM_POLARITY_INVERTED);
    assert(result == PWM_SUCCESS);
    pwm_status_t status;
    assert(pwm_get_status(18, &status) == PWM_SUCCESS);
    assert(status.polarity == PWM_POLARITY_INVERTED);
}

/**
 * T17: pwm_get_status(18, &status) after init reflects the expected state.
 */
static void test_get_status_after_init(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    pwm_status_t status;
    int result = pwm_get_status(18, &status);
    assert(result == PWM_SUCCESS);
    assert(status.gpio_pin == 18);
    assert(status.pwm_chip == 0);
    assert(status.pwm_channel == 0);
    assert(status.is_enabled == true);
    assert(status.is_exported == true);
    assert(status.frequency_hz == 1000);
    assert(status.duty_cycle_percent == 0.0f);
    assert(status.polarity == PWM_POLARITY_NORMAL);
}

/**
 * T18: pwm_is_enabled(18) returns true after init.
 */
static void test_is_enabled_after_init(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    assert(pwm_is_enabled(18) == true);
}

/**
 * T19: pwm_is_enabled(18) returns false before any init.
 */
static void test_is_enabled_before_init(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_is_enabled(18) == false);
}

/**
 * T20: With stub_set_export_delay(PWM_EXPORT_RETRIES), pwm_init(18, 1000) returns
 * PWM_ERROR_IO.
 *
 * COUPLING NOTE: stub_set_export_delay() must receive exactly PWM_EXPORT_RETRIES
 * (defined in pwm-hal-internal.h) to reliably exhaust all iterations of the retry
 * loop in pwm_export().  A value smaller than PWM_EXPORT_RETRIES would let the
 * loop succeed partway through and return PWM_SUCCESS instead.  If the retry loop
 * bound changes, update PWM_EXPORT_RETRIES — this test will automatically track it.
 */
static void test_export_timeout(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    stub_set_export_delay(PWM_EXPORT_RETRIES);
    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T21: pwm_set_frequency(18, 1000) before init returns PWM_ERROR_NOT_EXPORTED.
 * pwm_find_state() returns NULL → NOT_EXPORTED.
 */
static void test_set_frequency_before_init_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_set_frequency(18, 1000);
    assert(result == PWM_ERROR_NOT_EXPORTED);
}

/**
 * T22: pwm_set_frequency(18, 0) after init returns PWM_ERROR_INVALID_PARAM.
 * Frequency 0 is below PWM_MIN_FREQUENCY_HZ.
 */
static void test_set_frequency_invalid_freq(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_set_frequency(18, 0);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T23: pwm_set_polarity(18, PWM_POLARITY_NORMAL) before init returns
 * PWM_ERROR_NOT_EXPORTED.
 */
static void test_set_polarity_before_init_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_set_polarity(18, PWM_POLARITY_NORMAL);
    assert(result == PWM_ERROR_NOT_EXPORTED);
}

/**
 * T24: pwm_set_polarity(18, 99) after init returns PWM_ERROR_INVALID_PARAM.
 * 99 is not a valid pwm_polarity_t value (valid: 0=NORMAL, 1=INVERTED).
 */
static void test_set_polarity_invalid_value(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_set_polarity(18, (pwm_polarity_t)99);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T25: pwm_deinit(18) before any init returns PWM_SUCCESS.
 * pwm_find_state() returns NULL → early return PWM_SUCCESS (idempotent).
 */
static void test_deinit_before_init_succeeds(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_deinit(18);
    assert(result == PWM_SUCCESS);
}

/**
 * T26: pwm_get_status(18, NULL) returns PWM_ERROR_INVALID_PARAM.
 * NULL status pointer is rejected before state lookup.
 */
static void test_get_status_null_ptr_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_get_status(18, NULL);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T27: pwm_get_chip_channel(18, NULL, NULL) returns PWM_ERROR_INVALID_PARAM.
 * NULL output pointers are rejected before map lookup.
 */
static void test_get_chip_channel_null_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int chip, channel;
    int result = pwm_get_chip_channel(18, NULL, NULL);
    assert(result == PWM_ERROR_INVALID_PARAM);
    result = pwm_get_chip_channel(18, NULL, &channel);
    assert(result == PWM_ERROR_INVALID_PARAM);
    result = pwm_get_chip_channel(18, &chip, NULL);
    assert(result == PWM_ERROR_INVALID_PARAM);
    (void)chip;    /* output only; value discarded — suppress -Wunused warnings */
    (void)channel;
}

/**
 * T28: pwm_write(18, 0.0) returns PWM_SUCCESS.
 * 0.0% is the lower boundary of the valid duty cycle range [0.0, 100.0].
 */
static void test_write_boundary_zero(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_write(18, 0.0f);
    assert(result == PWM_SUCCESS);
}

/**
 * T29: pwm_write(18, 100.0) returns PWM_SUCCESS.
 * 100.0% is the upper boundary of the valid duty cycle range [0.0, 100.0].
 */
static void test_write_boundary_full(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    int result = pwm_write(18, 100.0f);
    assert(result == PWM_SUCCESS);
}

/**
 * T30: pwm_init(18, 1000) returns PWM_ERROR_IO when the period write fails.
 * The period write is the first sysfs write after export succeeds in pwm_init.
 */
static void test_init_fails_on_period_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    stub_set_write_fail_on("/period", PWM_ERROR_IO);
    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T31: pwm_init(18, 1000) returns PWM_ERROR_IO when the duty_cycle write fails.
 */
static void test_init_fails_on_duty_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    stub_set_write_fail_on("/duty_cycle", PWM_ERROR_IO);
    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T32: pwm_init(18, 1000) returns PWM_ERROR_IO when the enable write fails.
 */
static void test_init_fails_on_enable_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    stub_set_write_fail_on("/enable", PWM_ERROR_IO);
    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T33: pwm_set_frequency(18, 2000) returns PWM_ERROR_IO when the period write fails.
 * pwm_set_frequency first disables (write to .../enable), then writes period.
 * Setting write_fail_on("/period") lets the disable write succeed and fails only
 * the period write.  The one-shot is consumed on "/period", so the re-enable
 * attempt succeeds.  The return code must be PWM_ERROR_IO.
 */
static void test_set_frequency_fails_on_period_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/period", PWM_ERROR_IO);
    int result = pwm_set_frequency(18, 2000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T34: pwm_set_polarity(18, PWM_POLARITY_INVERTED) returns PWM_ERROR_IO when the
 * polarity write fails.  pwm_set_polarity first disables, then writes polarity.
 * Setting write_fail_on("/polarity") lets the disable succeed and fails the
 * polarity write.  The re-enable attempt succeeds (one-shot consumed).
 */
static void test_set_polarity_fails_on_polarity_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/polarity", PWM_ERROR_IO);
    int result = pwm_set_polarity(18, PWM_POLARITY_INVERTED);
    assert(result == PWM_ERROR_IO);
}

/**
 * T35: pwm_error_string() returns a non-NULL, non-empty string for every
 * defined error code.
 */
static void test_error_string_all_codes(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    const pwm_error_t codes[] = {
        PWM_SUCCESS,
        PWM_ERROR_INVALID_PIN,
        PWM_ERROR_PERMISSION,
        PWM_ERROR_BUSY,
        PWM_ERROR_NOT_EXPORTED,
        PWM_ERROR_INVALID_PARAM,
        PWM_ERROR_IO,
        PWM_ERROR_NOT_ENABLED,
        PWM_ERROR_HARDWARE,
    };
    for (size_t i = 0; i < sizeof(codes) / sizeof(codes[0]); i++) {
        const char *s = pwm_error_string(codes[i]);
        assert(s != NULL);
        assert(s[0] != '\0');
    }
}

/**
 * T36: pwm_error_string() with an unknown code returns a non-NULL pointer
 * (the "Unknown error" default branch).
 */
static void test_error_string_unknown_code(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    const char *s = pwm_error_string((pwm_error_t)-99);
    assert(s != NULL);
    assert(s[0] != '\0');
}

/**
 * T37: pwm_pin_is_valid() returns true for all Pi 1-4 PWM-capable GPIOs
 * (12, 13, 18, 19) and false for non-PWM GPIOs (99, 0, 1, 4).
 */
static void test_pin_is_valid_all_pi14_pins(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_pin_is_valid(12)  == true);
    assert(pwm_pin_is_valid(13)  == true);
    assert(pwm_pin_is_valid(18)  == true);
    assert(pwm_pin_is_valid(19)  == true);
    assert(pwm_pin_is_valid(99)  == false);
    assert(pwm_pin_is_valid(0)   == false);
    assert(pwm_pin_is_valid(1)   == false);
    assert(pwm_pin_is_valid(4)   == false);
}

/**
 * T38: With stub_set_pi5(true), pwm_pin_is_valid() returns true for
 * Pi 5 PWM GPIOs (12, 13, 18, 19) and false for GPIO 99.
 */
static void test_pin_is_valid_pi5_pins(void) {
    stub_reset();
    stub_set_pi5(true);
    pwm_reset_state_for_testing();

    assert(pwm_pin_is_valid(12)  == true);
    assert(pwm_pin_is_valid(13)  == true);
    assert(pwm_pin_is_valid(18)  == true);
    assert(pwm_pin_is_valid(19)  == true);
    assert(pwm_pin_is_valid(99)  == false);
}

/**
 * T39: pwm_init(18, PWM_MAX_FREQUENCY_HZ + 1) returns PWM_ERROR_INVALID_PARAM.
 * Frequency above PWM_MAX_FREQUENCY_HZ is rejected.
 */
static void test_init_freq_too_high(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(18, PWM_MAX_FREQUENCY_HZ + 1);
    assert(result == PWM_ERROR_INVALID_PARAM);
}

/**
 * T40: pwm_get_status(18, &status) before any init returns PWM_ERROR_NOT_EXPORTED.
 * pwm_find_state() returns NULL → NOT_EXPORTED.
 */
static void test_get_status_before_init_fails(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    pwm_status_t status;
    int result = pwm_get_status(18, &status);
    assert(result == PWM_ERROR_NOT_EXPORTED);
}

/**
 * T41: pwm_write() propagates a sysfs I/O error from pwm_sysfs_write().
 * After a successful init, injecting a write failure on the duty_cycle path
 * causes pwm_write() to return PWM_ERROR_IO.
 */
static void test_write_fails_on_sysfs_io(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/duty_cycle", PWM_ERROR_IO);
    int result = pwm_write(18, 50.0f);
    assert(result == PWM_ERROR_IO);
}

/**
 * T42: pwm_set_frequency() propagates a sysfs I/O error on the duty-cycle
 * update step. After init, injecting a write failure on the duty_cycle path
 * causes pwm_set_frequency() to return PWM_ERROR_IO (init already consumed
 * the duty_cycle write, so the fail fires on pwm_set_frequency's duty write).
 */
static void test_set_frequency_fails_on_duty_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/duty_cycle", PWM_ERROR_IO);
    int result = pwm_set_frequency(18, 2000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T43: pwm_init(18, PWM_MAX_FREQUENCY_HZ) returns PWM_SUCCESS.
 * At 100 MHz the period is 10 ns (1,000,000,000 / 100,000,000 = 10).
 */
static void test_init_max_freq_succeeds(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    int result = pwm_init(18, PWM_MAX_FREQUENCY_HZ);
    assert(result == PWM_SUCCESS);

    pwm_status_t status;
    assert(pwm_get_status(18, &status) == PWM_SUCCESS);
    assert(status.period_ns == 10);
    assert(status.frequency_hz == PWM_MAX_FREQUENCY_HZ);
}

/**
 * T44: pwm_set_frequency(18, 2000) returns PWM_ERROR_IO when the disable
 * write to /enable fails.  Failure is injected after a successful init so
 * that the fault fires on the first /enable write inside pwm_set_frequency.
 */
static void test_set_frequency_fails_on_disable(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/enable", PWM_ERROR_IO);
    int result = pwm_set_frequency(18, 2000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T45: pwm_set_polarity(18, PWM_POLARITY_INVERTED) returns PWM_ERROR_IO when
 * the disable write to /enable fails.  Failure is injected after a successful
 * init so that the fault fires on the first /enable write in pwm_set_polarity.
 */
static void test_set_polarity_fails_on_disable(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/enable", PWM_ERROR_IO);
    int result = pwm_set_polarity(18, PWM_POLARITY_INVERTED);
    assert(result == PWM_ERROR_IO);
}

/**
 * T46: pwm_set_frequency(18, 2000) returns an error when both the period write
 * and the subsequent re-enable write fail.
 *
 * Setup:
 *   stub_set_write_fail_after("/enable", PWM_ERROR_IO, 1) — lets the first
 *   /enable write (disable step) succeed, then fails the second (re-enable).
 *   stub_set_write_fail_on("/period", PWM_ERROR_IO) — fails the period write,
 *   triggering the re-enable attempt that then also fails.
 *
 * Both mechanisms use independent slots and may be armed simultaneously.
 */
static void test_set_frequency_reenable_fails_after_period_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_after("/enable", PWM_ERROR_IO, 1);
    stub_set_write_fail_on("/period", PWM_ERROR_IO);
    int result = pwm_set_frequency(18, 2000);
    assert(result == PWM_ERROR_IO);
    assert(pwm_is_enabled(18) == false);
}

/**
 * T47: pwm_deinit(18) propagates the error when the unexport sysfs write fails.
 * The state is freed regardless; the caller receives the unexport error code.
 * Verified by confirming GPIO 12 (same chip/channel as GPIO 18 on Pi 1-4) can
 * be initialised after the failed deinit — proving the slot was released.
 */
static void test_deinit_unexport_fail_propagates(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_on("/unexport", PWM_ERROR_IO);
    int result = pwm_deinit(18);
    assert(result == PWM_ERROR_IO);
    /* State slot must be freed even though unexport failed. */
    assert(pwm_init(12, 1000) == PWM_SUCCESS);
}

/**
 * T48: pwm_set_polarity(18, PWM_POLARITY_INVERTED) returns an error when both
 * the polarity write and the subsequent re-enable write fail.
 *
 * Mirrors T46 for pwm_set_polarity.
 *
 * Setup:
 *   stub_set_write_fail_after("/enable", PWM_ERROR_IO, 1) — lets the first
 *   /enable write (disable step) succeed, then fails the second (re-enable).
 *   stub_set_write_fail_on("/polarity", PWM_ERROR_IO) — fails the polarity write,
 *   triggering the re-enable attempt that then also fails.
 *
 * Both mechanisms use independent slots and may be armed simultaneously.
 */
static void test_set_polarity_reenable_fails_after_polarity_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    assert(pwm_init(18, 1000) == PWM_SUCCESS);
    stub_set_write_fail_after("/enable", PWM_ERROR_IO, 1);
    stub_set_write_fail_on("/polarity", PWM_ERROR_IO);
    int result = pwm_set_polarity(18, PWM_POLARITY_INVERTED);
    assert(result == PWM_ERROR_IO);
    assert(pwm_is_enabled(18) == false);
}

/**
 * T49: pwm_init(18, 1000) returns PWM_ERROR_IO when the export sysfs write fails.
 * The write to pwmchipN/export is the first I/O step in pwm_export(); failure
 * propagates directly to pwm_init() without entering the poll loop.
 */
static void test_init_fails_on_export_write(void) {
    stub_reset();
    pwm_reset_state_for_testing();

    stub_set_write_fail_on("/export", PWM_ERROR_IO);
    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_IO);
}

/**
 * T50: pwm_init(18, 1000) returns PWM_ERROR_HARDWARE when all state slots are full.
 * pwm_fill_channels_for_testing() pre-fills every g_pwm_channels slot with a
 * fictional pin (gpio_pin = 100..107, chip=0, ch=1).  GPIO 18 maps to ch=0,
 * so the conflict check passes, but pwm_alloc_state() finds no free slot and
 * returns NULL, causing pwm_init() to return PWM_ERROR_HARDWARE.
 */
static void test_init_fails_when_all_slots_full(void) {
    stub_reset();
    pwm_reset_state_for_testing();
    pwm_fill_channels_for_testing();

    int result = pwm_init(18, 1000);
    assert(result == PWM_ERROR_HARDWARE);
}

/* ============================================================
 * Main
 * ============================================================ */

int main(void) {
    RUN(test_init_gpio18_succeeds);
    RUN(test_init_gpio13_succeeds);
    RUN(test_init_conflict_gpio12_after_gpio18);
    RUN(test_reinit_same_pin_not_busy);
    RUN(test_write_before_init_fails);
    RUN(test_deinit_releases_state);
    RUN(test_pin_is_valid_rejects_invalid);
    RUN(test_init_invalid_freq);
    RUN(test_pi5_pin_map);
    RUN(test_write_after_init_succeeds);
    RUN(test_write_invalid_duty_low);
    RUN(test_write_invalid_duty_high);
    RUN(test_init_invalid_pin);
    RUN(test_set_frequency_valid);
    RUN(test_set_polarity_normal);
    RUN(test_set_polarity_inverted);
    RUN(test_get_status_after_init);
    RUN(test_is_enabled_after_init);
    RUN(test_is_enabled_before_init);
    RUN(test_export_timeout);
    RUN(test_set_frequency_before_init_fails);
    RUN(test_set_frequency_invalid_freq);
    RUN(test_set_polarity_before_init_fails);
    RUN(test_set_polarity_invalid_value);
    RUN(test_deinit_before_init_succeeds);
    RUN(test_get_status_null_ptr_fails);
    RUN(test_get_chip_channel_null_fails);
    RUN(test_write_boundary_zero);
    RUN(test_write_boundary_full);
    RUN(test_init_fails_on_period_write);
    RUN(test_init_fails_on_duty_write);
    RUN(test_init_fails_on_enable_write);
    RUN(test_set_frequency_fails_on_period_write);
    RUN(test_set_polarity_fails_on_polarity_write);
    RUN(test_error_string_all_codes);
    RUN(test_error_string_unknown_code);
    RUN(test_pin_is_valid_all_pi14_pins);
    RUN(test_pin_is_valid_pi5_pins);
    RUN(test_init_freq_too_high);
    RUN(test_get_status_before_init_fails);
    RUN(test_write_fails_on_sysfs_io);
    RUN(test_set_frequency_fails_on_duty_write);
    RUN(test_init_max_freq_succeeds);
    RUN(test_set_frequency_fails_on_disable);
    RUN(test_set_polarity_fails_on_disable);
    RUN(test_set_frequency_reenable_fails_after_period_write);
    RUN(test_set_polarity_reenable_fails_after_polarity_write);
    RUN(test_deinit_unexport_fail_propagates);
    RUN(test_init_fails_on_export_write);
    RUN(test_init_fails_when_all_slots_full);

    printf("\nAll %d tests passed.\n", g_tests_run);
    return 0;
}
