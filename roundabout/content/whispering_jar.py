"""
The Whispering Jar — Pipe Room, Tale and Ale (Quest 4).

Design: quests.md (Quest 4), items.md (The Whispering Jar, Wax Seal, Silver
Dust), mechanics.md (Whispering Jar).

- In order: PRESS SEAL (or PRESS / PUT SEAL ON JAR) seals the crack — the seal
  is used up and 5 Zenni turn up in the bottom of the jar. DUST JAR (or
  SPRINKLE / PUT DUST ON JAR) — the dust is used up. Dust before the seal is
  refused.
- READ INSCRIPTION / LETTERS / ETCHING / BASE / JAR: Medium perception check every time
  (glasses bonus / auto-pass apply). Before both steps the words do nothing;
  after them the jar whispers the thermal vent hint and Quest 4 completes.
  Reading again repeats the whisper.
- LISTEN: the hum before, quiet after.

State: JAR-SEALED, JAR-DUSTED, JAR-RESTORED
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG

if TYPE_CHECKING:
    from engine.world import World

_PRESS = (
    "You press the wax seal over the crack. The wax gives, then takes — it spreads "
    "along the line of the crack and sets, red against the blue-grey glaze. The hum "
    "steadies."
)
_COINS = (
    "Something clinks inside the jar. Five Zenni sit in the bottom, kept there by the "
    "crack until now. You pocket them."
)
_DUST_FIRST = "The dust would only sift into the crack."
_DUST = (
    "You sprinkle the silver dust over the jar. It clings to the glaze and settles into "
    "the etched letters around the base, and for a moment the whole jar glints."
)
_WORN = "The letters are worn almost smooth. You can't make them out."
_UNCHANGED = (
    "Around the base, worn almost smooth: \"Hold what was heard. Speak what was held.\" "
    "You say the words aloud. The jar hums on, unchanged."
)
_WHISPER = (
    "You read the words around the base aloud: \"Hold what was heard. Speak what was "
    "held.\" The hum rises, wavers, and stops. In the silence, a voice no louder than "
    "breath: \"The ceiling of the thermal vent holds a secret.\" Then nothing."
)
_HUM = "A low, steady hum. Up close, it almost sounds like a voice holding a single note."
_QUIET = "Nothing. The jar is quiet now."
_MENDED = "A mended ceramic jar sits on the side table, quiet."
_MENDED_EXAMINE = (
    "A ceramic jar, glazed blue-grey, its crack sealed with red wax. A fine silver "
    "shimmer clings to the letters around its base. It doesn't hum any more."
)
_NO_JAR_SEAL = "There's nothing here to press it on."
_NO_JAR_DUST = "There's nothing here worth dusting."
_NOTHING_TO_DUST = "You have nothing to dust it with."


def _held(w: World, name: str) -> bool:
    return w.player is not None and w.objects[name] in w.player.contents


def _press(w: World) -> None:
    from content import quests
    w.move_object(w.objects["WAX-SEAL"], None)
    w.set_global("JAR-SEALED", True)
    quests.discover(w, "4")
    print(_PRESS)
    w.globals["zenni"] = w.globals.get("zenni", 0) + 5
    print(_COINS)


def _dust(w: World) -> None:
    if not w.get_global("JAR-SEALED"):
        print(_DUST_FIRST)
        return
    w.move_object(w.objects["SILVER-DUST"], None)
    w.set_global("JAR-DUSTED", True)
    print(_DUST)


def _read(w: World) -> None:
    from content import quests
    from content.perception import MEDIUM
    from content.player import check_perception
    if not check_perception(w, MEDIUM):
        print(_WORN)
        return
    if not (w.get_global("JAR-SEALED") and w.get_global("JAR-DUSTED")):
        print(_UNCHANGED)
        return
    print(_WHISPER)
    if not w.get_global("JAR-RESTORED"):
        w.set_global("JAR-RESTORED", True)
        jar = w.objects["WHISPERING-JAR"]
        jar.fdesc = _MENDED
        jar.ldesc = _MENDED
        jar.examine = _MENDED_EXAMINE
        quests.complete(w, "4", zenni_override=0)   # the 5 Zenni came with the seal


def pipe_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg != M_BEG:
        return M_NOT_HANDLED
    jar = w.objects["WHISPERING-JAR"]
    seal, dust = w.objects["WAX-SEAL"], w.objects["SILVER-DUST"]
    prsa, prso, prsi = w.prsa, w.prso, w.prsi
    if prsi not in (None, jar):
        return M_NOT_HANDLED
    if prsa in ("V-PUSH", "V-PUT-ON") and prso is seal and _held(w, "WAX-SEAL"):
        _press(w)
        return M_HANDLED
    if _held(w, "SILVER-DUST") and ((prsa == "V-DUST" and prso is jar)
                                    or (prsa == "V-PUT-ON" and prso is dust)):
        _dust(w)
        return M_HANDLED
    if prsa == "V-DUST" and prso is jar:
        print(_NOTHING_TO_DUST)
        return M_HANDLED
    if prsa == "V-READ" and prso is jar:
        _read(w)
        return M_HANDLED
    if prsa == "V-LISTEN" and prso in (None, jar):
        print(_QUIET if w.get_global("JAR-RESTORED") else _HUM)
        return M_HANDLED
    return M_NOT_HANDLED


def v_dust(w: World) -> int:
    """DUST anywhere else."""
    print(_NO_JAR_DUST)
    return M_HANDLED


def v_push(w: World) -> int:
    """PRESS SEAL away from the jar; other pushes get the default line."""
    if w.prso is not None and w.prso.name == "WAX-SEAL":
        print(_NO_JAR_SEAL)
        return M_HANDLED
    from content.verbs import v_move
    return v_move(w)


def make_rooms(world) -> None:
    world.rooms["PIPE-ROOM"].action = pipe_room_action
