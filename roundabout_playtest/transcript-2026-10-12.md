# Roundabout.exe â€” Playtest Transcript

Each section is one launch of the game. Commands piped in are listed first, then the raw output.

## Launch 0 â€” first look
Commands: `look`
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

>
```

## Launch 1 â€” mailbox and surroundings
Commands: `open mailbox` `read leaflet` `inventory` `examine door` `help` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Please answer yes or no.
"Are you up for an adventure?" (yes/no) Please answer yes or no.
"Are you up for an adventure?" (yes/no) Please answer yes or no.
"Are you up for an adventure?" (yes/no) Please answer yes or no.
"Are you up for an adventure?" (yes/no) Traceback (most recent call last):
  File "main.py", line 22, in <module>
  File "main.py", line 16, in main
  File "engine\game.py", line 189, in run
  File "engine\game.py", line 229, in do_turn
  File "engine\game.py", line 302, in _dispatch
  File "engine\game.py", line 340, in perform
  File "engine\game.py", line 404, in _perform_chain
  File "content\verbs.py", line 44, in v_open
  File "content\char_create.py", line 140, in run_opening
  File "content\char_create.py", line 115, in _prompt_adventure
EOFError: EOF when reading a line
[PYI-32020:ERROR] Failed to execute script 'main' due to unhandled exception!
```

## Launch 2 â€” accepting the errand
Commands: `open mailbox` `yes` `Rowan` `` `` `` `` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.

[Press ENTER to continue] Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
"I have read destinies in the lines of a man's palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?"
Your choice (warrior/mage/rogue): Please choose warrior, mage, or rogue.
Your choice (warrior/mage/rogue): Please choose warrior, mage, or rogue.
Your choice (warrior/mage/rogue): Please choose warrior, mage, or rogue.
Your choice (warrior/mage/rogue): Please choose warrior, mage, or rogue.
Your choice (warrior/mage/rogue): Traceback (most recent call last):
  File "main.py", line 22, in <module>
  File "main.py", line 16, in main
  File "engine\game.py", line 189, in run
  File "engine\game.py", line 229, in do_turn
  File "engine\game.py", line 302, in _dispatch
  File "engine\game.py", line 340, in perform
  File "engine\game.py", line 404, in _perform_chain
  File "content\verbs.py", line 44, in v_open
  File "content\char_create.py", line 155, in run_opening
  File "content\char_create.py", line 126, in _prompt_class
EOFError: EOF when reading a line
[PYI-25144:ERROR] Failed to execute script 'main' due to unhandled exception!
```

## Launch 3 â€” class choice
Commands: `open mailbox` `yes` `` `rogue` `Rowan` `` `` `` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.

[Press ENTER to continue] Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
"I have read destinies in the lines of a man's palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?"
Your choice (warrior/mage/rogue): "A Rogue. Yes." He seems to find this amusing in a quiet way. "You know, I should have seen that. Something about the way you looked at the door when you came in." He shakes his head. "Pay attention to everything. You already know how. Just keep doing it."

You have chosen: Rogue
Hearts: 5  Starting skill: bow

"And your name?" 
Welcome, Rowan.

"There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem."

He stands and moves to the window.

"It fell through the roof of a man named Pyronicus. He's holding it in good faith, completely unaware of what it is. He'll give it up without a fight."

He turns back.

"I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."

[Press ENTER to continue] Almost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out. "Here," he says. "Ten Zenni. Don't spend it all on drinks."

"When you're ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.

> I beg your pardon?

> I beg your pardon?

> 
```

## Launch 4 â€” exploring the tower
Commands: `open mailbox` `yes` `` `rogue` `Rowan` `` `look` `examine painting` `examine music box` `inventory` `talk to will` `save` `` `quit` `y` `` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.

[Press ENTER to continue] Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
"I have read destinies in the lines of a man's palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?"
Your choice (warrior/mage/rogue): "A Rogue. Yes." He seems to find this amusing in a quiet way. "You know, I should have seen that. Something about the way you looked at the door when you came in." He shakes his head. "Pay attention to everything. You already know how. Just keep doing it."

You have chosen: Rogue
Hearts: 5  Starting skill: bow

"And your name?" 
Welcome, Rowan.

"There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem."

He stands and moves to the window.

"It fell through the roof of a man named Pyronicus. He's holding it in good faith, completely unaware of what it is. He'll give it up without a fight."

He turns back.

"I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."

[Press ENTER to continue] Almost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out. "Here," he says. "Ten Zenni. Don't spend it all on drinks."

"When you're ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.

> Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> "One more thing," Will says, rising from his chair. "The ring — I should have told you, it—"
The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You can't see any box here!

> You are empty-handed.
You have 10 Zenni.

> You can't see any will here!

> Saved.

> I beg your pardon?

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 5 â€” restore, tavern
Commands: `restore` `look` `examine mailbox` `talk to lynds` `` `` `` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> What does this look like? A Great Underground Empire?

> West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> There is a small mailbox here.

> You can't see any lynds here!

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> 
```

## Launch 6 â€” create then restore, tavern
Commands: `open mailbox` `yes` `` `rogue` `Rowan` `` `restore` `look` `examine mailbox` `talk to lynds` `` `` `` 
```
West of House
You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.

> The mailbox opens.
Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn't belong, and someone who is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."

"Are you up for an adventure?" (yes/no) Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.

[Press ENTER to continue] Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
"I have read destinies in the lines of a man's palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?"
Your choice (warrior/mage/rogue): "A Rogue. Yes." He seems to find this amusing in a quiet way. "You know, I should have seen that. Something about the way you looked at the door when you came in." He shakes his head. "Pay attention to everything. You already know how. Just keep doing it."

You have chosen: Rogue
Hearts: 5  Starting skill: bow

"And your name?" 
Welcome, Rowan.

"There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem."

He stands and moves to the window.

"It fell through the roof of a man named Pyronicus. He's holding it in good faith, completely unaware of what it is. He'll give it up without a fight."

He turns back.

"I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."

[Press ENTER to continue] Almost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out. "Here," he says. "Ten Zenni. Don't spend it all on drinks."

"When you're ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.

> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> A mailbox sits near the door, entirely out of place.

> Lynds looks at you the way a person looks at something they're about to do that they've done many times before. He sets his drink down and puts his elbow on the table.
"Go on then."
Lynds wins without apparent effort. He picks his drink back up. "Not bad." He means it as a compliment. "Come back whenever."

> I beg your pardon?

> I beg your pardon?

> I beg your pardon?

> 
```

## Launch 7 â€” tavern: mailbox, bar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open mailbox` `s` `look` `talk to bartender` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> You can't go that way.

> Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> You can't see any bartender here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 8 â€” tower again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to will passion` `ask will about ring` `x box` `x lacquered music box` `x desk` `open music box` `x painting` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> There's no response from the Will Passion.

> You can't see any ring here!

> I don't know the word "x".

> I don't know the word "x".

> I don't know the word "x".

> It's locked. There's a small keyhole in the front.

> I don't know the word "x".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 9 â€” tower examine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine music box` `examine desk` `examine papers` `examine will` `read papers` `take music box` `examine painting` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> A small lacquered music box, its lid locked tight. Will glances up from his papers. "That belonged to a student of mine. Bright. Restless. Never came back for it." He goes back to his writing, a little slower than before.

> You can't see any desk here!

> You can't see any papers here!

> Will Passion sits with the unhurried stillness of a man who has seen centuries compressed into a single lifetime.
His long dark robes of deep violet — trimmed in crimson cord that winds like a binding spell — hang loosely from broad, weathered shoulders.
His hair, dark as a raven's wing but streaked with the silver of hard-won wisdom, falls long and untamed past his shoulders.
His beard is full and commanding, the kind that seems to grow with intent.
Thin, almost delicate wire-rimmed spectacles rest upon his nose — an odd contrast to everything else about him, as if he borrowed them from a much more ordinary man.
On his wrist sits a leather cuff, dark and worn.
Around his neck, a crimson cord from which hangs... something. You can't quite make it out.

> You can't see any papers here!

> You can't take the music box.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 10 â€” tavern bar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `ask about pyronicus` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.
A woman behind the bar glances up as you come in — shoulder-length red hair, appraisal done in about a second, apparently satisfactory.
"New face," she says, not unkindly. "I'm May. Drinks are two Zenni, food's the same — keeps you on your feet longer than you'd think. Rooms are upstairs if you need to sleep it off properly."
She sets a glass down and leans one hand on the bar.
"If you get stuck on something and want a nudge in the right direction, money talks. Shamus is in the kitchen if you need supplies — he keeps more than recipes back there."
She picks the glass back up and goes back to work. The conversation is over when she decides it is.

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> That sentence isn't one I recognize.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 11 â€” board and May
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read board` `ask may about pyronicus` `ask may about ring` `talk to may` `buy drink` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Notices are pinned to the board, newer ones over older:
WANTED: someone to mend the old aqueduct beneath the town. The fountain's been dry for years. Drinks will be cheaper for it. — May
MISSING: a young man, last seen heading toward the dungeon. He may not be himself. If you find him, bring him out. Please.

> You can't see any pyronicus here!

> You can't see any ring here!

> She picks the glass back up and goes back to work. The conversation is over when she decides it is.

> May glances at you and sets the glass back down. "You don't need it. Come back when you do."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 12 â€” kitchen
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `talk to shamus` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Shamus wipes his hands on his apron. "What can I do for you?" He tips his head at the slate by the door. "Prices are up. Ask if you need something that isn't."
He glances at the pot on the fire and frowns at it. "There's a stew recipe I haven't made in years. Needs bog thyme, and a pot that isn't cracked. All of mine are."

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 13 â€” slate, buy
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read slate` `buy bow` `open cellar door` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
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

> You can't see any bow here!

> The cellar door is locked.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 14 â€” stew, buy torch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `ask shamus about stew` `ask about stew` `buy torch` `inventory` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> You can't see any stew here!

> That sentence isn't one I recognize.

> Shamus takes the Zenni and slides the torch across the counter. "Anything else?"

> You are carrying:
  Torch
You have 10 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 15 â€” dagger, upstairs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `buy dagger` `north` `north` `up` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Shamus takes the Zenni and slides the dagger across the counter. "Anything else?"
Shamus hands it over, then looks at the way you're holding it. "See the knight in the square before you swing that at anything."

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 16 â€” upstairs doors
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open door` `examine window` `look through window` `exits` `down` `out` `save` `quit` `yes`
```
> Restored.
Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> You can't see any door here!

> You can't see any window here!

> That sentence isn't one I recognize.

> I don't know the word "exits".

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 17 â€” leaving the tavern
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 18 â€” the knight
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to knight` `` `` `examine statue` `examine fountain` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> The Knight stands at ease in the square, watching the town go about its business. When he notices you, he turns fully to face you — unhurried, attentive. "You're looking at me like someone who wants to learn something," he says. "I teach one thing. Come find me when you're ready to show me what you already know."

> I beg your pardon?

> I beg your pardon?

> The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.

> You see nothing special about the fountain.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 19 â€” square exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `west` `west` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East
Main Street ends here, or nearly does. The buildings thin out toward the east — a few shuttered fronts, a sign that's lost its lettering, the church standing apart to the south as though it chose its distance deliberately. The wasteland begins where the cobblestones stop.

> Main East
Main Street ends here, or nearly does. The buildings thin out toward the east — a few shuttered fronts, a sign that's lost its lettering, the church standing apart to the south as though it chose its distance deliberately. The wasteland begins where the cobblestones stop.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West
Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley.

> Main West
Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 20 â€” archery range
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `talk to archer` `save` `quit` `yes`
```
> Restored.
Main West
Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley.

> Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
Raznak stands at the near end of the range, watching the targets.
An arrow from the far end of the range catches you. Someone shouts an apology in a language you don't speak.

> Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
Raznak stands at the near end of the range, watching the targets.

> Raznak eyes you the way he'd eye an arrow with a bad fletching — not hostile, just certain you're not ready.
"You want something from me, go talk to the encampment first. West of here. When they know you, come back."
He turns away. The conversation is over.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 21 â€” encampment
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `hearts` `west` `look` `save` `quit` `yes`
```
> Restored.
Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
Raznak stands at the near end of the range, watching the targets.

> I don't know the word "hearts".

> Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
"You want something from us. They always want something. Prove yourself. Talk to Haalvar — north. If you can satisfy him, come back."

> Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 22 â€” Haalvar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `status` `diagnose` `score` `north` `talk to haalvar` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> I don't know the word "status".

> You have 4 of 5 hearts.

> Score: 0
Level 1 (10 XP)
Zenni: 5
0 treasures on display.

> Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing.
Haalvar lounges beside the stone, looking pleased with himself.
Haalvar says: "I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"

> Haalvar says: "I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 23 â€” riddle
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `sea` `save` `quit` `yes`
```
> Restored.
Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing.
Haalvar lounges beside the stone, looking pleased with himself.

> The stone glows. Haalvar: "The stone is satisfied. I am also satisfied, which happens less often. Go south — there is a circle there that will want your attention next."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 24 â€” riddle attempts
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `say sea` `answer sea` `the sea` `say the sea` `save` `quit` `yes`
```
> Restored.
Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing.
Haalvar lounges beside the stone, looking pleased with himself.

> I don't know the word "say".

> I don't know the word "answer".

> I don't know the word "sea".

> I don't know the word "say".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 25 â€” ring of stones
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `look` `save` `quit` `yes`
```
> Restored.
Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing.
Haalvar lounges beside the stone, looking pleased with himself.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 26 â€” circle
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to child` `examine stones` `examine symbol` `examine heart stone` `examine child` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> The child says nothing.

> You can't see any stones here!

> You can't see any symbol here!

> You see nothing special about the heart stone.

> A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 27 â€” circle actions
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine air stone` `touch heart stone` `enter circle` `touch air stone` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You see nothing special about the air stone.

> Fiddling with the heart stone has no effect.

> You can't see any circle here!

> Fiddling with the air stone has no effect.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 28 â€” circle more
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `push air stone` `in` `wait` `examine earth stone` `examine fire stone` `examine water stone` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Pushing the air stone has no effect.

> You can't go that way.

> Time passes...

> You see nothing special about the earth stone.

> You see nothing special about the fire stone.

> You see nothing special about the water stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 29 â€” Ivanaar, fire pit
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `talk to ivanaar` `west` `look` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> "Haalvar speaks well of you. That's not nothing. The circle is south."

> The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora sits by the fire, a cup in hand.

> The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora sits by the fire, a cup in hand.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 30 â€” Aylora
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to aylora` `` `` `examine barrel` `save` `quit` `yes`
```
> Restored.
The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora sits by the fire, a cup in hand.

> Aylora looks you over and doesn't reach for the barrel. "Haalvar's stone and the circle first," she says. "I don't waste Thornbrew on strangers."

> I beg your pardon?

> I beg your pardon?

> You can't see any barrel here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 31 â€” buying a hint
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `east` `east` `south` `south` `buy hint` `ask may for hint` `pay may` `save` `quit` `yes`
```
> Restored.
The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora sits by the fire, a cup in hand.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow from the far end of the range catches you. Someone shouts an apology in a language you don't speak.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> You can't see any hint here!

> That sentence isn't one I recognize.

> May waits. "How much?"

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 32 â€” paying May
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `diagnose` `pay may` `2` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> You have 3 of 5 hearts.

> May waits. "How much?"

> I don't know the word "2".

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 33 â€” paying May, phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pay may 2 zenni` `give 2 zenni to may` `pay 2 zenni` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.
"The Keeper of the Faiths has gone missing. No one's seen him in some time."

> May looks at the coin and shakes her head slowly. "I'd be robbing you. Ask me again when something changes."

> You can't see any zenni here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 34 â€” drink, town hall
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `buy drink` `diagnose` `north` `north` `north` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> May sets a glass on the bar and fills it without being asked what you want. Two Zenni.

> You have 4 of 5 hearts.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above.

> Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 35 â€” Town Hall rooms
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `east` `east` `look` `save` `quit` `yes`
```
> Restored.
Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above.

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Town Hall

> Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 36 â€” council and clerk
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to man` `talk to mayor` `west` `west` `talk to clerk` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> He looks up from his papers with the expression of someone who has been interrupted before and expects to be interrupted again. "Can I help you?" It is not entirely a question.

> You can't see any mayor here!

> Town Hall

> Records Room

> The clerk doesn't put down his pen. "If you're here about the charter, the answer is no. It's the town's only copy, and the town isn't in the habit of lending it to strangers." He goes back to his ledger.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 37 â€” Town Hall upstairs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `up` `look` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Town Hall

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 38 â€” display cabinet
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open cabinet` `look in cabinet` `examine cabinet` `save` `quit` `yes`
```
> Restored.
Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> The glass door swings open on a stiff hinge. Among the yellowed charters and a tarnished civic medal sits a wax seal — a disc of old red wax, stamped with the town crest.

> A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 39 â€” take seal
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take seal` `take medal` `take charters` `inventory` `save` `quit` `yes`
```
> Restored.
Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.
A wax seal sits among the documents in the open cabinet.

> You take the wax seal.

> You can't see any medal here!

> You can't see any charters here!

> You are carrying:
  Torch
  Dagger
  Wax seal
You have 1 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 40 â€” library
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `south` `south` `west` `north` `look` `save` `quit` `yes`
```
> Restored.
Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You can't go that way.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 41 â€” library
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 42 â€” librarian
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to librarian` `` `` `search catalogue` `examine catalogue` `save` `quit` `yes`
```
> Restored.
Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

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

> You can't see any catalogue here!

> You can't see any catalogue here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 43 â€” library details
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine card catalogue` `read ledger` `examine librarian` `examine shelves` `north` `look` `save` `quit` `yes`
```
> Restored.
Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> You can't see any catalogue here!

> You can't see any ledger here!

> You see nothing special about the librarian.

> You can't see any shelves here!

> You can't go that way.

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 44 â€” library exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `west` `up` `down` `save` `quit` `yes`
```
> Restored.
Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> The Stacks
The passage from the Main Hall opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Library — Main Hall

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 45 â€” Archivist
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `talk to archivist` `` `` `examine maps` `save` `quit` `yes`
```
> Restored.
Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> The Stacks

> He looks up when spoken to, marking his place with two fingers before setting the book aside.
"Yes. I've been trying to authenticate a map — provenance is unclear, which makes it nearly useless for the purpose I need it for. There's an engraving in the lower passages that should settle the question, if I could get a clean impression of it."
He glances at the table, then back.
"I can't leave this. If you're heading down that way — thin paper, a stick of charcoal, and some patience. The engraving is in the Inscription Chamber. You'll know it when you see it."

> I beg your pardon?

> I beg your pardon?

> You can't see any maps here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 46 â€” alley
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `southeast` `look` `save` `quit` `yes`
```
> Restored.
The Stacks
The passage from the Main Hall opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Library — Main Hall

> Main West

> You hear music — a familiar melody. You have reached level 2!
The Alley
The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.

> The Alley
The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 47 â€” deep alley
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
The Alley
The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.

> The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A figure waits in the shadow of the crates, very still, weight on the balls of their feet. They've seen you see them. There's a cudgel in one hand — this is the alley's mugger, and they mean business.

> The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A figure waits in the shadow of the crates, very still, weight on the balls of their feet. They've seen you see them. There's a cudgel in one hand — this is the alley's mugger, and they mean business.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 48 â€” mugger talk
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to mugger` `` `` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A figure waits in the shadow of the crates, very still, weight on the balls of their feet. They've seen you see them. There's a cudgel in one hand — this is the alley's mugger, and they mean business.

> There's no response from the mugger.

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 49 â€” crates, fight
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `search crates` `examine barrels` `attack mugger with dagger` `diagnose` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A figure waits in the shadow of the crates, very still, weight on the balls of their feet. They've seen you see them. There's a cudgel in one hand — this is the alley's mugger, and they mean business.

> You can't see any crates here!

> You can't see any barrels here!

> You trade blows. Both of you feel it.

> You have 3 of 5 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 50 â€” fight on
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `attack mugger with dagger` `diagnose` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A figure waits in the shadow of the crates, very still, weight on the balls of their feet. They've seen you see them. There's a cudgel in one hand — this is the alley's mugger, and they mean business.

> You land a solid blow. The mugger staggers.
The mugger goes down and doesn't get up. Something clatters to the cobbles beside them — a roll of lockpicks.

> You have 3 of 5 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 51 â€” loot
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take lockpicks` `search mugger` `inventory` `score` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.
A roll of lockpicks lies on the cobbles.

> You take the lockpicks.

> You can't see any mugger here!

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
You have 4 Zenni.

> Score: 0
Level 2 (32 XP)
Zenni: 4
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 52 â€” cellar lock
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `northwest` `east` `south` `south` `south` `pick lock` `unlock cellar door with lockpicks` `save` `quit` `yes`
```
> Restored.
The Back Alley
Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.

> The Alley

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> This lock can't be picked.

> You don't have the key to it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 53 â€” paper, music box
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `buy thin paper` `north` `north` `open mailbox` `pick lock` `unlock music box with lockpicks` `open music box` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Shamus takes the Zenni and slides the thin paper across the counter. "Anything else?"

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
You notice a door to the north you hadn't seen before.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> You already have the lockpicks.

> It's locked. There's a small keyhole in the front.

> It's locked. There's a small keyhole in the front.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 54 â€” box, north door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pick music box` `pick lock on music box` `north` `look` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> You can't pick that.

> That sentence isn't one I recognize.

> You push open the bedroom door and step inside.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.

> Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 55 â€” glasses
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine glasses` `take glasses` `wear glasses` `look` `examine bed` `look under bed` `save` `quit` `yes`
```
> Restored.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.

> Wire-rimmed glasses, the lenses a little smudged. They look perfectly ordinary.

> You take the wire-rimmed glasses.

> You put on the wire-rimmed glasses.

> Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.

> Narrow, and made with the perfunctory neatness of someone who knows they'll be up again soon.

> Nothing under the bed but dust and a sock that has given up.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 56 â€” glasses in tower
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `examine will` `examine music box` `examine nightstand` `save` `quit` `yes`
```
> Restored.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.

> Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.
Will looks up from his desk. His eyes go to the glasses on your face and stay there. For a moment nothing in the room moves. Then he is out of his chair, and whatever happens next, you don't see it coming.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 57 â€” after death: return glasses
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove glasses` `drop glasses` `inventory` `look` `save` `quit` `yes`
```
> Restored.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.

> Wire-rimmed glasses removed.

> You set the glasses back on the nightstand, where they were.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
You have 10 Zenni.

> Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses rests on the nightstand.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 58 â€” to the church
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take candle` `south` `examine painting` `north` `east` `south` `look` `save` `quit` `yes`
```
> Restored.
Will Passion's Bedroom
This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant.
Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing.
A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon.
A nightstand holds a half-melted candle and a ring left by a cup that was never there long enough to matter.
The rest of the room is Will's business and clearly has been for a very long time.
A pair of wire-rimmed glasses rests on the nightstand.

> You can't see any candle here!

> Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 59 â€” church dial and door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine dial` `examine altar` `examine door` `pick lock` `unlock door with lockpicks` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> You can't see any dial here!

> You can't see any altar here!

> You see nothing special about the narrow door.

> This lock can't be picked.

> That key doesn't fit.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 60 â€” dial phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine brass dial` `turn dial` `examine stone altar` `examine marks` `look at dial` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> You can't see any dial here!

> You can't see any dial here!

> You can't see any altar here!

> You can't see any marks here!

