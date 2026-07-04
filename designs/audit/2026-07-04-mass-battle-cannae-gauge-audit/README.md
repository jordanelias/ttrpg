# Mass-battle Cannae gauge-band failure — root-cause audit and fix plan — 2026-07-04

**Status:** **RATIFIED (ED-MB-0002, 2026-07-04)** — merged via PR #73 (ED-1094 merge-ratifies-by-default:
Jordan's review-and-merge of this PROPOSED doc is the ratification event). Findings (§1) and fix plan
(§2) stand as adjudicated. **DG-3 and DG-4 (§3) are RESOLVED** per Jordan's rulings the same day —
see the addendum at the end of §3 for the exact rulings and their operationalization. DG-1, DG-2, and
DG-5 remain OPEN, per their own stated sequencing (they depend on the DG-3/DG-4 fix landing and the
gauge being re-measured before they can be judged on real data).

**Trigger.** ED-MB-0001 (2026-07-02, the movement/pathing fix plan) landed real `envelop`/`sweep`/
`wheel`/`kite` steering on the live default node path and disclosed-but-did-not-chase one finding:
enabling `PER_CELL`'s previously-inert combat mechanics (fatigue, charge shock, envelopment-sigma)
made the H3-H6 Cannae-pattern historical gauge rows collapse from a passing baseline to 0-13%
losses against a 45-72% expected band, and left `test_envelop_reaches_rear_node` xfailed
(`strict=False`) pending exactly this investigation. `HANDOFF.md`'s "Next action for whoever picks
this up" flagged the underlying question as open: *"numerically-dominant vs. thin-and-yielding
pinning force; a maneuver time-budget separate from the frontal fight's own clock... needs either
Jordan's design call or a dedicated combat-balance pass."* This audit is that pass.

**Method.** A four-lens adversarial read (`clock_coupling`, `historical_fidelity`,
`alternative_mechanism`, `design_options`), Fable-adjudicated across all four, with every contested
fact re-verified directly against the working tree (not taken from any lens's own report) before
adjudication: the C4/C7 gauge compositions and pass status (`tests/sim/gauge_mb.py`), the live-path
encirclement penalty (`tests/sim/mass_battle/orchestration.py:757-758`), the C-ii pool split
(`orchestration.py:504-528`), and the §A.4 casualty-fraction trigger arithmetic
(`tests/sim/mass_battle/core/state.py:27-38`). Full per-lens verdicts and the disagreement
resolutions are Part 3/5 of the source synthesis this README compresses; that reasoning is not
reproduced verbatim here, only its conclusions and the confidence each one carries.

---

## 1. Findings — ranked root-cause account

Confidence labels are carried through from the adjudication unchanged; nothing below has been
softened relative to what the synthesis actually claimed. **RC-1 and RC-2 are established. RC-3 is
indicated but confounded. RC-4 is a real, separate design gap. RC-5 is a flatly undiagnosed
residual.**

**RC-1 (VERY HIGH confidence) — Composition-coupling defects in the aggregation/accounting layer.**
The instant a unit has more than one subunit, three verified mechanisms make it fight worse than
the identical troops fielded as one subunit, independent of what the second subunit does:
- **(a) Multi-front pool asymmetry** (`orchestration.py:504-528`, `POOL_VARIANT="C-ii"`): a
  composed subunit's combat pool is scaled by its troop *fraction of the whole unit*, while a
  single-subunit opponent rolls its **full** pool into every simultaneous engagement pair. The live
  encirclement tax (`orchestration.py:757-758`, `−0.2σ`/pair for a doubly-engaged defender, ~−0.48
  net successes/pair) is real but far too small to close the gap this creates.
- **(b) Shared morale write-routing** (`hierarchy/units.py`, `erode_morale`/`cohesion`, ~L404-431):
  subunits built without their own morale value (`morale=None`) route every write to the parent
  Unit's single morale pool. Two subunits' independent §A.4 casualty-fraction triggers therefore
  erode **one shared pool twice per phase** — a double-count, not doubled damage.
- **(c) Per-subunit casualty denominators under `PER_CELL`** (`core/state.py:27-38`): a subunit's
  50%/25% morale-trigger fractions are computed against that **subunit's own** starting troop
  count, which is smaller than the unit's, so composed subunits trip the triggers materially faster
  than unit-level accounting would.
- Two more, narrower bugs ride alongside these and are fixable independent of any design call (see
  §2 steps 1-2): a fixture-only "ghost cell" construction bug (`tests/sim/mass_battle/
  validators.py:205` assigns `starting_position` **after** `Subunit.__post_init__` has already
  initialized node state from the old value — the detachment never actually starts where the
  fixture claims it does), and a float-epsilon `math.floor()` on the pool computation
  (`orchestration.py:527-528`) that can silently drop a whole combat-pool die when the raw pool
  value sits a hair under an integer boundary.
- **Honestly held gap:** (a), (b), and (c) were never individually ablated. Their *joint*
  sufficiency to produce the fixture's failure is proven (see RC-2's ablation). Their *relative
  weights* are not measured.

