---
name: operations-knowledge
description: Domain expertise for Operations persona - team scaling, process maturity, organizational design, execution capacity
type: persona_skill
persona: personas/advisory/operations
version: 1.0.0
---

# Operations Domain Knowledge

> Organizational scaling frameworks, process maturity models, team capacity planning, and execution assessment for business decisions.

---

## Organizational Scaling

### Startup Stage Characteristics

| Stage | Team Size | Structure | Leadership |
|-------|-----------|-----------|------------|
| **Founding** | 1-5 | Flat, informal | Founders do everything |
| **Early** | 5-20 | Functional clusters | First managers emerge |
| **Growth** | 20-100 | Functional departments | Leadership team forms |
| **Scale** | 100-500 | Divisions/business units | Executive layer |
| **Enterprise** | 500+ | Matrix/complex | Professional management |

### Team Scaling Transitions

| Transition | Typical Pain Points | Required Changes |
|------------|---------------------|------------------|
| **5 → 20** | Communication overhead | Weekly all-hands, written docs |
| **20 → 50** | Manager gaps | Hire/promote first-line managers |
| **50 → 100** | Culture dilution | Explicit values, onboarding |
| **100 → 250** | Coordination costs | Middle management, processes |
| **250+** | Speed vs control | Decentralization, clear ownership |

### Key Role Emergence Timeline

| Role | Typical Stage | Trigger |
|------|---------------|---------|
| **First Engineer Hire** | Pre-seed/Seed | Can't build it all yourself |
| **First Customer Success** | Post-revenue | Customer complaints |
| **First Sales Rep** | Series A | Founder can't do all sales |
| **Head of Engineering** | Post-10 engineers | Coordination needs |
| **VP Sales** | Post-5 sales reps | Sales process scaling |
| **CFO** | Series B+ | Financial complexity |
| **COO** | Series B+ | Operational complexity |
| **CHRO** | 100+ employees | People complexity |

---

## Process Maturity

### Process Maturity Model

| Level | Characteristics | Indicators |
|-------|-----------------|------------|
| **1: Initial** | Ad hoc, reactive | Tribal knowledge, heroics |
| **2: Repeatable** | Basic processes exist | Checklists, some docs |
| **3: Defined** | Standardized, documented | Playbooks, training |
| **4: Measured** | Quantitative management | Metrics, dashboards |
| **5: Optimizing** | Continuous improvement | A/B testing, iteration |

### Process Assessment by Function

| Function | Level 1 (Ad hoc) | Level 3 (Defined) | Level 5 (Optimizing) |
|----------|------------------|-------------------|---------------------|
| **Sales** | Founder sells | Sales playbook | Revenue operations |
| **Engineering** | Ship when ready | Sprint planning | DevOps, CI/CD |
| **Customer Success** | Reactive support | Onboarding process | Health scoring |
| **Finance** | Spreadsheets | Monthly close | Real-time analytics |
| **HR** | Informal hiring | Structured interviews | Talent analytics |

### When to Formalize Processes

| Indicator | Threshold | Process Needed |
|-----------|-----------|----------------|
| **Repetition** | Done > 3 times | Document it |
| **Handoffs** | Multiple people involved | Define ownership |
| **Errors** | Mistakes recurring | Create checklist |
| **Training** | New hire needs it | Write playbook |
| **Scale** | Will do 10x more | Automate it |

---

## Capacity Planning

### Engineering Capacity

| Metric | Calculation | Benchmark |
|--------|-------------|-----------|
| **Velocity** | Story points per sprint | Team-specific baseline |
| **Deployment Frequency** | Deploys per week | Daily+ for mature teams |
| **Lead Time** | Commit to production | Hours to days |
| **Bug Rate** | Bugs per feature | Decreasing trend |

### Sales Capacity

| Metric | Calculation | Benchmark |
|--------|-------------|-----------|
| **Quota per Rep** | Revenue / headcount | 4-5x OTE |
| **Ramp Time** | Months to full productivity | 3-6 months |
| **Pipeline Coverage** | Pipeline / quota | 3-4x |
| **Activities** | Calls/emails per day | 50-100 activities |

### Support Capacity

| Metric | Calculation | Target |
|--------|-------------|--------|
| **Tickets per Agent** | Tickets / agents | 50-100/month |
| **Response Time** | Time to first response | < 1 hour |
| **Resolution Time** | Time to close | < 24 hours |
| **CSAT** | Customer satisfaction | > 90% |

### Capacity Planning Formula

```
Required Headcount = (Volume × Time per Task) / Available Hours × Productivity Factor
```

| Factor | Typical Value |
|--------|---------------|
| **Productivity Factor** | 70-80% (meetings, admin) |
| **Ramp Factor** | 50% for first 3 months |
| **Buffer** | 10-20% for variability |

---

## Hiring and Talent

### Hire vs Promote Decision

| Factor | Hire Externally | Promote Internally |
|--------|-----------------|-------------------|
| **Skill Gap** | Major new capability | Incremental growth |
| **Timeline** | Urgent need | Can develop over time |
| **Culture** | Need fresh perspective | Culture critical |
| **Cost** | Budget available | Cost conscious |
| **Retention** | Low internal expectations | High internal expectations |

