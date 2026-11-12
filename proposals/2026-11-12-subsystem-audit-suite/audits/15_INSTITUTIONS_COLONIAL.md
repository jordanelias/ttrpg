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
| `requisition` (a levy) | **what the place yields** | `stewardship` (a new vocation, by FA-P6's interface) + SC's `standing_dice` when through a seat | `difficulty` routine + `remove` + `stakes` (share of the place's store demanded: `levy_ob`, ≤¼ 0, ≤½ 0.5, more 1.0) + `regard` (the place's cohort toward the actor) − `evidence` (a held assessment of the place, §4.3; a grant the cohort has heard of) | full amount and the actor learns the store's true size · full amount · half (floor), the rest stays · nothing moves, `requisition.refused`, witnessed |
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

(§4 onward is appended below.)
