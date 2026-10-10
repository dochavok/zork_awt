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
# Seed 7 gives 35 Zenni by Will's first teaching in section F.
_SEED = 7

# experience.md — Exploration total: room XP paid over a run that enters every room.
_EXPLORATION_XP = 167


def _always_max(a, b):
    return b


# The parser's generic refusals — never what a walkthrough step is for.
_REFUSALS = (
    "You can't see any ",
    "I don't know the word",
    "That sentence isn't one I recognize.",
    "I beg your pardon?",
    "You can't go that way.",
    "A Great Underground Empire?",
    "You aren't holding the",
    "You don't have enough Zenni",
)


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
            # "[a|b]" requires every piece to appear in the output
            missing = [f for f in frag.split("|") if f and f.lower() not in out.lower()]
            if missing:
                self.failures.append(
                    f"SECTION [{section.name}]\n"
                    f"  cmd     : {cmd!r}\n"
                    f"  missing : {frag!r}\n"
                    f"  got     : {out[:300]!r}"
                )
            # A refusal can still hold the fragment ("You can't see any ring
            # here!" holds "ring"), so a refused step fails unless its fragment
            # asks for the refusal.
            refused = [r for r in _REFUSALS if r in out and r.lower() not in frag.lower()]
            if refused:
                self.failures.append(
                    f"SECTION [{section.name}]\n"
                    f"  cmd     : {cmd!r}\n"
                    f"  refused : {refused[0]!r}\n"
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
        # The full-score run enters every room worth XP. Entries are
        # recorded by an enter hook — some rooms reset room.visited to force
        # their full description, so the flag alone can't be trusted.
        entered = {self.world.here.name}
        room_xp_start = sum(r.value for r in self.world.rooms.values())
        self.game.register_enter_hook(lambda w, room: entered.add(room.name))

        runner = NarrativeRunner(self.game, self.world)
        runner.run_all(sections)

        missed = sorted(n for n, r in self.world.rooms.items()
                        if r.value > 0 and n not in entered)
        if missed:
            runner.failures.append(
                "ROOM COVERAGE — rooms worth XP never entered:\n  " + ", ".join(missed)
            )
        # Entering a room pays its XP and zeroes room.value (engine/game.py)
        room_xp_paid = room_xp_start - sum(r.value for r in self.world.rooms.values())
        if room_xp_start != _EXPLORATION_XP or room_xp_paid != _EXPLORATION_XP:
            runner.failures.append(
                f"EXPLORATION XP — design total {_EXPLORATION_XP}, engine rooms total "
                f"{room_xp_start}, paid in the run {room_xp_paid}"
            )
        runner.report(self)


if __name__ == "__main__":
    unittest.main(verbosity=2)
