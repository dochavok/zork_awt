"""
The Old Oak and its neighbours: Beekeeper's Cottage, Swarm Tree, and the
Verdant Circle shrine in Roundabout Forest.

Text: locations.md (The Old Oak, Beekeeper's Cottage, Swarm Tree, Roundabout
Forest), npcs.md (Child at the Old Oak, Beekeeper), items.md (Kite, Rune
Stones, Verdant Circle Shrine Bowl).

State (story flags):
    KITE-DOWN         kite retrieved from the oak (CLIMB TREE)
    KITE-RETURNED     kite given back to the child (Quest 41 complete)
    BEEKEEPER-MET     beekeeper's first-visit speech given (Quest 24 discovered)
    SWARM-SETTLED     smoke jar used at the Swarm Tree (the jar is used up)
    QUEEN-RETURNED    queen vial given back (Quest 24 complete)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_ENTER, M_LOOK, M_END

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# The Old Oak — Quest 41, The Child's Kite
# ---------------------------------------------------------------------------

_OAK_START = "A large oak dominates the clearing, old enough to have opinions."
_OAK_KITE = " A kite is tangled in its upper branches."
_OAK_END = (
    " The forest begins to the north; Beach Road runs south. A cottage sits "
    "off to the west, and to the east a broad old tree hums faintly."
)

CHILD_WAITING = (
    "A child stands under the oak, staring up at the kite with the patience "
    "of someone who has been at it a while."
)
CHILD_PLAYING = "The child is flying the kite in the clearing, badly and happily."

_CHILD_TALK = '"It\'s stuck," the child says, pointing up. As if you might not have noticed.'
_CLIMB = (
    "You haul yourself up through the branches and work the kite loose. "
    "Something comes free with it — a small flat stone on a cord, tangled in "
    "the line. It drops into the grass below."
)
_GIVE_KITE = (
    "The child takes the kite in both hands, inspects it for damage, finds "
    "none worth mentioning, and runs off to try again."
)


def oak_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        kite = "" if w.get_global("KITE-DOWN") else _OAK_KITE
        print(_OAK_START + kite + _OAK_END)
        return M_HANDLED
    return M_NOT_HANDLED


def climb_tree(w: World) -> None:
    if w.get_global("KITE-DOWN"):
        print("You climb a little way up the oak. There's nothing else up there.")
        return
    print(_CLIMB)
    w.set_global("KITE-DOWN", True)
    w.move_object(w.objects["KITE"], w.player)
    w.move_object(w.objects["OLD-OAK-RUNE-STONE"], w.rooms["OLD-OAK"])


def talk_child(w: World) -> None:
    if w.get_global("KITE-RETURNED"):
        print(CHILD_PLAYING)
    else:
        print(_CHILD_TALK)


def give_kite(w: World) -> None:
    from content import quests
    print(_GIVE_KITE)
    w.move_object(w.objects["KITE"], None)
    w.set_global("KITE-RETURNED", True)
    child = w.objects["OAK-CHILD"]
    child.fdesc = child.ldesc = CHILD_PLAYING
    quests.complete(w, "41")


# ---------------------------------------------------------------------------
# Beekeeper's Cottage — Quest 24 discovery
# ---------------------------------------------------------------------------

_BEEKEEPER_SPEECH = (
    '"You\'ll want to keep clear of the tree east of the oak," she says, '
    "before you've said anything. \"Swarm got loose and nested in a hollow "
    "there. I'd fetch them back, but my smoke kit's gone — somewhere in the "
    'tunnels under town, last I knew." She shrugs. "If you come across it."'
)


_BEEKEEPER_AFTER = (
    '"They\'re settling back in," she says, nodding toward the hives. "Took them '
    'a day to forgive me. Bees hold grudges."'
)
_QUEEN_RETURNED = (
    "She takes the vial in both hands and holds it up to the light. \"There she is,\" "
    "she says softly, to the bee rather than to you. When she looks up, she's smiling. "
    "\"The rest will follow her home. Here — you've earned this.\" She presses a small "
    "jar of honey into your hands. It's faintly warm.\n"
    "[Enchanted honey added to inventory.]"
)
_EAT_HONEY = ("You eat the honey. It tastes like summer, with something older "
              "underneath, and the warmth spreads out from your chest.")
HONEY_HEARTS = 2


def talk_beekeeper(w: World) -> None:
    print(_BEEKEEPER_AFTER if w.get_global("QUEEN-RETURNED") else _BEEKEEPER_SPEECH)


def give_queen(w: World) -> None:
    """GIVE VIAL TO BEEKEEPER — honey straight to the inventory, Quest 24."""
    from content import quests
    print(_QUEEN_RETURNED)
    w.move_object(w.objects["QUEEN-VIAL"], None)
    w.move_object(w.objects["ENCHANTED-HONEY"], w.player)
    w.set_global("QUEEN-RETURNED", True)
    quests.complete(w, "24")     # 10 XP, 5 Zenni, silent


def eat_honey(w: World) -> None:
    """EAT HONEY — 2 hearts, up to the maximum; the honey is used up."""
    g = w.globals
    print(_EAT_HONEY)
    w.move_object(w.objects["ENCHANTED-HONEY"], None)
    g["hearts"] = min(g.get("max_hearts", g.get("hearts", 1)), g.get("hearts", 1) + HONEY_HEARTS)


def cottage_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_END and not w.get_global("BEEKEEPER-MET"):
        from content import quests
        w.set_global("BEEKEEPER-MET", True)
        quests.discover(w, "24")
        print(_BEEKEEPER_SPEECH)
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Swarm Tree — without the smoke jar the swarm drives the player back out
# ---------------------------------------------------------------------------

_SWARM = "The swarm boils out of the hollow before you can do anything useful. You retreat."
_TREE = (
    "A broad-trunked tree at the forest edge, older than the others around it. A low "
    "drone comes from a dark gap in the bark at chest height. The air nearby has a "
    "quality that suggests strongly you should not approach without a plan."
)
_SETTLED = "The bees drift in and out of the hollow, slow and drowsy, paying you no mind."
_SMOKE = (
    "You break the wax and tip the jar toward the hollow. Grey smoke spills out, thick "
    "and slow, and pours into the gap in the bark. The drone falters and drops to a low, "
    "drowsy hum. The bees settle. Just inside the hollow, something small and glass "
    "catches the light."
)


def swarm_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_TREE)
        if w.get_global("SWARM-SETTLED"):
            print(_SETTLED)
        return M_HANDLED
    jar = w.objects["SMOKE-JAR"]
    if msg == M_BEG:
        if w.prsa == "V-USE" and w.prso is jar and jar in w.player.contents \
                and not w.get_global("SWARM-SETTLED"):
            print(_SMOKE)
            w.move_object(jar, None)                    # used up
            w.set_global("SWARM-SETTLED", True)
            w.objects["QUEEN-VIAL"].clear_flag("INVISIBLE")
            return M_HANDLED
        return M_NOT_HANDLED
    # M_END: after the room has been entered (XP awarded) and described.
    # Carrying the smoke jar keeps the swarm in the hollow.
    if msg == M_END and not w.get_global("SWARM-SETTLED") and jar not in w.player.contents:
        from content.combat import _take_damage
        print(_SWARM)
        _take_damage(w, 1)
        if not w.get_global("GAME-OVER"):
            w.game.enter_room(w.rooms["OLD-OAK"])
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Roundabout Forest — Verdant Circle shrine, bowl piece (Easy perception)
# ---------------------------------------------------------------------------

def forest_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    from content import shrine_bowl
    if msg == M_LOOK:
        shrine_bowl.forest_look(w)   # pedestal state (Quest 49)
        return M_HANDLED
    if msg == M_BEG:
        return shrine_bowl.forest_beg(w)
    if msg == M_ENTER:
        from content import quests
        from content.perception import EASY, reveal_if_found
        quests.discover(w, "49")   # shrine is visible on entry
        # before the description, so a found piece is listed with the room
        reveal_if_found(w, "BOWL-PIECE-FOREST", EASY)
    return M_NOT_HANDLED
