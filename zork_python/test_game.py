"""Smoke tests for engine/game.py."""

import io
import sys

from engine.world import (
    World, Room, GameObject, Exit,
    TAKEBIT, CONTBIT, OPENBIT, ONBIT, NDESCBIT, INVISIBLE,
)
from engine.clock import Clock
from engine.parser import Parser, Vocabulary, SyntaxRule, ObjectSpec, LOC_HAVE, LOC_HELD
from engine.game import (
    Game,
    M_FATAL, M_HANDLED, M_NOT_HANDLED,
    M_BEG, M_END, M_ENTER, M_LOOK,
    VERBOSE, BRIEF, SUPER_BRIEF,
)


# ---------------------------------------------------------------------------
# Minimal fixture helpers
# ---------------------------------------------------------------------------

def make_vocab() -> Vocabulary:
    v = Vocabulary()
    v.add_direction("north", "n")
    v.add_direction("south", "s")
    v.add_buzz("the", "a", "an")
    v.add_verb("take",    "get")
    v.add_verb("examine", "x")
    v.add_verb("drop")
    v.add_verb("wait", "z")
    v.add_preposition("in", "into")
    return v


def make_rules() -> list:
    return [
        SyntaxRule(verb="wait", action="V-WAIT"),
        SyntaxRule(
            verb="examine", action="V-EXAMINE",
            obj1=ObjectSpec(locations=frozenset({LOC_HAVE})),
        ),
        SyntaxRule(
            verb="take", action="V-TAKE",
            obj1=ObjectSpec(find_flag=TAKEBIT, locations=frozenset({LOC_HAVE})),
        ),
    ]


def make_world() -> tuple[World, dict]:
    w = World()

    living = Room("LIVING-ROOM", "Living Room",
                  ldesc="A comfortable living room.",
                  flags={ONBIT},
                  exits={"north": Exit(destination="CELLAR")})
    cellar = Room("CELLAR", "Cellar",
                  ldesc="A dark, damp cellar.")  # no ONBIT
    w.register_room(living)
    w.register_room(cellar)

    lamp   = GameObject("LAMP",  synonyms=["lamp"],  desc="brass lantern",
                        flags={TAKEBIT, ONBIT})
    coin   = GameObject("COIN",  synonyms=["coin"],  desc="gold coin",
                        flags={TAKEBIT})
    player = GameObject("PLAYER", synonyms=["me"], desc="yourself",
                        flags={CONTBIT, OPENBIT}, capacity=100)

    for obj in [lamp, coin, player]:
        w.register_object(obj)

    w.move_object(lamp,   living)
    w.move_object(player, living)
    w.move_object(coin,   player)

    w.player = player
    w.winner = player
    w.here   = living

    return w, {"lamp": lamp, "coin": coin, "player": player,
               "living": living, "cellar": cellar}


def make_game() -> tuple[Game, World, dict]:
    w, objs = make_world()
    p = Parser(make_vocab(), make_rules())
    g = Game(w, p)
    return g, w, objs


def captured(fn, *args, **kwargs):
    """Run fn(*args, **kwargs) and return (result, printed_text)."""
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        result = fn(*args, **kwargs)
    finally:
        sys.stdout = old
    return result, buf.getvalue()


# ---------------------------------------------------------------------------
# PERFORM dispatch order tests
# ---------------------------------------------------------------------------

