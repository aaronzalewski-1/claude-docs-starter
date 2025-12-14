---
name: review-decision
description: Multi-persona review of implementation decisions. Use when evaluating architectural choices, technology selections, implementation approaches, or design patterns. Triggers on phrases like "review this decision", "should I use X or Y", "debate this approach", "evaluate my plan to", or the explicit /review-decision command.
---

# Review Decision

Evaluate implementation decisions through five specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-decision <decision or implementation approach>
```

Also triggers on natural language requests to review, debate, or evaluate architectural/implementation choices.

## Personas

### Skeptic

**Role:** Fact-checker and assumption challenger.

**Process:**
1. Identify every technical claim in the proposed decision
2. For each claim, perform web search to verify against official documentation:
   - Framework features: Search official docs
   - Packages/libraries: Verify they exist, check version compatibility
   - ORM behaviors: Confirm against current documentation
   - API limitations: Find documented constraints (rate limits, size limits, etc.)
3. Flag unverified assumptions that need validation before committing
4. Challenge "obvious" choices that may have non-obvious drawbacks

**Output includes:**
- Verified claims with source references
- Unverified claims requiring investigation
- Assumptions that need testing
- Confidence score (0.0-1.0)

### Architect

**Role:** Enforces SOLID principles, clean abstractions, and pattern consistency.

**Evaluates:**
- Does this align with established patterns in the codebase?
- Does it create coupling that will be painful to change?
- Is the abstraction at the right level?
- Will this be testable in isolation?
- Does it violate single responsibility?

**Flags:**
- Pattern inconsistencies with existing code
- Tight coupling to specific implementations
- Missing abstraction layers
- Testability concerns

### Economist

**Role:** Evaluates cost, time investment, and ROI.

**Calculates:**
- Resource costs at expected scale (cloud services, third-party APIs)
- Development time to implement vs. alternatives
- Maintenance burden over 12-month horizon
- Opportunity cost of learning curve

**Context awareness:**
- Budget constraints
- Team size and capacity
- MVP vs. scale-ready tradeoffs

### Pragmatist

**Role:** Advocates for shipping and iteration over perfection.

**Questions:**
- Do we have paying customers yet?
- Has this need been validated?
- What's the simplest thing that could work?
- Can we defer this complexity?

**Recommends:**
- MVP approaches that validate assumptions
- Migration paths from simple to sophisticated
- When to take technical debt intentionally

### {{TECH_STACK}} Advocate

<!-- Customize this persona for your tech stack: ".NET Advocate", "React Advocate", "Python Advocate", etc. -->

**Role:** Ensures idiomatic implementation for your technology stack.

**Checks:**
- Correct packages/libraries for your framework version
- Framework idioms and conventions
- Whether a library already solves this problem
- ORM/database best practices
- Cloud SDK patterns (if applicable)

**Provides:**
- Specific package recommendations with versions
- Code pattern suggestions
- Links to relevant official documentation

## Output Format

```markdown
## Decision Under Review
[Restate the decision clearly]

## Skeptic
[Verification results, unverified claims, challenged assumptions]
**Confidence: X.X**

## Architect
[Pattern analysis, coupling concerns, abstraction evaluation]
**Confidence: X.X**

## Economist
[Cost analysis, time investment, ROI assessment]
**Confidence: X.X**

## Pragmatist
[MVP perspective, shipping considerations, deferral opportunities]
**Confidence: X.X**

## {{TECH_STACK}} Advocate
[Framework guidance, package recommendations, idiomatic patterns]
**Confidence: X.X**

## Consensus
[Synthesized recommendation weighing all perspectives]

**Recommendation:** [Clear action]
**Key tradeoff:** [Primary tension between personas]
**Deferred decision:** [What can wait until later]
```

## Skeptic Verification Protocol

The Skeptic MUST perform actual verification, not hypothetical concerns:

1. **Framework/Platform Claims**
   ```
   Search: "[feature name] site:official-docs-url"
   Verify: Feature exists, works as described, check limitations
   ```

2. **Packages/Libraries**
   ```
   Search: "[package name] [package manager]"
   Verify: Package exists, is actively maintained, compatible with your version
   ```

3. **Size/Rate Limits**
   ```
   Search: "[service] limits quotas"
   Document: Specific numbers that constrain the decision
   ```

4. **ORM/Database Behaviors**
   ```
   Search: "[behavior] [ORM name] [version]"
   Verify: Behavior works as assumed in current version
   ```

## Confidence Scoring

Each persona provides a confidence score:

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | High confidence, verified/well-understood |
| 0.7-0.8 | Moderate confidence, some assumptions |
| 0.5-0.6 | Low confidence, significant unknowns |
| <0.5 | Insufficient information to evaluate |

## Consensus Weighting

Default weights (adjust based on project phase):

| Phase | Skeptic | Architect | Economist | Pragmatist | Tech Advocate |
|-------|---------|-----------|-----------|------------|---------------|
| Pre-validation (no users) | 0.15 | 0.15 | 0.20 | 0.35 | 0.15 |
| Post-validation (early users) | 0.20 | 0.25 | 0.20 | 0.15 | 0.20 |
| Scale-ready (growth phase) | 0.20 | 0.30 | 0.15 | 0.10 | 0.25 |

## When Personas Disagree

If confidence-weighted scores diverge by >0.3, explicitly surface the tradeoff:

> **Conflict:** Architect (0.8) and Pragmatist (0.85) disagree. Architect prefers [X] for maintainability; Pragmatist recommends [Y] to ship faster. Resolution depends on: [specific factor user must decide].

## Example

```
/review-decision Use Redis for session caching instead of in-memory cache
```

Triggers full persona analysis with:
- Skeptic verifying Redis hosting costs, connection limits, failure modes
- Architect evaluating coupling to Redis, abstraction layer needs
- Economist calculating cost vs. alternatives at projected scale
- Pragmatist questioning whether simpler in-memory suffices pre-validation
- Tech Advocate confirming correct client library, connection pooling patterns
