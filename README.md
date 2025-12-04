# CLAUDE Documentation Starter Kit

A template structure for organizing [Claude Code](https://docs.anthropic.com/en/docs/claude-code) documentation in your projects. This starter kit provides a proven organizational pattern for maintaining project context that helps Claude Code work more effectively with your codebase.

## Why Use This?

Claude Code works best when it has structured context about your project. This documentation pattern:

- **Reduces repetitive explanations** - Document architectural decisions once, reference everywhere
- **Prevents common mistakes** - Capture lessons learned so Claude doesn't repeat them
- **Enables context loading** - Load relevant docs only when needed (database work, API work, etc.)
- **Tracks project evolution** - Maintain changelog and roadmap for continuity across sessions

## Quick Start

1. Copy the `CLAUDE.md` file and `docs/CLAUDE/` folder to your project root
2. Find and replace all `{{PLACEHOLDER}}` markers with your project values
3. Fill in project-specific sections (architecture, API endpoints, etc.)
4. Commit the docs to your repository

## Placeholders Reference

Use find-and-replace to customize these placeholders:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Your project name | MyApp |
| `{{PROJECT_DESCRIPTION}}` | One-line description | E-commerce platform for handmade goods |
| `{{VERSION}}` | Current version | 1.0.0 |
| `{{LAST_UPDATED}}` | Last update date | January 2025 |
| `{{TECH_STACK_BACKEND}}` | Backend framework | ASP.NET Core 8.0 |
| `{{TECH_STACK_FRONTEND}}` | Frontend framework | React 18 |
| `{{TECH_STACK_DATABASE}}` | Database technology | PostgreSQL + EF Core |
| `{{REPO_URL}}` | Repository URL | https://github.com/org/repo |

## File Overview

| File | Purpose | What to Customize |
|------|---------|-------------------|
| `CLAUDE.md` | Navigation hub and quick reference | Context triggers, tech stack, critical reminders |
| `docs/CLAUDE/DEVELOPMENT.md` | Operational guidelines for Claude | Add your lessons learned, project-specific patterns |
| `docs/CLAUDE/ARCHITECTURE.md` | System design documentation | Your entities, schema, project structure |
| `docs/CLAUDE/API-REFERENCE.md` | Endpoint documentation | Your API endpoints and DTOs |
| `docs/CLAUDE/CHANGELOG.md` | Version history | Track your releases and changes |
| `docs/CLAUDE/ROADMAP.md` | Feature planning | Your milestones and planned work |
| `docs/CLAUDE/SESSION-STATE.template.json` | Multi-session state tracking | Use as-is for complex multi-session work |

## Documentation Structure

```
your-project/
├── CLAUDE.md                    # Entry point - always read first
└── docs/
    └── CLAUDE/
        ├── DEVELOPMENT.md       # How to work on this project
        ├── ARCHITECTURE.md      # What the system looks like
        ├── API-REFERENCE.md     # API endpoint details
        ├── CHANGELOG.md         # What changed and when
        ├── ROADMAP.md           # What's planned
        └── SESSION-STATE.template.json
```

## Key Patterns Included

### Context Loading Triggers

The `CLAUDE.md` file includes XML-style triggers that tell Claude when to load specific documentation:

```xml
<load_database_context>
Before modifying database schema:
1. Read ARCHITECTURE.md
2. Check existing entity patterns
</load_database_context>
```

### Lessons Learned Framework

`DEVELOPMENT.md` includes a case study template for documenting mistakes:

```markdown
**Case Study N: [Title] ([Date])**

**Context:** What were you trying to do?
**The Mistake:** What went wrong?
**Why It Was Wrong:** Root cause analysis
**What Should Have Been Done:** Correct approach
**General Principles Derived:** Lessons for the future
```

### Operational Checklists

Pre-built checklists for common workflows:
- Architectural analysis (5 steps)
- Debugging integration tests (8 steps)
- Pre-commit verification

## Tips for Success

1. **Start with DEVELOPMENT.md** - This file has the most reusable content. Fill in your environment setup and coding guidelines first.

2. **Add lessons as you learn them** - When Claude makes a mistake or you discover a gotcha, add it to the Lessons Learned section.

3. **Keep it current** - Update CHANGELOG.md with each release. Stale documentation is worse than no documentation.

4. **Use context triggers** - Add `<load_X_context>` sections for areas where Claude frequently needs reminders.

5. **Don't over-document** - Focus on things Claude gets wrong or asks about repeatedly. Let code speak for itself where possible.

## Contributing

Found a pattern that works well? Open a PR to share improvements with the community.

## License

MIT License - Use freely in your projects.

---

*This starter kit was extracted from production documentation patterns that evolved over months of Claude Code usage.*
