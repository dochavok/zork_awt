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

    if obj.name == "MUSIC-BOX":
        from content import music_box
        music_box.open_box(world)
        return M_HANDLED

    if obj.name == "DISPLAY-CABINET":     # Upper Hall — Quest 4 wax seal
        if world.get_global("CABINET-OPEN"):
            print("It's already open.")
        else:
            world.set_global("CABINET-OPEN", True)
            world.objects["WAX-SEAL"].clear_flag("INVISIBLE")
            print("The glass door swings open on a stiff hinge. Among the yellowed "
                  "charters and a tarnished civic medal sits a wax seal — a disc of "
                  "old red wax, stamped with the town crest.")
        return M_HANDLED

    if obj.name == "MINE-CHEST":
        from content import mid_tier
        mid_tier.open_chest(world)
        return M_HANDLED

    if obj.name == "BURIED-CHEST":
        from content import ship
        ship.open_chest(world)
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

    if obj.name == "MUSIC-BOX":           # Quest 12 — Will's hints
        from content import music_box
        music_box.examine(world)
        return M_HANDLED

    if obj.name == "WHISPERING-JAR":      # Quest 4 — discovered on a look
        from content import quests
        print(obj.examine)
        quests.discover(world, "4")
        return M_HANDLED

    # Generic examine: the examine text, else the room line. Looking at an
    # object doesn't touch it — its room listing stays the same.
    desc = obj.examine or obj.ldesc or obj.fdesc
    if desc:
        print(desc)
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


def v_score(world: World) -> int:
    from content import ending
    ending.score(world)
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
    if keeper.pour(world):
        return M_HANDLED
    if world.prso is not None and world.prso.name == "GLACIER-MELT":   # Quest 34 — only the pool
        print("You'd rather not waste it.")
        return M_HANDLED
    return M_NOT_HANDLED


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

    if obj.name == "IDOL":                # Trap 33 — off the pedestal unswapped
        from content import upper_tier
        if upper_tier.take_idol(world):
            return M_HANDLED

    if obj.name == "GUNPOWDER":
        from content import mine
        if mine.take_refused(world):
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
    if obj.name == "SILVER-DUST":
        print("You pinch the silver dust out of the crack and pocket it.")
        return M_HANDLED
    print(f"You take the {obj.desc}.")
    if obj.name == "MUSIC-BOX-KEY":
        from content import bog
        bog.key_taken(world)
    if obj.name == "GUNPOWDER":
        from content import mine
        mine.gunpowder_taken(world)
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
    if obj.name == "IVANAAR-TUNIC":   # items.md — Ivanaar's Tunic
        print("You pull the tunic on. The weave settles across your shoulders, "
              "lighter than it looks.")
        return M_HANDLED
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

    if obj.name == "GUNPOWDER":
        from content import mine
        if mine.drop_gunpowder(world):
            return M_HANDLED
    if obj.name == "SUPPORT-BEAM":        # PUT BEAM in the Gallery props it (Quest 38)
        from content import aqueduct
        if aqueduct.in_gallery(world) and not world.get_global("TIMBERS-CLEARED") \
                and int(world.get_global("TIMBERS-DOWN") or 0) >= 3:
            aqueduct.prop_passage(world)
            return M_HANDLED
    world.move_object(obj, world.here)
    print(f"You drop the {obj.desc}.")
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
        # Quest 40 — mentioned wistfully until the stew is back on the menu
        from content import quests
        if quests.get_state(world, "40") != quests.COMPLETE:
            if world.get_global("SHAMUS-HAS-THYME"):
                print('He glances at the thyme by the stove, then frowns at the pot '
                      'on the fire. "Still need a pot that isn\'t cracked."')
            elif world.get_global("SHAMUS-HAS-POT"):
                print('He glances at the new pot by the stove. "Still need that bog thyme."')
            else:
                print(
                    'He glances at the pot on the fire and frowns at it. "There\'s a '
                    "stew recipe I haven't made in years. Needs bog thyme, and a pot "
                    'that isn\'t cracked. All of mine are."'
                )
            quests.discover(world, "40")
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

    if obj.name in ("LIBRARIAN", "ARCHIVIST"):
        from content import library
        (library.talk_librarian if obj.name == "LIBRARIAN" else library.talk_archivist)(world)
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


