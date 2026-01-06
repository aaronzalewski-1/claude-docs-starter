---
name: review-{{PACKAGE}}-decision
description: Multi-persona {{DOMAIN}} review. Use when evaluating {{REVIEW_TRIGGERS}}. Triggers on phrases like {{TRIGGER_PHRASES}}.
---

# {{DOMAIN}} Decision Review

Run a comprehensive multi-persona analysis for {{DOMAIN_LOWERCASE}} decisions.

## Decision Under Review

$ARGUMENTS

---

## Process

### Step 1: Context Detection

Identify the decision context:
- **Decision Type**: {{DECISION_TYPES}}
- **Key Stakeholders**: {{STAKEHOLDERS}}
- **Time Horizon**: {{TIME_HORIZONS}}

### Step 2: Run Persona Analyses

Execute each persona in sequence, capturing their analysis:

{{PERSONA_LIST}}

### Step 3: Synthesize Results

After all personas have analyzed the decision:

1. **Identify Consensus Areas** - Where do personas agree?
2. **Surface Conflicts** - Where do perspectives diverge (>0.3 confidence gap)?
3. **Weight by Context** - Apply contextual weighting based on decision type
4. **Form Recommendation** - Synthesize into actionable guidance

---

## Contextual Weighting

Weights vary based on the decision context:

{{WEIGHTING_TABLE}}

---

## Output Format

### Individual Analyses

For each persona, present:
```
### [Persona Name]

**Assessment**: [Summary in 2-3 sentences]

**Key Concerns**:
- [Concern 1]
- [Concern 2]

**Recommendation**: [Recommend/Caution/Block]
**Confidence**: [0.0-1.0]
```

### Weighted Consensus

| Persona | Weight | Confidence | Weighted Score | Recommendation |
|---------|--------|------------|----------------|----------------|
{{CONSENSUS_TABLE_ROWS}}
| **Consensus** | | | **[Avg]** | **[Final]** |

### Key Tensions

If any personas have confidence divergence > 0.3:

| Tension | Personas | Resolution Path |
|---------|----------|-----------------|
| [Issue] | [A] vs [B] | [How to resolve] |

### Final Recommendation

**[Proceed/Proceed with Caution/Reconsider/Block]**

[2-3 paragraph synthesis explaining the recommendation, key considerations, and suggested next steps]

### What Can Wait

Items that can be deferred or aren't critical for this decision:
- [Deferrable item 1]
- [Deferrable item 2]

---

## Next Steps

After review completion:

1. **Save as Artifact**: Re-run with `--save <name>` to generate a formal document
2. **Deep Dive**: Run individual persona for more detail
3. **Implement**: Use `/DEEPPLAN` to plan implementation

---

*{{PACKAGE_TITLE}} Package - {{PERSONA_COUNT}} Personas*
