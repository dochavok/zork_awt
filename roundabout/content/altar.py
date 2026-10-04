"""
The Church of All altar: the attunement dial and the ring binding ritual.

Design: ring-rituals.md (The Church of All Altar), locations.md (The Altar),
experience.md (Ring ritual — 5 XP).

- TURN DIAL RIGHT moves forward through the seven religions, LEFT moves back;
  both wrap. Default: The Keepers of the Lantern.
- Each artifact glows when its religion is selected — placed first and then
  attuned, or placed while already attuned. A glow stays lit when the dial
  moves on; taking the artifact off the altar puts it out.
- PUT RING ON ALTAR with all three glowing: the binding ceremony. The
  artifacts are consumed and the ring returns to the inventory, bound.
  Placing it doesn't tick corruption; a worn ring comes off first through the
  normal removal (the late-stage removal roll still applies).

State: DIAL (index 0–6), GLOW-<artifact>, ring_bound
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK
from engine.world import Room, Exit, ONBIT, RLANDBIT, NDESCBIT, WEARBIT

if TYPE_CHECKING:
    from engine.world import World

RELIGIONS = [
    "The Verdant Circle", "The Veil of the Arcane", "The Brotherhood of the Pale Blade",
    "The Weavers of the Thread", "The House of the Coin", "The Keepers of the Lantern",
    "The Hearth Folk",
]
_DEFAULT = 5   # The Keepers of the Lantern

# artifact object → (religion index, glow line, listing verb, colour)
_ARTIFACTS = {
    "PALE-BLADE": (2, "The Pale Blade begins to glow — a clean white light, steady, coming "
                      "from somewhere inside the steel.", "lies", "white"),
    "WEREWOLFS-AMULET": (1, "The Werewolf's Amulet begins to glow — a deep red, pulsing "
                            "faintly at the void in the star's center.", "lies", "red"),
    "CRYSTAL-BOWL": (0, "The Crystal Bowl begins to glow — green, soft and even, as if light "
                        "were pooling in it like water.", "sits", "green"),
}

_ALTAR = (
    "The altar is plain stone, unadorned. The dial dominates it — brass, worn at the "
    "edges from use, seven symbols arranged around its face. The currently selected "
    "religion is marked in a faint glow. The air here feels slightly different from "
    "the nave. Not sacred, exactly. Attentive."
)
_PLACED = "You set the {name} on the altar. It rests on the bare stone. Nothing happens — yet."
_DOESNT_BELONG = "That doesn't belong on the altar."
_NOT_YET = "Nothing happens. Something is missing from the ritual. You pick up the ring."
_CEREMONY = (
    "The altar goes still. The three lights — green, red, white — begin to move, "
    "slowly, tracing the edge of the stone toward the ring.\n\n"
    "The green reaches it first. The Crystal Bowl — patience, growth, the long memory "
    "of living things. It wraps the ring in something ancient and unhurried, the way "
    "roots find stone. The bowl glows brightly and disappears into light.\n\n"
    "The red follows. The Werewolf's Amulet — arcane power, older than the names given "
    "to it. It finds the ring's hidden nature and drags it into the light where it "
    "cannot pretend to be otherwise. The amulet fades into magic.\n\n"
    "The white arrives last. The Pale Blade — sacrifice, the calm acceptance of what "
    "must be given up. It seals what the others have found and named. A glint flashes "
    "off the blade, and it's gone.\n\n"
    "The ring sits on the altar alone. Whatever door was open in the ring is closed. "
    "For now.\n\n"
    "The ring is bound."
)


def _dial(w: World) -> int:
    d = w.get_global("DIAL")
    return _DEFAULT if d is None else d


def _on_altar(w: World, name: str) -> bool:
    return w.objects[name].location is w.rooms["ALTAR"]


def _glowing(w: World, name: str) -> bool:
    return bool(w.get_global("GLOW-" + name))


def _light_matching(w: World) -> None:
    """Light any artifact on the altar whose religion is now selected."""
    for name, (religion, line, _, _) in _ARTIFACTS.items():
        if _on_altar(w, name) and not _glowing(w, name) and religion == _dial(w):
            print(line)
            w.set_global("GLOW-" + name, True)


def turn_dial(w: World, step: int) -> None:
    if w.here is None or w.here.name != "ALTAR":
        print("There's no dial here.")
        return
    w.set_global("DIAL", (_dial(w) + step) % len(RELIGIONS))
    print(f"The altar shimmers. The dial is set to {RELIGIONS[_dial(w)]}.")
    _light_matching(w)


def altar_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_ALTAR)
        print(f"The dial is set to {RELIGIONS[_dial(w)]}.")
        for name, (_, _, verb, colour) in _ARTIFACTS.items():
            if _on_altar(w, name):
                obj = w.objects[name]
                glow = f", glowing {colour}" if _glowing(w, name) else ""
                print(f"The {obj.desc} {verb} on the altar{glow}.")
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    stone = w.objects["ALTAR-STONE"]
    if w.prsa == "V-PUT-ON" and w.prsi is stone and w.prso is not None:
        _put_on_altar(w, w.prso)
        return M_HANDLED
    if w.prsa == "V-TAKE" and w.prso is not None and w.prso.name in _ARTIFACTS \
            and _on_altar(w, w.prso.name):
        w.set_global("GLOW-" + w.prso.name, False)   # off the altar, the glow goes out
        w.prso.clear_flag(NDESCBIT)
    return M_NOT_HANDLED


def _put_on_altar(w: World, obj) -> None:
    if obj not in w.player.contents:
        print(f"You aren't carrying the {obj.desc}.")
        return
    if obj.name == "RING":
        _place_ring(w, obj)
        return
    if obj.name not in _ARTIFACTS:
        print(_DOESNT_BELONG)
        return
    print(_PLACED.format(name=obj.desc))
    w.move_object(obj, w.here)
    obj.set_flag(NDESCBIT)                 # the altar listing describes it
    _light_matching(w)


def _place_ring(w: World, ring) -> None:
    if ring.has_flag(WEARBIT):
        from content import corruption
        if not corruption.try_remove_ring(w):
            return                          # the late-stage roll failed; it stays on
        ring.clear_flag(WEARBIT)
        from content import chuckle
        chuckle.update_ghost_visibility(w)
    if not all(_on_altar(w, n) and _glowing(w, n) for n in _ARTIFACTS):
        print(_NOT_YET)                     # the ring stays in the inventory
        return
    from content.experience import award_xp
    print(_CEREMONY)
    for name in _ARTIFACTS:
        w.move_object(w.objects[name], None)        # consumed
        w.set_global("GLOW-" + name, False)
    w.globals["ring_bound"] = True                  # back in the inventory, bound
    award_xp(w, 5)


def make_rooms(world) -> None:
    altar = Room(name="ALTAR", desc="The Altar", ldesc="", value=1)
    altar.set_flag(ONBIT)      # part of the church
    altar.set_flag(RLANDBIT)
    world.register_room(altar)
    world.rooms["CHURCH-NAVE"].exits["east"] = Exit(destination="ALTAR")
    altar.exits["west"] = Exit(destination="CHURCH-NAVE")
    altar.action = altar_action
