"""
Dungeon middle tier, key side south of the Mine Passage: Inscription Chamber,
Cave Creature's Lair, Echo Alcove, Magnetic Vault, Deep Lock Door.

Design: locations.md (those rooms), traps.md (Trap 8 Rope Snare, Trap 15
Magnetic Chest), quests.md (Quests 7, 28, 42), items.md (Rubbing, Bone Flute,
Diamond Brooch), experience.md (Trap Disarmament XP).

- Inscription Chamber: Medium perception each visit for the dungeon rune stone
  and for the snare (Trap 8). Spotting the snare reveals the crawlspace (east,
  Cave Creature's Lair) and the player steps around it (3 XP, Rogue +5). A
  failed check fires the snare on entry: the player hangs upside down — only
  LOOK / INVENTORY work until PULL FREE / STRUGGLE (Medium strength, retry) or
  CUT CORD with a blade. Firing it also reveals the crawlspace.
- RUB PAPER ON ENGRAVING: thin paper + charcoal → rubbing (both used up).
- Magnetic Vault: Medium perception spots the filings. DISARM LODESTONE (Medium
  trap disarm, retry) → 4 XP, Rogue +5. OPEN CHEST undisarmed fires the pulse
  once: carried iron items stick to the chest; TAKE / PULL each is a Medium
  strength check.
- Deep Lock Door: sealed dead end.

State: INSCRIPTION-SNARE-SPOTTED, SNARE-FIRED, SNARE-HANGING, CRAWLSPACE-FOUND,
       VAULT-SPOTTED, LODESTONE-STATE (None / "removed" / "fired"),
       VAULT-CHEST-OPEN, MAGNET-STUCK (list of object names)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK, M_ENTER
from engine.world import Room, Exit, RLANDBIT, OPENBIT, NDESCBIT

if TYPE_CHECKING:
    from engine.world import World

# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

_CHAMBER = (
    "A cave room, wider than the passage leading to it. One wall has been worked "
    "— smoothed and carved with an inscription, old enough that the edges have "
    "softened. The other walls are natural stone, unmodified."
)
_CRAWLSPACE = (
    "A low gap in the east wall, partly shadowed — easy to miss. It goes back "
    "further than it looks."
)
_SNARE_SPOTTED = (
    "A loop of fine cord lies half-buried in the dirt in front of the gap — a "
    "snare, set and waiting."
)
_SNARE_SNAPPED = "A snapped cord dangles from a hook in the ceiling."
_SNARE_FIRES = (
    "Your foot comes down on something that gives. A cord snaps tight around your "
    "ankle and the floor drops away — you're yanked off your feet and left "
    "swinging upside down from a hook in the ceiling. From down here the room "
    "looks different: there's a low gap in the east wall you hadn't noticed."
)
_HANGING = "You're hanging upside down by one ankle. That needs dealing with first."
_STRUGGLE_FAIL = "You twist and strain, but the cord holds. You swing gently, upside down."
_STRUGGLE_OK = (
    "You haul yourself up, get a hand to the knot and work your ankle free. You "
    "drop to the dirt in an undignified heap."
)
_CUT_FREE = "You saw through the cord and drop to the dirt in a heap."
_NO_BLADE = "You've nothing to cut it with."

_RUBBED = (
    "You press the thin paper flat against the carved wall and work the charcoal "
    "across it. The inscription comes up pale against the black, line by line. You "
    "peel the rubbing away carefully. The charcoal is worn down to nothing."
)
_NO_CHARCOAL = "You'd need something to rub with — charcoal, maybe."
_NO_PAPER = "You'd need something to take the rubbing on."
_ALREADY_RUBBED = "You've already got a rubbing of it."

_LAIR = (
    "A low, rank-smelling hollow at the end of the crawlspace. The floor is matted "
    "with old bedding — grass, fur, things that were once other things — and "
    "gnawed bones are pushed against the walls. Whatever lives here isn't home. It "
    "hasn't been for a while, or it's only just left."
)
_ECHO = (
    "A shallow alcove, barely deeper than it is wide, the rock curved like the "
    "inside of a shell. Your own breathing comes back to you a beat late. A faint "
    "grinding drifts up from somewhere far below — bone on stone. The passage runs "
    "north and south."
)
_VAULT = (
    "A square room, stone walls, a single chest at the center on a low stone "
    "platform. The room feels subtly wrong in a way that takes a moment to "
    "identify — small metal objects have drifted toward the chest, as if drawn."
)
_VAULT_DEFAULT = "A nail in the wall points toward it. Dust has settled in a faint ring around the latch."
_VAULT_SPOTTED = (
    "A nail in the wall points toward it. The ring of metallic filings around the "
    "latch is deliberate — a lodestone is built into the lid. Opening the chest "
    "without removing it first would be a problem."
)
_NOTHING_TO_DISARM = "You don't see anything to disarm."
_NOTHING_LEFT = "There's nothing left to disarm."
_LODESTONE_OUT = (
    "You slide a hand under the lid's lip, find the lodestone and work it loose. "
    "The filings slump out of their ring. The chest is just a chest now."
)
_LODESTONE_STUCK = "The lodestone is set fast. You can't get it loose — not this time."
_CHEST_OPENS = "The lid lifts easily. Inside, on a fold of black cloth, lies a diamond brooch."
_STUCK_LINE = "Stuck fast to the side of the chest: {items}."
_BROOCH_IN_CHEST = "In the open chest lies a diamond brooch."
_CHEST_ALREADY = "The chest is already open."
_PULSE = (
    "The lid comes up an inch and the air goes tight. Everything iron you're "
    "carrying wrenches toward the chest and slams against it: {items}. They're "
    "stuck fast."
)
_PULSE_NOTHING = (
    "The lid comes up an inch and the air goes tight — then eases. Nothing you're "
    "carrying answers to it."
)
_DEEP_LOCK = (
    "The passage ends at a door set deep into the stone. It is sealed absolutely — "
    "no lock visible, no handle, no gap at the frame. Whatever mechanism holds it "
    "closed is on the other side, or nowhere. This door does not open. The passage "
    "ends here."
)
_DOOR_SHUT = "This door does not open."

# Iron and steel only (items.md — Trap 15)
MAGNETIC = (
    "LOCKPICKS", "CROWBAR", "PICKAXE", "SHOVEL", "FLINT-AND-STEEL", "KEY-RING",
    "MIDDLE-TIER-KEY", "CELLAR-KEY", "PORTCULLIS-BAR", "PALE-BLADE",
)
_BLADES = ("PALE-BLADE",)
_FREE_ACTIONS = ("V-LOOK", "V-INVENTORY", "V-SCORE", "V-SAVE", "V-RESTORE", "V-QUIT")


def _rogue_xp(w: World, base: int) -> None:
    from content.experience import award_xp
    award_xp(w, base + (5 if w.globals.get("player_class") == "rogue" else 0))


def _carried(w: World, name: str) -> bool:
    return w.objects[name] in w.player.contents


# ---------------------------------------------------------------------------
# Inscription Chamber — Trap 8 and the rubbing
# ---------------------------------------------------------------------------

def chamber_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        from content.perception import MEDIUM, reveal_if_found
        from content.player import check_perception
        reveal_if_found(w, "DUNGEON-RUNE-STONE", MEDIUM)
        if not w.get_global("CRAWLSPACE-FOUND"):
            if check_perception(w, MEDIUM):
                w.set_global("INSCRIPTION-SNARE-SPOTTED", True)
                w.set_global("CRAWLSPACE-FOUND", True)
                _rogue_xp(w, 3)
            else:
                w.set_global("SNARE-PENDING", True)   # fires after the description
        return M_NOT_HANDLED
    if msg == M_LOOK:
        print(_CHAMBER)
        if w.get_global("CRAWLSPACE-FOUND"):
            print(_CRAWLSPACE)
        if w.get_global("INSCRIPTION-SNARE-SPOTTED"):
            print(_SNARE_SPOTTED)
        elif w.get_global("SNARE-FIRED") and not w.get_global("SNARE-HANGING"):
            print(_SNARE_SNAPPED)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    if w.get_global("SNARE-HANGING"):
        return _hanging_turn(w)
    if w.prsa == "V-RUB" and w.objects["ENGRAVING"] in (w.prso, w.prsi):
        _rub(w)
        return M_HANDLED
    return M_NOT_HANDLED


def on_enter(w: World, room) -> None:
    """Trap 8 fires after the room description when the snare wasn't spotted."""
    if room.name != "INSCRIPTION-CHAMBER" or not w.get_global("SNARE-PENDING"):
        return
    w.set_global("SNARE-PENDING", False)
    w.set_global("SNARE-FIRED", True)
    w.set_global("SNARE-HANGING", True)
    w.set_global("CRAWLSPACE-FOUND", True)
    print(_SNARE_FIRES)