**RC-2 (HIGH confidence) — The recovery target is fictitious: the old `PER_CELL=0` green baseline
was an artifact, not a working model.** Under `PER_CELL=0`, `cell_troops` only decrements under
`PER_CELL`, so multi-subunit cohesion was frozen at 1.0 and the §A.4 triggers structurally could
never fire — the pre-flip H3-H6 pass validated an **invincibility bug**, not the envelopment
tactic. This is corroborated three independent ways (control-blindness of the old single-subunit
control; the frozen-cohesion code read directly; the deterministic det-inert ablation below). **Any
fix judged by "restore the pre-flip numbers" is re-installing the artifact.** `PER_CELL=1` did not
break a correct model; it unmasked RC-1.

**RC-3 (MEDIUM confidence) — RC-1's couplings plausibly extend to gauge scale, but the gauge causal
picture is confounded, not proven.** The strongest evidence in the whole audit is a
fixture-scale ablation, already committed as `test_envelop_reaches_rear_node`'s investigation
(`tests/valoria/test_mass_battle_maneuvers.py`): a pinning-main-body-plus-detachment fixture loses
**byte-identically** whether the detachment envelops, marches straight in, or never moves at all —
which decisively refutes "two racing clocks" *for that fixture* and points at the accounting layer
instead. But this cannot be assumed to transfer to the gauge as-is:
- The fixture's detachment was a construction-bug ghost (the RC-1 bullet above); the gauge's real
  `build_envelopment` wings demonstrably do wheel (tracked tick-by-tick from row 36 to row 14.4,
  wrapping past the defender at col ~20.6 — `tests/coverage_matrix.md`'s 2026-07-02 entries). An
  ablation on a fixture whose "maneuver" never actually happened cannot license a claim about what
  happens when the maneuver genuinely does.
- **C7 falsifies composition-count as a clean discriminator.** C7 (`gauge_mb.py:220`,
  `_envelop_army` — genuinely multi-subunit, cavalry wings) **passes** its 65-100 band. Nine
  single-subunit rows fail. Composition alone does not separate passing from failing rows in either
  direction.
- **C4 vs C7 is the sharpest unexplained datapoint in the audit.** Both are cavalry envelopment
  attacks on a Line defender built from the identical `_envelop_army` composition (`gauge_mb.py:197`
  vs `:220`); C4 (defender stance default, band 75-95) **fails**, C7 (defender `stance='hold',
  discipline=8`, band 65-100) **passes**. Whatever separates them — defender stance, discipline, or
  the wider C7 band itself — has not been traced.
- A three-way confound sits underneath all of it: LC-8's composition rework, the ED-1091 recoil
  physics ruling, and the `PER_CELL` default flip all landed inside the same PR window, and the
  joint configuration was never independently validated before this audit.
- **Genuinely open, and cheap to close** (see §2 steps 3-5): whether a real maneuver-time race
  exists at gauge scale — as opposed to the fixture's inert-ghost artifact — has not been measured.

**RC-4 (design gap, not a defect) — Historically correct pinning behavior is inexpressible in the
current engine.** There is no state between "standing and eroding" and "routed." Hannibal's center
did not out-endure the Romans at Cannae; it traded ground in ordered withdrawal. The engine's
fatigue model actively makes a thin formation its *worst*-performing configuration, inverting the
thin center's historical function. This is real, but it is a target-state question, not a cause of
the current gauge failure — authoring it before RC-1 is fixed would tune new canon to compensate
for bugs, which is exactly the band-fitting this repo's discipline forbids.

**RC-5 (LOW-MEDIUM confidence, undiagnosed) — A broad single-subunit failure this audit did not
explain.** Only 4/20 gauge rows currently pass (H1, C2, C6, C7). Nine of the sixteen failing rows —
**H2, H7, H8, H9, R1, R3, C1, C3, C5** — are single-subunit matchups where none of RC-1's
composition couplings apply. RC-1/RC-3 explain at most the H3-H6/H10-H11/C4 composed-army subset.
Something about `PER_CELL` pacing or lethality in plain, uncomposed fights is also off-band, and
**this audit did not diagnose it.** Treat as a separate, still-unopened lane item — do not fold it
into the composition-coupling fix and do not assume closing RC-1 will move these nine rows at all.

**Demoted, not merely deprioritized:** "two racing clocks" as a *general* (gauge-scale) account —
refuted by C7 and the fixture/gauge disanalogy above, though it survives narrowly at fixture scope;
slow-detour/time-of-impact throttling as a root cause — the geometry claim is contradicted by the
`frontage + 2` clearance code and `best_t` was never instrumented; sigma-stack culprits
(`PC_ENVELOP_SIGMA=0.0`, provably inert) — ruled out by direct read; missing-yield-mechanic as the
*cause* of the current gauge failure (it remains real as a *target-state* gap, RC-4).

---

## 2. Fix plan — dependency-ordered, gate-free work only

**Read this before the steps:** every item below is a bug fix or a measurement. **None of them
fix RC-1's three couplings, resolve RC-3's open question, or touch RC-4/RC-5.** The actual
accounting-semantics fix is blocked on Jordan's ruling on DG-3 (and DG-4 for morale scoping) in
§3 — building it without that ruling means guessing at a design decision, which this plan will not
do. **If the only thing you take from this document is one sentence, it is this: the fix plan
below produces evidence, not the fix.** Do not skip ahead and implement a DG-3/DG-4 option because
it seems obvious — see §3 for why each option has a real cost the others don't.

1. **Fix the validator fixture's ghost-cell construction bug**
   (`tests/sim/mass_battle/validators.py:205`, `_attacker_envelop`). Reorder so `starting_position`
   is supplied to `_line(...)`/the `Subunit` constructor **before** `__post_init__` initializes node
   state, not assigned after. Independent of every other step; touches only a diagnostic fixture
   that `tests/sim/mass_battle/bat.py` never imports (confirmed: `bat.py` has no `validators`
   import) — **zero byte-exact digest impact.** Do this first because step 3 below reuses this
   fixture and must not inherit a construction-order bug that makes "the detachment never actually
   moved" indistinguishable from "the detachment's movement doesn't matter."

2. **Fix the float-epsilon pool-floor bug**
   (`orchestration.py:527-528`, `a_pool = max(1, math.floor(a_pool_raw))` and its `b_pool` twin).
   Guard the floor against float accumulation error (e.g. `math.floor(a_pool_raw + 1e-9)`) so a
   pool value that should land exactly on an integer doesn't lose a whole die to representation
   error. Independent of step 1. **Unlike every step in the ED-MB-0001 fix plan, this touches
   combat-resolution code shared by BOTH the grid and field/node movement paths** — do not assume
   grid-mode digests are safe by construction this time (see §4). Land this before step 3 so the
   per-coupling ablation isn't itself contaminated by an unrelated off-by-one.

3. **Build a per-coupling ablation harness for RC-1(a)/(b)/(c)**, at fixture scale, reusing this
   codebase's existing toggle idiom (`validators.py`'s `_set_movement_path`,
   `orchestration.PER_CELL`/`FIELD_MOVEMENT` module-level booleans set pre-construction). Add
   independently-settable toggles for: the pool-split formula (§2a — compare `POOL_VARIANT="C-ii"`
   against a full-pool-per-pair alternative), shared-vs-isolated morale write-routing (§2b), and
   unit-level-vs-subunit-level casualty denominators (§2c). Run all 8 on/off combinations against
   the fixed fixture from step 1 and record which couplings are individually sufficient to reproduce
   the failure and which are only jointly sufficient. **This is instrumentation only — the toggles
   must default to today's live behavior and must not change any gauge or CI outcome by existing.**
   Depends on steps 1-2 (a clean fixture, a clean pool floor) so the resulting weights aren't noise
   from either bug.

