# Round 3: Implementation Roadmap - Platform Linux ARM Modernization

**Status**: ✅ READY - Rounds 1 & 2 complete
**Prerequisites**: Read all Round 1 & 2 documents
**Estimated Time**: 2-3 hours

---

## Objective

Synthesize findings from Rounds 1 & 2 into a **detailed, prioritized, phased implementation roadmap** that provides:
1. Clear phases with specific tasks and dependencies
2. Realistic effort estimates and timelines
3. Success criteria per phase
4. Quick-start action plan (first week tasks)
5. Risk assessment and mitigation strategies

**Scope**: Create actionable roadmap from research to production
**Approach**: Organize all identified tasks into logical, dependency-ordered phases
**Output**: `03-implementation-roadmap.md`

---

## Context from Rounds 1 & 2

### Round 1: Initial Assessment

**Top 5 Priorities Identified**:
1. Cross-compilation fixes (S effort, High impact) - Only macOS x86_64 works
2. Framework modernization (M effort, High impact) - WiringPi deprecated
3. CI/CD infrastructure (S-M effort, High impact) - Zero testing
4. Modern board support (S effort, Medium impact) - Missing Pi 4, 5
5. Platform architecture review (M effort, Medium impact) - Deferred

### Round 2: Deep-Dive Findings

**Priority 1: Cross-Compilation**
- **Critical Discovery**: PlatformIO packages unavailable for Linux x86_64/Windows
- **Solution**: System-installed toolchains (apt/brew/manual)
- **Phases**: Phase 1 (single arch, 4h) → Phase 2 (dual arch, 3.5h)
- **Total Effort**: 7.5 hours
- **Dependency**: None - can start immediately

**Priority 2: Frameworks**
- **Recommendations**: lgpio (modern, Pi 5), pigpio (Pi 4-), bare-metal, WiringPi (legacy)
- **Approach**: System dependencies (apt install), not PlatformIO packages
- **Builder Scripts**: 4 frameworks × 2-4 hours each = 8-16 hours
- **Total Effort**: 10-18 hours
- **Dependency**: Cross-compilation working helps testing

**Priority 3: Boards**
- **Missing**: Pi 4 (critical), Pi 5 (critical), 400, CM4, Zero 2 W
- **Approach**: Copy-paste JSON with SoC/frequency updates
- **Effort**: 30 min per board × 5 boards = 2.5 hours
- **Total Effort**: 3-4 hours (including testing)
- **Dependency**: Frameworks affect board compatibility

**Priority 4: CI/CD**
- **Phases**: Phase 1 (Ubuntu, 2h) → Phase 2 (full matrix, 3h) → Phase 3 (quality gates, 2h)
- **Total Effort**: 7 hours
- **Critical Dependency**: REQUIRES Priority 1 (cross-compilation) complete first

**Round 2 Total Estimated Effort**: 27.5-36.5 hours

---

## Input Documents

### Required Reading

1. **Round 1**: `01-initial-assessment.md`
   - Current state, blockers, priority rankings
   - Feature gaps vs reference platforms

2. **Round 2 - Priority Analyses** (read all four):
   - `02-priority-cross-compilation.md` - Toolchain solutions
   - `02-priority-frameworks.md` - GPIO library ecosystem
   - `02-priority-boards.md` - Hardware specifications
   - `02-priority-ci-cd.md` - Testing infrastructure

3. **References**: `REFERENCES.md`
   - All source materials and code references

---

## Roadmap Generation Tasks

### Task 1: Extract and Organize All Tasks (30-40 min)

**Compile master task list** from all Round 2 documents:

1. **Cross-Compilation Tasks**:
   - Phase 1: Single arch support (Linux x86_64, Windows, macOS ARM)
   - Phase 2: Dual arch support (armv7 + aarch64)
   - Documentation (installation guides per OS)
   - Testing

2. **Framework Tasks**:
   - Bare-metal/framework-less option
   - lgpio framework builder + examples
   - pigpio framework builder + examples
   - Update WiringPi to GC2 fork
   - libgpiod builder (optional/advanced)
   - Framework selection guide
   - Migration examples

