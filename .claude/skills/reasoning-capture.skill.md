---
name: reasoning-capture
description: >
  Framework for capturing decision reasoning at milestones.
  MUST use for: reasoning capture, decision documentation, session recovery.
  Triggers: capture reasoning, why did we, decision history, reasoning log, decision point.
type: skill
version: 1.0.0
---

# Reasoning Capture Skill

> Framework for capturing informal decision reasoning that complements formal artifacts (ADRs, Literature Reviews, Board Memos).

---

## Purpose

Formal artifacts capture final decisions. This system captures:
- **Intermediate reasoning** - How we got to the decision
- **Rejected alternatives** - What we considered and why we said no
- **Assumptions** - What we're betting on being true
- **Evidence trail** - What informed our thinking
- **Tradeoffs** - What we knowingly sacrificed
- **Dependencies** - Which prior decisions this builds on

---

## Capture Triggers

### Explicit Triggers
| Trigger | Depth | Notes |
|---------|-------|-------|
| `/capture-reasoning` command | User-specified | Default: standard |
| User says "capture this decision" | standard | Recognize intent |

### Implicit Triggers (via CLAUDE.md directive)
| Milestone | Depth | What to Capture |
|-----------|-------|-----------------|
| After persona analysis | full | Consensus, tensions, persona contributions |
| Plan approval | standard | Approach chosen, scope, deferrals |
| Pre-commit | light | Change rationale, key assumption |
| After `/REFOCUS` | standard | Hypothesis evolution, root cause |
| Significant decision point | standard | When making architectural/implementation choices |

### Decision Point Recognition

Recognize decision-making language:
- "Let's go with X because..."
- "I recommend X over Y because..."
- "After considering the options, we should..."
- "The tradeoff is acceptable because..."
- Choosing between mutually exclusive options

---

## Entry Structure

### Required Fields (All Depths)

```json
{
  "schemaVersion": "1.0.0",
  "id": "YYYY-MM-DD-{shortId}",
  "timestamp": "ISO 8601",
  "trigger": {
    "type": "explicit_capture | persona_completion | plan_approval | pre_commit | refocus | decision_point",
    "milestone": "Human-readable description",
    "source": "Command or context that triggered"
  },
  "reasoning": {
    "decisionPoint": "What question were we answering?",
    "rationale": "Why this answer?"
  },
  "dependsOn": [],
  "outcome": {
    "decision": "The final decision made"
  }
}
```

### Standard Depth (Add These)

```json
{
  "context": {
    "task": "Current task",
    "phase": "Workflow phase",
    "relatedFiles": []
  },
  "reasoning": {
    "alternatives": [
      {
        "option": "Alternative considered",
        "rejectionReason": "Why rejected",
        "pros": [],
        "cons": []
      }
    ],
    "assumptions": [
      {
        "assumption": "What we're assuming",
        "validated": false,
        "risk": "low | medium | high"
      }
    ],
    "tradeoffs": [
      {
        "tradeoff": "What we sacrificed",
        "acceptedRisk": "Risk we accepted",
        "mitigation": "How we mitigate"
      }
    ]
  },
  "outcome": {
    "confidence": 0.0-1.0,
    "nextSteps": [],
    "revisitTriggers": []
  }
}
```

### Full Depth (Add These)

```json
{
  "reasoning": {
    "evidence": [
      {
        "claim": "Factual claim",
        "source": "Where from",
        "sourceType": "documentation | codebase | persona_analysis | user_input | external_reference",
        "confidence": 0.0-1.0
      }
    ]
  },
  "personaContributions": [
    {
      "persona": "Persona name",
      "keyFinding": "Main insight",
      "confidence": 0.0-1.0,
      "recommendations": []
    }
  ],
  "linkedArtifacts": {
    "adr": "Path to ADR if exists",
    "sessionState": "Path to SESSION-STATE.json"
  }
}
```

---

## Dependency Handling

### CRITICAL: Always Ask About Dependencies

During capture, ALWAYS prompt:

```
Does this decision depend on any previous decisions?
- [Y] Yes - I'll search for related decisions
- [N] No - This is independent
- [S] Skip - I'll add dependencies later
```

If Yes:
1. Read `docs/reasoning/index.json`
2. Search `byTopic` for related entries
3. Present matches for user selection
4. Add selected IDs to `dependsOn` array

### Why This Matters

