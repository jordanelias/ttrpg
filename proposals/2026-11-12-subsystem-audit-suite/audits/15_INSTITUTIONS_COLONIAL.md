# INSTITUTIONS — COLONIAL: empire at distance and empire-maintenance, adapted to Valoria

## Status: REFERENCE (a design and plan in proposal form; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: bb6dfc3 (working tree)

Lane: institutions, FAMILY=COLONIAL (`INSTITUTIONS_BRIEF.md`). Sourcing marks used throughout:
`[TREE]` = stated in the tree's research at the cited path (itself tier 3, secondary); `[MEMORY]` =
memory-grade, from general reading, not checked against a source this session; `[UNVERIFIED]` = a
specific figure or date not checked. **Shapes are the durable finding; every figure is a lead.**
`[CHECKED]` on a code or canon claim means the file was opened at that place this session.

---

## 0. Verdict

**Valoria does not need a colonial empire added to it: it is already a post-colonial realm with the
former metropole on its border, and every colonial mechanism the brief names has a site in the world as
it stands, built out of the primitives the engine already carries (seat, rung, `oblige`, `covenant`,
`dispensation`, `transfer`, `requisition`, `seize`, `march`, `ban`, `petition`, `determine`).** The single
largest obstacle is not a missing primitive but a missing *distance*: the engine has no cost for governing
far from where you sit. Every binding decision is known to every living person at once
(`epistemic.py::_ch_chronicle`, §3.1); a levy taken three territories away is taken as surely as one taken
in the next room (`requisition` and `transfer` are unrolled, §3.2); no appointed agent drifts toward the
people he governs; no term ends in an audit. So a governor at the end of a road behaves exactly as a clerk
beside the throne, and the stories the institution exists to produce (the over-mighty marcher lord, the tax
farmer who becomes a power, the charter that hardens into a right, the settler community that outgrows its
founder, the client elite that changes patron) cannot arise.

