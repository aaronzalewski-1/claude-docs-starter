# Persona System

**Multi-perspective analysis through domain-specific persona packages.**

The persona system provides structured analysis through specialized analytical lenses organized into **packages**. Each package contains complementary personas for a specific domain. Personas examine inputs from their unique perspective, then orchestrators synthesize weighted consensus.

---

## Overview

### Package Architecture

Personas are organized into domain-specific packages:

```
┌─────────────────────────────────────────────────────────────┐
│  PACKAGES                                                    │
│  product/ - Software development decisions                   │
│  research/ - Research analysis and source evaluation         │
│  advisory/ - Business strategy and founder guidance          │
├─────────────────────────────────────────────────────────────┤
│  ORCHESTRATORS                                               │
│  /review-product-decision - Runs all product personas        │
│  /review-research - Runs all research personas               │
│  /review-business-decision - Runs all advisory personas      │
├─────────────────────────────────────────────────────────────┤
│  PERSONA COMMANDS                                            │
│  /personas/product:skeptic, /personas/research:librarian     │
│  /personas/advisory:cfo, /personas/advisory:strategist       │
│  Individual analytical lenses with step-by-step processes    │
├─────────────────────────────────────────────────────────────┤
│  PERSONA SKILLS                                              │
│  Domain expertise: frameworks, metrics, evaluation criteria  │
└─────────────────────────────────────────────────────────────┘
```

### Three-Tier Architecture

Each package consists of three tiers:

| Tier | Purpose | Example |
|------|---------|---------|
| **Orchestrator** | Run all personas in package, weight and synthesize | `/review-product-decision <decision>` |
| **Persona Command** | Single analytical perspective | `/personas/product:skeptic <decision>` |
| **Persona Skill** | Domain expertise backing the persona | Auto-loaded by command |

### Why This Architecture?

**Separation of concerns:**
- Commands define *what* to do (process, output format)
- Skills provide *knowledge* (frameworks, metrics, thresholds)
- Orchestrators handle *coordination* (sequencing, weighting)

**Domain organization:**
- Related personas grouped into packages
- Each package optimized for specific analysis types
- Packages can be extended or new ones created

**Reusability:**
- Persona skills can be referenced by multiple commands
- New personas can be added without modifying orchestrators
- Domain expertise maintained in one place

---

## Product Package

**Purpose**: Software product development decisions - architecture, technology selection, cost analysis, scope management.

**Orchestrator**: `/review-product-decision`

### Skeptic

**Mandate:** *Trust nothing. Verify everything.*

**Role:** Fact-checker and assumption challenger.

**Use when you need:**
- Technical claims verified against documentation
- Assumptions identified and challenged
- Sources of truth cited
- Unverified statements flagged

**Key Frameworks (from PersonaSkill):**
- Source credibility hierarchy (Tier 1-4)
- Claim categorization (Factual, Performance, Best Practice, Predictive)
- Technology lifecycle awareness
- Verification workflows

**Invocation:**
```
/personas/product:skeptic Should we use Redis for caching?
```

---

### Architect

**Mandate:** *Design for change. Isolate what varies.*

**Role:** Guardian of structural integrity and pattern consistency.

**Use when you need:**
- SOLID principle evaluation
- Pattern consistency check
- Coupling and dependency analysis
- Testability assessment

**Key Frameworks (from PersonaSkill):**
- SOLID principles with detection questions
- Pattern catalog (creational, structural, behavioral)
- Coupling metrics (Ca, Ce, Instability)
- Clean Architecture layer rules
- Code smell detection

**Invocation:**
```
/personas/product:architect Evaluate this service layer design
```

---

### Economist

**Mandate:** *Every choice has a cost. Make them visible.*

**Role:** Cost analyst and ROI evaluator.

**Use when you need:**
- Cost comparison across options
- Hidden cost identification
- ROI and payback period calculation
- Scale economics projection
- Build vs buy analysis

