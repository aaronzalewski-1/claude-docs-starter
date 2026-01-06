---
name: core-anthropic-expert-knowledge
description: Domain expertise for Anthropic Expert persona - Claude best practices, dynamic prompt engineering, constitutional AI principles, and effective LLM interaction patterns
type: persona_skill
persona: personas/core/anthropic-expert
version: 2.0.0
---

# Anthropic Expert Domain Knowledge

> Authoritative guidance on Anthropic best practices, Claude capabilities, dynamic prompt engineering, and effective AI interaction patterns.

---

## Core Anthropic Principles

### Constitutional AI Foundation

**Definition**: Claude is trained using Constitutional AI (CAI), which guides behavior through explicit principles rather than only human feedback.

| Principle | Implication for Prompting |
|-----------|---------------------------|
| Helpfulness | Claude aims to be maximally helpful within safety bounds |
| Harmlessness | Claude refuses genuinely harmful requests |
| Honesty | Claude acknowledges uncertainty and limitations |

**Key Insight**: Work with Claude's training, not against it. Clear, direct requests aligned with these principles yield better results than attempts to circumvent them.

---

## Dynamic Prompt Engineering

### What is Dynamic Prompt Engineering?

**Definition**: Constructing prompts programmatically based on context, user input, or system state rather than using static prompt templates.

| Approach | Use Case | Example |
|----------|----------|---------|
| **Template Interpolation** | Variable insertion | `Analyze {document_type}: {content}` |
| **Conditional Sections** | Context-dependent instructions | Include RAG context only when available |
| **Adaptive Complexity** | Match prompt to task difficulty | Simple tasks get minimal prompts |
| **Role Composition** | Combine personas dynamically | Domain expert + format specialist |

### Dynamic Prompt Patterns

#### Pattern 1: Contextual Priming

```
Base prompt + Domain context + Task-specific instructions + Output format
```

**When to use**: Complex tasks requiring domain knowledge and specific outputs.

**Example structure**:
```
You are assisting with {domain}.

Background context:
{retrieved_context}

Task: {specific_task}

Respond in {format} format.
```

#### Pattern 2: Progressive Disclosure

**Definition**: Reveal information incrementally based on need.

| Stage | Content | Purpose |
|-------|---------|---------|
| Initial | Core task only | Minimize distraction |
| On-demand | Supporting details | Add when relevant |
| Fallback | Recovery instructions | Handle edge cases |

**When to use**: Multi-turn conversations where context builds over time.

#### Pattern 3: Adaptive Persona Selection

```
if task.requires_technical_depth:
    include_persona("domain_expert")
if task.requires_structure:
    include_persona("format_specialist")
if task.is_high_stakes:
    include_persona("safety_reviewer")
```

**When to use**: Tasks with varying requirements across dimensions.

---

## Prompt Engineering Best Practices

### Clarity and Structure

| Practice | Why It Works |
|----------|--------------|
| **Be direct** | Claude responds well to clear, unambiguous requests |
| **Use XML tags** | `<context>`, `<task>`, `<output>` improve parsing |
| **Separate concerns** | Distinct sections for context, task, format |
| **Provide examples** | Few-shot learning improves consistency |

### XML Tag Usage

**Recommended tags**:
```xml
<context>Background information</context>
<task>What to do</task>
<constraints>Limitations or requirements</constraints>
<output_format>Expected response structure</output_format>
<examples>Few-shot examples</examples>
```

**Why XML works**:
- Unambiguous section boundaries
- Easy to parse programmatically
- Familiar from Claude's training data
- Supports nested structure

### Effective Instructions

| Good | Avoid |
|------|-------|
| "List three key points" | "Tell me everything about..." |
| "Respond in JSON format with fields: name, value" | "Give me some structured data" |
| "If uncertain, say 'I'm not sure'" | (Assuming Claude will always guess) |
| "Focus on X, Y, Z aspects" | "Be comprehensive" (unbounded) |

---

## Claude-Specific Capabilities

### Strengths to Leverage

| Capability | Best Use | Prompt Approach |
|------------|----------|-----------------|
| **Long context** | Document analysis, multi-source synthesis | Provide full context, reference by section |
| **Structured output** | JSON, XML, tables, code | Explicit format specification with examples |
| **Nuanced reasoning** | Complex analysis, tradeoff evaluation | Ask for reasoning before conclusions |
| **Instruction following** | Multi-step workflows | Numbered steps, clear success criteria |
| **Self-correction** | Iterative refinement | Ask Claude to review its own output |

### Limitations to Navigate

| Limitation | Mitigation Strategy |
|------------|---------------------|
| **Knowledge cutoff** | Provide current context, use tools for real-time data |
| **Cannot execute code** | Provide execution results, use tool integration |
| **No persistent memory** | Include relevant prior context in prompts |
| **May be overly cautious** | Clarify legitimate use cases explicitly |
| **Confidence vs. accuracy** | Request uncertainty acknowledgment |

---

## System Prompt Design

### Effective System Prompts

**Structure**:
```
1. Role definition (who Claude is in this context)
2. Context (what the user is trying to accomplish)
3. Behavioral guidelines (how to respond)
4. Constraints (what to avoid)
5. Output expectations (format, length, style)
```

**Example template**:
```
You are a {role} helping users with {domain}.

Context: {background_about_the_application}

Guidelines:
- {behavioral_guideline_1}
- {behavioral_guideline_2}

Constraints:
- {constraint_1}
- {constraint_2}

Respond in {style} style, keeping responses {length_guidance}.
```