> You can't see any dial here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 61 â€” church other
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pray` `examine pews` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> You bow your head. The church receives it the way it receives everything — without asking which god it was meant for.

> You can't see any pews here!

> Main East

> You hear music — a familiar melody. You have reached level 3!
Roundabout Wasteland
The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently.
The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly.
To the south, a volcano rises against the sky — large, dark, and entirely convincing.

> Roundabout Wasteland
The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently.
The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly.
To the south, a volcano rises against the sky — large, dark, and entirely convincing.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 62 â€” volcano
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine structures` `south` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Wasteland
The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently.
The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly.
To the south, a volcano rises against the sky — large, dark, and entirely convincing.

> You can't see any structures here!

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 63 â€” descending
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `light torch` `down` `look` `save` `quit` `yes`
```
> Restored.
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> It's already lit.

> Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 64 â€” Pyronicus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to pyronicus` `` `` `` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 65 â€” the ring
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine ring` `inventory` `examine forge` `talk to pyronicus` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> A plain dark ring.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
You have 13 Zenni.

> You see nothing special about the forge.

> He goes back to what he was doing. The conversation, apparently, is over.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 66 â€” charcoal, return
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take charcoal` `take coal` `up` `north` `west` `west` `south` `open mailbox` `give ring to will` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> You can't see any charcoal here!

> You can't see any coal here!

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
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 67 â€” church dial again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `inventory` `examine painting` `north` `east` `south` `examine dial` `turn dial` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
You have 13 Zenni.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> You can't see any dial here!

> You can't see any dial here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 68 â€” May hint 2
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `west` `south` `south` `pay may 2 zenni` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May pushes the Zenni back. "Keep it. I've got nothing worth that right now." She goes back to wiping the bar.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 69 â€” knight again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `talk to knight` `show ring to knight` `examine knight` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> The Knight stands at ease in the square, watching the town go about its business. When he notices you, he turns fully to face you — unhurried, attentive. "You're looking at me like someone who wants to learn something," he says. "I teach one thing. Come find me when you're ready to show me what you already know."

> I don't know the word "show".

> A tall man in plain, well-kept armour, a red cross faded on the breast. He wears his sword like a tool he respects. His eyes are calm, and they miss very little.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 70 â€” spar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `spar with knight` `train with knight` `ask knight about faith` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> I don't know the word "spar".

> I don't know the word "train".

> You can't see any faith here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 71 â€” cellar key
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `ask may for key` `ask may about cellar` `talk to may` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> That sentence isn't one I recognize.

> You can't see any cellar here!

> May glances up. "Heard the back alley's gone quiet." She sets a glass on the bar. "That one's on the house."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 72 â€” back to circle
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `diagnose` `north` `north` `west` `west` `west` `south` `talk to child` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> You have 5 of 6 hearts.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Ritual Circle
A child stands at the edge of the circle, watching you without a word.

> The child says nothing.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 73 â€” circle offerings
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine carved symbol` `give paper to child` `put ring on heart stone` `heart` `inventory` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You can't see any symbol here!

> The child doesn't take the thin paper.

> "Bring it to me, or keep it close," Will said. You keep it close.

> There was no verb in that sentence!

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
You have 13 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 74 â€” wearing the ring
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear ring` `look` `examine heart stone` `talk to child` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You see nothing special about the heart stone.

> The child says nothing.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 75 â€” invisible at the bar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `east` `east` `east` `south` `south` `look` `take key` `steal key` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar
The ring is warm. You hadn't noticed until just now. You're not sure when it started.

> Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> You can't see any key here!

> I don't know the word "steal".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 76 â€” invisible charter
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `west` `look` `take charter` `remove ring` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> You can't see any charter here!

> Plain dark ring removed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 77 â€” wasteland edges
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `south` `east` `east` `north` `east` `south` `west` `east` `down` `down` `north` `east` `west` `south` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> You can't go that way.

> Beach Road
A road that forks — south toward Roundabout Beach, north toward Roundabout Forest via The Old Oak.

> Roundabout Beach
Roundabout Beach opens up as the town falls behind you — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> You can't go that way.

> The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it.
A coil of rope sits loose on a bollard.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> A Pie Rat on deck looks you over with the thoroughness of someone whose job is exactly this. "You don't even look like a pirate." He doesn't move. Neither, apparently, will you.

> Roundabout Beach

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 78 â€” rope, forest
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `take rope` `west` `north` `north` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Beach
Roundabout Beach opens up as the town falls behind you — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull.

> The Docks
A coil of rope sits loose on a bollard.

> You take the coil of rope.

> Roundabout Beach

> Beach Road

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. A kite is tangled in its upper branches. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. A kite is tangled in its upper branches. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 79 â€” kite
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to child` `climb oak` `take kite` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. A kite is tangled in its upper branches. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.

> "It's stuck," the child says, pointing up. As if you might not have noticed.

> You haul yourself up through the branches and work the kite loose. Something comes free with it — a small flat stone on a cord, tangled in the line. It drops into the grass below.

> You already have the kite.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 80 â€” return kite
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `take stone` `examine stone` `give kite to child` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
A child stands under the oak, staring up at the kite with the patience of someone who has been at it a while.
A small flat stone on a cord lies in the grass.

> You can't go that way.

> You take the flat rune stone.

> A small flat stone, dark and smooth, threaded on a cord. Mineral veins run through it in a pattern that looks almost intentional.

> The child takes the kite in both hands, inspects it for damage, finds none worth mentioning, and runs off to try again.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 81 â€” cottage
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.
"You'll want to keep clear of the tree east of the oak," she says, before you've said anything. "Swarm got loose and nested in a hollow there. I'd fetch them back, but my smoke kit's gone — somewhere in the tunnels under town, last I knew." She shrugs. "If you come across it."

> Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 82 â€” forest
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `north` `look` `north` `look` `save` `quit` `yes`
```
> Restored.
Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> You can't go that way.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 83 â€” shrine and mine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take shard` `examine shrine` `enter mine` `down` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.
Among the shards on the pedestal, one piece is larger than the rest — a curved section of the rim, still whole.

> You take the large bowl piece.

> You see nothing special about the pedestal.

> You can't see any mine here!

> Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY.

> Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 84 â€” into the mine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `look` `north` `look` `save` `quit` `yes`
```
> Restored.
Mine Entrance
The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals. The smell of rock dust and old torchsmoke is thick here.
A pickaxe leans against the wall.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals. The smell of rock dust and old torchsmoke is thick here.
A pickaxe leans against the wall.

> You can't go that way.

> Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals. The smell of rock dust and old torchsmoke is thick here.
A pickaxe leans against the wall.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 85 â€” pickaxe, deeper
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take pickaxe` `down` `look` `save` `quit` `yes`
```
> Restored.
Main Shaft
The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals. The smell of rock dust and old torchsmoke is thick here.
A pickaxe leans against the wall.

> You take the pickaxe.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
One of the timber supports has split along the grain, and the rock above it sags. If anything in this mine wanted to come down, it would start there.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 86 â€” tunnel branches
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `south` `east` `west` `down` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> The Rat's Nest
A widening in the tunnel that someone has decided is a room. Crates and barrels are stacked with more care than the surroundings suggest — this is storage, not clutter. The Pie Rats keep their surplus here.
A Pie Rat disguise sits among the contraband.

> Mine Tunnels
A split timber support sags under the rock above it.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 87 â€” disguise
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `take disguise` `examine crates` `search barrels` `south` `examine support` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> The Rat's Nest
A Pie Rat disguise sits among the contraband.

> You take the Pie Rat disguise.

> You can't see any crates here!

> You can't see any barrels here!

> Mine Tunnels
A split timber support sags under the rock above it.

> A split timber support sags under the rock above it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 88 â€” to the ship
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `up` `south` `south` `south` `east` `wear disguise` `east` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Main Shaft

> Mine Entrance

> Roundabout Forest

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Beach

> The Docks

> You put on the Pie Rat disguise.

> The Pie Rat at the gangplank squints at your coat, then at you. "Crew's all aboard. Don't know you." He doesn't move.

> The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 89 â€” Pie Rat guard
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `inventory` `talk to pie rat` `talk to pirate` `talk to guard` `save` `quit` `yes`
```
> Restored.
The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Flat rune stone
  Large bowl piece
  Pickaxe
  Pie Rat disguise (being worn)
You have 19 Zenni.

> You can't see any rat here!

> You can't see any pirate here!

> You can't see any guard here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 90 â€” statue
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove disguise` `west` `north` `west` `west` `west` `pry statue with pickaxe` `open statue with pickaxe` `save` `quit` `yes`
```
> Restored.
The Docks
The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it.

> Pie Rat disguise removed.

> Roundabout Beach

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You can't get any leverage on that.

> The base is sealed tight. Something with leverage could pry it open.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 91 â€” rune stone at circle
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `west` `west` `south` `give rune stone to child` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Ritual Circle
A child stands at the edge of the circle, watching you without a word.

> Which stone do you mean, the flat rune stone, the earth stone, the air stone, the fire stone, the water stone, or the heart stone?

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 92 â€” flat rune stone
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `give flat rune stone to child` `look` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> The child doesn't take the flat rune stone.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 93 â€” rune stone use
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear flat rune stone` `look` `put flat rune stone on heart stone` `drop flat rune stone` `look` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You can't wear the flat rune stone.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> You can't put the flat rune stone on the heart stone.

> You drop the flat rune stone.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.
There is a flat rune stone here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 94 â€” rune stone to Vikings
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take flat rune stone` `north` `give flat rune stone to ivanaar` `north` `give flat rune stone to haalvar` `talk to haalvar` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.
There is a flat rune stone here.

> You take the flat rune stone.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Ivanaar turns the stone over once and hands it back. "Three," he says, and returns to his fire.

> Haalvar's Hut
Haalvar lounges beside the stone, looking pleased with himself.

> Haalvar doesn't take the flat rune stone.

> "Go south — there is a circle there that will want your attention next."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 95 â€” Raznak again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `talk to raznak` `diagnose` `save` `quit` `yes`
```
> Restored.
Haalvar's Hut
The hut is close and warm and smells of tallow. In the center sits a stone carved with runes — solid to the touch, but its surface moves like dark water, as if something underneath is breathing.
Haalvar lounges beside the stone, looking pleased with himself.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Raznak eyes you the way he'd eye an arrow with a bad fletching — not hostile, just certain you're not ready.
"You want something from me, go talk to the encampment first. West of here. When they know you, come back."
He turns away. The conversation is over.

> You have 5 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 96 â€” Lynds rematch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `south` `talk to lynds` `arm wrestle lynds` `save` `quit` `yes`
```
> Restored.
Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Lynds looks at you the way a person looks at something they're about to do that they've done many times before. He sets his drink down and puts his elbow on the table.
"Go on then."
Lynds wins without apparent effort. He picks his drink back up. "Not bad." He means it as a compliment. "Come back whenever."

> "Give me a bit. I'm still drinking."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 97 â€” humming tree
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `east` `east` `east` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.
The swarm boils out of the hollow before you can do anything useful. You retreat.
The Old Oak
The child is flying the kite in the clearing, badly and happily.

> The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 98 â€” Tip Journal
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `west` `west` `south` `south` `south` `buy tip journal` `read tip journal` `save` `quit` `yes`
```
> Restored.
The Old Oak
A large oak dominates the clearing, old enough to have opinions. The forest begins to the north; Beach Road runs south. A cottage sits off to the west, and to the east a broad old tree hums faintly.
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus takes the Zenni and slides the Tip Journal across the counter. "Anything else?"

> JOURNAL

The Locked Music Box       [Organic]

The Ruined Aqueduct        [Board]

The Lost Apprentice        [Board]

Shamus's Recipe            [Organic]

The Hollow Statue          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.

The Undead Warden          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.

The Viking Trust Trials    [Organic]

The Archivist's Request    [Organic]

Fight the Knight           [Organic]

The Beekeeper's Swarm      [Organic]

The Ruined Shrine          [Organic]

Beat Lynds                 [Organic]

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 99 â€” fight the knight
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `fight knight` `diagnose` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> "I'm Rowan, and I'm ready."

He looks at you. Something in his posture shifts — just slightly. "Then let's see what you know." He draws his weapon.

> You have 4 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 100 â€” knight duel
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `attack knight with dagger` `diagnose` `attack knight with dagger` `diagnose` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You get inside his guard and land a clean blow. He gives ground, nodding.

> You have 4 of 6 hearts.

> You get inside his guard and land a clean blow. He gives ground, nodding.

> You have 4 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 101 â€” knight duel cont.
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `attack knight with dagger` `attack knight with dagger` `attack knight with dagger` `diagnose` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You trade blows, and both of you land one.
He holds still for a moment after you land the deciding blow. Then something in his posture shifts — subtle, but real. "Good, Rowan," he says. Just that. He sheathes his weapon and nods toward an open space in the square. "Again — this time I'll show you what you did right."

> "Three Zenni, Rowan, and I'll show you what you did right."

> "Three Zenni, Rowan, and I'll show you what you did right."

> You have 3 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 102 â€” knight training
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pay knight 3 zenni` `` `score` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> He walks you through it twice, slowly, then once at speed: your footing, your guard, where your weight goes when you swing. By the end your arms ache, and something has settled into them that wasn't there before.
"Shamus, at the inn, keeps weapons in the back. Tell him I sent you."

> I beg your pardon?

> Score: 0
Level 3 (71 XP)
Zenni: 11
0 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 103 â€” Shamus weapons
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `talk to shamus` `` `` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus wipes his hands on his apron. "What can I do for you?" He tips his head at the slate by the door. "Prices are up. Ask if you need something that isn't."
He glances at the pot on the fire and frowns at it. "There's a stew recipe I haven't made in years. Needs bog thyme, and a pot that isn't cracked. All of mine are."

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 104 â€” slate again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read slate` `tell shamus about knight` `ask shamus about weapons` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... (sold)
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... (sold)
  Dagger .......... (sold)
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds.

> You can't see any knight here!

> You can't see any weapons here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 105 â€” probing exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `east` `east` `east` `north` `north` `west` `east` `east` `south` `south` `west` `south` `east` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> You can't go that way.

> You can't go that way.

> You can't go that way.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> The Volcano

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 106 â€” digging in the mine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `east` `north` `north` `down` `down` `down` `dig` `dig with pickaxe` `look` `save` `quit` `yes`
```
> Restored.
The Volcano
The volcano fills the sky above you — black rock streaked with old flows, a thread of smoke rising from the summit, heat rolling down the slope in slow waves. It is large, dark, and entirely convincing. There is no way in that you can see.
Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark.

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> Mine Entrance

> Main Shaft

> Mine Tunnels
A split timber support sags under the rock above it.

> There's nothing here worth digging for.

> There's nothing here worth digging for.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 107 â€” the split support
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `hit support with pickaxe` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> You can't fight the split timber support.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 108 â€” support again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `break support` `push support` `kick support` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Nice try.

> Pushing the split timber support has no effect.

> Kicking the split timber support has no obvious effect.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 109 â€” probing town interiors
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `up` `south` `east` `east` `east` `west` `west` `west` `south` `north` `north` `west` `east` `south` `east` `north` `east` `south` `north` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Main Shaft

> Mine Entrance

> Roundabout Forest

> The Old Oak
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
Your last heart gives out. The dark closes in, and this time it keeps you.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 110 â€” after bee death: to tavern upstairs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `diagnose` `up` `up` `up` `south` `south` `west` `west` `west` `south` `up` `north` `east` `west` `south` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> You have 3 of 6 hearts.

> Main Shaft

> Mine Entrance

> Roundabout Forest

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Upstairs Hall

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 111 â€” sleep
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `sleep` `diagnose` `save` `quit` `yes`
```
> Restored.
Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> I don't know the word "sleep".

> You have 3 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 112 â€” seal to clerk
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `south` `buy food` `north` `north` `north` `west` `give seal to clerk` `talk to clerk` `save` `quit` `yes`
```
> Restored.
Upstairs Hall
The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May calls back to the kitchen and a plate appears shortly after. She sets it in front of you. "Two Zenni."

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> The clerk doesn't take the wax seal.

> The clerk doesn't put down his pen. "If you're here about the charter, the answer is no. It's the town's only copy, and the town isn't in the habit of lending it to strangers." He goes back to his ledger.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 114 â€” (dev hints received) banner
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `diagnose` `inventory` `east` `south` `west` `west` `west` `examine banner` `read banner` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> You have 4 of 6 hearts.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
You have 9 Zenni.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.
An arrow hisses past, close enough to hear the fletching.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> Four runes are stitched along the banner, left to right: Earth, Air, Fire, Water.

> There's nothing written on the banner.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 115 â€” activating the circle
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `activate earth stone` `activate air stone` `activate fire stone` `activate water stone` `activate heart stone` `look` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Ritual Circle
A child stands at the edge of the circle, watching you without a word.

> The Earth stone hums and lights from within.

> The Air stone hums and lights from within.

> The Fire stone hums and lights from within.

> The Water stone hums and lights from within.

> The Heart stone hums and lights from within.
The fifth stone lights, and all five hum together for a moment. The child looks at you, then points back toward the encampment.

> The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 116 â€” Aylora
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `talk to ivanaar` `west` `talk to aylora` `` `` `save` `quit` `yes`
```
> Restored.
The Ritual Circle
Five rune stones stand in a ring around a carved symbol in the earth: Air, Earth, Fire, Water, and one marked with a heart. The ground inside the ring is swept clean.
A child stands at the edge of the circle, watching you without a word.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> "Two down. The fire pit is west. Don't embarrass yourself."

> The Fire Pit
Aylora sits by the fire, a cup in hand.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Aylora sets two cups on the bench and fills them from the barrel. "Thornbrew," she says. "Five cups. Last one standing." She pushes one toward you.

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 117 â€” Thornbrew
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drink cup` `drink` `drink thornbrew` `diagnose` `save` `quit` `yes`
```
> Restored.
The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora sits by the fire, a cup in hand.

> You can't see any cup here!

> You drain the cup. Aylora matches you, but slower.
You drain the cup. Aylora matches you, but slower.
You drain the cup. Aylora matches you, but slower.
Aylora sets down her cup with great care, looks at it, and slides gently off the bench. Aylora passes out.
A nearby Viking stares at her, then at you. "Ivanaar won't believe that unless he sees it."

> You can't see any thornbrew here!

> You have 4 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 118 â€” Ivanaar's verdict
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `talk to ivanaar` `` `` `inventory` `save` `quit` `yes`
```
> Restored.
The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora is slumped on the bench, snoring.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> "You're standing. That's something. But Aylora's not here to tell me how it went — and I'll believe it when I see it."

> I beg your pardon?

> I beg your pardon?

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
You have 12 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 119 â€” proof for Ivanaar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `wake aylora` `take aylora` `carry aylora` `take cup` `examine aylora` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.

> The Fire Pit
Aylora is slumped on the bench, snoring.

> I don't know the word "wake".

> You get her under the arms and start to drag.

> You get her under the arms and start to drag.

> You can't see any cup here!

> Aylora is slumped on the bench, snoring.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 120 â€” dragging Aylora
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `talk to ivanaar` `` `` `save` `quit` `yes`
```
> Restored.
The Fire Pit
A great fire burns in a stone-lined pit, benches drawn up close around it. Cups, a barrel, and a smell that could strip paint. This is where the encampment settles its arguments.
Aylora is slumped on the bench, snoring.

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
You hear music — a familiar melody. You have reached level 4!

> Ivanaar returns to his fire.

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 121 â€” Raznak
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `talk to raznak` `` `` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 122 â€” gunpowder, Pyronicus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `south` `south` `south` `buy gunpowder` `north` `north` `north` `east` `east` `south` `down` `give runed metal to pyronicus` `` `` `save` `quit` `yes`
```
> Restored.
Archery Range
Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used.
The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus takes the Zenni and slides the gunpowder across the counter. "Anything else?"

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> The Volcano

> Pyronicus's Forge
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.
Something catches your eye, tucked out of sight: 5 Zenni. You pocket them.

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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 123 â€” to the support
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `north` `east` `north` `north` `down` `down` `down` `put gunpowder on support` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> The Volcano

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> Mine Entrance

> Main Shaft

> Mine Tunnels
A split timber support sags under the rock above it.

> You can't put the gunpowder on the split timber support.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 124 â€” gunpowder phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `use gunpowder on support` `blow up support` `light gunpowder` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> Nothing happens.

> You can't blast anything by using words.

> Not while you're holding it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 125 â€” the blast
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop gunpowder` `light gunpowder` `look` `diagnose` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.

> You wedge the gunpowder in against the split timber.

> You bring the torch close and think better of it. An open flame and loose powder — it'd go up in your hand. A fuse wants a spark.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> You have 4 of 6 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 126 â€” making a spark
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `strike pickaxe` `shoot gunpowder` `light gunpowder with torch` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> That's not something I know how to strike.

> You can't fight the gunpowder.

> You bring the torch close and think better of it. An open flame and loose powder — it'd go up in your hand. A fuse wants a spark.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 127 â€” rope fuse
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `tie rope to gunpowder` `put rope on gunpowder` `light rope` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> There's nothing here to tie it to.

> You can't put the coil of rope on the gunpowder.

> You can't light the coil of rope.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 128 â€” bow and throw
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `shoot gunpowder with bow` `throw torch at gunpowder` `look` `inventory` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> You can't fight the gunpowder.

> You'd rather keep hold of the torch.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
You have 17 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 129 â€” tip May
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `up` `south` `south` `west` `west` `west` `south` `south` `tip may 2` `tip may 5` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Main Shaft

> Mine Entrance

> Roundabout Forest

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.
"Bees aren't aggressive by nature — beekeepers have known for centuries how to calm them. Something about smoke. Ask me why it works and I couldn't tell you, but it does."

> May pockets the coins carefully. "That buys you something worth hearing," she says.
"There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 130 â€” bigger tip
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `tip may 10` `read tip journal` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> May counts the coins once, pockets them, and leans all the way across the bar. "Rowan," she says.
"No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew."

> JOURNAL

The Locked Music Box       [Organic]

The Ruined Aqueduct        [Board]

The Lost Apprentice        [Board]

Shamus's Recipe            [Organic]

The Hollow Statue          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.
  Tip: There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it.
  Tip: No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew.

The Undead Warden          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.
  Tip: There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it.
  Tip: No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew.

The Archivist's Request    [Organic]

The Beekeeper's Swarm      [Organic]
  Tip: Bees aren't aggressive by nature — beekeepers have known for centuries how to calm them. Something about smoke. Ask me why it works and I couldn't tell you, but it does.

The Ruined Shrine          [Organic]

Beat Lynds                 [Organic]

The Brotherhood Stones     [Organic]

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 131 â€” Lynds lvl 4, statue tools
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `talk to lynds` `north` `pry statue with pale blade` `pry statue with dagger` `pry statue with bow` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Lynds looks at you the way a person looks at something they're about to do that they've done many times before. He sets his drink down and puts his elbow on the table.
"Go on then."
Lynds wins without apparent effort. He picks his drink back up. "Not bad." He means it as a compliment. "Come back whenever."

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You can't get any leverage on that.

> You can't get any leverage on that.

> You can't get any leverage on that.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 132 â€” beach dig, forge spark
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `east` `south` `dig` `search sand` `north` `west` `south` `down` `ask pyronicus about spark` `take ember` `take flint` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> Roundabout Beach

> There's nothing here worth digging for.

> You can't see any sand here!

> Beach Road

> Roundabout Wasteland

> The Volcano

> Pyronicus's Forge
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> You can't see any spark here!

> You can't see any ember here!

> You can't see any flint here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 133 â€” bowl to Pyronicus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `give bowl piece to pyronicus` `talk to pyronicus` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus doesn't take the large bowl piece.

> He goes back to what he was doing. The conversation, apparently, is over.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 134 â€” (dev hint: assay room) Main Shaft south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `north` `east` `north` `north` `down` `down` `south` `look` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> The Volcano

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> Mine Entrance

> Main Shaft

> Assay Room
A side room off the main shaft, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.
A flint and steel striker lies on the workbench among the crucibles.
Looking closer, the gap in the far wall goes further back than it should — a rough passage, just wide enough to squeeze through, running east into the dark.

> Assay Room
A side room off the main shaft, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.
A flint and steel striker lies on the workbench among the crucibles.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 135 â€” striker, east passage
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take striker` `east` `look` `save` `quit` `yes`
```
> Restored.
Assay Room
A side room off the main shaft, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.
A flint and steel striker lies on the workbench among the crucibles.

> You take the flint and steel.

> Hidden Secondary Entrance
The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.
The torch catches the dark and pushes it back. Good thinking, getting one of these.

> Hidden Secondary Entrance
The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 136 â€” tunnel network
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `look` `save` `quit` `yes`
```
> Restored.
Hidden Secondary Entrance
The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.