**Key Frameworks (from PersonaSkill):**
- Cost categories (direct, development, operational, maintenance)
- Developer time estimation models
- TCO template
- Scale economics (linear, sub-linear, super-linear)
- Build vs buy calculator

**Invocation:**
```
/personas/product:economist Compare cloud vs self-hosted database costs
```

---

### Pragmatist

**Mandate:** *Ship to learn. Perfect later.*

**Role:** MVP advocate and complexity challenger.

**Use when you need:**
- Complexity justification
- MVP path identification
- Deferral opportunities
- "Do we really need this?" analysis

**Key Frameworks (from PersonaSkill):**
- MVP criteria matrix
- Complexity justification framework
- Deferral decision tree
- Reversibility assessment
- Simplification strategies

**Invocation:**
```
/personas/product:pragmatist Is this caching layer worth building now?
```

---

## Research Package

**Purpose**: Research analysis - evaluating sources, assessing methodology, challenging claims, synthesizing findings.

**Orchestrator**: `/review-research`

### Skeptic

**Mandate:** *Trust nothing. Verify everything.*

**Role:** Truth guardian and claim validator.

**Use when you need:**
- Citations verified against actual sources
- Data integrity assessment
- Misrepresentation pattern detection
- Primary source tracing

**Key Frameworks (from PersonaSkill):**
- Citation verification frameworks
- Statistical red flag detection
- Data integrity assessment
- Common misrepresentation patterns
- Primary source tracing methods

**Invocation:**
```
/personas/research:skeptic Verify the citations in this paper support its claims
```

---

### Librarian

**Mandate:** *Primary sources. Credible citations.*

**Role:** Source curator and evidence evaluator.

**Use when you need:**
- Source credibility assessment
- Citation chain tracing
- Evidence hierarchy evaluation
- Better source identification

**Key Frameworks (from PersonaSkill):**
- Source type classification (Primary, Secondary, Tertiary, Popular)
- CRAAP test (Currency, Relevance, Authority, Accuracy, Purpose)
- Citation chain analysis
- Evidence hierarchy (meta-analyses → RCTs → cohort → case studies → opinion)

**Invocation:**
```
/personas/research:librarian Evaluate these sources on climate change
```

---

### Methodologist

**Mandate:** *Valid methods. Reproducible results.*

**Role:** Research design and validity guardian.

**Use when you need:**
- Research design evaluation
- Internal/external validity assessment
- Statistical approach review
- Bias detection

**Key Frameworks (from PersonaSkill):**
- Research design classification (quantitative, qualitative, mixed)
- Internal validity threats (history, maturation, selection, etc.)
- External validity dimensions (population, ecological, temporal)
- Statistical test selection criteria
- Quality assessment rubrics

**Invocation:**
```
/personas/research:methodologist Assess this study's methodology
```

---

### Critic

**Mandate:** *Steel-man, then challenge.*

**Role:** Devil's advocate and assumption challenger.

**Use when you need:**
- Counterargument generation
- Alternative explanations
- Assumption testing
- Claim stress-testing

**Key Frameworks (from PersonaSkill):**
- Toulmin argumentation model
- Logical fallacy detection
- Alternative explanation types (confounding, reverse causation, third variable)
- Steel-manning techniques
- Robustness testing

**Invocation:**
```
/personas/research:critic Challenge this hypothesis
```

---

### Synthesizer

**Mandate:** *Connect the dots. Find the patterns.*

**Role:** Pattern finder and knowledge integrator.

**Use when you need:**
- Theme identification across sources
- Relationship mapping between concepts
- Knowledge integration
- Gap identification

**Key Frameworks (from PersonaSkill):**
- Synthesis methodologies (narrative, thematic, framework, meta-ethnography)
- Theme identification (inductive, deductive, abductive)
- Relationship mapping (supports, contradicts, correlates, enables)
- Integration strategies (chronological, conceptual, methodological)
- Gap analysis (evidence, population, setting, mechanism)

**Invocation:**
```
/personas/research:synthesizer Connect these findings on remote work
```

