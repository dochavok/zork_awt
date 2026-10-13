# Roundabout playtest: handoff notes

My own working notes for resuming the playtest. (Not part of the feedback.)

## Rules of the playtest (from the developer)
- Play as an ordinary first-time player; know only what the game shows. Don't read the game's files, source, or anything online. Only read Roundabout.exe output and my own notes here.
- Set aside memories of the famous older game the opening resembles; if I notice I'm leaning on outside knowledge, flag it in the feedback instead.
- Play curiously, not as a verb sweep. Record stuck points and move on after a reasonable effort.
- Keep `transcript.md` (every launch) and `feedback.md` (entries in the set format, plus periodic "Where I think I'm going" notes) up to date as I go.
- **Mark anything found through a developer hint as assisted.**
- The developer has been steering step by step lately and says "pause" at points. Do what's asked, then stop and report.

## How to run a turn
- The game can't stay open between messages. Each turn: create the character, RESTORE, run a few commands, SAVE, QUIT.
- Start-up: `open mailbox` → `yes` → (ENTER) → `rogue` → `Rowan` → (ENTER) → `restore`. RESTORE only works after character creation.
- End: `save`, `quit`, `yes`. SAVE takes no filename (it writes `Rowan.sav` in this folder).
- Dying skips my end-of-batch SAVE, so the previous save survives. Useful for recovering.
- Helper script (lives in the session scratchpad, so it may need recreating). `turn.sh "label" cmd1 cmd2 ...` runs the preamble, the commands, then save/quit/yes. It trims the output to after "> Restored." and appends a section to transcript.md:

```bash
#!/bin/bash
cd /c/roundabout_playtest
label="$1"; shift
out=$(printf '%s\n' "open mailbox" "yes" "" "rogue" "Rowan" "" "restore" "$@" "save" "quit" "yes" | timeout 30 ./Roundabout.exe 2>&1 | sed -n '/^> Restored\./,$p')
{
  echo; echo "## $label"
  echo "(preamble: open mailbox / yes / rogue / Rowan / restore — omitted)"
  echo -n "Commands: "; printf '`%s` ' "$@"; echo '`save` `quit` `yes`'
  echo '```'; echo "$out"; echo '```'
} >> transcript.md
echo "$out"
```
- Append feedback by writing a chunk to the scratchpad with the Write tool and then `cat chunk >> feedback.md`. A big inline heredoc broke on quoting once.
- The last transcript section is "Launch 451". GAME COMPLETED (ring bound, 153/300, 4/9 treasures). Final summary written at the top of feedback.md.

