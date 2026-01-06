---
name: INITIALIZE_STARTER_KIT
description: Initialize Claude Code Decision Framework (project)
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion, TodoWrite
---

# Initialize Decision Framework

Guide the user through customizing the Claude Code Decision Framework for their specific project.

---

## Implementation Principles

<minimize_permission_requests>
**This command functions as an installer. Minimize user interruptions:**

1. **Gather ALL information before writing** - Complete Phases 1-3 (discovery, understanding, confirmation) before any file operations
2. **Pre-authorize file operations** - Show complete file manifest, get blanket approval in Phase 4
3. **Batch writes in parallel** - Execute multiple Write tools in a single response = single permission prompt
4. **Read templates first** - Read operations don't require permission; prepare all content before writing
5. **Two permission checkpoints maximum:**
   - Phase 4: Authorize core files (CLAUDE.md, project skill, user manual)
   - Phase 6: Authorize persona files (if creating custom personas)
</minimize_permission_requests>

---

## Installation State Schema

The installer uses a state file (`.claude/initialization-state.json`) to track progress and enable recovery from partial failures.

### State Statuses

| Status | Meaning | Recovery Action |
|--------|---------|-----------------|
| `pending` | Installation started but no files written yet | Resume or clean restart |
| `core_complete` | CLAUDE.md and project skill created | Resume from persona phase |
| `personas_complete` | Custom personas created (if any) | Resume from completion phase |
| `complete` | Installation fully successful | Normal reinstall/uninstall |

### State File Structure

```json
{
  "status": "pending|core_complete|personas_complete|complete",
  "startedAt": "[ISO 8601 timestamp]",
  "completedAt": "[ISO 8601 timestamp or null]",
  "version": "1.0.0",
  "projectName": "[Display Name]",
  "projectNameKebab": "[kebab-case-name]",
  "domain": "[detected or selected domain]",
  "setupMode": "full|quick",
  "config": {
    "backend": "[tech]",
    "frontend": "[tech or null]",
    "database": "[tech or null]",
    "buildCommand": "[command]",
    "testCommand": "[command]",
    "migrationCommand": "[command or null]"
  },
  "filesCreated": [],
  "personasCreated": [],
  "pendingPersonas": []
}
```

### Recovery Principle

**Write state BEFORE operations, update state AFTER success.**

This ensures that if an operation fails:
1. The state file exists and indicates what was attempted
2. On retry, Phase 0 can detect the incomplete state
3. User can choose to resume or start fresh

---

## Overview

This command runs an 8-phase guided workflow using Claude's dialog UI for all user decisions:

| Phase | Name | Description |
|-------|------|-------------|
| 0 | Detect | Check for prior initialization; offer reinstall/uninstall |
| 1 | Welcome | Present overview and confirm user wants to proceed |
| 2 | Discover | Scan for user's existing project files |
| 3 | Understand | Analyze files, present findings, confirm accuracy |
| 4 | Configure | Guide through CLAUDE.md and project skill configuration |
| 5 | Propose | Suggest custom personas based on domain |
| 6 | Build | Create custom persona package if accepted |
| 7 | Complete | Generate user manual and present summary |

---

## Phase 0: Detect (Reinstall/Uninstall)

**Run this phase FIRST before any welcome message.**

### Step 0.1: Check Initialization State

Check if the starter kit has already been initialized:

1. **Primary check:** Look for `.claude/initialization-state.json`
2. **If found, check `status` field:**
   - `"complete"` → Fully initialized (Step 0.4)
   - `"pending"`, `"core_complete"`, or `"personas_complete"` → Incomplete installation (Step 0.3)
3. **Fallback checks** (if state file missing):
   - Check if any `.claude/skills/*.skill.md` exists (not `.template`)
   - Check if `CLAUDE.md` contains no `{{` placeholders
   - If orphan files found → Treat as incomplete (Step 0.3)

### Step 0.2: If NOT Initialized

