// SPDX-License-Identifier: Apache-2.0
/**
 * PWM Hardware Abstraction Layer (HAL) Implementation
 *
 * Implements hardware PWM control using the Linux kernel PWM subsystem via
 * sysfs (/sys/class/pwm/pwmchipX/). Provides comprehensive error handling
 * for permissions, busy channels, invalid pins, and hardware limitations.
 *
 * @file pwm-hal.c
 * @author PlatformIO Linux ARM Platform
 * @version 1.0.0
 * @date 2025-11-12
 */

#include "pwm-hal.h"
#include "pwm-hal-internal.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

/* ============================================================================
 * Internal Data Structures and Constants
 * ============================================================================ */

/**
 * @brief PWM state tracking for each channel
 */
typedef struct {
    int gpio_pin;              /**< GPIO pin number (BCM), -1 if unused */
    int pwm_chip;              /**< PWM chip number */
    int pwm_channel;           /**< PWM channel (0 or 1) */
    bool is_exported;          /**< Channel exported to userspace */
    bool is_enabled;           /**< PWM output enabled */
    uint32_t frequency_hz;     /**< Current frequency in Hz */
    float duty_cycle_percent;  /**< Current duty cycle (0.0-100.0%) */
    pwm_polarity_t polarity;   /**< Current polarity */
} pwm_channel_state_t;

/* Maximum number of PWM channels to track */
#define MAX_PWM_CHANNELS 8

/* Global state tracking array */
static pwm_channel_state_t g_pwm_channels[MAX_PWM_CHANNELS];
static bool g_pwm_initialized = false;

/* Maximum string length for reading/writing sysfs values */
#define MAX_VALUE_LEN 64

/* Pin maps defined here (always linked). Sysfs implementations: see pwm-hal-sysfs.c */

/**
 * Pi 1-4: pwmchip0
 * - GPIO 12 -> PWM0 (chip 0, channel 0)
 * - GPIO 13 -> PWM1 (chip 0, channel 1)
 * - GPIO 18 -> PWM0 (chip 0, channel 0) [conflicts with GPIO 12]
 * - GPIO 19 -> PWM1 (chip 0, channel 1) [conflicts with GPIO 13]
 *
 * Pi 5: pwmchip2/3 (RP1 chip)
 * - GPIO 12 -> PWM0 (chip 2, channel 0)
 * - GPIO 13 -> PWM1 (chip 2, channel 1)
 * - GPIO 18 -> PWM0 (chip 2, channel 0) [conflicts with GPIO 12]
 * - GPIO 19 -> PWM1 (chip 2, channel 1) [conflicts with GPIO 13]
 *
 * Note: GPIO 18/19 share the same PWM channels as GPIO 12/13.
 * Using both simultaneously requires additional conflict detection.
 */
const pwm_pin_map_t g_pwm_pin_map_pi1_4[] = {
    {12, 0, 0},  // GPIO 12 -> pwmchip0, channel 0
    {13, 0, 1},  // GPIO 13 -> pwmchip0, channel 1
    {18, 0, 0},  // GPIO 18 -> pwmchip0, channel 0 (alt function)
    {19, 0, 1},  // GPIO 19 -> pwmchip0, channel 1 (alt function)
    {-1, -1, -1} // Sentinel
};

const pwm_pin_map_t g_pwm_pin_map_pi5[] = {
    {12, 2, 0},  // GPIO 12 -> pwmchip2, channel 0
    {13, 2, 1},  // GPIO 13 -> pwmchip2, channel 1
    {18, 2, 0},  // GPIO 18 -> pwmchip2, channel 0 (alt function)
    {19, 2, 1},  // GPIO 19 -> pwmchip2, channel 1 (alt function)
    {-1, -1, -1} // Sentinel
};

/* ============================================================================
 * Internal Helper Functions
 * ============================================================================ */

static void pwm_init_state(void); /* forward declaration — defined below UNIT_TESTING block */

#ifdef UNIT_TESTING
/**
 * @brief Reset all PWM state for unit tests.
 *
 * Called at the start of each test case.  Only compiled with -DUNIT_TESTING=1.
 */
