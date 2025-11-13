# Manual Steps: Documentation Reorganization Follow-up

**Date**: 2025-11-13
**Purpose**: Document manual actions required to complete the documentation reorganization for PlatformIO platform submission

This file lists all manual steps that need to be completed after the automated reorganization. These steps require tools, permissions, or network access not available in the automated environment.

---

## Table of Contents

1. [Completed by Automation](#completed-by-automation)
2. [Required Manual Steps](#required-manual-steps)
3. [Optional Manual Steps](#optional-manual-steps)
4. [Validation Checklist](#validation-checklist)

---

## Completed by Automation

The following reorganization was completed automatically and committed to git:

✅ **Directory Reorganization:**
- Moved `issues/` → `.github/ISSUE_ASSESSMENTS/`
- Moved `research/` → `.archive/research/`
- Moved reference docs → `.archive/references/`
- Created `.archive/README.md` explaining archive contents
- Created `.github/ISSUE_ASSESSMENTS/README.md` explaining issue workflow

✅ **Documentation Cleanup:**
- Removed reference platform docs from `docs/` (espressif8266, ststm32, raspberrypi)
- Moved internal planning docs to `.archive/`
- Kept user-facing guides in `docs/` (UPLOAD.md, DEBUGGING.md, etc.)
- Preserved Sphinx build files (conf.py, index.rst, platforms/)

✅ **README Simplification:**
- Streamlined main README.md from 514 to 288 lines
- Improved organization with clear sections
- Added better navigation to detailed docs
- Preserved original as `.archive/README-ORIGINAL.md`

---

## Required Manual Steps

### Step 1: Push Git Tag for Current State

**Why**: Create a snapshot before further changes, enabling easy rollback if needed.

**Commands**:
```bash
# Create annotated tag
git tag -a v1.7.0-before-wiki -m "Snapshot before moving research to wiki - all content preserved in .archive/"

# Push tag to remote
git push origin v1.7.0-before-wiki

# Or push all tags
git push --tags
```

**Validation**: Verify tag exists on GitHub under "Releases"

---

### Step 2: Create GitHub Wiki from Research Content

**Why**: Make research artifacts discoverable without cluttering main repository. Follows PlatformIO platform standards.

**Option A: Manual Wiki Creation (Recommended)**

1. **Enable Wiki** on GitHub repository:
   - Go to repository Settings → Features
   - Check "Wikis"

2. **Create Wiki Pages** from research files:

   Navigate to Wiki tab and create these pages:

   | Wiki Page Title | Source File | Description |
   |----------------|-------------|-------------|
   | Home | Create new | Wiki home with overview and navigation |
   | Modernization Overview | `.archive/research/00-INDEX.md` | Master progress tracker |
   | Round 1: Initial Assessment | `.archive/research/01-initial-assessment.md` | High-level comparison |
   | Round 2: Boards Analysis | `.archive/research/02-priority-boards.md` | Board support deep-dive |
   | Round 2: CI/CD Analysis | `.archive/research/02-priority-ci-cd.md` | CI/CD modernization |
   | Round 2: Cross-Compilation | `.archive/research/02-priority-cross-compilation.md` | Cross-compilation analysis |
   | Round 2: Frameworks | `.archive/research/02-priority-frameworks.md` | GPIO frameworks analysis |
   | Round 3: Roadmap | `.archive/research/03-implementation-roadmap.md` | Implementation plan |
   | Fork Analysis | `.archive/research/FORK-ANALYSIS-SUMMARY.md` | Fork comparison summary |
   | Implementation Status | `.archive/research/IMPLEMENTATION_STATUS.md` | Current status |
   | References | `.archive/research/REFERENCES.md` | Source references |

3. **Create Wiki Home Page**:
   ```markdown
   # Platform-linux_arm Modernization Documentation

   This wiki documents the modernization effort for the platform-linux_arm PlatformIO platform.

   ## Navigation

   ### Research Rounds
   - [[Modernization Overview]] - Progress tracker and master index
   - [[Round 1: Initial Assessment]] - High-level platform comparison
   - [[Round 2: Boards Analysis]] - Board support deep-dive
   - [[Round 2: CI/CD Analysis]] - CI/CD modernization
   - [[Round 2: Cross-Compilation]] - Cross-compilation analysis
   - [[Round 2: Frameworks]] - GPIO frameworks analysis
   - [[Round 3: Roadmap]] - Implementation plan

   ### Status & References
   - [[Implementation Status]] - Current modernization status
   - [[Fork Analysis]] - Comparison with original platform
   - [[References]] - Source materials and links

   ## About This Research

   When this platform was forked from the official platformio/platform-linux_arm
   (last updated May 2022), comprehensive research was conducted to modernize it
   to match the quality and features of reference platforms (espressif32, ststm32).

   This documentation provides transparency into the decision-making process and
   serves as a guide for similar modernization efforts.
   ```

4. **Optional: Add Images**
   - Upload any diagrams or screenshots if available
   - Link from wiki pages

**Option B: Automated Wiki Creation (Advanced)**

If you prefer automation:

```bash
# Clone wiki repository (GitHub wikis are git repos)
git clone https://github.com/sfo2001/platform-linux_arm.wiki.git

# Copy research files
cd platform-linux_arm.wiki
cp ../.archive/research/*.md .

# Rename files to wiki-friendly names (replace spaces with dashes)
# Create Home.md with navigation
# Commit and push
git add *.md
git commit -m "docs: add modernization research documentation"
git push origin master
```

**Validation**: Visit `https://github.com/sfo2001/platform-linux_arm/wiki` and verify pages are accessible.

---

### Step 3: Update CLAUDE.md to Reference New Locations

**Why**: Ensure Claude Code (or future contributors) knows where to find research materials.

**File**: `/CLAUDE.md`

**Changes**:
Update the "Modernization Research Workflow" section to reference the wiki:

```markdown
## Modernization Research Workflow

This repository underwent a structured research and analysis workflow to guide modernization.
The complete research artifacts are available in the GitHub Wiki:

**Wiki**: https://github.com/sfo2001/platform-linux_arm/wiki

For offline access, research artifacts are preserved in `.archive/research/` directory.

### Quick Links
- [Modernization Overview](wiki link) - Progress tracker
- [Implementation Roadmap](wiki link) - Phase-by-phase plan
- [Implementation Status](wiki link) - Current status
```

---

### Step 4: Decide Final Disposition of .archive/

**Why**: Choose whether to keep, remove, or ignore the archive directory based on your goals.

**Options**:

**Option A: Keep .archive/ in Repository (Current State)**
- ✅ Fully version-controlled
- ✅ Accessible offline
- ✅ No extra setup needed
- ❌ Adds ~500KB to repository
- **Action**: None required, already committed

**Option B: Remove .archive/ After Wiki Creation**
- ✅ Clean repository matching PlatformIO standards
- ✅ Smaller repo size
- ❌ Loses git history of research files
- ❌ Requires wiki for access
- **Action**:
  ```bash
  # After wiki is created and verified
  git rm -r .archive/
  git commit -m "docs: move research to wiki, remove .archive/"
  git push
  ```

**Option C: Add .archive/ to .gitignore (Keep Locally)**
- ⚠️ **DON'T DO THIS** - Will lose files in sandbox environment
- Only viable if you have a persistent local copy
- **Action**: Not recommended for this workflow

**Recommendation**: Choose Option A (keep) until wiki is fully set up and verified, then consider Option B.

---

### Step 5: Update Repository Description and Topics

**Why**: Improve discoverability on GitHub and PlatformIO Registry.

**GitHub Repository Settings**:

1. **Description**: Update to match README
   ```
   PlatformIO platform for ARM-based Linux systems (Raspberry Pi, Orange Pi). Supports cross-compilation, remote debugging, and modern GPIO frameworks (lgpio, pigpio, WiringPi). Modernized fork with Pi 5 support.
   ```

2. **Topics**: Add relevant tags
   ```
   platformio
   raspberry-pi
   arm-linux
   embedded
   gpio
   cross-compilation
   lgpio
   raspberry-pi-5
   embedded-linux
   iot
   ```

3. **Website**: Add documentation link
   ```
   https://docs.platformio.org/page/platforms/linux_arm.html
   ```
   (Or your fork's documentation URL)

**Where**: GitHub repository → About section (click gear icon)

---

### Step 6: Verify All Documentation Links

**Why**: Ensure no broken links after reorganization.

**Actions**:

1. **Check README.md links**:
   ```bash
   # Install markdown link checker (optional)
   npm install -g markdown-link-check

   # Check for broken links
   markdown-link-check README.md
   ```

2. **Manually verify key links**:
   - [ ] CHANGELOG.md exists and is linked correctly
   - [ ] CONTRIBUTING.md exists and is linked correctly
   - [ ] All docs/ links point to correct files
   - [ ] Examples directory references are accurate

3. **Test external links**:
   - [ ] PlatformIO Registry link
   - [ ] ARM Developer toolchain downloads
   - [ ] lgpio/pigpio/WiringPi project links

**Fix**: Update any broken links in README.md or documentation files.

---

### Step 7: Create GitHub Release for v1.7.0

**Why**: Make the current stable version easily accessible for users.

**Actions**:

1. **Tag the release** (if not already done):
   ```bash
   git tag -a v1.7.0 -m "Release 1.7.0: The Modernization Release"
   git push origin v1.7.0
   ```

2. **Create GitHub Release**:
   - Go to repository → Releases → "Draft a new release"
   - Choose tag: `v1.7.0`
   - Release title: `v1.7.0 - The Modernization Release`
   - Description: Copy from CHANGELOG.md or create summary:

   ```markdown
   # Release 1.7.0: The Modernization Release

   Major modernization of platform-linux_arm with comprehensive improvements.

   ## Highlights
   - ✅ Raspberry Pi 5 support
   - ✅ Modern lgpio framework (Pi 5 compatible)
   - ✅ Cross-compilation from macOS (Intel + Apple Silicon), Linux, Windows
   - ✅ Remote debugging with GDB over SSH
   - ✅ Automated remote deployment and testing
   - ✅ Comprehensive documentation and examples

   ## Breaking Changes
   - pigpio deprecated for Pi 5 (use lgpio instead)

   See [CHANGELOG.md](CHANGELOG.md) for complete details.
   ```

3. **Publish Release**

**Validation**: Verify release appears on GitHub and can be installed via:
```bash
pio pkg install --global --platform https://github.com/sfo2001/platform-linux_arm.git#v1.7.0
```

---

### Step 8: Test Installation from Various Sources

**Why**: Ensure platform installs correctly for end users.

**Test Cases**:

1. **Install from GitHub (development version)**:
   ```bash
   pio pkg install --global --platform https://github.com/sfo2001/platform-linux_arm.git
   ```

2. **Install from GitHub tag**:
   ```bash
   pio pkg install --global --platform https://github.com/sfo2001/platform-linux_arm.git#v1.7.0
   ```

3. **Install from local directory**:
   ```bash
   pio pkg install --global --platform file://.
   ```

4. **Verify installation**:
   ```bash
   pio platform list
   # Should show linux_arm @ 1.7.0
   ```

5. **Build example project**:
   ```bash
   cd examples/lgpio-blink
   pio run
   # Should compile successfully
   ```

**Fix**: Address any installation or build errors.

---

## Optional Manual Steps

### Optional 1: Submit Platform to PlatformIO Registry

**When**: After all required steps are complete and thoroughly tested.

**Prerequisites**:
- [ ] All required manual steps completed
- [ ] Platform thoroughly tested on real hardware
- [ ] Documentation complete and accurate
- [ ] Examples working and well-documented
- [ ] No critical bugs or issues

**Process**:

1. **Review submission requirements**:
   - Read: https://docs.platformio.org/en/latest/platforms/creating_platform.html#publishing

2. **Verify platform.json**:
   ```bash
   # Check all required fields present
   cat platform.json | grep -E "(name|title|description|version|repository)"
   ```

3. **Test package publishing (dry-run)**:
   ```bash
   # From platform root
   pio pkg publish --dry-run
   ```

4. **Publish to registry**:
   ```bash
   pio pkg publish
   ```

5. **Decision point**: Publish to personal namespace or contribute to official `platformio/` namespace?

   **Personal namespace** (faster):
   - Publish as `sfo2001/platform-linux_arm`
   - Full control, immediate availability
   - Users install via: `platform = sfo2001/platform-linux_arm`

   **Official namespace** (requires approval):
   - Submit PR to PlatformIO organization
   - Requires CLA signature
   - Longer review process
   - Better visibility and trust
   - Users install via: `platform = linux_arm`

**Resources**:
- PlatformIO Publishing Guide: https://docs.platformio.org/en/latest/core/userguide/pkg/cmd_publish.html
- CLA: https://docs.platformio.org/en/latest/legal/index.html#contributor-license-agreement

---

### Optional 2: Create Additional Documentation

**When**: After core documentation is complete, if you want to expand.

**Ideas**:

1. **Tutorial: "Getting Started with Raspberry Pi GPIO"**
   - Step-by-step guide for beginners
   - From setup to first blink program
   - Troubleshooting common issues

2. **Tutorial: "Migrating from WiringPi to lgpio"**
   - API comparison table
   - Migration examples
   - Common pitfalls

3. **Individual Board Documentation Pages**
   - Detailed specs for each board
   - GPIO pinout diagrams
   - Board-specific considerations

4. **Hardware Testing Guide**
   - How to test GPIO, I2C, SPI on each board
   - Required hardware (LEDs, sensors, etc.)
   - Expected results

**Location**: `docs/tutorials/` or wiki pages

---

### Optional 3: Set Up CI/CD for Documentation

**When**: If you want automated documentation building/publishing.

**Options**:

1. **Sphinx Documentation Build**:
   - Add GitHub Action to build Sphinx docs on push
   - Publish to GitHub Pages
   - Example workflow:
   ```yaml
   name: Build Docs
   on: [push]
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Build Sphinx docs
           run: |
             pip install sphinx
             cd docs && make html
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html
   ```

2. **Link Checking**:
   - Automated link validation on PRs
   - Catch broken links before merge

3. **Markdown Linting**:
   - Ensure consistent documentation style
   - Enforce markdown best practices

---

### Optional 4: Create Video Tutorials or Demos

**When**: If you want to improve accessibility for visual learners.

**Ideas**:
- Platform installation and setup walkthrough
- Remote debugging demo in VS Code
- GPIO programming tutorial (LED blink to sensor reading)
- Cross-compilation setup on different OSes

**Hosting**: YouTube, Vimeo, or embed in GitHub wiki

---

### Optional 5: Community Engagement

**When**: After platform is stable and well-documented.

**Actions**:
1. **Announce on forums**:
   - PlatformIO Community Forums
   - Raspberry Pi Forums
   - Reddit (r/raspberry_pi, r/PlatformIO)

2. **Blog post**:
   - Write about modernization journey
   - Technical decisions and lessons learned
   - Link to research wiki

3. **Social media**:
   - Tweet about release
   - Tag @PlatformIO_Org

---

## Validation Checklist

Before considering the reorganization complete, verify:

### Repository Structure
- [ ] `.github/ISSUE_ASSESSMENTS/` exists with all issue assessments
- [ ] `.archive/research/` contains all research files
- [ ] `.archive/references/` contains reference platform docs
- [ ] `docs/` contains only user-facing documentation
- [ ] `README.md` is streamlined and well-organized
- [ ] All changes committed to git

### Documentation Quality
- [ ] All links in README.md work
- [ ] All docs/ links point to existing files
- [ ] Examples directory matches README descriptions
- [ ] CONTRIBUTING.md is clear and actionable
- [ ] CHANGELOG.md is up to date

### Git & Releases
- [ ] Git tag created for pre-reorganization state
- [ ] All changes committed with clear messages
- [ ] Git history is clean (no accidental commits)
- [ ] Changes pushed to remote repository
- [ ] GitHub release created for v1.7.0

### External Resources
- [ ] GitHub Wiki created (optional but recommended)
- [ ] Research content accessible via wiki
- [ ] Repository description updated
- [ ] Topics/tags added to repository
- [ ] Links to external docs verified

### Testing
- [ ] Platform installs from GitHub
- [ ] Example projects build successfully
- [ ] Documentation builds with Sphinx (if applicable)
- [ ] No broken links in documentation

---

## Quick Summary: What You Need to Do

**Minimum (Required)**:
1. ✅ Review and commit the automated changes
2. ✅ Push git tags for version snapshots
3. ✅ Verify documentation links work
4. ✅ Test platform installation

**Recommended**:
5. ✅ Create GitHub Wiki from research content
6. ✅ Update CLAUDE.md to reference new locations
7. ✅ Create GitHub release for v1.7.0
8. ✅ Update repository description and topics

**Optional** (do later):
9. ⚪ Submit to PlatformIO Registry
10. ⚪ Create additional tutorials
11. ⚪ Set up documentation CI/CD
12. ⚪ Community engagement

---

## Support

If you encounter issues:

1. **Check `.archive/README.md`** - Explains what's in the archive
2. **Check `.github/ISSUE_ASSESSMENTS/README.md`** - Explains issue workflow
3. **Compare with git history** - See what changed
4. **Reference original README** - Available as `.archive/README-ORIGINAL.md`

---

## Notes

- All file moves preserve git history (using `git mv` or `git add -A`)
- Nothing was deleted - everything is either in its new location or in `.archive/`
- The `.archive/` directory is committed to git - it's not ignored
- You can always restore the original state using the git tag

---

**Created**: 2025-11-13
**Last Updated**: 2025-11-13
**Related Files**: `.archive/README.md`, `.github/ISSUE_ASSESSMENTS/README.md`
