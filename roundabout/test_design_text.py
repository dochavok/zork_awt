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
    ("altar", "ALTAR_EAST"),
    ("aqueduct", "_BACK_NORTH"),
    ("aqueduct", "_BLOCKS_STATE"),
    ("aqueduct", "CHANNEL_ENDS"),
    ("aqueduct", "_CROWBAR_WONT"),
    ("aqueduct", "_FLOOD"),
    ("aqueduct", "_GALLERY_BACK_NORTH"),
    ("aqueduct", "_GALLERY_CLEARED"),
    ("aqueduct", "_NO_MORTAR"),
    ("aqueduct", "_NO_TIMBERS"),
    ("aqueduct", "_PLACED"),
    ("aqueduct", "_SEALED"),
    ("aqueduct", "_SLIPS"),
    ("aqueduct", "_STILL_GAP"),
    ("aqueduct", "_TIMBER_DOWN"),
    ("aqueduct", "_TIMBERS"),
    ("aqueduct", "_TOO_HEAVY"),
    ("aqueduct", "_WHOLE"),
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
    ("cellar", "_BONE_DOOR_SEEP"),
    ("cellar", "_DROWN_STAIRS"),
    ("cellar", "_DROWN_TUNNEL"),
    ("cellar", "_MAY_BOOTS"),
    ("cellar", "_MAY_KEY"),
    ("combat", "_FINISH_LINES"),
    ("combat", "_TUNIC_LINES"),
    ("dark_branch", "_BLOCKED"),
    ("dark_branch", "_SPIRITS_IGNORE"),
    ("dark_branch", "_SPIRITS_SEE"),
    ("dark_branch", "_TRAPPED_BOUND"),
    ("dark_branch", "_TRAPPED_END"),
    ("dark_branch", "_TRAPPED_INKED"),
    ("dark_branch", "_TRAPPED_NO_RING"),
    ("combat_room", "_BELL"),
    ("combat_room", "_DEN_BASE"),
    ("combat_room", "_DEN_NORTH"),
    ("combat_room", "_DEN_SEALED"),
    ("combat_room", "_DODGE"),
    ("combat_room", "_DOOR_OPEN"),
    ("combat_room", "_DOOR_WONT_CLOSE"),
    ("combat_room", "DOOR_EXAMINE"),
    ("combat_room", "_SLIP_PAST"),
    ("combat_room", "WARDEN_BLOCKS"),
    ("combat_room", "_ROUND_LOST"),
    ("combat_room", "_TRIGGER"),
    ("combat_room", "PLATE_EXAMINE"),
    ("combat_room", "_WARDEN_EMERGES"),
    ("combat_room", "WARDEN_PRESENCE"),
    ("char_create", "_PAUSE_CUE"),
    ("flooding", "_LEFT"),
    ("flooding", "DEN_SEALED"),
    ("flooding", "LEVERS_EXAMINE"),
    ("flooding", "PLATE_EXAMINE"),
    ("flooding", "SLUICE_POURING"),
    ("flooding", "SLUICE_STOPPED"),
    ("flooding", "_MIDDLE"),
    ("flooding", "_RIGHT"),
    ("flooding", "_ROOM"),
    ("flooding", "_ROOM_FIRST"),
    ("flooding", "_SLAB"),
    ("flooding", "_SPENT"),
    ("flooding", "_STUMP"),
    ("flooding", "_SWEPT"),
    ("flooding", "_TRIGGER"),
    ("flooding", "_URGENCY"),
    ("flooding", "_WATER_ENTRY"),
    ("flooding", "_WATER_RISEN"),
    ("flooding", "_WATER_RISEN_STILL"),
    ("flooding", "_WATER_STILL"),
    ("frozen_soldier", "_NO_HEAT"),
    ("frozen_soldier", "_PLAIN_TORCH_LIT"),
    ("frozen_soldier", "_THAW_1"),
    ("gravestone", "LISTING_MUD"),
    ("gravestone", "_LISTING_GROUND"),
    ("gravestone", "_LOADED"),
    ("gravestone", "_NO_STAIRS"),
    ("gravestone", "_PLACED"),
    ("gravestone", "_ROWAN_AFTER"),
    ("gravestone", "_ROWAN_FIRST"),
    ("gravestone", "_ROWAN_START"),
    ("gravestone", "_ROWAN_TROPHY"),
    ("gravestone", "_ROWAN_WAITING"),
    ("gravestone", "_TIPPED_OFF"),
    ("inscription", "_HANGING"),
    ("inscription", "DEEP_LOCK_SOUTH"),
    ("inscription", "DEEP_LOCK_EXAMINE"),
    ("inscription", "_DEEP_LOCK_PICK"),
    ("inscription", "_DOOR_SHUT"),
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
    ("quest_board", "POSTINGS"),
    ("ship", "_CREW_ABOARD"),
    ("ship", "_NO_COIN"),
    ("ship", "_NO_DISGUISE"),
    ("kevry", "_CARRIED"),
    ("kevry", "_FIRST_SEEN"),
    ("kevry", "_QUARTERS"),
    ("kevry", "_SEEN_AGAIN"),
    ("kevry", "_SEEN_ENCHANTED"),
    ("mine", "SHAFT_UP_BURIED"),
    ("mine", "SHAFT_UP_OPEN"),
    ("mine", "_BURIED"),
    ("mine", "_BURIED_UP"),
    ("mine", "_FUSE_BURNING"),
    ("mine", "_LIT"),
    ("mine", "_NO_FLINT"),
    ("mine", "_TORCH_NO"),
    ("notorious", "_CURSE"),
    ("notorious", "_FINE"),
    ("notorious", "_LEDGER"),
    ("notorious", "_NOTORIOUS"),
    ("notorious", "_PAID"),
    ("notorious", "STANDING"),
    ("notorious", "SURE_PROMPT"),
    ("pond", "BOTTLE_IN_POND"),
    ("rest", "_RESTED"),
    ("search", "NOTHING"),
    ("search", "_LEAD_IN"),
    ("shrine_bowl", "_ALREADY_PLACED"),
    ("shrine_bowl", "_ASSEMBLED"),
    ("shrine_bowl", "_BARE"),
    ("shrine_bowl", "_BOWL_PLACED"),
    ("shrine_bowl", "_JUST_A_COIN"),
    ("shrine_bowl", "_MISSING_PIECES"),
    ("shrine_bowl", "_MIXED"),
    ("shrine_bowl", "_NOT_THIS_SHRINE"),
    ("shrine_bowl", "_NO_WATER"),
    ("shrine_bowl", "_ON_PEDESTAL_CRYSTAL"),
    ("shrine_bowl", "_ON_PEDESTAL_REPAIRED"),
    ("shrine_bowl", "_PEDESTAL"),
    ("shrine_bowl", "PLINTH"),
    ("shrine_bowl", "_PRAY_BROKEN"),
    ("shrine_bowl", "_PRAY_DONE"),
    ("shrine_bowl", "_PRAY_PLACED"),
    ("shrine_bowl", "_REMAINS"),
    ("shrine_bowl", "_TRANSFORMED"),
    ("rooms", "LIGHTHOUSE_CHAIN"),
    ("rooms", "BEDROOM_DOOR_FOUND"),
    ("rooms", "BEDROOM_DOOR_STAYS"),
    ("rooms", "ALLEY_NORTH"),
    ("rooms", "BACK_ALLEY_SOUTH"),
    ("rooms", "SEA_WEST_NORTH"),
    ("ship", "DECK_AT_DOCKS"),
    ("ship", "DECK_OFF_ISLAND"),
    ("aqueduct", "_TIMBERS_LEFT"),
    ("scenery", "BEDROLLS"),
    ("scenery", "CRATES"),
    ("scenery", "CRATES_SEARCH"),
    ("scenery", "ENTRANCE_CEILING"),
    ("scenery", "EQUIPMENT"),
    ("scenery", "JOURNALS"),
    ("scenery", "JOURNALS_STAY"),
    ("scenery", "MIRROR_BREAK"),
    ("scenery", "MIRROR_TOUCH"),
    ("scenery", "MIRRORS_FREED"),
    ("scenery", "MIRRORS_SEEN"),
    ("scenery", "MIRRORS_UNSEEN"),
    ("scenery", "RUBBLE"),
    ("scenery", "RUBBLE_CLIMB"),
    ("scenery", "RUBBLE_SEARCH"),
    ("scenery", "ROOM_MIRRORS"),
    ("scenery", "RUNNER"),
    ("scenery", "STOOL"),
    ("scenery", "ALLEY_MUGGER"),
    ("scenery", "ALLEY_QUIET"),
    ("scenery", "ALTAR_EXAMINE"),
    ("scenery", "CATALOGUE"),
    ("scenery", "CATALOGUE_CARD"),
    ("scenery", "DIAL"),
    ("scenery", "DIAL_GLOW"),
    ("scenery", "FLOORBOARDS"),
    ("scenery", "FOUNTAIN_DRY"),
    ("scenery", "FOUNTAIN_RUNNING"),
    ("scenery", "HALL_DOORS"),
    ("scenery", "LEDGER"),
    ("scenery", "SHELVES"),
    ("scenery", "TOWER_DESK"),
    ("scenery", "TOWER_PAPERS_ALONE"),
    ("scenery", "TOWER_PAPERS_WILL"),
    ("scenery", "VIEWS"),
    ("scenery", "WINDOW_SHUT"),
    ("shrine_path", "BRIDGE_WEST_SHUT"),
    ("tavern", "DOOR_OUT"),
    ("tavern", "ROOMS_RENTED"),
    ("shrine_path", "_LIFT_FAILS"),
    ("shrine_path", "_LIFTED"),
    ("mid_tier", "_ROPE_STAYS"),
    ("mid_tier", "_NOTHING_TO_TIE"),
    ("mid_tier", "_HOLE_EXITS"),
    ("mid_tier", "CREVICE_EAST"),
    ("objects", "HANGING_ROPE_EXAMINE"),
    ("objects", "CHARTER_TEXT"),
    ("objects", "GLASSES_EXAMINE"),
    ("objects", "GLASSES_EXAMINE_ENCHANTED"),
    ("objects", "LIGHTHOUSE_DESK"),
    ("objects", "LIGHTHOUSE_LOG"),
    ("objects", "LIGHTHOUSE_STONE"),
    ("objects", "LIGHTHOUSE_STONE_STAYS"),
    ("shrine_path", "_PORT_EXITS_OPEN"),
    ("shrine_path", "_PORT_EXITS_SHUT"),
    ("shrine_path", "_PROPPED"),
    ("shrine_path", "_PROPPED_FROM_SOUTH"),
    ("shrine_path", "_DOWN"),
    ("shrine_path", "_DROPS"),
    ("shrine_path", "_DROP_FIRST"),
    ("shrine_path", "_KEY_DOOR_BACK"),
    ("shrine_path", "_SHOCK"),
    ("shrine_path", "_RETRY_DISARMED"),
    ("shrine_path", "_RETRY_FAILS"),
    ("shrine_path", "_UNSPOTTED"),
    ("shrine_path", "_NOTHING_LEFT"),
    ("shrine_path", "_EX_CHARGED"),
    ("shrine_path", "_EX_MECHANISM_SEEN"),
    ("shrine_path", "_EX_DISCHARGED"),
    ("shrine_path", "_EX_MECHANISM"),
    ("shrine_path", "_EX_LEVER_DOWN"),
    ("statue", "_PRIED"),
    ("still_den", "_BOW_FAILS"),
    ("still_den", "_MISSES"),
    ("still_den", "_NARROW_PASS"),
    ("still_den", "_NARROW_PASS_QUIET"),
    ("trap_side", "APPRENTICE_AFFLICTED"),
    ("trap_side", "APPRENTICE_ATTACKS"),
    ("trap_side", "APPRENTICE_UNAWARE"),
    ("trap_side", "APPRENTICE_UNSEEING"),
    ("trap_side", "_DIGS_THROUGH"),
    ("trap_side", "_DIG_BLOCKED"),
    ("trap_side", "_DUG"),
    ("trap_side", "_FAREWELL"),
    ("trap_side", "_FREED"),
    ("trap_side", "_GLOVES_ADDED"),
    ("trap_side", "_NOT_THROUGH"),
    ("trap_side", "_SURFACE"),
    ("trap_side", "_CELL"),
    ("trap_side", "_CELL_DUG"),
    ("tunnels", "_BLOCKED"),
    ("tunnels", "_SEES_YOU"),
    ("tunnels", "_BRIDGE"),
    ("tunnels", "_BRIDGE_BOGGART"),
    ("tunnels", "_BRIDGE_LOOTED"),
    ("tunnels", "_BRIDGE_STRONGBOX"),
    ("tunnels", "_PAY_REFUSED"),
    ("tunnels", "_TOLL"),
    ("upper_tier", "SLAB_BLOCKS"),
    ("upper_tier", "_SUPPLY_DISARMED"),
    ("upper_tier", "_SUPPLY_FIRED"),
    ("upper_tier", "_TRAP17"),
    ("upper_tier", "_STORAGE_BEAM"),
    ("upper_tier", "STORAGE_EAST"),
    ("upper_tier", "_STORAGE_BOTH"),
    ("upper_tier", "_STORAGE_CART"),
    ("upper_tier", "_STORAGE_NONE"),
    ("upper_tier", "_IDOL_SPOTTED"),
    ("upper_tier", "_PLATE_FIRED"),
    ("upper_tier", "_PLATE_SALTED"),
    ("upper_tier", "_LIFT_BARE"),
    ("upper_tier", "_NOT_BLOCKED"),
    ("upper_tier", "_PRIED"),
    ("upper_tier", "_PRY_FAILED"),
    ("upper_tier", "_SLAB_DOWN"),
    ("verbs", "_IVORY_HEAT"),
    ("verbs", "_JUST_GO"),
    ("verbs", "_LITLOCK_OPEN"),
    ("verbs", "_LITLOCK_UNKNOWN"),
    ("verbs", "_RELOCK"),
    ("verbs", "_UNPICKABLE"),
    ("verbs", "_IDOL_NUDGED"),
    ("verbs", "_ICE_WINS"),
    ("verbs", "_NO_STAKE_TARGET"),
    ("verbs", "_ALREADY_HOLDING"),
    ("verbs", "_NOTHING_NEEDS_PROPPING"),
    ("verbs", "_NOTHING_TO_PROP_WITH"),
    ("verbs", "_ONLY_MAY"),
    ("verbs", "_WHICH_WAY"),
    ("mid_tier", "_CHEST_LOCKED"),
    ("mid_tier", "_CHEST_PICKED"),
    ("verbs", "_LOWER_TIED"),
    ("verbs", "_LOWER_UNTIED"),
    ("bedroom", "NOTHING_UNDER"),
    ("bedroom", "SPRIG_FOUND"),
    ("bedroom", "SPRIG_LDESC"),
    ("bedroom", "UNDER_BED"),
    ("init", "WHITE_HOUSE_KNOCK"),
    ("ink", "LITLOCK_DOOR"),
    ("tool_alcove", "_ASKS"),
    ("tool_alcove", "_BACK_SOUTH"),
    ("verbs", "_LANTERN_NOT_HELD"),
    ("verbs", "_LANTERN_STAYS_LIT"),
    ("verbs", "_TORCH_STAYS_LIT"),
    ("verbs", "_PRAY"),
    ("ways", "ARCH"),
    ("ways", "ENTER_WHAT"),
    ("ways", "LOOK_AROUND"),
    ("ways", "_ONLY"),
    ("ways", "UP_OR_DOWN"),
    ("verbs", "_LAND_PROMPT"),
    ("verbs", "_NO_PLACE_TO_LAND"),
    ("verbs", "_PRAY_CHURCH"),
    ("verbs", "_RESTART_PROMPT"),
    ("verbs", "_UNTRAINED"),
    ("verbs", "_WHICH_DIRECTION"),
    ("vikings", "_IVANAAR_STATES"),
    ("whispering_jar", "_ALREADY_SEALED"),
    ("whispering_jar", "_NO_FILL"),
    ("whispering_jar", "_NO_JAR_SEAL"),
    ("whispering_jar", "_PRESS"),
]

