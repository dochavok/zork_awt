# Enchanted Realms: One Ring — Mechanics

Authoritative reference for all confirmed game mechanics and systems. Brainstorm ideas (mechanic ideas.md, mechanic ideas vol2.md) are separate — nothing here is tentative.
Update this file immediately when any mechanic is confirmed or changed.

---

## Core Systems

### Classes

Players choose one of three classes at the start of the game. Class selection is permanent.

| Class | Starting Hearts | Starting Skill | Challenge Roll Bonus |
|-------|----------------|----------------|----------------------|
| Warrior | 6 | Weapon use | Strength checks |
| Mage | 4 | Spell casting | Perception checks |
| Rogue | 5 | Bow use | Perception, Trap Disarm & Fishing checks |

Each class can acquire the other classes' skills through training and quests.

---

### Hearts & Health

- Players have hearts modified by class (see above).
- Restored only at the inn (full heal) or by purchasing food and drink (1 heart).
- The inn is the only healing location in the game.
- Heart Necklace (quest reward) permanently adds one heart — equips in neck slot.

---

### Zenni (Currency)

Found in the world, in chests, or rewarded by Dungeon Masters. No Zenni cap. Spent on: inn rest, food and drink, skill training, vendor items, and hints.

**Economy baseline:**
| Item | Cost |
|------|------|
| Food & Drink (1 heart) | 2 Zenni |
| Hearty Stew (2 hearts) | 2 Zenni — unlocked after Quest 40 |
| Inn Rest (full heal) | 5 Zenni |
| Weapon training | 3 Zenni |
| Archery training | 3 Zenni |
| Spell training (Will) | 3 Zenni |
| Gunpowder | 5 Zenni |
| Fishing Rod | 8 Zenni |
| Tip Journal | 5 Zenni |
| Thin paper | 2 Zenni |

**Zenni sources:**
- Will Passion opening gift: 10 Zenni
- Hidden room Zenni: 18 rooms randomized per new game; 9 Easy / 5 Medium / 1 Hard pay 1–3 Zenni each; 3 Very Hard pay 5 Zenni each (~36 Zenni total if all found); Actually Enchanted Glasses pass all checks and find all rooms automatically
- Desert Island buried chest: 30 Zenni
- Vendor buyback: half price, own items only; no buyback for treasure
- Quest rewards: TBD per quest

---

### XP & Leveling

- XP earned through combat, quests, and discovering new locations.
- Leveling is instant when XP threshold is met.
- Level cap: 8. Full XP thresholds and dice progression in `experience.md`.
- Leveling improves dice rolls for both combat and challenge checks.

---

### Dice & Roll System

All checks are dice-based and hidden from the player. Players see outcomes only, never numbers.

**Roll types:**
- **Perception** — finding hidden things, noticing details, spotting traps. Class bonus: Mages and Rogues.
- **Strength** — forcing doors, breaking locks, prying, physical feats (arm wrestling, rope snare escape, portcullis lift, timber clearing, Boggart strongbox, magnetic chest recovery). Class bonus: Warriors.
- **Agility** — dodging hazards (Archery Range arrow dodge before Viking trust earned). No class bonus.
- **Trap disarm** — disabling a detected trap without triggering it. Class bonus: Rogues.
- **Fishing** — `FISH` at Roundabout Pond; success retrieves the bottle (Quest 12). Class bonus: Rogues.

**Perception mechanic:**

All perception checks are fully invisible to the player. The roll fires silently on every qualifying visit. The player sees only outcomes — they find the thing, or they don't. No indication a check occurred, no failure message.

- **Repeating checks** fire every visit until the thing is found (bog items, ship hold treasure map, back alley mugger, Dankhaus path). Once found, permanently visible.
- **One-time checks** fire once per visit to a room (Tool Alcove, Prayer Alcove). Player must return for another attempt — pull-back mechanics handle motivation for critical-path rooms.
- **Second Glance (Level 5 ability):** On any failed perception check, the roll automatically fires a second time. Invisible — the player never knows it happened. They simply find things more reliably after Level 5.
- **Enchanted Glasses:** Small bonus to all perception rolls. **Actually Enchanted Glasses:** Pass all perception checks automatically — no roll required.
- **Class bonuses:** Mages and Rogues receive an inherent bonus to perception rolls. Applied silently to every check.

**Difficulty tiers:**

Target numbers are absolute — a higher-level player beats the same check more reliably as their dice pool grows.

| Tier | Target | Usage |
|------|--------|-------|
| Easy | 5 | Critical path items, early overworld, quest breadcrumbs |
| Medium | 9 | Optional items, repeating checks, moderate consequence traps |
| Hard | 14 | Well-hidden traps, significant consequences, critical path with pull-back |
| Very Hard | 18 | Most subtle tells, severe consequences (ink trap), intentionally punishing |

Perception check locations and difficulty ratings are annotated inline in `locations.md`.

**Damage types** (tracked for future use — no current mechanical effect):
| Type | Source |
|------|--------|
| Physical | Combat (all enemies), mugger, bee swarm (Swarm Tree), errant arrow (Archery Range), Bone Crunch Floor (Trap 36), Skeleton Room (instant death) |
| Smoke | Trap 17 (Supply Room clay pot) |
| Lightning | Trap 19 (Electrified Portcullis) |
| Arcane | Quest 34 Mid Room pool (magical dark water) |
| Poison | Gradual drain over turns — no confirmed source yet |
| Fire | Heat and flame — no confirmed source yet |
| Fall | Drops and pits — no confirmed source yet |
| Water | Drowning (Flooded Cellar before drain — instant death fail state) |