> You can't go that way.

> Hidden Secondary Entrance
The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 137 â€” finding the way on
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
Hidden Secondary Entrance
The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine.

> The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 138 â€” Forgotten Shaft exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `north` `south` `down` `save` `quit` `yes`
```
> Restored.
The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine.

> You can't go that way.

> You can't go that way.

> The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 139 â€” Undercroft mapping
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `east` `west` `east` `south` `north` `down` `up` `save` `quit` `yes`
```
> Restored.
The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling.

> The Forgotten Shaft

> You can't go that way.

> Hidden Secondary Entrance

> The Forgotten Shaft

> The Undercroft

> The Forgotten Shaft

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 140 â€” Undercroft exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `look` `save` `quit` `yes`
```
> Restored.
The Forgotten Shaft
The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. To the west, a rougher passage breaks off and climbs toward the mine.

> The Undercroft

> You can't go that way.

> The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 141 â€” Undercroft south/west
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
The Undercroft
A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling.

> The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways. The one to the east runs back toward the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways. The one to the east runs back toward the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 142 â€” Undercroft west
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `save` `quit` `yes`
```
> Restored.
The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways. The one to the east runs back toward the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> You can't go that way.

> The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways. The one to the east runs back toward the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 143 â€” toward the cellar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
The Junction
The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch three ways. The one to the east runs back toward the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 144 â€” black oak door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine door` `open door` `east` `save` `quit` `yes`
```
> Restored.
The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> You see nothing special about the black oak door.

> You lift the latch. The door doesn't open so much as leave — the water behind it takes it off its hinges and you with it. The Bone Passage fills in the time it takes to understand what's happening.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 145 â€” after flood death: Bone Passage south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 146 â€” the crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> You can't go that way.

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 147 â€” through the arch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `enter crypt` `go through arch` `east` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> You can't see any crypt here!

> That sentence isn't one I recognize.

> You can't go that way.

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 148 â€” arch, other dirs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `down` `in` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 149 â€” the arch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine arch` `north` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> You can't see any arch here!

> The Bone Passage

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 150 â€” Junction south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `look` `save` `quit` `yes`
```
> Restored.
The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> The Junction

> The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.
Carved into the bridge's keystone, half worn away: the town's crest, and beneath it, PUBLIC PROPERTY.

> The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 151 â€” toll keeper
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to figure` `` `` `talk to troll` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> "Toll," the Boggart says, holding out a hand without looking at it. "Two hundred. Each way. Non-negotiable." He doesn't say two hundred of what, and you get the impression he's never had to.

> I beg your pardon?

> I beg your pardon?

> You can't see any troll here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 152 â€” seal to Boggart
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `give seal to boggart` `examine keystone` `attack boggart` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> The Boggart doesn't take the wax seal.
The torch burns a little lower than it did.

> You can't see any keystone here!

> You can't fight the Boggart.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 153 â€” (dev hint: up from Charnel Walk)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `east` `south` `up` `look` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> The Junction

> The Bone Passage

> Charnel Walk

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 154 â€” crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `search remains` `examine alcoves` `south` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> You can't see any remains here!

> You can't see any alcoves here!

> You can't go that way.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 155 â€” crypt far passage
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> You can't go that way.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 156 â€” crypt other dirs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> You can't go that way.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 157 â€” crypt west/up
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> You can't go that way.

> The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 158 â€” crypt up/down
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 159 â€” mausoleum door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open door` `out` `look` `save` `quit` `yes`
```
> Restored.
The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> You can't see any door here!
The torch is noticeably dimmer now. It won't last forever.

> You can't go that way.

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 160 â€” leaving mausoleum
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `south` `east` `west` `look` `save` `quit` `yes`
```
> Restored.
The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
The air is still in a way that has nothing to do with wind.

> The Mausoleum

> You can't go that way.

> You can't go that way.

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 161 â€” crypt far passage
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `down` `look` `save` `quit` `yes`
```
> Restored.
The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> The Crypt

> Charnel Walk

> Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 162 â€” crypt diagonals
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `northeast` `northwest` `southeast` `southwest` `look` `save` `quit` `yes`
```
> Restored.
Charnel Walk
The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.

> The Crypt

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.
The torch gutters. You don't have much time left on it.

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 163 â€” new torch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `north` `north` `look` `north` `west` `south` `south` `south` `buy torch` `inventory` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> The Mausoleum

> Graveyard

> Church of All

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus glances at the torch. "That one's had it." He hands you a fresh one. "Three Zenni."

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
You have 3 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 164 â€” the blast
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `east` `east` `east` `north` `north` `down` `down` `down` `light gunpowder` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> Mine Entrance

> Main Shaft

> Mine Tunnels
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> You strike the flint. The fuse catches with a sharp hiss. The gunpowder is burning. Time to leave.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 165 â€” running
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `wait` `down` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Main Shaft

> Time passes...

> Mine Tunnels
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.
The mine finds its weak point. So does the ceiling above you.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 166 â€” running properly
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `wait` `wait` `wait` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Main Shaft

> Mine Entrance

> Time passes...

> Time passes...
The mine finds its weak point. So does the ceiling above you.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 167 â€” clear of the mine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `up` `wait` `wait` `look` `save` `quit` `yes`
```
> Restored.
Mine Tunnels
The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.
A split timber support sags under the rock above it.
A paper packet of gunpowder.

> Main Shaft

> Mine Entrance

> Roundabout Forest

> Time passes...
A muffled BOOM shakes the ground beneath your feet. Dust and splinters billow from the mine entrance as it collapses inward. The Pie Rats go running to investigate — and the ship is unguarded.

> Time passes...

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 168 â€” boarding the ship
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `east` `east` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Beach

> The Docks

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.
A shovel is lashed to the rail near the bow.

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.
A shovel is lashed to the rail near the bow.
Wedged under a barrel lashed to the rail is a fold of oilcloth. Inside is a hand-drawn map: a small island just off the sea lane, a dotted line, and an X near the trees. You tuck it away.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 169 â€” ship
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take shovel` `read map` `down` `look` `save` `quit` `yes`
```
> Restored.
Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.
A shovel is lashed to the rail near the bow.

> You take the shovel.

> There's nothing written on the treasure map.

> You can't go that way.

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 170 â€” sailing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine map` `sail` `look` `save` `quit` `yes`
```
> Restored.
Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> A hand-drawn map on oilcloth. A small island south of the sea lane, east of Roundabout, with a dotted line up the beach and an X near the trees.

> You cast off and the ship moves into open water. The sails catch the wind.

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 171 â€” at sea
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> Western Roundabout Sea
The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore.

> Western Roundabout Sea
The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 172 â€” at sea 2
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
Western Roundabout Sea
The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore.

> Roundabout Sea
The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.

> Roundabout Sea
The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 173 â€” south to island
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Sea
The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.

> You can't go that way.

> Roundabout Sea
The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 174 â€” further east
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Sea
The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.

> Eastern Roundabout Sea
Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. East of it, the sea continues without comment.

> Eastern Roundabout Sea
Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. East of it, the sea continues without comment.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 175 â€” landing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Eastern Roundabout Sea
Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. East of it, the sea continues without comment.

> You can't go that way.

> Eastern Roundabout Sea
Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. East of it, the sea continues without comment.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 176 â€” landing phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `land` `go to island` `disembark` `look` `save` `quit` `yes`
```
> Restored.
Eastern Roundabout Sea
Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. East of it, the sea continues without comment.

> Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.

> That sentence isn't one I recognize.

> You're not on a ship.

> Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 177 â€” X marks the spot
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `dig` `north` `look` `save` `quit` `yes`
```
> Restored.
Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.

> You pace it out from the map — up the beach, toward the trees, to where the X should be. Two feet down, the shovel hits wood: a small chest, iron-banded and crusted with salt.

> The ocean offers no opinion on that idea, and neither does your survival instinct.

> Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.
A salt-crusted chest sits in the hole you dug.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 178 â€” chest
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open chest` `look in chest` `take all from chest` `inventory` `save` `quit` `yes`
```
> Restored.
Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.
A salt-crusted chest sits in the hole you dug.

> The hinges complain, but the lid comes up. Inside, wrapped in oilcloth: 30 Zenni. You pocket them.

> A salt-crusted chest sits in the hole you dug.

> The torch isn't in the chest.
The dagger isn't in the chest.
The wax seal isn't in the chest.
The lockpicks isn't in the chest.
The thin paper isn't in the chest.
The plain dark ring isn't in the chest.
The coil of rope isn't in the chest.
The large bowl piece isn't in the chest.
The pickaxe isn't in the chest.
The Pie Rat disguise isn't in the chest.
The flat rune stone isn't in the chest.
The Tip Journal isn't in the chest.
The bow isn't in the chest.
The Pale Blade isn't in the chest.
The flint and steel isn't in the chest.
The treasure map isn't in the chest.
The shovel isn't in the chest.
The chest isn't in the chest.
The Rowan isn't in the chest.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
  Treasure map
  Shovel
You have 33 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 179 â€” sailing home
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `board ship` `sail` `west` `west` `west` `look` `save` `quit` `yes`
```
> Restored.
Desert Island
The sand on the beach is undisturbed. That fact, for some reason, does not comfort you.
Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone.
An empty chest sits in the hole you dug.

> Pie Rat Ship — Deck

> You cast off and the ship moves into open water. The sails catch the wind.

> Roundabout Sea

> Western Roundabout Sea

> Pie Rat Ship — Deck
The Pie Rats are waiting on the dock. Nobody says anything for a while. The biggest of them walks the deck stem to stern and finds nothing wrong with his ship, which seems to annoy him more than damage would have. He snorts, digs in a pocket, and flips you a coin. It rings on the boards at your feet.

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.
A Pie Rat Coin lies on the boards.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 180 â€” Pie Rat Coin
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take coin` `examine coin` `west` `west` `north` `west` `west` `west` `south` `south` `tip may 15` `save` `quit` `yes`
```
> Restored.
Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.
A Pie Rat Coin lies on the boards.

> You take the Pie Rat Coin.

> A heavy coin stamped with a grinning rat in a tricorn hat. It isn't money anywhere you know of.

> The Docks

> Roundabout Beach

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May looks genuinely uncomfortable. "I appreciate the thought, but no." She slides it all back. "Ask me something and we'll talk."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 181 â€” tip 10
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `tip may 10` `tip may 5` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> May counts the coins once, pockets them, and leans all the way across the bar. "Rowan," she says.
"I've seen plenty of people try Lynds. The ones who come back and win aren't the same people who first sat down across from him."

> May pockets the coins carefully. "That buys you something worth hearing," she says.
"Rushing through a place and knowing a place aren't the same thing. I've learned that much."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 182 â€” searching the crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `east` `south` `south` `south` `down` `search` `examine passage` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> The Mausoleum
The torch catches the dark and pushes it back. Good thinking, getting one of these.

> The Crypt

> You search carefully but find nothing unusual.

> You can't see any passage here!

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 183 â€” footprints
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `follow footprints` `examine footprints` `in` `out` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> I don't know the word "follow".

> You can't see any footprints here!

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 184 â€” lighthouse
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `up` `north` `north` `north` `east` `east` `east` `south` `east` `east` `sail` `east` `north` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> The Mausoleum

> You can't go that way.

> Graveyard

> Church of All

> Main East

> Roundabout Wasteland

> Beach Road

> You can't go that way.

> Roundabout Beach

> The Docks

> Pie Rat Ship — Deck

> You cast off and the ship moves into open water. The sails catch the wind.

> Western Roundabout Sea

> You can't go that way.

> Western Roundabout Sea
The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 185 â€” open sea
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `north` `east` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
Western Roundabout Sea
The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore.

> Roundabout Sea

> You can't go that way.

> Eastern Roundabout Sea

> You can't go that way.

> Open Ocean
Open ocean in every direction. Nothing else.

> Open Ocean
Open ocean in every direction. Nothing else.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 186 â€” open ocean
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `north` `south` `look` `save` `quit` `yes`
```
> Restored.
Open Ocean
Open ocean in every direction. Nothing else.

> Open Ocean
The ocean does not vary its presentation.

> You can't go that way.

> You can't go that way.

> Open Ocean
The ocean does not vary its presentation.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 187 â€” home
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `west` `west` `west` `west` `look` `save` `quit` `yes`
```
> Restored.
Open Ocean
The ocean does not vary its presentation.

> Open Ocean

> Eastern Roundabout Sea

> Roundabout Sea

> Western Roundabout Sea

> Pie Rat Ship — Deck

> Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 188 â€” (dev hint: NE from beach)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `west` `northeast` `look` `save` `quit` `yes`
```
> Restored.
Pie Rat Ship — Deck
The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.

> The Docks

> Roundabout Beach

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.
A scroll lies on the desk, weighted at one corner with a smooth stone.

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.
A scroll lies on the desk, weighted at one corner with a smooth stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 189 â€” the scroll
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take scroll` `examine scroll` `read scroll` `examine stone` `inventory` `save` `quit` `yes`
```
> Restored.
The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.
A scroll lies on the desk, weighted at one corner with a smooth stone.

> You take the Unbind Undead scroll.

> A spell scroll headed Unbind Undead, in a cramped, careful hand.

> The words are legible. The meaning is not. Whatever is written here was meant for someone with a different kind of mind — or a different kind of training. Will Passion, in his tower, has been known to translate this sort of thing for people like you.

> A small flat stone, dark and smooth, threaded on a cord. Mineral veins run through it in a pattern that looks almost intentional.

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
  Treasure map
  Shovel
  Pie Rat Coin
  Unbind Undead scroll
You have 18 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 190 â€” stone, stairs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take stone` `take smooth stone` `up` `look` `save` `quit` `yes`
```
> Restored.
The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.

> You already have the flat rune stone.
The torch burns a little lower than it did.

> You can't see any stone here!

> You can't go that way.

> The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 191 â€” the stairs
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `climb stairs` `examine desk` `read papers` `save` `quit` `yes`
```
> Restored.
The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.

> You can't see any stairs here!

> You can't see any desk here!

> You can't see any papers here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 192 â€” to Will with the scroll
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `southwest` `north` `west` `west` `west` `south` `open mailbox` `give scroll to will` `` `` `save` `quit` `yes`
```
> Restored.
The Lighthouse
The keeper's room is small and round, the walls curving with the tower. A narrow stair spirals up toward the lamp. A desk sits under the one window, papers stacked with more care than anything else in the room — whoever works here left in the middle of something and meant to come back.

> Roundabout Beach

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, reading silently for a moment. Then he reads it aloud — not to you, exactly, more as if the words need to be heard in the right kind of room. When he finishes, you understand it. You're not sure how. "Keep that," he says, nodding at the space where the scroll was. It's gone. "The knowing, I mean."
[Unbind Undead spell learned.]

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 193 â€” Lynds rematch (dev suggestion)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `score` `examine painting` `talk to lynds` `` `` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> Score: 0
Level 4 (107 XP)
Zenni: 18
0 treasures on display.

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

> I beg your pardon?
The torch is noticeably dimmer now. It won't last forever.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 194 â€” (dev hint: north of archery range)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `west` `west` `north` `look` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path and the bog, ringed with reeds and the occasional frog. The water is dark and calm.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.
You see a bottle at the bottom of the pond.

> Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path and the bog, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 195 â€” pond
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take bottle` `swim` `north` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Pond
The pond is easy to walk past without noticing. It sits low between the town path and the bog, ringed with reeds and the occasional frog. The water is dark and calm.
You see a bottle at the bottom of the pond.

> You can't take the bottle.

> You don't want to swim in that!

> The Bog of Eternal Stench
A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave.
Half-sunk in the mud at the edge of the reeds, a curved shard of pale ceramic catches what light there is.
A clump of thyme grows on a dry hummock among the reeds, improbably green.

> The Bog of Eternal Stench
A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave.
Half-sunk in the mud at the edge of the reeds, a curved shard of pale ceramic catches what light there is.
A clump of thyme grows on a dry hummock among the reeds, improbably green.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 196 â€” bog
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take shard` `take thyme` `north` `look` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave.
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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 197 â€” hollow log
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `look in log` `search log` `take metal` `inventory` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds. Something small and metal glints inside it.

> Rotten through the middle and hollow end to end. Wedged inside: a small brass key.

> You search carefully but find nothing unusual.
The torch gutters. You don't have much time left on it.

> You can't see any metal here!

> You are carrying:
  Torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
  Treasure map
  Shovel
  Pie Rat Coin
  Heart necklace (not worn)
  Muddy bowl piece
  Bog thyme
You have 24 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 198 â€” brass key, bog paths
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take key` `north` `west` `east` `look` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.
A hollow log lies half-sunk among the reeds. Something small and metal glints inside it.

> You take the music box key.

> You can't go that way.

> You can't go that way.

> The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.
A grey stone sits at the water's edge, one face worn flat.

> The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.
A grey stone sits at the water's edge, one face worn flat.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 199 â€” grey stone
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine grey stone` `take grey stone` `look under grey stone` `north` `east` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.
A grey stone sits at the water's edge, one face worn flat.

> A grey stone, heavy for its size, one face worn flat by water. Faint lines are etched across the surface in no pattern you recognize.

> You take the grey rune stone.

> There is nothing but dust there.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 200 â€” bog paths
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
Half-sunk in the mud at the water's edge, a slab of dressed stone lies face-down — too square to be anything the bog made. Someone dumped it here.
Off to the east, the brush isn't quite as dense as it should be. Behind it, a path — narrow, deliberate — leads to something low and round. A yurt, improbably dry.

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 201 â€” gravestone
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `turn gravestone` `examine gravestone` `read gravestone` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> You can't turn that.
The torch gutters and goes out.

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> There's nothing written on the gravestone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 202 â€” the yurt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> Dankhaus Common Room
Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.
Litlock looks up from whatever he's doing with the particular alertness of someone who has been waiting for company without admitting it to himself. He takes you in. Then he grins — wide, genuine, the kind that arrives before the person decides to smile.
"Right," he says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> Dankhaus Common Room
Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 203 â€” Litlock
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to litlock` `1` `` `` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.

> "Right," Litlock says. "Entertain me."
  1. Tell a joke
  2. Do something physical

> You clear your throat. "I have a joke."
Litlock leans back. "Everyone has a joke. Let's see if yours is different."
  1. A pun
  2. An absurd observation

> I beg your pardon?

> I beg your pardon?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 204 â€” Litlock joke
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to litlock` `1` `2` `1` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.

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

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 205 â€” music box
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `west` `south` `south` `south` `east` `east` `south` `open mailbox` `unlock music box with key` `open music box` `save` `quit` `yes`
```
> Restored.
Dankhaus Common Room
Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.

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

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits on the corner of Will's desk, its lid locked shut.

> The key turns with a soft click. The lid lifts, and a short melody plays — a few bright notes, a little out of tune, then nothing. Inside, folded small, is a scroll.

> A small lacquered music box, its lid open.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 206 â€” box scroll, Shamus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take scroll` `examine scroll` `read scroll` `examine painting` `south` `south` `give thyme to shamus` `` `buy torch` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.
A folded scroll lies in the music box.

> You take the Light scroll.

> A spell scroll headed Light, in a small, quick hand.

> Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, reading silently for a moment. Then he reads it aloud — not to you, exactly, more as if the words need to be heard in the right kind of room. When he finishes, you understand it. You're not sure how. "Keep that," he says, nodding at the space where the scroll was. It's gone. "The knowing, I mean."
[Light spell learned.]

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus takes the thyme, crushes a leaf between his fingers and breathes it in. "That's the stuff." He sets it by the stove. "Now a pot that holds water, and we're in business."

> I beg your pardon?

> Shamus glances at the torch. "That one's had it." He hands you a fresh one. "Three Zenni."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 207 â€” to the crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `east` `south` `south` `south` `down` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> The Mausoleum
The torch catches the dark and pushes it back. Good thinking, getting one of these.

> The Crypt

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 208 â€” casting in the crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `cast unbind undead` `cast light` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Nothing here answers the spell.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Crypt

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 209 â€” far passage with Light
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `north` `west` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 210 â€” mausoleum and graveyard look
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `look` `north` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> The Mausoleum

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Graveyard

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 211 â€” into the graveyard building
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `look` `east` `look` `examine` `building` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

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
The building has the quality of a held breath.
Something in the walls makes a sound as you cross the threshold — not quite a creak, not quite a welcome.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> That sentence isn't one I recognize.

> I don't know the word "building".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 212 â€” the Entrance details
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine booth` `examine stool` `examine hooks` `examine runner` `examine ceiling` `search booth` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> The ticket window is cracked but intact. A small wooden sign on the ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. The booth is empty. Whoever collected the tickets isn't collecting anymore.

> You can't see any stool here!

> Empty brackets where something square once hung — the right shape for mirrors, though whatever was here is long gone. The hooks in the deeper rooms still have their tenants.

> You can't see any runner here!

> You can't see any ceiling here!

> You search carefully but find nothing unusual.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 213 â€” trying exits from the Entrance
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `south` `read sign` `examine sign` `east` `look` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> You can't go that way.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> There's nothing written on the ticket booth.

> The ticket window is cracked but intact. A small wooden sign on the ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. The booth is empty. Whoever collected the tickets isn't collecting anymore.

> You can't go that way.

> The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 214 â€” more exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `up` `down` `northeast` `southeast` `southwest` `northwest` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> Graveyard

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 215 â€” the mirror
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `examine mirror` `examine reflection` `close eyes` `walk backwards` `cast light` `south` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> The Entrance

> You can't see any mirror here!

> You can't see any reflection here!

> You can't see any eyes here!

> You can't see any backwards here!

