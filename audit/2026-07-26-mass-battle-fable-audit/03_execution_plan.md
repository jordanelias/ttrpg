# Mass battle — execution plan v2 (ED-MB-0045)

**Verified against:** `main` @ `4029870` · **Lane:** MB · **Supersedes:** plan v1 (same path, git history)

> **v2 exists because v1 was substantially wrong.** Four Fable-5 critics attacked it; three of its five
> severity-1 findings turned out to be **code-true but incidence-zero**, its headline framing was
> refuted by instrumented measurement, and one of its own guards could not fail. Every one of those
> failures is preserved below as a **named guardrail (§1)**, attached to the task where it would recur.
> The failures are the most instructive content in this document — do not delete them.
>
> **Fresh session: this is self-contained.** Line references verified against `4029870`; re-check
> before editing.

---

## §0 — Orientation

**Where the engine is.** `tests/sim/mass_battle/` — 28 modules, 10,503 LOC — **despite living under
`tests/`**. `systems/mass_battle/sim/` (5 modules) is a stale twin the campaign still calls via
`systems/factions/sim/faction_action.py:349`.

```bash
cd /home/user/ttrpg/tests/sim && PYTHONPATH=. python3 -m mass_battle.<module>
```

**Evidence base:** `01_findings_register.md` (six-dimension Fable-5 audit, ED-MB-0045) ·
`audit/2026-07-26-mass-battle-vector-audit/` (structural, ED-MB-0043) · this plan's git history for
the adversarial review that produced §1.

### What is actually wrong right now — corrected

v1 claimed "battles are being distorted right now" by three mechanisms. **Instrumented measurement
refuted all three.** The wrappers used were proven non-perturbing (grid digests reproduced byte-exact
with them installed):

| v1 claim | Measured |
|---|---|
| Degree-boundary ulp zeroing exchanges | **209,778** `compute_degree` calls · **0** within 1e-9 of a boundary · **0** flips. `_sigma_net_boost` is bimodal: exactly `0.0` or `≥1e-3` |
| Sub-phase truncation dropping engagements | **102,260** cascade calls · max depth-group count **3** vs a bound of **5** · **0** truncations |
| Cell-map desync distorting battles | Drift fires **125×/gauge battery** — but the *morale* consequences are **latent** behind `PC_CELL_MORALE=0` |

**The two things genuinely wrong right now, neither of which v1 listed:**

1. **Both shipped-mode goldens are RED and have been since PR #235/#236 (2026-07-24/25)**, undetected,
   spanning both audits. `unit_field` and `cell_field` both mismatch; pinning `PC_STOCHASTIC_ROUT=0`
   still mismatches, so **≥2 mechanisms** moved them. The audits reasoned about protecting a mode that
   had already drifted.
2. **Casualty realism is 2/20**, with loser-conditioned means spanning **29.1–79.2%** (H6 = 79.2% at a
   100% win rate; H4/Cannae decA = 5.0, below its 45–62 band). v1 quoted a 2026-07-25 scoreboard as if
   current and called totals "near-band". They are not.

**One genuinely-live cell defect nobody claimed:** three un-re-keyed maps are live at
`PC_CELL_MORALE=0` — `cell_facing_vec`, `halted_cells`, `_speed_accum`. After drift, `cell_facing_vec`
lookups on new ids fall through to `(advance_dir, 0)` defaults, **silently resetting the drifted body's
committed facing** ~125× per gauge battery. This — not the morale desync v1 advertised — is the real
current cell-map distortion.

**Standing directives this plan serves:**
> *"the cell needs to be the primitive for morale, discipline, quality, stamina, rout, health, armour,
> facing, damage, troops count"* · *"validate emergent results top-down from historical precedent"* ·
> *"we are still trying to solve mass battle the system, for itself"* · *"make identifying what's
> happening and preventing conflicts etc going forward"*

---

## §1 — GUARDRAILS (each one is a failure this plan already made)

**These are not aphorisms. Each is a specific mistake, with the task it now guards.**

