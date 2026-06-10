# Enchanted Realms: One Ring — Items

Authoritative item reference. Every item: room description, inventory description, location found, quest use, consumable/missable flags, weight (TBD).
Update this file immediately when any item detail is designed or changed.

---

## Equipment

### The Bow
**Slot:** None (carried)
**Weight:** 1
**Location:** Awarded by Raznak at the Archery Range after Viking trust trials complete.
- **Rogues:** Raznak hands it over immediately on first interaction after trust earned — no training required, no Zenni cost.
- **Warriors / Mages:** Awarded after paying 3 Zenni for archery training.

Required to make ranged (bow) attacks in combat. Must be carried in inventory.

**First round bonus:** The opening bow attack in any combat gains +5 to the roll — advantage of distance and surprise. Subsequent rounds in the same combat have no bonus.

**Inventory description:** "A bow, plain and well-maintained, strung tight and balanced. It has the feeling of something that expects to be used correctly."

---

### The One Ring *(Core Quest Item)*
**Slot:** Ring
**Weight:** 1
**Location:** Pyronicus's Forge (retrieved from Pyronicus on first visit)
**Quest use:** Required throughout — invisibility enables Chuckle House, Spirit Room passage, and other quests. Consumed (corrupts) during the three Church of All rituals.

- Only one exists in the game.
- Grants **invisibility** while worn.
- Carries a **corruption timer** — each turn worn advances the counter. Timer pauses when removed; resumes when re-equipped. Never resets.
- Milestone messages warn as corruption progresses.
- **Late-stage removal:** At final corruption ticks, player must pass a challenge roll to remove the ring. Near-miss and clean success narrated differently.
- **Full corruption = game over (failure ending).**
- Altar use does not tick corruption — the ring is being used for its purpose, not personal gain.
- **Bound state (after binding ceremony):** Invisibility no longer functions. `WEAR RING`: *"The ring won't go on. It simply won't."* Must be returned to Will Passion to complete the ring quest.

---

### Enchanted Glasses / Actually Enchanted Glasses
**Slot:** Head
**Weight:** 1
**Location:** Will Passion's Bedroom (hidden room in the Wizard Tower)
**Inventory description (regular):** "wire-rimmed glasses"
**Inventory description (enchanted):** "slightly glowing wire-rimmed glasses"
**In Will's Bedroom after DROP:** "a pair of wire-rimmed glasses rests on the nightstand" (or "slightly glowing" if enchanted)

- Enchanted Glasses: small bonus to perception checks.
- Actually Enchanted Glasses: pass all perception checks automatically — no roll required.
- Upgraded by **Kevry Talborn** — only if already equipped (head slot) when player arrives at his island.
- **Warning:** Equipping in Will's presence triggers an instant fail state — Will attacks, no recovery. The bedroom is safe only because Will is not there.
- **End-game return:** Dropping in Will's Bedroom at end-game earns XP — double if Actually Enchanted.
- Missable only if player never finds Will's hidden bedroom.

---

### Heart Necklace
**Slot:** Neck
**Weight:** 1
**Location:** Awarded by beating Lynds at arm wrestling (Tale and Ale)
**Quest use:** None — permanent stat bonus.

Permanently adds one heart to player's maximum heart count.

---

### Crowbar
**Slot:** None (carried)
**Weight:** 3
**Location:** Prayer Alcove, Dungeon Upper Tier
**Quest use:** Quest 25 (flooded cellar drain cover), Quests 19&30 (statue base), Trap 33 escape (Idol Room stone door)

Found in a carved niche in the Prayer Alcove — perception check reveals the alcove's full depth.

---

### Guardian's Lantern
**Slot:** None (carried)
**Weight:** 2
**Location:** Dropped by The Warden (Combat Room / Creature Den, Dungeon Upper Tier)
**Quest use:** Required to dispel magical darkness in the Dark Room (lower tier). Quest 34 sub-chain gated behind it.

`TURN ON LANTERN` or `LIGHT LANTERN` both work. Flickers but does not light anywhere except the Dark Room. Hangs permanently on wall hook in Dark Room once lit there — not takeable after.

---

