"""
Dungeon lower tier, east branch: Antechamber (Trap 36) → The Lower Crossing →
The Narrow Pass → The Still Den (the undead werewolf).

Design: locations.md (Antechamber, Skeleton Room, The Lower Crossing, The
Narrow Pass, The Still Den), traps.md (Trap 36), mechanics.md (Undead Werewolf
Chain), items.md (Werewolf's Amulet), experience.md (Trap 36: 3 XP; werewolf:
15 XP).

- Antechamber: CLEAR BONES disarms Trap 36. EAST or SOUTH before clearing is
  death; WEST is always safe. SOUTH after clearing is the Skeleton Room —
  death on entry.
- Still Den: three descriptions — first visit, werewolf up (every LOOK and
  every entry once it has risen, BRIEF or not), dead. It rises once, on the
  first entry. No combat round on an entry turn; every later turn there while
  the werewolf lives is one round (it rolls 3d20 against the player; the
  player takes 1 heart on a loss, a won round gets a miss line, the werewolf
  never takes damage).
  DRIVE STAKE INTO WEREWOLF with the consecrated stake kills it outright; the
  stake stays in the body and the amulet drops.
- The Ivory Torch hangs on the Still Den wall (Quest 34); it's heat, not light.
- Lower Crossing north is the Tool Alcove (content/tool_alcove.py).
- Lower Crossing south (Dark Room) is wired in content/dark_branch.py.

State: BONES-CLEARED, DEN-JUST-ENTERED, WEREWOLF-RISEN, WEREWOLF-DEAD
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END, M_BEG
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

WEREWOLF_DICE = (3, 20)   # raised from 3d10 2026-10-12: it barely landed past Level 4

_BONES = (
    "A low chamber, its floor carpeted wall to wall in dry bones — not scattered, "
    "laid, every one of them placed. Doorways lead east and south, and the rubble "
    "lies to the west."
)
_PATH = (
    "A low chamber, its floor carpeted wall to wall in dry bones — except for a "
    "narrow path of bare stone that now runs through them, east to west. Doorways "
    "lead east and south, and the rubble lies to the west."
)
_GRINDING = (
    "The sound is coming from beyond the south doorway — bone grinding on stone, "
    "steady and unhurried. You get the distinct impression that silence is not "
    "optional here."
)
_CLEARED = (
    "You crouch and work slowly, lifting the bones aside one at a time and "
    "setting each down without a sound, until a narrow path of bare stone runs "
    "across the room. Beyond the south doorway, the grinding goes on, unbothered."
)
_ALREADY_CLEAR = "The path is already clear."
_BONES_CRACK = "The bones crack underfoot. The grinding stops. Then the doorway fills."
_SKELETONS = (
    "You step through and the grinding stops. For one long breath nothing moves. "
    "Then all of them move — from the walls, from the floor, from the dark at the "
    "back where there were more than you thought. Bony hands find your arms, your "
    "coat, your throat. You go down under the weight of them and do not get up."
)

_CROSSING = (
    "The passage widens here into a rough crossing, the stone walls bearing the "
    "marks of tools long since abandoned. The floor is grit and old dust. Three "
    "ways lead on from here, none of them encouraging. North, a short passage "
    "ends in a cramped alcove. East, the walls close in toward a long, narrow "
    "pass. South, the dark is thicker than it has any right to be. The "
    "bone-strewn antechamber is back to the west."
)
_NARROW_PASS = (
    "A long passage, barely wide enough for your shoulders. The walls are close "
    "and the ceiling drops toward the east. Somewhere that way, something breathes "
    "— slow and irregular, like sleep that isn't quite sleep. The crossing is back "
    "to the west."
)
_NARROW_PASS_QUIET = (
    "A long passage, barely wide enough for your shoulders. The walls are close "
    "and the ceiling drops toward the east, where the den lies quiet now. The "
    "crossing is back to the west."
)

_DEN = (
    "A wide cave, low but not cramped. The walls are gouged at every height — "
    "long parallel marks, overlapping, years of them. The floor is worn smooth in "
    "a rough oval, the path of something that has been pacing this space for "
    "longer than it can remember."
)
_DEN_ALIVE = (" Something lies curled at the far end of the oval, grey and motionless. "
              "That changes the moment you enter.")
_DEN_UP = (
    "A wide cave, low but not cramped, the walls gouged at every height. The werewolf "
    "paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive "
    "in years. It hasn't taken its eyes off you. The narrow pass is back to the west."
)
_DEN_AFTER = (" Nothing paces it now. The scholar lies where the creature fell, the stake still "
              "in him. The narrow pass is back to the west.")
_RISES = (
    "The grey shape unfolds from the floor: a werewolf, taller than a man, long in the "
    "arm, its fur gone patchy over skin that hasn't been alive in years. It turns its "
    "head toward you and starts forward."
)
_CLAWS = "The werewolf's claws find you."
# A round the player wins, in turn (locations.md — The Still Den)
_MISSES = (
    "The werewolf lunges. You get clear — barely.",
    "Claws rake the air where you were standing a moment ago.",
    "It circles, feints, and comes in fast. You're not where it expected.",
    "The werewolf's swipe catches nothing but the edge of your sleeve.",
)
_STAKE_HOME = (
    "You get inside its reach and drive the stake home. The sheen along the "
    "silver flares white."
)
_REVERTS = (
    "The creature drops. Between one moment and the next, it is not the creature "
    "anymore. The scholar lies on the floor of the cave he came down here to find."
)
# The amulet's fall, so the player knows it's there (approved 2026-10-11)
_AMULET_FALLS = (
    "Something slips loose from around his neck as he falls and comes to rest on "
    "the stone beside him: a tarnished amulet, a seven-pointed star on its face."
)
# mechanics.md — Undead Werewolf, weapon failure messages
FIREBALL_FAILS = (
    "The fire takes hold for a moment — then dies. Whatever this creature is made of, "
    "it isn't interested in burning."
)
_MELEE_FAILS = (
    "Your {weapon} finds its mark. The creature doesn't notice. It turns toward you "
    "with the patience of something that has been waiting a very long time."
)
_STAKE_NUDGE = " The stake at your belt feels heavier."
# The stake after the kill: it stays in the scholar (decided 2026-10-13 / 10-14)
_STAKE_IN_HIM = (
    "It stands out of his chest, the silver gone dull. Whatever it was holding "
    "down, it's holding it still."
)
_DARE_NOT = "You dare not remove it."
_PLAIN_STAKE = (
    "The stake pierces flesh. The werewolf snarls — pain, but not the right kind. "
    "It pulls free and the wound closes. You need something more than silver."
)


def _game_over(w: World, text: str) -> None:
    print(text + "\n\n*** GAME OVER ***")
    w.set_global("GAME-OVER", True)
    w.game.quit()


# ---------------------------------------------------------------------------
# Antechamber (Trap 36)
# ---------------------------------------------------------------------------

def narrow_pass_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_NARROW_PASS_QUIET if w.get_global("WEREWOLF-DEAD") else _NARROW_PASS)
        return M_HANDLED
    return M_NOT_HANDLED


def antechamber_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_PATH if w.get_global("BONES-CLEARED") else _BONES)
        print(_GRINDING)
        return M_HANDLED
    return M_NOT_HANDLED


def clear_bones(w: World) -> None:
    if w.get_global("BONES-CLEARED"):
        print(_ALREADY_CLEAR)
        return
    from content.experience import award_xp
    print(_CLEARED)
    w.set_global("BONES-CLEARED", True)
    w.ways_changed("ANTECHAMBER")
    award_xp(w, 3 + (5 if w.globals.get("player_class") == "rogue" else 0))


class _BoneExit(Exit):
    """EAST/SOUTH out of the Antechamber: the bones crack unless cleared."""

    def resolve(self, world):
        if not world.get_global("BONES-CLEARED"):
            _game_over(world, _BONES_CRACK)
            return None, None
        return super().resolve(world)


class _SkeletonRoom(Exit):
    """SOUTH after clearing: the Skeleton Room — death on entry."""

    def resolve(self, world):
        if not world.get_global("BONES-CLEARED"):
            _game_over(world, _BONES_CRACK)
        else:
            _game_over(world, _SKELETONS)
        return None, None


# ---------------------------------------------------------------------------
# The Still Den
# ---------------------------------------------------------------------------

_STAKE_VERBS = ("V-USE", "V-PUT-IN", "V-PUT-ON", "V-PUSH")


def _stake_named(w: World) -> bool:
    """The stake, held, named against the werewolf by any verb but DRIVE:
    USE / PUT / PUSH STAKE IN(TO) WEREWOLF, ATTACK / STAB / KILL WEREWOLF WITH STAKE."""
    werewolf, stake = w.objects["WEREWOLF"], w.objects["SILVER-STAKE"]
    if werewolf.location is not w.here or stake not in w.player.contents:
        return False
    return ((w.prsa in _STAKE_VERBS and w.prso is stake and w.prsi is werewolf)
            or (w.prsa == "V-MELEE" and w.prso is werewolf and w.prsi is stake))


def _stake_in_scholar(w: World) -> int:
    """After the kill the stake stays in him: EXAMINE answers, TAKE / PULL refuse."""
    stake = w.objects["SILVER-STAKE"]
    if w.prso is not stake or stake.location is not w.here:
        return M_NOT_HANDLED
    if w.prsa == "V-EXAMINE":
        print(_STAKE_IN_HIM)
        return M_HANDLED
    if w.prsa in ("V-TAKE", "V-PULL", "V-MOVE"):
        print(_DARE_NOT)
        return M_HANDLED
    return M_NOT_HANDLED


def den_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    dead = w.get_global("WEREWOLF-DEAD")
    risen = w.get_global("WEREWOLF-RISEN")
    if msg == M_BEG:
        if dead:
            return _stake_in_scholar(w)
        if _stake_named(w):
            _stake_home(w)
            return M_HANDLED
        return M_NOT_HANDLED
    if msg == M_LOOK:
        if dead:
            print(_DEN + _DEN_AFTER)
        elif risen:
            print(_DEN_UP)
        else:
            print(_DEN + _DEN_ALIVE)
        return M_HANDLED
    if msg == M_ENTER and not dead:
        w.set_global("DEN-JUST-ENTERED", True)
        if risen:
            w.rooms["STILL-DEN"].visited = False   # its full description on every entry
    elif msg == M_END and not dead and not w.get_global("GAME-OVER"):
        if w.get_global("DEN-JUST-ENTERED"):
            w.set_global("DEN-JUST-ENTERED", False)
            if not risen:              # no round on the entry turn
                print(_RISES)
                w.set_global("WEREWOLF-RISEN", True)
        else:
            _werewolf_round(w)
    return M_NOT_HANDLED


def _werewolf_round(w: World) -> None:
    from content import combat
    n = int(w.get_global("WEREWOLF-MISSES") or 0)
    if not combat.defend(w, WEREWOLF_DICE, _CLAWS):   # bonuses count; only the stake harms it
        print(_MISSES[n % len(_MISSES)])
        w.set_global("WEREWOLF-MISSES", n + 1)


def drive_stake(w: World) -> bool:
    """DRIVE STAKE [INTO WEREWOLF]. True if handled here."""
    werewolf = w.objects["WEREWOLF"]
    stake = w.objects["SILVER-STAKE"]
    if w.prso is not stake or werewolf.location is not w.here \
            or w.prsi not in (None, werewolf):
        return False
    _stake_home(w)
    return True


def _stake_home(w: World) -> None:
    """The stake into the werewolf, however it was phrased."""
    werewolf = w.objects["WEREWOLF"]
    stake = w.objects["SILVER-STAKE"]
    if not w.get_global("STAKE-CONSECRATED"):
        print(_PLAIN_STAKE)
        return
    from content.combat import award_combat_xp
    print(_STAKE_HOME)
    print(_REVERTS)
    print(_AMULET_FALLS)
    w.set_global("WEREWOLF-DEAD", True)
    w.move_object(stake, w.here)                     # stays in the body
    stake.set_flag("NDESCBIT")                       # the room text says so
    stake.set_flag("TRYTAKEBIT")                     # no implicit "(Taken)"
    w.move_object(werewolf, None)
    w.move_object(w.objects["SCHOLAR"], w.here)
    w.move_object(w.objects["WEREWOLFS-AMULET"], w.here)
    award_combat_xp(w, "werewolf")
    from content import quests                       # the chain ends here
    quests.complete(w, "19")
    quests.complete(w, "30")


def stake_input_hook(w: World, text: str):
    """STAKE [THE] WEREWOLF: "stake" is a noun to the parser, so this is the
    same turn as DRIVE STAKE INTO WEREWOLF."""
    if text.lower().split() not in (["stake", "werewolf"], ["stake", "the", "werewolf"]):
        return False
    if w.here is None or w.here.name != "STILL-DEN" \
            or w.objects["SILVER-STAKE"] not in w.player.contents:
        return False
    from engine.game import HOOK_NO_TURN
    w.game.do_turn("drive stake into werewolf")      # its own turn and round
    return HOOK_NO_TURN


_BOW_FAILS = (
    "The arrow strikes true and stays there. The werewolf looks at it briefly, "
    "then at you. It does not appear concerned."
)


def shot(w: World) -> None:
    """SHOOT WEREWOLF: the arrow does nothing; the turn's round still happens."""
    print(_BOW_FAILS)


