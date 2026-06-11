# Enchanted Realms: One Ring — Locations

Authoritative room-by-room reference. Every room: description, connections, items, mechanics, NPC states.
Update this file immediately when any location detail is designed or changed.

**XP defaults:** All rooms award 1 XP on first discovery unless noted otherwise. Exceptions: ocean traversal squares (0 XP), Kevry's Island rooms (5 XP each), dungeon lower tier rooms (2 XP each), dungeon trap side mid-tier rooms (2 XP each), Burial Chamber (3 XP), Skeleton Room (0 XP — instant death on entry). Perception-gated rooms (hidden behind a perception check to discover) award double their base value, except critical path rooms which are set individually. Each room's XP value is noted in its entry below.

---

## Opening Area

### White House / West of House
**XP: 1**
Opening area; homage to Zork. One room only. Any command except `OPEN MAILBOX` returns: *"What does this look like? A Great Underground Empire?"* Opening the mailbox triggers Will's appearance in the field. Will delivers opening text and asks "Are you up for an adventure?" No = game over, never leaves field. Yes = teleported to Will's Wizard Tower. Never revisited after opening sequence.

---

## Will's Wizard Tower

### Will's Wizard Tower (Main Room)
**XP: 1**
Accessed via mailbox portal from White House (opening sequence) or via mailbox in Tale and Ale Main Room.

**First impression:** *The tower doesn't announce itself. It simply is — books, firelight, the low hum of something you can't quite locate. A desk dominates one end, buried under papers that somehow manage to look organized. A painting hangs on the wall, slightly crooked. The room has the feeling of a place where important things happen without any particular fuss.*

Contains a painting of the Tale and Ale — `LOOK AT PAINTING` teleports player back to Tale and Ale Main Room. Painting hangs slightly crooked; Will never straightens it.

### Will Passion's Bedroom
**XP: 1**
Hidden room inside the tower. **Discovery:** Silent Easy perception check fires on every visit to the Main Room. On success, bedroom door becomes visible — permanently. No nudge, no hint. Repeating check. "Where the magic happens." Contains the Enchanted Glasses on the nightstand. Equipping the glasses in Will's presence triggers an instant fail state — Will attacks, no recovery. The bedroom is safe because Will is not there. `DROP GLASSES` places them on the nightstand — description persists. Contains **dragon-nip** — a glowing sprig hidden under the nightstand, practically impossible to find (requires perfect roll at highest level, or Actually Enchanted Glasses). Will has been looking for it everywhere. Returning it to Will earns the **Golden Dragon Scale** (treasure item). Will suspects where it was found but doesn't ask.

**Room description:**
*This is, apparently, where the magic happens. The bedroom is smaller than the main room and considerably more honest about its occupant. Books here are not organized — they are stacked, wedged, balanced, and in at least one case load-bearing. A narrow bed sits against the far wall, made with the perfunctory neatness of someone who knows they'll be up again soon. A nightstand holds a pair of wire-rimmed glasses, a half-melted candle, and a ring left by a cup that was never there long enough to matter. The rest of the room is Will's business and clearly has been for a very long time.*

**Glasses on nightstand (before taking):** *A pair of wire-rimmed glasses sit on the nightstand. They look perfectly ordinary.*

**Glasses on nightstand (after DROP GLASSES):** *Your wire-rimmed glasses sit on the nightstand where you left them.*

**Dragon-nip (perception success only):** *Something small glows faintly under the nightstand — easy to miss, impossible to unsee once noticed. A sprig of something, tucked against the baseboard as if it rolled there and was forgotten.*

---

## Roundabout Town — Main Street

### Main West
**XP: 1**
Western end of Main Street. Library to the north. Archery Range further west. Southeast leads to The Alley.

**Room description:** *Main Street narrows toward the west end, the buildings pulling back slightly as if making room for something that never arrived. The library stands to the north, solid and unhurried. The road continues west toward the archery range. To the southeast, a gap between buildings leads into the alley.*

### Roundabout Town Square
**XP: 1**
Center of town. Town Hall to the north. Tavern to the south. Southwest leads to The Alley. Contains a **fountain** — dry until Quest 22 (The Ruined Aqueduct) is completed. Once flowing, fountain water is required for Quest 49 (The Ruined Shrine) clay adhesive.

**Room description (default — fountain dry, statue unexamined):** *The square is the kind of place a town organizes itself around without quite deciding to. Cobblestones, worn smooth at the center. The Town Hall anchors the north end with the authority of a building that has never doubted its own importance. The tavern faces it from the south, which seems about right. A fountain stands in the middle — dry, the basin cracked at one edge, the stonework patient in the way of things that have been waiting a long time. A stone statue stands to one side — a civic figure of some kind, the plaque below it worn to illegibility.*

**Room description (fountain dry, statue examined — seam visible):** *...A stone statue stands to one side. The plaque below it is worn to illegibility, but the base has a seam around it — visible now that you're looking. Something with leverage could open it.*

**Room description (fountain dry, statue looted):** *...The statue stands to one side, its base pried open and empty. Whatever was inside is gone.*

**Room description (fountain flowing — Quest 22 complete):** *The fountain has been running long enough now that people have stopped remarking on it. The square sounds different with water in it.* (Statue state as above — independent.)

**Statue states are independent of fountain state — combine as appropriate.**

### Main East
**XP: 1**
Eastern end of Main Street. Church of All to the south. Roundabout Wasteland to the east.

*Main Street ends here, or nearly does. The buildings thin out toward the east — a few shuttered fronts, a sign that's lost its lettering, the church standing apart to the south as though it chose its distance deliberately. The wasteland begins where the cobblestones stop.*

### The Alley
**XP: 1**
*The gap between buildings is narrow enough that the sky above is just a strip. Cobblestones give way to packed dirt underfoot. The tavern's back wall runs along the south side. It smells like kitchen waste and something less identifiable. Further south, the alley deepens.* Accessible from Roundabout Town Square (southwest) and Main West (southeast). Exits north to Roundabout Town Square only. South leads to The Back Alley.

### The Back Alley
**XP: 1**
*Darker than the alley, smaller, and considerably less welcoming. The tavern's back wall seals the south end. Broken crates and barrels have accumulated here the way things do when no one is watching. The ground is stained. The air is close. This is where things happen that don't happen on Main Street.* Dead end behind the tavern.

**Mugger mechanic:** A shadowy figure lurks here. Perception check fires every visit until the mugger is spotted and slain. On failed perception: player is mugged — loses 1 heart (physical damage) and 2–3 Zenni (random), loses consciousness, wakes in the Back Alley one turn later. If player has no Zenni: still mugged, 1 heart damage, nothing taken. On successful perception: mugger is visible — fight to the death. Losing the fight: player wakes with 1 heart remaining, text nudges them to rest at the inn. Winning: mugger is slain permanently, Back Alley is safe.

**Loot:** A set of lockpicks — opens the large iron chest in the Mine Passage (mid-tier dungeon), bolted to the floor, contains 20 Zenni. Not a general trap disarm tool.

**Quest Board cascade:** After 100 turns if mugger not yet slain, May posts a bounty notice. Free drink reward when mugger is slain (May flag clears after use).

---

## Town Hall

### Town Hall (Exterior / Main Entrance)
**XP: 1**
*The Town Hall in Roundabout dominates the northern side of the town square. It is a massive brick building with two floors, a broad sloped roof, and a tower with a conical roof in the center. The double doors are solid oak and very heavy.* North of Roundabout Town Square. Two floors plus tower.

Ground floor entry. Grand foyer. Stairs lead up to the Upper Hall. Council Chamber to one side, Records Room to the other.

### Council Chamber
**XP: 1**
Ground floor, off the Main Entrance. Where town business is conducted. **Councilman Rowan Finch** is found here — grandson of Calder Finch, a noted dungeon explorer. Quest 32 giver. Rewards the player with Calder's Middle Tier Key upon quest completion.

**Room description:** *The room where Roundabout conducts its official business, which is to say the room where Roundabout sits in chairs and argues. A long table dominates the center — solid oak, scarred from use. The chairs around it are mismatched in the way of things that have been replaced one at a time over many years. A man sits at the far end with the bearing of someone who has inherited both the title and the table.*

### Records Room
**XP: 1**
Ground floor, off the Main Entrance. Dusty and bureaucratic. Contains the **town charter** — required for Quest 27. The Records Room Worker initially refuses to hand over the charter. After the player returns the pocket watch (from the Chuckle House ghost quest), he gives up the charter as thanks — the watch belonged to his family. Charter is a quest item.

**Room description:** *Floor-to-ceiling shelves on every wall, packed with ledgers and rolled documents in an order that apparently makes sense to someone. The room smells of old paper and the particular dust of things that have not been touched in years. A clerk sits at a desk near the window, surrounded by more of the same. He looks up when you enter with the expression of a man who was hoping you wouldn't.*

### Upper Hall
**XP: 1**
Second floor, top of the stairs. Connects to the Tower. Contains a display cabinet of old town documents and civic artifacts — unlocked, accessible from the start. `OPEN CABINET` reveals contents. The **wax seal** (Quest 4) is inside — `TAKE SEAL` picks it up. No perception check required.

**Room description:** *The second floor is quieter than the ground floor in the way that second floors always are — the noise of official business doesn't quite reach here. A long hall with a runner of carpet gone thin at the center. A display cabinet stands against the wall, unlocked, glass-fronted, holding an assortment of old civic documents and artifacts. The kind of things a town keeps because no one has decided to throw them away.*

### The Tower
**XP: 1**
Accessed from the Upper Hall. Top of the conical tower, overlooking Roundabout Town Square. Contains the **Trophy Case** — a locked glass display case built into the stone wall, where treasure items found during the playthrough are stored.

**Room description:** *The tower room is round, the walls following the cone of the roof above. A single window looks out over the town square, narrow enough that the view is more suggestion than panorama. The Trophy Case dominates the far wall — old wood and glass, built into the stone as if someone planned for it from the start. It is empty. The placard mounted below it reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY FOR THE GLORY OF ROUNDABOUT. The case has not been added to in some time.*

