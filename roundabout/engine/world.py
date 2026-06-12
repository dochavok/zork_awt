"""
World model: rooms, objects, flags, and the game world container.

Mirrors the ZIL object/room system from 1dungeon.zil and gglobals.zil.
The engine layer is content-agnostic; all Zork-specific data lives in content/.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Optional, Union

# ---------------------------------------------------------------------------
# Flag constants
# These mirror ZIL FLAGS/FSET? semantics. Stored as frozensets on each object.
# ---------------------------------------------------------------------------

# Object flags
TAKEBIT    = "TAKEBIT"    # player can pick this up
CONTBIT    = "CONTBIT"    # is a container
OPENBIT    = "OPENBIT"    # container/door is currently open
TRYTAKEBIT = "TRYTAKEBIT" # run object's action before attempting take
NDESCBIT   = "NDESCBIT"   # suppress from automatic room-contents listing
BURNBIT    = "BURNBIT"    # can be set on fire
READBIT    = "READBIT"    # has readable text
TURNBIT    = "TURNBIT"    # can be turned/wound
ACTORBIT   = "ACTORBIT"   # is an NPC / actor
WEAPONBIT  = "WEAPONBIT"  # usable as a weapon
CLIMBBIT   = "CLIMBBIT"   # can be climbed
DRINKBIT   = "DRINKBIT"   # can be consumed
DOORBIT    = "DOORBIT"    # is a door object
TOOLBIT    = "TOOLBIT"    # is a tool (e.g. hands, weapon slot)
INVISIBLE  = "INVISIBLE"  # not shown or described anywhere
SACREDBIT  = "SACREDBIT"  # cannot be taken by player
SURFACEBIT = "SURFACEBIT" # objects can be placed on top of it
TOUCHBIT   = "TOUCHBIT"   # has been interacted with at least once
RMUNGBIT   = "RMUNGBIT"   # room/object description has been changed
TRANSBIT   = "TRANSBIT"   # transparent container (contents visible when closed)
WEARBIT    = "WEARBIT"    # currently being worn
VEHBIT     = "VEHBIT"     # is a vehicle the player can enter
SEARCHBIT  = "SEARCHBIT"  # has already been searched
FIGHTBIT   = "FIGHTBIT"   # currently engaged in combat
STAGGERED  = "STAGGERED"  # fighter is staggered (combat state)

# Room flags
ONBIT    = "ONBIT"    # room is lit (or lamp/light source is on)
RLANDBIT = "RLANDBIT" # room is above ground (outdoors/land)
SACREDBIT_ROOM = SACREDBIT  # same bit: player cannot drop items here

# Convenient aliases used in engine logic
LIT = ONBIT


# ---------------------------------------------------------------------------
# Exit
# ---------------------------------------------------------------------------

@dataclass
class Exit:
    """
    One directional connection out of a room.

    destination  -- name of the target Room, or None if the exit is blocked
    message      -- text shown when the exit is blocked (destination is None)
                    or as a narration when passing through (destination set)
    condition    -- optional callable(World) -> bool; if provided the exit
                    is only passable when it returns True, otherwise the
                    fail_message is shown instead
    fail_message -- shown when condition returns False
    """
    destination: Optional[str] = None
    message: Optional[str] = None
    condition: Optional[Callable[[World], bool]] = None
    fail_message: Optional[str] = None

    def resolve(self, world: World) -> tuple[Optional[Room], Optional[str]]:
        """
        Evaluate this exit in the current world state.

        Returns (room, None) on success, or (None, message) on failure.
        """
        if self.condition is not None and not self.condition(world):
            return None, self.fail_message or "You can't go that way."
        if self.destination is None:
            return None, self.message or "You can't go that way."
        room = world.rooms.get(self.destination)
        if room is None:
            return None, "You can't go that way."
        return room, self.message  # message may be a narration (rare)


# ---------------------------------------------------------------------------
# GameObject
# ---------------------------------------------------------------------------

@dataclass
class GameObject:
    """
    Any entity in the world: item, NPC, scenery, or the player.

    Mirrors ZIL <OBJECT> with its properties and FLAGS.
    """
    name: str

    # Vocabulary used by the parser
    synonyms:   list[str] = field(default_factory=list)
    adjectives: list[str] = field(default_factory=list)

    # Descriptions
    desc:  str = ""   # short label used in listings ("brass lantern")
    fdesc: str = ""   # first-time room description (before player touches it)
    ldesc: str = ""   # subsequent room description
    text:  str = ""   # readable content (READBIT objects)

    # Properties mirroring ZIL PROPDEFs
    size:     int = 5   # bulk; default from <PROPDEF SIZE 5>
    capacity: int = 0   # how much it can hold (0 = not a container)
    value:    int = 0   # base score value
    tvalue:   int = 0   # trophy-case score value
    strength: int = 0   # combat strength (actors)

    # Flags — use the constants above
    flags: set[str] = field(default_factory=set)

    # Action handler: callable(world, verb, prso, prsi) or None
    # Signature mirrors ZIL ROUTINE called via PERFORM
    action: Optional[Callable] = None

    # Content-of function: called when something is placed inside this object
    contfcn: Optional[Callable] = None

    # ---- runtime-only state (not part of world definition) ----

    # Where this object currently is: a Room, another GameObject, or None
    _location: Optional[Union[Room, GameObject]] = field(
        default=None, init=False, repr=False
    )

    # Objects directly inside this object (if CONTBIT)
    contents: list[GameObject] = field(default_factory=list, init=False)

    # True once the player has seen/taken this object (tracks fdesc vs ldesc)
    touched: bool = field(default=False, init=False)

    # ---- flag helpers ----

    def has_flag(self, flag: str) -> bool:
        return flag in self.flags

    def set_flag(self, flag: str) -> None:
        self.flags.add(flag)

    def clear_flag(self, flag: str) -> None:
        self.flags.discard(flag)

    # ---- location helpers ----

    @property
    def location(self) -> Optional[Union[Room, GameObject]]:
        return self._location

    def containing_room(self) -> Optional[Room]:
        """Walk up the container chain to find the room this object is in."""
        loc = self._location
        while isinstance(loc, GameObject):
            loc = loc._location
        return loc if isinstance(loc, Room) else None

    def is_in(self, container: Union[Room, GameObject]) -> bool:
        return self._location is container

    def contents_size(self) -> int:
        """Total bulk of objects directly inside this object."""
        return sum(o.size for o in self.contents)

    def can_hold(self, obj: GameObject) -> bool:
        """True if this container has room for obj."""
        return self.capacity > 0 and self.contents_size() + obj.size <= self.capacity

    def __repr__(self) -> str:
        return f"<GameObject {self.name!r}>"


# ---------------------------------------------------------------------------
# Room
# ---------------------------------------------------------------------------

@dataclass
class Room:
    """
    A location in the world.

    Mirrors ZIL <ROOM> with its direction exits, flags, globals, and action.
    """
    name: str
    desc: str  # short title shown in brief/normal mode

    ldesc: str = ""  # long description shown in verbose / first-visit

    # Direction exits: keys are direction names ('north', 'south', …)
    exits: dict[str, Exit] = field(default_factory=dict)

    # Room-level flags
    flags: set[str] = field(default_factory=set)

    # Names of objects always accessible from here regardless of their location
    # (ZIL GLOBAL property on rooms — e.g. WHITE-HOUSE visible from nearby rooms)
    global_objects: list[str] = field(default_factory=list)

    # Room action: called with (world, message_type) at begin/end of each turn
    action: Optional[Callable] = None

    # Exploration score: awarded once when player first enters this room (ZIL VALUE property)
    value: int = 0

    # ---- runtime-only state ----

    # Objects whose _location is this room right now
    contents: list[GameObject] = field(default_factory=list, init=False)

    # True once the player has visited (controls ldesc vs desc display)
    visited: bool = field(default=False, init=False)

    # ---- flag helpers ----

    def has_flag(self, flag: str) -> bool:
        return flag in self.flags

    def set_flag(self, flag: str) -> None:
        self.flags.add(flag)

    def clear_flag(self, flag: str) -> None:
        self.flags.discard(flag)

    def is_lit(self) -> bool:
        return self.has_flag(ONBIT)

    def __repr__(self) -> str:
        return f"<Room {self.name!r}>"


# ---------------------------------------------------------------------------
# World
# ---------------------------------------------------------------------------

class World:
    """
    The complete game state: rooms, objects, player, and global variables.

    Content modules call register_room() / register_object() to populate the
    world, then call initialize() to wire up location references.
    """

    def __init__(self) -> None:
        self.rooms:   dict[str, Room]       = {}
        self.objects: dict[str, GameObject] = {}

        # Player character (set by content init)
        self.player: Optional[GameObject] = None

        # Current room the player (winner) is in
        self.here: Optional[Room] = None

        # Current acting character (usually == player, changes during NPC turns)
        self.winner: Optional[GameObject] = None

        # Last object referenced in a command (resolved "it"/"them")
        self.it_object: Optional[GameObject] = None

        # Current verb/action (set by Game.perform; used by content handlers)
        self.prsa: Optional[str] = None
        # Primary object (direct object) of current command
        self.prso: Optional[GameObject] = None
        # Secondary object (indirect object) of current command
        self.prsi: Optional[GameObject] = None

        # Direction of current walk command (set by Game._dispatch)
        self.walk_dir: Optional[str] = None

        # Back-reference to the Game instance (set by Game.__init__)
        self.game: Optional[object] = None

        # Score and turn counter
        self.score:     int = 0
        self.score_max: int = 350
        self.moves:     int = 0

        # Arbitrary named globals used by content (mirrors ZIL <GLOBAL> vars)
        # e.g. world.globals["WON-FLAG"] = False
        self.globals: dict[str, object] = {}

        # Load-bearing capacity globals (ZIL LOAD-MAX / LOAD-ALLOWED)
        self.load_max:     int = 100
        self.load_allowed: int = 100

    # ------------------------------------------------------------------ #
    # Registration                                                         #
    # ------------------------------------------------------------------ #

    def register_room(self, room: Room) -> Room:
        self.rooms[room.name] = room
        return room

    def register_object(self, obj: GameObject) -> GameObject:
        self.objects[obj.name] = obj
        return obj

    # ------------------------------------------------------------------ #
    # Location management                                                  #
    # ------------------------------------------------------------------ #

    def move_object(
        self,
        obj: GameObject,
        destination: Union[Room, GameObject, None],
    ) -> None:
        """Move obj to destination (Room, container GameObject, or None)."""
        old_loc = obj._location
        if old_loc is not None:
            if isinstance(old_loc, Room):
                old_loc.contents.remove(obj)
            elif isinstance(old_loc, GameObject):
                old_loc.contents.remove(obj)

        obj._location = destination
        if destination is not None:
            if isinstance(destination, Room):
                destination.contents.append(obj)
            elif isinstance(destination, GameObject):
                destination.contents.append(obj)

    def place_object(self, obj_name: str, location_name: str) -> None:
        """
        Resolve names and call move_object.  Used during world initialization.
        location_name may be a Room name or a GameObject name.
        """
        obj = self.objects.get(obj_name)
        if obj is None:
            raise KeyError(f"Unknown object: {obj_name!r}")
        dest: Union[Room, GameObject, None] = self.rooms.get(location_name)
        if dest is None:
            dest = self.objects.get(location_name)
        if dest is None:
            raise KeyError(f"Unknown location: {location_name!r}")
        self.move_object(obj, dest)

    # ------------------------------------------------------------------ #
    # Accessors                                                            #
    # ------------------------------------------------------------------ #

    def player_inventory(self) -> list[GameObject]:
        """Objects directly carried by the player."""
        if self.player is None:
            return []
        return list(self.player.contents)

    def player_load(self) -> int:
        """Total bulk currently carried."""
        return sum(o.size for o in self.player_inventory())

    def room_contents(self, room: Optional[Room] = None) -> list[GameObject]:
        """Objects physically in a room (not inside containers)."""
        r = room or self.here
        return list(r.contents) if r else []

    def global_objects_for(self, room: Optional[Room] = None) -> list[GameObject]:
        """Objects that are globally accessible from a room."""
        r = room or self.here
        if r is None:
            return []
        result = []
        for name in r.global_objects:
            obj = self.objects.get(name)
            if obj is not None:
                result.append(obj)
        return result

    def is_accessible(self, obj: GameObject) -> bool:
        """
        True if the player can currently see and interact with obj.

        An object is accessible if it is:
        - carried by the player, or inside something carried,
        - in the current room (or inside an open container in the room),
        - a global object for the current room.
        """
        if obj in self.player_inventory():
            return True
        if self._in_open_chain(obj, self.player):
            return True
        if self.here and obj in self.here.contents:
            return True
        if self.here and self._in_open_room_container(obj):
            return True
        if obj in self.global_objects_for():
            return True
        return False

    def _in_open_chain(self, obj: GameObject, container: Optional[GameObject]) -> bool:
        """True if obj is nested inside container through open containers."""
        if container is None:
            return False
        for item in container.contents:
            if item is obj:
                return True
            if item.has_flag(CONTBIT) and (item.has_flag(OPENBIT) or item.has_flag(TRANSBIT)):
                if self._in_open_chain(obj, item):
                    return True
        return False

    def _in_open_room_container(self, obj: GameObject) -> bool:
        """True if obj is inside an open container that is in the current room."""
        if self.here is None:
            return False
        for item in self.here.contents:
            if item.has_flag(CONTBIT) and (item.has_flag(OPENBIT) or item.has_flag(TRANSBIT)):
                if self._in_open_chain(obj, item):
                    return True
        return False

    def is_lit(self) -> bool:
        """
        True if the current location is lit.

        A room is lit if:
        - it has the ONBIT (outdoor / permanently lit), or
        - a lit light source is in the room or in the player's inventory.
        """
        if self.here is None:
            return False
        if self.here.is_lit():
            return True
        return self._has_light_source(self.here) or self._has_light_source(self.player)

    def _has_light_source(self, container: Optional[Union[Room, GameObject]]) -> bool:
        """Recursively check for a lit light source inside container."""
        if container is None:
            return False
        items = container.contents if isinstance(container, GameObject) else container.contents
        for obj in items:
            if obj.has_flag(ONBIT) and not obj.has_flag(INVISIBLE):
                return True
            if obj.has_flag(CONTBIT) and (obj.has_flag(OPENBIT) or obj.has_flag(TRANSBIT)):
                if self._has_light_source(obj):
                    return True
        return False

    # ------------------------------------------------------------------ #
    # Global variable helpers                                              #
    # ------------------------------------------------------------------ #

    def get_global(self, name: str, default: object = None) -> object:
        return self.globals.get(name, default)

    def set_global(self, name: str, value: object) -> None:
        self.globals[name] = value

    def flag_set(self, obj_name: str, flag: str) -> bool:
        """Convenience: check a named object's flag (used in Exit conditions)."""
        obj = self.objects.get(obj_name)
        return obj is not None and obj.has_flag(flag)
