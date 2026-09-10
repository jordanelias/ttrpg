# Part D — collisions, conflicts, and the honest residue

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`.

---

## §1 · The Goldenfurt collision table, mechanic by mechanic

Goldenfurt (`systems/settlements/goldenfurt_slice/reference/`, PROPOSAL 2026-06-23, S0–S1 built) is
the repository's most complete answer to *what does managing a settlement feel like*. It also collides
with Layer 1 in at least sixteen places. Each is resolved as **RE-EXPRESS**, **REFUSE with its price
named**, or **kept as evidence Layer 1 is missing something** — never papered over, and never resolved
by deference.

| # | Goldenfurt mechanic | verdict | the re-expression, or the price of refusal |
|---|---|---|---|
| 1 | **Π on the Settlement** (`sim_build_spec.md:41, 129-145`; `registry.py:79` — zero readers, zero writers) | **REFUSE the field · RE-EXPRESS the quantity · REFUSE the homeostat, price named** | Π's inputs are already carriers with licensed decay: unserved Needs are live Petitions and Records with `ttl`; "active grudges" are claims in persons' ledgers decaying at `H-103`; "ambitions in motion" are live `commit`-to-`OUGHT` edges (Q4). `pressure(rung)` is a barrier Query over those, and its band crossings emit (P5's pattern). ⚠ **`restore_toward(3)` is refused**: a term that *raises* pressure in a quiet town is an unwound clock (`T-c`) — *"the world may silt a harbour; it may not sour a town's mood"* (`driver.py:478`; `holonic:848-849`). **Price: a well-governed town goes quiet.** **Substitute:** Q4 — the world moves because named people want things, which is why `W31(a)` puts `commit` first. |
| 2 | **The deck draws `1 + ⌊Π/3⌋`** (`event_deck.md:3`; `sim_build_spec.md:124`) | **REFUSE the draw · RE-EXPRESS the cards** | The draw is a world-driven generator of occasions with no author — `T-c`'s fourth clock. **And greenfield v2 already deleted it for a second, independent reason:** *"two documents cannot both ration the same stream"* (`08_settlement_management.md:223-226`, O-6). A card **is** a `Question`: its trigger predicate is a question source, its responses are the `opening_set`, its `seeds` are `causes[]`. The Π-biased family weighting is `question_sources` order plus the aggregation rule (`H-54`). **The 28 cards become corpus cases in NPC-083's shape** — authoring for `W28`, not mechanism. ⚠ **Residual refusal with a price:** the *Opportunity* family — *"the world offers instead of threatening"* at low Π — **has no author.** A quiet town gets a `yield.taken` surplus or a Site crossing *upward* under `restore`, witnessed as Q3, and nothing else. |
| 3 | **The Directive "arrives"** (§1.4; `sim_build_spec.md:103-115`, *"NEVER none"*) | **RE-EXPRESS (P7) · REFUSE the cadence** | A named person with `remit:issue` spends a scene; scope enumerates executors; each complies or defies. **No mandatory season.** Price: NPC-083's *"owed every season"* becomes *"owed when issued"*. |
| 4a | **Precedent** tag | **RE-EXPRESS** | A `Record` at the Rung (`create_record` executes) — holdable, burnable, forgeable; **it survives succession because the Rung holds it**, which is exactly what `sim_build_spec.md:70` wanted with *"on `Settlement.ledger`, not on the governor"*. Institutional memory is *"Records at a Rung"* (`holonic:520`). **Better than the tag: it has handles.** |
| 4b | **Grudge** tag | **RE-EXPRESS, via `ID-7`** | A claim in the wronged person's ledger, decaying (`H-103`), renewed by re-witnessing. A settlement-level grudge is a **cohort's** grudge — a Person at weight 200 holding the claim. `T-a` refuses the tag; `ID-7` supplies what it wanted. |
| 4c | **Debt** / **Compact** | **RE-EXPRESS** | An `oblige` Tenure with a `T-n` declared term in `payload` — a row that exists and *"left P39's 'a relationship carries state' WITH NO WRITER"* (`write_matrix.yaml:336-342`). A Compact's Petition right is `carry` eligibility. ⚠ `oblige` has no effect (`W31(a)`). |
| 4d | **Reputation: Just / Harsh** | **RE-EXPRESS as `standing`** | `standing_of` exists (`decision.py:692-713`) as the gap between told-by and firsthand claims about oneself; its **polarity** is `F.11`'s open item. A settlement-level Reputation is refused by §D.2's NEVER row. |
| 4e | **Leverage** tag | **RE-EXPRESS** | A `Record` — evidence held; `open_case` declares its stages on it. |
| 4f | **Collective Liability / Bind the Cells** (§1.3b, ED-SE-0020) | **RE-EXPRESS — and it fits better than it did** | A five-household `knot`, stored once on the lower id (`holonic:544`); a member's act is witnessed by knot-mates through the **`firsthand_via_knot`** claim source that already exists (`rosters.yaml:119`). ⚠ The *auto-stamp on the whole cell* is refused — a threshold producing an outcome. **What the knot gives is witnessing**, and the governor's `levy` on the cell is one act against a `knot`ted set. |
| 5 | **The ambition tick** (`sim_build_spec.md:154-165`) | **REFUSE the tick · RE-EXPRESS (it already exists)** | A clock nobody wound — and `08_ch5`'s *"a scheduled recovery tick converts a consequence system into a treadmill"* applies with the sign flipped. **Layer 1's version already runs:** a live `commit`-to-`OUGHT` raises Q4 every season (`world_q.py:223-231`); *"progress"* is the world the acts produced, and *"has the votes"* is others' `commit` edges (P5). **Price: an ambition advances only by scenes, so it is slower — and obstructable (`T-g`), which Goldenfurt's tick was not.** |
| 6 | **AP = 2 + FacilityTier (+1 Seat)** (§1.1; `registry.py:93`; D2 *"canonical"*) | **ALREADY EXPRESSED, with a residual channel** | `budget = 5 + offices × 1 − body − legs` (`decision.py:142-167`, ruled 2026-09-02). ⚠ **Two rulings, two formulas, one quantity** — see §2 row 7. The FacilityTier term has **no person-side channel** today, because `budget` takes no World; the bridge is that a facility **seats an office** (`establish` names *"a rung to establish it at"*), and offices are person-side. |
| 7 | **Needs** (§1.5) | **RE-EXPRESS** | A settlement has no needs; **its people do** (`AX-1`) — Q1–Q4 of persons at the rung; a cohort's need is the population's (`ID-7`). |
| 8 | **Method choice hands power to a faction** (§1.3's design note) | **ALREADY SPELLABLE** | `Develop: funding=guild` is `exchange`/`transfer` with a Guild member as counterparty, whose `hold`/`oblige` edges are the *"standing claimant"*; `corvée` is `levy` on the crowd → `compliance.withheld` by a cohort. Effects for `exchange` and `levy` are `W31`. |
| 9 | **Suspicion → Recall** (§1.4; G606) | **RE-EXPRESS (P7)** | The issuer's own ledger, decaying; recall is `revoke`. **The death-spiral is structurally impossible** (decay), and Jordan's E11 symmetry is free. |
| 10 | **Clerk Capacity / Corruption** (§1.1a, ED-SE-0022) | **RE-EXPRESS — and the opacity is free** | `oblige` a clerk (a Person, P3-minted on demand); the clerk's skimming is a `transfer` to his own hearth, witnessed only through channels, so **the governor holds no claim unless one reached him** (`AX-2`); `Investigate` is the six investigation acts (rows exist, `H-62` ungraded). ⚠ The *"+1 AP per clerk"* is refused — a modifier. **What a clerk gives is his own five scenes spent on the governor's obligations.** |
| 11 | **Survey / Assessment** (§1.3a, ED-SE-0018) | **PARTIAL — one grammar gap** | The locked *kokudaka* is a `Record` whose `subject_matter` is the figure. But a `levy` that reads the Record **rather than live stores** needs a `requires` form reading a Record's `subject_matter` — `[GAP: not among the seven closed forms at `rosters.yaml:883`; a grammar addition, not a primitive]`. |
| 12 | **Encabezamiento** (§1.3a, ED-SE-0019) | **RE-EXPRESS** | Row 4c. |
| 13 | **Ordenanza** (§1.3c, **RATIFIED** ED-SE-0023) | **BLOCKED, not refused** | `petition` → `carry` → a Date → `determine`. **The judging set is absent** (`H-32`, `W26`). |
| 14 | **Local Actors** (`settlement_layer_v30.md:852-862`) | **RE-EXPRESS** | Cohorts (`T-l`, `ID-7`) plus individuation on demand (P3); the count-by-type table is the **world-gen roster**, which is `H-05`/`F.31`'s licensed form (*"a roster read from a registry row; not a clock"*) — **and also greenfield v2's own disposition** (`03_world_population.md:78-91`). Disposition −5..+5 is `stance` (`(Person, stance)` at `[RES]`, no writer — `W-F`). |
| 15 | **The Geneva trap** (§1.3 Keep Order: Clergy; G204) | **RE-EXPRESS — and it is a Query result** | `establish` an office at the rung with `body: <a Church organ>` (`carriers.py:442-472`) → a Church member holds a seat here → `Faction.holdings` (P5) includes the settlement. ***"The Church is the thing holding Goldenfurt together" is `faction_q.resolve(...).holdings`, not a card.*** |
| 16 | **The two-stroke churn guarantee** (Part 4) | **REFUSE the guarantee · KEEP the property** | *"Guaranteed to turn every season"* is the clock. Jordan's design ruling R4 — *"THE WORLD MUST CHURN"* (`references/design_rulings_2026-09-06.md:77`) — is honoured by **Q4 plus P2's bodies clock**: the world moves because people want things and bodies age, and by nothing else. |

**Kept as evidence Layer 1 is missing something — two items, honestly.** (i) **The Opportunity family**
(row 2's residual): a quiet, well-run place generates nothing but matter Events, and **there is no
lawful "the world offers" that is not somebody's act.** (ii) **The FacilityTier → budget channel**
(row 6): infrastructure cannot reach a governor's scene budget without a resolver-side read, and
`budget`'s no-World signature is `T-f`'s. **Both are priced; neither is a primitive.**

---

## §2 · Ratified rulings in conflict — named, not resolved by preference

**1 · `AX-5`'s wording against §25 and §10.3 — resolved by the text, with a wording defect.**
`01_AXIOMS.md:165-181` is a paragraph about **individuation**: *"the world may never individuate a
person nobody's act demanded. A world-generation roster is not a clock and is lawful; a population that
grows on its own is not."* Six lines earlier (`:168-170`) it says *"birth is envelope weight, not a
`create`, so individuation is not 'bodies'."* **So the axiom itself separates two quantities** —
envelope weight (bodies clock, licensed at `holonic:854, 860, 1040`) and the count of `Person` carriers
(demand-only, `driver.py:1375-1383`). **Not a contradiction: a scope distinction the same paragraph
draws.** ⚠ **The defect is the word *"population"* at `:179`**, which a strict reader can attach to the
envelope; it should read *a headcount of persons*. Recorded on the axiom; not re-argued.

**2 · `driver.py:431-436` against `holonic:854, 868-871` — the code refuses a licensed motion.**
The comment reads `T-b` and L4 too widely: a body is not an outcome, and `body` is `social:false`. By
§0.05 (*"decide and then CHANGE THE CODE"*), §0 test 3 (answered by a design document) and test 4
(precedent: `Site.condition` wear crosses floors and emits without an outcome), **this is not an
escalation.** P1 is the fix.

**3 · Greenfield v2's *"not a function of time"* against Layer 1 — superseded on one point, dissolved
on the other.** `03_world_population.md:50` quantifies over the **person store** — its four events at
`:151-159` all move `|persons|`, and `:164-165` says *"Population count and population composition are
different questions."* Layer 1 agrees that **no clock mints a Person**. **The envelope is not persons**
(ideal-v2 `01:587-589`: *"not the representation of the living population"*), so greenfield's rule has
nothing to say about it and P2 does not violate it. ⚠ **Where they genuinely conflict** — greenfield
§4.1:167-173's *"Death is an outcome, never a clock"* against `holonic:854`'s *"natural death | one of
the three licensed clocks"* — **the RATIFIED text (ED-IN-0204, 2026-09-05) postdates the PROPOSED one
(2026-08-29, "held back from ratification-on-merge") and governs.** Greenfield's reason (ED-IN-0201's
head-post gate) is answered by Layer 1 differently: the seat falls vacant, and *"if no person acts, the
thing does not occur"* (`09:51-53`). **A third position exists and is refused:** from-scratch's
*"Producer: birth… all acts"* (`04_hearth_and_community.md:155`) makes birth an act, contradicting
`holonic:403`. Layer 1 governs.

**4 · `q_s = 0.5·L_s + 0.5·PS_s` (`settlement_layer_v30.md:165`) — this set sides with
governance-corpus-rebuild's disposition, for a Layer 1 reason.** In Layer 1 there is **no `q_s` to
calibrate**: Legitimacy is what is held *right about the seat* — a Query over Records (charters) held,
and commits to the *title's* proposition — while Popular Support is P5's commit share. **Two Queries,
blended only at a consumer**, and `AX-3` is what keeps them apart: evidence moves the first through
Records, argument moves the second through commits. Greenfield's C-6 (*"an unre-calibrated improvement
is worse than the thing it improves"*) is **right about a field and moot about a Query pair**.
`lps_wiring_v1.md`'s `compliance(s)` (`:85-86`) survives as the consumer-side blend, **on the legacy
tree only.**

⚠ **AND THIS DIVERGES FROM R7 ON THE SAME QUANTITY, WHICH THE FIRST DRAFT DID NOT ACKNOWLEDGE.** R7
assigns the inputs differently: *"holdings count and military capacity and influence are Queries over
`hold` and `commit` edges; **legitimacy, the leader's standing and populace morale are Queries over
`stance`/`convictions`**."* This row derives Legitimacy from **Records held plus commits to the title's
proposition** — that is, from edges, not from interiors. **R7 governs and this row does not follow it.**
The reconciliation is not available to this set, because following R7 requires something to write
`stance`, and that is `H-62`, which nothing here proposes (§6.2). **Recorded as a divergence from a
ruling on the same quantity, not resolved.**

**5 · `scale_hierarchy_v1.md` §2 (RATIFIED 2026-07-13) against `rosters.yaml:92` (RATIFIED
2026-09-05) — a live tension, recorded.** §2: *"territories are the fixed geographic units; a province
is an emergent aggregation that exists only while its constituent territories share a common faction
holder… simply stops existing as a unit."* Layer 1: `province` is a `rung_kind` with a `contain`
parent — **a stored address.** Two readings: **(a)** the rung is the *address* (where a provincial
court sits, holds Records, has Dates) and province-hood is a Query
`coheres(w, rung) = all holders of the territories' hold-Tenures commit to one proposition` — cheap,
and it keeps `r1_aggregate` walkable; **(b)** the ruling's literal — no node, provinces named on the
fly. §0's tests: not superseded explicitly (ED-IN-0204 does not cite §2); not irrelevant; **test 5
favours (a)**, because `02_HIERARCHIES.md:87` needs single-parent for *"aggregate over my
descendants"*. **Recorded as (a), with the residual that §2's *"stops existing"* is then metaphorical —
and not escalated. But no synthesis may present §2 as unmodified.**

