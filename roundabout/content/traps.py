"""
Trap mechanics for Roundabout: The God-Forsaken Ring.

Sourced from AWT_story_line/traps.md.

Each trap is wired as a room M_ENTER handler (or object interaction).
Trap flow:
  1. Perception check on room entry (silent).
  2. If perceived: player sees the trap and may disarm it.
  3. If not perceived (or player ignores it): trap fires.

Registration:
  register_traps(world) must be called from content/init.py after make_rooms().
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def register_traps(world: "World") -> None:
    """Wire all trap handlers onto their rooms as M_ENTER actions."""
    _wire(world, "lower-crypt",        _enter_lower_crypt)
    _wire(world, "inscription-chamber",_enter_inscription_chamber)
    _wire(world, "magnetic-vault",     _enter_magnetic_vault)
    _wire(world, "chuckle-house-entrance", _enter_chuckle_house)
    _wire(world, "supply-room",        _enter_supply_room)
    _wire(world, "portcullis-corridor",_enter_portcullis_corridor)
    _wire(world, "idol-room",          _enter_idol_room)
    _wire(world, "bone-passage",       _enter_bone_passage)
    _wire(world, "skeleton-room",      _enter_skeleton_room)
    _wire(world, "flooding-room",      _enter_flooding_room)
    _wire(world, "ink-corridor",       _enter_ink_corridor)
    _wire(world, "combat-room",        _enter_combat_room)


def _wire(world: "World", room_name: str, handler) -> None:
    room = world.rooms.get(room_name)
    if room is None:
        return
    # Engine expects room.enter_action to be a callable(world) -> int
    # Rooms may already have an enter action; chain if so.
    existing = getattr(room, "enter_action", None)
    if existing is not None:
        original = existing
        def chained(w, _orig=original, _new=handler):
            result = _new(w)
            if result == M_NOT_HANDLED:
                return _orig(w)
            return result
        room.enter_action = chained
    else:
        room.enter_action = handler


# ---------------------------------------------------------------------------
# Helpers shared across traps
# ---------------------------------------------------------------------------

def _damage(world: "World", hearts: int, source: str = "") -> None:
    from content.combat import _take_damage
    _take_damage(world, hearts)


def _perception_check(world: "World", difficulty: int) -> bool:
    from content.player import check_perception
    # Enchanted glasses auto-succeed on perception
    if world.globals.get("actually_enchanted_glasses_worn"):
        return True
    return check_perception(world, difficulty)


def _trap_seen(world: "World", trap_key: str) -> bool:
    return world.globals.get(f"trap_seen_{trap_key}", False)


def _trap_fired(world: "World", trap_key: str) -> bool:
    return world.globals.get(f"trap_fired_{trap_key}", False)


def _mark_seen(world: "World", trap_key: str) -> None:
    world.globals[f"trap_seen_{trap_key}"] = True


def _mark_fired(world: "World", trap_key: str) -> None:
    world.globals[f"trap_fired_{trap_key}"] = True


def _mark_disarmed(world: "World", trap_key: str) -> None:
    world.globals[f"trap_disarmed_{trap_key}"] = True


def _is_disarmed(world: "World", trap_key: str) -> bool:
    return world.globals.get(f"trap_disarmed_{trap_key}", False)


# ---------------------------------------------------------------------------
# Trap 5 -- Swinging Blade Pendulum (inert, atmospheric only)
# ---------------------------------------------------------------------------

def _enter_lower_crypt(world: "World") -> int:
    """Trap 5: atmospheric only -- blade has already fired. No mechanical effect."""
    if not world.globals.get("lower_crypt_entered"):
        world.globals["lower_crypt_entered"] = True
        print(
            "A massive blade hangs from the ceiling on a rusted chain, "
            "motionless. It has been motionless for a long time. "
            "The skeleton on the floor beneath it is not going anywhere. "
            "The pressure plate under its feet is still depressed."
        )
    return M_NOT_HANDLED  # let normal room desc run


# ---------------------------------------------------------------------------
# Trap 8 -- Rope Snare (Inscription Chamber)
# ---------------------------------------------------------------------------

def _enter_inscription_chamber(world: "World") -> int:
    """Trap 8: ankle snare in the crawlspace off the Inscription Chamber."""
    key = "rope_snare"

    if _is_disarmed(world, key) or _trap_fired(world, key):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        # Player was warned; still entering -- they chose to go in
        return M_NOT_HANDLED

    # Perception check (MEDIUM = 9)
    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "Your eye catches something -- a loop of fine cord, almost invisible "
            "against the dark soil. Someone laid a snare here, set at ankle height. "
            "The cord is attached to a hook in the ceiling. "
            "You step around it carefully."
        )
        # Reveal crawlspace exit
        _reveal_crawlspace(world)
        return M_NOT_HANDLED

    # Trap fires -- player snagged
    _mark_fired(world, key)
    world.globals["rope_snare_active"] = True
    world.globals["rope_snare_turns"] = 3  # turns trapped

    print(
        "Something catches your ankle. Before you can react, you're yanked off your feet -- "
        "the cord snaps taut and you swing upward, suspended by one ankle from a ceiling hook.\n\n"
        "The world is upside down. This is, objectively, a problem.\n\n"
        "You can CUT the rope (if you have something sharp) or attempt to PULL free."
    )
    # Reveal crawlspace even when trapped -- the violent swing reveals the entrance
    _reveal_crawlspace(world)

    # Register a per-turn daemon to count trapped turns
    _register_snare_daemon(world)
    return M_HANDLED


def _reveal_crawlspace(world: "World") -> None:
    if world.globals.get("crawlspace_revealed"):
        return
    world.globals["crawlspace_revealed"] = True
    # Unlock the hidden exit from inscription-chamber to cave-creature-lair
    room = world.rooms.get("inscription-chamber")
    if room and hasattr(room, "exits"):
        from engine.world import Exit
        room.exits["crawl"] = Exit(destination="cave-creature-lair")
        room.exits["crawlspace"] = Exit(destination="cave-creature-lair")


def _register_snare_daemon(world: "World") -> None:
    clock = world.game.clock
    if clock.get("rope-snare-daemon") is not None:
        return

    def _snare_tick(w: "World") -> bool:
        if not w.globals.get("rope_snare_active"):
            return False
        turns = w.globals.get("rope_snare_turns", 0)
        turns -= 1
        w.globals["rope_snare_turns"] = turns
        if turns <= 0:
            w.globals["rope_snare_active"] = False
            print(
                "The cord finally gives enough for you to haul yourself up "
                "and work the loop free. You drop to the floor, "
                "somewhat more cautious than you were before."
            )
            return False
        msgs = {
            2: "You are still upside down. This is not improving.",
            1: "Your face is quite red. One more turn and you may work free on your own.",
        }
        if turns in msgs:
            print(msgs[turns])
        event = w.game.clock.get("rope-snare-daemon")
        if event:
            event.ticks = 1
        return False

    clock.add_demon("rope-snare-daemon", _snare_tick)
    event = clock.get("rope-snare-daemon")
    if event:
        event.ticks = 1


# ---------------------------------------------------------------------------
# Trap 15 -- Magnetic Chest (Magnetic Vault)
# ---------------------------------------------------------------------------

def _enter_magnetic_vault(world: "World") -> int:
    """Trap 15: perception check reveals lodestone; opening chest without disarming pulls metal."""
    key = "magnetic_chest"

    if _is_disarmed(world, key) or _trap_fired(world, key):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        return M_NOT_HANDLED

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "You notice unusual metallic filings arranged in a precise ring "
            "around the chest's latch. There is also what appears to be a lodestone "
            "embedded in the lid's underside. This chest has been rigged. "
            "REMOVE the lodestone before opening it."
        )
    return M_NOT_HANDLED


def fire_magnetic_chest(world: "World") -> None:
    """Called when player opens the magnetic chest without disarming."""
    key = "magnetic_chest"
    if _is_disarmed(world, key) or _trap_fired(world, key):
        return

    _mark_fired(world, key)

    # Collect metal items from player inventory
    metal_items = _collect_metal_items(world)
    if not metal_items:
        print(
            "The chest lid swings open. A dull thrum fills the air. "
            "Something was supposed to happen -- "
            "but you're apparently not carrying anything that qualifies. "
            "Lucky."
        )
        return

    chest = world.objects.get("magnetic-chest")
    chest_room = world.rooms.get("magnetic-vault")

    print(
        "The chest lid swings open. A dull thrum fills the air -- and every metal object "
        "in your possession lurches toward the chest simultaneously.\n"
    )

    pulled = []
    for obj in metal_items:
        world.move_object(obj, chest_room)
        pulled.append(obj.desc or obj.name)

    print(
        f"The following items are yanked free and slam against the chest: "
        f"{', '.join(pulled)}.\n\n"
        "You can attempt to PRY each one loose (strength check required, one turn per item)."
    )
    world.globals["magnetic_items_stuck"] = [o.name for o in metal_items]


def _collect_metal_items(world: "World") -> list:
    metal_names = {
        "sword", "long-sword", "short-sword", "bow", "silver-stake",
        "consecrated-stake", "crowbar", "portcullis-bar", "shovel",
        "forgotten-blade", "key", "cellar-key", "mid-tier-key", "music-box-key",
        "keepers-keys", "lockpicks", "ivaanars-tunic",
    }
    result = []
    for obj in world.player_inventory():
        if obj.name in metal_names:
            result.append(obj)
    return result


# ---------------------------------------------------------------------------
# Trap 16 -- Mirror Shatter Trap (Chuckle House)
# ---------------------------------------------------------------------------

def _enter_chuckle_house(world: "World") -> int:
    """Trap 16: crossbow behind mirror fires once; perception disarms."""
    key = "mirror_trap"

    if _is_disarmed(world, key) or _trap_fired(world, key):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        return M_NOT_HANDLED

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "You spot it before you're all the way through the door: "
            "a thin firing pin visible at the edge of the mirror's frame, "
            "and the faint silhouette of a crossbow through the glass behind it. "
            "You carefully remove the pin. "
            "The crossbow, uncocked, becomes a piece of furniture."
        )
        _mark_disarmed(world, key)
        return M_NOT_HANDLED

    # Trap fires
    _mark_fired(world, key)
    print(
        "Something clicks as you step past the mirror. "
        "A bolt catches you across the shoulder -- not deep, but enough.\n\n"
        "The crossbow behind the glass is now spent. "
        "Whatever it was guarding, it's guarding less effectively now."
    )
    _damage(world, 1, "crossbow bolt")
    return M_NOT_HANDLED  # room description still runs


# ---------------------------------------------------------------------------
# Trap 17 -- Smoke Bomb Cache (Supply Room)
# ---------------------------------------------------------------------------

def _enter_supply_room(world: "World") -> int:
    """Trap 17: smoke jar hidden on unstable shelf; disturbing shelf without disarming deals 1 heart."""
    key = "smoke_shelf"

    if _is_disarmed(world, key) or world.globals.get("supply_room_entered"):
        return M_NOT_HANDLED

    world.globals["supply_room_entered"] = True

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "The shelf across from you holds a row of clay pots. "
            "Most of them are ordinary -- but one near the left end is sitting "
            "at a slightly different angle, its base against a pot behind it. "
            "If that one is disturbed without care, it will come down on the rest.\n\n"
            "You identify which pot is the trigger and carefully remove it first. "
            "The shelf is now safe to search."
        )
        _mark_disarmed(world, key)
        _reveal_smoke_jar(world)
    # Smoke jar visible to everyone eventually -- just may cost a heart
    return M_NOT_HANDLED


def fire_smoke_shelf(world: "World") -> None:
    """Called when player takes from supply shelf without disarming."""
    key = "smoke_shelf"
    if _is_disarmed(world, key) or _trap_fired(world, key):
        return

    _mark_fired(world, key)
    print(
        "The pot tips. Then the next one. "
        "A sharp crack, then a billowing cloud of acrid black smoke.\n\n"
        "Your lungs burn. When the smoke clears, the shelf is a wreck -- "
        "but among the shards and dust you can see the smoke jar, intact."
    )
    _damage(world, 1, "smoke damage")
    _reveal_smoke_jar(world)


def _reveal_smoke_jar(world: "World") -> None:
    if world.globals.get("smoke_jar_revealed"):
        return
    world.globals["smoke_jar_revealed"] = True
    jar = world.objects.get("smoke-jar")
    if jar and jar.location is None:
        world.move_object(jar, world.rooms.get("supply-room"))


# ---------------------------------------------------------------------------
# Trap 19 -- Electrified Portcullis (Portcullis Corridor)
# ---------------------------------------------------------------------------

def _enter_portcullis_corridor(world: "World") -> int:
    """Trap 19: charged portcullis blocks passage; perception/disarm/strength to pass."""
    key = "portcullis"

    if _is_disarmed(world, key) or world.globals.get("portcullis_open"):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        return M_NOT_HANDLED

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "The portcullis across the corridor is visibly charged -- "
            "a faint blue crackle runs along the bars at irregular intervals. "
            "The discharge mechanism is set into the wall to your right: "
            "a recessed panel, currently glowing. "
            "You can DISARM the portcullis (dexterity check) or try to LIFT it "
            "after discharging the charge first. "
            "A portcullis bar would prop it open once raised."
        )
    return M_NOT_HANDLED


def fire_portcullis_shock(world: "World") -> None:
    """Called when player touches the charged portcullis."""
    key = "portcullis"
    if _is_disarmed(world, key) or _trap_fired(world, key):
        return

    print(
        "The portcullis bites back.\n\n"
        "A sharp crack and a flash -- you are thrown backward a step. "
        "Your hands tingle unpleasantly and there is a smell of ozone. "
        "The portcullis is still blocking the corridor, "
        "and it is still very much charged."
    )
    _damage(world, 1, "arcane lightning")
    world.globals["portcullis_stunned"] = True  # skip player action next turn


def disarm_portcullis(world: "World") -> bool:
    """
    Called from V-DISARM or V-UNLOCK on portcullis.
    Returns True on success.
    """
    from content.player import check_trap_disarm
    key = "portcullis"

    if _is_disarmed(world, key):
        print("The portcullis is already discharged.")
        return True

    if check_trap_disarm(world, 9):
        _mark_disarmed(world, key)
        print(
            "You work the discharge panel carefully. "
            "The blue crackle fades. The portcullis is now safe to touch -- "
            "though still quite solid. You can now try to LIFT it."
        )
        return True
    else:
        print(
            "Your hand slips. The panel sparks. "
            "You pull back quickly -- the charge is still active."
        )
        _damage(world, 1, "arcane discharge")
        return False


# ---------------------------------------------------------------------------
# Trap 29 -- Pressure Plate Bell (Combat Room / Warden encounter)
# ---------------------------------------------------------------------------

def _enter_combat_room(world: "World") -> int:
    """Trap 29: pressure plate in corridor alerts the Warden inside Combat Room."""
    key = "bell_plate"

    if _is_disarmed(world, key) or _trap_fired(world, key):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        return M_NOT_HANDLED

    # Enchanted glasses reveal automatically
    auto_reveal = world.globals.get("actually_enchanted_glasses_worn")

    if auto_reveal or _perception_check(world, 9):
        _mark_seen(world, key)
        glasses_msg = " The enchanted glasses make it impossible to miss." if auto_reveal else ""
        print(
            f"A pressure plate is set into the corridor just before the doorway.{glasses_msg}\n\n"
            "Stepping on it will ring a bell in the room beyond and alert whatever waits there. "
            "You can DISARM it (press it slowly from the side) or "
            "JUMP ON PLATE if you want to trigger the fight on your own terms."
        )
        return M_NOT_HANDLED

    # Not seen -- fires on entry
    _fire_bell_plate(world)
    return M_NOT_HANDLED


def _fire_bell_plate(world: "World") -> None:
    key = "bell_plate"
    if _trap_fired(world, key):
        return

    _mark_fired(world, key)
    print(
        "Something gives underfoot -- a dull clunk. "
        "A bell rings, clear and unhurried, from the room ahead.\n\n"
        "Whatever is in there knows you're coming."
    )
    world.globals["warden_alerted"] = True
    world.globals["hostile_warden"] = True


def disarm_bell_plate(world: "World") -> None:
    """Called from V-DISARM or explicit side-press action."""
    key = "bell_plate"
    if _is_disarmed(world, key):
        print("The plate is already wedged. No bell to ring.")
        return
    if not _trap_seen(world, key):
        print("You're not sure what you'd be disarming.")
        return

    _mark_disarmed(world, key)
    print(
        "You press the plate slowly from the side, easing it down "
        "until it wedges against the floor. No bell. "
        "The Warden, if there is one, is unaware of you."
    )


def trigger_bell_plate_deliberate(world: "World") -> None:
    """JUMP ON PLATE -- deliberate trigger."""
    print(
        "You step squarely onto the pressure plate. "
        "The bell rings. You're ready for it."
    )
    _fire_bell_plate(world)


# ---------------------------------------------------------------------------
# Trap 33 -- Weight-Sensitive Pedestal (Idol Room)
# ---------------------------------------------------------------------------

def _enter_idol_room(world: "World") -> int:
    """Trap 33: no perception check needed -- idol is plainly visible on pedestal."""
    if not world.globals.get("idol_room_entered"):
        world.globals["idol_room_entered"] = True
        print(
            "In the center of the room, on a low stone pedestal, sits a small golden idol. "
            "The pedestal looks like it's under some kind of pressure -- "
            "the stone around it is slightly depressed, as if it's been weighted. "
            "Removing the idol without replacing it with something of equal weight "
            "seems like exactly the kind of thing that ends badly."
        )
    return M_NOT_HANDLED


def fire_idol_trap(world: "World") -> None:
    """Called when idol is taken without SWAP."""
    if world.globals.get("idol_swapped_safely") or world.globals.get("idol_trap_fired"):
        return

    world.globals["idol_trap_fired"] = True
    print(
        "The pedestal drops. A deep rumble from somewhere behind the walls.\n\n"
        "A heavy stone door slams shut behind you. "
        "The room is quiet again. "
        "You are not going out the way you came in."
    )
    world.globals["idol_room_sealed"] = True


def pry_idol_door(world: "World") -> bool:
    """PRY DOOR in the idol room after trap fires. Returns True on success."""
    if not world.globals.get("idol_room_sealed"):
        print("The door is open.")
        return True

    crowbar = world.objects.get("crowbar")
    if not crowbar or crowbar.location is not world.player:
        print(
            "The stone door is set tight. "
            "You'd need a crowbar to have any hope of forcing it."
        )
        return False

    from content.player import check_strength
    if check_strength(world, 12):
        world.globals["idol_room_sealed"] = False
        print(
            "The crowbar finds a seam. You lever with everything you have. "
            "The door grinds open -- slowly, noisily, but open. "
            "You are out."
        )
        return True
    else:
        print(
            "The crowbar bends slightly. The door doesn't. "
            "It is considerably heavier than you. "
            "Try again -- or try harder."
        )
        return False


# ---------------------------------------------------------------------------
# Trap 36 -- Bone Crunch Floor (Bone Passage / Antechamber approach)
# ---------------------------------------------------------------------------

def _enter_bone_passage(world: "World") -> int:
    """
    Trap 36: bones are plainly visible -- no perception check.
    Player must CLEAR BONES before proceeding toward skeleton-room.
    """
    if world.globals.get("bone_passage_cleared"):
        return M_NOT_HANDLED

    if world.globals.get("bone_passage_entered"):
        return M_NOT_HANDLED

    world.globals["bone_passage_entered"] = True
    print(
        "The passage floor is carpeted with dry bones -- not scattered randomly, "
        "but arranged. Someone put them here, or something did. "
        "The sound coming from beyond the far doorway is bone grinding on stone, "
        "steady and unhurried.\n\n"
        "You get the distinct impression that silence is not optional here."
    )
    return M_NOT_HANDLED


def _enter_skeleton_room(world: "World") -> int:
    """Trap 36 guard: entering skeleton-room without clearing bones = instant death."""
    if not attempt_enter_skeleton_room(world):
        return M_HANDLED  # jigs_up was called
    return M_NOT_HANDLED


def attempt_enter_skeleton_room(world: "World") -> bool:
    """
    Called when player tries to enter skeleton-room from bone-passage.
    Returns True if passage is safe; prints death text and calls jigs_up if not.
    """
    if world.globals.get("bone_passage_cleared"):
        return True

    print(
        "The bones crack underfoot. "
        "The grinding stops. "
        "Then the doorway fills."
    )
    world.game.jigs_up("The skeletons reached you before you could reach them.")
    return False


def clear_bones(world: "World") -> bool:
    """CLEAR BONES in bone-passage. Returns True on success."""
    here = world.here.name if world.here else ""

    if here != "bone-passage":
        return False

    if world.globals.get("bone_passage_cleared"):
        print("The bones are already swept aside.")
        return True

    world.globals["bone_passage_cleared"] = True
    print(
        "You work methodically, sweeping the bones to the sides of the passage "
        "without letting them crunch underfoot. "
        "It takes patience. When you finish, a clear path leads toward the doorway.\n\n"
        "The grinding continues from beyond. It doesn't care."
    )
    return True


# ---------------------------------------------------------------------------
# Trap 41 -- Pressure Plate Flooding (Flooding Room)
# ---------------------------------------------------------------------------

def _enter_flooding_room(world: "World") -> int:
    """Trap 41: pressure plate floods the room; two turns to pull middle lever."""
    key = "flooding_plate"

    if _is_disarmed(world, key) or _trap_fired(world, key):
        return M_NOT_HANDLED

    if world.globals.get("flooding_room_entered"):
        return M_NOT_HANDLED

    world.globals["flooding_room_entered"] = True

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "Near the entrance, set into the floor: a pressure plate, "
            "suspiciously clean in a room that is otherwise filthy. "
            "You step around it. "
            "Three levers are mounted on the far wall -- Left, Middle, Right."
        )
        return M_NOT_HANDLED

    # Plate fires -- player didn't see it
    _trigger_flooding(world)
    return M_NOT_HANDLED


def _trigger_flooding(world: "World") -> None:
    key = "flooding_plate"
    if _trap_fired(world, key):
        return

    _mark_fired(world, key)
    world.globals["flooding_active"] = True
    world.globals["flooding_turns"] = 2

    print(
        "Something clicks underfoot.\n\n"
        "A sluice opens in the wall. Water begins flooding in, fast.\n\n"
        "Three levers are mounted on the wall -- Left, Middle, Right. "
        "You have two turns."
    )
    _register_flood_daemon(world)


def _register_flood_daemon(world: "World") -> None:
    clock = world.game.clock
    if clock.get("flood-daemon") is not None:
        return

    def _flood_tick(w: "World") -> bool:
        if not w.globals.get("flooding_active"):
            return False

        turns = w.globals.get("flooding_turns", 0) - 1
        w.globals["flooding_turns"] = turns

        if turns == 1:
            print("The water is at your knees. One turn left.")
            event = w.game.clock.get("flood-daemon")
            if event:
                event.ticks = 1
        elif turns <= 0:
            _flood_sweep(w)
        else:
            event = w.game.clock.get("flood-daemon")
            if event:
                event.ticks = 1
        return False

    clock.add_demon("flood-daemon", _flood_tick)
    event = clock.get("flood-daemon")
    if event:
        event.ticks = 1


def _flood_sweep(world: "World") -> None:
    world.globals["flooding_active"] = False
    print(
        "The water reaches the ceiling. "
        "You are swept through the sluice with it.\n\n"
        "You emerge, coughing and considerably wetter, in a low passage below the flooding room. "
        "The way back up is gone."
    )
    # Teleport to flood sump below
    sump = world.rooms.get("flood-sump")
    if sump:
        world.move_object(world.winner, sump)
        world.here = sump
        world.game.describe_room()


def pull_flood_lever(world: "World", side: str) -> None:
    """
    Called from V-PULL on Left/Middle/Right lever in flooding-room.
    side: "left" | "middle" | "right"
    """
    if not world.globals.get("flooding_active"):
        print("The levers are just levers. Nothing to stop.")
        return

    if side == "left":
        if world.globals.get("left_lever_spent"):
            print("You already tried that one.")
            return
        world.globals["left_lever_spent"] = True
        print("The lever grinds but won't move.")

    elif side == "right":
        if world.globals.get("right_lever_spent"):
            print("You already tried that one.")
            return
        world.globals["right_lever_spent"] = True
        print("The lever snaps off in your hand.")

    elif side == "middle":
        world.globals["flooding_active"] = False
        # Disable flood daemon
        event = world.game.clock.get("flood-daemon")
        if event:
            event.enabled = False
        _mark_disarmed(world, "flooding_plate")
        print(
            "The middle lever moves smoothly. "
            "A heavy clunk from deep in the wall -- and the water stops rising. "
            "Slowly, through a drain you hadn't noticed before, it begins receding."
        )


# ---------------------------------------------------------------------------
# Trap 45 -- Invisible Thread Ink (Ink Corridor)
# ---------------------------------------------------------------------------

def _enter_ink_corridor(world: "World") -> int:
    """Trap 45: thread at chest height; perception spots it; triggering douses in ink."""
    key = "ink_thread"

    if _is_disarmed(world, key) or _trap_fired(world, key) or world.globals.get("inked"):
        return M_NOT_HANDLED

    if _trap_seen(world, key):
        return M_NOT_HANDLED

    if _perception_check(world, 9):
        _mark_seen(world, key)
        print(
            "A thin thread is strung across the corridor at chest height -- "
            "nearly invisible, but the slight shadow it casts on the wall gives it away. "
            "An ink bladder hangs above it. You cut the thread cleanly. "
            "The bladder drops harmlessly."
        )
        _mark_disarmed(world, key)
        return M_NOT_HANDLED

    # Fires
    _mark_fired(world, key)
    world.globals["inked"] = True
    print(
        "Something catches your chest. A sharp snap, then a cold splash.\n\n"
        "Black ink. Everywhere. Your clothes, your face, your hands -- "
        "you are comprehensively, thoroughly, embarrassingly inked.\n\n"
        "Most people in Roundabout will not deal with you like this. "
        "The inn has a bath. Five Zenni."
    )
    return M_NOT_HANDLED


def bathe_ink(world: "World") -> None:
    """Clear ink status. Called from inn rest or explicit BATHE action."""
    if world.globals.get("inked"):
        world.globals["inked"] = False
        print("The ink washes out. You look like yourself again.")
    else:
        print("You are not inked.")


# ---------------------------------------------------------------------------
# Ink status NPC guard -- called before NPC interactions
# ---------------------------------------------------------------------------

def check_ink_npc_block(world: "World", npc_key: str) -> bool:
    """
    Returns True if the NPC refuses to deal with an inked player.
    Caller should print the refusal and return M_HANDLED without advancing dialogue.
    """
    if not world.globals.get("inked"):
        return False

    # NPCs unaffected by ink
    unaffected = {"innkeeper", "toll-keeper", "kevry", "boggart"}
    if npc_key in unaffected:
        return False

    # Will Passion: disdainful but still engages
    if npc_key == "will":
        print(
            "Will peers over his spectacles. "
            "'And you found the thread,' he says, and pauses. "
            "'Everyone finds the thread.' He turns back to his work. "
            "'The inn has a bath. Use it. Twice.'"
        )
        return True  # blocks further interaction

    # Chuckle House ghost: can't be seen/interacted with while inked
    if npc_key in ("chuckle-ghost", "ghost"):
        print("The ink negates the ring's effect here. The ghost cannot be seen.")
        return True

    # All others: refuse
    print(
        f"{'They look' if npc_key not in ('may', 'shamus', 'litlock') else npc_key.title() + ' looks'} "
        "at you, then at the state of you. "
        "\"Come back when you've cleaned up.\" That's all they say."
    )
    return True
