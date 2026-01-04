---
name: cfo-knowledge
description: Domain expertise for CFO persona - financial analysis, runway management, unit economics, fundraising metrics
type: persona_skill
persona: personas/advisory/cfo
version: 1.0.0
---

# CFO Domain Knowledge

> Financial frameworks, runway analysis, unit economics, and fundraising metrics for startup financial decision-making.

---

## Runway Analysis

### Burn Rate Calculation

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Gross Burn** | Total monthly expenses | Cash going out the door |
| **Net Burn** | Gross Burn - Revenue | Actual cash consumption |
| **Runway (months)** | Cash Balance / Net Burn | Months until cash-out |

### Runway Thresholds

| Runway | Risk Level | Action Required |
|--------|------------|-----------------|
| > 18 months | **Low** | Focus on growth, can take risks |
| 12-18 months | **Moderate** | Start fundraising conversations |
| 6-12 months | **Elevated** | Active fundraising required |
| 3-6 months | **High** | Emergency cost cuts or bridge round |
| < 3 months | **Critical** | Survival mode, all options on table |

### Default Alive Calculation

**Default Alive**: Will you reach profitability before running out of money at current growth rate?

```
Monthly Revenue Growth Rate = (Current Revenue / Revenue 6 months ago)^(1/6) - 1
Months to Profitability = ln(Gross Burn / Current Revenue) / ln(1 + Growth Rate)
```

| Status | Interpretation |
|--------|----------------|
| **Default Alive** | Months to profitability < Runway |
| **Default Dead** | Months to profitability > Runway |

---

## Unit Economics

### Customer Acquisition Cost (CAC)

| Formula | Components |
|---------|------------|
| **Simple CAC** | (Sales + Marketing Spend) / New Customers |
| **Fully Loaded CAC** | (S&M Spend + Salaries + Tools + Overhead) / New Customers |
| **Blended CAC** | Total S&M / (New + Expansion Customers) |

### Customer Lifetime Value (LTV)

| Model | Formula | Use When |
|-------|---------|----------|
| **Simple** | ARPU × Average Lifespan | Early stage, limited data |
| **Churn-based** | ARPU / Monthly Churn Rate | Subscription with stable churn |
| **Margin-adjusted** | (ARPU × Gross Margin) / Churn | Mature with variable costs |
| **Cohort-based** | Sum of actual cohort revenue | Best accuracy, requires data |

### LTV:CAC Ratio

| Ratio | Interpretation | Action |
|-------|----------------|--------|
| < 1:1 | **Losing money** on each customer | Fix unit economics before scaling |
| 1:1 - 2:1 | **Unsustainable** growth | Improve retention or reduce CAC |
| 3:1 | **Healthy** benchmark | Standard target for SaaS |
| > 5:1 | **Under-investing** in growth | Increase marketing spend |

### CAC Payback Period

| Formula | Interpretation |
|---------|----------------|
| CAC / (ARPU × Gross Margin) | Months to recover acquisition cost |

| Payback | Assessment |
|---------|------------|
| < 6 months | Excellent - fast capital recycling |
| 6-12 months | Good - typical for SMB SaaS |
| 12-18 months | Acceptable - typical for enterprise |
| > 18 months | Concerning - capital intensive |
| > 24 months | Problematic - requires cheap capital |

---

## Revenue Metrics

### Monthly Recurring Revenue (MRR)

| Component | Definition |
|-----------|------------|
| **New MRR** | Revenue from new customers |
| **Expansion MRR** | Upgrades and cross-sells |
| **Contraction MRR** | Downgrades (negative) |
| **Churned MRR** | Lost customers (negative) |
| **Net New MRR** | New + Expansion - Contraction - Churned |

### Net Revenue Retention (NRR)

| Formula | Target |
|---------|--------|
| (Starting MRR + Expansion - Contraction - Churn) / Starting MRR | > 100% |

| NRR | Assessment |
|-----|------------|
| > 130% | Exceptional - strong expansion |
| 110-130% | Excellent - healthy growth |
| 100-110% | Good - expansion covers churn |
| 90-100% | Concerning - net contraction |
| < 90% | Critical - significant churn |

### Gross Margin

| Type | Formula | Target |
|------|---------|--------|
| **Software** | (Revenue - COGS) / Revenue | > 70% |
| **Services** | (Revenue - Delivery Cost) / Revenue | > 50% |
| **Blended** | Weighted by revenue mix | Depends on mix |

---

## Fundraising Metrics

### Valuation Methods

| Method | Formula | Best For |
|--------|---------|----------|
| **Revenue Multiple** | ARR × Multiple | SaaS, growth stage |
| **Growth-Adjusted** | ARR × (Growth Rate / 100) | High-growth companies |
| **Comparable Transactions** | Based on similar exits | Late stage, pre-exit |
| **DCF** | Present value of future cash flows | Profitable companies |

