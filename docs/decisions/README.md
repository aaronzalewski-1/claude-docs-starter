# Decision Artifacts

This folder stores formal documents generated from multi-persona analyses.

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
| **Product** | Architecture Decision Record | `/export-artifact adr <name>` |
| **Research** | Literature Review | `/export-artifact literature-review <name>` |
| **Advisory** | Board Memo | `/export-artifact board-memo <name>` |

---

## Workflow

1. Run a persona review command:
   ```
   /review-product-decision Should we use Redis for caching?
   ```

2. After review completes, export to a formal document:
   ```
   /export-artifact adr redis-caching
   ```

3. Find your artifact at:
   ```
   docs/decisions/product/2026-01-04-redis-caching/README.md
   ```

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
