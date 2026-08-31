# F4 — ADJUDICATION: the season loop and the execution path

Adjudicator lane: season loop + execution path. Read-only over `/home/user/ttrpg`; this file is the
lane's only write. Date: 2026-08-31.

---

## 0. METHOD, and what I verified myself

Primary sources read directly, not inherited from trace logs:

- `proposals/2026-08-31-ideal-v2/02_THE_SEASON_LOOP.md` — **all 1,206 lines**.
- `proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md` §4 (`:816-874`), §6 (`:1448-1473`), §7 D-2/F1
  (`:1475-1560`), section map.
- `proposals/2026-08-31-ideal/10_SUPERSEDING.md` §5.5-§7.1 (`sed 600-720`) — the seven-phase table
  and three-write-class table, verbatim.
- `engine/autoload/engine_clock.py` — **in full** (127 lines).
- `engine/mc_v18.py` — the callback, stubs, `run_campaign` loop (`:110-300`); dataclass fields per R1.
- `engine/substrate/keys.py:422-601` — `TickScheduler` in full: emission paths, OF-7 deferred-apply,
  `accounting_boundary()`, `next_tick()`.
- `references/module_contracts.yaml:1128-1141` — the `engine_clock` `doc: null` row, verbatim.
- `registers/editorial_ledger_in.jsonl:57` — **ED-IN-0201 in full** (quoted at §8).
- `proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md:713-720, :886` — observation O-2.
- `tools/m1_acceptance.py` — grepped for writes first (`open(path, encoding=...)` read-mode at `:207`,
  print-only output at `:416`), then **executed `--summary` myself**: verdict `NOT MET`, row 4 `0/7`,
  row 1 `2 stub_resolve` hits, row 2 PASS (`641aa8c55c3e…`).
- `tests/valoria/` (167 files) and `engine/tests/` (15 files + goldens) enumerated;
  `tests/valoria/test_engine_clock_phases.py:1-33` read; `engine/tests/test_f7_smoke_oracle.py:361-371`,
  `engine/tests/test_world_population.py:1-30`, `systems/world/sim/npe.py:105-122`,
  `engine/mc_v18.py:100,310` read to verify the npc-counter guard-blindness claim myself.
- Trace logs R1/R2/R6 and PR337/338/343/344 logs read as secondary sources; every load-bearing claim
  below re-cites the primary file:line I checked.

Adversarial posture: I tried to break the six-step design's two central claims (that it is the first
`engine_clock` contract, and that it does not conflict with running code) before ruling. Both broke
partially; the rulings below carry the damage.

---

## 1. ⭐ THE THREE COMPETING LOOPS, RULED

### 1a. The seven-phase season (PR #343, `10_SUPERSEDING.md` §6.2)

Reproduced from `10_SUPERSEDING.md` (read via sed, §6.2 table): **P0 CALENDAR · P1 SETTLE · P2 NEEDS ·
P3 VIEW · P4 CHOOSE · P5 RESOLVE · P6 WITNESS · P7 RECKON**, "phases run in order; within a phase
everything is simultaneous." Three write classes bound one-to-one to phases (§6.3): calendar→P0,
matter→P1, acts→P5 — "There are exactly three write classes, and no others may be added."

Two internal defects, found on read:
- **The header says "SEVEN PHASES" over an eight-row table.** P0…P7 is eight entries. Either P0 is
  being counted as phase zero or the doc miscounted its own spine; either way the number in the
  title is not the number in the table. [minor, but a spine document should count its own spine]
- **The reckoning operations (P7: decay, eviction, individuation, de-individuation) have no write
  class.** They are not calendar, not matter, not acts — so under §6.3's own closed-class rule, P7
  performs unlicensed writes. `02_THE_SEASON_LOOP.md:115-118` states this exact defect as its reason
  for the fourth class, and it is correct.

### 1b. The six-step loop (PR #344, `02_THE_SEASON_LOOP.md` — current head)

Reproduced from `02:38-94`: **CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS**; four
barriers (CALENDAR, MATTER, RESOLVE, WITNESS — `02:96-112`); DELIBERATE is a pure per-person map,
CENSUS a global pass sharing WITNESS's join; four write classes (CALENDAR / MATTER / ACTS / INTERIOR,
`02:114-132`), with a class explicitly *not* a phase — MATTER-class writes happen at both MATTER and
CENSUS (`02:129-132`). Word-only step names, letter-number spellings banned (`02:30-32`). Its own
status line: "Nothing here has executed… done means it runs, and none of this runs" (`02:3-5`), and
"This document is REFERENCE, not mechanism" (`02:1204-1205`).

### 1c. The running three-phase tick — the actual code

`engine/autoload/engine_clock.py:73-77` exports the three phase names; `run_tick` (`:115-127`)
composes, in order:

```python
result = advance_season(world)                       # --- SEASON_TICK ---
if action_callback is not None:
    action_callback(world)                           # --- ACTION ---
sched = scheduler_of(world)
if sched is not None:
    sched.accounting_boundary()                      # --- ACCOUNTING_BOUNDARY opens ---
composition.require('accounting')(world)
if sched is not None:
    sched.next_tick()                                # --- tick closes ---
```

