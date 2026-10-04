"""
Verb handlers for Roundabout: The God-Forsaken Ring.
Built incrementally — handlers added as walkthrough sections require them.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# Score helper (called by game.enter_room on first visit)
# Room value is the room's exploration XP (locations.md **XP:**).
# ---------------------------------------------------------------------------

def _score_upd(world: World, amount: int) -> None:
    world.score += amount
    world.set_global("SCORE", world.score)
    from content.experience import award_xp
    award_xp(world, amount)


# ---------------------------------------------------------------------------
# V-OPEN
# ---------------------------------------------------------------------------

def v_open(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    # White House mailbox — triggers opening sequence
    if obj.name == "MAILBOX-WHITE-HOUSE":
        if world.get_global("OPENING-DONE"):
            print("The mailbox is already open.")
            return M_HANDLED
        print("The mailbox opens.")
        world.set_global("OPENING-DONE", True)
        from content.char_create import run_opening
        run_opening(world, world.game)
        return M_HANDLED

    # Tower / tavern mailbox — teleports to Tower
    if obj.name == "MAILBOX-TOWER":
        print("You open the mailbox. A familiar warmth pulls you through.")
        tower = world.rooms.get("WIZARDS-TOWER")
        if tower is not None:
            world.game.enter_room(tower)
        return M_HANDLED

    if obj.name == "STRONGBOX":
        from content import tunnels
        tunnels.open_strongbox(world)
        return M_HANDLED

    if obj.name == "KEEPER-DOOR":
        from content import keeper
        keeper.open_door(world)
        return M_HANDLED

    if obj.name in ("CELLAR-DOOR", "TUNNEL-DOOR-CELLAR", "TUNNEL-DOOR-BONE", "CASHBOX"):
        from content import cellar
        {"CELLAR-DOOR": cellar.open_cellar_door, "CASHBOX": cellar.open_cashbox}.get(
            obj.name, cellar.open_tunnel_door)(world)
        return M_HANDLED

    # Statue base — crowbar required (opening with the crowbar: Section J)
    if obj.name == "STATUE":
        print("The base is sealed tight. Something with leverage could pry it open.")
        return M_HANDLED

    print("You can't open that.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-EXAMINE
# ---------------------------------------------------------------------------

def v_examine(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    # Painting — teleports to Tale and Ale (npcs.md: Will, steps 7–8)
    if obj.name == "PAINTING":
        if not world.get_global("TOWER-WARNING-DONE"):
            world.set_global("TOWER-WARNING-DONE", True)
            print(
                '"One more thing," Will says, rising from his chair. '
                '"The ring — I should have told you, it—"'
            )
        print(
            "The painting is larger than it looked. Or you are smaller. The "
            "tavern in the frame tilts toward you, and then you are simply "
            "there — the smell of woodsmoke and ale arriving before anything "
            "else does."
        )
        tavern = world.rooms.get("TALE-AND-ALE")
        if tavern is not None:
            world.game.enter_room(tavern)
        return M_HANDLED

    # Town Square statue — seam visible to anyone who looks (locations.md)
    if obj.name == "STATUE":
        world.set_global("STATUE-EXAMINED", True)
        from content.statue import statue_state
        state = statue_state(world)
        if state == "looted":
            print(
                "The statue stands to one side, its base pried open and empty. "
                "Whatever was inside is gone."
            )
        elif state == "open":
            print("The statue stands to one side, its base pried open.")
        else:
            print(
                "The plaque below it is worn to illegibility, but the base has "
                "a seam around it — visible now that you're looking. Something "
                "with leverage could open it."
            )
        return M_HANDLED

    if obj.name == "WILL":
        from content.objects import WILL_APPEARANCE
        print(WILL_APPEARANCE)
        return M_HANDLED

    from content import gravestone
    if gravestone.examine(world, obj):
        return M_HANDLED

    # Generic examine: show ldesc or fdesc
    desc = obj.ldesc or obj.fdesc
    if desc:
        print(desc)
        obj.touched = True
    else:
        print(f"You see nothing special about the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-LOOK (bare look — redescribe current room)
# ---------------------------------------------------------------------------

def v_drive_stake(world: World) -> int:
    from content import still_den
    return M_HANDLED if still_den.drive_stake(world) else M_NOT_HANDLED


def v_turn_dial_left(world: World) -> int:
    from content import altar
    altar.turn_dial(world, -1)
    return M_HANDLED


def v_turn_dial_right(world: World) -> int:
    from content import altar
    altar.turn_dial(world, +1)
    return M_HANDLED


def v_mix(world: World) -> int:
    from content import shrine_bowl
    return M_HANDLED if shrine_bowl.mix(world) else M_NOT_HANDLED


def v_place(world: World) -> int:
    if world.prso is not None and world.prso.name == "AQUEDUCT-BLOCKS":
        from content import aqueduct
        aqueduct.place_blocks(world)
        return M_HANDLED
    return M_NOT_HANDLED


def v_seal(world: World) -> int:
    from content import aqueduct
    if aqueduct.is_aqueduct_part(world.prso):
        aqueduct.seal(world)
        return M_HANDLED
    return M_NOT_HANDLED


def v_pour(world: World) -> int:
    from content import keeper
    return M_HANDLED if keeper.pour(world) else M_NOT_HANDLED


def v_look_up(world: World) -> int:
    from content import lower_tier
    lower_tier.look_up(world)
    return M_HANDLED


def v_look(world: World) -> int:
    world.game.desc_mode_override = True
    world.game.describe_room()
    world.game.desc_mode_override = False
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-SAVE / V-RESTORE  (engine/savegame.py)
# ---------------------------------------------------------------------------

def v_save(world: World) -> int:
    from engine import savegame
    savegame.save(world.game)
    print("Saved.")
    return M_HANDLED


def v_restore(world: World) -> int:
    from engine import savegame
    if not savegame.restore(world.game):
        print("There's no saved game to restore.")
        return M_HANDLED
    print("Restored.")
    world.game.desc_mode_override = True
    world.game.describe_room()
    world.game.desc_mode_override = False
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-INVENTORY  (INVENTORY / I)
# Item names are the items.md "inventory description" (obj.desc).
# ---------------------------------------------------------------------------

def v_inventory(world: World) -> int:
    from engine.world import WEARBIT
    player = world.player
    items = [o for o in (player.contents if player else []) if o is not player]
    if not items:
        print("You are empty-handed.")
        return M_HANDLED

    print("You are carrying:")
    for obj in items:
        if obj.has_flag(WEARBIT):
            note = " (being worn)"
        elif obj.has_flag("WEARABLE"):
            note = " (not worn)"
        else:
            note = ""
        print(f"  {obj.desc[:1].upper()}{obj.desc[1:]}{note}")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-TAKE
# ---------------------------------------------------------------------------

def v_take(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    if obj.name == "AYLORA":
        from content import vikings
        vikings.take_aylora(world)
        return M_HANDLED

    if obj.name == "GRAVESTONE":
        from content import gravestone
        gravestone.take_stone(world)
        return M_HANDLED

    from engine.world import TAKEBIT, SACREDBIT
    if not obj.has_flag(TAKEBIT):
        print(f"You can't take the {obj.desc}.")
        return M_HANDLED

    if obj.has_flag(SACREDBIT):
        print(f"The {obj.desc} is fixed in place.")
        return M_HANDLED

    player = world.player
    if player is None:
        return M_NOT_HANDLED

    if obj in player.contents:
        print(f"You already have the {obj.desc}.")
        return M_HANDLED

    obj.touched = True
    world.move_object(obj, player)
    print(f"You take the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-WEAR
# ---------------------------------------------------------------------------

def v_wear(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    player = world.player
    if player is None:
        return M_NOT_HANDLED

    if obj not in player.contents:
        world.move_object(obj, player)

    from engine.world import WEARBIT
    if obj.has_flag(WEARBIT):
        print(f"You're already wearing the {obj.desc}.")
        return M_HANDLED
    if obj.name == "RING":
        from content import corruption, chuckle
        corruption.wear_ring(world)
        if not world.globals.get("ring_worn"):
            return M_HANDLED   # bound / fully corrupted: it won't go on
        obj.set_flag(WEARBIT)
        print("You slip the ring on. When you look down, your hand is still "
              "there — but only because you know where to look.")
        chuckle.update_ghost_visibility(world)
        return M_HANDLED
    obj.set_flag(WEARBIT)
    if obj.name == "ENCHANTED-GLASSES":
        _set_glasses_state(world)
    print(f"You put on the {obj.desc}.")
    if obj.name == "ENCHANTED-GLASSES":
        from content import kevry
        kevry.on_wear_glasses(world)
    if obj.name == "HEART-NECKLACE":
        from content.lynds import necklace_worn
        necklace_worn(world, True)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-REMOVE  (REMOVE <worn item>)
# ---------------------------------------------------------------------------

def v_remove(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    from engine.world import WEARBIT
    player = world.player
    if player is None or obj not in player.contents or not obj.has_flag(WEARBIT):
        print(f"You aren't wearing the {obj.desc}.")
        return M_HANDLED

    if obj.name == "RING":
        from content import corruption, chuckle
        if not corruption.try_remove_ring(world):
            return M_HANDLED   # late-stage roll failed; the ring stays on
        chuckle.update_ghost_visibility(world)

    obj.clear_flag(WEARBIT)
    if obj.name == "ENCHANTED-GLASSES":
        _set_glasses_state(world)
    if obj.name == "HEART-NECKLACE":
        from content.lynds import necklace_worn
        necklace_worn(world, False)
    print(f"{obj.desc[0].upper()}{obj.desc[1:]} removed.")
    return M_HANDLED


def _set_glasses_state(world: World) -> None:
    """Set the perception stats (content/player.py) from the glasses' worn/enchanted state."""
    from engine.world import WEARBIT
    glasses = world.objects.get("ENCHANTED-GLASSES")
    worn = bool(glasses and glasses.has_flag(WEARBIT))
    actually = worn and bool(world.get_global("GLASSES-ENCHANTED"))
    world.globals["enchanted_glasses_worn"] = worn and not actually
    world.globals["actually_enchanted_glasses_worn"] = actually


