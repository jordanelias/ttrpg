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

---

# §11 — ADVERSARIAL AMENDMENTS (Fable-5 review, 2026-07-26)

Four Fable-5 critics attacked this plan (ordering/gates · technical design · evidence · orchestration),
read-only, relay-pattern. **Every amendment below was re-verified by the orchestrator.** Two critics
were still running when this was written — noted at §11.9.

## 11.0 — ⚠ THE SHIPPED CONFIGURATION'S GOLDEN IS CURRENTLY RED

**MEASURED, clean working tree, `main` @ `46a25ca`:**
```
$ cd tests/sim && python3 mass_battle/bat.py --check          # exit 1
DIGEST cell_field  3a0952b331d6ba1e...
[BYTE-EXACT FAIL] cell_field: expected a1a97940fed111fa... got 3a0952b331d6ba1e...
```
`bat.py` last moved in **#236 (2026-07-25)**. The `cell_field` digest — the shipped configuration
(`FIELD_MOVEMENT=1`) — **has been failing since then and nobody knew, because nothing runs it.**

S1.5 was not a risk. It is a realised, undetected regression. Three consequences:

1. **A1 is now unambiguously first**, and gains a sub-task: **A1a — re-baseline `cell_field`, with the
   drift root-caused and the mechanism published.** Do not re-record blind; find what moved it.
2. **This refutes an amendment the ordering critic proposed** on the basis that "the field goldens
   already exist and already pass at HEAD (exit 0)". They do not pass. Amendment 11.1 is *rejected*
   in its original form — recorded because a rejected attack is evidence too.
3. **New ordering constraint neither the plan nor any critic had:** B1a cannot use "digests unchanged"
   as its correctness proof until A1a lands. **You cannot prove you changed nothing against a baseline
   that is already wrong.**

## 11.1 — Critical path was wrong at both ends · **I introduced this regression**

`02_remediation_plan.md` §9 correctly stated `A1 → B1 → B3`, with the DG-6 re-measure *after* Phase B.
`03`'s §9 silently swapped B1 off the path in favour of `A1 → A5 → D1`, with no rationale anywhere.

**Corrected critical path: `A1a → A1 → B1a → B1b → B1c → D1`.** B1 is the size-L refactor of a 10.5k-LOC
data model; it is the longest pole and belongs on the path. A5a and A2 run parallel, not in series.
**`HANDOFF_MB.md` carries the wrong path too and must be corrected in the same commit**, or a fresh
session inherits it from the banner regardless of this file.

## 11.2 — ⚠ WORST DEFECT: D1 was not gated on the `check_drift` fix

D1's ordering (§5) read: A5 → cell-morale re-measure → CV-vs-N → decide σ. **`B1c` appears nowhere.**

But this plan's own register calls S1.4 a **"re-flip blocker"**, and the confounded-and-retracted
measurement ran the gauge in **multi mode**, whose roster includes non-Line shapes. Orchestrator-verified
trigger:
```
MIN_DISCIPLINE: Line 1 · Column 3 · Arrowhead 4 · GappedLine 5
condition: eff_discipline < MIN_DISCIPLINE[shape] AND shape != "Line"
measured: 20 re-key events / 20 battles (Arrowhead, Column @ discipline 2); 0 for Line-only
```
Running the flag ON for a *measurement* is subject to the identical confound as a *flip*. Executed as
written, D1 would produce a **third** confounded measurement — on the plan's flagship decision, the
exact failure this plan exists to end.

**Amended D1 order:** 1. A5a → 2. **B1c, or a standalone `check_drift` full re-key fix** (ten maps,
mutation-verified — this does *not* require the full CellTable, which shortens the path) → 3. honest
re-measure → 4. CV-vs-N ON → 5. decide σ. **A cheaper unblock exists and must be tried first:** if D1's
matchups are Line-only, instrument a drift counter and **assert 0 across all D1 battles**. If it holds,
D1 runs before B1c; if it fires, B1c is a hard gate. Either way the assertion is the artifact.

## 11.3 — ⚠ D1's falsifier was measuring the wrong quantity · **the estimand trap**

