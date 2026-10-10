"""
World initialization for Roundabout: The God-Forsaken Ring.
Call initialize_world(world, game) once at startup before game.run().
"""

from __future__ import annotations
from engine.world import GameObject
from content.rooms import make_rooms
from content.objects import make_objects
from content.verbs import register_verbs


def initialize_world(world, game, seed=None) -> None:
    """
    seed: fixes this playthrough's random setup (Zenni rooms). None = random.
    Tests pass a fixed seed so the setup is randomized once and stays put.
    """
    make_rooms(world)
    make_objects(world)
    _make_player(world)
    _init_player_state(world)
    _place_objects(world)
    _wire_whitehouse_action(world, game)
    # Ty's Cargo table: PLAY CARGO / BET n; REROLL / STAND while choosing.
    # First (before register_verbs' hooks), so an open reroll-or-stand choice
    # is seen before any other hook.
    from content import cargo
    game.register_input_hook(cargo.input_hook)
    register_verbs(game)

    import random
    from content import zenni_rooms
    zenni_rooms.assign(world, random.Random(seed))
    game.register_enter_hook(zenni_rooms.on_enter)

    # Lighting: dark rooms block entry without a light; torch timer
    from content import light
    game.register_walk_check(light.dark_block)
    game.register_enter_hook(light.on_enter)

    # Quest 32: a loaded hand cart can't take stairs; first-push line
    from content import gravestone
    game.register_walk_check(gravestone.stairs_block)
    game.register_enter_hook(gravestone.on_enter)

    # Trap 8: the snare fires after the Inscription Chamber description
    from content import inscription
    game.register_enter_hook(inscription.on_enter)

    # Quest 34: the Lower Crossing pull-back line after leaving the Tool Alcove
    from content import tool_alcove
    game.register_enter_hook(tool_alcove.on_enter)
    game.register_input_hook(gravestone.set_stone_input_hook)

    # Quest 49: ASSEMBLE BOWL (every bowl piece answers to "bowl")
    from content import shrine_bowl
    game.register_input_hook(shrine_bowl.assemble_input_hook)

    # Pie Rat Ship: treasure map check aboard, ship away from harbor
    from content import ship
    game.register_enter_hook(ship.on_enter)
    from content.verbs import make_land_input_hook
    game.register_input_hook(make_land_input_hook)   # MAKE LAND = LAND
    from content.verbs import buy_input_hook
    game.register_input_hook(buy_input_hook)         # BUY X from Shamus's stock
    from content.tavern import bar_input_hook
    game.register_input_hook(bar_input_hook)         # BUY DRINK / FOOD / STEW, RENT ROOM
    from content import journal
    game.register_input_hook(journal.journal_input_hook)   # READ JOURNAL without one
    world.objects["TIP-JOURNAL"].action = journal.journal_action
    from content.trap_side import dream_input_hook
    game.register_input_hook(dream_input_hook)       # Dream Corridor menus
    from content.vikings import give_zenni_input_hook
    game.register_input_hook(give_zenni_input_hook)  # GIVE RAZNAK THREE ZENNI
    from content import knight
    game.register_input_hook(knight.give_zenni_input_hook)  # GIVE KNIGHT THREE ZENNI
    game.register_input_hook(knight.shoot_input_hook)  # SHOOT KNIGHT: no turn
    game.register_enter_hook(knight.on_enter)        # leaving abandons the trial

    # Pie Rat heist: weak point check; the blown entrance stays sealed
    from content import mine
    game.register_enter_hook(mine.on_enter)
    from content import combat
    game.register_enter_hook(combat.on_enter)        # a fresh fight's opening round (bow +5)
    game.register_walk_check(mine.sealed_check)
    from content import ship
    game.register_walk_check(ship.gangplank_check)   # EAST from the Docks = BOARD SHIP
    from content import mine_branch
    game.register_enter_hook(mine_branch.on_enter)   # the Assay Room gap

    # Roundabout Pond: bottle sighting check on each visit
    from content import pond
    game.register_enter_hook(pond.on_enter)

    # Will's Bedroom: dragon-nip check (Quest 58)
    from content import bedroom
    game.register_enter_hook(bedroom.on_enter)

    # The Quest Board: game-start notices; Shamus's on the first Kitchen visit
    from content import quest_board
    quest_board.setup(world)
    game.register_enter_hook(quest_board.on_enter)

    # RESTORE <name>: another character's save (engine/savegame.py)
    from content.verbs import restore_named_input_hook
    game.register_input_hook(restore_named_input_hook)

    # REST — Level 6: 1 heart, 50-turn reuse, not in a fight
    from content import rest
    game.register_input_hook(rest.rest_input_hook)

    # Clock events created mid-game: RESTORE rebuilds them in a fresh game
    # (engine/savegame.py). Every event added after setup needs one here.
    from content import corruption, light, mine, ship
    game.register_clock_factory("ring-corruption-clock", corruption.ensure_clock)
    game.register_clock_factory("torch-clock", light.ensure_torch_clock)
    game.register_clock_factory("dark-cast-window", light.ensure_cast_window)
    game.register_clock_factory("mine-fuse", mine.ensure_fuse_clock)
    game.register_clock_factory("map-clock", ship.ensure_map_clock)

    # May's hints: TIP MAY [#]; tracking for conditional hints
    from content import may_hints
    game.register_input_hook(may_hints.tip_input_hook)
    game.register_input_hook(may_hints.give_zenni_input_hook)   # GIVE 3 ZENNI TO MAY
    game.register_enter_hook(may_hints.on_enter)

    # Floor listings for plural and mass names (mechanics.md)
    for name, article in _ARTICLES.items():
        world.objects[name].article = article

    # Start in the White House — the player object in it, not just "here"
    world.here = world.rooms["WHITE-HOUSE"]
    world.move_object(world.player, world.here)


