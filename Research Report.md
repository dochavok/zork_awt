# Zork I (1980) — A Complete Design Reference for Building a Similar Text Adventure

## TL;DR

- **Zork I is a treasure-hunt text adventure built on a fixed 350-point economy: collect 19 treasures scattered across ~110 rooms and deposit them in a trophy case in the white house’s living room to win and earn the rank “Master Adventurer.”** Each treasure scores twice — once for first picking it up and again for casing it — and a handful of room-entry milestones round the total to exactly 350.
- The game runs in an ~83 KB Z-machine version 3 story file (release 88), recognizes about 600 vocabulary words through a sentence-level parser of ~60 verbs, and is defined by a tight resource loop: a battery lantern that dies after exactly 385 turns, a wandering thief who steals your treasures, and deadly grues in any unlit room.
- To recreate it, prioritize three pillars: (1) a parser that accepts full sentences and answers wrong input with personality; (2) a non-linear map gated by puzzle “flags” with multiple solutions; and (3) a dual-scoring treasure economy plus light/inventory management that creates constant low-grade tension.

## Key Findings

**Rooms:** ~110 room objects total (per the Z-Machine Standards Document), of which roughly 70–75 are distinctly named, meaningful locations; the remainder are repetitive maze/dead-end filler. The world divides into Above Ground (white house, forest, river, rainbow), House Interior, and the Great Underground Empire (cellar/troll, the maze, Round Room & Temple complex, Dam & Reservoir, Coal Mine, Land of the Dead).

**Items:** 60 takeable objects (per the same source). These split into **19 treasures** (plus a 20th “treasure,” the map, that appears at 350 points), a dozen-plus **tools** (lantern, sword, knives, rope, screwdriver, wrench, matchbook, garlic, shovel, bell, book, candles, air pump, skeleton key, coal), and **containers** (trophy case, brown sack, bottle, coffin, basket, buoy, egg, chalice).

**Verbs:** ~60 distinct verbs and 12 movement directions. The manual’s appendix lists ~70 verb words including unusual ones like PRAY, WAVE, INFLATE, DEFLATE, WIND, RING, READ, DIG, ECHO, and the easter-egg words XYZZY, PLUGH, ZORK, and “Hello Sailor.”

**Scoring (exact):** Maximum 350. Treasures carry a “take” value and a “case” value; the 19 take-values sum to 143 and the 19 case-values sum to 129 (272 total). Five room-entry milestones add 78 (house 10, cellar 25, past troll 5, Drafty Room 13, Treasure Room 25). 272 + 78 = 350.

**Technical scope:** ~83 KB story file (84,876 bytes for release 88), Z-machine v3, ~600-word vocabulary, ~5,500 opcodes. ~15–20 major puzzles; commonly cited as having ~28 ways to die (community figure).

## Details

### 1. Rooms / Locations

The Z-Machine Standards Document (Appendix E, drawn from Paul David Doherty’s Infocom fact sheet) states authoritatively that **“Zork I has 110 rooms and 60 takeable objects”**  — well above the stated version-3 average of “69 rooms, 39 takeable objects.”  The “110” counts every ROOM object in the game’s object tree, which includes many near-identical maze and dead-end rooms; the number of distinctly described, narratively meaningful rooms is closer to 70–75. The maze alone contributes 22 rooms “west of the Troll Room”  (15 twisty maze rooms, 4 dead ends, plus the Cyclops Room, Treasure Room, and Grating Room), explaining most of the gap.

The world is organized into clear themed areas:

