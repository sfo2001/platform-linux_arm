# Fork Features → GitHub Issues Cross-Reference

**Date:** 2025-11-11
**Purpose:** Quick reference mapping fork analysis findings to existing GitHub issues

---

## Fork Features Identified → Issue Status

| Fork Feature | Fork Source | Priority | GitHub Issue | Status |
|--------------|-------------|----------|--------------|--------|
| **ARMv8 64-bit Support** | tsandmann | CRITICAL | ✅ **IMPLEMENTED** | Phase 2, Task 2.2 complete |
| **RPi 3 Board** | tsandmann | MEDIUM | ✅ **IMPLEMENTED** | Included in 9 boards |
| **RPi 4 Board** | Our addition | HIGH | ✅ **IMPLEMENTED** | Phase 0 complete |
| **RPi 5 Board** | Our addition | HIGH | ✅ **IMPLEMENTED** | Phase 1 complete |
| **WiringPi GC2 Update** | Our addition | MEDIUM | ✅ **IMPLEMENTED** | Phase 2, Task 2.3 complete |
| **GDB Remote Debugging** | SRCX-IOTG | HIGH | [Issue #35](https://github.com/sfo2001/platform-linux_arm/issues/35) | 📋 **ISSUE CREATED** |
| **SCP Upload Protocol** | SRCX-IOTG | MEDIUM | [Issue #36](https://github.com/sfo2001/platform-linux_arm/issues/36) | 📋 **ISSUE CREATED** |
| **Remote Test Execution** | Extension | MEDIUM | [Issue #37](https://github.com/sfo2001/platform-linux_arm/issues/37) | 📋 **ISSUE CREATED** |
| **PWM HAL for lgpio** | Our addition | OPTIONAL | [Issue #34](https://github.com/sfo2001/platform-linux_arm/issues/34) | 📋 **ISSUE CREATED** |
| **RaspIArduino Framework** | ferbar | LOW | ❌ **NOT CREATED** | Future consideration |
| **Generic Linux Board** | ferbar | LOW | ❌ **NOT CREATED** | Future consideration |
| **ARTIK Boards** | SRCX-IOTG | N/A | ❌ **SKIP** | Vendor-specific, not relevant |

---

## Implementation Status Summary

### ✅ Already Implemented (5 features)

**From Fork Analysis:**
- ARMv8 64-bit architecture support (tsandmann fork inspiration)
- Raspberry Pi 3 Model B board
- WiringPi GC2 fork update

**Our Additions:**
- Raspberry Pi 4 Model B board
- Raspberry Pi 5 board
- Complete board coverage (9 boards total)
- Modern frameworks (lgpio, WiringPi GC2)
- Multi-platform CI/CD

**Result:** ✅ Our implementation is superior to all forks on core features

---

### 📋 Issues Created - Ready for Implementation (4 features)

#### High Priority Professional Development Tools

**Issue #35: Remote Debugging Support (GDB over SSH)**
- **Source:** SRCX-IOTG fork pattern
- **Priority:** 🔴 HIGH
- **Effort:** 6-8 hours
- **Phase:** Phase 3 Extension or Phase 4 Priority 1
- **URL:** https://github.com/sfo2001/platform-linux_arm/issues/35
- **Status:** Comprehensive requirements documented, ready for implementation

**Issue #36: Custom Upload/Deployment Protocol (SCP/Rsync/SSH)**
- **Source:** SRCX-IOTG fork pattern
- **Priority:** 🟡 MEDIUM
- **Effort:** 4-6 hours
- **Phase:** Phase 3 Extension or Phase 4 Priority 1
- **URL:** https://github.com/sfo2001/platform-linux_arm/issues/36
- **Status:** Requirements for SCP, rsync, SSH documented

**Issue #37: Remote Test Execution on Target Hardware**
- **Source:** Extension of upload/debug patterns
- **Priority:** 🟡 MEDIUM
- **Effort:** 3-4 hours
- **Phase:** Phase 4
- **URL:** https://github.com/sfo2001/platform-linux_arm/issues/37
- **Status:** Complements upload/debug features

#### Optional Enhancement

**Issue #34: Linux PWM Hardware Abstraction Layer (HAL)**
- **Source:** Our research (sysfs /sys/class/pwm)
- **Priority:** 🟢 OPTIONAL
- **Effort:** 6-9 hours
- **Phase:** Deferred (not critical path)
- **URL:** https://github.com/sfo2001/platform-linux_arm/issues/34
- **Status:** Comprehensive specification, can be implemented anytime
- **Note:** Already referenced in roadmap as Task 2.5

---

### ❌ Not Created - Future Consideration (2 features)

**RaspIArduino Framework** (ferbar fork)
- **Priority:** 🟢 LOW
- **Reason:** Niche audience, external dependency (piduino)
- **Decision:** Community-driven, Phase 4 if demand exists
- **Action:** Monitor community interest before creating issue

**Generic Linux Board** (ferbar fork)
- **Priority:** 🟢 LOW
- **Reason:** Flexibility for non-Pi ARM devices
- **Decision:** Phase 4, after Pi ecosystem mature
- **Action:** Part of broader non-Pi board support (existing Priority 6 issues)

---

### ⚫ Skipped - Not Relevant

**Samsung ARTIK Boards** (SRCX-IOTG fork)
- **Reason:** Vendor-specific, discontinued hardware
- **Decision:** Extract patterns (upload/debug), skip boards

---

## Detailed Issue Summaries

### Issue #35: Remote Debugging Support

**Key Requirements:**
- IDE-integrated GDB debugging over SSH
- Support gdbserver on target
- Cross-architecture GDB (armv7 and aarch64)
- SSH tunnel transport
- Breakpoints, stepping, variable inspection
- Configuration via platformio.ini

**Example Configuration:**
```ini
[env:pi4_debug]
board = raspberrypi_4b
debug_tool = gdb
debug_server = ssh
debug_port = 192.168.1.100:2345
debug_ssh_user = pi
debug_ssh_keyfile = ~/.ssh/id_rsa
```

**Success Criteria:**
- Users can click "Debug" in IDE
- Connects automatically to remote gdbserver
- Breakpoints and stepping work
- Clear error messages for setup issues

**Documentation:** Comprehensive requirements in issue #35

---

### Issue #36: Custom Upload/Deployment Protocol

**Key Requirements:**
- Automated deployment via `pio run --target upload`
- Support SCP (simple secure copy)
- Support rsync (incremental sync)
- Support SSH (optional post-deploy execution)
- SSH key authentication
- Configurable target paths
- Multi-target support

**Example Configuration:**
```ini
[env:pi4_deploy]
board = raspberrypi_4b
upload_protocol = scp
upload_host = 192.168.1.100
upload_user = pi
upload_port = 22
upload_path = /home/pi/projects/myapp
upload_ssh_keyfile = ~/.ssh/id_rsa
upload_flags = --chmod=755
```

**Success Criteria:**
- Users configure target in platformio.ini
- Click "Upload" in IDE
- Binary automatically transferred to remote Pi
- Executable permissions preserved
- Completes in <10 seconds

**Documentation:** Comprehensive requirements in issue #36

---

### Issue #37: Remote Test Execution

**Key Requirements:**
- Run tests on actual hardware via `pio test`
- SSH transport to target
- Capture test output
- Support Unity test framework
- Clear pass/fail reporting

**Example Configuration:**
```ini
[env:pi4_test]
board = raspberrypi_4b
test_transport = ssh
test_host = 192.168.1.100
test_user = pi
```

**Success Criteria:**
- Users run `pio test`
- Tests execute on remote Pi
- Output captured and displayed
- Pass/fail clearly reported

**Documentation:** Requirements in issue #37

---

### Issue #34: Linux PWM HAL

**Key Requirements:**
- Hardware PWM via `/sys/class/pwm` sysfs
- User-friendly GPIO pin API
- Auto-detection of PWM chips
- Board-specific pin mapping tables
- Support all Pi models (1-5)
- Example: LED fade

**Example Usage:**
```c
#include <pwm_hal.h>

int main() {
    // GPIO18 on Pi 4 maps to PWM0
    pwm_init(18, 1000);  // 1kHz frequency
    pwm_write(18, 50);    // 50% duty cycle

    // Fade LED
    for (int i = 0; i <= 100; i++) {
        pwm_write(18, i);
        usleep(10000);
    }

    pwm_deinit(18);
    return 0;
}
```

**Success Criteria:**
- User-friendly API accepting GPIO pin numbers
- Transparent sysfs operations
- Works on all Pi models
- Clear error messages
- Comprehensive documentation

**Documentation:** Full specification in issue #34

---

## Phase Recommendations

### Phase 3 Extension (Optional - 8-12 hours)

**Professional Development Tools Bundle:**
- Issue #35: GDB remote debugging (6-8h)
- Issue #36: SCP/rsync upload (4-6h)

**Value:**
- Enables professional remote development workflow
- Headless Pi deployment
- IDE-integrated debugging

**Decision Point:**
- Implement if targeting professional developers
- Can defer to Phase 4 if focusing on getting core platform stable

---

### Phase 4 (Community & Enhancement - 15-20 hours)

**Remote Workflow Complete:**
- Issue #37: Remote test execution (3-4h)
- Testing and documentation refinement (2-3h)

**Optional Enhancements:**
- Issue #34: PWM HAL (6-9h) - Community-driven
- RaspIArduino framework (4-6h) - If demand exists

**Non-Pi Board Support:**
- Existing Priority 6 issues (#31, #30, #29, #25, #24, #22)
- Batch implementation (10-15h total)

---

## Usage Guide

### For Implementers

**To implement a feature from fork analysis:**

1. **Check this document** - Is there already a GitHub issue?
2. **Read the issue** - Requirements and acceptance criteria documented
3. **Reference fork code** - See FORK-ANALYSIS.md and FORK-ROADMAP-CROSSREF.md
4. **Follow patterns** - Implementation guidance in cross-reference document
5. **Test thoroughly** - Cross-platform and hardware validation
6. **Update roadmap** - Mark task complete, update status

### For Project Managers

**Priority decision matrix:**

| Feature | Issue | Effort | Impact | Priority |
|---------|-------|--------|--------|----------|
| GDB Debugging | #35 | 6-8h | HIGH | Phase 3 ext or Phase 4 P1 |
| Upload Protocols | #36 | 4-6h | MEDIUM | Phase 3 ext or Phase 4 P1 |
| Remote Testing | #37 | 3-4h | MEDIUM | Phase 4 |
| PWM HAL | #34 | 6-9h | LOW | Phase 4 optional |

**Recommendation:**
- **Core platform complete** (Phases 0-3) → Production-ready
- **Add #35 + #36** → Professional development experience
- **Add #34 + #37** → Complete feature set
- **RaspIArduino** → Community-driven, if demand exists

### For Contributors

**Want to contribute? Choose an issue:**

**Good First Issues:**
- Issue #36: Upload protocols (moderate complexity, clear scope)
- Issue #34: PWM HAL (optional, well-specified)

**Experienced Contributors:**
- Issue #35: GDB debugging (complex, requires debug protocol knowledge)
- Issue #37: Remote testing (requires understanding of test frameworks)

**All issues have:**
- ✅ Comprehensive requirements
- ✅ Acceptance criteria
- ✅ Implementation considerations
- ✅ Example configurations
- ✅ Success criteria

---

## Document Maintenance

**Update this document when:**
- New issues created from fork analysis
- Issues implemented and closed
- New forks discovered with valuable features
- Priorities change based on community feedback

**Cross-references:**
- `research/FORK-ANALYSIS.md` - Detailed fork investigation
- `research/FORK-ROADMAP-CROSSREF.md` - Feature-by-feature comparison
- `research/FORK-ANALYSIS-SUMMARY.md` - Executive summary
- `research/03-implementation-roadmap.md` - Implementation phases
- `research/00-INDEX.md` - Research progress tracker

---

**Last Updated:** 2025-11-11
**Issues Tracked:** 4 created, 2 future consideration, 1 skipped
**Implementation Status:** 5 features complete, 4 issues ready for implementation
**Next Review:** After Phase 3 complete or when new forks discovered
