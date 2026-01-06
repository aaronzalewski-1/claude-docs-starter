# Claude Code Decision Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://docs.anthropic.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Multi-perspective analysis and weighted consensus for Claude Code**

A framework for structured decision-making with [Claude Code](https://docs.anthropic.com/en/docs/claude-code), featuring 15 specialized personas, weighted consensus synthesis, formal document generation, context management, and living documentation.

## What This Does

Transform how you work with Claude Code:

- **15 specialized personas** across 4 packages that analyze from distinct perspectives
- **Weighted consensus** that synthesizes viewpoints based on project phase and context
- **Formal artifacts** (ADRs, Literature Reviews, Board Memos) generated automatically
- **Context management** that keeps Claude focused across complex, multi-session work
- **Living documentation** designed to evolve and accumulate institutional knowledge

## Quick Example

```
/review-product-decision Should we use Redis for caching? --save redis-decision
```

This triggers 4 personas (Skeptic, Architect, Economist, Pragmatist), produces a weighted consensus, and saves an Architecture Decision Record to `docs/decisions/product/2026-01-05-redis-decision/README.md`.

## Persona Packages

| Package | Orchestrator | Personas | Use For |
|---------|--------------|----------|---------|
| **Core** | Individual invocation | Skeptic, Anthropic Expert | Verification across domains, Claude optimization |
| **Product** | `/review-product-decision` | + Architect, Economist, Pragmatist | Architecture choices, technology selection, build vs buy |
| **Research** | `/review-research` | + Librarian, Methodologist, Critic, Synthesizer | Source evaluation, claim verification, literature synthesis |
| **Advisory** | `/review-business-decision` | + CFO, GTM, Strategist, Ops, Product, Counsel | Strategic decisions, funding, growth, partnerships |

Each orchestrator runs the Core Skeptic plus domain-specific personas, then synthesizes weighted consensus that varies by project phase and decision type.

## Installation

```
/INITIALIZE_STARTER_KIT
```

8-phase guided setup:
1. Analyzes your existing project files
2. Detects your domain and tech stack
3. Fills in documentation placeholders
4. Optionally creates custom personas for your domain
5. Generates a personalized user manual

**Manual setup:** Copy `CLAUDE.md`, `docs/CLAUDE/`, and `.claude/` to your project root, then replace `{{PLACEHOLDER}}` markers.

## Key Features

### Multi-Persona Decision Analysis

Instead of single-perspective answers, get analysis from multiple complementary viewpoints:

```
/review-product-decision Should we add a caching layer?
```

**Output includes:**
- Individual persona analyses with confidence scores
- Weighted consensus table
- Key tensions between personas
- Final recommendation with rationale

### Formal Artifact Generation

Save analysis to shareable documents:

| Package | Artifact | Command |
|---------|----------|---------|
| **Product** | Architecture Decision Record | `/review-product-decision <decision> --save <name>` |
| **Research** | Literature Review | `/review-research <question> --save <name>` |
| **Advisory** | Board Memo | `/review-business-decision <decision> --save <name>` |

Generated markdown converts to PDF/DOCX via pandoc.

### Individual Persona Consultation

Invoke any persona directly for focused analysis:

```
/personas/core:skeptic Is this claim about PostgreSQL performance actually verified?
/personas/product:architect Evaluate this service layer design for SOLID compliance
/personas/advisory:cfo What's our runway if we hire 5 engineers?
/personas/research:librarian Evaluate these sources on climate change
```

### Context and Focus Management

XML-style triggers in `CLAUDE.md` automatically load relevant documentation based on what you're working on:

```xml
<load_database_context>
When: Modifying database schema, entities, or migrations
Triggers: schema, migration, entity, DbContext
Required Reading: ARCHITECTURE.md, existing entity patterns
</load_database_context>

<load_debugging_context>
When: Investigating failures, unexpected behavior
Triggers: error, failure, bug, broken, not working
Required Reading: DEVELOPMENT.md debugging checklist
</load_debugging_context>
```

When you say "add a migration," the database context loads. When you say "the build is broken," the debugging context loads. Claude reads what it needs before acting.

**Workflow commands** handle common challenges:

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/INITIALIZE_STARTER_KIT` | 8-phase guided setup | First-time installation |
| `/DEEPPLAN` | Structured implementation planning | Multi-step features needing phased execution |
| `/REFOCUS` | Debug reset protocol | When stuck or going in circles |
| `/NEXTSTEPS` | Sprint planning assistant | Planning what to work on next |
| `/codebase-context` | Quick project summary | Session start orientation |
| `/list-personas` | Discover available personas | Finding the right perspective |

`/REFOCUS` is particularly valuable—when debugging spirals or Claude keeps suggesting failed approaches, it forces a structured reset: What was the original objective? What approaches failed? What assumptions need questioning?

### Living Documentation

The framework is designed around documents that evolve, not static templates that rot.

**Lessons learned accumulate** in `DEVELOPMENT.md`:

```markdown
**Case Study: Migration Created But Not Applied**

**The Mistake:** Created migration file, committed with message implying
table existed, but never applied the migration.

**General Principles Derived:**
1. Migration Creation ≠ Migration Application
2. Verify database state, not just build state
```

Each mistake becomes guidance that persists beyond individual sessions.

**Documentation stays current** through focused files:

| Document | What Evolves |
|----------|--------------|
| `DEVELOPMENT.md` | Coding patterns, debugging checklists, lessons learned |
| `ARCHITECTURE.md` | System design, schema, domain model |
| `CHANGELOG.md` | Version history, migration notes |
| `IMPROVEMENTS.md` | Improvement proposals, implementation status |

**Locked decisions** prevent re-litigation of settled architectural choices:

```markdown
## Locked Architectural Decisions

### 1. Single-Tenant Deployment Model
Do NOT recommend: multi-tenant designs, tenant selection APIs
```

Claude respects these boundaries while remaining flexible on living decisions.

## Documentation Structure

```
your-project/
├── CLAUDE.md                    # Entry point with context triggers
├── .claude/
│   ├── commands/                # Slash commands and orchestrators
│   │   ├── personas/            # 15 individual persona commands
│   │   │   ├── core/            # Skeptic, Anthropic Expert
│   │   │   ├── product/         # Architect, Economist, Pragmatist
│   │   │   ├── research/        # Librarian, Methodologist, Critic, Synthesizer
│   │   │   └── advisory/        # CFO, GTM, Strategist, Ops, Product, Counsel
│   │   ├── review-*.md          # Package orchestrators
│   │   └── *.md                 # Workflow commands (DEEPPLAN, REFOCUS, etc.)
│   ├── skills/                  # Domain expertise backing personas
│   │   └── personas/            # Knowledge bases for each persona
│   └── templates/               # Artifact document templates
└── docs/
    ├── CLAUDE/                  # Project documentation (living documents)
    │   ├── DEVELOPMENT.md       # Operational guidelines + lessons learned
    │   ├── ARCHITECTURE.md      # System design, schema, domain model
    │   ├── CHANGELOG.md         # Version history
    │   ├── IMPROVEMENTS.md      # Improvement proposals
    │   ├── PERSONAS.md          # Complete persona reference
    │   ├── PERSONA-PACKAGES.md  # Creating custom packages
    │   └── SESSION-STATE.json   # Multi-session work tracking
    └── decisions/               # Generated artifacts
        ├── product/             # ADRs
        ├── research/            # Literature reviews
        └── advisory/            # Board memos
```

## Extensibility

### Create Custom Persona Packages

The three-tier architecture separates concerns:

| Tier | Location | Purpose |
|------|----------|---------|
| **Commands** | `.claude/commands/personas/<package>/` | Define process and output format |
| **Skills** | `.claude/skills/personas/<package>/` | Provide domain expertise |
| **Orchestrator** | `.claude/commands/review-<package>-*.md` | Coordinate and synthesize |

See [PERSONA-PACKAGES.md](docs/CLAUDE/PERSONA-PACKAGES.md) for step-by-step guidance.

### Domain-Specific Personas

`/INITIALIZE_STARTER_KIT` suggests custom personas based on your domain:

| Domain | Suggested Personas |
|--------|-------------------|
| **Healthcare** | Compliance Officer, Clinical Advisor, Patient Advocate |
| **Fintech** | Risk Analyst, Security Auditor, Fraud Specialist |
| **E-commerce** | Customer Experience, Inventory, Payment Security |
| **SaaS B2B** | Customer Success, Enterprise Sales, Integration Architect |

## Who This Is For

| Audience | What You Get |
|----------|--------------|
| **Teams using Claude Code** | Structured process for architectural/business decisions |
| **Technical Leaders** | ADR generation, documented decision rationale |
| **Founders/Executives** | Multi-perspective business advisory (7 personas) |
| **Researchers** | Literature review synthesis with source evaluation |
| **Framework Builders** | Extensible architecture for custom persona packages |

## Tips for Success

1. **Run reviews without `--save` first** - See if the analysis is useful before creating artifacts
2. **Trust the disagreements** - Persona conflicts reveal important tradeoffs
3. **Use individual personas for quick consultations** - Full reviews aren't always needed
4. **Export artifacts for decisions that matter** - Creates institutional memory
5. **Customize weights for your phase** - Pre-validation projects weight Pragmatist higher; scale-ready projects weight Architect higher
6. **Capture lessons learned** - When something goes wrong, add a case study to DEVELOPMENT.md
7. **Use `/REFOCUS` when stuck** - Don't let debugging sessions spiral; reset systematically
8. **Keep documentation current** - The framework works best when docs evolve with your project

## Contributing

Found a pattern that works well? Improvements to personas, new domain packages, or documentation enhancements are welcome. Open a PR to share with the community.

## License

MIT License - Use freely in your projects.

---

*This framework evolved from production documentation patterns and research into structured disagreement as a decision-making methodology. The multi-persona system reflects the principle that multiple perspectives reveal blind spots that single-perspective analysis misses.*
