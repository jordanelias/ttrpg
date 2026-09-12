# Part E — Valoria plotted on every axis in the suite

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠⚠ **SUPERSEDED BY `proposals/2026-09-12-emergent-narrative-primitives-v2/` (same session, same
`ED-IN-0217`).** This set applied the wrong test: it disposed of mechanics on **architecture rules** and
**implementation facts** as though those refuse an idea, which they do not — and it never cited **`R2`**,
the ruling that makes every refusal *instrumental, not terminal* and requires each to be **argued** against
five terminal properties (`references/design_rulings_2026-09-06.md:37-50`). Its facts are largely sound and
its citations reproduce; **its verdicts do not follow from them.** Kept as the audit trail. Read
`…-v2/02_THE_RESCORE.md` for what changed and why, and `…-v2/01_THE_TEN.md` for the set that replaces this
one.


Jordan's ask: the seven documents fall into three rough groups — **management**, **strategy** and
**emergence** — and each evaluates games against many axes. *Plot Valoria on every one, so we can see
what the game does for each design quality the suite interrogates.*

**How to read this.** Every cell is the value **the running tree** takes, cited at `file:line`, not
the value a design document claims for it (`CLAUDE.md` §0.05 — a `## Status:` line is reference, never
a mechanism). Where Valoria has **no value on an axis**, that is stated as *off-axis* rather than
forced to the nearest point, because the forcing is what would make this table lie. Where a carrier
exists with no producer, the cell reads **declared / unproduced**, which is the single most common
answer in this document and the finding of Parts A–D.

**One measurement is quoted throughout** and was taken this session on this tree:

```
build_world(0):        3 persons · 0 live `hold` tenures · stance [] · capability {} for all
86 corpus worlds:      258 persons · 3 distinct ids · 1 eligibility set · budget {5: 258}
opening_set:           177,170 candidates · 17,400 self-subject · 0 other-person subject
corpus_run:            11 of 38 verbs execute · 89 worlds → 25 distinct executed sets
                       degrees {Failure 386 · Partial 60 · Success 37 · Overwhelming 0}
```

---

# §1 · MANAGEMENT — the nine-titles axes

The later revision gives seven axes plus two cross-cutting disciplines; the earlier gives five. Both
are plotted; where they ask the same question differently, that is noted rather than collapsed.

## 1.1 · The seven axes

| # | axis | the suite's scale | **Valoria** | grounded at |
|---|---|---|---|---|
| **1** | **Population resolution** | individual → household → typed pool → fungible token → absent | **OFF-AXIS — declared at two resolutions, produced at neither.** `Rung.envelope` is band-indexed counts; `Person.weight` is *an acting crowd* (S9.1, "a cohort is a Person at weight > 1"). **Neither has a writer.** In the world the loop drives: 3 individual Persons, all at weight 1 | `state/carriers.py:368` · `:560` · `loop/census.py:33-36` (*"NO CLOCK GENERATES ANYTHING"*) |
| **2** | **Named-agent cardinality** | none → scarce & capped → many → unbounded | **Scarce — but by omission, not by cap.** 3 distinct ids across 86 worlds. The suite's "scarce" titles cap deliberately (KoH II's eight); Valoria's cast was never authored — `W27`, 0 of 143 cases carry one. **And no verb creates a Person** | measured; `loop/census.py:29-36` |
| **3** | **Contested object — what actually kills you** | labour / time / logistics / allegiance / legitimacy | ⚠ **NOTHING. A value no title in the suite occupies.** Subsistence is drawn every season and **a shortfall emits nothing and decides nothing** — L5: *"a threshold crossing MAY NEVER PRODUCE AN OUTCOME… Inventing starvation here would be the outcome L5 forbids."* The only death is `kill / wound` | `loop/matter.py:179-184` · `loop/effects.py:308-418` |
| **4** | **Player position** | administrator above ↔ embedded actor within | **Embedded, and more strongly than any title in the suite.** Not a stance but a prohibition: *"every character has the budget — the archive's asymmetric economy is REJECTED… precisely the player-only mechanism §07 §1 forbids"* | `architecture/PLAN.md:438` |
| **5** | **Control channel** | 1 direct order → 2 zone & auto-allocate → 3 delegate to a named agent → 4 lobby a body | **RUNG 1 ONLY.** Rung 2 **refused** (`AX-1` — a zone allocating persons is nobody deciding). Rung 3 **blocked** — `remit:` is unevaluable person-side (`H-71`) and `Act` carries no `via` (`H-108`), so delegation is unbuildable. Rung 4 **declines** — `convene` exists and its eligibility refuses person-side. The suite observes *"no game uses more than two adjacent rungs"*; **Valoria uses one** | `01_AXIOMS.md:71-74` · `decision/options.py:161-168` |
| **6** | **Coupling latency** | immediate / seasonal / shock-punctuated / lagged cohort | **All four occupied, by four different mechanisms.** **Immediate**: one *round* — `U2` runs DELIBERATE→RESOLVE→WITNESS five times a tick, and a claim deposited in round 0 can cause a deliberation in a later round of the same season. **Seasonal**: the three licensed world motions — matter, bodies, *the fading of memory* (a claim decays 5/season against 100, so ~20 seasons). **Shock**: death. **Lagged**: ⭐ **term maturation** — MATTER ripens an act-declared stage at a later tick and writes `Record.matured`, *"the only mechanism in the design by which one season's act reaches into a later one WITHOUT anybody acting again"*, and it **stops if the maker is gone**. ⚠ Two of these are rarer than anything in the suite: decaying belief as a licensed world motion, and a lag that is **an act ripening rather than a clock running** | `01_AXIOMS.md:151-165` · `loop/driver.py:361-401` · `loop/matter.py:55-109` · `data/fixtures.py:428-429` |
| **7** | **Durability and reset** | persistent / ephemeral wiped / ephemeral + carry-over | **Persistent, single campaign, no reset.** And the one irreversibility is absolute: `kill / wound` at *Felled* sets body 0, closes every Tenure naming the person, **and deletes them from the world** | `loop/effects.py:385-417` |

## 1.2 · The earlier revision's five axes, where they differ

