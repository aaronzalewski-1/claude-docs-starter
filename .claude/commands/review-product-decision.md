---
name: review-product-decision
description: Multi-persona review of product implementation decisions. Use when evaluating architectural choices, technology selections, implementation approaches, or design patterns. Triggers on phrases like "review this decision", "should I use X or Y", "debate this approach", "evaluate my plan to", or the explicit /review-product-decision command.
---

# Review Product Decision

Evaluate product/implementation decisions through four specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-product-decision <decision or implementation approach> [--save <name>]
```

**Arguments:**
- `decision`: The technical decision or implementation approach to evaluate
- `--save <name>`: (Optional) Save the analysis as an ADR to `docs/decisions/product/`

Also triggers on natural language requests to review, debate, or evaluate architectural/implementation choices.

**Examples:**
```
/review-product-decision Should we use Redis or Memcached for session caching?
/review-product-decision Use microservices architecture --save microservices-decision
```

## Package: Product Development

This orchestrator invokes four analytical personas from the **Product Development** package:

| Persona | Role | Focus |
|---------|------|-------|
| **Skeptic** | Fact-checker | Verify claims, challenge assumptions |
| **Architect** | Structure guardian | SOLID principles, patterns, coupling |
| **Economist** | Cost analyst | ROI, TCO, scale economics |
| **Pragmatist** | MVP advocate | Simplicity, deferral, shipping |

Each persona has:
- A **command** (`/personas/product:skeptic`, etc.) for individual invocation
- A **PersonaSkill** with domain expertise frameworks

## Orchestration Process

### Phase 1: Run Each Persona

For the decision provided, run each persona analysis **in sequence**:

1. **Skeptic Analysis** (`/personas/core:skeptic`)
   - Verify all technical claims
   - Flag unverified assumptions
   - Challenge "obvious" choices

2. **Architect Analysis** (`/personas/product:architect`)
   - Evaluate SOLID alignment
   - Check pattern consistency
   - Assess coupling and testability

3. **Economist Analysis** (`/personas/product:economist`)
   - Calculate costs across options
   - Assess ROI and payback period
   - Project scale economics

4. **Pragmatist Analysis** (`/personas/product:pragmatist`)
   - Validate the need
   - Find MVP alternatives
   - Identify deferral opportunities

### Phase 2: Synthesize Consensus

After all personas have analyzed, reason through before producing the synthesis:

**Pre-Synthesis Reasoning (think through these):**
1. Which claims were verified by multiple personas?
2. Where do confidence scores diverge most significantly?
3. What would change each persona's recommendation?
4. Are there any contradictions between persona findings?
5. Which persona's concerns are most critical given the project phase?

Then produce a weighted synthesis.

## Output Format

```markdown
## Decision Under Review
[Restate the decision clearly]

---

## Skeptic Analysis
[Verification results, unverified claims, challenged assumptions]
**Confidence: X.X**

---

## Architect Analysis
[Pattern analysis, coupling concerns, abstraction evaluation]
**Confidence: X.X**

---

## Economist Analysis
[Cost analysis, time investment, ROI assessment]
**Confidence: X.X**

---

## Pragmatist Analysis
[MVP perspective, shipping considerations, deferral opportunities]
**Confidence: X.X**

---

## Weighted Consensus

| Persona | Confidence | Weight | Weighted Score |
|---------|------------|--------|----------------|
| Skeptic | X.X | 0.XX | X.XX |
| Architect | X.X | 0.XX | X.XX |
| Economist | X.X | 0.XX | X.XX |
| Pragmatist | X.X | 0.XX | X.XX |
| **Weighted Average** | | | **X.XX** |

### Synthesis
[Integrated analysis considering all perspectives]

### Key Tradeoffs
[Primary tensions between personas and how to resolve]

### Recommendation
[Clear action with rationale]

### What Can Wait
[Items that can be deferred, with triggers for revisiting]
```

## Consensus Weighting

Default weights vary by project phase. Adjust based on your context:

| Phase | Skeptic | Architect | Economist | Pragmatist |
|-------|---------|-----------|-----------|------------|
| **Pre-validation** (no users) | 0.15 | 0.15 | 0.20 | **0.50** |
| **Post-validation** (early users) | 0.20 | 0.25 | 0.20 | 0.35 |
| **Scale-ready** (growth phase) | 0.20 | **0.30** | 0.15 | 0.35 |

### Weighting Rationale

**Pre-validation** (no users yet):
- **Pragmatist dominates (0.50)** - Ship to learn. Perfect code for the wrong feature is waste.
- Skeptic/Architect low (0.15) - Verification and structure matter less than learning speed.
- Economist moderate (0.20) - Keep an eye on costs, but don't optimize prematurely.

**Post-validation** (early users, iterating):
- **Architect increases (0.25)** - With real users, sustainable design starts to matter.
- Pragmatist decreases (0.35) - Still ship fast, but with more care.
- Skeptic increases (0.20) - Verify claims now that decisions have real impact.

**Scale-ready** (growth phase):
- **Architect dominates (0.30)** - Poor architecture now creates compounding debt.
- Pragmatist still high (0.35) - Keep shipping, but technical debt is riskier.
- Economist decreases (0.15) - Scale economics usually already understood.

### Example Calculation

For a **Pre-validation** project:
```
Skeptic:    0.75 confidence × 0.15 weight = 0.11
Architect:  0.80 confidence × 0.15 weight = 0.12
Economist:  0.85 confidence × 0.20 weight = 0.17
Pragmatist: 0.90 confidence × 0.50 weight = 0.45
                              ────────────────────
