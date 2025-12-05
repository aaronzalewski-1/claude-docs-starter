# Deep Planning Implementation Workflow

## Step 1: Present Plan for Review
Present the implementation plan as text in the conversation. Do NOT use the `EnterPlanMode` tool.
After presenting the plan, ask "Ready to proceed?" and wait for explicit user confirmation before implementing.

## Step 2: Load Required Context
**Read these files BEFORE asking any questions:**

**Always read:**
- [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md) - Architecture principles, debugging guidance, lessons learned

**Conditional - based on task type:**
- **Database/Entity work**: [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) - Schema, domain model
- **API work**: [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md) - Endpoints, response formats
- **Feature planning**: [ROADMAP.md](docs/CLAUDE/ROADMAP.md) - Planned features, priorities

**Also read relevant existing code in the affected areas.**

> **IMPORTANT**: Do NOT ask questions that are answered in these documents.

## Step 3: Clarifying Questions
Ask ONLY about:
- Business requirements not covered in documentation
- Ambiguous acceptance criteria
- Trade-off decisions requiring user input
- Scope boundaries

## Step 4: Present Phased Implementation Plan
Use this table format:

| Phase | Objective | Files Affected | Integration Tests | Commit Message |
|-------|-----------|----------------|-------------------|----------------|
| 1     | ...       | ...            | ...               | ...            |
| 2     | ...       | ...            | ...               | ...            |

Include for each phase:
- Clear, measurable objective
- Specific files to create/modify
- Integration test coverage
- Descriptive commit message

## Step 5: Implementation Workflow
For each phase:

1. **Create TodoWrite entries** for phase tasks
2. **Implement** changes following DEVELOPMENT.md patterns
3. **Write and run** integration tests
4. **PAUSE** - Present changes for user review before commit
5. **Commit** with the planned message after approval
6. **Mark todos complete** and proceed to next phase

## Step 6: Documentation Updates
At completion, update these specific files:

| File | Update Required |
|------|-----------------|
| **CHANGELOG.md** | Add version entry documenting changes |
| **ROADMAP.md** | Move completed items to "Completed Milestones" |
| **SESSION-STATE.json** | Clear or update (for multi-phase work only) |

## Recovery
If debugging spirals or implementation gets stuck:
- Suggest `/REFOCUS` to reset approach systematically

## Completion
After final commit and documentation updates:
- Suggest `/NEXTSTEPS` if user wants to plan follow-up work
