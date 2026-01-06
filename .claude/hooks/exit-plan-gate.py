#!/usr/bin/env python3
"""
PreToolUse hook for ExitPlanMode - enforces two-step plan approval workflow.

First call: Blocks and reminds Claude to present a plan summary.
Second call (within 5 min): Allows the tool to proceed.

This ensures users can review the plan before the approval modal appears.
"""

import json
import os
import sys
import time

# State file to track if reminder was shown (use temp directory for cross-platform)
STATE_FILE = os.path.join(os.environ.get('TEMP', '/tmp'), 'claude-plan-reminder-shown')
REMINDER_TIMEOUT_SECONDS = 300  # 5 minutes


def main():
    # Read tool input from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Hook error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    tool_name = input_data.get("tool_name", "")

    # Only act on ExitPlanMode tool
    if tool_name != "ExitPlanMode":
        sys.exit(0)  # Allow other tools to proceed

    # Check if reminder was recently shown
    if os.path.exists(STATE_FILE):
        try:
            mtime = os.path.getmtime(STATE_FILE)
            if time.time() - mtime < REMINDER_TIMEOUT_SECONDS:
                # Reminder was shown recently - allow the call and reset state
                os.remove(STATE_FILE)
                sys.exit(0)
        except OSError:
            pass  # File may have been deleted, treat as first call

    # First call or stale state - block and show reminder
    try:
        with open(STATE_FILE, 'w') as f:
            f.write(str(time.time()))
    except OSError as e:
        print(f"Hook warning: Could not write state file: {e}", file=sys.stderr)
        # Continue anyway - worst case is reminder shows every time

    # Return deny with helpful message to Claude
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "PLAN REVIEW REQUIRED: Before exiting plan mode, please present a clear "
                "summary of your plan to the user. Include:\n"
                "1. What you will implement\n"
                "2. Which files will be created or modified\n"
                "3. Any key decisions or tradeoffs\n\n"
                "After presenting the summary and receiving user confirmation, "
                "call ExitPlanMode again to proceed."
            )
        }
    }

    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
