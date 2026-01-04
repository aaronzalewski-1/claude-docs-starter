---
name: review-business-decision
description: Multi-persona business advisory review. Use when evaluating strategic decisions, growth plans, funding decisions, or any significant business choice. Triggers on phrases like "should we", "evaluate this decision", "business advice", or the explicit /review-business-decision command.
---

# Review Business Decision

Evaluate business decisions through a seven-persona advisory board, with dynamic weighting based on business maturity stage and decision focus area.

## Command Format

```
/review-business-decision <decision> [stage:<stage>] [focus:<focus>]
```

Also triggers on natural language requests for business advice or decision evaluation.

## Package: Advisory

This orchestrator invokes seven advisory personas from the **Advisory** package:

| Persona | Role | Focus |
|---------|------|-------|
| **Skeptic** | Truth verifier | Verify claims, challenge assumptions, test data |
| **CFO** | Financial guardian | Runway, unit economics, fundraising |
| **Go-to-Market** | Revenue champion | Customer acquisition, retention, pricing |
| **Strategist** | Vision keeper | Competitive positioning, exits, moats |
| **Operations** | Execution realist | Capacity, process, scalability |
| **Product Advisor** | User advocate | PMF, prioritization, roadmap |
| **Counsel** | Risk manager | Legal, compliance, IP, contracts |

Each persona has:
- A **command** (`/personas/advisory:cfo`, etc.) for individual invocation
- A **PersonaSkill** with domain expertise frameworks

---

## Context Detection

### Stage Detection

Detect business maturity stage from context clues:

| Stage | Indicators |
|-------|------------|
| **Pre-seed** | "idea", "haven't built", "exploring", no product |
| **Seed** | "MVP", "early customers", "pre-revenue", "first users" |
| **Series A** | "PMF", "scaling", "repeatable sales", "Series A" |
| **Series B+** | "growth stage", "Series B/C", "optimizing", "expanding" |
| **Exit** | "acquisition", "IPO", "exit", "due diligence", "strategic buyer" |

### Focus Detection

Detect decision focus area from context clues:

| Focus | Indicators |
|-------|------------|
| **Strategy** | "pivot", "market entry", "competitive", "direction" |
| **Funding** | "raise", "fundraise", "investors", "runway", "valuation" |
| **Growth** | "acquisition", "marketing", "sales", "revenue" |
| **Product** | "feature", "roadmap", "prioritize", "build" |
| **Operations** | "hire", "team", "process", "scale", "capacity" |
| **Legal** | "contract", "compliance", "IP", "legal", "risk" |

### Exit Type Detection

When stage is Exit, detect exit type:

| Exit Type | Indicators |
|-----------|------------|
| **Acquisition** | "acquire", "strategic buyer", "M&A", "acquisition" |
| **IPO** | "IPO", "public", "going public", "S-1" |
| **Acqui-hire** | "acqui-hire", "team acquisition", "talent acquisition" |

---

## Two-Dimensional Weighting System

### Stage-Based Default Weights

| Stage | Skeptic | CFO | GTM | Strategist | Ops | Product | Counsel |
|-------|---------|-----|-----|------------|-----|---------|---------|
| **Pre-seed** | 0.08 | 0.07 | 0.11 | **0.27** | 0.07 | **0.25** | 0.15 |
| **Seed** | 0.10 | 0.11 | 0.16 | 0.15 | 0.12 | **0.24** | 0.12 |
| **Series A** | 0.12 | 0.16 | **0.24** | 0.15 | 0.12 | 0.12 | 0.09 |
| **Series B+** | 0.12 | **0.20** | 0.15 | 0.12 | **0.20** | 0.11 | 0.10 |
| **Exit** | 0.10 | **0.22** | 0.10 | **0.23** | 0.10 | 0.07 | **0.18** |

### Focus-Based Weight Modifiers

| Focus | Skeptic | CFO | GTM | Strategist | Ops | Product | Counsel |
|-------|---------|-----|-----|------------|-----|---------|---------|
| **Strategy** | +0.02 | -0.03 | +0.00 | **+0.10** | -0.03 | +0.02 | -0.03 |
| **Funding** | **+0.08** | **+0.10** | +0.00 | +0.06 | -0.08 | -0.03 | +0.02 |
| **Growth** | +0.02 | +0.00 | **+0.10** | +0.00 | +0.00 | +0.02 | -0.03 |
| **Product** | +0.00 | -0.03 | +0.02 | +0.00 | +0.00 | **+0.10** | -0.03 |
| **Operations** | +0.00 | +0.02 | -0.03 | -0.03 | **+0.10** | +0.00 | +0.00 |
| **Legal** | +0.03 | +0.00 | -0.05 | +0.00 | +0.00 | -0.05 | **+0.12** |

