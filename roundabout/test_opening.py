"""
The opening's pauses (npcs.md — Will Passion, Pauses): two stops, each with
a visible cue, and no silent waits.
Run with: pytest roundabout/test_opening.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world

_CUE = "[Press ENTER to continue] "


def _run_opening():
    from content.char_create import run_opening
    w, g = _make_world()
    prompts = []

    def _input(prompt=""):
        prompts.append(prompt)
        p = prompt.lower()
        if "adventure" in p:
            return "yes"
        if "warrior/mage/rogue" in p:
            return "warrior"
        if "your name" in p:
            return "Tess"
        return ""

    buf = io.StringIO()
    with patch("content.char_create.input", _input), patch("sys.stdout", buf):
        run_opening(w, g)
    return w, prompts, buf.getvalue()


def test_two_pauses_with_cue_and_no_silent_waits():
    w, prompts, out = _run_opening()
    assert "" not in prompts                       # every wait shows something
    assert prompts.count(_CUE) == 2
    assert [p for p in prompts if p != _CUE] == [
        '"Are you up for an adventure?" (yes/no) ',
        "Your choice (warrior/mage/rogue): ",
        '"And your name?" ',
    ]


def test_pause_order():
    _w, prompts, _out = _run_opening()
    assert prompts == [
        '"Are you up for an adventure?" (yes/no) ',
        _CUE,                                      # after "Then we begin"
        "Your choice (warrior/mage/rogue): ",
        '"And your name?" ',
        _CUE,                                      # after the ring briefing
    ]


def test_opening_still_sets_up_the_player():
    w, _prompts, out = _run_opening()
    assert w.globals["player_name"] == "Tess"
    assert w.globals["player_class"] == "warrior"
    assert w.globals["zenni"] >= 10
    assert out.rstrip().endswith("The conversation, it seems, is over.")
