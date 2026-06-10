# Enchanted Realms: One Ring — Ring Rituals

Authoritative reference for the One Ring critical path: three artifact quest lines, Church of All ritual mechanics, and Will Passion's briefing structure.
Update this file immediately when any ring quest detail is designed or changed.

---

## Overview

The One Ring quest has two phases:

1. **Retrieval:** Get the ring from Pyronicus (passive — he hands it over willingly).
2. **Binding:** Perform three rituals at the Church of All altar to bind the ring safely. Each ritual requires a different religion attuned on the altar dial, the One Ring placed on the altar, and a specific artifact found during quests. The artifact is consumed (destroyed) by the ritual.

All three rituals must be completed. The ring quest cannot be completed without them.

**Corruption note:** Placing the ring on the altar for a ritual does NOT tick corruption. The ring is being used for its intended purpose, not personal gain. This is a sacred design constraint — never change this.

---

## Will Passion's Briefing Structure

**Opening briefing (tower, first visit):**
Will tells the player to retrieve the ring from Pyronicus. No mention of rituals yet.

*"There is a ring in Roundabout. It belongs to no one and everyone, depending on how you look at it — which is part of the problem. It fell through the roof of a man named Pyronicus. He's holding it in good faith, completely unaware of what it is. He'll give it up without a fight. I need you to retrieve it. Bring it to me, or keep it close — but understand this: the ring is useful. It is also patient. And patient things have a way of getting what they want eventually."*

**Second briefing (player returns ring to Will) — CONFIRMED:**

*Will sets down his pen when he sees the ring. He doesn't reach for it.*

*"Good," he says. "Sit down."*

*He doesn't wait to see if you do.*

*"The ring can't be destroyed. I want to be clear about that — not by force, not by fire, not by anything one person or one faith could bring to bear. What's inside it is older than the methods we have for ending things."*

*He moves to the window.*

*"But three faiths together — three distinct sources of power, each contributing something the others cannot — that's another matter. There is a Church in Roundabout. The Church of All. You'll find an altar there with a dial. Seven religions. Three of them are what you need."*

*He turns back.*

*"I won't tell you which three. You'll know them when you find them. The things they ask of you will make it obvious."*

*He picks up his pen.*

*"When it's done, bring it back."*

---

## The Church of All Altar

Located in The Altar sub-room of the Church of All.

**Dial:** `TURN DIAL LEFT` and `TURN DIAL RIGHT` cycle through seven religions. Current attunement shown in room description.

**Seven religions in dial order:**
1. The Verdant Circle — *A sprouting seed inside a circle of leaves.*
2. The Veil of the Arcane — *A seven-pointed star with a void at its center.*
3. The Brotherhood of the Pale Blade — *A white sword on a black field.*
4. The Weavers of the Thread — *Three threads braided into one, ends frayed.*
5. The House of the Coin — *A coin, heads on one side, a question mark on the other.*
6. The Keepers of the Lantern — *A lit lantern with an open door.*
7. The Hearth Folk — *A fire inside a house outline, door open.*

**Ritual mechanic — CONFIRMED:**

**Sequence (any order for artifacts):**
1. Place any artifact on the altar — it sits on the stone surface. Nothing happens yet.
2. Turn dial to the matching religion — altar shimmers. Artifact glows in its color. Artifact remains on altar.
3. Repeat for the remaining two artifacts — each glows when its religion is attuned.
4. Once all three artifacts are glowing, place the ring on the altar — ritual fires. All three artifacts consumed. Ring quest advances.

**Artifact colors:**
- **The Crystal Bowl** (The Verdant Circle) → green
- **The Werewolf's Amulet** (The Veil of the Arcane) → red
- **The Pale Blade** (The Brotherhood of the Pale Blade) → white

**Wrong religion attuned:** Altar shimmers normally from dial turn, but artifact does not glow. Player keeps turning.

**Ring placed before all three artifacts are glowing:** *"Nothing happens. Something is missing from the ritual. You pick up the ring."* Ring returns to inventory automatically. Same text fires whether zero, one, or two artifacts are glowing.

**Binding ceremony text (all three artifacts glowing, ring placed):**

*The altar goes still. The three lights — green, red, white — begin to move, slowly, tracing the edge of the stone toward the ring.*

*The green reaches it first. The Crystal Bowl — patience, growth, the long memory of living things. It wraps the ring in something ancient and unhurried, the way roots find stone. The bowl glows brightly and disappears into light.*

*The red follows. The Werewolf's Amulet — arcane power, older than the names given to it. It finds the ring's hidden nature and drags it into the light where it cannot pretend to be otherwise. The amulet fades into magic.*

