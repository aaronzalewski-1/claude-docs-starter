---
name: audit-reasoning
description: Check data quality of reasoning logs and index health. Identifies missing fields, orphaned dependencies, index sync issues, and stale sandbox entries. Use --fix to repair issues.
---

# Audit Reasoning

Check and repair the health of the reasoning capture system.

## Command Format

```
/audit-reasoning [--fix]
```

**Arguments:**
- `--fix`: Automatically repair fixable issues (rebuild index, etc.)

**Examples:**
```
/audit-reasoning
/audit-reasoning --fix
```

---

## What Gets Audited

### 1. Data Quality
- Entries missing required fields
- Invalid schema versions
- Malformed JSON

### 2. Dependency Integrity
- Orphaned dependency references (point to non-existent entries)
- Circular dependencies
- Missing reverse links

### 3. Index Health
- Index entry count vs actual entries
- Missing entries in index
- Stale entries (in index but deleted)
- Topic classification accuracy

### 4. Sandbox Status
- Sandbox entries older than 30 days (stale)
- Promoted entries still in sandbox
- Incomplete reconsiderations

---

## Process

### Step 1: Load All Data

1. Read `docs/reasoning/index.json`
2. Glob all `docs/reasoning/YYYY-MM-DD-reasoning-log.json` files
3. Glob all `docs/reasoning/sandbox/*.json` files
4. Build in-memory map of all entries

### Step 2: Check Data Quality

For each entry, verify:

**Required fields:**
- `schemaVersion`
- `id`
- `timestamp`
- `trigger.type`
- `reasoning.decisionPoint`
- `reasoning.rationale`
- `dependsOn` (can be empty array)
- `outcome.decision`

**Record issues:**
```json
{
  "entryId": "2026-01-03-abc123",
  "issues": ["missing: dependsOn", "missing: outcome.decision"]
}
```

### Step 3: Check Dependencies

For each entry with `dependsOn`:
1. Verify each referenced ID exists
2. Check for circular references
3. Note orphaned references

### Step 4: Check Index Sync

Compare index to actual entries:

**In index but not in files:** Stale index entries
**In files but not in index:** Missing from index
**Count mismatch:** Index `totalEntries` wrong

### Step 5: Check Sandbox

For each sandbox entry:
1. Calculate age (days since `reconsiderationDate`)
2. Check `status` field
3. Verify `originalDecisionId` exists
4. Check for completeness

---

## Output Format

```markdown
## Reasoning Audit Report

**Audit Date:** [timestamp]
**Total Active Entries:** [count]
**Total Sandbox Entries:** [count]

---

### Data Quality

| Status | Count |
|--------|-------|
| Valid entries | [n] |
| Entries with issues | [n] |

**Issues Found:**

| Entry ID | Date | Issues |
|----------|------|--------|
| [id] | [date] | Missing: dependsOn |
| [id] | [date] | Invalid schema version |

---

### Dependency Integrity

| Status | Count |
|--------|-------|
| Valid dependencies | [n] |
| Orphaned references | [n] |
| Circular dependencies | [n] |

**Orphaned References:**

| Entry | References | Status |
|-------|------------|--------|
| [id] | [missing-id] | Target not found |

---

### Index Health

| Metric | Index | Actual | Status |
|--------|-------|--------|--------|
| Total entries | [n] | [n] | [OK/MISMATCH] |
| Topic coverage | [n] | [n] | [OK/INCOMPLETE] |
| Confidence mapping | [n] | [n] | [OK/INCOMPLETE] |

**Sync Issues:**

- Missing from index: [count] entries
- Stale in index: [count] entries

**Missing Entries:**
- [id] ([date]) - not in index

---

### Sandbox Status

| Status | Count |
|--------|-------|
| Active reconsiderations | [n] |
| Promoted | [n] |
| Stale (>30 days) | [n] |

**Stale Sandbox Entries:**

| Entry | Age | Original Decision |
|-------|-----|-------------------|
| [id] | [n] days | [original] |

**Recommendation:** Review or clean up stale entries.

---

### Summary

| Category | Status |
|----------|--------|
| Data Quality | [OK/ISSUES] |
| Dependencies | [OK/ISSUES] |
| Index Sync | [OK/OUT OF SYNC] |
| Sandbox | [OK/NEEDS ATTENTION] |

**Overall Health:** [HEALTHY/NEEDS ATTENTION/CRITICAL]

---

### Recommendations

[If issues found:]
1. Run `/audit-reasoning --fix` to rebuild index
2. Review entries with missing fields
3. Clean up stale sandbox entries
4. Verify orphaned dependency references

[If healthy:]
System is healthy. No action needed.
```

