---
name: list-personas
description: List all available personas with their expertise and usage examples. Use for discovering which persona to invoke for a specific question.
---

# List Available Personas

Display all available personas organized by package, with quick reference for when to use each one.

---

## Persona Packages Overview

| Package | Focus | Personas | Use When |
|---------|-------|----------|----------|
| **Core** | Cross-domain utilities | 2 | Verification, AI/LLM questions |
| **Product** | Technical decisions | 4 | Architecture, costs, shipping |
| **Research** | Information quality | 4 | Sources, methodology, synthesis |
| **Advisory** | Business decisions | 7 | Finance, legal, strategy, ops |

---

## Core Package

Cross-domain personas that support all decision types.

### Skeptic (`/personas/core:skeptic`)
**Mandate:** Trust nothing. Verify everything.

**Use when you need to:**
- Verify technical claims ("Redis handles 100k connections")
- Challenge assumptions ("Our market is growing 40% YoY")
- Fact-check research citations
- Find evidence for business claims

**Example:**
```
/personas/core:skeptic Verify that "React 18 automatically batches all state updates"
```

### Anthropic Expert (`/personas/core:anthropic-expert`)
**Mandate:** Optimal Claude integrations following best practices.

**Use when you need to:**
- Review prompt designs
- Optimize Claude API usage
- Structure tool schemas
- Evaluate AI integration patterns

**Example:**
```
/personas/core:anthropic-expert Review this system prompt for our customer support bot
```

---

## Product Package

For technical implementation decisions.

### Architect (`/personas/product:architect`)
**Mandate:** Design for change. Isolate what varies.

**Use for:** SOLID principles, pattern consistency, coupling analysis, testability

**Example:**
```
/personas/product:architect Should we use a monorepo or separate repos for our microservices?
```

### Economist (`/personas/product:economist`)
**Mandate:** Every choice has a cost. Make them visible.

**Use for:** Build vs buy, TCO analysis, hidden costs, ROI calculations

**Example:**
```
/personas/product:economist Build vs buy analysis for authentication - Auth0 vs custom
```

### Pragmatist (`/personas/product:pragmatist`)
**Mandate:** Ship to learn. Perfect later.

**Use for:** MVP identification, complexity justification, deferral decisions

**Example:**
```
/personas/product:pragmatist Do we really need microservices for our MVP?
```

---

## Research Package

For evaluating information quality and synthesis.

### Librarian (`/personas/research:librarian`)
**Mandate:** Primary sources. Credible citations.

**Use for:** Source credibility, finding primary sources, citation chains

**Example:**
```
/personas/research:librarian Find the primary source for "90% of startups fail"
```

### Methodologist (`/personas/research:methodologist`)
**Mandate:** Valid methods. Reproducible results.

**Use for:** Study quality, research design, statistical validity

**Example:**
```
/personas/research:methodologist Is a sample size of 100 sufficient for this user survey?
```

### Critic (`/personas/research:critic`)
**Mandate:** Steel-man, then challenge.

**Use for:** Counterarguments, alternative explanations, stress-testing claims

**Example:**
```
/personas/research:critic Challenge the thesis that remote work reduces productivity
```

### Synthesizer (`/personas/research:synthesizer`)
**Mandate:** Connect the dots. Find the patterns.

**Use for:** Integrating sources, finding themes, building mental models

**Example:**
```
/personas/research:synthesizer What patterns emerge from our user interview findings?
```

---

## Advisory Package

For business and strategic decisions.

### CFO (`/personas/advisory:cfo`)
**Mandate:** Numbers tell the truth.

**Use for:** Runway, unit economics, financial modeling, fundraising

**Example:**
```
/personas/advisory:cfo Should we hire 3 engineers now or wait until Series A?
```

### Go-to-Market (`/personas/advisory:go-to-market`)
**Mandate:** Revenue is oxygen.

**Use for:** Pricing, customer acquisition, ICP, sales strategy

**Example:**
```
/personas/advisory:go-to-market Should we price per seat or per usage?
```

