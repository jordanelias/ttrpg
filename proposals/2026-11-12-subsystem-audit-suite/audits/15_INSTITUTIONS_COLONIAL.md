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

(§1.3, the geography file's territories and edges, and §1.4, the persons, are appended below once read.)
