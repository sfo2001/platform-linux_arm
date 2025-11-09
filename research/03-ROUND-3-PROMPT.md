# Round 3: Implementation Roadmap - Platform Linux ARM Modernization

**Status**: 🔴 NOT READY - Complete Rounds 1 & 2 first

---

## Instructions

This prompt will be used after Rounds 1 and 2 are complete to synthesize findings into a detailed, actionable implementation roadmap.

**Do not start Round 3 until**:
1. Round 1 is complete (`01-initial-assessment.md` exists)
2. Round 2 is complete (all priority area analyses exist)
3. This prompt has been reviewed and customized if needed
4. 00-INDEX.md has been updated

---

## Objective

Synthesize all findings from Rounds 1 & 2 into a **detailed, prioritized, phased implementation roadmap** that:
- Defines clear phases with dependencies
- Provides effort estimates and timelines
- Includes success criteria per phase
- Identifies quick wins and critical path
- Creates actionable task list to start immediately

**Output**: `03-implementation-roadmap.md`

---

## Input Documents

### Required Reading Before Starting Round 3

1. **Round 1 Output**: `01-initial-assessment.md`
   - Overall state assessment
   - Critical blockers
   - Priority areas identified

2. **Round 2 Outputs**: `02-priority-*.md` files
   - Detailed analysis per priority area
   - Proposed solutions
   - Effort estimates
   - Dependencies

3. **References**: `REFERENCES.md`
   - All source materials
   - Code patterns
   - Documentation links

---

## Roadmap Generation Tasks

### Task 1: Synthesize Findings (20-30 min)

Review all Round 1 & 2 documents and extract:

1. **All Identified Tasks**: Compile complete list of tasks across all priorities
2. **Dependencies**: Map which tasks depend on others
3. **Effort Estimates**: Consolidate effort estimates from Round 2
4. **Critical Path**: Identify blocking tasks that unblock multiple others
5. **Quick Wins**: Find high-impact, low-effort tasks

**Output**: Master task list with dependencies mapped

---

### Task 2: Define Implementation Phases (30-40 min)

Organize tasks into logical phases:

**Phase Structure**:
- **Phase 0: Foundation** - Critical fixes to make platform functional
- **Phase 1: Core Functionality** - Essential features for basic use
- **Phase 2: Feature Parity** - Match reference platform capabilities
- **Phase 3: Excellence** - Testing, CI/CD, documentation
- **Phase 4: Polish** - Performance, edge cases, community prep

For each phase:
- Clear goal statement
- List of included tasks
- Dependencies on previous phases
- Success criteria
- Estimated timeline

**Output**: Phased roadmap structure

---

### Task 3: Prioritize Within Phases (20-30 min)

Within each phase, order tasks by:
1. **Dependencies**: What must happen first?
2. **Impact**: What unblocks the most value?
3. **Risk**: What has unknowns that need early investigation?
4. **Quick wins**: What builds momentum?

**Output**: Prioritized task order within each phase

---

### Task 4: Effort & Timeline Estimation (20-30 min)

For each phase:
1. Sum effort estimates for all tasks
2. Account for unknowns and buffer (add 20-30%)
3. Identify parallel vs sequential work
4. Estimate calendar time based on available resources

Create timeline:
- Optimistic scenario (full-time, no blockers)
- Realistic scenario (part-time, expected blockers)
- Pessimistic scenario (interruptions, discoveries)

**Output**: Timeline estimates per phase

---

### Task 5: Risk Assessment (15-20 min)

For each phase, identify:
1. **Technical Risks**: What could go wrong?
2. **Dependency Risks**: External factors (upstream changes, etc.)
3. **Knowledge Risks**: What unknowns exist?
4. **Mitigation Strategies**: How to reduce risks?

**Output**: Risk matrix and mitigation plan

---

### Task 6: Quick-Start Action Plan (15-20 min)

Create immediate action plan:

**First Day**:
- [ ] Task 1: [Specific, actionable]
- [ ] Task 2: [Specific, actionable]
- [ ] Task 3: [Specific, actionable]

**First Week**:
- [ ] Milestone 1: [What should be achieved]
- [ ] Milestone 2: [What should be achieved]