### Apprentice's Gloves
**Slot:** Hands
**Weight:** 1
**Location:** Reward from Quest 50 (The Lost Apprentice) — apprentice gives them on Bog-NW exit
**Quest use:** None — combat bonus.

+3 combat roll bonus. Missable — Quest 50 is inaccessible if Flooding Room trap is disarmed before triggering.

---

## Quest Items

### Treasure Map
**Weight:** 1
**Location:** Pie Rat Ship — Hold / Below Deck
**Quest use:** Guarantees `DIG` success on the Desert Island buried chest on the first attempt. Without the map: 10% chance per `DIG`.

Found via silent perception check — fires once per turn spent aboard the ship. Actually Enchanted Glasses pass all perception checks; map found on first turn. A player who sails to Kevry's island without finding the map, gets the glasses enchanted there, and returns to the ship will auto-find the map on their next turn aboard.

Not consumable — stays in inventory after use.

---

### Runed Metal
**Weight:** 3
**Location:** Awarded by Ivanaar Stormbringer after all three Viking trust trials
**Quest use:** Taken to Pyronicus's forge → forged into the Pale Blade.

Dense, rune-carved, warm to the touch even in open air. Brotherhood metal kept since before the encampment.

---

### The Pale Blade
**Weight:** 3
**Location:** Forged by Pyronicus from runed metal
**Quest use:** Ring ritual artifact — consumed at The Brotherhood of the Pale Blade ritual at the Church of All altar.

Forging scene confirmed — see `ring-rituals.md` (Artifact 1, Step 3).

---

### Werewolf's Amulet
**Weight:** 1
**Location:** Dropped by the undead werewolf in The Still Den (lower tier)
**Quest use:** Ring ritual artifact — consumed at The Veil of the Arcane ritual at the Church of All altar.

A tarnished amulet bearing the seven-pointed star of The Veil of the Arcane.

---

### The Crystal Bowl
**Weight:** 2
**Location:** Transformed from the repaired ceramic bowl at the Verdant Circle shrine (Roundabout Forest) — place repaired bowl on pedestal, then offer a Zenni coin
**Quest use:** Ring ritual artifact — consumed at The Verdant Circle ritual at the Church of All altar. See Quest 49 in `quests.md`.

**Inventory description:** *A crystal bowl, clear as still water. A continuous line is etched into the rim — looping back on itself, no beginning, no end. It has the feeling of something that has been waiting a long time to be this.*

---


### Silver Stake
**Weight:** 2
**Location:** Hollow base of the Town Square statue — crowbar opens it
**Quest use:** Must be consecrated with holy water → consecrated silver stake → `DRIVE STAKE INTO WEREWOLF`.

Found alongside a folded note signed with the Keeper's emerald wax seal.

---

### Consecrated Silver Stake
**Weight:** 2
**Location:** Created from silver stake + holy water (`POUR HOLY WATER ON STAKE`)
**Quest use:** Only weapon that destroys the undead werewolf.

---

### Holy Water
**Weight:** 1
**Location:** Vial on writing desk in Keeper's Chamber (Church of All) — Keeper's key ring required to enter
**Quest use:** Consecrates the silver stake.

---

### Keeper's Key Ring
**Weight:** 1
**Location:** On the Keeper's skeleton in the Lower Crypt (dungeon lower tier)
**Inventory description:** "A ring of keys, old iron, worn smooth from years of use."
**In-room description (on skeleton):** "The skeleton's fingers are curled loosely around a ring of keys."
**Quest use:** Opens the Keeper's Chamber in the Church of All.

After keys taken: inventory description persists — room does not revert to skeleton description.

---

### Middle Tier Key
**Weight:** 1
**Location:** Reward from Quest 32 (The Missing Gravestone) — Councilman Rowan Finch
**Quest use:** Opens the Mid-Tier Key Door in the Dungeon Upper Tier.

Left by Calder Finch. *"He left a key. Said it led to a lower level — wouldn't say what was down there."*

---

### Town Charter
**Weight:** 1
**Location:** Records Room, Town Hall — awarded by Records Room Worker after returning the pocket watch
**Quest use:** Required for Quest 27 (The Toll Bridge Operator). `GIVE CHARTER TO BOGGART` clears the bridge to the dungeon.

---

