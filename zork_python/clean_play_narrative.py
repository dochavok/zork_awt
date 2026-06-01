"""
Play through the narrative walkthrough (walkthrough_text_narrative.txt).
random.randint is patched to _always_max for deterministic combat.
"""
import io, sys
sys.path.insert(0, 'c:/zork_awt/zork_python')
from unittest.mock import patch

def _always_max(a, b): return b

with patch('random.randint', _always_max):
    from engine.world import World
    from engine.clock import Clock
    from engine.parser import Parser
    from engine.game import Game
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    from content.init import initialize_world

    world = World()
    game = Game(world, Parser(make_vocabulary(), make_syntax_rules()), Clock())
    initialize_world(world, game)

    buf = io.StringIO()
    with patch('sys.stdout', buf):
        game.enter_room(world.here)
    print(buf.getvalue(), end='')

    def c(cmd):
        buf = io.StringIO()
        with patch('sys.stdout', buf):
            game.do_turn(cmd)
        out = buf.getvalue()
        print(f'> {cmd}')
        print(out, end='' if out.endswith('\n') else '\n')
        return out

    def sec(n):
        print(f'\n{"="*60}')
        print(f'  {n}')
        print(f'{"="*60}')

    def put_treasures(keep_names=()):
        """Deposit all treasures from inventory into the trophy case.

        Identifies non-treasure items (tvalue == 0) and any explicitly kept
        items by name, then issues 'put all but X in case'.  This exercises
        the all-but parser syntax and deposits exactly the treasure items.
        """
        inv = list(world.winner.contents) if world.winner else []
        keep_ids = {id(world.objects[k]) for k in keep_names if k in world.objects}
        to_deposit = [o for o in inv if o.tvalue > 0 and id(o) not in keep_ids]
        if not to_deposit:
            return
        deposit_ids = {id(o) for o in to_deposit}

        # Build full exclusion list: everything in scope that is NOT being deposited.
        # Walk inventory, room contents (recursively into open containers), and
        # global objects to capture everything the parser's LOC_HAVE would find.
        def _collect(container, seen):
            for o in list(getattr(container, 'contents', [])):
                if id(o) not in seen:
                    seen.add(id(o))
                    yield o
                    if o.has_flag('CONTBIT') and (o.has_flag('OPENBIT') or o.has_flag('TRANSBIT')):
                        yield from _collect(o, seen)

        seen_ids: set = set()
        scope_objs = []
        for o in _collect(world.winner, seen_ids):
            scope_objs.append(o)
        if world.here:
            for o in _collect(world.here, seen_ids):
                scope_objs.append(o)
        for o in world.global_objects_for():
            if id(o) not in seen_ids:
                seen_ids.add(id(o))
                scope_objs.append(o)

        exclude = [o for o in scope_objs
                   if id(o) not in deposit_ids and o.synonyms]

        if not exclude:
            c('put all in case')
            return
        nouns = [o.synonyms[0] for o in exclude]
        c('put all but ' + ' and '.join(nouns) + ' in case')

    def report():
        print(f'\n{"="*60}')
        print(f'  FINAL STATE')
        print(f'{"="*60}')
        print(f'Score: {world.score}')
        print(f'Moves: {world.moves}')
        print(f'Location: {world.here.name if world.here else "unknown"}')
        inv = [o.desc for o in (world.winner.contents if world.winner else [])]
        print(f'Inventory: {inv}')
        tc = world.objects.get('TROPHY-CASE')
        if tc:
            print(f'Trophy case: {[o.desc for o in tc.contents]}')

    # ------------------------------------------------------------------
    sec('A - The Jeweled Egg')
    # ------------------------------------------------------------------
    # Narrative: OPEN MAILBOX, READ LEAFLET, NORTH x2, CLIMB TREE, TAKE EGG
    c('open mailbox')
    c('read leaflet')
    c('north')
    c('north')
    c('climb tree')
    c('take egg')

    # ------------------------------------------------------------------
    sec('B - The Troll')
    # ------------------------------------------------------------------
    # Narrative: DOWN, SOUTH, EAST; OPEN WINDOW, WEST; TAKE BOTTLE, WEST;
    # OPEN CASE, TAKE SWORD, TAKE LANTERN; EAST, UP;
    # TURN LANTERN ON, TAKE ROPE, TURN LANTERN OFF; DOWN, WEST;
    # MOVE RUG, OPEN TRAP DOOR, DOWN; TURN LANTERN ON;
    # NORTH, FIGHT TROLL WITH SWORD, DIAGNOSE
    c('down')
    c('south')
    c('east')
    c('open window')
    c('west')
    c('take bottle')
    c('west')
    c('open case')
    c('take sword')
    c('take lamp')
    c('east')
    c('up')
    c('turn on lamp')
    c('take rope')
    c('turn off lamp')
    c('down')
    c('west')
    c('move rug')
    c('open trap door')
    c('down')
    c('turn on lamp')
    c('north')
    c('kill troll with sword')
    c('diagnose')

    # ------------------------------------------------------------------
    sec('C - The Dead Adventurer')
    # ------------------------------------------------------------------
    # Narrative: WEST (maze); SOUTH, EAST, UP (dead adventurer);
    # TAKE COINS; SOUTHWEST, EAST, SOUTH, SOUTHEAST (cyclops room)
    c('west')
    c('south')
    c('east')
    c('up')
    c('take coins')
    c('southwest')
    c('east')
    c('south')
    c('southeast')

    # ------------------------------------------------------------------
    sec('D - Cyclops')
    # ------------------------------------------------------------------
    # Narrative: SAY "ULYSSES"; NORTHWEST, DROP COINS, SOUTHEAST;
    # UP; GIVE EGG TO THIEF; DOWN, NORTHWEST; TAKE COINS;
    # SOUTHEAST, EAST, EAST; OPEN CASE, PUT COINS IN CASE
    c('ulysses')
    c('northwest')
    c('drop coins')
    c('southeast')
    c('up')
    c('give egg to thief')
    c('down')
    c('northwest')
    c('take coins')
    c('southeast')
    c('east')
    c('east')
    c('open case')
    c('put coins in case')

    # ------------------------------------------------------------------
    sec('E - Exorcism')
    # ------------------------------------------------------------------
    # Narrative: DOWN; NORTH, EAST, NORTH, NORTHEAST, EAST, NORTH (dam lobby);
    # TAKE MATCHBOOK; SOUTH, SOUTH, DOWN (loud room), WEST, SOUTHEAST, EAST (dome);
    # TIE ROPE TO RAILING, DOWN (torch room); SOUTH, TAKE BELL;
    # SOUTH (altar), TAKE CANDLES, TAKE BOOK; DOWN, DOWN (entrance to hades);
    # OPEN MATCHBOOK, RING BELL, LIGHT MATCH, LIGHT CANDLES WITH MATCH,
    # WAVE CANDLES, READ BOOK;
    # POUR WATER ON BELL, TAKE BELL, PUT CANDLES OUT, DROP BOTTLE;
    # SOUTH (land of living dead), TAKE SKULL;
    # NORTH, UP, NORTH, NORTH, NORTH, WEST, WEST, SOUTH
    c('open trap door')
    c('down')
    c('north')
    c('east')
    c('north')
    c('northeast')
    c('east')
    c('north')
    c('take matchbook')
    c('south')
    c('south')
    c('down')
    c('west')
    c('southeast')
    c('east')
    c('tie rope to railing')
    c('down')
    c('south')
    c('take bell')
    c('south')
    c('take candles')
    c('take book')
    c('down')
    c('down')
    c('open matchbook')
    c('ring bell')
    c('take candles')
    c('light match')
    c('light candles with match')
    c('wave candles')
    c('read book')
    c('pour water on bell')
    c('take bell')
    c('put out candles')
    c('drop bottle')
    c('south')
    c('take skull')
    c('north')      # land-of-dead → entrance-to-hades
    c('up')         # entrance-to-hades → tiny-cave
    c('north')      # tiny-cave → mirror-room-2 (mine area)
    c('north')      # → narrow-passage
    c('north')      # → round-room
    c('west')       # → east-west passage
    c('west')       # → troll room
    c('south')      # → cellar

    # ------------------------------------------------------------------
    sec('F - A Quick Detour')
    # ------------------------------------------------------------------
    # Narrative: SOUTH, EAST (gallery), TAKE PAINTING;
    # Retrace: WEST, NORTH, UP (living room)
    c('south')          # cellar → east-of-chasm
    c('east')           # east-of-chasm → gallery
    c('take painting')
    c('west')           # gallery → east-of-chasm
    c('north')          # east-of-chasm → cellar
    c('up')             # cellar → living room

    # ------------------------------------------------------------------
    sec('G - Fighting the Thief')
    # ------------------------------------------------------------------
    # Narrative: TAKE COINS, WEST x2; SAVE; NORTH (treasure room);
    # GIVE COINS TO THIEF, KILL THIEF WITH SWORD, GIVE SKULL TO THIEF,
    # repeat until thief dead (RESTORE and retry if not);
    # DOWN, EAST x2, DIAGNOSE; WEST x2, UP, TAKE ALL;
    # DOWN, EAST x2, PUT ALL TREASURES IN CASE;
    # Return for stiletto; TAKE CANARY, EAST x2, NORTH x2, UP,
    # WIND CANARY, DOWN, TAKE BAUBLE, SOUTH, EAST, WEST x2,
    # PUT ALL TREASURE IN CASE
    import tempfile, os as _os

    _save_path = tempfile.mktemp(suffix='.sav')
    world.set_global('SAVE-FILE', _save_path)

    c('take coins')
    c('west')
    c('west')
    c('save')

    _thief = world.objects.get('THIEF')
    for _attempt in range(20):
        c('up')                     # cyclops room → treasure room
        c('give coins to thief')
        c('kill thief with sword')
        c('give skull to thief')
        c('kill thief with sword')
        if _thief and _thief.has_flag('INVISIBLE'):
            break
        c('restore')                # back to cyclops room, retry

    if _os.path.exists(_save_path):
        _os.unlink(_save_path)
    world.set_global('SAVE-FILE', None)

    # Recover and loot
    c('down')                       # treasure room → cyclops room
    c('east')                       # → strange passage
    c('east')                       # → living room
    c('diagnose')
    c('west')                       # → strange passage
    c('west')                       # → cyclops room
    c('up')                         # → treasure room
    c('take all')
    c('down')                       # → cyclops room
    c('east')                       # → strange passage
    c('east')                       # → living room
    put_treasures()
    # Return for stiletto (narrative; take all already grabbed it)
    c('west')
    c('west')
    c('up')
    c('take stiletto')
    c('down')
    c('east')
    c('east')
    # Wind the canary to produce the bauble
    c('take canary')
    c('east')
    c('east')
    c('north')
    c('north')
    c('up')
    c('wind up canary')
    c('down')
    c('take bauble')
    c('south')
    c('east')
    c('west')
    c('west')
    put_treasures()

    # ------------------------------------------------------------------
    sec('H - The Treasure Chest in the Reservoir')
    # ------------------------------------------------------------------
    # Navigate to Maintenance Room to get wrench+screwdriver, enable bolt
    c('down')           # living room → cellar
    c('north')          # cellar → troll room
    c('east')           # troll room → ew-passage
    c('north')          # ew-passage → chasm
    c('northeast')      # chasm → reservoir-south
    c('east')           # reservoir-south → dam-room
    c('north')          # dam-room → dam-lobby
    c('north')          # dam-lobby → maintenance-room
    c('push red button')    # turns room lights on permanently
    c('turn off lamp')      # save batteries
    c('take wrench')
    c('take screwdriver')
    c('push yellow button') # enables bolt turning (GATE-FLAG)
    c('south')          # maintenance-room → dam-lobby
    c('south')          # dam-lobby → dam-room
    c('turn bolt with wrench')  # opens sluice gates; drains reservoir immediately
    c('west')           # dam-room → reservoir-south
    c('turn on lamp')
    c('north')          # reservoir-south → reservoir (LOW-TIDE now open)
    c('drop all but lamp')  # drop at RESERVOIR; pick up on the way back
    c('north')          # reservoir → reservoir-north
    c('north')          # reservoir-north → atlantis-room
    c('take trident')
    c('south')          # atlantis-room → reservoir-north
    c('south')          # reservoir-north → reservoir
    c('take trunk')
    c('south')          # reservoir → reservoir-south
    c('southwest')      # reservoir-south → chasm
    c('southwest')      # chasm → ew-passage
    c('west')           # ew-passage → troll-room
    c('south')          # troll-room → cellar
    c('up')             # cellar → living-room
    put_treasures()

    # ------------------------------------------------------------------
    sec('I - The Coal Mines')
    # ------------------------------------------------------------------
    # Get garlic first (protection against bat)
    c('east')               # living room → kitchen
    c('open sack')
    c('take garlic')
    c('west')               # kitchen → living room
    # Navigate back to reservoir to collect dropped items
    c('down')
    c('north')
    c('east')
    c('north')
    c('northeast')
    c('north')              # reservoir-south → reservoir
    c('take all')           # reclaim everything dropped in section H
    # Navigate to bat room: reservoir → reservoir-north → atlantis → small-cave →
    #   mirror-room-1 → cold-passage → slide-room → mine-entrance → squeeky → bat-room
    c('north')              # reservoir → reservoir-north
    c('north')              # reservoir-north → atlantis-room  (narrative missing this NORTH)
    c('up')                 # atlantis-room → small-cave
    c('north')              # small-cave → mirror-room-1
    c('north')              # mirror-room-1 → cold-passage
    c('west')               # cold-passage → slide-room
    c('north')              # slide-room → mine-entrance
    c('west')               # mine-entrance → squeeky-room
    c('north')              # squeeky-room → bat-room
    c('take figurine')
    c('east')               # shaft room
    c('put screwdriver in basket')
    c('drop matchbook')
    c('drop candles')
    # Down through smelly/gas rooms into coal mine
    c('north')              # smelly room
    c('down')               # gas room
    c('take bracelet')
    c('east')
    c('northeast')
    c('southeast')
    c('southwest')
    c('down')
    c('down')
    c('west')
    c('drop all but lamp')
    c('east')
    c('south')
    c('take coal')
    c('north')
    c('up')
    c('up')
    c('north')
    c('east')
    c('south')
    c('north')
    c('up')
    c('south')              # back at shaft room
    # Load basket and lower it
    c('take candles')
    c('take matchbook')
    c('light match')
    c('light candles with match')
    c('put candles in basket')
    c('put coal in basket')
    c('lower basket')
    # Navigate back down to lower shaft / machine room
    # shaft-room → smelly → gas → mine-1 → mine-2 → mine-3 → mine-4 → ladder-top → ladder-bottom → timber-room
    c('north')              # shaft-room → smelly-room
    c('down')               # smelly-room → gas-room
    c('east')               # gas-room → mine-1
    c('northeast')          # mine-1 → mine-2
    c('southeast')          # mine-2 → mine-3
    c('southwest')          # mine-3 → mine-4
    c('down')               # mine-4 → ladder-top
    c('down')               # ladder-top → ladder-bottom
    c('west')               # ladder-bottom → timber-room
    c('drop all')
    c('west')               # timber-room → lower-shaft (basket now here)
    c('take candles')
    c('take coal')
    c('take screwdriver')
    c('south')              # machine room
    c('open lid')
    c('put coal in machine')
    c('close lid')
    c('turn switch with screwdriver')
    c('open lid')
    c('take diamond')
    c('north')              # lower shaft
    c('put candles in basket')
    c('put diamond in basket')
    c('put screwdriver in basket')
    c('east')
    # Backtrack up to shaft room to raise basket
    c('take all but timbers and stiletto')
    c('east')
    c('up')
    c('up')
    c('north')
    c('east')
    c('south')
    c('north')
    c('up')
    c('south')              # shaft room
    c('raise basket')
    c('take candles')
    c('take diamond')
    # Return to trophy case
    c('west')
    c('south')
    c('east')
    c('south')
    c('down')
    c('up')
    put_treasures()

    # ------------------------------------------------------------------
    sec('J - Eerie Silence')
    # ------------------------------------------------------------------
    # Navigate to dam to close it (makes loud room quiet)
    c('down')
    c('north')
    c('east')
    c('east')
    c('north')
    c('northeast')
    c('east')               # dam-room
    c('turn bolt with wrench')
    # Quickly to loud room (now quiet) for platinum bar
    c('south')              # deep-canyon
    c('down')               # loud-room
    c('take bar')
    c('west')               # round-room
    # Navigate to torch room
    c('southeast')          # engravings-cave
    c('east')               # dome-room
    c('down')               # torch-room (rope still tied)
    c('turn off lamp')
    c('drop lamp')
    c('drop candles')
    c('take torch')
    # Get sceptre from coffin
    c('south')              # north-temple
    c('east')               # egypt-room
    c('open coffin')
    c('take sceptre')
    # Return to trophy case
    c('west')
    c('south')
    c('down')
    c('north')
    c('north')
    c('north')
    c('west')
    c('west')
    c('south')
    c('up')
    put_treasures(keep_names=('SCEPTRE', 'TORCH'))

    # ------------------------------------------------------------------
    sec('K - End of the Rainbow')
    # ------------------------------------------------------------------
    # Navigate to end of rainbow: living room → kitchen → behind house →
    # clearing → canyon view → cliff middle → canyon bottom → end of rainbow
    c('east')               # kitchen
    c('east')               # behind house
    c('east')               # clearing
    c('east')               # canyon view
    c('down')               # cliff middle
    c('down')               # canyon bottom
    c('north')              # end of rainbow
    c('wave sceptre')
    c('take pot')
    # Cross rainbow to sandy beach: east (onto rainbow) → east (falls) →
    # north (shore) → north (sandy beach)
    c('east')               # on the rainbow
    c('east')               # aragain falls
    c('north')              # shore
    c('north')              # sandy beach
    c('take shovel')
    c('northeast')          # sandy cave
    c('dig sand with shovel')
    c('take scarab')
    # Backtrack to trophy case
    c('southwest')          # sandy beach
    c('south')              # shore
    c('south')              # aragain falls
    c('west')               # on the rainbow
    c('west')               # end of rainbow
    c('southwest')          # canyon bottom
    c('up')                 # cliff middle
    c('up')                 # canyon view
    c('northwest')          # clearing
    c('west')               # behind house
    c('west')               # kitchen
    c('west')               # living room
    put_treasures(keep_names=('TORCH',))

    # ------------------------------------------------------------------
    sec('L - Row, Row, Row Your Boat')
    # ------------------------------------------------------------------
    # Navigate to dam, reopen it, then get pump from reservoir-north
    c('down')
    c('north')
    c('east')
    c('east')
    c('east')
    c('up')             # loud-room → deep-canyon
    c('northwest')      # reservoir-south
    c('east')           # dam-room
    c('turn bolt with wrench')  # reopen dam; LOW-TIDE = True
    c('west')           # reservoir-south
    c('north')          # reservoir
    c('north')          # reservoir-north
    c('take pump')
    # Get inflatable boat from dam-base
    c('south')          # reservoir
    c('south')          # reservoir-south
    c('east')           # dam-room
    c('down')           # dam-base
    c('take plastic')
    # Navigate to white cliffs beach to launch
    c('up')             # dam-room
    c('south')          # deep-canyon
    c('down')           # loud-room
    c('east')           # damp-cave
    c('east')           # white-cliffs-north (launch point)
    c('drop all but pump and torch')
    c('inflate plastic with pump')
    c('get in boat')
    c('launch boat')
    c('wait')           # river carries us: white-cliffs-north → river-3
    c('wait')           # river-3, clock ticking
    c('wait')           # → river-4 (buoy is here)
    c('take buoy')
    c('east')           # land on sandy beach
    c('open buoy')
    c('take emerald')
    c('drop buoy')
    c('get out of boat')
    c('deflate boat')
    c('take plastic')
    # Return to trophy case via rainbow path
    c('south')          # shore → aragain falls
    c('west')           # on the rainbow
    c('west')           # end of rainbow
    c('southwest')      # canyon bottom
    c('up')             # cliff middle
    c('up')             # canyon view
    c('northwest')      # clearing
    c('west')           # behind house
    c('west')           # kitchen
    c('west')           # living room
    put_treasures(keep_names=('TORCH',))
    # Retrieve dropped items from white cliffs beach
    c('down')
    c('north')
    c('east')
    c('east')
    c('east')
    c('east')
    c('east')           # white-cliffs-north
    c('take all')       # label stays inside the deflated boat

    # ------------------------------------------------------------------
    sec('M - Ramses Coffin')
    # ------------------------------------------------------------------
    # Navigate from white cliffs beach to egypt room
    c('west')           # damp-cave
    c('west')           # loud-room
    c('west')           # round-room
    c('southeast')      # engravings-cave
    c('east')           # dome-room
    c('down')           # torch-room
    c('south')          # north-temple
    c('east')           # egypt-room
    # Drop everything except torch to make room for coffin (size 55)
    c('drop all but torch')
    c('take coffin')
    # Navigate to south-temple (altar) to pray
    c('west')           # north-temple
    c('south')          # south-temple
    c('pray')           # warp to forest-1
    # Return to trophy case from forest-1
    c('east')           # path? or south?
    c('south')          # north-of-house
    c('southeast')      # east-of-house
    c('west')           # kitchen
    c('west')           # living-room
    put_treasures()

    # ------------------------------------------------------------------
    sec('O - Into the Tomb')
    # ------------------------------------------------------------------
    c('read parchment')
    c('east')           # kitchen
    c('east')           # behind house
    c('southwest')      # south of house
    c('northwest')      # west of house
    c('southwest')      # stone barrow (WON-FLAG required)
    c('in')             # enter tomb — win!

    report()
