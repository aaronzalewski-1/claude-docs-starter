---
name: librarian-knowledge
description: Domain expertise for Librarian persona - source evaluation, citation tracing, evidence hierarchies
type: persona_skill
persona: personas/research/librarian
version: 1.0.0
---

# Librarian Domain Knowledge

> Source evaluation frameworks, citation analysis, and evidence quality hierarchies.

---

## Source Classification

### Primary Sources

**Definition**: Original, first-hand accounts or direct evidence.

| Field | Primary Sources |
|-------|-----------------|
| **Science** | Original research papers, raw data, lab notebooks |
| **History** | Letters, diaries, photographs, artifacts |
| **Law** | Statutes, court decisions, regulations |
| **Business** | Financial reports, internal memos, meeting minutes |
| **Technology** | Source code, API docs, RFC specifications |

### Secondary Sources

**Definition**: Analysis, interpretation, or synthesis of primary sources.

| Type | Examples |
|------|----------|
| **Reviews** | Literature reviews, systematic reviews |
| **Analysis** | Commentary, critique, case studies |
| **Reference** | Textbooks, handbooks |
| **News** | Journalism about events |

### Tertiary Sources

**Definition**: Compilations of primary and secondary sources.

| Type | Examples |
|------|----------|
| **Encyclopedias** | Wikipedia, Britannica |
| **Indexes** | Bibliographies, databases |
| **Directories** | Who's Who, industry guides |
| **Fact books** | Almanacs, yearbooks |

---

## Source Evaluation Framework (CRAAP)

### Currency

| Question | Red Flag | Green Flag |
|----------|----------|------------|
| When published/updated? | >5 years in fast-moving field | Recent, regularly updated |
| Links working? | Broken links | All links valid |
| Information current? | Outdated stats/facts | Current data cited |

### Relevance

| Question | Red Flag | Green Flag |
|----------|----------|------------|
| Does it address your question? | Tangential | Direct match |
| Who is the intended audience? | Wrong level/field | Appropriate audience |
| Is the scope right? | Too broad/narrow | Right scope |

### Authority

| Question | Red Flag | Green Flag |
|----------|----------|------------|
| Who is the author? | No author, anonymous | Named expert |
| What are their credentials? | No relevant expertise | Relevant qualifications |
| Who is the publisher? | Unknown, predatory | Reputable institution |
| Is there contact info? | None | Available |

### Accuracy

| Question | Red Flag | Green Flag |
|----------|----------|------------|
| Is information supported? | No citations | Sources cited |
| Can claims be verified? | Unverifiable | Traceable to evidence |
| Has it been reviewed? | No review process | Peer-reviewed |
| Are there factual errors? | Errors found | Accurate when checked |

### Purpose

| Question | Red Flag | Green Flag |
|----------|----------|------------|
| Why does this exist? | To sell, propagandize | To inform, educate |
| Is bias disclosed? | Hidden agenda | Transparent |
| Is it fact or opinion? | Opinion as fact | Clear distinction |
| Are conflicts disclosed? | Hidden conflicts | COI stated |

---

## Evidence Hierarchies

### Clinical/Medical Evidence Pyramid

| Level | Evidence Type | Description |
|-------|---------------|-------------|
| 1 | Systematic reviews/Meta-analyses | Synthesis of multiple studies |
| 2 | Randomized controlled trials | Experimental, controlled |
| 3 | Cohort studies | Observational, longitudinal |
| 4 | Case-control studies | Retrospective comparison |
| 5 | Case series/reports | Individual observations |
| 6 | Expert opinion | Without explicit evidence |
| 7 | Mechanistic reasoning | Based on theory alone |

### Social Science Evidence

| Level | Evidence Type |
|-------|---------------|
| 1 | Systematic reviews with meta-analysis |
| 2 | Randomized experiments |
| 3 | Quasi-experiments |
| 4 | Controlled observational studies |
| 5 | Uncontrolled observational studies |
| 6 | Qualitative studies |
| 7 | Expert opinion |

### Legal Evidence

| Level | Evidence Type |
|-------|---------------|
| 1 | Constitutional/statutory law |
| 2 | Regulations |
| 3 | Supreme Court decisions |
| 4 | Appellate court decisions |
| 5 | Trial court decisions |
| 6 | Legal commentary/treatises |
| 7 | Expert opinion |

