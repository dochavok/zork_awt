"""
Verb handlers for Roundabout: The God-Forsaken Ring.
Built incrementally — handlers added as walkthrough sections require them.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# Score helper (called by game.enter_room on first visit)
# ---------------------------------------------------------------------------

def _score_upd(world: World, amount: int) -> None:
    world.score += amount
    world.set_global("SCORE", world.score)


# ---------------------------------------------------------------------------
# V-OPEN
# ---------------------------------------------------------------------------

def v_open(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    # White House mailbox — triggers opening sequence
    if obj.name == "MAILBOX-WHITE-HOUSE":
        if world.get_global("OPENING-DONE"):
            print("The mailbox is already open.")
            return M_HANDLED
        print("The mailbox opens.")
        world.set_global("OPENING-DONE", True)
        from content.char_create import run_opening
        run_opening(world, world.game)
        return M_HANDLED

    # Tower / tavern mailbox — teleports to Tower
    if obj.name == "MAILBOX-TOWER":
        print("You open the mailbox. A familiar warmth pulls you through.")
        tower = world.rooms.get("WIZARDS-TOWER")
        if tower is not None:
            world.game.enter_room(tower)
        return M_HANDLED

    print("You can't open that.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-EXAMINE
# ---------------------------------------------------------------------------

def v_examine(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    # Painting — teleports to Tale and Ale
    if obj.name == "PAINTING":
        print(
            "The painting shows the Tale and Ale in warm amber light — tables, "
            "people, the comfortable noise of an evening going well. As you look "
            "at it the room seems to shift, and then you are there."
        )
        tavern = world.rooms.get("TALE-AND-ALE")
        if tavern is not None:
            world.game.enter_room(tavern)
        return M_HANDLED

    # Generic examine: show ldesc or fdesc
    desc = obj.ldesc or obj.fdesc or obj.desc
    if desc:
        print(desc)
        obj.touched = True
    else:
        print(f"You see nothing special about the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-LOOK (bare look — redescribe current room)
# ---------------------------------------------------------------------------

def v_look(world: World) -> int:
    world.game.desc_mode_override = True
    world.game.describe_room()
    world.game.desc_mode_override = False
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-TAKE
# ---------------------------------------------------------------------------

def v_take(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    from engine.world import TAKEBIT, SACREDBIT
    if not obj.has_flag(TAKEBIT):
        print(f"You can't take the {obj.desc}.")
        return M_HANDLED

    if obj.has_flag(SACREDBIT):
        print(f"The {obj.desc} is fixed in place.")
        return M_HANDLED

    player = world.player
    if player is None:
        return M_NOT_HANDLED

    obj.touched = True
    desc = obj.ldesc or obj.desc

    if obj in player.contents:
        # Auto-take already moved it; just confirm with description
        print(f"Taken. {desc}" if desc else "Taken.")
        return M_HANDLED

    world.move_object(obj, player)
    print(f"Taken. {desc}" if desc else "Taken.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

def register_verbs(game) -> None:
    game.register_verb("V-OPEN",    v_open)
    game.register_verb("V-EXAMINE", v_examine)
    game.register_verb("V-LOOK",    v_look)
    game.register_verb("V-TAKE",    v_take)
