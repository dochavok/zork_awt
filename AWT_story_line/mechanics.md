# Roundabout: The God-Forsaken Ring — Mechanics

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
| Food & Drink (1 heart) | 2 Zenni — 1 Zenni after Quest 22 |
| Hearty Stew (2 hearts) | 2 Zenni — unlocked after Quest 40; 1 Zenni after Quest 22 |
| Inn Rest (full heal) | 5 Zenni |
| Weapon training | 3 Zenni |
| Archery training | 3 Zenni |
| Spell training (Will) | Free (decided 2026-10-05) |
| Gunpowder | 5 Zenni |
| Fishing Rod | 8 Zenni |
| Dagger | 5 Zenni |
| Mace | 25 Zenni |
| Battle Axe | 100 Zenni |
| Tip Journal | 5 Zenni |
| Thin paper | 2 Zenni |
| Torch | 3 Zenni |

**Zenni sources:**
- Will Passion opening gift: 10 Zenni
- Hidden room Zenni: 36 rooms randomized per new game; 18 Easy / 10 Medium / 2 Hard pay 1–3 Zenni each; 6 Very Hard pay 5 Zenni each (~74 Zenni total if all found); Actually Enchanted Glasses pass all checks and find all rooms automatically
- Desert Island buried chest: 30 Zenni
- Quest rewards: ~133 Zenni across all 27 active quests (3–10 Zenni per quest, mirroring XP tiers)

---

### XP & Leveling

- XP earned through combat, quests, and discovering new locations.
- Leveling is instant when XP threshold is met.
- Level cap: 8. Full XP thresholds and dice progression in `experience.md`.
- Leveling improves dice rolls for both combat and challenge checks.

---

### Inventory Display

`WEAR X` works only on wearable items (the glasses, the ring, the Heart Necklace, the gloves, the tunic, the boots, the Pie Rat disguise); anything else: *You can't wear the X.*

`INVENTORY` / `I` lists carried items by their inventory description (items.md). Worn items show **(being worn)**; an equipped weapon shows **(equipped)**; wearable items carried but not worn show **(not worn)**. Nothing carried: *"You are empty-handed."*

The purse always ends the list: *"You have 12 Zenni."* (*"You have 1 Zenni."*, *"You have no Zenni."*). Empty-handed prints both lines. There is no other place the player is told the total, besides `SCORE` during play (below) — no `ZENNI` / `PURSE` command, and the end-of-game score leaves Zenni out (decided 2026-10-05).

### Dice & Roll System

All checks are dice-based and hidden from the player. Players see outcomes only, never numbers.