- Impact analysis requires complete dependency graph
- "Garbage in, garbage out" - incomplete links break `/analyze-impact`
- `dependsOn` field is REQUIRED (can be empty `[]`, but must be explicit)

---

## Index Management

### On Each Capture

After writing entry to daily log:

1. Read `docs/reasoning/index.json`
2. Update `totalEntries`
3. Update `lastUpdated`
4. Add entry ID to appropriate `byTopic` arrays (extract from decisionPoint/context)
5. Add to `byConfidence` based on `outcome.confidence`
6. Update `dependencyGraph` if `dependsOn` is populated
7. Add to `entries` array
8. Write updated index

### Topic Extraction

Extract topics from:
- Keywords in `reasoning.decisionPoint`
- File paths in `context.relatedFiles`
- Explicit tags if provided

Common topics: authentication, database, caching, api, frontend, testing, deployment, security

---

## Storage Locations

| File | Purpose |
|------|---------|
| `docs/reasoning/YYYY-MM-DD-reasoning-log.json` | Daily active log |
| `docs/reasoning/index.json` | Fast lookup index |
| `docs/reasoning/sandbox/*.json` | Isolated reconsiderations |

### Daily Log Format

```json
{
  "date": "YYYY-MM-DD",
  "schemaVersion": "1.0.0",
  "entries": [
    { /* entry 1 */ },
    { /* entry 2 */ }
  ]
}
```

---

## Quality Criteria

### Good Entry
- **Specific** - Names the exact decision, not vague summary
- **Complete** - Includes alternatives seriously considered
- **Honest** - Acknowledges assumptions and uncertainties
- **Traceable** - Links to evidence and related artifacts
- **Connected** - `dependsOn` populated when applicable
- **Actionable** - Includes revisit triggers

### Poor Entry
- "We decided to use X" (no rationale)
- Lists one option (no alternatives)
- Claims 100% confidence (no acknowledged risks)
- Empty `dependsOn` when dependencies exist
- No link to source material

---

## Sandbox Rules

### NEVER Read Sandbox for Active Queries

When processing `/query-decisions` or `/visualize-decisions`:
- Read ONLY from `docs/reasoning/YYYY-MM-DD-reasoning-log.json` files
- NEVER include `docs/reasoning/sandbox/*.json` entries
- Sandbox is isolated by design

### Sandbox Entry Requirements

All sandbox entries MUST have:
- `"status": "sandbox"` field
- Filename ending in `-recon.json`
- `originalDecisionId` linking to source decision

---

## Integration

### With SESSION-STATE.json

```json
{
  "reasoningContext": {
    "dailyLogFile": "docs/reasoning/YYYY-MM-DD-reasoning-log.json",
    "capturedDecisions": 5,
    "unvalidatedAssumptions": ["assumption text"],
    "pendingRevisitTriggers": ["trigger text"]
  }
}
```

### With Persona System

After `/review-*-decision` commands:
1. Auto-capture with `trigger.type = "persona_completion"`
2. Populate `personaContributions` from analysis
3. Extract confidence from weighted consensus
4. Link to ADR if `--save` was used

### With DEEPPLAN Workflow

| Phase | Capture? |
|-------|----------|
| Phase 1-2: Investigate/Clarify | No (gathering, not deciding) |
| Phase 3: Plan | Capture if significant scoping decisions |
| Phase 4: Approve | Capture approval rationale |
| Phase 5: Implement | Light capture at commits |
| Phase 6: Document | Reference reasoning in CHANGELOG |

---

## Confidence Scoring Guide

| Score | Meaning | When to Use |
|-------|---------|-------------|
| 0.9-1.0 | High confidence | Verified facts, tested approaches |
| 0.7-0.8 | Moderate confidence | Reasonable assumptions, some unknowns |
| 0.5-0.6 | Low confidence | Significant unknowns, educated guess |
| < 0.5 | Very low | Speculative, needs validation |

---

## Recovery and Review

### Session Recovery

When starting a new session:
1. Read `docs/reasoning/index.json` for overview
2. Load recent entries for context
3. Check `pendingRevisitTriggers` in SESSION-STATE
4. Review unvalidated assumptions

### Decision Archaeology

When asking "why did we decide X?":
1. Search index `byTopic` for keywords
2. Load matching entries from daily logs
3. Follow `dependsOn` for context chain
4. Check `linkedArtifacts` for formal docs
