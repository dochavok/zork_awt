"""
The mid-tier trap side below the Flooding Room: Dream Corridor, Lost
Apprentice's Cell (Quest 50), Supply Cache, Flood Sump. (The Spillway is in
content/flooding.py.)

Design: locations.md (Trap Side), mechanics.md (The Dream Corridor; enemy
stats), quests.md (Quest 50), items.md (Apprentice's Gloves, Gold Nugget),
npcs.md (The Afflicted Apprentice).

- Dream Corridor: numbered menus (Level 1 → 2A/2B → outcome). A failure wakes
  the player at the entrance and the opening scene repeats; a success puts
  them in the Cell. Afterwards it's an ordinary passage.
- Cell: the afflicted apprentice — one round per KILL APPRENTICE (2d8, 3
  hearts, the Warden's rules; leaving resets him). Fireball works. Defeat
  breaks the affliction (12 XP, not a kill); he finishes his tunnel himself,
  hands over his gloves and climbs out, and Quest 50 completes (2026-10-14:
  no shovel needed). UP is then one-way to Bog-NW. An invisible player he
  doesn't see.
- Supply Cache: SEARCH RUBBLE uncovers the gold nugget.

State: DREAM-STEP (None | "1" | "2A" | "2B" | "A1".."B3"), DREAM-PASSED,
       APPRENTICE-HEARTS, APPRENTICE-FREED, APPRENTICE-SEEN, APPRENTICE-UNSEEN,
       TUNNEL-DUG, NUGGET-FOUND
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_ENTER, M_LOOK
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

APPRENTICE_HEARTS = 3
APPRENTICE_DICE = (2, 8)

# --- Dream Corridor (mechanics.md — The Dream Corridor) -----------------------

_WAKE = "You wake up at the entrance. The footprints are there. Your size. Your stride."

_INCITING = (
    "The corridor is low and wet. Water drips somewhere behind you. Your light throws "
    "just enough to see the floor — and the footprints already pressed into the mud. "
    "Leading in from the entrance. Your size. Your stride. You haven't been here before."
)
_LEVEL_2 = {
    "2A": (
        "The prints lead forward. You know this feeling — the particular shape of a place "
        "you've already moved through. You have been here. You just don't remember when."
    ),
    "2B": (
        "You step off the prints. The corridor looks different from here — longer, maybe, "
        "or the walls are closer. Nothing you can point to. Just the feeling that the "
        "version of this place you're now standing in is not the one you entered."
    ),
}
# Each sense: its Level 2 line, then the Level 3 set-up.
_SENSE = {
    "A1": (
        "The footprints change. Halfway down the corridor they shift — your stride "
        "lengthens, the toe digs deeper. Whatever you were walking toward, you were walking "
        "faster by the time you reached it. You follow the change.",
        "The footprints end at a wall. Not a door — a wall. But the mud at the base is "
        "disturbed, smeared, like something passed through it. The light flickers.",
    ),
    "A2": (
        "A sound comes from your left — a passage you didn't notice before, or didn't exist "
        "before. Water moving. Not dripping. Flowing. Like something is draining toward an "
        "opening.",
        "You turn left. The passage is narrow — barely a shoulder's width. The sound of "
        "moving water is clearer now, ahead and below. The passage slopes down. The light "
        "gutters in a draft coming up from somewhere beneath you.",
    ),
    "A3": (
        "It stops you mid-step. Something warm. Cooked. Completely wrong for a place like "
        "this — bread, maybe, or stew. Coming from ahead, faint but real, the kind of smell "
        "that makes your body move before your mind does.",
        "The smell gets stronger as you move. At the end of the corridor a low alcove opens "
        "to the right — just wide enough to crouch into. Inside: nothing. No food, no fire, "
        "no source. The smell is overwhelming in here. Your stomach responds before your "
        "brain does.",
    ),
    "B1": (
        "Something pulls at you — not physical, not quite. A certainty about one direction "
        "that has no evidence behind it. The kind of knowing that lives below thought. You "
        "trust it, or you don't.",
        "The certainty leads you to a section of wall that looks identical to every other "
        "section of wall. No seam, no mark, no reason. The feeling is loudest here. Your "
        "light doesn't flicker. The wall doesn't breathe. It just is — and something in you "
        "insists this is the place.",
    ),
    "B2": (
        "Your light catches the wall of a side tunnel you hadn't noticed — or that wasn't "
        "there before. Claw marks run along the stone at shoulder height. Deep, parallel, "
        "dragged fast. Whatever made them was large. Whatever made them went that way. You "
        "follow anyway.",
        "The claw marks run the length of the tunnel, shoulder height, deep and continuous. "
        "You follow them.\n"
        "The tunnel is long enough that the entrance is behind you and the far end is still "
        "ahead. The marks don't stop or change. They just keep going.\n"
        "Then the tunnel goes silent in a way it wasn't silent before. One breath of "
        "stillness.\n"
        "Then something at the far end shifts. Not loud. Not close. Just present. Aware, "
        "maybe. The marks continue toward it.",
    ),
    "B3": (
        "The ground hums. Low, slow, rhythmic. Like something heavy moving far below, or far "
        "ahead — it's impossible to tell. Your boots feel it more than you do. You follow "
        "the vibration.",
        "The vibration leads you to a section of floor where it is strongest — a rough "
        "circle of stone, slightly discolored, slightly lower than the surrounding floor. The "
        "hum comes up through your boots and into your legs. It is steady. It is patient. It "
        "has been doing this for a long time.",
    ),
}
# Outcomes: (option 1, option 2) — (succeeds, text)
_OUTCOME = {
    "A1": (
        (False, "Cold stone. Solid. You press harder, run your fingers along the seam where "
                "the smear meets the surface. Nothing gives. It is definitively, completely a "
                "wall. You press your forehead against it. " + _WAKE),
        (False, "Distance doesn't help. It's a wall. Flat, unbroken, mortared tight. Whatever "
                "the smear in the mud means, it doesn't mean a door. You stand there long "
                "enough to be certain. " + _WAKE),
    ),
    "A2": (
        (True, "The slope levels. The passage opens. The sound of water is all around you "
               "now — a drain somewhere below the floor, pulling the flood somewhere useful. "
               "The air is damp but moving. Ahead, a doorway. You walk through it. You are "
               "through."),
        (False, "The draft gets stronger. The passage narrows further and then opens without "
                "warning — onto nothing. A drop. You can't see the bottom. The light goes "
                "with you. " + _WAKE + " Your heart is going very fast and you're not "
                "entirely sure why."),
    ),
    "A3": (
        (False, "The alcove goes back further than it looked. You crouch deeper, light "
                "first. The smell is everywhere and the source is nowhere. The ceiling gets "
                "lower. You keep looking. The light goes out. " + _WAKE + " You are not "
                "hungry anymore."),
        (True, "You keep walking. The smell fades behind you the way smells do when you stop "
               "chasing them. The corridor ends at a doorway. You don't remember the corridor "
               "having a doorway. You walk through it. You are through."),
    ),
    "B1": (
        (True, "You don't slow down. You don't brace. You walk into it the way you'd walk "
               "through a doorway you've used a thousand times. The wall is not there. The "
               "room beyond is. You are through it before you've decided what just happened. "
               "You are through."),
        (False, "You wait. The certainty doesn't grow or fade — it just sits there, patient, "
                "offering nothing new. The corridor is very quiet. You wait longer. The light "
                "holds. Nothing happens. The feeling eventually becomes indistinguishable "
                "from doubt. " + _WAKE + " The certainty is gone."),
    ),
    "B2": (
        (True, "You don't slow down. Whatever is ahead has already heard you — stopping "
               "won't help and going back won't either. You walk toward the sound. The tunnel "
               "ends at a doorway. Nothing is there. Nothing was ever there, or it's somewhere "
               "you're not anymore. You walk through it. You are through."),
        (False, "You take one step back. Then another. The sound doesn't repeat but the "
                "silence that follows it is worse. You turn and move fast, faster, back "
                "toward the entrance, back toward the footprints, back toward something that "
                "made sense. " + _WAKE + " The far end of the tunnel is very far away now."),
    ),
    "B3": (
        (True, "The hum rises through you the moment your full weight is on it — up through "
               "your legs, your chest, your jaw. The floor doesn't move. You do. The corridor "
               "shifts around you, or you shift through it, and then you are somewhere else. "
               "The hum is gone. The room ahead is quiet and real. You are through."),
        (True, "The vibration is different through your palm than through your boots — more "
               "specific, like a word you almost recognize.\n"
               "You press harder. The circle of stone depresses slightly, just enough to feel "
               "deliberate, and something in the corridor unlocks without a sound.\n"
               "A doorway is there that wasn't before. You stand up and walk through it. You "
               "are through."),
    ),
}
_MENUS = {
    "1":  ("Follow them", "Go another way"),
    "2A": ("Look closer at the prints", "Listen", "Breathe in"),
    "2B": ("Trust the feeling", "Look around", "Feel the ground"),
    "A1": ("Press your hand against the wall", "Step back and look at the full wall"),
    "A2": ("Follow the slope down toward the sound", "Follow the draft, toward air"),
    "A3": ("Crouch inside and look for the source", "Ignore it and keep moving"),
    "B1": ("Press forward into the wall", "Wait and see"),
    "B2": ("Keep walking", "Fall back"),
    "B3": ("Step onto the discolored stone", "Kneel and press your hand to it"),
}
_CORRIDOR_PLAIN = ("A low, wet corridor running north and south. There are footprints in "
                   "the mud, and they are only yours.")

# --- Lost Apprentice's Cell ---------------------------------------------------

_CELL = (
    "A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped "
    "in one corner. Low in the weakest stretch of wall, where the rock gives way to packed "
    "earth, someone has clawed out a tunnel, angling steeply up into the dark — and "
    "stopping a little short of anything. Passages lead north and south."
)
_CELL_DUG = (
    "A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped "
    "in one corner. Low in the weakest stretch of wall, where the rock gives way to packed "
    "earth, the tunnel angles steeply up to a ragged patch of grey light. Passages lead "
    "north and south."
)
_STOPPED = (
    "A young man crouches at the mouth of the tunnel, his hands raw, fingers still hooked "
    "as if he stopped mid-scrape and forgot how to start again."
)
APPRENTICE_ATTACKS = (
    _STOPPED + " He turns as you come in. His eyes are wrong — too wide, too fixed — and "
    "he comes at you without a word."
)
APPRENTICE_UNSEEING = _STOPPED + " He doesn't look round."
APPRENTICE_AFFLICTED = ("The apprentice crouches between you and the tunnel, breathing "
                        "hard, watching you with eyes that don't blink enough.")
APPRENTICE_UNAWARE = ("The apprentice crouches at the mouth of the tunnel, staring up into "
                      "the dark. He hasn't noticed you.")
_ROUND_WON = "You get a blow in. He staggers, shakes his head, and comes again."
_ROUND_LOST = "He's faster than he looks. His fists find you. You take a hit."
_ROUND_TIE = "You trade blows. Both of you feel it."
_FREED = (
    "He goes down on one knee and stays there. When he looks up, his eyes are his own again "
    "— red-rimmed, frightened, very young. \"I was digging,\" he says. \"I was digging for "
    "so long.\" He looks at his hands as if they belong to someone else."
)
_DIGS_THROUGH = (
    "He gets to his feet slowly and looks at the tunnel for a long moment. Then he climbs "
    "back into it. You hear him digging — not frantic now, just steady — then a soft slump "
    "of earth, and grey light spills down the shaft along with the smell of the bog."
)
_FAREWELL = (
    "He slides back down, filthy and almost smiling. He peels off his gloves and holds them "
    "out. \"They were for digging,\" he says. \"I won't be doing that again.\" He starts up "
    "the tunnel, stops, and looks back. \"Tell Will—\" He shakes his head. \"No. I'll tell "
    "him myself.\" Then he's gone."
)
_GLOVES_ADDED = "[Apprentice's Gloves added to inventory.]"
_DIG_BLOCKED = "He's not going to let you near it."
_DUG = "The tunnel's through. There's nothing left to dig."
_NOT_THROUGH = "The tunnel isn't through. You can see where it ends, a little short of anything."
_SURFACE = (
    "You climb the tunnel hand over hand and haul yourself out into the reeds. A line of "
    "muddy footprints leads away toward town."
)

# --- Supply Cache / Flood Sump ------------------------------------------------

_CACHE = (
    "A side room half-buried by a collapse. Broken crates and a toppled shelf poke out of "
    "the rubble that fills the far end. Whatever was stored here was stored a long time ago. "
    "Passages lead north and south."
)
_NUGGET_FOUND = ("You shift the loose stone at the edge of the rubble. Something underneath "
                 "catches the light — a nugget of gold the size of a thumb joint.")
_NOTHING_ELSE = "There's nothing else under there."
_SUMP = (
    "The passage ends here in a low chamber, the floor wet — a shallow pool covers most of "
    "it, fed by seepage through the walls. The water is still and dark. The ceiling is "
    "close. This is the lowest point down here, and it feels like it. The only way out is "
    "back north."
)


# =============================================================================
# Dream Corridor
# =============================================================================

def _menu(step: str) -> None:
    print("\n".join(f"  {i}. {label}" for i, label in enumerate(_MENUS[step], 1)))


def _begin(w: World) -> None:
    print(_INCITING)
    w.set_global("DREAM-STEP", "1")
    _menu("1")


def dream_input_hook(w: World, text: str) -> bool:
    """Numbered choices while the Dream Corridor is unpassed."""
    step = w.get_global("DREAM-STEP")
    if not step or w.here is None or w.here.name != "DREAM-CORRIDOR":
        return False
    choice = text.strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(_MENUS[step]):
        return False
    n = int(choice)
    if step == "1":
        nxt = "2A" if n == 1 else "2B"
        print(_LEVEL_2[nxt])
        w.set_global("DREAM-STEP", nxt)
        _menu(nxt)
    elif step in ("2A", "2B"):
        sense = f"{step[1]}{n}"
        level2, setup = _SENSE[sense]
        print(level2)
        print(setup)
        w.set_global("DREAM-STEP", sense)
        _menu(sense)
    else:
        passed, text_out = _OUTCOME[step][n - 1]
        print(text_out)
        if passed:
            w.set_global("DREAM-STEP", None)
            w.set_global("DREAM-PASSED", True)
            w.game.enter_room(w.rooms["LOST-APPRENTICES-CELL"])
        else:
            _begin(w)
    return True


class _DreamSouth(Exit):
    """South through the corridor: only once it's been passed."""
    def resolve(self, world):
        if not world.get_global("DREAM-PASSED"):
            _begin(world)
            return None, None
        return super().resolve(world)


