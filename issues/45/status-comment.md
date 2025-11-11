## ⏳ Status Update - Planned for Phase 4 Implementation

This feature request is **valid and planned** for **Phase 4: Community Expansion** (optional enhancement).

**RaspIArduino framework support is NOT yet implemented**, but is included in the platform roadmap as a community-driven feature.

### 📋 Feature Summary

Enable Arduino-compatible API on Raspberry Pi using piduino library, allowing Arduino developers to easily port code to Pi:

```cpp
// Arduino sketch on Raspberry Pi
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

### 🔍 Source

Identified from community fork analysis: **ferbar/platform-linux_arm** (raspiarduino branch)
- **Repository**: https://github.com/ferbar/platform-linux_arm
- **Branch**: raspiarduino
- **Implementation**: Proven working since February 2022

### ✅ Value Proposition

**Pros**:
- Familiar API for Arduino developers
- Easy migration path from Arduino to Raspberry Pi
- Educational value (teaching GPIO with known API)
- Attracts Arduino community to platform

**Considerations**:
- Niche audience (overlap with lgpio/WiringPi)
- External dependency (piduino library)
- Maintenance burden (additional framework)

### 📅 Roadmap Position

**Phase**: Phase 4 - Community Expansion
**Priority**: 🟡 MEDIUM (community-driven)
**Effort**: 4-6 hours implementation
**Timeline**: After Phases 0-3 complete

### 📝 Implementation Tasks

1. Research piduino library (availability, license, maintenance status)
2. Create `builder/frameworks/raspiarduino.py` framework builder
3. Configure board support (add to existing boards or create generic_linux.json)
4. Create example project (raspiarduino-blink)
5. Document Arduino API compatibility and limitations
6. Test on actual Raspberry Pi hardware

### 🎯 Implementation Trigger

This feature will be implemented when:
- ✅ Phase 3 complete (core platform stable)
- ✅ Community demand demonstrated (10+ upvotes or comments)
- ✅ piduino library validated as maintainable
- ✅ Contributor willing to implement and maintain

### 💡 Current Alternatives

While waiting for RaspIArduino:
- **WiringPi**: Similar API, already supported (Phase 2 complete)
- **lgpio**: Modern Linux GPIO approach (Phase 1 complete)
- **Native Arduino IDE**: Run Arduino IDE directly on Pi (no cross-compile)

### 🤝 Call for Contributors

This is an excellent candidate for community contribution:
- Well-defined scope (4-6 hours)
- Clear reference implementation (ferbar fork)
- Isolated feature (minimal integration)
- Good documentation available

**Interested in implementing this?** Comment below or check the detailed assessment in `issues/45/assessment.md`.

### 📚 References

- **Detailed Assessment**: `issues/45/assessment.md`
- **Fork Analysis**: `research/FORK-ANALYSIS.md` (ferbar/platform-linux_arm section)
- **Roadmap**: `research/03-implementation-roadmap.md` (Phase 4 future enhancements)
- **Implementation Guide**: `research/FORK-ROADMAP-CROSSREF.md` (Section 3)

---

**Status**: ⏳ PLANNED (Phase 4, community-driven)
**Labels**: `enhancement`, `future-enhancement`, `phase-4`, `community-contribution-welcome`
**Related Issues**: #35 (debugging), #36 (upload), #34 (PWM HAL)