def _hanging_turn(w: World) -> int:
    if w.prsa in _FREE_ACTIONS:
        return M_NOT_HANDLED
    if w.prsa == "V-STRUGGLE":
        from content.perception import MEDIUM
        from content.player import check_strength
        if check_strength(w, MEDIUM):
            print(_STRUGGLE_OK)
            w.set_global("SNARE-HANGING", False)
        else:
            print(_STRUGGLE_FAIL)
        return M_HANDLED
    if w.prsa == "V-CUT" and w.prso is w.objects["SNARE"]:
        blade = w.prsi if w.prsi is not None and w.prsi.name in _BLADES else next(
            (w.objects[b] for b in _BLADES if _carried(w, b)), None)
        if blade is None or not _carried(w, blade.name):
            print(_NO_BLADE)
        else:
            print(_CUT_FREE)
            w.set_global("SNARE-HANGING", False)
        return M_HANDLED
    print(_HANGING)
    return M_HANDLED


def _rub(w: World) -> None:
    if _carried(w, "RUBBING"):
        print(_ALREADY_RUBBED)
    elif not _carried(w, "THIN-PAPER"):
        print(_NO_PAPER)
    elif not _carried(w, "CHARCOAL"):
        print(_NO_CHARCOAL)
    else:
        print(_RUBBED)
        w.move_object(w.objects["THIN-PAPER"], None)
        w.move_object(w.objects["CHARCOAL"], None)
        rubbing = w.objects["RUBBING"]
        w.move_object(rubbing, w.player)
        rubbing.touched = True


