# Module-Adjudication Verdict — Full Graph

**2026-06-10 · `valoria-module-adjudicator` Stages 0–4 · scope: full graph (27 modules)**

`[SELF-AUTHORED — bias risk]` The skill, assessor, and contract registry under verdict were authored by earlier 2026-06-10 sessions. This file is read as external work; an independent-reviewer addendum is appended (§7).

Completes the staged run whose Stage-1 extraction, derived views, and ledger entries (ED-1005/1006/1007/1008) landed earlier today; this is the missing **Stage-3 capstone**. It introduces no new apparatus and appends nothing to the ledger — every finding below is already an OPEN entry.

- **Assessor:** `contract_adjudicator.py` A1–A12 over `references/module_contracts.yaml` v2.1 (commit 4c474c52). Re-run this session: **27 violations / 58 warnings**, matching ED-1008's recorded run.
- **Derived views (generated — never hand-edit):** `module_flowchart.mermaid` · `state_graph.mermaid` · `module_map_flat.md`.

---

## 1 · GRAPH VERDICT: **OPEN**

Closure is blocked by three structural classes — **none is an unsafe loop or a smooth-degradation defect.** All three are already ledgered OPEN for Jordan:

| # | Sev | Class | Count | Ledgered |
|---|---|---|---|---|
| 1 | P2 | **F2 — emitted Key type canon uses but registry never defined** (A2) | 7 | ED-1007 (4) + ED-1006 (3) |
| 2 | P2 | **Registry-derived module with no home design doc** (W-DOC) — root cause of the A6 cluster | 11 / 27 | ED-1006 |
| 3 | P3 | **A6 cross-scale seam — no canonical top-down Key-delivery rule** (provincial/peninsula → personal/scene/settlement) | 19 | ED-1006 |

Safety checks that **PASS** (the defects that would make a graph *dangerous* rather than *incomplete* are absent):
- **A7 loop annotation: PASS.** No cycle is undamped+unbounded. The one annotated cycle (settlement `Mandate ↔ Legitimacy/Popular Support`) carries its §1.8 saturating + mean-reverting damper (ED-1008).
- **A5 derived-write guard: PASS (0).** No `derived_value` is marked writable; aggregates route deltas to substrate (derived_stats §11).
- **A1 schema / stub-edge ban: PASS.** Both stubs (`personal_combat`, `campaign_architecture`) carry zero edges, as required.

The graph is **incomplete and under-specified, not unsafe.** Severity is dominated by missing registrations and missing docs, not by runaway dynamics.

---

## 2 · STAGE-2 JUDGMENT PASS (what the assessor cannot check)

**J1 — bucket fitness: PASS (null, examined).** Every owned quantity's bucket is canon-consistent. `threadwork.Coherence` is correctly `pool` (depleting, variable-cost); `peninsular_strain.Turmoil/IP` correctly `clock`; settlement `Local Economy / Garrison / Public Order` and `province Accord` correctly `derived_value` (non-writable); settlement `Legitimacy / Popular Support` as settlement-scale `track` is consistent with the holder-scoped canon-structure ruling (PI 2026-05-30). No track-that-is-really-a-clock, no stored-pool violation. `[NULL: J1 bucket fitness across 27 modules — examined, nothing found]`

**J2 — transition semantics: the decisive judgment.** The 19 A6 seams are *not* a simple "contract failed to cite an existing handoff." Reading `scale_transitions_v30` in full:
- **Bottom-up is canon-covered and safeguarded.** §5 Domain Echo delivers personal/scene outcomes up to faction stats with a hard **±2 cap**, one-Echo-per-scene-per-faction (PP-329), and queued-to-Accounting timing that explicitly prevents real-time BG manipulation (§5.3, PP-109). §5.5 (Accord), §5.4 (Piety→Mandate), §5.6 (Thread) instantiate it. This direction is sound.
- **Top-down has no Key-delivery rule.** §3's eight handoffs are mode/scale *bridges* (Personal↔Thread, Scene→Mass, Mass→Personal); §4 Zoom-In passes *modifiers* (DA degree → scene difficulty). Neither defines how a `da.*` / `state.*` / `env.*` Key *emitted at provincial/peninsula scale is delivered to a personal/scene/settlement consumer* through the single-update stream. The open question (ED-1006): is cross-scale delivery **engine-mediated and A6-exempt** (the substrate stream is scale-agnostic — any observer reads any appended Key), or does §3 need an explicit top-down delivery rule? **This is Jordan's to decide, and the A6 severity hinges on it** — if "exempt," 19 violations evaporate and A6 needs a scale-agnostic-stream carve-out (assessor is then the defect, per the script-subordinate-to-canon guardrail).

