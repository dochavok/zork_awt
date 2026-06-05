# Enchanted Realms: One Ring

### Game Design Document v0.2

-----

## Overview

A Zork-style text adventure RPG. The player explores a rich world, uncovers hidden characters, manages resources, and faces a central moral dilemma: a ring of invisibility that slowly corrupts its wearer. The core loop balances exploration, combat, skill progression, and the ever-present temptation of the ring.

**Planned Versions:**

- *One Ring* — This document. Centers on the corruption ring quest.
- *Two Towers* — Potential sequel, TBD.

-----

## Classes

Players choose one of three classes at the start of the game. Class affects starting skills, heart count, dice roll bonuses, and challenge roll affinities.

|Class  |Starting Hearts|Starting Skill|Challenge Roll Bonus           |
|-------|---------------|--------------|-------------------------------|
|Warrior|6              |Weapon use    |Strength checks                |
|Mage   |4              |Spell casting |Perception checks              |
|Rogue  |5              |Bow use       |Perception & trap disarm checks|

Each class can acquire the other classes’ skills through quests and trainers (see Skill Progression).

-----

## Core Mechanics

### Hearts & Health

- Players have 5 hearts by default, modified by class (see above).
- Hearts can be restored only at the inn (full heal) or by purchasing food and drink at the inn (restores 1 heart).
- The inn is the only healing location in the game.
- A **Heart Necklace** quest item can permanently add one heart. Equipped in the neck armor slot.

### Zenni (Currency)

- Zenni is the in-game currency.
- Found scattered throughout the world (some require perception checks to discover), in chests, or rewarded by Dungeon Masters.
- Spent on: inn rest (full heal), food and drink (1 heart), skill training, vendor items, and hints.

**Economy baseline:**
| Item | Cost |
|------|------|
| Food & Drink (1 heart) | 2 Zenni |
| Inn Rest (full heal) | 5 Zenni |
| Weapon training | 3 Zenni |
| Archery training | 3 Zenni |
| Spell training (Will) | 3 Zenni |
| Gunpowder | 5 Zenni |
| Fishing Rod | 8 Zenni |
| Tip Journal | 5 Zenni |

