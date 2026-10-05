# Roundabout: The God-Forsaken Ring — Items

Authoritative item reference. Every item: room description, inventory description, location found, quest use, consumable/missable flags, weight. Weight scale in `mechanics.md` — Weight System section.
Update this file immediately when any item detail is designed or changed.

---

## Equipment

### The Bow
**Slot:** None (carried)
**Weight:** 1
**Location:** Awarded by Raznak at the Archery Range after Viking trust trials complete.
- **Rogues:** Raznak hands it over immediately on first interaction after trust earned — no training required, no Zenni cost.
- **Warriors / Mages:** Awarded after paying 3 Zenni for archery training.

Required to make ranged (bow) attacks in combat. `SHOOT` equips it (mechanics.md — Equipping weapons); it can't be worn.

**First round bonus:** The opening bow attack in any combat gains +5 to the roll — advantage of distance and surprise. Subsequent rounds in the same combat have no bonus.

**Inventory description (examine):** "A bow, plain and well-maintained, strung tight and balanced. It has the feeling of something that expects to be used correctly." Handed straight to the player — *[Bow added to inventory.]*

---

### The God-Forsaken Ring *(Core Quest Item)*
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
**Name vs. description:** "Enchanted Glasses" and "Actually Enchanted Glasses" (after Kevry's enchantment) are the item's names in design docs and walkthroughs. In-game text uses the descriptions below.
**Weight:** 1
**Location:** Will Passion's Bedroom (hidden room in the Wizard Tower)
**Inventory description (regular):** "wire-rimmed glasses"
**Inventory description (enchanted):** "slightly glowing wire-rimmed glasses"
**In Will's Bedroom after DROP:** "a pair of wire-rimmed glasses rests on the nightstand" (or "slightly glowing" if enchanted)

- Enchanted Glasses: small bonus to perception checks.
- Actually Enchanted Glasses: pass all perception checks automatically — no roll required.
- Upgraded by **Kevry Talborn** — automatically on arrival if worn (head slot); if only carried, putting them on in front of him triggers it.
- **Warning:** Equipping in Will's presence triggers an instant fail state — Will attacks, no recovery. The bedroom is safe only because Will is not there.
- **Fail text:** *Will looks up from his desk. His eyes go to the glasses on your face and stay there. For a moment nothing in the room moves. Then he is out of his chair, and whatever happens next, you don't see it coming.* — then GAME OVER. Fires when the player arrives in the tower wearing them or puts them on there.
- **End-game return:** Dropping in Will's Bedroom (`DROP GLASSES` or `PUT GLASSES ON NIGHTSTAND`) completes Quest 53 the first time — double XP if Actually Enchanted. Text: *You set the glasses back on the nightstand, where they were.*
- Missable only if player never finds Will's hidden bedroom.

---

### Dragon-Nip
**Weight:** 1
**Location:** Will Passion's Bedroom, under the nightstand (Hard perception check — locations.md)
**Inventory description:** "glowing sprig"
**Parser names:** dragon-nip, sprig, nip
**Examine:** *A small sprig, three narrow leaves on a woody stem, giving off a faint golden glow. It smells of smoke and something sweet.*
**Quest use:** Quest 58 — give to Will Passion for the Golden Dragon Scale. Consumed (Will keeps it). Never explained.

---

### Heart Necklace
**Slot:** Neck
**Examine:** *A simple cord with a clay charm, worn smooth.*
**Weight:** 1
**Location:** Awarded by beating Lynds at arm wrestling (Tale and Ale)
**Quest use:** None — permanent stat bonus.

Adds one heart to the player's maximum heart count **while worn** (neck slot). Removing it takes the heart away again.

---

### Dagger
**Slot:** None (carried)
**Weight:** 1
**Location:** Purchased from Shamus (Kitchen, Tale and Ale) — 5 Zenni
**Quest use:** None — combat weapon.
**Skill required:** Weapon Use (Warriors always; Mages/Rogues after Quest 54)

Combat bonus: +2 to melee roll. Without Weapon Use skill, carries in inventory but provides no bonus.

**Inventory description:** "A short blade, plain-handled and well-balanced. Nothing fancy about it."

---

### Mace
**Slot:** None (carried)
**Weight:** 2
**Location:** Purchased from Shamus (Kitchen, Tale and Ale) — 25 Zenni
**Quest use:** None — combat weapon.
**Skill required:** Weapon Use (Warriors always; Mages/Rogues after Quest 54)

Combat bonus: +4 to melee roll. Without Weapon Use skill, carries in inventory but provides no bonus.

**Inventory description:** "A heavy flanged mace, solid iron head, leather-wrapped grip. It has the look of something that settles arguments."

---

### Battle Axe
**Slot:** None (carried)
**Weight:** 3
**Location:** Purchased from Shamus (Kitchen, Tale and Ale) — 100 Zenni
**Quest use:** None — combat weapon.
**Skill required:** Weapon Use (Warriors always; Mages/Rogues after Quest 54)

Combat bonus: +6 to melee roll. Without Weapon Use skill, carries in inventory but provides no bonus.

**Inventory description:** "A broad-headed battle axe, balanced for a two-handed swing. Shamus keeps it behind the counter. It is not subtle."

---

### Crowbar
**Slot:** None (carried)
**Weight:** 3
**Examine:** *A heavy iron crowbar, one end flattened to a lip. Made for getting into things.*
**Location:** Prayer Alcove, Dungeon Upper Tier
**Quest use:** Quest 25 (flooded cellar drain cover), Quests 19&30 (statue base), Trap 33 escape (Idol Room stone door)

Found in a carved niche in the Prayer Alcove — perception check reveals the alcove's full depth.

---

### Guardian's Lantern
**Room description (dropped):** *An old lantern lies on the floor, its glass faintly green.*
**Examine:** *A guard's lantern, heavy brass, the glass tinted a faint green. It flickers when you lift it, as if it wants to light and can't decide where.*
**Slot:** None (carried)
**Weight:** 2
**Location:** Dropped by The Warden in the Combat Room (Dungeon Upper Tier)
**Quest use:** Required to dispel magical darkness in the Dark Room (lower tier). Quest 34 sub-chain gated behind it.

`TURN ON LANTERN` or `LIGHT LANTERN` both work. Flickers but does not light anywhere except the Dark Room — it is not a substitute for a torch or Light spell in ordinary dark rooms. In the Dark Room, it collapses magical darkness instantly and opens the passage south. Hangs permanently on wall hook in Dark Room once lit there — not takeable after.

**Lit anywhere else:** *The lantern flickers, as if it wants to light and can't decide where. Not here, apparently.*

---

### Torch
**Weight:** 2
**Location:** Purchased from Shamus (Kitchen, Tale and Ale) — 3 Zenni
**After burnout:** inventory name *burnt-out torch*; examine *A burnt-out torch, cold and black at the end.*
**Quest use:** None — primary early-game light source for dungeon and Secret Tunnels.

Always lit from purchase. Timer starts on first dark room entry (not on purchase). 100-turn burnout — game over on expiry. One torch at a time in inventory; Shamus swaps at 69 turns remaining or below. Full mechanic in `mechanics.md` — Lighting System section.

---

### Apprentice's Gloves
**Slot:** Hands
**Weight:** 1
**Location:** Reward from Quest 50 (The Lost Apprentice) — apprentice gives them on Bog-NW exit
**Quest use:** None — combat bonus.

+3 combat roll bonus. Missable — Quest 50 is inaccessible if Flooding Room trap is disarmed before triggering. Straight to the inventory from the apprentice.

---

### Bartender's Boots
**Slot:** Legs
**Weight:** 1
**Examine:** *Tall leather boots, salt-stained, soft at the ankle. Someone wore these into worse than a cellar and walked back out.*
**Location:** Reward from Quest 25 (The Flooded Cellar) — May gives them on the next `TALK TO MAY` after the cellar drains.
**Quest use:** None — trap disarm bonus.

+3 trap disarm roll bonus. Flavor on receipt: *"forgot I had these, should have given them to you BEFORE you cleaned up the cellar."* Full line in `npcs.md` — May.

---

### Cellar Key
**Weight:** 1
**Examine:** *An iron key, rust-bloomed, on a loop of string gone grey.*
**Location:** May gives it on `TALK TO MAY` while the player carries the crowbar (Quest 25).
**Quest use:** Quest 25 — unlocks the cellar door in the Kitchen. Stays in the lock once used (never returns to inventory).

---

### Cashbox (Cellar Zenni Cache)
**Room description:** *A rusted tin cashbox sits on a high shelf, above the old waterline.*
**Location:** Cellar/Storeroom — visible once the cellar is drained.
**Quest use:** Quest 25 cache. `OPEN CASHBOX` → 10 Zenni: *The lid gives on the third try. Inside, wrapped in oilcloth and perfectly dry: 10 Zenni. Somebody planned for the flood better than they planned for the drain.*

---

## Quest Items

### Treasure Map
**Weight:** 1
**Location:** Pie Rat Ship — Deck (the ship has no hold)
**Examine:** *A hand-drawn map on oilcloth. A small island south of the sea lane, east of Roundabout, with a dotted line up the beach and an X near the trees.*
**Quest use:** Guarantees `DIG` success on the Desert Island buried chest on the first attempt. Without the map: 10% chance per `DIG`.

Found via silent perception check (**Hard, 14** — not critical, only extra Zenni).
The check fires once per turn spent aboard the ship. Found text in locations.md (Pie Rat Ship — Deck). Actually Enchanted Glasses pass all perception checks; map found on first turn. A player who sails to Kevry's island without finding the map, gets the glasses enchanted there, and returns to the ship will auto-find the map on their next turn aboard.

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

**On the shrine pedestal:** *A crystal bowl sits on the pedestal, clear as still water.*
**Inventory description:** *A crystal bowl, clear as still water. A continuous line is etched into the rim — looping back on itself, no beginning, no end. It has the feeling of something that has been waiting a long time to be this.*

---


### Silver Stake
**Weight:** 2
**Examine:** *A slim stake of solid silver, the point still sharp. Someone hid this deliberately.*
**Location:** Hollow base of the Town Square statue — crowbar opens it
**Quest use:** Must be consecrated with holy water → consecrated silver stake → `DRIVE STAKE INTO WEREWOLF`.

Found alongside a folded note signed with the Keeper's emerald wax seal.

---

### Consecrated Silver Stake
**Weight:** 2
**Location:** Created from silver stake + holy water (`POUR HOLY WATER ON STAKE`)
**Quest use:** Only weapon that destroys the undead werewolf.
**Examine / inventory:** *A slim stake of solid silver, the point still sharp. It holds a faint, steady sheen that has nothing to do with the light.*

`POUR HOLY WATER ON STAKE` (both carried; works anywhere; the vial is used up): *You unstop the vial and pour it slowly along the stake, end to end. The silver drinks it — there's no other word for it. When the last drop is gone, the metal holds a faint, steady sheen, as if lit from somewhere you can't see.*
Pouring it without the stake, or onto anything else: *You'd rather not waste it.*

---

### Holy Water
**Weight:** 1
**Location:** Vial on writing desk in Keeper's Chamber (Church of All) — Keeper's key ring required to enter
**Quest use:** Consecrates the silver stake.
**Examine / inventory:** *A small glass vial of clear water, stoppered and sealed with a dab of green wax.*
On the desk, the Keeper's Chamber room description covers it.

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
**Examine:** *A heavy iron key, its bow worked into the shape of a finch in flight. The teeth are worn smooth at the tips.*
**Location:** Reward from Quest 32 (The Missing Gravestone) — Councilman Rowan Finch holds it out; straight to the inventory — *[Middle Tier Key added to inventory.]*
**Quest use:** Opens the Mid-Tier Key Door in the Dungeon Upper Tier.

Left by Calder Finch. *"He left a key. Said it led to a lower level — wouldn't say what was down there."*

---

### Town Charter
**Weight:** 1
**Location:** Records Room, Town Hall — awarded by Records Room Worker after returning the pocket watch
**Examine:** *A rolled document tied with faded ribbon. The town seal is pressed into the wax at the bottom, and the handwriting is the careful kind that expects to be read for a long time.*
**Quest use:** Required for Quest 27 (The Toll Bridge Operator). `GIVE CHARTER TO BOGGART` clears the bridge to the dungeon.
**After Quest 27:** the Boggart hands it back, so it stays in the inventory. It has no further use; the player can drop it anywhere. (Decided 2026-10-05.)

---

### Vial of Holy Water *(see Holy Water above)*

---

### Vial of Glacier Melt
**Examine:** *A stoppered vial of water so cold the glass has frosted. It doesn't warm in your hand.*
**Weight:** 1
**Location:** Prayer Alcove, Dungeon Upper Tier (alongside crowbar)
**Quest use:** Quest 34 mid room — `POUR VIAL IN WATER` freezes the pool, player crosses freely. Used up.

---

### Ivory Torch
**Weight:** 2
**Nature:** a source of magical heat, not light — it never lights a dark room (the Light spell is still needed).
**Room description:** *An ivory torch is set in an iron bracket on the wall. There's no flame at its head, but the air around it shimmers with heat.*
**Examine:** *A torch with a shaft of carved ivory, yellowed with age. Its head has never been lit — it doesn't need to be. Heat pours off it, steady and impossible, enough to make your hand ache if you hold it close.*
**`LIGHT IVORY TORCH`:** *It doesn't need lighting. The heat is already there.*
**Location:** Mounted on wall in The Still Den (lower tier) — take before leaving
**Quest use:** Quest 34 — required to thaw the frozen soldier over two turns (`HOLD TORCH NEAR ICE` / `MELT ICE WITH TORCH` twice). Not needed afterwards.

---

### Unbind Undead Scroll
**Weight:** 1
**Room description (on the desk):** *A scroll lies on the desk, weighted at one corner with a smooth stone.*
**Inventory description:** *A spell scroll headed Unbind Undead, in a cramped, careful hand.*
**Location:** Silas Bryne's desk at the Lighthouse (Roundabout Beach)
**Quest use:** Quest 17 — `CAST UNBIND UNDEAD` releases the ghost in the Chuckle House.

Mages read scroll directly (consumed). Warriors/Rogues bring to Will (consumed, spell learned). Spell reuse timer: 20 turns.

---

### Light Spell Scroll
**Weight:** 1
**Location:** Inside the locked music box in Will's Wizard Tower — key in hollow log, Bog-NW (Quest 12)
**Room description (in the open music box):** *A folded scroll lies in the music box.*
**Examine:** *A spell scroll headed Light, in a small, quick hand.*
**Quest use:** Quest 12 (finding it completes the quest). Teaches the Light spell — mechanics.md (Light Spell).

---

### Incantation Scroll
**Weight:** 1
**Location:** Reward from Quest 28 (The Archivist's Request)
**Quest use:** Quest 34 — `READ SCROLL` answers the speaking door in the Tool Alcove (lower tier). Not used up; it can be left behind once the door is open.
**Received:** straight to the inventory from the Archivist — *[Incantation scroll added to inventory.]*
**Examine:** *A rolled scroll, the paper gone soft with age. The writing runs in close, even lines in no script you know — and yet the words sit easily in your mouth when you look at them.*
**`READ SCROLL` anywhere but the speaking door:** *You read the words under your breath. Nothing answers. Wherever these are meant to be spoken, it isn't here.* A use-item scroll — any class can read it.

---

### Fireball Scroll
**Weight:** 1
**Location:** Reward from Quest 7 (The Bone Flute) — given by Pyronicus, straight to the inventory.
**Examine:** *A spell scroll headed Fireball, in a heavy, slanted hand. The paper is warm to the touch.*
**Quest use:** Spell scroll — teaches Fireball (castable in combat). Warriors and Rogues take it to Will (resistance and teaching rules in mechanics.md).

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

### The Whispering Jar
**Location:** Pipe Room, Tale and Ale (fixed in place).
**Room description:** *A cracked ceramic jar sits on the side table, humming faintly to itself.*
**Examine:** *A ceramic jar, glazed blue-grey, a crack running from lip to base. It hums — a low, steady note you feel more than hear. Letters are etched around its base, worn almost smooth.* (First look discovers Quest 4.)
**Quest use:** Quest 4 — restored with the wax seal, silver dust and the inscription etched on its base.

**Built (2026-10-04):** steps go in order — seal, dust, read. The seal and the dust are used up.
- **`PRESS SEAL`** (also `PRESS SEAL ON JAR`, `PUT SEAL ON JAR`): *You press the wax seal over the crack. The wax gives, then takes — it spreads along the line of the crack and sets, red against the blue-grey glaze. The hum steadies.* Then: *Something clinks inside the jar. Five Zenni sit in the bottom, kept there by the crack until now. You pocket them.* (The quest's 5 Zenni.)
- **`DUST JAR`** (also `SPRINKLE DUST ON JAR`, `PUT DUST ON JAR`): with no silver dust — *You have nothing to dust it with.* Before the seal — *The dust would only sift into the crack.* After — *You sprinkle the silver dust over the jar. It clings to the glaze and settles into the etched letters around the base, and for a moment the whole jar glints.*
- **`READ INSCRIPTION`** (also `READ LETTERS` / `ETCHING` / `WORDS` / `BASE` / `JAR`): Medium perception check every time. Failed: *The letters are worn almost smooth. You can't make them out.* Before seal and dust: *Around the base, worn almost smooth: "Hold what was heard. Speak what was held." You say the words aloud. The jar hums on, unchanged.* After both (Quest 4 completes; the same text on every later read): *You read the words around the base aloud: "Hold what was heard. Speak what was held." The hum rises, wavers, and stops. In the silence, a voice no louder than breath: "The ceiling of the thermal vent holds a secret." Then nothing.*
- **`LISTEN`** / **`LISTEN TO JAR`:** before — *A low, steady hum. Up close, it almost sounds like a voice holding a single note.* After — *Nothing. The jar is quiet now.*
- **Restored room line:** *A mended ceramic jar sits on the side table, quiet.*
- **Restored examine:** *A ceramic jar, glazed blue-grey, its crack sealed with red wax. A fine silver shimmer clings to the letters around its base. It doesn't hum any more.*
- "Inscription" also names the Inscription Chamber engraving (mid-tier); the two never share a room.

---

### Wax Seal
**Weight:** 1
**Location:** Display cabinet, Town Hall Upper Hall — `OPEN CABINET`, `TAKE SEAL`. No perception check. (Cabinet text in locations.md — Upper Hall.)
**Room description (open cabinet):** *A wax seal sits among the documents in the open cabinet.*
**Examine:** *A disc of old red wax, still soft enough to press. The town crest is stamped into its face.*
**Quest use:** Quest 4 (The Whispering Jar) — `PRESS SEAL` on the jar as part of the restoration sequence. Used up.

---

### Silver Dust
**Weight:** 1
**Location:** Mine Passage, Dungeon Mid-Tier — perception check required
**Quest use:** Quest 4 — `DUST JAR` as part of the Whispering Jar restoration. Used up.
**Room description (once found):** *A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.*
**`TAKE SILVER DUST`:** *You pinch the silver dust out of the crack and pocket it.*
**Examine:** *A pinch of fine silver dust. It catches the light even down here.*

---

### Bone Flute
**Weight:** 1
**Location:** Cave Creature's Lair, Dungeon Mid-Tier (off Inscription Chamber)
**Quest use:** Quest 7 — return to Pyronicus for fireball scroll reward.
**Room description:** *Among the bones lies one that's been hollowed and pierced along its length — a flute.*
**Examine:** *A flute carved from a long, pale bone, finger holes drilled along its length. Someone made this with care. It wasn't the creature.*

---

### Rubbing
**Weight:** 1
**Location:** Made in the Inscription Chamber — `RUB PAPER ON ENGRAVING` (uses up the thin paper and the charcoal); goes straight to the inventory.
**Examine:** *A charcoal rubbing of the engraving — pale characters on a black ground. You still can't read a word of it.*
**Quest use:** Quest 28 — give to the Archivist.

---

### Diamond Brooch
**Weight:** 1
**Location:** Inside the chest in the Magnetic Vault (mid-tier) — behind Trap 15.
**Room description (in the open chest):** *In the open chest lies a diamond brooch.*
**Examine:** *A brooch of worked silver set with a single diamond the size of a thumbnail. Even in this light it throws sparks.*
**Treasure:** 45 points.

---

### Music Box Key
**Weight:** 1
**Location:** Hollow log in Bog-NW — Medium perception check to find the log (log text in locations.md)
**Examine:** *A small brass key, green at the edges, with a bow shaped like a treble clef.*
**Quest use:** Quest 12 — opens the locked music box in Will's Wizard Tower. Stays in the lock once used.

---

### Pie Rat Disguise
**Weight:** 1
**Location:** The Rat's Nest, Pie Rats Mining Inc.
**Quest use:** Required for the Pie Rat Ship heist (board ship while crew is distracted by explosion).

---

### Pie Rat Coin
**Weight:** 1
**Location:** Flipped by a Pie Rat after the player returns the stolen ship (scene text in locations.md — Pie Rat Ship — Deck). Lands on the boards in the player's room.
**Room description:** *A Pie Rat Coin lies on the boards.*
**Examine:** *A heavy coin stamped with a grinning rat in a tricorn hat. It isn't money anywhere you know of.*
**Quest use:** Treasure item. Also the player's pass back aboard: after the ship is returned, `BOARD SHIP` works only while the coin is carried.

---

### Buried Chest (Desert Island)
**Room description:** *A salt-crusted chest sits in the hole you dug.* Once emptied: *An empty chest sits in the hole you dug.*
**Location:** Desert Island — buried; revealed by `DIG` (shovel required; treasure map guarantees it, otherwise 10% per dig — text in locations.md).
**Use:** Zenni cache, like the Cellar cashbox. Fixed in place. `OPEN CHEST` pockets the Zenni directly — no `TAKE ZENNI`: *The hinges complain, but the lid comes up. Inside, wrapped in oilcloth: 30 Zenni. You pocket them.*
Opening it again: *The chest is open, and empty.*

---

### Town Charter *(see above)*

---

### Pocket Watch
**Weight:** 1
**Location:** Dropped by ghost in Ghost's Room, Chuckle House (after `CAST UNBIND UNDEAD`)
**Quest use:** Quest 17 — deliver to Records Room Worker → receives town charter in thanks.

Also: a separate gold pocket watch hangs from the skeleton's finger in The Crevice (mid-tier dungeon) — Trophy Case treasure item, **missable** (The Crevice is permanently inaccessible after the Stored Room collapses).

### Gold Pocket Watch
**Weight:** 1
**Location:** The Crevice (mid-tier) — hanging from the skeleton's finger; part of the room description. `TAKE WATCH`.
**Examine:** *A gold pocket watch, its case engraved in a pattern worn almost smooth. It stopped long ago at a quarter past three.*
**Treasure:** 30 points. **Missable** — gone for good once the Stored Room is dug.

---

### Hand Cart
**Examine:** *A sturdy two-wheeled cart, the handles worn smooth. Built to carry more than a person could.*
**Weight:** 5
**Location:** Storage Area, Dungeon Upper Tier
**Examine (loaded):** *The cart sits low on its axle under Calder Finch's gravestone.*
**Quest use:** Quest 32 — needed to move Calder Finch's heavy gravestone from the bog back to the cemetery.

Carried like any item. While loaded:
- **First move after loading (once):** *The cart takes some getting started. Once it's rolling, it wants to keep going.*
- **`UP` / `DOWN` refused:** *Not with that on it.*
- `DROP CART` leaves the stone in the cart; at the Graveyard it does the same as `UNLOAD STONE`.

After the stone is back at the Graveyard the cart stays there (still takeable — nothing else uses it).

---

### Gravestone (Calder Finch)
**Weight:** 10
**Location:** Face-down in the mud in Bog-SE — perception check to find
**Quest use:** Quest 32 — return to cemetery. Requires hand cart. `LOAD STONE ONTO CART` to move, `UNLOAD STONE` at the Graveyard to set it back.

- **Spotted (perception, first time):** *Half-sunk in the mud at the water's edge, a slab of dressed stone lies face-down — too square to be anything the bog made. Someone dumped it here.*
- **Room description (found, in the bog):** *A gravestone lies face-down in the mud.*
- **Examine:** *You tip up one edge far enough to read it: CALDER FINCH — EXPLORER.*
- **`TAKE STONE`:** *It doesn't budge. Whatever carried this out here didn't carry it by hand.*
- **`LOAD STONE ONTO CART` (no cart):** *You'll need something to put it on.*
- **`LOAD STONE ONTO CART`:** *You tip the gravestone up out of the mud and walk it, corner by corner, onto the cart. The axle complains. The bog lets go of the stone with a sound you'd rather not have heard. The gravestone is loaded.*
- **`UNLOAD STONE` at the Graveyard:** *You wheel the cart to the empty plot — a rectangle of disturbed earth with a broken stub of mortar at its head — and tip the gravestone back into place. It settles as if it remembers the spot. You leave the cart beside it; it's done its job.* Stone fixed in place; cart dropped.
- **`UNLOAD STONE` anywhere else:** *You tip the gravestone off the cart. It lands face-down, which seems to be its preference.* Stone stays in that room; `LOAD` works again.
- **Synonyms:** `UNLOAD STONE` / `UNLOAD GRAVESTONE` / `UNLOAD CART` / `UNLOAD STONE FROM CART` / `PUT STONE ON GRAVE` / `PLACE STONE` / `SET STONE` / `RETURN STONE` / `DROP STONE` / `DROP GRAVESTONE`.

---

### Thin Paper
**Weight:** 1
**Location:** Purchased from Shamus (2 Zenni). Destroyed if player gets wet — reappears for sale.
**Examine:** *A few sheets of thin, almost translucent paper — the kind that takes a rubbing.*
**Quest use:** Quest 28 — `RUB PAPER ON ENGRAVING` in Inscription Chamber with charcoal → produces rubbing for archivist.

---

### Charcoal
**Weight:** 1
**Location:** Mine Passage, Dungeon Mid-Tier — no perception check needed
**Room description:** *A few lumps of charcoal lie in a cold fire ring near the tools.*
**Examine:** *Light, black lumps. They'd leave a mark on anything.*
**Quest use:** Quest 28 — used with thin paper to produce rubbing. Used up: the charcoal and the thin paper are both gone once the rubbing is made.

---

### Smoke Jar
**Weight:** 2
**Location:** Supply Room, Dungeon Upper Tier — behind Trap 17 (unstable shelf of clay pots)
**Room description:** *A squat glass jar sits among the clay pots, stoppered with wax.*
**Examine:** *A squat glass jar, stoppered with wax. Something grey and dense shifts inside it.*
**Quest use:** Quest 24 — carrying it keeps the swarm off; `USE SMOKE JAR` at the Swarm Tree settles the bees (used up).

---

### Sack of Salt
**Examine:** *It looks like it weighs as much as a Chachapoyan Fertility Idol.*
**Weight:** 4
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** `SWAP IDOL WITH SALT` — safe weight swap for Chachapoyan Fertility Idol pedestal (Trap 33).

---

### Portcullis Bar
**Examine:** *A length of iron as thick as your wrist, notched at one end. Heavy, and built to take weight.*
**Weight:** 3
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** Props the Portcullis Corridor gate permanently open (Trap 19).

---

### Mortar Compound
**Examine:** *A tub of grey mortar compound, still workable under the lid. Someone meant to fix something down here.*
**Weight:** 2
**Location:** Supply Room, Dungeon Upper Tier
**Quest use:** Quest 22 (The Ruined Aqueduct) — seals the stone blocks in the gap.

---

### Support Beam
**Examine:** *A heavy timber beam, squared and solid. Something meant to hold up a ceiling.*
**Weight:** 4
**Location:** Storage Area, Dungeon Upper Tier
**Quest use:** Quest 38 — props the cleared passage in Collapsed Gallery, makes shortcut permanent. Once propped it stays (can't be taken back).

---

### Pickaxe
**Weight:** 3
**Location:** Main Shaft, Pie Rats Mining Inc. — leaning against the wall, no perception check needed.
**Quest use:** Quest 38 — required to clear the three timbers in Collapsed Gallery (three strength checks).

---

### Gunpowder
**Weight:** 2
**Location:** Purchased from Shamus (5 Zenni)
**Quest use:** Pie Rat Ship heist — `DROP GUNPOWDER` at the structural weak point in the Mine Tunnels, `LIGHT GUNPOWDER` to trigger explosion (text in locations.md — Mine Tunnels).

---

### Flint and Steel
**Weight:** 2
**Location:** Assay Room workbench — *A flint and steel striker lies on the workbench among the crucibles.*
**Quest use:** Pie Rat Ship heist — used to light the gunpowder fuse (`LIGHT GUNPOWDER`). Not a light source. No timer.

---

### Fishing Rod
**Weight:** 2
**Location:** Purchased from Shamus (8 Zenni)
**Examine:** *A jointed wooden rod with a cork grip and a reel that clicks when you turn it. The line looks newer than the rod.*
**Quest use:** Roundabout Pond — `FISH` to retrieve the bottle from the pond floor.

---

### Ship-in-a-Bottle
**Weight:** 2
**Location:** Roundabout Pond — on the bottom until fished out (perception and fishing rolls in locations.md); lands on the bank.
**Room description (on the bank):** *A Ship-in-a-Bottle lies in the reeds at the water's edge.*
**Examine:** *A tiny ship in full sail, sealed in green glass. Someone spent a long time on the rigging. The name on the hull is too small to read — almost.*
**Quest use:** Treasure item (Treasure Items table).

---

### Lockpicks
**Weight:** 1
**Location:** Looted from the Back Alley mugger after defeating him
**Use:** Opens the large iron chest in Mine Passage (contains 20 Zenni). Not a quest item; not a general trap disarm tool.

---

### Fire Clay
**Weight:** 1
**Location:** Thermal Vent Room ceiling (lower tier) — invisible until `LOOK UP`; `TAKE CLAY` retrieves it
**Room description (once found):** *A seam of reddish clay is pressed into the overhang above you.*
**Examine / inventory:** *A lump of reddish fire clay, dense and faintly warm. It takes the print of your fingers.*
**Quest use:** Quest 49 — mixed with fountain water to make clay adhesive for reassembling the shrine bowl.

---

### Clay Adhesive
**Weight:** 1
**Location:** Made at the flowing Town Square fountain — `MIX CLAY WITH WATER` (fire clay used up)
**Examine / inventory:** *A palmful of soft red clay adhesive, tacky to the touch. It won't stay workable forever, but it doesn't seem in a hurry.*
**Quest use:** Quest 49 — `ASSEMBLE BOWL` (used up).

---

### Repaired Bowl
**Weight:** 2
**Location:** `ASSEMBLE BOWL` — three bowl pieces + clay adhesive
**Examine / inventory:** *A ceramic bowl, pieced back together, the seams of red clay still visible. A faint etched line runs around the rim without a break.*
**On the shrine pedestal:** *The repaired bowl sits on the pedestal.*
**Quest use:** Quest 49 — `PUT BOWL ON PEDESTAL`, then a Zenni offering → The Crystal Bowl.

---

### Verdant Circle Shrine Bowl (3 pieces)
**Weight:** 1 each
**Names (2026-10-04):** each piece has its own name so the player can say which — forest piece: *large bowl piece*; bog piece: *muddy bowl piece*; Shrine Room piece: *stone bowl piece*. Each answers to its own word (`TAKE LARGE PIECE`) and to "bowl piece" when it's the only one in reach.
**Examine (forest piece):** *A curved piece of ceramic from the shrine bowl, part of the rim. A faint etched line runs along its edge.*
**Bog piece (Bog-SW):** room listing *Half-sunk in the mud at the edge of the reeds, a curved shard of pale ceramic catches what light there is.* Examine: *A piece of the shrine bowl, caked with bog mud. Under the mud, a faint etched line.*
**Locations:**
1. Near the shrine in Roundabout Forest (perception check)
2. Bog of Eternal Stench (SW) (perception check)
3. Dungeon Upper Tier — Shrine Room (perception check)
**Quest use:** Quest 49 — assemble with fire clay + fountain water → Repaired Bowl.

---

### Bee Queen (Glass Vial)
**Weight:** 1
**Location:** Near the nest in the swarm room (Quest 24)
**Quest use:** Quest 24 — return to beekeeper for enchanted honey reward.
**Room description:** *In the hollow, a small glass vial holds a single tagged bee.* (Visible once the bees settle.)
**Examine:** *A small glass vial, stoppered with cork. Inside, one bee — larger than the rest, a dab of blue paint on her back. She seems unbothered.*

---

### Enchanted Honey
**Weight:** 1
**Location:** Reward from Quest 24 (The Beekeeper's Swarm) — straight to the inventory.
**Quest use:** Consumable — restores 2 hearts when consumed (up to the maximum).
**Examine:** *A small jar of honey, dark gold and faintly warm. It glows a little, as if it's thinking about something.*
**`EAT HONEY`:** *You eat the honey. It tastes like summer, with something older underneath, and the warmth spreads out from your chest.*

---

### Kite
**Weight:** 1
**Location:** Tangled in The Old Oak — `CLIMB TREE` retrieves it (Quest 41).
**Quest use:** Quest 41 — `GIVE KITE TO CHILD`.
The Old Oak rune stone falls free when the kite comes down — see Rune Stones.

---

### Rune Stones (3)
**Weight:** 2 each
**Names (2026-10-04):** Old Oak stone: *flat rune stone*; bog stone: *grey rune stone*; Inscription Chamber stone: *pale rune stone*. Each answers to its own word (`TAKE GREY STONE`) and to "rune stone" when it's the only one in reach.
**Locations:**
1. **Bog rune stone:** Bog-NE (Medium perception check). Room listing: *A grey stone sits at the water's edge, one face worn flat.* Examine: *A grey stone, heavy for its size, one face worn flat by water. Faint lines are etched across the surface in no pattern you recognize.*
2. **Dungeon rune stone:** Inscription Chamber, mid-tier (perception check) — *A pale stone, roughly square, with deep natural veins of darker mineral running through it like old script.*
3. **Old Oak rune stone:** Falls into the grass when the kite comes down (Quest 41). Room listing: *A small flat stone on a cord lies in the grass.* Examine: *A small flat stone, dark and smooth, threaded on a cord. Mineral veins run through it in a pattern that looks almost intentional.*
**Quest use:** Quest 42 (The Brotherhood Stones) — deliver all three to Ivanaar at the Viking Encampment.

---

### Ivanaar's Tunic
**Slot:** Chest
**Weight:** 1
**Location:** Reward from Quest 42 (The Brotherhood Stones) — Ivanaar restores the runes and gives the tunic on delivery of all three stones.
**Quest use:** None — combat bonus.
**Examine:** *A tunic of Brotherhood weave, old but not worn. The runes along the hem and collar glow faintly, restored.*
**`WEAR TUNIC`:** *You pull the tunic on. The weave settles across your shoulders, lighter than it looks.* Damage avoidance applies only while it's worn.

Brotherhood weave, old but not worn. The runes along the hem and collar are faint until the stones are delivered — restored by Ivanaar on completion.

**Damage avoidance:** When the enemy wins a combat round, the tunic rolls 1d10 silently. Result of 7–10 (40%) negates the damage. Fixed — does not scale with player level. On a successful avoidance, one of four flavor messages fires at random:

1. *The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.*
2. *For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.*
3. *The runes along the collar catch the light briefly. You are less hurt than you expected to be.*
4. *Something in the weave absorbed it. You felt the impact — and then didn't.*

---

### Bog Thyme
**Weight:** 1
**Location:** Bog-SW — Medium perception check
**Room description:** *A clump of thyme grows on a dry hummock among the reeds, improbably green.*
**Examine:** *Small grey-green leaves with a smell sharp enough to cut through the bog. Almost.*
**Quest use:** Quest 40 (Shamus's Recipe) — deliver with clay pot to Shamus for hearty stew menu upgrade.

---

### Small Clay Pot
**Weight:** 1
**Location:** Supply Room, Dungeon Upper Tier — visible in wreckage of Trap 17 (clay pot shelf) whether trap is triggered or disarmed. The one intact pot that survives the collapse.
**Room description:** *One small clay pot sits on the shelf, the only one without a crack.*
**Examine:** *A small clay pot, plain and sound. Not a crack in it.*
**Quest use:** Quest 40 — Shamus's pots are all cracked; needs this to cook the hearty stew.

---

### Tip Journal
**Weight:** 1
**Location:** Purchased from Shamus (5 Zenni)
**Quest use:** None — flavor item. Contains in-world tips and observations.
On sale on Shamus's slate (2026-10-05). The journal's contents and `READ JOURNAL` (mechanics.md) aren't designed in detail or built yet — todo.md known issues.

---

### Lockpicks *(see above)*

---

## Treasure Items (Trophy Case)

All high-value items. Delivered to the Trophy Case in Town Hall Tower.

| Item | Location | Weight | Points | Notes |
|------|----------|--------|--------|-------|
| **The Forgotten Blade** | The Fountain Room, Dungeon Lower Tier | 3 | 60 | Most valuable treasure in game; not a combat weapon, ceremonial only. Straight to the inventory from the soldier. Examine: *A ceremonial sword, long and narrow, the blade unmarked by any use. The hilt is wrapped in faded cloth that might once have been a colour.* |
| **Diamond Brooch** | Magnetic Vault, Dungeon Mid-Tier | 1 | 45 | Second most valuable treasure in game |
| **Funeral Mask of Hammered Gold** | Burial Chamber, Dungeon Lower Tier | 3 | 36 | Spirits do not react to taking it. Examine: *A face of hammered gold, serene and thin-lipped, eyes closed. Heavier than it looks, and cold, as if it has been waiting a long time to be picked up.* |
| **Golden Dragon Scale** | Reward from returning dragon-nip to Will | 1 | 36 | Dragon-nip hidden under nightstand in Will's Bedroom. Inventory description: "golden dragon scale". Examine: *A single scale, larger than your palm and heavier than gold has any right to be. It catches the light like a mirror that's decided to be something else.* |
| **Chachapoyan Fertility Idol** | Idol Room, Dungeon Upper Tier | 4 | 30 | Safe swap required (sack of salt); same weight as sack of salt. Examine: *A small stone figurine, squat and round-bellied, worn smooth by hands that weren't yours. A Chachapoyan Fertility Idol, if you had to guess.* |
| **Gold Pocket Watch** | The Crevice, Dungeon Mid-Tier | 1 | 30 | **Missable** — permanently inaccessible after Stored Room collapses |
| **Ship-in-a-Bottle** | Roundabout Pond (fishing rod + challenge roll) | 2 | 24 | Plain treasure — no quest, no May hint |
| **Gold Nugget** | Supply Cache, Dungeon Mid-Tier Trap Side | 2 | 21 | Buried in rubble (`SEARCH RUBBLE`). Examine: *A rough nugget of gold, heavy for its size, still gritty with rock dust.* |
| **Pie Rat Coin** | Flipped by a Pie Rat after returning the stolen ship | 1 | 18 | Unusual currency; pirate provenance |