---

## Fix Mode

When `--fix` is specified:

### Auto-fixable Issues

1. **Rebuild index:**
   - Scan all log files
   - Extract entries and metadata
   - Rebuild `byTopic`, `byConfidence`, `dependencyGraph`
   - Update `totalEntries` and `lastUpdated`

2. **Remove stale index entries:**
   - Remove references to deleted entries

3. **Add missing `dependsOn`:**
   - Add empty array `[]` if field missing

### Manual-fix Required

1. **Orphaned dependencies:**
   - Report but don't auto-remove (may indicate data loss)

2. **Invalid schema versions:**
   - Report for manual migration

3. **Stale sandbox entries:**
   - Report but don't auto-delete (user decision)

---

## Fix Output

```markdown
## Audit Fix Report

**Actions Taken:**

### Index Rebuilt
- Scanned [n] log files
- Found [n] entries
- Updated topic mappings for [n] entries
- Updated confidence mappings for [n] entries
- Rebuilt dependency graph with [n] edges

### Fields Added
- Added missing `dependsOn` to [n] entries

### Issues Remaining (Manual Fix Required)

| Issue | Count | Action Needed |
|-------|-------|---------------|
| Orphaned dependencies | [n] | Review and update manually |
| Invalid schema | [n] | Run migration |
| Stale sandbox | [n] | Review and promote/delete |

---

**Index Status:** Rebuilt successfully
**File:** docs/reasoning/index.json
```

---

## Scheduled Audits

Recommend running audit:
- Weekly during active development
- After any manual edits to reasoning files
- Before major decision reviews
- When queries return unexpected results

---

## Examples

### Example 1: Check Health

**Input:**
```
/audit-reasoning
```

**Output:**
```markdown
## Reasoning Audit Report

**Audit Date:** 2026-01-06T15:00:00Z
**Total Active Entries:** 47
**Total Sandbox Entries:** 3

---

### Data Quality

| Status | Count |
|--------|-------|
| Valid entries | 45 |
| Entries with issues | 2 |

**Issues Found:**

| Entry ID | Date | Issues |
|----------|------|--------|
| 2026-01-03-abc123 | 2026-01-03 | Missing: dependsOn |
| 2026-01-04-def456 | 2026-01-04 | Missing: outcome.confidence |

---

### Index Health

| Metric | Index | Actual | Status |
|--------|-------|--------|--------|
| Total entries | 45 | 47 | MISMATCH |

**Missing from index:** 2 entries

---

### Summary

**Overall Health:** NEEDS ATTENTION

**Recommendations:**
1. Run `/audit-reasoning --fix` to rebuild index
2. Review 2 entries with missing fields
```

### Example 2: Fix Issues

**Input:**
```
/audit-reasoning --fix
```

**Output:**
```markdown
## Audit Fix Report

**Actions Taken:**

### Index Rebuilt
- Scanned 12 log files
- Found 47 entries
- Updated topic mappings
- Rebuilt dependency graph

### Fields Added
- Added missing `dependsOn` to 2 entries

---

**Index Status:** Rebuilt successfully
**Overall Health:** HEALTHY
```