**6 · `(Person, weight)`'s `by:` cell and `H-49` against `driver.py:425`** — a matrix provenance cell
asserting a reader that does not exist. `ID-13` **at the register**. P1 makes it true; **the cell must
be rewritten either way.**

**7 · `AP = 2 + FacilityTier` (D2, *"canonical for player-facing play"*) against `scene_budget = 5 +
offices` (ruled 2026-09-02, `fixtures.py:161-171`)** — two Jordan rulings, two formulas, one quantity
(a governor's per-season action budget), on two trees. ED-IN-0204 governs `engine/season/`; D2 is on the
retire-set. The *shape* D2 carried — infrastructure raises capacity — survives only through the office
channel (§1 row 6). ⚠ **An `S` defect (*"two ladders for one quantity"*) exists across the trees until
the legacy formula is retired with its tree.**

**8 · The orchestrating session's own chain — *"`stores/weight` falls → `need` fires"* — is false at
that link** (`01_PRIMITIVE_BASE.md` §3.4). Recorded here so that no reader of this set carries it
forward as a fact about the code.

---

## §3 · The adjudications this set was asked to make

### §3.1 · The `Field` / `Gauge` proposal — **SUPERSEDED**

`systems/_architecture/reference/governance_type_registry_v1.md:243-298` proposes a `Field` (or
`Gauge`) parallel to `Key`: persistent, continuously readable, with a **required `decay_fn`** and a
**required `aggregate_fn`**. **Verdict: superseded by ED-IN-0204. Close it with `T-a`
(`01_AXIOMS.md:255-282`), §D.2's NEVER row (`:824-825`), and `ID-1`'s barrier cache (`:426`).**

**The concrete test, with Π as the quantity, because a verdict without one is a preference:** a Field
with a `decay_fn` integrates past inputs with forgetting. **A Query over carriers that themselves decay
under the three clocks** — a Record's `ttl`, a Claim's `confidence`, a Tenure's `until` — **integrates
the same history with the same forgetting, and keeps the inputs addressable.** You can burn the
petition, bribe the clerk, kill the man who must renew the term. `aggregate_fn` is `r1_aggregate`.
**The one capability a Field has that a Query lacks is a value whose inputs no longer exist — and that
is `AX-6`'s ratchet by definition** (*"a state nobody can end"*, `:394`). The cost of the Query form is
O(edges) per read, answered by the barrier cache (`04_CODE:153`).

⚠ **What survives of the proposal, and it is real:** its `derived_flags` — a VECTOR throwing a FLAG at a
threshold — **is `ID-17`'s "band on a Query"**, and Layer 1 has that **only for `Site.condition`
today**. Reading 09 §2:104's *"when the share crosses a declared band, the crossing emits"* has **no
producer**. **P5 builds the first one.** So the registry **named a real absence and proposed the wrong
carrier for it.**

### §3.2 · Three research primitives that do not survive, and why

- **Dual scoring modes under uncertainty (Pax Pamir).** **No scoreboard is lawful** — a stored campaign
  aggregate. The expressible form is two `OUGHT` Propositions the player commits to, with an ending
  evaluated on which holds (`W30`; `ENDINGS_CLASSIFIED.yaml`). **Null on "scoring"; not null on
  "opposite investments under uncertainty", which is `AX-2`.**
- **Work-areas / auto-allocation (Dawn of Man, Banished).** **Refused as stated** — auto-allocation is
  nobody deciding (`AX-1`). The lawful crowd-labour is a cohort's `work`. ⚠ Whether a cohort's `work`
  delta **scales with weight** is open: `_eff_work` (`effects.py:214-229`) reports the site and defers
  the delta to §27.3's accumulator, and the delta's source is the act's payload, not `weight`.
  `[GAP: cohort labour magnitude — `W32`'s item]`.
- **Influence as a priced currency for weighted voting (Bannerlord).** **Refused:** the budget is
  **scenes**, and a second budget is the engine deciding options
  (`03_VERBS_AND_LOOPS.md:136-144`). **Price: there is no "spend influence" verb.** Influence is
  `faction_value` (P5) — what you *have*, not what you *spend*.

### §3.3 · The two cautionary tales the uploaded research ends on

The Guild 3's emergent NPC AI was repeatedly **disabled** because citizens burned the player's house
down; Tropico's fully-simulated citizens visibly shack-squat. **The unsupervised-cast risk is bounded
here by three things Layer 1 already has:** the scene budget (nobody does more than five things);
refusal-emits (an NPC's act on your house is a contest, not a write); and de-individuation (P3) — a cast
nobody remembers folds back.

⚠ **What is *not* bounded is expression.** `08_ch5` §8.2's Tale-Spin finding applies: **P2's envelope
Events and P5's crossings are tracked, and nothing in this set expresses them beyond the log.** Named
as the set's unbudgeted line item, in the same milestone as the substrate rather than after it.

---

## §4 · The one genuine escalation — **E-1** (filed as `ED-SE-0051`, `needs_jordan: true`)

Every other open question in this set was closed by `CLAUDE.md` §0's five tests. **Closed without
Jordan, with the test that closed each:** the starvation comment (tests 3 + 4); `AX-5`'s wording (test
3); greenfield's death rule (test 1); the `Field`/`Gauge` (test 1); the province node (test 5,
recorded); AP against scenes (test 1); *"can an NPC take the player's seat"* (test 5 — `T-g`: a player
is a Person, and a `player_seats_are_contestable` toggle is special-casing an entity, which §10 forbids);
the nine dispensation terms (authoring; test 4, on `conviction_axes`' `incomplete:` precedent); and
founding at settlement kind (**already** `needs_jordan` as SE-9(a) — not re-raised).

> ### **E-1 · The bound on the demographic loop: matter only, or matter plus hearth capacity?**
>
> **Filed as `ED-SE-0051`** (`registers/editorial_ledger_se.jsonl`, `status: open`,
> `needs_jordan: true`), because a PR body is not a persistence channel and there is no context
> between sessions. **That row queues the question and ratifies nothing** — it is the one row
> `CLAUDE.md` §0 permits an adversarial pass to append, and it qualifies on the only ground §0
> allows: it requires a human decision.
>
> **P2 as specified is bounded only by the larder — Malthus.** A fed hearth grows until it cannot feed
> itself, and P1 thins it. **The alternative bounds births additionally by a capacity of the hearth's
> Sites** — Banished's housing — as a `hearth_capacity` fixture table per `site_kind`, adding no new
> primitive.
>
> **These are materially different games.** Matter-only produces waves the player cannot pre-empt except
> by grain. Capacity makes **P4 the lever** the uploaded research says the genre's strongest entries
> (Manor Lords, Banished) actually use, and lets the player throttle growth by building.
>
> **Layer 1 is silent:** §25 licenses the clock and names no bound. §0 test 5 leans to the matter-only
> arm, because it uses only what exists — **but the feel of settlement management turns on this, and it
> would not be an engineering call.**
>
> **Priced.** Matter-only costs nothing new. Capacity costs one fixture table and one conjunct in P2's
> births term. **Both ship with P1 as the `−` term either way.**

**Closest calls that did *not* survive the five tests, named so nobody re-raises them:** whether the
envelope eats (calibration, `ID-6`); whether cohort deaths land at MAT or CEN (a matrix edit; test 5;
swept); and de-individuation (already ruled at `holonic:1019`).

---

## §5 · What could not be established

- `[GAP: whether loader invariant 2 fires today on `(Rung, exists)` / `(Site, exists)` — `engine/season/data/matrix.py:200-230` was not opened. It decides whether P4 is a **fix** or a **first producer**.]`
- `[GAP: `combat_seam.py`'s path import of `systems/combat/` — not opened; the second seam is `requirements.yaml:99-103, 286`'s claim, not a read.]`
- `[GAP: the register's next free `H-` id — allocate above `H-112` by reading the tail of `engine/season/hole_register.yaml`, **never max+1 by assumption**.]`
- `[GAP: whether `Record.forgery_quality` has any reader — bears on P7's *"forgeable"*.]`
- `[GAP: cohort `work` magnitude against `weight` — `W32`.]`
- `[GAP: `incompatible(a, b)` beyond same-subject / same-predicate / different-value — unspecified; P5 records a hole row rather than reaching for natural-language processing.]`
- `[GAP: the envelope's `marks_bundle` and `capability_distribution` (ideal-v2 `01:595`) — Layer 1's `Envelope` is **counts only** (`holonic:372`); P3 mints with empty capability and says so. `F.6`'s `practice` verb is the repair, and it is outside this set.]`
- `[GAP: the `world` scale's 10 cases (`W28`'s *"≥2 realm Rungs"* reading) — untested against P5's `faction_value`, which sums over one containment tree.]`

---

## §6 · The rulings of 2026-09-06 — found late, and they move three things

⚠ **`references/design_rulings_2026-09-06.md` was found after this set was drafted, and it is the most
current ruling surface in the tree — eight Jordan rulings given in conversation on 2026-09-06, the day
*after* ED-IN-0204 ratified Layer 1.** Its header: *"Authority, not inference… recorded here because
nothing else in the tree carries them."* Under §0.05 it is REFERENCE and ratifies nothing; as **agent
instruction and as a record of what Jordan has decided**, it governs what this set may claim.

⚠ **A caveat on reading it, so nobody scores it wrongly:** it cites `engine/season/` and `architecture/`
against the then-unmerged branch, and its `shape.py:NNNN` references point at a file the decomposition
(ED-IN-0203) has since **deleted**. An unresolvable `shape.py` line is **relocated, not fabricated** —
its symbols moved into `engine/season/state/`, `loop/`, `queries/` and `decision.py`.

**Three of the eight move this set.**

### §6.1 · R2 — the refusals are instrumental, not terminal, and that binds this document

> *"you have license to do whatever makes for the best game architecture. your only constraints are
> making this as dynamic and capable and flexible and emergent and persistent as possible."*

The reading recorded there: **the ratified refusals become instrumental rather than terminal. *"Each
must be justified against these five or changed."*** With the caveat that most were derived to serve
exactly those properties — *no target on an Event* exists **because misattribution is a feature, and
that IS emergence**; *only a person acts* is why obstruction and deception need no verbs; *no stored
aggregate* is why a resolved view cannot go stale — so a naive reading **reduces what it means to
increase**. And the standard it sets: *"the null result — 'examined, this refusal earns its place' — is
a real finding, and must be argued rather than deferred to."*

⚠ **Applied to this set honestly, that is a mixed score.** §1 refuses eight Goldenfurt mechanics.
**Argued against the five properties, with a price stated:** Π's `restore_toward` (row 1 — *"a
well-governed town goes quiet"*), the deck draw (row 2 — the Opportunity family has no author), the
mandatory Directive (row 3 — *"owed every season"* becomes *"owed when issued"*), the ambition tick (row
5 — slower, but **obstructable**, which the tick was not), and the clerk AP bonus (row 10 — what a clerk
gives is his own five scenes). **Deferred to an axiom rather than argued — four, named by the adversarial pass:** (i) the
**auto-allocation** refusal (§3.2), which stops at *"nobody deciding (`AX-1`)"* and offers a substitute
— *"a cohort's `work`"* — that **does not execute**: `work` is *"attempted and always refused"*
(`requirements.yaml:203-204`) and `H-105`'s `work` effect is graded absent, with no price named;
(ii) the **Bind-the-Cells auto-stamp** (§1 row 4f); (iii) the **"+1 AP per clerk"** (§1 row 10); and
(iv) **lps_wiring's independence roll** (P5's *Refuses*). Each is a single axiom-citation with no
price. **Named as a debt of this document**, not repaired here, because repairing it is an argument
and not an edit.

