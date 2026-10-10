"""
The Still Den's descriptions (locations.md — The Still Den): first visit,
werewolf up, werewolf dead; the rising text once; EXAMINE WEREWOLF and
EXAMINE SCHOLAR. The werewolf is named whenever it's up, so the player knows
what the stake is for.

Expected text is the design's, written out here.
Run with: pytest roundabout/test_still_den.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from contextlib import contextmanager
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

_BASE = ("A wide cave, low but not cramped. The walls are gouged at every height — long "
         "parallel marks, overlapping, years of them. The floor is worn smooth in a rough "
         "oval, the path of something that has been pacing this space for longer than it "
         "can remember.")
FIRST = _BASE + (" Something lies curled at the far end of the oval, grey and motionless. "
                 "That changes the moment you enter.")
RISES = ("The grey shape unfolds from the floor: a werewolf, taller than a man, long in the "
         "arm, its fur gone patchy over skin that hasn't been alive in years. It turns its "
         "head toward you and starts forward.")
UP = ("A wide cave, low but not cramped, the walls gouged at every height. The werewolf "
      "paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive "
      "in years. It hasn't taken its eyes off you.")
DEAD = _BASE + (" Nothing paces it now. The scholar lies where the creature fell, the "
                "stake still in him.")
EXAMINE_WEREWOLF = ("A werewolf, long dead and still moving. Old wounds cross its chest — "
                    "blade cuts, arrow holes, burns — and every one of them has closed.")
EXAMINE_SCHOLAR = ("Just a man, thin and tired-looking, ink still worked into the creases "
                   "of his fingers. The stake is still in him. Whatever he came down here "
                   "to find, he found it.")
CLAWS = "The werewolf's claws find you."
NOTHING_SPECIAL = "nothing special"
OLD_STILL = "It is very still right now."          # the old alive text, now gone


def _pass(hearts=6):
    """At The Narrow Pass, torch lit, stake carried, the Still Den not yet seen."""
    from content import light
    w, g = _make_world(cls="warrior", hearts=hearts)
    w.move_object(w.objects["TORCH"], w.player)
    with patch("sys.stdout", io.StringIO()):
        light.light_torch(w)
    w.move_object(w.objects["SILVER-STAKE"], w.player)
    w.move_object(w.player, w.rooms["NARROW-PASS"])
    w.here = w.rooms["NARROW-PASS"]
    return w, g


@contextmanager
def _always_hit():
    """Every werewolf round lands: any round shows as CLAWS and a lost heart."""
    with patch("content.player.roll", return_value=1), \
         patch("content.combat._enemy_roll", return_value=30):
        yield


# --- First visit -----------------------------------------------------------------

def test_first_entry_describes_the_den_then_it_rises():
    w, g = _pass()
    with _always_hit():
        out = _do(g, "east")
    assert FIRST in out
    assert RISES in out
    assert out.index(FIRST) < out.index(RISES)
    assert UP not in out and OLD_STILL not in out
    assert CLAWS not in out                         # no round on the entry turn
    assert w.globals["hearts"] == 6


def test_the_rising_names_the_werewolf():
    assert "werewolf" in RISES and "werewolf" in UP


# --- Werewolf up ----------------------------------------------------------------

def test_look_after_it_rises_shows_it_up_and_is_a_round():
    w, g = _pass()
    _do(g, "east")
    with _always_hit():
        out = _do(g, "look")
    assert UP in out
    assert FIRST not in out and RISES not in out and OLD_STILL not in out
    assert CLAWS in out
    assert w.globals["hearts"] == 5


def test_return_visit_shows_it_up_in_brief_mode():
    from engine.game import BRIEF
    w, g = _pass()
    assert g.desc_mode == BRIEF
    _do(g, "east")
    _do(g, "west")
    with _always_hit():
        out = _do(g, "east")
    assert UP in out                                # full description despite BRIEF
    assert RISES not in out and FIRST not in out
    assert CLAWS not in out                         # entering is still free
    assert w.globals["hearts"] == 6


def test_every_return_visit_shows_it_up():
    w, g = _pass()
    _do(g, "east")
    for _ in range(3):
        _do(g, "west")
        assert UP in _do(g, "east")


def test_it_rises_only_once_even_leaving_at_once():
    w, g = _pass()
    out = _do(g, "east") + _do(g, "west") + _do(g, "east") + _do(g, "west") + _do(g, "east")
    assert out.count(RISES) == 1


def test_examine_werewolf():
    w, g = _pass()
    _do(g, "east")
    out = _do(g, "examine werewolf")
    assert EXAMINE_WEREWOLF in out
    assert NOTHING_SPECIAL not in out


def test_examine_werewolf_is_a_round():
    w, g = _pass()
    _do(g, "east")
    with _always_hit():
        out = _do(g, "examine werewolf")
    assert CLAWS in out
    assert w.globals["hearts"] == 5


def test_a_restored_game_remembers_it_has_risen(tmp_path):
    from engine import savegame
    w, g = _pass()
    _do(g, "east")
    path = str(tmp_path / "den.sav")
    savegame.save(g, path)
    w2, g2 = _make_world(cls="warrior")
    assert savegame.restore(g2, path)
    out = _do(g2, "look")
    assert UP in out and FIRST not in out


# --- Werewolf dead -------------------------------------------------------------

def _killed():
    w, g = _pass()
    w.set_global("STAKE-CONSECRATED", True)
    _do(g, "east")
    _do(g, "drive stake into werewolf")
    assert w.get_global("WEREWOLF-DEAD")
    return w, g


def test_look_after_the_kill():
    w, g = _killed()
    out = _do(g, "look")
    assert DEAD in out
    assert UP not in out and FIRST not in out
    assert CLAWS not in out


def test_examine_scholar_after_the_kill():
    w, g = _killed()
    out = _do(g, "examine scholar")
    assert EXAMINE_SCHOLAR in out
    assert NOTHING_SPECIAL not in out


def test_return_after_the_kill_follows_brief_mode():
    w, g = _killed()
    _do(g, "west")
    out = _do(g, "east")
    assert "The Still Den" in out
    assert DEAD not in out and UP not in out and RISES not in out
    assert DEAD in _do(g, "look")
