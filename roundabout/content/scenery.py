"""
Scenery the room text names (TODO #15, 2026-10-14; text in locations.md under
each room, windows in mechanics.md — Windows).
- Surface: Will's desk and papers, the library's catalogue, shelves and ledger,
  the fountain, the Altar's dial, the Upstairs Hall's doors and floorboards, and
  a WINDOW scenery object in every room that has one.
- Underground: the rubble, the Encampment's journals, bedrolls and equipment, the
  Rat's Nest crates, the Chuckle House Entrance's stool, runner and ceiling, and
  the Ghost's Room mirrors (by the ghost's own visibility rule, chuckle._visible).
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World

# --- Will's Wizard Tower -------------------------------------------------------------
TOWER_DESK = (
    "A broad old desk, scarred by years of elbows and spilled ink. Every inch of it is "
    "papers, except the corner where Will rests his pen."
)
TOWER_PAPERS_WILL = (
    'Will slides a sheet over the top of the pile without looking up. "Correspondence," '
    'he says. "Mostly unanswered."'
)
TOWER_PAPERS_ALONE = (
    "Notes in Will's small, fast hand, on subjects you'd need a year to follow. You put "
    "them back where they were."
)

# --- Library — Main Hall -------------------------------------------------------------
CATALOGUE = (
    "Hundreds of small drawers, each labelled in faded ink. The drawer marked V sits a "
    "little open, as if someone has been in it more than most."
)
CATALOGUE_CARD = (
    "Under 'Veil of the Arcane' there's a single card. The borrower's line has been "
    "filled in by the same hand, over and over, down the whole card — and then nothing."
)
SHELVES = (
    "Floor to ceiling, packed in columns. The gaps between them are narrow, and one at "
    "the east end runs back further than it should."
)
LEDGER = (
    'She keeps a hand on it. "The application," she says, in someone else\'s voice. '
    '"There\'s a date. There\'s no return date."'
)

# --- Town Square ---------------------------------------------------------------------
FOUNTAIN_DRY = (
    "Dry for years. The basin is cracked at one edge, and the spout is furred with old "
    "lime. Whatever fed it came from somewhere underground."
)
FOUNTAIN_RUNNING = (
    "Water runs from the spout into the basin, clear and cold. The crack at the edge "
    "weeps a little, but it holds."
)

# --- The Altar -----------------------------------------------------------------------
ALTAR_EXAMINE = (
    "The altar is plain stone, unadorned. The dial dominates it — brass, worn at the "
    "edges from use, seven symbols arranged around its face."
)
DIAL = (
    "Seven symbols ring its brass face, left to right: a sprouting seed inside a circle "
    "of leaves; a seven-pointed star with a void at its center; a white sword on a black "
    "field; three threads braided into one; a coin with a question mark; a lit lantern "
    "with an open door; a fire inside a house."
)
DIAL_GLOW = "The glow sits on the {symbol} — {religion}."
SYMBOLS = ["seed", "star", "sword", "threads", "coin", "lantern", "fire"]   # dial order

# --- Upstairs Hall -------------------------------------------------------------------
HALL_DOORS = "Three plain doors, each with a brass number gone brown with handling."
FLOORBOARDS = (
    "They creak whatever you do. Regular guests have learned where not to step; you "
    "haven't."
)

# --- Windows -------------------------------------------------------------------------
WINDOW_SHUT = "The window doesn't open, and you're not about to start breaking things."
ALLEY_MUGGER = (
    "Below, the alley runs narrow and dim between the backs of buildings. In one doorway "
    "something that might be a man stands very still, watching the street end."
)
ALLEY_QUIET = (
    "Below, the alley runs narrow and dim between the backs of buildings. Nothing moves "
    "in it now, and it looks the better for it."
)
VIEWS = {
    "GUEST-ROOM-1": ("The street below, carts and people going about the day. From up here "
                     "the town looks like it knows what it's doing."),
    "GUEST-ROOM-2": ("One window gives on the street, the other on the square. Between them "
                     "you can see most of Roundabout going about its business."),
    "CHURCH-NAVE": ("The windows are narrow, more slit than glass. Thin bars of light, and "
                    "beyond them only sky."),
    "RECORDS-ROOM": ("The window looks onto the square. The clerk's desk is placed so that "
                     "he can't see out of it, which may be deliberate."),
    "TOWN-HALL-TOWER": ("A slice of the square below — the fountain, the tops of heads, a "
                        "cart turning. More suggestion than panorama."),
    "LIGHTHOUSE": ("Grey water, the beach curving away to the southwest. Far to the east, "
                   "on the horizon, a smudge that might be cloud and might not."),
}
WINDOW_ROOMS = ["UPSTAIRS-HALL", *VIEWS]


# --- Underground (locations.md under each room) ---------------------------------------
RUBBLE = (
    "Broken flagstones, packed earth and splintered timber, settled into a rough slope. "
    "It was the floor upstairs, until you came along."
)
RUBBLE_SEARCH = "You turn over a few stones. Nothing under them but more stones."
RUBBLE_CLIMB = "You're standing on it already. The way up is the rope."
JOURNALS = (
    "Two hands share the pages. One is cramped and hurried, full of a seven-pointed "
    "star; it stops mid-sentence. The other is careful, and goes on a few pages more: "
    "'He is not himself. I will go for silver.'"
)
JOURNALS_STAY = "You leave them where they are. Someone meant to come back to them."
BEDROLLS = "Two bedrolls, side by side, long since gone flat. Nobody has slept in them for years."
EQUIPMENT = (
    "Lamps with no oil, a surveyor's chain, a hammer and chisel set down beside a "
    "half-cut sample. Everything here was put down to be picked up again."
)
CRATES = (
    "Stencilled PIE RATS MINING INC. — ORE, though nothing in them rattles like ore. "
    "Most are nailed shut."
)
CRATES_SEARCH = (
    "The lids are nailed down tight, and the ones that aren't hold sacking, rope and "
    "salted fish. Whatever's worth stealing here, it isn't in the crates."
)
STOOL = (
    "A tall wooden stool, worn pale where someone sat for years selling tickets. It's "
    "still pushed in at exactly the angle they left it."
)
RUNNER = (
    "Faded to the colour of dust. Up close the pattern is faces after all — small, "
    "grinning, repeated down the length of the hall."
)
ENTRANCE_CEILING = (
    "Painted once with a sky full of laughing moons. Most of the paint has flaked away; "
    "the laughing hasn't."
)
MIRRORS_SEEN = (
    "Your reflections crowd every surface, each a beat late or a beat early. Look long "
    "enough and one of them seems to be watching something just behind you."
)
MIRRORS_UNSEEN = (
    "The mirrors repeat the room and nothing else. You aren't in any of them. Only the "
    "grey figure stands outside them, unrepeated."
)
MIRRORS_FREED = "Just mirrors now, and just you in them, keeping time properly."
MIRROR_BREAK = (
    "Seven years' bad luck, times however many of these there are. You leave them be."
)
MIRROR_TOUCH = "Cold glass. Colder than the room."

# The two single-mirror rooms: (visible, invisible, ghost freed)
ROOM_MIRRORS = {
    "REJECTION-MIRROR": (
        "A tall mirror in a frame of grinning faces, the silvering gone at the edges. "
        "Your reflection watches you a moment longer than you watch it. It doesn't look "
        "pleased to see you.",
        "A tall mirror in a frame of grinning faces. It shows the room, the doorway, the "
        "faces. It doesn't show you.",
        "A tall mirror in a frame of grinning faces. Your reflection keeps time with you "
        "now, which is somehow worse.",
    ),
    "SHATTER-TRAP-MIRROR": (
        "Larger than the last, the glass rippled with age. Your reflection wavers as you "
        "move, as if it's deciding whether to let you by.",
        "Larger than the last, the glass rippled with age. The ripples move across an "
        "empty room.",
        "Larger than the last, the glass rippled with age. Your reflection wavers, but "
        "it lets you be.",
    ),
}

_SEARCHES = ("V-SEARCH", "V-DIG", "V-MOVE", "V-PUSH", "V-PULL", "V-RAISE", "V-OPEN",
             "V-LOOK-INSIDE", "V-LOOK-UNDER")


def rubble_action(w: World) -> int:
    if w.prsa in _SEARCHES:
        print(RUBBLE_SEARCH)
        return M_HANDLED
    if w.prsa in ("V-CLIMB", "V-CLIMB-UP"):
        print(RUBBLE_CLIMB)
        return M_HANDLED
    return M_NOT_HANDLED


def journals_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-READ", "V-OPEN", "V-SEARCH"):
        print(JOURNALS)
        return M_HANDLED
    if w.prsa == "V-TAKE":
        print(JOURNALS_STAY)
        return M_HANDLED
    return M_NOT_HANDLED


def equipment_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-SEARCH"):
        print(EQUIPMENT)
        return M_HANDLED
    return M_NOT_HANDLED


def crates_action(w: World) -> int:
    if w.prsa in _SEARCHES:
        print(CRATES_SEARCH)
        return M_HANDLED
    return M_NOT_HANDLED


def mirrors_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-LOOK-INSIDE"):
        from content.chuckle import _visible
        seen, unseen, freed = ROOM_MIRRORS.get(
            w.here.name, (MIRRORS_SEEN, MIRRORS_UNSEEN, MIRRORS_FREED))
        if w.get_global("GHOST-FREED"):
            print(freed)
        else:
            print(seen if _visible(w) else unseen)
        return M_HANDLED
    if w.prsa in ("V-DESTROY", "V-MELEE"):
        print(MIRROR_BREAK)
        return M_HANDLED
    if w.prsa in ("V-RUB", "V-TOUCH"):
        print(MIRROR_TOUCH)
        return M_HANDLED
    return M_NOT_HANDLED


def tower_papers(w: World) -> int:
    """EXAMINE / READ PAPERS, SEARCH DESK: Will covers them if he's there."""
    here = w.objects["WILL"].location is w.here
    print(TOWER_PAPERS_WILL if here else TOWER_PAPERS_ALONE)
    return M_HANDLED