| # | Guardrail | The failure that produced it |
|---|---|---|
| **G1** | **Existence in source is not evidence of rate. Instrument and count before assigning severity.** | v1 put three findings at severity 1 on code-reading alone. Measured incidence: 0, 0, and latent. Neither six auditors nor the orchestrator counted anything. **Guards: every severity label in §3–§4.** |
| **G2** | **A guard must be able to fail. Prove it by mutation before you ship it.** | v1's own A2 guard `compute_degree(ob-1e-16, ob)` **passes on unfixed code** for ob=3 and ob=6 — `3-1e-16 == 3` in float64. A vacuous assertion, in a plan whose theme is vacuous assertions. **Guards: A2, B1b, every new test.** |
| **G3** | **An invariant must be true of healthy state.** | v1's `CellTable.check()` ("keys == ids; Σtroops == troop_count") is false by design: emptiness *is* the `PC_CELL_MORALE` gate, and `troop_count` is a spawn constant. Red on tick 1 of every battle — which makes its own mutation guard unfalsifiable. **Guards: B1b.** |
| **G4** | **Verify the instrument before quoting its number.** | v1 quoted `melee p=2.50` as an engine property. It is a **grid-endpoint artifact of an unidentifiable fit on rout-truncated data** — 40/40 melee trajectories rout because the "no-rout" pin doesn't disable rout, and volley exchanges zero fire. Same class: quoting a red golden as a safety net. **Guards: A1, A6, D1.** |
| **G5** | **Do not generalise from a gated-off feature to its substrate.** | Fork #5's "delete the cell layer and little changes" generalises evidence about the **off-by-default cell-morale programme** to the **entire per-cell substrate** — while `PER_CELL=1` ships, the C-battery exists only under it, and the octagon multiplier reads `cell_facing_vec`. **Guards: fork #5, D2.** |
| **G6** | **Attack the setup, not only the statistics.** | v1's D1 falsifier measured **roll-level** CV, which cell-morale contagion cannot affect by construction — it would have fired vacuously and killed its own hypothesis. CLAUDE.md §0.1 exists because a prior pass "attacked the result's statistics and never its setup". **Guards: D1.** |
| **G7** | **Agreement between instruments that share a blind spot is not triangulation.** | Four instruments "confirmed" `scene_outcome.battle_concluded` as a dangling Key; all four read `module_contracts` without the Key registry. The authoritative graph refuted them. **Guards: E1, any multi-tool finding.** |
| **G8** | **A rejected attack is evidence. Record it.** | A critic argued A1 was over-serialising because "the field goldens already pass at HEAD". They don't. Recording the refutation is what stopped that amendment landing. **Guards: every review.** |
| **G9** | **Architecture rationales need measurement, not intuition.** | v1 rejected a per-cell class because array-of-structs is "slower in a Monte-Carlo oracle" and "further from `PackedFloat32Array`". Benchmarked: **AoS is 15–40% faster** in CPython, and *neither* layout is a packed array. Both reasons false. **Guards: B1.** |
| **G10** | **Do not chain a large ledger job in front of a small measurement.** | v1 bundled ~116 constants of citation work in front of a measurement needing ~6. Bundling is the *documented cause of the last stall*. **Guards: A5.** |
| **G11** | **One golden-moving PR in flight, globally, ever.** | Two concurrent golden-movers make both deltas unattributable — §0.1 #4 by construction. **Guards: A1a, A2, B1a.** |

---

## §2 — HARD RULES

1. **Do not touch §6 forks.** Decisions, not work. If a task needs one, stop and ask.
2. **One task per PR.**
3. **Every fix ships a mutation-verified guard** (G2) — revert it, watch the guard fail, restore. Say so
   in the commit body.
4. **Goldens moved ⇒ publish the delta** — which mechanism, how much. Never silent.
5. **No wake-ups** — `send_later`/`create_trigger` deny-listed (ED-IN-0084).
6. **IDs:** `id_reservations.yaml` `lane_ids.lanes.MB.next_free` (**46**) — take, bump, co-commit.
7. **Close the loop:** `pytest tests/valoria -q` + `tools/valoria_local.py --staged`, update
   `registers/handoffs/HANDOFF_MB.md`.

---

## §3 — TRACK A: repair the instruments · **gates everything**

### A1a — Bisect and re-record the red shipped-mode goldens · **DO FIRST** · G4, G11

Both `unit_field` (`bat.py:322`) and `cell_field` (`bat.py:370`) fail `--check` at HEAD. Last recorded
2026-07-23/24; PRs #235/#236 (impulse momentum; `PC_STOCHASTIC_ROUT` default flip) re-recorded **only
the grid modes**.