This runs today: `mc_v18.run_campaign` calls `composition.require('season_driver')` every season
(`mc_v18.py:271`), which resolves to `season.run_season` wrapping `run_tick`; the ACTION body is
`_faction_actions_callback` (`mc_v18.py:124-215`). Phase ordering is pinned by
`tests/valoria/test_engine_clock_phases.py` (falsifier `test_accounting_runs_inside_the_accounting_phase`,
red against the pre-move tree per its docstring `:30-33`), and campaign output is pinned by byte-exact
seeded goldens (`engine/tests/test_mc_v18_regression.py`, `test_f7_smoke_oracle.py`,
`test_parliamentary_bridge.py`'s `_ON_KEYLOG_HASH`). The barrier semantics are real code:
`keys.py:_emit_at_depth` defers an `apply` iff `self._phase == _PHASE_ACTION` (OF-7);
`accounting_boundary()` (`keys.py:585-596`) drains pending applies in emission order and flips phase;
`next_tick()` (`keys.py:598-601`) raises `TerminationBreach` on an undrained queue and resets the
tick-wide emission cap.

### THE RULING

**The six-step loop is a REFINEMENT of the three-phase tick, not a replacement — and it is only
acceptable as a refinement.** The seven-phase P0–P7 season is **retired** (it is already superseded by
its own successor: `02` corrects it on four argued points — WITNESS globality, the unlicensed P7
writes, class-vs-phase, and the barrier count — and each correction is right; see §10). The three
loops resolve as:

| loop | disposition |
|---|---|
| three-phase tick (`engine_clock.py`) | **AUTHORITATIVE MECHANISM.** Per CLAUDE.md §0.05, the code is the formula. It stays the single owner of tick composition; nothing may build a rival driver. |
| six-step loop (`02_THE_SEASON_LOOP.md`) | **AUTHORITATIVE CONTRACT (design reference), adopted with the amendments in §3**, to be implemented *inside* `run_tick`, never beside it. |
| seven-phase P0–P7 (`10_SUPERSEDING.md` §6.2) | **RETIRED — superseded by `02`.** Quotable as history only; its three-class table must not be cited (it cannot license P7). |

**Why refinement is answerable from the code, not from prose.** `run_tick` was *built* to be refined:
its ACTION body is caller-supplied (`engine_clock.py:91-95` — "the dispatch policy differs between the
batch sim, an interactive Godot session, and a test injecting deterministic actions"), and its own
docstring disclaims implementing the full drain topology (`engine_clock.py:12-18` — "This module is
the SEAM… Growing it is a separate, non-neutral change"). The mapping that makes the six steps a
decomposition of the three phases, with each seam named:

| tick phase (code) | six-step content | seam |
|---|---|---|
| SEASON_TICK (`advance_season`) | **CALENDAR** — the date advance already lives here (`season_manager.py:29-38`: season+=1, arc rollover, seasonal resets). Dates/dockets/convening conditions are additive growth of this phase. | clean |
| ACTION (`action_callback`) | **MATTER → DELIBERATE → RESOLVE** — the scheduler stays `_PHASE_ACTION` throughout, so OF-7 keeps deferring settlement-locus applies exactly as today. | ⚠ two seams, below |
| ACCOUNTING_BOUNDARY (`accounting_boundary()` + `run_accounting` + `next_tick()`) | **WITNESS → CENSUS** — the join. The existing boundary already IS a barrier that legitimately writes (it drains OF-7 applies and lets accounting write immediately, `keys.py:568-575`), which is the running-code precedent for `02`'s "two barriers legitimately write" claim. | clean in shape |

The two real seams, stated so nobody discovers them mid-implementation:

1. **`run_accounting` runs after ACTION today; MATTER runs before deliberation in the design.**
   `systems/overview/sim/accounting.py`'s world-self-writes (track drift, NPC stance drift via
   `simulate_npc_actions` — `mc_v18.py:174-182` comment) are MATTER-class work sitting in the
   boundary phase. `02:257-259` requires "events resolve FIRST, and acts resolve against the world
   they leave." Migrating accounting's matter-half to a pre-deliberation position is a
   **golden-moving reorder** and is sequenced late in §6 (step 8) with a mandatory control. Until it
   lands, accounting stays where it is — the interim state is "aggregate-layer MATTER runs at the
   boundary," which is wrong per the contract and correct per the code, and the code wins until the
   migration executes (§0.05).
2. **WITNESS and CENSUS have no code home at all** — no `Claim`, no per-person ledger, no
   individuation (R1 §7: zero of the design's ~22 objects exist as first-class engine types;
   independently confirmed by grep per R1 §11.4). They are net-new growth at the boundary phase.

**What replacement would cost, so the refusal is priced:** orphaning `engine_clock` would orphan the
phase machine that OF-7, B1 no-sync-reentry, and the tick-wide emission cap hang off
(`keys.py:422-601`), the phase-pinning test, the byte-exact goldens, and `propagation_spec_v1.md`
§O.1 — CANONICAL since 2026-07-02 and quoted as the module's own charter (`engine_clock.py:5-11`).
That is the entire determinism surface of the only thing that runs. Refusal is not conservatism; it
is arithmetic.

**R2's framing is corrected in passing:** R2 §8 said the six-step granularity "has no precedent
against the CANON three-phase tick." It has exactly one precedent — *as a refinement*, via the seams
above. What it lacked was a stated mapping. The mapping is now stated; a session implementing the
loop implements the mapping, not a new spine.

---

## 2. ⭐ IS THIS THE MISSING `engine_clock` CANON? — ruling on O-2

**O-2 as written** (`04_GODOT_IMPLEMENTABILITY.md:713-720`): the six steps + four barriers + four
write classes + the write matrix "IS that specification," citing `module_contracts.yaml:1128-1136`
(`doc: null`, verified — `engine_clock` is one of the **nine** `doc: null` modules per CLAUDE.md §6's
corrected parse; a naive grep returns 10, the tenth inside a quoted string).

**RULING: UPHELD WITH A CORRECTION THAT CHANGES WHAT GETS WRITTEN.** `02:15-22`'s banner — "THIS
DOCUMENT IS THE `engine_clock` CONTRACT, AND IT HAS NEVER EXISTED… nobody had written what a tick
does" — is **overstated and partly false**. A tick contract exists at coarse grain:
`systems/_architecture/propagation_spec_v1.md` §O.1, CANONICAL since 2026-07-02, states the exact
composition "SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY" and single ownership — quoted verbatim in
`engine_clock.py:6-11`, which was built to implement it. What has never existed is the **fine-grain**
contract: what happens *inside* each phase, who may write what, and the barrier/write-class algebra.
`02` supplies that, and nothing else in the tree does (R2 §8: no `systems/` doc proposes the
MATTER/DELIBERATE/WITNESS/CENSUS split).

**What must be written, and where:**

1. A design doc at `systems/_architecture/engine_clock_v1.md` (or the systems-side home CURRENT.md
   assigns), whose §1 is the reconciliation table from §1 above — it must cite **both**
   `propagation_spec_v1.md` §O.1 (the ratified coarse grain it refines) and
   `proposals/2026-08-31-ideal-v2/02_THE_SEASON_LOOP.md` (the fine grain), and must state the two
   seams (accounting reorder; WITNESS/CENSUS net-new). Filing it flips
   `module_contracts.yaml:1130`'s `doc: null` to a real pointer and updates the row's `emits:` to
   include `mechanical.season_change` (currently one of the two unconsumed-by-name keys per my
   `m1_acceptance` run).
2. Its ratification rides an ordinary PR under ED-1094 — but because it **refines ratified canon**
   (§O.1), the PR body must call that out loudly per CLAUDE.md §2's held-back rule, not bundle it
   silently.
3. Per §0.05 the doc is reference. The *mechanism* half is §6's execution path: the doc closes
   `doc: null`; only code closes the juncture.

**What the competing-spine reading would cost** (if O-2 were read as "adopt `02` and deprecate
§O.1"): re-ratifying a canonical spec that running, golden-pinned code implements, for zero
behavioural gain — the exact "prose declared authoritative over code" move §0.05 forbids.

---

## 3. ⭐ THE AUTHORITATIVE LOOP

**Adopted: six steps, four barriers, four write classes, per `02_THE_SEASON_LOOP.md`, nested in the
three-phase tick per §1's mapping.** Word-only names, no letter-number spellings (`02:30-32` — the
B1/M1 citation-collision rationale is sound; this repo already burned on exactly that). Amendments
are marked ⊕.

### Steps, with reads / writes / invariants / refusals / closing barrier

| step | reads | writes (class) | key invariants | closing barrier |
|---|---|---|---|---|
| **CALENDAR** (`02:159-244`) | dates, live convening conditions (predicate may read ONLY holder's own state, an R-1 on-demand descendant aggregate, or the calendar — `02:196-199`), option-enabling claims | dates, dockets (CALENDAR) | fires occasions, decides nothing; vacant-allocator semantics (`02:181-191`) — a vacant date fires, allocates nothing, lapses; step 4 re-evaluates suppressed-grievance enabling conditions (`02:219-232`) | itself — barrier 1 |
| **MATTER** (`02:247-378`) | frozen prior state, per-op substreams | matter, bodies, travel, `yield` roll, envelope weights (births/deaths), `condition -= wear` — MATTER class; existence of non-social subjects | events resolve first; no social quantity moves; no act's effect lands; death sets `until` on Tenures but does NOT open the conferral Date (CALENDAR does, next tick — `02:333-344`) and does NOT propagate (news travels — `02:346-353`); birth is envelope weight, not `mint` (`02:355-360`) | itself — barrier 2; world frozen after |
| **DELIBERATE** (`02:381-513`) | frozen world via `sense` (two floats only), own ledger via `assemble`, own remits | **nothing but the returned Act** (no class) | pure map, any order; `opening_set` is belief and can be wrong (`02:454-464`); one act per person or cohort, universally (`02:483-500`, ARCH §7 D-2) | none — it is a map, not a barrier |
| **RESOLVE** (`02:516-812`) | declared Acts (`changes[]`/`reads[]`/`contests[]`), world | everything else (ACTS), incl. every act-caused `condition` delta | touch-graph conflict rule (`02:541-565`); five strata (`02:584-597`); one roll, one obstacle, refusal at `Ob > 2×Pool` with the season still spent (`02:627-630`); sum-then-clamp-once (`02:570-576`); tie-break `H(act_id, world_seed)` | itself — barrier 3 |
| **WITNESS** (`02:815-915`) | this season's Events, presence/channels/Knots | one person's own ledger only (INTERIOR) | fan-out global, deposit per-person (`02:834-841`); Knot deposits reuse the event id (corroboration fails closed); four claim constructors, no fifth; eviction on `confidence_live × recency` only, never salience (`02:883-902`) | itself — barrier 4 (the join) |
| **CENSUS** (`02:919-1025`) | the post-eviction ledger set, read ONCE | the population: individuation/de-individuation, envelope-weight reconcile (MATTER class) | demand-driven only — "nothing generates without a demand," no clock (`02:1018-1022`); weight-1 record IS a person, no conversion op | shares WITNESS's join — no barrier of its own |

### The write matrix — reproduced (from `02:1080-1093`, adopted verbatim)

| written thing | CALENDAR | MATTER | DELIBERATE | RESOLVE | WITNESS | CENSUS |
|---|---|---|---|---|---|---|
| `Date`, `DocketItem` | **yes** | no | no | **yes** (`carry`, `convene`) | no | no |
| larders, `stores` | no | **yes** | no | **yes** (`transfer`, `levy`) | no | no |
| bodies, ageing, death | no | **yes** | no | no (killing is ACTS-class an act's effect) | no | no |
| travel legs | no | **yes** | no | **yes** (movement, stratum 1) | no | no |
| `yield` | no | **yes**, only here | no | no | no | no |
| envelope weight | no | **yes** | no | no | no | **yes** |
| `condition(site)` | no | **yes — `wear` ONLY** | no | **yes** — act deltas, only here | no | no |
| `Tenure` | no | **yes** (`until` on death) | no | **yes** | no | no |
| carrier existence | no | **yes** (death) | no | **yes** (`mint`/`efface`) | no | **yes** (individuation) |
| `stance` | no | no | no | **yes** | no | no |
| ledger | no | no | no | no | **yes**, own only | no |
| returned `Act` | no | no | **yes** | — | no | no |

Any unmarked cell is a write-class violation.

### Is a write class a phase? RULED: NO — and the running code already practices this.

`02:129-132`'s argument is upheld, and it has an execution-side witness the document never cites:
the ACCOUNTING_BOUNDARY today both drains ACTION-phase deferred applies *and* accepts immediate
applies from accounting emissions (`keys.py:568-575` — defer only when `_PHASE_ACTION`). One write
class (settlement-locus effect), two phases writing it, by ratified design (OF-7, 2026-07-07). The
class-not-phase rule is therefore not a novelty of the proposal; it is how the only running barrier
already behaves. The seven-phase table's class-per-phase binding is retired with it.

⊕ **Amendment 1 (interim accounting).** Until §6 step 8 executes, `run_accounting`'s writes are
MATTER-class work performed at the boundary. This is a declared, temporary matrix violation, named
here so no session "fixes" it by moving code without the mandated control.

⊕ **Amendment 2 (ordering rule, exact).** The authoritative season ordering is: barrier 1
(CALENDAR) → barrier 2 (MATTER, world freezes) → map (DELIBERATE, unordered) → barrier 3 (RESOLVE:
strata 1–5, hash tie-breaks, batch-clamp) → barrier 4 (WITNESS fan-out then per-person deposit,
unordered) → CENSUS against the single post-eviction snapshot → `next_tick`. Inside the tick
machine: CALENDAR ∈ SEASON_TICK; MATTER/DELIBERATE/RESOLVE ∈ ACTION; WITNESS/CENSUS ∈
ACCOUNTING_BOUNDARY.

---

## 4. ORDER INDEPENDENCE AND THE PARALLELISM LICENCE

**The claim, precisely** (`02:134-156`, `02:1109-1128`): four properties — (i) previewing cannot
change outcomes; (ii) two attempts resolved in different order give the same answers; (iii) adding a
person re-phases no other roll; (iv) the DELIBERATE map may run in any order at any concurrency.

**What it rests on:** (i)-(iii) on per-operation substreams `H(world_seed, tick, subject_id,
purpose)` (ARCH §6) — never a shared sequence, never a counter; (iv) on three repairs the v2 pass
made: individuation/de-individuation moved out of the map into CENSUS (the de-individuation predicate
reads *other* ledgers — order-dependent inside a map, `02:936-948`), hash-derived ids (no allocator),
and INTERIOR writes only.

**Does it survive?** As an *argument*, yes — I found no shared mutable state the document missed,
and its own stated limit is honest ("a reading found none rather than that a run found none,"
`02:1201-1203`). As a *property*, no: nothing enforces it. The document's own §10 names the soft
spot — `sense` takes a World and only convention keeps it to two floats (`02:1120-1125`). Structural
test 1 (§7) is the enforcement.

**The float-summation problem — what the LOOP requires of the fixed-point lane.** `02:570-576` is
correct that clamp-as-you-go breaks commutativity and that step 6's sum-then-clamp-once repairs it.
**But the repair is incomplete over IEEE floats: addition is not associative, so "SUM deltas" has an
order-dependent value at the ulp even before the clamp.** This repo has already shipped that defect
class once — a 1-ulp aggregate error crossed a damage-degree boundary while the identity test passed
(CLAUDE.md §0.1 pt 2) — and the determinism surface here is *byte-exact* (`KeyLog.content_hash`,
`keys.py:459-461`; the `sim-regression` CI job runs serial precisely because parallelism would race
the seeded oracle, per R6 §6). The fixed-point ruling belongs to its own lane; **what this lane
requires of whatever it rules** is one of exactly two shapes, stated as an obligation:

- **(preferred) every field declared `additive` accumulates in integer fixed-point units** — exact
  addition is associative, so the parallelism licence survives arbitrary join order; or
- **the RESOLVE join canonically sorts deltas before summation** (key: `H(act_id, world_seed)`, the
  tie-break hash that already exists) — bit-exact but serializes the join, spending part of the
  parallelism licence to keep floats.

A third option — "floats, unsorted, approx-compare" — is refused: it makes structural test 4
unable to observe its own failure (§0.1 pt 2: `pytest.approx` on an exactness claim is an absent
assertion).

**What CENSUS is for**, in one sentence: it converts the two genuinely global population reads —
de-individuation's cross-ledger predicate and individuation's minting of addressable objects — from
a race inside the map into a single barrier read of one post-eviction snapshot (`02:936-948`). It is
required for order-independence of the *map*; it is not a birth/death pass (that is MATTER, `02:355-360`).

---

## 5. DETERMINISM ACROSS THE LOOP

**As built** (verified in code): one seeded stream, `World.rng = random.Random(seed)`
(`game_state.py:306`), passed explicitly to faction actions, scene dispatch, and the parliamentary
bridge (`mc_v18.py:138,149,158` region); sub-stream derivation at the combat bridge
(`combat_bridge.py:140`, `random.Random(rng.getrandbits(32))`); one documented global-state
save/restore around the contest kernel (`scene_dispatch.py:299-306`); replay surface =
`KeyLog.content_hash()` (sha256 over sorted-key JSON per Key in log order, `keys.py:454-461`) plus
byte-exact seeded goldens (`test_mc_v18_regression.py:126-132` — n=2 seed 0 win-share/winners/battles
and a same-seed equality assertion; `test_f7_smoke_oracle.py` — n=8 seed 42 plus telemetry pins).

**As designed**: `substream(op) = H(world_seed, tick, subject_id, purpose)` (ARCH §6), covering
actorless rolls (`yield`) and `mint`. Two die readings, pool and magnitude, both declared.

**Ruling:** the design's scheme is the correct generalisation of the pattern the code already uses
at its best seam (`combat_bridge.py:140`) and the direct fix for the code's measured worst defect —
**loading 2 NPCs moved the seed-42 winner purely by shifting the shared stream's phase** (integration
master F1, `_part4.md:70-76` via R6 §1). Adopt it. What makes a replay identical: same seed, same
code path, same substream keys. What breaks it, in current code: any new draw inserted into
`world.rng`'s sequence (the F1 hazard — this is the channel the NPC loader must NOT use, §8); the
global-`random` seam if any new caller touches it outside the save/restore idiom; float summation
order once RESOLVE batching lands (§4); and the uncontrolled golden re-pin path CLAUDE.md §7 names
(nothing verifies a regeneration was intended).

---

## 6. ⭐ THE EXECUTION PATH

Per §0.2, every step ends in something running, with the artifact named. Step 1 is executable
against the current tree this week. Order is chosen so determinism-neutral work lands first
(integration master F10's attribution rule) and every golden-moving step carries its control.
"balance_oracle" = `tools/balance_oracle.py` (n≥100 campaign instrument, deliberately not CI —
CLAUDE.md §7); byte-identity = five seeded campaigns + both pinned batches compared field-by-field
including `key_log_hash` (the `engine_clock.py:44-51` control, re-used).

| # | what gets built | execution artifact that proves it | what it unblocks | size |
|---|---|---|---|---|
| 1 | **Season-close emitter**: `mechanical.season_change` emitted at SEASON_TICK and `mechanical.accounting` at the boundary, via the existing scheduler, flag-gated by scheduler presence like everything else | `pytest engine/tests` green with the two keys visible in the KeyLog; my `m1_acceptance` row-3 "2 unconsumed by name" reads differently; flag-OFF path byte-identical (control); flag-ON `_ON_KEYLOG_HASH` re-pinned with an intentional note | **M1 juncture 6** (board: "emitter missing… consumer already built and tested"); makes the running tick observable | S (~50 LOC + test) |
| 2 | **Person loader v0** (ED-IN-0201 precondition): `create_world` gains a default-OFF `PERSONNEL` param; ON, it mints one leader per faction (4) and fills `Settlement.governor_id` **through `generate_npc`** (`npe.py:226`) so `npc_counter` moves and every guard sees it, drawing from `H(seed,"worldgen",faction)`-style derived streams, **never `world.rng`** (the F1 channel) | flag OFF: full byte-identity across goldens (the §0.1-pt-4 control arm); flag ON: seeded campaign completes with `npcs_generated == roster size`; `test_f7_smoke_oracle.py:371`'s `npcs == 0` guard updated on the ON arm only, citing this step | ED-IN-0201 clause 1 becomes satisfiable; unblocks 8 systems per the synergy matrix | M |
| 3 | **The gate** (clause 1): with PERSONNEL on, `_faction_actions_callback` requires a living leader before `faction_action`; a leaderless faction acts zero times | a test that kills a leader mid-campaign and asserts that faction's action count freezes; balance_oracle A/B (OFF vs ON, same seeds) recorded — the mandated MOVES-class control from ED-IN-0201's own text | faction collapse gets its mechanism; `succession` contest becomes reachable | S-M |
| 4 | **The decider** (clause 2): `npc_ai.select_action` de-stubbed into the first real `choose(person, view₀, sensation₀) -> Act` — identity changes the **option set** (conviction/ethic gates candidates), never a modifier (the NERS flat-shift trap, per ED-IN-0201) | `stub_hits` on the M1 probe drops 2→1 (m1_acceptance row 1 measurably improves); A/B test: two different leaders, same seed, divergent action mixes; structural test 1's harness lands here (§7) | the `choose` signature exists in running code; DELIBERATE has a beachhead | M |
| 5 | **engine_clock canon + CALENDAR v0**: file the §2 design doc (closes `doc: null`); implement minimal `Date`/docket firing inside SEASON_TICK | the doc PR (reference); a test that a Date scheduled at tick t fires at tick t+h; `test_engine_clock_phases.py` extended, still green | the loop's first step exists as code; conferral-date flow for step 3's dead leaders | M |
| 6 | **WITNESS v0**: `Claim` type + per-person ledger + `witness(person, key) -> claims` over the existing Key fan-out (`Visibility` already carries the observer sets, `keys.py:100-111`) | structural test 2 (two witnesses disagree) green — first of the four ever to run; KeyLog hash untouched (INTERIOR writes only — that byte-identity IS the control) | the epistemic layer executes; withheld-news mechanics become buildable | L |
| 7 | **RESOLVE batching**: additive-field accumulator, sum-then-clamp-once at the boundary, fixed-point per the other lane's ruling (§4's obligation) | structural test 4 (order independence, incl. the clamp-boundary triple) green; byte-identity on all paths not using the accumulator | the parallelism licence becomes testable instead of asserted | M-L |
| 8 | **MATTER v0 + the reorder**: `wear`/`yield` minimal; `run_accounting`'s matter-half moves pre-deliberation | golden-moving by design: balance_oracle both arms + full re-pin with commit-message note naming this step; `test_engine_clock_phases.py` amended deliberately | the write matrix stops carrying Amendment 1's declared violation | L |
| 9 | **CENSUS v0**: the Named trigger only (demand-driven mint — "the praefect fines a smuggler and the engine must produce one") | structural test 3 (officeless person acts, petitions, receives an opportunity) green; population moves in a seeded run and `npc_counter` accounts for every mint | the population loop closes at its smallest honest scope | M |

Steps 1–4 are executable against the current tree with no new architecture. Every later step builds
on an artifact a prior step produced. Nothing in this table is done when its document exists.

---

## 7. ⭐ THE FOUR STRUCTURAL TESTS, SPECIFIED

All four target `tests/valoria/` (pytest, CI job `unit-tests`). Each names its falsifier (§0.1 pt 3)
and each assertion can observe the failure it excludes (§0.1 pt 2 — including asserting that it
asserted).

**T1 — no decision function can see the world.** *Setup:* import the module owning `choose` (step 4's
`npc_ai` successor) in a subprocess, modeled on
`tests/valoria/test_engine_does_not_import_systems.py`'s probe. *Assertions:* (a)
`inspect.signature(choose)` has no parameter typed/named `world`; (b) an AST walk over `choose`'s
module finds no reference to `engine.autoload.game_state` or any singleton accessor, and no read of
the event log; (c) **the scanner is proven able to fail**: a fixture module that deliberately reads
`game_state` is scanned and the test asserts it IS flagged, and `assert modules_checked >= 1`.
*Falsifier:* add a `world` parameter or a `game_state` import to `choose`'s module — (a)/(b) go red;
delete the fixture — (c) goes red. *Caveat carried:* in GDScript this downgrades to
"unreachable-by-name" (autoloads are globals — the guarantee was already found unenforceable there
per the design's own commit history via R6 §4.1); the Python test is the oracle-side enforcement and
the port must carry an explicit-World-first-arg convention instead.

**T2 — two witnesses of one event can disagree.** *Setup:* one `Key` with two observers of different
vantage/marks (step 6's fixtures); call `witness(p1, e)` and `witness(p2, e)` — two calls, never a
collection (the collection signature must not exist to call). *Assertions:* both return non-empty
claim lists (`assert len(c1) and len(c2)` — observing the vacuous case); the claims have distinct
ids AND differ in value or construal; each deposited only into its own ledger (the other ledger's
length is unchanged — observing an INTERIOR breach). *Falsifier:* implement `witness` as a broadcast
writing one shared claim object — the distinct-id assertion fails; implement it reading the other
ledger — the length assertion fails.

**T3 — a person with no office can act, petition, and receive an opportunity.** *Setup:* a minted
Person holding zero `hold` Tenures over any Office (step 9). *Assertions:* `opening_set(person,
view)` is non-empty (`assert len(openings) >= 1`); it contains `petition`; a chosen act reaches
RESOLVE and produces an Event (not a refusal-by-eligibility — refusal-by-obstacle is legal);
`assert resolved_count >= 1`. *Falsifier:* gate `opening_set` or the resolver on office-holding —
the set empties or the act is refused, and the test observes exactly that. This encodes
`02:509-513`'s row: office changes whether a decision *binds others*, never whether you may act.

**T4 — order independence.** *Setup:* N=6 acts against one world snapshot, including the §5.2 poison
triple — three `alter`s of `+0.3, −0.5, +0.3` on one `additive` `[0,1]` field sitting at 0.9 — plus
one conflicting pair (an `efface` racing a `mint` on the same parent). *Assertions:* over ≥10
permutations of submission order (sampled + both extremes): the canonicalized Event list is
identical; the post-state hash is **bit-identical** (not approx — §4's refusal); the conflict pair
routes to `contest` in every permutation; `assert permutations_run >= 10`. *Falsifier:*
clamp-as-you-go fails the poison triple (0.9→1.0→0.5→0.8 vs 0.9→0.4→0.7→1.0-clamped orderings
diverge); a sequence-position tie-break fails the Event-list identity; float accumulation without
the §4 obligation fails the bit-identity at the ulp — which is precisely the failure the assertion
must be able to see, and approx-comparison would blind it.

---

## 8. ⭐ THE ZERO-PEOPLE PROBLEM AND ED-IN-0201

**The ruling, quoted in full** (`registers/editorial_ledger_in.jsonl:57`; Jordan's words verbatim
inside it):

> "PERSONNEL PRECONDITION — RULED BY JORDAN, THIS SESSION, NOT EXECUTED. Verbatim: 'all faction
> actions, settlement governance, mass battles, etc are predicated upon people existing. we do not
> allow the game to perform faction actions if there is no leader of that faction, and that leader
> themselves is going to influence what choices are made for available faction actions in the same
> way that the person(s) who are governing a settlement or conducting a battle may make different
> choices with the same information and options.' Filed status:open and NOT needs_jordan — Jordan
> has ruled; what is missing is execution. TWO CLAUSES, and they are separable. (1) THE GATE: no
> leader, no faction action; no governor, no settlement governance; no commander, no battle (the
> third is the one genuine ambiguity — see below). (2) THE DECIDER: the person shapes WHICH action
> is chosen from the same option set with the same information. Clause 2 is presence-as-identity,
> not presence-as-a-stat… THE BOOTSTRAP CONSEQUENCE, which is the load-bearing one: under clause 1,
> with world.npcs empty, a campaign performs ZERO faction actions. The ruling therefore promotes the
> person loader from an enhancement to a PRECONDITION OF THE ENGINE RUNNING… NERS NOTE: clause 2
> must not be implemented as a flat trait bonus on the selection roll… the leader changes the OPTION
> SET and the POOL SOURCE, not a modifier… ONE GENUINE AMBIGUITY, flagged rather than decided: 'no
> commander, no battle' has two readings… (a) a faction with no available commander CANNOT declare a
> conquest, or (b) it can, and an unled army fights at a penalty… IMPACT CLASS: MOVES, at the
> largest scale in the tree — it changes which actions occur, so every seeded golden moves and a
> balance_oracle control is mandatory."

(Full entry also names the measured state; elided here only for length — the ledger row is the
source.)

**Current state, established from code by me:** `Faction` has no leader field
(`game_state.py:109-140` region per R1 inventory, corroborated by the ledger's own read);
`_faction_actions_callback` gates on exactly `faction.parliamentary` and `faction.territories`
(`mc_v18.py:132-137`) then acts unconditionally; `generate_npc` has no live call site — both season
hooks are honest `stub_resolve` deferrals (`mc_v18.py:193-215`), and my `m1_acceptance` run measured
exactly those 2 stub hits on the probe season; `npcs_generated` is `world.npc_counter`
(`mc_v18.py:100,310`), incremented only inside `generate_npc`'s id path (`npe.py:117-122`);
`test_f7_smoke_oracle.py:368-371` asserts `npcs == 0` across the pinned batch. **The guard blindness
is confirmed:** a loader that appends to `world.npcs` directly never touches `npc_counter`, so both
the F7 telemetry pin and the population guard stay green while the world silently gains people —
which is why §6 step 2 REQUIRES the loader route through `generate_npc`.

**What must land, in order:** loader (flag-OFF-neutral) → gate → decider — §6 steps 2-4. **What
breaks when it does:**

1. **The RNG-phase channel.** Any loader draw taken from `world.rng` shifts every subsequent draw in
   the campaign — the measured F1 effect (2 NPCs moved the seed-42 winner). Mandate: the loader
   draws only from derived substreams (`combat_bridge.py:140`'s idiom, or ARCH §6's hash scheme).
   This makes the flag-OFF arm provably byte-identical and makes the flag-ON deltas attributable to
   the *gate and decider*, not to stream phase.
2. **The `npc_counter` guard blindness** — closed by construction (route through `generate_npc`),
   plus one new guard in the `test_morale_write_sweep.py` pattern: assert
   `sum(len(v) for v in world.npcs.values()) == world.npc_counter` after any campaign, so a future
   bypass loader trips loudly.
3. **The seeded goldens move** — `GOLDEN_WIN_SHARE`/`GOLDEN_WINNERS`/`GOLDEN_BATTLES_MEAN`
   (`test_mc_v18_regression.py:126-129`), the f7 pins, `_ON_KEYLOG_HASH` — on the flag-ON arm only.

**The §0.1-pt-4 control, specified:** two arms, same experiment. **Arm A (control):** head +
loader code, `PERSONNEL` OFF — must be byte-identical to head across five seeded campaigns and both
pinned batches including `key_log_hash`; this proves the wiring itself is inert. **Arm B:**
`PERSONNEL` ON, same seeds — goldens re-pinned in the same commit, with `balance_oracle` (n≥100,
identical seed list both arms) reporting the win-share table for OFF vs ON side by side, so the
behavioural delta is measured rather than banked. The gate (step 3) and decider (step 4) each repeat
Arm-B's oracle run against the previous step's ON-state, so the three MOVES-class changes are
attributed separately — F10's exact warning ("eight cheap writers landed together are unmeasurable")
applied to three.

---

## 9. WHAT THE LOOP REFUSES — authoritative list, with enforcement class

M = mechanical (a type/test/code shape makes the violation unwritable or red); C = convention (prose
someone must honour). Today, with nothing executing, every row is C; the class below is what each
becomes when its §6 step lands.

| refusal | source | class when built |
|---|---|---|
| CALENDAR decides nothing, schedules only dates | `02:238-244` | C (code review) — no natural type gate |
| no petition ends by a fact about the world | `02:243` | C |
| no act's effect lands at MATTER; `wear` is MATTER's only `condition` writer | `02:283-299` | **M** — write-matrix test over the accumulator's call sites |
| `choose` sees no `World` | `02:505-507` | **M** in Python (T1); C in GDScript (unreachable-by-name only) |
| no decision function reads the event log | `02:511`, `SUP:613-615` | **M** — T1's AST clause |
| DELIBERATE writes nothing global; mints nothing | `02:508-510` | **M** — return-type shape + T4 |
| resolver takes no `Person`; branches on no verb, event kind, or named entity | `02:803-807` | C, partially M (a grep-ceiling test in the `test_engine_does_not_import_systems.py` style is cheap and warranted once the resolver exists) |
| no second resolver / auto-resolve / fast path; three fidelities differ only in who chooses | `02:808` | C — this is the one refusal only discipline enforces, and Total War's 20-year divergence is the cost of losing it |
| `Ob > 2×Pool` refuses the roll; season still spent; refusal is a witnessed Event | `02:627-630` | **M** — resolver branch + test |
| ties break on `H(act_id, world_seed)`, never rank/office/position | `02:539-540` | **M** — T4 |
| consensus broadcast is a type error — `witness` takes one person | `02:845-848` | **M** — the collection signature is never written (T2 guards the shape) |
| WITNESS deposits into one ledger; mints roots only here; four constructors, no fifth | `02:906-915` | **M** — constructor closure + T2 |
| eviction ranks on `confidence_live × recency`, never salience | `02:883-894` | **M** — unit test on the eviction comparator |
| CENSUS: nothing generates without a demand; never on a clock | `02:1018-1021` | **M** — the f7-style `npcs_generated` telemetry pin, re-pointed at demand provenance |
| no threshold fires an outcome (matter-band verb closure is the one licence) | `02:1159-1162` | C |
| if no person acts, no *social* thing occurs (Jordan's-partition rescope of no-fallback) | `02:1133-1140` | C, becoming M piecewise as the gate (§6 step 3) lands — the ED-IN-0201 gate is its first mechanical instance |
| no apparatus: the loop ships no validator/register/process doc beyond its named tests | `02:1163-1164` | C — and binding on every session implementing §6 |

---

## 10. WHAT I OVERTURN

1. **`10_SUPERSEDING.md` §6's season (P0–P7) and its three-phase-bound write classes** — retired,
   superseded by `02`. Grounds, each verified: WITNESS's fan-out is cross-person and cannot live in
   a per-person map; P7's reckoning writes are unlicensed under its own closed three-class rule;
   class-bound-to-phase is refuted by the running boundary's own OF-7 behaviour
   (`keys.py:568-575`); and the "SEVEN PHASES" header sits over an eight-row table.
2. **`02:15-22`'s claim that the `engine_clock` contract "HAS NEVER EXISTED" and "nobody had
   written what a tick does."** Partially false: `propagation_spec_v1.md` §O.1 (CANONICAL
   2026-07-02) wrote the tick at coarse grain and running code implements it
   (`engine_clock.py:5-11`). `02` is the fine grain, and must be filed as a refinement of §O.1
   (§2), not as first canon.
3. **Any replacement reading of O-2** — the six-step loop lands inside `run_tick` via §1's mapping;
   no rival driver, ever.
4. **R2's "no precedent" framing** — narrowed: the six steps have exactly one legal relationship to
   the canon tick (refinement via the stated mapping), and it now exists.
5. **Any implementation of ED-IN-0201 clause 2 as a modifier** — already forbidden by the ruling's
   own NERS note; restated here because it is the cheapest wrong implementation and someone will
   reach for it.
6. **Any NPC loader that writes `world.npcs` without `generate_npc`/`npc_counter`** — overturned
   pre-emptively as a guard-invisible write (§8's confirmed blindness).

Not overturned: ED-IN-0201 (ruled, binding); the four-barrier/four-class algebra (adopted);
`02`'s vacant-allocator, one-act, and no-fallback-rescope rulings (adopted as contract).

---

## 11. WHAT ESCALATES TO JORDAN

Applying §0's five tests (superseded → irrelevant → answered-by-doc → precedent → architecture) to
every candidate this lane surfaced:

- **Closed without escalation:** the loop-count question (answered by architecture + code, §1); O-2
  (answered by doc + code, §2); the class-vs-phase question (answered by running-code precedent,
  §3); the D-2 act economy (answered by ARCH §7's own resolution — with one *verification* work
  item: ARCH §7 admits it never read `proposals/2026-08-30-fixes/02_the_act_economy.md`; a session
  must diff the two and only escalate if they disagree); `wear` values and
  `season_factor`'s distribution (measurable — instrument work for `balance_oracle`-class tooling,
  not a ruling); the accounting reorder (engineering call with a mandated control, §6 step 8).
- **ESCALATE 1 — the commander ambiguity in ED-IN-0201.** "(a) no commander → no conquest
  declarable, vs (b) declarable but the unled army fights at a penalty." Survives all five tests:
  the ruling itself flags it open, no doc or precedent settles it, and the two readings are
  materially different games (a gate game vs a leverage game). Blocks nothing before §6 step 3
  reaches conquest; must be answered before it does.
- **ESCALATE 2 (as a loud PR callout, not a queue row) — ratifying the reconciled `engine_clock`
  canon.** The §2 doc refines ratified canon (`propagation_spec_v1.md` §O.1). Under ED-1094
  merge-ratification suffices, but §2's own rule requires the refinement called out prominently in
  the PR body as held back for explicit sign-off, because it touches ratified text.

Nothing else in this lane needs Jordan.

---

## 12. CONFIDENCE per ruling

| ruling | confidence |
|---|---|
| §1 refinement-not-replacement; three-phase tick stays the mechanism owner | **High** — grounded in code read in full, its pinned tests, and §0.05 |
| §1 retirement of the P0–P7 season | **High** — its successor's corrections are verified against its own text |
| §2 O-2 upheld-with-correction (fine-grain canon; §O.1 stays the coarse spine) | **High** |
| §3 adoption of six steps / 4 barriers / 4 classes + write matrix | **High on the algebra; Medium on MATTER's exact content** (wear/yield constants unmeasured by the design's own admission) |
| §4 parallelism licence sound as argument, unenforced; fixed-point obligation | **High** — the IEEE non-associativity point is mathematics, and the repo's own §0.1 pt 2 incident is the precedent |
| §5 substream scheme adoption | **High** — it generalises the code's best existing seam and fixes its measured worst defect |
| §6 execution-path ordering | **Medium-High** — step contents verified feasible against the tree; sizes are estimates; step 8's reorder is the riskiest and is priced |
| §7 test specifications | **High** — each has a named falsifier and a vacuity guard |
| §8 loader order, guard closure, and the two-arm control | **High** — guard blindness verified in code myself; control follows §0.1 pt 4 and ED-IN-0201's own MOVES note |
| §9 enforcement classifications | **Medium** — classes for unbuilt steps are predictions about buildable shape |
| §11 single genuine escalation (commander ambiguity) | **High** |

*[unclear] markers carried:* whether ARCH §7's D-2 resolution agrees with
`proposals/2026-08-30-fixes/02_the_act_economy.md` (unread by the design and by this lane — assigned
as verification, §11); `season_factor(territory)`'s distribution (open in the design itself,
`02:1177-1178`).
