"""Quick debug script to trace the jade deposit failure in test_14."""
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


def cmd(game, command, verbose=False):
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        game.do_turn(command)
    out = buf.getvalue()
    if verbose or True:
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

    # Quick navigation to Living Room via standard route
    def c(command):
        return cmd(game, command)

    # Standard start
    c("go south"); c("go east"); c("open window"); c("enter house")
    c("go west"); c("take lamp"); c("move rug"); c("open trap door")
    c("turn on lamp"); c("go down"); c("go north"); c("take lantern")

    # Actually, let me use a shortcut - teleport player to Living Room
    # and set up game state manually for testing jade deposit

    print("\n--- Shortcut: teleporting to Living Room with jade ---")
    winner = world.winner
    living_room = world.rooms.get("LIVING-ROOM")
    jade = world.objects.get("JADE-FIGURINE")
    case = world.objects.get("TROPHY-CASE")

    print(f"Living Room: {living_room}")
    print(f"Jade: {jade}")
    print(f"Case: {case}")

    if jade and winner:
        world.move_object(jade, winner)
        print(f"Jade location after move: {jade.location}")
        print(f"Jade in winner's contents: {jade in winner.contents}")

    if living_room and winner:
        world.here = living_room
        print(f"Player now in: {world.here.name}")

    if case:
        from engine.world import OPENBIT
        case.set_flag(OPENBIT)
        print(f"Case flags after open: {case.flags}")
        print(f"Case has OPENBIT: {case.has_flag(OPENBIT)}")

    # Now try put jade in case
    print("\n--- Attempting 'put jade in case' ---")
    out = cmd(game, "put jade in case")
    print(f"Result: {out!r}")

    jade_loc = jade.location if jade else None
    print(f"Jade location after put: {jade_loc}")
    print(f"Case has jade: {jade_loc is case}")
