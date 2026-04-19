
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
