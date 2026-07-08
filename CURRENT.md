# Valoria — Current Canonical Surface · **Generation v40**

> **Generation v40** = the consolidated, contracts-bound, Godot-ready generation: the v30 per-system
> flatten **+** universal Key substrate (PP-687) **+** contracts spine v3 (schema-2) **+** combat-engine
> ratification (ED-900–904) **+** descriptor registry **+** master-workplan v4 orchestration. "v40" is a
> *generation marker*, not a filename suffix — the `_v30` files remain (renaming 138 files / ~16k
> citations buys no clarity). Currency is carried here + by each head's `## Status:` line, enforced by
> `tools/ci_generation_consistency.py`.

**This is the single human-readable index of what is live.** When in doubt about whether a doc
is current, start here. Machine-readable source of truth: `references/canonical_sources.yaml`
(SHA-pinned) and `canon/mechanics_index.yaml`. Superseded exploration lives under `archives/`
and `deprecated/` — present for history, *not* canonical.

_Last reconciled: 2026-07-08 (**Pessimist subtractive-action audit RATIFIED** — Jordan "Please
ratify all", ED-IN-0027: `references/throughlines_meta.md` gains **§8.2-A** — the subtractive
disposition (KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT, judged as-if-built), the first *removal* verdict
the vetting framework has ever carried; the corpus docket's verdicts are filed as lane work-item EDs
ED-PC-0007/SC-0012/FA-0006/SE-0005/WR-0007/FI-0004 (decisions ratified, execution = per-lane
follow-ups); audit at `designs/audit/2026-07-08-pessimist-action-audit/`). Prior reconcile: 2026-07-07
(**Resolution-plan Stratum-A truth-reconciliation first pass** — the
doc/registry/ledger core executed: ED-FI-0003/ED-IN-0022/ED-IN-0023/ED-IN-0024/ED-IN-0025/ED-SE-0004/
ED-PC-0004 flipped `resolved`; ED-FA-0004/ED-WR-0005 doc-slice done with sim deferred to Stratum B;
CI-75→CI-100 + fork-2 doc propagation; ED-PC-0005 filed; see `resolution_plan_v1.md` §7. Prior
same-day: Key & Echo Armature v1 + unaddressed-areas audit, ED-IN-0017/0018,
consolidated ruling pass ED-IN-0026 — "ratify all" — RULED on the same branch/PR before merge:
OF-7/OF-B1 ADOPTED into `key_substrate_v30.md`/`propagation_spec_v1.md`, ED-IN-0012/0013 renumbered
to ED-IN-0019/0020, A15 process extension landed in `key_type_registry_v30.md` §10, first
executable Key substrate `sim/substrate/keys.py` shipped, `canonical_sources.yaml` re-synced via
`freshness_gate.py --update`; previous reconcile 2026-07-05 NERS qualitative audit RATIFIED, 12
lane EDs filed, MERGED PR #77; narrative-engine v1 + v2 "Churn Engine" designs + master workplan v6
+ steering reconciliation ED-IN-0006/ED-IN-0009 — roadmap_state retired to
`deprecated/references/`, v5 archived, decision queue snapshotted — PR #78; 2026-07-04
scene-combat R2 MERGED PR #72 + R3 plan-of-record RATIFIED; 2026-07-02 ED-1083 doctrine + ED-1093
propagation-spec + ED-1094 merge-ratifies convention; 2026-07-01 month-overview + architecture
consolidation; 2026-06-28 deprecation & currency sweep + v40 generation declaration). Every row is
the head of its lineage; predecessors are archived._

