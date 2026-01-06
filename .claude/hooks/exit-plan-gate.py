#!/usr/bin/env python3
"""
PreToolUse hook for ExitPlanMode - enforces two-step plan approval workflow.

First call: Blocks and reminds Claude to present a plan summary.
Second call (within timeout): Allows the tool to proceed.

This ensures users can review the plan before the approval modal appears.

Environment variables (via .env):
    CLAUDE_HOOK_PLAN_GATE_TIMEOUT: Timeout in seconds (default: 300)
    CLAUDE_HOOK_DEBUG: Enable debug output (default: false)
"""

import json
import sys
import time
from pathlib import Path

# Import cross-platform utilities
# This also auto-loads .env file
from utils import get_temp_dir, get_hook_timeout, debug_log

# State file to track if reminder was shown (cross-platform temp directory)
STATE_FILE = get_temp_dir() / 'claude-plan-reminder-shown'
REMINDER_TIMEOUT_SECONDS = get_hook_timeout(default=300)


def main():
    debug_log(f"Plan gate hook triggered")
    debug_log(f"State file: {STATE_FILE}")
    debug_log(f"Timeout: {REMINDER_TIMEOUT_SECONDS} seconds")

    # Read tool input from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Hook error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    tool_name = input_data.get("tool_name", "")
    debug_log(f"Tool name: {tool_name}")

    # Only act on ExitPlanMode tool
    if tool_name != "ExitPlanMode":
        debug_log("Not ExitPlanMode, allowing")
        sys.exit(0)  # Allow other tools to proceed

    # Check if reminder was recently shown
    if STATE_FILE.exists():
        try:
            mtime = STATE_FILE.stat().st_mtime
            elapsed = time.time() - mtime
            debug_log(f"State file exists, age: {elapsed:.1f}s")

            if elapsed < REMINDER_TIMEOUT_SECONDS:
                # Reminder was shown recently - allow the call and reset state
                STATE_FILE.unlink()
                debug_log("Within timeout, allowing ExitPlanMode")
                sys.exit(0)
            else:
                debug_log("State file expired, will show reminder again")
        except OSError as e:
            debug_log(f"Error checking state file: {e}")
            pass  # File may have been deleted, treat as first call

    # First call or stale state - block and show reminder
    try:
        STATE_FILE.write_text(str(time.time()))
        debug_log("Created/updated state file, blocking exit")
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