### System Prompt Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| Overly long prompts | Dilutes focus | Prioritize essential instructions |
| Contradictory rules | Confuses behavior | Test for conflicts |
| Vague role definitions | Inconsistent responses | Specific, actionable role |
| No examples | Ambiguous expectations | Include 1-2 concrete examples |
| Attempting jailbreaks | Unreliable, may fail | Work within guidelines |

---

## Few-Shot Learning

### When to Use Few-Shot Examples

| Scenario | Example Count | Purpose |
|----------|---------------|---------|
| Novel format | 2-3 examples | Establish pattern |
| Edge case handling | 1-2 per edge case | Show boundary behavior |
| Tone/style | 1-2 examples | Calibrate voice |
| Complex reasoning | 1 detailed example | Demonstrate process |

### Example Structure

```xml
<examples>
<example>
<input>User query or context</input>
<output>Expected response format and content</output>
<reasoning>Why this output is correct (optional)</reasoning>
</example>
</examples>
```

### Few-Shot Best Practices

| Practice | Rationale |
|----------|-----------|
| Use realistic examples | Synthetic examples may mislead |
| Include edge cases | Prevent failure modes |
| Match target format exactly | Formatting is learned from examples |
| Order examples strategically | Recent examples have more influence |

---

## Chain of Thought and Reasoning

### When to Request Explicit Reasoning

| Use Chain-of-Thought | Skip Chain-of-Thought |
|---------------------|----------------------|
| Complex analysis | Simple factual queries |
| Multi-step problems | Direct format conversion |
| Decisions with tradeoffs | Straightforward instructions |
| Debugging/troubleshooting | Routine operations |

### Prompting for Reasoning

**Explicit approach**:
```
Think through this step by step:
1. First, identify...
2. Then, analyze...
3. Finally, conclude...

Show your reasoning, then provide your final answer.
```

**Structured reasoning output**:
```xml
<reasoning>
Step-by-step analysis here
</reasoning>
<conclusion>
Final answer here
</conclusion>
```

---

## Tool Use and Function Calling

### Designing Tool Descriptions

| Element | Best Practice |
|---------|---------------|
| **Name** | Clear, action-oriented (e.g., `search_database`) |
| **Description** | When and why to use the tool |
| **Parameters** | Explicit types, constraints, examples |
| **Return format** | What the tool returns |

### Tool Use Patterns

**Pattern: Prefer tools for real-time data**
```
When asked about current information (dates, prices, availability),
use the appropriate tool rather than relying on training data.
```

**Pattern: Chain tools logically**
```
1. Use search_tool to find relevant items
2. Use get_details_tool to expand on selected items
3. Synthesize results for the user
```

---

## Safety and Alignment Considerations

### Working Within Guidelines

| Approach | Why It Works |
|----------|--------------|
| Explain legitimate purpose | Disambiguates intent |
| Provide appropriate context | Helps Claude understand scope |
| Accept reasonable refusals | Safety features are intentional |
| Rephrase if unclear | Clarity often resolves caution |

### Handling Sensitive Topics

| Topic Type | Recommended Approach |
|------------|---------------------|
| Security/pentesting | Clarify authorization context |
| Medical/legal | Note informational vs. advice distinction |
| Controversial topics | Request balanced, factual treatment |
| Code review | Focus on analysis, not exploitation |

---

## Prompt Optimization

### Iteration Workflow

```
1. Start simple -> Test -> Identify failure modes
2. Add constraints -> Test -> Check for over-constraint
3. Add examples -> Test -> Verify generalization
4. Refine wording -> Test -> Measure consistency
```

### Measuring Prompt Quality

| Metric | How to Assess |
|--------|---------------|
| **Consistency** | Same input -> same output pattern |
| **Accuracy** | Factual correctness of responses |
| **Format compliance** | Adherence to requested structure |
| **Completeness** | All required elements present |
| **Efficiency** | Minimal tokens for desired output |

### Common Optimization Targets

| Issue | Optimization |
|-------|--------------|
| Responses too verbose | Add length constraints, "be concise" |
| Missing edge cases | Add few-shot examples for edges |
| Wrong format | Provide explicit format example |
| Over-cautious | Clarify legitimate use case |
| Under-cautious | Add safety reminders |

---

## Evaluation Criteria for Prompt Decisions

### Decision Quality Checklist

When evaluating a prompting approach:

- [ ] **Clarity**: Is the prompt unambiguous?
- [ ] **Alignment**: Does it work with Claude's training, not against it?
- [ ] **Structure**: Are sections clearly delineated?
- [ ] **Examples**: Are appropriate few-shot examples included?
- [ ] **Constraints**: Are limitations explicit and reasonable?
- [ ] **Format**: Is the expected output format clear?
- [ ] **Efficiency**: Is the prompt as concise as possible while being complete?
- [ ] **Testability**: Can we measure if this prompt works?

### Confidence Calibration

| Evidence Quality | Confidence Modifier |
|------------------|---------------------|
| Follows Anthropic documentation | +0.15 |
| Tested with multiple inputs | +0.1 |
| Uses recommended patterns (XML tags, etc.) | +0.1 |
| Clear, unambiguous instructions | +0.05 |
| Novel/experimental approach | -0.1 |
| Contradicts Anthropic guidance | -0.2 |
| Attempts to circumvent safety | -0.3 |

---

## Authoritative References

| Reference | Purpose | Link |
|-----------|---------|------|
| Anthropic Documentation | Official Claude usage guides | [docs.anthropic.com](https://docs.anthropic.com) |
| Claude Prompt Engineering | Prompting best practices | [docs.anthropic.com/claude/docs/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |
| Anthropic Research | Constitutional AI, RLHF papers | [anthropic.com/research](https://www.anthropic.com/research) |
| Claude Model Card | Capabilities and limitations | [anthropic.com/claude](https://www.anthropic.com/claude) |