- **Do:** bisect the mismatch across those commits; re-record with a **per-mechanism delta published**
  (rule 4). This is a bisection task, not a re-record — v1 sized it wrong.
- **Verify:** `bat.py --check` green in all four modes, twice consecutively. **If two identical local
  runs differ, STOP** — non-determinism halts B1 as well.

### A1b — Wire the field goldens into CI · G4

- **Do:** own CI job (~4 min, not inside the 5-min `tests/valoria` budget) running `bat.py --check` at
  `FIELD_MOVEMENT=1` for both `PER_CELL` modes.
- **⚠ Pin the FULL toggle vector**, mirroring `_PINNED_OFF` (`test_mass_battle_byte_exact.py:63-78`).
  `bat.py`'s mode key reads only `PER_CELL`/`FIELD_MOVEMENT`, so a run missing `PC_NODE_COHESION=0`
  silently checks a node-cohesion battle against the grid golden. Minimal pinning is how ED-1089 went
  wrong.
- **Guard:** the job — but only meaningful **after A1a**. A gate born red is not a gate.

### A2 — Epsilon the degree boundaries · **hygiene, NOT a battle change** · G1, G2

- **Do:** guard **all three** comparisons in `resolution.py:64-68`, not just `Success`. Guarding one
  institutionalises an asymmetric attacker-favouring correction (`net <= 0` lets a mathematically-zero
  boost escape `Failure`). **Epsilon: absolute `1e-9`** — net magnitudes are bounded by pool scale so
  accumulated ulp error is ≤ ~1e-13, while a *designed* σ landing inside 1e-9 is ~1e-9/exchange.
- **Also:** snap `|σ| < 1e-12 → 0` at the `_sigma_net_boost` chokepoint — the semantically-correct
  statement, and it covers all three cited producers at once.
- **Reconcile:** `units.py:621-631` is an existing producer-side fix for this exact class. State which
  regime is authoritative and whether it stays. Two overlapping exactness regimes is how the next
  confound happens.
