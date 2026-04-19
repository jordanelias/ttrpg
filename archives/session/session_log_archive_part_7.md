
session_id: sim_alternate_branches2_2026-04-17
session_close: 2026-04-17
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []
resolutions_this_session:
  - Alternate branches batch 2: Branches K-T (10 new alternates)
  - K: Olafsson wins College vote — extra-territorial heresy designation as legal shadow on Hafenmark inner circle
  - L: Thale defects to Vaynard — trilateral intelligence arrangement; collapses cleanly at Coup
  - M: Himlensendt Arc C public during Grand Contest — Klapp framework saves him; TC-5; Vaynard-Himlensendt scholarly alliance
  - N: Baralta Arc B triggers — Niflhel arrangement creates permanent constitutional precedent; Feldhaus crisis
  - O: Stenskald endorses bloodline — Varfell succession locked to hereditary; Incapacity Assessment cascade at S28
  - P: Linder reports RS comment fully — Himlensendt sermon; offhand comment becomes public political theology
  - Q: Vaynard no practitioner at S3 Discovery Event — Arc C from absence of support, not excess of exposure
  - R: Feldhaus no addendum — forced Parliamentary motion creates broader precedent than addendum would have
  - S: Haelgrund refuses synthesis request — both parties build Thread-perception map independently; neutrality dataset more consequential
  - T: Almud enters Arc A at S14 — reform prevents Counter advance; Ehrenwall moral ledger shifts
  - Cross: neutrality always political; smallest actions most consequential; reform requires voluntary uncertainty
files_modified:
  - tests/sim_alternate_branches2_2026-04-17.md (new)
  - canon/editorial_ledger.yaml (ED-670/671/672/673; 15 P2 EDs archived; next_id: 674)
  - canon/editorial_ledger_archive.yaml (15 P2 EDs archived)
  - tests/coverage_matrix.md (batch 2 alt findings; Batches 1-2 findings trimmed to archive)
  - tests/coverage_matrix_archive.md (Batches 1-2 CM content archived)
open_items:
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
  - ED-670/672/673 (P2)
  - All prior open items carried forward

---

session_id: repo_restructure_cleanup_2026-04-18
session_close: 2026-04-18
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
  description: >
    Restructure cleanup complete. file_index regenerated, 36 skeleton headers
    fixed, editorial_gate bypass removed, canonical_sha__ keys updated,
    freshness gate re-synced, file_index trimmed below threshold.
    Remaining CI items: 11 missing_skeleton errors on gm_ref arc docs and
    3 audit docs (pre-existing, never had skeletons). These are auto-fixable
    but not critical.
blockers: []
commits:
  - 3069849: "file_index regen, 36 skeleton header fixes, editorial_gate bypass removed"
  - ea543dc: "canonical_sha__ key fixes pass 1"
  - 67672f7: "canonical_sha__ key fixes pass 2"
  - 38bad89: "canonical_sha__ key fixes pass 3"
  - freshness_gate: "SHA re-sync (49 fields)"
  - a76d5bd: "file_index trimmed below 8k threshold"
open_items:
  - "11 missing_skeleton errors (gm_ref arcs + audit docs) — generate in future session"
  - "arc_register.md freshness — pre-existing, needs params re-sync"
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)

---

# Session Log — 2026-04-18 (engine audit + editorial decisions)
last_stage: Engine audit + 7 editorial decisions committed. Engine rebuild next.
next_action:
  skill: simulation engine rebuild
  description: >
    Rebuild tests/sim_framework/ from scratch against canonical params.
    50 gaps in engine_v2.py (tests/audit/engine_audit_2026-04-18.md).
    7 editorial decisions (tests/audit/editorial_decisions_ci_pv_2026-04-18.md).
    Previous NPC PC sims (a6f468ee) invalid.
  blockers: []
commits:
  - 98b0fa10: "[simulation] SIM-B2 all items resolved"
  - a6f468ee: "[simulation] 11 NPC PC campaigns — INVALID"
  - 54730ea5: "[simulation] engine audit — 50 gaps"
  - 9b58a979: "[simulation] TC/CI/TCV conflict register"
  - 19448617: "[editorial] 7 CI/PV/seizure/victory decisions"
resolutions_this_session:
  - "SIM-B2-01/02/03 PASS"
  - "Engine audit: 50 gaps"
  - "7 editorial decisions committed"
open_items:
  - Engine rebuild required
  - PV values for T2,T4,T5,T6,T7,T10,T11,T13,T17 TBD
  - TC->CI, TCV->PV propagation across 8+ files
P1-BLOCKER count: 0

---

session_id: peninsular_strain_restructure_propagation
session_close: 2026-04-19
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

# Session Log — 2026-04-19
last_stage: Scene mechanics audit + ED-295/297 resolved + engine v3 fixes (victory check, RS recovery, formula propagation)
next_action:
  skill: simulation — Warden emergence + Uncontrolled reclaim + TC→CI propagation
  description: >
    Engine v3 victory check fixed. RS recovery added (WC-gated). 3 params conflicts propagated.
    ED-295/297 resolved via historical precedent. Mass combat ×3 stale ref fixed.
    Blocking: WC never advances → RS recovery never fires.
    Need: Warden emergence mechanic, Uncontrolled territory reclaim, TC→CI/TCV→PV propagation.
  blockers: []
commits:
  - 801ff5cd: ED-295/297 resolved, Composure Cha×3 propagated
  - 4759c543: Stamina End×5 + Disposition=Bonds propagated
  - 472355b9: Mass combat ×3 stale ref fixed
  - pending: Victory check + RS recovery fixes
P1-BLOCKER count: 0

---

