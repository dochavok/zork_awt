# Roundabout: The God-Forsaken Ring — Experience & Leveling

Authoritative reference for XP sources, leveling curve, dice progression, and level rewards.
Update this file immediately when any XP value or level detail is designed or changed.

---

## Sources of XP

### Exploration (passive, automatic)
Each room has a defined XP value awarded the first time it is discovered. Most rooms award 1 XP. Significant destinations award more. Ocean traversal squares award 0 XP. Perception-gated rooms (hidden behind a perception check to discover) generally award double their base value; critical path rooms are set individually. All room XP values are defined in `locations.md`.

**Exploration total (all confirmed rooms): 133 XP**

---

### Quest Completion
Each quest has a specific XP value. All quests bumped by a flat +2 XP from base guideline values.

| Quest | Name | XP |
|-------|------|----|
| Quest 4 | The Whispering Jar | 10 |
| Quest 7 | The Bone Flute | 6 |
| Quest 12 | The Locked Music Box | 10 |
| Quests 19 & 30 | The Hollow Statue / The Undead Warden | 22 |
| Quest 17 | The Frozen Watch | 17 |
| Quest 22 | The Ruined Aqueduct | 10 |
| Quest 24 | The Beekeeper's Swarm | 10 |
| Quest 25 | The Flooded Cellar | 10 |
| Quest 27 | The Toll Bridge Operator | 6 |
| Quest 28 | The Archivist's Request | 6 |
| Quest 32 | The Missing Gravestone | 12 |
| Quest 34 | The Frozen Soldier | 17 |
| Quest 38 | The Collapsed Passage | 8 |
| Quest 40 | Shamus's Recipe | 6 |
| Quest 41 | The Child's Kite | 4 |
| Quest 42 | The Brotherhood Stones | 12 |
| Quest 49 | The Ruined Shrine | 17 |
| Quest 50 | The Lost Apprentice | 12 |
| Quest 51 | The Back Alley Mugger | 6 |
| Quest 52 | Make Litlock Laugh | 6 |
| Quest 53 | Will's Glasses | 10 or 20 (10 if regular Enchanted Glasses returned; 20 if Actually Enchanted) |
| Quest 54 | Fight the Knight | 8 |
| Quest 55 | The Archer's Trial | 6 |
| Quest 56 | Will's Teaching | 4 per spell |
| Quest 57 | The Viking Trust Trials | 12 |
| Quest 58 | The Dragon-Nip | 4 |
| Quest 59 | Beat Lynds | 5 |

**Quest total (confirmed): 254–264 XP** (Quest 53 variable — 219 if glasses not enchanted, 229 if Actually Enchanted)

---

### Trap Disarmament
Successfully disarming a trap awards XP. Triggering a trap awards nothing. Intentional triggers (e.g. `JUMP ON PLATE`) award nothing.

| Trap | Description | XP |
|------|-------------|----|
| Trap 5 | Swinging Blade Pendulum (inert — atmospheric only) | 0 |
| Trap 8 | Rope Snare — Ankle | 3 |
| Trap 15 | Magnetic Chest | 4 |
| Trap 16 | Mirror Shatter Trap | 3 |
| Trap 17 | Smoke Bomb Cache | 3 |
| Trap 19 | Electrified Portcullis | 5 |
| Trap 29 | Pressure Plate — Bell | 3 |
| Trap 33 | Weight-Sensitive Pedestal (safe swap) | 5 |
| Trap 36 | Bone Crunch Floor | 3 |
| Trap 41 | Pressure Plate — Flooding | 5 |
| Trap 45 | Invisible Thread — Ink | 5 |

**Trap total (confirmed): 39 XP**

---

### Combat
XP scales with enemy difficulty. Named/boss enemies award toward the higher end.

| Enemy | Location | XP |
|-------|----------|----|
| Back Alley Mugger | The Back Alley | 5 |
| Aylora (drinking challenge) | The Fire Pit, Viking Encampment | 2 |
| Afflicted Apprentice | Lost Apprentice's Cell, mid-tier trap side | 8 |
| The Warden | Combat Room, Dungeon Upper Tier | 12 |
| Undead Werewolf | The Still Den, Dungeon Lower Tier | 15 |

**Combat total (confirmed): 42 XP**