4. **Run the gauge-scale frozen-wings ablation.** Same technique as the fixture's det-inert
   ablation, applied to `build_envelopment`: freeze the wings' positions in place for the whole
   battle and compare H3/H4/H5/H6 outcomes against the normal wheeling run. If the frozen-wing
   result is statistically indistinguishable from the wheeling result, that is gauge-scale evidence
   for "no genuine maneuver-clock race" (matching the fixture's finding); if frozen wings perform
   measurably worse than wheeling wings, that is gauge-scale evidence *for* a real race that the
   fixture's ghost-detachment ablation could never have detected. Either outcome is informative and
   neither is assumed going in. This is the single measurement DG-5 in §3 is conditioned on —
   record the result explicitly, it decides whether DG-5 is even a live question.

5. **Trace the C4-vs-C7 divergence.** Both rows use the identical `_envelop_army` cavalry
   composition against a Line defender; C4 (default defender stance, 75-95 band) fails, C7
   (`stance='hold', discipline=8`, 65-100 band) passes. Instrument a side-by-side run varying only
   the defender's stance/discipline kwargs and identify which mechanic (brace interaction, the
   hold-stance immobility, discipline-scaled morale resistance, or the band width itself) accounts
   for the split. This feeds DG-1's evidentiary basis directly — do not guess at DG-1 without it.

