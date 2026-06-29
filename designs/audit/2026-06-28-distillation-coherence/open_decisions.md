<!-- STATUS: AUDIT — open decisions + deferred work from the 2026-06-28 distillation/coherence pass. Not canon. -->

# Distillation & Coherence — Open Decisions & Deferred Work
**Date:** 2026-06-28 · Companion to `distillation_coherence_report.md` + `verification_addendum.md`.

What the investigation + adversarial pass surfaced that was **not** applied in this PR, split into: (1) safe relabels deferred only because they need canon process; (2) design decisions only Jordan can make; (3) the multi-file structural programs. Letter tags reference the addendum.

## 0. Applied (PR #26 + the follow-up relabel PR)
- `strike_module.gd`: ER-2 continuity correction in `_degree()` (verified bug; ~5–9pp low below 5D). [RU-1]
- `module_contracts.yaml` bucket relabels track→clock: conviction scars, Thread Fatigue, knot strain, persuasion_track (bidirectional). [A4/BUCKET-1]
- `module_contracts.yaml` faction_state self-loop: "damper unconfirmed" → cite drift_coef=0.6 + 4-season counter + crisis-bypass. [LD-5]
- The verification addendum (incl. ESCP §D) + the report's verification pointer.

## 0b. Also applied (relabel PR)
- npc projects + arc-state buckets -> clock [A4]; resolver reclassifications (articulation->deterministic_accounting RU-4; scene_slate/game_director->manifest, scene_timer/audit observability RU-5); social_contest<->npc 2-cycle damper [LD-1]; settlement_economy retire-rec [LD-2]; faction_state=two docs [A6]; miraculous_event doc/scales [P6].

## 1. Still deferred (canon process or larger refactor — NOT design decisions)
- **KC-1 registry enum fix:** `key_type_registry_v30.md` — `default_permanence: structural → persistent`; `default_time_horizon: medium → near` (on `opinion_revised`/`gossip`/`concern_resolved`). **Do NOT delete `default_visibility`** (A9). Needs a registry supersession note + likely a co-file reconciliation (key_type_registry is Class-A governed). [KC-1]
- **Resolver-enum relabels** (`module_contracts.yaml`): `armature_dot_product`→`deterministic_accounting` + "interpretation primitive" note [RU-4]; `scene_slate` state_reader→manifest, `game_director`→manifest/orchestrator, `scene_timer`/`audit`→observability (out of runtime enum) [RU-5]; fold `dice_pool`+`d_sigma`→`instance_a` + render flag [RU-1]. Contract-internal but voluminous — batch as one adjudicator pass.
- **npc arc-state + projects** bucket track→clock [A4].
- **Dedup annotations:** settlement_economy retire-note; campaign_architecture — retire the *contract stub* (NOT the file; reconcile −4/−6 first, A10); `faction_state = {faction_layer_v30 + faction_behavior_v30}` (A6); miraculous_event `doc:null`→`designs/scene/miraculous_event_v30.md` + scales `[personal,settlement,peninsula]`, and resolve its CANONICAL-vs-PROVISIONAL header (P6).
- **social_contest `loops:[]`** → name the npc_behavior 2-cycle [LD-1].

## 2. Design decisions only Jordan can make (canon — not fabricated)
1. **CI threshold scheme (J-29):** 30/50/70 (clocks.md) vs 40/55/65/80/100 (registry/ci_political §2.1) vs 75 (conviction_track §3). MUST resolve before keying `mechanical.ci_milestone_crossed`. Defensible default: the registry 40/55/65/80/100.
2. **Instance-B resolver parameters** (BASE/SLOPE/FLOOR/CAP/offsets): form ratified (ED-874); numbers are `[OPEN — Jordan tuning]`.
3. **5th conviction axis:** resolve the "permitted" clause (key_substrate §2.4; matrix §4.1; taxonomy §2.2) to a firm **NO + Stage-10 gate**, on the +0.4 hierarchical-gap + symmetry rationale (NOT "Self-Other covers it" — orthogonal). Class-A clause in 3 docs → PP/ratification. [A12]
4. **`scene.thread_operation` vs `meta.thread_woven`:** likely collapse to thread_woven, but it partially reverses ED-935 → needs a Jordan supersession; confirm the failed/incomplete-operation path isn't dropped. [KC-4]
5. **Piety 3-way rename:** pick canonical names (personal conviction-scar vs territorial PT) + resolve the EXISTING "ruling pending" PT collision in `name_collision_database`; route via `alias_registry`, NOT `ci_naming_check`. Fix the "Piety Track offset" misuse in `fieldwork_v30` (not social_contest). [A5/P3]
6. **§9 settlement multipliers** (×50/×20) canonization — activates the inert `g_dv0` gate + the settlement half of the track↔derived couple. [A3/BUCKET-3]
7. **F2 stub payloads:** ratify the 4 genuine stubs (`thread_operation`, `draft_da`, `displacement`, `combat_resolved`) — DECISIONS.md item 29. [A7/KC-2]
8. **`env.crisis` source field:** add as **optional** (Class-B, avoids supersession) so consumers can tell authored vs mechanical crises. [P6]

## 3. Multi-file structural programs
- **#1 — Bus the zero-Key systems** (KC-5/LD-4/XS-1/ESCP-5): a `substrate_state` module owning MS + Key types `environmental.ms_delta` (batched at Accounting) / `environmental.ms_threshold_crossed` / `mechanical.ci_milestone_crossed` / `mechanical.theocracy_attempt` / `state.era_transition` / `settlement_event.*` + emit-wiring across territorial_piety, ci_political, victory, MS. Gated on J-29 (§2.1) + family-naming + Class-B vetting. Justify per-system: replay for the writers, observability for victory (A8). Key the **Founding Scene**, not the struck §5.2 RM gate (A11). Each keyed doc: "emitting Keys ≠ promotion to CANONICAL." **Highest-leverage move; 4 lenses converge on it.**
- **§12.3 targets[] discipline** (XS-2): populate sub-scale `targets[]`/`stat_deltas` on cross-scale emitters (the 8 down-seams + mass_battle `scene.battle_concluded` + the General-Duel bridge). Add the Lane-B lint ("for each Key type with registry-declared sub-scale consumers, validate ≥1 `target[]` at the consumer's scale").
- **ESCP-1:** reconcile the two Godot architectures — mark `scene_tree_architecture.md`'s manager-autoload pattern superseded by the BaseEngine+EngineModule skeleton (keep the UI scene tree).
- **ESCP-2:** author an `EngineManifest` `.tres` per runtime system, mirroring its `module_contracts.yaml` entry (the evolvability backbone).
- **ESCP-3:** decompose the threadwork + mass_battle + npc_behavior monoliths into BaseEngine + EngineModules.
- **B1:** record in `scale_transitions §12` the verdict "keep the 8 handoffs (adjudication layer)"; distill the empty §3.3; Key-bridge §3.7 by reusing `scene.combat_strike` + a duel flag.

**Sequence:** resolve the §2 decisions that gate structural work first (esp. J-29 and the piety/family naming), then the bus-fix (#1) as the highest-leverage program.
