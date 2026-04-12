// SPDX-License-Identifier: Apache-2.0
/**
 * pwm-hal-sysfs-stub.c — Test stub for the pwm-hal sysfs seam.
 *
 * Implements the four seam functions declared in pwm-hal-internal.h without
 * touching the filesystem.  Export state is tracked in a small table.
 */
#include "pwm-hal-sysfs-stub.h"
#include "pwm-hal-internal.h"
#include "pwm-hal.h"

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/* Tracks which chip+channel pairs have been exported. */
/* Chips 0..7, channels 0..1 — matches MAX_PWM_CHANNELS and HAL limits. */
#define STUB_MAX_CHIPS    8
#define STUB_MAX_CHANNELS 2

static bool s_use_pi5;
static bool s_exported[STUB_MAX_CHIPS][STUB_MAX_CHANNELS];
static int  s_export_delay_remaining;
static bool s_export_written;
static const char *s_write_fail_suffix;
static int         s_write_fail_error;

/* ---- Stub control ---- */

void stub_reset(void) {
    s_use_pi5 = false;
    s_export_delay_remaining = 0;
    s_export_written = false;
    s_write_fail_suffix = NULL;
    s_write_fail_error  = 0;
    for (int c = 0; c < STUB_MAX_CHIPS; c++) {
        for (int ch = 0; ch < STUB_MAX_CHANNELS; ch++) {
            s_exported[c][ch] = false;
        }
    }
}

void stub_set_pi5(bool is_pi5) {
    s_use_pi5 = is_pi5;
}

void stub_set_export_delay(int n_failures) {
    s_export_delay_remaining = n_failures;
}

void stub_set_write_fail_on(const char *path_suffix, int error_code) {
    s_write_fail_suffix = path_suffix;
    s_write_fail_error  = error_code;
}

/* ---- Seam function implementations ---- */

void pwm_sysfs_sleep_ms(int ms) {
    (void)ms; /* no-op in unit-test builds — delays are not modelled */
}

int pwm_sysfs_write(const char *path, const char *value) {
    int chip;
    /*
     * One-shot write failure injection: if a suffix was registered via
     * stub_set_write_fail_on(), check whether this path ends with it.
     * If it matches, consume the one-shot and return the configured error.
     */
    if (s_write_fail_suffix != NULL) {
        size_t plen = strlen(path);
        size_t slen = strlen(s_write_fail_suffix);
        if (plen >= slen && strcmp(path + plen - slen, s_write_fail_suffix) == 0) {
            s_write_fail_suffix = NULL; /* consume — one-shot */
            return s_write_fail_error;
        }
    }
    /*
     * Detect export/unexport by matching the sysfs path pattern.
     * The prefix "/sys/class/pwm/pwmchipN/" is derived from PWM_SYSFS_BASE
     * (defined in pwm-hal-internal.h).  If PWM_SYSFS_BASE changes, update
     * the sscanf format strings below to match.
     *
     *   PWM_SYSFS_BASE "/pwmchipN/export"   → mark chip N, channel=value exported
     *   PWM_SYSFS_BASE "/pwmchipN/unexport" → mark chip N, channel=value unexported
     * All other paths succeed silently (period, duty_cycle, enable, polarity).
     */
    if (sscanf(path, "/sys/class/pwm/pwmchip%d/export", &chip) == 1) {
        int channel = -1;
        /*
         * Parse channel from value string.  Use sscanf so malformed input
         * returns an out-of-range channel that the bounds check below rejects,
         * rather than silently returning 0 (atoi behaviour).
         */
        if (sscanf(value, "%d", &channel) != 1) {
            channel = -1;
        }
        if (chip >= 0 && chip < STUB_MAX_CHIPS &&
            channel >= 0 && channel < STUB_MAX_CHANNELS) {
            s_exported[chip][channel] = true;
            s_export_written = true;
        }
        return PWM_SUCCESS;
    }
    if (sscanf(path, "/sys/class/pwm/pwmchip%d/unexport", &chip) == 1) {
        int channel = -1;
        /*
         * Parse channel from value string.  Use sscanf so malformed input
         * returns an out-of-range channel that the bounds check below rejects,
         * rather than silently returning 0 (atoi behaviour).
         */
        if (sscanf(value, "%d", &channel) != 1) {
            channel = -1;
        }
        if (chip >= 0 && chip < STUB_MAX_CHIPS &&
            channel >= 0 && channel < STUB_MAX_CHANNELS) {
            s_exported[chip][channel] = false;
        }
        return PWM_SUCCESS;
    }
    return PWM_SUCCESS;
}

int pwm_sysfs_read(const char *path, char *value, size_t max_len) {
    (void)path;
    /* Return a safe default — tests that need specific read values should
     * extend the stub with a per-path override table. */
    if (max_len > 0) {
        strncpy(value, "0", max_len);
        value[max_len - 1] = '\0';
    }
    return PWM_SUCCESS;
}

bool pwm_is_exported(int chip, int channel) {
    if (chip < 0 || chip >= STUB_MAX_CHIPS)         return false;
    if (channel < 0 || channel >= STUB_MAX_CHANNELS) return false;
    if (!s_exported[chip][channel])                  return false;
    /* Simulate delayed sysfs directory creation for timeout path testing.
     * The delay counter only activates once the export write has been seen,
     * so pre-write calls to pwm_is_exported() cannot prematurely consume it. */
    if (s_export_written && s_export_delay_remaining > 0) {
        s_export_delay_remaining--;
        return false;
    }
    return true;
}

const pwm_pin_map_t *pwm_get_pin_map(void) {
    return s_use_pi5 ? g_pwm_pin_map_pi5 : g_pwm_pin_map_pi1_4;
}
