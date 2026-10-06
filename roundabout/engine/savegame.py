"""
SAVE / RESTORE — snapshot of the mutable game state.

Behaviour (room/object actions, exit conditions, clock handlers) is code and
is rebuilt by initialize_world; only data that play can change is saved:
globals, object placement and text/flags, room visit state, the current room,
score, the turn count, clock timers, and description mode.

The file is named after the character: <name>.sav (mechanics.md — Save and
Restore). DEFAULT_PATH is only for a game with no name yet.
"""

from __future__ import annotations
import copy
import os
import pickle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.game import Game

DEFAULT_PATH = "roundabout.sav"

_OBJ_FIELDS = ("desc", "fdesc", "ldesc", "examine", "text", "synonyms", "adjectives",
               "flags", "touched", "size", "capacity", "value", "tvalue", "strength")


def snapshot(game: Game) -> dict:
    w = game.world

    def loc(o):
        where = o._location
        if where is None:
            return None
        kind = "room" if where.name in w.rooms and w.rooms[where.name] is where else "obj"
        return (kind, where.name)

    return {
        "globals": copy.deepcopy(w.globals),
        "objects": {
            name: {f: copy.deepcopy(getattr(o, f)) for f in _OBJ_FIELDS if hasattr(o, f)}
            for name, o in w.objects.items()
        },
        # contents order per container, so listings come back identical
        "room_contents": {n: [o.name for o in r.contents] for n, r in w.rooms.items()},
        "obj_contents": {n: [c.name for c in o.contents] for n, o in w.objects.items()},
        "locations": {name: loc(o) for name, o in w.objects.items()},
        "rooms": {n: {"visited": getattr(r, "visited", False), "value": r.value, "flags": set(r.flags)}
                  for n, r in w.rooms.items()},
        "here": w.here.name if w.here else None,
        "score": w.score,
        "moves": w.moves,          # turn-based timers store absolute turn numbers
        "clock": {n: (e.ticks, e.enabled) for n, e in game.clock._events.items()},
        "desc_mode": game.desc_mode,
    }


def apply(game: Game, data: dict) -> None:
    w = game.world
    w.globals.clear()
    w.globals.update(copy.deepcopy(data["globals"]))

    for name, fields in data["objects"].items():
        o = w.objects.get(name)
        if o is None:
            continue
        for f, v in fields.items():
            setattr(o, f, copy.deepcopy(v))

    # Placement: clear every container, then rebuild in saved order
    for r in w.rooms.values():
        r.contents.clear()
    for o in w.objects.values():
        o.contents.clear()
    for name, where in data["locations"].items():
        o = w.objects.get(name)
        if o is None:
            continue
        if where is None:
            o._location = None
        else:
            kind, cname = where
            o._location = w.rooms[cname] if kind == "room" else w.objects[cname]
    for cname, names in data["room_contents"].items():
        if cname in w.rooms:
            w.rooms[cname].contents.extend(w.objects[n] for n in names if n in w.objects)
    for cname, names in data["obj_contents"].items():
        if cname in w.objects:
            w.objects[cname].contents.extend(w.objects[n] for n in names if n in w.objects)

    for n, st in data["rooms"].items():
        r = w.rooms.get(n)
        if r is not None:
            r.visited, r.value, r.flags = st["visited"], st["value"], set(st["flags"])

    w.here = w.rooms.get(data["here"]) if data["here"] else None
    w.score = data["score"]
    w.moves = data.get("moves", 0)     # saves from before the turn count was kept: 0
    # Clock: a mid-game event the save had but this game lacks (always so in a
    # fresh game) is rebuilt from its factory; one this game created after the
    # save wasn't running then, so it's switched off.
    clock = game.clock
    for n, factory in game.clock_factories.items():
        e = clock._events.get(n)
        if n in data["clock"] and e is None:
            factory(w)
        elif n not in data["clock"] and e is not None:
            e.enabled = False
    for n, (ticks, enabled) in data["clock"].items():
        e = clock._events.get(n)
        if e is not None:
            e.ticks, e.enabled = ticks, enabled
    game.desc_mode = data["desc_mode"]


def path_for(name: str | None) -> str:
    """The save file for a character: <name>.sav in the current folder. Only
    letters, digits, spaces, hyphens, underscores and apostrophes are kept;
    a name with none of them falls back to roundabout.sav."""
    safe = "".join(c for c in (name or "") if c.isalnum() or c in " -_'").strip(" .")
    return f"{safe}.sav" if safe else DEFAULT_PATH


def find(name: str | None) -> str | None:
    """The existing save file for `name`, matching the name in any case."""
    want = path_for(name).lower()
    for entry in os.listdir("."):
        if entry.lower() == want and os.path.isfile(entry):
            return entry
    return None


def save(game: Game, path: str | None = None) -> None:
    path = path or path_for(game.world.globals.get("player_name"))
    with open(path, "wb") as fh:
        pickle.dump(snapshot(game), fh)


def restore(game: Game, path: str | None = None) -> bool:
    path = path or find(game.world.globals.get("player_name"))
    if path is None:
        return False
    try:
        with open(path, "rb") as fh:
            data = pickle.load(fh)
    except (OSError, pickle.UnpicklingError, EOFError):
        return False
    apply(game, data)
    return True
