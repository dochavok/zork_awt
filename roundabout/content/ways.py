"""
Stairs and places (mechanics.md — Parser Verbs, Stairs and places; TODO #15,
2026-10-14).

- One STAIRS scenery object, a global of every room whose text has stairs or
  steps. STAIRS says which way each room's stairs go (and the exit that takes);
  SHOWN hides them while the room doesn't show them (the Kitchen's cellar
  door shut, the Volcano's stairs not yet found, the key door locked).
- CLIMB / GO UP / DOWN STAIRS, ASCEND / DESCEND, TAKE / USE STAIRS take them.
  Both ways and no direction given: "Up or down?", no turn (as TURN DIAL).
- PLACES: a named place in a room and the way into it — ENTER / GO INTO /
  GO IN / GO THROUGH it; bare ENTER or IN uses the room's one place.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World

# Room -> {which way the stairs go: the exit that takes them}
STAIRS = {
    "TALE-AND-ALE":      {"up": "up"},
    "UPSTAIRS-HALL":     {"down": "down"},
    "TOWN-HALL":         {"up": "up"},
    "UPPER-HALL":        {"up": "up", "down": "down"},
    "TOWN-HALL-TOWER":   {"down": "down"},
    "MAUSOLEUM":         {"down": "down"},
    "CRYPT":             {"up": "up"},            # its way down is a sloping passage
    "CHARNEL-WALK":      {"up": "up"},
    "KITCHEN":           {"down": "down"},
    "CELLAR":            {"up": "up"},
    "MID-TIER-KEY-DOOR": {"down": "south"},
    "KEY-DOOR-LANDING":  {"up": "north"},
    "VOLCANO":           {"down": "down"},
    "PYRONICUS-FORGE":   {"up": "up"},
    "LIGHTHOUSE":        {"up": "up"},            # the chained stair: UP's refusal
}

# Rooms whose stairs are only there in some states
SHOWN = {
    "KITCHEN":           lambda w: bool(w.get_global("CELLAR-DOOR-OPEN")),
    "VOLCANO":           lambda w: bool(w.get_global("VOLCANO-STAIRS-FOUND")),
    "MID-TIER-KEY-DOOR": lambda w: bool(w.get_global("KEY-DOOR-UNLOCKED")),
}

# Room -> (place object, the way in)
PLACES = {
    "ROUNDABOUT-FOREST": ("FOREST-MINE", "down"),
    "CHARNEL-WALK":      ("CRYPT-ARCH", "up"),
}

UP_OR_DOWN = "Up or down?"
_ONLY = "The stairs only go {way}."
_LEAD = {
    ("up",): "The stairs lead up.",
    ("down",): "The stairs lead down.",
    ("down", "up"): "The stairs lead up and down.",
}
ARCH = ("A low arch of older stone, its keystone worn smooth. Beyond it, steps "
        "climb up into the crypt.")


# Other room globals that only exist in some states
GLOBAL_SHOWN = {
    "LIBRARY-LEDGER": lambda w: bool(w.get_global("LIBRARIAN-MET")),   # she's brought it out
}


def global_filter(w: World, room, obj) -> bool:
    """World.global_filter: the stairs only where the room shows them; the
    library's ledger only once the librarian has brought it out."""
    if obj.name in GLOBAL_SHOWN:
        return GLOBAL_SHOWN[obj.name](w)
    if obj.name != "STAIRS":
        return True
    shown = SHOWN.get(room.name)
    return shown is None or shown(w)


def _walk(w: World, direction: str) -> int:
    w.walk_dir = direction
    return w.game.perform("V-WALK")


def take_stairs(w: World, want: Optional[str] = None) -> int:
    """Up or down the stairs here; want=None goes the only way they go."""
    ways = STAIRS.get(w.here.name if w.here else "", {})
    if want is None:
        if len(ways) > 1:
            from engine.game import M_NO_TURN
            print(UP_OR_DOWN)
            return M_NO_TURN
        want = next(iter(ways))
    if want not in ways:
        print(_ONLY.format(way=next(iter(ways))))
        return M_HANDLED
    return _walk(w, ways[want])


def stairs_action(w: World) -> int:
    """The STAIRS object: EXAMINE, TAKE / USE / ENTER STAIRS."""
    if w.prsa == "V-EXAMINE":
        ways = STAIRS.get(w.here.name, {})
        print(_LEAD[tuple(sorted(ways))])
        return M_HANDLED
    if w.prsa in ("V-TAKE", "V-USE", "V-ENTER", "V-WALK"):
        return take_stairs(w)
    return M_NOT_HANDLED


def place_here(w: World):
    """(place object, way in) for the current room, or None."""
    entry = PLACES.get(w.here.name if w.here else "")
    return (w.objects[entry[0]], entry[1]) if entry else None


def enter(w: World) -> bool:
    """ENTER [place] / GO INTO / IN / THROUGH [place]. True if handled here."""
    if w.prso is not None and w.prso.name == "STAIRS":
        take_stairs(w)
        return True
    place = place_here(w)
    if place is None:
        return False
    obj, way = place
    if w.prso is None or w.prso is obj:
        _walk(w, way)
        return True
    return False


def pre_walk_in(w: World) -> int:
    """Bare IN / GO IN with no "in" exit: the room's one place, if it has one."""
    if w.walk_dir != "in" or w.here is None or "in" in w.here.exits:
        return M_NOT_HANDLED
    place = place_here(w)
    if place is None:
        return M_NOT_HANDLED
    return _walk(w, place[1]) or M_HANDLED
