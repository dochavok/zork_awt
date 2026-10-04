"""
Town Hall — the Records Room Worker and the town charter (Quest 17 → 27).

Design: locations.md (Town Hall, Council Chamber, Records Room, Upper Hall,
The Tower), npcs.md (Records Room Worker), quests.md (Quest 17).
- The worker refuses the charter until he's given the pocket watch.
- GIVE WATCH TO WORKER: he recognises it as his family's, hands over the
  charter, and Quest 17 completes (17 XP, 8 Zenni).
- Council Chamber (Rowan Finch, Quest 32), the Upper Hall cabinet (Quest 4)
  and the Trophy Case in the Tower (content/trophy_case.py) come with their own
  sections.

State: CHARTER-GIVEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.world import Room, Exit, ONBIT, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_WORKER_REFUSES = (
    "The clerk doesn't put down his pen. \"If you're here about the charter, the "
    "answer is no. It's the town's only copy, and the town isn't in the habit of "
    "lending it to strangers.\" He goes back to his ledger."
)
_WORKER_GIVEN = (
    "The clerk takes the watch without much interest — then turns it over, and "
    "stops. He opens the lid and looks at the worn engraving for a long time, his "
    "thumb moving across it as if he can read it by touch.\n"
    '"This was my uncle\'s," he says quietly. "He went into that place by the '
    'graveyard. We never—" He stops. Closes the lid. Holds it a moment longer.\n'
    "Then he stands, goes to a shelf without looking, and comes back with a "
    "rolled document tied in faded ribbon. He puts it in your hands. \"The "
    'charter. Take it. Whatever you need it for."\n'
    "[Town Charter added to inventory.]"
)
_WORKER_AFTER = (
    "The clerk is turning the pocket watch over in his hands. He nods to you, "
    "but doesn't say anything."
)


def talk_worker(w: World) -> None:
    print(_WORKER_AFTER if w.get_global("CHARTER-GIVEN") else _WORKER_REFUSES)


def give_watch(w: World) -> None:
    from content import quests
    print(_WORKER_GIVEN)
    w.set_global("CHARTER-GIVEN", True)
    w.move_object(w.objects["POCKET-WATCH"], w.objects["RECORDS-WORKER"])
    w.move_object(w.objects["TOWN-CHARTER"], w.player)
    quests.complete(w, "17")


def make_rooms(world) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    hall = room(
        "TOWN-HALL", "Town Hall",
        "The Town Hall in Roundabout dominates the northern side of the town "
        "square. It is a massive brick building with two floors, a broad sloped "
        "roof, and a tower with a conical roof in the center. The double doors "
        "are solid oak and very heavy.\n"
        "Inside, the foyer is wide and echoing, the floor worn smooth in a path "
        "from the doors to the stairs. The Council Chamber opens to the east, the "
        "Records Room to the west, and a staircase climbs to the floor above.",
    )
    council = room(
        "COUNCIL-CHAMBER", "Council Chamber",
        "The room where Roundabout conducts its official business, which is to "
        "say the room where Roundabout sits in chairs and argues.\n"
        "A long table dominates the center — solid oak, scarred from use. The "
        "chairs around it are mismatched in the way of things that have been "
        "replaced one at a time over many years.\n"
        "A man sits at the far end with the bearing of someone who has inherited "
        "both the title and the table.",
    )
    records = room(
        "RECORDS-ROOM", "Records Room",
        "Floor-to-ceiling shelves on every wall, packed with ledgers and rolled "
        "documents in an order that apparently makes sense to someone.\n"
        "The room smells of old paper and the particular dust of things that "
        "have not been touched in years.\n"
        "A clerk sits at a desk near the window, surrounded by more of the same. "
        "He looks up when you enter with the expression of a man who was hoping "
        "you wouldn't.",
    )
    upper = room(
        "UPPER-HALL", "Upper Hall",
        "The second floor is quieter than the ground floor in the way that second "
        "floors always are — the noise of official business doesn't quite reach "
        "here.\n"
        "A long hall with a runner of carpet gone thin at the center.\n"
        "A display cabinet stands against the wall, unlocked, glass-fronted, "
        "holding an assortment of old civic documents and artifacts. The kind of "
        "things a town keeps because no one has decided to throw them away.",
    )
    tower = room(
        "TOWN-HALL-TOWER", "The Tower",
        "The tower room is round, the walls following the cone of the roof above. "
        "A single window looks out over the town square, narrow enough that the "
        "view is more suggestion than panorama.\n"
        "The Trophy Case dominates the far wall — old wood and glass, built into "
        "the stone as if someone planned for it from the start. It is empty.\n"
        "The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN "
        "PERPETUITY FOR THE GLORY OF ROUNDABOUT.\n"
        "The case has not been added to in some time.",
    )

    world.rooms["TOWN-SQUARE"].exits["north"] = Exit(destination="TOWN-HALL")
    hall.exits.update(south=Exit(destination="TOWN-SQUARE"), east=Exit(destination="COUNCIL-CHAMBER"),
                      west=Exit(destination="RECORDS-ROOM"), up=Exit(destination="UPPER-HALL"))
    council.exits["west"] = Exit(destination="TOWN-HALL")
    records.exits["east"] = Exit(destination="TOWN-HALL")
    upper.exits.update(down=Exit(destination="TOWN-HALL"), up=Exit(destination="TOWN-HALL-TOWER"))
    tower.exits["down"] = Exit(destination="UPPER-HALL")
