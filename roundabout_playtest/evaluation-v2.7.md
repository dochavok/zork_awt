# Roundabout v2.7: Round-2 Evaluation (Sable the Rogue)

Build checked: `VERSION` → "Roundabout: The God-Forsaken Ring � v2.7-roundabout". New character Sable (Rogue), 127 launches, all in `transcript-v2.7.md`. Where I reloaded a backup save to test something on a branch (other levers, disarm rolls, the ring's warning ladder), the transcript labels that launch "(backup: …)" or "SANDBOX", and I restored my real save afterwards.

## Summary

**How far I got.** Level 6, score 51 (2 treasures in the case: the idol and a new gold nugget), 8 hearts. I took the main route from the ring to the Middle Tier Key and the silver dust. Along the way I freed the ghost, got the charter, cleared the Boggart, beat the Warden, did the new Flooding Room / Lost Apprentice sequence, drained the cellar and solved the Whispering Jar. I stopped after the jar and the last-heart test, as the scope allowed. I didn't go back to the lower level (Spirit Room) because it needs the shovel from the Pie Rat ship.

**Three biggest improvements**
1. **Exits are named almost everywhere, including underground.** Every tunnel and dungeon room I entered names its ways out. So do the places that cost me the most in round 1: the Pipe Room ("a doorway leads to a quieter room and the smell of pipe smoke"), the tower stair, the church's altar archway and graveyard door, the beach's lighthouse, the Mine Passage's east side passage, and the Charnel Walk's steps up. I never once had to probe directions blind. That was my top round-1 problem, and it's essentially solved.
2. **The signal puzzles now lead you.** The Combat Room springs its own trap and sends the Warden through the door. The cellar drain says what's wrong ("packed solid with rotted sacking and root") and what to do ("Clear that, and the water has somewhere to go"). The jar tells you its letters have lost their silver, refuses the dust until the crack is sealed ("The dust would only sift into the crack"), and accepts natural phrasings (`repair jar`, `put dust on letters`). The charter's `read` now quotes the toll clause. The redesigned Flooding Room and Lost Apprentice I solved with no prior knowledge at all. None of these needed round-1 knowledge or a hint.
3. **The ring talks to you.** On the next wearing after the first warning, it says "It remembers where it left off", which is exactly the message round 1 lacked. There are warnings at 10, 20, 30 and 40, every tick after 40, a changing removal line ("slides off easily" → "sticks at the knuckle"), and a new near-miss line late on ("It didn't want to. You're not sure you could have held out another moment."). Together they make the budget something you can watch.

**Three biggest remaining problems**
1. **Hidden gates with no pointer.** Below level 3 the volcano says "There is no way in that you can see". The staircase only appears at level 3, so the opening errand silently stalls (I lost several launches here; in round 1 I happened to be level 3). The councilman gives the Middle Tier Key only after you've seen the locked iron door, and until then he repeats an unrelated speech. The Thornbrew contest and Lynds are also silently level-gated.
2. **Parser and scenery gaps that remain.** `out`, `leave` and `leave church` give "Which direction?" in every building I tried. `exit` opens the *quit* prompt and swallows the next command. `x slate` fails while `examine slate` works. `read` still contradicts `examine` on the banner, the gravestone and the pocket watch. Named scenery still "can't be seen" in a dozen rooms (the crates, the volcano, the pews, the mausoleum door, the circle's stones, the Idol Room's pedestal and plate, the crypt's footprints).
3. **Unavoidable trap damage and its follow-on at level 4.** The ink tripwire, the smoke pot and the Shatter Trap all hit me with no chance to react, costing 3 hearts. The ink then silently blocked the councilman and May. There's no `wash` verb, and `x me` doesn't mention the ink. The way out (May → "Rooms are upstairs" → the door says rooms are "rented from the bartender" → `rent room`) works but goes round in a circle. Also in this area: the Ghost's Room exit seems random, and the ring doesn't help, so I spent 4 ring ticks for nothing.

**Does the ring now feel fair?** Mostly, yes. The "it remembers" line is what turns the budget from a hidden trap into a resource. The 10-tick steps let me count: by my count wearing is itself a tick, and the 20/30/40 warnings landed exactly where I predicted. The 41–49 roll is still a roll. But the game now spends every tick in that zone telling you to stop ("Take it off. Soon." … "Why would you take it off?"), so walking into it is a choice rather than an ambush. Two things still undercut planning. First, removal at 41–43 still says "Whatever it wants, it didn't get it this time", the same reassuring line that misled me in round 1. Second, the Ghost's Room ate ring ticks on exits the ring couldn't help with. Fix those and I'd call it fair.

---

## The 13 changes

### 1. Exits: Fixed (two bog rooms missed)
- **Round-1 entry:** "Underground rooms don't list their exits, and the torch is on a timer" (also "Leaving the tavern: 'out' doesn't work and the exit isn't named", "The Stacks exit isn't mentioned", "The east exit from the wasteland isn't mentioned", "The Assay Room exit isn't mentioned", "The church has a second unmentioned exit, to the Graveyard", "Northeast from the beach isn't signposted", "North from the archery range isn't signposted", "The Entrance names no exits…", "The Rickety Bridge doesn't mention its north exit", "(ASSISTED) The Pipe Room off the tavern isn't mentioned anywhere", "(ASSISTED) The Town Hall has a third floor I never found", "(ASSISTED) The Stored Room east of the Mine Passage is unmentioned", "(ASSISTED) The altar is its own room east of the nave")
- **What I did:** Played the whole route and read every room's first description. Round-1 knowledge helped me choose *where* to go, but I never needed it to know *which way*: the text gave the direction every time except the two bog rooms below.
- **The game said:** "To the east, a doorway leads to a quieter room and the smell of pipe smoke. … The street door opens north onto the square." / "At its far end, a narrower stair turns upward into the tower" / "To the east, through a low archway, a stone altar stands in a space of its own … a side door to the south lets out into the graveyard." / "Passages branch three ways: east toward the cellar, north toward the old mine workings, and south, where the floor drops away toward a ravine." / "a narrower side passage opens to the east."
- **Verdict:** A real fix. It removed most of my round-1 stuck points. Gaps: the two middle bog rooms (the log room and the grey-stone room) name no exits at all. The Upstairs Hall names only the stairs. The Volcano below level 3 says "There is no way in that you can see" (see New problems).

### 2. Changed rooms: Fixed
- **Round-1 entry:** "Litlock's 'see things differently' reveals a building in the graveyard, but brief mode hides it"
- **What I did:** Came back to rooms after their ways changed: the graveyard after Litlock, the tower after the music box, the kitchen after the cellar, the portcullis, the iron door, the apprentice's cell.
- **The game said:** Graveyard (full description on re-entry): "To the east, a low building stands where there was nothing before — and you are not sure how you missed it." Tower: "You notice a door to the north you hadn't seen before." Kitchen: "The cellar door stands open … Stone steps lead down into the cellar." Cell: "the tunnel angles steeply up to a ragged patch of grey light."
- **Verdict:** Works everywhere I checked. Small leftovers: after I opened the black oak door from the cellar side, the Bone Passage still describes it as "set into the older stone" with no sign it's open. And when I climbed out of the apprentice's tunnel, the bog room I came out in doesn't mention the tunnel.

### 3. Scenery: Partly
- **Round-1 entry:** "Fountain gets 'nothing special' despite a rich description", "Library scenery isn't examinable", "The named mirrors can't be examined", "The Combat Room door: not an object", "`read charter` says there's no writing on it", "The pocket watch's engraving: `read` says there's no writing", "Calder Finch's gravestone: good clue, inconsistent verbs"
- **What I did:** Examined the focal nouns in each room's text with one verb and one noun.
- **The game said:** Now working: fountain ("Whatever fed it came from somewhere underground"), statue ("Something with leverage could open it"), card catalogue ("The drawer marked V sits a little open"), mirrors ("It shows the room, the doorway, the faces. It doesn't show you."), Combat Room door, Flooding Room levers and sluice, forest pedestal, Shrine Room plinth (with the seed symbol), lighthouse desk/stair/chain, ticket booth, charter (`read`: "One clause has been underlined by a later hand … PUBLIC PROPERTY — free of toll"). Still "You can't see any … here!": Back Alley crates, the Archivist's maps, the volcano (inside the Volcano room), archery targets, the circle's stones and symbol, church pews, the mausoleum's iron door, the crypt's footprints/passage/alcoves, the Idol Room's pedestal and plate, the Creature Den's bones, the Cache's sacking. `read` still contradicts `examine`: banner (`x`: "Four runes are stitched along the banner…" / `read`: "There's nothing written on the banner."), gravestone (`x`: "CALDER FINCH — EXPLORER" / `read`: "There's nothing written on the gravestone."), pocket watch (`x`: "engraved, but too worn to read" / `read`: "There's nothing written on the pocket watch.").
- **Verdict:** Much better where it matters most (the mirrors, the Combat Room door, the charter). But many named nouns remain dead ends, and the three `read` contradictions above survive.

### 4. Parser: Partly
- **Round-1 entry:** "'x' isn't accepted as examine", "Leaving the tavern: 'out' doesn't work and the exit isn't named", "'enter mine' fails; 'down' works", "Haalvar's riddle: satisfying, but only a bare answer works"
- **What I did:** `x` throughout; `enter church`, `enter town hall`, `enter mine`; `out`, `leave`, `leave church`, `go out`, `exit` in the tavern, the Town Hall, the church, the mausoleum and the mirror building; `drop all` at the Rickety Bridge; possessives (`x shamus's slate`, `x child's kite`, `x beekeeper's hives`); `answer sea`.
- **The game said:** `x` works almost everywhere, but `x slate` → "You can't see any slate here!" while `examine slate` and `x the slate` work. ENTER works ("Mine Entrance…"). `out`/`leave`/`leave church`/`go out` → "Which direction?" in every building. `exit` → "Quit now? (type "no" to save first) [yes/no]", and my next command was taken as the answer. `drop all` → "You toss the burnt-out torch aside. … You drop the dagger. …" (works). Possessives parse: the error names the base noun ("You can't see any kite here!"). `answer sea` now works ("The stone glows."); `say sea` and `the sea` still don't. `unclog drain` works as well as `clear drain`. `drop burnt-out torch` → "You can't see any torch here!"
- **Verdict:** X, ENTER, DROP ALL and apostrophes work. OUT and LEAVE don't work anywhere I tried, and `exit` meaning quit is a trap for exactly the player who types it to leave a building.

### 5. Dropped items: Fixed
- **Round-1 entry:** "Dropped hand cart isn't listed in the room"
- **What I did:** Dropped the support beam in the Storage Area, left the hand cart at the graveyard plot, and did `drop all` (17 items) in the Shrine Room.
- **The game said:** "Equipment has been left here: a heavy support beam laid across the floor." / "An empty hand cart stands beside it." / "There is a dagger here. There is a wax seal here. … There is a stone bowl piece here." (every item, every visit)
- **Verdict:** Fixed. Everything I dropped was listed every time I came back.

### 6. Combat Room (*signal*): Fixed
- **Round-1 entry:** "(ASSISTED) The Combat Room trap has to be triggered on purpose, but I'd disarmed it"; also "The Combat Room door: not an object", "The Warden fight: no feedback on progress, and Unbind Undead doesn't work on it", "The Warden lets you walk past from behind"
- **What I did:** Walked in from the Idol Room, examined the Warden, the door and the plate, then `attack warden with pale blade` ×5. Round-1 knowledge did nothing here: the room did everything itself.
- **The game said:** "As you enter the room, a flagstone shifts under your foot and sinks with a heavy click. … Somewhere behind the heavy door, a bell rings … the door at the east end begins to grind open. … The Warden." / "The Warden stands between you and the open door, swaying, waiting for you to move." / plate: "One flagstone sits a finger's width lower than the rest. You found it the usual way."
- **Verdict:** Yes, a first-time player gets this with no help: the trap fires, the door opens, and the guard stands in the doorway. Still open from round 1: every hit says "You land a solid blow. The Warden staggers, and comes on anyway." until it drops, so there's still no sense of progress. Unbind Undead on an obviously undead guard says "Nothing here answers the spell." The Warden never hit back at level 5.

### 7. Flooding Room and the Lost Apprentice (*signal*): Fixed
- **Round-1 entry:** "The Flooding Room levers: stuck" and "(DEVELOPER NOTE) The Flooding Room's levers and its plate: I never got a fair chance at them"; Boggart: "The Boggart's toll"
- **What I did:** Entered from the Creature Den and examined everything. Pulled the left lever, then went back to the pre-lever save and tried middle, right, and waiting six turns. Played the Dream Corridor menus by trial and error, then explored the Cell, Cache and Sump. At the apprentice I tried `talk`, `cast unbind undead`, `give pickaxe`, `use pickaxe on tunnel`, `dig` and `light lantern` before `attack apprentice` ×2. Boggart: `wear ring`, `south`. All of this was new content; round-1 knowledge didn't apply.
- **The game said:** "Behind you, a stone slab drops across the doorway … The levers on the north wall suddenly look very interesting." Levers: "Nothing says which does what." Left: "something in the floor opens with a deep, sucking roar … The current takes you down through the sluice". Middle: "the sluice slams shut, and the water stops coming. It doesn't go anywhere, either." Right: "The lever snaps off in your hand … pushes the water up to your waist." Corridor: "the footprints already pressed into the mud. … Your size. Your stride." Wrong choices loop: "You wake up at the entrance." Apprentice: "He's not going to let you near it." → "his eyes are his own again … 'I was digging,' he says." → "[Apprentice's Gloves added to inventory.]" Boggart: "'Toll,' the Boggart says, holding out a hand to the exact patch of air you're standing in. 'Don't think I can't see you.'"
- **Verdict:** A first-time player would get through. The trap fires itself, every lever does something visible, and the dream loop resets harmlessly, so trial and error is fair. The apprentice's "comes at you" plus "He's not going to let you near it" makes the fight readable, and his release is a lovely scene. The board's "He may not be himself" pays off. Small notes: examining the levers gives no clue at all, so it's a pure guess (harmless here). The room says "In a few heartbeats it's above your knees", but the water then sits knee-deep "still pouring" forever. That kills the tension; either let it rise or say the pressure is holding.

### 8. Traps: Partly (retry couldn't be tested)
- **Round-1 entry:** "The rogue auto-disarming the crossbow trap felt great" / "(ASSISTED) The Combat Room trap has to be triggered on purpose, but I'd disarmed it"
- **What I did:** Walked into traps at level 4 (Shatter Trap Mirror, Ink Corridor, Supply Room) and level 5 (Portcullis Corridor). For the retry I reloaded the alcove save 3 times and walked into the portcullis corridor each time.
- **The game said:** Level 4: "Something clicks behind the frame. A bolt cracks out of the dark and catches you before you can move." / "Something snags across your chest … Ink comes down in a cold black sheet" / "a clay pot tips, falls and bursts, and the room fills with choking grey smoke." Level 5, every time: "You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it."
- **Verdict:** They now scale. At level 4 they hit, and at level 5 the portcullis was disarmed. But at level 4 there was no roll shown and no chance to react: three traps in a row just took a heart each (7 → 4), which felt like a tax rather than a challenge. The portcullis disarm succeeded 4 of 4 times, so I never saw a failure and couldn't test the retry. Its sentence is also garbled (missing "you" and "and"). The portcullis itself (lift, then `prop portcullis with portcullis bar`) is a nice use of the Supply Room bar.

### 9. Last heart: Fixed
- **Round-1 entry:** "The Swarm Tree drains hearts silently, and killed me"
- **What I did:** Walked into the Swarm Tree repeatedly, from 7 hearts down to 1.
- **The game said:** "The swarm boils out of the hollow before you can do anything useful. You retreat." (×6), then on the last one: "You're hurting badly now. One more like that and you won't get up."
- **Verdict:** The warning is clear and well placed. The individual hits are still silent, though: each approach only says "You retreat", and I had to `diagnose` to see I'd lost anything. Each approach now throws you straight back to the oak, so you can't stand there and bleed out without choosing to walk in again.

### 10. The ring (*signal*): Partly (much improved)
- **Round-1 entry:** "The ring's 'you can't take it off' game over is random", "The Spirit Room needs the ring, but the ring's earlier countdown makes it a guaranteed game over", "(ASSISTED, confirmation) The ring's budget can't be reset", "The ring's countdown on the way out was excellent"
- **What I did, in my real game (14 ticks total):**
  - Toll Bridge, to test whether the Boggart sees through it (item 7): `wear ring`, `south`, remove. **2 ticks.**
  - Mirror building to the ghost: wear, south, x mirror, south, x mirror, south, cast, take watch. **8 ticks** (total 10).
  - Trying to leave the Ghost's Room: wear, north ×3. All three were turned around anyway. **4 ticks** (total 14), wasted; see New problems.
  - I didn't reach the Spirit Room.
  - **Sandbox (throwaway branch from a backup save, then my real save restored):** I wore it on from 14 to 20, 30 and 40, then tried removal 8 times in the 41–49 zone, to read the full ladder.
  - Round-1 knowledge helped a lot: I knew from round 1 to keep wearings short and count. A new player wouldn't, but the "remembers" line now teaches it.
- **The game said:**
  - Tick 10: "The ring is warm. You hadn't noticed until just now. You're not sure when it started."
  - Next wearing: "The warmth is there before the ring is all the way on. It remembers where it left off."
  - 20: "The ring feels less like something you're wearing and more like something you're holding onto. Or something holding onto you."
  - 30: "The ring is heavier than it was. Not in weight — in presence. It knows you're wearing it."
  - 40: "The ring is harder to ignore than it was. … You should take it off. You know you should take it off."
  - Ticks 41–48, one line each: "Take it off. You should take it off." / "Take it off. Soon." / "You could take it off. You could." / "Take it — the thought slides away…" / "Off. Take it— You lose the rest of the sentence." / "You don't need to take it off. Do you?" / "Why would you take it off?"
  - Removal lines: up to about 14, "Plain dark ring removed." Around 20: "It slides off easily enough. Your finger stays warm where it was." At 30–40: "It sticks at the knuckle, just for a moment, before it lets you go." At 43: "Whatever it wants, it didn't get it this time." (4 of 4). At 47: once that same line; twice "The ring comes off. It didn't want to. You're not sure you could have held out another moment."; once "Your fingers find it. They don't do what you ask. It's fine. The ring is fine."
- **Verdict:** The warnings now let you plan. "It remembers" tells you the budget is cumulative, the steps of 10 let you count, and the removal lines tell you roughly where you are. A first-time player could now budget the ring, which round 1 made impossible. Two things short of fair: (a) at 41–43, a successful removal still prints the reassuring "Whatever it wants, it didn't get it this time", while the near-miss line at 47 is the honest one; (b) the tick-10 warning is so soft ("You hadn't noticed") that, without the next wearing's "remembers", I'd not have read it as a budget.

### 11. Kitchen cellar (*signal*): Fixed
- **Round-1 entry:** "(ASSISTED) The cellar needed `clear drain`, and I missed it"
- **What I did:** Got the key from May (she noticed the crowbar), `unlock cellar door with key`, `open cellar door`, `x drain`, `pry drain with crowbar`, then read the result and `x drain` again before trying `pull sacking` (not a noun) and `unclog drain` (worked). My round-1 knowledge told me the crowbar mattered and that clearing was the step, but the game now says both outright.
- **The game said:** May: "If you can get the cover off that drain, it's yours to clear. … Do it from the top of the stairs. Nobody goes down into that water." After prying: "Below the cover, the drain mouth is packed solid with rotted sacking and root. The water isn't going anywhere." `x drain`: "The drain mouth is choked with rotted sacking and root. Clear that, and the water has somewhere to go." Then: "When it's quiet again, the stairs go all the way down."
- **Verdict:** Yes, a first-time player would find it: the game names the problem and the verb, and it takes `unclog`. The cellar description then names "a low door of black oak that nobody upstairs has mentioned", which is a nice touch. Only nit: "sacking" is named but isn't a noun.

### 12. The Whispering Jar (*signal*): Fixed (May's tip not seen)
- **Round-1 entry:** "The humming jar: 'You've nothing to fill the crack with'" and "(ASSISTED) The Whispering Jar: `press seal`, then `dust jar`, neither of which I'd have found"
- **What I did:** Read the jar on my first visit to the tavern. Later, with the seal and dust, I deliberately avoided the round-1 commands and used natural ones: `put dust on letters` (refused), `repair jar`, then `put dust on letters` again, `read jar`. Round-1 knowledge told me which two items to bring. The game's own links are: the jar ("The silver that once filled them has worn away"), the dust ("Where it's settled in the creases of your fingers, every line stands out"), and the seal ("still soft enough to press"). I think those would get a new player there.
- **The game said:** First read: "The silver that once filled them has worn away to a few bright flecks, and without it they're only the shape of words, not the words." Dust first: "The dust would only sift into the crack." Seal: "You press the wax seal over the crack … The hum steadies." In-between state: "A ceramic jar, glazed blue-grey, its crack sealed with red wax." Then: "Silver dust has settled into the letters around its base, and they stand out clearly now." Read: "'Hold what was heard. Speak what was held.' … 'The ceiling of the thermal vent holds a secret.'" Room afterwards: "A mended ceramic jar sits on the side table, quiet."
- **Verdict:** Fixed. The silver dust is clearly linked to the letters, the ordering is taught by a refusal, and every in-between state is described correctly in both `x` and the room text. I couldn't check May's tip that names the room: from a pre-jar backup her 5 and 10 Zenni tips went to the scholar and the Keeper's office instead.

### 13. Torch (kept on purpose): not re-tested
- **Round-1 entry:** "The torch burns down even indoors in town"
- **What I did:** Nothing deliberate. It burned out on Main West on the way to the graveyard, and I used Light from then on.
- **Verdict:** Doesn't bother me now that the underground names its exits. The torch timer only hurt in round 1 because I was guessing directions in the dark.

---

## New problems

### The volcano's way in only appears at level 3, and nothing says so
- **Where:** The Volcano
- **I typed:** `south` (from the wasteland), `down`, `x volcano`, `search`, re-entering three times, `wait` ×2
- **The game said:** "There is no way in that you can see." / "You can't go that way." / "You can't see any volcano here!" After levelling to 3 elsewhere: "Something about the heat is wrong — it rises, but it doesn't burn. Where the rock meets the ground, an uneven staircase leads down into the dark."
- **What I expected or wanted:** This is the first errand, so a new player hits it at level 1–2 and is told flatly there's no way in. Either show the staircase always, or give a "come back when you're more experienced" line. The round-1 contradiction ("no way in" followed by a way in) is still there once it appears.
- **Kind:** stuck point
- **How much it mattered:** major

### `exit` opens the quit prompt and swallows the next command
- **Where:** Tale and Ale, Main Room
- **I typed:** `exit`, then `leave tavern`
- **The game said:** "Quit now? (type "no" to save first) [yes/no]" (my `leave tavern` was taken as the answer)
- **What I expected or wanted:** `exit` is a very natural way to leave a building. Make it a direction (like `out`), or at least don't let the yes/no prompt eat an ordinary command.
- **Kind:** parser
- **How much it mattered:** moderate

### `x slate` fails, though `examine slate` works
- **Where:** Kitchen
- **I typed:** `x slate`, `x shamus's slate`, `examine slate`, `x the slate`
- **The game said:** "You can't see any slate here!" (twice), then the slate's text (twice)
- **What I expected or wanted:** `x` should match `examine` everywhere; it works on every other noun I tried.
- **Kind:** parser
- **How much it mattered:** minor

### The Ghost's Room exit seems random, and the ring doesn't help
- **Where:** Ghost's Room (after freeing the ghost)
- **I typed:** `north` ×2 without the ring; `wear ring`, `north` ×3; `x mirrors`, `x doorway`, `search`; every other direction; then `north` again
- **The game said:** "You head for the door. The mirrors turn you around somewhere along the way, and you find yourself back in the middle of the room." (5 times) / `x mirrors`: "Just mirrors now, and just you in them, keeping time properly." Then on the sixth `north`: "The Shatter Trap Mirror"
- **What I expected or wanted:** In round 1 the ring walked me straight out. Here it cost 4 ring ticks for nothing. The room text ("Your reflections are wrong by a fraction") also contradicts `x mirrors` ("keeping time properly"). If leaving needs something, say what; if it's chance, it shouldn't happen once the ghost is gone.
- **Kind:** bug / unclear text
- **How much it mattered:** moderate (it burns ring budget)

### The Middle Tier Key needs you to have seen the iron door first
- **Where:** Council Chamber
- **I typed:** `talk to man` (×6) after placing the gravestone, before and after filling the Trophy Case
- **The game said:** "My grandfather built this town as much as anyone. … It's been empty for years." (even with 2 treasures in the case). After I'd visited the Mid-Tier Key Door: "I went out to the cemetery this morning … He left a key."
- **What I expected or wanted:** The gravestone is clearly the thing he cares about, so once it's back he should hand over the key, or say why not yet ("he said it opened a door below; have you seen it?"). His "empty for years" line should also notice the treasures.
- **Kind:** stuck point / stale text
- **How much it mattered:** moderate

### Covered in ink: an unannounced blocker, with no wash verb
- **Where:** Ink Corridor, then Council Chamber, the fountain, the pond, the Bar, Upstairs Hall
- **I typed:** `wash`, `wash in fountain`, `clean ink`, `bathe`, `rinse`, `swim`, `x me`, `x ink`, `tip may 5`, `open door` (upstairs), `rent room`
- **The game said:** Councilman: "takes one look at the ink and wants nothing to do with you until it's gone." / "I don't know the word "wash"." / `x me`: "You see nothing special about the Sable." / May: "Rooms are upstairs. That's all you're getting from me until you've used one." / door: "The rooms are rented from the bartender downstairs." / `rent room`: "There's a bath up there. Use it. … The ink takes three changes of water and most of the soap. It comes off."
- **What I expected or wanted:** The consequence is a good idea, and the bath is funny. But the ink wasn't mentioned again until an NPC refused me, I couldn't examine it, and `wash` isn't a verb. May's line could name the action ("Rent a room and use the bath"), and `x me` should show the ink. (`x me` also says "the Sable".)
- **Kind:** parser / unclear text
- **How much it mattered:** moderate

### Low-level traps take a heart each with no chance to react
- **Where:** Shatter Trap Mirror, Ink Corridor, Supply Room (all at level 4)
- **I typed:** just walking in
- **The game said:** "A bolt cracks out of the dark and catches you before you can move." / "Ink comes down in a cold black sheet" / "your eyes are streaming and your chest aches."
- **What I expected or wanted:** "Retuned to my level" felt like "always hits below level 5": 3 hearts gone in a few rooms with nothing I could have done. A visible disarm attempt that can fail (and be retried), or a hint before stepping in, would make these feel like play rather than a fee.
- **Kind:** design
- **How much it mattered:** moderate

### Smaller items
- **The portcullis disarm sentence is garbled:** "You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it." (minor, unclear text)
- **`drop burnt-out torch` isn't understood:** "You can't see any torch here!"; `drop all` handled it. (minor, parser)
- **The Flooding Room's water never rises:** "In a few heartbeats it's above your knees", then knee-deep "still pouring" through six `wait`s. No pressure, and the text says otherwise. (minor, unclear text)
- **The bog room above the apprentice's tunnel doesn't mention the tunnel** after you climb out of it. (minor, missing exit)
- **The mugger now ambushes you on entry and vanishes:** "Mugged — and whoever did it is still out there." I never saw him again and didn't get to fight him for the lockpicks. That may be intended, but nothing tells you where he went. (minor, unclear)

## Still open (from round 1, not on the list)
- Em-dashes print as "�" (including in the VERSION line).
- Traceback when piped input ends at a prompt: known; I didn't hit it this round.
- The Bar description still says "She works the bar…" before May is introduced.
- `read` contradicts `examine`: banner, gravestone, pocket watch (see item 3).
- The gravestone still says "You tip up one edge far enough to read it" after it stands upright in the graveyard.
- The Volcano still says "There is no way in that you can see" next to the staircase line.
- The Haalvar riddle doesn't take `say sea` or `the sea` (`answer sea` now works).
- The heart necklace gives no message about the extra heart ("You put on the heart necklace." → `diagnose` shows 7 max).
- The Warden and Lynds give no progress feedback in fights ("…comes on anyway" every hit; Lynds: "Not bad").
- Unbind Undead on the Warden: "Nothing here answers the spell."
- Swarm Tree hits are silent (only the new last-heart warning speaks).
- `x man` in the Council Chamber: "You see nothing special about the Councilman Rowan Finch." (stray "the", name leak). The councilman still shares a common player name.
- Thornbrew and Lynds are silently level-gated (Thornbrew lost at level 2, won at 3; Lynds lost at 3, won at 4; nothing hints at it).