**Trophy Case — examine (`LOOK AT CASE` / `EXAMINE CASE`):** *The case is well-made — solid glass panels, brass fittings, velvet lining gone slightly pale with age. Whoever built it expected it to hold things worth looking at. At the moment it holds nothing. The placard below names the donor. The velvet has the faint impressions of items once displayed here and since removed — or perhaps never placed at all.*

**Trophy Case — verb behavior:**
- `OPEN CASE` — opens the case; required before placing items.
- `CLOSE CASE` — closes the case.
- `PUT <ITEM> IN CASE` / `DROP <ITEM> IN CASE` — if open: places treasure, registers in count. Confirmation text: *"The [item name] settles into the velvet. The case is a better place for it."* If closed: *"The case is closed."*
- `LOOK IN CASE` / `EXAMINE CASE` — lists contents and count, whether open or closed (glass panels — visible either way). Count line: *"[N] treasure[s] on display."* During play, total is never revealed. Win condition fires full display: *"9 of 9 treasures on display."*
- `TAKE <ITEM> FROM CASE` — *"That belongs to Roundabout now."* Not permitted at any time.

---

## Tale and Ale Tavern

### Main Room
**XP: 1**
Central gathering space. Entry point into the inn. Contains a mailbox — completely out of place, acknowledged by no one. `OPEN MAILBOX` teleports player to Will's Wizard Tower.

**Connections:** South → Bar. North → Pipe Room. Northwest → Ty's Casino Corner. Up (staircase) → Upstairs Hall.

**Room description:** *The Tale and Ale announces itself with warmth before you're fully through the door — woodsmoke, something cooking, the low sound of people who have decided their evening is going well. Tables fill most of the floor, a mix of occupied and merely claimed. The bar is south. A staircase climbs along the east wall. To the north, a doorway leads to a quieter room and the smell of pipe smoke. In the far northwest corner, someone is throwing dice. The whole room has the quality of a place that has been exactly like this for a long time and intends to stay that way. Against the wall near the entrance, entirely at odds with everything around it, stands a mailbox. No one looks at it.*

### Bar
**XP: 1**
Where drinks are ordered; food & drink purchases happen here (1 heart, 2 Zenni; hearty stew 2 hearts after Quest 40). **May** (bartender) works here. Quest Board is described in the room text; `LOOK AT BOARD` lists active posted quests.

**Connections:** North → Main Room. South → Kitchen.

**Room description:** *The bar runs the length of the south wall — solid oak, worn smooth at the elbows. Bottles line the shelf behind it in an arrangement that suggests a system only May understands. She works the bar with the efficiency of someone who has answered every question before and will answer them all again without complaint. A board on the wall to one side holds notices — quest postings, local announcements, things people want found or done. The kitchen is further south.*

### Ty's Casino Corner
**XP: 1**
Gambling area inside the tavern. Cargo game (Ship, Captain, Crew dice game). Player sets wager per round; Ty matches. Ty's bankroll: 30 Zenni. Full mechanic in `mechanics.md`.

**Connections:** Southeast → Main Room.

**Room description:** *The northwest corner of the tavern has been claimed so thoroughly it might as well be a different establishment. A large round table dominates the space, ringed with mismatched chairs. Ty sits at the head of it — or what he has decided is the head — presiding over the dice with the calm of a man who has never once worried about the outcome. The noise from the main room reaches here as a comfortable murmur. The game is Cargo: Ship, Captain, and Crew. The stakes are in Zenni.*

### Pipe Room
**XP: 1**
Smoking parlor. Atmospheric; natural gathering spot for Rogues and shady deals.

**Connections:** South → Main Room.

**Room description:** *The pipe room is quieter than the rest of the tavern, which appears to be the point. A few low chairs, a side table, the particular haze of an evening's worth of smoke that has nowhere urgent to be. Conversations here are conducted at a volume that doesn't carry. The kind of room where people come to think, or to be seen thinking, or to say things they'd rather not say at the bar.*

### Kitchen
**XP: 1**
Back-of-house. **Shamus** works here — cook and unofficial vendor. `TALK TO SHAMUS` to buy or sell items. Cellar door to the Cellar/Storeroom is here; bartender holds the key.

**Connections:** North → Bar. Down (cellar door, key required) → Cellar/Storeroom.

**Room description:** *The kitchen is warm and loud in the way that working kitchens are — pots, fire, the particular authority of someone who knows exactly what they're doing. Shamus moves through it without wasted motion, cooking and selling in equal measure — if you need something, he's worth asking. Dried herbs hang from the ceiling in loose bundles. A scarred wooden table dominates the center. The cellar door is set into the floor near the far wall; a faint smell of damp rises from it even when it's shut. The bartender keeps the key.*

### Upstairs Hall
**XP: 1**
Connects the three guest rooms. Accessed via staircase from Main Room.

**Connections:** Down (staircase) → Main Room. Doors lead to Guest Room 1, Guest Room 2, Guest Room 3.

**Room description:** *The upstairs hall is narrow and low-ceilinged, the floorboards announcing every step. Three doors lead off it — the guest rooms. A window at the far end looks out over the alley below. The stairs down creak in a specific sequence that regular guests have learned to navigate quietly.*

### Guest Room 1
**XP: 1**
One of three guest rooms off the Upstairs Hall. Assigned randomly by May when the player pays for rest. Player wakes here refreshed (full heal).

**Room description:** *A plain room, honestly kept. Bed, washstand, a window that looks out over the street. The kind of room that asks nothing of you.*

**Wake-up description:** *You come around slowly. The bed is better than it had any reason to be. Light comes through the window — enough to know you slept. You feel considerably more capable than you did.*

### Guest Room 2
**XP: 1**
One of three guest rooms off the Upstairs Hall. Assigned randomly by May when the player pays for rest. Player wakes here refreshed (full heal).

**Room description:** *A corner room, slightly larger than it needs to be. Two windows, a wardrobe that doesn't quite close, a rag rug that was once a specific color. Comfortable in an unassuming way.*

**Wake-up description:** *The wardrobe door has drifted open in the night. You close it out of habit. Whatever was wrong with you yesterday, sleep has addressed most of it.*

### Guest Room 3
**XP: 1**
One of three guest rooms off the Upstairs Hall. Assigned randomly by May when the player pays for rest. Player wakes here refreshed (full heal).

**Room description:** *The smallest of the three rooms, tucked at the end of the hall. Low ceiling, narrow bed, a single candle on the nightstand burned to nothing. Quiet in a way the other rooms aren't.*

**Wake-up description:** *You wake in the small room at the end of the hall. The candle is out. You are rested — properly, completely rested. That will do.*

### Cellar / Storeroom
**XP: 1**
Below the kitchen; accessed via a cellar door in the kitchen. Bartender holds the key. Starts flooded — drain must be unclogged (crowbar required) before the room is usable. Once drained, reveals a door to the Secret Tunnel. Tunnel door stays in whatever state the player leaves it. Travel bidirectional once drained. Entering from either direction before draining = instant drowning fail state (water damage, no warning, no roll). The flood is obvious from the kitchen doorway — no perception check on entry.

**Connections:** Up (cellar door) → Kitchen. West (tunnel door) → The Junction (Secret Tunnels). **Pre-drain:** tunnel door exists and is openable from The Junction side — opening it before the cellar is drained triggers instant drowning fail state. Post-drain: bidirectional travel freely available.

---

## Library

### Library (Main Hall)
**XP: 1**
*The library is smaller than the building suggests from outside — half the floor space is shelving, floor to ceiling, packed in columns with narrow gaps between. A card catalogue occupies one wall. The other holds a reading table, lamp burning low, a cup of something gone cold. The librarian looks up when you enter. Unlike every librarian you have ever imagined, she appears to want to talk to you.*

Entry space. Lavish wood, copper, and gold. The endless shelves begin here. Medieval exterior with startling red double doors. Interior feels ancient — Babylonian/Egyptian in flavor but older, furnished for comfort. Foundation is secretly a temple to Thoth; all staff are priests/clergy. Only Litlock and long-time patrons know the true nature. **The Librarian** (half-elf, half-Kenku) works here. Full dialogue in `npcs.md`.

### The Stacks
**XP: 1**
The Archivist's working space. Deeper in the collection than the Main Hall suggests is possible.

*The passage from the Main Hall opens into something that shouldn't fit inside this building. The shelves here are older — darker wood, no labels, arranged in a logic that isn't immediately obvious and may not be alphabetical. The ceiling is lost somewhere above the lamplight. At the far end, a large table holds the controlled wreckage of ongoing work: rolled maps weighted open at the corners, books splayed face-down, sheets of careful notation in a hand that doesn't waste space. The Archivist sits at the center of it, or rather the work surrounds him and he happens to be there too.*

**The Archivist** works here. Full dialogue in `npcs.md`. `TALK TO ARCHIVIST` to interact.

**Book research mechanic:** `TALK TO ARCHIVIST` about a subject → he offers matching titles → `READ BOOK` on each in place (books cannot be taken). Only the correct title advances the relevant quest; wrong books yield flavor text. If player names the specific title, he retrieves it directly. Synonyms accepted. May's hints tie in: Tier 1–2 by topic, Tier 3 names the exact title.

---

## Church of All

### Church of All (Nave)
**XP: 1**
Appears as a normal medieval church from the outside. Near the Graveyard. Contains a dial at the altar that allows attunement to any of 7 religions. `TURN DIAL LEFT` and `TURN DIAL RIGHT` cycle through religions one at a time. Current attunement shown in room description. Attunement can be changed freely — no penalty.

**Room description:** *The church is plain inside — stone floor, wooden pews worn smooth, light coming through narrow windows in thin bars. It could belong to any faith. That appears to be the point. At the far end, where an altar would normally hold a single symbol, there is instead a stone altar with a brass dial mounted at its face. Seven marks around the dial. Whatever is currently selected glows faintly.*

### The Altar
**XP: 1**
Separate sub-room inside the Church of All. Contains the attunement dial and the ritual space.

**Room description:** *The altar is plain stone, unadorned. The dial dominates it — brass, worn at the edges from use, seven symbols arranged around its face. The currently selected religion is marked in a faint glow. The air here feels slightly different from the nave. Not sacred, exactly. Attentive.*

