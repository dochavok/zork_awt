"""
CAST <spell> — spell names aren't objects, so CAST is read from the raw input
line (engine input hook) rather than the parser.

Design: mechanics.md (spell table: Unbind Undead — releases a bound spirit,
20-turn reuse timer). Spells are known via player stats spell_<name>.
Casting where there's nothing to affect does nothing and doesn't start the
reuse timer.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

_SPELLS = {
    "unbind undead": ("spell_unbind_undead", 20),
    "light": ("spell_light", 0),          # no reuse timer (mechanics.md — Light Spell)
}


def cast_input_hook(w: World, text: str) -> bool:
    words = text.strip().lower().split()
    if not words or words[0] not in ("cast", "incant", "chant"):
        return False
    name = " ".join(words[1:]).split(" at ")[0].split(" on ")[0].strip()
    if name not in _SPELLS:
        return False   # let the parser handle anything else
    flag, reuse = _SPELLS[name]
    if not w.globals.get(flag):
        print("You don't know that spell.")
        return True

    until = int(w.get_global(f"COOLDOWN-{flag}") or 0)
    if w.moves < until:
        print("You reach for the spell and find it isn't ready yet.")
        return True

    if name == "light":
        from content import light
        light.cast_light(w)
        return True

    if name == "unbind undead":
        from content import chuckle
        if chuckle.free_ghost(w):
            w.set_global(f"COOLDOWN-{flag}", w.moves + reuse)
        else:
            print("Nothing here answers the spell.")
    return True