**Class bonuses by roll type:**
- Warriors: Strength checks
- Mages: Perception checks
- Rogues: Perception, Trap Disarm, and Fishing checks

---

### Combat

Dice-based, scales with player level. Warriors start proficient with melee; Rogues with bows; Mages with spells. Cross-class skills acquirable via trainers and quests.

**Round structure:** Turn-based. Player issues an attack command each round (`KILL X WITH SWORD`, `SHOOT X WITH BOW`, `CAST FIREBALL AT X`). Player and enemy roll simultaneously. Higher roll wins the right to deal damage — 1 heart per hit. On a tie, both deal 1 heart damage simultaneously.

**Fleeing:** Player may flee by leaving the room. Enemy resets to full hearts.

**Bow — first round bonus:** +5 to the attack roll on the opening bow attack of any combat. No bonus on subsequent rounds.

**Fireball:** Guaranteed 1 heart damage — no roll required. 10-turn reuse timer. Effectively once per combat encounter.

**Confirmed enemy stats:**

| Enemy | Location | Attack Level | Dice | Hearts | Notes |
|-------|----------|-------------|------|--------|-------|
| Back Alley Mugger | The Back Alley | 1 | 1d6 | 2 | Early game; winnable at Level 1 but not trivial |
| Aylora | The Fire Pit, Viking Encampment | 2 | 2d6 | 3 | Strength challenge, best of five rounds; retryable |
| Afflicted Apprentice | Lost Apprentice's Cell, mid-tier trap side | 3 | 2d8 | 3 | Missable; player may arrive at low level via Flooding Room |
| The Warden | Combat Room, Dungeon Upper Tier | 4 | 2d10 | 5 | One-time fight; monstrous, former dungeon guardian |
| Undead Werewolf | The Still Den, Dungeon Lower Tier | 5 | 3d10 | — | Cannot be harmed by conventional weapons; stake kill only — see Undead Werewolf Chain |

---

### Skill Progression

Each class starts with one combat skill. The other two can be acquired through quests. Skills learned this way are permanent.

**Cross-class skill matrix:**

| Skill | Warrior | Mage | Rogue |
|-------|---------|------|-------|
| Melee weapon | Starts with | Quest 54 — Fight the Knight | Quest 54 — Fight the Knight |
| Bow / Archery | Quest 55 — The Archer's Trial | Quest 55 — The Archer's Trial | Starts with |
| Spell casting | Quest 56 — Will's Teaching | Starts with | Quest 56 — Will's Teaching |

**Weapon training (Quest 54)** — The Redcrosse Knight: Knight of Faith, Roundabout Town Square. Trial by combat — full fight to 1 heart remaining; he stops just before the killing blow. He yields if the player wins; sends them away to train more if they lose. Minimum Level 3 to attempt. Cost: 3 Zenni. Classes: Mage, Rogue only.

**Archery training (Quest 55)** — Raznak (Viking), Archery Range. Requires all three Viking trust trials complete (Quest 57) first. Arrow hazard on range is silently disabled once trust earned. Rogues start with bow — not beckoned by Raznak and cannot trigger this quest. Cost: 3 Zenni. Classes: Warrior, Mage only.

**Spell training (Quest 56)** — Will Passion, Wizard Tower. Warriors and Rogues cannot read spell scrolls directly — resistance message points them to Will. Bring any spell scroll; Will teaches it aloud; scroll consumed, spell learned permanently. Repeatable for each new scroll. Cost: 3 Zenni per spell. Cannot wear Enchanted Glasses in Will's presence during teaching. Classes: Warrior, Rogue only.

---

### Armor Slots

- Head
- Chest
- Legs
- Hands
- Neck *(Heart Necklace)*
- Ring *(The One Ring)*

Armor is found through exploration and never degrades.

**Armor audit (complete):**
| Slot | Item |
|------|------|
| Head | Enchanted Glasses / Actually Enchanted Glasses |
| Chest | Ivanaar's Tunic (Quest 42 reward) |
| Legs | Boots (Quest 25 reward) |
| Hands | Apprentice's Gloves (Quest 50 reward) |
| Neck | Heart Necklace (Lynds arm wrestling) |
| Ring | The One Ring |

**Ivanaar's Tunic — damage avoidance:**
When the enemy wins a combat round and would deal 1 heart damage, the tunic fires a silent 1d10 roll. Result of 7–10 (40%) negates the damage entirely. Fixed — does not scale with player level. The roll is completely hidden; no message indicates it occurred. On a successful avoidance, one of four flavor messages fires at random instead of taking damage:

1. *The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.*
2. *For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.*
3. *The runes along the collar catch the light briefly. You are less hurt than you expected to be.*
4. *Something in the weave absorbed it. You felt the impact — and then didn't.*

---

## The One Ring

- Grants invisibility while worn.
- Corruption timer advances each turn worn. Pauses on removal; resumes on re-equip. Never resets.
- **Total ticks to full corruption: 50.**
- Altar use at Church of All does NOT tick corruption — the ring is being used for its purpose, not personal gain.
- 2–3 quests require or significantly benefit from invisibility (confirmed: Chuckle House; TBD: 1–2 more).

**Corruption milestones:**

| Tick | Event |
|------|-------|
| 10 | First warning |
| 25 | Midpoint warning |
| 40 | Urgent warning |
| 41–49 | Challenge roll window — removal requires passing a roll; difficulty escalates each tick |
| 50 | Full corruption — game over (failure ending), no roll offered |

**Milestone messages:**

