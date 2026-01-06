---
name: capture-reasoning
description: Explicitly capture decision reasoning to the reasoning log. Use when you want to document the rationale behind a significant decision, including alternatives considered and assumptions made.
---

# Capture Reasoning

Explicitly capture decision reasoning for the current context.

## Command Format

```
/capture-reasoning <decision or context> [--depth full|standard|light]
```

**Arguments:**
- `decision`: The decision point or context to capture
- `--depth`: Capture depth (default: standard)
  - `full`: All fields, detailed alternatives, evidence, persona contributions
  - `standard`: Core fields, top alternatives, key assumptions
  - `light`: Decision + rationale only (for pre-commit or minor decisions)

**Examples:**
```
/capture-reasoning Why we chose PostgreSQL over MongoDB
/capture-reasoning Authentication approach --depth full
/capture-reasoning Pre-commit: Added input validation --depth light
```

---

## Process

### Step 1: Identify Decision Point

Restate the decision clearly:
- What question was being answered?
- What context led to this decision point?

Ask if unclear:
> What specific decision are you documenting?

### Step 2: Gather Core Information

**Always collect:**
1. **Decision Point**: The question being answered
2. **Rationale**: Why this choice was made (1-3 sentences)
3. **Final Decision**: The conclusion reached

### Step 3: Prompt for Dependencies

**CRITICAL - Always ask:**

```
Does this decision depend on any previous decisions?
- [Y] Yes - I'll search for related decisions
- [N] No - This is independent
- [S] Skip - I'll add dependencies later
```

**If Yes:**
1. Read `docs/reasoning/index.json`
2. Search `byTopic` for related keywords
3. Present matching entries:
   ```
   Found related decisions:
   1. 2026-01-03-abc123: "Database selection for user data"
   2. 2026-01-04-def456: "Caching strategy"

   Which decisions does this depend on? (comma-separated numbers, or 'none')
   ```
4. Add selected IDs to `dependsOn` array

### Step 4: Gather Depth-Specific Information

**For `standard` and `full` depth:**

Ask about alternatives:
> What alternatives did you consider? Why were they rejected?

Ask about assumptions:
> What assumptions is this decision based on? Are any unvalidated?

Ask about tradeoffs:
> What tradeoffs are you accepting with this decision?

**For `full` depth only:**

Ask about evidence:
> What evidence or sources informed this decision?

Include persona contributions if recent analysis exists.

### Step 5: Generate Entry

Create the JSON entry following the schema in `reasoning-capture.skill.md`.

**Entry ID Format:** `YYYY-MM-DD-{8-char-random}`

Example: `2026-01-06-a1b2c3d4`

### Step 6: Write to Daily Log

1. Determine today's log file: `docs/reasoning/YYYY-MM-DD-reasoning-log.json`
2. If file exists, read and append to `entries` array
3. If file doesn't exist, create with structure:
   ```json
   {
     "date": "YYYY-MM-DD",
     "schemaVersion": "1.0.0",
     "entries": []
   }
   ```
4. Append new entry
5. Write file

### Step 7: Update Index

1. Read `docs/reasoning/index.json`
2. Increment `totalEntries`
3. Update `lastUpdated` to current ISO timestamp
4. Extract topics from decision (keywords from decisionPoint, file paths)
5. Add entry ID to relevant `byTopic` arrays
6. Add to `byConfidence.high/medium/low` based on confidence score:
   - high: >= 0.8
   - medium: 0.5-0.79
   - low: < 0.5
7. If `dependsOn` is populated, update `dependencyGraph`
8. Add entry ID to `entries` array
9. Write index

### Step 8: Confirm Capture

Report:

```markdown
## Reasoning Captured

**Decision:** [decision point summary]
**Entry ID:** [id]
**File:** docs/reasoning/YYYY-MM-DD-reasoning-log.json

**Summary:**
- Alternatives documented: X
- Assumptions recorded: Y
- Dependencies linked: Z

**Index Updated:**
- Topics: [extracted topics]
- Confidence: [high/medium/low]
```

---

## Depth Guidelines

### Light Depth

Use for:
- Pre-commit rationale
- Minor implementation choices
- Well-understood decisions

Captures:
- Decision point
- Rationale (1-2 sentences)
- Final decision

