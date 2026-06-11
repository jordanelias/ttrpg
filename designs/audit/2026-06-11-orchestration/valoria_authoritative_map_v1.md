# Valoria — Authoritative Map v1 (governance ⊗ canon ⊗ mechanics, one navigation surface)
**2026-06-11 · status: PROPOSED (Jordan-vetoable) · companion to `valoria_master_workplan_v4.md` (the register/docket) and `valoria_authoritative_graph_v1.md` (the edge layer)**

**What this is.** The single "where is everything, what is its status, which file is live" surface across all three layers of the project — governance, canon (metaphysics/world/characters/events), and mechanics (substrate/systems/modules) — synthesized from the full 2026-06-11 corpus. Per the corrected consolidation discipline (atlas R3): this is a **synthesis index over live sources, not a replacement** — every underlying artifact named in §1 stays authoritative for its own depth; status defects are tracked **once**, in workplan v4 §2 (rows cited here as `W#n`), never duplicated.

**as_of:** the 2026-06-11 upload corpus; underlying canon at the SHAs pinned in each source (`scale_transitions@17e75c6e` · `key_type_registry@19a69b89` · `key_substrate@3a4259e7` · contracts `c8e982b5` · game-flow `c005da27`/`6199d83a`). **Verified against live HEAD `d010fe27` at commit (2026-06-11): editorial ledger = 653 entries / 0 duplicate IDs; the v2 source layer (master · atlas · game-flow · flatten) confirmed committed. The two value flags below (CI 22v28; MS-start) remain OPEN — not resolved this session.**

`[SELF-AUTHORED — bias risk: synthesizes Claude-authored sources. Inherited-verdict and source-tier calibrations from atlas §7 apply throughout: loop-safety/NERS verdicts are inherited from the source audits (sims cited, not re-run); contract-derived rows are secondary to the primary-canon spine.]`

---

## §1 — DOCUMENT-AUTHORITY MAP (which file is live, for what)