- **Above Ground (White House exterior & Forest):** West of House (the start, with the mailbox), North/South/Behind House, several Forest rooms, Forest Path, Up a Tree (the bird’s nest with the jeweled egg), Clearing, the grating clearing, Canyon View, Rocky Ledge, Canyon Bottom, End of Rainbow, Aragain Falls, and Stone Barrow (the endgame exit to Zork II).
- **House Interior:** Kitchen (brown sack, bottle, window, chimney), Attic (rope, nasty knife), and the Living Room (trophy case, elvish sword, brass lantern, rug, trap door).
- **Cellar & Troll Area:** Cellar (trap-door entry), Troll Room, East-West Passage, Gallery (the painting), and Studio (chimney back up to the Kitchen).
- **The Maze:** 15 “twisty little passages, all alike,” 4 dead ends, the Cyclops Room, the Thief’s Treasure Room, and the Grating Room. A dead adventurer’s skeleton (with bag of coins, skeleton key, rusty knife, and a burned-out lantern) sits in the maze.
- **Round Room & Temple Complex:** Round Room (central hub where the thief starts), passages, Engravings Cave, Dome Room, Torch Room, North and South Temple/Altar, Egyptian Room, Entrance to Hades, and the Land of the (Living) Dead.
- **Dam & Reservoir:** Flood Control Dam #3, Dam Lobby, Maintenance Room (four colored buttons), Dam Base, Reservoir South/North, and the Atlantis Room.
- **Coal Mine:** two Mirror Rooms (teleport pair), Slide Room, Squeaky Room, Bat Room, Shaft Room (basket mechanism), Smelly Room, Gas Room, a four-room coal-mine maze, Ladder Top/Bottom, Timber Room, Drafty Room, and the Machine Room (coal → diamond).
- **Frigid River / Rainbow:** five river segments (with the red buoy holding the emerald), White Cliffs beaches, Sandy Beach (shovel), and Sandy Cave (dig for the scarab).

### 2. Items / Objects

There are **60 takeable objects**. They fall into four categories.

**The 19 treasures** (with their take/case point values and locations):

|Treasure               |Take|Case|Location                        |
|-----------------------|----|----|--------------------------------|
|Jewel-encrusted egg    |5   |5   |Bird’s nest, Up a Tree          |
|Golden clockwork canary|6   |4   |Inside the egg                  |
|Beautiful painting     |4   |6   |Gallery                         |
|Platinum bar           |10  |5   |Loud Room                       |
|Ivory torch            |14  |6   |Torch Room (also a light source)|
|Gold coffin            |10  |15  |Egyptian Room (also a container)|
|Egyptian sceptre       |4   |6   |Inside the coffin               |
|Trunk of jewels        |15  |5   |Reservoir (when drained)        |
|Crystal trident        |4   |11  |Atlantis Room                   |
|Jade figurine          |5   |5   |Bat Room                        |
|Sapphire bracelet      |5   |5   |Gas Room                        |
|Huge diamond           |10  |10  |Created from coal in the machine|
|Bag of coins           |10  |5   |The Maze                        |
|Crystal skull          |10  |10  |Land of the Living Dead         |
|Jeweled scarab         |5   |5   |Buried in Sandy Cave            |
|Large emerald          |5   |10  |Inside the buoy                 |
|Silver chalice         |10  |5   |Treasure Room                   |
|Pot of gold            |10  |10  |End of Rainbow                  |
|Brass bauble           |1   |1   |Dropped by the songbird         |

A **20th “treasure”** — an ancient map/parchment — materializes in the trophy case once you reach 350 points and opens the path to the Stone Barrow.

**Tools / utility items:** brass lantern (primary light), elvish sword (glows near danger, best vs. troll), nasty knife (best vs. thief), rusty knife (cursed), rope, screwdriver, wrench, matchbook, clove of garlic, shovel, bloody axe (troll’s), stiletto (thief’s), brass bell, black book, pair of candles, hand-held air pump, skeleton key, lump of coal, lunch/sandwich, bottle of water, pile of leaves.

**Containers:** trophy case (the goal repository), brown sack, glass bottle, gold coffin, the basket/dumbwaiter, red buoy, jeweled egg, silver chalice, and the mailbox.

**NPCs/creatures:** the Troll (killed with the sword), the Thief (a roaming pickpocket killed with the knife in his Treasure Room), the Cyclops (frightened off by “Odysseus”/“Ulysses” or fed lunch and water), a vampire bat (repelled by garlic), the ghosts of Hades (banished by a bell/candle/book ritual), and a songbird.

### 3. Actions / Verbs

The Zork I parser was a landmark: it accepted full sentences (“put the lamp and sword in the case,” “drop all except lantern,” “look under the rug”) rather than the two-word verb-noun commands of Colossal Cave Adventure. The vocabulary is about 600 words (“Early games such as ‘Zork I’ know about 600 words,” per the Z-Machine Standards Document), with roughly 60 distinct verbs (synonyms like CARRY/GET/TAKE collapse to a single verb internally).

