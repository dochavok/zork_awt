"""
Full-score walkthrough test — v2.

Executes walkthrough_fullscore.txt literally via game.do_turn() only.
No set_room(), no give_item(), no w.globals writes, no or-True guards.

If a command produces wrong output, the engine is wrong — fix the engine.

Run with:
    pytest roundabout/test_walkthrough_fullscore_v2.py -v
or (from c:\\zork_awt\\roundabout):
    python test_walkthrough_fullscore_v2.py
"""

import sys
import os
import re
import io
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

_WALKTHROUGH_PATH = os.path.join(os.path.dirname(__file__), "walkthrough_fullscore.txt")


# ---------------------------------------------------------------------------
# Input feed (same logic as ring test)
# ---------------------------------------------------------------------------

_OPENING_INPUTS = [
    "",         # pause after step 1 mailbox
    "warrior",  # class selection
    "",         # pause after class confirm
    "Tester",   # name entry
    "",         # pause after ring briefing
    "",         # pause after zenni handoff
    "",         # pause after sendoff
]

_EXTRA_PAUSES = [""] * 500


def _make_input_feed():
    seq = _OPENING_INPUTS + _EXTRA_PAUSES
    idx = [0]

    def _feed(prompt=""):
        val = seq[idx[0]] if idx[0] < len(seq) else ""
        idx[0] += 1
        return val

    return _feed


def _always_max(a, b):
    return b


# ---------------------------------------------------------------------------
# Narrative parser (shared logic — identical to ring test)
# ---------------------------------------------------------------------------

class Section:
    def __init__(self, name: str):
        self.name = name
        self.steps: list[tuple[str, str]] = []


def parse_walkthrough(path: str) -> list[Section]:
    sections: list[Section] = []
    current: Section | None = None

    cmd_re = re.compile(r"^>\s+(.+?)(?:\s+\[([^\]]*)\])?\s*$")
    sec_re = re.compile(r"^([A-Z]+[A-Z0-9]*\))\s+(.+)")

    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")

            m = sec_re.match(line)
            if m:
                current = Section(f"{m.group(1)} {m.group(2)}")
                sections.append(current)
                continue

            m = cmd_re.match(line)
            if m and current is not None:
                cmd = m.group(1).strip()
                frag = (m.group(2) or "").strip()
                current.steps.append((cmd, frag))

    return sections


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

class NarrativeRunner:
    def __init__(self, game, world):
        self.game = game
        self.world = world
        self.failures: list[str] = []

    def run_section(self, section: Section) -> None:
        for cmd, frag in section.steps:
            buf = io.StringIO()
            with patch("sys.stdout", buf):
                self.game.do_turn(cmd)
            out = buf.getvalue()
            if frag and frag.lower() not in out.lower():
                self.failures.append(
                    f"SECTION [{section.name}]\n"
                    f"  cmd     : {cmd!r}\n"
                    f"  missing : {frag!r}\n"
                    f"  got     : {out[:300]!r}"
                )

    def run_all(self, sections: list[Section]) -> None:
        for sec in sections:
            self.run_section(sec)

    def report(self, tc: unittest.TestCase) -> None:
        if self.failures:
            tc.fail(
                f"\n{len(self.failures)} walkthrough failure(s):\n\n"
                + "\n\n".join(self.failures)
            )


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

def _make_game():
    from engine.world import World
    from engine.clock import Clock
    from engine.parser import Parser
    from engine.game import Game
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    from content.init import initialize_world

    w = World()
    p = Parser(make_vocabulary(), make_syntax_rules())
    c = Clock()
    g = Game(w, p, c)
    initialize_world(w, g)
    return g, w


class TestFullScoreNarrative(unittest.TestCase):

    def setUp(self):
        self._rand_patch = patch("random.randint", _always_max)
        self._rand_patch.start()

        self._input_feed = _make_input_feed()
        self._input_patch = patch("content.char_create.input", self._input_feed)
        self._input_patch.start()

        self.game, self.world = _make_game()

    def tearDown(self):
        self._rand_patch.stop()
        self._input_patch.stop()

    def test_fullscore_narrative(self):
        sections = parse_walkthrough(_WALKTHROUGH_PATH)
        self.assertTrue(
            sections,
            f"No sections parsed from {_WALKTHROUGH_PATH} — check the file exists and has section headers.",
        )
        runner = NarrativeRunner(self.game, self.world)
        runner.run_all(sections)
        runner.report(self)


if __name__ == "__main__":
    unittest.main(verbosity=2)
