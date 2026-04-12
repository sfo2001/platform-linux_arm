// SPDX-License-Identifier: Apache-2.0
/**
 * pwm-hal-sysfs.c — Production sysfs implementations for pwm-hal seam.
 *
 * Linked in production builds.  Replaced by tests/stubs/pwm-hal-sysfs-stub.c
 * in unit-test builds (CMake target test_pwm_hal sets -DUNIT_TESTING=1 and
 * links this file out).
 */
#include "pwm-hal.h"
#include "pwm-hal-internal.h"

#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

/* ---- Seam implementations ---- */

int pwm_sysfs_write(const char *path, const char *value) {
    int fd = open(path, O_WRONLY);
    if (fd < 0) {
        if (errno == EACCES || errno == EPERM)  return PWM_ERROR_PERMISSION;
        if (errno == EBUSY)                      return PWM_ERROR_BUSY;
        if (errno == ENOENT || errno == ENODEV)  return PWM_ERROR_NOT_EXPORTED;
        return PWM_ERROR_IO;
    }

    ssize_t len     = (ssize_t)strlen(value);
    ssize_t written = write(fd, value, (size_t)len);
    close(fd);

    if (written != len) {
        if (errno == EACCES || errno == EPERM)  return PWM_ERROR_PERMISSION;
        if (errno == EBUSY)                      return PWM_ERROR_BUSY;
        if (errno == EINVAL)                     return PWM_ERROR_INVALID_PARAM;
        return PWM_ERROR_IO;
    }

    return PWM_SUCCESS;
}

void pwm_sysfs_sleep_ms(int ms) {
    if (ms <= 0) return;
    usleep((useconds_t)ms * 1000);
}

/* TODO(#124): currently dead code — no caller in pwm-hal.c. */
int pwm_sysfs_read(const char *path, char *value, size_t max_len) {
    int fd = open(path, O_RDONLY);
    if (fd < 0) {
        if (errno == EACCES || errno == EPERM)  return PWM_ERROR_PERMISSION;
        if (errno == ENOENT || errno == ENODEV)  return PWM_ERROR_NOT_EXPORTED;
        return PWM_ERROR_IO;
    }

    if (max_len == 0) {
        close(fd);
        return PWM_ERROR_INVALID_PARAM;
    }

    ssize_t len = read(fd, value, max_len - 1);
    close(fd);

    if (len < 0) return PWM_ERROR_IO;

    value[len] = '\0';
    if (len > 0 && value[len - 1] == '\n') value[len - 1] = '\0';

    return PWM_SUCCESS;
}

bool pwm_is_exported(int chip, int channel) {
    char path[MAX_PATH_LEN];
    struct stat st;
    snprintf(path, sizeof(path), "%s/pwmchip%d/pwm%d", PWM_SYSFS_BASE, chip, channel);
    return (stat(path, &st) == 0 && S_ISDIR(st.st_mode));
}

const pwm_pin_map_t *pwm_get_pin_map(void) {
    /*
     * Heuristic: pwmchip2 exists on Pi 5 (two PWM controllers) but not on
     * Pi 1–4 (single controller, pwmchip0 only).  Known limitation: this
     * detection can produce a false Pi 5 result if pwmchip2 is present for
     * another reason (e.g. a USB PWM adapter), or a false Pi 1–4 result if
     * the Pi 5 pwm overlay is not loaded.  Tracked for improvement in #124.
     */
    struct stat st;
    if (stat("/sys/class/pwm/pwmchip2", &st) == 0 && S_ISDIR(st.st_mode)) {
        return g_pwm_pin_map_pi5;
    }
    return g_pwm_pin_map_pi1_4;
}
