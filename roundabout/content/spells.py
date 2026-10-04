"""
CAST <spell> — spell names aren't objects, so CAST is read from the raw input
line (engine input hook) rather than the parser.

Design: mechanics.md (spell table: Unbind Undead — releases a bound spirit,
20-turn reuse timer). Spells are known via player stats spell_<name>.
Casting where there's nothing to affect does nothing and doesn't start the
reuse timer. Casting before a spell is ready again doesn't use a turn.

Fireball (mechanics.md — Combat): CAST FIREBALL [AT X]. Against an enemy here
(the mugger, the Warden): 1 heart, no roll, no strike back that round. The
werewolf: its failure line, and the round still happens. The Fountain Room ice:
its own line. Either way the 10-turn timer starts only when it hits something
alive; nothing to hit: "Nothing here answers the spell."
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

_SPELLS = {
    "unbind undead": ("spell_unbind_undead", 20),
    "light": ("spell_light", 0),          # no reuse timer (mechanics.md — Light Spell)
    "fireball": ("spell_fireball", 10),
}


def cast_input_hook(w: World, text: str) -> bool:
    words = text.strip().lower().split()
    if not words or words[0] not in ("cast", "incant", "chant"):
        return False
    rest = " ".join(words[1:])
    name = rest.split(" at ")[0].split(" on ")[0].strip()
    target = rest[len(name):].strip()
    for prep in ("at ", "on "):
        if target.startswith(prep):
            target = target[len(prep):].strip()
    if name not in _SPELLS:
        return False   # let the parser handle anything else
    flag, reuse = _SPELLS[name]
    if not w.globals.get(flag):
        print("You don't know that spell.")
        return True

    until = int(w.get_global(f"COOLDOWN-{flag}") or 0)
    if w.moves < until:
        from engine.game import HOOK_NO_TURN
        print("You reach for the spell and find it isn't ready yet.")
        return HOOK_NO_TURN

    if name == "light":
        from content import light
        light.cast_light(w)
        return True

    if name == "fireball":
        if _fireball(w, target):
            w.set_global(f"COOLDOWN-{flag}", w.moves + reuse)
        return True

    if name == "unbind undead":
        from content import chuckle
        if chuckle.free_ghost(w):
            w.set_global(f"COOLDOWN-{flag}", w.moves + reuse)
        else:
            print("Nothing here answers the spell.")
    return True


# ---------------------------------------------------------------------------
# Fireball
# ---------------------------------------------------------------------------

_ICE_LINE = (
    "The fireball bursts against the block and rolls off it like water off glass. The "
    "frost doesn't so much as dull. I guess not every problem can be solved with "
    "fireball."
)


def _fireball_hit(enemy) -> str:
    return (f"Fire leaves your hands in a single roaring sheet and takes the {enemy.desc} "
            "full on. It reels back through the smoke.")


def _here(w: World, name: str):
    obj = w.objects.get(name)
    if obj is None or obj.location is not w.here or obj.has_flag("INVISIBLE"):
        return None
    return obj


def _named(obj, words: str) -> bool:
    names = set(obj.synonyms) | set(obj.desc.lower().split())
    return any(word in names for word in words.split())


def _fireball(w: World, target: str) -> bool:
    """CAST FIREBALL [AT X]. True if it hit something (the timer starts)."""
    from engine.game import M_END
    from content import knight
    if knight.not_that(w):      # Quest 54: steel only
        return False
    enemies = [o for o in (_here(w, n) for n in ("MUGGER", "WARDEN", "WEREWOLF", "APPRENTICE")) if o]
    if w.get_global("APPRENTICE-FREED"):
        enemies = [o for o in enemies if o.name != "APPRENTICE"]
    ice = _here(w, "ICE-BLOCK")
    if target:
        enemies = [o for o in enemies if _named(o, target)]
        ice = ice if ice is not None and _named(ice, target) else None
    if enemies:
        enemy = enemies[0]
        if enemy.name == "WEREWOLF":
            from content import still_den
            print(still_den.FIREBALL_FAILS)
        else:
            print(_fireball_hit(enemy))
            if enemy.name == "MUGGER":
                from content import back_alley
                back_alley.fireball_hit(w)
            elif enemy.name == "APPRENTICE":
                from content import trap_side
                trap_side.fireball_hit(w)
            else:
                from content import combat_room
                combat_room.fireball_hit(w)
        # The turn's room round (the werewolf's claws) still happens
        if w.here is not None and w.here.action is not None:
            w.here.action(w, M_END)
        return True
    if ice is not None:
        print(_ICE_LINE)
        return False
    print("Nothing here answers the spell.")
    return False
