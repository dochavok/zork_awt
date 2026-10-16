# Roundabout v2.7 â€” Playtest Transcript (round 2, Sable the Rogue)

Each section is one launch of the game. Commands piped in are listed first, then the raw output. Launches after the first omit the character-creation/restore preamble.

## Launch 1 â€” first launch: version, character, tower
(fresh launch, full output)
Commands: `VERSION` `look` `x mailbox` `open mailbox` `yes` `` `rogue` `Sable` `` `look` `x painting` `x music box` `x desk` `read papers` `x will` `talk to will` `inventory` `save` `quit` `yes`
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> Roundabout: The God-Forsaken Ring — v2.7-roundabout

> West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.

[Press ENTER to continue] Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting of a tavern hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
"I have read destinies in the lines of a man's palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?"
Your choice (warrior/mage/rogue): "A Rogue. Yes." He seems to find this amusing in a quiet way. "You know, I should have seen that. Something about the way you looked at the door when you came in." He shakes his head. "Pay attention to everything. You already know how. Just keep doing it."

You have chosen: Rogue
Hearts: 5  Starting skill: bow

"And your name?" 
Welcome, Sable.

"There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem."

He stands and moves to the window.

"It fell through the roof of a man named Pyronicus. He's holding it in good faith, completely unaware of what it is. He'll give it up without a fight."

He turns back.

"I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."

[Press ENTER to continue] Almost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out. "Here," he says. "Ten Zenni. Don't spend it all on drinks."

"When you're ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.

> Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting of a tavern hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> "One more thing," Will says, rising from his chair. "The ring — I should have told you, it—"
The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You can't see any box here!

> You can't see any desk here!

> You can't see any papers here!

> You can't see any will here!

> You can't see any will here!

> You are empty-handed.
You have 10 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 2 â€” tavern: bar, kitchen, parser
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `look` `x mailbox` `x lynds` `south` `look` `x board` `read board` `talk to may` `` `` `south` `look` `read slate` `x shamus's slate` `x cellar door` `buy torch` `buy dagger` `inventory` `north` `north` `out` `look` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> A mailbox sits near the door, entirely out of place.

> Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.
A woman behind the bar glances up as you come in — shoulder-length red hair, appraisal done in about a second, apparently satisfactory.
"New face," she says, not unkindly. "I'm May. Drinks are two Zenni, food's the same — keeps you on your feet longer than you'd think. Rooms are upstairs if you need to sleep it off properly."
She sets a glass down and leans one hand on the bar.
"If you get stuck on something and want a nudge in the right direction, money talks. Shamus is in the kitchen if you need supplies — he keeps more than recipes back there."
She picks the glass back up and goes back to work. The conversation is over when she decides it is.

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.

> Notices are pinned to the board, newer ones over older:
WANTED: someone to mend the old aqueduct beneath the town. The fountain's been dry for years. Drinks will be cheaper for it. — May
MISSING: a young man, last seen heading toward the dungeon. He may not be himself. If you find him, bring him out. Please.

> Notices are pinned to the board, newer ones over older:
WANTED: someone to mend the old aqueduct beneath the town. The fountain's been dry for years. Drinks will be cheaper for it. — May
MISSING: a young man, last seen heading toward the dungeon. He may not be himself. If you find him, bring him out. Please.

> She picks the glass back up and goes back to work. The conversation is over when she decides it is.

> I beg your pardon?

> I beg your pardon?

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... 2 Zenni
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... 5 Zenni
  Dagger .......... 5 Zenni
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds.

> You can't see any slate here!

> You see nothing special about the cellar door.

> Shamus takes the Zenni and slides the torch across the counter. "Anything else?"

> Shamus takes the Zenni and slides the dagger across the counter. "Anything else?"
Shamus hands it over, then looks at the way you're holding it. "See the knight in the square before you swing that at anything."

> You are carrying:
  Torch
  Dagger
You have 2 Zenni.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Which direction?

> Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 3 â€” parser checks, pipe room, upstairs
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `leave` `exit` `leave tavern` `go out` `south` `south` `x slate` `examine slate` `x shamus' slate` `x the slate` `north` `north` `east` `x jar` `read jar` `listen to jar` `x letters` `x crack` `west` `up` `look` `x window` `down` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Which direction?

> Quit now? (type "no" to save first) [yes/no] 
> Which direction?

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... 2 Zenni
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... 5 Zenni
  Dagger .......... (sold)
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds.

> Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... 2 Zenni
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... 5 Zenni
  Dagger .......... (sold)
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds.

> You can't see any slate here!

> Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... 2 Zenni
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... 5 Zenni
  Dagger .......... (sold)
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> You trace the letters around the base. The silver that once filled them has worn away to a few bright flecks, and without it they're only the shape of words, not the words.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Below, the alley runs narrow and dim between the backs of buildings. In one doorway something that might be a man stands very still, watching the street end.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 4 â€” square and Town Hall
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `look` `x fountain` `x statue` `x seam` `x knight` `north` `look` `west` `look` `x clerk` `talk to clerk` `` `east` `east` `look` `x man` `west` `up` `look` `x cabinet` `open cabinet` `take seal` `x seal` `up` `look` `down` `down` `south` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. Main Street runs off east and west, and to the southwest a gap between buildings leads into an alley.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. Main Street runs off east and west, and to the southwest a gap between buildings leads into an alley.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Dry for years. The basin is cracked at one edge, and the spout is furred with old lime. Whatever fed it came from somewhere underground.

> The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.

> The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.

> A tall man in plain, well-kept armour, a red cross faded on the breast. He wears his sword like a tool he respects. His eyes are calm, and they miss very little.

> Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above. The heavy doors open south onto the square.

> Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above. The heavy doors open south onto the square.

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years. The door back to the foyer is east.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years. The door back to the foyer is east.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> You see nothing special about the clerk.

> The clerk doesn't put down his pen. "If you're here about the charter, the answer is no. It's the town's only copy, and the town isn't in the habit of lending it to strangers." He goes back to his ledger.

> I beg your pardon?

> Town Hall

> Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> You see nothing special about the Councilman Rowan Finch.

> Town Hall

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center. At its far end, a narrower stair turns upward into the tower; the main staircase leads back down to the foyer.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center. At its far end, a narrower stair turns upward into the tower; the main staircase leads back down to the foyer.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> The glass door swings open on a stiff hinge. Among the yellowed charters and a tarnished civic medal sits a wax seal — a disc of old red wax, stamped with the town crest.

> You take the wax seal.

> A disc of old red wax, still soft enough to press. The town crest is stamped into its face.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama. The narrow stair winds back down to the hall below.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama. The narrow stair winds back down to the hall below.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.

> Upper Hall

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 5 â€” Main West, library, alley, mugger
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `look` `north` `look` `x catalogue` `x shelves` `talk to librarian` `` `` `east` `look` `x maps` `west` `south` `southeast` `look` `south` `look` `x crates` `attack mugger with dagger` `attack mugger with dagger` `attack mugger with dagger` `diagnose` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. Main Street runs off east and west, and to the southwest a gap between buildings leads into an alley.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West
Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley. The town square is back to the east.

> Main West
Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley. The town square is back to the east.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
At the east end, one of the gaps between the shelves runs back further than the building should allow. The red doors to the street are south.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
At the east end, one of the gaps between the shelves runs back further than the building should allow. The red doors to the street are south.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Hundreds of small drawers, each labelled in faded ink. The drawer marked V sits a little open, as if someone has been in it more than most.

> Floor to ceiling, packed in columns. The gaps between them are narrow, and one at the east end runs back further than it should.

> She sets down what she's holding and folds her hands on the desk. Her voice arrives in pieces — tones and rhythms that don't quite match, stitched together at the seams.
"I have been waiting for someone to come asking."
She pulls a thin ledger from under the desk without looking for it.
"'The Veil of the Arcane — I need access to whatever you have.' That's what he said. First thing. Didn't introduce himself. I didn't ask."
She opens the ledger to a marked page.
"He was here for — weeks. Every day. 'Have you found anything else? Anything older?' He was very — 'I think I've found something. I think I know where it is.'"
She closes the ledger.
"And then he stopped coming. I checked the application. There's a date. There's no — 'I'll be back by —' there's no return date. There never was."
She looks at you steadily.
"'The lower passages. That's where it will be. That's where everything that old ends up.'"
She sets the ledger aside.

> I beg your pardon?

> I beg your pardon?

> The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> You can't see any maps here!

> Library — Main Hall

> Main West
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> The Alley
The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. At the north end the alley splits — northeast back to the town square, northwest to Main West.
The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.

> The Alley
The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. At the north end the alley splits — northeast back to the town square, northwest to Main West.
The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.

> The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. The only way out is back north, which is worth remembering. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
Something hits you from behind. The alley tilts, then goes away.
You come to in the Back Alley, lighter in the pocket and sore in the head. Mugged — and whoever did it is still out there.

> The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. The only way out is back north, which is worth remembering. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.

> You can't see any crates here!

> You can't see any mugger here!

> You can't see any mugger here!

> You can't see any mugger here!

> You have 4 of 5 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 6 â€” to the volcano for the ring
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `inventory` `north` `northeast` `east` `look` `east` `look` `south` `look` `x structures` `light torch` `down` `look` `talk to pyronicus` `` `` `` `x ring` `inventory` `x forge` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. The only way out is back north, which is worth remembering. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.

> You are carrying:
  Torch
  Dagger
  Wax seal
You have 13 Zenni.

> The Alley
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East
Main Street ends here, or nearly does. The buildings thin out toward the east — a few shuttered fronts, a sign that's lost its lettering, the church standing apart to the south as though it chose its distance deliberately. The wasteland begins to the east, where the cobblestones stop. Back to the west, the street opens into the town square.

> Main East
Main Street ends here, or nearly does. The buildings thin out toward the east — a few shuttered fronts, a sign that's lost its lettering, the church standing apart to the south as though it chose its distance deliberately. The wasteland begins to the east, where the cobblestones stop. Back to the west, the street opens into the town square.

> Roundabout Wasteland
The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently.
The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly.
The cause is a matter of some local sensitivity. The prevailing theory among residents involves adventurers, which explains why no one wants to discuss it in detail.
To the south, a volcano rises against the sky — large, dark, and entirely convincing. Eastward, a rutted road leaves the wreckage behind and heads for the smell of salt; the town is back to the west.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Roundabout Wasteland
The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently.
The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly.
The cause is a matter of some local sensitivity. The prevailing theory among residents involves adventurers, which explains why no one wants to discuss it in detail.
To the south, a volcano rises against the sky — large, dark, and entirely convincing. Eastward, a rutted road leaves the wreckage behind and heads for the smell of salt; the town is back to the west.

> You hear music — a familiar melody. You have reached level 2!
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> You can't see any structures here!

> It's already lit.

> You can't go that way.

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> You can't see any pyronicus here!

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> You can't see any ring here!

> You are carrying:
  Torch
  Dagger
  Wax seal
You have 17 Zenni.

> You can't see any forge here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 7 â€” volcano: looking for a way in
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x volcano` `x rock` `x smoke` `x heat` `search` `climb volcano` `north` `west` `south` `look` `x dial` `x altar` `x pews` `x door` `north` `east` `south` `look` `save` `quit` `yes`
```
> Restored.
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> You can't see any volcano here!

> You can't see any rock here!

> You can't see any smoke here!

> You can't see any heat here!

> You search carefully but find nothing unusual.

> You can't see any volcano here!

> Roundabout Wasteland

> Main East

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
To the east, through a low archway, a stone altar stands in a space of its own, something brass catching the light at its face. The street door is north; a side door to the south lets out into the graveyard.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
To the east, through a low archway, a stone altar stands in a space of its own, something brass catching the light at its face. The street door is north; a side door to the south lets out into the graveyard.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> The altar is through the archway to the east.

> The altar is through the archway to the east.

> You can't see any pews here!

> You see nothing special about the narrow door.

> Main East

> Roundabout Wasteland

