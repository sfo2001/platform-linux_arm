# [Round Number] - [Analysis Topic]

**Date**: YYYY-MM-DD
**Round**: [1, 2, 3, etc.]
**Status**: [In Progress | Complete | Needs Revision]
**Related Documents**: [Links to other research docs this builds on]

---

## Executive Summary

*(2-3 paragraph overview of key findings and recommendations)*

**Critical Findings**:
- [Most important discovery 1]
- [Most important discovery 2]
- [Most important discovery 3]

**Recommended Actions**:
1. [Top priority action]
2. [Second priority action]
3. [Third priority action]

---

## Detailed Findings

### [Finding Category 1]

**Current State**:
- [What exists now in platform-linux_arm]
- [Specific issues or limitations]

**Reference Platform Approach**:
- [How platform-espressif32 handles this] - *[See REFERENCES.md: link]*
- [How platform-raspberrypi handles this] - *[See REFERENCES.md: link]*

**Key Patterns Identified**:
1. [Pattern 1]: [Brief description]
2. [Pattern 2]: [Brief description]

**Gap Analysis**:
| Aspect | platform-linux_arm | Reference Platforms | Gap Level |
|--------|-------------------|---------------------|-----------|
| [Aspect 1] | [Current state] | [Expected state] | 🔴 Critical / 🟡 Medium / 🟢 Minor |
| [Aspect 2] | [Current state] | [Expected state] | 🔴 Critical / 🟡 Medium / 🟢 Minor |

**References**:
- [Specific file/line reference 1] - *[See REFERENCES.md: link]*
- [Specific file/line reference 2] - *[See REFERENCES.md: link]*

---

### [Finding Category 2]

*(Repeat structure above for each major finding category)*

---

## Comparative Analysis

### Feature Comparison Matrix

| Feature | linux_arm (current) | espressif32 | raspberrypi | Priority |
|---------|---------------------|-------------|-------------|----------|
| [Feature 1] | ❌ / ⚠️ / ✅ | ✅ | ✅ | High / Medium / Low |
| [Feature 2] | ❌ / ⚠️ / ✅ | ✅ | ✅ | High / Medium / Low |

**Legend**:
- ✅ Fully implemented
- ⚠️ Partially implemented or broken
- ❌ Not implemented

---

## Technical Insights

### [Insight 1]: [Title]

**Observation**: [What was discovered]

**Implications**: [Why this matters for platform-linux_arm]

**Implementation Note**: [How to apply this - high-level only, detailed in roadmap]

**Reference**: *[See REFERENCES.md: link]*

---

## Blockers & Dependencies

### Critical Blockers
1. **[Blocker 1]**
   - **Impact**: [What this prevents]
   - **Root Cause**: [Why this is broken]
   - **Dependency**: [What needs to happen first]

2. **[Blocker 2]**
   *(same structure)*

### Dependencies
- [Dependency 1]: Requires [X] before [Y] can be implemented
- [Dependency 2]: [Reference platform feature] depends on [core capability]

---

## Priority Ranking

Based on this analysis, prioritize the following areas:

1. **[Priority Area 1]** - *[Effort: S/M/L/XL] | Impact: High/Medium/Low*
   - Rationale: [Why this is priority]
   - Quick wins: [Any immediate improvements possible]

2. **[Priority Area 2]** - *[Effort: S/M/L/XL] | Impact: High/Medium/Low*
   *(same structure)*

3. **[Priority Area 3]** - *[Effort: S/M/L/XL] | Impact: High/Medium/Low*
   *(same structure)*

---

## Effort Estimates

| Task Category | Effort (T-shirt) | Justification |
|---------------|------------------|---------------|
| [Task 1] | S / M / L / XL | [Why this estimate] |
| [Task 2] | S / M / L / XL | [Why this estimate] |

**Effort Scale**:
- **S (Small)**: 1-2 days, straightforward, well-understood
- **M (Medium)**: 3-5 days, some complexity or unknowns
- **L (Large)**: 1-2 weeks, significant complexity or research needed
- **XL (Extra Large)**: 2+ weeks, major undertaking with dependencies

---

## Next Steps

### Immediate Actions (This Round)
- [ ] [Action 1]
- [ ] [Action 2]

### Follow-up for Next Round
- [ ] [What needs deeper analysis]
- [ ] [Additional research needed]
- [ ] [Questions to answer]

### Information Gaps
- [What information is still missing]
- [Where to find it]
- [Why it matters]

---

## References & Sources

**All detailed references are in [REFERENCES.md](REFERENCES.md)**

**Key sources used in this analysis**:
1. [Source 1 name] - [Brief description]
2. [Source 2 name] - [Brief description]
3. [Source 3 name] - [Brief description]

---

## Appendix (Optional)

### Code Snippets
*(Only include if critical for understanding - prefer references otherwise)*

```python
# Example pattern from reference platform
# Source: [link in REFERENCES.md]
def example_pattern():
    pass
```

### Diagrams
*(If helpful for architecture/flow understanding)*

---

**Document Status**:
- ✅ Research complete
- ✅ Findings documented
- ✅ References added to REFERENCES.md
- ✅ INDEX.md updated
- ⬜ Peer reviewed
- ⬜ Incorporated into roadmap