### Strategist (`/personas/advisory:strategist`)
**Mandate:** Play the long game.

**Use for:** Competitive positioning, moats, pivots, partnerships

**Example:**
```
/personas/advisory:strategist What's our defensible moat in this market?
```

### Operations (`/personas/advisory:operations`)
**Mandate:** Execution eats strategy.

**Use for:** Team capacity, hiring, process scalability, key-person risk

**Example:**
```
/personas/advisory:operations Can our team of 5 handle this new product line?
```

### Product Advisor (`/personas/advisory:product-advisor`)
**Mandate:** Build what matters.

**Use for:** PMF signals, feature prioritization, roadmap strategy

**Example:**
```
/personas/advisory:product-advisor Should we prioritize mobile app or API integrations?
```

### Counsel (`/personas/advisory:counsel`)
**Mandate:** Risk is not optional.

**Use for:** Legal structure, IP protection, contracts, compliance

**Example:**
```
/personas/advisory:counsel Should we incorporate as LLC or C-Corp for fundraising?
```

---

## Multi-Persona Reviews (Orchestrators)

For comprehensive analysis, use orchestrated reviews that run multiple personas:

| Command | Personas | Output |
|---------|----------|--------|
| `/review-product-decision` | Skeptic → Architect → Economist → Pragmatist | ADR |
| `/review-research` | Skeptic → Librarian → Methodologist → Critic → Synthesizer | Literature Review |
| `/review-business-decision` | Skeptic → CFO → GTM → Strategist → Ops → Product → Counsel | Board Memo |

**Example:**
```
/review-product-decision Should we use Redis or PostgreSQL for session storage?
```

---

## Understanding Confidence Scores

All personas output confidence scores (0.0-1.0). Here's what they mean:

### Score Thresholds

| Score | Label | What It Means | Recommended Action |
|-------|-------|---------------|-------------------|
| **0.90-1.00** | High | Well-understood domain, verified information | Proceed with confidence |
| **0.70-0.89** | Moderate | Some assumptions or uncertainties remain | Note risks, proceed cautiously |
| **0.50-0.69** | Low | Significant unknowns or conflicting information | Investigate before deciding |
| **< 0.50** | Insufficient | Cannot provide meaningful analysis | Do not proceed without resolution |

### Interpreting Scores in Context

**Technical decisions (Product package):**
- 0.85+ → Implementation can begin
- 0.70-0.84 → Prototype first, validate assumptions
- < 0.70 → Need more research or spikes

**Research claims (Research package):**
- 0.90+ → Can cite with confidence
- 0.70-0.89 → Cite with caveats
- < 0.70 → Need better sources

**Business decisions (Advisory package):**
- 0.80+ → Board-ready recommendation
- 0.60-0.79 → Needs additional validation
- < 0.60 → Premature to decide

### When Personas Disagree

In orchestrated reviews, if confidence scores diverge by >0.3:
- This indicates genuine uncertainty, not persona failure
- The synthesis will highlight the tension
- Consider running individual personas for deeper analysis

---

## Quick Reference Card

**Need to verify a claim?** → `/personas/core:skeptic`

**Technical architecture question?** → `/personas/product:architect`

**What will this cost?** → `/personas/product:economist`

**Can we ship simpler?** → `/personas/product:pragmatist`

**Is this source reliable?** → `/personas/research:librarian`

**Is this study valid?** → `/personas/research:methodologist`

**What's the counterargument?** → `/personas/research:critic`

**Can we afford this?** → `/personas/advisory:cfo`

**How do we sell this?** → `/personas/advisory:go-to-market`

**What's the strategy?** → `/personas/advisory:strategist`

**Can the team handle this?** → `/personas/advisory:operations`

**Should we build this feature?** → `/personas/advisory:product-advisor`

**Is this legal/compliant?** → `/personas/advisory:counsel`

**Multi-perspective product analysis?** → `/review-product-decision`

**Multi-perspective research analysis?** → `/review-research`

**Multi-perspective business analysis?** → `/review-business-decision`