> The Volcano

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 8 â€” volcano: re-entering
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `south` `look` `north` `south` `look` `x ground` `x slope` `x flows` `listen` `wait` `wait` `look` `save` `quit` `yes`
```
> Restored.
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> Roundabout Wasteland

> The Volcano

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> Roundabout Wasteland

> The Volcano

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> You can't see any ground here!

> You can't see any slope here!

> You can't see any flows here!

> You hear nothing out of the ordinary.

> Time passes...

> Time passes...

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 9 â€” knight and May tip about the volcano
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `west` `west` `talk to knight` `` `` `south` `south` `tip may 2` `save` `quit` `yes`
```
> Restored.
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> The Knight stands at ease in the square, watching the town go about its business. When he notices you, he turns fully to face you — unhurried, attentive. "You're looking at me like someone who wants to learn something," he says. "I teach one thing. Come find me when you're ready to show me what you already know."

> I beg your pardon?

> I beg your pardon?

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.
"The Keeper of the Faiths has gone missing. No one's seen him in some time."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 10 â€” west: archery range and encampment
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `score` `north` `north` `west` `west` `look` `x targets` `talk to archer` `west` `look` `north` `look` `talk to haalvar` `` `` `the sea` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.

> Score: 0
Level 2 (21 XP)
Zenni: 15
0 treasures on display.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
The road back to town runs east. To the north, a footpath slips away through the reeds toward lower, wetter ground.
Raznak stands at the near end of the range, watching the targets.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.
An arrow hisses past, close enough to hear the fletching.

> Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
The road back to town runs east. To the north, a footpath slips away through the reeds toward lower, wetter ground.
Raznak stands at the near end of the range, watching the targets.

> You can't see any targets here!

> Raznak eyes you the way he'd eye an arrow with a bad fletching — not hostile, just certain you're not ready.
"You want something from me, go talk to the encampment first. West of here. When they know you, come back."
He turns away. The conversation is over.

> Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit; the archery range is back to the east.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.
"You want something from us. They always want something. Prove yourself. Talk to Haalvar — north. If you can satisfy him, come back."

> Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit; the archery range is back to the east.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing. The door flap opens south onto the encampment.
Haalvar lounges beside the stone, looking pleased with himself.
Haalvar says: "I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"

> Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing. The door flap opens south onto the encampment.
Haalvar lounges beside the stone, looking pleased with himself.

> Haalvar says: "I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"

> I beg your pardon?

> I beg your pardon?

> I don't know the word "sea".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 11 â€” Haalvar's riddle, circle
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `answer sea` `say sea` `sea` `south` `talk to ivanaar` `` `` `x banner` `read banner` `south` `look` `x stones` `x symbol` `talk to child` `` `activate earth stone` `activate air stone` `activate fire stone` `activate water stone` `activate heart stone` `look` `score` `save` `quit` `yes`
```
> Restored.
Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing. The door flap opens south onto the encampment.
Haalvar lounges beside the stone, looking pleased with himself.

> The stone glows. Haalvar: "The stone is satisfied. I am also satisfied, which happens less often. Go south — there is a circle there that will want your attention next."

> I don't know the word "say".

> I don't know the word "sea".

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> "Haalvar speaks well of you. That's not nothing. The circle is south."

> I beg your pardon?

> I beg your pardon?

> Four runes are stitched along the banner, left to right: Earth, Air, Fire, Water.

> There's nothing written on the banner.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean. The path back to the encampment runs north.
A child stands at the edge of the circle, watching you without a word.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean. The path back to the encampment runs north.
A child stands at the edge of the circle, watching you without a word.

> You can't see any stones here!

> You can't see any symbol here!

> The child says nothing.

> I beg your pardon?

> The Earth stone hums and lights from within.

> The Air stone hums and lights from within.

> The Fire stone hums and lights from within.

> The Water stone hums and lights from within.

> The Heart stone hums and lights from within.
The fifth stone lights, and all five hum together for a moment. The child looks at you, then points back toward the encampment.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean. The path back to the encampment runs north.
A child stands at the edge of the circle, watching you without a word.

> Score: 0
Level 2 (25 XP)
Zenni: 18
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 12 â€” Ivanaar, Aylora, Thornbrew
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `talk to ivanaar` `` `` `west` `look` `talk to aylora` `` `` `drink` `east` `talk to ivanaar` `` `` `west` `take aylora` `east` `talk to ivanaar` `` `` `inventory` `score` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean. The path back to the encampment runs north.
A child stands at the edge of the circle, watching you without a word.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> "Two down. The fire pit is west. Don't embarrass yourself."

> I beg your pardon?

> I beg your pardon?

> The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments. The longhouses are back to the east.
Aylora sits by the fire, a cup in hand.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments. The longhouses are back to the east.
Aylora sits by the fire, a cup in hand.

> Aylora sets two cups on the bench and fills them from the barrel. "Thornbrew," she says. "Five cups. Last one standing." She pushes one toward you.

> I beg your pardon?

> I beg your pardon?

> Aylora drains hers without blinking. Yours fights back.
Aylora drains hers without blinking. Yours fights back.
Aylora drains hers without blinking. Yours fights back.
You pass out.
Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
A nearby Viking: "Ha! Aylora strikes again. Don't feel bad — she's been doing this since she could reach the cup."

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> You can't see any ivanaar here!

> I beg your pardon?

> I beg your pardon?

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> You can't see any aylora here!

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> You can't see any ivanaar here!

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
You have 21 Zenni.

> Score: 0
Level 2 (26 XP)
Zenni: 21
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 13 â€” north to the pond and bog
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `north` `look` `x bottle` `north` `look` `take shard` `take thyme` `north` `look` `x log` `search log` `take key` `take metal` `east` `look` `take grey stone` `south` `look` `x gravestone` `read gravestone` `east` `look` `save` `quit` `yes`
```
> Restored.
Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
The road back to town runs east. To the north, a footpath slips away through the reeds toward lower, wetter ground.
Raznak stands at the near end of the range, watching the targets.

> Main West

> Library — Main Hall

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
At the east end, one of the gaps between the shelves runs back further than the building should allow. The red doors to the street are south.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> You can't see any bottle here!

> You can't go that way.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
At the east end, one of the gaps between the shelves runs back further than the building should allow. The red doors to the street are south.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> You can't see any shard here!

> You can't see any thyme here!

> You can't go that way.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
At the east end, one of the gaps between the shelves runs back further than the building should allow. The red doors to the street are south.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> You can't see any log here!

> You can't see any log here!

> You can't see any key here!

> You can't see any metal here!

> The Stacks

> The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> You can't see any stone here!

> You can't go that way.

> The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> You can't see any gravestone here!

> You can't see any gravestone here!

> You can't go that way.

> The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 14 â€” north to the pond and bog (retry)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `south` `west` `north` `look` `x bottle` `north` `look` `take shard` `take thyme` `north` `look` `x log` `search log` `take key` `take metal` `east` `look` `take grey stone` `south` `look` `x gravestone` `read gravestone` `east` `look` `save` `quit` `yes`
```
> Restored.
The Stacks
The passage from the Main Hall, back to the west, opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Library — Main Hall

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path to the south and the bog to the north, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path to the south and the bog to the north, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> A tiny ship in full sail, sealed in green glass. Someone spent a long time on the rigging. The name on the hull is too small to read — almost.

> The Bog of Eternal Stench
A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave. The pond lies back to the south.
Half-sunk in the mud at the edge of the reeds, a curved shard of pale ceramic catches what light there is.
A clump of thyme grows on a dry hummock among the reeds, improbably green.

> The Bog of Eternal Stench
A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave. The pond lies back to the south.
Half-sunk in the mud at the edge of the reeds, a curved shard of pale ceramic catches what light there is.
A clump of thyme grows on a dry hummock among the reeds, improbably green.

> You take the muddy bowl piece.

> You take the bog thyme.

> The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds. Something small and metal glints inside it.

> The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds. Something small and metal glints inside it.

> Rotten through the middle and hollow end to end. Wedged inside: a small brass key.

> You search carefully but find nothing unusual.

> You take the music box key.

> You can't see any metal here!

> The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.

> The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.

> You can't see any stone here!

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
Half-sunk in the mud at the water's edge, a slab of dressed stone lies face-down — too square to be anything the bog made. Someone dumped it here.
Off to the east, the brush isn't quite as dense as it should be. Behind it, a path — narrow, deliberate — leads to something low and round. A yurt, improbably dry.

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> There's nothing written on the gravestone.

> Something in the air near the door shifts as you approach. Not hostile. More like a house that knows you haven't been introduced yet.

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 15 â€” back to town: music box, thyme
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `west` `south` `south` `south` `east` `east` `south` `open mailbox` `look` `unlock music box with key` `open music box` `take scroll` `read scroll` `x painting` `south` `south` `give thyme to shamus` `` `score` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> The Bog of Eternal Stench
A grey stone sits at the water's edge, one face worn flat.

> The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench

> Roundabout Pond
You see a bottle at the bottom of the pond.

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting of a tavern hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
You notice a door to the north you hadn't seen before.

> Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting of a tavern hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
A door in the north wall stands where you'd have sworn there wasn't one.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> The key turns with a soft click. The lid lifts, and a short melody plays — a few bright notes, a little out of tune, then nothing. Inside, folded small, is a scroll.

> A small lacquered music box, its lid open.

> You take the Light scroll.

> Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, reading silently for a moment. Then he reads it aloud — not to you, exactly, more as if the words need to be heard in the right kind of room. When he finishes, you understand it. You're not sure how. "Keep that," he says, nodding at the space where the scroll was. It's gone. "The knowing, I mean."
[Light spell learned.]
You hear music — a familiar melody. You have reached level 3!

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus takes the thyme, crushes a leaf between his fingers and breathes it in. "That's the stuff." He sets it by the stove. "Now a pot that holds water, and we're in business."

> I beg your pardon?

> Score: 0
Level 3 (45 XP)
Zenni: 26
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 16 â€” volcano at level 3
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `north` `east` `east` `south` `look` `down` `look` `talk to pyronicus` `` `` `` `x ring` `inventory` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see. The wasteland is back to the north.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right. The uneven stairs climb back up into it.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right. The uneven stairs climb back up into it.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus sets down his work and regards you with calm, unhurried eyes. "Will's errand," he says. "Yes."
He moves to a workbench and returns with the ring, placing it in your hand with the care of someone returning something that was never theirs.
"It fell through my ceiling," he says. "Rings don't do that by accident."
He pauses. "Will told you what you need to know, I assume."
He goes back to what he was doing. The conversation, apparently, is over.

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> A plain dark ring.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
You have 26 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 17 â€” ring to Will
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `up` `north` `west` `west` `south` `open mailbox` `give ring to will` `` `` `` `` `inventory` `x ring` `north` `look` `south` `x painting` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right. The uneven stairs climb back up into it.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> The Volcano

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> Will sets down his pen when he sees the ring. He doesn't reach for it.
"Good," he says. "Sit down."
He doesn't wait to see if you do.
"The ring can't be destroyed. I want to be clear about that — not by force, not by fire, not by anything one person or one faith could bring to bear. What's inside it is older than the methods we have for ending things."
He moves to the window.
"But three faiths together — three distinct sources of power, each contributing something the others cannot — that's another matter. There is a Church in Roundabout. The Church of All. You'll find an altar there with a dial. Seven religions. Three of them are what you need."
He turns back.
"I won't tell you which three. You'll know them when you find them. The things they ask of you will make it obvious."
He picks up his pen.
"When it's done, bring it back."

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
You have 26 Zenni.

> A plain dark ring.

> You push open the bedroom door and step inside.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The door back to the tower is south.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.

> Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The door back to the tower is south.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.

> Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 18 â€” Lynds at level 3
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x lynds` `talk to lynds` `` `` `` `diagnose` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Lynds looks at you the way a person looks at something they're about to do that they've done many times before. He sets his drink down and puts his elbow on the table.
"Go on then."
Lynds wins without apparent effort. He picks his drink back up. "Not bad." He means it as a compliment. "Come back whenever."

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> You have 5 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 19 â€” Thornbrew rematch
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `west` `west` `west` `west` `talk to aylora` `` `` `drink` `take aylora` `east` `talk to ivanaar` `` `` `inventory` `score` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Fire Pit
Aylora sits by the fire, a cup in hand.

> Aylora sets two cups on the bench and fills them from the barrel. "Thornbrew," she says. "Five cups. Last one standing." She pushes one toward you.

> I beg your pardon?

> I beg your pardon?

> You drain the cup. Aylora matches you, but slower.
Aylora drains hers without blinking. Yours fights back.
You drain the cup. Aylora matches you, but slower.
You drain the cup. Aylora matches you, but slower.
Aylora sets down her cup with great care, looks at it, and slides gently off the bench. Aylora passes out.
A nearby Viking stares at her, then at you. "Ivanaar won't believe that unless he sees it."