def tower_desk_action(w: World) -> int:
    if w.prsa == "V-SEARCH":                 # not the room's SEARCH: that stays available
        return tower_papers(w)
    return M_NOT_HANDLED


def tower_papers_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-READ", "V-SEARCH"):
        return tower_papers(w)
    return M_NOT_HANDLED


def catalogue_action(w: World) -> int:
    if w.prsa in ("V-SEARCH", "V-OPEN", "V-LOOK-INSIDE"):
        print(CATALOGUE_CARD)
        return M_HANDLED
    return M_NOT_HANDLED


def fountain_action(w: World) -> int:
    if w.prsa == "V-EXAMINE":
        print(FOUNTAIN_RUNNING if w.get_global("FOUNTAIN-RUNNING") else FOUNTAIN_DRY)
        return M_HANDLED
    return M_NOT_HANDLED


def dial_action(w: World) -> int:
    if w.prsa != "V-EXAMINE" or w.here is None or w.here.name != "ALTAR":
        return M_NOT_HANDLED
    from content import altar
    n = altar._dial(w)
    print(DIAL + " " + DIAL_GLOW.format(symbol=SYMBOLS[n], religion=altar.RELIGIONS[n]))
    return M_HANDLED


def hall_doors_action(w: World) -> int:
    if w.prsa in ("V-OPEN", "V-KNOCK", "V-ENTER", "V-UNLOCK"):
        from content.tavern import ROOMS_RENTED
        print(ROOMS_RENTED)
        return M_HANDLED
    return M_NOT_HANDLED