- **Tick 10:** *The ring is warm. You hadn't noticed until just now. You're not sure when it started.*
- **Tick 25:** *The ring is heavier than it was. Not in weight — in presence. It knows you're wearing it. You find yourself aware of it in a way you weren't before.*
- **Tick 40:** *The ring is harder to ignore than it was. You are aware of it the way you're aware of a sound that hasn't stopped. You should take it off. You know you should take it off.*

**Late-stage removal (ticks 41–49):** Every attempt to remove the ring requires passing a challenge roll. Uses the player's current level dice only — no bonus applied. Higher-level players roll better dice and succeed more reliably. Difficulty increases by 2 each tick:

| Tick | Target |
|------|--------|
| 41 | 5 |
| 42 | 7 |
| 43 | 9 |
| 44 | 11 |
| 45 | 13 |
| 46 | 15 |
| 47 | 17 |
| 48 | 19 |
| 49 | 21 |

**Removal outcome messages:**
- **Clean success:** *You remove the ring. Whatever it wants, it didn't get it this time.*
- **Near-miss success:** *The ring comes off. It didn't want to. You're not sure you could have held out another moment.*
- **Failure:** *You try to take the ring off. Your fingers find it. They don't do what you ask.*

**Game over message (tick 50):** *You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.*

**Corruption is sacred:** Ring corruption must never be reduced, slowed, or mitigated by any mechanic, item, or quest reward. This is a hard design constraint.

---

### Enchanted Glasses

Two versions:
- **Enchanted Glasses:** Small bonus to perception checks.
- **Actually Enchanted Glasses:** Pass all perception checks automatically — no roll required.

Upgrade path: equip glasses (head slot) before reaching Kevry Talborn's island (69 squares east in Open Ocean) → Kevry enchants them.

Warning: equipping outside Will's Bedroom triggers instant fail state. Equipping inside permitted.

End-game return: dropping in Will's Bedroom earns XP (double if Actually Enchanted).

---

## Spell Mechanics

Spells learned permanently once acquired.

**Reuse timers:** Number of turns before spell can be cast again. Starts when cast — independent of duration.

**Duration:** Number of turns effect lasts. Independent of reuse timer.

**Two light sources** (any combo of torch and/or Light spell) function the same as one — no stacking bonus, just redundancy.

**Spell scrolls vs. use-item scrolls:** Spell scrolls teach a spell permanently (Light, Unbind Undead, Fireball). Use-item scrolls are consumed on use without teaching anything (incantation scroll — Quest 28/34 speaking door). The resistance mechanic below applies to spell scrolls only; use-item scrolls work for all classes.

**Warrior/Rogue scroll resistance:** `READ SCROLL` on a spell scroll returns:

*"The words are legible. The meaning is not. Whatever is written here was meant for someone with a different kind of mind — or a different kind of training. Will Passion, in his tower, has been known to translate this sort of thing for people like you."*

Scroll is not consumed. Player retains it. Bringing the scroll to Will Passion in the Wizard Tower triggers the teaching interaction via either `READ SCROLL` (in his presence) or `GIVE SCROLL TO WILL` — Will takes it, reads it aloud, scroll consumed, spell learned permanently.

| Spell | Effect | Duration | Reuse Timer | Source |
|-------|--------|----------|-------------|--------|
| Light | Creates light source | 10 turns | 20 turns | Quest 12 — music box key in Bog-NW |
| Unbind Undead | Releases a bound spirit | Instant | 20 turns | Lighthouse — scroll on Silas Bryne's desk |
| REST | Recovers 1 heart | Instant | 50 turns | Granted at Level 6 — no scroll required, no XP awarded |
| Fireball | Guaranteed 1 heart damage — no roll required | Instant | 10 turns | Quest 7 reward — Pyronicus |

**REST notes:** Outside combat only — hostile in room returns *"You can't rest now, there's fighting to be done!"* Before reuse timer expires returns *"What are you sitting around for, there's a dungeon to explore!"* Works while inked. Stacks with inn healing and food.

**Standard level-up message (all levels):** *"You hear music — a familiar melody. You have reached level [#]!"*

**Level-up message on acquiring REST (Level 6 only):** Fires after the standard level-up message. *"You feel a deeper sense of calm settle over you — the kind that comes with hard-won experience. You can now REST to recover when the fighting stops."*

**Nobu's Favor (Level 7) and Finishing Move (Level 8):** No additional message. Secret abilities are never announced.

---

## Finishing Move

Granted silently at Level 8. The player is never told this ability exists — no level-up message, no journal entry, nothing.

**Trigger:** All 3d20 roll 15 or higher in a single combat roll (~2.7% chance per roll).

**Effect:** Instant kill. The enemy is defeated immediately regardless of remaining health.

**Narrative (shown to player on trigger):**

*"Finish him."*
*The voice is not yours. It doesn't need to be.*
*You already knew how this was going to end. The voice just said it out loud.*
*Your body is already moving.*

**Design notes:**
- The voice has no source and no attribution. It is never explained.
- The ability is intentionally invisible — players who trigger it will wonder; players who never trigger it will never know it existed.
- No exemptions — by Level 8 all named/ritual fights are expected to be complete.

---

## Nobu's Favor

Granted silently at Level 7. The player is never told this ability exists — no level-up message, no journal entry, nothing. It simply fires when needed.

**Trigger:** Player is reduced to 0 hearts.

**Effect:** Survives on 1 heart. Transported instantly to the Tale and Ale Main Room. Once per game — does not reset.

**Narrative (shown to player on trigger):**

*The world goes dark. Not the dungeon dark — something older than that. Quieter.*

*You are somewhere else.*

*A voice, close and unhurried, as if it has all the time there is: "But did you die?"*

