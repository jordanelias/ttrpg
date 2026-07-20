# Cluster C-STUB dossier

_Sonnet evidence cluster, read-only; archived verbatim by the Fable orchestrator (2026-07-07)._

## NotImplementedError census (file:line · module · purpose)

**Part A — the "Pass 2l armature stub" family + siblings: 19 distinct sim/ files** (matches the charter's "~19 sim NotImplementedError stubs" — confirmed by exact count, not the charter's own estimate). Each file's docstring names a canon source and a status tag; three flavors of tag appear (`Pass 2l armature stub` ×16, `Pass 3 follow-up stub` ×1, ad hoc ×2 — treaty.py, tribunal.py):

| # | file:line | module | purpose (from docstring) |
|---|---|---|---|
| 1 | `sim/cross_scale/articulation.py:24,28,32` | Articulation Layer (PP-688) | Tier-1 UI lens (`render_protagonist_lens`), Tier-2 triggers (`evaluate_articulation_triggers`), Tier-3 chronicle (`generate_chronicle_entry`) — canon source `designs/articulation/articulation_layer_v30.md` |
| 2 | `sim/provincial/varfell_mandate_action.py:31` | Varfell Mandate-gain action (placeholder-named, VARFELL-MANDATE-ACTION-001) | `attempt_mandate_action` — mechanism flagged broken by Jordan 2026-05-17 (double-cost asymmetry); name+mechanism both pending contamination audit |
| 3 | `sim/provincial/treaty.py:107` | Crown Treaties (`propose_treaty` only — `process_treaty_expirations` IS implemented) | generic non-Senator-Outward treaty formation path |
| 4 | `sim/provincial/charter_liberties.py:20` | Hafenmark Charter of Liberties | `attempt_charter` — canon source `faction_canon_v30.md` §6 |
| 5 | `sim/provincial/infrastructure_reclamation.py:21` | Church Infrastructure-Backed Reclamation | `compute_reclamation_bonus` — canon authoring itself still pending (Pass 2f) |
| 6 | `sim/peninsular/rs_track.py:21` | Rendering Stability world-track | `apply_rs_delta` — canon source `threadwork_v30.md` Part 5 |
| 7 | `sim/provincial/home_sanctuary.py:21,25` | Church T9 Home Sanctuary | `t9_invasion_modifier`, `check_sanctuary_active` |
| 8 | `sim/peninsular/ip_track.py:22,26` | Altonian Imperial Pressure world-track | `apply_ip_delta`, `check_phased_occupation_threshold` — canon source `peninsular_strain_v30.md` |
| 9 | `sim/personal/tribunal.py:149` | Asymmetric Proceedings, generic §7 dispatch (`run_tribunal`) | Succession Contest (§7.2) + Heresy Investigation Lifecycle (§7.3); the narrower `run_excommunication_tribunal` (§7.1) IS implemented |
| 10 | `sim/provincial/hafenmark_equipment.py:22` | Hafenmark faction equipment (Wagenburg + Bombards) | `apply_hafenmark_equipment` — canon doc not yet authored at all |
| 11 | `sim/provincial/altonian_reinforcements.py:21` | Hafenmark Altonian Reinforcements (choice-locked) | `invoke_altonian_reinforcements` |
| 12 | `sim/personal/investigation.py:23,27,31` | Investigation systems (NPE / Dialogue Lattice / Response Matrix) | `resolve_npe_response`, `evaluate_dialogue_lattice`, `apply_response_matrix` — canon source `investigation_systems_v30.md` |
| 13 | `sim/personal/companion.py:21` | Companion scene resolution | `run_companion_scene` — canon source `designs/godot/scene_tree_architecture.md` |
| 14 | `sim/personal/fieldwork.py:25,29,33` | Fieldwork (Exploration/Investigation/Socializing) | `run_fieldwork_scene`, `advance_disposition`, `advance_evidence` — canon source `fieldwork_v30.md` |
| 15 | `sim/provincial/varfell_territorial_acquisition.py:33` | Varfell territorial-acquisition (placeholder-named) | `attempt_territorial_acquisition` — mechanism v12c-validated (N=1000), identity wrapping pending audit |
| 16 | `sim/autoload/npc_ai.py:23,27` | NPC priority trees / faction AI dispatch | `select_action`, `evaluate_priority_stack` — priority-stack contents flagged possibly contaminated |
| 17 | `sim/world/miraculous_event.py:21` | Miraculous event resolution | `trigger_miraculous_event` — canon source `miraculous_event_v30.md` |
| 18 | `sim/world/restoration_movement.py:23,27` | Restoration Movement world-level PT decay/emergence | `process_rm_pt_decay`, `check_rm_emergence_trigger` — canon authoring pending Pass 2d |
| 19 | `sim/thread/rendering.py:22,26` | Rendering Stability world-track / Calamity (P-07) | `apply_rs_strain`, `check_calamity_threshold` — canon source `threadwork_v30.md` Part 5 |