## Current state (after launch 235)
- **Location:** Roundabout Forest (shrine), saved. Carrying: ring, Pale Blade, honey, Werewolf's Amulet, Tip Journal, CRYSTAL BOWL. Level 8, 161 Zenni, score 153.
- Rowan, Rogue, Level 5, about 38 Zenni. The torch burned out (gone). Cast `cast light` on entering the dark (Mausoleum); it lasts while underground.
- **Spells known:** Unbind Undead (used on the mirror ghost), Light.
- **Inventory:** Dagger, Wax seal, Lockpicks, Thin paper, Plain dark ring (not worn), Coil of rope, Large bowl piece, Muddy bowl piece, Pickaxe, Pie Rat disguise, Flat rune stone, Grey rune stone, Tip Journal, Bow, Pale Blade, Flint and steel, Treasure map, Shovel, Pie Rat Coin, Heart necklace (not worn), Town Charter. (The pocket watch went to the clerk.)
- **RING WARNING:** wearing it makes you invisible (mirrors can't see you, and the ghost becomes visible). Its "take it off" countdown seems to persist across wearings. It reached "You could take it off. You could." after about 5 moves on the second wearing. Wear it only briefly.

## Session 4 (unassisted)
- Mirror building east of the Graveyard: Entrance `south` → Rejection Mirror → `south` Shatter Trap Mirror (the trap auto-disarmed; level 5) → `south` Ghost's Room (dead end). Each mirror bounces you unless the ring is worn. `west` from the Entrance = Graveyard.
- Ghost (visible only with the ring) + `cast unbind undead` → pocket watch → `give watch to clerk` (Records) → Town Charter.
- `give charter to boggart` → bridge cleared, strongbox 10 Zenni → `south` = Dungeon Entrance.
- Route: Graveyard `south` Mausoleum `down` Crypt `down` Charnel Walk `north` Bone Passage `west` Junction `south` Toll Bridge `south` Dungeon Entrance.

## Map (directions that work)
- **Opening:** West of House (`open mailbox` = start). The tavern mailbox ↔ Will's Tower (via `open mailbox`); the tower painting ↔ the tavern main room (`examine painting`). Tower `north` = Will's Bedroom (DON'T wear Will's glasses near him: instant death).
- **Tavern:** Main Room: `south` Bar (May), `south` Kitchen (Shamus, shop slate, locked cellar); `up` Upstairs Hall (dead end); `north` Town Square.
- **Square:** `north` Town Hall (`west` Records/clerk, `east` Council, `up` Upper Hall/cabinet); `east` Main East; `west` Main West.
- **Main West:** `north` Library (`east` the Stacks/Archivist); `west` Archery Range; `southeast` Alley → `south` Back Alley.
- **Archery Range:** `west` Viking Encampment (`north` Haalvar's hut, `south` Ritual Circle, `west` Fire Pit); `north` Roundabout Pond → `north` Bog 1 → `north` Bog 2 (log) → `east` Bog 3 (grey stone) → `south` Bog 4 (gravestone) → `east` Dankhaus Common Room (Litlock).
- **Main East:** `south` Church of All → `south` Graveyard → `south` Mausoleum → `down` Crypt → `down` Charnel Walk. Graveyard now shows a new building to the `east`.
- **Main East:** `east` Wasteland → `south` Volcano → `down` Pyronicus's Forge; Wasteland `east` Beach Road → `north` Old Oak (`west` Beekeeper, `east` Swarm Tree = damage, `north` Forest/shrine → `down` Mine, now collapsed); Beach Road `south` Beach → `east` Docks → `east` Pie Rat Ship (`sail`, then `east` x3 → `land` Desert Island). Beach `northeast` Lighthouse.
- **Underground (mine side, now collapsed):** Main Shaft `south` Assay Room → `east` Hidden Entrance → `east` Forgotten Shaft → `south` Undercroft → `south` Junction (`east` Bone Passage, `south` Toll Bridge/Boggart). Bone Passage: `south` Charnel Walk, `up` from Charnel = Crypt. **Don't open the black oak door in the Bone Passage (drowning).**

## Done
- Ring retrieved and shown to Will (main quest: destroy it via 3 of 7 faiths at the church dial; the dial isn't referenceable yet).
- Viking Trust Trials (Pale Blade forged by Pyronicus; bow from Raznak). Knight beaten and trained. Mugger beaten. Kite returned. Mine blast → ship → island treasure. Lynds beaten (Heart Necklace). Litlock entertained (bog joke → "see things differently" → graveyard building revealed). Music box opened (Light scroll). Thyme given to Shamus.

## Open threads
- **Dungeon:** first wing done (aqueduct fixed, idol taken). Blocked: the Collapsed Gallery timbers (bar/crowbar give "no leverage") and the Combat Room east door (not an object).
- **Crypt far passage:** won't open in any direction, even with Light; Unbind Undead says "Nothing here answers the spell."
- (Boggart: SOLVED with the charter.)
- (Charter: obtained via the watch.)
- **Statue** (needs "leverage"; the pickaxe, blade, dagger and bow all fail). Journal links it to the Keeper of the Faiths and the Undead Warden.
- **Keeper's office** = the locked church west door (need his key).
- **Church dial** not referenceable.
- **Tavern cellar** (May keeps the key).
- **Shamus's stew:** needs "a pot that holds water."
- **Shrine bowl:** have 2 pieces; more scattered.
- **Brotherhood stones:** have 2 of 3 (flat, grey). Ivanaar wants all three.
- **Beekeeper's smoke kit** (somewhere underground) → the swarm.
- **Archivist:** rubbing of the Inscription Chamber engraving (have thin paper; need charcoal).
- **Pond bottle** (maybe the fishing rod, 8 Zenni).
- **Board quests:** the aqueduct, the lost apprentice. Calder Finch's gravestone in the bog; the missing scholar (librarian).
- **Heart Necklace:** unknown use (wear it?).

## Developer hints received so far (all marked assisted in the feedback)
`activate` for the stones; the banner by Ivanaar; `tip may #`; gunpowder from Shamus for the split support; the Assay Room south of the Main Shaft (flint); `up` from Charnel Walk; `northeast` from the beach (lighthouse); a Rogue can't read the scroll (Will translates); retry Lynds after levelling; `north` from the archery range.

## Feedback file status
- Summary at the top: session 1 plus the session 2 and 3 addenda. Not yet updated for the lighthouse, bog, Dankhaus, music box, or graveyard-reveal work (those entries exist at the bottom).
- At the end of play, refresh the top summary (three biggest problems, three best moments).

## Dungeon map (session 4, unassisted)
Dungeon Entrance `south` Ink Corridor: `west` Supply Room (took the bar, pot, smoke jar, mortar, salt), `east` Storage Area (took the hand cart) `south` Collapsed Aqueduct (FIXED: `place block` x3, `fix aqueduct`) `south` Collapsed Gallery (timbers block the east). Ink Corridor `south` Narrow Passageway `south` Idol Room (`swap idol with salt`) `south` Combat Room (east door shut) `south` Prayer Alcove (took the crowbar, glacier-melt vial).
Level 6 (REST unlocked), about 64 Zenni. New items: Portcullis bar, Small clay pot, Smoke jar, Sack of salt (left on the pedestal), Idol, Crowbar, Vial of glacier melt, Hand cart. Mortar used.
Ideas: smoke jar → swarm; clay pot + water → Shamus; cart → gravestone ("The cart's for the gravestone"); crowbar → statue; idol → ?

## Session 4, part 2
- (ASSISTED) Combat Room: `jump on plate` (the only working verb) → the Warden. Unbind Undead does nothing. Killed it with about 5 `attack warden with pale blade` in one launch (the developer said I was close after 4). Drop: Guardian's Lantern.
- Combat Room `east` Creature Den `north` Flooding Room: 3 levers (left grinds, middle nothing, right SNAPPED OFF). Stuck.
- (ASSISTED) Collapsed Gallery: `use pickaxe on timbers` x3 → overhang → `take beam` (Storage Area) → `prop overhang with beam` → `east` Rickety Bridge (south: iron door, not yet visited).
- **RING IS DANGEROUS:** the countdown persists between wearings. `remove ring` at the late stage is a RANDOM game over. Avoid wearing it again. Back up Rowan.sav before risks (copies in the scratchpad: Rowan_bridge.sav etc.).

## Session 4, part 3
- Rickety Bridge: `south` refuses unless almost everything is dropped (`drop all` works; the ring stays). Far side = "Mid-Tier Key Door": needs a key (lockpicks fail). Not worth crossing yet.
- Rickety Bridge `north` (unmentioned) = Shrine Room: took the stone bowl piece (now 3 pieces). `assemble bowl` → "The pieces fit, but nothing holds them together." Needs a binder (mortar was used up).
- Dropped items don't always show in room listings (the cart was invisible but still there).
- Backups of saves are in the scratchpad (Rowan_lantern.sav = Combat Room after the Warden).

## Session 4, part 4 (surface errands)
- Fountain running (aqueduct payoff). Statue: `use crowbar on statue` → silver stake + green-wax note ("for whoever comes after me... someone careful").
- Quest board is in the BAR. New posting: Pyronicus wants a bone flute from "the middle passages below" (bring to the forge).
- May (seeing the crowbar) gave the cellar key. Cellar unlocked, drain cover pried off from the top step (`pry drain with crowbar`); water still there. `down` = DEATH.
- Pot given to Shamus → stew on the menu.
- (ASSISTED, May tips x2: "locked door needs a key; someone in town knows" / "Rowan Finch at the Town Hall".) The gravestone moved by cart from the bog to the Graveyard plot (`put gravestone in cart`, `place gravestone`) → Council Chamber, `talk to man` (Councilman Rowan Finch) → MIDDLE TIER KEY.
- `use smoke jar` at the Swarm Tree → queen vial → beekeeper → ENCHANTED HONEY.
- About 56 Zenni after the tips.
- Next ideas: honey as the shrine bowl binder; Middle Tier Key on the iron door (drop all to cross the bridge, take only the key + light?); bone flute; lantern; silver stake.

## Session 4, part 5 (lower level)
- Middle Tier Key opened the iron door (key left in the lock). Key Door Landing `south` Mine Passage (chest: 20 Zenni with lockpicks; charcoal, silver dust) `south` Inscription Chamber (pale rune stone = the 3rd Brotherhood stone; `rub inscription with charcoal` → Rubbing) — `east` past an inert snare = Cave Creature's Lair (BONE FLUTE) — `south` Echo Alcove (`play flute` = "That's silly!") `south` Magnetic Vault (`remove lodestone`, `open chest` → DIAMOND BROOCH) `south` Deep Lock Door (dead end). Level 7.
- (ASSISTED) The cellar needs `clear drain` after the cover is off. Not done yet.
- To deliver: flute → Pyronicus (forge); rubbing → Archivist; pale stone + flat + grey → Ivanaar; brooch → ?; silver dust/stake → ?

## Session 4, part 6 (deliveries)
- Rubbing → Archivist → INCANTATION SCROLL (readable by a Rogue; "Wherever these are meant to be spoken, it isn't here"). Will won't take it.
- Pale + flat + grey stones → Ivanaar → IVANAAR'S TUNIC (worn).
- Bone flute → Pyronicus → Fireball scroll → Will → FIREBALL spell learned.
- (ASSISTED) `clear drain` → cellar drained → cashbox 10 Zenni; the cellar `west` black oak door = Bone Passage (tavern shortcut underground).
- (ASSISTED) Bridge = hidden WEIGHT limit (the silver stake is heavy). (Correction: both directions are checked.)
- (ASSISTED) Wear the heart necklace (+1 max heart).
- Open: Incantation (where to speak it? the Deep Lock Door / Crypt far passage / Shrine?), lantern, brooch, idol, silver stake + dust, shrine bowl binder, Flooding Room levers.
- (ASSISTED) Town Hall Upper Hall `up` = The Tower: TROPHY CASE (`put X in case`). Idol, brooch and Pie Rat Coin are on display (score 93). Silver dust is not a treasure.
- (ASSISTED) Mine Passage `east` (unmentioned) = Stored Room → `dig` (needs the shovel) → Hole to Below → `tie rope to timber` → `down` = Pile of Rubble.

## Lower level (session 4, part 7)
Pile of Rubble: `north` Lower Crypt (the Keeper's skeleton; took the KEY RING; green wax disc stays) `north` Thermal Vent Room (warm dead end). `east` Antechamber (bone floor: walking = GAME OVER; `clear bones` first) → `east` Lower Crossing: `north` Tool Alcove (`read incantation scroll` opens the wall) `north` Flooded Passage (bottomless pool; try the glacier-melt vial?); `east` Narrow Pass (something sleeping; unvisited); `south` Dark Room (`light lantern` → lantern hung, room lit) `south` Spirit Room (spirits block south; the ring makes them ignore you BUT the ring = GAME OVER the next turn now; probable soft-lock). Antechamber `south` = the grinding creature (unvisited).
Backups in the scratchpad: Rowan_rubble/ante/crossing/alcove/darkroom.sav.
- Spirit Room: you can't leave either way once inside (soft-lock); the developer says it's optional (one treasure missed). The ring can't be reset.
- Still Den (Narrow Pass east): the werewolf can't be hurt; `take torch` then `west` works → IVORY TORCH. `pour vial into pool` freezes the Flooded Passage → north Fountain Room → `melt ice with torch` x3 → the soldier gives the FORGOTTEN BLADE (a treasure, now in the case). Antechamber `south` = GAME OVER (skeleton horde), no solution found.
- Church west door: `unlock west door with keys` → Keeper's Chamber: note (the werewolf = the scholar of the Veil; consecrate the stake) + holy water. `take stake`, `pour holy water on stake`, then `drive stake into werewolf` (ONLY that verb works) → Werewolf's Amulet, level 8.
- Pipe Room: cracked humming jar, "Hold what was heard. Speak what was held." `repair jar` → "You've nothing to fill the crack with." (filler needed; same issue as the shrine bowl).
- (ASSISTED) Jar: `press seal` then `dust jar` (silver dust) then `read jar` → "The ceiling of the thermal vent holds a secret." The journal weighs nothing (keep it).
- Thermal Vent `examine ceiling` → fire clay. (ASSISTED) `mix clay with water` at the Town Square fountain → clay adhesive → `repair bowl` → REPAIRED BOWL. Where it goes is unclear: the forest shrine accepts `put bowl on shrine` with a joke reply; the underground Shrine Room plinth isn't a noun.
- (ASSISTED) Forest: `put bowl on pedestal`, then `put zenni on pedestal` → CRYSTAL BOWL (a treasure? or a faith item: seed-and-leaves symbol).
- After play, the developer noted misses: a far-east island by ship (sail much further east), the Flooding Room plate/levers (a treasure; the Rogue auto-disarm locks it out), and the Spirit Room (ring over-used). Added to feedback.md under 'After play'.