---

## Advisory Package

**Purpose**: Business advisory for founders and decision makers - strategy, funding, growth, operations, legal.

**Orchestrator**: `/review-business-decision`

**Unique Feature**: Two-dimensional weighting based on business maturity stage AND decision focus area.

### Skeptic

**Mandate:** *Trust nothing. Verify everything.*

**Role:** Truth verifier and assumption tester.

**Use when you need:**
- Business claims verified
- Market data validated
- Assumptions tested
- Business fallacies detected
- Vendor claims assessed

**Key Frameworks (from PersonaSkill):**
- Business claim verification
- Market data validation
- Common business fallacy detection
- Vendor/partner claim assessment
- Assumption testing methods

**Invocation:**
```
/personas/advisory:skeptic Verify the market size claims in this pitch deck
```

---

### CFO

**Mandate:** *Numbers tell the truth.*

**Role:** Financial guardian and runway protector.

**Use when you need:**
- Runway impact analysis
- Unit economics evaluation
- Fundraising timing and terms
- Cost structure assessment
- ROI calculations

**Key Frameworks (from PersonaSkill):**
- Runway calculations and burn analysis
- Unit economics (CAC, LTV, payback period)
- Fundraising metrics and dilution math
- Cost structure analysis

**Invocation:**
```
/personas/advisory:cfo What's our runway if we hire 5 engineers?
```

---

### Go-to-Market

**Mandate:** *Revenue is oxygen.*

**Role:** Revenue champion and customer acquisition strategist.

**Use when you need:**
- Customer acquisition strategy
- Pricing and positioning decisions
- Sales process optimization
- Retention and expansion analysis
- GTM model selection

**Key Frameworks (from PersonaSkill):**
- ICP and segmentation frameworks
- GTM motion comparison (sales-led, product-led, etc.)
- Pricing strategy models
- Retention and expansion levers

**Invocation:**
```
/personas/advisory:go-to-market Should we pursue enterprise or SMB first?
```

---

### Strategist

**Mandate:** *Play the long game.*

**Role:** Vision keeper and competitive positioning expert.

**Use when you need:**
- Long-term strategic planning
- Competitive positioning analysis
- Market entry decisions
- Exit strategy evaluation
- Moat assessment

**Key Frameworks (from PersonaSkill):**
- Porter's Five Forces
- TAM/SAM/SOM analysis
- Moat types and durability
- Exit path comparison

**Invocation:**
```
/personas/advisory:strategist Is this market window closing?
```

---

### Operations

**Mandate:** *Execution eats strategy.*

**Role:** Execution realist and capacity planner.

**Use when you need:**
- Team capacity assessment
- Hiring and org design
- Process maturity evaluation
- Scalability analysis
- Execution risk identification

**Key Frameworks (from PersonaSkill):**
- Organizational scaling patterns
- Process maturity model
- Capacity planning formulas
- Risk assessment methods

**Invocation:**
```
/personas/advisory:operations Can we ship this by Q2?
```

---

### Product Advisor

**Mandate:** *Build what matters.*

**Role:** User advocate and prioritization expert.

**Use when you need:**
- Product-market fit assessment
- Feature prioritization
- Build vs buy decisions
- Roadmap strategy
- User value validation

**Key Frameworks (from PersonaSkill):**
- PMF signals and measurement
- RICE/ICE prioritization
- MVP definition criteria
- Competitive response strategies

**Invocation:**
```
/personas/advisory:product-advisor Should we build or buy this feature?
```

---

### Counsel

**Mandate:** *Risk is not optional.*

**Role:** Legal guardian and risk manager.

**Use when you need:**
- Legal risk assessment
- Compliance requirements
- IP protection strategy
- Contract review
- Corporate structure decisions

**Key Frameworks (from PersonaSkill):**
- Entity structure comparison
- IP protection frameworks
- Compliance by business type
- Term sheet analysis

**Invocation:**
```
/personas/advisory:counsel What are the risks of this partnership?
```

