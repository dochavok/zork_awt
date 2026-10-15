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
TRAP_XP = {8: 3, 15: 4, 16: 3, 17: 3, 19: 5, 33: 5, 36: 3, 41: 5, 45: 5}
TRAP_TOTAL = 36            # Trap 29 is a scripted event, 0 XP (2026-10-14)
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
    with _rolls(total), patch("sys.stdout", buf), _no_pause():
        g.enter_room(w.rooms[room])
        g.do_turn("wait")
    return buf.getvalue()


def _no_pause():
    """Answer a [Press ENTER to continue] (the Combat Room's plate)."""
    return patch("content.char_create.input", lambda p="": "")


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

def test_trap_table_totals_36():
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
                                  "PORTCULLIS-CORRIDOR", "FLOODING-ROOM",
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


@pytest.mark.parametrize("command", [
    "use portcullis bar", "use bar on gate", "put bar", "place bar",
    "put bar under portcullis", "place iron bar beneath gate",
])
def test_trap19_bar_props_the_held_portcullis(command):
    from content.shrine_path import _PROPPED
    w, g = _world()
    _arrive(w, g, "PORTCULLIS-CORRIDOR", HIGH)      # spotted and discharged
    w.move_object(w.objects["PORTCULLIS-BAR"], w.player)
    _cmd(g, "lift portcullis", HIGH)
    assert _PROPPED in _do(g, command)
    assert w.get_global("PORTCULLIS") == "propped"
    assert w.objects["PORTCULLIS-BAR"].location is None


def test_trap19_put_bar_with_portcullis_down_just_drops_it():
    w, g = _world()
    _arrive(w, g, "PORTCULLIS-CORRIDOR", HIGH)
    w.move_object(w.objects["PORTCULLIS-BAR"], w.player)
    assert "You drop the portcullis bar." in _do(g, "put bar")
    assert w.objects["PORTCULLIS-BAR"].location is w.here


@pytest.mark.parametrize("total,shown", [(LOW, False), (HIGH, True)])
def test_trap33_plate_described_only_once_spotted(total, shown):
    from content.upper_tier import _IDOL_SPOTTED
    w, g = _world()
    out = _arrive(w, g, "IDOL-ROOM", total)
    assert (_IDOL_SPOTTED in out) is shown


def test_trap33_plate_line_after_taking_idol_without_salt():
    from content.upper_tier import _IDOL_SPOTTED, _PLATE_FIRED, _SLAB_DOWN
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", HIGH)                # plate spotted
    _do(g, "take idol")
    out = _do(g, "look")
    assert _PLATE_FIRED in out and _SLAB_DOWN in out
    assert _IDOL_SPOTTED not in out
    assert "holds a figurine" not in out


def test_trap33_plate_line_after_salt_swap():
    from content.upper_tier import _IDOL_SPOTTED, _PLATE_SALTED, _SLAB_DOWN
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", HIGH)
    _give(w, "SACK-OF-SALT")
    _cmd(g, "swap idol with salt", HIGH)
    out = _do(g, "look")
    assert _PLATE_SALTED in out
    assert _IDOL_SPOTTED not in out and _SLAB_DOWN not in out


def test_trap33_slab_described_until_pried_even_if_plate_unseen():
    from content.upper_tier import _PLATE_FIRED, _SLAB_DOWN
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", LOW)                 # plate never spotted
    _do(g, "take idol")
    out = _do(g, "look")
    assert _SLAB_DOWN in out and _PLATE_FIRED not in out
    _give(w, "CROWBAR")
    _cmd(g, "pry slab", HIGH)
    assert _SLAB_DOWN not in _do(g, "look")


def test_trap33_idol_without_swap_shuts_the_north_door():
    from content.upper_tier import SLAB_BLOCKS
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", LOW)
    _do(g, "take idol")
    assert w.get_global("IDOL-DOOR-SHUT")
    assert SLAB_BLOCKS in _do(g, "north")
    assert w.here.name == "IDOL-ROOM"
    with _no_pause():
        _do(g, "south")                             # the way south stays open
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


