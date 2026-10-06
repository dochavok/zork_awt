"""
Quest 25 — The Flooded Cellar; Quest 32 — The Missing Gravestone; the hollow
statue (Quests 19 & 30). quests.md, locations.md, items.md, npcs.md.

The walkthroughs play each of these once, in the right order. These check the
wrong orders: drowning before the drain, the cart on stairs, the stone set
down in the wrong place, Rowan's dialogue states, the crowbar gates.

Expected numbers and text are the design's, written out here (or text
constants pinned to the design by test_design_text.py).
Run with: pytest roundabout/test_cellar_gravestone.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import light, quests

CACHE_ZENNI = 10                                   # quests.md — Quest 25 cashbox
NOT_BY_HAND = "It doesn't budge. Whatever carried this out here didn't carry it by hand."
ROWAN_KEY = ('He holds it out. "Take it. It was never meant for me."')
KEY_ADDED = "[Middle Tier Key added to inventory.]"
STATUE_SEALED = "The base is sealed tight. Something with leverage could pry it open."
STATUE_SEAM = ("The plaque below it is worn to illegibility, but the base has a seam around "
               "it — visible now that you're looking. Something with leverage could open it.")
STAKE_LISTING = "A silver stake lies in the hollow of the statue's base."
STATUE_LOOTED = "its base pried open and empty. Whatever was inside is gone."


def _world():
    w, g = _make_world(cls="warrior", level=3, hearts=5, zenni=10)
    _give(w, "TORCH")
    with patch("sys.stdout", io.StringIO()):
        light.light_torch(w)
    return w, g


def _give(w, name):
    obj = w.objects[name]
    obj.clear_flag("INVISIBLE")
    w.move_object(obj, w.player)


def _go(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


# ===========================================================================
# Quest 25 — The Flooded Cellar
# ===========================================================================

def _at_may(crowbar=True):
    w, g = _world()
    _go(w, "BAR")
    _do(g, "talk to may")                          # her introduction comes first
    if crowbar:
        _give(w, "CROWBAR")
    return w, g


def _door_open(drained=False):
    """Key from May, cellar door unlocked and open; optionally drained."""
    w, g = _at_may()
    _do(g, "talk to may")
    _do(g, "south")
    _do(g, "unlock door with key")
    _do(g, "open door")
    assert w.here.name == "KITCHEN" and w.get_global("CELLAR-DOOR-OPEN")
    if drained:
        _do(g, "use crowbar on drain")
        _do(g, "clear drain")
        assert w.get_global("CELLAR-DRAINED")
    return w, g


def test_may_gives_the_key_only_to_someone_carrying_the_crowbar():
    from content.cellar import _MAY_KEY
    w, g = _at_may(crowbar=False)
    assert _MAY_KEY not in _do(g, "talk to may")
    assert w.objects["CELLAR-KEY"] not in w.player.contents
    assert quests.get_state(w, "25") == "undiscovered"
    _give(w, "CROWBAR")
    assert _MAY_KEY in _do(g, "talk to may")
    assert w.objects["CELLAR-KEY"] in w.player.contents
    assert quests.get_state(w, "25") != "undiscovered"


def test_cellar_door_needs_the_key_and_keeps_it():
    w, g = _at_may()
    _do(g, "south")
    _do(g, "open door")
    assert not w.get_global("CELLAR-DOOR-OPEN")    # locked, no key yet
    _do(g, "north")
    _do(g, "talk to may")
    _do(g, "south")
    _do(g, "unlock door with key")
    assert w.objects["CELLAR-KEY"] not in w.player.contents   # it stays in the lock
    _do(g, "open door")
    assert w.get_global("CELLAR-DOOR-OPEN")


def test_down_before_the_drain_drowns():
    from content.cellar import _DROWN_STAIRS
    w, g = _door_open()
    out = _do(g, "down")
    assert _DROWN_STAIRS in out
    assert w.get_global("GAME-OVER") is True


def test_tunnel_door_from_bone_passage_before_the_drain_drowns():
    from content.cellar import _DROWN_TUNNEL
    w, g = _world()
    _go(w, "BONE-PASSAGE")
    out = _do(g, "open door")
    assert _DROWN_TUNNEL in out
    assert w.get_global("GAME-OVER") is True


def test_drain_needs_the_cover_off_first():
    w, g = _door_open()
    _do(g, "clear drain")
    assert not w.get_global("CELLAR-DRAINED")
    _do(g, "use crowbar on drain")
    _do(g, "clear drain")
    assert w.get_global("CELLAR-DRAINED")
    assert quests.is_complete(w, "25")


def test_drained_cellar_is_safe_and_pays_the_cache_once():
    w, g = _door_open(drained=True)
    _do(g, "down")
    assert w.here.name == "CELLAR" and not w.get_global("GAME-OVER")
    before = w.globals["zenni"]
    _do(g, "open cashbox")
    assert w.globals["zenni"] == before + CACHE_ZENNI
    _do(g, "open cashbox")
    assert w.globals["zenni"] == before + CACHE_ZENNI


def test_tunnel_door_after_the_drain_opens_both_ways():
    w, g = _door_open(drained=True)
    _do(g, "down")
    _do(g, "open door")
    _do(g, "west")
    assert w.here.name == "BONE-PASSAGE"
    _do(g, "east")
    assert w.here.name == "CELLAR"


def test_may_gives_the_boots_once_after_the_drain():
    from content.cellar import _MAY_BOOTS
    w, g = _door_open(drained=True)
    _do(g, "north")
    assert _MAY_BOOTS in _do(g, "talk to may")
    assert w.objects["BARTENDERS-BOOTS"] in w.player.contents
    assert _MAY_BOOTS not in _do(g, "talk to may")


# ===========================================================================
# Quest 32 — The Missing Gravestone
# ===========================================================================

def _stone_found():
    """Standing in Bog-SE with the gravestone spotted."""
    w, g = _world()
    with patch("content.player.roll", return_value=99), patch("sys.stdout", io.StringIO()):
        g.enter_room(w.rooms["BOG-SE"])
        g.do_turn("wait")
    assert w.get_global("GRAVESTONE-FOUND") is True
    return w, g


def _loaded():
    w, g = _stone_found()
    _give(w, "HAND-CART")
    _do(g, "load stone onto cart")
    assert w.objects["GRAVESTONE"].location is w.objects["HAND-CART"]
    return w, g


def test_gravestone_hidden_until_perception_easy():
    w, g = _world()
    with patch("content.player.roll", return_value=4), patch("sys.stdout", io.StringIO()):
        g.enter_room(w.rooms["BOG-SE"])            # Easy target 5: a 4 misses
        g.do_turn("wait")
    assert not w.get_global("GRAVESTONE-FOUND")
    assert w.objects["GRAVESTONE"].has_flag("INVISIBLE")


def test_gravestone_cant_be_carried_by_hand():
    w, g = _stone_found()
    assert NOT_BY_HAND in _do(g, "take stone")
    assert w.objects["GRAVESTONE"].location is w.rooms["BOG-SE"]


def test_loading_needs_the_cart():
    w, g = _stone_found()
    _do(g, "load stone onto cart")
    assert w.objects["GRAVESTONE"].location is w.rooms["BOG-SE"]


@pytest.mark.parametrize("direction", ["down", "up"])
def test_loaded_cart_cant_use_stairs(direction):
    from content.gravestone import _NO_STAIRS
    w, g = _loaded()
    room = "MAUSOLEUM" if direction == "down" else "CELLAR"
    _go(w, room)
    out = _do(g, direction)
    assert _NO_STAIRS in out
    assert w.here.name == room


def test_unloading_away_from_the_graveyard_tips_the_stone_off():
    from content.gravestone import _TIPPED_OFF, LISTING_MUD
    w, g = _loaded()
    _go(w, "BOG-NE")
    assert _TIPPED_OFF in _do(g, "unload stone")
    assert w.objects["GRAVESTONE"].location is w.rooms["BOG-NE"]
    assert w.objects["HAND-CART"] in w.player.contents          # the player keeps the cart
    assert not w.get_global("GRAVESTONE-RETURNED")
    assert LISTING_MUD in _do(g, "look")


def test_unloading_at_the_graveyard_sets_it_and_leaves_the_cart():
    from content.gravestone import _PLACED
    w, g = _loaded()
    _go(w, "GRAVEYARD")
    assert _PLACED in _do(g, "unload stone")
    assert w.get_global("GRAVESTONE-RETURNED")
    assert w.objects["GRAVESTONE"].location is w.rooms["GRAVEYARD"]
    assert w.objects["HAND-CART"].location is w.rooms["GRAVEYARD"]
    _do(g, "take stone")
    assert w.objects["GRAVESTONE"].location is w.rooms["GRAVEYARD"]   # fixed in place


def _at_rowan(w):
    _go(w, "COUNCIL-CHAMBER")


def test_rowan_dialogue_states_in_order():
    from content.gravestone import (_ROWAN_FIRST, _ROWAN_TROPHY, _ROWAN_START,
                                    _ROWAN_WAITING, _ROWAN_AFTER)
    w, g = _loaded()
    _at_rowan(w)
    assert _ROWAN_FIRST in _do(g, "talk to rowan")             # quest not yet discovered
    assert _ROWAN_TROPHY in _do(g, "talk to rowan")
    quests.discover(w, "32")                                   # the Mid-Tier Key Door seen
    assert _ROWAN_START in _do(g, "talk to rowan")
    assert _ROWAN_WAITING in _do(g, "talk to rowan")
    assert not quests.is_complete(w, "32")
    _go(w, "GRAVEYARD")
    _do(g, "unload stone")
    _at_rowan(w)
    out = _do(g, "talk to rowan")
    assert ROWAN_KEY in out and KEY_ADDED in out
    assert w.objects["MIDDLE-TIER-KEY"] in w.player.contents
    assert quests.is_complete(w, "32")
    assert _ROWAN_AFTER in _do(g, "talk to rowan")


def test_rowan_pays_nothing_until_the_stone_is_set():
    w, g = _loaded()
    quests.discover(w, "32")
    _at_rowan(w)
    _do(g, "talk to rowan")
    _go(w, "BOG-NE")
    _do(g, "unload stone")                                     # tipped off in the wrong place
    _at_rowan(w)
    assert ROWAN_KEY not in _do(g, "talk to rowan")
    assert w.objects["MIDDLE-TIER-KEY"] not in w.player.contents


# ===========================================================================
# The hollow statue — Quests 19 & 30
# ===========================================================================

def test_look_at_statue_shows_the_seam_and_discovers_19_and_30():
    w, g = _world()
    assert STATUE_SEAM in _do(g, "look at statue")
    assert quests.is_discovered(w, "19") and quests.is_discovered(w, "30")


def test_statue_without_crowbar_stays_sealed():
    w, g = _world()
    assert STATUE_SEALED in _do(g, "open statue")
    assert not w.get_global("STATUE-OPEN")


def test_crowbar_on_the_floor_is_not_enough():
    w, g = _world()
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.here)
    _do(g, "use crowbar on statue")
    assert not w.get_global("STATUE-OPEN")


def test_crowbar_opens_the_statue_with_no_roll():
    from content.statue import _PRIED
    w, g = _world()
    _give(w, "CROWBAR")
    with patch("content.player.roll", return_value=0):
        out = _do(g, "use crowbar on statue")
    assert _PRIED in out
    assert STAKE_LISTING in _do(g, "look")
    assert quests.is_discovered(w, "19") and quests.is_discovered(w, "30")


def test_statue_looted_once_both_items_are_taken():
    w, g = _world()
    _give(w, "CROWBAR")
    _do(g, "use crowbar on statue")
    _do(g, "take stake")
    assert STATUE_LOOTED not in _do(g, "look")                # the note is still inside
    _do(g, "take note")
    assert STATUE_LOOTED in _do(g, "look")


def test_unloading_outside_the_bog_leaves_it_on_the_ground():
    from content.gravestone import _LISTING_GROUND
    w, g = _loaded()
    _go(w, "MAUSOLEUM")
    _do(g, "unload stone")
    assert _LISTING_GROUND in _do(g, "look")


# --- Storage Area: the equipment line follows what's still there (locations.md) ---

@pytest.mark.parametrize("take,line", [
    ((), "_STORAGE_BOTH"),
    (("HAND-CART",), "_STORAGE_BEAM"),
    (("SUPPORT-BEAM",), "_STORAGE_CART"),
    (("HAND-CART", "SUPPORT-BEAM"), "_STORAGE_NONE"),
])
def test_storage_area_describes_what_is_left(take, line):
    from content import upper_tier
    w, g = _world()
    _go(w, "STORAGE-AREA")
    for name in take:
        _give(w, name)
    out = _do(g, "look")
    others = {"_STORAGE_BOTH", "_STORAGE_BEAM", "_STORAGE_CART", "_STORAGE_NONE"} - {line}
    assert getattr(upper_tier, line) in out
    assert not any(getattr(upper_tier, o) in out for o in others)
