# Roundabout: The God-Forsaken Ring

### Game Design Document v0.2

-----

## Overview

A Zork-style text adventure RPG. The player explores a rich world, uncovers hidden characters, manages resources, and faces a central moral dilemma: a ring of invisibility that slowly corrupts its wearer. The core loop balances exploration, combat, skill progression, and the ever-present temptation of the ring.

**Planned Versions:**

- *The God-Forsaken Ring* — This document. Centers on the corruption ring quest.
- *Two Towers* — Theme for the next game in the series.

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

Core mechanics are defined in `mechanics.md`. Systems covered there:

- Hearts & Health
- Zenni (Currency)
- The Inn
- XP & Leveling
- Dice & Roll System
- Challenge Roll Types (Perception, Strength, Agility, Trap Disarm, Fishing)
- Damage Types
- Class Bonuses
- Combat

-----

## Skill Progression

Skill progression is defined in `mechanics.md`. Quests covered there:

- Quest 54 — Fight the Knight (melee; Mage and Rogue)
- Quest 55 — The Archer's Trial (bow; Warrior and Mage)
- Quest 56 — Will's Teaching (spells; Warrior and Rogue)
- Quest 57 — The Viking Trust Trials (prerequisite for Quest 55)

-----

## Items & Equipment

### Armor Slots

Equipment occupies the following slots. Armor is found through exploration and never degrades.

- **Head**
- **Chest**
- **Legs**
- **Hands**
- **Neck** *(Heart Necklace quest reward)*
- **Ring** *(The God-Forsaken Ring)*

-----

## Special Mechanics

Special mechanics are defined in `mechanics.md`. Systems covered there:

- The God-Forsaken Ring & Corruption
- Enchanted Glasses
- Spell Mechanics
- Finishing Move
- Nobu's Favor
- Hint System (May)
- Tip Journal
- Quest Board
- Shovel & Dig Mechanic
- Zenni Rooms
- Skill Progression
- Chuckle House Mirrors
- The Stored Room / Hole to Below
- The Dream Corridor
- The Treasure Map
- The Pie Rat Ship Heist
- Guardian's Lantern — Dark Room Interaction
- Whispering Jar
- Undead Werewolf Chain
- Echo Alcove — Cross-Tier Audio
- Weight System (Rickety Bridge)
- Parser Verbs

-----

## World & Locations

See `locations.md` — authoritative room-by-room reference. All room descriptions, connections, items, mechanics, and NPC states live there.

-----

## Key NPCs

Key NPCs are defined in `npcs.md`. NPCs covered there include all Dungeon Masters (Will Passion, Litlock, Kevry Talborn, Pyronicus), trainers (Redcrosse Knight, Raznak), and town NPCs (May, Shamus, Lynds, The Librarian, The Archivist, and all others).

-----

## Open Questions & Design Notes

All open design questions are tracked in `todo.md`.