`dg6_friction_resolution.md:20-22` measures **"CV of net"** from `roll_pool(N)` — a **roll-level**
quantity, the CLT self-averaging of N per-soldier dice. Cell-morale contagion operates at the **battle**
level. It does not change the distribution of a single pool roll.

**So the falsifier as written — "if CV-vs-N still decays as O(1/√N) under `PC_CELL_MORALE=ON`" — would
fire vacuously and falsely kill the hypothesis, on a measurement that cannot see the effect.**

**Corrected estimand:** CV of **battle outcome margin** and **loser casualty fraction** across seeds, as
a function of army size N, at fixed matchup. **The OFF arm must first demonstrate that this
battle-scale quantity also decays ~O(1/√N)** — if it does not, DG-6's framing needs re-deriving before
any arm runs.

**Four arms, pre-registered before any confirmation run:** (0) both flags off — baseline **and positive
control**, must reproduce the decay; (1) `PC_CELL_MORALE=1` — the hypothesis; (2) `PC_FRICTION_CEV=1,
σ=1.1` — **known-cure comparator**, defines what "fixed" looks like; (3) both — interaction /
double-count check. Arm 1 is judged by which reference curve it resembles, not against an absolute
threshold. **Arms are independent samples, not paired** — the ON arm consumes extra RNG draws, so equal
seeds are not matched replicates.

**Pre-registration is the §0.1 #3 artifact:** estimand, arms, N-grid, seed blocks (exploration
0–99 / confirmation 100–499, confirmation untouched until frozen), decision rule, falsifier — committed
*before* the confirmation block runs. **No constant may change between blocks; any parameter touch
reopens pre-registration.**

## 11.4 — A5 must split; its budget was misstated

Agent-measured via the gate's own checker (orchestrator did not re-run it — flagged as agent-MEASURED):
`lanchester_signature.py` → **6** blocking constants; `test_persubunit_stress.py` → **116**.

Also: `test_persubunit_stress.py:191` fails **loudly** (its assert at `:193` catches it), not silently.
It therefore gates the eventual default *flip*, not any §5 *measurement*.

- **A5a** — lanchester reroute + ~6 citations. **Gates D1.** Small. Start day 1, parallel to A1.
- **A5b** — persubunit reroute + the ~116-constant ledger job. **Gates nothing on the critical path.**

The plan's "~100 constants" chained the whole ledger job in front of a measurement needing six — and
bundling is the *documented cause of the last stall*.

## 11.5 — E1 is not a one-line hour

`ED-MB-0010` carries `needs_jordan: true` and the row is tagged `[OPEN — Jordan]`. Under ED-1094 a merge
*can* ratify it — but only with the ledger flip co-committed and the ratification called out **loudly**
in the PR body. Real scope: the YAML row · the `[OPEN — Jordan]` comment · the ED-MB-0010 status flip ·
the dead alias in `build_graph.py` · regeneration of the five downstream surfaces (they are snapshots,
so "closes five surfaces" is deferred until regen).

**The "regenerate-never-hand-edit" caveat resolves in the plan's favour: no generator exists.** Hand
edit is the only path. Keep E1 as the cheapest win; stop calling it one line, and never merge it as
silent hygiene.

## 11.6 — Two more ordering hazards the plan missed

- **A2 vs B1a are mutually unsequenced.** A2 deliberately re-records all goldens; B1a's only proof is
  "digests unchanged". Run concurrently, A2's re-record lands mid-B1a and either raises a false alarm or
  silently absorbs a real B1a behaviour change. **Rule: A2 merges and re-records before B1a's final
  verification; B1a re-baselines after any golden-moving merge.** Combined with 11.0: **one
  golden-moving PR in flight globally, ever.**
- **B3 lets a session wire `reform_check`.** That is canon-required and currently dark; wiring it
  changes battles, deleting it repudiates canon. **Its only permitted disposition is *file for fork
  ruling*** — both branches are §7-class.

## 11.7 — Track C: keep it early, but bind it

The tension (instrumentation perturbing the goldens it protects) is real and **already solved in-repo**:
`workbench/trace.py` documents a gated seam that is "no-op unless ON → byte-exact", and the digest hashes
only the trial vector, not event streams.

