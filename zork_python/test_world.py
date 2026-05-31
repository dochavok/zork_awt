"""Smoke tests for engine/world.py."""

from engine.world import (
    World, Room, GameObject, Exit,
    TAKEBIT, CONTBIT, OPENBIT, ONBIT, TRANSBIT, NDESCBIT,
)


def test_basic_room_and_object():
    w = World()

    kitchen = Room("KITCHEN", "Kitchen", ldesc="A tidy kitchen.")
    w.register_room(kitchen)

    bottle = GameObject("BOTTLE", synonyms=["bottle"], desc="glass bottle",
                        flags={CONTBIT, OPENBIT}, capacity=20)
    water  = GameObject("WATER",  synonyms=["water"], desc="quantity of water",
                        flags={TAKEBIT}, size=4)
    w.register_object(bottle)
    w.register_object(water)

    w.move_object(bottle, kitchen)
    w.move_object(water,  bottle)

    assert bottle in kitchen.contents
    assert water  in bottle.contents
    assert water.containing_room() is kitchen
    print("PASS: basic room and object placement")


def test_move_object_updates_old_location():
    w = World()
    room_a = Room("ROOM-A", "Room A")
    room_b = Room("ROOM-B", "Room B")
    w.register_room(room_a)
    w.register_room(room_b)

    sword = GameObject("SWORD", synonyms=["sword"], desc="rusty sword", flags={TAKEBIT})
    w.register_object(sword)

    w.move_object(sword, room_a)
    assert sword in room_a.contents

    w.move_object(sword, room_b)
    assert sword not in room_a.contents
    assert sword in room_b.contents
    print("PASS: move_object clears old location")


def test_place_object_by_name():
    w = World()
    room = Room("LIVING-ROOM", "Living Room")
    lamp  = GameObject("LAMP", synonyms=["lamp", "lantern"], desc="brass lantern",
                       flags={TAKEBIT, ONBIT})
    w.register_room(room)
    w.register_object(lamp)

    w.place_object("LAMP", "LIVING-ROOM")
    assert lamp in room.contents
    print("PASS: place_object by name")


def test_is_accessible_in_room():
    w = World()
    room = Room("CELLAR", "Cellar")
    w.register_room(room)
    w.here = room

    player = GameObject("PLAYER", synonyms=["me"], desc="yourself")
    w.register_object(player)
    w.player = player
    w.winner = player

    sword = GameObject("SWORD", synonyms=["sword"], desc="elvish sword", flags={TAKEBIT})
    w.register_object(sword)
    w.move_object(sword, room)

    assert w.is_accessible(sword)
    print("PASS: object in current room is accessible")


def test_is_accessible_in_inventory():
    w = World()
    room = Room("CELLAR", "Cellar")
    w.register_room(room)
    w.here = room

    player = GameObject("PLAYER", synonyms=["me"], desc="yourself",
                        flags={CONTBIT, OPENBIT}, capacity=100)
    w.register_object(player)
    w.player = player
    w.winner = player
    w.move_object(player, room)

    lamp = GameObject("LAMP", synonyms=["lamp"], desc="brass lantern", flags={TAKEBIT})
    w.register_object(lamp)
    w.move_object(lamp, player)

    assert w.is_accessible(lamp)
    print("PASS: carried object is accessible")


def test_is_accessible_global():
    w = World()
    forest = Room("FOREST", "Forest", global_objects=["TREE"])
    w.register_room(forest)
    w.here = forest

    player = GameObject("PLAYER", synonyms=["me"], desc="yourself")
    w.register_object(player)
    w.player = player

    tree = GameObject("TREE", synonyms=["tree"], desc="large tree", flags={NDESCBIT})
    w.register_object(tree)

    assert w.is_accessible(tree)
    print("PASS: global object is accessible from room")


def test_lighting_lit_room():
    w = World()
    room = Room("CLEARING", "Clearing", flags={ONBIT})
    w.register_room(room)
    w.here = room
    assert w.is_lit()
    print("PASS: outdoor room with ONBIT is lit")


def test_lighting_lamp_in_inventory():
    w = World()
    room = Room("CAVE", "Cave")  # no ONBIT
    w.register_room(room)
    w.here = room

    player = GameObject("PLAYER", synonyms=["me"], desc="yourself",
                        flags={CONTBIT, OPENBIT}, capacity=100)
    w.register_object(player)
    w.player = player
    w.move_object(player, room)

    lamp = GameObject("LAMP", synonyms=["lamp"], desc="brass lantern",
                      flags={TAKEBIT, ONBIT})
    w.register_object(lamp)
    w.move_object(lamp, player)

    assert w.is_lit()
    print("PASS: dark room is lit when player carries lit lamp")


def test_exit_unconditional():
    w = World()
    room_a = Room("ROOM-A", "Room A", exits={"north": Exit(destination="ROOM-B")})
    room_b = Room("ROOM-B", "Room B")
    w.register_room(room_a)
    w.register_room(room_b)

    dest, msg = room_a.exits["north"].resolve(w)
    assert dest is room_b
    assert msg is None
    print("PASS: unconditional exit resolves correctly")


def test_exit_blocked_message():
    w = World()
    room = Room("ROOM-A", "Room A",
                exits={"east": Exit(message="The door is boarded shut.")})
    w.register_room(room)

    dest, msg = room.exits["east"].resolve(w)
    assert dest is None
    assert msg == "The door is boarded shut."
    print("PASS: blocked exit returns message")


def test_exit_conditional_pass():
    w = World()
    window = GameObject("KITCHEN-WINDOW", synonyms=["window"], desc="kitchen window",
                        flags={OPENBIT})
    w.register_object(window)

    room_a = Room("EAST-OF-HOUSE", "Behind House", exits={
        "west": Exit(
            destination="KITCHEN",
            condition=lambda world: world.flag_set("KITCHEN-WINDOW", OPENBIT),
            fail_message="The window is closed.",
        )
    })
    kitchen = Room("KITCHEN", "Kitchen")
    w.register_room(room_a)
    w.register_room(kitchen)

    dest, msg = room_a.exits["west"].resolve(w)
    assert dest is kitchen
    print("PASS: conditional exit passes when condition is true")


def test_exit_conditional_fail():
    w = World()
    window = GameObject("KITCHEN-WINDOW", synonyms=["window"], desc="kitchen window")
    # no OPENBIT
    w.register_object(window)

    room_a = Room("EAST-OF-HOUSE", "Behind House", exits={
        "west": Exit(
            destination="KITCHEN",
            condition=lambda world: world.flag_set("KITCHEN-WINDOW", OPENBIT),
            fail_message="The window is closed.",
        )
    })
    kitchen = Room("KITCHEN", "Kitchen")
    w.register_room(room_a)
    w.register_room(kitchen)

    dest, msg = room_a.exits["west"].resolve(w)
    assert dest is None
    assert msg == "The window is closed."
    print("PASS: conditional exit blocked when condition is false")


if __name__ == "__main__":
    test_basic_room_and_object()
    test_move_object_updates_old_location()
    test_place_object_by_name()
    test_is_accessible_in_room()
    test_is_accessible_in_inventory()
    test_is_accessible_global()
    test_lighting_lit_room()
    test_lighting_lamp_in_inventory()
    test_exit_unconditional()
    test_exit_blocked_message()
    test_exit_conditional_pass()
    test_exit_conditional_fail()
    print("\nAll tests passed.")
