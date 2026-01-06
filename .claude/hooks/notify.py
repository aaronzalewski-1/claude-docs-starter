#!/usr/bin/env python3
"""
Cross-platform notification utility for Claude Code hooks.

Sends desktop notifications using platform-appropriate methods:
- macOS: osascript (AppleScript)
- Linux: notify-send (libnotify)
- Windows: PowerShell toast notification

Usage:
    python notify.py "Your message"
    python notify.py "Your message" "Custom Title"

Environment variables (via .env):
    CLAUDE_HOOK_DEBUG: Enable debug output (default: false)
"""

import platform
import subprocess
import sys

# Import utilities for debug logging
try:
    from utils import debug_log, is_debug_enabled
except ImportError:
    # Fallback if run standalone without .env
    def debug_log(msg: str) -> None:
        pass
    def is_debug_enabled() -> bool:
        return False


def notify_macos(title: str, message: str) -> bool:
    """
    Send notification on macOS using osascript (AppleScript).

    Args:
        title: Notification title
        message: Notification body

    Returns:
        True if notification was sent successfully
    """
    try:
        # Escape quotes in message and title
        title_escaped = title.replace('"', '\\"')
        message_escaped = message.replace('"', '\\"')

        script = f'display notification "{message_escaped}" with title "{title_escaped}"'
        result = subprocess.run(
            ['osascript', '-e', script],
            check=True,
            capture_output=True,
            text=True
        )
        debug_log(f"macOS notification sent via osascript")
        return True
    except subprocess.CalledProcessError as e:
        debug_log(f"osascript failed: {e.stderr}")
        return False
    except FileNotFoundError:
        debug_log("osascript not found")
        return False


def notify_linux(title: str, message: str) -> bool:
    """
    Send notification on Linux using notify-send (libnotify).

    Requires libnotify-bin package on Debian/Ubuntu or libnotify on Fedora/Arch.

    Args:
        title: Notification title
        message: Notification body

    Returns:
        True if notification was sent successfully
    """
    try:
        result = subprocess.run(
            ['notify-send', title, message],
            check=True,
            capture_output=True,
            text=True
        )
        debug_log(f"Linux notification sent via notify-send")
        return True
    except subprocess.CalledProcessError as e:
        debug_log(f"notify-send failed: {e.stderr}")
        return False
    except FileNotFoundError:
        debug_log("notify-send not found - install libnotify-bin or libnotify")
        return False


def notify_windows(title: str, message: str) -> bool:
    """
    Send notification on Windows using PowerShell.

    Attempts Windows 10+ toast notification first, falls back to MessageBox.

    Args:
        title: Notification title
        message: Notification body

    Returns:
        True if notification was sent successfully
    """
    # Escape single quotes for PowerShell
    title_escaped = title.replace("'", "''")
    message_escaped = message.replace("'", "''")

    # Try Windows 10+ toast notification
    toast_script = f'''
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$template = @'
<toast>
    <visual>
        <binding template="ToastText02">
            <text id="1">{title_escaped}</text>
            <text id="2">{message_escaped}</text>
        </binding>
    </visual>
</toast>
'@
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml($template)
$toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Claude Code').Show($toast)
'''

    try:
        result = subprocess.run(
            ['powershell', '-NoProfile', '-Command', toast_script],
            check=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        debug_log("Windows toast notification sent")
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        debug_log(f"Toast notification failed: {e}, trying MessageBox fallback")

    # Fallback to simple MessageBox
    msgbox_script = f'''
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('{message_escaped}', '{title_escaped}', 'OK', 'Information')
'''

    try:
        result = subprocess.run(
            ['powershell', '-NoProfile', '-Command', msgbox_script],
            check=True,
            capture_output=True,
            text=True,
            timeout=30  # MessageBox waits for user interaction
        )
        debug_log("Windows MessageBox shown")
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        debug_log(f"MessageBox fallback failed: {e}")
        return False


def notify(title: str, message: str) -> bool:
    """
    Send notification using platform-appropriate method.

    Args:
        title: Notification title
        message: Notification body

    Returns:
        True if notification was sent successfully
    """
    system = platform.system()
    debug_log(f"Detected platform: {system}")

    if system == 'Darwin':
        return notify_macos(title, message)
    elif system == 'Linux':
        return notify_linux(title, message)
    elif system == 'Windows':
        return notify_windows(title, message)
    else:
        # Unknown platform - print to stderr as fallback
        print(f"[{title}] {message}", file=sys.stderr)
        debug_log(f"Unknown platform '{system}', printed to stderr")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: notify.py <message> [title]", file=sys.stderr)
        print("", file=sys.stderr)
        print("Examples:", file=sys.stderr)
        print('  python notify.py "Build completed"', file=sys.stderr)
        print('  python notify.py "Tests passed" "Claude Code"', file=sys.stderr)
        sys.exit(1)

    message = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "Claude Code"

    debug_log(f"Sending notification: title='{title}', message='{message}'")

    success = notify(title, message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