def melee(w: World) -> None:
    """KILL / ATTACK WEREWOLF: conventional weapons do nothing. The line names
    what was used; carrying the stake but not using it, a nudge."""
    from content import combat
    weapon = w.prsi or combat.equipped(w)
    if weapon is not None and weapon.name == "BOW":
        weapon = None
    line = _MELEE_FAILS.format(weapon=weapon.desc if weapon is not None else "fist")
    if w.objects["SILVER-STAKE"] in w.player.contents:
        line += _STAKE_NUDGE
    print(line)


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=2)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    ante = room("ANTECHAMBER", "Antechamber", "")
    crossing = room("LOWER-CROSSING", "The Lower Crossing", _CROSSING)
    narrow = room("NARROW-PASS", "The Narrow Pass", "")   # narrow_pass_action: before / after the kill
    den = room("STILL-DEN", "The Still Den", "")

    world.rooms["PILE-OF-RUBBLE"].exits["east"] = Exit(destination="ANTECHAMBER")
    ante.exits.update(west=Exit(destination="PILE-OF-RUBBLE"),
                      east=_BoneExit(destination="LOWER-CROSSING"),
                      south=_SkeletonRoom(destination=None))
    # Lower Crossing north: content/tool_alcove.py. South (Dark Room) is deferred
    crossing.exits.update(west=Exit(destination="ANTECHAMBER"), east=Exit(destination="NARROW-PASS"))
    narrow.exits.update(west=Exit(destination="LOWER-CROSSING"), east=Exit(destination="STILL-DEN"))
    den.exits.update(west=Exit(destination="NARROW-PASS"))

    ante.action = antechamber_action
    narrow.action = narrow_pass_action
    den.action = den_action
