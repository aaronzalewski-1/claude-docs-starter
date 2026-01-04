---
name: counsel-knowledge
description: Domain expertise for Counsel persona - legal structures, compliance frameworks, IP protection, contracts, risk management
type: persona_skill
persona: personas/advisory/counsel
version: 1.0.0
---

# Counsel Domain Knowledge

> Legal frameworks, compliance requirements, IP protection strategies, contract analysis, and risk management for startup decision-making.

---

## Entity Structure

### Entity Type Comparison

| Type | Liability | Taxation | Fundraising | Best For |
|------|-----------|----------|-------------|----------|
| **LLC** | Limited | Pass-through | Difficult | Small teams, consulting |
| **C-Corp** | Limited | Double taxation | Standard | VC-backed startups |
| **S-Corp** | Limited | Pass-through | Limited | Profitable small businesses |
| **B-Corp** | Limited | C-Corp rules | Standard | Mission-driven companies |

### Delaware C-Corp Advantages

| Advantage | Details |
|-----------|---------|
| **Predictable law** | Well-developed corporate case law |
| **Court of Chancery** | Expert judges for business disputes |
| **Investor familiarity** | Standard for VC investments |
| **Flexible governance** | Board-friendly statutes |
| **Privacy** | Officers/directors not public record |

### Entity Considerations by Stage

| Stage | Typical Structure | Key Considerations |
|-------|-------------------|-------------------|
| **Pre-seed** | LLC or Delaware C-Corp | If seeking VC, use C-Corp |
| **Seed** | Delaware C-Corp | Convert LLC if needed |
| **Series A+** | Delaware C-Corp | Standard requirement |
| **Exit** | Structure clean-up | Remove complexity before transaction |

---

## Intellectual Property

### IP Type Overview

| Type | Protects | Duration | Registration |
|------|----------|----------|--------------|
| **Patent** | Inventions, processes | 20 years | Required (USPTO) |
| **Copyright** | Creative works, code | Life + 70 years | Automatic (registration helps) |
| **Trademark** | Brand names, logos | Indefinite (if maintained) | Recommended (USPTO) |
| **Trade Secret** | Confidential business info | Indefinite (if secret) | Not registered |

### Patent Strategy

| Strategy | When to Use | Cost |
|----------|-------------|------|
| **Provisional Patent** | Early protection, 12-month runway | $2-5K |
| **Utility Patent** | Core technology protection | $15-30K |
| **Design Patent** | UI/visual design protection | $5-10K |
| **Freedom to Operate** | Before launching product | $10-30K |
| **No Patents** | When speed > protection | $0 |

### IP Assignment Requirements

| Document | Purpose | When Required |
|----------|---------|---------------|
| **PIIA** (Proprietary Information and Invention Assignment) | Employee IP assignment | All employees, day 1 |
| **Contractor IP Agreement** | Contractor work belongs to company | All contractors |
| **Founder IP Assignment** | Pre-formation work assigned | At incorporation |

### Common IP Mistakes

| Mistake | Risk | Prevention |
|---------|------|------------|
| No founder IP assignment | Prior work not owned by company | Execute at formation |
| Employee without PIIA | Employee could claim ownership | Mandatory on hiring |
| Open source contamination | Code license conflicts | License audit process |
| Contractor owns work | Work-for-hire ambiguity | Written agreement required |

---

## Compliance Frameworks

### Data Privacy Regulations

| Regulation | Jurisdiction | Key Requirements |
|------------|--------------|------------------|
| **GDPR** | EU residents | Consent, data rights, DPO |
| **CCPA/CPRA** | California residents | Disclosure, opt-out, deletion |
| **HIPAA** | US healthcare data | Security, privacy, breach notification |
| **SOC 2** | Enterprise customers | Security controls attestation |
| **PCI-DSS** | Payment card data | Cardholder data security |

### Compliance by Business Type

| Business Type | Key Compliance |
|---------------|----------------|
| **B2B SaaS** | SOC 2, data processing agreements |
| **Healthcare** | HIPAA, BAA with customers |
| **Fintech** | State licenses, BSA/AML, KYC |
| **Consumer App** | Privacy policy, COPPA if kids |
| **E-commerce** | PCI-DSS, consumer protection |

### Employment Law Essentials

| Area | Key Requirements |
|------|------------------|
| **Classification** | Employee vs. contractor (IRS tests) |
| **At-will Employment** | Offer letter language, exceptions |
| **Equity Grants** | 83(b) elections, vesting schedules |
| **Non-competes** | State-specific enforceability |
| **Discrimination** | Title VII, ADA, state laws |
| **Wages** | Minimum wage, overtime, exempt status |

---

## Contract Essentials

### Customer Contract Key Terms

| Term | Standard Position | Watch For |
|------|-------------------|-----------|
| **Limitation of Liability** | Cap at fees paid | Unlimited liability |
| **Indemnification** | Mutual, IP infringement | One-sided, broad scope |
| **Term and Renewal** | Annual, auto-renewal | Long lock-in, cancellation fees |
| **Data Rights** | Company retains | Customer owns all data |
| **SLA** | 99.9% uptime | Financial penalties |

### Vendor Contract Red Flags

| Red Flag | Risk | Negotiation Point |
|----------|------|-------------------|
| **Unlimited liability** | Disproportionate risk | Cap at contract value |
| **Auto-renewal > 1 year** | Lock-in | Opt-out notice period |
| **Broad IP license** | Losing ownership | Narrow to necessary scope |
| **Audit rights** | Operational burden | Reasonable notice, frequency |
| **Unilateral changes** | Terms can change | Mutual consent required |

### Partnership Agreement Essentials

