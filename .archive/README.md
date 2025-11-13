# Archive Directory

This directory contains internal project artifacts that are not intended for end users but are valuable for project history and transparency.

## Contents

### `research/`
**Modernization research and planning artifacts**

Contains the comprehensive research and planning documentation created during the platform modernization effort:

- `00-INDEX.md` - Master progress tracker for all research rounds
- `01-ROUND-1-PROMPT.md` - Initial assessment prompt
- `01-initial-assessment.md` - Initial platform analysis findings
- `02-ROUND-2-PROMPT.md` - Deep-dive analysis prompts
- `02-priority-*.md` - Detailed analysis of priority areas (boards, CI/CD, cross-compilation, frameworks)
- `03-ROUND-3-PROMPT.md` - Implementation roadmap prompt
- `03-implementation-roadmap.md` - Comprehensive implementation plan
- `FORK-*.md` - Fork analysis, issue mapping, and roadmap cross-reference
- `IMPLEMENTATION_STATUS.md` - Current implementation status tracking
- `REFERENCES.md` - Centralized repository of sources and references
- Additional analysis and planning documents

**Value**: Documents the thought process and decision-making behind platform modernization. Useful for understanding why certain architectural choices were made.

**Recommended Action**: Move to GitHub Wiki for better discoverability. See `MANUAL_STEPS.md` in repository root.

---

### `references/`
**Reference documentation from other PlatformIO platforms**

Contains documentation snapshots from reference PlatformIO platforms used during research:

- `espressif8266.md/html` - Espressif8266 platform documentation
- `ststm32.md/html` - STM32 platform documentation
- `raspberrypi.md/html` - Raspberry Pi RP2040 platform documentation
- `creating_platform.md/html` - PlatformIO platform creation guide

**Value**: Research materials showing best practices and structure from established platforms. Helped inform the modernization effort.

**Recommended Action**: Can be deleted after modernization is complete, or kept for historical reference. Original sources are available at docs.platformio.org.

---

### Root Files

- `DOCUMENTATION_PLAN.md` - Internal planning document for documentation reorganization
- `HARDWARE_TESTING.md` - Internal testing methodology and hardware validation notes

---

## Why This Directory Exists

During the transition from "modernized fork with comprehensive internal docs" to "clean PlatformIO-standard platform," we needed to:

1. **Preserve valuable research** - The research directory contains months of analysis that shouldn't be lost
2. **Match PlatformIO standards** - Reference platforms don't have research/issues directories in their repos
3. **Maintain transparency** - All project artifacts should remain accessible, just better organized

This `.archive/` directory is a **temporary holding area** committed to git. See `MANUAL_STEPS.md` for the recommended final disposition of this content.

---

## Next Steps

**Option 1: Move to GitHub Wiki (Recommended)**
- Create wiki pages from `research/*.md` files
- Provides better discoverability for interested contributors
- See `MANUAL_STEPS.md` section "Creating GitHub Wiki"

**Option 2: Keep in Repository**
- Leave `.archive/` committed in git
- Clearly labeled as internal/historical
- Takes up repo space but fully version-controlled

**Option 3: Delete After Wiki Creation**
- After moving to wiki, delete `.archive/` directory
- Add to `.gitignore` if you want local copy
- Cleanest repo, but loses git history tracking

---

## For Official PlatformIO Submission

If submitting this platform to the official PlatformIO registry:

- **Before submission**: Move `research/` to wiki or delete this directory
- **Rationale**: Reference platforms (espressif32, ststm32, raspberrypi) don't include internal planning docs

The research artifacts are extremely valuable for this fork's transparency and decision documentation, but should be organized separately from the production platform code.

---

**Created**: 2025-11-13
**Last Updated**: 2025-11-13
**See Also**: `MANUAL_STEPS.md` in repository root
