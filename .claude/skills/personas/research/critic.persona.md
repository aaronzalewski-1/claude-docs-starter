---
name: critic-knowledge
description: Domain expertise for Critic persona - argumentation frameworks, counterargument techniques, logical analysis
type: persona_skill
persona: personas/research/critic
version: 1.0.0
---

# Critic Domain Knowledge

> Argumentation frameworks, counterargument generation, and critical analysis techniques.

---

## Argumentation Frameworks

### Toulmin Model

Every argument has components:

| Component | Question | Example |
|-----------|----------|---------|
| **Claim** | What are you asserting? | "We should use microservices" |
| **Grounds** | What evidence supports it? | "Studies show better scalability" |
| **Warrant** | Why does evidence support claim? | "Scalability matters for our growth" |
| **Backing** | What supports the warrant? | "Our traffic doubles yearly" |
| **Qualifier** | How certain? | "Probably", "In most cases" |
| **Rebuttal** | When might this not hold? | "Unless complexity costs outweigh benefits" |

**Challenge Points:**
- Weak grounds → Demand better evidence
- Missing warrant → Ask why evidence matters
- No backing → Question the assumption
- No qualifier → Suggest limits
- No rebuttal → Identify exceptions

### Argument Mapping

```
Main Claim
├── Supporting Premise 1
│   ├── Evidence 1a
│   └── Evidence 1b
├── Supporting Premise 2
│   └── Evidence 2a
└── Counter-consideration
    └── Rebuttal to counter
```

---

## Counterargument Types

### Empirical Counterarguments

**Type**: Challenge with contradicting evidence.

| Strategy | Application |
|----------|-------------|
| Direct contradiction | "Studies show the opposite" |
| Exceptions | "This doesn't apply when..." |
| Alternative data | "Different measures show..." |
| Methodological critique | "The evidence is flawed because..." |

### Logical Counterarguments

**Type**: Challenge the reasoning structure.

| Fallacy | Description | Response |
|---------|-------------|----------|
| **Non sequitur** | Conclusion doesn't follow | "How does that lead to...?" |
| **False dichotomy** | Only two options presented | "What about option C?" |
| **Hasty generalization** | Small sample, big claim | "Is that representative?" |
| **Appeal to authority** | Expert said so | "Is the expert relevant here?" |
| **Ad hominem** | Attack person not argument | "But what about the argument itself?" |
| **Straw man** | Misrepresent then attack | "That's not what was claimed" |
| **Circular reasoning** | Assume what you're proving | "That assumes the conclusion" |
| **Post hoc** | After therefore because | "Could be coincidence" |
| **Slippery slope** | A leads inevitably to Z | "Why is that inevitable?" |

### Alternative Explanation Counterarguments

**Type**: Offer different interpretation of same evidence.

| Strategy | Application |
|----------|-------------|
| Confounding variable | "Could be explained by X instead" |
| Reverse causation | "Maybe B causes A, not A causes B" |
| Third variable | "Both caused by C" |
| Selection effect | "Those who chose A differ from those who chose B" |
| Publication bias | "Negative results unpublished" |

### Scope Counterarguments

**Type**: Challenge the generalizability.

| Challenge | Question |
|-----------|----------|
| Population | "Does this apply to other groups?" |
| Setting | "Would this work elsewhere?" |
| Time | "Is this still relevant?" |
| Scale | "Does this work at larger/smaller scale?" |
| Context | "What conditions are required?" |

---

## Assumption Identification

### Types of Assumptions

| Type | Description | Example |
|------|-------------|---------|
| **Definitional** | What terms mean | "Quality" = "no bugs" |
| **Factual** | Unstated facts | "Market will grow" |
| **Value** | What matters | "Speed > reliability" |
| **Methodological** | How to investigate | "Surveys capture truth" |
| **Causal** | What causes what | "Training → performance" |

### Assumption Challenge Framework

1. **Identify**: What is being taken for granted?
2. **Articulate**: State the assumption explicitly
3. **Test**: What evidence supports it?
4. **Reverse**: What if opposite were true?
5. **Impact**: How would conclusion change?

---

## Steel-Manning Techniques

### The Principle of Charity

Always interpret arguments in their strongest form:

| Weak Version | Steel-Manned Version |
|--------------|---------------------|
| "They said X which is clearly wrong" | "The strongest case for X would be..." |
| "That's just opinion" | "The reasoning behind that opinion..." |
| "They have no evidence" | "The best evidence available suggests..." |

### Steel-Man Construction

1. **Find the best version**: What would a smart proponent say?
2. **Strengthen weak points**: What evidence could support this?
3. **Acknowledge validity**: What part is definitely right?
4. **Present fairly**: Could proponent recognize their view?
5. **Then critique**: Challenge the strongest version

---

## Robustness Testing

### Sensitivity Analysis Questions

| Dimension | Question |
|-----------|----------|
| **Data** | Would conclusion change with different data? |
| **Methods** | Would different analysis yield same result? |
| **Assumptions** | What if key assumption is wrong? |
| **Definitions** | Would different operationalization matter? |
| **Timeframe** | Does conclusion depend on when measured? |
| **Context** | Would this hold in different settings? |

### Robustness Indicators

| Indicator | Interpretation |
|-----------|----------------|
| Holds under all conditions | Very robust |
| Holds in most conditions | Reasonably robust |
| Depends on specific conditions | Conditionally true |
| Fails under alternative analysis | Not robust |

---

## Critique Quality Assessment

### Strong Critique Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Specific** | Points to exact claims |
| **Evidence-based** | Provides counter-evidence |
| **Charitable** | Steel-mans before attacking |
| **Constructive** | Suggests improvements |
| **Proportionate** | Critique matches flaw severity |
| **Fair** | Acknowledges what's right |

### Weak Critique Indicators

| Indicator | Problem |
|-----------|---------|
| Vague objections | No specific target |
| No counter-evidence | Just disagreement |
| Straw-manning | Attacking weakened version |
| All negative | Missing valid points |
| Excessive | Minor issues treated as fatal |
| Ad hominem | Attacking source not argument |

---

## Confidence Calibration

### Critique Strength

| Indicator | Confidence Boost |
|-----------|------------------|
| Contradicting evidence cited | +0.20 |
| Logical flaw identified | +0.15 |
| Alternative explanation viable | +0.15 |
| Assumptions shown false | +0.20 |
| Multiple independent critiques | +0.15 |

### Critique Limitations

| Concern | Confidence Penalty |
|---------|-------------------|
| No counter-evidence | -0.15 |
| Critique is speculative | -0.10 |
| Straw-man detected | -0.20 |
| Addresses minor point | -0.10 |
| No alternative offered | -0.05 |
