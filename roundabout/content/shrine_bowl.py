"""
Quest 49 — The Ruined Shrine: clay adhesive, the repaired bowl and the
Verdant Circle shrine offering (Roundabout Forest).

Design: quests.md (Quest 49), items.md (Fire Clay, Clay Adhesive, Repaired
Bowl, The Crystal Bowl, Verdant Circle Shrine Bowl), locations.md (Town Square
fountain; Roundabout Forest pedestal states), ring-rituals.md (Artifact 3).

- MIX CLAY WITH WATER at the flowing Town Square fountain → clay adhesive.
- ASSEMBLE BOWL (REPAIR / FIX BOWL, COMBINE PIECES) anywhere with all three
  pieces and the adhesive → Repaired Bowl. An input hook: every piece answers to "bowl", so the parser would
  otherwise ask which one.
- PUT BOWL ON PEDESTAL, then PUT ZENNI ON PEDESTAL (OFFER / DROP ZENNI; COIN
  also works): 1 Zenni, the bowl becomes The Crystal Bowl, Quest 49 completes.
  The Zenni is an offering — it's gone. "Zenni" is an object only at the shrine.

State: BOWL-ON-PEDESTAL, BOWL-TRANSFORMED
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK

if TYPE_CHECKING:
    from engine.world import World

PIECES = ("BOWL-PIECE-FOREST", "BOWL-PIECE-BOG", "BOWL-PIECE-SHRINE")

_DRY = "The fountain is dry. You'll need clean running water."
_MIXED = (
    "You work the clay in your hands under the fountain's spill until it softens, "
    "then keeps softening, into something smooth and tacky that holds whatever it "
    "touches. Clay adhesive — enough for one careful job."
)
_NO_WATER = "You'll need water for that — clean and running."
_ASSEMBLED = (
    "You lay the three pieces out and work the adhesive into every edge, pressing "
    "them together one at a time. The seams hold. The etched line runs unbroken "
    "from one piece to the next, all the way around. It's a bowl again — not a "
    "pretty one, but whole."
)
_MISSING_PIECES = "You don't have all of it. Some of the bowl is still out there."
_NO_ADHESIVE = "The pieces fit, but nothing holds them together."

_FOREST_TOP = (
    "You wouldn't know, walking through here, that the ground beneath you is "
    "hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. "
    "Back to the south, the trees thin out toward the old oak.\n"
    "The mine entrance sits among the roots and undergrowth, a dark mouth "
    "leading down into the ground — easy to miss if you don't know to look.\n"
    "A stone shrine stands at the edge of the trees — old enough that the forest "
    "has started to take it back. A carved pedestal, still solid."
)
_REMAINS = (
    "On it, the remains of a ceramic bowl, smashed at some point and not recently. "
    "Three or four pieces visible here; others have clearly gone elsewhere."
)
_SYMBOL = "The symbol on the pedestal is a sprouting seed inside a circle of leaves."
_ON_PEDESTAL_REPAIRED = "The repaired bowl sits on the pedestal."
_ON_PEDESTAL_CRYSTAL = "A crystal bowl sits on the pedestal, clear as still water."
_BARE = "The pedestal is bare."

_BOWL_PLACED = (
    "The bowl settles into place. Nothing happens, but the quiet has changed. "
    "It feels like the shrine is waiting for an offering."
)
_ALREADY_PLACED = "The bowl is already on the pedestal."
_PEDESTAL = (
    "The shrine's pedestal is worn smooth on top, a shallow ring where something "
    "has rested for a long time. The symbol on it is a sprouting seed inside a "
    "circle of leaves."
)
_PRAY_BROKEN = (
    "You bow your head before the shrine. The carved seed looks back at you, "
    "patient. Whatever was offered here, it was offered in a bowl."
)
_PRAY_PLACED = (
    "You bow your head. The bowl sits empty on the pedestal. Prayers are "
    "welcome; an offering is expected."
)
_PRAY_DONE = (
    "You bow your head. Birdsong, pine, dappled light. The shrine has what it "
    "wanted."
)

# The underground Shrine Room's plinth (scenery; the bowl doesn't go here)
PLINTH = (
    "A waist-high stone plinth, finer work than anything around it. The "
    "depression in its top is bowl-shaped and empty, the stone inside worn "
    "smooth. Carved into its side, small and faded: a seed inside a circle of "
    "leaves."
)
_NOT_THIS_SHRINE = (
    "It would fit. But the symbol on the plinth is the forest shrine's, and the "
    "bowl belongs there."
)
_TRANSFORMED = (
    "The coin settles on the pedestal. For a moment, nothing. Then the bowl begins "
    "to change — ceramic going pale, then translucent, then clear. The etched "
    "design that was barely visible before catches the light now, sharp and "
    "permanent. What sits on the pedestal is no longer what you put there."
)
_JUST_A_COIN = (
    "The coin settles on the pedestal and stays there. The shrine accepts "
    "contributions at any time."
)
_NO_COIN = "You don't have a coin to offer."


# ---------------------------------------------------------------------------
# MIX CLAY WITH WATER
# ---------------------------------------------------------------------------

def mix(w: World) -> bool:
    """MIX CLAY [WITH WATER]. True if handled here."""
    clay = w.objects["FIRE-CLAY"]
    if w.prso is not clay:
        return False
    if clay not in w.player.contents:
        print(f"You aren't carrying the {clay.desc}.")
    elif w.here is None or w.here.name != "TOWN-SQUARE":
        print(_NO_WATER)
    elif not w.get_global("FOUNTAIN-RUNNING"):
        print(_DRY)
    else:
        print(_MIXED)
        w.move_object(clay, None)
        w.move_object(w.objects["CLAY-ADHESIVE"], w.player)
    return True


# ---------------------------------------------------------------------------
# ASSEMBLE BOWL
# ---------------------------------------------------------------------------

def assemble(w: World) -> None:
    held = w.player.contents
    if not all(w.objects[p] in held for p in PIECES):
        print(_MISSING_PIECES)
        return
    adhesive = w.objects["CLAY-ADHESIVE"]
    if adhesive not in held:
        print(_NO_ADHESIVE)
        return
    print(_ASSEMBLED)
    for p in PIECES:
        w.move_object(w.objects[p], None)
    w.move_object(adhesive, None)
    w.move_object(w.objects["REPAIRED-BOWL"], w.player)


def assemble_input_hook(w: World, text: str) -> bool:
    """ASSEMBLE / REASSEMBLE / REPAIR / FIX / GLUE / PATCH [THE] BOWL, COMBINE [THE] [BOWL] PIECES."""
    words = [x for x in text.lower().split() if x != "the"]
    if not words:
        return False
    verb, rest = words[0], words[1:]
    if (verb in ("assemble", "reassemble") and rest in ([], ["bowl"])) \
            or (verb in ("repair", "fix", "glue", "patch") and rest == ["bowl"]) \
            or (verb == "combine" and rest in (["pieces"], ["bowl", "pieces"])):
        assemble(w)
        return True
    return False


# ---------------------------------------------------------------------------
# The shrine pedestal (Roundabout Forest)
# ---------------------------------------------------------------------------

def _bowl_placed(w: World) -> bool:
    """The repaired bowl is on the pedestal. The location is checked too, so a
    save where the flag outlived the bowl (an old auto-take) reads correctly."""
    bowl = w.objects["REPAIRED-BOWL"]
    return bool(w.get_global("BOWL-ON-PEDESTAL")) and bowl.location is w.rooms["ROUNDABOUT-FOREST"]


def _pedestal_state(w: World) -> str:
    crystal = w.objects["CRYSTAL-BOWL"]
    if w.get_global("BOWL-TRANSFORMED"):
        return (_ON_PEDESTAL_CRYSTAL if crystal.location is w.here and crystal.has_flag("NDESCBIT")
                else _BARE)
    if _bowl_placed(w):
        return _ON_PEDESTAL_REPAIRED
    # Once the bowl is mended, its remains aren't on the pedestal any more
    return _BARE if w.objects["REPAIRED-BOWL"].location is not None else _REMAINS


def forest_look(w: World) -> None:
    print(_FOREST_TOP)
    print(_pedestal_state(w))
    print(_SYMBOL)


def _pray(w: World) -> None:
    if w.get_global("BOWL-TRANSFORMED"):
        print(_PRAY_DONE)
    else:
        print(_PRAY_PLACED if _bowl_placed(w) else _PRAY_BROKEN)


def _offer(w: World) -> None:
    zenni = w.globals.get("zenni", 0)
    if zenni < 1:
        print(_NO_COIN)
        return
    w.globals["zenni"] = zenni - 1             # an offering — it's gone
    if not _bowl_placed(w) or w.get_global("BOWL-TRANSFORMED"):
        print(_JUST_A_COIN)
        return
    from content import quests
    print(_TRANSFORMED)
    w.set_global("BOWL-TRANSFORMED", True)
    w.move_object(w.objects["REPAIRED-BOWL"], None)
    w.move_object(w.objects["CRYSTAL-BOWL"], w.here)   # NDESCBIT: the pedestal line covers it
    quests.complete(w, "49")


def forest_beg(w: World) -> int:
    """Forest M-BEG: the pedestal, the Zenni offering, taking the Crystal Bowl."""
    zenni, pedestal = w.objects["SHRINE-ZENNI"], w.objects["SHRINE-PEDESTAL"]
    bowl, crystal = w.objects["REPAIRED-BOWL"], w.objects["CRYSTAL-BOWL"]
    put = w.prsa in ("V-PUT-ON", "V-PUT-IN")   # IN or ON: the player means the same
    if w.prsa == "V-PRAY":
        _pray(w)
        return M_HANDLED
    if w.prsa == "V-EXAMINE" and w.prso is pedestal:
        print(_PEDESTAL)
        print(_pedestal_state(w))
        return M_HANDLED
    if w.prso is zenni and (w.prsa in ("V-GIVE", "V-DROP")
                            or (put and (w.prsi is pedestal
                                         or (w.prsi is bowl and _bowl_placed(w))))):
        _offer(w)
        return M_HANDLED
    if put and w.prso is bowl and w.prsi is pedestal:
        if _bowl_placed(w):
            print(_ALREADY_PLACED)
            return M_HANDLED
        if bowl not in w.player.contents:
            return M_NOT_HANDLED
        print(_BOWL_PLACED)
        w.set_global("BOWL-ON-PEDESTAL", True)
        w.move_object(bowl, w.here)
        bowl.set_flag("NDESCBIT")
        bowl.set_flag("TRYTAKEBIT")           # no implicit "(Taken)" off the pedestal
        return M_HANDLED
    if w.prsa == "V-TAKE" and w.prso is crystal and crystal.location is w.here:
        crystal.clear_flag("NDESCBIT")        # an ordinary item from here on
        return M_NOT_HANDLED
    if w.prsa == "V-TAKE" and w.prso is bowl and bowl.location is w.here:
        bowl.clear_flag("NDESCBIT")
        bowl.clear_flag("TRYTAKEBIT")
        w.set_global("BOWL-ON-PEDESTAL", False)
        return M_NOT_HANDLED
    return M_NOT_HANDLED


def offer_input_hook(w: World, text: str) -> bool:
    """Bare OFFER / DONATE at the forest shrine: one Zenni. Elsewhere the parser
    answers as before."""
    if w.here is None or w.here.name != "ROUNDABOUT-FOREST":
        return False
    if text.lower().split() not in (["offer"], ["donate"]):
        return False
    _offer(w)
    return True


def plinth_action(w: World) -> int:
    """The Shrine Room plinth: PUT BOWL IN DEPRESSION / ON PLINTH points home."""
    if w.prsa in ("V-PUT-ON", "V-PUT-IN") and w.prsi is w.objects["SHRINE-PLINTH"] \
            and w.prso is w.objects["REPAIRED-BOWL"] and w.prso in w.player.contents:
        print(_NOT_THIS_SHRINE)
        return M_HANDLED
    return M_NOT_HANDLED
