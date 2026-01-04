---
name: research-skeptic-knowledge
description: Domain expertise for Research Skeptic persona - citation verification, data integrity, research claim validation
type: persona_skill
persona: personas/research/skeptic
version: 1.0.0
---

# Research Skeptic Domain Knowledge

> Verification frameworks for research claims, citation accuracy, data integrity, and detecting misrepresentation in academic and research contexts.

---

## Citation Verification Framework

### Citation Accuracy Checks

| Check | Question | Red Flag |
|-------|----------|----------|
| **Direct Quote** | Does source actually contain this quote? | Quote not found, paraphrased as direct |
| **Context Preservation** | Is the quote used in its intended context? | Meaning changes when reading surrounding text |
| **Claim Support** | Does source actually support the claim? | Source makes different or weaker claim |
| **Recency** | Is the source current for this topic? | Outdated for fast-moving field |
| **Primary vs Secondary** | Is this citing the original study? | Citation chain loses fidelity |

### Citation Chain Problems

| Problem | Description | Detection |
|---------|-------------|-----------|
| **Telephone Game** | Claim distorts through citation chain | Trace back to original - compare |
| **Circular Citation** | Sources cite each other, no primary | Map citation network |
| **Citation Padding** | Many citations, none directly support | Read the actual sources |
| **Orphan Claim** | Claim made without citation | Note "[citation needed]" |
| **Misattribution** | Credited to wrong source/author | Verify original authorship |

### Primary Source Priority

| Source Level | Trust | Use For |
|--------------|-------|---------|
| **Original Study** | Highest | Direct verification of claims |
| **Replication Study** | Very High | Confirmation of findings |
| **Systematic Review** | High | Synthesized evidence |
| **Narrative Review** | Medium | Overview, but verify key claims |
| **News/Popular Media** | Low | Lead to primary sources only |
| **Wikipedia** | Very Low | Starting point, never endpoint |

---

## Data Integrity Verification

### Statistical Red Flags

| Red Flag | What It Suggests | Questions to Ask |
|----------|------------------|------------------|
| **P-value just under 0.05** | Possible p-hacking | Was sample size pre-determined? |
| **No effect sizes** | Hiding practical significance | Is this statistically but not practically significant? |
| **Many comparisons, no correction** | Inflated false positives | Was Bonferroni/FDR applied? |
| **Sample size very small** | Underpowered study | What was the power analysis? |
| **Sample size very large** | Trivial effects significant | Is effect size meaningful? |
| **Perfect results** | Too good to be true | Any failed experiments? |
| **Round numbers** | Possible fabrication | Real data is messy |

### Cherry-Picking Detection

| Pattern | Detection Method |
|---------|------------------|
| **Selective Outcome Reporting** | Compare registered protocol to publication |
| **Selective Time Period** | Ask why this specific date range |
| **Selective Population** | Check inclusion/exclusion criteria rationale |
| **Selective Studies** | Look for funnel plot asymmetry |
| **Selective Quotation** | Read full source, not just quoted part |

### Data Visualization Manipulation

| Manipulation | How to Spot |
|--------------|-------------|
| **Truncated Y-axis** | Check if axis starts at zero |
| **Misleading scale** | Compare apparent vs actual difference |
| **Cherry-picked timeframe** | Ask for longer historical view |
| **Dual Y-axes abuse** | Check if scales are comparable |
| **3D distortion** | Look for perspective tricks |
| **Binning manipulation** | Check if bins chosen to hide patterns |

---

## Claim Categorization

### Research Claim Types

| Type | Verifiability | Verification Approach |
|------|---------------|----------------------|
| **Empirical Fact** | High | Find original data/study |
| **Statistical Finding** | Medium-High | Check methods, replication |
| **Causal Claim** | Medium | Assess study design quality |
| **Generalization** | Medium-Low | Check population validity |
| **Prediction** | Low | Note assumptions, track record |
| **Expert Opinion** | Low | Note as opinion, check expertise |

### Strength of Evidence Hierarchy

| Evidence Type | Strength | Caveats |
|---------------|----------|---------|
| **Meta-analysis of RCTs** | Very Strong | Check for heterogeneity |
| **Large pre-registered RCT** | Strong | Check execution fidelity |
| **RCT** | Good | Check randomization, blinding |
| **Prospective Cohort** | Moderate | Can't establish causation |
| **Case-Control** | Moderate-Weak | Recall bias issues |
| **Cross-sectional** | Weak | Snapshot only |
| **Case Series** | Very Weak | No control group |
| **Expert Opinion** | Weakest | Not empirical evidence |

---

## Common Research Misrepresentation

