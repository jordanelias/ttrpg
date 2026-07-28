# Mass battle — comprehensive plan from the 2026-07-26 session

**Verified against:** `main` @ `4029870` · **Lane:** MB · **Owning EDs:** ED-MB-0043, ED-MB-0045
**Executes:** everything this session established about mass battle — repair *and* design.

> **Fresh session: this document is self-contained.** You do not need the conversation that produced
> it. Every task carries the files, the change, the verification command, the guard, and whether it
> changes battle outcomes. Line references were re-verified against `main` @ `4029870`; **re-check
> before editing** — this engine moves fast.

---

## §0 — Orientation

**What ran this session.** Two audits over mass battle, both merged:

| | What | ED |
|---|---|---|
| `audit/2026-07-26-mass-battle-vector-audit/` | Every structural graph the observatory can build, all directions. Found the *instrument* blind — `structure_audit` had been scanning a deleted tree for five days (88 `tools/` modules, **zero** simulation code). Fixed + guarded. | ED-MB-0043 |
| `audit/2026-07-26-mass-battle-fable-audit/01_findings_register.md` | Six independent Fable-5 auditors, read-only, one per dimension: code shape · historical fidelity · emergence · cell I/O · damage/health · pathing. Every promoted finding re-derived by the orchestrator. Three agent claims failed that check. | ED-MB-0045 |

**Where the engine is.** `tests/sim/mass_battle/` — 28 modules, 10,503 LOC — **despite living under
`tests/`**. `systems/mass_battle/sim/` (5 modules) is a stale twin the campaign still calls via
`systems/factions/sim/faction_action.py:349`. Run it:
```bash
cd /home/user/ttrpg/tests/sim && PYTHONPATH=. python3 -m mass_battle.<module>
```

**Three governing facts, all verified.**

1. **Battles are being distorted right now** — by a float-comparison bug, a silent engagement drop,
   and a cell-map desync. Not hypothetical (§2).
2. **The engine cannot explain a battle.** Asked *why did this go this way*, it answers with a win
   flag and casualty totals. Every diagnosis in both audits required building a bespoke probe; there
   are now **23** in `audit/2026-07-22-mass-battle-stress-test/`. That cost is the finding (§4).
3. **The measuring instruments are not watching.** The engine's own Lanchester harness is red and
   unwired; the shipped configuration has no regression oracle; two tests can pass vacuously. This is
   *why* two default flips were made on confounded measurements and retracted (§2).

**Jordan's standing directives, which this plan serves:**
> *"the cell needs to be the primitive for morale, discipline, quality, stamina, rout, health, armour,
> facing, damage, troops count"* · *"validate emergent results top-down from historical precedent"* ·
> *"we are still trying to solve mass battle the system, for itself"* · *"make identifying what's
> happening and preventing conflicts etc going forward"*

**Two tracks, and they interlock.** Repair (§2–§4) is not hygiene — it is the precondition for design
(§5). You cannot measure whether cell correlation fixes over-decisiveness on an instrument that is
red, and you cannot refactor cell state without a golden for the mode that ships.

---

## §1 — HARD RULES

