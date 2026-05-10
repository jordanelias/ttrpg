<!-- v30 path update applied 2026-04-13 -->
# VALORIA PROPAGATION MAP
## 2026-05-02 — Mandate audit resolution + Phase B trigger ruleset finalized (ED-784, ED-785)

**ED-784 (P1, closed) — Mandate audit Q1-Q5 resolved.** Jordan signoff 2026-05-02.

| Q | Resolution |
|---|---|
| Q1 Submission threshold | PS = 0 |
| Q2 PP-189 Institutional Mandate | L only |
| Q3 Failure-clause Church gain | L only |
| Q4 personal_mandate_view | `round((L+PS)/2)` (already in factions_personal.md per PP-686 v2) |
| Q5 Mandate≥4 gates | per-mechanic (Crown Policy L≥4, populist DAs PS≥4, deviation-cost gates strictness) |

Resolution log: `designs/audit/2026-05-01-stage-10-validation/03_mandate_consumer_audit.md` §5b.

**Phase 2 mechanical sweep queued (separate commit):** 9 consumer files + 8 reference files. Includes Ethical Framework Modifiers strike in `params/factions/stats_1_7_scale.md` (bg/core.md strike already applied).

**ED-785 (P2, closed) — Phase B trigger ruleset finalized.**

- Trigger #9 (cross-faction clustering): threshold |sim| > 0.7 → > 0.40 per Stage 10 §3.6 / A6 evidence.
- Trigger #10 (state.belief_revised) ADDED: tracked NPC fires Tier 2 cut scene directly. Closes Stage 10 §4.1 finding.

Total triggers in articulation §3.1: 10. Stage 8c calibration sweep (Phase 5a) refines further.

**Files touched this commit:**
- `designs/audit/2026-05-01-stage-10-validation/03_mandate_consumer_audit.md` (§5b RESOLVED, §6/§7 updated)
- `designs/articulation/articulation_layer_v30.md` (§3.1 — header, table, threshold, trigger 10 spec)
- `canon/editorial_ledger.yaml` (ED-784, ED-785 added; next_id 784 → 786)
- `references/propagation_map.md` (this section)

**Cross-references:** PP-688 (articulation layer canonical), Stage 10 articulation sim, Stage 8b/c sims, Mandate-consumer audit 2026-05-01.

---

## 2026-05-02 — Register cap revision + chunking sweep (ED-786)

**Trigger:** Three register files at >97% of cap during 2026-05-02 session forced ED-783 emergency archival mid-work. Caps were under-budgeted relative to actual work pace (2-3 commits/session, 800-1200 char ED entries, linear growth in canonical_sources with each new design doc).

**Cap raises** (`skills/valoria-orchestrator/scripts/github_ops.py` `TOKEN_THRESHOLDS`):

| File | Old | New | % raise |
|---|---:|---:|---:|
| `canon/editorial_ledger.yaml` | 2,000 | 4,000 | +100% |
| `canon/editorial_ledger_summary.yaml` | 1,000 | 2,000 | +100% |
| `references/file_index_summary.md` | 1,000 | 2,000 | +100% |
| `references/canonical_sources.yaml` | 5,000 | 8,000 | +60% |
| `tests/coverage_matrix.md` | 5,000 | 8,000 | +60% |
| `canon/patch_register_active.yaml` | 15,000 | 18,000 | +20% |

Unchanged: `session_log_current.md` (2k — session-bounded, rotates), `propagation_map.md` (15k — fine), `arc_register.md` (20k — huge headroom), `design_registry.yaml` (8k — 41% used), `valoria-orchestrator/SKILL.md` (8k).

**Chunking actions** (this commit):

