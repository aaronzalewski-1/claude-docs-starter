---
name: review-research
description: Multi-persona review of research questions and findings. Use when evaluating research quality, synthesizing sources, challenging claims, or assessing source credibility. Triggers on phrases like "review this research", "evaluate these sources", "synthesize these findings", or the explicit /review-research command.
---

# Review Research

Evaluate research questions and findings through five specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-research <research question, claim, or sources to evaluate> [--save <name>]
```

**Arguments:**
- `question`: The research question, claim, or sources to evaluate
- `--save <name>`: (Optional) Save the analysis as a Literature Review to `docs/decisions/research/`

Also triggers on natural language requests to review, evaluate, or synthesize research.

**Examples:**
```
/review-research Does intermittent fasting improve cognitive function?
/review-research Evaluate the evidence for remote work productivity --save remote-work-research
```

## Package: Research

This orchestrator invokes five analytical personas from the **Research** package:

| Persona | Role | Focus |
|---------|------|-------|
| **Skeptic** | Truth guardian | Citation verification, data integrity, claim validation |
| **Methodologist** | Validity guardian | Research design, methodology, statistical rigor |
| **Synthesizer** | Pattern finder | Integration, themes, relationships |
| **Critic** | Devil's advocate | Counterarguments, alternative explanations |
| **Librarian** | Source curator | Credibility, citations, evidence hierarchy |

Each persona has:
- A **command** (`/personas/research:methodologist`, etc.) for individual invocation
- A **PersonaSkill** with domain expertise frameworks

## Orchestration Process

### Phase 1: Run Each Persona

For the research question provided, run each persona analysis **in sequence**:

1. **Skeptic Analysis** (`/personas/core:skeptic`)
   - Verify citations support claims
   - Check data integrity
   - Detect misrepresentation patterns

2. **Librarian Analysis** (`/personas/research:librarian`)
   - Evaluate source credibility
   - Trace citation chains
   - Assess evidence hierarchy

3. **Methodologist Analysis** (`/personas/research:methodologist`)
   - Evaluate research design
   - Assess internal and external validity
   - Check statistical approach

4. **Critic Analysis** (`/personas/research:critic`)
   - Steel-man the claims
   - Generate counterarguments
   - Test assumptions

5. **Synthesizer Analysis** (`/personas/research:synthesizer`)
   - Identify themes across sources
   - Map relationships
   - Integrate findings

### Phase 2: Synthesize Consensus

After all personas have analyzed, reason through before producing the synthesis:

**Pre-Synthesis Reasoning (think through these):**
1. Which claims were verified across multiple personas?
2. Where do confidence scores diverge most significantly?
3. Did the Skeptic find citation issues that affect Synthesizer's conclusions?
4. Are there methodological concerns that undermine the findings?
5. What evidence would change each persona's assessment?

Then produce a weighted synthesis.

## Output Format

```markdown
## Research Question Under Review
[Restate the question/claim clearly]

---

## Skeptic Analysis
[Citation verification, data integrity, claim validation]
**Confidence: X.X**

---

## Librarian Analysis
[Source assessment, credibility evaluation, citation quality]
**Confidence: X.X**

---

## Methodologist Analysis
[Design evaluation, validity assessment, statistical concerns]
**Confidence: X.X**

---

## Critic Analysis
[Counterarguments, alternative explanations, assumption challenges]
**Confidence: X.X**

---

## Synthesizer Analysis
[Themes identified, relationships mapped, integrated understanding]
**Confidence: X.X**

---

## Weighted Consensus

| Persona | Confidence | Weight | Weighted Score |
|---------|------------|--------|----------------|
| Skeptic | X.X | 0.XX | X.XX |
| Librarian | X.X | 0.XX | X.XX |
| Methodologist | X.X | 0.XX | X.XX |
| Critic | X.X | 0.XX | X.XX |
| Synthesizer | X.X | 0.XX | X.XX |
| **Weighted Average** | | | **X.XX** |

### Synthesis
[Integrated analysis considering all perspectives]

### Key Findings
[What the evidence actually supports]

### Key Limitations
[What we cannot conclude and why]

### Recommendation
[Clear conclusion with confidence level]

### Further Research Needed
[Questions that remain unanswered]
```

## Consensus Weighting

Default weights vary by research phase. Adjust based on your context:

| Phase | Skeptic | Librarian | Methodologist | Critic | Synthesizer |
|-------|---------|-----------|---------------|--------|-------------|
| **Source Discovery** | 0.10 | **0.35** | 0.12 | 0.13 | 0.30 |
| **Quality Assessment** | 0.18 | 0.20 | **0.32** | 0.18 | 0.12 |
| **Claim Evaluation** | **0.28** | 0.15 | 0.20 | **0.25** | 0.12 |
| **Knowledge Integration** | 0.12 | 0.13 | 0.15 | 0.18 | **0.42** |

### Weighting Rationale

**Source Discovery** (finding what's out there):
- **Librarian dominates (0.35)** - Finding authoritative sources is the primary task.
- **Synthesizer high (0.30)** - Need to see patterns to know what's missing.
- Skeptic/Methodologist low - Rigor matters less during initial discovery.

**Quality Assessment** (evaluating what you found):
- **Methodologist dominates (0.32)** - Study design and validity are the focus.
- Skeptic/Critic moderate (0.18) - Verification and challenge support quality assessment.
- Synthesizer low (0.12) - Integration comes later.

**Claim Evaluation** (testing specific claims):
- **Skeptic high (0.28)** - Verifying claims against evidence is primary.
- **Critic high (0.25)** - Challenging claims and finding counterarguments.
- Librarian moderate (0.15) - Source quality still matters.

**Knowledge Integration** (building understanding):
- **Synthesizer dominates (0.42)** - Connecting patterns is the goal.
- Critic moderate (0.18) - Keep challenging even during integration.
- Others low - Foundation work is done.

### Example Calculation

For a **Claim Evaluation** task:
```
Skeptic:       0.85 confidence × 0.28 weight = 0.24
Librarian:     0.90 confidence × 0.15 weight = 0.14
Methodologist: 0.70 confidence × 0.20 weight = 0.14
Critic:        0.75 confidence × 0.25 weight = 0.19
Synthesizer:   0.80 confidence × 0.12 weight = 0.10
                                ────────────────────