**J3 — necessity: PASS with two open redundancy candidates.** Orphan emissions (A4) are read by the universal readers `articulation_layer` / `fieldwork_knots` and feed emergent narrative — load-bearing under `intent_of_game`, not removal candidates. Two genuine NERS-N questions (over-coupling, not under-): `settlement_economy` vs `settlement_layer §1.3 Local Economy`, and `faction_politics` vs `faction_state` — possible duplicate systems, boundary unestablished `[OPEN — Jordan]`.

---

## 3 · PER-MODULE VERDICT (verdict-first, NON-CONFORMANT first)

| Module | Status | Resolver | Scale | Verdict | Findings → ledger |
|---|---|---|---|---|---|
| npc_behavior | extracted | det_accounting | personal·scene | **NON-CONFORMANT** | A2×4 F2 (project_advanced/completed/failed, displacement)→ED-1007; A6×8 consume→ED-1006; A4 orphans |
| domain_actions | extracted | d_sigma | provincial | **NON-CONFORMANT** | A2 `scene.draft_da`→ED-1006; A6 producer; no home doc→ED-1006 |
| faction_politics | extracted | det_accounting | provincial | **NON-CONFORMANT** | A6 producer (→npc ×4); no home doc; boundary vs faction_state `[OPEN]`→ED-1006 |
| scene_slate | extracted | state_reader | scene | **NON-CONFORMANT** | A6 producer (×6); no home doc (W-DOC)→ED-1006 |
| peninsular_strain | extracted | det_accounting | peninsula | **NON-CONFORMANT** | A6 producer (env.* down-scale); A4 `env.crisis`; transitions empty despite home doc |
| scenario_authoring | extracted | manifest | peninsula | **NON-CONFORMANT** | A6 producer (`env.disaster`); A4 orphan; no home doc; classification `[OPEN]` |
| settlement_layer | extracted | det_accounting | settlement·territory | **NON-CONFORMANT** | A6×3 consume (env.*); stale index (pre-LPS-2e)→ED-1006 |
| settlement_economy | extracted | det_accounting | settlement | **NON-CONFORMANT** | A6×2 consume; no home doc; duplicate-of-settlement_layer? `[OPEN]` |
| piety_track | extracted | det_accounting | personal | **NON-CONFORMANT** | A8 doc absent from canonical_sources→ED-1006; A6×6 consume; 3-way name collision→ED-1006 |
| threadwork | extracted | dice_pool | personal·thread | **NON-CONFORMANT** | A2 `scene.thread_operation`→ED-1006; A4 orphan; doc-status ambiguity `[OPEN]` |
| mass_battle | extracted | dice_pool | scene | **NON-CONFORMANT** | A2 `scene_outcome.battle_concluded` (naming drift)→ED-1006; A4 orphan |
| faction_state | extracted | det_accounting | provincial | CONFORMANT | clean A1–A12; A11-info Mandate/Treasury computed in settlement_layer (ED-1008); vocab-name `[OPEN]` |
| social_contest | extracted | dice_pool | scene | CONFORMANT | clean |
| fieldwork_knots | extracted | dice_pool | personal·scene | CONFORMANT | universal reader; scene.gift attribution cross-check; §11 contradictions `[OPEN, pre-existing]` |
| articulation_layer | extracted | armature_dot | personal·scene·provincial | CONFORMANT | universal reader; significance-fn / belief_revised emit not extracted (note) |
| clock_registry | extracted | manifest | provincial | CONFORMANT | pure manifest; PROVISIONAL staleness flags ED-793/4/5 |
| territorial_piety | extracted | det_accounting | territory·provincial | CONFORMANT — isolated | zero Key integration (canonical doc, no registry entry; §10 candidate)→ED-1006; name collision |
| ci_political | extracted | det_accounting | provincial | CONFORMANT — isolated | zero Key integration (CI=100 unkeyed; §10 candidate)→ED-1006 |
| victory | extracted | state_reader | provincial·peninsula | CONFORMANT — isolated | era-transitions unkeyed (§10 candidate)→ED-1006; doc DESIGN-not-canonical; stale index |
| engine_clock | extracted | clock_advance | provincial | CONFORMANT — thin | A4 `season_change` orphan; no home doc |
| npc_memory | extracted | state_reader | personal | CONFORMANT — thin | no home doc (W-DOC); grounded in doc-12 §2.3 |
| miraculous_event | extracted | state_reader | personal·scene | CONFORMANT — thin | no home doc; system-vs-event classification `[OPEN]` |
| game_director | extracted | state_reader | scene | CONFORMANT — thin | no home doc; scene.scene_entered attribution conflict |
| scene_timer | extracted | clock_advance | scene | CONFORMANT — thin | no home doc |
| audit | extracted | state_reader | scene | CONFORMANT — thin | no home doc; runtime-vs-QA classification `[OPEN]` |
| personal_combat | **stub** | — | personal | STUB (correctly empty) | F3: no `scene_outcome` type for personal combat; deferred to combat-engine ratification (owned by active handoff) |
| campaign_architecture | **stub** | — | provincial | STUB (correctly empty) | reclassified as consolidation doc, not runtime module; retirement recommended→ED-1006 |

