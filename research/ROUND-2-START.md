# Start Round 2 Analysis - Quick Reference

Copy this prompt to start Round 2 in a fresh Claude Code session:

---

## Prompt for Claude Code:

```
I need you to conduct Round 2 of the platform-linux_arm modernization research.

CONTEXT:
- This is a forked PlatformIO platform for ARM Linux (Raspberry Pi, etc.)
- Round 1 identified 4 critical priorities that need deep technical analysis
- You're in Round 2: detailed analysis with concrete implementation guidance

BEFORE YOU START:
1. Read research/00-INDEX.md to understand the workflow
2. Read research/01-initial-assessment.md for Round 1 findings
3. Read research/REFERENCES.md for existing sources
4. Read research/FINDINGS-TEMPLATE.md for output structure

YOUR TASK:
Execute the detailed research plan in research/02-ROUND-2-PROMPT.md

DELIVERABLES (create 4 separate markdown files):
- research/02-priority-cross-compilation.md
- research/02-priority-frameworks.md
- research/02-priority-boards.md
- research/02-priority-ci-cd.md

Each document must follow FINDINGS-TEMPLATE.md structure and include:
- Executive summary with clear recommendations
- Detailed technical analysis with code examples
- Concrete implementation guidance
- Refined effort estimates
- All sources added to REFERENCES.md

WHEN COMPLETE:
- Update research/REFERENCES.md with all new sources
- Update research/00-INDEX.md to mark Round 2 complete

RESEARCH APPROACH:
- Use WebSearch/WebFetch extensively for toolchains, frameworks, hardware specs
- Fetch code from reference platforms (espressif32, raspberrypi, ststm32)
- Extract reusable patterns and provide concrete code examples
- Focus on actionable technical designs, not just descriptions

Estimated time: 3-4 hours
Can split into two sessions: Priorities 1-2, then 3-4

Begin Round 2 analysis now.
```

---

## Alternative Minimal Prompt (if above is too long):

```
Execute Round 2 modernization research for platform-linux_arm.

1. Read: research/02-ROUND-2-PROMPT.md (full instructions)
2. Read: research/01-initial-assessment.md (context from Round 1)
3. Produce 4 analysis documents following research/FINDINGS-TEMPLATE.md
4. Update REFERENCES.md and 00-INDEX.md when done

Begin now.
```

---

## Why This Works:

✅ **Points to the main instructions**: 02-ROUND-2-PROMPT.md has all the details
✅ **Provides context**: Tells Claude what Round 1 found and where to read it
✅ **Sets expectations**: 4 deliverables, specific structure, update tracking files
✅ **Guides approach**: WebSearch/WebFetch, extract patterns, concrete examples
✅ **Time estimate**: Helps Claude pace the work

The 02-ROUND-2-PROMPT.md is very comprehensive, so Claude mainly needs to be:
1. Told to read the prerequisite files
2. Reminded to follow the template structure
3. Reminded to update tracking files

Choose whichever prompt length you prefer - both should work!
