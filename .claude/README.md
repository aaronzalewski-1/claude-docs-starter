# .claude Folder

This folder contains Claude Code configuration and customizations for your project.

## Contents

```
.claude/
├── commands/           # Custom slash commands
│   ├── DEEPPLAN.md     # /DEEPPLAN - Structured implementation workflow
│   ├── REFOCUS.md      # /REFOCUS - Debug reset protocol
│   └── NEXTSTEPS.md    # /NEXTSTEPS - Sprint planning assistant
├── settings.local.json # Local permissions (git-ignored, user-specific)
└── README.md           # This file
```

## Commands

Custom slash commands are Markdown files in the `commands/` folder. The filename (without `.md`) becomes the command name.

- `/DEEPPLAN` - Use when starting a multi-step feature implementation
- `/REFOCUS` - Use when debugging spirals or you're stuck
- `/NEXTSTEPS` - Use when planning the next sprint

See [CREATING-COMMANDS.md](CREATING-COMMANDS.md) for how to create your own.

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
