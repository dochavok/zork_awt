"""
Verb handler registration for Zork I.

Reads verb routines from gverbs.zil and 1actions.zil and registers them with
the Game instance via game.register_verb() and game.register_preaction().
"""

from __future__ import annotations

import json
import random
from typing import TYPE_CHECKING

from engine.game import (
    M_FATAL, M_HANDLED, M_NOT_HANDLED,
    VERBOSE, BRIEF, SUPER_BRIEF,
)
from engine.world import (
    TAKEBIT, CONTBIT, OPENBIT, ACTORBIT, WEAPONBIT, WEARBIT,
    TOUCHBIT, BURNBIT, NDESCBIT, TOOLBIT, ONBIT, DOORBIT, SURFACEBIT,
    TRYTAKEBIT, TRANSBIT,
)

if TYPE_CHECKING:
    from engine.game import Game
    from engine.world import World


# NONLANDBIT: set on water/boat rooms where grues don't go
NONLANDBIT = "NONLANDBIT"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _verb(world: "World", *verbs: str) -> bool:
    return world.prsa in verbs


def _obj(world: "World", name: str):
    return world.objects.get(name)


def _flag(world: "World", name: str) -> bool:
    return bool(world.get_global(name))


# ---------------------------------------------------------------------------
# Meta-verb handlers
# ---------------------------------------------------------------------------

def _v_verbose(world: "World") -> int:
    world.game.desc_mode = VERBOSE
    print("Maximum verbosity.")
    return M_HANDLED


def _v_brief(world: "World") -> int:
    world.game.desc_mode = BRIEF
    print("Brief descriptions.")
    return M_HANDLED


def _v_super_brief(world: "World") -> int:
    world.game.desc_mode = SUPER_BRIEF
    print("Superbrief descriptions.")
    return M_HANDLED


def _v_look(world: "World") -> int:
    world.game.describe_room()
    return M_HANDLED


def _v_inventory(world: "World") -> int:
    winner = world.winner
    if winner is None or not list(winner.contents):
        print("You are empty-handed.")
        return M_HANDLED
    print("You are carrying:")
    for obj in winner.contents:
        if obj.has_flag(WEARBIT):
            print(f"  A {obj.desc} (being worn)")
        else:
            print(f"  A {obj.desc}")
        if obj.has_flag(CONTBIT) and obj.has_flag(OPENBIT):
            for inner in obj.contents:
                print(f"    A {inner.desc}")
    return M_HANDLED


def _v_quit(world: "World") -> int:
    _v_score(world)
    ans = input("Do you wish to leave the game? (Y is affirmative): ").strip().lower()
    if ans.startswith("y"):
        world.game.quit()
        return M_FATAL
    print("Ok.")
    return M_HANDLED


def _v_restart(world: "World") -> int:
    ans = input("Do you wish to restart? (Y is affirmative): ").strip().lower()
    if ans.startswith("y"):
        print("Restarting.")
        world.game.quit()
        return M_FATAL
    return M_HANDLED


_DEFAULT_SAVE_FILE = "zork.sav"


def _save_state(world: "World") -> dict:
    clock = world.game.clock

    obj_states = {}
    for name, obj in world.objects.items():
        loc = obj._location
        obj_states[name] = {
            "location": loc.name if loc is not None else None,
            "flags": sorted(obj.flags),
            "value": obj.value,
            "tvalue": obj.tvalue,
            "touched": obj.touched,
        }

    room_states = {}
    for name, room in world.rooms.items():
        room_states[name] = {
            "flags": sorted(room.flags),
            "visited": room.visited,
            "value": room.value,
        }

    clock_states = {}
    for name, event in clock._events.items():
        clock_states[name] = {"ticks": event.ticks, "enabled": event.enabled}

    return {
        "score": world.score,
        "score_max": world.score_max,
        "moves": world.moves,
        "here": world.here.name if world.here else None,
        "globals": dict(world.globals),
        "objects": obj_states,
        "rooms": room_states,
        "clock": clock_states,
    }


def _restore_state(world: "World", state: dict) -> None:
    clock = world.game.clock

    world.score = state["score"]
    world.score_max = state["score_max"]
    world.moves = state["moves"]
    world.globals = dict(state["globals"])

    here_name = state.get("here")
    if here_name:
        world.here = world.rooms[here_name]

    for name, obj_state in state["objects"].items():
        obj = world.objects.get(name)
        if obj is None:
            continue
        obj.flags = set(obj_state["flags"])
        obj.value = obj_state["value"]
        obj.tvalue = obj_state["tvalue"]
        obj.touched = obj_state["touched"]
        loc_name = obj_state["location"]
        if loc_name is None:
            new_loc = None
        elif loc_name in world.rooms:
            new_loc = world.rooms[loc_name]
        else:
            new_loc = world.objects.get(loc_name)
        world.move_object(obj, new_loc)

    for name, room_state in state["rooms"].items():
        room = world.rooms.get(name)
        if room is None:
            continue
        room.flags = set(room_state["flags"])
        room.visited = room_state["visited"]
        room.value = room_state["value"]

    for name, ev_state in state["clock"].items():
        event = clock._events.get(name)
        if event is None:
            continue
        event.ticks = ev_state["ticks"]
        event.enabled = ev_state["enabled"]


def _v_save(world: "World") -> int:
    path = str(world.get_global("SAVE-FILE") or _DEFAULT_SAVE_FILE)
    try:
        state = _save_state(world)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f)
        print("Saved.")
    except OSError as e:
        print(f"Save failed: {e}")
    return M_HANDLED


def _v_restore(world: "World") -> int:
    path = str(world.get_global("SAVE-FILE") or _DEFAULT_SAVE_FILE)
    try:
        with open(path, "r", encoding="utf-8") as f:
            state = json.load(f)
        _restore_state(world, state)
        print("Restored.")
    except (OSError, KeyError, ValueError) as e:
        print(f"Restore failed: {e}")
    return M_HANDLED


def _v_score(world: "World") -> int:
    score = world.score
    moves = world.moves
    score_max = world.score_max
    move_word = "move" if moves == 1 else "moves"
    print(f"Your score is {score} (total of {score_max} points), in {moves} {move_word}.")
    _score_rank(score)
    return M_HANDLED


def _score_rank(score: int) -> None:
    if score == 350:
        rank = "Master Adventurer"
    elif score > 330:
        rank = "Wizard"
    elif score > 300:
        rank = "Master"
    elif score > 200:
        rank = "Adventurer"
    elif score > 100:
        rank = "Junior Adventurer"
    elif score > 50:
        rank = "Novice Adventurer"
    elif score > 25:
        rank = "Amateur Adventurer"
    else:
        rank = "Beginner"
    print(f"This gives you the rank of {rank}.")


def _v_version(world: "World") -> int:
    print(
        "ZORK I: The Great Underground Empire\n"
        "Infocom interactive fiction - a fantasy story\n"
        "Copyright (c) 1981, 1982, 1983, 1984, 1985, 1986 Infocom, Inc. All rights reserved.\n"
        "ZORK is a registered trademark of Infocom, Inc."
    )
    return M_HANDLED