**Tally:** 11 NON-CONFORMANT · 14 CONFORMANT (4 isolated-unintegrated, 5 thin/doc-gap, 5 clean) · 2 stubs.

---

## 4 · ALL-DIRECTIONS COVERAGE (`canon/definitions.yaml`)

- **lateral / horizontal (same-scale):** present — scene-internal (`scene_slate` → `social_contest` / `mass_battle`), provincial-internal (`faction_state` ↔ `domain_actions`). No gap flagged.
- **bottom-up (substrate → aggregate recompute):** **covered** — Domain Echo (§5) + Accounting recompute (province Accord = floor(mean(settlement Order)), AUD-SET-02). A5 guards the illegal inverse.
- **vertical (cross-scale):** **half-covered** — bottom-up yes (capped Domain Echo); **top-down absent** (the 19 A6 seams; no §3 Key-delivery rule).
- **top-down (aggregate → substrate reads):** the open delivery gap; pending the engine-mediated-vs-explicit-handoff ruling.
- **diagonal (cross-scale AND cross-family):** **absent** — `da.*` (provincial DA family) → personal `npc_behavior` is both cross-scale and cross-family; same A6 gap.

---

## 5 · NERS MAPPING

- **N — Necessary:** mostly held. Orphan emissions are necessary (articulation / `intent_of_game`). Two over-coupling candidates open: `settlement_economy`/`settlement_layer`, `faction_politics`/`faction_state` `[OPEN — Jordan]`.
- **R — Robust: FAIL.** 7 unregistered emitted types + 11/27 modules with no home doc + no top-down delivery rule ⇒ wiring is not "complete, error-free."
- **S — Smooth: PARTIAL.** Bottom-up scale machinery is coherent and safeguarded; top-down Key delivery is undefined; stale indices (`settlement_layer`, `victory`) and a malformed `scene.gossip` yaml block are friction.
- **E — Elegant: at risk.** The 3-way piety/conviction name collision and the registry-derived-without-doc sprawl are intuitability hazards; the contract apparatus itself is lean (no over-engineering).

