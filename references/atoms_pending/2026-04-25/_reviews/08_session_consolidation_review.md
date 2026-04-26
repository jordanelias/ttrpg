# Exhaustive Review — `08_session_consolidation`

**Topic:** Session Consolidation 2026-04-25 (consolidated)
**Atoms:** 19
**Method:** strict ID-presence check in primary registers (definition-pattern aware: YAML `id: X-N` for ED/PP, `| T-N |` table-row or `## T-N` heading for T/M) + repo path-existence + substantive-claim extraction with best-match canon excerpt.

## Summary

### ID classification

- **DEFINED-IN-CANON:** present as a defined entry in primary register (YAML `id:` for ED/PP; table row or heading for T/M).
- **MENTIONED-IN-CANON:** appears in canon corpus but not as a primary-register definition (likely cross-reference or editorial marker).
- **PARTIAL:** defined in canon, but atom's discussion is materially richer.
- **NEW:** not present in any fetched canon file.

| status | count |
|---|---|
| DEFINED-IN-CANON | 1 |
| MENTIONED-IN-CANON | 7 |
| PARTIAL | 0 |
| NEW | 0 |

### Path verification

| status | count |
|---|---|
| MISSING-FROM-REPO | 1 |

### Substantive claims surfaced: 40

## ID-by-ID comparison

### ED-539 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/audit/valoria_systems_workplan.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__22__from-workplan-valoria-workplan-final-md`):
  > play (AUD-NPC-01), Accord propagation to settlement Order (AUD-SET-02), Derived stats calibration (AUD-DS-01), Faction politics simulation (AUD-FP-01), Coverage matrix P1 EDs (ED-588, 589, 612). - **ED-539** (TC reform + TCV revaluation + Seizure Accord compound effect) as the most urgent simulation gap. If Church still wins 50%+ after these three changes compound, the tc_political_redesign hasn't
- **canon context** (`designs/audit/valoria_systems_workplan.md`):
  > erged into victory_v30. Hafenmark Parliamentary alternate struck but replacement not fully specified.  **Outstanding:** ED-538 (compound simulation). ED-539 (TC reform compound). J-6 (Seizure Ob). Starting PT values (provisional).  ---  # S08 — TC POLITICAL REDESIGN  ## B. File Index  | File | Repo | Role | |------|------|------| | designs/board_game/tc_political_redesign_v30.md | ttrpg | CI miles

### ED-545 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/architecture/player_agency_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__19__from-rse-critique-valoria-rse-critique-md`):
  > ement / Aftermath). Automation handles sub-phases internally. - **S06 Faction Layer:** 100+ tracked values need UI information architecture. Territory-card representations. - **S17 Scale Transitions (ED-545, P1):** Substantially resolved by §4.3.2/§4.3.3/§4.4. Verify completeness against 120+ arc registry — every significant arc should have a Zoom In trigger.
- **canon context** (`designs/architecture/player_agency_v30.md`):
  > m In). It offers the scene. The player decides whether to spend a scene action on it. If they don't, the crisis resolves through NPC AI.  This solves ED-545 (only 5 Zoom In triggers) structurally: the Scene Slate IS the Zoom In trigger system. Any game state change that would be interesting to experience personally becomes a scene opportunity in the Slate.  ### 7.5 NPC Behavior (npc_behavior_v30) 

### ED-547 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/architecture/player_agency_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__19__from-rse-critique-valoria-rse-critique-md`):
  > SE critique (`valoria_rse_critique.md`)  - **S12 Social Contest:** UI suggested-style hint (mechanically strongest option given contest state). One-page TTRPG quick-reference card. - **S14 Fieldwork (ED-547):** Scene cap (3–5 per season) IS the fieldwork resource. Make explicit, not implied. - **S15 Mass Combat:** Three-phase compression for videogame (Strategy / Engagement / Aftermath). Automatio
- **canon context** (`designs/architecture/player_agency_v30.md`):
  > aligned with RM pursues RM Beliefs without faction infrastructure. RM Community Organizing is a scene opportunity in territories with Piety ≤ 1. | | ED-547 (Fieldwork resource cost) | Scene action budget IS the fieldwork cost — each investigation scene costs a scene action that could have been spent elsewhere. |  ---  ## §9 — RESOURCES (Throughline T2)  Personal economic capacity. Range: 0–5. Cap:

