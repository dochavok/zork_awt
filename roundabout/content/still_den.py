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
- Still Den: no combat round on the entry turn; every later turn there while
  the werewolf lives is one round (it rolls 3d10 against the player; the
  player takes 1 heart on a loss, the werewolf never takes damage).
  DRIVE STAKE INTO WEREWOLF with the consecrated stake kills it outright; the
  stake stays in the body and the amulet drops.
- Deferred: Lower Crossing north (Tool Alcove) and south (Dark Room) and the
  50/50 pull-back text; the Ivory Torch (Quest 34).

State: BONES-CLEARED, DEN-JUST-ENTERED, WEREWOLF-DEAD
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

WEREWOLF_DICE = (3, 10)

_BONES = (
    "A low chamber, its floor carpeted wall to wall in dry bones — not scattered, "
    "laid, every one of them placed. Doorways lead east and south; the way you "
    "came is west."
)
_PATH = "A narrow path of bare stone runs through the bones, east to west."
_GRINDING = (
    "The sound is coming from beyond that doorway — bone grinding on stone, "
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
    "marks of tools long since abandoned. Three directions offer themselves "
    "without comment. The floor is grit and old dust."
)
_NARROW_PASS = (
    "A long passage, barely wide enough for your shoulders. The walls are close "
    "and the ceiling drops as you move east. Somewhere ahead, something breathes "
    "— slow and irregular, like sleep that isn't quite sleep."
)

_DEN = (
    "A wide cave, low but not cramped. The walls are gouged at every height — "
    "long parallel marks, overlapping, years of them. The floor is worn smooth in "
    "a rough oval, the path of something that has been pacing this space for "
    "longer than it can remember."
)
_DEN_ALIVE = " It is very still right now. That changes the moment you enter."
_DEN_AFTER = " The scholar lies where the creature fell."
_RISES = (
    "At the far end of the oval, something unfolds from the floor — taller than a "
    "man, long in the arm, its fur gone grey and patchy over skin that hasn't been "
    "alive in years. It turns its head toward you and starts forward."
)
_CLAWS = "The werewolf's claws find you."
_STAKE_HOME = (
    "You get inside its reach and drive the stake home. The sheen along the "
    "silver flares white."
)
_REVERTS = (
    "The creature drops. Between one moment and the next, it is not the creature "
    "anymore. The scholar lies on the floor of the cave he came down here to find."
)
_MELEE_FAILS = (
    "Your blade finds its mark. The creature doesn't notice. It turns toward you "
    "with the patience of something that has been waiting a very long time."
)
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

def den_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    dead = w.get_global("WEREWOLF-DEAD")
    if msg == M_LOOK:
        print(_DEN + (_DEN_AFTER if dead else _DEN_ALIVE))
        return M_HANDLED
    if msg == M_ENTER and not dead:
        w.set_global("DEN-JUST-ENTERED", True)
    elif msg == M_END and not dead and not w.get_global("GAME-OVER"):
        if w.get_global("DEN-JUST-ENTERED"):
            w.set_global("DEN-JUST-ENTERED", False)
            print(_RISES)              # no round on the entry turn
        else:
            _werewolf_round(w)
    return M_NOT_HANDLED


def _werewolf_round(w: World) -> None:
    from content.player import roll
    from content.combat import _take_damage
    mine = roll(w)
    its = sum(random.randint(1, WEREWOLF_DICE[1]) for _ in range(WEREWOLF_DICE[0]))
    if its > mine:
        print(_CLAWS)
        _take_damage(w, 1)


def drive_stake(w: World) -> bool:
    """DRIVE STAKE [INTO WEREWOLF]. True if handled here."""
    werewolf = w.objects["WEREWOLF"]
    stake = w.objects["SILVER-STAKE"]
    if w.prso is not stake or werewolf.location is not w.here \
            or w.prsi not in (None, werewolf):
        return False
    if not w.get_global("STAKE-CONSECRATED"):
        print(_PLAIN_STAKE)
        return True
    from content.combat import award_combat_xp
    print(_STAKE_HOME)
    print(_REVERTS)
    w.set_global("WEREWOLF-DEAD", True)
    w.move_object(stake, None)                       # stays in the body
    w.move_object(werewolf, None)
    w.move_object(w.objects["SCHOLAR"], w.here)
    w.move_object(w.objects["WEREWOLFS-AMULET"], w.here)
    award_combat_xp(w, "werewolf")
    return True


def melee(w: World) -> None:
    """KILL / ATTACK WEREWOLF: conventional weapons do nothing."""
    print(_MELEE_FAILS)


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
    narrow = room("NARROW-PASS", "The Narrow Pass", _NARROW_PASS)
    den = room("STILL-DEN", "The Still Den", "")

    world.rooms["PILE-OF-RUBBLE"].exits["east"] = Exit(destination="ANTECHAMBER")
    ante.exits.update(west=Exit(destination="PILE-OF-RUBBLE"),
                      east=_BoneExit(destination="LOWER-CROSSING"),
                      south=_SkeletonRoom(destination=None))
    # Lower Crossing north (Tool Alcove) and south (Dark Room) are deferred
    crossing.exits.update(west=Exit(destination="ANTECHAMBER"), east=Exit(destination="NARROW-PASS"))
    narrow.exits.update(west=Exit(destination="LOWER-CROSSING"), east=Exit(destination="STILL-DEN"))
    den.exits.update(west=Exit(destination="NARROW-PASS"))

    ante.action = antechamber_action
    den.action = den_action