*The Main Room of the Tale and Ale materializes around you. The fire is going. Someone left a drink on the table. The chair nearest the hearth looks like it was made for exactly this moment.*

*You are alive. You are not sure how. You are quite sure you could use a rest.*

**Design notes:**
- Nobu is not an NPC. The name appears nowhere else in the game. The voice is never explained.
- The ability is intentionally invisible — players who trigger it will wonder; players who never trigger it will never know it existed.
- After firing, subsequent reduction to 0 hearts is permanent death as normal.

---

## Hint System (May)

May sells hints for Zenni at The Bar, Tale and Ale. Hints are tiered — each tier costs more than the last. Tiers must be purchased in order.

**Tier cost ranges** (TBD exact values — review against final economy):
- Tier 1: 1–3 Zenni
- Tier 2: 4–6 Zenni
- Tier 3: 7–12 Zenni

Some hints are conditional: May's tier 1 hint for Quests 19&30 fires only if player has not yet examined the statue. Post-visit Chuckle House hints unlock once player has entered the Chuckle House.

**May's responses by tip amount:**
- **Tier 1 (1–3 Zenni):** *May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.*
- **Tier 2 (4–6 Zenni):** *May pockets the coins carefully. "That buys you something worth hearing," she says.*
- **Tier 3 (7–12 Zenni):** *May counts the coins once, pockets them, and leans all the way across the bar.*
- **Nothing to share (any amount, no hints remaining):** Randomly selected from:
  1. *May pushes the Zenni back. "Keep it. I've got nothing worth that right now." She goes back to wiping the bar.*
  2. *May looks at the coin and shakes her head slowly. "I'd be robbing you. Ask me again when something changes."*
  3. *May sets the Zenni on the bar and slides it back. "Nothing in here worth selling today," she says, tapping her temple.*
- **Over 12 Zenni:** *May looks genuinely uncomfortable. "I appreciate the thought, but no." She slides it all back. "Ask me something and we'll talk."*

May only offers hints for quests that are discovered AND incomplete. She won't hint on undiscovered or finished quests. Each tier for each quest is a one-time purchase — May will not re-sell a tier already bought.

**Free drink flag system:** A boolean flag tracks pending free drinks, each with a reason string for contextual dialogue. Flag is set by quest events; cleared after the free drink is redeemed. Current known flags:
1. **Mugger slain** — *May thanks the player for dealing with whoever was lurking in the Back Alley, and doesn't charge for the drink.*

**Raznak nudge (free, no Zenni):** If the player has visited the Archery Range at least once but has never spoken to Raznak (not yet reached any dialogue state), May offers unprompted: *"You should talk to Raznak."* Fires once only. No tier, no cost.

---

## Tip Journal

Purchasable from Shamus (Tale and Ale Kitchen) for 5 Zenni. Available to the player on request at any time.

Records:
- Quests discovered and their discovery source (May, Quest Board, or organic)
- Hints purchased per tier per quest
- Quest completion status

A quest does not appear in the journal until it has been discovered — undiscovered quests are invisible to the player.

Display verb (`READ JOURNAL`? `OPEN JOURNAL`?), visual format of quest entries, and completed quest handling TBD — see `todo.md`.

---

## Quest Board

Located in The Bar of the Tale and Ale. Described in the room text. `LOOK AT BOARD` displays all currently posted quests. Completed quests are automatically removed from the board.