### Hiring Velocity Considerations

| Growth Rate | Hiring Implication | Risk |
|-------------|-------------------|------|
| **> 3x annual** | Rapid hiring, cultural risk | Culture dilution |
| **2-3x annual** | Aggressive but manageable | Execution pressure |
| **1.5-2x annual** | Sustainable growth | May miss opportunities |
| **< 1.5x annual** | Conservative | Under-investment risk |

### Contractor vs Full-time

| Factor | Contractor | Full-time |
|--------|------------|-----------|
| **Duration** | < 6 months | > 6 months |
| **Expertise** | Specialized, temporary | Core competency |
| **Cost** | Higher hourly, lower total | Lower hourly, higher total |
| **Control** | Less direct | Full control |
| **IP** | Careful on ownership | Clear ownership |

---

## Risk and Dependency Management

### Operational Risk Categories

| Category | Examples | Mitigation |
|----------|----------|------------|
| **Key Person** | Critical knowledge in one person | Documentation, cross-training |
| **Vendor** | Single point of failure | Backup vendors, SLAs |
| **Technical** | System failures | Redundancy, monitoring |
| **Process** | Manual error-prone steps | Automation, checks |
| **Compliance** | Regulatory requirements | Policies, audits |

### Bus Factor Analysis

| Bus Factor | Risk Level | Action |
|------------|------------|--------|
| **1** | Critical | Immediate documentation, cross-training |
| **2** | High | Document and expand knowledge |
| **3** | Moderate | Monitor, gradual expansion |
| **4+** | Low | Maintain, periodic review |

### Vendor Dependency Assessment

| Factor | Low Risk | High Risk |
|--------|----------|-----------|
| **Alternatives** | Many options | No alternatives |
| **Switching Cost** | Low | High |
| **Contract Terms** | Favorable | Vendor-favored |
| **Revenue %** | < 10% from vendor | > 30% from vendor |
| **Integration Depth** | API, loosely coupled | Deep integration |

---

## Execution Assessment

### Execution Health Indicators

| Indicator | Healthy | Unhealthy |
|-----------|---------|-----------|
| **Deadline Accuracy** | > 80% on time | < 50% on time |
| **Scope Creep** | Minimal | Constant expansion |
| **Burnout Signals** | Sustainable pace | Regular overtime |
| **Communication** | Clear, proactive | Surprises, confusion |
| **Quality** | Consistent | Variable |

### Project Risk Assessment

| Risk Factor | Questions |
|-------------|-----------|
| **Scope** | Is it well-defined? Stable? |
| **Resources** | Right skills? Availability? |
| **Timeline** | Realistic? Buffer included? |
| **Dependencies** | External dependencies? Blockers? |
| **Technical** | Unknown technology? Complexity? |

### Execution Readiness Checklist

| Dimension | Ready | Not Ready |
|-----------|-------|-----------|
| **Clear Goals** | SMART objectives defined | Vague direction |
| **Ownership** | DRI assigned | Committee ownership |
| **Resources** | Committed, available | Competing priorities |
| **Timeline** | Realistic, buffered | Aspirational |
| **Dependencies** | Mapped, managed | Unknown blockers |
| **Metrics** | Success criteria defined | "We'll know it when we see it" |

---

## Operational Due Diligence

### Exit Readiness Checklist

| Area | Ready | Issues |
|------|-------|--------|
| **Documentation** | Processes documented | Tribal knowledge |
| **Contracts** | Organized, accessible | Missing, scattered |
| **Team** | Retention agreements | Key person risk |
| **Systems** | Modern, documented | Legacy, undocumented |
| **Compliance** | Audit trail | Gaps in records |

### Integration Considerations

| Factor | Easier Integration | Harder Integration |
|--------|-------------------|-------------------|
| **Systems** | Standard, cloud-based | Custom, on-premise |
| **Processes** | Documented | Tribal knowledge |
| **Culture** | Aligned | Conflicting values |
| **Location** | Centralized | Distributed |
| **Contracts** | Transferable | Change of control issues |

---

## Stage-Specific Operations Focus

| Stage | Operations Priority | Key Question |
|-------|---------------------|--------------|
| **Pre-seed** | Founder bandwidth | "What can founders realistically do?" |
| **Seed** | First hires | "Who are the critical first hires?" |
| **Series A** | Process creation | "What processes are breaking?" |
| **Series B+** | Organizational scaling | "How do we scale without breaking?" |
| **Exit** | DD readiness | "Are we ready for scrutiny?" |

---

## Confidence Calibration

### Operations Confidence Boosters

| Indicator | Confidence Boost |
|-----------|------------------|
| Documented processes exist | +0.10 |
| Team has done this before | +0.15 |
| Clear ownership defined | +0.10 |
| Realistic timeline with buffer | +0.10 |
| Low key-person risk | +0.10 |

### Operations Confidence Penalties

| Concern | Confidence Penalty |
|---------|-------------------|
| Major capability gap | -0.15 |
| Significant hiring required | -0.15 |
| Key person dependency | -0.10 |
| No process documentation | -0.10 |
| Unrealistic timeline | -0.15 |