The official manual’s verb appendix lists: ANSWER, ATTACK, BLOW, BREAK, BURN, CLIMB, CLOSE, COUNT, CROSS, CUT, DEFLATE, DIG, DRINK, DROP, EAT, ENTER, EXAMINE, EXIT, EXTINGUISH, FILL, FOLLOW, GIVE, INFLATE, JUMP, KICK, KNOCK, LIGHT, LISTEN, LOCK, LOOK, LOWER, MOVE, OPEN, POUR, PRAY, PULL, PUSH, PUT, RAISE, READ, RING, SAY, SEARCH, SHAKE, SLIDE, SMELL, STAY, STRIKE, SWIM, TAKE, TELL, THROW, TIE, TOUCH, TURN, UNLOCK, WAKE, WALK, WAVE, WEAR, WIND. The 12 movement directions are N, S, E, W, NE, NW, SE, SW, UP, DOWN, IN, OUT. System commands include SAVE, RESTORE, RESTART, QUIT, SCORE, DIAGNOSE, INVENTORY, VERBOSE/BRIEF, and WAIT.

Game-specific/unusual verbs worth noting for a recreation: PRAY (teleports from the altar), WAVE (the sceptre, to solidify the rainbow), WIND (the canary), RING (the bell, for the Hades exorcism), DIG (sand only), ECHO (an alternate Loud Room solution), and the easter-egg magic words XYZZY and PLUGH (which respond “A hollow voice says ‘Fool.’”),  plus ZORK and “Hello Sailor.”

### 4. Scoring System (exact)

**Maximum score: 350**, confirmed by the manual, every winning transcript, and the source code’s scoring routine, which sums a base/event score with the live total of trophy-case contents.

Crucially, each treasure has **two values**: a “take” (touch) value awarded the first time you pick it up, and a “case” value awarded when it sits in the trophy case. This is why the game rewards both exploration and the act of depositing.

- **Take-values sum:** 143
- **Case-values sum:** 129
- **Treasure subtotal:** 272

**Progress (room-entry) points**, awarded once each. Per the official InvisiClues “How Points are Scored”: “You get 10 points for getting into the house, 25 for getting into the Cellar, 5 for getting past the Troll, 13 for getting to the Drafty Room, and 25 for getting to the Treasure Room. These points plus all the treasure points make 350.” 

- Getting into the house: 10
- Reaching the Cellar: 25
- Getting past the Troll: 5
- Reaching the Drafty Room: 13
- Reaching the Treasure Room: 25
- **Progress subtotal: 78**

**272 + 78 = exactly 350.** Your score is not affected by the number of moves taken; per the Zork Wiki/Wikipedia entry, “It is possible to score all 350 points in 231 moves (and complete the game completely in 236 moves)”  — and an optimized run can reach 350 in as few as 228 moves by exploiting a bug.

**Rank/title thresholds** (the ranks Inform 7’s documentation cites as drawn directly from Zork I):

|Score|Rank              |
|-----|------------------|
|0    |Beginner          |
|25   |Amateur Adventurer|
|50   |Novice Adventurer |
|100  |Junior Adventurer |
|200  |Adventurer        |
|300  |Master            |
|330  |Wizard            |
|350  |Master Adventurer |

(Caution when recreating: Zork II uses a similar-looking but different table scaled to 400 points  — do not confuse the two.)

### 5. Game Structure

**The trophy case / scoring hub:** The empty trophy case in the Living Room is both the win condition and the scoring anchor. You deposit treasures there; the game recomputes the case score live from its contents. When all 19 are inside (350 points), a whisper says “Look to your treasures for the final secret,”  and a map appears, opening the Stone Barrow southwest of the house — the transition into Zork II.

**Win condition:** Place all 19 treasures in the trophy case, then read the map and enter the Stone Barrow.

**Notable puzzles and mechanics:**

