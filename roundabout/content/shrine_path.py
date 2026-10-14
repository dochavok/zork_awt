"""
Upper tier, batch 3: Prayer Alcove → Mid-Tier Key Door.

Design: locations.md (Prayer Alcove, Portcullis Corridor, Shrine Room,
Rickety Bridge, Mid-Tier Key Door), traps.md (Trap 19), mechanics.md
(Weight System), quests.md (Quest 32, Quest 49).

- Prayer Alcove: the hidden niche — Easy perception, once per visit — holds
  the crowbar and the vial of glacier melt.
- Portcullis (Trap 19): Medium perception spots the charge, then the Medium
  disarm runs. Touching or lifting a charged portcullis shocks (1 heart, lose
  a turn). Discharged: LIFT PORTCULLIS (Medium strength) holds it up for one
  turn — USE PORTCULLIS BAR props it open for good, anything else drops it.
- Shrine Room: the third bowl piece — Easy perception.
- Rickety Bridge: carry weight over 12 blocks the crossing either way (south
  from the bridge, north from the Key Door). Seeing the iron door from the
  bridge discovers Quest 32 (silently).
- Mid-Tier Key Door: UNLOCK DOOR WITH KEY (Middle Tier Key) — the key stays in
  the lock and the door stays open.

State: NICHE-FOUND, PORTCULLIS (charged | discharged | propped),
       PORTCULLIS-HELD (turn lifted), TRAP19-CHECKED, KEY-DOOR-UNLOCKED
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

WEIGHT_LIMIT = 12

_ALCOVE = (
    "A low stone alcove off a passage that runs north and south, barely deep "
    "enough to stand in. A carved niche is set into the back wall, its edges worn "
    "smooth by hands."
)
_NICHE_FOUND = (
    "The niche goes back further than it looks. Behind the carved lip there's a "
    "gap — and inside it, things that were put there on purpose."
)

_PORT_BASE = "A straight corridor, closed off halfway along by an iron portcullis."
_PORT_CHARGE = (" The air around the bars has a faint, dry crackle, and the hairs on "
                "your arms stand up as you get close.")
_PORT_PROPPED = " The portcullis is propped open with an iron bar."
_PORT_EXITS_SHUT = " The corridor runs north and south; the bars stand between you and the far end."
_PORT_EXITS_OPEN = " The corridor runs north and south, the way through clear now."
_TRAP19 = "an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it"
_TRAP_DISARMED = "You spot {d} and are able to disarm it, neutralizing it."
_TRAP_BOTCHED = "You see {d}, but your attempt to disarm it fails miserably."
_SHOCK = (
    "Your hands close on the bars and the charge goes through you — a white "
    "snap, a smell like a struck match. When you can think again, you're on the floor."
)
_LIFTED = (
    "You get under the portcullis and heave. It rises, grinding, until it's "
    "head-high — and stays there only as long as you hold it."
)
_LIFT_FAILS = "You strain against the portcullis. It shifts an inch and settles back."
_DROPS = "You let go. The portcullis slams back down."
_PROPPED = (
    "You wedge the iron bar under the portcullis. It takes the weight with a "
    "groan and holds. The way south is open."
)
_PROPPED_FROM_SOUTH = (
    "You wedge the iron bar under the portcullis. It takes the weight with a "
    "groan and holds. The way north is open."
)
_DOWN = "The portcullis is down."

_SHRINE = (
    "The room is older than the dungeon around it — the stonework finer, the "
    "walls carved rather than cut. Someone built this with intention. A shallow "
    "bowl depression is set into a stone plinth at the center. The air is "
    "stiller here than in the corridors outside, as if the room has been "
    "holding its breath for a long time. A corridor leads north; to the south, "
    "the floor gives way to a narrow stone bridge."
)
SHRINE_PIECE = (
    "Something catches your eye near the base of the plinth — a curved "
    "fragment, stone, fitting the bowl's edge exactly."
)

_BRIDGE = (
    "A narrow stone bridge over a gap in the dungeon floor. The bridge is old — "
    "the stones have shifted slightly in their mortar, the edges worn. It looks "
    "crossable. It probably is. The far side leads south to a heavy iron door. "
    "To the north, a carved doorway leads into an older room."
)
BRIDGE_WEST_SHUT = "A side passage to the west is choked with debris."
_BRIDGE_WEST_OPEN = "To the west, a side passage leads back toward the Collapsed Gallery."
_OVERWEIGHT = (
    "The bridge groans under your load — a deep, unhappy sound from somewhere "
    "in the stone. It isn't going to hold. You'll need to lighten what you're carrying."
)
_KEY_DOOR = (
    "The door is iron, set deep into the stone. The lock is substantial — no "
    "amount of forcing will open this. It wants a key."
)
_KEY_DOOR_OPEN = (
    "The iron door stands open, the finch key still in its lock. Stone stairs "
    "lead down to the south."
)
_KEY_DOOR_BACK = "The bridge is back to the north."   # LOOK only — _KEY_DOOR is also the refusal
_KEY_TURNS = (
    "The finch key goes in stiffly and turns with a sound like a dropped anvil. "
    "The iron door swings inward under its own weight. Beyond it, stone stairs "
    "lead down. You leave the key in the lock."
)
_WRONG_KEY = "That key doesn't fit."


# ---------------------------------------------------------------------------
# Prayer Alcove
# ---------------------------------------------------------------------------

def niche_check(w: World) -> bool:
    """Prayer Alcove: Easy, once per visit until the niche is found. Shown with
    the room description."""
    if w.get_global("NICHE-FOUND"):
        return False
    from content.player import check_perception
    from content.perception import EASY
    if not check_perception(w, EASY):
        return False
    w.set_global("NICHE-FOUND", "pending")
    for name in ("CROWBAR", "GLACIER-MELT"):
        w.objects[name].clear_flag("INVISIBLE")
    return True


def alcove_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        niche_check(w)                  # once per visit (SEARCH: one more)
    elif msg == M_LOOK:
        print(_ALCOVE)
        if w.get_global("NICHE-FOUND") == "pending":
            w.set_global("NICHE-FOUND", True)
            print(_NICHE_FOUND)
        return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Portcullis Corridor (Trap 19)
# ---------------------------------------------------------------------------

def _state(w: World) -> str:
    return w.get_global("PORTCULLIS") or "charged"


def portcullis_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        state = _state(w)
        extra = {"charged": _PORT_CHARGE, "discharged": "", "propped": _PORT_PROPPED}[state]
        exits = _PORT_EXITS_OPEN if state == "propped" else _PORT_EXITS_SHUT
        print(_PORT_BASE + extra + exits)
        return M_HANDLED
    if msg == M_ENTER:
        w.set_global("ARRIVED-PORTCULLIS", True)
    elif msg == M_END:
        held = w.get_global("PORTCULLIS-HELD")
        if held is not None and w.moves > held:
            # Anything other than USE PORTCULLIS BAR straight after lifting
            w.set_global("PORTCULLIS-HELD", None)
            print(_DROPS)
        if w.get_global("ARRIVED-PORTCULLIS"):
            w.set_global("ARRIVED-PORTCULLIS", False)
            if _state(w) == "charged" and not w.get_global("TRAP19-CHECKED"):
                _check_trap19(w)
    return M_NOT_HANDLED


def _check_trap19(w: World) -> None:
    w.set_global("TRAP19-CHECKED", True)
    from content.player import check_perception, roll_class_bonus
    from content.perception import MEDIUM
    if not check_perception(w, MEDIUM):
        return                         # the charge goes unnoticed until touched
    if roll_class_bonus(w, "trap") >= MEDIUM:
        print(_TRAP_DISARMED.format(d=_TRAP19))
        w.set_global("PORTCULLIS", "discharged")
        from content.experience import award_xp
        award_xp(w, 5 + (5 if w.globals.get("player_class") == "rogue" else 0))
    else:
        print(_TRAP_BOTCHED.format(d=_TRAP19))
        _shock(w)


def _shock(w: World) -> None:
    from content.combat import _take_damage
    print(_SHOCK)
    _take_damage(w, 1)
    if not w.get_global("GAME-OVER"):
        w.game.clock.tick(w, command_parsed=True)   # stunned: lose a turn


def lift(w: World) -> None:
    if w.here is None or w.here.name != "PORTCULLIS-CORRIDOR":
        print("There's nothing here to lift.")
    elif _state(w) == "propped":
        print("It's already propped open.")
    elif _state(w) == "charged":
        _shock(w)
    else:
        from content.player import roll_class_bonus
        from content.perception import MEDIUM
        if roll_class_bonus(w, "strength") >= MEDIUM:
            print(_LIFTED)
            w.set_global("PORTCULLIS-HELD", w.moves)
        else:
            print(_LIFT_FAILS)


def portcullis_held(w: World) -> bool:
    """True right after a successful LIFT PORTCULLIS, while it's still up."""
    return (w.here is not None and w.here.name == "PORTCULLIS-CORRIDOR"
            and w.get_global("PORTCULLIS-HELD") is not None)