def test_trap33_lift_slab_pries_with_the_crowbar():
    from content.upper_tier import _LIFT_BARE, _NOT_BLOCKED, _PRIED, _PRY_FAILED
    w, g = _world()
    _arrive(w, g, "IDOL-ROOM", LOW)
    assert _NOT_BLOCKED in _do(g, "lift slab")       # not down yet
    _do(g, "take idol")
    assert _LIFT_BARE in _cmd(g, "lift slab", HIGH)  # no crowbar
    assert w.get_global("IDOL-DOOR-SHUT")
    _give(w, "CROWBAR")
    assert _PRY_FAILED in _cmd(g, "raise slab", LOW)
    assert w.get_global("IDOL-DOOR-SHUT")
    assert _PRIED in _cmd(g, "lift slab", HIGH)
    assert not w.get_global("IDOL-DOOR-SHUT")
    assert _NOT_BLOCKED in _do(g, "lift slab")       # already pried


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

# locations.md — Combat Room: the plate fires on first entry, from either
# side, whatever the rolls, the class or the glasses (redesigned 2026-10-14)
@pytest.mark.parametrize("total,cls,glasses", [(LOW, "warrior", False), (HIGH, "rogue", False),
                                               (HIGH, "rogue", True)])
def test_trap29_fires_on_entry_whatever_the_player(total, cls, glasses):
    from content.combat_room import _TRIGGER, _BELL, _WARDEN_EMERGES, WARDEN_HEARTS
    w, g = _world(cls)
    w.globals["actually_enchanted_glasses_worn"] = glasses
    out = _arrive(w, g, "COMBAT-ROOM", total)
    assert _TRIGGER in out and _BELL in out and _WARDEN_EMERGES in out
    assert not any(line in out for line in NOTICED)    # nothing to spot or disarm
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.objects["WARDEN"].location is w.rooms["COMBAT-ROOM"]
    assert w.globals["WARDEN-HEARTS"] == WARDEN_HEARTS == 5     # locations.md — 5 hearts
    assert w.globals["xp"] == 0                        # a scripted event pays nothing


def test_trap29_pauses_between_the_bell_and_the_warden():
    from content.combat_room import _TRIGGER, _BELL, _WARDEN_EMERGES
    from content.char_create import _PAUSE_CUE
    w, g = _world()
    buf = io.StringIO()

    def pause(prompt=""):
        buf.write("<" + prompt + ">")
        return ""
    with patch("sys.stdout", buf), patch("content.char_create.input", pause):
        g.enter_room(w.rooms["COMBAT-ROOM"])
        g.do_turn("wait")
    out = buf.getvalue()
    assert out.count(_PAUSE_CUE) == 1
    assert out.index(_TRIGGER) < out.index(_BELL) < out.index(_PAUSE_CUE) < out.index(_WARDEN_EMERGES)


def test_trap29_fires_coming_up_from_the_south():
    from content.combat_room import _BELL
    w, g = _world()
    w.move_object(w.player, w.rooms["PRAYER-ALCOVE"])
    w.here = w.rooms["PRAYER-ALCOVE"]
    with _no_pause():
        out = _do(g, "north")
    assert w.here.name == "COMBAT-ROOM" and _BELL in out


def test_trap29_doesnt_replay_on_return():
    from content.combat_room import _TRIGGER, WARDEN_PRESENCE
    w, g = _world()
    _arrive(w, g, "COMBAT-ROOM", LOW)
    _do(g, "north")
    out = _do(g, "south")                              # no pause needed: input isn't patched
    assert _TRIGGER not in out and WARDEN_PRESENCE in out


def test_trap29_an_old_save_with_the_plate_disarmed_fires_on_entry():
    # Before 2026-10-14 a disarmed plate left the Den door shut for good
    w, g = _world()
    w.set_global("PLATE-STATE", "disarmed")
    _arrive(w, g, "COMBAT-ROOM", LOW)
    assert w.get_global("PLATE-STATE") == "fired"
    assert w.objects["WARDEN"].location is w.rooms["COMBAT-ROOM"]


def test_trap29_the_flagstone_is_only_scenery():
    from content.combat_room import PLATE_EXAMINE
    w, g = _world()
    _arrive(w, g, "COMBAT-ROOM", LOW)
    assert PLATE_EXAMINE in _do(g, "examine flagstone")
    assert PLATE_EXAMINE in _do(g, "examine plate")
    assert "Nothing happens." in _do(g, "jump on plate")
    assert "There's nothing here to disarm." in _do(g, "disarm plate")
    assert w.globals["xp"] == 0


def test_trap29_the_den_door_is_open_once_the_warden_is_dead():
    w, g = _world()
    _arrive(w, g, "COMBAT-ROOM", LOW)
    w.set_global("WARDEN-DEAD", True)
    w.set_global("WARDEN-OUT", False)
    w.move_object(w.objects["WARDEN"], None)
    _do(g, "east")
    assert w.here.name == "CREATURE-DEN"