**Zenni sources:**
- **Starting Zenni:** Will Passion gives the player 10 Zenni during the opening tower scene — framed as "you'll need this."
- **Hidden room Zenni:** 18 rooms across the world contain 1–3 Zenni discoverable via perception check (average 2 Zenni = ~36 Zenni total if all found). Specific rooms are randomized per new game and saved for that playthrough. Actually Enchanted Glasses pass all perception checks — a thorough player with glasses can find most of them.
- **Buried chest (Desert Island):** 30 Zenni.
- **Additional chests:** 2–3 chests elsewhere in the world (locations TBD). Contents TBD — flag for design pass.
- **Vendor buyback:** Vendor buys back only items they sell, at half price. No buyback for treasure items.
- **Treasure case (Will's Tower):** Treasure items (ship-in-a-bottle, gold nugget, etc.) can be sold at Will's Wizard Tower. Prices TBD.
- **Quest rewards:** TBD per quest.
- **No Zenni cap** — players can hold any amount.

### The Inn

- One inn exists in the game.
- **Rest** — Full heal. Costs 5 Zenni.
- **Food & Drink** — Restores 1 heart. Costs 2 Zenni.
- The only way to fully restore health.

### XP & Leveling

- XP is earned through combat, completing quests, and discovering new locations.
- Leveling up is instant when the XP threshold is met.
- Total level cap TBD.
- Leveling improves dice rolls for both combat and challenge checks.

-----

## Dice & Roll System

All checks in the game are dice-based and hidden from the player.

- **Combat rolls** and **challenge rolls** use dice (d6, d10, d20, etc.).
- As players level up, they roll more dice and/or better dice, improving odds across all roll types.
- Players only ever see the outcome of a roll, never the numbers.
- Some rolls may occur completely invisibly, silently shaping the world without the player’s awareness.
- Items that improve rolls hint at their mechanical effect through their descriptions, preserving immersion.

### Challenge Roll Types

- Perception (finding hidden things, noticing details)
- Strength (forcing, breaking, physical feats)
- Trap detection & disarm
- Additional types TBD

### Damage Types

All damage in the game has a heart value and a damage type. Damage types have no mechanical effect currently but are tracked for future use — items may be designed that grant immunity or resistance to specific types.

| Damage Type | Notes |
|-------------|-------|
| **Smoke** | From smoke/fume sources — e.g. Trap 17 |
| **Physical** | Standard impact, blade, blunt damage |
| **Poison** | Gradual heart drain over turns |
| **Fire** | Heat and flame sources |
| **Fall** | Falling damage from drops and pits |
| **Arcane** | Magical sources — spells, runes, enchantments |
| **Lightning** | Electrical/arcane charge sources — e.g. Trap 19 |

Additional damage types TBD as traps and encounters are designed.

### Class Bonuses

- Mages have inherent perception bonuses.
- Warriors have inherent strength bonuses.
- Rogues have inherent bonuses to perception and trap-related checks.

-----

## Combat

- Combat rolls are dice-based and scale with player level.
- Warriors start proficient with melee weapons; Rogues with bows; Mages with spells.
- Cross-class combat skills can be learned (see Skill Progression).

-----

## Skill Progression

Each class starts with one combat skill and can unlock the others through training and quests. Training costs Zenni.

### Weapon Training — The Redcrosse Knight

- Full name: **The Redcrosse Knight: Knight of Faith**.
- Primarily a teacher, not an adversary — the "Fight the Knight" quest is a trial by combat to earn his respect, not a hostile encounter.
- Teaches melee weapon use to Mages and Rogues once the trial is passed.
- Located TBD.

### Archery Training

- Teaches bow use to Warriors and Mages.
- Located at an **archery range at the edge of town**.
- The range is a hazardous area — players passing through may be hit by arrows fired by the Vikings at the nearby encampment (challenge roll to avoid).
- Earning the Vikings' trust through the three encampment trials permanently disables the arrow hazard — the Vikings recognize the player and hold their fire.
- **Completing the Viking trust trials is required before archery training is available.** The trainer will not teach an untrusted outsider.
- Trainer: **Raznak**, a Viking. Found at the archery range. Three states: (1) **Trust not earned** — Raznak eyes the player with suspicion, says nothing. (2) **Trust earned, training not started** — Raznak notices the player and beckons; room description prompts `TALK TO RAZNAK` to begin. Rogues are not beckoned — they already know how to use a bow. (3) **Training complete** — Raznak acknowledges the player warmly. Details TBD.

### Spell Learning

- Mages learn spells by reading spell scrolls (scroll is consumed on learning).
- Warriors and Rogues must bring a scroll to a Dungeon Master (likely **Will Passion**) to have the spell taught to them (scroll consumed, spell learned permanently).
- Spells are learned permanently once acquired.

-----

## Items & Equipment

### Armor Slots

Equipment occupies the following slots. Armor is found through exploration and never degrades.

- **Head**
- **Chest**
- **Legs**
- **Hands**
- **Neck** *(Heart Necklace quest reward)*
- **Ring** *(The One Ring)*

### The Enchanted Glasses

- Two versions: **Enchanted Glasses** (regular) and **Actually Enchanted Glasses**.
- **Inventory description:** "wire-rimmed glasses" (regular); "slightly glowing wire-rimmed glasses" (Actually Enchanted).
- **In Will’s Bedroom:** After `DROP GLASSES`, description updates to "a pair of wire-rimmed glasses rests on the nightstand" (or "slightly glowing" if enchanted). Persists across visits.
- Enchanted Glasses provide a small bonus to perception checks.
- Actually Enchanted Glasses pass all perception checks automatically — no roll required.
- Found in **Will Passion’s Bedroom** — a hidden room inside Will’s Wizard Tower. Room description includes "where the magic happens."
- Upgraded to Actually Enchanted Glasses by **Kevry Talborn** — but only if the glasses are already equipped in the head slot when the player visits him.
- **Warning:** Wearing the glasses out of Will’s Bedroom triggers an instant fail state (Will attacks — no recovery). The player must pick them up and leave without equipping them. Equipping them inside the bedroom is permitted.
- **End-game return:** Dropping the glasses in Will’s Bedroom at end-game earns XP — double if Actually Enchanted. Rewards players who think to return them.
- Inventory item; can be picked up and dropped.
- Equips in the **head slot**.

### The One Ring *(Core Quest Item)*

- Only one exists in the game.
- **Origin:** The ring fell through the roof of Pyronicus’s home. Will Passion becomes aware of it and sends the player on a quest to retrieve it from Pyronicus. Pyronicus hands it over willingly.
- Grants **invisibility** while worn, enabling certain quests that cannot otherwise be completed.
- Equips in the **ring slot**.
- Carries a **corruption timer**: each turn the ring is worn advances the corruption counter.
- Milestone messages warn the player as corruption progresses.
- Removing the ring **pauses** the timer; putting it back on **resumes** from where it left off. The timer never resets.
- **Late-stage removal:** At the final corruption ticks, the player must pass a **challenge roll** to remove the ring. The outcome messages vary based on how close the roll was — near misses and clean successes are narrated differently, adding dread to the endgame.
- **Full corruption = game over (failure ending).**
- Design note: 2–3 quests should require or significantly benefit from invisibility, creating meaningful temptation to use the ring.

### Heart Necklace

- Quest reward item.
- Permanently adds one heart to the player’s maximum.
- Equips in the **neck slot**.

### The Forgotten Blade

- Treasure item — ceremonial sword of ancient ornate metalwork, craft lost to history. **Not a combat weapon; grants no combat bonus.**
- Given by the frozen soldier upon revival in the Quest 34 Fountain Room (lower tier dungeon).
- High value. Goes to the Trophy Case in Town Hall Tower.

### Spell Scrolls

- Found throughout the world.
- Mages: read to learn the spell. Scroll is consumed.
- Warriors/Rogues: must bring to a DM (likely Will) to learn. Scroll is consumed.

### Spell Mechanics

- All spells are learned permanently once acquired.
- **Reuse timers:** Every spell has a reuse timer — a number of turns that must pass before it can be cast again. The timer begins when the spell is cast.
- **Duration:** Some spells have a duration (number of turns the effect lasts). Duration and reuse timer are independent — the reuse timer starts when cast, not when the effect expires.
- Two light sources (any combination of torch and/or Light spell) function the same as one — no stacking bonus, just redundancy.

### Known Spells

| Spell | Effect | Duration | Reuse Timer | Source |
|-------|--------|----------|-------------|--------|
| **Light** | Creates a light source | 10 turns | 20 turns | Quest 12 — music box key in Bog-NW; scroll inside locked music box in Will's Tower |
| **Unbind Undead** | Releases a bound spirit | Instant | 20 turns | Lighthouse — scroll on Silas's desk |

-----

## Special Mechanics

### The Chuckle House (formerly Mirror Room)

- A standalone location (TBD placement in the world).
- Contains a mirror. If the player passes the mirror while **visible** (ring not worn), “yourself sees you” — the player is immediately kicked back to the room they came from.
- Passing the mirror while **invisible** (ring worn) proceeds normally.
- This is a single specific puzzle room, not a global rule.
- Design note: creates a natural incentive to use the ring, directly feeding into corruption temptation.

### The Stored Room / Hole to Below

A two-state room in the dungeon mid-tier. A spur off the Mine Passage — not on the critical path.

**Before digging — The Stored Room:**
*The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.*
A spur passage east leads to The Crevice (see below). One `DIG` (shovel required) collapses the floor permanently. The collapse also buries the passage to The Crevice — both rooms become inaccessible from this point forward.

**After digging — The Hole to Below:**
*Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.*
The collapse exposes a beam overhead. `TIE ROPE TO BEAM` (rope from the Docks) enables bidirectional travel. `DOWN`, `UP`, `CLIMB DOWN ROPE`, and `CLIMB UP ROPE` all work once rope is tied. Drops to the Pile of Rubble (lower tier entry room). No fall damage — the rope is required to descend safely.

**The Crevice:**
Dead-end spur east of the Stored Room. A narrow crack in the cave wall — a skeleton is wedged in the gap, having tried and failed to squeeze through. A gold pocket watch hangs from one outstretched finger. `TAKE WATCH` retrieves it (treasure item, sellable). Permanently inaccessible after the Stored Room floor collapses — the watch is missable.

**Will Passion audio note:**
On any `DIG` command anywhere in the game, a 1-in-20 random check triggers: *Will Passion materializes in your thoughts, uninvited. "Do you know how long it takes to dig a six-foot hole?" You suspect he does. You suspect he has timed it.* Applies equally to the Desert Island, the Stored Room, and the Quest 50 apprentice hole.

### The Dream Corridor

The Trap Corridor (mid-tier trap side, between Trap Side Entry and Lost Apprentice's Cell) is a branching decision tree — a liminal, dreamlike passage the player must navigate by instinct, sense, and nerve. The player does not know they are in a dream until they successfully pass through. On failure, the room description replays from the beginning and the same choices are presented again — identical every time. No damage, no cost. Just the loop.

**Structure:** 2 × 3 × 2 — three levels of decision yielding 12 outcomes. 6 successes, 6 failures.

---

**Inciting Event — Room Description (repeats on every failure):**

*The corridor is low and wet. Water drips somewhere behind you. Your torch throws just enough light to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.*

---

## Level 1 — Instinct vs. Caution

**A — Follow them**
**B — Go another way**

---

## Level 2A — Follow Path

*The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.*

**A1 — See:** *The footprints change. Halfway down the corridor they shift — your stride lengthens, the toe digs deeper. Whatever you were walking toward, you were walking faster by the time you reached it. You follow the change.*

**A2 — Hear:** *A sound comes from your left — a passage you didn't notice before, or didn't exist before. Water moving. Not dripping. Flowing. Like something is draining toward an opening.*

**A3 — Smell:** *It stops you mid-step. Something warm. Cooked. Completely wrong for a place like this — bread, maybe, or stew. Coming from ahead, faint but real, the kind of smell that makes your body move before your mind does.*

---

## Level 2B — Go Another Way Path

*You step off the prints. The corridor looks different from here — longer, maybe, or the walls are closer. Nothing you can point to. Just the feeling that the version of this place you're now standing in is not the one you entered.*

**B1 — Feel:** *Something pulls at you — not physical, not quite. A certainty about one direction that has no evidence behind it. The kind of knowing that lives below thought. You trust it, or you don't.*

**B2 — See:** *Your torch catches the wall of a side tunnel you hadn't noticed — or that wasn't there before. Claw marks run along the stone at shoulder height. Deep, parallel, dragged fast. Whatever made them was large. Whatever made them went that way. You follow anyway.*

**B3 — Feel:** *The ground hums. Low, slow, rhythmic. Like something heavy moving far below, or far ahead — it's impossible to tell. Your boots feel it more than you do. You follow the vibration.*

---

## Level 3 — Outcomes

### A1 — See (Follow path)
The footprints end at a wall. Not a door — a wall. But the mud at the base is disturbed, smeared, like something passed through it. The torch flickers.

**Option 1 — Press your hand against the wall** *(FAILURE)*
*Cold stone. Solid. You press harder, run your fingers along the seam where the smear meets the surface. Nothing gives. It is definitively, completely a wall. You press your forehead against it.*
*You wake up at the entrance. The footprints are there. Your size. Your stride.*

**Option 2 — Step back and look at the full wall** *(FAILURE)*
*Distance doesn't help. It's a wall. Flat, unbroken, mortared tight. Whatever the smear in the mud means, it doesn't mean a door. You stand there long enough to be certain.*
*You wake up at the entrance. The footprints are there. Your size. Your stride.*

---

### A2 — Hear (Follow path)
You turn left. The passage is narrow — barely a shoulder's width. The sound of moving water is clearer now, ahead and below. The passage slopes down. Your torch bends in a draft coming up from somewhere beneath you.

**Option 1 — Follow the slope down toward the sound** *(SUCCESS)*
*The slope levels. The passage opens. The sound of water is all around you now — a drain somewhere below the floor, pulling the flood somewhere useful. The air is damp but moving. Ahead, a doorway. You walk through it.*
*You are through.*

**Option 2 — Follow the draft — go toward the air, not the water** *(FAILURE)*
*The draft gets stronger. The passage narrows further and then opens without warning — onto nothing. A drop. You can't see the bottom. The torch goes with you.*
*You wake up at the entrance. The footprints are there. Your size. Your stride. Your heart is going very fast and you're not entirely sure why.*

---

### A3 — Smell (Follow path)
The smell gets stronger as you move. At the end of the corridor a low alcove opens to the right — just wide enough to crouch into. Inside: nothing. No food, no fire, no source. The smell is overwhelming in here. Your stomach responds before your brain does.

**Option 1 — Crouch inside and look for the source** *(FAILURE)*
*The alcove goes back further than it looked. You crouch deeper, torch first. The smell is everywhere and the source is nowhere. The ceiling gets lower. You keep looking. The torch goes out.*
*You wake up at the entrance. The footprints are there. Your size. Your stride. You are not hungry anymore.*

**Option 2 — Ignore it and keep moving forward** *(SUCCESS)*
*You keep walking. The smell fades behind you the way smells do when you stop chasing them. The corridor ends at a doorway. You don't remember the corridor having a doorway. You walk through it.*
*You are through.*

---

### B1 — Feel (Go another way path)
The certainty leads you to a section of wall that looks identical to every other section of wall. No seam, no mark, no reason. The feeling is loudest here. Your torch doesn't flicker. The wall doesn't breathe. It just is — and something in you insists this is the place.

**Option 1 — Trust it. Press forward into the wall.** *(SUCCESS)*
*You don't slow down. You don't brace. You walk into it the way you'd walk through a doorway you've used a thousand times. The wall is not there. The room beyond is. You are through it before you've decided what just happened.*
*You are through.*

**Option 2 — Trust it. Wait. See if something happens.** *(FAILURE)*
*You wait. The certainty doesn't grow or fade — it just sits there, patient, offering nothing new. The corridor is very quiet. You wait longer. The torch burns. Nothing happens. The feeling eventually becomes indistinguishable from doubt.*
*You wake up at the entrance. The footprints are there. Your size. Your stride. The certainty is gone.*

---

### B2 — See (Go another way path)
The claw marks run the length of the tunnel, shoulder height, deep and continuous. You follow them. The tunnel is long enough that the entrance is behind you and the far end is still ahead. The marks don't stop or change. They just keep going.

Then the tunnel goes silent in a way it wasn't silent before. One breath of stillness. Then something at the far end shifts. Not loud. Not close. Just present. Aware, maybe. The marks continue toward it.

**Option 1 — Keep walking.** *(SUCCESS)*
*You don't slow down. Whatever is ahead has already heard you — stopping won't help and going back won't either. You walk toward the sound. The tunnel ends at a doorway. Nothing is there. Nothing was ever there, or it's somewhere you're not anymore. You walk through it.*
*You are through.*

**Option 2 — Fall back.** *(FAILURE)*
*You take one step back. Then another. The sound doesn't repeat but the silence that follows it is worse. You turn and move fast, faster, back toward the entrance, back toward the footprints, back toward something that made sense.*
*You wake up at the entrance. The footprints are there. Your size. Your stride. The far end of the tunnel is very far away now.*

---

### B3 — Feel (Go another way path)
The vibration leads you to a section of floor where it is strongest — a rough circle of stone, slightly discolored, slightly lower than the surrounding floor. The hum comes up through your boots and into your legs. It is steady. It is patient. It has been doing this for a long time.

**Option 1 — Step onto the discolored stone** *(SUCCESS)*
*The hum rises through you the moment your full weight is on it — up through your legs, your chest, your jaw. The floor doesn't move. You do. The corridor shifts around you, or you shift through it, and then you are somewhere else. The hum is gone. The room ahead is quiet and real.*
*You are through.*

**Option 2 — Kneel and press your hand to it** *(SUCCESS)*
*The vibration is different through your palm than through your boots — more specific, like a word you almost recognize. You press harder. The circle of stone depresses slightly, just enough to feel deliberate, and something in the corridor unlocks without a sound. A doorway is there that wasn't before. You stand up and walk through it.*
*You are through.*

---

**On passing through:** The player arrives in the Lost Apprentice's Cell. No explanation is given for what the corridor was. The dream framing is never named in-game.

### The Treasure Map

- Hidden aboard the Pie Rat Ship in the hold/below deck.
- Each turn the player spends on the ship triggers a **perception check**.
- On success: the map is found and added to inventory.
- **Actually Enchanted Glasses** pass all perception checks — map is found on the first turn aboard.
- Carrying the map guarantees `DIG` success on the Desert Island buried chest on the first attempt.
- Without the map: each `DIG` on the island has a **10% chance** of finding the chest. Player can keep trying indefinitely.
- A player who sails all 69 squares to Kevry's hideout without finding the map, gets the glasses enchanted, and returns will auto-find the map on their next turn aboard the ship.

### The Pie Rat Ship Heist

A multi-step quest chain that grants access to the Pie Rat Ship — the only vessel available for sailing the Roundabout Sea.

1. **Find the disguise** — Pie Rat disguise found in the The Rat's Nest.
2. **Buy gunpowder** — Purchased from the Vendor (TBD location). Gunpowder alone does nothing without a light source.
3. **Take a torch** — Torch sconces in the mine tunnels. Taking a torch starts an immediate burnout timer of **40 turns** — it cannot be extinguished, only burns down. **Burnout = fail state.** The torch should be the last thing taken before planting the gunpowder — players who grab it early while exploring the mine will waste it. The correct order is not explicitly hinted. Alternate light sources exist but are harder to obtain (TBD).
4. **Plant the gunpowder** — `DROP GUNPOWDER` at the structural weak point in the mine (perception check to locate the spot).
5. **Light the fuse** — `LIGHT GUNPOWDER`. Description shows the fuse catches and begins burning. Narrative strongly implies the player should leave immediately.
6. **Exit the mine** — Player must reach the surface before the explosion. Failure to exit in time = death/fail state.
7. **Explosion** — Cave-in seals the main mine entrance permanently. Pie Rats abandon the ship to respond.
8. **Steal the ship** — Board and sail the Pie Rat Ship while the crew is distracted. Player may sail to Kevry's Secret Hideout (easter egg — no hints from May) or simply complete the heist without going east.
9. **Return the ship** — Pie Rats notice the ship was taken and returned. Reaction is split: angry but grudgingly impressed by the deception. One Pie Rat quietly flips the player a **Pie Rat Coin** — purpose TBD in a future quest.

**Notes:**
- The mine's hidden secondary entrance remains open after the cave-in and is the only way to reach items in the sealed section.
- May gives **no hints** about Kevry's island or the Enchanted Glasses — both are easter egg territory.
- Mining and piracy are linked — the mine is a Pie Rat smuggling front, not a legitimate operation.

-----

## The Four Dungeon Masters

Four hidden NPCs called Dungeon Masters are scattered throughout the world. All are helpful. They are discovered naturally as the player explores, and their full roles are TBD.

-----

### Will Passion

**Location:** White House mailbox *(homage to the original Zork)*

**Appearance:** *Will Passion sits with the unhurried stillness of a man who has seen centuries compressed into a single lifetime. His long dark robes of deep violet — trimmed in crimson cord that winds like a binding spell — hang loosely from broad, weathered shoulders. His hair, dark as a raven’s wing but streaked with the silver of hard-won wisdom, falls long and untamed past his shoulders. His beard is full and commanding, the kind that seems to grow with intent. Thin, almost delicate wire-rimmed spectacles rest upon his nose — an odd contrast to everything else about him, as if he borrowed them from a much more ordinary man. On his wrist sits a leather cuff, dark and worn. Around his neck, a crimson cord from which hangs... something. You can’t quite make it out.*

- **Opening scene:** The game begins West of the White House. Any command except `OPEN MAILBOX` returns: *"What does this look like? A Great Underground Empire?"* Opening the mailbox triggers Will’s appearance in the field. **Will’s opening text:** *Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another. "You opened the mailbox," he says. "I wasn’t entirely certain you would." He studies you for a moment. "I have a small errand for you. It involves a town called Roundabout, an object that has a habit of ending up where it doesn’t belong, and someone who is holding it quite innocently and will give it up without a fuss." He pauses. "The object itself is another matter."* Will then asks: *"Are you up for an adventure?"*
- **No:** *Will pauses. "No," he repeats, tasting the word. "Interesting." He waves a hand, not unkindly. "Off you go, then." And he is gone. The field is quiet. The mailbox stands closed in the morning light, as though it never opened. As though none of this happened.* GAME OVER. Player never leaves the field.
- **Yes:** *Will straightens to his full height. Something changes in the air — a pressure, a stillness, the sense of a page turning. "Then we begin," he says. The field vanishes. The tower arrives around you like a cloak settling onto broad shoulders.* Player is teleported to Will’s Wizard Tower.
- The White House is never revisited — the player is dropped into Roundabout after the tower visit and never returns to the field.
- **Tower visit sequence:**
  1. Player arrives — sees tower first impression.
  2. **Class selection:** Will attempts to identify the player’s class but cannot. *"I have read destinies in the lines of a man’s palm, in the pattern of stars, in the way smoke rises from a candle. And yet here you stand, entirely unreadable."* He sighs. *"Just tell me — Warrior, Mage, or Rogue?"* Player selects class. Will acknowledges with class-specific text. Class selection is permanent.
     - **Warrior:** *Will’s expression shifts — not quite approval, but something close. "A Warrior. Yes. I can see it now, actually." He seems mildly embarrassed to have missed it. "Good. You’ll need that in you before this is done."*
     - **Mage:** *Will tilts his head. "A Mage. Yes — I almost had it." He says this as though he’s been working on a puzzle and just found the missing piece. "Good. You’ll see things others miss. Pay attention to that instinct."*
     - **Rogue:** *Will leans back slightly. "A Rogue. Yes." He seems to find this amusing in a quiet way. "You know, I should have seen that. Something about the way you looked at the door when you came in." He shakes his head. "Pay attention to everything. You already know how. Just keep doing it."*
  3. **Name entry:** Will asks: *"And your name?"* Player types their name. Stored and used by NPCs as familiarity grows. Priority NPCs: May, Shamus, Raznak, Redcrosse Knight, Vikings. Others TBD. **Design note:** Review all NPC dialogue and flag where name use is appropriate.
  4. **Ring quest briefing:** Will delivers ring quest text (see above).
  5. **Zenni handoff:** *Almost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out. "Here," he says. "Ten Zenni. Don’t spend it all on drinks."* Player receives 10 Zenni.
  6. **Send-off:** *"When you’re ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.* Player must discover the painting to leave. Asking for help triggers sarcastic responses (see above).
  7. **Trailing warning:** As the player looks at the painting and is transported, Will speaks: *"One more thing," Will says, rising from his chair. "The ring — I should have told you, it—"* The transport cuts him off. Whatever he was going to say stays in the tower.
  8. **Transition text:** *The painting is larger than it looked. Or you are smaller. The tavern in the frame tilts toward you, and then you are simply there — the smell of woodsmoke and ale arriving before anything else does.* Player lands in the Tale and Ale Main Room. No NPC reacts to their arrival.
- **Return portal:** A painting of the Tale and Ale hangs in Will’s Wizard Tower. `LOOK AT PAINTING` teleports the player back to the Tale and Ale Main Room. The painting is slightly crooked; Will never straightens it. The painting is the only way out of the tower on first visit — Will alludes to it without spelling it out: *"When you’re ready," Will says, settling back into his chair, "Roundabout awaits." He picks up his pen. The conversation, it seems, is over.*
- **Tower exit sarcasm:** If the player asks how to get to Roundabout or how to leave the tower, Will responds with one of the following (randomly selected): (1) *Will doesn’t look up. "Guild hall," he says. Just those two words. Then silence.* (2) *Will sets down his pen. "I dispatched you on a quest involving a cursed ring and a man whose roof it fell through, and your first obstacle is... leaving the room." He picks his pen back up. "Take your time."* (3) *"The tower," Will says patiently, "does not have a front door per se. Look around. I find that helps."* (4) *Will peers at you over his spectacles. "You found a mailbox in a field and opened it. I have every confidence you’ll solve this."* (5) *Will once watched a student spend forty minutes in this room before finding the exit. "I won’t tell you how long you’ve been here," he says. "Yet."*
- **Tavern mailbox:** A mailbox sits in the Tale and Ale Main Room, completely out of place. No NPC acknowledges it. `OPEN MAILBOX` teleports the player back to Will’s Wizard Tower. Works both directions: Tavern → Tower and Tower → Tavern (via painting).
- Teaches non-mage classes how to learn spells from scrolls.
- One of the more mechanically important DMs for Warrior and Rogue players.
- **Sends the player on the One Ring quest** — **Ring quest briefing text:** *Will is quiet for a moment before he speaks. "There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem." He stands and moves to the window. "It fell through the roof of a man named Pyronicus. He’s holding it in good faith, completely unaware of what it is. He’ll give it up without a fight." He turns back. "I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."*
- **Will’s hidden room** contains the Enchanted Glasses. Wearing them out of this room triggers an instant fail state.

-----

### Litlock

**Location:** The Dankhaus, hidden in the bog behind dense brush. Perception check required to find it.

- Personality: **Jovial**.
- The bog contains four rooms. Only one has the brush-hidden path to the Dankhaus.
- Each time the player passes through the correct bog room, a perception check occurs.
- On success, the path is revealed and **permanently visible** for the rest of the playthrough.
- On failure, the player passes through without noticing and can try again.
- Access to the Dankhaus is gated by the magical wards — see ward mechanic in Open Questions.

-----

### Kevry Talborn

**Location:** A small island, **69 squares into the Open Ocean east of the Eastern Roundabout Sea** *(Easter egg)*

- Requires a boat to reach.
- Optional — not required for game completion.
- **Enchants the Enchanted Glasses** — but only if they are already equipped (head slot) when the player arrives.
- The long journey is the reward in itself for dedicated explorers.

-----

### Pyronicus

**Location:** Below the illusory volcano, east of the Roundabout Wasteland.

- Lives in a single large obsidian room built around an ancient forge — the forge’s heat and smoke power the volcanic illusion above.
- The volcano is a magical illusion Pyronicus created to discourage visitors. It is elaborate and convincing — false heat, false smoke, false rumbling. A harder-than-normal perception check is required to see through it. Once pierced, an uneven staircase descending DOWN leads to the forge room.
- Will told Pyronicus to expect the player — he is unconcerned about being found and surrenders the ring willingly.
- **Holds the One Ring** — it fell through his roof (the illusion). He is not hostile and hands it over without argument.
- **Forges the Pale Blade** — if the player brings the runed metal from the Viking Encampment, Pyronicus forges it into the Pale Blade artifact required for The Brotherhood of the Pale Blade ring ritual. Dialogue for this interaction TBD.
- Role beyond ring retrieval and forging TBD — likely quest hooks tied to the forge and volcano quests (Quests 21, 26, 35, 42, 45).

-----

## World & Locations

|Location                        |Notes                                                                        |
|--------------------------------|-----------------------------------------------------------------------------|
|White House                     |Opening area; homage to Zork. One room only — West of House. Any command except `OPEN MAILBOX` returns: *"What does this look like? A Great Underground Empire?"* Opening the mailbox triggers Will’s appearance in the field. Will delivers opening text and asks "Are you up for an adventure?" No = game over, never leaves field. Yes = teleported to Will’s Wizard Tower. Never revisited after opening sequence.|
|Town                            |Central hub; inn, archery range nearby.                                      |
|**Roundabout Wasteland**        |*The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently. The ground doesn’t grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly. The cause is a matter of some local sensitivity. The prevailing theory among residents involves adventurers, which explains why no one wants to discuss it in detail. To the east, a volcano rises against the sky — large, dark, and entirely convincing.* East of Main East, opposite side of town from the Archery Range. Connects east toward the volcano. Single room. Quest hooks TBD.|
|**Beach Road**                  |East of the Wasteland. A road that forks in two directions — south toward Roundabout Beach, and uphill winding toward Roundabout Forest. Description conveys the uphill path winding upward before the player commits to a direction. Single room.|
|Archery Range                   |*Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used. The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.* Hazardous — challenge roll each time the player passes through to avoid being hit by an errant arrow. Permanently safe once the player earns the Vikings' trust (all three encampment trials complete). Raznak found here.|
|**Viking Encampment**           |West of the Archery Range (Archery Range is east). Followers of The Brotherhood of the Pale Blade. Three trust trials must be completed in order (Riddle Stone → Ritual Circle → Fire Pit) before runed metal is awarded by Ivanaar Stormbringer. Runed metal taken to Pyronicus's forge → forged into the **Pale Blade** → consumed at The Brotherhood of the Pale Blade ring ritual at the Church of All altar. **Named NPCs:** Ivanaar Stormbringer (greeter, runed metal handoff), Haalvar (Riddle Stone, Trial 1), unnamed child (Ritual Circle, Trial 2), Aylora (Fire Pit, Trial 3).|
|— The Encampment                |Central hub. Fire pit, longhouses, Vikings going about their business. East → Archery Range. North → Haalvar's Hut (Trial 1). South → The Ritual Circle (Trial 2). West → The Fire Pit (Trial 3). **Ivanaar Stormbringer** is found here — gruff greeter, softens after each completed trial. **Banner** on the wall — `LOOK AT BANNER` reveals four elemental rune symbols in order: Earth, Air, Fire, Water (clue for Ritual Circle). **Ivanaar states:** (0 trials) *"You want something from us. They always want something. Prove yourself. Talk to Haalvar — north. If you can satisfy him, come back."* (1 trial) *"Haalvar speaks well of you. That's not nothing. The circle is south."* (2 trials) *"Two down. The fire pit is west. Don't embarrass yourself."* (3 trials — seeing Aylora dragged in) *"Ivanaar looks at Aylora, then at you, then at Aylora again. He says nothing for a long moment. '...Thornbrew?' he finally asks. You nod. He laughs — once, short, like it surprised him too. Then he straightens, and the laugh is gone, and something older takes its place. 'Will Passion sent you. He asked me to build something that would tell him whether you were worth trusting with what comes next. He didn't tell me what comes next.' He moves to the longhouse and returns holding a length of dark metal — dense, rune-carved, warm to the touch even in the open air. He holds it with both hands. 'This is Brotherhood metal. It has been kept since before this encampment. It would make a fine blade in the right hands — a blacksmith who knows what he is looking at could tell you more.' He places it in your hands. 'I hope Will is right about you.' Ivanaar returns to his fire. He does not look back."* → awards runed metal.|
|— Haalvar's Hut                 |North of The Encampment. Trial 1 — The Riddle Stone. **Haalvar** administers the trial. The hut contains a stone with runic carvings and a fluid-like appearance — solid to the touch, its surface moves like dark water. On entry, Haalvar delivers the riddle: *"I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"* Player types the answer. **Correct answer:** `SEA` — stone glows; Haalvar: *"The stone is satisfied. I am also satisfied, which happens less often. Go south — there is a circle there that will want your attention next."* Trial 1 complete. **Wrong answer:** *"Impressive. Wrong, but impressive in its wrongness."* Retryable. **Actually Enchanted Glasses:** Kevry's voice whispers the answer.|
|— The Ritual Circle             |South of The Encampment. Trial 2 — The Ritual Circle. An unnamed child administers the trial — he does not speak. On entry he points to five rune stones arranged around a carved symbol on the ground. Each stone is clearly elemental: Earth, Air, Fire, Water, and Heart (the fifth element — heart carved into the stone face). **Correct order:** Earth → Air → Fire → Water → Heart. First four from the banner in The Encampment; Heart stone is always last. **Commands:** `ACTIVATE EARTH STONE`, `ACTIVATE AIR STONE`, `ACTIVATE FIRE STONE`, `ACTIVATE WATER STONE`, `ACTIVATE HEART STONE` (also accepts `ACTIVATE LOVE STONE` and `ACTIVATE LIFE STONE`). **Wrong order:** *"The child looks disappointed in you."* Resets all five. **Correct completion:** Child points back toward the encampment. Trial 2 complete.|
|— The Fire Pit                  |West of The Encampment. Trial 3 — The Drinking Challenge. **Aylora** is the Viking champion. Best of five rounds; each round is a strength-based challenge roll. Warriors get a class bonus; Rogues and Mages roll straight. **The drink:** Thornbrew. **Player wins:** Aylora passes out. Player drags her back to the encampment — triggers Ivanaar's surprise reaction and runed metal handoff. Trial 3 complete. **Player loses:** Player passes out. Wakes up in the encampment two turns later. A nearby Viking: *"Ha! Aylora strikes again. Don't feel bad — she's been doing this since she could reach the cup."* Retryable.|
|Roundabout Pond                 |Between town and the bog. Two-state room. **Base description:** *The pond is easy to walk past without noticing. It sits low between the town path and the bog, ringed with reeds and the occasional frog. The water is dark and calm.* Each visit fires a silent perception check. On success, the player sees: "You see a bottle at the bottom of the pond." — quest discovered, May’s hints unlock. Sighting is not permanent; check fires on every visit until quest is discovered. Once discovered, check stops. Retrieving the bottle requires a fishing rod (purchased from vendor) and a successful challenge roll (`FISH`); Rogues get a bonus. The bottle is a treasure item. **May’s hints:** imply Kevry was trying to retrieve his ship from the pond — player connects ship and bottle. Kevry knows about it but was never able to fish it out.|
|**Bog of Eternal Stench**       |Four rooms arranged in a 2×2 grid. Players may move diagonally between rooms. All four rooms share the name "Bog of Eternal Stench" — internally referenced as Bog-SE, Bog-NE, Bog-SW, Bog-NW. Accessed from the Roundabout Pond to the east.|
|— Bog-SE                        |*The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.* Entry point from the Roundabout Pond. Dankhaus hidden here — dense brush conceals the path; perception check required each visit until discovered. Once discovered, path is permanently visible.|
|— Bog-NE                        |*The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don’t really want to.*|
|— Bog-SW                        |*A flat expanse of bog, grey-green and indifferent. The water is still except where it isn’t. The smell arrived before you did and will be here long after you leave.*|
|— Bog-NW                        |*The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.* Contains a hollow log — perception check required to find it. Inside: the key to Will’s music box (Quest 12).|
|The Sea                         |Three Roundabout Sea rooms + 69 Open Ocean squares to Kevry’s island. Requires boat. Desert Island is a spur off the Eastern Roundabout Sea.|
|Kevry’s Island                  |Small location. Easter egg.                                                  |
|Will’s Wizard Tower             |Accessed via mailbox portal from White House (opening sequence) or via mailbox in Tale and Ale Main Room. **First impression:** *The tower doesn’t announce itself. It simply is — books, firelight, the low hum of something you can’t quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.* Contains a painting of the Tale and Ale — `LOOK AT PAINTING` teleports player back to Tale and Ale Main Room. Painting hangs slightly crooked; Will never straightens it.|
|— Will Passion’s Bedroom        |Hidden room inside the tower. "Where the magic happens." Contains the Enchanted Glasses on the nightstand. Equipping the glasses inside the bedroom is permitted; equipping them outside triggers instant fail state. `DROP GLASSES` places them on the nightstand — description persists. Contains **dragon-nip** — a glowing sprig hidden under the nightstand, practically impossible to find (requires perfect roll at highest level, or Actually Enchanted Glasses). Will has been looking for it everywhere. Returning it to Will earns the **Golden Dragon Scale** (treasure item). Will suspects where it was found but doesn’t ask.|
|The Chuckle House               |Funhouse with multiple mirror rooms. The Rejection Mirror repels visible players; ring required to pass. Ghost tied to the Rejection Mirror room — visible only while wearing ring. See Chuckle House entry in locations table.|
|Dungeon/Cave Area               |Three-tier dungeon. Upper tier finalized (15 rooms). Middle tier finalized (15 rooms). Lower tier in progress (11 of 20 rooms confirmed — see lower tier section below). Entry to lower tier via Hole to Below (Stored Room, mid-tier key side).|
|**Volcano Area**                |East of the Roundabout Wasteland. The volcano is a convincing magical illusion — false heat, smoke, and rumbling powered by Pyronicus's forge below. A harder-than-normal perception check pierces the illusion and reveals an uneven staircase (DOWN) to Pyronicus's home. Visible from the Wasteland to the east. Several quest items found in this area (Quests 21, 26, 35, 42, 45 — TBD exact locations).|
|— The Volcano                   |The illusory volcano itself. Appears entirely real. Harder perception check required to see through it. On success: uneven staircase DOWN revealed. On failure: player sees only an active volcano with no apparent entrance.|
|— Pyronicus's Forge             |*The room is large enough that the walls at the far end are suggestion rather than certainty. Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark. The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out. The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right. Pyronicus built this room first. The volcano came after.* Single room. Pyronicus is here — measured, slightly aloof. Brings the runed metal from the Viking Encampment here — Pyronicus forges it into the Pale Blade (Brotherhood of the Pale Blade ring ritual artifact). **Ring handover:** *Pyronicus sets down his work and regards you with calm, unhurried eyes. "Will's errand," he says. "Yes." He moves to a workbench and returns with the ring, placing it in your hand with the care of someone returning something that was never theirs. "It fell through my ceiling," he says. "Rings don't do that by accident." He pauses. "Will told you what you need to know, I assume." He goes back to what he was doing. The conversation, apparently, is over.* Repeated attempts to get more information from Pyronicus after the ring is handed over receive no response. Role beyond ring retrieval TBD.|
|**The Dankhaus**                |Three-bedroom home hidden in the bog behind dense brush. Perception check required to find it. Litlock's residence; also houses Lynds and Aurix the Kobold child. Appears as a yurt from outside. Several trusted NPCs have access.|
|— Common Room                   |Entry and gathering space. Large fireplace. Litlock's presence felt here most strongly on first visit — dulls with time.|
|— Kitchen                       |Domestic kitchen. TBD contents and use.                                      |
|— Garden                        |Large garden outside the Dankhaus. TBD — possible ingredient/item source.    |
|— Litlock's Room                |Litlock's private bedroom. TBD access and contents.                          |
|— Litlock's Study               |Litlock's workspace. TBD — likely quest-relevant items or information.       |
|— Lynds's Room                  |Semi-permanent residence of Lynds. TBD occupant details.                     |
|— Aurix's Room                  |Room of Aurix the Kobold child. TBD.                                         |
|**Magical Wards** *(design note)*|The Dankhaus has complicated magical wards that bar unwanted entry. **Needs dedicated design pass — likely becomes a mechanic.** See ward-removal ideas in Open Questions.|
|**Main Street**                 |Three-room commercial spine of Roundabout. Directions and connections: Town Hall to the north of Roundabout Town Square; Tavern to the south of Roundabout Town Square; Library to the north of Main West; Archery Range continues west of Main West; Church of All to the south of Main East. The Alley is accessible southwest from Roundabout Town Square and southeast from Main West — exits north to Roundabout Town Square only.|
|— Main West                     |Western end of Main Street. Library to the north. Archery Range further west. Southeast leads to The Alley.|
|— Roundabout Town Square        |Center of town. Town Hall to the north. Tavern to the south. Southwest leads to The Alley. Contains a **fountain** — dry until Quest 22 (The Ruined Aqueduct) is completed. Once flowing, fountain water is required for Quest 49 (The Ruined Shrine) clay adhesive.|
|— Main East                     |Eastern end of Main Street. Church of All to the south. Roundabout Wasteland to the east. TBD buildings.|
|— The Alley                     |*The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.* Accessible from Roundabout Town Square (southwest) and Main West (southeast). Exits north to Roundabout Town Square only. South leads to The Back Alley.|
|— The Back Alley                |*Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.* Dead end behind the tavern. **Mugger mechanic:** A shadowy figure lurks here. Perception check fires every visit until the mugger is spotted and slain. On failed perception: player is mugged — loses 1 heart (physical damage) and 2–3 Zenni (random), loses consciousness, wakes in the Back Alley one turn later with no description of what hit them. If player has no Zenni: still mugged, 1 heart damage, nothing taken. Ink has no effect on mugger. On successful perception: mugger is visible — fight to the death. Losing the fight: player wakes in alley with 1 heart remaining and text nudging them to rest at the inn. Winning: mugger is slain permanently, Back Alley is safe. **Loot:** A set of lockpicks — usable as a trap disarm tool. Opens the large iron chest in the Mine Passage (mid-tier dungeon), which is bolted to the floor and contains 20 Zenni. **Quest Board:** After 100 turns if mugger not yet slain, May posts: *"One of my regulars got mugged last night. If anyone deals with whoever's lurking in the Back Alley, drinks are on me."* **Free drink reward:** When mugger is slain, a free drink flag is set (reason: "mugger"). Next time player buys a drink at the bar, May thanks them and doesn't charge. Flag cleared after use.|
|**Town Hall**                   |*The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.* North of Roundabout Town Square. Two floors plus tower.|
|— Main Entrance                 |Ground floor entry. Grand foyer. Stairs lead up to the Upper Hall. Council Chamber to one side, Records Room to the other.|
|— Council Chamber               |Ground floor, off the Main Entrance. Where town business is conducted. **Councilman Rowan Finch** is found here — grandson of Calder Finch, a noted dungeon explorer. Rowan is the quest giver for Quest 32 (The Missing Gravestone). Rewards the player with Calder's Middle Tier Key upon quest completion.|
|— Records Room                  |Ground floor, off the Main Entrance. Dusty and bureaucratic. Contains the **town charter** — required for Quest 27 (The Toll Bridge Operator — bridge in the Secret Tunnels gates the Dungeon entrance). The **Records Room Worker** initially refuses to hand over the charter. After the player returns the pocket watch (from the Chuckle House ghost quest), he gives up the charter as thanks — the watch belonged to his family. The connection between the watch and his family is a surprise to him. Charter is a quest item.|
|— Upper Hall                    |Second floor, top of the stairs. Connects to the Tower. Contains a display cabinet of old town documents and civic artifacts — unlocked, accessible from the start. `OPEN CABINET` reveals contents. The **wax seal** (Quest 4) is inside — `TAKE SEAL` picks it up. No perception check required.|
|— The Tower                     |Accessed from the Upper Hall. Top of the conical tower, overlooking Roundabout Town Square. Contains the **Trophy Case** — an achievement display for treasure items found during the playthrough. Shows count of treasures found (e.g. 8/10). **Rowan Finch dialogue:** TBD — his grandfather Calder was a dungeon explorer who likely donated early items to the case; Rowan should acknowledge this connection.|
|**Tale and Ale Tavern**         |Accessed from Roundabout Town Square (south). Exterior faces the square.     |
|— Main Room                     |Central gathering space. Entry point into the inn. Contains a mailbox — completely out of place, acknowledged by no one. `OPEN MAILBOX` teleports player to Will's Wizard Tower.|
|— Bar                           |Where drinks are ordered; 1-heart food & drink purchases happen here. May (bartender) works here. Quest Board is described in the room text; `LOOK AT BOARD` lists active posted quests.|
|— Ty’s Casino Corner            |Gambling area inside the tavern. TBD mechanics.                              |
|— Pipe Room                     |Smoking parlor. Atmospheric; natural gathering spot for Rogues and shady deals.|
|— Kitchen                       |Back-of-house. Shamus works here — cook and unofficial vendor. `TALK TO SHAMUS` to buy or sell items. Cellar door to the Cellar/Storeroom is here; bartender holds the key.|
|— Stable                        |Exterior, adjacent to inn. Horse/cart quest TBD.                             |
|— Upstairs Hall                 |Connects the three guest rooms.                                              |
|— Guest Room 1                  |TBD occupant/use.                                                            |
|— Guest Room 2                  |TBD occupant/use.                                                            |
|— Guest Room 3                  |TBD occupant/use.                                                            |
|— Cellar / Storeroom            |Below the kitchen; accessed via a cellar door in the kitchen. Bartender holds the key. Starts flooded — drain must be unclogged (crowbar required) before the room is usable. Once drained, reveals a door to the Secret Tunnel. The tunnel door can be opened or closed and stays in whatever state the player leaves it. Travel is freely bidirectional once the cellar is drained. Entering from either direction before draining = instant drowning fail state (no warning). **Open question:** Should entering from the kitchen side (before draining) trigger a perception check to notice the flood before stepping in, or is it always a surprise? Leaning no roll — resolve later.|
|**Library**                     |Medieval exterior with startling red double doors. Interior feels ancient — Babylonian/Egyptian in flavor but older, furnished for comfort. Dimensional magic extends the stacks beyond natural size. Foundation is secretly a temple to Thoth; all staff are priests/clergy. Only Litlock and long-time patrons know the true nature of the place. **Room description:** *The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between. A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold. The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.*|
|— Main Hall                     |Entry space. Lavish wood, copper, and gold. The endless shelves begin here.  |
|— The Stacks                    |Dimensional magic makes this space larger than possible. Books cannot be taken — `READ BOOK` in place only.|
|**Church of All**               |Appears as a normal medieval church from the outside. Near the Graveyard. Contains a dial at the altar that allows attunement to any of 7 religions. `TURN DIAL LEFT` and `TURN DIAL RIGHT` cycle through religions one at a time. Current attunement is shown in the room description. Attunement can be changed freely — no penalty. Attunement to specific religions is required for certain quests (TBD). Sub-rooms TBD — needs dedicated design pass.|
|— Keeper's Chamber              |The private quarters of the Keeper of the Faiths — the priest who oversaw the Church of All. Door is locked; key found on the Keeper's skeleton in the lower crypt of the dungeon lower tier. Inside: sparse quarters, personal effects, a **vial of holy water** on the writing desk, and a note in the Keeper's hand. The note reveals that the scholar of The Veil of the Arcane who descended into the lower passages was transformed into an undead werewolf by the ancient magic he was studying — and that the silver stake must be consecrated with holy water to be effective against him. The Keeper prepared the holy water but descended before he could use it and never returned.|
|— The Altar                     |Separate sub-room inside the Church of All. Contains the attunement dial and the ritual space. **Seven religions (dial order left to right):** (1) **The Verdant Circle** — *A sprouting seed inside a circle of leaves.* Nature, growth, forests, patience. (2) **The Veil of the Arcane** — *A seven-pointed star with a void at its center.* Magic as faith; mystery is sacred. (3) **The Brotherhood of the Pale Blade** — *A white sword on a black field.* Death, sacrifice, fallen warriors; calm about mortality. (4) **The Weavers of the Thread** — *Three threads braided into one, ends frayed.* Fate, destiny, the pattern connecting all lives. (5) **The House of the Coin** — *A coin, heads on one side, a question mark on the other.* Trade, wealth, fair dealing; merchants and vendors. (6) **The Keepers of the Lantern** — *A lit lantern with an open door.* Hope, healing, guidance for the lost; most publicly visible faith. (7) **The Hearth Folk** — *A fire inside a house outline, door open.* Family, shelter, belonging; the faith of ordinary people. **Ring quest ritual mechanic:** Three rituals involving three different religions must be performed here as part of the One Ring quest. Each ritual requires: correct religion attuned on the dial, the One Ring placed on the altar, and a specific artifact (found during quests, TBD). The artifact is consumed by the ritual. All three rituals must be completed to progress the ring quest. Which three religions and their artifacts TBD — needs dedicated design pass.|
|**Graveyard**                   |*The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it. The church is behind you. The mausoleum sits at the far end, grey and patient. The air is still in a way that has nothing to do with wind.* South of the Church of All. Single room. Denizens TBD. No ring quest artifact here — the Werewolf's Amulet (Veil of the Arcane ritual artifact) is dropped by the undead werewolf in The Still Den.|
|— The Mausoleum                 |*The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.* South of the Graveyard. Weathered and decrepit. Stairs lead down to The Crypt.|
|— The Crypt                     |Two-state description. **First visit:** *The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.* **Subsequent visits:** *The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.* **Third+ visits:** *The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.* Connects south to The Charnel Walk (Secret Tunnels).|
|**The Chuckle House**           |A funhouse. Location in Roundabout TBD. Four rooms, linear. Ring (invisibility) required throughout — all mirrors repel visible players. The hostile ghost of the Records Room Worker's missing relative haunts the building, trapping players. Quest 17 anchor. Layout: Entrance → Rejection Mirror → Shatter Trap Mirror → Ghost's Room.|
|— The Entrance                  |TBD — entry room, sets the tone. Mirror mechanic not yet active here.|
|— The Rejection Mirror          |A mirror that repels visible players — stepping in front of it while visible sends the player back to the Entrance. Passing while invisible (ring worn) proceeds normally. No ghost here — ghost is in the last room.|
|— The Shatter Trap Mirror       |A mirror that repels visible players. Also rigged with a crossbow behind the frame (Trap 16). Fires at any player passing through — visible or invisible. Perception check spots the firing pin and disarms it before it fires; otherwise the crossbow fires once and is spent. Either way, the trap is no longer a factor on the way out or on return visits. Mirror still repels visible players until the ghost is freed.|
|— Ghost's Room                  |Mirrors on all sides. The ghost of the Records Room Worker's missing relative haunts this room — hostile, does not want the watch recovered. Ghost is visible only while wearing the ring. `CAST UNBIND UNDEAD` (or scroll equivalent) releases the ghost; he says *"Thank you. I can rest now."* and departs, dropping the pocket watch. **Exit mechanic:** 50% chance each attempt to leave fails — player returned to same room with a disorientation message. Permanent — does not end when ghost is freed. **Post-freeing:** Mirrors no longer repel visible players anywhere in the Chuckle House. Watch remains on floor for pickup.|
|**May's hints — Ghost/Watch quest:**|**Before visiting Chuckle House — Tier 1:** People say the mirrors in the Chuckle House show more than they should. Most folks don't go back a second time. **Tier 2:** Word is a family member of the records room clerk went into the Chuckle House years ago and never came out. He doesn't talk about it. **Tier 3:** The trick with the Chuckle House is that some doors only open for people the mirrors can't find. **After visiting Chuckle House (ghost not yet freed) — Tier 1:** Malevolent spirits can only be freed through magic. **Tier 2:** Silas Bryne — keeps the lighthouse — mentioned he came across a spell he couldn't make heads or tails of. Left it on his desk. **Gating:** Post-visit hints unlock once player has entered the Chuckle House, regardless of how far they got.|
|**May's hints — Charter/Records Worker quest:**|**Tier 1:** The clerk's not giving up that charter easily. Some debts aren't paid in Zenni — and he's carrying one he doesn't know about yet. **Tier 2:** There are things the clerk would trade that charter for without a second thought. He just hasn't been offered the right one. **Tier 3:** Word is the records room clerk had a relative who went into the Chuckle House years ago and never came back. He doesn't talk about it. He's also the one sitting on the town charter, and he's not giving it up easily — but something personal might move him more than an argument would. **Special rule:** If the ghost quest is complete and the charter has not yet been obtained, Tiers 1 and 2 are auto-marked as given (whether purchased or not) and only Tier 3 is available for purchase.|
|**The Old Oak**                 |Between Beach Road Fork and Roundabout Forest. A large oak dominates this spot on the path uphill. A child stands here — a kite is tangled in the upper branches. `CLIMB TREE` retrieves the kite; a rune stone threaded on a cord falls free as it comes loose. `GIVE KITE TO CHILD` completes Quest 41. The rune stone is one of three needed for Quest 42 (The Runesmith's Commission).|
|**Roundabout Forest**           |*You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.* Single room. Transitional space above the mine. Connects downhill to The Old Oak. Possible Zenni discovery via perception check (TBD).|
|**Pie Rats Mining Inc.**        |Underground beneath Roundabout Forest. Legitimate mining facade; actually a smuggling front for the Pie Rats pirate faction. Lore: the Pie Rats established the mine generations ago as a supply and storage operation to support their seafaring raids — the tunnels connect to hidden sea-facing chambers used to move contraband. The forest above provides cover.|
|— Mine Entrance                 |Forest floor entrance. Sealed permanently after the cave-in explosion.       |
|— Main Shaft                    |Central spine of the mine. Connects the Mine Entrance (up) to the Mine Tunnels (down). Side passage leads to the Assay Room.|
|— Assay Room                    |Off the Main Shaft via a side passage. Where ore samples were tested. Connects to the Hidden Secondary Entrance into the Secret Tunnels. No treasure — gold nugget moved to Supply Cache (dungeon mid-tier trap side).|
|— Hidden Secondary Entrance     |Between the Assay Room and the Forgotten Shaft. Perception check required from the mine/Assay Room side; obvious and auto-discovered from the tunnel/Forgotten Shaft side. Remains accessible after the cave-in.|
|— Mine Tunnels                  |Working tunnels below the Main Shaft. Torch sconces on the walls — torches can be taken but immediately begin burning down (40 turn timer). Burnout is a fail state for the gunpowder sequence. Torch should be the last item taken before planting gunpowder — grabbing it early wastes it.|
|— The Rat's Nest                |Off the Mine Tunnels. Hidden storage for Pie Rat contraband. Contains the Pie Rat disguise required for the ship heist.|
|**Secret Tunnels**              |Underground pre-dungeon level connecting the Tavern Cellar, the mine, the Graveyard Crypt, and the Dungeon entrance. Entirely subterranean. Room count and layout subject to change as quests and traps are added.|
|— The Junction                  |First room off the Tavern Cellar. Hub of the Secret Tunnels — branches toward the mine (east), the Graveyard Crypt (west/TBD direction), and deeper into the tunnels toward the dungeon.|
|— The Undercroft                |Wide rough-hewn passage on the mine branch. Main trunk heading deeper toward the mine.|
|— The Forgotten Shaft           |Narrowing abandoned passage. Connects to the Hidden Secondary Entrance on the mine side.|
|— The Bone Passage              |Crypt branch off the Junction. Older stonework; tone shifts here toward the graveyard.|
|— The Charnel Walk              |Final room before the Graveyard Crypt entrance. Graveyard/crypt design is a separate design pass.|
|— The Toll Bridge               |Deep in the Secret Tunnels. A small bridge over an underground ravine — the only route to the Dungeon Entrance. A **Boggart** has claimed squatter's rights and charges an extortionate toll. Gives no hints about what would satisfy him. Perception check reveals faded official seal — public property — triggering quest discovery and unlocking May's one-tier hint. `GIVE CHARTER TO BOGGART` forces him out. He drops his strongbox (strength check to open — several turns' worth of Zenni). Bridge permanently free after. (Quest 27)|
|— Dungeon Entrance              |Beyond the Toll Bridge. The threshold between the Secret Tunnels and the Dungeon Upper Tier. First room of the dungeon proper. Connects south into the Ink Corridor.|
|**Dungeon — Upper Tier**        |15-room layout. Critical path runs Dungeon Entrance → Ink Corridor → Supply Room → [Narrow Passageway] → Idol Room → Combat Room → Quest Cache → Portcullis Corridor → Shrine Room → [Rickety Bridge] → Mid-Tier Key Door. Storage branch (Storage Area → Collapsed Gallery) splits off at Ink Corridor; Quest 38 shortcut exits into the Rickety Bridge. Creature Den and Flooding Room are spurs east off the Combat Room.|
|— Ink Corridor                  |First room past the Dungeon Entrance. A thin cord stretched at chest height carries an ink bladder — triggering it douses the player. No warning; the cord is invisible until hit. Room splits: west to Supply Room branch, east to Storage Area branch. (Trap 45)|
|— Supply Room                   |West branch off Ink Corridor. Shelves of old stores. Contains: sack of salt (described as "looks like it weighs as much as a Chachapoyan Fertility Idol"), mortar compound (Quest 18), portcullis bar (Quest 19), smoke jar (Quest 24 — guarded by Trap 17). **Trap 17:** A shelf of clay pots — disturbing it without disarming smashes one pot, dealing 1 heart smoke damage; smoke jar is then visible in the wreckage either way. Perception spots the unstable arrangement. **Layout note:** Supply Room must be reached before Idol Room — the sack of salt is required to safely swap the idol.|
|— Narrow Passageway           |Short connecting passage between the Supply Room and the Idol Room. Enforces item-first ordering — the player passes through the Supply Room before reaching the pedestal.|
|— Idol Room                     |South end of the Narrow Passageway. A **Chachapoyan Fertility Idol** sits on a pressure-sensitive pedestal. Removing it without replacing it with something of equal weight slams a stone door shut behind the player — no exit unless the player has the crowbar (`PRY DOOR`, strength check, not guaranteed). Safe swap: place the sack of salt on the pedestal simultaneously with `SWAP IDOL WITH SALT`. The idol is treasure. Connects south to Combat Room. (Trap 33)|
|— Storage Area                  |East branch off Ink Corridor. Wide chamber used for dungeon maintenance stores. Contains: hand cart (Quest 32), support beam (Quest 38). No passage deeper — the only way forward from this branch is via the Quest 38 shortcut once cleared.|
|— Collapsed Gallery             |South of Storage Area. A partially collapsed tunnel — timbers wedged across it blocking a secondary exit (Quest 38). Pickaxe from the mine required; three strength checks clear the timbers; propping with the support beam makes the shortcut permanent. **Exit: opens into the Rickety Bridge**, placing the player between the Shrine Room and the Mid-Tier Key Door. Dead-end until Quest 38 is completed.|
|— Creature Den                  |East of the Idol Room, directly adjacent to the Combat Room. Lair of **The Warden** — permanently empty after defeat. On examination after the fight: remnants of a uniform or insignia mark this as an official post, no names. Something that was stationed here deliberately, long ago. The Warden drops a **named quest item** (see below) on defeat.|
|— Combat Room                   |South of the Idol Room. A pressure plate in the corridor before this room rings a bell in the Creature Den — the player hears the sound and knows something is coming before they enter. **The Warden** emerges: completely monstrous in appearance, no visible human origin on first encounter — the lore of what it once was is told by the den and its drop, not its face. Standard combat (attack and defend rolls only). One-time fight — den permanently empty after defeat. **Trap interaction:** Perception check spots the plate; disarming wedges it down, bypassing the fight entirely. `JUMP ON PLATE` triggers the bell deliberately — required for full completion since the Warden's drop is needed on the key side of the mid tier. **Enchanted Glasses:** Auto-reveal the plate, giving the player an explicit choice between disarm and trigger without a roll. Spur east (via Creature Den) leads to the Flooding Room. Connects south to Quest Cache. (Trap 29)|
|— The Warden's Drop             |**The Guardian's Lantern** — a magical lantern carried as part of the Warden's official duties as dungeon guardian. `TURN ON LANTERN` or `LIGHT LANTERN` both work. Flickers but does not light anywhere except the Dark Room in the lower tier, where it cuts through magical darkness and opens passage forward. Required to access the Spirit Room and Burial Chamber sub-chain in the lower tier.|
|— Flooding Room                 |Spur east off the Combat Room, accessed through or past the Creature Den. A low-lying cave room with a pressure plate that opens a sluice and floods the room in two turns. Three levers on the wall — Left (stuck, permanently spent), Right (breaks off, permanently spent), Middle (correct, closes the sluice). Once a lever is pulled it cannot be pulled again — "You already tried that one." No warning on entry; always a surprise on first visit. After a wrong pull on turn 1, the game delivers an explicit warning: *"The water is at your knees. One turn left."* Failure on turn 2 sweeps the player through the sluice into the mid tier directly below this room's map position — one-way, no damage, no return from above. Mid tier escape is via Quest 50 (Bog-NW exit). Perception check *before entry* spots the suspiciously clean pressure plate; disarming jams the plate before the sluice opens. **Design note:** A player who solves the lever puzzle on their first visit will never access the mid tier trap side — and Quest 50 (The Lost Apprentice) is on that side. To complete all quests, the player must be swept through at least once. This is intentional: the flooding room is the natural, unforced delivery mechanism for Quest 50 discovery. Players who disarm the trap before entry will need another route to the trap side — resolve during mid tier design pass. (Trap 41)|
|— Prayer Alcove                 |South of the Combat Room. A low stone alcove — looks like a dead end until examined. A carved niche in the back wall suggests it was used for devotion at some point. Contains: **crowbar** (Quest 25; Quests 19&30; Trap 33 escape); **vial of glacier melt** (Quest 34 mid room — `POUR VIAL IN WATER` freezes the pool, allowing the player to cross). Perception check reveals the alcove's full depth. Connects south to Portcullis Corridor.|
|— Portcullis Corridor           |South of Quest Cache. A metal portcullis blocks the corridor, carrying an arcane charge. Touching it without disarming: 1 heart lightning damage, stunned one turn. Three ways through: (1) perception check spots the charge and discharge mechanism in the wall; (2) disarm check discharges it safely; (3) strength check lifts it — only after discharge, otherwise triggers damage. Portcullis Bar (from Supply Room) props it permanently open with `USE PORTCULLIS BAR`. Without the bar it drops when released. (Trap 19)|
|— Shrine Room                   |South of Portcullis Corridor. A small carved stone room, older than the surrounding dungeon stonework. Contains one of the three Verdant Circle shrine bowl pieces (Quest 49) — visible on a perception check. Connects south into the Rickety Bridge.|
|— Rickety Bridge                |Short connecting passage between the Shrine Room and the Mid-Tier Key Door. Also the exit point for the Quest 38 shortcut — the Collapsed Gallery opens into this passage from the west, letting players who cleared the tunnel bypass everything above the Shrine Room. **Weight mechanic:** The bridge has a carry weight limit (exact number TBD — see weight system memory). If the player's inventory exceeds the limit, crossing fails: the bridge groans and the player is turned back. The player must drop items, cross, then return for them. The bridge is always crossable at the limit or below — this is a logistical puzzle, not a trap. Returning to retrieve dropped items works freely in both directions at or under the weight limit.|
|— Mid-Tier Key Door             |South end of the Rickety Bridge. Heavy iron door leading to the key side of the mid tier. *The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.* Picking with lockpicks returns: "This lock can't be picked." Finding this door triggers quest discovery for Quest 32 and unlocks May's three-tier hints. No Quest Board posting. Middle Tier Key (Quest 32 reward) is the only way through.|
|**Dungeon — Middle Tier**       |15-room layout. Key side (10 rooms) accessed via Middle Tier Key Door. Trap side (5 rooms) accessed via Flooding Room sweep only. Hole to Below (Stored Room collapse) is the only route to the lower tier.|
|— Key Door Landing              |Base of the key door staircase. Rough-cut cave room. Connects south to Mine Passage.|
|— Mine Passage                  |Worked cave section with old support timbers and rusting tools. Contains: charcoal (Quest 28, no perception check needed); silver dust (Quest 4, perception check required); large iron chest bolted to the floor — too heavy to move, lockpick-only (Back Alley mugger's lockpicks), contains 20 Zenni (mine payroll, abandoned). Connects south to Stored Room.|
|— Stored Room                   |Deliberate rubble fill hiding a hole below. Spur east to The Crevice. One `DIG` (shovel required) collapses floor permanently — becomes Hole to Below; spur east buried permanently. **Before:** *The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.* **After (Hole to Below):** *Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way. [Rope detail once rope tied off.]* Beam exposed by collapse — `TIE ROPE TO BEAM` enables bidirectional travel. `DOWN`/`UP`/`CLIMB DOWN ROPE`/`CLIMB UP ROPE` once rope tied. Rope found at the Docks (one item in world).|
|— The Crevice                   |Dead-end spur east of the Stored Room. A skeleton is wedged in a narrow crack — tried to squeeze through and failed. Gold pocket watch hangs from one outstretched finger. `TAKE WATCH` (treasure, sellable). Permanently inaccessible after Stored Room collapses — missable.|
|— Inscription Chamber           |Ancient inscription on cave wall (Quest 28: `RUB PAPER ON ENGRAVING` with thin paper + charcoal). Rune stone (Quest 42, perception check). Crawlspace in east wall leads to Cave Creature's Lair — revealed by Trap 8 (Rope Snare) trigger or perception check.|
|— Cave Creature's Lair          |Accessed via crawlspace off Inscription Chamber. Creature absent, never encountered. Bone flute on floor (Quest 7).|
|— Echo Alcove                   |Listening station. One-way acoustic connection to the Skeleton Room in the lower tier — the sound of bones grinding drifts up from below. Room description is the same on every visit: *"A faint grinding drifts up from somewhere far below — bone on stone."* The Guardian's Lantern (Warden's drop) activates the full cross-tier mechanical interaction — TBD during lower tier layout pass.|
|— Magnetic Vault                |Heavily magnetic room. Trap 15 (Magnetic Chest) on central chest — opening without disarming yanks all metal items to the chest; perception reveals metallic filings in ring around latch; disarm removes lodestone from lid. Diamond brooch inside (second most valuable treasure in game).|
|— Deep Lock Door                |End of key side critical path. Permanently sealed — no key, no lockpicks, dead end. Lower tier is reached only via the Hole to Below.|
|**Dungeon — Lower Tier**        |20-room layout (11 confirmed, 9 TBD). Entry via Hole to Below (rope required to return). Layout and critical path structure TBD.|
|— Lower Entry                   |Bottom of Hole to Below. Rope anchor point for return to mid tier.|
|— Lower Crypt                   |Early room. Contains the skeleton of the Keeper of the Faiths — robes identify him as a Keeper; same emerald wax seal as the statue note. Killed by an inert pendulum blade (Trap 5 variant) before reaching the werewolf; blade hangs motionless overhead, dried blood on the edge, skull split. Key ring: *"The skeleton's fingers are curled loosely around a ring of keys."* (In inventory: *"A ring of keys, old iron, worn smooth from years of use."*) Key opens the Keeper's Chamber in the Church of All.|
|— The Encampment                |Scholar and Keeper's research area. Journals, equipment, atmospheric remnants of two people who came here and did not leave. No mechanical trigger — context and lore only.|
|— Thermal Vent Room             |Warm air rises from fissures in the floor. Fire clay (Quest 49) pressed into ceiling overhang — invisible until `LOOK UP`, then `TAKE CLAY` retrieves it. No perception check. Jar whisper (*"The ceiling of the thermal vent holds a secret."*) is the only hint anywhere.|
|— Bone Crunch Floor Room        |Dry bones arranged plainly on the floor — no perception check needed. Warning text: *"The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here."* `CLEAR BONES` disarms. Moving through without clearing: instant death. Death text: *"The bones crack underfoot. The grinding stops. Then the doorway fills."* (Trap 36)|
|— Skeleton Room                 |Dead end. Full room of undead skeletons. Instant death on entry if Trap 36 triggered. Never required — nothing inside.|
|— Werewolf's Room               |Undead werewolf (critical path — ring quest). Cannot be harmed by conventional weapons. `DRIVE STAKE INTO WEREWOLF` with consecrated silver stake destroys it. Ivory Torch mounted on wall — take before leaving. Werewolf drops: **Werewolf's Amulet** (ring ritual artifact, The Veil of the Arcane).|
|— Tool Alcove                   |Quest 34 barrier room. North of The Junction. Appears as a dead end — empty iron brackets on walls. Speaking door disguised as back wall. Perception check required for discovery. **Three-state room:** (1) *Before discovery:* "The passage ends at a shallow recess lined with iron brackets — the kind used to hang tools or equipment. The brackets are empty. The back wall is flat and featureless." (2) *Perception check fires:* "Something in the back wall notices you. You're not sure how you know that, but you do." — immediately followed by persistent description. (3) *Persistent (after discovery):* "As you focus on the back wall, it asks you something. Once. The sound of it fills the alcove and then is gone, leaving only the clear impression that an answer is expected." `READ SCROLL` response: *"The wall goes quiet in a way it wasn't quiet before. Then, slowly, it opens. You get the sense it had begun to doubt anyone would ever answer."* — scroll consumed; passage north opens permanently. *Open state (all future visits):* "The passage ends at a shallow recess lined with empty iron brackets. The back wall stands open. It has nothing left to ask."|
|— Quest 34 Mid Room             |North of Tool Alcove. A channel of dark water fills the room wall to wall — narrow but uncrossable. **Room description:** *"Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it."* **Swimming penalty:** *"The moment you enter, the water is inside you somehow — not wet, not cold, just wrong. The pain that follows is real and serious and spreads fast. You are back at the doorway, bleeding from nowhere you can see."* (1 heart damage; player returned to doorway automatically.) **Freeze solution:** `POUR VIAL IN WATER` (vial of glacier melt from Prayer Alcove, upper tier) freezes the pool; player crosses freely.|
|— Quest 34 Fountain Room        |North of Quest 34 Mid Room. Contains a soldier encased in a block of magical ice — alive but suspended. **Room description:** *"Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed."* **Turn 1 (`HOLD TORCH NEAR ICE`):** *"The ivory torch throws heat that seems wrong for its size. Where the flame meets the ice, the frost retreats — a wet gleam spreading outward from the torch's reach. A single deep crack sounds from somewhere inside the block — not shattering, just shifting. A small clear window opens in the surface. Through it, the figure is closer than expected. Still composed. Still waiting."* **Turn 2 (`HOLD TORCH NEAR ICE`):** *"The crack deepens — then several more, fast, branching outward from the window. The block doesn't collapse so much as release. The ice falls away in sheets, and the soldier steps forward out of it as if he had been about to do so anyway. He blinks. He looks at his hands. He looks at you."* **Soldier handoff:** *"He looks at the sword at his side as if surprised to find it still there. He draws it and holds it out to you without ceremony. 'The Forgotten Blade,' he says. 'It has no business down here.' Neither, apparently, does he — he moves past you and is gone before you can speak."* Soldier reappears in town as a minor NPC offering free weapon training sessions. **Reward: The Forgotten Blade** — see Items.|
|— Dark Room                     |Magical darkness fills the passage ahead. Player can remain but cannot move forward — hard block, no damage, no escalation. Normal torches and Light spell ineffective. Guardian's Lantern (Warden's drop, upper tier) required. `TURN ON LANTERN` or `LIGHT LANTERN` dispels darkness and opens passage.|
|— Spirit Room                   |6–9 silent spirits. Terrifying in their silence. Hard block in both directions while player is visible — cannot move forward or back. One Ring (invisibility) required to pass. Spirits cannot be killed.|
|— Burial Chamber                |*"The chamber is circular, the walls carved with processions of figures — mourners, by the look of them, rendered in a style no living hand in Roundabout would recognize. Niches hold candles that have not burned in centuries, wax melted flat and cold. The plinth at the center holds the mask. Everything in this room was arranged deliberately, long ago, by people who are not coming back."* Contains: **Funeral Mask of Hammered Gold** (treasure) on central plinth. Taking the mask triggers no reaction from the spirits.|
|— Trap Side Entry               |Base of the sluice from the Flooding Room above. One-way drop, no damage. No exits except south.|
|— Dream Corridor                |Liminal branching passage between Trap Side Entry and Lost Apprentice's Cell. A 2×3×2 decision tree — 12 outcomes, 6 success, 6 failure. On failure the room resets and replays; player has no awareness of the loop until they pass through. Full tree in Special Mechanics section.|
|— Lost Apprentice's Cell        |Quest 50: combat with afflicted apprentice; post-combat `USE SHOVEL` finishes hole to Bog-NW; apprentice follows player out; Apprentice's Gloves reward (hands slot, +2/+3 combat TBD); quest completes on bog exit.|
|— Supply Cache                  |Partially collapsed side room. Contains a **gold nugget** — buried in the rubble, treasure item. Rewards exploration on the trap side.|
|— Flood Sump                    |Lowest point on trap side. Shallow pool. No confirmed items.|
|**Roundabout Beach**            |*Roundabout Beach opens up as the town falls behind you — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull. The lighthouse stands to the north on a finger of rock, its lamp turning slowly. It smells like freedom, or at least like salt.* Layout: Town → Beach → Docks (east/west TBD) → board ship → Roundabout Sea → Open Ocean. Lighthouse is north, perpendicular to the main axis. Players carrying a shovel will likely attempt to dig. `DIG` succeeds up to 5 times with flavor text (finding nothing but wet sand); on the 6th attempt: "The beach is littered with holes. There's nowhere else to dig." Each `DIG` counts as a turn (torch burnout and ring corruption tick normally).|
|— The Lighthouse                |Dead-end room off Roundabout Beach to the north, perpendicular to the main town↔docks axis. Open, unattended. A desk holds a scroll — the Unbind Undead spell, left by Silas Bryne (the keeper, an unmet NPC referenced only in May's Quest 17 hints). No quest assigned to this location beyond the scroll. Quests 14 and 23 both retired.|
|— The Docks                     |East (or west — TBD) of Roundabout Beach. *The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it, which she more or less does — the only vessel worth the name in Roundabout's harbor. The smell is fish and brine and honest work.* Boarding the ship from the docks puts the player on the Roundabout Sea. **Rope:** A coil of rope is visible as a takeable item — `TAKE ROPE` picks it up. This is the one Rope item in the world, used to tie off the Hole to Below beam in the dungeon mid-tier (`TIE ROPE TO BEAM`).|
|**Pie Rat Ship**                |Moored at the Docks. Crewed by Pie Rats until the explosion draws them away. The only vessel available to sail the Roundabout Sea. Boarding commands — all are synonyms: `BOARD SHIP`, `GET ON SHIP`, `CLIMB ABOARD`, `ENTER SHIP`. `BOARD SHIP` is also used to re-board from the Desert Island, returning the player to the Eastern Roundabout Sea.|
|— Deck                          |Main accessible area of the ship. TBD.|
|— Ship's Hold / Below Deck      |Hidden area of the ship. Contains a **treasure map** — found via per-turn perception check while aboard. Actually Enchanted Glasses guarantee finding it.|
|— Shovel                        |Found on the ship deck. One item in the world. Three confirmed uses: (1) Desert Island — digs up the buried chest; (2) Stored Room (dungeon mid-tier) — one `DIG` collapses the floor permanently, creating the Hole to Below; (3) Quest 50 (Lost Apprentice's Cell) — finishes the apprentice's hole to Bog-NW exit.|
|**Roundabout Sea**              |Three-room coastal body of water between the Docks and the Open Ocean. The Desert Island is visible from the Eastern Roundabout Sea and accessible as a spur — not on the main east axis.|
|— Western Roundabout Sea        |*The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore. Ahead, the coast begins to fall away.*|
|— Roundabout Sea                |*The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.*|
|— Eastern Roundabout Sea        |*Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. Nothing out here suggested this was coming. It sits quietly off the bow, waiting to be noticed. East of it, the sea continues without comment.* `DOCK`, `LAND`, `MOOR`, or `MAKE LAND` puts the player ashore on the Desert Island. Continuing east enters the Open Ocean.|
|**Open Ocean**                  |69 rooms extending east from the Eastern Roundabout Sea. Kevry's Secret Hideout is at square 69. Each room draws a random description from the pool below. The rare option triggers infrequently. **Standard pool:** (1) "Open ocean in every direction. Nothing else." (2) "The ocean does not vary its presentation." (3) "No land. No landmarks. Just the creak of the hull and the indifferent sea." (4) "The ocean offers nothing in any direction. It does not apologize for this." (5) "Sea. Sky. Nothing else to report." **Rare option:** "You could swear you heard laughter just now. Distant, directionless. The ocean is empty in every direction. You've been out here a while." Rare option triggers at 1-in-100 chance per room entered.|
|**Desert Island**               |A spur off the Eastern Roundabout Sea — not on the main east axis. Visible from the Eastern Roundabout Sea. Reached via `DOCK`, `LAND`, `MOOR`, or `MAKE LAND`. `BOARD SHIP` returns the player to the Eastern Roundabout Sea. Appears to be the obvious payoff for sailing east — masks Kevry's location 69 squares further into the Open Ocean.|
|— Island Shore                  |*The sand on the beach is undisturbed. That fact, for some reason, does not comfort you. Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone. The quiet here is a different kind of quiet than the open ocean — heavier, more deliberate. You have the distinct feeling that something happened here once. The island isn't telling.* The only room on the island. A buried chest is here — not visible without digging.|
|— Buried Chest                  |Dug up with the shovel. With the treasure map: `DIG` succeeds immediately. Without the map: 10% chance per `DIG` attempt. Actually Enchanted Glasses auto-succeed the map perception check aboard the ship, making the chest guaranteed. Contents: 30 Zenni + TBD quest item.|
|**Kevry's Secret Hideout**      |Easter egg. 69 squares into the Open Ocean. No hints from May. Boarding commands (`DOCK`, `LAND`, `MOOR`, `MAKE LAND`) to come ashore; `BOARD SHIP` returns player to Open Ocean square 69.|
|— Land, Ho!                     |*The island resolves out of the horizon slowly, then all at once. Sand, trees, solid ground. You've earned this. The beach curves invitingly ahead.* First room on the island. Same boarding mechanic as Desert Island.|
|— Empty Beach                   |*The beach is long and quiet, the sand unmarked. A line of scrubby trees runs along the inland edge. Somewhere beyond them, half-hidden, a small structure. The only sounds are the water behind you and the wind doing very little. It feels like a place that has been left alone for a long time and is content with that.*|
|— A House                       |*The interior is cluttered in the way that only makes sense to its owner. Charts pinned to every surface, ropes coiled with obsessive care, a hammock in the corner. A lantern hangs from a beam. Someone has been here a long time and made their peace with it.* Room name changes to Kevry's House after the player enters and interacts with Kevry.|
|— Captain's Quarters            |*A small back room, all table and charts and the smell of ink. A weathered man sits hunched over a map, muttering. He doesn't hear you come in. When he finally looks up, his face does something complicated — surprise, then recognition of the type that doesn't require prior acquaintance, then a wide and genuine grin.* Kevry is found here. Eccentric, friendly, excited to see another sailor. Enchants the Enchanted Glasses if already equipped in the head slot. **Design note:** Unlike the rest of the game, this section is dialogue-heavy. Full dialogue tree for Kevry needs a dedicated design pass.|

-----

## Key NPCs

### May *(Bartender, Tale and Ale)*

- A tall, fit woman with shoulder-length red hair. Looks to be in her late thirties. Tomboyish — focused on comfort and practicality rather than style.
- Works the bar in the Tale and Ale.
- **First interaction:** Gives a free introductory hint pointing the player to the Quest Board, and mentions that she knows more for a small tip — introducing the hint system.
- Subsequently sells tiered hints for Zenni (see Hint System below).
- **Free drink flag system:** A boolean flag tracks pending free drinks, each with a reason string for contextual dialogue. Flag is set by quest events; cleared after the free drink is redeemed on the player's next drink purchase. Current known flags: (1) **Mugger slain** — *"May thanks the player for dealing with whoever was lurking in the Back Alley, and doesn't charge for the drink."*

-----

### Shamus *(Cook & Vendor, Tale and Ale)*

- *Shamus is short and wide, with a shaved head and a grey beard that hasn't been trimmed in some time. He moves around the kitchen with surprising efficiency for his size. He doesn't say much, but when he does it tends to be useful. The kind of man you'd go to if you needed something that wasn't on any official list.*
- Found in the Tale and Ale Kitchen.
- Officially the cook. Unofficially, the vendor — he can "get stuff."
- **Stock:**

| Item | Cost | Buyback |
|------|------|---------|
| Gunpowder | 5 Zenni | 2 Zenni |
| Tip Journal | 5 Zenni | 2 Zenni |
| Fishing Rod | 8 Zenni | 4 Zenni |

- Buyback is half price, items sold by Shamus only. No buyback for treasure or found items.
- Additional stock TBD — alternate light sources for the mine heist at minimum.

### The Librarian *(Library)*

- Half-elf, half-Kenku. A unique NPC — the only one of her kind in Roundabout.
- Elves staff the library; Kenku ibis-form librarians assist. She bridges both.
- All library staff wear blue/green monk robes; those in charge have emerald cuffs. She has emerald cuffs.
- **Interaction:** `TALK TO LIBRARIAN`. Her Kenku heritage shapes her speech — she stitches together fragments she has overheard, often verbatim phrases from conversations she's had. For the scholar quest, the fragments she stitches are things the scholar said to her directly, making her account feel like grief rather than exposition.
- **By topic:** Player asks about a subject; she offers several matching titles. Player must `READ BOOK` on each — only the correct one advances the quest. Wrong books yield flavor text only.
- **By title:** Player names the specific book; she retrieves it directly. One `READ BOOK` and done.
- Synonyms are accepted — asking about "sorcery" and "magic" yield the same list.
- Books cannot be taken from the library.
- May's hint system ties in: Tier 1–2 hints send the player to the library by topic; Tier 3 names the specific title.

**TALK TO LIBRARIAN — First interaction:**

She sets down what she's holding and folds her hands on the desk. Her voice arrives in pieces — tones and rhythms that don't quite match, stitched together at the seams.

*"I have been waiting for* someone *to come asking."*

She pulls a thin ledger from under the desk without looking for it.

*"'The Veil of the Arcane — I need access to whatever you have.' That's what he said. First thing. Didn't introduce himself. I didn't ask."*

She opens the ledger to a marked page.

*"He was here for —* weeks. *Every day. 'Have you found anything else? Anything older?' He was very — 'I think I've found something. I think I know where it is.' "*

She closes the ledger.

*"And then he stopped coming. I checked the application. There's a date. There's no — 'I'll be back by —' there's no return date. There never was."*

She looks at you steadily.

*"'The lower passages. That's where it will be. That's where everything that old ends up.' "*

She sets the ledger aside.

**TALK TO LIBRARIAN — Subsequent visits (before werewolf defeated):**

*"'The lower passages.' That's all I have. That's the last thing."*

**TALK TO LIBRARIAN — After werewolf defeated:**

She looks at you for a moment when you come in.

*"'It's not a dead end — it's* a beginning.' "*

She picks up her book.

*"He said that once, about a research problem. I think about it."*

### Lynds *(Tale and Ale regular)*

- Known for his **strength** — renowned in Roundabout.
- Found in the Tale and Ale bar.
- Will **arm wrestle any player who asks**, at any time — no gating required.
- The arm wrestle is a **strength-based challenge roll**; higher player level improves the odds.
- On **losing:** Lynds is impressed and genuinely surprised — reacts warmly, not as a sore loser.
- On **winning (player loses):** TBD reaction; player can return and try again as they level up.
- **Beating Lynds** rewards two things:
  1. The **Heart Necklace** (permanent +1 heart).
  2. An **invitation to the Dankhaus** — the mechanic that bypasses the magical wards and grants access to Litlock.

-----

## Hint System

### May's Tips

- May sells hints ("tips") for Zenni at the Tale and Ale bar.
- **3 tiers** per quest: Tier 1 (vague nudge) → Tier 2 (more specific) → Tier 3 (near-explicit).
- Hints are unlocked by **tip amount**, not order. The player tips any amount; May responds based on how much was given. The player never sees exact tier costs — they discover the ranges through play.
- **Tier costs:** Tier 1: 1–3 Zenni. Tier 2: 4–6 Zenni. Tier 3: 7–12 Zenni.
- Each tier for each quest is a **one-time purchase** — May will not re-sell a tier already bought.
- May only offers hints for quests that are: **discovered AND incomplete**. She won't hint on undiscovered or finished quests.
- **May's responses by tip amount:**
  - **Tier 1 (1–3 Zenni):** *May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.*
  - **Tier 2 (4–6 Zenni):** *May pockets the coins carefully. "That buys you something worth hearing," she says.*
  - **Tier 3 (7–12 Zenni):** *May counts the coins once, pockets them, and leans all the way across the bar.*
  - **Nothing to share (any amount, no hints remaining):** Randomly selected from: (1) *May pushes the Zenni back. "Keep it. I've got nothing worth that right now." She goes back to wiping the bar.* (2) *May looks at the coin and shakes her head slowly. "I'd be robbing you. Ask me again when something changes."* (3) *May sets the Zenni on the bar and slides it back. "Nothing in here worth selling today," she says, tapping her temple.*
  - **Over 12 Zenni:** *May looks genuinely uncomfortable. "I appreciate the thought, but no." She slides it all back. "Ask me something and we'll talk."*

### Tip Journal

- A purchasable item (vendor TBD).
- Available to the player on request at any time.
- Records:
  - Quests discovered and their discovery source (May, Quest Board, or organic)
  - Hints purchased per tier per quest
  - Quest completion status
- A quest does not appear in the journal until it has been discovered — undiscovered quests are invisible to the player.

### Quest Board

- Located in the Bar of the Tale and Ale — described in the room text.
- `LOOK AT BOARD` command displays all currently posted quests.
- Completed quests are automatically removed from the board.
- Some quests, when triggered or completed, **post new entries** to the board — creating a cascade of unlockable content.
- Counts as a quest discovery source for journal tracking purposes.

-----

## Open Questions & Design Notes

- [x] Red Knight name — The Redcrosse Knight: Knight of Faith. Antagonist of the "Fight the Knight" quest.
- [x] Heart Necklace — rewarded by beating Lynds at arm wrestling.
- [x] Bathing cost after ink trap — included with inn rest at 5 Zenni.
- [x] Vendor mechanic — Shamus (cook, Tale and Ale Kitchen). Sells gunpowder (5Z), Tip Journal (5Z), Fishing Rod (8Z). Buyback at half price for his items only.
- [x] Archery trainer — Raznak, Viking, at Archery Range. Requires Viking trust trials. Three NPC states designed.
- [ ] Finalize number of levels and XP thresholds.
- [ ] Design 2–3 quests that require or benefit from ring invisibility (Chuckle House is one; need 1–2 more).
- [ ] Define full list of spell types available via scrolls.
- [ ] Player name — review all NPC dialogue and flag where name use is appropriate once familiarity established. Priority: May, Shamus, Raznak, Redcrosse Knight, Vikings.
- [ ] Pyronicus forging interaction — design the full quest/scene for bringing the Viking runed metal to Pyronicus and receiving the Pale Blade.
- [ ] Design 2–3 additional chests in the world — locations, contents, Zenni amounts TBD.
- [ ] Treasure case in Will’s Wizard Tower — prices for treasure items (ship-in-a-bottle, gold nugget, etc.) TBD.
- [ ] Ty’s Casino Corner — Zenni stakes for Cargo game TBD.
- [ ] Hearty stew (Quest 40 inn upgrade) — set Zenni cost for 2-heart option.
- [ ] Assign quest Zenni rewards across all quests once quest list is finalized.
- [ ] Flesh out the Redcrosse Knight as full NPC — location, personality, Fight the Knight quest design.
- [ ] Armor items to design for head, chest, legs, hands slots.
- [ ] Define all challenge roll types and their dice.
- [x] Chuckle House — four-room linear layout designed and locked. Quest 17 fully resolved. Room descriptions and Roundabout placement still TBD (writing pass).
- [x] Dungeon/Cave Area — upper tier 15-room layout finalized. See Dungeon Upper Tier section.
- [x] Dungeon upper tier — Quest 38 Collapsed Gallery exit resolved: opens into Rickety Bridge.
- [x] Dungeon/Cave Area — lower tier layout and critical path structure finalized. All 17 rooms confirmed.
- [x] Dungeon upper tier — Combat Room creature: The Warden. Former dungeon guardian, now mindless. Monstrous appearance, standard combat, one-time fight. Den shows uniform/insignia remnants post-fight.
- [x] Dungeon upper tier — The Warden's drop item: **Guardian's Lantern** — magical lantern required to dispel magical darkness in lower tier Dark Room.
- [x] Dungeon upper tier — Flooding Room: no damage on sweep, displacement only. Destination = mid tier position directly below. One-way.
- [ ] Finalize corruption challenge roll: dice type, difficulty, outcome messages for near-miss vs. clean success vs. failure.
- [ ] **Dankhaus magical wards — design pass needed.** Five candidate mechanics: (1) Litlock’s invitation (2) ward token (3) spell/scroll (4) reputation threshold (5) ring invisibility at corruption cost.
- [ ] Hint system — review Zenni tier cost ranges (1–3, 4–6, 7–12) against final economy once quest rewards set.
- [ ] Lynds — define reaction when player loses the arm wrestle.
- [ ] Quest Board — design full cascade: which quests unlock new postings and in what order.
- [x] Viking Encampment — all three trials designed and locked. NPCs named. Room descriptions complete.
- [ ] Town Hall — Upper Hall contents (wax seal display cabinet confirmed; further contents TBD); Tower quest use.
- [ ] Church of All — sub-rooms; which quests require specific religion attunement.
- [x] Pie Rat Coin — confirmed as treasure item, no quest use.
- [ ] Pie Rat heist — define alternate light sources (harder to obtain than mine torch).
- [ ] Pie Rat Ship deck — flesh out sub-rooms and items/interactions aboard.
- [ ] Pie Rats Mining Inc. sealed section — determine items hidden there.
- [ ] Desert Island buried chest — determine TBD quest item alongside 30 Zenni.
- [x] Lighthouse — Quests 14 & 23 retired. Lighthouse is open, unattended. Unbind Undead scroll on Silas Bryne's desk. No further quest assigned.
- [ ] Graveyard — denizens TBD; dedicated design pass needed.
- [ ] Kevry’s island dialogue — full dialogue tree for Kevry; flagged as dialogue-heavy design pass.
- [ ] Opening Roundabout experience — May’s first interaction, Quest Board introduction, tutorial moment.
- [ ] Alternate light sources for mine heist — add to Shamus’s stock once designed.
- [ ] **Dice system** — design the dice mechanic (d6, d10, d20 etc.), roll thresholds, and how leveling improves rolls. Ties directly into XP/level scale.
- [ ] **XP/level scale** — design level cap, XP thresholds per level, and how leveling improves dice rolls. Ties directly into dice system. Design both together.
- [ ] **Dragon-nip quest** — glowing sprig hidden under the nightstand in Will’s bedroom. Practically impossible to find — requires perfect roll at highest level or Actually Enchanted Glasses equipped in the bedroom. Returning it to Will grants Golden Dragon Scale (treasure). Will suspects it came from his bedroom but doesn’t ask — dialogue TBD. Dragon-nip implies Will has a dragon familiar — never confirmed, only implied.
- [ ] **Dragon-nip dialogue** — flesh out Will’s reaction when player returns the dragon-nip. He suspects it’s his but doesn’t ask where it was found. Tone: quietly pleased, slightly embarrassed, says little.
- [ ] **Golden Dragon Scale** — treasure item reward for dragon-nip quest. Goes to Trophy Case in Town Hall Tower.
- [ ] **Trophy Case** — Town Hall Tower. Achievement display for treasure items (e.g. 8/10 found). Rowan Finch dialogue TBD — his grandfather Calder likely donated early items; add connection.
- [ ] **Treasure achievement system** — design full treasure list, total count, and end-game display. Replaces Zork scoring with achievement-style tracking.
- [x] **Enchanted Glasses descriptions** — "wire-rimmed glasses" (regular), "slightly glowing wire-rimmed glasses" (Actually Enchanted). In Will’s bedroom, description updates to show them on the nightstand after DROP GLASSES. Persists across visits.