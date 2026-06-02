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
- Spent on: inn rest (full heal), food and drink (1 heart), and skill training.

### The Inn

- One inn exists in the game.
- **Rest** — Full heal, costs Zenni.
- **Food & Drink** — Restores 1 heart, costs Zenni.
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
- The range is a hazardous area — players passing through may be hit by stray arrows (challenge roll to avoid).
- A quest exists to permanently disable the stray arrow hazard.
- Trainer details TBD.

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
- Enchanted Glasses provide a small bonus to perception checks.
- Actually Enchanted Glasses pass all perception checks automatically — no roll required.
- Found in **Will Passion’s Bedroom** — a hidden room inside Will’s Wizard Tower. Room description includes "where the magic happens."
- Upgraded to Actually Enchanted Glasses by **Kevry Talborn** — but only if the glasses are already equipped in the head slot when the player visits him.
- **Warning:** Wearing the glasses out of Will’s Bedroom triggers an instant fail state (Will attacks — no recovery). The player must pick them up and leave without equipping them.
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

### Spell Scrolls

- Found throughout the world.
- Mages: read to learn the spell. Scroll is consumed.
- Warriors/Rogues: must bring to a DM (likely Will) to learn. Scroll is consumed.

-----

## Special Mechanics

### The Mirror Room

- A standalone location (TBD placement in the world).
- Contains a mirror. If the player passes the mirror while **visible** (ring not worn), “yourself sees you” — the player is immediately kicked back to the room they came from.
- Passing the mirror while **invisible** (ring worn) proceeds normally.
- This is a single specific puzzle room, not a global rule.
- Design note: creates a natural incentive to use the ring, directly feeding into corruption temptation.

### The Dig Room

- Located in a new dungeon/cave area (TBD).
- Contains a spot that can be dug — only revealed on a successful **perception check**.
- Digging the spot causes the **entire floor to collapse**. The player automatically falls through to the room below with no input.
- This creates a **one-way connection** downward — there is no falling back up through the hole.
- An **alternate path back up** must exist within the dungeon (TBD design).
- **Open question:** Does the fall deal damage? TBD.

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

1. **Find the disguise** — Pie Rat disguise found in the Mine Tunnels beneath Roundabout Forest.
2. **Buy gunpowder** — Purchased from the Vendor (TBD location). Gunpowder alone does nothing without a light source.
3. **Take a torch** — Torch sconces in the mine tunnels. Taking a torch starts an immediate burnout timer — it cannot be extinguished, only burns down. **Burnout = fail state.** Alternate light sources exist but are harder to obtain (TBD).
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

Opening the mailbox teleports the player to **Will’s Wizard Tower**. Will can teleport players back to the White House.

- Likely teaches non-mage classes how to learn spells from scrolls.
- One of the more mechanically important DMs for Warrior and Rogue players.
- **Sends the player on the One Ring quest** — aware that the ring landed in Pyronicus’s home, Will dispatches the player to retrieve it.
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

**Location:** A small island, **69 moves across the sea** *(Easter egg)*

- Requires a boat to reach.
- Optional — not required for game completion.
- **Enchants the Enchanted Glasses** — but only if they are already equipped (head slot) when the player arrives.
- The long journey is the reward in itself for dedicated explorers.

-----

### Pyronicus

**Location:** TBD — likely a **volcano or fire area**

- Name implies fire; environment TBD.
- **Holds the One Ring** — it fell through his roof. He is not hostile about it and surrenders the ring willingly when the player arrives on Will’s errand.
- Role otherwise distinct from other three DMs, TBD.
- The fire/volcano area would be a unique, dangerous environment.

-----

## World & Locations

