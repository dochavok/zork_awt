"""
Input ending, or Ctrl+C, at any prompt ends the game quietly; output is always
UTF-8 (mechanics.md — The end of the game; TODO #25, 2026-10-15).
Run with: pytest roundabout/test_end_of_input.py  (from c:\\zork_awt)
"""

import os
import subprocess
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.dirname(__file__))
_HERE = os.path.dirname(os.path.abspath(__file__))


def _play(text):
    """main.py with `text` piped in: (exit code, raw output bytes)."""
    run = subprocess.run([sys.executable, "main.py"], input=text.encode("utf-8"),
                         cwd=_HERE, capture_output=True, timeout=60)
    return run.returncode, run.stdout + run.stderr


@pytest.mark.parametrize("text", [
    "open mailbox\n",                           # at "Are you up for an adventure?"
    "open mailbox\nyes\n",                      # at the first [Press ENTER to continue]
    "open mailbox\nyes\n\nrogue\n",             # at "And your name?"
    "open mailbox\nyes\n\nrogue\nSable\n",      # at the second pause
    "open mailbox\nyes\n\n",                    # at the class question
])
def test_input_ending_at_a_prompt_ends_quietly(text):
    code, out = _play(text)
    assert code == 0
    assert b"Traceback" not in out and b"EOFError" not in out


def test_piped_output_is_utf8():
    code, out = _play("VERSION\n")
    assert code == 0
    assert "Roundabout: The God-Forsaken Ring — v".encode("utf-8") in out


def test_ctrl_c_at_a_prompt_ends_quietly(capsys):
    import main
    answers = iter(["open mailbox"])

    def fake_input(prompt=""):
        try:
            return next(answers)
        except StopIteration:
            raise KeyboardInterrupt
    with patch("builtins.input", fake_input):
        main.main()                              # returns: no traceback, no exception
    out = capsys.readouterr().out
    assert 'He pauses. "The object itself is another matter."' in out   # reached the question