### ED-577 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/threadwork/threadwork_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__29__phase-iv-simulation-completion`):
  > ation.** AUD-SET-03. Largest unsimulated canonical layer. 5. **RM victory probability.** AUD-VIC-02. RM is "hardest mode" — needs validation that it's *possible*. 6. **Co-Movement card calibration.** ED-577-01 through 04. Hard dependency for simulation reliability.
- **canon context** (`designs/threadwork/threadwork_v30.md`):
  > t naturally possess, modeling the strategic value of Thread-monitoring intelligence networks.  ## 4.3 Auto-Effect Tables  ### Co-Movement Cards 1–15 (ED-577 — canonical card list)  All Thread Tension references from the original deck are converted to Mending Stability (inverted polarity: original +TT becomes −MS, original −TT becomes +MS).  | Card | Name | Actualized Effect | Unactualized Effect |

### ED-588 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/victory_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__22__from-workplan-valoria-workplan-final-md`):
  > * Knot formation during play (AUD-NPC-01), Accord propagation to settlement Order (AUD-SET-02), Derived stats calibration (AUD-DS-01), Faction politics simulation (AUD-FP-01), Coverage matrix P1 EDs (ED-588, 589, 612). - **ED-539** (TC reform + TCV revaluation + Seizure Accord compound effect) as the most urgent simulation gap. If Church still wins 50%+ after these three changes compound, the tc_p
- **canon context** (`designs/provincial/victory_v30.md`):
  > T9.  RM holds T9 through cultural presence, not military garrison. Control is maintained while: - RM has ≥ 3 Presence markers in T9 - PT in T9 ≤ 3 *(ED-588 resolved 2026-04-16: revised from PT ≤ 1. T9 starts PT 5 under Church management; ≤ 1 was unreachable post-Uprising without 4+ seasons of RM governance. PT ≤ 3 is achievable immediately after Uprising OW: PT 5 − 2 = PT 3. RM must then prevent C

### ED-663 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/scene/derived_stats_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__25__phase-0-housekeeping-prerequisite-not-optional`):
  > ing (prerequisite, not optional)  Per `valoria_workplan_final.md` Phase 0. Must complete before substantial new design work.  1. Rebuild `editorial_ledger_summary.yaml` (workplan 0.1). 2. Deduplicate ED-663 in active ledger (0.2). 3. Update file_index_summary.md propagation-pending count (0.3). 4. Run broken_dependency_checker against propagation_map (0.4). 5. Verify session_log open_items against
- **canon context** (`designs/scene/derived_stats_v30.md`):
  > ld - Haushalt Competence bonus: +Competence × 25 gold/season (Competence 0–3). Cap: Haushalt Competence income cannot exceed Wealth × 50 per season. (ED-663 resolution) - Campaign Supply (units in hostile territory): −100 gold/season - Siege (attacker): −100 gold/season per active siege - Muster (Levy): −50 gold - Muster (Professional): −150 gold - Muster (Heavy Infantry/Cavalry): −300 gold - Must

### ED-668 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_master_consolidation__25__phase-0-housekeeping-prerequisite-not-optional`):
  > ndex_summary.md propagation-pending count (0.3). 4. Run broken_dependency_checker against propagation_map (0.4). 5. Verify session_log open_items against editorial_ledger (0.5). 6. Triage P0 blockers ED-668–672 (0.6). Resolve before any Phase I work. 7. Params file staleness audit (0.7).
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > 6-04-24 from active ledger   - id: ED-660     date: 2026-04-17     description: "Certainty scale: Almstedt Certainty 6→4 (Jordan-confirmed 2026-04-23)."     status: resolved     severity: P2    - id: ED-668     date: 2026-04-17     description: "MS decline rate calibration — resolved by MS trajectory v1 (f2b5d143) and references/ms_budget.md. Baseline upward pressure ~0.2 MS/year from Warden contr

### PP-508 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/mass_battle_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__24__from-simulation-review-simulation-review-2026-04-1`):
  > . - **PP-NPC-01 through NPC-04 are critical for videogame AI.** Crown Decree gate (Mandate ≥ 3), coup determinism fix, Church drift conditioning, Varfell cooldown. - **Mass combat splitting doctrine (PP-508) confirmed.** +9% to +45% advantage. Counters: Narrow Pass terrain, Feigned Retreat. - **Coalition Grand Contest mechanic validated.** Shared pool (14) handles 5 exchanges without Spent.  ---  
- **canon context** (`designs/provincial/mass_battle_v30.md`):
  > mune to that flank | 1 | Sacrifices offence | | Hammer & Anvil | Shield Wall holds; Fast unit envelops | 3 | Break Anvil first |  Splitting doctrine (PP-508 — replaces P2-14 note, ED-358): Splitting is structurally across simultaneous engagements. Simulation results: - Split dominates concentration by +9% to +45% win-rate depending on Command matchup. - Only cases where split advantage is negligib

## Path verification

| path | status | atom occurrences |
|---|---|---|
| `designs/architecture/core_experiential_moments.md` | MISSING-FROM-REPO | 1 |

## Substantive claim findings

_40 substantive claims (max 3 per atom) with best-match canon excerpts._

### Matched claims (33)

- **atom** `valoria_master_consolidation__00__preamble`
  - claim: > Each prior output's substance is integrated below; conflicts are resolved in favor of the most recently grounded version with revisions from the recommendation check applied.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > 11). threadwork_v25_historical.md had mismatched label — internal banner added. sim_ttrpg_batch_legacy_* files flagged for follow-up banner pass (low priority). See designs/audit/label_audit_2026-04-19.md."     status: resolved     severity: P3     s

- **atom** `valoria_master_consolidation__00__preamble`
  - claim: > **Session Trajectory** — what was produced, in what order, with what grounding
2.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/5)
  - canon excerpt: >  severity: P1     source: "PP-674"    - id: ED-600     date: 2026-04-19     description: "Niflhel named operatives (Quartermaster, Quiet One) — dead. Session B Niflhel dissolution. STRUCK in arc_expansion_v30.md (bdf8a6a2)."     status: resolved     