### Standard Depth (Default)

Use for:
- Regular implementation decisions
- Architecture choices
- Technology selections

Captures:
- Full context
- Top 2-3 alternatives with rejection reasons
- Key assumptions with validation status
- Accepted tradeoffs
- Confidence score
- Revisit triggers

### Full Depth

Use for:
- Major architectural decisions
- After persona analyses
- Decisions with significant uncertainty
- Decisions others will need to understand

Captures:
- Everything in standard
- Detailed evidence with sources
- Persona contributions (if applicable)
- Linked artifacts

---

## Integration

### With Recent Persona Analysis

If a `/review-*-decision` command was recently run:
- Auto-populate `personaContributions` from analysis
- Use weighted consensus confidence
- Link to ADR if `--save` was used

### With SESSION-STATE

After capture, update SESSION-STATE.json if it exists:
- Increment `reasoningContext.capturedDecisions`
- Add unvalidated assumptions to `unvalidatedAssumptions`
- Add revisit triggers to `pendingRevisitTriggers`

---

## Examples

### Example 1: Database Decision (Standard)

```
/capture-reasoning Why we chose PostgreSQL for session storage
```

**Output Entry:**
```json
{
  "schemaVersion": "1.0.0",
  "id": "2026-01-06-a1b2c3d4",
  "timestamp": "2026-01-06T10:30:00Z",
  "trigger": {
    "type": "explicit_capture",
    "milestone": "Database technology selection",
    "source": "/capture-reasoning"
  },
  "context": {
    "task": "Implementing user session management",
    "phase": "Design",
    "relatedFiles": ["src/auth/session.ts"]
  },
  "reasoning": {
    "decisionPoint": "Which database to use for user session storage?",
    "rationale": "PostgreSQL provides ACID guarantees critical for auth data, and we already have PostgreSQL expertise on the team.",
    "alternatives": [
      {
        "option": "Redis",
        "rejectionReason": "Adds operational complexity; sessions don't need sub-ms latency",
        "pros": ["Fast", "Built for sessions"],
        "cons": ["Another system to manage", "Persistence config complexity"]
      },
      {
        "option": "MongoDB",
        "rejectionReason": "Eventual consistency unacceptable for auth data",
        "pros": ["Flexible schema"],
        "cons": ["No ACID", "Overkill for structured data"]
      }
    ],
    "assumptions": [
      {
        "assumption": "Session read/write volume will stay under 1000/sec",
        "validated": false,
        "risk": "medium"
      }
    ],
    "tradeoffs": [
      {
        "tradeoff": "Slightly higher latency than Redis",
        "acceptedRisk": "May need optimization if latency becomes issue",
        "mitigation": "Can add Redis cache layer later if needed"
      }
    ]
  },
  "dependsOn": [],
  "outcome": {
    "decision": "Use PostgreSQL for session storage",
    "confidence": 0.85,
    "nextSteps": ["Design session schema", "Implement session repository"],
    "revisitTriggers": ["If session latency exceeds 50ms p99", "If volume exceeds 1000/sec"]
  }
}
```

### Example 2: Pre-commit (Light)

```
/capture-reasoning Added rate limiting to login endpoint --depth light
```

**Output Entry:**
```json
{
  "schemaVersion": "1.0.0",
  "id": "2026-01-06-e5f6g7h8",
  "timestamp": "2026-01-06T14:45:00Z",
  "trigger": {
    "type": "explicit_capture",
    "milestone": "Pre-commit rationale",
    "source": "/capture-reasoning --depth light"
  },
  "reasoning": {
    "decisionPoint": "Should we add rate limiting to login?",
    "rationale": "Prevents brute force attacks; standard security practice."
  },
  "dependsOn": [],
  "outcome": {
    "decision": "Added 5 attempts per minute rate limit to login endpoint"
  }
}
```

---

## Error Handling

### If Daily Log Write Fails
- Report error to user
- Suggest manual retry
- Do not update index

### If Index Update Fails
- Log entry is still valid
- Warn user index may be out of sync
- Suggest `/audit-reasoning --fix` to rebuild

### If Dependencies Can't Be Found
- Allow empty `dependsOn` array
- Warn that impact analysis may be incomplete
- Suggest reviewing and adding dependencies later
