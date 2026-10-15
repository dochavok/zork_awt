"""
SEARCH — one deliberate extra look per visit (mechanics.md — Perception: SEARCH).

Room perception checks fire when the player arrives. SEARCH re-runs the ones
that haven't succeeded yet in this room — hidden items, hidden exits, hidden
Zenni — once per visit, for a turn. The same check functions run on entry and
here, so the difficulty lives in one place.

- Found: the check's own line (some at the end of the turn). Finds that only
  show in the room description get a lead-in, then the full description.
- Nothing found, nothing left to find, or already searched this visit:
  "You search carefully but find nothing unusual." — the same line either way.
- Not re-run: the arrival traps (Traps 8, 16, 17, 45, the Combat Room and
  Flooding Room plates, the mugger) — they're over before the player can type —
  and the ship's map, which already rolls every turn.

State: SEARCHED-HERE (cleared on every room entry)
"""

from __future__ import annotations
import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

NOTHING = "You search carefully but find nothing unusual."
_LEAD_IN = "Searching carefully, you notice something you missed."
_DARK = "It's too dark to see!"

# room -> [(module, function, shows_itself)]. shows_itself: the check prints
# its own line (now or at end of turn); otherwise the find only appears in the
# room description.
_CHECKS = {
    "WIZARDS-TOWER":       [("rooms", "bedroom_door_check", True)],
    "VOLCANO":             [("rooms", "volcano_stairs_check", False)],
    "BOG-SW":              [("rooms", "bog_sw_check", False)],
    "BOG-NE":              [("bog", "reveal", False)],
    "BOG-NW":              [("bog", "reveal", False)],
    "BOG-SE":              [("gravestone", "bog_se_enter", True), ("dankhaus", "path_check", True)],
    "INSCRIPTION-CHAMBER": [("inscription", "rune_stone_check", False)],
    "MAGNETIC-VAULT":      [("inscription", "vault_check", False)],
    "MINE-PASSAGE":        [("mid_tier", "silver_dust_check", False)],
    "ROUNDABOUT-FOREST":   [("old_oak", "bowl_piece_check", False)],
    "PRAYER-ALCOVE":       [("shrine_path", "niche_check", False)],
    "PORTCULLIS-CORRIDOR": [("shrine_path", "trap19_check", True)],
    "SHRINE-ROOM":         [("shrine_path", "shrine_piece_check", False)],
    "TOOL-ALCOVE":         [("tool_alcove", "alcove_check", False)],
    "TOLL-BRIDGE":         [("tunnels", "seal_check", True)],
    "IDOL-ROOM":           [("upper_tier", "idol_plate_check", False)],
}
# Enter hooks that check their own room: fn(w, room), every room
_HOOKS = [("mine", "on_enter"), ("mine_branch", "on_enter"), ("pond", "on_enter"),
          ("bedroom", "on_enter"), ("zenni_rooms", "on_enter")]


def _fn(module: str, name: str):
    return getattr(importlib.import_module(f"content.{module}"), name)


def on_enter(w: World, room) -> None:
    """Enter hook: a new visit — SEARCH is available again."""
    w.set_global("SEARCHED-HERE", False)


def search(w: World) -> None:
    room = w.here
    if room is None:
        return
    if not w.is_lit():
        print(_DARK)
        return
    if w.get_global("SEARCHED-HERE"):
        print(NOTHING)
        return
    w.set_global("SEARCHED-HERE", True)

    found = quiet = False
    for module, name, shows in _CHECKS.get(room.name, []):
        args = (w, room.name) if (module, name) == ("bog", "reveal") else (w,)
        if _fn(module, name)(*args):
            found = True
            quiet = quiet or not shows
    for module, name in _HOOKS:
        if _fn(module, name)(w, room):
            found = True
    if quiet:
        print(_LEAD_IN)
        w.game.desc_mode_override = True
        w.game.describe_room()
        w.game.desc_mode_override = False
    elif not found:
        print(NOTHING)