- `canon/editorial_ledger.yaml`: 4 closed entries (ED-782, ED-783, ED-784, ED-785) → `archives/editorial/editorial_ledger_archive_2026_05_02_b.yaml`. Active 1,968 → 1,107 tokens (now 28% of new 4k cap).
- `tests/coverage_matrix.md`: All historical sim batches 2026-04-17 to 2026-04-19 → `tests/coverage_matrix_archive_2026_04_19.md`. Open Findings table pruned to unresolved-only (resolved rows still traceable via ED refs in archive). Active 4,983 → 358 tokens (now 4% of new 8k cap).
- `references/canonical_sources.yaml`: All 7 remaining `# Last touched: ...` breadcrumb comments stripped (continuing 2026-05-02-a sweep). Editorial history now exclusively traced via ED entries + propagation_log. Active 4,333 → 4,130 tokens (now 52% of new 8k cap).

**Not chunked** (deliberate):

- `canonical_sources.yaml`: structural split by domain (personal/provincial/meta) considered but rejected — every consumer (sim_gate, audit hooks) reads this file; refactor blast radius too large for marginal benefit once cap raised to 8k. Revisit if growth trajectory pushes back into >80% in <8 weeks.
- `patch_register_active.yaml`: already chunked aggressively in ED-783 (now 8,533/18,000 = 47% of new cap). No further action.

**Discipline note** (going forward): When any register passes 80% of cap, archive proactively in the same commit as the next routine work. Treat 80% as the operational ceiling, not 100%.

**Cross-references:** ED-782 (collision repair), ED-783 (initial archival sweep), ED-786 (this entry).

**Files in this commit:**
- `skills/valoria-orchestrator/scripts/github_ops.py` (TOKEN_THRESHOLDS revised + comment block)
- `canon/editorial_ledger.yaml` (ED-786 added; ED-782/783/784/785 archived)
- `archives/editorial/editorial_ledger_archive_2026_05_02_b.yaml` (NEW)
- `tests/coverage_matrix.md` (historical sections moved to archive; Open Findings pruned)
- `tests/coverage_matrix_archive_2026_04_19.md` (NEW)
- `references/canonical_sources.yaml` (Last-touched breadcrumbs stripped)
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: stats_1_7_scale.md (commit A)

First commit of the L+PS mechanical migration sweep mandated by ED-784. `params/factions/stats_1_7_scale.md` is the canonical 1-7 stat block file — most foundational of the 9 consumer files.

**Header migration:** Stat block header `Mandate / Influence / Wealth / Military / Intel / Stability` → `Legitimacy / Popular_Support / Influence / Wealth / Military / Intel / Stability`. Starting Stats table header columns expanded `M (TTRPG) | M (BG)` → `L (TTRPG) | PS (TTRPG) | L (BG) | PS (BG)`. All faction rows seeded with equal L=PS values per PP-686 v2 §3.4-3.5 (Crown 5/5/5/5, Church 5/5/5/5, Hafenmark 4/4/4/4, Varfell 4/4/4/4, Guilds 3/3/3/3, Löwenritter —/—/3/3).

**Mechanic migrations (per audit §2.1 classifications):**

| Mechanic | Roll/Effect | Classification |
|---|---|---|
| Crown Royal Decree | Mandate vs Ob 2 | **L** (procedural) |
| Church Excommunication | Mandate vs target Mandate | **L** vs target **L** (procedural authority both sides) |
| Excommunication outcome | target Mandate −1 | target **L** −1 (institutional) |
| CI 60 Territorial Seizure | Mandate vs floor(owner's Mandate / 2) + 1 | **L** vs floor(owner's **L** / 2) + 1 |
| CI Seizure failure | Mandate −1 | Church **L** −1 |
| RM Community Weaving | Mending Mandate prerequisite ≥ 1 | Mending **PS** ≥ 1 (populist) |
| Baralta Suppression | Church Mandate −1/season while Mandate ≥ 4 | Church **L** −1/season while Baralta **L** ≥ 4 |
| Baralta Heresy outcomes | Church Mandate −1, Baralta's Mandate −1 | Church **L** −1, Baralta's **L** −1 |
| Baralta CI Suppression gate | while Baralta Mandate ≥ 4 | while Baralta **L** ≥ 4 |
| RM Mending prerequisite | Mandate ≥ 1 | **PS** ≥ 1 |
| Mandate Recovery (ED-066b) | factions with Mandate < starting recover +1 | **L** AND **PS** independently (cap at each starting value) |
| Institutional Mandate Trigger (ED-003) | Faction Mandate ≥ 4 | Faction **L** ≥ 4 (per audit Q2 — institutional) |
| Institutional Mandate Uphold/Appease (PP-189) | Mandate ≥ 4, Mandate −1 | **L** ≥ 4, **L** −1 (per audit Q2) |
| RM Revolution DA pool | Mandate (as dice) + History | **PS** (as dice) + History (populist) |
| RM Revolution outcome | Mandate −1 on failure | **PS** −1 on failure |
| PI track accrual | any faction Mandate < 3 at accounting | any faction **PS** < 3 (populace dissatisfaction trigger) |
| PI revolt check failure | Mandate −1 | **PS** −1 (outcome-driven populist loss) |