- **atom** `valoria_master_consolidation__02__2-2-scale-transi`
  - claim: > - **§4.3.3:** 5 world-state Zoom In triggers (Clock Band Transition, NPC Conviction Crisis, Treaty Proposed/Broken, Territory Control Change, Warden Emergency).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 6/8)
  - canon excerpt: > 4     date: 2026-04-19     description: "Hafenmark food vulnerability and Crown Einhir suppression DA — resolved as non-mechanics. Both exist only as worldbuilding texture. Existing mechanics (Trade Network, Heresy Investigation, Church AP, Parliamen

- **atom** `valoria_master_consolidation__02__2-2-scale-transi`
  - claim: > - **§4.4:** "Where Were You?" retrospective scenes (4 player-context cases: companion present, Knot partner, high Disposition, no connection).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 6/8)
  - canon excerpt: > 'WC 3 is the singular endgame survival path' to three-path framing (disciplined non-Warden / WC 3 cooperative / WC 3 wagered). Prior framing produced player misread that WC 3 was a survival floor; correct reading is budget enabler with three viable l

- **atom** `valoria_master_consolidation__07__2-7-throughlines`
  - claim: > 11 upward transitions (DE-1 through DE-11), 9 downward transitions (ZI-1 through ZI-9), 10 lateral transitions (LT-1 through LT-10).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: > 68     date: 2026-04-17     description: "MS decline rate calibration — resolved by MS trajectory v1 (f2b5d143) and references/ms_budget.md. Baseline upward pressure ~0.2 MS/year from Warden contribution; Secession War-scale events ~1 MS/year net dow

- **atom** `valoria_master_consolidation__19__from-rse-critiqu`
  - claim: > - **S14 Fieldwork (ED-547):** Scene cap (3–5 per season) IS the fieldwork resource.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/6)
  - canon excerpt: > attle frequency."     status: resolved     severity: P2     source: "2026-04-24 audit conversation P1-1"    # Migrated 2026-04-24 from active ledger (Scene Slate + scale_transitions entries — committed 3e6b0b3 + 19fc650)   - id: ED-745     date: 2026

