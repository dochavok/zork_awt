# Enchanted Realms: One Ring — Design Reference

## Source of Truth for Game Design

All game design decisions are recorded in `c:\zork_awt\AWT_story_line\`:

| File | Contents |
|------|----------|
| `locations.md` | Every room: description, connections, items present, mechanics triggered, NPC states |
| `npcs.md` | Every NPC: dialogue states, quest role, name-use triggers |
| `items.md` | Every item: room/inventory descriptions, location found, quest use, consumable/missable flags |
| `quests.md` | All 50 quests: discovery trigger, steps, rewards, May's hint tiers, prerequisites, cascade effects |
| `traps.md` | All traps: mechanics, location, disarm methods, consequences |
| `mechanics.md` | All confirmed game mechanics and systems (combat, corruption, dice, parser verbs, etc.) |
| `ring-rituals.md` | One Ring critical path end-to-end: three artifact quest lines, Church of All rituals |
| `gameplay design.md` | Core systems reference: classes, economy, combat framework, NPC deep dives, world overview |

## The Rule

**When designing anything new, update the relevant file above immediately.**

Do not store design decisions in memory files. Memory is for session context and cross-session reminders only — not authoritative content. If a design decision lives only in memory, it will eventually be lost.

## Reading Order for a New Session

To get full context on the current state of the game, read in this order:
1. `gameplay design.md` — systems, classes, economy, DM NPCs
2. `locations.md` — world geography and dungeon layout
3. `quests.md` — quest status and cascade
4. `ring-rituals.md` — critical path status
5. `npcs.md` and `items.md` as needed for specific design work
