# Mass Battle — Loose-Ends Gather & Resolution (2026-06-20)

**Scope:** every open mass-battle loose end, gathered from all authoritative sources and driven to a terminal state.
**Frame:** ED-907's FM three-level command architecture — *army strategy/formation → sub-unit (troop type + subformation + tactic) → each cell inherits the best execution of that tactic* — confirmed verbatim by Jordan this session. That confirmation is the fidelity sign-off ED-907 invited; it is also the yardstick several findings below are measured against.

> **STATUS — EXECUTED 2026-06-20 (Jordan: "accept ratify resolve all").** All staged changes applied, ED-907 ratified, full decision surface resolved. Commits: ED-1032 engine fix `46373da8` · pool propagation `c82681dd` · ledger ratify/resolve `07fa954e`. §0–§6 below are the original triage; the executed state is **§8**.

## §0 — Disposition summary

| Bucket | Count | Items |
|---|---|---|
| **A. Closed since 06-09** (per-subunit chain + v4.x doc) — verified | 6 | MB4/MB7/MB9/stalemate/stratagem; per-subunit Disc/Morale/formation/rout; ED-905, ED-872, ED-909, ED-882 |
| **B. Filed now** (ledger hygiene, was staged/untracked) | 3 | ED-970, ED-971, ED-1032 (orphaning) |
| **C. Staged ready** (design-touching → Jordan green-light) | 2 | orphaning engine fix (validated); tri-strata doc §A.4 + params propagation |
| **D. Jordan decision** (surfaced + recommendation) | 7 | ED-875/G8; ED-907 ratification; orphaning-fix adoption; ED-907 unbuilt layers; reform/rally; PP-683/N1; docket J-9/J-10 |

No P1 findings. The resolution core remains NERS-compliant (06-09 verdict: COMPLIANT-WITH-BACKLOG); this pass empties the *hygiene* portion of that backlog and specifies the rest.

## §1 — Sources gathered (trail)

editorial ledger @ HEAD `57a6788de21b` (17 mass-battle entries; 16 resolved + ED-907 provisional) · 2026-06-09 comprehensive analysis (`designs/audit/2026-06-09-massbattle-comprehensive/massbattle_comprehensive_analysis.md` §7 F1–F12, §8 staged ED-970/971, §9 open-Jordan) · 2026-06-09 NERS verdict (same dir) · ED-907 / ED-899 / ED-875 / ED-905 / ED-872 / ED-909 full text · canon doc `designs/provincial/mass_battle_v30.md` §A.4 · `params/mass_combat.md` (v3) · `tests/coverage_matrix.md` · live engine (`tests/sim/mass_battle/`, local byte-exact copy) — TEST 1/2/3 this session · the 10-battle re-enactment + drift diagnostic this session.

## §2 — Register

### A. Closed since 2026-06-09 (verified, do not reopen)
The 05-28 mechanical defects (MB4/MB7/MB9, stalemate, stratagem) closed in canon. The per-sub-unit Discipline / Morale / formation / rout model landed and was canonized across **ED-1018→ED-1028** (doc v4.x). Adjacent EDs resolved/closed: **ED-905** (ratify 06-05 work), **ED-872** (pool floor = Size→0 deletion), **ED-909** (formation/subformation taxonomy + echelon), **ED-882** (MS band hysteresis — substrate layer, not mass-battle core; carries an unrelated MS=0 residual PST-1).

### B. Filed now — ledger hygiene (was staged or untracked)
The 06-09 audit staged two P2 candidates but did **not** append them (★ID-conflict counsel); both IDs are confirmed free at HEAD, so they are filed under their assigned IDs to preserve cross-references. The orphaning is new this session.

- **ED-970** [open · P2 · mass_battle/volley] — *ED-800 closed-but-unpropagated.* Jordan-decided Volley pool `min(Size,Power)+Power` (2026-05-11) is live in the engine; doc §A.4 / volley sections still teach the old framing. Doc-reconciliation only; no mechanic change. (Provenance: 06-09 analysis §8.)
- **ED-971** [open · P2 · mass_battle/fm_architecture] — *ED-910 grounded on an absent control surface.* The open recommendation against importing FM IP/OOP cited a per-turn control surface that does not exist in the engine; re-ground or amend it against ED-907 (which now supplies the canonical FM framing). (Provenance: 06-09 analysis §8.)
- **ED-1032** [open · P2 · mass_battle/spatial] — *Formation-drift cell orphaning* (see §4). Spatial-fidelity defect; HP/strength uncorrupted. Fix designed + validated; adoption pending Jordan (mechanics-touching).

