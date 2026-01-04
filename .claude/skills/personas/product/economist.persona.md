---
name: economist-knowledge
description: Domain expertise for Economist persona - cost calculation models, ROI frameworks, TCO analysis
type: persona_skill
persona: personas/product/economist
version: 1.0.0
---

# Economist Domain Knowledge

> Cost calculation models, ROI frameworks, and economic analysis for technical decisions.

---

## Cost Categories

### Direct Costs (Visible)

| Category | Components | How to Estimate |
|----------|------------|-----------------|
| **Cloud Services** | Compute, storage, networking, managed services | Cloud provider pricing calculator |
| **Licenses** | Per-seat, per-instance, enterprise agreements | Vendor pricing pages |
| **Third-party APIs** | Per-call, per-token, monthly minimums | API documentation |
| **Infrastructure** | Servers, certificates, domains | Provider pricing |

### Development Costs

| Category | Components | How to Estimate |
|----------|------------|-----------------|
| **Implementation** | Initial coding, testing, deployment | Story points → hours × rate |
| **Learning Curve** | Training, documentation reading, experimentation | Industry averages by complexity |
| **Integration** | Connecting to existing systems | Based on API complexity |
| **Migration** | Data migration, cutover, parallel running | Data volume × complexity |

### Operational Costs (Often Hidden)

| Category | Components | How to Estimate |
|----------|------------|-----------------|
| **Monitoring** | Alerting setup, dashboard maintenance | Hours/week × rate |
| **Incident Response** | On-call, investigation, remediation | Historical incident frequency |
| **Scaling Management** | Capacity planning, auto-scaling tuning | % of ops time |
| **Security Updates** | Patching, vulnerability response | Vendor SLA × internal process |

### Maintenance Costs (The Iceberg)

| Category | Components | How to Estimate |
|----------|------------|-----------------|
| **Dependency Updates** | Library updates, breaking changes | Quarterly audit hours |
| **Framework Upgrades** | Major version migrations | Industry migration guides |
| **Knowledge Transfer** | Onboarding, documentation | Per new team member |
| **Technical Debt** | Deferred refactoring, workarounds | Debt ratio × velocity impact |

---

## Cost Estimation Models

### Developer Time

**Baseline Rate**: $100-150/hour (fully loaded senior developer)

| Task Type | Typical Range | Multiplier for Unfamiliarity |
|-----------|---------------|------------------------------|
| CRUD feature | 4-8 hours | 1.5x |
| Integration | 8-24 hours | 2x |
| Complex business logic | 16-40 hours | 1.5x |
| Performance optimization | 8-40 hours | 2x |
| Security hardening | 8-24 hours | 1.5x |

### Estimation Accuracy

| Estimate Type | Accuracy Range | When to Use |
|---------------|----------------|-------------|
| Rough order of magnitude | ±50-100% | Early exploration |
| Budget estimate | ±25-50% | Planning phase |
| Detailed estimate | ±10-25% | Commitment phase |
| Actuals tracking | ±5-10% | Execution phase |

### Risk Multipliers

| Risk Factor | Multiplier | When to Apply |
|-------------|------------|---------------|
| New technology | 1.5x | First project with tech |
| Complex integration | 1.3x | Multiple external systems |
| Unclear requirements | 1.5x | Scope likely to change |
| Team unfamiliarity | 1.3x | New domain or stack |
| Tight deadline | 1.2x | Compressed timeline |

---

## ROI Framework

### ROI Calculation

```
ROI = (Net Benefit / Total Cost) × 100

Net Benefit = Gross Benefit - Ongoing Costs
Total Cost = Development + Migration + First Year Operations
```

### Payback Period

```
Payback Period = Total Investment / Annual Net Benefit

Investment = Development + Migration + Setup
Annual Net Benefit = Yearly Savings - Yearly Costs
```

### Break-Even Analysis

| Metric | Good | Acceptable | Concerning |
|--------|------|------------|------------|
| Payback Period | < 6 months | 6-12 months | > 12 months |
| ROI (Year 1) | > 200% | 100-200% | < 100% |
| ROI (Year 3) | > 500% | 200-500% | < 200% |

### Benefit Categories

| Category | How to Quantify |
|----------|-----------------|
| **Time Savings** | Hours saved × hourly rate |
| **Error Reduction** | Incident cost × reduction % |
| **Faster Time-to-Market** | Revenue per week × weeks saved |
| **Scalability** | Avoided infrastructure cost |
| **Developer Productivity** | Velocity increase × team cost |

---

## TCO (Total Cost of Ownership) Template

### Year 1