_ARTICLES = {
    "LOCKPICKS": "plural", "APPRENTICE-GLOVES": "plural", "BARTENDERS-BOOTS": "plural",
    "CHARCOAL": "some", "SILVER-DUST": "some", "BOG-THYME": "some", "FIRE-CLAY": "some",
    "CLAY-ADHESIVE": "some", "ENCHANTED-HONEY": "some", "MORTAR": "some",
    "THIN-PAPER": "some", "RUNED-METAL": "some",
}


def _make_player(world) -> None:
    player = GameObject(
        name="PLAYER",
        desc="Adventurer",
        synonyms=["me", "myself", "self"],
    )
    from content import ink, ring

    def _player_action(w):
        # The ring can't be dropped; inked: NPC refusals, Will's disdain
        return ring.guard(w) or ink.player_action(w)

    player.action = _player_action
    world.register_object(player)
    world.player = player
    world.winner = player


def _init_player_state(world) -> None:
    """
    Player stats use lowercase keys (content/player.py, combat.py, experience.py,
    corruption.py, quests.py). Story/world flags use UPPERCASE-HYPHEN keys.
    Class-dependent values (hearts, skill_*) are set by char_create.
    """
    world.globals.update({
        "hearts": 5,
        "max_hearts": 5,
        "zenni": 0,
        "xp": 0,
        "level": 1,
        "ring_corruption": 0,
        "ring_worn": False,
        "enchanted_glasses_worn": False,
        "actually_enchanted_glasses_worn": False,
    })