# Quest 40 — Shamus's Recipe (quests.md; text in npcs.md, Shamus)
_SHAMUS_THYME = (
    'Shamus takes the thyme, crushes a leaf between his fingers and breathes it in. '
    '"That\'s the stuff." He sets it by the stove. "Now a pot that holds water, and '
    'we\'re in business."'
)
_SHAMUS_POT = (
    'Shamus turns the pot over, taps it, holds it up to the light. Not a crack. '
    '"Now that\'s a pot." He sets it by the stove. "Bog thyme, and we\'re in business."'
)
_SHAMUS_STEW = (
    "Shamus puts the two together like they've been waiting for each other. The "
    "kitchen fills with a smell you haven't smelled in this town before — thick, "
    'green, and warm. "Hearty stew," he says. "Back on the menu. Tell May."'
)


def _give_shamus(world: World, item) -> None:
    from content import quests
    world.move_object(item, None)          # by the stove — he keeps it
    flag = "SHAMUS-HAS-THYME" if item.name == "BOG-THYME" else "SHAMUS-HAS-POT"
    world.set_global(flag, True)
    quests.discover(world, "40")
    if world.get_global("SHAMUS-HAS-THYME") and world.get_global("SHAMUS-HAS-POT"):
        print(_SHAMUS_STEW)
        world.set_global("HEARTY-STEW", True)   # inn menu upgrade (buying food isn't built yet)
        quests.complete(world, "40")
    else:
        print(_SHAMUS_THYME if item.name == "BOG-THYME" else _SHAMUS_POT)


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

    # Bound ring to Will — the final scene and the end of the game
    if npc.name == "WILL" and item.name == "RING" and world.globals.get("ring_bound"):
        from content import ending
        ending.return_ring(world)
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

    # Bog thyme / small clay pot to Shamus — Quest 40, either order
    if npc.name == "SHAMUS" and item.name in ("BOG-THYME", "SMALL-CLAY-POT"):
        _give_shamus(world, item)
        return M_HANDLED

    # Runed metal to Pyronicus — forges the Pale Blade
    if npc.name == "PYRONICUS" and item.name == "RUNED-METAL":
        from content import vikings
        vikings.forge_pale_blade(world)
        return M_HANDLED

    # Rune stones to Ivanaar — Quest 42 → Ivanaar's Tunic
    if npc.name == "BEEKEEPER" and item.name == "QUEEN-VIAL":
        from content import old_oak
        old_oak.give_queen(world)
        return M_HANDLED
    if npc.name == "IVANAAR" and item.name in ("OLD-OAK-RUNE-STONE", "BOG-RUNE-STONE",
                                               "DUNGEON-RUNE-STONE"):
        from content import vikings
        vikings.give_stones(world)
        return M_HANDLED

    # Bone flute to Pyronicus — Quest 7 → Fireball scroll
    if npc.name == "PYRONICUS" and item.name == "BONE-FLUTE":
        from content import inscription
        inscription.give_flute(world)
        return M_HANDLED

    # Rubbing to the Archivist — Quest 28 → incantation scroll
    if npc.name == "ARCHIVIST" and item.name == "RUBBING":
        from content import library
        library.give_rubbing(world)
        return M_HANDLED

    print(f"{_npc_subject(npc)} doesn't take the {item.desc}.")
    return M_HANDLED


# NPCs known by a title rather than a name ("The Archivist").
_TITLED_NPCS = {"ARCHIVIST", "BOGGART", "WARDEN"}