1. **Do not touch §7 (Jordan forks).** Decisions, not work. If a task seems to need one, stop and ask.
2. **One task per PR.** Several move byte-exact goldens; bundling makes the delta unreadable.
3. **Every fix ships a mutation-verified guard** (CLAUDE.md §0.1 #5): revert the fix, watch the guard
   fail, restore. Say you did this in the commit body.
4. **Goldens moved ⇒ publish the delta** — which mechanism, how much. Never a silent re-record.
5. **No wake-ups.** `send_later` / `create_trigger` are deny-listed (ED-IN-0084).
6. **IDs:** read `references/id_reservations.yaml` `lane_ids.lanes.MB.next_free` (**46** now), take it,
   bump, co-commit. Never max+1.
7. **Close the loop:** `pytest tests/valoria -q` + `tools/valoria_local.py --staged`, then update
   `registers/handoffs/HANDOFF_MB.md`.

---

## §2 — TRACK A: make the instrument trustworthy · **GATES EVERYTHING**

### A1 — Wire the shipped configuration's goldens into CI · **DO FIRST**

`hierarchy/units.py:32` → `FIELD_MOVEMENT` defaults `"1"`. `tests/valoria/test_mass_battle_byte_exact.py:74`
pins it to `'0'` and its docstring says the field goldens *"are NOT checked here … Run them manually
instead."* The mode the engine ships, visualises and gauges is protected by someone remembering.

- **Do:** a CI job running `bat.py --check` at `FIELD_MOVEMENT=1` for **both** `PER_CELL` modes
  (`EXPECTED['unit_field']` / `['cell_field']`). ~4 min; must not share the 5-min `tests/valoria` budget.
- **Guard:** the job.
- **Changes battles:** no — it protects them. **B1 has no safety net without this.**

### A2 — Epsilon-guard the degree **consumer** · **CHANGES BATTLES**

```bash
cd tests/sim && PYTHONPATH=. python3 -c "
from mass_battle.resolution import compute_degree, _sigma_net_boost
print(compute_degree(3.0,3), compute_degree(3+_sigma_net_boost(-1e-16,9),3))"   # Success Partial
```
`resolution.py:64-68` compares a **float** net to hard integer thresholds with no epsilon — while the
pool floor in the same pipeline (`orchestration.py:865`) has one. At the universal `dr=1`, `Partial`
gives **0 damage** where `Success` gives 3. Exchanges are being zeroed.

- **Do:** guard the **consumer**, not a fourth producer. Three other tiny-negative-σ producers exist
  (`core/state.py:86-88`, `percell.py:268`, `resolution.py:78`); the consumer closes all at once.
- **Guard:** `compute_degree(ob - 1e-16, ob) == "Success"`.
- **Requires A1 merged** or the field-mode delta is invisible.

### A3 — Make the sub-phase truncation loud

`orchestration.py:1431` → `if sub_idx >= MAX_SUB_PHASES: break`. Bare `break`, no log, no counter —
those pairs deal **zero damage that tick**. `MAX_SUB_PHASES = 5` is self-tagged `CALIBRATED-DEBT`
(`config.py:136`). Add a counter + trace event; **do not change the value**. Report in the PR how
often it fires — that number decides whether the value itself needs a ruling.

### A4 — Fix the two verification defects

- **A4a** `test_octagon_damage.py` `test_front_takes_no_arc_penalty` (~93-102): `if rear > 0: assert …`
  with **no** `assert checked >= N`. Vacuous if no seed produces rear damage. Its two siblings (`:85`,
  `:122`) do it right — copy them.
- **A4b** `test_morale_write_sweep.py:36-40` claims `build_unit` gives the subunit its own morale:
  ```bash
  cd tests/sim && PYTHONPATH=. python3 -c "
  from mass_battle.engine import build_unit; print(build_unit('Line',3,'A','A',20).subunits[0].morale)"  # None
  ```
  Both params test the *inheriting* branch, so `orchestration.py:2098-2103` — `between_turn_recovery`
  calling `set_morale(eff_morale)`, which **flattens every cell to the mean** each turn boundary — has
  zero coverage. `build_army` puts every gauge body there. If the flatten turns out to be wrong, **file
  it, do not fix in place**.

### A5 — Finish the scalar-write sweep · **GATES ALL OF §5**

Two harness sites left unswept: `lanchester_signature.py:126`, `test_persubunit_stress.py:191`. Under
`PC_CELL_MORALE=ON` they become silent no-ops — and `lanchester_signature` pins morale high
*specifically to disable rout*, so a no-op there measures the Lanchester exponent on **truncated**
battles. That exponent is what DG-6's entire root-cause rests on.

- **Do:** route both onto `set_morale`; add both to `_CELL_OWNED`.
- **⚠ Budget:** touching either file drags ~100 pre-existing uncited constants into the
  anti-fabrication gate. Expect to cite or ledger them. **This is why the sweep stalled last time.**

### A6 — Land the law harness report-only

`lanchester_signature` exits 1 today and **nothing runs it**:
```
[FAIL] LAW EXPONENTS  melee p=2.50 (≤1.4 linear)  volley p=0.50 (≥1.6 square)
```
`core/attrition.py` argues frontage-capping makes superiority *"a LINEAR edge, never square"*; measured
melee is **p=2.50 — the scan-grid ceiling**, so the true exponent is ≥2.5, worse than the square law it
claims to prevent. Wire it **report-only**. The blocking flip waits on fork #2 (two of its three PASSes
are degenerate: volley passes on `cas_exchange = inf`, and its melee 2:1 check demands ≥65% while
measuring 100%, where dg6 adopts ~70% as the historical target).

---

## §3 — TRACK B: ownership — one owner per fact, one loud invariant

Ten facts in mass battle have two or more owners and **nothing checks any of them**.

### B1 — `CellTable` · **the structural centrepiece**

