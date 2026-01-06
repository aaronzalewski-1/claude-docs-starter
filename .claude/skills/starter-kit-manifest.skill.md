---
name: starter-kit-manifest
description: Complete list of files included in the Claude Code Decision Framework, used by /INITIALIZE_STARTER_KIT to identify user's existing project files
type: skill
version: 1.0.0
---

# Framework File Manifest

> This skill provides the definitive list of files that are part of the Claude Code Decision Framework.
> Any files NOT in this list (and not in excluded directories) are considered the user's "existing context".

---

## Usage

When running `/INITIALIZE_STARTER_KIT`:
1. Scan all files in the project directory
2. Exclude files matching this manifest
3. Exclude infrastructure directories (see Exclusions below)
4. Remaining files = user's existing project context

---

## Starter Kit Files (77 total)

### Root Directory (4 files)

```
.gitignore
CLAUDE.md
LICENSE
README.md
```

### .claude/ Configuration (6 files)

```
.claude/CREATING-COMMANDS.md
.claude/CREATING-SKILLS.md
.claude/README.md
.claude/hooks.template.json
.claude/settings.local.json
.claude/settings.template.json
```

### .claude/commands/ Workflow Commands (8 files)

```
.claude/commands/DEEPPLAN.md
.claude/commands/INITIALIZE_STARTER_KIT.md
.claude/commands/NEXTSTEPS.md
.claude/commands/REFOCUS.md
.claude/commands/codebase-context.md
.claude/commands/list-personas.md
.claude/commands/review-business-decision.md
.claude/commands/review-product-decision.md
.claude/commands/review-research.md
```

### .claude/commands/personas/advisory/ (7 files)

```
.claude/commands/personas/advisory/cfo.md
.claude/commands/personas/advisory/counsel.md
.claude/commands/personas/advisory/go-to-market.md
.claude/commands/personas/advisory/operations.md
.claude/commands/personas/advisory/product-advisor.md
.claude/commands/personas/advisory/skeptic.md
.claude/commands/personas/advisory/strategist.md
```

### .claude/commands/personas/product/ (4 files)

```
.claude/commands/personas/product/architect.md
.claude/commands/personas/product/economist.md
.claude/commands/personas/product/pragmatist.md
.claude/commands/personas/product/skeptic.md
```

### .claude/commands/personas/research/ (5 files)

```
.claude/commands/personas/research/critic.md
.claude/commands/personas/research/librarian.md
.claude/commands/personas/research/methodologist.md
.claude/commands/personas/research/skeptic.md
.claude/commands/personas/research/synthesizer.md
```

### .claude/skills/ Base Skills (3 files)

```
.claude/skills/artifact-registry.skill.md
.claude/skills/project-name.skill.md.template
.claude/skills/starter-kit-manifest.skill.md
```

### .claude/skills/personas/advisory/ (7 files)

```
.claude/skills/personas/advisory/cfo.persona.md
.claude/skills/personas/advisory/counsel.persona.md
.claude/skills/personas/advisory/go-to-market.persona.md
.claude/skills/personas/advisory/operations.persona.md
.claude/skills/personas/advisory/product-advisor.persona.md
.claude/skills/personas/advisory/skeptic.persona.md
.claude/skills/personas/advisory/strategist.persona.md
```

### .claude/skills/personas/product/ (4 files)

```
.claude/skills/personas/product/architect.persona.md
.claude/skills/personas/product/economist.persona.md
.claude/skills/personas/product/pragmatist.persona.md
.claude/skills/personas/product/skeptic.persona.md
```

### .claude/skills/personas/research/ (5 files)

```
.claude/skills/personas/research/critic.persona.md
.claude/skills/personas/research/librarian.persona.md
.claude/skills/personas/research/methodologist.persona.md
.claude/skills/personas/research/skeptic.persona.md
.claude/skills/personas/research/synthesizer.persona.md
```

