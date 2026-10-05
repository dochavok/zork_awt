"""
The Trophy Case in The Tower (Town Hall) — treasures are deposited for good.

Design: locations.md (The Tower — Trophy Case), mechanics.md (Trophy Case,
Score), items.md (Treasure Items table — points).

- OPEN / CLOSE CASE. PUT (or DROP) a treasure IN CASE while it's open: the
  treasure stays there for good and its points go to the score. Score and
  count are worked out from what's in the case (points() / count(), read by
  SCORE and the ending), so they always match what's on display.
- Non-treasures are refused, and so is a treasure already in the case;
  nothing comes back out.
- The Tower description and EXAMINE / LOOK IN CASE list what's behind the glass.

State: CASE-OPEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK
from engine.world import TRYTAKEBIT

if TYPE_CHECKING:
    from engine.world import World

# items.md — Treasure Items (Trophy Case)
TREASURE_POINTS = {
    "FORGOTTEN-BLADE": 60, "DIAMOND-BROOCH": 45, "FUNERAL-MASK": 36,
    "GOLDEN-DRAGON-SCALE": 36, "IDOL": 30, "GOLD-WATCH": 30,
    "SHIP-IN-A-BOTTLE": 24, "GOLD-NUGGET": 21, "PIE-RAT-COIN": 18,
}

_TOWER_TOP = (
    "The tower room is round, the walls following the cone of the roof above. A "
    "single window looks out over the town square, narrow enough that the view is "
    "more suggestion than panorama."
)
_CASE_EMPTY = (
    "The Trophy Case dominates the far wall — old wood and glass, built into the "
    "stone as if someone planned for it from the start. It is empty."
)
_CASE_FILLED = (
    "The Trophy Case dominates the far wall — old wood and glass, built into the "
    "stone as if someone planned for it from the start. Behind the glass: {items}."
)
_PLACARD = (
    "The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN "
    "PERPETUITY FOR THE GLORY OF ROUNDABOUT."
)
_UNTOUCHED = "The case has not been added to in some time."
_ADDED_TO = "Someone has been adding to it."

_EXAMINE_TOP = (
    "The case is well-made — solid glass panels, brass fittings, velvet lining "
    "gone slightly pale with age. Whoever built it expected it to hold things "
    "worth looking at."
)
_EXAMINE_EMPTY = (
    "At the moment it holds nothing. The placard below names the donor.\n"
    "The velvet has the faint impressions of items once displayed here and since "
    "removed — or perhaps never placed at all."
)

_OPENS = "The glass door swings open on its brass hinges."
_ALREADY_OPEN = "It's already open."
_CLOSES = "You close the case."
_ALREADY_CLOSED = "It's already closed."
_CLOSED = "The case is closed."
_NOT_TREASURE = "The case is for treasures. That isn't one."
_ALREADY_IN = "It's already in the case."
_DEPOSITED = "The {item} settles into the velvet. The case is a better place for it."
_KEPT = "That belongs to Roundabout now."


def _contents(w: World) -> list:
    return list(w.objects["TROPHY-CASE"].contents)


def _list(objs) -> str:
    names = [f"the {o.desc}" for o in objs]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def points(w: World) -> int:
    """Score: the points of every treasure in the case."""
    return sum(TREASURE_POINTS.get(o.name, 0) for o in _contents(w))


def count(w: World) -> int:
    return sum(1 for o in _contents(w) if o.name in TREASURE_POINTS)


def _count_line(n: int) -> str:
    return f"{n} treasure{'' if n == 1 else 's'} on display."


def _examine(w: World) -> None:
    held = _contents(w)
    print(_EXAMINE_TOP)
    if not held:
        print(_EXAMINE_EMPTY)
    else:
        print(f"Behind the glass: {_list(held)}.")
        print(_count_line(len(held)))


def _deposit(w: World, item) -> None:
    case = w.objects["TROPHY-CASE"]
    if not w.get_global("CASE-OPEN"):
        print(_CLOSED)
    elif item.location is case:
        print(_ALREADY_IN)
    elif item.name not in TREASURE_POINTS:
        print(_NOT_TREASURE)
    else:
        w.move_object(item, case)
        item.set_flag(TRYTAKEBIT)    # no implicit "(Taken)" out of the case
        print(_DEPOSITED.format(item=item.desc))


def tower_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        held = _contents(w)
        print(_TOWER_TOP)
        print(_CASE_FILLED.format(items=_list(held)) if held else _CASE_EMPTY)
        print(_PLACARD)
        print(_ADDED_TO if held else _UNTOUCHED)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    case = w.objects["TROPHY-CASE"]
    prso, prsi = w.prso, w.prsi
    if prso is case and w.prsa in ("V-EXAMINE", "V-LOOK-INSIDE"):
        _examine(w)
    elif prso is case and w.prsa == "V-OPEN":
        print(_ALREADY_OPEN if w.get_global("CASE-OPEN") else _OPENS)
        w.set_global("CASE-OPEN", True)
    elif prso is case and w.prsa == "V-CLOSE":
        print(_CLOSES if w.get_global("CASE-OPEN") else _ALREADY_CLOSED)
        w.set_global("CASE-OPEN", False)
    elif prsi is case and w.prsa == "V-PUT-IN" and prso is not None:
        _deposit(w, prso)
    elif prso is not None and prso.location is case and w.prsa in ("V-TAKE", "V-TAKE-FROM"):
        print(_KEPT)
    else:
        return M_NOT_HANDLED
    return M_HANDLED


def make_rooms(world) -> None:
    tower = world.rooms["TOWN-HALL-TOWER"]
    tower.ldesc = ""
    tower.action = tower_action