- **Guard (G2 — v1's was vacuous):**
  ```python
  for ob in (1, 3, 6):
      assert compute_degree(math.nextafter(float(ob), -math.inf), ob) == "Success"
  # plus the real repro verbatim:
  assert compute_degree(3 + _sigma_net_boost(-1e-16, 9), 3) == "Success"
  ```
- **Prediction, stated because G1 demands it:** *this moves no digest in any of the four modes.*
  If one moves, something else is wrong — investigate, do not re-record.

### A3 — Count the sub-phase truncation · **measured incidence zero** · G1

`orchestration.py:1431` — bare `break`, no counter. **Measured: 0 truncations in 102,260 calls; max
group count 3 vs a bound of 5.** Keep the task (a silent drop should never be silent), drop the
severity.

- **Do:** count **truncated pairs and their engaged-troop weight**, not fire-count — truncation drops
  the *deepest-sorted* groups, a systematic bias against deep formations (D6's "too deep to fight").
- **⚠ Report from workloads where cascades occur** (gauge multi-unit, field modes, Cannae/envelopment).
  The pinned grid battery reads 0 and will mislead.
- `trace_event` is a no-op unless tracing is on — the counter must ride the result dict or C4.
- **Do not change `MAX_SUB_PHASES`.** It is `CALIBRATED-DEBT`; changing it moves goldens with no
  measurement.

### A4 — Fix the two vacuous verifications · G2

- **A4a** `test_octagon_damage.py` `test_front_takes_no_arc_penalty` (~93-102): `if rear > 0: assert …`
  with no `assert checked >= N`. Its two siblings (`:85`, `:122`) do it right.
- **A4b** `test_morale_write_sweep.py:36-40` claims `build_unit` gives the subunit its own morale.
  Measured `None` — so both params test the *inheriting* branch and the own-morale path
  (`orchestration.py:2098-2103`, which flattens every cell to the mean each turn boundary) has **zero
  coverage**, while `build_army` puts every gauge body there. If the flatten proves wrong: **file it,
  do not fix in place.**

### A5a — Scalar-write sweep, lanchester only · **gates D1** · G10

`lanchester_signature.py:126`. ~**6** blocking constants (not the ~100 v1 budgeted — that number was
the *other* file).

- **⚠ Carve-out:** the site is `ua.morale = ua.morale_start = NO_ROUT_MORALE`. `set_morale` covers the
  morale half; `morale_start` is **non-cellular** and must stay a bare write — it needs a `_CELL_OWNED`
  whitelist entry or the sweep gate blocks its own fix.
- **Falsifier (G2):** in the trajectory loop, `assert not ua.routed and not ub.routed` every tick, and
  `assert checked >= TRAJ_SEEDS`.

### A5b — Scalar-write sweep, persubunit · **off the critical path** · G10

`test_persubunit_stress.py:191` + ~**116** constants. It fails **loudly** (its own assert catches it),
so it gates the eventual default *flip*, not any measurement. Do not chain it in front of A5a.

### A6a — Repair the Lanchester harness · **before wiring or arbitrating it** · G4

**The harness does not measure what it claims.** Measured: the `NO_ROUT_MORALE=1e9` pin does not
disable rout, because `_stochastic_break` triggers on **casualty fraction**, not morale — 40/40 melee
trajectories rout, the fit window collapses to 30 ticks, and the cv objective is **monotone across the
whole scan grid with no interior minimum**. `p=2.50` is a grid endpoint, not an estimate.
`PC_STOCHASTIC_ROUT` defaulted ON on 2026-07-25 — one day before the audits — and silently broke it.

Volley is worse: 40/40 trajectories, **0.0% casualties on both sides**, `cv=0` at every `p`; the `inf`
exchange ratio is a `0/0` guard, and the big side won **0/100**. Nothing happens at all — the same
ranged-hold standoff as ED-MB-0044.

- **Do:** make the rout pin actually disable rout; make the volley scenario exchange fire.
- **Strike from the record:** "the true exponent is ≥2.5, worse than the square law." Unsupported.

### A6b — Wire it report-only · after A6a. Blocking flip waits on fork #2.

---

## §4 — TRACK B: ownership · G9

### B1a — The cell-state owner · **design re-opened; do not start until §4a below is closed**

**v1's rationale was measurably false (G9).** AoS benchmarks **15–40% faster** than the parallel-dict
SoA layout in CPython (25 cells/subunit, all access patterns), and *neither* layout is a
`PackedFloat32Array` — both are `(r,c)`-tuple-keyed hash maps, so the Godot-distance argument was
decorative. **Decide the design on measured grounds or on the one honest argument** (a thin wrapper is
the lowest float-order-risk introduction path — and that variant *enforces nothing*).

**Three constraints v1 missed:**

1. **"Owns the state" and "behaviour-preserving by construction" cannot both hold.** External writers
   exist in every layer (`percell.py:119`, `orchestration.py:1705` replaces the attribute outright,
   `contact.py:222`, `check_drift`'s wholesale reassignment, `seed_cell_morale`), and duck-typed readers
   assume dict semantics (`getattr(atom,'cell_troops',None) or {}` — a proxy without `__bool__` changes
   that branch). Either expose the live dicts (owning nothing; detection, not prevention) **or** rewrite
   ~50 sites (where the float-order risk lives). **Pick one and say which.**
2. **Float-order preservation requires per-map insertion order**, and the maps do not share one today —
   spawn-order (`cell_troops`, `cell_morale`) vs movement-order (`cell_facing_vec`, `cell_last_speed`,
   `_speed_accum`). A unified `.ids` set cannot represent that. Order-sensitive consumers:
   `sum(cell_troops.values())`, the `eff_morale` loop, `_pair_engaged_troops`' walk (**already the site
   of one digest-moving bug**), `list(cell_facing_vec.values())` averaged. Plus RNG: `cell_breakpoint`
   draws in `cell_start_troops` order — reorder and every later draw shifts.
3. **§4a — the verification net has a hole over the exact bug.** A1's digests run at
   `PC_CELL_MORALE=0`, where the three cell-morale maps are **empty**. They verify float-order for every
   map *except* the three whose desync motivates the task. **A fifth digest mode (`PC_CELL_MORALE=1`,
   freshly recorded) must exist before B1a starts**, or "if digests move, you changed behaviour" is
   vacuous over cell state.

### B1b — The invariant · **v1's version was false by design** · G3

Per-map class, not one rule:
- **value maps** (`cell_troops`, `cell_morale`, `cell_start_troops`, `cell_breakpoint`, `_cell_target`):
  **empty XOR `keys == ids`** — emptiness *is* the flag gate.
- **lazy/set maps** (`halted_cells`, `merged_cells`, `cell_facing_vec`, `cell_last_speed`,
  `_speed_accum`): **`keys ⊆ ids`**.
- **conservation:** `|Σcell_troops − last_conservation_point| ≤ ε` — **never** against `troop_count`,
  which is a spawn constant and false from the first casualty.
- **Guard (G2):** corrupt one map, assert `.check()` fails — only meaningful once `.check()` is true of
  healthy state.

### B1c — Route `check_drift` through the owner · **not "S"**

Drift has **no old→new key bijection** (arbitrary shape → Line, different cell count). Per-map policy is
unmade and at least two are §6-class rulings: `cell_morale` (mean? troop-weighted? *carrying the
low-morale corner is the feature's whole point*) and `cell_breakpoint` (a **drawn** value — redraw and
shift the `_cell_random` stream, or inherit from which dead cell?).

**Immediate, independent of B1a:** the live facing-loss defect (§0) is fixed by re-keying
`cell_facing_vec` alone. A standalone `rekey_cells(new_ids)` covering all per-cell containers is ~30
lines and achieves B1c's correctness goal **without B1a's L-sized risk**. Consider doing that first.

### B2 — The pool formula · **the mirrors have already diverged** · G1

Not a maybe. Three flag-gated divergences: friction CEV + yield malus in `subunit_combat_pool`;
`OVEREXTEND_PENALTY` in `Unit.base_combat_pool`; side-effect asymmetry on `broken`.

So v1's "collapse, **or** add a mirror test" is illusory — a defaults-pinned test **passes while
certifying a false docstring**. **Collapse is the only real option**, and it needs a ruling on whether
the pursuit pool carries CEV/yield (fork-adjacent). File the divergence first.

### B3 — Wire or delete the dead machinery

`provenance.py` (0 importers, all `loc`s stale, yet cited as canon) · `merged_cells` /
`resolve_internal_collisions` (0 call sites) · `_find_contacts_field` · `PC_FACING_MODEL` family ·
`COMMAND_SIGMA_ENABLED`.

**⚠ `reform_check` is NOT "zero enablers anywhere"** — `validators.py` sets and exercises
`REFORM_CHECK_ENABLED` across 7 cases. And it is canon-required (mass_battle_v30 §A.5/PP-241): wiring it
changes battles, deleting it repudiates canon. **Its only permitted disposition is *file for fork
ruling*.**

---

## §5 — TRACK C: observability · G4

**Binding rule for every C PR:** use the existing `start_trace`/`trace_event` seam — gated, **zero RNG
draws**, no float writes to engine state. Merge guard: all four digests byte-identical with tracing off,
mutation-verified by inserting a state-perturbing event and watching a digest move.

- **C1 — per-phase casualty attribution.** Tag every casualty with source and tick. **Load-bearing:** it
  is the only way to measure §0's inverted causal shape (engine kills the loser *then* breaks him;
  history breaks *then* kills), and the only way to check A2/B1c's predicted no-op. Verifier gate:
  **conservation** — Σ attributed == total hp delta, mutation-verified by untagging one path.
  **Sequence: after A2/A3, before B1a** — its conservation check then doubles as a second
  behaviour-preservation instrument during the refactor.
- **C4 — invariant reporting.** Only the hp-vs-Σcells slice starts now; the `CellTable.check()` and
  truncation-counter surfaces **do not exist yet** (B1b, A3).
- **C5 — promote the workbench.** ⚠ **Fix concurrency first:** `server.py` serves trace requests on a
  `ThreadingHTTPServer` while `run_traced_battle` seeds the **process-global** RNG and toggles a
  **module-global** trace buffer — two concurrent requests interleave RNG streams and clear each other's
  trace. Also `from trace import …` shadows stdlib `trace` process-wide.
- C2 (break decision log), C3 (mechanism attribution) — valuable, optional until a question needs them.

---

## §6 — TRACK D: the system itself

### D1 — Over-decisiveness · **the plan's central bet** · G6, G4

**v1's falsifier measured the wrong quantity.** `dg6`'s CV table is **"CV of net"** from `roll_pool(N)` —
**roll-level**. Cell contagion acts at the **battle** level and cannot change a single pool roll's
distribution, so that curve stays O(1/√N) *regardless of the truth*.

- **Estimand:** CV of **battle outcome margin** and **loser casualty fraction** across seeds, vs army
  size N, at fixed matchup. **Arm 0 must first demonstrate the battle-scale quantity also decays
  ~O(1/√N)** — if not, DG-6's framing needs re-deriving before any arm runs.
- **Four arms:** (0) both off — baseline **and positive control**; (1) `PC_CELL_MORALE=1` — hypothesis;
  (2) `PC_FRICTION_CEV=1, σ=1.1` — **known-cure comparator**, defines what "fixed" looks like; (3) both
  — interaction/double-count. Arm 1 is judged by which reference curve it resembles.
- **Arms are independent samples, not paired** — the ON arm consumes extra RNG draws.
- **Pre-registration (the §0.1 #3 artifact):** estimand, arms, N-grid, seed blocks (exploration 0–99 /
  confirmation 100–499), decision rule, falsifier — committed **before** the confirmation block. **No
  constant may change between blocks.**
- **⚠ Gate:** the cell-morale re-measure is invalid while `check_drift` corrupts cell state (S1.4). Fix
  the re-key first — **or** assert a drift counter of **0** across all D1 battles (Line-only matchups
  make this achievable; drift needs a non-Line shape below `MIN_DISCIPLINE`: Line 1 · Column 3 ·
  Arrowhead 4 · GappedLine 5). Either way the assertion is the artifact.
- **Confound checks, each with an artifact:** per-arm config fingerprint diff showing *only* the flag
  under test · write-liveness (`assert checked >= 1` that recovery moved cell values) · termination-cause
  distribution per arm · drift-counter assertion · no tuning between blocks.

### D2 — Cell-primitive phases 3–4 · G5

After the ownership question settles. Phase 3 (stamina/discipline/quality per cell, retiring `col_grid`
— blocked on fork #7) then phase 4 (hp/armour). Unblocks `PC_STOCHASTIC_ROUT`'s fate and
`ROUT_CASCADE_FRAC`, both currently undecidable under the confound.

### D3 — Envelopment regimes

Fork #A/#B stands. **The standing diagnosis chases dead code:** ED-MB-0038/0039 blame the APEX-forward
centre, but `engine.py:414-419` applies `APEX` only when the caller *omits* `starting_position`, and
both harnesses pass it explicitly — **it never executes in H3/H10 or the golden battery.** Two live
candidates, neither proven: `min()` over a **set** (`orchestration.py:1744`, value-dependent iteration
order) and banker's rounding at exactly `.5` (consistent with the measured start-row *parity*
sensitivity). **Do not decide D3 before D1** — option B may share machinery.

### D4 — R3 ranged-vs-ranged · ED-MB-0044

**v1 called this "ship without a ruling". Wrong.** `STANCE_SPEED_MOD['hold'] = -99` independently zeroes
`step`, so removing the early-return does nothing — it is a **two-gate** change. `hold` is load-bearing
for `freeze_wings`, the refused flank, and `STANCE_COMMITMENT`. `_kite_goal`'s band is **inverted** for
melee (`PC_KITE_STANDOFF=5` vs max reach 0.3). **Recommended: change the R3 *scenario*
(`stance='balanced'` + `kite`), not `hold` semantics.** Falsifier: run it that way; casualties should
become non-zero.

### D5 — Casualty realism · **promoted; v1 understated this badly**

**2/20**, loser means **29.1–79.2%**, H4/Cannae decA **5.0** against a 45–62 band. And the causal shape
is inverted: `pursuit_damage` is never called in the measured mode, so the engine generates the entire
loser total during formed melee, pre-break. **Needs C1 to measure.**

### D6 — Historical grounding

`triplex acies` misapplied (a **depth** arrangement cited for a lateral tripartition) and load-bearing —
`n_cmd` is the only free parameter landing H3 in band, chosen *after* measuring the sweep. du Picq's
15–30% band is not his. Envelopment **inverts** du Picq (damage multiplier dominant, morale downstream).
Sabin cited on both sides of a depth contradiction.

---

## §7 — FORKS: do not execute · one reworded

1. **The two engine trees** — declare / adapter / promote.
2. **Two incompatible 2:1 targets** — ≥65% vs ~70%. **Cannot be adjudicated until A6a lands** (G4).
3. **CEV naming and σ** — Dupuy's CEV is a persistent per-force fitted residual, not an i.i.d.
   per-battle draw.
4. **`triplex acies`.**
5. **⚠ REWORDED (G5).** v1 said *"the cell is not yet load-bearing; delete the cell layer and little
   shipped behaviour changes."* **That is refuted for the shipped engine.** `PER_CELL=1` ships; the
   C-battery exists only under it; `_charge_shock_sigma` returns 0 without it; the octagon multiplier —
   which the audit itself calls envelopment's dominant effect — reads `cell_facing_vec`. **The
   defensible claim is: "cell-level *morale/rout state* is not yet load-bearing."** Establishing
   anything stronger needs a real ablation matrix (`PER_CELL=0` vs `1`; per-cell facing frozen to
   subunit-uniform; matched density and granularity; C3 attribution) which does not exist. **Do not put
   the v1 wording in front of Jordan** — it could redirect the architecture against his own directive on
   evidence that cannot distinguish "cells don't matter" from "cell-morale isn't wired yet".
6. **Which damage law is canon.**
7. **Where fatigue lives** — blocks `col_grid` retirement.
8. **The absent mechanisms** — terrain, pursuit in the measured mode, the general as an entity,
   surrender, ammunition, weather. These would change battles more than all of §3–§5 combined, and they
   are design, not repair.

---

## §8 — TRACK E: canon and registries

- **E1 — delete the `scene_outcome.battle_concluded` emit row.** = **ED-MB-0010, open since
  2026-07-13**. It is the *family* name of `scene.battle_concluded`, not a Key (G7 — four instruments
  agreed it was real because all four shared one blind spot). **Not a one-line hour:** it carries
  `needs_jordan: true`, so under ED-1094 it is a **merge-ratification** — co-commit the ledger flip,
  remove the `[OPEN — Jordan]` comment, delete the dead alias in `build_graph.py`, regenerate the
  observability artifacts, and **state in the PR body that merge = the ruling**. Never as silent
  hygiene. (The "regenerate-never-hand-edit" caveat resolves in our favour: **no generator exists.**)
- **E2** ED-MB-0009 — orphaned fragment citing a `stage5_clocks.md` that never existed.
- **E3** ED-MB-0008 → **docs-only**: neither contradictory DR table is what the code implements (the
  armour catalogue is explicitly unwired; the engine uses a free scalar defaulting to 1).
- **E4** 3 of 6 MB docs lack `## Status:`; the head is `WORKING DESIGN` while the integration doc beside
  it is CANONICAL. (A CANONICAL flip is itself ratification — rides ED-1094.)
- **E5** `engine/params/mass_combat.md` describes a 7-phase d10 dice game; the engine runs continuous
  ticks. Header cites a path that never existed.
- **E6** The `mass_battle` contract's `consumes: []` / `state: []` — **deliberately deferred** until B
  settles what state a battle owns. Ship an honest `status`/`gap_notes` now.
- **E7** Typed params — gated on D1 and fork #6 (only ~17 of ~92 MB magnitudes survive scrutiny).
- **E8** Correct the record: retire ED-MB-0041's armour-inversion claim (refuted — 0.115/0.061/0.035/
  0.015 at dr 0/1/2/3, monotone decreasing); correct the APEX text (D3); strike the `p=2.50` claim (A6a).