**Attunement line (updates on each dial turn):** *The dial is set to [religion name].*

**Default attunement:** The Keepers of the Lantern.

**Dial turn feedback:** The altar shimmers. Room description does not otherwise change.

**Seven religions (dial order left to right):**
1. **The Verdant Circle** — *A sprouting seed inside a circle of leaves.* Nature, growth, forests, patience.
2. **The Veil of the Arcane** — *A seven-pointed star with a void at its center.* Magic as faith; mystery is sacred.
3. **The Brotherhood of the Pale Blade** — *A white sword on a black field.* Death, sacrifice, fallen warriors; calm about mortality.
4. **The Weavers of the Thread** — *Three threads braided into one, ends frayed.* Fate, destiny, the pattern connecting all lives.
5. **The House of the Coin** — *A coin, heads on one side, a question mark on the other.* Trade, wealth, fair dealing; merchants and vendors.
6. **The Keepers of the Lantern** — *A lit lantern with an open door.* Hope, healing, guidance for the lost; most publicly visible faith.
7. **The Hearth Folk** — *A fire inside a house outline, door open.* Family, shelter, belonging; the faith of ordinary people.

**Ring quest ritual mechanic:** See `ring-rituals.md` for full sequence. Summary:
- Place artifacts on altar in any order. Each glows when the correct religion is attuned on the dial.
- Verdant Circle (Crystal Bowl) → green. Veil of the Arcane (Werewolf's Amulet) → red. Brotherhood of the Pale Blade (Pale Blade) → white.
- Once all three are glowing, place the ring on the altar to complete the ritual sequence.
- Ring placed before all three are glowing: *"Nothing happens. Something is missing from the ritual. You pick up the ring."* Ring returns to inventory automatically.
- Wrong religion attuned when artifact placed: altar shimmers normally but artifact does not glow.


### Keeper's Chamber
**XP: 1**
The private quarters of the Keeper of the Faiths. Door is locked; key found on the Keeper's skeleton in the Lower Crypt (dungeon lower tier). Inside: sparse quarters, personal effects, a **vial of holy water** on the writing desk, and a note in the Keeper's hand. The note reveals that the scholar of The Veil of the Arcane was transformed into an undead werewolf — and that the silver stake must be consecrated with holy water to be effective. `POUR HOLY WATER ON STAKE` → consecrated silver stake.

**Room description (vial present):** *A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a vial of clear liquid, and a note in a careful hand. Whatever the Keeper was preparing for, he prepared it here.*

**Room description (vial taken):** *A small room, plainly kept. A narrow bed, a writing desk, a shelf of religious texts. The kind of room that belongs to someone who doesn't spend much time in it. On the desk: a note in a careful hand.*

**Note:** Readable but not takeable. Reveals the scholar became an undead werewolf and that the stake must be consecrated with holy water.

---

## Graveyard

### Graveyard
**XP: 1**
South of the Church of All. Single room. North to Church of All; south to Mausoleum. West exit to Chuckle House appears only after Litlock's bonk (Quest 16) — absent from description until then.

**Pre-bonk description:** *The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it. The church stands to the north. The mausoleum sits at the far end to the south, grey and patient. The air is still in a way that has nothing to do with wind.*

**Post-bonk description:** *The graves here are old, most of them. Headstones lean at angles that suggest the ground beneath has shifted, or decided it no longer agrees with what's above it. The church stands to the north. The mausoleum sits at the far end to the south, grey and patient. To the west, a low building stands where there was nothing before — and you are not sure how you missed it. It is a low structure with a painted facade — or was, once. The paint shows something cheerful from a distance: bright colors, broad shapes, a kind of deliberate festivity. Up close, the colors are gone to grey and the shapes resolve into faces. They are smiling. They have been smiling for a very long time. The air is still in a way that has nothing to do with wind.*

**Town square statue:** The statue in Roundabout Town Square has a hollow base — seam visible to anyone who types `LOOK AT STATUE` (no perception check). Attempting to open without a crowbar: *"The base is sealed tight. Something with leverage could pry it open."* Crowbar opens it → silver stake + folded note inside. Note unsigned but identified by emerald wax seal (same seal as Keeper's skeleton). May's tier 1 hint (fires only if player has not yet examined the statue): *"Someone was seen tampering with the statue in Roundabout Town Square. Probably nothing. Probably."*

### The Mausoleum
**XP: 1**
*The mausoleum is older than anything around it. The stone is dark with age and moisture, the carved details worn to suggestions. The door is heavy iron, pitted with rust but still on its hinges. Whatever family name was once above the entrance has been lost to weather. Steps descend inside toward the crypt below.* South of the Graveyard. Weathered and decrepit. Stairs lead down to The Crypt.

### The Crypt
**XP: 1**
**First visit:** *The crypt has not been visited recently. Dust lies undisturbed on the stone floor, on the alcoves, on the remains within them. It is very quiet. Very cold. At the far end a rough-cut passage opens into darkness — older than the crypt itself, by the look of the stonework.*

**Subsequent visits:** *The crypt is quiet and cold. Dust lies on the stone floor — a set of footprints visible in it, the only sign anything has changed. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.*

**Third+ visits:** *The crypt is quiet and cold. Dust lies on the stone floor — several sets of footprints visible in it. For a crypt, it's practically a thoroughfare. The alcoves hold their dead without comment. At the far end the passage leads on into the dark.*

Connects south to The Charnel Walk (Secret Tunnels).

---

## The Chuckle House

**Location:** West of the Graveyard. Dead-end spur — not visible or accessible until Litlock's quest is complete (bonk on the head mechanic). No perception check can find it; the building is genuinely invisible until the bonk. Once visible, it remains visible for the rest of the playthrough.

Four rooms, linear. Ring (invisibility) required throughout — all mirrors repel visible players. Quest 17 anchor.

### The Entrance
**XP: 1**
No mirrors in this room — mirror mechanic begins in the Rejection Mirror. The building was a funhouse; that history is legible from this room.

**Room description:** *The entrance hall is wider than the exterior suggests. A faded runner covers the floor — the pattern beneath the grime might have been geometric once, or might have been faces too; it's hard to say now. The ceiling is low and painted, or was. Hooks on the wall where coats or hats once hung, empty now. A ticket booth stands to one side, the glass cracked, the stool inside still in place as if whoever left simply forgot to come back. The building has the quality of a held breath.*

**On entry (first visit only):** *Something in the walls makes a sound as you cross the threshold — not quite a creak, not quite a welcome.*

**Ticket booth (EXAMINE BOOTH / LOOK AT BOOTH):** *The ticket window is cracked but intact. A small wooden sign on the ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. The booth is empty. Whoever collected the tickets isn't collecting anymore.*

**Hooks on wall (EXAMINE HOOKS / LOOK AT HOOKS):** *Empty brackets where something square once hung — the right shape for mirrors, though whatever was here is long gone. The hooks in the deeper rooms still have their tenants.*

**Exits:** South to Graveyard; north to Rejection Mirror.

### The Rejection Mirror
**XP: 1**
A mirror that repels visible players — stepping in front of it while visible sends the player back to the Entrance. Passing while invisible (ring worn) proceeds normally. No ghost here — ghost is in the last room.

### The Shatter Trap Mirror
**XP: 1**
A mirror that repels visible players. Also rigged with a crossbow behind the frame (Trap 16). Fires at any player passing through — visible or invisible. Perception check spots the firing pin and disarms it before it fires; otherwise the crossbow fires once and is spent. Mirror still repels visible players until the ghost is freed.

### Ghost's Room
**XP: 1**
Mirrors on all sides. The ghost of the Records Room Worker's missing relative haunts this room — hostile. Ghost visible only while wearing the ring. `CAST UNBIND UNDEAD` releases the ghost; he says *"Thank you. I can rest now."* and drops the pocket watch. **Exit mechanic:** 50% chance each attempt to leave fails — player returned to same room with a disorientation message. Permanent — does not end when ghost is freed. Post-freeing: mirrors no longer repel visible players anywhere in the Chuckle House.

**May's hints — Ghost/Watch quest:**
- Before visiting — Tier 1: People say the mirrors in the Chuckle House show more than they should. Most folks don't go back a second time.
- Before visiting — Tier 2: Word is a family member of the records room clerk went into the Chuckle House years ago and never came out. He doesn't talk about it.
- Before visiting — Tier 3: The trick with the Chuckle House is that some doors only open for people the mirrors can't find.
- After visiting (ghost not yet freed) — Tier 1: Malevolent spirits can only be freed through magic.
- After visiting (ghost not yet freed) — Tier 2: Silas Bryne — keeps the lighthouse — mentioned he came across a spell he couldn't make heads or tails of. Left it on his desk.

---

## Roundabout Wasteland & Volcano

### Roundabout Wasteland
**XP: 1**
*The wasteland sits at the edge of Roundabout like an embarrassing relative. Something went very wrong here, and not recently. The ground doesn't grow anything. The structures that remain are shells. Whatever happened, it happened thoroughly. The cause is a matter of some local sensitivity. The prevailing theory among residents involves adventurers, which explains why no one wants to discuss it in detail. To the east, a volcano rises against the sky — large, dark, and entirely convincing.* East of Main East. Single room. Quest hooks TBD.

### The Volcano
**XP: 1**
The illusory volcano itself. Appears entirely real. Harder perception check required to see through it. On success: uneven staircase DOWN revealed. On failure: player sees only an active volcano with no apparent entrance.

### Pyronicus's Forge
**XP: 2**
*The room is large enough that the walls at the far end are suggestion rather than certainty. Obsidian everywhere — floor, walls, ceiling — smooth and black and catching the forge light in brief amber before giving it back to the dark. The forge itself dominates the center: enormous, ancient, burning with the steady purpose of something that has never been allowed to go out. The heat it produces rises through the rock above, feeding an illusion so convincing that even the smoke smells right. Pyronicus built this room first. The volcano came after.* Single room.

**Ring handover:** *Pyronicus sets down his work and regards you with calm, unhurried eyes. "Will's errand," he says. "Yes." He moves to a workbench and returns with the ring, placing it in your hand with the care of someone returning something that was never theirs. "It fell through my ceiling," he says. "Rings don't do that by accident." He pauses. "Will told you what you need to know, I assume." He goes back to what he was doing. The conversation, apparently, is over.*

**Pale Blade forging:** When player brings runed metal from the Viking Encampment: Pyronicus forges it into the Pale Blade. Full forge scene confirmed — see `ring-rituals.md` (Artifact 1, Step 3).

---

## Archery Range & Viking Encampment

### Archery Range
**XP: 1**
*Straw targets line the far end of a long cleared field, bristling with arrows. The range is well-used. The Vikings from the encampment to the west use it freely — and apparently consider the entire field fair game, including the parts you're standing in.* Hazardous — agility challenge roll each time the player passes through to avoid being hit by an errant arrow; failure deals 1 heart physical damage. Permanently safe once all three Viking trust trials are complete (silent mechanic, no acknowledgment). **Raznak** found here.

### Viking Encampment (The Encampment — hub)
**XP: 1**
West of the Archery Range. Followers of The Brotherhood of the Pale Blade. Three trust trials must be completed in order: Riddle Stone (Trial 1) → Ritual Circle (Trial 2) → Fire Pit (Trial 3).

Central hub. Fire pit, longhouses, Vikings going about their business. East → Archery Range. North → Haalvar's Hut (Trial 1). South → The Ritual Circle (Trial 2). West → The Fire Pit (Trial 3).

**Banner:** `LOOK AT BANNER` reveals four elemental rune symbols in order: Earth, Air, Fire, Water (clue for Ritual Circle Trial 2).

**Ivanaar Stormbringer states:**
- 0 trials: *"You want something from us. They always want something. Prove yourself. Talk to Haalvar — north. If you can satisfy him, come back."*
- 1 trial: *"Haalvar speaks well of you. That's not nothing. The circle is south."*
- 2 trials: *"Two down. The fire pit is west. Don't embarrass yourself."*
- 3 trials (runed metal handoff): See below.

**Runed metal handoff (after all three trials):** Triggered when player drags Aylora back after Trial 3.

*Ivanaar looks at Aylora, then at you, then at Aylora again. He says nothing for a long moment. "...Thornbrew?" he finally asks. You nod. He laughs — once, short, like it surprised him too. Then he straightens, and the laugh is gone, and something older takes its place. "Will Passion sent you. He asked me to build something that would tell him whether you were worth trusting with what comes next. He didn't tell me what comes next." He moves to the longhouse and returns holding a length of dark metal — dense, rune-carved, warm to the touch even in the open air. He holds it with both hands. "This is Brotherhood metal. It has been kept since before this encampment. It would make a fine blade in the right hands — a blacksmith who knows what he is looking at could tell you more." He places it in your hands. "I hope Will is right about you."*

*"One more thing. There are three stones out in the world — Brotherhood metal, rune-carved. They've been scattered a long time. If you come across them, bring them to me." He glances back once. "I'll make it worth your time."*

*Ivanaar returns to his fire.*

**[Runed Metal added to inventory.]**

### Haalvar's Hut (Trial 1 — The Riddle Stone)
**XP: 1**
North of The Encampment. **Haalvar** administers the trial. The hut contains a stone with runic carvings and a fluid-like appearance — solid to the touch, its surface moves like dark water. On entry, Haalvar delivers the riddle: *"I have no legs but travel far. I have no mouth but swallow ships. I have no hands but I will take everything you own if you let me. What am I?"*

- **Correct answer:** `SEA` — stone glows; Haalvar: *"The stone is satisfied. I am also satisfied, which happens less often. Go south — there is a circle there that will want your attention next."* Trial 1 complete.
- **Wrong answer:** *"Impressive. Wrong, but impressive in its wrongness."* Retryable.
- **Actually Enchanted Glasses:** Kevry's voice whispers the answer.

### The Ritual Circle (Trial 2)
**XP: 1**
South of The Encampment. An unnamed child administers the trial — he does not speak. Five rune stones arranged around a carved symbol: Earth, Air, Fire, Water, Heart.

**Correct order:** Earth → Air → Fire → Water → Heart. First four from the banner; Heart stone always last.

**Commands:** `ACTIVATE EARTH STONE`, `ACTIVATE AIR STONE`, `ACTIVATE FIRE STONE`, `ACTIVATE WATER STONE`, `ACTIVATE HEART STONE` (also accepts `ACTIVATE LOVE STONE` and `ACTIVATE LIFE STONE`).

- **Wrong order:** *"The child looks disappointed in you."* Resets all five.
- **Correct completion:** Child points back toward the encampment. Trial 2 complete.

### The Fire Pit (Trial 3 — The Drinking Challenge)
**XP: 1**
West of The Encampment. **Aylora** is the Viking champion. Best of five rounds; each round is a strength-based challenge roll. Warriors get a class bonus; Rogues and Mages roll straight. The drink: Thornbrew.

- **Player wins:** Aylora passes out. Player drags her back to the encampment → triggers Ivanaar's runed metal handoff.
- **Player loses:** Player passes out. Wakes up in the encampment two turns later. A nearby Viking: *"Ha! Aylora strikes again. Don't feel bad — she's been doing this since she could reach the cup."* Retryable.

---

## Roundabout Pond & Bog

### Roundabout Pond
**XP: 1**
Between town and the bog. Two-state room.

**Base description:** *The pond is easy to walk past without noticing. It sits low between the town path and the bog, ringed with reeds and the occasional frog. The water is dark and calm.*

Each visit fires a silent perception check. On success: "You see a bottle at the bottom of the pond." — quest discovered, May's hints unlock. Sighting not permanent; check fires on every visit until quest is discovered. Retrieving the bottle requires a fishing rod (purchased from vendor) and a successful challenge roll (`FISH`); Rogues get a bonus. The bottle is a treasure item.

**May's hints:** Imply Kevry was trying to retrieve his ship from the pond — player connects ship and bottle. Kevry knows about it but was never able to fish it out himself.

### Bog of Eternal Stench
**XP: 1 per bog room (4 total)**
Four rooms arranged in a 2×2 grid. Players may move diagonally between rooms. All four display the same room title to the player: **"The Bog of Eternal Stench"** — directional designations (Bog-NE, Bog-NW, Bog-SE, Bog-SW) are internal design references only, never shown to the player. Accessed from the Roundabout Pond to the east.

- **Bog-SE:** *The bog stretches in every direction, dark water between clumps of soggy earth. The smell is comprehensive and personal. Reeds crowd the edges of every dry patch. Something is moving just out of sight, or was.* Entry point. Dankhaus hidden here — dense brush conceals the path; perception check required each visit until discovered. Once discovered, path is permanently visible.
- **Bog-NE:** *The ground here is technically solid. Technically. Dark water pools between tufts of coarse grass. The smell has layers. You have stopped trying to identify them, and don't really want to.* Contains a rune stone (Quest 42) — perception check required.
- **Bog-SW:** *A flat expanse of bog, grey-green and indifferent. The water is still except where it isn't. The smell arrived before you did and will be here long after you leave.* Contains bog thyme (Quest 40) — perception check required to spot it among the reeds.
- **Bog-NW:** *The reeds are taller here, crowding in from the edges. The water is darker. The smell is worse. This part of the bog feels less visited, which is saying something.* Contains a hollow log — perception check required to find it. Inside: the key to Will's music box (Quest 12). Also: Quest 50 Bog-NW exit surfaces here (shovel required to finish hole from Lost Apprentice's Cell).

### The Dankhaus
**XP: 1 per room**
Three-bedroom home hidden in the bog behind dense brush. Perception check required to find it (Bog-SE). Litlock's residence; also houses Lynds and Aurix the Kobold child. Appears as a yurt from outside. Magical wards bar uninvited entry — cleared by flag set when player beats Lynds at arm wrestling (Lynds's invitation). Ward deflection (no invitation): *Something in the air near the door shifts as you approach. Not hostile. More like a house that knows you haven't been introduced yet.*