⚠ **AND A READER MUST KNOW WHICH CRITERION WAS APPLIED: this set was evaluated against §0.06's NERS
definitions and NOT against R2's five properties.** Those are different tests. A proposal that passes
NERS may still fail *"dynamic · capable · flexible · emergent · persistent"*, and **nothing here has
been scored against them.**

### §6.2 · R7 — the decisive ruling ratifies P5's shape, and exposes what this set is missing

> **RULED: no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED.**

That is P5's whole approach, and the refusal of stored L/PS (§1 rows 1, 4d, 14), arriving as a direct
ruling rather than as an inference from `T-a`. It also settles the fork this set assumed away: **echo
model** (a battle lost → legitimacy −2 everywhere, instantly) versus **architecture model** (only those
who *learn* of it revise). Jordan: *"yeah this is better."* And the consequence the set should have led
with: **⚠ there is no single faction-legitimacy number — it is a field over the population, so a ruler
can be wrong about their own standing**, which makes `§C.11`'s explanation contract **structural rather
than a courtesy**: the player sees their character's estimate, never the true aggregate.

⚠ **AND IT NAMES THE HOLE IN THIS SET.** R7 holds that *legitimacy, the leader's standing and populace
morale are Queries over `stance`/`convictions`* — over **interiors**, not over `commit` edges — and
therefore that:

> ***"`H-62` is unavoidable and first-rank. Nothing moves until a verb writes an interior."*** And:
> *"`H-62` + `H-84` ARE this ruling's mechanism."*

**`H-62` is tier 0 and grade `absent`** in the live register: *"NO PART E VERB WRITES ANY `Person`
INTERIOR"*, with 11 RES rows lacking a producing verb, six of them `Person` interior. **This set
contains no proposal for it.** P1 writes `Person.body`, and on the set's own argument (§C.1) that is
**read-off matter, not interiority** — so it does not count. **The set therefore proposes seven
producers and omits the one Jordan's own ruling calls first-rank.**

**Stated as a gap rather than patched**, because the repair is a design object of its own: the shape is
already supplied — an interior write is *a consequence of an outcome*, which is what the `Degree`-keyed
`writes` column declares (`#358 rev.2 §C.4`) — so what is missing is **which verbs write which axis at
which degree**, and that is a proposal this set did not make. **P5 is weaker for it:** the commit share
it computes is the *risk-of-revolt* Query Reading 09 licenses over `commit` edges, and it is **not** the
legitimacy Query R7 describes over `stance`. Two different quantities, and this set builds only the
first.

### §6.3 · R6 — *"propagation without reaction is a chronicle, not a game"*

R6 rules that a domain echo is **a fact, not a magnitude** — the governor dies in a duel, and the game
records factually that the settlement is now absent a governor. It then names the missing link and calls
it *"the plan's spine"*:

> **THE FACT PROPAGATES AND NOTHING REACTS TO IT.** *"Nothing forms a Question about a vacant office.
> `question_sources` carries Q1–Q3 plus Q4 `need` and none is 'a world-fact changed in a way that
> concerns me.' So the governor dies, the office empties, and no ambitious person forms a candidate."*
> And the constraint on any fix: **`choose` receives no World**, so a person cannot notice a world-fact
> directly — it must reach them through their ledger or their View.

The rulings file's own closing summary makes this the single outstanding item: *"work, not a ruling —
and it is one item, shared with R8: **build the consumer that makes a person form a candidate from what
they came to believe.** Until that exists, every epistemic carrier this file names is a carrier without
a reader."*

⚠ **This set is almost entirely producers, and it should say so.** P1's Q3-referent fix — changing the
band-crossing question's referent from a **verb name** to the person's containing rung id, so
`opening_set` can form candidates at all — **is a consumer fix, and it is the only one in the set.** It
is currently buried in P1's *Adds* as a data correction; **on R6's reading it is among the most valuable
lines in the set**, because a question source that produces no candidate is exactly *a carrier without a
reader*. **The vacancy case R6 names is not addressed by anything here.**

### §6.4 · The other five, in brief

- **R1** closes `F.32` — the war survives its declarer through the seat, and the inheritor gains
  **standing in a peace negotiation, not an automatic exit.** **Layer 1's `F.32` row at
  `04_CODE:1136` is unswept.**