**Roll types:**
- **Perception** — finding hidden things, noticing details, spotting traps. Class bonus: Mages and Rogues.
- **Strength** — forcing doors, breaking locks, prying, physical feats (arm wrestling, rope snare escape, portcullis lift, timber clearing, Boggart strongbox, magnetic chest recovery, Thornbrew drinking contest — contested vs. Aylora's 1d6 + 2, see locations.md Fire Pit). Class bonus: Warriors.
- **Agility** — dodging hazards (Archery Range arrow dodge before Viking trust earned; Easy, 5). No class bonus.
- **Trap disarm** — disabling a detected trap without triggering it. Class bonus: Rogues.

**Trap detection and disarm flow:**
Both rolls fire automatically on room entry. The player issues no verb — the mechanic is fully hidden.

1. **Perception roll fires.** On failure: trap not seen, springs normally with its standard consequence text.
2. **On perception success: disarm roll fires immediately.**
   - **Disarm success:** *"You spot [descriptor] and are able to disarm it, neutralizing it."* Trap does not fire.
   - **Disarm failure:** *"You see [descriptor], but your attempt to disarm it fails miserably."* Trap fires — standard consequence text follows immediately after.

Each trap entry in `traps.md` includes a `descriptor` field used in the above messages.
- **Fishing** — `FISH` at Roundabout Pond; success retrieves the bottle (a treasure; no quest). Class bonus: Rogues.

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
| Arcane | The Flooded Passage pool (magical dark water) |
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

**Round structure:** Turn-based. Player issues an attack command each round (`KILL X WITH MACE`, `SHOOT X WITH BOW`, `CAST FIREBALL AT X`). Player and enemy roll simultaneously. Higher roll wins the right to deal damage — 1 heart per hit. On a tie, both deal 1 heart damage simultaneously.

**Fleeing:** Player may flee by leaving the room. Enemy resets to full hearts.

**Bow — first round bonus:** +5 to the attack roll on the opening bow attack of any combat. No bonus on subsequent rounds.

**Bow attacks (decided 2026-10-05):** `SHOOT X` / `SHOOT X WITH BOW` (and `KILL X WITH BOW`) is one round against the mugger, the Warden or the afflicted apprentice, with the bow roll (Gear bonuses, below).
- Shot lines: hit — *Your arrow finds its mark. The [mugger / Warden / apprentice] staggers.* Tie — *You loose an arrow as it closes on you. Both of you feel it.* A miss uses the fight's own "you take a hit" line.
- The +5 applies only when the fight's first round since it last reset (leaving resets the mugger, Warden and apprentice) is a bow shot. Swing first and later shots get nothing.
- `SHOOT` equips the bow if it's carried but not equipped (the equip line prints, then the round). No bow carried: *You've nothing to shoot with.*
- `SHOOT X WITH` something other than the bow: *That won't shoot anything.* Shooting a non-enemy: *You can't fight the X.*
- The werewolf: its bow line (Undead Werewolf, below); that turn's werewolf round still happens. The knight: his bow line (npcs.md); no turn used.
- The Archery Range targets take no SHOOT commands.

**Fireball:** Guaranteed 1 heart damage — no roll required. 10-turn reuse timer. Effectively once per combat encounter.
- **Built (2026-10-04):** `CAST FIREBALL` / `CAST FIREBALL AT [enemy]`. The fireball is the whole round: the enemy loses 1 heart and doesn't strike back. Hit line: *Fire leaves your hands in a single roaring sheet and takes the [enemy] full on. It reels back through the smoke.* With no target named, it hits the enemy present.
- The werewolf: its failure line (Undead Werewolf, below), and the turn's werewolf round still happens. The timer starts.
- The Fountain Room ice (Quest 34): *The fireball bursts against the block and rolls off it like water off glass. The frost doesn't so much as dull. I guess not every problem can be solved with fireball.* No timer.
- Nothing to hit: *Nothing here answers the spell.* No timer.
- **Any spell cast before it's ready:** *You reach for the spell and find it isn't ready yet.* — doesn't use a turn.

**Melee weapons:** Warriors may use melee weapons from the start. Mages and Rogues require the Weapon Use skill (Quest 54) before any weapon provides a bonus — without it, `KILL X` defaults to unarmed (+0) regardless of inventory. Three weapons are sold by Shamus (Kitchen, Tale and Ale): Dagger (+2, 5 Zenni), Mace (+4, 25 Zenni), Battle Axe (+6, 100 Zenni). The combat roll for a melee attack is the player's base roll plus the equipped weapon's bonus (Equipping weapons, below).

**Gear bonuses (decided 2026-10-05):** one set of combat rules (content/combat.py) serves every fight — the mugger, the Warden, the apprentice, the knight and the werewolf.
- Melee roll = level dice + the equipped melee weapon (+2 / +4 / +6) + the Apprentice's Gloves (+3, only while worn).
- Bow roll = level dice + 5 on the opening round of the fight + the gloves (+3, while worn). No melee weapon bonus.
- A weapon is usable by a Warrior, or by a Mage or Rogue once Quest 54 is complete. Anyone can buy and carry one; unusable, it adds nothing.
- Ivanaar's Tunic's avoidance roll applies to every hit the player takes in every fight, the mugger's included.
- The werewolf: the roll (with all bonuses) only decides whether its claws land. Nothing but the stake harms it.
- Weapons are always on sale at Shamus's (npcs.md — Shamus, The slate).

### Equipping weapons

Decided 2026-10-05. `EQUIP X` / `WIELD X` takes up the bow, the Dagger, the Mace or the Battle Axe. One at a time; only the equipped one counts in a fight.
- `KILL X` uses the equipped melee weapon — bare hands (+0) if nothing or the bow is equipped. `SHOOT X` uses the bow and equips it if needed.
- `KILL X WITH Y`: if Y is a carried weapon the player can use, it's equipped first and the round follows in the same turn; otherwise the round is fought as normal. `KILL X WITH BOW` is a bow shot.
- Nothing equipped: *You take up the bow.* Something else equipped: *You put away the mace and take up the bow.* Already equipped: *You're already holding the bow.*
- Melee weapons need Weapon Use (Warriors; Mages and Rogues after Quest 54). Without it: *You don't know how to fight with the dagger. The knight in the square teaches that.* The bow: anyone who has it (it always comes with the skill).
- `EQUIP` anything else: *You can't equip the rope.*
- `UNEQUIP X` / `REMOVE X`: *You put away the mace.* Not equipped: *You aren't holding the mace.*
- Dropping, giving or otherwise parting with the equipped item unequips it silently. INVENTORY shows it with **(equipped)**.

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

**Spell training (Quest 56)** — Will Passion, Wizard Tower.
Warriors and Rogues cannot read spell scrolls directly — resistance message points them to Will.
Bring any spell scroll; Will teaches it aloud; scroll consumed, spell learned permanently. Repeatable for each new scroll.
No cost — Will teaches for free (decided 2026-10-05). Wearing the Enchanted Glasses in Will's presence is an instant fail state (Will attacks, no recovery) — see items.md. Remove them before entering the tower.
Classes: Warrior, Rogue only.

---

### Armor Slots

- Head
- Chest
- Legs
- Hands
- Neck *(Heart Necklace)*
- Ring *(The God-Forsaken Ring)*

Armor is found through exploration and never degrades.

**Armor audit (complete):**
| Slot | Item |
|------|------|
| Head | Enchanted Glasses / Actually Enchanted Glasses |
| Chest | Ivanaar's Tunic (Quest 42 reward) |
| Legs | Bartender's Boots (Quest 25 reward) |
| Hands | Apprentice's Gloves (Quest 50 reward) |
| Neck | Heart Necklace (Lynds arm wrestling) |
| Ring | The God-Forsaken Ring |

**Ivanaar's Tunic — damage avoidance:**
When the enemy wins a combat round and would deal 1 heart damage, the tunic fires a silent 1d10 roll. Result of 7–10 (40%) negates the damage entirely. Fixed — does not scale with player level. The roll is completely hidden; no message indicates it occurred. On a successful avoidance, one of four flavor messages fires at random instead of taking damage:

1. *The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.*
2. *For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.*
3. *The runes along the collar catch the light briefly. You are less hurt than you expected to be.*
4. *Something in the weave absorbed it. You felt the impact — and then didn't.*

---

## The God-Forsaken Ring

- Grants invisibility while worn. `WEAR RING`: *You slip the ring on. When you look down, your hand is still there — but only because you know where to look.*
- Corruption timer advances each turn worn. Pauses on removal; resumes on re-equip. Never resets.
- Can't be dropped (items.md — The God-Forsaken Ring): *"Bring it to me, or keep it close," Will said. You keep it close.* Weight 0.
- **Total ticks to full corruption: 50.**
- Altar use at Church of All does NOT tick corruption — the ring is being used for its purpose, not personal gain.
- Quests requiring invisibility: Chuckle House (Quest 17 — mirrors repel visible players) and Dankhaus (Litlock will not engage while player is invisible).

**Corruption milestones:**

| Tick | Event |
|------|-------|
| 10 | First warning |
| 25 | Midpoint warning |
| 40 | Urgent warning |
| 41–49 | Challenge roll window — removal requires passing a roll; difficulty escalates each tick; a message each tick |
| 50 | Full corruption — game over (failure ending), no roll offered |

**Milestone messages:**

- **Tick 10:** *The ring is warm. You hadn't noticed until just now. You're not sure when it started.*
- **Tick 25:** *The ring is heavier than it was. Not in weight — in presence. It knows you're wearing it. You find yourself aware of it in a way you weren't before.*
- **Tick 40:** *The ring is harder to ignore than it was. You are aware of it the way you're aware of a sound that hasn't stopped. You should take it off. You know you should take it off.*
- **Ticks 41–49** (decided 2026-10-09): one line on each tick, the player's own voice giving way, so tick 50 lands as the end of a slide. Like every milestone, a line prints once, on the turn the ring reaches that tick — ticks only advance while the ring is worn.
  - **41:** *Take it off. You should take it off.*
  - **42:** *Take it off. Soon.*
  - **43:** *You could take it off. You could.*
  - **44:** *Take it — the thought slides away before you finish it.*
  - **45:** *Off. Take it… You lose the rest of the sentence.*
  - **46:** *You don't need to take it off. Do you?*
  - **47:** *Why would you take it off?*
  - **48:** *It's fine. The ring is fine.*
  - **49:** *The ring is warm, and you are warm, and everything is fine.*

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

**Game over message (tick 50) — a fail condition, no resurrection:** *You reach for the ring. Your hand doesn't move. You watch it not move. The ring is warm and patient and it has been waiting for exactly this. You are not going to take it off.*

**Corruption is sacred:** Ring corruption must never be reduced, slowed, or mitigated by any mechanic, item, or quest reward. This is a hard design constraint.

---

### Enchanted Glasses

Two versions:
- **Enchanted Glasses:** Small bonus to perception checks.
- **Actually Enchanted Glasses:** Pass all perception checks automatically — no roll required.

Upgrade path: equip glasses (head slot) before reaching Kevry Talborn's island (69 squares east in Open Ocean) → Kevry enchants them.

Warning: wearing them in Will's presence triggers an instant fail state (Will attacks, no recovery). Equipping inside the bedroom is safe — Will is not there.

End-game return: dropping in Will's Bedroom earns XP (double if Actually Enchanted).

---

## Spell Mechanics

Spells learned permanently once acquired.

**Reuse timers:** Number of turns before spell can be cast again. Starts when cast — independent of duration.

**Duration:** Number of turns effect lasts. Independent of reuse timer.

**Casting (`CAST <spell>`):**
- Nothing to affect: *"Nothing here answers the spell."* — the reuse timer does not start.
- Reuse timer still running: *"You reach for the spell and find it isn't ready yet."*
- Spell not learned: *"You don't know that spell."*

**Spell scrolls vs. use-item scrolls:** Spell scrolls teach a spell permanently (Light, Unbind Undead, Fireball). Use-item scrolls teach nothing and aren't used up (incantation scroll — Quest 28/34 speaking door; full rules in items.md). The resistance mechanic below applies to spell scrolls only; use-item scrolls work for all classes.

**Warrior/Rogue scroll resistance:** `READ SCROLL` on a spell scroll returns:

*"The words are legible. The meaning is not. Whatever is written here was meant for someone with a different kind of mind — or a different kind of training. Will Passion, in his tower, has been known to translate this sort of thing for people like you."*

Scroll is not consumed. Player retains it. Bringing the scroll to Will Passion in the Wizard Tower triggers the teaching interaction via either `READ SCROLL` (in his presence) or `GIVE SCROLL TO WILL` — Will takes it, reads it aloud, scroll consumed, spell learned permanently.

**Mage reads a spell scroll:** *You read the scroll through once, and the words settle into you as if they had always meant to. The scroll crumbles to dust in your hands.* Spell learned, scroll consumed.

| Spell | Effect | Duration | Reuse Timer | Source |
|-------|--------|----------|-------------|--------|
| Light | Creates light in darkness — see Lighting System | Continuous while in dark | None | Quest 12 — music box key in Bog-NW |
| Unbind Undead | Releases a bound spirit | Instant | 20 turns | Lighthouse — scroll on Silas Bryne's desk |
| REST | Recovers 1 heart | Instant | 50 turns | Granted at Level 6 — no scroll required, no XP awarded |
| Fireball | Guaranteed 1 heart damage — no roll required | Instant | 10 turns | Quest 7 reward — Pyronicus |

**REST notes:** Outside combat only — hostile in room returns *"You can't rest now, there's fighting to be done!"* Before reuse timer expires returns *"What are you sitting around for, there's a dungeon to explore!"* Works while inked. Stacks with inn healing and food.
- **Built (2026-10-05):** `REST` heals 1 heart and starts the 50-turn timer: *You sit with your back to the nearest wall and let your breathing slow. When you get up, some of the ache has gone with it.*
- Before Level 6: *You're not tired.* At full hearts: *You're as rested as you're going to get.* (no timer started).
- "Hostile in room" = a live enemy there: the spotted mugger, the Warden once he's out, the afflicted apprentice before he's freed, the living werewolf, a knight trial in progress.
- Every refusal (before Level 6, in a fight, timer not up, full hearts) uses no turn.

**Standard level-up message (all levels):** *"You hear music — a familiar melody. You have reached level [#]!"*

**Level-up message on acquiring REST (Level 6 only):** Fires after the standard level-up message. *"You feel a deeper sense of calm settle over you — the kind that comes with hard-won experience. You can now REST to recover when the fighting stops."*

**Nobu's Favor (Level 7) and Finishing Move (Level 8):** No additional message. Secret abilities are never announced.

---

## Finishing Move

Granted silently at Level 8. The player is never told this ability exists — no level-up message, no journal entry, nothing.

**Trigger:** All 3d20 roll 15 or higher in a single combat roll (~2.7% chance per roll).

**Effect:** Instant kill. The enemy is defeated immediately regardless of remaining health.

**Built (2026-10-05):** checked at the start of every attack round against the mugger, the Warden and the afflicted apprentice (he is freed, as on any win). Not the knight (a trial that stops at one heart) and not the werewolf (only the stake harms it). The player takes no damage that round.
The roll is one draw of 216 in 8,000 — the same odds as 3d20 all at 15+ — so the always-max test dice never trigger it.

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

**Death (0 hearts, no Nobu's Favor):** GAME OVER — *Your last heart gives out. The dark closes in, and this time it keeps you.* (Exceptions: the Back Alley mugger and its fight knock the player out instead.)

---

## Hint System (May)

May sells hints for Zenni at The Bar, Tale and Ale. Hints are tiered — each tier costs more than the last. Tiers must be purchased in order.

**The player tips blind.** There is no menu, no listed price.
The player gives May a Zenni amount and May decides what it buys.
The tier boundaries are never shown to the player — only May "knows" them.
A player who tips 3 Zenni every time will always get Tier 1 hints and never know they could have paid more.
A player who tips 7 Zenni from the start will unlock Tier 3 but overpay for early hints.
The inefficiency is intentional — it rewards players who experiment and pay attention to May's responses.

**Tier cost ranges (internal — never shown to player):**
- Tier 1: 1–3 Zenni
- Tier 2: 4–6 Zenni
- Tier 3: 7–12 Zenni

Some hints are conditional: May's tier 1 hint for Quests 19&30 fires only if player has not yet examined the statue. Post-visit Chuckle House hints unlock once player has entered the Chuckle House.

**May's responses by tip amount:**
- **Tier 1 (1–3 Zenni):** *May palms the coin without looking at it, leans in, and shares what she knows. "That's worth something," she says.*
- **Tier 2 (4–6 Zenni):** *May pockets the coins carefully. "That buys you something worth hearing," she says.*
- **Tier 3 (7–12 Zenni):** *May counts the coins once, pockets them, and leans all the way across the bar. "[Name]," she says.*
- **Nothing to share (any amount, no hints remaining):** Randomly selected from:
  1. *May pushes the Zenni back. "Keep it. I've got nothing worth that right now." She goes back to wiping the bar.*
  2. *May looks at the coin and shakes her head slowly. "I'd be robbing you. Ask me again when something changes."*
  3. *May sets the Zenni on the bar and slides it back. "Nothing in here worth selling today," she says, tapping her temple.*
- **Over 12 Zenni:** *May looks genuinely uncomfortable. "I appreciate the thought, but no." She slides it all back. "Ask me something and we'll talk."*
- **No amount (`TIP MAY`):** *May waits. "How much?"*
- **Zero (`TIP MAY 0`):** *May looks at your empty hand, then at you. "That's nothing."*
- **More than the player has:** *May looks at you evenly. "You're short." She goes back to work.*
- **Not in the Bar:** *May isn't here.*
- **Giving Zenni is tipping** (decided 2026-10-05): with May present, `GIVE 3 ZENNI TO MAY`, `GIVE MAY 3 ZENNI`, `HAND MAY 3 ZENNI` and `PAY MAY 3` work exactly like `TIP MAY 3` (same lines, same tiers). `GIVE ZENNI TO MAY` / `PAY MAY` with no amount: *May waits. "How much?"* Giving her an item is still an ordinary GIVE.
- `TIP [#]` without May's name tips May too — she's the only one who takes tips.
- No Zenni changes hands in the last six cases.

The response follows the amount tipped, not the tier delivered — a 7-Zenni tip that falls back to a Tier 1 hint still gets the Tier 3 response. The hint follows the response. "[Name]" is the player's name. (Decided 2026-10-04.)

**One-tier hints** count as Tier 1. **Phased hints** (Quests 17 and 32): when a quest moves to its next phase, hints left unbought in the earlier phase stop being sold.

**Hints before discovery:** Quests 19&30 and Quest 4 are sold before they're discovered, and buying one discovers the quest; Quest 34's late hint is sold before discovery but doesn't discover it. Per-quest conditions are in quests.md. (Decided 2026-10-04; confirmed 2026-10-05 that the 19&30 hints stay on sale from game start.)

**Which hint a tip buys (decided 2026-10-04):** the tip amount sets the tier paid for. May gives a random hint at exactly that tier — chosen from the quests whose next unbought hint is that tier. If there are none, she steps down one tier and picks at random there, and so on down to Tier 1.
Tiers stay in order per quest, so a large tip can buy a low tier (the overpaying above). If nothing is left at or below the tier paid for, she gives a "nothing to share" line and the Zenni comes back.

May only offers hints for quests that are discovered AND incomplete. She won't hint on undiscovered or finished quests. Each tier for each quest is a one-time purchase — May will not re-sell a tier already bought.

**Free drink flag system:** A boolean flag tracks pending free drinks, each with a reason string for contextual dialogue. Flag is set by quest events; cleared after the free drink is redeemed. Current known flags:
1. **Mugger slain** — *May thanks [Name] for dealing with whoever was lurking in the Back Alley, and doesn't charge for the drink.*

**Raznak nudge (free, no Zenni):** If the player has visited the Archery Range at least once but has never spoken to Raznak (not yet reached any dialogue state), May offers unprompted: *"You should talk to Raznak."* Fires once only. No tier, no cost.

---

## Lighting System

### Dark Rooms

The following areas are dark and require a light source to enter:
- **Dungeon** — all rooms (Upper, Middle, and Lower Tier)
- **Secret Tunnels** — all rooms (abandoned, unmaintained, genuinely lightless)
- **The Crypt and Mausoleum** — cold, unlit stone

**Naturally lit areas (no light source required):**
Overworld, town, mine (active, torches on walls), Dankhaus, bog, beach, sea.

**Dark room behavior:** Darkness is a hard block — the player cannot enter without a light source. No navigation in the dark, no death-by-darkness, just a wall: *"It's too dark to go any further without a light."*

---

### Light Sources

Three distinct light sources, each with a separate role:

| Source | Works in dark rooms | Works in Dark Room (magical darkness) | Notes |
|--------|--------------------|-----------------------------------------|-------|
| Torch | Yes | No | Vendor item, 100-turn burnout, early game |
| Light spell | Yes | No | Continuous (no duration limit, no reuse timer), Quest 12 unlock |
| Guardian's Lantern | Yes | Yes | One-time Dark Room solution, stays on wall |

The Dark Room (lower tier) is immune to both torch and Light spell — *"This is not like being in the dark. This is something the dark is doing on purpose."* The Guardian's Lantern is the only answer there.

---

### Torch

Purchased from Shamus (Kitchen, Tale and Ale) for 3 Zenni. Weight: 2.

- Always lit from the moment of purchase — no `LIGHT TORCH` verb required.
- **Timer starts on first dark room entry**, not on purchase. A player who buys a torch and spends time in town loses nothing.
- **One torch at a time** in inventory. Shamus will swap a torch at any point depending on life remaining — see swap tiers below.
- **Ignition message (fires once per torch, on first dark room entry):**
  *The torch catches the dark and pushes it back. Good thinking, getting one of these.*

**Warning messages (by turns remaining):**

| Turns remaining | Message |
|----------------|---------|
| 50 | *The torch burns a little lower than it did.* |
| 30 | *The torch is noticeably dimmer now. It won't last forever.* |
| 15 | *The torch gutters. You don't have much time left on it.* |
| 0 | Burnout — see below |

**Torch burnout (turn 0):** Once lit, the torch can't be put out — the timer runs every turn after the first dark room entry.
- **Game over** only if the player is in a dark room **and** no exit from it leads straight to a lit room: *The torch goes out. In the dark, something shifts. You never find out what.*
- **Otherwise** (in a lit area, or one move from one, or with the Light spell already lit) the torch just goes out: *The torch gutters and goes out.* The player can walk back to the light.
- **Light spell known but not lit** (stranded as above): not game over, but the player must cast it fast — *The torch goes out. The dark closes in fast — if you're going to cast something, now would be the time.* `CAST LIGHT` within the next two commands (commands the parser doesn't understand don't count). Otherwise: *In the dark, something shifts. You never find out what.* — GAME OVER.

**Dropping the torch** (decided 2026-10-05):
- A burnt-out torch has no use. `DROP TORCH` (or `DROP ALL`) removes it from the game, back into Shamus's stock: *You toss the burnt-out torch aside. It's no good to anyone now.*
- A lit torch dropped stays on the floor (*A lit torch.*).
- `BUY TORCH` when not carrying one sells a fresh torch; a lit one left lying elsewhere quietly leaves its room (there is only one torch).
- A lit torch left lying keeps burning down. In another room it does so unseen: no warnings, no burnout line, no stranded check.
- Carried, or on the floor of the player's room, it gets all the messages above, stranded check (and game over) included.

**Shamus swap tiers (`BUY TORCH` while already carrying a torch — the only way to swap; 3 Zenni):**

| Turns remaining | Shamus response |
|----------------|-----------------|
| 100–70 | *Shamus glances at the torch. "That one's got plenty of life left." He hands it back. "Come see me when it's lower."* — no swap |
| 69–30 | *Shamus glances at the torch. "Getting there." He hands you a fresh one. "Three Zenni."* |
| 29–15 | *Shamus glances at the torch. "That one's running short." He hands you a fresh one. "Three Zenni."* |
| 14–0 | *Shamus glances at the torch. "That one's had it." He hands you a fresh one. "Three Zenni."* |

Swapped torches reset the timer to 100. The ignition message fires again on next dark room entry. Like a bought torch, the fresh one does not start burning until that entry. At 100–70 no Zenni is taken.

---

### Light Spell

Learned permanently via Quest 12 (Light scroll, music box in Will's Tower).

- Cast once on entering darkness. Runs continuously while the player remains in dark rooms. Extinguishes automatically on returning to naturally lit areas, resets silently, ready to cast again.
- Knowing the spell lets the player step from a lit room into a dark one without a light: it's pitch black there (*It is pitch black. You are likely to be eaten by a grue.*) until `CAST LIGHT`. Moving on from an unlit dark room into another dark room is still refused (*It's too dark to go any further without a light.*).
- `CAST LIGHT` in a naturally lit room: *There's light enough here already.* While the spell is already lit: *The light's already with you.*
- No duration limit. No reuse timer.
- Does not work in the Dark Room (lower tier) — magical darkness is immune to natural light sources. `CAST LIGHT` there before the lantern gets its own line (locations.md — Dark Room).

**Cast message:**
*The darkness pulls back. The spell settles into a steady glow — patient, reliable, yours for as long as you're down here.*

The Light spell replaces the torch as the primary light source once Quest 12 is complete. Players carrying a torch can drop it to free carry weight (useful on the Rickety Bridge weight limit).

---

### No Light Source — Will's Messages

Fires when the player attempts to enter a dark room without any light source (no torch, Light spell not active). Selected randomly from the pool below. Fires once per dark room attempt — not repeated on subsequent attempts in the same session.

The message does **not** fire if the player has the Light spell but hasn't cast it — they have a solution available.

1. *Will Passion materializes in your thoughts, uninvited. "You can't see anything. Somewhere above you, Shamus has torches for sale. I'm just going to leave that there."*
2. *It's completely dark. Will Passion's voice surfaces somewhere in the back of your mind: "Shamus. Kitchen. Three Zenni. You're welcome."*
3. *You can't see anything. Will Passion, uninvited: "I believe Shamus has torches. In the kitchen. Above you. For sale. I want to be very clear that I am not judging you."*
4. *The dark is complete. Will Passion materializes in your thoughts. "You are aware, I assume, that Shamus sells torches. You have been made aware of this in a way you perhaps weren't before. That's all I have."*

---

## Tip Journal

Purchasable from Shamus (Tale and Ale Kitchen) for 5 Zenni. Available to the player on request at any time.

**Display verb:** `READ JOURNAL`

**What it records:**
- Every discovered quest — does not appear until discovered; undiscovered quests are invisible
- How the quest was discovered: `[Board]` (Quest Board posting), `[May]` (May's hint), or `[Organic]` (found in world)
- Each hint purchased from May, in order, with the full hint text, labelled `Tip:` — never its tier number, which stays hidden from the player (decided 2026-10-09)

**What it does not record:**
- Completed quests — they drop off immediately on completion, keeping the journal a live action list

**Entry format:**

```
JOURNAL

The Bone Flute         [Board]
  Tip: Check the dungeon mid-tier — there's a passage off the Inscription Chamber.
  Tip: The cave creature isn't there. It's safe to go in.

The Whispering Jar     [Organic]

The Ruined Aqueduct    [Board]
  Tip: The aqueduct is southeast of town. The problem is visible from the road.
```

- Quest name and discovery source on one line
- Purchased hints appear indented below, each on its own line as `Tip:` and the full text
- No hints purchased: nothing below the quest name — silence is implicit
- Completed quests: removed from journal immediately on completion

**Edge cases:**
- Player has not purchased the journal: `READ JOURNAL` returns *"You don't have a journal."*
- Player has the journal but no quests discovered yet: *"The journal is empty."*
- Player has the journal and all active quests complete: *"The journal is empty."* (same message — no distinction)

**Rules (decided 2026-10-05):**
- Quests are shown by name only. Quest numbers are never shown to the player.
- The discovery tag is the first way the quest was discovered, and never changes: `[Board]` — read on the Quest Board; `[May]` — discovered by buying her hint (The Hollow Statue, The Undead Warden, The Whispering Jar); `[Organic]` — everything else.
- Quests are listed in the order they were discovered.
- A hint that covers two quests (The Hollow Statue and The Undead Warden) is listed under both.
- Phased quests (The Frozen Watch, The Missing Gravestone): hints from earlier phases stay. Each hint is labelled with the tier it was bought at, in purchase order, so a quest can read Tier 1, Tier 2, Tier 1.
- The Frozen Soldier's late hint is bought before that quest is discovered; it shows under the quest once it is.
- `READ JOURNAL` works with the journal carried or on the floor of the current room. Anywhere else: *You don't have a journal.* `EXAMINE JOURNAL` is the same as `READ JOURNAL`.
- Layout: `JOURNAL`, a blank line, then the quests. Names are padded so the tags line up in one column. A blank line between quests.
- Weight 0. The player isn't told; a journal is light, so it would be one of the last things dropped anyway, and keeping it never costs them anything.

---

## Quest Board

Located in The Bar of the Tale and Ale. Described in the room text. `LOOK AT BOARD` displays all currently posted quests. Completed quests are automatically removed from the board.

**Confirmed postings (cascade order):**
- Quest 22 (The Ruined Aqueduct) — posted at game start
- Quest 40 (Shamus's Recipe) — posted on first visit to the Kitchen (meeting Shamus)
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

Full cascade design — which quests unlock new postings — confirmed above.

**Rules (decided 2026-10-04):**
- `LOOK AT BOARD`, `READ BOARD` and `EXAMINE BOARD` all list the board. Nouns: board, quest board, notice board, notices, notice.
- A posted quest is discovered when the player reads the board while it's posted — not when it's posted. A notice the player never reads discovers nothing.
- Postings are listed in the order they went up. Completed quests are left off.
- "First meets Pyronicus" (Quest 7) is the ring hand-over (`TALK TO PYRONICUS`); the notice goes up 20 turns later.
- Quest 40 is also discovered by talking to Shamus; the Kitchen-visit posting is a second route.
- Quest 50's notice comes down for good when Trap 41 is disarmed. If the player already read it, the quest stays discovered; unread, it never appears.
- The Quest 51 bounty goes up at 100 turns only if the mugger is still alive.

**Board text:**
- Header: *Notices are pinned to the board, newer ones over older:*
- Empty: *The board holds nothing but pinholes and the corners of notices long since torn away.*

**Postings** (one line each, in posting order):
- Quest 22: *WANTED: someone to mend the old aqueduct beneath the town. The fountain's been dry for years. Drinks will be cheaper for it. — May*
- Quest 50 (unsigned — Will): *MISSING: a young man, last seen heading toward the dungeon. He may not be himself. If you find him, bring him out. Please.*
- Quest 40: *WANTED: bog thyme, and a cooking pot that isn't cracked. Bring both to the kitchen. There's a stew in it. — Shamus*
- Quest 7: *WANTED: a bone flute, somewhere in the middle passages below. Bring it to the forge beneath the volcano. — Pyronicus*
- Quest 17: *MISSING: a relative of mine went into the Chuckle House some years ago and never came out. If he lives, tell him to come home. If he doesn't, I would like his pocket watch. — Records Room, Town Hall*
- Quest 24: *SWARM LOOSE: my bees have taken up in a hollow tree at the forest edge. Help wanted bringing the queen home. Honey for your trouble. — the cottage west of the Old Oak*
- Quest 51: *BOUNTY: someone's been robbing people in the back alley. Whoever puts a stop to it drinks free. — May*

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

36 rooms across the world contain hidden Zenni, discoverable via silent perception check. Rooms are selected randomly at game initialization and fixed for that playthrough. Actually Enchanted Glasses pass all perception checks — all 36 rooms found automatically.

**Found message:** *Something catches your eye, tucked out of sight: [N] Zenni. You pocket them.* ("pocket it" for 1 Zenni.) The check repeats on every visit until that room's Zenni is found.

**Difficulty distribution (assigned at game init):**
| Tier | Count | Target | Zenni |
|------|-------|--------|-------|
| Easy | 18 | 5 | 1–3 |
| Medium | 10 | 9 | 1–3 |
| Hard | 2 | 14 | 1–3 |
| Very Hard | 6 | 18 | 5 |

**Eligible room pool:**

*Overworld & Town:*
White House, Will's Wizard Tower (Main Room), Will's Bedroom,
Main West, Town Square, Main East, The Alley, Back Alley,
Town Hall, Council Chamber, Records Room, Upper Hall, The Tower,
Tale & Ale Main Room, Bar, Ty's Casino Corner, Pipe Room, Kitchen, Upstairs Hall, Cellar/Storeroom,
Library Main Hall, The Stacks,
Church Nave, The Altar, Keeper's Chamber,
Graveyard, The Mausoleum, The Crypt,
Roundabout Wasteland, The Volcano, Pyronicus's Forge,
Archery Range, Viking Encampment, Haalvar's Hut, Ritual Circle, Fire Pit,
Roundabout Pond, Dankhaus rooms,
Beach Road, The Old Oak, Beekeeper's Cottage, Swarm Tree, Roundabout Forest,
Roundabout Beach, The Lighthouse, The Docks, Pie Rat Ship Deck

*Dungeon — Upper Tier:*
Ink Corridor, Supply Room, Narrow Passageway, Idol Room, Storage Area, Collapsed Gallery, Creature Den, Combat Room, Prayer Alcove, Portcullis Corridor, Shrine Room, Mid-Tier Key Door

*Dungeon — Mid Tier:*
Key Door Landing, Stored Room, Inscription Chamber, Cave Creature's Lair, Echo Alcove, Magnetic Vault, Deep Lock Door, The Spillway and Trap Side rooms (5)

*Dungeon — Lower Tier:*
Lower Crypt, The Encampment, Thermal Vent Room, The Lower Crossing, The Narrow Pass, The Still Den, Tool Alcove, The Flooded Passage, The Fountain Room, Spirit Room, Burial Chamber

**Excluded rooms (not eligible):**
All four Bog rooms, all Sea / Open Ocean squares, Desert Island, Kevry's Island, Pie Rat Ship Hold, Flooding Room, Dream Corridor, Dark Room, Hole to Below / Pile of Rubble, Rickety Bridge, Collapsed Aqueduct, all Chuckle House rooms (Entrance, Rejection Mirror, Shatter Trap Mirror, Ghost's Room), Mine Passage, The Crevice (has dedicated treasure — gold pocket watch), Skeleton Room (instant death on entry)
Also excluded: Guest Rooms 1–3 (Tale and Ale) — entered only by renting a room, with a random room each time.

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

Two-state room in the dungeon mid-tier. After digging, this room effectively becomes the Hole to Below — all references to "Hole to Below" refer to the Stored Room post-dig.

**Before digging:** *The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.*

**DIG action (shovel required):** One `DIG` collapses the floor permanently. The east spur to The Crevice is severed — the hole is too wide to cross. The Crevice and its gold pocket watch are permanently inaccessible. Beam exposed by collapse.

**DIG response message:** *The shovel bites into the packed rubble and the floor gives way — the fill cascades into the darkness below. You scramble back from the edge. A gaping hole now separates you from the eastern passage.*

**After digging:** *Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.*

**East exit (post-dig):** Blocked regardless of rope state. The hole cannot be crossed.

**DOWN / CLIMB DOWN without rope:** *The drop is serious. You'd need something to climb down on.*

**JUMP / JUMP DOWN (post-dig):** Death. *It occurs to you, as you fall, that this may not have been a good decision. You die.*

**TIE ROPE TO BEAM:** Rope from Docks (one item in world) tied to exposed beam enables safe bidirectional travel: `DOWN`, `UP`, `CLIMB DOWN ROPE`, `CLIMB UP ROPE`. No fall mechanic — player never falls involuntarily.

---

### The Dream Corridor

Liminal branching passage between The Spillway and Lost Apprentice's Cell (mid-tier trap side). Player does not know they are in a dream until they successfully pass through. On failure, room resets and replays — identical every time. No damage, no cost. Just the loop.

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
- Option 1 — Press hand against the wall: *FAILURE*
- Option 2 — Step back and look at the full wall: *FAILURE* (both options fail — the prose below)

**A2 — Hear (Follow path):** Narrow passage, sound of moving water below.
- Option 1 — Follow slope down toward sound: *SUCCESS*
- Option 2 — Follow draft, go toward air: *FAILURE* — passage opens onto nothing; drop.

**A3 — Smell (Follow path):** Smell gets stronger at a low alcove.
- Option 1 — Crouch inside and look for source: *FAILURE* — the light goes out.
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
*The corridor is low and wet. Water drips somewhere behind you. Your light throws just enough to see the floor — and the footprints already pressed into the mud. Leading in from the entrance. Your size. Your stride. You haven't been here before.*

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
- **B2 — See:** *Your light catches the wall of a side tunnel you hadn't noticed — or that wasn't there before. Claw marks run along the stone at shoulder height. Deep, parallel, dragged fast. Whatever made them was large. Whatever made them went that way. You follow anyway.*
- **B3 — Feel:** *The ground hums. Low, slow, rhythmic. Like something heavy moving far below, or far ahead — it's impossible to tell. Your boots feel it more than you do. You follow the vibration.*

**Level 3 — Outcomes:**

*A1 — The footprints end at a wall. Not a door — a wall. But the mud at the base is disturbed, smeared, like something passed through it. The light flickers.*
- Press hand against wall → FAILURE: *Cold stone. Solid. You press harder, run your fingers along the seam where the smear meets the surface. Nothing gives. It is definitively, completely a wall. You press your forehead against it. You wake up at the entrance. The footprints are there. Your size. Your stride.*
- Step back and look at the full wall → FAILURE: *Distance doesn't help. It's a wall. Flat, unbroken, mortared tight. Whatever the smear in the mud means, it doesn't mean a door. You stand there long enough to be certain. You wake up at the entrance. The footprints are there. Your size. Your stride.*

*A2 — You turn left. The passage is narrow — barely a shoulder's width. The sound of moving water is clearer now, ahead and below. The passage slopes down. The light gutters in a draft coming up from somewhere beneath you.*
- Follow slope down toward sound → SUCCESS: *The slope levels. The passage opens. The sound of water is all around you now — a drain somewhere below the floor, pulling the flood somewhere useful. The air is damp but moving. Ahead, a doorway. You walk through it. You are through.*
- Follow draft — go toward air, not water → FAILURE: *The draft gets stronger. The passage narrows further and then opens without warning — onto nothing. A drop. You can't see the bottom. The light goes with you. You wake up at the entrance. The footprints are there. Your size. Your stride. Your heart is going very fast and you're not entirely sure why.*

*A3 — The smell gets stronger as you move. At the end of the corridor a low alcove opens to the right — just wide enough to crouch into. Inside: nothing. No food, no fire, no source. The smell is overwhelming in here. Your stomach responds before your brain does.*
- Crouch inside and look for the source → FAILURE: *The alcove goes back further than it looked. You crouch deeper, light first. The smell is everywhere and the source is nowhere. The ceiling gets lower. You keep looking. The light goes out. You wake up at the entrance. The footprints are there. Your size. Your stride. You are not hungry anymore.*
- Ignore it and keep moving forward → SUCCESS: *You keep walking. The smell fades behind you the way smells do when you stop chasing them. The corridor ends at a doorway. You don't remember the corridor having a doorway. You walk through it. You are through.*

*B1 — The certainty leads you to a section of wall that looks identical to every other section of wall. No seam, no mark, no reason. The feeling is loudest here. Your light doesn't flicker. The wall doesn't breathe. It just is — and something in you insists this is the place.*
- Trust it. Press forward into the wall → SUCCESS: *You don't slow down. You don't brace. You walk into it the way you'd walk through a doorway you've used a thousand times. The wall is not there. The room beyond is. You are through it before you've decided what just happened. You are through.*
- Trust it. Wait. See if something happens → FAILURE: *You wait. The certainty doesn't grow or fade — it just sits there, patient, offering nothing new. The corridor is very quiet. You wait longer. The light holds. Nothing happens. The feeling eventually becomes indistinguishable from doubt. You wake up at the entrance. The footprints are there. Your size. Your stride. The certainty is gone.*

*B2 — The claw marks run the length of the tunnel, shoulder height, deep and continuous. You follow them.*
*The tunnel is long enough that the entrance is behind you and the far end is still ahead. The marks don't stop or change. They just keep going.*
*Then the tunnel goes silent in a way it wasn't silent before. One breath of stillness.*
*Then something at the far end shifts. Not loud. Not close. Just present. Aware, maybe. The marks continue toward it.*
- Keep walking → SUCCESS: *You don't slow down. Whatever is ahead has already heard you — stopping won't help and going back won't either. You walk toward the sound. The tunnel ends at a doorway. Nothing is there. Nothing was ever there, or it's somewhere you're not anymore. You walk through it. You are through.*
- Fall back → FAILURE: *You take one step back. Then another. The sound doesn't repeat but the silence that follows it is worse. You turn and move fast, faster, back toward the entrance, back toward the footprints, back toward something that made sense. You wake up at the entrance. The footprints are there. Your size. Your stride. The far end of the tunnel is very far away now.*

*B3 — The vibration leads you to a section of floor where it is strongest — a rough circle of stone, slightly discolored, slightly lower than the surrounding floor. The hum comes up through your boots and into your legs. It is steady. It is patient. It has been doing this for a long time.*
- Step onto the discolored stone → SUCCESS: *The hum rises through you the moment your full weight is on it — up through your legs, your chest, your jaw. The floor doesn't move. You do. The corridor shifts around you, or you shift through it, and then you are somewhere else. The hum is gone. The room ahead is quiet and real. You are through.*
- Kneel and press your hand to it → SUCCESS: *The vibration is different through your palm than through your boots — more specific, like a word you almost recognize.*
  *You press harder. The circle of stone depresses slightly, just enough to feel deliberate, and something in the corridor unlocks without a sound.*
  *A doorway is there that wasn't before. You stand up and walk through it. You are through.*

**On passing through:** The player arrives in the Lost Apprentice's Cell. No explanation is given for what the corridor was. The dream framing is never named in-game.

**Built (2026-10-04):** "light", not "torch" — by now the player's light may be the spell. Numbered menus, as Litlock's tree:
- Level 1: 1. Follow them, 2. Go another way. 2A: 1. Look closer at the prints, 2. Listen, 3. Breathe in. 2B: 1. Trust the feeling, 2. Look around, 3. Feel the ground.
- Level 3: A1 Press your hand against the wall / Step back and look at the full wall; A2 Follow the slope down toward the sound / Follow the draft, toward air; A3 Crouch inside and look for the source / Ignore it and keep moving; B1 Press forward into the wall / Wait and see; B2 Keep walking / Fall back; B3 Step onto the discolored stone / Kneel and press your hand to it.
- Entering (every time until passed): the inciting event and menu 1. A failure: the outcome, then the inciting event and menu 1 again. A success: the outcome, then the Cell. Other commands work as normal; `NORTH` goes back to the Spillway (the tree starts over); `SOUTH` before passing replays the inciting event and menu.
- **Once passed:** *A low, wet corridor running north and south. There are footprints in the mud, and they are only yours.*

---

### The Treasure Map

Hidden aboard the Pie Rat Ship in the hold.

Each turn aboard fires a silent perception check (Hard, 14 — the map isn't critical, only extra Zenni). On success: map found and added to inventory. Actually Enchanted Glasses pass all checks — map found on first turn.

Without the map: each `DIG` on Desert Island has a 10% chance of finding the buried chest (contains 30 Zenni). Player can keep trying indefinitely.

Carrying the map guarantees `DIG` success on Desert Island on first attempt.

---

### The Pie Rat Ship Heist

Multi-step quest chain that grants access to the Pie Rat Ship.

1. Find Pie Rat disguise in The Rat's Nest (mine).
2. Buy gunpowder from Shamus (5 Zenni).
3. Take the flint and steel from the Assay Room workbench.
4. Find the structural weak point in the Mine Tunnels (Easy perception, every visit until found), then `DROP GUNPOWDER` there.
5. `LIGHT GUNPOWDER` (flint and steel carried; gunpowder at the weak point) — fuse catches. Five turns to get out.
6. Still inside the mine (Mine Entrance, Main Shaft, Assay Room, Mine Tunnels, Rat's Nest) when it goes: death, GAME OVER.
7. Explosion — cave-in seals main mine entrance permanently.
Text (locations.md — Mine Tunnels, Mine Entrance) covers the weak point, the drop, the refusals, the fuse, the explosion and the death line.
8. Steal the ship while Pie Rats respond to explosion. Boarding needs the disguise **and** the explosion (or, later, the Pie Rat Coin) — locations.md, Pie Rat Ship — Deck, The gangplank.
9. Return the ship — Pie Rats angry but grudgingly impressed. One Pie Rat flips player a Pie Rat Coin (Trophy Case treasure item). From then on, `BOARD SHIP` works only while the player carries the coin (locations.md — Pie Rat Ship — Deck).

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

### Ty's Casino Corner — Cargo (Ship, Captain, and Crew)

Dice minigame in the northwest corner of the Tale and Ale. Ty runs the game. One round per PLAY / BET; the player can play again right away while they have the Zenni.
Built 2026-10-05 (content/cargo.py). Fair d6 — no level dice, no Lucky. The faces are shown (the "players never see numbers" rule is for skill rolls only).

**The goal:** Lock in a 6 (Ship), 5 (Captain), and 4 (Crew) in that exact order across up to 3 rolls, then score the highest possible total on the remaining two dice (the Cargo). Highest Cargo wins the round.

**Locking rules:**
- Only one die fills each slot — one 6, one 5, one 4, in sequence.
- A 5 cannot lock without a 6 already locked. A 4 cannot lock without a 6 and 5 locked.
- Extra 6s or 5s rolled before their slot is needed are rerollable — they do not lock automatically.
- Multiple sequence dice can lock in a single roll (e.g. rolling 6 and 5 on Roll 1 locks both).
- All locking is automatic — the player never decides which sequence dice to keep.

**Turn sequence:**
- Roll 1: Roll all 5 dice. Lock any sequence dice earned (6, then 5 if 6 is locked, then 4 if both are locked).
- Roll 2: Roll all unlocked dice. Lock any further sequence dice earned.
- Roll 3: Roll all unlocked dice. Lock any further sequence dice earned.
- Failure to lock all three by end of Roll 3 = score of 0 for the round.

**The Cargo decision:**
- Once 6, 5, and 4 are all locked, the remaining two dice are the Cargo (score = sum, 2–12).
- If rolls remain when the sequence is complete, the player may reroll **one or both** Cargo dice for a potentially higher score (each reroll uses a roll).
- **The rerolled result must be kept, even if lower.** This is the only player decision in the game.

**Order:** Ty rolls first, then the player — the player knows the score to beat. Ties (including both 0) are a push: stakes back.
If Ty misses 6-5-4 (scores 0) and the player makes it, the player wins outright — no reroll choice, the round settles at once.

**Ty's rerolls (decided 2026-10-05):** while rolls remain, he keeps any cargo die showing 4–6 and rerolls any showing 1–3; both 4+ means he stands. (Simulated with a player who chooses well: player wins ~38%, Ty ~37%, push ~24%.)

**Commands (the Casino Corner):**
- `PLAY CARGO [n]` / `PLAY [n]` / `BET n` / `WAGER n` start a round at stake n. `TALK TO TY` gives his intro.
- While the player's choice is open: `REROLL BOTH`, `REROLL n` (the die showing n; with a pair, one of them), `STAND`.
- Bare `REROLL`, a number not on the cargo dice, or any other command gets Ty's waiting line and uses no turn (SAVE / RESTORE / QUIT still work).

**Ty's roll dialogue:**

- *Roll 1 — locks all three immediately:* Ty looks at the dice for a moment without touching them. "Six, five, four." He sets three aside with two fingers, unhurried. "Cargo." He rolls the remaining two. He doesn't look surprised.
- *Roll 1 — no 6, gets it on Roll 2:* The first roll comes up without a six. Ty considers the dice the way a man considers weather — not concerned, just noting it. He sweeps them up. The second roll produces the six. He sets it aside. "There it is." As if it were never in doubt.
- *Roll 3 — fails to lock all three, scores zero:* The dice don't cooperate. Ty watches the last roll settle. No four. He looks at the table for a moment, then at you. "Happens." He gathers the dice. "Your turn."
- *Any other way:* Ty rolls, sets the dice aside as they come, and rolls again.
- *Rerolls one cargo die:* Ty keeps the [6] and rolls the [2] again. *Both:* Ty sweeps up both cargo dice and rolls again.
- *His score:* Ty's cargo: [N]. — then the score line below.

**Ty's score dialogue:**

- *Cargo 1–6:* "Not much cargo on that ship." He records the score without ceremony.
- *Cargo 7–12:* "Full load." A pause. "That'll be hard to beat."

**Win/loss outcomes:**

- *Player wins:* Ty looks at the scores. He slides the pot across without comment. "Well played."
- *Player loses:* Ty looks at the scores. He pulls the pot in. "Better luck." He means it plainly — no gloating.
- *Push:* Ty looks at the scores. "Push." He slides your stake back.

**The player's roll:**

- *Each roll:* First roll: 6, 2, 5, 3, 1. You set aside the six and the five. (Second / Third roll show only the dice rolled.) Nothing locked: Nothing to set aside.
- *Sequence done, rolls left:* Ship, Captain and Crew. Your cargo: 2 and 6 — 8. Reroll one, both, or stand? (on the last roll, without the question — the round settles)
- *Reroll one:* You roll the 2 again: 5. Your cargo: 6 and 5 — 11. *Both:* You roll the cargo again: 6 and 4 — 10. Rolls still left: Reroll one, both, or stand?
- *No full sequence:* No crew. Your score: 0. (or No ship / No captain — the first slot missing)
- *Bare REROLL:* Ty waits. "Both, or just the [lowest]?" (REROLL BOTH, REROLL [lowest], or STAND)
- *Anything else while choosing:* Ty waits. "Reroll or stand?" (REROLL BOTH, REROLL [lowest], or STAND)

**Stakes:** Player sets the wager each round; Ty matches it. No per-round cap. Ty starts with a bankroll of 30 Zenni; what he wins goes back into it. No lockout timer; Ty is always available to play until cleaned out.

- **No stake:** *Ty taps the table in front of you. "Stake first."* **Zero:** *"Zero's not a bet."* **More than the player has:** *Ty glances at your purse. "You don't have that."

- **Normal wager:** Ty matches without comment. Round proceeds.
- **Wager exceeds Ty's remaining bankroll:** *"I can match [X]." He sets the Zenni on the table. "That's what I've got."* Round proceeds automatically at the reduced wager.
- **Ty cleaned out:** *Ty doesn't say anything for a moment. He looks at the table, then at you, then back at the table. "You cleaned me out." A small nod, as if confirming something to himself. "I don't play on credit." He reaches for his drink and doesn't reach for the dice.* Game permanently unavailable for the rest of the playthrough.
- **Afterwards (PLAY / BET / TALK TO TY):** *Ty raises his drink an inch. "Table's closed. You saw to that."

---

### Whispering Jar (Quest 4)

Restored with wax seal + silver dust + the inscription etched into its base (`READ INSCRIPTION` — Medium perception check; Enchanted Glasses give their bonus, Actually Enchanted Glasses pass). Whispers: *"The ceiling of the thermal vent holds a secret."* Rules and text: items.md — The Whispering Jar.

Reading the inscription again repeats the whisper (no further reward). `LISTEN` afterwards: *Nothing. The jar is quiet now.* This is the only hint anywhere for the fire clay in the Thermal Vent Room (lower tier, `LOOK UP`).

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

**Round timing:** no round on the turn the player enters The Still Den. Every later turn there while the werewolf lives is one round; on a loss: *The werewolf's claws find you.* (1 heart). Ties and wins do nothing. An attack command prints its weapon failure message and is that turn's round.

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

The Rickety Bridge (between Shrine Room and Mid-Tier Key Door, upper tier) has a carry weight limit of **12**.

If inventory exceeds limit: bridge groans, and the crossing is blocked in either direction (south to the Key Door, or north back from it — same groan text). Player must drop items on the near side, cross, then return for them. Always crossable at or under limit. This is a logistical puzzle, not a trap.

**Weight scale (1–5, with two exceptions):**
- **0** — The God-Forsaken Ring (can't be dropped, so it never counts)
- **1** — tiny/negligible: rings, keys, coins, vials, scrolls, glasses, maps, paper, herbs, clothing
- **2** — small/light: torches, flutes, jars, rods, nuggets
- **3** — moderate: crowbar, pickaxe, rope, shovel, portcullis bar, runed metal, swords
- **4** — heavy: sack of salt, Chachapoyan Fertility Idol, support beam
- **5** — very heavy / not portable solo: hand cart
- **10** — gravestone (cart-only; never crosses bridge)

**Weight is invisible to the player.** No carry total is displayed. The player discovers the limit only when the bridge groans and refuses passage.

**Minimum critical load to complete the game past the bridge:** 9 (rope 3 + lantern 2 + consecrated silver stake 2 + vial of glacier melt 1 + incantation scroll 1). The limit of 12 gives 3 points of comfortable headroom while forcing players carrying heavy upper-tier items (Idol, pickaxe, sack of salt, support beam) to make deliberate choices.

---

### Trophy Case

Fixed container in The Tower (Town Hall). Treasure items are placed here permanently — they cannot be removed once deposited.

**Rules:**
- Case must be open to accept items (`OPEN CASE` first).
- `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` — registers treasure in count. Confirmation: *"The [item name] settles into the velvet. The case is a better place for it."*
- A treasure already in the case isn't counted again: *"It's already in the case."*
- `TAKE <ITEM> FROM CASE` — always returns: *"That belongs to Roundabout now."*
- `LOOK IN CASE` / `EXAMINE CASE` — lists contents and count whether open or closed (glass panels visible either way).
- **Count display:** *"[N] treasure[s] on display."* No denominator shown during play. Win condition reveals: *"9 of 9 treasures on display."*
- Treasures can be deposited at any time, as they're collected. Depositing is the only thing that changes the score: each treasure adds its points (items.md — Treasure Items table). Non-treasures are refused. Full text in locations.md — The Tower.
- The Pie Rat Coin is also the pass for re-boarding the Pie Rat ship; once it's in the case the ship can't be boarded again (no sailing is needed after the Pie Rat business).

### Score

**Score = treasure points deposited in the Trophy Case** (the only points in the design; 300 possible). The engine's Zork-style room score from Phase 1 is not shown — room visits already award XP.

**`SCORE` during play** (no denominators, no tier):
```
Score: 0
Level 6 (412 XP)
Zenni: 12
0 treasures on display.
```

**End of game** (runs automatically after Will's final scene; adds denominators and the tier title):
```
Score: 0 of 300
Level 6 (412 XP)
0 of 9 treasures on display.
Title: Empty-Handed
```
The tier title appears only at the end. The Trophy Case itself isn't built yet — until it is, score and treasures read 0.

**Treasure achievement tiers (end-game display):**
Shown at game end alongside player level. Based on total points deposited in the Trophy Case.

| Points | Title |
|--------|-------|
| 0 | Empty-Handed |
| 1–59 | Scavenger |
| 60–119 | Loot Goblin |
| 120–179 | Treasure Hunter |
| 180–239 | Plunder King |
| 240–299 | Roundabout's Unhinged Treasure Enthusiast |
| 300 | Calder Finch |

Total possible: 300 points (9 treasures). The Gold Pocket Watch (30 pts) is missable — permanently inaccessible after the Stored Room collapses. A thorough player who misses one high-value item or two low-value items will land in the 240–299 tier.

---

### Save and Restore

Decided 2026-10-05.
- `SAVE` writes the game to a file named after the character, `<name>.sav` (e.g. `Tess.sav`), in the folder the game runs from: *Saved.* Saving again overwrites it.
- `RESTORE` loads the current character's own file. A new launch always starts with character creation, so a returning player creates a character with the same name, then `RESTORE`s. No file: *There's no saved game to restore.*
- `RESTORE <name>` loads that character's file (any case): *Restored.* No file: *There's no saved game for Boromir.* Play goes on as the saved character, so later SAVEs go to that name's file.
- SAVE and RESTORE use no turn. After GAME OVER all input is refused, RESTORE included — relaunch and restore.
- A restore brings back everything, the turn count and running timers included (ring corruption, the torch, a lit fuse).
- Rooms renamed in play take their name from the game's flags, so any save restores them right, saves from before 2026-10-09 included: the Stored Room is the Hole to Below once dug, and A House is Kevry's House once Kevry is met. Restoring an earlier save brings the earlier name back.
- File names keep only letters, digits, spaces, hyphens, underscores and apostrophes; a name with none of them saves as `roundabout.sav`.
- The walkthrough tests play "Tester", so they write `Tester.sav`.

**Quitting** (decided 2026-10-09)
- `QUIT` (or `Q`) asks: *Quit now? (type "no" to save first) [yes/no]* — it doesn't save. `YES` or `Y` (any case) ends the game at once, with no exit pause. Any other answer plays on, so the player can `SAVE` and quit again.
- QUIT uses no turn and works anywhere: at West of House before the mailbox, and while Ty waits for a cargo choice.

**The end of the game** (decided 2026-10-09)
- When the game ends on its own (death, corruption, declining the adventure, the ending), the final text stays on screen with *[Press ENTER to exit]*; the game closes on ENTER. Without it, a console window opened by double-clicking the game closes before the player can read how it ended.

### Parser Verbs (Confirmed)

**Object descriptions (global):** an item has a room line (where it's first placed), an optional listing for after it's been moved, and its examine text (items.md "Examine"). `EXAMINE` shows the examine text and never changes how the item is listed; with no examine text it shows the item's room line. A moved item with no designed listing is listed as "There is a [item] here."
**Which object a word means:** when a word matches several objects, `TAKE`, `EXAMINE`, `LOAD`, `UNLOAD` and `CUT` prefer the ones not in the player's pack (e.g. `EXAMINE JAR` in the Pipe Room means the Whispering Jar, not a carried smoke jar; `CUT CORD` in the snare means the snare, not the heart necklace).
**Second object of `PUT` / `SPRINKLE` / `PRESS … ON`:** prefers what isn't in the pack (`PUT SEAL ON JAR` means the Whispering Jar, not a carried smoke jar). `DUST` and `LISTEN TO` prefer what isn't in the pack, like `TAKE`.
**`DUST [thing]`** (Quest 4): `DUST JAR` in the Pipe Room; anywhere else *There's nothing here worth dusting.* `PRESS SEAL` away from the jar: *There's nothing here to press it on.*
**`STRUGGLE` / `PULL FREE`** (also `WRIGGLE`, `SQUIRM`, `THRASH`): escapes the Trap 8 snare (Medium strength); anywhere else *Nothing happens.*
**Keys:** `UNLOCK` / `OPEN [thing] WITH KEY` when several carried keys match "key": if only one of them fits that thing, it's used without asking (cellar door — cellar key, Mid-Tier Key Door — Middle Tier Key, Keeper's Chamber door — key ring, music box — music box key).
**`GIVE [thing]` with several matches:** items meant for someone who is present are preferred (`GIVE SCROLL TO WILL` means a spell scroll, not the incantation scroll).
**`GIVE` a set:** items handed over together count as one hand-over — `GIVE STONES` / `GIVE STONE TO IVANAAR` means all three rune stones ("stones" is a word for each of them). Spell scrolls aren't a set; Will still asks which one when two are carried.
**NPC hand-overs:** an item an NPC gives the player goes straight to the inventory, with the line *[Item Name added to inventory.]* (the item's name, title case — e.g. *[Middle Tier Key added to inventory.]*). The player never `TAKE`s from an NPC.
**`GIVE` refused:** *[NPC] doesn't take the [item].* NPCs known by a title or a common noun take "The" (*The Archivist doesn't take the rubbing.*, *The clerk …*); named NPCs don't (*Will Passion …*).
**`DROP`:** *You drop the [item].* (Designed drops — e.g. the gravestone — use their own text.) Dropping something worn takes it off first, silently.
**Several objects in one command** (`DROP ALL`, `TAKE ALL`, comma lists): one result per item. A result is labelled "[item]:" only when its line doesn't already name the item (refusals, special lines).
- `TAKE ALL` (and `TAKE ALL BUT …`) leaves out what the player already carries; if nothing is left: "There's nothing here you can take." (as in Zork). `TAKE X` for a carried item still says "You already have the X."
- `DROP ALL` (and `DROP ALL BUT …`) leaves out worn items and the ring. If nothing is left: carrying nothing at all — *You are empty-handed.*; worn items other than the ring — *You'll need to remove anything you want to drop.*; only the ring (worn or not) — the ring's line, *"Bring it to me, or keep it close," Will said. You keep it close.*
- `DROP ALL BUT …` that keeps back everything droppable: *That leaves nothing to drop.* The ring's line and the worn-items line above take priority when they apply. (Decided 2026-10-05.)

**A missing tool in a full sentence:** `SEAL JOINTS WITH MORTAR` without the mortar and `MIX CLAY WITH WATER` away from the fountain give the designed lines, the same as the short forms (`SEAL JOINTS`, `MIX CLAY`). Elsewhere a missing object after WITH still gets *You can't see any [word] here!* (Decided 2026-10-05.)

**Floor listings** (decided 2026-10-05):
- An item on the floor shows its first-sight line until it has been in the player's hands (taken, bought or handed over), then its own line, else *There is a/an [item] here.*
- Plural names: *There are [item] here.* (lockpicks, Apprentice's Gloves, Bartender's Boots).
- Mass names: *There is some [item] here.* (charcoal, silver dust, bog thyme, fire clay, clay adhesive, enchanted honey, mortar compound, thin paper, runed metal).

**`LISTEN` defaults** (decided 2026-10-05; where no room or object has its own line — the Whispering Jar and the Tool Alcove do):
- Plain `LISTEN`: *You hear nothing out of the ordinary.*
- `LISTEN TO` an object: *The [object] makes no sound.* (as in Zork).
- `LISTEN TO` an NPC: *[Name] isn't saying anything right now.* LISTEN is passive: it never stands in for TALK TO, so it can't discover quests or start hand-overs.

**`PULL` / `MOVE` / `PUSH` defaults** (decided 2026-10-05; where no room or object has its own line — the Flooding Room levers, the wax seal, the Magnetic Vault's stuck items, the Supply Cache rubble do):
- `PULL` / `TUG` / `YANK` / `MOVE` a takeable object: *Moving the [object] reveals nothing.* A fixed object: *You can't move the [object].* (as in Zork).
- `PUSH` any object: *Pushing the [object] has no effect.*
- Any of them on an NPC: *[Name] wouldn't appreciate that.*

| Verb | Context |
|------|---------|
| `OPEN MAILBOX` | White House / Tale and Ale — portal to Will's Tower |
| `DIG` | Shovel required; three confirmed uses plus beach flavor |
| `LIGHT GUNPOWDER` | Pie Rat heist — requires flint and steel in inventory |
| `CAST LIGHT` | Light spell — runs continuously while in darkness, no reuse timer |
| `FISH` | Roundabout Pond; requires fishing rod |
| `TURN DIAL LEFT` / `TURN DIAL RIGHT` | Church of All altar — cycles through 7 religions |
| `BOARD SHIP` / `GET ON SHIP` / `CLIMB ABOARD` / `ENTER SHIP` | Boarding Pie Rat Ship (all synonyms) |
| `SET SAIL` / `SAIL` | Begin sailing from Docks; directional movement (`GO EAST`, `SAIL EAST`) once underway |
| `DOCK` | Going ashore — same action as `LAND` / `MOOR` / `MAKE LAND` (locations.md — Pie Rat Ship) |
| `TALK TO [NPC]` | Standard NPC interaction verb |
| `BUY DRINK` / `ORDER DRINK` | The Bar only — 2 Zenni, restores 1 heart; May refuses at full hearts |
| `BUY FOOD` / `ORDER FOOD` | The Bar only — 2 Zenni, restores 1 heart; May refuses at full hearts |
| `BUY STEW` / `ORDER STEW` | The Bar only, after Quest 40 — 2 Zenni, restores 2 hearts; May refuses at full hearts |
| `RENT ROOM` / `BUY ROOM` | The Bar only — 5 Zenni, full heal; May refuses at full hearts unless the player is inked (the room's bath clears ink) |
| `TIP MAY [#]` / `TIP MAY [#] ZENNI` | The Bar only — hint purchase; May determines tier by amount. `GIVE [#] ZENNI TO MAY` / `PAY MAY [#]` are the same |
| `LOOK AT BOARD` | Quest Board in The Bar |
| `LOOK AT STATUE` | Town Square statue — reveals seam (no roll) |
| `LOOK AT BANNER` | Viking Encampment — reveals elemental runes (Trial 2 clue) |
| `LOOK UP` / `LOOK AT CEILING` | Thermal Vent Room — reveals fire clay on ceiling (synonyms). Anywhere else it acts as a plain `LOOK`. |
| `ACTIVATE [ELEMENT] STONE` | Ritual Circle (Trial 2) — also accepts LOVE/LIFE for Heart |
| `POUR HOLY WATER ON STAKE` | Creates consecrated silver stake |
| `DRIVE STAKE INTO WEREWOLF` | Destroys undead werewolf |
| `CAST UNBIND UNDEAD` | Releases ghost in Ghost's Room (Chuckle House) |
| `CAST` (no spell) | No turn. Lists known spells in the order Light, Unbind Undead, Fireball: *Cast what? You know Light, Unbind Undead and Fireball.* / *Cast what? You know Light.* None: *You don't know any spells.* (2026-10-05) |
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
| `UNLOAD STONE` (also `UNLOAD GRAVESTONE` / `UNLOAD CART` / `UNLOAD STONE FROM CART` / `PUT STONE ON GRAVE` / `PLACE STONE` / `SET STONE` / `RETURN STONE` / `DROP STONE`) | Quest 32 — at the Graveyard, sets the gravestone back and leaves the cart |
| `USE CROWBAR ON DRAIN` (also `PRY COVER` / `REMOVE COVER WITH CROWBAR`) | Quest 25 — removes the cellar drain cover from the Kitchen top step |
| `JUMP ON PLATE` | Trap 29 — intentionally triggers Warden bell; opens the Creature Den door |
| `PRY DOOR` | Trap 33 escape — crowbar + strength check |
| `USE PORTCULLIS BAR` | Trap 19 — props portcullis open permanently |
| `CLIMB TREE` | The Old Oak — retrieves kite + rune stone |
| `LOOK AT MUSIC BOX` | Will's Tower — triggers quest discovery and hint sequence (Quest 12) |
| `READ JOURNAL` | Tip Journal — displays all active discovered quests with purchased hints |
| `REST` | Level 6+ — recovers 1 heart; 50-turn reuse; not with a live enemy in the room (Spell Mechanics — REST notes) |
| `SAVE` | Saves to `<name>.sav`, named after the character; no turn (Save and Restore) |
| `RESTORE` / `RESTORE <name>` | Loads the character's own save, or the named character's; no turn (Save and Restore) |
| `QUIT` / `Q` | Asks first; yes ends the game, anything else plays on; no turn (Save and Restore — Quitting) |
| `OPEN CASE` / `CLOSE CASE` | Trophy Case in The Tower — case must be open to place items |
| `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` | Trophy Case — places treasure permanently; case must be open |
| `LOOK IN CASE` / `EXAMINE CASE` | Trophy Case — lists contents and count; visible through glass whether open or closed |
| `TAKE <ITEM> FROM CASE` | Trophy Case — always refused: *"That belongs to Roundabout now."* |

---

### Synonym Policy

1. **Synonyms are free** — registered via `add_verb(canonical, *aliases)` in `vocabulary.py`. No new handler needed; all aliases resolve to the canonical before the parser dispatches.
2. **New canonical verbs are expensive** — each requires a `SyntaxRule` in `syntax.py` and a handler in `verbs.py`. Only introduce a new canonical when no existing verb can cover the action.
3. **Multi-word commands** (e.g., `TURN DIAL LEFT`) use `particle=` in `SyntaxRule` — not separate verb registrations.
4. **Context routing** (e.g., `BUY DRINK` vs `BUY FOOD`) is handler logic dispatching on the object noun, not separate verbs.
5. **`cast` is its own canonical** — split from `exorcise`. `cast` owns `incant`, `chant`, `spell`. `exorcise` keeps `banish`, `begone`. (`drive` is its own canonical — `DRIVE STAKE INTO WEREWOLF`, see below.)
6. **`set` ownership** — `set` is removed from `turn` aliases and assigned to `sail` so `SET SAIL` → canonical `sail`. Deliberate collision resolution.
7. **Object lists** — `TAKE BLADE AND MASK`, `DROP SHOVEL, FIRE CLAY AND AMULET`: each item resolved on its own, one line per item (verbs that take several objects). Two words for one thing (`FLINT AND STEEL`) count once.
8. **Numeric arguments** (`TIP MAY 5`) — `tip` is the canonical verb; the handler parses the trailing number from raw input. No vocabulary entry needed for the number token.

---

### Verb Canonical Map (Implementation Reference)

All Roundabout commands mapped to their canonical verb. Use this as the spec for `vocabulary.py`, `syntax.py`, and `verbs.py`.

#### Already Covered by Zork I Base — No Changes Needed

| Roundabout Command | Canonical | Notes |
|---|---|---|
| `JUMP ON PLATE` | `jump` | ✓ base verb |
| `ACTIVATE [ELEMENT] STONE` | `activate` | ✓ base verb |
| `TALK TO [NPC]` | `talk` | ✓ base verb |
| `READ SCROLL` / `READ JOURNAL` | `read` | ✓ base verb |
| `GIVE SCROLL TO WILL` | `give` | ✓ base verb |
| `TIE ROPE TO BEAM` | `tie` | ✓ base verb |
| `CLIMB DOWN ROPE` / `CLIMB UP ROPE` / `CLIMB TREE` | `climb` | ✓ base verb |
| `RUB PAPER ON ENGRAVING` | `rub` | ✓ base verb |
| `POUR HOLY WATER ON STAKE` / `POUR VIAL IN WATER` | `pour` | ✓ base verb |
| `LIGHT GUNPOWDER` | `light` | ✓ base verb |
| `TURN ON LANTERN` / `LIGHT LANTERN` | `turn` / `light` | ✓ base verbs |
| `OPEN MAILBOX` / `OPEN CASE` / `CLOSE CASE` | `open` / `close` | ✓ base verbs |
| `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` | `put` / `drop` | ✓ base verbs |
| `LOOK AT BOARD/STATUE/BANNER` / `LOOK IN CASE` | `look` + prep `at`/`in` | ✓ base verb + prep |
| `TAKE <ITEM> FROM CASE` | `take` | ✓ base verb |
| `EXAMINE CASE` | `examine` | ✓ base verb |
| `DISEMBARK` | `disembark` | ✓ base verb |
| `DIG` | `dig` | ✓ base verb |
| `HOLD TORCH NEAR ICE` | `take` (`hold` is already an alias) | ✓ synonym exists |

#### Synonym Addition to Existing Canonical

| Roundabout Command | Canonical | Change |
|---|---|---|
| `GET ON SHIP` / `CLIMB ABOARD` / `ENTER SHIP` | `board` | Add `aboard` as synonym of `board`; add `SyntaxRule(verb="climb", particle="aboard")` → `V-BOARD` |

#### New Canonical Verbs Needed

| Roundabout Command | New Canonical | Synonyms | Action |
|---|---|---|---|
| `SAIL` / `SET SAIL` / `SAIL EAST` etc. | `sail` | (remove `set` from `turn`; do not alias `set`→`sail` — parser finds first verb token) | `V-SAIL` + directional particle rules |
| `DOCK` | `dock` | `moor` | `V-DOCK` |
| `BUY DRINK` / `ORDER DRINK` / `ORDER FOOD` / `BUY STEW` / `RENT ROOM` / `BUY ROOM` | `buy` | `order`, `purchase`, `rent` | `V-BUY` (handler routes on object) |
| `TIP MAY [#]` / `TIP MAY [#] ZENNI` | `tip` | — | `V-TIP` (handler reads numeric from raw input) |
| `FISH` | `fish` | `angle` | `V-FISH` |
| `DRIVE STAKE INTO WEREWOLF` | `drive` | — | `V-DRIVE-STAKE` |
| `SWAP IDOL WITH SALT` | `swap` | `trade`, `exchange` | `V-SWAP` |
| `CLEAR BONES` / `CLEAR DRAIN` | `clear` | — | `V-CLEAR` |
| `LOAD STONE ONTO CART` | `load` | — | `V-LOAD` |
| `PRY DOOR` | `pry` | `lever`, `jimmy` | `V-PRY` |
| `USE PORTCULLIS BAR` | `use` | — | `V-USE` |
| `CAST LIGHT` / `CAST UNBIND UNDEAD` | `cast` | `incant`, `chant`, `spell` (remove these from `exorcise`) | `V-CAST` |

#### SyntaxRule Addition Only (Canonical Exists, Particle Missing)

| Roundabout Command | Canonical | SyntaxRule to Add |
|---|---|---|
| `TURN DIAL LEFT` | `turn` | `SyntaxRule(verb="turn", particle="left", ...)` → `V-TURN-DIAL` |
| `TURN DIAL RIGHT` | `turn` | `SyntaxRule(verb="turn", particle="right", ...)` → `V-TURN-DIAL` |
| `LOOK UP` / `LOOK AT CEILING` | `look` | `SyntaxRule(verb="look", particle="up", ...)` → `V-LOOK-UP` |