*The white arrives last. The Pale Blade — sacrifice, the calm acceptance of what must be given up. It seals what the others have found and named. A glint flashes off the blade, and it's gone.*

*The ring sits on the altar alone. Whatever door was open in the ring is closed. For now.*

*The ring is bound.*

**Post-ceremony:** Ring returned to player inventory in bound state. Invisibility no longer functions. Player must return bound ring to Will Passion to complete the ring quest.

**`WEAR RING` while bound:** *The ring won't go on. It simply won't.*

**Will's final scene (player returns bound ring) — CONFIRMED:**

*Will takes the ring from your hand. He holds it for a moment without looking at it — as though he's listening for something. Then, apparently satisfied, he sets it down on the desk.*

*"Good," he says.*

*He looks at you properly for the first time since you walked in.*

*"You're alive," he says. "I wasn't certain you would be. I should have told you that at the start." He pauses. "I didn't, because I needed you to go."*

*He picks up his pen.*

*"Well done."*

*He means it. You can tell because he doesn't say anything else.*

**Altar description:** Stone altar, nothing elaborate. The dial gives it a mystical quality — each turn of the dial causes the altar to shimmer.

---

## Artifact 1 — The Pale Blade
**Religion:** The Brotherhood of the Pale Blade

### Quest Chain

