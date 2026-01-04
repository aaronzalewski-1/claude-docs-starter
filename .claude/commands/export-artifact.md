---
name: export-artifact
description: Generate formal documents from persona analyses. Use after /review-product-decision, /review-research, or /review-business-decision commands. Triggers on phrases like "export artifact", "generate document", "create ADR", "create board memo", or the explicit /export-artifact command.
---

# Export Artifact

Generate formal markdown documents from multi-persona analyses, suitable for conversion to DOCX or PDF.

## Command Format

```
/export-artifact <artifact-type> <name>
```

**Arguments:**
- `artifact-type`: One of `adr`, `literature-review`, `board-memo`
- `name`: Descriptive name in kebab-case (e.g., `redis-caching`, `series-a-timing`)

$ARGUMENTS

---

## Available Artifacts (MVP)

| Artifact | Command | After Review | Output |
|----------|---------|--------------|--------|
| **ADR** | `/export-artifact adr <name>` | `/review-product-decision` | Architecture Decision Record |
| **Literature Review** | `/export-artifact literature-review <name>` | `/review-research` | Literature Review Document |
| **Board Memo** | `/export-artifact board-memo <name>` | `/review-business-decision` | Board-Ready Decision Memo |

---

## Prerequisites

Before running this command, you **must** have:

1. Run a persona review command in the current conversation:
   - `/review-product-decision` → enables `adr` export
   - `/review-research` → enables `literature-review` export
   - `/review-business-decision` → enables `board-memo` export

2. The analysis must be complete with weighted consensus

If no recent analysis exists, this command will inform you and suggest running the appropriate review command first.

---

## Process

### Step 1: Validate Context

Check the current conversation for a recent persona analysis:

1. **Identify the review type** - Which `/review-*` command was run?
2. **Verify completion** - Is there a weighted consensus section?
3. **Match artifact type** - Does the requested artifact match the review package?

| Review Command | Valid Artifact Types |
|----------------|---------------------|
| `/review-product-decision` | `adr` |
| `/review-research` | `literature-review` |
| `/review-business-decision` | `board-memo` |

**If mismatch:** Inform user and suggest correct artifact type.

### Step 2: Extract Analysis Data

From the persona analysis in the conversation, extract:

#### For ADR (from `/review-product-decision`):
- Decision statement → Context
- Consensus recommendation → Decision
- Benefits from each persona → Positive Consequences
- Risks/tradeoffs → Negative Consequences
- "What Can Wait" items → Neutral Consequences
- Options discussed → Alternatives
- Persona confidence scores → Analysis Summary table

#### For Literature Review (from `/review-research`):
- Consensus synthesis → Executive Summary
- Source evaluations → Sources Evaluated table
- Methodologist findings → Methodology Assessment
- Skeptic analysis → Claim Verification
- Synthesizer themes → Themes and Patterns
- Key limitations → Gaps and Limitations
- Recommendation → Recommendations

#### For Board Memo (from `/review-business-decision`):
- Detected stage/focus → Decision Context
- Each persona's analysis → Advisory Perspectives sections
- Weighted consensus table → Consensus Table
- Key tensions → Key Risks
- Recommendation → Recommendation
- Critical actions → Required Actions
- Triggers for revisiting → Milestones

### Step 3: Generate Document

1. **Load template** from `.claude/templates/<package>/<artifact-type>.template.md`
2. **Populate sections** with extracted analysis data
3. **Calculate today's date** for filename and metadata
4. **Generate filename**: `YYYY-MM-DD-<name>`

### Step 4: Save to Storage

Create the artifact in the decisions folder:

```
docs/decisions/<package>/YYYY-MM-DD-<name>/README.md
```

**Package mapping:**
- `adr` → `docs/decisions/product/`
- `literature-review` → `docs/decisions/research/`
- `board-memo` → `docs/decisions/advisory/`

### Step 5: Confirm and Provide Next Steps

Return:
1. **File path** of created artifact
2. **Conversion instructions** for other formats
3. **Git command** to track the decision

---

## Output Format

After successful export:

```markdown
## Artifact Generated

**File:** `docs/decisions/<package>/YYYY-MM-DD-<name>/README.md`

### Preview

[First 20 lines of generated document]

### Next Steps

**Convert to other formats:**
```bash
cd docs/decisions/<package>/YYYY-MM-DD-<name>

# To PDF
pandoc README.md -o decision.pdf

# To Word
pandoc README.md -o decision.docx

# To HTML
pandoc README.md -o decision.html --standalone
```

**Track in git:**
```bash
git add docs/decisions/<package>/YYYY-MM-DD-<name>/
git commit -m "Add <artifact-type>: <name>"
```
```

---

## Error Handling

### No Recent Analysis Found

```markdown
## Export Failed

No recent persona analysis found in this conversation.

**To export an artifact:**
1. First run a review command:
   - `/review-product-decision <decision>` for ADR
   - `/review-research <topic>` for Literature Review
   - `/review-business-decision <decision>` for Board Memo

2. Then run `/export-artifact <type> <name>`
```

### Artifact Type Mismatch

```markdown
## Export Failed

You requested `<requested-type>` but the recent analysis was from `/review-<actual-package>`.

**Valid artifact for this analysis:** `<valid-artifact-type>`

Run: `/export-artifact <valid-artifact-type> <name>`
```

### Missing Name Argument

```markdown
## Name Required

Please provide a descriptive name for the artifact:

```
/export-artifact <type> <name>
```

**Examples:**
- `/export-artifact adr redis-caching-decision`
- `/export-artifact literature-review intermittent-fasting`
- `/export-artifact board-memo series-a-timing`

**Naming guidelines:**
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- Avoid dates (added automatically)
```

---

## Examples

### Example 1: Export ADR after Product Decision Review

```
User: /review-product-decision Should we use Redis or Memcached for session caching?

[... persona analysis completes ...]

User: /export-artifact adr redis-vs-memcached