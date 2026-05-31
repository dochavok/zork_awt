"""Smoke tests for engine/clock.py."""

from engine.world import World, Room
from engine.clock import Clock, ClockEvent


def make_world():
    w = World()
    w.register_room(Room("START", "Start Room"))
    return w


def test_basic_countdown():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("LANTERN", lambda world: fired.append("lantern") or True, ticks=3)

    c.tick(w)  # ticks: 3→2
    c.tick(w)  # ticks: 2→1
    assert not fired

    c.tick(w)  # ticks: 1→0 → fires
    assert fired == ["lantern"]
    assert w.moves == 3
    print("PASS: event fires after correct number of ticks")


def test_quiescent_after_fire():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("EVT", lambda world: fired.append(1) or True, ticks=1)
    c.tick(w)   # fires
    c.tick(w)   # ticks=0 → quiescent, should NOT fire again
    c.tick(w)

    assert len(fired) == 1
    print("PASS: event does not fire again after going quiescent")


def test_requeue_after_fire():
    w = make_world()
    fired = []

    def handler(world):
        fired.append(1)
        return True

    c = Clock()
    c.queue("EVT", handler, ticks=2)
    c.tick(w)
    c.tick(w)   # fires
    assert len(fired) == 1

    c.queue("EVT", handler, ticks=2)  # re-arm
    c.tick(w)
    c.tick(w)   # fires again
    assert len(fired) == 2
    print("PASS: re-queued event fires again")


def test_enable_disable():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("EVT", lambda world: fired.append(1) or True, ticks=2)
    c.disable("EVT")
    c.tick(w)
    c.tick(w)
    assert not fired, "disabled event should not fire"

    c.enable("EVT")
    c.queue("EVT", lambda world: fired.append(1) or True, ticks=1)
    c.tick(w)
    assert len(fired) == 1
    print("PASS: disable/enable controls event firing")


def test_clock_wait():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("EVT", lambda world: fired.append(1) or True, ticks=1)
    c.wait()
    c.tick(w)   # skipped due to CLOCK-WAIT
    assert not fired
    assert w.moves == 0, "CLOCK-WAIT should also suppress MOVES increment"

    c.tick(w)   # now fires
    assert len(fired) == 1
    assert w.moves == 1
    print("PASS: CLOCK-WAIT skips one tick including MOVES increment")


def test_demon_runs_always():
    w = make_world()
    fired = []

    c = Clock()
    # Arm a demon with ticks=1 so it fires immediately.
    c.queue("GRUE", lambda world: fired.append("grue") or True, ticks=1, is_demon=True)

    c.tick(w, command_parsed=False)  # no command — demon should still fire
    assert fired == ["grue"]
    print("PASS: demon fires even when no command was parsed")


def test_interrupt_skipped_without_command():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("TROLL", lambda world: fired.append("troll") or True, ticks=1)
    # is_demon defaults to False → interrupt

    c.tick(w, command_parsed=False)  # no command → interrupt skipped
    assert not fired
    print("PASS: interrupt is skipped when command_parsed=False")


def test_interrupt_fires_with_command():
    w = make_world()
    fired = []

    c = Clock()
    c.queue("TROLL", lambda world: fired.append("troll") or True, ticks=1)

    c.tick(w, command_parsed=True)
    assert fired == ["troll"]
    print("PASS: interrupt fires when command_parsed=True")


def test_mixed_demons_and_interrupts():
    w = make_world()
    log = []

    c = Clock()
    c.queue("GRUE",   lambda world: log.append("grue")   or True, ticks=1, is_demon=True)
    c.queue("THIEF",  lambda world: log.append("thief")  or True, ticks=1)

    # Turn where parser failed: only demon fires
    c.tick(w, command_parsed=False)
    assert log == ["grue"]

    # Re-arm both for next test
    log.clear()
    c.queue("GRUE",  lambda world: log.append("grue")  or True, ticks=1, is_demon=True)
    c.queue("THIEF", lambda world: log.append("thief") or True, ticks=1)

    # Turn where parser succeeded: both fire
    c.tick(w, command_parsed=True)
    assert "grue"  in log
    assert "thief" in log
    print("PASS: demon fires on failed parse; interrupt only on success")


def test_moves_incremented_each_tick():
    w = make_world()
    c = Clock()
    for _ in range(5):
        c.tick(w)
    assert w.moves == 5
    print("PASS: world.moves incremented once per tick")


def test_fired_any_return_value():
    w = make_world()
    fired_output = []

    def silent_handler(world):
        return False   # no visible output

    def loud_handler(world):
        fired_output.append(1)
        return True    # produced output

    c = Clock()
    c.queue("SILENT", silent_handler, ticks=1)
    result = c.tick(w)
    assert result is False

    c.queue("LOUD", loud_handler, ticks=1)
    result = c.tick(w)
    assert result is True
    print("PASS: tick() return value reflects whether any handler produced output")


def test_add_demon_idempotent():
    w = make_world()
    fired = []

    c = Clock()
    c.add_demon("LIGHT", lambda world: fired.append(1) or True)
    c.add_demon("LIGHT", lambda world: fired.append(99) or True)  # second call ignored

    # Arm it
    c.queue("LIGHT", lambda world: fired.append(1) or True, ticks=1, is_demon=True)
    c.tick(w)

    # Should only fire once
    assert len(fired) == 1
    print("PASS: add_demon is idempotent for duplicate names")


if __name__ == "__main__":
    test_basic_countdown()
    test_quiescent_after_fire()
    test_requeue_after_fire()
    test_enable_disable()
    test_clock_wait()
    test_demon_runs_always()
    test_interrupt_skipped_without_command()
    test_interrupt_fires_with_command()
    test_mixed_demons_and_interrupts()
    test_moves_incremented_each_tick()
    test_fired_any_return_value()
    test_add_demon_idempotent()
    print("\nAll tests passed.")
