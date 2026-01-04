# Persona Package Architecture

**Purpose**: Guide for creating domain-specific persona packages with the three-tier architecture.

---

## Overview

Personas are organized into **packages** - domain-specific groupings of complementary personas that work together to analyze problems from multiple perspectives.

```
.claude/
├── commands/
│   ├── personas/
│   │   ├── product/           # Software Product Development package
│   │   │   ├── skeptic.md
│   │   │   ├── architect.md
│   │   │   ├── economist.md
│   │   │   └── pragmatist.md
│   │   ├── research/          # Research Analysis package
│   │   │   ├── skeptic.md
│   │   │   ├── methodologist.md
│   │   │   ├── synthesizer.md
│   │   │   ├── critic.md
│   │   │   └── librarian.md
│   │   └── advisory/          # Business Advisory package
│   │       ├── skeptic.md
│   │       ├── cfo.md
│   │       ├── go-to-market.md
│   │       ├── strategist.md
│   │       ├── operations.md
│   │       ├── product-advisor.md
│   │       └── counsel.md
│   ├── review-product-decision.md   # Product package orchestrator
│   ├── review-research.md           # Research package orchestrator
│   └── review-business-decision.md  # Advisory package orchestrator
│
└── skills/
    └── personas/
        ├── product/           # Product persona skills
        │   ├── skeptic.persona.md
        │   ├── architect.persona.md
        │   ├── economist.persona.md
        │   └── pragmatist.persona.md
        ├── research/          # Research persona skills
        │   ├── skeptic.persona.md
        │   ├── methodologist.persona.md
        │   ├── synthesizer.persona.md
        │   ├── critic.persona.md
        │   └── librarian.persona.md
        └── advisory/          # Advisory persona skills
            ├── skeptic.persona.md
            ├── cfo.persona.md
            ├── go-to-market.persona.md
            ├── strategist.persona.md
            ├── operations.persona.md
            ├── product-advisor.persona.md
            └── counsel.persona.md
```

---

## Three-Tier Architecture

Each persona package consists of three tiers:

| Tier | Location | Purpose |
|------|----------|---------|
| **Commands** | `.claude/commands/personas/<package>/` | Define persona mandate, process, output format |
| **Skills** | `.claude/skills/personas/<package>/` | Provide domain expertise frameworks |
| **Orchestrator** | `.claude/commands/review-<package>-*.md` | Run all personas, synthesize consensus |

### Tier 1: Persona Commands

Commands define **what** the persona does and **how** it operates.

**Structure:**
```markdown
---
name: persona-name
description: When to invoke this persona
persona_skill: skills/personas/<package>/persona-name.persona.md
---

# Persona Name

You are the **Persona Name** - [role description].

## Your Mandate
[Core responsibility in 3-5 words]

## Process
[Step-by-step analysis approach]

## Output Format
[Structured output template]

## Confidence Scoring
[How to rate confidence]
```

### Tier 2: Persona Skills

Skills provide **domain expertise** - the frameworks, taxonomies, and evaluation criteria.

**Structure:**
```markdown
---
name: persona-knowledge
description: Domain expertise for [Persona] persona
type: persona_skill
persona: personas/<package>/persona-name
version: 1.0.0
---

# Persona Domain Knowledge

> [One-line description of expertise area]

---

## Framework 1
[Tables, criteria, evaluation methods]

## Framework 2
[More domain knowledge]

## Confidence Calibration
[How findings affect confidence scores]
```

### Tier 3: Orchestrator

Orchestrators run all personas in a package and synthesize weighted consensus.

**Structure:**
```markdown
---
name: review-<package>-<type>
description: Multi-persona review for [domain]
---

# Review [Domain]

## Package: [Package Name]
[Table of personas with roles]

## Orchestration Process
### Phase 1: Run Each Persona
[Order and invocation instructions]

### Phase 2: Synthesize Consensus
[Weighting and synthesis approach]

## Output Format
[Combined output template with consensus table]

## Consensus Weighting
[Phase-based or context-based weights]
```

---

## Creating a New Package

### Step 1: Design Your Personas

Before writing any files, design the package:

1. **Identify the domain**: What type of analysis does this package serve?
2. **Define 3-5 personas**: Each should have a distinct perspective
3. **Ensure complementary coverage**: Personas should cover different aspects
4. **Plan the analysis flow**: Which persona should run first/last?

**Design Template:**