### Pattern 1: "Studies Show"

**Indicator**: Vague reference to "research" or "studies" without specifics.

**Verification**:
- Which specific study?
- Published where?
- Sample size and methodology?
- Has it been replicated?

**Red Flag Phrases**:
- "Research shows..."
- "Scientists have found..."
- "Studies suggest..."
- "Experts agree..."

### Pattern 2: Correlation as Causation

**Indicator**: Causal language for observational data.

**Questions**:
- Was this an experiment or observation?
- What confounders exist?
- Is reverse causation possible?
- What's the proposed mechanism?

**Red Flag Phrases**:
- "X causes Y" (from correlational study)
- "X leads to Y"
- "X results in Y"

### Pattern 3: Relative vs Absolute Risk

**Indicator**: Dramatic relative risk without context.

**Example**:
- "Drug X doubles your risk!" (relative)
- Actual: 0.001% → 0.002% (absolute)

**Questions**:
- What's the baseline risk?
- What's the absolute risk change?
- What's the NNT (Number Needed to Treat)?

### Pattern 4: Single Study Syndrome

**Indicator**: Major claim based on one study.

**Questions**:
- Has this been replicated?
- What do meta-analyses say?
- Any contradicting studies?
- Is this a preprint or peer-reviewed?

### Pattern 5: Survivorship Bias

**Indicator**: Only success cases examined.

**Questions**:
- What about the failures?
- Is the sample representative?
- Selection effects at play?

---

## Source Quality Assessment

### Journal Quality Indicators

| Indicator | Good Sign | Warning Sign |
|-----------|-----------|--------------|
| **Peer Review** | Rigorous process described | No/minimal review |
| **Impact Factor** | Established in field | Very new, no metrics |
| **Publisher** | Reputable academic press | Unknown/predatory |
| **Retraction Rate** | Low, transparent process | High or hidden |
| **Editorial Board** | Known experts | Unknown/fake names |

### Preprint Caution

| Consideration | Note |
|---------------|------|
| **Not peer-reviewed** | May have errors, lower confidence |
| **Subject to change** | Check for published version |
| **Faster dissemination** | Good for cutting-edge, risky for conclusions |
| **Version tracking** | Note which version you read |

### Predatory Publishing Red Flags

| Red Flag | Description |
|----------|-------------|
| **Spam solicitation** | Unsolicited publication invitations |
| **Fake metrics** | Made-up impact factors |
| **Fast acceptance** | Unrealistically quick review |
| **Broad scope** | "Journal of Everything" |
| **Poor website** | Spelling errors, broken links |
| **Hidden fees** | Fees not disclosed upfront |

---

## Verification Workflows

### Quick Citation Check (5 min)

1. Find the cited source
2. Search for the specific claim in source
3. Read surrounding context
4. Confirm claim is accurately represented
5. Note any discrepancies

### Deep Source Verification (30 min)

1. Obtain full text of primary source
2. Identify key methodology and findings
3. Check if conclusions match claims made about it
4. Look for limitations acknowledged by authors
5. Search for replication studies
6. Check for retractions or corrections
7. Document verification status

### Statistical Claim Verification

1. Find original data or study
2. Check sample size and power
3. Verify statistical test appropriateness
4. Look for effect sizes, not just p-values
5. Check for multiple comparison corrections
6. Note any pre-registration

---

## Confidence Calibration

### Evidence Strength Boosters

| Indicator | Confidence Boost |
|-----------|------------------|
| Primary source verified | +0.20 |
| Replicated finding | +0.20 |
| Pre-registered study | +0.15 |
| Large, well-powered study | +0.15 |
| Peer-reviewed publication | +0.10 |
| Effect size meaningful | +0.10 |

### Confidence Penalties

| Concern | Confidence Penalty |
|---------|-------------------|
| Cannot find primary source | -0.25 |
| Single unreplicated study | -0.20 |
| Citation doesn't support claim | -0.30 |
| Predatory journal | -0.25 |
| Significant methodological flaws | -0.20 |
| P-hacking indicators | -0.20 |
| Only relative risk reported | -0.10 |

---

## Red Flags Quick Reference

### Immediate Skepticism Triggers

| Trigger | Action |
|---------|--------|
| "Studies show" without citation | Demand specific source |
| Extraordinary claim | Require extraordinary evidence |
| Confirms existing bias too neatly | Extra scrutiny |
| Single study, major conclusion | Look for replications |
| Preprint presented as fact | Note limitations |
| Press release, not paper | Find original study |
| "Breakthrough" language | Marketing, not science |
| No limitations acknowledged | Incomplete picture |