3. **Board Tasks**:
   - Add Pi 4 Model B
   - Add Pi 5
   - Add Pi 400
   - Add CM4
   - Add Zero 2 W
   - Board selection documentation
   - Testing

4. **CI/CD Tasks**:
   - Phase 1: Basic workflow (Ubuntu, 2 examples)
   - Phase 2: Full matrix (3 OS, all examples)
   - Phase 3: Quality gates (pre-commit, release automation)
   - Documentation (contributor guide)

5. **Documentation Tasks**:
   - README updates (cross-compilation setup)
   - Framework comparison guide
   - Board selection guide
   - Troubleshooting guide
   - Migration guide (WiringPi → lgpio/pigpio)

**Output**: Complete task inventory with effort estimates from Round 2

---

### Task 2: Map Dependencies (20-30 min)

**Create dependency graph**:

1. **Critical Path Identification**:
   - What tasks MUST happen before others?
   - Example: Cross-compilation (P1) must complete before CI/CD (P4) Phase 1

2. **Parallel Work Opportunities**:
   - Which tasks can run concurrently?
   - Example: Board definitions (P3) independent of frameworks (P2)

3. **Blocking Relationships**:
   - Cross-compilation → CI/CD (hard dependency)
   - Frameworks → Advanced CI/CD testing (soft dependency)
   - Boards → Framework compatibility testing (soft dependency)

**Output**: Dependency diagram (text or structured list)

---

### Task 3: Define Implementation Phases (40-50 min)

**Organize tasks into logical phases**:

#### Phase 0: Foundation & Quick Wins
**Goal**: Get basic cross-compilation working, unblock majority of users
**Duration**: 1-2 weeks
**Tasks**:
- Cross-compilation Phase 1 (single arch)
- Raspberry Pi 4 board definition
- Bare-metal framework option
- Basic documentation updates

**Success Criteria**:
- Ubuntu x86_64 users can cross-compile
- Windows users can cross-compile
- macOS ARM users can cross-compile
- Pi 4 board selectable
- Non-GPIO apps buildable

#### Phase 1: Core Modernization
**Goal**: Add modern frameworks and boards, establish testing
**Duration**: 2-3 weeks
**Tasks**:
- lgpio framework (Pi 5 compatible)
- pigpio framework (Pi 4 compatible)
- Pi 5 board definition
- CI/CD Phase 1 (basic Ubuntu testing)
- Framework selection guide

**Success Criteria**:
- Pi 5 supported with lgpio
- Pi 4 has pigpio option
- Automated CI testing running
- Framework migration path documented

#### Phase 2: Complete Coverage
**Goal**: Full board support, comprehensive frameworks, full CI matrix
**Duration**: 1-2 weeks
**Tasks**:
- Pi 400, CM4, Zero 2 W boards
- WiringPi GC2 fork update
- Cross-compilation Phase 2 (dual arch)
- CI/CD Phase 2 (full OS matrix)
- Complete documentation

**Success Criteria**:
- All modern Pi boards supported
- Both 32-bit and 64-bit targets
- CI tests all OS × examples
- Complete user documentation

#### Phase 3: Quality & Polish
**Goal**: Production-ready platform, maintainable, contributor-friendly
**Duration**: 1 week
**Tasks**:
- CI/CD Phase 3 (quality gates)
- Pre-commit hooks
- Release automation
- Contributing guide
- Advanced examples

**Success Criteria**:
- All PRs automatically tested
- Release process automated
- Contributors have clear guidance
- Example library diverse

**Total Timeline**: 5-8 weeks (calendar time, assuming part-time work)

---

### Task 4: Effort and Timeline Estimation (20-30 min)

**Per-Phase Breakdown**:

| Phase | Tasks | Total Effort (hours) | Parallel Potential | Calendar Time |
|-------|-------|---------------------|-------------------|---------------|
| Phase 0 | 4-5 | 6-8 hours | Low (sequential) | 1-2 weeks |
| Phase 1 | 5-6 | 10-14 hours | Medium | 2-3 weeks |
| Phase 2 | 6-8 | 8-12 hours | High | 1-2 weeks |
| Phase 3 | 4-5 | 5-7 hours | Medium | 1 week |
| **Total** | **20-24** | **29-41 hours** | - | **5-8 weeks** |

**Assumptions**:
- 5-10 hours/week availability (part-time)
- Some tasks parallelizable (board definitions while waiting for CI)
- Unknowns add 20-30% buffer (already included)

**Scenarios**:
- **Optimistic** (10 hrs/week, no blockers): 4-5 weeks
- **Realistic** (7 hrs/week, expected delays): 5-8 weeks
- **Pessimistic** (5 hrs/week, major blockers): 8-12 weeks

---

### Task 5: Risk Assessment and Mitigation (15-20 min)

**Identify risks per phase**:

| Risk | Probability | Impact | Phase | Mitigation Strategy |
|------|-------------|--------|-------|---------------------|
| System toolchains hard to install (Windows) | Medium | Medium | Phase 0 | Detailed guides, Docker alternative |
| Framework cross-compile libs unavailable | Medium | High | Phase 1 | Build from source instructions, sysroot approach |
| Pi 5 hardware unavailable for testing | Medium | Low | Phase 1 | Community testing, emulation |
| CI/CD breaks on one OS | Medium | Low | Phase 1-2 | fail-fast: false, per-OS debugging |
| WiringPi GC2 fork abandoned | Low | Low | Phase 2 | Already have alternatives (lgpio, pigpio) |
| Dual-arch complexity exceeds estimates | Medium | Medium | Phase 2 | Can defer to later if needed |

---

### Task 6: Quick-Start Action Plan (15-20 min)

**Create concrete first steps**:

#### Week 1: Cross-Compilation Foundation
**Day 1-2**: Implement cross-compilation Phase 1
- [ ] Update builder/main.py with OS detection
- [ ] Test on Linux x86_64 (install gcc-arm-linux-gnueabihf)
- [ ] Test on macOS ARM (install via brew)
- [ ] Document toolchain installation per OS

**Day 3-4**: Quick wins
- [ ] Add Raspberry Pi 4 board definition
- [ ] Add bare-metal framework option
- [ ] Create basic README section on cross-compilation

**Day 5**: Testing & Documentation
- [ ] Build wiringpi-blink on all platforms
- [ ] Verify binaries are ARM architecture
- [ ] Update platformio.json description

**Week 1 Success**: Linux/macOS/Windows users can cross-compile, Pi 4 selectable

#### Week 2: Framework Modernization Begins
**Day 1-2**: lgpio framework
- [ ] Create builder/frameworks/lgpio.py
- [ ] Create examples/lgpio-blink
- [ ] Test on Ubuntu x86_64 cross-compile
- [ ] Document lgpio installation

**Day 3**: Pi 5 support
- [ ] Add raspberrypi_5 board definition
- [ ] Test lgpio-blink for Pi 5 target
- [ ] Document Pi 5 specifics (RP1 controller, lgpio requirement)

**Day 4-5**: CI/CD Foundation
- [ ] Create .github/workflows/examples.yml (Phase 1)
- [ ] Test Ubuntu workflow with 2 examples
- [ ] Fix any CI issues

**Week 2 Success**: lgpio framework working, Pi 5 supported, CI running

#### Month 1 Milestones:
- [ ] Phase 0 complete (cross-compilation, quick wins)
- [ ] Phase 1 50% complete (lgpio done, pigpio in progress)
- [ ] CI/CD Phase 1 running

---

## Deliverable Document Structure

Create `03-implementation-roadmap.md` with:

### 1. Executive Summary (1-2 pages)
- Project goals and current state recap
- High-level phase overview (0-3)
- Critical path and timeline
- Resource requirements