| Persona | Role | Focus | Runs |
|---------|------|-------|------|
| [Name] | [Short role] | [What they analyze] | [Order] |

### Step 2: Create Folder Structure

```bash
# Create command folders
mkdir -p .claude/commands/personas/<package-name>

# Create skill folders
mkdir -p .claude/skills/personas/<package-name>
```

### Step 3: Create Persona Skills (Domain Expertise First)

Create skills before commands - they define the domain knowledge the commands reference.

**Template: `.claude/skills/personas/<package>/<persona>.persona.md`**

```markdown
---
name: <persona>-knowledge
description: Domain expertise for <Persona> persona - [key areas]
type: persona_skill
persona: personas/<package>/<persona>
version: 1.0.0
---

# <Persona> Domain Knowledge

> [One-line expertise description]

---

## [Framework Category 1]

### [Framework Name]

| Criterion | Description | Application |
|-----------|-------------|-------------|
| [Item] | [What it means] | [How to use] |

[Additional frameworks, tables, evaluation criteria]

---

## Confidence Calibration

### [Quality/Strength] Indicators

| Indicator | Confidence Boost |
|-----------|------------------|
| [Positive signal] | +0.XX |

### [Concern/Weakness] Indicators

| Concern | Confidence Penalty |
|---------|-------------------|
| [Negative signal] | -0.XX |
```

### Step 4: Create Persona Commands

**Template: `.claude/commands/personas/<package>/<persona>.md`**

```markdown
---
name: <persona>
description: [When to use this persona]. Use when [specific triggers].
persona_skill: skills/personas/<package>/<persona>.persona.md
---

# <Persona> Persona

You are the **<Persona>** - [role description]. Your role is to [core responsibility].

## Your Mandate

**[3-5 word imperative]**

You exist to prevent:
- [Problem 1 this persona catches]
- [Problem 2 this persona catches]
- [Problem 3 this persona catches]

## [Input] Under Review

$ARGUMENTS

## Quick Mode

For simple evaluations, skip to **[Key Section]** + **Recommendation** only.

---

## Your Process

### Step 1: [First Analysis Step]
[What to do and why]

### Step 2: [Second Analysis Step]
[What to do and why]

[Continue with 4-6 steps total]

---

## Output Format

```markdown
## <Persona> Analysis

### [Input] Under Review
[Restate clearly]

### [Analysis Section 1]
[Structured findings]

### [Analysis Section 2]
[Structured findings]

### Recommendation
[Clear recommendation]

### Verdict
[Summary]

**Confidence: X.X**
```

## Confidence Scoring

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | [High confidence criteria] |
| 0.7-0.8 | [Moderate confidence criteria] |
| 0.5-0.6 | [Low confidence criteria] |
| < 0.5 | [Insufficient criteria] |

## Domain Expertise

Reference your PersonaSkill (`skills/personas/<package>/<persona>.persona.md`) for:
- [Framework 1]
- [Framework 2]
- [Framework 3]

## Potential Conflicts

| Conflict With | Typical Tension | Resolution |
|---------------|-----------------|------------|
| **[Other Persona]** | [What they disagree about] | [How to resolve] |

---

## Handoff to Analysis

After assessment, offer relevant next steps:

| If Assessment Shows | Recommend |
|--------------------|-----------|
| [Condition 1] | → **[Other Persona]** for [reason] |
| [Condition 2] | → **[Other Persona]** for [reason] |
```

### Step 5: Create Orchestrator

**Template: `.claude/commands/review-<package>-<type>.md`**

```markdown
---
name: review-<package>-<type>
description: Multi-persona review of [domain]. Use when [triggers]. Triggers on phrases like "[phrase 1]", "[phrase 2]", or the explicit /review-<package>-<type> command.
---

# Review [Domain]

Evaluate [input type] through [N] specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-<package>-<type> <input description>
```

Also triggers on natural language requests to [action verbs].

## Package: [Package Name]

This orchestrator invokes [N] analytical personas from the **[Package]** package:

| Persona | Role | Focus |
|---------|------|-------|
| **[Persona 1]** | [Short role] | [Focus area] |
| **[Persona 2]** | [Short role] | [Focus area] |
| **[Persona 3]** | [Short role] | [Focus area] |
| **[Persona 4]** | [Short role] | [Focus area] |

Each persona has:
- A **command** (`/personas/<package>:<persona>`, etc.) for individual invocation
- A **PersonaSkill** with domain expertise frameworks

