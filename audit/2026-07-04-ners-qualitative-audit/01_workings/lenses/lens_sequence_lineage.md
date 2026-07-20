# Lens: sequence_lineage — working notes (2026-07-04)

## FORWARDS — does the build order sequence toward the Godot North Star?

Critical path to any playable multi-module Godot build (godot_conversion_strategy_v1.md Part VI):
- **Gate-0 blocking preconditions (VI.1), all UNEXECUTED:**
  - G0.1 Key schema v1→v2 migration (D1 = P1; "everything downstream consumes Keys", strategy line 195).
  - G0.2 reconcile three contradictory architecture docs (R3 = P1-legibility, line 197).
  - G0.4 Key-type registrations (scene.combat_resolved, scene.thread_operation) — must land *before* combat/thread ports emit.
- **engine_clock home doc = "unlocated [GAP]"** (strategy line 67; module row 8). It is the temporal spine "every system hangs off" (line 123). propagation_spec_v1 now supplies its *candidate* home doc (CURRENT.md L32) but module_contracts doc:null grade stays unflipped pending ED-1051.
- **Typed engine-params:** only combat has a generated typed export (`references/engine_params/combat_engine_v1.json`, round-trip CI). The other 26 modules are un-exported — CLAUDE.md §5 typed-params gap.
- **No named "playable-season" milestone** exists in any steering doc. The strategy sequences module ports (Part VI) but no surface defines a first end-to-end playable slice.

What is being polished OUT OF ORDER: personal combat (1/27 modules ported) received TWO more deep passes at/after the Gate-0 freeze — R2 closing-distance redesign MERGED 2026-07-04 (PR #72), R3 weapon-morphology consolidation in flight (PR #76), weapon-morphology granularity audit merged (PR #74). Meanwhile Gate-0 (Key v2, engine_clock, three-doc reconciliation) has not moved. The one ported slice is being deepened; the precondition that unblocks all other slices is frozen. (Charter calibration: Gate-0 unexecuted = KNOWN; new evidence = two more combat passes landed 07-02/07-04 against the frozen gate.)

### 3 highest-leverage next moves
1. **Execute Gate-0** (G0.1 Key v1→v2 migration + G0.2 three-doc reconciliation + G0.4 Key-type registrations) — the single blocking precondition to any module port beyond the combat slice.
2. **Author the engine_clock home doc** (flip module_contracts doc:null; propagation_spec_v1 already supplies the candidate transform) — the temporal spine 10/27 doc:null modules and the Accounting cadence hang off; ED-1051.
3. **Reconcile the steering surface + name a playable-season milestone**: repoint roadmap_state.yaml to live HEAD, flip workplan v5 §3 J-38 open→resolved, and define a first end-to-end playable slice no surface currently owns.

## BACKWARDS — head fidelity to ratifying lineage (5 supersession samples)

1. **combat_v30 (PARTIAL) → ED-900 / combat_engine_v1** (register L216-225). CURRENT.md head = combat_engine_v1. FAITHFUL.
2. **ED-912 Disposition/Knot ±5, supersedes PP-632/PP-684** (register L227-248). `files_to_recheck` lists `designs/scene/articulation_layer_v30.md §2.4` — **that path does not exist**; live head is `designs/articulation/articulation_layer_v30.md` (verified ls). The propagation checklist points at a moved/nonexistent file → a session honoring ED-912 cannot follow the register to the actual articulation head (which does read Bonds, §2.3/§2.4). STALE RECHECK PATH.
3. **VTM-STRIKE / CR-STRIKE 2026-04-19 (Varfell Cultural Reformation struck)** (register L37-66). victory_v30.md L103: "~~Cultural Reformation~~ STRUCK CR-STRIKE-2026-04-19. Varfell = military-only." FAITHFUL.
4. **godot implementation_sequence.md (PARTIAL) → conversion strategy Part VI** (register L193-203). CURRENT.md points at the strategy as the Lane-C governing spec. FAITHFUL.
5. **PP-687 EventImpact → Key.impact_vector** (register L67-78). key_substrate_v30 is the head (CURRENT.md L30). FAITHFUL.

4/5 faithful; ED-912 carries a stale recheck path.

**Register completeness gap (backwards):** the register is FROZEN at ED-912 / 2026-06-28. It contains NO entry for **GD-1** (per-faction victory + Partition co-victory strike — corroborates victory dossier: peninsular_strain_v30 §6.3 Partition still unmarked, invisible to the register), NO **mass-battle ED-MB / FIELD_MOVEMENT / PER_CELL** default-flips (corroborates registers_graphs no-back-propagation finding), and NO propagation-spec/contest-rebuild supersessions. Supersession authority stops ~1 week before HEAD.

## ONE STEERING SURFACE? — NO.

Four+ steering surfaces, only ONE fresh-and-authoritative:
- **CURRENT.md** — reconciled 2026-07-04, tracks R2/R3/propagation-spec. TRUSTWORTHY.
- **decision_queue.md** (month-overview) — 2026-07-02; item 18/J-38 marked "RATIFIED 2026-07-02 (ED-1093/1094), CANONICAL" (L75, L100-101). Fresh but scoped to that session.
- **workplan v5 §3 J-38** (L74) — still frames propagation-spec as an OPEN decision key that "lands as its own PROPOSED design doc." DIRECT CONTRADICTION with CURRENT.md + decision_queue (both = resolved/CANONICAL). §10 de-stales the doc only to `d80d364` (pre-07-01), so all 07-01→07-04 ratifications are unreconciled here.
- **roadmap_state.yaml** — `updated: 2026-06-28`, `current_phase: 2` "Document undocumented subsystems" items_done 0. Describes a MAY audit track wholly divorced from the live combat/contest/architecture work. Its own header (L10-11) declares stale roadmap "a defect of the same class as a stale session log." Self-indicted.
- **supersession_register.yaml** — frozen 2026-06-28 (above).

Concrete disagreement a session hits: "is propagation-spec authored?" → CURRENT.md/decision_queue say CANONICAL, workplan v5 says open-to-author. "Where are we?" → roadmap_state says Phase-2 doc-undocumented-subsystems; CURRENT.md says R3 combat + contest rebuild. A session bootstrapping from workplan v5 or roadmap_state alone builds on a stale premise — meta-legibility failure, resumed-from-stale risk. Only CURRENT.md's hand-reconciliation holds the surface together, exactly the single-point-of-truth fragility CLAUDE.md §1 already concedes.