def dream_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER and not w.get_global("DREAM-PASSED"):
        w.here.visited = False        # the full scene and menu on every entry until passed
        return M_NOT_HANDLED
    if msg == M_LOOK:
        if w.get_global("DREAM-PASSED"):
            print(_CORRIDOR_PLAIN)
        else:
            _begin(w)
        return M_HANDLED
    return M_NOT_HANDLED


class _DreamNorth(Exit):
    """Back to the Spillway: the corridor forgets where you were."""
    def resolve(self, world):
        world.set_global("DREAM-STEP", None)
        return super().resolve(world)


# =============================================================================
# Lost Apprentice's Cell
# =============================================================================

def _apprentice(w: World):
    return w.objects["APPRENTICE"]


def _afflicted(w: World) -> bool:
    return _apprentice(w).location is w.rooms["LOST-APPRENTICES-CELL"] \
        and not w.get_global("APPRENTICE-FREED")


def fight_round(w: World) -> None:
    """KILL APPRENTICE — one round (content/combat.py)."""
    from content import combat
    hearts = int(w.globals.get("APPRENTICE-HEARTS", APPRENTICE_HEARTS))
    hearts -= combat.fight_round(w, APPRENTICE_DICE, _ROUND_WON, _ROUND_LOST, _ROUND_TIE)
    w.globals["APPRENTICE-HEARTS"] = hearts
    if hearts <= 0 and not w.get_global("GAME-OVER"):
        _freed(w)


