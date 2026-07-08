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
| **Personal combat** | `designs/scene/combat_engine_v1/` (resolver package; ED-900–904, re-ratified ED-904; D1–D9 ED-1029). **R2 closing-distance/facing/grip/contact redesign (I0–I8) MERGED to main (PR #72, 2026-07-04)** per `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md` (+ `i8_capstone_audit.md`). **Next phase: R3 weapon-model consolidation — `designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md` (RATIFIED plan-of-record; U0→U9 + T-P2 + T5; JD-1…JD-8 open), implementing on PR #76.** Typed Class-C export: `references/engine_params/combat_engine_v1.json` — GENERATED from `config.py` via `tools/export_engine_params.py`, round-trip-checked blocking in CI (ED-1052 seed); the Godot port regenerates from it, never hand-edits |
| **Mass battle** | `designs/provincial/mass_battle_v30.md` (+ `mass_battle_integration_v30.md`) |
| **Social contest** | `designs/scene/social_contest_v30.md` (+ `_index`, `_infill`; `params/contest.md`) — ⚠️ a staged **contest_rebuild** is in flight (Gate 0 ratified 2026-06-30; reserved ED 1055–1079 / PP 800–809; **Stages 1a–3 / Gates A–C ratified through 2026-07-02, ED-1055–1062** — kernel at `sim/personal/contest/`; Stage 4 "four games" next). **2026-07-05: Fable 5 subsystem audit RATIFIED** (`designs/audit/2026-07-05-fable5-social-contest-audit/`, PR #80 + post-merge "Ratify all") — consequence-spine-first sequencing adopted (P0 → P1 ∥ P3-lite → Stage 4 → calibration); **ED-SC-0002 RULED (2026-07-08, composed keying)**; P0 docket **ED-SC-0003..0005 still await Jordan's picks** (ED-SC-0004 blocks calibration). **2026-07-08: the P1 consequence spine (ED-SC-0006/0007) is EXECUTED for the one live trigger** — `scene_dispatch.py` routes Stability Crisis → Emergency Council to the promoted kernel (`build_contest`/`resolve_contest`) via a `[SEED]` party-derivation bridge (`_emergency_council_parties`, derived from the SAME faction's own L/Sta aggregate stats — no invented actor), and its verdict now sets a Domain-Echo (Mandate channel, composed-keyed) that fires when `ECHO_TRANSPORT` is on (`sim/tests/test_mc_v18_regression.py`, `test_echo_transport.py`); the kernel is no longer dead-in-campaign and its outcome is no longer discarded. `parliamentary_vote`-in-the-loop is now wired for the **Censure tier only** (`sim/provincial/parliamentary_action.py`, ED-SC-0007 item 2, executed 2026-07-08 — see the Faction/political row); the other four Sanction tiers + constructive motions remain unbuilt. A P3-lite interactive Agôn harness (`sim/personal/contest/agon_harness.py`) also landed 2026-07-08. **⚠️ JORDAN RULING NEEDED: ED-SC-0013** — Total-Victory Mandate rider (−1) vs Censure target effect (−1) composing to −2 on one faction in one motion; implemented as stacking (literal default), not ratified. This row remains the head until a rebuild stage supersedes it |
| **Faction / political** | `designs/provincial/faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` + `faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`) — **2026-07-08: FA/SE historical-precedent research docket filed and partly EXECUTED same day** (`designs/audit/2026-07-08-fa-se-historical-precedent-research/`; 9 FA proposals + citation batch, `ED-FA-0007..0016`). **Executed:** Muster re-grounded as a fiscal-military purchase (ED-FA-0008); state-conditioned action-mix retiring the fixed 30/35/20/15 vector (ED-FA-0011); conquest Terms-vs-Storm fork, (a)/(b) only — Sack (c) still needs_jordan (ED-FA-0012); all 4 citation patches (ED-FA-0016); Parliamentary-Censure fallback wired into `faction_take_action` (see Social contest row). **Still PROPOSED-only:** Fiscal Stance (`faction_layer_v30` §5.9, ED-FA-0007) — no Treasury sim coupling yet |
| **Settlement / territory** | `designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `designs/world/geography_v30.md`) — ⚠️ a **governance-play redesign** is in PROPOSAL (`designs/territory/governance_play_redesign_v1.md`, 2026-06-22; G1 prerequisite built: `sim/territory/registry.py` + tests). ED-SE-0001 ordered this tracking (ratified NERS audit, PR #77, 2026-07-05) until the first stage lands — executed 2026-07-07 (ED-SE-0004, OPT-16). **2026-07-08: §1.8a Settlement-grain L/PS derivation events added (PROPOSED, ED-SE-0006)** — the report's top-priority distillation (Weberian traditional/legal-rational/charismatic typology → the L/PS split); 9 more SE proposals filed as `ED-SE-0007..0016`, **all authored into the doc as PROPOSED same day** (§1.8b/c succession+Exit, §3.3a charters, §4.3a/b dearth+grain routes, §5.3 Entry Terms — the last one partly LIVE via a dormant sim proxy read by `faction_action.py`'s ED-FA-0012 conquest fork; §7.1 CP-2 annotation). No SE-lane sim code yet beyond that one dormant proxy |
| **Threadwork** | `designs/threadwork/threadwork_v30.md` (+ `thread_horizontal_integration_spec.md`) |
| **Architecture / Key substrate** | `designs/architecture/key_substrate_v30.md` (+ `key_type_registry_v30.md`) — **2026-07-07: first executable substrate landed** (`sim/substrate/keys.py` — Key/KeyLog/TickScheduler, 25 tests) via the Key & Echo Armature v1 (`designs/architecture/key_echo_armature_v1.md`, ED-IN-0018, RATIFIED — consolidated ruling pass ED-IN-0026). §4.1 steps 4/5 amended per OF-7/OF-B1 (now RATIFIED, see the doc's own pointer note); `key_type_registry_v30.md` §10 gained the A15 rendering-disposition precondition + a header CANONICAL/PROVISIONAL split correction |
| **Architecture / Holonic doctrine** | `designs/architecture/holonic_container_doctrine_v1.md` — CANONICAL (ratified 2026-07-02, ED-1083/ED-1094); cross-maps the container/wrapper/propagation vocabulary onto module_contracts/sim-ladder/Key-substrate/Key-log-parity. Does NOT itself author the propagation-spec transform — see next row |
| **Architecture / Propagation spec** | `designs/architecture/propagation_spec_v1.md` — CANONICAL (ratified 2026-07-02, ED-1093/ED-1094; workplan v5 J-38). Ordering/determinism, aggregate-up, distribute-down, and termination (TERMINATION-ONLY — cross-tick convergence NOT proven) transforms; supplies `engine_clock`'s candidate home doc, but the `doc: null`/[ASSUMPTION] grade in `module_contracts.yaml` stays unflipped until ED-1051 is separately resolved. **2026-07-07: OF-7/OF-B1 RATIFIED** (consolidated ruling pass, ED-IN-0026 — §4.1 steps 4/5 amended; `sim/substrate/keys.py` defaults both flags ON). Remaining open flags tracked in the doc's own §5 (D.6/OF-D6, `decay()`, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) |
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