session_id: 768069d5458ae791
session_close: 2026-04-19
phase: 0
status: handoff
last_stage: Ledger damage assessment complete, execution plan verified
next_action:
  skill: editorial — ledger repair + audit document commit
  description: >
    Phase 1: Rebuild canon/editorial_ledger.yaml with 42 open entries from
    archives/editorials/editorial_ledger_archive_1001_1200.yaml. Mark ED-620,624,628,643
    resolved (verified against victory_v30). Set next_id:704. Lost IDs: 670-672,698-703.
    Phase 2: Commit 4 docs to designs/audit/ — system_audit_2026-04-18.md,
    system_audit_part2_2026-04-18.md, valoria_design_session_2026-04-17.md,
    valoria_integration_proposal.md.
    Phase 3: Register ~30 new flags as ED-704+ from uploaded audits (4 P1, 13 P2, 8 P3,
    5 blocking integration specs, 4 design deliverables).
    Phase 4: Rebuild editorial_ledger_summary.yaml and editorial_ledger_index.md.
blockers: []
commits:
  - pending: "[fix] ledger repair — rebuild active ledger from archive open items"
  - pending: "[audit] commit 4 uncommitted audit/design documents"
  - pending: "[editorial] register ~30 new flags from system audit + integration proposal"
open_items:
  existing_open: 42
  new_p1: [AUD-NPC-01, AUD-SET-02, AUD-DS-01, AUD-FP-01]
  new_p2: [AUD-COM-01, AUD-COM-04, AUD-SC-02, AUD-SC-03, AUD-TW-01, AUD-TW-02, AUD-MB-02, AUD-VIC-02, AUD-SET-01, AUD-SET-03, AUD-NPC-02, AUD-NPC-03, AUD-UI-01, AUD-UI-02]
  new_p3: [AUD-FW-02, AUD-MB-01, AUD-ST-01, AUD-VIC-01, AUD-CT-01, AUD-CH-01, AUD-INV-01, AUD-CK-01]
  blocking_integration: [B-1_DomainEchoTable, B-2_SceneSlateUnification, B-3_DialogueLatticeHandoff, B-4_StabilityTriggerCoupling, B-5_J7TerritoryScale]
  design_deliverables: [StartingScenarios, CampaignPortrait, LegendsMode, PostCalamityEra]
data_integrity_notes:
  - Active ledger was truncated in prior session (only 8 resolved entries remained)
  - Summary claimed ED-670-679 open; ED-673-679 actually resolved in archive
  - ED-670-672 and ED-698-703 permanently lost (6 IDs)
  - index_gen.py reported 0 entries (stale)
  - Do NOT close open entries without reading affected design doc to verify
  - 3 uploaded files already committed (integration_audit_v3, settlement_bridge, comprehensive_audit)

---

# Session Log — 2026-04-19
last_stage: TC→CI global rename + Warden sim + T9 TCV fix
next_action:
  skill: patch — resolve remaining CI conflicts (ceiling, seizure threshold/Ob, CI=100 event)
  description: >
    TC globally renamed to CI (Church Influence). T9 TCV fixed to 5.
    Warden emergence sim completed — mechanics work, NPC priority tree fixed.
    Uncontrolled reclaim sim completed — free march works, ED-704 raised (Seizure vs Uncontrolled).
    CI formula consistency verified. CI ceiling conflict (75 vs 100) still unresolved in design.
    6 design conflicts remain from tc_tcv_conflict_register (seizure threshold, Ob formula, CI=100 event, Church victory condition).
  blockers: [6 design decisions pending Jordan input]
commits:
  - 0b2d09e: sim Warden emergence + Uncontrolled reclaim + CI propagation
  - 44b3f10: TC→CI global rename (20 files) + T9 TCV=5 fix + file renames
  - pending: NPC priority tree fix + session log
P1-BLOCKER count: 0

---

session_id: 8052c04a7b7d8d2b
session_close: 2026-04-19
phase: 0
status: complete
last_stage: All 7 CI/PV/Seizure conflicts resolved and propagated
next_action:
  skill: editorial — remaining cleanup
  description: >
    All 7 conflicts from tc_tcv_conflict_register resolved.
    Remaining:
    1. Regenerate skeletons (victory_v30, ci_political_v30, military_layer_v30 all stale).
    2. Rebuild editorial_ledger_summary.yaml (stale).
    3. Rebuild editorial_ledger_index.md (stale).
    4. NPC priority tree pending commit from prior session log — verify if already committed.
    5. PV table in ci_political §1 still has old TCV numbers per-territory (T8=3 etc) — 
       the table was only header-renamed, values not updated to match victory_v30.
    6. params/bg/victory.md TCV table values still stale (T8=3, T9=3) — needs PV update.
  blockers: []
commits:
  - 9a1c890: resolve 7 conflicts in victory_v30 + 4 params files
  - 9515e4e: mark conflicts resolved in register + coverage matrix
  - a31cb7b: propagate to military_layer, campaign_architecture, ci_political
data_integrity_notes:
  - One-shot Mass Seizure replaces Graduated Seizure (PP-494 superseded)
  - Ob = 10 - PT - infrastructure (floor 1) replaces both 7-PT and 2+Fort+max(0,3-PT)
  - PV values T8/T12=4, T3/T14=3, total 35 (Crown 14, Hafenmark 7, Varfell 7, Church 5)
  - CI >= 60 threshold for Mass Seizure, CI caps at 100
  - Victory = Peninsular Sovereignty for all factions, CI is tool not win condition

---

