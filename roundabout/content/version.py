"""
VERSION — which build is this? (mechanics.md — Parser Verbs; operations.md).

A built .exe carries content/_version.py, written by build_exe.py from
`git describe --tags --dirty` and never committed. Run from source, the game
asks git directly. Either way the answer is the git tag the game was built
from, e.g. v2.2-roundabout, or v2.2-roundabout-2-g516dfc1 for a build two
commits past it ("-dirty" if there were uncommitted changes).
"""

from __future__ import annotations
import os
import subprocess

TITLE = "Roundabout: The God-Forsaken Ring"


def git_version() -> str | None:
    """The tag description of the source tree, or None without git."""
    try:
        out = subprocess.run(
            ["git", "describe", "--tags", "--dirty", "--always"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True, text=True, timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return out.stdout.strip() or None


def version() -> str:
    try:
        from content._version import VERSION      # stamped into a built .exe
        return VERSION
    except ImportError:
        return git_version() or "unknown version"


def line() -> str:
    return f"{TITLE} — {version()}"