- **Common Room:** Entry and gathering space. Large fireplace. **XP: 3** (perception-gated discovery bonus). *Litlock fills whatever room he's in without trying to. The common room is large enough, and he's in it — near the fireplace, which is also large, and burning steadily. Chairs, a table, shelves. The kind of room that works because the people in it make it work. He looks up.*
- **Kitchen:** *A working kitchen — herbs drying overhead, something on the fire, the garden accessible through the east door. It smells like it has always smelled like this.*
- **Garden:** *The garden shouldn't work. The bog is right there, the soil is wrong, and nothing about this location suggests flowers or vegetables. And yet. Raised beds, neatly kept. Things growing that have no business growing here. The Dankhaus wall is to the west. The bog presses in on every other side and seems to have accepted that it lost this argument.*
- **Litlock's Room:** *A plain room — bed, chest, a low shelf of things that don't announce themselves. Nothing here suggests the man who laughed until he had to put something down. That version of Litlock lives in the common room. This one is private.*
- **Litlock's Study:** *The study is where Litlock keeps the part of himself he doesn't lead with. Shelves of books and things that aren't books. A desk with papers in an order that makes sense to someone. A candle burned low. The jovial man from the common room was entirely real — so is this room, and they belong to the same person.*
- **Lynds's Room:** *Lynds's room. Large, untidy, comfortable. The furniture has been through some things.*
- **Aurix's Room:** *Small bed, small shelf, the accumulated objects of a child who picks things up and keeps them. The chalk marks on the floor have been there long enough that no one is going to do anything about them.*

---

## Beach Road, Forest & Mine

### Beach Road
**XP: 1**
East of the Wasteland. A road that forks — south toward Roundabout Beach, uphill winding toward Roundabout Forest. Single room.

### The Old Oak
**XP: 1**
Between Beach Road Fork and Roundabout Forest. A large oak dominates this spot. A child stands here — a kite is tangled in the upper branches. `CLIMB TREE` retrieves the kite; a rune stone threaded on a cord falls free. `GIVE KITE TO CHILD` completes Quest 41. The rune stone is one of three needed for Quest 42.