void pwm_reset_state_for_testing(void) {
    g_pwm_initialized = false;
    for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
        g_pwm_channels[i].gpio_pin          = -1;
        g_pwm_channels[i].pwm_chip          = -1;
        g_pwm_channels[i].pwm_channel       = -1;
        g_pwm_channels[i].is_exported       = false;
        g_pwm_channels[i].is_enabled        = false;
        g_pwm_channels[i].frequency_hz      = 0;
        g_pwm_channels[i].duty_cycle_percent = 0.0f;
        g_pwm_channels[i].polarity          = PWM_POLARITY_NORMAL;
    }
}

/**
 * @brief Fill all state slots with dummy entries to simulate slot exhaustion.
 *
 * Populates every g_pwm_channels slot with a fictional gpio_pin (100+i) and
 * chip=0, channel=1 so that a subsequent pwm_init() for any real pin passes
 * the conflict check (channel 0 is unused) but fails pwm_alloc_state() with
 * NULL, causing pwm_init() to return PWM_ERROR_HARDWARE.
 *
 * Called at the start of the slot-exhaustion test case only.
 * Only compiled with -DUNIT_TESTING=1.
 */
void pwm_fill_channels_for_testing(void) {
    pwm_init_state(); /* mark initialized so pwm_init() won't wipe slots on entry */
    for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
        g_pwm_channels[i].gpio_pin   = 100 + i; /* fictional pins, not in pin map */
        g_pwm_channels[i].pwm_chip   = 0;
        g_pwm_channels[i].pwm_channel = 1;       /* ch=1 ≠ ch=0 used by GPIO 18 */
    }
}
#endif /* UNIT_TESTING */

/**
 * @brief Initialize global state tracking on first use
 */
static void pwm_init_state(void) {
    if (!g_pwm_initialized) {
        for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
            g_pwm_channels[i].gpio_pin = -1;
            g_pwm_channels[i].pwm_chip = -1;
            g_pwm_channels[i].pwm_channel = -1;
            g_pwm_channels[i].is_exported = false;
            g_pwm_channels[i].is_enabled = false;
            g_pwm_channels[i].frequency_hz = 0;
            g_pwm_channels[i].duty_cycle_percent = 0.0f;
            g_pwm_channels[i].polarity = PWM_POLARITY_NORMAL;
        }
        g_pwm_initialized = true;
    }
}

/**
 * @brief Find state entry for a GPIO pin
 *
 * @param pin GPIO pin number
 * @return Pointer to state entry, or NULL if not found
 */
static pwm_channel_state_t* pwm_find_state(int pin) {
    pwm_init_state();

    for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
        if (g_pwm_channels[i].gpio_pin == pin) {
            return &g_pwm_channels[i];
        }
    }
    return NULL;
}

/**
 * @brief Allocate state entry for a GPIO pin
 *
 * @param pin GPIO pin number
 * @param chip PWM chip number
 * @param channel PWM channel number
 * @return Pointer to allocated state entry, or NULL if no slots available
 */
static pwm_channel_state_t* pwm_alloc_state(int pin, int chip, int channel) {
    pwm_init_state();

    // Check if already allocated
    pwm_channel_state_t* existing = pwm_find_state(pin);
    if (existing) {
        return existing;
    }

    // Find free slot
    for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
        if (g_pwm_channels[i].gpio_pin == -1) {
            g_pwm_channels[i].gpio_pin = pin;
            g_pwm_channels[i].pwm_chip = chip;
            g_pwm_channels[i].pwm_channel = channel;
            return &g_pwm_channels[i];
        }
    }

    return NULL; // No free slots
}

/**
 * @brief Free state entry for a GPIO pin
 *
 * @param pin GPIO pin number
 */
static void pwm_free_state(int pin) {
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (state) {
        state->gpio_pin = -1;
        state->pwm_chip = -1;
        state->pwm_channel = -1;
        state->is_exported = false;
        state->is_enabled = false;
        state->frequency_hz = 0;
        state->duty_cycle_percent = 0.0f;
        state->polarity = PWM_POLARITY_NORMAL;
    }
}