- **R4 · THE WORLD MUST CHURN** — *"Lands on `F.20` — the world only decays. `Rung.exists` and
  `Site.exists` have zero producers."* **This is a direct Jordan ruling on P4's exact subject**, and P4
  executes routes (1) *churn by NPC action* and (2) *churn by matter* of the four it names. §1 row 16
  cites it only for the churn *guarantee*; **it is more than that — it is P4's warrant.**
- **R5** distinguishes **engine persistence** (snapshot, save, load, the log) from **diegetic
  persistence** — *"what the world itself holds, in objects that outlive the witnesses and can be moved,
  copied, forged, seized and burned"* — and rules the second **a game mechanic**. That is P7's warrant,
  and P7 does not cite it. It also records that **`_ch_document_key` was repaired 2026-09-07
  (ED-IN-0202, PR #379)** to test the subjects in `changes[]` (`engine/season/epistemic.py:259`;
  `loop/predicates.py:86-92`) — so the **channel** fires for non-authors, while **`H-84`'s Record-moving
  half remains tier 0 and `absent`.** The set's treatment stands, with that refinement.
- **R3** is six requirements read as one loop, and **R8** rules that every term of an observation —
  identity, act and motive — is **independently unknowable and its own claim**, not a field. ⚠ P5 should
  be read against R8: it assumes a witness of `commitment.made` knows **who** committed. Under R8 that
  is a `who` term that may be `None`. **Not repaired here; named.**

---

## §7 · The loop register, as it would stand

`ID-16` requires a design to enumerate its loops and **sign** each one; `G13` requires an amplifying row
to name its bound in `default:` — **and its clause 3 is a presence check that would accept `"TBD"`**
(`register.py:329-333`), so the bounds below are stated to be real rather than to pass a gate.

| row | kind | sign | bound in `default:` | from |
|---|---|---|---|---|
| `H-102` | LOOP | **+** | the fixtures (`ask_budget`, `ledger_cap`, decay, aggregation `first`) — its own cell says *"UNDER THIS INSTRUMENT'S OWN FIXTURES IT CANNOT AMPLIFY AT ALL"* | existing |
| `H-103` | LOOP | **−** | none — damping | existing |
| `H-104` | LOOP | **−** | none — damping | existing |
| `H-112` | LOOP | **+** | a MATTER-only buffer `if` | existing (**a defect**) |
| `H-<a>` | LOOP | **−** | none — dearth thins the eaters; the draw falls | **P1** |
| `H-<b>` | LOOP | **+** | `fed_ratio` (P1, `H-<a>`) · `mortality[elder] = 1` · finite yield per Site (`H-93`) · `season_factor` (`H-26`) | **P2** |
| `H-<c>` | LOOP | **+** | `scene_budget` · the grown band (P2) · de-individuation · `W29`'s ceiling (**engineering, not design**) | **P3** |
| `H-<d>` | LOOP | **+** | wear (`H-07`) · the stake cost · `season_factor` · scenes | **P4** |
| `H-<e>` | LOOP | **+** | scenes · presence (`fan_out_mode`) · `repudiate` (P6) · `claim_decay` (`H-103`) | **P5** |
| `H-<f>` | LOOP | **−** | none — repudiation removes edges | **P6** |
| `H-<g>` | LOOP | **−** | none — defiance invites revocation; compliance accumulates nothing | **P7** |

**Four amplifying, three damping, and every `+` names an existing `−`.** `ID-16`'s *"season 40 resembles
season 30"* stops being the only available outcome, **and each way it can stop is a row a loader
validates and a test executes.**

