---
name: review-product-decision
description: Multi-persona review of product implementation decisions. Use when evaluating architectural choices, technology selections, implementation approaches, or design patterns. Triggers on phrases like "review this decision", "should I use X or Y", "debate this approach", "evaluate my plan to", or the explicit /review-product-decision command.
---

# Review Product Decision

Evaluate product/implementation decisions through four specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-product-decision <decision or implementation approach>
```

Also triggers on natural language requests to review, debate, or evaluate architectural/implementation choices.

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

1. **Skeptic Analysis** (`/personas/product:skeptic`)
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

After all personas have analyzed, produce a weighted synthesis.

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

**Pre-validation**: Pragmatist has highest weight - ship to learn before optimizing.

**Post-validation**: Architect weight increases - sustainable design matters more.

**Scale-ready**: Architect dominates - structural integrity is critical.

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
/personas/product:skeptic Should we use Redis for caching?
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

## Next Steps

After consensus, offer relevant follow-up options:

| If Analysis Shows | Offer |
|-------------------|-------|
| More verification needed | Deep-dive research workflow |
| Architectural changes | Implementation guidance |
| Cost optimization | Scale economics projection |
| Simplification recommended | MVP implementation approach |
