#!/usr/bin/env python3
"""
Cross-platform utilities for Claude Code hooks.

Provides:
- .env file loading (required, fails if missing)
- Cross-platform path handling using pathlib
- Platform-agnostic temp directory access
- Debug logging support

Usage:
    from utils import get_project_dir, get_temp_dir, debug_log
"""

import os
import sys
import tempfile
from pathlib import Path
from typing import Dict, Optional

# Determine project root from script location
# .claude/hooks/utils.py -> .claude/hooks -> .claude -> project root
HOOKS_DIR = Path(__file__).parent.resolve()
CLAUDE_DIR = HOOKS_DIR.parent
PROJECT_ROOT = CLAUDE_DIR.parent


def load_dotenv() -> Dict[str, str]:
    """
    Load environment variables from .env file.

    The .env file is REQUIRED. If it doesn't exist, prints an error
    message and exits with code 1.

    Returns:
        Dict of variables that were loaded from .env
    """
    env_file = PROJECT_ROOT / '.env'
    loaded: Dict[str, str] = {}

    if not env_file.exists():
        print(f"ERROR: .env file not found at {env_file}", file=sys.stderr)
        print("", file=sys.stderr)
        print("To fix this:", file=sys.stderr)
        print(f"  1. Copy .env.example to .env:", file=sys.stderr)
        print(f"     cp {PROJECT_ROOT / '.env.example'} {env_file}", file=sys.stderr)
        print(f"  2. Edit .env and set CLAUDE_PROJECT_DIR to your project path", file=sys.stderr)
        sys.exit(1)

    with open(env_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            # Parse KEY=value
            if '=' not in line:
                continue

            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()

            # Remove surrounding quotes if present
            if len(value) >= 2:
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]

            # Set in environment (overwrites existing)
            if key:
                os.environ[key] = value
                loaded[key] = value

    return loaded


def get_project_dir() -> Path:
    """
    Get project directory from CLAUDE_PROJECT_DIR environment variable.

    Returns:
        Path to project root

    Raises:
        SystemExit if CLAUDE_PROJECT_DIR is not set
    """
    env_dir = os.environ.get('CLAUDE_PROJECT_DIR')
    if not env_dir:
        print("ERROR: CLAUDE_PROJECT_DIR environment variable is not set", file=sys.stderr)
        print("", file=sys.stderr)
        print("Set it in your .env file:", file=sys.stderr)
        print("  CLAUDE_PROJECT_DIR=/path/to/your/project", file=sys.stderr)
        sys.exit(1)

    return Path(env_dir).resolve()


def get_temp_dir() -> Path:
    """
    Get temporary directory for hook state files.

    Prefers CLAUDE_TEMP_DIR environment variable if set,
    otherwise uses the platform's default temp directory.

    Returns:
        Path to temp directory (created if doesn't exist)
    """
    env_temp = os.environ.get('CLAUDE_TEMP_DIR')
    if env_temp:
        temp_path = Path(env_temp)
        temp_path.mkdir(parents=True, exist_ok=True)
        return temp_path

    return Path(tempfile.gettempdir())


def get_python_path() -> str:
    """
    Get Python interpreter path.

    Prefers CLAUDE_PYTHON_PATH environment variable if set,
    otherwise returns the current Python executable.

    Returns:
        Path to Python interpreter
    """
    return os.environ.get('CLAUDE_PYTHON_PATH', sys.executable)


def is_debug_enabled() -> bool:
    """
    Check if hook debugging is enabled via CLAUDE_HOOK_DEBUG.

    Returns:
        True if debugging is enabled
    """
    value = os.environ.get('CLAUDE_HOOK_DEBUG', '').lower()
    return value in ('true', '1', 'yes')


def debug_log(message: str) -> None:
    """
    Print debug message to stderr if debugging is enabled.

    Args:
        message: Debug message to print
    """
    if is_debug_enabled():
        print(f"[HOOK DEBUG] {message}", file=sys.stderr)


def get_hook_timeout(default: int = 300) -> int:
    """
    Get hook timeout from CLAUDE_HOOK_PLAN_GATE_TIMEOUT.

    Args:
        default: Default timeout in seconds

    Returns:
        Timeout in seconds
    """
    try:
        return int(os.environ.get('CLAUDE_HOOK_PLAN_GATE_TIMEOUT', default))
    except ValueError:
        return default


# Auto-load .env when module is imported
_loaded_vars = load_dotenv()

# Log what was loaded if debugging
if _loaded_vars:
    debug_log(f"Loaded {len(_loaded_vars)} variables from .env: {list(_loaded_vars.keys())}")
