"""
Verb handlers for Roundabout: The God-Forsaken Ring.

All Roundabout-specific verbs implemented here.
Handler signature: handler(world: World) -> int
Returns M_HANDLED, M_NOT_HANDLED, or M_FATAL.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_FATAL
from engine.world import (
    TAKEBIT, WEARBIT, CONTBIT, OPENBIT, DOORBIT, READBIT,
    ACTORBIT, WEAPONBIT, DRINKBIT, INVISIBLE, NDESCBIT,
    SURFACEBIT, SACREDBIT, BURNBIT,
)

if TYPE_CHECKING:
    from engine.game import Game
    from engine.world import World


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

def register_verbs(game: "Game") -> None:
    g = game

    # Meta / system
    g.register_verb("V-VERBOSE",     _v_verbose)
    g.register_verb("V-BRIEF",       _v_brief)
    g.register_verb("V-SUPER-BRIEF", _v_super_brief)
    g.register_verb("V-DIAGNOSE",    _v_diagnose)
    g.register_verb("V-INVENTORY",   _v_inventory)
    g.register_verb("V-QUIT",        _v_quit)
    g.register_verb("V-RESTART",     _v_restart)
    g.register_verb("V-RESTORE",     _v_restore)
    g.register_verb("V-SAVE",        _v_save)
    g.register_verb("V-SCORE",       _v_score)
    g.register_verb("V-SCRIPT",      _v_noop)
    g.register_verb("V-UNSCRIPT",    _v_noop)
    g.register_verb("V-VERSION",     _v_version)

    # Navigation -- V-WALK pre-registered by engine; do NOT override
    g.register_verb("V-BACK",        _v_back)
    g.register_verb("V-WAIT",        _v_wait)
    g.register_verb("V-ENTER",       _v_enter)
    g.register_verb("V-EXIT",        _v_exit)
    g.register_verb("V-LEAVE",       _v_exit)
    g.register_verb("V-CLIMB",       _v_climb)
    g.register_verb("V-CLIMB-UP",    _v_climb_up)
    g.register_verb("V-CLIMB-DOWN",  _v_climb_down)
    g.register_verb("V-DISEMBARK",   _v_disembark)
    g.register_verb("V-BOARD",       _v_board_ship)
    g.register_verb("V-BOARD-SHIP",  _v_board_ship)

    # Look
    g.register_verb("V-LOOK",        _v_look)
    g.register_verb("V-EXAMINE",     _v_examine)
    g.register_verb("V-LOOK-UP",     _v_look_up)
    g.register_verb("V-LOOK-INSIDE", _v_look_inside)
    g.register_verb("V-LOOK-UNDER",  _v_look_under)

    # Object manipulation
    g.register_verb("V-TAKE",        _v_take)
    g.register_verb("V-TAKE-FROM",   _v_take)
    g.register_verb("V-DROP",        _v_drop)
    g.register_verb("V-PUT-IN",      _v_put_in)
    g.register_verb("V-PUT-ON",      _v_put_on)
    g.register_verb("V-PUT",         _v_put_in)
    g.register_verb("V-APPLY",       _v_put_in)
    g.register_verb("V-WEAR",        _v_wear)
    g.register_verb("V-READ",        _v_read)
    g.register_verb("V-OPEN",        _v_open)
    g.register_verb("V-CLOSE",       _v_close)
    g.register_verb("V-LOCK",        _v_lock)
    g.register_verb("V-UNLOCK",      _v_unlock)
    g.register_verb("V-SEARCH",      _v_search)
    g.register_verb("V-POUR",        _v_pour)
    g.register_verb("V-TIE",         _v_tie)
    g.register_verb("V-UNTIE",       _v_untie)
    g.register_verb("V-THROW",       _v_throw)
    g.register_verb("V-EAT",         _v_eat)
    g.register_verb("V-DRINK",       _v_drink)
    g.register_verb("V-TURN",        _v_turn)
    g.register_verb("V-TURN-ON",     _v_lamp_on)
    g.register_verb("V-TURN-OFF",    _v_lamp_off)
    g.register_verb("V-TURN-DIAL",   _v_turn_dial)
    g.register_verb("V-ACTIVATE",    _v_lamp_on)
    g.register_verb("V-LAMP-ON",     _v_lamp_on)
    g.register_verb("V-LAMP-OFF",    _v_lamp_off)
    g.register_verb("V-LIGHT",       _v_light)
    g.register_verb("V-PULL",        _v_pull)
    g.register_verb("V-PUSH",        _v_push)
    g.register_verb("V-RUB",         _v_rub)
    g.register_verb("V-MOVE",        _v_move)
    g.register_verb("V-RAISE",       _v_raise)
    g.register_verb("V-LOWER",       _v_lower)
    g.register_verb("V-CUT",         _v_cut)
    g.register_verb("V-SWING",       _v_melee)
    g.register_verb("V-FILL",        _v_fill)
    g.register_verb("V-DIG",         _v_dig)
    g.register_verb("V-CLEAR",       _v_clear)
    g.register_verb("V-LOAD",        _v_load)
    g.register_verb("V-PRY",         _v_pry)
    g.register_verb("V-USE",         _v_use)
    g.register_verb("V-SWAP",        _v_swap)

    # NPC interaction
    g.register_verb("V-TALK",        _v_talk)
    g.register_verb("V-GIVE",        _v_give)
    g.register_verb("V-HELLO",       _v_hello)
    g.register_verb("V-FOLLOW",      _v_follow)
    g.register_verb("V-WAKE",        _v_wake)
    g.register_verb("V-SAY",         _v_say)
    g.register_verb("V-YELL",        _v_say)
    g.register_verb("V-ANSWER",      _v_answer)
    g.register_verb("V-REPLY",       _v_answer)
    g.register_verb("V-WAVE",        _v_wave)
    g.register_verb("V-FIND",        _v_find)

    # Combat
    g.register_verb("V-MELEE",       _v_melee)
    g.register_verb("V-SHOOT",       _v_shoot)
    g.register_verb("V-ATTACK",      _v_melee)
    g.register_verb("V-KILL",        _v_melee)
    g.register_verb("V-DRIVE-STAKE", _v_drive_stake)
    g.register_preaction("V-MELEE",  _pre_melee)

    # Economy
    g.register_verb("V-BUY",         _v_buy)
    g.register_verb("V-TIP",         _v_tip)
    g.register_verb("V-PLAY",        _v_play)

    # Roundabout-specific
    g.register_verb("V-FISH",        _v_fish)
    g.register_verb("V-SAIL",        _v_sail)
    g.register_verb("V-SAIL-DIR",    _v_sail)
    g.register_verb("V-DOCK",        _v_dock)
    g.register_verb("V-PRAY",        _v_pray)
    g.register_verb("V-CAST",        _v_cast)
    g.register_verb("V-REST",        _v_rest)

    # Environment
    g.register_verb("V-JUMP",        _v_jump)
    g.register_verb("V-JUMP-ON",     _v_jump)
    g.register_verb("V-CLIMB-TREE",  _v_climb_tree)
    g.register_verb("V-SWIM",        _v_swim)
    g.register_verb("V-CROSS",       _v_cross)

    # Flavor/catch-all
    g.register_verb("V-SMELL",       _v_smell)
    g.register_verb("V-LISTEN",      _v_listen)
    g.register_verb("V-STAND",       _v_stand)
    g.register_verb("V-CURSE",       _v_curse)
    g.register_verb("V-WISH",        _v_wish)
    g.register_verb("V-BURN",        _v_burn)
    g.register_verb("V-KNOCK",       _v_knock)
    g.register_verb("V-DISARM",      _v_disarm)
    g.register_verb("V-BATHE",       _v_bathe)
    g.register_verb("V-RING",        _v_noop)
    g.register_verb("V-ROLL",        _v_noop)
    g.register_verb("V-SHAKE",       _v_noop)
    g.register_verb("V-SPIN",        _v_noop)
    g.register_verb("V-SQUEEZE",     _v_noop)
    g.register_verb("V-LEAN",        _v_noop)
    g.register_verb("V-KICK",        _v_noop)
    g.register_verb("V-KISS",        _v_noop)
    g.register_verb("V-MAKE",        _v_noop)
    g.register_verb("V-MELT",        _v_noop)
    g.register_verb("V-BRUSH",       _v_noop)
    g.register_verb("V-BLAST",       _v_noop)
    g.register_verb("V-INFLATE",     _v_noop)
    g.register_verb("V-DEFLATE",     _v_noop)
    g.register_verb("V-DESTROY",     _v_noop)
    g.register_verb("V-ENCHANT",     _v_noop)
    g.register_verb("V-EXORCISE",    _v_cast)   # exorcise → cast pathway
    g.register_verb("V-LUBRICATE",   _v_noop)
    g.register_verb("V-PLUG",        _v_noop)
    g.register_verb("V-PUMP",        _v_noop)
    g.register_verb("V-PICK",        _v_noop)
    g.register_verb("V-REPENT",      _v_noop)
    g.register_verb("V-COUNT",       _v_noop)
    g.register_verb("V-NOOP",        _v_noop)


# ---------------------------------------------------------------------------
# Engine-required helper
# ---------------------------------------------------------------------------

def _score_upd(world: "World", delta: int) -> None:
    """Add delta to world score. Required by engine's game.py import."""
    world.score += delta


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _say(text: str) -> None:
    print(text)


