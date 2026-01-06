---
name: query-decisions
description: Natural language search of past decisions in the reasoning log. Use when you need to understand why a decision was made, what alternatives were considered, or what assumptions underlie past choices.
---

# Query Decisions

Search and synthesize answers from past decision reasoning using natural language.

## Command Format

```
/query-decisions <natural language question>
```

**Examples:**
```
/query-decisions Why did we choose PostgreSQL?
/query-decisions What assumptions did we make about authentication?
/query-decisions Which decisions had low confidence?
/query-decisions What alternatives did we consider for caching?
/query-decisions Show me all database-related decisions
```

---

## Process

### Step 1: Parse Query Intent

Identify what the user is looking for:

| Query Type | Pattern | Action |
|------------|---------|--------|
| **Why** | "Why did we...", "What led to..." | Find decision + rationale |
| **What** | "What did we decide about...", "What assumptions..." | Find specific fields |
| **Which** | "Which decisions...", "Which had..." | Filter by criteria |
| **Alternatives** | "What alternatives...", "What else did we consider..." | Extract alternatives array |
| **Dependencies** | "What depends on...", "What led to..." | Trace dependency graph |

### Step 2: Read Index for Fast Lookup

1. Read `docs/reasoning/index.json`
2. Extract search keywords from query
3. Find matching entry IDs in `byTopic`
4. If confidence-based query, use `byConfidence`
5. If dependency query, use `dependencyGraph`

### Step 3: Load Relevant Entries

1. For each matching entry ID:
   - Determine date from ID prefix (YYYY-MM-DD)
   - Read from `docs/reasoning/YYYY-MM-DD-reasoning-log.json`
   - Extract matching entry from `entries` array
2. If no index matches, fall back to full scan of recent logs

### Step 4: Synthesize Answer

Compose answer based on query type:

**For "Why" queries:**
```markdown
## Why We Chose [X]

**Decision:** [decisionPoint]
**Date:** [timestamp]

**Rationale:**
[reasoning.rationale]

**Key Factors:**
- [evidence items]
- [tradeoffs accepted]

**Assumptions Made:**
- [assumption 1] (validated/unvalidated)
- [assumption 2]

**Source:** Entry [id] from [date]
```

**For "What alternatives" queries:**
```markdown
## Alternatives Considered for [Topic]

### [Decision 1]
**Chose:** [outcome.decision]

**Rejected:**
1. **[alternative.option]**
   - Why rejected: [rejectionReason]
   - Pros: [pros]
   - Cons: [cons]

2. **[alternative.option]**
   ...

**Source:** Entry [id] from [date]
```

**For "Which decisions" queries:**
```markdown
## Decisions Matching: [criteria]

| Date | Decision | Confidence | Topic |
|------|----------|------------|-------|
| [date] | [decisionPoint] | [confidence] | [topic] |
| ... | ... | ... | ... |

**Total:** X decisions found
```

### Step 5: Include Source References

Always end with:
```markdown
---
**Sources:**
- Entry [id]: [brief description] ([date])
- Entry [id]: [brief description] ([date])
```

---

## Query Types

### Finding Specific Decisions

```
/query-decisions Why did we choose Redis for caching?
```

1. Search index for "redis", "caching"
2. Load matching entries
3. Return decision + rationale + alternatives

### Finding Assumptions

```
/query-decisions What assumptions did we make about user scale?
```

1. Search for "scale", "user"
2. Extract all `assumptions` arrays from matches
3. Group by validated/unvalidated
4. Return with risk levels

### Finding Low-Confidence Decisions

```
/query-decisions Which decisions had low confidence?
```

1. Read `index.byConfidence.low`
2. Load all matching entries
3. Return table with confidence scores

### Tracing Dependencies

```
/query-decisions What decisions depend on our auth choice?
```

1. Find auth-related decision ID
2. Search `dependencyGraph` for entries that reference it
3. Return dependency chain

### Recent Decisions

```
/query-decisions What decisions did we make this week?
```

1. Calculate date range
2. Read relevant daily log files
3. Return chronological list

---

## Output Formats

### Detailed (Default)

Full context including rationale, alternatives, assumptions.

### Summary

```
/query-decisions What did we decide about databases? --summary
```

Just decision points and dates, no details.

### Table

```
/query-decisions Show all decisions --table
```

Tabular format for overview.

---

## Scope Control

### By Date Range

```
/query-decisions decisions from January 2026
/query-decisions decisions in the last 7 days
```

### By Topic

```
/query-decisions all authentication decisions
/query-decisions database decisions
```

### By Confidence

```
/query-decisions high confidence decisions
/query-decisions decisions we were uncertain about
```

---

## Important: Sandbox Exclusion

**NEVER include entries from `docs/reasoning/sandbox/`**

Sandbox contains isolated reconsiderations that are NOT active decisions.
Only query from `docs/reasoning/YYYY-MM-DD-reasoning-log.json` files.

---

## Error Handling

### No Matches Found

```markdown
## No Decisions Found

No reasoning entries match your query for "[search terms]".

**Suggestions:**
- Try broader search terms
- Check if decisions were captured (run `/audit-reasoning`)
- The decision may predate reasoning capture

**Available topics in index:**
- [list byTopic keys]
```

### Empty Reasoning Log

```markdown
## No Reasoning History

The reasoning log is empty. Decisions haven't been captured yet.

**To start capturing:**
- Use `/capture-reasoning <decision>` for explicit capture
- Decisions will be auto-captured at milestones per CLAUDE.md directive
```

---

## Examples

### Example 1: Why Query

**Input:**
```
/query-decisions Why did we choose PostgreSQL over MongoDB?
```

**Output:**
```markdown
## Why We Chose PostgreSQL Over MongoDB

**Decision:** Which database to use for user data storage?
**Date:** 2026-01-03

**Rationale:**
PostgreSQL provides ACID guarantees critical for user data integrity.
Our team already has PostgreSQL expertise, reducing onboarding time.

**Alternatives Rejected:**
1. **MongoDB**
   - Why rejected: Eventual consistency unacceptable for auth data
   - Pros: Flexible schema, horizontal scaling
   - Cons: No ACID, operational complexity

**Assumptions:**
- User count stays under 100K year 1 (unvalidated, medium risk)
- Read-heavy workload (validated via analytics)

**Confidence:** 0.85

---
**Source:** Entry 2026-01-03-a1b2c3d4
```

### Example 2: List Query

**Input:**
```
/query-decisions Which decisions had low confidence?
```

**Output:**
```markdown
## Low Confidence Decisions (< 0.5)

| Date | Decision | Confidence | Key Uncertainty |
|------|----------|------------|-----------------|
| 2026-01-04 | Caching strategy | 0.45 | Unknown traffic patterns |
| 2026-01-05 | Rate limiting thresholds | 0.40 | No production data yet |

**Recommendation:** Consider revisiting these decisions once more data is available.

---
**Sources:**
- Entry 2026-01-04-e5f6g7h8
- Entry 2026-01-05-i9j0k1l2
```