/**
 * @brief Export PWM channel to userspace
 *
 * @param chip PWM chip number
 * @param channel PWM channel number
 * @return PWM_SUCCESS on success, error code on failure
 */
static int pwm_export(int chip, int channel) {
    char path[MAX_PATH_LEN];
    char value[MAX_VALUE_LEN];

    // Check if already exported
    if (pwm_is_exported(chip, channel)) {
        return PWM_SUCCESS;
    }

    // Export channel
    snprintf(path, sizeof(path), "%s/pwmchip%d/export", PWM_SYSFS_BASE, chip);
    snprintf(value, sizeof(value), "%d", channel);

    int result = pwm_sysfs_write(path, value);
    if (result != PWM_SUCCESS) {
        return result;
    }

    // Wait for sysfs to create the channel directory (up to 100ms)
    for (int i = 0; i < PWM_EXPORT_RETRIES; i++) {
        if (pwm_is_exported(chip, channel)) {
            return PWM_SUCCESS;
        }
        pwm_sysfs_sleep_ms(10); /* 10ms; no-op in unit-test builds */
    }

    return PWM_ERROR_IO; // Export didn't complete in time
}

/**
 * @brief Unexport PWM channel from userspace
 *
 * @param chip PWM chip number
 * @param channel PWM channel number
 * @return PWM_SUCCESS on success, error code on failure
 */
static int pwm_unexport(int chip, int channel) {
    char path[MAX_PATH_LEN];
    char value[MAX_VALUE_LEN];

    // Check if already unexported
    if (!pwm_is_exported(chip, channel)) {
        return PWM_SUCCESS;
    }

    /* Disable before unexporting — best-effort; unexport proceeds regardless of result. */
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, chip, channel);
    (void)pwm_sysfs_write(path, "0");

    // Unexport channel
    snprintf(path, sizeof(path), "%s/pwmchip%d/unexport", PWM_SYSFS_BASE, chip);
    snprintf(value, sizeof(value), "%d", channel);

    return pwm_sysfs_write(path, value);
}

/* ============================================================================
 * Public API Implementation - Core Functions
 * ============================================================================ */

int pwm_init(int pin, uint32_t freq_hz) {
    int chip, channel;
    int result;

    pwm_init_state();   // explicit; pwm_find_state also calls this — defense in depth

    // Validate frequency
    if (freq_hz < PWM_MIN_FREQUENCY_HZ || freq_hz > PWM_MAX_FREQUENCY_HZ) {
        return PWM_ERROR_INVALID_PARAM;
    }

    // Get chip and channel for this pin
    result = pwm_get_chip_channel(pin, &chip, &channel);
    if (result != PWM_SUCCESS) {
        return result;
    }

    // Check for conflicting channel usage
    // GPIO 12/18 share PWM0, GPIO 13/19 share PWM1
    for (int i = 0; i < MAX_PWM_CHANNELS; i++) {
        if (g_pwm_channels[i].gpio_pin != -1 &&
            g_pwm_channels[i].gpio_pin != pin &&
            g_pwm_channels[i].pwm_chip == chip &&
            g_pwm_channels[i].pwm_channel == channel) {
            // Channel already in use by a different pin
            return PWM_ERROR_BUSY;
        }
    }

    // Allocate state entry
    pwm_channel_state_t* state = pwm_alloc_state(pin, chip, channel);
    if (!state) {
        return PWM_ERROR_HARDWARE; // Out of state slots
    }

    // Export channel
    result = pwm_export(chip, channel);
    if (result != PWM_SUCCESS) {
        pwm_free_state(pin);
        return result;
    }
    state->is_exported = true;

    // Calculate period in nanoseconds
    uint64_t period_ns = 1000000000ULL / freq_hz;

    // Set period
    char path[MAX_PATH_LEN];
    char value[MAX_VALUE_LEN];
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/period",
             PWM_SYSFS_BASE, chip, channel);
    snprintf(value, sizeof(value), "%llu", (unsigned long long)period_ns);
    result = pwm_sysfs_write(path, value);
    if (result != PWM_SUCCESS) {
        pwm_unexport(chip, channel);
        pwm_free_state(pin);
        return result;
    }

    // Set duty cycle to 0 initially
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/duty_cycle",
             PWM_SYSFS_BASE, chip, channel);
    result = pwm_sysfs_write(path, "0");
    if (result != PWM_SUCCESS) {
        pwm_unexport(chip, channel);
        pwm_free_state(pin);
        return result;
    }

    // Enable PWM output
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, chip, channel);
    result = pwm_sysfs_write(path, "1");
    if (result != PWM_SUCCESS) {
        pwm_unexport(chip, channel);
        pwm_free_state(pin);
        return result;
    }

    // Update state
    state->is_enabled = true;
    state->frequency_hz = freq_hz;
    state->duty_cycle_percent = 0.0f;
    state->polarity = PWM_POLARITY_NORMAL;

    return PWM_SUCCESS;
}