| Element | Importance | Key Considerations |
|---------|------------|-------------------|
| **Scope** | High | Clear boundaries of partnership |
| **Exclusivity** | High | Geographic, market, temporal limits |
| **Revenue Share** | High | Calculation method, timing |
| **IP Ownership** | High | Who owns joint developments |
| **Term/Termination** | Medium | Exit conditions, notice period |
| **Non-compete** | Medium | Post-termination restrictions |

---

## Fundraising Legal

### Term Sheet Key Terms

| Term | Founder-Friendly | Investor-Friendly |
|------|------------------|-------------------|
| **Liquidation Preference** | 1x non-participating | 2x+ participating |
| **Anti-dilution** | Broad-based weighted avg | Full ratchet |
| **Board Composition** | Founder majority | Investor majority |
| **Protective Provisions** | Standard only | Extensive veto rights |
| **Pro-rata Rights** | None or limited | Full pro-rata |
| **Drag-along** | High threshold (80%+) | Low threshold (50%) |

### Red Flags in Term Sheets

| Red Flag | Risk | Counter |
|----------|------|---------|
| **Participating preferred** | Double-dip on exit | Non-participating |
| **Full ratchet anti-dilution** | Severe down-round impact | Weighted average |
| **Investor board majority** | Loss of control | Equal or founder majority |
| **Broad protective provisions** | Operational constraints | Limit to material decisions |
| **Pay-to-play** | Force existing investors | Remove or narrow scope |

### SAFE vs. Convertible Note

| Feature | SAFE | Convertible Note |
|---------|------|------------------|
| **Debt instrument** | No | Yes |
| **Interest** | None | 2-8% typical |
| **Maturity date** | None | 12-24 months |
| **Valuation cap** | Yes | Yes |
| **Discount** | Optional | Common (15-25%) |
| **Complexity** | Simple | More complex |

---

## Risk Management

### Risk Categories

| Category | Examples | Mitigation |
|----------|----------|------------|
| **Legal** | Lawsuits, regulatory action | Insurance, compliance programs |
| **Operational** | System failures, key person | Redundancy, documentation |
| **Financial** | Cash shortage, fraud | Controls, insurance |
| **Strategic** | Market changes, competition | Diversification, monitoring |
| **Reputational** | PR crises, data breaches | Crisis plan, security |

### Insurance Requirements

| Insurance Type | Coverage | When Required |
|----------------|----------|---------------|
| **D&O** | Director/officer personal liability | At first funding |
| **E&O/Professional** | Professional service claims | If selling services |
| **Cyber Liability** | Data breach costs | If handling customer data |
| **General Liability** | Physical premises, events | If physical location |
| **Workers' Comp** | Employee injuries | When hiring employees |

### Litigation Risk Assessment

| Factor | Lower Risk | Higher Risk |
|--------|------------|-------------|
| **Industry** | B2B SaaS | Consumer, fintech, healthcare |
| **IP landscape** | Clear freedom to operate | Crowded patent space |
| **Employment** | Small team, clear policies | Large team, misclassification |
| **Customer contracts** | Liability caps | Unlimited liability |
| **Data handling** | Minimal PII | Sensitive data |

---

## Exit Legal Considerations

### Acquisition Due Diligence Areas

| Area | Key Documents | Common Issues |
|------|---------------|---------------|
| **Corporate** | Formation docs, cap table | Missing consents, wrong entity |
| **IP** | Assignments, licenses | Incomplete assignments |
| **Contracts** | Customer, vendor | Change of control provisions |
| **Employment** | Agreements, equity grants | Missing PIIAs, classification |
| **Litigation** | Pending/threatened | Undisclosed claims |
| **Compliance** | Regulatory filings | Gaps in compliance |

### M&A Deal Structure

| Structure | Tax Treatment | Liability |
|-----------|---------------|-----------|
| **Stock Purchase** | Capital gains to sellers | Buyer assumes all |
| **Asset Purchase** | Ordinary income possible | Buyer chooses what to assume |
| **Merger** | Capital gains to sellers | Surviving entity assumes |

### Reps & Warranties Focus

| Category | Key Representations |
|----------|---------------------|
| **Organization** | Valid existence, authority |
| **Capitalization** | Accurate cap table, no hidden equity |
| **IP** | Ownership, no infringement |
| **Contracts** | No breaches, no change of control issues |
| **Compliance** | No violations, permits current |
| **Litigation** | No pending or threatened claims |

### IPO Legal Requirements

| Requirement | Details |
|-------------|---------|
| **S-1 Registration** | Comprehensive disclosure document |
| **SOX Compliance** | Internal controls, certifications |
| **Audited Financials** | 2-3 years, PCAOB auditor |
| **Corporate Governance** | Independent directors, committees |
| **Quiet Period** | Restrictions on communications |

---

## Stage-Specific Legal Focus

| Stage | Priority Legal Matters |
|-------|----------------------|
| **Pre-seed** | Entity formation, founder agreements, IP assignment |
| **Seed** | SAFE/convertible notes, employee agreements, basic compliance |
| **Series A** | Preferred stock docs, option pool, board governance |
| **Series B+** | International expansion, M&A readiness, compliance scaling |
| **Exit** | Due diligence prep, reps & warranties, deal structure |

---

## Confidence Calibration

### Legal Confidence Boosters

| Indicator | Confidence Boost |
|-----------|------------------|
| Clean cap table, no issues | +0.15 |
| All IP properly assigned | +0.15 |
| Compliance program in place | +0.10 |
| Legal counsel engaged | +0.10 |
| Insurance appropriate to stage | +0.10 |

### Legal Confidence Penalties

| Concern | Confidence Penalty |
|---------|-------------------|
| Missing founder IP assignment | -0.20 |
| Pending litigation | -0.15 |
| Regulatory compliance gaps | -0.15 |
| No employee agreements | -0.10 |
| Unknown cap table issues | -0.15 |
