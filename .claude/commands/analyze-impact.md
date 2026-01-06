---
name: analyze-impact
description: Analyze the ripple effects of changing a decision. Shows dependency chains, affected artifacts, and effort estimates before committing to changes.
---

# Analyze Impact

Understand the consequences of changing a decision before committing to changes.

## Command Format

```
/analyze-impact <decision-id or sandbox-id> [--if-changed <new-choice>]
```

**Arguments:**
- `decision-id`: Active decision ID (e.g., `2026-01-03-abc123`)
- `sandbox-id`: Sandbox reconsideration ID (e.g., `2026-01-06-caching-recon`)
- `--if-changed`: Specify the alternative to analyze (optional)

**Examples:**
```
/analyze-impact 2026-01-03-abc123
/analyze-impact 2026-01-06-caching-recon
/analyze-impact 2026-01-03-abc123 --if-changed "Use MongoDB instead"
```

---

## What Impact Analysis Reveals

### 1. Dependency Graph
Which subsequent decisions depend on this one?

### 2. Assumption Cascade
Which assumptions in other decisions would be invalidated?

### 3. Artifact Impact
Which ADRs, code, or documentation would need updating?

### 4. Effort Estimate
Scope of changes required.

---

## Process

### Step 1: Load Decision

**For active decision:**
1. Parse ID and load from daily log
2. Get current outcome and assumptions

**For sandbox reconsideration:**
1. Load from `docs/reasoning/sandbox/`
2. Get both original and proposed outcome

### Step 2: Trace Dependencies

1. Read `docs/reasoning/index.json`
2. Search `dependencyGraph` for entries that reference this decision
3. Recursively trace downstream decisions
4. Build dependency tree

### Step 3: Analyze Assumption Cascade

For each downstream decision:
1. Check if any assumptions reference the decision being changed
2. Identify which assumptions would be invalidated
3. Assess risk level of each invalidation

### Step 4: Find Affected Artifacts

Search for artifacts that reference this decision:
1. ADRs in `docs/decisions/`
2. Code files mentioned in `context.relatedFiles`
3. Documentation that references the decision
4. SESSION-STATE if decision is active

### Step 5: Estimate Effort

Categorize impact:
- **Trivial:** Documentation update only
- **Minor:** 1-2 code files, no architecture change
- **Moderate:** Multiple files, possible interface changes
- **Major:** Architectural changes, multiple systems affected
- **Critical:** Foundational decision, widespread changes

### Step 6: Generate Report

---

## Output Format

```markdown
## Impact Analysis: [Decision Point]

**Decision ID:** [id]
**Current Outcome:** [outcome]
**Proposed Change:** [if --if-changed, show alternative]

---

### Downstream Dependencies

[X] decisions directly depend on this decision.

```
[This Decision]
├── Decision A (2026-01-04)
│   └── Decision C (2026-01-06)
└── Decision B (2026-01-05)
    └── Decision D (2026-01-07)
```

| Decision | Date | Dependency Type | Risk if Changed |
|----------|------|-----------------|-----------------|
| [title] | [date] | assumes [X] | High/Medium/Low |
| ... | ... | ... | ... |

---

### Assumption Cascade

**Assumptions that would be invalidated:**

| Decision | Assumption | Status | Impact |
|----------|------------|--------|--------|
| Decision A | "Database supports X" | Would be invalid | High |
| Decision B | "Latency under Y ms" | May be invalid | Medium |

**Decisions requiring re-evaluation:** [count]

---

### Affected Artifacts

**Code:**
- `src/services/cache.ts` - Implements current decision
- `src/config/database.ts` - Configuration based on decision

**Documentation:**
- `docs/decisions/product/2026-01-03-database/README.md` - ADR to supersede
- `docs/CLAUDE/ARCHITECTURE.md` - References decision

**Configuration:**
- `.env.example` - Environment variables

---

### Effort Estimate

**Impact Level:** [Trivial/Minor/Moderate/Major/Critical]

**Changes Required:**
- [ ] Update [X] code files
- [ ] Supersede [Y] ADR(s)
- [ ] Re-evaluate [Z] dependent decisions
- [ ] Update documentation
- [ ] Migration/data changes: [Yes/No]

**Estimated Scope:**
- Code changes: [description]
- Testing needed: [description]
- Documentation: [description]

---

### Recommendations

**If changing this decision:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Consider:**
- [Important consideration]
- [Risk to be aware of]

---

### If Changed To: [Alternative]

[Only if --if-changed provided]

**Specific impacts of choosing [alternative]:**
- [Impact 1]
- [Impact 2]

**Compatibility:**
- [What works]
- [What breaks]
```

---

## Dependency Types

### Direct Dependency
Decision B explicitly lists Decision A in `dependsOn`.

### Assumption Dependency
Decision B assumes something that depends on Decision A's outcome.

### Implicit Dependency
Decision B's context suggests reliance on Decision A, even if not explicit.

---

## Risk Assessment

### High Risk
- Foundational decision (many dependents)
- Active code relying on decision
- Assumptions deeply embedded in other decisions
- No easy migration path

### Medium Risk
- Some dependents exist
- Code changes required but contained
- Assumptions can be updated
- Clear migration path

### Low Risk
- Few or no dependents
- Mostly documentation changes
- Isolated impact
- Easy rollback

---

## From Sandbox Reconsiderations

When analyzing a sandbox entry:

```markdown
## Impact Analysis: Reconsidered Decision

**Original:** [original decision]
**Proposed:** [revised recommendation from sandbox]
**Alignment:** [same/modified/reversed]

### What Would Change

If we adopt the reconsidered decision:
[analysis of switching from original to proposed]
```

---

## Examples

### Example 1: Active Decision Impact

**Input:**
```
/analyze-impact 2026-01-03-abc123
```

**Output:**
```markdown
## Impact Analysis: Database Selection (PostgreSQL)

**Decision ID:** 2026-01-03-abc123
**Current Outcome:** Use PostgreSQL for user data

---

### Downstream Dependencies

3 decisions directly depend on this decision.

```
Database Selection (PostgreSQL)
├── Authentication (JWT) - 2026-01-04
│   └── Session Handling - 2026-01-05
└── User Schema Design - 2026-01-04
```

| Decision | Date | Dependency Type | Risk if Changed |
|----------|------|-----------------|-----------------|
| Authentication | 2026-01-04 | Uses PG session store | High |
| User Schema | 2026-01-04 | PG-specific types | Medium |
| Session Handling | 2026-01-05 | Assumes PG transactions | High |

---

### Assumption Cascade

**Assumptions that would be invalidated:**

| Decision | Assumption | Impact |
|----------|------------|--------|
| Authentication | "ACID transactions available" | High |
| Session Handling | "Strong consistency for auth" | High |

**Decisions requiring re-evaluation:** 2

---

### Affected Artifacts

**Code:**
- `src/db/connection.ts`
- `src/models/User.ts`
- `src/auth/session.ts`

**Documentation:**
- `docs/decisions/product/2026-01-03-database/README.md`

---

### Effort Estimate

**Impact Level:** Major

**Changes Required:**
- [ ] Update 5+ code files
- [ ] Supersede 1 ADR
- [ ] Re-evaluate 2 dependent decisions
- [ ] Update architecture docs
- [ ] Data migration required

**Recommendation:** High-impact change. Consider carefully.
```

### Example 2: With Alternative

**Input:**
```
/analyze-impact 2026-01-03-abc123 --if-changed "Use MongoDB instead"
```

Adds specific analysis of PostgreSQL → MongoDB migration.
