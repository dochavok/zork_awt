"""
The Lighthouse (locations.md — The Lighthouse): the smooth stone that weights
the Unbind Undead scroll, the desk and the keeper's log. TODO #15, 2026-10-14.

- The stone is scenery on the desk and never taken. While the scroll is there
  the scroll's listing covers it; once the scroll is taken, its own listing.
- TAKE STONE here means this stone, not a carried rune stone: it has TAKEBIT
  (TAKE prefers TAKEBIT objects) and the room's M-BEG refuses the take.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG

if TYPE_CHECKING:
    from engine.world import World


def room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg != M_BEG:
        return M_NOT_HANDLED
    stone = w.objects["LIGHTHOUSE-STONE"]
    if w.prsa == "V-TAKE" and w.prso is w.objects["SCROLL-UNBIND-UNDEAD"]:
        stone.clear_flag("NDESCBIT")         # its own listing from now on
        return M_NOT_HANDLED
    if w.prso is stone and w.prsa in ("V-TAKE", "V-MOVE", "V-PULL", "V-RAISE"):
        from content.objects import LIGHTHOUSE_STONE_STAYS
        print(LIGHTHOUSE_STONE_STAYS)        # before PRE-TAKE, so it's never taken
        return M_HANDLED
    return M_NOT_HANDLED