**Provincial-scale subset:** files #2–5, #7, #10, #11, #15 (8 files, all under `sim/provincial/`) are exactly the "~8 provincial [actions]" the master workplan gestures at without enumerating (§3 Stage 2.5; narrative engine v2 line 163). This dossier is the first place they're named.

**Part B — contest-engine stubs (separate armature, NOT counted in the 19):**

| file:line | purpose |
|---|---|
| `sim/personal/contest/wrapper.py:199-204` | `_stub(game)` factory — registers `consensus`, `negotiation`, `inquiry` as `GAMES` router rows that raise; only `game='agon'` is WIRED |
| `sim/personal/contest/modes.py:328,331,334` | `DyadicMode.play`, `NegotiationMode.play`, `CeremonialMode.play` — "SCAFFOLD… separate sub-system — [to] build" |
| `sim/personal/contest/dictionaries.py:710` | `panel_win_condition` — raises only for `aggregation="unanimity_required"` — narrow, not a whole-module gap |
| `sim/personal/contest/resolver.py:51` | `WinCondition.resolve` — abstract base-class method, standard ABC pattern, not a content gap |

**Godot / other entry points:** no NotImplementedError stubs found under `designs/godot/` or `tools/` for fieldwork/investigation — `sim/personal/fieldwork.py` and `sim/personal/investigation.py` are the *only* fieldwork/investigation entry points anywhere in the corpus.

---

## doc:null census

| Module | Owns | gap_note | Candidate home |
|---|---|---|---|
| `npc_memory` | Memory store written from Keys, queried by NPC Procedures | "home doc unlocated — Memory schema lives in doc-12 §2.3 schema bridge; standalone spec [GAP]" | none — schema embedded in `political_dynamics_keys_migration_v30` §2.3, never promoted |
| `scene_slate` | Deterministic 7-priority slate generation | "home doc unlocated — referenced from `settlement_layer_v30` §4.1 and substrate §8.5; standalone doc [GAP]"; attribution conflict with `game_director` over `mechanical.scene_entered` | none; sim DOES have `sim/autoload/scene_slate.py` (implemented) — code outran the doc |
| `game_director` | Season-loop + zoom-stack orchestrator | "registry-derived; home doc unlocated [GAP]" | none; no `sim/` file implements it at all (not even a stub) |
| `scene_timer` | Wall-clock sidecar OUTSIDE the Key log (tooling) | "registry-derived; home doc unlocated [GAP]" | none; low-priority (observability only) |
| `audit` | QA/telemetry consumer of scene lifecycle Keys | "runtime-system vs QA-tooling classification [OPEN — Jordan]; home doc unlocated [GAP]" | none; low-priority (tooling) |
| `domain_actions` | `da_framework` — Domain Action resolution (all 5 DA types) | "home doc unlocated [GAP] — the DA resolver spec at `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md` is audit output, not a `designs/` home" | that spec, not yet promoted; **workplan §2 item 3: smallest doc:null closure, highest M1 leverage** |
| `settlement_economy` | (nominally) settlement-level economy | "relationship to `settlement_layer` §1.3 Local Economy unestablished [OPEN]"; **"RECOMMEND RETIRE… phantom module (no doc/state/logic)"** | none — the contract's own verdict is retirement, a different gap-class than the other nine |
| `engine_clock` | Season counter, `mechanical.accounting`/`mechanical.season_change` emission | "home doc unlocated [GAP]… propagation_spec_v1 supplies the candidate home; ED-1051 open, doc:null stays unflipped until then" | `propagation_spec_v1` — **the most directly workplan-cited doc:null (T0 row, ED-1051)** |
| `faction_politics` | Standing ladder, coup, succession | "boundary vs `faction_state` unestablished [OPEN]; home doc [GAP]" | **STALE flag** — `designs/provincial/faction_politics_v30.md` (PP-660, CANONICAL, 1,115 lines) already exists (KNOWN, ep-14). Separately: **zero `sim/` code anywhere implements coup/succession logic** — not even a stub file |
| `scenario_authoring` | Authoring-time event/scenario injection | "authoring-time vs runtime classification [OPEN — Jordan]; home doc [GAP]" | resolved as **fork 11**, RATIFIED 2026-07-05 (ED-IN-0011) — but `module_contracts.yaml` never updated; still doc:null / [ASSUMPTION] / "[OPEN — Jordan]" three days after ratification |

