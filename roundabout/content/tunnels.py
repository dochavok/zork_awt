"""
The Crypt and the Secret Tunnels to the Dungeon Entrance — Quest 27.

Design: locations.md (The Crypt, Charnel Walk, The Bone Passage, The Junction,
The Undercroft, The Toll Bridge, Dungeon Entrance), quests.md (Quest 27),
npcs.md (Boggart).
- All of these rooms are dark (light.py).
- Toll Bridge: Medium perception spots the faded official seal → Quest 27
  discovered. The Boggart blocks the way south and his toll (200) can't be
  paid. GIVE CHARTER TO BOGGART evicts him, drops the strongbox, completes
  Quest 27. The strongbox opens on a Medium strength check: 10 Zenni.
- The Bone Passage's east door (Tavern Cellar) comes with Quest 25.

State: CRYPT-VISITS, SEAL-FOUND, BOGGART-GONE, STRONGBOX-OPEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

TOLL = 200
STRONGBOX_ZENNI = 10

_CRYPT = {
    1: ("The crypt has not been visited recently. Dust lies undisturbed on the "
        "stone floor, on the alcoves, on the remains within them. It is very "
        "quiet. Very cold. At the far end a rough-cut passage opens into "
        "darkness — older than the crypt itself, by the look of the stonework."),
    2: ("The crypt is quiet and cold. Dust lies on the stone floor — a set of "
        "footprints visible in it, the only sign anything has changed. The "
        "alcoves hold their dead without comment. At the far end the passage "
        "leads on into the dark."),
    3: ("The crypt is quiet and cold. Dust lies on the stone floor — several "
        "sets of footprints visible in it. For a crypt, it's practically a "
        "thoroughfare. The alcoves hold their dead without comment. At the far "
        "end the passage leads on into the dark."),
}

_BRIDGE_BOGGART = (
    "A narrow stone bridge spans a ravine in the tunnel floor — the drop below "
    "is deep enough that the bottom isn't visible. The bridge looks solid.\n"
    "A small, dense figure has planted itself at the center of it with the "
    "unmistakable air of someone who intends to stay.\n"
    "He eyes you with the satisfaction of a man whose position has never once "
    "been successfully argued with."
)
_BRIDGE_STRONGBOX = "The bridge is empty now. The strongbox sits where he was."
_BRIDGE_LOOTED = "The bridge is empty. The open strongbox sits where he was, lid thrown back."

_SEAL = (
    "Carved into the bridge's keystone, half worn away: the town's crest, and "
    "beneath it, PUBLIC PROPERTY."
)
_SEAL_HAVE_CHARTER = "You remember something about a bridge in the town charter."

_TOLL = (
    '"Toll," the Boggart says, holding out a hand without looking at it. "Two '
    'hundred Zenni. Each way. Non-negotiable." He doesn\'t explain how he '
    "arrived at the figure, and you get the impression he's never had to."
)
# The toll can't actually be paid
_PAY_REFUSED = (
    "He doesn't want your money. Whatever he wants 200 of, you don't have it."
)
_BLOCKED = "The Boggart doesn't move. Neither, it turns out, can you."
_EVICTED = (
    "The Boggart takes the charter, unrolls it, and reads. His lips move. He "
    "reads a particular clause twice. Then he rolls it back up with great "
    "dignity, hands it back, and gets off the bridge. \"Public property,\" he "
    "mutters. \"Should've been told.\" He stomps off into the tunnels, leaving "
    "behind a battered strongbox where he was sitting."
)
_BOX_OPENED = (
    "You get your fingers under the lid and heave. It gives with a shriek of "
    f"rusted hinges. Inside: {STRONGBOX_ZENNI} Zenni. You pocket them."
)
_BOX_STUCK = "The lid doesn't budge. Whatever's holding it shut is stronger than you are, for now."


class _BoggartExit(Exit):
    def resolve(self, world):
        if not world.get_global("BOGGART-GONE"):
            return None, _BLOCKED
        return super().resolve(world)


def crypt_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        w.set_global("CRYPT-VISITS", int(w.get_global("CRYPT-VISITS") or 0) + 1)
    elif msg == M_LOOK:
        print(_CRYPT[min(3, max(1, int(w.get_global("CRYPT-VISITS") or 1)))])
        return M_HANDLED
    return M_NOT_HANDLED


def bridge_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        if not w.get_global("BOGGART-GONE"):
            print(_BRIDGE_BOGGART)
        elif w.get_global("STRONGBOX-OPEN"):
            print(_BRIDGE_LOOTED)
        else:
            print(_BRIDGE_STRONGBOX)
        return M_HANDLED
    if msg == M_ENTER and not w.get_global("SEAL-FOUND"):
        from content.player import check_perception
        from content.perception import MEDIUM
        if check_perception(w, MEDIUM):
            w.set_global("SEAL-FOUND", "pending")
    elif msg == M_END and w.get_global("SEAL-FOUND") == "pending":
        from content import quests
        w.set_global("SEAL-FOUND", True)
        quests.discover(w, "27")
        print(_SEAL)
        if w.objects["TOWN-CHARTER"] in w.player.contents:
            print(_SEAL_HAVE_CHARTER)
    return M_NOT_HANDLED


def talk_boggart(w: World) -> None:
    print(_TOLL)


def pay_boggart(w: World) -> None:
    print(_PAY_REFUSED)


def give_charter(w: World) -> None:
    from content import quests
    print(_EVICTED)
    w.set_global("BOGGART-GONE", True)
    w.move_object(w.objects["BOGGART"], None)
    w.move_object(w.objects["STRONGBOX"], w.rooms["TOLL-BRIDGE"])
    quests.complete(w, "27")


def open_strongbox(w: World) -> None:
    if w.get_global("STRONGBOX-OPEN"):
        print("The strongbox is already open, and empty.")
        return
    from content.player import roll_class_bonus
    from content.perception import MEDIUM
    if roll_class_bonus(w, "strength") >= MEDIUM:
        print(_BOX_OPENED)
        w.set_global("STRONGBOX-OPEN", True)
        w.globals["zenni"] = w.globals.get("zenni", 0) + STRONGBOX_ZENNI
    else:
        print(_BOX_STUCK)


def make_rooms(world) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=1)
        r.set_flag(RLANDBIT)   # no ONBIT — dark
        world.register_room(r)
        return r

    crypt = room("CRYPT", "The Crypt", "")
    charnel = room(
        "CHARNEL-WALK", "Charnel Walk",
        "The passage ends at a low arch ahead — beyond it, the crypt. The air is "
        "colder here, noticeably so, as if the temperature has been coming down "
        "gradually and this is where it arrives. The walls are older stone, "
        "darker with moisture. The silence has a different quality than the "
        "tunnels behind you.",
    )
    bone = room(
        "BONE-PASSAGE", "The Bone Passage",
        "The stonework here is older than the rest of the tunnels — rougher cut, "
        "the joints wider, the walls slightly damp to the touch. The passage runs "
        "south. Whatever built this part didn't build it at the same time as the "
        "rest. The name feels earned.\n"
        "In the east wall, a low door of black oak is set into the older stone.",
    )
    junction = room(
        "JUNCTION", "The Junction",
        "The tunnel opens up here — not much, but enough to feel like a decision "
        "point. Rough stone walls, a ceiling low enough to notice. Passages branch "
        "three ways. The one to the east runs back toward the cellar. The air is "
        "damp and smells of old earth and something faintly mineral. Down here, "
        "sound doesn't carry the way it should.",
    )
    undercroft = room(
        "UNDERCROFT", "The Undercroft",
        "A wide passage, rough-hewn and unfinished, the kind of digging done in a "
        "hurry by people who knew where they were going. The walls are close "
        "enough that two people could pass but would have to mean it. The floor "
        "is uneven underfoot. The air is heavier here, deeper-smelling.",
    )
    bridge = room("TOLL-BRIDGE", "The Toll Bridge", "")
    entrance = room(
        "DUNGEON-ENTRANCE", "Dungeon Entrance",
        "The tunnel ends at a threshold — stone floor, stone walls, a passage "
        "leading south into darkness. Whatever is ahead doesn't announce itself. "
        "The air is different here: stiller, older, with a quality that suggests "
        "the dark ahead has been dark for a very long time. This is the end of the "
        "tunnels. The dungeon begins.",
    )

    # The Mausoleum is dark too (mechanics.md — Lighting System)
    mausoleum = world.rooms["MAUSOLEUM"]
    mausoleum.clear_flag("ONBIT")
    mausoleum.exits["down"] = Exit(destination="CRYPT")

    crypt.exits.update(up=Exit(destination="MAUSOLEUM"), down=Exit(destination="CHARNEL-WALK"))
    charnel.exits.update(up=Exit(destination="CRYPT"), north=Exit(destination="BONE-PASSAGE"))
    # Bone Passage east → Tavern Cellar (tunnel door) is wired in cellar.py
    bone.exits.update(south=Exit(destination="CHARNEL-WALK"), west=Exit(destination="JUNCTION"))
    junction.exits.update(east=Exit(destination="BONE-PASSAGE"), north=Exit(destination="UNDERCROFT"),
                          south=Exit(destination="TOLL-BRIDGE"))
    # Undercroft north → Forgotten Shaft: content/mine_branch.py
    undercroft.exits["south"] = Exit(destination="JUNCTION")
    bridge.exits.update(north=Exit(destination="JUNCTION"),
                        south=_BoggartExit(destination="DUNGEON-ENTRANCE"))
    # Dungeon Entrance south → Ink Corridor is wired in content/upper_tier.py
    entrance.exits["north"] = Exit(destination="TOLL-BRIDGE")

    crypt.action = crypt_action
    bridge.action = bridge_action