A passing lint would be **necessary, not sufficient**, for NERS; behavioral compliance remains with `valoria-resolution-diagnostic`.

---

## 6 · STAGE 4 — ENFORCE & RE-TEST

**Re-test status: not runnable to violations = 0.** Every residual routes to a canon mechanism that is a Jordan-gated structural decision; the terminal state is `[OPEN — Jordan]`, exactly the skill's anticipated outcome. The verdict adds no apparatus, so it introduces no new A1–A12 defects (Stage-4 self-check clean).

Remediation routing (all OPEN, all already ledgered — no new appends):

| Finding | Owning canon mechanism | Decision | Ledger |
|---|---|---|---|
| F2 ×7 unregistered types | registry §10 Class-B extension, or strike from doc-12 §8 | Jordan | ED-1006 / ED-1007 |
| A6 top-down delivery gap | extend `scale_transitions` §3 with a top-down Key-delivery rule **OR** declare engine-mediated delivery A6-exempt (then assessor gains a scale-agnostic-stream carve-out + tests) | Jordan | ED-1006 |
| 11 undocumented modules | author home design docs, or ratify registry-derived-only status | Jordan | ED-1006 |
| 3-way piety/conviction name collision | naming resolution | Jordan | ED-1006 |
| A8 `conviction_track_v1` not in canonical_sources | declare in canonical_sources (mechanical, once collision resolved) | Jordan | ED-1006 |
| Unkeyed canonical systems (territorial_piety, ci_political, victory era-transitions) | registry §10 / Keys-migration | Jordan | ED-1006 |
| Stale indices + `scene.gossip` yaml + A9 37-vs-38 | tooling regen / count reconcile | mechanical | ED-1006 |

**Standing hook proposals** (per architecture `<migration_and_growth>` — proposed, *not built*; building requires tests + spectrum-table + PI updates in one change):
- Level-4 co-file: `key_type_registry_v30.md` ↔ `module_contracts.yaml` — a registry change without contract reconciliation (or vice versa) fails commit.
- Level-3 grep: emit-type literals in `designs/**` cross-checked against parsed registry `type_id`s (catches F2 at commit).
- Level-4: `contract_gate()` wrapping `adjudicate()` at `task_gate('design')` entry.

---

## 7 · INDEPENDENT-REVIEWER ADDENDUM (bias counterweight)

Surfacing what the authoring sessions are incentivized to under-weight:

1. **The 11 "extracted" doc-less modules may be dressed-up stubs.** The guardrail is "stubs stay empty"; these carry edges grounded *only* in the registry's emitting/consuming matrix, with no independent design doc. Counting them as `extracted` (not `stub`) inflates apparent graph coverage — 40% of the "verified" graph rests on a single source (the registry), not on system specs. An honest reading is that the engine has **~14 specified systems + ~11 registry-shadow systems + 2 stubs**, and the shadow systems are where the A6/F2 findings concentrate. Consider a third status (`registry_derived`) so the verdict does not overstate extraction.
2. **A6's 19 "violations" are conditional on an undecided model.** If Jordan rules the substrate stream scale-agnostic (the single-update rule already says *observers interpret → consume* without a scale predicate), these are false positives and the assessor over-fires. The verdict ranks them P3 precisely because their reality is contingent — do not treat the count as 19 confirmed defects until the delivery model is ruled.

---

## CITATIONS

- `skills/valoria-module-adjudicator/SKILL.md`
- `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py`
- `references/module_contracts.yaml` (v2.1, commit 4c474c52)
- `references/canonical_sources.yaml`
- `designs/architecture/scale_transitions_v30.md` (§1–§5, §7)
- `designs/architecture/key_type_registry_v30.md` (parsed by assessor; 38 `###` type headings vs §9-declared 37)
- `canon/02_canon_constraints.md`
- `canon/editorial_ledger.jsonl` (ED-1005, ED-1006, ED-1007, ED-1008)
- `designs/audit/2026-06-10-module-adjudication/module_map_flat.md`
