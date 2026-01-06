# Decision Artifacts

This folder stores formal documents generated from multi-persona analyses.

**Related Documentation:**
- [PERSONAS.md](../CLAUDE/PERSONAS.md) - Full persona system reference
- [PERSONA-PACKAGES.md](../CLAUDE/PERSONA-PACKAGES.md) - Package architecture
- [artifact-registry.skill.md](../../.claude/skills/artifact-registry.skill.md) - Template mappings

---

## Structure

```
docs/decisions/
├── product/              # From /review-product-decision
│   └── YYYY-MM-DD-name/
├── research/             # From /review-research
│   └── YYYY-MM-DD-name/
└── advisory/             # From /review-business-decision
    └── YYYY-MM-DD-name/
```

Each decision folder contains:
- `README.md` - The generated artifact document
- Supporting files as needed

---

## Artifact Types

| Package | Artifact | Command |
|---------|----------|---------|
| **Product** | Architecture Decision Record | `/review-product-decision <decision> --save <name>` |
| **Research** | Literature Review | `/review-research <question> --save <name>` |
| **Advisory** | Board Memo | `/review-business-decision <decision> --save <name>` |

---

## Workflow

Run a persona review command with `--save` to generate an artifact in a single step:

```
/review-product-decision Should we use Redis for caching? --save redis-caching
```

Find your artifact at:
```
docs/decisions/product/2026-01-04-redis-caching/README.md
```

---

## When to Save

| Scenario | Use `--save`? | Rationale |
|----------|---------------|-----------|
| Formal documentation needed | ✅ Yes | Creates permanent record |
| Stakeholder communication | ✅ Yes | Shareable, convertible to PDF/DOCX |
| Architectural decision | ✅ Yes | ADRs are valuable project artifacts |
| Quick exploration | ❌ No | Just run the review without saving |
| Personal learning | ❌ No | Review output is sufficient |
| Iterating on a decision | ❌ No | Save only when finalized |

**Tip:** Run the review first without `--save` to see if the analysis is useful, then re-run with `--save` if you want to preserve it.

---

## Format Conversion

Convert markdown artifacts to other formats using pandoc:

```bash
# To PDF
pandoc README.md -o decision.pdf

# To Word
pandoc README.md -o decision.docx

# To HTML
pandoc README.md -o decision.html --standalone
```

**Install pandoc:** https://pandoc.org/installing.html

---

## Naming Convention

- **Date**: YYYY-MM-DD (ISO format)
- **Name**: kebab-case, descriptive
- **Examples**:
  - `2026-01-04-redis-caching`
  - `2026-01-04-series-a-timing`
  - `2026-01-04-intermittent-fasting-research`

---

## Version History

Artifacts are versioned through git history. To see changes to a decision:

```bash
git log --oneline docs/decisions/product/2026-01-04-redis-caching/
```

For major revisions, create a new dated folder rather than modifying the original.

---

## Artifact Templates

Each package uses a specific template to structure the generated document:

| Package | Template | Preview |
|---------|----------|---------|
| **Product** | ADR | [adr.template.md](../../.claude/templates/product/adr.template.md) |
| **Research** | Literature Review | [literature-review.template.md](../../.claude/templates/research/literature-review.template.md) |
| **Advisory** | Board Memo | [board-memo.template.md](../../.claude/templates/advisory/board-memo.template.md) |

Templates define the document structure and how persona outputs map to sections.

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Folder not created | Missing `--save` flag | Re-run with `--save <name>` appended |
| Wrong package folder | Used wrong review command | Use the correct review command for your domain |
| Pandoc not found | Not installed | Install from [pandoc.org](https://pandoc.org/installing.html) |
| Name conflicts | Duplicate artifact name on same date | Use a more specific name or different date |
| Empty artifact | Review was incomplete | Ensure all personas completed before saving |

### Common Mistakes

1. **Forgetting `--save`**: The review runs but no file is created
   - Fix: Re-run the exact same command with `--save <name>` added

2. **Using spaces in names**: `--save my decision` fails
   - Fix: Use kebab-case: `--save my-decision`

3. **Wrong command for domain**: Using `/review-product-decision` for a business strategy question
   - Fix: Use `/review-business-decision` for business decisions, `/review-research` for research questions