---

## §9 — ORDER

```
A1a  bisect + re-record red goldens ────────► GATE (G4, G11)
A1b  wire CI with the FULL pin vector
      │
      ├── parallel worktrees, one PR each:
      │     A3 (counter)   A4 (vacuous tests)   A5a (lanchester, ~6 constants)
      │     A6a (repair harness) → A6b (report-only)
      │     E1 (ED-1094 ratification)   E8/E4 (editorial)
      │   MAIN, alone in the single golden-moving slot:  A2
      │
      ▼
C1   casualty attribution ──► doubles as a 2nd behaviour-preservation instrument
      │
      ▼
§4a  record the 5th digest mode (PC_CELL_MORALE=1)  ──► GATE for B1a
B1a → B1b → B1c        [or: standalone rekey_cells first — fixes the live facing loss cheaply]
      │
      ▼
D1   pre-register → Fable referee → arms 0-3 → decide σ
      └── D2 · D3 (after D1) · D5 (needs C1)
```

**Critical path: `A1a → A1b → §4a → B1a → B1c → D1`.**
**First merged PR: A1a** (the goldens are red *now*). **Cheapest independent win: E1.**

---

## §10 — ORCHESTRATION for a max-intensity session

**Global.** Relay, not dialogue — critics dispatched *after* the producer, given the artifact only
(diff / protocol / measurement table), never the producer's reasoning, always read-only. Lanes return a
fixed-format summary (`task · files · guard+mutation-verified Y/N · digests moved Y/N + mechanism +
magnitude · constants dragged in · falsifier outcome · next action`). **Orchestrator — never a lane —
writes `HANDOFF_MB.md` and allocates IDs.** **Sim runs are Bash in ONE environment, never delegated** —
per-agent environment drift is the confound machine. **One golden-moving PR globally (G11).**