int pwm_write(int pin, float duty_cycle_percent) {
    // Validate duty cycle
    if (duty_cycle_percent < PWM_MIN_DUTY_CYCLE ||
        duty_cycle_percent > PWM_MAX_DUTY_CYCLE) {
        return PWM_ERROR_INVALID_PARAM;
    }

    // Find state
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_ERROR_NOT_EXPORTED;
    }

    // Calculate duty cycle in nanoseconds
    uint64_t period_ns = 1000000000ULL / state->frequency_hz;
    uint64_t duty_cycle_ns = (uint64_t)((double)period_ns * ((double)duty_cycle_percent / 100.0));

    // Set duty cycle
    char path[MAX_PATH_LEN];
    char value[MAX_VALUE_LEN];
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/duty_cycle",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    snprintf(value, sizeof(value), "%llu", (unsigned long long)duty_cycle_ns);

    int result = pwm_sysfs_write(path, value);
    if (result != PWM_SUCCESS) {
        return result;
    }

    // Update state
    state->duty_cycle_percent = duty_cycle_percent;

    return PWM_SUCCESS;
}

int pwm_deinit(int pin) {
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_SUCCESS; // Already deinitialized
    }

    // Unexport channel
    int result = pwm_unexport(state->pwm_chip, state->pwm_channel);

    // Free state regardless of unexport result
    pwm_free_state(pin);

    return result;
}

/* ============================================================================
 * Public API Implementation - Extended Functions
 * ============================================================================ */

int pwm_set_frequency(int pin, uint32_t freq_hz) {
    // Validate frequency
    if (freq_hz < PWM_MIN_FREQUENCY_HZ || freq_hz > PWM_MAX_FREQUENCY_HZ) {
        return PWM_ERROR_INVALID_PARAM;
    }

    // Find state
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_ERROR_NOT_EXPORTED;
    }

    // Calculate new period
    uint64_t period_ns = 1000000000ULL / freq_hz;

    // Disable output before changing period
    char path[MAX_PATH_LEN];
    char value[MAX_VALUE_LEN];
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    int result = pwm_sysfs_write(path, "0");
    if (result != PWM_SUCCESS) {
        return result;
    }

    // Set new period
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/period",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    snprintf(value, sizeof(value), "%llu", (unsigned long long)period_ns);
    result = pwm_sysfs_write(path, value);
    if (result != PWM_SUCCESS) {
        // Try to re-enable with old settings
        snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
                 PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
        int re_enable_result = pwm_sysfs_write(path, "1");
        if (re_enable_result != PWM_SUCCESS) {
            state->is_enabled = false;
        }
        return result;
    }

    // Update duty cycle to maintain percentage
    uint64_t duty_cycle_ns = (uint64_t)((double)period_ns * ((double)state->duty_cycle_percent / 100.0));
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/duty_cycle",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    snprintf(value, sizeof(value), "%llu", (unsigned long long)duty_cycle_ns);
    result = pwm_sysfs_write(path, value);
    if (result != PWM_SUCCESS) {
        // Try to re-enable with new period and zero duty cycle
        snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
                 PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
        int re_enable_result = pwm_sysfs_write(path, "1");
        if (re_enable_result != PWM_SUCCESS) {
            state->is_enabled = false;
        }
        return result;
    }

    // Re-enable output
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_write(path, "1");
    if (result != PWM_SUCCESS) {
        state->is_enabled = false;
        return result;
    }

    // Update state
    state->frequency_hz = freq_hz;

    return PWM_SUCCESS;
}

