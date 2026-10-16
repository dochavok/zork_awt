import sys

from engine.world import World
from engine.clock import Clock
from engine.parser import Parser
from engine.game import Game
from content.vocabulary import make_vocabulary
from content.syntax import make_syntax_rules
from content.init import initialize_world


def _utf8_output() -> None:
    """Piped, Python writes the Windows code page and em-dashes come out as "�"
    (mechanics.md — The end of the game; TODO #25). A console is UTF-8 already."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main() -> None:
    _utf8_output()
    while True:                     # RESTART builds a fresh game from scratch
        w = World()
        p = Parser(make_vocabulary(), make_syntax_rules())
        g = Game(w, p, Clock())
        initialize_world(w, g)
        try:
            g.run()
        except (EOFError, KeyboardInterrupt):
            # Input ended (or Ctrl+C) at a prompt the main loop doesn't own — the
            # opening's questions, a [Press ENTER] pause: end quietly, as the
            # > prompt does (TODO #25)
            print()
            break
        if not g.restart_requested:
            break


if __name__ == "__main__":
    main()
