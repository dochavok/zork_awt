"""
Traps (traps.md; experience.md — Trap Disarmament, Class XP Adjustments).

The walkthroughs force every roll to its maximum, so they only ever see a trap
spotted and disarmed. These fix the level roll low and high and check both
sides: what a disarm pays (Warrior and Rogue), and what a trap does when it
fires. Triggering a trap — by accident or on purpose — pays nothing.

Expected numbers and text are the design's, written out here (or text
constants pinned to the design by test_design_text.py).
Run with: pytest roundabout/test_traps.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import light

LOW, HIGH = 0, 99          # level roll totals: every Medium check fails / passes

# experience.md — Trap Disarmament: XP per disarm (Rogues +5 each)
TRAP_XP = {8: 3, 15: 4, 16: 3, 17: 3, 19: 5, 29: 3, 33: 5, 36: 3, 41: 5, 45: 5}
TRAP_TOTAL = 39
ROGUE_BONUS = 5

# traps.md / locations.md text
BONES_CRACK = "The bones crack underfoot. The grinding stops. Then the doorway fills."
# mechanics.md — the shared disarm success / failure lines
NOTICED = ("and are able to disarm it, neutralizing it.",
           "but your attempt to disarm it fails miserably.")
FLOOD_WARNING = "The water is at your knees. One turn left."


def _quiet(fn, *a, **kw):
    with patch("sys.stdout", io.StringIO()):
        return fn(*a, **kw)


def _world(cls="warrior"):
    """Level 1, torch lit, and no room pays exploration XP — so XP moves only for traps."""
    w, g = _make_world(cls=cls, level=1, hearts=5, zenni=10)
    _give(w, "TORCH")
    _quiet(light.light_torch, w)
    for room in w.rooms.values():
        room.value = 0
    return w, g


def _give(w, name):
    obj = w.objects[name]
    obj.clear_flag("INVISIBLE")
    w.move_object(obj, w.player)


def _rolls(total):
    return patch("content.player.roll", return_value=total)


def _arrive(w, g, room, total):
    """Walk into `room` and spend one turn there, every level roll fixed at `total`."""
    buf = io.StringIO()
    with _rolls(total), patch("sys.stdout", buf):
        g.enter_room(w.rooms[room])
        g.do_turn("wait")
    return buf.getvalue()


def _arrive_botched(w, g, room):
    """Walk in and spend a turn: the trap is spotted, then the disarm roll fails.
    (Perception is forced rather than queued as the first roll — a random Zenni
    find in the room can take a perception roll of its own.)"""
    buf = io.StringIO()
    with patch("content.player.check_perception", return_value=True), \
         _rolls(LOW), patch("sys.stdout", buf):
        g.enter_room(w.rooms[room])
        g.do_turn("wait")
    return buf.getvalue()


def _cmd(g, cmd, total):
    with _rolls(total):
        return _do(g, cmd)


# ---------------------------------------------------------------------------
# What each disarm pays — experience.md's table, Warrior and Rogue
# ---------------------------------------------------------------------------

def test_trap_table_totals_39():
    assert sum(TRAP_XP.values()) == TRAP_TOTAL


def _disarm(trap, w, g):
    """Disarm one trap the way the player would, every roll passing."""
    if trap == 8:
        _arrive(w, g, "INSCRIPTION-CHAMBER", HIGH)       # spotted: you step around it
    elif trap == 15:
        _arrive(w, g, "MAGNETIC-VAULT", HIGH)            # filings spotted
        _cmd(g, "disarm lodestone", HIGH)
    elif trap == 16:
        _arrive(w, g, "SHATTER-TRAP-MIRROR", HIGH)
    elif trap == 17:
        _arrive(w, g, "SUPPLY-ROOM", HIGH)
    elif trap == 19:
        _arrive(w, g, "PORTCULLIS-CORRIDOR", HIGH)
    elif trap == 29:
        _arrive(w, g, "COMBAT-ROOM", HIGH)
    elif trap == 33:
        _give(w, "SACK-OF-SALT")
        _arrive(w, g, "IDOL-ROOM", HIGH)
        _cmd(g, "swap idol with salt", HIGH)
    elif trap == 36:
        _arrive(w, g, "ANTECHAMBER", HIGH)
        _cmd(g, "clear bones", HIGH)
    elif trap == 41:
        _arrive(w, g, "FLOODING-ROOM", HIGH)
    elif trap == 45:
        _arrive(w, g, "INK-CORRIDOR", HIGH)


# (Mages are left out: their +1 per first dungeon-room entry is test_mage_bonus.py's.)
@pytest.mark.parametrize("cls,bonus", [("warrior", 0), ("rogue", ROGUE_BONUS)])
@pytest.mark.parametrize("trap", sorted(TRAP_XP))
def test_disarm_pays_design_xp(trap, cls, bonus):
    w, g = _world(cls)
    _disarm(trap, w, g)
    assert w.globals["xp"] == TRAP_XP[trap] + bonus


# ---------------------------------------------------------------------------
# Missed or botched: the trap fires and pays nothing
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("cls", ["warrior", "rogue"])
@pytest.mark.parametrize("room", ["INSCRIPTION-CHAMBER", "SHATTER-TRAP-MIRROR", "SUPPLY-ROOM",
                                  "PORTCULLIS-CORRIDOR", "COMBAT-ROOM", "FLOODING-ROOM",
                                  "INK-CORRIDOR"])
def test_missed_trap_pays_nothing(room, cls):
    w, g = _world(cls)
    out = _arrive(w, g, room, LOW)
    assert w.globals["xp"] == 0
    assert not any(line in out for line in NOTICED)     # unnoticed: no disarm attempt


def test_trap8_snare_fires_and_holds_until_pulled_free():
    from content.inscription import _HANGING
    w, g = _world()
    _arrive(w, g, "INSCRIPTION-CHAMBER", LOW)
    assert w.get_global("SNARE-HANGING")
    assert w.get_global("CRAWLSPACE-FOUND")        # triggering it reveals the crawlspace too
    assert _HANGING in _do(g, "west")              # can't leave while hanging
    _cmd(g, "pull free", LOW)                      # Medium strength: retry allowed
    assert w.get_global("SNARE-HANGING")
    for _ in range(5):
        _do(g, "wait")                             # no release on its own
    assert w.get_global("SNARE-HANGING")
    _cmd(g, "pull free", HIGH)
    assert not w.get_global("SNARE-HANGING")
    assert w.globals["xp"] == 0


def test_trap15_failed_disarm_leaves_the_lodestone_and_pays_nothing():
    w, g = _world()
    _arrive(w, g, "MAGNETIC-VAULT", HIGH)
    _cmd(g, "disarm lodestone", LOW)
    assert w.get_global("LODESTONE-STATE") is None
    assert w.globals["xp"] == 0
    _cmd(g, "disarm lodestone", HIGH)              # retry allowed
    assert w.get_global("LODESTONE-STATE") == "removed"
    assert w.globals["xp"] == TRAP_XP[15]


def test_trap15_unspotted_cannot_be_disarmed():
    w, g = _world()
    _arrive(w, g, "MAGNETIC-VAULT", LOW)
    _cmd(g, "disarm lodestone", HIGH)
    assert w.get_global("LODESTONE-STATE") is None
    assert w.globals["xp"] == 0


@pytest.mark.parametrize("perceive", [LOW, "botch"])
def test_trap16_crossbow_once_for_one_heart(perceive):
    # Missed, or spotted but botched: the crossbow fires once (1 heart) and is spent
    w, g = _world()
    if perceive == LOW:
        _arrive(w, g, "SHATTER-TRAP-MIRROR", LOW)
    else:
        _arrive_botched(w, g, "SHATTER-TRAP-MIRROR")
    assert w.globals["hearts"] == 4
    _arrive(w, g, "SHATTER-TRAP-MIRROR", LOW)       # return visit: no longer a factor
    assert w.globals["hearts"] == 4
    assert w.globals["xp"] == 0


def test_trap17_smoke_costs_a_heart_but_the_jar_is_still_there():
    w, g = _world()
    _arrive(w, g, "SUPPLY-ROOM", LOW)
    assert w.globals["hearts"] == 4
    assert not w.objects["SMOKE-JAR"].has_flag("INVISIBLE")
    _arrive(w, g, "SUPPLY-ROOM", LOW)               # first entry only
    assert w.globals["hearts"] == 4


def test_trap17_botched_disarm_still_smokes():
    w, g = _world()
    out = _arrive_botched(w, g, "SUPPLY-ROOM")
    assert NOTICED[1] in out
    assert w.globals["hearts"] == 4
    assert w.globals["xp"] == 0


def test_trap17_disarmed_jar_without_damage():
    w, g = _world()
    _arrive(w, g, "SUPPLY-ROOM", HIGH)
    assert w.globals["hearts"] == 5
    assert not w.objects["SMOKE-JAR"].has_flag("INVISIBLE")


def test_trap19_unnoticed_charge_shocks_on_lift_and_costs_a_turn():
    w, g = _world()
    _arrive(w, g, "PORTCULLIS-CORRIDOR", LOW)
    assert w.globals["hearts"] == 5                 # unnoticed: nothing yet
    moves = w.moves
    _cmd(g, "lift portcullis", HIGH)                # still charged: lifting shocks
    assert w.globals["hearts"] == 4
    assert w.moves == moves + 2                     # the lift, then the stunned turn
    assert w.get_global("PORTCULLIS-HELD") is None


def test_trap19_botched_discharge_shocks():
    w, g = _world()
    _arrive_botched(w, g, "PORTCULLIS-CORRIDOR")
    assert w.globals["hearts"] == 4
    assert w.globals["xp"] == 0


def test_trap19_discharged_lift_needs_medium_strength():
    from content.shrine_path import _LIFT_FAILS
    w, g = _world()
    _arrive(w, g, "PORTCULLIS-CORRIDOR", HIGH)      # spotted and discharged
    assert _LIFT_FAILS in _cmd(g, "lift portcullis", LOW)
    assert w.get_global("PORTCULLIS-HELD") is None
    assert w.globals["hearts"] == 5                 # discharged: no shock
    _cmd(g, "lift portcullis", HIGH)
    assert w.get_global("PORTCULLIS-HELD") is not None


@pytest.mark.parametrize("total,shown", [(LOW, False), (HIGH, True)])
def test_trap33_plate_described_only_once_spotted(total, shown):
    from content.upper_tier import _IDOL_SPOTTED
    w, g = _world()
    out = _arrive(w, g, "IDOL-ROOM", total)
    assert (_IDOL_SPOTTED in out) is shown


def test_trap33_idol_without_swap_shuts_the_north_door():
    from content.upper_tier import SLAB_BLOCKS
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", LOW)
    _do(g, "take idol")
    assert w.get_global("IDOL-DOOR-SHUT")
    assert SLAB_BLOCKS in _do(g, "north")
    assert w.here.name == "IDOL-ROOM"
    _do(g, "south")                                 # the way south stays open
    assert w.here.name == "COMBAT-ROOM"
    assert w.globals["xp"] == 0


def test_trap33_pry_needs_crowbar_and_medium_strength_with_retries():
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", LOW)
    _do(g, "take idol")
    _cmd(g, "pry door", HIGH)                       # no crowbar
    assert w.get_global("IDOL-DOOR-SHUT")
    _give(w, "CROWBAR")
    _cmd(g, "pry door", LOW)
    assert w.get_global("IDOL-DOOR-SHUT")
    _cmd(g, "pry door", HIGH)
    assert not w.get_global("IDOL-DOOR-SHUT")


@pytest.mark.parametrize("direction", ["east", "south"])
def test_trap36_bones_kill_without_clearing(direction):
    w, g = _world()
    _arrive(w, g, "ANTECHAMBER", HIGH)              # no roll can save you here
    out = _cmd(g, direction, HIGH)
    assert BONES_CRACK in out
    assert w.get_global("GAME-OVER") is True


def test_trap36_west_is_always_safe():
    w, g = _world()
    _arrive(w, g, "ANTECHAMBER", LOW)
    _do(g, "west")
    assert not w.get_global("GAME-OVER")
    assert w.here.name == "PILE-OF-RUBBLE"


def test_trap41_glasses_then_botched_disarm_floods():
    from content.flooding import _SPOTTED
    w, g = _world()
    w.globals["actually_enchanted_glasses_worn"] = True
    assert _SPOTTED in _arrive(w, g, "FLOODING-ROOM", LOW)     # revealed; the player chooses
    assert w.get_global("FLOOD-TURNS") is None
    _cmd(g, "disarm plate", LOW)
    assert w.get_global("FLOOD-TURNS") is not None
    assert w.get_global("FLOOD-PLATE") != "disarmed"
    assert w.globals["xp"] == 0


def test_trap41_missed_plate_floods_the_room():
    w, g = _world()
    _arrive(w, g, "FLOODING-ROOM", LOW)
    assert w.get_global("FLOOD-TURNS") is not None
    assert FLOOD_WARNING in _do(g, "pull left lever")
    _do(g, "pull right lever")
    assert w.here.name != "FLOODING-ROOM"           # swept down to the mid tier
    assert not w.get_global("GAME-OVER")            # no damage on the sweep
    assert w.globals["hearts"] == 5


def test_trap41_botched_disarm_on_arrival_floods():
    w, g = _world()
    assert NOTICED[1] in _arrive_botched(w, g, "FLOODING-ROOM")
    assert w.get_global("FLOOD-TURNS") is not None
    assert w.get_global("FLOOD-PLATE") != "disarmed"
    assert w.globals["xp"] == 0


@pytest.mark.parametrize("botched", [False, True])
def test_trap45_thread_inks_the_player(botched):
    w, g = _world()
    if botched:
        assert NOTICED[1] in _arrive_botched(w, g, "INK-CORRIDOR")
    else:
        _arrive(w, g, "INK-CORRIDOR", LOW)
    assert w.get_global("INKED")
    assert w.globals["hearts"] == 5                 # no heart damage
    assert w.globals["xp"] == 0


# ---------------------------------------------------------------------------
# Trap 29 — the Combat Room plate, and the Warden behind it
# ---------------------------------------------------------------------------

def test_trap29_missed_plate_rings_the_bell_and_opens_the_den():
    from content.combat_room import _BELL, _WARDEN_EMERGES, WARDEN_HEARTS
    w, g = _world()
    out = _arrive(w, g, "COMBAT-ROOM", LOW)
    assert _BELL in out and _WARDEN_EMERGES in out
    assert not any(line in out for line in NOTICED)    # stepped on it unawares
    assert not w.get_global("PLATE-SPOTTED")
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.objects["WARDEN"].location is w.rooms["COMBAT-ROOM"]
    assert w.globals["WARDEN-HEARTS"] == WARDEN_HEARTS == 5     # locations.md — 5 hearts
    assert w.globals["xp"] == 0


def test_trap29_botched_disarm_rings_the_bell():
    from content.combat_room import _BELL
    w, g = _world()
    assert _BELL in _arrive_botched(w, g, "COMBAT-ROOM")
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.globals["xp"] == 0


def test_trap29_disarmed_plate_leaves_the_den_door_shut():
    w, g = _world()
    _arrive(w, g, "COMBAT-ROOM", HIGH)
    assert w.get_global("PLATE-STATE") == "disarmed"
    _do(g, "east")                                  # locations.md — the Den door stays shut
    assert w.here.name == "COMBAT-ROOM"


def test_trap29_jump_on_plate_fires_it_and_pays_nothing():
    from content.combat_room import _BELL
    w, g = _world()
    _arrive(w, g, "COMBAT-ROOM", HIGH)              # disarmed: 3 XP
    out = _do(g, "jump on plate")
    assert _BELL in out
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.globals["xp"] == TRAP_XP[29]           # the jump added nothing


def test_trap29_glasses_reveal_the_plate_and_the_player_chooses():
    from content.combat_room import _PLATE_SPOTTED
    w, g = _world()
    w.globals["actually_enchanted_glasses_worn"] = True
    out = _arrive(w, g, "COMBAT-ROOM", LOW)         # no perception roll needed
    assert _PLATE_SPOTTED in out
    assert w.get_global("PLATE-STATE") is None      # neither disarmed nor fired yet
    assert not w.objects["PRESSURE-PLATE"].has_flag("INVISIBLE")
    _cmd(g, "disarm plate", HIGH)
    assert w.get_global("PLATE-STATE") == "disarmed"
    assert w.globals["xp"] == TRAP_XP[29]


def test_trap29_glasses_then_botched_disarm_fires():
    w, g = _world()
    w.globals["actually_enchanted_glasses_worn"] = True
    _arrive(w, g, "COMBAT-ROOM", LOW)
    _cmd(g, "disarm plate", LOW)
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.globals["xp"] == 0


def test_warden_back_to_full_hearts_after_fleeing():
    # mechanics.md — Fleeing: the enemy resets to full hearts
    w, g = _world()
    w.globals["skill_melee"] = True
    _arrive(w, g, "COMBAT-ROOM", LOW)               # plate fires, Warden out
    with _rolls(HIGH), patch("content.combat.random.randint", return_value=1):
        _do(g, "kill warden")
    assert w.globals["WARDEN-HEARTS"] == 4
    _do(g, "north")
    _do(g, "south")
    assert w.here.name == "COMBAT-ROOM"
    assert w.globals["WARDEN-HEARTS"] == 5
