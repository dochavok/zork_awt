"""
Anything that can be carried is listed wherever it's dropped (mechanics.md —
Floor listings; TODO #20, 2026-10-14).

Every takeable object is picked up where it starts — by TAKE, and by a verb that
takes it first ("(Taken)": WEAR) — carried to an ordinary room, dropped, and
must then appear in LOOK. Objects that start nowhere (shop stock, quest
rewards) are handed over. New objects are covered automatically.

Before this, an item a room's own text described kept that room's "don't list"
flag everywhere: the hand cart dropped on the Rickety Bridge (playtest), the
support beam, the gold watch, and anything picked up by WEAR / DRINK / PUT,
which skipped the room's TAKE handling.
Run with: pytest roundabout/test_dropped_items_listed.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do, _make_world

PLAIN = "MAIN-EAST"
# Not dropped the ordinary way (their own DROP rules — mechanics.md / items.md)
SPECIAL_DROP = {"RING", "TORCH", "GRAVESTONE"}

_w, _ = _make_world()
TAKEABLE = sorted(n for n, o in _w.objects.items()
                  if o.has_flag("TAKEBIT") and not o.has_flag("TRYTAKEBIT")
                  and n not in SPECIAL_DROP)
START = {n: (_w.objects[n].location.name if _w.objects[n].location is not None
             and _w.objects[n].location.name in _w.rooms else None) for n in TAKEABLE}


# What a player has done before they can pick these up where they start: the
# quest step that makes the object reachable, set as the game sets it
_BEFORE = {
    "QUEEN-VIAL": {"SWARM_SETTLED": True},   # the smoke jar, used in the hollow (old_oak.py)
}


def _pick_up(name, how):
    """The object in the player's hands, picked up as a player would."""
    room = START[name] or PLAIN
    # Dark rooms: light by the spell, not a second torch ("Which torch do you mean")
    w, g, _ = _look(room, LIGHT_SPELL_ACTIVE=True, **_BEFORE.get(name, {}))
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")                  # as if found
    if START[name] is None:
        w.move_object(obj, w.player)                # handed over
        return w, g, obj
    _do(g, f"{how} {obj.synonyms[0]}")
    return w, g, obj


@pytest.mark.parametrize("how", ["take", "wear"])
@pytest.mark.parametrize("name", TAKEABLE)
def test_dropped_item_is_listed(name, how):
    w, g, obj = _pick_up(name, how)
    if obj.location is not w.player:
        pytest.skip(f"{how} doesn't pick it up where it starts")
    w.move_object(w.player, w.rooms[PLAIN])
    w.here = w.rooms[PLAIN]
    for other in list(w.player.contents):          # e.g. the lit torch a dark room needed
        if other is not obj and obj.synonyms[0] in other.synonyms:
            w.move_object(other, None)
    _do(g, f"drop {obj.synonyms[0]}")
    assert obj.location is w.here, f"DROP {name} didn't leave it here"
    look = _do(g, "look")
    shown = obj.desc.lower() in look.lower() or (obj.ldesc and obj.ldesc in look)
    assert shown, f"{name} dropped in {PLAIN} isn't listed:\n{look}"


def test_most_objects_are_really_picked_up():
    """The skips above are the exception: most objects really are picked up."""
    taken = 0
    for n in TAKEABLE:
        w, _, obj = _pick_up(n, "take")
        taken += obj.location is w.player
    assert taken >= len(TAKEABLE) * 0.9, f"only {taken} of {len(TAKEABLE)} picked up"


# --- The cart, the beam and the watch at home; the loaded cart -------------------------

def test_not_listed_twice_where_the_room_describes_it():
    for name, room in (("HAND-CART", "STORAGE-AREA"), ("SUPPORT-BEAM", "STORAGE-AREA"),
                       ("GOLD-WATCH", "THE-CREVICE")):
        w, g, _ = _look(room)
        obj = w.objects[name]
        _do(g, f"take {obj.synonyms[0]}")
        _do(g, f"drop {obj.synonyms[0]}")
        assert f"There is a {obj.desc} here." not in _do(g, "look"), name


def test_a_dropped_loaded_cart_shows_the_gravestone():
    w, g, _ = _look("BOG-SE")
    w.objects["GRAVESTONE"].flags.discard("INVISIBLE")
    w.move_object(w.objects["HAND-CART"], w.player)
    _do(g, "put stone in cart")
    _do(g, "drop cart")
    assert "The cart sits low on its axle under Calder Finch's gravestone." in _do(g, "look")
    _do(g, "take cart")
    _do(g, "unload stone")
    _do(g, "drop cart")
    assert "There is a hand cart here." in _do(g, "look")


def test_the_cart_at_the_graveyard_before_the_stone_is_back():
    w, g, _ = _look("GRAVEYARD")
    w.move_object(w.objects["HAND-CART"], w.player)
    _do(g, "drop cart")
    assert "There is a hand cart here." in _do(g, "look")


# --- "(Taken)" is a real TAKE ----------------------------------------------------------

def test_drink_holy_water_takes_it_off_the_desk():
    w, g, _ = _look("KEEPERS-CHAMBER")
    out = _do(g, "drink holy water")
    assert "(Taken)" in out and "You take the" not in out
    assert w.get_global("HOLY-WATER-TAKEN")
    assert "On the desk: a note in a careful hand." in _do(g, "look")


def test_wear_amulet_off_the_altar_puts_its_glow_out():
    w, g, _ = _look("ALTAR", DIAL=1)                      # The Veil of the Arcane
    amulet = w.objects["WEREWOLFS-AMULET"]
    amulet.flags.discard("INVISIBLE")
    w.move_object(amulet, w.player)
    _do(g, "put amulet on altar")
    assert w.get_global("GLOW-WEREWOLFS-AMULET")
    _do(g, "wear amulet")
    assert amulet.location is w.player
    assert not w.get_global("GLOW-WEREWOLFS-AMULET")


def test_a_refused_take_stops_the_command():
    w, g, _ = _look("LIGHTHOUSE")
    out = _do(g, "wear stone")                       # the paperweight stays (TRYTAKEBIT)
    assert "(Taken)" not in out
    assert w.objects["LIGHTHOUSE-STONE"].location is w.here