**Ethical Framework Modifiers strikes (PP-686 v2 / SUPERSESSION-PP686-002 + 003):**
- §General "Ethical Framework Ob Modifiers" table: SUPERSEDED, struck through, replaced by triadic decomposition in `faction_behavior_v30.md §3.7` (mission_alignment_modifier + cascade_alignment_modifier + expectation_alignment_modifier, ±2 cap).
- §Löwenritter "Ethical Framework Modifiers (PP-246)" table: SUPERSEDED, struck through. Löwenritter's Mission/cascade/expectation tags now authored in faction state per `faction_behavior_v30 §3.7`.

**Open item flagged:** Pre-existing inconsistency between Starting Stats table (Varfell BG Mandate 4) and L18 footnote (Varfell BG Mandate 3). Footnote updated to match table; flagged for Jordan confirmation as part of ED-784 Phase 2 (not blocking).

**Files in this commit:**
- `params/factions/stats_1_7_scale.md` (38 Mandate refs migrated; 2 Ethical Framework sections struck; Starting Stats table header + 6 rows updated; L18 footnote inconsistency flagged)
- `references/canonical_sources.yaml` (canonical_sha bumped)
- `references/propagation_map.md` (this section)

**Cross-references:** ED-784 (umbrella), PP-686 v2 (faction behavior v2), audit §2.1 (per-site classifications), `params/factions_personal.md` (L+PS canonical authority for seed-equal rule), `params/bg/core.md` (Ethical Framework strike applied 2026-05-01 SUPERSESSION-PP686-001).

**Remaining Phase 2 work:** 8 consumer files (faction_actions, factions_personal additional refs, ministry, institutions, parliament, ci_seizure, tracks, stress_patches, phases) + 8 reference files. Subsequent commits B, C, D.

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit B (faction_actions + ministry + factions_personal)

Second commit of the L+PS migration sweep. Three consumer files migrated.

**`params/bg/faction_actions.md` (38 refs):** All Mandate references in territory/parliamentary/charter/conquest mechanics → L (procedural authority across the board). Bulk patterns:

- `Roll: Mandate vs Ob ...` → `Roll: L vs Ob ...` (Assert, Charter, Influence, Tribune Investigate, Conquest)
- `controlling faction Mandate`, `controlling faction global Mandate`, `target Mandate`, `target controller Mandate` → L equivalents (institutional/procedural opposition)
- `Baralta's Mandate ≥ 4` (PP-431-COR CI suppression) → `Baralta's L ≥ 4`
- `Church Mandate +1` (failure-clause gain per audit Q3) → `Church L +1`
- `Hafenmark Mandate +1` (Manoeuvre/Conquest gain) → `Hafenmark L +1`
- `Hafenmark Mandate ≥ 4` (Conquest prerequisite) → `Hafenmark L ≥ 4`
- `Hafenmark Mandate >` (Manoeuvre gate) → `Hafenmark L >`
- `Church global Mandate >` (Church-prominent gate) → `Church global L >`
- `floor(Mandate / 2) + 1` (Charter limit, Assert/Seize Ob) → `floor(L / 2) + 1`
- `Mandate 0 from submission` (Diplomatic Token suspension) → `PS 0 from submission` (per audit Q1)
- Defensive Institutional Mandate (PP-189) gate `Mandate ≥ 4` → `L ≥ 4` (per audit Q2)
- Legacy mechanic name "Institutional Mandate" preserved in textual reference (Q2).

