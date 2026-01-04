---
name: skeptic-knowledge
description: Domain expertise for Skeptic persona - verification frameworks, source credibility, claim categorization
type: persona_skill
persona: personas/product/skeptic
version: 1.0.0
---

# Skeptic Domain Knowledge

> Verification frameworks, source hierarchies, and claim categorization for rigorous fact-checking.

---

## Source Credibility Hierarchy

### Tier 1: Authoritative Sources (Highest Trust)

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Official Documentation | Framework docs, RFC specs, vendor docs | 0.95 |
| First-party SDK Source | GitHub repos from framework maintainers | 0.90 |
| API Reference (versioned) | Swagger/OpenAPI from official sources | 0.90 |

**When to use**: Always prefer these for technical claims about features, behaviors, limits.

### Tier 2: Vetted Secondary Sources (Good Trust)

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Published Benchmarks | TechEmpower, official performance guides | 0.80 |
| Conference Talks (official) | Vendor conferences, recorded talks | 0.75 |
| Established Tech Media | InfoQ, The Register (technical pieces) | 0.70 |

**When to use**: Cross-reference with Tier 1 when possible.

### Tier 3: Community Sources (Verify Required)

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Stack Overflow (high votes) | Answers with 50+ votes, accepted | 0.60 |
| Well-maintained blogs | Individual developer blogs, Medium (tech) | 0.50 |
| GitHub Issues/Discussions | Insights on edge cases and bugs | 0.50 |

**When to use**: Good for real-world experiences, but verify claims against Tier 1.

### Tier 4: Unverified Sources (Low Trust)

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Random blog posts | Undated, unknown author | 0.30 |
| AI-generated content | ChatGPT answers, AI summaries | 0.20 |
| Outdated documentation | >2 years old for fast-moving tech | 0.20 |

**When to use**: Starting points only. Always verify.

---

## Claim Categorization Framework

### Category 1: Factual Claims

**Definition**: Objectively verifiable statements about how something works.

| Claim Type | Verification Method | Example |
|------------|---------------------|---------|
| API Behavior | Read source code or docs | "This ORM supports batch updates" |
| Feature Existence | Check official docs | "The API has rate limiting" |
| Version Compatibility | Check release notes | "Library X supports version Y" |

**Required Evidence**: Link to official documentation or source code.

### Category 2: Performance Claims

**Definition**: Statements about speed, scale, or resource usage.

| Claim Type | Verification Method | Example |
|------------|---------------------|---------|
| Throughput | Benchmarks, load tests | "Redis handles 100k ops/sec" |
| Latency | Measured P50/P99 | "Cold start is 200ms" |
| Memory Usage | Profiling data | "This approach avoids allocations" |

**Required Evidence**: Benchmark data with methodology, or "unverified - needs testing".

### Category 3: Best Practice Claims

**Definition**: Statements about recommended approaches.

| Claim Type | Verification Method | Example |
|------------|---------------------|---------|
| Design Pattern | Source in authoritative guide | "Repository pattern for data access" |
| Security Practice | OWASP, official security guides | "Use parameterized queries" |
| Architecture Style | Vendor architecture guides | "Prefer composition over inheritance" |

**Required Evidence**: Citation to recognized authority or explicit "opinion".

### Category 4: Predictive Claims

**Definition**: Statements about future outcomes.

| Claim Type | Verification Method | Example |
|------------|---------------------|---------|
| Scalability | Historical data, architecture analysis | "This will scale to 10k users" |
| Maintenance | Similar project history | "This approach reduces tech debt" |
| Adoption | Market trends | "This technology will become mainstream" |

**Required Evidence**: Reasoning and assumptions made explicit. Cannot be fully verified.

---

## Technology Lifecycle Awareness

### Lifecycle Stages