**Nothing in this design is decided by a fixed rule (Jordan's standing rule, 2026-11-12: *"We do not do
deterministic"*).** Every consequential colonial outcome is a draw on the engine's one roll form (pool
against an obstacle that is the task's difficulty plus named modifiers, four graded bands), with the odds
set by persons, seats, distance and venue: **what a levy yields**, **whether an order carries its force to
a far addressee**, **whether tribute arrives**, **whether a charter is upheld when it is called in**,
**whether an audit finds what the governed swear to**, **whether a revolt's field is won**. State sets the
odds; a well-placed governor still loses a convoy sometimes and a hated one still collects sometimes.
What stays arithmetic is only bookkeeping (stores conserved, a term's clock, who holds a seat). The one
new obstacle term this lane asks for is **`remove`** (how far the exercised seat sits from what it acts
on, §3.2); the one new registry is **`instruments.yaml`** (the closed set of grant and treaty forms, §4);
the rest is content: rows in `offices.yaml`, `arrangements.yaml`, `rosters.yaml`, `goals.yaml` and the
cast.

The four sites, in the world's own terms (canon citations in §1):

| # | colonial mechanism | where it already sits in Valoria |
|---|---|---|
| A | **The metropole and its frontier governor** — empire at distance, the information delay, reconquest or re-absorption by treaty, hostage-kin, the trade prefect | **Altonia**: the Katepano and the Kommerkiarios (`offices.yaml: foreign_seats`), the Doux, the "ancient trade treaties", the tutoring demand on Prince Torben |
| B | **Indirect rule through a contained institution, and its reversal** — the grant of a jurisdiction in exchange for quiet; missions; the client that outgrows the patron | **The Church of Solmund's containment grant** (Himmelenger, T9), now run in reverse by the Church against the Crown; the Solmundan minority inside Altonia |
| C | **Conquest tenure and vassalage** — the crown and two ducal houses founded by ranked accomplishment in the Secession War; what a conquest-founded house owes and is owed; marcher liberty; internal colony | **The Crown, Hafenmark, Varfell** (`off_king.obligees`); the **caste gradient** on the southern Einhir; the "instrumental" southern Crown territories; **Askeheim** (T15), held by no faction |
| D | **The chartered company and the entrepôt** — monopoly by charter, the trade fort, the factor, the company that governs | **Schoenland** (neutral offshore trade nation, T16), the **Guilds** and the Hafenmark charter tradition, the harbour sites |

What this lane decides, in one line each (the body gives evidence and the exact edits):

1. **No new carrier type is admitted.** Charter, monopoly, land grant, tribute, wardship, tax farm,
   capitulation and protectorate are `dispensation` Records (minted by `issue` downward, `covenant`
   across) whose terms are read from a row of one new closed registry, plus seats and `oblige` Tenures
   the engine already has. The cut test fails for a `Charter` type, a `Colony` rung kind and a `Company`
   faction kind (§4.4).
2. **Distance is a property of the path, not of the institution** (§3): one obstacle term, `remove`,
   read off the `contain` chain and the geography file's adjacency, entering every roll made through a
   seat on something far from it; and news crosses a border only in a person or a paper.
3. **Rank is a ranked ledger of accomplishment** and the Secession War is its first three entries
   (§5). The tree disagrees with Jordan's statement in two places; both are named in §5.2. One is
   reconciled by reading; one is canon text and is listed in §11.
4. **Nine existing verbs gain behaviour, none is added** (§6): `covenant`, `issue`, `requisition`,
   `transfer`, `oblige`, `release`, `seize`, `open_case`/`determine` (two new arrangement rows), and
   `found`. A proposed tenth, `audit`, fails its cut test: it is `open_case` under a new arrangement row.
5. **The first playable scenario is "The Farm of the Southern Tolls"** (§9): a Crown seat farms the
   revenue of Stillhelm to a holder for a term; each season the farmer chooses how hard to press and
   rolls for what the place yields; the governed petition or leave; the term ends in an audit hearing
   whose verdict is a draw weighted by what was sworn and held. Playable from the farmer's seat, the
   grantor's seat or a petitioner's hearth, on the code the season loop runs.

Sections follow the brief's order. §11 lists what survives to Jordan (three items).

---

## 1. The world's actual overseas, frontier and holding structure (read from the tree)

Everything in this section is read from code or canon; where a design document is the only source it is
marked as intent.

### 1.1 Valoria is a former colony, and the metropole is next door

`canon/03_canonical_timeline.md` [CHECKED :54–:106]:

- **Altonia conquered the peninsula and held it for about two centuries** (~50–200 AG). The canon's own
  word is "colonial" (:50, :54, :58, :76).
- **Containment through accommodation** (:58): Altonia could not suppress the Church of Solmund, so it
  granted it "a cathedral city (Himmelenger, T9) with tax-exempt religious lands, educational rights,
  archival authority, and charitable operations", in exchange for staying inside a jurisdiction, not
  mobilising followers, and providing "pastoral services that reduce Altonian administrative burden".
  The canon names its own parallel, British India (:60). **This is indirect rule through a client
  institution, already canon.**
- **Incubation** (:62): two centuries inside the container produced "the most institutionally mature
  organisation on the peninsula". **The cage became a school** (:68): at game start the Church applies
  "Altonia's containment logic in reverse", making itself indispensable to the Crown.
- **Cultural imperialism** (:66): Altonia "systematically destroys Valnese records, monuments, and
  temples", which is why no claim to ancient blood can be proved (:80) — the root of deed-monarchy.
- **Cross-border presence** (:64): "Altonia's own population includes a significant Solmundan minority";
  the Church has "Altonian missionaries" (:118). **The mission runs from the former colony into the
  former metropole.**
- **The Secession Wars** (~195–200 AG, :72–:106): a coalition of the three nations — Valorsmark,
  Baiamont (later Hafenmark), Lupicco (later Varfell) — "primarily northern"; the first Almqvist's
  "leadership proves decisive"; "authority is entirely earned through wartime deeds"; the Church
  consecrates. "The Crown is first among equals"; "ducal authority cannot be unilaterally overridden";
  "the Baralta family's ducal status was earned through wartime deeds" (:88–:90).
- **The caste** (:94–:100): the informal second-class status of the southern Einhir is "the structural
  consequence of the south's exclusion from the war coalition's leadership"; "stigma radiates from the
  Southernmost"; "southern Crown territories are viewed as instrumental". **This is the realm's internal
  colony**: a periphery governed for the centre's purposes, by people marked as lesser.
- **After independence** (:110–:122): trade reopened through **Schoenland** (220–235 AG, "politically
  toxic"), then **direct trade routes with Altonia** (238 AG) "ratified by Elske's marriage to Doux
  Alexios Laskaris"; "militarised trade routes"; "Altonia eyeing [Prince Torben] as leverage"; an
  Altonian **tutoring demand** on the prince (:141). **Schoenland** is "a neutral offshore trade nation
  outside the realm" that "trades with both Altonia and Valoria without regard to whether they are at
  war" (:167, ED-IN-0356).

### 1.2 What the engine carries of it today

- **The rung ladder** `person → hearth → community → settlement → territory → province → duchy → realm`
  (`rosters.yaml: rung_kinds`) [CHECKED]. The authored realm goes realm → duchy → territory and has
  **zero `province` rungs** (`offices.yaml:510` note; `governance_spine.yaml:57–58`) [CHECKED].
- **Thirty-one authored seats** (`offices.yaml: seats`) and **two foreign seats** (`foreign_seats`):
  `off_katepano` ("Katepano", holder NPC-089, remit `[dispatch, issue]`, rung `{settlement: "ALT-1"}`,
  conferral and revocation both `null`: "canon names no way the empire fills or strips the post") and
  `off_kommerkiarios` ("Kommerkiarios", NPC-090, remit `[issue]`: "trade prefect at the Schoenland
  interface … Enforces ancient trade treaties") [CHECKED :607–:632]. They exist only in a world built
  with `build_realm(foreign=True)`.
- **`foreign_factions: [Altonia, Schoenland]`** and **`foreign_cast`** with one minted territory `ALT`
  and one settlement `ALT-1` (`rosters.yaml`) [CHECKED by load]. Schoenland has no seat and no place.
- **Vassalage is one field**: `off_king.obligees: ["NPC-070", "NPC-050", "NPC-052"]` — the Grand Master,
  the Duchess of Hafenmark and the Duke of Varfell hold an `oblige` Tenure toward the King's seat, "the
  King's vassals, sworn by the same path" (CR-86, ED-IN-0342; `offices.yaml:196`) [CHECKED]. The
  obligation has **no term and no declared content** (`:132–:133`: "with no term … a seat seeded at
  world-gen has no opening act to declare one").
- **How the three founding seats are filled, as coded** [CHECKED `offices.yaml:187–:237`]:
  `off_king` → `conferral: inheritance` (claimed by the holder of the heir title); 
  `off_duchess_hafenmark` → `conferral: null`; `off_duke_varfell` → `conferral: elected` ("first among
  the Jarls, not a monarch"). Both ducal seats: `revocation: rung_above_in_holdings`, and "no duchy is
  [in the monarch's holdings], as built … so nobody strips them until content places one" (:85–:88).
- **Conferral bases** `[appointed, elected, annex, inheritance]`; **revocation bases**
  `[rung_above_same_faction, rung_above_in_holdings]` (`rosters.yaml`) [CHECKED by load]. `annex` is the
  ruled word for a seat taken with the ground (ED-IN-0256) and is the conquest basis this lane builds on.
- **Tenure kinds** `[hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban]`; **record
  kinds** include `dispensation {terms, to, at}`, `petition`, `works`, `faction_sheet`, `cover`, `army`
  [CHECKED by load]. **Matter kinds** `[grain, salt, timber, ore, coin]`; **site kinds** include
  `harbour` and `garrison`.
- **Thrust axes** already name the colonial stakes: `purge_altonia`, `overthrow_caste`, `uphold_caste`,
  `revive_einhir`, `suppress_einhir_revival` (`rosters.yaml: thrust_axes`) [CHECKED by load].
- **The one ending**: `peninsular_sovereignty` — one faction holding every `territory` rung
  (`rosters.yaml: endings`, GD-1) [CHECKED by load].

### 1.3 The ground (`systems/settlements/valoria_geography_v30.yaml`, read through `data/geography.py`)

Seventeen `provinces:` rows (the engine's territories), 37 settlements, 26 adjacency edges [CHECKED by
load]. The frontier and holding structure, in the file's own words:

| ground | territories | what the file says |
|---|---|---|
| **The northern passes (the Altonian frontier)** | T3 Lowenskyst (Crown, fort 3), T10 Spartfell (Hafenmark, fort 2) | `altonian_passes`: primary "Crown holds gate", secondary "Hafenmark holds gate"; a third, naval, "via Schoenland permission". Altonia is a **land empire beyond the mountains**, not overseas |
| **The mines** | T17 Halvarshelm (Hafenmark) | "Northern mines. Iron and copper. Guild operations"; S-023 "Guild labor presence" |
| **The granary** | T5 Feldmark, T2 Kronmark (Crown) | "Crown breadbasket. Hafenmark food dependency anchor" |
| **The southern gates (the calamity frontier)** | T6 Stillhelm (Crown), T13 Oastad (Varfell) | "Calamity-adjacent"; each a `gate` edge to T15 |
| **The unheld ground** | T15 Askeheim | `faction: Uncontrolled`, no settlement, "Calamity epicenter. Forgetting zone" |
| **The contained city** | T9 Himmelenger (Church) | "Altonian containment-placement"; S-036 "Sovereign ecclesiastical city-state" |
| **The entrepôt** | T16 Schoenland | "Independent island republic. Altonian trade. Naval choke control"; one `coastal` edge, to T1 |
| **Hafenmark's holdings** | T7, T8, T10, T17 | highland, timber, mines, a pass; T8 Gransol "West sea trade. Schoenland route" |
| **Varfell's holdings** | T4, T11, T12, T13 | fjords and highland; the caste gradient's high end (canon :100) |

There is **no overseas possession and no province rung**; the realm's "empire at distance" is measured in
territory hops on this graph (the longest shortest path inside the realm is T3 to T13, [UNVERIFIED]
length), across one mountain border to Altonia and one strait to Schoenland.

### 1.4 What a built realm holds (probe, §15 E-1: `build_realm(0)`, no season run, `PYTHONHASHSEED=0`)

- 83 persons, 34 offices, 414 rungs, 2 Records (both `works`), 70 Propositions (66 OUGHT, 4 HOLDS).
  **No `dispensation` exists at build**: the "ancient trade treaties" the Kommerkiarios enforces, the
  containment grant, the settlement of 200 AG and the ducal liberties are in no Record.
- **Four `oblige` edges**, all without a term: NPC-041 → `off_restoration_leader`; NPC-050, NPC-052,
  NPC-070 → `off_king`. Through them `purview_reaches(off_king, …)` is True for `duchy_hafenmark`,
  `duchy_varfell`, `terr_T8`, `terr_T12`, and (by containment) `terr_T9` and `terr_T15`; False for
  `terr_T16`, `terr_ALT`, `set_alt_1`. So **the vassal oath is the only thing that puts the duchies under
  the Crown**, exactly as `state/gate.py:422-449` states (the oblige clause, one edge deep, a detachment
  is the edge ceasing to be live).
- Altonia: three persons (NPC-011, NPC-089, NPC-090) at `set_alt_1`, two seats, both `conferral: None`,
  `revocation: None`. **Schoenland: one cohort at `set_s_037`, no named person, no seat.**
- Every treasury rung reads empty stores at build (`r_valoria`, the three duchies, `terr_T1`, `terr_T9`,
  `set_alt_1`, `set_s_037`) under the shipped `endowment_mode: uniform` (SE's
  `07_SE_treasury_granary_B.md` is the proposal that seeds them).
- Site kinds: 37 `harbour`, 37 `seam`, 37 `garrison`, 211 `dwelling`: one of each working site in every
  settlement, inland villages included (SE's finding; cited, not redone). **A harbour is therefore not
  yet a place on a coast**; §4.3's `staple` form is written so that it does not depend on that being
  fixed.

---

## 2. How it really worked

Sourcing: paragraphs marked `[TREE]` restate the tree's research at the cited file (tier 3, secondary,
itself verified once by an adversarial pass, `research/governance/00_MANIFEST.md`). Paragraphs marked
`[MEMORY]` are this lane's general reading, **not checked against a source in this session**: the tree
holds no research file on the chartered companies, the Spanish Indies beyond the residencia, settler
colonies, indirect rule in Africa and India, or the Mongol system (a grep of `research/` for those terms
returns passing mentions only, §15 E-2). Their **shapes** are well attested and are what the design uses;
every date and figure in a `[MEMORY]` paragraph is `[UNVERIFIED]` and nothing in the design depends on one.

### 2.1 The problem every such institution solves, and the three answers

A ruler wants revenue, soldiers and obedience from people he cannot see. His agent is far away, knows
more than he does, and is acquiring local friends (`research/fa_se_historical_precedent_research_v1.md`
T5, "the governor problem") `[TREE]`. Every colonial and imperial institution is one of three answers, or
a mixture:

1. **Send your own man and watch him** (bureaucratic governorship). Roman imperial provinces under
   *legati Augusti*, fixed terms of about one to three years, full civil and military authority within
   the province (`research/governance/governance_modes.md` Roman §5) `[TREE]`; the Castilian Indies'
   viceroys and *audiencias*, disciplined by the **residencia** (a judge collects sworn complaints from
   the governed at the end of every tenure) and the **visita** (an unannounced inspection mid-tenure)
   `[TREE: T5]`; the Carolingian **missi dominici**, paired itinerant inspectors
   (`governance_modes.md` Carolingian §1.5) `[TREE]`; the Ming–Qing **rule of avoidance** (no service in
   the home province, rotation about every three years) and the Censorate `[TREE: T5]`; Ottoman
   **timar** rotation, so that revenue rights did not congeal into local lordship `[TREE: T5;
   governance_modes.md Ottoman §7]`. *Cost:* salaries, and the watcher must himself be watched. *Decay:*
   **venality**: the French *paulette* made office heritable property for a fee, after which the crown
   "could no longer rotate, audit, or dismiss what it had sold" `[TREE: T2, T5]`; the Han inspector who
   becomes a regional ruler (`governance_modes.md` Han §1.7) `[TREE]`.
2. **Sell or grant the right and take a share** (the farm, the fief, the charter). Roman **publicani**,
   Ottoman **iltizam** and its life-term mutation **malikâne**, the French **Ferme Générale**: "cash now
   plus collection outsourced equals over-extraction by the farmer, odium accruing partly to the state,
   and the farmer becoming a political actor in his own right" `[TREE: T2]`. The **fief** is the same
   trade in soldiers: land and jurisdiction for service, by homage and fealty, with relief paid at
   succession, aid and counsel owed, forfeiture for breach, and the rule that the vassal of my vassal is
   not my vassal `[MEMORY]` (the engine has already taken this last rule, `state/gate.py:432-439`). The
   **marcher lord** is the fief at the frontier: quasi-palatine liberties (own courts, castles, private
   war) *because* he holds the border, "and precisely for that reason the crown's most chronic
   over-mighty-subject problem" `[TREE: T8]`. The **chartered company** is the same trade again, in
   commerce: a body of merchants receives by charter, for a term of years, a monopoly of trade beyond
   some line and with it the powers of a state there (to fortify, garrison, make treaties, coin, judge),
   in return for loans, customs and renewal fees; it is governed at home by a court of directors answering
   to shareholders and abroad by governors and factors at **factories** (fortified warehouses in someone
   else's port); its servants are paid little and trade on their own account; its charter comes up for
   renewal and each renewal is a political fight in the metropole; its interlopers are seized; and when
   it acquires territorial revenue it stops being a merchant and becomes a government that its own
   sovereign must then regulate and at last absorb `[MEMORY: the English and Dutch East India companies;
   dates UNVERIFIED]`. *Decay:* the grantee outlives the grant: privilege **hardens by age into right**
   (prescription); revoking it is "never an administrative act; it is a regime-legitimacy event" (Edward
   I's *quo warranto*; London's charter, 1683) `[TREE: T4]`.
3. **Leave the local ruler in place and rule him** (indirect rule, tribute, clientage). Roman client
   kings `[MEMORY]`; the Mongol practice of confirming a conquered prince by a patent and taking tribute
   through him, with a resident overseer and a census, the prince travelling to the khan's court to be
   confirmed and rivals bidding there for the patent `[MEMORY]`; Ottoman tributary states; **Ragusa**,
   which paid tribute for centuries "while prospering", against the **Danegeld**, the extortion spiral
   `[TREE: T10]`; the Ottoman **millet**, confessional self-government under its own head
   (`governance_modes.md` Ottoman §4) `[TREE]`; in the modern empires, the resident at a prince's court,
   the subsidiary treaty (the prince pays for the garrison that controls him), and the rule that a line
   without an heir lapses to the paramount power `[MEMORY]`. **Hostage-kin** make it hold: the
   Tokugawa **sankin-kōtai** (`governance_modes.md` Shogunate §1.9) `[TREE]`; sons raised at the
   overlord's court `[MEMORY]`. *Cost:* almost nothing. *Decay:* the client changes patron; or the
   contained institution uses its protected space to grow, which is the tree's own canon for the Church
   (§1.1).

### 2.2 Extraction, and what makes it explode

`[TREE: T1, T3]` Effective yield is rate × base × compliance, and compliance rises with the governed's
belief that the demand is fair and that others are paying (Levi's quasi-voluntary compliance).
Administrative capacity raises yield without raising resentment proportionally (Brewer). **It is the
invariance of the demand in a bad year, not its level, that detonates revolt** (Scott); crowds target
millers and forestallers before the state (Thompson); famine is a failure of access, not of supply (Sen).
Forced labour drafts and tribute in kind by rotation among subject communities (the Andean *mita*, the
*repartimiento*, corvée) `[MEMORY]` are the same extraction paid in hands instead of stores; the
*encomienda* granted a settler the labour or tribute of a named community in return for its protection
and instruction, and the crown spent a century trying to stop it becoming heritable `[MEMORY]`.

### 2.3 Settlement, the garrison and the frontier

`[TREE: T8]` Soldier-settlers hold land for service: Byzantine *themata*, the Habsburg **Militärgrenze**
(land, toleration and exemption from dues for perpetual militia duty), Roman *coloniae* and *limitanei*,
Cossack hosts, Chinese *tuntian*. Towns are planted or chartered as magnets: "town air makes free after a
year and a day" `[TREE: T4]`. Settler societies proper received land by grant per head brought over,
governed themselves in assemblies under a charter or a proprietor, were left alone for generations, and
revolted when the metropole, after a costly war fought partly on their behalf, began to tax, garrison and
restrict them without their assent `[MEMORY]`. **The settler–metropole conflict is a charter dispute**:
each side reads the same founding grant differently.

### 2.4 Conquest terms and the entry

`[TREE: T6]` A garrison that surrenders on terms keeps its property and the town is spared; one that
forces a storm forfeits protection; sack is cheap tactically and ruinous reputationally. The other half is
the **entry**: the new lord swears to the place's privileges and is paid for confirming them (the
*Joyeuse Entrée* of Brabant; accession charters). "A conqueror who confirmed bought cheap legitimacy at
the price of constrained extraction; one who imposed new law bought full extraction at the price of a
resentful base."

### 2.5 The Church's part

`[TREE: T7]` At the parish, the right to name the priest (advowson) and the local interdict. At the
frontier `[MEMORY]`: royal patronage over the colonial church (the crown names bishops in return for
funding the mission); the mission as a frontier institution that gathers, instructs and administers a
people ahead of or instead of the garrison; orders that become the natives' protectors against the
settlers and are expelled for it. In Valoria the direction is reversed and is canon: the **contained**
church administers for the empire, grows, and at independence charges the new crown for consecration
(§1.1).

### 2.6 Elective and fragmented empire

`[TREE: governance_modes.md HRE §1–§6]` The Holy Roman Empire: an elective crown that one house may win
repeatedly without ever owning it; a **two-stage legitimation** (election, then a separate coronation
another power may withhold); **immediacy** (holding directly of the emperor) as a status that can be
traded away by others (**mediatization**); the **ministeriales**, unfree administrators used because they
had no standing of their own, who rose into the nobility by service; a peace decreed and never funded
(the Common Penny). The Mongol and Ottoman successions `[MEMORY; fratricide and kafes TREE: T9]`: the
empire as family property, divided among heirs or fought for among them.

### 2.7 Distance

`[MEMORY]` A letter from the metropole to a distant governor and its answer took most of a year in the
sea empires; the Mongol relay (*yam*) and the Roman public post cut that for official messengers only.
Consequences that recur everywhere: the **man on the spot** decides and reports afterwards; the centre
legislates for a situation that no longer exists; a royal order is received with the formula "I obey but
do not execute" pending appeal; whoever controls the correspondence controls the centre's picture of the
province. `[TREE: T5]` records the agent's information advantage as the root of the governor problem; the
tree has nothing on transit times, and the design below needs none: it needs only that news and orders
travel by persons and papers and can fail to arrive.

---

## 3. Distance: what the engine lacks, and the two edits that supply it

### 3.1 News is instantaneous and universal today

`engine/season/epistemic.py::_ch_chronicle` [CHECKED :649–:686]: "It is an EVENT-KIND FILTER, not a
per-person predicate: when it fires it fires for everyone alive", for every kind a `binding_decision` row
emits; measured there as "the ONLY channel minting `told_by`" in the realm (879 claims in one season,
0 with the channel forced off). So the Katepano at `set_alt_1` learns of a Crown decree in the season it
is issued, and the King learns of every conferral in Altonia. The plan already schedules the repair,
**CR-29** (`workplans/valoria_master_workplan_v11_part4.md:118-129`) [CHECKED]: an event-kind `reach`
channel with a kind→reach map, then `chronicle`'s deletion; FA-01's Schoenland clause and IN-36's
"perception channels at the border" wait on it. **This lane does not redo CR-29.** It supplies the rows of
its map that the colonial institutions turn on, and one rule for the border (proposal
`15_INSTITUTIONS_COLONIAL_B_distance.md`):

- **Nothing reaches across a root.** A person whose place lies under a different root rung from the
  Event's place (the realm, `terr_ALT`, `terr_T16`) is admitted by no reach row. News crosses in a person
  who crosses (`move`, a `march`'s arrival, a `dispatch`ed man) and then `tell`s, or in a Record that is
  `give`n. Both are existing verbs and **`tell` is already a draw** (four bands; a loss is a telling that
  did not land).
- **Inside a root, a binding decision reaches the exercised seat's purview, not the realm.** The reach
  value `purview` admits the persons whose place `purview_reaches(seat, place)` is True for the seat the
  act was exercised through. A ducal decree is then known in the duchy and (through the oath clause) to
  nobody above it; the King hears of it if somebody tells him.

The falsifier for the border is CR-29's own exit ("the same event at reach `room` and at reach `realm`
deposits into different ledger counts") plus one line: at `build_realm(0)`, one season, no person at
`set_alt_1` holds a `told_by` claim whose chain is empty about a realm Event.

### 3.2 Acting at a distance is as sure as acting at home today

`requisition`, `transfer`, `exchange`, `seize`, `issue` and `covenant` carry no `contests:` cell and no
banded `emits:` [CHECKED by load of `verb_table.yaml`, §15 E-3]: they execute or are refused, with no
roll. A levy on Oastad ordered from Valorsplatz moves the stores if the seat's purview reaches. Under the
standing rule each of these is a thing "that could go either way for the people in the fiction". The
design therefore makes four of them **graded acts on the one roll form** (the route `research`, `examine`
and `surveil` already take through `rosters.yaml: graded_inquiries`, provider `social_contest.roll`
[CHECKED by load]), and adds one obstacle term to SC-B's closed roster
(`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`, `obstacle_terms`):

> **`remove`** — how far the actor stands from what he acts on. Unit: obstacle units. Value:
> `remove_step` × hops, where *hops* is the number of territory-to-territory steps on the shortest path
> over `data/geography.py::adjacent_territories()` between the territory of the **actor's own place**
> (`world_q.place_of`) and the territory of the act's subject or destination, plus `border_hops` when the
> two lie under different roots (a foreign place is entered at the nearest pass or coast the file names).
> Sign: hostile (inside the bound). Applies to: any graded act exercised through a seat (`Act.via`).
> Owner of the reading: one Query, `queries/world_q.py::remove(w, place_a, place_b) -> int`. Owner of the
> numbers: `data/fixtures.py` `remove_step` (first value **0.25** Ob per hop; sweep {0 control, 0.25,
> 0.5}) and `border_hops` (first value **2**; sweep {1, 2, 3}), each with a NUMBER row in the hole
> register. The first value is chosen so that the realm's longest internal path costs about as much as one
> step of SC-B's `stakes` table; it is a lead, to be set by `13_SC_calibration.md`'s method.

It reads the **actor's** place, not the seat's rung, on purpose: a king on progress shortens his own
remove (itinerant kingship, `[TREE: CP-5]`), and a ruler who wants a far levy taken well must either go
there or seat a man there. **Delegation is the remedy for distance and the origin of the agent problem**;
that sentence is the whole institution, and it now falls out of one term.

The four graded acts (full rows in `…_B_distance.md`; band effects graded and recoverable):

| act | what the draw decides | pool | obstacle terms (SC-B names; `remove` new) | Overwhelming · Success · Partial · Failure |
|---|---|---|---|---|
| `requisition` (a levy) | **what the place yields** | `stewardship` (a new vocation, by FA-P6's interface) + SC's `standing_dice` when through a seat | `difficulty` routine + `remove` + `stakes` (share of the place's store demanded: `levy_ob`, ≤¼ 0, ≤½ 0.5, more 1.0) + `regard` (the place's cohort toward the actor) − `evidence` (a held `faction_sheet` Record naming the place among its holdings, the existing `survey` product; a grant the cohort has heard of) | full amount and the actor learns the store's true size · full amount · half (floor), the rest stays · nothing moves, `requisition.refused`, witnessed |
| `transfer` between two places (a payment, a tribute, a convoy) | **whether it arrives** | `stewardship` of the carrier | `difficulty` plain + `remove` + `stakes` (amount, as above) + 1.0 if a territory on the path holds a faction at war with the sender (`world_q.at_war`) | all arrives (O and S) · half arrives, half stays at the origin · nothing moves, the season's carriage is spent |
| `issue` to an addressee elsewhere (an order) | **whether the order carries its force** | `copying` (the existing clerk's vocation) + `standing_dice` | `difficulty` routine + `remove` + `opposition` (addressee's score ÷ 2) + `regard` (addressee toward issuer) − `oath_step` 0.5 if the addressee holds a live sworn `oblige` to the seat | terms arrive whole **and** every witness of the delivery can attest it (a later defiance is provable) · terms arrive whole · terms arrive open to reading: `construe` forms for the addressee ("I obey but do not execute") · the addressee learns a writ exists and not its terms; reissue is the recovery |
| `seize` (a taking under a writ) | **whether the taking holds** | `stewardship` + `standing_dice` | `difficulty` demanding + `remove` + `regard` (the holder's) + `stakes` (the Tenure it closes) − `evidence` (the warrant held) | taken, uncontested · taken, and the dispossessed holds a claim to petition on · the thing is sealed, not taken (a `detain`-like hold the next act or a hearing resolves) · refused, witnessed |

A transfer inside one settlement, an order to a man in the room and a levy by a mayor on his own town
have `remove` 0 and keep their present odds at the control arm (`remove_step` 0 and each new `stakes`
entry 0 reproduce today's execution for the three unrolled rows only if a control band is forced; that
control is stated honestly in the proposal: **these are declared hash movers, not EQUAL arms**).

**For the FA lane (not this lane's file):** `06_FA_decree_binds.md` edit 2 deposits a writ's terms to
every addressee the news reaches. Under the standing rule that is the "binds with no resolution roll" case
the brief lists. The `issue` row above is this lane's offered form for the repair; the owner is FA.

### 3.3 What is deliberately not built

No transit clock, no message queue, no per-road speed: a journey costs the traveller scene budget per leg
already (`loop/effects_migration.py::_relocate`, `Person.travel_leg`; "`Query.budget`'s distance penalty"
[CHECKED :98–:126]), and a held, undelivered claim is simply a claim one person has and another has not.
The "information delay" of the sea empires becomes: *the centre knows what somebody came and told it, as
well as he told it.*

---

## 4. The play-facing model

### 4.1 Primitives: what exists, what is reused, what is new

| primitive (brief's list) | in the engine today | used here for | new? |
|---|---|---|---|
| **seat** | `Office` (rung, remit acts, conferral, revocation, binds, upkeep); `establish`, `confer`, `revoke`, `release`, `succeed` | governor, farmer, factor, warden of a march, resident, inspector, the far superior | no; content rows |
| **body** | `rosters.yaml: office_bodies` (19) | a company (a body whose seats sit at trade places), the imperial court | no; content rows |
| **procedure** | `arrangements.yaml` (9 rows, 13 keys) | the audit, the calling-in of a charter | no; **two rows** |
| **instrument / document** | `Record` kind `dispensation {terms, to, at}`, minted by `issue` (down purview) and `covenant` (across); `Record.stages` is its term | every grant and treaty | the Record no; **the closed set of forms is new** (`instruments.yaml`) |
| **claim** | `Claim`, `petition`, the deed kinds, `deeds_judged` | complaint, deed-claim, the accomplishment ledger | no |
| **obligation** | Tenure `oblige` person → seat, with `term`, renewed by `transfer` at `upkeep_of(seat)`; purview's oath clause | homage, service tenure, a company's servants, the client's bond | no |
| **patron–client edge** | the same `oblige` (sworn) and `commit`; `establishment_of` | client elites; the change of patron is `release` + `oblige` | no |
| **treasury / credit line** | `Rung.stores` at the seat's rung; `transfer`, `requisition`, `exchange` | the farm's advance and rent, tribute, subscription and dividend | no (credit proper is the banking lane's) |
| **jurisdiction** | `purview_reaches` (containment + oath) | immunity, the march, the factory's precinct | no |
| **sanction** | `ban`, `detain`, `revoke`, `seize`; the embargo is persons' withheld `exchange` | forfeiture, recall, interdiction of trade | no |

**Reused: ten of ten. New: one registry and one obstacle term (§3.2).**

### 4.2 The one new thing: `engine/season/instruments.yaml`, a closed set in data

`covenant`'s own row says "ITS READERS ARE DEFERRED … neither tribute nor allied sides read a covenant"
(`verb_table.yaml`, `covenant.writes_note`) [CHECKED]. A treaty today is a Record whose `terms` names an
uttered Proposition that nothing can read. The repair follows the tree's own method for proceedings
(`arrangements.yaml`: "a proceeding is just defined parameters"): **an instrument is just defined
parameters.** One file, one loader (`data/instruments.py`, unknown keys rejected), one row per form:

```yaml
- id:           <form name>
  made_by:      issue | covenant          # which verb mints it: down purview, or across
  grantor_act:  <a remit_acts member>     # what the granting seat must hold
  term:         <seasons> | null          # null: for the grantee's life in the seat
  renewal:      grantor | both | none     # who must act for it to run on
  confers:      <a seat template> | null  # the seat the grant establishes and confers, if any
  due:          [ {by: grantor|grantee, kind: <deed kind>, every: <seasons>|once, of: <operand map>} ]
  forbears:     [ {by: grantor|grantee, kind: <deed kind>, over: grant_ground|grantee} ]
  lapse:        reverts | stands          # at maturity unrenewed
  hardens:      true | false              # does age add evidence weight (prescription)
```

Every value is checked at load against an existing owner: `kind` must be a `data/verbs.py::DEED_KINDS`
member (so a clause can only name something a verb emits), `grantor_act` a `remit_acts` member, the seat
template's bases members of `conferral_bases` and `revocation_bases`. The dispensation's content gains one
key, `form`, naming a row; its `terms` stays an uttered Proposition (so the K-54 reading, "a treaty is an
uttered Proposition both holders commit to", is unchanged).

**What reads it** (three Queries, no stored state, no MATTER pass):

1. `world_q.dues(w, pid)` — a standing occasion in `vacancies`' and `writs_addressed`' shape. For each
   live instrument to which `pid` is party (he holds it, or his own ledger holds its content claim), each
   `due` clause that binds his side and has no matching deed of his in its current period stamps that
   clause's referent on the question he answers. He then pays, performs, or does not: **his choice,
   through the one chooser**, and the performing act is itself a draw wherever §3.2 makes it one (tribute
   is a `transfer` between places).
2. `person_q.kept(p, record) -> int` — person-side, computed when read, `suspicion_of`'s shape
   (`06_FA_decree_binds.md` edit 4): over `p`'s **own ledger**, plus one for each period in which he holds
   a claim of the due deed by the bound party, minus one for each matured period in which he holds none,
   minus one for each claim of a forborne deed done. It is what `p` *believes* about the instrument's
   keeping; two parties' readings differ whenever news did not arrive, which is the point.
3. `world_q.breaches(w, pid)` — the mirror occasion: where `kept(p, record)` is below zero, the bound
   party and the grant's seat are stamped on `p`'s question, classed `Person` and `Office`. What he does
   with it is an existing verb: `petition`, `open_case` (the calling-in, §6), `revoke`, `release` of his
   own oath (which a known breach makes cost him no regard, read through CHAR's regard reader), `seize`,
   `march`.

**An immunity is not a wall.** A `forbears` clause forbids nothing in the gate. A grantor who levies
inside a granted immunity can: the levy is rolled as any levy (§3.2), the grantee's people witness it, and
the breach is a claim in their ledgers. This follows SE's ruling on relief ("withholding is the act",
`07_SE_treasury_granary_B.md` R-SE-29) and the tree's rule that defiance costs what the other party then
chooses to do.

### 4.3 The forms this family needs (ten rows; full text in `…_A_instruments.md`)

| form | made by | what it is | confers | due | forbears | historical shape |
|---|---|---|---|---|---|---|
| `homage` | covenant | the bond of a conquest-founded house to the crown | — | grantee: a relief (`transfer.made` to the grantor's rung) once at each succession of either seat. grantor: re-issues the instrument at each succession (`renewal: both`). The muster and the summons are not clauses: the live `oblige` already licenses them (`may_muster`'s oath clause, CP-T09-07 (b); `dispatch` to sworn men, CP-T09-08) | grantor: `tenure.closed` by `revoke`, `rung.seized`, `requisition.taken` over the grantee's ground | fief; the settlement of 200 AG (canon :88) |
| `land_grant` | issue | unheld or taken ground given for settlement | a `Lord`-post seat at the ground, `conferral: appointed`, heritable by a `successions` title | grantee: a `rung.founded` within the term, or the grant reverts | grantor: `requisition` over the ground for the first term | military colony, headright `[TREE T8; MEMORY]` |
| `march` | issue | a frontier held on wide powers | a warden's seat with `dispatch` and `determine` at a pass or gate territory | grantee: a `garrison` kept in repair (`site.restored`) | grantor: `open_case` over the warden's men | marcher lordship `[TREE T8]` |
| `farm` | covenant | the revenue of a ground sold for a term | a farmer's seat with `issue` (hence `requisition`) at the ground, term 4 | grantee: an advance once, a rent each season, both `transfer.made` to the grantor's rung | grantor: `requisition` over the ground while it runs | publicani, iltizam `[TREE T2]` |
| `charter` | issue | a town's or a body's self-rule | the body's head seat, `conferral: elected` | grantee: a fee at each succession of the grantor's seat | grantor: `revoke`, `confer` on the chartered seats | borough charter, Magdeburg law `[TREE T4]` |
| `staple` | issue | a body's sole right to trade a matter kind at a place | a factor's seat with `issue` at the settlement | grantee: a rent each year | grantor: a second `staple` of that kind there (`dispensation.issued` with the same `of:`) | company monopoly, the staple port `[MEMORY]` |
| `immunity` | issue | a jurisdiction left alone | — | grantee: none (quiescence is a `forbears`: no `march`, no `seize` against the grantor) | grantor: `requisition`, `seize`, `open_case` over the ground | the containment grant (canon :58) |
| `tribute` | covenant | payment for peace or protection | — | grantee: `transfer.made` each year. grantor (the `protected` variant): a `march.declared` against whoever marches on the grantee | grantor: `march` on the grantee | Ragusa, the Danegeld `[TREE T10, FA-8]` |
| `wardship` | covenant | a person of one house kept at another's court | — | grantee: the named person's `residence.changed` to the grantor's settlement, once | grantee: the person's return while it runs | hostage-kin `[TREE Shogunate §1.9]`; the tutoring demand (canon :141) |
| `capitulation` | covenant | terms on which a place is given up | — | grantee: `place.surrendered`, once | grantor: `rung.razed`, `requisition` over the place for the first term | honours of war, the entry `[TREE T6]` |

A **company** is not a form and not a faction kind. It is a body (`office_bodies` row) holding a `staple`
or a `charter`; its servants are persons with an `oblige` to its seats, paid by the seat's `transfer`
(the existing upkeep renewal, `loop/effects_economy.py::_renewals`); its subscribers are persons who
`transfer` into its seat's rung and hold a `tribute`-shaped instrument against it (a dividend is a `due`
on the company). That is joint stock in the engine's units with no new carrier. Banking and credit proper
belong to the merchant-republic lane (§10).

### 4.4 Cut tests (what dies without each candidate primitive)

- **`instruments.yaml`**: without it, every treaty, tribute, charter, farm and capitulation is an
  unreadable Proposition; `covenant` has no reader (its own row). *Kept.* E, last: one file and three
  Queries against ten institutions and the Altonian treaties, the containment grant and the ducal
  settlement becoming things persons can keep or break.
- **A `Charter` Record kind**: dies nothing; `rosters.yaml: record_kinds` already notes a covenant "is a
  dispensation distinguished by what its `terms` names". *Cut.*
- **A `colony` rung kind**: a planted settlement is a `settlement` rung founded by `found` on granted
  ground; its being a colony is the instrument its lord holds. *Cut.* (`found` exists; whether a new
  settlement may be added to the 37 is SE's and Jordan's, `[TREE: SE-9(a)]`; the `land_grant` form
  works on converting an existing village as well.)
- **A `company` faction kind**: a faction is "a derived view with no verbs" (`queries/faction_q.py`). A
  body with seats is enough. *Cut.*
- **An `audit` verb**: it is `open_case` under an arrangement row (§6.2). *Cut.*
- **A stored `suspicion`, `legitimacy`, `prescription` or `governor_emergence` value**: Layer 1 refuses a
  social quantity that moves at MATTER (`state/world.py:64-107`, cited from `audits/12_ARCS_adjudication.md`
  rank 1, not opened here). Each is a fold over a ledger or a Tenure's age. *Cut.*
- **`remove`** (the obstacle term): without it distance costs nothing and every colonial story collapses
  into the capital. *Kept.*

---

## 5. Legitimacy: rank as a ranked ledger of accomplishment

### 5.1 What the tree already has

- **Canon:** deed-monarchy; "authority is entirely earned through wartime deeds"; "cadet branches as
  deed-families"; "the deed-presumption is rebuttable"; the heir "inherits the presumption his father
  created" and must prove it (`canon/03_canonical_timeline.md:80–:92, :117`) [CHECKED].
- **Code:** a deed is an Event of a `data/verbs.py::DEED_KINDS` kind; `queries/person_q.py::deeds_judged(p,
  referent)` is each person's own valuation of a referent's deeds from his own ledger (`:97`);
  `rosters.yaml: standing_routes` partitions deed kinds into `dominance` (`person.died`, `body.changed`,
  `field.won`, `rung.seized`, `record.seized`, `requisition.taken`) and `prestige` (every other);
  `standing.band_crossed` is logged when a person's standing gap changes band and is "read only as a
  QUESTION about its tellers" (`rosters.yaml: logged_kinds`); `conferral_bases` includes `annex` (a seat
  taken with its ground; "which act fills an … `annex` seat is not ruled"); `successions: {off_king:
  off_heir}`; `continuation_ties: [heir_title, sworn]` [all CHECKED by load].
- **Design vocabulary (archived, intent only):** a **Recognized Deed** is "an action the Church,
  Parliament, or a senior military commander publicly endorses" (`faction_politics_v30.md:170`); in
  Varfell "any Deed-Claim succession … needs the Skald-Chief's endorsement" (`:315`, carried into
  `offices.yaml:523`).

### 5.2 Jordan's statement against the tree

*"Royalty by noble conquest, i.e. the first king had the greatest accomplishment in the secession war,
followed by the first Duke of Hafenmark and the first Duke of Varfell."*

| # | the tree says | against the statement | disposition |
|---|---|---|---|
| 1 | Canon :80, :90: the first Almqvist's leadership "proves decisive"; Baralta's ducal status "earned through wartime deeds" | agrees for the king and Hafenmark | none needed |
| 2 | Canon :76, :96: the coalition was "primarily northern"; the south was "peripheral and culturally stigmatised"; the caste is "the structural consequence of the south's exclusion from the war coalition's leadership" | **in tension**: a first Duke of Varfell with the third-greatest accomplishment was in the coalition and was rewarded with a duchy | **Jordan's word governs the world.** Third of three is the junior place and is consistent with exclusion from *leadership*; it is not consistent with "peripheral". The canon sentence is ratified text, so its rewording is §11 item 1 |
| 3 | `offices.yaml:226-237`: `off_duke_varfell.conferral: elected`, source "first among the Jarls, not a monarch" | **apparent** conflict only | reconciled by reading (ladder step 4, the tree's own distinction): *how the seat was founded* (conquest) is not *how each holder is seated* (the Jarls elect). The Holy Roman crown is the research's precedent: elective, and won by one house for centuries `[TREE: HRE §1]`. No edit to the seat |
| 4 | `offices.yaml:213-224`: `off_duchess_hafenmark.conferral: null` | the code says nothing about how Hafenmark passes | proposed: `inheritance`, by `off_king`'s precedent (ladder step 4), with a `successions` title that **nobody holds at build** (canon: Baralta is "unmarried, childless, heirless"). `…_D_accomplishment.md`, an `[ASSUMPTION; Jordan to correct]` content edit in FA's file |
| 5 | **No fact in code ranks the three founders.** No founder exists as a person, no Secession deed exists as an Event or a claim | the order of accomplishment is carried by nothing | proposed: three prehistory deeds seeded through the gate (below) |

### 5.3 The design

**(a) The ledger is each person's own.** There is no world-level rank. `person_q.accomplishment(p, q)` is
`p`'s `deeds_judged` of `q` over the `prestige` and `dominance` kinds he holds claims of, **plus the
presumption `q` inherits**: for each seat `q` holds, `p`'s judgement of the deeds of the person whose
`hold` on that seat closed before `q`'s opened (read from `p`'s own `tenure.opened`/`tenure.closed`
claims), times `presumption_gain`, recursively, so a founder's deed is worth `presumption_gain`ⁿ to the
nth holder after him. Unit: the unit of `deeds_judged`. Owner: `data/fixtures.py: presumption_gain`,
first value **0.5**, sweep {0 control, 0.5, 0.75}. **Standing passes down the seat, not the blood**:
that is deed-logic as canon states it ("loyal to Crown as institution, not bloodline", :145), it is
Kantorowicz's corporate crown `[TREE: SE-6]`, and the third-generation decay is Ibn Khaldun's
`[TREE: CP-2]`. Blood enters only where a seat's `conferral` is `inheritance` and an heir title exists.

**(b) The Secession War is three seeded deeds.** At world-gen, before tick 0 and through the gate (the
route `audits/12_ARCS_adjudication.md` §6 row 16 decides for prehistory, "acts and witnessed Events …
not constructed Claims"), three `field.won` Events are written whose doers are the three founders, as
dead persons with a closed `hold` on `off_king`, `off_duchess_hafenmark` and `off_duke_varfell`, the
King's with three such deeds, Hafenmark's two, Varfell's one `[ASSUMPTION; the counts carry the order and
nothing else; Jordan to correct]`. The cast learns them `told_by` at build. From there (a) gives Almud
half his father's standing in every ledger and gives Baralta and Vaynard half their founders', in
Jordan's order, **until somebody does something.**

**(c) Certification is an instrument, and it shifts odds.** A recognised deed is a `dispensation` of form
`recognition` (an eleventh row, shared with the crown and Church lanes, §10) issued by a seat with
`determine` in its remit: the Confessor (consecration), a Crown seat, the Grand Master, the Skald-Chief.
In any later contest where the deed is cited, the recognition is `evidence` (SC-B's term; weight by the
hearer's regard for the certifying seat's faction, through `heritage_regard`'s existing fold). It decides
nothing: a rival body may issue a `recognition` of a rival deed, or open a case on this one, and **which
reading the room takes is the hearing's draw.**

**(d) A new accomplishment raises a house or unseats one through three existing routes**, each a draw:
1. *By reception.* When `accomplishment(p, claimant) − accomplishment(p, incumbent)` crosses a band for
   `p` (the existing `standing.band_crossed` log, re-keyed to this gap), the seat and the claimant ride
   `p`'s question. `p` may `oblige` to the claimant's seat, `release` his oath to the incumbent's, or
   `petition`. Enough released oaths and the incumbent's purview no longer reaches (§1.4).
2. *By hearing.* A deed-claim is a `petition` to the body that fills the seat; the plan's `succession`
   arrangement row (`disposes: hold`, CR-35; `arrangements.yaml` header) hears it; `determine` rolls.
3. *By conquest.* An `annex` seat is filled by the holder of the seat through which its ground was taken
   (a won `march`, a `seize` that held, a `place.surrendered` under a `capitulation`). This is the one
   ruling this lane asks of FA (`state/gate.py::FILLED_BY["annex"]`): ladder step 4, on Jordan's own
   statement that the three founding seats were won this way.

**(e) What a conquest-founded house owes and is owed** is the `homage` row (§4.3): it owes the muster and the
summons (by the oath itself) and a relief at each succession; it is owed confirmation at each succession
and the grantor's forbearance on its ground (canon :88, "ducal authority cannot be unilaterally
overridden"). The three built oaths (§1.4) gain that form as content. A king who levies inside a duchy
has breached, visibly; a duke who withholds the relief from a new king has breached, visibly; each breach
is the other's licence, and what either then does about it is a choice followed by a draw.

---

## 6. Verbs, procedures and contests

### 6.1 Verbs (all existing; mapped to `verb_table.yaml`)

| verb | today (E-3; verb-lane readings where cited) | what this family adds | owner of the row text |
|---|---|---|---|
| `covenant` | executes rarely; "0 of 41 executed" (`workplans/…v11_part2.md:67`); no reader | a `form` operand from `instruments.yaml` (by `rosters.yaml: choice_sourced`' route); `dues`/`kept`/`breaches` read it | this lane, proposal A; SOCIAL verb lane for the row |
| `issue` | executes, binds nobody (`audits/14_VERBS_BINDING.md` §0) | optional `form`; graded at `remove` (§3.2) | BINDING verb lane; FA-P1 |
| `requisition` | unrolled | graded: the levy's yield | MATERIAL verb lane; this lane states the roll |
| `transfer` | unrolled; renews `oblige` terms through a seat | graded between places: carriage | MATERIAL verb lane |
| `seize` | unrolled; "only refused or never attempted" (ARCS rank 9) | graded: whether the taking holds | MATERIAL verb lane |
| `oblige` / `release` | forms only on a seat the person was told of | the client's change of patron; a known breach as the releaser's ground | unchanged rows |
| `establish` / `confer` | `establish` mostly refused; `confer` never chosen (BINDING §0) | the `confers:` seat of a grant; term from FA-P3's `term:` key | FA-P3, BINDING lane |
| `open_case` / `determine` | `determine` refused on `docket` | two arrangement rows (§6.2) | SC lane's `05_SC_playable_hearing_B.md` for reach |
| `found` | executes on a held `works` | the `land_grant`'s due deed | unchanged |
| `dispatch` | executes, writes nothing | the inspector, the envoy, the courier: CP-T09-08 as adopted by `14_VERBS_BINDING.md` §4 | BINDING lane |
| `march`, `surrender`, `raze` | fields are draws (mass battle) | conquest, revolt; `capitulation` terms | PHYSICAL lane, MB |

No verb is added. `audit`, `charter`, `colonise`, `farm`, `pay_tribute`, `embargo` were each tested and
each is an existing verb with an instrument form or an arrangement row.

### 6.2 Two procedures (rows of `arrangements.yaml`; full text in `…_C_audit_and_charter.md`)

**`audit`** (the residencia; the visita is the same row opened mid-term by a `dispatch`ed inspector).
Opened by `open_case` through the seat that conferred the audited seat, or its successor, when the
audited `hold` closes for any reason, or at will if the opener is present at the audited seat's rung
(`remove` 0: an inspection must be on the spot). `disposal: bench`; `floor: open` (the governed may
speak); `proofs: [testimony, record]`: testimony is what residents of the governed ground hold of the
officer's deeds (their own claims of `requisition.taken`, `record.seized`, unanswered `petition.filed`),
records are his accounts (an assessment Record, a quittance from an earlier audit, forgeries included,
through FI's evidence interface). `standard: demanding`. `disposes:` band-keyed (SC-P4's map,
`05_SC_arrangement_rows_that_bind.md`): against the officer at Overwhelming `ban` (from seats in the
opener's purview, FA-P3's scoping); at Success `oblige` to the opener's seat with a `due` of restitution;
at Partial a `Record` only (an admonition every later bench may read as evidence); at Failure nothing is
opened and the officer receives a quittance Record (`05_SC_acquittal.md`'s shape). **The verdict is the
bench's draw**; a guilty governor with friends on the bench and a forged account is sometimes cleared,
and an honest one before a hostile successor is sometimes ruined.

**`quo_warranto`** (the calling-in of a grant). Opened by the grantor's seat or its successor against the
holder of an instrument. `proofs: [record, testimony, oath]`; the instrument itself is the holder's
evidence and, where its form `hardens`, **its age adds weight**: one unit of proof weight per
`prescription_seasons` held, capped at three (owner `data/fixtures.py`; first value **8**; sweep {4, 8,
16}; unit: seasons per unit of SC's `proof_step` weight). `standard: demanding`; `stakes`: the seat the
grant confers. Band-keyed disposal, for the mover: at Overwhelming and Success the conferred
`hold` closes (a closing disposal, the one code change this lane asks of SC; proposal C states the
fallback); Partial the grant stands for a fee (a `due` on the holder, the confirmation fine
`[TREE: SE-4]`); Failure the grant stands and the judgment is a Record that is evidence in every later
calling-in. Every other holder of the same form hears of it at the reach of the bench's
`disposal_reach`, and judges the mover by it (`deeds_judged`): London, 1683 `[TREE: T4]`, as persons'
reactions and not as a realm-wide modifier.

### 6.3 The contests, each with its roll

| contest | who rolls | venue | modifiers that matter most (SC's dimension table, `audits/13_SC_contest_interrogation.md` §2) |
|---|---|---|---|
| the levy | the collector | the place | `remove`; the cohort's `regard`; the share demanded; a held assessment |
| the convoy | the carrier | the path | `remove`; war on the path; the amount |
| the order at a distance | the issuer | the addressee's place | `remove`; a live oath; the addressee's `regard` and score |
| the audit | the bench (`determine`); the officer and the governed (`speak`) | the governed ground | testimony held by residents; accounts; `reception`; the opener's stake |
| the calling-in | the bench; grantor and holder (`speak`) | the grantor's court | the instrument's age; `reception`; rival recognitions |
| the bid for a farm or a patent | each bidder (`petition` then `speak` at the grantor's sitting) | the grantor's court | the advance offered (a `transfer` made), `regard`, standing dice |
| the field | commanders (mass battle) | the ground | MB's; `capitulation` offered before it |

---

## 7. Tuning dimensions

Stated on the SC lane's dimension table (`audits/13_SC_contest_interrogation.md` §2 and §5; its five
tuning tables are the owners, this lane adds rows and one term and no table of its own).

| dimension | how it enters this family's rolls | owner (single) |
|---|---|---|
| **distance** (new) | `remove`, on every graded act through a seat | `world_q.remove`; `data/fixtures.py: remove_step`, `border_hops` |
| **venue** | the audit sits on the governed ground (open floor: the governed speak); the calling-in sits at the grantor's court (the grantor's bench, his `reception`); a levy's venue is the place levied | `arrangements.yaml` rows `audit`, `quo_warranto` and their `standard:` (SC's T2) |
| **personality** | the farmer who presses or remits, the governor who goes native or stays the centre's man, the Katepano who probes or invades are **the chooser's** reading of pursuits (CHAR §0A; `02_CHAR_goal_lean_on_its_own_question.md`); in a roll, temperament is leverage by a matched appeal, never an obstacle term (SC's ruling, kept) | `npcs.yaml`, cohort temperaments; `advantage_sources` |
| **affiliation** | `altonian_civics` (the collaborator's creed), `einhir_restoration`, `solmund_orthodoxy` reach every roll **through `regard`** by `person_q.heritage_regard` (CR-31), and so set a southern cohort's resistance to a northern collector with no new term | `references/descriptor_registry.yaml: affiliation_roster`; SC's T3 |
| **office** | SC's `standing_dice` when the actor holds a seat of the body whose business it is; a grant's `confers:` seat is what gives a farmer or factor those dice | SC's T4; `offices.yaml` |
| **evidence** | a held assessment (`faction.surveyed`'s Record) for a levy; the warrant for a seizure; the instrument and its age for a calling-in; sworn complaints and accounts for an audit; a `recognition` for a deed-claim | SC's T5 (`proof_step`); `prescription_seasons` |
| **stakes** | the share of a store demanded; the Tenure a verdict opens or closes | SC's T4 `stakes_ob`; new table `levy_ob` beside it |
| **publicity** | authored into the row's `standard` (SC's R-5): the audit's open floor is a harder room for the officer | `arrangements.yaml` |
| **season** | none as a global modifier (SC's R-6, kept): a lean season reaches a levy through the cohort's hunger-moved `regard` and through the share a fixed demand now is of a smaller store. **That is Scott's invariance-under-dearth, obtained with no rule for it** | — |

## 8. Emergent narrative with no player

Each row is a story the institution produces by itself, the conditions it arises under, and the reading
that would show it happened **and could fail to**. None is an event; each is persons' acts.

| story | arises when | instrument reading (a fold over the Event log; none is built, each is a `harness/` report of `strife.py`'s kind) | how it can fail to show |
|---|---|---|---|
| **The farmer becomes a power** | a `farm` runs; the farmer's levies succeed; he pays his men from the surplus | the farmer's `establishment_of(seat)` exceeds the grantor's local establishment; at term's end the audit is not opened, or is opened and acquits | no farm is ever granted (formation); every levy fails (`remove` too dear) |
| **The dearth revolt** | a fixed rent meets a short store; the farmer demands a larger share to make it; the cohort's regard falls; the next levy's odds fall; he sends for force | a `requisition.refused` followed within two seasons by `march.declared` or `petition.filed` naming the farmer, in the same territory | the farmer remits (the chooser prefers regard); stores never run short |
| **The over-mighty warden** | a `march` grant; fields won on the frontier; locals swear to the warden's seat | `oblige` edges to the warden's seat from persons resident in the march exceed those to the grantor's; a calling-in is opened, or never dares to be | no field is fought at the pass |
| **The charter that hardened** | a `charter` or `staple` older than `prescription_seasons`; a new holder of the grantor's seat wants the revenue | a `quo_warranto` case whose holder cites an instrument with age weight ≥ 1; its verdict; other holders' `regard` for the mover after it | no succession at the grantor's seat; the successor confirms for the fee |
| **The client changes patron** | a tributary or sworn house holds `kept < 0` on its lord's side (protection not given, a levy inside its immunity) and a rival offers a `covenant` | a `tenure.closed` (an `oblige` released) followed by `duty.taken` to another faction's seat by the same person | no rival is within reach to offer; news of the breach never arrives |
| **The recalled governor does not come** | an `issue` of recall rolls Partial or Failure at `remove`, or lands and is defied | `compliance.withheld` or `terms.distorted` by a seat-holder on a writ naming his own seat, then the issuer's next act toward him | the order lands whole and he obeys |
| **The contained institution outgrows the grant** | an `immunity` holder's establishment and stores grow behind the grantor's forbearance | the immunity holder's seat count and treasury against the grantor's over seasons; the first `breaches` occasion on either side | the grantor breaches early and wins the field |
| **The metropole's man on the spot** | the Katepano, at `border_hops` from her superior, marches or treats on her own reading; the court hears a season later what an envoy told it | an Altonian `march.declared` or `covenant.offered` with no prior `dispensation.issued` from the court seat naming it; then the court's answer | the court's orders always arrive (remove 0 arm) |
| **The ward who stayed** | a `wardship` runs; the ward's regard for the host's house rises (CHAR's regard) | the ward's `stance_toward` host and home over seasons; at term, a `residence.changed` home, or none | CHAR's regard does not move (F-CHAR-03 today) |

## 9. Playable standalone and integrated

**First scenario: "The Farm of the Southern Tolls".** Ground: `terr_T6` Stillhelm (Crown, calamity-
adjacent, "population uneasy", a gate to Askeheim, heritage gradient high: canon :100). Fixture: the
realm as built plus one seeded `farm` instrument: grantor `off_lord_treasurer`, a farmer's seat
established at `terr_T6` (term 4 seasons), an advance paid, a rent due each season. Three seats to play:

- **the farmer** (the player's default): each season, how large a share to demand of which settlement
  (the levy's stakes), whether to go there himself (`remove` 0) or send (`dispatch`), whether to remit in
  a lean season, whether to pay his men (`transfer`, upkeep) or pocket it, whether to commission an
  assessment (`survey`) first. He sees the roll's terms (SC-P1's term list on the Event) and so why a
  levy fell short.
- **the Lord Treasurer**: whether to grant, to whom (the bid), whether to levy inside the farm (a
  breach), whether to send an inspector, whether to open the audit and before which bench.
- **a Stillhelm hearth head**: pay, hide stores (`conceal`), `petition`, testify, `migrate` (exit),
  swear to the farmer or to the Restoration Movement.

End conditions: the term matures and the audit is determined (four graded endings by band), or the
farmer's `hold` closes earlier by recall, release, death or a field. Stable continuation: the farm is
renewed, re-let to a rival, or the ground reverts. **One code path:** the scenario is the season loop on a
realm with one extra instrument and one extra seat; nothing in it is harness-only. Entry point: a
`harness/exercises.py` case (the existing player-proxy surface, `play_surface.py`), per FA's
`06_FA_playable_scenario.md` and SC's `05_SC_playable_hearing_B.md`, which this scenario composes and
does not replace: the audit *is* SC's playable hearing with this lane's row.

**Execution artifact (the gate for the whole plan).** `python -m engine.season.harness.institution
INST-COLONIAL-01 6 S` (the report proposal E specifies) for S in 0..4, `PYTHONHASHSEED=0`, six seasons (`MAX_SEASONS`), NPC chooser in all three seats, prints per
seed: levies attempted and their bands; rent `transfer`s attempted and their bands; `kept` as each of the
two parties reads it at each season's end; petitions filed; whether the audit was opened and its band.
**Pass:** across the five seeds at least two different audit bands occur and at least one levy lands in
each of three bands (the outcome is not a function of the fixture). **Control:** the same seeds with the
instrument absent: no farmer's seat, no levy through it, hash equal to the base realm. **Planted
failure:** force every roll's band to Success; the five seeds then agree on every count, and the pass
condition reddens. Five seeds are five trajectories, not a rate; no balance claim is made from them.

**Second scenario: "The Katepano's Latitude"** (the M-ABROAD arcs; after proposal B). `build_realm(S,
foreign=True)` plus the court seat (§12 batch 2): play the Katepano (probe, press, treat, demand the
ward, obey or construe the court), or the King's envoy.

What is missing today for either: the instrument registry and its three Queries; the four graded rows;
`remove`; the two arrangement rows; CR-29's reach; FA-P1 and FA-P3; SC's hearing reach (H-254); a
`stewardship` vocation with at least two persons holding different scores. Each is a named batch in §12.

## 10. Interfaces to other institutions

Named primitives and verbs only. **Exports** are what this family builds and the others may use;
**imports** are what it needs from them. The synthesis lane should read the first row of each block
first: it is where the lanes are likeliest to have built the same thing twice.

**Shared with every family (the reconciliation point):**
- `instruments.yaml` (registry; row schema §4.2). This family authors ten rows. A papal bull, a privilege
  of a doge, an imperial chrysobull, a bank's bill and a guild's charter are, by this lane's reading,
  further rows of the same file. If another lane has proposed a second registry for grants or treaties,
  **one of the two should die**; this lane's claim is only that the keys `due`, `forbears`, `confers`,
  `term`, `renewal`, `lapse`, `hardens` are sufficient for its ten.
- `world_q.dues`, `person_q.kept`, `world_q.breaches` (the three readers of any instrument).
- `remove` (obstacle term) and `world_q.remove` (Query).
- `recognition` (an instrument form: a seat certifies a deed). Authored here only as far as §5.3 (c)
  needs; its home is the crown and Church lanes.

| with | exports (this family → them) | imports (them → this family) |
|---|---|---|
| **the crown** (deed-monarchy, court, succession) | `homage` (form) and its `due`/`forbears`; `FILLED_BY["annex"]` by conquest; `person_q.accomplishment` and `presumption_gain`; the three seeded Secession deeds; `quo_warranto` (arrangement row); `audit` (arrangement row) for any appointed seat | the `succession` arrangement row (`disposes: hold`, CR-35); `successions` titles for ducal seats; the crown's `recognition`; `confer` with FA-P3's `term:`; `revoke` under FA-P1's recall occasion |
| **the Church** | `immunity` (form): the containment grant as a held instrument with a grantor's `forbears`; the border rule (missionaries are persons who cross and `tell`); `land_grant` usable for a mission's ground | consecration as a `recognition`; `excommunication_deliberation`'s `ban` as the sanction that releases sworn men from an oath (the Church lane decides whether a `ban` on a lord is a ground for his vassals' `release`; this family reads only that the oath is no longer live); the parish seat (advowson) if that lane builds it `[TREE: SE-8]` |
| **the Byzantine-style bureaucracy** (Altonia; any salaried administration) | `remove`; the graded `issue` (an order's force at a distance); `audit` (the residencia) and the inspector by `dispatch`; the far superior's seat (`off_altonian_court`, M-ABROAD) with `appointed` / `rung_above_same_faction` on the Katepano and the Kommerkiarios, so that recall exists | the ranks, seals and clerks' sequence that decide **how many hands an order passes through** (this family treats an `issue` as one roll; if that lane makes it several, `remove` enters each); the `stewardship` and `copying` vocations' definitions and any office that adds dice; rotation rules as `term:` values |
| **the merchant republics and banking houses** | `staple` and `charter` (forms); the factor's seat at a trade place; the graded `transfer` (carriage) as the risk a bill of exchange exists to avoid; `tribute` (form) as the shape of a dividend | credit (a loan against future `due`s; the advance on a `farm` is their business as soon as it is borrowed); the embargo (a body's members forbearing `exchange` with a named party, `[TREE: FA-9]`); Schoenland's seats and persons (IN-36's residue "Schoenland as persons") and its election or lot procedures; `exchange`'s price |
| **guilds and orders** (as the brief's synthesis list names them) | `charter`; `quo_warranto` | the body's internal election |
| **the peoples under them** (cohorts, hearths) | the cohort as the levy's counterparty (`regard`); `petition`, testimony at an `audit`, `migrate` as exit | CHAR's regard movement; SE's stores, hunger bands and census |

## 11. Survivors for Jordan

Three, after the five-step ladder. Everything else in this file was answered by a ruling, the plan,
precedent or the architecture and is recorded where it was decided.

1. **The canon sentence on the south's part in the Secession War** (`canon/03_canonical_timeline.md:76,
   :96`; ratified text; §5.2 row 2). Jordan's statement makes the first Duke of Varfell the third-ranked
   victor. *Option A:* reword canon so the south fought, ranked third, and was **relegated in the
   settlement despite the deed**: Varfell's grievance is then a claim on the same ledger as Baralta's (a
   deed under-rewarded), and Vaynard is a pretender within the order. *Option B:* keep the canon wording
   and read the first Duke of Varfell's accomplishment as recognised later and grudgingly: Varfell stands
   half outside the ledger, and Vaynard is a revolutionary against it. The two are different games for
   every southern character. (This lane's seeding, §5.3 (b), fits A and needs one count changed for B.)
2. **May an office be sold?** The `farm` sells a revenue for a term, with an audit at the end; that is
   inside every ruling. **Venality** is a seat conferred for a payment, heritable, with the audit waived
   (the *paulette*; `[TREE: SE-7]` left it `needs_jordan`: "does Valoria sell offices?"). *Option A:* a
   form `purchase` exists (`confers:` a seat with a `successions` title, `forbears:` the grantor's
   `open_case` over it): the crown can raise money fast and loses the seat for good, and a class of
   office-owning families appears who are nobles by purchase, **directly against nobility by deed**.
   *Option B:* no such form: every seat stays answerable, and money buys only farms and staples. A makes
   "deed against purse" a standing conflict of the setting; B keeps the deed-order unmixed.
3. **Forced labour keyed on caste.** The historical family includes labour drafts on a subject people
   (§2.2). In Valoria the subject people exists and is canon (the southern Einhir). *Option A:* a form
   `corvee` (a levy of hands: a cohort's seasons of `site.worked` owed to a grantee's site) may be issued
   over southern ground: the caste becomes an extraction institution with persons, seats and an audit,
   and its abolition is a playable fight over an instrument. *Option B:* the caste stays what canon calls
   it, "informal", with no instrument: it acts only through `regard` (`heritage_regard`), and nobody in
   the world can grant or abolish it by an act. This is a tone decision about canon and is not this
   lane's to take.

Decided here and **not** escalated, with the ladder step: the foreign superior as one seated person
(step 4, Altonia's two seats and ARCS §6 row 12); a non-victory ending `reabsorption` (`holds: {post:
King}`, `under: Altonia`) by `theocracy`'s precedent (step 4; the endings roster's own second row;
proposal B carries it as content `[ASSUMPTION; Jordan to correct]`); `off_duchess_hafenmark` to
`inheritance` (step 4); no stored suspicion or legitimacy (step 1, Layer 1); no new verb (step 5).

## 12. Implementation plan

Ordered, gated, against the present code. Cost classes: **edit** (data or a few lines at one owner),
**small build** (one Query or loader with its tests), **design-first** (needs a decision or another
lane's shape before it can be written). Every batch ends with the one test file covering it; the suite
runs once at the close (CLAUDE.md §0.4). Dependencies on other lanes are named, not rebuilt.

| batch | what lands | files (owner) | class | needs first | gate (execution artifact) and falsifier |
|---|---|---|---|---|---|
| **C-1 instruments** (proposal A) | `instruments.yaml` + `data/instruments.py`; `form` content key on `dispensation`; `choice_sourced` rows for `covenant` and `issue`; `world_q.dues`, `person_q.kept`, `world_q.breaches`; ten rows | `engine/season/instruments.yaml` (new), `data/instruments.py` (new), `data/files.py`, `rosters.yaml: record_kinds, choice_sourced`, `queries/world_q.py`, `queries/person_q.py` | small build | `covenant` and `issue` forming on what the actor knows (`14_VERBS_SOCIAL2_A`, BINDING lane) | with the file empty, `build_realm(0)` hash EQUAL; with one hand-placed `tribute`, the payer's question carries the payee's rung in the due season and not after a matching `transfer.made`; planted: drop the period test and the occasion never returns in the next period |
| **C-2 distance** (proposal B) | `world_q.remove`; `remove` in `obstacle_terms`; fixtures `remove_step`, `border_hops`, `levy_ob`; `requisition`, `transfer`, `issue`, `seize` graded; reach rows for CR-29's map; the court seat and `ALT-0`; `reabsorption` ending | `queries/world_q.py`, `rosters.yaml`, `data/fixtures.py`, `verb_table.yaml` (four rows), `offices.yaml: foreign_seats`, `rosters.yaml: foreign_cast, endings`, `references/npc_registry.yaml` (one person) | small build ×2; the four rows are **declared hash movers** | SC-B (the obstacle form and `obstacle_terms`); CR-29; a `stewardship` vocation (FA-P6's interface; CHAR/CORE own the definition) | the same levy by the same actor at 0 and at 4 hops, 400 seeded draws each, shows band shares that differ in the direction of the term and overlap (neither arm is all one band); `remove_step: 0` reproduces the 0-hop shares; a realm Event deposits no claim at `set_alt_1` in its own tick |
| **C-3 audit and calling-in** (proposal C) | arrangement rows `audit`, `quo_warranto`; `prescription_seasons`; governor and farmer `term:` content | `arrangements.yaml`, `data/fixtures.py`, `offices.yaml` | edit | SC-P4 (band-keyed `disposes:`), SC's hearing reach (H-254, `05_SC_playable_hearing_B.md`), FA-P3 (`term:`), `05_SC_acquittal.md` | on a hand-built hearing, 400 seeded `determine` draws with and without three sworn complaints held by the bench show different band shares, both with spread; an instrument aged 0 and aged 16 seasons likewise |
| **C-4 the ledger of accomplishment** (proposal D) | `person_q.accomplishment`; `presumption_gain`; three seeded founders and deeds; `homage` on the three built oaths; `off_duchess_hafenmark` to `inheritance`; `FILLED_BY["annex"]` | `queries/person_q.py`, `data/fixtures.py`, `harness/populated.py` (seeding, through the gate), `offices.yaml`, `rosters.yaml: successions`, `state/gate.py` | small build; seeding is a declared mover | C-1; ARCS' prehistory route (`12_ARCS_case_on_the_realm.md`); CR-35 for the hearing route; §11 item 1 for the counts | at `build_realm(0)`, for a majority of the cast `accomplishment(p, king) > accomplishment(p, duchess) > accomplishment(p, duke_varfell)`, and with `presumption_gain: 0` all three read their own deeds only; planted: reverse two seeded counts and the order reverses |
| **C-5 the scenario** (proposal E) | the `farm` fixture on `terr_T6`; the report; the second scenario's fixture | `engine/season/cases/exercises/` (one case), `harness/` (one report, `strife.py`'s kind) | small build | C-1 to C-3; FA's and SC's playable scenarios; CHAR's regard movement for the dearth story | §9's execution artifact, its control and its planted failure |

**What each batch unblocks among the nine requirements** (`dossiers/00_NINE.md`, read by name only):
C-1 consequence and propagation through governance (a treaty that is kept or broken is read by a later
decision); C-2 non-omniscient characters and probabilistic chains at the strategic scale; C-3 strategic
and management actions with a hearing as their consequence; C-4 memory and attitude toward houses; C-5
the standing playable-standalone requirement for this institution.

## 13. Provided arcs and characters

Read at the rows of `audits/12_ARCS_adjudication.md` (the case files themselves were not opened by this
lane; `[ARCS]`). That audit ranks **M-ABROAD** ("powers beyond the map, through persons … none written;
§6 row 12") as owned by nobody; this lane takes it.

| case | need (short, `[ARCS]`) | represented today? | change | proposal | depends on |
|---|---|---|---|---|---|
| NPC-089 Zoe Palaiologina | a frontier governor chooses a posture; a superior may recall (N1, N2, N6) | seat and goals authored; no superior; her court hears everything at once | the court seat; the border rule; graded `issue` at `border_hops` | B | CR-29 |
| ARC-25 The Schoenland Pivot | a neutral third party evaluates on externally visible facts and aligns | Schoenland has a cohort and no person | Schoenland's seats are the merchant-republic lane's; this lane supplies the border rule (it sees only what crossed) and `staple`/`tribute` as what it can offer | A, B | IN-36 residue; republics lane |
| ARC-20, ARC-45 The Tutoring Demand | a formal demand, its two answers, a person sent away | no carrier (the gauge "Invasion Pressure" is refused by Layer 1, ARCS rank 1) | the demand is a `wardship` offered by `covenant` from an Altonian seat; compliance is the ward's `migrate`; refusal is a claim the Katepano holds | A | C-1; ARCS' staged goals for the "threshold" |
| NSC-05 Torben in Altonia | a held person's allegiance moves; retrieval by force | no carrier for being held abroad by agreement | `wardship`'s `forbears` (return) and its breach as licence; the allegiance is CHAR's regard | A | CHAR regard; MB for the retrieval |
| ARC-38 The Sandcastle Alliance | agents of rival external powers; off-map superiors decide (N2) | no off-map superior | the court seat pattern | B | — |
| NPC-083 Hedda Kronvald | a governor spends limited means; her authority issues directives; the settlement makes demands | seats and stores exist; orders bind nobody | graded `issue`; `audit`; the levy roll; `dues` as the settlement's demands | B, C | FA-P1; SE treasury |
| ARC-36 The Tithe That Fed the Enemy | a levy optimised by one actor feeds another | `requisition` unrolled, treasury empty | the levy roll; `farm`/`tribute` forms | A, B | SE `07_SE_treasury_granary_B.md` |
| ARC-17 The Sinigaglia Dinner | a superior's response to a subordinate's disloyalty | FA-P1's recall | the recall that may not arrive (§8) | B | FA-P1 |

Soonest: NPC-089 and ARC-38 (content plus the border rule), then NPC-083, then the tutoring pair.

## 14. Capability and chooser surface

(a) **Capabilities this family's rolls read:** `stewardship` (levy, carriage, seizure; new vocation, to be
defined once in the surface `01_CORE_capability_authoring_surface.md` and `02_CHAR_capability_definitions.md`
propose, by FA-P6's two-row pattern in `rosters.yaml: verb_capability` and `vocation_attribute`; the name
is Jordan's) and `copying` (drafting and delivering an order; existing). `judgment` (FA-P6) for the two
benches. Standing dice by office (SC's T4). Nothing is hard-coded: every number above names its fixture.
(b) **RPG axioms implemented:** skill supplies dice and gates nothing; difficulty class composed of task
plus situational modifiers; range penalty (`remove`); degrees of success with partial success as a real
outcome; a contract as a tracked obligation; reputation as each observer's own tally. **Lacking, and a
designer would expect it:** a reaction roll for a population (here it is the cohort's `regard` entering
the levy, not a separate roll).
(c) **Chooser** (CHAR's statement, `audits/02_CHAR_audit.md` §0A, cited): every decision in this family
is a seated person's through the one chooser: whether to grant, how much to demand, whether to pay,
whether to obey, whether to open the audit. The player takes any of those seats through the same
candidates. **No NPC rule is hard-coded here**; `dues` and `breaches` only stamp referents, as
`vacancies` does. What makes these NPCs characterful is that the same breach is answered with a petition
by one holder and a march by another, and the reason trail is the instrument, the clause and the claim
(`01_CORE_reason_trail_in_the_act_store.md`).

## 15. Research transfer and evidence log

**Transferred (changes what is built):** the governor problem and its three answers `[TREE T5]` → `audit`,
`term:`, the inspector; tax farming `[TREE T2]` → `farm`; prescription and quo warranto `[TREE T4]` →
`hardens`, `quo_warranto`; the oath as the only tie `[TREE Carolingian §1.8; HRE]` → already the engine's
purview rule; tribute's two poles `[TREE T10]` → `tribute` with and without the grantor's `due`;
conquest terms `[TREE T6]` → `capitulation`; hostage-kin `[TREE Shogunate §1.9]` → `wardship`;
invariance under dearth `[TREE T3]` → obtained from the levy's stakes, no rule; elective-but-dynastic
`[TREE HRE §1]` → §5.2 row 3; ministeriales `[TREE HRE §6]` → exported to the bureaucracy lane, not used.
**Tried and did not transfer:** per-settlement Legitimacy and Popular Support scalars, the suspicion
track, `governor_emergence` (`[TREE]` Step 3: all are stored social quantities Layer 1 refuses; each is
re-expressed as a fold); the Hansa embargo (the republics lane's); immediacy and mediatization (no
`province` rung exists to mediate through); transit times (no source, and no need). **Nulls:** the tree
names no shipped game that models an audit at the end of a governor's term with testimony from the
governed, and none that makes a charter's age evidence; this lane found none in
`research/game_precedent_suite/` by grep and did not read that suite in full `[UNVERIFIED]`.
**Memory-grade and unused for any number:** everything marked `[MEMORY]` in §2.

**Evidence log** (`PYTHONHASHSEED=0`; outputs under `scratchpad/runs/INST_COLONIAL/`):
- E-1 `probe_build.py` → `probe_build.txt`: `build_realm(0)`, no season; hash
  `600d8b27147478e158553552cc1409a5`; the counts, oaths, purview readings, foreign rungs, site kinds and
  empty treasuries quoted in §1.4.
- E-2 `grep -rn` over `research/` for the chartered-company, viceroyalty, settler, Mongol and entrepôt
  terms: matches only in `research/by_lane/` cross-references and the historical action catalogue's
  one-line crisis list; no research file on those subjects.
- E-3 a load of `verb_table.yaml` printing `contests:` and `emits:` per row: `requisition`, `transfer`,
  `exchange`, `seize`, `issue`, `covenant`, `revoke`, `confer`, `oblige`, `release` carry no `contests:`
  and a flat `emits:`; fourteen rows are banded.
- Not run: `pytest`; `aperture`; `corpus_run`; any seeded season. Every reading of computed play in this
  file is quoted from the lane audit named beside it.
- Not opened: `decision/options.py`, `loop/witness.py`, `data/verbs.py` beyond grep, `state/world.py`,
  the case files, `audits/02_CHAR_audit.md` beyond its section list, the SE and MB audits, the digests
  (`digests/DG_*`; this lane read the research and the registries they digest directly), `.audit/`.
  Claims that rest on those are quoted from the file that made them and marked.
