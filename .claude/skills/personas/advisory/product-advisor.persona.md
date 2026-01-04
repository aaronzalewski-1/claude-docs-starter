---
name: product-advisor-knowledge
description: Domain expertise for Product Advisor persona - product strategy, PMF signals, feature prioritization, roadmap planning
type: persona_skill
persona: personas/advisory/product-advisor
version: 1.0.0
---

# Product Advisor Domain Knowledge

> Product-market fit assessment, feature prioritization frameworks, competitive product strategy, and roadmap planning for business decisions.

---

## Product-Market Fit

### PMF Signals

| Signal | Strength | Measurement |
|--------|----------|-------------|
| **Retention** | Very Strong | D30, D90 retention rates |
| **Organic Growth** | Very Strong | % customers from referrals |
| **Net Promoter Score** | Strong | NPS > 50 |
| **"Very Disappointed"** | Strong | > 40% on Sean Ellis test |
| **Revenue Growth** | Strong | MoM revenue increase |
| **Usage Frequency** | Medium | DAU/MAU ratio |
| **Feature Requests** | Medium | Requests for more vs. different |

### Sean Ellis PMF Test

Survey: "How would you feel if you could no longer use [product]?"

| Response | % of Users | PMF Signal |
|----------|------------|------------|
| Very disappointed | > 40% | **Strong PMF** |
| Very disappointed | 25-40% | **Emerging PMF** |
| Very disappointed | < 25% | **No PMF** |

### PMF Stage Assessment

| Stage | Characteristics | Next Step |
|-------|-----------------|-----------|
| **No Fit** | High churn, no pull | Pivot or iterate on value prop |
| **Early Signs** | Some retention, some pull | Double down on what's working |
| **PMF Emerging** | Growing organically, requests for more | Scale cautiously |
| **PMF Achieved** | Strong retention, word-of-mouth | Scale aggressively |

### Retention Benchmarks by Product Type

| Product Type | Good D1 | Good D7 | Good D30 |
|--------------|---------|---------|----------|
| **Consumer App** | > 40% | > 20% | > 10% |
| **B2B SaaS** | > 80% | > 70% | > 60% |
| **E-commerce** | N/A | > 10% | > 5% |
| **Gaming** | > 30% | > 15% | > 5% |

---

## Feature Prioritization

### RICE Framework

| Factor | Description | Scale |
|--------|-------------|-------|
| **R**each | How many users affected? | Users per quarter |
| **I**mpact | How much impact per user? | 0.25 (minimal) to 3 (massive) |
| **C**onfidence | How sure are we? | 0% to 100% |
| **E**ffort | Person-months to build | Engineering time |

**Score = (Reach × Impact × Confidence) / Effort**

### ICE Framework

| Factor | Description | Scale |
|--------|-------------|-------|
| **I**mpact | Expected business impact | 1-10 |
| **C**onfidence | Certainty in estimates | 1-10 |
| **E**ase | Inverse of effort | 1-10 |

**Score = Impact × Confidence × Ease**

### MoSCoW Prioritization

| Category | Definition | Typical % |
|----------|------------|-----------|
| **Must Have** | Critical for release | 60% |
| **Should Have** | Important, not vital | 20% |
| **Could Have** | Nice to have | 15% |
| **Won't Have** | Future consideration | 5% |

### Kano Model Categories

| Category | User Reaction if Present | User Reaction if Absent |
|----------|--------------------------|------------------------|
| **Basic** | Neutral (expected) | Dissatisfied |
| **Performance** | Satisfied (linear) | Dissatisfied (linear) |
| **Delighters** | Highly satisfied | Neutral |
| **Indifferent** | Neutral | Neutral |
| **Reverse** | Dissatisfied | Satisfied |

---

## Roadmap Strategy

### Roadmap Types

| Type | Time Horizon | Detail Level | Best For |
|------|--------------|--------------|----------|
| **Now-Next-Later** | Flexible | Decreasing | Agile teams |
| **Theme-based** | Quarters | Feature groups | Alignment |
| **Timeline** | Fixed dates | Specific features | External commitments |
| **Outcome-based** | Flexible | Metrics focus | OKR-driven orgs |

### Roadmap Anti-patterns

| Anti-pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| **Feature Factory** | Building without outcomes | Tie features to metrics |
| **Date-driven** | Arbitrary deadlines | Outcome-driven releases |
| **Everything Important** | No prioritization | Ruthless prioritization |
| **Customer-driven** | Loudest voice wins | Aggregate and validate |
| **Competitor Copy** | Reactive, not strategic | Focus on differentiation |

### Technical Debt Management

| Debt Type | Examples | When to Address |
|-----------|----------|-----------------|
| **Prudent-Deliberate** | Shortcuts taken knowingly | Schedule payback |
| **Prudent-Inadvertent** | Learned better approach | When touching that code |
| **Reckless-Deliberate** | Cut corners to ship | ASAP - high risk |
| **Reckless-Inadvertent** | Didn't know better | During next refactor |

