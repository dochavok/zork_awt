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

### Weapon Training — The Red Knight

- Teaches melee weapon use to Mages and Rogues.
- Located TBD. *(Reminder: look up the name of the red knight.)*

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

- Two versions: **Regular** and **Enchanted**.
- Regular glasses provide a small bonus to perception checks.
- Enchanted glasses make perception checks significantly easier or guarantee success.
- Found in a **hidden room inside Will’s Wizard Tower**.
- Enchanted by **Kevry Talbots** — but only if the glasses are already equipped in the head slot when the player visits him.
- **Warning:** Wearing the glasses out of Will’s hidden room triggers an instant fail state (Will attacks — no recovery). The player must pick them up and leave without equipping them.
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

**Location:** Hidden beneath a bog

- Personality: **Jovial**.
- The bog contains four rooms. Only one has a hidden passage to Litlock’s house.
- Each time the player passes through the correct bog room, a perception check occurs.
- On success, the passage is revealed and **permanently visible** for the rest of the playthrough.
- On failure, the player passes through without noticing and can try again.

-----

### Kevry Talbots

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

|Location           |Notes                                                                        |
|-------------------|-----------------------------------------------------------------------------|
|White House        |Opening area; homage to Zork. Mailbox portal to Will’s tower.                |
|Town               |Central hub; inn, archery range nearby.                                      |
|Archery Range      |Edge of town; hazardous stray arrows; quest to make safe.                    |
|The Bog            |Four rooms; one hides Litlock’s house. Perception-gated.                     |
|The Sea            |69 moves to Kevry’s island. Requires boat.                                   |
|Kevry’s Island     |Small location. Easter egg.                                                  |
|Will’s Wizard Tower|Accessed via mailbox portal. Contains hidden room with the Enchanted Glasses.|
|Mirror Room        |Standalone location TBD. Visible players are repelled; ring required to pass.|
|Dungeon/Cave Area  |New area TBD. Contains the Dig Room with a collapsing floor puzzle.          |
|Volcano Area       |TBD. Home of Pyronicus. Holds the One Ring until player retrieves it.        |

-----

## Open Questions & Design Notes

- [ ] Red Knight name — *look this up.*
- [ ] Finalize number of levels and XP thresholds.
- [ ] Design 2–3 quests that require or benefit from ring invisibility (Mirror Room is one candidate).
- [ ] Define full list of spell types available via scrolls.
- [ ] Flesh out Pyronicus’s role and the volcano area beyond ring retrieval.
- [ ] Determine cost of inn rest and training in Zenni.
- [ ] Flesh out the Red Knight and archery trainer as full NPCs.
- [ ] Armor items to design for each slot.
- [ ] Additional armor slot review pass planned (flagged for later).
- [ ] Define all challenge roll types and their dice.
- [ ] Heart Necklace — determine which quest rewards it.
- [ ] Mirror Room — determine world placement.
- [ ] Dungeon/Cave Area — design layout, alternate path back up from dig room, and whether falling deals damage.
- [ ] Finalize corruption challenge roll: define dice type, difficulty, and full set of outcome messages for near-miss vs. clean success vs. failure.