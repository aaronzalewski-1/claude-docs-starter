# Decision Reasoning Capture

> Capture, query, visualize, and reconsider decision-making processes.

This system complements formal artifacts (ADRs, Literature Reviews, Board Memos) by capturing the informal reasoning that those documents miss - the "why" behind incremental decisions, rejected alternatives, and underlying assumptions.

---

## Directory Structure

```
docs/reasoning/
├── README.md                           # This file
├── index.json                          # Fast lookup index (topic, confidence, dependencies)
├── YYYY-MM-DD-reasoning-log.json       # Daily reasoning entries
└── sandbox/                            # Isolated reconsideration analyses
    └── YYYY-MM-DD-{topic}-recon.json   # Sandbox entries (never auto-merged)
```

---

## Quick Start

### Capture a Decision

```
/capture-reasoning "Why we chose PostgreSQL over MongoDB"
```

Or with depth control:
```
/capture-reasoning "Authentication approach" --depth full
```

### Query Past Decisions

```
/query-decisions Why did we choose Redis?
/query-decisions What assumptions did we make about scaling?
/query-decisions Which decisions had low confidence?
```

### Visualize Decision History

```
/visualize-decisions last-week --view events --format mermaid
/visualize-decisions "authentication" --view roles --format ascii
```

### Reconsider a Decision (Isolated)

```
/reconsider-decision "2026-01-03-abc123" --run-personas
```

### Analyze Impact Before Changing

```
/analyze-impact "2026-01-03-abc123" --if-changed "Use MongoDB instead"
```

### Promote to Active Planning

```
/promote-reconsideration "2026-01-06-auth-recon" --to-plan
```

---

## Entry Schema

Each reasoning entry captures:

```json
{
  "schemaVersion": "1.0.0",
  "id": "2026-01-06-a1b2c3d4",
  "timestamp": "2026-01-06T14:30:00Z",
  "trigger": {
    "type": "explicit_capture",
    "milestone": "Architecture decision",
    "source": "/capture-reasoning"
  },
  "context": {
    "task": "Implementing user authentication",
    "phase": "Design",
    "relatedFiles": ["src/auth/", "docs/CLAUDE/ARCHITECTURE.md"]
  },
  "reasoning": {
    "decisionPoint": "Which database to use for user sessions?",
    "rationale": "PostgreSQL provides ACID guarantees needed for auth data...",
    "alternatives": [
      {
        "option": "MongoDB",
        "rejectionReason": "Eventually consistent model risky for auth",
        "pros": ["Flexible schema", "Easy horizontal scaling"],
        "cons": ["No ACID", "Overkill for structured auth data"]
      }
    ],
    "assumptions": [
      {
        "assumption": "User count will stay under 100K for year 1",
        "validated": false,
        "risk": "medium"
      }
    ],
    "evidence": [
      {
        "claim": "PostgreSQL handles 10K concurrent connections",
        "source": "PostgreSQL documentation",
        "sourceType": "documentation",
        "confidence": 0.9
      }
    ],
    "tradeoffs": [
      {
        "tradeoff": "Less flexible schema",
        "acceptedRisk": "May need migrations for schema changes",
        "mitigation": "Use JSONB columns for extensible fields"
      }
    ]
  },
  "dependsOn": [],
  "personaContributions": [],
  "outcome": {
    "decision": "Use PostgreSQL for user sessions",
    "confidence": 0.85,
    "nextSteps": ["Set up PostgreSQL instance", "Design session schema"],
    "revisitTriggers": ["If user count exceeds 100K", "If write throughput becomes bottleneck"]
  },
  "linkedArtifacts": {
    "adr": null,
    "sessionState": "docs/CLAUDE/SESSION-STATE.json"
  }
}
```

---

## Capture Depths

| Depth | When to Use | Fields Included |
|-------|-------------|-----------------|
| **full** | Major architectural decisions, persona analyses | All fields, detailed alternatives |
| **standard** | Regular implementation decisions | Core fields, top 2-3 alternatives, key assumptions |
| **light** | Pre-commit rationale, minor choices | Decision + rationale only |

---

## Index Structure

The `index.json` file enables fast lookup at scale (100+ decisions):

```json
{
  "schemaVersion": "1.0.0",
  "lastUpdated": "2026-01-06T14:30:00Z",
  "totalEntries": 127,
  "byTopic": {
    "authentication": ["2026-01-03-abc123", "2026-01-05-def456"],
    "database": ["2026-01-02-jkl012"]
  },
  "byConfidence": {
    "high": ["entries with confidence >= 0.8"],
    "medium": ["entries with confidence 0.5-0.79"],
    "low": ["entries with confidence < 0.5"]
  },
  "dependencyGraph": {
    "2026-01-05-def456": ["2026-01-03-abc123"]
  }
}
```

---

## Sandbox Rules

The `sandbox/` directory contains isolated reconsideration analyses:

1. **Never auto-merged** - Only `/promote-reconsideration` moves content to active planning
2. **Distinct naming** - Files end in `-recon.json` (vs `-log.json` for active)
3. **Status field** - Every sandbox entry has `"status": "sandbox"`
4. **Read isolation** - Query and visualize commands ignore sandbox by default

---

## Visualization Views

| View | Purpose | Best For |
|------|---------|----------|
| `process` | Decision workflow: trigger → analysis → outcome | Understanding how a decision was made |
| `roles` | Persona contributions and conflicts | Seeing which perspectives influenced decisions |
| `events` | Timeline with dependencies | Tracing decision chains and causality |

**Filtering options:**
- `--filter topic:auth` - Only decisions on a topic
- `--filter confidence:>0.7` - Only high-confidence decisions
- `--filter has-dependencies` - Only decisions with explicit dependencies
- `--limit 20` - Cap output entries

---

## Data Quality

Run periodic audits:

```
/audit-reasoning
```

Checks for:
- Missing required fields
- Orphaned dependency references
- Index out of sync
- Stale sandbox entries (>30 days)

Fix issues:
```
/audit-reasoning --fix
```

---

## Integration Points

### With Formal Artifacts
- Reasoning entries can link to ADRs via `linkedArtifacts.adr`
- Use `--save` on review commands for formal documentation
- Reasoning captures the "messy middle" that ADRs formalize

### With SESSION-STATE.json
- `reasoningContext` section tracks daily log file and captured decisions
- `keyDecisions` entries link to reasoning via `reasoningEntryId`

### With Persona System
- After `/review-*-decision` commands, reasoning is auto-captured
- `personaContributions` field stores persona findings and confidence scores

---

## Commands Reference

| Command | Purpose |
|---------|---------|
| `/capture-reasoning` | Explicitly capture decision reasoning |
| `/query-decisions` | Natural language search of past decisions |
| `/visualize-decisions` | Generate process/roles/events diagrams |
| `/reconsider-decision` | Re-evaluate a past decision in sandbox |
| `/analyze-impact` | Understand ripple effects of changing a decision |
| `/promote-reconsideration` | Move sandbox analysis to active planning |
| `/audit-reasoning` | Check data quality and index health |
