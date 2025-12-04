# Creating Custom Slash Commands

Custom slash commands let you create reusable workflows that Claude Code can execute with a single command.

## Quick Start

1. Create a Markdown file in `.claude/commands/`
2. The filename becomes the command (e.g., `MYCOMMAND.md` → `/MYCOMMAND`)
3. Write instructions in Markdown that tell Claude what to do

## File Structure

```
.claude/
└── commands/
    ├── MYCOMMAND.md      # /MYCOMMAND
    ├── review.md         # /review
    └── test-all.md       # /test-all
```

## Command Format

Commands are just Markdown files with instructions. Claude reads and follows them.

### Basic Example

```markdown
# Run Tests and Report

1. Run the test suite: `npm test`
2. If tests fail, analyze the failures
3. Suggest fixes for any failing tests
4. Report a summary of results
```

### Structured Example

```markdown
# Code Review Checklist

## Step 1: Gather Context
- Read the files that were changed (check git diff)
- Understand what the changes are trying to accomplish

## Step 2: Review Criteria
Check each change against:
- [ ] Follows project coding standards
- [ ] Has appropriate test coverage
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed

## Step 3: Output
Provide a structured review with:
1. **Summary**: What the changes do
2. **Strengths**: What's done well
3. **Concerns**: Issues to address
4. **Suggestions**: Optional improvements
```

## Tips for Effective Commands

### 1. Be Specific About Actions

```markdown
# Good - Clear actions
1. Run `npm test` to execute the test suite
2. Read any failing test files
3. Identify the root cause of failures

# Avoid - Vague instructions
1. Check if tests pass
2. Fix any issues
```

### 2. Reference Project Documentation

```markdown
## Required Reading
Before proceeding, read:
- [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md) - Coding standards
- [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) - System design

> **IMPORTANT**: Follow the patterns documented in these files.
```

### 3. Define Clear Output Format

```markdown
## Output Format
Present findings as:

| File | Issue | Severity | Recommendation |
|------|-------|----------|----------------|
| ... | ... | High/Medium/Low | ... |
```

### 4. Include Recovery Steps

```markdown
## If Stuck
If you encounter issues:
- Use `/REFOCUS` to reset your approach
- Ask the user for clarification before proceeding
```

### 5. Use Conditional Logic

```markdown
## Step 2: Based on Task Type

**If adding a new feature:**
- Check ROADMAP.md for context
- Review similar existing features

**If fixing a bug:**
- Find the root cause before fixing
- Add a regression test
```

## Command Patterns

### Workflow Command
Guides Claude through a multi-step process with checkpoints.
See: [DEEPPLAN.md](commands/DEEPPLAN.md)

### Recovery Command
Helps Claude reset when stuck or going in circles.
See: [REFOCUS.md](commands/REFOCUS.md)

### Analysis Command
Has Claude analyze something and produce a structured report.
See: [NEXTSTEPS.md](commands/NEXTSTEPS.md)

## Using Commands with Arguments

Commands can reference `$ARGUMENTS` to accept parameters:

```markdown
# Review PR

Review pull request $ARGUMENTS.

1. Fetch PR details: `gh pr view $ARGUMENTS`
2. Review the changes
3. Provide feedback
```

Usage: `/review 123` → Reviews PR #123

## Best Practices

1. **Keep commands focused** - One command, one purpose
2. **Document prerequisites** - What context does Claude need?
3. **Define success criteria** - How does Claude know it's done?
4. **Include examples** - Show the expected output format
5. **Reference existing docs** - Don't duplicate, link to DEVELOPMENT.md etc.

## Debugging Commands

If a command isn't working as expected:

1. **Check the filename** - Must be in `.claude/commands/` with `.md` extension
2. **Test incrementally** - Try simpler instructions first
3. **Be explicit** - Claude follows instructions literally
4. **Add checkpoints** - Include "PAUSE and confirm before proceeding" steps
