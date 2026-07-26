# Mass battle — Fable-5 max-effort READ-ONLY audit (ED-MB-0045)

**Date:** 2026-07-26 · **Lane:** MB · **Base:** `f4ab261` · **Posture:** read-only — no engine file,
config, golden, flag, doc or contract was modified by this audit.

**Method.** Six independent Fable-5 auditors, one per requested dimension, each given read-only tools
(no Write/Edit) so independence is *structural* per CLAUDE.md §10, and each briefed to separate
MEASURED from INFERRED and to name a falsifier per finding. Dimensions: code shape & compliance ·
fidelity to historical precedent / military theory · primitive emergence · I/O beginning with cells ·
damage & health · pathing.

**Verification.** Agents are not trusted by default. Every finding promoted to §1–§2 below was
**re-derived by the orchestrator** against the working tree — re-running the harness, re-reading the
cited lines, or executing the agent's own falsifier. Claims that failed verification are recorded in
§5, including one of my own.

---

## §1 — Severity 1: silent result corruption

### S1.1 — The engine's own law-validation instrument is RED, and nothing runs it

**VERIFIED (re-run by orchestrator, both paths):**
```
$ PYTHONPATH=. python3 -m mass_battle.lanchester_signature      # PER_CELL=0
$ PER_CELL=1 PYTHONPATH=. python3 -m mass_battle.lanchester_signature
  [FAIL] LAW EXPONENTS (linear/square) melee p=2.50 (≤1.4 linear) volley p=0.50 (≥1.6 square)
  exit=1
```
`core/attrition.py:12-43` states the mechanism claim: frontage-capping means "numerical superiority is
a LINEAR edge (via overlap/envelopment), **never square**." Measured, melee fits at **p=2.50 — the
ceiling of the scan grid** (`FIT_P_HI=2.51`, `lanchester_signature.py:116`), so the true exponent is
≥2.5: *worse than the square law the code says it prevents.* Volley fits p=0.50 against a ≥1.6 bar.

**Nothing executes this harness.** Grep over `.github/workflows/`, `tests/valoria/`, `engine/tests/`
returns only a comment in `test_morale_write_sweep.py:119-127` explaining why the file is out of scope
for a *different* check. It exits non-zero and has for at least a week.

Two of its three PASSing checks are also degenerate: `SQUARE (volley 2:1)` passes on
`cas_exchange = inf` — the 2:1 side took literally zero casualties — and `LINEAR (melee 2:1)` requires
≥65% and measures **100%**, while `dg6_friction_resolution.md` §4 adopts ~70% as the historical 2:1
target. **The repo holds two incompatible validation targets for the same quantity**; one must be
repudiated.

*Falsifier:* the harness passing `LAW EXPONENTS`. It does not.

### S1.2 — A 1-ulp float error still zeroes an exchange: the fix patched the producer, not the consumer

**VERIFIED (reproduced by orchestrator):**
```
net = 3.0                  → degree=Success  → dmg 4 → after dr=1 → 3
net = 3 + σ(-1e-16)        → degree=Partial  → dmg 1 → after dr=1 → 0
       = 2.9999999999999996
```
`compute_degree` (`resolution.py:64-68`) compares a **float** net against hard integer thresholds with
**no epsilon guard** — while the pool floor twelve lines away in the same pipeline did get one
(`orchestration.py:865`, added after this exact defect ate a die at 2.999…96).

This is the CLAUDE.md §0.1 #2 case in the doctrine's own words. The historical fix patched **one
producer** (`units.py:621-631`, the uniform cell-mean fast path). Every other producer of a
tiny-negative σ re-triggers the class: sibling pull (`core/state.py:86-88`), fatigue float division
(`percell.py:268`), morale ratio (`resolution.py:78`).

*Falsifier:* show every live path delivers exact integers to `compute_degree`, or add the guard.
Neither exists.

### S1.3 — Engagements past the 5th depth group are silently dropped