Ten parallel per-cell maps on `Subunit` (`hierarchy/units.py:371-400` + `cell_troops`), no key-set
invariant anywhere. `Unit.check_drift()` re-keys `cell_troops` and **none of the other nine**:
```bash
cd tests/sim && PYTHONPATH=. python3 -c "
import inspect, mass_battle.hierarchy.units as HU
src=inspect.getsource(HU.Unit.check_drift)
for m in ['cell_troops','cell_morale','cell_start_troops','cell_breakpoint','_cell_target',
          'halted_cells','merged_cells','cell_facing_vec','cell_last_speed','_speed_accum']:
    print(f'{m:20s}', 're-keyed' if m in src else '*** NOT TOUCHED ***')"
```
Drift fires in ordinary play (`discipline_check_phase → check_drift`, `core/state.py:237`; any non-Line
shape below `MIN_DISCIPLINE`). After it `cell_morale` is keyed to a dead shape → aggregation collapses
to the key intersection → **morale immortality**, plus phantom breaks propagating to healthy cells.

**Design — read `02_remediation_plan.md` §3 first.** **Not a per-cell object.** Array-of-structs is
slower in a Monte-Carlo oracle and further from the `PackedFloat32Array` layout the Godot port wants.
Keep struct-of-arrays, add the missing owner:
```
CellTable   .ids   .troops .morale …   .add() .remove() .rekey()   .view(id)   .check()
            .check()  ⇒  every map's keys == .ids  AND  Σtroops == troop_count
```
- **B1a** introduce the owner — behaviour-preserving, **preserve float operation order exactly**.
  Verified by A1's digests in both modes. If they move, you changed behaviour: stop, find out why.
- **B1b** `.check()` at phase boundaries under a debug flag + a guard that corrupts one map and asserts
  failure.
- **B1c** route `check_drift` through `.rekey()`. One call replaces ten forgotten ones.
  **Changes battles under cell morale** — removes morale immortality and phantom breaks.

**This supersedes ED-MB-0043's phase-3/4 ordering.** Every new cell-owned field currently costs a new
map, a bulk-write site, a guard key, and a forgotten re-key. Ten fields paid that tax; Jordan's
directive names six more. **Pay it once here.**

### B2 — Collapse the six remaining duplicate owners

| Duplicate | Sites | Action |
|---|---|---|
| Combat-pool formula | `core/exchange.py:63-134` + `hierarchy/units.py:2339-2370`; docstring says *"Mirrors EXACTLY"*, no test. `(5.0-disc)*0.5` open-coded at `exchange.py:87` and `units.py:2337` | Collapse, or add the mirror-equality test. **The test may reveal they already drifted** — that is a finding. |
| Stamina ×3 | `_ColBlock.stamina`, `Subunit.stamina`, `Unit.stamina`; two live drain laws | One owner. Interacts with fork #7. |
| Facing/arc ×2 | `_per_cell_angle_mod` (`orchestration.py:872-1004`) + `_octagon_cell_mods` (`:1029-`, "THE single owner"); pin-perception gated differently (`:933` vs `:1076-1078`) | Retire legacy or unify gating; lift both out of the 652-line `resolve_engagements` so they are testable at all |
| Health ×2 | `unit.hp` vs Σ`cell_troops`; `eff_size`/`cohesion` read a *different ledger depending on subunit count* (`units.py:807-818`) | One ledger, other derived. Fold into B1. |
| Damage law ×2 | Band model vs linear PP-233 in `pursuit_damage` (`orchestration.py:2326`) | Fork #6 |
| Movement ×2 | `advance_cells` (grid) + `_node_advance` (field) | **Deliberate** — frozen oracle. Cost, not defect. |

### B3 — Wire or delete the dead machinery

ED-MB-0041's own rule. One line of disposition each: `provenance.py` (0 importers, every `loc` stale,
yet cited as canon at `orchestration.py:1153,1166`) · `merged_cells` / `resolve_internal_collisions`
(0 call sites) · `reform_check` (**canon-required**, mass_battle_v30 §A.5/PP-241, permanently dark) ·
`_find_contacts_field` · the `PC_FACING_MODEL` family · `COMMAND_SIGMA_ENABLED`.

### B4 — Conflict-prevention guards (so the class cannot recur)

