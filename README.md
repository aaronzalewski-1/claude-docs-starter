# Claude Code Decision Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://docs.anthropic.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Multi-perspective analysis and weighted consensus for Claude Code**

A framework for structured decision-making with [Claude Code](https://docs.anthropic.com/en/docs/claude-code), featuring 15 specialized personas, weighted consensus synthesis, and formal document generation.

## What This Does

Transform how you make decisions with Claude Code:

- **4 persona packages** covering product development, research, business advisory, and core verification
- **15 specialized personas** that analyze from distinct perspectives
- **Weighted consensus** that synthesizes multiple viewpoints based on context
- **Formal artifacts** (ADRs, Literature Reviews, Board Memos) generated automatically

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

### Context-Aware Documentation

XML-style triggers in `CLAUDE.md` load relevant documentation automatically:

```xml
<load_database_context>
When: Modifying database schema, entities, or migrations
Required Reading: ARCHITECTURE.md, existing entity patterns
</load_database_context>

<load_decision_review_context>
When: Evaluating architectural choices or technology selections
Required Action: Use /review-product-decision for multi-persona analysis
</load_decision_review_context>
```

### Workflow Commands

| Command | Purpose |
|---------|---------|
| `/INITIALIZE_STARTER_KIT` | Guided first-time setup |
| `/DEEPPLAN` | Structured implementation planning |
| `/REFOCUS` | Debug reset protocol when stuck |
| `/NEXTSTEPS` | Sprint planning assistant |
| `/list-personas` | Discover available personas |

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
│   │   └── *.md                 # Workflow commands
│   ├── skills/                  # Domain expertise backing personas
│   │   └── personas/            # Knowledge bases for each persona
│   └── templates/               # Artifact document templates
└── docs/
    ├── CLAUDE/                  # Project documentation
    │   ├── DEVELOPMENT.md       # Operational guidelines
    │   ├── ARCHITECTURE.md      # System design
    │   ├── PERSONAS.md          # Complete persona reference
    │   └── PERSONA-PACKAGES.md  # Creating custom packages
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

## Contributing

Found a pattern that works well? Improvements to personas, new domain packages, or documentation enhancements are welcome. Open a PR to share with the community.

## License

MIT License - Use freely in your projects.

---

*This framework evolved from production documentation patterns and research into structured disagreement as a decision-making methodology. The multi-persona system reflects the principle that multiple perspectives reveal blind spots that single-perspective analysis misses.*