### Build vs Buy Decision

| Factor | Build | Buy |
|--------|-------|-----|
| **Core Competency** | Yes | No |
| **Differentiation** | Key differentiator | Commodity |
| **Control** | Need full control | Standard is fine |
| **Time** | Have time | Need it now |
| **Expertise** | Have skills | Lack expertise |
| **Maintenance** | Can sustain | Prefer vendor support |

---

## User Research

### Research Method Selection

| Method | Best For | Sample Size | Time |
|--------|----------|-------------|------|
| **User Interviews** | Deep understanding | 5-15 | 2-4 weeks |
| **Surveys** | Quantitative validation | 100+ | 1-2 weeks |
| **Usability Testing** | UX issues | 5-10 | 1-2 weeks |
| **A/B Testing** | Optimization | 1000+ | 2-4 weeks |
| **Analytics** | Behavior patterns | All users | Ongoing |
| **Session Recording** | Friction discovery | 50+ | 1 week |

### Jobs-to-be-Done Framework

| Component | Question | Example |
|-----------|----------|---------|
| **Job Performer** | Who is the user? | "A project manager..." |
| **Job** | What are they trying to do? | "...trying to keep team aligned..." |
| **Context** | When/where? | "...during sprint planning..." |
| **Outcome** | What's the desired result? | "...so everyone knows priorities." |

### Feature Validation Process

| Stage | Method | Pass Criteria |
|-------|--------|---------------|
| **Problem Validation** | Interviews | 8/10 users have problem |
| **Solution Validation** | Prototypes | Users understand and want it |
| **Demand Validation** | Landing page | Conversion > X% |
| **Usage Validation** | MVP/Beta | Retention metrics |

---

## Competitive Strategy

### Competitive Response Options

| Response | When to Use | Risk |
|----------|-------------|------|
| **Ignore** | Not relevant to your segment | Miss real threat |
| **Monitor** | Early/unclear threat | May be too late |
| **Fast Follow** | Feature is table stakes | Me-too perception |
| **Differentiate** | Can't win on same dimension | May not resonate |
| **Leapfrog** | Have superior approach | Execution risk |

### Feature Parity Assessment

| Category | Your Position | Strategic Implication |
|----------|---------------|----------------------|
| **Ahead** | Unique capability | Protect and extend |
| **Parity** | Same as competitors | Compete on other dimensions |
| **Behind** | Missing table stakes | Must address |
| **Different** | Alternative approach | May be strength or weakness |

### Platform Strategy

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Point Solution** | Best at one thing | Early stage, niche |
| **Suite** | Multiple integrated products | Mature, broader market |
| **Platform** | Enable third parties | Network effects opportunity |
| **Ecosystem** | Create value network | Market leader position |

---

## MVP Definition

### MVP Types

| Type | Purpose | Scope |
|------|---------|-------|
| **Concierge** | Manual validation | Zero code |
| **Wizard of Oz** | Fake automation | UI only, manual backend |
| **Piecemeal** | Combine existing tools | Integration heavy |
| **Landing Page** | Demand validation | Marketing only |
| **Single Feature** | Core value validation | One key feature |
| **Functional** | Full loop, minimal | End-to-end, basic |

### MVP Scope Checklist

| Question | Cut If... |
|----------|-----------|
| **Does it validate our core hypothesis?** | No - must have |
| **Would users pay without it?** | Yes - cut it |
| **Is it needed for core job-to-be-done?** | No - cut it |
| **Is it a "nice to have"?** | Yes - cut it |
| **Can we fake it manually first?** | Yes - don't build it |

### Feature Creep Warning Signs

| Warning Sign | Indication |
|--------------|------------|
| "While we're at it..." | Scope expanding |
| Edge case handling | Over-engineering |
| Admin features before users | Wrong priority |
| "Competitors have it" | Reactive building |
| No one asked for it | Building in vacuum |

---

## Stage-Specific Product Focus

| Stage | Product Priority | Key Question |
|-------|------------------|--------------|
| **Pre-seed** | Problem validation | "Is this a real problem worth solving?" |
| **Seed** | MVP and PMF | "Can we build something people want?" |
| **Series A** | Feature depth | "What features drive retention?" |
| **Series B+** | Platform/expansion | "How do we expand the value proposition?" |
| **Exit** | Product differentiation | "What's defensible about our product?" |

---

## Confidence Calibration

### Product Confidence Boosters

| Indicator | Confidence Boost |
|-----------|------------------|
| User research supports decision | +0.15 |
| Usage data validates need | +0.20 |
| PMF signals strong | +0.15 |
| Clear prioritization rationale | +0.10 |
| Team has shipped similar before | +0.10 |

### Product Confidence Penalties

| Concern | Confidence Penalty |
|---------|-------------------|
| No user validation | -0.20 |
| Feature request from single customer | -0.10 |
| "Competitors have it" as only rationale | -0.15 |
| Scope poorly defined | -0.10 |
| Technical feasibility uncertain | -0.15 |