**VERIFIED:** `orchestration.py:1431` — `if sub_idx >= MAX_SUB_PHASES: break`. A bare `break`: no log,
no counter, no warning. Those pairs produce **zero damage that tick**. `MAX_SUB_PHASES = 5` is
self-tagged `CALIBRATED-DEBT … magnitude fitted to engine behaviour, no external source`
(`config.py:136`) — its former `canonical:` tag was a bare-integer self-whitelist deleted in
ED-MB-0041. Deep formations lose engagements invisibly.

### S1.4 — `check_drift` re-keys ONE of ten per-cell maps

**VERIFIED (executed the agent's falsifier):**
```
cell_troops        re-keyed
cell_morale        *** NOT TOUCHED ***      cell_start_troops  *** NOT TOUCHED ***
cell_breakpoint    *** NOT TOUCHED ***      _cell_target       *** NOT TOUCHED ***
halted_cells       *** NOT TOUCHED ***      merged_cells       *** NOT TOUCHED ***
cell_facing_vec    *** NOT TOUCHED ***      cell_last_speed    *** NOT TOUCHED ***
_speed_accum       *** NOT TOUCHED ***
```
Drift is reachable in ordinary play (`discipline_check_phase → check_drift`, `core/state.py:237`; any
non-Line shape below `MIN_DISCIPLINE`). After it, `cell_morale` is keyed to a **dead shape** while
`cell_troops` is keyed to the live one.

INFERRED consequences under seeded cell morale: `eff_morale` weights one by the other → aggregation
collapses to the key *intersection*; if empty, it falls through to the stale scalar the cell path
never writes → **morale immortality**. `check_cell_breaks` reads old ids against new troops → `lost =
1.0` → phantom breaks that `propagate_cell_breaks` then spreads onto live cells.

Latent only because `PC_CELL_MORALE` is off. **It is a re-flip blocker that the handoff does not
currently list.**

### S1.5 — The shipped default configuration has no automated regression oracle

**VERIFIED:** `FIELD_MOVEMENT` defaults to `"1"` (`hierarchy/units.py:32`). The CI byte-exact test
pins it to `'0'` (`test_mass_battle_byte_exact.py:74`) and states in its own docstring: the
`FIELD_MOVEMENT=1` goldens *"are NOT checked here … Run them manually instead."* CI runs
`pytest tests/valoria` and `pytest engine/tests`; neither reaches `bat.py --check` in field mode.

The mode the engine ships, visualises (`workbench/server.py`) and gauges is protected only by someone
remembering to run it.

---

## §2 — Severity 2: the verification apparatus reports green without looking

A theme, not a list — five independent instances.

| # | Instrument | Defect | Status |
|---|---|---|---|
| S2.1 | `test_octagon_damage.py:93-102` | `if rear > 0: assert …` with **no** `assert checked >= N`. Passes vacuously if no seed produces rear damage. Its two immediate siblings do it correctly (`:85`, `:122`) — the omission is conspicuous. | **VERIFIED** |
| S2.2 | `test_morale_write_sweep.py:36-40` | Claims `build_unit` gives the subunit its **own** morale. Measured: `subunit.morale = None` → both fixture params exercise the *inheriting* branch. The own-morale path — where `between_turn_recovery` calls `set_morale(eff_morale)` and **flattens every cell to the mean** each turn boundary (`orchestration.py:2098-2103`) — has **zero coverage**, and `build_army` puts every gauge body on it. | **VERIFIED** (`subunit.morale = None`) |
| S2.3 | `test_octagon_damage.py:15-16` | Docstring claims the legacy `PC_OCTAGON_DMG=0` path is "asserted byte-unchanged by the existing bat.py digest + persubunit stress suite". The CI digest **pins `PC_OCTAGON_DMG='1'`**; `test_persubunit_stress.py` lives under `tests/sim/` and is not collected by CI. Nothing exercises the legacy path. | MEASURED by agent |
| S2.4 | `provenance.py` | Zero importers repo-wide; every `loc` field stale (`DAMAGE_BY_DEGREE` claimed `config.py:72`, actual `:290`; `K_LINEAR` `:125` vs `:382`). Two inline citations cite the stale locs *as canon* (`orchestration.py:1153,1166`). | MEASURED by agent |
| S2.5 | Flag coverage | 42+ boolean toggles; CI exercises the diagonal only (one flag flipped against default). No pairwise coverage. Permanently-dark paths with zero enablers anywhere: `_find_contacts_field` (~35 lines), `reform_check` (**a canon-required mechanic**, mass_battle_v30 §A.5/PP-241, `REFORM_CHECK_ENABLED` never set), the whole `PC_FACING_MODEL` family, and `COMMAND_SIGMA_ENABLED` (dead behind `POOL_QUALITY_MODEL`). | MEASURED by agent |

---

## §3 — Severity 2: nothing has one owner (CLAUDE.md §8 core invariant)

| Duplicated rule | Sites | Guard? |
|---|---|---|
| Combat-pool formula (3-branch model) | `core/exchange.py:63-134` + `hierarchy/units.py:2339-2370`; docstring says *"Mirrors Unit.base_combat_pool EXACTLY"* | **None.** Already diverged: subunit owner applies yield malus + friction CEV, unit owner applies neither but adds overextend. **VERIFIED:** `(5.0-disc)*0.5` open-coded at `exchange.py:87` and `units.py:2337`; no test asserts the mirror. |
| Per-cell facing/arc | `_per_cell_angle_mod` (`orchestration.py:872-1004`) + `_octagon_cell_mods` (`:1029-`, documented "THE single owner") | Both run every engagement; pin-perception gated differently (`:933` vs `:1076-1078`) |
| Movement | `advance_cells` (grid) + `_node_advance` (field) | Ratified oracle freeze — cost, not defect. Drift already materialised once (`units.py:2386-2395`) |
| Stamina | **Three** stores: `_ColBlock.stamina`, `Subunit.stamina`, `Unit.stamina`, two independent drain laws both live | None |
| Morale verbs | Three dialects (cell / subunit / unit) | Sweep guard exists (good) but scans only 6 files |
| Per-cell state | **Ten** parallel maps, no key-set invariant anywhere | Only a single *sum* check (`validators.py:350`) |
| Damage law | Band model (`DAMAGE_BY_DEGREE`) + linear PP-233 form in `pursuit_damage` (`orchestration.py:2326`) | Two laws coexist |

**On the cell representation (Jordan's question, "cell probably needs to be a class").** The semantic
answer is yes — but *class* may be the wrong shape. A per-cell **object** is array-of-structs: slower
in a Monte-Carlo oracle, and further from the `PackedFloat32Array` layout the Godot port wants. What
is missing is an **owner and an invariant** — one `CellTable` that owns all ten maps, is the sole
writer, and enforces "all maps share a key set, troops conserve". That makes S1.4 a single re-key
instead of ten independent ones, nine of which were forgotten, and makes phases 3–4 add a column
rather than repeat a ritual. *Falsifier for the perf objection: benchmark objects vs maps; if the
delta is noise, a plain class is simpler and my objection is worthless.*

---

## §4 — Historical fidelity and emergence

### 4.1 — Named sources: what verifies, what does not

- **`triplex acies` is misapplied, and the misapplication is load-bearing.** `gauge_mb.py:167-188`
  builds the envelopment defender as `n_cmd=3` commands **side-by-side** citing "Polybius VI /
  *triplex acies*". *Triplex acies* is a **depth** arrangement (hastati/principes/triarii in three
  successive lines), not a lateral tripartition. Left/centre/right is real ancient practice but a
  *different, uncited* precedent. This matters because `n_cmd` is the only free parameter that lands
  H3 in band: **0% @1 → ~53-71% @3 → ~95% @6 → 100% @9**, and it was chosen **after** measuring that
  sweep. A citation is laundering a fitted parameter as independently grounded.
- **du Picq:** mechanism attributions largely faithful (`_charge_shock_sigma` is genuinely du
  Picq-shaped); the 15–30% break band is **not his** — it is "Jordan historical research 2026-07-23"
  re-attributed to du Picq in `core/state.py:35,118`. *Battle Studies* is qualitative and gives no
  casualty-percentage break band.
- **du Picq, inverted:** envelopment's dominant modelled effect is a **damage-received multiplier**
  (1.0/1.5/2.0 stacking to ~3.0×), with morale collapse downstream of casualties. du Picq's actual
  claim — quoted in the repo at `validators.py:168-169` — is that flank/rear attacks kill *because the
  defender breaks*. The engine has men fighting identically while dying 3× faster.
- **Sabin is cited on both sides of a contradiction:** grounded as relief/fatigue management, yet
  `SUPPORT_WEIGHTS`' 0.3 floor with no rank cutoff also makes depth **additive killing power** — the
  reading Sabin argues against. Depth relieves *and* kills; "too deep to fight" (the Cannae Roman
  column) is unrepresentable.
- **Fabricated/unfindable citations:** `geometry.py:183` cites `mass_battle_v30.md §A.3b — 45deg
  octagon`; v30 contains **zero** occurrences of "octagon" (the engine's own comments at
  `orchestration.py:936,1075` admit this — the fabricated citation survives in `geometry.py`).
  `DAMAGE_BY_DEGREE` cites `mass_combat.md §A.4` — **no such section**; the nearest canon (PP-233)
  specifies a *different, linear* law. `K_LINEAR` wears a `canonical:` tag pointing at a doc that says
  *"Coefficient values are sim-tuned at implementation — not pre-decided here."* `BATTLEFIELD_SIZE`'s
  citation is **circular** — v30:121 says "treat config.py as leading canon".
- **Verified-good:** `VOLLEY_TN=6`, `BLOCK_SIZE=100`, `PER_DIE_NET_EV=0.4`, `PC_CHARGE_SIGMA=0.55`,
  `CELL_FLOOR/CAP`, and `PC_FRICTION_SIGMA`'s Dupuy calibration table all resolve to real sources.
  Pattern: dice-math and scale conventions verify; **combat magnitudes are fitted or invented**.

### 4.2 — Casualty realism: totals near-band, causal shape inverted

With `PC_STOCHASTIC_ROUT=1` the gauge reads loser 29–41% / winner 3.3–17%. But **`pursuit_damage` is
never called in the measured mode** — only inside `run_multi_unit_battle`, which the gauge, `bat.py`
and `lanchester_signature` never invoke. So the engine generates the *entire* loser total during
formed melee, pre-break. Historically the winner/loser asymmetry is generated almost entirely in
flight/pursuit. **The engine kills the loser and then breaks him; history breaks the loser and then
kills him.** The 15–30% band is also doing double duty as both break-onset and total-loss band —
coherent only because pursuit is absent.

### 4.3 — DG-6 / CEV verdict

**Mathematics right, historical label wrong, magnitude doing illegitimate work.** The O(1/√N)
diagnosis is correct and the once-per-battle correlated shock is the textbook fix. But Dupuy's CEV is
a **post-hoc fitted residual, persistent per force** (German ~1.2–1.3 across engagements) — not an
i.i.d. per-battle draw. At σ=1.1 per side, 1-SD of the effectiveness *ratio* spans ≈0.21×–4.8×; no
Dupuy-measured CEV approaches that. And σ=1.1 was calibrated so a **single scalar** reproduces the
whole DLEDB curve — a variance *prosthesis* absorbing every mechanism the engine lacks (§4.5). As
those land, σ will double-count.

**Recommendation:** keep the mixture structure, **rename it** (Clausewitz/Beyerchen friction, not
"Dupuy CEV"), expect σ to shrink. Shipping it OFF pending the envelopment gate is the right call.

This **strengthens** the ED-MB-0043 plan's recommendation to measure cell-lattice correlation first:
correlation generated by a mechanism does not need a prosthesis, and does not double-count later.

### 4.4 — Emergence verdict: subunit-emergent, not cell-emergent

The flagship "emergent" behaviours are **builder-authored postures**. `build_envelopment` does not
discover the ring — it manufactures its preconditions: wings placed on opposite flanks *specifically*
so the left/right test wheels them in mirror (the comment calls this "the load-bearing invariant of a
double envelopment"), frozen at `stance='hold'`, released by a scripted `tick:4` clock tagged
`CALIBRATED-DEBT`. Decisively, the repo's **own** sweep found H4 (Cannae) passes its band with
envelopment pathing switched **OFF**.

Outcome magnitude ordering (agent-measured individually, ordering INFERRED): per-cell **density**
scalar > **subunit partition count** (0%/53%/95% at n_cmd 1/3/6) > per-battle unit scalar > cell-level
state. The whole cell-morale programme moved win-share by **one row**, and phases 1+2 were
**byte-identical** across all 20 rows.

**Counterfactual:** delete the cell layer, keep subunit position/frontage/troop total — little shipped
behaviour changes. Jordan's directive is implemented as: troops ✓, facing ✓, morale/rout/damage built
but **dark**, discipline/quality/stamina/armour **not per-cell at all**.

Entity special-casing survives: `charge_pen = 3 if troop_type == 'cavalry'`, brace-recoil requiring the
charger *literally be* `'cavalry'` with `mounted_archers` excluded **by name**, speed multipliers keyed
on type-name lists. *Falsifier:* add "cataphracts" to `TROOP_TYPE_STATS` — charge, recoil and wheel
will not follow from its stats; three hardcoded name lists must be edited.

### 4.5 — Mechanisms with no representation at all

Terrain/elevation/weather/ground · pursuit in the measured mode · surrender & prisoners · **the general
as an entity** (no position, no death, no "general falls" panic) · surprise/deception/ambush/fog ·
ammunition depletion & the skirmish phase · reserve commitment as a decision under uncertainty ·
wounded-vs-dead · night/duration lulls.

---

## §5 — Claims that FAILED verification (including one of mine)

**5.1 — MY OWN ERROR.** I hypothesised mid-audit that `ncells` was never assigned, making the
Lanchester density branch dead code. **Wrong** — it is assigned at `hierarchy/units.py:2221`. It is set
*once* at spawn and never updated (not even by `check_drift`), which is a real staleness bug, but not
the dead-code one I guessed. Caught before it reached a finding.

**5.2 — MY OWN ERROR, and it reverses a recommendation I gave.** In the ED-MB-0043 plan I called the
R3 fix "the one item I would ship without a ruling". The pathing audit refutes that, verified:
- Bypassing the `hold` early-return **does nothing on its own** — `STANCE_SPEED_MOD['hold'] = -99`
  (`config.py:262`) independently zeroes `step`, and all goal resolution including `_kite_goal` sits
  inside `if target_centroid and step > 0:`. **It is a two-gate change, not one.**
- `hold` is **load-bearing** elsewhere: `build_envelopment`'s `freeze_wings` is documented as relying
  on hold being "fully sufficient to freeze position, no separate position-pinning mechanism needed";
  `build_refused_flank`'s refused wing; and `STANCE_COMMITMENT` reads `hold` as defensive commitment in
  the exchange. A role-keyed bypass breaks the timed release, the DG-5 ablation instrument, and gives a
  moving body defensive pool treatment.
- `_kite_goal` **does not generalise**: `PC_KITE_STANDOFF = 5` against a max melee reach of 0.3 (pike)
  makes the band `[5, 0.3]` **inverted** — a melee kiter flees inside 5 and closes beyond 5 forever.
- Lower-blast-radius alternative: change the **R3 scenario** (`stance='balanced'` + `kite`) rather than
  the engine's `hold` semantics. *Falsifier:* run R3 that way; casualties should become non-zero.

**5.3 — A standing `needs_jordan` diagnosis names a dead code path. VERIFIED.** ED-MB-0038/0039
attribute the envelopment side-asymmetry to "the enveloper's APEX-forward centre
(`build_envelopment`, `start_row+APEX*advance_dir`) + wing placement vs the flat command line".
`engine.py:414-419` applies `APEX` **only in the `else` branch — when the caller omits the centre's
`starting_position`**. Both harnesses pass it explicitly (`gauge_mb.py:257`, `bat.py:70`). **In H3/H10
and the whole `bat.py` battery the apex offset never executes.** The diagnosis in `HANDOFF_MB.md`
should be corrected before more work is spent on it.

The pathing auditor **could not** find a deterministic `<`-vs-`<=` or rounding bias statically and says
so plainly. Two non-equivariance candidates under `r → 49−r`, neither proven the 54pp driver:
`min()` over a **set** (`orchestration.py:1744`) tie-breaking by value-dependent iteration order, and
banker's rounding at exactly `.5` (consistent with the measured start-row *parity* sensitivity).
*Falsifiers given:* canonicalise to `min(sorted(...))` and re-run the mirror; sweep start rows
preserving the exact mirror midpoint.

**5.4 — ED-MB-0041's "armour causes MORE arrow casualties" is REFUTED as current.** Agent-measured
300-seed volley + 40-seed battle sweep: target casualty fraction **0.115 / 0.061 / 0.035 / 0.015** at
dr 0/1/2/3 — strictly monotone decreasing. The inversion was real and is fixed (`h_per_size` is now
dead code). The claim should be retired rather than left circulating.

**5.5 — Neither of ED-MB-0008's two contradictory DR tables is what the code implements.** The armour
catalogue transcribes PP-188 but is **explicitly unwired** (`equipment/armour.py:16-18`); the live
engine uses a free scalar `Unit.dr` defaulting to **1 everywhere**. `RANGED_DR_DEFAULT=2` is
unreachable and uncited. So ED-MB-0008 is a *documentation* contradiction with no current code
consequence — which changes its priority.

---

## §6 — Disposition

Forward-only per the audit-skill contract. **No action was taken; this is a read-only record.**

| Finding | Disposition |
|---|---|
| S1.1 Lanchester law red + unwired | **ED-MB-0045**, needs_jordan — repudiate one of the two incompatible 2:1 targets, then wire the harness |
| S1.2 degree-boundary ulp | **ED-MB-0045** — guard the *consumer*, not another producer |
| S1.3 `MAX_SUB_PHASES` silent drop | **ED-MB-0045** — at minimum log the truncation |
| S1.4 `check_drift` desync | **ED-MB-0045** — re-flip blocker; add to `HANDOFF_MB.md`'s precondition list |
| S1.5 shipped default unguarded | **ED-MB-0045** — needs a CI budget decision (field battery ~80-110s/mode) |
| S2.1–S2.5 vacuous/absent verification | **ED-MB-0045** |
| §3 single-owner violations | **ED-MB-0045**; the `CellTable` proposal supersedes the plan's phase-3/4 ordering |
| §4.1 misapplied/fabricated citations | **ED-MB-0045**, needs_jordan (`triplex acies` is load-bearing) |
| §4.3 CEV naming + σ double-count | **needs_jordan** — strengthens ED-MB-0043's measure-the-primitive-first recommendation |
| §4.4 emergence verdict | **needs_jordan** — the cell is not yet load-bearing |
| 5.2 R3 fix blast radius | **Corrects ED-MB-0043's plan.** No longer "ship without a ruling" |
| 5.3 APEX dead path | **Correct `HANDOFF_MB.md`** ED-MB-0038/0039 text |
| 5.4 armour inversion | **Retire the claim** from ED-MB-0041 |
| 5.5 DR tables | **Re-prioritise ED-MB-0008** — docs-only, no code consequence |

## §7 — What this audit did not check

- **The orchestrator executed only the Lanchester harness, the degree-boundary reproduction, the
  `check_drift` falsifier and targeted greps.** No gauge run, no byte-exact battery, no probe
  re-execution. Every gauge/probe number quoted is the **repo's own recorded measurement**.
- Five of six auditors ran fully read-only and executed nothing; their INFERRED items are unexecuted
  predictions.
- No external source (Polybius, du Picq, Dupuy, Sabin) was verified against its actual text — no
  source texts exist in-repo. All such claims are **recalled and labelled**, never treated as verified.
- `resolve_engagements` (652 lines) was only spot-checked — it is the prime remaining suspect region
  for the ED-MB-0039 asymmetry if a deterministic bias exists.
- The stale twin `systems/mass_battle/sim/massbattle.py` was not semantically diffed against the live
  engine.
- ~90 `[canonical:]` tags exist; ~18 were opened and checked.