> You get her under the arms and start to drag.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Ivanaar looks at Aylora, then at you, then at Aylora again. He says nothing for a long moment.
"...Thornbrew?" he finally asks.
You nod. He laughs — once, short, like it surprised him too. Then he straightens, and the laugh is gone, and something older takes its place.
"Will Passion sent you. He asked me to build something that would tell him whether you were worth trusting with what comes next. He didn't tell me what comes next."
He moves to the longhouse and returns holding a length of dark metal — dense, rune-carved, warm to the touch even in the open air. He holds it with both hands.
"This is Brotherhood metal. It has been kept since before this encampment. It would make a fine blade in the right hands — a blacksmith who knows what he is looking at could tell you more."
He places it in your hands. "I hope Will is right about you."
"One more thing. There are three stones out in the world — Brotherhood metal, rune-carved. They've been scattered a long time. If you come across them, bring them to me."
He glances back once. "I'll make it worth your time."
Ivanaar returns to his fire.
[Runed Metal added to inventory.]

> Ivanaar returns to his fire.

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Runed metal
You have 31 Zenni.

> Score: 0
Level 3 (62 XP)
Zenni: 31
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 20 â€” Raznak, Pale Blade
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `talk to raznak` `` `` `east` `east` `east` `east` `south` `down` `give runed metal to pyronicus` `` `` `` `inventory` `up` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit; the archery range is back to the east.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Aylora is slumped on the bench, snoring.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Raznak watches you cross the range. He doesn't say anything for a moment. His eyes go to your hands. Then your stance. Then back to your hands.
"You've done this before."
It isn't a question. He disappears into the longhouse and returns with a bow — plain, well-maintained, strung and ready.
"Don't embarrass it," he says, and hands it over.
[Bow added to inventory.]

> I beg your pardon?

> I beg your pardon?

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> The Volcano

> Pyronicus's Forge
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus turns the metal over in his hands without speaking. He runs a thumb along the runes. Then he sets it on the forge.
"Brotherhood metal," he says. "I haven't seen this in some time." He picks up his hammer. "You know what it's for."
He doesn't phrase it as a question.
The forge does the rest quickly — the metal accepts the heat the way it has been waiting to, and Pyronicus works it with the focused economy of someone who has done this before and expects to do it again. When he's done, he holds it up. The blade is pale, almost white, and thin in the way of something that doesn't need to be heavy to do what it does.
He holds it out, pommel first.
"It will go willingly," he says. "When the time comes."
He goes back to his work.
[Runed Metal removed from inventory. The Pale Blade added to inventory.]

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
You have 31 Zenni.

> The Volcano

> Roundabout Wasteland

> Beach Road
The rutted track out of the wasteland firms up here into something a cart could use, and then can't decide where to go. South, it runs down toward the beach and the smell of salt. North, it climbs toward a great old oak at the edge of the forest. The wasteland is back to the west.

> Beach Road
The rutted track out of the wasteland firms up here into something a cart could use, and then can't decide where to go. South, it runs down toward the beach and the smell of salt. North, it climbs toward a great old oak at the edge of the forest. The wasteland is back to the west.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 21 â€” beach, docks, lighthouse
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `x lighthouse` `east` `look` `take rope` `look` `west` `northeast` `look` `take scroll` `read scroll` `x stone` `x stairs` `x desk` `up` `look` `x paperweight` `down` `save` `quit` `yes`
```
> Restored.
Beach Road
The rutted track out of the wasteland firms up here into something a cart could use, and then can't decide where to go. South, it runs down toward the beach and the smell of salt. North, it climbs toward a great old oak at the edge of the forest. The wasteland is back to the west.

> Roundabout Beach
Roundabout Beach opens out below the town — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull. The lighthouse stands to the northeast on a finger of rock, its lamp turning slowly. Beach Road runs back north toward the trees. It smells like freedom, or at least like salt.

> Roundabout Beach
Roundabout Beach opens out below the town — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull. The lighthouse stands to the northeast on a finger of rock, its lamp turning slowly. Beach Road runs back north toward the trees. It smells like freedom, or at least like salt.

> Why not go in and look around?

> The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. The Pie Rat Ship sits in her berth to the east like she owns it, which she more or less does — the only vessel worth the name in Roundabout's harbor. The smell is fish and brine and honest work. The beach is back to the west.
A coil of rope sits loose on a bollard.

> The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. The Pie Rat Ship sits in her berth to the east like she owns it, which she more or less does — the only vessel worth the name in Roundabout's harbor. The smell is fish and brine and honest work. The beach is back to the west.
A coil of rope sits loose on a bollard.

> You take the coil of rope.

> The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. The Pie Rat Ship sits in her berth to the east like she owns it, which she more or less does — the only vessel worth the name in Roundabout's harbor. The smell is fish and brine and honest work. The beach is back to the west.

> Roundabout Beach
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp, a chain hung across its foot. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back. The door out to the beach is southwest.
A scroll lies on the desk, weighted at one corner with a smooth stone.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp, a chain hung across its foot. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back. The door out to the beach is southwest.
A scroll lies on the desk, weighted at one corner with a smooth stone.

> You take the Unbind Undead scroll.

> The words are legible. The meaning is not. Whatever is written here was meant for someone with a different kind of mind — or a different kind of training. Will Passion, in his tower, has been known to translate this sort of thing for people like you.

> A smooth grey stone from the beach, worn flat by the sea. Someone picked it out for exactly this job.

> The stairs lead up.

> A plain desk under the window, its top worn pale where an elbow rests. The papers on it are a keeper's log, tide tables and lamp hours, all in the same careful hand.

> A tag on the chain reads: KEEPER ONLY. Whoever the keeper is, they'd clearly rather you didn't.

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp, a chain hung across its foot. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back. The door out to the beach is southwest.
A smooth stone sits on the desk where the scroll was.

> A smooth grey stone from the beach, worn flat by the sea. Someone picked it out for exactly this job.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 22 â€” Old Oak, kite, forest
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `southwest` `north` `north` `look` `x oak` `talk to child` `climb oak` `take kite` `down` `take stone` `give kite to child` `look` `north` `look` `x shrine` `x pedestal` `take shard` `look` `save` `quit` `yes`
```
> Restored.
The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp, a chain hung across its foot. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back. The door out to the beach is southwest.
A smooth stone sits on the desk where the scroll was.

> Roundabout Beach

> Beach Road

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. A kite is tangled in its upper branches. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. A kite is tangled in its upper branches. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.

> You see nothing special about the oak.

> "It's stuck," the child says, pointing up. As if you might not have noticed.

> You haul yourself up through the branches and work the kite loose. Something comes free with it — a small flat stone on a cord, tangled in the line. It drops into the grass below.

> You already have the kite.

> You can't go that way.

> You take the flat rune stone.

> The child takes the kite in both hands, inspects it for damage, finds none worth mentioning, and runs off to try again.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. Back to the south, the trees thin out toward the old oak.
The mine entrance sits among the roots and undergrowth, a dark mouth leading down into the ground — easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. Back to the south, the trees thin out toward the old oak.
The mine entrance sits among the roots and undergrowth, a dark mouth leading down into the ground — easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> The shrine's pedestal is worn smooth on top, a shallow ring where something has rested for a long time. The symbol on it is a sprouting seed inside a circle of leaves.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.

> The shrine's pedestal is worn smooth on top, a shallow ring where something has rested for a long time. The symbol on it is a sprouting seed inside a circle of leaves.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.

> You take the large bowl piece.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. Back to the south, the trees thin out toward the old oak.
The mine entrance sits among the roots and undergrowth, a dark mouth leading down into the ground — easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 23 â€” into the mine
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `enter mine` `look` `x torch` `north` `look` `take pickaxe` `south` `down` `look` `north` `look` `take disguise` `south` `south` `look` `take striker` `east` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. Back to the south, the trees thin out toward the old oak.
The mine entrance sits among the roots and undergrowth, a dark mouth leading down into the ground — easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY. Someone has added, in different handwriting: THIS MEANS YOU. In another hand: ME? And beneath that, in the first handwriting: NO, NOT YOU SLOTH. Past the sign, the shaft drops down into the dark; the forest is back up the slope.

> Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY. Someone has added, in different handwriting: THIS MEANS YOU. In another hand: ME? And beneath that, in the first handwriting: NO, NOT YOU SLOTH. Past the sign, the shaft drops down into the dark; the forest is back up the slope.

> A lit torch.

> You can't go that way.

> Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY. Someone has added, in different handwriting: THIS MEANS YOU. In another hand: ME? And beneath that, in the first handwriting: NO, NOT YOU SLOTH. Past the sign, the shaft drops down into the dark; the forest is back up the slope.

> You can't see any pickaxe here!

> You can't go that way.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals — functional, not decorative. The smell of rock dust and old torchsmoke is thick here. A side room opens to the south, and the shaft itself goes on down into the workings below.
Daylight shows faintly back up the way to the entrance.
A pickaxe leans against the wall.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals — functional, not decorative. The smell of rock dust and old torchsmoke is thick here. A side room opens to the south, and the shaft itself goes on down into the workings below.
Daylight shows faintly back up the way to the entrance.
A pickaxe leans against the wall.

> You can't go that way.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals — functional, not decorative. The smell of rock dust and old torchsmoke is thick here. A side room opens to the south, and the shaft itself goes on down into the workings below.
Daylight shows faintly back up the way to the entrance.
A pickaxe leans against the wall.

> You can't see any disguise here!

> Assay Room
A side room off the main shaft, which lies back to the north, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.
A flint and steel striker lies on the workbench among the crucibles.
Looking closer, the gap in the far wall goes further back than it should — a rough passage, just wide enough to squeeze through, running east into the dark.

> You can't go that way.

> Assay Room
A side room off the main shaft, which lies back to the north, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.
A flint and steel striker lies on the workbench among the crucibles.

> You take the flint and steel.

> Hidden Secondary Entrance
The gap in the assay room wall, to the west, opens into a rough passage that runs east toward the tunnel network below. It does not appear on any official plan of the mine. It would not.
The torch catches the dark and pushes it back. Good thinking, getting one of these.