def _place_objects(world) -> None:
    world.move_object(world.objects["MAILBOX-WHITE-HOUSE"], world.rooms["WHITE-HOUSE"])
    world.move_object(world.objects["PAINTING"],            world.rooms["WIZARDS-TOWER"])
    world.move_object(world.objects["MAILBOX-TOWER"],       world.rooms["TALE-AND-ALE"])
    world.move_object(world.objects["ENCHANTED-GLASSES"],   world.rooms["WIZARDS-BEDROOM"])
    world.move_object(world.objects["NIGHTSTAND"],          world.rooms["WIZARDS-BEDROOM"])
    world.move_object(world.objects["QUEST-BOARD"],         world.rooms["BAR"])
    world.move_object(world.objects["DRAGON-NIP"],          world.rooms["WIZARDS-BEDROOM"])
    world.move_object(world.objects["RING"],                world.objects["PYRONICUS"])
    # Mine objects
    world.move_object(world.objects["PICKAXE"],          world.rooms["MAIN-SHAFT"])
    world.move_object(world.objects["PIE-RAT-DISGUISE"], world.rooms["RATS-NEST"])
    world.move_object(world.objects["FLINT-AND-STEEL"],  world.rooms["ASSAY-ROOM"])
    world.move_object(world.objects["WEAK-POINT"],       world.rooms["MINE-TUNNELS"])
    # Shamus's stock (gunpowder, torch, fishing rod, thin paper) isn't in the
    # world until it's bought — BUY X in the Kitchen (verbs.buy_input_hook)
    world.move_object(world.objects["WHISPERING-JAR"], world.rooms["PIPE-ROOM"])
    world.move_object(world.objects["TY"],        world.rooms["CASINO-CORNER"])
    world.move_object(world.objects["LIBRARIAN"], world.rooms["LIBRARY"])
    world.move_object(world.objects["ARCHIVIST"], world.rooms["STACKS"])
    # TREASURE-MAP is found aboard; PIE-RAT-COIN is flipped when the ship comes back
    world.move_object(world.objects["BURIED-CHEST"], world.rooms["DESERT-ISLAND"])
    world.move_object(world.objects["SHIP-IN-A-BOTTLE"], world.rooms["ROUNDABOUT-POND"])
    # Ship objects
    world.move_object(world.objects["SHOVEL"], world.rooms["SHIP-DECK"])
    world.move_object(world.objects["ROPE"],   world.rooms["DOCKS"])
    # NPCs
    world.move_object(world.objects["SHAMUS"], world.rooms["KITCHEN"])
    from content.verbs import slate_action
    world.move_object(world.objects["SLATE"], world.rooms["KITCHEN"])
    world.objects["SLATE"].action = slate_action
    world.move_object(world.objects["KEVRY"],  world.rooms["CAPTAINS-QUARTERS"])
    world.move_object(world.objects["PYRONICUS"], world.rooms["PYRONICUS-FORGE"])
    world.move_object(world.objects["WILL"],   world.rooms["WIZARDS-TOWER"])
    world.move_object(world.objects["FORGE"],  world.rooms["PYRONICUS-FORGE"])
    # Archery Range & Viking Encampment
    for obj, room in (
        ("RAZNAK",       "ARCHERY-RANGE"),
        ("IVANAAR",      "VIKING-ENCAMPMENT"),
        ("BANNER",       "VIKING-ENCAMPMENT"),
        ("HAALVAR",      "HAALVARS-HUT"),
        ("RIDDLE-STONE", "HAALVARS-HUT"),
        ("CHILD",        "RITUAL-CIRCLE"),
        ("EARTH-STONE",  "RITUAL-CIRCLE"),
        ("AIR-STONE",    "RITUAL-CIRCLE"),
        ("FIRE-STONE",   "RITUAL-CIRCLE"),
        ("WATER-STONE",  "RITUAL-CIRCLE"),
        ("HEART-STONE",  "RITUAL-CIRCLE"),
        ("AYLORA",       "FIRE-PIT"),
    ):
        world.move_object(world.objects[obj], world.rooms[room])
    world.move_object(world.objects["STATUE"], world.rooms["TOWN-SQUARE"])
    world.move_object(world.objects["KNIGHT"], world.rooms["TOWN-SQUARE"])
    world.move_object(world.objects["SCROLL-UNBIND-UNDEAD"], world.rooms["LIGHTHOUSE"])
    world.move_object(world.objects["MUSIC-BOX"],    world.rooms["WIZARDS-TOWER"])
    world.move_object(world.objects["SCROLL-LIGHT"], world.rooms["WIZARDS-TOWER"])
    # Old Oak area (KITE and OLD-OAK-RUNE-STONE appear on CLIMB TREE)
    world.move_object(world.objects["OAK-CHILD"], world.rooms["OLD-OAK"])
    world.move_object(world.objects["OAK-TREE"],  world.rooms["OLD-OAK"])
    world.move_object(world.objects["BEEKEEPER"], world.rooms["BEEKEEPERS-COTTAGE"])
    world.move_object(world.objects["BOWL-PIECE-FOREST"], world.rooms["ROUNDABOUT-FOREST"])
    world.move_object(world.objects["BOWL-PIECE-BOG"],    world.rooms["BOG-SW"])
    world.move_object(world.objects["BOG-THYME"],         world.rooms["BOG-SW"])
    world.move_object(world.objects["BOG-RUNE-STONE"],    world.rooms["BOG-NE"])
    world.move_object(world.objects["HOLLOW-LOG"],        world.rooms["BOG-NW"])
    world.move_object(world.objects["MUSIC-BOX-KEY"],     world.rooms["BOG-NW"])
    world.move_object(world.objects["MUGGER"], world.rooms["BACK-ALLEY"])
    world.move_object(world.objects["MAY"],    world.rooms["BAR"])
    world.move_object(world.objects["LYNDS"],  world.rooms["TALE-AND-ALE"])
    # HEART-NECKLACE is handed over when Lynds is beaten
    world.move_object(world.objects["DANKHAUS"], world.rooms["BOG-SE"])
    world.move_object(world.objects["LITLOCK"],  world.rooms["DANKHAUS-COMMON-ROOM"])
    world.move_object(world.objects["AURIX"],    world.rooms["AURIX-ROOM"])
    world.move_object(world.objects["TICKET-BOOTH"],  world.rooms["CHUCKLE-ENTRANCE"])
    world.move_object(world.objects["CHUCKLE-HOOKS"], world.rooms["CHUCKLE-ENTRANCE"])
    world.move_object(world.objects["GHOST"],         world.rooms["GHOSTS-ROOM"])
    # POCKET-WATCH is dropped when the ghost is freed
    world.move_object(world.objects["RECORDS-WORKER"], world.rooms["RECORDS-ROOM"])
    world.move_object(world.objects["DISPLAY-CABINET"], world.rooms["UPPER-HALL"])
    world.move_object(world.objects["WAX-SEAL"],        world.rooms["UPPER-HALL"])
    world.move_object(world.objects["ROWAN-FINCH"],    world.rooms["COUNCIL-CHAMBER"])
    # Quest 32: MIDDLE-TIER-KEY goes to the player when Rowan hands it over
    world.move_object(world.objects["GRAVESTONE"], world.rooms["BOG-SE"])
    world.move_object(world.objects["GRAVE"],      world.rooms["GRAVEYARD"])
    # Quest 25: CELLAR-KEY and BARTENDERS-BOOTS come from May
    for obj, room in (("CELLAR-DOOR", "KITCHEN"), ("DRAIN", "KITCHEN"),
                      ("TUNNEL-DOOR-CELLAR", "CELLAR"), ("TUNNEL-DOOR-BONE", "BONE-PASSAGE"),
                      ("CASHBOX", "CELLAR")):
        world.move_object(world.objects[obj], world.rooms[room])
    # TOWN-CHARTER is handed over for the pocket watch
    world.move_object(world.objects["BOGGART"], world.rooms["TOLL-BRIDGE"])
    # STRONGBOX is dropped when the Boggart leaves
    for obj, room in (("PORTCULLIS-BAR", "SUPPLY-ROOM"), ("MORTAR", "SUPPLY-ROOM"),
                      ("SACK-OF-SALT", "SUPPLY-ROOM"), ("HAND-CART", "STORAGE-AREA"),
                      ("SUPPORT-BEAM", "STORAGE-AREA"), ("GALLERY-TIMBERS", "COLLAPSED-GALLERY"), ("IDOL", "IDOL-ROOM"), ("IDOL-DOOR", "IDOL-ROOM"),
                      ("SMOKE-JAR", "SUPPLY-ROOM"), ("SMALL-CLAY-POT", "SUPPLY-ROOM"),
                      ("PRESSURE-PLATE", "COMBAT-ROOM"), ("INSIGNIA", "CREATURE-DEN"),
                      ("CROWBAR", "PRAYER-ALCOVE"), ("GLACIER-MELT", "PRAYER-ALCOVE"),
                      ("BOWL-PIECE-SHRINE", "SHRINE-ROOM"), ("PORTCULLIS", "PORTCULLIS-CORRIDOR"),
                      ("MID-TIER-DOOR", "MID-TIER-KEY-DOOR"), ("MINE-CHEST", "MINE-PASSAGE"),
                      ("CHARCOAL", "MINE-PASSAGE"), ("SILVER-DUST", "MINE-PASSAGE"),
                      ("GOLD-WATCH", "THE-CREVICE"), ("CREVICE-SKELETON", "THE-CREVICE"),
                      ("ENGRAVING", "INSCRIPTION-CHAMBER"), ("SNARE", "INSCRIPTION-CHAMBER"),
                      ("DUNGEON-RUNE-STONE", "INSCRIPTION-CHAMBER"), ("BONE-FLUTE", "CAVE-CREATURES-LAIR"),
                      ("VAULT-CHEST", "MAGNETIC-VAULT"), ("LODESTONE", "MAGNETIC-VAULT"),
                      ("DEEP-LOCK", "DEEP-LOCK-DOOR"),
                      ("SUPPORT-TIMBER", "STORED-ROOM"), ("KEY-RING", "LOWER-CRYPT"),
                      ("SKELETON", "LOWER-CRYPT"), ("KEEPER-SEAL", "LOWER-CRYPT"),
                      ("PENDULUM-BLADE", "LOWER-CRYPT"), ("FIRE-CLAY", "THERMAL-VENT-ROOM"),
                      ("VENT-CEILING", "THERMAL-VENT-ROOM"), ("KEEPER-DOOR", "CHURCH-NAVE"),
                      ("HOLY-WATER", "KEEPERS-CHAMBER"), ("KEEPER-NOTE", "KEEPERS-CHAMBER"),
                      ("BONES", "ANTECHAMBER"), ("WEREWOLF", "STILL-DEN"), ("IVORY-TORCH", "STILL-DEN"),
                      ("ALCOVE-WALL", "TOOL-ALCOVE"),
                      ("TROPHY-CASE", "TOWN-HALL-TOWER"),
                      ("AQUEDUCT-BLOCKS", "COLLAPSED-AQUEDUCT"), ("AQUEDUCT", "COLLAPSED-AQUEDUCT"),
                      ("FOUNTAIN", "TOWN-SQUARE"), ("SHRINE-PEDESTAL", "ROUNDABOUT-FOREST"),
                      ("ALTAR-STONE", "ALTAR"), ("DIAL", "ALTAR")):
        world.move_object(world.objects[obj], world.rooms[room])
    # Trap 15: the diamond brooch waits inside the Magnetic Vault chest
    world.move_object(world.objects["DIAMOND-BROOCH"], world.objects["VAULT-CHEST"])
    world.move_object(world.objects["FLOODED-POOL"], world.rooms["FLOODED-PASSAGE"])
    world.move_object(world.objects["ICE-BLOCK"], world.rooms["FOUNTAIN-ROOM"])
    world.move_object(world.objects["SPIRITS"], world.rooms["SPIRIT-ROOM"])
    world.move_object(world.objects["QUEEN-VIAL"], world.rooms["SWARM-TREE"])
    world.objects["QUEEN-VIAL"].give_to = "BEEKEEPER"
    for obj, room in (("APPRENTICE", "LOST-APPRENTICES-CELL"),
                      ("APPRENTICE-TUNNEL", "LOST-APPRENTICES-CELL"),
                      ("CACHE-RUBBLE", "SUPPLY-CACHE"), ("GOLD-NUGGET", "SUPPLY-CACHE")):
        world.move_object(world.objects[obj], world.rooms[room])
    for obj in ("FLOOD-PLATE", "LEVER-LEFT", "LEVER-MIDDLE", "LEVER-RIGHT"):
        world.move_object(world.objects[obj], world.rooms["FLOODING-ROOM"])
    world.move_object(world.objects["FUNERAL-MASK"], world.rooms["BURIAL-CHAMBER"])

    # Which key opens what — the parser uses this to pick the right key when
    # several match "key" (UNLOCK DOOR WITH KEY)
    for lock, key in (("CELLAR-DOOR", "CELLAR-KEY"), ("MID-TIER-DOOR", "MIDDLE-TIER-KEY"),
                      ("KEEPER-DOOR", "KEY-RING"), ("MUSIC-BOX", "MUSIC-BOX-KEY")):
        world.objects[lock].key_name = key

    # Who an item is meant for — the parser uses this when several carried items
    # match (GIVE SCROLL TO WILL means a spell scroll, not the incantation scroll)
    from content.will import SPELL_SCROLLS
    from content.vikings import RUNE_STONES
    for scroll in SPELL_SCROLLS:
        world.objects[scroll].give_to = "WILL"
    # GIVE STONES / GIVE STONE TO IVANAAR hands over all three (Quest 42)
    for stone in RUNE_STONES:
        world.objects[stone].give_to = "IVANAAR"
        world.objects[stone].give_as_set = True

    # LOCKPICKS drop when the mugger is slain
    # RUNED-METAL is handed over by Ivanaar; PALE-BLADE is forged by Pyronicus


def _wire_whitehouse_action(world, game) -> None:
    """
    White House: any command except OPEN MAILBOX (or QUIT) returns the Zork joke.
    OPEN MAILBOX is handled by the mailbox object action (V-OPEN verb handler).
    """
    from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG

    def whitehouse_action(w, msg=M_BEG):
        if msg == M_BEG:
            # Block all verbs except V-OPEN targeting the mailbox
            if w.prsa == "V-OPEN" and w.prso is not None and w.prso.name == "MAILBOX-WHITE-HOUSE":
                return M_NOT_HANDLED  # let V-OPEN proceed
            if w.prsa not in (None, "V-WALK", "V-LOOK", "V-EXAMINE", "V-QUIT"):
                print('What does this look like? A Great Underground Empire?')
                return M_HANDLED
        return M_NOT_HANDLED

    world.rooms["WHITE-HOUSE"].action = whitehouse_action