def _v_script(world: "World") -> int:
    print("Scripting is not implemented in this version.")
    return M_HANDLED


def _v_unscript(world: "World") -> int:
    print("Scripting is not implemented in this version.")
    return M_HANDLED


def _v_diagnose(world: "World") -> int:
    print("You are in perfect health.")
    return M_HANDLED


def _v_wait(world: "World") -> int:
    print("Time passes...")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Object verb handlers
# ---------------------------------------------------------------------------

def _v_take(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None or winner is None:
        print("Take what?")
        return M_HANDLED
    if prso.location is winner:
        if prso.has_flag(WEARBIT):
            print("You are already wearing it.")
        else:
            print("You already have that!")
        return M_HANDLED
    loc = prso.location
    if loc is not None and hasattr(loc, "has_flag"):
        if loc.has_flag(CONTBIT) and not loc.has_flag(OPENBIT):
            print("You can't reach something that's inside a closed container.")
            return M_HANDLED
    if not prso.has_flag(TAKEBIT):
        if prso.has_flag(TRYTAKEBIT):
            print(f"You can't take the {prso.desc}.")
        else:
            print(f"You can't take that!")
        return M_HANDLED
    world.move_object(prso, winner)
    # Award value points the first time a treasure is picked up (ZIL SCORE-OBJ).
    if getattr(prso, "tvalue", 0) > 0:
        score_obj(world, prso)
    prso.set_flag(TOUCHBIT)
    if prso.has_flag(WEARBIT):
        print(f"You are now wearing the {prso.desc}.")
    else:
        print("Taken.")
    return M_HANDLED


def _pre_take(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None:
        return M_NOT_HANDLED
    if winner and prso.location is winner:
        if prso.has_flag(WEARBIT):
            print("You are already wearing it.")
        else:
            print("You already have that!")
        return M_HANDLED
    loc = prso.location
    if loc is not None and hasattr(loc, "has_flag"):
        if loc.has_flag(CONTBIT) and not loc.has_flag(OPENBIT):
            print("You can't reach something that's inside a closed container.")
            return M_HANDLED
    prsi = world.prsi
    if prsi is not None:
        ground = _obj(world, "GROUND")
        if ground and prsi is ground:
            world.prsi = None
            return M_NOT_HANDLED
        if prso.location is not prsi:
            print(f"The {prso.desc} isn't in the {prsi.desc}.")
            return M_HANDLED
        world.prsi = None
    return M_NOT_HANDLED


def _v_drop(world: "World") -> int:
    prso = world.prso
    here = world.here
    winner = world.winner
    if prso is None:
        print("Drop what?")
        return M_HANDLED
    if winner and prso.location is not winner:
        print("You don't have that!")
        return M_HANDLED
    if here:
        world.move_object(prso, here)
    print("Dropped.")
    return M_HANDLED


def _pre_drop(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None:
        return M_NOT_HANDLED
    if winner and prso is winner.location:
        world.game.perform("V-DISEMBARK", prso)
        return M_HANDLED
    return M_NOT_HANDLED


def _v_examine(world: "World") -> int:
    prso = world.prso
    if prso is None:
        print("Examine what?")
        return M_HANDLED
    text = getattr(prso, "text", None)
    if text:
        print(text)
        return M_HANDLED
    if prso.has_flag(CONTBIT) or prso.has_flag(DOORBIT):
        return _v_look_inside(world)
    print(f"There's nothing special about the {prso.desc}.")
    return M_HANDLED


def _v_look_inside(world: "World") -> int:
    prso = world.prso
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(DOORBIT) and not prso.has_flag(CONTBIT):
        if prso.has_flag(OPENBIT):
            print(f"The {prso.desc} is open, but I can't tell what's beyond it.")
        else:
            print(f"The {prso.desc} is closed.")
        return M_HANDLED
    if prso.has_flag(CONTBIT):
        if prso.has_flag(ACTORBIT):
            print("There is nothing special to be seen.")
            return M_HANDLED
        can_see = prso.has_flag(OPENBIT) or prso.has_flag(TRANSBIT)
        if can_see:
            items = [o for o in prso.contents]
            if not items:
                if prso.has_flag(SURFACEBIT):
                    print(f"There is nothing on the {prso.desc}.")
                else:
                    print(f"The {prso.desc} is empty.")
            else:
                print(f"The {prso.desc} contains:")
                for item in items:
                    print(f"  A {item.desc}")
        else:
            print(f"The {prso.desc} is closed.")
        return M_HANDLED
    print(f"You can't look inside a {prso.desc}.")
    return M_HANDLED


def _v_open(world: "World") -> int:
    prso = world.prso
    if prso is None:
        print("Open what?")
        return M_HANDLED
    if prso.has_flag(CONTBIT) and getattr(prso, "capacity", 0) != 0:
        if prso.has_flag(OPENBIT):
            print("It is already open.")
            return M_HANDLED
        prso.set_flag(OPENBIT)
        prso.set_flag(TOUCHBIT)
        items = [o for o in prso.contents]
        if not items or prso.has_flag(TRANSBIT):
            print("Opened.")
        elif len(items) == 1 and not items[0].has_flag(TOUCHBIT) and items[0].fdesc:
            print(f"The {prso.desc} opens.")
            print(items[0].fdesc)
        else:
            names = ", ".join(f"a {o.desc}" for o in items)
            print(f"Opening the {prso.desc} reveals {names}.")
        return M_HANDLED
    if prso.has_flag(DOORBIT):
        if prso.has_flag(OPENBIT):
            print("It is already open.")
        else:
            prso.set_flag(OPENBIT)
            print(f"The {prso.desc} opens.")
        return M_HANDLED
    print(f"You must tell me how to do that to a {prso.desc}.")
    return M_HANDLED


def _v_close(world: "World") -> int:
    prso = world.prso
    if prso is None:
        print("Close what?")
        return M_HANDLED
    if prso.has_flag(CONTBIT) and getattr(prso, "capacity", 0) != 0:
        if prso.has_flag(OPENBIT):
            prso.clear_flag(OPENBIT)
            print("Closed.")
            if not world.is_lit():
                print("It is now pitch black.")
        else:
            print("It is already closed.")
        return M_HANDLED
    if prso.has_flag(DOORBIT):
        if prso.has_flag(OPENBIT):
            prso.clear_flag(OPENBIT)
            print(f"The {prso.desc} is now closed.")
        else:
            print("It is already closed.")
        return M_HANDLED
    print("You cannot close that.")
    return M_HANDLED


def _v_put(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    winner = world.winner
    if prso is None or prsi is None:
        print("Put what where?")
        return M_HANDLED
    if not prsi.has_flag(OPENBIT):
        print(f"The {prsi.desc} isn't open.")
        return M_HANDLED
    if prso is prsi:
        print("How can you do that?")
        return M_HANDLED
    if prso.location is prsi:
        print(f"The {prso.desc} is already in the {prsi.desc}.")
        return M_HANDLED
    cap = getattr(prsi, "capacity", 0)
    sz = getattr(prso, "size", 5)
    cur_weight = sum(getattr(o, "size", 5) for o in prsi.contents)
    if cap > 0 and cur_weight + sz > cap:
        print("There's no room.")
        return M_HANDLED
    if winner and prso.location is not winner and prso.has_flag(TRYTAKEBIT):
        print(f"You don't have the {prso.desc}.")
        return M_HANDLED
    world.move_object(prso, prsi)
    prso.set_flag(TOUCHBIT)
    print("Done.")
    return M_HANDLED


def _pre_put(world: "World") -> int:
    return _pre_give(world)


def _pre_give(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None:
        return M_NOT_HANDLED
    if winner and prso.location is not winner:
        print(f"That's easy for you to say since you don't even have the {prso.desc}.")
        return M_HANDLED
    return M_NOT_HANDLED


def _v_give(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prsi is None:
        print("Give it to whom?")
        return M_HANDLED
    if not prsi.has_flag(ACTORBIT):
        print(f"You can't give a {prso.desc if prso else 'thing'} to a {prsi.desc}!")
        return M_HANDLED
    print(f"The {prsi.desc} refuses it politely.")
    return M_HANDLED


def _v_attack(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    winner = world.winner
    if prso is None:
        print("Attack what?")
        return M_HANDLED
    if not prso.has_flag(ACTORBIT):
        print(f"I've known strange people, but fighting a {prso.desc}?")
        return M_HANDLED
    if prsi is None:
        hands = _obj(world, "HANDS")
        if hands:
            prsi = hands
    if prsi is None or (hasattr(prsi, "name") and prsi.name == "HANDS"):
        print(f"Trying to attack a {prso.desc} with your bare hands is suicidal.")
        return M_HANDLED
    if winner and prsi.location is not winner:
        print(f"You aren't even holding the {prsi.desc}.")
        return M_HANDLED
    if not prsi.has_flag(WEAPONBIT):
        print(f"Trying to attack the {prso.desc} with a {prsi.desc} is suicidal.")
        return M_HANDLED
    print(f"You swing the {prsi.desc} at the {prso.desc} but miss.")
    return M_HANDLED


def _v_throw(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    winner = world.winner
    if prso is None:
        print("Throw what?")
        return M_HANDLED
    if winner and prso.location is not winner:
        print("You don't have that!")
        return M_HANDLED
    here = world.here
    me = _obj(world, "ME")
    if prsi and me and prsi is me:
        world.game.jigs_up(
            f"A terrific throw! The {prso.desc} hits you squarely in the head. Normally,\n"
            "this wouldn't do much damage, but by incredible mischance, you fall over\n"
            "backwards trying to duck, and break your neck, justice being swift and\n"
            "merciful in the Great Underground Empire."
        )
        return M_FATAL
    if prsi and prsi.has_flag(ACTORBIT):
        if here:
            world.move_object(prso, here)
        print(f"The {prsi.desc} ducks as the {prso.desc} flies by and crashes to the ground.")
        return M_HANDLED
    if here:
        world.move_object(prso, here)
    print("Thrown.")
    return M_HANDLED


def _v_burn(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    winner = world.winner
    if prsi is None:
        print("You didn't say with what!")
        return M_HANDLED
    flamebit = "FLAMEBIT"
    onbit = ONBIT
    if not (prsi.has_flag(flamebit) and prsi.has_flag(onbit)):
        print(f"With a {prsi.desc}??!?")
        return M_HANDLED
    if prso is None:
        return M_NOT_HANDLED
    if not prso.has_flag(BURNBIT):
        print(f"You can't burn a {prso.desc}.")
        return M_HANDLED
    if winner and (prso.location is winner or winner.location is prso):
        if winner.location is prso:
            action = "in"
        else:
            action = "holding"
        world.remove_object(prso)
        world.game.jigs_up(
            f"The {prso.desc} catches fire. Unfortunately, you were {action} it at the time."
        )
        return M_FATAL
    world.remove_object(prso)
    print(f"The {prso.desc} catches fire and is consumed.")
    return M_HANDLED


def _pre_burn(world: "World") -> int:
    prsi = world.prsi
    if not prsi:
        print("You didn't say with what!")
        return M_HANDLED
    flamebit = "FLAMEBIT"
    if prsi.has_flag(flamebit) and prsi.has_flag(ONBIT):
        return M_NOT_HANDLED
    print(f"With a {prsi.desc}??!?")
    return M_HANDLED


def _v_eat(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    foodbit = "FOODBIT"
    drinkbit = "DRINKBIT"
    if prso is None:
        print("Eat what?")
        return M_HANDLED
    if prso.has_flag(foodbit):
        if winner and prso.location is not winner and (prso.location is None or prso.location.location is not winner):
            print("You're not holding that.")
            return M_HANDLED
        print("Thank you very much. It really hit the spot.")
        world.remove_object(prso)
        return M_HANDLED
    if prso.has_flag(drinkbit):
        print("Thank you very much. I was rather thirsty (from all this talking, probably).")
        return M_HANDLED
    print(f"I don't think that the {prso.desc} would agree with you.")
    return M_HANDLED


def _v_drink(world: "World") -> int:
    return _v_eat(world)


def _v_read(world: "World") -> int:
    prso = world.prso
    if prso is None:
        print("Read what?")
        return M_HANDLED
    if not world.is_lit():
        print("It is impossible to read in the dark.")
        return M_HANDLED
    text = getattr(prso, "text", None)
    if text:
        print(text)
        return M_HANDLED
    if not prso.has_flag("READBIT"):
        print(f"How does one read a {prso.desc}?")
        return M_HANDLED
    print(f"There's nothing written on the {prso.desc}.")
    return M_HANDLED


def _pre_read(world: "World") -> int:
    if not world.is_lit():
        print("It is impossible to read in the dark.")
        return M_HANDLED
    prsi = world.prsi
    if prsi and not prsi.has_flag(TRANSBIT):
        print(f"How does one look through a {prsi.desc}?")
        return M_HANDLED
    return M_NOT_HANDLED


def _v_find(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None:
        print("Find what?")
        return M_HANDLED
    hands = _obj(world, "HANDS")
    lungs = _obj(world, "LUNGS")
    me = _obj(world, "ME")
    if hands and prso is hands or lungs and prso is lungs:
        print("Within six feet of your head, assuming you haven't left that somewhere.")
        return M_HANDLED
    if me and prso is me:
        print("You're around here somewhere...")
        return M_HANDLED
    global_objects = _obj(world, "GLOBAL-OBJECTS")
    if global_objects and prso.location is global_objects:
        print("You find it.")
        return M_HANDLED
    if winner and prso.location is winner:
        print("You have it.")
        return M_HANDLED
    here = world.here
    if here and (prso.location is here or prso.name in [o.name for o in here.global_objects]):
        print("It's right here.")
        return M_HANDLED
    loc = prso.location
    if loc is not None and hasattr(loc, "has_flag"):
        if loc.has_flag(ACTORBIT):
            print(f"The {loc.desc} has it.")
            return M_HANDLED
        if loc.has_flag(SURFACEBIT):
            print(f"It's on the {loc.desc}.")
            return M_HANDLED
        if loc.has_flag(CONTBIT):
            print(f"It's in the {loc.desc}.")
            return M_HANDLED
    print("Beats me.")
    return M_HANDLED


def _v_move(world: "World") -> int:
    prso = world.prso
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(TAKEBIT):
        print(f"Moving the {prso.desc} reveals nothing.")
        return M_HANDLED
    print(f"You can't move the {prso.desc}.")
    return M_HANDLED


def _pre_move(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None:
        return M_NOT_HANDLED
    if winner and prso.location is winner:
        print("You aren't an accomplished enough juggler.")
        return M_HANDLED
    return M_NOT_HANDLED


def _v_shake(world: "World") -> int:
    prso = world.prso
    here = world.here
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(ACTORBIT):
        print("This seems to have no effect.")
        return M_HANDLED
    if not prso.has_flag(TAKEBIT):
        print(f"You can't take it; thus, you can't shake it!")
        return M_HANDLED
    if prso.has_flag(CONTBIT):
        if prso.has_flag(OPENBIT):
            items = list(prso.contents)
            if items:
                for item in items:
                    item.set_flag(TOUCHBIT)
                    if here:
                        world.move_object(item, here)
                print(f"The contents of the {prso.desc} spill to the ground.")
            else:
                print("Shaken.")
        else:
            items = list(prso.contents)
            if items:
                print(f"It sounds like there is something inside the {prso.desc}.")
            else:
                print(f"The {prso.desc} sounds empty.")
        return M_HANDLED
    print("Shaken.")
    return M_HANDLED


def _v_turn(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prso is None:
        return M_NOT_HANDLED
    if prsi is None or prsi is _obj(world, "ROOMS"):
        print("Your bare hands don't appear to be enough.")
        return M_HANDLED
    if not prso.has_flag("TURNBIT"):
        print("You can't turn that!")
        return M_HANDLED
    print("This has no effect.")
    return M_HANDLED


def _pre_turn(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prso is None:
        return M_NOT_HANDLED
    book = _obj(world, "BOOK")
    rooms = _obj(world, "ROOMS")
    if (prsi is None or prsi is rooms) and not (book and prso is book):
        print("Your bare hands don't appear to be enough.")
        return M_HANDLED
    if not prso.has_flag("TURNBIT"):
        print("You can't turn that!")
        return M_HANDLED
    return M_NOT_HANDLED


def _v_lock(world: "World") -> int:
    print("It doesn't seem to work.")
    return M_HANDLED


def _v_unlock(world: "World") -> int:
    return _v_lock(world)


def _v_tie(world: "World") -> int:
    prsi = world.prsi
    winner = world.winner
    if prsi and winner and prsi is winner:
        print("You can't tie anything to yourself.")
        return M_HANDLED
    prso = world.prso
    print(f"You can't tie the {prso.desc if prso else 'that'} to that.")
    return M_HANDLED


def _v_untie(world: "World") -> int:
    print("This cannot be tied, so it cannot be untied!")
    return M_HANDLED


def _v_wear(world: "World") -> int:
    prso = world.prso
    if prso is None:
        return M_NOT_HANDLED
    if not prso.has_flag(WEARBIT):
        print(f"You can't wear the {prso.desc}.")
        return M_HANDLED
    world.game.perform("V-TAKE", prso)
    return M_HANDLED


def _v_push(world: "World") -> int:
    prso = world.prso
    print(f"Pushing the {prso.desc if prso else 'that'} has no effect.")
    return M_HANDLED


def _v_pull(world: "World") -> int:
    prso = world.prso
    print(f"Pulling the {prso.desc if prso else 'that'} has no effect.")
    return M_HANDLED


def _v_wave(world: "World") -> int:
    prso = world.prso
    print(f"Waving the {prso.desc if prso else 'that'} has no effect.")
    return M_HANDLED


def _v_rub(world: "World") -> int:
    prso = world.prso
    print(f"Fiddling with the {prso.desc if prso else 'that'} has no effect.")
    return M_HANDLED


def _v_smell(world: "World") -> int:
    prso = world.prso
    if prso:
        print(f"It smells like a {prso.desc}.")
    else:
        print("You smell nothing unusual.")
    return M_HANDLED


def _v_listen(world: "World") -> int:
    prso = world.prso
    if prso:
        print(f"The {prso.desc} makes no sound.")
    else:
        print("You hear nothing unusual.")
    return M_HANDLED


def _v_climb(world: "World") -> int:
    prso = world.prso
    here = world.here
    if prso and prso.has_flag("CLIMBBIT"):
        if here and here.name == "PATH":
            world.game.do_walk("up")
            return M_HANDLED
        if here:
            up_exit = here.exits.get("up")
            if up_exit:
                world.game.do_walk("up")
                return M_HANDLED
        print(f"There are no climbable trees here.")
        return M_HANDLED
    if prso:
        print(f"You can't climb the {prso.desc}.")
    else:
        print("What do you want to climb?")
    return M_HANDLED


def _v_swim(world: "World") -> int:
    here = world.here
    if here and here.has_flag("GLOBAL-WATER"):
        print("Swimming isn't usually allowed in the dungeon.")
        return M_HANDLED
    global_water = _obj(world, "GLOBAL-WATER")
    if global_water and here and global_water in here.global_objects:
        print("Swimming isn't usually allowed in the dungeon.")
        return M_HANDLED
    print("Go jump in a lake!")
    return M_HANDLED


def _v_jump(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"The {prso.desc} is too big to jump over.")
        return M_HANDLED
    here = world.here
    if here:
        down_exit = here.exits.get("down")
        if down_exit and down_exit.destination is None and down_exit.message:
            print("This was not a very safe place to try jumping.")
            world.game.jigs_up("You should have looked before you leaped.")
            return M_FATAL
    import random
    msgs = [
        "Very good. Now you can go to the second grade.",
        "Are you enjoying yourself?",
        "Wheeeeeeeeee!!!!!",
        "Do you expect me to applaud?",
    ]
    print(random.choice(msgs))
    return M_HANDLED


def _v_wait(world: "World") -> int:
    print("Time passes...")
    return M_HANDLED


def _v_say(world: "World") -> int:
    here = world.here
    if here:
        for obj in list(here.contents) + list(here.global_objects):
            if obj.has_flag(ACTORBIT):
                print(f"You must address the {obj.desc} directly.")
                return M_HANDLED
    print("Talking to yourself is a sign of impending mental collapse.")
    return M_HANDLED


def _v_hello(world: "World") -> int:
    prso = world.prso
    if prso:
        if prso.has_flag(ACTORBIT):
            print(f"The {prso.desc} bows his head to you in greeting.")
        else:
            print(f"It's a well known fact that only schizophrenics say \"Hello\" to a {prso.desc}.")
        return M_HANDLED
    import random
    greetings = [
        "Hello.",
        "Good day.",
        "Howdy.",
        "Hi there.",
    ]
    print(random.choice(greetings))
    return M_HANDLED


def _v_yell(world: "World") -> int:
    print("Aaaarrrrgggghhhh!")
    return M_HANDLED


def _v_pray(world: "World") -> int:
    here = world.here
    if here and here.name == "SOUTH-TEMPLE":
        forest1 = world.rooms.get("FOREST-1")
        if forest1:
            world.game.enter_room(forest1)
        return M_HANDLED
    print("If you pray enough, your prayers may be answered.")
    return M_HANDLED


def _v_odysseus(world: "World") -> int:
    here = world.here
    cyclops = _obj(world, "CYCLOPS")
    if here and here.name == "CYCLOPS-ROOM" and cyclops and cyclops.location is here and not _flag(world, "CYCLOPS-FLAG"):
        world.set_global("CYCLOPS-FLAG", True)
        world.set_global("MAGIC-FLAG", True)
        print(
            "The cyclops, hearing the name of his father's deadly nemesis, flees the room\n"
            "by knocking down the wall on the east of the room."
        )
        if cyclops:
            world.move_object(cyclops, None)
        return M_HANDLED
    print("Wasn't he a sailor?")
    return M_HANDLED


def _v_frobozz(world: "World") -> int:
    print("The FROBOZZ Corporation created, owns, and operates this dungeon.")
    return M_HANDLED


def _v_zork(world: "World") -> int:
    print("At your service!")
    return M_HANDLED


def _v_plugh(world: "World") -> int:
    print("A hollow voice says \"Fool.\"")
    return M_HANDLED


def _v_count(world: "World") -> int:
    prso = world.prso
    blessings = _obj(world, "BLESSINGS")
    if prso and blessings and prso is blessings:
        print("Well, for one, you are playing Zork...")
        return M_HANDLED
    print("You have lost your mind.")
    return M_HANDLED


def _v_dig(world: "World") -> int:
    prsi = world.prsi
    hands = _obj(world, "HANDS")
    if prsi is None:
        world.prsi = hands
    if prsi and prsi.has_flag(TOOLBIT):
        print(f"Digging with the {prsi.desc} is slow and tedious.")
    else:
        print(f"Digging with a {prsi.desc if prsi else 'that'} is silly.")
    return M_HANDLED


def _v_search(world: "World") -> int:
    print("You find nothing unusual.")
    return M_HANDLED


def _v_repent(world: "World") -> int:
    print("It could very well be too late!")
    return M_HANDLED


def _v_win(world: "World") -> int:
    print("Naturally!")
    return M_HANDLED


def _v_wish(world: "World") -> int:
    print("With luck, your wish will come true.")
    return M_HANDLED


def _v_curse(world: "World") -> int:
    prso = world.prso
    if prso:
        if prso.has_flag(ACTORBIT):
            print("Insults of this nature won't help you.")
        else:
            print("What a loony!")
    else:
        print("Such language in a high-class establishment like this!")
    return M_HANDLED


def _v_bug(world: "World") -> int:
    print("Bug? Not in a flawless program like this! (Cough, cough).")
    return M_HANDLED


def _v_score_verb(world: "World") -> int:
    return _v_score(world)


def _v_lamp_on(world: "World") -> int:
    prso = world.prso
    lightbit = "LIGHTBIT"
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(lightbit):
        if prso.has_flag(ONBIT):
            print("It is already on.")
        else:
            prso.set_flag(ONBIT)
            print(f"The {prso.desc} is now on.")
            if not world.is_lit():
                world.game.describe_room()
        return M_HANDLED
    if prso.has_flag(BURNBIT):
        print(f"If you wish to burn the {prso.desc}, you should say so.")
        return M_HANDLED
    print("You can't turn that on.")
    return M_HANDLED


def _v_lamp_off(world: "World") -> int:
    prso = world.prso
    lightbit = "LIGHTBIT"
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(lightbit):
        if not prso.has_flag(ONBIT):
            print("It is already off.")
        else:
            prso.clear_flag(ONBIT)
            print(f"The {prso.desc} is now off.")
            if not world.is_lit():
                print("It is now pitch black.")
        return M_HANDLED
    print("You can't turn that off.")
    return M_HANDLED


def _v_strike(world: "World") -> int:
    prso = world.prso
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(ACTORBIT):
        print(f"Since you aren't versed in hand-to-hand combat, you'd better attack the {prso.desc} with a weapon.")
        return M_HANDLED
    return world.game.perform("V-LAMP-ON", prso)


def _v_stab(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if winner is None:
        return M_NOT_HANDLED
    weapon = None
    for item in winner.contents:
        if item.has_flag(WEAPONBIT):
            weapon = item
            break
    if weapon:
        return world.game.perform("V-ATTACK", prso, weapon)
    print(f"No doubt you propose to stab the {prso.desc if prso else 'that'} with your pinky?")
    return M_HANDLED


def _v_mung(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(ACTORBIT):
        return world.game.perform("V-ATTACK", prso)
    print("Nice try.")
    return M_HANDLED


def _pre_mung(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prso is None:
        return M_NOT_HANDLED
    if prsi is None or not prsi.has_flag(WEAPONBIT):
        if prsi is None:
            print(f"Trying to destroy the {prso.desc} with your bare hands is futile.")
        else:
            print(f"Trying to destroy the {prso.desc} with a {prsi.desc} is futile.")
        return M_HANDLED
    return M_NOT_HANDLED


def _v_enter(world: "World") -> int:
    prso = world.prso
    # V-THROUGH with a VEHBIT object → board the vehicle (ZIL V-THROUGH logic)
    if world.prsa == "V-THROUGH" and prso is not None and prso.has_flag("VEHBIT"):
        return world.game.perform("V-BOARD", prso)
    world.game.do_walk("in")
    return M_HANDLED


def _v_exit_verb(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    if prso is None or prso is _obj(world, "ROOMS"):
        if winner and hasattr(winner.location, "has_flag") and winner.location.has_flag("VEHBIT"):
            return world.game.perform("V-DISEMBARK", winner.location)
        world.game.do_walk("out")
        return M_HANDLED
    if winner and prso.location is winner:
        return world.game.perform("V-DISEMBARK", prso)
    world.game.do_walk("out")
    return M_HANDLED


def _v_cross(world: "World") -> int:
    print("You can't cross that!")
    return M_HANDLED


def _v_back(world: "World") -> int:
    print("Sorry, my memory is poor. Please give a direction.")
    return M_HANDLED


def _v_stand(world: "World") -> int:
    winner = world.winner
    if winner and hasattr(winner.location, "has_flag") and winner.location.has_flag("VEHBIT"):
        return world.game.perform("V-DISEMBARK", winner.location)
    print("You are already standing, I think.")
    return M_HANDLED


def _v_follow(world: "World") -> int:
    print("You're nuts!")
    return M_HANDLED


def _v_knock(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(DOORBIT):
        print("Nobody's home.")
    elif prso:
        print(f"Why knock on a {prso.desc}?")
    else:
        print("Knock on what?")
    return M_HANDLED


def _v_kiss(world: "World") -> int:
    print("I'd sooner kiss a pig.")
    return M_HANDLED


def _v_kick(world: "World") -> int:
    prso = world.prso
    print(f"Kicking the {prso.desc if prso else 'that'} has no obvious effect.")
    return M_HANDLED


def _v_wake(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"The {prso.desc} is rudely awakened.")
    else:
        prso_name = prso.desc if prso else "that"
        print(f"The {prso_name} isn't sleeping.")
    return M_HANDLED


def _v_answer(world: "World") -> int:
    print("Nobody seems to be awaiting your answer.")
    return M_HANDLED


def _v_send(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"Why would you send for the {prso.desc}?")
    else:
        print("That doesn't make sends.")
    return M_HANDLED


def _v_look_under(world: "World") -> int:
    print("There is nothing but dust there.")
    return M_HANDLED


def _v_look_behind(world: "World") -> int:
    prso = world.prso
    print(f"There is nothing behind the {prso.desc if prso else 'that'}.")
    return M_HANDLED


def _v_fill(world: "World") -> int:
    prso = world.prso
    here = world.here
    global_water = _obj(world, "GLOBAL-WATER")
    water = _obj(world, "WATER")
    if prso is None:
        return M_NOT_HANDLED
    if global_water and here and global_water in here.global_objects:
        if prso.has_flag(CONTBIT) and prso.has_flag(OPENBIT):
            if water:
                world.move_object(water, prso)
            print("The bottle is now full of water.")
        else:
            print("You can't fill that here.")
        return M_HANDLED
    print("There's nothing to fill it with.")
    return M_HANDLED


def _v_pour(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    water = _obj(world, "WATER")
    if prso and water and prso is water:
        if prsi and prsi.has_flag("FLAMEBIT") and prsi.has_flag(ONBIT):
            print(f"The {prsi.desc} is extinguished.")
            prsi.clear_flag(ONBIT)
            prsi.clear_flag("FLAMEBIT")
            world.remove_object(water)
        else:
            world.remove_object(water)
            if prsi:
                print(f"The water spills over the {prsi.desc}, to the floor, and evaporates.")
            else:
                print("The water spills to the floor and evaporates.")
        return M_HANDLED
    print("You can't pour that.")
    return M_HANDLED


def _v_squeeze(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"The {prso.desc} does not understand this.")
    else:
        print("How singularly useless.")
    return M_HANDLED


def _v_hatch(world: "World") -> int:
    print("Bizarre!")
    return M_HANDLED


def _v_chomp(world: "World") -> int:
    print("Preposterous!")
    return M_HANDLED


def _v_plug(world: "World") -> int:
    print("This has no effect.")
    return M_HANDLED


def _v_inflate(world: "World") -> int:
    print("How can you inflate that?")
    return M_HANDLED


def _v_deflate(world: "World") -> int:
    print("Come on, now!")
    return M_HANDLED


def _v_pick(world: "World") -> int:
    print("You can't pick that.")
    return M_HANDLED


def _v_make(world: "World") -> int:
    print("You can't do that.")
    return M_HANDLED


def _v_melt(world: "World") -> int:
    prso = world.prso
    print(f"It's not clear that a {prso.desc if prso else 'that'} can be melted.")
    return M_HANDLED


def _v_roll(world: "World") -> int:
    prso = world.prso
    print(f"Rolling the {prso.desc if prso else 'that'} has no obvious effect.")
    return M_HANDLED


def _v_spin(world: "World") -> int:
    print("You can't spin that!")
    return M_HANDLED


def _v_wind(world: "World") -> int:
    prso = world.prso
    print(f"You cannot wind up a {prso.desc if prso else 'that'}.")
    return M_HANDLED


def _v_incant(world: "World") -> int:
    print("The incantation echoes back faintly, but nothing else happens.")
    return M_HANDLED


def _v_ring(world: "World") -> int:
    print("How, exactly, can you ring that?")
    return M_HANDLED


def _v_pick_up(world: "World") -> int:
    return world.game.perform("V-TAKE", world.prso)


def _v_command(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"The {prso.desc} pays no attention.")
    else:
        print("You cannot talk to that!")
    return M_HANDLED


def _v_tell(world: "World") -> int:
    prso = world.prso
    if prso is None:
        return M_NOT_HANDLED
    if prso.has_flag(ACTORBIT):
        print(f"The {prso.desc} pauses for a moment, perhaps thinking that you should reread\nthe manual.")
    else:
        print(f"You can't talk to the {prso.desc}!")
    return M_HANDLED


def _v_mumble(world: "World") -> int:
    print("You'll have to speak up if you expect me to hear you!")
    return M_HANDLED


def _v_stay(world: "World") -> int:
    print("You will be lost without me!")
    return M_HANDLED


def _v_rape(world: "World") -> int:
    print("What a (ahem!) strange idea.")
    return M_HANDLED


def _v_lower(world: "World") -> int:
    prso = world.prso
    print(f"Playing in this way with the {prso.desc if prso else 'that'} has no obvious effect.")
    return M_HANDLED


def _v_raise_verb(world: "World") -> int:
    return _v_lower(world)


def _v_oil(world: "World") -> int:
    print("You probably put spinach in your gas tank, too.")
    return M_HANDLED


def _v_disembark(world: "World") -> int:
    prso = world.prso
    winner = world.winner
    here = world.here
    if prso is None or (prso is _obj(world, "ROOMS") and winner):
        if winner and hasattr(winner.location, "has_flag") and winner.location.has_flag("VEHBIT"):
            vehicle = winner.location
            prso = vehicle
        else:
            print("You're not in anything!")
            return M_HANDLED
    if winner and winner.location is not prso:
        print("You're not in that!")
        return M_FATAL
    if here and here.has_flag("RLANDBIT"):
        print("You are on your own feet again.")
        world.move_object(winner, here)
    else:
        print("You realize that getting out here would be fatal.")
        return M_FATAL
    return M_HANDLED


def _v_play(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag(ACTORBIT):
        print(f"You become so engrossed in the role of the {prso.desc} that you kill yourself, just as he might have done!")
        world.game.jigs_up("")
        return M_FATAL
    print("That's silly!")
    return M_HANDLED


def _v_exorcise(world: "World") -> int:
    print("What a bizarre concept!")
    return M_HANDLED


def _v_echo(world: "World") -> int:
    print("echo echo ...")
    return M_HANDLED


def _v_blast(world: "World") -> int:
    print("You can't blast anything by using words.")
    return M_HANDLED


def _v_apply(world: "World") -> int:
    return _v_rub(world)


def _v_activate(world: "World") -> int:
    return _v_lamp_on(world)


def _v_extinguish(world: "World") -> int:
    return _v_lamp_off(world)


def _v_disenchant(world: "World") -> int:
    print("Nothing happens.")
    return M_HANDLED


def _v_enchant(world: "World") -> int:
    print("Nothing happens.")
    return M_HANDLED


def _v_launch(world: "World") -> int:
    prso = world.prso
    if prso and prso.has_flag("VEHBIT"):
        print("You can't launch that by saying \"launch\"!")
    else:
        print("That's pretty weird.")
    return M_HANDLED


def _v_board(world: "World") -> int:
    prso = world.prso
    here = world.here
    winner = world.winner
    if prso is None:
        return M_NOT_HANDLED
    if not prso.has_flag("VEHBIT"):
        print(f"You have a theory on how to board a {prso.desc}, perhaps?")
        return M_HANDLED
    if prso.location is not here:
        print(f"The {prso.desc} must be on the ground to be boarded.")
        return M_HANDLED
    if winner and winner.location is not None and hasattr(winner.location, "has_flag") and winner.location.has_flag("VEHBIT"):
        print(f"You are already in the {winner.location.desc}!")
        return M_HANDLED
    if winner:
        world.move_object(winner, prso)
    print(f"You are now in the {prso.desc}.")
    return M_HANDLED


def _v_treasure(world: "World") -> int:
    here = world.here
    if here and here.name == "NORTH-TEMPLE":
        dest = world.rooms.get("TREASURE-ROOM")
        if dest:
            world.game.enter_room(dest)
        return M_HANDLED
    if here and here.name == "TREASURE-ROOM":
        dest = world.rooms.get("NORTH-TEMPLE")
        if dest:
            world.game.enter_room(dest)
        return M_HANDLED
    print("Nothing happens.")
    return M_HANDLED


def _v_lean(world: "World") -> int:
    print("Getting tired?")
    return M_HANDLED


def _v_pump(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    pump = _obj(world, "PUMP")
    winner = world.winner
    if prsi and pump and prsi is not pump:
        print(f"Pump it up with a {prsi.desc}?")
        return M_HANDLED
    if pump and winner and pump.location is winner:
        return world.game.perform("V-INFLATE", prso, pump)
    print("It's really not clear how.")
    return M_HANDLED


def _v_poke(world: "World") -> int:
    prso = world.prso
    print(f"Poking the {prso.desc if prso else 'that'} has no obvious effect.")
    return M_HANDLED


def _v_puncture(world: "World") -> int:
    prso = world.prso
    print(f"Puncturing the {prso.desc if prso else 'that'} has no obvious effect.")
    return M_HANDLED


def _v_spray(world: "World") -> int:
    return _v_squeeze(world)


def _v_send_to(world: "World") -> int:
    return _v_send(world)


def _v_slide(world: "World") -> int:
    prso = world.prso
    here = world.here
    if here and here.name == "SLIDE-ROOM":
        dest = world.rooms.get("CELLAR")
        if dest:
            world.game.enter_room(dest)
        return M_HANDLED
    print(f"You can't slide the {prso.desc if prso else 'that'}.")
    return M_HANDLED


def _v_brush(world: "World") -> int:
    print("If you wish, but heaven only knows why.")
    return M_HANDLED


def _v_climb_up(world: "World") -> int:
    world.game.do_walk("up")
    return M_HANDLED


def _v_climb_down(world: "World") -> int:
    world.game.do_walk("down")
    return M_HANDLED


def _v_cut(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prso and prso.has_flag(ACTORBIT):
        return world.game.perform("V-ATTACK", prso, prsi)
    if prsi and prsi.has_flag(WEAPONBIT) and prso and prso.has_flag(BURNBIT):
        winner = world.winner
        if winner and winner.location is prso:
            print("Not a bright idea, especially since you're in it.")
            return M_HANDLED
        world.remove_object(prso)
        print(f"Your skillful {prsi.desc}smanship slices the {prso.desc} into innumerable slivers which blow away.")
        return M_HANDLED
    if prsi and not prsi.has_flag(WEAPONBIT):
        print(f"The \"cutting edge\" of a {prsi.desc} is hardly adequate.")
        return M_HANDLED
    print(f"Strange concept, cutting the {prso.desc if prso else 'that'}...")
    return M_HANDLED


def _v_swing(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if prsi is None:
        print("Whoosh!")
        return M_HANDLED
    return world.game.perform("V-ATTACK", prsi, prso)


def _v_move_to(world: "World") -> int:
    print("You can't push things to that.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

def _v_walk_with_grue(world: "World") -> int:
    """V-WALK override: grue kills in dark when there is no exit (80% chance)."""
    direction = world.walk_dir or ""
    here = world.here
    if here and direction not in here.exits:
        if (not world.is_lit()
                and random.randint(1, 100) <= 80
                and not here.has_flag(NONLANDBIT)):
            world.game.jigs_up(
                "Oh, no! You have walked into the slavering fangs of a lurking grue!"
            )
            return M_FATAL
    return world.game.do_walk(direction)


def score_obj(world: "World", obj) -> None:
    """Award obj.value points once (zeroes value after scoring, mirrors SCORE-OBJ)."""
    if obj is None or obj.value <= 0:
        return
    _score_upd(world, obj.value)
    obj.value = 0


def _score_upd(world: "World", delta: int) -> None:
    """Update BASE-SCORE and world.score by delta (mirrors SCORE-UPD)."""
    base = int(world.get_global("BASE-SCORE") or 0)
    base += delta
    world.set_global("BASE-SCORE", base)
    world.score = max(0, world.score + delta)
    world.set_global("SCORE", world.score)
    if world.score >= 350 and not world.get_global("WON-FLAG"):
        world.set_global("WON-FLAG", True)
        _map = world.objects.get("MAP")
        if _map:
            _map.clear_flag("INVISIBLE")
        print('\nAn almost inaudible voice whispers in your ear, "Look to your treasures'
              '\nfor the final secret."')


def register_verbs(game: "Game") -> None:
    """Register all verb and preaction handlers with the game."""

    # Walk with grue check
    game.register_verb("V-WALK",       _v_walk_with_grue)

    # Meta verbs
    game.register_verb("V-VERBOSE",    _v_verbose)
    game.register_verb("V-BRIEF",      _v_brief)
    game.register_verb("V-SUPER-BRIEF", _v_super_brief)
    game.register_verb("V-LOOK",       _v_look)
    game.register_verb("V-INVENTORY",  _v_inventory)
    game.register_verb("V-QUIT",       _v_quit)
    game.register_verb("V-RESTART",    _v_restart)
    game.register_verb("V-SAVE",       _v_save)
    game.register_verb("V-RESTORE",    _v_restore)
    game.register_verb("V-SCORE",      _v_score_verb)
    game.register_verb("V-VERSION",    _v_version)
    game.register_verb("V-SCRIPT",     _v_script)
    game.register_verb("V-UNSCRIPT",   _v_unscript)
    game.register_verb("V-DIAGNOSE",   _v_diagnose)
    game.register_verb("V-WAIT",       _v_wait)

    # Lamp
    game.register_verb("V-LAMP-ON",    _v_lamp_on)
    game.register_verb("V-LAMP-OFF",   _v_lamp_off)

    # Object manipulation
    game.register_verb("V-TAKE",       _v_take)
    game.register_verb("V-DROP",       _v_drop)
    game.register_verb("V-EXAMINE",    _v_examine)
    game.register_verb("V-LOOK-INSIDE", _v_look_inside)
    game.register_verb("V-OPEN",       _v_open)
    game.register_verb("V-CLOSE",      _v_close)
    game.register_verb("V-PUT",        _v_put)
    game.register_verb("V-GIVE",       _v_give)
    game.register_verb("V-THROW",      _v_throw)
    game.register_verb("V-BURN",       _v_burn)
    game.register_verb("V-EAT",        _v_eat)
    game.register_verb("V-DRINK",      _v_drink)
    game.register_verb("V-READ",       _v_read)
    game.register_verb("V-FIND",       _v_find)
    game.register_verb("V-MOVE",       _v_move)
    game.register_verb("V-SHAKE",      _v_shake)
    game.register_verb("V-TURN",       _v_turn)
    game.register_verb("V-LOCK",       _v_lock)
    game.register_verb("V-UNLOCK",     _v_unlock)
    game.register_verb("V-TIE",        _v_tie)
    game.register_verb("V-UNTIE",      _v_untie)
    game.register_verb("V-WEAR",       _v_wear)
    game.register_verb("V-PUSH",       _v_push)
    game.register_verb("V-PULL",       _v_pull)
    game.register_verb("V-WAVE",       _v_wave)
    game.register_verb("V-RUB",        _v_rub)
    game.register_verb("V-SMELL",      _v_smell)
    game.register_verb("V-LISTEN",     _v_listen)
    game.register_verb("V-CLIMB",      _v_climb)
    game.register_verb("V-CLIMB-FOO",  _v_climb)
    game.register_verb("V-SWIM",       _v_swim)
    game.register_verb("V-JUMP",       _v_jump)
    game.register_verb("V-SAY",        _v_say)
    game.register_verb("V-HELLO",      _v_hello)
    game.register_verb("V-YELL",       _v_yell)
    game.register_verb("V-PRAY",       _v_pray)
    game.register_verb("V-ODYSSEUS",   _v_odysseus)
    game.register_verb("V-FROBOZZ",    _v_frobozz)
    game.register_verb("V-ZORK",       _v_zork)
    game.register_verb("V-PLUGH",      _v_plugh)
    game.register_verb("V-COUNT",      _v_count)
    game.register_verb("V-DIG",        _v_dig)
    game.register_verb("V-SEARCH",     _v_search)
    game.register_verb("V-REPENT",     _v_repent)
    game.register_verb("V-WIN",        _v_win)
    game.register_verb("V-WISH",       _v_wish)
    game.register_verb("V-CURSE",      _v_curse)
    game.register_verb("V-BUG",        _v_bug)
    game.register_verb("V-ATTACK",     _v_attack)
    game.register_verb("V-MUNG",       _v_mung)
    game.register_verb("V-STAB",       _v_stab)
    game.register_verb("V-FILL",       _v_fill)
    game.register_verb("V-POUR",       _v_pour)
    game.register_verb("V-SQUEEZE",    _v_squeeze)
    game.register_verb("V-HATCH",      _v_hatch)
    game.register_verb("V-CHOMP",      _v_chomp)
    game.register_verb("V-PLUG",       _v_plug)
    game.register_verb("V-INFLATE",    _v_inflate)
    game.register_verb("V-DEFLATE",    _v_deflate)
    game.register_verb("V-PICK",       _v_pick)
    game.register_verb("V-MAKE",       _v_make)
    game.register_verb("V-MELT",       _v_melt)
    game.register_verb("V-ROLL",       _v_roll)
    game.register_verb("V-SPIN",       _v_spin)
    game.register_verb("V-WIND",       _v_wind)
    game.register_verb("V-INCANT",     _v_incant)
    game.register_verb("V-RING",       _v_ring)
    game.register_verb("V-COMMAND",    _v_command)
    game.register_verb("V-TELL",       _v_tell)
    game.register_verb("V-MUMBLE",     _v_mumble)
    game.register_verb("V-STAY",       _v_stay)
    game.register_verb("V-RAPE",       _v_rape)
    game.register_verb("V-LOWER",      _v_lower)
    game.register_verb("V-RAISE",      _v_raise_verb)
    game.register_verb("V-OIL",        _v_oil)
    game.register_verb("V-DISEMBARK",  _v_disembark)
    game.register_verb("V-PLAY",       _v_play)
    game.register_verb("V-EXORCISE",   _v_exorcise)
    game.register_verb("V-ECHO",       _v_echo)
    game.register_verb("V-BLAST",      _v_blast)
    game.register_verb("V-APPLY",      _v_apply)
    game.register_verb("V-ACTIVATE",   _v_activate)
    game.register_verb("V-EXTINGUISH", _v_extinguish)
    game.register_verb("V-DISENCHANT", _v_disenchant)
    game.register_verb("V-ENCHANT",    _v_enchant)
    game.register_verb("V-LAUNCH",     _v_launch)
    game.register_verb("V-BOARD",      _v_board)
    game.register_verb("V-TREASURE",   _v_treasure)
    game.register_verb("V-LEAN",       _v_lean)
    game.register_verb("V-PUMP",       _v_pump)
    game.register_verb("V-POKE",       _v_poke)
    game.register_verb("V-PUNCTURE",   _v_puncture)
    game.register_verb("V-SPRAY",      _v_spray)
    game.register_verb("V-SLIDE",      _v_slide)
    game.register_verb("V-BRUSH",      _v_brush)
    game.register_verb("V-CLIMB-UP",   _v_climb_up)
    game.register_verb("V-CLIMB-DOWN", _v_climb_down)
    game.register_verb("V-CUT",        _v_cut)
    game.register_verb("V-SWING",      _v_swing)
    game.register_verb("V-STRIKE",     _v_strike)
    game.register_verb("V-ENTER",      _v_enter)
    game.register_verb("V-THROUGH",    _v_enter)
    game.register_verb("V-EXIT",       _v_exit_verb)
    game.register_verb("V-LEAVE",      lambda w: (w.game.do_walk("out"), M_HANDLED)[1])
    game.register_verb("V-CROSS",      _v_cross)
    game.register_verb("V-BACK",       _v_back)
    game.register_verb("V-STAND",      _v_stand)
    game.register_verb("V-FOLLOW",     _v_follow)
    game.register_verb("V-KNOCK",      _v_knock)
    game.register_verb("V-KISS",       _v_kiss)
    game.register_verb("V-KICK",       _v_kick)
    game.register_verb("V-WAKE",       _v_wake)
    game.register_verb("V-ANSWER",     _v_answer)
    game.register_verb("V-SEND",       _v_send)
    game.register_verb("V-LOOK-UNDER", _v_look_under)
    game.register_verb("V-LOOK-BEHIND", _v_look_behind)
    game.register_verb("V-LOOK-ON",    _v_look_inside)

    # Preactions
    game.register_preaction("V-TAKE",  _pre_take)
    game.register_preaction("V-DROP",  _pre_drop)
    game.register_preaction("V-PUT",   _pre_put)
    game.register_preaction("V-GIVE",  _pre_give)
    game.register_preaction("V-MOVE",  _pre_move)
    game.register_preaction("V-TURN",  _pre_turn)
    game.register_preaction("V-BURN",  _pre_burn)
    game.register_preaction("V-READ",  _pre_read)
    game.register_preaction("V-MUNG",  _pre_mung)
