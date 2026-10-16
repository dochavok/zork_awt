"""
Full-score walkthrough test — v2.

Executes walkthrough_fullscore.txt literally via game.do_turn() only.
No set_room(), no give_item(), no w.globals writes, no or-True guards.
The parser and runner are in walkthrough_runner.py.

If a command produces wrong output, the engine is wrong — fix the engine.

Run with:
    pytest roundabout/test_walkthrough_fullscore_v2.py -v
or (from c:\\zork_awt\\roundabout):
    python test_walkthrough_fullscore_v2.py
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import walkthrough_runner as wt

# experience.md — Exploration total: room XP paid over a run that enters every room.
_EXPLORATION_XP = 167


class TestFullScoreNarrative(wt.WalkthroughTestCase):

    def test_fullscore_narrative(self):
        # The full-score run enters every room worth XP. Entries are
        # recorded by an enter hook — some rooms reset room.visited to force
        # their full description, so the flag alone can't be trusted.
        entered = {self.world.here.name}
        room_xp_start = sum(r.value for r in self.world.rooms.values())
        self.game.register_enter_hook(lambda w, room: entered.add(room.name))

        runner = self.run_walkthrough(wt.FULLSCORE_PATH)

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
