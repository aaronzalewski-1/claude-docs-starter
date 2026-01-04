---
name: pragmatist-knowledge
description: Domain expertise for Pragmatist persona - MVP criteria, complexity justification, deferral decision frameworks
type: persona_skill
persona: personas/product/pragmatist
version: 1.0.0
---

# Pragmatist Domain Knowledge

> MVP criteria, complexity justification, and deferral frameworks for shipping-focused decisions.

---

## MVP Criteria Matrix

### Must-Have vs Nice-to-Have

| Category | Must-Have If | Nice-to-Have If |
|----------|--------------|-----------------|
| **Security** | Data breach = company-ending | Defense in depth |
| **Compliance** | Legal requirement | Best practice |
| **Core Function** | Without it, product doesn't work | Enhances experience |
| **Performance** | Users will abandon | Users will complain |
| **Reliability** | Failure = data loss | Failure = inconvenience |

### Feature Prioritization Framework

```
Priority = Impact × Confidence / Effort

Impact: How much value does this deliver? (1-10)
Confidence: How sure are we it's needed? (1-10)
Effort: How much work is it? (1-10)
```

| Priority Score | Category | Action |
|----------------|----------|--------|
| > 7 | High value, high confidence | Build first |
| 4-7 | Moderate | Build if time permits |
| < 4 | Low priority | Defer or cut |

### The "What Would We Cut?" Test

Ask: "If we only had one week, what would we absolutely NOT build?"

| If Answer Is | Then It's |
|--------------|-----------|
| "We'd still build it" | Must-have |
| "We'd do it differently" | Simplify it |
| "We'd skip it" | Nice-to-have |
| "What is that?" | Cut it now |

---

## Complexity Justification Framework

### When Complexity IS Justified

| Justification | Evidence Required |
|---------------|-------------------|
| **User demand** | Real users have asked for this |
| **Core differentiator** | This is why customers choose us |
| **Regulatory requirement** | Legal or compliance mandate |
| **Security necessity** | Prevents critical vulnerability |
| **Proven bottleneck** | Measured performance problem |

### When Complexity is NOT Justified

| Anti-Justification | Why It's Wrong |
|--------------------|----------------|
| "We might need it someday" | YAGNI - You Aren't Gonna Need It |
| "Best practices say..." | Best practice for whom? At what scale? |
| "Other companies do it" | They have different constraints |
| "It's more elegant" | Elegance ≠ Value |
| "It's only a little more work" | Compound interest on complexity |

### Complexity Audit Checklist

For each proposed complexity, answer:

- [ ] Who specifically asked for this?
- [ ] What happens if we don't do it?
- [ ] What's the simplest thing that could work?
- [ ] Can we defer this until we have more data?
- [ ] What's the maintenance burden?

---

## Deferral Decision Tree

```
Should we build this now?
│
├─ Is it required for basic functionality?
│  ├─ Yes → Build it
│  └─ No ↓
│
├─ Do we have validated user demand?
│  ├─ Yes → Consider building
│  └─ No ↓
│
├─ Can we fake it manually first?
│  ├─ Yes → Fake it, measure demand, then decide
│  └─ No ↓
│
├─ Is the decision reversible?
│  ├─ Yes → Defer until we have data
│  └─ No → Analyze more carefully
```

### Deferral Categories

| Category | Defer Until | Examples |
|----------|-------------|----------|
| **Performance optimization** | Measured bottleneck | Caching, denormalization |
| **Scale features** | 10x current load | Sharding, horizontal scaling |
| **Edge case handling** | It actually happens | Rare error conditions |
| **Advanced features** | Core is validated | Power user features |
| **Perfect UX** | Users complain | Polish, animations |

### The "Last Responsible Moment"

**Definition**: The point at which NOT deciding becomes more costly than deciding.

| Decision Type | Last Responsible Moment |
|---------------|------------------------|
| Database schema | When data format is stable |
| API contracts | When external consumers exist |
| Architecture patterns | When team needs consistency |
| Technology choice | When integration begins |

---

## Reversibility Assessment

### Reversibility Levels

| Level | Description | Examples |
|-------|-------------|----------|
| **Easy** | Undo in hours, no data loss | Config change, feature flag |
| **Moderate** | Undo in days, some rework | API change (internal only) |
| **Hard** | Undo in weeks, significant rework | Database schema, external API |
| **Impossible** | Cannot meaningfully undo | Public API, data deletion |

### Risk-Based Decision Rules

| Reversibility | Confidence Needed | Decision Speed |
|---------------|-------------------|----------------|
| Easy | Low (>30%) | Decide fast |
| Moderate | Medium (>50%) | Decide with review |
| Hard | High (>75%) | Decide carefully |
| Impossible | Very high (>90%) | Decide with stakeholders |

### Reversibility Patterns

| Pattern | How It Adds Reversibility |
|---------|---------------------------|
| Feature flags | Turn off without deploy |
| Database migrations (both ways) | Roll back schema changes |
| API versioning | Keep old behavior available |
| A/B testing | Validate before full rollout |
| Soft deletes | Recover deleted data |

---

## Simplification Strategies

### Strategy 1: Remove Features

| Question | If Yes |
|----------|--------|
| Does anyone use this? | Keep (measure first) |
| Would anyone miss it? | Remove |
| Can users work around it? | Remove |

### Strategy 2: Reduce Scope

| Full Version | 80% Version | 50% Version |
|--------------|-------------|-------------|
| CRUD with audit trail | CRUD with soft delete | CRUD only |
| Real-time updates | Polling every 30s | Manual refresh |
| Multi-tenant | Single tenant | Hardcoded tenant |

### Strategy 3: Replace with Manual Process

| Automated | Manual Replacement |
|-----------|-------------------|
| Email notifications | Slack message from developer |
| Report generation | SQL query → Excel |
| User provisioning | Admin creates account |
| Payment processing | Invoice manually |

### Strategy 4: Use Existing Solutions

| Build | Buy/Use |
|-------|---------|
| Custom auth | Auth0, Firebase Auth, Cognito |
| Search | Elasticsearch, Algolia |
| File storage | S3, Cloud Storage |
| Email sending | SendGrid, SES, Mailgun |

---

## The Pragmatist's Questions

### Before Starting

1. **"What if we just... didn't?"** - What happens if we skip this entirely?
2. **"What would we build with one week?"** - Forces prioritization
3. **"How would we know it's working?"** - Defines success criteria
4. **"What's the manual workaround?"** - Reveals if automation is premature

### During Development

1. **"Is this solving a problem we have?"** - Not a problem we might have
2. **"Who is this for?"** - Specific user or imaginary one?
3. **"What's the simplest test?"** - Happy path first
4. **"Can we ship this today?"** - Incremental value

### Before Adding Complexity

1. **"What evidence supports this need?"** - Data, not opinion
2. **"What's the cost of being wrong?"** - Reversibility assessment
3. **"What else could this time buy?"** - Opportunity cost
4. **"Will this matter in 6 months?"** - Time perspective

---

## Confidence Scoring

### Complexity Justified

| Evidence | Confidence Modifier |
|----------|---------------------|
| Real user request | +0.2 |
| Measured problem | +0.15 |
| Regulatory requirement | +0.15 |
| Core differentiator | +0.1 |
| Performance bottleneck (proven) | +0.1 |

### Complexity Unjustified

| Evidence | Confidence Modifier |
|----------|---------------------|
| "We might need it" | -0.2 |
| "Best practice" (without context) | -0.15 |
| "Other companies do it" | -0.1 |
| No stated user need | -0.15 |
| Optimization without measurement | -0.2 |