| Stage | Characteristics | Trust for Production |
|-------|-----------------|---------------------|
| **Alpha** | Incomplete, breaking changes expected | Do not use |
| **Beta/Preview** | Feature-complete, may have bugs | Test only |
| **Release Candidate** | Stable, final testing | Cautious production |
| **GA (General Availability)** | Production-ready, supported | Yes |
| **Maintenance Mode** | Security fixes only | Consider migration |
| **Deprecated** | End-of-life announced | Plan migration |
| **End of Life** | No support | Do not use |

### Version-Specific Verification

| Technology | How to Check Lifecycle |
|------------|----------------------|
| Major frameworks | Official support policy pages |
| Cloud services | Vendor updates blog, service pages |
| Package managers | Repository activity, last publish date |
| Libraries | GitHub repo activity, issue response time |

---

## Common Unverified Assumption Patterns

### Pattern 1: "It Works This Way"

**Indicator**: Claim about API/framework behavior without documentation reference.

**Questions to ask**:
- Where is this documented?
- Which version was this tested against?
- Does this apply to our specific configuration?

### Pattern 2: "Best Practice"

**Indicator**: Assertion that something is "the right way" without context.

**Questions to ask**:
- Best practice according to whom?
- In what context? (scale, team size, domain)
- What are the tradeoffs?

### Pattern 3: "Performance"

**Indicator**: Claims about speed/efficiency without measurements.

**Questions to ask**:
- Measured or assumed?
- Under what load/conditions?
- What's the comparison baseline?

### Pattern 4: "Everyone Uses This"

**Indicator**: Appeal to popularity without evidence.

**Questions to ask**:
- Who specifically uses this?
- In what context?
- What problems did they encounter?

### Pattern 5: "This Will Scale"

**Indicator**: Future performance claims without analysis.

**Questions to ask**:
- Based on what architecture analysis?
- What are the bottlenecks?
- What happens at 10x current load?

---

## Verification Workflows

### Quick Verification (5 min)

1. Search: `[claim] site:official-docs-url` (or relevant official docs)
2. Check version: Is the doc for our version?
3. Confirm: Does the doc explicitly support the claim?
4. Flag: If not found, mark as "unverified"

### Deep Verification (30 min)

1. Find authoritative source
2. Trace claim to specific documentation
3. Check for version-specific notes
4. Look for counterexamples
5. Document evidence or uncertainty

### Code Verification

1. Read the actual implementation
2. Check for configuration that affects behavior
3. Write a minimal test case
4. Document findings with line numbers

---

## Confidence Calibration

### Evidence Strength

| Evidence Type | Confidence Boost |
|---------------|------------------|
| Official docs (current version) | +0.3 |
| Source code confirmation | +0.2 |
| First-party benchmark | +0.15 |
| Multiple independent confirmations | +0.1 |
| Stack Overflow (high votes) | +0.05 |

### Uncertainty Penalties

| Uncertainty Type | Confidence Penalty |
|------------------|-------------------|
| No documentation found | -0.2 |
| Outdated source (>1 year) | -0.15 |
| Contradicting sources | -0.2 |
| Version mismatch | -0.15 |
| Single source only | -0.1 |

### Confidence Thresholds

| Confidence | Interpretation |
|------------|----------------|
| >= 0.9 | Verified - proceed with confidence |
| 0.7-0.9 | Likely correct - minor verification recommended |
| 0.5-0.7 | Uncertain - significant verification needed |
| < 0.5 | Unverified - do not rely on this claim |

---

## Red Flags

### Immediate Skepticism Triggers

| Trigger | Why Suspicious |
|---------|----------------|
| "Always" or "Never" | Absolutes are rarely accurate |
| No version specified | Behavior often varies by version |
| "I think" or "I believe" | Opinion, not fact |
| Outdated date (>2 years) | Technology moves fast |
| No source cited | Where does this come from? |
| Contradicts official docs | Docs are usually right |
| "Works for me" | Environment-specific |
| Copy-pasted from AI | AI hallucinates confidently |

### Verification-Resistant Claims

Some claims are hard to verify but important to flag:

- Scalability projections
- "Enterprise-ready" assertions
- Security guarantees
- Future compatibility promises
- "Industry standard" claims
