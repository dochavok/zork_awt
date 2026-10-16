"""
Answering "Which X do you mean?" (mechanics.md — Answering "Which do you
mean?"; ZIL ORPHAN-MERGE). The next input, if every word fits one of the
offered objects, picks it and the asked command runs; anything else is a new
command.
Run with: pytest roundabout/test_which_answer.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do

ALL_THREE = ("Which scroll do you mean, the incantation scroll, the Fireball scroll, "
             "or the Light scroll?")
SPELLS_ONLY = "Which scroll do you mean, the Fireball scroll, or the Light scroll?"
MAGE_READS = "the words settle into you as if they had always meant to"


def _mage_with_scrolls():
    w, g = _make_world(cls="mage")
    for name in ("INCANTATION-SCROLL", "FIREBALL-SCROLL", "SCROLL-LIGHT"):
        obj = w.objects[name]
        obj.flags.discard("INVISIBLE")   # hidden until found in play
        w.move_object(obj, w.player)
    return w, g


@pytest.mark.parametrize("answer", ["fireball", "fireball scroll", "the fireball one"])
def test_answer_picks_the_scroll_and_runs_the_command(answer):
    w, g = _mage_with_scrolls()
    assert ALL_THREE in _do(g, "read scroll")
    out = _do(g, answer)
    assert MAGE_READS in out and "[Fireball spell learned.]" in out
    assert w.globals.get("spell_fireball")
    assert w.objects["INCANTATION-SCROLL"].location is w.player
    assert w.objects["SCROLL-LIGHT"].location is w.player


def test_answer_that_still_fits_several_asks_again():
    w, g = _mage_with_scrolls()
    _do(g, "read scroll")
    assert SPELLS_ONLY in _do(g, "spell")
    out = _do(g, "light")
    assert "[Light spell learned.]" in out
    assert w.globals.get("spell_light") and not w.globals.get("spell_fireball")


def test_answer_works_for_other_verbs():
    w, g = _mage_with_scrolls()
    _do(g, "drop scroll")
    assert "You drop the incantation scroll." in _do(g, "incantation")
    assert w.objects["INCANTATION-SCROLL"].location is w.here


@pytest.mark.parametrize("cmd,expect", [
    ("north", "Town Hall"),
    ("inventory", "You are carrying:"),
])
def test_a_new_command_is_not_an_answer(cmd, expect):
    w, g = _mage_with_scrolls()
    _do(g, "read scroll")
    out = _do(g, cmd)
    assert expect in out
    assert MAGE_READS not in out


def test_the_question_is_answered_only_once():
    w, g = _mage_with_scrolls()
    _do(g, "read scroll")
    _do(g, "fireball")
    assert "There was no verb in that sentence!" in _do(g, "fireball")   # a known word, not an answer


def test_the_question_lapses_after_another_command():
    w, g = _mage_with_scrolls()
    _do(g, "read scroll")
    _do(g, "inventory")
    out = _do(g, "fireball")
    assert MAGE_READS not in out
    assert not w.globals.get("spell_fireball")


FIREBALL_EXAMINE = "A spell scroll headed Fireball"


def test_again_repeats_the_answered_command():
    w, g = _mage_with_scrolls()
    _do(g, "examine scroll")
    assert FIREBALL_EXAMINE in _do(g, "fireball")
    out = _do(g, "again")
    assert FIREBALL_EXAMINE in out
    assert "Which scroll" not in out


def test_again_after_the_chosen_object_is_gone_asks_about_what_is_left():
    w, g = _mage_with_scrolls()
    _do(g, "read scroll")
    _do(g, "fireball")   # the Fireball scroll crumbles
    out = _do(g, "again")
    assert "Which scroll do you mean, the incantation scroll, or the Light scroll?" in out
    assert "[Light spell learned.]" in _do(g, "light")