def fireball_hit(w: World) -> None:
    """CAST FIREBALL at the apprentice: 1 heart, no roll, no strike back."""
    hearts = int(w.globals.get("APPRENTICE-HEARTS", APPRENTICE_HEARTS)) - 1
    w.globals["APPRENTICE-HEARTS"] = hearts
    if hearts <= 0 and not w.get_global("GAME-OVER"):
        _freed(w)


def _freed(w: World) -> None:
    from content.combat import award_combat_xp
    print(_FREED)
    w.set_global("APPRENTICE-FREED", True)
    award_combat_xp(w, "apprentice", kill=False)   # the affliction breaks; he lives
    _digs_himself_out(w)


def _digs_himself_out(w: World) -> None:
    """Freed, he finishes the tunnel, hands over his gloves and climbs out
    (redesigned 2026-10-14: no shovel needed). Quest 50 completes here."""
    from content import quests
    from content.char_create import _pause
    print(_DIGS_THROUGH)
    _pause()
    print(_FAREWELL)
    print(_GLOVES_ADDED)
    w.move_object(_apprentice(w), None)
    w.move_object(w.objects["APPRENTICE-GLOVES"], w.player)
    w.set_global("TUNNEL-DUG", True)
    w.ways_changed("LOST-APPRENTICES-CELL")
    w.set_global("QUEST50-DONE", True)
    quests.complete(w, "50")              # 12 XP, 5 Zenni, silent; the notice comes down