- **atom** `valoria_master_consolidation__19__from-rse-critiqu`
  - claim: > - **S06 Faction Layer:** 100+ tracked values need UI information architecture.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/6)
  - canon excerpt: >  until a specific architecture is selected."     status: resolved     severity: P2    - id: ED-712     date: 2026-04-19     description: "Generalized Faction Succession Contest. Resolved 2026-04-24 across two commits: (1) social_contest §7.2 (commit 

- **atom** `valoria_master_consolidation__19__from-rse-critiqu`
  - claim: > - **S17 Scale Transitions (ED-545, P1):** Substantially resolved by §4.3.2/§4.3.3/§4.4.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/5)
  - canon excerpt: > nseparability driving transformation propagation). (4) peninsular_strain L231: §2.4.2 (nonexistent — only §2.4 + §2.4b exist) → §2.4b Accord vs Order Scale Distinction (which is the actual canonical surface for personal-scale Order cap rule). 5th fin

- **atom** `valoria_master_consolidation__22__from-workplan-va`
  - claim: > - **Phase 1 P1 blockers:** Knot formation during play (AUD-NPC-01), Accord propagation to settlement Order (AUD-SET-02), Derived stats calibration (AUD-DS-01), Faction politics simulation (AUD-FP-01), Coverage matrix P1 EDs (ED-588, 589, 612).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 6/8)
  - canon excerpt: > 7-4.9). Source: 2026-04-24 audit §3.9."     status: resolved     severity: P3    - id: ED-753     date: 2026-04-24     description: "mass_battle §A.7 Phase 2 Volley gains design-rationale paragraph: Power-only formula is intentional asymmetry — Volle

- **atom** `valoria_master_consolidation__22__from-workplan-va`
  - claim: > If Church still wins 50%+ after these three changes compound, the tc_political_redesign hasn't addressed the balance problem.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: > Einhir suppression DA — resolved as non-mechanics. Both exist only as worldbuilding texture. Existing mechanics (Trade Network, Heresy Investigation, Church AP, Parliamentary Motion) cover the design space. See designs/audit/gap_resolution_2026-04-19

- **atom** `valoria_master_consolidation__24__from-simulation-`
  - claim: > Phase 0 (workplan housekeeping) is prerequisite to all subsequent phases.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/6)
  - canon excerpt: > 7-4.9). Source: 2026-04-24 audit §3.9."     status: resolved     severity: P3    - id: ED-753     date: 2026-04-24     description: "mass_battle §A.7 Phase 2 Volley gains design-rationale paragraph: Power-only formula is intentional asymmetry — Volle

- **atom** `valoria_master_consolidation__25__phase-0-housekee`
  - claim: > Must complete before substantial new design work.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/4)
  - canon excerpt: >  (Hafenmark/Löwenritter/RM lacking М-4 characterization). Framework resolution: T-15a/b/c in throughlines_meta_infill.md §3.1. Design-doc propagation complete 2026-04-19: Hafenmark §8.4, Löwenritter §8.9, RM §8.8 (factions_personal_v30)."     status:

- **atom** `valoria_master_consolidation__25__phase-0-housekee`
  - claim: > Deduplicate ED-663 in active ledger (0.2).
  - best match: `canon/editorial_ledger.yaml` (overlap 2/4)
  - canon excerpt: > tus: open     severity: P2     source: "PP-666"    - id: ED-768     date: 2026-04-24     description: "Orphaned PROVISIONAL markers identified across active spec corpus. 13 markers reference low-numbered EDs (ED-063, ED-071, ED-074, ED-098, ED-137, E

- **atom** `valoria_master_consolidation__27__phase-ii-experie`
  - claim: > Must precede further mechanical specification.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > c edit warranted at present."     status: resolved     severity: P2    - id: ED-669     date: 2026-04-17     description: "Irreversible institutional precedent persistence across campaigns. Resolved 2026-04-24: closed as deferred-pending-design-inten

- **atom** `valoria_master_consolidation__27__phase-ii-experie`
  - claim: > **Author Five Moments document.** Recommendation #1.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > Witness Spirit Ob 1→2 raise during caste-transgressive Conviction display, Conviction Shake 1→2 seasons on failed check, self-applied Doubt Marker on Authority RS while invoking caste-transgressive Conviction). §3.6.2 defines Conviction Reformation a

