"""
REST — a Level 6 ability (mechanics.md — Spell Mechanics: REST notes;
experience.md — Leveling Curve).

- Recovers 1 heart. 50-turn reuse timer, started when rested. No XP.
- Outside combat only: a live enemy in the room refuses it — the spotted
  mugger, the Warden once he's out, the afflicted apprentice before he's
  freed, the living werewolf, a knight trial in progress.
- Works while inked. Stacks with inn healing and food.
- Refusals use no turn: before Level 6, in a fight, before the timer is up,
  or at full hearts (decided 2026-10-05).

State: COOLDOWN-spell_rest (the move REST is ready again)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

REST_REUSE = 50

_NOT_TIRED = "You're not tired."
_FIGHTING = "You can't rest now, there's fighting to be done!"
_TOO_SOON = "What are you sitting around for, there's a dungeon to explore!"
_FULL = "You're as rested as you're going to get."
_RESTED = (
    "You sit with your back to the nearest wall and let your breathing slow. "
    "When you get up, some of the ache has gone with it."
)


def _in(w: World, room: str) -> bool:
    return w.here is not None and w.here.name == room


def hostile_here(w: World) -> bool:
    """A live enemy in the room (mechanics.md — REST: outside combat only)."""
    if _in(w, "BACK-ALLEY"):
        return bool(w.get_global("MUGGER-SPOTTED")) and not w.get_global("MUGGER-DEAD")
    if _in(w, "COMBAT-ROOM"):
        return bool(w.get_global("WARDEN-OUT")) and not w.get_global("WARDEN-DEAD")
    if _in(w, "LOST-APPRENTICES-CELL"):
        return not w.get_global("APPRENTICE-FREED")
    if _in(w, "STILL-DEN"):
        return not w.get_global("WEREWOLF-DEAD")
    if _in(w, "TOWN-SQUARE"):
        return bool(w.get_global("KNIGHT-FIGHTING"))
    return False


def rest_input_hook(w: World, text: str):
    if text.strip().lower() != "rest":
        return False
    from engine.game import HOOK_NO_TURN
    g = w.globals
    if not g.get("spell_rest"):
        print(_NOT_TIRED)
        return HOOK_NO_TURN
    if hostile_here(w):
        print(_FIGHTING)
        return HOOK_NO_TURN
    if w.moves < int(w.get_global("COOLDOWN-spell_rest") or 0):
        print(_TOO_SOON)
        return HOOK_NO_TURN
    if g.get("hearts", 0) >= g.get("max_hearts", 0):
        print(_FULL)
        return HOOK_NO_TURN
    g["hearts"] += 1
    w.set_global("COOLDOWN-spell_rest", w.moves + REST_REUSE)
    print(_RESTED)
    return True