def _here_name(world: "World") -> str:
    return world.here.name if world.here else ""


def _has_item(world: "World", item_name: str) -> bool:
    """True if player is carrying named item."""
    obj = world.objects.get(item_name)
    return obj is not None and obj.location is world.player


def _in_room(world: "World", item_name: str) -> bool:
    """True if named item is in current room."""
    obj = world.objects.get(item_name)
    return obj is not None and obj.location is world.here


def _item(world: "World", name: str):
    return world.objects.get(name)


def _deduct_zenni(world: "World", amount: int) -> bool:
    """Deduct Zenni. Returns True on success, prints message and returns False if short."""
    if world.globals.get("zenni", 0) < amount:
        _say("May looks at you evenly. \"You're short.\" She goes back to work.")
        return False
    world.globals["zenni"] -= amount
    return True


def _add_zenni(world: "World", amount: int) -> None:
    world.globals["zenni"] = world.globals.get("zenni", 0) + amount


def _heal(world: "World", hearts: int) -> None:
    g = world.globals
    g["hearts"] = min(g.get("hearts", 1) + hearts, g.get("max_hearts", 5))


def _at_full_health(world: "World") -> bool:
    g = world.globals
    return g.get("hearts", 1) >= g.get("max_hearts", 5)


def _item_name(obj) -> str:
    return obj.desc or obj.name if obj else "that"


# ---------------------------------------------------------------------------
# Meta / system
# ---------------------------------------------------------------------------

def _v_verbose(world: "World") -> int:
    from engine.game import VERBOSE
    world.game.desc_mode = VERBOSE
    _say("Maximum verbosity.")
    return M_HANDLED


def _v_brief(world: "World") -> int:
    from engine.game import BRIEF
    world.game.desc_mode = BRIEF
    _say("Brief descriptions.")
    return M_HANDLED


def _v_super_brief(world: "World") -> int:
    from engine.game import SUPER_BRIEF
    world.game.desc_mode = SUPER_BRIEF
    _say("Room titles only.")
    return M_HANDLED


def _v_diagnose(world: "World") -> int:
    g = world.globals
    level  = g.get("level", 1)
    hearts = g.get("hearts", 5)
    max_h  = g.get("max_hearts", 5)
    zenni  = g.get("zenni", 0)
    xp     = g.get("xp", 0)
    cls    = (g.get("player_class") or "unknown").capitalize()
    tick   = g.get("ring_corruption", 0)
    worn   = g.get("ring_worn", False)
    _say(f"Level {level} {cls}.  Hearts: {hearts}/{max_h}.  Zenni: {zenni}.  XP: {xp}.")
    if worn:
        _say(f"The ring is on your finger. Corruption: {tick}/50.")
    return M_HANDLED


def _v_inventory(world: "World") -> int:
    items = world.player_inventory()
    carrying = [o for o in items if o.name != "player"]
    if not carrying:
        _say("You are empty-handed.")
    else:
        _say("You are carrying:")
        for item in carrying:
            _say(f"  {_item_name(item)}")
    return M_HANDLED


def _v_quit(world: "World") -> int:
    return M_FATAL


def _v_restart(world: "World") -> int:
    _say("Restart not yet implemented.")
    return M_HANDLED


def _v_restore(world: "World") -> int:
    _say("Restore not yet implemented.")
    return M_HANDLED


def _v_save(world: "World") -> int:
    _say("Save not yet implemented.")
    return M_HANDLED


def _v_score(world: "World") -> int:
    g = world.globals
    xp    = g.get("xp", 0)
    level = g.get("level", 1)
    tc    = g.get("trophy_count", 0)
    _say(f"You have {xp} XP (Level {level}). Trophy items delivered: {tc}.")
    _say(f"Score: {world.score} in {world.moves} moves.")
    return M_HANDLED


def _v_version(world: "World") -> int:
    _say("Roundabout: The God-Forsaken Ring.")
    return M_HANDLED