> Hidden Secondary Entrance
The gap in the assay room wall, to the west, opens into a rough passage that runs east toward the tunnel network below. It does not appear on any official plan of the mine. It would not.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 24 â€” pickaxe, tunnels
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `north` `take pickaxe` `south` `east` `east` `look` `down` `look` `east` `look` `south` `look` `south` `look` `save` `quit` `yes`
```
> Restored.
Hidden Secondary Entrance
The gap in the assay room wall, to the west, opens into a rough passage that runs east toward the tunnel network below. It does not appear on any official plan of the mine. It would not.

> Assay Room
A side room off the main shaft, which lies back to the north, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.

> Main Shaft
A pickaxe leans against the wall.

> You take the pickaxe.

> Assay Room

> Hidden Secondary Entrance

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine. Southward, the passage widens again.

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine. Southward, the passage widens again.

> You can't go that way.

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine. Southward, the passage widens again.

> You can't go that way.

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine. Southward, the passage widens again.

> The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling. The passage runs north toward older, narrower stone, and south to where the tunnels meet.

> The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling. The passage runs north toward older, narrower stone, and south to where the tunnels meet.

> The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways: east toward the cellar, north toward the old mine workings, and south, where the floor drops away toward a ravine. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways: east toward the cellar, north toward the old mine workings, and south, where the floor drops away toward a ravine. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 25 â€” Bone Passage, Charnel Walk, Toll Bridge
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `look` `x door` `south` `look` `x footprints` `north` `west` `south` `look` `x boggart` `talk to boggart` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways: east toward the cellar, north toward the old mine workings, and south, where the floor drops away toward a ravine. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south, and west toward the junction. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south, and west toward the junction. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> The wood is dark and swollen, and a thin seep of cold water spreads across the floor beneath it.

> Charnel Walk
The passage ends at a low arch, and beyond it worn steps climb up into the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels running back to the north.

> Charnel Walk
The passage ends at a low arch, and beyond it worn steps climb up into the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels running back to the north.

> You can't see any footprints here!

> The Bone Passage

> The Junction

> The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.
Carved into the bridge's keystone, half worn away: the town's crest, and beneath it, PUBLIC PROPERTY.

> The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> You see nothing special about the Boggart.

> "Toll," the Boggart says, holding out a hand without looking at it. "Two hundred. Each way. Non-negotiable." He doesn't say two hundred of what, and you get the impression he's never had to.

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Unbind Undead scroll
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
You have 40 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 26 â€” ring vs the Boggart
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `south` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> 'Toll,' the Boggart says, holding out a hand to the exact patch of air you're standing in. 'Don't think I can't see you.' He doesn't move. Neither, it turns out, can you.

> Plain dark ring removed.

> The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 27 â€” up through the crypt to town
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `east` `south` `up` `look` `x footprints` `x passage` `x alcoves` `up` `look` `x door` `out` `look` `north` `look` `north` `west` `south` `open mailbox` `give scroll to will` `` `` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> The Junction

> The Bone Passage

> Charnel Walk

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage slopes down into darkness — older than the crypt itself, by the look of the stonework. Steps climb up to the mausoleum.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage slopes down into darkness — older than the crypt itself, by the look of the stonework. Steps climb up to the mausoleum.

> You can't see any footprints here!

> You can't see any passage here!

> You can't see any alcoves here!

> You hear music — a familiar melody. You have reached level 4!
The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below. The graveyard lies back to the north.

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below. The graveyard lies back to the north.

> You can't see any door here!

> Which direction?

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below. The graveyard lies back to the north.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
The air is still in a way that has nothing to do with wind.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
The air is still in a way that has nothing to do with wind.
The torch burns a little lower than it did.

> Church of All

> The door is locked.

> Graveyard

> You can't see any mailbox here!

> You can't see any will here!

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 28 â€” to Will with the scroll
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `west` `south` `open mailbox` `give scroll to will` `` `` `x painting` `talk to lynds` `` `diagnose` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
The air is still in a way that has nothing to do with wind.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, reading silently for a moment. Then he reads it aloud — not to you, exactly, more as if the words need to be heard in the right kind of room. When he finishes, you understand it. You're not sure how. "Keep that," he says, nodding at the space where the scroll was. It's gone. "The knowing, I mean."
[Unbind Undead spell learned.]

> I beg your pardon?

> I beg your pardon?

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Lynds looks at you the way a person looks at something they're about to do that they've done many times before. He sets his drink down and puts his elbow on the table.
"Go on then."
Lynds holds still for a moment after his hand goes down. Then he laughs — short, surprised, genuine.
"Huh."
He studies you for a moment, then reaches into his shirt and pulls out a necklace — a simple cord, a clay charm worn smooth. He sets it on the table between you.
"My grandmother made that. Said it kept her heart going longer than it had any right to. I don't know if that's true but I've never had reason to doubt it. You earned it."
He picks up his drink.
"Come find us in the bog sometime. Ask for the Dankhaus. Tell them Lynds sent you."
[Heart Necklace added to inventory.]

> I beg your pardon?

> You have 5 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 29 â€” necklace, to the Dankhaus
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x necklace` `wear necklace` `diagnose` `north` `west` `west` `north` `north` `north` `east` `take grey stone` `south` `east` `look` `tell litlock lynds sent me` `talk to litlock` `` `` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor.
To the east, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The street door opens north onto the square.
The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way.
Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> A simple cord with a clay charm, worn smooth.

> You put on the heart necklace.
The torch is noticeably dimmer now. It won't last forever.

> You have 6 of 7 hearts.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Roundabout Pond
You see a bottle at the bottom of the pond.

> The Bog of Eternal Stench

> The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench
A grey stone sits at the water's edge, one face worn flat.

> You take the grey rune stone.

> The Bog of Eternal Stench
A gravestone lies face-down in the mud.

> Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.
Litlock looks up from whatever he's doing with the particular alertness of someone who has been waiting for company without admitting it to himself. He takes you in. Then he grins — wide, genuine, the kind that arrives before the person decides to smile.
"Right," he says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.

> You can't see any me here!

> "Right," Litlock says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> I beg your pardon?

> I beg your pardon?
The torch gutters. You don't have much time left on it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 30 â€” Litlock's joke
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `talk to litlock` `1` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.

> "Right," Litlock says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> You clear your throat. "I have a joke."
Litlock leans back. "Everyone has a joke. Let's see if yours is different."
  1. A pun
  2. An absurd observation

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 31 â€” Litlock's joke, continued
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `talk to litlock` `1` `2` `1` `` `look` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.

> "Right," Litlock says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> You clear your throat. "I have a joke."
Litlock leans back. "Everyone has a joke. Let's see if yours is different."
  1. A pun
  2. An absurd observation

> "You know," you say, "I've been thinking about the bog. Specifically about the smell. And I think the smell isn't the bog at all — I think the bog smells fine and it's everything else that's wrong."
Litlock blinks. Then something shifts in his expression — not quite a laugh yet, but its immediate predecessor.
"Go on," he says.
  1. Push further
  2. Explain it

> "In fact," you continue, with complete conviction, "I think the bog has been unfairly maligned for years, and someone should apologize to it."
That does it.
Litlock laughs — fully, completely, the kind of laugh that takes over a person entirely. He laughs until he has to put something down. He laughs until Aurix appears in the doorway to see what's happening and then disappears again.
When he finally stops, he wipes his eyes, looks at you with something that might be respect, and reaches over and bonks you firmly on the top of the head with two knuckles.
"There," he says. "You'll see things a bit differently now. Don't ask me to explain it."
He picks up whatever he put down and goes back to it, still smiling.

> I beg your pardon?

> Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 32 â€” graveyard after Litlock
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `north` `west` `south` `south` `south` `east` `east` `east` `south` `south` `east` `look` `x sign` `x booth` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
The common room is large, and so is the fireplace, burning steadily against the far wall. Chairs, a table, shelves. The kind of room that works because the people in it make it work. Doors lead off it to the north, south and east, and the front door opens west onto the bog.
Litlock fills whatever room he's in without trying to, and he fills this one from a chair near the fire. He looks up.

> The Bog of Eternal Stench
A gravestone lies face-down in the mud.

> The Bog of Eternal Stench

> The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench

> Roundabout Pond
You see a bottle at the bottom of the pond.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Main West
The torch gutters and goes out.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.
Something in the walls makes a sound as you cross the threshold — not quite a creak, not quite a welcome.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> The ticket window is cracked but intact. A small wooden sign on the ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. The booth is empty. Whoever collected the tickets isn't collecting anymore.

> The ticket window is cracked but intact. A small wooden sign on the ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. The booth is empty. Whoever collected the tickets isn't collecting anymore.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 33 â€” mirror building, without the ring
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `x mirror` `x reflection` `x frame` `south` `look` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> You can't see any mirror here!

> You can't see any reflection here!

> You can't see any frame here!

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 34 â€” ring through the mirrors to the ghost
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `south` `x mirror` `south` `x mirror` `south` `cast unbind undead` `take watch` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> The Rejection Mirror
A narrow room with a single tall mirror filling the far wall, its frame carved with grinning faces. The glass is old and silvered at the edges. The doorway to the south is beside it — you'd have to pass right in front of it to get there. The entrance hall is back to the north.

> A tall mirror in a frame of grinning faces. It shows the room, the doorway, the faces. It doesn't show you.

> The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south. The first mirror's room is back to the north.
Something clicks behind the frame. A bolt cracks out of the dark and catches you before you can move.

> Larger than the last, the glass rippled with age. The ripples move across an empty room.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.
A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> "Thank you. I can rest now."
The grey figure thins until the mirrors have nothing left to repeat. Something falls where he stood and lands with a small metallic click — a pocket watch.

> You take the pocket watch.
The ring is warm. You hadn't noticed until just now. You're not sure when it started.

> Plain dark ring removed.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 35 â€” leaving the mirrors
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `diagnose` `x watch` `read watch` `north` `look` `north` `look` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> You have 5 of 7 hearts.

> A plain silver pocket watch, stopped. The inside of the lid is engraved, but too worn to read.

> There's nothing written on the pocket watch.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 36 â€” ring out of the mirrors
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `north` `north` `north` `remove ring` `diagnose` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> Plain dark ring removed.

> You have 5 of 7 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 37 â€” finding the real doorway
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x mirrors` `x reflections` `x doorway` `x door` `search` `find doorway` `close eyes` `back` `out` `look` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> Just mirrors now, and just you in them, keeping time properly.

> Just mirrors now, and just you in them, keeping time properly.

> You can't see any doorway here!

> You can't see any door here!

> You search carefully but find nothing unusual.

> You can't see any doorway here!

> You can't see any eyes here!

> Sorry, my memory is poor. Please give a direction.

> Which direction?

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 38 â€” trying every direction
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `east` `west` `up` `down` `northeast` `northwest` `southeast` `southwest` `north` `go back` `leave` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. Somewhere among them is the one real doorway, back the way you came. It is very cold.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south. The first mirror's room is back to the north.

> You can't see any back here!

> Which direction?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 39 â€” out through the mirrors without the ring
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `north` `north` `look` `diagnose` `save` `quit` `yes`
```
> Restored.
The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south. The first mirror's room is back to the north.

> The Rejection Mirror
A narrow room with a single tall mirror filling the far wall, its frame carved with grinning faces. The glass is old and silvered at the edges. The doorway to the south is beside it — you'd have to pass right in front of it to get there. The entrance hall is back to the north.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> You can't go that way.

> You can't go that way.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> You have 5 of 7 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 40 â€” watch to the clerk
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `out` `north` `north` `west` `north` `west` `give watch to clerk` `` `` `x charter` `read charter` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
Past the booth, a narrow passage leads south, deeper into the building. The door you came in by opens west onto the graveyard.
The building has the quality of a held breath.

> Which direction?

> You can't go that way.

> You can't go that way.

> Graveyard

> Church of All

> The door is locked.

> You can't see any clerk here!

> I beg your pardon?

> I beg your pardon?

> You can't see any charter here!

> You can't see any charter here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 41 â€” watch to the clerk (retry), enter verbs
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `leave church` `north` `enter church` `north` `west` `enter town hall` `west` `give watch to clerk` `` `` `x charter` `read charter` `east` `leave` `out` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
To the east, through a low archway, a stone altar stands in a space of its own, something brass catching the light at its face. The street door is north; a side door to the south lets out into the graveyard.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> Which direction?

> Main East

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> The clerk takes the watch without much interest — then turns it over, and stops. He opens the lid and looks at the worn engraving for a long time, his thumb moving across it as if he can read it by touch.
"This was my uncle's," he says quietly. "He went into that place by the graveyard. We never—" He stops. Closes the lid. Holds it a moment longer.
Then he stands, goes to a shelf without looking, and comes back with a rolled document tied in faded ribbon. He puts it in your hands. "The charter. Take it. Whatever you need it for."
[Town Charter added to inventory.]

> I beg your pardon?

> I beg your pardon?

> A rolled document tied with faded ribbon. The town seal is pressed into the wax at the bottom, and the handwriting is the careful kind that expects to be read for a long time.

> Most of it is the language of people who expected to be argued with: boundaries, rights of way, who mends the well. One clause has been underlined by a later hand: the town's bridges and crossings, above ground and below, are PUBLIC PROPERTY — free of toll, and free of anyone who'd charge one.

> Town Hall

> Which direction?

> Which direction?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 42 â€” charter to the Boggart, into the dungeon
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `east` `south` `south` `south` `down` `cast light` `down` `north` `west` `south` `give charter to boggart` `` `look` `open strongbox` `south` `look` `save` `quit` `yes`
```
> Restored.
Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above. The heavy doors open south onto the square.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> It is pitch black. You are likely to be eaten by a grue.

> It's too dark to go any further without a light.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Mausoleum

> The Crypt

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't see any boggart here!

> I beg your pardon?

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage slopes down into the dark. Steps climb up to the mausoleum.

> You can't see any strongbox here!

> You can't go that way.

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage slopes down into the dark. Steps climb up to the mausoleum.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 43 â€” crypt exits
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x footprints` `x passage` `follow footprints` `north` `south` `east` `west` `northeast` `northwest` `southeast` `southwest` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage slopes down into the dark. Steps climb up to the mausoleum.

> You can't see any footprints here!

> You can't see any passage here!

