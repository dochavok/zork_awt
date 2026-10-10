"""
Kevry Talborn — Captain's Quarters, Kevry's island (Quest 53, glasses).

Design: npcs.md (Kevry Talborn), quests.md (Quest 53), locations.md
(A House / Kevry's House, Captain's Quarters).
- Glasses worn on arrival: Kevry enchants them automatically.
- Glasses carried but not worn: he notices ("I know you brought them");
  WEAR GLASSES in front of him starts the enchantment.
- No glasses: TALK TO KEVRY gets a line that hints at the quest.
- "A House" becomes "Kevry's House" once the player has met him.

State: KEVRY-MET, GLASSES-ENCHANTED (with content/verbs._set_glasses_state)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_NOT_HANDLED, M_ENTER, M_END

if TYPE_CHECKING:
    from engine.world import World

_ENCHANT = (
    "Kevry looks at the glasses, then at you, then at the glasses again. "
    '"Will sent you." It isn\'t a question. He takes them gently. "Interesting '
    'that he didn\'t come himself." He does something brief and private with '
    "them that you don't quite follow. When he hands them back they feel "
    'different. Lighter, somehow, and more certain. "There. Don\'t lose them."'
)
_CARRIED = '"You\'ve got something in there," Kevry says, not looking up. "I know you brought them."'
_NO_GLASSES = (
    '"Hold still." Kevry leans in and studies you — eyes, nose, the bridge of '
    "the nose specifically — with the focus of a man reading a chart. Then he "
    'sits back. "No. At first I thought you were who Will sent to bring them." '
    'He shrugs. "Never mind. Nobody\'s brought them in years. Doesn\'t stop me '
    'hoping."'
)


def _glasses(w: World):
    return w.objects.get("ENCHANTED-GLASSES")


def _here_with_kevry(w: World) -> bool:
    k = w.objects.get("KEVRY")
    return k is not None and w.here is not None and k.location is w.here


def _met(w: World) -> None:
    if not w.get_global("KEVRY-MET"):
        w.set_global("KEVRY-MET", True)
        w.game.apply_room_names()                    # now Kevry's House


def quarters_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    """On arrival (after the room description, where Kevry looks up)."""
    if msg == M_ENTER:
        w.set_global("ARRIVED-CAPTAINS-QUARTERS", True)
        return M_NOT_HANDLED
    if msg == M_END and w.get_global("ARRIVED-CAPTAINS-QUARTERS"):
        w.set_global("ARRIVED-CAPTAINS-QUARTERS", False)
        g = _glasses(w)
        if g is None or w.get_global("GLASSES-ENCHANTED") or g not in w.player.contents:
            return M_NOT_HANDLED
        _met(w)
        from engine.world import WEARBIT
        if g.has_flag(WEARBIT):
            enchant(w)
        else:
            print(_CARRIED)
    return M_NOT_HANDLED


def on_wear_glasses(w: World) -> None:
    """WEAR GLASSES in front of Kevry starts the enchantment."""
    if _here_with_kevry(w) and not w.get_global("GLASSES-ENCHANTED"):
        enchant(w)


def talk(w: World) -> None:
    _met(w)
    g = _glasses(w)
    if w.get_global("GLASSES-ENCHANTED"):
        print('Kevry glances up from his map. "Don\'t lose them."')
    elif g is not None and g in w.player.contents:
        print(_CARRIED)
    else:
        print(_NO_GLASSES)


def enchant(w: World) -> None:
    from content.verbs import _set_glasses_state
    print(_ENCHANT)
    g = _glasses(w)
    # Name: Actually Enchanted Glasses. Description (items.md):
    # "slightly glowing wire-rimmed glasses".
    g.desc = "slightly glowing wire-rimmed glasses"
    g.ldesc = "A pair of slightly glowing wire-rimmed glasses rests on the nightstand."
    g.adjectives = ["wire-rimmed", "enchanted", "actually", "slightly", "glowing"]
    w.set_global("GLASSES-ENCHANTED", True)
    _set_glasses_state(w)