---

## Using the System

### Individual Persona Analysis

Use individual personas for focused, single-perspective analysis:

**Product Package:**
```
/personas/product:skeptic Does Azure CLU support batch inference?
/personas/product:architect Should we add a caching layer?
/personas/product:economist What's the real cost of adding Redis?
/personas/product:pragmatist Can we ship without the admin dashboard?
```

**Research Package:**
```
/personas/research:skeptic Verify these citations actually support the claims
/personas/research:librarian Evaluate this meta-analysis
/personas/research:methodologist Is this sample size adequate?
/personas/research:critic What are the counterarguments to this claim?
/personas/research:synthesizer What themes emerge from these studies?
```

**Advisory Package:**
```
/personas/advisory:skeptic Verify the market size claims in this pitch deck
/personas/advisory:cfo What's our runway if we hire 5 engineers?
/personas/advisory:go-to-market Should we pursue enterprise or SMB?
/personas/advisory:strategist Is this market window closing?
/personas/advisory:operations Can we execute a Q2 launch?
/personas/advisory:product-advisor Should we build or buy this feature?
/personas/advisory:counsel What are the legal risks of this partnership?
```

### Full Multi-Persona Review

Use orchestrators for comprehensive analysis when you need multiple perspectives:

**Product Decisions:**
```
/review-product-decision Use Redis for session caching instead of in-memory cache
```
Triggers all four product personas, then synthesizes weighted consensus.

**Research Questions:**
```
/review-research Does intermittent fasting improve cognitive function?
```
Triggers all five research personas (including Skeptic), then synthesizes weighted consensus.

**Business Decisions:**
```
/review-business-decision Should we raise a Series A now or wait 6 months?
```
Triggers all seven advisory personas (including Skeptic) with stage-aware weighting, then synthesizes weighted consensus.

---

## Weighted Consensus

### Product Package Weighting

Different project phases weight personas differently:

| Phase | Skeptic | Architect | Economist | Pragmatist |
|-------|---------|-----------|-----------|------------|
| **Pre-validation** | 0.15 | 0.15 | 0.20 | **0.50** |
| **Post-validation** | 0.20 | 0.25 | 0.20 | 0.35 |
| **Scale-ready** | 0.20 | **0.30** | 0.15 | 0.35 |

**Rationale:**
- **Pre-validation**: Pragmatist dominates - shipping to learn is more valuable than optimizing prematurely
- **Post-validation**: Architect weight increases as sustainable design matters more
- **Scale-ready**: Architect dominates because structural integrity is critical at scale

### Research Package Weighting

Different research phases weight personas differently:

| Phase | Skeptic | Librarian | Methodologist | Critic | Synthesizer |
|-------|---------|-----------|---------------|--------|-------------|
| **Source Discovery** | 0.10 | **0.35** | 0.12 | 0.13 | 0.30 |
| **Quality Assessment** | 0.18 | 0.20 | **0.32** | 0.18 | 0.12 |
| **Claim Evaluation** | **0.28** | 0.15 | 0.20 | **0.25** | 0.12 |
| **Knowledge Integration** | 0.12 | 0.13 | 0.15 | 0.18 | **0.42** |

**Rationale:**
- **Source Discovery**: Librarian dominates - finding good sources is the priority
- **Quality Assessment**: Methodologist dominates - rigor is the focus
- **Claim Evaluation**: Skeptic and Critic co-dominate - verifying and challenging claims is key
- **Knowledge Integration**: Synthesizer dominates - building understanding is the goal

### Advisory Package Weighting

The Advisory package uses **two-dimensional weighting**: business maturity stage AND decision focus area.

**Stage-Based Default Weights:**