int pwm_set_polarity(int pin, pwm_polarity_t polarity) {
    // Validate polarity
    if (polarity != PWM_POLARITY_NORMAL && polarity != PWM_POLARITY_INVERTED) {
        return PWM_ERROR_INVALID_PARAM;
    }

    // Find state
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_ERROR_NOT_EXPORTED;
    }

    // Disable output before changing polarity
    char path[MAX_PATH_LEN];
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    int result = pwm_sysfs_write(path, "0");
    if (result != PWM_SUCCESS) {
        return result;
    }

    // Set polarity
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/polarity",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    /* kernel sysfs uses "inversed" (not "inverted") — see Documentation/driver-api/pwm.rst */
    const char* polarity_str = (polarity == PWM_POLARITY_NORMAL) ? "normal" : "inversed";
    result = pwm_sysfs_write(path, polarity_str);
    if (result != PWM_SUCCESS) {
        // Try to re-enable with old polarity
        snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
                 PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
        int re_enable_result = pwm_sysfs_write(path, "1");
        if (re_enable_result != PWM_SUCCESS) {
            state->is_enabled = false;
        }
        return result;
    }

    // Re-enable output
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_write(path, "1");
    if (result != PWM_SUCCESS) {
        state->is_enabled = false;
        return result;
    }

    // Update state
    state->polarity = polarity;

    return PWM_SUCCESS;
}

int pwm_get_state(int pin, pwm_state_t *status) {
    if (!status) {
        return PWM_ERROR_INVALID_PARAM;
    }

    // Find state
    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_ERROR_NOT_EXPORTED;
    }

    // Fill status structure
    status->gpio_pin = state->gpio_pin;
    status->pwm_chip = state->pwm_chip;
    status->pwm_channel = state->pwm_channel;
    status->is_enabled = state->is_enabled;
    status->is_exported = state->is_exported;
    status->frequency_hz = state->frequency_hz;
    status->duty_cycle_percent = state->duty_cycle_percent;
    status->polarity = state->polarity;
    status->period_ns = 1000000000ULL / state->frequency_hz;
    status->duty_cycle_ns = (uint64_t)((double)status->period_ns * ((double)state->duty_cycle_percent / 100.0));

    return PWM_SUCCESS;
}