> I don't know the word "follow".

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage slopes down into the dark. Steps climb up to the mausoleum.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 44 â€” crypt: other ways down
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `d` `go down` `descend` `climb down` `enter passage` `in` `up` `down` `down` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage slopes down into the dark. Steps climb up to the mausoleum.

> Charnel Walk

> You can't go that way.

> The stairs only go up.

> The stairs only go up.

> You can't see any passage here!

> The Crypt

> The Mausoleum

> The Crypt

> Charnel Walk

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 45 â€” charter to the Boggart
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `west` `south` `give charter to boggart` `` `look` `x strongbox` `open strongbox` `south` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch, and beyond it worn steps climb up into the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels running back to the north.

> The Bone Passage

> The Junction

> The Toll Bridge

> The Boggart takes the charter, unrolls it, and reads. His lips move. He reads a particular clause twice. Then he rolls it back up with great dignity, hands it back, and gets off the bridge. "Public property," he mutters. "Should've been told." He stomps off into the tunnels, leaving behind a battered strongbox where he was sitting.

> I beg your pardon?

> The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
The bridge is empty now. The strongbox sits where he was.

> You see nothing special about the strongbox.

> You get your fingers under the lid and heave. It gives with a shriek of rusted hinges. Inside: 10 Zenni. You pocket them.

> Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, the bridge back to the north, and a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, the bridge back to the north, and a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 46 â€” Ink Corridor, Supply Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `west` `look` `x mechanism` `take bar` `take pot` `take jar` `take mortar` `take salt` `inventory` `save` `quit` `yes`
```
> Restored.
Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, the bridge back to the north, and a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south; the dungeon entrance is back to the north.
Something snags across your chest — a thread, there and gone. Above you, something bursts. Ink comes down in a cold black sheet and doesn't stop until you're wearing all of it.

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south; the dungeon entrance is back to the north.

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath. The doorway back to the corridor is east.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
Your foot catches on something in the floor. On the shelf beside you a clay pot tips, falls and bursts, and the room fills with choking grey smoke. When it clears, your eyes are streaming and your chest aches.

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath. The doorway back to the corridor is east.
Shards of a burst clay pot lie scattered in front of the shelf near the entrance.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
A squat glass jar sits among the clay pots, stoppered with wax.
One small clay pot sits on the shelf, the only one without a crack.

> You can't see any mechanism here!

> You take the portcullis bar.

> You take the small clay pot.

> You take the smoke jar.

> You take the mortar compound.

> You take the sack of salt.

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Portcullis bar
  Small clay pot
  Smoke jar
  Mortar compound
  Sack of salt
You have 67 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 47 â€” Storage Area, aqueduct
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `diagnose` `east` `east` `look` `x cart` `x beam` `south` `look` `x blocks` `x gap` `place block` `place block` `place block` `fix aqueduct` `look` `diagnose` `save` `quit` `yes`
```
> Restored.
Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath. The doorway back to the corridor is east.
Shards of a burst clay pot lie scattered in front of the shelf near the entrance.

> You have 4 of 7 hearts.

> Ink Corridor

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water. The corridor is back to the west.
Something catches your eye, tucked out of sight: 5 Zenni. You pocket them.

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water. The corridor is back to the west.

> A sturdy two-wheeled cart, the handles worn smooth. Built to carry more than a person could.

> A heavy timber beam, squared and solid. Something meant to hold up a ceiling.

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south. The storage chamber is back to the north.

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south. The storage chamber is back to the north.

> Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> You get your arms under the first block and heave it up into the gap. It grinds into place. Water finds its way around it, but less of it.

> The second block is heavier, or you're more tired. It goes in beside the first with a sound like a door shutting.

> The last block fights you the whole way up. Then it seats, and the gap is closed — though water still beads and runs at every joint.

> You work the mortar into every joint, pressing it in with your thumbs until the seeping stops. For a moment the channel is silent. Then the water finds its way through — the whole length of the aqueduct, running toward town.
You hear music — a familiar melody. You have reached level 5!

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, with a mended section in the middle where the mortar is still pale. Water moves through it quietly, on its way to somewhere it's needed. A passage leads on south. The storage chamber is back to the north.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 48 â€” Narrow Passageway, Idol Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `west` `south` `look` `south` `look` `x idol` `x pedestal` `x plate` `swap idol with salt` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, with a mended section in the middle where the mortar is still pale. Water moves through it quietly, on its way to somewhere it's needed. A passage leads on south. The storage chamber is back to the north.

> Storage Area

> You can't go that way.

> Ink Corridor

> Narrow Passageway
A short passage, plain stone, lower-ceilinged than the corridor to the north. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> Narrow Passageway
A short passage, plain stone, lower-ceilinged than the corridor to the north. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. Doorways lead north and south.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. Doorways lead north and south.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> A small stone figurine, squat and round-bellied, worn smooth by hands that weren't yours. A Chachapoyan Fertility Idol, if you had to guess.

> You can't see any pedestal here!

> You can't see any plate here!

> You set the sack of salt on the pedestal and lift the idol away in the same motion. The pedestal doesn't so much as twitch.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. Doorways lead north and south.
At the center stands a stone pedestal. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the salt's weight is holding it down now.
A sack of salt sits on the pedestal where the idol was.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 49 â€” Combat Room, first look
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `x warden` `x door` `x plate` `x east door` `diagnose` `save` `quit` `yes`
```
> Restored.
Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. Doorways lead north and south.
At the center stands a stone pedestal. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the salt's weight is holding it down now.
A sack of salt sits on the pedestal where the idol was.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Doorways lead north and south. Whatever happened in here happened more than once.
As you enter the room, a flagstone shifts under your foot and sinks with a heavy click. For a moment nothing happens, and that's somehow worse.
Somewhere behind the heavy door, a bell rings — once, flat and loud. Something on the other side moves. Then, slowly, the door at the east end begins to grind open.
[Press ENTER to continue] The door swings the rest of the way. The thing that comes through it was a guard once — the scraps of a uniform still hang off it — but whatever it is now is mostly reach, teeth, and intent. The Warden.

> The Warden stands between you and the open door, swaying, waiting for you to move.

> The heavy door stands open on the Creature Den. From this side you can see it was never meant to be opened from here.

> One flagstone sits a finger's width lower than the rest. You found it the usual way.

> The heavy door stands open on the Creature Den. From this side you can see it was never meant to be opened from here.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 50 â€” fighting the Warden
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `cast unbind undead` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `diagnose` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Doorways lead north and south. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Nothing here answers the spell.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 51 â€” fighting the Warden (2)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Doorways lead north and south. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.
The Warden goes down hard and doesn't get up. Something rolls from its grip and clatters across the floor — a lantern, unlit, its glass faintly green.

> You can't see any warden here!

> You can't see any warden here!

> You have 5 of 8 hearts.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Doorways lead north and south. Whatever happened in here happened more than once.
An old lantern lies on the floor, its glass faintly green.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 52 â€” Creature Den, Flooding Room first look
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `take lantern` `east` `look` `x bones` `north` `look` `x levers` `x left lever` `x middle lever` `x right lever` `x sluice` `x plate` `x water` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Doorways lead north and south. Whatever happened in here happened more than once.
An old lantern lies on the floor, its glass faintly green.

> You take the Guardian's Lantern.

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north; the combat room is back through the door to the west.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north; the combat room is back through the door to the west.

> You can't see any bones here!

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth.
Your foot comes down on a stone that sinks a little too easily. Click. You're starting to suspect the builders got a discount on pressure plates.
Behind you, a stone slab drops across the doorway with a boom you feel in your teeth. The grate on the north wall bursts open and water comes through in a cold, roaring sheet. In a few heartbeats it's above your knees.
The levers on the north wall suddenly look very interesting.

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> Three iron levers in a row — left, middle, right. Nothing says which does what.

> Three iron levers in a row — left, middle, right. Nothing says which does what.

> Three iron levers in a row — left, middle, right. Nothing says which does what.

> Three iron levers in a row — left, middle, right. Nothing says which does what.

> A square mouth low in the north wall, barred with an iron grate. Water is pouring through it.

> Somewhere under the water is the stone that started this. You don't need to see it again.

> You can't see any water here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 53 â€” Flooding Room: levers
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `look` `pull left lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> The left lever fights you, then comes down all at once. Under the water, something in the floor opens with a deep, sucking roar.
The water closes over your head and the floor drops away. The current takes you down through the sluice, turning you over in the dark, and lets go.
The Spillway
The sluice deposited you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> The Spillway
The sluice deposited you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 54 â€” the Spillway and beyond
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `x everything` `south` `look` `save` `quit` `yes`
```
> Restored.
The Spillway
The sluice deposited you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.

> Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> You can't see any everything here!

> The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 55 â€” Dream Corridor: follow
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `1` `look` `save` `quit` `yes`
```
> Restored.
Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 56 â€” Dream Corridor: follow, look closer
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `1` `1` `1` `1` `save` `quit` `yes`
```
> Restored.
Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> The footprints change. Halfway down the corridor they shift — your stride lengthens, the toe digs deeper. Whatever you were walking toward, you were walking faster by the time you reached it. You follow the change.
The footprints end at a wall. Not a door — a wall. But the mud at the base is disturbed, smeared, like something passed through it. The light flickers.
  1. Press your hand against the wall
  2. Step back and look at the full wall

> Cold stone. Solid. You press harder, run your fingers along the seam where the smear meets the surface. Nothing gives. It is definitively, completely a wall. You press your forehead against it. You wake up at the entrance. The footprints are there. Your size. Your stride.
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 57 â€” Dream Corridor: step back
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `1` `1` `2` `save` `quit` `yes`
```
> Restored.
Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> The footprints change. Halfway down the corridor they shift — your stride lengthens, the toe digs deeper. Whatever you were walking toward, you were walking faster by the time you reached it. You follow the change.
The footprints end at a wall. Not a door — a wall. But the mud at the base is disturbed, smeared, like something passed through it. The light flickers.
  1. Press your hand against the wall
  2. Step back and look at the full wall

> Distance doesn't help. It's a wall. Flat, unbroken, mortared tight. Whatever the smear in the mud means, it doesn't mean a door. You stand there long enough to be certain. You wake up at the entrance. The footprints are there. Your size. Your stride.
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 58 â€” Dream Corridor: listen
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `1` `2` `save` `quit` `yes`
```
> Restored.
Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> A sound comes from your left — a passage you didn't notice before, or didn't exist before. Water moving. Not dripping. Flowing. Like something is draining toward an opening.
You turn left. The passage is narrow — barely a shoulder's width. The sound of moving water is clearer now, ahead and below. The passage slopes down. The light gutters in a draft coming up from somewhere beneath you.
  1. Follow the slope down toward the sound
  2. Follow the draft, toward air

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 59 â€” Dream Corridor: listen, slope down
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `1` `2` `1` `save` `quit` `yes`
```
> Restored.
Dream Corridor
The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.
  1. Follow them
  2. Go another way

> The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.
  1. Look closer at the prints
  2. Listen
  3. Breathe in

> A sound comes from your left — a passage you didn't notice before, or didn't exist before. Water moving. Not dripping. Flowing. Like something is draining toward an opening.
You turn left. The passage is narrow — barely a shoulder's width. The sound of moving water is clearer now, ahead and below. The passage slopes down. The light gutters in a draft coming up from somewhere beneath you.
  1. Follow the slope down toward the sound
  2. Follow the draft, toward air

> The slope levels. The passage opens. The sound of water is all around you now — a drain somewhere below the floor, pulling the flood somewhere useful. The air is damp but moving. Ahead, a doorway. You walk through it. You are through.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
A young man crouches at the mouth of the tunnel, his hands raw, fingers still hooked as if he stopped mid-scrape and forgot how to start again. He turns as you come in. His eyes are wrong — too wide, too fixed — and he comes at you without a word.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 60 â€” the Lost Apprentice
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `look` `x young man` `x tunnel` `talk to young man` `diagnose` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> You see nothing special about the tunnel.

> There's no response from the apprentice.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 61 â€” apprentice: the spell
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `cast unbind undead` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Nothing here answers the spell.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 62 â€” apprentice: exits
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `look` `north` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Supply Cache
A side room half-buried by a collapse. Broken crates and a toppled shelf poke out of the rubble that fills the far end. Whatever was stored here was stored a long time ago. Passages lead north and south.

