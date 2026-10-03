"""
The Dankhaus and Litlock — Quest 52, Make Litlock Laugh.

Design: locations.md (Bog-SE, the Dankhaus rooms), npcs.md (Litlock),
quests.md (Quest 52).
- Bog-SE: Medium perception check every visit until the path east is found.
- East from Bog-SE: hidden until the path is found; warded until Lynds's
  invitation (DANKHAUS-INVITED, set when Lynds is beaten).
- Litlock's 2×2×2 tree: numbered menu after each line. Failures loop back to
  Tier 1. Success: the bonk — Chuckle House visible, Quest 52 complete.

State: DANKHAUS-PATH-FOUND, LITLOCK-MET, LITLOCK-TIER, LITLOCK-PATH,
       LITLOCK-BONKED, CHUCKLE-HOUSE-VISIBLE
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, ONBIT, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# Bog-SE — the hidden path and the wards
# ---------------------------------------------------------------------------

BOG_SE_LDESC = (
    "The bog stretches in every direction, dark water between clumps of "
    "soggy earth. The smell is comprehensive and personal. Reeds crowd the "
    "edges of every dry patch. Something is moving just out of sight, or was."
)
_PATH_LINE = "A narrow path leads east through the brush to a low, round yurt."
_PATH_SPOTTED = (
    "Off to the east, the brush isn't quite as dense as it should be. Behind "
    "it, a path — narrow, deliberate — leads to something low and round. A "
    "yurt, improbably dry."
)
_WARD = (
    "Something in the air near the door shifts as you approach. Not hostile. "
    "More like a house that knows you haven't been introduced yet."
)


class _WardedExit(Exit):
    """East from Bog-SE: hidden until the path is found, warded until invited."""

    def resolve(self, world):
        if not world.get_global("DANKHAUS-PATH-FOUND"):
            return None, "You can't go that way."
        if not world.get_global("DANKHAUS-INVITED"):
            return None, _WARD
        return super().resolve(world)


def bog_se_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER and not w.get_global("DANKHAUS-PATH-FOUND"):
        from content.player import check_perception
        from content.perception import MEDIUM
        if check_perception(w, MEDIUM):
            w.set_global("DANKHAUS-PATH-FOUND", True)
            w.set_global("DANKHAUS-PATH-JUST-FOUND", True)
            w.objects["DANKHAUS"].clear_flag("INVISIBLE")
        return M_NOT_HANDLED
    if msg == M_LOOK:
        print(BOG_SE_LDESC)
        if w.get_global("DANKHAUS-PATH-FOUND") and not w.get_global("DANKHAUS-PATH-JUST-FOUND"):
            print(_PATH_LINE)
        return M_HANDLED
    if msg == M_END and w.get_global("DANKHAUS-PATH-JUST-FOUND"):
        w.set_global("DANKHAUS-PATH-JUST-FOUND", False)
        print(_PATH_SPOTTED)
    return M_NOT_HANDLED


def enter_dankhaus(w: World) -> None:
    """ENTER DANKHAUS / ENTER YURT from Bog-SE — same as walking east."""
    w.walk_dir = "east"
    w.game.do_walk("east")


# ---------------------------------------------------------------------------
# Rooms (locations.md). Dankhaus rooms aren't strictly grid-aligned — see the
# layout note there.
# ---------------------------------------------------------------------------

def make_rooms(world, bog_se: Room) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    common = room(
        "DANKHAUS-COMMON-ROOM", "Dankhaus Common Room",
        "Litlock fills whatever room he's in without trying to. The common room "
        "is large enough, and he's in it — near the fireplace, which is also "
        "large, and burning steadily. Chairs, a table, shelves. The kind of room "
        "that works because the people in it make it work. He looks up.",
        value=3,
    )
    hearth = room(
        "DANKHAUS-HEARTH-ROOM", "Dankhaus Hearth Room",
        "A working hearth room — herbs drying overhead, something on the fire, "
        "the garden accessible through the east door. It smells like it has "
        "always smelled like this.",
    )
    garden = room(
        "DANKHAUS-GARDEN", "Dankhaus Garden",
        "The garden shouldn't work. The bog is right there, the soil is wrong, "
        "and nothing about this location suggests flowers or vegetables. And "
        "yet. Raised beds, neatly kept. Things growing that have no business "
        "growing here. The Dankhaus wall is to the west. The bog presses in on "
        "every other side and seems to have accepted that it lost this argument.",
    )
    litlocks_room = room(
        "LITLOCKS-ROOM", "Litlock's Room",
        "A plain room — bed, chest, a low shelf of things that don't announce "
        "themselves. Nothing here suggests the man who laughed until he had to "
        "put something down. That version of Litlock lives in the common room. "
        "This one is private.",
    )
    study = room(
        "LITLOCKS-STUDY", "Litlock's Study",
        "The study is where Litlock keeps the part of himself he doesn't lead "
        "with. Shelves of books and things that aren't books. A desk with papers "
        "in an order that makes sense to someone. A candle burned low. The "
        "jovial man from the common room was entirely real — so is this room, "
        "and they belong to the same person.",
    )
    lynds_room = room(
        "LYNDS-ROOM", "Lynds's Room",
        "Lynds's room. Large, untidy, comfortable. The furniture has been "
        "through some things.",
    )
    aurix_room = room(
        "AURIX-ROOM", "Aurix's Room",
        "Small bed, small shelf, the accumulated objects of a child who picks "
        "things up and keeps them. The chalk marks on the floor have been there "
        "long enough that no one is going to do anything about them.",
    )

    bog_se.exits["east"] = _WardedExit(destination="DANKHAUS-COMMON-ROOM")
    common.exits.update(west=Exit(destination="BOG-SE"), east=Exit(destination="DANKHAUS-HEARTH-ROOM"),
                        north=Exit(destination="LITLOCKS-ROOM"), south=Exit(destination="AURIX-ROOM"))
    hearth.exits.update(west=Exit(destination="DANKHAUS-COMMON-ROOM"),
                        south=Exit(destination="LYNDS-ROOM"), east=Exit(destination="DANKHAUS-GARDEN"))
    garden.exits["west"] = Exit(destination="DANKHAUS-HEARTH-ROOM")
    litlocks_room.exits.update(south=Exit(destination="DANKHAUS-COMMON-ROOM"),
                               east=Exit(destination="LITLOCKS-STUDY"))
    study.exits["west"] = Exit(destination="LITLOCKS-ROOM")
    lynds_room.exits["north"] = Exit(destination="DANKHAUS-HEARTH-ROOM")
    aurix_room.exits["north"] = Exit(destination="DANKHAUS-COMMON-ROOM")

    bog_se.ldesc = ""
    bog_se.action = bog_se_action
    common.action = common_room_action


# ---------------------------------------------------------------------------
# Litlock — Quest 52 (npcs.md: full tree)
# ---------------------------------------------------------------------------

_INCITING = (
    "Litlock looks up from whatever he's doing with the particular alertness "
    "of someone who has been waiting for company without admitting it to "
    "himself. He takes you in. Then he grins — wide, genuine, the kind that "
    "arrives before the person decides to smile.\n"
    '"Right," he says. "Entertain me."'
)
_RESTART = '"Right," Litlock says. "Entertain me."'

_MENUS = {
    "1":  ("Tell a joke", "Do something physical"),
    "2A": ("A pun", "An absurd observation"),
    "2B": ("Something dignified", "Something committed and ridiculous"),
    "3":  ("Push further", "Explain it"),
}

_A = (
    'You clear your throat. "I have a joke."\n'
    'Litlock leans back. "Everyone has a joke. Let\'s see if yours is different."'
)
_B = (
    "You don't say anything. You just do something.\n"
    "Litlock watches with the focused attention of a man who has seen a great "
    "deal and is genuinely curious whether this will be new."
)
_A1 = (
    "You deliver the pun. It lands with the particular thud of something that "
    "was never going to work.\n"
    'Litlock stares at you for a moment. "That," he says carefully, "was a pun. '
    'I respect that you tried. I do not respect the pun." He waves a hand. "Again."'
)
_A2 = (
    '"You know," you say, "I\'ve been thinking about the bog. Specifically '
    "about the smell. And I think the smell isn't the bog at all — I think the "
    "bog smells fine and it's everything else that's wrong.\"\n"
    "Litlock blinks. Then something shifts in his expression — not quite a "
    "laugh yet, but its immediate predecessor.\n"
    '"Go on," he says.'
)
_B1 = (
    "You execute a formal bow. Precise. Respectful. Technically flawless.\n"
    'Litlock watches the whole thing. "That was very well done," he says. "I am '
    'completely unmoved. Try something else."'
)
_B2 = (
    "You sit down on the floor. Not because there's nowhere to sit — there are "
    "chairs. You just sit on the floor, look up at Litlock, and wait.\n"
    "Litlock looks at you. Looks at the chairs. Looks back at you.\n"
    "Something in his face is working very hard not to become a laugh.\n"
    '"Why," he says carefully, "are you on the floor?"'
)
_C1 = {
    "A": ('"In fact," you continue, with complete conviction, "I think the bog has '
          'been unfairly maligned for years, and someone should apologize to it."'),
    "B": ('You look up at him from the floor. "I find it clarifying," you say. '
          '"You should try it."'),
}
_C1_LAUGH = (
    "That does it.\n"
    "Litlock laughs — fully, completely, the kind of laugh that takes over a "
    "person entirely. He laughs until he has to put something down. He laughs "
    "until Aurix appears in the doorway to see what's happening and then "
    "disappears again.\n"
    "When he finally stops, he wipes his eyes, looks at you with something that "
    "might be respect, and reaches over and bonks you firmly on the top of the "
    "head with two knuckles.\n"
    '"There," he says. "You\'ll see things a bit differently now. Don\'t ask me '
    'to explain it."\n'
    "He picks up whatever he put down and goes back to it, still smiling."
)
_C2 = {
    "A": ('"What I mean is," you begin, "the fundamental olfactory baseline of—"\n'
          'Litlock holds up a hand. "Stop. You were almost there. You explained it. '
          'You can never explain it." He shakes his head with genuine sadness. "Again."'),
    "B": ('"It\'s a metaphor," you say. "For groundedness. For—"\n'
          'Litlock closes his eyes briefly. "You were right there," he says. "Right '
          'there. And then you talked." He opens his eyes. "Again."'),
}


def _menu(tier: str) -> None:
    a, b = _MENUS[tier]
    print(f"  1. {a}\n  2. {b}")


def _start(w: World, text: str) -> None:
    print(text)
    w.set_global("LITLOCK-TIER", "1")
    _menu("1")


def common_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    """Inciting moment on the first visit after the wards clear (Quest 52)."""
    if msg == M_END and not w.get_global("LITLOCK-MET"):
        from content import quests
        w.set_global("LITLOCK-MET", True)
        quests.discover(w, "52")
        _start(w, _INCITING)
    return M_NOT_HANDLED


def talk_litlock(w: World) -> None:
    if w.get_global("LITLOCK-BONKED"):
        print("Litlock is still smiling about it.")
        return
    _start(w, _RESTART)


def litlock_input_hook(w: World, text: str) -> bool:
    """Numbered choices while Litlock's tree is open in the Common Room."""
    tier = w.get_global("LITLOCK-TIER")
    if not tier or w.here is None or w.here.name != "DANKHAUS-COMMON-ROOM":
        return False
    choice = text.strip()
    if choice not in ("1", "2"):
        return False

    if tier == "1":
        if choice == "1":
            print(_A); w.set_global("LITLOCK-TIER", "2A"); _menu("2A")
        else:
            print(_B); w.set_global("LITLOCK-TIER", "2B"); _menu("2B")
    elif tier in ("2A", "2B"):
        path = tier[1]
        fail, success = (_A1, _A2) if path == "A" else (_B1, _B2)
        if choice == "1":
            print(fail); w.set_global("LITLOCK-TIER", "1"); _menu("1")
        else:
            print(success); w.set_global("LITLOCK-PATH", path)
            w.set_global("LITLOCK-TIER", "3"); _menu("3")
    elif tier == "3":
        path = w.get_global("LITLOCK-PATH") or "A"
        if choice == "1":
            print(_C1[path]); print(_C1_LAUGH)
            _bonk(w)
        else:
            print(_C2[path]); w.set_global("LITLOCK-TIER", "1"); _menu("1")
    return True


def _bonk(w: World) -> None:
    from content import quests
    w.set_global("LITLOCK-TIER", None)
    w.set_global("LITLOCK-BONKED", True)
    w.set_global("CHUCKLE-HOUSE-VISIBLE", True)
    quests.complete(w, "52")
