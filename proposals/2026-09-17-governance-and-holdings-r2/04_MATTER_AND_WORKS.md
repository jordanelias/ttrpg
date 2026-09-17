# 04 · MATTER AND WORKS — how matter reaches people, and what it is to build something

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: **`SE`** · id: **`ED-SE-0053`**. Round two of `proposals/2026-09-17-governance-and-holdings/`; this file **supersedes `02_THE_BUILT_WORLD.md`'s delivery and hearth-store moves** and keeps the rest of it by pointer, struck where overturned.
## Grade under `CLAUDE.md` §0.2: **`paper`.** Nothing designed here executes. §C.5 names the artifact that would move it and says what it costs.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *"large-context synthesis"* and *"contract closure"*), from a read-only `fable`-tier plan that adjudicated the round-one verdict before this file was written. Four sibling documents were authored concurrently from that plan; this file writes only its own subject (**Q3**) and the `works` lifecycle.
## Scope pin: every `path:line` below was **re-opened in this session against the working tree** before it was quoted, and every count was produced by running the thing that would have shown it wrong (`CLAUDE.md` §0.1 pt 3 — *"a citation you have not opened is not a citation"*). Where a carried-forward citation was wrong it is **struck in place and recorded in the APPENDIX**; there are **eleven** such repairs and two of them change a claim rather than a line number.
## Conventions (suite-binding, from the round-one README): **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, cited `§Letter.Number` and **never by line**; **`AX`** = `architecture/meta/01_AXIOMS.md`, cited `AX-n` / `ID-n` / `T-x` with a line as a finding aid only; **`holonic`** = `architecture/holonic_ARCHITECTURE.md`. A bare `01`/`02`/`03`/`04` means a file in **this** directory unless the sentence says *round one*. This file's falsifiers are **`MW-n`** and its loops **`MW-L±n`**; round one's `BW-n` rows that survive are mapped in §D.0. The multi-season construction is **a `works`** (round one `01` §A.12's ruling, binding on the suite) — never *a work*, which collides with the live verb `work`, and never *a project*.

---

> **Jordan, the sentence this document exists to make executable:** *"a player whose character can
> govern a settlement would like to be able to explicitly set policies or **advance a project to
> build something**."* · *"a change to how a rung functions will likely have impacts on rungs below
> it. **A provincial policy on farming taxation may end up impacting a hearth**, you know?"* ·
> *"I do not want this work to be constrained by existing work. I want the best possible design
> ideas and concepts, and we can modify code accordingly."*
>
> **And the clause this document exists to make false**, `ARCH §F.20`, verbatim: *"⚠ **FOUNDING
> VERBS** — no stage names a verb that founds a hearth or builds a site | the rows are dropped until
> a verb is ruled | **the world only decays — nothing is ever founded or built.** This is what blocks
> build step 2."*
>
> ⚠ **THE SECOND QUOTATION IS THE FALSIFIER OF THE FIRST, AND IT STILL IS.** `§F.20` does not close
> because this file is written. It closes when a `rung.founded` and a `site.built` Event appear in a
> run's log. **MEASURED THIS SESSION, one season of `build_realm(0)`: neither appears, and the log's
> sixteen kinds are listed at §A.2.1.**

---

# PART 0 · THE CONFORMANCE DIVISION

**This is not a design claim. It is a division, and it must be read before PART A**, because most of
what follows is either **already ruled Layer 1 and merely unbuilt**, or **a declared row with no
producer**. Crediting a conformance item as new design is how a proposal inflates itself; reading an
extension as ratified is how a session ships an unruled change. Round one's README made this
division suite-binding and it is kept.

## 0.1 · CONFORMANCE — ruled or declared already, and unbuilt

| the thing | where it is already ruled or declared | what is missing |
|---|---|---|
| **matter and bodies move by themselves at MATTER** | **`AX-5`** (`AX:151`): *"THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS: MATTER, BODIES, AND THE FADING OF MEMORY"*, stated as a **list** (`AX:162`) | **bodies.** Two of the three motions run (`matter.py:111-153` decay, `:155-225` matter); the second has no code |
| **`(Person, body)` moves at MATTER and emits** | `write_matrix.yaml:161-167` — `steps: [MAT, RES]`, `class: "MATTER/ACTS"`, `social: "false"`, `emits: "`body.changed` · `person.died`"` | the **MAT half.** The RES half runs: `_eff_kill` (`effects.py:389`, `:393`, `:403`). ⚠ **STRUCK:** round one's *"`(Person, body)` is a matrix row with no writer"* is **false as stated** — see the APPENDIX |
| **a person may die at MATTER** | `write_matrix.yaml:189-195` — `(Person, exists)`, `steps: [MAT, RES, CEN]`, `emits: "`person.died` · `person.individuated`"` | any MATTER-step producer |
| **a person's body reads as BANDS off `band_floors["body"]`** | `decision/budget.py:64-75`, `body_band_penalty`, **live and person-side**, called from `budget()` at `:60` and from the loop at `deliberate.py:116-117` | **a nonzero input.** MEASURED: all 46 persons at `body == 1000`, `body_band_penalty == 0` for all 46 |
| **the band table for a person's body already exists and is already declared as such** | `rosters.yaml:1196-1199` (`band_floors.body` = `{full_operations: 800, limited: 500, withdrawal_only: 100}`), and `rosters.yaml:814-815` says it in its own words: *"⚠⚠ `body` IS NOT A SITE. It is `(Person, body)`'s band row, here because `band_floors` keys on THIS roster and `H-38` ruled `Site.condition` is the model — **no second scheme**"* | nothing. **§A.4.3 spends this rather than adding `band_floors.person`, and that is a DEPARTURE FROM THE PLAN, argued there** |
| **a death ends every Tenure THROUGH the death** | `holonic §15.3`; implemented at `effects.py:415-418` | one **owner**. The cascade is four lines inside one effect body; MATTER needs the same four |
| **`(Rung, exists)` and `(Site, exists)` are declared with a step, a class, a `by:` and an emission** | `write_matrix.yaml:294-300` (`rung.founded`) and `:322-328` (`site.built`) | **a producer.** MEASURED by the matrix header's own reproduce command (`write_matrix.yaml:41-45`): **40 rows, 10 producerless `[RES]` rows**, both of these among them |
| **`restore` is a fully specified verb row with a formula** | `verb_table.yaml:448-467` — `eligibility: ["own", "presence:<site>"]`, `writes: ["Site.condition"]`, `emits: ["site.restored"]`, `emits_on_refusal: ["restore.refused"]`, `grade: "ruled"`, and the formula at **`:465`**: `Δ = +(1 − condition) × f(degree) × share` | an `@effect_for` body. MEASURED: **11 effect bodies**, `restore` not among them; `resolvable_verbs()` returns **18 of 38** and excludes it |
| **`share` and `draw_share` are declared resolver-side Queries** | `holonic §17` roster — `draw_share` at `:599`, `share` at `:600`, under the header *"`Query` — never stored, always recomputed"* at `:591` | an implementation. §A.6.4 gives one and counts it **0 added**, on round one's own precedent for `capacity` |
| **`capacity` is a declared resolver-side Query** | `holonic:600` | an implementation, **gated on `ED-SE-0051`** (§A.11). Not built here |
| **a works is a Record kind, opened by an act that already runs** | `ARCH §A.3` row 11 (*"`Petition`, `Dispensation` … **kinds of `Record`**"*) and `ARCH §B.4`/`§B.5`'s synthesis call folding them *"with no new rows"* | the `works` row on `record_kinds` (a NEW roster, owned by sibling `02`) and the two bodies §A.7 gives |
| **the maker of a Record holds it, and a maturation stops if the maker is gone** | `effects.py:286-289` mints the `hold` in the same act; `matter.py:73-78` looks the live holder up and refuses the maturation with the reason TRACEd verbatim — *"a half-made copy STOPS rather than finishing itself"* | **nothing. Both run today.** MEASURED: `record.created` fires **69 times** in one season |
| **a fabric's condition may not be node-keyed onto a place** | `ARCH §B.4`: *"Node-keying is structurally unwritable: a Rung has no condition field, so the collapse cannot be spelled"* (`:252`); `holonic:449-451` gives the two-wrong-answers argument | nothing. It is structural: `Rung.__setattr__` raises on an undeclared field (`carriers.py:589-597`) |
| **`hold`'s object domain excludes `Site`** | `holonic:538` — `hold : Person → Office | Rung | Record | Proposition`, **1 per object**; `ARCH` PART D row 14 grades *"a banner holding territory"* **STRUCTURAL (typed)** | the check. `World.add_tenure` (`world.py:223`, *"The ONE writer"*) validates `t.kind` (`:242-247`) and `contain` ascent (`:248-256`) and **nothing about object class** |

## 0.2 · EXTENSION — new, and argued here

| the extension | §  | what it rests on |
|---|---|---|
| `nearest_store(w, rung, kind)` — eaters draw **up** the containment ladder | A.3 | `world_q.parent_of` (`:48`), already the ladder walk |
| the larder draw becomes **per eater**, weighted by `Person.weight` | A.3.2 | `Person.weight` (`carriers.py:376`) is the cohort size and the draw ignores it; `write_matrix.yaml:217-223`'s `by:` says *"H-11's subsistence default reads it ('scaled by weight'), so every season touches it"* — **and it does not** |
| the larder pass **splits** from the yield pass into two loops | A.3.3 | forced by the ascent: per-rung interleaving is safe only while the draw is same-rung |
| a shortfall becomes a **signed** `(Person, body)` delta, one number, both directions | A.4.1–A.4.2 | `AX-5` motion 2; `write_matrix.yaml:161-167` |
| `_crossings(...)` — one helper, sites and persons | A.4.3 | factored from `matter.py:252-277`; **no new table** |
| `World.remove_person(pid, cause)` | A.4.5 | factored from `effects.py:415-418`; **one cascade, two callers** |
| `ceiling(w, site)` — the works' matured stages bound the fabric | A.6.3 | counted off `w.log`'s `term.matured` emissions, which `World.last_emission_of` already reads |
| `share(w, p, site)` — the actor's draw-share, derived from co-presence | A.6.4 | `holonic:600` declares it; `world_q.presence` (`:172`) supplies it |
| `restore`'s effect body, and the **delta channel** the fold does not have | A.6.5 | `resolve.py:311-351`'s `earned` out-parameter is the precedent for the shape |
| `found` — one verb, two declared rows, one earned per act | A.7.1 | `resolve.py:338-346`'s `{kind: [ids]}` mapping was built for exactly this |

## 0.3 · DEPARTURE — where this contradicts something standing, said out loud

1. **From the round-two PLAN, §2.3:** the plan specifies *"a NEW `band_floors.person` cell set
   (`{able: 500, failing: 100}`)"*. **REFUSED.** `band_floors.body` already exists, is already
   declared by its own roster note to be `(Person, body)`'s band row, and is **already read
   person-side by live code** (`budget.py:73`). A `person` key would also **refuse at load**:
   `band_floors`' outer key is validated against `site_kinds` (`rosters.yaml:1180`, and
   `fixtures.py:110-123` checks it **both directions**), so `person` would raise `Forbidden` unless
   `person` joined `site_kinds` — which would then demand a `wear_per_season.person` row and a
   `site_yield.person` row or the world would not load. Two ladders for one quantity is an **S**
   defect by `CLAUDE.md` §0.06's own words (*"calculations consistent in methodology"*). Decided at
   §0's **step 4 (precedent: `H-38`, quoted in the roster and again at `hole_register.yaml:793`)**
   and **step 5 (architecture)**. Full argument at §A.4.3.
2. **From round one `02` §A.6's RULED block:** its repair was *"two content moves plus a predicate"* —
   commons eaters ascending by `contain` closure, and DWELLING/PRODUCER fabrics re-keyed to the
   hearth or community they are. **Both content moves are withdrawn.** They move the FABRIC to the
   people; this moves the DRAW to the matter. The ontology is unchanged, no `venues.yaml` row is
   re-keyed, `matter.py:205-206`'s `site.rung != rid: continue` stays exactly as written, and
   `presence:<site>` still has no referent in the populated world — which is stated as a surviving
   limit rather than solved by moving 74 fabrics.
