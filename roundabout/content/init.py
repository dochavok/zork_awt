"""
World initialization for Roundabout: The God-Forsaken Ring.
Call initialize_world(world, game) once at startup before game.run().
"""

from __future__ import annotations
from engine.world import GameObject
from content.rooms import make_rooms
from content.objects import make_objects
from content.verbs import register_verbs


def initialize_world(world, game) -> None:
    make_rooms(world)
    make_objects(world)
    _make_player(world)
    _init_player_state(world)
    _place_objects(world)
    _wire_whitehouse_action(world, game)
    register_verbs(game)

    # Start in the White House
    world.here = world.rooms["WHITE-HOUSE"]


def _make_player(world) -> None:
    player = GameObject(
        name="PLAYER",
        desc="Adventurer",
        synonyms=["me", "myself", "self"],
    )
    world.register_object(player)
    world.player = player
    world.winner = player


def _init_player_state(world) -> None:
    """
    Player stats use lowercase keys (content/player.py, combat.py, experience.py,
    corruption.py, quests.py). Story/world flags use UPPERCASE-HYPHEN keys.
    Class-dependent values (hearts, skill_*) are set by char_create.
    """
    world.globals.update({
        "hearts": 5,
        "max_hearts": 5,
        "zenni": 0,
        "xp": 0,
        "level": 1,
        "ring_corruption": 0,
        "ring_worn": False,
        "enchanted_glasses_worn": False,
        "actually_enchanted_glasses_worn": False,
    })


def _place_objects(world) -> None:
    world.move_object(world.objects["MAILBOX-WHITE-HOUSE"], world.rooms["WHITE-HOUSE"])
    world.move_object(world.objects["PAINTING"],            world.rooms["WIZARDS-TOWER"])
    world.move_object(world.objects["MAILBOX-TOWER"],       world.rooms["TALE-AND-ALE"])
    world.move_object(world.objects["ENCHANTED-GLASSES"],   world.rooms["WIZARDS-BEDROOM"])
    world.move_object(world.objects["RING"],                world.objects["PYRONICUS"])
    # Mine objects
    world.move_object(world.objects["PICKAXE"],          world.rooms["MAIN-SHAFT"])
    world.move_object(world.objects["PIE-RAT-DISGUISE"], world.rooms["RATS-NEST"])
    world.move_object(world.objects["FLINT-AND-STEEL"],  world.rooms["MINE-TUNNELS"])
    # Shamus sells gunpowder/torch — starts in Kitchen as vendor inventory
    world.move_object(world.objects["GUNPOWDER"], world.rooms["KITCHEN"])
    world.move_object(world.objects["TORCH"],     world.rooms["KITCHEN"])
    # Ship objects
    world.move_object(world.objects["SHOVEL"], world.rooms["SHIP-DECK"])
    world.move_object(world.objects["ROPE"],   world.rooms["DOCKS"])
    # NPCs
    world.move_object(world.objects["SHAMUS"], world.rooms["KITCHEN"])
    world.move_object(world.objects["KEVRY"],  world.rooms["CAPTAINS-QUARTERS"])
    world.move_object(world.objects["PYRONICUS"], world.rooms["PYRONICUS-FORGE"])
    world.move_object(world.objects["WILL"],   world.rooms["WIZARDS-TOWER"])


def _wire_whitehouse_action(world, game) -> None:
    """
    White House: any command except OPEN MAILBOX returns the Zork joke.
    OPEN MAILBOX is handled by the mailbox object action (V-OPEN verb handler).
    """
    from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG

    def whitehouse_action(w, msg=M_BEG):
        if msg == M_BEG:
            # Block all verbs except V-OPEN targeting the mailbox
            if w.prsa == "V-OPEN" and w.prso is not None and w.prso.name == "MAILBOX-WHITE-HOUSE":
                return M_NOT_HANDLED  # let V-OPEN proceed
            if w.prsa not in (None, "V-WALK", "V-LOOK", "V-EXAMINE"):
                print('What does this look like? A Great Underground Empire?')
                return M_HANDLED
        return M_NOT_HANDLED

    world.rooms["WHITE-HOUSE"].action = whitehouse_action
