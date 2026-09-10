# Part B (1 of 2) — the substrate proposals: P1 · P2 · P3 · P4

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`.

All four land in `engine/season/`, the tree Layer 1 governs. **None adds a carrier, a `Tenure` kind,
an eligibility kind, a step, a write class or a `Sensation` scalar.** Grades use
`architecture/meta/04_CODE_ARCHITECTURE.md:72-92`: **STRUCTURAL** (the defect has no spelling) ·
**MECHANICAL** (one path, it refuses, one named test sees a bypass) · **CONVENTION** (a reader
notices, stated as such and never dressed up).

Every number is `assumption` with a site and a three-point sweep per `ID-6`. **No proposal here
proposes a value.**

---

# P1 · DEARTH REACHES THE BODY

### the subsistence shortfall writes `(Person, body)` and emits

**Claim.** The one licensed motion the design already names and the code refuses — matter reaching
bodies — is the missing first link of the revolt chain and the damping term every later loop needs.

**Starts from.** `write_matrix.yaml:161-167` — `(Person, body) · [MAT, RES] · MATTER/ACTS ·
social false · emits body.changed · person.died`. `driver.py:415-436` computes `short` per rung and
then does nothing with it. `rosters.yaml:973-976` — `band_floors.body: {full_operations 800,
limited 500, withdrawal_only 100}` already gate the body. `decision.py:165, 890` — `budget()` already
subtracts `body_band_penalty` on those floors. `world_q.py:217-221` — Q3 already accepts a
person-keyed crossing (`if who == p.id`). And `holonic:868-871` §25.2: *"MATTER touches persons…
condition is taken from the Sites you stand beside. Bodies are a licensed clock, so this is sanctioned
world-driving, not a new exception."*

**Adds.**
- ⚠ **THE DENOMINATOR IS STATED ONCE, HERE, AND IT IS THE SAME EXPRESSION IN BOTH PLACES** — the
  adversarial pass found P1 and P2 disagreeing about it, which would have been the *third* expression
  for one quantity in a set whose whole §3.2 exists to end the second. **Define
  `mouths(r) = Σ weight(eaters at r) + Σ envelope(r)`** (the envelope term is P2's; before P2 it is
  zero). **The draw is `wt × mouths(r)` and the deficit share is `short × weight(p) / mouths(r)`.**
  Read any other way — a draw over 203 mouths and a shortfall distributed across a denominator of 3 —
  **the named cast absorbs the envelope's hunger and dies at the first shortfall**, which is the
  opposite of the damping P1 claims. The envelope's own residual share is carried by P2's
  `deaths[band] × (1 + k′·(1 − fed_ratio))`.
- In `matter()`, after the larder draw: for each eater `p` at rung `r`,
  `deficit_p = short × weight(p) / mouths(r)`, then
  `w.write("body", MATTER, lambda: setattr(p, "body", max(0, p.body − k·deficit_p)),
  record_kind="Person", fieldname="body", driver="Event", emits="body.changed", subject=p.id,
  causes=[p's prior body.changed | r's stores.changed Event])`.
  **The draw itself changes to `wt × Σ weight(eaters)`** — which fixes `01_PRIMITIVE_BASE.md` §3.2 and
  makes `SUBSIST` and the larder one arithmetic.
- **Band crossing.** If `before ≥ floor > after` for any `band_floors["body"]` floor, append
  `(p.id, verb, before, after, ev.id)` to `w.crossings` — the person-keyed tuple Q3 already reads —
  and emit `condition.band_crossed` with `subject = p.id`, `causes = [the body.changed Event]`.
  **Q3's referent becomes the person's containing rung id** so `opening_set` can form candidates
  *about the hearth* — `transfer`, `petition`, `speak`, `move`.
  ⚠ **CORRECTED BY THE ADVERSARIAL PASS — the first draft called this "a data fix at `world_q.py:221`,
  `referents=(at,)` rather than `(what,)`", and that edit does not produce the referent.** `:217-221`
  computes `at` as `w.sites.get(who).rung`, and `w.sites.get(<a person id>)` is `None`, so the edit
  would yield `referents=(None,)`. **The fix needs `at = parent_of(w, who)` when `who` names a
  person**, and it is a branch, not a one-word swap. ⚠ **And a second under-specification:** the
  person-keyed branch fires for that person **only** (`who == p.id`), so **nobody else at the hearth
  gets the question** — which is what the *"candidates about the hearth"* argument needs. Closing that
  is a further change this proposal does not specify. ⚠ **Nor is this `H-110`'s repair**, which wants
  the crossing's **event id** carried onto the Question (`hole_register.yaml:1495-1499`) — a different
  one-line change to the same line. **P1 takes the referent branch, not `H-110`.**
- **At `body == 0`:** a `(Person, exists)` MATTER write emitting `person.died`, closing every live
  Tenure naming `p` through `caused_person_exists=p.id` — the §15.3 seam
  `engine/season/state/world.py:373-379` already enforces, and the pattern `_eff_kill` already uses at
  `effects.py:383-386`.
- **For a cohort (`weight > 1`):** body is the cohort's mean condition; the weight decrement lands at
  CENSUS on the existing `(Person, weight) · [CEN]` row, `weight −= round(weight × mortality(band))`.
  ⚠ **This is the one place a matrix edit is declined** (`[MAT, CEN]` on weight) in favour of a
  one-season lag. `assumption`; site `census()`; sweep
  `[CEN (default), MAT (a matrix edit), none (control: cohorts never shrink)]`.
- **Fixtures:** `k` (body loss per unit deficit) and `mortality[band]` — `assumption`, register rows,
  three-point sweeps.

**New primitive?** None. One data fix (Q3's referent), one arithmetic fix (`len` → `Σ weight`), one
new write site on a row that already exists.

**Compliance.**

| axiom | argument | grade · checker |
|---|---|---|
| `AX-5` | bodies are on the list (`01_AXIOMS.md:151`); §25:854 licenses *"natural death"*; §25.2 licenses MATTER touching persons | **STRUCTURAL under the gate · MECHANICAL at runtime** — `(Person, body)` admits MAT and `world.py:325-343` **raises `Forbidden`** on any other step. ⚠ Regraded by the adversarial pass: a runtime refusal is not an absent spelling (`04_CODE:88-92`) |
| `T-b` | the crossing emits and produces no outcome; a **body is not an outcome, it is the case** (§D.0's second kind, `01_AXIOMS.md:685`); what changes is `budget()` and the question set — *what may be chosen* | **MECHANICAL** — `w.write` refuses a `social:true` write by an Event (`world.py:351-357`); `body` is `social:false` |
| `AX-1` | nobody decides; hunger narrows scenes and raises a question; the person still chooses | **STRUCTURAL** (`choose` takes no World — `T-f`) |
| `AX-4` | one writer per season for `body` at MATTER, holding the driver's token | **MECHANICAL** (`write()`'s class check, `:344-350`) |
| §15.3 | death closes Tenures only through the death the same row caused | **MECHANICAL** (`world.py:373-379`) |
| `ID-3` | every write emits, with a non-`ROOT` cause | **MECHANICAL** — `world.py:391-406` refuses a MATTER write declaring no emission |

**⚠ The code comment this overturns.** `driver.py:431-436` refuses starvation as *"the outcome L5
forbids… a social consequence written at MATTER."* **Both halves misread the design.** `body` is
`social:false` by Part D's own row, and `T-b`'s "outcome" is *"what a decision produces"*
(`01_AXIOMS.md:285-286`) — a body declining is not a decision. Under `CLAUDE.md` §0.05 (*"decide and
then CHANGE THE CODE — never declare the prose authoritative"*) the code moves to match §25. This
closes by §0 test 3 (answered by a design document) and test 4 (precedent: `Site.condition` wear
crosses floors and emits without producing an outcome). **Not an escalation.**

**Loop. Sign `−`.** Shortfall → fewer and lighter eaters → smaller draw → the shortfall closes. A
damping term; `G13` asks for a bound only on `+`. Register as a `LOOP` row, `default: none — damping`.

**Gap filled.** Reading 09 §2.1's first link; `H-11`'s *"scaled by weight"* made true; the `S` defect
of `01_PRIMITIVE_BASE.md` §3.2; the death cascade `driver.py:319` lists as `not_implemented`.

⚠ **AND ONE MORE, WHICH IS WORTH MORE THAN THE OTHERS AND WAS BURIED IN *Adds* AS A DATA FIX.** The Q3
referent correction — from a **verb name** to the person's containing rung id (`world_q.py:221`) — is
**the only CONSUMER fix in this entire set.** Everything else in P1–P7 is a producer: a writer, an
emission, a Query. `references/design_rulings_2026-09-06.md` **R6** names precisely this as the spine:
*"THE FACT PROPAGATES AND NOTHING REACTS TO IT… `question_sources` carries Q1–Q3 plus Q4 `need` and
none is 'a world-fact changed in a way that concerns me.'"* — and the rulings file's closing summary
calls the outstanding item *"build the consumer that makes a person form a candidate from what they came
to believe. Until that exists, every epistemic carrier this file names is a carrier without a reader."*
**Q3 is today a live question source that produces no candidate**, which is exactly that defect; this
line closes it for the crossing case. **It does not close R6's vacancy case, and nothing in this set
does** (`05_` §6.3).

**Borrows.** **Banished** and **Dawn of Man**'s food-limited attrition as the *shape* — a population
that outgrows its larder shrinks — and the uploaded teardown's Stage 1 insistence that the population
primitive constrains everything. **Sen's entitlement failure** via SE-2
(`research/fa_se_historical_precedent_research_v1.md:250-254`): a dearth is a store-to-mouth gap, not
a "Prosperity 0".
**Refuses.** Goldenfurt's `Order −2, PS −2` on Ignore (a social write at MATTER — L4); any starvation
*event card*; a "Dearth state" field; **Medieval Dynasty's per-person hunger meter as interior state**
— body is read-off matter, not a mood.

**Falsifier (`ID-11`).** `test_p1_a_hearth_that_cannot_feed_its_people_narrows_their_season`: seed
`tiny_world` with stores below the draw; assert a `body.changed` Event per eater with
`causes ≠ [ROOT]`; a `condition.band_crossed` with `subject = p.id` when a floor is crossed;
`budget(p)` strictly less than under the fed control; and `questions_for(w, p)` containing a
`band_crossed` question whose **referent is the hearth id**. Control arm: stores ≥ draw → no
`body.changed`. **Assert on `p.body` and the log, never on a counter** — the domestic guard from
`proposals/2026-08-25-throughlines-and-precedent/08_ch5_what_we_should_not_do.md`, whose own
population guards pin a call counter rather than the world. A failing run: `body.changed` emitted with
`[ROOT]`; a crossing whose referent is a verb string; or a cohort at weight 200 whose body moves as if
it were one mouth.

**W-item.** Unblocks `W8`'s own proof (*"stores neither monotonically deplete nor overflow"* is
impossible while eaters ignore weight). Touches no planned item's scope; `W29` (the tenure cache) is a
prerequisite only for casts larger than three.

---

# P2 · THE BODIES CLOCK

### ageing, births and deaths move `Rung.envelope` at MATTER

**Claim.** The envelope's band counts move on the licensed `bodies` clock — the only compounding
quantity the design permits without an author — and **P1 is its bound**.

**Starts from.** `(Rung, envelope) · [MAT, CEN] · MATTER · emits envelope.changed`
(`write_matrix.yaml:287-293`); `holonic:401-406`; `:854, 860`; W9 (`probes.py:1532-1544`) as the
executed write pattern; `driver.py:413` (*"BODIES… STILL NOT BUILT"*); and `driver.py:418`'s
`for rid in sorted(w.rungs)` as the existing precedent for a MATTER pass over every rung.

**Adds.**
- **A roster `envelope_bands`** in `rosters.yaml` — ordered, `open: true`, with the note that order is
  semantic, exactly as `strata` carries at `:121-129`. **The names and the count are `assumption`;
  Layer 1 gives neither.** Seed with the smallest set that carries the dynamics — three bands
  `[young, grown, elder]`; sweep `[3, 4 (the W9 literal), 2]`. `Rung.envelope` stays a list indexed by
  the roster, and the loader refuses a length mismatch (the `wear_per_season` check at
  `fixtures.py:106-123` is the precedent).
- **Fixtures**, all `assumption` with register rows and three-point sweeps: `band_seasons` (seasons a
  head spends in a band before shifting), `fertility` (band-0 additions per grown head per season),
  and `mortality[band]` with `mortality[elder] = 1.0` on the shift out of the last band — **nobody
  outlives the roster**.
- **The MATTER pass**, serial, before the larder (§25's order is *"bodies, larders, yield"*,
  `holonic:846`). Per rung with a non-empty envelope: **(i)** every `band_seasons` ticks, counts shift
  one band up, and the elder shift is the death; **(ii)**
  `births = fertility × envelope[grown] × fed_ratio(r)`, where `fed_ratio` is `1 − short/draw` from
  P1's larder arithmetic — last season's, since larders run after bodies, the same "eat last season's
  stores" ordering `driver.py:406-411` already defends; **(iii)**
  `deaths[band] = mortality[band] × envelope[band] × (1 + k′·(1 − fed_ratio))`. Each is a
  `w.write("envelope", MATTER, …, emits="envelope.changed", causes=[r's prior envelope.changed |
  ROOT])` — **a licensed clock's genuine first emission is the only lawful `[ROOT]`**, per
  `driver.py:485-490`.
- **The envelope eats.** P2 supplies the second term of P1's `mouths(r) = Σ weight(eaters at r) +
  Σ envelope(r)` — **one expression, defined once in P1 and used in both the draw and the deficit
  share.** Without this the envelope is matter in name only — `ID-13`.
- **A Query** `population(w, rung) = r1_aggregate(w, rung, λd: Σ envelope(d) + Σ weight(p) for p in
  presence(w, d))` — the lawful `W_s`, owned by Nobody, cached at the barrier
  (`04_CODE_ARCHITECTURE.md:153`).
  ⚠ **`[GAP: no consumer.]`** Nothing in P1–P7 reads it — the envelope reaches the larder through
  `mouths(r)`, not through this Query. **By `ID-13` that makes it declared and not built**, which is
  the exact defect `01_PRIMITIVE_BASE.md` §2 catalogues against `Sensation.standing`. Named rather
  than shipped as if it were a mechanism; the honest reader for it is a future settlement-scale
  consumer, and this set does not have one.
- **CENSUS reconciliation** (`holonic:1019-1020`, *"envelope reconciliation"*): after P3's
  individuation, `envelope[grown] −= Σ weight minted this season`; a mint that would take a band below
  zero **refuses** and emits `individuation.refused` (§42.2's polarity rule).

**New primitive?** None. A roster for an existing field whose *shape* is declared and whose *bands*
are not; three fixtures; one Query.

**Compliance.**

| axiom | argument | grade · checker |
|---|---|---|
| `AX-5` / `T-c` | bodies is one of the three; *"Nobody wound any of the three, and you cannot bribe silt"* — so `fertility`/`mortality` are fixtures, unbuyable, and acts reach them only through matter (`fed_ratio`) | **STRUCTURAL under the gate · MECHANICAL at runtime** for the step restriction (the same `world.py:325-343` raise); **MECHANICAL at load** for *no act writes the envelope* — no `verb_table.yaml` row declares `writes: Rung.envelope`, and loader invariant 1 (`04_CODE:456`) checks it |
| `AX-5`'s costed clause (`01_AXIOMS.md:177-179`) | *"a population that grows on its own is not [lawful]"* is quantified over **individuation** (see `05_` §2 row 1); the envelope grows and **no Person exists because time passed** — CENSUS stays demand-driven (`driver.py:1375-1383`) | **MECHANICAL** — `(Person, exists)` at CEN requires a `person.demanded` antecedent (P3); a test asserts `\|persons\|` is unchanged by 100 seasons of P2 alone |
| `T-i` | not a per-container clock: one driver pass over all rungs, exactly as wear over all Sites | **CONVENTION** — a reader sees the loop lives in `matter()`; `PLAN.md` §8.1:1989 |
| §10.3 *"the envelope does not act"* | no ledger, no stance, no Tenure subject; it appears in no `Act.actor` and no `presence()` result | **STRUCTURAL** — `presence()` returns persons only (`world_q.py:152-154`) |
| `T-a` | `population()` is a Query; nothing stores it | **STRUCTURAL under the gate · MECHANICAL at runtime** — `Rung.__setattr__` **raises** on an undeclared attribute (`carriers.py:531-538`); the whitelist is enforced at assignment, not at compile |
| L4 *"NO SOCIAL QUANTITY MOVES HERE"* | the envelope is `social:false` matter | **MECHANICAL** (`world.py:351-357`) |

**Loop. Sign `+`.** `envelope[grown] ↑ → births ↑ → (band_seasons later) envelope[grown] ↑`.

**Bound — stated so `G13` has something real in `default:`, because `G13` will not check it:**
**(i)** `fed_ratio` — births scale down and deaths up as the larder falls short, which is P1's `−`
term, and `yield` is the only source of stores (`effects.py:411`, `rosters.yaml:940-942`), finite per
Site per season; **(ii)** `mortality[elder] = 1.0` caps a lifespan at `bands × band_seasons`;
**(iii)** `condition_scale`-bounded yield (`driver.py:458-460`).

⚠ **Without P1 this loop has no bound, and `G13` would accept `default: "TBD"`**
(`register.py:329-333`). **P2 must not merge before P1.** The period is `≥ 2 × band_seasons` seasons,
which under `MAX_SEASONS = 6` (`H-33`, `PLAN.md:1372`) is unobservable — so P2's falsifier depends on
`W29`.

**Gap filled.** `F.19`'s dynamics half; `ID-16`/`H-106`'s absent amplifying loop; `F.28`
(*"nothing bounds a spiral across seasons"*) gets its first declared bound; and the
`env.population_change` Key's four declared causes
(`systems/_architecture/reference/key_type_registry_v30.md:816-831` — migration · mortality ·
birth_surge · conscription) get three producers: births and deaths here, conscription in P3, and
migration is `move`, which already executes.

**Borrows.** **Banished's delayed cohort** — the boom that dies as a wave — as *dynamics on an agreed
primitive*. **Medieval Dynasty's maternity hole** as the shape of a delayed inflow. **Victoria 3**'s
rule, via `04_ch1`'s R5: *"a top-level number must be derived from the agents backing it, never
independently tracked"* — `population()` derives.
**Refuses.** Banished's **housing as the lever** (that is `F.20`, P4 — and see the `E-1` escalation);
Medieval Dynasty's per-person marriage and pregnancy timers (individuals are not on a clock; the
envelope is); **CK2/CK3's parentless spawns and five-figure character counts**
(`research/valoria_game_precedent_companion_v1.md:176-181`, the corpus's own refuse #13 — and the
envelope is O(bands) per rung, which is the whole point); and **greenfield v2's
Local-Actor-count-per-place-type as *the* population**
(`proposals/2026-08-29-greenfield-systems-suite-v2/03_world_population.md:83-88`) — kept instead as
the world-gen roster, which is `H-05`/`F.31`'s licensed form.

**Falsifier.** `test_p2_a_boom_dies_as_a_wave`: seed `envelope = [0, N, 0]` with `fed_ratio = 1`; run
`3 × band_seasons` seasons under `W29`; assert `envelope[young]` peaks at season 1, `envelope[grown]`
at `band_seasons + 1`, `envelope[elder]` at `2 × band_seasons + 1`, then zero; assert every
`envelope.changed` after the first chains to the previous one (no second `[ROOT]`); assert
`|w.persons|` unchanged. **Two control arms**, as guard 10 demands: `fertility = 0` → the envelope is
monotone non-increasing; `fed_ratio → 0` (an empty larder) → births 0, deaths elevated. ⚠ **And a
third arm the adversarial pass requires, because P1's falsifier seeds no envelope and this one pins
`fed_ratio = 1`, so neither can see the `mouths(r)` disagreement:** an **envelope-present** arm —
three named persons and an envelope of 200 — asserting the draw is over 203 and that no named
person's `body` absorbs the envelope's share. A failing run:
a band count going negative; an envelope changing at a step other than MAT or CEN (the gate raises); or
a Person appearing with no `person.demanded` antecedent.

**W-item.** Extends `W8`'s MATTER pass; depends on `W29` for observation. **Duplicates no item** — no
`W`-item supplies a rule for how a quantity moves over time.

---

# P3 · INDIVIDUATION IS A REFUSAL

### `person.demanded` and the CENSUS mint

**Claim.** A demand is a refusal Event whose `emits_on_refusal` names a person who does not exist;
CENSUS reads those Events once and mints a `Person` out of the envelope, at weight, with a person-rung
and a `contain` edge in the same write.

**Starts from.** `driver.py:1371-1383` (CENSUS writes nothing);
`(Person, exists) · [MAT, RES, CEN] · emits person.died · person.individuated`
(`write_matrix.yaml:189-195`); `(Person, weight) · [CEN]` (`:217-223`); `F.1`'s stated default
*"a refusal Event kind `person.demanded`"* (`04_CODE_ARCHITECTURE.md:1063`); `H-51`
(`hole_register.yaml:582-591`); `F.30` — *"an individuated Person needs a new person-rung and
`contain` edge in the same CENSUS write, or the new Person is nowhere"* (`04_CODE:1134`); and
`01_AXIOMS.md:172-175` — *"A demand is produced by acts. So individuation is authored: the demand is
its author."*

**Adds.**
- **A roster `demand_kinds`** — the refusal kinds that constitute a demand, **read off the verb table
  rather than invented**: `dispatch.refused` when its precondition *"the named person exists"*
  (`verb_table.yaml:184`) fails; `levy.refused` where the payload names hands rather than matter
  (conscription); `petition` at a rung with no live person; and a **Named** operand — an act whose
  `subject` resolves inside a cohort (*"the praefect fines **a smuggler**"*,
  `proposals/2026-08-31-ideal-v2/02_THE_SEASON_LOOP.md:963-965`). ideal-v2's two rosters (five
  generation triggers, four individuation triggers, `:956-969`) are adopted as the **target**, and only
  the members the loop can already emit are shipped; the roster carries
  `incomplete: {have: n, target: 9}` exactly as `conviction_axes` does at `rosters.yaml:149-152`.
- **CENSUS**, reading the season's log once (`holonic:1019`, *"reads the post-eviction ledger set
  ONCE"*): for each `person.demanded` Event at rung `r` requesting weight `n` (default 1; conscription
  requests `n`), if `envelope[grown](r) ≥ n`, mint
  `Person(id=H(seed, tick, r, "individuated:"+event.id), weight=n)` — marks and capability drawn from
  the envelope
  `[assumption: Layer 1's Envelope is counts only (`holonic:372`), so P3 mints with empty capability
  and the parent rung's marks, and records the gap]` — together with a `Rung(kind="person")` and a
  `contain` Tenure into `r` **in the same write** (`F.30`); then `envelope[grown] −= n`; and emit
  `person.individuated` with `causes = [the demanding Event]`. Otherwise emit `individuation.refused`.
- **De-individuation** (§29, `holonic:1019`): a person with no live `hold`, no `knot`, no live
  Petition, and whom no other person's post-eviction ledger names, folds back — weight returns to the
  envelope, `(Person, exists)` closes at CEN. Order-safe because CENSUS reads one snapshot (ideal-v2
  `02:936-945`). `assumption`; sweep `[on (default), never (control), knot-only]`.

**New primitive?** None. A roster; a CENSUS body on rows that already exist. **What is deliberately
not added:** a `Cohort` subclass (`PLAN.md` §8.1:1989; `T-l`), a demand *field*, a spawn queue, a
clock.

**Compliance.**

| axiom | argument | grade · checker |
|---|---|---|
| `AX-5` (costed clause) | every mint has an act as antecedent — `causes[]` walks refusal Event → act id; *"no clock generates anything"* holds by construction | **MECHANICAL** — a test walks `causes[]` from every `person.individuated` to an `Act` in `driver.resolved` (the `R3` route, `PLAN.md:1544-1546`) |
| `AX-1` | the demanding act had a person actor; `driver.py:651-655` refuses any other | **STRUCTURAL** |
| `AX-6` | de-individuation is the closer; nothing minted is permanent without a holder or a rememberer | **MECHANICAL** (the CENSUS predicate) |
| `T-l` / `ID-7` | one class, `weight = n`; a conscripted cohort of 40 goes through the same `choose` — probe P21 already demonstrates it | **STRUCTURAL** — no subclass exists to convert to |
| `T-a` | nothing stores *how many were minted*; the envelope is the residual | **STRUCTURAL** |
| §26.1 / `T-f` | CENSUS is resolver-side; `choose` never sees the envelope | **STRUCTURAL** |

**Loop. Sign `+`**, and it is `H-102` extended: more persons → more acts → more refusals naming absent
persons → more persons. **Bound:** `scene_budget` (5) per person per season, since each demand costs a
scene; the envelope's grown band, finite and P2-fed; and de-individuation returning the unused.
Declare a `LOOP` row naming all three. ⚠ Note the `W29` ~N³ wall (`PLAN.md:1378-1379, 1626-1633`) as
the **engineering** bound the design must not rely on — *"100 persons → seconds per season"*, measured
at 11.44 s and then 5.11 s at 97 persons, with the plan's own instruction to *"carry the conditions,
not the literal."*

**Gap filled.** `F.1`, `H-51`, `F.30`; the individuation half of `F.19`. `H-05`/`F.31`'s world-gen
roster is the *other* lawful source and is left exactly as it is — *"a roster read from a registry
row; not a clock"* (`hole_register.yaml:106-116`).

**Borrows.** **URR's importance gate** (`04_ch1` R5 — generate cheaply, simulate only above a
threshold): the envelope *is* the cheap layer and individuation *is* the threshold, **demand-shaped
rather than importance-shaped**. **Caves of Qud's** abstract-then-reify. **Manor Lords'
family-as-atom** on the mint side — a hearth's people are one record until named.
**Refuses.** `generate_npc`'s seasonal tap (`systems/world/sim/npe.py:226`, zero callers — and the
reason it has none, no canon count, is the reason `AX-5` gives); any Local-Actor tier as a second
entity class (greenfield's own J-M ruling agrees, `03_world_population.md:78-80`); **Tropico's
fully-simulated citizens**, at the cost the teardown names — shack-squatting nobody asked for.

**Falsifier.** `test_p3_nobody_exists_because_time_passed`: 30 seasons of P2 with no acts →
`|persons|` constant. `test_p3_a_levy_that_names_hands_mints_a_cohort`: a `levy` payload requesting 40
hands at a settlement with `envelope[grown] ≥ 40` → at CENSUS one new `Person` at `weight = 40`, a
person-rung, a `contain` edge, `envelope[grown]` reduced by 40, and
`person.individuated.causes = [levy.refused.id]`; at `envelope[grown] = 10` → `individuation.refused`
and no Person. **Assert on `w.persons`, not on a counter.** A failing run: a Person whose `causes[]`
walk ends at `[ROOT]`.

**W-item.** `W27` (cast from case) is the **authored** source of persons; P3 is the **runtime** source.
They share `(Person, exists)` at CEN and must share the mint —
`H(seed, tick, subject, purpose)` (`04_CODE:145`). `W31(a)`'s "commit first" is unaffected. `W29` is a
hard dependency for casts larger than three.

---

# P4 · FOUNDING AND BUILDING

### `found` writes `(Rung, exists)`, `build` writes `(Site, exists)`

**Claim.** The two existence rows that have no producer get one verb each, timber and ore get their
first consumer, and the world stops only decaying.

**Starts from.** `(Rung, exists) · [RES] · ACTS · social true · emits rung.founded`
(`write_matrix.yaml:294-300`); `(Site, exists) · [RES] · emits site.built` (`:322-328`); `hearth` in
`rung_kinds` (`rosters.yaml:92`); `succeed: Rung → Person, 1` — *"the hearth's transmission pointer"*
(`holonic:542`); `site_kinds` and `site_yield` (`rosters.yaml:662, 923-950`); `establish` as the
precedent for an act that creates a carrier and its edges (`verb_table.yaml:194-199`); `F.20`/`H-41`/
`H-105`; and `ID-16`'s own text naming the site-condition loop `H-105` as *"a thing the design found
and filed"* (`01_AXIOMS.md:557-561`).

**Adds — two verb rows.**

```
found:  stratum uncontested_material · eligibility [presence:<rung>]
        requires_typed: {form: amount, of: from, kind: <kind>, at_least: <amount>}   # the founding stake
        writes [Rung.exists, Tenure.since, Tenure.since, Tenure.since, Rung.stores, Rung.stores]
        emits [rung.founded] · emits_on_refusal [founding.refused]

build:  stratum uncontested_material · eligibility [presence:<rung>]
        requires_typed: {form: amount, of: from, kind: timber|ore, at_least: <amount>}
        writes [Site.exists, Site.condition, Rung.stores]
        emits [site.built] · emits_on_refusal [building.refused]
```

`_eff_found`: mint `Rung(kind=hearth)` under the actor's present rung; three Tenures —
`contain(child → parent)`, `contain(actor → child)` (the founder moves in; `_eff_move` at
`effects.py:163` is the pattern for closing and opening containment), and `succeed(child → actor)`;
then move the stake `from` the actor's hearth `to` the new rung, using the two-sided `_eff_transfer`
pattern at `effects.py:445-452`. `_eff_build`: mint `Site(rung=here, kind, condition=initial)` and
debit the stores.

⚠ **Kind is restricted to `hearth` (and `community`).** Settlement founding collides with a standing
`needs_jordan` — SE-9(a), `fa_se_historical_precedent_research_v1.md:292-296`, *"never adding nodes"* —
and is left there rather than resolved by convenience.

**Closers (`ID-14`).** For `Site`: `condition → 0` under wear is the material end; `destroy_record`'s
shape would give a `raze` row if one were wanted, and none is added, because **wear already closes what
build opens**. For `Rung`: **declared closer: none, argued.** A founded rung is an *address* (§D.2,
*"the address, never the occupant"*); an empty hearth is a ruin — still nameable, still holding its
Records, constraining nothing. `AX-6` guards state that **constrains**, and an empty address
constrains no act. **Grade CONVENTION**, said as such; the alternative (`[RES, CEN]` on
`(Rung, exists)` with a CENSUS de-founding when envelope and presence are both zero) is one matrix
edit away and is named here so the next session does not re-derive it.

**New primitive?** None. Two verb rows on two existing matrix rows; two effects. **Loader invariant 2**
(`04_CODE:457` — *"every matrix row with RES has ≥1 producing verb"*) is *satisfied* by this proposal
for two rows that violate it today.
`[GAP: whether invariant 2 fires at load on `(Rung, exists)` today — `engine/season/data/matrix.py:200-230` was not opened]`.

**Compliance.**

| axiom | argument | grade |
|---|---|---|
| `AX-1` | a named person present at a place founds; no *"settlement grows"* | **STRUCTURAL** (`Act.actor` check, `driver.py:651-655`) |
| `AX-4` | the stake moves two-sided through `Rung.stores`; matter is conserved | ⚠ **CONVENTION — regraded.** The first draft named `F10`'s conservation assertion (`effects.py:429-438`), and **that assertion cannot see this failure**: it weighs every rung across its own probe season, which never runs `found`. A `_eff_found` that debits a stake and credits nothing is **invisible to it** — `ID-10`. A new conservation assertion over the founding path is what would earn MECHANICAL |
| `AX-6` | the founder owns the `succeed` and `contain` edges (§15.1); a hearth's people can leave, since `move` executes | **MECHANICAL** (the opener/closer map, loader invariant 6) |
| `T-b` | building changes which verbs a place **offers** (`band_floors`) — not an outcome | **MECHANICAL** — `world_q.verbs` gates on condition (`:132-135`), and it is a function a caller may simply not call |
| `ID-14` | opener declared for both; the Site closer is wear; the Rung closer is declared **absent with an argument** | **CONVENTION** on the Rung half — said so |
| §F.1 | two rows, no carrier | — |

**Loop. Sign `+`.** Sites → yield → stores → stakes → Sites. **Bound:** wear (`wear_per_season`,
`rosters.yaml:698-701`, a `−` clock on every Site); `season_factor`-bounded yield; the stake cost; and
the scene budget, since each `build` is a scene. **All four already exist.** Declare a `LOOP` row
naming them. This is the loop `ID-16` says `H-105` is one side of.

**⚠ The direct warrant, found late and stronger than `F.20` alone.**
`references/design_rulings_2026-09-06.md` **R4 · THE WORLD MUST CHURN** is a Jordan ruling on exactly
this subject: *"Lands on `F.20` — the world only decays. `Rung.exists` and `Site.exists` have **zero
producers**. Nothing founds, builds or grows."* It names **four routes, three of which need no axiom
moved**, and **P4 executes routes (1) churn by NPC action and (2) churn by matter.** So P4 is not an
inference from a register row — **it is the ruled work.**

**Gap filled.** `F.20`; `H-41` (two of its three rows); `H-105`'s complement; the three dead matter
kinds; and the teardown's sharpest named coverage gap — **Heroes of Might and Magic**'s *"accrual as a
property of a built structure in a place"* (`research/valoria_game_precedent_companion_v1.md:553`),
whose unasked question was *"is per-settlement accrual the missing writer for `facility_tier`?"*
`site_yield` on a built Site **is** that accrual.

**Borrows.** **Manor Lords' burgage plot** as the atom that grows organically — a hearth founded by a
person who moves into it, carrying a succession pointer. **Banished's housing as the lever** on P2's
inflow — **but only if `E-1` lands on the capacity arm** (`05_` §4). **HoMM's dwelling accrual.**
**Refuses.** Goldenfurt/`Develop`'s `Prosperity +1` (a stored aggregate on a Rung); Manor Lords'
burgage *level* as a stat (a Site's kind and condition **are** the level); any facility-tier scalar
(the tier is the set of Sites at the rung — a Query).

**Falsifier.** `test_p4_a_hearth_is_founded_by_a_person_present_with_a_stake`: `p_low` present at `S`
with `stores(hearth(p_low), grain) ≥ stake` → after RESOLVE a new `Rung(kind=hearth)` exists,
`parent_of(new) == "S"`, `parent_of("p_low") == new`, a live `succeed` from `new` to `p_low`, grain
conserved across the world, and `rung.founded.causes == [act.id]`; with insufficient grain →
`founding.refused`, no rung, grain unchanged. `test_p4_timber_is_finally_consumed`: a `build` debits
timber. A failing run: a hearth with no parent (so `descendants` cannot reach it), or matter created
from nothing.

**W-item.** `W8`'s stated scope stops at yield, and `04_CODE:61-62` says `F.20` *"fails the loader at
build step 2"* — **this is that item, and it is unnamed in the `W`-list.** `W32` (`work` does
something) is adjacent and independent.