**First Month**:
- [ ] Phase 0 complete: [Success criteria]

**Output**: Concrete first steps to start immediately

---

## Deliverable Structure

Create `03-implementation-roadmap.md` with:

### Executive Summary
- Project overview and goals
- High-level timeline (phases with durations)
- Critical success factors
- Resource requirements

### Implementation Phases

#### Phase 0: Foundation (Estimated: X weeks)
**Goal**: [Clear statement]

**Tasks**:
1. [Task name] - *[Effort: S/M/L] | [Owner: TBD]*
   - Description: [What needs to be done]
   - Dependencies: [What must complete first]
   - Success criteria: [How to know it's done]
   - References: [Links to relevant analysis]

2. [Task name] - *(same structure)*

**Phase Success Criteria**:
- ✅ [Criteria 1]
- ✅ [Criteria 2]

**Estimated Timeline**: [X weeks]

---

*(Repeat for each phase)*

---

### Dependency Graph

Visual representation of task dependencies (text-based):

```
Phase 0              Phase 1              Phase 2
┌─────────┐         ┌─────────┐         ┌─────────┐
│ Task A  │────────>│ Task D  │────────>│ Task G  │
└─────────┘         └─────────┘         └─────────┘
     │                    │
     v                    v
┌─────────┐         ┌─────────┐
│ Task B  │────────>│ Task E  │
└─────────┘         └─────────┘
     │
     v
┌─────────┐
│ Task C  │────────>│ Task F  │
└─────────┘         └─────────┘
```

### Critical Path

Identify the longest dependency chain:
1. [Task] → [Task] → [Task] = X weeks (critical path)
2. Parallel work opportunities: [Where work can be done concurrently]

### Effort Summary

| Phase | Tasks | Total Effort | Parallel Potential | Calendar Time |
|-------|-------|--------------|-------------------|---------------|
| Phase 0 | 5 | 3 weeks | Low (sequential) | 3-4 weeks |
| Phase 1 | 8 | 5 weeks | Medium | 3-4 weeks |
| Phase 2 | 12 | 8 weeks | High | 4-5 weeks |
| Phase 3 | 6 | 4 weeks | Medium | 2-3 weeks |
| **Total** | **31** | **20 weeks** | - | **12-16 weeks** |

### Risk Assessment

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [How to mitigate] |
| [Risk 2] | High/Med/Low | High/Med/Low | [How to mitigate] |

### Quick-Start Action Plan

**Immediate Actions (Start Today)**:
1. [ ] [Specific task with clear acceptance criteria]
2. [ ] [Specific task with clear acceptance criteria]
3. [ ] [Specific task with clear acceptance criteria]

**First Week Milestones**:
- [ ] [Milestone 1]
- [ ] [Milestone 2]

**First Month Goals**:
- [ ] [Goal 1 - Phase 0 complete]
- [ ] [Goal 2]

### Resource Requirements

**Tools/Infrastructure**:
- [Tool/service needed]
- [Access/accounts required]

**Knowledge/Skills**:
- [Expertise needed]
- [Learning resources]

**Time Commitment**:
- Minimum: [X hours/week] (part-time, extended timeline)
- Recommended: [Y hours/week] (steady progress)
- Optimal: [Z hours/week] (fast track)

---

## Success Criteria

Round 3 is successful if:
- ✅ Complete, actionable roadmap exists
- ✅ All tasks from Rounds 1 & 2 incorporated
- ✅ Dependencies clearly mapped
- ✅ Effort estimates and timeline provided
- ✅ Can start implementation immediately with clear first steps
- ✅ Risk factors identified with mitigation plans

---

## Output Checklist

When Round 3 is complete:

- [ ] `03-implementation-roadmap.md` created
- [ ] All phases defined with clear goals
- [ ] All tasks listed with effort estimates
- [ ] Dependencies mapped
- [ ] Quick-start action plan ready
- [ ] REFERENCES.md updated if new sources consulted
- [ ] 00-INDEX.md updated (Round 3 marked complete)
- [ ] Ready to begin implementation

---

**Placeholder**: This file is ready to use after Rounds 1 & 2 complete.
Review and customize if needed based on Round 2 findings.
