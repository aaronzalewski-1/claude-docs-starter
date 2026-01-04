---
name: artifact-registry
description: Defines artifact types, templates, and persona-to-section mappings for document generation from persona analyses
type: skill
version: 1.0.0
---

# Artifact Registry

> Central registry defining how persona analyses map to formal documents.

---

## Overview

This skill defines the artifact types available for export after running multi-persona review commands. Each artifact type specifies:

- **trigger_review**: The review command that produces the source data
- **personas**: Which personas contribute to the artifact
- **sections**: How persona outputs map to document sections
- **format**: Output format (markdown, convertible to DOCX/PDF)

---

## MVP Artifacts

### Product Package

#### ADR (Architecture Decision Record)

| Property | Value |
|----------|-------|
| **Command** | `/export-artifact adr <name>` |
| **Trigger** | After `/review-product-decision` |
| **Format** | Markdown |
| **Template** | `.claude/templates/product/adr.template.md` |

**Section Mappings:**

| Section | Source |
|---------|--------|
| Context | Decision statement from review |
| Decision | Consensus recommendation |
| Consequences (Positive) | Benefits identified by personas |
| Consequences (Negative) | Risks and tradeoffs from analysis |
| Consequences (Neutral) | "What Can Wait" section |
| Alternatives Considered | Options discussed by personas |
| Analysis Summary | Weighted consensus table |

**Contributing Personas:**
- Architect: Pattern alignment, SOLID evaluation, coupling concerns
- Skeptic: Verified claims, flagged assumptions
- Economist: Cost analysis, ROI, scale economics
- Pragmatist: MVP assessment, deferral opportunities

---

### Research Package

#### Literature Review

| Property | Value |
|----------|-------|
| **Command** | `/export-artifact literature-review <name>` |
| **Trigger** | After `/review-research` |
| **Format** | Markdown |
| **Template** | `.claude/templates/research/literature-review.template.md` |

**Section Mappings:**

| Section | Source |
|---------|--------|
| Executive Summary | Consensus synthesis |
| Sources Evaluated | Librarian source credibility table |
| Methodology Assessment | Methodologist validity analysis |
| Claim Verification | Skeptic citation and data integrity check |
| Themes and Patterns | Synthesizer theme identification |
| Gaps and Limitations | Key limitations from consensus |
| Recommendations | Consensus recommendation |

**Contributing Personas:**
- Skeptic: Citation verification, data integrity, misrepresentation detection
- Librarian: Source credibility, evidence hierarchy, citation chains
- Methodologist: Research design, validity assessment, statistical rigor
- Critic: Counterarguments, alternative explanations, assumption challenges
- Synthesizer: Themes, relationships, integrated understanding

---

### Advisory Package

#### Board Memo

| Property | Value |
|----------|-------|
| **Command** | `/export-artifact board-memo <name>` |
| **Trigger** | After `/review-business-decision` |
| **Format** | Markdown |
| **Template** | `.claude/templates/advisory/board-memo.template.md` |

**Section Mappings:**

| Section | Source |
|---------|--------|
| Executive Summary | Consensus synthesis |
| Decision Context | Stage, focus area, decision statement |
| Advisory Perspectives | Summary from each of 7 personas |
| Consensus Table | Full weighted consensus with scores |
| Key Risks | Key tensions and conflicts identified |
| Recommendation | Consensus recommendation |
| Required Actions | Critical actions from analysis |
| Milestones for Revisiting | Triggers that would change decision |

**Contributing Personas:**
- Skeptic: Claim verification, assumption testing
- CFO: Financial impact, runway, unit economics
- Go-to-Market: Revenue, acquisition, positioning
- Strategist: Long-term implications, competitive positioning
- Operations: Execution feasibility, capacity
- Product Advisor: PMF impact, user value
- Counsel: Legal risks, compliance, contracts

---

## Storage Convention

Generated artifacts are stored in:

```
docs/decisions/<package>/YYYY-MM-DD-<artifact-name>/
├── README.md          # The generated artifact
└── analysis.json      # Structured analysis data (optional)
```

**Naming Convention:**
- Date: ISO format (YYYY-MM-DD)
- Name: kebab-case, descriptive (e.g., `redis-caching-decision`)

**Examples:**
- `docs/decisions/product/2026-01-04-redis-caching/README.md`
- `docs/decisions/research/2026-01-04-intermittent-fasting/README.md`
- `docs/decisions/advisory/2026-01-04-series-a-timing/README.md`

---

## Format Conversion

Generated markdown can be converted to other formats:

| Target | Command |
|--------|---------|
| PDF | `pandoc README.md -o decision.pdf` |
| DOCX | `pandoc README.md -o decision.docx` |
| HTML | `pandoc README.md -o decision.html` |

**Requirements:**
- [Pandoc](https://pandoc.org/) installed
- Optional: Custom CSS for HTML, LaTeX template for PDF

---

## Future Artifacts (Post-MVP)

| Package | Artifact | Priority | Description |
|---------|----------|----------|-------------|
| Product | Cost Analysis | High | Detailed cost comparison with ROI |
| Product | Comparison Matrix | Medium | Options scored against criteria |
| Research | Evidence Summary | High | Claim verification report |
| Research | Annotated Bibliography | Medium | Categorized sources with notes |
| Advisory | Strategic Plan | High | Comprehensive strategy document |
| Advisory | Pitch Deck Outline | Medium | Investor presentation structure |
| Advisory | Financial Model Spec | Low | Model assumptions and structure |

---

## Integration with Review Commands

The export command checks for recent persona analysis:

1. **Context Check**: Verify a review command was recently executed
2. **Package Detection**: Identify which package produced the analysis
3. **Artifact Validation**: Confirm requested artifact matches the package
4. **Template Loading**: Load appropriate template for artifact type
5. **Section Mapping**: Extract persona outputs to template sections
6. **Generation**: Create markdown file in decisions folder
7. **Confirmation**: Return file path and conversion instructions