Skip to Phase 1 (Welcome). This is a fresh installation.

### Step 0.3: If Incomplete Installation Detected

Read `.claude/initialization-state.json` to determine what was completed:

```
## Incomplete Installation Detected

A previous installation attempt did not complete successfully.

**Status:** [status] (started [startedAt])

**What was completed:**
[If status >= core_complete:]
✓ CLAUDE.md configured
✓ Project skill created: .claude/skills/[project-name].skill.md
[If status >= personas_complete:]
✓ Custom personas created

**What remains:**
[If status == pending:]
• Configure CLAUDE.md and create project skill
• Create custom personas (optional)
• Generate user manual
[If status == core_complete:]
• Create custom personas (optional)
• Generate user manual
[If status == personas_complete:]
• Generate user manual
```

```json
{
  "questions": [
    {
      "question": "How would you like to proceed with the incomplete installation?",
      "header": "Recovery",
      "multiSelect": false,
      "options": [
        {
          "label": "Resume installation (Recommended)",
          "description": "Continue from where it left off"
        },
        {
          "label": "Start fresh",
          "description": "Remove partial files and begin again"
        },
        {
          "label": "Cancel",
          "description": "Exit without changes"
        }
      ]
    }
  ]
}
```

**If "Resume installation":**
- Based on `status`, skip to the appropriate phase:
  - `pending` → Phase 4 (Configure)
  - `core_complete` → Phase 5 (Propose personas) or Phase 7 if quick setup
  - `personas_complete` → Phase 7 (Complete)
- Restore context from state file (projectName, domain, config, etc.)

**If "Start fresh":**
- Delete all files listed in `filesCreated` and `personasCreated`
- Delete `.claude/initialization-state.json`
- Continue to Phase 1 (Welcome)

**If "Cancel":**
- Exit without changes

### Step 0.4: If Fully Initialized

Read `.claude/initialization-state.json` to get current configuration, then present:

```
## Existing Installation Detected

This project was initialized on [timestamp].

**Current configuration:**
• Project: [projectName]
• Domain: [domain]
• Custom personas: [count] created

**Files that were created:**
• .claude/skills/[project-name].skill.md
• docs/CLAUDE/USER-MANUAL.md
[If personas exist:]
• .claude/commands/personas/[domain]/ ([count] personas)
```

```json
{
  "questions": [
    {
      "question": "What would you like to do?",
      "header": "Reinstall",
      "multiSelect": false,
      "options": [
        {
          "label": "Update configuration",
          "description": "Change project settings without affecting custom personas"
        },
        {
          "label": "Full reset",
          "description": "Remove all generated files and run setup from scratch"
        },
        {
          "label": "Uninstall",
          "description": "Remove all generated files and exit"
        },
        {
          "label": "Cancel",
          "description": "Exit without changes"
        }
      ]
    }
  ]
}
```

### Step 0.4: Handle Reinstall Options