def use_bar(w: World) -> bool:
    """USE PORTCULLIS BAR. Returns True if handled here."""
    if w.here is None or w.here.name != "PORTCULLIS-CORRIDOR":
        return False
    if w.get_global("PORTCULLIS-HELD") is None:
        print(_DOWN)
        return True
    w.set_global("PORTCULLIS-HELD", None)
    w.set_global("PORTCULLIS", "propped")
    w.ways_changed("PORTCULLIS-CORRIDOR")
    w.move_object(w.objects["PORTCULLIS-BAR"], None)   # stays in the portcullis
    print(_PROPPED_FROM_SOUTH if _side(w) == "south" else _PROPPED)
    return True


def _side(w: World) -> str:
    """Which side of the portcullis the player is on: "north" (from the Prayer
    Alcove) or "south" (from the Shrine Room, by the Quest 38 shortcut)."""
    return w.get_global("PORTCULLIS-SIDE") or "north"


class _IntoCorridor(Exit):
    """Into the Portcullis Corridor: you arrive on the side you came from."""

    def resolve(self, world):
        room, msg = super().resolve(world)
        if room is not None:
            from_south = world.here is not None and world.here.name == "SHRINE-ROOM"
            world.set_global("PORTCULLIS-SIDE", "south" if from_south else "north")
        return room, msg