---

## [ASSUMPTION] resolver census

Grep-exact — every module whose `resolver:` line itself carries `[ASSUMPTION]`: **11 modules** — `faction_state` (L57, deterministic_accounting) · `npc_behavior` (L109) · `npc_memory` (L181, state_reader) · `piety_track` (L202) · `territorial_piety` (L241) · `domain_actions` (L474, d_sigma) · `peninsular_strain` (L498) · `settlement_economy` (L613) · `faction_politics` (L711) · `miraculous_event` (L731, state_reader) · `scenario_authoring` (L748, manifest).

Note: `engine_clock`'s `[ASSUMPTION]` (L696) sits on its `season counter` **state field**, not its `resolver:` line — excluded per the literal reading. Also excluded: `scene_slate`, `game_director`, `scene_timer`, `audit` — their resolver comments carry `[verification RU-5]` annotations, not `[ASSUMPTION]`.

---

## The stub × milestone map

| Item | Blocks | Workplan citation \| NOT-BLOCKING |
|---|---|---|
| `domain_actions` doc:null + resolver `[ASSUMPTION]` | **M1 junctures 1 & 2** | §2 item 3: "junctures 1–2 have no owning design doc… highest M1 leverage" |
| `engine_clock` doc:null | **M1 juncture 6** + GO-lane entry (M3 Gate-0) | §5 T0 row "ED-1051 — blocks juncture 6; GO entry"; §2 item 2 |
| contest wrapper STUB rows (consensus/negotiation/inquiry) + modes.py scaffolds | **M1 juncture 3** | §1 juncture 3 = "SC next stage (four deliberative games)" — 3 of 4 are exactly these stubs (stub fact KNOWN via PR #80; the juncture-3/M1 block citation is this dossier's addition) |
| `tribunal.py` `run_tribunal` (Succession/Heresy §7.2/7.3) | juncture-3 family via "Inquiry" | inferred link, not in §4-SC's text |
| `npc_ai`, `ip_track`, `rs_track` + 8 provincial stubs (11 files) | **Stage 2.5 Layer B only** — explicitly NOT M1 | §3 Stage 2.5 precondition set |
| `rs_track.py` + `thread/rendering.py` | Also juncture 5 via ED-WR-0002 | both use stale "RS" name; unenumerated "residual RS carriers" under ED-WR-0002's catch-all |
| `scenario_authoring` doc:null (fork 11) | Stage 1 compile home (M2 path) | §5 T1 row; RATIFIED at default but module_contracts not updated |
| `faction_politics` doc:null | tangential to juncture 1 | KNOWN (ep-14); deeper: zero sim code (new) |
| `articulation.py` (3 stubs) | reads like M1 juncture 7 but is NOT what juncture 7 cites | juncture 7 = narrative Stage 0 (ED-IN-0004), a separate newer pipeline; churn.md has zero mentions of articulation.py — an orphaned, superseded-in-spirit stub with no current owner |
| `investigation.py`, `fieldwork.py` (6 stubs) | feed FI evidence supply chain → juncture 3 input | indirect per workplan's own wording ("shapes theirs") |
| `companion.py`, `miraculous_event.py`, `restoration_movement.py` (5 stubs) | NOT-BLOCKING | no workplan citation anywhere; miraculous_event is C-INJ territory |
| `piety_track`/`territorial_piety`/`settlement_economy`/`peninsular_strain` [ASSUMPTION]s | NOT-BLOCKING M1 directly | settlement_economy carries its own RECOMMEND-RETIRE verdict |
| `npc_behavior`, `npc_memory`, `npc_ai` | **no lane owns NPC in workplan §4 at all** | §4 has no NPC lane section (PC/MB/SC/SE/WR/FI/FA/GO only) |

---

## Findings (C-STUB-1..7)

**C-STUB-1 · P2 · NEW · NOT-INTENDED** — the "~8 provincial" and "~19 sim stubs" the workplan cites by round number were never enumerated anywhere; this dossier is the first place they're named. Evidence: `narrative_engine_design_v2_churn.md:162-163`; workplan v6 §3 Stage 2.5.

**C-STUB-2 · P2 · NEW · UNDETERMINED** — "~19 sim stubs on Layer-B paths" over-claims: only 11 of 19 are plausibly Layer-B paths; the other 8 are personal/scene/world-track content stubs, some closer to M1 (fieldwork/investigation feed juncture 3's supply chain) — bundling risks silently deferring M1-adjacent stubs to "post-M1" by association.

**C-STUB-3 · P2 · NEW · NOT-INTENDED** — `domain_actions` closure is "highest M1 leverage" in workplan prose (§2 item 3) but absent from the formal §5 T0 register table (rows: F-F/fork-8, fork 1, fork 2, JD-1, ED-1051) — no pointer for the monthly reconcile to refresh.

**C-STUB-4 · P3 · NEW · UNDETERMINED** — fork 11 RATIFIED 2026-07-05 but `module_contracts.yaml` not updated in the same PR (still `[OPEN — Jordan]`); the merge-ratifies convention (CLAUDE.md §2) covers docs with `## Status:` lines, not machine-checked registries — a possible gap in the convention's own scope.

**C-STUB-5 · P3 · NEW · NOT-INTENDED** — `rs_track.py` and `thread/rendering.py` are unenumerated "residual RS carriers" under ED-WR-0002's catch-all; whoever implements them must do the MS rename in the same pass or reintroduce the stale name into new code.

**C-STUB-6 · P3 · NEW · NOT-INTENDED** — `faction_politics` has zero `sim/` code representation (not even a stub file) despite well-specified Keys in the registry — strictly deeper than any of the 19 counted stubs.

**C-STUB-7 · P3 · NEW · UNDETERMINED** — NPC-family modules (npc_behavior, npc_memory, npc_ai) have no owning lane in workplan v6 §4 at all, despite [ASSUMPTION] resolvers, doc:null, and a Stage-2.5 precondition among them.

---

## Honest gaps

- No sibling cluster dossiers existed on disk at time of writing — findings may partially converge with C-INJ/C-FI/C-NPC/C-SIG output and need Fable-stage reconciliation.
- PR #80's full KNOWN inventory not verified line-by-line — treat C-STUB-1..7 as provisionally NEW pending the non-duplication check.
- Map covers the M1/M2/M3 milestone structure only, not the full seam taxonomy of gap classes 2/3.
- `dictionaries.py:710` and `resolver.py:51` judged out-of-class for the milestone map (narrow branch / ABC pattern) — judgment call flagged.
- Did not open `spec/churn_amendments.md` or the full forecast-tractability dossier behind the Stage 2.5 citation.
