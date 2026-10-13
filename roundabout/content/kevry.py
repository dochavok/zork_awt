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

from engine.game import M_NOT_HANDLED, M_HANDLED, M_ENTER, M_END, M_LOOK

if TYPE_CHECKING:
    from engine.world import World

_ENCHANT = (
    "Kevry looks at the glasses, then at you, then at the glasses again. "
    '"Will sent you." It isn\'t a question. He takes them gently. "Interesting '
    'that he didn\'t come himself." He does something brief and private with '
    "them that you don't quite follow. When he hands them back they feel "
    'different. Lighter, somehow, and more certain. "There. Don\'t lose them."'
)
_CARRIED = ('"You\'ve got something in there," Kevry says, his eyes on your pack. '
            '"I know you brought them."')
_QUARTERS = (
    "A small back room, all table and charts and the smell of ink. The doorway "
    "back into the house is west."
)
_FIRST_SEEN = (
    "A weathered man sits hunched over a map, muttering. He doesn't hear you "
    "come in. When he finally looks up, his face does something complicated — "
    "surprise, then recognition of the type that doesn't require prior "
    'acquaintance, then a wide and genuine grin. "Kevry," he says, by way of hello.'
)
_SEEN_AGAIN = "Kevry sits hunched over his map, muttering. He looks up and grins."
_SEEN_ENCHANTED = (
    "Kevry sits hunched over his map. He looks up long enough to check you still "
    "have the glasses."
)
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
    """The room, then Kevry's line (he introduces himself the first time);
    the glasses reaction follows at the end of the arrival turn."""
    if msg == M_LOOK:
        print(_QUARTERS)
        if not _here_with_kevry(w):
            return M_HANDLED
        if not w.get_global("KEVRY-MET"):
            print(_FIRST_SEEN)
            _met(w)                                  # he's said his name
        elif w.get_global("GLASSES-ENCHANTED"):
            print(_SEEN_ENCHANTED)
        else:
            print(_SEEN_AGAIN)
        return M_HANDLED
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
    g.desc = "slightly glowing wire-rimmed glasses"   # the room line follows (objects._Glasses)
    from content.objects import GLASSES_EXAMINE_ENCHANTED
    g.examine = GLASSES_EXAMINE_ENCHANTED
    g.adjectives = ["wire-rimmed", "enchanted", "actually", "slightly", "glowing"]
    w.set_global("GLASSES-ENCHANTED", True)
    _set_glasses_state(w)