---

## Citation Analysis

### Citation Chain Tracing

**Process:**
```
Current Source [D]
    │ cites
    ▼
Secondary Source [C]
    │ cites
    ▼
Secondary Source [B]
    │ cites
    ▼
Primary Source [A] ← TRACE TO HERE
```

### Citation Quality Checks

| Check | What to Look For |
|-------|------------------|
| **Accuracy** | Does citation say what claimer says? |
| **Context** | Is citation used in original context? |
| **Completeness** | Is full finding represented? |
| **Currency** | Is citation still current/valid? |
| **Circularity** | Does A cite B cite A? |

### Citation Red Flags

| Red Flag | Concern |
|----------|---------|
| No citation for major claim | Unverifiable |
| Citation to self only | May be circular |
| Citation to press release | Not peer-reviewed |
| Citation to abstract only | May misrepresent full paper |
| Broken citation chain | Cannot verify original |
| Citation to retracted work | Invalid evidence |

---

## Academic Source Evaluation

### Journal Quality Indicators

| Indicator | What It Means |
|-----------|---------------|
| **Impact Factor** | Average citations per article |
| **h-index** | Journal productivity and impact |
| **Peer Review** | Expert evaluation |
| **Indexing** | Listed in major databases |
| **Publisher** | Reputable academic publisher |

### Predatory Journal Red Flags

| Red Flag | Warning |
|----------|---------|
| Unsolicited email invitations | Aggressive solicitation |
| Very fast peer review (days) | Inadequate review |
| No clear editorial process | Lack of rigor |
| Vague journal scope | Accepts anything |
| Hidden or unclear fees | Financial focus |
| No retraction policy | No quality control |
| Fake impact factors | Misleading metrics |

### Author Credibility

| Indicator | How to Check |
|-----------|--------------|
| **Expertise** | Publications in field |
| **Affiliation** | Institutional connection |
| **Citations** | Others cite their work |
| **Conflicts** | Disclosed interests |
| **Track record** | Previous reliable work |

---

## Online Source Evaluation

### Domain Credibility

| Domain | Typical Credibility | Notes |
|--------|---------------------|-------|
| .gov | High | Government sources |
| .edu | Medium-High | Academic institutions |
| .org | Variable | Non-profits, some biased |
| .com | Variable | Commercial, verify carefully |
| .io | Variable | Tech common, verify |

### Website Evaluation

| Element | What to Check |
|---------|---------------|
| **About page** | Organization info, mission |
| **Author info** | Who wrote it, credentials |
| **Date** | When published/updated |
| **Sources** | Citations provided |
| **Contact** | Way to reach organization |
| **Design** | Professional vs. amateur |
| **Ads** | Heavy advertising = caution |

---

## Finding Better Sources

### Academic Sources

| Resource | What It Offers |
|----------|----------------|
| **Google Scholar** | Broad academic search |
| **PubMed** | Biomedical literature |
| **JSTOR** | Humanities, social sciences |
| **IEEE Xplore** | Engineering, technology |
| **arXiv** | Preprints (physics, CS, math) |
| **SSRN** | Social science preprints |

### Government/Official Sources

| Resource | What It Offers |
|----------|----------------|
| **data.gov** | US government data |
| **WHO** | Global health data |
| **World Bank** | Economic data |
| **OECD** | International statistics |

### Standards and Specifications

| Resource | What It Offers |
|----------|----------------|
| **RFC Editor** | Internet standards |
| **ISO** | International standards |
| **W3C** | Web standards |
| **NIST** | US measurement standards |

---

## Confidence Calibration

### Source Quality Indicators

| Indicator | Confidence Boost |
|-----------|------------------|
| Peer-reviewed | +0.20 |
| Primary source | +0.15 |
| Multiple corroborating sources | +0.15 |
| Expert author | +0.10 |
| Reputable publisher | +0.10 |
| Recent and current | +0.05 |

### Source Quality Concerns

| Concern | Confidence Penalty |
|---------|-------------------|
| No author | -0.15 |
| No date | -0.10 |
| No citations | -0.15 |
| Conflicts of interest | -0.15 |
| Outdated | -0.10 |
| Single source | -0.10 |
| Predatory journal | -0.25 |
