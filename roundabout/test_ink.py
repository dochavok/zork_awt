"""
The inked player (traps.md — Trap 45; npcs.md, each NPC's "Inked player").
Run with: pytest roundabout/test_ink.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

SHAMUS = 'points the ladle at the door. "Not in my kitchen."'
RAZNAK = 'Raznak lowers his bow and studies you. "Wash," he says. "Then we talk."'
KNIGHT = '"I teach those who present themselves properly. Come back clean."'
CLERK = 'slides the ledger out of your reach. "Not near the records. Not like that."'
LIBRARIAN = 'between you and the shelves. "Not with those hands."'
LITLOCK = 'From inside, Litlock\'s voice: "Not like that, you\'re not."'
WILL = 'Everyone finds the thread." He turns back to his work. "The inn has a bath. Use it. Twice."'


def shared(name):
    return f"{name} takes one look at the ink and wants nothing to do with you until it's gone."


def _at(room, inked=True, **kw):
    w, g = _make_world(**kw)
    if inked:
        w.set_global("INKED", True)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


def _carry(w, name):
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")   # hidden until found in play
    w.move_object(obj, w.player)


# --- the six with their own lines ------------------------------------------------

def test_shamus_refuses_talk_buy_give_but_slate_reads():
    from content.quests import get_state
    w, g = _at("KITCHEN")
    assert SHAMUS in _do(g, "talk to shamus")
    assert get_state(w, "40") == "undiscovered"
    assert SHAMUS in _do(g, "buy dagger")
    assert w.objects["DAGGER"].location is None and w.globals["zenni"] == 10
    _carry(w, "BOG-THYME")
    assert SHAMUS in _do(g, "give thyme to shamus")
    assert w.objects["BOG-THYME"].location is w.player
    assert "Chalked on the slate" in _do(g, "read slate")
    assert "Chalked on the slate" in _do(g, "list")


def test_shamus_refuses_torch_exchange():
    w, g = _at("KITCHEN")
    _carry(w, "TORCH")
    assert SHAMUS in _do(g, "buy torch")


def test_raznak_refuses():
    w, g = _at("ARCHERY-RANGE", zenni=10)
    assert RAZNAK in _do(g, "talk to raznak")
    assert RAZNAK in _do(g, "give raznak three zenni")
    assert RAZNAK in _do(g, "pay raznak")
    assert w.globals["zenni"] == 10


def test_knight_refuses():
    w, g = _at("TOWN-SQUARE")
    w.set_global("KNIGHT-WON", True)
    for cmd in ("talk to knight", "challenge knight", "fight knight",
                "pay knight", "give knight three zenni"):
        assert KNIGHT in _do(g, cmd), cmd
    assert not w.get_global("KNIGHT-FIGHTING")
    assert w.globals["zenni"] == 10 and not w.globals.get("skill_melee")
    _carry(w, "BOW")
    assert KNIGHT in _do(g, "shoot knight")


def test_records_worker_refuses():
    w, g = _at("RECORDS-ROOM")
    assert CLERK in _do(g, "talk to clerk")
    _carry(w, "POCKET-WATCH")
    assert CLERK in _do(g, "give watch to clerk")
    assert w.objects["POCKET-WATCH"].location is w.player


def test_librarian_refuses():
    w, g = _at("LIBRARY")
    assert LIBRARIAN in _do(g, "talk to librarian")


def test_examine_still_works():
    w, g = _at("KITCHEN")
    assert SHAMUS not in _do(g, "examine shamus")


def test_litlock_door_even_invited():
    w, g = _at("BOG-SE")
    w.set_global("DANKHAUS-PATH-FOUND", True)
    w.set_global("DANKHAUS-INVITED", True)
    w.set_global("GRAVESTONE-FOUND", True)
    out = _do(g, "east")
    assert LITLOCK in out and "introduced yet" not in out
    assert w.here.name == "BOG-SE"


# --- the quest givers (shared line) ---------------------------------------------

@pytest.mark.parametrize("room,cmd,name", [
    ("STACKS", "talk to archivist", "The Archivist"),
    ("OLD-OAK", "talk to child", "The child"),
    ("BEEKEEPERS-COTTAGE", "talk to beekeeper", "The beekeeper"),
    ("VIKING-ENCAMPMENT", "talk to ivanaar", "Ivanaar Stormbringer"),
    ("HAALVARS-HUT", "talk to haalvar", "Haalvar"),
    ("FIRE-PIT", "talk to aylora", "Aylora"),
    ("PYRONICUS-FORGE", "talk to pyronicus", "Pyronicus"),
    ("COUNCIL-CHAMBER", "talk to rowan", "Councilman Rowan Finch"),
    ("TALE-AND-ALE", "challenge lynds", "Lynds"),
])
def test_quest_givers_refuse(room, cmd, name):
    w, g = _at(room)
    assert shared(name) in _do(g, cmd)


def test_quest_giver_keeps_item():
    w, g = _at("BEEKEEPERS-COTTAGE")
    _carry(w, "QUEEN-VIAL")
    assert shared("The beekeeper") in _do(g, "give vial to beekeeper")
    assert w.objects["QUEEN-VIAL"].location is w.player


def test_pyronicus_keeps_the_ring():
    w, g = _at("PYRONICUS-FORGE")
    w.move_object(w.objects["RING"], w.objects["PYRONICUS"])
    _do(g, "talk to pyronicus")
    assert w.objects["RING"].location is w.objects["PYRONICUS"]


def test_aylora_drink_refused():
    w, g = _at("FIRE-PIT")
    w.set_global("RIDDLE-DONE", True)
    w.set_global("CIRCLE-DONE", True)
    assert shared("Aylora") in _do(g, "drink")
    assert not w.get_global("AYLORA-OUT")


def test_ritual_stones_still_work():
    w, g = _at("RITUAL-CIRCLE")
    assert "The Earth stone hums" in _do(g, "activate earth stone")


# --- arrivals hold until clean ---------------------------------------------------

def _walk_to(w, g, dest):
    """Walk through the exit from here that leads to `dest`."""
    d = next(d for d, e in w.here.exits.items()
             if getattr(e, "destination", None) == dest)
    out = _do(g, d)
    assert w.here.name == dest
    return out


def _encampment_neighbour(w):
    return next(e.destination for e in w.rooms["VIKING-ENCAMPMENT"].exits.values()
                if getattr(e, "destination", None) not in (None, "HAALVARS-HUT"))


def test_ivanaar_greeting_holds():
    from content.quests import get_state
    from content.vikings import _IVANAAR_STATES
    w, g = _make_world()
    outside = _encampment_neighbour(w)
    w, g = _at(outside)
    w.set_global("VIKING-TRUST", True)          # no arrows at the range
    out = _walk_to(w, g, "VIKING-ENCAMPMENT")
    assert _IVANAAR_STATES[0] not in out
    assert get_state(w, "57") == "undiscovered"
    _walk_to(w, g, outside)
    w.set_global("INKED", False)
    out = _walk_to(w, g, "VIKING-ENCAMPMENT")
    assert _IVANAAR_STATES[0] in out
    assert get_state(w, "57") != "undiscovered"


def test_haalvar_riddle_holds_and_answers_refused():
    from content.vikings import _RIDDLE
    w, g = _at("VIKING-ENCAMPMENT")
    out = _walk_to(w, g, "HAALVARS-HUT")
    assert _RIDDLE not in out
    assert shared("Haalvar") in _do(g, "sea")
    assert not w.get_global("RIDDLE-DONE")


def test_beekeeper_greeting_holds():
    from content.quests import get_state
    w, g = _at("BEEKEEPERS-COTTAGE")
    _do(g, "look")
    assert get_state(w, "24") == "undiscovered"
    assert not w.get_global("BEEKEEPER-MET")
    w.set_global("INKED", False)
    _do(g, "look")
    assert get_state(w, "24") != "undiscovered"


# --- Will ----------------------------------------------------------------------

def test_will_talk_every_time():
    w, g = _at("WIZARDS-TOWER")
    for _ in range(2):
        out = _do(g, "talk to will")
        assert WILL in out and "no response" not in out


def test_will_disdain_once_then_teaches():
    w, g = _at("WIZARDS-TOWER", cls="warrior", zenni=10)
    _carry(w, "SCROLL-LIGHT")
    _carry(w, "SCROLL-UNBIND-UNDEAD")
    out = _do(g, "give light scroll to will")
    assert WILL in out
    assert out.index(WILL) < out.index("The knowing, I mean.")
    assert w.globals.get("spell_light")
    out = _do(g, "give unbind scroll to will")
    assert WILL not in out and w.globals.get("spell_unbind_undead")


def test_will_disdain_shows_again_after_a_bath_and_new_ink():
    from content import ink
    w, g = _at("WIZARDS-TOWER", cls="warrior", zenni=10)
    _carry(w, "SCROLL-LIGHT")
    _do(g, "read light scroll")
    assert w.get_global("WILL-DISDAIN-SHOWN")
    ink.cleaned(w)
    assert not w.get_global("INKED") and not w.get_global("WILL-DISDAIN-SHOWN")


def test_will_clean_unchanged():
    w, g = _at("WIZARDS-TOWER", inked=False)
    assert WILL not in _do(g, "talk to will")


# --- clean again ---------------------------------------------------------------

def test_clean_player_is_served():
    w, g = _at("KITCHEN", inked=False)
    assert SHAMUS not in _do(g, "talk to shamus")
    assert "What can I do for you?" in _do(g, "talk to shamus")