class _CrawlspaceExit(Exit):
    def resolve(self, world):
        if not world.get_global("CRAWLSPACE-FOUND"):
            return None, "You can't go that way."
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Magnetic Vault — Trap 15
# ---------------------------------------------------------------------------

def vault_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        if not w.get_global("VAULT-SPOTTED") and w.get_global("LODESTONE-STATE") is None:
            from content.perception import MEDIUM
            from content.player import check_perception
            if check_perception(w, MEDIUM):
                w.set_global("VAULT-SPOTTED", True)
        return M_NOT_HANDLED
    if msg == M_LOOK:
        spotted = w.get_global("VAULT-SPOTTED") and w.get_global("LODESTONE-STATE") is None
        print(_VAULT + " " + (_VAULT_SPOTTED if spotted else _VAULT_DEFAULT))
        # The chest is a fixture (never listed itself), so its contents are shown here
        brooch = w.objects["DIAMOND-BROOCH"]
        if w.get_global("VAULT-CHEST-OPEN") and brooch.location is w.objects["VAULT-CHEST"]:
            print(_BROOCH_IN_CHEST)
        stuck = w.globals.get("MAGNET-STUCK") or []
        if stuck:
            print(_STUCK_LINE.format(items=_list(w.objects[n].desc for n in stuck)))
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    chest, lodestone = w.objects["VAULT-CHEST"], w.objects["LODESTONE"]
    if w.prsa == "V-DISARM" or (w.prsa in ("V-REMOVE", "V-TAKE") and w.prso is lodestone):
        _disarm(w)
        return M_HANDLED
    if w.prsa in ("V-OPEN", "V-UNLOCK") and w.prso is chest:
        _open_chest(w)
        return M_HANDLED
    stuck = w.globals.get("MAGNET-STUCK") or []
    if w.prsa in ("V-TAKE", "V-PULL") and w.prso is not None and w.prso.name in stuck:
        _pry(w, w.prso)
        return M_HANDLED
    return M_NOT_HANDLED


