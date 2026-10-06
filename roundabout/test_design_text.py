"""
Text the tests take from the code must be the design's text.

Many tests assert against the code's own text constants (e.g. may_hints._Q32)
instead of copying every line into the test. That only tests the design if
those constants are the design's words. This test checks each one appears
verbatim in AWT_story_line/*.md (ignoring markdown emphasis and line breaks;
{placeholders} are checked piece by piece; the engine's GAME OVER banner is
not design text).

When a constant changes, update the design file first — or this fails.
Run with: pytest roundabout/test_design_text.py  (from c:\\zork_awt)
"""

import glob
import importlib
import os
import re
import pytest

_DOCS = os.path.join(os.path.dirname(__file__), "..", "AWT_story_line", "*.md")


def _norm(s):
    s = s.replace("*** GAME OVER ***", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


_DESIGN = _norm(" ".join(_read(f) for f in glob.glob(_DOCS)))

# (content module, constant) — every text constant a test asserts against
USED_BY_TESTS = [
    ("aqueduct", "_NO_MORTAR"),
    ("aqueduct", "_SEALED"),
    ("back_alley", "_ROUND_TIE"),
    ("back_alley", "_ROUND_WON"),
    ("cargo", "_CHOOSE"),
    ("cargo", "_CLEANED_OUT"),
    ("cargo", "_CLOSED"),
    ("cargo", "_INTRO"),
    ("cargo", "_LOSE"),
    ("cargo", "_PUSH"),
    ("cargo", "_SHORT"),
    ("cargo", "_STAKE_FIRST"),
    ("cargo", "_TY_ALL_AT_ONCE"),
    ("cargo", "_TY_FAILS"),
    ("cargo", "_TY_HIGH"),
    ("cargo", "_TY_REROLLS_BOTH"),
    ("cargo", "_TY_SIX_ON_TWO"),
    ("cargo", "_WIN"),
    ("combat", "_FINISH_LINES"),
    ("combat", "_TUNIC_LINES"),
    ("combat_room", "_ROUND_LOST"),
    ("flooding", "_LEFT"),
    ("knight", "BOW_REFUSED"),
    ("light", "_BURNOUT_FATAL"),
    ("light", "_BURNOUT_SAFE"),
    ("light", "_WARNINGS"),
    ("may_hints", "_NOTHING"),
    ("may_hints", "_Q17_AFTER"),
    ("may_hints", "_Q17_BEFORE"),
    ("may_hints", "_Q17_CHARTER"),
    ("may_hints", "_Q19"),
    ("may_hints", "_Q19_STATUE"),
    ("may_hints", "_Q24"),
    ("may_hints", "_Q25"),
    ("may_hints", "_Q27"),
    ("may_hints", "_Q32"),
    ("may_hints", "_Q32_CART"),
    ("may_hints", "_Q34"),
    ("may_hints", "_Q4"),
    ("may_hints", "_Q42"),
    ("may_hints", "_Q49"),
    ("may_hints", "_Q59"),
    ("ship", "_CREW_ABOARD"),
    ("ship", "_NO_COIN"),
    ("ship", "_NO_DISGUISE"),
    ("shrine_bowl", "_MIXED"),
    ("shrine_bowl", "_NO_WATER"),
    ("still_den", "_BOW_FAILS"),
    ("verbs", "_UNTRAINED"),
    ("whispering_jar", "_NO_JAR_SEAL")
]


def _strings(value):
    if isinstance(value, dict):
        value = list(value.values())
    if not isinstance(value, (list, tuple)):
        value = [value]
    return [s for s in value if isinstance(s, str) and len(s) >= 20]


@pytest.mark.parametrize("module,name", USED_BY_TESTS)
def test_constant_is_design_text(module, name):
    value = getattr(importlib.import_module(f"content.{module}"), name)
    for text in _strings(value):
        for piece in re.split(r"\{[^}]*\}", text):
            piece = _norm(piece)
            if len(piece) >= 15:
                assert piece in _DESIGN, f"{module}.{name} is not in the design docs: {piece!r}"