- **The trap door:** Descending closes and bars it behind you, creating early tension; once you find another way out, it stays open. 
- **Egg & canary:** The jeweled egg must be opened by the Thief (give it to him or leave it where he’ll take it); after killing him you recover the opened egg with the clockwork canary inside. Winding the canary in the forest summons a songbird that drops the brass bauble — three treasures from one chain. (Failing to hand off the egg before the endgame can make the game unwinnable.)
- **Flood Control Dam #3:** Press the yellow button in the Maintenance Room to activate the panel, then turn the bolt with the wrench to drain the reservoir and reach the trunk of jewels and the Atlantis trident.
- **Loud Room:** Two solutions — drain/refill the reservoir to create a moment of silence, or simply say “ECHO.”
- **Cyclops:** Two solutions — say “Odysseus”/“Ulysses” (he flees and opens a shortcut to the Living Room), or feed him the lunch and water.
- **Hades exorcism:** Ring the bell, light the candles, and read the black book  — in the right order and quickly — to banish the spirits and reach the crystal skull.
- **Coal mine / diamond machine:** Carry nothing through the narrow Timber Room passage; lower light and tools via the basket; put coal in the machine and turn the switch with the screwdriver to make the diamond. An open flame in the Gas Room is fatal.
- **Rainbow:** Wave the sceptre at Aragain Falls or End of Rainbow to make the rainbow solid and reach the pot of gold.
- **The mazes:** Drop items as breadcrumbs to map; the thief disrupts this.

**Time limits / lantern:** There is no global timer, but the **brass lantern’s battery dies after exactly 385 turns** (release 88). As Z-machine expert Andrew Plotkin documented from a source disassembly (“The Visible Zorker,” Jan 2025): “it’s a timer function which counts down from 200. When that runs out, it displays a message from LAMP-TABLE and resets to 100. Then 70, then 15, then it’s dead. So the total lamp life is 385.”  The warnings escalate from “The lamp appears a bit dimmer” to “definitely dimmer now” to “nearly out,” then darkness. The **ivory torch is an unlimited light source** (but is an open flame, deadly in the Gas Room, and a treasure the thief may steal). In the dark, a grue will eat you. Best practice (and intended design) is to conserve the lantern and rely on the torch once found.

**Death & resurrection:** When you die you may be resurrected as a spirit or reappear in the forest with your belongings scattered (valuables underground, non-valuables above ground). Resurrection requires having previously visited the South Temple altar. The game is “as fair as baseball — three strikes and you’re out”: after a third death the game ends permanently. Death scatters your treasures, forcing a costly recovery. Community catalogues commonly cite about 28 distinct ways to die.

**The thief:** A roaming antagonist who steals treasures from rooms you’ve visited (and sometimes from your person), stockpiling them in his Treasure Room. He is hard to kill early; your combat ability scales with your score, so the intended approach is to avoid him until late, then fight him with the nasty knife to recover everything he’s taken.

### 6. Technical Scope

- **Story file size:** ~83 KB — precisely 84,876 bytes for release 88 (serial 840726), Z-machine version 3. This matches the Standards Document’s note that Zork-trilogy files are “about 85K,”  the smallest era of Infocom games.
- **Engine:** Z-machine v3, written in ZIL (Zork Implementation Language, a streamlined MDL/LISP derivative) and compiled to bytecode. The original mainframe Zork occupied over 1 MB of MDL; the Z-machine and the split into three games made it fit ~80 KB floppies.
- **Vocabulary:** ~600 words (v3 truncates dictionary words to 6 characters).
- **Code size:** ~5,500 opcodes, about a third of them branches — verbatim from the Z-Machine Standards Document: “‘Zork I’ uses only about 5500 opcodes… about a third of all opcodes are branches.”
- **Verbs:** ~60 distinct.
- **Puzzles:** roughly 15–20 major puzzles (no official count exists; some have multiple solutions, complicating any tally).
- **Ways to die:** commonly cited as ~28 (a fan-compiled figure, not official).
- **Word count of in-game text:** no authoritative figure is published; the text is ZSCII-compressed inside the ~83 KB file.

### 7. Other Design Decisions Worth Copying

