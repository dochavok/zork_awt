"""
The Tip Journal — READ JOURNAL / EXAMINE JOURNAL.

Design: mechanics.md (Tip Journal), items.md (Tip Journal).

- A live quest log: each discovered, unfinished quest by name (never its
  number), in discovery order, tagged with how it was first found —
  [Board], [May] or [Organic] — and every hint bought from May for it,
  indented, labelled with the tier it was bought at, in purchase order.
- The hint that covers The Hollow Statue covers The Undead Warden too.
- Readable carried or on the floor here; anywhere else, "You don't have a
  journal."

State: QUEST-LOG [(quest, source)] (content/quests.py),
       HINT-LOG [(quest, tier, text)] (content/may_hints.py)
"""

from __future__ import annotations
import re
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World

_NONE = "You don't have a journal."
_EMPTY = "The journal is empty."
_HEADER = "JOURNAL"
_SHARED_HINT = {"30": "19"}     # The Undead Warden lists The Hollow Statue's hints


def _within_reach(w: World) -> bool:
    loc = w.objects["TIP-JOURNAL"].location
    while loc is not None:
        if loc is w.player or loc is w.here:
            return True
        loc = getattr(loc, "location", None)
    return False


def _entries(w: World) -> list[tuple[str, str]]:
    from content import quests
    seen, out = set(), []
    for q, source in w.globals.get("QUEST-LOG", []):
        if q not in seen:
            seen.add(q)
            out.append((q, source))
    for q in quests.active_quest_ids(w):         # set without a log entry
        if q not in seen:
            seen.add(q)
            out.append((q, "Organic"))
    return [(q, s) for q, s in out
            if quests.is_discovered(w, q) and not quests.is_complete(w, q)]


def read(w: World) -> None:
    from content import quests
    entries = _entries(w)
    if not entries:
        print(_EMPTY)
        return
    width = max(len(quests.name(q)) for q, _s in entries) + 4
    hints = w.globals.get("HINT-LOG", [])
    blocks = []
    for q, source in entries:
        lines = [f"{quests.name(q).ljust(width)}[{source}]"]
        for hq, tier, text in hints:
            if hq == q or hq == _SHARED_HINT.get(q):
                lines.append(f"  Tier {tier}: {text}")
        blocks.append("\n".join(lines))
    print(_HEADER + "\n\n" + "\n\n".join(blocks))


def journal_action(w: World) -> int:
    if w.prsa in ("V-READ", "V-EXAMINE"):
        read(w)
        return M_HANDLED
    return M_NOT_HANDLED


_ASK = re.compile(r"^\s*(read|examine|x|look at|l at)\s+(the\s+|my\s+)?(tip\s+)?journal\s*$")


def journal_input_hook(w: World, text: str) -> bool:
    """READ JOURNAL with no journal within reach."""
    if not _ASK.match(text.lower()) or _within_reach(w):
        return False
    print(_NONE)
    return True