Multi-owner scan for the MB tree · configuration-liveness guard (**reuse**
`test_structure_audit.py::test_code_roots_all_exist`, do not reimplement — CLAUDE.md §8) · citation
integrity resolving `[canonical: <doc> §<sec>]` and failing on a missing section (three fabricated
citations found) · pairwise flag coverage for the interacting families (`PC_CELL_*`,
`PER_CELL`×`FIELD_MOVEMENT`, octagon×cell-damage) · golden-drift disclosure required on any `EXPECTED`
change.

---

## §4 — TRACK C: observability — the battle must explain itself

**Jordan: *"make identifying what's happening… going forward."*** This track has no prior tracking
item. Seed exists: `workbench/trace.py` has `start_trace`/`get_trace`.

| # | Item | Answers |
|---|---|---|
| **C1** | **Per-phase casualty attribution** — tag every casualty with source (melee/volley/pursuit/freed-attacker/cellwise) + tick. **Load-bearing:** it is the only way to measure the §5 finding that the engine kills the loser *then* breaks him while history breaks *then* kills. Currently unmeasurable. | where losses come from |
| **C2** | **Break decision log** — why each subunit broke: which threshold, casualty fraction, morale, own break-point vs contagion | who broke first, why |
| **C3** | **Mechanism attribution** — per battle, which mechanisms were live and how much each moved the result. Turns "subunit-emergent, not cell-emergent" from inference into measurement. | what decided it |
| **C4** | **Invariant reporting** — surface `CellTable.check()`, hp-vs-cells agreement, and A3's truncation counter as first-class battle output, not debug prints | conflicts as they happen |
| **C5** | **Promote the workbench** — make the trace the standard diagnostic artifact so the next question does not need a 24th bespoke probe | all of it |

**Cap:** C1 and C4 are the load-bearing pair. C2/C3/C5 are valuable but optional until a specific
question needs them.

---

## §5 — TRACK D: the system itself

**This is "solve mass battle for itself".** All of it is gated on A5 → honest cell-morale measurement.

### D1 — Over-decisiveness (DG-6): **test the primitive before adopting the patch**

ED-MB-0016, open, needs_jordan. Melee attrition sums N independent per-soldier dice → CV self-averages
as O(1/√N) (measured 0.89→0.06 for N=4→1024) → outcomes collapse to 100%/0% where history shows bands.

`dg6_friction_resolution.md` correctly names **correlation across combatants** as the only lever that
breaks CLT self-averaging (citing Kress 2024), then implements the *simplest* form: one shared
per-battle LogNormal shock. **Its disclosed cost: gauge 6/20 → 4/20** — it buys strategic realism by
degrading tactical realism.

**But a second, mechanistic source of correlation already exists and has never been measured against
this problem.** ED-MB-0042's cell morale with 8-neighbourhood break contagion makes casualties arrive
in correlated clumps — from a primitive, at the tactical scale, per Jordan's own directive.
`PC_CELL_MORALE` is OFF and its one measurement was confounded and retracted.

**Order, and the order is the point:**
1. A5 (scalar sweep) → 2. honest cell-morale re-measure → 3. **re-measure DG-6's CV-vs-N curve with
cell morale ON** → 4. only then decide `PC_FRICTION_SIGMA`: adopt / lower / drop.

**Named falsifier:** if CV-vs-N still decays as O(1/√N) under the flag ON, this is wrong and the shared
shock is right. **That measurement does not exist. This is a hypothesis with a stated test.**

Separately (fork #3): the CEV *name* is wrong regardless — Dupuy's CEV is a persistent per-force fitted
residual, not an i.i.d. per-battle draw.

### D2 — Cell-primitive phases 3–4

After B1. Phase 3: stamina + discipline + quality per cell, retiring `col_grid` (blocked on fork #7 —
`col_grid` is a derived cache for density/depth but **authoritative** for stamina keyed to the
battlefield *column*, so fatigue does not follow men who shift laterally). Phase 4: hp + armour per cell.
Each inherits the write guard by adding one `_CELL_OWNED` key.

**Unblocks two deferred decisions:** `PC_STOCHASTIC_ROUT`'s fate (measured inert at 35.6% vs 36.1% —
but under the same confound, so undecidable until A5) and `ROUT_CASCADE_FRAC` (inert at 1.0 until
phase 3 defines a "section").

### D3 — Envelopment regimes

ED-MB-0039. Pure-infantry parity envelopment is deployment-chaotic (±54pp side swing); combined-arms is
stable and ~100%; the moderate 55–72% historical bands sit in an engine gap. Fork #A/#B stands.