**Formula**: `Final Weight = Stage Weight + Focus Modifier` (then normalize to 1.0)

### Exit Type Weight Override

When exit type is detected, use these weights instead:

| Exit Type | Skeptic | CFO | GTM | Strategist | Ops | Product | Counsel |
|-----------|---------|-----|-----|------------|-----|---------|---------|
| **Acquisition** | 0.10 | 0.22 | 0.07 | **0.25** | 0.11 | 0.07 | **0.18** |
| **IPO** | 0.10 | **0.25** | 0.10 | 0.18 | 0.10 | 0.07 | **0.20** |
| **Acqui-hire** | 0.08 | 0.10 | 0.04 | 0.14 | **0.30** | 0.15 | **0.19** |

---

## Orchestration Process

### Phase 1: Context Detection

Before running personas, detect:
1. **Stage**: Business maturity stage from context
2. **Focus**: Decision type from context
3. **Exit Type**: If stage is Exit, determine exit type
4. **Calculate Weights**: Apply 2D weighting formula

### Phase 2: Run Each Persona

Run each persona analysis **in sequence**:

1. **Skeptic Analysis** (`/personas/advisory:skeptic`)
   - Verify business claims and data
   - Test key assumptions
   - Check for business fallacies

2. **CFO Analysis** (`/personas/advisory:cfo`)
   - Financial impact assessment
   - Runway and unit economics implications
   - Investment/ROI analysis

3. **Go-to-Market Analysis** (`/personas/advisory:go-to-market`)
   - Revenue and customer impact
   - Acquisition and retention implications
   - Pricing and positioning effects

4. **Strategist Analysis** (`/personas/advisory:strategist`)
   - Long-term strategic implications
   - Competitive positioning impact
   - Exit path considerations

5. **Operations Analysis** (`/personas/advisory:operations`)
   - Execution feasibility
   - Capacity and hiring needs
   - Process and scalability

6. **Product Advisor Analysis** (`/personas/advisory:product-advisor`)
   - Product-market fit impact
   - User value assessment
   - Roadmap implications

7. **Counsel Analysis** (`/personas/advisory:counsel`)
   - Legal and regulatory risks
   - IP and compliance considerations
   - Contract and liability issues

### Phase 3: Synthesize Consensus

After all personas have analyzed, produce weighted synthesis.

---

## Output Format

```markdown
## Business Decision Under Review
[Restate the decision clearly]

**Detected Context:**
- **Stage:** [Pre-seed/Seed/Series A/Series B+/Exit]
- **Focus:** [Strategy/Funding/Growth/Product/Operations/Legal]
- **Exit Type:** [If applicable: Acquisition/IPO/Acqui-hire]

---

## Skeptic Analysis
[Claim verification, assumption testing, data validation]
**Key Concern:** [Primary verification issue]
**Confidence: X.X**

---

## CFO Analysis
[Financial perspective, runway impact, unit economics]
**Key Concern:** [Primary financial consideration]
**Confidence: X.X**

---

## Go-to-Market Analysis
[Revenue perspective, customer acquisition, positioning]
**Key Concern:** [Primary GTM consideration]
**Confidence: X.X**

---

## Strategist Analysis
[Long-term perspective, competitive positioning, exit implications]
**Key Concern:** [Primary strategic consideration]
**Confidence: X.X**

---

## Operations Analysis
[Execution perspective, capacity, process implications]
**Key Concern:** [Primary operational consideration]
**Confidence: X.X**

---

## Product Advisor Analysis
[Product perspective, PMF impact, user value]
**Key Concern:** [Primary product consideration]
**Confidence: X.X**

---

## Counsel Analysis
[Legal perspective, compliance, risk implications]
**Key Concern:** [Primary legal consideration]
**Confidence: X.X**

---

## Advisory Board Consensus

| Persona | Confidence | Weight | Weighted Score |
|---------|------------|--------|----------------|
| Skeptic | X.X | 0.XX | X.XX |
| CFO | X.X | 0.XX | X.XX |
| Go-to-Market | X.X | 0.XX | X.XX |
| Strategist | X.X | 0.XX | X.XX |
| Operations | X.X | 0.XX | X.XX |
| Product Advisor | X.X | 0.XX | X.XX |
| Counsel | X.X | 0.XX | X.XX |
| **Weighted Average** | | | **X.XX** |

### Board Alignment
**[High/Medium/Low]** - [Explanation of agreement or divergence]

### Key Tensions
[If confidence divergence >0.3, surface the conflict with resolution path]

### Synthesis
[Integrated analysis considering all perspectives and stage context]

### Recommendation
**[Proceed/Proceed with conditions/Do not proceed]**
[Clear rationale tied to weighted analysis]

### Critical Actions
1. [Immediate action needed]
2. [Follow-up action]
3. [Risk mitigation]

### Milestones to Revisit
[Triggers that would change this decision - stage transitions, metric thresholds]
```