6. **Do not attempt to diagnose RC-5 in this pass.** The nine single-subunit failing rows (H2, H7,
   H8, H9, R1, R3, C1, C3, C5) are outside every mechanism this audit traced. Flag them as a
   separate, not-yet-opened investigation lane rather than folding a guess about them into this fix
   plan or into any DG-3/DG-4 decision.

**What this plan deliberately does not include:** any change to `POOL_VARIANT`'s formula, to
morale scoping, to the H3-H6/C4 army composition, to a yield/fighting-withdrawal mechanic, or to
wing-timing/maneuver-budget mechanics. Every one of those is gated below. Building any of them now
would be inventing a default Jordan hasn't ratified — exactly what CLAUDE.md's ED-1094 convention
and this repo's anti-fabrication discipline (§7/§8) exist to prevent.

---

## 3. Decision gates

Every item here is a judgment call, not a fact question. Options are presented with real tradeoffs
on both sides — none is a recommendation dressed up as a finding. **Sequencing matters and is not
optional:** DG-3/DG-4 gate the actual RC-1 fix; DG-1 and DG-2 depend on that fix landing and the
gauge being re-measured before they can be judged on real data instead of the current
artifact-contaminated numbers; DG-5 is conditional on §2 step 4's result and may not even be a live
question.

### DG-3 — Multi-front combat-pool accounting semantics (blocks the actual RC-1(a) fix)

The current asymmetry — a composed subunit's pool scaled by troop-fraction-of-whole-unit, a
single-subunit opponent rolling its full pool into every simultaneous pair, tempered only by a
`−0.2σ`/pair encirclement tax — is a verified fact (`orchestration.py:504-528,757-758`). What the
*correct* model should be is not:
- **Option A: Split the defender's pool across pairs symmetrically** (both sides pay the
  simultaneous-engagement cost the same way). Pro: removes the asymmetry at its root, cleanest
  conceptual fix. Con: largest blast radius — moves every gauge row and every mirror matchup that
  ever puts a unit in >1 simultaneous pair, not just the composed-army rows; every one of those
  needs a deliberate, signed digest re-record.
- **Option B: Apply engage-fraction symmetrically** (keep per-pair pool splitting but scale the
  *single*-subunit opponent's pool down by its own engage-fraction too, rather than letting it roll
  full pool into both pairs). Pro: narrower, more surgical change than Option A; targets exactly the
  asymmetry RC-1(a) identifies. Con: still an engine-semantics change with gauge-wide reach; the
  "right" engage-fraction formula for a non-composed unit fighting on two fronts is itself a modeling
  choice, not obviously derivable from what exists today.
