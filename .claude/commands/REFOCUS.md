# Stop and Refocus - Debug Reset Protocol

**STOP.** Take a step back from the current debugging approach.

## Immediate Actions

1. **Enter Plan Mode**: Use `EnterPlanMode` to reset context and think systematically

2. **State the Problem Clearly**: In 1-2 sentences, what is the actual error or unexpected behavior? Not symptoms, but the core issue.

3. **Review What's Been Tried**: List the approaches already attempted and why they didn't work

## Required Reading Before Continuing

Re-read these sections from [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md):

1. **Debugging Checklist** - The 8-step checklist for when integration tests fail
2. **Debugging Best Practices** - Detailed debugging methodology
3. **Lessons Learned from Real Refactorings** - Past mistakes and their solutions

## Refocus Questions

Answer these before proposing a new approach:

1. **Do I have the actual error message?** (Not just HTTP status codes)
2. **Have I verified the basic assumptions?** (Target frameworks match? Dependencies registered? Database migrated?)
3. **Am I solving the right problem?** (Or a symptom of a deeper issue?)
4. **What does the simplest possible test case look like?**
5. **Is there a similar pattern in the codebase that already works?**

## Common Rabbit Holes to Avoid

- Debugging from HTTP status codes instead of actual exceptions
- Assuming the problem is complex when it might be simple (missing registration, wrong framework)
- Making changes without understanding the existing code first
- Not checking if tests target the correct framework version

## Output

After reviewing, present:
1. **Revised Problem Statement**: What we're actually solving
2. **Root Cause Hypothesis**: Based on evidence, not guessing
3. **Proposed Approach**: Simple, focused next step
4. **Validation Method**: How we'll know if it works