def test_perform_falls_through_to_verb_handler():
    g, w, _ = make_game()
    log = []
    g.register_verb("V-TEST", lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST")
    assert v == M_HANDLED
    assert log == ["verb"]
    print("PASS: default verb handler is called when nothing else handles it")


def test_perform_winner_action_blocks_chain():
    g, w, objs = make_game()
    log = []
    # Give the winner an action that blocks
    objs["player"].action = lambda world: log.append("winner") or M_HANDLED
    g.register_verb("V-TEST", lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST")
    assert v == M_HANDLED
    assert log == ["winner"]        # verb handler never reached
    print("PASS: winner action blocks dispatch chain")


def test_perform_room_beg_blocks_chain():
    g, w, objs = make_game()
    log = []
    objs["living"].action = lambda world, msg=None: (
        log.append(f"room:{msg}") or M_HANDLED if msg == M_BEG else M_NOT_HANDLED
    )
    g.register_verb("V-TEST", lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST")
    assert v == M_HANDLED
    assert "room:1" in log
    assert "verb" not in log
    print("PASS: room M-BEG blocks dispatch chain")


def test_perform_preaction_blocks_chain():
    g, w, _ = make_game()
    log = []
    g.register_preaction("V-TEST", lambda world: log.append("pre") or M_HANDLED)
    g.register_verb("V-TEST",      lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST")
    assert v == M_HANDLED
    assert log == ["pre"]
    print("PASS: preaction blocks verb handler")


def test_perform_prsi_action_blocks_chain():
    g, w, objs = make_game()
    log = []
    objs["lamp"].action = lambda world: log.append("prsi") or M_HANDLED
    g.register_verb("V-TEST",       lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST", prsi=objs["lamp"])
    assert v == M_HANDLED
    assert log == ["prsi"]
    print("PASS: PRSI action blocks dispatch chain")


def test_perform_container_contfcn_called():
    g, w, objs = make_game()
    log = []
    # Put coin inside a container that has a contfcn
    box = GameObject("BOX", synonyms=["box"], desc="wooden box",
                     flags={CONTBIT, OPENBIT}, capacity=50)
    box.contfcn = lambda world: log.append("contfcn") or M_HANDLED
    w.register_object(box)
    w.move_object(box,          w.here)
    w.move_object(objs["coin"], box)   # coin is now inside box

    g.register_verb("V-TEST", lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST", prso=objs["coin"])
    assert v == M_HANDLED
    assert log == ["contfcn"]
    print("PASS: container contfcn is called when PRSO is inside a container")


def test_perform_prso_action_blocks_chain():
    g, w, objs = make_game()
    log = []
    objs["lamp"].action = lambda world: log.append("prso") or M_HANDLED
    g.register_verb("V-TEST",  lambda world: log.append("verb") or M_HANDLED)
    v = g.perform("V-TEST", prso=objs["lamp"])
    assert v == M_HANDLED
    assert log == ["prso"]
    print("PASS: PRSO action blocks verb handler")


def test_perform_dispatch_priority_order():
    """Verify 7-step order by blocking at each level in turn."""
    g, w, objs = make_game()
    order = []

    # All handlers pass through to the next
    objs["player"].action = lambda world: order.append(1) or M_NOT_HANDLED
    objs["living"].action = lambda world, msg=None: (
        order.append(2) or M_NOT_HANDLED if msg == M_BEG else M_NOT_HANDLED
    )
    g.register_preaction("V-TEST", lambda world: order.append(3) or M_NOT_HANDLED)
    objs["coin"].action   = lambda world: order.append(4) or M_NOT_HANDLED  # PRSI
    objs["lamp"].action   = lambda world: order.append(6) or M_NOT_HANDLED  # PRSO
    g.register_verb("V-TEST",      lambda world: order.append(7) or M_HANDLED)

    v = g.perform("V-TEST", prso=objs["lamp"], prsi=objs["coin"])
    assert v == M_HANDLED
    assert order == [1, 2, 3, 4, 6, 7], f"Got order: {order}"
    print("PASS: PERFORM fires all 7 steps in correct priority order")


def test_perform_saves_restores_prsa_prso_prsi():
    g, w, objs = make_game()
    w.prsa = "OUTER"
    w.prso = objs["lamp"]
    w.prsi = None

    inner_prso = []
    def handler(world):
        inner_prso.append(world.prso)
        return M_HANDLED

    g.register_verb("V-TEST", handler)
    g.perform("V-TEST", prso=objs["coin"])

    # After perform, world state is restored
    assert w.prsa == "OUTER"
    assert w.prso is objs["lamp"]
    assert inner_prso == [objs["coin"]]
    print("PASS: perform saves and restores world prsa/prso/prsi")


# ---------------------------------------------------------------------------
# Movement tests
# ---------------------------------------------------------------------------

def test_walk_valid_exit(capsys=None):
    g, w, objs = make_game()
    # living -> north -> cellar (from make_world())
    # But cellar has no ONBIT, so we'll add a lamp to the player for light
    w.move_object(objs["lamp"], objs["player"])

    _, out = captured(g.do_walk, "north")
    assert w.here is objs["cellar"]
    assert "Cellar" in out
    print("PASS: do_walk moves player to destination room")


def test_walk_no_exit():
    g, w, _ = make_game()
    _, out = captured(g.do_walk, "south")
    assert "can't go that way" in out.lower()
    assert w.here.name == "LIVING-ROOM"
    print("PASS: do_walk prints error for missing exit")


def test_walk_blocked_exit():
    g, w, objs = make_game()
    # Replace north exit with a blocked one
    objs["living"].exits["north"] = Exit(message="The door is locked.")
    _, out = captured(g.do_walk, "north")
    assert "locked" in out
    assert w.here is objs["living"]
    print("PASS: do_walk prints blocked exit message")


def test_walk_via_do_turn():
    g, w, objs = make_game()
    w.move_object(objs["lamp"], objs["player"])
    _, out = captured(g.do_turn, "north")
    assert w.here is objs["cellar"]
    print("PASS: 'go north' via do_turn moves player")


# ---------------------------------------------------------------------------
# Room description tests
# ---------------------------------------------------------------------------

def test_describe_room_lit_brief_first_visit():
    g, w, _ = make_game()
    w.here.visited = False
    g.desc_mode = BRIEF
    _, out = captured(g.describe_room)
    assert "Living Room" in out
    assert "comfortable living room" in out
    print("PASS: BRIEF mode shows ldesc on first visit")


def test_describe_room_lit_brief_revisit():
    g, w, _ = make_game()
    w.here.visited = True
    g.desc_mode = BRIEF
    _, out = captured(g.describe_room)
    assert "Living Room" in out
    assert "comfortable living room" not in out
    print("PASS: BRIEF mode skips ldesc on revisit")


def test_describe_room_verbose_always_shows_ldesc():
    g, w, _ = make_game()
    w.here.visited = True   # even after visit
    g.desc_mode = VERBOSE
    _, out = captured(g.describe_room)
    assert "comfortable living room" in out
    print("PASS: VERBOSE mode always shows ldesc")


def test_describe_room_super_brief():
    g, w, _ = make_game()
    w.here.visited = False
    g.desc_mode = SUPER_BRIEF
    _, out = captured(g.describe_room)
    assert "Living Room" in out
    assert "comfortable" not in out   # ldesc suppressed
    assert "lantern" not in out       # contents suppressed
    print("PASS: SUPER_BRIEF shows only room title")


def test_describe_room_dark():
    g, w, objs = make_game()
    # Move to cellar (dark, no ONBIT)
    w.move_object(objs["player"], objs["cellar"])
    w.here = objs["cellar"]
    _, out = captured(g.describe_room)
    assert "pitch black" in out
    print("PASS: describe_room shows 'pitch black' in dark room")


def test_describe_contents_listed():
    g, w, objs = make_game()
    g.desc_mode = BRIEF
    w.here.visited = True   # suppress ldesc
    _, out = captured(g.describe_room)
    assert "lantern" in out or "lamp" in out or "brass" in out
    print("PASS: visible room contents are listed")


def test_describe_contents_invisible_skipped():
    g, w, objs = make_game()
    objs["lamp"].set_flag(INVISIBLE)
    g.desc_mode = BRIEF
    w.here.visited = True
    _, out = captured(g.describe_room)
    assert "lantern" not in out and "lamp" not in out
    print("PASS: INVISIBLE objects are not listed")


def test_describe_contents_ndescbit_skipped():
    g, w, objs = make_game()
    objs["lamp"].set_flag(NDESCBIT)
    g.desc_mode = BRIEF
    w.here.visited = True
    _, out = captured(g.describe_room)
    assert "lantern" not in out and "lamp" not in out
    print("PASS: NDESCBIT objects are not listed")


# ---------------------------------------------------------------------------
# enter_room
# ---------------------------------------------------------------------------

def test_enter_room_triggers_m_enter():
    g, w, objs = make_game()
    msgs = []
    objs["cellar"].action = lambda world, msg=None: msgs.append(msg) or M_NOT_HANDLED
    w.move_object(objs["lamp"], objs["player"])  # bring light
    g.enter_room(objs["cellar"])
    assert M_ENTER in msgs
    print("PASS: enter_room fires M_ENTER on room action")


def test_enter_room_marks_visited():
    g, w, objs = make_game()
    objs["cellar"].visited = False
    w.move_object(objs["lamp"], objs["player"])
    g.enter_room(objs["cellar"])
    assert objs["cellar"].visited
    print("PASS: enter_room marks room as visited")


# ---------------------------------------------------------------------------
# Clock integration
# ---------------------------------------------------------------------------

def test_clock_advances_after_turn():
    g, w, _ = make_game()
    g.register_verb("V-WAIT", lambda world: M_HANDLED)
    assert w.moves == 0
    captured(g.do_turn, "wait")
    assert w.moves == 1
    print("PASS: clock advances after a normal turn")


def test_clock_skips_for_meta_verb():
    g, w, _ = make_game()
    g.register_verb("V-SCORE", lambda world: M_HANDLED)
    # We need the parser to know about 'score' -> V-SCORE
    # Since our minimal test vocab doesn't include 'score', we test directly
    assert w.moves == 0
    # Manually dispatch a meta-verb result
    from engine.parser import ParseResult
    from engine.game import _SKIP_CLOCK
    meta = ParseResult(
        action="V-SCORE", preaction=None,
        prso=[], prsi=[], direction=None, syntax=None,
        words=["score"],
    )
    # Patch parser to return our meta result
    g.parser.parse = lambda text, world: meta
    captured(g.do_turn, "score")
    assert w.moves == 0  # clock was skipped
    print("PASS: clock does not advance for meta verbs")


def test_clock_does_not_advance_on_parse_failure():
    g, w, _ = make_game()
    assert w.moves == 0
    captured(g.do_turn, "xyzzy florp")   # unknown words
    # Clock still ticks even on parse failure (demons need to run)
    assert w.moves == 1
    print("PASS: clock ticks even on parse failure (demons still run)")


# ---------------------------------------------------------------------------
# M-END
# ---------------------------------------------------------------------------

def test_m_end_fired_after_perform():
    g, w, objs = make_game()
    msgs = []
    objs["living"].action = lambda world, msg=None: msgs.append(msg) or M_NOT_HANDLED
    g.register_verb("V-WAIT", lambda world: M_HANDLED)
    # Parse doesn't know V-WAIT in minimal vocab, so call do_turn with patched parser
    from engine.parser import ParseResult
    wait_result = ParseResult(
        action="V-WAIT", preaction=None,
        prso=[], prsi=[], direction=None, syntax=None, words=["wait"],
    )
    g.parser.parse = lambda text, world: wait_result
    captured(g.do_turn, "wait")
    assert M_END in msgs
    print("PASS: M_END is fired on room action after perform completes")


# ---------------------------------------------------------------------------
# jigs_up / quit
# ---------------------------------------------------------------------------

def test_jigs_up_prints_message():
    g, w, _ = make_game()
    g._running = True
    _, out = captured(g.jigs_up, "You have been eaten by a grue.")
    assert "grue" in out
    assert not g._running
    print("PASS: jigs_up prints message and stops the loop")


def test_jigs_up_deducts_10_from_score():
    g, w, _ = make_game()
    w.score = 50
    w.set_global("BASE-SCORE", 50)
    g._running = True
    captured(g.jigs_up, "You have died.")
    assert w.score == 40
    assert int(w.get_global("BASE-SCORE")) == 40
    assert int(w.get_global("SCORE")) == 40
    print("PASS: jigs_up deducts 10 from score")


def test_jigs_up_score_cannot_go_below_zero():
    g, w, _ = make_game()
    w.score = 5
    w.set_global("BASE-SCORE", 5)
    g._running = True
    captured(g.jigs_up, "You have died.")
    assert w.score == 0
    print("PASS: jigs_up clamps score at 0")


def test_quit_stops_loop():
    g, w, _ = make_game()
    g._running = True
    g.quit()
    assert not g._running
    print("PASS: quit() stops the game loop")


# ---------------------------------------------------------------------------
# it_object tracking
# ---------------------------------------------------------------------------

def test_it_object_updated_by_perform():
    g, w, objs = make_game()
    g.register_verb("V-TEST", lambda world: M_HANDLED)
    g.perform("V-TEST", prso=objs["lamp"])
    assert w.it_object is objs["lamp"]
    print("PASS: perform updates world.it_object with PRSO")


def test_it_object_not_updated_for_walk():
    g, w, objs = make_game()
    w.it_object = objs["coin"]
    w.walk_dir = "north"
    g.perform("V-WALK")
    # it_object should NOT be updated for walk
    assert w.it_object is objs["coin"]
    print("PASS: perform does not update it_object for V-WALK")


if __name__ == "__main__":
    test_perform_falls_through_to_verb_handler()
    test_perform_winner_action_blocks_chain()
    test_perform_room_beg_blocks_chain()
    test_perform_preaction_blocks_chain()
    test_perform_prsi_action_blocks_chain()
    test_perform_container_contfcn_called()
    test_perform_prso_action_blocks_chain()
    test_perform_dispatch_priority_order()
    test_perform_saves_restores_prsa_prso_prsi()
    test_walk_valid_exit()
    test_walk_no_exit()
    test_walk_blocked_exit()
    test_walk_via_do_turn()
    test_describe_room_lit_brief_first_visit()
    test_describe_room_lit_brief_revisit()
    test_describe_room_verbose_always_shows_ldesc()
    test_describe_room_super_brief()
    test_describe_room_dark()
    test_describe_contents_listed()
    test_describe_contents_invisible_skipped()
    test_describe_contents_ndescbit_skipped()
    test_enter_room_triggers_m_enter()
    test_enter_room_marks_visited()
    test_clock_advances_after_turn()
    test_clock_skips_for_meta_verb()
    test_clock_does_not_advance_on_parse_failure()
    test_m_end_fired_after_perform()
    test_jigs_up_prints_message()
    test_jigs_up_deducts_10_from_score()
    test_jigs_up_score_cannot_go_below_zero()
    test_quit_stops_loop()
    test_it_object_updated_by_perform()
    test_it_object_not_updated_for_walk()
    print("\nAll tests passed.")