> Supply Cache
A side room half-buried by a collapse. Broken crates and a toppled shelf poke out of the rubble that fills the far end. Whatever was stored here was stored a long time ago. Passages lead north and south.

> Lost Apprentice's Cell
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 63 â€” Supply Cache and beyond
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `x crates` `x rubble` `search` `south` `look` `x everything` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Supply Cache

> You see nothing special about the rubble.

> You see nothing special about the rubble.

> You shift the loose stone at the edge of the rubble. Something underneath catches the light — a nugget of gold the size of a thumb joint.

> Flood Sump
The passage ends here in a low chamber, the floor wet — a shallow pool covers most of it, fed by seepage through the walls. The water is still and dark. The ceiling is close. This is the lowest point down here, and it feels like it. The only way out is back north.

> Flood Sump
The passage ends here in a low chamber, the floor wet — a shallow pool covers most of it, fed by seepage through the walls. The water is still and dark. The ceiling is close. This is the lowest point down here, and it feels like it. The only way out is back north.

> You can't see any everything here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 64 â€” Flood Sump, nugget
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x pool` `search pool` `search` `north` `take nugget` `x nugget` `north` `north` `look` `save` `quit` `yes`
```
> Restored.
Flood Sump
The passage ends here in a low chamber, the floor wet — a shallow pool covers most of it, fed by seepage through the walls. The water is still and dark. The ceiling is close. This is the lowest point down here, and it feels like it. The only way out is back north.

> You can't see any pool here!

> You can't see any pool here!

> You search carefully but find nothing unusual.

> Supply Cache
There is a gold nugget here.

> You take the gold nugget.

> A rough nugget of gold, heavy for its size, still gritty with rock dust.

> Lost Apprentice's Cell
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Dream Corridor

> Dream Corridor
A low, wet corridor running north and south. There are footprints in the mud, and they are only yours.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 65 â€” apprentice: the pickaxe
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `give pickaxe to apprentice` `look` `save` `quit` `yes`
```
> Restored.
Dream Corridor
A low, wet corridor running north and south. There are footprints in the mud, and they are only yours.

> Lost Apprentice's Cell
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> The apprentice doesn't take the pickaxe.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 66 â€” apprentice: the tunnel
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `use pickaxe on tunnel` `dig` `x bedding` `show lantern to apprentice` `light lantern` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Nothing happens.

> He's not going to let you near it.

> You can't see any bedding here!

> I don't know the word "show".

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 67 â€” apprentice: subdue
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `attack apprentice` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> You get a blow in. He staggers, shakes his head, and comes again.

> You have 5 of 8 hearts.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 68 â€” apprentice: subdue (2)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `attack apprentice` `attack apprentice` `attack apprentice` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, someone has clawed out a tunnel, angling steeply up into the dark — and stopping a little short of anything. Passages lead north and south.
The apprentice crouches between you and the tunnel, breathing hard, watching you with eyes that don't blink enough.

> You get a blow in. He staggers, shakes his head, and comes again.

> You get a blow in. He staggers, shakes his head, and comes again.
He goes down on one knee and stays there. When he looks up, his eyes are his own again — red-rimmed, frightened, very young. "I was digging," he says. "I was digging for so long." He looks at his hands as if they belong to someone else.
He gets to his feet slowly and looks at the tunnel for a long moment. Then he climbs back into it. You hear him digging — not frantic now, just steady — then a soft slump of earth, and grey light spills down the shaft along with the smell of the bog.
[Press ENTER to continue] He slides back down, filthy and almost smiling. He peels off his gloves and holds them out. "They were for digging," he says. "I won't be doing that again." He starts up the tunnel, stops, and looks back. "Tell Will—" He shakes his head. "No. I'll tell him myself." Then he's gone.
[Apprentice's Gloves added to inventory.]

> You have 5 of 8 hearts.

> Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, the tunnel angles steeply up to a ragged patch of grey light. Passages lead north and south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 69 â€” (backup: before lever) middle lever
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `pull middle lever` `look` `pull middle lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> The middle lever comes down with a heavy clunk. Behind the grate the sluice slams shut, and the water stops coming. It doesn't go anywhere, either.

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water stands knee-deep across the floor, flat and still. The grate has stopped pouring.

> You already tried that one.

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water stands knee-deep across the floor, flat and still. The grate has stopped pouring.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 70 â€” (after middle) right lever, then left
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `pull right lever` `look` `pull left lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water stands knee-deep across the floor, flat and still. The grate has stopped pouring.

> The lever snaps off in your hand. Behind the grate something gives with a groan, and a fresh surge pushes the water up to your waist.

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water stands waist-deep across the floor, flat and still. The grate has stopped pouring.

> The left lever fights you, then comes down all at once. Under the water, something in the floor opens with a deep, sucking roar.
The water closes over your head and the floor drops away. The current takes you down through the sluice, turning you over in the dark, and lets go.
The Spillway
The sluice deposited you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> The Spillway
The sluice deposited you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 71 â€” (backup: before lever) waiting in the flood
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wait` `wait` `wait` `wait` `wait` `wait` `look` `diagnose` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Flooding Room
A low cave, the floor dipping toward the middle. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. A stone slab seals the doorway to the south. Water churns knee-deep across the floor, still pouring through the grate.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 72 â€” up the apprentice's tunnel
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x gloves` `wear gloves` `up` `look` `save` `quit` `yes`
```
> Restored.
Lost Apprentice's Cell
A cramped cell cut into the rock, more burrow than room. Scraps of bedding are heaped in one corner. Low in the weakest stretch of wall, where the rock gives way to packed earth, the tunnel angles steeply up to a ragged patch of grey light. Passages lead north and south.

> You see nothing special about the Apprentice's Gloves.

> You put on the Apprentice's Gloves.

> You climb the tunnel hand over hand and haul yourself out into the reeds. A line of muddy footprints leads away toward town.
The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 73 â€” bog to the Prayer Alcove
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `south` `south` `east` `east` `east` `south` `south` `south` `cast light` `down` `down` `north` `west` `south` `south` `south` `south` `south` `south` `south` `look` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench

> Roundabout Pond
You see a bottle at the bottom of the pond.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Mausoleum

> The Crypt

> Charnel Walk

> The Bone Passage

> The Junction

> The Toll Bridge
A narrow stone bridge, solid-looking for all its age, spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. Across it, the tunnel runs on south; the junction is back to the north.
The bridge is empty. The open strongbox sits where he was, lid thrown back.

> Dungeon Entrance

> Ink Corridor

> Narrow Passageway

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Doorways lead north and south. Whatever happened in here happened more than once.

> Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
The niche goes back further than it looks. Behind the carved lip there's a gap — and inside it, things that were put there on purpose.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 74 â€” crowbar, south of the alcove
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `take crowbar` `take vial` `x vial` `south` `look` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> You take the crowbar.

> You take the vial of glacier melt.

> A stoppered vial of water so cold the glass has frosted. It doesn't warm in your hand.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The air around the bars has a faint, dry crackle, and the hairs on your arms stand up as you get close. The corridor runs north and south; the bars stand between you and the far end.
You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 75 â€” portcullis
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x portcullis` `x mechanism` `lift portcullis` `look` `save` `quit` `yes`
```
> Restored.
Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.

> Heavy iron bars, set into grooves in the walls. The crackle is gone.

> A plate of dark metal set flush into the stone, a short lever at its center. The lever is down.

> You get under the portcullis and heave. It rises, grinding, until it's head-high — and stays there only as long as you hold it.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.
You let go. The portcullis slams back down.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 76 â€” propping the portcullis
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `lift portcullis` `prop portcullis with bar` `look` `south` `look` `save` `quit` `yes`
```
> Restored.
Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.

> You get under the portcullis and heave. It rises, grinding, until it's head-high — and stays there only as long as you hold it.

> Which bar do you mean, the portcullis bar, or the crowbar?

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.
You let go. The portcullis slams back down.

> The portcullis is down.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 77 â€” propping the portcullis (2)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `lift portcullis` `prop portcullis with portcullis bar` `look` `south` `look` `save` `quit` `yes`
```
> Restored.
Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The corridor runs north and south; the bars stand between you and the far end.

> You get under the portcullis and heave. It rises, grinding, until it's head-high — and stays there only as long as you hold it.

> You wedge the iron bar under the portcullis. It takes the weight with a groan and holds. The way south is open.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The portcullis is propped open with an iron bar. The corridor runs north and south, the way through clear now.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 78 â€” Shrine Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `take fragment` `x plinth` `x depression` `assemble bowl` `inventory` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> You take the stone bowl piece.

> A waist-high stone plinth, finer work than anything around it. The depression in its top is bowl-shaped and empty, the stone inside worn smooth. Carved into its side, small and faded: a seed inside a circle of leaves.

> A waist-high stone plinth, finer work than anything around it. The depression in its top is bowl-shaped and empty, the stone inside worn smooth. Carved into its side, small and faded: a seed inside a circle of leaves.

> The pieces fit, but nothing holds them together.

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 79 â€” (backup: alcove) portcullis disarm roll 1
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `diagnose` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The air around the bars has a faint, dry crackle, and the hairs on your arms stand up as you get close. The corridor runs north and south; the bars stand between you and the far end.
You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 80 â€” (backup: alcove) portcullis disarm roll 2
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `diagnose` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The air around the bars has a faint, dry crackle, and the hairs on your arms stand up as you get close. The corridor runs north and south; the bars stand between you and the far end.
You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 81 â€” (backup: alcove) portcullis disarm roll 3
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `diagnose` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove off a passage that runs north and south, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The air around the bars has a faint, dry crackle, and the hairs on your arms stand up as you get close. The corridor runs north and south; the bars stand between you and the far end.
You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it.

> You have 5 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 82 â€” to the Storage Area for the cart
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `north` `north` `north` `north` `east` `look` `take cart` `x cart` `take beam` `inventory` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.

> Portcullis Corridor
A straight corridor, closed off halfway along by an iron portcullis. The portcullis is propped open with an iron bar. The corridor runs north and south, the way through clear now.

> Prayer Alcove

> Combat Room

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Storage Area

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water. The corridor is back to the west.

> You take the hand cart.

> A sturdy two-wheeled cart, the handles worn smooth. Built to carry more than a person could.

> You take the support beam.

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
  Hand cart
  Support beam
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 83 â€” drop test, cart to the bog
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `drop beam` `drop burnt-out torch` `look` `west` `east` `west` `north` `north` `north` `east` `south` `up` `up` `north` `north` `north` `west` `west` `west` `north` `north` `north` `east` `south` `x gravestone` `put gravestone in cart` `look` `save` `quit` `yes`
```
> Restored.
Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Scuffs in the dust show where equipment once stood. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water. The corridor is back to the west.

> You drop the support beam.

> You can't see any torch here!

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water. The corridor is back to the west.

> Ink Corridor

> Storage Area

> Ink Corridor

> Dungeon Entrance

> The Toll Bridge

> The Junction

> The Bone Passage

> Charnel Walk

> The Crypt

> The Mausoleum

> Graveyard

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Roundabout Pond
You see a bottle at the bottom of the pond.

> The Bog of Eternal Stench

> The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench

> The Bog of Eternal Stench
A gravestone lies face-down in the mud.

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> You tip the gravestone up out of the mud and walk it, corner by corner, onto the cart. The axle complains. The bog lets go of the stone with a sound you'd rather not have heard. The gravestone is loaded.

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 84 â€” gravestone to the graveyard, councilman
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `west` `south` `south` `south` `east` `east` `look` `x fountain` `east` `south` `south` `look` `place gravestone` `look` `north` `north` `west` `north` `east` `talk to man` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.

> The Bog of Eternal Stench
The cart takes some getting started. Once it's rolling, it wants to keep going.

> The Bog of Eternal Stench
A hollow log lies half-sunk among the reeds.

> The Bog of Eternal Stench

> Roundabout Pond
You see a bottle at the bottom of the pond.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. Main Street runs off east and west, and to the southwest a gap between buildings leads into an alley.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Water runs from the spout into the basin, clear and cold. The crack at the edge weeps a little, but it holds.

> Main East

> Church of All

> Graveyard

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> You wheel the cart to the empty plot — a rectangle of disturbed earth with a broken stub of mortar at its head — and tip the gravestone back into place. It settles as if it remembers the spot. You leave the cart beside it; it's done its job.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.
One headstone near the path stands straighter than the others, newly scrubbed of mud: CALDER FINCH — EXPLORER. An empty hand cart stands beside it.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Council Chamber

> Councilman Rowan Finch takes one look at the ink and wants nothing to do with you until it's gone.

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 85 â€” washing off the ink
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x me` `west` `south` `wash` `wash in fountain` `north` `east` `talk to man` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> You see nothing special about the Sable.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> I don't know the word "wash".