# Imported by tests but not design text (the guard below skips them)
NOT_DESIGN_TEXT = {
    ("zenni_rooms", "ELIGIBLE_ROOMS"),   # room names, not text
    ("vikings", "_RIDDLE"),              # the design's riddle with "Haalvar says: " in front
}


def _strings(value):
    """Every text in a constant — nested dicts, lists and tuples too (a dict of
    tuples used to yield nothing, so it passed unchecked)."""
    if isinstance(value, str):
        return [value] if len(value) >= 20 else []
    if isinstance(value, dict):
        value = list(value.values())
    if isinstance(value, (list, tuple)):
        return [s for v in value for s in _strings(v)]
    return []


@pytest.mark.parametrize("module,name", USED_BY_TESTS)
def test_constant_is_design_text(module, name):
    value = getattr(importlib.import_module(f"content.{module}"), name)
    for text in _strings(value):
        for piece in re.split(r"\{[^}]*\}", text):
            piece = _norm(piece)
            if len(piece) >= 15:
                assert piece in _DESIGN, f"{module}.{name} is not in the design docs: {piece!r}"


def _imported_text_constants():
    """(module, name) for every `from content.<module> import <name>` in a test
    file whose value is text. (Attribute access — may_hints._Q32 — isn't seen.)"""
    import ast
    here = os.path.dirname(__file__)
    found = set()
    for path in glob.glob(os.path.join(here, "test_*.py")):
        for node in ast.walk(ast.parse(_read(path))):
            if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("content."):
                module = node.module.split(".", 1)[1]
                for alias in node.names:
                    value = getattr(importlib.import_module(node.module), alias.name, None)
                    if _strings(value):
                        found.add((module, alias.name))
    return found


def test_every_imported_text_constant_is_listed():
    # A test asserting against code text only checks the design if that text is
    # the design's — so every one a test imports must be listed above.
    unlisted = _imported_text_constants() - set(USED_BY_TESTS) - NOT_DESIGN_TEXT
    assert sorted(unlisted) == []