### C. Staged ready — design-touching, awaiting Jordan green-light
- **Orphaning engine fix** — re-key `cell_troops` to the new shape's pattern on drift. Validated (§4). Mechanics-touching (alters drifting-unit footprint) → not committed unilaterally.
- **Tri-strata propagation (F3 / ED-899 FOLLOW-UP)** — exact doc §A.4 + params edits in §5. Propagation of an already-decided value; staged rather than committed because it is a canonical-doc mechanic edit warranting Jordan's eyes + the design-gate/re-pin flow.

### D. Jordan decisions — surfaced (consolidated in §6 with recommendations)
ED-875/Gate G8 (low-Command σ-leverage) · ED-907 ratification · orphaning-fix adoption · ED-907 unbuilt player-control layers · reform-unreachable + rally-unimplemented · PP-683 cap exception + N1 gate-vector manifest · docket J-9 / J-10.

## §3 — ED-907 implementation map (FM three-level architecture vs engine)

| ED-907 element | Engine state | Status |
|---|---|---|
| L1 Aggression {Cautious/Balanced/Pressing} | `stance` aggressive/balanced/hold + `STANCE_SPEED_MOD` | **present** (3-way, terms differ) |
| L1 Cohesion-priority {Hold shape / Adapt} | — formations *always* adapt (drift to Line); no hold-shape path | **absent** |
| L2 Unit formation — allocation grid (set intent → auto-distribute, per-cell override) | — formations built directly via `of_type`; no allocation surface | **absent** (videogame-UI/future) |
| L2/3 formation geometry | `CELL_PATTERN_FN`, `_oriented`, `MIN_DISCIPLINE` | **present** |
| L3 role / subformation | `TROOP_TYPE_ROLES`, `order_target_idx`, `target_condition`, `roles_for` | **present** |
| cell inherits tactic execution | `eff_discipline`, `advance_cells`, `cells()`, `check_drift` | **present but defective** (orphaning, §4) |
| instructions / brace | `instructions`, `brace` | **present** |
| intervention-window cadence (~5–20/battle) | — no such control loop | **absent** (player-control/future) |
| "mentality" term | — engine uses `stance` | n/a (terminology) |

**Reading:** the *resolution* half of ED-907 is realized; the *player-control* half (allocation grid, cohesion-priority axis, intervention windows) is unbuilt and is videogame-UI/future work, not a defect. The one defect inside the realized half is the orphaning.

## §4 — Orphaning defect: diagnosis + validated fix

**Empirical (TEST 1, single Arrowhead sub-unit, Disc 3 → drifts at the phase boundary):**
`sum(cell_troops.values())` equals unit HP at every tick, before and after drift (376==376, 321==321 through casualties) — **strength and combat pool are correct**. But at the drift tick, the spatial view diverges by a constant **157.4 / 376 ≈ 42%**:

```
 t5  Arrowhead  hp=388.0  allcells=388.0  iter_cells=388.0  orphan=  0.0
 t6  Line       hp=376.0  allcells=376.0  iter_cells=218.6  orphan=157.4
 t12 Line       hp=321.0  allcells=321.0  iter_cells=163.7  orphan=157.4   (constant)
```

**Root cause:** `cell_troops` is keyed by `(orig_r, orig_c)` of the *spawn* shape's pattern. `Unit.check_drift` (orchestration L1367) does a bare `a.shape = "Line"` with no re-keying. `iter_cells`/`cells()` walk `_oriented(self)` for the *current* (Line) shape; only the ~58% of cell-ids shared between the Arrowhead and Line patterns match the dict, so the Arrowhead-only wing entries stay in `cell_troops` (counted in HP and `troop_total`) but are never yielded — invisible on the grid **and** inert: front-cell casualty distribution operates on `iter_cells`, so the orphaned wing never takes casualties, occupies no frontage, and cannot be enveloped. The unit fights at full HP-driven strength behind a phantom-narrow footprint.

**Severity: P2 spatial-fidelity.** No HP corruption (the invariant `sum(cell_troops)==hp` holds); outcomes are approximately right because the pool is HP-driven. What is wrong is the spatial layer — exactly the layer the cell model and ED-907's "each cell inherits the best execution" exist to make faithful.

**Fix (validated this session)** — on drift, re-key to the new shape's pattern, mirroring spawn:

```python
def check_drift(self):
    for a in self.subunits:
        if a.eff_discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
            total = sum(a.cell_troops.values())                 # preserve strength
            a.shape = "Line"
            new_ids = [(o_r, o_c) for o_r, o_c, _x, _y in _oriented(a)]   # Line pattern
            per = total / len(new_ids) if new_ids else 0.0
            a.cell_troops = {pid: per for pid in new_ids}        # re-key + redistribute
```

