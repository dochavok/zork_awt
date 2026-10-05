"""
The God-Forsaken Ring can't be dropped (items.md — The God-Forsaken Ring).

DROP / PUT (anywhere but the altar) / THROW RING get Will's line, worn or
not — no removal attempt, no corruption roll. PUT RING ON ALTAR and GIVE
RING TO WILL still work. The ring carries KEEPBIT, so ALL (DROP ALL, PUT
ALL IN ...) leaves it out (engine/parser.py). Weight 0 (objects.py).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World

KEEP_CLOSE = '"Bring it to me, or keep it close," Will said. You keep it close.'

_PARTING = frozenset({"V-DROP", "V-PUT", "V-PUT-IN", "V-PUT-ON", "V-PLACE", "V-THROW"})


def guard(w: World) -> int:
    """First in the PERFORM chain (the player's action)."""
    ring = w.prso
    if w.prsa not in _PARTING or ring is None or ring.name != "RING" \
            or ring.location is not w.player:
        return M_NOT_HANDLED
    if w.prsa == "V-PUT-ON" and w.prsi is not None and w.prsi.name == "ALTAR-STONE":
        return M_NOT_HANDLED          # the binding ritual (altar.py)
    print(KEEP_CLOSE)
    return M_HANDLED