**`params/bg/ministry.md` (32 refs):** Ministry is a structurally institutional (administrative apparatus) entity. Per audit Q2, Ministry's "Mandate" → Ministry **L** only. Bulk: `Ministry Mandate` → `Ministry L`; `Crown Mandate ≥ 4` (Crown decree-support gate) → `Crown L ≥ 4`; bare `Mandate 3D vs Ob 1` (Ministry rolls) → `L 3D vs Ob 1`; `Ministry Collapse (Mandate 0)` → `Ministry Collapse (L 0)`; `AP-token in T13, Mandate ≥ 2` → `... Ministry L ≥ 2`. Stat-block row updated to indicate `PS not tracked for Ministry — administrative apparatus has no separate populist axis`.

**`params/factions_personal.md` (18 refs):** Mostly canonical-authoring file (PP-686 v2 source); bulk of "Mandate" mentions are intentional historical/derived references. Migrations applied:

- Starting Values table header expanded: `Mandate | Influence | ...` → `Legitimacy | Popular_Support | Influence | ...`
- All 7 faction rows seeded with equal L=PS values per PP-686 v2 (Crown 5/5, Church 5/5, Hafenmark 4/4, Varfell 4/4, Guilds 3/3, Revolution —/—, Löwenritter —/—)
- L36 "Löwenritter (no Mandate, no Wealth)" → "no L, no PS, no Wealth"
- Crown Royal Decree pool, Church Excommunication pool/gate, Hafenmark Sovereign Authority Doctrine pool → L (procedural authority)
- "Active attack on Mandate/Wealth" Stability check → "Active attack on L, PS, or Wealth"
- "Pool: relevant faction stat (typically Mandate or Influence)" → "(typically L, PS, or Influence depending on action's procedural-vs-populist nature)"
- Church Mandate ≥ 5 / Piety DA pool → Church L ≥ 5 / L pool (institutional)
- L38 init note phrasing updated to remove the now-stale "Mandate value above" reference (table no longer has a Mandate column); replaced with the canonical seed-equal rule with explicit per-faction values.

**Preserved intentionally** (L, PS, derived Mandate retained for backward compat):
- L8 PP-686 v2 NOTE comment block
- L14 derived Mandate row (`~~Mandate~~ (derived) | Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)`)
- L38 init note (now updated phrasing, but keeps "Mandate" only in narrative explanation)

**Cumulative ED-784 Phase 2 progress:**

| File | Mandate refs | Status |
|---|---:|---|
| stats_1_7_scale.md | 38 | ✓ Commit A (f8ac629) |
| factions_personal.md | 18 | ✓ Commit B |
| faction_actions.md | 38 | ✓ Commit B |
| ministry.md | 32 | ✓ Commit B |
| institutions.md | ~21 | pending |
| parliament.md | ~16 | pending |
| ci_seizure.md | ~12 | pending |
| tracks.md | ~11 | pending |
| stress_patches.md | ~9 | pending |
| phases.md | ~2 | pending |
| 8 reference files | ~56 | pending |

**Files in Commit B:**
- `params/bg/faction_actions.md`
- `params/bg/ministry.md`
- `params/factions_personal.md`
- `references/canonical_sources.yaml` (3 SHAs bumped)
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit C (institutions + parliament + ci_seizure + tracks + stress_patches + phases)

Third commit of the L+PS migration sweep. Six consumer files migrated, ~99 Mandate refs total.