# locations.md — Combat Room: the Warden blocks EAST only, and strikes at
# anyone who tries (one roll; only he can hurt)
def _warden_out(cls="warrior"):
    w, g = _world(cls)
    _arrive(w, g, "COMBAT-ROOM", LOW)                  # plate fires, Warden out
    return w, g


def _east(g, total, warden_die):
    with _rolls(total), patch("content.combat.random.randint", return_value=warden_die):
        return _do(g, "east")


def test_warden_blocks_east_and_a_dodge_costs_nothing():
    from content.combat_room import WARDEN_BLOCKS, _DODGE
    w, g = _warden_out()
    out = _east(g, HIGH, 1)
    assert out.index(WARDEN_BLOCKS) < out.index(_DODGE)
    assert w.here.name == "COMBAT-ROOM"
    assert w.globals["hearts"] == 5


@pytest.mark.parametrize("total", [LOW, 3])            # lost, and tied (3d10 all 1s = 3)
def test_warden_blocks_east_and_a_lost_or_tied_roll_takes_a_heart(total):
    from content.combat_room import WARDEN_BLOCKS, _ROUND_LOST, _DODGE
    w, g = _warden_out()
    out = _east(g, total, 1)
    assert out.index(WARDEN_BLOCKS) < out.index(_ROUND_LOST) and _DODGE not in out
    assert w.here.name == "COMBAT-ROOM"
    assert w.globals["hearts"] == 4
    assert w.globals["WARDEN-HEARTS"] == 5             # the player never hits back


def test_warden_strike_at_east_can_kill():
    # Normal death rules
    w, g = _warden_out()
    w.globals["hearts"] = 1
    _east(g, LOW, 1)
    assert w.get_global("GAME-OVER") is True


@pytest.mark.parametrize("way,room", [("north", "IDOL-ROOM"), ("south", "PRAYER-ALCOVE")])
def test_warden_lets_you_flee_north_or_south_unharmed(way, room):
    from content.combat_room import WARDEN_BLOCKS, _ROUND_LOST
    w, g = _warden_out()
    with _rolls(LOW), patch("content.combat.random.randint", return_value=10):
        out = _do(g, way)
    assert w.here.name == room
    assert WARDEN_BLOCKS not in out and _ROUND_LOST not in out
    assert w.globals["hearts"] == 5


def test_invisible_slips_past_the_warden():
    from content.combat_room import WARDEN_BLOCKS, _SLIP_PAST
    w, g = _warden_out()
    w.globals["ring_worn"] = True
    out = _east(g, LOW, 10)
    assert _SLIP_PAST in out and WARDEN_BLOCKS not in out
    assert w.here.name == "CREATURE-DEN"
    assert w.globals["hearts"] == 5


def test_inked_ring_wearer_is_seen_and_blocked():
    # Ink (Trap 45) cancels the ring's invisibility — the Chuckle House rule
    from content.combat_room import WARDEN_BLOCKS
    w, g = _warden_out()
    w.globals["ring_worn"] = True
    w.set_global("INKED", True)
    assert WARDEN_BLOCKS in _east(g, HIGH, 1)
    assert w.here.name == "COMBAT-ROOM"


# locations.md — Combat Room: the Den door is an object, open from the
# plate's first firing on
@pytest.mark.parametrize("cmd", ["examine door", "examine heavy door", "look at door"])
def test_den_door_examines_open(cmd):
    from content.combat_room import DOOR_EXAMINE
    w, g = _warden_out()
    assert DOOR_EXAMINE in _do(g, cmd)


def test_den_door_open_and_close():
    from content.combat_room import _DOOR_OPEN, _DOOR_WONT_CLOSE
    w, g = _warden_out()
    assert _DOOR_OPEN in _do(g, "open door")
    assert _DOOR_WONT_CLOSE in _do(g, "close door")
    assert _DOOR_WONT_CLOSE in _do(g, "shut door")
    assert w.here.name == "COMBAT-ROOM"


def test_warden_pays_15_xp():
    # experience.md — Combat: the Warden 15 (raised from 12 when Trap 29 stopped paying)
    from content.combat_room import fireball_hit
    w, g = _world("rogue")                             # no Warrior +10 per kill
    _arrive(w, g, "COMBAT-ROOM", LOW)
    w.globals["WARDEN-HEARTS"] = 1
    _quiet(fireball_hit, w)
    assert w.get_global("WARDEN-DEAD")
    assert w.globals["xp"] == 15


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