⚠ Two honest qualifications on the register itself. **`G13` cannot see a loop nobody declared** — which
is how `H-112` went unrecorded until an audit read `World.write` — so this table is a claim about the
loops this set *knows about*, not a completeness claim. And **`H-106`, the derived check that would
recompute the cycle set from what is written against every typed reader, remains unbuilt** and blocked
on `F.24`.

---

## §8 · The adversarial pass

Per `CLAUDE.md` §0, no result here is reported without having been attacked, and per §10 the critic was
made structurally independent rather than declaredly so: a read-only agent with `Read`, `Grep` and
`Glob` and **no write tools**, holding **this document set and not the reasoning that produced it**, and
instructed to break it against the working tree.

**Twelve findings, ranked by consequence. Nine changed the documents; three are recorded as debts.**
The critic's own summary of the base it attacked: *"The set's factual base is unusually accurate; the
failures above are almost all in composition, grading and self-scoring, not in the reading of the
tree."* That is the shape of what follows.

### §8.1 · What it broke, and what changed

| # | finding | disposition |
|---|---|---|
| **1** | **P5's amplifying loop has no producer for its first arrow.** `opening_set` forms a candidate only for `subject in q.referents` (`decision.py:183, 228`); Q2's referents are `(c.subject,)` and fire only when `c.subject in mine` — i.e. **only for a person who has already committed**; Q4's referents are `(prop.subject,)`, **the Proposition's subject field, not its id**. **An uncommitted bystander can never form a `commit` Candidate.** | **FIXED.** P5's loop is regraded **declared and unreachable**, the `H-102` shape; the missing fifth question source is priced as **a new primitive this set does not propose**; and `01_` §3.4's four broken links are corrected to **five** |
| **1b** | **P5's falsifier could not observe that.** It asserted a share equality with a control of *"no `utter` → the share raises"*; **on a tree where nobody can form a `commit`, both arms pass: `0 == 0`** — `ID-10` in §0.1 pt 2's exact shape | **FIXED.** The treatment arm now asserts `len(live commits) > 0` **before** the equality, and a second adverse control pins that zero `commit` Candidates form |
| **2a** | **`04_` asserted `F.32`'s gap stands.** R1 closed it — *"the last surviving escalation before this ruling"* | **FIXED** (§C.6, correction visible) |
| **2b** | **§2 row 4 derives Legitimacy from edges; R7 rules it a Query over `stance`/`convictions`** | **RECORDED as a divergence from a ruling on the same quantity, not resolved** — following R7 needs `H-62`, which nothing here proposes |
| **2c** | **R2 makes the refusals instrumental; four are deferred rather than argued** | **FIXED** — §6.1 names all four, and records that this set was scored against §0.06 and **not** against R2's five |
| **3** | **A Person minted at CENSUS cannot have witnessed the act that demanded them.** WITNESS runs before CENSUS (`driver.py:1391-1399`), so a minted Person has an empty ledger, and Q2 requires `c.when == w.tick - 1`. **Corollary: every Event emitted at CENSUS is unwitnessable** — which hits P3's `person.individuated`, P2's reconciliation emission, and P5's CENSUS crossing | **FIXED.** §C.3's trace is corrected — the cohort's first possible question is **`t+2`**, and the general corollary is stated |
| **4** | **Six compliance rows graded STRUCTURAL where the checker is a runtime refusal** — the measured defect class `04_CODE:78-80` names. The set was internally inconsistent about one function: `world.py:325-343` graded STRUCTURAL and `:351-357`, eight lines later in the same body, graded MECHANICAL | **FIXED.** All six regraded to `STRUCTURAL under the gate · MECHANICAL at runtime`, or to MECHANICAL/CONVENTION, per `:88-92`'s required form |
| **5** | **P1 and P2 disagreed about the subsistence denominator** — a third expression for one quantity, in a set whose §3.2 exists to end the second; and on the literal reading **the named cast absorbs the envelope's hunger and dies at the first shortfall**, the opposite of the damping claimed | **FIXED.** `mouths(r)` is defined **once**, in P1, and used in both the draw and the deficit share; P2's falsifier gains an **envelope-present** arm, since neither existing arm could see the disagreement |
| **6** | **"Six of seven NPC-083 needs met" was unsupported** — need 3's second half (*"repeated defiance accumulating toward a threshold"*) is refused by the same `T-b` argument used to refuse need 7, and need 2 is met in vocabulary only | **FIXED.** Rescored **four met, two in vocabulary only, one refused** — in all three places it appeared |
| **7** | **P1's "one data fix at `world_q.py:221`" does not produce its own falsifier's referent.** `at = w.sites.get(who).rung` is `None` for a person id | **FIXED.** Restated as a **branch** (`parent_of` when `who` names a person), with the second under-specification named (the branch fires for that person only) and `H-110` distinguished |
| **8** | **`faction_value` and `population` have no consumer** — `ID-13`, the defect class the set itself catalogues against `Sensation.standing` | **FIXED.** Both marked `[GAP: no consumer]`; P5 now states plainly that it supplies §5.1's **arithmetic and not its use** |
| **9** | **The set cites eight lines of a comment and stops immediately before the measured control adverse to its own thesis** — `all_five` measured **0 of 1,467 forks** changing a later decision | **FIXED.** §C.8 now carries it, and says which clause each epistemic claim runs through |
| **10** | **P7 overturns a written refusal** (`verb_table.yaml:117`, `rosters.yaml:873-876`) **without flagging it**, where P1's equivalent overturn is flagged loudly | **FIXED** at the site, **and in `00_INDEX.md`'s held-back list item 4**, which now names both overturns instead of saying "two" and naming one |
| **10b** | **P7's falsifier passes and its stated mechanism was wrong** — the candidate is absent for want of a **referent** (clause 3), not for want of a ledger claim; clause 4's ruled polarity is *"absence of a belief is not a belief in the negative"* | **FIXED**, with the correction visible, because *"a reader who built from the explanation would have built the wrong thing"* |
| **11a** | **P4's `AX-4` named a checker that cannot see P4's failure** — `F10` weighs rungs across its own probe season, which never runs `found` | **FIXED.** Regraded **CONVENTION**, with what would earn MECHANICAL named |
| **11b** | **§D.0 files `weight` as *read off*, and P1/P2 write it as matter** | **RECORDED.** The critic grades P1's *body-is-the-case* argument **sound**, and finds the `weight` tension **inside Layer 1** (the matrix row is MATTER at CEN) rather than an error by this set — but the set extended its §D.0 argument from `body` to `weight` silently, and should not have |

