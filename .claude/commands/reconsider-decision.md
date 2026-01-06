---
name: reconsider-decision
description: Re-evaluate a past decision in an isolated sandbox. Use when circumstances have changed, assumptions were invalidated, or you want to explore "what if" scenarios without affecting active planning.
---

# Reconsider Decision

Re-evaluate a past decision in isolation, optionally running personas again with current knowledge.

## Command Format

```
/reconsider-decision <decision-id or search> [--run-personas]
```

**Arguments:**
- `decision-id`: Entry ID (e.g., `2026-01-03-abc123`) or search term
- `--run-personas`: Re-run persona analysis with current context

**Examples:**
```
/reconsider-decision 2026-01-03-abc123
/reconsider-decision "database selection" --run-personas
/reconsider-decision "caching strategy"
```

---

## Core Principle: Isolation

**Reconsiderations are ISOLATED from active planning.**

- Output goes to `docs/reasoning/sandbox/`
- Never modifies active reasoning logs
- Never auto-merges into plans or roadmaps
- Only `/promote-reconsideration` moves sandbox → active

---

## Process

### Step 1: Find Original Decision

**If ID provided:**
1. Parse date from ID prefix
2. Read `docs/reasoning/YYYY-MM-DD-reasoning-log.json`
3. Find entry with matching ID

**If search term provided:**
1. Read `docs/reasoning/index.json`
2. Search `byTopic` and `entries` for matches
3. If multiple matches, present options:
   ```
   Found multiple decisions matching "database":
   1. 2026-01-03-abc123: "Database selection for users"
   2. 2026-01-05-def456: "Database indexing strategy"

   Which decision do you want to reconsider? (1-2)
   ```

### Step 2: Load Original Context

Display original decision:

```markdown
## Original Decision

**ID:** [id]
**Date:** [timestamp]
**Decision Point:** [reasoning.decisionPoint]

**What We Decided:**
[outcome.decision]

**Original Rationale:**
[reasoning.rationale]

**Alternatives Considered:**
[list alternatives]

**Assumptions Made:**
[list assumptions with validation status]

**Confidence:** [confidence]

**Dependencies:** [dependsOn entries]
```

### Step 3: Gather Reconsideration Context

Ask:
```
Why are you reconsidering this decision?
- [C] Circumstances changed
- [A] Assumptions invalidated
- [N] New information available
- [E] Exploring alternatives
- [O] Other
```

Based on response, prompt for details:
- What changed?
- What new information do we have?
- Which assumptions were wrong?

### Step 4: Re-evaluate (Optional Personas)

**If `--run-personas`:**
1. Run `/review-product-decision` or appropriate orchestrator
2. Use current context + original decision as input
3. Capture persona contributions

**If no personas:**
1. Manual re-evaluation
2. Ask about alternatives with new context
3. Ask about updated assumptions

### Step 5: Generate Sandbox Entry

Create file: `docs/reasoning/sandbox/YYYY-MM-DD-{topic}-recon.json`

**Schema:**
```json
{
  "schemaVersion": "1.0.0",
  "id": "2026-01-06-abc123-recon",
  "status": "sandbox",
  "reconsiderationDate": "2026-01-06T14:30:00Z",
  "original": {
    "decisionId": "2026-01-03-abc123",
    "decisionDate": "2026-01-03",
    "decisionPoint": "Original question",
    "outcome": "Original decision"
  },
  "trigger": {
    "type": "circumstances_changed | assumptions_invalidated | new_information | exploring",
    "description": "Why reconsidering"
  },
  "changedContext": {
    "whatChanged": "Description of changes",
    "newInformation": ["New facts"],
    "invalidatedAssumptions": [
      {
        "assumption": "Original assumption",
        "whyInvalid": "What we learned"
      }
    ]
  },
  "revisedAnalysis": {
    "decisionPoint": "Same or refined question",
    "rationale": "New rationale with current context",
    "alternatives": [
      {
        "option": "Alternative",
        "assessment": "How it looks now",
        "pros": [],
        "cons": []
      }
    ],
    "newAssumptions": [],
    "evidence": []
  },
  "personaContributions": [],
  "proposedOutcome": {
    "recommendation": "What we'd recommend now",
    "confidence": 0.0,
    "changesRequired": ["What would need to change"],
    "impactAreas": ["Areas affected"]
  },
  "comparison": {
    "originalDecision": "What we decided",
    "revisedRecommendation": "What we'd decide now",
    "alignment": "same | modified | reversed",
    "keyDifferences": ["Main changes in thinking"]
  }
}
```

### Step 6: Report and Advise

```markdown
## Reconsideration Complete

**Original Decision:** [original]
**Revised Recommendation:** [proposed]
**Alignment:** [same/modified/reversed]

**Key Differences:**
- [difference 1]
- [difference 2]

**Sandbox File:** docs/reasoning/sandbox/YYYY-MM-DD-{topic}-recon.json

---

### Next Steps

To understand impact of changing:
```
/analyze-impact YYYY-MM-DD-{topic}-recon
```

To incorporate into active planning:
```
/promote-reconsideration YYYY-MM-DD-{topic}-recon --to-plan
```

**Note:** This analysis is isolated. No active plans or logs were modified.
```

---

## With Personas

When using `--run-personas`:

1. **Frame the question:**
   "Given [original decision] and [changed context], should we reconsider?"

2. **Run appropriate orchestrator:**
   - Product decisions: `/review-product-decision`
   - Research questions: `/review-research`
   - Business decisions: `/review-business-decision`

3. **Capture contributions:**
   Store in `personaContributions` array

4. **Note conflicts:**
   If personas now recommend differently than original

---

## Comparison Outcomes

### Same
Original decision still valid with current information.
```
alignment: "same"
keyDifferences: ["Confidence increased due to validation"]
```

### Modified
Original direction correct, but approach needs adjustment.
```
alignment: "modified"
keyDifferences: ["Same database, but different indexing strategy"]
```

### Reversed
Original decision should be changed.
```
alignment: "reversed"
keyDifferences: ["Would now choose MongoDB over PostgreSQL"]
```

---

## Safety Rails

### What This Command Does NOT Do

- Modify original decision entries
- Update active reasoning logs
- Change SESSION-STATE
- Alter any plans or roadmaps
- Trigger automatic updates

### What Requires Explicit Action

- `/analyze-impact` to understand consequences
- `/promote-reconsideration` to move to active
- Manual updates to code/docs if decision changes

---

## Examples

### Example 1: Simple Reconsideration

**Input:**
```
/reconsider-decision "caching strategy"
```

**Output:**
```markdown
## Original Decision

**ID:** 2026-01-05-e5f6g7h8
**Date:** 2026-01-05
**Decision Point:** What caching strategy should we use?

**What We Decided:** Use Redis for session caching

**Original Rationale:** Need fast access for session data, Redis is industry standard.

**Confidence:** 0.45 (low - no production data)

---

Why are you reconsidering this decision?
> [User selects: New information available]

What new information do we have?
> [User: We now have production metrics showing 95% of sessions are < 1KB and read-once]

---

## Revised Analysis

Given the new information that sessions are small and read-once:
- Redis may be over-engineered
- In-memory cache on app server could suffice
- Simpler architecture, fewer moving parts

**Revised Recommendation:** Use in-memory LRU cache
**Confidence:** 0.75
**Alignment:** Reversed

**Sandbox File:** docs/reasoning/sandbox/2026-01-06-caching-recon.json
```

### Example 2: With Personas

**Input:**
```
/reconsider-decision 2026-01-03-abc123 --run-personas
```

Runs full persona analysis on the original decision with current context, stores results in sandbox.
