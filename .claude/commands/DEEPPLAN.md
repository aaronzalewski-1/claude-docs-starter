# Deep Planning - Structured Implementation Workflow

A systematic workflow for implementing non-trivial features with user checkpoints. Ensures investigation before planning, and approval before implementation.

## When to Use

Use `/DEEPPLAN` for:
- Multi-file features requiring coordination across layers
- New functionality where approach isn't obvious
- Changes affecting multiple system components
- Work that would benefit from phased commits

## When NOT to Use

Skip this workflow for:
- Single-file bug fixes with clear solutions
- Minor refactors or formatting changes
- Adding simple methods to existing patterns
- Work where you already have explicit, detailed instructions

For these, just implement directly.

---

## Phase 1: Investigate

**Do NOT propose solutions yet.** First, understand the landscape.

### Required Reading

```
Read docs/CLAUDE/DEVELOPMENT.md    # Architecture principles, patterns, lessons learned
```

### Conditional Reading (based on task type)

| Task Type | Read |
|-----------|------|
| Database/Entity work | `Read docs/CLAUDE/ARCHITECTURE.md` |
| API work | `Read docs/CLAUDE/API-REFERENCE.md` |
| Feature planning | `Read docs/CLAUDE/ROADMAP.md` |

### Codebase Investigation

1. **Find affected files**: Use Glob/Grep to locate code areas that will change
2. **Read existing patterns**: Understand how similar features are implemented
3. **Identify dependencies**: What does this touch? What touches this?
4. **Check for conflicts**: Is related work in progress? (`git status`)

**Output**: Brief summary of what you found (3-5 bullets max).

---

## Phase 2: Clarify

Ask questions ONLY about things not answered by investigation:

- Business requirements unclear from code/docs
- Ambiguous acceptance criteria
- Trade-offs requiring user preference
- Scope boundaries (what's in vs. out)

**If no questions needed, say so and proceed.**

---

## Phase 3: Plan

Present a phased implementation plan using this format:

### Implementation Plan: [Feature Name]

**Approach**: [1-2 sentence summary of the strategy]

| Phase | Objective | Files | Tests | Commit Message |
|-------|-----------|-------|-------|----------------|
| 1 | [Measurable goal] | [Specific files] | [Test coverage] | [Descriptive message] |
| 2 | [Measurable goal] | [Specific files] | [Test coverage] | [Descriptive message] |

**Complexity**: Low / Medium / High

**Risks**: [Any technical risks or uncertainties]

---

## Phase 4: Approve

After presenting the plan:

> **Ready to proceed with this plan?**
> - "yes" / "proceed" → Begin implementation
> - "no" / feedback → Revise plan based on input
> - "simplify" → Reduce scope to MVP

**Do NOT begin implementation without explicit approval.**

---

## Phase 5: Implement

For each phase in the plan:

1. **Track**: Create TodoWrite entries for phase tasks
2. **Implement**: Follow patterns from DEVELOPMENT.md
3. **Test**: Write and run tests for the phase
4. **Review**: Present a summary of changes before committing:
   - Files modified
   - Key changes made
   - Test results
5. **Commit**: After user approval, commit with planned message
6. **Complete**: Mark todos done, proceed to next phase

### Between Phases

Pause and confirm before starting the next phase:
> **Phase N complete. Ready for Phase N+1?**

---

## Phase 6: Document

After final commit, update:

| File | Action |
|------|--------|
| `docs/CLAUDE/CHANGELOG.md` | Add entry for this change |
| `docs/CLAUDE/ROADMAP.md` | Move to "Completed" if applicable |

---

## Recovery

### Signs You Need to Refocus

- Same error appearing after 3+ fix attempts
- Scope creeping beyond original plan
- Uncertainty about root cause
- Making changes without understanding why

### Action

Invoke `/REFOCUS` to:
1. Dump current state
2. Re-read debugging guidance
3. Produce revised approach

---

## What NOT to Do

- **Don't propose plans before investigating** - Read code first
- **Don't implement before approval** - Wait for explicit "yes"
- **Don't skip phases** - Each checkpoint prevents rework
- **Don't batch commits** - One commit per phase
- **Don't ignore test failures** - Fix before proceeding
- **Don't forget documentation** - CHANGELOG updates are required

---

## Completion

After Phase 6:
- Summarize what was delivered
- Suggest `/NEXTSTEPS` if user wants to plan follow-up work
