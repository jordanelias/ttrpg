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
