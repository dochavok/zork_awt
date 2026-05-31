"""
Play through the narrative walkthrough (walkthrough_text_narrative.txt).
Commands are extracted from the narrative; output is captured and printed.
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
        treasures = [o for o in inv if o.tvalue > 0]
        if not treasures:
            return
        keep_ids = {id(world.objects[k]) for k in keep_names if k in world.objects}
        exclude = [o for o in inv if o.tvalue == 0 or id(o) in keep_ids]
        if not exclude:
            c('put all in case')
            return
        nouns = [o.synonyms[0] for o in exclude if o.synonyms]
        if not nouns:
            c('put all in case')
            return
        c('put all but ' + ' and '.join(nouns) + ' in case')

    # ------------------------------------------------------------------
    sec('A - The Jeweled Egg')
    # ------------------------------------------------------------------
    c('open mailbox')
    c('read leaflet')
    c('north')
    c('north')
    c('climb tree')
    c('take egg')

    # ------------------------------------------------------------------
    sec('B - The Troll')
    # ------------------------------------------------------------------
    c('down')
    c('south')
    c('east')
    c('open window')
    c('west')           # enter house via kitchen window
    c('take bottle')
    c('west')           # living room
    c('open case')
    c('take sword')
    c('take lamp')
    c('east')           # kitchen
    c('up')             # attic
    c('turn on lamp')
    c('take rope')
    c('turn off lamp')
    c('down')           # kitchen
    c('west')           # living room
    c('move rug')
    c('open trap door')
    c('down')           # cellar
    c('turn on lamp')
    c('north')          # troll room
    c('kill troll with sword')
    c('diagnose')

    # ------------------------------------------------------------------
    sec('C - The Dead Adventurer')
    # ------------------------------------------------------------------
    c('west')           # maze-1
    c('south')          # maze-2
    c('east')           # maze-3
    c('up')             # maze-5 (skeleton + coins)
    c('take coins')
    c('southwest')
    c('east')
    c('south')
    c('southeast')      # cyclops room

    # ------------------------------------------------------------------
    sec('D - Cyclops')
    # ------------------------------------------------------------------
    c('ulysses')
    c('northwest')      # maze-15
    c('drop coins')
    c('southeast')      # cyclops room
    c('up')             # treasure room (thief hideout)
    c('give egg to thief')
    c('down')           # cyclops room
    c('northwest')      # maze-15
    c('take coins')
    c('southeast')      # cyclops room
    c('east')           # strange passage
    c('east')           # living room
    c('open case')
    c('put coins in case')

    # ------------------------------------------------------------------
    sec('E - Exorcism')
    # ------------------------------------------------------------------
    c('open trap door')  # TOUCHBIT set from section B; must explicitly open before each descent
    c('down')           # cellar
    c('north')          # troll room
    c('east')           # ew-passage
    c('north')          # chasm
    c('northeast')      # reservoir south
    c('east')           # dam room
    c('north')          # dam lobby
    c('take matchbook')
    c('south')          # dam room
    c('south')          # deep canyon
    c('down')           # loud room
    c('west')           # round room
    c('southeast')      # engravings room
    c('east')           # dome room
    c('tie rope to railing')
    c('down')           # torch room
    c('south')          # ? heading toward bell
    c('take bell')
    c('south')          # altar
    c('take candles')
    c('take book')
    c('down')           # tiny cave
    c('down')           # entrance to hades
    # "open matchbook" is V-OPEN (requires DOORBIT) but MATCH has none.
    # ZIL MATCH-FUNCTION handles <VERB? COUNT OPEN> for display; use "count" instead.
    # Actually the sequence doesn't need the match count — go straight to ringing.
    c('ring bell')
    c('take candles')
    c('light match')
    c('light candles with match')
    c('wave candles')   # narrative says this; may not be a valid verb
    c('read book')
    c('pour water on bell')  # E-2: cool hot bell; empties the bottle
    c('take bell')
    c('put out candles')
    c('drop bottle')         # now empty after pouring water on bell
    c('south')          # land of living dead
    c('take skull')
    # return path from Hades: north, up, north north north, west west, south
    c('north')          # entrance to hades
    c('up')             # tiny cave
    c('north')
    c('north')
    c('north')
    c('west')
    c('west')
    c('south')

    # ------------------------------------------------------------------
    sec('F - A Quick Detour')
    # ------------------------------------------------------------------
    c('south')
    c('east')
    c('take painting')
    c('west')
    c('north')
    c('up')

    # ------------------------------------------------------------------
    sec('G - Fighting the Thief')
    # ------------------------------------------------------------------
    # We should be in Living Room after section F
    c('take coins')
    c('west')           # strange passage
    c('west')           # cyclops room
    c('up')             # treasure room (thief's hideout)
    c('give coins to thief')
    # TODO: Replace with a save/restore retry loop once save/restore is implemented.
    # See memory item test-game-save.md — the narrative describes saving before the
    # fight and restoring to retry until successful.  For now, force thief death
    # programmatically so the remainder of the walkthrough can proceed.
    from content.actions import _robber_function, F_DEAD
    _robber_function(world, F_DEAD)
    print("(thief defeated)")
    # G-3: narrative says go heal before looting
    c('down')           # cyclops room
    c('east')           # strange passage
    c('east')           # living room
    c('turn on lamp')
    c('diagnose')
    # G-3: return to loot the treasure room
    c('west')           # strange passage
    c('west')           # cyclops room
    c('up')             # treasure room
    c('take all')
    c('down')           # cyclops room
    c('east')           # strange passage
    c('east')           # living room
    put_treasures()
    # G-4: narrative says make a separate return trip for the stiletto
    c('west')
    c('west')
    c('up')
    c('take stiletto')
    c('down')
    c('east')
    c('east')
    c('put stiletto in case')
    # Canary / bauble
    c('take canary')
    c('east')           # kitchen
    c('east')           # east of house
    c('north')          # north of house
    c('north')
    c('up')             # up a tree
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
    c('down')           # cellar
    c('north')          # troll room
    c('east')           # ew-passage
    c('north')          # chasm
    c('northeast')      # reservoir south
    c('east')           # dam room
    c('north')          # dam lobby
    c('north')          # maintenance room
    c('push red button')
    c('turn off lamp')
    c('take wrench')
    c('take screwdriver')
    c('push yellow button')
    c('south')          # dam lobby
    c('south')          # dam room
    c('turn bolt with wrench')
    c('wait')
    c('wait')
    c('wait')
    c('west')           # reservoir south
    c('turn on lamp')
    c('north')          # reservoir (now low tide)
    # TODO: 'drop/take all but X' requires parser exclusion support (see memory: parser-all-but.md).
    # Until implemented, this command drops the lamp too and breaks navigation from here onward.
    c('drop all but lamp')
    c('north')          # reservoir north
    c('north')          # atlantis room
    c('take trident')
    c('south')          # reservoir north
    c('south')          # reservoir
    c('take trunk')
    # return to trophy case
    c('south')
    c('southwest')
    c('southwest')
    c('west')
    c('south')
    c('up')
    put_treasures()

    # ------------------------------------------------------------------
    sec('I - The Coal Mines')
    # ------------------------------------------------------------------
    # Get garlic from kitchen
    c('east')           # kitchen
    c('open sack')
    c('take garlic')
    c('west')           # living room
    c('down')           # cellar
    c('north')          # troll room
    c('east')           # ew-passage
    c('north')          # chasm
    c('northeast')      # reservoir south
    c('north')          # reservoir (low tide) — reclaim items dropped here in section H
    c('take all')
    c('north')          # reservoir north
    c('take all')       # pump is here
    # Navigate to bat room via coal mines
    c('north')          # atlantis room
    c('up')
    c('north')
    c('north')
    c('west')
    c('north')
    c('west')
    c('north')          # bat room
    c('take figurine')
    c('east')           # shaft room
    c('put screwdriver in basket')
    c('drop matchbook')     # I-1: narrative: drop to save space; pick up on return trip
    c('drop candles')
    c('north')          # smelly room
    c('down')           # gas room
    c('take bracelet')
    c('east')           # mine-1
    c('northeast')
    c('southeast')
    c('southwest')
    c('down')
    c('down')
    c('west')           # lower shaft / timber room area
    c('drop all but lamp')
    c('east')
    c('south')          # machine room?
    c('take coal')
    c('north')
    c('up')
    c('up')
    c('north')
    c('east')
    c('south')
    c('north')
    c('up')             # shaft room
    c('south')          # smelly room? or back toward basket
    c('take candles')
    c('take matchbook')
    c('light match')
    c('light candles with match')
    c('put candles in basket')
    c('put coal in basket')
    c('lower basket')
    c('north')
    c('down')
    c('east')
    c('northeast')
    c('southeast')
    c('southwest')
    c('down')
    c('west')
    c('drop all')
    c('west')           # lower shaft / basket room
    c('take candles')
    c('take coal')
    c('take screwdriver')
    c('south')          # machine room
    c('open lid')
    c('put coal in machine')
    c('close lid')
    c('turn switch with screwdriver')
    c('open lid')
    c('take diamond')
    c('north')
    c('put candles in basket')      # I-2: narrative: put candle, diamond, screwdriver in basket
    c('put diamond in basket')
    c('put screwdriver in basket')
    c('east')
    c('take all but timber and stiletto')   # I-3: narrative: take all but timber, stiletto
    c('east')
    c('up')
    c('up')
    c('north')
    c('east')
    c('south')
    c('north')
    c('up')
    c('south')
    c('raise basket')
    c('take candles')   # I-2: narrative: take candle and diamond from raised basket
    c('take diamond')
    c('west')
    c('south')
    c('east')
    c('south')
    c('down')
    c('up')
    put_treasures()

    # ------------------------------------------------------------------
    sec('J - Eerie Silence / Loud Room Platinum Bar')
    # ------------------------------------------------------------------
    c('down')
    c('north')
    c('east')
    c('east')
    c('north')
    c('northeast')
    c('east')
    c('turn bolt with wrench')   # close gates → loud room goes quiet (primary method)
    c('south')
    c('down')
    c('take bar')               # J-1: removed echo; bolt-turning is the narrative's primary method
    c('west')
    # get torch from torch room
    c('southeast')
    c('east')
    c('down')
    c('turn off lamp')
    c('drop lamp')
    c('drop candles')           # J-2: narrative: drop lantern AND candles in torch room
    c('take torch')
    c('south')
    c('east')
    c('open coffin')
    c('take sceptre')
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
    put_treasures(keep_names=('SCEPTRE',))        # J-3: keep sceptre for K rainbow

    # ------------------------------------------------------------------
    sec('K - End of the Rainbow')
    # ------------------------------------------------------------------
    c('east')
    c('east')
    c('east')
    c('east')
    c('down')
    c('down')
    c('north')          # aragain falls
    c('wave sceptre')
    c('take pot')
    c('east')
    c('east')
    c('north')
    c('north')
    c('take sword')
    c('northeast')      # sandy beach
    c('take shovel')    # K-1: pick up shovel (required to dig)
    c('northeast')      # sandy cave
    c('dig in sand with shovel')
    c('take scarab')
    # backtrack to trophy case
    c('southwest')
    c('south')
    c('south')
    c('west')
    c('west')
    c('southwest')
    c('up')
    c('up')
    c('northwest')
    c('west')
    c('west')
    c('west')
    put_treasures(keep_names=('TORCH',))          # K-2: keep torch for section L

    # ------------------------------------------------------------------
    sec('L - Row, Row, Row Your Boat')
    # ------------------------------------------------------------------
    c('down')
    c('north')
    c('east')
    c('east')
    c('east')
    c('up')
    c('northwest')
    c('north')
    c('north')
    c('take pump')
    c('south')
    c('south')
    c('east')
    c('down')
    c('take plastic')   # inflatable boat
    c('up')
    c('south')
    c('down')
    c('east')
    c('east')
    c('drop all but pump and torch')    # L-1: narrative: DROP ALL BUT PUMP, TORCH
    c('inflate plastic with pump')
    c('get in boat')
    c('launch')
    c('wait')
    c('wait')
    c('wait')
    c('wait')
    c('take buoy')
    c('east')           # land on east shore
    c('open buoy')
    c('take emerald')
    c('drop buoy')
    c('get out of boat')
    c('deflate boat')
    c('take plastic')
    c('south')
    c('west')
    c('west')
    c('southwest')
    c('up')
    c('up')
    c('northwest')
    c('west')
    c('west')
    c('west')
    c('west')
    put_treasures()    # deposits emerald (and any other treasure carried)
    # L-2: recover items dropped at dam base; ends at White Cliffs Beach
    c('down')
    c('north')
    c('east')
    c('east')
    c('east')
    c('east')
    c('east')
    c('take all but label')

    # ------------------------------------------------------------------
    sec('M - Ramses Coffin')
    # ------------------------------------------------------------------
    # Player is at White Cliffs Beach after L's recovery trip
    c('west')
    c('west')
    c('west')
    c('southeast')
    c('east')
    c('down')
    c('south')
    c('east')           # tiny cave → coffin area
    c('take coffin')
    c('south')
    c('pray')
    c('west')
    c('south')
    c('southeast')
    c('west')
    c('west')
    put_treasures()

    # ------------------------------------------------------------------
    sec('O - Into the Tomb')
    # ------------------------------------------------------------------
    c('read parchment')     # O-1: parchment appears after filling trophy case
    c('east')
    c('east')
    c('southwest')
    c('northwest')
    c('southwest')
    c('in')

    # Final report
    print()
    print('=' * 60)
    print('  FINAL STATE')
    print('=' * 60)
    print(f'Score: {world.score}')
    print(f'Location: {world.here.name if world.here else "unknown"}')
    inv = [o.desc for o in (world.winner.contents if world.winner else [])]
    print(f'Inventory: {inv}')
    tc = world.objects.get('TROPHY-CASE')
    if tc:
        case_items = [o.desc for o in tc.contents]
        print(f'Trophy case: {case_items}')
