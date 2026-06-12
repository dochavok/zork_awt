"""
Room definitions for Roundabout: The God-Forsaken Ring.

All descriptions sourced from AWT_story_line/locations.md.
XP values per locations.md header: default 1 XP unless noted.
Dungeon lower tier: 2 XP. Trap side mid-tier: 2 XP.
Burial Chamber: 3 XP. Skeleton Room: 0 XP. Ocean squares: 0 XP.
Kevry's Island rooms: 5 XP each.

Dark rooms (no ONBIT): all dungeon tiers, Secret Tunnels, Crypt/Mausoleum.
Lit rooms (ONBIT): overworld, town, mine (active torches), bog, beach, sea.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from engine.world import Room, Exit, ONBIT

if TYPE_CHECKING:
    from engine.world import World


def make_rooms(world: "World") -> None:
    """Register all rooms. Called by initialize_world()."""
    _make_opening_area(world)
    _make_wills_tower(world)
    _make_main_street(world)
    _make_town_hall(world)
    _make_tale_and_ale(world)
    _make_library(world)
    _make_church_of_all(world)
    _make_graveyard(world)
    _make_chuckle_house(world)
    _make_wasteland_volcano(world)
    _make_archery_vikings(world)
    _make_pond_bog(world)
    _make_beach_forest_mine(world)
    _make_beach_sea(world)
    _make_secret_tunnels(world)
    _make_dungeon_upper(world)
    _make_dungeon_mid_key(world)
    _make_dungeon_mid_trap(world)
    _make_dungeon_lower(world)


# ---------------------------------------------------------------------------
# Opening area
# ---------------------------------------------------------------------------

def _make_opening_area(world: "World") -> None:
    from engine.game import M_BEG, M_HANDLED

    room = Room(
        name="white-house",
        desc="White House",
        ldesc=(
            "A white clapboard house stands in a field, west of nothing in particular. "
            "A mailbox stands by the path."
        ),
        exits={},
        flags={ONBIT},
        value=1,
    )

    _ALLOWED = {"V-OPEN", "V-QUIT", "V-LOOK", "V-EXAMINE", "V-INVENTORY"}

    def _white_house_action(w, msg):
        if msg != M_BEG:
            return None
        if w.prsa in _ALLOWED:
            return None
        print("What does this look like? A Great Underground Empire?")
        return M_HANDLED

    room.action = _white_house_action
    world.register_room(room)


# ---------------------------------------------------------------------------
# Will's Wizard Tower
# ---------------------------------------------------------------------------

def _make_wills_tower(world: "World") -> None:
    world.register_room(Room(
        name="wills-tower-main",
        desc="Will's Wizard Tower",
        ldesc=(
            "The tower doesn't announce itself. It simply is — books, firelight, the low hum of "
            "something you can't quite locate. A desk dominates one end, buried under papers that "
            "somehow manage to look organized. A painting hangs on the wall, slightly crooked. "
            "The room has the feeling of a place where important things happen without any particular fuss."
        ),
        exits={
            "out":   Exit(destination="main-west"),
            "south": Exit(destination="main-west"),
            "up":    Exit(destination="wills-bedroom"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="wills-bedroom",
        desc="Will's Bedroom",
        ldesc=(
            "This is, apparently, where the magic happens. The bedroom is smaller than the main room "
            "and considerably more honest about its occupant.\n"
            "Books here are not organized — they are stacked, wedged, balanced, and in at least one "
            "case load-bearing.\n"
            "A narrow bed sits against the far wall, made with the perfunctory neatness of someone "
            "who knows they'll be up again soon.\n"
            "A nightstand holds a pair of wire-rimmed glasses, a half-melted candle, and a ring "
            "left by a cup that was never there long enough to matter.\n"
            "The rest of the room is Will's business and clearly has been for a very long time."
        ),
        exits={"down": Exit(destination="wills-tower-main")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Roundabout Town — Main Street
# ---------------------------------------------------------------------------

def _make_main_street(world: "World") -> None:
    world.register_room(Room(
        name="main-west",
        desc="Main West",
        ldesc=(
            "Main Street narrows toward the west end, the buildings pulling back slightly as if "
            "making room for something that never arrived. The library stands to the north, solid "
            "and unhurried. The road continues west toward the archery range. To the southeast, "
            "a gap between buildings leads into the alley."
        ),
        exits={
            "east":      Exit(destination="town-square"),
            "north":     Exit(destination="library-main-hall"),
            "southeast": Exit(destination="the-alley"),
            "west":      Exit(destination="tale-and-ale-main",
                              message="The mailbox shimmers. You are somewhere else entirely."),
            "in":        Exit(destination="tale-and-ale-main",
                              message="The mailbox shimmers. You are somewhere else entirely."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="town-square",
        desc="Roundabout Town Square",
        ldesc=(
            "The square is the kind of place a town organizes itself around without quite deciding to. "
            "Cobblestones, worn smooth at the center.\n"
            "The Town Hall anchors the north end with the authority of a building that has never "
            "doubted its own importance. The tavern faces it from the south, which seems about right.\n"
            "A fountain stands in the middle — dry, the basin cracked at one edge, the stonework "
            "patient in the way of things that have been waiting a long time.\n"
            "A stone statue stands to one side — a civic figure of some kind, the plaque below "
            "it worn to illegibility."
        ),
        exits={
            "west":      Exit(destination="main-west"),
            "east":      Exit(destination="main-east"),
            "north":     Exit(destination="town-hall-exterior"),
            "south":     Exit(destination="tale-and-ale-main"),
            "southwest": Exit(destination="the-alley"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="main-east",
        desc="Main East",
        ldesc=(
            "Main Street ends here, or nearly does. The buildings thin out toward the east — a few "
            "shuttered fronts, a sign that's lost its lettering, the church standing apart to the "
            "south as though it chose its distance deliberately. The wasteland begins where the "
            "cobblestones stop."
        ),
        exits={
            "west":  Exit(destination="town-square"),
            "south": Exit(destination="church-nave"),
            "east":  Exit(destination="roundabout-wasteland"),
            "north": Exit(destination="roundabout-pond"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-alley",
        desc="The Alley",
        ldesc=(
            "The gap between buildings is narrow enough that the sky above is just a strip. "
            "Cobblestones give way to packed dirt underfoot.\n"
            "The tavern's back wall runs along the south side. It smells like kitchen waste and "
            "something less identifiable. Further south, the alley deepens."
        ),
        exits={
            "north":     Exit(destination="town-square"),
            "northwest": Exit(destination="main-west"),
            "south":     Exit(destination="back-alley"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="back-alley",
        desc="The Back Alley",
        ldesc=(
            "Darker than the alley, smaller, and considerably less welcoming. The tavern's back "
            "wall seals the south end. Broken crates and barrels have accumulated here the way "
            "things do when no one is watching. The ground is stained. The air is close. This is "
            "where things happen that don't happen on Main Street."
        ),
        exits={"north": Exit(destination="the-alley")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Town Hall
# ---------------------------------------------------------------------------

def _make_town_hall(world: "World") -> None:
    world.register_room(Room(
        name="town-hall-exterior",
        desc="Town Hall Exterior",
        ldesc=(
            "The Town Hall in Roundabout dominates the northern side of the town square. "
            "It is a massive brick building with two floors, a broad sloped roof, and a tower "
            "with a conical roof in the center. The double doors are solid oak and very heavy."
        ),
        exits={
            "south": Exit(destination="town-square"),
            "in":    Exit(destination="council-chamber"),
            "north": Exit(destination="council-chamber"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="council-chamber",
        desc="Council Chamber",
        ldesc=(
            "The room where Roundabout conducts its official business, which is to say the room "
            "where Roundabout sits in chairs and argues.\n"
            "A long table dominates the center — solid oak, scarred from use. The chairs around "
            "it are mismatched in the way of things that have been replaced one at a time over "
            "many years.\n"
            "A man sits at the far end with the bearing of someone who has inherited both the "
            "title and the table."
        ),
        exits={
            "south": Exit(destination="town-hall-exterior"),
            "out":   Exit(destination="town-hall-exterior"),
            "up":    Exit(destination="upper-hall"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="records-room",
        desc="Records Room",
        ldesc=(
            "Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents "
            "in an order that apparently makes sense to someone.\n"
            "The room smells of old paper and the particular dust of things that have not been "
            "touched in years.\n"
            "A clerk sits at a desk near the window, surrounded by more of the same. He looks "
            "up when you enter with the expression of a man who was hoping you wouldn't."
        ),
        exits={"west": Exit(destination="upper-hall")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="upper-hall",
        desc="Upper Hall",
        ldesc=(
            "The second floor is quieter than the ground floor in the way that second floors "
            "always are — the noise of official business doesn't quite reach here.\n"
            "A long hall with a runner of carpet gone thin at the center.\n"
            "A display cabinet stands against the wall, unlocked, glass-fronted, holding an "
            "assortment of old civic documents and artifacts. The kind of things a town keeps "
            "because no one has decided to throw them away."
        ),
        exits={
            "down":  Exit(destination="council-chamber"),
            "east":  Exit(destination="records-room"),
            "west":  Exit(destination="the-tower"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-tower",
        desc="The Tower",
        ldesc=(
            "The tower room is round, the walls following the cone of the roof above. A single "
            "window looks out over the town square, narrow enough that the view is more "
            "suggestion than panorama.\n"
            "The Trophy Case dominates the far wall — old wood and glass, built into the stone "
            "as if someone planned for it from the start. It is empty.\n"
            "The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY "
            "FOR THE GLORY OF ROUNDABOUT.\n"
            "The case has not been added to in some time."
        ),
        exits={"east": Exit(destination="upper-hall")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Tale and Ale Tavern
# ---------------------------------------------------------------------------

def _make_tale_and_ale(world: "World") -> None:
    world.register_room(Room(
        name="tale-and-ale-main",
        desc="Tale and Ale — Main Room",
        ldesc=(
            "The Tale and Ale announces itself with warmth before you're fully through the door — "
            "woodsmoke, something cooking, the low sound of people who have decided their evening "
            "is going well.\n"
            "Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. "
            "A staircase climbs along the east wall.\n"
            "To the north, a doorway leads to a quieter room and the smell of pipe smoke. "
            "In the far northwest corner, someone is throwing dice.\n"
            "The whole room has the quality of a place that has been exactly like this for a long "
            "time and intends to stay that way.\n"
            "Against the wall near the entrance, entirely at odds with everything around it, "
            "stands a mailbox. No one looks at it."
        ),
        exits={
            "south":     Exit(destination="tale-and-ale-bar"),
            "north":     Exit(destination="pipe-room"),
            "northwest": Exit(destination="tys-casino-corner"),
            "up":        Exit(destination="tale-and-ale-upstairs-hall"),
            "east":      Exit(destination="town-square"),
            "out":       Exit(destination="town-square"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="tale-and-ale-bar",
        desc="The Bar",
        ldesc=(
            "The bar runs the length of the south wall — solid oak, worn smooth at the elbows. "
            "Bottles line the shelf behind it in an arrangement that suggests a system only "
            "May understands.\n"
            "She works the bar with the efficiency of someone who has answered every question "
            "before and will answer them all again without complaint.\n"
            "A board on the wall to one side holds notices — quest postings, local announcements, "
            "things people want found or done. The kitchen is further south."
        ),
        exits={
            "north": Exit(destination="tale-and-ale-main"),
            "south": Exit(destination="tale-and-ale-kitchen"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="tys-casino-corner",
        desc="Ty's Casino Corner",
        ldesc=(
            "The northwest corner of the tavern has been claimed so thoroughly it might as well "
            "be a different establishment.\n"
            "A large round table dominates the space, ringed with mismatched chairs. Ty sits at "
            "the head of it — or what he has decided is the head — presiding over the dice with "
            "the calm of a man who has never once worried about the outcome.\n"
            "The noise from the main room reaches here as a comfortable murmur. The game is Cargo: "
            "Ship, Captain, and Crew. The stakes are in Zenni."
        ),
        exits={"southeast": Exit(destination="tale-and-ale-main")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="pipe-room",
        desc="Pipe Room",
        ldesc=(
            "The pipe room is quieter than the rest of the tavern, which appears to be the point.\n"
            "A few low chairs, a side table, the particular haze of an evening's worth of smoke "
            "that has nowhere urgent to be.\n"
            "Conversations here are conducted at a volume that doesn't carry. The kind of room "
            "where people come to think, or to be seen thinking, or to say things they'd rather "
            "not say at the bar."
        ),
        exits={"south": Exit(destination="tale-and-ale-main")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="tale-and-ale-kitchen",
        desc="The Kitchen",
        ldesc=(
            "The kitchen is warm and loud in the way that working kitchens are — pots, fire, the "
            "particular authority of someone who knows exactly what they're doing.\n"
            "Shamus moves through it without wasted motion, cooking and selling in equal measure — "
            "if you need something, he's worth asking.\n"
            "Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates "
            "the center.\n"
            "The cellar door is set into the floor near the far wall; a faint smell of damp rises "
            "from it even when it's shut. The bartender keeps the key."
        ),
        exits={
            "north": Exit(destination="tale-and-ale-bar"),
            "down":  Exit(destination="cellar-storeroom",
                         condition=lambda w: bool(w.globals.get("cellar_key_used")),
                         fail_message="The cellar door is locked. The bartender keeps the key."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="tale-and-ale-upstairs-hall",
        desc="Upstairs Hall",
        ldesc=(
            "The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. "
            "Three doors lead off it — the guest rooms. A window at the far end looks out over "
            "the alley below. The stairs down creak in a specific sequence that regular guests "
            "have learned to navigate quietly."
        ),
        exits={
            "down":  Exit(destination="tale-and-ale-main"),
            "north": Exit(destination="guest-room-1"),
            "east":  Exit(destination="guest-room-2"),
            "west":  Exit(destination="guest-room-3"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="guest-room-1",
        desc="Guest Room",
        ldesc="A plain room, honestly kept. Bed, washstand, a window that looks out over the street. The kind of room that asks nothing of you.",
        exits={"south": Exit(destination="tale-and-ale-upstairs-hall"),
               "out":   Exit(destination="tale-and-ale-upstairs-hall")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="guest-room-2",
        desc="Guest Room",
        ldesc="A corner room, slightly larger than it needs to be. Two windows, a wardrobe that doesn't quite close, a rag rug that was once a specific color. Comfortable in an unassuming way.",
        exits={"west":  Exit(destination="tale-and-ale-upstairs-hall"),
               "out":   Exit(destination="tale-and-ale-upstairs-hall")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="guest-room-3",
        desc="Guest Room",
        ldesc="The smallest of the three rooms, tucked at the end of the hall. Low ceiling, narrow bed, a single candle on the nightstand burned to nothing. Quiet in a way the other rooms aren't.",
        exits={"east":  Exit(destination="tale-and-ale-upstairs-hall"),
               "out":   Exit(destination="tale-and-ale-upstairs-hall")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="cellar-storeroom",
        desc="Cellar / Storeroom",
        ldesc=(
            "The cellar is flooded — dark water covers the floor to knee height, with no obvious "
            "drain. The smell of damp is pervasive. A door to the west is set into the wall "
            "just above the waterline. A drain cover is visible on the floor."
        ),
        exits={
            "up":   Exit(destination="tale-and-ale-kitchen"),
            "west": Exit(destination="secret-tunnels-junction",
                         condition=lambda w: bool(w.globals.get("cellar_drained")),
                         fail_message="The tunnel door opens onto dark, rushing water. Entering would be suicide."),
        },
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Library
# ---------------------------------------------------------------------------

def _make_library(world: "World") -> None:
    world.register_room(Room(
        name="library-main-hall",
        desc="Library Main Hall",
        ldesc=(
            "The library is smaller than the building suggests from outside — half the floor "
            "space is shelving, floor to ceiling, packed in columns with narrow gaps between.\n"
            "A card catalogue occupies one wall. The other holds a reading table, lamp burning "
            "low, a cup of something gone cold.\n"
            "The librarian looks up when you enter. Unlike every librarian you have ever imagined, "
            "she appears to want to talk to you."
        ),
        exits={
            "west":  Exit(destination="main-west"),
            "south": Exit(destination="town-square"),
            "east":  Exit(destination="the-stacks"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-stacks",
        desc="The Stacks",
        ldesc=(
            "The passage from the Main Hall opens into something that shouldn't fit inside this "
            "building.\n"
            "The shelves here are older — darker wood, no labels, arranged in a logic that isn't "
            "immediately obvious and may not be alphabetical. The ceiling is lost somewhere above "
            "the lamplight.\n"
            "At the far end, a large table holds the controlled wreckage of ongoing work: rolled "
            "maps weighted open at the corners, books splayed face-down, sheets of careful notation "
            "in a hand that doesn't waste space.\n"
            "The Archivist sits at the center of it, or rather the work surrounds him and he "
            "happens to be there too."
        ),
        exits={"west": Exit(destination="library-main-hall")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Church of All
# ---------------------------------------------------------------------------

def _make_church_of_all(world: "World") -> None:
    world.register_room(Room(
        name="church-nave",
        desc="Church of All",
        ldesc=(
            "The church is plain inside — stone floor, wooden pews worn smooth, light coming "
            "through narrow windows in thin bars. It could belong to any faith. That appears "
            "to be the point.\n"
            "At the far end, where an altar would normally hold a single symbol, there is instead "
            "a stone altar with a brass dial mounted at its face. Seven marks around the dial. "
            "Whatever is currently selected glows faintly."
        ),
        exits={
            "north":     Exit(destination="main-east"),
            "south":     Exit(destination="graveyard"),
            "east":      Exit(destination="the-altar"),
            "in":        Exit(destination="the-altar"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-altar",
        desc="The Altar",
        ldesc=(
            "The altar is plain stone, unadorned. The dial dominates it — brass, worn at the "
            "edges from use, seven symbols arranged around its face. The currently selected "
            "religion is marked in a faint glow. The air here feels slightly different from "
            "the nave. Not sacred, exactly. Attentive."
        ),
        exits={
            "west":  Exit(destination="church-nave"),
            "out":   Exit(destination="church-nave"),
            "north": Exit(destination="keepers-chamber",
                          condition=lambda w: bool(w.globals.get("keepers_door_unlocked")),
                          fail_message="The door is locked. It needs a key."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="keepers-chamber",
        desc="Keeper's Chamber",
        ldesc=(
            "A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. "
            "The kind of room that belongs to someone who doesn't spend much time in it. On the "
            "desk: a vial of clear liquid, and a note in a careful hand. Whatever the Keeper was "
            "preparing for, he prepared it here."
        ),
        exits={"south": Exit(destination="the-altar")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Graveyard
# ---------------------------------------------------------------------------

def _make_graveyard(world: "World") -> None:
    world.register_room(Room(
        name="graveyard",
        desc="Graveyard",
        ldesc=(
            "The graves here are old, most of them. Headstones lean at angles that suggest the "
            "ground beneath has shifted, or decided it no longer agrees with what's above it. "
            "The church stands to the north. The mausoleum sits at the far end to the south, "
            "grey and patient. The air is still in a way that has nothing to do with wind."
        ),
        exits={
            "north": Exit(destination="church-nave"),
            "south": Exit(destination="the-mausoleum"),
            "west":  Exit(destination="chuckle-house-entrance",
                          condition=lambda w: bool(w.globals.get("chuckle_house_visible")),
                          fail_message="There's nothing to the west but old graves."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-mausoleum",
        desc="The Mausoleum",
        ldesc=(
            "The mausoleum is older than anything around it. The stone is dark with age and "
            "moisture, the carved details worn to suggestions. The door is heavy iron, pitted "
            "with rust but still on its hinges. Whatever family name was once above the entrance "
            "has been lost to weather. Steps descend inside toward the crypt below."
        ),
        exits={
            "north": Exit(destination="graveyard"),
            "out":   Exit(destination="graveyard"),
            "down":  Exit(destination="the-crypt"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-crypt",
        desc="The Crypt",
        ldesc=(
            "The crypt has not been visited recently. Dust lies undisturbed on the stone floor, "
            "on the alcoves, on the remains within them. It is very quiet. Very cold. At the far "
            "end a rough-cut passage opens into darkness — older than the crypt itself, by the "
            "look of the stonework."
        ),
        exits={
            "up":    Exit(destination="the-mausoleum"),
            "south": Exit(destination="charnel-walk"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="lower-crypt",
        desc="Lower Crypt",
        ldesc=(
            "A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the "
            "ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in "
            "robes. Whatever the Keeper came down here to do, this is as far as he got."
        ),
        exits={
            "south": Exit(destination="pile-of-rubble"),
            "north": Exit(destination="thermal-vent-room"),
        },
        flags=set(),  # dark
        value=2,
    ))


# ---------------------------------------------------------------------------
# Chuckle House
# ---------------------------------------------------------------------------

def _make_chuckle_house(world: "World") -> None:
    world.register_room(Room(
        name="chuckle-house-entrance",
        desc="Chuckle House — Entrance",
        ldesc=(
            "The entrance hall is wider than the exterior suggests. A faded runner covers the "
            "floor — the pattern beneath the grime might have been geometric once, or might have "
            "been faces too; it's hard to say now.\n"
            "The ceiling is low and painted, or was. Hooks on the wall where coats or hats once "
            "hung, empty now.\n"
            "A ticket booth stands to one side, the glass cracked, the stool inside still in "
            "place as if whoever left simply forgot to come back.\n"
            "The building has the quality of a held breath."
        ),
        exits={
            "south": Exit(destination="graveyard"),
            "north": Exit(destination="rejection-mirror"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="rejection-mirror",
        desc="The Rejection Mirror",
        ldesc=(
            "A tall mirror in a tarnished frame occupies most of one wall. The glass is clear "
            "enough to show the room — and you, if you're visible. The frame has the look of "
            "something that has been here a long time and intends to stay."
        ),
        exits={
            "south": Exit(destination="chuckle-house-entrance"),
            "north": Exit(destination="shatter-trap-mirror"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="shatter-trap-mirror",
        desc="The Shatter Trap Mirror",
        ldesc=(
            "Another mirror, larger than the last, in a heavier frame. The glass catches the "
            "light in a way that feels watchful. The frame around it has bulk to it — not just "
            "decoration. Something is built into it."
        ),
        exits={
            "south": Exit(destination="rejection-mirror"),
            "north": Exit(destination="ghosts-room"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="ghosts-room",
        desc="Ghost's Room",
        ldesc=(
            "Mirrors on all sides. Whatever this room was meant to show, it shows everything "
            "at once — every angle, every reflection, every version of the space folding back "
            "into itself. The effect is disorienting in a way that stops being interesting quickly.\n"
            "Something is here. Not visible. But present."
        ),
        exits={
            "south": Exit(destination="shatter-trap-mirror"),
        },
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Wasteland, Volcano, Pyronicus
# ---------------------------------------------------------------------------

def _make_wasteland_volcano(world: "World") -> None:
    world.register_room(Room(
        name="roundabout-wasteland",
        desc="Roundabout Wasteland",
        ldesc=(
            "The wasteland sits at the edge of Roundabout like an embarrassing relative. "
            "Something went very wrong here, and not recently.\n"
            "The ground doesn't grow anything. The structures that remain are shells. Whatever "
            "happened, it happened thoroughly.\n"
            "The cause is a matter of some local sensitivity. The prevailing theory among "
            "residents involves adventurers, which explains why no one wants to discuss it "
            "in detail.\n"
            "To the east, a volcano rises against the sky — large, dark, and entirely convincing."
        ),
        exits={
            "west":  Exit(destination="main-east"),
            "east":  Exit(destination="the-volcano"),
            "north": Exit(destination="archery-range"),
            "south": Exit(destination="dungeon-entrance"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-volcano",
        desc="The Volcano",
        ldesc=(
            "It looks entirely real. Heat rises from the ground. The summit is lost in haze. "
            "A harder look reveals an uneven staircase descending into the rock — visible only "
            "now that you're looking for it."
        ),
        exits={
            "west": Exit(destination="roundabout-wasteland"),
            "in":   Exit(destination="pyronicus-forge"),
            "down": Exit(destination="pyronicus-forge"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="pyronicus-forge",
        desc="Pyronicus's Forge",
        ldesc=(
            "The room is large enough that the walls at the far end are suggestion rather than "
            "certainty.\n"
            "Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the "
            "forge light in brief amber before giving it back to the dark.\n"
            "The forge itself dominates the center: enormous, ancient, burning with the steady "
            "purpose of something that has never been allowed to go out.\n"
            "The heat it produces rises through the rock above, feeding an illusion so convincing "
            "that even the smoke smells right.\n"
            "Pyronicus built this room first. The volcano came after."
        ),
        exits={
            "out":  Exit(destination="the-volcano"),
            "up":   Exit(destination="the-volcano"),
        },
        flags={ONBIT},
        value=2,
    ))


# ---------------------------------------------------------------------------
# Archery Range & Viking Encampment
# ---------------------------------------------------------------------------

def _make_archery_vikings(world: "World") -> None:
    world.register_room(Room(
        name="archery-range",
        desc="Archery Range",
        ldesc=(
            "Straw targets line the far end of a long cleared field, bristling with arrows. "
            "The range is well-used.\n"
            "The Vikings from the encampment to the west use it freely — and apparently consider "
            "the entire field fair game, including the parts you're standing in."
        ),
        exits={
            "south": Exit(destination="roundabout-wasteland"),
            "west":  Exit(destination="viking-encampment"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="viking-encampment",
        desc="Viking Encampment",
        ldesc=(
            "A ring of longhouses and cookfires, the smell of roasting meat and oak smoke. "
            "The Brotherhood of the Pale Blade makes its home here.\n"
            "A banner above the main longhouse bears four symbols in sequence. "
            "East leads to the archery range. North leads to Haalvar's Hut. "
            "South leads to the ritual circle. West leads to the fire pit."
        ),
        exits={
            "east":  Exit(destination="archery-range"),
            "north": Exit(destination="haalvar-hut"),
            "south": Exit(destination="ritual-circle"),
            "west":  Exit(destination="fire-pit"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="haalvar-hut",
        desc="Haalvar's Hut",
        ldesc=(
            "A low longhouse, warm inside. A stone sits on a plinth near the center — its surface "
            "has the fluid appearance of dark water, though it is solid to the touch. "
            "Haalvar stands near it with the patience of a man who has asked this question many times."
        ),
        exits={"south": Exit(destination="viking-encampment")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="ritual-circle",
        desc="The Ritual Circle",
        ldesc=(
            "A circle of standing stones, each carved with a rune. Five stones stand at the "
            "compass points and center. An unnamed child stands to one side, watching, but "
            "does not speak."
        ),
        exits={"north": Exit(destination="viking-encampment")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="fire-pit",
        desc="The Fire Pit",
        ldesc=(
            "A fighting pit at the edge of the encampment, ringed with flat stones. "
            "Aylora is here — a broad, calm woman with a cup of something dark in one hand. "
            "She looks at you the way athletes look at things they are about to defeat."
        ),
        exits={"east": Exit(destination="viking-encampment")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Roundabout Pond & Bog
# ---------------------------------------------------------------------------

def _make_pond_bog(world: "World") -> None:
    world.register_room(Room(
        name="roundabout-pond",
        desc="Roundabout Pond",
        ldesc=(
            "The pond is easy to walk past without noticing. It sits low between the town path "
            "and the bog, ringed with reeds and the occasional frog. "
            "The water is dark and calm."
        ),
        exits={
            "west":  Exit(destination="main-east"),
            "east":  Exit(destination="bog-se"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="bog-se",
        desc="Bog of Eternal Stench",
        ldesc=(
            "The bog stretches in every direction, dark water between clumps of soggy earth. "
            "The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. "
            "Something is moving just out of sight, or was."
        ),
        exits={
            "west":      Exit(destination="roundabout-pond"),
            "north":     Exit(destination="bog-ne"),
            "west":      Exit(destination="bog-sw"),
            "northwest": Exit(destination="bog-nw"),
            "east":      Exit(destination="dankhaus-entrance",
                              condition=lambda w: bool(w.globals.get("dankhaus_path_found")),
                              fail_message="Dense brush presses in from the east. There's no way through — or maybe you just haven't found it."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="bog-ne",
        desc="Bog of Eternal Stench",
        ldesc=(
            "The ground here is technically solid. Technically. Dark water pools between tufts "
            "of coarse grass. The smell has layers. You have stopped trying to identify them, "
            "and don't really want to."
        ),
        exits={
            "south": Exit(destination="bog-se"),
            "west":  Exit(destination="bog-nw"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="bog-sw",
        desc="Bog of Eternal Stench",
        ldesc=(
            "A flat expanse of bog, grey-green and indifferent. The water is still except where "
            "it isn't. The smell arrived before you did and will be here long after you leave."
        ),
        exits={
            "north":     Exit(destination="bog-se"),
            "northeast": Exit(destination="bog-nw"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="bog-nw",
        desc="Bog of Eternal Stench",
        ldesc=(
            "The reeds are taller here, crowding in from the edges. The water is darker. The "
            "smell is worse. This part of the bog feels less visited, which is saying something."
        ),
        exits={
            "east":      Exit(destination="bog-ne"),
            "southeast": Exit(destination="bog-se"),
            "south":     Exit(destination="bog-sw"),
        },
        flags={ONBIT},
        value=1,
    ))

    # Dankhaus
    world.register_room(Room(
        name="dankhaus-entrance",
        desc="The Dankhaus",
        ldesc=(
            "The building looks like a yurt from outside — rounded, low, incongruously solid "
            "for something this deep in a bog. The door is plain wood. Something in the air "
            "near it shifts as you approach — not hostile. More like a house that knows you "
            "haven't been introduced yet."
        ),
        exits={
            "west": Exit(destination="bog-se"),
            "in":   Exit(destination="dankhaus-common-room",
                         condition=lambda w: bool(w.globals.get("dankhaus_invited")),
                         fail_message="Something in the air near the door shifts as you approach. Not hostile. More like a house that knows you haven't been introduced yet."),
        },
        flags={ONBIT},
        value=3,  # perception-gated discovery bonus
    ))

    world.register_room(Room(
        name="dankhaus-common-room",
        desc="Dankhaus — Common Room",
        ldesc=(
            "Litlock fills whatever room he's in without trying to. The common room is large "
            "enough, and he's in it — near the fireplace, which is also large, and burning "
            "steadily. Chairs, a table, shelves. The kind of room that works because the people "
            "in it make it work. He looks up."
        ),
        exits={
            "out":   Exit(destination="dankhaus-entrance"),
            "east":  Exit(destination="dankhaus-kitchen"),
            "north": Exit(destination="litlock-room"),
            "south": Exit(destination="lynds-room"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="dankhaus-kitchen",
        desc="Dankhaus — Kitchen",
        ldesc=(
            "A working kitchen — herbs drying overhead, something on the fire, the garden "
            "accessible through the east door. It smells like it has always smelled like this."
        ),
        exits={
            "west": Exit(destination="dankhaus-common-room"),
            "east": Exit(destination="dankhaus-garden"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="dankhaus-garden",
        desc="The Garden",
        ldesc=(
            "The garden shouldn't work. The bog is right there, the soil is wrong, and nothing "
            "about this location suggests flowers or vegetables. And yet. Raised beds, neatly kept. "
            "Things growing that have no business growing here. The Dankhaus wall is to the west. "
            "The bog presses in on every other side and seems to have accepted that it lost this argument."
        ),
        exits={"west": Exit(destination="dankhaus-kitchen")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="litlock-room",
        desc="Litlock's Room",
        ldesc=(
            "A plain room — bed, chest, a low shelf of things that don't announce themselves. "
            "Nothing here suggests the man who laughed until he had to put something down. "
            "That version of Litlock lives in the common room. This one is private."
        ),
        exits={
            "south": Exit(destination="dankhaus-common-room"),
            "east":  Exit(destination="litlock-study"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="litlock-study",
        desc="Litlock's Study",
        ldesc=(
            "The study is where Litlock keeps the part of himself he doesn't lead with. Shelves "
            "of books and things that aren't books. A desk with papers in an order that makes "
            "sense to someone. A candle burned low. The jovial man from the common room was "
            "entirely real — so is this room, and they belong to the same person."
        ),
        exits={"west": Exit(destination="litlock-room")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="lynds-room",
        desc="Lynds's Room",
        ldesc="Lynds's room. Large, untidy, comfortable. The furniture has been through some things.",
        exits={"north": Exit(destination="dankhaus-common-room")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="aurix-room",
        desc="Aurix's Room",
        ldesc=(
            "Small bed, small shelf, the accumulated objects of a child who picks things up "
            "and keeps them. The chalk marks on the floor have been there long enough that "
            "no one is going to do anything about them."
        ),
        exits={"north": Exit(destination="lynds-room")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Beach Road, Forest & Mine
# ---------------------------------------------------------------------------

def _make_beach_forest_mine(world: "World") -> None:
    world.register_room(Room(
        name="beach-road",
        desc="Beach Road",
        ldesc=(
            "A road that forks here — south toward Roundabout Beach, uphill winding toward "
            "Roundabout Forest. The town is behind you to the north."
        ),
        exits={
            "north": Exit(destination="town-square"),
            "south": Exit(destination="roundabout-beach"),
            "west":  Exit(destination="the-old-oak"),
            "east":  Exit(destination="beekeeper-cottage"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-old-oak",
        desc="The Old Oak",
        ldesc=(
            "A vast oak at a crossroads. Something is wedged in the upper branches — a kite, "
            "by the look of it. A child stands nearby, watching it with the particular expression "
            "of someone who has already tried reaching it and knows they can't."
        ),
        exits={
            "east":  Exit(destination="beach-road"),
            "west":  Exit(destination="roundabout-forest"),
            "south": Exit(destination="beekeeper-cottage"),
            "north": Exit(destination="swarm-tree"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="beekeeper-cottage",
        desc="Beekeeper's Cottage",
        ldesc=(
            "A low wooden cottage sits at the edge of the trees, almost part of the forest. "
            "Stacked hive boxes line the south wall, painted in fading colours. The smell of "
            "beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is "
            "here — a broad woman with patience in her posture and a concerning number of sting "
            "marks on her forearms."
        ),
        exits={
            "west":  Exit(destination="beach-road"),
            "north": Exit(destination="the-old-oak"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="swarm-tree",
        desc="Swarm Tree",
        ldesc=(
            "A broad-trunked tree at the forest edge, older than the others around it. A low "
            "drone comes from a dark gap in the bark at chest height. The air nearby has a "
            "quality that suggests strongly you should not approach without a plan."
        ),
        exits={"south": Exit(destination="the-old-oak")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="roundabout-forest",
        desc="Roundabout Forest",
        ldesc=(
            "You wouldn't know, walking through here, that the ground beneath you is hollow. "
            "The forest is peaceful — birdsong, dappled light, the smell of pine.\n"
            "The mine entrance sits somewhere among the roots and undergrowth, easy to miss "
            "if you don't know to look.\n"
            "The crumbled Verdant Circle shrine is visible at the edge of the trees — a carved "
            "pedestal, still solid, holding the remains of a ceramic bowl, smashed and scattered. "
            "The symbol: a sprouting seed inside a circle of leaves."
        ),
        exits={
            "east":  Exit(destination="the-old-oak"),
            "down":  Exit(destination="mine-entrance"),
            "in":    Exit(destination="mine-entrance"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="mine-entrance",
        desc="Mine Entrance",
        ldesc=(
            "The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up "
            "with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — "
            "AUTHORIZED PERSONNEL ONLY. Someone has added, in different handwriting: THIS MEANS YOU. "
            "In another hand: ME? And beneath that, in the first handwriting: NO, NOT YOU SLOTH."
        ),
        exits={
            "up":   Exit(destination="roundabout-forest"),
            "out":  Exit(destination="roundabout-forest"),
            "down": Exit(destination="mine-main-shaft"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="mine-main-shaft",
        desc="Mine — Main Shaft",
        ldesc=(
            "The main shaft drops away from the entrance in a single rough-cut passage, wide "
            "enough for two men and a cart. Timber supports run at intervals — functional, "
            "not decorative. The smell of rock dust and old torchsmoke is thick here."
        ),
        exits={
            "up":    Exit(destination="mine-entrance"),
            "east":  Exit(destination="mine-assay-room"),
            "down":  Exit(destination="mine-tunnels"),
        },
        flags={ONBIT},  # active mine with torches on walls
        value=1,
    ))

    world.register_room(Room(
        name="mine-assay-room",
        desc="Assay Room",
        ldesc=(
            "A side room off the main shaft, fitted out for testing ore samples. A long workbench "
            "runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, "
            "crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie "
            "Rats were mining, someone was genuinely checking its quality. The far wall has a gap "
            "in it that doesn't look entirely accidental."
        ),
        exits={
            "west":  Exit(destination="mine-main-shaft"),
            "east":  Exit(destination="mine-hidden-secondary",
                          condition=lambda w: bool(w.globals.get("mine_gap_found")),
                          fail_message="The gap in the wall is there, but you haven't found the right angle."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="mine-hidden-secondary",
        desc="Hidden Secondary Entrance",
        ldesc=(
            "The gap in the assay room wall opens into a rough passage that connects to the "
            "tunnel network below. It does not appear on any official plan of the mine. "
            "It would not."
        ),
        exits={
            "west":  Exit(destination="mine-assay-room"),
            "east":  Exit(destination="secret-tunnels-forgotten-shaft"),
        },
        flags={ONBIT},
        value=2,
    ))

    world.register_room(Room(
        name="mine-tunnels",
        desc="Mine Tunnels",
        ldesc=(
            "The working tunnels branch off the main shaft in two directions, following veins "
            "of ore that may or may not have been the point. Torch sconces are fixed to the "
            "walls at intervals — the torches in them are real and lit. The smell of fresh-cut "
            "rock is strongest here. The floor is rutted with cart tracks."
        ),
        exits={
            "up":    Exit(destination="mine-main-shaft"),
            "east":  Exit(destination="mine-rats-nest"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="mine-rats-nest",
        desc="The Rat's Nest",
        ldesc=(
            "A widening in the tunnel that someone has decided is a room. Crates and barrels "
            "are stacked with more care than the surroundings suggest — this is storage, not "
            "clutter. The Pie Rats keep their surplus here: things that aren't ore, things that "
            "don't show up on manifests, things that would raise questions on a dock."
        ),
        exits={"west": Exit(destination="mine-tunnels")},
        flags={ONBIT},
        value=1,
    ))


# ---------------------------------------------------------------------------
# Roundabout Beach & Sea
# ---------------------------------------------------------------------------

def _make_beach_sea(world: "World") -> None:
    world.register_room(Room(
        name="roundabout-beach",
        desc="Roundabout Beach",
        ldesc=(
            "Roundabout Beach opens up as the town falls behind you — a generous sweep of sand, "
            "the water catching whatever light the sky offers. The docks stretch east to where "
            "the Pie Rat Ship is moored, close enough to read the name on its hull. The lighthouse "
            "stands to the north on a finger of rock, its lamp turning slowly. It smells like "
            "freedom, or at least like salt."
        ),
        exits={
            "north": Exit(destination="lighthouse"),
            "east":  Exit(destination="the-docks"),
            "west":  Exit(destination="beach-road"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="lighthouse",
        desc="The Lighthouse",
        ldesc=(
            "Open and unattended. A desk holds a scroll — left by Silas Bryne, "
            "who is not here. The lamp turns above."
        ),
        exits={"south": Exit(destination="roundabout-beach")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="the-docks",
        desc="The Docks",
        ldesc=(
            "The boards flex slightly underfoot, worn smooth by years of boots and cargo. "
            "Bollards thick with rope line the edge. A coil of rope sits loose on the nearest "
            "bollard. The Pie Rat Ship sits in her berth like she owns it, which she more or "
            "less does — the only vessel worth the name in Roundabout's harbor. "
            "The smell is fish and brine and honest work."
        ),
        exits={
            "west":  Exit(destination="roundabout-beach"),
            "north": Exit(destination="lighthouse"),
            "in":    Exit(destination="pie-rat-ship-deck",
                          condition=lambda w: bool(w.globals.get("has_disguise") or w.globals.get("ship_stolen")),
                          fail_message="A Pie Rat on deck looks you over with the thoroughness of someone whose job is exactly this. \"You don't even look like a pirate.\" He doesn't move. Neither, apparently, will you."),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="pie-rat-ship-deck",
        desc="Pie Rat Ship — Deck",
        ldesc=(
            "The deck is cluttered in the way of a working vessel — coils of line, barrels "
            "lashed to the rail, a general smell of fish and salt and something that has been "
            "at sea too long. This is a ship that wants to move."
        ),
        exits={
            "out":  Exit(destination="the-docks"),
            "down": Exit(destination="pie-rat-ship-hold"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="pie-rat-ship-hold",
        desc="Pie Rat Ship — Hold",
        ldesc=(
            "Below decks. Crates and casks everywhere. The smell of tar and old timber. "
            "A narrow bunk is wedged into one corner. There's more here than just cargo — "
            "but finding it requires looking."
        ),
        exits={"up": Exit(destination="pie-rat-ship-deck")},
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="western-roundabout-sea",
        desc="Western Roundabout Sea",
        ldesc=(
            "The smell of the town still reaches you here — smoke and bread underneath the salt. "
            "The beach stretches behind you, the lighthouse standing watch to the north. The "
            "water is choppier than it looked from shore. Ahead, the coast begins to fall away."
        ),
        exits={
            "west": Exit(destination="the-docks"),
            "east": Exit(destination="roundabout-sea-middle"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="roundabout-sea-middle",
        desc="Roundabout Sea",
        ldesc=(
            "The coast is gone. There is nothing in any direction but open water and sky. "
            "The sea moves in long slow swells that lift and drop the hull with a steady "
            "indifference. You are very small out here."
        ),
        exits={
            "west": Exit(destination="western-roundabout-sea"),
            "east": Exit(destination="eastern-roundabout-sea"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="eastern-roundabout-sea",
        desc="Eastern Roundabout Sea",
        ldesc=(
            "Is that — yes. An island. Small, tree-lined, a beach curving around the side "
            "facing you. The water around it is shallow and clear. Nothing out here suggested "
            "this was coming. It sits quietly off the bow, waiting to be noticed. East of it, "
            "the sea continues without comment."
        ),
        exits={
            "west":  Exit(destination="roundabout-sea-middle"),
            "east":  Exit(destination="open-ocean-1"),
            "south": Exit(destination="desert-island"),
            "land":  Exit(destination="desert-island"),
        },
        flags={ONBIT},
        value=1,
    ))

    world.register_room(Room(
        name="desert-island",
        desc="Desert Island",
        ldesc=(
            "The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.\n"
            "Nothing here is threatening and nothing here is welcoming. The island feels like "
            "a place that has been waiting — not for you specifically, but for someone.\n"
            "The quiet here is a different kind of quiet than the open ocean — heavier, more "
            "deliberate.\n"
            "You have the distinct feeling that something happened here once. The island isn't telling."
        ),
        exits={"north": Exit(destination="eastern-roundabout-sea")},
        flags={ONBIT},
        value=1,
    ))

    # Open ocean — 69 squares; we register one stub and handle navigation programmatically
    # For Phase 2, register the first and last squares plus Kevry's island
    world.register_room(Room(
        name="open-ocean-1",
        desc="Open Ocean",
        ldesc="Open ocean in every direction. Nothing else.",
        exits={
            "west": Exit(destination="eastern-roundabout-sea"),
            "east": Exit(destination="open-ocean-2"),
        },
        flags={ONBIT},
        value=0,
    ))

    # Intermediate ocean squares generated programmatically
    for i in range(2, 69):
        world.register_room(Room(
            name=f"open-ocean-{i}",
            desc="Open Ocean",
            ldesc="The ocean does not vary its presentation.",
            exits={
                "west": Exit(destination=f"open-ocean-{i-1}"),
                "east": Exit(destination=f"open-ocean-{i+1}"),
            },
            flags={ONBIT},
            value=0,
        ))

    world.register_room(Room(
        name="open-ocean-69",
        desc="Open Ocean",
        ldesc="Sea. Sky. Nothing else to report.",
        exits={
            "west": Exit(destination="open-ocean-68"),
            "east": Exit(destination="kevry-land-ho"),
            "land": Exit(destination="kevry-land-ho"),
        },
        flags={ONBIT},
        value=0,
    ))

    # Kevry's Island
    world.register_room(Room(
        name="kevry-land-ho",
        desc="Land, Ho!",
        ldesc=(
            "The island resolves out of the horizon slowly, then all at once. Sand, trees, solid "
            "ground. You've earned this. The beach curves invitingly ahead."
        ),
        exits={
            "out":  Exit(destination="open-ocean-69"),
            "east": Exit(destination="kevry-empty-beach"),
        },
        flags={ONBIT},
        value=5,
    ))

    world.register_room(Room(
        name="kevry-empty-beach",
        desc="Empty Beach",
        ldesc=(
            "The beach is long and quiet, the sand unmarked. A line of scrubby trees runs along "
            "the inland edge. Somewhere beyond them, half-hidden, a small structure. The only "
            "sounds are the water behind you and the wind doing very little. It feels like a "
            "place that has been left alone for a long time and is content with that."
        ),
        exits={
            "west": Exit(destination="kevry-land-ho"),
            "east": Exit(destination="kevry-house"),
        },
        flags={ONBIT},
        value=5,
    ))

    world.register_room(Room(
        name="kevry-house",
        desc="A House",
        ldesc=(
            "The interior is cluttered in the way that only makes sense to its owner. Charts "
            "pinned to every surface, ropes coiled with obsessive care, a hammock in the corner. "
            "A lantern hangs from a beam. Someone has been here a long time and made their "
            "peace with it."
        ),
        exits={
            "west":  Exit(destination="kevry-empty-beach"),
            "north": Exit(destination="kevry-captains-quarters"),
        },
        flags={ONBIT},
        value=5,
    ))

    world.register_room(Room(
        name="kevry-captains-quarters",
        desc="Captain's Quarters",
        ldesc=(
            "A small back room, all table and charts and the smell of ink. A weathered man "
            "sits hunched over a map, muttering. He doesn't hear you come in. When he finally "
            "looks up, his face does something complicated — surprise, then recognition of the "
            "type that doesn't require prior acquaintance, then a wide and genuine grin."
        ),
        exits={"south": Exit(destination="kevry-house")},
        flags={ONBIT},
        value=5,
    ))


# ---------------------------------------------------------------------------
# Secret Tunnels
# ---------------------------------------------------------------------------

def _make_secret_tunnels(world: "World") -> None:
    world.register_room(Room(
        name="secret-tunnels-junction",
        desc="The Junction",
        ldesc=(
            "The tunnel opens up here — not much, but enough to feel like a decision point. "
            "Rough stone walls, a ceiling low enough to notice. Passages branch in three "
            "directions. The one behind you leads back up to the cellar. The air is damp and "
            "smells of old earth and something faintly mineral. Down here, sound doesn't carry "
            "the way it should."
        ),
        exits={
            "north": Exit(destination="cellar-storeroom"),
            "east":  Exit(destination="secret-tunnels-undercroft"),
            "west":  Exit(destination="bone-passage"),
            "south": Exit(destination="toll-bridge"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="secret-tunnels-undercroft",
        desc="The Undercroft",
        ldesc=(
            "A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry "
            "by people who knew where they were going. The walls are close enough that two "
            "people could pass but would have to mean it. The floor is uneven underfoot. "
            "The air is heavier here, deeper-smelling."
        ),
        exits={
            "west":  Exit(destination="secret-tunnels-junction"),
            "east":  Exit(destination="secret-tunnels-forgotten-shaft"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="secret-tunnels-forgotten-shaft",
        desc="The Forgotten Shaft",
        ldesc=(
            "The passage narrows as it goes — not dangerously, but noticeably. The stonework "
            "changes here, older and less deliberate, as if this part of the tunnel predates "
            "whoever dug the rest. The far wall has a gap in it that doesn't look entirely accidental."
        ),
        exits={
            "west":  Exit(destination="secret-tunnels-undercroft"),
            "east":  Exit(destination="mine-hidden-secondary"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="bone-passage",
        desc="The Bone Passage",
        ldesc=(
            "The stonework here is older than the rest of the tunnels — rougher cut, the joints "
            "wider, the walls slightly damp to the touch. The passage runs west. Whatever built "
            "this part didn't build it at the same time as the rest. The name feels earned."
        ),
        exits={
            "east": Exit(destination="secret-tunnels-junction"),
            "west": Exit(destination="charnel-walk"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="charnel-walk",
        desc="The Charnel Walk",
        ldesc=(
            "The passage ends at a low arch ahead — beyond it, the crypt. The air is colder "
            "here, noticeably so, as if the temperature has been coming down gradually and "
            "this is where it arrives. The walls are older stone, darker with moisture. "
            "The silence has a different quality than the tunnels behind you."
        ),
        exits={
            "east":  Exit(destination="bone-passage"),
            "north": Exit(destination="the-crypt"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="toll-bridge",
        desc="The Toll Bridge",
        ldesc=(
            "A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep "
            "enough that the bottom isn't visible. The bridge looks solid.\n"
            "A small, dense figure has planted itself at the center of it with the unmistakable "
            "air of someone who intends to stay.\n"
            "He eyes you with the satisfaction of a man whose position has never once been "
            "successfully argued with."
        ),
        exits={
            "north": Exit(destination="secret-tunnels-junction"),
            "south": Exit(destination="dungeon-entrance",
                          condition=lambda w: bool(w.globals.get("boggart_gone")),
                          fail_message="The Boggart plants himself firmly in your path. \"Toll,\" he says. He does not move."),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="dungeon-entrance",
        desc="Dungeon Entrance",
        ldesc=(
            "The tunnel ends at a threshold — stone floor, stone walls, a passage leading south "
            "into darkness. Whatever is ahead doesn't announce itself. The air is different here: "
            "stiller, older, with a quality that suggests the dark ahead has been dark for a very "
            "long time. This is the end of the tunnels. The dungeon begins."
        ),
        exits={
            "north": Exit(destination="toll-bridge"),
            "south": Exit(destination="ink-corridor"),
        },
        flags=set(),  # dark
        value=1,
    ))


# ---------------------------------------------------------------------------
# Dungeon — Upper Tier
# ---------------------------------------------------------------------------

def _make_dungeon_upper(world: "World") -> None:
    world.register_room(Room(
        name="ink-corridor",
        desc="Ink Corridor",
        ldesc=(
            "The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. "
            "It feels like an entrance to something, which it is. The passage splits ahead, "
            "west and east."
        ),
        exits={
            "north": Exit(destination="dungeon-entrance"),
            "west":  Exit(destination="supply-room"),
            "east":  Exit(destination="storage-area"),
        },
        flags=set(),  # dark
        value=1,
    ))

    world.register_room(Room(
        name="supply-room",
        desc="Supply Room",
        ldesc=(
            "A storage room, wide and low. Shelves run along three walls — some collapsed, "
            "most still holding whatever was left here when this place was abandoned. The "
            "contents are various: tools, containers, materials that suggest someone was "
            "keeping this dungeon supplied. It smells of old wood and something chemical underneath."
        ),
        exits={
            "east":  Exit(destination="ink-corridor"),
            "south": Exit(destination="narrow-passageway"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="narrow-passageway",
        desc="Narrow Passageway",
        ldesc=(
            "A short passage, plain stone, lower-ceilinged than the corridor behind you. It "
            "goes south and ends at a doorway. The kind of passage that exists to connect two "
            "places and has no opinion about either of them."
        ),
        exits={
            "north": Exit(destination="supply-room"),
            "south": Exit(destination="idol-room"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="idol-room",
        desc="Idol Room",
        ldesc=(
            "The room is small and oddly formal — the stonework here is more deliberate than "
            "the corridors outside, the walls smoothed, the floor level. At the center, a "
            "stone pedestal holds a figurine. The room has the feeling of something that has "
            "been waiting for someone to make a mistake."
        ),
        exits={
            "north": Exit(destination="narrow-passageway"),
            "south": Exit(destination="combat-room"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="storage-area",
        desc="Storage Area",
        ldesc=(
            "A wide chamber, larger than expected — the dungeon opens up here before closing "
            "back down. The walls are rough, the floor uneven. Equipment has been left here: "
            "a hand cart against one wall, a heavy support beam laid across the floor. "
            "The east wall is solid. The south passage is blocked."
        ),
        exits={
            "west":  Exit(destination="ink-corridor"),
            "south": Exit(destination="collapsed-gallery"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="collapsed-gallery",
        desc="Collapsed Gallery",
        ldesc=(
            "The passage runs south but doesn't get far. Heavy timbers have come down across "
            "it — not from collapse exactly, more like someone wedged them there deliberately. "
            "The wood is old but solid. Beyond them, darkness."
        ),
        exits={
            "north": Exit(destination="storage-area"),
            "south": Exit(destination="rickety-bridge",
                          condition=lambda w: bool(w.globals.get("gallery_cleared")),
                          fail_message="The timbers block the way south. They need to be cleared."),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="creature-den",
        desc="Creature Den",
        ldesc=(
            "A rough side chamber — the lair of something large and recently departed. "
            "The floor is marked with deep scores. Whatever lived here is gone."
        ),
        exits={
            "west": Exit(destination="combat-room"),
            "east": Exit(destination="flooding-room"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="combat-room",
        desc="Combat Room",
        ldesc=(
            "A wide chamber, stone-walled and plain. A pressure plate is set into the corridor "
            "south of the entrance — easy to miss in the dark. Whatever it does, it does it loudly."
        ),
        exits={
            "north": Exit(destination="idol-room"),
            "south": Exit(destination="prayer-alcove"),
            "east":  Exit(destination="creature-den"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="flooding-room",
        desc="Flooding Room",
        ldesc=(
            "A low-lying cave, the floor wet from seepage. Three levers are mounted on the "
            "east wall. The room is damp and close."
        ),
        exits={"west": Exit(destination="creature-den")},
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="prayer-alcove",
        desc="Prayer Alcove",
        ldesc=(
            "A low stone alcove — looks like a dead end until you examine it. A carved niche "
            "in the back wall goes back further than expected."
        ),
        exits={
            "north": Exit(destination="combat-room"),
            "south": Exit(destination="portcullis-corridor"),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="portcullis-corridor",
        desc="Portcullis Corridor",
        ldesc=(
            "A metal portcullis blocks the corridor ahead, carrying an arcane charge. "
            "Touching it without disarming would be unpleasant."
        ),
        exits={
            "north": Exit(destination="prayer-alcove"),
            "south": Exit(destination="shrine-room",
                          condition=lambda w: bool(w.globals.get("portcullis_open")),
                          fail_message="The portcullis blocks the way. It needs to be disarmed or propped open."),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="shrine-room",
        desc="Shrine Room",
        ldesc=(
            "The room is older than the dungeon around it — the stonework finer, the walls "
            "carved rather than cut. Someone built this with intention. A shallow bowl "
            "depression is set into a stone plinth at the center. The air is stiller here "
            "than in the corridors outside, as if the room has been holding its breath "
            "for a long time."
        ),
        exits={
            "north": Exit(destination="portcullis-corridor"),
            "south": Exit(destination="rickety-bridge"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="rickety-bridge",
        desc="Rickety Bridge",
        ldesc=(
            "A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the "
            "stones have shifted slightly in their mortar, the edges worn. It looks crossable. "
            "It probably is. The far side leads south to a heavy iron door."
        ),
        exits={
            "north": Exit(destination="shrine-room"),
            "west":  Exit(destination="collapsed-gallery"),
            "south": Exit(destination="mid-tier-key-door"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="mid-tier-key-door",
        desc="Mid-Tier Key Door",
        ldesc=(
            "The door is iron, set deep into the stone. The lock is substantial — no amount "
            "of forcing will open this. It wants a key."
        ),
        exits={
            "north": Exit(destination="rickety-bridge"),
            "south": Exit(destination="key-door-landing",
                          condition=lambda w: bool(w.globals.get("mid_tier_key_used")),
                          fail_message="The door is locked. It wants a key."),
        },
        flags=set(),
        value=1,
    ))


# ---------------------------------------------------------------------------
# Dungeon — Middle Tier, Key Side
# ---------------------------------------------------------------------------

def _make_dungeon_mid_key(world: "World") -> None:
    world.register_room(Room(
        name="key-door-landing",
        desc="Key Door Landing",
        ldesc=(
            "The staircase deposits you in a rough cave at the bottom — low ceiling, unworked "
            "stone, the kind of room that exists because something had to be at the bottom "
            "of the stairs. The air is cooler here, damper. The passage continues south."
        ),
        exits={
            "north": Exit(destination="mid-tier-key-door"),
            "south": Exit(destination="mine-passage"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="mine-passage",
        desc="Mine Passage",
        ldesc=(
            "A worked section of cave — support timbers at intervals, rusting tools left where "
            "they were dropped. The smell of old rock dust is thick here. Someone mined this "
            "passage, or used it as a route through to something being mined. "
            "A large iron chest is bolted to the floor against one wall."
        ),
        exits={
            "north": Exit(destination="key-door-landing"),
            "south": Exit(destination="stored-room"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="stored-room",
        desc="Stored Room",
        ldesc=(
            "The floor is packed tight with rubble — not the chaotic scatter of a cave-in, "
            "but deliberate, careful fill. Someone put this here on purpose."
        ),
        exits={
            "north": Exit(destination="mine-passage"),
            "east":  Exit(destination="the-crevice",
                          condition=lambda w: not bool(w.globals.get("stored_room_collapsed")),
                          fail_message="The spur east is buried under rubble."),
            "south": Exit(destination="inscription-chamber"),
            "down":  Exit(destination="hole-to-below",
                          condition=lambda w: bool(w.globals.get("stored_room_collapsed")),
                          fail_message="There's no hole here yet."),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="the-crevice",
        desc="The Crevice",
        ldesc=(
            "A narrow crack in the rock face. A skeleton is wedged in it — tried to squeeze "
            "through and failed. A gold pocket watch hangs from one outstretched finger."
        ),
        exits={"west": Exit(destination="stored-room")},
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="inscription-chamber",
        desc="Inscription Chamber",
        ldesc=(
            "A cave room, wider than the passage leading to it. One wall has been worked — "
            "smoothed and carved with an inscription, old enough that the edges have softened. "
            "The other walls are natural stone, unmodified."
        ),
        exits={
            "north": Exit(destination="stored-room"),
            "east":  Exit(destination="cave-creature-lair",
                          condition=lambda w: bool(w.globals.get("crawlspace_found")),
                          fail_message="The east wall is solid."),
            "south": Exit(destination="echo-alcove"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="cave-creature-lair",
        desc="Cave Creature's Lair",
        ldesc=(
            "A low cave, the ceiling close. Whatever lived here is absent. The floor is "
            "littered with bones — animal, mostly — and discarded objects. A bone flute "
            "lies on the floor."
        ),
        exits={"west": Exit(destination="inscription-chamber")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="echo-alcove",
        desc="Echo Alcove",
        ldesc=(
            "A faint grinding drifts up from somewhere far below — bone on stone."
        ),
        exits={"north": Exit(destination="inscription-chamber"),
               "south": Exit(destination="magnetic-vault")},
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="magnetic-vault",
        desc="Magnetic Vault",
        ldesc=(
            "A square room, stone walls, a single chest at the center on a low stone platform. "
            "The room feels subtly wrong in a way that takes a moment to identify — small metal "
            "objects have drifted toward the chest, as if drawn. A nail in the wall points toward "
            "it. Dust has settled in a faint ring around the latch."
        ),
        exits={
            "north": Exit(destination="echo-alcove"),
            "south": Exit(destination="deep-lock-door"),
        },
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="deep-lock-door",
        desc="Deep Lock Door",
        ldesc=(
            "The passage ends at a door set deep into the stone. It is sealed absolutely — "
            "no lock visible, no handle, no gap at the frame. Whatever mechanism holds it "
            "closed is on the other side, or nowhere. This door does not open. The passage "
            "ends here."
        ),
        exits={"north": Exit(destination="magnetic-vault")},
        flags=set(),
        value=1,
    ))

    world.register_room(Room(
        name="hole-to-below",
        desc="Hole to Below",
        ldesc=(
            "The ceiling is a jagged wound — stone and packed earth hanging at the edge where "
            "the floor above used to be. Below that: the rubble that was the floor, now a "
            "rough-graded pile. A rope hangs from a beam above."
        ),
        exits={
            "up":   Exit(destination="stored-room",
                         condition=lambda w: bool(w.globals.get("rope_tied")),
                         fail_message="The beam is above you, but there's nothing to climb."),
            "down": Exit(destination="pile-of-rubble"),
        },
        flags=set(),
        value=1,
    ))


# ---------------------------------------------------------------------------
# Dungeon — Middle Tier, Trap Side
# ---------------------------------------------------------------------------

def _make_dungeon_mid_trap(world: "World") -> None:
    world.register_room(Room(
        name="the-spillway",
        desc="The Spillway",
        ldesc=(
            "The sluice deposits you here — wet stone, low ceiling, the sound of water draining "
            "somewhere below. The chamber is small and close. There's no way back up. "
            "The passage continues south."
        ),
        exits={"south": Exit(destination="dream-corridor")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="dream-corridor",
        desc="Dream Corridor",
        ldesc=(
            "The corridor is low and wet. Water drips somewhere behind you. Your torch throws "
            "just enough light to see the floor — and the footprints already pressed into the "
            "mud. Leading in from the entrance. Your size. Your stride. "
            "You haven't been here before."
        ),
        exits={
            "north": Exit(destination="the-spillway"),
            "south": Exit(destination="lost-apprentice-cell",
                          condition=lambda w: bool(w.globals.get("dream_corridor_passed")),
                          fail_message="The corridor leads you back to where you started. The footprints are there. Your size. Your stride."),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="lost-apprentice-cell",
        desc="Lost Apprentice's Cell",
        ldesc=(
            "A rough cell, its walls scarred with use. The apprentice is here — afflicted, "
            "changed, dangerous. The shovel against the wall suggests someone was trying "
            "to dig their way out."
        ),
        exits={
            "north": Exit(destination="dream-corridor"),
            "out":   Exit(destination="bog-nw",
                          condition=lambda w: bool(w.globals.get("apprentice_rescued")),
                          fail_message="The passage isn't finished yet."),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="supply-cache",
        desc="Supply Cache",
        ldesc=(
            "A partially collapsed side room. Rubble everywhere. Something glints in the pile."
        ),
        exits={"north": Exit(destination="lost-apprentice-cell")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="flood-sump",
        desc="Flood Sump",
        ldesc=(
            "The passage ends here in a low chamber, the floor wet — a shallow pool covers "
            "most of it, fed by seepage through the walls. The water is still and dark. "
            "The ceiling is close. This is the lowest point down here, and it feels like it."
        ),
        exits={"north": Exit(destination="supply-cache")},
        flags=set(),
        value=2,
    ))


# ---------------------------------------------------------------------------
# Dungeon — Lower Tier
# ---------------------------------------------------------------------------

def _make_dungeon_lower(world: "World") -> None:
    world.register_room(Room(
        name="pile-of-rubble",
        desc="Pile of Rubble",
        ldesc=(
            "The ceiling is a jagged wound — stone and packed earth hanging at the edge where "
            "the floor above used to be. Below that: the rubble that was the floor, now a "
            "rough-graded pile you're standing on. The air smells of disturbed earth and "
            "something older underneath it. Passages lead further in."
        ),
        exits={
            "up":    Exit(destination="hole-to-below",
                          condition=lambda w: bool(w.globals.get("rope_tied")),
                          fail_message="There's no way back up without a rope."),
            "east":  Exit(destination="antechamber"),
            "south": Exit(destination="lower-dungeon-encampment"),
            "north": Exit(destination="lower-crypt"),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="lower-dungeon-encampment",
        desc="The Encampment",
        ldesc=(
            "The camp is old but not abandoned — abandoned implies a choice. Bedrolls still "
            "laid out. Equipment set down mid-use. Journals open to pages no one finished. "
            "Whatever happened here, no one saw it coming."
        ),
        exits={"north": Exit(destination="pile-of-rubble")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="thermal-vent-room",
        desc="Thermal Vent Room",
        ldesc=(
            "Warm air rises from fissures in the floor. The ceiling above is obscured by "
            "the heat shimmer. Something is pressed into the rock overhang above — "
            "visible only if you look up."
        ),
        exits={"south": Exit(destination="lower-crypt")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="antechamber",
        desc="Antechamber",
        ldesc=(
            "The sound is coming from beyond that doorway — bone grinding on stone, steady "
            "and unhurried. You get the distinct impression that silence is not optional here."
        ),
        exits={
            "west":  Exit(destination="pile-of-rubble"),
            "east":  Exit(destination="the-junction-lower"),
            "south": Exit(destination="skeleton-room"),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="skeleton-room",
        desc="Skeleton Room",
        ldesc="You should not be here. This is immediately, unambiguously clear.",
        exits={"north": Exit(destination="antechamber")},
        flags=set(),
        value=0,  # instant death on entry
    ))

    world.register_room(Room(
        name="the-junction-lower",
        desc="The Junction",
        ldesc=(
            "The passage widens here into a rough junction, the stone walls bearing the marks "
            "of tools long since abandoned. Three directions offer themselves without comment. "
            "The floor is grit and old dust."
        ),
        exits={
            "west":  Exit(destination="antechamber"),
            "east":  Exit(destination="the-narrow-pass"),
            "south": Exit(destination="dark-room"),
            "north": Exit(destination="tool-alcove"),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="the-narrow-pass",
        desc="The Narrow Pass",
        ldesc=(
            "A long passage, barely wide enough for your shoulders. The walls are close and "
            "the ceiling drops as you move east. Somewhere ahead, something breathes — slow "
            "and irregular, like sleep that isn't quite sleep."
        ),
        exits={
            "west": Exit(destination="the-junction-lower"),
            "east": Exit(destination="the-still-den"),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="the-still-den",
        desc="The Still Den",
        ldesc=(
            "A wide cave, low but not cramped. The walls are gouged at every height — long "
            "parallel marks, overlapping, years of them. The floor is worn smooth in a rough "
            "oval, the path of something that has been pacing this space for longer than it "
            "can remember. It is very still right now. That changes the moment you enter."
        ),
        exits={"west": Exit(destination="the-narrow-pass")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="tool-alcove",
        desc="Tool Alcove",
        ldesc=(
            "The passage ends at a shallow recess lined with iron brackets — the kind used "
            "to hang tools or equipment. The brackets are empty. The back wall is flat and featureless."
        ),
        exits={
            "south": Exit(destination="the-junction-lower"),
            "north": Exit(destination="quest-34-mid-room",
                          condition=lambda w: bool(w.globals.get("tool_alcove_door_open")),
                          fail_message="The back wall is flat and featureless."),
        },
        flags=set(),
        value=3,
    ))

    world.register_room(Room(
        name="quest-34-mid-room",
        desc="Mid Room",
        ldesc=(
            "Everything in this room is becoming the pool. Water seeps through the walls in "
            "thin lines, runs down the stone, disappears into the dark surface below. "
            "The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless "
            "as far as you can tell. The passage north is visible on the other side. "
            "The water is between you and it."
        ),
        exits={
            "south": Exit(destination="tool-alcove"),
            "north": Exit(destination="quest-34-fountain-room",
                          condition=lambda w: bool(w.globals.get("mid_room_frozen")),
                          fail_message="The pool fills the room wall to wall. You cannot cross."),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="quest-34-fountain-room",
        desc="Fountain Room",
        ldesc=(
            "Cold stops you at the threshold — not wind, just cold, settled and absolute. "
            "The fountain to your left has been frozen mid-pour for what might be a very long "
            "time. The block of ice in the center of the room is frosted thick, but not so "
            "thick you can't see the shape inside it. A person. Standing. Composed."
        ),
        exits={"south": Exit(destination="quest-34-mid-room")},
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="dark-room",
        desc="The Dark Room",
        ldesc=(
            "You cannot see anything. This is not like being in the dark. "
            "This is something the dark is doing on purpose."
        ),
        exits={
            "north": Exit(destination="the-junction-lower"),
            "south": Exit(destination="spirit-room",
                          condition=lambda w: bool(w.globals.get("dark_room_lit")),
                          fail_message="The magical darkness blocks all passage."),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="spirit-room",
        desc="Spirit Room",
        ldesc=(
            "The room is silent. Shapes drift through it — sparse, irregular, neither here "
            "nor entirely anywhere. They are not human. They are not entirely not human. "
            "They take note of you the moment you enter. The passage north is visible. "
            "Getting there is another matter."
        ),
        exits={
            "north": Exit(destination="dark-room"),
            "south": Exit(destination="burial-chamber",
                          condition=lambda w: bool(w.globals.get("ring_worn")),
                          fail_message="The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making."),
        },
        flags=set(),
        value=2,
    ))

    world.register_room(Room(
        name="burial-chamber",
        desc="Burial Chamber",
        ldesc=(
            "The chamber is circular, the walls carved with processions of figures — mourners, "
            "by the look of them, rendered in a style no living hand in Roundabout would "
            "recognize. Niches hold candles that have not burned in centuries, wax melted flat "
            "and cold. The plinth at the center holds the mask. Everything in this room was "
            "arranged deliberately, long ago, by people who are not coming back."
        ),
        exits={"north": Exit(destination="spirit-room")},
        flags=set(),
        value=3,
    ))
