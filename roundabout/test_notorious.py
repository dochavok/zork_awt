"""
CURSE and the Notorious penalty (mechanics.md — Cursing and Notorious;
npcs.md — Will Passion: Cursing in his presence).
Run with: pytest roundabout/test_notorious.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_knight import _make_world, _do
from test_quit_and_exit import _run
from content import notorious, quests

def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


def _tower(zenni):
    w, g = _make_world(zenni=zenni)
    _goto(w, "WIZARDS-TOWER")
    w.set_global("ZENNI-ROOMS", {})       # no hidden-Zenni find on entering the tower
    return w, g


# --- Cursing away from Will ----------------------------------------------------

@pytest.mark.parametrize("word", ["curse", "damn", "shit", "fuck"])
def test_curse_alone(word):
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    out = _do(g, word)
    assert "Such language in a high-class establishment like this!" in out
    assert "lucky that you weren't within 10 feet of the guild hall" in out


def test_curse_at_a_person():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    npc = w.objects["PYRONICUS"]
    w.move_object(npc, w.here)
    npc.flags.discard("INVISIBLE")
    assert "Insults of this nature won't help you." in _do(g, "curse pyronicus")


def test_curse_at_a_thing():
    w, g = _make_world()
    shovel = w.objects["SHOVEL"]
    w.move_object(shovel, w.player)
    assert "What a loony!" in _do(g, "curse shovel")


# --- Will's fine ---------------------------------------------------------------

def test_pay_takes_half_rounded_up():
    w, g = _tower(zenni=7)
    script, out = _run(g, ["curse", "pay"])
    assert notorious.FINE_PROMPT in script.prompts
    assert "Half of what you carry — 4 Zenni." in out
    assert notorious._PAID in out
    assert w.globals["zenni"] == 3
    assert not notorious.is_notorious(w)


def test_one_zenni_pays_one():
    w, g = _tower(zenni=1)
    _run(g, ["curse", "pay"])
    assert w.globals["zenni"] == 0


def test_refuse_then_no_pays_after_all():
    w, g = _tower(zenni=10)
    script, out = _run(g, ["curse", "refuse", "no"])
    assert notorious.SURE_PROMPT in script.prompts
    assert notorious._PAID in out
    assert w.globals["zenni"] == 5
    assert not notorious.is_notorious(w)


def test_refuse_then_yes_is_notorious():
    w, g = _tower(zenni=10)
    script, out = _run(g, ["curse", "refuse", "yes"])
    assert notorious._NOTORIOUS in out
    assert notorious.is_notorious(w)
    assert w.globals["zenni"] == 10               # nothing taken


def test_unclear_answer_asks_again():
    w, g = _tower(zenni=4)
    script, _ = _run(g, ["curse", "maybe", "pay"])
    assert script.prompts.count(notorious.FINE_PROMPT) == 2
    assert w.globals["zenni"] == 2


def test_empty_purse_gets_the_ledger():
    w, g = _tower(zenni=0)
    script, out = _run(g, ["curse"])
    assert notorious._LEDGER in out
    assert notorious.FINE_PROMPT not in script.prompts
    assert not notorious.is_notorious(w)


def test_each_curse_is_a_new_fine():
    w, g = _tower(zenni=10)
    _run(g, ["curse", "pay", "damn", "pay"])
    assert w.globals["zenni"] == 2                # 10 -> 5 -> 2


def test_guild_hall_line_not_shown_in_the_tower():
    w, g = _tower(zenni=4)
    _, out = _run(g, ["curse", "pay"])
    assert "guild hall" not in out


# --- What Notorious costs ------------------------------------------------------

def test_notorious_quests_pay_no_xp_or_zenni():
    w, g = _make_world(zenni=10)
    w.set_global("NOTORIOUS", True)
    xp = w.globals["xp"]
    quests.complete(w, "41")                      # The Child's Kite: 4 XP, 3 Zenni
    assert quests.is_complete(w, "41")            # the quest still finishes
    assert w.globals["xp"] == xp
    assert w.globals["zenni"] == 10


def test_quests_pay_normally_otherwise():
    w, g = _make_world(zenni=10)
    xp = w.globals["xp"]
    quests.complete(w, "41")
    assert w.globals["xp"] == xp + 4
    assert w.globals["zenni"] == 13


def test_notorious_will_teaches_but_no_xp():
    w, g = _tower(zenni=0)
    w.set_global("NOTORIOUS", True)
    scroll = w.objects["SCROLL-UNBIND-UNDEAD"]
    w.move_object(scroll, w.player)
    xp = w.globals["xp"]
    _do(g, "give unbind scroll to will")
    assert w.globals.get("spell_unbind_undead")
    assert w.globals["xp"] == xp


def test_score_and_journal_show_notorious():
    w, g = _make_world()
    assert notorious.STANDING not in _do(g, "score")
    w.set_global("NOTORIOUS", True)
    assert notorious.STANDING in _do(g, "score")
    w.move_object(w.objects["TIP-JOURNAL"], w.player)
    assert notorious.STANDING in _do(g, "read journal")


def test_notorious_survives_save_and_restore(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    w, g = _tower(zenni=10)
    _run(g, ["curse", "refuse", "yes", "save"])
    w2, g2 = _make_world()
    _do(g2, "restore")
    assert notorious.is_notorious(w2)