*Note: Additional combat encounters will be assigned XP during the combat design pass. Guidelines: standard enemies 2–4 XP, named/boss enemies 10–15 XP.*

---

## XP Summary

| Source | XP |
|--------|----|
| Exploration | 133 |
| Quests | 254–264 |
| Traps (disarm) | 39 |
| Combat | 42 |
| **Confirmed base total** | **478–488 XP** |
| Class bonus (Warrior) | +40 XP |
| Class bonus (Mage) | +46 XP |
| Class bonus (Rogue) | +50 XP |
| **Confirmed total with class bonus** | **518–538 XP** (varies by class and Quest 53 outcome) |

Class bonuses are awarded on top of base XP and vary by class. Quest 53 awards 10 XP (glasses not enchanted) or 20 XP (Actually Enchanted) — a completionist who sails to Kevry earns the higher value. All classes clear the Level 8 threshold of 420 XP comfortably on a completionist run.

Level 8 threshold: 420 XP. Every class clears it on a completionist run.

---

## Dice Progression

Players start with 1d6. Each level upgrades the dice pool — either better dice (larger die size) or additional dice. Players never see the numbers; they only see outcomes.

**Corruption removal roll exception:** Uses level dice only — no bonus applied. See `mechanics.md` (The God-Forsaken Ring — Late-stage removal).

| Level | Dice | Bonus | Min | Expected Value | Max |
|-------|------|-------|-----|----------------|-----|
| 1 | 1d6  | +0 | 1  | 3.5  | 6  |
| 2 | 2d6  | +1 | 3  | 8.0  | 13 |
| 3 | 2d8  | +2 | 4  | 11.0 | 18 |
| 4 | 2d10 | +3 | 5  | 14.0 | 23 |
| 5 | 3d10 | +4 | 7  | 20.5 | 34 |
| 6 | 3d12 | +5 | 8  | 24.5 | 41 |
| 7 | 2d20 | +6 | 8  | 27.0 | 46 |
| 8 | 3d20 | +7 | 10 | 38.5 | 67 |

---

## Leveling Curve

Front-loaded — early levels come quickly so the player feels progression before the dungeon. Slows through mid and late game.

| Level | Cumulative XP | Additional Hearts | Skill / Ability |
|-------|--------------|-------------------|-----------------|
| 1 | 0   | — | — |
| 2 | 20  | — | — |
| 3 | 45  | +1 | — |
| 4 | 85  | — | Lucky (reroll 1s on all roll types) |
| 5 | 145 | +1 | Second Glance (reroll failed perception checks once, invisible to player) |
| 6 | 225 | — | REST (recover 1 heart; 50-turn reuse; outside combat only) |
| 7 | 320 | +1 | Nobu's Favor (secret — see `mechanics.md`) |
| 8 | 420 | — | Finishing Move (all 3d20 roll 15+: instant kill; ~2.7% per combat roll; secret — see `mechanics.md`) |

Level 2 should be reachable through normal early exploration and one or two quests — the player should level up before they ever enter the dungeon, arriving feeling ready rather than fragile.

Hearts are granted at Levels 3, 5, and 7. The Heart Necklace (Lynds arm wrestling reward) is a separate source. Total maximum hearts: class base + 3 (leveling) + 1 (Heart Necklace).

**Hard constraint:** Corruption resistance (bonus die on ring removal challenge roll) is explicitly excluded from all level rewards. Ring corruption is never mitigated by any mechanic, item, or level reward.

---

## Class XP Adjustments

Each class gets a bonus in their natural domain. Class identity feels present in progression without locking any content. Bonuses are calibrated so a completionist run of confirmed content yields approximately 40–50 class bonus XP regardless of class.

- **Warriors** — +10 XP per combat kill (4 confirmed kills = +40 XP; grows naturally as combat design pass adds encounters)
- **Mages** — +1 XP per new dungeon room discovered (dungeon only — not overworld or ocean; 46 reachable rooms = +46 XP)
- **Rogues** — +5 XP per trap disarmed (10 disarmable traps = +50 XP)

**Class bonus totals (confirmed content):**

| Class | Bonus | Confirmed events | Bonus XP |
|-------|-------|-----------------|----------|
| Warrior | +10/kill | 4 kills | +40 XP |
| Mage | +1/dungeon room | 46 rooms | +46 XP |
| Rogue | +5/trap disarmed | 10 traps | +50 XP |