Weighted Average:                          0.81
```

## When Personas Disagree

If confidence-weighted scores diverge by >0.3, explicitly surface the conflict:

> **Conflict:** Methodologist (0.5) and Synthesizer (0.8) disagree.
> - Methodologist flags methodological concerns
> - Synthesizer sees useful patterns despite limitations
>
> **Resolution depends on:** [How critical is methodological rigor for this question?]

## Confidence Scoring

Each persona provides a confidence score:

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | High confidence - strong evidence, rigorous analysis |
| 0.7-0.8 | Moderate confidence - good evidence, some gaps |
| 0.5-0.6 | Low confidence - significant concerns |
| < 0.5 | Insufficient - major issues or insufficient evidence |

## Individual Persona Usage

You can invoke personas individually for focused analysis:

```
/personas/core:skeptic Verify the citations in this paper support its claims
/personas/research:librarian Evaluate these sources on climate change
/personas/research:methodologist Assess this study's methodology
/personas/research:critic Challenge this hypothesis
/personas/research:synthesizer Connect these findings on remote work
```

## Example

```
/review-research Does intermittent fasting improve cognitive function?
```

Triggers full persona analysis:
- **Skeptic**: Verifies that cited studies support claimed cognitive benefits, checks data integrity
- **Librarian**: Evaluates source quality, finds primary research, checks citation chains
- **Methodologist**: Assesses study designs, sample sizes, measurement validity
- **Critic**: Generates counterarguments, alternative explanations, tests assumptions
- **Synthesizer**: Integrates findings, identifies themes, maps what's known

Then synthesizes weighted consensus with recommendation.

## Related Packages

| Package | Orchestrator | Use For |
|---------|--------------|---------|
| **Product** | `/review-product-decision` | Implementation decisions, architecture |
| **Research** | `/review-research` | Research questions, literature analysis |

## If Analysis Cannot Proceed

If the review cannot be completed due to insufficient information:

1. **Identify which personas are blocked** - Which analyses cannot proceed?
2. **State what's missing** - Sources not accessible? Methodology unclear?
3. **Provide partial analysis** - Complete what CAN be done
4. **Set confidence to reflect gaps** - Flag incomplete areas
5. **Recommend investigation path** - How to get the missing information

**Example:**
> **Blocked:** Methodologist cannot assess - original study behind paywall
> **Partial analysis available:** Librarian found secondary sources; Critic can work from abstract
> **Recommendation:** Access original study through institution or request from authors

---

## Next Steps

After consensus, offer relevant follow-up options:

| If Analysis Shows | Offer |
|-------------------|-------|
| Citations don't support claims | Skeptic deep-dive on specific claims |
| Need better sources | Source discovery strategies |
| Methodological concerns | Study design recommendations |
| Claims need testing | Additional critique approaches |
| Ready to integrate | Synthesis frameworks |

---

## Saving as Literature Review (--save option)

When `--save <name>` is provided, generate a Literature Review document after the analysis.

### Step 1: Generate Literature Review Content

After completing the weighted consensus, transform the analysis into literature review format:

| Analysis Section | Literature Review Section |
|------------------|--------------------------|
| Consensus synthesis | Executive Summary |
| Source evaluations | Sources Evaluated |
| Methodologist findings | Methodology Assessment |
| Skeptic analysis | Claim Verification |
| Synthesizer themes | Themes and Patterns |
| Key limitations | Gaps and Limitations |
| Recommendation | Recommendations |

### Step 2: Create Literature Review File

Save to: `docs/decisions/research/YYYY-MM-DD-<name>/README.md`

Use template from `.claude/templates/research/literature-review.template.md`

### Step 3: Report Save Location

After saving, append to output:

```markdown
---

## Literature Review Saved

**File:** `docs/decisions/research/YYYY-MM-DD-<name>/README.md`

**Convert to other formats:**
```bash
cd docs/decisions/research/YYYY-MM-DD-<name>
pandoc README.md -o review.pdf    # PDF
pandoc README.md -o review.docx   # Word
```

**Track in git:**
```bash
git add docs/decisions/research/YYYY-MM-DD-<name>/
git commit -m "Literature Review: <name>"
```
```

### Naming Guidelines

- Use kebab-case: `intermittent-fasting`, `remote-work-productivity`
- Be descriptive but concise
- Date prefix added automatically