**Binding rule for every C-track PR:** use the existing `start_trace`/`trace_event` seam — gated, **zero
RNG draws**, no float writes to engine state. Merge guard: all `bat.py --check` digests byte-identical
with tracing off, mutation-verified by inserting a state-perturbing event and watching a digest move.

**C4 "start early" was wrong:** two of its three surfaces do not exist yet (`CellTable.check()` from
B1b, the truncation counter from A3). Only the hp-vs-Σcells slice starts now. **C1 correctly sequences
after A2/A3 and before B1a** — where its conservation check becomes a *second* behaviour-preservation
instrument during the refactor.

## 11.8 — Orchestration for a max-intensity session

**Global.** Relay, not dialogue — critics are dispatched *after* the producer with the artifact only
(diff / protocol / measurement table), never the producer's reasoning, and always read-only. Lanes
return a fixed-format summary (`task · files · guard+mutation-verified Y/N · digests moved Y/N +
mechanism + magnitude · constants dragged in · falsifier outcome · next action`). **The orchestrator —
never a lane — writes `HANDOFF_MB.md` and allocates ED-MB ids** (serialise `next_free`; concurrent
allocation is the exact failure the lane namespace was built against). **Sim runs are Bash in one
environment, never delegated** — per-agent environment drift between arms is the confound machine.

**Per-task shape.**

