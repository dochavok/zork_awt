from engine.world import World
from engine.clock import Clock
from engine.parser import Parser
from engine.game import Game
from content.vocabulary import make_vocabulary
from content.syntax import make_syntax_rules
from content.init import initialize_world


def main() -> None:
    w = World()
    p = Parser(make_vocabulary(), make_syntax_rules())
    g = Game(w, p, Clock())
    initialize_world(w, g)
    g.run()


if __name__ == "__main__":
    main()