|Location                        |Notes                                                                        |
|--------------------------------|-----------------------------------------------------------------------------|
|White House                     |Opening area; homage to Zork. Mailbox portal to Will’s tower.                |
|Town                            |Central hub; inn, archery range nearby.                                      |
|Archery Range                   |Edge of town; hazardous stray arrows; quest to make safe.                    |
|The Bog                         |Four rooms; one hides Litlock’s house. Perception-gated.                     |
|The Sea                         |69 moves to Kevry’s island. Requires boat.                                   |
|Kevry’s Island                  |Small location. Easter egg.                                                  |
|Will’s Wizard Tower             |Accessed via mailbox portal.                                                 |
|— Will Passion’s Bedroom        |Hidden room inside the tower. "Where the magic happens." Contains the Enchanted Glasses. Equipping the glasses here triggers an instant fail state.|
|Mirror Room                     |Standalone location TBD. Visible players are repelled; ring required to pass.|
|Dungeon/Cave Area               |New area TBD. Contains the Dig Room with a collapsing floor puzzle.          |
|Volcano Area                    |TBD. Home of Pyronicus. Holds the One Ring until player retrieves it.        |
|**The Dankhaus**                |Three-bedroom home hidden in the bog behind dense brush. Perception check required to find it. Litlock's residence; also houses Lynds and Aurix the Kobold child. Appears as a yurt from outside. Several trusted NPCs have access.|
|— Common Room                   |Entry and gathering space. Large fireplace. Litlock's presence felt here most strongly on first visit — dulls with time.|
|— Kitchen                       |Domestic kitchen. TBD contents and use.                                      |
|— Garden                        |Large garden outside the Dankhaus. TBD — possible ingredient/item source.    |
|— Litlock's Room                |Litlock's private bedroom. TBD access and contents.                          |
|— Litlock's Study               |Litlock's workspace. TBD — likely quest-relevant items or information.       |
|— Lynds's Room                  |Semi-permanent residence of Lynds. TBD occupant details.                     |
|— Aurix's Room                  |Room of Aurix the Kobold child. TBD.                                         |
|**Magical Wards** *(design note)*|The Dankhaus has complicated magical wards that bar unwanted entry. **Needs dedicated design pass — likely becomes a mechanic.** See ward-removal ideas in Open Questions.|
|**Tale and Ale Tavern**         |                                                                             |
|— Main Room                     |Central gathering space. Entry point into the inn.                           |
|— Bar                           |Where drinks are ordered; 1-heart food & drink purchases happen here. May (bartender) works here. Quest Board is described in the room text; `LOOK AT BOARD` lists active posted quests.|
|— Ty’s Casino Corner            |Gambling area inside the tavern. TBD mechanics.                              |
|— Pipe Room                     |Smoking parlor. Atmospheric; natural gathering spot for Rogues and shady deals.|
|— Kitchen                       |Back-of-house. Cook NPC TBD; potential quest/information source.             |
|— Stable                        |Exterior, adjacent to inn. Horse/cart quest TBD.                             |
|— Upstairs Hall                 |Connects the three guest rooms.                                              |
|— Guest Room 1                  |TBD occupant/use.                                                            |
|— Guest Room 2                  |TBD occupant/use.                                                            |
|— Guest Room 3                  |TBD occupant/use.                                                            |
|— Cellar / Storeroom            |Below the kitchen. Contains a secret passage — destination TBD.             |
|**Library**                     |Medieval exterior with startling red double doors. Interior feels ancient — Babylonian/Egyptian in flavor but older, furnished for comfort. Dimensional magic extends the stacks beyond natural size. Foundation is secretly a temple to Thoth; all staff are priests/clergy. Only Litlock and long-time patrons know the true nature of the place.|
|— Main Hall                     |Entry space. Lavish wood, copper, and gold. The endless shelves begin here.  |
|— The Stacks                    |Dimensional magic makes this space larger than possible. Books cannot be taken — `READ BOOK` in place only.|
|**Pie Rats Mining Inc.**        |Underground beneath Roundabout Forest. Legitimate mining facade; actually a smuggling front for the Pie Rats pirate faction. Lore: the Pie Rats established the mine generations ago as a supply and storage operation to support their seafaring raids — the tunnels connect to hidden sea-facing chambers used to move contraband. The forest above provides cover.|
|— Mine Entrance                 |Forest floor entrance. Sealed permanently after the cave-in explosion.       |
|— Mine Tunnels                  |Working tunnels. Torch sconces on the walls — torches can be taken but immediately begin burning down. Burnout is a fail state for the gunpowder sequence. Pie Rat disguises are found here.|
|— Smuggling Chamber             |Deeper in the mine. Hidden storage for Pie Rat contraband. TBD items.       |
|— Hidden Secondary Entrance     |Below the main tunnels. Hidden — harder to find; perception check required, easier with enchanted glasses. Remains accessible after the cave-in. Any items in the sealed section are only reachable via this route.|
|**Pie Rat Ship**                |Moored at Roundabout Beach. Crewed by Pie Rats until the explosion draws them away. The only vessel available to sail the Roundabout Sea.|
|— Deck                          |Main accessible area of the ship. TBD.|
|— Ship's Hold / Below Deck      |Hidden area of the ship. Contains a **treasure map** — found via per-turn perception check while aboard. Actually Enchanted Glasses guarantee finding it.|
|— Shovel                        |Found on the ship deck. Required to dig on the Desert Island.|
|— Open Sea                      |Extends east from the Roundabout Sea. Each space appears identical: "You see the ocean for miles." Desert Island appears at 2–3 squares east. Kevry's Secret Hideout at 69 squares east.|
|**Desert Island**               |Small island 2–3 squares east of the Roundabout Sea. Appears to be the obvious payoff for sailing east — masks Kevry's location 66–67 squares further.|
|— Island Shore                  |The only room on the island. A buried chest is here — not visible without digging.|
|— Buried Chest                  |Dug up with the shovel. With the treasure map: `DIG` succeeds immediately. Without the map: 10% chance per `DIG` attempt. Actually Enchanted Glasses auto-succeed the map perception check aboard the ship, making the chest guaranteed. Contents: ~20 Zenni + TBD quest item.|