> There's light enough here already.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 216 â€” necklace at the mirror
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear necklace` `south` `remove necklace` `smile` `south` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> You put on the heart necklace.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> Heart necklace removed.

> I don't know the word "smile".
The torch burns a little lower than it did.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 217 â€” trying the ring at the mirror (NOT saved)
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> The Rejection Mirror
A narrow room with a single tall mirror filling the far wall, its frame carved with grinning faces. The glass is old and silvered at the edges. The doorway to the south is beside it — you'd have to pass right in front of it to get there.

> The Rejection Mirror
A narrow room with a single tall mirror filling the far wall, its frame carved with grinning faces. The glass is old and silvered at the edges. The doorway to the south is beside it — you'd have to pass right in front of it to get there.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 218 â€” ring on, past the Rejection Mirror
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear ring` `south` `examine mirror` `examine frame` `south` `look` `save` `quit` `yes`
```
> Restored.
The Entrance
The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now.
The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now.
A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back.
The building has the quality of a held breath.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> The Rejection Mirror
A narrow room with a single tall mirror filling the far wall, its frame carved with grinning faces. The glass is old and silvered at the edges. The doorway to the south is beside it — you'd have to pass right in front of it to get there.

> You can't see any mirror here!

> You can't see any frame here!

> The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south.
You spot a firing pin behind the mirror's frame, a crossbow cocked and ready and are able to disarm it, neutralizing it.
You hear music — a familiar melody. You have reached level 5!

> The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south.
The ring is heavier than it was. Not in weight — in presence. It knows you're wearing it. You find yourself aware of it in a way you weren't before.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 219 â€” south past the Shatter Trap, ring off
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove ring` `south` `look` `save` `quit` `yes`
```
> Restored.
The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south.

> Plain dark ring removed.

> The mirror finds you. Your reflection looks back at you with an expression you aren't making — and then you are back where you started, with no memory of turning around.

> The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 220 â€” ring on, further south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear ring` `south` `look` `south` `save` `quit` `yes`
```
> Restored.
The Shatter Trap Mirror
Another mirror, another frame of carved smiles. This one is larger than the last, the glass faintly rippled with age, so your reflection wavers as you move. The way on is past it, to the south.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.
A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.
A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 221 â€” the ghost
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine figure` `examine ghost` `talk to ghost` `remove ring` `talk to ghost` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.
A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> A figure stands among the reflections, grey and thin and turned toward you — the only thing in the room that isn't repeated.

> There's no response from the ghost.

> Plain dark ring removed.

> You can't see any ghost here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 222 â€” unbinding the ghost
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear ring` `cast unbind undead` `look` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The torch is noticeably dimmer now. It won't last forever.

> "Thank you. I can rest now."
The grey figure thins until the mirrors have nothing left to repeat. Something falls where he stood and lands with a small metallic click — a pocket watch.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.
A pocket watch lies on the floor where the ghost stood.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 223 â€” the pocket watch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take watch` `examine watch` `open watch` `remove ring` `extinguish torch` `look` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.
A pocket watch lies on the floor where the ghost stood.

> You take the pocket watch.

> A plain silver pocket watch, stopped. The inside of the lid is engraved, but too worn to read.

> You can't open that.

> Plain dark ring removed.

> A torch burns until it's done. There's no putting it out.

> Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 224 â€” watch and exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read watch` `wind watch` `rub watch` `east` `west` `north` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.

> There's nothing written on the pocket watch.

> I don't know the word "wind".

> Fiddling with the pocket watch has no effect.

> You can't go that way.

> You can't go that way.

> You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 225 â€” leaving the mirror building
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear ring` `north` `north` `north` `west` `remove ring` `look` `save` `quit` `yes`
```
> Restored.
Ghost's Room
Mirrors on every wall, angled at each other so the room goes on in every direction at once. Your reflections are wrong by a fraction — a beat late, or a beat early. It is very cold.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The torch gutters. You don't have much time left on it.

> The Shatter Trap Mirror
The ring is harder to ignore than it was. You are aware of it the way you're aware of a sound that hasn't stopped. You should take it off. You know you should take it off.

> The Rejection Mirror
Take it off. You should take it off.

> The Entrance
Take it off. Soon.

> Graveyard
You could take it off. You could.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 226 â€” to Will with the watch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `west` `south` `examine painting` `show watch to will` `give watch to will` `ask will about watch` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You can't see any painting here!

> I don't know the word "show".

> You can't see any will here!

> You can't see any will here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 227 â€” to Will via the mailbox
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open mailbox` `look` `give watch to will` `ask will about watch` `talk to will` `save` `quit` `yes`
```
> Restored.
Tale and Ale — Main Room
The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well.
Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs to the upper floor. A mailbox sits near the door, entirely out of place and acknowledged by no one.
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> You open the mailbox. A familiar warmth pulls you through.
Will's Wizard Tower
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.
The torch gutters and goes out.

> Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> Will Passion doesn't take the pocket watch.

> There's no response from the Will Passion.

> There's no response from the Will Passion.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 228 â€” the Archivist and the watch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine painting` `north` `west` `north` `east` `look` `give watch to archivist` `talk to archivist` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main West

> Library — Main Hall

> The Stacks
Something catches your eye, tucked out of sight: 5 Zenni. You pocket them.

> The Stacks
The passage from the Main Hall opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> The Archivist doesn't take the pocket watch.

> He looks up when spoken to, marking his place with two fingers before setting the book aside.
"Yes. I've been trying to authenticate a map — provenance is unclear, which makes it nearly useless for the purpose I need it for. There's an engraving in the lower passages that should settle the question, if I could get a clean impression of it."
He glances at the table, then back.
"I can't leave this. If you're heading down that way — thin paper, a stick of charcoal, and some patience. The engraving is in the Inscription Chamber. You'll know it when you see it."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 229 â€” the librarian and the watch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `give watch to librarian` `talk to librarian` `save` `quit` `yes`
```
> Restored.
The Stacks
The passage from the Main Hall opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Library — Main Hall

> Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> The librarian doesn't take the pocket watch.

> "'The lower passages.' That's all I have. That's the last thing."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 230 â€” the clerk and the watch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `north` `west` `look` `give watch to clerk` `talk to clerk` `save` `quit` `yes`
```
> Restored.
Library — Main Hall
The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between.
A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold.
The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> The clerk takes the watch without much interest — then turns it over, and stops. He opens the lid and looks at the worn engraving for a long time, his thumb moving across it as if he can read it by touch.
"This was my uncle's," he says quietly. "He went into that place by the graveyard. We never—" He stops. Closes the lid. Holds it a moment longer.
Then he stands, goes to a shelf without looking, and comes back with a rolled document tied in faded ribbon. He puts it in your hands. "The charter. Take it. Whatever you need it for."
[Town Charter added to inventory.]

> The clerk is turning the pocket watch over in his hands. He nods to you, but doesn't say anything.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 231 â€” to the Crypt with the charter
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine charter` `read charter` `east` `south` `east` `south` `south` `south` `down` `cast light` `look` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> A rolled document tied with faded ribbon. The town seal is pressed into the wax at the bottom, and the handwriting is the careful kind that expects to be read for a long time.

> There's nothing written on the town charter.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Graveyard

> It is pitch black. You are likely to be eaten by a grue.

> It's too dark to go any further without a light.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Mausoleum

> The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 232 â€” down to the Toll Bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `down` `north` `west` `south` `look` `save` `quit` `yes`
```
> Restored.
The Mausoleum
The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.

> The Crypt

> Charnel Walk

> The Bone Passage

> The Junction

> The Toll Bridge

> The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 233 â€” the charter vs the Boggart
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `talk to boggart` `show charter to boggart` `give charter to boggart` `look` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.
A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay.
He eyes you with the satisfaction of a man whose position has never once been successfully argued with.

> "Toll," the Boggart says, holding out a hand without looking at it. "Two hundred. Each way. Non-negotiable." He doesn't say two hundred of what, and you get the impression he's never had to.

> I don't know the word "show".

> The Boggart takes the charter, unrolls it, and reads. His lips move. He reads a particular clause twice. Then he rolls it back up with great dignity, hands it back, and gets off the bridge. "Public property," he mutters. "Should've been told." He stomps off into the tunnels, leaving behind a battered strongbox where he was sitting.

> The Toll Bridge
The bridge is empty now. The strongbox sits where he was.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 234 â€” the strongbox
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine strongbox` `open strongbox` `pick lock` `unlock strongbox with lockpicks` `look` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
The bridge is empty now. The strongbox sits where he was.

> You see nothing special about the strongbox.

> You get your fingers under the lid and heave. It gives with a shriek of rusted hinges. Inside: 10 Zenni. You pocket them.

> You already have the lockpicks.

> You can't unlock that.

> The Toll Bridge
The bridge is empty. The open strongbox sits where he was, lid thrown back.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 235 â€” across the bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
The Toll Bridge
The bridge is empty. The open strongbox sits where he was, lid thrown back.

> Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 236 â€” into the dungeon
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Dungeon Entrance
The tunnel ends at a threshold — stone floor, stone walls, a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.
You spot a near-invisible thread strung at chest height across the corridor and are able to disarm it, neutralizing it.

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 237 â€” Ink Corridor west
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `look` `save` `quit` `yes`
```
> Restored.
Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.
You spot an unstable arrangement of clay pots, one of them the trigger and are able to disarm it, neutralizing it.

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
A squat glass jar sits among the clay pots, stoppered with wax.
One small clay pot sits on the shelf, the only one without a crack.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 238 â€” Supply Room items
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine mechanism` `examine jar` `examine pot` `examine bar` `examine salt` `examine mortar` `save` `quit` `yes`
```
> Restored.
Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
A squat glass jar sits among the clay pots, stoppered with wax.
One small clay pot sits on the shelf, the only one without a crack.

> You can't see any mechanism here!

> A squat glass jar, stoppered with wax. Something grey and dense shifts inside it.

> A small clay pot, plain and sound. Not a crack in it.

> A length of iron as thick as your wrist, notched at one end. Heavy, and built to take weight.

> It looks like it weighs as much as a Chachapoyan Fertility Idol.

> A tub of grey mortar compound, still workable under the lid. Someone meant to fix something down here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 239 â€” taking supplies
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take bar` `take pot` `take jar` `take mortar` `take salt` `inventory` `save` `quit` `yes`
```
> Restored.
Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.
A heavy iron bar leans in the corner, notched at one end — the kind of thing made to hold something open.
A sealed tub of mortar compound sits on a low shelf.
A fat sack of salt slumps against the shelves.
A squat glass jar sits among the clay pots, stoppered with wax.
One small clay pot sits on the shelf, the only one without a crack.

> You take the portcullis bar.

> You take the small clay pot.

> You take the smoke jar.

> You take the mortar compound.

> You take the sack of salt.

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
  Treasure map
  Shovel
  Pie Rat Coin
  Heart necklace (not worn)
  Muddy bowl piece
  Grey rune stone
  Town charter
  Portcullis bar
  Small clay pot
  Smoke jar
  Mortar compound
  Sack of salt
You have 61 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 240 â€” Ink Corridor east
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `look` `save` `quit` `yes`
```
> Restored.
Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.

> Ink Corridor

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 241 â€” Storage Area and south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine cart` `examine beam` `south` `look` `save` `quit` `yes`
```
> Restored.
Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> A sturdy two-wheeled cart, the handles worn smooth. Built to carry more than a person could.

> A heavy timber beam, squared and solid. Something meant to hold up a ceiling.

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 242 â€” repairing the aqueduct
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine blocks` `examine gap` `take block` `repair aqueduct` `use mortar` `put mortar in gap` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> You see nothing special about the stone blocks.

> You see nothing special about the aqueduct.

> They're far too heavy to carry off. They belong in the channel.

> There's still a gap. Mortar won't hold back that much water.

> Nothing happens.

> That won't fit in the aqueduct.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 243 â€” lifting the blocks
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `lift block` `put block in aqueduct` `lift block with bar` `push block` `north` `take cart` `push cart` `pull cart` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> Nothing happens.

> That won't fit in the aqueduct.

> That sentence isn't one I recognize.

> Pushing the stone blocks has no effect.

> Storage Area

> You take the hand cart.

> Pushing the hand cart has no effect.

> Moving the hand cart reveals nothing.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 244 â€” cart and blocks
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `put block in cart` `load cart` `use cart` `drop cart` `put block in cart` `save` `quit` `yes`
```
> Restored.
Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a heavy support beam laid across the floor. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> Collapsed Aqueduct

> The cart's for the gravestone.

> That doesn't need loading.

> Nothing happens.

> You drop the hand cart.

> The cart's for the gravestone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 245 â€” levering the blocks
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take cart` `pry block with bar` `use bar on block` `lever block` `raise block` `place block` `fix aqueduct` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. Three of its blocks lie tumbled on the floor below the gap, and water spills from the broken end, runs across the stone and away down the passage south.

> You take the hand cart.

> You can't get any leverage on that.

> Nothing happens.

> You can't get any leverage on that.

> Nothing happens.

> You get your arms under the first block and heave it up into the gap. It grinds into place. Water finds its way around it, but less of it.

> There's still a gap. Mortar won't hold back that much water.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 246 â€” finishing the aqueduct
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `place block` `place block` `fix aqueduct` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, until here. A section of it has given way. One block sits back in the gap; the other two lie on the floor below it. Water still spills through what's left of the break and away down the passage south.

> The second block is heavier, or you're more tired. It goes in beside the first with a sound like a door shutting.

> The last block fights you the whole way up. Then it seats, and the gap is closed — though water still beads and runs at every joint.

> You work the mortar into every joint, pressing it in with your thumbs until the seeping stops. For a moment the channel is silent. Then the water finds its way through — the whole length of the aqueduct, running toward town.

> Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, with a mended section in the middle where the mortar is still pale. Water moves through it quietly, on its way to somewhere it's needed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 247 â€” south of the aqueduct
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, with a mended section in the middle where the mortar is still pale. Water moves through it quietly, on its way to somewhere it's needed.

> Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 248 â€” the timbers
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine timbers` `move timbers` `pry timbers with bar` `cut timbers with blade` `east` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> You see nothing special about the timbers.

> You can't move the timbers.

> You can't get any leverage on that.

> Strange concept, cutting the timbers...

> The timbers block the way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 249 â€” timbers, more ideas
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `burn timbers` `light timbers` `break timbers with pickaxe` `climb timbers` `west` `south` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> You can't light the timbers.

> You can't light the timbers.

> That sentence isn't one I recognize.

> You can't climb the timbers.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 250 â€” Ink Corridor south
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `west` `south` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Collapsed Aqueduct

> Storage Area

> Ink Corridor

> Narrow Passageway
A short passage, plain stone, lower-ceilinged than the corridor behind you. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.

> Narrow Passageway
A short passage, plain stone, lower-ceilinged than the corridor behind you. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 251 â€” through the doorway
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Narrow Passageway
A short passage, plain stone, lower-ceilinged than the corridor behind you. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 252 â€” the idol swap
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine figurine` `examine pedestal` `put salt on pedestal` `look` `save` `quit` `yes`
```
> Restored.
Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> A small stone figurine, squat and round-bellied, worn smooth by hands that weren't yours. A Chachapoyan Fertility Idol, if you had to guess.

> You can't see any pedestal here!

> You can't see any pedestal here!

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 253 â€” swap phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `swap idol with salt` `replace idol with salt` `put salt on plate` `examine plate` `look` `save` `quit` `yes`
```
> Restored.
Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.

> You set the sack of salt on the pedestal and lift the idol away in the same motion. The pedestal doesn't so much as twitch.

> I don't know the word "replace".

> You can't see any plate here!

> You can't see any plate here!

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center stands a stone pedestal. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the salt's weight is holding it down now.
A sack of salt sits on the pedestal where the idol was.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 254 â€” Idol Room exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine idol` `south` `east` `west` `down` `save` `quit` `yes`
```
> Restored.
Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center stands a stone pedestal. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the salt's weight is holding it down now.
A sack of salt sits on the pedestal where the idol was.

> A small stone figurine, squat and round-bellied, worn smooth by hands that weren't yours. A Chachapoyan Fertility Idol, if you had to guess.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.
You spot a pressure plate set into the corridor floor and are able to disarm it, neutralizing it.
You hear music — a familiar melody. You have reached level 6!
You feel a deeper sense of calm settle over you — the kind that comes with hard-won experience. You can now REST to recover when the fighting stops.

> The door is shut.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 255 â€” the Combat Room door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine door` `open door` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> You can't see any door here!

> You can't see any door here!

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 256 â€” Combat Room other ways
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `pick lock` `knock` `unlock east door` `east` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> Prayer Alcove
A low stone alcove, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands. It looks like a dead end.
The niche goes back further than it looks. Behind the carved lip there's a gap — and inside it, things that were put there on purpose.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> You can't go that way.

> You already have the lockpicks.

> That sentence isn't one I recognize.

> You can't see any door here!

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 257 â€” the alcove
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take crowbar` `take vial` `examine vial` `examine niche` `examine crowbar` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands. It looks like a dead end.
A crowbar lies in the recess, one end flattened from use.
A small stoppered vial sits beside it, the glass frosted despite the damp.

> You take the crowbar.

> You take the vial of glacier melt.

> A stoppered vial of water so cold the glass has frosted. It doesn't warm in your hand.

> You can't see any niche here!

> A heavy iron crowbar, one end flattened to a lip. Made for getting into things.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 258 â€” crowbar on the timbers
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `north` `east` `south` `south` `pry timbers with crowbar` `east` `look` `save` `quit` `yes`
```
> Restored.
Prayer Alcove
A low stone alcove, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands. It looks like a dead end.

> Combat Room

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> You can't get any leverage on that.

> The timbers block the way.

> Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 259 â€” crowbar phrasing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `use crowbar on timbers` `move timbers with crowbar` `pry timbers` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Nothing happens.

> That sentence isn't one I recognize.

> You can't get any leverage on that.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 260 â€” waiting in the Combat Room
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `west` `south` `south` `south` `wait` `wait` `pry door with crowbar` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Collapsed Aqueduct

> Storage Area

> Ink Corridor

> Narrow Passageway

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Combat Room

> Time passes...

> Time passes...

> You can't see any door here!

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 261 â€” inventory check
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `inventory` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> You are carrying:
  Burnt-out torch
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pickaxe
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Bow
  Pale Blade
  Flint and steel
  Treasure map
  Shovel
  Pie Rat Coin
  Heart necklace (not worn)
  Muddy bowl piece
  Grey rune stone
  Town charter
  Portcullis bar
  Small clay pot
  Smoke jar
  Hand cart
  Chachapoyan Fertility Idol
  Crowbar
  Vial of glacier melt
You have 69 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 262 â€” triggering the plate (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine plate` `examine trap` `step on plate` `trigger trap` `rearm trap` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> You see nothing special about the pressure plate.

> You can't see any trap here!

> That sentence isn't one I recognize.

> I don't know the word "trigger".