- **Parser with personality.** Zork I was among the first games whose parser had a “strong personality,” kicking off interactive fiction’s tradition of metafictional humor and self-parody.  Wrong or nonsensical input gets witty, in-character replies (e.g., “A hollow voice says ‘Fool.’”) rather than a flat error. The dry, sardonic narrator tone is a defining feature.
- **Multiple solutions.** Zork I contains “possibly the first examples of alternative solutions to puzzles” (Cyclops and Loud Room each have two). Rewarding lateral thinking — and acknowledging good guesses even when they don’t work — is a hallmark to emulate.
- **Minimal opening, deep world.** The famous opening (“You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here.”)  is deliberately spare, contrasting with the rich detail discovered through exploration. No tutorial; the house teaches mechanics naturally.
- **Non-linear, flag-gated design.** Most of the map is open; progress is gated by puzzle “flags” (e.g., MAGIC-FLAG, RAINBOW-FLAG, WON-FLAG) that open conditional exits. Players solve puzzles in many orders.
- **Resource tension without a clock.** Instead of a turn limit, tension comes from the finite lantern, the roaming thief, inventory weight limits, and grue-filled darkness.
- **Score as a soft progress meter.** Designers later noted the score is almost a “distraction” — the real goal is the ritual of retrieving wealth and depositing it.  The dual take/case scoring reinforces both halves of that loop.
- **Difficulty.** Contemporary tip sheets rated Zork I “extremely difficult” for beginners and “difficult to hard” for experienced players  — challenging but fairer than its sequels.

## Recommendations

**Stage 1 — Define the economy and map skeleton first.** Decide your point ceiling (Zork uses a round 350) and adopt the **dual-value treasure model**: a “discovery” value plus a “deposit” value, with a central hub (the trophy case analog) that recomputes score from its contents. Add a handful of one-time milestone awards for reaching key areas. Target ~15–20 treasures and ~70 meaningful rooms; you do not need 110 unless you pad with a maze. *Benchmark to change course:* if playtesters can reach max score in well under ~200 moves or without solving most puzzles, your milestone/treasure balance is too generous (a polished Zork I run takes 231 moves).

**Stage 2 — Build the parser and tone.** Implement full-sentence parsing (verb + multiple nouns + prepositions, ALL/EXCEPT, “and”) with ~50–70 verbs, and invest early in **personality-rich rejection messages** and easter eggs. This is the single most-cited reason Zork endures. *Benchmark:* if more than ~10–15% of reasonable player inputs return a generic “I don’t understand,” expand synonyms and syntax before adding content.

**Stage 3 — Layer in tension systems.** Add a finite light source (Zork’s 385-turn lantern with graduated warnings) plus an unlimited-but-risky alternative, a roaming thief-like antagonist that scales with player progress, inventory weight limits, and lethal darkness. Provide **multiple solutions** to at least your two or three signature puzzles. *Benchmark:* if testers never feel resource pressure, shorten the light timer or make the antagonist more active; if they feel constant unfair death, add resurrection (Zork’s altar mechanic) and a “three strikes” cushion.

**Stage 4 — Polish for fairness.** Avoid unwinnable states where possible, or signpost them; Zork’s egg-to-thief dependency is a notorious example of a puzzle that can silently lock you out. Add a rank/title ladder tied to score thresholds for a sense of progression, and a graceful endgame trigger (Zork’s map-in-the-case → barrow). *Benchmark:* if blind playtesters routinely hit dead ends they can’t diagnose, add more in-world clues (Zork uses readable books, inscriptions, and item descriptions as hints).

## Caveats

- **Version matters.** Figures here describe release 88 (serial 840726, Z-machine v3), the most widely distributed version. Earlier releases (e.g., r2) and the later “Solid Gold” v5 edition differ in details (the dam drain timing, parser features like OOPS/UNDO, and an added hint system). Mini-Zork is heavily condensed.
- **“110 rooms / 60 objects”** comes from Doherty’s fact sheet via the Z-Machine Standards Document and reflects the object-tree counts (including maze filler); the count of *meaningful, distinctly named* rooms is lower (~70–75). Treat sub-counts of forest and maze rooms as approximate.
- **“19 vs. 20 treasures”** is a common point of confusion: there are 19 treasures you actually find and case; the 20th item (the map) appears automatically at 350 points. In-universe lore pages that say “Twenty Treasures” conflate later Zork material.
- **Unverified figures:** the “~28 ways to die” and any specific “number of puzzles” are community-compiled, not from primary sources. No authoritative in-game word count is published.
- **Lamp life:** 385 turns is confirmed by Andrew Plotkin’s source disassembly of release 88; one informal forum test reported ~450 moves, likely a different release or counting method. Use 385 for release 88.
- **Rank thresholds:** the 0/25/50/100/200/300/330/350 ladder is the table Inform 7’s manual attributes directly to Zork I; the 0-floor and the 350 “Master Adventurer” top are independently confirmed by transcripts, but if exactness is critical, verify the intermediate values against the gverbs.zil source.