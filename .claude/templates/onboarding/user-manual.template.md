# {{PROJECT_NAME}} - Claude Code User Manual

**Generated:** {{GENERATED_DATE}}
**Framework Version:** 1.0.0

---

## Quick Start

This project uses the Claude Code Decision Framework for AI-assisted development and structured decision analysis.

### Your Project Profile

| Property | Value |
|----------|-------|
| **Project Type** | {{PROJECT_TYPE}} |
| **Tech Stack** | {{TECH_STACK}} |
| **Domain** | {{DOMAIN}} |
| **Key Entities** | {{KEY_ENTITIES}} |

---

## Available Commands

### Workflow Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/DEEPPLAN` | Structured implementation workflow | Starting multi-step features |
| `/REFOCUS` | Debug reset protocol | When stuck or going in circles |
| `/NEXTSTEPS` | Sprint planning assistant | Planning next work items |
| `/codebase-context` | Quick project summary | Session start orientation |
| `/list-personas` | Show available personas | Finding the right persona |

### Decision Review Commands

| Command | Package | Artifact Output |
|---------|---------|-----------------|
| `/review-product-decision` | Product (4 personas) | Architecture Decision Record |
| `/review-research` | Research (5 personas) | Literature Review |
| `/review-business-decision` | Advisory (7 personas) | Board Memo |
{{CUSTOM_REVIEW_COMMAND}}

### Individual Persona Commands

**Core Package:**
- `/personas/core:skeptic` - Verify claims and challenge assumptions (works across all domains)
- `/personas/core:anthropic-expert` - Claude/AI best practices and prompt optimization

**Product Package:**
- `/personas/product:architect` - Evaluate structural integrity
- `/personas/product:economist` - Analyze costs and ROI
- `/personas/product:pragmatist` - Find MVP path

**Research Package:**
- `/personas/research:librarian` - Evaluate source credibility
- `/personas/research:methodologist` - Assess research validity
- `/personas/research:critic` - Challenge hypotheses
- `/personas/research:synthesizer` - Connect patterns

**Advisory Package:**
- `/personas/advisory:cfo` - Financial analysis
- `/personas/advisory:go-to-market` - Revenue strategy
- `/personas/advisory:strategist` - Long-term positioning
- `/personas/advisory:operations` - Execution feasibility
- `/personas/advisory:product-advisor` - Product-market fit
- `/personas/advisory:counsel` - Legal and compliance

{{CUSTOM_PERSONAS_SECTION}}

---

## Workflow Examples

### Example 1: Planning a New Feature

```
User: /DEEPPLAN Add user authentication with OAuth

Claude: [Reads documentation, presents phased implementation plan]
```

### Example 2: Evaluating a Technical Decision

```
User: /review-product-decision Should we use Redis or PostgreSQL for session storage? --save session-storage-decision

Claude: [Runs 4 personas, provides weighted consensus, saves to docs/decisions/product/2026-01-04-session-storage-decision/README.md]
```

### Example 3: Quick Persona Consultation

```
User: /personas/product:architect Is this service design following SOLID principles?

Claude: [Evaluates from architectural perspective]
```

{{CUSTOM_WORKFLOW_EXAMPLES}}

---

## Documentation Structure

Your project documentation is organized in `docs/CLAUDE/`:

| Document | Purpose |
|----------|---------|
| [DEVELOPMENT.md](docs/CLAUDE/DEVELOPMENT.md) | Coding patterns, debugging, lessons learned |
| [ARCHITECTURE.md](docs/CLAUDE/ARCHITECTURE.md) | System design, schema, domain model |
| [API-REFERENCE.md](docs/CLAUDE/API-REFERENCE.md) | Endpoint specifications |
| [CHANGELOG.md](docs/CLAUDE/CHANGELOG.md) | Version history |
| [ROADMAP.md](docs/CLAUDE/ROADMAP.md) | Planned features |
| [IMPROVEMENTS.md](docs/CLAUDE/IMPROVEMENTS.md) | Improvement proposals |
| [PERSONAS.md](docs/CLAUDE/PERSONAS.md) | Persona system reference |

---

## Context Loading Triggers

Claude automatically loads relevant documentation based on your task:

| Trigger Keywords | Documentation Loaded |
|------------------|---------------------|
| schema, migration, entity | ARCHITECTURE.md |
| endpoint, controller, API | API-REFERENCE.md |
| test, spec, fixture | Test patterns |
| error, failure, bug | DEVELOPMENT.md debugging checklist |
| should we, compare, tradeoffs | Use `/review-*` commands |

---

## Next Steps

1. **Review your CLAUDE.md** - Ensure placeholders are filled in correctly
2. **Update DEVELOPMENT.md** - Add your coding patterns and lessons learned
3. **Try a decision review** - Use `/review-product-decision` on a pending decision
4. **Customize personas** - Add domain-specific personas as needed

---

## Tips for Effective Use

### Before Starting Work
- Run `/codebase-context` to orient Claude to your project
- Check `docs/CLAUDE/SESSION-STATE.json` for in-progress work

### When Making Decisions
- Use `/review-*` commands for significant choices
- Export artifacts to document decisions for future reference

### When Stuck
- Use `/REFOCUS` to reset approach systematically
- Check the debugging checklist in DEVELOPMENT.md

### Building Knowledge
- Document lessons learned in DEVELOPMENT.md
- Update CHANGELOG.md after significant changes

---

## Customization Guide

### Adding New Personas

1. Create command file: `.claude/commands/personas/{package}/{name}.md`
2. Create skill file: `.claude/skills/personas/{package}/{name}.persona.md`
3. Update the package orchestrator to include the new persona
4. Document in `docs/CLAUDE/PERSONAS.md`

See [PERSONA-PACKAGES.md](docs/CLAUDE/PERSONA-PACKAGES.md) for detailed instructions.

### Adding New Commands

1. Create markdown file in `.claude/commands/`
2. Filename becomes the command (e.g., `my-command.md` → `/my-command`)
3. Document in this user manual

See [CREATING-COMMANDS.md](.claude/CREATING-COMMANDS.md) for patterns.

---

*Generated by `/INITIALIZE_STARTER_KIT` on {{GENERATED_DATE}}*
