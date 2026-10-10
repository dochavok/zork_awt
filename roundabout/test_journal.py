"""
The Tip Journal — READ JOURNAL (mechanics.md — Tip Journal; items.md — Tip Journal).
Run with: pytest roundabout/test_journal.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import quests

NONE = "You don't have a journal."
EMPTY = "The journal is empty."


def _world(carry=True):
    w, g = _make_world()
    w.globals["quest_states"] = {}
    w.globals["QUEST-LOG"] = []
    w.globals["HINT-LOG"] = []
    room = w.rooms["TOWN-SQUARE"]
    w.move_object(w.player, room)
    w.here = room
    if carry:
        w.move_object(w.objects["TIP-JOURNAL"], w.player)
    return w, g


def _lines(out):
    return out.rstrip("\n").split("\n")


def test_no_journal():
    w, g = _world(carry=False)
    assert _do(g, "read journal").strip() == NONE
    assert _do(g, "examine tip journal").strip() == NONE


def test_left_in_another_room():
    w, g = _world()
    w.move_object(w.objects["TIP-JOURNAL"], w.rooms["KITCHEN"])
    assert _do(g, "read journal").strip() == NONE


def test_on_the_floor_here_reads():
    w, g = _world()
    w.move_object(w.objects["TIP-JOURNAL"], w.here)
    assert _do(g, "read journal").strip() == EMPTY


def test_empty_until_something_is_discovered():
    w, g = _world()
    assert _do(g, "read journal").strip() == EMPTY
    assert _do(g, "examine journal").strip() == EMPTY


def test_discovery_order_tags_and_columns():
    w, g = _world()
    quests.discover(w, "7")                      # organic
    quests.discover(w, "22", "Board")
    quests.discover(w, "4")
    out = _do(g, "read journal")
    lines = _lines(out)
    assert lines[0] == "JOURNAL" and lines[1] == ""
    assert lines[2:] == [
        "The Bone Flute         [Organic]", "",      # the design's example layout
        "The Ruined Aqueduct    [Board]", "",
        "The Whispering Jar     [Organic]",
    ]
    assert "Quest" not in out and not any(c.isdigit() for c in out)   # no numbers


def test_reading_the_board_tags_board():
    w, g = _world()
    w.move_object(w.player, w.rooms["BAR"])
    w.here = w.rooms["BAR"]
    _do(g, "read board")
    out = _do(g, "read journal")
    assert "The Ruined Aqueduct" in out
    line = [l for l in _lines(out) if l.startswith("The Ruined Aqueduct")][0]
    assert line.endswith("[Board]")


def test_first_source_sticks():
    w, g = _world()
    quests.discover(w, "22")
    quests.discover(w, "22", "Board")
    assert "[Board]" not in _do(g, "read journal")


def test_may_hint_discovers_statue_and_warden():
    w, g = _world()
    w.move_object(w.player, w.rooms["BAR"])
    w.here = w.rooms["BAR"]
    w.globals["zenni"] = 10
    with patch("content.may_hints.random.randint", return_value=1):
        _do(g, "tip may 1")
    hint = w.globals["HINT-LOG"][0][2]
    lines = _lines(_do(g, "read journal"))
    statue = lines.index([l for l in lines if l.startswith("The Hollow Statue")][0])
    warden = lines.index([l for l in lines if l.startswith("The Undead Warden")][0])
    assert lines[statue].endswith("[May]") and lines[warden].endswith("[May]")
    assert lines[statue + 1] == f"  Tip: {hint}"
    assert lines[warden + 1] == f"  Tip: {hint}"


def test_hints_in_purchase_order_labelled_tip():
    w, g = _world()
    quests.discover(w, "17")
    w.globals["HINT-LOG"] = [("17", 1, "First."), ("22", 1, "Other."),
                             ("17", 2, "Second."), ("17", 1, "Next phase.")]
    assert _lines(_do(g, "read journal"))[2:] == [
        "The Frozen Watch    [Organic]",
        "  Tip: First.",
        "  Tip: Second.",
        "  Tip: Next phase.",
    ]
    assert "tier" not in _do(g, "read journal").lower()     # tiers stay hidden


def test_late_hint_shows_once_discovered():
    w, g = _world()
    w.globals["HINT-LOG"] = [("34", 1, "Late.")]
    assert _do(g, "read journal").strip() == EMPTY
    quests.discover(w, "34")
    assert "  Tip: Late." in _do(g, "read journal")


def test_completed_quests_drop_off():
    w, g = _world()
    quests.discover(w, "7")
    quests.discover(w, "22", "Board")
    quests.complete(w, "7")
    out = _do(g, "read journal")
    assert "The Bone Flute" not in out and "The Ruined Aqueduct" in out
    quests.complete(w, "22")
    assert _do(g, "read journal").strip() == EMPTY


def test_journal_weighs_nothing():
    w, _g = _world()
    assert w.objects["TIP-JOURNAL"].size == 0