**Two things this session adds:**
- **The standing diagnosis chases dead code.** ED-MB-0038/0039 blame the enveloper's APEX-forward
  centre. `engine.py:414-419` applies `APEX` **only when the caller omits `starting_position`**, and
  both harnesses pass it explicitly (`gauge_mb.py:257`, `bat.py:70`). **It never executes in H3/H10 or
  the golden battery.** Stop that line of investigation.
- **Two live candidates**, neither proven: `min()` over a **set** (`orchestration.py:1744`) tie-breaking
  by value-dependent iteration order; and banker's rounding at exactly `.5` (consistent with the
  measured start-row *parity* sensitivity). Falsifiers: canonicalise to `min(sorted(...))` and re-run
  the mirror; sweep start rows preserving the exact mirror midpoint.
- **Ordering:** do **not** decide D3 before D1's measurement — option B (gated seal-failure variance) is
  the same shape as D1's recommendation and may share machinery.

### D4 — R3 ranged-vs-ranged never engages

**ED-MB-0044, filed, needs_jordan. Its proposed fix was under-scoped — see §6.**

### D5 — Casualty shape and the missing pursuit

Totals are near-band (loser 29–41%, winner 3.3–17%) but the **causal shape is inverted**:
`pursuit_damage` is called only inside `run_multi_unit_battle`, which the gauge, `bat.py` and
`lanchester_signature` never invoke. So the engine generates the entire loser total during formed
melee, pre-break. History generates it in flight. **The engine kills the loser then breaks him;
history breaks then kills.** C1 is the only way to measure this. The 15–30% band is also doing double
duty as both break-onset and total-loss band — coherent only because pursuit is absent.

### D6 — Historical grounding repairs

`triplex acies` is misapplied — a **depth** arrangement cited for a lateral tripartition — and it is
load-bearing (fork #4). du Picq's 15–30% break band is **not his** (it is a 2026-07-23 directive
re-attributed in `core/state.py:35,118`). Envelopment **inverts** du Picq: the dominant modelled effect
is a damage multiplier with morale downstream, where his claim is that flank/rear attacks kill
*because the defender breaks*. Sabin is cited on both sides of a depth contradiction — depth both
relieves *and* kills, so "too deep to fight" (the Cannae Roman column) is unrepresentable.

---

## §6 — TRACK E: canon, params, contract, registries

| # | Item |
|---|---|
| **E1** | **Delete the phantom emit row — cheapest win in the whole plan, one line.** This is **ED-MB-0010, open since 2026-07-13**. `references/module_contracts.yaml` `mass_battle.emits` lists both `scene_outcome.battle_concluded` and `scene.battle_concluded`; the former is **not a Key** — it is the *family* name of the latter. Confirm: `python3 tools/observability/build_graph.py` then check `graph.json` keys — only `scene.battle_concluded` exists. **Closes five surfaces at once** (structure_audit dangling-emit, vector Mode E, vector Mode H, workbench card `wb-00aeffeb7f`, `INCOMPLETENESS.md:146`). Caveat: the file is nominally regenerate-never-hand-edit — confirm the path first. |
| **E2** | ED-MB-0009: orphaned rule fragment citing a `stage5_clocks.md` that has **never existed**. Reconstruct or remove. |
| **E3** | ED-MB-0008 → **re-scoped to docs-only**: neither contradictory DR table is what the code implements (armour catalogue explicitly unwired at `equipment/armour.py:16-18`; engine uses a free scalar defaulting to 1). Priority drops. |
| **E4** | 3 of 6 MB docs have **no `## Status:` line**; the `CURRENT.md` head is `WORKING DESIGN`, not CANONICAL, while the integration doc beside it *is* canonical. |
| **E5** | `engine/params/mass_combat.md` describes a **7-phase d10 dice game**; the engine runs continuous ticks with a per-cell morale lattice and octagon multipliers. Header cites a path that has never existed; stamped `2026-04-03`. Reconcile or mark superseded. |
| **E6** | The `mass_battle` contract declares `consumes: []`, `state: []` — **deliberately deferred** until B1/B2 settle what state a battle owns. Ship an honest `status`/`gap_notes` now; populate after Track B. |
| **E7** | Typed params — point `tools/export_engine_params.py` (already working, CI round-trip-checked for personal combat) at MB's `config.py`. **Gated** on D1/fork #6: ED-MB-0041 found only ~17 of ~92 MB magnitudes survive scrutiny. |
| **E8** | Correct the record: retire ED-MB-0041's armour-inversion claim (**refuted** — measured 0.115/0.061/0.035/0.015 at dr 0/1/2/3, monotone decreasing); correct the ED-MB-0038/0039 APEX text (§5 D3). |