| Task | Fan-out | Tiers and lenses |
|---|---|---|
| **A1/A1a** | 3 | Haiku: exhaustive env-flag inventory (pins must be exhaustive, not minimal — ED-1089 precedent) · Sonnet: the CI job · **Opus read-only critic**: pin-matrix completeness + demand the mutation artifact. **Orchestrator runs the job twice — if the two runs differ, STOP; that halts B1 too.** |
| **A2** | 3 + measurement | Haiku: call-graph of every σ producer reaching `compute_degree` · Sonnet: guard + test · **Opus critic**: the real question is **epsilon magnitude vs *designed* fractional nets** — `PC_FRACTIONAL_POOL` and `_morale_sigma` produce legitimately non-integer nets meant to land `Partial`; prove the epsilon cannot promote the smallest designed decrement. Attribution: a temporary degree-flip counter, with `counter = 0 ⇔ digest identical`. |
| **A5a** | 4 | Sonnet: reroute (**preserve the semantic trap** — the `1e9` pin exists to disable rout; under the flag `set_morale` must propagate it to cells; falsifier = `assert not routed` every tick **plus** `assert checked >= TRAJ_SEEDS`) · Haiku: constant extraction · Sonnet ×1: classify · **Opus citation critic**: resolve every `[canonical: doc §sec]` against the actual doc, fail on a missing section. Non-negotiable — three fabricated MB citations already exist. |
| **B1a** | producer **SOLO** | Haiku: exhaustive ten-map read/write inventory (also the critic's coverage oracle) · Sonnet: order-sensitivity scan (`.values()` aggregation, `set` iteration, float summation order) · **producer = the main Opus session, not a subagent** · **Opus read-only critic** sees diff + inventory only. **Do not split the ten maps across agents** — that guarantees inconsistent invariant semantics at the seams. **Critical semantic:** `cell_morale` is *empty until seeded*, and the scalar path must stay verbatim — the key-set invariant must accommodate deliberately-unseeded maps or B1a silently changes every unseeded battle. |
| **C1** | 3 | Haiku: every casualty-mutation site · Sonnet: tag through the trace seam · **Opus verifier**: (a) **conservation** — Σ attributed == total hp delta, mutation-verified by untagging one path; (b) non-perturbation. Conservation is a total check, so a bypassed path cannot hide. |
| **D1** | see 11.3 | Runs = Bash, one environment. Fits = scripted. **Verdict = Opus applying the pre-registered rule** — pre-registration exists so the verdict is not a judgment call. |

**Fable 5 — strict promotion list, two nodes only.** §10 makes fable an *upgrade trigger*, never a
default, and over-promotion is the failure mode.
1. **The D1 protocol referee** — the only node with documented evidence of a cheaper tier failing *this
   exact node, twice*. Gets the frozen protocol doc alone, read-only, one question: **are the arms the
   same experiment, and can the estimand observe the effect it claims to test?** §11.3 proves this node
   is not ceremonial — it is what caught the estimand trap.
2. **B1a divergence root-cause — conditional only**, if digests move and one full Opus attribution pass
   fails. Record the failed Opus artifact as the promotion evidence.

Explicit non-promotions: re-running Fable critics over implementation diffs re-audits settled findings;
B1a *authorship* is engineering, not judgment (the design is already ruled); §7 fork memos are Opus
synthesis — the judgment in a fork belongs to Jordan, not a bigger model.

**Do not parallelise:** B1a's write · D1's execution · golden re-records (one globally, ever) · ED
allocation and handoff writes · the small tasks (E1, A3, A4, B1b — dispatch overhead exceeds the task) ·
critic multiplication (one independent critic per gated artifact).

**Concurrency map.** Wave 0 serial: **A1a → A1**, and E1 anytime. Wave 1 parallel worktrees, one PR
each: A3 · A4 · A5a · E8/E4 — with **A2 alone in the single golden-moving slot on main**. Wave 2 serial:
C1 → B1a → B1b → B1c. Wave 3: D1 (background sweeps) with A6 · B3-dispositions alongside.

**Stop conditions.** Field digests differ across two identical local runs · A2's flip-counter leaves an
unexplained residual · A5 classification needs a *new canonical magnitude* (fabrication territory) ·
**any** digest movement during B1a (no acceptable delta exists) · any map turns out to carry semantics
incompatible with a shared key-set (that is design, not refactor) · C1 conservation cannot hold without
reordering damage application (instrumenting must never restructure the instrumented) · D1 Arm 0 fails
to reproduce its control, or fingerprints differ beyond the flag under test, or the drift-counter
assertion fires · **any** urge to tune σ or contagion constants to improve an arm's banding · any task
that turns out to need a §7 answer.

## 11.9 — Review status

Two of four critics (technical design, evidence/audit-the-audit) were still running when this section
was written. **§11 is therefore incomplete, not final** — a session picking this up should expect a
further amendment block, and should treat the technical design of `CellTable` (§3) and the residual
strength of the S1.1–S1.5 evidence as **not yet adversarially settled**.

---

# §12 — SECOND AMENDMENT BLOCK (technical-design critic)

Completes §11.9's outstanding review. Orchestrator-verified where marked.

## 12.1 — ⚠ MY A2 GUARD IS VACUOUS · **the plan committed the defect it exists to fix**

**MEASURED:**
```
ob=1: (ob-1e-16)==ob ? False  → 'Partial'    ← only this one works
ob=3: (ob-1e-16)==ob ? True   → 'Success'    ← passes on UNFIXED code
ob=6: (ob-1e-16)==ob ? True   → 'Success'    ← passes on UNFIXED code
math.nextafter(ob,-inf) → 'Partial' for ob ∈ {1,3,6}   ← a guard that CAN fail
```
`ulp(3) ≈ 4.4e-16 > 1e-16`, so `3 - 1e-16` *is* `3`. The guard specified at §2/A2 **cannot observe
the failure it excludes** — CLAUDE.md §0.1 #2, in a plan whose §2 theme is vacuous assertions.

**Replacement guard:** `compute_degree(math.nextafter(ob, -inf), ob) == "Success"` for `ob ∈ {1,3,6}`,
**plus** the `_sigma_net_boost(-1e-16, 9)` repro verbatim. Mutation-verify both.

## 12.2 — A2 is under-specified in three further ways

- **Epsilon unstated.** Both operands are floats (`ob = max(1, b_net)` carries its own σ-boost), so the
  guard must absorb error in *both*. Specify **absolute `1e-9`**: net magnitudes are bounded by pool
  scale, so accumulated ulp error is ≤ ~1e-13, while a *designed* σ landing within 1e-9 of a threshold
  is ~1e-9/exchange. A relative or 1e-6 epsilon starts eating real `Partial` outcomes.
- **Only 1 of 3 boundaries named.** The same noise class attacks `net <= 0` (a mathematically-zero
  boost computed as +1e-16 escapes `Failure` — biasing *toward* damage) and `net >= 2*ob`. Guarding
  `Success` alone institutionalises an asymmetric attacker-favouring correction. **All three
  comparisons in `resolution.py:64-68` get the same treatment.**
- **A redundant producer fix already exists and must be reconciled.** `units.py:621-631` is an
  exact-uniform-mean special case whose own comment describes this precise degree-boundary failure.
  A2 makes it redundant. **State which regime is authoritative and whether that special case stays** —
  two overlapping exactness regimes with different scopes is how the next confounded measurement
  happens. Preferred shape: snap `|σ| < 1e-12 → 0` at the `_sigma_net_boost` chokepoint (the
  semantically-correct statement) **and** epsilon all three consumer boundaries.

## 12.3 — ⚠ B1b's invariant is FALSE BY DESIGN · **fails as written**

`.check()` was specified as "every map's keys == `.ids`; Σtroops == troop_count". Both halves are wrong:

- **Emptiness is the feature.** `cell_morale` / `cell_start_troops` / `cell_breakpoint` are *empty until
  seeded*, and `eff_morale` branches on `if self.cell_morale:` — **emptiness IS the `PC_CELL_MORALE`
  gate**. Forcing `keys == ids` turns cell semantics permanently ON. `_speed_accum` is documented
  "empty and untouched on the default path → byte-exact". `halted_cells` / `merged_cells` are
  rebuilt per tick and are strict subsets *by semantics*. `cell_facing_vec` / `cell_last_speed` are
  lazily populated in movement order, and **both their truthiness and their contents are consumed**
  (`orchestration.py:1773-1774` branches on truthiness then averages the values) — pre-keying flips a
  live branch and changes a float mean.
- **`Σtroops == troop_count` is false from the first casualty:** `troop_count` is a spawn constant;
  casualties go to `cell_troops` only.

**Corrected spec — per-map class, not one rule:** *value maps* → empty XOR `keys == ids`;
*lazy/set maps* → `keys ⊆ ids`; conservation → `|Σcell_troops − last_conservation_point| ≤ ε`, never
against `troop_count`. As originally written the check is red on tick 1 of every battle, which makes
B1b's "corrupt one map and assert it fails" guard **unfalsifiable**.

## 12.4 — The CellTable rationale was measurably backwards · **decision re-opened**

**Agent-MEASURED** (CPython 3.11, 25 cells/subunit, identical access patterns): a dict of `__slots__`
cell objects (AoS) beat the parallel-dict layout (SoA) on **every** pattern — keyed 2-field read 1.10
vs 1.29 µs, `items()` iteration 0.80 vs 1.08, 2-field write 1.33 vs 2.22. **AoS is 15–40% faster.**
The SoA locality intuition is a compiled/numpy fact; a `(r,c)`-tuple-keyed dict of boxed floats has no
locality, so *k* fields cost *k* hashes under SoA vs one hash + *k* slot reads under AoS. At engine
scale the delta is ~2–3 s across a multi-minute gauge run **in either direction — it decides nothing.**

The Godot half is also decorative: *neither* layout is a `PackedFloat32Array`; both are tuple-keyed
hash maps, and the sketched `CellTable` does not change the keying scheme.

**Both stated reasons for rejecting a per-cell class are false.** The design may still be chosen, but
on the *true* argument — a thin wrapper over the existing dicts is the lowest-float-order-risk
introduction path — and that variant **enforces nothing** (12.5). State the real trade or re-open.

## 12.5 — "Owns the state" and "behaviour-preserving by construction" cannot both hold

External writers exist in every layer (`percell.py:119`, `orchestration.py:1705` replaces the attribute
outright, `contact.py:222`, `check_drift`'s wholesale `a.cell_troops = {…}`, `seed_cell_morale`), and
duck-typed readers assume dict semantics (`getattr(atom,'cell_troops',None) or {}` — a proxy without
`__bool__` silently changes that branch). **Either** B1a exposes the live dicts through properties, in
which case the maps themselves escape and `.view(id)` is irrelevant — detection at phase boundaries,
not prevention — **or** it rewrites ~50 sites, which is exactly where the float-order risk lives.
In Python you get at most one. The plan claimed both.

## 12.6 — B1c is not "S" — it hides ~4 unmade policy rulings

Drift has **no old→new key bijection** (arbitrary shape → Line, different cell count). `cell_troops`
has a defined policy. `cell_morale` does not — mean? troop-weighted? *carrying the low-morale corner is
the feature's entire point.* `cell_breakpoint` is a **drawn random value**: redraw (shifting the
`_cell_random` stream for every later draw) or inherit (from which dead cell)? Same for `_cell_target`
and the lazy maps. **At least the morale and breakpoint policies are §7-class design rulings**, sized
"S" in the plan.

## 12.7 — The verification net has a hole exactly over the bug being fixed

A1's digests run at default `PC_CELL_MORALE=0`, where the three cell-morale maps are **empty**. So
"behaviour-preserving, verified by A1's digests" verifies float-order for every map *except the three
whose desync is the headline*, and B1c's battle-visible change has no golden, no gauge row, and no CI
mode observing it. **A fifth digest mode (`PC_CELL_MORALE=1`, freshly recorded) must exist before B1a
starts**, or the "if digests move, you changed behaviour" protocol is vacuous over cell state.

## 12.8 — Both field goldens are stale, not just `cell_field`

Agent-MEASURED: `unit_field` also mismatches (`6f594233…` vs committed `d44f211f…`), and pinning
`PC_STOCHASTIC_ROUT=0` still mismatches — so **≥2 mechanisms** moved the field digests since their last
recording (2026-07-23/24), while the impulse-momentum change and the `PC_STOCHASTIC_ROUT` flip landed
2026-07-25 with no field re-record. **A1a is a bisection task, not a re-record.** Also: `bat.py`'s mode
key reads only `PER_CELL`/`FIELD_MOVEMENT`, so a run missing `PC_NODE_COHESION=0` silently checks a
node-cohesion battle against the grid golden — **the CI job must pin the full `_PINNED_OFF` vector**,
not the two toggles A1 names.

## 12.9 — A3 will measure zero and mislead; B2's "or" is illusory; A5 needs a carve-out

- **A3:** the repo's own audit found the cascade never produces >1 group in the pinned grid battery, so
  "report how often it fires" reads **0** there. Report from gauge multi-unit / field / Cannae
  workloads. And frequency is the wrong quantity — truncation drops the *deepest-sorted* groups, a
  systematic bias against deep formations (precisely D6's "too deep to fight"). **Count truncated pairs
  and their engaged-troop weight.** Note `trace_event` is a no-op unless tracing is on, so the counter
  must ride the result dict or C4.
- **B2:** the mirrors have **already diverged** in three flag-gated branches (friction CEV + yield malus
  in the subunit path; `OVEREXTEND_PENALTY` in the unit path; plus side-effect asymmetry on `broken`).
  So "the test may reveal drift" is not a possible outcome — it is certain. A defaults-pinned test
  **passes while certifying a false docstring**. Collapse is the only real option, and it needs a
  ruling on whether the pursuit pool carries CEV/yield — fork-adjacent, not a refactor.
- **A5:** `lanchester_signature.py:126` is `ua.morale = ua.morale_start = NO_ROUT_MORALE`. The
  `morale_start` half is **non-cellular** and must stay a bare write — so it needs a `_CELL_OWNED`
  whitelist entry, or the sweep gate blocks its own fix.

## 12.10 — Revised verdicts

| Item | Verdict |
|---|---|
| A1 | **Fails as written** — both field goldens stale; job red on first run; needs bisect + full toggle-vector pinning |
| A2 | **Guard vacuous (verified)**; epsilon unstated; 1 of 3 boundaries; reconcile with the `units.py:621-631` producer fix |
| A3 | Survives, amended — count pairs × troop weight, from workloads where cascades actually occur |
| A5 | Survives with a `morale_start` carve-out |
| B1a | **Major amendment** — rationale measurably false; enforcement vs behaviour-preservation contradiction; needs a 5th recorded mode first |
| B1b | **Fails as written** — invariant false by design for ≥5 maps and after first blood |
| B1c | Survives as a goal; **size wrong** — hides §7-class rekey policy rulings |
| B2 | Amendment — drift already certain; the "or" is illusory |

**Most likely to fail in implementation: B1a.** Its success criterion is triply compromised — the
goldens are already red, they run blind to the cell-morale maps, and it must preserve per-map insertion
orders that a unified `.ids` cannot represent plus an RNG draw order nothing records. **The predictable
outcome is a fourth retracted flip: a refactor declared behaviour-preserving because a blind instrument
did not move.** Do not start B1a until 12.7 and 12.8 are closed.

---

# §13 — THIRD AMENDMENT BLOCK · **§0's governing fact #1 is REFUTED by measurement**

The evidence critic instrumented the engine (pass-through wrappers, proven non-perturbing — grid
digests reproduced byte-exact with wrappers installed) and ran the full bat battery ×4 modes plus the
full 20-row × 60-seed gauge. Its measurements overturn the plan's own framing. **Agent-MEASURED at
scale; the orchestrator verified the drift and golden legs independently.**

## 13.1 — "Battles are being distorted right now" fails on all three legs as stated

| Leg | Claimed | **Measured** |
|---|---|---|
| Degree-boundary ulp (S1.2) | "Exchanges are being zeroed" | **209,778** `compute_degree` calls; 137,951 with non-integer nets; **ZERO within 1e-9 of an integer; ZERO degree flips.** `_sigma_net_boost` over ~190k calls is **bimodal** — exactly `0.0` or `≥1e-3`, nothing in between |
| Sub-phase truncation (S1.3) | "Deep formations lose fights" | **102,260** cascade calls; max depth-group count ever observed **3**, against a bound of **5**; **ZERO truncations, ZERO dropped engagements** |
| `check_drift` desync (S1.4) | listed among current distorters | Drift **fires 125×/gauge battery** (confirmed, stronger than my own measurement) — but the *morale* consequences stay **latent** behind `PC_CELL_MORALE=0` |

**Corrected fact #1.** Two things *are* distorting or misreporting battles right now, and neither was in
my list: **(a)** the shipped-mode goldens are already red (§11.0/§12.8), and **(b)** the casualty-realism
scoreboard reads **2/20** with loser-conditioned means spanning **29.1–79.2%** (H6 = 79.2% at a 100%
win rate; H4/Cannae decA = 5.0, below its 45–62 band). My §4.2/D5 text quoted a 07-25 scoreboard as if
current — disclosed in §7 as "the repo's own recorded measurement", then used as live. **D5's premise
"totals are near-band" is wrong; the current miss is wide.**

**A2 keeps its guard (it is cheap, correct hygiene and §12.1 fixed its vacuity) but LOSES its
"CHANGES BATTLES" label** — the prediction is now explicit and testable: *A2 moves no digest in any
mode.* State that prediction in the PR; if a digest does move, something else is wrong.
**A3 likewise drops off the severity-1 list** — count it, but its measured incidence is zero.

## 13.2 — S1.1's exponent is an artifact, not a measurement · **A6 and fork #2 are mis-scoped**

The harness's "no-rout" premise is broken: `NO_ROUT_MORALE=1e9` does not disable rout, because
`_stochastic_break` triggers on **casualty fraction**, not morale, and the punch drives any finite pin
to −1. Measured: **40/40 melee trajectories terminate by rout**; the fit window collapses to 30 ticks;
the cv objective is **monotone across the entire scan grid with no interior minimum** — so `p=2.50` is
a **grid-endpoint artifact of an unidentifiable fit on rout-truncated data**, not an attrition-law
estimate. And `PC_STOCHASTIC_ROUT` defaulted ON on 2026-07-25 — *one day before these audits* — silently
breaking the instrument.

Volley is worse: **40/40 trajectories, 0.0% casualties on both sides**; `cv = 0` at every `p`, so
`best_p = 0.5` is just the first grid point. The `inf` exchange ratio comes from a `0/0` guard — **both**
sides took zero and the big side won **0/100**. Nothing happens in the volley scenario at all (the same
ranged-hold standoff as ED-MB-0044, which the plan tracks separately without noticing it also zeroes
this leg).

**Consequence:** "the true exponent is ≥2.5, worse than the square law" is **unsupported** and must be
struck from the register and from §2/A6. **A6 as written wires an instrument in which three of four
checks are degenerate and the fourth is unidentifiable — report-only wiring would report artifacts with
green-looking provenance.** The prior task is **repairing the harness** (make the rout pin actually
disable rout; make the volley scenario exchange fire) — that is now A6a, and fork #2 cannot be
adjudicated until it lands.

## 13.3 — ⚠ Fork #5's emergence verdict is REFUTED as written · **highest-leverage overclaim in the corpus**

"Delete the cell layer and little shipped behaviour changes" is an inference drawn from evidence about
the **cell-morale programme** — a gated-off, once-measured-and-retracted feature — and then promoted
into a claim about the **entire per-cell substrate**. Against it:

- The register's own §4.1 credits the octagon **damage-received multiplier** as envelopment's dominant
  effect — and it is computed from **`cell_facing_vec` and per-cell contact arcs**, i.e. from the cell
  layer. **The verdict contradicts the same document's fidelity section.**
- `_charge_shock_sigma` returns 0.0 unless `PER_CELL`; fatigue, depth, density and cavalry speed are all
  `PER_CELL`-gated; **the entire C-battery is skipped at `PER_CELL=0`**, and the `unit`/`cell` digests
  differ wholesale. `PER_CELL=1` is the shipped default.
- "Phases 1+2 byte-identical" is true **by construction** — those phases are deliberately inert while
  unseeded. That is evidence about gating discipline, not about causal weight.

**The defensible claim is "cell-level *morale/rout state* is not yet load-bearing."** The recorded claim
is about "the cell layer" and is **false for the shipped engine** — and it is queued as a Jordan fork
that could redirect the architecture *against his own standing directive*, on evidence that cannot
distinguish "cells don't matter" from "cell-morale isn't wired yet". **Reword fork #5 before it is
ruled on.** Establishing it properly needs a real ablation matrix (`PER_CELL=0` vs `1`, and separately
per-cell facing frozen to subunit-uniform, at matched density and granularity, with C3 attribution) —
which does not exist.

## 13.4 — Live defects nobody claimed

- **Facing loss on drift, in the shipped config.** Three un-re-keyed maps are live at `PC_CELL_MORALE=0`:
  `cell_facing_vec`, `halted_cells`, `_speed_accum`. After drift, `cell_facing_vec` lookups on new ids
  fall through to `(advance_dir, 0)` defaults — **silently resetting the drifted body's committed
  facing**, a real current octagon-input distortion occurring ~125× per gauge battery. Unclaimed by any
  of the six auditors. **This is the one genuinely-current cell-map distortion, and it is not the one
  the plan advertised.**
- **Workbench concurrency (C5 hazard).** `server.py` serves trace requests on a `ThreadingHTTPServer`
  while `run_traced_battle` seeds the **process-global** RNG and toggles a **module-global** trace
  buffer — two concurrent requests interleave RNG streams and clear each other's trace mid-battle.
  C5 proposes promoting exactly this tool to "the standard diagnostic artifact". Fix before promoting.
  (`from trace import …` also shadows stdlib `trace` process-wide.)
- **S2.5's "zero enablers anywhere" for `reform_check` is false** — `validators.py` saves, sets and
  exercises `REFORM_CHECK_ENABLED` across 7 cases. B3's disposition must account for it.

## 13.5 — Net effect on the plan

**Re-ordered by measured severity:**

1. **A1a — repair the red shipped-mode goldens** (bisect #235/#236, re-record with per-mechanism delta). Unchanged as first task; now the *only* member of the old fact #1.
2. **A6a — repair the Lanchester harness** before wiring or arbitrating it (new; blocks A6 and fork #2).
3. **Casualty-realism 2/20 and the H4/H6 misses** — promote into the plan; currently absent.
4. **Facing-loss-on-drift** — the real current cell distortion; fold into B1c's justification.
5. A2, A3 — keep as hygiene with explicit *no-digest-movement* predictions; **demote from severity 1**.
6. **Reword fork #5** before it reaches Jordan.

**Standing lesson for the executing session.** Three of my five severity-1 findings were code-true but
**incidence-false**, and none of the six auditors nor I measured incidence before assigning severity.
**A defect's existence in source is not evidence of its rate.** Before labelling anything "changes
battles", instrument and count it — the wrappers used here are proven non-perturbing and cheap.