def _v_noop(world: "World") -> int:
    _say("That doesn't accomplish anything here.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

def _v_back(world: "World") -> int:
    _say("You can't go back that way.")
    return M_HANDLED


def _v_wait(world: "World") -> int:
    _say("Time passes.")
    return M_HANDLED


def _v_enter(world: "World") -> int:
    return M_NOT_HANDLED


def _v_exit(world: "World") -> int:
    return M_NOT_HANDLED


def _v_climb(world: "World") -> int:
    _say("You can't climb that.")
    return M_HANDLED


def _v_climb_up(world: "World") -> int:
    return M_NOT_HANDLED


def _v_climb_down(world: "World") -> int:
    return M_NOT_HANDLED


def _v_climb_tree(world: "World") -> int:
    if _here_name(world) == "the-old-oak":
        obj = _item(world, "dragon-nip")
        # Kite is up in tree -- perception check (kite retrieval handled via Quest 41 actions)
        _say(
            "You haul yourself up into the lower branches. "
            "The kite is wedged higher than you can reach from here. "
            "The child below watches with interest but offers no advice."
        )
        return M_HANDLED
    _say("There's no climbable tree here.")
    return M_HANDLED


def _v_disembark(world: "World") -> int:
    here = _here_name(world)
    if here in ("pie-rat-ship-deck", "pie-rat-ship-hold"):
        world.game.do_walk(world, "out")
        return M_HANDLED
    _say("You're not aboard anything.")
    return M_HANDLED


def _v_board_ship(world: "World") -> int:
    here = _here_name(world)
    if here == "the-docks":
        g = world.globals
        if not g.get("has_disguise") and not g.get("ship_stolen"):
            _say(
                "A Pie Rat on deck looks you over with the thoroughness of someone whose job is exactly this. "
                '"You don\'t even look like a pirate." He doesn\'t move. Neither, apparently, will you.'
            )
            return M_HANDLED
        world.game.do_walk(world, "in")
        return M_HANDLED
    _say("There's no ship here to board.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Look
# ---------------------------------------------------------------------------

def _v_look(world: "World") -> int:
    world.game.describe_room()
    return M_HANDLED


def _v_examine(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("What do you want to examine?")
        return M_HANDLED

    # Painting in Will's tower: trigger transition
    if obj.name == "painting" and _here_name(world) == "wills-tower-main":
        from content.char_create import enter_painting
        enter_painting(world)
        return M_HANDLED

    obj.touched = True
    text = obj.ldesc or obj.fdesc or obj.desc
    if text:
        _say(text)
    else:
        _say(f"You see nothing special about the {_item_name(obj)}.")
    return M_HANDLED


def _v_look_up(world: "World") -> int:
    if _here_name(world) == "thermal-vent-room":
        # Reveal fire clay if not already found
        clay = _item(world, "fire-clay")
        if clay and INVISIBLE in clay.flags:
            clay.flags.discard(INVISIBLE)
            clay.location  # already set to None (not in world room)
            world.move_object(clay, world.here)
            _say(
                "You look up. The ceiling above the vent is crusted with something -- "
                "warm and plastic-looking, a lump of fire clay baked from below. "
                "You reach up and work it free."
            )
            return M_HANDLED
        elif clay and clay.location is world.here:
            _say("The fire clay is up there, but you already have what you need from it.")
            return M_HANDLED
    _say("You look up. Nothing unusual.")
    return M_HANDLED


def _v_look_inside(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Look inside what?")
        return M_HANDLED
    if not obj.has_flag(CONTBIT):
        _say(f"You can't look inside the {_item_name(obj)}.")
        return M_HANDLED
    if not obj.has_flag(OPENBIT):
        _say(f"The {_item_name(obj)} is closed.")
        return M_HANDLED
    contents = [o for o in getattr(obj, "contents", [])]
    if not contents:
        _say(f"The {_item_name(obj)} is empty.")
    else:
        _say(f"The {_item_name(obj)} contains:")
        for item in contents:
            _say(f"  {_item_name(item)}")
    return M_HANDLED


def _v_look_under(world: "World") -> int:
    obj = world.prso
    if obj and obj.name == "nightstand" and _here_name(world) == "wills-bedroom":
        # Dragon-nip hidden under nightstand
        from content.perception import check_perception, MEDIUM
        nip = _item(world, "dragon-nip")
        if nip and INVISIBLE in nip.flags:
            nip.flags.discard(INVISIBLE)
            world.move_object(nip, world.here)
            _say(
                "Beneath the nightstand, pushed back against the wall: a dried sprig of something. "
                "It smells unlike anything you have smelled before."
            )
            return M_HANDLED
    _say("There's nothing of interest underneath.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Object manipulation
# ---------------------------------------------------------------------------

def _v_take(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("What do you want to take?")
        return M_HANDLED
    if not obj.has_flag(TAKEBIT):
        _say(f"You can't take the {_item_name(obj)}.")
        return M_HANDLED
    if obj.has_flag(SACREDBIT):
        _say("That belongs here.")
        return M_HANDLED
    if obj.location is world.player:
        _say(f"You already have the {_item_name(obj)}.")
        return M_HANDLED
    # Carry limit: max 20 bulk
    carried = sum(o.size for o in world.player_inventory())
    if carried + obj.size > 20:
        _say("You're carrying too much to take that.")
        return M_HANDLED

    # Special: wearing ring
    if obj.name == "ring":
        from content.corruption import try_remove_ring, is_worn
        if is_worn(world):
            if not try_remove_ring(world):
                return M_HANDLED
            # ring is now off -- fall through to take
    # Special: Enchanted Glasses -- warn if Will is present
    if obj.name in ("glasses", "enchanted-glasses") and _here_name(world) == "wills-tower-main":
        will = _item(world, "will")
        if will and will.location is world.here:
            _say(
                'Will looks up sharply. "Take those off. I can\'t teach someone '
                'who already thinks they can see everything." '
                "The interaction ends there."
            )
            return M_HANDLED

    world.move_object(obj, world.player)
    obj.touched = True
    _say("Taken.")

    # Idol pedestal trap (Trap 33): fires when idol is taken without safe swap
    if obj.name == "idol" and _here_name(world) == "idol-room":
        if not world.globals.get("idol_swapped_safely"):
            from content.traps import fire_idol_trap
            fire_idol_trap(world)

    # Auto-mark disguise acquired
    if obj.name == "disguise":
        world.globals["has_disguise"] = True

    return M_HANDLED


def _v_drop(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("What do you want to drop?")
        return M_HANDLED
    if obj.location is not world.player:
        _say(f"You don't have the {_item_name(obj)}.")
        return M_HANDLED

    here = _here_name(world)

    # Wearing ring: must call try_remove_ring
    if obj.name == "ring" and world.globals.get("ring_worn"):
        from content.corruption import try_remove_ring
        if not try_remove_ring(world):
            return M_HANDLED

    # Enchanted Glasses dropped in Will's Bedroom
    if obj.name in ("glasses", "enchanted-glasses") and here == "wills-bedroom":
        world.move_object(obj, world.here)
        bonus_xp = 20 if obj.name == "enchanted-glasses" else 10
        from content.experience import award_xp
        award_xp(world, bonus_xp)
        _say(
            f"You set the {_item_name(obj)} down on the nightstand. "
            "There's something satisfying about returning something to where it belongs."
        )
        return M_HANDLED

    world.move_object(obj, world.here)
    _say("Dropped.")
    return M_HANDLED


def _v_put_in(world: "World") -> int:
    obj       = world.prso
    container = world.prsi
    if obj is None or container is None:
        _say("You need to specify what to put and where.")
        return M_HANDLED

    # Trophy Case special handling
    if container.name == "trophy-case":
        return _put_in_trophy_case(world, obj)

    # Pour vial into pool (Quest 34)
    if obj.name == "glacier-melt" and _here_name(world) == "quest-34-mid-room":
        _say(
            "You pour the vial into the dark pool. "
            "The water reacts instantly -- a deep creak as it freezes, surface locking "
            "from the point of contact outward until the entire pool is solid. "
            "Cold steam rises and fades. You can cross."
        )
        world.move_object(obj, None)
        world.globals["mid_room_frozen"] = True
        return M_HANDLED

    if not container.has_flag(CONTBIT):
        _say(f"You can't put things in the {_item_name(container)}.")
        return M_HANDLED
    if not container.has_flag(OPENBIT):
        _say(f"The {_item_name(container)} is closed.")
        return M_HANDLED
    if not container.can_hold(obj):
        _say(f"There's no room in the {_item_name(container)}.")
        return M_HANDLED
    world.move_object(obj, container)
    _say("Done.")
    return M_HANDLED


def _put_in_trophy_case(world: "World", obj) -> int:
    """Handle delivering a treasure to the Trophy Case."""
    if obj.value <= 0:
        _say(f"The {_item_name(obj)} doesn't belong in the Trophy Case.")
        return M_HANDLED
    if _here_name(world) != "the-tower":
        _say("The Trophy Case is in the Tower, Town Hall.")
        return M_HANDLED
    _score_upd(world, obj.value)
    world.globals["trophy_count"] = world.globals.get("trophy_count", 0) + 1
    world.globals.setdefault("trophy_items", []).append(obj.name)
    world.move_object(obj, world.here)  # leave it in the case room
    _say(
        f"You place the {_item_name(obj)} in the Trophy Case. "
        f"It joins the display with the quiet authority of something that earned its spot."
    )
    return M_HANDLED


def _v_put_on(world: "World") -> int:
    obj     = world.prso
    surface = world.prsi
    if obj is None:
        _say("Put what where?")
        return M_HANDLED

    # "Put ring on altar" -- ritual use
    if obj.name == "ring" and surface and surface.name in ("altar", "dial"):
        return _ring_on_altar(world)

    if surface is None or not surface.has_flag(SURFACEBIT):
        _say(f"You can't put things on that.")
        return M_HANDLED
    world.move_object(obj, surface)
    _say("Done.")
    return M_HANDLED


def _ring_on_altar(world: "World") -> int:
    """Place ring on Church of All altar for ritual use."""
    if _here_name(world) != "the-altar":
        _say("The altar is in the Church of All.")
        return M_HANDLED

    dial = world.globals.get("altar_dial_setting", "none")
    ring = _item(world, "ring")
    if not ring or ring.location is not world.player:
        _say("You don't have the ring.")
        return M_HANDLED

    # Check ritual requirements (handled by quests/actions -- stub dispatch)
    from content.actions import altar_ritual
    return altar_ritual(world, dial)


def _v_wear(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("What do you want to wear?")
        return M_HANDLED
    if not obj.has_flag(WEARBIT):
        _say(f"You can't wear the {_item_name(obj)}.")
        return M_HANDLED
    if obj.location is not world.player:
        _say(f"You don't have the {_item_name(obj)}.")
        return M_HANDLED

    # Ring: special wear logic
    if obj.name == "ring":
        from content.corruption import wear_ring
        wear_ring(world)
        _say("You slip the ring onto your finger. It fits as though it was waiting.")
        world.globals["ring_worn"] = True
        return M_HANDLED

    # Enchanted Glasses: warn if Will present
    if obj.name in ("glasses", "enchanted-glasses"):
        will = _item(world, "will")
        if will and will.location is world.here:
            _say(
                '"Take those off. I can\'t teach someone who already thinks they can see everything." '
                "Will's tone leaves no room for negotiation."
            )
            return M_HANDLED
        if obj.name == "glasses":
            world.globals["enchanted_glasses_worn"] = True
        else:
            world.globals["actually_enchanted_glasses_worn"] = True
        obj.set_flag("WEARING")
        _say(f"You put on the {_item_name(obj)}.")
        return M_HANDLED

    if obj.name == "boots":
        world.globals["boots_worn"] = True
    elif obj.name == "gloves":
        world.globals["gloves_worn"] = True
    elif obj.name == "ivaanars-tunic":
        world.globals["ivaanars_tunic_worn"] = True
    elif obj.name == "heart-necklace":
        if not world.globals.get("necklace_bonus_applied"):
            world.globals["necklace_bonus_applied"] = True
            world.globals["max_hearts"] = world.globals.get("max_hearts", 5) + 1
            world.globals["hearts"] = world.globals.get("hearts", 5) + 1

    obj.set_flag("WEARING")
    _say(f"You put on the {_item_name(obj)}.")
    return M_HANDLED


def _v_read(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("What do you want to read?")
        return M_HANDLED
    if not obj.has_flag(READBIT):
        _say(f"There's nothing to read on the {_item_name(obj)}.")
        return M_HANDLED

    # Spell scroll resistance for Warriors/Rogues
    scroll_names = ("light-scroll", "unbind-scroll", "fireball-scroll")
    if obj.name in scroll_names:
        return _read_spell_scroll(world, obj)

    # Incantation scroll (Quest 34 -- use-item, all classes)
    if obj.name == "incantation-scroll":
        return _read_incantation_scroll(world, obj)

    if obj.text:
        _say(obj.text)
    else:
        _say(f"The {_item_name(obj)} has nothing useful written in it.")
    return M_HANDLED


def _read_spell_scroll(world: "World", obj) -> int:
    cls = world.globals.get("player_class", "")
    if cls == "mage":
        # Mages read directly
        _learn_spell(world, obj)
        return M_HANDLED
    # Warriors/Rogues: resistance message
    will = _item(world, "will")
    will_here = will and will.location is world.here
    if will_here:
        # In Will's presence -- teach it
        _teach_via_will(world, obj)
        return M_HANDLED
    _say(
        "The words are legible. The meaning is not. "
        "Whatever is written here was meant for someone with a different kind of mind -- "
        "or a different kind of training. "
        "Will Passion, in his tower, has been known to translate this sort of thing for people like you."
    )
    return M_HANDLED


def _learn_spell(world: "World", obj) -> None:
    spell_map = {
        "light-scroll":    "spell_light",
        "unbind-scroll":   "spell_unbind_undead",
        "fireball-scroll": "spell_fireball",
    }
    key = spell_map.get(obj.name)
    if key and not world.globals.get(key):
        world.globals[key] = True
        _say(
            "Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, "
            "reading silently for a moment. Then he reads it aloud -- not to you, exactly, "
            "more as if the words need to be heard in the right kind of room. "
            'When he finishes, you understand it. You\'re not sure how. "Keep that," he says, '
            "nodding at the space where the scroll was. It's gone. \"The knowing, I mean.\""
        ) if False else _say("You read the scroll. The knowledge settles into you with unexpected clarity.")
        world.move_object(obj, None)  # consumed
    else:
        _say("You already know this spell.")


def _teach_via_will(world: "World", obj) -> None:
    spell_map = {
        "light-scroll":    "spell_light",
        "unbind-scroll":   "spell_unbind_undead",
        "fireball-scroll": "spell_fireball",
    }
    key = spell_map.get(obj.name)
    if key and not world.globals.get(key):
        world.globals[key] = True
        _say(
            "Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, "
            "reading silently for a moment. Then he reads it aloud -- not to you, exactly, "
            "more as if the words need to be heard in the right kind of room. "
            "When he finishes, you understand it. You're not sure how. "
            '"Keep that," he says, nodding at the space where the scroll was. '
            "It's gone. \"The knowing, I mean.\""
        )
        world.move_object(obj, None)  # consumed
    else:
        _say("You already know this spell.")


def _read_incantation_scroll(world: "World", obj) -> int:
    if _here_name(world) == "tool-alcove" and not world.globals.get("tool_alcove_door_open"):
        _say(
            "You read the scroll aloud. The syllables fill the alcove with unexpected resonance. "
            "The back wall shifts -- a seam appears, then a door, swinging inward. "
            "Beyond it, darkness and the smell of cold stone."
        )
        world.globals["tool_alcove_door_open"] = True
        world.move_object(obj, None)  # consumed
        return M_HANDLED
    _say("You read the scroll. The words resonate, but there's nothing here to answer them.")
    return M_HANDLED


def _v_open(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Open what?")
        return M_HANDLED

    # Mailbox in white-house: triggers opening sequence
    if obj.name == "mailbox" and _here_name(world) == "white-house":
        if world.globals.get("opening_complete"):
            _say("The mailbox is open. There's nothing new in it.")
        else:
            _say("The mailbox opens. Inside: nothing. And then --")
            from content.char_create import run_opening
            run_opening(world)
        return M_HANDLED

    # Music box: requires key
    if obj.name == "music-box":
        key = _item(world, "music-box-key")
        if key and key.location is world.player:
            obj.set_flag(OPENBIT)
            _say(
                "The key turns smoothly. The lid opens. "
                "Inside, nested in old velvet: a scroll."
            )
            scroll = _item(world, "light-scroll")
            if scroll:
                world.move_object(scroll, world.here)
            return M_HANDLED
        else:
            _say("The music box is locked. It needs a key.")
            return M_HANDLED

    # Magnetic chest (Trap 15): fire trap if not disarmed
    if obj.name in ("chest", "magnetic-chest") and _here_name(world) == "magnetic-vault":
        if not world.globals.get("trap_disarmed_magnetic_chest") and not world.globals.get("trap_fired_magnetic_chest"):
            from content.traps import fire_magnetic_chest
            fire_magnetic_chest(world)
            # Chest opens regardless
        obj.set_flag(OPENBIT)
        _say("Opened.")
        return M_HANDLED

    if not (obj.has_flag(CONTBIT) or obj.has_flag(DOORBIT)):
        _say(f"You can't open the {_item_name(obj)}.")
        return M_HANDLED
    if obj.has_flag(OPENBIT):
        _say(f"The {_item_name(obj)} is already open.")
        return M_HANDLED
    obj.set_flag(OPENBIT)
    _say("Opened.")

    # Display cabinet in upper hall: wax seal inside
    if obj.name == "display-cabinet" and _here_name(world) == "upper-hall":
        seal = _item(world, "wax-seal")
        if seal and seal.location is None:
            world.move_object(seal, world.here)
            _say("Inside: a wax seal and some old civic documents.")
    return M_HANDLED


def _v_close(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Close what?")
        return M_HANDLED
    if not obj.has_flag(OPENBIT):
        _say(f"The {_item_name(obj)} is already closed.")
        return M_HANDLED
    obj.clear_flag(OPENBIT)
    _say("Closed.")
    return M_HANDLED


def _v_lock(world: "World") -> int:
    _say("You can't lock that.")
    return M_HANDLED


def _v_unlock(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Unlock what?")
        return M_HANDLED

    # Cellar door (Quest 25)
    if obj.name in ("cellar-door", "cellar") and _here_name(world) == "tale-and-ale-kitchen":
        key = _item(world, "cellar-key")
        if key and key.location is world.player:
            world.globals["cellar_key_used"] = True
            _say("The key turns. The cellar door swings open.")
            return M_HANDLED
        _say("It's locked. The bartender has the key.")
        return M_HANDLED

    # Mid-Tier Key Door
    if obj.name in ("door", "iron-door") and _here_name(world) == "mid-tier-key-door":
        key = _item(world, "mid-tier-key")
        if key and key.location is world.player:
            world.globals["mid_tier_key_used"] = True
            _say("The key fits. The door opens with a heavy groan.")
            return M_HANDLED
        _say("The door is locked. It wants a specific key.")
        return M_HANDLED

    # Large iron chest (Mine Passage -- lockpicks)
    if obj.name in ("chest", "iron-chest") and _here_name(world) == "mine-passage":
        picks = _item(world, "lockpicks")
        if picks and picks.location is world.player:
            world.globals["mine_chest_open"] = True
            _add_zenni(world, 20)
            _say(
                "The lockpicks make short work of it. Inside: twenty Zenni, "
                "and the smell of old metal and ambition."
            )
            return M_HANDLED
        _say("It's locked tight. Lockpicks would help.")
        return M_HANDLED

    # Keeper's Chamber door
    if _here_name(world) == "the-altar":
        keys = _item(world, "keepers-keys")
        if keys and keys.location is world.player:
            world.globals["keepers_door_unlocked"] = True
            _say("The key ring has what this door needs. The door opens.")
            return M_HANDLED
        _say("The door is locked. It needs a key.")
        return M_HANDLED

    _say("You can't unlock that here.")
    return M_HANDLED


def _v_search(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Search what?")
        return M_HANDLED

    # Statue base -- hollow, contains silver stake
    if obj.name == "statue" and _here_name(world) == "town-square":
        crowbar = _item(world, "crowbar")
        if crowbar and crowbar.location is world.player:
            stake = _item(world, "silver-stake")
            if stake and stake.location is None:
                world.move_object(stake, world.here)
                _say(
                    "The base of the statue is hollow -- a seam runs around it at ground level. "
                    "The crowbar opens it with some effort. "
                    "Inside: a silver stake and a folded note sealed with emerald wax."
                )
                return M_HANDLED
            elif stake:
                _say("The hollow base is open. You already took what was inside.")
                return M_HANDLED
        _say("The statue base looks solid. You'd need something to pry it with.")
        return M_HANDLED

    _say(f"You search the {_item_name(obj)}. Nothing unusual turns up.")
    return M_HANDLED


def _v_pour(world: "World") -> int:
    obj  = world.prso
    dest = world.prsi
    if obj is None:
        _say("Pour what?")
        return M_HANDLED

    # Holy water on silver stake
    if obj.name == "holy-water" and dest and dest.name == "silver-stake":
        if dest.location is world.player:
            stake = _item(world, "consecrated-stake")
            if stake is None:
                from content.objects import _place
                from engine.world import GameObject
                stake = GameObject(
                    name="consecrated-stake",
                    synonyms={"consecrated silver stake", "consecrated stake", "holy stake", "silver stake"},
                    desc="a consecrated silver stake",
                    ldesc="The silver stake has been anointed with holy water. The metal has a faint sheen to it now.",
                    flags=set({TAKEBIT, WEAPONBIT}),
                    size=2,
                )
                world.register_object(stake)
            world.move_object(stake, world.player)
            world.move_object(dest, None)   # stake consumed in transformation
            world.move_object(obj, None)    # holy water consumed
            _say(
                "You pour the holy water over the silver stake. "
                "The metal takes on a faint sheen -- not wet, more like a memory of light."
            )
            return M_HANDLED

    _say(f"You pour the {_item_name(obj)}. It doesn't accomplish much.")
    return M_HANDLED


def _v_tie(world: "World") -> int:
    obj  = world.prso
    dest = world.prsi
    if obj and obj.name == "rope":
        here = _here_name(world)
        if here in ("stored-room", "hole-to-below"):
            if obj.location is world.player:
                world.globals["rope_tied"] = True
                world.move_object(obj, world.here)
                _say(
                    "You secure the rope to the beam above. "
                    "It hangs down into the dark below. "
                    "Getting back up will be possible now."
                )
                return M_HANDLED
    _say("That doesn't seem possible here.")
    return M_HANDLED


def _v_untie(world: "World") -> int:
    _say("There's nothing tied here.")
    return M_HANDLED


def _v_throw(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Throw what?")
        return M_HANDLED
    if obj.location is not world.player:
        _say(f"You don't have the {_item_name(obj)}.")
        return M_HANDLED
    _say(f"You hurl the {_item_name(obj)}. It lands nearby.")
    world.move_object(obj, world.here)
    return M_HANDLED


def _v_eat(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Eat what?")
        return M_HANDLED
    if obj.location is not world.player:
        _say(f"You don't have the {_item_name(obj)}.")
        return M_HANDLED

    # Enchanted honey: restore 2 hearts
    if obj.name == "enchanted-honey":
        _heal(world, 2)
        world.move_object(obj, None)
        _say(
            "The honey is extraordinary -- sweet but not cloying, warm going down. "
            "You feel better. Considerably better."
        )
        return M_HANDLED

    if obj.has_flag(DRINKBIT):
        return _v_drink(world)

    _say(f"You eat the {_item_name(obj)}.")
    world.move_object(obj, None)
    return M_HANDLED


def _v_drink(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Drink what?")
        return M_HANDLED
    if obj.location is not world.player:
        _say(f"You don't have the {_item_name(obj)}.")
        return M_HANDLED
    _say(f"You drink the {_item_name(obj)}.")
    world.move_object(obj, None)
    return M_HANDLED


def _v_turn(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Turn what?")
        return M_HANDLED
    _say(f"The {_item_name(obj)} doesn't turn.")
    return M_HANDLED


def _v_turn_dial(world: "World") -> int:
    """Turn the Church of All altar dial left or right."""
    if _here_name(world) not in ("the-altar", "church-nave"):
        _say("There's no dial here.")
        return M_HANDLED

    # The parser provides direction via prso or world.prsi
    # We check what the parser resolved as the second object / particle
    obj = world.prso
    direction = None
    if obj:
        n = getattr(obj, "name", "") or ""
        if "left" in n:
            direction = "left"
        elif "right" in n:
            direction = "right"

    if direction is None:
        _say("Turn the dial left or right?")
        return M_HANDLED

    religions = ["Brotherhood of the Pale Blade", "The Veil of the Arcane",
                 "Verdant Circle", "The Tide Faith", "The Ashen Path",
                 "The Silver Compact", "The Unnamed"]
    current = world.globals.get("altar_dial_index", 0)
    if direction == "left":
        current = (current - 1) % len(religions)
    else:
        current = (current + 1) % len(religions)
    world.globals["altar_dial_index"] = current
    world.globals["altar_dial_setting"] = religions[current].lower().replace(" ", "-")
    _say(f"The dial turns. The glow settles on: {religions[current]}.")
    return M_HANDLED


def _v_lamp_on(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Turn on what?")
        return M_HANDLED

    # Guardian's Lantern in Dark Room
    if obj.name == "lantern":
        if obj.location is not world.player:
            _say("You don't have the lantern.")
            return M_HANDLED
        if _here_name(world) == "dark-room":
            _say(
                "You light the lantern. "
                "The magical darkness does not retreat gracefully -- it collapses, suddenly, "
                "as if the lantern was exactly what was needed and nothing else would have worked. "
                "The room is revealed. You hang the lantern on the wall hook -- it holds."
            )
            world.globals["dark_room_lit"] = True
            world.move_object(obj, world.here)   # affixed to wall
            return M_HANDLED
        _say("The lantern flickers but gives no useful light here.")
        return M_HANDLED

    if obj.has_flag(BURNBIT):
        obj.set_flag("ON")
        _say(f"The {_item_name(obj)} is now lit.")
        return M_HANDLED
    _say(f"You can't light the {_item_name(obj)}.")
    return M_HANDLED


def _v_lamp_off(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Turn off what?")
        return M_HANDLED
    if obj.has_flag(BURNBIT):
        obj.clear_flag("ON")
        _say(f"The {_item_name(obj)} is now off.")
        return M_HANDLED
    _say(f"The {_item_name(obj)} isn't on.")
    return M_HANDLED


def _v_light(world: "World") -> int:
    obj  = world.prso
    dest = world.prsi
    if obj is None:
        _say("Light what?")
        return M_HANDLED

    # LIGHT GUNPOWDER (heist)
    if obj.name == "gunpowder":
        flint = _item(world, "flint-and-steel")
        if not flint or flint.location is not world.player:
            _say("You'd need flint and steel to light that.")
            return M_HANDLED
        here = _here_name(world)
        if here == "mine-tunnels":
            _say(
                "You strike the flint. The fuse catches. "
                "You have enough time to get clear -- or not, if you linger."
            )
            world.globals["gunpowder_lit"] = True
            world.globals["heist_explosion_pending"] = True
            world.move_object(obj, world.here)
            return M_HANDLED
        _say("There's nothing here to make useful use of that.")
        return M_HANDLED

    if obj.has_flag(BURNBIT):
        obj.set_flag("ON")
        _say(f"The {_item_name(obj)} is lit.")
        return M_HANDLED
    _say(f"You can't light the {_item_name(obj)}.")
    return M_HANDLED


def _v_pull(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Nothing happens.")
        return M_HANDLED

    here = _here_name(world)

    # Flooding Room levers (Trap 41)
    if here == "flooding-room":
        from content.traps import pull_flood_lever
        name = getattr(obj, "name", "") or ""
        if "left" in name:
            pull_flood_lever(world, "left")
            return M_HANDLED
        if "right" in name:
            pull_flood_lever(world, "right")
            return M_HANDLED
        if "middle" in name or name in ("lever", "levers"):
            pull_flood_lever(world, "middle")
            return M_HANDLED

    # Flooding Room levers by room state (no named object -- plain PULL LEVER)
    if here == "flooding-room" and world.globals.get("flooding_active"):
        _say("Which lever? Left, middle, or right?")
        return M_HANDLED

    _say("Nothing happens.")
    return M_HANDLED


def _v_push(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Nothing happens.")
        return M_HANDLED

    # Pressure plate -- explicit push (trap awareness)
    if obj.name == "pressure-plate":
        _say("You deliberately step on the pressure plate.")
        return M_HANDLED

    _say("Nothing happens.")
    return M_HANDLED


def _v_rub(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Rub what?")
        return M_HANDLED

    # RUB PAPER ON ENGRAVING (Quest 28)
    if obj.name == "thin-paper" and _here_name(world) == "inscription-chamber":
        charcoal = _item(world, "charcoal")
        if charcoal and charcoal.location is world.player:
            _say(
                "You hold the paper against the engraving and work the charcoal across it. "
                "A pattern emerges -- clear, detailed, unmistakably old. "
                "The rubbing lifts perfectly."
            )
            world.globals["rubbing_made"] = True
            obj.name = "rubbing"
            obj.desc = "a charcoal rubbing"
            obj.ldesc = (
                "A rubbing of the inscription in the chamber below. "
                "The lines are precise and the detail is good."
            )
            return M_HANDLED
        _say("You'd need charcoal to make a rubbing.")
        return M_HANDLED

    _say(f"You rub the {_item_name(obj)}. Nothing happens.")
    return M_HANDLED


def _v_move(world: "World") -> int:
    _say("It doesn't budge.")
    return M_HANDLED


def _v_raise(world: "World") -> int:
    _say("You can't raise that.")
    return M_HANDLED


def _v_lower(world: "World") -> int:
    _say("You can't lower that.")
    return M_HANDLED


def _v_cut(world: "World") -> int:
    _say("You'd need something sharp for that.")
    return M_HANDLED


def _v_fill(world: "World") -> int:
    obj  = world.prso
    src  = world.prsi
    if obj is None:
        _say("Fill what?")
        return M_HANDLED
    _say(f"There's nothing suitable to fill the {_item_name(obj)} with here.")
    return M_HANDLED


def _v_dig(world: "World") -> int:
    here = _here_name(world)
    shovel = _item(world, "shovel")
    if not shovel or shovel.location is not world.player:
        _say("You'd need a shovel for that.")
        return M_HANDLED

    # Will Passion audio note (1/20 chance)
    if random.randint(1, 20) == 1:
        _say("(Somewhere distant, you imagine a dry voice saying: \"Really.\")")

    # Stored Room collapse (mid-tier)
    if here == "stored-room" and not world.globals.get("stored_room_collapsed"):
        _say(
            "You dig into the fill. It goes faster than expected -- the material was never "
            "compacted properly. After some work the floor gives way: a rough hole drops "
            "into darkness below. A rope would help getting back up."
        )
        world.globals["stored_room_collapsed"] = True
        return M_HANDLED

    # Desert Island buried chest
    if here == "desert-island":
        return _dig_desert_island(world)

    # Lost Apprentice's Cell escape tunnel (Quest 50)
    if here == "lost-apprentice-cell":
        if world.globals.get("apprentice_rescued"):
            progress = world.globals.get("tunnel_dig_progress", 0) + 1
            world.globals["tunnel_dig_progress"] = progress
            if progress >= 3:
                world.globals["apprentice_rescued_escaped"] = True
                _say(
                    "The last of the dirt gives way. Fresh bog air floods in. "
                    "The tunnel connects to the bog above. You can both get out."
                )
            else:
                _say(f"You dig. Progress: {progress}/3.")
            return M_HANDLED

    _say("Digging here doesn't accomplish anything.")
    return M_HANDLED


def _dig_desert_island(world: "World") -> int:
    g = world.globals
    has_map = _has_item(world, "treasure-map")

    if has_map:
        success = True
    else:
        success = random.randint(1, 10) == 1  # 10% without map

    if g.get("desert_chest_found"):
        _say("The hole is already dug. The chest is open. There's nothing left to dig for.")
        return M_HANDLED

    if success:
        g["desert_chest_found"] = True
        _add_zenni(world, 50)
        _say(
            "The shovel strikes something solid. "
            "A chest -- old, salt-rotted wood but iron hardware still good. "
            "Inside: fifty Zenni, and the smell of a very long time."
        )
    else:
        _say("You dig. Nothing but sand and more sand.")
    return M_HANDLED


def _v_clear(world: "World") -> int:
    obj  = world.prso
    here = _here_name(world)

    # CLEAR DRAIN (cellar, Quest 25)
    if here == "cellar-storeroom" and not world.globals.get("cellar_drained"):
        crowbar = _item(world, "crowbar")
        if crowbar and crowbar.location is world.player:
            _say(
                "You pry the drain cover loose with the crowbar. "
                "Water swirls and begins draining quickly. "
                "The cellar floor appears as the water drops."
            )
            world.globals["cellar_drained"] = True
            return M_HANDLED
        _say("The drain cover is corroded shut. You'd need a crowbar.")
        return M_HANDLED

    # CLEAR BONES (Trap 36)
    if here == "bone-passage":
        from content.traps import clear_bones
        clear_bones(world)
        return M_HANDLED

    _say("There's nothing to clear here.")
    return M_HANDLED


def _v_load(world: "World") -> int:
    obj  = world.prso
    dest = world.prsi

    # LOAD STONE ONTO CART (Quest 32)
    if obj and obj.name == "gravestone" and dest and dest.name == "hand-cart":
        if obj.location is world.here and dest.location is world.here:
            world.move_object(obj, dest)
            _say(
                "You wrestle the heavy gravestone onto the cart. "
                "It takes real effort -- the stone is thick marble. "
                "Now you can move it."
            )
            return M_HANDLED

    _say("Nothing to load here.")
    return M_HANDLED


def _v_pry(world: "World") -> int:
    obj    = world.prso
    crowbar = _item(world, "crowbar")
    here   = _here_name(world)

    if not crowbar or crowbar.location is not world.player:
        _say("You'd need a crowbar for that.")
        return M_HANDLED

    # PRY statue base (town square -- silver stake)
    if here == "town-square" and (obj is None or obj.name in ("statue", "base")):
        stake = _item(world, "silver-stake")
        if stake and stake.location is None:
            world.move_object(stake, world.here)
            _say(
                "The crowbar finds the seam at the base of the statue. "
                "With effort the base pops open -- hollow inside. "
                "A silver stake, and a folded note with an emerald wax seal."
            )
            return M_HANDLED
        _say("The statue base is already open.")
        return M_HANDLED

    # PRY drain cover (cellar -- same as clear drain)
    if here == "cellar-storeroom" and not world.globals.get("cellar_drained"):
        _say(
            "You pry the drain cover loose. "
            "Water swirls and begins draining. "
            "The cellar floor appears as the water drops."
        )
        world.globals["cellar_drained"] = True
        return M_HANDLED

    # PRY sealed idol room door (Trap 33)
    if here == "idol-room" and world.globals.get("idol_room_sealed"):
        from content.traps import pry_idol_door
        pry_idol_door(world)
        return M_HANDLED

    # PRY lodestone from magnetic chest (Trap 15)
    if obj and obj.name in ("lodestone", "chest", "magnetic-chest") and here == "magnetic-vault":
        if world.globals.get("trap_disarmed_magnetic_chest"):
            _say("The lodestone is already removed.")
            return M_HANDLED
        world.globals["trap_disarmed_magnetic_chest"] = True
        _say(
            "You work the crowbar into the gap between the lid and the body of the chest. "
            "The lodestone pops free and clatters to the floor. "
            "The chest is now safe to open."
        )
        return M_HANDLED

    _say("You lever at it with the crowbar. Nothing gives.")
    return M_HANDLED


def _v_use(world: "World") -> int:
    obj = world.prso
    if obj is None:
        _say("Use what?")
        return M_HANDLED

    # USE PORTCULLIS BAR
    if obj.name == "portcullis-bar" and _here_name(world) == "portcullis-corridor":
        if obj.location is world.player:
            world.globals["portcullis_open"] = True
            world.move_object(obj, world.here)
            _say(
                "You wedge the iron bar through the portcullis gate, propping it up. "
                "It holds. The passage south is open."
            )
            return M_HANDLED

    # USE IVORY TORCH (Quest 34 -- thaw frozen soldier)
    if obj.name == "ivory-torch" and _here_name(world) == "quest-34-fountain-room":
        if obj.location is not world.player:
            _say("You don't have the ivory torch.")
            return M_HANDLED
        progress = world.globals.get("thaw_progress", 0) + 1
        world.globals["thaw_progress"] = progress
        if progress == 1:
            _say(
                "You hold the torch close to the ice. "
                "The frost on the surface begins to sweat. "
                "A second pass should do it."
            )
        elif progress >= 2:
            _say(
                "The ice gives way -- not in a rush, but steadily, "
                "slabs of it sliding to the floor as the block loses cohesion. "
                "The figure inside blinks. Looks around. Looks at you."
            )
            world.globals["soldier_thawed"] = True
            blade = _item(world, "forgotten-blade")
            if blade:
                world.move_object(blade, world.here)
                _say(
                    "He holds out a sword -- flat across both palms, the grip toward you. "
                    "No words. No ceremony. He sets it down on the floor and walks away."
                )
            # Soldier appears in town on subsequent visits
            world.globals["soldier_in_town"] = True
        return M_HANDLED

    _say(f"Using the {_item_name(obj)} doesn't accomplish anything here.")
    return M_HANDLED


def _v_swap(world: "World") -> int:
    obj  = world.prso
    dest = world.prsi

    # SWAP IDOL WITH SALT -- Idol Room trap
    if (obj and obj.name == "idol" and dest and dest.name == "sack-of-salt") or \
       (obj and obj.name == "sack-of-salt" and dest and dest.name == "idol"):
        if _here_name(world) == "idol-room":
            idol = _item(world, "idol")
            salt = _item(world, "sack-of-salt")
            if idol and salt and salt.location is world.player:
                world.move_object(idol, world.player)
                world.move_object(salt, world.here)
                world.globals["idol_swapped_safely"] = True
                _say(
                    "You place the sack of salt on the pedestal in one motion "
                    "as you lift the idol free. "
                    "The pedestal settles. Nothing clicks. Nothing fires."
                )
                return M_HANDLED
        _say("That swap won't work here.")
        return M_HANDLED

    _say("That doesn't seem possible here.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# NPC interaction
# ---------------------------------------------------------------------------

def _v_talk(world: "World") -> int:
    npc = world.prso
    if npc is None:
        _say("Talk to whom?")
        return M_HANDLED
    # Ink check
    if world.globals.get("inked"):
        from content.traps import check_ink_npc_block
        if check_ink_npc_block(world, npc.name):
            return M_HANDLED
    # Dispatch to NPC module (Phase 7)
    from content import npcs as npc_module
    return npc_module.dispatch_talk(world, npc)


def _v_give(world: "World") -> int:
    obj = world.prso
    npc = world.prsi
    if obj is None or npc is None:
        _say("Give what to whom?")
        return M_HANDLED
    # Dispatch to NPC module (Phase 7)
    from content import npcs as npc_module
    return npc_module.dispatch_give(world, obj, npc)


def _v_hello(world: "World") -> int:
    _say("Hello yourself.")
    return M_HANDLED


def _v_follow(world: "World") -> int:
    _say("They pay you no mind.")
    return M_HANDLED


def _v_wake(world: "World") -> int:
    _say("Leave them be.")
    return M_HANDLED


def _v_say(world: "World") -> int:
    _say("Your words fall flat.")
    return M_HANDLED


def _v_answer(world: "World") -> int:
    _say("There's no question pending.")
    return M_HANDLED


def _v_wave(world: "World") -> int:
    _say("You wave. Nobody waves back.")
    return M_HANDLED


def _v_find(world: "World") -> int:
    _say("You'll have to look for it yourself.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Combat
# ---------------------------------------------------------------------------

def _pre_melee(world: "World") -> int:
    """Preaction for V-MELEE: block explicit weapon use without skill."""
    explicit = world.prsi
    if explicit is None or getattr(explicit, "name", None) not in ("dagger", "mace", "battle-axe"):
        return M_NOT_HANDLED
    g = world.globals
    has_skill = g.get("skill_melee") or g.get("player_class") == "warrior"
    if not has_skill:
        _say("You don't know how to fight with that. Find someone to teach you.")
        return M_HANDLED
    return M_NOT_HANDLED


def _best_melee_weapon(world: "World") -> str:
    """Return the name of the best usable melee weapon in inventory, or 'melee' for unarmed."""
    g = world.globals
    has_skill = g.get("skill_melee") or g.get("player_class") == "warrior"
    if not has_skill:
        return "melee"
    _WEAPON_PRIORITY = [("battle-axe", 6), ("mace", 4), ("dagger", 2)]
    for obj_name, _ in _WEAPON_PRIORITY:
        obj = _item(world, obj_name)
        if obj and obj.location is world.player:
            return obj_name
    return "melee"


def _v_melee(world: "World") -> int:
    npc = world.prso
    if npc is None:
        _say("Attack what?")
        return M_HANDLED

    # KILL X WITH <weapon> — explicit weapon specified via prsi
    explicit = world.prsi
    if explicit is not None and getattr(explicit, "name", None) in ("dagger", "mace", "battle-axe"):
        g = world.globals
        has_skill = g.get("skill_melee") or g.get("player_class") == "warrior"
        if not has_skill:
            _say("You don't know how to fight with that. Find someone to teach you.")
            return M_HANDLED
        weapon = explicit.name
    else:
        weapon = _best_melee_weapon(world)

    from content.actions import start_combat
    return start_combat(world, npc, weapon=weapon)


def _v_shoot(world: "World") -> int:
    npc = world.prso
    if npc is None:
        _say("Shoot what?")
        return M_HANDLED
    bow = _item(world, "bow")
    if not bow or bow.location is not world.player:
        _say("You don't have a bow.")
        return M_HANDLED
    from content.actions import start_combat
    return start_combat(world, npc, weapon="bow")


def _v_drive_stake(world: "World") -> int:
    """DRIVE STAKE INTO WEREWOLF -- the only way to kill the undead werewolf."""
    npc = world.prso
    here = _here_name(world)

    if here != "the-still-den":
        _say("There's nothing to drive a stake into here.")
        return M_HANDLED

    stake = _item(world, "consecrated-stake")
    if not stake or stake.location is not world.player:
        # Try unconsecrated -- doesn't work
        plain = _item(world, "silver-stake")
        if plain and plain.location is world.player:
            _say(
                "You drive the silver stake at the werewolf. "
                "It passes through it like smoke -- or like the stake means nothing without something more. "
                "The werewolf does not seem impressed."
            )
        else:
            _say("You'd need a consecrated silver stake for that.")
        return M_HANDLED

    # Success
    _say(
        "The consecrated silver stake connects.\n"
        "The werewolf does not scream. It simply stops -- mid-motion, mid-purpose, "
        "as though someone cut the thread that was holding it together.\n"
        "It falls.\n"
        "The amulet at its throat catches the torchlight as it goes down."
    )
    world.globals["werewolf_dead"] = True
    # Amulet drops
    amulet = _item(world, "werewolf-amulet")
    if amulet:
        world.move_object(amulet, world.here)
    # XP
    from content.combat import award_combat_xp
    award_combat_xp(world, "werewolf")
    # Quest advancement
    from content.quests import complete
    complete(world, "30")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Economy
# ---------------------------------------------------------------------------

def _v_buy(world: "World") -> int:
    here = _here_name(world)
    obj  = world.prso

    if here in ("tale-and-ale-bar", "tale-and-ale-main"):
        # Ink blocks May's vendor/hint services
        if world.globals.get("inked"):
            from content.traps import check_ink_npc_block
            if check_ink_npc_block(world, "may"):
                return M_HANDLED
        return _buy_at_bar(world, obj)
    if here == "tale-and-ale-kitchen":
        if world.globals.get("inked"):
            from content.traps import check_ink_npc_block
            if check_ink_npc_block(world, "shamus"):
                return M_HANDLED
        return _buy_from_shamus(world, obj)
    _say("There's nothing available to buy here.")
    return M_HANDLED


def _buy_at_bar(world: "World", obj) -> int:
    g = world.globals

    # Hearty stew (Quest 40 unlocks)
    want_stew = obj and "stew" in getattr(obj, "name", "")
    want_food = obj and obj.name in ("food", "meal")
    want_room = obj and obj.name in ("room", "key", "lodging")
    want_drink = (obj is None) or (obj and obj.name in ("drink", "ale", "beer", "wine"))

    if want_room:
        cost = 5
        if _at_full_health(world):
            _say("May stops halfway to the key. \"You're fine. Come back when you're not.\"")
            return M_HANDLED
        if not _deduct_zenni(world, cost):
            return M_HANDLED
        _say("\"Five Zenni,\" May says, and slides a key across the bar. \"Sleep well.\"")
        # Teleport to random guest room
        rooms = ["guest-room-1", "guest-room-2", "guest-room-3"]
        dest = world.rooms.get(random.choice(rooms))
        if dest:
            world.move_object(world.winner, dest)
            world.here = dest
            g["hearts"] = g.get("max_hearts", 5)
            # Bathing included with room
            from content.traps import bathe_ink
            bathe_ink(world)
            world.game.describe_room()
        return M_HANDLED

    if want_stew and g.get("hearty_stew_available"):
        cost = 2
        if _at_full_health(world):
            _say("May glances at you and sets the plate back. \"You don't need it. Come back when you do.\"")
            return M_HANDLED
        if not _deduct_zenni(world, cost):
            return M_HANDLED
        _heal(world, 2)
        _say("A bowl of hearty stew arrives. It's remarkable. Two Zenni.")
        return M_HANDLED

    # Food or drink
    cost = 2
    if _at_full_health(world):
        _say("May glances at you and sets the glass back down. \"You don't need it. Come back when you do.\"")
        return M_HANDLED
    if not _deduct_zenni(world, cost):
        return M_HANDLED
    _heal(world, 1)
    if want_food:
        _say("May calls back to the kitchen and a plate appears shortly after. She sets it in front of you. \"Two Zenni.\"")
    else:
        _say("May sets a glass on the bar and fills it without being asked what you want. Two Zenni.")

    # Free drink flag
    if g.get("free_drink_pending"):
        g["free_drink_pending"] = False
        reason = g.pop("free_drink_reason", "")
        if "mugger" in reason:
            _say(f"May refills without asking. \"On the house. For dealing with whoever that was.\"")
    return M_HANDLED


def _buy_from_shamus(world: "World", obj) -> int:
    if not world.globals.get("shamus_met"):
        _say("Shamus looks up. \"Talk to me first.\"")
        return M_HANDLED

    catalog = {
        "gunpowder":    ("gunpowder", 5),
        "tip-journal":  ("tip-journal", 5),
        "fishing-rod":  ("fishing-rod", 8),
        "torch":        ("torch", 3),
    }

    if obj is None:
        items_list = ", ".join(f"{k} ({v} Zenni)" for k, (_, v) in catalog.items())
        _say(f"Shamus sells: {items_list}.")
        return M_HANDLED

    key = None
    for name in catalog:
        if name in (getattr(obj, "name", "") or ""):
            key = name
            break

    if key is None:
        _say(f"Shamus doesn't carry that.")
        return M_HANDLED

    item_name, cost = catalog[key]
    if not _deduct_zenni(world, cost):
        return M_HANDLED

    item = _item(world, item_name)
    if item is None:
        # Create fresh torch on purchase
        from engine.world import GameObject
        item = GameObject(
            name=item_name,
            synonyms={item_name},
            desc=f"a {item_name}",
            flags=set({TAKEBIT, BURNBIT}),
            size=2,
        )
        world.register_object(item)

    world.move_object(item, world.player)
    _say(f"Shamus hands over the {item_name} without ceremony. {cost} Zenni.")

    if item_name == "torch":
        world.globals["torch_turns_remaining"] = 100
    return M_HANDLED


def _v_tip(world: "World") -> int:
    """TIP MAY [#] -- May's hint system."""
    if _here_name(world) not in ("tale-and-ale-bar", "tale-and-ale-main"):
        _say("You need to be at the bar to tip May.")
        return M_HANDLED

    # Amount parsed from prso or globals["tip_amount"]
    amount = world.globals.pop("tip_amount", None)
    if amount is None:
        obj = world.prso
        if obj is not None:
            # Try to use obj's value as zenni amount
            try:
                amount = int(obj.value)
            except (ValueError, TypeError, AttributeError):
                amount = 1
        else:
            amount = 1

    amount = int(amount)

    if amount > 12:
        _say("May looks genuinely uncomfortable. \"I appreciate the thought, but no.\" She slides it all back. \"Ask me something and we'll talk.\"")
        return M_HANDLED

    if world.globals.get("zenni", 0) < amount:
        _say("May looks at you evenly. \"You're short.\" She goes back to work.")
        return M_HANDLED

    # Determine tier
    if amount <= 3:
        tier = 1
    elif amount <= 6:
        tier = 2
    else:
        tier = 3

    # Get active quests that have hints available
    from content.quests import active_quest_ids
    active = active_quest_ids(world)

    hints_given = world.globals.setdefault("hints_given", {})
    available = [qid for qid in active if hints_given.get(qid, 0) < tier]

    if not available:
        responses = [
            "May pushes the Zenni back. \"Keep it. I've got nothing worth that right now.\" She goes back to wiping the bar.",
            "May looks at the coin and shakes her head slowly. \"I'd be robbing you. Ask me again when something changes.\"",
            "May sets the Zenni on the bar and slides it back. \"Nothing in here worth selling today,\" she says, tapping her temple.",
        ]
        _say(random.choice(responses))
        return M_HANDLED

    world.globals["zenni"] -= amount

    # Pick first available hint quest and advance it
    qid = available[0]
    hints_given[qid] = tier

    tier_intros = {
        1: "May palms the coin without looking at it, leans in, and shares what she knows. \"That's worth something,\" she says.",
        2: "May pockets the coins carefully. \"That buys you something worth hearing,\" she says.",
        3: f"May counts the coins once, pockets them, and leans all the way across the bar. \"{world.globals.get('player_name', 'Friend')},\" she says.",
    }
    _say(tier_intros[tier])

    # Dispatch to per-quest hint text (Phase 7 will fill these in; stub for now)
    from content.actions import may_hint
    may_hint(world, qid, tier)
    return M_HANDLED


def _v_play(world: "World") -> int:
    """PLAY CARGO -- Ty's dice game."""
    if _here_name(world) not in ("tys-casino-corner", "tale-and-ale-main"):
        _say("There's no game to play here.")
        return M_HANDLED

    from content.actions import play_cargo
    return play_cargo(world)


# ---------------------------------------------------------------------------
# Roundabout-specific
# ---------------------------------------------------------------------------

def _v_fish(world: "World") -> int:
    here = _here_name(world)
    if here != "roundabout-pond":
        _say("There's no good fishing here.")
        return M_HANDLED

    rod = _item(world, "fishing-rod")
    if not rod or rod.location is not world.player:
        _say("You'd need a fishing rod.")
        return M_HANDLED

    if world.globals.get("pond_fished"):
        _say("The pond is quiet. You've already retrieved what was here.")
        return M_HANDLED

    from content.player import check_fishing
    # Rogues get a bonus; base difficulty 9
    success = check_fishing(world, 9)

    if success:
        world.globals["pond_fished"] = True
        # Ship-in-a-bottle is the trophy item; bottle is the quest item
        bottle = _item(world, "ship-in-a-bottle")
        if bottle is None:
            from engine.world import GameObject
            bottle = GameObject(
                name="ship-in-a-bottle",
                synonyms={"ship in a bottle", "bottle", "ship"},
                desc="a ship-in-a-bottle",
                ldesc="A glass bottle, sealed with wax. A fully-rigged ship inside.",
                flags=set({TAKEBIT}),
                size=2,
                value=24,
            )
            world.register_object(bottle)
        world.move_object(bottle, world.player)
        _say(
            "Your line snags something heavy. "
            "After some effort a glass bottle breaks the surface -- sealed with wax, "
            "a fully-rigged ship visible inside. You have no idea how it got down there."
        )
    else:
        _say("You fish for a while. Nothing bites.")
    return M_HANDLED


def _v_sail(world: "World") -> int:
    here = _here_name(world)
    if not world.globals.get("at_sea") and here not in ("pie-rat-ship-deck",):
        _say("You'd need to be aboard a ship to sail.")
        return M_HANDLED

    # Determine direction from prso
    obj = world.prso
    direction = None
    if obj:
        n = getattr(obj, "name", "") or ""
        for d in ("north", "south", "east", "west"):
            if d in n:
                direction = d
                break

    if direction is None:
        direction = "east"  # default: set sail = east

    # SAIL: move ship through sea rooms
    world.globals["at_sea"] = True
    world.game.do_walk(world, direction)
    return M_HANDLED


def _v_dock(world: "World") -> int:
    if not world.globals.get("at_sea"):
        _say("You'd need to be at sea to dock.")
        return M_HANDLED
    # Return to docks
    docks = world.rooms.get("the-docks")
    if docks:
        world.move_object(world.winner, docks)
        world.here = docks
        world.globals["at_sea"] = False
        world.globals["ship_stolen"] = False  # returned
        world.game.describe_room()
        # Quest: returning stolen ship
        from content.quests import is_complete, complete
        if not is_complete(world, "22"):
            pass  # ship return quest handled in actions
    return M_HANDLED


def _v_pray(world: "World") -> int:
    here = _here_name(world)
    if here in ("church-nave", "the-altar"):
        dial = world.globals.get("altar_dial_setting", "none")
        _say(f"You bow your head before the altar. The dial is set to {dial.replace('-', ' ').title()}.")
        # Ritual prayers dispatched through ring ritual quest chain
        from content.actions import altar_pray
        return altar_pray(world, dial)
    if here == "ritual-circle":
        _say("You bow your head within the circle of stones. The runes respond with a faint warmth.")
        return M_HANDLED
    _say("You bow your head. The moment passes without incident.")
    return M_HANDLED


def _v_cast(world: "World") -> int:
    obj = world.prso
    here = _here_name(world)
    g   = world.globals

    # Determine spell from prso name or prsi
    spell = None
    if obj:
        n = getattr(obj, "name", "") or ""
        if "light" in n:
            spell = "light"
        elif "unbind" in n or "undead" in n:
            spell = "unbind_undead"
        elif "fireball" in n or "fire" in n:
            spell = "fireball"
        elif "rest" in n:
            spell = "rest"

    if spell is None:
        _say("Cast what spell?")
        return M_HANDLED

    # Light spell
    if spell == "light":
        if not g.get("spell_light"):
            _say("You don't know the Light spell.")
            return M_HANDLED
        cooldown = g.get("light_spell_cooldown", 0)
        if cooldown > 0:
            _say(f"The spell needs {cooldown} more turns before you can cast it again.")
            return M_HANDLED
        g["light_spell_active"] = True
        g["light_spell_active_turns"] = 10
        g["light_spell_cooldown"] = 20
        _say("You cast Light. The darkness retreats.")
        return M_HANDLED

    # Unbind Undead
    if spell == "unbind_undead":
        if not g.get("spell_unbind_undead"):
            _say("You don't know Unbind Undead.")
            return M_HANDLED
        cooldown = g.get("unbind_cooldown", 0)
        if cooldown > 0:
            _say(f"The spell needs {cooldown} more turns to recharge.")
            return M_HANDLED
        if here == "ghosts-room":
            from content.actions import unbind_ghost
            return unbind_ghost(world)
        _say("The spell finds nothing here to unbind.")
        return M_HANDLED

    # Fireball -- combat only
    if spell == "fireball":
        if not g.get("spell_fireball"):
            _say("You don't know Fireball.")
            return M_HANDLED
        cooldown = g.get("fireball_cooldown", 0)
        if cooldown > 0:
            _say(f"The fireball needs {cooldown} more turns to recharge.")
            return M_HANDLED
        npc = world.prsi
        if npc is None:
            _say("Cast fireball at what?")
            return M_HANDLED
        from content.actions import start_combat
        return start_combat(world, npc, weapon="fireball")

    # REST
    if spell == "rest":
        return _v_rest(world)

    _say("That spell doesn't do anything here.")
    return M_HANDLED


def _v_rest(world: "World") -> int:
    g = world.globals
    if not g.get("spell_rest"):
        _say("What are you sitting around for, there's a dungeon to explore!")
        return M_HANDLED

    # Check for hostile NPC in room
    for obj in getattr(world.here, "contents", []):
        if obj.has_flag(ACTORBIT) and world.globals.get(f"hostile_{obj.name}"):
            _say("You can't rest now, there's fighting to be done!")
            return M_HANDLED

    cooldown = g.get("rest_cooldown", 0)
    if cooldown > 0:
        _say("What are you sitting around for, there's a dungeon to explore!")
        return M_HANDLED

    if _at_full_health(world):
        _say("You rest briefly. You feel fine already.")
        return M_HANDLED

    _heal(world, 1)
    g["rest_cooldown"] = 50
    _say("You sit. The weariness doesn't go away exactly, but it gets quieter. You feel somewhat restored.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

def _v_jump(world: "World") -> int:
    obj  = world.prso
    here = _here_name(world)

    # JUMP ON PLATE -- deliberate bell plate trigger (Trap 29)
    if obj and obj.name in ("plate", "pressure-plate") and here == "combat-room":
        from content.traps import trigger_bell_plate_deliberate
        trigger_bell_plate_deliberate(world)
        return M_HANDLED

    _say("You jump. Nothing interesting happens.")
    return M_HANDLED


def _v_swim(world: "World") -> int:
    here = _here_name(world)
    if here in ("roundabout-pond", "roundabout-beach") or world.globals.get("at_sea"):
        _say("The water is cold and uninviting. You decide against it.")
        return M_HANDLED
    if here == "cellar-storeroom" and not world.globals.get("cellar_drained"):
        _say(
            "The water is dark and knee-deep. You wade in. "
            "The far wall has a door -- but it opens onto rushing water. Entering would be fatal."
        )
        return M_HANDLED
    _say("There's no suitable water to swim in here.")
    return M_HANDLED


def _v_cross(world: "World") -> int:
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Flavor
# ---------------------------------------------------------------------------

def _v_smell(world: "World") -> int:
    here = _here_name(world)
    if "bog" in here or here in ("bog-se", "bog-ne", "bog-sw", "bog-nw"):
        _say("The smell is comprehensive and personal.")
        return M_HANDLED
    if "cellar" in here:
        _say("Damp. Old wood. Something you cannot identify.")
        return M_HANDLED
    _say("You detect no unusual odors.")
    return M_HANDLED


def _v_listen(world: "World") -> int:
    here = _here_name(world)
    if here == "echo-alcove":
        _say("A faint grinding drifts up from somewhere far below -- bone on stone.")
        return M_HANDLED
    _say("You hear nothing unusual.")
    return M_HANDLED


def _v_stand(world: "World") -> int:
    _say("You are already standing.")
    return M_HANDLED


def _v_curse(world: "World") -> int:
    _say("Such language.")
    return M_HANDLED


def _v_wish(world: "World") -> int:
    _say("Your wish hangs in the air, unanswered.")
    return M_HANDLED


def _v_burn(world: "World") -> int:
    _say("You'd need a flame for that.")
    return M_HANDLED


def _v_knock(world: "World") -> int:
    _say("You knock. No answer.")
    return M_HANDLED


def _v_disarm(world: "World") -> int:
    obj  = world.prso
    here = _here_name(world)

    # Portcullis (Trap 19)
    if here == "portcullis-corridor" and (obj is None or obj.name in ("portcullis", "mechanism", "panel")):
        from content.traps import disarm_portcullis
        disarm_portcullis(world)
        return M_HANDLED

    # Bell plate (Trap 29)
    if here == "combat-room" and (obj is None or obj.name in ("plate", "pressure-plate")):
        from content.traps import disarm_bell_plate
        disarm_bell_plate(world)
        return M_HANDLED

    _say("There's nothing to disarm here.")
    return M_HANDLED


def _v_bathe(world: "World") -> int:
    here = _here_name(world)
    if here in ("inn-room", "guest-room-1", "guest-room-2", "guest-room-3", "inn-bathroom"):
        from content.traps import bathe_ink
        bathe_ink(world)
        return M_HANDLED
    _say("There's no place to bathe here. The inn has a bath -- five Zenni for a room.")
    return M_HANDLED