-----

## Key NPCs

### May *(Bartender, Tale and Ale)*

- Works the bar in the Tale and Ale.
- **First interaction:** Gives a free introductory hint pointing the player to the Quest Board, and mentions that she knows more for a small tip — introducing the hint system.
- Subsequently sells tiered hints for Zenni (see Hint System below).

### The Librarian *(Library)*

- Half-elf, half-Kenku. A unique NPC — the only one of her kind in Roundabout.
- Elves staff the library; Kenku ibis-form librarians assist. She bridges both.
- All library staff wear blue/green monk robes; those in charge have emerald cuffs. She has emerald cuffs.
- **By topic:** Player asks about a subject; she offers several matching titles. Player must `READ BOOK` on each — only the correct one advances the quest. Wrong books yield flavor text only.
- **By title:** Player names the specific book; she retrieves it directly. One `READ BOOK` and done.
- Synonyms are accepted — asking about "sorcery" and "magic" yield the same list.
- Books cannot be taken from the library.
- May's hint system ties in: Tier 1–2 hints send the player to the library by topic; Tier 3 names the specific title.

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
- Tiers can be purchased **in any order** — no requirement to buy Tier 1 before Tier 3.
- Each tier for each quest is a **one-time purchase** — May will not re-sell a tier already bought.
- May only offers hints for quests that are: **discovered AND incomplete**. She won't hint on undiscovered or finished quests.
- Zenni amounts per tier TBD — to be tuned once the game economy is finalized.

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
- [ ] Finalize number of levels and XP thresholds.
- [ ] Design 2–3 quests that require or benefit from ring invisibility (Mirror Room is one candidate).
- [ ] Define full list of spell types available via scrolls.
- [ ] Flesh out Pyronicus’s role and the volcano area beyond ring retrieval.
- [ ] Determine cost of inn rest and training in Zenni.
- [ ] Flesh out the Red Knight and archery trainer as full NPCs.
- [ ] Armor items to design for each slot.
- [ ] Additional armor slot review pass planned (flagged for later).
- [ ] Define all challenge roll types and their dice.
- [x] Heart Necklace — rewarded by beating Lynds at arm wrestling.
- [ ] Mirror Room — determine world placement.
- [ ] Dungeon/Cave Area — design layout, alternate path back up from dig room, and whether falling deals damage.
- [ ] Finalize corruption challenge roll: define dice type, difficulty, and full set of outcome messages for near-miss vs. clean success vs. failure.
- [ ] **Dankhaus magical wards — design pass needed.** Five candidate mechanics for what removes/bypasses the wards:
  1. **Litlock's invitation** — Litlock must explicitly invite the player during dialogue. The ward reads intent; uninvited entry triggers a magical repel or stun.
  2. **A ward token** — Litlock (or another trusted NPC) gives the player a physical token (coin, amulet, carved bone). Carrying it satisfies the ward. Token can be lost, stolen, or loaned to another character.
  3. **A specific spell or scroll** — A ward-breaking scroll exists in the world (rare, possibly guarded). Using it grants permanent access but may have consequences — Litlock knows and reacts.
  4. **Reputation threshold** — The ward is tied to the player's standing with Litlock or the town. Access unlocks automatically once a trust/reputation score is high enough, no item or dialogue required.
  5. **The ring** — Wearing the ring while approaching grants invisibility from the ward's detection. Access is gained, but each entry costs corruption ticks — a meaningful tradeoff that ties the Dankhaus into the ring mechanic.
- [ ] Hint system — tune Zenni costs per tier once game economy is finalized.
- [ ] Tip Journal — determine which vendor sells it.
- [ ] Lynds — define his reaction when the player loses the arm wrestle.
- [ ] Quest Board — design the full cascade: which quests unlock new board postings and in what order.
- [ ] Flesh out remaining spreadsheet locations: Church of All, Graveyard, Town Hall, Viking Encampment, Roundabout Wasteland, Chuckle House, Secret Tunnel, Roundabout Pond, Roundabout Forest, Back Alley, Roundabout Beach.
- [ ] Vendor mechanic — design shops, stock, and pricing. Vendor sells gunpowder (Pie Rat heist) and Tip Journal at minimum.
- [ ] Pie Rat Coin — determine which future quest uses it.
- [ ] Pie Rat heist — define alternate light sources (harder to obtain than mine torch).
- [ ] Pie Rat Ship deck — flesh out sub-rooms and any items/interactions aboard.
- [ ] Pie Rats Mining Inc. hidden secondary entrance — determine what items are hidden in the sealed section; note they are easier to find with Actually Enchanted Glasses.
- [ ] Desert Island buried chest — determine TBD quest item alongside the ~20 Zenni.
- [ ] Tune buried chest Zenni amount (~20) against final game economy.