Weighted Average:                          0.85
```

## When Personas Disagree

If confidence-weighted scores diverge by >0.3, explicitly surface the conflict:

> **Conflict:** Architect (0.8) and Pragmatist (0.9) disagree.
> - Architect prefers [X] for maintainability
> - Pragmatist recommends [Y] to ship faster
>
> **Resolution depends on:** [specific factor the user must decide]

## Confidence Scoring

Each persona provides a confidence score:

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | High confidence - verified/well-understood |
| 0.7-0.8 | Moderate confidence - some assumptions |
| 0.5-0.6 | Low confidence - significant unknowns |
| < 0.5 | Insufficient information to evaluate |

## Individual Persona Usage

You can invoke personas individually for focused analysis:

```
/personas/core:skeptic Should we use Redis for caching?
/personas/product:architect Evaluate this service layer design
/personas/product:economist Compare cloud vs self-hosted database
/personas/product:pragmatist Is this feature worth building now?
```

## Example

```
/review-product-decision Use Redis for session caching instead of in-memory cache
```

Triggers full persona analysis:
- **Skeptic**: Verifies Redis hosting costs, connection limits, failure modes
- **Architect**: Evaluates coupling to Redis, abstraction layer needs
- **Economist**: Calculates cost vs. alternatives at projected scale
- **Pragmatist**: Questions whether simpler in-memory suffices pre-validation

Then synthesizes weighted consensus with recommendation.

## Related Packages

| Package | Orchestrator | Use For |
|---------|--------------|---------|
| **Product** | `/review-product-decision` | Implementation decisions, architecture |
| **Research** | `/review-research` | Research questions, literature analysis |

## If Analysis Cannot Proceed

If the review cannot be completed due to insufficient information:

1. **Identify which personas are blocked** - Which analyses cannot proceed?
2. **State specifically what's missing** - Technical details, context, requirements?
3. **Provide partial analysis** - Complete what CAN be done
4. **Set confidence to reflect gaps** - Low confidence for incomplete areas
5. **List specific questions** - What must be answered to proceed?

**Example:**
> **Blocked:** Economist cannot assess costs without knowing expected scale
> **Partial analysis available:** Skeptic and Architect can proceed
> **Questions needed:**
> - Expected user count at launch?
> - Growth projections for year 1?
> - Budget constraints?

---

## Next Steps

After consensus, offer relevant follow-up options:

| If Analysis Shows | Offer |
|-------------------|-------|
| More verification needed | Deep-dive research workflow |
| Architectural changes | Implementation guidance |
| Cost optimization | Scale economics projection |
| Simplification recommended | MVP implementation approach |

---

## Saving as ADR (--save option)

When `--save <name>` is provided, generate an Architecture Decision Record after the analysis.

### Step 1: Generate ADR Content

After completing the weighted consensus, transform the analysis into ADR format:

| Analysis Section | ADR Section |
|------------------|-------------|
| Decision statement | Context |
| Consensus recommendation | Decision |
| Benefits from each persona | Positive Consequences |
| Risks/tradeoffs identified | Negative Consequences |
| "What Can Wait" items | Neutral Consequences |
| Options discussed | Alternatives Considered |
| Persona findings & scores | Analysis Summary |

### Step 2: Create ADR File

Save to: `docs/decisions/product/YYYY-MM-DD-<name>/README.md`

Use template from `.claude/templates/product/adr.template.md`

### Step 3: Report Save Location

After saving, append to output:

```markdown
---

## ADR Saved

**File:** `docs/decisions/product/YYYY-MM-DD-<name>/README.md`

**Convert to other formats:**
```bash
cd docs/decisions/product/YYYY-MM-DD-<name>
pandoc README.md -o decision.pdf    # PDF
pandoc README.md -o decision.docx   # Word
```

**Track in git:**
```bash
git add docs/decisions/product/YYYY-MM-DD-<name>/
git commit -m "ADR: <name>"
```
```

### Naming Guidelines

- Use kebab-case: `redis-caching`, `auth-strategy`
- Be descriptive but concise
- Date prefix added automatically
