Based on everything in the design docs, here’s a proposed XP system:

XP System Proposal

Sources of XP

Exploration (passive, automatic)  
Each room has a defined XP value awarded the first time it is discovered. Most rooms award 1 XP. Significant destinations award more. Ocean traversal squares award 0 XP. Perception-gated rooms (hidden behind a perception check to discover) generally award double their base value; critical path rooms are set individually. All room XP values are defined in locations.md.

Combat  
XP scales with enemy difficulty. These are guidelines — each combat encounter has a specific XP value defined during the combat design pass. Standard enemies: 2–4 XP. Named or boss-tier enemies: 10–15 XP. The design should ensure that avoiding combat is a meaningful trade-off — you skip the risk but also skip the reward.

Quest Completion  
Main quest milestones (critical path events): 20–30 XP each. Side quests scale with complexity — simple fetch quests award ~4 XP; multi-step quests award ~8–10 XP; long chains with prerequisites award 15–20 XP.

Trap Disarmament  
Successfully disarming a trap rather than triggering it awards 3–5 XP. These are guidelines — each trap has a specific XP value defined during the trap design pass. More complex disarms (multi-step, strength check required) award toward the higher end.

Skill Acquisition  
Completing the quest or trainer interaction that grants a new combat skill (weapon use, archery, first spell learned) awards a one-time bonus of 5 XP. For spells, only the first spell learned awards XP — subsequent spells do not. This keeps XP gain balanced across classes: every class gets exactly one skill-acquisition bonus, from different sources.

Dice Progression

Players start with 1d6. Each level upgrades the dice pool — either better dice (larger die size) or additional dice. A flat bonus to all rolls is added every level. Players never see the numbers; they only see outcomes.

| Level | Dice | Bonus | Min | Expected Value | Max |
|-------|------|-------|-----|---------------|-----|
| 1 | 1d6  | +0 | 1  | 3.5  | 6  |
| 2 | 2d6  | +1 | 3  | 8.0  | 13 |
| 3 | 2d8  | +2 | 4  | 11.0 | 18 |
| 4 | 2d10 | +3 | 5  | 14.0 | 23 |
| 5 | 3d10 | +4 | 7  | 20.5 | 34 |
| 6 | 3d12 | +5 | 8  | 24.5 | 41 |
| 7 | 2d20 | +6 | 8  | 27.0 | 46 |
| 8 | 3d20 | +7 | 10 | 38.5 | 67 |

Leveling Curve

Front-loaded — early levels come quickly so the player feels progression before the dungeon. Slows through mid and late game. No artificial cap; the world's total available XP (~460) is the ceiling.

| Level | Cumulative XP | Additional Hearts | Skill / Ability |
|-------|--------------|-------------------|-----------------|
| 1 | 0   | — | — |
| 2 | 20  | — | — |
| 3 | 45  | +1 | — |
| 4 | 85  | — | Lucky (reroll 1s on all roll types) |
| 5 | 145 | +1 | Second Glance (reroll failed perception checks once) |
| 6 | 225 | — | REST (recover 1 heart; 50-turn reuse; outside combat only) |
| 7 | 320 | +1 | Nobu's Favor (secret — see mechanics.md) |
| 8 | 420 | — | Finishing Move (all 3d20 roll 15+: instant kill; ~2.7% per combat roll) |

Level 2 should be reachable through normal early exploration and one or two quests — the player should level up before they ever enter the dungeon, so they arrive feeling ready rather than fragile.

Note: Corruption resistance (bonus die on ring removal challenge roll) is explicitly excluded from all level rewards. Ring corruption is never mitigated by any mechanic, item, or level reward. Hard constraint.

Hearts are granted at Levels 3, 5, and 7 — one per level. The Heart Necklace (quest reward) remains a separate source. Total maximum hearts: class base + 3 (leveling) + 1 (Heart Necklace) + any other quest rewards.

Class XP Adjustments

Each class gets a flat XP bonus in their natural domain. This makes class identity feel present in progression without locking any content.

	•	Warriors — +1 XP per combat kill
	•	Mages — +1 XP per new dungeon room discovered (dungeon only — not overworld or ocean traversal)
	•	Rogues — +1 XP per trap disarmed