| Task | Shape |
|---|---|
| **A1a** | Solo bisect (Opus). Haiku: commit-range diff inventory. **Opus critic** on the published delta: does each mechanism named actually account for its digest? |
| **A1b** | Haiku: exhaustive env-flag inventory → Sonnet: the job → **Opus critic**: pin-matrix completeness + demand the mutation artifact |
| **A2** | Haiku: σ-producer call graph → Sonnet: guard + test → **Opus critic**: prove the epsilon cannot promote the smallest *designed* σ decrement. Verify the no-digest-movement prediction (G1) |
| **A5a** | Sonnet: reroute (preserve the `morale_start` carve-out) → Haiku: constant extraction → Sonnet: classify → **Opus citation critic**: resolve every `[canonical: doc §sec]` against the actual doc. Non-negotiable — three fabricated MB citations already exist |
| **A6a** | Solo Sonnet repair → **Opus critic**: does the repaired harness now produce an *identifiable* fit? (G4) |
| **B1a** | **Producer SOLO — the main Opus session, never split.** Haiku: ten-map read/write inventory (also the critic's coverage oracle) · Sonnet: order-sensitivity scan · **Opus read-only critic** sees diff + inventory only. Splitting the maps across agents guarantees inconsistent seam semantics |
| **C1** | Haiku: casualty-mutation sites → Sonnet: tag through the trace seam → **Opus verifier**: conservation, mutation-verified by untagging one path |
| **D1** | Runs = Bash, one environment. Fits = scripted. **Verdict = Opus applying the pre-registered rule** — pre-registration exists so the verdict is not a judgment call |

**Fable 5 — exactly two nodes.** Over-promotion is the failure mode.
1. **The D1 protocol referee** — the only node with documented evidence of a cheaper tier failing *this
   exact node twice*. Gets the frozen protocol alone, read-only, one question: **are the arms the same
   experiment, and can the estimand observe the effect it claims to test?** This node is what caught
   G6; it is not ceremonial.
2. **B1a divergence root-cause — conditional**, only if digests move and one full Opus attribution pass
   fails. Record the failed Opus artifact as the promotion evidence.

**Do not parallelise:** B1a's write · D1's execution · golden re-records · ID allocation and handoff
writes · small tasks (E1, A3, A4, B1b) · critic multiplication (one independent critic per gated
artifact).

**Stop conditions.** Two identical local runs of `bat.py --check` differ · A2's prediction fails without
explanation · A5 needs a *new canonical magnitude* (fabrication territory) · **any** digest movement
during B1a · a map's semantics prove incompatible with a shared key-set (that is design, not refactor) ·
C1 conservation cannot hold without reordering damage application (instrumenting must never restructure
the instrumented) · D1 Arm 0 fails its control, fingerprints differ beyond the flag, or the drift counter
fires · **any** urge to tune σ or contagion constants to improve an arm's banding · any task that needs a
§7 answer.

---

## §11 — Provenance

Plan v1 and the three adversarial amendment blocks that dismantled it are in this file's git history
(`46a25ca`, `7ef96ea`, `7b20011`). v2 folds every surviving correction into the tasks themselves and
promotes every failure into §1. **If you find v2 wrong, add a guardrail — that is what §1 is for.**
