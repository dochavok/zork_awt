"""
Minimal ring quest walkthrough test — v2.

Executes walkthrough_ring.txt literally via game.do_turn() only.
No set_room(), no give_item(), no w.globals writes, no or-True guards.

If a command produces wrong output, the engine is wrong — fix the engine.

Run with:
    pytest roundabout/test_walkthrough_ring_v2.py -v
or (from c:\\zork_awt\\roundabout):
    python test_walkthrough_ring_v2.py
"""

import sys
import os
import re
import io
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

_WALKTHROUGH_PATH = os.path.join(os.path.dirname(__file__), "walkthrough_ring.txt")


# ---------------------------------------------------------------------------
# Input feed
# ---------------------------------------------------------------------------

# Answers are chosen by prompt text, so the opening can add or reorder
# prompts without breaking the feed. Bare pauses (no prompt) get "".
_PROMPT_ANSWERS = [
    ("adventure", "yes"),       # Will: "Are you up for an adventure?"
    ("warrior/mage/rogue", "warrior"),
    ("your name", "Tester"),
]


def _make_input_feed():
    def _feed(prompt=""):
        p = prompt.lower()
        for key, answer in _PROMPT_ANSWERS:
            if key in p:
                return answer
        return ""

    return _feed


# Random setup (Zenni rooms) is randomized once and fixed for the tests.
# Seed 7 is on the lean side: 8 Zenni by Will's teaching in section D.
_SEED = 7


def _always_max(a, b):
    return b


# ---------------------------------------------------------------------------
# Narrative parser
# ---------------------------------------------------------------------------

class Section:
    def __init__(self, name: str):
        self.name = name
        self.steps: list[tuple[str, str]] = []   # (command, fragment)


def parse_walkthrough(path: str) -> list[Section]:
    """
    Parse the walkthrough .txt file into sections.

    Lines starting with '>' are commands.  The bracketed [fragment] at the
    end is the required output fragment.  Lines starting with '(' are
    input() responses during char creation — they are fed to the input mock
    rather than to do_turn().  Section headers are lines matching /^[A-Z]+\\)/.
    A fragment may list several required pieces separated by "|".
    """
    sections: list[Section] = []
    current: Section | None = None

    # Regex: "> COMMAND   [fragment]" — fragment is optional
    cmd_re = re.compile(r"^>\s+(.+?)(?:\s+\[([^\]]*)\])?\s*$")
    # Section header: one or more capital letters/numbers + closing paren
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
            # "[a|b]" requires every piece to appear in the output
            missing = [f for f in frag.split("|") if f and f.lower() not in out.lower()]
            if missing:
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
    initialize_world(w, g, seed=_SEED)
    return g, w


class TestRingQuestNarrative(unittest.TestCase):

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

    def test_ring_quest_narrative(self):
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