| axis | **Valoria** |
|---|---|
| Individual-agent ↔ statistical abstraction | **Individual at the acting layer, absent at the governed layer.** Every actor is a `Person`; there is no modelled populace beneath them, because `Rung.envelope` has no writer |
| Player-as-god ↔ player-as-embedded-actor | Embedded — see 1.1 #4 |
| Direct control ↔ indirect influence | **Neither, in the suite's sense.** The player does not control others *or* influence them; they are one Person choosing their own acts. Indirection is not a design choice here, it is `AX-1` |
| Scarcity source | **None yet** — see 1.1 #3 |
| **How faction / loyalty is modelled** | ⚠ **By none of the suite's five patterns.** No bloc dominance, no mutually-exclusive approval, no influence-priced vote, no court manipulation, and not "environmental". A faction is *a Proposition plus `commit` edges* — a theorem of `AX-1` (`T-h`). **A faction never acts; the actor is always the person holding the office.** There is no loyalty scalar anywhere: `stance` is read by the scorer and written by nothing | `01_AXIOMS.md:237` · `rosters.yaml:853-855` · `decision/choose.py:83` |

---

# §2 · STRATEGY — the thirteen-games axes

## 2.1 · The seven axes

| # | axis | **Valoria** | grounded at |
|---|---|---|---|
| **I** | **Contested object: land ↔ allegiance** | **Allegiance, structurally** — R7 rules every aggregate a Query over `hold` and `commit` edges, so legitimacy, standing and influence are *derived from allegiance* and never stored. But nothing yet contests it: 0 live `hold` tenures | `design_rulings_2026-09-06.md:169-173` |
| **II** | **Player position: above ↔ inside** | **Inside, by prohibition** — as 1.1 #4 |
| **III** | **Control channel** | Rung 1 — as 1.1 #5. ⚠ The suite names *zone-and-auto-allocate* as the rung absent from all thirteen; Valoria **refuses** it on `AX-1`, which is a different thing from lacking it |
| **IV** | **Named-agent cardinality** | Scarce by omission — as 1.1 #2 |
| **V** | **Coupling latency** | Three licensed motions — as 1.1 #6 |
| **VI** | **Durability** | Persistent — as 1.1 #7 |
| **VII** | **Clock count** | ⚠ **ONE TICK, TWO GRANULARITIES — and a second unjoined WORLD.** `w.tick` advances **once** per season while five rounds of DELIBERATE → RESOLVE → WITNESS run inside it, so the scene round is not a clock. But `engine/mc_v18.py` runs a complete independent season loop and `engine/season/` never imports it — *"the two are not joined"* | `loop/driver.py:356-405` · `requirements.yaml` R-04 |

**The axis the suite says will not support one.** It declines to make *population resolution* an axis
for the thirteen because eleven sit at the same value. **Valoria sits at a twelfth value:** declared
twice, produced never.

## 2.2 · The eight primitive families (later) and seven clusters (earlier)

| family / cluster | **what Valoria has** |
|---|---|
| **A · Political currency & resolution bodies** | **No political currency exists.** No spendable stock; R7 forbids the carrier. The nearest throttle is the **act economy** — 5 scene-actions per person per season, +1 per live office hold, −1 per body-band or travel-leg crossed, floor 1. Measured: **5 for all 258 persons**, because offices are 0 and the only writer of `body` is death |
| **B · Loyalty, opinion & defection** | Carriers without producers: `stance` (read, unwritten), `convictions` (13, projected onto 4 axes, **correlated** — 9 of 13 within 60° of the mean). No defection cost: `release` is taken 164 times, closes 6 edges, refuses 158, and `requires_typed: none` means no belief can make walking away harder |
| **C · Personnel scarcity & delegation** | **The whole family is unreachable.** Ten of 38 verbs can never be offered to anybody, and they are exactly the governance slice (`H-71`, `H-33`, `H-75`). `confer` has an effect and declines person-side |
| **D · Spatial control** | `contain` gives the eight-rung ladder person→hearth→community→settlement→territory→province→duchy→realm. No painting, no fill-to-own, no claims. `Site.condition` is a **one-directional ratchet** — wear lowers it every season and `work` does not restore it (`H-105`) |
| **E · Relational control & scoring** | **No score and no ending.** Every member of this family needs one |
| **F · Action & turn economy** | Shipped and **flat** — see family A. The suite calls a character-derived, decaying action budget *"family F's most under-used idea"*; Valoria shipped it first and left it constant |
| **G · Advancement & goal generation** | **Ambition exists and is not a field:** a `commit` Tenure to an OUGHT Proposition, read by Q4 `need` as a standing question every season. That *is* the ambition mechanism. What is missing is a **deadline** (the question never forces) and an `ambitions(p)` read |
| **H · Durability, reset & legibility** | Persistent; no reset; and legibility is ruled the *opposite* way to the suite's assumption — §C.11: *"The engine owes the ARITHMETIC of what the character already holds, and nothing else"* |

---

# §3 · EMERGENCE — the compendium and the mechanical specification

## 3.1 · The four sets