- **Option C: Substantially raise the encirclement tax** instead of touching the pool-split formula
  at all. Pro: smallest code change, reuses an existing mechanic (`ENCIRCLEMENT_PENALTY`) rather than
  introducing a new one. Con: a magnitude bump risks being exactly the band-fitting this repo
  forbids unless the new value is independently derived (not just "whatever number passes the
  gauge"); may not be structurally sufficient even at a large value, since the pool-split
  asymmetry is multiplicative and the tax is additive per pair.
- **Option D: Do nothing to the pool formula; treat RC-1(a) as intended asymmetry.** Pro: zero
  engine risk. Con: leaves the strongest confirmed defect in the whole audit unaddressed, and every
  composed-army gauge row stays contaminated by it, making DG-1 (composition) impossible to judge
  cleanly.

### DG-4 — Morale scoping for composed armies (blocks the RC-1(b) fix)

Should preset-built subunits get **per-subunit morale pools** (localized breaks — a broken center
with wings still fighting on, enabling §A.12 cascade pressure between them), or is the **shared
unit-level pool the intended §A.4 semantics**, with only the double-trigger aggregation bug fixed
(each phase, the shared pool should erode from the unit's *aggregate* casualty picture once, not
from each subunit's independent trigger)?
- **Option A: Per-subunit morale pools.** Pro: the only way "center breaks, wings fight on" (a
  design_options-proposed army-termination-aggregation extension) becomes expressible at all; more
  historically expressive. Con: new state, new §A.12 cascade-interaction surface to design and test;
  larger scope than a bug fix.
- **Option B: Keep the shared pool; fix only the double-count.** Pro: minimal, surgical, matches
  "the double-count looks like a defect" reading directly. Con: a composed army's morale still
  behaves as one indivisible body — Cannae's actual center-vs-wing distinction stays unexpressed,
  meaning RC-4's target state remains uncapturable even after this fix.
- Note the double-counting is *plausibly* a bug under either option — but which option you pick
  changes what "fixed" even means here (stop double-eroding one shared value, vs. give each subunit
  its own value to erode once). Don't fix code before this is answered.

### DG-1 — What should the H3-H6/C4 pinning composition encode? (needs DG-3/DG-4 + step 5's C4/C7 trace first)

The current symmetric-thirds `_envelop_army` composition was never historically ratified — it
passed only under the RC-2 invincibility artifact, so "restore it" is not a valid target.
- **Option A: Majority pin** (historical order of battle — roughly 2/3+ of the force pins, a
  minority envelops with cavalry/Fast wings). Pro: grounded in the cited evidentiary primitives
  (Polybius/Livy); precedent exists for exactly this kind of gauge-composition fix (C2/C5/C6);
  leaves the engine untouched. Con: changes what H3-H6 actually *test*; requires amending the
  grounding doc's band basis, not just the fixture; **C4 already fails its band with cavalry wings
  present**, so a majority-pin composition alone is not guaranteed to close the gap — this option
  risks looking like progress on paper while RC-1's mechanism is still live underneath if applied
  before DG-3/DG-4 land.
- **Option B: Thin-and-yielding center** (Cannae's actual designed-weak center). Pro: highest
  fidelity to the historical tactic this gauge exists to validate. Con: **currently inexpressible**
  without RC-4's fighting-withdrawal mechanic (DG-2) landing first; under the present fatigue model,
  thinness is actively punished, so this option cannot be evaluated honestly until DG-2 is resolved
  and built.
- **Option C: Keep the status-quo symmetric-thirds composition; fix only the engine.** Pro:
  cleanest attribution — any gauge movement is provably the engine fix, not a composition change
  riding along with it. Con: perpetuates a composition nobody actually chose; if RC-5's undiagnosed
  single-subunit pacing issue is real, "the engine" may never cleanly pass this composition even
  once RC-1 is fixed.

### DG-2 — Author a fighting-withdrawal / yield mechanic? (new design surface; hard-sequenced after RC-1)

This is new canon, not a bug fix — ED-MB lane, its own digest blast radius, Jordan-gated by this
repo's own conventions on authoring new mechanics.
- **Option A: Build it now**, converting net-success differential into displacement via the
  existing recoil/knock-back idiom (no new constant required). Pro: only known carrier for the
  historically correct Cannae-center behavior; reuses an existing mechanism class rather than
  inventing one. Con: **sequencing it before RC-1's accounting fix is a hard mistake, not a style
  preference** — it would tune new canon to compensate for bugs still present in the pool/morale
  layer, the exact band-fitting failure this repo's discipline forbids. Also needs a gating design
  (against pseudo-kiting abuse) and interacts with the existing path-budget ruling (ED-MB-0001 §6).
- **Option B: Defer entirely until after RC-1 lands and the gauge is re-measured.** Pro: avoids
  building on an unstable floor; lets the re-measured gauge tell you whether a yield mechanic is
  even still needed to close H3-H6, or whether the accounting fix alone gets there. Con: leaves
  RC-4's design gap open for at least one more full pass; if the accounting fix alone is
  insufficient, this defers real progress on Cannae fidelity by a full cycle.

### DG-5 — Wing-timing mechanism (explicitly conditional; may not be a live question at all)

**Do not open this gate before §2 step 4 has run.** If the frozen-wings gauge ablation shows no
meaningful difference from wheeling wings (matching the fixture's finding), this gate likely has
nothing to resolve — there is no race to budget. Only if that ablation shows a genuine gap should
the following be weighed:
- **Option A: Kinematic release** (a wing's decision to commit is a function of its own travel
  progress, zero new constants, reuses the already-Jordan-ruled path-budget operands from
  ED-MB-0001 §6). Pro: cheapest, most mechanically consistent with what's already ratified. Con:
  only applicable if the gap is genuinely kinematic, not a pacing/lethality issue (which RC-5 makes
  plausible).
- **Option B: Command-gated timing window** (a second, Command-scaled clock governing when a wing
  "counts" as arrived). Pro: reuses the Command-scaling idiom already proposed elsewhere (ED-MB-0001
  gate 1). Con: risks a second Command-gated timing system competing with ED-MB-0001's still-DEFERRED
  gate 1 (conditional-tactics transition speed) — two Command-gated clocks in the same subsystem
  without a clear division of labor is exactly the kind of shape divergence CLAUDE.md §10 warns
  against.
- **Option C: Do nothing; treat the current single frontal clock as final.** Pro: zero new
  mechanism. Con: if step 4's ablation does show a real race, this option simply reintroduces
  RC-3 as a permanent, unaddressed gap.
- Binding design principle carried through regardless of which option (if any) is chosen: **do not
  decouple the pinning-force clock and the maneuver clock by fiat.** `historical_fidelity`'s
  ratified-worthy point survives the rest of its critique — the coupling between the center's
  endurance and the wings' travel time *is* Cannae's historical content, not an implementation
  accident to engineer away.

### Addendum — DG-3/DG-4 rulings (Jordan, 2026-07-04, recorded verbatim + operationalized)

**DG-3 = Option A (split the defender's pool symmetrically across pairs).** Jordan's directive was to
weigh options "in terms of long-term integrity and fidelity to reality"; Option A was recommended and
adopted on that basis: it extends the pool-split mechanism composed subunits already use to apply
symmetrically to whoever else is fighting on multiple fronts, rather than inventing an underived
engage-fraction formula (Option B) or a band-fit magnitude bump (Option C) — and it is the physically
correct model besides: a force fighting on two fronts genuinely cannot commit full effectiveness to
both, which is the entire mechanism that makes envelopment dangerous in the first place. Its accepted
cost is a full, deliberate digest re-record across every gauge row/mirror matchup with >1 simultaneous
pair — the same kind of one-time cost this repo has paid for Stage A's TOI refactor, LC-8, and the
`PER_CELL` default flip.

**DG-4 = a blend of per-subunit and whole-unit morale** ("Morale is blend of per-subunit as well as
whole unit," Jordan, 2026-07-04) — **operationalized by wiring already-existing, currently-inert
machinery, not by authoring new state:**
- `hierarchy/units.py` already has everything the blend needs: `Subunit.agg_morale()`/`derive_rout()`
  (~L1460-1481) compute a troop-weighted aggregate of subunits' own `eff_morale` for whole-unit rout,
  and `cascade_morale_hit()` (~L1482-1491) already exists for genuine army-wide contagion events
  (general death, flank collapse) that sap every subunit's own morale simultaneously. Both are real,
  already-wired mechanisms — not something this fix needs to design.
- The reason none of it activates for composed armies today: `engine.build_army` (confirmed by direct
  read, `engine.py:243-246`) only forwards a per-subunit `morale` override when the CALLER explicitly
  sets it in that subunit's spec dict. No existing composed-army spec (gauge rows, `build_envelopment`,
  `build_refused_flank`) does this, so every subunit's `morale` stays the dataclass default `None`, and
  `eff_morale`/`erode_morale` (units.py:384-386, 424-431) fall through to the shared parent `Unit.morale`
  for every subunit — this is the exact mechanism behind RC-1(b)'s double-count (two subunits' independent
  §A.4 triggers both writing to the one shared fallback pool).
- **The fix: default each subunit to its own real starting morale value at `build_army`/
  `build_envelopment`/`build_refused_flank` construction time**, closing the double-count by construction
  (each subunit's own trigger now erodes only its own pool) — no new dataclass field, no new cascade
  design. The "whole unit" half of the blend is not deleted; it emerges from the same aggregate/cascade
  machinery already in place, exactly matching this codebase's "no flat bonus, effects emerge" discipline.
  This also directly unblocks RC-4/DG-1's "center breaks, wings fight on" case, since a subunit with its
  own real morale can now independently rout while `derive_rout()`'s troop-weighted aggregate still
  governs whole-army collapse.

Both rulings unblock RC-1's actual fix; they do not resolve DG-1/DG-2/DG-5, which remain open and
gated on the re-measured gauge per their own stated dependencies.

---

## 4. Verification

### Byte-exact invariants

- **§2 step 1 (validator fixture fix): zero digest impact, verify by inspection, not by re-running
  `bat.py`.** `validators.py` is not imported by `bat.py` (confirmed: no `validators` import in
  `tests/sim/mass_battle/bat.py`) — only `tests/valoria/test_mass_battle_maneuvers.py` consumes it.
  Confirm this import boundary hasn't changed before relying on this claim.
- **§2 step 2 (pool-floor epsilon fix) is the one item in this whole plan that can move digests —
  do not treat grid-mode as safe by construction here.** Every prior mass-battle fix plan (including
  all of ED-MB-0001) kept the two grid-mode digests (`unit`, `cell`) byte-exact *by construction*,
  because every change lived inside `_node_advance`/the node movement path, which the grid digests
  never enter. `orchestration.py`'s pool-floor computation (`a_pool`/`b_pool`, ~L527-528) is shared
  by **all four** `bat.py` modes (`unit`, `cell`, `unit_field`, `cell_field`) — run all four after
  this fix, not just the field ones. If any of the four changes, that is expected **only** if the
  specific matchup/seed in that golden fixture happens to sit on an integer-boundary float; verify
  by hand that the delta traces to the epsilon guard and not to an unrelated change, then record a
  deliberate, Jordan-signed re-record exactly as ED-MB-0001's steps 2/4/5/7 did
  (`tests/coverage_matrix.md` entry + updated golden hash in `bat.py`). If a digest changes and you
  cannot trace the delta to the epsilon guard specifically, treat that as a regression, not an
  expected re-baseline, and stop.
- **§2 steps 3-5 (ablation harnesses/instrumentation) must not change any committed digest or gauge
  pass/fail count.** They are read-only measurement code paths; any toggle they add must default to
  today's live behavior. If landing the harness changes so much as one digit of any `bat.py` digest
  or moves any of the 4/20 currently-passing gauge rows, that is a bug in the harness (a toggle
  defaulting the wrong way), not a discovery — fix the harness before reporting a result.
- **Anything from §3 (DG-1 through DG-5), once ruled and built, is explicitly NOT covered by any
  byte-exact invariant.** Those are the deliberate accounting/composition/mechanic changes this
  whole plan exists to gate — a full, signed digest re-record (all 4 `bat.py` modes) and a full
  `gauge_mb.py` re-run are the expected, required outcome of implementing any of them, not a
  regression to be avoided.

### Gauge rows to re-run, and against what

- **Full gauge, both modes, after §2 alone (before any DG lands):** `python tests/sim/gauge_mb.py`
  single and multi. Expected: **no change** to the current baseline (single 2/20, multi 4/20 — H1,
  C2, C6, C7 passing) from steps 1-2 (bug fixes should not move a gauge outcome that isn't already
  sitting on the specific epsilon/construction bug they touch); confirm this explicitly rather than
  assuming it — if the baseline moves at all from steps 1-2 alone, that is worth understanding before
  proceeding to step 3-5's ablations.
- **Fixture-scale (step 1 + step 3):** re-run `test_envelop_reaches_rear_node`'s underlying fixture
  (`v_envelop(path='node')`, `tests/sim/mass_battle/validators.py`) with the repaired
  `_attacker_envelop` and the per-coupling ablation toggles from step 3, all 8 on/off combinations.
  Record which combination(s) reproduce the failure — this is the missing relative-weight data RC-1
  never had.
- **Gauge-scale (step 4):** frozen-wings vs wheeling-wings re-run of **H3 (55-72), H4/Cannae
  (45-62), H5 (48-62), H6 (48-60)** — the four rows the composed pinning-force-plus-envelopment
  tactic actually tests (bands per `references/historical/mass_battle_gauge_grounding.md` §3 /
  `gauge_mb.py:164-169`). A statistically meaningful gap between frozen and wheeling is the
  confirmation criterion for "a genuine gauge-scale race exists" (opens DG-5); no meaningful gap is
  the confirmation criterion for "composition-coupling is gauge-scale-sufficient on its own, no race
  exists" (closes DG-5 without building anything).
- **C4/C7 trace (step 5):** re-run **C4 (75-95, `gauge_mb.py:197`)** and **C7 (65-100,
  `gauge_mb.py:220`)** varying only defender stance/discipline; confirmation criterion is
  identifying the specific mechanic (not just correlating stance with pass/fail) that accounts for
  the ~25-point band difference and the pass/fail split.
- **After any DG-3/DG-4 option is actually built (future work, not this plan):** full `gauge_mb.py`
  re-run, both modes, all 20 rows — not just H3-H6/C4. DG-3's options are explicitly gauge-wide in
  reach (they touch pool math every composed and multi-front matchup uses), so a re-run scoped to
  only the Cannae-pattern rows would miss regressions elsewhere. `tests/valoria` (currently 88
  passed/10 skipped/1 xfailed) must also be re-run in full; expect `test_envelop_reaches_rear_node`
  to either newly pass (evidence the fix worked) or to fail in a way that no longer matches its
  current documented xfail reason (evidence the fix changed the failure mode without closing it —
  update the xfail reason rather than leaving stale reasoning attached to new behavior either way).

### What would constitute confirmation the fix actually worked

- **Confirmation, not just motion:** H3/H4/H5/H6/C4 landing inside their historical bands is
  necessary but not sufficient — also confirm the *mechanism* moved, not just the number. Re-run
  step 3's per-coupling ablation post-fix and verify the specific coupling(s) DG-3/DG-4 targeted no
  longer reproduce the det-inert-style failure signature at fixture scale.
- **Explicitly NOT confirmation:** bands passing because a composition, magnitude, or fixture
  parameter was retuned to fit them (the band-fitting this repo's discipline forbids throughout —
  CLAUDE.md §7, this plan's own §2 closing paragraph). If a change to `_envelop_army`'s troop split,
  a gauge band width, or any `PER_CELL`/pool magnitude is the thing that made a row pass, trace
  whether that change was independently derived (DG-1/DG-3 ratified) or just happened to work —
  only the former counts.
- **RC-5's nine single-subunit rows are explicitly out of scope for "did the fix work."** Do not
  read continued failure on H2/H7/H8/H9/R1/R3/C1/C3/C5 as evidence the RC-1 fix failed — this audit
  never claimed RC-1 explains them, and closing RC-1 was never expected to move them (§1, §2 step 6).
  Continued failure there is expected and should be logged as RC-5's open lane item, not folded back
  into this audit's confirmation criteria.