### Beekeeper's Cottage
**XP: 1**
*A low wooden cottage sits at the edge of the trees, almost part of the forest. Stacked hive boxes line the south wall, painted in fading colours. The smell of beeswax and woodsmoke is pleasant in a specific, unhurried way. The beekeeper is here — a broad woman with patience in her posture and a concerning number of sting marks on her forearms.* Spur west off The Old Oak, at the forest edge.

**Beekeeper (NPC):** On first visit, explains that a swarm escaped and nested in a hollow tree at the forest edge — she gestures east. She can't get near it without her smoke equipment, which is somewhere in the tunnels below. Quest 24 discovered on first visit. After quest: warm, gives enchanted honey reward.

### Swarm Tree
**XP: 1**
*A broad-trunked tree at the forest edge, older than the others around it. A low drone comes from a dark gap in the bark at chest height. The air nearby has a quality that suggests strongly you should not approach without a plan.* Spur east off The Old Oak, adjacent to Beekeeper's Cottage.

**Without smoke jar:** Walking within reach triggers the swarm — 1 heart damage (physical), player retreats automatically to The Old Oak. *"The swarm boils out of the hollow before you can do anything useful. You retreat."*
**With smoke jar:** `USE SMOKE JAR` — bees settle. Queen vial visible in hollow. `TAKE VIAL` completes the collection step.

### Roundabout Forest
**XP: 1**
*You wouldn't know, walking through here, that the ground beneath you is hollow. The forest is peaceful — birdsong, dappled light, the smell of pine. The mine entrance sits somewhere among the roots and undergrowth, easy to miss if you don't know to look.* Single room. Transitional space above the mine. Connects downhill to The Old Oak. The crumbled Verdant Circle shrine is visible on entry — no perception check required. **Shrine description:** *A stone shrine stands at the edge of the trees — old enough that the forest has started to take it back. A carved pedestal, still solid. On it, the remains of a ceramic bowl, smashed at some point and not recently. Three or four pieces visible here; others have clearly gone elsewhere. The symbol on the pedestal is a sprouting seed inside a circle of leaves.*

### Pie Rats Mining Inc.
**XP: 1 per room**
Underground beneath Roundabout Forest. Legitimate mining facade; actually a smuggling front for the Pie Rats pirate faction.

- **Mine Entrance:** Forest floor. Sealed permanently after the cave-in explosion.

  *The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY. Someone has added, in different handwriting: THIS MEANS YOU. In another hand: ME? And beneath that, in the first handwriting: NO, NOT YOU SLOTH.*

  **Post-cave-in:** *The entrance is gone. The explosion brought the whole thing down — timbers, signage, and a significant quantity of rock. Whatever was inside is inside permanently, or accessible some other way.*

- **Main Shaft:** Central spine. Connects Mine Entrance (up) to Mine Tunnels (down). Side passage to Assay Room. Contains a **pickaxe** — mining equipment, obvious and takeable.

  *The main shaft drops away from the entrance in a single rough-cut passage, wide enough for two men and a cart. Timber supports run at intervals — functional, not decorative. The smell of rock dust and old torchsmoke is thick here.*

- **Assay Room:** Off Main Shaft. Where ore samples were tested. Connects to Hidden Secondary Entrance into Secret Tunnels.

  *A side room off the main shaft, fitted out for testing ore samples. A long workbench runs the length of one wall, scarred with acid burns and impact marks. Scales, tongs, crucibles — the tools of a working assay operation, left mid-use. Whatever the Pie Rats were mining, someone was genuinely checking its quality. The far wall has a gap in it that doesn't look entirely accidental.*

- **Hidden Secondary Entrance:** Between Assay Room and Forgotten Shaft. Perception check from mine side; auto-discovered from tunnel side. Remains accessible after cave-in. **XP: 2**

  *The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.*

- **Mine Tunnels:** Working tunnels. Torch sconces on walls — torches taken immediately begin burning down (40 turn timer). Burnout = fail state for gunpowder sequence.

  *The working tunnels branch off the main shaft in two directions, following veins of ore that may or may not have been the point. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The smell of fresh-cut rock is strongest here. The floor is rutted with cart tracks.*

- **The Rat's Nest:** Off Mine Tunnels. Hidden storage for Pie Rat contraband. Contains the Pie Rat disguise required for the ship heist.

  *A widening in the tunnel that someone has decided is a room. Crates and barrels are stacked with more care than the surroundings suggest — this is storage, not clutter. The Pie Rats keep their surplus here: things that aren't ore, things that don't show up on manifests, things that would raise questions on a dock.*

---

## Roundabout Beach & Sea

### Roundabout Beach
**XP: 1**
*Roundabout Beach opens up as the town falls behind you — a generous sweep of sand, the water catching whatever light the sky offers. The docks stretch east to where the Pie Rat Ship is moored, close enough to read the name on its hull. The lighthouse stands to the north on a finger of rock, its lamp turning slowly. It smells like freedom, or at least like salt.*

Players carrying a shovel will likely attempt to dig. `DIG` succeeds up to 5 times with flavor text (nothing but wet sand); 6th attempt: "The beach is littered with holes. There's nowhere else to dig."

