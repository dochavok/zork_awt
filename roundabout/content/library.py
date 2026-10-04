"""
The Library — Main Hall (the Librarian) and The Stacks (the Archivist).
Design: locations.md (Library), npcs.md (The Librarian, The Archivist),
quests.md (Quest 28).

GIVE RUBBING TO ARCHIVIST (or TALK TO ARCHIVIST carrying it): his line, the
incantation scroll to the inventory, Quest 28 completes (3 Zenni, silent).

Deferred: the Archivist's book-research mechanic (TALK TO ARCHIVIST about a
subject, READ BOOK) — see todo.md.
"""

from __future__ import annotations
from engine.world import World, Room, Exit, ONBIT, RLANDBIT

_MAIN_HALL = (
    "The library is smaller than the building suggests from outside — half the "
    "floor space is shelving, floor to ceiling, packed in columns with narrow gaps "
    "between.\n"
    "A card catalogue occupies one wall. The other holds a reading table, lamp "
    "burning low, a cup of something gone cold.\n"
    "The librarian looks up when you enter. Unlike every librarian you have ever "
    "imagined, she appears to want to talk to you."
)
_STACKS = (
    "The passage from the Main Hall opens into something that shouldn't fit "
    "inside this building.\n"
    "The shelves here are older — darker wood, no labels, arranged in a logic "
    "that isn't immediately obvious and may not be alphabetical. The ceiling is "
    "lost somewhere above the lamplight.\n"
    "At the far end, a large table holds the controlled wreckage of ongoing work: "
    "rolled maps weighted open at the corners, books splayed face-down, sheets of "
    "careful notation in a hand that doesn't waste space.\n"
    "The Archivist sits at the center of it, or rather the work surrounds him and "
    "he happens to be there too."
)

# npcs.md — The Librarian
_LIBRARIAN_FIRST = (
    "She sets down what she's holding and folds her hands on the desk. Her voice "
    "arrives in pieces — tones and rhythms that don't quite match, stitched "
    "together at the seams.\n"
    '"I have been waiting for someone to come asking."\n'
    "She pulls a thin ledger from under the desk without looking for it.\n"
    "\"'The Veil of the Arcane — I need access to whatever you have.' That's what "
    "he said. First thing. Didn't introduce himself. I didn't ask.\"\n"
    "She opens the ledger to a marked page.\n"
    "\"He was here for — weeks. Every day. 'Have you found anything else? Anything "
    "older?' He was very — 'I think I've found something. I think I know where it "
    "is.'\"\n"
    "She closes the ledger.\n"
    "\"And then he stopped coming. I checked the application. There's a date. "
    "There's no — 'I'll be back by —' there's no return date. There never was.\"\n"
    "She looks at you steadily.\n"
    "\"'The lower passages. That's where it will be. That's where everything that "
    "old ends up.'\"\n"
    "She sets the ledger aside."
)
_LIBRARIAN_AGAIN = "\"'The lower passages.' That's all I have. That's the last thing.\""
_LIBRARIAN_AFTER_WEREWOLF = (
    "She looks at you for a moment when you come in.\n"
    "\"'It's not a dead end — it's a beginning.'\"\n"
    'She picks up her book. "He said that once, about a research problem. I think '
    'about it."'
)

# npcs.md — The Archivist (Quest 28)
_ARCHIVIST_FIRST = (
    "He looks up when spoken to, marking his place with two fingers before "
    "setting the book aside.\n"
    "\"Yes. I've been trying to authenticate a map — provenance is unclear, which "
    "makes it nearly useless for the purpose I need it for. There's an engraving "
    "in the lower passages that should settle the question, if I could get a "
    'clean impression of it."\n'
    "He glances at the table, then back.\n"
    "\"I can't leave this. If you're heading down that way — thin paper, a stick "
    "of charcoal, and some patience. The engraving is in the Inscription Chamber. "
    'You\'ll know it when you see it."'
)
ARCHIVIST_RUBBING = (
    "He takes the rubbing and holds it to the light without speaking for a "
    "moment.\n"
    '"Yes." He sets it down flat, smoothing the edges. "This appears to be an '
    'answer to a question I was never able to find." He opens a drawer and '
    'produces a rolled scroll. "Take this. I\'ve had it for years — couldn\'t '
    'place it. I suspect you\'ll find the question before I would."'
)
_ARCHIVIST_AFTER_SCROLL = (
    "He is already working when you arrive.\n"
    '"Whatever that engraving answers — I suspect it\'s somewhere in the lower '
    'passages. Somewhere that feels like it\'s waiting." He doesn\'t look up. '
    '"That\'s not intuition. That\'s just what the text implies."'
)
_ARCHIVIST_AFTER_Q34 = (
    '"The soldier." He says it quietly, to himself as much as to you. "I had '
    'assumed the chamber was ceremonial. Not occupied." He makes a note. "Thank '
    'you for telling me."'
)


def talk_librarian(w: World) -> None:
    if w.get_global("WEREWOLF-DEAD"):
        print(_LIBRARIAN_AFTER_WEREWOLF)
    elif w.get_global("LIBRARIAN-MET"):
        print(_LIBRARIAN_AGAIN)
    else:
        print(_LIBRARIAN_FIRST)
        w.set_global("LIBRARIAN-MET", True)


def talk_archivist(w: World) -> None:
    from content import quests
    if quests.get_state(w, "34") == quests.COMPLETE:
        print(_ARCHIVIST_AFTER_Q34)
    elif quests.get_state(w, "28") == quests.COMPLETE:
        print(_ARCHIVIST_AFTER_SCROLL)
    elif w.player is not None and w.objects["RUBBING"] in w.player.contents:
        give_rubbing(w)
    else:
        print(_ARCHIVIST_FIRST)
        quests.discover(w, "28")


def give_rubbing(w: World) -> None:
    """GIVE RUBBING TO ARCHIVIST (or TALK TO him carrying it) — Quest 28."""
    from content import quests
    w.move_object(w.objects["RUBBING"], None)
    print(ARCHIVIST_RUBBING)
    print("[Incantation scroll added to inventory.]")
    w.move_object(w.objects["INCANTATION-SCROLL"], w.player)
    quests.complete(w, "28")     # 3 Zenni, paid silently


def make_rooms(world) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=1)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    hall = room("LIBRARY", "Library — Main Hall", _MAIN_HALL)
    stacks = room("STACKS", "The Stacks", _STACKS)
    world.rooms["MAIN-WEST"].exits["north"] = Exit(destination="LIBRARY")
    hall.exits.update(south=Exit(destination="MAIN-WEST"), east=Exit(destination="STACKS"))
    stacks.exits["west"] = Exit(destination="LIBRARY")
