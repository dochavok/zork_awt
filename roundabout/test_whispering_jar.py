"""
The Whispering Jar, Quest 4 (items.md — The Whispering Jar, Silver Dust;
quests.md — Quest 4). The walkthrough plays it once, in order; these check the
letters before the dust, the failed read, and the in-between room and examine
lines (2026-10-15, TODO #19).

Expected text is the design's, written out here (or text constants pinned to
the design by test_design_text.py).
Run with: pytest roundabout/test_whispering_jar.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do
from content import quests
from content.whispering_jar import (_UNREADABLE, _WORN, _WHISPER, _SEALED, _SEALED_EXAMINE,
                                    _DUSTED, _DUSTED_EXAMINE)

UNTOUCHED = "A cracked ceramic jar sits on the side table, humming faintly to itself."
MENDED = "A mended ceramic jar sits on the side table, quiet."


def _pipe_room(seal=True, dust=True):
    w, g = _make_world(cls="warrior", level=5)
    w.move_object(w.player, w.rooms["PIPE-ROOM"])
    w.here = w.rooms["PIPE-ROOM"]
    for name, wanted in (("WAX-SEAL", seal), ("SILVER-DUST", dust)):
        if wanted:
            obj = w.objects[name]
            obj.clear_flag("INVISIBLE")
            w.move_object(obj, w.player)
    return w, g


def _read(g, passed=True):
    with patch("content.player.check_perception", return_value=passed) as roll:
        return _do(g, "read jar"), roll


def test_letters_unreadable_before_the_dust_with_no_roll():
    w, g = _pipe_room()
    for step in (None, "press seal on jar"):          # untouched, then sealed
        if step:
            _do(g, step)
        out, roll = _read(g)
        assert _UNREADABLE in out
        assert "Hold what was heard" not in out
        assert not roll.called
    assert not quests.is_complete(w, "4")


def test_dusted_jar_reads_and_whispers():
    w, g = _pipe_room()
    _do(g, "press seal on jar")
    _do(g, "dust jar")
    out, roll = _read(g)
    assert _WHISPER in out and roll.called
    assert quests.is_complete(w, "4")


def test_failed_read_once_dusted():
    w, g = _pipe_room()
    _do(g, "press seal on jar")
    _do(g, "dust jar")
    out, _ = _read(g, passed=False)
    assert _WORN in out
    assert _WHISPER not in out
    assert not quests.is_complete(w, "4")
    out, _ = _read(g)                                  # every read rolls again
    assert _WHISPER in out


def test_room_and_examine_follow_each_step():
    w, g = _pipe_room()
    assert UNTOUCHED in _do(g, "look")
    _do(g, "press seal on jar")
    assert _SEALED in _do(g, "look")
    assert _SEALED_EXAMINE in _do(g, "examine jar")
    _do(g, "dust jar")
    assert _DUSTED in _do(g, "look")
    assert _DUSTED_EXAMINE in _do(g, "examine jar")
    _read(g)
    assert MENDED in _do(g, "look")


def test_silver_dust_examine_leans_toward_the_letters():
    w, g = _pipe_room(seal=False)
    assert "every line stands out" in _do(g, "examine dust")


def test_may_names_the_pipe_room():
    from content.may_hints import _Q4
    assert _Q4.startswith("That jar in the pipe room, east off the main room")
