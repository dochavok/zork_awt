"""
Underground scenery (TODO #15, 2026-10-14; locations.md under each room): the
rubble, the Encampment's journals, bedrolls and equipment (and "journal" there
meaning them), the Rat's Nest crates, the Chuckle House Entrance's stool,
runner and ceiling, the Ghost's Room mirrors by visibility, and the
part-cleared timbers.
Run with: pytest roundabout/test_underground_scenery.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do
from content.scenery import (RUBBLE, RUBBLE_SEARCH, RUBBLE_CLIMB, JOURNALS, JOURNALS_STAY,
                             BEDROLLS, EQUIPMENT, CRATES, CRATES_SEARCH, STOOL, RUNNER,
                             ENTRANCE_CEILING, MIRRORS_SEEN, MIRRORS_UNSEEN, MIRRORS_FREED,
                             MIRROR_BREAK, MIRROR_TOUCH)
from content.aqueduct import _TIMBERS, _TIMBERS_LEFT, _NO_TIMBERS


def _say(room, command, **globals_):
    w, g, _ = _look(room, **globals_)
    return w, _do(g, command)


@pytest.mark.parametrize("room, command, text", [
    ("PILE-OF-RUBBLE", "examine rubble", RUBBLE),
    ("PILE-OF-RUBBLE", "search rubble", RUBBLE_SEARCH),
    ("PILE-OF-RUBBLE", "dig rubble", RUBBLE_SEARCH),
    ("PILE-OF-RUBBLE", "move rubble", RUBBLE_SEARCH),
    ("PILE-OF-RUBBLE", "climb rubble", RUBBLE_CLIMB),
    ("LOWER-ENCAMPMENT", "read journals", JOURNALS),
    ("LOWER-ENCAMPMENT", "examine journals", JOURNALS),
    ("LOWER-ENCAMPMENT", "take journals", JOURNALS_STAY),
    ("LOWER-ENCAMPMENT", "examine bedrolls", BEDROLLS),
    ("LOWER-ENCAMPMENT", "examine equipment", EQUIPMENT),
    ("LOWER-ENCAMPMENT", "search equipment", EQUIPMENT),
    ("RATS-NEST", "examine crates", CRATES),
    ("RATS-NEST", "examine barrels", CRATES),
    ("RATS-NEST", "search barrels", CRATES_SEARCH),
    ("RATS-NEST", "open crate", CRATES_SEARCH),
    ("CHUCKLE-ENTRANCE", "examine stool", STOOL),
    ("CHUCKLE-ENTRANCE", "examine runner", RUNNER),
    ("CHUCKLE-ENTRANCE", "examine pattern", RUNNER),
    ("CHUCKLE-ENTRANCE", "examine ceiling", ENTRANCE_CEILING),
    ("CHUCKLE-ENTRANCE", "look up", ENTRANCE_CEILING),
    ("GHOSTS-ROOM", "break mirror", MIRROR_BREAK),
    ("GHOSTS-ROOM", "touch mirror", MIRROR_TOUCH),
])
def test_scenery(room, command, text):
    _, out = _say(room, command)
    assert text in out


@pytest.mark.parametrize("held", [False, True])
@pytest.mark.parametrize("command", ["examine journal", "read journal", "read the journal",
                                     "x journal"])
def test_journal_in_the_encampment_means_the_camps(command, held):
    w, g, _ = _look("LOWER-ENCAMPMENT")
    if held:
        tip = w.objects["TIP-JOURNAL"]
        tip.flags.discard("INVISIBLE")
        w.move_object(tip, w.player)
    out = _do(g, command)
    assert JOURNALS in out
    assert "You don't have a journal." not in out and "Which journal" not in out


def test_tip_journal_is_still_the_players():
    w, g, _ = _look("LOWER-ENCAMPMENT")
    tip = w.objects["TIP-JOURNAL"]
    tip.flags.discard("INVISIBLE")
    w.move_object(tip, w.player)
    assert JOURNALS not in _do(g, "read tip journal")


def test_read_journal_elsewhere_is_unchanged():
    _, out = _say("TOWN-SQUARE", "read journal")
    assert "You don't have a journal." in out


@pytest.mark.parametrize("command", ["examine mirrors", "examine mirror", "look in mirror",
                                     "examine reflection"])
def test_mirrors_by_visibility(command):
    _, out = _say("GHOSTS-ROOM", command)
    assert MIRRORS_SEEN in out
    w, g, _ = _look("GHOSTS-ROOM")
    w.globals["ring_worn"] = True
    assert MIRRORS_UNSEEN in _do(g, command)
    w, g, _ = _look("GHOSTS-ROOM", INKED=True)            # ink cancels the ring
    w.globals["ring_worn"] = True
    assert MIRRORS_SEEN in _do(g, command)
    _, out = _say("GHOSTS-ROOM", command, GHOST_FREED=True)
    assert MIRRORS_FREED in out


@pytest.mark.parametrize("down, text", [(0, _TIMBERS), (1, _TIMBERS_LEFT[0]),
                                        (2, _TIMBERS_LEFT[1]), (3, _NO_TIMBERS)])
def test_examine_timbers_follows_the_count(down, text):
    _, out = _say("COLLAPSED-GALLERY", "examine timbers", TIMBERS_DOWN=down)
    assert text in out
    assert "nothing special" not in out


# --- The Rejection Mirror and Shatter Trap Mirror; MY (2026-10-14) -------------------

from content.scenery import ROOM_MIRRORS


@pytest.mark.parametrize("room", list(ROOM_MIRRORS))
@pytest.mark.parametrize("command", ["examine mirror", "look in mirror", "examine frame",
                                     "examine reflection"])
def test_single_mirrors_by_visibility(room, command):
    seen, unseen, freed = ROOM_MIRRORS[room]
    _, out = _say(room, command)
    assert seen in out
    w, g, _ = _look(room)
    w.globals["ring_worn"] = True
    assert unseen in _do(g, command)
    w, g, _ = _look(room, INKED=True)
    w.globals["ring_worn"] = True
    assert seen in _do(g, command)
    _, out = _say(room, command, GHOST_FREED=True)
    assert freed in out


@pytest.mark.parametrize("room", list(ROOM_MIRRORS))
def test_single_mirrors_break_and_touch(room):
    _, out = _say(room, "break mirror")
    assert MIRROR_BREAK in out
    _, out = _say(room, "touch mirror")
    assert MIRROR_TOUCH in out


def _with_tip_journal(room):
    w, g, _ = _look(room)
    tip = w.objects["TIP-JOURNAL"]
    tip.flags.discard("INVISIBLE")
    w.move_object(tip, w.player)
    return w, g


@pytest.mark.parametrize("room", ["TOWN-SQUARE", "LOWER-ENCAMPMENT"])
def test_read_my_journal(room):
    w, g = _with_tip_journal(room)
    out = _do(g, "read my journal")
    assert "The journal is empty." in out
    assert JOURNALS not in out and "Which journal" not in out


def test_my_is_ignored_with_any_object():
    w, g = _with_tip_journal("TOWN-SQUARE")
    _do(g, "drop my journal")
    assert w.objects["TIP-JOURNAL"].location is w.here
    assert "You have" in _do(g, "count my zenni")