**`params/bg/institutions.md` (27 refs):** Bulk migration — Ministry Mandate / Crown Mandate / Church Mandate / Crown's Mandate → L equivalents. Specific edits: Cardinal of Temperance Altonian diplomacy advancement roll (Mandate vs Ob = floor(Altonian diplomacy/2)+1) → L; bare Crown confirmation roll (Mandate vs Ob 2) → L; Ministry stat-row narrative ("Its Mandate (3) represents institutional legitimacy") → L (3) with audit Q2 footnote. All institutional throughout — Ministry is administrative apparatus per audit Q2 (no separate populist axis).

**`params/bg/parliament.md` (19 refs):** All procedural-authority parliamentary mechanics. Notable migrations:
- Crown Policy gates (`Mandate ≥ 4`) → `L ≥ 4` per audit Q5 procedural-authority interpretation
- §Mandate Recovery (PP-174): renamed to track L+PS independently, like ED-066b in stats_1_7_scale
- §Mandate Suppression (PP-296): renamed §L Suppression. Coalition cap targets institutional L stat (procedural-authority suppression). PS-targeting suppression (e.g., populist undermining via Information ops) noted as not bound by this cap.
- Institutional Mandate Uphold/Appease (PP-189): legacy name preserved, mechanic operates on L per audit Q2 (header + body footnoted)
- Trigger scope: Domain Action targeting "Mandate stat" → "L stat" (institutional context)
- Crown end-of-Phase-4 Mandate −1 → L −1

**`params/bg/ci_seizure.md` (20 refs):** Pure procedural Church religious-authority mechanics. All Mandate refs → L: Conditional Passive prominence gate, Suppress §3.7 opponent action, Hafenmark Structural Suppression (PP-431-COR Baralta L ≥ 4), Church/non-Church Political pool formulas (Mandate ± floor(CI/N)), seizure prerequisites (Church L ≥ 4, Prominence Church L > controlling faction L).