| Category | Amount | Notes |
|----------|--------|-------|
| Development | $ | Implementation + testing |
| Migration | $ | Data, cutover, parallel run |
| Infrastructure (setup) | $ | Initial provisioning |
| Training | $ | Team learning curve |
| **Subtotal: Upfront** | $ | |
| Cloud services (monthly × 12) | $ | |
| Operations (hours × rate × 12) | $ | |
| Maintenance (hours × rate × 12) | $ | |
| **Subtotal: Ongoing** | $ | |
| **Year 1 Total** | $ | |

### Year 2-3 (Ongoing)

| Category | Year 2 | Year 3 |
|----------|--------|--------|
| Cloud services | $ | $ |
| Operations | $ | $ |
| Maintenance | $ | $ |
| Major upgrades | $ | $ |
| **Annual Total** | $ | $ |

### 3-Year TCO

| Component | Amount | % of Total |
|-----------|--------|------------|
| Year 1 | $ | |
| Year 2 | $ | |
| Year 3 | $ | |
| **Total TCO** | $ | 100% |

---

## Scale Economics

### Linear Scaling

```
Cost = Base + (Unit Cost × Volume)
```

| Service Type | Typical Behavior |
|--------------|------------------|
| Storage | Linear (per GB) |
| API calls (simple) | Linear (per call) |
| User licenses | Linear (per seat) |

### Sub-Linear Scaling (Economies of Scale)

```
Cost = Base + (Unit Cost × Volume^0.7)
```

| Service Type | Typical Behavior |
|--------------|------------------|
| Reserved instances | Volume discounts |
| Enterprise agreements | Tier pricing |
| CDN bandwidth | Committed use discounts |

### Super-Linear Scaling (Dis-economies)

```
Cost = Base + (Unit Cost × Volume^1.3)
```

| Service Type | Typical Behavior |
|--------------|------------------|
| Memory-intensive compute | Memory scales faster than compute |
| High-availability | Redundancy multiplies cost |
| Compliance/security | More data = more risk surface |

### Scale Projection Template

| Scale | Current | 2x | 10x | 100x |
|-------|---------|-----|-----|------|
| Compute | $ | $ | $ | $ |
| Storage | $ | $ | $ | $ |
| Network | $ | $ | $ | $ |
| API calls | $ | $ | $ | $ |
| **Total Monthly** | $ | $ | $ | $ |

---

## Opportunity Cost Framework

### Definition

**Opportunity Cost** = Value of the next best alternative foregone

### Calculation

```
Opportunity Cost = Best Alternative Value - Chosen Option Value

Where:
- Alternative Value = What else could this time/money enable?
- Chosen Option Value = Expected return from this investment
```

### Common Alternatives

| Investment | Alternative Uses |
|------------|------------------|
| 40 dev hours | Bug fixes, tech debt, other feature |
| $10k/month cloud spend | Different architecture, more developers |
| 3-month project | Faster MVP, market validation |

### Decision Matrix

| Factor | Option A | Option B | Winner |
|--------|----------|----------|--------|
| Direct cost | $ | $ | |
| Opportunity cost | $ | $ | |
| Risk-adjusted value | $ | $ | |
| Time to value | weeks | weeks | |
| **Total Score** | | | |

---

## Build vs Buy Framework

### Build Favors When

| Factor | Threshold |
|--------|-----------|
| Core differentiator | This IS your product |
| Unique requirements | No solution fits >70% |
| Long-term investment | >3 year horizon |
| Team capability | Strong in this domain |
| Control needed | Compliance, security, customization |

### Buy Favors When

| Factor | Threshold |
|--------|-----------|
| Commodity capability | Standard problem, solved |
| Time-to-market critical | Need it yesterday |
| Maintenance burden | Don't want to own it |
| Domain expertise lacking | Learning curve too steep |
| Cost comparison | Buy < Build at 3 years |

### Build vs Buy Calculator

```
Build Cost (3 Year) =
  Development +
  Maintenance (Year 1-3) +
  Infrastructure (Year 1-3) +
  Opportunity Cost

Buy Cost (3 Year) =
  License/Subscription (Year 1-3) +
  Integration +
  Customization +
  Training +
  Vendor Lock-in Risk Premium
```

---

## Confidence Scoring

### Cost Certainty

| Evidence | Confidence Modifier |
|----------|---------------------|
| Documented pricing | +0.2 |
| Similar project actuals | +0.15 |
| Vendor quote | +0.1 |
| Industry benchmarks | +0.05 |

### Cost Uncertainty

| Factor | Confidence Modifier |
|--------|---------------------|
| New technology (no precedent) | -0.2 |
| Variable pricing model | -0.15 |
| Unclear requirements | -0.15 |
| Multi-vendor solution | -0.1 |
