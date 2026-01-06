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
| [CORE-LIBRARY.md](docs/CLAUDE/CORE-LIBRARY.md) | Library/SDK documentation (optional) |

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

Context triggers ensure Claude loads the right documentation at the right time. Each trigger specifies:
- **When** to activate (task patterns)
- **What** to read (required documentation)
- **Why** it matters (prevents common mistakes)

<!--
Customize these triggers for your project. Add domain-specific triggers as needed.
-->

<load_database_context>
**When:** Modifying database schema, entities, migrations, or data access patterns.
**Triggers:** schema, migration, entity, DbContext, repository, query

**Example phrases that trigger this context:**
- "Add a new table for..."
- "Create a migration to..."
- "Update the User entity..."
- "Add a foreign key between..."

**Required Reading:**
1. [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) - Database schema section
2. Existing entity definitions in your models/entities folder
3. Recent migration files for naming conventions

**Why:** Prevents schema inconsistencies, naming convention violations, and migration ordering issues.
</load_database_context>

<load_api_context>
**When:** Creating or modifying REST/GraphQL endpoints, DTOs, or API contracts.
**Triggers:** endpoint, controller, API, DTO, request, response

**Example phrases that trigger this context:**
- "Add an endpoint for..."
- "Create a new API for..."
- "What should the response format be for..."
- "Add validation to the request..."

**Required Reading:**
1. [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md) - Endpoint conventions
2. Existing controller patterns for consistency
3. DTO naming and validation patterns

**Why:** Ensures consistent endpoint naming, response formats, and error handling.
</load_api_context>

<load_frontend_context>
**When:** Building or modifying UI components, views, or client-side logic.
**Triggers:** component, view, page, UI, frontend, styling

**Required Reading:**
1. Existing component patterns and folder structure
2. CSS/styling conventions (design system, variables)
3. State management patterns in use

**Why:** Maintains visual consistency and predictable component behavior.
</load_frontend_context>

<load_testing_context>
**When:** Writing or modifying unit tests, integration tests, or test infrastructure.
**Triggers:** test, spec, fixture, mock, assertion

**Required Reading:**
1. Existing test patterns and naming conventions
2. Test data setup and fixture patterns
3. Shared test utilities or helpers

**Why:** Ensures tests are consistent, maintainable, and follow established patterns.
</load_testing_context>

<load_debugging_context>
**When:** Investigating failures, unexpected behavior, or integration issues.
**Triggers:** error, failure, bug, broken, not working, debug

**Example phrases that trigger this context:**
- "Why is this test failing?"
- "I'm getting error X when..."
- "This endpoint returns 500"
- "The build is broken after..."

**Required Reading:**
1. [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md) - Debugging Checklist section
2. Recent git commits for related changes
3. Build/test output for actual error messages

**Why:** Prevents debugging spirals. Follow the checklist: get the actual error message, verify infrastructure, test layers independently.
</load_debugging_context>

<load_decision_review_context>
**When:** Evaluating architectural choices, technology selections, or implementation approaches.
**Triggers:** should we, which approach, compare, tradeoffs, decision, evaluate

**Example phrases that trigger this context:**
- "Should we use Redis or Memcached?"
- "What's the best approach for..."
- "Compare these two options..."
- "Evaluate whether we should..."

**Required Action:**
Use `/review-product-decision <decision>` to run multi-persona analysis, or invoke individual personas:
- `/personas/core:skeptic` - Verify claims and challenge assumptions
- `/personas/product:architect` - Evaluate structural integrity
- `/personas/product:economist` - Analyze costs and ROI
- `/personas/product:pragmatist` - Find MVP path

**Why:** Prevents one-dimensional analysis. Multiple perspectives reveal hidden tradeoffs.
</load_decision_review_context>

<load_improvements_context>
**When:** Planning major architectural work, refactoring, or new features.
**Triggers:** refactor, improve, redesign, proposal, enhancement

**Required Reading:**
1. [IMPROVEMENTS.md](docs/CLAUDE/IMPROVEMENTS.md) - Check if already proposed
2. Related improvement proposals for dependencies
3. [ROADMAP.md](docs/CLAUDE/ROADMAP.md) - Current priorities

**Why:** Prevents duplicate work and ensures changes align with project direction.
</load_improvements_context>

<load_core_library_context>
<!-- Use this if your project has a shared library or SDK component -->
**When:** Modifying shared library code that other projects depend on.
**Triggers:** core, library, SDK, shared, package

