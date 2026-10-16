"""
Minimal ring quest walkthrough test — v2.

Executes walkthrough_ring.txt literally via game.do_turn() only.
No set_room(), no give_item(), no w.globals writes, no or-True guards.
The parser and runner are in walkthrough_runner.py.

If a command produces wrong output, the engine is wrong — fix the engine.

Run with:
    pytest roundabout/test_walkthrough_ring_v2.py -v
or (from c:\\zork_awt\\roundabout):
    python test_walkthrough_ring_v2.py
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import walkthrough_runner as wt


class TestRingQuestNarrative(wt.WalkthroughTestCase):

    def test_ring_quest_narrative(self):
        self.run_walkthrough(wt.RING_PATH).report(self)


if __name__ == "__main__":
    unittest.main(verbosity=2)