## Orchestration Process

### Phase 1: Run Each Persona

For the [input] provided, run each persona analysis **in sequence**:

1. **[Persona 1] Analysis** (`/personas/<package>:<persona1>`)
   - [What they evaluate]

2. **[Persona 2] Analysis** (`/personas/<package>:<persona2>`)
   - [What they evaluate]

[Continue for all personas]

### Phase 2: Synthesize Consensus

After all personas have analyzed, produce a weighted synthesis.

## Output Format

```markdown
## [Input Type] Under Review
[Restate clearly]

---

## [Persona 1] Analysis
[Analysis content]
**Confidence: X.X**

---

[Repeat for each persona]

---

## Weighted Consensus

| Persona | Confidence | Weight | Weighted Score |
|---------|------------|--------|----------------|
| [Persona 1] | X.X | 0.XX | X.XX |
| [Persona 2] | X.X | 0.XX | X.XX |
| [Persona 3] | X.X | 0.XX | X.XX |
| [Persona 4] | X.X | 0.XX | X.XX |
| **Weighted Average** | | | **X.XX** |

### Synthesis
[Integrated analysis]

### Key Findings
[What evidence supports]

### Key Concerns
[What remains problematic]

### Recommendation
[Clear conclusion with confidence]

### Next Steps
[Follow-up actions]
```

## Consensus Weighting

Default weights vary by [context/phase]. Adjust based on your context:

| [Context] | [Persona 1] | [Persona 2] | [Persona 3] | [Persona 4] |
|-----------|-------------|-------------|-------------|-------------|
| **[Context A]** | **0.XX** | 0.XX | 0.XX | 0.XX |
| **[Context B]** | 0.XX | **0.XX** | 0.XX | 0.XX |

[Explain when each context applies]

## When Personas Disagree

If confidence-weighted scores diverge by >0.3, explicitly surface the conflict:

> **Conflict:** [Persona A] (0.X) and [Persona B] (0.X) disagree.
> - [Persona A] flags [concern]
> - [Persona B] sees [opportunity]
>
> **Resolution depends on:** [Key question]

## Individual Persona Usage

You can invoke personas individually for focused analysis:

```
/personas/<package>:<persona1> [input]
/personas/<package>:<persona2> [input]
```

## Related Packages