| Stage | Skeptic | CFO | GTM | Strategist | Ops | Product | Counsel |
|-------|---------|-----|-----|------------|-----|---------|---------|
| **Pre-seed** | 0.08 | 0.07 | 0.11 | **0.27** | 0.07 | **0.25** | 0.15 |
| **Seed** | 0.10 | 0.11 | 0.16 | 0.15 | 0.12 | **0.24** | 0.12 |
| **Series A** | 0.12 | 0.16 | **0.24** | 0.15 | 0.12 | 0.12 | 0.09 |
| **Series B+** | 0.12 | **0.20** | 0.15 | 0.12 | **0.20** | 0.11 | 0.10 |
| **Exit** | 0.10 | **0.22** | 0.10 | **0.23** | 0.10 | 0.07 | **0.18** |

**Focus modifiers** are then applied based on decision type (Strategy, Funding, Growth, Product, Operations, Legal).

**Rationale:**
- **Pre-seed**: Strategist and Product dominate - validate the problem and vision
- **Seed**: Product dominates - find product-market fit
- **Series A**: Go-to-Market dominates - scale what works
- **Series B+**: CFO and Operations dominate - optimize and scale efficiently
- **Exit**: CFO, Strategist, and Counsel dominate - maximize deal value

### Conflict Resolution

When persona confidence scores diverge by >0.3, orchestrators surface the conflict:

> **Conflict:** Architect (0.8) and Pragmatist (0.9) disagree.
> - Architect prefers abstraction layer for maintainability
> - Pragmatist recommends direct implementation to ship faster
>
> **Resolution depends on:** Current project phase and timeline constraints

---

## Artifact Production

After running a multi-persona review, you can export the analysis to a formal document suitable for sharing, archiving, or converting to DOCX/PDF.

### Available Artifacts

| Package | Artifact | Command | Output |
|---------|----------|---------|--------|
| **Product** | Architecture Decision Record | `/export-artifact adr <name>` | ADR document |
| **Research** | Literature Review | `/export-artifact literature-review <name>` | Review document |
| **Advisory** | Board Memo | `/export-artifact board-memo <name>` | Board-ready memo |

### Workflow

1. **Run a persona review:**
   ```
   /review-product-decision Should we use Redis for caching?
   ```

2. **Export to artifact after analysis completes:**
   ```
   /export-artifact adr redis-caching
   ```

3. **Find your artifact:**
   ```
   docs/decisions/product/2026-01-04-redis-caching/README.md
   ```

### Format Conversion

Generated markdown can be converted to other formats using pandoc:

```bash
cd docs/decisions/product/2026-01-04-redis-caching/

# To PDF
pandoc README.md -o decision.pdf

# To Word
pandoc README.md -o decision.docx

# To HTML
pandoc README.md -o decision.html --standalone
```

### Storage Structure

Artifacts are stored in date-based folders with git history for versioning:

```
docs/decisions/
├── product/              # From /review-product-decision
│   └── YYYY-MM-DD-name/
├── research/             # From /review-research
│   └── YYYY-MM-DD-name/
└── advisory/             # From /review-business-decision
    └── YYYY-MM-DD-name/
```

See [docs/decisions/README.md](../decisions/README.md) for full documentation.

---

## Confidence Scoring

All personas use a 0.0-1.0 confidence scale:

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | High confidence - verified/well-understood |
| 0.7-0.8 | Moderate confidence - some assumptions |
| 0.5-0.6 | Low confidence - significant unknowns |
| < 0.5 | Insufficient information to evaluate |

### Evidence-Based Calibration

Each persona skill defines confidence modifiers based on evidence strength. Examples:

**Positive modifiers:**
- Official documentation cited (+0.2)
- Measured data available (+0.15)
- Follows established patterns (+0.1)

**Negative modifiers:**
- Unverified claims (-0.2)
- New technology without precedent (-0.15)
- Contradicting sources (-0.2)

---

## Creating New Packages

For detailed guidance on creating new persona packages, see [PERSONA-PACKAGES.md](PERSONA-PACKAGES.md).

### Quick Summary