int pwm_sample_hardware(int pin, pwm_state_t *status) {
    char path[MAX_PATH_LEN];
    char buf[MAX_VALUE_LEN];
    int result;

    if (!status) {
        return PWM_ERROR_INVALID_PARAM;
    }

    pwm_channel_state_t* state = pwm_find_state(pin);
    if (!state) {
        return PWM_ERROR_NOT_EXPORTED;
    }

    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/period",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_read(path, buf, sizeof(buf));
    if (result != PWM_SUCCESS) {
        return result;
    }
    char *end_ptr;
    uint64_t period_ns = strtoull(buf, &end_ptr, 10);
    if (end_ptr == buf || (*end_ptr != '\0' && *end_ptr != '\n') || period_ns == 0) {
        return PWM_ERROR_IO;
    }

    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/duty_cycle",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_read(path, buf, sizeof(buf));
    if (result != PWM_SUCCESS) {
        return result;
    }
    uint64_t duty_cycle_ns = strtoull(buf, &end_ptr, 10);
    if (end_ptr == buf || (*end_ptr != '\0' && *end_ptr != '\n')) {
        return PWM_ERROR_IO;
    }

    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/enable",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_read(path, buf, sizeof(buf));
    if (result != PWM_SUCCESS) {
        return result;
    }
    int enable_val = 0;
    if (sscanf(buf, "%d", &enable_val) != 1) {
        return PWM_ERROR_IO;
    }

    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d/polarity",
             PWM_SYSFS_BASE, state->pwm_chip, state->pwm_channel);
    result = pwm_sysfs_read(path, buf, sizeof(buf));
    if (result != PWM_SUCCESS) {
        return result;
    }
    /* kernel sysfs uses "inversed" (not "inverted") — see Documentation/driver-api/pwm.rst.
     * Relies on pwm_sysfs_read() stripping the trailing '\n'; the production
     * implementation (pwm-hal-sysfs.c) does this unconditionally. */
    pwm_polarity_t polarity;
    if (strcmp(buf, "normal") == 0) {
        polarity = PWM_POLARITY_NORMAL;
    } else if (strcmp(buf, "inversed") == 0) {
        polarity = PWM_POLARITY_INVERTED;
    } else {
        return PWM_ERROR_IO;
    }

    /* Clamp raw duty_cycle_ns so the caller also sees a bounded nanosecond
     * value, not just a bounded percentage.  A sysfs race could deliver a
     * duty_cycle > period snapshot; cap it before storing. */
    if (duty_cycle_ns > period_ns) duty_cycle_ns = period_ns;

    status->gpio_pin          = state->gpio_pin;
    status->pwm_chip          = state->pwm_chip;
    status->pwm_channel       = state->pwm_channel;
    status->is_exported       = state->is_exported;
    status->period_ns         = period_ns;
    status->duty_cycle_ns     = duty_cycle_ns;
    status->is_enabled        = (enable_val != 0);
    status->polarity          = polarity;
    status->frequency_hz      = (uint32_t)(1000000000ULL / period_ns);
    status->duty_cycle_percent = (float)((double)duty_cycle_ns / (double)period_ns * 100.0);
    if (status->duty_cycle_percent > 100.0f) status->duty_cycle_percent = 100.0f;
    /* defensive: duty_cycle_ns is uint64_t, cannot be negative */
    if (status->duty_cycle_percent < 0.0f)   status->duty_cycle_percent = 0.0f;

    return PWM_SUCCESS;
}

bool pwm_is_enabled(int pin) {
    pwm_channel_state_t* state = pwm_find_state(pin);
    return (state && state->is_enabled);
}

/* ============================================================================
 * Public API Implementation - Utility Functions
 * ============================================================================ */

const char* pwm_error_string(pwm_error_t error) {
    switch (error) {
        case PWM_SUCCESS:
            return "Success";
        case PWM_ERROR_INVALID_PIN:
            return "GPIO pin does not support PWM";
        case PWM_ERROR_PERMISSION:
            return "Permission denied (run setup-pwm-perms.sh)";
        case PWM_ERROR_BUSY:
            return "PWM channel already in use";
        case PWM_ERROR_NOT_EXPORTED:
            return "PWM channel not exported";
        case PWM_ERROR_INVALID_PARAM:
            return "Invalid parameter value";
        case PWM_ERROR_IO:
            return "I/O error accessing sysfs";
        case PWM_ERROR_NOT_ENABLED:
            return "PWM channel not enabled";
        case PWM_ERROR_HARDWARE:
            return "Hardware-specific limitation";
        default:
            return "Unknown error";
    }
}

bool pwm_pin_is_valid(int pin) {
    const pwm_pin_map_t* map = pwm_get_pin_map();

    for (int i = 0; map[i].gpio_pin != -1; i++) {
        if (map[i].gpio_pin == pin) {
            return true;
        }
    }

    return false;
}

int pwm_get_chip_channel(int pin, int *chip, int *channel) {
    if (!chip || !channel) {
        return PWM_ERROR_INVALID_PARAM;
    }

    const pwm_pin_map_t* map = pwm_get_pin_map();

    for (int i = 0; map[i].gpio_pin != -1; i++) {
        if (map[i].gpio_pin == pin) {
            *chip = map[i].pwm_chip;
            *channel = map[i].pwm_channel;
            return PWM_SUCCESS;
        }
    }

    return PWM_ERROR_INVALID_PIN;
}