class _PortcullisExit(Exit):
    """Out of the corridor past the portcullis — only the side you're on is open
    until it's propped."""

    def __init__(self, destination, beyond):
        super().__init__(destination=destination)
        self.beyond = beyond               # the side this exit leads to

    def resolve(self, world):
        if _state(world) != "propped" and _side(world) != self.beyond:
            return None, _DOWN
        room, msg = super().resolve(world)
        if room is not None and world.get_global("PORTCULLIS-HELD") is not None:
            world.set_global("PORTCULLIS-HELD", None)   # walking off lets go
            print(_DROPS)
        return room, msg


# ---------------------------------------------------------------------------
# Shrine Room, Rickety Bridge, Mid-Tier Key Door
# ---------------------------------------------------------------------------

def shrine_piece_check(w: World) -> bool:
    """Shrine Room: the shrine bowl piece, Easy, every visit (and SEARCH)."""
    from content.perception import EASY, reveal_if_found
    return reveal_if_found(w, "BOWL-PIECE-SHRINE", EASY)


def shrine_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        shrine_piece_check(w)
    return M_NOT_HANDLED


def carried_weight(w: World) -> int:
    def total(container) -> int:
        return sum(o.size + total(o) for o in container.contents)
    return total(w.player)


class _BridgeExit(Exit):
    def resolve(self, world):
        if carried_weight(world) > WEIGHT_LIMIT:
            return None, _OVERWEIGHT
        return super().resolve(world)


def bridge_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        # The iron door is in sight from the bridge — Quest 32 is discovered
        from content import quests
        quests.discover(w, "32")
    elif msg == M_LOOK:
        from content.aqueduct import shortcut_open
        print(_BRIDGE)
        print(_BRIDGE_WEST_OPEN if shortcut_open(w) else BRIDGE_WEST_SHUT)
        return M_HANDLED
    return M_NOT_HANDLED


def key_door_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        door = _KEY_DOOR_OPEN if w.get_global("KEY-DOOR-UNLOCKED") else _KEY_DOOR
        print(door + " " + _KEY_DOOR_BACK)
        return M_HANDLED
    return M_NOT_HANDLED


def unlock_key_door(w: World) -> None:
    if w.get_global("KEY-DOOR-UNLOCKED"):
        print("It's already unlocked. The key is still in the lock.")
        return
    key = w.objects["MIDDLE-TIER-KEY"]
    if w.prsi is not None and w.prsi is not key:
        print(_WRONG_KEY)
        return
    if key not in w.player.contents:
        print(_KEY_DOOR)
        return
    print(_KEY_TURNS)
    w.set_global("KEY-DOOR-UNLOCKED", True)
    w.ways_changed("MID-TIER-KEY-DOOR")
    w.move_object(key, w.objects["MID-TIER-DOOR"])   # stays in the lock


class _KeyDoor(Exit):
    def resolve(self, world):
        if not world.get_global("KEY-DOOR-UNLOCKED"):
            return None, _KEY_DOOR
        return super().resolve(world)


def make_rooms(world) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    alcove = room("PRAYER-ALCOVE", "Prayer Alcove", "", value=2)
    port = room("PORTCULLIS-CORRIDOR", "Portcullis Corridor", "")
    shrine = room("SHRINE-ROOM", "Shrine Room", _SHRINE)
    bridge = room("RICKETY-BRIDGE", "Rickety Bridge", "")   # bridge_action: the west line changes
    door = room("MID-TIER-KEY-DOOR", "Mid-Tier Key Door", "")   # key_door_action: locked / open

    world.rooms["COMBAT-ROOM"].exits["south"] = Exit(destination="PRAYER-ALCOVE")
    alcove.exits.update(north=Exit(destination="COMBAT-ROOM"), south=_IntoCorridor(destination="PORTCULLIS-CORRIDOR"))
    port.exits.update(north=_PortcullisExit("PRAYER-ALCOVE", beyond="north"),
                      south=_PortcullisExit("SHRINE-ROOM", beyond="south"))
    shrine.exits.update(north=_IntoCorridor(destination="PORTCULLIS-CORRIDOR"), south=Exit(destination="RICKETY-BRIDGE"))
    # Rickety Bridge west → Collapsed Gallery is gated by Quest 38
    bridge.exits.update(north=Exit(destination="SHRINE-ROOM"), south=_BridgeExit(destination="MID-TIER-KEY-DOOR"))
    # Key Door north crosses the bridge too; south → Key Door Landing (mid tier, content/mid_tier.py)
    door.exits.update(north=_BridgeExit(destination="RICKETY-BRIDGE"), south=_KeyDoor(destination="KEY-DOOR-LANDING"))

    alcove.action = alcove_action
    port.action = portcullis_action
    shrine.action = shrine_action
    bridge.action = bridge_action
    door.action = key_door_action