session_id: 28f8f05e21dcc578
session_close: 2026-04-19
phase: 0
status: complete
last_stage: All cleanup items resolved — PV values, skeletons, summary, index
next_action:
  skill: confirm with Jordan
  description: >
    All handoff items from prior sessions resolved:
    - PV values propagated and total corrected (33, not 35)
    - 3 stale skeletons regenerated (victory_v30, ci_political_v30, military_layer_v30)
    - editorial_ledger_summary.yaml rebuilt (2 P1, 37 P2, 1 P3 = 40 open)
    - editorial_ledger_index.md rebuilt (40 entries)
    - Varfell P2b T15 march confirmed present
    - index_gen.py parser incompatible with list-format ledger (does not block — summary generated manually)
    Next priorities:
    - Fix index_gen.py _collect_ed_entries to handle list-format ledger
    - Register ~28 audit flags from prior sessions (source docs lost — may need re-audit)
    - Engine v3 tuning (faction AI expansion rate)
  blockers: []
commits:
  - b5c0370: PV values fixed (T12=4, T3=3, T14=3, total 33, starting PV corrected)
  - 97104f0: 3 skeletons regenerated + ledger summary/index rebuilt

---

session_id: 2026-04-19-engine-v3-rebuild-plus-canon-strikes
session_close: 2026-04-19
phase: 0
status: complete
last_stage: engine_v3.6 committed + workplan for v4 rebuild + VTM and Cultural Reformation struck from canon
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads of:
    mass_battle_v30, settlement_layer_v30, faction_layer_v30, faction_politics_v30,
    factions_personal_v30, npc_behavior_v30, params/bg/* (all 15+ files),
    threadwork_v30, calamity_radiation_v30, southernmost_v30.
    Output: tests/sim_framework/canon_audit.md listing every system + source +
    gap flag. Six gaps already flagged in workplan as editorial blockers:
    mine income rate, food vulnerability mechanic, Crown Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence.
    Phase 0 confirms whether these gaps are real or exist in canon sections
    not yet read. After audit, Phase 1 (substrate — territory graph + settlement
    sublayer + Calamity radiation state) starts. Do not touch engine_v3 until
    audit complete.
  blockers: []
commits:
  - 422fa07: Mass Seizure exponential declaration curve P=((CI-60)/40)^3.3 + supersession_check hook
  - 2e70d77: Engine v3.1 — 6 bug fixes + Warden emergence
  - 3f07396: Engine v3.2 — territory inheritance + LocalMilitia revolt + 0-territory elimination
  - f7aa0ed: Engine v3.3 — VTM struck from engine + RS seasonal decay
  - bc57b6c: Engine v3.4 — Church infrastructure buildup + heresy investigation + Hafenmark wealth
  - d225feb: Engine v3.5 — earlier Mass Seizure curve P=((CI-40)/60)^2.5 + elimination cascade
  - 297f892: Engine v3.6 — Cultural Reformation struck from engine + Varfell pure military
  - 13b8f30: Workplan for engine_v4 full rebuild from canonical game systems
  - 613ebf9: VTM + Cultural Reformation struck from canon — ED-706, ED-707
session_highlights:
  - Engine v3 went through 6 iterations. Final state at 297f892 has correct dice, CI, RS, territory inheritance, LocalMilitia revolt, exponential seizure curve. Still structurally wrong for rebuild (no geography, no settlements, no mass battles).
  - Supersession register infrastructure now live. canon/supersession_register.yaml + supersession_check hook in valoria_hooks.py fires during pre_commit_gate as non-blocking warning when commits touch flagged files. Verified live during commits 422fa07 and 613ebf9.
  - VTM struck — no canonical advancement mechanic existed, was placeholder. Varfell victory paths A/B/C + Cultural Reformation pool formula need rewrite (ED-706).
  - Cultural Reformation struck — Jordan clarified Vaynard is Reinhardt von Lohengramm parallel. Military conqueror, not ideological converter. Varfell expansion is purely military. Tribune intel remains, Thread operations remain as personal-scale actions. (ED-707)
  - Extensive faction identity canon review: Almud = best player at table playing defense on all fronts (weaponizes Einhir question, redirects threats into each other, wins late by absorbing wreckage). Baralta = iron personality + parliamentary prowess + mining wealth → best troops, food vulnerability. Vaynard = revolutionary southern Einhir, closest to Thread, hemmed in by fortresses. Himlensendt = true believer whose pastoral service drifts into theocracy. Caste system = binary (Einhir-heritage vs not), structurally load-bearing for NPC ecosystem.
  - Engine v3 is architecturally wrong. Has been building NPC-vs-NPC stat-comparison loop without player, scenes, zoom-in, actual mass battles, Thread operations, terrain, adjacency, settlement-level Church infrastructure, or geographic constraints. Correct dice/CI/RS mechanics but wrong faction model.
  - Workplan for engine_v4 full rebuild from game systems up, not from faction win-rate targets down. 6 phases, ~8 sessions.
open_items:
  - ED-706 VTM strike — Varfell victory paths A/B/C need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction_actions, Varfell ladder, NPC priority trees need rewrite (P2)
  - Six canon gaps flagged in workplan blocking parts of v4 rebuild (mine income rate, food vulnerability, Einhir suppression action, RM activation trigger, Thread ops in mass battle, subnational faction emergence)
  - coverage_matrix at 4537/5000 tokens — warning threshold
  - editorial_ledger at 1652/2000 tokens — warning threshold (after ED-706 and ED-707 added)
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1) — note: Path B itself pending rewrite after VTM strike
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)

---

session_id: 2026-04-19-provisional-mechanics-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-666 provisional mechanics arc test — 4 scenarios × 3 seeds, committed 6ea1f3e
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads of:
    mass_battle_v30, settlement_layer_v30, faction_layer_v30, faction_politics_v30,
    factions_personal_v30, npc_behavior_v30, params/bg/* (all 15+ files),
    threadwork_v30, calamity_radiation_v30, southernmost_v30.
    Output: tests/sim_framework/canon_audit.md listing every system + source +
    gap flag. Six gaps already flagged in workplan as editorial blockers:
    mine income rate, food vulnerability mechanic, Crown Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence.
    Phase 0 confirms whether these gaps are real or exist in canon sections
    not yet read. After audit, Phase 1 (substrate — territory graph + settlement
    sublayer + Calamity radiation state) starts.
    NOTE: Arc test surfaced 8 additional gaps in PP-666 mechanics — see
    tests/sim_framework/arc_test_results.md. Two design issues flagged:
    (1) Secession oscillation loop in fractional_province_ownership_v30 — needs cooldown.
    (2) Splinter viability at Mandate 1 unclear in faction_succession_split_v30.
    These should be resolved before PP-666 mechanics are canonized.
  blockers:
    - settlement_adjacency_map.yaml not authored — blocks adjacency mechanic canonization
    - fractional_province_ownership_v30 Secession cooldown gap — produces oscillation loop
commits:
  - 6ea1f3e: PP-666 arc test — 4 scenarios, 8 gap flags, secession loop + splinter viability issues
session_highlights:
  - Ran targeted simulation of three PROVISIONAL PP-666 mechanics: settlement_adjacency_v30,
    fractional_province_ownership_v30, faction_succession_split_v30.
  - Settlement adjacency fires correctly. Path-constrained invasion → partial capture →
    fractionalization works as designed.
  - Succession split produces meaningful seed-to-seed variance (clear vs narrow outcomes
    drive divergent arcs). RM backing interaction (+1 Influence on partial success) is
    well-designed.
  - Fractional province oscillation bug: no Secession cooldown in spec. Settlement
    seceeds → consolidates → seceeds in consecutive seasons indefinitely. Needs 2-season
    post-Consolidation cooldown added to fractional_province_ownership_v30.
  - Splinter faction at Mandate 1 is non-functional: collapses in ~4 seasons. Spec
    unclear whether splinter is "chaos token" or "durable rival".
  - Dominant emergent arc across all scenarios: RM ascent from Varfell political fracture.
    Vaynard dies → succession split → Eastern Varfell at Mandate 1 fails fragmentation
    checks → Grauwald/Oastad secede to RM → RM reaches Stage 3 by mid-game.
    This arc is mechanically grounded and design-intent-aligned but may be too fast
    (Stage 3 by S02 in degraded-Order scenarios).
  - Full seed-determinism in Arc 3 (no succession event) — dice pools too static,
    no real variance without high-variance events. Engine_v4 needs dynamic Influence.
  - Crown and Church are passive across all arcs. Expected for this simulation scope;
    confirms engine_v4 needs Crown suppression AI and Church Mass Seizure to be active actors.
open_items:
  - ED-706 VTM strike — Varfell victory paths A/B/C need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction_actions, Varfell ladder, NPC priority trees need rewrite (P2)
  - Six canon gaps from workplan (mine income rate, food vulnerability, Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence)
  - Eight new gap flags from arc test — see tests/sim_framework/arc_test_results.md
  - coverage_matrix at 4537/5000 tokens — warning threshold
  - editorial_ledger at 1652/2000 tokens — warning threshold
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1) — note: Path B itself pending rewrite after VTM strike
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
  - PP-666 fractional_province_ownership_v30 — Secession cooldown gap (new, from arc test)
  - PP-666 faction_succession_split_v30 — splinter viability at Mandate 1 unclear (new, from arc test)
  - PP-666 settlement_adjacency_map.yaml — not authored, blocks canonization (new, from arc test)

---

session_id: 2026-04-19-batch2-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-666 arc test Batch 2 — 5 variants, bugs fixed, committed acfe32d
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads listed
    in the workplan. Output: tests/sim_framework/canon_audit.md.
    NOTE: Three spec fixes now required before PP-666 mechanics can be
    canonized — see tests/sim_framework/arc_test_batch2_results.md.
  blockers:
    - PP-666 spec fix 1: fractional_province_ownership §2.6 — RM→RM Secession candidate bug
    - PP-666 spec fix 2: faction_succession_split §4 — RM emergence threshold Order=0 clarification
    - PP-666 spec fix 3: faction_succession_split §2.4 — splinter Influence split decision required
commits:
  - acfe32d: arc test batch 2 — 5 variants, 3 sim bugs fixed, 5 design findings, 3 spec fixes
session_highlights:
  - Batch 2 ran 5 design variants against Batch 1 findings. Three sim bugs fixed first:
    (1) RM Inf incrementing on RM→RM no-op seceessions; (2) same-season Consolidation
    race overwriting just-seceeded settlements; (3) succession triggers not firing due
    to session state loss.
  - B2-1 (secession cooldown): cooldown fix has zero effect. Root cause was wrong —
    oscillation is RM→RM secessions on already-RM settlements, not Consolidation churn.
    Spec fix needed: Secession candidates must be restricted to national-faction-held
    settlements (not subnational/RM).
  - B2-2 (RM emergence threshold): Order=0 is correct. Order<=1 produces deterministic
    RM growth (7 settlements, low variance). Order=0 produces 4-5 settlements with genuine
    seed variance and RM growing via political leverage (succession split momentum) rather
    than settlement accumulation — matches design intent.
  - B2-3 (splinter Mandate floor): floor has zero effect. Splinter Influence is unsplit
    (spec §2.4 explicitly). Mandate floor is not the survival lever. Design decision needed:
    split Influence 60/40 same as Mandate if durable rival splinters are intended.
  - B2-4 (Crown suppression): suppression AI backfires. Spending Influence on Ob+1 to
    fragmentation checks adds Ob to Crown's OWN province defense, not rivals'. Crown PV
    drops from 20.0 to 18.2 (seed 42). Crown Influence exhausted by S05. Suppression
    cannot be modeled as fragmentation Ob modifier — needs Mandate/Influence drain on
    target faction in engine_v4 Phase 4 political AI.
  - B2-5 (mutual fractionalization): most interesting arc. Hafenmark-Varfell cold-war
    standoff where both hold stakes in each other's territory. Less RM growth than
    single-fractionalization. T13 fractionalizes as secondary effect of distracted Varfell.
    Consider treaty mechanic for diplomatic resolution of mutual fractionalization.
open_items:
  - ED-706 VTM strike — Varfell victory paths need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction actions need rewrite (P2)
  - Six canon gaps from workplan (mine income, food vulnerability, etc.)
  - PP-666 spec fix 1: fractional_province_ownership §2.6 Secession candidates restriction
  - PP-666 spec fix 2: faction_succession_split §4 RM emergence threshold Order=0
  - PP-666 spec fix 3: faction_succession_split §2.4 splinter Influence split decision
  - PP-666 settlement_adjacency_map.yaml still not authored
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)

---

session_id: 2026-04-19-batch3-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: arc test batch 3 — CI/seizure, RS decay, Fort, IP/Vanguard, suppression race — committed 8088bc3
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0. Workplan at tests/sim_framework/workplan_rebuild_2026-04-19.md.
    Phase 0 is a canon audit — no engine changes. Produce tests/sim_framework/canon_audit.md.
    Batch 3 surfaced 7 new gaps to add to audit checklist.
  blockers:
    - PP-431-COR not modeled correctly in B3-5 suppression race; re-run needed
    - AER generation mechanic not found in any doc; blocks Vanguard resolution path
commits:
  - 8088bc3: arc test batch 3 — CI/seizure, RS decay, Fort constraint, IP/Vanguard, suppression race
session_highlights:
  - B3-1 (CI/Seizure): Seizure fires S10-15 at CI 78-100. Hafenmark suppression delays ~2 seasons.
    Piety Yield at T9 (SW5, PT5) = +6/season, exceeds ±5 cap. Assert is irrelevant once T9 PT
    is maximized. Church Stability collapses from unnecessary Assert failures.
  - B3-2 (RS decay): Fully deterministic — no dice variance. Active war (2 battles/s): RS hits 79
    at S11, 59 at S21, Vanguard deploys S19. Campaign-scale warfare produces Rupture at S25.
    Proximity gradient working correctly. Warden emergence at S30 in active-war scenario.
  - B3-3 (Fort constraint): T14 Fort3 is an absolute wall (Varfell 4d vs Ob 6 = expected Failure).
    Route A (T2, no fort) is too easy — T2 is ungarrisoned and Varfell reaches it S1-5.
    Route C (Askeheim) functionally equivalent to Route A at high RS.
    T2 garrison needs to be Crown default behavior (priority tree gap).
  - B3-4 (IP/Vanguard): AER4 provides only ~1 season delay on Vanguard. AER5 is the only real
    counter. Coalition cannot stop Vanguard militarily — needs non-military resolution. Vanguard
    reaches T1 within 5-6 seasons of deployment. Campaign arc shape confirmed: expansion S1-10,
    Church seizure S10-14, Vanguard crisis S19-24, Warden emergence S24-30.
  - B3-5 (Suppression race): Structural suppression alone insufficient. Parliamentary Challenge
    adds 0-7 season variance. PP-431-COR not modeled (Challenge should replace structural, not
    supplement it) — re-run needed. Piety Yield dominates; Assert/Suppress minigame is mechanically
    irrelevant above PT3 at T9.
  - Campaign arc shape: Three-act structure emerges naturally from mechanical interactions.
    Expansion (S1-10) → Crisis/Seizure (S10-20) → External pressure/endgame (S20-30).
open_items:
  - ED-706, ED-707 (VTM/Cultural Reformation rewrites, P2)
  - Six workplan gaps (mine income, food vulnerability, Einhir suppression, RM trigger, Thread in battle, subnational emergence)
  - PP-666 spec fixes (3 from Batch 2)
  - B3-5 re-run needed with PP-431-COR correctly modeled (Challenge replaces structural suppression)
  - GAP: CI seasonal cap vs Piety Yield — Assert irrelevant at T9 PT5; design review needed
  - GAP: AER generation mechanic — not found in any read doc
  - GAP: T2 Kronmark garrison — Crown priority tree gap
  - GAP: Warden emergence mechanics post-RS40 — not specified beyond appearance trigger
  - GAP: Campaign-scale vs standard battle distinction — not canonically defined
  - ED-671, ED-666, ED-667, ED-632, ED-633, ED-629, ED-663 (P1 blockers, carried forward)

---

session_id: 2026-04-19-batch4-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: arc test batch 4 — PI/RDT/TD/Accord/Coup — committed d195dbc
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0. Workplan at tests/sim_framework/workplan_rebuild_2026-04-19.md.
    Phase 0 canon audit, produce tests/sim_framework/canon_audit.md.
    Batch 4 added 6 new gap flags. Notable: T9 PT=5 at game start changes B3-1
    findings (CI hits cap from S1). Coup triggers PI collapse to 0 permanently.
  blockers:
    - T9 PT=5 at game start (canonical) — B3-1 seizure timing results need revision
    - Coup Counter advancement sources not in any read doc
commits:
  - d195dbc: arc test batch 4 — PI track, RDT/TD, Accord revolt, Löwenritter Coup
session_highlights:
  - B4-1 (PP-431-COR fix): Corrected model produces S12-S18 variance vs S12-S14 structural-only.
    Challenge is a situational tool (play near CI thresholds), not a blanket every-season strategy.
    T9 PT=5 at game start discovered — B3-1 used wrong PT values; Piety Yield hits cap from S1.
  - B4-2 (PI track): PI is structurally net-positive under Hafenmark pressure. PI never reaches
    NonFunctional (≤2) without the Coup. PI drifts to 15+ over 30 seasons. Upper-band effects
    (Crown Policy M≥4) trivially met by Crown M=5. PI track needs either higher-frequency loss
    sources or more meaningful ceiling effects.
  - B4-3 (RDT/TD): CI60 fires at S8 in every seed (T9 PT=5 canonical). TD4 (Ob+2 at HF territories)
    not reached until S20 — after first Seizure attempt. TD5 (T8 permanently unseizable) fires S24.
    RDT/TD is a viable long-game defensive path for Hafenmark, but the first 12 seasons are exposed.
    Seizure Failure consequences (Stab-1 + Casus Belli) not tracked — gap for engine_v4.
  - B4-4 (Accord revolt): Strain hits Collapse (10) by S4-5 under 2 battles/season. Cascade driven
    by garrison coverage, not battle intensity. Recovery path absent under sustained conflict.
    Treaty mechanic (-1 Strain from diplomatic resolution) not modeled — key missing piece.
  - B4-5 (Löwenritter Coup): PI collapses to 0 immediately post-coup and stays there permanently.
    PI=0 gives Church CI+2/season but this is largely redundant past CI80. Real consequence is
    permanent loss of Parliament as Hafenmark tool. Paradox: Coup accelerates Church victory —
    Crown must prevent the Coup to avoid enabling Church. Post-coup board (Löwenritter at T14 Fort3
    Mil6, PI=0, CI accelerating) is the richest player decision space in the design.
    Coup Counter advancement sources and Coup effect on Crown Mandate are unspecified gaps.
open_items:
  - B3-1 results need revision — T9 PT=5 canonical, not PT=1 as assumed; CI hits cap S1
  - ED-706, ED-707 (P2 rewrites)
  - PP-666 spec fixes (3 from Batch 2)
  - B3-5 suppression race already rerun as B4-1 (PP-431-COR corrected)
  - GAP: T9 PT=5 at start — Piety Yield hits cap from S1; Assert irrelevant immediately
  - GAP: Coup Counter advancement sources not in read docs
  - GAP: Coup effect on Crown Mandate not canonical
  - GAP: Seizure Failure consequences (Stab-1 + Casus Belli) not modeled in any sim
  - GAP: Treaty mechanic interaction with Strain not modeled
  - GAP: PI track upper-bound effects need design review
  - All prior open items carried forward

---

session_id: 2026-04-19-sim-batches-ignition-architecture
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Pass 1 cleanup complete — supersession banners + coverage index. Conflict architecture proposal committed.
next_action:
  skill: Pass 2 Session A — structural foundation specs
  description: >
    Write three-scale resolution model (settlement→province→peninsula) into phases.md or
    settlement_layer_v30. Write bishop appointment action into faction_actions.md + propagate
    to settlement_layer §3.2, ci_seizure.md, npc_behavior §8.2 Church tree. Write PP-666
    spec patches (secession candidate restriction, RM Order=0 threshold). Flag splinter
    Influence split for Jordan design decision.
  blockers:
    - Jordan design decision: splinter Influence split (60/40 or unsplit)
    - Jordan design decision: CI cap vs Piety Yield at T9 (reduce SW or raise cap)
    - Jordan design decision: T2 garrison in Crown priority tree (explicit or accept exposure)
    - Jordan design decision: Almud's father assassination — strike backstory or make live
commits:
  - 6ea1f3e: B1 arc test — PP-666 provisional mechanics, 4 scenarios
  - acfe32d: B2 arc test — 5 design variants, 3 sim bugs fixed
  - 8088bc3: B3 arc test — CI/seizure, RS decay, Fort, IP/Vanguard, suppression race
  - d195dbc: B4 arc test — PI track, RDT/TD, Accord revolt, Löwenritter Coup
  - c5be6fc: early-game ignition analysis (historical precedents, Tensions Deck v1)
  - db953eb: session audit — 7 issues, 20 gaps consolidated
  - 2494e7a: conflict architecture proposal — unified design (3-scale model, bishop appointment,
              graduated autonomy, Niflhel dissolved, Tensions Deck rescoped)
  - ab0365d: Tensions Deck pair validation — 15/15 pass (revised to 6 external bilateral cards)
  - de8769d: Pass 1 cleanup — supersession banners on B1/B3/ignition + sim coverage index
session_highlights:
  - 4 sim batches tested 18 mechanical systems across 20+ scenarios. 20 gap flags surfaced.
    3 spec patches ready. 4 design decisions flagged for Jordan.
  - Core finding: the game already starts on fire — 5 provinces have non-aligned settlements
    at game start. Settlement governance friction IS the ignition system. No new mechanic needed
    for early-game conflict; only recognition that fragmentation checks fire from S1.
  - Three-scale model: Peninsula (victory) → Province (contest) → Settlement (engine). Control
    flows up, pressure flows down. Settlement resolves first each season.
  - Church expansion: bishop appointment action (Ob 1 where Church building ≥ tier 2) gives
    Church a settlement-level territorial path independent of CI timer. Mass Seizure becomes
    formalization of settlement-level reality, not the primary expansion mechanic. Geneva trap:
    factions accept Church infrastructure for Stability bonus → Church claims governance later.
  - Graduated Löwenritter autonomy (4-stage) replaces binary coup. Autonomous stage (de facto
    independent, de jure loyal) is the richest game state.
  - Niflhel struck as faction. Functions distributed to settlement phenomena: black markets
    (Order ≤ 1), intelligence brokers (settlement NPCs), Thread exploitation sites (locations).
  - Tensions Deck: 6 external bilateral cards, draw 2 at game start. Each card is a fuse
    (S0 seed → S8+ fire). Factions: each appears in exactly 3 cards. 15/15 pairs validated
    against belligerent-target-opportunity criteria. Internal tensions (Löwenritter autonomy,
    Guild instability, RM emergence) are emergent downstream of external pressures, not forced.
  - Royal assassination: fuse model (S8+ fire, succeed-on-fire). 3 targets produce 3 different
    mid-games: Lenneth dead → Almud revenge; Torben dead → Elske retrieval/Altonian provocation;
    Almud dead → Lenneth inverts Crown identity (pro-Thread, pro-Einhir).
  - Pass 1 cleanup complete: supersession banners on 3 docs, sim coverage index created with
    reading order + supersession map + consolidated gap list + campaign arc timeline.
open_items:
  - Pass 2 Session A: three-scale model spec, bishop appointment, PP-666 patches
  - Pass 2 Session B: graduated Löwenritter autonomy, Niflhel dissolution
  - Pass 2 Session C: Tensions Deck spec, Royal assassination fuse detail
  - 4 Jordan design decisions pending (splinter Influence, CI cap, T2 garrison, father backstory)
  - 7 unspecified systems (AER, Warden behavior, campaign battle scale, Coup advancement,
    Coup→Mandate, Seizure failure chain, treaty→Strain)
  - 6 data gaps (adjacency map, fractional stake disposition, contender pools, RM disposition,
    consolidation Influence, PI upper-bound)

---

session_id: 2026-04-19-session-a-spec-patches
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Session A spec patches written (7 patches). Propagation into target files deferred to fresh session.
next_action:
  skill: Session A propagation — apply patches to target files
  description: >
    Apply 7 patches from designs/architecture/session_a_spec_patches.md into their target files.
    Patches 1-6 are ready (exact text provided). Patch 7 (backstory strike) requires full reads
    of character_histories_v30, npc_character_analyses_v30, worldbuilding_v30 to find and modify
    specific passages. Then Session B (graduated Löwenritter autonomy, Niflhel dissolution).
  blockers:
    - editorial_ledger.yaml at 1698/2000 tokens — needs archival before more EDs added
    - Jordan design decision still pending: CI cap vs Piety Yield at T9
commits:
  - 1581cde: Session A spec patches — 3-scale model, bishop appointment, 3 PP-666 patches, T2 garrison, backstory strike
session_highlights:
  - 7 spec patches written and committed as consolidated document ready for propagation.
  - Jordan decisions resolved: splinter Influence 60/40 split, T2 small garrison, strike father assassination backstory.
  - CI cap vs Piety Yield explained to Jordan — awaiting decision (reduce T9 SW or raise cap).
  - editorial_ledger at warning threshold (1698/2000) — needs archival batch.
open_items:
  - Propagate patches 1-6 into target files (phases.md, faction_actions.md, settlement_layer_v30,
    ci_seizure.md, npc_behavior_v30, fractional_province_ownership_v30, faction_succession_split_v30,
    npc_priority_trees.md)
  - Propagate patch 7 (backstory strike) after full reads of character/worldbuilding docs
  - Session B: graduated Löwenritter autonomy + Niflhel dissolution
  - Session C: Tensions Deck 6 cards + Royal assassination fuse
  - CI cap vs Piety Yield — Jordan design decision pending
  - editorial_ledger archival needed

---

session_id: 2026-04-19-throughlines-framework
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-674 framework enforcement + tier N committed; framework now mandatory validation tool
next_action:
  skill: framework-use
  description: >
    Apply vetting framework to next design proposal. First real test candidates:
    Hafenmark/Löwenritter/RM institutional-attractor throughlines (closes ED-717
    M-4 gap). Workflow: task_gate('design_proposal') → classify per §8.1 →
    vetting chain per class → produce vetting: block → safe_commit invokes
    vetting_gate. Class C/D/E remain lightweight; Class A/B require full block.
  blockers:
    - Jordan decision: address ED-717 Hafenmark/Löwenritter/RM factions one-at-a-time or joint proposal
    - Jordan decision: retroactive canon audit timing (deferred until engine_v4 smoke-test data available)
commits:
  - 193d5ee: PP-664 VTM residual cleanup
  - d7c5f20: PP-665 Yrsa Vossen rename
  - c3de2ef: PP-666 three new systems (settlement adjacency, fractional ownership, succession split)
  - 2fd00f0: PP-667 gap sweep
  - b0dfcef: PP-668 OPEN ITEMS propagation
  - 53f7c5b: PP-669 skeleton freshness
  - 80294a3: PP-670 label audit + ED-716
  - 8498e97: PP-671 throughlines meta-synthesis + ED-717
  - 03da060: PP-672 throughlines hierarchical framework (canonical vetting guide) + ED-718
  - f2f3efe: PP-673 terminology cleanup (skeleton→index for auto-gen) + ED-719
  - 3fab28a: PP-674 framework enforcement + tier N (Necessity Test) + ED-720
session_highlights:
  - Canonical vetting framework adopted. Five tiers (N, Ω, Μ, М, Τ, Q, Μ̄) with scope classification (A-E), rating rubric (+/✓/−/○), 15-term Failure Lexicon. Skeleton/infill split for load efficiency.
  - Tier N (Necessity) added above Ω. Subject-grounding check against Renaissance-era political-leadership dynamics. Codifies user constraint that Valoria's complexity is earned only when modeling load-bearing historical dynamics, not added for its own sake.
  - Framework enforcement landed as vetting_gate() hook. Class A/B patch entries from PP-674 forward require vetting: block with class/necessity/omega/mu/m_ratings/q keys. Enforced at commit time and by CI. Grandfathering via pre-framework true.
  - Terminology collision resolved. "skeleton" now reserved for canonical rulesets in mechanical-spec-only style. Auto-generated heading/line/token companions renamed from *_skeleton.md to *_index.md. tools/skeleton_gen.py renamed to tools/doc_index_gen.py. 75 files renamed, 8 code/skill files migrated.
  - Meta-throughlines synthesis produced 6 structural patterns covering all 25 T-throughlines with primary/secondary tagging. М-3 and М-4 audit corrections applied (T-05 removed from М-3 conflation; T-18/T-19 split to М-2 geography from М-1 decay).
  - Hafenmark/Löwenritter/RM institutional-attractor gaps persist (ED-717). М-4 vetting of faction proposals involving them defaults to undefined baseline until own T-throughlines added.
  - PP-666 three systems validated against framework retroactively. Settlement adjacency, fractional province ownership, faction succession split all pass N (load-bearing Renaissance dynamics) and pass multiple М extensions.
open_items:
  - ED-717 (Hafenmark/Löwenritter/RM substrate-posture gaps) — persists; M-4 defaults to undefined baseline until resolved
  - Retroactive canon audit — deferred until engine_v4 smoke-test load-bearing data
  - Sparse throughline-interaction matrix — 7 of 25 throughlines have mapped cross-interactions; 18 unmodeled
  - Three sim_ttrpg_batch_legacy files with filename-only labels — low-priority, deferred (PP-670 note)
  - Skeleton-staleness no CI regeneration — skeletons (canonical rulesets) drift when canonical changes; no automated check currently

---

---
session_id: session_a_propagation
session_close: 2026-04-19
phase: patch
status: CLOSED
last_stage: All 7 Session A patches propagated into target files.
next_action:
  skill: design
  description: >
    Session B — graduated Löwenritter autonomy + Niflhel dissolution.
    Session C — Tensions Deck 6 cards + Royal Crisis assassination fuse.
blockers:
  - editorial_ledger.yaml at 1698/2000 tokens — needs archival
  - CI cap vs Piety Yield at T9 — Jordan design decision pending
commits:
  - e89d196: Patches 1-6 propagated (8 target files)
  - 7da338a: Patch 7 backstory strike (3 files)
  - 677dc25: Checklist 1-6 DONE
  - 6c2e6f1: Checklist 7 DONE
open_items:
  - Session B: Löwenritter autonomy + Niflhel dissolution
  - Session C: Tensions Deck + Royal Crisis fuse
  - editorial_ledger archival

---

session_id: 2026-04-19-session-b-niflhel-lowenritter
session_close: 2026-04-19
phase: 0
status: partial — Session B core done, secondary propagation + Session C remain
last_stage: Session B core propagation — Niflhel dissolution + Löwenritter graduated autonomy in primary canonical files
next_action:
  skill: Session B completion + Session C
  description: >
    Session B secondary propagation (see remaining items below), then
    Session C: Tensions Deck 6-card spec + Royal assassination fuse.
  blockers:
    - Jordan design decision still pending: CI cap vs Piety Yield at T9
commits:
  - f8dafe0: Niflhel dissolution — params strike (core, stats_1_7_scale, npc_priority_trees)
  - 1fdc160: Niflhel dissolution — T-10 struck (throughlines_complete, registry, meta, meta_infill)
  - 747adcd: Niflhel dissolution — npc_behavior_v30 (§2.12, §8.8, §8.8a struck; scattered refs updated)
  - c0be619: Löwenritter graduated autonomy — Coup Counter replaced (core, institutions, clock_registry)
  - f6b6ae6: Löwenritter graduated autonomy — npc_behavior_v30 (§8.7, §7.5, arc refs updated)
  - d78d7b9: Niflhel dissolution — settlement_layer_v30 §4.7-4.9 (black markets, intelligence brokers, Thread exploitation sites)
session_highlights:
  - Niflhel dissolved across primary canonical files. Faction stat blocks, priority trees, T-10 throughline struck. Replacement settlement-level phenomena (black markets §4.7, intelligence brokers §4.8, Thread exploitation sites §4.9) added to settlement_layer_v30.
  - Löwenritter graduated autonomy (4-stage Loyal/Restless/Autonomous/Split) replaces binary Coup Counter in core params, institutions, clock_registry, and npc_behavior_v30. Reversible at stages 1-3.
  - М-4 throughline count updated 5→4 (T-10 struck). Distribution now М-1:4 М-2:2 М-3:3 М-4:4 М-5:6 М-6:5.
  - conflict_architecture_proposal.md content treated as canon per Jordan directive.
open_items:
  - Session B secondary propagation:
    - npc_roster_v30.md — convert Quartermaster/Quiet One NPCs to independent settlement-tied actors
    - baralta_crown_claim_v30.md — Coup Counter → graduated autonomy refs
    - victory_v30 — Coup references update
    - params/bg/victory.md — Coup references update
    - designs/arcs/* — scattered Niflhel/Coup refs in arc files (arcs_31_35, arc_expansion, emergent_campaign_arcs)
    - factions_personal_v30 — Niflhel personal-scale refs
    - params/bg/npcs_special.md — Niflhel NPC entries
    - npc_behavior_v30.md — 8 incidental Niflhel refs remaining (table entries, not mechanical definitions)
    - conflict_architecture_proposal.md — update status from PROPOSAL to CANON
    - ED-667 (Coup Counter readiness gap) — likely resolved by graduated autonomy; verify and close
  - Session C:
    - Tensions Deck 6-card spec (from conflict_architecture_proposal) — write into params or architecture file
    - Royal assassination fuse spec (3 targets: Lenneth/Torben/Almud) — write into params or architecture
    - Propagate to npc_behavior_v30, campaign_architecture_v1, and relevant arc files
  - Patch 7 from Session A (backstory strike) — needs full reads of character_histories_v30, npc_character_analyses_v30, worldbuilding_v30
  - Session log was stale (still showed PP-674 session) — this close updates it
  - Index regeneration needed for modified files
  - ED-717 (Hafenmark/Löwenritter/RM substrate-posture gaps) — original task; blocked until Session B/C complete
  - CI cap vs Piety Yield at T9 — Jordan design decision pending
P1-BLOCKER count: 2
