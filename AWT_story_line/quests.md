# Enchanted Realms: One Ring — Quests

Authoritative quest reference. All 50 quest slots with discovery trigger, steps, rewards, May's hint tiers, prerequisites, and cascade effects.
Update this file immediately when any quest detail is designed or changed.

**Quest numbering note:** Not all quest numbers are used. Numbers marked "Quest Removed From Game" were retired or removed during design and must not be reused. All retired ideas are archived in `unused_quest_ideas.md` (separate directory). Next available number: 52.

---

## Quest 1 — Quest Removed From Game

## Quest 2 — Quest Removed From Game

## Quest 3 — Quest Removed From Game

---

## Quest 4 — The Whispering Jar

**Discovery:** Inn's back room — a cracked ceramic jar hums faintly. Innkeeper mentions it used to call out warnings.
**Prerequisites:** Wax seal (Town Hall Upper Hall) + silver dust (Mine Passage, dungeon mid-tier, perception check) + restoration phrase (etched into base of jar — readable with perception check or Enchanted Glasses).
**Steps:**
1. `OPEN CABINET` in Town Hall Upper Hall → `TAKE SEAL` (no perception check)
2. Descend to Mine Passage in dungeon mid-tier → find silver dust (perception check required)
3. Return to jar → `PRESS SEAL`, `DUST JAR`, `READ INCANTATION`
4. Jar whispers once: *"The ceiling of the thermal vent holds a secret."* — one time only, never repeated.

**Reward:** The Whispering Jar hint points player to fire clay in the Thermal Vent Room (lower tier, `LOOK UP`). No other hint for this exists anywhere.

**May's hint (one tier only — unlocks once player has first descended to the lower tier):** *"That jar in the back room of the inn — people say it used to warn about things. If it's still got something to say, I'd want to hear it before going any deeper."*

---

## Quest 5 — Quest Removed From Game

## Quest 6 — Quest Removed From Game

---

## Quest 7 — The Bone Flute

**Discovery:** Quest Board posting — Pyronicus posts a notice 20 turns after the player first meets him.
**Prerequisites:** Access to Inscription Chamber (dungeon mid-tier).
**Steps:**
1. Find crawlspace off Inscription Chamber — revealed by Trap 8 (Rope Snare) trigger or perception check.
2. Enter Cave Creature's Lair (creature absent, never encountered).
3. Take bone flute from floor.
4. Return flute to Pyronicus.

**Reward:** Fireball spell scroll — castable in combat.

---

## Quest 8 — Quest Removed From Game

## Quest 9 — Quest Removed From Game

## Quest 10 — Quest Removed From Game

## Quest 11 — Quest Removed From Game

---

## Quest 12 — The Locked Music Box

