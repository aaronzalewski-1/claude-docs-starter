# Refresh Codebase Context

Regenerate and display a codebase summary for quick context loading at session start.

## Steps

1. **Analyze project structure:**
   - Count files by type (`.cs`, `.ts`, `.py`, `.go`, etc.)
   - List top-level directories and their purposes
   - Identify key configuration files

2. **Report summary:**
   - Project type (backend, frontend, full-stack, library)
   - Primary language and framework
   - File counts by extension
   - Key entry points (main files, API controllers, etc.)

3. **List recent changes:**
   ```bash
   git log --oneline -10
   ```

4. **Check for active work:**
   - Look for `docs/CLAUDE/SESSION-STATE.json`
   - Report any in-progress tasks or blockers

## Output Format

```markdown
## Codebase Summary

**Project:** {{PROJECT_NAME}}
**Type:** [backend | frontend | full-stack | library]
**Primary Stack:** [e.g., ASP.NET Core 8.0 + React 18]

### File Counts
| Extension | Count |
|-----------|-------|
| .cs       | X     |
| .ts       | X     |
| ...       | ...   |

### Key Directories
- `src/` - Application source code
- `tests/` - Test projects
- `docs/` - Documentation

### Recent Activity
[Last 5-10 commits]

### Active Work
[Contents of SESSION-STATE.json if exists, or "No active multi-session work"]
```

## When to Use

- **Session start**: Quick context loading without reading all documentation
- **After refactoring**: Verify file counts and structure changed as expected
- **Returning after break**: Catch up on recent commits and any in-progress work
- **Context limits**: When you need a lighter-weight summary than full doc loading

## Customization

For projects with build tools that generate summaries, you can add a script step:

```bash
# Example for projects with custom snapshot tools
{{SNAPSHOT_COMMAND}}
```

Then read the generated summary file instead of manual analysis.

## Notes

- This command provides a quick overview, not deep analysis
- For architectural understanding, use `/DEEPPLAN` with proper context loading
- For debugging context, use `/REFOCUS`
