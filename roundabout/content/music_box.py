"""
Quest 12 — The Locked Music Box (quests.md — Quest 12; items.md — Music Box
Key, Light Spell Scroll).

LOOK AT MUSIC BOX in Will's tower discovers the quest and gives Will's three
hints in turn (the third repeats). The key from the Bog-NW hollow log opens
it — the key stays in the lock — and the Light scroll is found: Quest 12
completes then. Will teaches the scroll to Warriors and Rogues (will.py).

Globals: MUSIC-BOX-HINT (0–3), MUSIC-BOX-OPEN.
"""

from __future__ import annotations
from engine.world import World, NDESCBIT, TAKEBIT

BOX_LOCKED_LISTING = "A small lacquered music box sits on the corner of Will's desk, its lid locked shut."
BOX_OPEN_LISTING = "A small lacquered music box sits open on the corner of Will's desk."

_HINTS = (
    "A small lacquered music box, its lid locked tight. Will glances up from his "
    "papers. \"That belonged to a student of mine. Bright. Restless. Never came back "
    "for it.\" He goes back to his writing, a little slower than before.",
    "Will doesn't look up. \"He spent half his apprenticeship out in the bog. Came "
    "back smelling of it, every time.\"",
    "\"Hid things, too,\" Will says. \"Hollow logs, mostly. Said nobody ever looks "
    "inside a log.\"",
)
_OPEN_WITH_SCROLL = "A small lacquered music box, its lid open."
_OPEN_EMPTY = "A small lacquered music box, its lid open. Empty now."
_LOCKED = "It's locked. There's a small keyhole in the front."
_OPENED = (
    "The key turns with a soft click. The lid lifts, and a short melody plays — a "
    "few bright notes, a little out of tune, then nothing. Inside, folded small, is "
    "a scroll."
)


def examine(w: World) -> None:
    """LOOK AT / EXAMINE MUSIC BOX."""
    if w.get_global("MUSIC-BOX-OPEN"):
        scroll = w.objects["SCROLL-LIGHT"]
        print(_OPEN_WITH_SCROLL if scroll.location is w.here else _OPEN_EMPTY)
        return
    from content import quests
    hint = int(w.get_global("MUSIC-BOX-HINT") or 0)
    print(_HINTS[min(hint, len(_HINTS) - 1)])
    if hint == 0:
        quests.discover(w, "12")
    w.set_global("MUSIC-BOX-HINT", min(hint + 1, len(_HINTS)))


def open_box(w: World) -> None:
    """OPEN MUSIC BOX [WITH KEY] / UNLOCK MUSIC BOX [WITH KEY]."""
    if w.get_global("MUSIC-BOX-OPEN"):
        examine(w)
        return
    key = w.objects["MUSIC-BOX-KEY"]
    if key not in w.player.contents:
        print(_LOCKED)
        return
    print(_OPENED)
    w.set_global("MUSIC-BOX-OPEN", True)
    box = w.objects["MUSIC-BOX"]
    box.fdesc = BOX_OPEN_LISTING
    # The key stays in the lock
    w.move_object(key, w.here)
    key.set_flag(NDESCBIT)
    key.clear_flag(TAKEBIT)
    w.objects["SCROLL-LIGHT"].clear_flag("INVISIBLE")
    from content import quests
    quests.discover(w, "12")
    quests.complete(w, "12")     # the scroll is found
