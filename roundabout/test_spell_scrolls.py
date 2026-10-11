"""
Spell scrolls (mechanics.md — Spell training, Warrior/Rogue scroll resistance,
Mage reads a spell scroll; npcs.md — Will, spell teaching).

Every way of learning a spell names the spell it taught.
Run with: pytest roundabout/test_spell_scrolls.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

MAGE_READS = "the words settle into you as if they had always meant to"
RESISTANCE = "Will Passion, in his tower, has been known to translate"
TEACHING = "The knowing, I mean."

SCROLLS = [
    ("SCROLL-LIGHT", "spell_light", "[Light spell learned.]"),
    ("SCROLL-UNBIND-UNDEAD", "spell_unbind_undead", "[Unbind Undead spell learned.]"),
    ("FIREBALL-SCROLL", "spell_fireball", "[Fireball spell learned.]"),
]


def _at(room, cls, scroll):
    w, g = _make_world(cls=cls)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    obj = w.objects[scroll]
    obj.flags.discard("INVISIBLE")   # hidden until found in play
    w.move_object(obj, w.player)
    return w, g


@pytest.mark.parametrize("scroll,flag,learned", SCROLLS)
def test_mage_reads_and_is_told_the_spell(scroll, flag, learned):
    w, g = _at("TOWN-SQUARE", "mage", scroll)
    out = _do(g, "read scroll")
    assert MAGE_READS in out
    assert learned in out
    assert out.index(MAGE_READS) < out.index(learned)
    assert w.globals.get(flag)
    assert w.objects[scroll].location is None   # consumed


@pytest.mark.parametrize("cls", ["warrior", "rogue"])
@pytest.mark.parametrize("scroll,flag,learned", SCROLLS)
def test_warrior_and_rogue_resist_and_learn_nothing(cls, scroll, flag, learned):
    w, g = _at("TOWN-SQUARE", cls, scroll)
    out = _do(g, "read scroll")
    assert RESISTANCE in out
    assert "spell learned" not in out
    assert not w.globals.get(flag)
    assert w.objects[scroll].location is w.player   # not consumed


@pytest.mark.parametrize("cmd", ["read scroll", "give scroll to will"])
@pytest.mark.parametrize("scroll,flag,learned", SCROLLS)
def test_will_teaches_and_the_spell_is_named(cmd, scroll, flag, learned):
    w, g = _at("WIZARDS-TOWER", "warrior", scroll)
    out = _do(g, cmd)
    assert TEACHING in out
    assert learned in out
    assert out.index(TEACHING) < out.index(learned)
    assert w.globals.get(flag)
    assert w.objects[scroll].location is None   # consumed


# READ SCROLL with the incantation scroll carried too: every scroll is readable,
# so the parser asks instead of picking the incantation scroll.

INCANTATION_AWAY = "Wherever these are meant to be spoken, it isn't here."


@pytest.mark.parametrize("cls", ["mage", "warrior", "rogue"])
@pytest.mark.parametrize("scroll,flag,learned", SCROLLS)
def test_read_scroll_asks_which_when_the_incantation_is_carried(cls, scroll, flag, learned):
    w, g = _at("TOWN-SQUARE", cls, scroll)
    w.move_object(w.objects["INCANTATION-SCROLL"], w.player)
    out = _do(g, "read scroll")
    assert "Which scroll do you mean" in out
    assert "the incantation scroll" in out
    assert w.objects[scroll].desc in out
    assert INCANTATION_AWAY not in out
    assert not w.globals.get(flag)


@pytest.mark.parametrize("scroll,flag,learned", SCROLLS)
def test_mage_names_the_spell_scroll_beside_the_incantation(scroll, flag, learned):
    w, g = _at("TOWN-SQUARE", "mage", scroll)
    w.move_object(w.objects["INCANTATION-SCROLL"], w.player)
    adjective = w.objects[scroll].adjectives[0]
    out = _do(g, f"read {adjective} scroll")
    assert learned in out
    assert w.globals.get(flag)
    assert w.objects["INCANTATION-SCROLL"].location is w.player
