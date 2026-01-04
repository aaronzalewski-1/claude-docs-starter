---
name: methodologist-knowledge
description: Domain expertise for Methodologist persona - research design, validity frameworks, statistical evaluation
type: persona_skill
persona: personas/research/methodologist
version: 1.0.0
---

# Methodologist Domain Knowledge

> Research design evaluation, validity assessment, and methodological rigor frameworks.

---

## Research Design Classification

### Quantitative Designs

| Design | Purpose | Strength | Weakness |
|--------|---------|----------|----------|
| **Experimental (RCT)** | Establish causation | Strong internal validity | Often artificial conditions |
| **Quasi-experimental** | Test causation without randomization | More practical | Selection bias risk |
| **Correlational** | Identify relationships | Large samples possible | Cannot prove causation |
| **Survey/Cross-sectional** | Describe population at point in time | Efficient | No temporal sequence |
| **Longitudinal** | Track changes over time | Shows change patterns | Expensive, attrition |

### Qualitative Designs

| Design | Purpose | Strength | Weakness |
|--------|---------|----------|----------|
| **Phenomenological** | Understand lived experience | Rich depth | Small samples |
| **Grounded theory** | Generate theory from data | Data-driven | Time intensive |
| **Ethnographic** | Understand culture/context | Natural setting | Observer effects |
| **Case study** | Deep dive single instance | Comprehensive | Limited generalizability |
| **Narrative** | Understand through stories | Captures complexity | Interpretation challenges |

### Mixed Methods

| Approach | When to Use |
|----------|-------------|
| **Sequential explanatory** | Quantitative first, qualitative explains |
| **Sequential exploratory** | Qualitative first, quantitative tests |
| **Convergent** | Simultaneous, compare results |
| **Embedded** | One method supports the other |

---

## Validity Frameworks

### Internal Validity Threats

| Threat | Description | Detection | Mitigation |
|--------|-------------|-----------|------------|
| **History** | External events affect outcome | Check timeline for events | Control group, short duration |
| **Maturation** | Natural development over time | Long study, no controls | Control group |
| **Testing** | Pre-test affects post-test | Pre-test administered | Solomon four-group design |
| **Instrumentation** | Measurement changes | Different raters/tools | Standardize, calibrate |
| **Regression** | Extreme scores regress to mean | Selected for extremes | Random selection |
| **Selection** | Groups differ at start | Non-random assignment | Randomization, matching |
| **Attrition** | Differential dropout | Compare completers/dropouts | Intent-to-treat analysis |
| **Diffusion** | Treatment spreads to control | Groups can communicate | Physical separation |
| **Compensation** | Control receives other benefits | Control seems disadvantaged | Monitor, document |
| **Rivalry** | Control tries harder | Competition between groups | Blind conditions |
| **Demoralization** | Control performs worse | Control knows status | Blind, active control |

### External Validity Dimensions

| Dimension | Question | Threats |
|-----------|----------|---------|
| **Population** | To whom does this generalize? | Sample selection, volunteer bias |
| **Ecological** | To what settings? | Lab vs. field, Hawthorne effect |
| **Temporal** | To what times? | Historical context, trends |
| **Treatment** | To what variations? | Dosage, fidelity, components |

### Construct Validity

| Threat | Description |
|--------|-------------|
| **Inadequate explication** | Construct poorly defined |
| **Construct confounding** | Measuring multiple constructs |
| **Mono-operation bias** | Single operationalization |
| **Mono-method bias** | Single measurement method |
| **Evaluation apprehension** | Awareness affects behavior |
| **Experimenter expectancies** | Researcher bias |

---

## Statistical Evaluation Criteria

### Power and Sample Size

| Effect Size | Small Sample Risk |
|-------------|-------------------|
| Large (d > 0.8) | May detect with n = 20-30 |
| Medium (d = 0.5) | Need n = 50-100 |
| Small (d = 0.2) | Need n = 200+ |