**Rule of thumb:** designs/** canon bodies are the *what*; the 06-09→06-11 analysis layer is the *state of the what*; generated artifacts regenerate, never hand-merge (conflict-resolution #9).

| Domain | LIVE authority | Superseded / lagging | Notes |
|---|---|---|---|
| **Workplan** | `valoria_master_workplan_v4.md` (this orchestration; PROPOSED) | v3 (06-10, frozen on commit of v4) → R2 + 06-06 capstone (bannered) → delta (dead) | J-keys stable across versions |
| **Interdependency (graph layer)** | master v1 (v2-corrected) = navigable index · **atlas v1** = edge depth · `valoria_authoritative_graph_v1.md` = this orchestration's unified view | — (sources stay live per R3; nothing superseded) | the five source views (hierarchy/wiring/game-flow×2/verdict) remain authoritative detail |
| **Canon examination** | canon flatten **v2** (adversarially reconciled; same path supersedes v1) | flatten v1 (git history) | C-register lives in W4 §2 rows 7–14, 25–28 |
| **Temporal spec** | game-flow analysis + flat-spec **v2** (flat-spec = the live value-table reference, registries A–G) | v1 cuts (git history) | Step-6 Accounting; CI ≈S16; §H scorecard |
| **Personal-combat resolver** | `designs/scene/combat_engine_v1/` — **CANONICAL** (ED-900–904) | `combat_v30` **PARTIAL** (resolution only; lore retained — do NOT full-deprecate) · v31/v32 proposals DEPRECATED · `params/combat.md` → `deprecated/` | residual = W4 #17 / J-33 |
| **Faction resolver** | d+σ (ED-874, ratified) | bare-stat pools (dead) | propagation residual W4 #21 |
| **Mass battle** | live tick engine (`tests/sim/mass_battle/`, Instance A) = leading canon | design doc + params **LAGGING** (tri-strata drift, ED-899 FOLLOW-UP) | W4 #18 / J-9 |
| **Social contest** | L1 canonical (contradicted) + **CR1–CR7 = provisional canon-of-record** + groundup engine ratified-for-commit | — | the blocking work is propagation, not design — W4 #15 / J-31 |
| **Conversion (Lane C)** | `godot_conversion_strategy_v1.md` (`b42aa03`) with v3/v4-stated errata corrections authoritative until LC-0c folds them | `implementation_sequence.md` G1–G7 PARTIAL · `data_serialization_spec.md` FRAMING superseded | valoria-game repo frozen since 05-04 = refit target |
| **Module spine** | `references/module_contracts.yaml` v3 schema-2 → **generates** `module_map_flat.md` + 2 mermaids | v2.1-basis verdict numbers (re-run queued LB-5) | generated = regenerate, never hand-edit |
| **Editorial store** | `canon/editorial_ledger.jsonl` — 639 @06-09 (0 dup verified) → 653 @06-11 | YAML ledgers (deprecated/) | ★P1 struck; ED refs ledger-verified always |
| **Instrument health** | `canon/mechanics_index.yaml` usable; **`canonical_registry.md` = most-drifted instrument** ("Definitive" header unearned) | — | J-24 re-ratify-or-demote; seed-CI 22v28 lives here |
| **Roadmap** | 06-09 HTML — authoritative for ★P1 strike + lane state | stale at B.1 gate text (deprecations already executed); pre-dates J-keys | regen rides LB-3 / K-1 |
| **Arc corpus** | arc_expansion + throughline_resolutions (CANONICAL, with named staleness) | CP14 layer non-live per README — **except arcs_28_30, which canon/01 Am-5 binds and which fails it** (W4 #10 / J-25) | README itself misplaced (C14b → LA-16) |
| **Enforcement** | `valoria_hooks.py`/`github_ops.py` (code wins over spec) + `supersession_register.yaml` (17 entries) + deprecation map (legible companion) | M3/M4-hard never built (chat-side discipline) | LB-19 wires register into bootstrap fetch |

## §2 — GOVERNANCE SNAPSHOT (one paragraph each; detail in PI/architecture)

**Repos:** `jordanelias/ttrpg` (design truth + orchestration + hooks + index pipeline) · `jordanelias/valoria-game` (Godot 4.6 implementation; frozen 05-04, Lane-C refit target). **Lanes:** A canon/editorial (ED 890–939) · B infra, WIP=1 (940–969) · C sim/Godot (970–999); write-disjoint; the J-docket is the shared park-against register. **Enforcement reality:** Level-4 hooks live (safe_commit, task_gate, sim_gate, naming, co-file, size, collisions, rate-limit); M3 completeness and M4 citation-hard never built — chat-side discipline; commits to main land (B6 struck); CollisionError = re-fetch + retry. **Infrastructure roadmap:** Phases 0–2 done/≈done; 3–7 gated on Wave-3 decisions and the K-budget (K-1 report_open_items · K-2 freshness SHA-split · K-3 supersession vocabulary).

## §3 — CANON MAP (condensed; full flatten = canon flatten v2 §1–§4)

**Metaphysics spine (canon/00–02; all P-rule checks NULL-clean):** Threads = constitutive ground, three co-moving axes, Inseparability (P-01) → everything routes through co-movement. Ein Sof below the waterline (P-08 epistemological barrier → religious poetry is the *correct* register; the TS Gate makes Thread evidence invalid vs TS-0 interlocutors). Rendering by consciousness (P-03); Coherence = layer-2 integrity (P-10/P-15), orthogonal to TS (ED-301); the Leap opens a vulnerability window. Monstrosity ontological (P-02/04/05); Solmund = threadcut, third mode (P-06). Calamity = rendered-side over-draw (P-07; Lurianic frame canon **only** as RM self-understanding). Forgetting (P-13; TN8 check, TS-29 gate; permanent at Askeheim). Coherence-0 outcomes TS-banded (30–49 freefall → 90–100 Resonant); Critical band = designed 2–4-season Einhir replication; Rupture = legitimate ending ("the world becomes unintelligible"). GD-1 sole victory · GD-2 deterministic-first · GD-3 insurgency pipeline.

**World spine:** −12 AG Einhir Catastrophe → Solmund (−5→0, dissolution off-map) → Church catalyst (0–200) → Altonian colonial + Himmelenger grant → Secession (195–200) → deed-monarchy → **245 AG game start** (MS 72 · CI 22-or-28 ⚑W4-§0 · IP 20 · Strain 0). 17 territories, **15 playable** (T1–T14+T17); T15 Askeheim = the wound (Proximity 0, PT 0, Forgetting permanent); T16 off-board. Calamity radiation = Proximity(0–5) × MS-band lookup, dynamic. **218 AG backstory stands in canon/03 — the purported strike is unratified (C2 REVERSED → J-23).** One world track under four names (⚑ J-21). Clocks: CI (Seizure 60; declaration `((CI−60)/40)^3.3`; CI≥60→IP+2 = the central pacing valve; CI 100 forces Mass Seizure) · IP (tutoring 30 / prep 60 / Vanguard 75) · Strain 0–10 banded · PI (≥20 → Crown elimination) · per-territory Accord/PT/Prosperity/Fort/SW/Attention.

**Characters (anchors; framework = 13 Convictions × 4-axis matrix, Self-Other scalar, TS/Coherence/Spirit/Certainty):** Almud (TS 28, Manuel-Komnenos; Belief-2 sovereign constraint) · Lenneth (TS-ceiling SA-gated; archive date ⚑J-28) · Torben (emergence-window ED-609) · Himlensendt (sincere keystone; originary-Locks trigger) · Cardinals Jarnstal/Olafsson/Tormann/Klapp (⚑Klapp dual-state J-27) · Baralta (Henry-VIII/Isabella; pure RM adversary) · **Vaynard = Reinhardt-coded conqueror, ratified — scholar-collector arc layer un-struck (⚑LA-22)** · Ehrenwall (TS 0/Certainty 5; graduated autonomy replaces Coup Counter) · Edeyja/Orm (Warden anchors; Orm's death ≈ −7 seasons to Rupture) · Vossen/Hann (RM). Roster ~35 Active/30 Passive; relational graph PP-724 PROVISIONAL.

**Events:** settled past as timeline above; forward fuses = Royal Crisis card (S8+) · Altonian ladder (IP 30→60→75) · Generational Shift × autonomy × Crown Claim · Church schism cascade · GD-3 pipeline · Miraculous Events (SA escalator) · Southernmost cracking → ritual window ([NAME-PENDING ED-048]) · Longevity table (ED-567 open). Endgame: nine-condition STABLE ↔ zero-condition Einhir-recreation; arcs 28–30 = the binding-but-defective endgame trilogy (⚑J-25).

## §4 — MECHANICS MAP (the machine; modules in §5; edges in the graph doc)

**Substrate:** the Key — typed, validated, append-only; **emission is the only state-mutation path**; save = `initial_conditions + Key log`, replay deterministic; `causes[]` = provenance DAG. 37 registered types / 7 families (+7 unregistered ⚑J-2). Single-update rule `§4.1`: validate → append → compute_observers (scale-agnostic `§4.2`) → armature.interpret → memory → **apply_state_changes** → TYPE_SUBSCRIPTIONS consume → causal-graph edge. **Five resolver archetypes:** A dice-pool d10/TN7 (≡ continuous-Normal in videogame mode) · B **d+σ** `P = clamp(0.5+0.1·(stat−difficulty), .05, .90)` — every faction-stat action (ED-874) · C deterministic accounting · D clock-advance · E armature dot-product (cut-scene ≥ 0.40).

**Value taxonomy (classification dictates legal ops — conflation is the root drift class):** base stats 1–7 (Mandate **derived**, LPS-2e) · pools computed-never-stored (Combat `max(5,H+6)` · Argue `(P×2)+H+3+style` · Thread `(Spi×2)+H+TPS` · Mass `min(Size,Cmd)+Cmd`) · derived values never-written-directly (Treasury W×100 · Discipline Stab×10 · Reputation Inf×15 · Levies Mil×2 · Legitimacy Mand×20 — **live-verified exact**; personal block incl. Composure ×3-vs-+6 ⚑J-12) · tracks (bounded) vs clocks (monotonic). **Actors:** 13-Conviction vector → 13×4 matrix → armature 4-vector (derived, never authored); Self-Other scalar modulates attribution.

**Temporal spine (corrected):** init 7 steps (world 15T/35S/14P → factions → clocks MS 72·CI ⚑·IP 20·PI 7 → Tension ignition → chargen → tick). Season = S0 slate (8-step gen) → S1 personal (3–5 scenes; unpursued resolve by AI) → S2 strategic (GD-2 mandatories → 7-step stack; all d+σ) → INT zooms (BG never pauses, PP-110) → S4 cascade (Echo caps; depth 3) → **S5 Accounting, 10 steps strict** — clocks at Step 4 (clocks ONLY: CI seq → RS/MS → IP → PI), **Accord/Strain/battle at Step 6** (ED-678; peninsular_strain's "4c/4d/4e" = pre-consolidation labels) — → Step 10 victory check + season advance. Era transitions extend, never end. **Metronome (DERIVED):** CI 28→60 ≈ **S16 uncontested** (≈S19 if seed=22 ⚑); IP floor ~16 worst-case; MS Fragile ≈3–12 war-seasons; campaign ~12–25 seasons ≈ 50–100 scenes. Implementation order = dependency order: **Wave S spine → 1 deterministic → 2 provincial → 3 dice engines → 4 actors/read-side.**

## §5 — SYSTEM/MODULE STATUS TABLE (27 contracted modules; honest split ≈ 14 specified + 11 registry-shadow + 2 stubs)

| Scale | Module (impl / canon name) | Resolver | Conformance | System-depth verdict | Register |
|---|---|---|---|---|---|
| Personal | personal_combat (stub) ← combat_engine_v1 | A | STUB (correctly empty) | engine CANONICAL; 1v1 melee core COMPLIANT; **system NON-COMPLIANT** (coverage F1 + traditions F2 + seams F3/F4) | W4 #17 / J-33 |
| Personal | threadwork | A | NON-CONF (F2 type) | design NERS-compliant; **record-S FAIL** | W4 #16 / J-32 |
| Personal | fieldwork_knots | D+A | CONF (universal reader) | compliant; P1 line-split gates port | W4 #20 / LA-1 |
| Personal | piety_track / conviction_track | det | NON-CONF (A8, names) | collision cluster | W4 #6 / J-2·J-30 |
| Personal | npc_behavior · npc_memory · miraculous_event | E/C · state · state | NON-CONF ×4 F2 · thin · thin | observers of the stream; doc-12 §8 types unregistered | W4 #3/#4 |
| Scene | social_contest | A+D | CONF (clean) | architecture healthy (pools 5–18D, deep clock); **record non-compliant, repair ratified-unpropagated** | W4 #15 / J-31 |
| Scene | mass_battle | A in 7-phase | NON-CONF (naming) | **COMPLIANT-WITH-BACKLOG** (engine PASS; doc strata lag) | W4 #18 / J-9 |
| Scene | scene_slate · game_director · scene_timer · audit | state/clock | CONF/thin | shadow-doc set | W4 #4 |
| Settlement | settlement_layer · settlement_economy · territorial_piety | C | NON-CONF / dup? / isolated | aggregation math sound; quartet gates first port; Niflhel intra-doc row | W4 #19/#12 / J-19·J-34·J-5 |
| Provincial | faction_state / faction_layer | C (+B actions) | CONF | core fixed (d+σ, FSS-LOOP-1/2); inversion open; propagation debt | W4 #2/#21 / J-7 |
| Provincial | domain_actions / da_framework · faction_politics | B · det | NON-CONF (no doc; F2; A6 producer) | shadow + seam source | W4 #1/#4 |
| Provincial | ci_political · clock_registry · engine_clock | D+B · manifest · clock | CONF-isolated · CONF · thin | CI unkeyed (§10 candidate); registry PROVISIONAL flags | W4 #28 |
| Prov/Pen | victory | C (state-reader) | CONF-isolated | unwired (treaty.py ~157L); **GD-1 number contested** | W4 #7 / J-22→J-11 |
| Peninsula | peninsular_strain · scenario_authoring | D · manifest | NON-CONF (A6 down-producers; orphans) | shocks defined; delivery = J-1 | W4 #1 |
| Connective | articulation_layer | E | CONF (universal reader) | the Key-log→narrative bridge | — |
| Connective | campaign_architecture (stub) | — | STUB | reclassified consolidation doc; retirement recommended | ED-1006/1009 |

**Whole-graph NERS (inherited, ED-1009):** N mostly-held · **R FAIL** (7 unregistered types + 11 shadow docs + the missing direction) · S PARTIAL · E at-risk (collisions, shadow sprawl). **Safety set PASSES:** A7/A5/A1/J1 — incomplete, not unsafe.

## §6 — CANON↔MECHANICS INTERACTION SPINE (full table = flatten v2 §5)

P-01 → co-movement on every op (recovery included) · P-08 → Forgetting check / Seam-Text gate / TS Gate · P-10/15 → Coherence track + PP-261 zero-transition · P-13 → Askeheim permanence + expedition retention ladder · P-14 → cumulative band effects · Coherence-0 taxonomy → PP-261 + arcs 28–30 (defective, J-25) · GD-1 → victory_check (threshold ⚑J-22) · GD-2 → mandatory Govern/Muster (≤3; threshold intent ⚑J-19) · GD-3 → insurgency + parliamentary-eligibility gate · Calamity → Proximity×MS lookup, [THREAD] tags, no-echo (PP-532) · Solmund's works → miraculous_event (Mending Ob≥6, Prox≤2 → SA/Accord/Prox-mod; triple Church/Baralta/RM reading is the design) · caste → Viability Matrix (Niflhel row ⚑J-26) · `intent_of_game` → articulation + Domain Echo + zoom triggers (= loop L7, by design).

## §7 — HONESTY BLOCK

`[READ: bootstrapped + verified at HEAD d010fe27 this session — ledger 653/0-dup; v2 source layer (canon_flatten_examination.md · interdependency master/atlas · game-flow) confirmed committed.]` · `[GAP: the two §0 value flags (CI 22v28; MS-start referent, commit 2edf6432) remain OPEN — Jordan/investigation items, deliberately unresolved.]` · Inherited verdicts labelled (loop safety, NERS, sims). · `[CONFIDENCE: high]` on structure, status, and authority assignments (all corpus-cited); `[CONFIDENCE: medium]` only where the corpus itself flags it (seed CI; MS-start; C4a's "TC" reconstruction; C14e residual mapping).