> I don't know the word "rearm".

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 263 â€” plate phrasing (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `press plate` `push plate` `stand on plate` `jump on plate` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.

> Pushing the pressure plate has no effect.

> Pushing the pressure plate has no effect.

> That sentence isn't one I recognize.

> Somewhere behind the heavy door, a bell rings — once, flat and loud. Something on the other side moves.
The door at the east end grinds open. The thing that comes through it was a guard once — the scraps of a uniform still hang off it — but whatever it is now is mostly reach, teeth, and intent. The Warden.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 264 â€” the Warden
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine warden` `cast unbind undead` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> The Warden stands between you and the open door, swaying, waiting for you to move.

> Nothing here answers the spell.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 265 â€” fighting the Warden
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `attack warden with pale blade` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> You land a solid blow. The Warden staggers, and comes on anyway.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 266 â€” fighting the Warden, cont.
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You have 6 of 7 hearts.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 267 â€” journal, then ring past the Warden
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read journal` `wear ring` `east` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> JOURNAL

The Lost Apprentice        [Board]

Shamus's Recipe            [Organic]

The Hollow Statue          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.
  Tip: There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it.
  Tip: No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew.

The Undead Warden          [Organic]
  Tip: The Keeper of the Faiths has gone missing. No one's seen him in some time.
  Tip: There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it.
  Tip: No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew.

The Archivist's Request    [Organic]

The Beekeeper's Swarm      [Organic]
  Tip: Bees aren't aggressive by nature — beekeepers have known for centuries how to calm them. Something about smoke. Ask me why it works and I couldn't tell you, but it does.

The Ruined Shrine          [Organic]

The Brotherhood Stones     [Organic]
  Tip: Rushing through a place and knowing a place aren't the same thing. I've learned that much.

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
Take it — the thought slides away before you finish it.

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.
Off. Take it… You lose the rest of the sentence.

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.
You don't need to take it off. Do you?

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 268 â€” ring off in the Creature Den
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove ring` `look` `examine bones` `save` `quit` `yes`
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> You try to take the ring off. Your fingers find it. They don't do what you ask.
Why would you take it off?

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.
It's fine. The ring is fine.

> You can't see any bones here!
The ring is warm, and you are warm, and everything is fine.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 269 â€” ring stuck test (NOT saved)
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> You aren't wearing the plain dark ring.

> Time passes...

> Time passes...

> Combat Room
The Warden stands between you and the open door, swaying, waiting for you to move.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
The Warden stands between you and the open door, swaying, waiting for you to move.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 270 â€” ring off, saved in the Den
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove ring` `inventory` `save` `quit` `yes`
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 271.1 â€” remove ring retest (NOT saved)
```

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.
```

## Launch 271.2 â€” remove ring retest (NOT saved)
```

> You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.
```

## Launch 271.3 â€” remove ring retest (NOT saved)
```

> You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.
```

## Launch 272.1 â€” remove ring and save (retry)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove ring` `look` `save` `quit` `yes`
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 272.2 â€” remove ring and save (retry)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `remove ring` `look` `save` `quit` `yes`
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> You remove the ring. Whatever it wants, it didn't get it this time.
Plain dark ring removed.

> Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 273 â€” north from the Den
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `save` `quit` `yes`
```
> Restored.
Creature Den
A low den that stinks of old straw and older meat. Bones are piled in one corner with a care that's somehow worse than if they'd been scattered. A passage leads on to the north.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.
You spot a suspiciously clean pressure plate set into the cave floor and are able to disarm it, neutralizing it.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 274 â€” the levers
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine levers` `examine left lever` `examine middle lever` `examine right lever` `examine sluice` `examine plate` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> You can't see any levers here!

> You see nothing special about the left lever.

> You see nothing special about the middle lever.

> You see nothing special about the right lever.

> You can't see any sluice here!

> You see nothing special about the pressure plate.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 275 â€” left lever
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pull left lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> The lever grinds but won't move.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 276 â€” middle and right levers
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pull middle lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Nothing happens.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 277 â€” right lever
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pull right lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> The lever snaps off in your hand.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 278 â€” forcing the left lever
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pry left lever with crowbar` `push left lever` `push middle lever` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> You can't get any leverage on that.

> Pushing the left lever has no effect.

> Pushing the middle lever has no effect.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 279 â€” jump on the Flooding Room plate (NOT saved)
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Nothing happens.

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Time passes...

> Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 280 â€” walking back past the Warden (NOT saved)
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Creature Den

> Combat Room
The Warden stands between you and the open door, swaying, waiting for you to move.

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Idol Room
The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.
At the center stands a stone pedestal. The room has the feeling of something that has been waiting for someone to make a mistake.
The pedestal has a pressure plate built into its surface — the salt's weight is holding it down now.
A sack of salt sits on the pedestal where the idol was.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 281 â€” pickaxe on the timbers (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `north` `north` `north` `east` `south` `south` `use pickaxe on timbers` `hit timbers with pickaxe` `chop timbers with pickaxe` `look` `save` `quit` `yes`
```
> Restored.
Flooding Room
A low cave, the floor dipping toward the middle and slick with old silt. Three iron levers stand in a row on the north wall — left, middle, right — above a grated sluice mouth. The only way out is back south.

> Creature Den

> Combat Room
The Warden stands between you and the open door, swaying, waiting for you to move.

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> You set the pickaxe into the first timber and lever. It groans, splinters, and comes down. Behind it, the second shifts.

> The second timber is wedged tighter. It gives anyway, all at once, and the third sags loose.

> That sentence isn't one I recognize.

> Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 282 â€” last timber, then east
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `use pickaxe on timbers` `east` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.

> The last timber comes away in two pieces. The way east is open — though the rock overhead creaks, and a little dust drifts down.

> The overhang creaks every time you move. It needs propping before you'd trust it.

> Collapsed Gallery
The passage runs east. The timbers are down, but the rock overhead sags where they were, and it creaks.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 283 â€” the beam for the overhang
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `take beam` `south` `south` `prop overhang with beam` `use beam` `east` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Gallery
The passage runs east. The timbers are down, but the rock overhead sags where they were, and it creaks.

> Collapsed Aqueduct

> Storage Area

> You take the support beam.

> Collapsed Aqueduct

> Collapsed Gallery

> You wrestle the support beam upright and wedge it under the worst of the overhang. The creaking stops.

> 
> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 284 â€” round two with the Warden (ASSISTED nudge)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `west` `south` `south` `south` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `attack warden with pale blade` `diagnose` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Collapsed Gallery

> Collapsed Aqueduct

> Storage Area

> Ink Corridor

> Narrow Passageway

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Combat Room
The Warden stands between you and the open door, swaying, waiting for you to move.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.

> The Warden's reach finds you. You take a hit.

> You land a solid blow. The Warden staggers, and comes on anyway.

> You land a solid blow. The Warden staggers, and comes on anyway.
The Warden goes down hard and doesn't get up. Something rolls from its grip and clatters across the floor — a lantern, unlit, its glass faintly green.

> You have 5 of 7 hearts.

> Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
An old lantern lies on the floor, its glass faintly green.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 285 â€” the lantern
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take lantern` `examine lantern` `light lantern` `rest` `diagnose` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.
An old lantern lies on the floor, its glass faintly green.

> You take the Guardian's Lantern.

> A guard's lantern, heavy brass, the glass tinted a faint green. It flickers when you lift it, as if it wants to light and can't decide where.

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> You sit with your back to the nearest wall and let your breathing slow. When you get up, some of the ache has gone with it.

> You have 6 of 7 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 286 â€” across the Rickety Bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `east` `south` `south` `east` `examine bridge` `south` `look` `save` `quit` `yes`
```
> Restored.
Combat Room
A long, low room, wider than it is deep, the floor scarred and the walls pocked with old damage. At the east end the heavy door stands open. Whatever happened in here happened more than once.

> Idol Room
A sack of salt sits on the pedestal where the idol was.

> Narrow Passageway

> Ink Corridor

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> Rickety Bridge

> You can't see any bridge here!

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 287 â€” lightening the load
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop cart` `drop shovel` `drop pickaxe` `south` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> You drop the hand cart.

> You drop the shovel.

> You drop the pickaxe.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 288 â€” lightening further
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop crowbar` `drop bow` `drop torch` `drop idol` `south` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.

> You drop the crowbar.

> You drop the bow.

> You toss the burnt-out torch aside. It's no good to anyone now.

> You drop the Chachapoyan Fertility Idol.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 289 â€” what am I carrying?
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `inventory` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.

> You are carrying:
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Large bowl piece
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Pale Blade
  Flint and steel
  Treasure map
  Pie Rat Coin
  Heart necklace (not worn)
  Muddy bowl piece
  Grey rune stone
  Town charter
  Portcullis bar
  Small clay pot
  Smoke jar
  Vial of glacier melt
  Guardian's Lantern
You have 74 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 290 â€” dropping the bar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop bar` `south` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.

> You drop the portcullis bar.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 291 â€” bridge weight test (NOT saved)
```
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.

> You drop the coil of rope.

> You drop the flat rune stone.

> You drop the grey rune stone.

> You drop the large bowl piece.

> You drop the muddy bowl piece.

> You drop the Pie Rat disguise.

> You drop the Guardian's Lantern.

> Which blade do you mean, the dagger, or the Pale Blade?

> You drop the small clay pot.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 292 â€” bridge tests: ring / drop all (NOT saved)
```
There is a portcullis bar here.

> "Bring it to me, or keep it close," Will said. You keep it close.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> Quit now? (type "no" to save first) [yes/no] 
-----
There is a portcullis bar here.

> You drop the dagger.
You drop the wax seal.
You drop the lockpicks.
You drop the thin paper.
You drop the coil of rope.
You drop the large bowl piece.
You drop the Pie Rat disguise.
You drop the flat rune stone.
You drop the Tip Journal.
You drop the Pale Blade.
You drop the flint and steel.
You drop the treasure map.
You drop the Pie Rat Coin.
You drop the heart necklace.
You drop the muddy bowl piece.
You drop the grey rune stone.
You drop the town charter.
You drop the small clay pot.
You drop the smoke jar.
You drop the vial of glacier melt.
You drop the Guardian's Lantern.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> You are carrying:
  Plain dark ring (not worn)
You have 74 Zenni.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 293 â€” lockpicks on the Key Door (NOT saved)
```
There is a portcullis bar here.

> You drop the dagger.

> You take the lockpicks.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> That sentence isn't one I recognize.

> That key doesn't fit.

> You see nothing special about the iron door.

> The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> Rickety Bridge
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a dagger here.
There is a wax seal here.
There is some thin paper here.
There is a coil of rope here.
There is a large bowl piece here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a Pale Blade here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a small clay pot here.
There is a smoke jar here.
There is a vial of glacier melt here.
There is a Guardian's Lantern here.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 294 â€” the Shrine Room
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `take fragment` `examine plinth` `examine bowl` `put pieces in bowl` `put large piece on plinth` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.
Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.

> You take the stone bowl piece.

> You can't see any plinth here!

> Which bowl do you mean, the large bowl piece, the muddy bowl piece, or the stone bowl piece?

> You can't see any pieces here!

> You can't see any plinth here!

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 295 â€” assembling the bowl
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `combine large piece with muddy piece` `assemble bowl` `repair bowl` `put stone piece on large piece` `drop large piece` `look` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> You can't mix that.

> The pieces fit, but nothing holds them together.

> The pieces fit, but nothing holds them together.

> You can't put the stone bowl piece on the large bowl piece.

> You drop the large bowl piece.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.
There is a large bowl piece here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 296 â€” gluing the bowl
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take large piece` `repair bowl with wax` `assemble bowl with wax seal` `light lantern` `inventory` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.
There is a large bowl piece here.

> You take the large bowl piece.

> Which bowl do you mean, the muddy bowl piece, the stone bowl piece, or the large bowl piece?

> That sentence isn't one I recognize.

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> You are carrying:
  Dagger
  Wax seal
  Lockpicks
  Thin paper
  Plain dark ring (not worn)
  Coil of rope
  Pie Rat disguise (not worn)
  Flat rune stone
  Tip Journal
  Pale Blade
  Flint and steel
  Treasure map
  Pie Rat Coin
  Heart necklace (not worn)
  Muddy bowl piece
  Grey rune stone
  Town charter
  Small clay pot
  Smoke jar
  Vial of glacier melt
  Guardian's Lantern
  Stone bowl piece
  Large bowl piece
You have 74 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 297 â€” where did the cart go?
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `take cart` `examine cart` `west` `north` `north` `west` `take cart` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Rickety Bridge
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.

> You take the hand cart.

> A sturdy two-wheeled cart, the handles worn smooth. Built to carry more than a person could.

> Collapsed Gallery

> Collapsed Aqueduct

> Storage Area

> Ink Corridor

> You already have the hand cart.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 298 â€” collecting gear at the bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `south` `south` `east` `take all` `look` `save` `quit` `yes`
```
> Restored.
Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> Rickety Bridge
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.

> You take the shovel.
You take the pickaxe.
You take the crowbar.
You take the bow.
You take the Chachapoyan Fertility Idol.
You take the portcullis bar.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 299 â€” back to the surface
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `west` `north` `north` `north` `east` `south` `up` `up` `north` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Collapsed Gallery

> Collapsed Aqueduct

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

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 300 â€” the quest board
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `west` `look` `read board` `examine board` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You can't see any board here!

> You can't see any board here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 301 â€” the statue seam
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `pry statue with crowbar` `use crowbar on statue` `use bar on statue` `use pickaxe on statue` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You can't get any leverage on that.

> You work the crowbar into the seam and lean on it. Stone grinds against stone, and the base of the statue swings open on a hinge nobody was meant to find. Inside, in the dark: a silver stake, and a folded note.

> Which bar do you mean, the crowbar, or the portcullis bar?

> Nothing happens.

> Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
The statue stands to one side, its base pried open.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.
A silver stake lies in the hollow of the statue's base.
A folded note lies beside it, sealed with green wax.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 302 â€” stake and note
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take stake` `take note` `examine stake` `read note` `open note` `read note` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
The statue stands to one side, its base pried open.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.
A silver stake lies in the hollow of the statue's base.
A folded note lies beside it, sealed with green wax.

> You take the silver stake.

> You take the folded note.

> A slim stake of solid silver, the point still sharp. Someone hid this deliberately.

> "Kept here for whoever comes after me. I hope it's someone careful." There's no name — only the green wax seal.

> You can't open that.

> "Kept here for whoever comes after me. I hope it's someone careful." There's no name — only the green wax seal.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 303 â€” Town Hall board
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `read board` `examine board` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
The statue stands to one side, its base pried open and empty. Whatever was inside is gone.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above.

> You can't see any board here!

> You can't see any board here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 304 â€” board and May
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `read board` `talk to may` `save` `quit` `yes`
```
> Restored.
Town Hall
The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.
Inside, the foyer is wide and echoing, the floor worn smooth in a path from the doors to the stairs. The Council Chamber opens to the east, the Records Room to the west, and a staircase climbs to the floor above.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Notices are pinned to the board, newer ones over older:
WANTED: bog thyme, and a cooking pot that isn't cracked. Bring both to the kitchen. There's a stew in it. — Shamus
WANTED: a bone flute, somewhere in the middle passages below. Bring it to the forge beneath the volcano. — Pyronicus
SWARM LOOSE: my bees have taken up in a hollow tree at the forest edge. Help wanted bringing the queen home. Honey for your trouble. — the cottage west of the Old Oak

> May's eyes drop to the crowbar and stay there. "Now that's useful." She reaches under the bar and sets an iron key on the counter. "Cellar. It flooded years back — the drain clogged, and we shut the door and stopped thinking about it. If you can get the cover off that drain, it's yours to clear." She slides the key over. "Do it from the top of the stairs. Nobody goes down into that water."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 305 â€” the pot for Shamus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `give pot to shamus` `talk to shamus` `look` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Shamus puts the two together like they've been waiting for each other. The kitchen fills with a smell you haven't smelled in this town before — thick, green, and warm. "Hearty stew," he says. "Back on the menu. Tell May."

> Shamus wipes his hands on his apron. "What can I do for you?" He tips his head at the slate by the door. "Prices are up. Ask if you need something that isn't."

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 306 â€” the cellar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `unlock cellar door with key` `open cellar door` `examine cellar` `look down` `examine drain` `pry drain with crowbar` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.
Shamus works the kitchen with practiced efficiency.

> The key turns stiffly. The lock hasn't been asked to do anything in years. You leave it where it is.

> The cellar door comes up on a breath of cold, wet air. Stone steps lead down — three of them, then water, still and clear, filling the cellar nearly to the beams. At the foot of the steps, through the water, you can make out the square iron cover of a drain.

> You see nothing special about the cellar door.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> You see nothing special about the drain.

> You lie flat on the top step and reach the crowbar down through the water, feeling along the bottom step until the lip catches the edge of the grate. You lean on it. The cover comes up with a jolt and slides off into the dark.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 307 â€” waiting for the cellar to drain
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wait` `wait` `look` `down` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> Time passes...

> Time passes...

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> You start down the steps. On the fourth there isn't a step — only water, colder than it has any right to be. The kitchen's light shrinks to a square above you, and then it doesn't.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 308 â€” tipping May
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `tell may about stew` `tip may 10` `tip may 10` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Below it, water fills the stairwell almost to the top step.
Shamus works the kitchen with practiced efficiency.

> Bar

> You can't see any stew here!

> May counts the coins once, pockets them, and leans all the way across the bar. "Rowan," she says.
"There's a locked door down in the tunnels, they say. Heavy thing — needs a proper key. Word is someone in town might know something about it."

> May counts the coins once, pockets them, and leans all the way across the bar. "Rowan," she says.
"The Finch family goes back a long way in Roundabout. Rowan's grandfather was quite the explorer, from what I hear. Rowan works up at the Town Hall if you want to ask him about it."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 309 â€” the clerk about the Finches
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `west` `talk to clerk` `ask clerk about grandfather` `ask clerk about finch` `ask clerk about key` `ask clerk about calder` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> The clerk is turning the pocket watch over in his hands. He nods to you, but doesn't say anything.

> You can't see any grandfather here!

> You can't see any finch here!

> You can't see any key here!

> You can't see any calder here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 310 â€” cart to the gravestone
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `south` `west` `west` `north` `north` `north` `east` `south` `look` `examine gravestone` `put gravestone in cart` `load gravestone` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Town Hall

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

> The Bog of Eternal Stench
The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.
A narrow path leads east through the brush to a low, round yurt.
A gravestone lies face-down in the mud.

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> You tip the gravestone up out of the mud and walk it, corner by corner, onto the cart. The axle complains. The bog lets go of the stone with a sound you'd rather not have heard. The gravestone is loaded.

> It's already on the cart.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 311 â€” gravestone to the Graveyard
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `west` `south` `south` `south` `east` `east` `east` `south` `south` `place gravestone` `look` `save` `quit` `yes`
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

> Main East

> Church of All

> Graveyard

> You wheel the cart to the empty plot — a rectangle of disturbed earth with a broken stub of mortar at its head — and tip the gravestone back into place. It settles as if it remembers the spot. You leave the cart beside it; it's done its job.

> Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.
One headstone near the path stands straighter than the others, newly scrubbed of mud: CALDER FINCH — EXPLORER. An empty hand cart stands beside it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 312 â€” telling the clerk
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine gravestone` `north` `north` `west` `north` `west` `talk to clerk` `save` `quit` `yes`
```
> Restored.
Graveyard
The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it.
The church stands to the north. The mausoleum sits at the far end to the south, grey and patient.
To the east, a low building stands where there was nothing before — and you are not sure how you missed it.
It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity.
Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time.
The air is still in a way that has nothing to do with wind.
One headstone near the path stands straighter than the others, newly scrubbed of mud: CALDER FINCH — EXPLORER. An empty hand cart stands beside it.

> You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Records Room

> The clerk is turning the pocket watch over in his hands. He nods to you, but doesn't say anything.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 313 â€” other Town Hall rooms
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `look` `west` `up` `look` `save` `quit` `yes`
```
> Restored.
Records Room
Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone.
The room smells of old paper and the particular dust of things that have not been touched in years.
A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.

> Town Hall

> Council Chamber

> Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Upper Hall
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 314 â€” cabinet and council man
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine cabinet` `open cabinet` `down` `east` `talk to man` `examine man` `save` `quit` `yes`
```
> Restored.
Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> It's already open.

> Town Hall

> Council Chamber

> "I went out to the cemetery this morning," Rowan says. "Grandfather's stone is back where it belongs." Then, flatly: "That cart you left by the grave came from the dungeon. Don't bother denying it — I've seen it before, in my grandfather's papers." He studies you for a moment. "He left a key. Said it led to a lower level — wouldn't say what was down there." He holds it out. "Take it. It was never meant for me."
[Middle Tier Key added to inventory.]

> You see nothing special about the Councilman Rowan Finch.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 315 â€” smoke jar at the swarm
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `east` `east` `east` `north` `open smoke jar` `east` `look` `save` `quit` `yes`
```
> Restored.
Council Chamber
The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues.
A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years.
A man sits at the far end with the bearing of someone who has inherited both the title and the table.

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> You can't open that.

> Swarm Tree

> Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 316 â€” smoking the bees
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `use smoke jar` `look` `save` `quit` `yes`
```
> Restored.
Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.

> You break the wax and tip the jar toward the hollow. Grey smoke spills out, thick and slow, and pours into the gap in the bark. The drone falters and drops to a low, drowsy hum. The bees settle. Just inside the hollow, something small and glass catches the light.

> Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.
The bees drift in and out of the hollow, slow and drowsy, paying you no mind.
In the hollow, a small glass vial holds a single tagged bee.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 317 â€” the queen to the beekeeper
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take vial` `west` `west` `give vial to beekeeper` `talk to beekeeper` `look` `save` `quit` `yes`
```
> Restored.
Swarm Tree
A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.
The bees drift in and out of the hollow, slow and drowsy, paying you no mind.
In the hollow, a small glass vial holds a single tagged bee.

> You take the queen vial.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beekeeper's Cottage

> She takes the vial in both hands and holds it up to the light. "There she is," she says softly, to the bee rather than to you. When she looks up, she's smiling. "The rest will follow her home. Here — you've earned this." She presses a small jar of honey into your hands. It's faintly warm.
[Enchanted honey added to inventory.]

> "They're settling back in," she says, nodding toward the hives. "Took them a day to forgive me. Bees hold grudges."

> Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 318 â€” back down, lantern in the Crypt
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `south` `west` `west` `south` `south` `south` `cast light` `down` `light lantern` `look` `save` `quit` `yes`
```
> Restored.
Beekeeper's Cottage
A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Church of All

> Graveyard

> It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Mausoleum

> The Crypt

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 319 â€” down to the Rickety Bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `north` `west` `south` `south` `south` `east` `south` `south` `east` `look` `save` `quit` `yes`
```
> Restored.
The Crypt
The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.

> Charnel Walk

> The Bone Passage

> The Junction

> The Toll Bridge

> Dungeon Entrance

> Ink Corridor

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> Rickety Bridge

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 320 â€” crossing light
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop all` `take key` `take pale blade` `take honey` `take lantern` `south` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> You drop the dagger.
You drop the wax seal.
You drop the lockpicks.
You drop the thin paper.
You drop the coil of rope.
You drop the Pie Rat disguise.
You drop the flat rune stone.
You drop the Tip Journal.
You drop the Pale Blade.
You drop the flint and steel.
You drop the treasure map.
You drop the Pie Rat Coin.
You drop the heart necklace.
You drop the muddy bowl piece.
You drop the grey rune stone.
You drop the town charter.
You drop the vial of glacier melt.
You drop the Guardian's Lantern.
You drop the stone bowl piece.
You drop the large bowl piece.
You drop the shovel.
You drop the pickaxe.
You drop the crowbar.
You drop the bow.
You drop the Chachapoyan Fertility Idol.
You drop the portcullis bar.
You drop the silver stake.
You drop the folded note.
You drop the Middle Tier Key.
You drop the enchanted honey.

> You take the Middle Tier Key.

> You take the Pale Blade.

> You take the enchanted honey.

> You take the Guardian's Lantern.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 321 â€” the Middle Tier Key
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `unlock door with key` `open door` `south` `look` `save` `quit` `yes`
```
> Restored.
Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> The finch key goes in stiffly and turns with a sound like a dropped anvil. The iron door swings inward under its own weight. Beyond it, stone stairs lead down. You leave the key in the lock.

> You can't open that.

> Key Door Landing
The staircase deposits you in a rough cave at the bottom — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south.

> Key Door Landing
The staircase deposits you in a rough cave at the bottom — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 322 â€” south from the Landing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Key Door Landing
The staircase deposits you in a rough cave at the bottom — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 323 â€” Mine Passage items
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take charcoal` `take dust` `examine dust` `examine chest` `open chest` `look` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.
A few lumps of charcoal lie in a cold fire ring near the tools.
A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.

> You take the charcoal.

> You pinch the silver dust out of the crack and pocket it.

> A pinch of fine silver dust. It catches the light even down here.

> You see nothing special about the iron chest.

> The chest is locked. The lock looks pickable — if you had the tools.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 324 â€” fetching the lockpicks
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `look` `take lockpicks` `south` `south` `south` `unlock chest with lockpicks` `open chest` `look` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a dagger here.
There is a wax seal here.
There are lockpicks here.
There is some thin paper here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a silver stake here.
There is a folded note here.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a dagger here.
There is a wax seal here.
There are lockpicks here.
There is some thin paper here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a silver stake here.
There is a folded note here.

> You take the lockpicks.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> The lockpicks find the pins one by one, and the lid comes up with a groan. Inside are 20 Zenni, which you pocket.

> The chest is empty.

> Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall, its lid open.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 325 â€” beyond the Mine Passage
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Mine Passage
A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall, its lid open.

> Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.
A small pale stone near the base of the carved wall catches your eye — etched with faint lines.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.
A small pale stone near the base of the carved wall catches your eye — etched with faint lines.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 326 â€” inscription and stone
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take stone` `examine stone` `read inscription` `examine inscription` `examine snare` `disarm snare` `save` `quit` `yes`
```
> Restored.
Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.
A small pale stone near the base of the carved wall catches your eye — etched with faint lines.

> You take the pale rune stone.

> A pale stone, roughly square, with deep natural veins of darker mineral running through it like old script.

> Rows of characters cut into the smoothed stone, worn soft at the edges. Not a script you know. It would take a rubbing to carry it anywhere.

> Rows of characters cut into the smoothed stone, worn soft at the edges. Not a script you know. It would take a rubbing to carry it anywhere.

> You see nothing special about the snare.

> There's nothing here to disarm.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 327 â€” the rubbing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `north` `take paper` `south` `south` `south` `south` `rub inscription with charcoal` `make rubbing` `inventory` `save` `quit` `yes`
```
> Restored.
Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a dagger here.
There is a wax seal here.
There is some thin paper here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a silver stake here.
There is a folded note here.

> Which paper do you mean, the thin paper, or the folded note?

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Inscription Chamber

> You'd need something to take the rubbing on.

> You can't see any rubbing here!

> You are carrying:
  Plain dark ring (not worn)
  Pale Blade
  Enchanted honey
  Guardian's Lantern
  Charcoal
  Silver dust
  Lockpicks
  Pale rune stone
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 328 â€” the rubbing, again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `north` `take thin paper` `take silver stake` `south` `south` `south` `south` `rub inscription with charcoal` `inventory` `save` `quit` `yes`
```
> Restored.
Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a dagger here.
There is a wax seal here.
There is some thin paper here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a silver stake here.
There is a folded note here.

> You take the thin paper.

> You take the silver stake.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't see any inscription here!

> You are carrying:
  Plain dark ring (not worn)
  Pale Blade
  Enchanted honey
  Guardian's Lantern
  Charcoal
  Silver dust
  Lockpicks
  Pale rune stone
  Thin paper
  Silver stake
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 329 â€” the rubbing, third try
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop lockpicks` `drop stake` `south` `south` `south` `south` `rub inscription with charcoal` `inventory` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a folded note here.

> You drop the lockpicks.

> You drop the silver stake.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Inscription Chamber

> You press the thin paper flat against the carved wall and work the charcoal across it. The inscription comes up pale against the black, line by line. You peel the rubbing away carefully. The charcoal is worn down to nothing.

> You are carrying:
  Plain dark ring (not worn)
  Pale Blade
  Enchanted honey
  Guardian's Lantern
  Silver dust
  Pale rune stone
  Rubbing
You have 92 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 330 â€” east past the snare (NOT saved)
```
> Cave Creature's Lair
A low, rank-smelling hollow at the end of the crawlspace. The floor is matted with old bedding — grass, fur, things that were once other things — and gnawed bones are pushed against the walls. Whatever lives here isn't home. It hasn't been for a while, or it's only just left.
Among the bones lies one that's been hollowed and pierced along its length — a flute.

> Cave Creature's Lair
A low, rank-smelling hollow at the end of the crawlspace. The floor is matted with old bedding — grass, fur, things that were once other things — and gnawed bones are pushed against the walls. Whatever lives here isn't home. It hasn't been for a while, or it's only just left.
Among the bones lies one that's been hollowed and pierced along its length — a flute.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 331 â€” the bone flute
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `take flute` `examine flute` `west` `look` `save` `quit` `yes`
```
> Restored.
Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.

> Cave Creature's Lair
A low, rank-smelling hollow at the end of the crawlspace. The floor is matted with old bedding — grass, fur, things that were once other things — and gnawed bones are pushed against the walls. Whatever lives here isn't home. It hasn't been for a while, or it's only just left.
Among the bones lies one that's been hollowed and pierced along its length — a flute.

> You take the bone flute.

> A flute carved from a long, pale bone, finger holes drilled along its length. Someone made this with care. It wasn't the creature.

> Inscription Chamber

> Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 332 â€” Inscription Chamber exits
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `down` `light lantern` `look` `save` `quit` `yes`
```
> Restored.
Inscription Chamber
A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.
A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.
A loop of fine cord lies half-buried in the dirt in front of the gap — a snare, set and waiting.

> Echo Alcove
A shallow alcove, barely deeper than it is wide, the rock curved like the inside of a shell. Your own breathing comes back to you a beat late. A faint grinding drifts up from somewhere far below — bone on stone. The passage runs north and south.

> You can't go that way.

> You can't go that way.

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> Echo Alcove
A shallow alcove, barely deeper than it is wide, the rock curved like the inside of a shell. Your own breathing comes back to you a beat late. A faint grinding drifts up from somewhere far below — bone on stone. The passage runs north and south.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 333 â€” flute in the Echo Alcove, then south (NOT saved)
```

> That's silly!

> Echo Alcove
A shallow alcove, barely deeper than it is wide, the rock curved like the inside of a shell. Your own breathing comes back to you a beat late. A faint grinding drifts up from somewhere far below — bone on stone. The passage runs north and south.

> Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall points toward it. The ring of metallic filings around the latch is deliberate — a lodestone is built into the lid. Opening the chest without removing it first would be a problem.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall points toward it. The ring of metallic filings around the latch is deliberate — a lodestone is built into the lid. Opening the chest without removing it first would be a problem.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 334 â€” the Magnetic Vault
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `examine lodestone` `remove lodestone` `take lodestone` `examine chest` `look` `save` `quit` `yes`
```
> Restored.
Echo Alcove
A shallow alcove, barely deeper than it is wide, the rock curved like the inside of a shell. Your own breathing comes back to you a beat late. A faint grinding drifts up from somewhere far below — bone on stone. The passage runs north and south.

> Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall points toward it. The ring of metallic filings around the latch is deliberate — a lodestone is built into the lid. Opening the chest without removing it first would be a problem.
Something catches your eye, tucked out of sight: 1 Zenni. You pocket it.

> You see nothing special about the lodestone.

> You slide a hand under the lid's lip, find the lodestone and work it loose. The filings slump out of their ring. The chest is just a chest now.

> There's nothing left to disarm.

> You see nothing special about the chest.

> Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall still points toward it, though nothing pulls at it now. The filings lie in a loose scatter below the latch.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 335 â€” opening the vault chest
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open chest` `look` `save` `quit` `yes`
```
> Restored.
Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall still points toward it, though nothing pulls at it now. The filings lie in a loose scatter below the latch.

> The lid lifts easily. Inside, on a fold of black cloth, lies a diamond brooch.

> Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall still points toward it, though nothing pulls at it now. The filings lie in a loose scatter below the latch.
In the open chest lies a diamond brooch.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 336 â€” brooch and onward
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take brooch` `examine brooch` `south` `east` `west` `look` `save` `quit` `yes`
```
> Restored.
Magnetic Vault
A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall still points toward it, though nothing pulls at it now. The filings lie in a loose scatter below the latch.
In the open chest lies a diamond brooch.

> You take the diamond brooch.

> A brooch of worked silver set with a single diamond the size of a thumbnail. Even in this light it throws sparks.

> You hear music — a familiar melody. You have reached level 7!
Deep Lock Door
The passage ends at a door set deep into the stone. It is sealed absolutely — no lock visible, no handle, no gap at the frame. Whatever mechanism holds it closed is on the other side, or nowhere. This door does not open. The passage ends here.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> You can't go that way.

> You can't go that way.

> Deep Lock Door
The passage ends at a door set deep into the stone. It is sealed absolutely — no lock visible, no handle, no gap at the frame. Whatever mechanism holds it closed is on the other side, or nowhere. This door does not open. The passage ends here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 337 â€” back to the bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `north` `north` `north` `north` `north` `north` `look` `save` `quit` `yes`
```
> Restored.
Deep Lock Door
The passage ends at a door set deep into the stone. It is sealed absolutely — no lock visible, no handle, no gap at the frame. Whatever mechanism holds it closed is on the other side, or nowhere. This door does not open. The passage ends here.

> Magnetic Vault

> Echo Alcove

> Inscription Chamber

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a folded note here.
There are lockpicks here.
There is a silver stake here.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a folded note here.
There are lockpicks here.
There is a silver stake here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 338 â€” gear up, to the Archivist
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take all` `west` `north` `north` `west` `north` `north` `north` `east` `south` `up` `up` `north` `north` `north` `west` `west` `north` `east` `give rubbing to archivist` `talk to archivist` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a flat rune stone here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a Pie Rat Coin here.
There is a heart necklace here.
There is a muddy bowl piece here.
There is a grey rune stone here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a Chachapoyan Fertility Idol here.
There is a portcullis bar here.
There is a folded note here.
There are lockpicks here.
There is a silver stake here.

> You take the dagger.
You take the wax seal.
You take the coil of rope.
You take the Pie Rat disguise.
You take the flat rune stone.
You take the Tip Journal.
You take the flint and steel.
You take the treasure map.
You take the Pie Rat Coin.
You take the heart necklace.
You take the muddy bowl piece.
You take the grey rune stone.
You take the town charter.
You take the vial of glacier melt.
You take the stone bowl piece.
You take the large bowl piece.
You take the shovel.
You take the pickaxe.
You take the crowbar.
You take the bow.
You take the Chachapoyan Fertility Idol.
You take the portcullis bar.
You take the folded note.
You take the lockpicks.
You take the silver stake.

> Collapsed Gallery

> Collapsed Aqueduct

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

> Library — Main Hall

> The Stacks

> He takes the rubbing and holds it to the light without speaking for a moment.
"Yes." He sets it down flat, smoothing the edges. "This appears to be an answer to a question I was never able to find." He opens a drawer and produces a rolled scroll. "Take this. I've had it for years — couldn't place it. I suspect you'll find the question before I would."
[Incantation scroll added to inventory.]

> He is already working when you arrive.
"Whatever that engraving answers — I suspect it's somewhere in the lower passages. Somewhere that feels like it's waiting." He doesn't look up. "That's not intuition. That's just what the text implies."

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 339 â€” stones to Ivanaar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `west` `west` `look` `give stones to ivanaar` `talk to ivanaar` `save` `quit` `yes`
```
> Restored.
The Stacks
The passage from the Main Hall opens into something that shouldn't fit inside this building.
The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight.
At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space.
The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.

> Library — Main Hall

> Main West

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Viking Encampment
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Aylora is slumped on the bench, snoring.

> Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Aylora is slumped on the bench, snoring.

> Ivanaar turns the stones over in his hands, one by one. He doesn't speak for a long moment.
When he looks up, something has settled in his expression that wasn't there before.
"Rowan."
He says it the way you'd say the name of someone you've decided to trust. He sets the stones down and disappears into the longhouse.
He returns with a folded tunic — Brotherhood weave, the runes along the hem faintly lit now.
"Wear it," he says, and hands it over.
He returns to his fire.
[Ivanaar's Tunic added to inventory.]

> Ivanaar returns to his fire.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 340 â€” tunic, then flute to Pyronicus
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `wear tunic` `examine tunic` `east` `east` `east` `east` `east` `south` `down` `give flute to pyronicus` `talk to pyronicus` `save` `quit` `yes`
```
> Restored.
Viking Encampment
Longhouses ring a wide clearing, smoke rising from their roof-holes. A banner hangs from a pole near the largest one, its runes stitched in thread gone dark with weather.
Vikings go about their business — mending, sharpening, arguing — and keep half an eye on you while they do it. Paths lead north to a hut, south to a ring of stones, and west toward the glow of a fire pit.
Ivanaar Stormbringer sits by the central fire, watching you with the patience of someone who expects to be impressed or disappointed, and has not decided which.
Aylora is slumped on the bench, snoring.

> You pull the tunic on. The weave settles across your shoulders, lighter than it looks.

> A tunic of Brotherhood weave, old but not worn. The runes along the hem and collar glow faintly, restored.

> Archery Range
Raznak stands at the near end of the range, watching the targets.

> Main West

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> The Volcano

> Pyronicus's Forge
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> Pyronicus takes the flute and turns it once in the forge light. "Not the creature's," he says. "Someone played this for it." He sets it on the workbench with more care than you expected, then hands you a scroll sealed with a dab of black wax. "Fire. You'll want it below."
[Fireball scroll added to inventory.]

> He goes back to what he was doing. The conversation, apparently, is over.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 341 â€” scrolls to Will
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `north` `west` `west` `south` `open mailbox` `give fireball scroll to will` `give incantation scroll to will` `talk to will` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
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

> Will glances at the scroll, then at you. He takes it without ceremony and unrolls it, reading silently for a moment. Then he reads it aloud — not to you, exactly, more as if the words need to be heard in the right kind of room. When he finishes, you understand it. You're not sure how. "Keep that," he says, nodding at the space where the scroll was. It's gone. "The knowing, I mean."
[Fireball spell learned.]

> Will Passion doesn't take the incantation scroll.

> There's no response from the Will Passion.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 342 â€” incantation scroll, then the drain (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine incantation scroll` `read incantation scroll` `examine painting` `south` `south` `clear drain` `look` `save` `quit` `yes`
```
> Restored.
Will's Wizard Tower
The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.
Will Passion sits at his desk, pen in hand.
A small lacquered music box sits open on the corner of Will's desk.

> A rolled scroll, the paper gone soft with age. The writing runs in close, even lines in no script you know — and yet the words sit easily in your mouth when you look at them.

> You read the words under your breath. Nothing answers. Wherever these are meant to be spoken, it isn't here.

> The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.
Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
Shamus works the kitchen with practiced efficiency.

> You work the crowbar down into the open drain and lever. Something gives — a fist of rotted sacking and root comes up through the water — and the whole cellar starts to turn. The water drops a step, then another, then goes all at once with a long, sucking roar you feel through the kitchen floor. When it's quiet again, the stairs go all the way down.

> Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 343 â€” the cellar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `look` `save` `quit` `yes`
```
> Restored.
Kitchen
The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing.
Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking.
Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center.
Prices are chalked on a slate by the door.
The cellar door stands open near the far wall, May's key still in the lock. Stone steps lead down into the cellar.
Shamus works the kitchen with practiced efficiency.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 344 â€” cashbox and oak door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `open cashbox` `take cashbox` `open door` `west` `look` `save` `quit` `yes`
```
> Restored.
Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> The lid gives on the third try. Inside, wrapped in oilcloth and perfectly dry: 10 Zenni. Somebody planned for the flood better than they planned for the drain.

> You can't take the cashbox.

> The door swings inward onto dark stone. Cold air comes through it, and the smell of old earth.

> It is pitch black. You are likely to be eaten by a grue.

> It is pitch black. You are likely to be eaten by a grue.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 345 â€” light beyond the oak door
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `cast light` `look` `save` `quit` `yes`
```
> Restored.
It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Bone Passage

> The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 346 â€” wearing the heart necklace (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `diagnose` `wear necklace` `examine necklace` `diagnose` `save` `quit` `yes`
```
> Restored.
The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> You have 7 of 8 hearts.

> You put on the heart necklace.

> A simple cord with a clay charm, worn smooth.

> You have 8 of 9 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 347 â€” the Town Hall's third floor (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `up` `north` `north` `north` `north` `up` `look` `up` `look` `save` `quit` `yes`
```
> Restored.
The Bone Passage
The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs south. Whatever built this part didn't build it at the same time as the rest. The name feels earned.
In the east wall, a low door of black oak is set into the older stone.

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Bar

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Upper Hall

> Upper Hall
The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here.
A long hall with a runner of carpet gone thin at the center.
A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.
Something catches your eye, tucked out of sight: 5 Zenni. You pocket them.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 348 â€” the Trophy Case
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine case` `open case` `put idol in case` `put brooch in case` `look` `score` `save` `quit` `yes`
```
> Restored.
The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
The case has not been added to in some time.

> The case is well-made — solid glass panels, brass fittings, velvet lining gone slightly pale with age. Whoever built it expected it to hold things worth looking at.
At the moment it holds nothing. The placard below names the donor.
The velvet has the faint impressions of items once displayed here and since removed — or perhaps never placed at all.

> The glass door swings open on its brass hinges.

> The Chachapoyan Fertility Idol settles into the velvet. The case is a better place for it.

> The diamond brooch settles into the velvet. The case is a better place for it.

> The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. Behind the glass: the Chachapoyan Fertility Idol and the diamond brooch.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
Someone has been adding to it.

> Score: 75
Level 7 (360 XP)
Zenni: 129
2 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 349 â€” more for the case?
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `put coin in case` `put silver dust in case` `score` `save` `quit` `yes`
```
> Restored.
The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. Behind the glass: the Chachapoyan Fertility Idol and the diamond brooch.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
Someone has been adding to it.

> The Pie Rat Coin settles into the velvet. The case is a better place for it.

> The case is for treasures. That isn't one.

> Score: 93
Level 7 (360 XP)
Zenni: 129
3 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 350 â€” back down to the mid tier
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `down` `south` `south` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `east` `south` `south` `east` `look` `save` `quit` `yes`
```
> Restored.
The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. Behind the glass: the Chachapoyan Fertility Idol, the diamond brooch and the Pie Rat Coin.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
Someone has been adding to it.

> Upper Hall

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

> It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Bone Passage

> The Junction

> The Toll Bridge

> Dungeon Entrance

> Ink Corridor

> Storage Area

> Collapsed Aqueduct

> Collapsed Gallery

> Rickety Bridge

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 351 â€” the Storage Area (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `look` `examine east wall` `examine wall` `light lantern` `read incantation scroll` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Collapsed Gallery

> Collapsed Aqueduct

> Storage Area

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Scuffs in the dust show where equipment once stood. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> You can't see any wall here!

> You can't see any wall here!

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> You read the words under your breath. Nothing answers. Wherever these are meant to be spoken, it isn't here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 352 â€” the solid east wall (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `knock on wall` `search` `cast fireball` `look` `save` `quit` `yes`
```
> Restored.
Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Scuffs in the dust show where equipment once stood. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> You can't go that way.

> You can't see any wall here!

> You search carefully but find nothing unusual.

> Nothing here answers the spell.

> Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Scuffs in the dust show where equipment once stood. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 353 â€” Supply Room trip mechanism (ASSISTED, NOT saved)
```

> You can't go that way.

> Ink Corridor

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.

> You can't see any shelf here!

> You can't see any mechanism here!

> You can't see any mechanism here!

> Ink Corridor
The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead — west, east, and on to the south.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 354 â€” Supply Room trip mechanism (ASSISTED, NOT saved)
```

> Ink Corridor

> Supply Room

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.

> You can't see any shelf here!

> You can't see any mechanism here!

> You can't see any mechanism here!

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 355 â€” Supply Room nouns (ASSISTED, NOT saved)
```

> Supply Room

> You can't see any plate here!

> You can't see any trip here!

> You can't see any shelves here!

> You can't see any plate here!

> Supply Room
A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned.
The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.
One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 356 â€” Storage Area attempts (ASSISTED, NOT saved)
```

> You can't see any scuffs here!

> A pinch of fine silver dust. It catches the light even down here.

> You can't see any floor here!

> You hear nothing out of the ordinary.

> There's nothing here worth digging for.

> You can't see any wall here!

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 357 â€” to the Mine Passage (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `drop all` `take pale blade` `take honey` `take lantern` `take incantation scroll` `take silver dust` `take lockpicks` `south` `south` `south` `east` `look` `save` `quit` `yes`
```
> Restored.
Storage Area
A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Scuffs in the dust show where equipment once stood. The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.

> Collapsed Aqueduct

> You can't go that way.

> You drop the Pale Blade.
You drop the enchanted honey.
You drop the Guardian's Lantern.
You drop the silver dust.
You drop the dagger.
You drop the wax seal.
You drop the coil of rope.
You drop the Pie Rat disguise.
You drop the Tip Journal.
You drop the flint and steel.
You drop the treasure map.
You drop the muddy bowl piece.
You drop the town charter.
You drop the vial of glacier melt.
You drop the stone bowl piece.
You drop the large bowl piece.
You drop the shovel.
You drop the pickaxe.
You drop the crowbar.
You drop the bow.
You drop the portcullis bar.
You drop the folded note.
You drop the lockpicks.
You drop the silver stake.
You drop the incantation scroll.

> You take the Pale Blade.

> You take the enchanted honey.

> You take the Guardian's Lantern.

> You take the incantation scroll.

> You pinch the silver dust out of the crack and pocket it.

> You take the lockpicks.

> Collapsed Gallery

> You can't go that way.

> You can't go that way.

> Rickety Bridge

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 358 â€” east of the Mine Passage (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `east` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.

> Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 359 â€” the rubble (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine rubble` `search` `dig` `move rubble` `light lantern` `save` `quit` `yes`
```
> Restored.
Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.

> You can't see any rubble here!

> You search carefully but find nothing unusual.

> The fill is packed too tight to move by hand. You'd need a shovel.

> You can't see any rubble here!

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 360 â€” fetch the shovel and dig
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `north` `west` `north` `take shovel` `south` `east` `south` `south` `south` `east` `dig` `look` `save` `quit` `yes`
```
> Restored.
Stored Room
The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a shovel here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a silver stake here.

> You take the shovel.

> Collapsed Gallery

> Rickety Bridge

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't go that way.

> There's nothing here worth digging for.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 361 â€” shovel across the bridge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `drop lantern` `drop lockpicks` `drop honey` `south` `south` `south` `east` `dig` `look` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> You drop the Guardian's Lantern.

> You drop the lockpicks.

> You drop the enchanted honey.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Stored Room

> The shovel bites into the packed rubble and the floor gives way — the fill cascades into the darkness below. You scramble back from the edge. A gaping hole now separates you from the eastern passage.

> Hole to Below
Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.
One of the old support timbers juts out over the edge, still sound.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 362 â€” the hole
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine timber` `examine hole` `down` `east` `save` `quit` `yes`
```
> Restored.
Hole to Below
Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.
One of the old support timbers juts out over the edge, still sound.

> You see nothing special about the support timber.

> You can't see any hole here!

> The drop is serious. You'd need something to climb down on.

> The gap where the floor used to be is far too wide to cross.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 363 â€” rope for the timber
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `north` `west` `north` `drop shovel` `take rope` `south` `east` `south` `south` `south` `east` `tie rope to timber` `look` `save` `quit` `yes`
```
> Restored.
Hole to Below
Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.
One of the old support timbers juts out over the edge, still sound.

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a Guardian's Lantern here.
There are lockpicks here.
There is some enchanted honey here.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a coil of rope here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a silver stake here.

> You drop the shovel.

> You take the coil of rope.

> Collapsed Gallery

> Rickety Bridge
There is a Guardian's Lantern here.
There are lockpicks here.
There is some enchanted honey here.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Hole to Below

> You knot the rope around the timber and pay it out over the edge. It goes taut, then slack — the far end is resting on something solid.

> Hole to Below
Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.
One of the old support timbers juts out over the edge, still sound.
A rope is knotted around the timber, hanging down into the dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 364 â€” lantern and honey, then down
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `north` `take lantern` `take honey` `take lockpicks` `south` `south` `south` `east` `down` `look` `inventory` `save` `quit` `yes`
```
> Restored.
Hole to Below
Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.
One of the old support timbers juts out over the edge, still sound.
A rope is knotted around the timber, hanging down into the dark.

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is a Guardian's Lantern here.
There are lockpicks here.
There is some enchanted honey here.

> You take the Guardian's Lantern.

> You take the enchanted honey.

> You take the lockpicks.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Hole to Below

> Pile of Rubble
The ceiling is a jagged wound — stone and packed earth hanging at the edge where the floor above used to be. Below that: the rubble that was the floor, now a rough-graded pile you're standing on. The air smells of disturbed earth and something older underneath it. Passages lead north, east, and south.

> Pile of Rubble
The ceiling is a jagged wound — stone and packed earth hanging at the edge where the floor above used to be. Below that: the rubble that was the floor, now a rough-graded pile you're standing on. The air smells of disturbed earth and something older underneath it. Passages lead north, east, and south.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Incantation scroll
  Silver dust
  Guardian's Lantern
  Enchanted honey
  Lockpicks
You have 129 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 365 â€” Pile of Rubble north
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `light lantern` `save` `quit` `yes`
```
> Restored.
Pile of Rubble
The ceiling is a jagged wound — stone and packed earth hanging at the edge where the floor above used to be. Below that: the rubble that was the floor, now a rough-graded pile you're standing on. The air smells of disturbed earth and something older underneath it. Passages lead north, east, and south.

> Lower Crypt
A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.
The skeleton's fingers are curled loosely around a ring of keys.

> Lower Crypt
A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.
The skeleton's fingers are curled loosely around a ring of keys.

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 366 â€” the Keeper's keys
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take keys` `examine keys` `examine skeleton` `search skeleton` `north` `east` `west` `save` `quit` `yes`
```
> Restored.
Lower Crypt
A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.
The skeleton's fingers are curled loosely around a ring of keys.

> You take the key ring.

> A ring of keys, old iron, worn smooth from years of use.

> The robes have rotted at the seams, but the cord around the skeleton's neck has held. On it hangs a disc of emerald-green wax.

> You search carefully but find nothing unusual.

> Thermal Vent Room
A dead end, and a warm one. Heat rises from fissures in the floor, faint but steady, and the air smells of hot stone. The only way out is back south.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> You can't go that way.

> You can't go that way.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 367 â€” vent and wax disc
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `light lantern` `read incantation scroll` `search` `south` `take disc` `take wax` `examine pendulum` `save` `quit` `yes`
```
> Restored.
Thermal Vent Room
A dead end, and a warm one. Heat rises from fissures in the floor, faint but steady, and the air smells of hot stone. The only way out is back south.

> The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.

> You read the words under your breath. Nothing answers. Wherever these are meant to be spoken, it isn't here.

> You search carefully but find nothing unusual.

> Lower Crypt

> It's the Keeper's. You leave it with him.

> It's the Keeper's. You leave it with him.

> The blade hangs dead still, a curved length of iron as wide as a man. The edge is dark with old blood.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 368 â€” Pile of Rubble east
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `east` `look` `save` `quit` `yes`
```
> Restored.
Lower Crypt
A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.

> Pile of Rubble

> Antechamber
A low chamber, its floor carpeted wall to wall in dry bones — not scattered, laid, every one of them placed. Doorways lead east and south; the way you came is west.
The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here.

> Antechamber
A low chamber, its floor carpeted wall to wall in dry bones — not scattered, laid, every one of them placed. Doorways lead east and south; the way you came is west.
The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 369 â€” Antechamber east (NOT saved)
```

> The bones crack underfoot. The grinding stops. Then the doorway fills.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 369 â€” Antechamber south (NOT saved)
```

> The bones crack underfoot. The grinding stops. Then the doorway fills.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 370 â€” Antechamber: sneak east (NOT saved)
```

> I don't know the word "sneak".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: tiptoe east (NOT saved)
```

> I don't know the word "tiptoe".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: crawl east (NOT saved)
```

> I don't know the word "crawl".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: move bones (NOT saved)
```

> You can't move the bones.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: clear bones (NOT saved)
```

> You crouch and work slowly, lifting the bones aside one at a time and setting each down without a sound, until a narrow path of bare stone runs across the room. Beyond the south doorway, the grinding goes on, unbothered.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: examine bones (NOT saved)
```

> You see nothing special about the bones.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 370 â€” Antechamber: listen (NOT saved)
```

> You hear nothing out of the ordinary.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 371 â€” clearing the bones, east
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `clear bones` `east` `look` `save` `quit` `yes`
```
> Restored.
Antechamber
A low chamber, its floor carpeted wall to wall in dry bones — not scattered, laid, every one of them placed. Doorways lead east and south; the way you came is west.
The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here.

> You crouch and work slowly, lifting the bones aside one at a time and setting each down without a sound, until a narrow path of bare stone runs across the room. Beyond the south doorway, the grinding goes on, unbothered.

> The Lower Crossing
The passage widens here into a rough crossing, the stone walls bearing the marks of tools long since abandoned. Three directions offer themselves without comment. The floor is grit and old dust.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.

> The Lower Crossing
The passage widens here into a rough crossing, the stone walls bearing the marks of tools long since abandoned. Three directions offer themselves without comment. The floor is grit and old dust.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 372 â€” Lower Crossing north (NOT saved)
```
> Tool Alcove
The passage ends at a shallow recess lined with iron brackets — the kind used to hang tools or equipment. The brackets are empty. The back wall is flat and featureless.
Something in the back wall notices you. You're not sure how you know that, but you do.
As you focus on the back wall, it asks you something. Once. The sound of it fills the alcove and then is gone, leaving only the clear impression that an answer is expected.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 372 â€” Lower Crossing east (NOT saved)
```
> The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 372 â€” Lower Crossing south (NOT saved)
```
> Dark Room
You cannot see anything. This is not like being in the dark. This is something the dark is doing on purpose.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 373 â€” answering the wall
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `read incantation scroll` `look` `save` `quit` `yes`
```
> Restored.
The Lower Crossing
The passage widens here into a rough crossing, the stone walls bearing the marks of tools long since abandoned. Three directions offer themselves without comment. The floor is grit and old dust.

> Tool Alcove
The passage ends at a shallow recess lined with iron brackets — the kind used to hang tools or equipment. The brackets are empty. The back wall is flat and featureless.
Something in the back wall notices you. You're not sure how you know that, but you do.
As you focus on the back wall, it asks you something. Once. The sound of it fills the alcove and then is gone, leaving only the clear impression that an answer is expected.

> The wall goes quiet in a way it wasn't quiet before. Then, slowly, it opens. You get the sense it had begun to doubt anyone would ever answer.

> Tool Alcove
The passage ends at a shallow recess lined with empty iron brackets. The back wall stands open. It has nothing left to ask.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 374 â€” through the wall
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `look` `save` `quit` `yes`
```
> Restored.
Tool Alcove
The passage ends at a shallow recess lined with empty iron brackets. The back wall stands open. It has nothing left to ask.

> The Flooded Passage
Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.

> The Flooded Passage
Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 375 â€” the Dark Room
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine pool` `south` `south` `south` `light lantern` `look` `save` `quit` `yes`
```
> Restored.
The Flooded Passage
Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.

> You see nothing special about the pool.

> Tool Alcove

> The Lower Crossing

> Dark Room
You cannot see anything. This is not like being in the dark. This is something the dark is doing on purpose.

> The lantern opens and the darkness collapses. No gradual brightening — one moment nothing, the next a plain stone room, fully lit, as if it had always been waiting to be seen.
Unremarkable in every way except one: it is not dark. After what just happened, that feels like quite a lot.
There is a hook on the wall. You hang the lantern on it. It feels like the right thing to do, and apparently it was.

> Dark Room
A plain stone room, unremarkable in every way. Stone walls, stone floor, passages north and south. The Guardian's Lantern burns steadily on the wall. It is not dark.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 376 â€” south of the Dark Room
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `look` `save` `quit` `yes`
```
> Restored.
Dark Room
A plain stone room, unremarkable in every way. Stone walls, stone floor, passages north and south. The Guardian's Lantern burns steadily on the wall. It is not dark.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 377 â€” Spirit Room: cast unbind undead (NOT saved)
```

> Nothing here answers the spell.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 377 â€” Spirit Room: east (NOT saved)
```

> You can't go that way.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 377 â€” Spirit Room: west (NOT saved)
```

> You can't go that way.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 378 â€” Spirit Room: south / look (NOT saved)
```

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 378 â€” Spirit Room: examine shapes / examine spirits (NOT saved)
```

> Shapes, mostly. Sparse, irregular, never quite where you looked. Somewhere between six and nine of them; they won't hold still long enough to count.

> Shapes, mostly. Sparse, irregular, never quite where you looked. Somewhere between six and nine of them; they won't hold still long enough to count.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 378 â€” Spirit Room: talk to spirits / cast light (NOT saved)
```

> There's no response from the spirits.

> The light's already with you.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 379 â€” Spirit Room: use silver dust (NOT saved)
```

> Nothing happens.

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 379 â€” Spirit Room: throw silver dust at spirits (NOT saved)
```

> You'd rather keep hold of the silver dust.

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 379 â€” Spirit Room: scatter silver dust (NOT saved)
```

> That sentence isn't one I recognize.

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 380 â€” Spirit Room with the ring (NOT saved)
```

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The attention in the room drops all at once — not gradually, immediately. The shapes drift back to their own patterns. They have forgotten you entirely.
You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 381 â€” Spirit Room with the ring, moving on (NOT saved)
```

> You slip the ring on. When you look down, your hand is still there — but only because you know where to look.
The attention in the room drops all at once — not gradually, immediately. The shapes drift back to their own patterns. They have forgotten you entirely.
You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 382 â€” the Narrow Pass (NOT saved)
```

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.

> You can't go that way.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> You can't go that way.

> Spirit Room
The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passages on either side are visible. Getting to them is another matter.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 383 â€” restored the Dark Room backup; to the Narrow Pass
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `look` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
Dark Room
A plain stone room, unremarkable in every way. Stone walls, stone floor, passages north and south. The Guardian's Lantern burns steadily on the wall. It is not dark.

> Dark Room
A plain stone room, unremarkable in every way. Stone walls, stone floor, passages north and south. The Guardian's Lantern burns steadily on the wall. It is not dark.

> The Lower Crossing

> The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 384 â€” east of the Narrow Pass (NOT saved)
```
> The Still Den
A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. Something lies curled at the far end of the oval, grey and motionless. That changes the moment you enter.
An ivory torch is set in an iron bracket on the wall. There's no flame at its head, but the air around it shimmers with heat.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
An ivory torch is set in an iron bracket on the wall. There's no flame at its head, but the air around it shimmers with heat.
The werewolf lunges. You get clear — barely.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 385 â€” werewolf: put silver dust on pale blade (NOT saved)
```
The werewolf lunges. You get clear — barely.
> The Still Den
Claws rake the air where you were standing a moment ago.
> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 385 â€” werewolf: rub silver dust on blade (NOT saved)
```
The werewolf's claws find you.
> The Still Den
The werewolf lunges. You get clear — barely.
> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 385 â€” werewolf: attack werewolf with pale blade (NOT saved)
```
The werewolf's claws find you.
> The Still Den
The werewolf lunges. You get clear — barely.
> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 385 â€” werewolf: cast fireball (NOT saved)
```
The werewolf lunges. You get clear — barely.
> The Still Den
Claws rake the air where you were standing a moment ago.
> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 386 â€” werewolf: put silver dust on pale blade (NOT saved)
```

> You can't put the silver dust on the Pale Blade.
The werewolf's claws find you.
Something in the weave absorbed it. You felt the impact — and then didn't.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 386 â€” werewolf: attack werewolf with pale blade (NOT saved)
```
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 386 â€” werewolf: cast fireball (NOT saved)
```
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> The fire takes hold for a moment — then dies. Whatever this creature is made of, it isn't interested in burning.
The werewolf lunges. You get clear — barely.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 387 â€” fetching the stake and the vial
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `west` `west` `up` `west` `north` `north` `north` `west` `north` `drop lockpicks` `drop key ring` `drop silver dust` `drop incantation scroll` `take silver stake` `take vial` `south` `east` `south` `south` `south` `east` `down` `inventory` `save` `quit` `yes`
```
> Restored.
The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.

> The Lower Crossing

> Antechamber

> Pile of Rubble

> Hole to Below

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a vial of glacier melt here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a silver stake here.
There is a shovel here.

> You drop the lockpicks.

> You can't see any ring here!

> You drop the silver dust.

> You drop the incantation scroll.

> You take the silver stake.

> You take the vial of glacier melt.

> Collapsed Gallery

> Rickety Bridge

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Hole to Below

> Pile of Rubble

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Key ring
  Silver stake
  Vial of glacier melt
You have 136 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 388 â€” stake vs werewolf (NOT saved)
```
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf lunges. You get clear — barely.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
An ivory torch is set in an iron bracket on the wall. There's no flame at its head, but the air around it shimmers with heat.
Claws rake the air where you were standing a moment ago.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 389 â€” werewolf: attack werewolf with silver stake (NOT saved)
```
> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.
Something in the weave absorbed it. You felt the impact — and then didn't.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 389 â€” werewolf: kill werewolf with stake (NOT saved)
```

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf lunges. You get clear — barely.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 389 â€” werewolf: use stake on werewolf (NOT saved)
```
> Nothing happens.
The werewolf's claws find you.
The runes along the collar catch the light briefly. You are less hurt than you expected to be.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 390 â€” werewolf: cast unbind undead (NOT saved)
```
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> Nothing here answers the spell.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 390 â€” werewolf: take torch (NOT saved)
```

> You take the ivory torch.
The werewolf's claws find you.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 390 â€” werewolf: light torch (NOT saved)
```
> It doesn't need lighting. The heat is already there.
The werewolf's claws find you.
For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 391 â€” werewolf: torch / repeated stake (NOT saved)
```
> You take the ivory torch.
The werewolf lunges. You get clear — barely.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
Claws rake the air where you were standing a moment ago.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
It circles, feints, and comes in fast. You're not where it expected.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.

> You have 7 of 9 hearts.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 391 â€” werewolf: torch / repeated stake (NOT saved)
```
> You take the ivory torch.
The werewolf's claws find you.
For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf lunges. You get clear — barely.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.

> You have 6 of 9 hearts.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 392 â€” werewolf: no blade / take torch and flee (NOT saved)
```
> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf lunges. You get clear — barely.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.
Something in the weave absorbed it. You felt the impact — and then didn't.

> Quit now? (type "no" to save first) [yes/no] 
-----
The werewolf lunges. You get clear — barely.

> The Narrow Pass

> The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 393 â€” grabbing the ivory torch
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `east` `east` `east` `take torch` `west` `examine torch` `diagnose` `save` `quit` `yes`
```
> Restored.
Pile of Rubble
The ceiling is a jagged wound — stone and packed earth hanging at the edge where the floor above used to be. Below that: the rubble that was the floor, now a rough-graded pile you're standing on. The air smells of disturbed earth and something older underneath it. Passages lead north, east, and south.

> Antechamber

> The Lower Crossing

> The Narrow Pass

> The Still Den
A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. Something lies curled at the far end of the oval, grey and motionless. That changes the moment you enter.
An ivory torch is set in an iron bracket on the wall. There's no flame at its head, but the air around it shimmers with heat.
Something catches your eye, tucked out of sight: 2 Zenni. You pocket them.
The grey shape unfolds from the floor: a werewolf, taller than a man, long in the arm, its fur gone patchy over skin that hasn't been alive in years. It turns its head toward you and starts forward.

> You take the ivory torch.
The werewolf's claws find you.
For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.

> The Narrow Pass

> A torch with a shaft of carved ivory, yellowed with age. Its head has never been lit — it doesn't need to be. Heat pours off it, steady and impossible, enough to make your hand ache if you hold it close.

> You have 8 of 9 hearts.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 394 â€” pool: pour vial into pool (NOT saved)
```
> You unstopper the vial and tip it over the pool. The glacier melt hits the surface and the cold spreads out from it in a white rush, wall to wall, faster than water should freeze. The pool goes still. Then it goes solid.

> The Flooded Passage
The pool fills the room wall to wall, frozen solid. Water still seeps down the walls and stops where it meets the ice. The passage north is on the other side, and nothing stands between you and it now.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 394 â€” pool: use vial on pool (NOT saved)
```
> Nothing happens.

> The Flooded Passage
Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 394 â€” pool: drop vial in pool (NOT saved)
```
> That won't fit in the pool.

> The Flooded Passage
Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 395 â€” freezing the pool and crossing
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `pour vial into pool` `north` `look` `save` `quit` `yes`
```
> Restored.
The Narrow Pass
A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.

> The Lower Crossing

> Tool Alcove

> The Flooded Passage

> You unstopper the vial and tip it over the pool. The glacier melt hits the surface and the cold spreads out from it in a white rush, wall to wall, faster than water should freeze. The pool goes still. Then it goes solid.

> The Fountain Room
Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.

> The Fountain Room
Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 396 â€” melting the ice
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine ice` `melt ice with torch` `look` `save` `quit` `yes`
```
> Restored.
The Fountain Room
Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.

> Frosted thick. Inside, a soldier stands composed, eyes open, waiting.

> The ivory torch throws heat that seems wrong for its size. Where the flame meets the ice, the frost retreats — a wet gleam spreading outward from the torch's reach.
A single deep crack sounds from somewhere inside the block — not shattering, just shifting.
A small clear window opens in the surface. Through it, the figure is closer than expected. Still composed. Still waiting.

> The Fountain Room
Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 397 â€” melting the ice, cont.
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `melt ice with torch` `melt ice with torch` `look` `save` `quit` `yes`
```
> Restored.
The Fountain Room
Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.

> The crack deepens — then several more, fast, branching outward from the window. The block doesn't collapse so much as release. The ice falls away in sheets, and the soldier steps forward out of it as if he had been about to do so anyway. He blinks. He looks at his hands. He looks at you.
He looks at the sword at his side as if surprised to find it still there. He draws it and holds it out to you without ceremony. "The Forgotten Blade," he says. "It has no business down here." Neither, apparently, does he — he moves past you and is gone before you can speak.
[The Forgotten Blade added to inventory.]

> You can't see any ice here!

> The Fountain Room
The fountain to your left is still frozen mid-pour. Where the block of ice stood, there's only a spreading wet patch on the floor and a few sheets of ice melting at its edges.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 398 â€” Forgotten Blade vs werewolf (NOT saved)
```

> A ceremonial sword, long and narrow, the blade unmarked by any use. The hilt is wrapped in faded cloth that might once have been a colour.

> The Flooded Passage

> Tool Alcove

> The Lower Crossing

> The Narrow Pass

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.
Something in the weave absorbed it. You felt the impact — and then didn't.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
The werewolf lunges. You get clear — barely.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 399 â€” Fountain Room north (NOT saved)
```

> You can't go that way.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 399 â€” Fountain Room east (NOT saved)
```

> You can't go that way.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 399 â€” Fountain Room west (NOT saved)
```

> You can't go that way.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 400 â€” south of the Antechamber (NOT saved)
```

> Tool Alcove

> The Lower Crossing

> Antechamber

> You step through and the grinding stops. For one long breath nothing moves. Then all of them move — from the walls, from the floor, from the dark at the back where there were more than you thought. Bony hands find your arms, your coat, your throat. You go down under the weight of them and do not get up.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 401 â€” Antechamber: cast fireball then south (NOT saved)
```
> Nothing here answers the spell.

> You step through and the grinding stops. For one long breath nothing moves. Then all of them move — from the walls, from the floor, from the dark at the back where there were more than you thought. Bony hands find your arms, your coat, your throat. You go down under the weight of them and do not get up.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 401 â€” Antechamber: cast unbind undead then south (NOT saved)
```
> Nothing here answers the spell.

> You step through and the grinding stops. For one long breath nothing moves. Then all of them move — from the walls, from the floor, from the dark at the back where there were more than you thought. Bony hands find your arms, your coat, your throat. You go down under the weight of them and do not get up.

*** GAME OVER ***

[Press ENTER to exit] 
```

## Launch 402 â€” treasures to the Tower
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `west` `west` `up` `west` `north` `north` `north` `west` `north` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `north` `north` `up` `up` `put forgotten blade in case` `put ivory torch in case` `score` `save` `quit` `yes`
```
> Restored.
The Fountain Room
The fountain to your left is still frozen mid-pour. Where the block of ice stood, there's only a spreading wet patch on the floor and a few sheets of ice melting at its edges.

> The Flooded Passage

> Tool Alcove

> The Lower Crossing

> Antechamber

> Pile of Rubble

> Hole to Below

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't go that way.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't go that way.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't go that way.

> You can't go that way.

> You can't go that way.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.

> You can't go that way.

> You can't go that way.

> You can't see any case here!

> You can't see any case here!

> Score: 93
Level 7 (409 XP)
Zenni: 146
3 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 403 â€” lightening for the crossing north
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `inventory` `drop silver stake` `north` `look` `save` `quit` `yes`
```
> Restored.
Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Key ring
  Silver stake
  Ivory torch
  Forgotten Blade
You have 146 Zenni.

> You drop the silver stake.

> Rickety Bridge

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 404 â€” up to the Tower
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `north` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `north` `north` `up` `up` `put forgotten blade in case` `put ivory torch in case` `score` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is some silver dust here.
There is an incantation scroll here.

> Storage Area

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

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Town Hall

> Upper Hall

> The Tower

> The Forgotten Blade settles into the velvet. The case is a better place for it.

> The case is for treasures. That isn't one.

> Score: 153
Level 7 (409 XP)
Zenni: 146
4 treasures on display.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 405 â€” the Keeper's office
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `down` `down` `south` `east` `south` `look` `unlock west door with keys` `west` `look` `save` `quit` `yes`
```
> Restored.
The Tower
The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama.
The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. Behind the glass: the Chachapoyan Fertility Idol, the diamond brooch, the Pie Rat Coin and the Forgotten Blade.
The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT.
Someone has been adding to it.

> Upper Hall

> Town Hall

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Church of All

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
In the west wall, a narrow door of dark wood is shut tight, a heavy lock beneath the latch.

> The third key you try is the right one. The lock gives with a dry click, and the door swings inward on a small, plain room. You leave the keys hanging in the lock.

> Keeper's Chamber
A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a vial of clear liquid, and a note in a careful hand. Whatever the Keeper was preparing for, he prepared it here.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> Keeper's Chamber
A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a vial of clear liquid, and a note in a careful hand. Whatever the Keeper was preparing for, he prepared it here.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 406 â€” the Keeper's note and vial
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read note` `take note` `take vial` `examine vial` `examine texts` `search desk` `save` `quit` `yes`
```
> Restored.
Keeper's Chamber
A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a vial of clear liquid, and a note in a careful hand. Whatever the Keeper was preparing for, he prepared it here.

> "If you are reading this, I did not come back. The scholar of the Veil went down to the lower caves and did not come back as himself. What paces down there now is undead, and silver alone will not end it. The stake must be consecrated — pour the holy water on this desk over it. It is the last I blessed. I hid the stake where the town would keep it safe."

> You leave it where the Keeper left it.

> You take the vial of holy water.

> A small glass vial of clear water, stoppered and sealed with a dab of green wax.

> You can't see any texts here!

> You can't see any desk here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 407 â€” holy water to the stake
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `north` `west` `south` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `east` `south` `south` `east` `drop ivory torch` `south` `pour holy water on stake` `examine stake` `inventory` `save` `quit` `yes`
```
> Restored.
Keeper's Chamber
A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a note in a careful hand.

> Church of All

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
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

> Storage Area

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is some silver dust here.
There is an incantation scroll here.

> Collapsed Gallery

> Rickety Bridge

> You drop the ivory torch.

> Mid-Tier Key Door
There is a silver stake here.

> You'd rather not waste it.

> A slim stake of solid silver, the point still sharp. Someone hid this deliberately.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Vial of holy water
You have 149 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 408 â€” consecrating the stake
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take stake` `pour holy water on stake` `examine stake` `save` `quit` `yes`
```
> Restored.
Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.
There is a silver stake here.

> You take the silver stake.

> You unstop the vial and pour it slowly along the stake, end to end. The silver drinks it — there's no other word for it. When the last drop is gone, the metal holds a faint, steady sheen, as if lit from somewhere you can't see.

> A slim stake of solid silver, the point still sharp. It holds a faint, steady sheen that has nothing to do with the light.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 409 â€” consecrated stake: attack werewolf with stake (NOT saved)
```

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf lunges. You get clear — barely.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
The werewolf's claws find you.
The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 409 â€” consecrated stake: use stake on werewolf (NOT saved)
```

> Nothing happens.
The werewolf's claws find you.
The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
The werewolf's claws find you.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 410 â€” consecrated stake: drop pale blade / attack werewolf (NOT saved)
```
> You drop the Pale Blade.
The werewolf lunges. You get clear — barely.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.
The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 410 â€” consecrated stake: drop pale blade / stab werewolf with stake (NOT saved)
```
> You drop the Pale Blade.
The werewolf's claws find you.

> Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.
The werewolf's claws find you.
Something in the weave absorbed it. You felt the impact — and then didn't.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 410 â€” consecrated stake: throw stake at werewolf / look (NOT saved)
```
> You'd rather keep hold of the consecrated silver stake.
The werewolf lunges. You get clear — barely.

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.
Claws rake the air where you were standing a moment ago.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 410 â€” consecrated stake: drive stake into werewolf / look (NOT saved)
```
Something slips loose from around his neck as he falls and comes to rest on the stone beside him: a tarnished amulet, a seven-pointed star on its face.
You hear music — a familiar melody. You have reached level 8!

> The Still Den
A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. Nothing paces it now. The scholar lies where the creature fell, the stake still in him.
A tarnished amulet lies beside the scholar, a seven-pointed star on its face.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 411 â€” the scholar of the Veil
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `east` `down` `east` `east` `east` `east` `drive stake into werewolf` `take amulet` `examine amulet` `examine scholar` `save` `quit` `yes`
```
> Restored.
Mid-Tier Key Door
The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.

> Key Door Landing

> Mine Passage

> Hole to Below

> Pile of Rubble

> Antechamber

> The Lower Crossing

> The Narrow Pass

> The Still Den
A wide cave, low but not cramped, the walls gouged at every height. The werewolf paces the worn oval in the floor, grey fur hanging from skin that hasn't been alive in years. It hasn't taken its eyes off you.

> You get inside its reach and drive the stake home. The sheen along the silver flares white.
The creature drops. Between one moment and the next, it is not the creature anymore. The scholar lies on the floor of the cave he came down here to find.
Something slips loose from around his neck as he falls and comes to rest on the stone beside him: a tarnished amulet, a seven-pointed star on its face.
You hear music — a familiar melody. You have reached level 8!

> You take the Werewolf's Amulet.

> A tarnished amulet bearing the seven-pointed star of The Veil of the Arcane.

> Just a man, thin and tired-looking, ink still worked into the creases of his fingers. The stake is still in him. Whatever he came down here to find, he found it.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 412 â€” up to the pipe room (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `west` `west` `west` `up` `west` `north` `north` `north` `west` `north` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `east` `look` `save` `quit` `yes`
```
> Restored.
The Still Den
A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. Nothing paces it now. The scholar lies where the creature fell, the stake still in him.

> The Narrow Pass

> The Lower Crossing

> Antechamber

> Pile of Rubble

> Hole to Below

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is an ivory torch here.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is some silver dust here.
There is an incantation scroll here.

> Storage Area

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
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 413 â€” the humming jar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine jar` `listen to jar` `open jar` `take jar` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> You can't open that.

> You can't take the ceramic jar.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 414 â€” the jar's letters
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read jar` `read letters` `examine letters` `examine crack` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Around the base, worn almost smooth: "Hold what was heard. Speak what was held." You say the words aloud. The jar hums on, unchanged.

> Around the base, worn almost smooth: "Hold what was heard. Speak what was held." You say the words aloud. The jar hums on, unchanged.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 415 â€” jar: repair jar (NOT saved)
```

> You've nothing to fill the crack with.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 415 â€” jar: put honey on crack (NOT saved)
```

> You can't put the enchanted honey on the ceramic jar.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 415 â€” jar: fix jar with honey (NOT saved)
```

> You can't fix that.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 416 â€” fetching the wax seal (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `east` `south` `take wax seal` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `east` `press seal` `examine jar` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
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

> Storage Area

> Collapsed Aqueduct
There is a dagger here.
There is a wax seal here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is some silver dust here.
There is an incantation scroll here.

> You take the wax seal.

> Storage Area

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

> You press the wax seal over the crack. The wax gives, then takes — it spreads along the line of the crack and sets, red against the blue-grey glaze. The hum steadies.
Something clinks inside the jar. Five Zenni sit in the bottom, kept there by the crack until now. You pocket them.

> A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 417 â€” the jar, step two
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take jar` `listen to jar` `read jar` `speak` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> You can't take the ceramic jar.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> Around the base, worn almost smooth: "Hold what was heard. Speak what was held." You say the words aloud. The jar hums on, unchanged.

> I don't know the word "speak".

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: sing (NOT saved)
```

> I don't know the word "sing".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: hum (NOT saved)
```

> I don't know the word "hum".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: say hello (NOT saved)
```

> I don't know the word "say".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: shout (NOT saved)
```

> Aaaarrrrgggghhhh!

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: whistle (NOT saved)
```

> I don't know the word "whistle".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 418 â€” jar: talk to jar (NOT saved)
```

> There's no response from the ceramic jar.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 419 â€” May's tip on the jar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `tip may 10` `tip may 5` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> May counts the coins once, pockets them, and leans all the way across the bar. "Rowan," she says.
"That jar in the back room of the inn — people say it used to warn about things. If it's still got something to say, I'd want to hear it before going any deeper."

> May sets the Zenni on the bar and slides it back. "Nothing in here worth selling today," she says, tapping her temple.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 420 â€” journal and silver dust
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `down` `west` `west` `south` `south` `south` `east` `south` `take journal` `take silver dust` `read journal` `save` `quit` `yes`
```
> Restored.
Bar
The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands.
She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint.
A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.

> Kitchen
Shamus works the kitchen with practiced efficiency.

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> It is pitch black. You are likely to be eaten by a grue.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> It's too dark to go any further without a light.

> Cellar
A rusted tin cashbox sits on a high shelf, above the old waterline.

> You can't go that way.

> You can't see any journal here!

> You can't see any dust here!

> You don't have a journal.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 421 â€” journal and silver dust, again
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `cast light` `west` `south` `south` `south` `east` `south` `take journal` `take silver dust` `read journal` `save` `quit` `yes`
```
> Restored.
Cellar
The cellar is still wet — the walls dark to shoulder height, a tide line of silt marking where the water stood for years. Barrels lie where the flood left them, staves sprung. The drain gurgles now and then, like it's still thinking about it. In the west wall is a low door of black oak that nobody upstairs has mentioned.
A rusted tin cashbox sits on a high shelf, above the old waterline.

> It is pitch black. You are likely to be eaten by a grue.

> The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.
The Bone Passage

> The Junction

> The Toll Bridge

> Dungeon Entrance

> Ink Corridor

> Storage Area

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a Tip Journal here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is some silver dust here.
There is an incantation scroll here.

> You take the Tip Journal.

> You pinch the silver dust out of the crack and pocket it.

> JOURNAL

The Lost Apprentice    [Board]

The Ruined Shrine      [Organic]

The Whispering Jar     [Organic]
  Tip: That jar in the back room of the inn — people say it used to warn about things. If it's still got something to say, I'd want to hear it before going any deeper.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 422 â€” dust jar (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `east` `dust jar` `listen to jar` `look` `save` `quit` `yes`
```
> Restored.
Collapsed Aqueduct
A stone channel runs through the room at waist height, east to west — an aqueduct, old work and good work, with a mended section in the middle where the mortar is still pale. Water moves through it quietly, on its way to somewhere it's needed.
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> Storage Area

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

> You sprinkle the silver dust over the jar. It clings to the glaze and settles into the etched letters around the base, and for a moment the whole jar glints.

> A low, steady hum. Up close, it almost sounds like a voice holding a single note.

> Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 423 â€” reading the dusted jar
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `read jar` `examine jar` `listen to jar` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A cracked ceramic jar sits on the side table, humming faintly to itself.

> You read the words around the base aloud: "Hold what was heard. Speak what was held." The hum rises, wavers, and stops. In the silence, a voice no louder than breath: "The ceiling of the thermal vent holds a secret." Then nothing.

> A ceramic jar, glazed blue-grey, its crack sealed with red wax. A fine silver shimmer clings to the letters around its base. It doesn't hum any more.

> Nothing. The jar is quiet now.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 424 â€” down to the Thermal Vent
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `west` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `east` `south` `east` `south` `south` `east` `south` `south` `east` `down` `north` `north` `look` `examine ceiling` `look up` `search` `save` `quit` `yes`
```
> Restored.
Pipe Room
The pipe room is quieter than the rest of the tavern, which appears to be the point.
A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be.
A mended ceramic jar sits on the side table, quiet.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
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

> Storage Area

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> You can't go that way.

> Collapsed Gallery

> You can't go that way.

> Rickety Bridge
There is an ivory torch here.

> Mid-Tier Key Door

> Key Door Landing

> You can't go that way.

> You can't go that way.

> Mid-Tier Key Door

> Rickety Bridge
There is an ivory torch here.

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is an ivory torch here.

> You can't see any ceiling here!

> Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is an ivory torch here.

> You search carefully but find nothing unusual.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 425 â€” to the Thermal Vent
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `south` `east` `down` `north` `north` `look` `examine ceiling` `look up` `search` `save` `quit` `yes`
```
> Restored.
Rickety Bridge
A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.
There is an ivory torch here.

> Mid-Tier Key Door

> Key Door Landing

> Mine Passage

> Hole to Below

> Pile of Rubble

> Lower Crypt

> Thermal Vent Room

> Thermal Vent Room
A dead end, and a warm one. Heat rises from fissures in the floor, faint but steady, and the air smells of hot stone. The only way out is back south.

> Above you, the rock bulges into a low overhang. Pressed into its underside is a seam of reddish clay, warm and still soft.

> Above you, the rock bulges into a low overhang. Pressed into its underside is a seam of reddish clay, warm and still soft.

> You search carefully but find nothing unusual.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 426 â€” the clay
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take clay` `examine clay` `inventory` `save` `quit` `yes`
```
> Restored.
Thermal Vent Room
A dead end, and a warm one. Heat rises from fissures in the floor, faint but steady, and the air smells of hot stone. The only way out is back south.
A seam of reddish clay is pressed into the overhang above you.

> You take the fire clay.

> A lump of reddish fire clay, dense and faintly warm. It takes the print of your fingers.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Werewolf's Amulet
  Tip Journal
  Fire clay
You have 154 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 427 â€” mending the shrine bowl
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `up` `west` `north` `north` `north` `west` `north` `take large piece` `take muddy piece` `take stone piece` `south` `east` `north` `assemble bowl` `look` `save` `quit` `yes`
```
> Restored.
Thermal Vent Room
A dead end, and a warm one. Heat rises from fissures in the floor, faint but steady, and the air smells of hot stone. The only way out is back south.

> Lower Crypt

> Pile of Rubble

> Hole to Below

> Mine Passage

> Key Door Landing

> Mid-Tier Key Door

> Rickety Bridge
There is an ivory torch here.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a muddy bowl piece here.
There is a town charter here.
There is a stone bowl piece here.
There is a large bowl piece here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> You take the large bowl piece.

> You take the muddy bowl piece.

> You take the stone bowl piece.

> Collapsed Gallery

> Rickety Bridge
There is an ivory torch here.

> Shrine Room

> The pieces fit, but nothing holds them together.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 428 â€” bowl: assemble bowl with clay (NOT saved)
```
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> I don't know the word "assemble".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 428 â€” bowl: repair bowl with clay (NOT saved)
```
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Which bowl do you mean, the large bowl piece, the muddy bowl piece, or the stone bowl piece?

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 428 â€” bowl: use clay (NOT saved)
```
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Nothing happens.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 428 â€” bowl: press clay (NOT saved)
```
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Pushing the fire clay has no effect.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 428 â€” bowl: put clay on bowl (NOT saved)
```
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Which bowl do you mean, the large bowl piece, the muddy bowl piece, or the stone bowl piece?

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 429 â€” bowl: repair bowl (NOT saved)
```

> The pieces fit, but nothing holds them together.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 429 â€” bowl: fix bowl (NOT saved)
```

> The pieces fit, but nothing holds them together.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 429 â€” bowl: mend bowl (NOT saved)
```

> I don't know the word "mend".

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 429 â€” bowl: put clay on large piece (NOT saved)
```

> You can't put the fire clay on the large bowl piece.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 430 â€” bowl to the forge
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `north` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `north` `east` `east` `south` `down` `repair bowl` `give clay to pyronicus` `talk to pyronicus` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Rickety Bridge
There is an ivory torch here.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a town charter here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> Storage Area

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

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> The Volcano

> Pyronicus's Forge
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> The pieces fit, but nothing holds them together.

> Pyronicus doesn't take the fire clay.

> He goes back to what he was doing. The conversation, apparently, is over.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 431 â€” clay at the fountain (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `up` `north` `west` `west` `mix clay with water` `examine clay` `save` `quit` `yes`
```
> Restored.
Pyronicus's Forge
The room is large enough that the walls at the far end are suggestion rather than certainty.
Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark.
The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out.
The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right.
Pyronicus built this room first. The volcano came after.
Pyronicus works at the forge, unhurried, as though he has been expecting company and sees no reason to stop for it.

> The Volcano

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You work the clay in your hands under the fountain's spill until it softens, then keeps softening, into something smooth and tacky that holds whatever it touches. Clay adhesive — enough for one careful job.

> A palmful of soft red clay adhesive, tacky to the touch. It won't stay workable forever, but it doesn't seem in a hurry.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 432 â€” repairing the bowl with adhesive (NOT saved)
```
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
The statue stands to one side, its base pried open and empty. Whatever was inside is gone.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You lay the three pieces out and work the adhesive into every edge, pressing them together one at a time. The seams hold. The etched line runs unbroken from one piece to the next, all the way around. It's a bowl again — not a pretty one, but whole.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Werewolf's Amulet
  Tip Journal
  Repaired bowl
You have 154 Zenni.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 433 â€” the repaired bowl to the forest shrine
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `repair bowl` `east` `east` `east` `north` `north` `look` `put bowl on shrine` `put bowl in shrine` `save` `quit` `yes`
```
> Restored.
Roundabout Town Square
The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center.
The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right.
The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.
The statue stands to one side, its base pried open and empty. Whatever was inside is gone.
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> You lay the three pieces out and work the adhesive into every edge, pressing them together one at a time. The seams hold. The etched line runs unbroken from one piece to the next, all the way around. It's a bowl again — not a pretty one, but whole.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills.

> (Taken)
That won't fit in the pedestal.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 434 â€” forest shrine: put bowl on shrine / put zenni in bowl (NOT saved)
```
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills.

> That won't fit in the repaired bowl.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 434 â€” forest shrine: put bowl on shrine / pray (NOT saved)
```
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills.

> If you pray enough, your prayers may be answered.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 435 â€” the bowl to the underground Shrine Room
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `west` `west` `west` `south` `south` `south` `down` `west` `cast light` `west` `south` `south` `south` `east` `south` `south` `east` `north` `put bowl on plinth` `put bowl in depression` `drop bowl` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Tale and Ale — Main Room
Lynds sits at a corner table, a drink in front of him and an elbow's worth of space cleared beside it.

> Bar

> Kitchen
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

> Storage Area

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a town charter here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> Collapsed Gallery

> Rickety Bridge
There is an ivory torch here.

> Shrine Room

> You can't see any plinth here!

> You can't see any depression here!

> You drop the repaired bowl.

> Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 436 â€” picking the bowl back up
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take bowl` `put bowl on pedestal` `put bowl in bowl` `inventory` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> You take the repaired bowl.

> You can't see any pedestal here!

> That won't fit in the repaired bowl.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Werewolf's Amulet
  Tip Journal
  Repaired bowl
You have 154 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 437 â€” forest shrine: bowl + pray x4 (NOT saved)
```
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills.

> If you pray enough, your prayers may be answered.

> If you pray enough, your prayers may be answered.

> If you pray enough, your prayers may be answered.

> If you pray enough, your prayers may be answered.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 438 â€” bowl on the forest pedestal (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `west` `north` `north` `west` `north` `north` `north` `east` `east` `up` `north` `north` `north` `east` `east` `east` `north` `north` `put bowl on pedestal` `look` `save` `quit` `yes`
```
> Restored.
Shrine Room
The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.

> Rickety Bridge
There is an ivory torch here.

> Collapsed Gallery

> Collapsed Aqueduct
There is a dagger here.
There is a Pie Rat disguise here.
There is a flint and steel here.
There is a treasure map here.
There is a town charter here.
There is a pickaxe here.
There is a crowbar here.
There is a bow here.
There is a portcullis bar here.
There is a folded note here.
There is a shovel here.
There are lockpicks here.
There is an incantation scroll here.

> Storage Area

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

> Roundabout Town Square
The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, watching the town go about its business.

> Main East

> Roundabout Wasteland

> Beach Road

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Roundabout Forest

> The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 439 â€” an offering (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `put zenni on pedestal` `look` `inventory` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The repaired bowl sits on the pedestal.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The coin settles on the pedestal. For a moment, nothing. Then the bowl begins to change — ceramic going pale, then translucent, then clear. The etched design that was barely visible before catches the light now, sharp and permanent. What sits on the pedestal is no longer what you put there.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
A crystal bowl sits on the pedestal, clear as still water.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Pale Blade
  Enchanted honey
  Werewolf's Amulet
  Tip Journal
You have 161 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 440 â€” the crystal bowl
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `take crystal bowl` `examine crystal bowl` `look` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
A crystal bowl sits on the pedestal, clear as still water.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> You take the Crystal Bowl.

> A crystal bowl, clear as still water. A continuous line is etched into the rim — looping back on itself, no beginning, no end. It has the feeling of something that has been waiting a long time to be this.

> Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The pedestal is bare.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 441 â€” the church dial
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `south` `south` `west` `west` `south` `examine dial` `examine altar` `turn dial` `save` `quit` `yes`
```
> Restored.
Roundabout Forest
You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine.
The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.
A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid.
The pedestal is bare.
The symbol on the pedestal is a sprouting seed inside a circle of leaves.

> The Old Oak
The child is flying the kite in the clearing, badly and happily.

> Beach Road

> Roundabout Wasteland

> Main East

> Church of All

> You can't see any dial here!

> You can't see any altar here!

> You can't see any dial here!

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 442 â€” church: examine brass dial (NOT saved)
```

> You can't see any dial here!

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 442 â€” church: examine marks (NOT saved)
```

> You can't see any marks here!

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 442 â€” church: use amulet (NOT saved)
```

> Nothing happens.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 442 â€” church: wear amulet (NOT saved)
```

> You can't wear the Werewolf's Amulet.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 442 â€” church: drop amulet (NOT saved)
```

> You drop the Werewolf's Amulet.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.
There is a Werewolf's Amulet here.
```

## Launch 442 â€” church: drop crystal bowl (NOT saved)
```

> You drop the Crystal Bowl.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.
There is a Crystal Bowl here.
```

## Launch 442 â€” church: pray (NOT saved)
```

> You bow your head. The church receives it the way it receives everything — without asking which god it was meant for.

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 443 â€” offerings on the altar (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `put amulet on altar` `look` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> You can't see any altar here!

> Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 444 â€” altar: put amulet on stone altar (NOT saved)
```

> You can't see any altar here!

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 444 â€” altar: drop amulet|score (NOT saved)
```

> You drop the Werewolf's Amulet.

> Score: 153
Level 8 (475 XP)
Zenni: 161
4 treasures on display.
```

## Launch 444 â€” altar: put crystal bowl on altar (NOT saved)
```

> You can't see any altar here!

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 445 â€” east to the altar (ASSISTED)
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `east` `look` `save` `quit` `yes`
```
> Restored.
Church of All
The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point.
At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.
The narrow door in the west wall stands open, a ring of keys hanging from its lock.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Keepers of the Lantern.
Something catches your eye, tucked out of sight: 3 Zenni. You pocket them.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Keepers of the Lantern.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 446 â€” reading the dial
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine dial` `turn dial` `examine dial` `save` `quit` `yes`
```
> Restored.
The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Keepers of the Lantern.

> You see nothing special about the dial.

> Which way — left or right?

> You see nothing special about the dial.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 447 â€” the seven faiths
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `turn dial right` `turn dial right` `turn dial right` `turn dial right` `turn dial right` `turn dial right` `turn dial right` `save` `quit` `yes`
```
> Restored.
The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Keepers of the Lantern.

> The altar shimmers. The dial is set to The Hearth Folk.

> The altar shimmers. The dial is set to The Verdant Circle.

> The altar shimmers. The dial is set to The Veil of the Arcane.

> The altar shimmers. The dial is set to The Brotherhood of the Pale Blade.

> The altar shimmers. The dial is set to The Weavers of the Thread.

> The altar shimmers. The dial is set to The House of the Coin.

> The altar shimmers. The dial is set to The Keepers of the Lantern.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 448 â€” Veil + amulet (NOT saved)
```

> The altar shimmers. The dial is set to The Hearth Folk.

> The altar shimmers. The dial is set to The Verdant Circle.

> The altar shimmers. The dial is set to The Veil of the Arcane.

> You set the Werewolf's Amulet on the altar. It rests on the bare stone. Nothing happens — yet.
The Werewolf's Amulet begins to glow — a deep red, pulsing faintly at the void in the star's center.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Veil of the Arcane.
The Werewolf's Amulet lies on the altar, glowing red.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 449 â€” three faiths + ring (NOT saved)
```
> You set the Werewolf's Amulet on the altar. It rests on the bare stone. Nothing happens — yet.
The Werewolf's Amulet begins to glow — a deep red, pulsing faintly at the void in the star's center.

> The altar shimmers. The dial is set to The Verdant Circle.

> You set the Crystal Bowl on the altar. It rests on the bare stone. Nothing happens — yet.
The Crystal Bowl begins to glow — green, soft and even, as if light were pooling in it like water.

> The altar shimmers. The dial is set to The Veil of the Arcane.

> The altar shimmers. The dial is set to The Brotherhood of the Pale Blade.

> You set the Pale Blade on the altar. It rests on the bare stone. Nothing happens — yet.
The Pale Blade begins to glow — a clean white light, steady, coming from somewhere inside the steel.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Brotherhood of the Pale Blade.
The Pale Blade lies on the altar, glowing white.
The Werewolf's Amulet lies on the altar, glowing red.
The Crystal Bowl sits on the altar, glowing green.

> The altar goes still. The three lights — green, red, white — begin to move, slowly, tracing the edge of the stone toward the ring.

The green reaches it first. The Crystal Bowl — patience, growth, the long memory of living things. It wraps the ring in something ancient and unhurried, the way roots find stone. The bowl glows brightly and disappears into light.

The red follows. The Werewolf's Amulet — arcane power, older than the names given to it. It finds the ring's hidden nature and drags it into the light where it cannot pretend to be otherwise. The amulet fades into magic.

The white arrives last. The Pale Blade — sacrifice, the calm acceptance of what must be given up. It seals what the others have found and named. A glint flashes off the blade, and it's gone.

The ring sits on the altar alone. Whatever door was open in the ring is closed. For now.

The ring is bound.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Brotherhood of the Pale Blade.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 450 â€” binding the ring (ASSISTED: altar room east, PUT ON ALTAR)
```
> Restored.
The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Keepers of the Lantern.

> The altar shimmers. The dial is set to The Hearth Folk.

> The altar shimmers. The dial is set to The Verdant Circle.

> The altar shimmers. The dial is set to The Veil of the Arcane.

> You set the Werewolf's Amulet on the altar. It rests on the bare stone. Nothing happens — yet.
The Werewolf's Amulet begins to glow — a deep red, pulsing faintly at the void in the star's center.

> The altar shimmers. The dial is set to The Verdant Circle.

> You set the Crystal Bowl on the altar. It rests on the bare stone. Nothing happens — yet.
The Crystal Bowl begins to glow — green, soft and even, as if light were pooling in it like water.

> The altar shimmers. The dial is set to The Veil of the Arcane.

> The altar shimmers. The dial is set to The Brotherhood of the Pale Blade.

> You set the Pale Blade on the altar. It rests on the bare stone. Nothing happens — yet.
The Pale Blade begins to glow — a clean white light, steady, coming from somewhere inside the steel.

> The altar goes still. The three lights — green, red, white — begin to move, slowly, tracing the edge of the stone toward the ring.

The green reaches it first. The Crystal Bowl — patience, growth, the long memory of living things. It wraps the ring in something ancient and unhurried, the way roots find stone. The bowl glows brightly and disappears into light.

The red follows. The Werewolf's Amulet — arcane power, older than the names given to it. It finds the ring's hidden nature and drags it into the light where it cannot pretend to be otherwise. The amulet fades into magic.

The white arrives last. The Pale Blade — sacrifice, the calm acceptance of what must be given up. It seals what the others have found and named. A glint flashes off the blade, and it's gone.

The ring sits on the altar alone. Whatever door was open in the ring is closed. For now.

The ring is bound.

> The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Brotherhood of the Pale Blade.

> Score: 153
Level 8 (481 XP)
Zenni: 164
4 treasures on display.

> You are carrying:
  Plain dark ring (not worn)
  Heart necklace (being worn)
  Ivanaar's Tunic (being worn)
  Enchanted honey
  Tip Journal
You have 164 Zenni.

> Saved.

> Quit now? (type "no" to save first) [yes/no] 
```

## Launch 451 â€” telling Will
(preamble: open mailbox / yes / rogue / Rowan / restore â€” omitted)
Commands: `examine ring` `west` `north` `west` `south` `open mailbox` `talk to will` `give ring to will` `score` `save` `quit` `yes`
```
> Restored.
The Altar
The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.
The dial is set to The Brotherhood of the Pale Blade.

> A plain dark ring.

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

> There's no response from the Will Passion.

> Will takes the ring from your hand. He holds it for a moment without looking at it — as though he's listening for something. Then, apparently satisfied, he sets it down on the desk.

"Good," he says.

He looks at you properly for the first time since you walked in.

"You're alive," he says. "I wasn't certain you would be. I should have told you that at the start." He pauses. "I didn't, because I needed you to go."

He picks up his pen.

"Well done, Rowan."

He means it. You can tell because he doesn't say anything else.

Score: 153 of 300
Level 8 (481 XP)
4 of 9 treasures on display.
Title: Treasure Hunter

*** THE RING IS BOUND — GO BACK TO THE GUILD HALL FOR REWARDS ***

[Press ENTER to exit] 
```