### .claude/templates/ Artifact Templates (3 files)

```
.claude/templates/advisory/board-memo.template.md
.claude/templates/product/adr.template.md
.claude/templates/research/literature-review.template.md
```

### .claude/templates/onboarding/ (4 files)

```
.claude/templates/onboarding/persona-command.template.md
.claude/templates/onboarding/persona-skill.template.md
.claude/templates/onboarding/review-orchestrator.template.md
.claude/templates/onboarding/user-manual.template.md
```

### docs/CLAUDE/ Documentation Framework (11 files)

```
docs/CLAUDE/API-REFERENCE.md
docs/CLAUDE/APPENDIX.md
docs/CLAUDE/ARCHITECTURE.md
docs/CLAUDE/CHANGELOG.md
docs/CLAUDE/CORE-LIBRARY.md
docs/CLAUDE/DEVELOPMENT.md
docs/CLAUDE/IMPROVEMENTS.md
docs/CLAUDE/PERSONA-PACKAGES.md
docs/CLAUDE/PERSONAS.md
docs/CLAUDE/ROADMAP.md
docs/CLAUDE/SESSION-STATE.template.json
```

### docs/ Other Documentation (4 files)

```
docs/decisions/README.md
docs/blog-claude-code-improvements.md
docs/blog-draft-enhancements-dec-2025.md
docs/blog-multi-persona-decision-making.md
```

---

## Excluded Directories

These directories should always be excluded from context scanning:

| Directory | Reason |
|-----------|--------|
| `.git/` | Version control metadata |
| `node_modules/` | JavaScript dependencies |
| `vendor/` | PHP/Go dependencies |
| `dist/` | Build output |
| `build/` | Build output |
| `bin/` | Compiled binaries |
| `obj/` | .NET intermediate files |
| `__pycache__/` | Python cache |
| `.venv/` | Python virtual environment |
| `target/` | Rust/Java build output |
| `.next/` | Next.js build cache |
| `.nuxt/` | Nuxt.js build cache |
| `coverage/` | Test coverage reports |

---

## Excluded File Patterns

These file types should be excluded from context reading:

| Pattern | Reason |
|---------|--------|
| `*.lock` | Lock files (package-lock.json, yarn.lock, etc.) |
| `*.log` | Log files |
| `*.min.js`, `*.min.css` | Minified assets |
| `*.map` | Source maps |
| `*.png`, `*.jpg`, `*.gif`, `*.svg`, `*.ico` | Images |
| `*.woff`, `*.woff2`, `*.ttf`, `*.eot` | Fonts |
| `*.pdf`, `*.docx`, `*.xlsx` | Documents |
| `*.zip`, `*.tar`, `*.gz` | Archives |
| `*.exe`, `*.dll`, `*.so`, `*.dylib` | Binaries |

---

## Generated Files (Created During Initialization)

These files are NOT part of the starter kit. They are created by `/INITIALIZE_STARTER_KIT` and tracked in `.claude/initialization-state.json` for uninstall/reinstall.

### Core Generated Files

```
.claude/initialization-state.json          # Tracks installation state
.claude/skills/{project-name}.skill.md     # Project-specific skill (from template)
docs/CLAUDE/USER-MANUAL.md                 # Customized user manual
```

### Custom Persona Files (Optional)

If user creates custom domain personas:

```
.claude/commands/personas/{domain}/        # Custom persona commands
.claude/skills/personas/{domain}/          # Custom persona skills
.claude/commands/review-{domain}-decision.md  # Custom domain orchestrator
```

**Note:** Pre-built personas (`advisory/`, `product/`, `research/`) are part of the starter kit. Custom personas use OTHER domain names (e.g., `fintech/`, `healthcare/`).

---

## Maintenance

When adding new files to the starter kit:
1. Add the file path to the appropriate section above
2. Update the file count in the section header
3. Update the total count in the "Starter Kit Files" header