def window_view(w: World) -> str:
    if w.here.name == "UPSTAIRS-HALL":
        return ALLEY_QUIET if w.get_global("MUGGER-DEAD") else ALLEY_MUGGER
    return VIEWS[w.here.name]


def window_action(w: World) -> int:
    if w.prsa == "V-EXAMINE":
        print(window_view(w))
        return M_HANDLED
    if w.prsa in ("V-OPEN", "V-DESTROY", "V-CLIMB", "V-ENTER", "V-MELEE"):
        print(WINDOW_SHUT)
        return M_HANDLED
    return M_NOT_HANDLED


# --- TODO #28 (2026-10-15): nouns the room text names ---------------------------------
# Plain ones (default "nothing special" line): the Back Alley's crates, the range's
# targets, the pews, the mausoleum's iron door, the crypt's alcoves, passage and
# footprints (once visited), the Creature Den's bones. Lines in locations.md.
VOLCANO = "Large, dark, and smoking gently. It seems determined to be every inch a volcano."
VOLCANO_FOUND = "Even knowing about the stairs, it doesn't look any less real. That's the unsettling part."
PEDESTAL = ("A waist-high column of the same deliberate stonework. The figurine sits "
            "exactly at its center, as if someone measured.")
PEDESTAL_EMPTY = "A waist-high column of the same deliberate stonework, empty now."
RING_STONES = ("Five rune stones, waist-high, set evenly around the symbol. Each has one "
               "rune cut deep into its face: Air, Earth, Fire, Water, and a heart.")
CIRCLE_SYMBOL = ("Lines cut into the packed earth run from the center out to each of the "
                 "five stones, joining them.")


def volcano_action(w: World) -> int:
    if w.prsa != "V-EXAMINE":
        return M_NOT_HANDLED
    print(VOLCANO_FOUND if w.get_global("VOLCANO-STAIRS-FOUND") else VOLCANO)
    return M_HANDLED


def pedestal_action(w: World) -> int:
    """The Idol Room's pedestal: the idol on it, the salt, or nothing; the plate
    line once it's been spotted (upper_tier.py — Trap 33)."""
    if w.prsa != "V-EXAMINE":
        return M_NOT_HANDLED
    from content import upper_tier as ut
    if ut._idol_on_pedestal(w):
        lines, plate = [PEDESTAL], ut._IDOL_SPOTTED
    elif w.get_global("IDOL-SWAPPED"):
        lines, plate = [ut.SALT_ON_PEDESTAL], ut._PLATE_SALTED
    else:
        lines, plate = [PEDESTAL_EMPTY], ut._PLATE_FIRED
    if w.get_global("IDOL-PLATE-SPOTTED"):
        lines.append(plate)
    print(" ".join(lines))
    return M_HANDLED
