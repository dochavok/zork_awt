"""
Game loop and PERFORM dispatch chain.

Mirrors the ZIL MAIN-LOOP / PERFORM routines from gmain.zil.

The Game class owns:
  - the parse -> perform -> clock pipeline (one call per turn)
  - the PERFORM dispatch chain (7-step priority order)
  - room entry / description logic
  - the death (JIGS-UP) handler
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional

if TYPE_CHECKING:
    from engine.clock import Clock
    from engine.parser import Parser, ParseResult
    from engine.world import GameObject, Room, World

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# PERFORM return values (gmain.zil M-FATAL / M-HANDLED / M-NOT-HANDLED)
M_FATAL       = 2
M_HANDLED     = 1
M_NOT_HANDLED = 0

# Room/object message types sent to action handlers
M_BEG     = 1   # start of turn (before verb dispatch)
M_ENTER   = 2   # player just entered the room
M_LOOK    = 3   # describe the room (called from describe_room)
M_FLASH   = 4   # brief flash / redescription
M_OBJDESC = 5   # describe an object in the room
M_END     = 6   # end of turn (after verb dispatch)

# Description modes
VERBOSE     = 0   # always show long description + contents
BRIEF       = 1   # long description on first visit only (default)
SUPER_BRIEF = 2   # room title only

# Action names that do NOT advance the clock (ZIL: clocker skipped for these)
_SKIP_CLOCK: frozenset[str] = frozenset({
    "V-SAVE", "V-RESTORE", "V-QUIT", "V-RESTART",
    "V-SCORE", "V-VERSION", "V-SCRIPT", "V-UNSCRIPT",
    "V-VERBOSE", "V-BRIEF", "V-SUPER-BRIEF",
})


# ---------------------------------------------------------------------------
# Game
# ---------------------------------------------------------------------------

class Game:
    """
    Main game controller.

    Content modules register verb handlers and preaction handlers; the engine
    wires them together and drives the turn loop.

    Handler signature convention:
        handler(world: World) -> int
    Return M_HANDLED (1) to consume the action, M_NOT_HANDLED (0) to pass it
    on, or M_FATAL (2) to end the game immediately.
    """

    def __init__(
        self,
        world: World,
        parser: Parser,
        clock: Optional[Clock] = None,
    ) -> None:
        from engine.clock import Clock as _Clock

        self.world  = world
        self.parser = parser
        self.clock  = clock if clock is not None else _Clock()

        # action name -> default (last-resort) verb handler
        self._verb_handlers: dict[str, Callable[[World], int]] = {}

        # action name -> preaction handler (runs before default handler)
        self._preaction_handlers: dict[str, Callable[[World], int]] = {}

        self.desc_mode: int = BRIEF
        self._running:  bool = False

        # Attach back-reference so content handlers can call game methods
        world.game = self

        # Register the built-in walk handler; content may override it
        self._verb_handlers["V-WALK"] = lambda w: self.do_walk(
            getattr(w, "walk_dir", None) or ""
        )

    # ------------------------------------------------------------------ #
    # Registration                                                         #
    # ------------------------------------------------------------------ #

    def register_verb(self, action: str, handler: Callable[[World], int]) -> None:
        """Register the default (fallback) handler for an action name."""
        self._verb_handlers[action] = handler

    def register_preaction(
        self, action: str, handler: Callable[[World], int]
    ) -> None:
        """Register a preaction handler that runs before the verb handler."""
        self._preaction_handlers[action] = handler

    # ------------------------------------------------------------------ #
    # Main loop                                                            #
    # ------------------------------------------------------------------ #

    def run(self) -> None:
        """Read-eval-print loop: describe the starting room then process turns."""
        self._running = True
        self.enter_room(self.world.here)

        while self._running:
            try:
                line = input("\n> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            self.do_turn(line)

    def do_turn(self, input_text: str) -> int:
        """
        Process one player turn.

        Parses input_text, dispatches to PERFORM, fires M-END on the room,
        then advances the clock.  Returns the PERFORM result.
        """
        w = self.world
        result = self.parser.parse(input_text, w)
        command_parsed = result is not None

        v = M_NOT_HANDLED
        if command_parsed:
            v = self._dispatch(result)
            # M-END: room end-of-turn notification, outside the perform chain
            if v != M_FATAL and w.here is not None and w.here.action is not None:
                w.here.action(w, M_END)

        # Advance the clock unless the action explicitly bypasses it
        is_meta = command_parsed and result.action in _SKIP_CLOCK
        if not is_meta:
            self.clock.tick(w, command_parsed=command_parsed)

        return v

    # ------------------------------------------------------------------ #
    # Dispatch                                                             #
    # ------------------------------------------------------------------ #

    def _dispatch(self, result: ParseResult) -> int:
        """Route a ParseResult into the PERFORM chain."""
        w = self.world

        if result.action == "V-WALK":
            w.walk_dir = result.direction
            return self.perform("V-WALK")

        # Multi-object (MANY): dispatch each object in turn with a label
        if len(result.prso) > 1:
            v = M_NOT_HANDLED
            for obj in result.prso:
                prsi = result.prsi[0] if result.prsi else None
                print(f"{obj.desc}:")
                r = self.perform(result.action, obj, prsi)
                if r == M_FATAL:
                    return M_FATAL
                v = r
            return v

        prso = result.prso[0] if result.prso else None
        prsi = result.prsi[0] if result.prsi else None

        # Auto-take: ZIL ITAKE-CHECK — if syntax has TAKE and prso is not
        # directly held, silently move it to inventory and print "(Taken)".
        # Only applies when the object has TAKEBIT but not TRYTAKEBIT.
        if (prso is not None
                and result.syntax is not None
                and result.syntax.obj1 is not None
                and result.syntax.obj1.auto_take
                and w.player is not None
                and prso not in w.player.contents):
            from engine.world import TAKEBIT, TRYTAKEBIT
            if prso.has_flag(TAKEBIT) and not prso.has_flag(TRYTAKEBIT):
                w.move_object(prso, w.player)
                print("(Taken)")

        return self.perform(result.action, prso, prsi)

    # ------------------------------------------------------------------ #
    # PERFORM                                                              #
    # ------------------------------------------------------------------ #

    def perform(
        self,
        action: str,
        prso: Optional[GameObject] = None,
        prsi: Optional[GameObject] = None,
    ) -> int:
        """
        PERFORM dispatch chain (mirrors ZIL PERFORM from gmain.zil).

        Priority order:
          1. winner/actor action
          2. current room action with M_BEG
          3. registered preaction handler
          4. PRSI (indirect object) action
          5. PRSO container's contfcn
          6. PRSO action
          7. default verb handler

        The first handler that returns a truthy value (M_HANDLED or M_FATAL)
        short-circuits the rest.  PRSA/PRSO/PRSI are saved and restored.
        """
        w = self.world

        old_prsa, old_prso, old_prsi = w.prsa, w.prso, w.prsi
        w.prsa = action
        w.prso = prso
        w.prsi = prsi

        if prso is not None and action != "V-WALK":
            w.it_object = prso

        try:
            v = self._perform_chain(action, prso, prsi)
        finally:
            w.prsa = old_prsa
            w.prso = old_prso
            w.prsi = old_prsi

        return v

    def _perform_chain(
        self,
        action: str,
        prso: Optional[GameObject],
        prsi: Optional[GameObject],
    ) -> int:
        w = self.world

        # 1. Winner/actor action
        if w.winner is not None and w.winner.action is not None:
            v = w.winner.action(w)
            if v:
                return v

        # 2. Room M-BEG (or vehicle M-BEG when player is inside a VEHBIT object)
        effective_actor = w.here
        if w.winner is not None:
            winner_loc = w.winner.location
            if winner_loc is not None and hasattr(winner_loc, "has_flag") and winner_loc.has_flag("VEHBIT"):
                effective_actor = winner_loc  # type: ignore[assignment]
        if effective_actor is not None and effective_actor.action is not None:
            v = effective_actor.action(w, M_BEG)
            if v:
                return v

        # 3. Preaction
        pre = self._preaction_handlers.get(action)
        if pre is not None:
            v = pre(w)
            if v:
                return v

        # 4. PRSI action
        if prsi is not None and prsi.action is not None:
            v = prsi.action(w)
            if v:
                return v

        # 5. Container contfcn (the container that directly holds PRSO)
        if prso is not None and action != "V-WALK":
            from engine.world import GameObject as _GO
            loc = prso.location
            if isinstance(loc, _GO) and loc.contfcn is not None:
                v = loc.contfcn(w)
                if v:
                    return v

        # 6. PRSO action
        if prso is not None and action != "V-WALK" and prso.action is not None:
            v = prso.action(w)
            if v:
                return v

        # 7. Default verb handler
        handler = self._verb_handlers.get(action)
        if handler is not None:
            return handler(w)

        return M_NOT_HANDLED

    # ------------------------------------------------------------------ #
    # Movement                                                             #
    # ------------------------------------------------------------------ #

    def do_walk(self, direction: str) -> int:
        """
        Default V-WALK handler: attempt to move the player in `direction`.

        Content may override V-WALK entirely by registering a verb handler,
        but this method remains callable for the common case.
        """
        w = self.world
        here = w.here

        if here is None:
            return M_NOT_HANDLED

        exit_ = here.exits.get(direction)
        if exit_ is None:
            print("You can't go that way.")
            return M_HANDLED

        room, msg = exit_.resolve(w)
        if msg is not None:
            print(msg)
        if room is None:
            return M_HANDLED

        self.enter_room(room)
        return M_HANDLED

    # ------------------------------------------------------------------ #
    # Room entry and description                                           #
    # ------------------------------------------------------------------ #

    def enter_room(self, room: Optional[Room]) -> int:
        """
        Move the winner to `room`, trigger M_ENTER, then describe the room.

        Returns M_FATAL if the room action signals it, M_HANDLED otherwise.
        """
        if room is None:
            return M_NOT_HANDLED

        w = self.world

        if w.winner is not None:
            w.move_object(w.winner, room)
        w.here = room

        if room.action is not None:
            v = room.action(w, M_ENTER)
            if v == M_FATAL:
                return M_FATAL

        # Award exploration score on first visit (ZIL SCORE-OBJ .RM).
        if not room.visited and room.value > 0:
            from content.verbs import _score_upd
            _score_upd(w, room.value)
            room.value = 0

        self.describe_room()
        room.visited = True
        return M_HANDLED

    def describe_room(self) -> None:
        """
        Print the current room's title and (optionally) its long description
        and visible contents, according to desc_mode and visit history.
        """
        w = self.world
        room = w.here
        if room is None:
            return

        if not w.is_lit():
            print("It is pitch black. You are likely to be eaten by a grue.")
            return

        print(room.desc)

        show_long = (self.desc_mode == VERBOSE) or (
            self.desc_mode == BRIEF and not room.visited
        )
        if show_long:
            if room.ldesc:
                print(room.ldesc)
            elif room.action is not None:
                room.action(w, M_LOOK)

        if self.desc_mode != SUPER_BRIEF:
            self._describe_contents(room)

    def _describe_contents(self, room: Room) -> None:
        """Print visible objects in the room."""
        from engine.world import INVISIBLE, NDESCBIT
        w = self.world

        for obj in list(room.contents):
            if w.winner is not None and obj is w.winner:
                continue
            if obj.has_flag(INVISIBLE) or obj.has_flag(NDESCBIT):
                continue
            if not obj.touched and obj.fdesc:
                print(obj.fdesc)
            elif obj.ldesc:
                print(obj.ldesc)
            else:
                print(f"There is {_article(obj.desc)} here.")

    # ------------------------------------------------------------------ #
    # Death / quit                                                         #
    # ------------------------------------------------------------------ #

    def _scatter_items(self) -> None:
        """Move player inventory to scatter destinations: valuables underground, junk to CLEARING."""
        lld      = self.world.rooms.get("LAND-OF-LIVING-DEAD")
        clearing = self.world.rooms.get("CLEARING")
        player   = self.world.winner
        if not player or not lld or not clearing:
            return
        for item in list(player.contents):
            dest = lld if (item.tvalue or 0) > 0 else clearing
            self.world.move_object(item, dest)

    def jigs_up(self, message: str) -> None:
        """Death handler: scatter items, track deaths, resurrect or end game (ZIL JIGS-UP)."""
        print(message)
        base = int(self.world.get_global("BASE-SCORE") or 0) - 10
        self.world.set_global("BASE-SCORE", base)
        self.world.score = max(0, self.world.score - 10)
        self.world.set_global("SCORE", self.world.score)

        self._scatter_items()

        deaths = int(self.world.get_global("DEATHS-SO-FAR") or 0) + 1
        self.world.set_global("DEATHS-SO-FAR", deaths)

        if deaths >= 3:
            print("\n**** You have died ****\n\nUnfortunately, you have run out of chances. "
                  "Better luck next time.")
            self._running = False
            return

        if self.world.get_global("VISITED-ALTAR"):
            clearing = self.world.rooms.get("CLEARING")
            self.world.move_object(self.world.winner, clearing)
            self.world.here = clearing
            print("\nAs you take your last breath, a warm glow surrounds you...\n"
                  "You are resurrected in a clearing in the forest.\n"
                  "Your score has been adjusted.")
        else:
            print("\n**** You have died ****\n\nYou have not been granted the gift of resurrection.")
            self._running = False

    def quit(self) -> None:
        """Stop the game loop cleanly."""
        self._running = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _article(desc: str) -> str:
    """Return 'an X' or 'a X' based on the first character of desc."""
    if desc and desc[0].lower() in "aeiou":
        return f"an {desc}"
    return f"a {desc}"