**Required Reading:**
1. [CORE-LIBRARY.md](docs/CLAUDE/CORE-LIBRARY.md) - Public API surface
2. Locked architectural decisions (do not change)
3. Downstream consumers that would be affected

**Why:** Library changes have ripple effects. Ensure no breaking changes to public APIs.
</load_core_library_context>

<load_generation_context>
<!-- Use this for projects with content/data generation features -->
**When:** Modifying content generation, data seeding, or synthetic data creation.
**Triggers:** generate, seed, sample data, fixture data

**Required Reading:**
1. Existing generation patterns and templates
2. [APPENDIX.md](docs/CLAUDE/APPENDIX.md) - Seed data definitions
3. Domain terminology and constraints

**Why:** Ensures generated content matches domain expectations and existing patterns.
</load_generation_context>

<load_artifact_context>
**When:** Working with decision artifacts, exporting reviews, or managing formal documentation.
**Triggers:** artifact, decision record, ADR, literature review, board memo, --save, export

**Example phrases that trigger this context:**
- "Save this review as an ADR"
- "Where do decision artifacts go?"
- "Export this analysis"
- "Generate a board memo"

**Required Reading:**
1. [docs/decisions/README.md](docs/decisions/README.md) - Artifact storage and workflow
2. [.claude/skills/artifact-registry.skill.md](.claude/skills/artifact-registry.skill.md) - Template mappings

**Why:** Ensures artifacts are saved correctly with proper naming conventions and folder structure.
</load_artifact_context>

<load_reasoning_context>
**When:** Starting a new session on complex work, reviewing past decisions, understanding decision history.
**Triggers:** session recovery, why did we, decision history, reasoning review, past decisions, what assumptions

**Example phrases that trigger this context:**
- "Why did we decide to use X?"
- "What assumptions did we make about Y?"
- "Show me the decision history for authentication"
- "What were the alternatives we considered?"

**Required Reading:**
1. [docs/reasoning/README.md](docs/reasoning/README.md) - Reasoning capture system overview
2. [docs/reasoning/index.json](docs/reasoning/index.json) - Decision index for fast lookup
3. Recent entries in `docs/reasoning/YYYY-MM-DD-reasoning-log.json`

**Required Action:**
Use reasoning commands for decision intelligence:
- `/query-decisions <question>` - Natural language search of past decisions
- `/visualize-decisions` - Generate process/roles/events diagrams
- `/reconsider-decision` - Re-evaluate a past decision in sandbox
- `/analyze-impact` - Understand ripple effects before changes

**Why:** Reasoning capture provides context that formal documents miss - the "why" behind incremental decisions.
</load_reasoning_context>

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

## Decision Reasoning Capture

<reasoning_capture_directive>
**Implicit Reasoning Capture**

At the following milestones, capture decision reasoning to `docs/reasoning/`:

### After Persona Analyses
After completing any `/review-*-decision` command or individual persona analysis:
1. Extract key decision points from the analysis
2. Capture alternatives considered (from persona debates)
3. Record the consensus recommendation and confidence
4. Note unresolved tensions or assumptions
5. Write entry with `trigger.type = "persona_completion"`

### Before Commits
Before executing a git commit during implementation work:
1. Briefly capture what decision led to this change
2. Note any alternatives that were considered
3. Record assumptions that influenced the approach
4. Use `--depth light` for routine commits

### At Plan Approval
When a user approves a DEEPPLAN phase or implementation plan:
1. Capture the approved approach
2. Document why this approach over alternatives
3. Record scope decisions (what was deferred)
4. Write entry with `trigger.type = "plan_approval"`

### At Significant Decision Points
When making architectural or implementation choices that involve tradeoffs:
1. Recognize decision-making language ("Let's go with...", "I recommend...")
2. Capture the decision, rationale, and alternatives
3. Note assumptions and accepted tradeoffs
4. **Always ask about dependencies** on prior decisions

### Index Maintenance
After each capture:
1. Update `docs/reasoning/index.json` with new entry
2. Add to appropriate `byTopic` arrays
3. Update `dependencyGraph` if dependencies exist
4. Increment `totalEntries`

### When NOT to Capture
- Trivial implementation details (variable names, formatting)
- Decisions already captured in formal ADRs (avoid duplication)
- User explicitly declines capture ("skip reasoning capture")
- Pure information gathering (no decision made)
</reasoning_capture_directive>

---

**Full documentation: [docs/CLAUDE/](docs/CLAUDE/)**