**Step 1 — Viking Trust Trials**
The Viking Encampment (west of Archery Range) follows The Brotherhood of the Pale Blade. Three trust trials must be completed in order:
1. Riddle Stone (Haalvar's Hut) — answer: `SEA`
2. Ritual Circle (The Ritual Circle) — correct order: Earth → Air → Fire → Water → Heart
3. Drinking Challenge (The Fire Pit) — beat Aylora at Thornbrew; drag her back to camp

**Step 2 — Runed Metal Handoff**
After Trial 3, Ivanaar Stormbringer awards the runed metal.

*"Will Passion sent you. He asked me to build something that would tell him whether you were worth trusting with what comes next. He didn't tell me what comes next."*

He holds the runed metal with both hands:

*"This is Brotherhood metal. It has been kept since before this encampment. It would make a fine blade in the right hands — a blacksmith who knows what he is looking at could tell you more."*

*"I hope Will is right about you."*

**[Runed Metal added to inventory.]**

The player must infer from Ivanaar's hint ("a blacksmith who knows what he is looking at") that the metal goes to Pyronicus.

**Step 3 — Pyronicus's Forge**
Bring runed metal to Pyronicus's Forge (below the illusory volcano). Pyronicus forges it into the Pale Blade.

**Trigger:** `GIVE METAL TO PYRONICUS` or `PUT METAL ON FORGE` (with runed metal in inventory)

*Pyronicus turns the metal over in his hands without speaking. He runs a thumb along the runes. Then he sets it on the forge.*

*"Brotherhood metal," he says. "I haven't seen this in some time." He picks up his hammer. "You know what it's for."*

*He doesn't phrase it as a question.*

*The forge does the rest quickly — the metal accepts the heat the way it has been waiting to, and Pyronicus works it with the focused economy of someone who has done this before and expects to do it again. When he's done, he holds it up. The blade is pale, almost white, and thin in the way of something that doesn't need to be heavy to do what it does.*

*He holds it out, pommel first.*

*"It will go willingly," he says. "When the time comes."*

*He goes back to his work.*

**[Runed Metal removed from inventory. The Pale Blade added to inventory.]**

**Step 4 — Ritual**
Bring the Pale Blade to the Church of All altar. Attune to The Brotherhood of the Pale Blade. Place ring + artifact on altar. Blade is consumed. Ritual complete.

### Discovery Path
- Archery Range arrow hazard → Viking Encampment (organic discovery)
- No May hint currently designed for this chain
- Player infers Pyronicus connection from Ivanaar's "blacksmith" hint

---

## Artifact 2 — The Werewolf's Amulet
**Religion:** The Veil of the Arcane

### Quest Chain

**Step 1 — Discovery (two paths)**
- **Path A (Scholar):** `TALK TO LIBRARIAN` → scholar researched the Veil of the Arcane, descended into lower passages and never returned. May tier 1 hint: *"There's talk of a scholar who went into the deep passages and never came back. The Librarian might know something about it."*
- **Path B (Keeper):** May's three-tier hints about the missing Keeper of the Faiths → locked Keeper's Chamber at Church of All.

**Step 2 — Silver Stake**
`LOOK AT STATUE` in Roundabout Town Square (no perception check — seam visible on examination). Get crowbar (Prayer Alcove, Dungeon Upper Tier). `USE CROWBAR ON STATUE BASE` → silver stake + Keeper's note with emerald wax seal. Attempting to open without crowbar: *"The base is sealed tight. Something with leverage could pry it open."*

May's backstop hint (fires only if player has not examined the statue): *"Someone was seen tampering with the statue in Roundabout Town Square. Probably nothing. Probably."*

**Step 3 — Keeper's Key Ring**
Descend to Lower Crypt (Dungeon Lower Tier, via Hole to Below). Find Keeper's skeleton under inert pendulum blade.

Room description: *A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.*

Emerald seal on cord around neck matches statue note. `TAKE KEYS`.

**Step 4 — Holy Water**
Keeper's key ring opens the Keeper's Chamber (Church of All). Inside: vial of holy water + Keeper's note explaining the scholar was transformed into an undead werewolf. `POUR HOLY WATER ON STAKE` → consecrated silver stake.

**Step 5 — Kill the Werewolf**
The Still Den (Dungeon Lower Tier, east through The Narrow Pass). `DRIVE STAKE INTO WEREWOLF` → werewolf destroyed; reverts to scholar appearance on death. Drops **Werewolf's Amulet**.

Room description: *A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. It is very still right now. That changes the moment you enter.*

Take Ivory Torch from wall before leaving (required for Quest 34).

**Step 6 — Ritual**
Bring Werewolf's Amulet to the Church of All altar. Attune to The Veil of the Arcane. Place ring + artifact on altar. Amulet consumed. Ritual complete.

### Identified Gaps (Session 2026-06-04)
- Statue seam is now guaranteed visible on `LOOK AT STATUE` — no perception check (fixed)
- May's backstop hint added for players who walk past statue without examining (fixed)
- Crowbar failure message added: *"The base is sealed tight. Something with leverage could pry it open."* (fixed)
- Keeper's skeleton room description written and confirmed (fixed)
- Werewolf's Room scholar connection — RESOLVED. Post-combat room description: *"The scholar lies where the creature fell."* Reversion text confirmed.
- Werewolf combat mechanic TBD: attack cadence, player options each turn — **BLOCKED on combat system design**
- Death/reversion text confirmed: *"The creature drops. Between one moment and the next, it is not the creature anymore. The scholar lies on the floor of the cave he came down here to find."*
- Post-combat room description confirmed (see locations.md — The Still Den)

---

## Artifact 3 — The Repaired Bowl
**Religion:** The Verdant Circle

### Quest Chain

**Step 1 — Discovery**
Perception check in Roundabout Forest reveals a crumbled shrine to The Verdant Circle. Offering bowl is smashed — three pieces scattered.

**Step 2 — Collect Three Bowl Pieces**
- Piece 1: Near the shrine in Roundabout Forest (perception check)
- Piece 2: In the bog (perception check)
- Piece 3: Dungeon Upper Tier — Shrine Room (perception check)

**Step 3 — Fire Clay**
Descend to Thermal Vent Room (Dungeon Lower Tier). `LOOK UP` reveals fire clay pressed into ceiling overhang. `TAKE CLAY`. No perception check. The Whispering Jar (Quest 4) is the only hint anywhere: *"The ceiling of the thermal vent holds a secret."*

**Step 4 — Fountain Water**
Return to Roundabout Town Square fountain. Mix fire clay with fountain water → clay adhesive. **Prerequisite:** Quest 22 (Ruined Aqueduct) must be complete — fountain only runs after aqueduct is repaired. Failure text if dry: *"The fountain is dry. You'll need clean running water."*

**Step 5 — Assemble Bowl**
Assemble three pieces using clay adhesive → The Repaired Bowl.

**Step 6 — Shrine Offering**
Return to Verdant Circle shrine in Roundabout Forest. Place repaired bowl on pedestal with Zenni coin offering. Bowl becomes ring ritual artifact — The Repaired Bowl. Full mechanic in `quests.md` (Quest 49).

**May's hints:**
- Tier 1: *"Something about that shrine bowl needs water — clean, running water. Check the Quest Board; there may be something relevant posted."*
- Tier 2: *"The town fountain hasn't run in years. Word is the aqueduct beneath the dungeon needs repair — it's on the Quest Board if you haven't seen it."*

**Step 7 — Ritual**
Bring The Crystal Bowl to the Church of All altar. Attune to The Verdant Circle. Place ring + artifact on altar. Bowl consumed. Ritual complete.