- **atom** `valoria_master_consolidation__27__phase-ii-experie`
  - claim: > Enumerate 3–7 moments with state preconditions, player actions, sensory design, consequences, dependent systems.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > elow ≥ 2 prerequisite. Revised: ≥ 2 disruptive ops in same season → WC −1 (cap −1/season). Arc D fires only if WC was ≥ 1 in prior 4 seasons (initial-state WC 0 ≠ Arc D). Source: 2026-04-24 stress-test 2."     status: resolved     severity: P2     so

- **atom** `valoria_master_consolidation__28__phase-iii-docume`
  - claim: > Refresh stale canonical files (clock_registry most urgently; J-7 scale decision propagated).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 5/8)
  - canon excerpt: >  resolved     severity: P2     source: "PP-671"    - id: ED-718     date: 2026-04-19     description: "Throughlines hierarchical framework (PP-672) — canonical vetting guide adopted. Five tiers: Ω (intent, 1), Μ (modes, 4), М (meta-throughlines, 6), 

- **atom** `valoria_master_consolidation__28__phase-iii-docume`
  - claim: > Treat as working notes; migrate canonical content to Layer 1.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/7)
  - canon excerpt: > rain §4.1 replaces battle-season +1 with per-territory +1 capped at +3/season. peninsular_strain §4.2 decouples decay from peninsula-wide peace, adds Treaty-pair decay (−1/pair, cap −2/season). peninsular_strain §4.4 reframes Strain/IP from 'no cross

- **atom** `valoria_master_consolidation__29__phase-iv-simulat`
  - claim: > **ED-539 compound effect.** Most urgent.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > 4-24     description: "Officer death roll scoped per-battle, not per-Size-loss-event. Spec was ambiguous (could be read as per-event with multi-stage compounding probability). Resolution: 1d20 vs total Size lost in battle, single roll at battle resol

- **atom** `valoria_master_consolidation__29__phase-iv-simulat`
  - claim: > TC reform + TCV revaluation + Seizure Accord ≥ 2.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: >  all factions."     status: resolved     severity: P2    # Migrated 2026-04-24: ED-704 resolved   - id: ED-704     date: 2026-04-19     description: "Seizure does not apply to Uncontrolled territories. Resolved 2026-04-24: peninsular_strain §5.2 adds

- **atom** `valoria_master_consolidation__29__phase-iv-simulat`
  - claim: > **Rendering Strain integration.** Recommendation #5.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > 4-22)."     status: resolved     severity: P4    # Migrated 2026-04-25 (resolved 2026-04-24/25)   - id: ED-769     date: 2026-04-24     description: "Rendering Stability → Mending Stability rename residual cleanup. strategic_layer_v30_infill.md L22 P

- **atom** `valoria_master_consolidation__30__phase-v-convicti`
  - claim: > Author Conviction pedagogy progression (Season 1 introductory scene, structured difficulty across subsequent seasons).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/8)
  - canon excerpt: > Witness Spirit Ob 1→2 raise during caste-transgressive Conviction display, Conviction Shake 1→2 seasons on failed check, self-applied Doubt Marker on Authority RS while invoking caste-transgressive Conviction). §3.6.2 defines Conviction Reformation a

- **atom** `valoria_master_consolidation__30__phase-v-convicti`
  - claim: > Specify Collective Rendering Shift victory path (Stage 1 + Stage 2).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/7)
  - canon excerpt: > 4-22)."     status: resolved     severity: P4    # Migrated 2026-04-25 (resolved 2026-04-24/25)   - id: ED-769     date: 2026-04-24     description: "Rendering Stability → Mending Stability rename residual cleanup. strategic_layer_v30_infill.md L22 P

- **atom** `valoria_master_consolidation__30__phase-v-convicti`
  - claim: > Implement Scar propagation through Knots, institutions, public spaces (P-12 mechanically).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/8)
  - canon excerpt: > posture gaps (Hafenmark/Löwenritter/RM lacking М-4 characterization). Framework resolution: T-15a/b/c in throughlines_meta_infill.md §3.1. Design-doc propagation complete 2026-04-19: Hafenmark §8.4, Löwenritter §8.9, RM §8.8 (factions_personal_v30)."

