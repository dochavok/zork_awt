"""Debug script to trace BAG-OF-COINS issue in test_14."""
import io
import sys
from unittest.mock import patch


def _always_max(a, b):
    return b


def _make_game():
    from engine.world import World
    from engine.clock import Clock
    from engine.parser import Parser
    from engine.game import Game
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    from content.init import initialize_world

    world = World()
    parser = Parser(make_vocabulary(), make_syntax_rules())
    game = Game(world, parser, Clock())
    initialize_world(world, game)
    return game


def cmd(game, command):
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        game.do_turn(command)
    out = buf.getvalue()
    print(f">>> {command}")
    if out.strip():
        print(out.rstrip())
    return out


with patch("random.randint", _always_max):
    game = _make_game()
    world = game.world

    buf = io.StringIO()
    with patch("sys.stdout", buf):
        game.enter_room(world.here)

    # Check initial locations
    bag = world.objects.get("BAG-OF-COINS")
    keys = world.objects.get("KEYS")
    maze5 = world.rooms.get("MAZE-5")
    print(f"BAG-OF-COINS initial location: {bag.location.name if bag and bag.location else 'None'}")
    print(f"KEYS initial location: {keys.location.name if keys and keys.location else 'None'}")
    print()

    # Teleport player to Maze-5
    winner = world.winner
    if maze5 and winner:
        world.here = maze5
        print(f"Player teleported to: {world.here.name}")

    # List objects in Maze-5
    print(f"Objects in Maze-5: {[o.name for o in maze5.contents]}")
    print()

    # Try to take coins
    out = cmd(game, "take coins")
    print(f"Bag location after take: {bag.location.name if bag and bag.location else 'None'}")
    print(f"Winner contents: {[o.name for o in winner.contents]}")
    print()

    # Navigate to Cyclops Room
    case_room = world.rooms.get("LIVING-ROOM")
    cyclops_room = world.rooms.get("CYCLOPS-ROOM")
    cyclops = world.objects.get("CYCLOPS")
    if cyclops_room:
        world.here = cyclops_room
        print(f"Player teleported to: {world.here.name}")

    print(f"CYCLOPS-FLAG before: {world.get_global('CYCLOPS-FLAG')}")
    print(f"MAGIC-FLAG before: {world.get_global('MAGIC-FLAG')}")
    out = cmd(game, "Ulysses")
    print(f"CYCLOPS-FLAG after: {world.get_global('CYCLOPS-FLAG')}")
    print(f"MAGIC-FLAG after: {world.get_global('MAGIC-FLAG')}")
    print()

    # Navigate to Strange Passage and Living Room
    out = cmd(game, "go east")
    print(f"Now in: {world.here.name}")
    out = cmd(game, "go east")
    print(f"Now in: {world.here.name}")
    print()

    # Check trophy case
    case = world.objects.get("TROPHY-CASE")
    from engine.world import OPENBIT
    print(f"Trophy case open: {case.has_flag(OPENBIT) if case else 'N/A'}")
    if case:
        case.set_flag(OPENBIT)
        print("Manually opened case")

    # Try put coins in case
    out = cmd(game, "put coins in case")
    print(f"Bag location after put: {bag.location.name if bag and bag.location else 'None'}")
    print(f"Case contains: {[o.name for o in case.contents] if case else 'N/A'}")
    print(f"case_has result: {bag.location is case}")