---

## §7 — DO NOT EXECUTE: eight Jordan forks

1. **The two engine trees** — declare / adapter / promote. Under "declare", campaign-scale `mc_v18`
   conclusions come from the **stale** model and reflect none of this work.
2. **Two incompatible 2:1 validation targets** — `lanchester_signature` demands ≥65% and measures 100%;
   dg6 adopts ~70%. One must be repudiated before A6 can become a gate.
3. **CEV naming and σ** (D1).
4. **`triplex acies`** — `n_cmd` is the only free parameter landing H3 in band, chosen *after* measuring
   the 0/53/95 sweep.
5. **The emergence verdict** — the cell is not yet load-bearing; envelopment is builder-authored, and
   the repo's own sweep found H4 passes with envelopment pathing **OFF**. Delete the cell layer and
   little shipped behaviour changes.
6. **Which damage law is canon** — the band model cites a nonexistent `§A.4`; PP-233 is linear.
7. **Where fatigue lives** — blocks `col_grid` retirement (D2).
8. **The absent mechanisms** — terrain, pursuit in the measured mode, the general as an entity,
   surrender/prisoners, ammunition, weather. **These would change battles more than all of §2–§6
   combined**, and they are design, not repair.

---

## §8 — ED-MB-0044 (R3): read before touching

The handoff once called this "ship without a ruling". **That was wrong** and is corrected in the ledger.
Verified:
- `STANCE_SPEED_MOD['hold'] = -99` (`config.py:262`) independently zeroes `step`, and all goal
  resolution sits behind `if target_centroid and step > 0:`. Removing the early-return achieves
  **nothing alone** — it is a two-gate change.
- `hold` is **load-bearing**: `build_envelopment`'s `freeze_wings` is documented as relying on it,
  `build_refused_flank`'s refused wing, and `STANCE_COMMITMENT`'s defensive pool treatment.
- `_kite_goal` does **not** generalise: `PC_KITE_STANDOFF = 5` vs max melee reach 0.3 (pike) → the band
  `[5, 0.3]` is inverted.

**Recommended instead:** change the **R3 scenario** (`stance='balanced'` + `instructions=('kite',)`),
not the engine's `hold` semantics. *Falsifier:* run it that way — casualties should become non-zero and
draws drop. If still 100% draw at 0.0%, the analysis is wrong.

---

## §9 — Order

```
A1  field goldens in CI ─────────────────────────► GATE for A2 and B1
     ├── A2 degree guard          [CHANGES BATTLES]
     ├── A3 loud truncation        ├── A4 verification defects
     ├── A6 law harness (report-only)
     └── A5 scalar-write sweep ───────────────────► GATE for ALL of §5
                                                      │
B1  CellTable (a→b→c)  [B1c CHANGES BATTLES] ◄───────┤
     └── B2 duplicates · B3 wire-or-delete · B4 guards
                                                      │
C1 + C4  observability ── start early; they are how you SEE whether
                          A2/B1c/D1 changed what you think they changed
                                                      ▼
D1  cell-morale re-measure → DG-6 CV-vs-N under correlation → decide σ
     ├── D2 cell phases 3–4      ├── D3 envelopment (after D1)
     └── D5 pursuit/casualty shape (needs C1)

any time, independent:  E1 (1 line, cheapest win) · E8 (editorial) · E4
```

**Critical path: A1 → A5 → D1.** **First merged PR in an hour: E1.**

---

## §10 — Conventions

```
[scope] description (ED-MB-NNNN)     scope ∈ editorial|patch|simulation|infrastructure|fix|bugfix|design|godot|cleanup
```
Commit body states: what changed · the guard **and that it was mutation-verified** · test results · if
goldens moved, **which mechanism and by how much**.

PRs fill `.github/PULL_REQUEST_TEMPLATE.md`; held-back items called out **loudly** (ED-1094 — merging
ratifies PROPOSED contents by default).

```bash
python -m pytest tests/valoria -q
python tools/valoria_local.py --staged
python tools/validate_ed_citations.py        # if a ledger or id_reservations changed
python tools/currency_consistency_check.py
```

**Open MB ledger items this plan covers:** ED-MB-0008 (E3) · 0009 (E2) · 0010 (E1) · 0016 (D1) ·
0044 (§8). **Not covered:** other lanes' backlog — see their `HANDOFF_<LANE>.md`.
