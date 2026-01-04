# .claude Folder

This folder contains Claude Code configuration and customizations for your project.

## Contents

```
.claude/
├── commands/                 # Custom slash commands
│   ├── personas/             # Analytical persona commands
│   │   ├── skeptic.md        # /personas:skeptic - Fact-checker
│   │   ├── architect.md      # /personas:architect - Structure guardian
│   │   ├── economist.md      # /personas:economist - Cost analyst
│   │   └── pragmatist.md     # /personas:pragmatist - MVP advocate
│   ├── review-decision.md    # /review-decision - Multi-persona orchestrator
│   ├── DEEPPLAN.md           # /DEEPPLAN - Structured implementation workflow
│   ├── REFOCUS.md            # /REFOCUS - Debug reset protocol
│   ├── NEXTSTEPS.md          # /NEXTSTEPS - Sprint planning assistant
│   └── codebase-context.md   # /codebase-context - Refresh context
├── skills/                   # Domain-specific skills
│   ├── personas/             # Persona domain expertise
│   │   ├── skeptic.persona.md
│   │   ├── architect.persona.md
│   │   ├── economist.persona.md
│   │   └── pragmatist.persona.md
│   └── *.skill.md            # Project skills with locked decisions
├── settings.local.json       # Local permissions (git-ignored)
└── README.md                 # This file
```

## Personas

The persona system provides multi-perspective analysis for implementation decisions.

### Three-Tier Architecture

| Tier | Purpose | Example |
|------|---------|---------|
| **Persona Command** | Analytical lens with process | `/personas:skeptic` |
| **Persona Skill** | Domain expertise frameworks | `skeptic.persona.md` |
| **Orchestrator** | Runs all personas, synthesizes | `/review-decision` |

### Available Personas

| Persona | Mandate | Use When |
|---------|---------|----------|
| **Skeptic** | Trust nothing. Verify everything. | Need claims verified, assumptions challenged |
| **Architect** | Design for change. Isolate what varies. | Evaluating structure, patterns, testability |
| **Economist** | Every choice has a cost. Make them visible. | Comparing costs, build vs buy, ROI |
| **Pragmatist** | Ship to learn. Perfect later. | Questioning complexity, finding MVP path |

### Usage

**Individual persona:**
```
/personas:skeptic Should we use this library?
```

**Full multi-persona review:**
```
/review-decision Add caching layer to improve performance
```

See [docs/CLAUDE/PERSONAS.md](../docs/CLAUDE/PERSONAS.md) for detailed documentation.

## Commands

Custom slash commands are Markdown files in the `commands/` folder. The filename (without `.md`) becomes the command name.

- `/DEEPPLAN` - Use when starting a multi-step feature implementation
- `/REFOCUS` - Use when debugging spirals or you're stuck
- `/NEXTSTEPS` - Use when planning the next sprint
- `/review-decision` - Multi-persona decision review

See [CREATING-COMMANDS.md](CREATING-COMMANDS.md) for how to create your own.

## Skills

Skills are domain-specific knowledge files that provide Claude with persistent context about your project. Unlike commands (which automate workflows), skills encode:

- **Locked architectural decisions** - Prevent Claude from re-litigating settled choices
- **Mandatory reading requirements** - Ensure docs are read before certain tasks
- **Domain patterns** - Project-specific conventions and anti-patterns

**Getting Started:**
1. Copy `.claude/skills/project-name.skill.md.template` to `yourproject.skill.md`
2. Fill in your project-specific values
3. Document your locked decisions

See [CREATING-SKILLS.md](CREATING-SKILLS.md) for detailed guidance.

## Settings

### settings.local.json (User-Specific)

This file configures which commands Claude can run without asking. It's git-ignored because permissions are personal preferences.

Create your own based on [settings.template.json](settings.template.json).

### Common Permission Patterns

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test:*)",
      "Bash(npm run build:*)",
      "Bash(git status:*)"
    ]
  }
}
```

## Hooks (Optional)

Claude Code supports hooks that run before/after tool calls. See [hooks.template.json](hooks.template.json) for examples.

## Learn More

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Custom Commands Guide](CREATING-COMMANDS.md)
- [Custom Skills Guide](CREATING-SKILLS.md)
- [Personas Documentation](../docs/CLAUDE/PERSONAS.md)
