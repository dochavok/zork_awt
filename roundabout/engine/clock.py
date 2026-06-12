"""
Clock / daemon system.

Mirrors the ZIL GCLOCK module (gclock.zil).

The ZIL clock is a flat table divided into two regions:
  [C-INTS .. C-DEMONS)   -- interrupts: only processed after a successful parse
  [C-DEMONS .. C-TABLELEN) -- demons: processed every turn, parse success or not

Each entry has three fields:
  enabled  -- whether the entry participates in the tick
  ticks    -- countdown; 0 = quiescent (won't fire); decremented each turn;
              fires when it goes from 1 → 0
  handler  -- callable to invoke when ticks reaches 0

CLOCKER additionally supports CLOCK-WAIT: when set, the next tick is skipped
entirely and MOVES is not incremented.

In Python we store entries in an ordered dict keyed by a string name (the
ZIL routine name), so they can be looked up, queued, enabled, and disabled
by name.  The is_demon flag replaces the two-region table layout.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Optional

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# ClockEvent
# ---------------------------------------------------------------------------

@dataclass
class ClockEvent:
    """One entry in the clock table."""

    name: str

    # callable(world) -> bool
    # Returns True if the handler produced visible output (narration, warning…).
    handler: Callable[[World], bool]

    # Countdown ticks.  0 = quiescent (won't fire until re-queued).
    ticks: int = 0

    # When False the entry is completely ignored by tick().
    enabled: bool = True

    # Demons are processed even when the parser failed to match a command.
    # Interrupts (is_demon=False) are only processed after a successful parse.
    is_demon: bool = False

    def __repr__(self) -> str:
        kind = "demon" if self.is_demon else "interrupt"
        status = "on" if self.enabled else "off"
        return f"<ClockEvent {self.name!r} {kind} ticks={self.ticks} {status}>"


# ---------------------------------------------------------------------------
# Clock
# ---------------------------------------------------------------------------

class Clock:
    """
    The game clock.  One Clock instance lives on the World.

    Registration methods (queue, add_demon) are called by content modules
    during world initialisation.  tick() is called once per game turn by the
    game loop.
    """

    def __init__(self) -> None:
        # Insertion order is preserved (Python 3.7+), which determines
        # evaluation order — important for deterministic event firing.
        self._events: dict[str, ClockEvent] = {}

        # Mirrors CLOCK-WAIT: when True the next tick() call is a no-op.
        self._wait: bool = False

    # ------------------------------------------------------------------ #
    # Registration / scheduling                                            #
    # ------------------------------------------------------------------ #

    def queue(
        self,
        name: str,
        handler: Callable[[World], bool],
        ticks: int,
        *,
        is_demon: bool = False,
    ) -> ClockEvent:
        """
        Schedule a named event to fire after `ticks` turns.

        Mirrors ZIL QUEUE + INT.  If an event with this name already exists
        its tick count is reset and it is re-enabled; the handler and demon
        flag are left unchanged (the ZIL INT routine returns the existing slot
        without modifying RTN).

        ticks=1  → fires on the very next clock tick
        ticks=N  → fires N turns from now
        ticks=0  → quiescent; does nothing until queue()d again
        """
        if name in self._events:
            event = self._events[name]
            event.ticks = ticks
            event.enabled = True
        else:
            event = ClockEvent(
                name=name,
                handler=handler,
                ticks=ticks,
                enabled=True,
                is_demon=is_demon,
            )
            self._events[name] = event
        return event

    def add_demon(
        self,
        name: str,
        handler: Callable[[World], bool],
    ) -> ClockEvent:
        """
        Register a demon — an event that is eligible every turn.

        Demons still need a ticks value > 0 to fire; call queue() or
        set event.ticks directly to arm them.  This method merely marks the
        event as is_demon=True so it is included even on turns where the
        parser failed.

        Calling add_demon on an already-registered event is a no-op.
        """
        if name not in self._events:
            self._events[name] = ClockEvent(
                name=name,
                handler=handler,
                ticks=0,
                enabled=True,
                is_demon=True,
            )
        return self._events[name]

    # ------------------------------------------------------------------ #
    # Enable / disable                                                     #
    # ------------------------------------------------------------------ #

    def enable(self, name: str) -> None:
        """Enable a registered event (mirrors ZIL ENABLE)."""
        if name in self._events:
            self._events[name].enabled = True

    def disable(self, name: str) -> None:
        """Disable a registered event without removing it (mirrors ZIL DISABLE)."""
        if name in self._events:
            self._events[name].enabled = False

    def get(self, name: str) -> Optional[ClockEvent]:
        """Return the event entry by name, or None."""
        return self._events.get(name)

    # ------------------------------------------------------------------ #
    # CLOCK-WAIT                                                           #
    # ------------------------------------------------------------------ #

    def wait(self) -> None:
        """
        Skip the next tick entirely (mirrors CLOCK-WAIT).

        Used by content when an action should not consume a clock turn
        (e.g. SAVE, RESTORE, SCORE in the original ZIL).
        """
        self._wait = True

    # ------------------------------------------------------------------ #
    # tick                                                                 #
    # ------------------------------------------------------------------ #

    def tick(self, world: World, command_parsed: bool = True) -> bool:
        """
        Advance the clock by one turn.

        Mirrors ZIL CLOCKER.

        command_parsed -- True when the parser successfully matched a command.
                          When False only demon events are processed;
                          interrupts are skipped.

        Side-effect: increments world.moves (as the ZIL CLOCKER does).

        Returns True if any event handler produced visible output.
        """
        # CLOCK-WAIT: skip this tick entirely.
        if self._wait:
            self._wait = False
            return False

        fired_any = False

        for event in list(self._events.values()):
            if not event.enabled:
                continue

            # Interrupts are only processed after a successful parse.
            if not event.is_demon and not command_parsed:
                continue

            # Quiescent: tick=0 means "not scheduled".
            if event.ticks == 0:
                continue

            event.ticks -= 1

            # ZIL: <NOT <G? .TICK 1>> fires when old tick <= 1, i.e. new tick = 0.
            if event.ticks == 0:
                result = event.handler(world)
                if result:
                    fired_any = True

        # MOVES is incremented here, matching ZIL CLOCKER behaviour.
        world.moves += 1

        return fired_any

    # ------------------------------------------------------------------ #
    # Introspection                                                        #
    # ------------------------------------------------------------------ #

    def __repr__(self) -> str:
        active = [e for e in self._events.values() if e.enabled and e.ticks > 0]
        return f"<Clock events={len(self._events)} active={len(active)}>"