### The Lighthouse
**XP: 1**
Dead-end room off Roundabout Beach to the north. Open, unattended. A desk holds a scroll — the **Unbind Undead spell**, left by Silas Bryne (unmet NPC, referenced only in May's Quest 17 hints). No quest assigned beyond the scroll. Quests 14 and 23 both retired.

### The Docks
**XP: 1**
*The boards flex slightly underfoot, worn smooth by years of boots and cargo. Bollards thick with rope line the edge. A coil of rope sits loose on the nearest bollard. The Pie Rat Ship sits in her berth like she owns it, which she more or less does — the only vessel worth the name in Roundabout's harbor. The smell is fish and brine and honest work.*

**Rope:** A coil of rope is visible as a takeable item. This is the one Rope item in the world — used to tie off the Hole to Below beam in the dungeon mid-tier (`TIE ROPE TO BEAM`).

### Pie Rat Ship — Deck
**XP: 1**
Moored at the Docks. Crewed by Pie Rats until the explosion draws them away. The only vessel available to sail the Roundabout Sea. Single room — no hold. Boarding commands (all synonyms): `BOARD SHIP`, `GET ON SHIP`, `CLIMB ABOARD`, `ENTER SHIP`. Sailing commands: `SET SAIL` (primary), `SAIL` (synonym). Directional movement once underway: `GO EAST`, `SAIL EAST`, etc. Leaving the ship at sea: *"The ocean offers no opinion on that idea, and neither does your survival instinct."* `DOCK` returns ship to Docks; `LAND` / `MOOR` / `MAKE LAND` puts player ashore at Desert Island or Kevry's Island.

**Boarding without disguise:** *A Pie Rat on deck looks you over with the thoroughness of someone whose job is exactly this. "You don't even look like a pirate." He doesn't move. Neither, apparently, will you.*

**Room description:** *The deck is cluttered in the way of a working vessel — coils of line, barrels lashed to the rail, a general smell of fish and salt and something that has been at sea too long. This is a ship that wants to move.*

**Shovel (in room, before taken):** *A shovel is lashed to the rail near the bow, practical and out of place at the same time.*

**Perception check (each turn aboard):** Silent check fires every turn until treasure map is found. On success: map added to inventory. Actually Enchanted Glasses pass automatically — map found on first turn. A player who sails to Kevry's island without finding the map, gets the glasses enchanted there, and returns to the ship will auto-find the map on their next turn aboard.

### The Sea
**XP: 1 per Roundabout Sea room (3 total); 0 XP for all 69 Open Ocean traversal squares; Desert Island: 1 XP**
Three Roundabout Sea rooms + 69 Open Ocean squares to Kevry's island. Requires boat. Desert Island is a spur off the Eastern Roundabout Sea.

### Western Roundabout Sea
**XP: 1**
*The smell of the town still reaches you here — smoke and bread underneath the salt. The beach stretches behind you, the lighthouse standing watch to the north. The water is choppier than it looked from shore. Ahead, the coast begins to fall away.*

### Roundabout Sea (Middle)
**XP: 1**
*The coast is gone. There is nothing in any direction but open water and sky. The sea moves in long slow swells that lift and drop the hull with a steady indifference. You are very small out here.*

### Eastern Roundabout Sea
**XP: 1**
*Is that — yes. An island. Small, tree-lined, a beach curving around the side facing you. The water around it is shallow and clear. Nothing out here suggested this was coming. It sits quietly off the bow, waiting to be noticed. East of it, the sea continues without comment.*

`DOCK`, `LAND`, `MOOR`, or `MAKE LAND` puts the player ashore on the Desert Island. Continuing east enters the Open Ocean.

### Open Ocean
**XP: 0 per room (69 rooms)**
Each room draws a random description from the pool below. The rare option triggers at 1-in-100 chance per room entered.

**Standard pool:**
1. *Open ocean in every direction. Nothing else.*
2. *The ocean does not vary its presentation.*
3. *No land. No landmarks. Just the creak of the hull and the indifferent sea.*
4. *The ocean offers nothing in any direction. It does not apologize for this.*
5. *Sea. Sky. Nothing else to report.*

**Rare option:** *You could swear you heard laughter just now. Distant, directionless. The ocean is empty in every direction. You've been out here a while.*

### Desert Island
**XP: 1**
Spur off the Eastern Roundabout Sea — not on the main east axis. Visible from the Eastern Roundabout Sea. Reached via `DOCK`, `LAND`, `MOOR`, or `MAKE LAND`. `BOARD SHIP` returns the player to the Eastern Roundabout Sea. Appears to be the obvious payoff for sailing east — masks Kevry's location 69 squares further into the Open Ocean.

**Island Shore (the only room):** *The sand on the beach is undisturbed. That fact, for some reason, does not comfort you. Nothing here is threatening and nothing here is welcoming. The island feels like a place that has been waiting — not for you specifically, but for someone. The quiet here is a different kind of quiet than the open ocean — heavier, more deliberate. You have the distinct feeling that something happened here once. The island isn't telling.*

A buried chest is here — not visible without digging. With the treasure map: `DIG` succeeds immediately. Without the map: 10% chance per `DIG` attempt. Contents: 30 Zenni.

### Kevry's Island
**XP: 5 per room (4 rooms = 20 total)**
Easter egg. 69 squares into the Open Ocean east of the Eastern Roundabout Sea. No hints from May. Boarding commands (`DOCK`, `LAND`, `MOOR`, `MAKE LAND`) to come ashore; `BOARD SHIP` returns player to Open Ocean square 69.

### Land, Ho!
**XP: 5**
First room on the island. Same boarding mechanic as Desert Island.

*The island resolves out of the horizon slowly, then all at once. Sand, trees, solid ground. You've earned this. The beach curves invitingly ahead.*

### Empty Beach
**XP: 5**
*The beach is long and quiet, the sand unmarked. A line of scrubby trees runs along the inland edge. Somewhere beyond them, half-hidden, a small structure. The only sounds are the water behind you and the wind doing very little. It feels like a place that has been left alone for a long time and is content with that.*

### A House / Kevry's House
**XP: 5**
Room name changes to **Kevry's House** after the player enters and interacts with Kevry.

*The interior is cluttered in the way that only makes sense to its owner. Charts pinned to every surface, ropes coiled with obsessive care, a hammock in the corner. A lantern hangs from a beam. Someone has been here a long time and made their peace with it.*

### Captain's Quarters
**XP: 5**
Kevry is found here. Enchants the Enchanted Glasses if already equipped in the head slot.

*A small back room, all table and charts and the smell of ink. A weathered man sits hunched over a map, muttering. He doesn't hear you come in. When he finally looks up, his face does something complicated — surprise, then recognition of the type that doesn't require prior acquaintance, then a wide and genuine grin.*

---

## Secret Tunnels

**XP: 1 per room**
Underground pre-dungeon level connecting the Tavern Cellar, the mine, the Graveyard Crypt, and the Dungeon Entrance.

- **The Junction:** First room off the Tavern Cellar. Hub — branches toward mine (east), Graveyard Crypt (west via Bone Passage and Charnel Walk), and deeper toward dungeon. A door to the north leads to the Cellar/Storeroom — if the cellar has not been drained, opening this door triggers instant drowning fail state.

  *The tunnel opens up here — not much, but enough to feel like a decision point. Rough stone walls, a ceiling low enough to notice. Passages branch in three directions. The one behind you leads back up to the cellar. The air is damp and smells of old earth and something faintly mineral. Down here, sound doesn't carry the way it should.*

- **The Undercroft:** Wide rough-hewn passage on the mine branch.

  *A wide passage, rough-hewn and unfinished, the kind of digging done in a hurry by people who knew where they were going. The walls are close enough that two people could pass but would have to mean it. The floor is uneven underfoot. The air is heavier here, deeper-smelling.*

- **The Forgotten Shaft:** Narrowing abandoned passage. Connects to the Hidden Secondary Entrance on the mine side.

  *The passage narrows as it goes — not dangerously, but noticeably. The stonework changes here, older and less deliberate, as if this part of the tunnel predates whoever dug the rest. The far wall has a gap in it that doesn't look entirely accidental.*

- **The Bone Passage:** Crypt branch off the Junction. Older stonework.

  *The stonework here is older than the rest of the tunnels — rougher cut, the joints wider, the walls slightly damp to the touch. The passage runs west. Whatever built this part didn't build it at the same time as the rest. The name feels earned.*

- **The Charnel Walk:** Final room before Graveyard Crypt entrance.

  *The passage ends at a low arch ahead — beyond it, the crypt. The air is colder here, noticeably so, as if the temperature has been coming down gradually and this is where it arrives. The walls are older stone, darker with moisture. The silence has a different quality than the tunnels behind you.*

- **The Toll Bridge:** Deep in the Secret Tunnels. A small bridge over an underground ravine — only route to the Dungeon Entrance. A **Boggart** has claimed squatter's rights and charges an extortionate toll. Perception check reveals faded official seal — public property — triggering Quest 27 discovery and unlocking May's hint. `GIVE CHARTER TO BOGGART` forces him out; drops strongbox (strength check to open, several turns' worth of Zenni). Bridge permanently free after. (Quest 27)

  **Room description (Boggart present):** *A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid. A small, dense figure has planted itself at the center of it with the unmistakable air of someone who intends to stay. He eyes you with the satisfaction of a man whose position has never once been successfully argued with.*

  **Room description (Boggart gone, strongbox present):** *The bridge is empty now. The strongbox sits where he was.*

  **Room description (strongbox opened/looted):** *The bridge is empty. The open strongbox sits where he was, lid thrown back.*

- **Dungeon Entrance:** Beyond the Toll Bridge. Threshold between Secret Tunnels and Dungeon Upper Tier. Connects south into the Ink Corridor.

  *The tunnel ends at a threshold — stone floor, stone walls, a passage leading south into darkness. Whatever is ahead doesn't announce itself. The air is different here: stiller, older, with a quality that suggests the dark ahead has been dark for a very long time. This is the end of the tunnels. The dungeon begins.*

---

## Dungeon — Upper Tier (15 rooms, FINALIZED)

**Critical path:** Dungeon Entrance → Ink Corridor → Supply Room → Narrow Passageway → Idol Room → Combat Room → Prayer Alcove → Portcullis Corridor → Shrine Room → Rickety Bridge → Mid-Tier Key Door

**Side branches:**
- Ink Corridor → east → Storage Area → Collapsed Gallery → Rickety Bridge (Quest 38 shortcut; dead-end until cleared)
- Combat Room → east → Creature Den → Flooding Room (spur; Trap 41; always a surprise)

### Ink Corridor
**XP: 1**
First room past the Dungeon Entrance. A thin cord stretched at chest height carries an ink bladder — triggering it douses the player in ink (negates invisibility). No warning; cord invisible until hit. Splits west to Supply Room, east to Storage Area. (Trap 45)

**Room description (default):** *The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead, west and east.*

**Room description (perception check passed):** *The corridor is narrow and plain — bare stone, low ceiling, torch brackets empty. It feels like an entrance to something, which it is. The passage splits ahead, west and east. A thin cord stretches across the passage at chest height — easy to miss. Something is attached to it.*

### Supply Room
**XP: 1**
West branch off Ink Corridor. Shelves of old stores. Contains: sack of salt ("looks like it weighs as much as a Chachapoyan Fertility Idol"), mortar compound (Quest 18/22), portcullis bar (Quest 19), smoke jar (Quest 24 — guarded by Trap 17). **Trap 17:** A shelf of clay pots — disturbing without disarming smashes one pot, 1 heart smoke damage; smoke jar and small clay pot (Quest 40) visible in wreckage either way. Perception spots the unstable arrangement. The small clay pot is the one intact pot that survives the collapse. Must be reached before Idol Room — sack of salt required for safe idol swap.

**Room description (default):** *A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned. The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath.*

**Room description (perception check passed):** *A storage room, wide and low. Shelves run along three walls — some collapsed, most still holding whatever was left here when this place was abandoned. The contents are various: tools, containers, materials that suggest someone was keeping this dungeon supplied. It smells of old wood and something chemical underneath. One of the shelves near the entrance has a trip mechanism built into the floor in front of it — barely visible. Whatever it triggers, it isn't subtle.*

### Narrow Passageway
**XP: 1**
Short connecting passage between Supply Room and Idol Room. Enforces item-first ordering.

**Room description:** *A short passage, plain stone, lower-ceilinged than the corridor behind you. It goes south and ends at a doorway. The kind of passage that exists to connect two places and has no opinion about either of them.*

### Idol Room
**XP: 1**
South end of Narrow Passageway. A **Chachapoyan Fertility Idol** sits on a pressure-sensitive pedestal. Removing without replacing with equal weight slams a stone door — no exit without crowbar (`PRY DOOR`, strength check). Safe swap: `SWAP IDOL WITH SALT` with sack of salt. Idol is treasure. Connects south to Combat Room. (Trap 33)

**Room description (default):** *The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake.*

**Room description (perception check passed):** *The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level. At the center, a stone pedestal holds a figurine. The room has the feeling of something that has been waiting for someone to make a mistake. The pedestal has a pressure plate built into its surface — the figurine's weight is the only thing keeping it inactive.*

### Storage Area
**XP: 1**
East branch off Ink Corridor. Wide chamber. Contains: hand cart (Quest 32), support beam (Quest 38). No passage deeper — only forward via Quest 38 shortcut once cleared.

**Room description:** *A wide chamber, larger than expected — the dungeon opens up here before closing back down. The walls are rough, the floor uneven. Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. The east wall is solid. The south passage is blocked.*

### Collapsed Gallery
**XP: 1**
South of Storage Area. Timbers wedged across it blocking a secondary exit (Quest 38). Pickaxe from mine required; three strength checks clear the timbers; propping with support beam makes shortcut permanent. **Exit opens into the Rickety Bridge** — bypasses everything above Shrine Room.

**Room description (blocked):** *The passage runs south but doesn't get far. Heavy timbers have come down across it — not from collapse exactly, more like someone wedged them there deliberately. The wood is old but solid. Beyond them, darkness.*

**Room description (cleared):** *The passage runs south, clear now. The timbers that blocked it are gone, the support beam holding the way open. The shortcut saves time — significant time.*

### Creature Den
**XP: 1**
East of Idol Room, adjacent to Combat Room. Lair of **The Warden** — permanently empty after defeat. On examination post-fight: remnants of a uniform/insignia mark this as an official post. The Warden drops the **Guardian's Lantern** on defeat.

### Combat Room
**XP: 1**
South of Idol Room. A pressure plate in the corridor before this room rings a bell in the Creature Den — player hears the sound before entering. **The Warden** emerges: completely monstrous in appearance; standard combat; one-time fight. **Trap interaction:** Perception check spots the plate; disarming bypasses the fight; `JUMP ON PLATE` triggers deliberately. Enchanted Glasses auto-reveal the plate. Spur east leads to Flooding Room. Connects south to Prayer Alcove. (Trap 29)

### The Warden's Drop
**Guardian's Lantern** — magical lantern. `TURN ON LANTERN` or `LIGHT LANTERN` both work. Flickers but does not light anywhere except the Dark Room in the lower tier, where it cuts through magical darkness and opens passage forward.

### Flooding Room
**XP: 1**
Spur east off Combat Room, through/past Creature Den. Low-lying cave. Pressure plate opens a sluice — floods the room in two turns. Three levers: Left (stuck, permanently spent), Right (breaks off, permanently spent), Middle (correct, closes sluice). No warning on entry. After a wrong pull on turn 1: explicit warning *"The water is at your knees. One turn left."* Failure sweeps player through sluice into mid tier directly below — one-way, no damage. Perception check *before entry* spots the suspiciously clean pressure plate; disarming jams it. (Trap 41)

### Prayer Alcove
**XP: 2**
South of Combat Room. A low stone alcove — looks like a dead end until examined. Carved niche in the back wall. Contains: **crowbar** (Quests 19&30, 25; Trap 33 escape); **vial of glacier melt** (Quest 34 mid room freeze). Perception check reveals full depth. Connects south to Portcullis Corridor.

### Portcullis Corridor
**XP: 1**
South of Prayer Alcove. A metal portcullis blocks the corridor, carrying an arcane charge. Touching without disarming: 1 heart lightning damage, stunned one turn. Three ways through: (1) perception spots charge and discharge mechanism; (2) disarm check discharges safely; (3) strength check lifts — only after discharge. Portcullis Bar from Supply Room props it permanently open. Without the bar it drops when released. (Trap 19)

### Shrine Room
**XP: 1**
South of Portcullis Corridor. A small carved stone room, older than surrounding dungeon stonework. Contains one of three Verdant Circle shrine bowl pieces (Quest 49) — visible on a perception check. Connects south into the Rickety Bridge.

**Room description (default):** *The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.*

**Room description (perception check passed):** *The room is older than the dungeon around it — the stonework finer, the walls carved rather than cut. Someone built this with intention. A shallow bowl depression is set into a stone plinth at the center. The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time. Something catches your eye near the base of the plinth — a curved fragment, stone, fitting the bowl's edge exactly.*

### Rickety Bridge
**XP: 1**
Short connecting passage between Shrine Room and Mid-Tier Key Door. Quest 38 shortcut exits here from the west. **Weight mechanic:** Carry weight limit: 12. If inventory exceeds limit, bridge groans and movement south is blocked — player cannot proceed until carry weight is at or under limit. Must drop items on this side, cross, then return for them. Always crossable at or under limit.

**Room description (default):** *A narrow stone bridge over a gap in the dungeon floor. The bridge is old — the stones have shifted slightly in their mortar, the edges worn. It looks crossable. It probably is. The far side leads south to a heavy iron door.*

**Room description (over weight limit):** *The bridge groans under your load — a deep, unhappy sound from somewhere in the stone. It isn't going to hold. You'll need to lighten what you're carrying.*

### Mid-Tier Key Door
**XP: 1**
South end of Rickety Bridge. Heavy iron door. *The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.* Lockpick attempt returns: "This lock can't be picked." Finding this door triggers Quest 32 discovery and unlocks May's three-tier hints. Middle Tier Key (Quest 32 reward) is the only way through.

---

## Dungeon — Middle Tier (15 rooms, FINALIZED)

**Key side** (10 rooms) accessed via Mid-Tier Key Door. **Trap side** (5 rooms) accessed via Flooding Room sweep only. Hole to Below (Stored Room collapse) is the only route to the lower tier.

### Key Side

#### Key Door Landing
**XP: 1**
Base of the key door staircase. Rough-cut cave room. Connects south to Mine Passage.

**Room description:** *The staircase deposits you in a rough cave at the bottom — low ceiling, unworked stone, the kind of room that exists because something had to be at the bottom of the stairs. The air is cooler here, damper. The passage continues south.*

#### Mine Passage
**XP: 1**
Worked cave section, old support timbers and rusting tools. Contains: charcoal (Quest 28, no perception check); silver dust (Quest 4, perception check); large iron chest bolted to floor — lockpick-only (Back Alley mugger's lockpicks), contains 20 Zenni. Connects south to Stored Room.

**Room description (default):** *A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall.*

**Room description (perception check passed):** *A worked section of cave — support timbers at intervals, rusting tools left where they were dropped. The smell of old rock dust is thick here. Someone mined this passage, or used it as a route through to something being mined. A large iron chest is bolted to the floor against one wall. A faint shimmer near the base of one timber catches your eye — silver dust, settled into a crack in the stone.*

#### Stored Room
**XP: 1**
Deliberate rubble fill hiding a hole. Spur east to The Crevice.

**Before digging:** *The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.*

One `DIG` (shovel required) collapses floor permanently → Hole to Below; spur east buried permanently. Beam exposed by collapse — `TIE ROPE TO BEAM` (rope from Docks) enables bidirectional travel. `DOWN`, `UP`, `CLIMB DOWN ROPE`, `CLIMB UP ROPE` once rope tied.

**After digging:** *Apparently the "something" being covered was a giant hole. The floor is gone — caved into the darkness below where the rubble gave way.* [Rope detail once rope tied off.]

#### The Crevice
**XP: 1**
Dead-end spur east of Stored Room. A skeleton is wedged in a narrow crack — tried to squeeze through and failed. Gold pocket watch hangs from one outstretched finger. `TAKE WATCH` (Trophy Case treasure). Permanently inaccessible after Stored Room collapses — **missable**.

#### Inscription Chamber
**XP: 1**
Ancient inscription on cave wall (Quest 28: `RUB PAPER ON ENGRAVING` with thin paper + charcoal). Rune stone (Quest 42, perception check). Crawlspace in east wall leads to Cave Creature's Lair — revealed by Trap 8 (Rope Snare) trigger or perception check.

**Room description (default):** *A cave room, wider than the passage leading to it. One wall has been worked — smoothed and carved with an inscription, old enough that the edges have softened. The other walls are natural stone, unmodified.*

**Room description (rune stone found):** *...A small pale stone near the base of the carved wall catches your eye — etched with faint lines.*

**Room description (crawlspace found):** *...A low gap in the east wall, partly shadowed — easy to miss. It goes back further than it looks.*

Both perception checks are independent — either, both, or neither may fire on a given visit.*

#### Cave Creature's Lair
**XP: 2**
Accessed via crawlspace off Inscription Chamber. Creature absent, never encountered. Bone flute on floor (Quest 7).

#### Echo Alcove
**XP: 1**
Listening station. One-way acoustic connection to the Antechamber in the lower tier — the sound of bones grinding drifts up from below. Same text every visit: *"A faint grinding drifts up from somewhere far below — bone on stone."* No interaction, no commands.

#### Magnetic Vault
**XP: 1**
Heavily magnetic room. Trap 15 (Magnetic Chest) on central chest — opening without disarming yanks all metal items to the chest. Perception reveals metallic filings in ring around latch; disarm removes lodestone from lid. Diamond brooch inside (second most valuable treasure in game).

**Room description (default):** *A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall points toward it. Dust has settled in a faint ring around the latch.*

**Room description (perception check passed):** *A square room, stone walls, a single chest at the center on a low stone platform. The room feels subtly wrong in a way that takes a moment to identify — small metal objects have drifted toward the chest, as if drawn. A nail in the wall points toward it. The ring of metallic filings around the latch is deliberate — a lodestone is built into the lid. Opening the chest without removing it first would be a problem.*

#### Deep Lock Door
**XP: 1**
End of key side critical path. Permanently sealed — no key, no lockpicks, dead end. Lower tier reached only via Hole to Below.

**Room description:** *The passage ends at a door set deep into the stone. It is sealed absolutely — no lock visible, no handle, no gap at the frame. Whatever mechanism holds it closed is on the other side, or nowhere. This door does not open. The passage ends here.*

### Trap Side (5 rooms — entered via Flooding Room sweep only)

#### The Spillway
**XP: 2**
Wet, low-ceilinged chamber at base of sluice. One-way drop from upper tier. No exits except south.

**Room description:** *The sluice deposits you here — wet stone, low ceiling, the sound of water draining somewhere below. The chamber is small and close. There's no way back up. The passage continues south.*



#### Dream Corridor
**XP: 2**
Liminal branching passage. 2×3×2 decision tree — 12 outcomes (6 success, 6 failure). Failure loops back to room start with no awareness. Full tree in `mechanics.md` (Special Mechanics section).

#### Lost Apprentice's Cell
**XP: 2**
Quest 50: combat with afflicted apprentice; post-combat `USE SHOVEL` finishes hole to Bog-NW; apprentice follows player out; Apprentice's Gloves reward (hands slot, +3); quest completes on bog exit.

#### Supply Cache
**XP: 2**
Partially collapsed side room. Contains a **gold nugget** — buried in rubble, treasure item.

#### Flood Sump
**XP: 2**
Lowest point on trap side. Shallow pool. No confirmed items.

**Room description:** *The passage ends here in a low chamber, the floor wet — a shallow pool covers most of it, fed by seepage through the walls. The water is still and dark. The ceiling is close. This is the lowest point down here, and it feels like it.*

---

## Dungeon — Lower Tier (17 rooms, FINALIZED 2026-06-04)

**Entry:** Hole to Below (rope required to return). Deep Lock Door — permanently sealed, no entry from mid tier.

### Layout

```
                                          [Quest 34 Fountain Room]
                                                    |
                                                    N
                                                    |
                                            [Quest 34 Mid Room]
                                                    |
                                                    N
                                                    |
                                              [Tool Alcove]
                                                    |
                                                    N
                                                    |
[Thermal Vent Room] (dead end)
        |
        N
        |
  [Lower Crypt]
        |
        N
        |
[Pile of Rubble] - E - [Antechamber] - E - [The Junction] - E - [The Narrow Pass] - E - [The Still Den]
        |                   |                     |
        S                   S                     S
        |                   |                     |
 [The Encampment]     [Skeleton Room]         [Dark Room]
                       (unreachable)               |
                                                   S
                                                   |
                                             [Spirit Room]
                                                   |
                                                   S
                                                   |
                                           [Burial Chamber]
```

### Pile of Rubble (Room 1)
**XP: 2**
Bottom of Hole to Below. Rope anchor point for return to mid tier.

*The ceiling is a jagged wound — stone and packed earth hanging at the edge where the floor above used to be. Below that: the rubble that was the floor, now a rough-graded pile you're standing on. The air smells of disturbed earth and something older underneath it. Passages lead further in.*

### Lower Crypt (Room 2)
**XP: 2**
Keeper's skeleton under inert pendulum blade. Key ring on skeleton.

**Room description:** *A rough cave, low-ceilinged and close. A pendulum blade hangs motionless from the ceiling — triggered long ago, dried blood on the edge. Beneath it, a skeleton in robes. Whatever the Keeper came down here to do, this is as far as he got.*

**Key item descriptions:**
- Keys on skeleton (in room): *"The skeleton's fingers are curled loosely around a ring of keys."*
- Keys in inventory: *"A ring of keys, old iron, worn smooth from years of use."*
- Keys dropped (after taken): inventory description persists — no revert to skeleton description.

The emerald wax seal on a cord around the skeleton's neck matches the seal on the statue note in Roundabout Town Square. Key opens the Keeper's Chamber in the Church of All.

### The Encampment (Room 3)
**XP: 2**
Scholar and Keeper's research area. Makeshift — bedrolls, scattered equipment, journals piled without order.

**Room description:** *The camp is old but not abandoned — abandoned implies a choice. Bedrolls still laid out. Equipment set down mid-use. Journals open to pages no one finished. Whatever happened here, no one saw it coming.*

No mechanical trigger — context and lore only.

### Thermal Vent Room (Room 4)
**XP: 2**
Dead-end spur. Warm air rises from fissures in the floor. Fire clay (Quest 49) pressed into ceiling overhang — invisible until `LOOK UP`; `TAKE CLAY` retrieves it. No perception check. Whispering Jar whisper (*"The ceiling of the thermal vent holds a secret."*) is the only hint anywhere.

### Antechamber / Bone Crunch Floor Room (Room 5)
**XP: 2**
Trap 36. Dry bones arranged plainly on the floor — no perception check needed.

**Warning text:** *"The sound is coming from beyond that doorway — bone grinding on stone, steady and unhurried. You get the distinct impression that silence is not optional here."*

`CLEAR BONES` disarms. Moving through without clearing: instant death.

**Death text:** *"The bones crack underfoot. The grinding stops. Then the doorway fills."*

### Skeleton Room (Room 6)
**XP: 0** (instant death on entry — XP unreachable)
Dead end south of Antechamber. 6–9 undead skeletons. Instant death on entry. Never required — nothing inside.

### The Junction (Room 7)
**XP: 2**
Navigational fork east of Antechamber.

*The passage widens here into a rough junction, the stone walls bearing the marks of tools long since abandoned. Three directions offer themselves without comment. The floor is grit and old dust.*

**50/50 text — fires when player exits Tool Alcove (Room 10) south into The Junction, before Tool Alcove discovery only. One of two variants selected at random:**
- *"As you step back into the junction, you're not sure why, but you feel like you left something unfinished back there."*
- *"Behind you, north, there's a sound — or almost a sound. Gone before you can name it."*

### The Narrow Pass (Room 8)
**XP: 2**
Long narrow passage east of The Junction leading to The Still Den.

*A long passage, barely wide enough for your shoulders. The walls are close and the ceiling drops as you move east. Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.*

### The Still Den / Werewolf's Room (Room 9)
**XP: 2**
Undead werewolf — critical path. Cannot be harmed by conventional weapons. Only `DRIVE STAKE INTO WEREWOLF` (stake must be consecrated with holy water first) destroys it. Reverts to scholar appearance on death. Ivory Torch mounted on wall — take before leaving. Werewolf drops **Werewolf's Amulet** (ring ritual artifact, The Veil of the Arcane).

**Room description (werewolf alive):** *A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. It is very still right now. That changes the moment you enter.*

**Room description (post-combat):** *A wide cave, low but not cramped. The walls are gouged at every height — long parallel marks, overlapping, years of them. The floor is worn smooth in a rough oval, the path of something that has been pacing this space for longer than it can remember. The scholar lies where the creature fell.*

**Death/reversion text:** *The creature drops. Between one moment and the next, it is not the creature anymore. The scholar lies on the floor of the cave he came down here to find.*

**TODO:** Werewolf combat mechanic — attack cadence, player options each turn.

### Tool Alcove (Room 10)
**XP: 3**
Quest 34 barrier room. North of The Junction. Speaking door disguised as back wall. Perception check required for discovery.

**Before discovery:** *"The passage ends at a shallow recess lined with iron brackets — the kind used to hang tools or equipment. The brackets are empty. The back wall is flat and featureless."*

**Perception check fires:** *"Something in the back wall notices you. You're not sure how you know that, but you do."* — immediately followed by persistent description.

**Persistent (after discovery):** *"As you focus on the back wall, it asks you something. Once. The sound of it fills the alcove and then is gone, leaving only the clear impression that an answer is expected."*

**`READ SCROLL` response:** *"The wall goes quiet in a way it wasn't quiet before. Then, slowly, it opens. You get the sense it had begun to doubt anyone would ever answer."* — scroll consumed; passage north opens permanently.

**Open state (all future visits):** *"The passage ends at a shallow recess lined with empty iron brackets. The back wall stands open. It has nothing left to ask."*

**Pull-back mechanics (before discovery only):**
- Freed soldier (town re-appearance, Quest 34 complete in another playthrough context — see npcs.md): *"There's a room down there that talked to me once. I never figured out what it said."*
- 50/50 text on Junction exit — see The Junction (Room 7) above.

### Quest 34 Mid Room (Room 11)
**XP: 2**
North of Tool Alcove. A channel of dark water fills the room wall to wall — narrow but uncrossable.

**Room description:** *Everything in this room is becoming the pool. Water seeps through the walls in thin lines, runs down the stone, disappears into the dark surface below. The ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless as far as you can tell. The passage north is visible on the other side. The water is between you and it.*

**Swimming penalty:** *The moment you enter, the water is inside you somehow — not wet, not cold, just wrong. The pain that follows is real and serious and spreads fast. You are back at the doorway, bleeding from nowhere you can see.* (1 heart arcane damage; player returned to doorway automatically.)

**Freeze solution:** `POUR VIAL IN WATER` (vial of glacier melt from Prayer Alcove, upper tier) freezes the pool; player crosses freely.

### Quest 34 Fountain Room (Room 12)
**XP: 2**
North of Quest 34 Mid Room. Contains a soldier encased in a block of magical ice — alive but suspended.

**Room description:** *Cold stops you at the threshold — not wind, just cold, settled and absolute. The fountain to your left has been frozen mid-pour for what might be a very long time. The block of ice in the center of the room is frosted thick, but not so thick you can't see the shape inside it. A person. Standing. Composed.*

**Turn 1 (`HOLD TORCH NEAR ICE`):** *The ivory torch throws heat that seems wrong for its size. Where the flame meets the ice, the frost retreats — a wet gleam spreading outward from the torch's reach. A single deep crack sounds from somewhere inside the block — not shattering, just shifting. A small clear window opens in the surface. Through it, the figure is closer than expected. Still composed. Still waiting.*

**Turn 2 (`HOLD TORCH NEAR ICE`):** *The crack deepens — then several more, fast, branching outward from the window. The block doesn't collapse so much as release. The ice falls away in sheets, and the soldier steps forward out of it as if he had been about to do so anyway. He blinks. He looks at his hands. He looks at you.*

**Soldier handoff:** *He looks at the sword at his side as if surprised to find it still there. He draws it and holds it out to you without ceremony. "The Forgotten Blade," he says. "It has no business down here." Neither, apparently, does he — he moves past you and is gone before you can speak.*

Soldier reappears in town as a minor NPC offering free weapon training sessions. Reward: **The Forgotten Blade** — see `items.md`.

### Dark Room (Room 11 — Dark branch off The Junction)
**XP: 2**
Magical darkness fills the passage ahead. Hard block without Guardian's Lantern. Normal torches and Light spell ineffective.

**Before lantern:** *You cannot see anything. This is not like being in the dark. This is something the dark is doing on purpose.*

**Lantern reveal:** *The lantern opens and the darkness collapses. No gradual brightening — one moment nothing, the next a plain stone room, fully lit, as if it had always been waiting to be seen. Unremarkable in every way except one: it is not dark. After what just happened, that feels like quite a lot. There is a hook on the wall. You hang the lantern on it. It feels like the right thing to do, and apparently it was.*

**Persistent (lantern hung):** *A plain stone room, unremarkable in every way. Stone walls, stone floor, a passage north. The Guardian's Lantern burns steadily on the wall. It is not dark.* Lantern stays on wall permanently — in room but not takeable.

### Spirit Room (Room 12 — Dark branch)
**XP: 2**
6–9 silent spirits. Hard block both directions while player is visible. One Ring required. Spirits cannot be killed. South of Dark Room.

**Room description:** *The room is silent. Shapes drift through it — sparse, irregular, neither here nor entirely anywhere. They are not human. They are not entirely not human. They take note of you the moment you enter. The passage north is visible. Getting there is another matter.*

**Attempt to pass while visible:** *The shapes collect between you and the passage. Not blocking — just there, watching, closer than they were. You sense that pressing forward would be a mistake you wouldn't finish making.*

**Ring on:** *The attention in the room drops all at once — not gradually, immediately. The shapes drift back to their own patterns. They have forgotten you entirely.*

### Burial Chamber (Room 13 — Dark branch)
**XP: 3**
South of Spirit Room.

*The chamber is circular, the walls carved with processions of figures — mourners, by the look of them, rendered in a style no living hand in Roundabout would recognize. Niches hold candles that have not burned in centuries, wax melted flat and cold. The plinth at the center holds the mask. Everything in this room was arranged deliberately, long ago, by people who are not coming back.*

Contains **Funeral Mask of Hammered Gold** (treasure) on central plinth. Taking the mask triggers no reaction from the spirits.

### Trap Side Rooms (Rooms 14–17 + Flood Sump)
These rooms are physically part of the mid-tier trap side, entered via the Flooding Room sluice sweep. Full room definitions are in the **Dungeon — Middle Tier / Trap Side** section above. XP values are defined there.