### Typical Revenue Multiples by Stage

| Stage | ARR Range | Multiple Range |
|-------|-----------|----------------|
| Pre-seed | < $100K | N/A (potential-based) |
| Seed | $100K - $1M | 10-30x |
| Series A | $1M - $5M | 10-20x |
| Series B | $5M - $15M | 8-15x |
| Series C+ | > $15M | 5-12x |

### Dilution Framework

| Round | Typical Dilution | Founder Ownership After |
|-------|------------------|------------------------|
| Pre-seed | 5-10% | 90-95% |
| Seed | 15-25% | 70-80% |
| Series A | 15-25% | 55-65% |
| Series B | 15-20% | 45-55% |
| Series C | 10-15% | 40-50% |
| Exit | - | 25-40% (typical) |

### Raise Amount Guidelines

| Guideline | Formula |
|-----------|---------|
| **Runway Target** | Raise = 18-24 months of projected burn |
| **Milestone-Based** | Raise enough to hit next funding milestone |
| **Dilution-Based** | Raise ≈ 20-25% of post-money valuation |

---

## Cost Structure Analysis

### Fixed vs Variable Costs

| Type | Examples | Scaling Behavior |
|------|----------|------------------|
| **Fixed** | Salaries, rent, software licenses | Doesn't change with revenue |
| **Variable** | COGS, payment processing, cloud costs | Scales with revenue |
| **Semi-variable** | Support staff, infrastructure | Step-function scaling |

### Cost Categories

| Category | Components | Target % of Revenue |
|----------|------------|---------------------|
| **COGS** | Hosting, support, implementation | 20-30% |
| **R&D** | Engineering, product, design | 20-30% |
| **S&M** | Sales, marketing, partnerships | 30-50% |
| **G&A** | Finance, legal, HR, admin | 10-20% |

### Operating Leverage

| Indicator | Formula | Interpretation |
|-----------|---------|----------------|
| **Contribution Margin** | Revenue - Variable Costs | Available to cover fixed costs |
| **Operating Leverage** | % Change in EBIT / % Change in Revenue | Higher = more leverage |

---

## Financial Controls

### Cash Management

| Control | Purpose | Threshold |
|---------|---------|-----------|
| **Cash Reserve** | Emergency buffer | 3 months expenses |
| **AP Aging** | Vendor payment timing | < 30 days for strategic vendors |
| **AR Aging** | Customer collection | > 90 days = bad debt risk |
| **Bank Covenant** | Lender requirements | Monitor continuously |

### Budget Variance Analysis

| Variance | Interpretation | Action |
|----------|----------------|--------|
| < 5% | On track | Continue monitoring |
| 5-15% | Notable | Investigate root cause |
| > 15% | Significant | Immediate review required |

---

## Stage-Specific Financial Focus

| Stage | Primary Metrics | Key Questions |
|-------|-----------------|---------------|
| **Pre-seed** | Burn rate, runway | "How long can we experiment?" |
| **Seed** | CAC, early LTV signals | "Can we acquire customers economically?" |
| **Series A** | Unit economics, NRR | "Do the economics work at scale?" |
| **Series B+** | Operating margin, efficiency | "Are we building a real business?" |
| **Exit** | Revenue multiple, EBITDA | "What's our valuation story?" |

---

## Exit Financial Considerations

### Acquisition Metrics

| Metric | Importance | Why |
|--------|------------|-----|
| **Revenue Quality** | High | Recurring > one-time |
| **Customer Concentration** | High | Top 10 customers < 50% |
| **Gross Margin** | High | > 70% for software |
| **Growth Rate** | Medium | Consistent > hockey stick |
| **Profitability Path** | Medium | Clear path matters |

### IPO Readiness

| Requirement | Standard |
|-------------|----------|
| **Revenue Scale** | > $100M ARR typically |
| **Growth Rate** | > 30% YoY |
| **Financial Controls** | SOX compliance ready |
| **Audited Financials** | 2-3 years history |
| **Predictability** | Consistent quarterly performance |

---

## Confidence Calibration

### Financial Confidence Boosters

| Indicator | Confidence Boost |
|-----------|------------------|
| Audited financials available | +0.15 |
| 12+ months of data | +0.10 |
| Unit economics proven | +0.15 |
| Cash runway > 12 months | +0.10 |
| Revenue growing > 50% YoY | +0.10 |

### Financial Confidence Penalties

| Concern | Confidence Penalty |
|---------|-------------------|
| No financial tracking | -0.20 |
| Runway < 6 months | -0.15 |
| Negative unit economics | -0.15 |
| Customer concentration > 50% | -0.10 |
| Projections only (no actuals) | -0.10 |