### 2. Phase Definitions

**For each phase (0-3)**:

#### Phase X: [Name]
**Goal**: [Clear statement]
**Duration**: [X weeks]
**Total Effort**: [Y hours]

**Tasks**:
1. **[Task Name]** - *Effort: [S/M/L] | Owner: TBD | Dependencies: [list]*
   - Description: [What needs to be done]
   - Success criteria: [How to know it's done]
   - References: [Links to Round 2 analysis]
   - Implementation notes: [Key technical points]

2. **[Task Name]** - *(same structure)*

**Phase Dependencies**:
- Requires: [Previous phase tasks]
- Enables: [Future phase tasks]

**Phase Success Criteria**:
- ✅ [Criteria 1]
- ✅ [Criteria 2]
- ✅ [Criteria 3]

**Risks for This Phase**:
- [Risk]: [Mitigation]

---

### 3. Dependency Visualization

**Critical Path** (longest dependency chain):
```
Phase 0: Cross-Compilation (1-2 weeks)
    ↓
Phase 1: lgpio + CI/CD Phase 1 (2-3 weeks)
    ↓
Phase 2: Full Coverage (1-2 weeks)
    ↓
Phase 3: Polish (1 week)
```

**Parallel Workstreams**:
```
Stream A: Cross-Compilation → CI/CD → Quality Gates
Stream B: Frameworks (lgpio, pigpio, bare-metal) → Examples
Stream C: Boards (independent, can be done anytime after cross-compile)
Stream D: Documentation (ongoing throughout)
```

---

### 4. Effort Summary Table

| Phase | Tasks | Dev Hours | Test Hours | Doc Hours | Total |
|-------|-------|-----------|-----------|-----------|-------|
| Phase 0 | 5 | 4 | 2 | 1 | 7 |
| Phase 1 | 6 | 8 | 3 | 3 | 14 |
| Phase 2 | 7 | 6 | 3 | 3 | 12 |
| Phase 3 | 5 | 3 | 2 | 2 | 7 |
| **Total** | **23** | **21** | **10** | **9** | **40** |

---

### 5. Risk Matrix

| Risk | Probability | Impact | Phase | Mitigation | Status |
|------|-------------|--------|-------|------------|--------|
| [Risk 1] | H/M/L | H/M/L | X | [Strategy] | 🔴/🟡/🟢 |

**Risk Legend**:
- 🔴 High risk, needs immediate mitigation
- 🟡 Medium risk, monitor
- 🟢 Low risk or mitigated

---

### 6. Quick-Start Action Plan

#### First Day:
1. [ ] [Specific task with clear acceptance criteria]
2. [ ] [Specific task with clear acceptance criteria]

#### First Week:
- [ ] [Milestone 1]
- [ ] [Milestone 2]
- [ ] [Milestone 3]

#### First Month:
- [ ] [Phase 0 complete]
- [ ] [Phase 1 50% complete]

---

### 7. Resource Requirements

**Development Environment**:
- Linux x86_64 machine (Ubuntu/Debian preferred)
- Optional: Windows machine for testing
- Optional: macOS ARM (Apple Silicon) for testing
- Optional: Raspberry Pi 4 or 5 for hardware validation

**Tools**:
- Python 3.11+ (for PlatformIO)
- ARM cross-toolchains (gcc-arm-linux-gnueabihf, gcc-aarch64-linux-gnu)
- Git, text editor/IDE
- GitHub account (for CI/CD)

**Knowledge/Skills**:
- Python (basic - for builder scripts)
- SCons (basic - pattern matching)
- GitHub Actions (basic - YAML editing)
- C/C++ (for examples)
- GPIO libraries (learnable from docs)

**Time Commitment**:
- Minimum: 5 hours/week (8-12 weeks timeline)
- Recommended: 7-10 hours/week (5-8 weeks timeline)
- Optimal: 15+ hours/week (4-5 weeks timeline)

---

### 8. Success Metrics

**Phase 0 Success Metrics**:
- [ ] Cross-compilation works on 3 platforms (Linux, macOS, Windows)
- [ ] At least 2 users successfully build examples
- [ ] Pi 4 board selectable and builds successfully

**Phase 1 Success Metrics**:
- [ ] lgpio framework works, tested on Pi 5 target
- [ ] CI/CD runs on every commit/PR
- [ ] Documentation covers installation on all platforms

**Phase 2 Success Metrics**:
- [ ] All modern Pi boards (4, 5, 400, CM4, Zero 2 W) defined
- [ ] CI tests pass on 3 OS with multiple examples
- [ ] 64-bit ARM targets build correctly

**Phase 3 Success Metrics**:
- [ ] Zero failed CI builds on main branch (quality gates working)
- [ ] Contributors can submit PRs with clear process
- [ ] Platform ready for upstream contribution to platformio org

---

### 9. Post-Implementation

**Ongoing Maintenance**:
- Monitor Raspberry Pi hardware releases (new boards)
- Update framework packages as new versions release
- Address community issues and PRs
- Maintain CI/CD as PlatformIO Core evolves

**Future Enhancements** (beyond this roadmap):
- Non-Raspberry Pi ARM boards (BeagleBone, ODROID)
- libgpiod v2 support (when available in Pi OS)
- Remote debugging infrastructure
- Upload protocols (SCP, rsync)
- Hardware-in-the-loop testing

**Community Engagement**:
- Announce modernization in PlatformIO community
- Seek testers for various platforms
- Invite contributions for non-Pi boards
- Consider upstreaming to official platformio org

---

## Success Criteria for Round 3

Round 3 is successful if the roadmap provides:

- ✅ **Clear phases** with specific, actionable tasks
- ✅ **Realistic timeline** with justification
- ✅ **Dependencies mapped** and critical path identified
- ✅ **Effort estimates** per task and phase
- ✅ **Success criteria** to know when each phase is done
- ✅ **Risk assessment** with mitigation strategies
- ✅ **Quick-start guide** - can begin implementation immediately
- ✅ **Resource requirements** clearly stated
- ✅ **All Round 2 tasks** incorporated

---

## Output Checklist

When Round 3 is complete, you should have:

- [ ] `03-implementation-roadmap.md` created (following structure above)
- [ ] All tasks from Round 2 organized into phases
- [ ] Dependencies clearly mapped
- [ ] Timeline and effort estimates per phase
- [ ] Quick-start action plan (first day/week/month tasks)
- [ ] Risk matrix with mitigation strategies
- [ ] Success metrics defined
- [ ] 00-INDEX.md updated (Round 3 marked complete)
- [ ] Ready to begin implementation

---

## Workflow Tips

### Don't Overcomplicate
- Phases should be simple and clear
- Tasks should be specific and actionable
- Avoid creating too many dependencies (simplify where possible)
- Focus on critical path (what MUST happen in order)

### Be Realistic
- Use Round 2 effort estimates (already refined)
- Add buffer for unknowns (20-30%)
- Account for part-time work (5-10 hrs/week is realistic)
- Don't over-optimize parallelization (coordination overhead)

### Make it Actionable
- Each task should have clear acceptance criteria
- Success criteria should be measurable
- Quick-start plan should be copy-pasteable
- Developers should be able to start Day 1

---

## Getting Started

To execute Round 3:

1. **Start fresh Claude Code session** in repository root
2. **Read all prerequisite documents**:
   - `research/01-initial-assessment.md`
   - `research/02-priority-cross-compilation.md`
   - `research/02-priority-frameworks.md`
   - `research/02-priority-boards.md`
   - `research/02-priority-ci-cd.md`
   - `research/REFERENCES.md`
3. **Execute roadmap generation** following this prompt
4. **Create `research/03-implementation-roadmap.md`**
5. **Update tracking files** (00-INDEX.md)

**Estimated time**: 2-3 hours
**Output**: Production-ready implementation roadmap

**Next step after Round 3**: Begin implementation following the roadmap!