**Power Analysis Checklist:**
- [ ] Was power analysis conducted a priori?
- [ ] Is power >= 0.80?
- [ ] Was effect size estimated reasonably?
- [ ] Is sample size justified?

### Statistical Test Selection

| Data Type | Groups | Parametric | Non-Parametric |
|-----------|--------|------------|----------------|
| Continuous | 2 independent | t-test | Mann-Whitney |
| Continuous | 2 paired | Paired t-test | Wilcoxon |
| Continuous | 3+ independent | ANOVA | Kruskal-Wallis |
| Categorical | 2 | Chi-square | Fisher's exact |
| Continuous predictor | Continuous outcome | Regression | Spearman |

### Common Statistical Errors

| Error | Description | Red Flag |
|-------|-------------|----------|
| **P-hacking** | Testing until p < 0.05 | Many comparisons, selective reporting |
| **HARKing** | Hypothesizing after results | Post-hoc "predictions" |
| **Multiple comparisons** | Inflated Type I error | No correction (Bonferroni, FDR) |
| **Violated assumptions** | Tests misapplied | No assumption checking |
| **Overfitting** | Model too complex | Parameters ~ sample size |
| **Effect size ignored** | Only report p-values | No practical significance |

---

## Quality Assessment Rubrics

### Quantitative Study Quality

| Criterion | Questions | Weight |
|-----------|-----------|--------|
| **Research design** | Appropriate for question? | High |
| **Sampling** | Representative? Adequate size? | High |
| **Measurement** | Valid? Reliable? | High |
| **Analysis** | Appropriate tests? Assumptions met? | Medium |
| **Confounds** | Controlled? Acknowledged? | High |
| **Reporting** | Complete? Transparent? | Medium |

### Qualitative Study Quality

| Criterion | Questions | Weight |
|-----------|-----------|--------|
| **Credibility** | Triangulation? Member checking? | High |
| **Transferability** | Thick description? Context? | Medium |
| **Dependability** | Audit trail? | Medium |
| **Confirmability** | Reflexivity? Bias acknowledged? | High |
| **Sampling** | Purposive? Theoretical saturation? | Medium |

### Systematic Review Quality (PRISMA)

| Element | Requirement |
|---------|-------------|
| **Protocol** | Registered? Published? |
| **Search** | Multiple databases? Grey literature? |
| **Selection** | Clear criteria? Duplicate screening? |
| **Data extraction** | Standardized? Duplicate? |
| **Bias assessment** | Risk of bias tool used? |
| **Synthesis** | Appropriate? Heterogeneity assessed? |

---

## Bias Detection

### Types of Bias

| Bias Type | Stage | Detection |
|-----------|-------|-----------|
| **Selection bias** | Sampling | Compare sample to population |
| **Response bias** | Data collection | Check response patterns |
| **Measurement bias** | Instrumentation | Calibration, validation |
| **Publication bias** | Reporting | Funnel plot, file drawer estimate |
| **Funding bias** | Throughout | Disclose, analyze by funder |
| **Confirmation bias** | Analysis | Pre-registration, blinding |
| **Survivorship bias** | Sampling | Consider failures/dropouts |

### Bias Risk Assessment

| Risk Level | Indicators |
|------------|------------|
| **Low** | Randomization, blinding, complete reporting |
| **Moderate** | Some controls, partial blinding |
| **High** | No controls, selective reporting |
| **Critical** | Fundamental design flaws |

---

## Confidence Calibration

### Quality Indicators

| Indicator | Confidence Boost |
|-----------|------------------|
| Pre-registration | +0.15 |
| Replication study | +0.20 |
| Large sample (powered) | +0.10 |
| Multiple measures | +0.10 |
| Independent replication | +0.25 |
| Peer review | +0.10 |

### Quality Concerns

| Concern | Confidence Penalty |
|---------|-------------------|
| No control group | -0.20 |
| Small sample | -0.15 |
| Multiple comparisons uncorrected | -0.15 |
| High attrition | -0.10 |
| Single measurement | -0.10 |
| Conflicts of interest | -0.15 |
