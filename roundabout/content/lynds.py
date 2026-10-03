"""
Lynds — Quest 59, Beat Lynds (arm wrestling, Tale and Ale).

Design: npcs.md (Lynds), quests.md (Quest 59), items.md (Heart Necklace).
- TALK TO LYNDS or CHALLENGE LYNDS: one contested strength roll, player vs
  Lynds's level-4 dice (2d10+3). Ties reroll.
- Loss: 20-turn cooldown before he'll go again.
- Win: Heart Necklace, Dankhaus invitation (wards cleared), Quest 59.
- Heart Necklace: +1 max heart while worn (neck slot).

State: LYNDS-BEATEN, LYNDS-COOLDOWN-UNTIL (world.moves), DANKHAUS-INVITED
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

COOLDOWN_TURNS = 20

LYNDS_PRESENCE = (
    "Lynds sits at a corner table, a drink in front of him and an elbow's "
    "worth of space cleared beside it."
)
_CHALLENGE = (
    "Lynds looks at you the way a person looks at something they're about to "
    "do that they've done many times before. He sets his drink down and puts "
    'his elbow on the table.\n"Go on then."'
)
_LOSS = (
    'Lynds wins without apparent effort. He picks his drink back up. "Not '
    'bad." He means it as a compliment. "Come back whenever."'
)
_COOLDOWN = '"Give me a bit. I\'m still drinking."'
_WIN = (
    "Lynds holds still for a moment after his hand goes down. Then he laughs "
    "— short, surprised, genuine.\n"
    '"Huh."\n'
    "He studies you for a moment, then reaches into his shirt and pulls out a "
    "necklace — a simple cord, a clay charm worn smooth. He sets it on the "
    "table between you.\n"
    '"My grandmother made that. Said it kept her heart going longer than it '
    "had any right to. I don't know if that's true but I've never had reason "
    'to doubt it. You earned it."\n'
    "He picks up his drink.\n"
    '"Come find us in the bog sometime. Ask for the Dankhaus. Tell them Lynds '
    'sent you."\n'
    "[Heart Necklace added to inventory.]"
)


def challenge(w: World) -> None:
    if w.get_global("LYNDS-BEATEN"):
        name = w.globals.get("player_name", "")
        print(f'Lynds grins. "You already beat me, {name}. I remember." He '
              "doesn't put his elbow down.")
        return
    if w.moves < int(w.get_global("LYNDS-COOLDOWN-UNTIL") or 0):
        print(_COOLDOWN)
        return

    print(_CHALLENGE)
    from content.player import roll_class_bonus
    while True:
        mine = roll_class_bonus(w, "strength")
        his = random.randint(1, 10) + random.randint(1, 10) + 3
        if mine != his:   # ties reroll
            break

    if mine > his:
        _win(w)
    else:
        print(_LOSS)
        w.set_global("LYNDS-COOLDOWN-UNTIL", w.moves + COOLDOWN_TURNS)


def _win(w: World) -> None:
    from content import quests
    print(_WIN)
    w.set_global("LYNDS-BEATEN", True)
    w.set_global("DANKHAUS-INVITED", True)   # Dankhaus wards cleared
    w.move_object(w.objects["HEART-NECKLACE"], w.player)
    quests.complete(w, "59")


def necklace_worn(w: World, worn: bool) -> None:
    """Heart Necklace: +1 max heart while worn (items.md)."""
    g = w.globals
    if worn:
        g["max_hearts"] = g.get("max_hearts", 1) + 1
        g["hearts"] = g.get("hearts", 1) + 1
    else:
        g["max_hearts"] = g.get("max_hearts", 2) - 1
        g["hearts"] = min(g.get("hearts", 1), g["max_hearts"])