def _disarm(w: World) -> None:
    state = w.get_global("LODESTONE-STATE")
    if state is not None:
        print(_NOTHING_LEFT)
    elif not w.get_global("VAULT-SPOTTED"):
        print(_NOTHING_TO_DISARM)
    else:
        from content.perception import MEDIUM
        from content.player import check_trap_disarm
        if check_trap_disarm(w, MEDIUM):
            print(_LODESTONE_OUT)
            w.set_global("LODESTONE-STATE", "removed")
            _rogue_xp(w, 4)
        else:
            print(_LODESTONE_STUCK)


def _open_chest(w: World) -> None:
    chest = w.objects["VAULT-CHEST"]
    if w.get_global("VAULT-CHEST-OPEN"):
        print(_CHEST_ALREADY)
        return
    w.set_global("VAULT-CHEST-OPEN", True)
    chest.set_flag(OPENBIT)
    if w.get_global("LODESTONE-STATE") is None:
        w.set_global("LODESTONE-STATE", "fired")
        iron = [w.objects[n] for n in MAGNETIC if _carried(w, n)]
        if not iron:
            print(_PULSE_NOTHING)
        else:
            for obj in iron:
                w.move_object(obj, w.here)
                obj.set_flag(NDESCBIT)      # listed by the room's stuck line
            w.globals["MAGNET-STUCK"] = [o.name for o in iron]
            print(_PULSE.format(items=_list(o.desc for o in iron)))
        return
    print(_CHEST_OPENS)


def _list(names) -> str:
    names = [f"the {n}" for n in names]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def _pry(w: World, obj) -> None:
    from content.perception import MEDIUM
    from content.player import check_strength
    if check_strength(w, MEDIUM):
        print(f"You wrench the {obj.desc} free.")
        w.move_object(obj, w.player)
        obj.clear_flag(NDESCBIT)
        w.globals["MAGNET-STUCK"] = [n for n in w.globals["MAGNET-STUCK"] if n != obj.name]
    else:
        print(f"The {obj.desc} won't budge.")


# ---------------------------------------------------------------------------
# Deep Lock Door
# ---------------------------------------------------------------------------

def deep_lock_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_BEG and w.prsa in ("V-OPEN", "V-UNLOCK", "V-PICK") and w.prso is w.objects["DEEP-LOCK"]:
        print(_DOOR_SHUT)
        return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    chamber = room("INSCRIPTION-CHAMBER", "Inscription Chamber", "")
    lair = room("CAVE-CREATURES-LAIR", "Cave Creature's Lair", _LAIR, value=2)
    echo = room("ECHO-ALCOVE", "Echo Alcove", _ECHO)
    vault = room("MAGNETIC-VAULT", "Magnetic Vault", "")
    deep = room("DEEP-LOCK-DOOR", "Deep Lock Door", _DEEP_LOCK)

    world.rooms["MINE-PASSAGE"].exits["south"] = Exit(destination="INSCRIPTION-CHAMBER")
    chamber.exits.update(north=Exit(destination="MINE-PASSAGE"),
                         east=_CrawlspaceExit(destination="CAVE-CREATURES-LAIR"),
                         south=Exit(destination="ECHO-ALCOVE"))
    lair.exits.update(west=Exit(destination="INSCRIPTION-CHAMBER"))
    echo.exits.update(north=Exit(destination="INSCRIPTION-CHAMBER"), south=Exit(destination="MAGNETIC-VAULT"))
    vault.exits.update(north=Exit(destination="ECHO-ALCOVE"), south=Exit(destination="DEEP-LOCK-DOOR"))
    deep.exits.update(north=Exit(destination="MAGNETIC-VAULT"))

    chamber.action = chamber_action
    vault.action = vault_action
    deep.action = deep_lock_action
