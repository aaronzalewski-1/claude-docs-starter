# Getting Claude to Actually Follow Your Documentation

**TL;DR:** Two patterns that dramatically improved my Claude Code workflow: (1) Skills with locked architectural decisions that force context loading before action, and (2) a multi-persona `/review-decision` command inspired by recent AI debate research. The result: less friction, less repetition, tighter adherence to project guidelines.

---

## The Problem We've All Felt

If you've used Claude Code on a real project, you've experienced this loop:

1. Claude suggests refactoring to a pattern you explicitly rejected
2. You explain why that won't work
3. Claude apologizes, proposes the same thing differently
4. You point to your documentation
5. Repeat

The documentation exists. Claude *can* read it. But there's a gap between "documentation available" and "documentation consulted before acting."

This week, that gap closed for me.

## Advancement #1: Skills That Enforce Context Loading

The breakthrough was structuring skills with **mandatory pre-work tables** and **locked architectural decisions**. Not suggestions—requirements.

```markdown
---
name: myproject
description: >
  Development work on MyProject. MUST use this skill for: schema changes,
  API work, scoring logic. This skill contains locked architectural decisions
  that MUST NOT be re-litigated.
---

## Mandatory Pre-Work

| Task Type | Required Reading |
|-----------|------------------|
| Database/Schema changes | `docs/CLAUDE/ARCHITECTURE.md` |
| API endpoint changes | `docs/CLAUDE/API-REFERENCE.md` |
| Any architectural recommendations | `docs/CLAUDE/ARCHITECTURE.md` (read FIRST) |

## Locked Architectural Decisions

These decisions have been made and MUST NOT be re-litigated:

### 1. Single-Tenant Deployment Model
Each deployment serves one customer. Do NOT recommend:
- Multi-tenant database designs
- Tenant selection APIs
- Shared infrastructure patterns

### 2. String-Based IDs Without Foreign Keys
`CustomerId` is a string without FK constraints. This is **intentional** for data portability. Do NOT recommend:
- Adding a Customers table
- Adding FK constraints
- Changing to Guid
```

The key insight: **explicit negation**. Not just "we use X" but "do NOT recommend Y, Z." Claude respects boundaries when they're clearly marked.

### The Observable Difference

Before: Claude would suggest multi-tenant patterns roughly every third session, requiring re-explanation.

After: Zero re-litigation. When Claude encounters a task that might touch a locked decision, it references the constraint and works within it.

The friction disappeared. The repetition stopped. I spend less time defending past decisions and more time building.

## Advancement #2: Multi-Persona Decision Review

This one came from an unexpected source: [research on AI agents debating mathematical problems](https://techxplore.com/news/2025-12-ai-agents-debate-mathematical.html). The finding that stuck with me: when AI agents argue from different positions, they catch errors that individual agents miss.

I built `/review-decision`—a command that evaluates architectural choices through five personas:

```markdown
## Personas

### Skeptic 🔍
Fact-checks every claim. Searches official docs. Flags unverified assumptions.

### Architect 📐
Enforces SOLID. Checks pattern consistency. Flags coupling concerns.

### Economist 💰
Calculates costs, time investment, maintenance burden. Context-aware of constraints.

### Pragmatist 🚀
Asks: "Do we have users? What's the simplest thing that works? Can we defer this?"

### Tech Advocate ⚙️
Ensures idiomatic implementation. Recommends packages. Links to docs.
```

Each persona provides a confidence score (0.0-1.0), and the consensus is weighted by project phase:

```markdown
| Phase | Skeptic | Architect | Economist | Pragmatist | Tech |
|-------|---------|-----------|-----------|------------|------|
| Pre-validation | 0.15 | 0.15 | 0.20 | 0.35 | 0.15 |
| Post-validation | 0.20 | 0.25 | 0.20 | 0.15 | 0.20 |
| Scale-ready | 0.20 | 0.30 | 0.15 | 0.10 | 0.25 |
```

Pre-validation? The Pragmatist weighs heavily—ship and learn. Scale-ready? Architect and Tech Advocate matter more.

### Using It

```
/review-decision Use Redis for session caching instead of in-memory
```

Claude responds with structured analysis from each persona, confidence scores, and a synthesized recommendation that surfaces the key tradeoff.

The Skeptic actually searches documentation. The Economist considers my constraints. When personas disagree by more than 0.3, the output explicitly surfaces the conflict rather than papering over it.

It's like having a review board that's appropriately staffed for *my* specific needs.

## What Changed This Week

The document architecture and Claude integration clicked. Not incrementally—categorically.

I went from "Claude knows about my docs" to "Claude consults specific docs before specific actions, respects locked decisions, and evaluates proposals through multiple lenses."

The patterns:

1. **Skills with teeth**: Mandatory pre-work tables + locked decisions with explicit "do NOT recommend" lists
2. **Context triggers**: `<load_X_context>` tags that tell Claude when to load which documentation
3. **Multi-persona review**: Structured debate that catches what single-perspective analysis misses

## Try It

The [claude-docs-starter](https://github.com/your-repo/claude-docs-starter) kit includes all of this:

- Skill template with locked decisions pattern
- `/review-decision` command (customize the personas for your stack)
- `/codebase-context` for quick session startup
- Context loading triggers for database, API, frontend, testing work
- Settings template with safety-hardened deny list

The personas in `/review-decision` are mine—Skeptic, Architect, Economist, Pragmatist, .NET Advocate. Yours might be different. A frontend project might want a UX Advocate. A startup might weight the Pragmatist even higher. The structure matters more than my specific choices.

---

*This is how I work with Claude Code now. It's collaborative in a way that felt aspirational a month ago. If you're fighting the same friction, maybe something here helps.*