| Subsystem | Current head |
|---|---|
| **Personal combat** | `designs/scene/combat_engine_v1/` (resolver package; ED-900–904, re-ratified ED-904; D1–D9 ED-1029). **R2 closing-distance/facing/grip/contact redesign (I0–I8) MERGED to main (PR #72, 2026-07-04)** per `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md` (+ `i8_capstone_audit.md`). **R3 weapon-model consolidation — `designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md` (RATIFIED plan-of-record; U0→U9 + T-P2 + T5).** U0 (units honesty, ED-PC-0002) + **U1 (PoB recalibration, ED-PC-0010) DONE**. **JD-4 + JD-9 DETERMINED (ED-PC-0009, 2026-07-08)** at the formula level (`geometry.py` cut/thrust floor fixes; `weapon_physics.reversed_grip_percussion`, the HEMA-grounded Mordhau model) — live mode-selection wiring deferred pending a separate `core.coupling` fix (see `handoffs/HANDOFF_PC.md`). U2 (graded mode affordance) partially scoped; JD-2/3/5/6/7/8 remain open. Typed Class-C export: `references/engine_params/combat_engine_v1.json` — GENERATED from `config.py` via `tools/export_engine_params.py`, round-trip-checked blocking in CI (ED-1052 seed); the Godot port regenerates from it, never hand-edits |
| **Mass battle** | `designs/provincial/mass_battle_v30.md` (+ `mass_battle_integration_v30.md`) |
| **Social contest** | `designs/scene/social_contest_v30.md` (+ `_index`, `_infill`; `params/contest.md`) — ⚠️ a staged **contest_rebuild** is in flight (Gate 0 ratified 2026-06-30; reserved ED 1055–1079 / PP 800–809; **Stages 1a–3 / Gates A–C ratified through 2026-07-02, ED-1055–1062** — kernel at `sim/personal/contest/`; Stage 4 "four games" next). **2026-07-05: Fable 5 subsystem audit RATIFIED** (`designs/audit/2026-07-05-fable5-social-contest-audit/`, PR #80 + post-merge "Ratify all") — consequence-spine-first sequencing adopted (P0 → P1 ∥ P3-lite → Stage 4 → calibration); P0 decision docket **ED-SC-0002..0005 still awaits Jordan's picks** (blocks ED-SC-0007 + calibration). **2026-07-08: ED-SC-0006 (P1 consequence spine, part 1) EXECUTED** — `scene_dispatch.py` now routes the one live trigger (Stability Crisis → Emergency Council) to the promoted kernel (`build_contest`/`resolve_contest`), via a new `[SEED]` party-derivation bridge (`_emergency_council_parties`, derived from the SAME faction's own L/Sta aggregate stats — no invented actor); the kernel is no longer dead-in-campaign (new test in `sim/tests/test_mc_v18_regression.py`). ED-SC-0007 (outcome→domain-echo wiring) remains open, still blocked on the ED-SC-0002 keying fork; this row remains the head until a rebuild stage supersedes it |
| **Faction / political** | `designs/provincial/faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` + `faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`) — **+ `designs/provincial/faction_politics_v30.md`** (PP-660, CANONICAL, approved 2026-04-17; rank-ladder/Standing 0–7 progression, sub-office ladders, caste system) — indexed into this row 2026-07-08 (ED-IN-0016; C-FA-6 had flagged it orphaned from this row despite its own self-declared CANONICAL status) |
| **Settlement / territory** | `designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `designs/world/geography_v30.md`) — ⚠️ a **governance-play redesign** is in PROPOSAL (`designs/territory/governance_play_redesign_v1.md`, 2026-06-22; G1 prerequisite built: `sim/territory/registry.py` + tests). ED-SE-0001 ordered this tracking (ratified NERS audit, PR #77, 2026-07-05) until the first stage lands — executed 2026-07-07 (ED-SE-0004, OPT-16). |
| **Threadwork** | `designs/threadwork/threadwork_v30.md` (+ `thread_horizontal_integration_spec.md`) |
| **Fieldwork / Investigation** | `designs/scene/fieldwork_v30.md` (Status: DESIGN — approved for commit) + `designs/scene/investigation_systems_v30.md` (Status: CANONICAL, approved 2026-04-17) — new row 2026-07-08 (ED-IN-0016). The two docs carried a live EP-8 contradiction (fieldwork's bare-roll Interview vs. investigation's Dialogue Lattice, which asserts an "instead of" total replacement of the single-roll object) — **RESOLVED 2026-07-08 by ED-FI-0004 ("Interview MERGE")**: the Dialogue Lattice (`investigation_systems_v30` System 3 / S14) is now the single canonical Interview home; the fieldwork §4.2 bare-roll Interview object is annotated as superseded but retained as the current mechanical baseline pending the ED-921 schedule/attribute reconciliation. Retires ED-921 + the fieldwork half of ED-IN-0016/EP-8 |
| **Architecture / Key substrate** | `designs/architecture/key_substrate_v30.md` (+ `key_type_registry_v30.md`) — **2026-07-07: first executable substrate landed** (`sim/substrate/keys.py` — Key/KeyLog/TickScheduler, 25 tests) via the Key & Echo Armature v1 (`designs/architecture/key_echo_armature_v1.md`, ED-IN-0018, RATIFIED — consolidated ruling pass ED-IN-0026). §4.1 steps 4/5 amended per OF-7/OF-B1 (now RATIFIED, see the doc's own pointer note); `key_type_registry_v30.md` §10 gained the A15 rendering-disposition precondition + a header CANONICAL/PROVISIONAL split correction |
| **Architecture / Holonic doctrine** | `designs/architecture/holonic_container_doctrine_v1.md` — CANONICAL (ratified 2026-07-02, ED-1083/ED-1094); cross-maps the container/wrapper/propagation vocabulary onto module_contracts/sim-ladder/Key-substrate/Key-log-parity. Does NOT itself author the propagation-spec transform — see next row |
| **Architecture / Propagation spec** | `designs/architecture/propagation_spec_v1.md` — CANONICAL (ratified 2026-07-02, ED-1093/ED-1094; workplan v5 J-38). Ordering/determinism, aggregate-up, distribute-down, and termination (TERMINATION-ONLY — cross-tick convergence NOT proven) transforms; supplies `engine_clock`'s candidate home doc, but the `doc: null`/[ASSUMPTION] grade in `module_contracts.yaml` stays unflipped until ED-1051 is separately resolved. **2026-07-07: OF-7/OF-B1 RATIFIED** (consolidated ruling pass, ED-IN-0026 — §4.1 steps 4/5 amended; `sim/substrate/keys.py` defaults both flags ON). Remaining open flags tracked in the doc's own §5 (D.6/OF-D6, `decay()`, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) |
| **Scale transitions** | `designs/architecture/scale_transitions_v30.md` — CANONICAL; three-mode (TTRPG / Hybrid / Board Game) zoom in/out mode-bridge protocol, incl. the Mandatory Zoom In Triggers table (§4.3.2). New row 2026-07-08 (ED-IN-0016 — this connective-tissue doc had no CURRENT.md row) |
| **Player agency** | `designs/architecture/player_agency_v30.md` — CANONICAL (approved 2026-04-17); Scene Slate (§4), Standing/Duty/Conviction player-motivation architecture. New row 2026-07-08 (ED-IN-0016 — same missing-row gap as Scale transitions above) |
| **Articulation** | `designs/articulation/articulation_layer_v30.md` |
| **NPC behaviour** | `designs/npcs/npc_behavior_v30.md` |
| **Master workplan** | `designs/workplans/valoria_master_workplan_v6.md` (CANON — RATIFIED 2026-07-05, ED-IN-0009/ED-IN-0011; supersedes v5 → `archives/workplans/` with banner; v4 stays the frozen 06-11/06-22 record. North-Star milestones M1/M2/M3 + tiered decision register §5 — the live decision surface; progress board `workplan_v6_progress.yaml` + `valoria-workplan-navigator`) |
| **Narrative engine** | `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (RATIFIED 2026-07-05, ED-IN-0011 — Jordan sign-off incl. the F-F/fork-8 Light-Function decision at its default, subtract-only + weight-set-as-data; supersedes-in-part v1, which is ratified-as-amended with spec chapters s1–s5 + `spec/churn_amendments.md`. Executes ED-IN-0003/0004; stages sequenced in workplan v6 §3) |
| **Godot conversion** | `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md` (Lane-C governing spec) |
| **Board game** | `params/board_game.md` + `params/bg/*` governing tables |
| **Dice / resolution** | `params/core.md` + Decision-E continuous/quasi-binomial + d+σ resolver (canonized 2026-05-15) |

## Naming / versioning note

The `_v30` suffix marks the **current** generation of each subsystem — it is not a stale tag.
There is no blanket `v40` rename planned; a new version number is earned by the *next actual major
revision* of a system (e.g. a future combat-engine leap), not by find-and-replace. Keeping the
`_v30` names avoids churning ~136 co-filed pairs, hundreds of `v30 §x` citations, and every
`canonical_sha__*` pin.

See `designs/audit/2026-06-28-deprecation-currency-sweep/deprecation_currency_plan.md` for the
full sweep, the archive rationale, and what was deferred (combat-themed audit folders, pending the
active combat-engine work).
