# Creating Custom Skills

Skills are domain-specific knowledge files that Claude Code can invoke when working on your project. Unlike slash commands (which trigger specific workflows), skills provide **persistent context** about your project's architecture, patterns, and constraints.

## Skills vs Commands

| Feature | Skills | Commands |
|---------|--------|----------|
| **Purpose** | Domain knowledge & constraints | Workflow automation |
| **Activation** | Keyword triggers or explicit invocation | `/command` syntax |
| **Content** | Architecture, locked decisions, patterns | Step-by-step instructions |
| **Use case** | "What to know" | "What to do" |

## When to Use Skills

Create a skill when you need Claude to:

- **Remember locked decisions** - Prevent re-litigation of settled architectural choices
- **Follow mandatory reading** - Ensure docs are read before certain task types
- **Apply domain patterns** - Enforce project-specific conventions consistently
- **Understand constraints** - Know what NOT to recommend

## Quick Start

1. Copy the template from `.claude/skills/project-name.skill.md.template`
2. Rename to match your project: `myproject.skill.md`
3. Fill in the placeholders with your project-specific values
4. Delete the instruction comments

## File Structure

```
.claude/
└── skills/
    ├── myproject.skill.md        # Your project skill
    └── project-name.skill.md.template  # Template (for reference)
```

**Naming Convention:** `{name}.skill.md` - The `.skill.md` suffix is required.

## Skill Anatomy

### Frontmatter (Required)

```yaml
---
name: myproject
description: >
  Development work on MyProject.
  MUST use this skill for: database changes, API work, UI components.
  Triggers on keywords: MyProject, schema, endpoint, component.
  This skill contains locked architectural decisions that MUST NOT be re-litigated.
---
```

The `description` field is critical - it tells Claude:
- **When to activate** the skill (triggers)
- **What it covers** (scope)
- **Key constraints** (locked decisions exist)

### Core Sections

| Section | Purpose |
|---------|---------|
| **Overview** | Brief project description |
| **Mandatory Pre-Work** | Required reading before task types |
| **Locked Architectural Decisions** | Settled decisions that must not be questioned |
| **Critical Patterns** | Key patterns and anti-patterns |
| **Technology Stack** | Tech choices and versions |
| **Project Structure** | Directory layout |
| **Quick Commands** | Build, test, migration commands |
| **Resources** | Links to reference documents |

## The "Locked Decisions" Pattern

This is the most valuable section of a skill. It prevents Claude from:

- Repeatedly suggesting alternatives to settled decisions
- Questioning architectural choices that have already been debated
- Wasting time re-litigating past decisions

### Format

```markdown
## Locked Architectural Decisions

These decisions have been made and MUST NOT be re-litigated:

### 1. Single-Tenant Deployment

Each deployment serves ONE tenant. This is intentional for data isolation.

Do NOT recommend:
- Multi-tenant database schemas
- Tenant selection APIs
- Shared connection pools
```

### Writing Effective Locked Decisions

1. **State the decision clearly** - What IS the approach?
2. **Explain why briefly** - Just enough context
3. **List what NOT to recommend** - Explicit anti-patterns
4. **Use strong language** - "MUST NOT", "Do NOT recommend"

## Tips for Effective Skills

### 1. Be Explicit About Triggers

```yaml
description: >
  MUST use this skill for: database migrations, EF Core changes,
  API endpoint modifications, authentication changes.
  Triggers on keywords: schema, migration, DbContext, endpoint, auth.
```

### 2. Link to Actual Documentation

Don't duplicate content - link to your project docs:

```markdown
## Mandatory Pre-Work

| Task Type | Required Reading |
|-----------|------------------|
| Database changes | `docs/CLAUDE/ARCHITECTURE.md` |
| API work | `docs/CLAUDE/API-REFERENCE.md` |
```

### 3. Include Domain-Specific Patterns

Add patterns unique to your project:

```markdown
## Critical Patterns

### Before Modifying the Payment Service

1. Read `docs/payment-integration.md` FIRST
2. Never store raw card numbers
3. All amounts use cents (integer), never decimals
```