### Vial of Holy Water *(see Holy Water above)*

---

### Vial of Glacier Melt
**Weight:** 1
**Location:** Prayer Alcove, Dungeon Upper Tier (alongside crowbar)
**Quest use:** Quest 34 mid room — `POUR VIAL IN WATER` freezes the pool, player crosses freely.

---

### Ivory Torch
**Weight:** 2
**Location:** Mounted on wall in The Still Den (lower tier) — take before leaving
**Quest use:** Quest 34 — required to thaw the frozen soldier over two turns (`HOLD TORCH NEAR ICE` twice).

---

### Unbind Undead Scroll
**Weight:** 1
**Location:** Silas Bryne's desk at the Lighthouse (Roundabout Beach)
**Quest use:** Quest 17 — `CAST UNBIND UNDEAD` releases the ghost in the Chuckle House.

Mages read scroll directly (consumed). Warriors/Rogues bring to Will (consumed, spell learned). Spell reuse timer: 20 turns.

---

### Light Spell Scroll
**Weight:** 1
**Location:** Inside the locked music box in Will's Wizard Tower — key in hollow log, Bog-NW (Quest 12)
**Quest use:** Quest 12. Light spell: 10 turns duration, 20 turns reuse.

---

### Incantation Scroll
**Weight:** 1
**Location:** Reward from Quest 28 (The Archivist's Request)
**Quest use:** Quest 34 — `READ SCROLL` answers the speaking door in the Tool Alcove (lower tier). Scroll consumed.

---

### Fireball Scroll
**Weight:** 1
**Location:** Reward from Quest 7 (The Bone Flute) — given by Pyronicus
**Quest use:** Castable in combat.

---

### Rope
**Weight:** 3
**Location:** Docks (coil of rope on a bollard — visible, takeable)
**Quest use:** `TIE ROPE TO BEAM` in the Stored Room (Hole to Below, mid-tier) enables bidirectional travel to lower tier. One item in the world.

---

### Shovel
**Weight:** 3
**Location:** Pie Rat Ship — Deck (lashed to rail near bow; takeable once aboard post-heist)
**Quest use:** Three confirmed uses: (1) Stored Room collapse → Hole to Below; (2) Desert Island buried chest; (3) Quest 50 — finish hole to Bog-NW from Lost Apprentice's Cell.

**In-room description:** *A shovel is lashed to the rail near the bow, practical and out of place at the same time.*
**Inventory description:** *A sturdy shovel, slightly salt-pitted. It has clearly spent time at sea.*

Will Passion 1-in-20 chance of audio note on any `DIG` command.

---

### Crowbar *(see Equipment above)*

---

### Wax Seal
**Weight:** 1
**Location:** Display cabinet, Town Hall Upper Hall — `OPEN CABINET`, `TAKE SEAL`. No perception check.
**Quest use:** Quest 4 (The Whispering Jar) — `PRESS SEAL` on the jar as part of the restoration sequence.

---

### Silver Dust
**Weight:** 1
**Location:** Mine Passage, Dungeon Mid-Tier — perception check required
**Quest use:** Quest 4 — `DUST JAR` as part of the Whispering Jar restoration.

---

### Bone Flute
**Weight:** 1
**Location:** Cave Creature's Lair, Dungeon Mid-Tier (off Inscription Chamber)
**Quest use:** Quest 7 — return to Pyronicus for fireball scroll reward.

---

### Music Box Key
**Weight:** 1
**Location:** Hollow log in Bog-NW — perception check to find hollow log
**Quest use:** Quest 12 — opens the locked music box in Will's Wizard Tower.

---

### Pie Rat Disguise
**Weight:** 1
**Location:** The Rat's Nest, Pie Rats Mining Inc.
**Quest use:** Required for the Pie Rat Ship heist (board ship while crew is distracted by explosion).

---

### Pie Rat Coin
**Weight:** 1
**Location:** Flipped by a Pie Rat after the player returns the stolen ship
**Quest use:** None — treasure item.

---

### Town Charter *(see above)*

---

### Pocket Watch
**Weight:** 1
**Location:** Dropped by ghost in Ghost's Room, Chuckle House (after `CAST UNBIND UNDEAD`)
**Quest use:** Quest 17 — deliver to Records Room Worker → receives town charter in thanks.

Also: a separate gold pocket watch hangs from the skeleton's finger in The Crevice (mid-tier dungeon) — Trophy Case treasure item, **missable** (The Crevice is permanently inaccessible after the Stored Room collapses).

---

### Hand Cart
**Weight:** 5
**Location:** Storage Area, Dungeon Upper Tier
**Quest use:** Quest 32 — needed to move Calder Finch's heavy gravestone from the bog back to the cemetery.

---

### Gravestone (Calder Finch)
**Weight:** 10
**Location:** Face-down in the bog — perception check to find
**Quest use:** Quest 32 — return to cemetery. Requires hand cart. `LOAD STONE ONTO CART` to move.

---

### Thin Paper
**Weight:** 1
**Location:** Purchased from vendor (2 Zenni). Destroyed if player gets wet — reappears for sale.
**Quest use:** Quest 28 — `RUB PAPER ON ENGRAVING` in Inscription Chamber with charcoal → produces rubbing for archivist.

---

### Charcoal
**Weight:** 1
**Location:** Mine Passage, Dungeon Mid-Tier — no perception check needed
**Quest use:** Quest 28 — used with thin paper to produce rubbing.

---

### Smoke Jar
**Weight:** 2
**Location:** Supply Room, Dungeon Upper Tier — behind Trap 17 (unstable shelf of clay pots)
**Quest use:** Quest 24 — holding smoke jar pacifies bees in swarm room.

---

### Sack of Salt
**Weight:** 4
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** `SWAP IDOL WITH SALT` — safe weight swap for Chachapoyan Fertility Idol pedestal (Trap 33).

---

### Portcullis Bar
**Weight:** 3
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** Props the Portcullis Corridor gate permanently open (Trap 19).

---

### Mortar Compound
**Weight:** 2
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** Quest 22 (The Ruined Aqueduct) — seals the stone blocks in the gap.

---

### Support Beam
**Weight:** 4
**Location:** Storage Area, Dungeon Upper Tier
**Quest use:** Quest 38 — props the cleared passage in Collapsed Gallery, makes shortcut permanent.

---

### Pickaxe
**Weight:** 3
**Location:** Main Shaft, Pie Rats Mining Inc. — leaning against the wall, no perception check needed.
**Quest use:** Quest 38 — required to clear the three timbers in Collapsed Gallery (three strength checks).

---

### Gunpowder
**Weight:** 2
**Location:** Purchased from Shamus (5 Zenni)
**Quest use:** Pie Rat Ship heist — `DROP GUNPOWDER` at structural weak point in mine, `LIGHT GUNPOWDER` to trigger explosion.

---

### Mine Torch
**Weight:** 2
**Location:** Torch sconces in Mine Tunnels
**Quest use:** Pie Rat Ship heist light source. Immediately begins 40-turn burnout timer on pickup — burnout is a fail state. Take last before lighting gunpowder.

---

### Fishing Rod
**Weight:** 2
**Location:** Purchased from Shamus (8 Zenni)
**Quest use:** Roundabout Pond — `FISH` to retrieve the bottle from the pond floor.

---

### Lockpicks
**Weight:** 1
**Location:** Looted from the Back Alley mugger after defeating him
**Use:** Opens the large iron chest in Mine Passage (contains 20 Zenni). Not a quest item; not a general trap disarm tool.

---

### Fire Clay
**Weight:** 1
**Location:** Thermal Vent Room ceiling (lower tier) — invisible until `LOOK UP`; `TAKE CLAY` retrieves it
**Quest use:** Quest 49 — mixed with fountain water to make clay adhesive for reassembling the shrine bowl.

---

### Verdant Circle Shrine Bowl (3 pieces)
**Weight:** 1 each
**Locations:**
1. Near the shrine in Roundabout Forest (perception check)
2. In the bog (perception check)
3. Dungeon Upper Tier — Shrine Room (perception check)
**Quest use:** Quest 49 — assemble with fire clay + fountain water → Repaired Bowl.

---

### Bee Queen (Glass Vial)
**Weight:** 1
**Location:** Near the nest in the swarm room (Quest 24)
**Quest use:** Quest 24 — return to beekeeper for enchanted honey reward.

---

### Enchanted Honey
**Weight:** 1
**Location:** Reward from Quest 24 (The Beekeeper's Swarm)
**Quest use:** Consumable — restores 2 hearts when consumed.

---

### Rune Stones (3)
**Weight:** 2 each
**Locations:**
1. **Bog rune stone:** Bog-NE (perception check) — *A grey stone, heavy for its size, one face worn flat by water. Faint lines are etched across the surface in no pattern you recognize.*
2. **Dungeon rune stone:** Inscription Chamber, mid-tier (perception check) — *A pale stone, roughly square, with deep natural veins of darker mineral running through it like old script.*
3. **Old Oak rune stone:** Reward from Quest 41 (The Child's Kite) — *A small flat stone, dark and smooth, threaded on a cord. Mineral veins run through it in a pattern that looks almost intentional.*
**Quest use:** Quest 42 (The Brotherhood Stones) — deliver all three to Ivanaar at the Viking Encampment.

---

### Ivanaar's Tunic
**Slot:** Chest
**Weight:** 1
**Location:** Reward from Quest 42 (The Brotherhood Stones) — Ivanaar restores the runes and gives the tunic on delivery of all three stones.
**Quest use:** None — combat bonus.

Brotherhood weave, old but not worn. The runes along the hem and collar are faint until the stones are delivered — restored by Ivanaar on completion.

**Damage avoidance:** When the enemy wins a combat round, the tunic rolls 1d10 silently. Result of 7–10 (40%) negates the damage. Fixed — does not scale with player level. On a successful avoidance, one of four flavor messages fires at random:

1. *The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.*
2. *For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.*
3. *The runes along the collar catch the light briefly. You are less hurt than you expected to be.*
4. *Something in the weave absorbed it. You felt the impact — and then didn't.*

---

### Bog Thyme
**Weight:** 1
**Location:** Bog-SW — perception check required
**Quest use:** Quest 40 (Shamus's Recipe) — deliver with clay pot to Shamus for hearty stew menu upgrade.

---

### Small Clay Pot
**Weight:** 1
**Location:** Supply Room, Dungeon Upper Tier — visible in wreckage of Trap 17 (clay pot shelf) whether trap is triggered or disarmed. The one intact pot that survives the collapse.
**Quest use:** Quest 40 — Shamus's pots are all cracked; needs this to cook the hearty stew.

---

### Tip Journal
**Weight:** 1
**Location:** Purchased from Shamus (5 Zenni)
**Quest use:** None — flavor item. Contains in-world tips and observations.

---

### Lockpicks *(see above)*

---

## Treasure Items (Trophy Case)

All high-value items. Delivered to the Trophy Case in Town Hall Tower.

| Item | Location | Weight | Points | Notes |
|------|----------|--------|--------|-------|
| **Diamond Brooch** | Magnetic Vault, Dungeon Mid-Tier | 1 | TBD | Second most valuable treasure in game |
| **Chachapoyan Fertility Idol** | Idol Room, Dungeon Upper Tier | 4 | TBD | Safe swap required (sack of salt); same weight as sack of salt |
| **Funeral Mask of Hammered Gold** | Burial Chamber, Dungeon Lower Tier | 3 | TBD | Spirits do not react to taking it |
| **The Forgotten Blade** | Quest 34 Fountain Room, Dungeon Lower Tier | 3 | TBD | Not a combat weapon; ceremonial only |
| **Golden Dragon Scale** | Reward from returning dragon-nip to Will | 1 | TBD | Dragon-nip hidden under nightstand in Will's Bedroom |
| **Ship-in-a-Bottle** | Roundabout Pond (fishing rod + challenge roll) | 2 | TBD | May's hints imply Kevry connection |
| **Gold Pocket Watch** | The Crevice, Dungeon Mid-Tier | 1 | TBD | **Missable** — permanently inaccessible after Stored Room collapses |
| **Gold Nugget** | Supply Cache, Dungeon Mid-Tier Trap Side | 2 | TBD | Buried in rubble |
| **Pie Rat Coin** | Flipped by a Pie Rat after returning the stolen ship | 1 | TBD | Unusual currency; pirate provenance |