**`params/bg/tracks.md` (16 refs):** Mostly Turmoil track + Hafenmark Awareness track effects. PP-686 v2 NOTE comment block (L1) preserved as historical record. Migrations:
- Cardinal Altonian diplomacy advancement roll → L (matches institutions.md)
- Strain "Mandate check" at Tension/Crisis/Collapse states → "L check" (institutional pressure on faction procedural authority)
- Hafenmark Awareness 3+ effects: Church Mandate −1 → Church L −1 (institutional strain); Hafenmark Mandate ≥ 3 → Hafenmark L ≥ 3 (CI suppression ratchet)
- Excommunication "+2 Mandate" cost annotation → "+2 L" (Church loses procedural authority equivalent to Hafenmark's PE-driven institutional resilience)

**`params/bg/stress_patches.md` (14 refs):** Mostly Restoration Movement Founding outcomes + PP-475 Submission ruling + Church Prominence formula. Migrations:
- Church Prominence formula → Church L > controlling faction L
- Baralta Mandate ≥ 4 (CI suppression context) → Baralta L ≥ 4
- §Submission + Mandate 0 Ruling (PP-475) → §Submission + PS 0 Ruling per audit Q1 explicitly (header + body)
- "halved Mandate = 0" → "halved PS = 0" (audit Q1 ratification)
- "Mandate 0" / "Mandate-0 effects" → "PS 0" / "PS-0 effects"
- RM Founding outcome stats: Mandate 2/Mandate 1 → L 2 + PS 2 / L 1 + PS 1 (seed equal per PP-686 v2). Inline TODO flagged: PP-460 says RM is statless; may be obsolete content — flagged for Jordan review.

**`params/bg/phases.md` (3 refs):** Brief migrations:
- Church Prominence update (ED-326): "Church global Mandate exceeds territory's controlling faction's global Mandate" → "Church global L exceeds ... controlling faction's global L"
- Torben Loyalty modifier "Crown upheld Mandate 2+ consecutive seasons" → "Crown upheld L 2+ consecutive seasons" (procedural Crown discipline reward)

**Cumulative ED-784 Phase 2 progress:**

| File | Mandate refs | Status |
|---|---:|---|
| stats_1_7_scale.md | 38 | ✓ Commit A (f8ac629) |
| factions_personal.md | 18 | ✓ Commit B (0a32a29) |
| faction_actions.md | 38 | ✓ Commit B (0a32a29) |
| ministry.md | 32 | ✓ Commit B (0a32a29) |
| institutions.md | 27 | ✓ Commit C |
| parliament.md | 19 | ✓ Commit C |
| ci_seizure.md | 20 | ✓ Commit C |
| tracks.md | 16 | ✓ Commit C |
| stress_patches.md | 14 | ✓ Commit C |
| phases.md | 3 | ✓ Commit C |
| 8 reference files | ~56 | pending Commit D |

**Subtotal so far:** 225 Mandate refs migrated across 10 consumer files. ED-784 Phase 2 (consumer-file sweep) complete pending Commit D (reference files).

**Note on canonical_sources.yaml:** The 6 files in this commit (`params/bg/{institutions,parliament,ci_seizure,tracks,stress_patches,phases}.md`) are not SHA-tracked in `references/canonical_sources.yaml`. Only some `params/bg/*.md` files have SHA records (core, clocks, victory, royal_assassination, tensions_deck, faction_actions, ministry); the rest are downstream reference files without independent canonical authority. No canonical_sources update is required for this commit.

**Files in Commit C:**
- `params/bg/institutions.md`
- `params/bg/parliament.md`
- `params/bg/ci_seizure.md`
- `params/bg/tracks.md`
- `params/bg/stress_patches.md`
- `params/bg/phases.md`
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit D — closure

Final commit. ED-784 Phase 2 work complete.

**7 reference files migrated** (74 refs total): `params/factions/riskbreakers_identity.md` (17), `params/bg/ed_resolutions.md` (9), `params/bg/victory.md` (12), `params/bg/core.md` (17), `params/bg/npc_priority_trees.md` (9), `params/bg/npcs_special.md` (5), `params/scale_transitions.md` (5). Migration patterns followed audit §2/§3 classifications + commits A/B/C established conventions: procedural rolls → L; populist outcomes (morale, defection, talent drain) → PS; institutional gates → L; Crown Policy/Hafenmark Sovereignty/Crown Treaty/Senator Outward → L; named victory conditions (Ecclesiastical Mandate) preserved as proper nouns with L footnote; Mandate-order resolution (PP-112) → derived-Mandate = round((L+PS)/2) per audit Q4.

**Notable:** core.md Starting Stats table split (Mandate column → Legitimacy + Popular_Support; all 7 faction rows seeded equal); core.md PP-686 v2 init block phrasing updated; victory.md Hafenmark Parliamentary Sovereignty Mandate≥4 → L≥4; Peninsular Partition "Both Mandate ≥ 3" → "Both L ≥ 3 AND PS ≥ 3" (institutional + populist viability per audit Q5 strict reading); npcs_special.md general capture/execution PS−1/−2 (morale-blow populist component); scale_transitions.md debate-outcome Domain Echo expanded to contested-axis (L procedural / PS populist).

**ED-784 Phase 2 — COMPLETE.** 17 files, **299 Mandate refs** migrated.

| Commit | SHA | Files | Refs |
|---|---|---:|---:|
| A | f8ac629 | stats_1_7_scale.md | 38 |
| B | 0a32a29 | factions_personal + faction_actions + ministry | 88 |
| C | 9a07316 | institutions + parliament + ci_seizure + tracks + stress_patches + phases | 99 |
| D | (this) | riskbreakers_identity + ed_resolutions + victory + core + npc_priority_trees + npcs_special + scale_transitions | 74 |

**Files in Commit D:** the 7 above + `references/canonical_sources.yaml` (3 SHAs bumped: victory, core, scale_transitions; other 4 not tracked) + `references/propagation_map.md` (this section).

**Watch-out:** propagation_map now ~99% of cap. Next session priority: archive ED-782..786 + Phase 2 commit-A/B/C/D sections from propagation_map (same chunking discipline as ED-786 editorial_ledger archival).

## PP-716 — Wound mechanic correction (2026-05-09)
**Source:** Jordan canonical clarification.
**Files patched:** designs/scene/derived_stats_v30.md (§4.1 authoritative), designs/scene/combat_v30.md (L253-378 wound spec + thread interface), designs/threadwork/threadwork_v30.md (Leap/Weaving/Pulling/Mending/FR pool penalty), params/combat.md (Health formula + Thread interface), params/mass_combat.md (CF Zoom-In).
**Propagation:** All references to wound-induced +1 Ob (combat→thread, mass-Command, BG-CF) flipped to −1D Pool. All Vitality = End × 10 references reverted to Health = (End+6)×(MW+1). MW = floor(End/2)+1 restored. derived_stats_v30 §4.1 made authoritative source; other files reference §4.1.
**ED resolved:** ED-789. **ED reverted:** ED-694.
**Open propagation:** tests/sim/combat_arch_residual_stress_01/r1_wound_permanence.md (Module 1 R1) is SUPERSEDED — banner added; needs redo against PP-716 canon. canonical_sources.yaml SHAs marked PENDING_PP_716 pending freshness_gate refresh.

## PP-717 npc_behavior §1.2 stale-redirect fix (2026-05-10)
**Class E (editorial); applied this commit.** No mechanical propagation; corrects documentation pointer drift.
- `designs/npcs/npc_behavior_v30.md §1.2`: redirects updated to point at `designs/personal/conviction_taxonomy_v30.md` (PP-684 canonical) and companion `conviction_axis_matrix_v30.md`.
- `designs/personal/conviction_track_v1.md`: SUPERSEDED banner added at top; §1 deprecated; §2 Scar accumulation preserved as canonical pending PP-718 weight-scaling review.
- `references/canonical_sources.yaml`: conviction_track entry annotated as PARTIALLY SUPERSEDED.
- No code changes. No simulation re-run.
- Surfaced by: conviction_stress_01 (A-L09 P1 drift) commit 57bd26f4.
- Cross-reference: this PP unblocks future readers of npc_behavior_v30 §1.2 from learning the legacy 9-Conviction set.

---

*Older entries (before the most recent 8) archived to `references/propagation_map_archive_2026-05-10.md` on 2026-05-10 to keep working file under 15k-token CI limit.*

## PP-719 fieldwork §5.6b sustained Disposition reduction clarification (2026-05-10)
**Class E (editorial); applied this commit.** Single-line clarification, no mechanical change.
- `designs/scene/fieldwork_v30.md §5.6b`: "sustained for 2 seasons" → "2 consecutive seasons (defined as Disposition value at Accounting in season N below +3 AND season N+1 below +3, both unbroken). Non-consecutive seasons below +3 do not aggregate."
- Surfaced by: EC-F2.A-01 in `fieldwork_lifecycle_stress_01` (commit ddccbf9a).
- No simulation re-run required.

## PP-720 R7 stress-FF threshold spec (2026-05-10)
**Class C (mechanical — parameter/resolution-path extension); applied this commit.**
- `designs/scene/combat_v30.md §5`: new subsection "Stress-FF (ranged into melee under stress conditions)" inserted before §6 ARMOUR.
- Stress conditions: Wounds ≥1 OR Composure ≤3 OR environmental degradation.
- Resolution: secondary FF roll TN+1 (single-stress) / TN+2 (multi-stress); damage = floor(STR/2) + weapon_mod_vs_armour.
- No new Ob channel; uses canonical Combat Pool + TN modifier.
- Tabletop fallback waiver clause preserves Game-Master flexibility.
- Surfaced by: combat_arch_residual_stress_01 Module 7 R7 (commit c58bc670).
