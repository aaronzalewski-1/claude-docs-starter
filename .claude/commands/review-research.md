---
name: review-research
description: Multi-persona review of research questions and findings. Use when evaluating research quality, synthesizing sources, challenging claims, or assessing source credibility. Triggers on phrases like "review this research", "evaluate these sources", "synthesize these findings", or the explicit /review-research command.
---

# Review Research

Evaluate research questions and findings through five specialized personas, each analyzing from their perspective before reaching weighted consensus.

## Command Format

```
/review-research <research question, claim, or sources to evaluate>
```

Also triggers on natural language requests to review, evaluate, or synthesize research.

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

1. **Skeptic Analysis** (`/personas/research:skeptic`)
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

After all personas have analyzed, produce a weighted synthesis.

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

**Source Discovery**: Librarian dominates - finding good sources is the priority.

**Quality Assessment**: Methodologist dominates - rigor is the focus.

**Claim Evaluation**: Skeptic and Critic co-dominate - verifying and challenging claims is key.

**Knowledge Integration**: Synthesizer dominates - building understanding is the goal.

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
/personas/research:skeptic Verify the citations in this paper support its claims
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

## Next Steps

After consensus, offer relevant follow-up options:

| If Analysis Shows | Offer |
|-------------------|-------|
| Citations don't support claims | Skeptic deep-dive on specific claims |
| Need better sources | Source discovery strategies |
| Methodological concerns | Study design recommendations |
| Claims need testing | Additional critique approaches |
| Ready to integrate | Synthesis frameworks |