> I don't know the word "wash".

> Town Hall

> Council Chamber

> Councilman Rowan Finch takes one look at the ink and wants nothing to do with you until it's gone.

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 86 â€” cleaning the ink
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `south` `clean ink` `clean me` `bathe` `rinse` `swim` `enter fountain` `use fountain` `drink from fountain` `x ink` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You can't see any ink here!

> If you wish, but heaven only knows why.

> There's nothing here to swim in.

> I don't know the word "rinse".

> There's nothing here to swim in.

> You can't go in there.

> Nothing happens.

> That sentence isn't one I recognize.

> You can't see any ink here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 87 â€” the pond for the ink
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `west` `north` `swim` `look` `wash` `enter pond` `bathe in pond` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. Main Street runs off east and west, and to the southwest a gap between buildings leads into an alley.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Roundabout Pond
You see a bottle at the bottom of the pond.

> You don't want to swim in that!

> Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path to the south and the bog to the north, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> I don't know the word "wash".

> You can't see any pond here!

> That sentence isn't one I recognize.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 88 â€” May: ink tip and crowbar
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `east` `east` `south` `south` `look` `talk to may` `` `tip may 5` `inventory` `save` `quit` `yes`
```
> Restored.
Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path to the south and the bog to the north, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.

> May looks at the ink, then at you. "Rooms are upstairs. That's all you're getting from me until you've used one."

> I beg your pardon?

> May looks at the ink, then at you. "Rooms are upstairs. That's all you're getting from me until you've used one."

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 89 â€” using a room upstairs
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `up` `look` `x doors` `open door` `enter room` `sleep` `rest` `wash` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Upstairs Hall

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Three plain doors, each with a brass number gone brown with handling.

> The rooms are rented from the bartender downstairs.

> You can't see any room here!

> I don't know the word "sleep".

> You're not tired.

> I don't know the word "wash".

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 90 â€” renting a room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `down` `south` `rent room` `buy room` `` `look` `save` `quit` `yes`
```
> Restored.
Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May looks at the ink for a long moment. "Five Zenni," she says, and slides a key across the bar. "There's a bath up there. Use it."
Guest Room 3
The ink takes three changes of water and most of the soap. It comes off.
You wake in the small room at the end of the hall. The candle is out. You are rested — properly, completely rested. That will do.
The door out to the hall is south.

> There's no one here to sell you that.

> I beg your pardon?

> Guest Room 3
The smallest of the three rooms, tucked at the end of the hall. Low ceiling, narrow bed, a single candle on the nightstand burned to nothing. Quiet in a way the other rooms aren't.
The door out to the hall is south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 91 â€” councilman, May and the cellar key
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `diagnose` `south` `down` `north` `north` `east` `talk to man` `` `` `west` `south` `south` `south` `talk to may` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
Guest Room 3
The smallest of the three rooms, tucked at the end of the hall. Low ceiling, narrow bed, a single candle on the nightstand burned to nothing. Quiet in a way the other rooms aren't.
The door out to the hall is south.

> You are in perfect health — 8 of 8 hearts.

> Upstairs Hall

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Council Chamber

> He looks up from his papers with the expression of someone who has been interrupted before and expects to be interrupted again. "Can I help you?" It is not entirely a question.

> I beg your pardon?

> I beg your pardon?

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May's eyes drop to the crowbar and stay there. "Now that's useful." She reaches under the bar and sets an iron key on the counter. "Cellar. It flooded years back — the drain clogged, and we shut the door and stopped thinking about it. If you can get the cover off that drain, it's yours to clear." She slides the key over. "Do it from the top of the stairs. Nobody goes down into that water."

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Muddy bowl piece
  Plain dark ring (not worn)
  Bow
  Pale Blade
  Coil of rope
  Flat rune stone
  Large bowl piece
  Flint and steel
  Pickaxe
  Heart necklace (being worn)
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Chachapoyan Fertility Idol
  Guardian's Lantern
  Gold nugget
  Apprentice's Gloves (being worn)
  Crowbar
  Vial of glacier melt
  Stone bowl piece
  Cellar key
You have 87 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 92 â€” kitchen cellar
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `south` `unlock cellar door with key` `open cellar door` `look` `x drain` `pry drain with crowbar` `look` `x drain` `x water` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only the bartender understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south, and the main room is back to the north.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> The key turns stiffly. The lock hasn't been asked to do anything in years. You leave it where it is.

> The cellar door comes up on a breath of cold, wet air. Stone steps lead down — three of them, then water, still and clear, filling the cellar nearly to the beams. At the foot of the steps, through the water, you can make out the square iron cover of a drain.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> A square iron cover at the foot of the steps, under the water.

> You lie flat on the top step and reach the crowbar down through the water, feeling along the bottom step until the lip catches the edge of the grate. You lean on it. The cover comes up with a jolt and slides off into the dark. Below the cover, the drain mouth is packed solid with rotted sacking and root. The water isn't going anywhere.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> The drain mouth is choked with rotted sacking and root. Clear that, and the water has somewhere to go.

> You can't see any water here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 93 â€” clearing the drain
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `pull sacking` `unclog drain` `clear drain with crowbar` `look` `down` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> You can't see any sacking here!

> You work the crowbar down into the open drain and lever. Something gives — a fist of rotted sacking and root comes up through the water — and the whole cellar starts to turn. The water drops a step, then another, then goes all at once with a long, sucking roar you feel through the kitchen floor. When it's quiet again, the stairs go all the way down.
You hear music — a familiar melody. You have reached level 6!
You feel a deeper sense of calm settle over you — the kind that comes with hard-won experience. You can now REST to recover when the fighting stops.

> That sentence isn't one I recognize.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 94 â€” cashbox, councilman again
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `open cashbox` `up` `north` `north` `north` `north` `east` `talk to man` `` `` `west` `west` `talk to clerk` `` `` `east` `east` `talk to man` `` `` `save` `quit` `yes`
```
> Restored.
Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> The lid gives on the third try. Inside, wrapped in oilcloth and perfectly dry: 10 Zenni. Somebody planned for the flood better than they planned for the drain.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Council Chamber

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> I beg your pardon?

> I beg your pardon?

> Town Hall

> Records Room

> The clerk is turning the pocket watch over in his hands. He nods to you, but doesn't say anything.

> I beg your pardon?

> I beg your pardon?

> Town Hall

> Council Chamber

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 95 â€” gravestone, councilman
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `talk to man` `talk to councilman` `west` `south` `east` `south` `south` `x gravestone` `read gravestone` `north` `north` `west` `north` `east` `talk to man` `` `` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> There's nothing written on the gravestone.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Council Chamber

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 96 â€” Trophy Case, councilman
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `up` `up` `put idol in case` `put nugget in case` `look` `score` `down` `down` `east` `talk to man` `` `` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Upper Hall

> The Tower

> The case is closed.

> The case is closed.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama. The narrow stair winds back down to the hall below.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.

> Score: 0
Level 6 (235 XP)
Zenni: 102
0 treasures on display.

> Upper Hall

> Town Hall

> Council Chamber

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 97 â€” Trophy Case (open), councilman
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `up` `up` `open case` `put idol in case` `put nugget in case` `score` `down` `down` `east` `talk to man` `` `` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Upper Hall

> The Tower

> The glass door swings open on its brass hinges.

> The Chachapoyan Fertility Idol settles into the velvet. The case is a better place for it.

> The gold nugget settles into the velvet. The case is a better place for it.

> Score: 51
Level 6 (235 XP)
Zenni: 102
2 treasures on display.

> Upper Hall

> Town Hall

> Council Chamber

> "My grandfather built this town as much as anyone. He explored the passages beneath it too — donated whatever he found to the Trophy Case upstairs. It's been empty for years. I don't know what that says about the state of adventure in Roundabout."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 98 â€” cellar shortcut to the Shrine Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `south` `south` `south` `south` `down` `west` `look` `west` `south` `south` `south` `south` `south` `south` `south` `south` `south` `look` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> The door is closed.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> The door is closed.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 99 â€” cellar shortcut to the Shrine Room (2)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `open door` `west` `look` `west` `south` `south` `south` `south` `south` `south` `south` `south` `south` `look` `save` `quit` `yes`
```
> Restored.
Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> The door swings inward onto dark stone. Cold air comes through it, and the smell of old earth.

> It is pitch black. You are likely to be eaten by a grue.

> It is pitch black. You are likely to be eaten by a grue.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It is pitch black. You are likely to be eaten by a grue.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 100 â€” light, to the Shrine Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `cast light` `look` `west` `south` `south` `south` `south` `south` `south` `south` `south` `south` `look` `save` `quit` `yes`
```
> Restored.
It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Bone Passage

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south, and west toward the junction. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> The Junction

> The Toll Bridge

> Dungeon Entrance

> Ink Corridor

> Narrow Passageway

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Combat Room

> Prayer Alcove

> Portcullis Corridor

> Shrine Room

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 101 â€” drop all, the bridge
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `drop all` `look` `inventory` `take wax seal` `take lantern` `south` `look` `south` `look` `x door` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.

> You toss the burnt-out torch aside. It's no good to anyone now.
You drop the dagger.
You drop the wax seal.
You drop the muddy bowl piece.
You drop the bow.
You drop the Pale Blade.
You drop the coil of rope.
You drop the flat rune stone.
You drop the large bowl piece.
You drop the flint and steel.
You drop the pickaxe.
You drop the grey rune stone.
You drop the town charter.
You drop the small clay pot.
You drop the smoke jar.
You drop the Guardian's Lantern.
You drop the crowbar.
You drop the vial of glacier melt.
You drop the stone bowl piece.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. A corridor leads north; to the south, the floor gives way to a narrow stone bridge.
There is a dagger here.
There is a wax seal here.
There is a muddy bowl piece here.
There is a bow here.
There is a Pale Blade here.
There is a coil of rope here.
There is a flat rune stone here.
There is a large bowl piece here.
There is a flint and steel here.
There is a pickaxe here.
There is a grey rune stone here.
There is a town charter here.
There is a small clay pot here.
There is a smoke jar here.
There is a Guardian's Lantern here.
There is a crowbar here.
There is a vial of glacier melt here.
There is a stone bowl piece here.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Apprentice's Gloves (being worn)
You have 102 Zenni.

> You take the wax seal.

> You take the Guardian's Lantern.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door. To the north, a carved doorway leads into an older room.
A side passage to the west is choked with debris.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door. To the north, a carved doorway leads into an older room.
A side passage to the west is choked with debris.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key. The bridge is back to the north.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key. The bridge is back to the north.

> You see nothing special about the iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 102 â€” back to the councilman after seeing the door
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `east` `east` `up` `north` `north` `north` `north` `east` `talk to man` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key. The bridge is back to the north.

> Rickety Bridge

> Shrine Room
There is a dagger here.
There is a muddy bowl piece here.
There is a bow here.
There is a Pale Blade here.
There is a coil of rope here.
There is a flat rune stone here.
There is a large bowl piece here.
There is a flint and steel here.
There is a pickaxe here.
There is a grey rune stone here.
There is a town charter here.
There is a small clay pot here.
There is a smoke jar here.
There is a crowbar here.
There is a vial of glacier melt here.
There is a stone bowl piece here.

> Portcullis Corridor

> Prayer Alcove

> Combat Room

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Dungeon Entrance

> The Toll Bridge

> The Junction

> The Bone Passage

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. Steps climb back up to the kitchen. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Council Chamber

> "I went out to the cemetery this morning," Rowan says. "Grandfather's stone is back where it belongs." Then, flatly: "That cart you left by the grave came from the dungeon. Don't bother denying it — I've seen it before, in my grandfather's papers." He studies you for a moment. "He left a key. Said it led to a lower level — wouldn't say what was down there." He holds it out. "Take it. It was never meant for me."
[Middle Tier Key added to inventory.]

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Apprentice's Gloves (being worn)
  Wax seal
  Guardian's Lantern
  Middle Tier Key
You have 108 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 103 â€” down to the key door and the Mine Passage
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `south` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `south` `south` `south` `south` `south` `south` `south` `south` `unlock door with key` `open door` `south` `look` `south` `look` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. The door back to the foyer is west.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> You can't go that way.

> You can't go that way.

> There's light enough here already.

> You can't go that way.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> It's already unlocked. The key is still in the lock.

> It's already open.

> You can't go that way.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> You can't go that way.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 104 â€” down to the key door (2)
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `down` `west` `cast light` `west` `south` `south` `south` `south` `south` `south` `south` `south` `south` `south` `south` `unlock door with key` `open door` `south` `look` `south` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door that leads back north to the bar.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Bone Passage

> The Junction

> The Toll Bridge

> Dungeon Entrance

> Ink Corridor

> Narrow Passageway

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Combat Room

> Prayer Alcove

> Portcullis Corridor

> Shrine Room
There is a dagger here.
There is a muddy bowl piece here.
There is a bow here.
There is a Pale Blade here.
There is a coil of rope here.
There is a flat rune stone here.
There is a large bowl piece here.
There is a flint and steel here.
There is a pickaxe here.
There is a grey rune stone here.
There is a town charter here.
There is a small clay pot here.
There is a smoke jar here.
There is a crowbar here.
There is a vial of glacier melt here.
There is a stone bowl piece here.

> Rickety Bridge

> Mid-Tier Key Door

> The finch key goes in stiffly and turns with a sound like a dropped anvil. The iron door swings inward under its own weight. Beyond it, stone stairs lead down. You leave the key in the lock.

> You can't open that.

> Key Door Landing
The staircase ends in a rough cave — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south, and the stairs climb back north to the iron door.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> Key Door Landing
The staircase ends in a rough cave — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south, and the stairs climb back north to the iron door.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. The stairs are back to the north; the passage runs on to the south, and a narrower side passage opens to the east. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. The stairs are back to the north; the passage runs on to the south, and a narrower side passage opens to the east. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 105 â€” silver dust
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x dust` `take dust` `x silver dust` `take charcoal` `inventory` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. The stairs are back to the north; the passage runs on to the south, and a narrower side passage opens to the east. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> A pinch of fine silver dust. It catches the light even down here. Where it's settled in the creases of your fingers, every line stands out.

