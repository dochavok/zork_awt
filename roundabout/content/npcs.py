"""
NPC dialogue trees for Roundabout: The God-Forsaken Ring.

Sourced from AWT_story_line/npcs.md, locations.md, quests.md.
All dialogue text is authoritative -- do not alter without updating source docs.

dispatch_talk(world, npc) -> int
dispatch_give(world, obj, npc) -> int
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World, GameObject


# ---------------------------------------------------------------------------
# Public dispatch
# ---------------------------------------------------------------------------

def dispatch_talk(world: "World", npc: "GameObject") -> int:
    handlers = {
        "may":          _talk_may,
        "shamus":       _talk_shamus,
        "ty":           _talk_ty,
        "will":         _talk_will,
        "litlock":      _talk_litlock,
        "archivist":    _talk_archivist,
        "librarian":    _talk_librarian,
        "toll-keeper":  _talk_toll_keeper,
        "boggart":      _talk_boggart,
        "child":        _talk_child,
        "beekeeper":    _talk_beekeeper,
        "priest":       _talk_priest,
        "mugger":       _talk_mugger,
        "knight":       _talk_knight,
        "archer":       _talk_archer,
        "raznak":       _talk_raznak,
        "lynds":        _talk_lynds,
        "ivanaar":      _talk_ivanaar,
        "haalvar":      _talk_haalvar,
        "aylora":       _talk_aylora,
        "pyronicus":    _talk_pyronicus,
        "kevry":        _talk_kevry,
        "rowan":        _talk_rowan,
        "records-worker": _talk_records_worker,
        "soldier":      _talk_soldier,
        "viking-1":     _talk_viking,
        "viking-2":     _talk_viking,
        "viking-3":     _talk_viking,
        "unnamed-child": _talk_unnamed_child,
    }
    handler = handlers.get(npc.name)
    if handler:
        return handler(world, npc)
    print(f"{npc.desc or npc.name} doesn't seem interested in conversation.")
    return M_HANDLED


def dispatch_give(world: "World", obj: "GameObject", npc: "GameObject") -> int:
    from content.quests import complete, is_complete, discover, start
    from content.experience import award_xp

    g = world.globals
    npc_key = npc.name
    obj_key = obj.name

    # --- May ---
    if npc_key == "may":
        if obj_key == "shamus-recipe" and not is_complete(world, "40"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, None)
            g["hearty_stew_available"] = True
            complete(world, "40")
            print(
                "May turns the recipe card over, reading. "
                "\"Shamus,\" she says, as if that explains everything. "
                "\"I'll make it tomorrow.\" She tucks it into her apron. "
                "\"You'll be able to order the stew from now on.\""
            )
            return M_HANDLED

    # --- Will ---
    if npc_key == "will":
        if obj_key in ("glasses", "enchanted-glasses") and not is_complete(world, "53"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, npc)
            xp_val = 20 if obj_key == "enchanted-glasses" else 10
            complete(world, "53", xp_override=xp_val)
            if obj_key == "enchanted-glasses":
                print(
                    "Will puts them on. Blinks twice. "
                    "\"These are mine. The real ones.\" He turns them over in his hands. "
                    "\"I thought they were just lost.\" A beat. "
                    "\"Thank you.\""
                )
            else:
                print(
                    "Will accepts the plain glasses. Puts them on. "
                    "\"Oh. These aren't enchanted.\" He sounds mildly disappointed. "
                    "\"But they're mine. Thank you.\""
                )
            return M_HANDLED

        if obj_key in scroll_names() and not is_complete(world, "56"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            # Check glasses block
            if g.get("enchanted_glasses_worn") or g.get("actually_enchanted_glasses_worn"):
                print(
                    "\"Take those off. I can't teach someone who already thinks "
                    "they can see everything.\""
                )
                return M_HANDLED
            _will_teach_scroll(world, obj)
            return M_HANDLED

        if obj_key == "dragon-nip":
            return _will_receive_dragon_nip(world, obj, npc)

    # --- Child ---
    if npc_key == "child":
        if obj_key == "kite" and not is_complete(world, "41"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, None)
            complete(world, "41")
            print(
                "The child reaches up for it with both hands. "
                "For a moment they just hold it -- not flying it, just holding it. "
                "Then they look up at you. They don't say anything. "
                "They don't need to."
            )
            return M_HANDLED

    # --- Beekeeper ---
    if npc_key == "beekeeper":
        if obj_key == "smoker" and not is_complete(world, "24"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, npc)
            g["enchanted_honey_available"] = True
            complete(world, "24")
            honey = world.objects.get("enchanted-honey")
            if honey:
                world.move_object(honey, world.here)
            print(
                "The beekeeper's face changes -- something that had been clenched in it "
                "finally lets go. \"My smoker. Yes. Thank you.\" "
                "He turns to the hives. \"Come back tomorrow -- I'll have honey.\"\n\n"
                "He gestures toward the shelf beside the hives. "
                "A jar of enchanted honey is already there."
            )
            return M_HANDLED

    # --- Archivist ---
    if npc_key == "archivist":
        if obj_key == "rubbing" and not is_complete(world, "28"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, npc)
            complete(world, "28")
            # Archivist gives incantation scroll
            scroll = world.objects.get("incantation-scroll")
            if scroll:
                world.move_object(scroll, world.player)
            print(
                "He takes the rubbing and holds it to the light without speaking for a moment.\n\n"
                "\"Yes.\" He sets it down flat, smoothing the edges. "
                "\"This appears to be an answer to a question I was never able to find.\" "
                "He opens a drawer and produces a rolled scroll. "
                "\"Take this. I've had it for years -- couldn't place it. "
                "I suspect you'll find the question before I would.\""
            )
            return M_HANDLED

    # --- Toll Keeper / Boggart ---
    if npc_key in ("toll-keeper", "boggart"):
        if obj_key == "charter":
            return _give_charter_to_boggart(world, obj, npc)
        if obj.value > 0 or obj_key in ("coin", "zenni"):
            return _pay_toll(world, obj, npc)

    # --- Records Worker ---
    if npc_key == "records-worker":
        if obj_key == "pocket-watch" and not is_complete(world, "17"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, npc)
            complete(world, "17")
            charter = world.objects.get("town-charter")
            if charter:
                world.move_object(charter, world.player)
            print(
                "He takes the watch. Turns it over. "
                "His expression changes -- quietly, privately.\n\n"
                "\"This belonged to my uncle,\" he says. \"I thought it was lost.\" "
                "He sets it down on the desk with care. "
                "\"The charter. Here.\" He opens a drawer and produces it. "
                "\"I don't know where you found that, but -- thank you.\""
            )
            return M_HANDLED

    # --- Rowan Finch ---
    if npc_key == "rowan":
        if obj_key == "gravestone" and not is_complete(world, "32"):
            if obj.location is not world.player:
                print("You don't have that.")
                return M_HANDLED
            world.move_object(obj, world.here)
            key = world.objects.get("mid-tier-key")
            if key:
                world.move_object(key, world.player)
            complete(world, "32")
            print(
                "Rowan Finch stands and looks at the gravestone for a long moment. "
                "He reaches out and touches the carved letters -- his grandfather's name.\n\n"
                "\"I hadn't realized how much it mattered until it was gone,\" he says. "
                "He turns back to you. \"Here.\" He takes a key from his desk. "
                "\"This unlocks the main passage to the middle tier. "
                "My grandfather left it in our family's care. "
                "I think he'd approve of where it's going.\""
            )
            return M_HANDLED

    # --- Ivanaar ---
    if npc_key == "ivanaar":
        if obj_key == "runed-metal" and not is_complete(world, "57"):
            print("Ivanaar already knows about the metal -- it came from here.")
            return M_HANDLED

    # --- Raznak ---
    if npc_key == "raznak":
        if obj_key in ("coin", "zenni") or obj.value >= 3:
            return _pay_raznak(world, obj, npc)

    # --- Kevry ---
    if npc_key == "kevry":
        if obj_key in ("glasses", "enchanted-glasses"):
            return _kevry_receive_glasses(world, obj)

    print(f"{npc.desc or npc.name} has no use for that.")
    return M_HANDLED


def scroll_names():
    return {"light-scroll", "unbind-scroll", "fireball-scroll"}


# ---------------------------------------------------------------------------
# Will Passion helpers
# ---------------------------------------------------------------------------

def _will_teach_scroll(world: "World", obj) -> None:
    spell_map = {
        "light-scroll":    "spell_light",
        "unbind-scroll":   "spell_unbind_undead",
        "fireball-scroll": "spell_fireball",
    }
    key = spell_map.get(obj.name)
    if not key:
        return

    if world.globals.get(key):
        print("You already know this spell.")
        return

    world.globals[key] = True
    world.move_object(obj, None)

    from content.quests import complete, is_complete
    if not is_complete(world, "56"):
        complete(world, "56")

    print(
        "Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, "
        "reading silently for a moment. Then he reads it aloud -- not to you, exactly, "
        "more as if the words need to be heard in the right kind of room. "
        "When he finishes, you understand it. You're not sure how. "
        "\"Keep that,\" he says, nodding at the space where the scroll was. "
        "It's gone. \"The knowing, I mean.\""
    )


def _will_receive_dragon_nip(world: "World", obj, npc) -> int:
    from content.quests import complete, is_complete
    if is_complete(world, "58"):
        print("Will already has what he needed.")
        return M_HANDLED
    if obj.location is not world.player:
        print("You don't have that.")
        return M_HANDLED

    world.move_object(obj, None)
    complete(world, "58")

    # Award dragon scale
    scale = world.objects.get("dragon-scale")
    if scale:
        world.move_object(scale, world.player)

    print(
        "He takes it from you. Stares at it for a moment -- not at you, at it.\n\n"
        "\"I've been looking for that.\"\n\n"
        "He sets it on the desk. Opens a low drawer and produces a scale -- large, gold, "
        "catching the light like a mirror that's decided to be something else. He holds it out.\n\n"
        "\"Where did you find it?\"\n\n"
        "He asks it the way someone asks a question they already suspect the answer to. "
        "He doesn't wait for a response.\n\n"
        "\"Never mind.\"\n\n"
        "He turns back to his work."
    )
    return M_HANDLED


# ---------------------------------------------------------------------------
# Toll / charter helpers
# ---------------------------------------------------------------------------

def _pay_toll(world: "World", obj, npc) -> int:
    from content.quests import complete, is_complete
    g = world.globals
    toll = 3

    if g.get("zenni", 0) < toll:
        print("\"Not enough,\" the toll keeper says flatly.")
        return M_HANDLED

    g["zenni"] -= toll
    g["toll_paid"] = True
    complete(world, "27")
    print(
        "The toll keeper takes the coins without looking at them. "
        "\"Through you go.\" The gate lifts."
    )
    return M_HANDLED


def _give_charter_to_boggart(world: "World", obj, npc) -> int:
    from content.quests import complete, is_complete
    if obj.location is not world.player:
        print("You don't have that.")
        return M_HANDLED

    world.move_object(obj, None)
    world.globals["boggart_evicted"] = True

    # Boggart leaves, drops strongbox
    strongbox = world.objects.get("strongbox")
    if strongbox:
        world.move_object(strongbox, world.here)

    # Move boggart out
    npc_obj = world.objects.get("boggart")
    if npc_obj:
        world.move_object(npc_obj, None)

    print(
        "The boggart reads it. Reads it again. His expression shifts through several emotions, "
        "none of them convenient for him.\n\n"
        "\"Fine,\" he says, with the dignity of someone who has no dignity left. "
        "\"Fine.\" He picks up a small strongbox from beside the bridge post, "
        "sets it down with a thump, and walks away without looking back.\n\n"
        "The bridge is clear."
    )
    return M_HANDLED


def _pay_raznak(world: "World", obj, npc) -> int:
    g = world.globals
    if g.get("zenni", 0) < 3:
        print("\"Come back when you do.\"")
        return M_HANDLED

    cls = g.get("player_class", "")
    if cls == "rogue":
        print("Raznak already gave you the bow.")
        return M_HANDLED

    g["zenni"] -= 3
    g["archery_skill"] = True

    bow = world.objects.get("bow")
    if bow and bow.location is not world.player:
        world.move_object(bow, world.player)

    g["raznak_stage"] = 3

    from content.quests import complete, is_complete
    if not is_complete(world, "55"):
        complete(world, "55")

    print(
        "Raznak watches you complete the final drill. He is quiet for a moment "
        "in the way of someone making a decision they've already made.\n\n"
        "\"You're not a natural,\" he says. \"You worked for it. That's better.\"\n\n"
        "He takes a bow from the rack -- slightly better than the practice ones, "
        "strung tight, balanced.\n\n"
        "\"This one's yours. It'll tell you when you're doing it wrong.\"\n\n"
        "He pauses.\n\n"
        "\"Most bows don't. This one does. Pay attention to it.\""
    )
    return M_HANDLED


def _kevry_receive_glasses(world: "World", obj) -> int:
    if obj.location is not world.player:
        print("You don't have that.")
        return M_HANDLED

    if not obj.has_flag("WEARING"):
        print(
            "\"You've got something in there,\" Kevry says, not looking up. "
            "\"Did you not bring them?\""
        )
        return M_HANDLED

    if obj.name != "enchanted-glasses":
        print(
            "Kevry looks at the glasses, then at you. "
            "\"These are plain. Will needs to enchant them first -- or you need to find the ones that are.\""
        )
        return M_HANDLED

    if world.globals.get("kevry_enchanted"):
        print("\"Already done,\" Kevry says. \"They're as good as they'll get.\"")
        return M_HANDLED

    world.globals["kevry_enchanted"] = True
    print(
        "Kevry looks at the glasses, then at you, then at the glasses again. "
        "\"Will sent you.\" It isn't a question. "
        "He takes them gently. \"Interesting that he didn't come himself.\" "
        "He does something brief and private with them that you don't quite follow. "
        "When he hands them back they feel different. "
        "Lighter, somehow, and more certain. \"There. Don't lose them.\""
    )
    return M_HANDLED


# ---------------------------------------------------------------------------
# Individual NPC talk handlers
# ---------------------------------------------------------------------------

def _talk_may(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "may"):
        return M_HANDLED

    g = world.globals
    stage = g.get("may_stage", 0)

    if stage == 0:
        name = g.get("player_name", "")
        print(
            "A woman behind the bar glances up as you come in -- "
            "shoulder-length red hair, appraisal done in about a second, apparently satisfactory.\n\n"
            "\"New face,\" she says, not unkindly. \"I'm May. "
            "Drinks are two Zenni, food's the same -- keeps you on your feet longer than you'd think. "
            "Rooms are upstairs if you need to sleep it off properly.\"\n\n"
            "She sets a glass down and leans one hand on the bar.\n\n"
            "\"If you get stuck on something and want a nudge in the right direction, money talks. "
            "Shamus is in the kitchen if you need supplies -- he keeps more than recipes back there.\"\n\n"
            "She picks the glass back up and goes back to work. "
            "The conversation is over when she decides it is."
        )
        g["may_stage"] = 1
        g["may_met"] = True
        from content.quests import discover
        discover(world, "51")
    elif stage == 1:
        print(
            "May refills a glass without looking at it. "
            "\"You need something? Buy a drink, tip me, or rent a room. "
            "I don't give advice for free, but I don't charge more than it's worth.\""
        )
    else:
        name = g.get("player_name", "")
        greeting = f"May glances at you. \"{name},\" she says" if name else "May glances at you"
        print(
            f"{greeting}. \"Still here. "
            "Bar's open, board's open, my ears are open.\""
        )
    return M_HANDLED


def _talk_shamus(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "shamus"):
        return M_HANDLED

    g = world.globals
    if not g.get("shamus_met"):
        print(
            "Shamus looks up from whatever he's doing -- it's hard to tell what it is. "
            "\"Shamus. I sell things.\" He gestures at the spread behind him. "
            "\"Gunpowder, journal, fishing rod, torches. "
            "Prices are fair. BUY to get something; I'll buy back at half price if you change your mind.\""
        )
        g["shamus_met"] = True
    else:
        print(
            "Shamus's attention is somewhere else. "
            "\"You know what I've got. BUY if you want something.\""
        )
    return M_HANDLED


def _talk_ty(world: "World", npc: "GameObject") -> int:
    g = world.globals
    if not g.get("ty_met"):
        print(
            "Ty looks up. He has the particular stillness of someone who has been waiting "
            "for a reason to stop waiting.\n\n"
            "\"Ty. I run the game in the corner.\" He slides a die toward you "
            "and catches it before it falls off the edge. "
            "\"Ship, Captain, and Crew. Bet one to five Zenni. "
            "You win if you get a six, five, and four -- "
            "and the remaining two dice sum to fifteen or more.\"\n\n"
            "A pause. \"Want to play?\""
        )
        g["ty_met"] = True
    else:
        print("Ty raises an eyebrow. \"Table's open. PLAY CARGO to start.\"")
    return M_HANDLED


def _talk_will(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "will"):
        return M_HANDLED

    g = world.globals
    here = world.here.name if world.here else ""
    stage = g.get("will_stage", 0)

    if here not in ("wills-tower-main", "wills-bedroom", "wills-study"):
        print("Will Passion is not here.")
        return M_HANDLED

    if stage == 0:
        print(
            "Will looks at you over the rim of whatever he's reading. "
            "The glasses he's wearing are not quite right -- "
            "they're plain where they should be enchanted.\n\n"
            "\"You're not one of my students.\" Not a question. "
            "\"If you need something, say it plainly.\""
        )
        g["will_stage"] = 1
        g["will_met"] = True
        from content.quests import discover
        discover(world, "53")
        discover(world, "56")
        return M_HANDLED

    if stage == 1:
        cls = g.get("player_class", "")
        name = g.get("player_name", "")
        if cls == "mage":
            print(
                "Will sets his book down. \"You have some training, then.\" "
                "He says it the way someone says it when they're about to give you more. "
                "\"Bring me the scrolls. I'll walk you through them -- not the words, "
                "the meaning behind the words. The words you can read yourself.\""
            )
        else:
            print(
                "Will nods slowly. \"You're not a mage. "
                "The scrolls won't open for you on their own.\" "
                "He picks up his book again. "
                "\"Bring them here. I can translate.\""
            )
        g["will_stage"] = 2
        return M_HANDLED

    # Subsequent visits -- tower exit sarcasm if player seems stuck
    if here == "wills-tower-main" and not g.get("ring_quest_started"):
        exits_msg = random.choice([
            "Will doesn't look up. \"Guild hall,\" he says. Just those two words. Then silence.",
            "\"I dispatched you on a quest involving a cursed ring and a man whose roof it fell through, "
            "and your first obstacle is... leaving the room.\" He picks his pen back up. \"Take your time.\"",
            "\"The tower does not have a front door per se. Look around. I find that helps.\"",
            "Will peers at you over his spectacles. "
            "\"You found a mailbox in a field and opened it. "
            "I have every confidence you'll solve this.\"",
        ])
        print(exits_msg)
        return M_HANDLED

    # Ring return
    ring = world.objects.get("ring")
    if ring and ring.location is world.player and g.get("ring_bound"):
        _will_ring_return(world)
        return M_HANDLED

    print(
        "Will glances up. \"Still around. Good. "
        "Bring me what you find -- some things only make sense when someone explains them.\""
    )
    return M_HANDLED


def _will_ring_return(world: "World") -> None:
    ring = world.objects.get("ring")
    if ring:
        world.move_object(ring, world.objects.get("will"))
    world.globals["ring_quest_complete"] = True
    print(
        "You hold out the ring.\n\n"
        "Will takes it. Holds it for a moment, not examining it -- listening to it, "
        "if that's the right word. Then he sets it on the desk.\n\n"
        "\"Well done.\"\n\n"
        "Two words. But the weight behind them is considerable.\n\n"
        "He picks up his pen."
    )
    from content.experience import award_xp
    award_xp(world, 50)


def _talk_litlock(world: "World", npc: "GameObject") -> int:
    g = world.globals
    here = world.here.name if world.here else ""

    if here not in ("dankhaus", "dankhaus-main"):
        print("Litlock is not here.")
        return M_HANDLED

    # Ward check
    if g.get("ring_worn") and not g.get("lynds_invitation"):
        print(
            "Litlock is here. He glances toward you -- or toward where you are -- "
            "with the unhurried attention of someone who has seen stranger things. "
            "Then he waits. He does not speak."
        )
        return M_HANDLED

    stage = g.get("litlock_stage", 0)

    if stage == 0:
        print(
            "Litlock looks up from whatever he's doing with the particular alertness "
            "of someone who has been waiting for company without admitting it to himself. "
            "He takes you in. Then he grins -- wide, genuine, the kind that arrives before "
            "the person decides to smile.\n\n"
            "\"Right,\" he says. \"Entertain me.\""
        )
        g["litlock_stage"] = 1
        g["litlock_met"] = True
        from content.quests import discover, start
        start(world, "52")
        return M_HANDLED

    if stage in (1, 2):
        _litlock_tier1(world, g)
        return M_HANDLED

    if stage == 3:
        print(
            "Litlock glances up. His expression has the quality of someone "
            "who remembers a good laugh. \"Back again,\" he says. \"Good.\""
        )
        return M_HANDLED

    return M_HANDLED


def _litlock_tier1(world: "World", g: dict) -> None:
    """Quest 52 -- Make Litlock Laugh: 2x2x2 dialogue tree."""
    print(
        "Litlock waits.\n\n"
        "  A) Tell a joke\n"
        "  B) Do something physical\n\n"
        "(Type A or B, or just choose one.)"
    )
    g["litlock_awaiting_tier1"] = True


def litlock_tier1_choice(world: "World", choice: str) -> None:
    g = world.globals
    if not g.get("litlock_awaiting_tier1"):
        return

    g.pop("litlock_awaiting_tier1", None)
    choice = choice.strip().lower()

    if choice in ("a", "joke", "tell"):
        print(
            "You clear your throat. \"I have a joke.\"\n\n"
            "Litlock leans back. \"Everyone has a joke. Let's see if yours is different.\"\n\n"
            "  A1) Wordplay / pun\n"
            "  A2) Absurdist observation"
        )
        g["litlock_path"] = "A"
        g["litlock_awaiting_tier2"] = True
    elif choice in ("b", "physical", "do"):
        print(
            "You don't say anything. You just do something.\n\n"
            "Litlock watches with the focused attention of a man who has seen "
            "a great deal and is genuinely curious whether this will be new.\n\n"
            "  B1) Something dignified\n"
            "  B2) Something completely committed and ridiculous"
        )
        g["litlock_path"] = "B"
        g["litlock_awaiting_tier2"] = True
    else:
        print("Litlock waits. (Type A or B.)")
        g["litlock_awaiting_tier1"] = True


def litlock_tier2_choice(world: "World", choice: str) -> None:
    g = world.globals
    if not g.get("litlock_awaiting_tier2"):
        return

    g.pop("litlock_awaiting_tier2", None)
    path = g.get("litlock_path", "A")
    choice = choice.strip().lower()

    if path == "A":
        if choice in ("a1", "pun", "wordplay", "1"):
            print(
                "You deliver the pun. It lands with the particular thud of something "
                "that was never going to work.\n\n"
                "Litlock stares at you for a moment. "
                "\"That,\" he says carefully, \"was a pun. "
                "I respect that you tried. I do not respect the pun.\" "
                "He waves a hand. \"Again.\""
            )
            g["litlock_stage"] = 1  # loop to tier 1
            g["litlock_awaiting_tier1"] = True
        elif choice in ("a2", "absurdist", "observation", "2"):
            print(
                "\"You know,\" you say, \"I've been thinking about the bog. "
                "Specifically about the smell. And I think the smell isn't the bog at all -- "
                "I think the bog smells fine and it's everything else that's wrong.\"\n\n"
                "Litlock blinks. Then something shifts in his expression -- "
                "not quite a laugh yet, but its immediate predecessor.\n\n"
                "\"Go on,\" he says.\n\n"
                "  C1) Push further\n"
                "  C2) Explain it"
            )
            g["litlock_path"] = "A2"
            g["litlock_awaiting_tier3"] = True
        else:
            print("(Type A1 or A2.)")
            g["litlock_awaiting_tier2"] = True
    else:  # path B
        if choice in ("b1", "dignified", "bow", "1"):
            print(
                "You execute a formal bow. Precise. Respectful. Technically flawless.\n\n"
                "Litlock watches the whole thing. "
                "\"That was very well done,\" he says. "
                "\"I am completely unmoved. Try something else.\""
            )
            g["litlock_stage"] = 1
            g["litlock_awaiting_tier1"] = True
        elif choice in ("b2", "ridiculous", "floor", "2"):
            print(
                "You sit down on the floor. Not because there's nowhere to sit -- "
                "there are chairs. You just sit on the floor, look up at Litlock, and wait.\n\n"
                "Litlock looks at you. Looks at the chairs. Looks back at you.\n\n"
                "Something in his face is working very hard not to become a laugh.\n\n"
                "\"Why,\" he says carefully, \"are you on the floor?\"\n\n"
                "  C1) Push further\n"
                "  C2) Explain it"
            )
            g["litlock_path"] = "B2"
            g["litlock_awaiting_tier3"] = True
        else:
            print("(Type B1 or B2.)")
            g["litlock_awaiting_tier2"] = True


def litlock_tier3_choice(world: "World", choice: str) -> None:
    from content.quests import complete, is_complete
    g = world.globals
    if not g.get("litlock_awaiting_tier3"):
        return

    g.pop("litlock_awaiting_tier3", None)
    path = g.get("litlock_path", "A2")
    choice = choice.strip().lower()

    if choice in ("c1", "push", "further", "1"):
        if path == "A2":
            extra = (
                "\"In fact,\" you continue, with complete conviction, "
                "\"I think the bog has been unfairly maligned for years, "
                "and someone should apologize to it.\""
            )
        else:
            extra = (
                "You look up at him from the floor. "
                "\"I find it clarifying,\" you say. \"You should try it.\""
            )

        print(
            f"{extra}\n\n"
            "That does it.\n\n"
            "Litlock laughs -- fully, completely, the kind of laugh that takes over a person entirely. "
            "He laughs until he has to put something down. "
            "He laughs until Aurix appears in the doorway to see what's happening "
            "and then disappears again.\n\n"
            "When he finally stops, he wipes his eyes, looks at you with something that might be respect, "
            "and reaches over and bonks you firmly on the top of the head with two knuckles.\n\n"
            "\"There,\" he says. \"You'll see things a bit differently now. "
            "Don't ask me to explain it.\"\n\n"
            "He picks up whatever he put down and goes back to it, still smiling."
        )
        g["litlock_bonked"] = True
        g["litlock_stage"] = 3
        # Chuckle House becomes visible
        g["chuckle_house_visible"] = True
        if not is_complete(world, "52"):
            complete(world, "52")

    elif choice in ("c2", "explain", "2"):
        if path == "A2":
            reaction = (
                "\"What I mean is,\" you begin, "
                "\"the fundamental olfactory baseline of--\"\n\n"
                "Litlock holds up a hand. \"Stop. You were almost there. "
                "You explained it. You can never explain it.\" "
                "He shakes his head with genuine sadness. \"Again.\""
            )
        else:
            reaction = (
                "\"It's a metaphor,\" you say. \"For groundedness. For--\"\n\n"
                "Litlock closes his eyes briefly. \"You were right there,\" he says. "
                "\"Right there. And then you talked.\" He opens his eyes. \"Again.\""
            )
        print(reaction)
        g["litlock_stage"] = 1
        g["litlock_awaiting_tier1"] = True
    else:
        print("(Type C1 or C2.)")
        g["litlock_awaiting_tier3"] = True


def _talk_archivist(world: "World", npc: "GameObject") -> int:
    g = world.globals
    stage = g.get("archivist_stage", 0)

    if stage == 0:
        print(
            "He looks up when spoken to, marking his place with two fingers "
            "before setting the book aside.\n\n"
            "\"Yes. I've been trying to authenticate a map -- provenance is unclear, "
            "which makes it nearly useless for the purpose I need it for. "
            "There's an engraving in the lower passages that should settle the question, "
            "if I could get a clean impression of it.\"\n\n"
            "He glances at the table, then back.\n\n"
            "\"I can't leave this. If you're heading down that way -- "
            "thin paper, a stick of charcoal, and some patience. "
            "The engraving is in the Inscription Chamber. You'll know it when you see it.\""
        )
        g["archivist_stage"] = 1
        g["archivist_met"] = True
        from content.quests import discover
        discover(world, "28")

    elif stage == 1:
        from content.quests import is_complete
        if is_complete(world, "28") and not is_complete(world, "34"):
            print(
                "He is already working when you arrive.\n\n"
                "\"Whatever that engraving answers -- I suspect it's somewhere in "
                "the lower passages. Somewhere that feels like it's waiting.\" "
                "He doesn't look up. \"That's not intuition. That's just what the text implies.\""
            )
        elif is_complete(world, "34"):
            print(
                "\"The soldier.\" He says it quietly, to himself as much as to you. "
                "\"I had assumed the chamber was ceremonial. Not occupied.\" "
                "He makes a note. \"Thank you for telling me.\""
            )
            g["archivist_stage"] = 2
        else:
            print(
                "He glances up. \"Thin paper, charcoal. "
                "The Inscription Chamber, lower tier. Have you been down yet?\""
            )

    else:
        print("He nods at you and goes back to his maps.")

    return M_HANDLED


def _talk_librarian(world: "World", npc: "GameObject") -> int:
    g = world.globals
    stage = g.get("librarian_stage", 0)

    if stage == 0:
        print(
            "She sets down what she's holding and folds her hands on the desk. "
            "Her voice arrives in pieces -- tones and rhythms that don't quite match, "
            "stitched together at the seams.\n\n"
            "\"I have been waiting for\" someone \"to come asking.\"\n\n"
            "She pulls a thin ledger from under the desk without looking for it.\n\n"
            "\"'The Veil of the Arcane -- I need access to whatever you have.' "
            "That's what he said. First thing. Didn't introduce himself. I didn't ask.\"\n\n"
            "She opens the ledger to a marked page.\n\n"
            "\"He was here for --\" weeks. \"Every day. 'Have you found anything else? "
            "Anything older?' He was very -- 'I think I've found something. "
            "I think I know where it is.'\"\n\n"
            "She closes the ledger.\n\n"
            "\"And then he stopped coming. I checked the application. "
            "There's a date. There's no -- 'I'll be back by --' there's no return date. "
            "There never was.\"\n\n"
            "She looks at you steadily.\n\n"
            "\"'The lower passages. That's where it will be. "
            "That's where everything that old ends up.'\"\n\n"
            "She sets the ledger aside."
        )
        g["librarian_stage"] = 1
        g["librarian_met"] = True

    elif stage == 1:
        from content.quests import is_complete
        if is_complete(world, "30"):
            print(
                "She looks at you for a moment when you come in.\n\n"
                "\"'It's not a dead end -- it's\" a beginning.\"\n\n"
                "She picks up her book. "
                "\"He said that once, about a research problem. I think about it.\""
            )
            g["librarian_stage"] = 2
        else:
            print("\"'The lower passages.' That's all I have. That's the last thing.\"")

    else:
        print("She nods at you over her book.")

    return M_HANDLED


def _talk_toll_keeper(world: "World", npc: "GameObject") -> int:
    g = world.globals
    if g.get("toll_paid"):
        print("The toll keeper nods. \"Through you go.\"")
    else:
        print(
            "The toll keeper stands at the gate. "
            "\"Three Zenni. Road maintenance.\" He doesn't elaborate on what road or what maintenance."
        )
        from content.quests import discover
        discover(world, "27")
    return M_HANDLED


def _talk_boggart(world: "World", npc: "GameObject") -> int:
    g = world.globals
    if g.get("boggart_evicted"):
        print("The boggart is gone.")
        return M_HANDLED

    if not g.get("boggart_met"):
        print(
            "The boggart has established squatter's rights with the confidence "
            "of someone who has studied the relevant laws very carefully.\n\n"
            "\"Toll,\" he says. \"Three Zenni, or you don't cross. "
            "Squatter's rights. I've been here longer than you.\"\n\n"
            "He does not look like he is joking."
        )
        g["boggart_met"] = True
    else:
        print(
            "\"Still here,\" the boggart says. Not triumphantly -- just as a statement of fact. "
            "\"Three Zenni. You know the rate.\"\n\n"
            "(A town charter, on the other hand, might make him rethink his position.)"
        )
    return M_HANDLED


def _talk_child(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import discover, is_complete

    if is_complete(world, "41"):
        print("The child waves at you. The kite is flying.")
        return M_HANDLED

    if not g.get("child_met"):
        print(
            "The child points upward without preamble. "
            "In the branches of the oak above: a kite. "
            "They look at you with the absolute, uncomplicated certainty "
            "that you are going to fix this."
        )
        g["child_met"] = True
        discover(world, "41")
    else:
        print("The child points at the kite again. Still stuck. Still certain you'll handle it.")
    return M_HANDLED


def _talk_beekeeper(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import discover, is_complete

    if not g.get("beekeeper_met"):
        print(
            "The beekeeper turns from the hives, expression tight. "
            "\"My smoker's gone. Without it I can't get near them.\" "
            "He gestures at the hives -- active, buzzing, clearly not interested in visitors. "
            "\"Someone took it. Or I put it down somewhere stupid. Either way.\""
        )
        g["beekeeper_met"] = True
        discover(world, "24")
    elif g.get("enchanted_honey_available"):
        print(
            "The beekeeper nods at you from the hives. "
            "\"Honey's on the shelf. Take what you need.\""
        )
    else:
        print(
            "\"Smoker's still missing. No smoker, no honey. "
            "I'm not going in there without it.\""
        )
    return M_HANDLED


def _talk_priest(world: "World", npc: "GameObject") -> int:
    g = world.globals
    if not g.get("priest_met"):
        print(
            "The priest turns from the altar. The robes are worn but clean. "
            "\"The Church of All welcomes all faiths to these walls.\" "
            "He gestures at the dial on the altar. "
            "\"Set it to yours before you pray. "
            "It matters to the ritual -- or so the liturgy says. "
            "I've never tested it the other way.\""
        )
        g["priest_met"] = True
    else:
        print(
            "The priest nods. \"The altar is open. "
            "Turn the dial to your faith before you offer your prayer.\""
        )
    return M_HANDLED


def _talk_mugger(world: "World", npc: "GameObject") -> int:
    print(
        "The mugger is not interested in conversation. "
        "\"Zenni. Now.\" They take a step forward."
    )
    world.globals["hostile_mugger"] = True
    from content.quests import start
    start(world, "51")
    return M_HANDLED


def _talk_knight(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "knight"):
        return M_HANDLED

    g = world.globals
    from content.quests import discover, is_complete

    level = g.get("level", 1)
    stage = g.get("knight_stage", 0)
    name = g.get("player_name", "")

    if stage == 0:
        print(
            "The Knight stands at ease in the square, watching the town go about its business. "
            "When he notices you, he turns fully to face you -- unhurried, attentive. "
            "\"You're looking at me like someone who wants to learn something,\" he says. "
            "\"I teach one thing. Come find me when you're ready to show me what you already know.\""
        )
        g["knight_stage"] = 1
        g["knight_met"] = True
        discover(world, "54")

    elif stage == 1:
        if level < 3:
            print(
                "He looks you over once. \"Not yet,\" he says, not unkindly. "
                "\"Come back when you've got more behind you.\""
            )
        else:
            name_line = f"\"I'm {name}, and I'm ready.\"" if name else "\"I'm ready.\""
            print(
                f"{name_line}\n\n"
                "He looks at you. Something in his posture shifts -- just slightly. "
                "\"Then let's see what you know.\" He draws his weapon."
            )
            g["knight_stage"] = 2
            g["hostile_knight"] = True
            from content.actions import start_combat
            knight_obj = world.objects.get("knight")
            if knight_obj:
                start_combat(world, knight_obj, weapon="melee")

    elif stage == 2:
        if is_complete(world, "54"):
            print(
                f"The Knight nods when he sees you. "
                f"{('\"' + name + '.\"') if name else '\"Good to see you.\"'} He goes back to his practice."
            )
        else:
            print("He draws his weapon without preamble.")
            g["hostile_knight"] = True
            knight_obj = world.objects.get("knight")
            if knight_obj:
                from content.actions import start_combat
                start_combat(world, knight_obj, weapon="melee")

    return M_HANDLED


def _talk_archer(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "archer"):
        return M_HANDLED

    g = world.globals
    from content.quests import discover, is_complete

    stage = g.get("archer_stage", 0)

    if stage == 0:
        print(
            "The archer nocks an arrow without turning to look at you. "
            "\"I'll give you one shot to impress me.\" She releases -- dead center. "
            "\"That's the standard. Match it.\""
        )
        g["archer_stage"] = 1
        g["archer_met"] = True
        discover(world, "55")
    elif stage == 1:
        bow = world.objects.get("bow")
        if not bow or bow.location is not world.player:
            print("\"Get a bow first,\" she says, not looking over.")
        elif not g.get("archery_skill"):
            print("\"Show me what you can do.\"")
            # Archery trial -- rolled against difficulty
            from content.player import check_perception
            if check_perception(world, 12):
                g["archer_stage"] = 2
                complete_archer_trial(world)
            else:
                print("Your shot goes wide. \"Again,\" she says.")
        else:
            print("\"You already have what you need.\"")
    else:
        print("She glances at you, then back at the targets.")

    return M_HANDLED


def complete_archer_trial(world: "World") -> None:
    from content.quests import complete, is_complete
    if not is_complete(world, "55"):
        complete(world, "55")
    print(
        "Your shot lands where hers did.\n\n"
        "She finally turns to look at you. A pause.\n\n"
        "\"Not bad.\" She sets her bow down. "
        "\"You've got the eye. The rest is practice.\""
    )


def _talk_raznak(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "raznak"):
        return M_HANDLED

    g = world.globals
    from content.quests import discover, is_complete

    stage = g.get("raznak_stage", 0)
    cls = g.get("player_class", "")
    name = g.get("player_name", "")

    if not g.get("lynds_invitation") and not g.get("viking_trust_complete"):
        print(
            "Raznak eyes you the way he'd eye an arrow with a bad fletching -- "
            "not hostile, just certain you're not ready.\n\n"
            "\"You want something from me, go talk to the encampment first. "
            "West of here. When they know you, come back.\"\n\n"
            "He turns away. The conversation is over."
        )
        return M_HANDLED

    if stage == 0:
        if cls == "rogue":
            print(
                "Raznak watches you cross the range. He doesn't say anything for a moment. "
                "His eyes go to your hands. Then your stance. Then back to your hands.\n\n"
                "\"You've done this before.\"\n\n"
                "It isn't a question. He disappears into the longhouse and returns with a bow -- "
                "plain, well-maintained, strung and ready.\n\n"
                "\"Don't embarrass it,\" he says, and hands it over."
            )
            bow = world.objects.get("bow")
            if bow:
                world.move_object(bow, world.player)
            g["raznak_stage"] = 3
            if not is_complete(world, "55"):
                from content.quests import complete
                complete(world, "55")
        else:
            print(
                "Raznak looks at you differently now -- not warm exactly, but the suspicion is gone. "
                "\"You want to learn the bow,\" he says. It isn't a question either. "
                "\"Three Zenni. We start now if you have it.\""
            )
            g["raznak_stage"] = 1
        discover(world, "55")

    elif stage == 1:
        if g.get("zenni", 0) >= 3:
            g["zenni"] -= 3
            g["archery_skill"] = True
            g["raznak_stage"] = 2
            print("\"Right. Let's start.\"")
            # Training scene -- 3 turns of practice (simplified: skip to completion)
            g["raznak_stage"] = 3
            bow = world.objects.get("bow")
            if bow:
                world.move_object(bow, world.player)
            print(
                "Raznak watches you complete the final drill. "
                "He is quiet for a moment in the way of someone making a decision they've already made.\n\n"
                "\"You're not a natural,\" he says. \"You worked for it. That's better.\"\n\n"
                "He takes a bow from the rack -- slightly better than the practice ones, "
                "strung tight, balanced.\n\n"
                "\"This one's yours. It'll tell you when you're doing it wrong.\"\n\n"
                "He pauses.\n\n"
                "\"Most bows don't. This one does. Pay attention to it.\""
            )
            if not is_complete(world, "55"):
                from content.quests import complete
                complete(world, "55")
        else:
            print("\"Come back when you do.\"")

    else:
        name_part = f"\"{name},\"" if name else ""
        print(
            f"Raznak looks up when you enter the range. "
            f"{name_part} he says, with a nod. "
            "He goes back to his work. That's the entire greeting, and somehow it's enough."
        )

    return M_HANDLED


def _talk_lynds(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import discover, is_complete, complete

    if not g.get("lynds_met"):
        print(
            "Lynds looks at you the way a person looks at something they're about to do "
            "that they've done many times before. He sets his drink down and puts his elbow on the table.\n\n"
            "\"Go on then.\""
        )
        g["lynds_met"] = True
        g["lynds_stage"] = "challenge"
        discover(world, "59")
        _resolve_lynds_arm_wrestle(world)
        return M_HANDLED

    stage = g.get("lynds_stage", "challenge")
    name = g.get("player_name", "")

    if is_complete(world, "59"):
        name_part = f"\"{name}.\"" if name else ""
        print(
            f"Lynds grins. {name_part} \"You already beat me.\" "
            "He doesn't put his elbow down."
        )
        return M_HANDLED

    cooldown = g.get("lynds_cooldown", 0)
    if cooldown > 0:
        print("\"Give me a bit. I'm still drinking.\"")
        return M_HANDLED

    print("Lynds sets his drink down and puts his elbow on the table. \"Go on then.\"")
    _resolve_lynds_arm_wrestle(world)
    return M_HANDLED


def _resolve_lynds_arm_wrestle(world: "World") -> None:
    from content.player import check_strength
    from content.quests import complete, is_complete

    g = world.globals

    # Win requires strength check difficulty 14
    if check_strength(world, 14):
        # Win
        if not is_complete(world, "59"):
            complete(world, "59")
        g["lynds_invitation"] = True
        g["lynds_stage"] = "won"

        # Heart necklace
        necklace = world.objects.get("heart-necklace")
        if necklace:
            world.move_object(necklace, world.player)

        name = g.get("player_name", "")
        print(
            "Lynds holds still for a moment after his hand goes down. "
            "Then he laughs -- short, surprised, genuine.\n\n"
            "\"Huh.\"\n\n"
            "He studies you for a moment, then reaches into his shirt and pulls out a necklace -- "
            "a simple cord, a clay charm worn smooth. He sets it on the table between you.\n\n"
            "\"My grandmother made that. Said it kept her heart going longer than it had any right to. "
            "I don't know if that's true but I've never had reason to doubt it. You earned it.\"\n\n"
            "He picks up his drink.\n\n"
            "\"Come find us in the bog sometime. Ask for the Dankhaus. Tell them Lynds sent you.\""
        )
        # Apply necklace bonus
        if not g.get("necklace_bonus_applied"):
            g["necklace_bonus_applied"] = True
            g["max_hearts"] = g.get("max_hearts", 5) + 1
            g["hearts"] = g.get("hearts", 5) + 1
    else:
        g["lynds_cooldown"] = 20
        print(
            "Lynds wins without apparent effort. He picks his drink back up. "
            "\"Not bad.\" He means it as a compliment. \"Come back whenever.\""
        )


def _talk_ivanaar(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "ivanaar"):
        return M_HANDLED

    g = world.globals
    from content.quests import discover, is_complete, complete, start

    stage = g.get("ivanaar_stage", 0)

    if stage == 0:
        print(
            "Ivanaar is a broad-shouldered man with a close-cropped beard and patient eyes. "
            "He looks you over without hurry.\n\n"
            "\"Stranger,\" he says. \"We have a word for people who walk into camp without invitation. "
            "We have a different word for people who earn one.\" "
            "He gestures toward the huts behind him. "
            "\"Three trials. Haalvar has the first. South circle for the second. "
            "Fire pit for the third. Complete them all and we'll talk.\""
        )
        g["ivanaar_stage"] = 1
        g["ivanaar_met"] = True
        discover(world, "57")
        start(world, "57")

    elif stage == 1:
        trials_done = g.get("trials_complete", 0)
        if trials_done < 3:
            print(
                f"Ivanaar glances at you. \"You've completed {trials_done} of three. "
                "Finish the rest.\""
            )
        else:
            # All trials complete
            g["ivanaar_stage"] = 2
            g["viking_trust_complete"] = True
            complete(world, "57")

            # Award runed metal
            metal = world.objects.get("runed-metal")
            if metal:
                world.move_object(metal, world.player)

            print(
                "Ivanaar watches you approach. Something in his expression has shifted.\n\n"
                "\"You've done it. All three.\" He says it quietly -- not a celebration, "
                "more like a conclusion that was inevitable.\n\n"
                "\"You've earned the word.\" He reaches into a chest behind him and "
                "produces a piece of worked metal -- runes along the edge, heavy with intent.\n\n"
                "\"Take this to the forge south of the wasteland. "
                "The smith there knows what to do with it.\""
            )

    else:
        print(
            "Ivanaar nods at you. \"You know where everything is now,\" he says. "
            "\"Use it.\""
        )

    return M_HANDLED


def _talk_haalvar(world: "World", npc: "GameObject") -> int:
    from content.traps import check_ink_npc_block
    if check_ink_npc_block(world, "haalvar"):
        return M_HANDLED

    g = world.globals
    if g.get("trial_1_complete"):
        print("Haalvar looks satisfied in the way of someone whose riddle was answered correctly. \"You passed.\"")
        return M_HANDLED

    print(
        "Haalvar leans back in his chair with the self-satisfaction of a man "
        "who has stumped a lot of people.\n\n"
        "\"The Riddle Stone. Simple rule: I ask, you answer. "
        "Get it right, first trial's done. "
        "Get it wrong, you come back tomorrow.\"\n\n"
        "He clears his throat with unnecessary ceremony.\n\n"
        "\"What has roots as nobody sees, is taller than trees, up, up, up it goes, "
        "and yet never grows?\"\n\n"
        "(Type ANSWER MOUNTAIN or ANSWER [your answer].)"
    )
    g["haalvar_riddle_active"] = True
    return M_HANDLED


def answer_haalvar_riddle(world: "World", answer: str) -> None:
    from content.quests import start
    g = world.globals

    if not g.get("haalvar_riddle_active"):
        print("Haalvar isn't waiting for an answer right now.")
        return

    correct_answers = {"mountain", "a mountain", "the mountain", "mountains"}
    # Also accept if wearing enchanted glasses (Kevry whispered it)
    glasses_hint = g.get("kevry_enchanted") and g.get("actually_enchanted_glasses_worn")

    if answer.strip().lower() in correct_answers or glasses_hint:
        g["haalvar_riddle_active"] = False
        g["trial_1_complete"] = True
        g["trials_complete"] = g.get("trials_complete", 0) + 1
        print(
            "Haalvar blinks. Then he laughs -- sharp, surprised.\n\n"
            "\"Mountain. Yes.\" He waves a hand. "
            "\"Go on. You're done here.\""
        )
    else:
        print(
            "Haalvar shakes his head slowly. "
            "\"No.\" He doesn't seem disappointed -- if anything, pleased. "
            "\"Come back tomorrow.\""
        )
        g["haalvar_riddle_active"] = False
        g["haalvar_cooldown"] = 5


def _talk_aylora(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import start

    if g.get("trial_3_complete"):
        print("Aylora is still asleep. She looks peaceful.")
        return M_HANDLED

    if not g.get("aylora_met"):
        print(
            "Aylora has the cheerful certainty of someone who has never lost a drinking contest "
            "and doesn't intend to start.\n\n"
            "\"Thornbrew,\" she says. \"You drink until someone stops. "
            "Usually it's not me.\" She slides a horn across the table. "
            "\"Ready?\""
        )
        g["aylora_met"] = True
        g["aylora_ready"] = True
    else:
        print("\"Ready when you are,\" Aylora says, refilling her horn.")
        g["aylora_ready"] = True

    start(world, "57")
    return M_HANDLED


def complete_aylora_trial(world: "World") -> None:
    g = world.globals
    if g.get("trial_3_complete"):
        return

    from content.player import check_strength
    if check_strength(world, 11):
        g["trial_3_complete"] = True
        g["trials_complete"] = g.get("trials_complete", 0) + 1

        # Move Aylora to passed-out state
        aylora = world.objects.get("aylora")
        if aylora:
            aylora.desc = "Aylora (passed out)"

        print(
            "She is surprised. It shows.\n\n"
            "The horn goes down. Aylora's expression passes through several emotions very quickly -- "
            "disbelief, respect, and then a cheerful acceptance that arrives with a thump "
            "as she folds forward and goes to sleep on the table.\n\n"
            "Ivanaar, who has apparently been watching from a distance, approaches.\n\n"
            "\"Hm,\" he says."
        )
    else:
        print(
            "Somewhere around the third horn you stop being able to feel your feet. "
            "Aylora watches you with professional interest as you make your exit.\n\n"
            "She looks fine."
        )


def _talk_pyronicus(world: "World", npc: "GameObject") -> int:
    g = world.globals

    if not g.get("pyronicus_met"):
        print(
            "Pyronicus sets down his work and regards you with calm, unhurried eyes. "
            "\"Will's errand,\" he says. \"Yes.\"\n\n"
            "He moves to a workbench and returns with the ring, "
            "placing it in your hand with the care of someone returning something that was never theirs.\n\n"
            "\"It fell through my ceiling,\" he says. "
            "\"Rings don't do that by accident.\"\n\n"
            "He pauses. \"Will told you what you need to know, I assume.\"\n\n"
            "He goes back to what he was doing. The conversation, apparently, is over."
        )
        g["pyronicus_met"] = True
        # Give ring to player
        ring = world.objects.get("ring")
        if ring:
            world.move_object(ring, world.player)

    elif g.get("runed_metal_delivered"):
        print(
            "Pyronicus is at the forge. He does not look up. "
            "\"It will be ready when it's ready.\""
        )
    else:
        print(
            "Pyronicus regards you with the same calm. "
            "\"Was there something else?\""
        )

    return M_HANDLED


def _talk_kevry(world: "World", npc: "GameObject") -> int:
    g = world.globals

    if not g.get("kevry_met"):
        glasses = world.objects.get("enchanted-glasses")
        if glasses and glasses.has_flag("WEARING"):
            # Trigger enchantment
            _kevry_receive_glasses(world, glasses)
        else:
            print(
                "Kevry looks up from something indistinct on a table that may or may not "
                "be a navigation instrument.\n\n"
                "\"Long way to come,\" he says. \"Must have been a reason.\"\n\n"
                "He waits."
            )
        g["kevry_met"] = True
    else:
        if g.get("kevry_enchanted"):
            print("\"All done,\" Kevry says. \"They'll do what you need.\"")
        else:
            print(
                "\"You've got something with you,\" Kevry says. "
                "\"Didn't bring the glasses?\""
            )

    return M_HANDLED


def _talk_rowan(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import discover, is_complete

    if not g.get("rowan_met"):
        print(
            "He looks up from his papers with the expression of someone who has been "
            "interrupted before and expects to be interrupted again. "
            "\"Can I help you?\" It is not entirely a question."
        )
        g["rowan_met"] = True

    elif not is_complete(world, "32"):
        print(
            "\"My grandfather built this town as much as anyone. "
            "He explored the passages beneath it too -- donated whatever he found to the Trophy Case upstairs. "
            "It's been empty for years. I don't know what that says about the state of adventure in Roundabout.\"\n\n"
            "He pauses. "
            "\"He had a gravestone in the cemetery. Someone took it recently. I haven't had time to pursue it.\""
        )
        discover(world, "32")
    else:
        print(
            "Rowan looks up and nods at you. "
            "\"Thank you again,\" he says. \"For the gravestone.\""
        )

    return M_HANDLED


def _talk_records_worker(world: "World", npc: "GameObject") -> int:
    g = world.globals
    from content.quests import is_complete

    if not g.get("records_worker_met"):
        print(
            "The records worker looks up from a cabinet drawer. "
            "\"The town charter? Yes, I have it. "
            "But I'm not handing it over to someone I don't know for reasons I don't know.\"\n\n"
            "He pauses. \"That pocket watch on the desk belonged to my uncle. "
            "Been missing for years. "
            "If you somehow found it -- then I'd know you'd been to places I'd trust you to be.\""
        )
        g["records_worker_met"] = True
    elif is_complete(world, "17"):
        print(
            "The records worker nods when he sees you. "
            "\"Charter's yours if you need it again.\""
        )
    else:
        print(
            "\"That watch,\" he says. "
            "\"If you find it -- I'd know who I was dealing with.\""
        )

    return M_HANDLED


def _talk_soldier(world: "World", npc: "GameObject") -> int:
    g = world.globals
    if not g.get("soldier_line_given"):
        print(
            "\"There's a room down there that talked to me once. I never figured out what it said.\""
        )
        g["soldier_line_given"] = True
    else:
        print("The soldier nods at you and goes back to whatever he's doing.")
    return M_HANDLED


def _talk_viking(world: "World", npc: "GameObject") -> int:
    g = world.globals
    stage = g.get("viking_trust_stage", 0)

    if stage == 0:
        print(
            "The viking looks you up and down. "
            "\"We test strangers here before we trust them. "
            "Three trials. You choose the order.\" "
            "He sits back down. \"When you're ready.\""
        )
        g["viking_trust_stage"] = 1
        from content.quests import discover
        discover(world, "57")
    else:
        print("\"The trials stand. When you're ready.\"")
    return M_HANDLED


def _talk_unnamed_child(world: "World", npc: "GameObject") -> int:
    """Trial 2 administrator -- does not speak."""
    g = world.globals

    if g.get("trial_2_complete"):
        print("The child points back toward the encampment. The trial is done.")
        return M_HANDLED

    if not g.get("ritual_circle_sequence_started"):
        print(
            "The child stands at the edge of the ritual circle and points at the standing stones. "
            "They look at you, then at the stones, then back at you. "
            "They don't speak.\n\n"
            "The stones are numbered -- or rather, they each bear a different rune. "
            "You need to touch them in the right order."
        )
        g["ritual_circle_sequence_started"] = True
    else:
        correct_order = g.get("ritual_stone_order")
        attempts = g.get("ritual_attempts", 0)

        if attempts == 0:
            print(
                "The child watches you study the stones. "
                "They don't help. They just watch."
            )
        else:
            print("The child watches.")

    return M_HANDLED


def complete_ritual_trial(world: "World", sequence: list) -> None:
    """Called when player touches stones in sequence."""
    g = world.globals
    correct = [1, 3, 2]  # stone order by index (sourced from locations.md ritual circle)

    g["ritual_attempts"] = g.get("ritual_attempts", 0) + 1

    if sequence == correct:
        g["trial_2_complete"] = True
        g["trials_complete"] = g.get("trials_complete", 0) + 1
        print(
            "The stones pulse once, in sequence -- a warmth that has nothing to do with the air. "
            "The child nods once, satisfied, and points back toward the encampment."
        )
    else:
        # Child looks disappointed
        print(
            "The child looks at the stones, then at you, then back at the stones. "
            "Their expression is politely disappointed. "
            "They point at the first stone again."
        )