| Package | Orchestrator | Use For |
|---------|--------------|---------|
| **[Package 1]** | `/review-<package1>-<type>` | [Use case] |
| **[Package 2]** | `/review-<package2>-<type>` | [Use case] |
```

---

## Existing Packages

### Product Package

**Purpose**: Software product development decisions

| Persona | Role | Focus |
|---------|------|-------|
| Skeptic | Fact-checker | Verify claims, check sources |
| Architect | Structure guardian | SOLID principles, patterns, coupling |
| Economist | Cost analyst | ROI, TCO, resource efficiency |
| Pragmatist | MVP advocate | Simplicity, deferral, reversibility |

**Orchestrator**: `/review-product-decision`

**Invocation**: `/personas/product:skeptic`, `/personas/product:architect`, etc.

### Research Package

**Purpose**: Research analysis and source evaluation

| Persona | Role | Focus |
|---------|------|-------|
| Skeptic | Truth guardian | Citation verification, data integrity, claim validation |
| Librarian | Source curator | Credibility, citations, evidence hierarchy |
| Methodologist | Validity guardian | Research design, methodology, statistics |
| Critic | Devil's advocate | Counterarguments, alternative explanations |
| Synthesizer | Pattern finder | Integration, themes, relationships |

**Orchestrator**: `/review-research`

**Invocation**: `/personas/research:skeptic`, `/personas/research:librarian`, etc.

### Advisory Package

**Purpose**: Business advisory for founders and decision makers

| Persona | Role | Focus |
|---------|------|-------|
| Skeptic | Truth verifier | Business claim verification, assumption testing |
| CFO | Financial guardian | Runway, unit economics, fundraising |
| Go-to-Market | Revenue champion | Acquisition, retention, pricing |
| Strategist | Vision keeper | Positioning, moats, exit planning |
| Operations | Execution realist | Capacity, process, scalability |
| Product Advisor | User advocate | PMF, prioritization, roadmap |
| Counsel | Risk manager | Legal, compliance, IP, contracts |

**Orchestrator**: `/review-business-decision`

**Invocation**: `/personas/advisory:skeptic`, `/personas/advisory:cfo`, etc.

**Unique Features**:
- **Two-dimensional weighting**: Stage (Pre-seed → Exit) × Focus (Strategy, Funding, Growth, etc.)
- **Exit mode specialization**: Different frameworks for Acquisition vs IPO vs Acqui-hire
- **Seven personas** providing comprehensive business advisory perspective

---

## Package Design Principles

### 1. Complementary Perspectives

Each persona should analyze from a different angle. Avoid overlap.

**Good**: Skeptic (truth), Architect (structure), Economist (cost), Pragmatist (scope)

**Bad**: Skeptic (truth), Verifier (truth), Validator (truth), Checker (truth)

### 2. Constructive Tension

Personas should sometimes disagree. This surfaces trade-offs.

**Example tensions:**
- Architect wants clean design vs. Pragmatist wants quick delivery
- Economist wants cost savings vs. Skeptic questions vendor claims

### 3. Clear Mandates

Each persona has a 3-5 word imperative that captures their core focus.

**Examples:**
- Skeptic: "Verify before trusting"
- Architect: "Structure enables evolution"
- Economist: "Every choice has cost"
- Pragmatist: "Ship value, defer complexity"

### 4. Actionable Output

Personas provide recommendations, not just analysis. Each analysis ends with a clear verdict and confidence score.

### 5. Domain Expertise in Skills

Commands define process; skills define knowledge. Keep domain frameworks in skills so they can be reused and updated independently.

---

## Extending Existing Packages

### Adding a Persona to a Package

1. Create the skill file: `.claude/skills/personas/<package>/<new-persona>.persona.md`
2. Create the command file: `.claude/commands/personas/<package>/<new-persona>.md`
3. Update the orchestrator to include the new persona
4. Define how the new persona's weight factors into consensus

### Creating Package Variants

For specialized contexts, create variant orchestrators:

```
review-product-decision.md      # General product decisions
review-product-architecture.md  # Architecture-focused (higher Architect weight)
review-product-cost.md          # Cost-focused (higher Economist weight)
```

---

## Artifact Production

Each package can produce formal documents from multi-persona analyses.

### Package Artifacts

| Package | Artifact | Command | Template |
|---------|----------|---------|----------|
| **Product** | Architecture Decision Record | `/export-artifact adr <name>` | `.claude/templates/product/adr.template.md` |
| **Research** | Literature Review | `/export-artifact literature-review <name>` | `.claude/templates/research/literature-review.template.md` |
| **Advisory** | Board Memo | `/export-artifact board-memo <name>` | `.claude/templates/advisory/board-memo.template.md` |

### Persona-to-Artifact Mapping

Each artifact type maps persona outputs to document sections:

**ADR (Product Package):**
- Context ← Decision statement
- Decision ← Consensus recommendation
- Consequences ← Benefits and risks from all personas
- Alternatives ← Options discussed
- Analysis Summary ← Weighted consensus table

**Literature Review (Research Package):**
- Executive Summary ← Consensus synthesis
- Sources Evaluated ← Librarian source credibility table
- Methodology Assessment ← Methodologist findings
- Claim Verification ← Skeptic analysis
- Themes and Patterns ← Synthesizer integration

**Board Memo (Advisory Package):**
- Executive Summary ← Consensus synthesis
- Advisory Perspectives ← Summary from each of 7 personas
- Consensus Table ← Full weighted scores
- Key Risks ← Tensions and conflicts
- Required Actions ← Critical actions

### Storage Convention

Generated artifacts are stored in:

```
docs/decisions/<package>/YYYY-MM-DD-<artifact-name>/
├── README.md          # The generated artifact
└── analysis.json      # Structured analysis data (optional)
```

See `.claude/skills/artifact-registry.skill.md` for full artifact definitions.

---

## Troubleshooting

### Persona Not Invoked

- Check command frontmatter has correct `name` field
- Verify skill reference path is correct
- Ensure file is in correct folder

### Skill Not Loading

- Check skill frontmatter has `type: persona_skill`
- Verify `persona` field matches command location
- Check file extension is `.persona.md`

### Consensus Weights Don't Sum to 1.0

Weights should sum to 1.0 for each context/phase. If they don't, the weighted average calculation will be skewed.

### Personas Producing Inconsistent Output

Ensure each persona command has the same output format structure. The orchestrator expects consistent sections to synthesize.