# ---------------------------------------------------------------------------
# V-DROP
# ---------------------------------------------------------------------------

def v_drop(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    from content import gravestone
    if obj.name == "GRAVESTONE":
        gravestone.unload(world)
        return M_HANDLED
    if obj.name == "HAND-CART" and gravestone.drop_cart(world):
        return M_HANDLED

    player = world.player
    if player is None or obj not in player.contents:
        print(f"You aren't carrying the {obj.desc}.")
        return M_HANDLED

    world.move_object(obj, world.here)
    print(f"Dropped. {obj.ldesc or obj.desc}")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-TALK  (TALK TO <npc>)
# ---------------------------------------------------------------------------

def v_talk(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    if obj.name == "SHAMUS":
        print(
            'Shamus wipes his hands on his apron. "What can I do for you? '
            'Gunpowder\'s five Zenni. Torches, three."'
        )
        return M_HANDLED

    if obj.name == "KEVRY":
        from content import kevry
        kevry.talk(world)
        return M_HANDLED

    _VIKING_TALK = {
        "IVANAAR": "talk_ivanaar", "HAALVAR": "talk_haalvar",
        "AYLORA": "talk_aylora", "RAZNAK": "talk_raznak",
    }
    if obj.name in _VIKING_TALK:
        from content import vikings
        getattr(vikings, _VIKING_TALK[obj.name])(world)
        return M_HANDLED

    if obj.name == "CHILD":
        print("The child says nothing.")
        return M_HANDLED

    if obj.name == "BOGGART":
        from content import tunnels
        tunnels.talk_boggart(world)
        return M_HANDLED

    if obj.name == "ROWAN-FINCH":
        from content import gravestone
        gravestone.talk_rowan(world)
        return M_HANDLED

    if obj.name == "RECORDS-WORKER":
        from content import town_hall
        town_hall.talk_worker(world)
        return M_HANDLED

    if obj.name == "LITLOCK":
        from content import dankhaus
        dankhaus.talk_litlock(world)
        return M_HANDLED

    if obj.name == "LYNDS":
        from content import lynds
        lynds.challenge(world)   # TALK TO LYNDS starts the challenge (npcs.md)
        return M_HANDLED

    if obj.name == "MAY":
        from content import tavern
        tavern.talk_may(world)
        return M_HANDLED

    if obj.name in ("OAK-CHILD", "BEEKEEPER"):
        from content import old_oak
        (old_oak.talk_child if obj.name == "OAK-CHILD" else old_oak.talk_beekeeper)(world)
        return M_HANDLED

    if obj.name == "PYRONICUS":
        ring   = world.objects.get("RING")
        player = world.player
        if ring is not None and player is not None and ring.location is obj:
            print(
                'Pyronicus sets down his work and regards you with calm, '
                'unhurried eyes. "Will\'s errand," he says. "Yes."\n'
                'He moves to a workbench and returns with the ring, placing it '
                'in your hand with the care of someone returning something that '
                'was never theirs.\n'
                '"It fell through my ceiling," he says. "Rings don\'t do that by '
                'accident."\n'
                'He pauses. "Will told you what you need to know, I assume."\n'
                'He goes back to what he was doing. The conversation, '
                'apparently, is over.'
            )
            world.move_object(ring, player)
            world.set_global("RING-RETRIEVED", True)
        else:
            print(
                "He goes back to what he was doing. The conversation, "
                "apparently, is over."
            )
        return M_HANDLED

    print(f"There's no response from the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-GIVE  (GIVE <item> TO <npc>)
# ---------------------------------------------------------------------------

# ring-rituals.md — Will Passion's Briefing Structure: Second briefing
_SECOND_BRIEFING = (
    "Will sets down his pen when he sees the ring. He doesn't reach for it.\n"
    '"Good," he says. "Sit down."\n'
    "He doesn't wait to see if you do.\n"
    '"The ring can\'t be destroyed. I want to be clear about that — not by '
    "force, not by fire, not by anything one person or one faith could bring "
    "to bear. What's inside it is older than the methods we have for ending "
    'things."\n'
    "He moves to the window.\n"
    '"But three faiths together — three distinct sources of power, each '
    "contributing something the others cannot — that's another matter. There "
    "is a Church in Roundabout. The Church of All. You'll find an altar there "
    'with a dial. Seven religions. Three of them are what you need."\n'
    "He turns back.\n"
    '"I won\'t tell you which three. You\'ll know them when you find them. The '
    'things they ask of you will make it obvious."\n'
    "He picks up his pen.\n"
    '"When it\'s done, bring it back."'
)


def v_give(world: World) -> int:
    item, npc = world.prso, world.prsi
    if item is None:
        return M_NOT_HANDLED
    if npc is None:
        print(f"Who do you want to give the {item.desc} to?")
        return M_HANDLED

    player = world.player
    if player is None or item not in player.contents:
        print(f"You aren't carrying the {item.desc}.")
        return M_HANDLED

    # Ring to Will — second briefing. He doesn't take it; the player keeps it.
    if npc.name == "WILL" and item.name == "RING" \
            and not world.get_global("SECOND-BRIEFING-DONE"):
        print(_SECOND_BRIEFING)
        world.set_global("SECOND-BRIEFING-DONE", True)
        return M_HANDLED

    # Spell scroll to Will — teaching (mechanics.md, Quest 56)
    if npc.name == "WILL":
        from content import will
        if item.name in will.SPELL_SCROLLS:
            will.teach(world, item)
            return M_HANDLED

    # Town charter to the Boggart — Quest 27, the bridge is public property
    if npc.name == "BOGGART" and item.name == "TOWN-CHARTER":
        from content import tunnels
        tunnels.give_charter(world)
        return M_HANDLED

    # Pocket watch to the Records Room clerk — Quest 17 → town charter
    if npc.name == "RECORDS-WORKER" and item.name == "POCKET-WATCH":
        from content import town_hall
        town_hall.give_watch(world)
        return M_HANDLED

    # Kite back to the child — Quest 41
    if npc.name == "OAK-CHILD" and item.name == "KITE":
        from content import old_oak
        old_oak.give_kite(world)
        return M_HANDLED

    # Runed metal to Pyronicus — forges the Pale Blade
    if npc.name == "PYRONICUS" and item.name == "RUNED-METAL":
        from content import vikings
        vikings.forge_pale_blade(world)
        return M_HANDLED

    print(f"{npc.desc} doesn't take the {item.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-ENTER  (ENTER DANKHAUS / ENTER YURT)
# ---------------------------------------------------------------------------

def v_enter(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "DANKHAUS":
        from content import dankhaus
        dankhaus.enter_dankhaus(world)
        return M_HANDLED
    print("You can't go in there.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-RAISE (LIFT PORTCULLIS) / V-USE (USE PORTCULLIS BAR)
# ---------------------------------------------------------------------------

def v_raise(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "PORTCULLIS":
        from content import shrine_path
        shrine_path.lift(world)
        return M_HANDLED
    print("Nothing happens.")
    return M_HANDLED


def v_use(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "CROWBAR" and world.prsi is not None             and world.prsi.name == "STATUE":
        from content import statue
        statue.pry_open(world)
        return M_HANDLED
    if obj is not None and obj.name == "CROWBAR" and world.prsi is not None \
            and world.prsi.name == "DRAIN":
        from content import cellar
        cellar.pry_drain(world)
        return M_HANDLED
    if obj is not None and obj.name == "PORTCULLIS-BAR":
        from content import shrine_path
        if shrine_path.use_bar(world):
            return M_HANDLED
    from content import aqueduct
    if obj is not None and obj.name == "MORTAR" and aqueduct.is_aqueduct_part(world.prsi):
        aqueduct.seal(world)
        return M_HANDLED
    print("Nothing happens.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-JUMP-ON / V-DISARM  (Trap 29 plate in the Combat Room)
# ---------------------------------------------------------------------------

def v_jump_on(world: World) -> int:
    from content import combat_room
    combat_room.jump_on_plate(world)
    return M_HANDLED


def v_disarm(world: World) -> int:
    from content import combat_room
    combat_room.disarm_plate(world)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-PAY  (PAY BOGGART)
# ---------------------------------------------------------------------------

def v_pay(world: World) -> int:
    obj = world.prso
    boggart = world.objects.get("BOGGART")
    if (obj is None or obj.name == "BOGGART") and boggart is not None             and boggart.location is world.here:
        from content import tunnels
        tunnels.pay_boggart(world)
        return M_HANDLED
    print("There's no one here to pay.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-CHALLENGE  (CHALLENGE LYNDS)
# ---------------------------------------------------------------------------

def v_challenge(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED
    if obj.name == "LYNDS":
        from content import lynds
        lynds.challenge(world)
        return M_HANDLED
    print(f"The {obj.desc} doesn't seem interested.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-MELEE  (KILL / ATTACK X) — one combat round per command (mechanics.md)
# ---------------------------------------------------------------------------

def v_melee(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED
    if obj.name == "MUGGER":
        from content import back_alley
        back_alley.fight_round(world)
        return M_HANDLED
    if obj.name == "WARDEN":
        from content import combat_room
        combat_room.fight_round(world)
        return M_HANDLED
    if obj.name == "WEREWOLF":
        from content import still_den
        still_den.melee(world)
        return M_HANDLED
    print(f"You can't fight the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-CLIMB  (CLIMB TREE)
# ---------------------------------------------------------------------------

def v_climb_tree(world: World) -> int:
    """CLIMB TREE parses as its own verb (particle "tree")."""
    if world.here is not None and world.here.name == "OLD-OAK":
        from content import old_oak
        old_oak.climb_tree(world)
    else:
        print("There's no tree here worth climbing.")
    return M_HANDLED


def v_climb(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED
    if obj.name == "OAK-TREE":
        from content import old_oak
        old_oak.climb_tree(world)
        return M_HANDLED
    print(f"You can't climb the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-READ  (READ SCROLL)
# ---------------------------------------------------------------------------

def v_read(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED
    from content import will
    if will.read_scroll(world, obj):
        return M_HANDLED
    if obj.text:
        print(obj.text)
    else:
        print(f"There's nothing written on the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-PUT-ON  (PUT METAL ON FORGE)
# ---------------------------------------------------------------------------

def v_put_on(world: World) -> int:
    item, target = world.prso, world.prsi
    if item is None or target is None:
        return M_NOT_HANDLED

    if item.name == "GRAVESTONE":   # PUT STONE ON GRAVE — Quest 32
        from content import gravestone
        gravestone.unload(world)
        return M_HANDLED

    player = world.player
    if player is None or item not in player.contents:
        print(f"You aren't carrying the {item.desc}.")
        return M_HANDLED

    if item.name == "RUNED-METAL" and target.name == "FORGE":
        from content import vikings
        vikings.forge_pale_blade(world)
        return M_HANDLED

    print(f"You can't put the {item.desc} on the {target.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-ACTIVATE  (ACTIVATE EARTH STONE)
# ---------------------------------------------------------------------------

def v_activate(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED
    from content import vikings
    if not vikings.activate_stone(world, obj):
        print(f"Nothing happens.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-DRINK  (bare DRINK at the Fire Pit)
# ---------------------------------------------------------------------------

def v_drink(world: World) -> int:
    from content import vikings
    if vikings.drink_contest(world):
        return M_HANDLED
    print("There's nothing here to drink.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-BUY
# ---------------------------------------------------------------------------

# mechanics.md — Economy baseline / Torch
_SHAMUS_PRICES = {"GUNPOWDER": 5, "TORCH": 3}


def v_buy(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    # Must be in Kitchen with Shamus to buy
    if world.here is None or world.here.name != "KITCHEN":
        print("There's no one here to sell you that.")
        return M_HANDLED

    if obj.name == "TORCH" and world.player is not None and obj in world.player.contents:
        from content import light
        light.exchange(world)
        return M_HANDLED

    zenni = world.globals.get("zenni", 0)
    price = _SHAMUS_PRICES.get(obj.name)
    if price is None:
        print('Shamus shakes his head. "Don\'t sell that."')
        return M_HANDLED

    if zenni < price:
        print(f"You don't have enough Zenni. (Need {price}, have {zenni}.)")
        return M_HANDLED

    player = world.player
    if player is None:
        return M_NOT_HANDLED

    world.globals["zenni"] = zenni - price
    world.move_object(obj, player)
    if obj.name == "TORCH":
        from content import light
        light.light_torch(world)   # lit from the moment of purchase
    print(
        f'Shamus takes the Zenni and slides the {obj.desc} across the counter. '
        f'"Anything else?"'
    )
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-BOARD-SHIP
# ---------------------------------------------------------------------------

_BOARD_FROM_ROOMS = frozenset({
    "DOCKS",
    "LAND-HO",
    "EMPTY-BEACH",
    "DESERT-ISLAND",
})


def v_board_ship(world: World) -> int:
    here = world.here
    if here is None or here.name not in _BOARD_FROM_ROOMS:
        print("There's no ship to board here.")
        return M_HANDLED

    # At the Docks: check disguise unless Pie Rats gone
    if here.name == "DOCKS" and not world.get_global("PIE-RATS-GONE"):
        player   = world.player
        disguise = world.objects.get("PIE-RAT-DISGUISE")
        if disguise is None or player is None or disguise not in player.contents:
            print(
                'A Pie Rat on deck looks you over with the thoroughness of '
                'someone whose job is exactly this. "You don\'t even look '
                'like a pirate." He doesn\'t move. Neither, apparently, will you.'
            )
            return M_HANDLED

    # Track where the ship is so sailing direction is correct
    if here.name in ("LAND-HO", "EMPTY-BEACH"):
        world.set_global("SHIP-OCEAN-POS", 69)   # at Kevry's island
    elif here.name == "DESERT-ISLAND":
        world.set_global("SHIP-OCEAN-POS", 0)    # at eastern sea
    else:
        world.set_global("SHIP-OCEAN-POS", None) # at docks, normal

    world.set_global("AT-SEA", False)
    deck = world.rooms.get("SHIP-DECK")
    if deck:
        world.game.enter_room(deck)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-DOCK  (DOCK — return ship to harbor)
# ---------------------------------------------------------------------------

def v_dock(world: World) -> int:
    here = world.here
    if here is None or here.name not in _SEA_ROOMS:
        print("You're not at sea.")
        return M_HANDLED

    world.set_global("AT-SEA", False)
    docks = world.rooms.get("DOCKS")
    if docks:
        world.game.enter_room(docks)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-SAIL  (SET SAIL — "sail" canonical, "set" is unknown word before it)
# ---------------------------------------------------------------------------

def v_sail(world: World) -> int:
    if world.here is None or world.here.name != "SHIP-DECK":
        print("You're not on the ship.")
        return M_HANDLED

    world.set_global("AT-SEA", True)
    # If returning from Kevry's island, place ship at open ocean square 69
    pos = world.get_global("SHIP-OCEAN-POS")
    if pos is not None:
        world.set_global("SHIP-POS-ROOM", f"OPEN-OCEAN-{pos}" if pos > 0 else "SEA-EAST")
    else:
        world.set_global("SHIP-POS-ROOM", None)
    print("You cast off and the ship moves into open water. The sails catch the wind.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-WALK preaction — intercepts at-sea movement (GO EAST/WEST, LAND)
# "LAND" is vocabulary direction; "GO EAST" is V-WALK with direction=east
# ---------------------------------------------------------------------------

def _pre_walk_at_sea(world: World) -> int:
    if not world.get_global("AT-SEA") and world.here is not None and \
            world.here.name not in _SEA_ROOMS:
        return M_NOT_HANDLED

    direction = getattr(world, "walk_dir", None)
    here = world.here
    if here is None:
        return M_NOT_HANDLED

    # LAND direction: go ashore
    if direction == "land":
        _handle_land(world)
        return M_HANDLED

    # Nautical east/west
    if direction in ("east", "west"):
        # Special case: sailing from ship deck after boarding from Kevry/Desert
        pos_room = world.get_global("SHIP-POS-ROOM")
        if here.name == "SHIP-DECK" and pos_room:
            dest = world.rooms.get(pos_room)
            world.set_global("SHIP-POS-ROOM", None)
        else:
            exit_ = here.exits.get(direction)
            if exit_ is None:
                print("There's no way to sail further in that direction.")
                return M_HANDLED
            dest = world.rooms.get(exit_.destination)
        if dest:
            if dest.name == "LAND-HO":
                world.set_global("AT-SEA", False)
            if dest.name in ("DOCKS", "SHIP-DECK"):
                world.set_global("AT-SEA", False)
            world.game.enter_room(dest)
        return M_HANDLED

    return M_NOT_HANDLED


_SEA_ROOMS = frozenset({
    "SHIP-DECK", "SEA-WEST", "SEA-MID", "SEA-EAST", "DESERT-ISLAND", "LAND-HO",
    *(f"OPEN-OCEAN-{i}" for i in range(1, 70)),
})


def _handle_land(world: World) -> None:
    here = world.here
    if here is None:
        return

    # Open Ocean square 69 → Land, Ho!
    if here.name == "OPEN-OCEAN-69":
        world.set_global("AT-SEA", False)
        land_ho = world.rooms.get("LAND-HO")
        if land_ho:
            world.game.enter_room(land_ho)
        return

    # Eastern Roundabout Sea → Desert Island
    if here.name == "SEA-EAST":
        desert = world.rooms.get("DESERT-ISLAND")
        if desert:
            world.set_global("AT-SEA", False)
            world.game.enter_room(desert)
        return

    # Desert Island or Land, Ho! → back to ship deck
    if here.name in ("DESERT-ISLAND", "LAND-HO"):
        world.set_global("AT-SEA", False)
        deck = world.rooms.get("SHIP-DECK")
        if deck:
            world.game.enter_room(deck)
        return

    print("There's no place to land here.")


# ---------------------------------------------------------------------------
# V-LIGHT  (LIGHT GUNPOWDER — starts heist fuse)
# ---------------------------------------------------------------------------

def v_light(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    if obj.name == "GUNPOWDER":
        # Must be in Mine Tunnels
        if world.here is None or world.here.name != "MINE-TUNNELS":
            print("This isn't the place for that.")
            return M_HANDLED
        print(
            "You strike the flint. The fuse catches with a sharp hiss. "
            "The gunpowder is burning. Time to leave."
        )
        world.set_global("FUSE-LIT", True)
        return M_HANDLED

    print(f"You can't light the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Mine cave-in — fires when player exits mine after lighting fuse
# ---------------------------------------------------------------------------

def _check_mine_cave_in(world: World) -> None:
    if world.get_global("FUSE-LIT") and not world.get_global("MINE-BLOWN"):
        here = world.here
        if here and here.name in ("MINE-ENTRANCE", "ROUNDABOUT-FOREST"):
            world.set_global("MINE-BLOWN", True)
            world.set_global("PIE-RATS-GONE", True)
            print(
                "A muffled BOOM shakes the ground beneath your feet. "
                "Dust and splinters billow from the mine entrance as it collapses "
                "inward. The Pie Rats go running to investigate — and the ship "
                "is unguarded."
            )


# ---------------------------------------------------------------------------
# Quest 25 / Quest 32 verbs: PRY, CLEAR, LOAD, UNLOAD, UNLOCK, PUT ON GRAVE
# ---------------------------------------------------------------------------

def v_pry(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "DRAIN":
        from content import cellar
        cellar.pry_drain(world)
        return M_HANDLED
    print("You can't get any leverage on that.")
    return M_HANDLED


def v_clear(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "DRAIN":
        from content import cellar
        cellar.clear_drain(world)
        return M_HANDLED
    if obj is not None and obj.name == "BONES":
        from content import still_den
        still_den.clear_bones(world)
        return M_HANDLED
    print("There's nothing to clear.")
    return M_HANDLED


def v_load(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "GRAVESTONE":
        from content import gravestone
        gravestone.load(world)
        return M_HANDLED
    print("That doesn't need loading.")
    return M_HANDLED


def v_unload(world: World) -> int:
    obj = world.prso
    if obj is None or obj.name in ("GRAVESTONE", "HAND-CART"):
        from content import gravestone
        gravestone.unload(world)
        return M_HANDLED
    print("That isn't loaded on anything.")
    return M_HANDLED


def v_unlock(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "CELLAR-DOOR":
        from content import cellar
        cellar.unlock_cellar_door(world)
        return M_HANDLED
    if obj is not None and obj.name == "MID-TIER-DOOR":
        from content import shrine_path
        shrine_path.unlock_key_door(world)
        return M_HANDLED
    if obj is not None and obj.name == "KEEPER-DOOR":
        from content import keeper
        keeper.unlock_door(world)
        return M_HANDLED
    print("You can't unlock that.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

def register_verbs(game) -> None:
    game.register_verb("V-OPEN",       v_open)
    game.register_verb("V-EXAMINE",    v_examine)
    game.register_verb("V-LOOK",       v_look)
    game.register_verb("V-LOOK-UP",    v_look_up)
    game.register_verb("V-POUR",       v_pour)
    game.register_verb("V-PLACE",      v_place)
    game.register_verb("V-MIX",        v_mix)
    game.register_verb("V-TURN-DIAL-LEFT",  v_turn_dial_left)
    game.register_verb("V-TURN-DIAL-RIGHT", v_turn_dial_right)
    game.register_verb("V-SEAL",       v_seal)
    game.register_verb("V-DRIVE-STAKE", v_drive_stake)
    game.register_verb("V-INVENTORY",  v_inventory)
    game.register_verb("V-SAVE",       v_save)
    game.register_verb("V-RESTORE",    v_restore)
    game.register_verb("V-TAKE",       v_take)
    game.register_verb("V-WEAR",       v_wear)
    game.register_verb("V-REMOVE",     v_remove)
    game.register_verb("V-DROP",       v_drop)
    game.register_verb("V-TALK",       v_talk)
    game.register_verb("V-GIVE",       v_give)
    game.register_verb("V-BUY",        v_buy)
    game.register_verb("V-BOARD-SHIP", v_board_ship)
    game.register_verb("V-DOCK",       v_dock)
    game.register_verb("V-SAIL",       v_sail)
    game.register_verb("V-LIGHT",      v_light)
    game.register_verb("V-PUT-ON",     v_put_on)
    game.register_verb("V-READ",       v_read)
    game.register_verb("V-CLIMB",      v_climb)
    game.register_verb("V-CLIMB-TREE", v_climb_tree)
    game.register_verb("V-MELEE",      v_melee)
    game.register_verb("V-CHALLENGE",  v_challenge)
    game.register_verb("V-PAY",        v_pay)
    game.register_verb("V-JUMP-ON",    v_jump_on)
    game.register_verb("V-DISARM",     v_disarm)
    game.register_verb("V-RAISE",      v_raise)
    game.register_verb("V-USE",        v_use)
    game.register_verb("V-PRY",        v_pry)
    game.register_verb("V-CLEAR",      v_clear)
    game.register_verb("V-LOAD",       v_load)
    game.register_verb("V-UNLOAD",     v_unload)
    game.register_verb("V-UNLOCK",     v_unlock)
    game.register_verb("V-ENTER",      v_enter)
    from content.dankhaus import litlock_input_hook
    game.register_input_hook(litlock_input_hook)
    from content.spells import cast_input_hook
    game.register_input_hook(cast_input_hook)
    game.register_verb("V-ACTIVATE",   v_activate)
    game.register_verb("V-DRINK",      v_drink)
    from content.vikings import riddle_input_hook
    game.register_input_hook(riddle_input_hook)
    # Preaction intercepts GO EAST/WEST and LAND while at sea
    game.register_preaction("V-WALK",  _pre_walk_at_sea)
