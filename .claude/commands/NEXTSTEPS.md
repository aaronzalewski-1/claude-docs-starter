# Next Steps - Sprint Planning Assistant

Analyze the project roadmap and suggest actionable tasks for the next sprint.

## Workflow

### Step 1: Review Current State

1. **Read the Roadmap**: `Read docs/CLAUDE/ROADMAP.md` - Review thoroughly
2. **Check Recent Changes**: `Read docs/CLAUDE/CHANGELOG.md` - Review latest completed work
3. **Verify Git Status**: Run `git log --oneline -10` to ensure roadmap reflects actual progress
4. **Check Work in Progress**: Run `git status` to identify uncommitted work

### Step 2: Roadmap Currency Check

Verify the roadmap is up to date by checking:

1. **Completed Items**: Are all recently completed features marked as ✅?
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
| **Complexity** | Medium | Low/Medium/High - Can this realistically fit in a sprint? |
| **Quick Wins** | Low | Any low-complexity, high-impact items to include? |

**Note:** Use complexity ratings (Low/Medium/High), not time estimates. Let the user determine scheduling.

### Step 4: Sprint Recommendation

Present your recommendations in this format:

## Recommended Sprint: v[X.Y] - [Theme]

**Goal:** [One sentence describing the sprint's primary objective]

### High Priority Tasks
| # | Task | Value | Complexity | Dependencies |
|---|------|-------|------------|--------------|
| 1 | ... | ... | Low/Med/High | ... |

### Medium Priority Tasks
| # | Task | Value | Complexity | Dependencies |
|---|------|-------|------------|--------------|
| 1 | ... | ... | Low/Med/High | ... |

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
4. **Scope Realistically**: Don't overload the sprint - quality over quantity
5. **Align with Architecture**: Ensure suggestions follow patterns in [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md)

## What NOT to Do

- **Don't propose tasks without reading actual code/files first** - Verify assumptions before recommending
- **Don't include time estimates** - Use complexity ratings only; let users determine scheduling
- **Don't recommend work already in progress** - Check git status for uncommitted changes
- **Don't duplicate existing roadmap items** - Cross-reference to avoid redundancy
- **Don't ignore dependencies** - If Task B requires Task A, don't put B before A

## Questions to Ask

Before finalizing recommendations, consider asking the user:

- What is the target deployment timeline?
- Are there any external dependencies or deadlines to consider?
- Is there preference for features vs. infrastructure work?
- Are any planned items now deprioritized or changed in scope?