| set | **Valoria** |
|---|---|
| **A · Generative substrate** (interacting rules, agents, shaped randomness, scale, constraint) | **Present.** `EFFECTS` × `requires_typed` × `witness` × `questions_for` is a genuine non-enumerable interaction. Randomness is **unshaped and refused shaping** — every draw is keyed `H(seed, tick, subject, purpose)`, *"no counter, no service"*, so PRD needs a stream Valoria has structurally declined |
| **B · Attribution & stakes** (intentional legibility, memory, control mode, irreversibility) | **Half.** Memory: `ledger` + `beliefs`. Irreversibility: death. **Attribution fails** — the gap between intent and outcome exists (`_sample_order`'s Gumbel) and is attributable to **the draw, not the person**; `requirements.yaml` R-08 says so in its own words |
| **C · Structuring units** (storylets, pacing) | **Storylets yes, pacing refused.** A verb row *is* a storylet — content + prerequisites + effects, 38 rows, with a loader that refuses an unlisted `writes:`. Every pacing mechanism in the suite is refused: `T-b` (a threshold may never produce an outcome), `AX-5` (no fourth clock), and ED-IN-0011 (the director is ratified **subtract-only**) |
| **D · Discourse** (surfacing, curation, retelling) | ⚠ **The weakest set, and the substrate is the best-prepared for it.** Every write carries `causes=[…]` and every Event carries `causes: list[str]`, so the why-chain is populated — **and no render exists.** Curation is refused on salience by comparator signature; a claim leaving a ledger **emits nothing**, so nobody can witness a forgetting |

## 3.2 · The four control parameters *(VII.1 — the suite's densest axis)*

| parameter | the suite's range | **Valoria** |
|---|---|---|
| **Granularity** | single action → policy | **The scene.** 5 per person per season, 1–3 interactions each; the person triages against a budget they asked for, and the engine never truncates |
| **Compliance** | 1.0 → ~0 | **< 1.0, and this is the design's sharpest near-miss.** `_sample_order` is Plackett–Luce via Gumbel at `softmax(score/0.1)`, so the top-ranked act is likely and not certain. **But the shortfall is not a person's** — R8: *"a tie is now broken by the DRAW, which is not the person — it is the absence of a reason, not a reason of theirs."* The suite's VII.2 condition — *the gap must be attributable to an agent* — **fails here** |
| **Latency** | 0 → months | **Two values, and the ruling naming one is recorded as unreconciled.** Claim-driven reaction is **one round**: `U2` runs five DELIBERATE→RESOLVE→WITNESS passes a tick and `questions_for(…, since=(tick, round))` selects *since I last deliberated*. The world's own motions are **one season**. The chain's *"no within-season reaction at person scale"* is logged as unreconciled with S40.2 at `harness/probes.py:1953` | `loop/driver.py:361-401` · `queries/world_q.py:211-214` |
| **Observability** | full → fogged and unreliable | ⚠ **Beyond the suite's scale. Not fogged — ABSENT.** `AX-2`: there is no view of world truth inside a decision, *"not capped, not filtered: absent."* `choose` receives no World, enforced by test; a `View` is capped at k and raises on any world collection. And `LedgerReader` returns the **stored** value, most-recent-then-most-confident — so **stale information is the default read**, which the suite calls the rarest and most potent epistemic mechanic |

## 3.3 · The eight persistence types *(VI.1)*

| type | **Valoria** |
|---|---|
| Moodlet (scalar + timer) | **absent** |
| Memory (indexed record) | **produced** — `Person.ledger`, decaying, evicted at 200 |
| Relationship (dyadic, often asymmetric) | **declared, unproduced** — `tie`/`knot` are tenure kinds with verb rows and **no effect**. Layer 1 rules the shape **two directed edges, each owned by its subject** |
| Reputation (public, visible to third parties) | **declared, degenerate** — `standing_of` returns `condition_scale` for every person in every world |
| Disposition weight (a rewritten distribution) | **matrix-only** — `(Person, axis_count)` is a `write_matrix.yaml:148` row and **`Person` has no `axis_count` field** (`carriers.py:364-396`). Weaker than declared |
| Scar (irreversible flag) | **matrix-only** — `(Person, scar)` at `write_matrix.yaml:197`; no such field either |
| Chronicle (append-only ordered log) | **produced, unbounded** — `World.log` is a bare list, never trimmed |
| Artifact (object carrying provenance) | **produced in part** — `Record` exists with stages that mature; `forgery_quality` is never written, and the `Record.ttl` → `record.expired` row (`write_matrix.yaml:273-279`) has no code in `matter.py`, so the artifact has **no lifespan of its own** |

**Three produced, two declared, two matrix-only, one absent.** The column's shape, not a ratio: **the
irreversible and the accumulating types are the ones with no field at all**, while the two that run
are the two that only ever append. `matrix_rows_without_a_field()` exists to report precisely the
matrix-only state, which is why it is worth distinguishing from *declared*.

## 3.4 · The scale ladder *(VII.3)*

character → party → **settlement** → **faction** → nation → civilization

**Valoria runs person, settlement and realm.** The faction scale is where 44 of the 54 unrepresentable
cases sit, and it runs in **a different engine the loop does not import**. The eight cross-scale
handoff rules the corpus specifies — Personal→Thread, Personal→Faction, Scene→Faction and five more —
**the loop implements none of them**, and their spec lives in a tree ED-IN-0204 marked not-retained.

## 3.5 · The fourteen requirements and the minimum machine

| | | |
|---|---|---|
| **Carried and produced** | 1 interacting systems · 4 permanent state · 10 epistemic gap · 12 curation *(partly — bounded and ordered live in two different objects, neither both)* |
| **Carried in schema, unproduced** | 2 attributable agents · 5 disposition rewriting |
| **Refused structurally** | 6 shaped randomness (keyed draws) · 8 escalation coupled to success (no economy) · 9 **visible clocks** (*"never a meter… no quantized horizon ever surfaces"*, ratified) |
| **Half** | 3 withheld authorship · 11 surfacing that names causes |
| **Unreachable on the current ladder** | 7 complication-modal resolution — **19% against the 41–45% the suite measures**, and `OVERWHELMING` is *mathematically unreachable* at the shipped fixtures |
| **Open and Jordan's** | 13 perceptually load-bearing variety — `ED-IN-0214` |
| **Absent entirely** | 14 a retelling artifact — no render exists |

**The six-item minimum machine:** ≥2 interacting systems **yes** · agents whose state explains their
behaviour **no** (`H-62`) · compliance < 1.0 attributable to that state **half** · permanent state
**yes** · randomness with memory **no, and refused** · surfacing that names causes **half**.

> **Item 3 is the suite's own nomination for the most-often-missing item, and it is the one Valoria
> misses.** Two documents and one acceptance file, written independently, name the same absent object.

---

# §4 · THE TWO CROSS-CUTTING DISCIPLINES

**Clock count.** One tick, two granularities — and the second granularity was **bought with a measured
control**, which is the discipline the suite asks for and none of its eighteen proposals performed:
R-03's flip rests on an execution against a `scene_budget = 1` arm that reproduces the pre-tick act
multiset exactly, with the price reported and not netted off.

**Legibility strategy — the fiction wrap.** ⚠ **Structurally inapplicable, and this is the most
interesting cell in the document.** The suite rates *"name the loss timer 'the Queen'"* the best
cost-to-value ratio in its entire catalogue. Valoria **has no authorless hostile quantity to name**:
`AX-5` licenses exactly three world motions and `T-c` refuses a fourth, because *"a quantity that
advances on its own with no author is a shadow actor."* **Valoria's antagonists are persons.** The
wrap exists to make a system feel like an agent; Valoria's systems are agents, so the trick has
nothing to do.

---

# §5 · WHAT THE PLOT SHOWS

**5.1 · Valoria is not a point in the suite's space.** On five axes it takes a value the suite's scale
does not carry:

| | |
|---|---|
| **Contested object** | **nothing kills you.** All thirty-three titles die of something |
| **Observability** | **absent, not fogged.** The scale runs full → unreliable; Valoria is off its end |
| **Control channel** | **one rung**, where the suite observes that no title uses fewer than two |
| **Population resolution** | **declared twice, produced never** — a twelfth value on an axis the suite declined to draw |
| **Fiction wrap** | **inapplicable by construction**, not merely absent |

**5.2 · Three of the five off-scale values are rulings; two are gaps. The distinction is the point.**

| off-scale value | ruling or gap | which |
|---|---|---|
| Observability absent | **ruling** | `AX-2` — world truth is absent inside a decision, by type |
| Fiction wrap inapplicable | **ruling** | a consequence of `AX-1` |
| Control channel at one rung | **ruling** for rung 2 (`AX-1`); **gap** for rungs 3–4 (`H-71`, `H-108`) |
| Contested object nothing | **gap** | `H-11`'s subsistence is written and unacted-on |
| Population resolution produced never | **gap** | `Rung.envelope` has no writer |

**The rulings share a direction** — *the player has less authority, and the world has fewer levers,
than any title in the corpus*: only a person acts, no magnitude is pushed, no threshold produces an
outcome, world truth is absent inside a decision. **The gaps share a different one**: a carrier exists
and nothing writes it. **Reading the two as one direction would flatter the design by dressing an
unbuilt consequence as a deliberate restraint**, and it is the error this table exists to prevent.

⚠ **And one thing the design does rank, contrary to the tidier version of this claim.** Questions are
ordered before a budget-bounded person answers them: across sources by `rosters.yaml`'s
`question_sources` order, *whose own note calls that order **semantic***, and within a source by
lexicographic order over content hashes — measured to decide `qs[0]` in **801 of 1,068
deliberations** (`queries/world_q.py:250-269`, `H-54`). What is refused is ranking a *memory* by
importance (§R); ranking a *question* is shipped, and its within-source half is **undeclared**, which
is a live hole rather than a design property.

**What Parts A–D found, with the counts as they reconcile there:** **27 false N-lines** per distinct
object (30 per instance) and **nine distinct ratified lines**, against **two transferable ideas** and
**three survivors** (§7.4). `04_CONSOLIDATION.md` §4.2 carries the tally and its counting convention.

**5.3 · Where Valoria is ahead of the corpus — three cells, and they are not the ones a reader expects.**

1. **Stale information as the *default* read.** The suite calls this rarer than fog of war and says it
   does strictly more narrative work. `LedgerReader` returns the last-observed value, never world
   truth, with the rationale written at the site.
2. **Belief with provenance.** The suite finds it in **2 of 33 titles** and grades it *"most likely to
   fail in practice."* `Claim` carries `source`, `confidence` and `when` by construction. What it
   lacks is a *speaker* in `source` — one argument (Part B `P3`).
3. **A graduated agent layer with a refusing loader — on one dial.** The suite's most actionable
   lesson, drawn from three shipped failures, is *specify the half-strength setting*. `fan_out_mode`
   is exactly that: three declared arms, and `observers_for` **refuses an unrecognised mode**
   (`epistemic.py:404-409`), the property all three failures lacked. ⚠ `choice_temperature` is **not**
   a second instance — `Fixtures.get` refuses an unregistered *name*, never an out-of-sweep *value*,
   and its control arm is disputed between `choose.py:141-147` and `hole_register.yaml:1278`
   (Part B `M4`).

**5.4 · Two objects stand behind most of what reads unproduced.** The cells that read *declared /
unproduced* or *matrix-only* are not that many separate problems. `stance`, the relationship edge,
reputation, the two matrix-only persistence types, compliance's attribution, requirement 2 and
minimum-machine item 3 all resolve behind the same pair: **a person-referent route into DELIBERATE**
(Part B `P1`) and **a verb that writes an interior** (`H-62`/`W-F`). Three ABSENT rows — `B5` poaching,
`C3` delegate-as-defection-vector, and opinion diffusion — resolve behind `P1` alone, which is a
consequence worth stating plainly: **one clause moves three primitives from ABSENT to reachable.**
Everything else in this document is produced, refused by a ratified line, or Jordan's.

---

## §6 · WHAT THIS PLOT DOES NOT ESTABLISH

**`[SELF-AUTHORED — bias risk]`** — this part plots the tree using ground Parts A–D established.

**The method limit that bounds every cell.** The suite's axes were built to *discriminate among shipped
games*. Valoria is not shipped, and on any axis whose scale presumes a running game, *off-axis* and
*not yet built* are indistinguishable from outside. Where a cell reads **declared / unproduced** or
**matrix-only** it means exactly that, and not that the design has chosen a value.

**Two denominators are in play and each cell inherits one.** The corpus has **86** buildable worlds and
**89** live ones (`engine/season/requirements.yaml:395`, `:407`). Per-person figures use 86 —
`258 = 86 × 3` — and per-run verb figures use 89. A cell comparing one against the other would be
comparing two experiments.

**Two engines run, and a cell's value can differ between them.** `engine/season/` is the loop; the
`engine/mc_v18.py` side reaches a parliamentary vote and declares a `victory` module
(`references/module_contracts.yaml:1078`). Every cell here is scored on **`engine/season/`** unless it
says otherwise; `M3` in Part B carries the disagreement between the two as a measurement.

**One figure in §3.5 is analytic, not measured.** The 19% Partial is computed exactly at
`pool_default = 2` against `obstacle_default = 2`; the corpus *measured* 12.4% (`Partial 60` of 483
degrees). Both are true of different quantities — the analytic figure is the per-contest probability at
the default pair, the measured one the realised mix over whatever pairs arose — and comparing either to
the suite's 41–45% band is comparing to a third thing again.

**Not re-measured here.** Every figure was measured earlier in this session at the instrument cited.
⚠ **One triple has no instrument in the tree**: `release`'s `164 taken · 6 closed · 158 refused` was
produced by a one-off script, and `requirements.yaml:351-360` says so itself.

# §7 · THE PRIMITIVE LEDGER — every catalogued mechanic in the suite, scored

§1–§4 plot Valoria on the **axes**. This section goes to the granularity the suite actually
catalogues at: **every primitive, cluster and set**. The verdict vocabulary is fixed, and the
distinctions in it are the point:

| verdict | means | the test that separates it from its neighbour |
|---|---|---|
| **PRODUCED** | a writer exists and the verb reaches the fold | it appears in `EFFECTS` (or writes nothing and contests), and `resolvable_verbs()` admits it |
| **PRODUCED, UNREACHED** | the effect is implemented; no candidate ever forms for it | the effect body exists, and the measured count is 0 |
| **DECLARED / UNPRODUCED** | the **carrier** exists — a dataclass field — and nothing writes it | the field is in `carriers.py`; no `EFFECTS` body writes it |
| **MATRIX-ONLY** | a `write_matrix.yaml` row names a field that **does not exist** | `matrix_rows_without_a_field()` (`carriers.py:591-624`) reports it. Weaker than DECLARED |
| **REFUSED** | a **design commitment** refuses what the mechanic *does* | the line is quoted, it is Jordan's or a theorem from one, and it refuses *this* object rather than an adjacent one |
| **REFUSED AS STORED — DERIVED FORM RULED IN** | `R7`/`L3` refuse the **stock**, and R7's next clause admits the same quantity as a **Query** | the distinction is R7's own: *"holdings count and military capacity and influence are **Queries over `hold` and `commit` edges**"* |

⚠ **The second row exists because the first was over-applied, and the correction runs one way: toward
the design being MORE open than these tables first said.** A ratified line that refuses a *stored
magnitude* has not refused the *idea* — `01_THE_PASSES.md` §4 sets this out with each refusal's grounds
marked **D** (a design commitment, Jordan's to revise), **T** (a theorem from one) or **I** (an
implementation fact, which is **never** a refusal). Where a row below reads *refused as stored*, the
derived form is a live proposal and not a closed question.
| **FALSE N-LINE** | the claimed possibility survives the cut, because something ruled in already provides it | per `skills/ners/SKILL.md` §3 — *something already ruled in provides it*. An object nothing provides is ABSENT, not a false N-line |
| **ABSENT** | no carrier, no writer, and no line refusing one | — |
| **PAPER** | already proposed in a prior set and graded `paper` | — |

⚠ **Eight terms rather than six, and the two additions earn their place by being checkable.**
`PRODUCED, UNREACHED` separates *the code is missing* from *the question never asks* — the difference
between work and a grammar gap, and the single most common confusion in this tree. `MATRIX-ONLY`
separates a field with no writer from **a row naming no field**, a state the tree instruments itself.

**The counting rule, stated so §7.4 is reproducible.** Each row is counted **once**, under the
**first** verdict it names. A row that reads *"as B1"* is a cross-reference and is **not** counted
again. A row whose verdict is a conjunction (*"X in prose, Y in code"*) counts under the code half,
since §0.05 makes the code the mechanism. Rows scoring something *beyond the suite's scale* are
counted under the verdict they take, with the out-of-scale note kept as a note.

## 7.1 · The strategy corpus — 41 primitives in eight families

### A · Political currency and resolution bodies

| | primitive | verdict |
|---|---|---|
| A1 | spendable political currency | **REFUSED AS STORED — DERIVED FORM RULED IN.** The stock is a magnitude carrier (R7); R7's next clause makes influence *"a Query over `hold` and `commit` edges"*, which is this primitive without the stock. Same treatment as `A2` |
| A2 | currency whose *supply* is a loyalty function | **REFUSED as a carrier; the shape is ruled in** — R7 makes influence a Query over `hold`/`commit` edges, which is A2's shape without the stock |
| A3 | currency that is also the victory condition | **TWO GROUNDS, AND ONLY ONE IS A REFUSAL.** A stored campaign aggregate is refused by R7 (**D**); *"no score exists"* is an implementation fact (**I**) and refuses nothing. A derived victory Query is not refused by any line quoted here |
| A4 | approval slope with a punitive tail | **SPLIT.** The slope is **refused as stored, ruled in as derived** (R7); the tail is **REFUSED** on `T-b` — a threshold producing an outcome. So a derived approval Query whose crossing raises a **Question** is the lawful whole of this primitive |
| A5 | vote as the resolution mechanism | **FALSE N-LINE** — it executes, in `parliamentary_vote.py` (d10 pool, TN 7), reached from `mc_v18` and tested. ⚠ In the *unjoined* engine |
| A6 | asymmetry balanced by auction | **ABSENT** — nothing refuses it; it bears on none of the nine requirements |

### B · Loyalty, opinion and defection

| | primitive | verdict |
|---|---|---|
| B1 | opinion as a modifier-stacked scalar | **DECLARED / UNPRODUCED** — `Person.stance`, read by the live scorer, written by nothing (`H-62`) |
| B2 | punished allegiance-switching | **FALSE N-LINE in prose, ABSENT in code** — `faction_politics_v30.md` rules it harder (defection = 2–3 ranks, Dishonored flag, mentors voided) and **no code reads that ladder**. `release` costs nothing: 164 taken, 158 refused, `requires_typed: none` |
| B3 | kinship as a permanent loyalty lock | **DECLARED / UNPRODUCED** — `tie`/`knot` are tenure kinds with verb rows and no effect |
| B4 | power base — usefulness and threat as one number | **REFUSED as a number; ruled in as a Query** — R7 names power base a Query over edges, so it cannot desync and cannot be gerrymandered |
| B5 | poaching with a priced entry condition | **ABSENT** — requires a candidate directed at another person, which no question source produces |
| B6 | shock-punctuated loyalty | **PRODUCED, narrowly** — death closes every Tenure naming the person, the one shock the tree ships |
| B7 | hidden loyalty with no indirect channel | **REFUSED, and the tree is stricter** — `AX-2` makes world truth *absent* inside a decision, and §C.11 obliges the engine to explain what the character already holds. The suite catalogues B7 as a negative result; Valoria refuses the negative result too |

### C · Personnel scarcity and delegation

| | primitive | verdict |
|---|---|---|
| C1 | hard-capped named agents | **ABSENT.** Nothing provides a cap and nothing refuses one: `AX-5` governs world motions and R7 governs magnitude carriers, neither cast size. `census.py:29-36` generates nobody and **no verb creates a Person**, so the cast is fixed at world-build by a missing producer — `(Person, exists)`'s CEN row with no writer. Scarce **by omission**, which is not a cap |
| C2 | delegate with a stipend and stat-proportional output | **DECLARED / UNREACHABLE** — `confer` has an effect; `remit:confer` declines person-side (`H-71`) |
| C3 | delegate as defection vector | **ABSENT** — needs both a seat and a person-directed act |
| C4 | class differentiation by assignment | **DECLARED** — `Office.remit_acts` is a closed six-act roster; 0 offices held |
| C5 | contract personnel with expiry | **REFUSED, verbatim** — `T-n`: an end nobody declared is a clock nobody wound. ⚠ **And licensed in the lawful form:** *"the opening act declares the terms"* |
| C6 | recruitment as a negotiation sub-game | **ABSENT** — no verb creates a Person |
| C7 | background as a small permanent modifier at hire | **DECLARED / UNPRODUCED** — `Person.marks` exists; **nothing writes it** |

### D · Spatial control

| | primitive | verdict |
|---|---|---|
| D1 | tile painting with severable supply | **REFUSED AS STORED** — a painted colour is a stored aggregate on a Rung (L3). Control derived from live `hold` edges over the containment forest is the same primitive without the field |
| D2 | fill-to-own province nodes | **ABSENT** — `contain` gives an eight-rung ladder, not ownership by completion |
| D3 | site selection as a durable decision | **DECLARED / UNPRODUCED** — `(Rung, exists)` and `(Site, exists)` are `[RES]` rows emitting `rung.founded`, **with no producing verb**. R4 names four routes to churn; all unbuilt |
| D4 | claim / casus belli as a legal gate | **ABSENT** |
| D5 | bidirectional cascade between two subsystems | **PRODUCED AND STRONGER** — `_eff_kill` writes body, existence and every naming Tenure in one effect, so a death propagates into the office ladder |

### E · Relational control and scoring

| | primitive | verdict |
|---|---|---|
| E1 | dominance with a gap condition | **REFUSED AS STORED** — the gap needs a score, and a score may be a **Query**. `standing_of` is precisely a gap computed rather than stored (`options.py:444-465`), so the shape is already in the tree |
| E2 | two scoring modes rewarding opposite investments | **REFUSED BY COMPOSITION** — the suite's own "most portable single rule"; it needs a scored event and R7 forbids the aggregate. Closes at `CLAUDE.md` §0 gate 5, not as a ruling request |
| E3 | status that gravitates to the centre | **REFUSED — on `L3`/R7, not `AX-3`.** There is no status to gravitate: standing is a **Query** (`design_rulings:172-174`) and `carriers.py:579,586` forbid storing one. `AX-3`'s carve-out governs claim *confidence*, a different quantity |
| E4 | rented rather than owned position | **PARTLY PRODUCED** — an office is not owned; it is a `hold` Tenure with cardinality 1, and `Query.hold_force` **raises** on a second live hold |

### F · Action and turn economy

| | primitive | verdict |
|---|---|---|
| F1 | action-point budget | **PRODUCED** — `budget()`: base 5 + office bonus − body-band − travel-leg, floor 1 |
| F2 | budget derived from a character, decaying with age | **PRODUCED IN SHAPE, FLAT IN VALUE** — the same function; measured **5 for all 258 persons**. Offices are 0, and `body` is written only by `kill / wound` — which includes a *Wounded* branch that leaves the person alive (`effects.py:402`), so the flatness is not "death is the only writer" but that **`kill / wound` never folds in the corpus**: `resolvable_verbs()`' third gate excludes a contested verb whose `subject` operand cannot be bound (`driver.py:100-119`, `H-80`). The suite calls this *"family F's most under-used idea"*; Valoria shipped it first and left it constant |
| F3 | strict phase order with a periodic extra phase | **PRODUCED for the order; the extra phase is REFUSED only if UNWOUND** — six steps in fixed order. A phase recurring on a hazard nobody set is `AX-5`; a phase convened by a nameable act is `T-c`-licensed, and the tree ships that shape as a `convene`d `Date` |
| F4 | two clocks | **REFUSED at person scale, PRESENT as two unjoined worlds** — one tick, two granularities; and `mc_v18` |

### G · Advancement and goal generation

| | primitive | verdict |
|---|---|---|
| G1 | use-based progression with gated learning | **ABSENT** — `Person.capability` has one writer and it zeroes |
| G2 | character-selected ambitions | **FALSE N-LINE** — a `commit` Tenure to an OUGHT Proposition, read by Q4 `need` as a standing question every season. *That is* the ambition mechanism |
| G3 | trait-driven AI goal selection | **PRODUCED, and correlated** — 13 convictions projected onto 4 axes; 9 of 13 within 60° of the mean; distinct executed sets fell 40 → 27. `ED-IN-0214`, Jordan's |
| G4 | event-driven ambition **with a deadline** | ⚠ **THE SURVIVOR OF THIS FAMILY.** Q4 produces a *standing* question with no horizon — the same question forever, never forced. A **term** on the `commit`, licensed by `T-n`, is the missing half |

### H · Durability, reset and legibility

| | primitive | verdict |
|---|---|---|
| H1 | board wipe after a scoring event | **REFUSED** — unauthored state change |
| H2 | fixed-term structure | **ABSENT** — no ending; `ENDINGS_CLASSIFIED.yaml` classifies prose and says so |
| H3 | split visible and hidden state | **HALF PRODUCED, HALF DECLARED.** *Produced and beyond the scale*: `AX-2` makes world truth **absent** rather than hidden, and §C.11 obliges only the arithmetic the character holds. *Declared*: the forgery half — `forge` declares `Record.forgery_quality` and has **no `EFFECTS` entry**, so it never folds and that field is never written; `destroy_record` folds but `H-75` records it *"CANNOT FIRE FOR ANY ACTOR"*. Counted under **DECLARED / UNPRODUCED** |
| H4 | rule-bound automaton opposition | **FALSE N-LINE** — every character runs the same `choose`; `View.__getattr__` raises on any world reach, so *cannot cheat* is structural **by type**, stronger than by rulebook |

## 7.2 · The management corpus — the consolidated catalogue

### Demographic — the family the strategy corpus lacks entirely

| primitive | verdict |
|---|---|
| ageing cohort | **PAPER** (2026-09-10) — `Rung.envelope` is the carrier, zero writers |
| temporary withdrawal from the labour force | **DECLARED / UNPRODUCED, not refused** — the step exists. MATTER matures act-declared terms (`matter.py:55-109`) and that is the lawful form an act-wound withdrawal would take, consistent with `C5`. What is missing is the carrier: maturation is implemented for `Record` stages, and `Tenure` has no `term` field (`verb_table.yaml:421`) |
| housing as the reproduction gate | **OPEN ESCALATION** — `ED-SE-0051`, matter-only vs matter-plus-hearth-capacity. *"Materially different games."* Jordan's |
| threshold immigration on standing | **SPLIT** — the stored settlement aggregate is **refused as stored**; the *threshold producing the migration* is **REFUSED** on `T-b`. A derived standing Query whose crossing raises a Question is lawful |
| inherited statistics | **ABSENT** — no verb creates a Person |

### Loyalty, opinion and belief

| primitive | verdict |
|---|---|
| opinion as a modifier-stacked scalar | **DECLARED / UNPRODUCED** — as B1 |
| punished loyalty-switching | as B2 |
| mutually exclusive faction demands | **EXPRESSIBLE, UNBUILT** — two OUGHT Propositions; `utter` executes, `commit` does not |
| **opinion diffusion within a population** | **ABSENT AND BLOCKED** — needs a belief about a person to reach a person; 0 of 177,170 candidates carry another person as subject |
| **fabricable evidence with a lifespan** | ⚠ **THE CLOSEST MATCH IN THE SUITE.** `Claim` carries `source`, `confidence`, `when`; confidence decays at MATTER; `forge` writes `Record.forgery_quality` and `destroy_record` exists. **Missing two arguments at one call site** — a speaker in `source` (`P3`) and the told content in `predicate`/`value` (`P6`) |
| **a rumour that is false, and attenuates as it spreads** | ⚠ **SURVIVOR.** `tell` requires the teller to hold a claim (`verb_table.yaml:499`) and the deposit discards it: `predicate = e.kind`, `value = True`, `confidence = confidence_default` (`witness.py:137`). Decay is a function of **age** and never of **transmission**, so third-hand arrives as confident as an eyewitness. Probes `P4` and `P16` hand-build the claims this would produce and are graded `by="construction"` |
| loyalty decay on a shock | as B6 |

### How pressure is arranged

| primitive | verdict |
|---|---|
| **inverse-linked meter triangle** | **REFUSED AS STORED, AND THE INVERSE LINKAGE IS THE PART WITH NO OBSTACLE.** Three *stored* global meters are refused (`carriers.py:579`, `:586`, R7). ⚠ Three **Queries** whose inputs overlap are inverse-linked by construction and store nothing — so the suite's *"most sophisticated pressure design"* is refused in its bookkeeping and **not** in its mechanism. An earlier revision of this row called it *"the tree's most comprehensive refusal"*, which mistook a storage rule for a design one |
| one dominant killer, everything routed into it | **FUNNEL PRODUCED, TERMINAL REFUSED** — every act discharges into `Rung.stores` and every person draws from it; **the shortfall emits nothing and decides nothing** |
| twin-population tension | **REFUSED AS STORED** — two stored aggregates. Two population Queries are not refused by any line quoted here; what is genuinely missing is a producer for either (`Rung.envelope` has no writer) |
| action-point budget | as F1 |

### Space, logistics and control

| primitive | verdict |
|---|---|
| **work areas with worker caps / auto-allocation** | **REFUSED** — `AX-1`: a zone allocating persons is nobody deciding |
| per-commodity targets as ratios to population | **REFUSED** — same rule, plus no population figure |
| organic plot growth along drawn roads | **ABSENT** |
| physical haulage with no teleporting storage | **PARTLY PRODUCED** — `_eff_transfer` is a two-sided store write that conserves matter and refuses a non-Rung side. Missing: a distance term. `travel_leg` is the precedent |
| range-limited seasonal work | **PARTLY PRODUCED** — `_eff_move` writes `travel_leg`; `budget` charges per leg. **Distance already prices acts.** Missing: season and mortality |

### Advancement, reset and progression

| primitive | verdict |
|---|---|
| skill by doing → mood → output (the double reinforcement) | **ABSENT** — no satisfaction field; `capability` zeroed |
| run plus meta-progression | **INAPPLICABLE** — one persistent campaign |
| **fiction wrapped around a hostile system** | **INAPPLICABLE BY CONSTRUCTION** — no authorless hostile quantity exists to name. See §4 |
| a rule-bound automaton paying every cost | as H4 |

## 7.3 · The emergence corpus — the fourteen primitives in four sets

| set | # | primitive | verdict |
|---|---|---|---|
| **A** | 1 | interacting simple rules | **PRODUCED** |
| A | 2 | agents with modelled internal state | **DECLARED / UNPRODUCED** — six `Person` interior rows, no producing verb (`H-62`) |
| A | 5 | randomness, shaped | **REFUSED** — keyed draws `H(seed, tick, subject, purpose)`, *"no counter, no service"*; PRD needs a stream |
| A | 7 | scale of representation | **PARTLY PRODUCED** — person, settlement, realm; faction unjoined |
| A | 8 | constraint / scarcity / friction | **PRODUCED** — the act budget, the ledger cap, `View` capped at k |
| **B** | 3 | attribution surface | ⚠ **HALF — the design's sharpest near-miss.** Compliance < 1.0 exists; the shortfall is the draw's, not the person's |
| B | 4 | persistent accumulating state | **PRODUCED** — ledger, Records, the log, death |
| B | 6 | control mode withholding authorship | **PRODUCED AND BEYOND THE SCALE** — `AX-2` |
| B | 9 | irreversibility / stakes | **PRODUCED** — death deletes |
| **C** | 10 | storylet units with preconditions | **FALSE N-LINE** — a verb row *is* one: 38 rows, fold = eligibility → `requires` → `writes` → `emits`, loader refuses an unlisted write |
| C | 11 | pacing / drama management | **REFUSED IN ITS PUSHED FORM ONLY.** `T-b` refuses a threshold that *produces* an outcome, `AX-5` a motion nobody wound, ED-IN-0011 a director that *adds*. ⚠ Each names a lawful sibling that is shipped or licensed: a band crossing **raises a Question** (`matter.py:260-277` → `world_q.py:234-238`), a clock **wound by `convene`** has handles, and a **subtract-only** director was ratified. Pacing is refused as something done *to* the player, not as a concern |
| **D** | 12 | surfacing / legibility | ⚠ **SUBSTRATE READY, NO RENDER.** Every write carries `causes=[…]`; nothing reads it out |
| D | 13 | curation / sifting | **REFUSED FOR MEMORY RETENTION, NOT FOR SELECTION.** The ledger comparator takes `confidence` and `recency` *and nothing else*, structurally (`04_CODE_ARCHITECTURE.md:972` row 39) — ranking a **memory** by importance is the refusal. ⚠ Ranking a **question** is shipped: `question_sources` order is called *semantic* by its own roster and decides `qs[0]` in 801 of 1,068 deliberations (`world_q.py:250-269`). Separately, **a forgetting emits nothing**, so it cannot be witnessed — an **I**, not a refusal |
| D | 14 | retelling / discourse | **ABSENT** — no render, no artifact |

**Set D is the weakest and its substrate is the best-prepared.** That is the single most actionable
line in this ledger, and it is not a proposal in Part B because a render is not one object.

## 7.4 · The ledger, counted — and how to reproduce the count

**80 rows across §7.1–7.3.** Four are cross-references (*"as B1"*, *"as B2"*, *"as B6"*, *"as F1"*) and
are not counted twice. The remaining **76** are counted once each, under the **first** verdict the cell
names, per §7's counting rule:

| verdict | count | where the weight sits |
|---|---|---|
| **REFUSED** by a ratified line | **21** | eight of the nine lines in `04_CONSOLIDATION.md` §4.2 |
| **PRODUCED** | **17** | incl. two *beyond the suite's scale* and one *substrate ready, no render* |
| **ABSENT** — no carrier, no writer, nothing refusing one | **14** | three of them behind `P1` alone |
| **DECLARED / UNPRODUCED** — the carrier exists, nothing writes it | **9** | |
| **FALSE N-LINE** | **5** | `A5` · `B2` · `G2` · `H4` · `C10` |
| **SURVIVORS** — catalogued, wanted, and lawful | **3** | `G4`'s term · a speaker in `Claim.source` · a false, attenuating rumour |
| **HALF** — a split verdict, counted under its code half | **2** | `F3` · `F4` |
| **INAPPLICABLE** — the axis does not apply to a single persistent campaign | **2** | |
| **PAPER** / open escalation / Jordan's | **2** | the ageing cohort · housing (`ED-SE-0051`) |
| **EXPRESSIBLE, UNBUILT** | **1** | |
| | **76** | |

`MATRIX-ONLY` scores **0** here and **2** in §3.3 — the two rows whose field does not exist are
persistence types, not catalogued primitives.

⚠ **`C1` moved out of FALSE N-LINE during this pass and the move is instructive.** A hard cap on named
agents looked refused-by-something-better, since `AX-5` and R7 both point away from stipulated
quantities. Neither speaks to cast size. `skills/ners/SKILL.md` §3 defines a false N-line as one where
*something already ruled in provides it*, and **nothing in this tree provides a cap** — no verb creates
a Person, so the cast is fixed at world-build by a missing producer. That is **ABSENT**. The general
form is worth keeping: *a verdict that reaches the right answer through the wrong line will
mis-classify the next primitive that resembles it.*

**What the two largest columns say together.** Twenty-one refusals and nine unproduced carriers against
seventeen produced: **the suite's catalogue is, for this tree, mostly a catalogue of things already
decided against, plus a short list of carriers waiting on a producer.** And the third column is the one
a reader should not skip: **fourteen ABSENT rows** — no carrier, no writer, nothing refusing one — of
which three (`B5` poaching, `C3` delegate-as-defection-vector, opinion diffusion) become reachable from
`P1` alone, and two (`C6` recruitment, inherited statistics) wait on the same missing producer as `C1`:
**no verb creates a Person.**

**What the three survivors have in common** is that each is a **field or argument already typed and
already read by something**, waiting on a producer: `Tenure` has no `term` but `T-n` names one and a
generic `release` verb is specified for it; `Claim.source` is a `str` filled with a channel label; and
`Claim.predicate` / `Claim.value` are `str` / `Any` filled with an event kind and a hard `True`.
**None is a system, and none needs a new carrier.**

⚠ **AND THE LEDGER IS ONE-DIRECTIONAL, WHICH IS ITS LARGEST LIMIT.** §7 scores *the suite's catalogue
against Valoria*. It does not score *Valoria's mechanics against the suite* — so a mechanic this tree
runs that no catalogued primitive names appears nowhere above, however central it is. Six such families
already execute in `engine/season/`. **`06_VALORIA_UNPLOTTED.md` (Part F) runs the ledger in the other
direction**, and it is the half that says what the game actually is rather than what it has refused.