def _npc_subject(npc) -> str:
    """An NPC at the start of a sentence: 'Will Passion', 'The Archivist', 'The clerk'."""
    if npc.name in _TITLED_NPCS or npc.desc[:1].islower():
        return f"The {npc.desc}"
    return npc.desc


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
    # Quest 38 — Collapsed Gallery
    if obj is not None and obj.name == "PICKAXE" and world.prsi is not None \
            and world.prsi.name == "GALLERY-TIMBERS":
        aqueduct.strike_timber(world)
        return M_HANDLED
    if obj is not None and obj.name == "SUPPORT-BEAM" and aqueduct.in_gallery(world):
        aqueduct.prop_passage(world)
        return M_HANDLED
    print("Nothing happens.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-JUMP-ON / V-DISARM  (Trap 29 plate in the Combat Room)
# ---------------------------------------------------------------------------

def v_jump_on(world: World) -> int:
    from content import combat_room, flooding
    if flooding.handles_plate(world):
        flooding.jump_on_plate(world)
        return M_HANDLED
    combat_room.jump_on_plate(world)
    return M_HANDLED


def v_struggle(world: World) -> int:
    """STRUGGLE / PULL FREE — only means something in the Trap 8 snare."""
    print("Nothing happens.")
    return M_HANDLED


def v_disarm(world: World) -> int:
    from content import combat_room, flooding
    if flooding.handles_plate(world):
        flooding.disarm_plate(world)
        return M_HANDLED
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
    raznak = world.objects.get("RAZNAK")
    if (obj is None or obj.name == "RAZNAK") and raznak is not None \
            and raznak.location is world.here:
        from content import vikings
        vikings.pay_raznak(world)
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
    if world.prso is not None and world.prso.name == "GALLERY-TIMBERS":   # HIT TIMBER
        from content import aqueduct
        aqueduct.strike_timber(world)
        return M_HANDLED
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
    if obj.name == "APPRENTICE" and not world.get_global("APPRENTICE-FREED"):
        from content import trap_side
        trap_side.fight_round(world)
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
    if obj.name == "INCANTATION-SCROLL":   # Quest 34 — only the speaking door answers
        print("You read the words under your breath. Nothing answers. Wherever these "
              "are meant to be spoken, it isn't here.")
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
# V-EAT  (EAT HONEY — Quest 24's enchanted honey)
# ---------------------------------------------------------------------------

def v_eat(world: World) -> int:
    obj = world.prso
    if obj is None or obj.name != "ENCHANTED-HONEY" or obj not in world.player.contents:
        return M_NOT_HANDLED
    from content import old_oak
    old_oak.eat_honey(world)
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
_SHAMUS_PRICES = {"GUNPOWDER": 5, "TORCH": 3, "FISHING-ROD": 8, "THIN-PAPER": 2}


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

    # At the Docks after the ship is returned: the Pie Rat Coin is the pass
    from content import ship
    if here.name == "DOCKS" and ship.boarding_refused(world):
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
# V-DOCK  (DOCK / MOOR — same action as LAND: go ashore)
# ---------------------------------------------------------------------------

def v_dock(world: World) -> int:
    _handle_land(world)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-DIG  (room actions handle their own dig spots first — Stored Room)
# ---------------------------------------------------------------------------

def v_dig(world: World) -> int:
    from content import ship
    if world.here is not None and world.here.name == "DESERT-ISLAND":
        ship.dig(world)
    else:
        print(ship.NOTHING_TO_DIG)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-FISH  (Roundabout Pond — content/pond.py)
# ---------------------------------------------------------------------------

def v_fish(world: World) -> int:
    from content import pond
    pond.fish(world)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-SAIL  (SET SAIL — "sail" canonical, "set" is unknown word before it)
# ---------------------------------------------------------------------------

def v_sail(world: World) -> int:
    if world.here is None or world.here.name != "SHIP-DECK":
        print("You're not on the ship.")
        return M_HANDLED

    world.set_global("AT-SEA", True)
    print("You cast off and the ship moves into open water. The sails catch the wind.")
    return M_HANDLED


def _sail_dir(direction: str):
    """SAIL EAST etc. — on a moored deck, casts off and moves in one turn."""
    def handler(world: World) -> int:
        here = world.here
        if here is None or here.name not in _SEA_ROOMS or here.name in (
                "DESERT-ISLAND", "LAND-HO"):
            print("You're not on the ship.")
            return M_HANDLED
        if here.name == "SHIP-DECK" and not world.get_global("AT-SEA"):
            v_sail(world)
        world.walk_dir = direction
        return world.game.perform("V-WALK")
    return handler


_NOT_UNDER_SAIL = "The ship isn't going anywhere until you set sail."


def _ship_origin(world: World):
    """The sea room the moored ship sits in (None = in harbor at the Docks)."""
    pos = world.get_global("SHIP-OCEAN-POS")
    if pos is None:
        return None
    return world.rooms.get(f"OPEN-OCEAN-{pos}" if pos > 0 else "SEA-EAST")


# ---------------------------------------------------------------------------
# V-WALK preaction — intercepts at-sea movement (GO EAST/WEST, LAND)
# "LAND" is vocabulary direction; "GO EAST" is V-WALK with direction=east
# ---------------------------------------------------------------------------

def _pre_walk_at_sea(world: World) -> int:
    direction = getattr(world, "walk_dir", None)

    # LAND direction: go ashore (answers everywhere, on the ship or not)
    if direction == "land":
        _handle_land(world)
        return M_HANDLED

    if not world.get_global("AT-SEA") and world.here is not None and \
            world.here.name not in _SEA_ROOMS:
        return M_NOT_HANDLED

    here = world.here
    if here is None:
        return M_NOT_HANDLED

    # Nautical east/west
    if direction in ("east", "west"):
        origin = here
        if here.name == "SHIP-DECK":
            # The deck sits wherever the ship is: in harbor, off Desert Island
            # (Eastern Roundabout Sea) or off Kevry's island (square 69).
            moored_at = _ship_origin(world)
            if not world.get_global("AT-SEA"):
                if moored_at is not None or direction != "west":
                    print(_NOT_UNDER_SAIL)
                    return M_HANDLED
            if moored_at is not None:
                origin = moored_at
        exit_ = origin.exits.get(direction)
        if exit_ is None:
            print("There's no way to sail further in that direction.")
            return M_HANDLED
        dest = world.rooms.get(exit_.destination)
        if dest:
            if dest.name in ("LAND-HO", "DOCKS", "SHIP-DECK"):
                world.set_global("AT-SEA", False)
            world.game.enter_room(dest)
            if dest.name == "SHIP-DECK":     # sailed back into harbor
                from content import ship
                ship.ship_returned(world)
        return M_HANDLED

    return M_NOT_HANDLED


_SEA_ROOMS = frozenset({
    "SHIP-DECK", "SEA-WEST", "SEA-MID", "SEA-EAST", "DESERT-ISLAND", "LAND-HO",
    *(f"OPEN-OCEAN-{i}" for i in range(1, 70)),
})


# Rooms that are aboard the ship (the islands are ashore)
_ABOARD_ROOMS = frozenset({
    "SHIP-DECK", "SEA-WEST", "SEA-MID", "SEA-EAST",
    *(f"OPEN-OCEAN-{i}" for i in range(1, 70)),
})

# Where the ship is → where going ashore puts you (locations.md — The Sea)
_ASHORE = {
    "SEA-WEST": "DOCKS",
    "SEA-EAST": "DESERT-ISLAND",
    "OPEN-OCEAN-69": "LAND-HO",
}


def _handle_land(world: World) -> None:
    """DOCK / LAND / MOOR / MAKE LAND — one action: go ashore where there's
    land beside the ship."""
    here = world.here
    if here is None or here.name not in _ABOARD_ROOMS:
        print("You're not on a ship.")
        return

    # On the deck the ship is wherever it's moored (None = in harbor)
    at = here
    if here.name == "SHIP-DECK":
        at = _ship_origin(world)
    dest = world.rooms.get(_ASHORE.get(at.name, "")) if at is not None else None
    if dest is None:
        print("There's no place to land here.")
        return

    world.set_global("AT-SEA", False)
    world.game.enter_room(dest)
    if dest.name == "DOCKS":
        from content import ship
        ship.ship_returned(world)


def make_land_input_hook(world: World, text: str) -> bool:
    """MAKE LAND — "make" is a parser verb with its own syntax."""
    if text.lower().split() == ["make", "land"]:
        _handle_land(world)
        return True
    return False


# ---------------------------------------------------------------------------
# V-TURN-ON / V-LAMP-ON  (TURN ON LANTERN — the Guardian's Lantern)
# ---------------------------------------------------------------------------

def v_turn_on(world: World) -> int:
    obj = world.prso
    if obj is None or obj.name != "GUARDIANS-LANTERN" or obj not in world.player.contents:
        return M_NOT_HANDLED
    from content import dark_branch
    dark_branch.light_lantern(world)
    return M_HANDLED


# ---------------------------------------------------------------------------
# V-LIGHT  (LIGHT GUNPOWDER — starts heist fuse)
# ---------------------------------------------------------------------------

def v_light(world: World) -> int:
    obj = world.prso
    if obj is None:
        return M_NOT_HANDLED

    if obj.name == "GUNPOWDER":
        from content import mine
        mine.light_gunpowder(world)
        return M_HANDLED

    if obj.name == "GUARDIANS-LANTERN" and obj in world.player.contents:
        from content import dark_branch
        dark_branch.light_lantern(world)
        return M_HANDLED

    if obj.name == "IVORY-TORCH":         # a source of heat, never of light
        print("It doesn't need lighting. The heat is already there.")
        return M_HANDLED

    print(f"You can't light the {obj.desc}.")
    return M_HANDLED


# ---------------------------------------------------------------------------
# Quest 25 / Quest 32 verbs: PRY, CLEAR, LOAD, UNLOAD, UNLOCK, PUT ON GRAVE
# ---------------------------------------------------------------------------

def v_pry(world: World) -> int:
    obj = world.prso
    if obj is not None and obj.name == "DRAIN":
        from content import cellar
        cellar.pry_drain(world)
        return M_HANDLED
    if obj is not None and obj.name == "IDOL-DOOR":
        from content import upper_tier
        upper_tier.pry_idol_door(world)
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


# ---------------------------------------------------------------------------
# V-DESTROY / V-PROP  (Quest 38 — Collapsed Gallery timbers)
# ---------------------------------------------------------------------------

def v_destroy(world: World) -> int:
    if world.prso is not None and world.prso.name == "GALLERY-TIMBERS":   # BREAK / CHOP TIMBER
        from content import aqueduct
        aqueduct.strike_timber(world)
        return M_HANDLED
    return M_NOT_HANDLED


def v_prop(world: World) -> int:
    from content import aqueduct
    names = {o.name for o in (world.prso, world.prsi) if o is not None}
    if aqueduct.in_gallery(world) and names & {"SUPPORT-BEAM", "GALLERY-TIMBERS"}:
        if world.objects["SUPPORT-BEAM"] in world.player.contents \
                or world.get_global("TIMBERS-CLEARED"):
            aqueduct.prop_passage(world)
            return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# V-SWAP  (SWAP IDOL WITH SALT — Trap 33)
# ---------------------------------------------------------------------------

def v_swap(world: World) -> int:
    names = {o.name for o in (world.prso, world.prsi) if o is not None}
    if "IDOL" in names:
        from content import upper_tier
        upper_tier.swap_idol(world)
        return M_HANDLED
    print("There's nothing here to swap.")
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
    if obj is not None and obj.name == "MUSIC-BOX":
        from content import music_box
        music_box.open_box(world)
        return M_HANDLED
    if obj is not None and obj.name == "MINE-CHEST":
        from content import mid_tier
        mid_tier.open_chest(world)
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
    game.register_verb("V-SCORE",      v_score)
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
    for d in ("north", "south", "east", "west"):
        game.register_verb(f"V-SAIL-{d.upper()}", _sail_dir(d))
    game.register_verb("V-DIG",        v_dig)
    game.register_verb("V-FISH",       v_fish)
    game.register_verb("V-LIGHT",      v_light)
    game.register_verb("V-TURN-ON",    v_turn_on)
    game.register_verb("V-LAMP-ON",    v_turn_on)
    game.register_verb("V-PUT-ON",     v_put_on)
    game.register_verb("V-READ",       v_read)
    game.register_verb("V-CLIMB",      v_climb)
    game.register_verb("V-CLIMB-TREE", v_climb_tree)
    game.register_verb("V-MELEE",      v_melee)
    game.register_verb("V-CHALLENGE",  v_challenge)
    game.register_verb("V-PAY",        v_pay)
    game.register_verb("V-SWAP",       v_swap)
    game.register_verb("V-DESTROY",    v_destroy)
    game.register_verb("V-PROP",       v_prop)
    game.register_verb("V-JUMP-ON",    v_jump_on)
    game.register_verb("V-DISARM",     v_disarm)
    game.register_verb("V-STRUGGLE",   v_struggle)
    from content import whispering_jar
    game.register_verb("V-DUST",       whispering_jar.v_dust)
    game.register_verb("V-PUSH",       whispering_jar.v_push)
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
    game.register_verb("V-EAT",        v_eat)
    from content.vikings import riddle_input_hook
    game.register_input_hook(riddle_input_hook)
    # Preaction intercepts GO EAST/WEST and LAND while at sea
    game.register_preaction("V-WALK",  _pre_walk_at_sea)