**If "Update configuration":**
- Skip to [Update Config Flow](#update-config-flow) (see below)

**If "Full reset":**
- Run [Uninstall Flow](#uninstall-flow) silently (no confirmation needed)
- Then continue to Phase 1 (Welcome) for fresh setup

**If "Uninstall":**
- Run [Uninstall Flow](#uninstall-flow) with confirmation
- Exit after completion

**If "Cancel":**
- Exit without changes

---

## Phase 1: Welcome

### Step 1.1: Present Welcome Dialog

Use `AskUserQuestion` to welcome the user and explain what will happen:

```json
{
  "questions": [
    {
      "question": "Ready to initialize the Claude Code Decision Framework for your project?",
      "header": "Welcome",
      "multiSelect": false,
      "options": [
        {
          "label": "Start Setup",
          "description": "Scan your project, configure documentation, and optionally create custom personas"
        },
        {
          "label": "Quick Setup",
          "description": "Just configure CLAUDE.md and project skill - skip persona creation"
        },
        {
          "label": "Cancel",
          "description": "Exit without making any changes"
        }
      ]
    }
  ]
}
```

**If "Cancel":** Thank the user and exit. No changes made.
**If "Quick Setup":** Set flag to skip Phases 5-6.
**If "Start Setup":** Continue to Phase 2.

---

## Phase 2: Discover

### Step 2.1: Load the Manifest

Read `.claude/skills/starter-kit-manifest.skill.md` to get the list of starter kit files.

### Step 2.2: Scan for User Files

Scan the project directory for files that are NOT part of the starter kit.

**Exclude these directories:**
- `.git/`, `node_modules/`, `vendor/`, `dist/`, `build/`, `bin/`, `obj/`
- `__pycache__/`, `.venv/`, `target/`, `.next/`, `.nuxt/`, `coverage/`

**Exclude these file patterns:**
- Lock files: `*.lock`, `package-lock.json`, `yarn.lock`
- Build artifacts: `*.min.js`, `*.min.css`, `*.map`
- Media: `*.png`, `*.jpg`, `*.gif`, `*.svg`, `*.ico`, `*.woff*`, `*.ttf`
- Documents: `*.pdf`, `*.docx`, `*.xlsx`
- Binaries: `*.exe`, `*.dll`, `*.so`, `*.dylib`

**Remaining files = User's "Existing Context"**

### Step 2.3: Report Discovery

Display to user (not a dialog, just informational output):

```
## Step 1 of 7: Discovering Your Project

Scanning for existing project files...

Found [N] files outside the starter kit:
• Source code: [count]
• Configuration: [count]
• Documentation: [count]
• Tests: [count]

Analyzing your project...
```

---

## Phase 3: Understand

### Step 3.1: Read Context Files

Read discovered files to extract project information. Prioritize:
1. `package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj` - Tech stack
2. `README.md`, `README.txt` - Project description
3. Source files in `src/`, `app/`, `lib/` - Domain entities
4. Configuration files - Architecture clues

### Step 3.2: Extract Project Profile

Identify:
- **Project Name**: From package.json, directory name, or README
- **Project Type**: Web app, API, library, CLI, mobile app, etc.
- **Tech Stack**: Languages, frameworks, databases
- **Domain**: E-commerce, healthcare, fintech, SaaS, gaming, EdTech, etc.
- **Key Entities**: Main domain objects/models
- **Architecture**: Monolith, microservices, serverless, etc.

### Step 3.3: Present Understanding and Confirm

Display findings then use `AskUserQuestion`:

```
## Step 2 of 7: Understanding Your Project

| Property | Detected Value |
|----------|----------------|
| Project Name | [name] |
| Project Type | [type] |
| Tech Stack | [stack] |
| Domain | [domain] |
| Key Entities | [entities] |
| Architecture | [pattern] |

Key files analyzed:
• [file1] - [purpose]
• [file2] - [purpose]

My understanding: [2-3 sentence summary]
```

```json
{
  "questions": [
    {
      "question": "Is this understanding of your project accurate?",
      "header": "Confirm",
      "multiSelect": false,
      "options": [
        {
          "label": "Yes, continue",
          "description": "The analysis is correct, proceed to configuration"
        },
        {
          "label": "Partially correct",
          "description": "I'll provide corrections so you can re-analyze"
        },
        {
          "label": "Very wrong",
          "description": "Start over with manual input"
        }
      ]
    }
  ]
}
```

**If "Yes, continue":** Proceed to Phase 4.
**If "Partially correct":** Ask what's wrong, update understanding, present again.
**If "Very wrong":** Use dialog to ask for manual input of each property.

---

## Phase 4: Configure

This phase updates TWO files:
1. `CLAUDE.md` - Project documentation hub
2. `{project-name}.skill.md` - Project-specific skill with locked decisions

### Step 4.0a: Initialize State File (Recovery Support)

**BEFORE any file operations**, create the state file with `status: "pending"`:

```json
{
  "status": "pending",
  "startedAt": "[ISO 8601 timestamp]",
  "completedAt": null,
  "version": "1.0.0",
  "projectName": "[confirmed project name]",
  "projectNameKebab": "[kebab-case]",
  "domain": "[confirmed domain]",
  "setupMode": "[full|quick]",
  "config": {
    "backend": "[confirmed tech]",
    "frontend": "[confirmed tech or null]",
    "database": "[confirmed tech or null]",
    "buildCommand": "[confirmed command]",
    "testCommand": "[confirmed command]",
    "migrationCommand": "[confirmed command or null]"
  },
  "filesCreated": [],
  "personasCreated": [],
  "pendingPersonas": "[list of personas user selected, if any]"
}
```

**Why write this first:** If subsequent operations fail, this file enables recovery on retry.

### Step 4.0b: Pre-Authorization (Minimize Permission Requests)

**IMPORTANT:** Before making any file changes, present a complete manifest of all files that will be created or modified, then request blanket authorization.

```
## Step 3 of 7: Review Planned Changes

The following files will be created or modified:

**Will be MODIFIED:**
• CLAUDE.md - Replace placeholder values with your project details

**Will be CREATED:**
• .claude/skills/{project-name}.skill.md - Your project-specific skill file
• docs/CLAUDE/USER-MANUAL.md - Your customized user manual
• .claude/initialization-state.json - Tracks installation for reinstall/uninstall

[If personas will be created, also list:]
• .claude/commands/personas/{domain}/{persona1}.md
• .claude/skills/personas/{domain}/{persona1}.persona.md
• .claude/commands/personas/{domain}/{persona2}.md
• .claude/skills/personas/{domain}/{persona2}.persona.md
• .claude/commands/review-{domain}-decision.md

**May be DELETED (optional):**
• .claude/skills/project-name.skill.md.template - Template no longer needed
```

```json
{
  "questions": [
    {
      "question": "Authorize all file operations listed above?",
      "header": "Authorize",
      "multiSelect": false,
      "options": [
        {
          "label": "Yes, authorize all (Recommended)",
          "description": "Proceed with all file operations without individual prompts"
        },
        {
          "label": "Authorize one-by-one",
          "description": "I want to approve each file operation individually"
        },
        {
          "label": "Cancel",
          "description": "Don't make any changes"
        }
      ]
    }
  ]
}
```

**If "Yes, authorize all":**
- Inform user: "Proceeding with authorized operations..."
- **CRITICAL - Batch file operations to minimize prompts:**
  1. Execute all Write/Edit operations in a SINGLE tool response (parallel tool calls)
  2. Group related files together (e.g., all persona files in one batch)
  3. Do NOT wait for individual confirmations between writes
- The user has pre-authorized these specific operations

**Implementation pattern for batched writes:**
```
In a single response, call multiple Write tools in parallel:
- Write tool: CLAUDE.md
- Write tool: .claude/skills/{project-name}.skill.md
- Write tool: docs/CLAUDE/USER-MANUAL.md
- Write tool: .claude/initialization-state.json
(All in the same message = single permission prompt for the batch)
```

**If "Authorize one-by-one":**
- Proceed normally (user will see individual permission dialogs)

**If "Cancel":**
- Exit without changes

### Step 4.1: Propose Placeholder Values

Based on confirmed understanding, propose values:

```
## Step 3 of 7: Configuration

Based on your project, I suggest these values:

**For CLAUDE.md:**
| Placeholder | Suggested Value |
|-------------|-----------------|
| {{PROJECT_NAME}} | [detected name] |
| {{PROJECT_DESCRIPTION}} | [from understanding] |
| {{VERSION}} | 1.0.0 |
| {{LAST_UPDATED}} | [today's date] |
| {{TECH_STACK_BACKEND}} | [detected] |
| {{TECH_STACK_FRONTEND}} | [detected or N/A] |
| {{TECH_STACK_DATABASE}} | [detected or N/A] |
| {{BUILD_COMMAND}} | [detected or suggested] |
| {{TEST_COMMAND}} | [detected or suggested] |
| {{MIGRATION_COMMAND}} | [detected or N/A] |

**For Project Skill (.claude/skills/{project-kebab}.skill.md):**
• File will be created from template
• Includes your tech stack and project structure
• Contains space for locked architectural decisions
```

```json
{
  "questions": [
    {
      "question": "Apply these configuration values?",
      "header": "Config",
      "multiSelect": false,
      "options": [
        {
          "label": "Apply all",
          "description": "Update CLAUDE.md and create project skill with these values"
        },
        {
          "label": "Modify first",
          "description": "Let me specify changes before applying"
        },
        {
          "label": "Skip config",
          "description": "Keep placeholder values, I'll update manually later"
        }
      ]
    }
  ]
}
```

### Step 4.2: Apply Configuration

**If "Apply all" or after modifications confirmed:**

1. **Update CLAUDE.md:**
   - Read `CLAUDE.md`
   - Replace each `{{PLACEHOLDER}}` with confirmed value
   - Write updated file

2. **Create Project Skill:**
   - Read `.claude/skills/project-name.skill.md.template`
   - Replace placeholders:
     - `{{project-name}}` → kebab-case project name
     - `{{PROJECT_NAME}}` → display name
     - `{{PROJECT_DESCRIPTION}}` → description
     - `{{BUILD_COMMAND}}`, `{{TEST_COMMAND}}`, `{{MIGRATION_COMMAND}}`
     - Technology stack table
     - Project structure diagram (based on detected structure)
   - Write to `.claude/skills/{project-name}.skill.md`
   - Delete the template file (or keep if user prefers)

3. **Update state to `core_complete`:**
   - Update `.claude/initialization-state.json`:
     - Set `"status": "core_complete"`
     - Add created files to `filesCreated` array

4. **Report completion:**
   ```
   ✓ Updated CLAUDE.md with project configuration
   ✓ Created .claude/skills/{project-name}.skill.md
   ```

**If "Skip config":** Note that user will update manually, proceed to Phase 5.

**State file after Phase 4:**
```json
{
  "status": "core_complete",
  "filesCreated": [
    ".claude/skills/[project-name].skill.md"
  ],
  ...
}
```

---

## Phase 5: Propose (Optional)

**Skip this phase if user selected "Quick Setup" in Phase 1.**

### Step 5.1: Generate Persona Suggestions

Based on confirmed domain, suggest 2-4 custom personas:

| Domain | Suggested Personas |
|--------|-------------------|
| Healthcare | Compliance Officer, Clinical Advisor, Patient Advocate, Data Privacy |
| Fintech | Risk Analyst, Compliance Officer, Security Auditor, Fraud Specialist |
| E-commerce | Customer Experience, Inventory Specialist, Payment Security, Fulfillment |
| SaaS B2B | Customer Success, Enterprise Sales, Integration Architect, Onboarding |
| Gaming | Player Experience, Monetization Analyst, Community Manager, QA Lead |
| EdTech | Curriculum Designer, Accessibility Expert, Learning Scientist, Student Advocate |
| DevTools | Developer Experience, API Designer, Documentation, Performance |
| IoT | Hardware Integration, Security, Reliability, Power Management |

### Step 5.2: Present Proposals

```
## Step 4 of 7: Custom Personas (Optional)

Based on your [domain] domain, I recommend adding these personas:

| Persona | Purpose |
|---------|---------|
| [Name 1] | [Brief mandate] |
| [Name 2] | [Brief mandate] |
| [Name 3] | [Brief mandate] |

These would complement the existing Product, Research, and Advisory packages.
```

```json
{
  "questions": [
    {
      "question": "Would you like to create these custom personas?",
      "header": "Personas",
      "multiSelect": true,
      "options": [
        {
          "label": "[Persona 1 Name]",
          "description": "[What this persona evaluates]"
        },
        {
          "label": "[Persona 2 Name]",
          "description": "[What this persona evaluates]"
        },
        {
          "label": "[Persona 3 Name]",
          "description": "[What this persona evaluates]"
        },
        {
          "label": "Skip all",
          "description": "Don't create any custom personas"
        }
      ]
    }
  ]
}
```

---

## Phase 6: Build (If Personas Accepted)

**Skip if no personas selected.**

### Step 6.1: Create Persona Files

**CRITICAL - Batch all persona file creation into a SINGLE tool response:**

Read all templates first (these don't require permission):
1. Read `.claude/templates/onboarding/persona-command.template.md`
2. Read `.claude/templates/onboarding/persona-skill.template.md`
3. Read `.claude/templates/onboarding/review-orchestrator.template.md`

Then execute ALL writes in parallel (single permission prompt):
```
In a single response, call multiple Write tools:
- Write: .claude/commands/personas/[domain]/[persona1].md
- Write: .claude/skills/personas/[domain]/[persona1].persona.md
- Write: .claude/commands/personas/[domain]/[persona2].md
- Write: .claude/skills/personas/[domain]/[persona2].persona.md
- Write: .claude/commands/personas/[domain]/[persona3].md
- Write: .claude/skills/personas/[domain]/[persona3].persona.md
- Write: .claude/commands/review-[domain]-decision.md
(All in same message = single permission prompt)
```

For each persona, use templates:

**Command file:** `.claude/commands/personas/[domain]/[persona-kebab].md`
- Use `persona-command.template.md`
- Replace placeholders with persona-specific content

**Skill file:** `.claude/skills/personas/[domain]/[persona-kebab].persona.md`
- Use `persona-skill.template.md`
- Include domain-specific evaluation frameworks

### Step 6.2: Create Review Orchestrator

Create `.claude/commands/review-[domain]-decision.md`:
- Use `review-orchestrator.template.md`
- Include all selected personas in the sequence
- Define contextual weighting

### Step 6.3: Update State to `personas_complete`

After persona files are successfully written:

1. **Update `.claude/initialization-state.json`:**
   - Set `"status": "personas_complete"`
   - Add all persona files to `personasCreated` array
   - Clear `pendingPersonas` array

**State file after Phase 6:**
```json
{
  "status": "personas_complete",
  "filesCreated": [
    ".claude/skills/[project-name].skill.md"
  ],
  "personasCreated": [
    ".claude/commands/personas/[domain]/[persona1].md",
    ".claude/skills/personas/[domain]/[persona1].persona.md",
    ".claude/commands/personas/[domain]/[persona2].md",
    ".claude/skills/personas/[domain]/[persona2].persona.md",
    ".claude/commands/review-[domain]-decision.md"
  ],
  "pendingPersonas": [],
  ...
}
```

### Step 6.4: Report Progress

```
## Step 5 of 7: Creating Personas

✓ Created .claude/commands/personas/[domain]/[persona1].md
✓ Created .claude/skills/personas/[domain]/[persona1].persona.md
✓ Created .claude/commands/personas/[domain]/[persona2].md
✓ Created .claude/skills/personas/[domain]/[persona2].persona.md
✓ Created .claude/commands/review-[domain]-decision.md
```

---

## Phase 7: Complete

### Step 7.1: Generate User Manual

Create `docs/CLAUDE/USER-MANUAL.md` using `.claude/templates/onboarding/user-manual.template.md`:
- Include project profile from Phase 3
- Include custom commands from Phase 6 (if any)
- Add domain-specific examples

### Step 7.2: Finalize State to `complete`

Update `.claude/initialization-state.json` to mark installation as complete:

1. **Update status and timestamp:**
   - Set `"status": "complete"`
   - Set `"completedAt": "[ISO 8601 timestamp]"`

2. **Add user manual to filesCreated:**
   - Append `"docs/CLAUDE/USER-MANUAL.md"` to `filesCreated` array

**Final state file:**
```json
{
  "status": "complete",
  "startedAt": "[ISO 8601 timestamp]",
  "completedAt": "[ISO 8601 timestamp]",
  "version": "1.0.0",
  "projectName": "[Display Name]",
  "projectNameKebab": "[kebab-case-name]",
  "domain": "[detected or selected domain]",
  "setupMode": "[full|quick]",
  "config": {
    "backend": "[tech]",
    "frontend": "[tech or null]",
    "database": "[tech or null]",
    "buildCommand": "[command]",
    "testCommand": "[command]",
    "migrationCommand": "[command or null]"
  },
  "filesCreated": [
    ".claude/skills/[project-name].skill.md",
    "docs/CLAUDE/USER-MANUAL.md"
  ],
  "personasCreated": [
    ".claude/commands/personas/[domain]/[persona1].md",
    ".claude/skills/personas/[domain]/[persona1].persona.md"
  ],
  "pendingPersonas": []
}
```

**Include the state update in the batched writes** along with the user manual.

### Step 7.3: Present Completion Summary

```
## Setup Complete! ✓

**Files Created/Updated:**
• CLAUDE.md - Updated with your project details
• .claude/skills/{project-name}.skill.md - Your project skill
• docs/CLAUDE/USER-MANUAL.md - Your customized user manual
[If personas created:]
• .claude/commands/personas/[domain]/ - Custom persona commands
• .claude/skills/personas/[domain]/ - Custom persona skills
• .claude/commands/review-[domain]-decision.md - Domain review orchestrator

**Next Steps:**
1. Review your project skill: `.claude/skills/{project-name}.skill.md`
   - Add locked architectural decisions that shouldn't be re-litigated
2. Review `docs/CLAUDE/DEVELOPMENT.md`
   - Add your coding patterns and lessons learned
3. Try a decision review: `/review-product-decision [your question]`

**Useful Commands:**
• `/review-product-decision` - Evaluate implementation decisions
• `/review-research` - Analyze research and sources
• `/review-business-decision` - Strategic business analysis
[If personas created:]
• `/review-[domain]-decision` - Your custom domain review
```

```json
{
  "questions": [
    {
      "question": "Would you like to do anything else?",
      "header": "Done",
      "multiSelect": false,
      "options": [
        {
          "label": "Open project skill",
          "description": "View the generated project skill file to add locked decisions"
        },
        {
          "label": "Open user manual",
          "description": "View your customized user manual"
        },
        {
          "label": "All done",
          "description": "Exit the setup wizard"
        }
      ]
    }
  ]
}
```

---

## Error Handling

### No Existing Context Found

If no user files are found outside the starter kit:

```json
{
  "questions": [
    {
      "question": "No existing project files found. How would you like to proceed?",
      "header": "No Files",
      "multiSelect": false,
      "options": [
        {
          "label": "Manual setup",
          "description": "I'll describe my project and you configure the starter kit"
        },
        {
          "label": "Add files first",
          "description": "Exit so I can add my project files, then run again"
        },
        {
          "label": "Cancel",
          "description": "Exit without changes"
        }
      ]
    }
  ]
}
```

### Unable to Determine Domain

If domain is unclear from the code:

```json
{
  "questions": [
    {
      "question": "What domain best describes your project?",
      "header": "Domain",
      "multiSelect": false,
      "options": [
        {
          "label": "Healthcare/Medical",
          "description": "Patient data, clinical workflows, HIPAA compliance"
        },
        {
          "label": "Fintech/Banking",
          "description": "Payments, trading, financial regulations"
        },
        {
          "label": "E-commerce/Retail",
          "description": "Shopping, inventory, fulfillment"
        },
        {
          "label": "SaaS/B2B",
          "description": "Business software, multi-tenant, subscriptions"
        }
      ]
    }
  ]
}
```

(Present additional domain options if none of these fit, or allow "Other" input)

---

## Recovery

If the user needs to restart or gets stuck:

```
To restart: `/INITIALIZE_STARTER_KIT`
For help: Check `.claude/CREATING-COMMANDS.md` and `.claude/CREATING-SKILLS.md`
```

---

## Uninstall Flow

**Triggered from Phase 0 when user selects "Uninstall" or "Full reset".**

### Step U.1: Show Files to Remove

Read `.claude/initialization-state.json` and present:

```
## Uninstall: Files to be Removed

**Will be DELETED:**
• .claude/skills/[project-name].skill.md
• docs/CLAUDE/USER-MANUAL.md
• .claude/initialization-state.json
[For each persona in personasCreated:]
• [persona file path]

**Will NOT be changed:**
• CLAUDE.md - You will need to manually restore placeholders if desired
• Pre-built personas (advisory, product, research packages)
• All starter kit template files
```

### Step U.2: Confirm (Skip if "Full reset")

```json
{
  "questions": [
    {
      "question": "Proceed with uninstallation?",
      "header": "Confirm",
      "multiSelect": false,
      "options": [
        {
          "label": "Yes, uninstall all",
          "description": "Remove all generated files listed above"
        },
        {
          "label": "Keep custom personas",
          "description": "Only remove core files, preserve persona files"
        },
        {
          "label": "Cancel",
          "description": "Exit without making any changes"
        }
      ]
    }
  ]
}
```

### Step U.3: Execute Deletion

**CRITICAL - Batch all deletions into a SINGLE tool response:**

```
In a single response, execute parallel Bash rm commands:
- rm .claude/skills/[project-name].skill.md
- rm docs/CLAUDE/USER-MANUAL.md
- rm .claude/initialization-state.json
[If deleting personas:]
- rm -r .claude/commands/personas/[domain]/
- rm -r .claude/skills/personas/[domain]/
- rm .claude/commands/review-[domain]-decision.md
```

### Step U.4: Report Completion

```
## Uninstall Complete

**Removed:**
• [list of deleted files]

**Note:** CLAUDE.md still contains your project-specific values.
To restore placeholders, manually edit CLAUDE.md or copy from a fresh starter kit.

To reinstall: `/INITIALIZE_STARTER_KIT`
```

---

## Update Config Flow

**Triggered from Phase 0 when user selects "Update configuration".**

### Step C.1: Read Current Configuration

Read `.claude/initialization-state.json` to get current values.

### Step C.2: Present Current Values

```
## Update Configuration

**Current values:**
| Setting | Current Value |
|---------|---------------|
| Project Name | [projectName] |
| Backend | [config.backend] |
| Frontend | [config.frontend] |
| Database | [config.database] |
| Build Command | [config.buildCommand] |
| Test Command | [config.testCommand] |
| Migration Command | [config.migrationCommand] |
```

```json
{
  "questions": [
    {
      "question": "Which settings would you like to update?",
      "header": "Update",
      "multiSelect": true,
      "options": [
        {
          "label": "Project Name",
          "description": "Currently: [projectName]"
        },
        {
          "label": "Tech Stack",
          "description": "Backend, frontend, database technologies"
        },
        {
          "label": "Commands",
          "description": "Build, test, and migration commands"
        },
        {
          "label": "All settings",
          "description": "Update all configuration values"
        }
      ]
    }
  ]
}
```

### Step C.3: Prompt for New Values

For each selected category, ask for new values. Use text input or present common options.

### Step C.4: Apply Updates

1. Update `CLAUDE.md` with new placeholder values
2. Update `.claude/skills/[project-name].skill.md` with new values
3. Update `.claude/initialization-state.json` with new config
4. If project name changed:
   - Rename skill file to new kebab-case name
   - Update filesCreated array in state

### Step C.5: Report Completion

```
## Configuration Updated

**Changed:**
• [list of updated settings]

**Files modified:**
• CLAUDE.md
• .claude/skills/[project-name].skill.md
• .claude/initialization-state.json
```
