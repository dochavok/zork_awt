"""
Will Passion's Bedroom — Quest 58 (The Dragon-Nip) and the Quest 53 return.

Text: locations.md (Will Passion's Bedroom), items.md (Dragon-Nip, Golden
Dragon Scale, Enchanted Glasses), npcs.md (Will Passion — Dragon-nip
returned), quests.md (Quests 53 and 58).

The sprig is hidden under the nightstand: a silent Hard perception check on
every entry (after the description) and again when the glasses are put on
here. Actually Enchanted Glasses auto-pass.

State (story flags):
    DRAGON-NIP-RETURNED   sprig given to Will (Quest 58 complete)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.world import INVISIBLE

if TYPE_CHECKING:
    from engine.world import World, Room


BEDROOM = "WIZARDS-BEDROOM"

SPRIG_FOUND = (
    "Something small glows faintly under the nightstand — easy to miss, "
    "impossible to unsee once noticed. A sprig of something, tucked against the "
    "baseboard as if it rolled there and was forgotten."
)
SPRIG_LDESC = "A sprig of something glows faintly under the nightstand."

_GLASSES_RETURNED = "You set the glasses back on the nightstand, where they were."

_WILL_SPRIG = (
    "He takes it from you. Stares at it for a moment — not at you, at it.\n"
    "\"I've been looking for that.\"\n"
    "He sets it on the desk. Opens a low drawer and produces a scale — large, "
    "gold, catching the light like a mirror that's decided to be something "
    "else. He holds it out.\n"
    "\"Where did you find it?\" He asks it the way someone asks a question they "
    "already suspect the answer to. He doesn't wait for a response. \"Never "
    "mind.\" He turns back to his work.\n"
    "[Golden Dragon Scale added to inventory.]"
)


def _in_bedroom(w: World) -> bool:
    return w.here is not None and w.here.name == BEDROOM


def check_sprig(w: World) -> None:
    """Silent Hard check while the sprig is still hidden under the nightstand."""
    from content.perception import HARD
    from content.player import check_perception
    sprig = w.objects["DRAGON-NIP"]
    if INVISIBLE not in sprig.flags or sprig.location is not w.rooms[BEDROOM]:
        return
    if check_perception(w, HARD):
        from content import quests
        sprig.clear_flag(INVISIBLE)
        print(SPRIG_FOUND)
        quests.discover(w, "58")


def on_enter(w: World, room: Room) -> None:
    """Enter hook: the sprig check, after the room description."""
    if room.name == BEDROOM:
        check_sprig(w)


def on_wear_glasses(w: World) -> None:
    """Putting the glasses on in the bedroom fires the check too."""
    if _in_bedroom(w):
        check_sprig(w)


def return_glasses(w: World) -> bool:
    """
    DROP GLASSES / PUT GLASSES ON NIGHTSTAND. In the bedroom the glasses go
    back on the nightstand; the first time completes Quest 53 (20 XP if
    Actually Enchanted, 10 otherwise; 5 Zenni). Returns False elsewhere.
    """
    if not _in_bedroom(w):
        return False
    from content import quests
    w.move_object(w.objects["ENCHANTED-GLASSES"], w.here)
    print(_GLASSES_RETURNED)
    xp = 20 if w.get_global("GLASSES-ENCHANTED") else 10
    quests.complete(w, "53", xp_override=xp)
    return True


def give_sprig(w: World) -> None:
    """GIVE DRAGON-NIP TO WILL — the scale straight to the inventory, Quest 58."""
    from content import quests
    print(_WILL_SPRIG)
    w.move_object(w.objects["DRAGON-NIP"], None)
    w.move_object(w.objects["GOLDEN-DRAGON-SCALE"], w.player)
    w.set_global("DRAGON-NIP-RETURNED", True)
    quests.complete(w, "58")
