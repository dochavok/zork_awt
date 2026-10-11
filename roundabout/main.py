from engine.world import World
from engine.clock import Clock
from engine.parser import Parser
from engine.game import Game
from content.vocabulary import make_vocabulary
from content.syntax import make_syntax_rules
from content.init import initialize_world


def main() -> None:
    while True:                     # RESTART builds a fresh game from scratch
        w = World()
        p = Parser(make_vocabulary(), make_syntax_rules())
        g = Game(w, p, Clock())
        initialize_world(w, g)
        g.run()
        if not g.restart_requested:
            break


if __name__ == "__main__":
    main()