- **atom** `valoria_master_consolidation__32__phase-vii-hand-a`
  - claim: > 14 named NPC dialogue trees and arcs.
  - best match: `canon/editorial_ledger.yaml` (overlap 2/3)
  - canon excerpt: > ' while ci_political_v30 §1.1 (current canonical) uses 'CI (Church Influence)'. Two parallel naming conventions in active spec. Now: glossary entry renamed to 'Church Influence | CI' with note that TC is renamed; collision note (L66) updated; abbrevi

- **atom** `valoria_master_consolidation__32__phase-vii-hand-a`
  - claim: > - **Supporting tier:** Chronicler voices (4–6 voices, evolving across seasons).
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/7)
  - canon excerpt: > 2, §1.3 (PP-667)."     status: resolved     severity: P2     source: "PP-667"    - id: ED-715     date: 2026-04-19     description: "OPEN ITEMS sweep across settlement_layer, military_layer, peninsular_strain, faction_layer, victory_v30, threadwork_v

- **atom** `valoria_master_consolidation__32__phase-vii-hand-a`
  - claim: > Dependency: Five Moments framework must exist before Core tier content authored.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/7)
  - canon excerpt: > al_v30)."     status: resolved     severity: P2     source: "PP-671"    - id: ED-718     date: 2026-04-19     description: "Throughlines hierarchical framework (PP-672) — canonical vetting guide adopted. Five tiers: Ω (intent, 1), Μ (modes, 4), М (me

- **atom** `valoria_master_consolidation__33__phase-viii-varia`
  - claim: > Build after core 245 AG campaign is playable.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 2/4)
  - canon excerpt: > tle §E.4 caps reframed accordingly. Source: 2026-04-24 audit conversation P1-1 — prior mechanism inverted historical Pax Romana logic (Pax stabilizes after conquest; spec taxed conquest itself). Combination of fix-options (1)+(3) per audit conversati

- **atom** `valoria_master_consolidation__36__how-recommendati`
  - claim: > Earlier session outputs that the fuller corpus invalidated were retracted explicitly in §3.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 3/8)
  - canon excerpt: >  Loyal/Restless/Autonomous/Split). See conflict_architecture_proposal.md, clock_registry_v30.md. Propagated Session B (c0be619, f6b6ae6) + 2026-04-19 session (148d0184..8ff353d3)."     status: resolved     severity: P2     source: "Session B graduate

- **atom** `valoria_master_consolidation__37__what-the-recomme`
  - claim: > Recommendation #1 (Five Moments) requires Jordan's authorial decisions before becoming implementable.
  - best match: `canon/editorial_ledger_archive.yaml` (overlap 4/8)
  - canon excerpt: > (PP-674). valoria_hooks.vetting_gate() enforces vetting: block on Class A/B patch register entries from PP-674 forward. New task type design_proposal requires loading throughlines_meta.md. Tier N added above Ω: subject-grounding check against Renaiss

_(3 more matched.)_

### Unmatched claims — possibly NEW or rephrased (7)

- atom `valoria_master_consolidation__00__preamble`: > **What the Corpus Already Contains** — features and revisions that obviated portions of earlier critique
3.
- atom `valoria_master_consolidation__07__2-7-throughlines`: > Sufficient Scope at 7 conditions.
- atom `valoria_master_consolidation__21__from-systematic-`: > Should be stated clearly in the game's own text.
- atom `valoria_master_consolidation__25__phase-0-housekee`: > Rebuild `editorial_ledger_summary.yaml` (workplan 0.1).
- atom `valoria_master_consolidation__28__phase-iii-docume`: > Deprecate Layer 2 uploaded documents.
- atom `valoria_master_consolidation__37__what-the-recomme`: > Acknowledged gaps in §8.
- atom `valoria_master_consolidation__37__what-the-recomme`: > Recommendation #3 (literal rendering) is near-implementable.

## Recommendation

**Recommendation: CANONICAL-PROMOTION-NEEDED — 7 IDs mentioned in canon but not in primary register; promote to formal entries before ingestion.**

- ID classification: {'DEFINED-IN-CANON': 1, 'MENTIONED-IN-CANON': 7, 'PARTIAL': 0, 'NEW': 0}
- Path verification: {'MISSING-FROM-REPO': 1}
- Substantive: 33 matched / 7 unmatched