def _dig(w: World) -> None:
    print(_DIG_BLOCKED if _afflicted(w) else _DUG)


class _TunnelUp(Exit):
    """UP the apprentice's tunnel to Bog-NW — one-way, once he's dug through."""
    def resolve(self, world):
        if not world.get_global("TUNNEL-DUG"):
            return None, _NOT_THROUGH
        room, _ = super().resolve(world)
        return room, _SURFACE


def _set_presence(w: World) -> None:
    """His first-sight line, then his presence — seen or not (the ring, not
    inked: the Chuckle House rule). Visible for the first time, he attacks."""
    from content.chuckle import _visible
    app = _apprentice(w)
    if _visible(w):
        app.ldesc = APPRENTICE_AFFLICTED if w.get_global("APPRENTICE-SEEN") else APPRENTICE_ATTACKS
        w.set_global("APPRENTICE-SEEN", True)
    else:
        app.ldesc = APPRENTICE_UNAWARE if w.get_global("APPRENTICE-UNSEEN") else APPRENTICE_UNSEEING
        w.set_global("APPRENTICE-UNSEEN", True)


def cell_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_CELL_DUG if w.get_global("TUNNEL-DUG") else _CELL)
        if _afflicted(w):
            _set_presence(w)
        return M_HANDLED
    if msg == M_ENTER:
        if _afflicted(w):
            # Coming back: he's at full strength again (the Warden's rule)
            w.set_global("APPRENTICE-HEARTS", APPRENTICE_HEARTS)
        return M_NOT_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    if w.get_global("APPRENTICE-FREED") and _apprentice(w).location is w.here:
        _digs_himself_out(w)                  # a save from before he dug himself out
    shovel = w.objects["SHOVEL"]
    tunnel = w.objects["APPRENTICE-TUNNEL"]
    if (w.prsa == "V-USE" and w.prso is shovel) or \
            (w.prsa == "V-DIG" and w.prso in (None, shovel, tunnel)):
        _dig(w)
        return M_HANDLED
    return M_NOT_HANDLED