### 4. Document Anti-Patterns

What should Claude avoid?

```markdown
### What NOT to Do

- Don't add caching without explicit request
- Don't refactor unrelated code
- Don't suggest microservices for single-deployment apps
```

## Example: Minimal Skill

For simpler projects, a minimal skill might be:

```markdown
---
name: myapp
description: >
  MyApp development. Contains locked decisions about database and API design.
---

# MyApp Development

## Locked Decisions

### PostgreSQL with Prisma

We use PostgreSQL with Prisma ORM. Do NOT recommend:
- Switching to MongoDB or other NoSQL
- Using raw SQL instead of Prisma
- Adding a second database

### REST API Design

All endpoints follow REST conventions. Do NOT recommend:
- GraphQL migration
- RPC-style endpoints

## Quick Commands

```bash
npm run dev      # Start development server
npm run test     # Run tests
npm run db:push  # Apply schema changes
```
```

## Debugging Skills

If your skill isn't being applied:

1. **Check the filename** - Must end in `.skill.md`
2. **Check the location** - Must be in `.claude/skills/`
3. **Check the frontmatter** - Valid YAML with `name` and `description`
4. **Check triggers** - Are keywords specific enough?

---

## Persona Skills

Persona skills are a special type of skill that provide domain expertise for analytical personas. They differ from project skills in purpose and structure.

### Persona Skill vs Project Skill

| Aspect | Project Skill | Persona Skill |
|--------|---------------|---------------|
| **Purpose** | Project-specific context | Domain expertise frameworks |
| **Content** | Locked decisions, patterns | Evaluation criteria, metrics |
| **Triggered by** | Task keywords | Persona command |
| **Location** | `.claude/skills/` | `.claude/skills/personas/` |
| **Naming** | `{project}.skill.md` | `{persona}.persona.md` |

### Persona Skill Structure

```yaml
---
name: persona-name-knowledge
description: Domain expertise for Persona Name - frameworks and evaluation criteria
type: persona_skill
persona: personas/persona-name
version: 1.0.0
---
```

### Content Sections

A persona skill typically includes:

1. **Frameworks** - Decision matrices, evaluation criteria
2. **Categories/Tiers** - Classification systems
3. **Metrics** - Quantitative thresholds and benchmarks
4. **Anti-patterns** - What to avoid and why
5. **Confidence Calibration** - How to score analysis certainty

### Example: Minimal Persona Skill

```markdown
---
name: reviewer-knowledge
description: Domain expertise for Code Reviewer persona
type: persona_skill
persona: personas/reviewer
version: 1.0.0
---

# Reviewer Domain Knowledge

## Code Quality Metrics

| Metric | Good | Acceptable | Concerning |
|--------|------|------------|------------|
| Cyclomatic complexity | < 10 | 10-20 | > 20 |
| Function length | < 30 lines | 30-50 | > 50 |
| Parameter count | < 4 | 4-6 | > 6 |

## Common Anti-patterns

| Pattern | Why It's Bad | Alternative |
|---------|--------------|-------------|
| God class | Too many responsibilities | Extract classes |
| Magic numbers | Hard to understand | Use named constants |

## Confidence Calibration

| Evidence | Modifier |
|----------|----------|
| Follows team conventions | +0.1 |
| Has test coverage | +0.1 |
| Introduces new pattern | -0.05 |
```

### Creating a New Persona

To add a new persona:

1. Create the persona skill in `.claude/skills/personas/{name}.persona.md`
2. Create the persona command in `.claude/commands/personas/{name}.md`
3. Reference the skill in the command's frontmatter
4. Optionally add to `/review-decision` orchestrator

---

## Learn More

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Creating Commands](CREATING-COMMANDS.md) - For workflow automation
- [Personas Documentation](../docs/CLAUDE/PERSONAS.md) - Full persona system guide
- [Project Documentation](../docs/CLAUDE/) - Your project-specific docs
