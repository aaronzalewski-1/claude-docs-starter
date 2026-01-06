---
name: promote-reconsideration
description: Move a sandbox reconsideration to active planning. This is the ONLY way to move isolated reconsiderations into the active workflow. Requires explicit user action.
---

# Promote Reconsideration

Move a sandbox reconsideration analysis into active planning or roadmap.

## Command Format

```
/promote-reconsideration <sandbox-id> [--to-plan | --to-roadmap]
```

**Arguments:**
- `sandbox-id`: ID of sandbox entry (e.g., `2026-01-06-caching-recon`)
- `--to-plan`: Add to current SESSION-STATE.json as action item
- `--to-roadmap`: Add to ROADMAP.md as future work item

**Examples:**
```
/promote-reconsideration 2026-01-06-caching-recon --to-plan
/promote-reconsideration 2026-01-06-auth-recon --to-roadmap
```

---

## Core Principle

**This is the ONLY gateway from sandbox to active.**

- Sandbox reconsiderations are isolated by design
- No automatic promotion ever occurs
- User must explicitly invoke this command
- Requires confirmation before proceeding

---

## Process

### Step 1: Load Sandbox Entry

1. Read from `docs/reasoning/sandbox/[sandbox-id].json`
2. Verify `status === "sandbox"`
3. If not found or not sandbox, error

### Step 2: Validate Entry

Check required fields:
- `original.decisionId` - Links to original decision
- `proposedOutcome.recommendation` - What we're promoting
- `comparison.alignment` - How it differs from original

If missing, warn and ask to complete analysis first.

### Step 3: Show Summary and Confirm

```markdown
## Promotion Request

**Sandbox Entry:** [id]
**Original Decision:** [original.decisionPoint]
**Original Outcome:** [original.outcome]

**Proposed Change:**
[proposedOutcome.recommendation]

**Alignment:** [comparison.alignment]
**Key Differences:**
- [difference 1]
- [difference 2]

**Target:** [--to-plan or --to-roadmap]

---

**Impact Summary:**
[Brief from analyze-impact if available]

---

Proceed with promotion?
- [Y] Yes, promote to [target]
- [N] No, keep in sandbox
- [A] Run /analyze-impact first
```

### Step 4: Execute Promotion

#### If `--to-plan`:

1. Read `docs/CLAUDE/SESSION-STATE.json` (or template if none exists)
2. Add to `nextSteps`:
   ```json
   {
     "step": "Implement reconsidered decision: [brief]",
     "source": "sandbox:[sandbox-id]",
     "priority": "high"
   }
   ```
3. Add to `context.keyDecisions`:
   ```json
   {
     "decision": "[proposedOutcome.recommendation]",
     "rationale": "Reconsidered from [original]",
     "date": "[now]",
     "reasoningEntryId": "[sandbox-id]",
     "status": "pending_implementation"
   }
   ```
4. Write updated SESSION-STATE

#### If `--to-roadmap`:

1. Read `docs/CLAUDE/ROADMAP.md`
2. Add entry to appropriate section:
   ```markdown
   ### Reconsidered: [Original Decision Title]

   **Status:** Planned
   **Source:** Sandbox analysis [sandbox-id]
   **Original:** [original decision]
   **Proposed:** [proposed change]

   **Rationale:** [brief from sandbox]

   **Next Steps:**
   - [ ] Review impact analysis
   - [ ] Implement changes
   - [ ] Update affected decisions
   ```
3. Write updated ROADMAP

### Step 5: Update Sandbox Status

Update sandbox entry:
```json
{
  "status": "promoted",
  "promotedTo": "plan" | "roadmap",
  "promotedDate": "[now]",
  "promotedBy": "user"
}
```

### Step 6: Report

```markdown
## Reconsideration Promoted

**From:** docs/reasoning/sandbox/[sandbox-id].json
**To:** [SESSION-STATE.json or ROADMAP.md]

**What Happened:**
- Added to [target] as action item
- Sandbox entry marked as promoted
- Original decision unchanged (update manually when implemented)

**Next Steps:**
1. Review the promoted item in [target]
2. Implement the reconsidered decision
3. Update original reasoning log when complete
4. Run `/capture-reasoning` for the new decision

**Note:** The original decision in the reasoning log is NOT automatically
updated. Capture a new reasoning entry when you implement the change.
```

---

## What Gets Promoted

### To Plan (SESSION-STATE)
- Immediate action items
- Active work for current session
- Changes to implement now

### To Roadmap
- Future work items
- Deferred changes
- Changes pending more analysis

---

## What Does NOT Happen

This command does NOT:
- Modify original decision entries
- Update the reasoning index
- Change code or documentation
- Create new reasoning entries
- Override existing decisions

All of those require separate, explicit actions.

---

## Validation Checks

### Before Promotion

1. **Sandbox exists:** Entry must be in sandbox directory
2. **Valid status:** Must have `status: "sandbox"`
3. **Complete analysis:** Must have `proposedOutcome`
4. **Not already promoted:** Check `status !== "promoted"`

### Errors

**Entry not found:**
```
Error: Sandbox entry [id] not found.
Check docs/reasoning/sandbox/ for available entries.
```

**Already promoted:**
```
Error: Entry [id] was already promoted on [date].
Target: [plan/roadmap]
```

**Incomplete analysis:**
```
Error: Sandbox entry is incomplete.
Missing: [field]
Run /reconsider-decision to complete the analysis.
```

---

## Examples

### Example 1: Promote to Plan

**Input:**
```
/promote-reconsideration 2026-01-06-caching-recon --to-plan
```

**Output:**
```markdown
## Promotion Request

**Sandbox Entry:** 2026-01-06-caching-recon
**Original Decision:** What caching strategy should we use?
**Original Outcome:** Use Redis for session caching

**Proposed Change:**
Use in-memory LRU cache instead of Redis

**Alignment:** Reversed
**Key Differences:**
- Simpler architecture (no Redis dependency)
- Sufficient for small session sizes
- Lower operational overhead

**Target:** SESSION-STATE.json (active plan)

---

Proceed with promotion? [Y/N/A]
> Y

---

## Reconsideration Promoted

**From:** docs/reasoning/sandbox/2026-01-06-caching-recon.json
**To:** docs/CLAUDE/SESSION-STATE.json

**Added to nextSteps:**
"Implement reconsidered decision: Switch from Redis to in-memory LRU cache"

**Next Steps:**
1. Review SESSION-STATE.json
2. Implement the caching change
3. Run /capture-reasoning for the new decision
```

### Example 2: Promote to Roadmap

**Input:**
```
/promote-reconsideration 2026-01-06-auth-recon --to-roadmap
```

Adds the reconsidered decision to ROADMAP.md as a future work item.

---

## Cleanup

After implementation is complete:

1. **Capture new decision:**
   ```
   /capture-reasoning "Switched caching from Redis to in-memory"
   ```

2. **Link to original:**
   In the new entry, reference the original decision in `dependsOn` or notes.

3. **Archive sandbox:**
   Promoted entries remain in sandbox with `status: "promoted"` for history.
