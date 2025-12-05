# {{PROJECT_NAME}} - Claude Code Documentation

**Version:** {{VERSION}}
**Last Updated:** {{LAST_UPDATED}}
**Project Type:** {{PROJECT_DESCRIPTION}}

---

## Documentation Index

The documentation is split into focused files for better organization and reduced context consumption.

**Location:** `docs/CLAUDE/`

| Document | Purpose |
|----------|---------|
| **[DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md)** | **READ FIRST** - Operational guidelines, coding patterns, lessons learned |
| [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) | System architecture, database schema, domain model |
| [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md) | REST API endpoints, request/response formats |
| [CHANGELOG.md](docs/CLAUDE/CHANGELOG.md) | Version history, migration notes |
| [ROADMAP.md](docs/CLAUDE/ROADMAP.md) | Completed milestones, planned features |
| [IMPROVEMENTS.md](docs/CLAUDE/IMPROVEMENTS.md) | Improvement proposals, implementation status |
| [APPENDIX.md](docs/CLAUDE/APPENDIX.md) | Process diagrams, seed data, glossary |

---

## Auto-Loaded Context

The following documentation is automatically loaded at session start:

@docs/CLAUDE/DEVELOPMENT.md

---

## Greenfield Development Directive

<!-- Remove this section if your project has production users requiring backwards compatibility -->

<greenfield_development>
**For greenfield projects with no production users:**

When proposing solutions:
- **Delete deprecated code** - Don't maintain legacy patterns "just in case"
- **Break interfaces freely** - Change APIs and schemas without migration concerns
- **Remove unused features** - If something isn't being used, delete it
- **Simplify aggressively** - Choose the cleanest design
- **No deprecation warnings** - Just remove or replace
- **Schema changes are cheap** - Drop and recreate if simpler

**Anti-patterns to avoid:**
- Adding `_legacy` suffixes to preserve old code
- Creating adapter layers for backwards compatibility
- Maintaining multiple ways to do the same thing
- Keeping deprecated fields "for safety"
</greenfield_development>

---

## Quick Start

1. **Always read [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md) first** - contains critical operational patterns
2. For database/entity work, read [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md)
3. For API work, read [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md)
4. For understanding recent changes, read [CHANGELOG.md](docs/CLAUDE/CHANGELOG.md)
5. For improvement planning, read [IMPROVEMENTS.md](docs/CLAUDE/IMPROVEMENTS.md)

### Session Initialization
At the start of complex or multi-session work:
1. Review recent git commits: `git log --oneline -10`
2. Check for in-progress work in `docs/CLAUDE/SESSION-STATE.json`
3. Run build to verify baseline: `{{BUILD_COMMAND}}`
4. Load context-specific documentation based on task type (see Context Loading Triggers)

---

## Context Loading Triggers

<!--
Add context triggers for your project. These help Claude load the right documentation
at the right time. Examples below - customize for your domain.
-->

<load_database_context>
Before modifying database schema, entities, or data access:
1. Read [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) - database schema section
2. Check existing entity patterns in your entities folder
3. Review migration history
</load_database_context>

<load_api_context>
Before modifying or adding API endpoints:
1. Read [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md)
2. Check existing controller patterns
3. Review endpoint naming conventions
</load_api_context>

<load_frontend_context>
Before modifying UI components:
1. Review existing component patterns
2. Check CSS/styling conventions
3. Follow established state management patterns
</load_frontend_context>

<!-- Add more context triggers as needed for your domain -->

---

## Frontend Design Guidelines

<!-- Customize with your project's specific frontend patterns -->

<frontend_design_thinking>
**Before building any UI**, establish context:
- **Purpose**: What problem does this interface solve? Who are the users?
- **Tone**: Commit to a bold aesthetic direction (minimalist, editorial, etc.)
- **Constraints**: Framework requirements, performance needs, accessibility
- **Differentiation**: What makes this design memorable?
</frontend_design_thinking>

<frontend_aesthetics>
**When implementing UI**, consider:
- **Typography**: Choose distinctive fonts appropriate for the project
- **Color & Theme**: Commit to cohesive palettes using CSS variables
- **Motion**: Focus on high-impact moments (page loads, staggered reveals)
- **Spatial Composition**: Use intentional negative space and layout
</frontend_aesthetics>

---

## Product Overview

{{PROJECT_DESCRIPTION}}

### Key Features
<!-- List 3-5 key features or differentiators -->
1. Feature one
2. Feature two
3. Feature three

### Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Backend | {{TECH_STACK_BACKEND}} | |
| Frontend | {{TECH_STACK_FRONTEND}} | |
| Database | {{TECH_STACK_DATABASE}} | |
<!-- Add more as needed: Cache, Message Queue, Cloud Provider, etc. -->

### Key Architectural Decisions
<!-- Document 3-5 important architectural choices and WHY they were made -->
1. **Decision One**: Rationale for this choice
2. **Decision Two**: Rationale for this choice
3. **Decision Three**: Rationale for this choice

---

## Critical Reminders

<!--
Add project-specific reminders here. These are things Claude frequently forgets
or gets wrong. Examples:
-->

### Before Making Changes
- [ ] Read relevant files before editing (Edit tool requires prior Read)
- [ ] Understand existing patterns before introducing new ones
- [ ] Check for related tests that may need updating

### Environment-Specific Notes
<!-- Add notes about your development environment -->
- Build command: `{{BUILD_COMMAND}}`
- Test command: `{{TEST_COMMAND}}`
- Database migrations: `{{MIGRATION_COMMAND}}`

### Common Gotchas
<!-- Document things that cause confusion or errors -->
1. Gotcha one - how to avoid it
2. Gotcha two - how to avoid it

---

## Verification Checklist

<verification_before_commit>
Run these checks before committing changes:

**Build & Tests**
```bash
# Build
{{BUILD_COMMAND}}

# Run tests
{{TEST_COMMAND}}
```

**Database Changes**
- [ ] Migration created if schema changed
- [ ] Migration reviewed for correctness
- [ ] Seed data updated if needed

**API Changes**
- [ ] Endpoint tested manually or via integration test
- [ ] Response format documented in API-REFERENCE.md
</verification_before_commit>

---

## Session Best Practices

### General Principles
- **Be explicit**: Specify desired output format and behavior clearly
- **Add context**: Explain *why* a behavior matters for better targeted responses
- **Examples matter**: Provide examples that align with desired behaviors

### Agentic Guidelines

<do_not_act_before_instructions>
Do not jump into implementation unless clearly instructed. When intent is ambiguous,
default to providing information and recommendations rather than making changes.
</do_not_act_before_instructions>

<investigate_before_answering>
Never speculate about code you have not read. If referencing a file, read it first.
Investigate relevant files BEFORE answering questions about the codebase.
</investigate_before_answering>

<avoid_overengineering>
Only make changes that are directly requested or clearly necessary. Keep solutions
simple and focused. Don't add features, refactor code, or make "improvements"
beyond what was asked.
</avoid_overengineering>

<avoid_hardcoding>
Implement solutions that work correctly for all valid inputs, not just test cases.
Do not hard-code values that only work for specific test inputs.
Focus on understanding requirements and implementing correct algorithms.
If tests are incorrect, inform the user rather than working around them.
</avoid_hardcoding>

---

**Full documentation: [docs/CLAUDE/](docs/CLAUDE/)**