**Discovery:** `LOOK AT MUSIC BOX` in Will's Wizard Tower — Will mentions it belonged to a student who never returned.
**Prerequisites:** Access to Will's Tower (available from start). Key is in Bog-NW hollow log.
**Discovery source:** Will directly (not May's list). Triggered by `LOOK AT MUSIC BOX` — no dialogue command needed.

**Will's hints (free, triggered by successive examinations):**
1. Will mentions the box and the missing student wistfully — quest discovered.
2. Will recalls the student spent a lot of time in the bog.
3. Will specifically remembers the student liked to hide things in hollow logs.
After all three hints given, subsequent `LOOK AT MUSIC BOX` repeats hint 3 only. Once scroll found, Will says nothing further.

**Steps:**
1. `LOOK AT MUSIC BOX` in Will's Tower — discovers quest, begins hint sequence.
2. Search Bog-NW — perception check reveals hollow log. Inside: music box key.
3. Return to tower → open music box with key → plays short melody → scroll inside.
4. **Mages:** Read scroll directly (consumed) → Light spell learned.
5. **Warriors/Rogues:** Take scroll to Will (cannot wear Enchanted Glasses in Will's presence) → scroll consumed, Light spell learned.

**Reward:** Light spell — 10 turns duration, 20 turns reuse timer.

---

## Quest 13 — Quest Removed From Game

## Quest 14 — Quest Removed From Game
*(Lighthouse quest — retired. See `locations.md` — Lighthouse.)*

## Quest 15 — Quest Removed From Game

## Quest 16 — Quest Removed From Game

---

## Quest 17 — The Frozen Watch

**Discovery:** Quest Board — Records Room Worker posts seeking news of a missing relative who entered the Chuckle House and never returned; asks for the relative's pocket watch if they are dead. Posting appears when the player delivers the One Ring to Will Passion (second briefing trigger).
**Prerequisites:** One Ring (required throughout Chuckle House); Unbind Undead spell (Lighthouse scroll).

**Steps:**
1. Find Quest Board posting.
2. Obtain Unbind Undead scroll from Lighthouse (Silas Bryne's desk).
   - Mages: read scroll directly.
   - Warriors/Rogues: bring to Will Passion.
3. Equip One Ring (invisibility required — all Chuckle House mirrors repel visible players).
4. Navigate Chuckle House: Entrance → Rejection Mirror → Shatter Trap Mirror → Ghost's Room.
5. `CAST UNBIND UNDEAD` on ghost → ghost says *"Thank you. I can rest now."* and drops pocket watch.
6. `TAKE WATCH` (50% exit-fail mechanic persists even after ghost freed — disorientation on failed exit attempt).
7. Deliver pocket watch to Records Room Worker → he gives town charter.

**Reward:** Town charter → required for Quest 27 (Toll Bridge/dungeon access).
**Corruption note:** Wearing the ring throughout the Chuckle House is an intentional corruption cost.

**May's hints (Ghost/Watch quest):**
- Before visiting — Tier 1: *"People say the mirrors in the Chuckle House show more than they should. Most folks don't go back a second time."*
- Before visiting — Tier 2: *"Word is a family member of the records room clerk went into the Chuckle House years ago and never came out. He doesn't talk about it."*
- Before visiting — Tier 3: *"The trick with the Chuckle House is that some doors only open for people the mirrors can't find."*
- After visiting (ghost not yet freed) — Tier 1: *"Malevolent spirits can only be freed through magic."*
- After visiting (ghost not yet freed) — Tier 2: *"Silas Bryne — keeps the lighthouse — mentioned he came across a spell he couldn't make heads or tails of. Left it on his desk."*

**May's hints (Charter/Records Worker):**
- Tier 1: *"The clerk's not giving up that charter easily. Some debts aren't paid in Zenni — and he's carrying one he doesn't know about yet."*
- Tier 2: *"There are things the clerk would trade that charter for without a second thought. He just hasn't been offered the right one."*
- Tier 3: *"Word is the records room clerk had a relative who went into the Chuckle House years ago and never came back. He doesn't talk about it. He's also the one sitting on the town charter, and he's not giving it up easily — but something personal might move him more than an argument would."*
- Special rule: if ghost quest is complete and charter not yet obtained, Tiers 1 and 2 auto-marked given; only Tier 3 available for purchase.

---

## Quest 18 — Quest Removed From Game

---

## Quests 19 & 30 — The Hollow Statue / The Undead Warden

*(Combined quest chain)*

**Discovery — Path A (The Scholar):** May's tier 1 hint: *"There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it."* → `TALK TO LIBRARIAN` reveals scholar researched The Veil of the Arcane and descended into the lower passages.

**Discovery — Path B (The Keeper):** May's hints (three tiers):
- Tier 1: *"The Keeper of the Faiths has gone missing. No one's seen him in some time."*
- Tier 2: *"Word is he went looking for someone — a scholar who'd gone into the deep passages and never come back."*
- Tier 3: *"No one can get into his office at the Church. Locked tight. You'd need his key to find out what he knew."*

**Discovery — Statue:** `LOOK AT STATUE` in Roundabout Town Square (no perception check — seam visible on examination). Attempting to open without crowbar: *"The base is sealed tight. Something with leverage could pry it open."*

**May's tier 1 hint (fires only if player has not yet examined the statue):** *"Someone was seen tampering with the statue in Roundabout Town Square. Probably nothing. Probably."*

**Steps:**
1. Get crowbar from Prayer Alcove (Dungeon Upper Tier — perception check reveals full depth of alcove).
2. `USE CROWBAR ON STATUE BASE` → reveals silver stake + folded note with Keeper's emerald wax seal.
3. Descend to Lower Crypt (Dungeon Lower Tier via Hole to Below) → find Keeper's skeleton under inert pendulum blade.
   - Robes and emerald seal match the statue note. Key ring on skeleton.
   - Room description: *"A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got."*
4. `TAKE KEYS` from skeleton.
5. Return to Church of All → use Keeper's keys on Keeper's Chamber door.
6. Inside Keeper's Chamber: find vial of holy water + Keeper's note (reveals scholar became undead werewolf; holy water must consecrate the stake).
7. `POUR HOLY WATER ON STAKE` → consecrated silver stake.
8. Descend to The Still Den (Dungeon Lower Tier) → undead werewolf.
9. `DRIVE STAKE INTO WEREWOLF` → werewolf destroyed; reverts to scholar appearance on death.
10. Werewolf drops **Werewolf's Amulet** (ring ritual artifact, The Veil of the Arcane).
11. Take Ivory Torch from wall before leaving.

**Reward:** Werewolf's Amulet → ring ritual artifact for The Veil of the Arcane ritual at Church of All altar. See `ring-rituals.md`.

---

## Quest 20 — Quest Removed From Game

## Quest 21 — Quest Removed From Game

---

## Quest 22 — The Ruined Aqueduct

**Discovery:** Quest Board — posted early, one of the first quests available.
**Prerequisites:** Access to Dungeon Upper Tier.

**Steps:**
1. Find collapsed aqueduct section in Dungeon Upper Tier — gap three rooms wide.
2. Locate stone blocks in collapsed gallery nearby.
3. Carry blocks two at a time to the gap (strength check each transit not to drop).
4. Place all three blocks.
5. Seal joints with mortar from Supply Room → aqueduct restored.

**Reward:** Innkeeper permanently lowers Food & Drink cost by 1 Zenni.
**Cascade:** Town Square fountain begins running → water required for Quest 49 (The Ruined Shrine) clay adhesive. Ensures most players complete this naturally before needing the fountain.

---

## Quest 23 — Quest Removed From Game
*(Lighthouse quest — retired. See `locations.md` — Lighthouse.)*

---

## Quest 24 — The Beekeeper's Swarm

**Discovery:** Beekeeper's Cottage (spur off The Old Oak) — beekeeper explains swarm escaped to a hollow tree at the forest edge. Quest Board posting appears when player receives the town charter (Quest 17 reward).
**Prerequisites:** Smoke jar from Supply Room (Dungeon Upper Tier, behind Trap 17).

**Steps:**
1. Get smoke jar from Supply Room (disarm or trigger Trap 17 — smoke jar visible in wreckage either way).
2. Hold smoke jar and walk into swarm room → bees pacified.
3. Take queen (small tagged bee in glass vial near nest).
4. Return queen to beekeeper.

**Reward:** Jar of enchanted honey — consumable, restores 2 hearts.

---

## Quest 25 — The Flooded Cellar

**Discovery:** Innkeeper mentions a locked cellar that flooded years ago and was sealed off.
**Prerequisites:** Crowbar from Dungeon Upper Tier (Prayer Alcove).

**Steps:**
1. Get cellar key from bartender.
2. Enter cellar via cellar door in kitchen.
3. Remove drain cover with crowbar.
4. `CLEAR DRAIN` → clog clears.
5. Cellar drains → reveals pre-flood Zenni cache + door to Secret Tunnel.

**Reward:** Zenni cache. Bartender gives a pair of boots (leg-slot armor, +3 trap disarm roll bonus — *"forgot I had these, should have given them to you BEFORE you cleaned up the cellar"*). Secret Tunnel door permanently accessible (bidirectional).

**Open question:** Perception check on kitchen-side entry before draining — leaning no roll. Resolve later.

---

## Quest 26 — Quest Removed From Game

---

## Quest 27 — The Toll Bridge Operator

**Discovery:** Find the Toll Bridge in the Secret Tunnels. Perception check on bridge reveals faded official seal → public property → quest discovery + May's hint unlocked.
**If player already has charter:** *"You remember something about a bridge in the town charter."*
**Prerequisites:** Town charter (from Quest 17 reward chain). No Quest Board entry.

**May's hint (one tier only):** *"There's something in the town charter about public bridges and rights of way. Might be worth a look."*

**Steps:**
1. Find Toll Bridge — Boggart charges extortionate toll, gives no hints about what would satisfy him.
2. Obtain town charter (via Quest 17 chain).
3. `GIVE CHARTER TO BOGGART` → Boggart reads it, grumbles, vacates. Drops strongbox.
4. Strength check to open strongbox → several turns' worth of Zenni.

**Reward:** Bridge permanently free. Dungeon Entrance accessible.

---

## Quest 28 — The Archivist's Request

**Discovery:** Archivist in town library trying to authenticate an old map — needs a rubbing from a specific dungeon engraving.
**Prerequisites:** Thin paper (vendor, 2 Zenni — destroyed if player gets wet, reappears for sale) + charcoal (Mine Passage, mid-tier, no perception check). No hints from May; no Quest Board posting.

**Steps:**
1. Buy thin paper from vendor (2 Zenni).
2. Find charcoal in Mine Passage (mid-tier).
3. In Inscription Chamber (mid-tier): `RUB PAPER ON ENGRAVING` → produces rubbing.
4. Return rubbing to archivist → earns incantation scroll.
   - Archivist: *"This appears to be an answer to a question I was never able to find."*

**Reward:** Incantation scroll — required for Quest 34 (speaking door in lower tier). Archivist's remark is the only connection to Quest 34.

---

## Quest 29 — Quest Removed From Game

## Quest 30 — *(see Quests 19 & 30 above)*

## Quest 31 — Quest Removed From Game

---

## Quest 32 — The Missing Gravestone

**Discovery:** Finding the Mid-Tier Key Door in the dungeon triggers quest discovery and unlocks May's three-tier hints. Councilman Rowan Finch approaches the player — his grandfather Calder Finch's gravestone was stolen from the cemetery. No Quest Board posting.

**May's hints:**
- Tier 1: *"There's a locked door down in the tunnels, they say. Heavy thing — needs a proper key. Word is someone in town might know something about it."*
- Tier 2: *"The Finch family goes back a long way in Roundabout. Rowan's grandfather was quite the explorer, from what I hear. Rowan works up at the Town Hall if you want to ask him about it."*
- Tier 3: *"Old Calder Finch — now there was an explorer. Spent more time underground than above it. Whatever he knew about that door went with him to the cemetery. Rowan might point you in the right direction."*
- Gravestone hint (one tier only): *"I've heard carts are good for moving heavy things. Stones, for instance."*

**Steps:**
1. Find Mid-Tier Key Door in dungeon upper tier → quest discovered.
2. Talk to Councilman Rowan Finch in Council Chamber (Town Hall).
3. Perception check in the bog → gravestone face-down in mud.
4. Find hand cart in Storage Area (Dungeon Upper Tier).
5. `LOAD STONE ONTO CART` → move gravestone back to cemetery.
6. Return to Rowan Finch.

**Reward interaction:** *"That cart came from the dungeon," Rowan says flatly. "Don't bother denying it — I've seen it before, in my grandfather's papers." He studies you for a moment. "He left a key. Said it led to a lower level — wouldn't say what was down there." He holds it out. "Take it. It was never meant for me."*

**Reward:** Middle Tier Key — opens Mid-Tier Key Door, gates access to key side of mid-tier dungeon.

---

## Quest 33 — Quest Removed From Game

---

## Quest 34 — The Frozen Soldier

**Discovery:** Organic — player finds Tool Alcove (lower tier) and the speaking door, then connects it to archivist's remark from Quest 28.
**Prerequisites:** Incantation scroll (Quest 28 reward) + Ivory Torch (The Still Den, lower tier).

**Steps:**
1. Find Tool Alcove (lower tier, north of The Junction) — perception check reveals speaking door disguised as back wall.
2. Door speaks in unknown language — clearly a question; cannot be understood.
3. `READ SCROLL` (incantation scroll) → door opens; scroll consumed. (*"The wall goes quiet in a way it wasn't quiet before. Then, slowly, it opens. You get the sense it had begun to doubt anyone would ever answer."*)
4. Pass through Quest 34 Mid Room — dark pool wall to wall.
   - Swimming: 1 heart damage, returned to doorway.
   - Solution: `POUR VIAL IN WATER` (vial of glacier melt, Prayer Alcove, upper tier) → pool freezes; player crosses freely.
5. Enter Quest 34 Fountain Room — soldier encased in magical ice.
6. `HOLD TORCH NEAR ICE` (turn 1) → ice begins to thaw.
7. `HOLD TORCH NEAR ICE` (turn 2) → soldier freed.
8. Soldier gives the Forgotten Blade and wanders off.

**Reward:** The Forgotten Blade — ceremonial sword, treasure item (not a combat weapon). Soldier reappears in town as minor NPC offering free weapon training sessions.

---

## Quest 35 — Quest Removed From Game

## Quest 36 — Quest Removed From Game

## Quest 37 — Quest Removed From Game

---

## Quest 38 — The Collapsed Passage

**Discovery:** Organic — player finds the Collapsed Gallery (Dungeon Upper Tier, east branch) blocked by timbers.
**Prerequisites:** Pickaxe (from mine, not dungeon) + support beam (Storage Area, Dungeon Upper Tier).

**Steps:**
1. Find Collapsed Gallery (east branch off Ink Corridor, south of Storage Area).
2. Get pickaxe from mine.
3. Three strength checks — one per main timber. After each success, another loosens.
4. After clearing all three, prop passage with support beam.

**Reward:** Permanent shortcut — passage exits into Rickety Bridge, placing player between Shrine Room and Mid-Tier Key Door, bypassing everything above. Significantly speeds dungeon traversal.

---

## Quest 39 — Quest Removed From Game

---

## Quest 40 — Shamus's Recipe

**Discovery:** Quest Board — posted early, one of the first quests available. Shamus also mentions it wistfully in conversation.
**Prerequisites:** Bog thyme (Bog-SW, perception check) + small clay pot (Supply Room, Dungeon Upper Tier — visible in Trap 17 wreckage).

**Steps:**
1. Find bog thyme via perception check in Bog-SW.
2. Find small clay pot in Supply Room — visible in wreckage of Trap 17 whether triggered or disarmed.
3. Deliver both to Shamus.

**Reward:** Permanent inn menu upgrade — "hearty stew" option, restores 2 hearts at the same price as Food & Drink (2 Zenni).

---

## Quest 41 — The Child's Kite

**Discovery:** Organic — child at The Old Oak with kite tangled in upper branches.
**Prerequisites:** None.

**Steps:**
1. `CLIMB TREE` → retrieves kite; rune stone on a cord falls free.
2. `TAKE RUNE STONE`.
3. `GIVE KITE TO CHILD` → quest complete.

**Reward:** Old Oak rune stone (one of three needed for Quest 42). No perception check required anywhere.

---

## Quest 42 — The Brotherhood Stones

**Discovery:** Ivanaar Stormbringer introduces the quest immediately after the trust trial runed metal handoff (Viking Encampment).
**Prerequisites:** Trust trials complete (Quest 19/30 chain).

**Rune stones:**
- **Bog rune stone:** *A grey stone, heavy for its size, one face worn flat by water. Faint lines are etched across the surface in no pattern you recognize.* Found in Bog-NE (perception check).
- **Dungeon rune stone:** *A pale stone, roughly square, with deep natural veins of darker mineral running through it like old script.* Found in Inscription Chamber, mid-tier (perception check).
- **Old Oak rune stone:** *A small flat stone, dark and smooth, threaded on a cord. Mineral veins run through it in a pattern that looks almost intentional.* Reward from Quest 41.

**Steps:**
1. Collect all three rune stones.
2. Return to Ivanaar at the Viking Encampment — `GIVE STONES TO IVANAAR`.

**Reward:** Ivanaar's Tunic — chest slot armor. Brotherhood weave with restored runes. Grants a damage avoidance roll during combat — a second roll during the combat phase that can negate damage that would otherwise be taken. **Note: include damage avoidance mechanic in combat system design.**

---

## Quest 43 — Quest Removed From Game

## Quest 44 — Quest Removed From Game

## Quest 45 — Quest Removed From Game

## Quest 46 — Quest Removed From Game

## Quest 47 — Quest Removed From Game

## Quest 48 — Quest Removed From Game

---

## Quest 49 — The Ruined Shrine

**Discovery:** Entering Roundabout Forest reveals a crumbled shrine to The Verdant Circle — visible to any player, no perception check required.
**Prerequisites:** Quest 22 (Ruined Aqueduct) must be complete — fountain only runs after aqueduct is repaired.

**Quest flow:** Find shrine → collect three bowl pieces → descend to lower tier for fire clay → return to fountain to mix adhesive → assemble bowl → return to shrine → bowl becomes ring ritual artifact.

**May's hints:**
- Tier 1: *"Something about that shrine bowl needs water — clean, running water. Check the Quest Board; there may be something relevant posted."*
- Tier 2: *"The town fountain hasn't run in years. Word is the aqueduct beneath the dungeon needs repair — it's on the Quest Board if you haven't seen it."*

**Bowl pieces (3):**
1. Near the shrine in Roundabout Forest (perception check — should be easy; set difficulty once perception mechanic is defined)
2. In the bog (perception check — should be easy; set difficulty once perception mechanic is defined)
3. Dungeon Upper Tier — Shrine Room (perception check — should be easy; set difficulty once perception mechanic is defined)

**Steps:**
1. Find shrine (perception check in Roundabout Forest) — quest discovered.
2. Collect all three bowl pieces.
3. Descend to Thermal Vent Room (lower tier) — `LOOK UP` reveals fire clay. `TAKE CLAY`.
4. Return to Town Square fountain (must be flowing — Quest 22 prerequisite). Mix fire clay with fountain water → clay adhesive.
   - If fountain dry: *"The fountain is dry. You'll need clean running water."*
5. Assemble bowl with adhesive.
6. Return to shrine → `PUT BOWL ON PEDESTAL` — shrine does not respond. Text: *"The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills."*
7. `PUT COIN ON PEDESTAL` (or `OFFER COIN`, `DROP COIN`) with any Zenni coin → transformation text fires → bowl becomes The Crystal Bowl (ring ritual artifact).

**Transformation text:** *The coin settles on the pedestal. For a moment, nothing. Then the bowl begins to change — ceramic going pale, then translucent, then clear. The etched design that was barely visible before catches the light now, sharp and permanent. What sits on the pedestal is no longer what you put there.*

**Reward:** The Repaired Bowl → ring ritual artifact for The Verdant Circle ritual at Church of All altar. See `ring-rituals.md`.

---

## Quest 50 — The Lost Apprentice

**Discovery:** Quest Board — Will Passion posts anonymously, describing a missing person last seen heading toward the dungeon. Posted at game start.
**Missability:** The Quest Board posting is removed permanently if the player disarms the Flooding Room trap (Trap 41). Those players never reach the trap side. Quest 50 is fully missable — no impact on the ring quest.

**Prerequisites:** Access to trap side of mid-tier (via Flooding Room sweep — one-way). Shovel.

**Steps:**
1. Be swept through the Flooding Room (Trap 41) → land on Trap Side Entry (mid-tier).
2. Navigate Dream Corridor → Lost Apprentice's Cell.
3. Combat with afflicted apprentice — defeating him breaks the affliction.
4. Apprentice comes around — disoriented, sad. Hole in cell floor is nearly through to surface.
5. `USE SHOVEL` → finishes hole to Bog-NW. Permanent exit created.
6. Apprentice follows player out.
7. As they surface in Bog-NW, apprentice gives his gloves. Quest completes on bog exit — no return to Will required.

**Reward:** Apprentice's Gloves — hands slot, +3 combat roll bonus. Will is visibly shaken when player next visits the tower; says little about it.

---

## Quest 51 — The Back Alley Mugger

**Discovery:** Organic — entering the Back Alley for the first time. Quest Board — May posts a bounty notice after 100 turns if the mugger has not yet been slain.
**Prerequisites:** None.

**Steps:**
1. Enter the Back Alley. Perception check fires on every visit until mugger is spotted.
   - Failed check: mugged — 1 heart damage, 2–3 Zenni stolen (nothing taken if broke). Player loses consciousness, wakes in the Back Alley one turn later.
2. Successful perception check: mugger is visible — fight to the death.
   - Losing: wake with 1 heart remaining; text nudges toward the inn.
   - Winning: mugger slain permanently. Back Alley is safe. Lockpicks drop as loot.
3. Collect reward from May at the tavern bar.

**Reward:** One free drink from May (1 heart restoration). May flag clears after use.
**Loot:** Lockpicks — opens the large iron chest in Mine Passage (20 Zenni). Not a general trap disarm tool.

---

## Quest Board Cascade

**Confirmed postings:**
- Quest 22 (The Ruined Aqueduct) — posted early, ensures most players complete before needing fountain
- Quest 40 (Shamus's Recipe) — posted early
- Quest 7 (The Bone Flute) — posted 20 turns after player first meets Pyronicus
- Quest 17 (The Frozen Watch) — posted by Records Room Worker when player delivers ring to Will (second briefing)
- Quest 24 (The Beekeeper's Swarm) — posted when player receives town charter (Quest 17 reward)
- Quest 50 (The Lost Apprentice) — posted anonymously by Will at game start; removed if Flooding Room trap disarmed
- Quest 51 (The Back Alley Mugger) — posted by May after 100 turns if mugger not yet slain; also discoverable organically

**Confirmed non-Board quests:**
- Quest 12 (discovered via `LOOK AT MUSIC BOX`)
- Quest 27 (discovered via Toll Bridge perception check)
- Quest 28 (discovered via archivist in library)
- Quest 32 (discovered via Mid-Tier Key Door)
- Quest 34 (discovered via Tool Alcove / speaking door)
- Quest 38 (discovered via Collapsed Gallery)
- Quest 41 (discovered organically at The Old Oak)