3. **From round one `02` §A.4.1:** `ceiling` was left undecidable (*"`matured stages` has no
   carrier"*). **Decided** at §A.6.3, off the emission log rather than off a per-stage field.
4. **From round one `02` §A.5.1:** `restore`'s blocker was named as *"`share` and `draw_share` are
   declared and unimplemented"* plus a units question. **Both decided** at §A.6.4–§A.6.5. A third
   blocker neither round found is named there: **the fold has no channel for an act's delta at all.**
5. **From `ARCH` PART D row 5**, which says *"The gate now refuses `before == after` at the write, so
   the receipt is never minted"*. **MEASURED FALSE OF THE GATE.** `World.write`
   (`world.py:295-471`) contains no such comparison — `:408` is `before = apply()` and nothing is
   compared, and the emission at `:441-469` is unconditional once `emits=` is passed. The refusal
   that exists is the **fold's**, and it is ACTS-side only (`resolve.py:259-269`). §A.1.3 draws the
   consequence: at MATTER **every block guards itself by hand**, and this document's body write must
   do the same.
6. **From the ratified program's ORDER** (`workplans/2026-09-11-reconciled-program.md:3`): items
   3a/3b and 12 build ahead of the Arc-2 gate. That departure is the suite's **RR-C**, owned by `05`,
   and this document does not argue it.

## 0.4 · WHAT THIS DOCUMENT MAY NOT CLAIM, and does not

- That anything here **runs**. Grade `paper` (§C.5).
- **Hearth larders.** No hearth gains a store, then or ever, by this design. The 4,810 units stay
  where they are produced.
- **Delivery.** Nothing moves matter across a `contain` edge except a person's `transfer`.
- **A demographic bound.** `ED-SE-0051` is **OPEN** and is not closed here (§A.11).
- **`fort_level` or `facility_tier` as free cuts.** Both withdrawals stand (§A.10.2).
- That `ED-SE-0051`'s **capacity** arm is ruled. It is *recommended*, on grounds §A.11 re-argues —
  including the admission that **this document destroys round one's decisive ground for it.**
- A **pacing** claim of any kind. `body_step` is injected, declared and swept (`AX` **ID-6**), and
  §A.4.6 gives the arithmetic at all three arms including the arm where the design breaks.

## 0.5 · WHAT IS CARRIED FROM ROUND ONE `02`, AND IT SURVIVED A PESSIMISTIC PASS

`AUDIT_VERDICT.md` is a terminal-pass record permitted by `CLAUDE.md` §0's narrow exception; it is
**read, not extended**. It attacked round one `02` and these are what it did not break — so they are
kept because they were **right**, not because they exist.

| carried | where it now lives | what the pass said |
|---|---|---|
| **the ontology** — a built thing's **fabric is a `Site`**, its **address is a `Rung`**, and the seam is **occupancy, derived, never stored**: *a building stands on a hearth; the hearth is the plot* | round one `02` §A.1–§A.1.2, by pointer; restated at §A.8 | not attacked. What WAS attacked is its **licensing argument** — see the next row |
| ⚠ **the licensing argument, STRUCK:** ~~*"breaking the wall destroys the district, because `destroy` sets `until` on every Tenure naming the destroyed id"*~~ | the refusal rests on **cardinality** instead | **UNSOUND.** Re-opened here: `holonic:588-589` reads *"`destroy` sets `until = tick` on every Tenure whose subject or object is the destroyed id, and **destroys nothing else.** It does not cascade into other carriers"* — a rule about which **Tenures** end, silent on which **objects** may be destroyed. And **nothing in this tree destroys a `Rung` or a `Site` at all**: both `exists` rows are producerless (re-measured this session). The cardinality ground is measured: `{harbour: 37, seam: 37}` over 37 settlements, so **many fabrics, one address**; 60 `community` and 211 `hearth` rungs carry **no** fabric, so **one address, no fabric**; and a field on a type is available to every kind of that type, so a `Rung.condition` for `hearth` is a `Rung.condition` for `realm` |
| **five site families, discriminated by which EXISTING table a condition band reaches** | §A.8 | not attacked. `regrowth: 0` rows were attacked and **deleted** — no `regrowth` table exists under `engine/` and nothing would read one |
| **fortification is an `ENCLOSURE` `Site` whose CONDITION IS ITS STRENGTH — bands, not a level — and there is NO siege subsystem** | §A.9 | not attacked |
| **`hold` never reaches a `Site`**, because mandatory single-holdership **deletes the commons** | §A.10.1 | not attacked. The *other* argument for widening — *"it makes `share` computable"* — was **falsified**: `share` was never a field |
| ⚠ **`fort_level` and `facility_tier` are NOT free cuts. Both cuts stay WITHDRAWN** | §A.10.2 | **verified reader by reader**, and the export check is **blocking** |
| **`governance_modes` / `power_bases` are not re-added** | nothing re-adds them | verified |
| **the measurement block reproduces** | §A.2, re-run this session | verified: the census, 38 verb rows / 18 resolvable / 11 effect bodies, 10 producerless `[RES]` rows of 40, `w.crossings` empty in every world any gate executes |

---

# PART A · THE CLAIMS

## A.1 · MATTER AS IT RUNS — every block, in the order `§25` fixes, with what it writes and what it emits

`loop/matter.py` is **296 lines and it is the driver's own body**, not a delegating stub: `loop/driver.py`
ends with `SeasonDriver.matter = matter`, so `inspect.getsource(SeasonDriver.matter)` returns that
source and eight tests read a step's body that way (`matter.py:3-9`). **Any change proposed here is a
change to a function eight tests read as text.** That is stated first because it is the single largest
migration cost in this document and it is invisible from the design side.

The order is not this module's choice. `matter.py:155-160` quotes `#353 §25` and follows it: *"Events
resolve FIRST, then bodies, larders, yield, travel, wear."* The code's actual sequence, opened line by
line:

### A.1.1 · The seven blocks

| # | block | lines | reads | writes, through which gate call | emits |
|---|---|---|---|---|---|
| 0 | **enter** — `w.step = Step.MATTER`, `TRACE.barrier(2)`, `w.discard_caches()` | `:31-35` | — | — | — |
| 1 | **the actorless event channel** — serial, *because it crosses owners* (`S31.1`); *"an actorless event is ONE Event spanning many rungs — sharding it per rung BREAKS `causes[]`, because ONE CAUSE IS ONE ID"* | `:51-53` | the `actorless` argument | appends to `w.log` **by hand** | the Events it was handed |
| 2 | **TERM MATURATION** — *"each maturation is A PERSON'S PAST ACT RIPENING, with `causes[]` pointing at the act that wound the clock"*, and **the only mechanism in the design by which one season's act reaches into a later one WITHOUT anybody acting again** (`:56-59`) | `:65-109` | `w.records`, each `rec.stages` tuple `(due, label, wound_by)`; a **live `hold` whose object is the Record** (`:73-74`) | `rec.matured = True` via `w.write("matured", WriteClass.MATTER, …, record_kind="Record", fieldname="matured", subject=rid, causes=[prior])` (`:106-109`) | **`term.matured`**, one per ripening stage. The id carries `new_draw()` (`world.py:446`), so **N stages ripening in one tick emit N distinct Events** — §A.6.3 rests on exactly that |
| 2a | **and it STOPS if the maker is gone** — `holder is None or holder not in w.persons` → `continue`, with the reason TRACEd verbatim: *"a half-made copy STOPS rather than finishing itself"* | `:73-78` | — | nothing | nothing |
| 3 | **CLAIM CONFIDENCE DECAY** — the third licensed clock | `:123-153` | `w.persons[*].ledger`, `fixtures.claim_decay()` | `c.confidence = after` through the gate (`:150-153`) | `claim.decayed` |
| 3a | ⚠ **and it guards its own no-op:** `after = max(0, c.confidence - decay)`; `if after == c.confidence: continue` — because at `claim_decay_per_season = 0` *"every claim still emitted `claim.decayed` every season while `max(0, …)` changed nothing, so the control arm of the sweep published a decay that did not happen"* | `:147-149` | — | — | — |
| 4 | **LARDERS** — `H-11`: *draw from the containing rung's stores, scaled by weight* | `:164-192` | `fixtures.subsistence_weight`, `world_q.presence(w, rid)` (`:169`) | `r.stores.update(after)` through the gate (`:188-192`), **guarded** by `if any(after[k] != have.get(k, 0) …)` (`:186`) | `stores.changed` |
| 4a | the draw: `draw = {k: wt * len(eaters) for k, wt in weights.items()}` | **`:174`** | — | — | — |
| 4b | the shortfall: `after` (`:176`), `short` (`:177-178`), `if short:` (`:179`) → **`TRACE.note` only** (`:184-185`), closing *"recorded, not acted on (L5: a crossing produces no outcome)"* | `:176-185` | — | **nothing** | **nothing** |
| 5 | **YIELD** — `§25`'s *"only here"* row, in the **same loop** as block 4, per rung | `:193-225` | `SITE_YIELD[site.kind]`, `site.condition`, `condition_scale`, `season_factor` | `(Rung, yield)` (`:214-218`) then `(Rung, stores)` credited (`:221-225`) | `yield.taken`, then `stores.changed` |
| 5a | ⚠ **the SITE's own `rung`, not the rung's `sites` list:** `if site.rung != rid: continue`. The first version read `r.sites`, *"a BACK-REFERENCE NOTHING MAINTAINS — it is empty for every rung in the corpus, so the whole yield step was INERT"* | **`:205-206`**, argued `:197-203` | — | — | — |
| 5b | the scaling: `int(base * (max(0, site.condition) / scale_) * factor)` — **multiplicative**, so a worn place produces less **without a second wear concept** | `:207-209` | — | — | — |
| 6 | **WEAR** — `w._in_parallel_map = True` (`:228`), then over every site: `wear = w.fixtures.wear(s.kind)` with **NO SILENT DEFAULT — unregistered kind raises** (`:233`) | `:228-246` | `fixtures.wear`, `band_floors` (`:230`) | `s.condition = max(0, s.condition - wear)` through the gate (`:242-246`), chained to `last_emission_of("condition.worn", s.id)` | `condition.worn` |
| 7 | **BAND CROSSINGS** — `S12.1/L5`: *A BAND EDGE CROSSING IS AN EMISSION, NOT A WRITE* | `:252-277` | `floors = floors_all.get(s.kind, {})` (`:260`) | **nothing** | **`condition.band_crossed`**, built by hand at `:267-270`, appended to `w.log` and to `emitted` at `:271` |
| 7a | the predicate — **DOWNWARD ONLY**: `if before >= floor > s.condition` | **`:262`** | — | — | — |
| 7b | ⚠ **and a SECOND carrier of the same fact:** `w.crossings.append((s.id, verb, before, s.condition, ev.id))` | **`:272`**, the list at `world.py:176` | — | — | — |
| 8 | **drain** — `emitted.extend(w._emitted_by_write)`, `clear()`, `w.frozen = True` (`S26.2`) | `:292-296` | — | — | everything the gate emitted this barrier |

**Three properties of that table are load-bearing on everything below.**

1. **Blocks 4 and 5 share one loop** (`for rid in sorted(w.rungs)` at `:167`). The larder draws and
   the yield credits are interleaved **per rung**, not in two passes. §A.3.3 shows why that is safe
   today and unsafe the moment the draw ascends.
2. **Block 7 writes nothing and decides nothing**, deliberately, on `L5`'s rule. So does block 4b.
   **The difference is that block 7 EMITS and block 4b does not** — and an emission is what a person
   can be asked about. That asymmetry is the whole of §A.4.
3. **`matter.py` touches no `Record` beyond `stages`/`matured` and no `Proposition` at all.** Opened
   at `:30-296`: true today, and **it stays true** under this document. MATTER reads no policy. That
   is sibling `02`'s constraint and this file does not weaken it.

### A.1.2 · The decision row is STALE about larders and yield, and this document corrects it

`matter.py:46-50` records the barrier's decision. Its `not_implemented` list reads, verbatim:

```
not_implemented=["the death cascade (S31.1 exception 2)",
                 "bodies, larders, yield, travel (S25's other rows)"])
```

⚠ **`not_implemented` is at `:49-50`, not `:50-51`.** Round one `02` §A.6.1 and the round-two plan
both cite `:50-51`; the line drifted. Repaired in the APPENDIX.

> ### RULED: **THE ROW IS FALSE ABOUT TWO OF ITS FOUR MEMBERS. LARDERS AND YIELD BOTH RUN. THE ROW BECOMES `not_implemented=["travel"]` IN THE SAME COMMIT THAT LANDS ITEM 3b, AND NOT BEFORE.**
>
> Larders run at `:164-192` and yield at `:193-225`; **MEASURED, one season of `build_realm(0)`:
> `yield.taken` 37, `stores.changed` 37.** A decision register whose row names code as unwritten
> while the code runs is the defect this file's own header calls out at `:41-45` — *"a decision
> register whose most frequent row names code never written is worse than no register"* — arriving
> from the other direction.
>
> **`bodies` and `travel` are TRUE as stated**, and `the death cascade` is true **of MATTER**: the
> cascade exists at `effects.py:415-418` and MATTER cannot reach it. So the row is right about three
> members, wrong about two, and the honest repair is one line — **but it may not be taken until
> bodies actually run**, or the row becomes false in the other direction, which is worse.

### A.1.3 · ⚠ THE GATE DOES NOT REFUSE A NO-OP, AND EVERY MATTER BLOCK GUARDS ITSELF BY HAND

`ARCH` PART D row 5 says the gate refuses `before == after`. **MEASURED FALSE OF THE GATE.**
`World.write` is `world.py:295-471`; `:408` is `before = apply()` and **nothing is compared to it**;
the emission block at `:441-469` fires unconditionally once `emits=` is passed, raising only if
`subject=` is missing (`:420-434`). The refusal that exists is the **fold's**, at
`resolve.py:259-269` — *"AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
SUCCESS"* — and it reads `changed`, which only an `@effect_for` body fills. **MATTER has no effects.**

So `matter.py` guards itself, twice, by hand:

- claim decay: `if after == c.confidence: continue` (`:148-149`), with the sweep's control arm named
  as the reason (`:138-146`).
- larders: `if any(after[k] != have.get(k, 0) for k in after)` (`:186`).

> ### RULED: **THE BODY WRITE CARRIES ITS OWN `if delta == 0: continue`, FOR THE SAME REASON AND CITED TO THE SAME TWO SITES. THIS DOCUMENT PROPOSES NO GATE-SIDE NO-OP CHECK.**
>
> Decided at §0's **step 4 (precedent)**: two siblings in the same function already do it, and the
> third doing it differently is the drift `CLAUDE.md` §8 forbids. A gate-side check would be a
> better design and it is **out of scope**: it would change the emission behaviour of eleven MATTER
> writes and every golden through MATTER, for a benefit this document does not need. Recorded as
> reference, not queued: **`ARCH` PART D row 5 describes a mechanism the code does not have at the
> gate**, and a session that reads the ARCH row and omits the guard ships a fabricated
> `body.changed` every season for every fed person in the world. That is the failure mode, named.

---

## A.2 · THE MEASURED DISCONNECTION

### A.2.1 · The command, and everything it says

```
$ python -m engine.season.harness.populated 2
```

**Re-run 2026-09-17 against the working tree.** Its own output:

```
rungs by kind        {realm 1, duchy 3, territory 17, settlement 37, community 60, hearth 211, person 46}
persons              46   (one per season loop)
buildings inhabited  26   (largest holds 8)
sites                74
after 2 season(s): 814 acts by 46 actors
act subjects         {self 345, another person 157, not a person 312}
claims by source     {firsthand 4425, told_by 8}
```

The matter figures are not printed by that harness, so they are taken by **driving one season on
`build_realm(0)` and reading `Rung.stores`, `Person.body`, `world_q.descendants` and `w.log`** — the
recipe, exactly, because a figure whose command cannot produce it is an unfalsifiable result claim
(`CLAUDE.md` §0.1 pt 3):

```python
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.decision import make_chooser
from engine.season.harness import probes as P
w = build_realm(0); d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
d.season(make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick)),
         question=None, subsistence=P.SUBSIST,
         contest_max_depth=w.fixtures.get("contest_max_depth"))
# then: Rung.stores by kind; p.body per person; world_q.descendants per settlement; Counter(e.kind for e in w.log)
```

**AFTER ONE SEASON:**

```
rungs holding any matter, by kind      {settlement: 37}          — and no other kind, at all
units by rung kind                     {settlement: 4810}
units by matter kind                   {grain 1480, salt 1110, ore 1850, timber 370}   = 4,810
hearths                                211        holding nothing: 211  of 211
sites                                  74         all 74 keyed to a settlement rung
sites with any person present at their rung        0  of 74
rungs with any presence                26         ALL of them hearths
persons                                46         all at body 1000; body_band_penalty 0 for all 46
persons with no live `contain` edge     0
w.crossings                            0
log, all sixteen kinds                 yield.taken 37 · stores.changed 37 · condition.worn 74
                                       claim.deposited 2175 · record.created 69 · proposition.uttered 54
                                       finding.none 85 · finding.made 52 · work.unavailable 38
                                       travel.blocked 23 · news.untold 22 · release.refused 18
                                       transfer.refused 16 · speech.made 13 · news.told 8 · travel.moved 3
                                       site.built 0 · rung.founded 0 · site.restored 0 · site.worked 0
                                       body.changed 0 · person.died 0 · condition.band_crossed 0
```

### A.2.2 · By matter kind, and the arithmetic that produces every figure

The headline is not an observation to be trusted; it is arithmetic, and it is worth doing because
**the arithmetic is what says the disconnection is structural rather than a seed's accident.**

`populated.build_realm` mints one `Site` per producing kind at each settlement
(`populated.py:368-374`, the mint at `:373`), at `condition = condition_scale`. `SITE_YIELD`
(`rosters.yaml:1166-1173`) is `harbour: {grain 40, salt 30}`, `seam: {ore 50, timber 10}`,
`body: {}`. `season_factor` is `1.0`; `condition_scale` is `1000`. Wear runs **after** yield in the
same barrier, so season 1's yield is taken at full condition:

| kind | per site | sites | per season | measured |
|---|---|---|---|---|
| grain | 40 | 37 harbours | 1,480 | **1,480** ✓ |
| salt | 30 | 37 harbours | 1,110 | **1,110** ✓ |
| ore | 50 | 37 seams | 1,850 | **1,850** ✓ |
| timber | 10 | 37 seams | 370 | **370** ✓ |
| | | | **4,810** | **4,810** ✓ |

And the demand side, from `subsistence_weight` = `{grain: 2, salt: 1}` (`rosters.yaml`, the
`subsistence_weight` table) over 46 persons all at `weight == 1`:

| kind | per eater | eaters | demanded | met | **unmet** |
|---|---|---|---|---|---|
| grain | 2 | 46 | 92 | **0** | **92** |
| salt | 1 | 46 | 46 | **0** | **46** |
| | | | **138** | **0** | **138** |

> ### MEASURED: **138 UNITS OF SUBSISTENCE GO UNMET EVERY SEASON WHILE 4,810 ARE PRODUCED — A SHORTFALL OF 2.9% OF PRODUCTION, MET AT 0%.**
>
> This is the sharpest available statement of the defect and it is sharper than the headline. The
> world is not poor. It is **not connected**: the surplus is 35× the demand, and the demand is met
> zero times.

### A.2.3 · The 13-of-37 split — and it is worse than the headline

`world_q.descendants(w, settlement)` (`:54`) walks the containment tree; counting persons in each
settlement's subtree:

```
settlements                                     37
  with a person anywhere in the contain subtree  13     holding  1,690 units
  with nobody in the subtree                     24     holding  3,120 units
by matter kind, settlements WITH people    {grain 520, salt 390, ore 650, timber 130}
by matter kind, settlements WITHOUT people  {grain 960, salt 720, ore 1200, timber 240}
```

13 × 130 = 1,690 ✓ and 24 × 130 = 3,120 ✓, so the split is exactly the per-settlement yield times the
count — which is the point: **the stores are uniform and the people are not.**

> ### RULED: **THE HEADLINE UNDERSTATES IT. 3,120 OF THE 4,810 UNITS — 65% — SIT AT RUNGS WITH NOBODY IN THEIR CONTAINMENT SUBTREE AT ALL, SO NO WALK OF ANY KIND CAN EVER REACH THEM FROM A PERSON.**
>
> That number is the one that decides what `nearest_store` can and cannot fix. An **upward** walk
> reaches the 1,690 and reaches none of the 3,120 — and it should not: **a settlement nobody lives
> in accumulating grain is not a bug, it is an unpeopled place with a harbour.** What would reach
> the 3,120 is somebody's `transfer`, i.e. a person travelling, which is the game. §A.3.5 measures
> exactly this: the walk closes the 138 and leaves the 3,120 where they are.
>
> ⚠ **And it is a fact about THIS instrument, not about the design.** 26 of 211 hearths are
> inhabited because `populated.py` seats one person per NPC case (46 cases) and `venues.yaml`
> supplies 211 building rows. A world with 211 inhabited hearths would have 37 of 37 settlements
> peopled. **Saying that plainly is the control**: the 13-of-37 figure is a property of a 46-person
> cast on a 211-plot map, and `ED-WR-0011` **ruled** the cast at 46 with **no season-tick
> generation at all** (*"World-gen NPC count, for now, is just the 46 NPCs we built"*, status
> `ruled`, `needs_jordan: false`). So the sparse map is the ruled state and will not fill itself.

### A.2.4 · ⚠ THE LARDER BLOCK FIRES 26 TIMES A SEASON AND WRITES ZERO TIMES

The strongest measurement in this document, because it is the one that shows the step is not merely
under-supplied but **inert**:

```
larder block (matter.py:164-192) fires at        26 rungs   (the 26 inhabited hearths)
                     writes (Rung, stores) at     0 rungs
`stores.changed` in the log                      37         — all 37 are YIELD credits, block 5
unmet subsistence                                138 units
```

Block 4's gate call at `:188-192` is guarded by `:186` — `if any(after[k] != have.get(k, 0) …)`. At a
hearth with `stores == {}`, `have.get(k, 0)` is 0, `after[k]` is `max(0, 0 - amt)` = 0, so **nothing
changed and the guard correctly refuses the write.** The step is not broken; it is **correct and
unreachable**, which is `AX` **ID-13**'s shape read at a step instead of a field (`AX:489`: *"A
column, flag or axis that no resolver consults is not a weak mechanism — it is a mechanism that does
not exist, wearing a schema's clothes"*).

The 185 uninhabited hearths never enter the block at all: `if eaters and weights` (`:170`) is false.
And the 37 settlements never enter it either — `world_q.presence(w, rid)` (`:172`) returns only
persons with a live `contain` edge **whose object is that exact rung**, and all 46 persons' edges name
hearths. **Presence is not transitive, by construction, and that is correct** (`presence` answers
*who is here*, not *who is under here*).

### A.2.5 · The diagnosis, observed rather than inferred

> ### RULED: **THIS IS NOT A PLACEMENT BUG AND NOT A CONTENT ERROR. IT IS TWO CORRECT READS OF TWO DIFFERENT RUNG KINDS WITH NO EDGE BETWEEN THEM, AND THE CLAMP IS WHAT HIDES IT.**
>
> - **Yield credits the SITE's own rung.** `matter.py:205-206`: `if site.rung != rid: continue`,
>   then a MATTER write to *that* rung's `stores` (`:221-225`). All 74 sites name a settlement.
> - **Subsistence draws from the rung the eaters are CONTAINED IN.** `matter.py:169`:
>   `eaters = world_q.presence(w, rid)`, then `draw = {k: wt * len(eaters)}` (`:174`) against
>   `r.stores` of **the same** `rid`. All 46 persons are contained in hearths.
> - **The shortfall is clamped away in writing.** `after = {k: max(0, have.get(k, 0) - amt) …}`
>   (`:176`) — the `max(0, …)` is the clamp — and the residue is `TRACE.note`d and dropped
>   (`:184-185`).
>
> **So the defect has exactly one shape: the draw and the credit are keyed to different rungs of the
> containment ladder, and the ladder edge between them is never walked.** Every other reading — a
> missing store, a mis-seated person, a bad `venues.yaml` row, an unset fixture — is refuted by the
> arithmetic in §A.2.2, which reproduces every figure from the rosters.

---

## A.3 · `nearest_store` — THE ANSWER, SPECIFIED COMPLETELY

> ### RULED: **MATTER STAYS WHERE IT IS PRODUCED. IT MOVES ONLY BY `transfer`. EATERS DRAW **UP** THE CONTAINMENT LADDER, AND THE WALK IS THE WHOLE MECHANISM.**
>
> This preserves **`AX-1`** because **a person moves matter and MATTER does not** — `transfer` is an
> act, it is built, and it conserves (`effects.py:437-480`: *"the giver's store goes DOWN and the
> receiver's goes UP… A one-sided transfer ANNIHILATES MATTER"*). It preserves **`AX` `T-c`**
> (`AX:304`) because **nothing new is wound**: the draw is not a new clock, it is the read the
> existing clock already performs, performed one rung higher. And it preserves **`L4`/`L5`** because
> the walk writes no social quantity and produces no outcome — the shortfall still decides nothing;
> it becomes an **emission**, which is a different thing (§A.4).

### A.3.1 · Signature, walk, tie-breaking, and what it may read

```
nearest_store(w: World, rung: str, kind: str) -> Optional[str]
    # RESOLVER-SIDE. World FIRST. Owned by NOBODY. Stores nothing. Caches nothing.
    # engine/season/queries/world_q.py, beside parent_of (:48) and descendants (:54).
    cur = rung
    while cur is not None:
        r = w.rungs.get(cur)
        if r is not None and (r.stores or {}).get(kind, 0) > 0:
            return cur
        cur = parent_of(w, cur)          # world_q.py:48 — the live `contain` edge, 1 parent
    return None                          # the root's store is empty of this kind
```

**Every clause is load-bearing and each is answerable:**

| clause | why exactly this | the alternative refused |
|---|---|---|
| **it returns a RUNG ID, never a quantity** | a Query that returned an amount would be an aggregate crossing a barrier; returning the **address** leaves the arithmetic at the call site, where the write class is already fixed | returning `(rung, amount)` — then two callers could disagree about how much was available, and `AX-4` gives a value one owner |
| **the walk is `parent_of`, not `descendants`** | `parent_of` is **1 parent** by the Tenure table (`holonic:539`, `contain : Rung → Rung`, **1 parent**), so the walk is a **path**, terminates, and needs no visited set | `descendants` — a downward walk would let a duke eat his tenants' grain without moving, which is the broadcast shape `holonic §37.3` forbids one layer down |
| **it terminates at the root** | `parent_of` returns `None` when no live `contain` edge names the rung as subject. The realm has none, so the loop ends. **No cycle is possible**: `World.add_tenure` refuses a `contain` edge that does not strictly ascend `rung_kinds` (`world.py:248-256`, raising `Forbidden` with code `S10`) | a depth cap — a number nobody chose, and `contain_ascends` already makes it unnecessary |
| **`> 0`, not `>= amount`** | the walk finds **where there is any of this kind**; how much it yields is the caller's clamp. A walk keyed on the amount would give **two eaters at one hearth two different answers**, which is arrival-order dependence — the property `resolve.py:530-553`'s sum-then-clamp exists to avoid | `>= need` — first eater walks to the settlement, second walks past it to the territory. Refused |
| **PER MATTER KIND** | `subsistence_weight` is `{grain: 2, salt: 1}` and `matter_kinds` is an **open registry** (`rosters.yaml`: *"It is a type parameter, not an enumeration"*). A rung may hold grain and no salt, and the two must resolve independently | one walk for "any store" — then a granary with grain and no salt answers for salt, which is `AX` **ID-5**'s *"refuse, don't default"* violated (`AX:451`) |
| **it may read `w.rungs`, `w.tenures` (through `parent_of`) and nothing else** | it is resolver-side, so a World is lawful (`holonic §17`'s side column *is* the enforcement). It touches no `Person`, no `Claim`, no `Record`, no `Site`, no fixture | reading `Site`s to prefer a producing rung — that is a second ordering rule, and the ladder is already an order |
| **NO TIE IS POSSIBLE, and that is a property rather than a policy** | at each step there is **exactly one** parent, so the walk visits a **totally ordered** sequence of rungs and the first hit is unique. **There is nothing to tie-break.** `hold_force`'s precedent (`world_q.py:138-145`) is the shape for the case where cardinality could be violated — it **raises** — and here it cannot be | a `sorted()` over candidate stores, or `H-54`'s hash. Neither is reachable |
| **it is NOT cached** | `World.cache_at_barrier` raises inside a parallel map (`world.py:474-476`) and the larder pass runs **serial**, so caching would be lawful — and the walk is `O(depth)` with depth ≤ 7, against a `presence` call that scans every Tenure. **The uncached walk is already cheaper than what it replaces** (§A.3.2) | a memo keyed `(rung, kind)` — it would go stale the moment the first eater draws, because the draw changes `stores` |

### A.3.2 · The draw becomes PER EATER, and `Person.weight` finally reaches a reader

Block 4 today (`matter.py:167-192`) iterates **rungs** and multiplies by a headcount:

```python
for rid in sorted(w.rungs):                     # :167   — 329 rungs
    eaters = world_q.presence(w, rid)            # :169   — scans every Tenure, per rung
    draw = {k: wt * len(eaters) for k, wt in weights.items()}   # :174 — len(), NOT weight
```

It becomes an iteration over **eaters**:

```python
home = world_q.home_of(w)                        # world_q.py:150 — ONE Tenure scan, {person: rung}
for pid in sorted(w.persons):                    # sorted: the write order must be deterministic
    p = w.persons[pid]
    at = home.get(pid)
    if at is None:
        continue                                 # a person with no live `contain` eats nowhere
    for k, wt in sorted(weights.items()):        # sorted: per-kind write order, deterministic
        need = wt * p.weight                     # ⭐ Person.weight, carriers.py:376
        src  = nearest_store(w, at, k)
        ...
```

**Four consequences, each measurable:**

1. **`Person.weight` reaches the reader the write matrix says it has.** `write_matrix.yaml:217-223`'s
   own `by:` cell claims *"H-11's subsistence default reads it ('scaled by weight'), so every season
   touches it"* — and `matter.py:174` reads `len(eaters)`. **The matrix row's justification is
   false today** and this makes it true. A cohort at weight 200 eats for two hundred, which is
   `AX` **T-l**'s whole point (*"A cohort is a `Person` at weight > 1, never a subclass"*, `AX:425`).
   MEASURED: all 46 persons at `weight == 1`, so **this changes no number in the populated world and
   changes the model** — the honest form, stated rather than sold.
2. **`home_of` replaces 329 `presence` calls with one Tenure scan.** `home_of` exists precisely
   because *"four sites had rolled it by hand"* (`world_q.py:150-170`) and it is the **inverse** of
   `presence`. This is the fifth caller and it is the one the docstring's list was missing.
3. **The 185 uninhabited hearths and the 37 settlements simply do not appear.** There is no rung loop,
   so there is no `if eaters` to be false 303 times.
4. **A person with no live `contain` edge is skipped, not defaulted.** MEASURED: 0 of 46 today. The
   skip is `AX` **ID-5** — refuse, don't default — and it must be a `TRACE.note`, not a silent
   `continue`, for the same reason `:184-185` is.

### A.3.3 · ⚠ THE LARDER PASS MUST SPLIT FROM THE YIELD PASS, AND THIS IS FORCED RATHER THAN CHOSEN

Blocks 4 and 5 share one loop over `sorted(w.rungs)` (`matter.py:167`). **Today that is safe**: the
draw reads `r.stores` of the *same* `rid` the yield is about to credit, and the draw happens first in
the body, so no rung eats what it has not produced.

**The moment the draw ascends, it is unsafe.** A hearth `b_x` sorts before its settlement `set_x`;
under a shared loop the hearth's eater draws at `nearest_store` → `set_x`, whose yield has **not yet**
been credited — correct. But a hearth whose id sorts *after* its settlement draws from a store the
same loop **already topped up this season**. Half the world would eat last season's grain and half
would eat this season's, decided by `_slug()`.

> ### RULED: **BLOCK 4 BECOMES ITS OWN LOOP, COMPLETING BEFORE BLOCK 5 BEGINS. `§25`'s ORDER — *"larders, yield"* — IS THEN OBEYED LITERALLY RATHER THAN PER RUNG, AND THE EXISTING TEST GETS STRONGER RATHER THAN WEAKER.**
>
> `engine/season/tests/test_season_shape.py:4711`,
> `test_w8_matter_draws_before_it_produces_which_is_353s_stated_order`, asserts on the **emitted
> order** and not on the source — *"Asserted on the EMITTED ORDER rather than on the source, because
> the source is what a reader checks and the log is what ran"* — and its assertion is
> `s_evs[:1] == ["stores.changed"]` for the one rung `S` that both draws and produces. **Splitting
> the passes keeps that true and makes it true globally:** every larder `stores.changed` precedes
> every `yield.taken`. The test stays green and its claim widens from *"rung `S` drew first"* to
> *"the world drew first"*.
>
> **What it costs:** one more pass over `w.rungs`-worth of work, and a second `last_emission_of`
> lookup per rung that both draws and yields (because `stores.changed` now fires twice for such a
> rung in one season, in two passes instead of two adjacent statements). That second emission
> already happens today and is already handled: `world.py:436-446` records that the draw ordinal
> was added to the emission id *precisely* because *"MATTER's larder draw and its yield credit both
> write `(Rung, stores)` and both emit `stores.changed` for the same rung in the same season"*.
> **The mechanism that makes the split safe was built for the interleaved version.**

### A.3.4 · What the walk does NOT do — five refusals, each with its reason

| refused | why |
|---|---|
| **it does not move matter** | the draw is a `(Rung, stores)` MATTER write **at the rung the walk found**, which is that rung's own store falling. **Nothing crosses a `contain` edge.** A tax that collects itself is the fourth clock `AX` **T-c** forbids and **`AX-5`** closes the list against (`AX:151`, *"you cannot bribe silt"*) |
| **it does not give a hearth a store** | no hearth gains a `stores` entry, now or later. The 211 hearths hold nothing after this change **and that is correct** — a household's larder is the plot's, and the plot's parent is where the harvest is |
| **it does not deliver** | there is no delivery act, no delivery queue, no `delivered()` Query. Round one proposed `delivered`/`demanded`; both are **withdrawn** and neither was built |
| **it does not reach a sibling** | the walk is strictly upward. A settlement with a full granary cannot feed the settlement next door; somebody must `transfer`. **That is the game** |
| **it does not prefer, rank, or ration** | there is no priority order among eaters. The order is `sorted(w.persons)`, which is deterministic and **arbitrary on purpose**: a ration order is a policy, policy is a `Record` a person issues, and **MATTER reads no policy** (§A.1.1 property 3). Whoever sorts first eats first, and §C.4's `MW-L−2` names that as the loop's own noise source |

### A.3.5 · The counterfactual, as ARITHMETIC — and it is honest about what it proves

Replaying the per-eater draw against the measured season-1 stores, **by computation, not by
execution** (nothing here runs; grade `paper`):

```
COUNTERFACTUAL, arithmetic over the measured world:
  met                        {grain 92, salt 46}  = 138 units      (today: 0)
  unmet                      {}                   = 0              (today: 138)
  rungs whose stores fall    13                                    (today: 0)
  persons whose full subsistence is met            46 of 46         (today: 0 of 46)
  units still sitting at settlements with nobody in subtree  3,120  (unchanged, and correctly so)
```

> ### RULED: **THE WALK CLOSES THE 138 AND LEAVES THE 3,120. BOTH HALVES ARE THE DESIGN WORKING.**
>
> And the finding that matters more than either: ⚠ **on THIS world the walk leaves the body chain
> UNOBSERVABLE.** 13 settlements yield 130 units a season each against a maximum draw of 24
> (`2×8 + 1×8` at the largest building's 8 residents). **The populated world is a surplus world by
> a factor of five**, so after item 3a lands, **`body.changed` would still be 0** and §A.4's entire
> chain would sit unexercised in a green suite. A session that lands 3a, measures 46-of-46 fed, and
> concludes the demographic loop works would be measuring the wrong half of itself — exactly
> `CLAUDE.md` §0.1 pt 3's *"X works today → open the CALL SITE, not the declaration."*
>
> **So item 3b's falsifier needs a world where the store runs out**, and the instrument for that is
> already in the tree and already declared: `site_yield`'s **`none` sweep arm**
> (`rosters.yaml:1150`, `sweep: [declared, uniform, none]`), whose own note says *"`none` IS THE
> CONTROL ARM, not a third opinion: with every cell zero the economy has no source, every store
> depletes monotonically, and `W8`'s own proof clause must fail. A sweep whose control arm cannot
> break the claim is not a control"* — and the loader **refuses an all-empty table as a default**
> (`fixtures.py:137-144`) so the control cannot ship. `MW-4` is built on that arm, with the
> `declared` arm as its control.

---

## A.4 · THE SHORTFALL CROSSES THE GATE — the chain, act by act

Five acts, in order, all inside MATTER's **serial** section (before `w._in_parallel_map = True` at
`matter.py:228`) — because `matter.py:37-40` already declares that the death cascade belongs there:
*"the EVENT CHANNEL and the DEATH CASCADE run SERIALLY, BEFORE the parallel section, because both
CROSS OWNERS (S31.1)."* **The placement is the file's own ruling, followed rather than chosen.**

### A.4.1 · ACT 1 — the shortfall becomes a fraction, and the fraction is the ration

Per eater, summed over matter kinds:

```
need = Σ_k  weights[k] × p.weight                     # what this body is owed this season
met  = Σ_k  min(need_k, stores[nearest_store(w, at, k)][k])    # what the walk actually delivered
ration = met / need                                    # ∈ [0, 1];  need > 0 always, since weights is non-empty
```

> ### RULED: **THE WEIGHTS ARE ALREADY THE RELATIVE IMPORTANCE, SO THE RATION IS A RAW UNIT SUM AND NOTHING IS WEIGHTED TWICE.**
>
> `subsistence_weight` is `{grain: 2, salt: 1}`, and its roster note is explicit that the weights are
> the registry's statement of what a body needs. Summing **units** therefore already applies them:
> grain counts twice because two units of it are owed. A second weighting inside `ration` would be
> two ladders for one quantity — an **S** defect by `CLAUDE.md` §0.06's *"calculations consistent in
> methodology with siblings"*. Decided at §0's **step 5**.
>
> ⚠ **And a kind with no weight is not in the sum at all**, which is `matter.py:171-173`'s existing
> rule read here: *"A kind with no weight RAISES rather than drawing nothing… so the loop is over
> the WEIGHTS, which is the registry, not over whatever the larder holds."* The loop stays over the
> weights.

### A.4.2 · ACT 2 — the body write, SIGNED, and it is one number for both directions

```
delta = int(body_step × (2 × ration − 1))                      # ration 1 → +step;  0.5 → 0;  0 → −step
if delta == 0:  continue                                        # §A.1.3 — the gate refuses no-ops nowhere
before = p.body
w.write("body", WriteClass.MATTER,
        lambda p=p, d=delta: setattr(p, "body",
            max(0, min(w.fixtures.get("condition_scale"), p.body + d))),
        record_kind="Person", fieldname="body", driver="Event",
        emits="body.changed", subject=pid, causes=[prior])
```

| element | why it is exactly this | citation |
|---|---|---|
| `WriteClass.MATTER` | the row is `class: "MATTER/ACTS"`; MATTER is the motion **`AX-5`** names second (*"MATTER, **BODIES**, and the fading of memory"*) | `write_matrix.yaml:161-167`; `AX:151` |
| `record_kind="Person", fieldname="body"` | the gate is keyed on `(kind, field)` — *"it was keyed on `thing`, and that is defect D1 in one line: `(Person, convictions)` rode on `stance`'s row, so a real gap became a PASS"* | `world.py:317-321` |
| `emits="body.changed"` | the row **declares** it, and the gate refuses a MATTER write that names no declared kind **and** one the row does not declare, in both directions | `world.py:396-406`; row at `:167` |
| `subject=pid` | the gate raises `Forbidden` if `emits` is passed without `subject` — *"the fallback was `subject or thing`, and `thing` is a human label… which is exactly the value that made every site's wear emit under the subject `"condition"`, so `last_emission_of` never matched and the clock re-rooted every season"* | `world.py:420-434` |
| `causes=[prior]` | the body is a **licensed clock**, and *"a clock chains to itself"*: `prior = w.last_emission_of("body.changed", pid) or ROOT`. `[ROOT]` is for the campaign seed and a licensed clock's **genuine first** emission only, so the `[ROOT]` count stops growing after season 1 — `W4`'s stated proof | `matter.py:234-239`; `world.py:447-453` |
| `max(0, min(scale, …))` | **the same clamp expression as `resolve.py:549`**, character for character in shape. Integer addition is associative and commutative, so it is order-independent **as a fact** (`S32/S48`), which is what lets a future second writer of the body commute with this one | `resolve.py:538-553` |
| `if delta == 0: continue` | §A.1.3. Without it every fed person at full body emits `body.changed` every season — a fabricated emission, at 46 per season in the measured world, published into every co-located ledger by WITNESS | `matter.py:148-149`, `:186` |
| `int(...)` truncation | `body` is a **fixed-point int on `condition_scale`**, as `carriers.py:385-392` argues at length: *"`condition_scale`, not a literal 1000: a person at full body is at the top of the same fixed-point scale `Site.condition` uses… A bare 1000 here would be a second, silent copy of that scale"* | `carriers.py:392` |

> ### RULED: **THE BODY MOVES IN BOTH DIRECTIONS BY ONE SIGNED STEP, AND THE FIXED POINT IS HALF RATIONS. `body_step` IS THE ONLY NUMBER.**
>
> **Why signed rather than falling only, and this is the load-bearing design choice in §A.4.** A
> fall-only body is a **ratchet**: one famine season narrows a person permanently, and over enough
> seasons everyone in the world is dead regardless of surplus. That is `AX` **ID-16**'s named defect
> — *"A model in which every loop is negative CONVERGES"* (`AX:544-548`) — and it is the *exact* shape
> `hole_register.yaml:1425-1432` files as `H-105`: *"SITE CONDITION IS A SEVERED LOOP, NOT A DAMPING
> ONE… A loop with one arm cut is a RATCHET wearing a loop's clothes."* **Building the body as a
> ratchet would be shipping `H-105` a second time, in the carrier next door.**
>
> **Why one number and not two.** `delta = body_step × (2·ration − 1)` maps ration `[0,1]` → delta
> `[−step, +step]` with its zero at `ration = 0.5`. So **half rations hold you where you are**, full
> rations mend you at the rate starvation wastes you, and the fixed point is a **derived consequence
> of one fixture** rather than a second authored number. The alternative — fall by the shortfall,
> rise by a separate `body_recovery` — is two numbers for one ladder and an **S** defect.
>
> **Why this is not a fourth motion.** It is **one** write on **one** row of **one** licensed motion.
> `(Rung, stores)` already moves in both directions at MATTER in this same function — down at
> `:188-192` (larder) and up at `:221-225` (yield) — so a MATTER quantity with two signs is the
> file's own precedent, not a new licence. Decided at §0's **step 4**.
>
> **`body_step` is INJECTED, DECLARED and SWEPT** (`AX` **ID-6**, `AX:452`). The build item that
> lands it mints its `engine/season/hole_register.yaml` row with `sweep: [declared, halved, doubled]`
> — the same three points `band_floors` carries (`rosters.yaml:1179`) — and the injection site is
> `engine/season/data/fixtures.py`'s `DEFAULT_FIXTURES`, beside `condition_scale` (`:160`).
> **This document proposes the site, the shape and the arithmetic of every arm. It proposes no ruled
> number, and §A.4.6 shows the arm at which the design breaks.**

### A.4.3 · ACT 3 — the band crossing, on `band_floors["body"]`, and **NOT** on a new cell set

The crossing block is `matter.py:252-277`. It is written inline against `s` (a Site) and its predicate
is `if before >= floor > s.condition` (`:262`) over `floors_all.get(s.kind, {})` (`:260`).

```
_crossings(w, subject_id, floors, before, after, cause_ev_id) -> list[Event]
    # engine/season/loop/matter.py — module-level, factored verbatim from :252-277.
    out = []
    for verb, floor in sorted(floors.items()):            # sorted: deterministic emission order
        if before >= floor > after:                       # the predicate, unchanged, DOWNWARD ONLY
            ev = Event(id=H(w.world_seed, w.tick, subject_id, f"crossing:{verb}"),
                       kind="condition.band_crossed", subject=subject_id, changes=[],
                       causes=[cause_ev_id] if cause_ev_id else [ROOT], emitted_at=w.tick)
            w.log.append(ev); out.append(ev)
            TRACE.event(ev.id, ev.kind, ev.causes)
        ...
    return out
```

Called **twice**: once per site with `floors_all.get(s.kind, {})` and the wear Event as cause, once per
person with `floors_all["body"]` and the `body.changed` Event as cause. **One helper, two callers, one
predicate, one Event kind, one table.**

> ### RULED: **PERSONS CROSS `band_floors["body"]` — THE CELL SET THAT ALREADY EXISTS, IS ALREADY DECLARED TO BE `(Person, body)`'s, AND IS ALREADY READ PERSON-SIDE BY LIVE CODE. NO `band_floors.person` IS ADDED, AND THIS IS A DEPARTURE FROM THE ROUND-TWO PLAN.**
>
> The plan (§2.3) specifies *"a NEW `band_floors.person` cell set (`{able: 500, failing: 100}`)"* and
> warns that `band_floors.body` is *"the SITE kind `body`… **not** a person's body; the proposal must
> not conflate them."* **Re-opened this session, the tree says the opposite of the warning, in three
> places:**
>
> 1. `rosters.yaml:814-815`, the `site_kinds` roster's own note: *"⚠⚠ `body` IS NOT A SITE. It is
>    `(Person, body)`'s band row, here because `band_floors` keys on THIS roster and `H-38` ruled
>    `Site.condition` is the model — **no second scheme.**"*
> 2. `decision/budget.py:64-75`, **live, person-side, in the loop**:
>    `body_band_penalty(p, fx)` = *"How many bands `p`'s body has fallen below the top, on
>    `band_floors["body"]`… `H-38` closed with `the answer is YES — Site.condition is the model`, and
>    this is that closure SPENT: the same floors table, the same 'a band is a floor you are at or
>    above' reading, one kind lower. **A second band scheme would have been the invention `H-38` was
>    closed to avoid.**"* Its body is `sum(1 for f in sorted(floors.values(), reverse=True) if p.body < f)`.
> 3. `hole_register.yaml:793`, `H-70`'s own cite: *"⚠ THE BAND TABLE IS NOT INVENTED: `band_floors`,
>    `body` row, already existed for the site gate, so this spends `H-38`'s closure… rather than
>    adding a second band scheme."*
>
> **And a `person` key would REFUSE AT LOAD.** `band_floors` declares `keys: [site_kinds]`
> (`rosters.yaml:1180`) and `fixtures.py:110-123` validates it **in both directions**: a table keyed
> past the roster raises `Forbidden`; a roster member with no row raises `Ungraded`. So
> `band_floors.person` raises unless `person` joins `site_kinds` — which then demands a
> `wear_per_season.person` row and (one direction, `:124-129`) permits a `site_yield.person` row.
> **Three coordinated data edits, to build a second ladder for a quantity that already has one.**
>
> Decided at §0's **step 4 (precedent, `H-38`, stated at three sites)** and **step 5 (architecture:
> the loader refuses it)**. **Cost to the plan's ledger: `band_floors.person` was counted 0 (content),
> so the count does not move; what moves is that three data edits and an S defect are avoided.**

⚠ **THE RESIDUAL HAZARD, NAMED RATHER THAN GLOSSED, BECAUSE IT IS REAL AND IT IS LIVE.** `body` is
simultaneously (a) a member of `site_kinds` and (b) the person-body band row. And **a `Site` of kind
`body` is genuinely constructed**: `engine/season/harness/headless.py:64` builds
`Site("scriptorium", "hearth_ostvik", "body", …)`. So in that one harness world the *same four cells*
serve a fabric's use-bands and a person's health-bands, and the site reading fires. That is a
`CLAUDE.md` §4 **idempotence** hazard — one row, two meanings, read cold. **The clean repair is to
give `band_floors` its own key roster instead of borrowing `site_kinds`; it is NOT taken here**,
because it changes a loader invariant for zero game consequence and this document's deliverable is
not loader hygiene. Recorded as reference, with its falsifier at `MW-9`. **A session that reads
`band_floors.body` as "the scriptorium's bands" has met the hazard.**

### A.4.4 · ACT 4 — what the crossing ALREADY COSTS, and this is the N-line

`body_band_penalty` is not proposed. It is **called every scene round of every season**:
`deliberate.py:116-117` →

```python
ask_budget = lambda p=p, v=v: max(0, decision.budget(p, v, k_budget, w.fixtures) - self._spent.get(p.id, 0))
```

and `budget()` at `budget.py:58-62` is `b = k + offices × budget_office_bonus`, then
`b -= body_band_penalty(p, fx)`, then `b -= len(p.travel_leg) × budget_leg_penalty`, returning
`max(1, b)` — with the floor's reason stated in place: *"a wounded duke gets fewer scenes, and a dying
one still gets one, because a budget of 0 would delete the person from the season silently rather
than narrowing them (S26.3's triage is the point)."*

**MEASURED: `body_band_penalty` returns 0 for all 46 persons, because all 46 sit at `body == 1000`.**

> ### RULED: **THE CONSEQUENCE OF STARVATION IS ALREADY BUILT, ALREADY WIRED INTO THE LOOP, AND HAS NEVER HAD A NONZERO INPUT. THIS DOCUMENT SUPPLIES THE INPUT AND NOTHING ELSE.**
>
> That is the N-line and it is the strongest one available: **cut the body write and a live, wired,
> tested mechanism in the decision layer remains permanently dead.** `AX` **ID-13** (`AX:489`) is the
> law it fails today — *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED"* — read from
> the reader's side: the reader exists and the **writer** does not.
>
> And the consequence is **`L5`-clean**. `matter.py:274-277` records the alternatives the crossing
> block refused, verbatim: *"write the consequence directly (L5 forbids: a crossing MAY NEVER PRODUCE
> AN OUTCOME)"*. The body crossing writes nothing either. What narrows the person is **not the
> crossing** — it is `budget()` **reading `p.body`** at DELIBERATE, one barrier later, person-side,
> with no World. **A threshold changed what could be chosen and produced no outcome**, which is `AX`
> **T-b** exactly (`AX:284`).

### A.4.5 · ACT 5 — death at zero, and `World.remove_person`

`_eff_kill`'s cascade is four lines (`effects.py:415-418`):

```python
for t in list(w.tenures):
    if (t.subject == who or t.object == who) and t.live:
        t.until = w.tick
del w.persons[who]
```

with the reason recorded above it: `w.tenures` and not `p.tenures`, because *"`p.tenures` is the
tenures this person is the SUBJECT of… so the old scan could not see an edge ANOTHER PERSON owns that
names the dead one as its OBJECT… `t10`, a live `tie` from `p_low` to `p_mid`, survived `p_mid`'s
death and then DANGLED."*

```
World.remove_person(self, pid: str, cause: Optional[str] = None) -> None
    # engine/season/state/world.py, beside add_tenure (:223, "The ONE writer").
    # The four lines above, verbatim, factored. §15.3: a tenure dies THROUGH the death of what it is
    # over, never beside it — so this is ONE operation and not a cascade a caller sequences.
```

MATTER calls it **through the gate**, on the row that already licenses it:

```python
if p.body == 0:
    w.write("exists", WriteClass.MATTER,
            lambda pid=pid: w.remove_person(pid, cause="subsistence"),
            record_kind="Person", fieldname="exists", driver="Event",
            emits="person.died", subject=pid, causes=[body_ev.id])
```

| element | licence |
|---|---|
| `(Person, exists)` at MATTER | `write_matrix.yaml:189-195` — `steps: [MAT, RES, CEN]`, `class: "MATTER/ACTS"`, `by: "DR-1, D8; bounded by §15.3's causation rule"` |
| `emits="person.died"` | the row declares it: `emits: "`person.died` · `person.individuated`"` |
| `causes=[body_ev.id]` | the death's antecedent is **the body write that reached zero**, not the season and not `[ROOT]`. `H-12` is ruled *"MATTER emits an Event per write so crossings have an antecedent"*, and `world.py:441-469` hands the write's own emission back through `w._emitted_by_write` for exactly this |
| **ONE write, not two** | `(Tenure, until)` is `[MAT]`-stepped and could be written separately. It is not, because `holonic §15.3` says the tenure ends **through** the death: *"a plague that kills the praefect ends his tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT"* (`effects.py:312-315`). `_eff_kill` writes it as one operation and MATTER does the same. §0 **step 4** |
| **deaths are collected and applied after the eater loop**, in `sorted` id order | `del w.persons[who]` mutates the dict the loop iterates. Collect `dead: list[str]` during the loop; apply after it, sorted. This is the same discipline every loop in `matter.py` already uses (`sorted(w.records)` `:65`, `sorted(w.persons)` `:124`, `sorted(w.rungs)` `:167`) and the reason is stated at `world.py:439-440`: *"the write order is deterministic (every loop here is sorted) and the counter follows it"* |

> ### RULED: **ONE CASCADE, TWO CALLERS. `_eff_kill` (`effects.py:404-419`) CALLS `World.remove_person` AND ITS BEHAVIOUR IS UNCHANGED BY CHARACTER.**
>
> The falsifier is structural and is `MW-6`: **grep for the cascade and find exactly one site.** Two
> copies of a four-line tenure sweep is `CLAUDE.md` §8's violation at the smallest scale where it
> still bites, and the bite is named in `effects.py`'s own comment — the version that scanned the
> wrong collection **dangled an edge**, silently, for one season, and was found by a test rather than
> by reading.

### A.4.6 · The arithmetic at all three sweep arms — including the arm where the design breaks

`condition_scale = 1000`; `band_floors["body"]` = `{full_operations: 800, limited: 500,
withdrawal_only: 100}`; `body_band_penalty(p) = |{f : p.body < f}|`. Total famine is `ration = 0`, so
`delta = −body_step` every season. Body after *n* seasons is `1000 − n × body_step`.

| arm | `body_step` | `full_operations` crossed | `limited` crossed | `withdrawal_only` crossed | dead | penalty ladder seen |
|---|---|---|---|---|---|---|
| **halved** | 50 | season **5** (950→750 at n=5… first `body < 800` at n=5, body 750) | season **11** (450) | season **19** (50) | season **20** | 0 → 1 → 2 → **3** |
| **declared** | 100 | season **3** (700) | season **6** (400) | season **10** (0) | season **10** | 0 → 1 → 2 → 3 |
| **doubled** | 200 | season **3** (400 — the first step past 800 is n=3? n=2 gives 600, so season **2**) | season **3** (400) | season **5** (0) | season **5** | 0 → 1 → 2 → 3 |

> ### ⚠ FINDING, AND IT IS STATED RATHER THAN PATCHED: **AT THE `declared` AND `doubled` ARMS THE `withdrawal_only` BAND AND DEATH FALL IN THE SAME SEASON, SO THE LOWEST BAND IS NEVER OCCUPIED FOR A SEASON AND THE THIRD RUNG OF `body_band_penalty` IS NEVER OBSERVED IN PLAY.**
>
> At `declared = 100`: n=9 gives body 100, which is **not** below the `withdrawal_only` floor of 100
> (the predicate is `p.body < f`), so penalty is 2; n=10 gives 0, penalty 3 **and** death. At
> `doubled = 200`: n=4 gives 200 (penalty 2), n=5 gives 0 (penalty 3 and death). **Only the `halved`
> arm gives every declared band a season of its own.**
>
> This is a fact about the **floors** as much as about the step, and the floors are themselves
> invented — `rosters.yaml:1186-1188`: *"⚠ THE FLOORS ARE INVENTED. #353 states that a band edge
> crossing emits and may produce no outcome; it supplies no edges."* **So the two must be swept
> together, and this document says so instead of choosing the number that makes its own arithmetic
> look best.** The falsifier is `MW-5`, it asserts that every declared band is occupied for at least
> one season on the shipped arm, and **it goes RED at `declared`** — which is the point, in the same
> way round one's `BW-3` went red on purpose.
>
> ⚠ **AND NO PACING CLAIM IS MADE ANYWHERE FROM THIS TABLE.** It is arithmetic over two invented
> tables. *Ten seasons of total famine to death* is not a design statement; it is what
> `1000 / 100` equals.

### A.4.7 · The whole chain, as writes, owners and emissions

| # | what is written | by whose act | write class · step | owner | emits | read by |
|---|---|---|---|---|---|---|
| 1 | nothing — `ration` is computed | **nobody** | — | Nobody (a local) | — | act 2 |
| 2 | `(Rung, stores)` down, **at the rung the walk found** | **nobody** — MATTER, `AX-5` motion 1 | `MATTER` · MAT | `Rung` | `stores.changed` | next season's draw; `restore`'s threshold |
| 3 | `(Person, body)`, **signed** | **nobody** — MATTER, `AX-5` motion 2 | `MATTER` · MAT | `Person` | `body.changed` | `body_band_penalty`; act 4; act 5 |
| 4 | **nothing** — `L5` | **nobody** | — | — | `condition.band_crossed`, subject = **the person** | WITNESS's fan-out → a Claim → a question |
| 5 | `(Person, exists)` + every Tenure naming them | **nobody** — MATTER | `MATTER` · MAT | `World.remove_person` | `person.died` | `presence`, `home_of`, `members`, `leaders`, `footprint`, `hold_force`, and `matter.py:73-74`'s works-holder check |
| — | the narrowing of the person's season | **the person, at DELIBERATE, reading their own body** | — | `budget()` | — | `ask_budget` |

> ### RULED: **NOT ONE MATRIX ROW IS EDITED, AND THAT IS THE FINDING RATHER THAN A CONVENIENCE.**
>
> `(Person, body)` is `[MAT, RES]` and declares `body.changed`. `(Person, exists)` is
> `[MAT, RES, CEN]` and declares `person.died`. `(Rung, stores)` is `[MAT, RES]` and declares
> `stores.changed`. **All three already admit a MATTER write and already declare the exact emission
> this chain needs.** The write matrix has been describing this mechanism since it was written; the
> only thing missing is the code. That is `AX` **ID-13** twice over — two declared rows whose MATTER
> half reaches no writer — closed by one block in one function, with **zero schema change, zero new
> table, zero new Event kind and zero new carrier.**
>
> ⚠ **What it DOES move: every golden through MATTER.** The chain adds emissions to the log in every
> world where a store runs short, which changes `World.content_hash()`. `CLAUDE.md` §7 requires a
> re-pin to be declared: **this one is intended, and it is declared here and again in the commit.**
> In the *populated* world at the shipped fixtures it moves **nothing**, because §A.3.5 measures the
> world as a surplus world — so the hash movement is confined to worlds where the walk runs dry, and
> a session that expects the populated hash to move is expecting the wrong thing.

---

## A.5 · `Rung.envelope` IS KEPT — and it is kept for a reason, not by omission

`envelope` is a declared field of `Rung`: it is in `_DECLARED` (`carriers.py:568-569`) and is
initialised to a list in the constructor (`:579`). It has a **matrix row**:
`write_matrix.yaml:287-293` — `(Rung, envelope)`, `steps: [MAT, CEN]`, `class: "MATTER"`,
`social: "false"`, `emits: "`envelope.changed`"`. It is named in **ratified Layer 1**:
`ARCH §B.3`'s `Rung :=` line carries `envelope`. And `loop/census.py`'s own docstring says CENSUS
*"owns `(Person, exists)` on individuation, `weight`, `envelope`"*.

**And nothing production reads or writes it.** MEASURED by `grep -rn envelope engine/ --include=*.py`:
the only sites are `carriers.py:569`/`:579` (the declaration), `census.py:1` (the docstring),
`harness/probes.py:1631-1637` (probe `W9`, which sets `r.envelope = [100, 200, 150, 60]` by hand and
then writes through the gate to prove the row works), `probes.py:1462` (a `law=` string), and
`engine/season/tests/test_season_shape.py:1842`/`:3738` (which list it among rows whose producer is
absent). **CENSUS writes nothing at all**: `census.py:33-38` records
`chose="demand-driven only; generated nobody"` and states that *"Rev 1 called the gate with an
`apply` that mutated nothing, which S30.2 calls 'worse than no gate'; the call is gone rather than
made cosmetic."*

> ### RULED: **`Rung.envelope` IS KEPT, UNWRITTEN, AS `ED-SE-0051`'s CARRIER. THE FIELD IS AN OPEN `ID-13` EXPOSURE AND IT IS HELD OPEN DELIBERATELY, BECAUSE ITS CONSUMER IS A RULING REQUEST AND NOT A MISSING FUNCTION.**
>
> `ED-SE-0051` asks *"THE BOUND ON THE DEMOGRAPHIC LOOP: matter only, or matter plus hearth
> capacity?"* and its own text describes the arm it is bounding: *"P2 ('the bodies clock') as
> specified is bounded only by the larder — a fed hearth's envelope grows until it cannot feed itself
> and P1 ('dearth reaches the body') thins it, which is Malthus."* The envelope **is** the thing that
> would grow. `proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md:142-150`
> is where that arm is specified, and it starts from exactly this row.
>
> **So this document builds P1 and does not build P2.** The body write (§A.4.2) **is** *"dearth
> reaches the body"*; the envelope's growth is the arm `ED-SE-0051` has not ruled. Deleting the field
> now would delete the ruling request's carrier and force whoever answers it to re-add a field,
> re-add a matrix row, and re-argue `ARCH §B.3`. **That is the cost of the cut, and it is why the
> exposure is cheaper than the deletion.**
>
> ⚠ **This is the one place this document knowingly keeps a field with no production reader**, and
> naming it is the honest form: `AX` **ID-13** says such a field *"is not declared"*, and this one is
> kept anyway, with the reason. The falsifier is `MW-10`: if `ED-SE-0051` is ever ruled **matter-only**,
> the field, its matrix row and CENSUS's claim over it **all become deletable in one commit**, and
> that commit is the artifact that closes this exposure.
>
> ⚠ **AND `ED-WR-0011` HAS ALREADY NARROWED WHAT THE ENVELOPE COULD MEAN, which matters to whoever
> answers RR-2.** It is **ruled** (`registers/editorial_ledger_wr.jsonl`, second row, status `ruled`,
> `needs_jordan: false`), Jordan verbatim: *"World-gen NPC count, for now, is just the 46 NPCs we
> built. We will return much later."* Its Option A, which the ruling took, reads: *"A CLOSED AUTHORED
> CAST. World-gen seeds N persons from an authored roster; there is **no season-tick generation at
> all**. Everyone who will ever matter exists at tick 0 and **the cast only shrinks (AX-5 motion 2,
> bodies)**."* So **the growth arm of the demographic loop is ruled absent today and the shrink arm is
> what this document builds.** `ED-SE-0051` is therefore **not gating** — nothing waits on it — and
> §A.11 says what that does to the recommendation.

---

## A.6 · A `works` IS A `Record` — the full lifecycle

> ### RULED: **THERE IS NO `undertake` VERB, NO `build`, NO `repair`, NO `raze`, NO `garrison`, NO `convert` AND NO BUILD QUEUE. A `works` IS A `Record` KIND WITH ACT-DECLARED STAGES, OPENED BY THE `create_record` THAT ALREADY RUNS. BUILDING AND REPAIRING ARE ONE ACT AT DIFFERENT BANDS.**
>
> Carried from round one `02` §A.4, which the pessimistic pass did not break. Cited to `ARCH §A.3`
> row 11 (*"`Petition`, `Dispensation` … **kinds of `Record`**"*) and `ARCH §B.4`/`§B.5`'s synthesis
> call that folded two kinds in *"with no new rows"*, extended to `works` on the same grounds;
> `AX` **ID-12** (`AX:454`) makes the kind a **data row**.

### A.6.1 · The field usage, key by key — every field of `Record` accounted for

`Record` is `carriers.py:422-445`: `id, rung, kind, forgery_quality, subject_matter, ttl, stages,
matured`.

| field | a `works` uses it as | citation / consequence |
|---|---|---|
| `id` | the works' identity. **`hold : Person → Record` names it**, which is how a works has a master | `holonic:538` |
| `rung` | **where the works is kept** — the rung whose records it is among. Set by `_eff_create_record` from `d.get("rung") or a.actor` (`effects.py:285`). For a works this is the plot's parent or the actor, and **it is NOT the target**: the target is `subject_matter["at"]` | `effects.py:285` |
| `kind` | `"works"`. A **row** on the NEW `record_kinds` roster (owned by sibling `02`), whose `subject_matter` keys it declares. `_eff_create_record` reads `d.get("kind") or "text"` (`:285`), so **the act names the kind and the default is `text`** | `effects.py:285`; `AX` **ID-12** |
| `forgery_quality` | **0, and it stays 0 for a works.** A forged works is a forged *plan*, not a forged fabric, and nothing in this document reads it. Named so the field is accounted for rather than silently unused | `carriers.py:428` |
| `subject_matter` | **`{plan, at}`** — see §A.6.2. Written **once**, inside `(Record, exists)`; there is **no `(Record, subject_matter)` matrix row**, so it cannot be written through the gate afterwards and **must not be mutated** | `write_matrix.yaml` has `Record` rows for `exists`, `matured`, `stages`, `ttl` and **no** `subject_matter` |
| `ttl` | **the abandonment clock the opening act declares.** `[MAT]`-stepped, decremented every season, and `rosters.yaml:768-784`'s `conditional_emission_rows` names it as the one row whose declared emission (`record.expired`) is **conditional**: *"emitting `record.expired` on every decrement would publish an expiry that has not happened"*. This is `AX` **T-n** (`AX:1165`) exactly — *an end that is not the owner's discretion is declared by the act that opened it* | `carriers.py:430`; `rosters.yaml:782` |
| `stages` | **the TERMS — time, not progress.** A list of `(due_tick, label, wound_by)`. `[RES]`-stepped, `class: ACTS`, `by: "D7 — §13.1: terms are act-declared, never MATTER-advanced"` | `write_matrix.yaml:266-272`; `matter.py:67-70` |
| `matured` | **at least one stage has ripened.** A single bool, Jordan-ruled 2026-09-10 and written at MATTER (`carriers.py:432-445`). **It is NOT per stage** — round one's `ceiling` depended on a per-stage reading and that is why §A.6.3 goes to the log instead | `carriers.py:445` |

> ### RULED: **THERE IS NO `stage` KEY, AND THE ROUND-TWO PLAN'S `{plan, at, stage}` BECOMES `{plan, at}`.**
>
> The plan specifies a `stage` int in `subject_matter`, *"advanced by `work`"*. **Refused, on three
> grounds, and the third is decisive.** (1) `subject_matter` has **no matrix row**, so advancing it
> would be an ungated write on a live carrier — the precise shape `ID-9` refuses (`AX:461`). (2) It
> would be a **second progress ladder** beside `Site.condition`, which is already the fabric's
> progress — an **S** defect. (3) **It is unnecessary:** §A.6.3 shows that *progress* is the
> condition and *permission to progress* is the ceiling, so nothing needs counting. Decided at §0's
> **step 5**. Cost to the plan: **one content key not added**, and `_eff_work` is not touched at all.

### A.6.2 · The four moments, and exactly one new verb

| # | moment | act | eligibility | requires | writes | emits / on refusal |
|---|---|---|---|---|---|---|
| 1 | **DECLARE the works** | **`create_record`** — *exists, RUNS, 69 times a season* | `own` | `—` | `(Record, exists)`, `(Record, stages)`, **and the maker's `hold`** | `record.created` |
| 2 | **RIPEN a term** | *nobody — the clock act 1 wound* | — | — | `(Record, matured)` at MATTER | **`term.matured`**, one per ripening stage |
| 2a | **…and it STOPS if the master is gone** | *nobody* | — | — | nothing | nothing, and a `TRACE.note` naming the reason |
| 3 | **STAKE the plot / RAISE the fabric into being** | **`found`** *(NEW — the one new verb)* | `own`, presence through `requires` | a live `works` naming this target, held by the actor, with `matured` true | `(Rung, exists)` **or** `(Site, exists)` — one earned per act | `rung.founded` / `site.built` / `found.refused` |
| 4 | **BUILD IT UP** | **`restore`** — *row exists, `grade: "ruled"`, NO effect body* | `own`, `presence:<site>` | the site exists and the actor is present at it | `(Site, condition)`, through the summing clamp, **bounded by `ceiling`** | `site.restored` / `restore.refused` |
| — | **WEAR** | *nobody* | — | — | `(Site, condition)` down at MATTER | `condition.worn` · `condition.band_crossed` |
| — | **END IT** | the **`ttl`** act 1 declared (`T-n`), or **`destroy_record`** by its holder (`T-m`, `AX:1154`) | `hold:<record>`, `presence` | — | `(Record, exists)`; every `hold` on it ends (`effects.py:302-305`) | the lapse / `record.destroyed` |

**AND MOMENTS 1 AND 2 ARE ALREADY EXECUTING, WHICH IS THE CHEAPEST THING IN THIS DOCUMENT.**
`_eff_create_record` (`effects.py:263-290`) takes the stages **from the act** — *"THE STAGES COME FROM
THE ACT, NOT FROM A DEFAULT"* (`:267-271`) — and, the part that makes the lifecycle close, **mints the
maker's `hold` in the same act** (`:286-289`): *"S13: possession is a `hold` Tenure owned by the
holder, never a field on the Record. The maker holds what they made until they part with it."*
`matter.py:73-78` then looks that holder up and refuses the maturation when there is none, with the
reason TRACEd verbatim: *"a half-made copy STOPS rather than finishing itself."*

> ### RULED: **A `works` THAT STALLS, IS INHERITED, OR DIES WITH ITS MASTER COSTS **ZERO NEW CODE**, BECAUSE BOTH HALVES OF THAT MECHANISM SHIPPED FOR AN UNRELATED REASON. THIS DOCUMENT SPENDS THEM RATHER THAN BUILDING THEM.**
>
> Both were re-opened this session and both are as quoted. `record.created` fires **69 times** in one
> measured season, each with a `hold` minted. **The best drama generator in the design is already
> running and has nothing to be about.**

### A.6.3 · `ceiling` — DECIDED, off the emission log

Round one left this open: *"⚠ 2026-09-17 NERS pass: `matured stages` has no carrier. `Record.matured`
is ONE bool for the whole Record."* **True, and the repair does not need a per-stage field.**

```
ceiling(w: World, site: Site) -> int
    # RESOLVER-SIDE. World FIRST. Owned by NOBODY. Stores nothing. AX T-a (:255).
    live = [r for r in w.records.values()
            if r.kind == "works"
            and (r.subject_matter or {}).get("at") == site.id
            and hold_force(w, r.id) is not None]          # a works with no master is not a bound
    if len(live) > 1:
        raise Forbidden(f"{len(live)} live works name {site.id}", "S15",
                        law="one works per target — hold_force's cardinality reading, one object up")
    if not live:
        return w.fixtures.get("condition_scale")           # no works: the fabric may be repaired to full
    rec = live[0]
    declared = len(rec.stages)
    if declared == 0:
        return w.fixtures.get("condition_scale")           # a works with no terms bounds nothing
    matured = sum(1 for e in w.log
                  if e.kind == "term.matured" and e.subject == rec.id)
    return w.fixtures.get("condition_scale") * min(matured, declared) // declared
```

| decision | ground |
|---|---|
| **the carrier for "how many stages have ripened" is `w.log`** | `term.matured` is emitted **once per ripening stage** (`matter.py:106-109`, inside the per-stage loop `:67`), and the gate gives each emission a **distinct id** via `new_draw()` (`world.py:436-446`, added because *"MATTER's larder draw and its yield credit both write `(Rung, stores)` … in the same season"*). So N stages ripening in one tick produce N Events and the count is exact |
| **reading the log from a Query is lawful** | `World.last_emission_of` (`world.py:447-453`) already scans `self.log` for a `(kind, subject)` match and is the design's own chaining primitive. This is the same read, counted instead of taken last. §0 **step 4** |
| **`min(matured, declared)`** | the log is append-only and a Record's `stages` list is act-declared, so a later act could in principle shorten it. The `min` makes the ratio total, and the clamp `max(0, min(ceiling, …))` makes the result total at the call site regardless |
| **integer division, `scale × n // d`** | `condition` is a fixed-point int on `condition_scale`; multiply before dividing so a 3-of-5 works reads 600 and not 0. Same discipline as `matter.py:207-209`'s `int(base * (condition/scale) * factor)` |
| **it RAISES on two live works naming one target** | `hold_force`'s precedent, verbatim: *"`hold` is 1 PER OBJECT… S54 item 20's lawful form rests on this cardinality"*, and it **raises** `Forbidden` with code `S15` (`world_q.py:138-145`). A Query that picked one of two would answer *plausibly and wrongly, forever* — `AX` **ID-5** |
| **the `cardinality` conjunct on `found` is what makes the raise unreachable in practice** | `cardinality` is one of the **closed seven** `requires_forms` (`rosters.yaml:1114`), and its `needs:` is `[subject, from, to]` (`:1119`). So the refusal is a **precondition that emits**, not an exception — `AX` **T-g**'s obstruction (`AX:353`), free |

**Where the ceiling binds.** `resolve.py:538-553` already sums every `(Site, condition)` delta across
the fold and clamps **once**, `max(0, min(scale, site.condition + total))` at `:549`, with its own
TRACE recording the refused alternative (*"clamp per delta (arrival-order dependent)"*).

> ### RULED: **THE CEILING IS ONE MORE TERM IN THAT ONE `min`. `scale` BECOMES `ceiling(w, site)`, WHICH RETURNS `scale` WHEN NO WORKS NAMES THE SITE — SO THE EXPRESSION IS UNCHANGED FOR EVERY SITE IN EVERY WORLD TODAY.**
>
> One edit, in one expression, in one owner, and the order-independence is untouched because the
> ceiling is a function of the world and not of the deltas. **And the migration cost is zero for
> existing worlds**: MEASURED, `w.records` holds 69 Records after one season and **none is of kind
> `works`** (the kind does not exist), so `ceiling` returns `condition_scale` for all 74 sites and
> `resolve.py:549` computes the same number it computes today.

**And it makes building and repairing one act at different bands, arithmetically:**

| the same act | reads as | because |
|---|---|---|
| `restore` at condition 0, 1 of 5 terms ripened | **raising the first courses** | the ceiling is 200 of 1000 and the fabric climbs toward it |
| `restore` at 990, 5 of 5 ripened | **repairing wear** | the ceiling is full |
| `restore` on a slighted fabric, 5 of 5 ripened | **rebuilding** | a finished works can always be repaired to full |
| `restore` at 200 with 1 of 5 ripened, again | **refused, and the refusal emits** | the delta clamps to the ceiling, nothing changes, and the fold refuses an act whose effect touched nothing (`resolve.py:259-269`) → `restore.refused` (`verb_table.yaml:463`) |

### A.6.4 · `share` — DECIDED, and the commons is what it protects

`restore`'s formula (`verb_table.yaml:465`) is `Δ = +(1 − condition) × f(degree) × share`. Round one
found the blocker correctly: `share` and `draw_share` are **declared Queries** (`holonic:599-600`)
with no implementation, and `share` was **never a field** — so the argument that widening `hold` to
`Site` would make it computable was false.

```
share(w: World, p: str, site: Site) -> tuple[int, int]     # a RATIO, numerator and denominator
    # RESOLVER-SIDE. Declared at holonic:600. Returns (1, n) where n = how many stand at the fabric.
    n = len(presence(w, site.rung))                        # world_q.py:172
    return (1, max(1, n))
```

> ### RULED: **AN ACTOR'S SHARE OF A FABRIC IS ONE OVER THE NUMBER OF PERSONS PRESENT AT ITS RUNG. IT IS DERIVED FROM A LIVE EDGE, NEEDS NO FIELD, AND IS THE READING THAT KEEPS THE COMMONS.**
>
> **Why not `Site.drawers`.** The field exists (`carriers.py:418`) and is **unwritable through the
> gate** — `write_matrix.yaml` retires the row — so nothing can maintain it. A `share` read off a
> list nothing writes is `AX` **ID-13**'s dead carrier. **And this document DELETES the field**
> (§B.2), which is the object it gives back for the Query it adds.
>
> **Why not 1.** `share = 1` is what mandatory single-holdership would give, and
> `proposals/2026-08-31-ideal/10_SUPERSEDING.md:1275-1279` names what dies: *"**At a commons with
> many drawers, single-act closure is impossible.** One boat among a harbour's forty moves at most a
> fortieth of a quarter of the harbour's condition in a maximum-degree season. **Closure is a
> collective outcome** — many actors, many seasons, crossing a band edge — which is the
> tragedy-of-the-commons shape the mechanism exists to produce: many rational private acts making
> everyone's practice worse, including the actor's."* The same passage records the other arm,
> withdrawn by its own author at `:1280-1282`: at a single-drawer site *"`share = 1`, and one
> Overwhelming season moves a quarter of the condition."* **Both halves must be read together**, and
> `share = 1` is the **special** case.
>
> **DECLARED, DEFAULTED AND SWEPT**, because the *shape* is ruled and the *reading* is not:
> `sweep: [presence_reciprocal, holders_reciprocal, one]`, where `one` is a **real control** — it
> deletes the commons, so a test over a 40-drawer harbour must break under it. A sweep whose control
> cannot break the claim is not a control (`rosters.yaml:1163-1165`, the same argument for
> `site_yield`'s `none`). Falsifier `MW-8`.
>
> **The arithmetic it reproduces.** At a 40-person harbour with headroom 1000 and a degree factor of
> ¼: `Δ = 1000 // (4 × 40) = 6` of 1000 in one Overwhelming season. That is
> `10_SUPERSEDING.md`'s *"a fortieth of a quarter"*, computed rather than asserted.
>
> **It costs 0 added objects**, on round one's own precedent for `capacity`: *"`capacity` is already
> **declared** in the §17 Query roster, so it is an implementation, not an addition."* `share` sits on
> the line above it (`holonic:600`).

### A.6.5 · `restore`'s body — and the third blocker neither round found

```
@effect_for("restore")
def _eff_restore(w, a, res=None) -> dict:
    site = w.sites.get(_operand(a, "site"))                  # effects.py:59 — _operand, NO fallback
    if site is None:
        return {}                                            # the fold emits restore.refused
    headroom = max(0, ceiling(w, site) - site.condition)
    num, den = degree_factor(res.degree)                     # the EXISTING ladder, not a new one
    s_num, s_den = share(w, a.actor, site)
    delta = (headroom * num * s_num) // (den * s_den)
    if delta == 0:
        return {}                                            # nothing to do: refuse, do not report
    return {"site.restored": [site.id]}, {site.id: delta}    # ids earned, and the DELTA
```

**Two decisions and one gap:**

| | |
|---|---|
| **units** | `(1 − condition)` in the formula is the **headroom fraction**, and `Site.condition` is a fixed-point int on `condition_scale` (`carriers.py:412-413`, `fixtures.py:160`). So `(1 − condition)` reads as `ceiling − condition` in fixed point. Multiply first, divide last; the result is an int delta on the same scale as wear's. **Decided.** |
| **`f(degree)`** | **the existing degree ladder, not a new one.** `AX` **T-k** (`AX:418`) is *"One resolver, one degree ladder"*. `_eff_kill` reads its magnitude off the `Resolution` the seam returned (`effects.py:383-403`) and `_apply_write` hands every effect that `Resolution` uniformly (`resolve.py:320-326`, *"EVERY EFFECT TAKES THE RESOLUTION, AND UNIFORMLY"*). `restore` reads `res.degree` the same way. **No new ladder is proposed and none may be.** |
| ⚠ **THE GAP: THE FOLD HAS NO CHANNEL FOR AN ACT'S DELTA AT ALL** | `_apply_write` returns `[StateChange(t, "set", "Act", fld) for t in touched]` (`resolve.py:351`) — `StateChange.delta` is left `None` (the field exists, `carriers.py:75`). The accumulator at `resolve.py:523-525` only collects `ch.delta` when it `isinstance(ch.delta, int)`. **So no act in the tree can contribute a delta, and that is `H-105` in one line:** *"`work` emits `site.worked` while accumulating no delta, which makes site condition a one-way ratchet — wear falls it every season and neither verb that could raise it can. A loop with one arm cut is a RATCHET wearing a loop's clothes"* (`hole_register.yaml:1425-1432`, re-filed `PRODUCER`). |

> ### RULED: **`_apply_write` GAINS A `deltas` OUT-PARAMETER, EXACTLY SYMMETRIC WITH THE `earned` ONE IT ALREADY HAS, AND `_apply_write` STAYS THE FOLD'S SINGLE WRITE SITE. THIS IS +1 AND IT IS COUNTED.**
>
> `earned` was added to `_apply_write` for the same class of reason and its comment says so:
> *"AN EFFECT MAY EARN SOME OF ITS DECLARED KINDS AND NOT OTHERS. A list means *all* of them (the
> original contract, unchanged); a MAPPING `{kind: [ids]}` names which. Without this the fold emitted
> EVERY kind in `emits:` the moment anything changed"* (`resolve.py:338-346`). `deltas` is the same
> shape one field over: the effect may fill it, `_apply_write` puts `delta=deltas.get(id)` on the
> `StateChange` it returns, and the accumulator at `:523-525` picks it up **with no change** because
> it already tests for an int.
>
> ⚠ **THE ALTERNATIVE IS REFUSED ON THE SUITE'S OWN PRINCIPLE.** The cheap route is for
> `_eff_restore` to write the delta onto `a.payload` and have `_apply_write` read it back. **That is
> intent reassignment** — *"any mechanism that rewrites the operands, the verb or the referent of an
> `Act` after `choose` returned it"* — which is **RR-P**'s third forbidden shape, and the `Act`
> dataclass is the actor's content with nothing after DELIBERATE writing it
> (`write_matrix.yaml:72-78`, `(Act[], returned)` is `steps: [DEL]`, *"DELIBERATE writes nothing
> else"*). **Under RR-P**, and stated as *under RR-P* because RR-P is not settled.
>
> ⚠ **What this closes and what it does not.** It closes the **channel**, so `restore` can raise a
> fabric. It does **not** close `H-105` for `work`: `work`'s row carries no `effect:` formula
> (`verb_table.yaml:755-770`), so `work` still accumulates nothing and `site.worked` is still a
> success report for a change that did not happen. **H-105 stays OPEN for `work`, and this document
> says so rather than claiming the row.**

### A.6.6 · The two stalls, designed honestly in both directions

- **TERM-STALL — you cannot hurry mortar.** Matter and hands are present; no further term has
  ripened. `ceiling` is where it was, the delta clamps to 0, and **the fold refuses an act whose
  effect touched nothing** (`resolve.py:259-269`) → `restore.refused`, which is **already on the row**
  (`verb_table.yaml:463`). It is arithmetic, not a cooldown, and there is no timer anywhere.
- **MATTER-STALL — a scaffolding standing empty.** Terms have ripened and the store cannot meet the
  cost. The cost is paid by `transfer` into the works' rung, whose `scalar_threshold` conjunct
  (`verb_table.yaml:732-739`, `of: from`, `scalar: stores`, `key: kind`, `threshold: amount`) fails,
  and `transfer`'s refusal fires. MEASURED: `transfer.refused` **16 times** in one season today, so
  the channel is live. **A fabric sitting visibly below a ceiling it is entitled to reach says so
  every season somebody tries.**

### A.6.7 · The unfinished `works` — five legible causes, inheritance, sabotage, and a thing standing in the world

**None of the five is an error state, each emits something different, and the emissions are the only
way anybody learns which.**

| cause | the mechanism, all of it already present | what a witness sees |
|---|---|---|
| **nobody has the matter** | `transfer`'s threshold refuses | `transfer.refused` |
| **nobody has the hands** | no act was spent; `budget()`'s five scenes are the bound and `body_band_penalty` narrows them (§A.4.4) | nothing — and that is correct: **neglect is not an act and must raise no question** |
| **the terms have not ripened** | `ceiling` frozen | `restore.refused` |
| **the master is dead** | his Tenures take `until` through `World.remove_person`; the works becomes **unheld**; `matter.py:73-78` refuses to mature it and TRACEs the reason | `person.died`, then **the silence of `term.matured`** |
| **the master was replaced by somebody who does not care** | a successor simply never takes the `hold`. The works stands; the fabric stands at whatever condition it reached | nothing, and the fabric is the evidence |

**INHERITANCE.** A works is a `Record` and `hold : Person → Record` is a Tenure, so passing mastership
is **`confer`/`release`/`revoke` on the Record** — verbs that exist, with `_eff_confer`
(`effects.py:93-126`), `_eff_release` (`:130`) and `_eff_revoke` (`:160`) all shipped. Sibling `02`'s
`give` (the H-84 verb) is the co-located hand-over. **Nothing new here**, and the cardinality is
already enforced: `hold_force` **raises** on a second live hold (`world_q.py:138-145`), so there is
exactly one master at a time and `ceiling` can always name him.

**SABOTAGE.** A rival does not need a verb. Three routes, all existing: (1) take the **plot** — `hold`
changes hands and the `found`/`restore` eligibility goes with it; (2) `destroy_record` the works
(`eligibility: ["hold:<record>", "presence"]`), which ends every `hold` on it (`effects.py:302-305`) —
so **only its own master may abandon it**, which is `AX` **T-m** (`AX:1154`); (3) contest the fabric
down, which is §A.9's siege reading: a negative `(Site, condition)` delta through the same clamp with
the sign flipped. **No `raze`, no `slight`, no sabotage verb.**

**AND A RIVAL MAY FINISH WHAT SOMEBODY ELSE BEGAN.** `restore` asks for `own` and presence and **no
office at all** (`verb_table.yaml:450-451`). So a cathedral begun by one faction and brought to full
condition by another's mason is a whole political event **with no special case anywhere**: the first
holds the works Record and therefore sets the ceiling; the second holds nothing, stands there with the
matter, and raises the fabric inside a ceiling his rival controls. **Neither can finish without the
other** — the master's `hold` is what makes MATTER advance the terms (`matter.py:73-74`), and the
mason's presence is what admits the `restore`.

> ### RULED: **AN UNFINISHED WORKS IS A DESIGNED STATE WITH NO ERROR IN IT, AND A HALF-BUILT FABRIC IS AN INDICTMENT OF WHOEVER SHOULD HAVE FINISHED IT — VISIBLE, ATTRIBUTABLE AND CONTESTABLE. NOTHING IN THIS SUBSECTION IS NEW CODE.**
>
> ⚠ **And the one thing it needs that does not exist: a question about the fabric.** `Q3`
> `band_crossed` is the source, its referent is `H-110`'s defect (the referent is the **verb string**,
> `hole_register.yaml:1533-1544`), and sibling `01` owns the repair. **MEASURED: `w.crossings` is
> empty in every world any gate executes**, because every site starts at 1000, wear is 10, and the
> highest floor is `bulk_shipping: 800` — **the first site crossing fires at MATTER pass 21**, while
> CI runs the populated world for one season and the corpus for at most six. **So the works
> lifecycle is unaskable-about until `01` lands and until a floor is crossed, and that is a
> dependency, not a defect of this document.** Stated, not banked.

---

## A.7 · `found` AND `restore` AS THE WORKS' TERMINAL STAGES

### A.7.1 · `found`, completely — one verb, two declared rows, one earned per act

```yaml
- verb:        "found"
  stratum:     "uncontested_material"          # rosters.yaml:138-146 — ORDER IS SEMANTIC
  eligibility: ["own", "presence:<rung>"]      # `own` LEADS. See the refusal note below.
  requires:    "a live works Record naming this target, held by the actor, whose terms have begun to ripen"
  requires_typed:
    all:
      - form:      existence                   # the works exists, as an OBJECT of a named class
        of:        subject
        kind:      Record
      - form:      scalar_threshold            # `Record.matured` — at least one term has ripened
        of:        subject
        scalar:    matured
        threshold: 1
        comparator: ">="
      - form:      cardinality                # one works per target
        of:        subject
  writes:      ["Rung.exists", "Site.exists"]  # TWO declared rows; ONE earned per act
  emits:       ["rung.founded", "site.built"]
  emits_on_refusal: ["found.refused"]
  grade:       "assumption"                    # the VERB is this document's; the ROWS are the tree's
```

```python
@effect_for("found")
def _eff_found(w, a, res=None) -> dict:
    rec = w.records.get(_operand(a, "subject"))
    if rec is None or rec.kind != "works":
        return {}
    plan = (rec.subject_matter or {}).get("plan") or {}
    at   = (rec.subject_matter or {}).get("at")
    if plan.get("as") == "rung":
        rid = f"{at}:{plan['kind']}"                        # deterministic, derived from the plan
        w.rungs[rid] = Rung(rid, plan["kind"])
        w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"contain:{rid}"),
                            rid, at, "contain", since=w.tick))   # world.py:223 — the ONE writer
        return {"rung.founded": [rid]}
    sid = f"{at}:{plan['kind']}"
    w.sites[sid] = Site(sid, at, plan["kind"], condition=0)       # a fabric begins at NOTHING
    return {"site.built": [sid]}
```

| decision | ground |
|---|---|
| **ONE verb, two write rows, one earned per act** | `_apply_write`'s `{kind: [ids]}` mapping was built for exactly this and says so: *"AN EFFECT MAY EARN SOME OF ITS DECLARED KINDS AND NOT OTHERS… Without this the fold emitted EVERY kind in `emits:` the moment anything changed — so `confer` onto an unheld office published `tenure.closed` with nothing closed"* (`resolve.py:338-346`). And the effect **runs once, on the first pair** (`:252-257`), with the other pairs still gated for class and Partition. **Two verbs (`found` and `build`) would be two rows, two bodies and two names for one act at two grains — and round one already ruled there is no `build`** |
| **`own` leads and presence enters through `requires`** | `eligibility: ["presence:<rung>"]` **alone** is declined person-side: `options.py:166-168` TRACEs *"`presence:` eligibility is unevaluable person-side (H-33, the presence index); `<verb>` declines rather than admitting"*. `restore`'s row already carries the fix and states it: *"eligibility is a DISJUNCTION (`own | presence:<site>`) so `own` alone admits, and the precondition is where presence actually binds"* (`verb_table.yaml:460`). **§0 step 4** |
| **`matured` and not "all terms ripened"** | the closed seven `requires_forms` (`rosters.yaml:1114`) reach a field, not a log count, so *"every declared term has ripened"* **cannot be spelled** without an eighth form — and an eighth form *"REFUSES AT LOAD, because an eighth form is a new thing a precondition can ask and that is a design change, not a table edit"* (`:1092-1094`). `Record.matured` is an existing field read by an existing form. **So the plot is staked when the works BEGINS to ripen and the fabric climbs as the rest ripens** — which is the ceiling's job, and is a better design than gating founding on completion: it puts a visible unfinished thing in the world early, which is the whole point |
| **`cardinality`, one of the closed seven** | `rosters.yaml:1114`, `needs: [subject, from, to]` (`:1119`). One works per target, as a **refusal that emits** rather than a queue. `rosters.yaml:1095-1098` records that `cardinality` *"has no typed cell today and that is not an omission… this roster records that the grammar has room for"* it — **this is that room being used** |
| **a new `Site` begins at condition 0** | a fabric that appeared at full condition would make `restore` pointless and would be a built thing nobody built. Condition 0 with a rising ceiling is *"raising the first courses"* (§A.6.3) |
| **the `contain` edge rides inside `(Rung, exists)`** | precedent: `_eff_create_record` mints the maker's `hold` inside `(Record, exists)` (`effects.py:286-289`), and `holonic §15.3` has a Tenure live and die **through** its object. **No new matrix row.** And `World.add_tenure` enforces the ladder: a `contain` edge that does not strictly ascend `rung_kinds` raises `Forbidden`/`S10` (`world.py:248-256`) — so **founding a hearth under a settlement is legal (strict ascent, not adjacency) and founding a duchy under a hearth is not** |
| **`grade: "assumption"`** | the two write-matrix rows are `grade`-bearing tree facts with a `by:` (`W2/H-41`); the **verb** is this document's and is graded honestly. `AX` **ID-6** |

### A.7.2 · What `found` closes, and what it leaves open

> ### RULED: **`found` IS THE PRODUCER TWO DECLARED ROWS HAVE BEEN WAITING FOR, AND IT CLOSES `ARCH §F.20` AND **TWO OF `H-41`'s THREE CELLS** — NOT THREE, AND NOT `H-34`.**
>
> - **`ARCH §F.20`** — *"no stage names a verb that founds a hearth or builds a site… **the world only
>   decays — nothing is ever founded or built.** This is what blocks build step 2."* Closed **when a
>   `rung.founded` and a `site.built` appear in a run's log**, which is `MW-2`'s artifact and is **0
>   today**, measured.
> - **`H-41`** (`hole_register.yaml:462-472`) is `kind: "SCHEMA_ROW ×3"`, `grade: "absent"`, and its
>   `hole:` names **three** cells: *"`(Rung, exists)`, `(Office, exists)`, `(Site, exists)` — founding
>   a hearth, establishing an office, building a site."* This closes the first and third. **The second
>   is sibling `03`'s** (`establish`/`confer`), and `H-41` therefore stays **open at reduced strength**.
> - ⚠ **`H-34` IS NOT PART OF THIS AND THE ROUND-TWO PLAN MIS-CITES IT.** Re-opened:
>   `hole_register.yaml:370-380` is `H-34`, `kind: "NUMBER"`, `owner: "params"`,
>   `hole: "establishment size per office kind"`. **It has nothing to do with the existence rows.**
>   The plan's §6 lists *"H-34/H-41 (the two producerless rows `(Rung, exists)`/`(Site, exists)` gain
>   `found`)"*; the hole is `H-41` **alone**. Repaired in the APPENDIX.
>
> **Left open, and named:** `ARCH §F.18` (upkeep's source) — untouched. `ARCH §F.20a` (**no verb
> writes any `Person` interior field**) — ⚠ **narrowed but NOT closed by this document:** `(Person,
> body)` is a Part D row and `social: "false"`, so it is **not** one of `§F.20a`'s six interior rows
> (`convictions`, `stance`, `scar`, `axis_count`, `coherence`, `beliefs`, all `social: "true"`). A body
> is not a conviction. **`§F.20a` stands entire**, and the consequence it names stands with it: **a
> person who builds visibly cannot move anyone's conviction.** `ARCH §F.20b` — untouched. `H-62`
> (interior writes) — untouched. `H-105` — closed for the **channel**, open for `work` (§A.6.5).
> `H-110` — sibling `01`'s.

---

## A.8 · THE FIVE SITE FAMILIES — roster rows, and the discriminator IS the rule

Carried from round one `02` §A.2, which the pessimistic pass did not break. **The discriminator is not
the fiction: it is which column of which EXISTING table the site's condition band reaches.**

| family | kinds (illustrative) | what its condition gates | the reader column | destruction removes |
|---|---|---|---|---|
| **PRODUCER** | `croft · field · seam · harbour · mill · quarry` | the rung's `yield` at MATTER | `site_yield[kind]` — **exists**, `rosters.yaml:1146-1173`, scaled by `condition/condition_scale` at `matter.py:207-209` | a source of matter |
| **VESSEL** | `granary · warehouse · cistern · byre` | how much the rung may **keep** | a bound on `Rung.stores`, an unbounded `dict` today — **the one genuinely absent reader column** | the bound on a surplus, and the surplus |
| **ENCLOSURE** | `rampart · gate · ditch · tower · keep` | **somebody else's** verb at this rung | `band_floors[kind]` — the mechanism **exists**, `rosters.yaml:1175-1199`; the kind does not | a refusal |
| **HALL** | `moot_hall · guildhall · minster · chapter_house` | whether a sitting may `convene` here | `band_floors[kind]`, read by `convene`'s `requires` | a venue |
| **DWELLING** | `cottage · townhouse · longhouse · barracks` | how many persons this rung may address | `capacity(w, rung)` — §A.11, **gated on `ED-SE-0051`** | the shelter |

> ### RULED: **THE FAMILIES ARE ROSTER ROWS, NEVER CARRIERS, AND THE DISCRIMINATOR IS THE RULE: *A KIND THAT REACHES NO NEW COLUMN IS NOT A NEW FAMILY.***
>
> A bakery that only produces is a **PRODUCER with a different `site_yield` row**. A gatehouse that
> both refuses an attacker and quarters a watch is **two Sites** — an ENCLOSURE at the quarter and a
> DWELLING at a hearth — because it does two things **and they can be lost separately**. Cited to
> `AX` **ID-12** (`AX:454`, *"A closed set lives in data"*) and to `rosters.yaml:809-812`, whose own
> note is the refusal that makes the roster safe: *"Adding a kind means adding a row here; asking
> about a kind that has no row RAISES."*
>
> **THE BASELINE IS TWO, NOT THREE, AND THE ROSTER SAYS SO.** `site_kinds` is
> `[harbour, seam, body]` (`rosters.yaml:816`) and its own note at `:814-815` reads *"⚠⚠ `body` IS NOT
> A SITE."* **So five families replaces an absence rather than enriching a taxonomy** — and §A.4.3
> re-opens the `body` row and finds it doing a **second** job that the note does not mention
> (`headless.py:64` builds a Site of that kind).
>
> **WHAT A NEW KIND COSTS, MEASURED AT THE LOADER RATHER THAN ASSERTED.** `fixtures.py:106-123`
> checks `wear_per_season` and `band_floors` against `site_kinds` **in both directions** — a table
> keyed past the roster raises `Forbidden`, a roster member with no row raises `Ungraded` (*"a wear
> table that returns 20 for an unregistered site kind does not fail — it answers, plausibly and
> wrongly, forever"*). `site_yield` is checked **one way only** (`:124-129`). **So every family lands
> with a `wear_per_season` row and a `band_floors` row or the world does not load**, and a
> `site_yield` row is optional. That is `AX` **ID-5** doing work a convention would not.
>
> ⚠ **AND EVERY NUMBER IN ALL THREE TABLES IS AN INJECTED DEFAULT WITH A SWEEP.** `site_yield` is
> `H-93`, `sweep: [declared, uniform, none]`, with its own *"⚠ WHAT A HARBOUR PRODUCES IS INVENTED"*;
> `band_floors` is `H-08` with *"⚠ THE FLOORS ARE INVENTED"*; `wear_per_season` is `H-07`, all three
> kinds at **10** against `condition_scale = 1000`. **No claim about pacing is made anywhere in this
> document, and none is made here.** The wear-to-restore ratio is not a difficulty slider: it sets
> **where every site in the world sits at rest**, and §C.5 names it as the largest unmeasured number
> the design now depends on.

---

## A.9 · FORTIFICATION — an `ENCLOSURE` `Site` whose CONDITION IS ITS STRENGTH, and **NO SIEGE SUBSYSTEM**

Carried from round one `02` §A.3, unbroken by the pass. Restated here **only** as the three reads,
because that is what makes it cost nothing.

> ### RULED: **A FORTIFICATION IS AN `ENCLOSURE`-FAMILY `Site` WHOSE `rung` IS THE QUARTER IT ENCLOSES. ITS CONDITION IS ITS STRENGTH — BANDS, NOT A LEVEL — AND WHAT IT GATES IS SOMEBODY ELSE'S VERB. ONE RAMPART PER QUARTER, SO A BESIEGER PICKS A QUARTER.**

| # | the read | onto what already exists | the cost |
|---|---|---|---|
| 1 | **THE BATTLEFIELD, wall intact** | `systems/mass_battle/reference/mass_battle_v30.md:543` already carries the row: `| Walls / fortifications | Defender +3 DR; no flanking; Slow cannot advance |` — an **environmental selector**, a terrain row, not a stat. A provider's IN-side calls `verbs(w, enclosure_site, band_floors[kind])` (`world_q.py:133-136`) at the contested rung and passes that row **iff `mans` is in the returned set**. The seam already receives the rung: `contest(w, rung, prize, claimants, …)` | ⚠ **one read inside a wrapper that does not exist.** `mass_battle` has no registered provider, so **this read has nothing to read yet**, and saying otherwise would be claiming a mechanism |
| 2 | **THE CHOKEPOINT — a band refusing a `move`** | `move`'s row is `eligibility: ["own"]`, `requires_typed: {form: contain_path, of: actor, to: to}`, `emits_on_refusal: ["travel.blocked"]`. The typed form is evaluated by `ContainPath` (`engine/season/data/requires.py:254`), and the resolver-side answer lives in **ONE** place: `WorldReader.read`'s `contain.path` branch (`world_q.py:732-737`), today a shared-ancestor test. **The reading adds one conjunct in that one branch.** MEASURED: `travel.blocked` fires **23 times** in one season, so the channel is live | ⚠ **the form cannot name the wall as an operand.** `contain_path`'s `needs:` is `[actor, subject, from, to]` (`rosters.yaml:1118`) — **no `site`** — and `requires_forms` is **CLOSED AT SEVEN**. So the enclosure is read by the predicate off the world, never bound as a cell operand. **That is a constraint the roster imposes, not a workaround**, and it is why this costs one branch rather than an eighth form |
| 3 | **THE SIEGE — a contest grading a NEGATIVE condition delta, and nothing more** | a `contest` at the rung returns a degree the fold grades into a negative `(Site, condition)` delta — **the same channel a repair uses with the sign flipped**, already licensed at `[MAT, RES]`. Several besiegers commute **by construction**: `resolve.py:538-553` sums every delta and clamps **once**, and its own TRACE records the refused alternative (*"clamp per delta (arrival-order dependent)"*) | **no new write class, no new step, no new carrier, no new degree ladder, and no siege object anywhere.** ⚠ And it needs §A.6.5's delta channel, which does not exist — **the same gap, and closing it once closes it for both** |

**A consequence nobody chose, falling out of an ordering that shipped for other reasons.** The strata
are `[movement, binding_decision, contested_physical, uncontested_material, social]` and *"ORDER IS
SEMANTIC HERE"* (`rosters.yaml:138-146`). A siege is `contested_physical`; a repair is
`uncontested_material`. **So a defender cannot patch a breach in the season it opens, and must
pre-invest.**

**A wall's resistance is not a number, and that is why the row asking for one has no answer.** It is
the verbs it removes from the attacker, the verbs it grants the defender, and the seasons it takes to
grade it down through three bands. `AX` **T-g** (`AX:353`, *"Obstruction needs no verb"*) is the
distinction: an obstacle is rolled against, an obstruction is not rolled against at all. **A wall is
an obstruction.** And a garrison is not a troop type: it is `presence(w, ward)` filtered by who is
bound to keep the walk.

**The epistemic half — the band may never be rendered as fact.** A wall's condition is world truth;
what an attacker holds is a `Claim` about it at a confidence that **already decays**
(`matter.py:147-153`). The typed predicate is evaluated against `WorldReader` at RESOLVE and against
`LedgerReader` person-side, and a relation the reader cannot answer returns `UNKNOWN` — *"so an
unimplemented one refuses rather than admitting"* (`requires.py:50-53`). **So a defender who lets the
walls rot and tells everyone they are sound is a play the design supports with no new mechanism**, and
**a fortification's band is rendered as the viewer's own estimate or not at all.**

---

## A.10 · HOLDINGS — what may never be held, and two cuts that stay WITHDRAWN

### A.10.1 · `hold` must not reach a `Site`

> ### RULED: **CONFIRMED, AND ON CARDINALITY PLUS THE COMMONS — NOT ON THE DESTROY CASCADE.**
>
> `hold`'s object domain is `Office | Rung | Record | Proposition`, **1 per object** (`holonic:538`);
> `ARCH` PART D row 14 grades *"a banner holding territory"* **STRUCTURAL (typed)**. **What is held is
> the RUNG the site keys to, or the `works` Record on it. Never the fabric.**
>
> **The ground is that widening it DELETES THE COMMONS.** `hold_force` **raises** on a second live hold
> (`world_q.py:138-145`), so a held fabric has exactly one holder, `share = 1` everywhere, and
> §A.6.4's forty-boat harbour stops existing as a category — **and with it the only mechanism in the
> design that produces collective ruin from rational private acts.**
>
> **Three things the refusal keeps, and they cost nothing.** (1) **The fabric outlives its holder's
> claim** — take the plot and the cathedral does not move, so you have taken it by taking the ground,
> **one edge changing hands rather than two.** (2) **A works can be held by somebody who does not hold
> the ground** (§A.6.7's mason and lord). (3) **Nobody holds a wall, and nobody should** — a rampart's
> rung is the quarter, and a wall is a common thing.
>
> **The cost, plainly:** you cannot confiscate a single building. You confiscate its plot, which takes
> everything on that plot. **That is correct** — a granary and its store move together, because
> `stores` is a `Rung` field.
>
> ⚠ **THE REFUSAL IS UNENFORCEABLE TODAY.** `World.add_tenure` is *"The ONE writer"* (`world.py:223`)
> and validates **two** things — `t.kind` on `TENURE_KINDS` (`:242-247`) and `contain` ascent
> (`:248-256`) — and then appends (`:257`). **It checks nothing about the object class of a `hold`**,
> so `Tenure(p, <a site id>, "hold")` is accepted, and `ARCH` PART D row 14's grade of **STRUCTURAL
> (typed)** describes a typed language this one is not. **The object-domain conjunct lands as one more
> conjunct beside the two already there**, and it **earns its existence** under `CLAUDE.md` §0.1 pt 5:
> a `Tenure` is read at RESOLVE, at MATTER and in six Queries, so it is **load-bearing on the game**;
> `add_tenure` is already the single writer; it fails on recurrence. **Sibling `05`'s item 16 owns the
> build step; the argument is round one `02` §A.5.3's and is a pointer, not a restatement.**

### A.10.2 · ⚠ `fort_level` AND `facility_tier` — BOTH CUTS STAY WITHDRAWN AS BREAKAGES

Carried verbatim in force from round one `02` §A.3.3, which **owns** this withdrawal. Not re-argued,
because re-arguing it is how it got restated in two files; the reasons, in one line each:

| ~~the cut~~ | why it is a breakage |
|---|---|
| ~~cut `fort_level`~~ | **WITHDRAWN.** Declared on the **live** `Territory` (`engine/autoload/game_state.py:241`), **derived** from garrison at `:324` under a comment that is the single-owner rule stated in place, round-tripped through the snapshot at `:381` and rebuilt at `:452`, with the rule repeated at the export leaf (`engine/substrate/world_initial_state.py:17-18`); and `terr.fort_level` is an authored descriptor key (`references/descriptor_registry.yaml:94`) cooked into `engine/engine_params/descriptors.json` behind `tools/export_descriptors.py --check`, which is **BLOCKING in CI** |
| ~~cut `facility_tier`~~ | **WITHDRAWN.** Read live at `systems/settlements/sim/registry.py:97` (the AP property), **set by its own loader** at `:146`, serialised at `:119`, and registered as `set.facility_tier` behind the same blocking export |

> **NEITHER IS CUT BY THIS DOCUMENT, AND THE ENGINE'S `fort_level` ALREADY *IS* THE SHAPE §A.9
> ARGUES FOR.** A derived quantity with one owner and a comment saying why it is derived is not the
> defect it was cited as; it is the defect's repair. §A.9 proposes the **head's** representation, in
> `engine/season/`, where there is none. **A session that deletes either field on this document's
> authority has misread it.** The deletion may still be defensible on *other* grounds — both sit in
> trees `ED-IN-0204` Decision 1 superseded. **The stated grounds were false**, and that is what this
> row records.

---

## A.11 · `ED-SE-0051` — the recommendation, and the ground this document DESTROYS

`ED-SE-0051` is **open**, `needs_jordan: true`, in `registers/editorial_ledger_se.jsonl`: *"E-1 — THE
BOUND ON THE DEMOGRAPHIC LOOP: matter only, or matter plus hearth capacity?"*, recorded as *"the one
question in `proposals/2026-09-10-settlements-factions-populations/` that survived all five of
`CLAUDE.md` §0's tests"*, with **LAYER 1 IS SILENT** stated in the row itself, and gating position 24
of the ratified order.

> ### RECOMMENDED — **NOT RULED, AND NOT CLOSED HERE: THE CAPACITY ARM, WHERE CAPACITY IS A `capacity(w, rung)` QUERY OVER DWELLING SITES WITH A FLOOR, NEVER A FIXTURE.**
>
> ```
> capacity(w, rung) -> int          # resolver-side, World FIRST, Nobody's. Declared at holonic:600.
>   = floor_fixture                                        # what a household keeps in a corner
>   + Σ over DWELLING Sites in this rung's containment subtree
>       whose condition >= band_floors[kind]["shelters"]
>     of that kind's declared `houses` count
> ```

**And the honest part first, because it is the part a later session will need.**

> ### ⚠ THIS DOCUMENT DESTROYS ROUND ONE'S DECISIVE GROUND FOR THE CAPACITY ARM, AND THE RECOMMENDATION MUST BE RE-ARGUED WITHOUT IT.
>
> Round one `02` §A.7's ground 1 was marked ⭐ decisive: *"**MATTER-ONLY IS NOT CURRENTLY A BOUND AT
> ALL.** `matter.py:185` records a shortfall and states in its own comment *recorded, not acted on*,
> and MEASURED: 0 of 211 hearths hold any matter after a season, so nothing is even being compared.
> **The choice is not between two bounds; it is between a bound and a TRACE note.**"* **That was true
> and this document makes it false.** §A.3 connects the draw and §A.4 makes the shortfall reach a
> body, a band, a budget and a death. **After items 3a and 3b, matter-only IS a bound** — it is
> `MW-L−2` composed with `MW-L−3`, and it bites. **So the strongest argument for capacity was an
> argument about an unbuilt engine, and building the engine retires it.**
>
> That is recorded rather than quietly dropped, because it is exactly the shape `CLAUDE.md` §0.1 pt 3
> warns about: a result about the tree, verified at the wrong half of itself. **A session that cites
> round one's ground 1 after item 3b lands is citing a measurement of a world that no longer exists.**

**The recommendation stands, on the two grounds that survive:**

1. **Capacity-as-a-fixture is the spreadsheet failure mode** — a number per facility kind, authored,
   never measured, and **unburnable, unholdable, untaxable**. Capacity-as-a-Query-over-live-fabric
   costs zero new tables beyond one `houses` column on a kind roster that must be authored anyway
   (§A.8), and it makes the player's building the lever Jordan asked for.
   `references/design_rulings_2026-09-06.md:169` is the governing line: *"Every aggregate is DERIVED,
   none is PUSHED."*
2. ⭐ **It makes decay and growth the same arithmetic.** A village whose crofts have worn below
   `shelters` **cannot hold the people in it**: capacity falls, and the excess must leave. So the
   damping term of the growth loop and the meaning of the decay loop are **one number**. Under an
   authored fixture they are two — and two ladders for one quantity is an **S** defect.

**`AX` T-b compliance** (`AX:284`): capacity bounds CENSUS's *individuation*, which is demand-driven
only, and **`AX-5`'s own resolution licenses exactly this** (`AX:172-175`, *"So individuation is
authored: the demand is its author"*). It **changes what may be admitted** and produces no outcome.

**THE FLOOR IS NOT DECORATION, AND AN ATTACK PUT IT THERE.** Attack: *a rung with `capacity == 0` and
`stores > 0`.* A newly founded hearth has no fabric, so capacity is zero, so **founding is
self-defeating** and the design fails at its own extreme — **R**'s completeness clause
(`CLAUDE.md` §0.06, *"a mechanism breaking at its extremes fails"*). The attack succeeded and changed
the design: the floor is what a household keeps, and the fabrics raise it above that. ⚠ **And §A.7.1
sharpens the attack**: `found` mints a `Site` at **condition 0**, which is below any `shelters` floor,
so a newly built cottage houses nobody until it is `restore`d above the band. **The floor is what
keeps the first season of a new hearth from being a contradiction.**

**The counter-argument, not hidden:** capacity lets a player **opt out** of the demographic game by
simply not building, where matter-only does not. The answer is that opting out is itself priced — a
small place is a weak place — whereas matter-only makes growth something that happens *to* the player.
**The objection is real and is the best case for the other arm.**

> ### RULED, on scope only: **`ED-SE-0051` IS NOT CLOSED, NOT ANSWERED, AND NOT GATING. `capacity` IS NOT BUILT BY THIS DOCUMENT AND IS COUNTED 0 ADDED, BECAUSE IT IS NOT ADDED.**
>
> It is the suite's **RR-2**, owned by `05`. `Rung.envelope` is kept as its carrier (§A.5).
> §0's **step 5 cannot take it**, because the two arms are materially different games — which is what
> the row itself says survived all five tests. **And `ED-WR-0011` (ruled) says the growth arm has no
> producer at all today**, so nothing waits on the answer: *"there is no season-tick generation at
> all… the cast only shrinks."* **It is answered alongside that row, by whoever reopens generation.**
> Cost of being wrong: **one Query swapped for a fixture.** It gates one build item and nothing else.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar:** `AX` **ID-13** (`AX:489`, *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT
DECLARED"*) and **ID-12** (`AX:454`, a closed set lives in data). **No new primitive without a row
here.** And the suite's meta-rule (`skills/ners/SKILL.md`: *a fix that adds a system has failed*):
every addition names what it removes, in the same section.

## B.1 · ADDED — nine names, each with why it is not a new primitive

| # | added | what | why it is not a new primitive | counted |
|---|---|---|---|---|
| 1 | **Query** | `nearest_store(w, rung, kind)` | a walk over `parent_of` (`world_q.py:48`), which **is** the ladder. It replaces "who delivers what to whom" — a family of two content moves, a delivery act and two Queries (`delivered`, `demanded`) round one proposed and this withdraws | **+1** |
| 2 | **Query** | `ceiling(w, site)` | resolver-side, Nobody's, storing nothing (`AX` **T-a**, `AX:255`). Counted honestly as new: **it is NOT in `holonic §17`'s roster**, unlike `share` and `capacity` | **+1** |
| 3 | **Query** | `share(w, p, site)` | **already DECLARED** at `holonic:600` under *"`Query` — never stored, always recomputed"*. An implementation, not an addition — round one's own precedent for `capacity` | **0** |
| 4 | **verb row** | `found` | the **producer two declared write-matrix rows have been waiting for** — `(Rung, exists)` (`write_matrix.yaml:294-300`) and `(Site, exists)` (`:322-328`), both with a step, a class, a `by:` and an emission and **no verb naming either cell**. `H-41` is `absent`; `§F.20` blocks build step 2 on it. **This closes `ID-13` rather than adding to the tree** | **+1** |
| 5 | **effect bodies** | `@effect_for("found")`, `@effect_for("restore")` | `restore`'s row is `grade: "ruled"` with five full columns and a specified formula (`verb_table.yaml:448-467`); what is missing is the body. Eleven exist; these are the twelfth and thirteenth | **+2** |
| 6 | **predicate** | `_req_found` | one predicate for one new verb row. `_req_restore` is **not** added: `restore`'s `requires_typed` is already two typed conjuncts evaluated by the existing grammar | **+1** |
| 7 | **fold widening** | `_apply_write`'s `deltas` out-parameter | **exactly symmetric with the `earned` out-parameter already there** (`resolve.py:311-351`), added for the same class of reason. It stays the fold's single write site; the accumulator at `:523-525` needs no change because it already tests for an int | **+1** |
| 8 | **MATTER block** | the body write + the `_crossings` call + the `remove_person` call | a new block in an existing step. A reader must hold *"MATTER moves bodies"*, so it is **+1 honestly** — and it edits **zero matrix rows**, adds **zero tables**, **zero Event kinds** and **zero carriers** (§A.4.7) | **+1** |
| 9 | **helpers, FACTORED not added** | `_crossings(...)` from `matter.py:252-277`; `World.remove_person` from `effects.py:415-418` | each is code **moved to one owner and called twice**. `CLAUDE.md` §8's invariant is that a rule lives once; factoring is that invariant being obeyed, not a new name for a reader to hold | **0** |
| — | **content, counted 0** (data, not mechanism) | `fixtures.body_step` (injected/declared/swept, `AX` **ID-6**); the `works` row on `record_kinds`; per-family `wear_per_season`/`band_floors`/`site_yield` rows; a `houses` column; `venues.yaml`'s site-kind column | each is a data edit under `AX` **ID-12**, and the loader refuses a missing coordinated row (`fixtures.py:106-123`) | **0** |

**Carriers added: 0. Fields on carriers added: 0. Matrix rows added or edited: 0. Write classes, steps,
strata, eligibility kinds, tenure kinds, `requires` forms and Event kinds added: 0.**

## B.2 · MADE UNNECESSARY — and every row is a DELETION or a non-addition, never a renaming

| made unnecessary | why it survives the cut |
|---|---|
| **`Site.drawers`** *(a field, deleted)* | declared at `carriers.py:418`, **unwritable through the gate** (its matrix row is retired), **0 readers**. §A.6.4 derives `share` from a live edge instead, so the field's only conceivable consumer is gone. `AX` **ID-13** |
| **`Rung.sites`** *(a field, deleted)* | whitelisted at `carriers.py:568` and *"a BACK-REFERENCE NOTHING MAINTAINS — it is empty for every rung in the corpus"* (`matter.py:198`), with **no `(Rung, sites)` row in `write_matrix.yaml`**, so it cannot be written through the gate at all. `Site.rung` is the maintained side (`matter.py:205-206`). ⚠ **AND THIS IS A DEPARTURE, NOT PURE CONFORMANCE:** `ARCH §B.3` declares `Rung := (id, kind, matter(stores, sites[], records[]), …)`, so **Layer 1 lists `sites[]`**. `AX` **ID-13** licenses the cut **against a ratified declaration**, and saying so is the honest form. It is part of **RR-B**, owned by `05` |
| **hearth larders** | §A.3. No hearth gains a store. The 4,810 units stay where they are produced |
| **a delivery move, a delivery act, and round one's `delivered` / `demanded` Queries** | §A.3.4. Neither was built; both are withdrawn |
| **round one `02` §A.6's two content moves** (commons eaters ascending; DWELLING/PRODUCER fabrics re-keyed to the rung people are in) | §0.3 item 2. **The walk moves the draw, not the fabric.** 74 `venues.yaml`/`populated.py` rows stay untouched and `matter.py:205-206` stays as written |
| **`band_floors.person`** (the plan's new cell set) | §A.4.3. `band_floors["body"]` exists, is declared to be `(Person, body)`'s, is read live at `budget.py:73`, and a `person` key **refuses at load** |
| **the `stage` key on `works`**, and any extension to `_eff_work` | §A.6.1. `subject_matter` has no matrix row; progress **is** `Site.condition`; the ceiling does the counting |
| **a per-stage `Record.matured`** | §A.6.3. The **emission log** carries the count, and `World.last_emission_of` already reads it |
| **`undertake` · `build` · `repair` · `raze` · `garrison` · `convert` · `capture` · `improve` · `ruin`** *(nine verbs never minted)* | `create_record` does the whole of the opening, holder included; `restore` bounded by `ceiling` is building **and** repairing at different bands; a garrison is `presence` filtered by who is bound; conversion is a new works on a standing fabric with a different kind; capture is `hold` changing hands; a ruin **is** condition 0 |
| **a build queue, a scheduler, a cooldown, a timer** | `hold`'s 1-per-object plus the `cardinality` conjunct is a **refusal** (`AX` **T-g**); the two stalls are arithmetic (§A.6.6) |
| **a siege subsystem** | §A.9 — three reads onto three mechanisms that already exist |
| **`hold : Person → Site`** | §A.10.1 — three expressible things die, and the commons dies with them |
| **a facility-tier ladder in the head; any `infrastructure_score` or settlement-level `condition`** | the node-keyed average by another name (`holonic:449-451`); and *"no magnitude carrier is admitted at any scale"* (`design_rulings_2026-09-06.md:169`) |
| **a `Holding{confers:[Capability]}` object, and every "+N to a roll" reading of a built thing** | `eligibility_kinds` is `[own, remit, hold, presence]` and its note reads *"⚠ `capability` IS NOT AND MUST NEVER BE A MEMBER… Adding a fifth kind is a DESIGN CHANGE… and not a table edit"*. **A built thing may supply an OPERAND — a store to spend, a hall to sit in, a site to be present at — never a gate on who may attempt a verb.** This is the most tempting import in the subject and the one that would break the eligibility model |
| **`regrowth: 0` rows** | already deleted by the pessimistic pass: **no `regrowth` table exists under `engine/` and nothing would read one.** A row nobody reads is `ID-13`'s dead carrier |

## B.3 · WITHDRAWN AND DECLINED — said out loud

| ~~withdrawn~~ | why |
|---|---|
| ~~cut `fort_level`~~ · ~~cut `facility_tier`~~ | §A.10.2 — **breakages**, behind a blocking export. Round one `02` §A.3.3 owns the withdrawal |
| ~~the destroy-cascade licence for the ontology~~ | §0.5 — **unsound**; `holonic:588-589` is about which **Tenures** end, and nothing destroys a `Rung` or a `Site` at all. The refusal rests on **cardinality** |
| ~~"widening `hold` makes `restore`'s `share` computable"~~ | §A.6.4 — `share` and `draw_share` are declared **Queries** (`holonic:599-600`); `share` was **never a field** |
| ~~round one `02` §A.7's ground 1 for the capacity arm~~ | §A.11 — **true when written, and made false by this document.** Recorded rather than dropped |
| ~~`ARCH` PART D row 5 as a MATTER guarantee~~ | §A.1.3 — the gate contains no `before == after` comparison; the refusal is the fold's and is ACTS-only |
| **declined:** a gate-side no-op check · a `band_floors` key roster · an eighth `requires` form · a `capacity` implementation | each argued in place (§A.1.3, §A.4.3, §A.7.1, §A.11). **The first two are better designs and out of scope**; the third would refuse at load; the fourth is `ED-SE-0051`'s |

## B.4 · THE COUNT, AND WHAT IT COSTS THE SUITE'S NET — stated in the unfavourable unit first

**This document is net POSITIVE on its own: +9 added, −2 removed, net +7 names.** It may be net-positive
only by pointing at the suite ledger's net, which is `05`'s and is the single owner of the count
(`CLAUDE.md` §0.1 pt 4 — *"A proposal that reports only the favourable unit fails"*).

> ### ⚠ AND IT SPENDS THREE OF THE SUITE'S NET, WHICH `05` MUST ABSORB OR REPORT.
>
> The round-two plan's ADDED table carries `nearest_store`, `found` and `@effect_for("restore")` /
> `@effect_for("found")` already. **It does NOT carry `ceiling`, `_req_found`, or `_apply_write`'s
> `deltas`.** Those are three names beyond the plan's ledger, so **the suite's net moves from −20 to
> −17**, and `05` must print −17 or explain where three went. `share` and `capacity` are **0** on
> `holonic §17`'s declaration, and `band_floors.person` and the `stage` key were content (0), so
> declining them buys the count nothing — what it buys is three data edits and two **S** defects
> avoided.
>
> **In the "systems" unit rather than the "names" unit:** in — one walk family, one bound (`ceiling`),
> one delta channel, one verb; out — nine verbs never minted, a delivery family, a build queue, a
> siege subsystem, two dead fields, a second band ladder and a second progress ladder. **By that unit
> it is strongly negative, and by the names unit it is +7.** Both are stated because reporting only
> the first is the failure mode.

## B.5 · **E**, SCORED LAST AND AS A RATIO — `CLAUDE.md` §0.06

§0.06: *"⚠ **E is never scored as an independent axis**: alone it is satisfiable by amputation, so
score it **last, as a ratio against what N and R found**."*

**Against what N and R found necessary (§C.4's N-lines and loops):** of the nine added names, **seven
are N-line carriers whose cut is named and lethal** — `nearest_store` (211 hearths starve beside 4,810
units), the MATTER body block (a live, wired decision-layer mechanism stays permanently dead),
`found` (two declared rows keep no producer and `§F.20` stands), the two effect bodies, `ceiling` (no
bound on a repair, so building and repairing cannot be one act), and `deltas` (no act can raise a
fabric at all — `H-105`). **Two are conceded as overhead:** `_req_found` (a predicate for a verb,
unavoidable, but it is still a name) and the `_crossings`/`remove_person` factoring, which is free by
the count and **costs a reader two indirections in the two functions they most need to read straight
through** — `matter.py` is read as text by eight tests and `_eff_kill` is the most heavily
docstringed body in `effects.py`.

> **E PASSES AS A RATIO — 7 of 9 additions are N-line carriers, against 9 verbs, 2 fields, a delivery
> family, a build queue, a siege subsystem and two second ladders out — AND IT WOULD FAIL IF SCORED
> ALONE**, because scored alone the cheapest version of this document is "delete the larder step".
>
> **The legibility half passes on its own test** — *"allows the player to intuit complex outcomes from
> simple choices"*: a player reads **half rations hold you steady**, **a fabric climbs to the terms
> that have ripened**, and **your store is your parent's store**, and all three are one sentence each.
>
> ⚠ **FINDINGS, STATED NOT SCORED AROUND.** (1) The three-way coupling of `wear` × `restore` ×
> `yield-scaled-by-condition` has a steady state **the player cannot compute** — they can intuit
> direction and not equilibrium. Carried from round one, unrepaired, and the repair is interface-side.
> (2) **`ceiling` composed with `share` composed with the degree ladder is three multiplications deep**,
> and a player at a forty-drawer harbour cannot intuit that his Overwhelming season moved 6 of 1000.
> **That is a real E cost of keeping the commons**, and §A.6.4 keeps the commons anyway, on R.

---

# PART C · THE THREE QUESTIONS

## C.1 · WHO OWNS THIS?

| the thing | owner | **not** |
|---|---|---|
| a person's body | **`Person`** (`carriers.py:392`), one writer per write class: MATTER (this document) and ACTS (`_eff_kill`) | never a `Rung` aggregate, never a cohort tally |
| a person's existence, and every Tenure naming them | **`World.remove_person`** — one owner, two callers | never a caller sequencing three writes (`holonic §15.3`) |
| where a body draws from | **`nearest_store`** — a Query, Nobody's | never a field, never a route, never a cached `{person: store}` map |
| an actor's share of a fabric | **`share`** — a Query over a live `contain` edge | never `Site.drawers`, which is deleted; never 1 |
| how high a fabric may be raised | **`ceiling`** — a Query over the works' `term.matured` emissions | never a field on the `Site`, never a per-stage bool on the `Record` |
| a fabric's condition | **`Site`**, one writer per write class (`write_matrix.yaml:315-321`, `[MAT, RES]`) | never a `Rung` — `Rung` has no condition field and `__setattr__` raises (`carriers.py:589-597`) |
| a works in progress, its terms and its ttl | **`Record`** (`carriers.py:422-445`) | never fields on the `Site` — then nobody would be master and MATTER would have no holder to check (`matter.py:73-74`) |
| who is master of a works | the **`hold` Tenure's subject**, minted by `create_record` (`effects.py:286-289`) | never a field on the Record, and never two at once (`hold_force` **raises**) |
| a plot, its store, its dates, its records | **`Rung`** (`carriers.py:568-569`) | never a social aggregate (`ARCH §B.3`: `NEVER: any social aggregate`) |
| the band a body or a fabric is in | **`band_floors`**, ONE table, TWO callers (`_crossings`, `body_band_penalty`) | never two cell sets, never `band_floors.person` |
| how much a season narrows a narrowed person | **`budget()`** person-side, reading `p.body` and a params table and **no World** | never the crossing, which produces no outcome (`AX` **T-b**) |
| the delta an act contributes | **`_apply_write`**, the fold's single write site | never `a.payload` — that is intent reassignment, **under RR-P** |
| `body_step`, the floors, the wear rates, the yields | **`rosters.yaml` / `DEFAULT_FIXTURES`**, each with a hole-register row and a three-point sweep | never a literal in a body (`CLAUDE.md` §0.05) |
| the order of MATTER's blocks | **`#353 §25`**, quoted and followed at `matter.py:155-160` | never this document, which reorders nothing and only **splits** one loop in two (§A.3.3) |

## C.2 · WHAT CAN CHECK THIS? — `STRUCTURAL | MECHANICAL | CONVENTION`

A claim of STRUCTURAL that is really MECHANICAL is *"a guard that cannot observe what it guards."*

| claim | grade | the checker, named |
|---|---|---|
| a body's band ladder is the same table a site's is | **MECHANICAL at load** | `band_floors` declares `keys: [site_kinds]` and `fixtures.py:110-123` validates **both directions**. A second cell set **raises** |
| a MATTER write on `(Person, body)` emits `body.changed` and nothing else | **MECHANICAL at the write** | `world.py:396-406` refuses a MATTER write that names no declared kind **and** one the row does not declare |
| a `body.changed` emission has an antecedent that is not `[ROOT]` after season 1 | **MECHANICAL** | `Event.__post_init__` refuses an empty `causes[]` at `S19.4` (`world.py:459-462` declines to re-implement it); `W4`'s `[ROOT]`-count proof is the assertion |
| **a fed person at full body emits nothing** | ⚠ **CONVENTION today, MECHANICAL only through the caller's own guard** | §A.1.3: the gate has **no** `before == after` check; `matter.py:148-149` and `:186` are hand-written guards. **The gap is named rather than graded away**, and `MW-3` is the test that would catch its absence |
| the death cascade has exactly one owner | **MECHANICAL, by a source scan** | `MW-6`: grep the four-line tenure sweep and assert **one** site. It is load-bearing on the game (a dangling edge survived a death for a season before this scan's predecessor was fixed) |
| `hold` never reaches a `Site` | ⚠ **NOTHING today; MECHANICAL once the conjunct lands** | `add_tenure` checks kind (`:242-247`) and `contain` ascent (`:248-256`) and **nothing about object class**. Layer 1 grades it STRUCTURAL (typed) in a typed language this is not. `05` item 16 owns the build step |
| a fabric's condition cannot be node-keyed onto a place | **STRUCTURAL at the type** | `Rung` has no condition field; `__setattr__` raises; `ARCH §B.4`: the collapse *"cannot be spelled"* |
| a built thing gains no new carrier | **STRUCTURAL** | there is no class to construct |
| a new site kind arrives with its wear and band rows | **MECHANICAL at load** | `fixtures.py:106-123`, both directions, raising `Forbidden`/`Ungraded` |
| no eighth `requires` form is smuggled in | **MECHANICAL at load** | `rosters.yaml:1092-1094` — *"a design change, not a table edit"* |
| a works with two live Records naming one target is refused | **MECHANICAL** | `ceiling` **raises** (`hold_force`'s precedent), and the `cardinality` conjunct refuses before it can happen |
| a repair that changed nothing mints no success Event | **MECHANICAL at the fold** | `resolve.py:259-269` reads `changed` and emits `emits_on_refusal`. ⚠ **ACTS-only** — see row 4 |
| a built kind never regrows unauthored | **MECHANICAL through what already emits** | `wear()` is the only MATTER writer of `(Site, condition)` and `restore`/`work` the only RESOLVE ones, so assert the **SIGN** of every `(Site, condition)` delta **by its step**. ~~a `regrowth: 0` row per kind~~ is struck: no such table exists and nothing would read one |
| the ceiling bounds the clamp and nothing else | **MECHANICAL** | one expression, `resolve.py:549`. `MW-7` asserts the ceiling is the only new term and that it equals `condition_scale` for every site in a world with no works |
| a fortification's band is never rendered as fact | **CONVENTION**, and it cannot be made structural here | the renderer does not exist. `ARCH §C.11` is the argument; the check is that a reviewer reads the read list |
| **the capacity arm of `ED-SE-0051`** | ⚠ **NOT A GRADE — a RULING REQUEST** | this column asks *what construction checks this claim*, and a ruling request has no construction because it has no answer. It is **RR-2**, `needs_jordan: true`, **LAYER 1 SILENT** stated in the row itself |
| **`body_step`'s value, and the floors'** | ⚠ **NOTHING, and that is the honest word** | both are injected with a three-point sweep and **neither has been measured against anything.** §C.5 names this as the largest unmeasured number the design now depends on. A grade here would be a claim |

## C.3 · WHOSE ACT MAKES IT HAPPEN?

**Every row: what is written, by whose act, read by whom, emitting what. No row is a system depositing
a thing.**

| what is written | by whose act | read by | emitting |
|---|---|---|---|
| `(Rung, stores)` **down**, at the rung the walk found | **nobody** — MATTER, `AX-5` motion 1 | next season's draw; `restore`'s threshold; `nearest_store` | `stores.changed` |
| `(Rung, stores)` **up** by yield | **nobody** — MATTER, scaled by the site's condition | the same | `yield.taken`, `stores.changed` |
| `(Rung, stores)` **across** a `contain` edge | **a person**, `transfer`, `own | hold:<store>` | the same | the verb's own emission / `transfer.refused` |
| `(Person, body)` **down** | **nobody** — MATTER, `AX-5` motion 2, the ration below ½ | `body_band_penalty`; `_crossings`; the death test | `body.changed` |
| `(Person, body)` **up** | **nobody** — MATTER, the ration above ½ | the same | `body.changed` |
| a **body band crossing** | **nobody** — and **it produces no outcome** (`L5`) | WITNESS's fan-out → a Claim → a question | `condition.band_crossed`, subject = **the person** |
| the **narrowing of a season** | **the person**, at DELIBERATE, reading their own body | `ask_budget` (`deliberate.py:116-117`) | — |
| `(Person, exists)` + every Tenure naming them | **nobody** — MATTER, at body 0 | `presence`, `home_of`, `members`, `leaders`, `footprint`, `hold_force`, `matter.py:73-74` | `person.died` |
| `(Record, exists)`, `(Record, stages)`, **the maker's `hold`** | **a person**, `create_record`, `own` | `matter.py:73-74`'s holder check; `ceiling` | `record.created` |
| `(Record, matured)` | **nobody** — the clock the opening act wound, `causes[]` naming that act | `ceiling`, via the emission count | `term.matured` |
| `(Rung, exists)` + its `contain` edge | **a person**, `found`, `own` + presence in `requires` | `presence`, `parent_of`, `descendants`, `nearest_store`, the larder pass | `rung.founded` / `found.refused` |
| `(Site, exists)` at condition 0 | **a person**, `found` | `verbs`, `site_yield`'s scaling, `ceiling`, the band predicate, `capacity` | `site.built` / `found.refused` |
| `(Site, condition)` **up** | **a person**, `restore`, through the summing clamp, **bounded by `ceiling`** | the same four | `site.restored` / `restore.refused` |
| `(Site, condition)` **down** by wear | **nobody** — MATTER | the same four | `condition.worn` · `condition.band_crossed` |
| `(Site, condition)` **down** by an attacker | **a person**, through the contest seam, graded to a negative delta | the same four | the contest's own emission |
| a `hold` changing hands | **a person**, `confer`/`release`/`revoke`/`give`, refused while one is live | `in_holdings`, `hold_force`, `footprint`, `ceiling` | the verb's own emission / its refusal |
| a works ending unfinished | the **`ttl` the opening act declared** (`T-n`), or **`destroy_record`** by its holder (`T-m`) | `ceiling` — which **freezes where it stood** | the lapse / `record.destroyed` |

## C.4 · THE LOOPS, NAMED AND SIGNED — `AX` **ID-16** (`AX:544-548`)

**ID-16, verbatim:** *"Every feedback path appears in the register with a direction. **A model in which
every loop is negative CONVERGES** — season 40 resembles season 30 — and convergence is not a design
goal, it is what happens when a design has no other ideas."*

⚠ **THE TREE'S CURRENT STATE IS THAT DEFECT, MEASURED.** The live register
(`engine/season/hole_register.yaml`) has **four** `kind: LOOP` rows — `H-102` (`:1383`), `H-103`
(`:1396`), `H-104` (`:1409`), `H-112` (`:1558`) — and **all four are inside the claims machinery.
Nothing in the register is about the world.** `H-105` (`:1422`) sits between them and was **re-filed
`PRODUCER`** precisely because it is not a loop: *"SITE CONDITION IS A SEVERED LOOP, NOT A DAMPING
ONE… A loop with one arm cut is a RATCHET wearing a loop's clothes."* And `ARCH §F.20` says the same
thing from the other side: ***"the world only decays — nothing is ever founded or built."***

| id | the cycle | sign | the damping or the bound, named — each a mechanism that already runs or is built here |
|---|---|---|---|
| **MW-L−1 · WEAR** | condition ↓ at MATTER → verbs removed → less yield → less to spend → condition ↓ | **−** | the ceiling is **full** for a finished works, so repair is always possible in principle; a fabric at 0 is a ruin on a plot that can be built on again. **The loop has a floor and the floor is re-enterable.** MEASURED: `condition.worn` **74** per season, 1000 → 990 |
| **MW-L−2 · SUBSISTENCE** | people eat stores → less surplus → fewer people can be seated | **−** | `nearest_store` × `Person.weight` (§A.3). **Built but unreachable today** — MEASURED: the block fires 26 times and writes **0** times |
| **MW-L−3 · THE BODY LOOP** ⭐ NEW | ration < ½ → body ↓ → band crossed → `body_band_penalty` ↑ → `budget()` ↓ → fewer acts → less `transfer`, less `restore` → less matter reaches you → body ↓ | **−**, and it is the **sharpest negative loop in the design** | **three bounds, none of them a number somebody picked.** (1) `budget()` floors at **1** (`budget.py:62`) — *"a dying one still gets one, because a budget of 0 would delete the person from the season silently rather than narrowing them"*; so a starving person **always retains one act** and the loop is escapable **by acting**. (2) `MW-L+1` is the same write with the sign flipped, so one good season reverses it. (3) It terminates: at body 0 the person is gone, which is `AX-5` motion 2 rather than an unbounded spiral |
| **MW-L+1 · THE RATION LOOP** ⭐ NEW, **and it is what keeps `MW-L−3` from being `H-105` again** | ration > ½ → body ↑ → band re-crossed upward → penalty ↓ → `budget()` ↑ → more acts → more matter reaches you → body ↑ | **+** | **structural, four ways:** the clamp at `condition_scale` (one `min`, `AX-4`'s one owner); the draw is against a store the world also feeds from, so a fed person's surplus is somebody else's shortfall in `MW-L−2`; wear subtracts from the yield that supplies the ration; and every act comes out of a budget of about five. ⚠ **AND ITS UPWARD CROSSING DOES NOT EMIT TODAY** — `_crossings`' predicate is `before >= floor > after`, **downward only** (`matter.py:262`), so **recovery is silent while ruin speaks.** Named as a limit at `MW-11`, not patched here: the repair is the same predicate in the other direction and it is sibling `01`'s question surface, not this document's |
| **MW-L+2 · THE WORKS LOOP** | a PRODUCER above its band → `(Rung, yield)` → `(Rung, stores)` → matter for `restore` → condition ↑ → more yield | **+** | **structural, three ways:** wear subtracts **unconditionally at MATTER, before any act's delta**, so the two writers need no commutativity argument; the clamp clamps once (`resolve.py:549`); and **`ceiling` bounds it to the terms that have ripened** — so the amplifying arm cannot outrun the clock the opening act wound. ⚠ **Connected for the first time by §A.6.5's delta channel**; `H-105`'s severed arm is why this loop has never turned |
| **MW-L+3 · THE SHELTER LOOP** | DWELLINGs above `shelters` → `capacity` → the envelope may grow → more presence → more hands **and more mouths** → more works | **+** | every added body raises the draw against the same larder (`MW-L−2`), and **capacity falls with the fabric**, so the bound tightens as the place wears. **This is `ED-SE-0051`'s subject and it is NOT BUILT** (§A.11); and `ED-WR-0011` (ruled) says the growth arm has **no producer at all** today |
| **MW-L+4 · THE FOUNDING LOOP** ⭐ NEW | `found` a plot → `found` a fabric → `restore` it above its band → yield → stores → matter for the next works → `found` | **+** | **the act budget** (each `create_record`, `found` and `restore` is one of about five, at one place, and the actor must be present); **the terms** (a works ripens on its own schedule — matter cannot buy time); **the standing bill** (everything already built wears against the same store, so **the more you have built the less you can build** — a bound that **tightens with success**, which no cap does); and **other people** (leave, masters, and whoever is present to break what you raise) |
| **MW-L−4 · THE NEGLECT LOOP** | a governor stops paying → bands cross → **crossings emit** → witnesses mint claims → his standing falls → he can bind fewer people to keep the wall → fewer keep it | **−** on him, **+** as drama | `claim.decayed` erodes the grievance (`matter.py:147-153`), and `AX` **T-m** (`AX:1154`) means he may always re-court and re-bind, paying acts. **The loop is escapable and the escape costs politics** |

> ### THE DEMONSTRATION THAT THIS DESIGN IS **NOT ALL-NEGATIVE**, WHICH IS WHAT `ID-16` ACTUALLY ASKS FOR
>
> **Four of the eight are `+`, and three of the four (`MW-L+1`, `MW-L+2`, `MW-L+4`) do not turn at all
> today.** `MW-L+2` is severed at `H-105`'s cut arm; `MW-L+4` has no producer at all, which is
> `ARCH §F.20` verbatim — ***"the world only decays — nothing is ever founded or built"***; and
> `MW-L+1` does not exist because `(Person, body)`'s MATTER half has no writer. **So `ARCH §F.20` is
> not a clause this document argues against. It is the exact defect being repaired, stated by the
> ratified architecture about itself**, and the three items that repair it are §A.6.5's delta channel,
> §A.7.1's `found` and §A.4.2's signed body write.
>
> ⭐ **THE TWO HALVES ARE COUPLED AT THE MECHANISM RATHER THAN BY TUNING**, and this is the property
> that makes the positives safe without a cap: **every act of `MW-L+2` adds a term to `MW-L−1`** (a
> raised fabric is a fabric that wears), and **every body `MW-L+1` mends adds a mouth to `MW-L−2`**.
> The amplifying loops' gain falls monotonically as they grow. **That is a bound that is a property of
> the arithmetic rather than of a number somebody picked.**
>
> ⚠ **THREE HONEST NOTES.** (1) **`ID-16`'s own representation is BLOCKED** — it asks for a cycle
> enumeration over *what is written* × *what is read* and `H-112` records that the read half cannot be
> built (*"a DERIVED check that recomputes the cycle set… cannot be built"*). **So this table is a
> claim about the loops I know of, not a completeness claim.** (2) **The standing/reputation loop is
> designed and INERT**: `ARCH §F.20a` — no verb writes any `Person` **interior** field — so building
> visibly cannot move anyone's conviction, and §A.7.2 confirms this document does **not** close it. A
> body is not a conviction. (3) **The falsifier of the whole table is one grep**: `rung.founded`,
> `site.built`, `site.restored` and `body.changed` are **all 0** in a measured season. **The design
> stops being all-negative exactly when those four are nonzero, and that is measurable in one run.**

## C.5 · **GRADE: `paper`** — and exactly what would move it

`CLAUDE.md` §0.2: *"A milestone juncture is done when the behaviour EXECUTES. Not when a document
exists with a `## Status:` line."* **Nothing designed in this document executes.** The honest ledger of
what does, MEASURED this session on one season of `build_realm(0)`:

```
wear                       RUNS            condition.worn 74 ·  1000 -> 990
larder draw                RUNS AND WRITES NOTHING          fires 26 · writes 0 · 138 units unmet
yield                      RUNS            yield.taken 37 · stores.changed 37 · 4,810 units at 37 settlements
site band crossings        RUN, DOWNWARD ONLY, AND FIRE AT PASS 21   w.crossings 0
a shortfall                RECORDED, NOT ACTED ON           matter.py:184-185
works Records              RUN             record.created 69, with the maker's hold minted
a works whose master died  REFUSES TO MATURE                matter.py:73-78 — zero new code
claim decay                RUNS            claim.deposited 2175 · (claim.decayed 0 in season 1)
bodies                     NO MATTER WRITER                 body.changed 0 · person.died 0
body_band_penalty          LIVE, WIRED, AND ZERO FOR ALL 46 PERSONS
founding / building        ZERO PRODUCERS                   rung.founded 0 · site.built 0
restore                    NO EFFECT BODY                   site.restored 0 · resolvable_verbs() 18 of 38
an act's delta             NO CHANNEL AT ALL                site.worked 0 · work.unavailable 38
a fabric anybody is at     NONE            0 of 74 sites
a hearth holding matter    NONE            0 of 211
```

> ### THE FIRST ARTIFACT, AND IT IS ONE COMMIT: **item 3a — `nearest_store` plus the per-eater draw — whose artifact is a `census` before/after on the measured world, moving `larder writes` from 0 to 13 and `unmet subsistence` from 138 to 0.** Nothing is blocked on a ruling, nothing new is authored, and it is measurable in one run.
>
> **The artifact that moves the GRADE off `paper` for the second half is `MW-2`'s `rung.founded`** —
> currently 0 and measurable in one grep — and it is downstream of `record_kinds` (sibling `02`'s) and
> of the delta channel.
>
> ⚠ **AND THE LARGEST UNMEASURED NUMBER THE DESIGN NOW DEPENDS ON IS NAMED RATHER THAN BURIED:**
> `body_step` against `band_floors["body"]`, both invented, both swept, and **neither measured against
> anything**. §A.4.6 shows the arithmetic at all three arms and shows that **two of the three arms
> never occupy the lowest band.** A session that ships `declared` without running `MW-5` has shipped a
> band nobody can be in.
>
> ⚠ **`python -m pytest tests/valoria -q -n auto` was NOT RUN for this document**, because this
> document changes no code. That is stated rather than implied (`CLAUDE.md` §0's requirement that a
> skipped step be said aloud). What WAS run is the harness and the measurement recipe at §A.2.1, and
> the matrix header's own reproduce command at `write_matrix.yaml:41-45`.

## C.6 · RULINGS — what this document decides, escalates, and refuses to escalate

**Decided by `CLAUDE.md` §0's five-step gate, with the step named** (§0's *"needs_jordan IS NOT A
PARKING SPACE"*):

| decision | step | the citation that closed it |
|---|---|---|
| persons cross `band_floors["body"]`, not a new cell set | **4** (precedent) + **5** (the loader refuses it) | `H-38`, quoted at `rosters.yaml:814-815`, `budget.py:64-75` and `hole_register.yaml:793` |
| the body moves with a **sign**, one fixture, fixed point at half rations | **5** (architecture: a fall-only body is `H-105` again) | `H-105` (`hole_register.yaml:1425-1432`); `AX` **ID-16** |
| the body write carries its own no-op guard | **4** (precedent, two siblings in the same function) | `matter.py:148-149`, `:186` |
| the larder pass splits from the yield pass | **5** (forced by the ascent) | `test_season_shape.py:4711`'s emitted-order assertion |
| death is ONE write at `(Person, exists)`, not three | **4** (precedent) | `holonic §15.3`; `effects.py:312-315` |
| `ceiling` counts `term.matured` emissions | **5** (there is no per-stage field and the log is a carrier) | `world.py:447-453`; `carriers.py:445` |
| `ceiling` **raises** on two live works naming one target | **4** (precedent) | `world_q.py:138-145` |
| `share` = 1 over persons present, swept, with `one` as a breaking control | **5** + `AX` **ID-6** | `holonic:600`; `10_SUPERSEDING.md:1275-1282` |
| the delta rides on `_apply_write`, **not** on `a.payload` | **5**, and **under RR-P** | `resolve.py:338-346`; `write_matrix.yaml:72-78` |
| `found` is one verb earning one of two declared rows | **4** (the `{kind: [ids]}` mapping was built for this) | `resolve.py:338-346`, `:252-257` |
| `found` requires `Record.matured`, not "all terms ripened" | **5** (an eighth form refuses at load) | `rosters.yaml:1092-1094`, `:1114` |
| the `works` `subject_matter` is `{plan, at}` — no `stage` | **5** | no `(Record, subject_matter)` matrix row exists |
| `Site.drawers` and `Rung.sites` are deleted | **5**, and `AX` **ID-13** against a ratified `ARCH §B.3` declaration | `carriers.py:418`, `:568`; `matter.py:198` |
| `Rung.envelope` is KEPT with no production reader | **5** (its consumer is a ruling request, and deleting it would force a re-add) | `ED-SE-0051`; `ARCH §B.3` |

**NOT escalated, and closed with its reason** — because §0 says clearing the queue is session work:

- *"Should the gate refuse a no-op?"* — **closed at step 5 as OUT OF SCOPE, not as answered.** It is a
  better design; it moves eleven MATTER writes and every golden through MATTER; this document does not
  need it and may not buy it.
- *"Should `band_floors` have its own key roster?"* — **closed the same way**, with the residual
  idempotence hazard named at §A.4.3 and its falsifier at `MW-9`.
- *"Which eater draws first?"* — **closed at step 5.** `sorted(w.persons)`, deterministic and
  arbitrary on purpose: a ration order is a policy, and **MATTER reads no policy.**
- *"What is `body_step`?"* — **not a ruling.** `AX` **ID-6**: injected, declared, swept. §A.4.6 gives
  the arithmetic and §C.5 names the measurement that is missing.

**ESCALATED — and only what this document's own subject forces:**

- **`ED-SE-0051` / RR-2** stays **OPEN**, `needs_jordan: true`, untouched and **not gating**
  (§A.11). This document *recommends* the capacity arm, records that it **destroys round one's
  decisive ground for that recommendation**, and re-argues it on the two that survive. **No row here
  may be cited as having closed it.** Per `ED-WR-0011` (ruled), the growth arm has no producer today,
  so it is answered alongside whoever reopens generation.
- **RR-B** (Layer-1 text this makes false) gains **one sentence from this document**:
  `ARCH §B.3`'s `Rung := (… matter(stores, sites[], records[]) …)` declares `sites[]`, and §B.2
  deletes it. Quoted at its `§`, **not edited**. The other three sentences are siblings'. Owner: `05`.
- **RR-P** is leaned on once, at §A.6.5, and is **stated as unsettled**: the refusal of the
  payload-mutation route is *under RR-P*.
- **RR-C** (sequencing ahead of the Arc-2 gate) covers items 3a, 3b and the works items. Owner: `05`;
  not argued here.

**No other ruling request is raised by this document, and that is deliberate** — `needs_jordan` means
*"Jordan is the only person who can answer this"*, not *"nobody got around to it."*

---

# PART D · FALSIFIERS — `AX` **ID-11** (`AX:453`), *ship the falsifier with the claim*

**The bar is `CLAUDE.md` §0.1 pt 2: an assertion must be able to OBSERVE the failure it excludes.**
A test that passes on a world where the mechanism cannot fire is absent, not weak. So every row below
carries a **control** — an arm on which the assertion must go the other way — and where the control
would be vacuous the row says so.

## D.0 · Round one's `BW-n` rows, mapped

`BW-2` (matter reaches people) → **`MW-1`**, re-aimed: round one's artifact was *"hearths holding
matter > 0"* and **this design never gives a hearth a store**, so that artifact would be red forever.
`BW-8` (`restore` mirrors decay and stops at the ceiling) → **`MW-7`**. `BW-9` (`found` is the
producer) → **`MW-2`**. `BW-3` (a `hold` on a Site is refused) and `BW-4` (no faction `hold` subject)
→ **sibling `05` item 16**, not restated. `BW-13` (the two withdrawals) → **`MW-13`**. `BW-5`'s
re-aimed sign assertion → **`MW-12`**. `BW-1`, `BW-11` (Q3's referent, the upward crossing) →
**sibling `01`**, with `MW-11` recording the half this document's own positive loop depends on.

## D.1 · The rows

| # | claim | what would show it wrong — **and the control** |
|---|---|---|
| **MW-1** | `nearest_store` connects the two halves of the matter economy | `test_an_eater_draws_from_the_nearest_ancestor_store`. **Artifact: on `build_realm(0)` after one season, the larder pass writes `(Rung, stores)` at 13 rungs (today 0) and unmet subsistence falls 138 → 0.** **Control A:** a person seated directly in a stocked rung draws **locally** and the walk terminates at step 0 — so the walk is not merely "always go up". **Control B:** a settlement with **nobody** in its `contain` subtree is **untouched** — 3,120 units stay where they are, which is §A.2.3's ruling as an assertion. ⚠ **Falsified if hearth stores become nonzero**: that would mean something delivered, and nothing may |
| **MW-2** | `found` is the producer `(Rung, exists)` and `(Site, exists)` have waited for, and `ARCH §F.20` closes | `test_found_is_the_producer_for_rung_exists_and_site_exists`. **Artifact: a `rung.founded` AND a `site.built` Event in a run's log — both 0 today, measurable in one grep.** **Control:** an act whose plan names a rung earns **`rung.founded` only** and the `site.built` pair is gated-but-unearned — which is what proves the `{kind: [ids]}` mapping is doing the work rather than both emissions firing on any change (`resolve.py:338-346`'s own measured defect: *"`confer` onto an unheld office published `tenure.closed` with nothing closed"*) |
| **MW-3** | a fed person at full body emits nothing | `test_a_fed_person_at_full_body_emits_no_body_changed`. **This is the row §A.1.3 exists for**: the gate has no no-op check, so without the caller's guard **46 fabricated `body.changed` Events fire every season** and WITNESS fans each into every co-located ledger. **Control:** the same world with the guard removed must go RED — a mutation check, because a test that only asserts "0 emissions in a fed world" also passes if the whole block is missing |
| **MW-4** | the shortfall reaches a body, a band, a budget and a death | driven on the **`site_yield` `none` sweep arm** (`rosters.yaml:1150`), the roster's own declared control, because §A.3.5 measures the populated world as a **surplus** world where the chain cannot fire. Assert, in order: `body.changed` > 0 · body falls by `body_step` · a `condition.band_crossed` whose **subject is a person** · `body_band_penalty` > 0 · `ask_budget` strictly lower than the same person's on the `declared` arm · at body 0, `person.died` and the person absent from `w.persons` and every Tenure naming them closed. **Control: the `declared` arm, where bodies are constant at 1000 and every one of those assertions must go the other way.** ⚠ **Without the control this test passes on a world where the chain never runs** |
| **MW-5** | every declared body band is occupied for at least one season | `test_every_body_band_is_occupied_before_death`. **IT GOES RED AT THE `declared` ARM AND AT `doubled`, AND THAT IS THE POINT** (§A.4.6): at `body_step = 100` the `withdrawal_only` crossing and death fall in the same season, so the third rung of `body_band_penalty` is never observed in play. **Control: the `halved` arm, where it goes green.** The row exists so the arm is chosen by arithmetic rather than by preference |
| **MW-6** | the death cascade has exactly one owner | `test_the_tenure_death_cascade_has_exactly_one_site` — a source scan for the four-line sweep, asserting **one** match. **Control:** it must go RED on a tree where `_eff_kill` keeps its own copy, which is the pre-factoring state, so the assertion is checkable by reverting. ⚠ And a behavioural half, because a source scan cannot see semantics: **a `kill / wound` at `Felled` and a MATTER death at body 0 must close the same Tenure set on the same world** |
| **MW-7** | `ceiling` bounds the clamp and nothing else | `test_ceiling_is_the_only_new_term_in_the_summing_clamp`. **Control, and it is the load-bearing half: on every world that exists today `ceiling` returns `condition_scale` for all 74 sites** — MEASURED, `w.records` holds 69 Records and **none is of kind `works`** — so `resolve.py:549` computes the same number and **no golden moves for this edit alone.** A golden that moves is the falsifier |
| **MW-8** | `share` keeps the commons | `test_a_commons_closes_collectively_and_a_single_drawer_does_not`: at a 40-person harbour one Overwhelming `restore` moves ~6 of 1000; at a 1-person site it moves a quarter of the headroom. **Control: the `one` sweep arm**, on which the 40-drawer case moves a quarter too — **the commons is deleted and the test must break.** A sweep whose control cannot break the claim is not a control |
| **MW-9** | `band_floors["body"]` reads the same way for a person and for a `body`-kind Site | `test_band_floors_body_is_read_the_same_by_both_callers`. ⚠ **This row exists because the hazard is live**: `engine/season/harness/headless.py:64` builds `Site("scriptorium", "hearth_ostvik", "body", …)`, so the four cells serve two subjects. Assert that `_crossings` and `body_band_penalty` agree on band membership for the same integer. **If they ever disagree, the borrowed roster key has become two meanings and §A.4.3's residual hazard has bitten** |
| **MW-10** | `Rung.envelope` is kept **only** as `ED-SE-0051`'s carrier | `test_rung_envelope_has_no_production_reader`, asserting the reader set is exactly `{carriers.py, census.py's docstring, probes.py, tests}`. ⚠ **The falsifier that matters is the other direction:** if a production reader is ever found, the field is **not** a held-open exposure and §A.5's ruling is wrong. And if `ED-SE-0051` is ruled **matter-only**, the field, its matrix row and CENSUS's claim over it become deletable in one commit — **that commit is the artifact that closes this row** |
| **MW-11** | the ration loop's recovery is visible | `test_an_upward_body_band_crossing_emits`. ⚠ **IT GOES RED**: `_crossings`' predicate is `before >= floor > after`, **downward only** (`matter.py:262`), so **ruin speaks and recovery is silent.** `MW-L+1` is a real loop whose positive arm nobody can witness. **Control: the 74 downward site crossings per season must not change count** when the upward predicate is added. Recorded as a limit; the repair is sibling `01`'s question surface |
| **MW-12** | nothing regrows unauthored | `test_no_matter_step_site_condition_write_has_a_positive_delta` — assert the **SIGN** of every `(Site, condition)` delta **by its step**: MATTER writes only down (`wear`), RESOLVE only through the fold. ⚠ Re-aimed from round one's `regrowth: 0` row, which is struck: **no `regrowth` table exists and nothing would read one**, and a test over a fixture cell cannot observe the failure it excludes (an unauthored positive delta comes from a **code path**). **If a built kind's condition ever rises with no `restore` in the log, a fortification repairs itself with no author and the design has silently taken the fourth-motion route `AX-5` refuses** |
| **MW-13** | `fort_level` and `facility_tier` are not free cuts | delete either and show CI green. **PREDICTED RED** at `tools/export_descriptors.py --check` (blocking) and at `systems/settlements/sim/registry.py:97`'s `ap` property. Carried from `BW-13` |
| **MW-14** | a built world with no player in it eats, starves, stalls, falls, forgets and **asks** | a season in which it emits nothing. **Six channels named, and their dependencies stated rather than banked:** a larder drawing (3a) · a body falling and crossing (3b, and it needs `MW-4`'s empty arm) · a works term ripening with nobody present (**runs today**) · a master's death stopping a works (**runs today**) · a works lapsing at its `ttl` (**runs today**) · a crossing becoming a **question** (⚠ **blocked on sibling `01`'s `H-110` repair AND on a world where a floor is crossed — MEASURED, the first site crossing fires at MATTER pass 21 and CI runs one season**). **Three of six run today; three do not, and the three that do not are the three a player would notice** |

> ### THE ONE CLAIM THIS WHOLE DOCUMENT STANDS OR FALLS ON
>
> **That the shortfall's consequence is already built and only its input is missing.** If
> `body_band_penalty` turns out not to be reached from the live loop, or `(Person, body)`'s MATTER
> half turns out to be forbidden by something not read here, then §A.4 is not *supplying an input to
> a wired mechanism* — it is **building a mechanism**, the object count is wrong, and the N-line at
> §A.4.4 collapses. **The check is two file reads and it was done:** `deliberate.py:116-117` calls
> `decision.budget`, which subtracts `body_band_penalty` at `budget.py:60`; and
> `write_matrix.yaml:161-167` is `steps: [MAT, RES]`. **Both were opened this session.**

---

# APPENDIX · CITATION REPAIRS

Every `path:line` above was opened before it was written (`CLAUDE.md` §0.1 pt 3). These were carried
in from round one or from the round-two plan **wrong**, are corrected silently above, and are recorded
here. **Two of them change a claim rather than a line number and are marked ⚠⚠.**

| cited as | actual | consequence |
|---|---|---|
| ⚠⚠ *"`(Person, body)` is a matrix row **with no writer**"* (round-two plan §2.3; round one `02` §A.6.1's neighbourhood) | **`(Person, body)` has a RES writer: `kill / wound`.** `_eff_kill` sets `p.body` at `effects.py:389`, `:393` and `:403`, and it goes **through the gate** — the effect runs inside `_apply_write`'s `apply()` closure (`resolve.py:327-346`), which `w.write` calls. **The MATTER half is what has no writer** | the loose form invites a session to add a second, ungated body writer. The precise form is what makes §A.4.7's *"not one matrix row is edited"* true |
| ⚠⚠ *"`band_floors`' `body` key is the SITE kind `body` … **not** a person's body; the proposal must not conflate them"* (round-two plan §2.3) | **The tree says the opposite, in three places**: `rosters.yaml:814-815` (*"`body` IS NOT A SITE. It is `(Person, body)`'s band row"*), `budget.py:64-75` (live person-side reader), `hole_register.yaml:793` (*"the `body` row already existed… rather than adding a second band scheme"*). ⚠ **And BOTH are true at once**: `headless.py:64` builds `Site("scriptorium", "hearth_ostvik", "body", …)`, so one key really does serve two subjects | the plan's `band_floors.person` would be a second ladder **and would refuse at load**. §A.4.3 |
| `matter.py:50-51` — the `not_implemented` list (round one `02` §A.6.1; round-two plan §3.3) | **`:49-50`.** The `TRACE.decision` call opens at `:46`; `chose=` is `:47`; `alternatives=` is `:48`; `not_implemented=` is `:49-50` | — |
| *"H-34/H-41 — the two producerless rows `(Rung, exists)`/`(Site, exists)` gain `found`"* (round-two plan §6) | **`H-41` alone.** `hole_register.yaml:462-472` is `H-41`, `kind: "SCHEMA_ROW ×3"`, covering `(Rung, exists)`, `(Office, exists)`, `(Site, exists)`. **`H-34` (`:370-380`) is `kind: "NUMBER"`, `owner: "params"`, `hole: "establishment size per office kind"`** — unrelated | citing `H-34` here would claim a closure over a number nobody has supplied |
| *"`found` closes `H-41`"* | **closes two of its three cells.** `(Office, exists)` is sibling `03`'s (`establish`/`confer`), so `H-41` stays open at reduced strength | §A.7.2 |
| ⚠ `ARCH` PART D row 5 — *"the gate now refuses `before == after` at the write"* (round one `02` §A.4.2, §C.2) | **`World.write` contains no such comparison.** `world.py:408` is `before = apply()` and nothing is compared; the emission block at `:441-469` is unconditional once `emits=` is passed. The refusal that exists is the **fold's** (`resolve.py:259-269`), **ACTS-only** | round one cited a Layer-1 sentence as a live MATTER guarantee. §A.1.3, and it is why §A.4.2 carries its own guard |
| `rosters.yaml:817` — `site_kinds` values (round one `02` §A.2 already repaired this once, to `:816`) | **`:816` is correct**; re-verified. `:809-815` is the note; `:814-815` the `body` clause | the earlier repair holds |
| `requires.py:252-278` — `ContainPath` (round one `02` §A.3.1) | the class is at **`:254`**; the resolver-side branch it observes is `world_q.py:732-737` | — |
| `world_q.py:508-517` / `:518` — Q3's presence gate and referent (round one `02` §A.6.2) | **not re-opened by this document.** Q3 is sibling `01`'s subject; the pointer is carried without a line and the claim is carried without the citation, per the rule that an unlineated true claim beats a fabricated line | stated so the omission is visible |
| `matter.py:164-195` — the larder step (round one `02` §D.15) | the block runs **`:164-192`**; `:193-225` is yield. The shortfall is `:176-185`, the `TRACE.note` closing at `:185`; the gate call is `:188-192` | — |
| `effects.py:262-290` — `_eff_create_record` (round one `02` §A.4) | the decorator is `:262`, `def` at **`:263`**, the stages comment `:267-271`, the hold mint **`:286-289`** | the hold mint is the load-bearing half and its line was right |
| `holonic:536` — `hold`'s domain | **`:538`** (`:536` is the table header, `:537` the separator). Re-verified; round one's repair holds | — |
| `holonic:600` — `share` | **`:599`** `draw_share`, **`:600`** `share` **and** `capacity`, under §17's header at `:591`. Both `share` and `capacity` are declared, which is why both count **0 added** | — |

**Two scope notes, so the appendix is honest about what it does not cover.**
(1) **Nothing in `engine/autoload/`, `engine/substrate/` or `systems/settlements/` was edited or
proposed for edit**; §A.10.2's rows are withdrawals, and a session that reads them as licences has
misread them. (2) **No precedent finding is cited anywhere above.** The one shape round one used — the
garrison convergence — is not needed by this document's subject, and citing Manor Lords, Banished or
Heroes of Might and Magic as a precedent finding would be **inventing one**: the precedent companion
records that the first is *"Absent entirely. Not surveyed, not declared, not cited"* and the second is
named twice and never surveyed on its own terms.

---

**END — `04_MATTER_AND_WORKS.md`. PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Grade: `paper`.**
