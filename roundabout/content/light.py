"""
Lighting and the torch (mechanics.md — Lighting System, Torch).

- Dark rooms (no ONBIT): the dungeon, the Secret Tunnels, the Crypt and the
  Mausoleum. Darkness is a hard block — the player can't walk into a dark
  room without a light source.
- The torch is lit from the moment it's bought (ONBIT). Its 100-turn timer
  starts on the first dark room entry and then runs every turn — it can't be
  put out. Warnings at 50, 30 and 15 turns left.
- Burnout is GAME OVER only if the player is in a dark room with no exit
  leading straight to a lit room. Otherwise the torch just goes out.

State: TORCH-LIT-TIMER (turns left, None until started)
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from engine.world import World, Room

TORCH_TURNS = 100

_TOO_DARK = "It's too dark to go any further without a light."
_IGNITION = "The torch catches the dark and pushes it back. Good thinking, getting one of these."
_WARNINGS = {
    50: "The torch burns a little lower than it did.",
    30: "The torch is noticeably dimmer now. It won't last forever.",
    15: "The torch gutters. You don't have much time left on it.",
}
_BURNOUT_FATAL = (
    "The torch goes out. In the dark, something shifts. You never find out what.\n\n"
    "*** GAME OVER ***"
)
_BURNOUT_SAFE = "The torch gutters and goes out."


def _torch(w: World):
    return w.objects.get("TORCH")


def _room_lit(room: Room) -> bool:
    return room.has_flag("ONBIT")


def dark_block(w: World, destination: Room) -> Optional[str]:
    """Walk check: refuse a move into a dark room without a light source."""
    if _room_lit(destination):
        return None
    if w._has_light_source(w.player):
        return None
    return _TOO_DARK


def on_enter(w: World, room: Room) -> None:
    """Enter hook: the torch timer starts on the first dark room entry."""
    torch = _torch(w)
    if torch is None or _room_lit(room) or w.get_global("TORCH-LIT-TIMER") is not None:
        return
    if torch in w.player.contents and torch.has_flag("ONBIT"):
        w.set_global("TORCH-LIT-TIMER", TORCH_TURNS)
        print(_IGNITION)
        _ensure_clock(w)


def light_torch(w: World) -> None:
    """A newly bought torch is lit; its timer waits for the first dark room."""
    torch = _torch(w)
    torch.set_flag("ONBIT")
    torch.ldesc = "A lit torch."
    w.set_global("TORCH-LIT-TIMER", None)


def _ensure_clock(w: World) -> None:
    clock = w.game.clock
    if clock.get("torch-clock") is None:
        clock.add_demon("torch-clock", _torch_demon)
    event = clock.get("torch-clock")
    event.enabled = True
    event.ticks = 1


def _torch_demon(w: World) -> bool:
    left = w.get_global("TORCH-LIT-TIMER")
    if left is None:
        return False
    left -= 1
    w.set_global("TORCH-LIT-TIMER", left)
    if left in _WARNINGS:
        print(_WARNINGS[left])
    if left <= 0:
        _burn_out(w)
        return True
    w.game.clock.get("torch-clock").ticks = 1
    return left in _WARNINGS


def _burn_out(w: World) -> None:
    torch = _torch(w)
    torch.clear_flag("ONBIT")
    torch.desc = "burnt-out torch"
    torch.ldesc = "A burnt-out torch, cold and black at the end."
    w.set_global("TORCH-LIT-TIMER", None)
    here = w.here
    if here is not None and not _room_lit(here) and not _one_move_from_light(w, here) \
            and not w._has_light_source(w.player):
        print(_BURNOUT_FATAL)
        w.set_global("GAME-OVER", True)
        w.game.quit()
    else:
        print(_BURNOUT_SAFE)


def _one_move_from_light(w: World, room: Room) -> bool:
    for exit_ in room.exits.values():
        dest = w.rooms.get(exit_.destination) if exit_.destination else None
        if dest is not None and _room_lit(dest):
            return True
    return False


# ---------------------------------------------------------------------------
# Shamus's exchange — BUY TORCH while already carrying one (mechanics.md swap tiers)
# ---------------------------------------------------------------------------

_SWAP_PRICE = 3
_SWAP_REFUSED = (
    "Shamus glances at the torch. \"That one's got plenty of life left.\" He hands "
    "it back. \"Come see me when it's lower.\""
)
_SWAP_TIERS = (   # (lowest turns left, line) — first match wins
    (30, "Shamus glances at the torch. \"Getting there.\" He hands you a fresh one. \"Three Zenni.\""),
    (15, "Shamus glances at the torch. \"That one's running short.\" He hands you a fresh one. \"Three Zenni.\""),
    (0,  "Shamus glances at the torch. \"That one's had it.\" He hands you a fresh one. \"Three Zenni.\""),
)
_SWAP_SHORT = "\"Three Zenni,\" Shamus says, and doesn't let go of the fresh one."


def turns_left(w: World) -> int:
    """Life left on the carried torch: 100 until its first dark room, 0 burnt out."""
    torch = _torch(w)
    if not torch.has_flag("ONBIT"):
        return 0
    left = w.get_global("TORCH-LIT-TIMER")
    return TORCH_TURNS if left is None else left


def exchange(w: World) -> None:
    left = turns_left(w)
    if left >= 70:
        print(_SWAP_REFUSED)
        return
    if w.globals.get("zenni", 0) < _SWAP_PRICE:
        print(_SWAP_SHORT)
        return
    line = next(text for floor, text in _SWAP_TIERS if left >= floor)
    w.globals["zenni"] -= _SWAP_PRICE
    print(line)
    torch = _torch(w)
    torch.desc = "torch"
    light_torch(w)   # fresh: lit, timer waits for the next dark room
