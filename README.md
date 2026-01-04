# CLAUDE Documentation Starter Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://docs.anthropic.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Templates and patterns for AI-assisted development with Claude Code**

A starter kit for organizing [Claude Code](https://docs.anthropic.com/en/docs/claude-code) documentation in your projects. Includes proven patterns for maintaining project context, custom slash commands, multi-persona decision analysis, and operational checklists that help Claude work more effectively with your codebase.

## Why Use This?

Claude Code works best when it has structured context about your project. This documentation pattern:

- **Reduces repetitive explanations** - Document architectural decisions once, reference everywhere
- **Prevents common mistakes** - Capture lessons learned so Claude doesn't repeat them
- **Enables context loading** - Load relevant docs only when needed (database work, API work, etc.)
- **Tracks project evolution** - Maintain changelog and roadmap for continuity across sessions
- **Provides structured decision analysis** - Multi-persona reviews surface tradeoffs and reduce blind spots

## Quick Start

1. Copy to your project root:
   - `CLAUDE.md` file
   - `docs/CLAUDE/` folder
   - `.claude/` folder (commands, skills, templates, settings)
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
| `docs/CLAUDE/IMPROVEMENTS.md` | Improvement proposals | Track refactoring ideas and their status |
| `docs/CLAUDE/APPENDIX.md` | Supplementary reference | Process diagrams, seed data, glossary |
| `docs/CLAUDE/PERSONAS.md` | Multi-persona system reference | Understand available personas and packages |
| `docs/CLAUDE/PERSONA-PACKAGES.md` | Guide for creating persona packages | Create domain-specific analytical lenses |
| `docs/CLAUDE/CORE-LIBRARY.md` | Library/SDK documentation | ADRs, public API surface (optional) |
| `docs/CLAUDE/SESSION-STATE.template.json` | Multi-session state tracking | Use as-is for complex multi-session work |

## Documentation Structure

```
your-project/
├── CLAUDE.md                    # Entry point - always read first
├── .claude/
│   ├── commands/                # Slash commands and orchestrators
│   │   ├── DEEPPLAN.md          # /DEEPPLAN - Structured implementation workflow
│   │   ├── REFOCUS.md           # /REFOCUS - Debug reset protocol
│   │   ├── NEXTSTEPS.md         # /NEXTSTEPS - Sprint planning assistant
│   │   ├── review-product-decision.md   # Multi-persona product analysis
│   │   ├── review-research.md           # Multi-persona research analysis
│   │   ├── review-business-decision.md  # Multi-persona business advisory
│   │   ├── export-artifact.md           # Generate formal documents
│   │   ├── codebase-context.md          # Quick project summary
│   │   └── personas/            # Individual persona commands
│   │       ├── product/         # Skeptic, Architect, Economist, Pragmatist
│   │       ├── research/        # Skeptic, Librarian, Methodologist, Critic, Synthesizer
│   │       └── advisory/        # Skeptic, CFO, GTM, Strategist, Ops, Product, Counsel
│   ├── skills/                  # Domain expertise backing personas
│   │   ├── artifact-registry.skill.md   # Artifact type definitions
│   │   └── personas/            # Persona knowledge bases
│   │       ├── product/         # SOLID, patterns, TCO, MVP criteria
│   │       ├── research/        # CRAAP test, evidence hierarchies, synthesis
│   │       └── advisory/        # Unit economics, GTM, strategy, compliance
│   ├── templates/               # Artifact document templates
│   │   ├── product/             # ADR template
│   │   ├── research/            # Literature review template
│   │   └── advisory/            # Board memo template
│   ├── CREATING-COMMANDS.md     # Guide: How to create your own commands
│   ├── CREATING-SKILLS.md       # Guide: How to create project skills
│   ├── settings.template.json   # Template: Auto-approve permissions
│   ├── hooks.template.json      # Template: Pre/post tool hooks
│   └── README.md                # Explains the .claude folder
└── docs/
    ├── CLAUDE/
    │   ├── DEVELOPMENT.md       # How to work on this project
    │   ├── ARCHITECTURE.md      # What the system looks like
    │   ├── API-REFERENCE.md     # API endpoint details
    │   ├── CHANGELOG.md         # What changed and when
    │   ├── ROADMAP.md           # What's planned
    │   ├── IMPROVEMENTS.md      # Improvement proposals and status
    │   ├── APPENDIX.md          # Supplementary reference material
    │   ├── PERSONAS.md          # Multi-persona system reference
    │   ├── PERSONA-PACKAGES.md  # Creating new persona packages
    │   ├── CORE-LIBRARY.md      # For library/SDK projects (optional)
    │   └── SESSION-STATE.template.json
    └── decisions/               # Generated decision artifacts
        ├── product/             # ADRs from /review-product-decision
        ├── research/            # Literature reviews from /review-research
        └── advisory/            # Board memos from /review-business-decision
```

## Key Features

### Multi-Persona Decision Analysis

The starter kit includes a complete multi-persona system for structured decision analysis. Instead of single-perspective answers, get analysis from multiple complementary viewpoints with weighted consensus.

**Three domain packages:**

| Package | Orchestrator | Personas | Use For |
|---------|--------------|----------|---------|
| **Product** | `/review-product-decision` | Skeptic, Architect, Economist, Pragmatist | Architecture choices, technology selection, scope decisions |
| **Research** | `/review-research` | Skeptic, Librarian, Methodologist, Critic, Synthesizer | Source evaluation, claim verification, literature synthesis |
| **Advisory** | `/review-business-decision` | Skeptic, CFO, GTM, Strategist, Ops, Product, Counsel | Strategic decisions, funding, growth, partnerships |

**Example usage:**
```
/review-product-decision Should we use Redis or Memcached for session caching?
```

Each persona analyzes from their unique perspective, then the orchestrator synthesizes a weighted consensus that varies by context (project phase, decision type).

**Individual personas** can also be invoked directly:
```
/personas:product:architect Evaluate this service layer design
/personas:advisory:cfo What's our runway if we hire 5 engineers?
/personas:research:librarian Evaluate these sources on climate change
```

See [PERSONAS.md](docs/CLAUDE/PERSONAS.md) for complete documentation.

### Artifact Production

After running a multi-persona review, export the analysis to formal documents:

```
/review-product-decision Should we add a caching layer?
[... analysis completes ...]

/export-artifact adr caching-decision
→ docs/decisions/product/2026-01-04-caching-decision/README.md
```

**Available artifacts:**

| Package | Artifact | Command |
|---------|----------|---------|
| Product | Architecture Decision Record | `/export-artifact adr <name>` |
| Research | Literature Review | `/export-artifact literature-review <name>` |
| Advisory | Board Memo | `/export-artifact board-memo <name>` |

Generated markdown converts to PDF/DOCX via pandoc.

### Context Loading Triggers

The `CLAUDE.md` file includes XML-style triggers that tell Claude when to load specific documentation:

```xml
<load_database_context>
Before modifying database schema:
1. Read ARCHITECTURE.md
2. Check existing entity patterns
</load_database_context>

<load_decision_review_context>
When evaluating architectural choices or technology selections:
Use /review-product-decision for multi-persona analysis
</load_decision_review_context>
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

### Workflow Commands

| Command | When to Use | What It Does |
|---------|-------------|--------------|
| `/DEEPPLAN` | Starting a multi-step feature | Presents plan for approval, creates phased implementation |
| `/REFOCUS` | Debugging spirals or stuck | Stops, re-reads guidance, produces revised approach |
| `/NEXTSTEPS` | Planning next sprint | Analyzes roadmap, suggests prioritized tasks |
| `/codebase-context` | Session start | Quick project summary with file counts, recent commits |

**Create your own:** See [.claude/CREATING-COMMANDS.md](.claude/CREATING-COMMANDS.md) for a guide on writing custom commands.

### Settings & Hooks Templates

Configure Claude Code behavior with the included templates:

| Template | Purpose |
|----------|---------|
| `settings.template.json` | Auto-approve common commands (build, test, lint) |
| `hooks.template.json` | Run scripts before/after tool calls (auto-format, notifications) |

**Setup:** Copy `settings.template.json` to `settings.local.json`, uncomment the commands for your tech stack, and customize.

## Optional Folders

These folders are recommended for larger projects:

| Folder | Purpose | When to Use |
|--------|---------|-------------|
| `docs/archive/` | Historical planning documents | Keep old plans/designs for reference |
| `docs/research/` | Domain knowledge, external frameworks | Store research materials, competitive analysis |
| `docs/diagrams/` | Mermaid diagrams, architecture visuals | When visual documentation helps understanding |
| `docs/CLAUDE/PLAN-*.md` | Implementation plans | For complex features needing dedicated planning |

## Tips for Success

1. **Start with DEVELOPMENT.md** - This file has the most reusable content. Fill in your environment setup and coding guidelines first.

2. **Add lessons as you learn them** - When Claude makes a mistake or you discover a gotcha, add it to the Lessons Learned section.

3. **Keep it current** - Update CHANGELOG.md with each release. Stale documentation is worse than no documentation.

4. **Use multi-persona reviews for significant decisions** - The structured disagreement surfaces tradeoffs a single perspective would miss.

5. **Export artifacts for decisions that matter** - ADRs and board memos create institutional memory that outlasts any single conversation.

6. **Don't over-document** - Focus on things Claude gets wrong or asks about repeatedly. Let code speak for itself where possible.

7. **Use the Greenfield directive** - For new projects without production users, keep the `<greenfield_development>` section in CLAUDE.md. For established projects, remove it.

## Contributing

Found a pattern that works well? Open a PR to share improvements with the community.

## License

MIT License - Use freely in your projects.

---

*This starter kit was extracted from production documentation patterns that evolved over months of Claude Code usage. The multi-persona system reflects research into structured disagreement as a decision-making tool.*