**Confirmed postings (cascade order):**
- Quest 22 (The Ruined Aqueduct) — posted early, ensures most players complete before needing fountain
- Quest 40 (Shamus's Recipe) — posted early
- Quest 7 (The Bone Flute) — posted 20 turns after player first meets Pyronicus
- Quest 17 (The Frozen Watch) — posted by Records Room Worker when player delivers ring to Will (second briefing)
- Quest 24 (The Beekeeper's Swarm) — posted when player receives town charter (Quest 17 reward)
- Quest 50 (The Lost Apprentice) — posted anonymously by Will at game start; removed if Flooding Room trap disarmed
- Quest 51 (The Back Alley Mugger) — posted by May after 100 turns if mugger not yet slain; also discoverable organically

**Non-Board quests (discovered organically or via NPC):**
- Quest 12 (discovered via `LOOK AT MUSIC BOX`)
- Quest 27 (discovered via Toll Bridge perception check)
- Quest 28 (discovered via archivist in library)
- Quest 32 (discovered via Mid-Tier Key Door)
- Quest 34 (discovered via Tool Alcove / speaking door)
- Quest 38 (discovered via Collapsed Gallery)
- Quest 41 (discovered organically at The Old Oak)

Full cascade design — which quests unlock new postings — TBD. See `todo.md`.

---

## Shovel & Dig Mechanic

One shovel in the world. Three confirmed uses:
1. Stored Room (mid-tier dungeon) → Hole to Below
2. Desert Island buried chest
3. Quest 50 — finish hole from Lost Apprentice's Cell to Bog-NW

The Werewolf's Amulet (Veil of the Arcane ring ritual artifact) is dropped by the undead werewolf on defeat — not found via dig.

**Will Passion audio note:** 1-in-20 random chance on any `DIG` command (all three dig locations equally, no cooldown):

*Will Passion materializes in your thoughts, uninvited. "Do you know how long it takes to dig a six-foot hole?" You suspect he does. You suspect he has timed it.*

Implemented as a post-dig random check on any successful DIG command.

Beach `DIG`: succeeds up to 5 times with flavor text (nothing but wet sand); 6th attempt: "The beach is littered with holes. There's nowhere else to dig." Each `DIG` counts as a turn.

---

## Zenni Rooms

18 rooms across the world contain hidden Zenni, discoverable via silent perception check. Rooms are selected randomly at game initialization and fixed for that playthrough. Actually Enchanted Glasses pass all perception checks — all 18 rooms found automatically.

**Difficulty distribution (assigned at game init):**
| Tier | Count | Target | Zenni |
|------|-------|--------|-------|
| Easy | 9 | 5 | 1–3 |
| Medium | 5 | 9 | 1–3 |
| Hard | 1 | 14 | 1–3 |
| Very Hard | 3 | 18 | 5 |

**Eligible room pool:**

*Overworld & Town:*
White House, Will's Wizard Tower (Main Room), Will's Bedroom, Main West, Town Square, Main East, The Alley, Back Alley, Town Hall Exterior, Council Chamber, Records Room, Upper Hall, The Tower, Tale & Ale Main Room, Bar, Ty's Casino Corner, Pipe Room, Kitchen, Upstairs Hall, Guest Rooms 1/2/3, Cellar/Storeroom, Library Main Hall, The Stacks, Church Nave, The Altar, Keeper's Chamber, Graveyard, The Mausoleum, The Crypt, Roundabout Wasteland, The Volcano, Pyronicus's Forge, Archery Range, Viking Encampment, Haalvar's Hut, Ritual Circle, Fire Pit, Roundabout Pond, Dankhaus rooms, Beach Road, The Old Oak, Beekeeper's Cottage, Swarm Tree, Roundabout Forest, Roundabout Beach, The Lighthouse, The Docks, Pie Rat Ship Deck

*Dungeon — Upper Tier:*
Ink Corridor, Supply Room, Narrow Passageway, Idol Room, Storage Area, Collapsed Gallery, Creature Den, Combat Room, Prayer Alcove, Portcullis Corridor, Shrine Room, Mid-Tier Key Door

*Dungeon — Mid Tier:*
Key Door Landing, Stored Room, Inscription Chamber, Cave Creature's Lair, Echo Alcove, Magnetic Vault, Deep Lock Door, Trap Side Entry and Trap Side rooms (5)

*Dungeon — Lower Tier:*
Lower Crypt, The Encampment, Thermal Vent Room, The Junction, The Narrow Pass, The Still Den, Tool Alcove, Quest 34 Mid Room, Quest 34 Fountain Room, Spirit Room, Burial Chamber

**Excluded rooms (not eligible):**
All four Bog rooms, all Sea / Open Ocean squares, Desert Island, Kevry's Island, Pie Rat Ship Hold, Flooding Room, Dream Corridor, Dark Room, Hole to Below / Pile of Rubble, Rickety Bridge, all Chuckle House rooms (Entrance, Rejection Mirror, Shatter Trap Mirror, Ghost's Room), Mine Passage, The Crevice (has dedicated treasure — gold pocket watch), Skeleton Room (instant death on entry)

---

## Hidden Connections (Phase 2 Only)

Certain passages or connections between rooms are hidden and require a perception check to discover. Once discovered, they are permanently visible for that playthrough. Global rule — applies to any hidden connection anywhere in the world.

---

## Special Mechanics

### The Chuckle House Mirrors

All mirrors in the Chuckle House repel visible players — stepping in front of one while visible sends the player back to the room they came from. Passing while invisible (ring worn) proceeds normally. Mirror mechanic ends throughout the building once the ghost is freed via Unbind Undead.

**Ghost's Room exit mechanic:** 50% chance each attempt to leave fails — player returned with a disorientation message. Permanent — does not end when ghost is freed.

---

### The Stored Room / Hole to Below

Two-state room in the dungeon mid-tier.

**Before digging:** *The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.*

One `DIG` (shovel required) collapses floor permanently → Hole to Below. Spur east (The Crevice) buried permanently and inaccessible.

**After digging:** *Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.*

Beam exposed by collapse. `TIE ROPE TO BEAM` (rope from Docks, one item in world) enables bidirectional travel: `DOWN`, `UP`, `CLIMB DOWN ROPE`, `CLIMB UP ROPE`.

---

### The Dream Corridor

Liminal branching passage between Trap Side Entry and Lost Apprentice's Cell (mid-tier trap side). Player does not know they are in a dream until they successfully pass through. On failure, room resets and replays — identical every time. No damage, no cost. Just the loop.

**Structure:** 2×3×2 — three levels of decision yielding 12 outcomes. 6 successes, 6 failures.

**Level A — Choose a sense to follow:**
- Hear (follow sound)
- Smell (follow smell)
- See (look for a way)
- Feel (follow instinct)

**Level B — Act on that sense:**
Each sense branches into 2 or 3 actions, each leading to Success or Failure.

Full tree (paths numbered A1–A3, B1–B3):

**A1 — See (Follow path):** The footprints. Your size. Your stride.
- Option 1 — Follow them: *SUCCESS* — they lead out.
- Option 2 — Wait: *FAILURE* — footprints fade; loop restarts.

**A2 — Hear (Follow path):** Narrow passage, sound of moving water below.
- Option 1 — Follow slope down toward sound: *SUCCESS*
- Option 2 — Follow draft, go toward air: *FAILURE* — passage opens onto nothing; drop.

**A3 — Smell (Follow path):** Smell gets stronger at a low alcove.
- Option 1 — Crouch inside and look for source: *FAILURE* — torch goes out.
- Option 2 — Ignore it, keep moving forward: *SUCCESS*

**B1 — Feel (Go another way):** Certainty leads to a blank section of wall.
- Option 1 — Trust it; press forward into wall: *SUCCESS*
- Option 2 — Trust it; wait and see: *FAILURE* — certainty becomes doubt.

**B2 — See (Go another way):** Claw marks run the length of the tunnel. Something shifts at the far end.
- Option 1 — Keep walking: *SUCCESS*
- Option 2 — Fall back: *FAILURE*

**B3 — Feel (Go another way):** Vibration strongest at a discolored circle of floor.
- Option 1 — Step onto discolored stone: *SUCCESS*
- Option 2 — Kneel and press hand to it: *SUCCESS* (both options succeed)

**Full prose text:**

**Inciting event (repeats on every failure):**
*The corridor is low and wet. Water drips somewhere behind you. Your torch throws just enough light to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.*

**Level 1 — Instinct vs. Caution:**
- A — Follow them
- B — Go another way

**Level 2A — Follow path:**
*The prints lead forward. You know this feeling — the particular shape of a place you've already moved through. You have been here. You just don't remember when.*

- **A1 — See:** *The footprints change. Halfway down the corridor they shift — your stride lengthens, the toe digs deeper. Whatever you were walking toward, you were walking faster by the time you reached it. You follow the change.*
- **A2 — Hear:** *A sound comes from your left — a passage you didn't notice before, or didn't exist before. Water moving. Not dripping. Flowing. Like something is draining toward an opening.*
- **A3 — Smell:** *It stops you mid-step. Something warm. Cooked. Completely wrong for a place like this — bread, maybe, or stew. Coming from ahead, faint but real, the kind of smell that makes your body move before your mind does.*

**Level 2B — Go another way:**
*You step off the prints. The corridor looks different from here — longer, maybe, or the walls are closer. Nothing you can point to. Just the feeling that the version of this place you're now standing in is not the one you entered.*

- **B1 — Feel:** *Something pulls at you — not physical, not quite. A certainty about one direction that has no evidence behind it. The kind of knowing that lives below thought. You trust it, or you don't.*
- **B2 — See:** *Your torch catches the wall of a side tunnel you hadn't noticed — or that wasn't there before. Claw marks run along the stone at shoulder height. Deep, parallel, dragged fast. Whatever made them was large. Whatever made them went that way. You follow anyway.*
- **B3 — Feel:** *The ground hums. Low, slow, rhythmic. Like something heavy moving far below, or far ahead — it's impossible to tell. Your boots feel it more than you do. You follow the vibration.*

**Level 3 — Outcomes:**

*A1 — The footprints end at a wall. Not a door — a wall. But the mud at the base is disturbed, smeared, like something passed through it. The torch flickers.*
- Press hand against wall → FAILURE: *Cold stone. Solid. You press harder, run your fingers along the seam where the smear meets the surface. Nothing gives. It is definitively, completely a wall. You press your forehead against it. You wake up at the entrance. The footprints are there. Your size. Your stride.*
- Step back and look at the full wall → FAILURE: *Distance doesn't help. It's a wall. Flat, unbroken, mortared tight. Whatever the smear in the mud means, it doesn't mean a door. You stand there long enough to be certain. You wake up at the entrance. The footprints are there. Your size. Your stride.*

*A2 — You turn left. The passage is narrow — barely a shoulder's width. The sound of moving water is clearer now, ahead and below. The passage slopes down. Your torch bends in a draft coming up from somewhere beneath you.*
- Follow slope down toward sound → SUCCESS: *The slope levels. The passage opens. The sound of water is all around you now — a drain somewhere below the floor, pulling the flood somewhere useful. The air is damp but moving. Ahead, a doorway. You walk through it. You are through.*
- Follow draft — go toward air, not water → FAILURE: *The draft gets stronger. The passage narrows further and then opens without warning — onto nothing. A drop. You can't see the bottom. The torch goes with you. You wake up at the entrance. The footprints are there. Your size. Your stride. Your heart is going very fast and you're not entirely sure why.*

*A3 — The smell gets stronger as you move. At the end of the corridor a low alcove opens to the right — just wide enough to crouch into. Inside: nothing. No food, no fire, no source. The smell is overwhelming in here. Your stomach responds before your brain does.*
- Crouch inside and look for the source → FAILURE: *The alcove goes back further than it looked. You crouch deeper, torch first. The smell is everywhere and the source is nowhere. The ceiling gets lower. You keep looking. The torch goes out. You wake up at the entrance. The footprints are there. Your size. Your stride. You are not hungry anymore.*
- Ignore it and keep moving forward → SUCCESS: *You keep walking. The smell fades behind you the way smells do when you stop chasing them. The corridor ends at a doorway. You don't remember the corridor having a doorway. You walk through it. You are through.*

*B1 — The certainty leads you to a section of wall that looks identical to every other section of wall. No seam, no mark, no reason. The feeling is loudest here. Your torch doesn't flicker. The wall doesn't breathe. It just is — and something in you insists this is the place.*
- Trust it. Press forward into the wall → SUCCESS: *You don't slow down. You don't brace. You walk into it the way you'd walk through a doorway you've used a thousand times. The wall is not there. The room beyond is. You are through it before you've decided what just happened. You are through.*
- Trust it. Wait. See if something happens → FAILURE: *You wait. The certainty doesn't grow or fade — it just sits there, patient, offering nothing new. The corridor is very quiet. You wait longer. The torch burns. Nothing happens. The feeling eventually becomes indistinguishable from doubt. You wake up at the entrance. The footprints are there. Your size. Your stride. The certainty is gone.*

*B2 — The claw marks run the length of the tunnel, shoulder height, deep and continuous. You follow them. The tunnel is long enough that the entrance is behind you and the far end is still ahead. The marks don't stop or change. They just keep going. Then the tunnel goes silent in a way it wasn't silent before. One breath of stillness. Then something at the far end shifts. Not loud. Not close. Just present. Aware, maybe. The marks continue toward it.*
- Keep walking → SUCCESS: *You don't slow down. Whatever is ahead has already heard you — stopping won't help and going back won't either. You walk toward the sound. The tunnel ends at a doorway. Nothing is there. Nothing was ever there, or it's somewhere you're not anymore. You walk through it. You are through.*
- Fall back → FAILURE: *You take one step back. Then another. The sound doesn't repeat but the silence that follows it is worse. You turn and move fast, faster, back toward the entrance, back toward the footprints, back toward something that made sense. You wake up at the entrance. The footprints are there. Your size. Your stride. The far end of the tunnel is very far away now.*

*B3 — The vibration leads you to a section of floor where it is strongest — a rough circle of stone, slightly discolored, slightly lower than the surrounding floor. The hum comes up through your boots and into your legs. It is steady. It is patient. It has been doing this for a long time.*
- Step onto the discolored stone → SUCCESS: *The hum rises through you the moment your full weight is on it — up through your legs, your chest, your jaw. The floor doesn't move. You do. The corridor shifts around you, or you shift through it, and then you are somewhere else. The hum is gone. The room ahead is quiet and real. You are through.*
- Kneel and press your hand to it → SUCCESS: *The vibration is different through your palm than through your boots — more specific, like a word you almost recognize. You press harder. The circle of stone depresses slightly, just enough to feel deliberate, and something in the corridor unlocks without a sound. A doorway is there that wasn't before. You stand up and walk through it. You are through.*

**On passing through:** The player arrives in the Lost Apprentice's Cell. No explanation is given for what the corridor was. The dream framing is never named in-game.

---

### The Treasure Map

Hidden aboard the Pie Rat Ship in the hold.

Each turn aboard fires a silent perception check. On success: map found and added to inventory. Actually Enchanted Glasses pass all checks — map found on first turn.

Without the map: each `DIG` on Desert Island has a 10% chance of finding the buried chest. Player can keep trying indefinitely.

Carrying the map guarantees `DIG` success on Desert Island on first attempt.

---

### The Pie Rat Ship Heist

Multi-step quest chain that grants access to the Pie Rat Ship.

1. Find Pie Rat disguise in The Rat's Nest (mine).
2. Buy gunpowder from Shamus (5 Zenni).
3. Take a torch from mine sconces — 40-turn burnout timer starts immediately. Take last — grabbing it early wastes it.
4. `DROP GUNPOWDER` at structural weak point in mine (perception check to locate).
5. `LIGHT GUNPOWDER` — fuse catches; narrative implies leave immediately.
6. Exit mine before explosion. Failure = death/fail state.
7. Explosion — cave-in seals main mine entrance permanently.
8. Steal the ship while Pie Rats respond to explosion.
9. Return the ship — Pie Rats angry but grudgingly impressed. One Pie Rat flips player a Pie Rat Coin (Trophy Case treasure item).

**Notes:**
- Hidden secondary mine entrance remains open after cave-in.
- May gives no hints about Kevry's island or the Enchanted Glasses.

---

### Guardian's Lantern — Dark Room Interaction

Guardian's Lantern (dropped by The Warden, upper tier) flickers everywhere in the dungeon but only functions in the Dark Room (lower tier). When activated there:
- Magical darkness collapses immediately (no gradual brightening).
- Room is revealed as a plain stone room with a hook on the wall.
- Lantern is hung on the hook — stays permanently, not takeable after.
- Passage forward (south) opens.

`TURN ON LANTERN` or `LIGHT LANTERN` both work.

---

### Whispering Jar (Quest 4)

Restored with wax seal + silver dust + incantation (etched into base — readable via perception check or Enchanted Glasses). Whispers once: *"The ceiling of the thermal vent holds a secret."*

One time only, never repeated. This is the only hint anywhere for the fire clay in the Thermal Vent Room (lower tier, `LOOK UP`).

---

### Undead Werewolf Chain

The only weapon that destroys the undead werewolf in The Still Den (lower tier): consecrated silver stake.

Chain:
1. Silver stake — Town Square statue base (crowbar to open; `LOOK AT STATUE` reveals seam, no perception check)
2. Keeper's key ring — Keeper's skeleton, Lower Crypt (emerald seal matches statue note)
3. Holy water — Keeper's Chamber, Church of All (key required)
4. `POUR HOLY WATER ON STAKE` → consecrated silver stake
5. `DRIVE STAKE INTO WEREWOLF` → werewolf destroyed; reverts to scholar appearance on death

**Combat mechanic:** The werewolf cannot be harmed by conventional weapons, spells, or bow. Each round the player and werewolf roll simultaneously — the player takes damage on a loss, but the werewolf takes no damage regardless of result. The only kill condition is `DRIVE STAKE INTO WEREWOLF` with the consecrated silver stake — instant kill, no roll required.

**Attack value:** Level 5 (3d10, EV 16.5). Late-game threat — a player without the stake burns hearts fast.

**Weapon failure messages:**
- **Melee:** *Your blade finds its mark. The creature doesn't notice. It turns toward you with the patience of something that has been waiting a very long time.*
- **Bow:** *The arrow strikes true and stays there. The werewolf looks at it briefly, then at you. It does not appear concerned.*
- **Fireball:** *The fire takes hold for a moment — then dies. Whatever this creature is made of, it isn't interested in burning.*
- **Unconsecrated stake:** *The stake pierces flesh. The werewolf snarls — pain, but not the right kind. It pulls free and the wound closes. You need something more than silver.*

---

### Echo Alcove — Cross-Tier Audio

Echo Alcove (mid-tier key side) is a one-way acoustic listener. Same text every visit: *"A faint grinding drifts up from somewhere far below — bone on stone."*

This sound originates from the Antechamber (lower tier) / Bone Crunch Floor Room — warning text there mirrors the echo: *"The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here."*

No commands available in the Echo Alcove.

---

### Weight System (Rickety Bridge)

The Rickety Bridge (between Shrine Room and Mid-Tier Key Door, upper tier) has a carry weight limit. Exact limit TBD.

If inventory exceeds limit: bridge groans, player turned back. Must drop items, cross, return for them. Always crossable at or under limit. This is a logistical puzzle, not a trap.

All items need weight values assigned — design pass needed.

---

### Trophy Case

Fixed container in The Tower (Town Hall). Treasure items are placed here permanently — they cannot be removed once deposited.

**Rules:**
- Case must be open to accept items (`OPEN CASE` first).
- `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` — registers treasure in count. Confirmation: *"The [item name] settles into the velvet. The case is a better place for it."*
- `TAKE <ITEM> FROM CASE` — always returns: *"That belongs to Roundabout now."*
- `LOOK IN CASE` / `EXAMINE CASE` — lists contents and count whether open or closed (glass panels visible either way).
- **Count display:** *"[N] treasure[s] on display."* No denominator shown during play. Win condition reveals: *"9 of 9 treasures on display."*

---

### Parser Verbs (Confirmed)

| Verb | Context |
|------|---------|
| `OPEN MAILBOX` | White House / Tale and Ale — portal to Will's Tower |
| `DIG` | Shovel required; three confirmed uses plus beach flavor |
| `LIGHT GUNPOWDER` | Pie Rat heist |
| `FISH` | Roundabout Pond; requires fishing rod |
| `TURN DIAL LEFT` / `TURN DIAL RIGHT` | Church of All altar — cycles through 7 religions |
| `BOARD SHIP` / `GET ON SHIP` / `CLIMB ABOARD` / `ENTER SHIP` | Boarding Pie Rat Ship (all synonyms) |
| `SET SAIL` / `SAIL` | Begin sailing from Docks; directional movement (`GO EAST`, `SAIL EAST`) once underway |
| `DOCK` | Returning ship to harbor |
| `TALK TO [NPC]` | Standard NPC interaction verb |
| `LOOK AT BOARD` | Quest Board in The Bar |
| `LOOK AT STATUE` | Town Square statue — reveals seam (no roll) |
| `LOOK AT BANNER` | Viking Encampment — reveals elemental runes (Trial 2 clue) |
| `LOOK UP` / `LOOK AT CEILING` | Thermal Vent Room — reveals fire clay on ceiling (synonyms) |
| `ACTIVATE [ELEMENT] STONE` | Ritual Circle (Trial 2) — also accepts LOVE/LIFE for Heart |
| `POUR HOLY WATER ON STAKE` | Creates consecrated silver stake |
| `DRIVE STAKE INTO WEREWOLF` | Destroys undead werewolf |
| `CAST UNBIND UNDEAD` | Releases ghost in Ghost's Room (Chuckle House) |
| `HOLD TORCH NEAR ICE` | Quest 34 — two turns to thaw frozen soldier |
| `POUR VIAL IN WATER` | Quest 34 — freezes dark pool in mid room |
| `READ SCROLL` | Quest 34 — answers speaking door (all classes); spell scrolls — Mage only (Warriors/Rogues get resistance message pointing to Will); in Will's Tower, triggers spell teaching for Warriors/Rogues |
| `GIVE SCROLL TO WILL` | Synonym for `READ SCROLL` in Will's Tower — Warriors/Rogues; both work |
| `TURN ON LANTERN` / `LIGHT LANTERN` | Guardian's Lantern — dispels Dark Room darkness |
| `TIE ROPE TO BEAM` | Hole to Below — enables bidirectional travel |
| `CLIMB DOWN ROPE` / `CLIMB UP ROPE` | Hole to Below traversal (also `DOWN` / `UP`) |
| `RUB PAPER ON ENGRAVING` | Quest 28 — produces rubbing in Inscription Chamber |
| `SWAP IDOL WITH SALT` | Trap 33 — safe pedestal swap in Idol Room |
| `CLEAR BONES` | Trap 36 — disarms Bone Crunch Floor Room |
| `CLEAR DRAIN` | Quest 25 — unclogs cellar drain after cover removed |
| `LOAD STONE ONTO CART` | Quest 32 — loads gravestone onto hand cart |
| `JUMP ON PLATE` | Trap 29 — intentionally triggers Warden bell |
| `PRY DOOR` | Trap 33 escape — crowbar + strength check |
| `USE PORTCULLIS BAR` | Trap 19 — props portcullis open permanently |
| `CLIMB TREE` | The Old Oak — retrieves kite + rune stone |
| `LOOK AT MUSIC BOX` | Will's Tower — triggers quest discovery and hint sequence (Quest 12) |
| `OPEN CASE` / `CLOSE CASE` | Trophy Case in The Tower — case must be open to place items |
| `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` | Trophy Case — places treasure permanently; case must be open |
| `LOOK IN CASE` / `EXAMINE CASE` | Trophy Case — lists contents and count; visible through glass whether open or closed |
| `TAKE <ITEM> FROM CASE` | Trophy Case — always refused: *"That belongs to Roundabout now."* |

Full verb list and synonym handling policy TBD — design pass needed.