Validation (same scenario, patched): post-drift **orphan → 0**, HP preserved (357.8 = sum(cells) = iter_cells_sum), full 25-cell Line complement restored.

**Honest mechanical caveat (why this is Jordan's call, not a silent bugfix):** the fix is byte-exact for any battle with no drift (the loop body never executes). For a unit that *does* drift it changes the post-drift spatial footprint — casualties now spread over the full re-keyed Line instead of the shared spine — so drifting-unit dynamics and the byte-exact digest change; the engine SHA would need re-pinning after adoption. This is the intended correction (the orphan removal *is* a behavior change), but it alters outcomes, so it is presented for adoption rather than committed.

**Decision options:** (a) **re-key/redistribute** (recommended — matches ED-907's inheritance principle and Jordan's restatement); (b) keep orphaning (status quo — spatially wrong); (c) treat drift as no cell-count reduction (Line at original width without the formation bonus — a different model). Recommend (a).

## §5 — Tri-strata propagation (F3 / ED-899 FOLLOW-UP) — exact edits, ready

The doc was updated to the per-sub-unit model this session, but the **pool formula** was not propagated, and params still sits at the v3 era. The doc already flags the legacy formula as OFF-path but never states the live value.

**Doc `designs/provincial/mass_battle_v30.md`:**
- L28 `**Effective Combat Pool = min(Size, Command) + Command** (PP-233)` → add the live value: `**Effective Combat Pool = Command × (1 + cohesion)** — 2×Command at full strength, decaying to Command at annihilation (cohesion = current_strength ÷ max_strength). [canonical: resolution.py base_combat_pool, COMMAND_SIGMA path; ED-899 (Jordan 2026-06-02), ED-1013 (smooth cohesion pool)]`, retaining the `min(Size,Command)+Command` line marked LEGACY/OFF-path.
- L433 (Phase-3 worked formula) — same substitution.
- Add ED-1013 to the §A.4 citation list (currently cites ED-899 only).

**Params `params/mass_combat.md`** — prepend a supersession banner: this file predates the per-sub-unit + cohesion-pool resolution; the PP-233 `min(Size,Command)+Command` pool (×5 in-file) is OFF-path (live pool = Command×(1+cohesion), ED-899/ED-1013); Discipline/Morale/formation-drift are now per-sub-unit (ED-1018→1028, doc v4.x §A.5/§A.6/§A.12); canonical mechanics-on-paper = the v4.x doc; treat sections below as historical unless confirmed against it.

Both are propagation of decided values; applying them requires the design-gate + canonical_sources re-pin. Held for Jordan's trigger.

## §6 — Jordan-decision surface (consolidated, with recommendations)

1. **ED-875 / Gate G8 — low-Command σ-leverage** [open]. Command σ-leverage is high at low Command under the COMMAND_SIGMA path. Genuine open gate. *Recommendation:* decide whether the high low-end leverage is intended (it rewards command quality steeply where it is scarcest) or should be dampened; bring the σ-sweep data to the call.
2. **ED-907 ratification.** Fidelity confirmed by Jordan this session (the FM restatement matches the filing). *Recommendation:* flip provisional → resolved; record this session's confirmation as provenance.
3. **Orphaning-fix adoption** (§4) — re-key vs orphan vs no-reduction. *Recommendation:* re-key (option a).
4. **ED-907 unbuilt player-control layers** — Cohesion-priority {Hold shape/Adapt}, the allocation grid, intervention-window cadence. *Recommendation:* confirm these are deferred videogame-UI/future, not current gaps (the resolution engine does not need them). Note: implementing the Hold-shape axis is the principled way to make formation drift player-conditioned rather than always-on.
5. **Reform unreachable in-engagement (F10) + rally unimplemented.** `reform_check` carries real §A.5/§A.7 logic but fires only for non-engaged units, so it never triggers mid-engagement (units in a sustained clash are always in contact); `rally_check` is an empty stub (deferred to cycle G-7). *Recommendation:* confirm reform-between-turns-only is intended, and that rally is a known future item — likely both intended/deferred, not bugs.
6. **PP-683 cap exception unwired; N1 (no canonical gate-vector manifest).** Minor. *Recommendation:* wire PP-683 or strike it; optionally add a one-page gate manifest (G8 etc.) for legibility.
7. **Docket J-9 (mass-battle canon set) / J-10 (weapon-physics constants).** The workplan v4 was never committed (corpus-only). J-9 is largely subsumed by the v4.x canon + this resolution. J-10 (weapon-physics constants) is a separate workstream with its own thread (2026-06-13 combat bottom-up; weapon-physics-stage2 handoff). *Recommendation:* close J-9 into this resolution; route J-10 to the weapon-physics thread.

## §7 — Confidence & limits

[CONFIDENCE: high] on everything cited to read source + the engine tests run this session (§3 map, §4 orphaning + fix, the ledger/verdict status). [CONFIDENCE: medium] on the run-to-run *outcome* deltas of the orphaning fix — the engine is stochastic, so the validation establishes the invariant (orphan→0, HP preserved) rather than a tick-matched outcome diff. The F4–F9/F11–F12 findings from the 06-09 analysis were not re-walked individually this pass; they were P3/below and the 06-09 verdict folded them into the backlog already characterized here. No P1 surfaced. All design-touching changes (§4, §5) are Jordan-vetoable and held for sign-off.

---

## §8 — EXECUTION RECORD (2026-06-20 · Jordan: "accept ratify resolve all")

All staged changes applied, ED-907 ratified, decision surface resolved. Commits (jordanelias/ttrpg, main):

**Stage A — orphaning fix (ED-1032), `46373da8`.** Re-key `cell_troops` to the new shape's pattern on drift in `orchestration.py` `check_drift` (mirrors spawn L629). Validated: stress S1-S18 PASS, drifted-unit orphan->0, HP preserved. Gauge digest fe995746->1f8c05a9 (first change since the per-subunit baseline; drift-only, non-drift identical). coverage_matrix co-filed; engine is not freshness-pinned (no re-pin).

**Stage B - tri-strata pool propagation, `c82681dd` (atomic, with re-pin).** Doc §A.4 (L30 banner + L433) and the params ED-899 banner now state the live exchange pool `Command*(1+cohesion)` = 2*Command full strength -> Command at annihilation (was flat 2*Command, ED-899 only). Closes the ED-1013 doc-lag. canonical_sources re-pinned for doc + params (params was independently stale-pinned, also fixed).
  - *Volley pool - finding corrected, not propagated.* Bottom-up read (`resolution.py` volley_phase/_roll_volley_pool) shows volley is **Power-based** (`max(1, eff_power - disc_pen)`, PP-503), matching the doc's ED-753. **No** volley doc-lag; F1/ED-970's "ED-800 min(Size,Power)+Power" claim is not borne out and is struck. Verifying bottom-up prevented injecting a wrong formula into canon.

**Stage C - ledger ratify/resolve, `07fa954e`.** ED-907 **ratified** (Jordan fidelity-confirmed; player-control layers deferred-UI). Resolved: ED-1032, ED-970 (corrected), ED-971 + ED-910 (FM IP/OOP re-grounded on the structural disanalogy, not adopted - the adopted FM analogy is ED-907's command hierarchy), ED-875/G8.

**Gate G8 / ED-875 - resolved (mechanical-tier, Jordan-vetoable).** Keep the high low-Command sigma-leverage as intended. Bottom-up: COMMAND_SIGMA pool = Command*(1+cohesion), so +1 Command is relatively larger at low Command (2->3 ~ +33% base vs 6->7 ~ +14%) - command quality matters most where scarce. Top-down anchor: generalship's outsized effect on small/poorly-led forces; acclaimed strategy designs (Total War, Field of Glory) make leadership leverage high for small/elite units. Model unchanged; precision retune, if wanted, needs a sigma-sweep (out of scope).

**Design-status confirmations.**
- ED-907 player-control layers (Cohesion-priority {Hold-shape/Adapt}, allocation grid, intervention windows): **deferred** videogame-UI/future, not current gaps. Implementing Hold-shape is the principled way to make drift player-conditioned when that UI is built.
- Reform/rally: reform_check is real §A.5/§A.7 logic but unreachable in-engagement (sustained clash = always in contact) -> **reform-between-turns-only is intended**; rally_check is an empty stub -> **rally deferred to cycle G-7**.

**Residuals (minor, noted).**
- PP-683 encirclement cap exception: documented (doc L208), engine-wiring unverified - verify/wire-or-strike in a focused follow-up.
- Engine comment lag: `base_combat_pool`'s top `[canonical:]` comment still cites the legacy `min(Size,Command)+Command`; behavior is correct and its §A.4 pointer now resolves to the corrected value. Cosmetic; sweep when next editing the file.
- Docket J-9 (mass-battle canon set): **folded into this resolution**. J-10 (weapon-physics constants): separate workstream -> route to the 2026-06-13 combat bottom-up / weapon-physics thread.

Net: the mass-battle backlog holds no open items except the two minor residuals and the J-10 hand-off. NERS posture unchanged (COMPLIANT); the S=PARTIAL tri-strata flag is closed for the exchange pool.
