"""
Room definitions for Roundabout: The God-Forsaken Ring.
Sourced from AWT_story_line/locations.md.
Built incrementally — rooms added as walkthrough sections require them.
"""

from __future__ import annotations
from engine.world import Room, Exit, ONBIT, RLANDBIT


def make_rooms(world) -> None:
    _make_opening(world)
    _make_tower(world)
    _make_tale_and_ale(world)


# ---------------------------------------------------------------------------
# Opening area
# ---------------------------------------------------------------------------

def _make_opening(world) -> None:
    r = Room(
        name="WHITE-HOUSE",
        desc="West of House",
        ldesc=(
            "You are standing in an open field west of a white house, "
            "with a boarded front door.\n"
            "There is a small mailbox here."
        ),
        value=1,
    )
    r.set_flag(ONBIT)
    r.set_flag(RLANDBIT)
    r.global_objects = ["MAILBOX-WHITE-HOUSE"]
    world.register_room(r)


# ---------------------------------------------------------------------------
# Will's Wizard Tower
# ---------------------------------------------------------------------------

def _make_tower(world) -> None:
    main = Room(
        name="WIZARDS-TOWER",
        desc="Will's Wizard Tower",
        ldesc=(
            "The tower doesn't announce itself. It simply is — books, firelight, "
            "the low hum of something you can't quite locate. A desk dominates one "
            "end, buried under papers that somehow manage to look organized. A "
            "painting hangs on the wall, slightly crooked. The room has the feeling "
            "of a place where important things happen without any particular fuss."
        ),
        value=1,
    )
    main.set_flag(ONBIT)
    main.global_objects = ["PAINTING", "MAILBOX-TOWER"]
    world.register_room(main)

    bedroom = Room(
        name="WIZARDS-BEDROOM",
        desc="Will Passion's Bedroom",
        ldesc=(
            "This is, apparently, where the magic happens. The bedroom is smaller "
            "than the main room and considerably more honest about its occupant.\n"
            "Books here are not organized — they are stacked, wedged, balanced, "
            "and in at least one case load-bearing.\n"
            "A narrow bed sits against the far wall, made with the perfunctory "
            "neatness of someone who knows they'll be up again soon.\n"
            "A nightstand holds a pair of wire-rimmed glasses, a half-melted "
            "candle, and a ring left by a cup that was never there long enough "
            "to matter.\n"
            "The rest of the room is Will's business and clearly has been for "
            "a very long time."
        ),
        value=1,
    )
    bedroom.set_flag(ONBIT)
    bedroom.exits["south"] = Exit(destination="WIZARDS-TOWER")
    bedroom.global_objects = ["ENCHANTED-GLASSES", "PAINTING"]
    world.register_room(bedroom)

    # North exit is perception-gated; condition checks world global set by room action
    main.exits["north"] = Exit(
        destination="WIZARDS-BEDROOM",
        condition=lambda w: bool(w.get_global("BEDROOM-DOOR-VISIBLE")),
        fail_message="You can't go that way.",
        message="You push open the bedroom door and step inside.",
    )

    from engine.game import M_NOT_HANDLED, M_ENTER
    from content.perception import EASY

    def tower_action(w, msg=M_NOT_HANDLED):
        if msg == M_ENTER:
            # Silent Easy perception check fires every visit until bedroom found
            if not w.get_global("BEDROOM-DOOR-VISIBLE"):
                from content.player import check_perception
                if check_perception(w, EASY):
                    w.set_global("BEDROOM-DOOR-VISIBLE", True)
                    print("You notice a door to the north you hadn't seen before.")
        return M_NOT_HANDLED

    main.action = tower_action


# ---------------------------------------------------------------------------
# Tale and Ale (Main Room only — enough for the painting portal landing)
# ---------------------------------------------------------------------------

def _make_tale_and_ale(world) -> None:
    r = Room(
        name="TALE-AND-ALE",
        desc="Tale and Ale — Main Room",
        ldesc=(
            "The Tale and Ale announces itself with warmth before you're fully "
            "through the door — woodsmoke, something cooking, the low sound "
            "of people who have decided their evening is going well.\n"
            "Tables fill most of the floor, a mix of occupied and merely claimed. "
            "The bar is south. A staircase climbs to the upper floor. A mailbox "
            "sits near the door, entirely out of place and acknowledged by no one."
        ),
        value=1,
    )
    r.set_flag(ONBIT)
    r.set_flag(RLANDBIT)
    r.global_objects = ["MAILBOX-TOWER"]
    world.register_room(r)