---

## When Advisors Disagree

If confidence-weighted scores diverge by >0.3, explicitly surface the conflict:

> **Conflict:** CFO (0.5) and Go-to-Market (0.9) disagree.
> - CFO: "Investment extends runway risk beyond comfort"
> - GTM: "Market window requires aggressive investment now"
>
> **Resolution depends on:** [Current runway, market timing evidence, fundraising prospects]

### Stage-Dependent Conflict Priorities

When conflicts arise, weight resolution toward:

| Stage | Favor... | Rationale |
|-------|----------|-----------|
| **Pre-seed** | Product Advisor, Strategist | Learning is priority |
| **Seed** | Operations, Product Advisor | Execution is priority |
| **Series A** | Go-to-Market, CFO | Sustainable growth is priority |
| **Series B+** | CFO, Operations | Efficiency is priority |
| **Exit** | Strategist, CFO, Counsel | Deal optimization is priority |

---

## Confidence Scoring

Each persona provides a confidence score:

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | High confidence - strong evidence, clear recommendation |
| 0.7-0.8 | Moderate confidence - good evidence, some assumptions |
| 0.5-0.6 | Low confidence - significant unknowns |
| < 0.5 | Insufficient - major gaps, cannot recommend |

---

## Individual Persona Usage

You can invoke personas individually for focused analysis:

```
/personas/advisory:skeptic Verify the market size claims in this pitch deck
/personas/advisory:cfo What's our runway impact if we hire 5 engineers?
/personas/advisory:go-to-market Should we pursue enterprise or SMB first?
/personas/advisory:strategist Is this market window closing?
/personas/advisory:operations Can we ship this by Q2?
/personas/advisory:product-advisor Should we build or buy this feature?
/personas/advisory:counsel What are the risks of this partnership?
```

---

## Example

```
/review-business-decision Should we raise a Series A now or wait 6 months?
```

**Detected Context:**
- Stage: Seed (transitioning to Series A)
- Focus: Funding
- Exit Type: N/A

Triggers full advisory analysis:
- **Skeptic**: Verifies growth claims, tests market timing assumptions, validates metrics
- **CFO**: Runway analysis, valuation considerations, dilution math
- **Go-to-Market**: Revenue metrics, growth trajectory for raise
- **Strategist**: Market timing, competitive dynamics, investor landscape
- **Operations**: Capacity to execute post-raise plan
- **Product Advisor**: PMF evidence, product milestones for raise
- **Counsel**: Term sheet considerations, governance implications

Then synthesizes weighted consensus with stage-appropriate recommendation.

---

## Related Packages

| Package | Orchestrator | Use For |
|---------|--------------|---------|
| **Product** | `/review-product-decision` | Technical implementation decisions |
| **Research** | `/review-research` | Research questions, source evaluation |
| **Advisory** | `/review-business-decision` | Business strategy, funding, growth |

---

## Next Steps

After consensus, offer relevant follow-up options:

| If Analysis Shows | Offer |
|-------------------|-------|
| Claims need verification | Skeptic deep-dive on specific assumptions |
| Need deeper financial analysis | CFO deep-dive on specific metrics |
| GTM strategy questions | Go-to-Market channel analysis |
| Strategic pivot consideration | Strategist scenario planning |
| Execution concerns | Operations capacity planning |
| Product validation needed | Product Advisor user research plan |
| Legal complexity | Counsel risk mitigation roadmap |
