"""
Quest discovery — every quest is discovered before it's completed, by the
trigger quests.md gives it.

Replays walkthrough_fullscore.txt through game.do_turn() (the full-score
walkthrough test checks its output; this one only watches quest states) and
records, for each quest, the order its states were set and the room the
player was in when it was discovered.

Run with (from c:\\zork_awt\\roundabout):
    py -m pytest test_quest_discovery.py -v
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import test_walkthrough_fullscore_v2 as fullscore
from content import quests

# Organic discoveries: quest -> room the trigger fires in (quests.md — Discovery)
_DISCOVERED_IN = {
    "19": "TOWN-SQUARE",        # LOOK AT STATUE
    "30": "TOWN-SQUARE",
    "34": "TOOL-ALCOVE",        # the speaking door found
    "41": "OLD-OAK",            # the child under the oak
    "42": "VIKING-ENCAMPMENT",  # Ivanaar's request at the runed-metal hand-over
    "51": "BACK-ALLEY",         # entering the alley
    "53": "WIZARDS-TOWER",      # the bedroom door found
    "58": "WIZARDS-BEDROOM",    # the sprig found
    "59": "TALE-AND-ALE",       # TALK TO / CHALLENGE LYNDS
}

_run = None


def _replay():
    """Run the full-score walkthrough once; return (world, history, found_in)."""
    global _run
    if _run is not None:
        return _run
    history: dict[str, list[str]] = {}
    found_in: dict[str, str] = {}
    real_set_state = quests.set_state

    with patch("random.randint", fullscore._always_max), \
            patch("content.char_create.input", fullscore._make_input_feed()):
        g, w = fullscore._make_game()

        def recording_set_state(world, quest_id, state):
            history.setdefault(quest_id, []).append(state)
            if state == quests.DISCOVERED and quest_id not in found_in:
                found_in[quest_id] = world.here.name if world.here else None
            real_set_state(world, quest_id, state)

        with patch.object(quests, "set_state", recording_set_state):
            for section in fullscore.parse_walkthrough(fullscore._WALKTHROUGH_PATH):
                for cmd, _frag in section.steps:
                    with patch("sys.stdout", io.StringIO()):
                        g.do_turn(cmd)
    _run = (w, history, found_in)
    return _run


class TestQuestDiscovery(unittest.TestCase):

    def test_discovered_before_completed(self):
        _w, history, _found = _replay()
        # Board quests (7, 17, 22, 50) are discovered by the walkthrough's two
        # LOOK AT BOARD steps (sections O and U)
        skipped = sorted(
            (q for q, states in history.items() if states[0] == quests.COMPLETE),
            key=int,
        )
        self.assertEqual(skipped, [], f"completed without being discovered: {skipped}")

    def test_organic_discovery_rooms(self):
        _w, _history, found_in = _replay()
        for quest_id, room in _DISCOVERED_IN.items():
            with self.subTest(quest=quest_id):
                self.assertEqual(found_in.get(quest_id), room)

    def test_quests_19_and_30_complete_at_the_werewolf(self):
        w, history, _found = _replay()
        for quest_id in ("19", "30"):
            with self.subTest(quest=quest_id):
                self.assertTrue(quests.is_complete(w, quest_id))
                self.assertEqual(history[quest_id][-1], quests.COMPLETE)


if __name__ == "__main__":
    unittest.main(verbosity=2)
