# Next Steps - Sprint Planning Assistant

Analyze the project roadmap and suggest actionable tasks for the next sprint.

## Workflow

### Step 1: Review Current State

1. **Read the Roadmap**: Review [ROADMAP.md](docs/CLAUDE/ROADMAP.md) thoroughly
2. **Check Recent Changes**: Review [CHANGELOG.md](docs/CLAUDE/CHANGELOG.md) for the latest completed work
3. **Verify Git Status**: Check recent commits to ensure roadmap reflects actual progress

### Step 2: Roadmap Currency Check

Verify the roadmap is up to date by checking:

1. **Completed Items**: Are all recently completed features marked as done?
2. **Version Numbers**: Does the current version in docs match the latest work?
3. **Planned Sprint**: Is there a defined next sprint with clear priorities?
4. **Stale Items**: Are there any planned items that have been completed but not updated?

If the roadmap is out of date, **propose specific updates** before proceeding.

### Step 3: Analyze Sprint Candidates

For the next sprint, evaluate potential tasks against these criteria:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Dependencies** | High | What must be completed first? What does this unblock? |
| **Business Value** | High | Does this move toward production readiness or key features? |
| **Technical Risk** | Medium | Is this well-understood or does it need exploration first? |
| **Effort Estimate** | Medium | Can this realistically fit in a sprint? |
| **Quick Wins** | Low | Any low-effort, high-impact items to include? |

### Step 4: Sprint Recommendation

Present your recommendations in this format:

## Recommended Sprint: v[X.Y] - [Theme]

**Goal:** [One sentence describing the sprint's primary objective]

### High Priority Tasks
| # | Task | Value | Effort | Dependencies |
|---|------|-------|--------|--------------|
| 1 | ... | ... | ... | ... |

### Medium Priority Tasks
| # | Task | Value | Effort | Dependencies |
|---|------|-------|--------|--------------|
| 1 | ... | ... | ... | ... |

### Optional Stretch Goals
- [Items to tackle if time permits]

### Rationale
[Brief explanation of why these tasks were selected and how they align with project goals]

### Risks & Mitigations
[Any technical or schedule risks with the proposed sprint]

## Output Requirements

1. **Be Specific**: Reference actual file paths, endpoints, or features from the codebase
2. **Be Actionable**: Each task should be something that can be picked up and started
3. **Consider Dependencies**: Order tasks logically based on what must come first
4. **Estimate Realistically**: Don't overload the sprint - quality over quantity
5. **Align with Architecture**: Ensure suggestions follow patterns in [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md)

## Questions to Ask

Before finalizing recommendations, consider asking the user:

- What is the target deployment timeline?
- Are there any external dependencies or deadlines to consider?
- Is there preference for features vs. infrastructure work?
- Are any planned items now deprioritized or changed in scope?