# =============================================================================
# Supply Cache / Flood Sump
# =============================================================================

def cache_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_CACHE)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    rubble = w.objects["CACHE-RUBBLE"]
    if (w.prsa in ("V-SEARCH", "V-MOVE", "V-DIG") and w.prso in (rubble, None)) or \
            (w.prsa == "V-DIG" and w.prso is w.objects["SHOVEL"]):
        if w.get_global("NUGGET-FOUND"):
            print(_NOTHING_ELSE)
        else:
            w.set_global("NUGGET-FOUND", True)
            w.objects["GOLD-NUGGET"].clear_flag("INVISIBLE")
            print(_NUGGET_FOUND)
        return M_HANDLED
    return M_NOT_HANDLED


def sump_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_SUMP)
        return M_HANDLED
    return M_NOT_HANDLED


def make_rooms(world) -> None:
    def room(name, desc, action):
        r = Room(name=name, desc=desc, ldesc="", value=2)
        r.set_flag(RLANDBIT)   # dark
        r.action = action
        world.register_room(r)
        return r

    dream = room("DREAM-CORRIDOR", "Dream Corridor", dream_action)
    cell = room("LOST-APPRENTICES-CELL", "Lost Apprentice's Cell", cell_action)
    cache = room("SUPPLY-CACHE", "Supply Cache", cache_action)
    sump = room("FLOOD-SUMP", "Flood Sump", sump_action)
    world.rooms["SPILLWAY"].exits["south"] = Exit(destination="DREAM-CORRIDOR")
    dream.exits.update(north=_DreamNorth(destination="SPILLWAY"),
                       south=_DreamSouth(destination="LOST-APPRENTICES-CELL"))
    cell.exits.update(north=Exit(destination="DREAM-CORRIDOR"),
                      south=Exit(destination="SUPPLY-CACHE"),
                      up=_TunnelUp(destination="BOG-NW"))
    cache.exits.update(north=Exit(destination="LOST-APPRENTICES-CELL"),
                       south=Exit(destination="FLOOD-SUMP"))
    sump.exits["north"] = Exit(destination="SUPPLY-CACHE")