### §8.2 · Three observations the critic recorded without ruling on

- **Layer 1 says `scale:` on verb rows is *"deleted; the loader rejects the key"* (`04_CODE:173`), and
  the tree does the opposite:** `engine/season/data/verbs.py:96` carries `scale: str = "person"`,
  `:234` reads it, `:293-297` raises `SystemExit` if it is **not** a rung kind, and
  `verb_table.yaml:126, 138, 437` still carry `scale: "settlement"`. **P4 proposes two verb rows with
  no `scale:` cell, which the loader will default to `person`.** This set asserts Layer 1 compliance
  throughout and never meets the divergence. **Unresolved, and it bears on P4 directly.**
- **The executable copy of the legacy L/standing is under `engine/`, not in prose.** §2 rows 4 and 7
  locate it *"on the legacy tree"* and cite only `.md`. `engine/autoload/game_state.py:109-133` is a
  live `Faction` dataclass with `L`, `Sta`, `standing` and `territories` as **stored fields** — the
  shape P5 forbids and §5.1 rules against, in Python, under `engine/`. It sits outside
  `engine/season/` and so outside Layer 1's stated scope; **whether it collides is not ruled here.**
- **Vocabulary collision, and `CLAUDE.md` §4's idempotence test bites.** This set uses bare `R4`, `R5`,
  `R7`, `R8` for **both** `requirements.yaml` rows and `design_rulings_2026-09-06.md` rulings.
  **Read `R-0N` as a requirement and bare `RN` as a ruling**; where it matters the citation
  disambiguates, and a later session should not have to work that out.

### §8.3 · What survived, and the attacks that failed

A PASS reported here is licensed by the attack named, not by an absent finding.

- **`Rung.envelope`** — declared, matrix row exact, `steps: [MAT, CEN]`, `by: DR-1`. The critic grepped
  `envelope` across all of `engine/**/*.py`: **the only write is the W9 probe and the only read its own
  assert. Upheld.**
- **`Person.weight`** — no writer anywhere; readers `probes.py:119` and `:691` only, both harness.
  **Upheld.**
- **`driver.py:425` is `wt * len(eaters)`** — verbatim, a head count. *"The set's sharpest claim — a
  cohort at weight 200 eats as one person — **is true**, and the two-arithmetics `S` defect is real…
  **the best finding in the set.**"* The falsified `by:` cell is `write_matrix.yaml:222` and `H-49` is
  `hole_register.yaml:558-560`. **Upheld.**
- **P1's overturn of the starvation comment holds, and it was attacked properly:** `T-b`'s *"an outcome
  is what a decision produces"* verbatim at `01_AXIOMS.md:285-286`; `(Person, body)` is
  `social: "false"` at `write_matrix.yaml:165`; the L4 gate fires only on `social and driver != "Act"`;
  §25.2 licenses MATTER touching persons; and `Site.condition` is the precedent that emits a crossing
  without an outcome. **Not an escalation, as claimed.**
- **The `AX-5` adjudication is sound, and the critic tried hard to break it.** The scope distinction is
  in the paragraph's own text: `01_AXIOMS.md:169-170` forecloses the bodies defence *for individuation*
  on the ground that *"birth is envelope weight, not a `create`, so individuation is not 'bodies'"* —
  **which necessarily concedes that envelope weight IS bodies.** **Not special pleading.** ⚠ One thing
  it says the set should state aloud and does not: **`fed_ratio` makes an act-reachable quantity
  modulate a licensed clock's rate**, and *"you cannot bribe silt"* is at least arguable against that.
  **Disclosed but never attacked. Recorded.**
- **P3's demand-driven mint respects `F.1`** — Layer 1 already assigns CENSUS *"the log for demand
  kinds"* (`04_CODE:161`), and a refusal Event **is** a demand in `F.1`'s sense. **Its defect is timing
  (finding 3), not licence.**
- **The `Field`/`Gauge` supersession is *"the strongest single argument in the set"*, argued rather than
  deferred, and the critic could not break it.**
- **Status claims all check out** — ED-IN-0204, §5.1 RATIFIED 2026-07-13, §2's *"stops existing"*,
  ED-SE-0023, ED-FA-0020/0022/0023, and ED-FA-0021 merged with `needs_jordan` FALSE. **Nothing proposed
  is presented as ratified.**
- **`H-84`: the set is right, not stale.** R5's repair fixed `_ch_document_key`'s witness predicate and
  narrows the row to the **Record route only**; no verb seats a `hold` on a Record today. **P7's
  dependency on `W24(a)` is correctly stated.**
- **The `[GAP:]` entries are real** — three spot-checked, none contradicted by an assertion elsewhere.
  **The `assumption` discipline holds:** *"I could not find a bare constant asserted as measured
  anywhere in the six files."*

> ### §8.4 · The null the critic states explicitly
> *"I looked specifically for a stored aggregate, a container clock, a threshold producing an outcome,
> an institution acting, or a two-writer value. **I found none.**"* `T-i` is respected — P2's pass is
> one driver loop over all rungs, matching the wear pass. `AX-1` is respected — no proposal gives an
> institution an `Act.actor`. **The claim that the set adds no carrier, `Tenure` kind, eligibility
> kind, step, write class or `Sensation` scalar is true as far as it could be tested**, and the
> primitive it comes closest to needing — a Query term in `requires` — **it names and refuses,
> correctly.**