1. **Design personas** - 3-5 complementary perspectives for your domain
2. **Create skills** - Domain expertise in `.claude/skills/personas/<package>/`
3. **Create commands** - Process definitions in `.claude/commands/personas/<package>/`
4. **Create orchestrator** - Coordination in `.claude/commands/review-<package>-*.md`

### Example Package Ideas

| Package | Purpose | Potential Personas |
|---------|---------|-------------------|
| **Security** | Security review | Threat Modeler, Penetration Tester, Compliance Auditor, Incident Responder |
| **UX** | User experience | User Advocate, Accessibility Expert, Performance Monitor, Design Systems |
| **Data** | Data analysis | Statistician, Data Engineer, Privacy Guardian, Visualization Expert |

---

## File Reference

### Product Package

**Commands:**
- `.claude/commands/personas/product/skeptic.md`
- `.claude/commands/personas/product/architect.md`
- `.claude/commands/personas/product/economist.md`
- `.claude/commands/personas/product/pragmatist.md`

**Skills:**
- `.claude/skills/personas/product/skeptic.persona.md`
- `.claude/skills/personas/product/architect.persona.md`
- `.claude/skills/personas/product/economist.persona.md`
- `.claude/skills/personas/product/pragmatist.persona.md`

**Orchestrator:**
- `.claude/commands/review-product-decision.md`

### Research Package

**Commands:**
- `.claude/commands/personas/research/skeptic.md`
- `.claude/commands/personas/research/librarian.md`
- `.claude/commands/personas/research/methodologist.md`
- `.claude/commands/personas/research/critic.md`
- `.claude/commands/personas/research/synthesizer.md`

**Skills:**
- `.claude/skills/personas/research/skeptic.persona.md`
- `.claude/skills/personas/research/librarian.persona.md`
- `.claude/skills/personas/research/methodologist.persona.md`
- `.claude/skills/personas/research/critic.persona.md`
- `.claude/skills/personas/research/synthesizer.persona.md`

**Orchestrator:**
- `.claude/commands/review-research.md`

### Advisory Package

**Commands:**
- `.claude/commands/personas/advisory/skeptic.md`
- `.claude/commands/personas/advisory/cfo.md`
- `.claude/commands/personas/advisory/go-to-market.md`
- `.claude/commands/personas/advisory/strategist.md`
- `.claude/commands/personas/advisory/operations.md`
- `.claude/commands/personas/advisory/product-advisor.md`
- `.claude/commands/personas/advisory/counsel.md`

**Skills:**
- `.claude/skills/personas/advisory/skeptic.persona.md`
- `.claude/skills/personas/advisory/cfo.persona.md`
- `.claude/skills/personas/advisory/go-to-market.persona.md`
- `.claude/skills/personas/advisory/strategist.persona.md`
- `.claude/skills/personas/advisory/operations.persona.md`
- `.claude/skills/personas/advisory/product-advisor.persona.md`
- `.claude/skills/personas/advisory/counsel.persona.md`

**Orchestrator:**
- `.claude/commands/review-business-decision.md`

---

## Best Practices

### When to Use Personas

**Do use personas for:**
- Architectural decisions with multiple valid approaches
- Technology selection with tradeoffs
- Research questions requiring source evaluation
- Feature scope decisions
- Build vs buy evaluations
- Business strategy decisions (funding, growth, exits)
- Founder/executive advisory needs

**Don't use personas for:**
- Simple bug fixes
- Trivial implementation details
- Questions with obvious answers
- Tasks requiring execution rather than analysis

### Getting Good Results

1. **Be specific** in your decision or research question
2. **Provide context** about project phase, constraints, or research goals
3. **Choose the right package** - product for development decisions, research for information analysis, advisory for business strategy
4. **Ask follow-ups** if a persona's analysis raises new questions
5. **Trust disagreements** - conflicts often reveal important tradeoffs

### Customizing for Your Project

1. **Adjust weights** in orchestrators for your project phase
2. **Add project context** to individual persona commands
3. **Create domain-specific packages** for your needs
4. **Extend PersonaSkills** with project-specific patterns
