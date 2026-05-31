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

    report()