> You pinch the silver dust out of the crack and pocket it.

> A pinch of fine silver dust. It catches the light even down here. Where it's settled in the creases of your fingers, every line stands out.

> You take the charcoal.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Apprentice's Gloves (being worn)
  Wax seal
  Guardian's Lantern
  Silver dust
  Charcoal
You have 109 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 106 â€” Stored Room peek
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `look` `x floor` `dig` `west` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. The stairs are back to the north; the passage runs on to the south, and a narrower side passage opens to the east. A large iron chest is bolted to the floor against one wall.

> Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose. A narrow passage carries on east beyond it; the mine passage is back to the west.
Something catches your eye, tucked out of sight: 5 Zenni. You pocket them.

> Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose. A narrow passage carries on east beyond it; the mine passage is back to the west.

> You can't see any floor here!

> The fill is packed too tight to move by hand. You'd need a shovel.

> Mine Passage

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 107 â€” east of the Stored Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `east` `look` `east` `look` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. The stairs are back to the north; the passage runs on to the south, and a narrower side passage opens to the east. A large iron chest is bolted to the floor against one wall.

> Stored Room

> The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, and from its outstretched finger dangles a gold pocket watch on a chain. The only way out is back west.

> The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, and from its outstretched finger dangles a gold pocket watch on a chain. The only way out is back west.

> The crack is far too narrow. He found that out.

> The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, and from its outstretched finger dangles a gold pocket watch on a chain. The only way out is back west.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 108 â€” the gold watch
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `x skeleton` `x watch` `take watch` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, and from its outstretched finger dangles a gold pocket watch on a chain. The only way out is back west.

> You see nothing special about the skeleton.

> A gold pocket watch, its case engraved in a pattern worn almost smooth. It stopped long ago at a quarter past three.

> You take the gold pocket watch.

> You are in perfect health — 8 of 8 hearts.

> The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, the finger empty now. The only way out is back west.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 109 â€” back up to the Pipe Room
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `west` `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `north` `east` `east` `up` `north` `north` `east` `look` `x jar` `x crack` `read jar` `save` `quit` `yes`
```
> Restored.
The Crevice
The passage pinches down to a crack in the far wall, and a skeleton is wedged into it at the shoulders — someone who tried to squeeze through and didn't fit. One arm hangs back toward you, the finger empty now. The only way out is back west.

> Stored Room

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door
The iron door stands open, the finch key still in its lock. Stone stairs lead down to the south. The bridge is back to the north.

> Rickety Bridge

> Shrine Room
There is a dagger here.
There is a muddy bowl piece here.
There is a bow here.
There is a Pale Blade here.
There is a coil of rope here.
There is a flat rune stone here.
There is a large bowl piece here.
There is a flint and steel here.
There is a pickaxe here.
There is a grey rune stone here.
There is a town charter here.
There is a small clay pot here.
There is a smoke jar here.
There is a crowbar here.
There is a vial of glacier melt here.
There is a stone bowl piece here.

> Portcullis Corridor

> Prayer Alcove

> Combat Room

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Dungeon Entrance

> The Toll Bridge

> The Junction

> The Bone Passage

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Pipe Room
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> You trace the letters around the base. The silver that once filled them has worn away to a few bright flecks, and without it they're only the shape of words, not the words.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 110 â€” jar: silver dust, first-time phrasing
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `put dust on letters` `x jar` `read jar` `listen to jar` `look` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> The dust would only sift into the crack.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> You trace the letters around the base. The silver that once filled them has worn away to a few bright flecks, and without it they're only the shape of words, not the words.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 111 â€” jar: the crack
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `repair jar` `seal crack with wax` `x jar` `read jar` `listen to jar` `look` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> You press the wax seal over the crack. The wax gives, then takes — it spreads along the line of the crack and sets, red against the blue-grey glaze. The hum steadies.
Something clinks inside the jar. Five Zenni sit in the bottom, kept there by the crack until now. You pocket them.

> The crack is already sealed.

> A ceramic jar, glazed blue-grey, its crack sealed with red wax. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> You trace the letters around the base. The silver that once filled them has worn away to a few bright flecks, and without it they're only the shape of words, not the words.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A ceramic jar sits on the side table, its crack sealed with red wax, humming faintly to itself.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 112 â€” jar: silver dust
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `put dust on letters` `x jar` `read jar` `listen to jar` `look` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A ceramic jar sits on the side table, its crack sealed with red wax, humming faintly to itself.

> You sprinkle the silver dust over the jar. It clings to the glaze and settles into the etched letters around the base, and for a moment the whole jar glints.

> A ceramic jar, glazed blue-grey, its crack sealed with red wax. It hums — a low, steady note you feel more than hear. Silver dust has settled into the letters around its base, and they stand out clearly now.

> You read the words around the base aloud: "Hold what was heard. Speak what was held." The hum rises, wavers, and stops. In the silence, a voice no louder than breath: "The ceiling of the thermal vent holds a secret." Then nothing.

> Nothing. The jar is quiet now.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A mended ceramic jar sits on the side table, quiet.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 113 â€” to the Swarm Tree
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `north` `east` `east` `east` `north` `look` `east` `look` `diagnose` `wait` `diagnose` `wait` `diagnose` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A mended ceramic jar sits on the side table, quiet.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan. The oak's clearing is back to the west, at a more comfortable distance.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You have 7 of 8 hearts.

> Time passes...

> You have 7 of 8 hearts.

> Time passes...

> You have 7 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 114 â€” Swarm Tree down to the last heart
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `east` `east` `east` `east` `east` `diagnose` `east` `diagnose` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> You have 2 of 8 hearts.

> Swarm Tree
The swarm boils out of the hollow before you can do anything useful. You retreat.
You're hurting badly now. One more like that and you won't get up.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> You have 1 of 8 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 115 â€” SANDBOX (throwaway branch from a backup save): ring ladder to ~20
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...
The ring feels less like something you're wearing and more like something you're holding onto. Or something holding onto you.

> It slides off easily enough. Your finger stays warm where it was.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 116 â€” SANDBOX: ring ladder to ~30
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...
The ring is heavier than it was. Not in weight — in presence. It knows you're wearing it. You find yourself aware of it in a way you weren't before.

> It sticks at the knuckle, just for a moment, before it lets you go.
Plain dark ring removed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 117 â€” SANDBOX: ring ladder to ~40
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...

> Time passes...
The ring is harder to ignore than it was. You are aware of it the way you're aware of a sound that hasn't stopped. You should take it off. You know you should take it off.

> It sticks at the knuckle, just for a moment, before it lets you go.
Plain dark ring removed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 118 â€” SANDBOX: ring 41-43, removal roll 1
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 119 â€” SANDBOX: ring 41-43, removal roll 2
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 120 â€” SANDBOX: ring 41-43, removal roll 3
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 121 â€” SANDBOX: ring 41-43, removal roll 4
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 122 â€” SANDBOX: ring to ~47, removal roll 1
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> Time passes...
Take it — the thought slides away before you finish it.

> Time passes...
Off. Take it… You lose the rest of the sentence.

> Time passes...
You don't need to take it off. Do you?

> Time passes...
Why would you take it off?

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 123 â€” SANDBOX: ring to ~47, removal roll 2
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> Time passes...
Take it — the thought slides away before you finish it.

> Time passes...
Off. Take it… You lose the rest of the sentence.

> Time passes...
You don't need to take it off. Do you?

> Time passes...
Why would you take it off?

> The ring comes off. It didn't want to. You're not sure you could have held out another moment.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 124 â€” SANDBOX: ring to ~47, removal roll 3
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> Time passes...
Take it — the thought slides away before you finish it.

> Time passes...
Off. Take it… You lose the rest of the sentence.

> Time passes...
You don't need to take it off. Do you?

> Time passes...
Why would you take it off?

> The ring comes off. It didn't want to. You're not sure you could have held out another moment.
Plain dark ring removed.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 125 â€” SANDBOX: ring to ~47, removal roll 4
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `wear ring` `wait` `wait` `wait` `wait` `wait` `wait` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The warmth is there before the ring is all the way on. It remembers where it left off.
Take it off. You should take it off.

> Time passes...
Take it off. Soon.

> Time passes...
You could take it off. You could.

> Time passes...
Take it — the thought slides away before you finish it.

> Time passes...
Off. Take it… You lose the rest of the sentence.

> Time passes...
You don't need to take it off. Do you?

> Time passes...
Why would you take it off?

> You try to take the ring off. Your fingers find it. They don't do what you ask.
It's fine. The ring is fine.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.
The ring is warm, and you are warm, and everything is fine.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 126 â€” (backup: before sealing the jar) May's tips
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `west` `south` `tip may 5` `tip may 10` `read tip journal` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar. The noise of the main room drifts in faintly through the doorway to the west.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May pockets the coins carefully. "That buys you something worth hearing," she says.
"There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it."

> May counts the coins once, pockets them, and leans all the way across the bar. "Sable," she says.
"No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew."

> You don't have a journal.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 127 â€” (main save restored) rest, apostrophes
(preamble: open mailbox / yes / ENTER / rogue / Sable / ENTER / restore â€” omitted)
Commands: `rest` `diagnose` `x kite` `x child's kite` `x the child's kite` `x oak's branches` `west` `look` `x beekeeper's hives` `x hives` `talk to beekeeper` `` `` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> You sit with your back to the nearest wall and let your breathing slow. When you get up, some of the ache has gone with it.

> You have 2 of 8 hearts.

> You can't see any kite here!

> You can't see any kite here!

> You can't see any kite here!

> You can't see any branches here!

> Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The old oak's clearing is back to the east. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.
"You'll want to keep clear of the tree east of the oak," she says, before you've said anything. "Swarm got loose and nested in a hollow there. I'd fetch them back, but my smoke kit's gone — somewhere in the tunnels under town, last I knew." She shrugs. "If you come across it."

> Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The old oak's clearing is back to the east. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.

> You can't see any hives here!

> You can't see any hives here!

> "You'll want to keep clear of the tree east of the oak," she says, before you've said anything. "Swarm got loose and nested in a hollow there. I'd fetch them back, but my smoke kit's gone — somewhere in the tunnels under town, last I knew." She shrugs. "If you come across it."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```
