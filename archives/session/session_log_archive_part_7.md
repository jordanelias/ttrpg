
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

---

session_id: 2026-04-19-session-bc-completion
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Session B + C propagation — Niflhel dissolution, Löwenritter graduated autonomy, Tensions Deck, Royal assassination
next_action:
  skill: Session B/C residual cleanup, then ED-717
  description: >
    Residual propagation: arc files with incidental Niflhel/Coup refs,
    assassination target NPC arc profiles in npc_behavior_v30, Patch 7
    backstory strike. Then ED-717 (Hafenmark/Löwenritter/RM substrate-posture
    throughlines, one at a time starting with Hafenmark).
  blockers:
    - Jordan design decision still pending: CI cap vs Piety Yield at T9
commits:
  - f8dafe0: Niflhel dissolution — params strike (core, stats_1_7_scale, npc_priority_trees)
  - 1fdc160: Niflhel dissolution — T-10 struck, М-4 count 5→4 (throughlines)
  - 747adcd: Niflhel dissolution — npc_behavior_v30 §2.12/§8.8/§8.8a struck
  - c0be619: Löwenritter graduated autonomy — Coup Counter replaced (core, institutions, clock_registry)
  - f6b6ae6: Löwenritter graduated autonomy — npc_behavior_v30 §8.7/§7.5 updated
  - d78d7b9: Niflhel dissolution — settlement_layer_v30 §4.7-4.9 (black markets, brokers, exploitation sites)
  - 6e952c3: conflict_architecture_proposal PROPOSAL→CANON, Coup→Autonomy in victory + baralta_crown_claim
  - 3cfa81f: Dalla Virke→independent broker, npcs_special Niflhel→settlement refs
  - d29d8b6: Tensions Deck 6-card spec + Royal assassination fuse spec (new params files)
  - 238cf45: Game Setup section in phases.md (Tensions Deck draw, starting settlements)
session_highlights:
  - Session B complete (10 commits across 2 context windows). Niflhel fully dissolved in primary canonical files — faction stats, priority trees, T-10 throughline, NPC sections all struck. Replacement settlement phenomena (black markets, intelligence brokers, Thread exploitation sites) canonized in settlement_layer_v30 §4.7-4.9.
  - Löwenritter graduated autonomy (4-stage Loyal/Restless/Autonomous/Split) replaces binary Coup Counter across all primary params, institutional docs, clock registry, and NPC behavior trees.
  - conflict_architecture_proposal.md elevated from PROPOSAL to CANON per Jordan directive.
  - Session C complete. Tensions Deck 6-card spec (params/bg/tensions_deck.md) and Royal assassination fuse (params/bg/royal_assassination.md) extracted as standalone canonical params. Game Setup section added to phases.md.
  - М-4 throughline count corrected 5→4 (T-10 struck). Remaining М-4 throughlines: T-08 (Church rendering reinforcement), T-09 (Varfell thread progressive), T-11 (Crown pragmatic instrumentalist), T-21 (Thread political warfare).
open_items:
  - Residual Niflhel/Coup refs in arc files (arcs_31_35, arc_expansion, emergent_campaign_arcs, factions_personal_v30) — incidental, not mechanical definitions
  - npc_behavior_v30 — 8 incidental Niflhel refs remaining in table entries; ~4 natural-language coup refs
  - Assassination target propagation to NPC arc profiles (Almud Arc A/B/C, Lenneth, Torben)
  - Patch 7 backstory strike (Session A) — needs full reads of character_histories_v30, npc_character_analyses_v30, worldbuilding_v30
  - ED-667 (Coup Counter readiness gap) — resolved by graduated autonomy; needs formal closure
  - Index regeneration for all modified files
  - ED-717 (Hafenmark/Löwenritter/RM substrate-posture gaps) — ready to start after cleanup
  - CI cap vs Piety Yield at T9 — Jordan design decision pending
P1-BLOCKER count: 2

---

session_id: 2026-04-19-session-bc-residual-and-ed717-hafen
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Session B/C residual propagation complete; ED-717 Hafenmark arm done (1 of 3)
next_action:
  skill: ED-717 Löwenritter arm, then RM arm
  description: >
    Propagate T-15b (Löwenritter Substrate-Agnostic Protector) into
    factions_personal_v30 §8.9. Then T-15c (RM Substrate-Heritage
    Reclaimer) into §8.8. Both framework definitions already exist in
    references/throughlines_meta_infill.md §3.1. Pattern: follow the
    Hafenmark §8.4 Substrate-Posture subsection added 2026-04-19 (commit
    2246887e). After both arms done, close ED-717 in ledger.
  blockers:
    - Jordan design decision still pending: CI cap vs Piety Yield at T9
blockers:
  - Jordan design decision still pending: CI cap vs Piety Yield at T9
commits:
  - 148d0184: emergent_campaign_arcs — post-Session-B/C note
  - fc9eea27: arcs_31_35 — post-Session-B/C note
  - bdf8a6a2: arc_expansion_v30 — banner + strike NIFLHEL operatives + strike LR-Niflhel proximity
  - bacb0519: factions_personal_v30 — strike §8.7 Niflhel + 7 incidental refs
  - 932078fa: npc_behavior_v30 — 7 incidental Niflhel/Coup refs updated (Löwenritter graduated autonomy language)
  - 818b5c87: Royal assassination fuse propagation — Almud Arc D/E/F; Torben §2.8; Lenneth §2; Elske §4
  - 8ff353d3: Patch 7 / Session B residual — strike Niflhel vocations, rename Ehrenwall Coup card → Ehrenwall Split
  - 89b57726: Close ED-667 (Coup Counter readiness gap) + ED-600 (Niflhel named operatives)
  - d393a220: Regenerate indexes for 6 docs (arc_expansion, factions_personal, npc_behavior, npc_character_analyses, character_histories, worldbuilding)
  - 2246887e: ED-717 Hafenmark arm — §8.4 Substrate-Posture subsection (T-15a) + infill update + ledger progress
  - 76ed3bf8: Regenerate factions_personal_v30 index (final)
P1-BLOCKER count: 2

---

session_id: 2026-04-19-resolve-all
session_close: 2026-04-19
phase: 0
status: complete
last_stage: All deliverable items resolved — ED-717 fully closed, ED-632/633 PROVISIONAL specs, ED-721 CI cap decision formalized (default Option A)
next_action:
  skill: Jordan approvals + remaining P2 ledger items
  description: >
    Three items await Jordan sign-off: (1) approve or amend the PROVISIONAL
    Shadow Renown spec (faction_politics_v30 §2.2b.i); (2) approve or amend
    the PROVISIONAL Deniability Debt spec (faction_politics_v30 §2.2b.ii);
    (3) decide ED-721 — CI cap vs Piety Yield at T9 — Option A (default,
    applied), B (T9 bypasses cap), or C (half-contribution). Remaining
    open P2 items in editorial_ledger.yaml (~40 entries) can be worked
    per priority at Jordan's direction.
  blockers: []
blockers: []
commits:
  - 38ab83a0: ED-717 Löwenritter + RM arms — Substrate-Posture subsections (T-15b §8.9, T-15c §8.8); ED-717 fully closed
  - 4271b084: ED-632 Shadow Renown + ED-633 Deniability Debt — PROVISIONAL mechanical specs in faction_politics_v30 §2.2b
  - 8d911ef5: ED-721 — CI cap vs Piety Yield at T9 formalized (Jordan decision pending; default Option A applied)
  - 39d7f85e: Regenerate indexes for 3 docs
P1-BLOCKER count: 0

---

session_id: 2026-04-19-approve-all-and-simready
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Approvals landed (ED-632/633/721 canonized); canonical_sources.yaml systems: block populated; full campaign simulation readiness report published
next_action:
  skill: Write automated full-campaign Python simulation harness
  description: >
    Design (§5 of tests/sim/campaign_simulation_readiness_2026-04-19.md)
    is complete with 17/17 full_stack systems canonically mapped and zero
    P1 blockers. Remaining work is engineering: (1) valoria_full_campaign_sim.py
    orchestrator covering the seasonal loop, all 17 systems, and scale
    transitions; (2) /home/claude/sim_verification_ledger.json mapping
    every mechanical constant to canonical source (per sim_gate); (3) test
    corpus of deterministic seeds for variant scenarios (RM-led, Church-
    dominant, Löwenritter split, Varfell conquest, Thread revelation).
    Estimated scope: 2-4 focused sessions. Not blocked by any design gap.
  blockers: []
blockers: []
commits:
  - 13c646fb: Canonize ED-632/633 (Shadow Renown + Deniability Debt) + ED-721 Option A (CI cap uniform at T9)
  - 393e76e3: Populate canonical_sources.yaml systems block (17 full_stack + 6 supporting)
  - ffc00895: Full campaign simulation readiness report published (tests/sim/campaign_simulation_readiness_2026-04-19.md)
P1-BLOCKER count: 0
design_complete: true
sim_harness_complete: false

---

session_id: 2026-04-19-sim-session-1
session_close: 2026-04-19
phase: 0
status: active
last_stage: Sim Session 1 foundation committed (129f2f2b); checkpoint acc07c85 written at 75% context
next_action:
  skill: Resume from canon/session_checkpoint.md — execute Session 2 Middle Layer
  description: >
    See canon/session_checkpoint.md for full Session 2 scope. Summary: add
    territory model (T1-T15), Domain Action framework with 6+ canonical DAs,
    Piety Yield/CI political pool, Peninsular Strain propagation, simplified
    mass combat and contest, faction AI stub, then 40-season smoke test with
    real DAs. All Session 1 ledger entries at /home/claude/sim_verification_ledger.json.
  blockers: []
blockers: []
commits:
  - 129f2f2b: Session 1 foundation — core engine + clocks + factions + seasonal loop (10-season smoke PASS)
  - acc07c85: Checkpoint — Session 1 done, Session 2 pending
P1-BLOCKER count: 0
design_complete: true
sim_harness_session_1_complete: true
sim_harness_session_2_complete: false
sim_harness_session_3_complete: false

---

session_id: 2026-04-19-sim-all-sessions
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Full campaign simulation harness complete (Sessions 1+2+3); 8-seed deterministic corpus PASS
next_action:
  skill: Tier A conquest loop (mass combat + territory seizure + Peninsular Sovereignty reachable)
  description: >
    The sim runs end-to-end but no faction can conquer another's territory
    yet, so Peninsular Sovereignty is unreachable in simulation. Tier A
    adds mass_battle_v30 resolution, Church CI=60+ TC Seizure DA, Crown
    military occupation, territory control changes with Accord damage.
    After Tier A: factions can win via Peninsular Sovereignty and we can
    measure win-rate distributions across seeds. See
    tests/sim/campaign_simulation_readiness_2026-04-19.md §5 for full
    Tier A/B/C scope.
  blockers: []
blockers: []
commits:
  - 129f2f2b: Sim Session 1 — foundation (core engine, clocks, factions, seasonal loop)
  - 99b469cf: Sim Session 2 — territory model + DA framework + Piety Yield + faction AI
  - 6264e685: Sim Session 3 — victory + Tensions Deck + Royal Assassination + Threadwork + 8-seed corpus
P1-BLOCKER count: 0
design_complete: true
sim_harness_complete: true

---

# SESSION LOG: 2026-04-20 ATOMIZATION RUN
## Status: ACTIVE — atomization workplan complete; minor follow-ups remain

last_stage: Atomization workplan 2026-04-20 — Batches 0/1/2/3/4/5§5.1+§5.2+§5.4+§5.4tier2/6/7/8 complete. D-1..D-7 + PR-1..PR-15 all resolved and committed. RS→MS sweep complete across all active non-archive non-superseded files (508 RS words + 161 'Rendering Stability' phrases swept). rs_budget.md renamed to ms_budget.md with 8 cross-ref updates. Throughlines completeness check extended to 30 entries (T-01..T-30).

next_action:
  skill: editorial
  description: >
    Atomization workplan substantially complete. Remaining targeted follow-ups:
    (1) RWCE / Miracle Investigation / SA-gating full mechanical integration per ED-735 — separate atomization workplan required (touches params/bg/faction_actions, clocks, NPC priority trees, Tension Cards, Conviction Scene UX).
    (2) D-3 (dissolution site specific but contested, off-map) — timeline/worldbuilding update per ED-724; separate workplan.
    (3) D-4 (Altonian invasion ~18 AG) — timeline revision per ED-725; separate workplan. Multiple cross-cutting references.
    (4) D-5 Einhir site-network three-layer operational model — new designs/world/einhir_site_network.md or expansion of calamity_radiation_v30 (ED-726 target corrected this sequence). Separate workplan.
    (5) D-6 (Lenneth TS pathway scholarly loosening, SA-gated, ceiling 10-20) — NPC analyses update per ED-727; separate workplan.
    (6) D-7 (Valn origin pre-Altonian) — worldbuilding update per ED-728; separate workplan.
    (7) PROVISIONAL marker audit — 45 active-path files contain [PROVISIONAL:] markers. Audit scope large; most markers pre-date this session. Enumerate and resolve individually when touched.
    (8) Auto-generated index files (e.g. references/file_index.md, *_index.md) still contain 'rs_budget' references. These regenerate via tools/doc_index_gen.py on next doc-index run. No manual patch needed.
    (9) canon/02 "formerly Rendering Stability per ED-731" cross-ref is intentional historical annotation — DO NOT sweep.
  blockers: []

commits_this_sequence:
  - 976e1e8a: '[editorial] Batch 6 §6.1 — Ob 7 AND→OR'
  - e642f195: '[editorial] D-1 cascade — 12y emergence / 7y ministry'
  - dc6e39ac: '[editorial] Ledger split + register D-1..D-7 + PR-1..PR-15'
  - 8f8388e9: '[editorial] D-2 + PR-15 — pre-Calamity governance + Seam Text metadata'
  - 39069744: '[editorial] Batch 1 — Finitude Pivot foundations §4.3'
  - 46da2d13: '[editorial] Batch 2 — Leap Mechanism amendment + anchors + cross-refs'
  - 576e9fea: '[editorial] Batch 5 §5.4 core + §5.2 — RS→MS core sweep + timeline L129/L179'
  - f2b5d143: '[editorial] Batch 3 — MS trajectory v1 + timeline L21/L181'
  - 239c1d3b: '[editorial] Batch 7 — BA-1 + B-1 + S-1 + Finding 7 worldbuilding §3.7'
  - a7cffdc0: '[editorial] Batch 8 — throughlines T-02/T-08 extensions + T-26..T-30'
  - bc7fe400: '[editorial] Session log + ED-726 correction (D-5 target)'
  - 560267ab: '[editorial] Batch 5 §5.4 tier-2 — RS→MS sweep 40 files (508+161)'
  - 2660d034: '[editorial] rs_budget.md → ms_budget.md rename + 8 cross-refs'
  - 162ab112: '[editorial] Throughlines completeness check — T-26..T-30 rows; 25→30'

## Atomization state at end of sequence

### Canonical doctrine
- canon/00 §4.3 Confrontation as Constitutive Finitude (PR-1 Option A) canonical
- canon/02_foundations_amendment_leap_mechanism.md (PR-2 Option A) canonical — 6 amendments
- canon/01 unchanged; canon/02 Amendment 1 refines layer-2 facings without reassigning layer-3
- threadwork_v30 §2.3 and §31 anchored to canon/02
- foundations §5.3 cross-ref to canon/02 added

### Terminology
- MS (Mending Stability) is canonical across all active non-archive tree
- RS terminology preserved only in: params/threadwork_superseded.md (intentional), designs/threadwork/threadwork_v25_historical.md (intentional), canon/02 "formerly RS" annotation (intentional), auto-regen indexes (self-heal)

### Timeline corrections
- L16: Altonian overlay, not indigenous nations (D-2 ED-723)
- L21: ~12y Catastrophe-to-dissolution (D-1 ED-722)
- L32: 12y emergence / 7y ministry (D-1 ED-722)
- L129: TT 28 → MS 72 Strained (PR-3 ED-731)
- L179: TT→MS inversion note
- L181: 7y ministry correction cell

### Worldbuilding
- §7.1 heading Indigenous→Altonian (D-2)
- §3.7 new Practitioner Witness Tradition (PR-14 Finding 7 ED-735)

### NPC
- §6 Baralta theology supplement (PR-11 BA-1 ED-732)

### Consolidated Solmund guide
- §3.2 Ficinian Cardinal canonical (PR-12 B-1 ED-733)
- §4.4 RM Lurianic canonical (PR-13 S-1 ED-734)
- §11.2 Finding 7 de-flagged (ED-735)
- §12 Seam Text metadata frame (PR-15 ED-736)
- L246 7y ministry (D-1), L387 Ob 7 AND→OR

### Mechanical docs
- designs/world/ms_trajectory_v1.md (13,409 chars) — 3/5 decision points resolved, 2 provisional
- references/ms_budget.md (formerly rs_budget.md) with rename history in header
- 8 files updated to reference ms_budget.md path

### Throughlines
- T-01..T-25 unchanged
- T-02 Extension (TL-1 constitutive finitude + TL-6 rendered/thread/ontical triple)
- T-08 Extension (TL-2 Church conflation as generative engine)
- T-26..T-30 novel: Recursion, Effects-real-explanation-wrong, Confrontation/Leap/Operation, Baralta cracker, Information asymmetry
- COMPLETENESS CHECK table updated 25→30 rows

### Editorial ledger
- Split to main + archive (archive: 13 resolved P2/P3)
- 16 resolution entries ED-722..ED-737 registered
- ED-726 description corrected (D-5 target is designs/world/ not canon/02)

---

session_id: 2026-04-21-rigorous-audit-s1-s7-synthesis-v3-1
session_close: 2026-04-21
phase: audit-synthesis-complete
status: closed
last_stage: >
  Rigorous audit S1–S7 synthesis v3.1 full commit sequence complete.
  ED-738 editorial committed (d80e1532). v3.1 synthesis + mechanical implementation
  revised + mechanical implications revised committed (cf8f2612). T-31..T-41 registry
  additions committed (d9ebd026). М-7..М-11 meta-throughline additions + T-26..T-41
  tag-table extension committed (c4db7299). Wave 1 workplans + gameplay assessment
  committed (b91a8c66). 41 total throughlines. 11 total meta-throughlines.
  Corrections applied per ED-738: consciousness-absent→non-reflexive register;
  non-episodic retention→cartographic register at specificity-gated resolution;
  pure apophatic→Regimes 1–3 cartographic + Regime 4 apophatic; different-givens→
  same given different receptive capacities; dive-log→below-waterline cartographic;
  six-phase Leap→two-decision player surface; Thread-Read not a separate operation;
  Hold vs Flee→Hold vs Turn-Away; water-metaphor extensions stripped; iceberg framing
  authorised for gameplay conceptualisation per ED-738 §4.

next_action:
  skill: editorial
  description: >
    Wave 1 atomization PP entries for P1/P3/P9/P10/P21 per designs/workplans/wave1_workplans.md.
    Blockers: P6-1 Coherence career floor (3 options); P15-1 Layer 3 prototype test.
    High-priority decisions: P1-1 surprise/prone Ob; P9-1 Hold vs Turn-Away confirm;
    P9-2 TS progress-point threshold; P18-1 Accord perception strength; P5-1 observer-variability.
    Secondary work: Session 8 rigorous audit per v3.1 §6 methodology (cross-matrix tensions;
    design recommendation synthesis; framework-original contributions inventory).
    T-26..T-30 registry reconciliation (v3.1 §4 open question 3).
    Sixteen total open editorial decisions enumerated in mechanical_implementation_revised §11.

blockers:
  - P6-1: Coherence career floor editorial decision (three options pending)
  - P15-1: Layer 3 prototype gameplay-contribution test

commits_this_sequence:
  - d80e1532: '[editorial] ED-738 — Ein Sof gradient + cartographic contemplative + ledger'
  - cf8f2612: '[editorial] S1–S7 rigorous audit synthesis v3.1 + mechanical implementation revised + implications'
  - d9ebd026: '[editorial] Throughlines T-31..T-41 — registry additions per v3.1 synthesis'
  - c4db7299: '[editorial] Meta-throughlines М-7..М-11 — skeleton table 6→11 + infill specs + T-26..T-41 tag-table extension'
  - b91a8c66: '[editorial] Wave 1 workplans P1/P3/P9/P10/P21 + gameplay contribution assessment'

throughlines_count: 41
meta_throughlines_count: 11

tier_assignments:
  N_direct: [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13]
  N_extended: [P14, P15-Layer3, P16, P17, P18]
  N_flavor_pending: [P19, P20, P21-ambitious, P22-conditional]

G_tiers:
  G_core: [P1, P3, P9, P10, P21-overlays]
  G_support: [P2, P5, P7, P8, P12, P13, P22, P18]
  G_texture: [P4, P11, P19, P20]
  G_frame: [P6]

---

session_id: 2026-04-22-ed717-cleanup
session_close: 2026-04-22
phase: 0
status: complete
last_stage: ED-717 closed (T-15a/b/c substrate-postures), ED-667 closed (graduated autonomy), PP-675 backstory strike, residual cleanup
next_action:
  skill: confirm with Jordan
  description: >
    All Session B/C/ED-717 work complete. Remaining:
    - Index regeneration for modified files
    - Remaining incidental Niflhel refs in arc/NPC files (non-mechanical, context-appropriate)
    - CI cap vs Piety Yield at T9 — Jordan design decision pending
    - Retroactive canon audit — deferred until engine_v4 smoke-test data
  blockers:
    - Jordan design decision: CI cap vs Piety Yield at T9
commits:
  - 5537bc9: ED-717 (1/3) — T-15a Hafenmark unmediated sovereigntist
  - cb50098: ED-717 (2/3 + 3/3) — T-15b Löwenritter substrate-agnostic protector + T-15c RM substrate-heritage reclaimer
  - fb16bd3: ED-717 resolved, ED-667 resolved in editorial ledger
  - 7b96edd: Residual Niflhel/Coup cleanup in arc files + factions_personal
  - ef19887: PP-675 backstory strike — assign PP number to STRUCK markers
session_highlights:
  - ED-717 CLOSED. Three new М-4 throughlines define substrate-postures for all factions:
    T-15a Hafenmark (unmediated sovereigntist — Protestant position, shares theology but rejects ecclesial monopoly and governance authority),
    T-15b Löwenritter (substrate-agnostic protector — Praetorian position, Thread irrelevant to military duty),
    T-15c RM (substrate-heritage reclaimer — unknowing inheritance via Einhir practice, only unconscious substrate-posture).
  - М-4 throughline count now 7. Every faction has a defined substrate-posture. All three TS-0 factions face distinct crises at Thread revelation.
  - ED-667 CLOSED. Graduated autonomy (4-stage) resolves Coup Counter readiness gap.
  - PP-675 assigned to backstory strike (Session A Patch 7). Father assassination → Royal Crisis Tension Card.
  - Residual Niflhel/Coup refs cleaned in arcs_31_35, emergent_campaign_arcs, factions_personal_v30_infill.
  - P1 blocker count reduced 2→1 (ED-667 resolved). Remaining P1: CI cap vs Piety Yield.
open_items:
  - CI cap vs Piety Yield at T9 — Jordan design decision pending (last P1)
  - Index regeneration for ~15 modified files
  - Retroactive canon audit — deferred until engine_v4 smoke-test data
  - Sparse throughline-interaction matrix — 7 of 25+3 throughlines have mapped cross-interactions
  - Remaining incidental Niflhel refs (~30 across arc/NPC files) — non-mechanical context references, not blocking
P1-BLOCKER count: 1

---

session_id: 2026-04-22-d3-d6-d7-propagation
session_close: 2026-04-22
phase: editorial
status: complete
last_stage: D-3/D-6/D-7 propagation complete 2026-04-22 (commits 9ff5a7de / 1b0c177f / 0d3a82e6). D-3 timeline §Solmund dissolution site paragraph; D-6 Lenneth TS pathway (SA-gated, ceiling 10-20) in NPC analyses + infill; D-7 Valn origin softened to pre-Altonian/possibly pre-Einhir in arcs_10_18.md §Terminology + ED-NEW-7 row. ED-724/727/728 descriptions amended. canonical_sources.yaml block added.
next_action:
  skill: editorial
  description: >
    Remaining follow-ups from 2026-04-20 atomization workplan:
    (1) D-4 Altonian invasion ~18 AG timeline revision (ED-725) — multi-file cross-refs. Dedicated chat.
    (2) D-5 Einhir site-network three-layer operational model (ED-726) — new designs/world/einhir_site_network.md OR expansion of designs/world/calamity_radiation_v30.md. Dedicated chat.
    (3) RWCE / Miracle Investigation / SA-gating full mechanical integration (ED-735) — separate atomization workplan touching params/bg/faction_actions, clocks, NPC priority trees, Tension Cards, Conviction Scene UX.
    (4) PROVISIONAL marker audit — 45 active-path files. Resolve individually when touched.
  priority: "D-4 or D-5 next depending on Jordan selection"
blockers: []
notes:
  - "canon/editorial_ledger.yaml at 1,836 / 2,000 tokens (WARN). Archival batch recommended before further resolution entries."
  - "Auto-regen indexes (*_index.md, references/file_index.md) still reference 'rs_budget'. Regenerate via tools/doc_index_gen.py on next doc-index run."
  - "canon/02 'formerly Rendering Stability per ED-731' cross-ref is intentional historical annotation — do not sweep."

---

session_id: 2026-04-23-consolidation-system
session_close: 2026-04-23
phase: infrastructure
status: complete
last_stage: >
  Naming/value/glossary consolidation system built in 4 parts (all committed).
  Part 1 (proper_noun_registry.yaml) at 4146bac + round-2 finalization at 0f0f38f:
    62 entries across 10 categories, 42 aliases, 0 open candidates.
    All 466 round-1 candidates auto-triaged via deterministic rules.
  Part 2 (alias_registry.yaml) at 3addd2b: 96 entries across 15 categories
    covering core/derived/thread stats, world clocks, debate, faction stats, combat,
    dice engine, narrative, thread ops, infra, modes, 4 collisions, 4 unresolved gaps,
    4 legacy renames.
  Part 3 (values_master.yaml + tools/extract_values.py) at ad6a8fd: 464 values
    extracted from 12 of 14 params files; 5 real conflicts surfaced (threadwork/superseded drift).
  Part 4 (tools/valoria_collator.py + references/collation_report_summary.yaml) at 8516cf6:
    scans all design/params/canon .md against the 3 registries.
    First run: 9101 findings after context-aware exemptions.
      COLLISION_USED_ALONE: 1092 (TC 943×, TD 80×, CP 69×)
      LEGACY_TERM_USED: 903 (RS 531×, Rendering Stability 158×, Cohesion 73×, CP 63×, TD 74×)
      UNKNOWN_ABBREVIATION: 3640 (long tail of per-doc terms)
      UNKNOWN_PROPER_NOUN: 3466 (mostly compound mechanical phrases)
next_action:
  skill: infrastructure
  description: >
    Concrete follow-ups surfaced by the collator:
    (1) Bulk-fix tool to consume collation_report_summary and do context-aware
        substitutions: TC → Theocracy Counter or Conviction Track (requires per-context
        disambiguation), RS → Mending Stability, Cohesion → Discipline,
        Combat Power → Power, CP in game-stat contexts → Character Point.
    (2) Extend values_master to scan designs/*.md too (not just params/), since the
        CI ceiling 75 vs 100 conflict likely lives in designs/, not params/.
    (3) Glossary additions for deferred terms from round 1: Arc, Zoom In, Cardinal.
    (4) Populate alias_registry unresolved gaps: CERT, TLK, DD, FSTAT — confirm full names.
    (5) Maret disambiguation pass — flagged for per-file context (two Marets: Uln vs Vossen).
  priority: "(1) bulk-fix tool is highest impact — addresses the 1092 collision + 903 legacy findings"
blockers: []
notes:
  - "Collation report per-instance detail (985KB) not committed — regenerate via tools/valoria_collator.py"
  - "Proper noun registry at 62 entries is saturated for this round; additional promotions will come from new design work"
  - "Five carried-over follow-ups from 2026-04-22 editorial session still pending: D-4, D-5, ED-735 (RWCE/Miracle Investigation/SA-gating), PROVISIONAL marker audit, doc_index_gen.py regeneration"

---

session_id: 2026-04-24-consolidation-followups
session_close: 2026-04-24
phase: infrastructure
status: complete
last_stage: >
  Continued follow-ups from 2026-04-23 consolidation-system close.
  Five commits:
    2071752 — alias_registry v2 (Certainty added, unresolved gaps closed via deprecated section),
              + references/numeric_bounds_report.yaml (targeted scan of 207 files for ceiling/cap/
              floor/threshold/max/min; 254 hits, 97 stats, 14 flagged as potentially drifted).
    02ba388 — bulk-fix applied: 104 substitutions across 22 files
              (Rendering Stability→Mending Stability: 74, Cohesion→Discipline: 29, Combat Power→Power: 1).
              User-authority paths skipped (designs/world, designs/npcs, designs/arcs, designs/territory).
              Historical/deprecated/superseded files skipped. Lines with rename-context markers skipped.
    08e0cf1 — tools/valoria_bulk_fix.py + glossary additions (Arc, Zoom In, Zoom Out, Cardinal).
    Glossary last_updated advanced to 2026-04-24.
  Collator re-run post-fix: 9101→8969 findings (−132). LEGACY_TERM_USED 903→799 (−104 matches substitutions).
  COLLISION_USED_ALONE 1092 unchanged — TC/TD/CP require per-context judgment, not auto-fixable.
next_action:
  skill: editorial
  description: >
    Only manual-judgment items remain from the consolidation system:
    (1) TC disambiguation sweep — 943 occurrences across design docs. Each TC instance must be
        manually classified as Theocracy Counter (faction clock) or Conviction Track (debate
        system). Top files: designs/audit/npc_faction_arc_interdependency_2026-04-18.md (61×),
        designs/arcs/narrative_scenario_chains.md (57×), designs/scene/conviction_track_v30.md (52×),
        designs/arcs/gm_ref/arcs_46_55_resolved.md (50×), designs/provincial/faction_politics_v30.md (48×).
    (2) CP and TD disambiguation — smaller footprint (~149 combined) but also per-context.
    (3) User-authority-path RS/Rendering Stability residuals — bulk-fix skipped designs/world,
        designs/npcs, designs/arcs, designs/territory. These need editorial-flagged commits if swept.
    (4) Numeric bounds report review — 14 stats flagged for potential drift; most are likely
        legitimate (multiple thresholds per stat) but a handful may be stale references.
    (5) Maret disambiguation pass — flagged since round-1 proper noun triage (Uln vs Vossen).
    (6) Five carried-over items from 2026-04-22: D-4, D-5, ED-735 (RWCE/Miracle/SA-gating),
        PROVISIONAL marker audit, doc_index_gen.py regen.
  priority: "TC disambiguation is the highest impact on mechanical correctness — ~30 min focused work on top 5 files clears 268 of 943"
blockers: []
notes:
  - "Collator per-instance report (962KB) not committed; regenerate via tools/valoria_collator.py"
  - "Numeric bounds report highlights Mending Stability threshold (20/40/60) inconsistencies in arcs — likely intentional multiple thresholds, not bugs"
  - "Certainty now registered in alias_registry — any remaining 'CERT' usages in active docs are now properly named (not unresolved)"

---

session_id: 2026-04-26-disambiguation-sweep
session_close: 2026-04-26
phase: editorial
status: complete
last_stage: >
  Full abbreviation disambiguation sweep. 9 commits:
    db0dcd0 — TC→CI + RS→MS top 5 files (185 TC, 61 RS)
    1a48d60 — TC→CI residuals in top 5 (83 TC, 21 RS)
    028a748 — TC→CI + RS→MS 60 design/params files (~422 TC, ~181 RS)
    44fbb1e — TC→CI + RS→MS 3 user-authority files (ED-783/784/785)
    dadf8e1 — TC→CI in 46 tests/canon files (853 TC)
    e024512 — Alias registry TC→CI update + numeric bounds review (ED-786)
    7989b11 — Maret Vossen → Yrsa Vossen propagation (14 files, PP-665)
    8563b46 — Maret Vossen → Yrsa Vossen NPC authority file (ED-787)
  Summary: ~1,543 TC→CI, ~263 RS→MS, ~100 Theocracy Counter→Church Influence (full term),
  23 Maret Vossen→Yrsa Vossen. Alias registry updated (theocracy_counter→church_influence,
  collision table TC entry marked resolved). Numeric bounds report reviewed: all 14 flagged
  stats = legitimate multiple thresholds or false positives, no drift.
  CP disambiguation confirmed complete (CP=Character Points per ED-136, no active Combat Power refs).
next_action:
  skill: editorial
  description: >
    Remaining items from consolidation queue:
    (1) RS in tests — ~1,340 instances. Cannot blind-replace: "RS" collides with Rhetorical Style
        (Evidence RS, Authority RS, Solidarity RS, Consequence RS in NPC debate contexts).
        Needs per-context classifier distinguishing RS=Mending Stability from RS=Rhetorical Style.
        Python files blocked by fabrication check; variable names (gs.rs, avg_rs) should not be renamed.
    (2) TD disambiguation — mostly Mermaid flowchart TD (valid). Small count of Thread Depth (removed
        PP-166) references may exist. Low priority.
    (3) ED-768 (P3) — PROVISIONAL marker audit. 13 orphaned markers referencing pre-ledger EDs.
        Requires Jordan review to determine which are still-open vs resolved-but-unarchived.
    (4) ED-543 (P1) — Clock registry refresh verification. Single-atom evidence; needs verification
        whether the registry refresh actually landed under another ED.
    (5) D-4 (Altonian invasion ~18 AG) — timeline revision per ED-725. Requires Jordan worldbuilding authority.
    (6) D-5 (Einhir site-network model) — new spec per ED-726. Requires Jordan worldbuilding authority.
    (7) doc_index_gen.py regen — index files stale after bulk renames. Mechanical but large scope.
    (8) Python sim file Maret rename (campaign_sim_npc_pcs_2026-04-18.py) — blocked by fabrication check.
    (9) TC in deprecated/ files — low priority, old docs.
  priority: "ED-543 (P1) verification is highest severity. RS test disambiguation is highest volume."
blockers: []
notes:
  - "Glossary notes in affected files updated to reflect CI = Church Influence (was TC = Theocracy Counter)"
  - "Alias registry collision_table TC entry marked resolved with 2026-04-26 sweep date"
  - "RS = Rhetorical Style is NOT in the alias_registry — needs entry added if it's a canonical term"
  - "Numeric bounds report reviewed inline (review header added). Regenerate after next collator run."
  - "Maret disambiguation was already decision-resolved (PP-665) but propagation was incomplete — now fixed in 15 active files"

---

session_id: 2026-04-27-phase0-foundation
session_close: 2026-04-27
phase: infrastructure
status: complete
last_stage: >
  Phase 0 Foundation — workplan v3 §2. 12 commits across ttrpg + valoria-game.
  ttrpg commits:
    3d7e46b — 0.1.1-0.1.3 register truthfulness (11 patch_register SHAs, editorial_summary rebuild)
    3edf7f0 — 0.2.1-0.2.3 threadwork audit P0 triage (28 P0s classified, 27 unknown IDs verified)
    6dadbe2 — 0.5.1 compliance_check auto-fetch wiring
    5e238ea + b07c459 — 0.5.2 freshness_gate regex fix + SHA population (47 fields)
    b5ca0a7 — 0.7.2 ttrpg README.md
  valoria-game commits:
    8be75e5 — 0.4.3/0.4.4 GameMode strip + A-02 disambiguation + Yrsa rename (7 files)
    f9ed815 — 0.4.3 followup broken ref fixes (3 files)
    600c5cf — 0.5.3 CI workflow (godot-ci.yml)
    e4a62db — 0.6.1-0.6.2 conversion_ledger + design_sync status reconciliation
    c41688c — 0.7.3 README.md rewrite
next_action:
  skill: infrastructure
  description: >
    Phase 0 remaining items:
    (1) 0.7.1 LICENSE — Jordan decision needed (proprietary/MIT/Apache/CC BY-NC/custom)
    (2) 0.7.4 Declare-deferred governance items (CONTRIBUTING, CODE_OF_CONDUCT, etc.)
    (3) 0.3.1 Params freshness sweep — freshness_gate now working; run full check + resolve stale entries
    (4) 0.4.6 ACTIONS_PER_FACTION_PER_SEASON PROVISIONAL value in Constants.gd — verify against canonical
    (5) Broken deps in propagation_map: skeleton_gen.py (renamed to doc_index_gen.py), sim_ttrpg_batch_legacy files — update propagation_map
    (6) DiceVariant.TTRPG/BG collapsed to STANDARD — verify no test failures
    (7) Session log next_action items from prior session still relevant: RS test disambiguation (~1,340), D-4/D-5 (Jordan worldbuilding), doc_index_gen regen
  priority: "LICENSE decision + Phase 0 exit criteria verification, then proceed to Phase 1"
blockers: ["LICENSE decision (0.7.1) — Jordan"]
notes:
  - "canonical_sources.yaml at 4,670/5,000 tokens after SHA injection — approaching threshold"
  - "compliance_check auto-fetch wired but untested (will fire on next bootstrap)"
  - "Threadwork P0 triage committed: 7 resolved, 15 Jordan-decision, 4 mechanical, 2 reclassify"
  - "GameMode enum fully stripped from valoria-game (100 .gd files scanned, 0 remaining refs)"
  - "Values master regen'd: 462 values, 5 false-positive conflicts (all superseded file)"
  - "Collator ran: 8,873 findings (3,884 unknown abbrevs, 3,594 unknown nouns, 919 legacy terms, 476 collisions)"

---

session_id: 2026-04-28-phase0-phase1
session_close: 2026-04-28
phase: editorial + infrastructure
status: in-progress
last_stage: >
  Phase 0 completion (12/13 exit criteria met, LICENSE pending) + Phase 1 partial.
  This session commits (ttrpg):
    4547737 — propagation_map broken dep fix
    052b82d — bootstrap wiring (compliance_check + freshness_gate)
    7f640e5 — F2 verification batch ED-745/746/747/748 resolved
    ba7497d — PP-666 trio vetting block
  This session commits (valoria-game):
    f9ed815 — GameMode strip broken ref followup (prior session continuation)
    600c5cf — CI workflow
    e4a62db — conversion_ledger + design_sync status reconciliation
    c41688c — README rewrite
  Prior session commits carried forward:
    3d7e46b — register truthfulness
    3edf7f0 — threadwork P0 triage
    8be75e5 — GameMode strip (7 files)
    6dadbe2 — compliance_check auto-fetch
    b07c459 — freshness_gate regex fix + SHA population
    b5ca0a7 — ttrpg README
next_action:
  skill: editorial
  description: >
    DECISION PENDING (Jordan):
    (1) Restore Intelligence as 6th faction stat? Review at designs/audit/faction_stats_renaissance_review.md
        - If yes: starting values Crown 3, Church 4, Hafenmark 3, Varfell 5, Loewenritter 2, Guilds 4
        - Fixes Spy Ob formula (currently broken), Varfell Path A re-gate, Varfell stat identity
        - If no: need replacement Spy Ob formula + Varfell Path A re-gate + Varfell differentiation
    (2) LICENSE decision (GOV-08) — proprietary/MIT/Apache/CC BY-NC/custom
    PHASE 1 REMAINING (after Intelligence decision):
    (3) 1.1 Knot Formation During Play — design decision
    (4) 1.2 Accord Propagation to Settlement Order — 15-25 rules need settlement targeting
    (5) 1.3 Derived Stats Calibration — depends on 1.2
    (6) 1.4 Faction Politics Sim — depends on 1.3
    (7) 1.8 Varfell Path A editorial rewrite — depends on Intelligence decision
    PHASE 0 RESIDUAL:
    (8) compliance_check atomizer dep — auto-fetch wired but atomizer.py not in fetch list
    (9) canonical_sources.yaml at 4670/5000 tokens — approaching threshold
  priority: "Intelligence decision unblocks Path A + Spy Ob + Varfell identity. Then 1.1/1.2 design decisions."
blockers:
  - "Intelligence stat decision (Jordan)"
  - "LICENSE decision (Jordan)"
  - "1.1 Knot Formation design (Jordan)"
  - "1.2 Accord Propagation design (Jordan)"
notes:
  - "Faction stats Renaissance review committed as designs/audit/faction_stats_renaissance_review.md"
  - "All P3 EDs resolved (745-748). Active ledger now 2 open (ED-710/711, both P2)"
  - "Phase 0 exit: 12/13 criteria met. Only LICENSE remains."
  - "Threadwork P0 triage: 7 resolved, 15 Jordan-decision, 4 mechanical, 2 reclassify"

---

session_id: 2026-04-28-stress-test-political-dynamics
session_close: 2026-04-29
phase: simulation
status: closed
last_stage: >
  Three-batch NERS stress test against 12_development_specification.md (political dynamics).
  Commits (ttrpg):
    33100e7b — 13_stress_tests_extended.md (20 issues, 1 critical, 8 high)
    cac8142 — 14_ners_stress_tests.md (25 issues, 9 design-fail, 8 gaps)
    bb79d1a1 — 15_stress_tests_batch3.md (23 issues, 2 critical, 11 design-fail)
    [this close] — 16_session_close_observations.md (comprehensive context, priority order)
  Total: 68 issues across 50 unique test cases. All patchable; no architectural redesign required.
next_action:
  skill: editorial
  description: >
    IMMEDIATE (before implementation):
    (1) Define select_proposal() + domain_armature_alignment table [E-36-A — Critical]
    (2) Define max_scars = inner_circle_active_npc_count x 2 [E-48-A — Critical]
    (3) Define conviction_alignment_multiplier values in Procedure D [E-BOT-A — Critical]
    (4) Single-writer Opinion model: B/C produce Memories only; D consolidates [ST-32-A / E-HORIZ-A]
    (5) Decision: define symbolic_effects consumption OR cut 210-entry table [E-38-A/B]
    PENDING (Jordan decisions, unchanged from prior session):
    (6) Intelligence stat as 6th faction stat — unblocks Spy Ob, Varfell Path A
    (7) LICENSE decision (GOV-08)
    (8) 1.1 Knot Formation During Play
    (9) 1.2 Accord Propagation to Settlement Order
  priority: "Items 1-4 are spec edits with correct answers — no design decision needed. Item 5 is highest-stakes decision (400 authoring entries affected)."
blockers:
  - "select_proposal() — requires domain_armature_alignment authored table (Jordan sign-off)"
  - "symbolic_effects decision (keep + define consumption vs cut table)"
  - "Intelligence stat decision (Jordan, prior session)"
  - "LICENSE decision (Jordan, prior session)"
notes:
  - "Full issue register + priority order in 16_session_close_observations.md"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold"
  - "Class A (undefined values): 15 issues — authoring/spec completeness, no design decisions"
  - "Class B (unused fields): 8 issues — field/procedure misalignment, cut or implement"
  - "Class C (tie-breaking/edge cases): 6 issues — implementation-facing, low urgency"
  - "Class D (ordering/double-write): 5 issues — single-writer Opinion fix resolves core cluster"

---

session_id: 2026-04-29-mass-battle-ners
session_close: 2026-04-29
phase: "2 — ongoing"
status: audit complete, patch proposals committed, terminology workplan committed
last_stage: >
  mass battle NERS stress test (batches 1+2) + historical review + patch proposals,
  systems overview compiled, connections artifact v1 produced,
  terminology conversion workplan drafted and committed (PP-675/ED-759 provisional)
next_action:
  skill: editorial
  description: >
    NEXT-SESSION PRIORITY (set by Jordan 2026-04-29):
    Re-do the connections artifact at designs/audit/2026-04-29-connections-artifact/
    with rigorous relationship audit. v1 (committed this session, /mnt/user-data/outputs/valoria_connections.jsx)
    was a first sketch — relationships were assigned by quick inspection of canonical_sources.yaml
    and the architecture skeletons, not by reading every system spec end-to-end.
    Required v2 work:
    (1) Read every system doc listed in canonical_sources.yaml at least to skeleton depth;
        for high-traffic hubs (faction_layer, scale_transitions, conflict_arch) read in full
    (2) For every node pair, decide: edge or no edge; if edge, then type (foundational/cascade/
        bidirectional/containment/gating), strength (1-4 rubric in node), state (canonical/
        provisional/gap), and label
    (3) Audit the v1 edges against the audit and remove/correct any that don't survive
    (4) Add edges that v1 missed (likely candidates: military_layer→faction_layer details,
        ms_trajectory↔threadwork specifics, throughlines→every Class A/B touchpoint,
        any second-order intersections through Self-Rendering/Leap)
    (5) Encode relationship quality not just by color but also by proximity/clustering
        and dash-pattern variation
    (6) Output: revised valoria_connections.jsx with audit log of edge decisions inline
        in a hidden EDGE_AUDIT comment block

    JORDAN DECISIONS REQUIRED (still pending from prior session):
    Mass battle (mass_battle_patch_proposals_2026-04-29.md):
    (1) DECISION-MB-01 through DECISION-MB-08 — 8 design decisions, recommended answers given
    Terminology conversion (designs/audit/2026-04-29-terminology-conversion/00_workplan.md §4):
    (2) 4.1 Strategic Mode vs Map Mode for BG (recommend: Strategic Mode)
    (3) 4.2 Scene Mode vs Encounter Mode for TTRPG (recommend: Scene Mode)
    (4) 4.3 Confirm Hybrid mode retired (3-mode → 2-mode + Zoom-In) — load-bearing
    (5) 4.4 Adjudicator → Resolver, or keep (recommend: keep)
    (6) 4.5 "session" policy (recommend: retire TTRPG-evening sense; allow hooks/UI senses)
    Standing decisions (still pending from prior sessions):
    (7) Intelligence stat restoration — see designs/audit/faction_stats_renaissance_review.md
    (8) LICENSE decision (GOV-08)
    (9) 1.1 Knot Formation During Play
    (10) 1.2 Accord Propagation
blockers:
  - "Connections artifact v2 audit pass (next session priority)"
  - "5 terminology workplan decisions (Jordan)"
  - "Topographic analysis findings review (Jordan, 12 TOPO entries to triage)"
  - "8 mass battle design decisions (Jordan)"
  - "8 auto-approvable mass battle patches awaiting approval (Jordan)"
  - "Intelligence stat decision (Jordan)"
  - "LICENSE decision (Jordan)"
notes:
  - "Stress test committed: designs/audit/mass_battle_stress_test_2026-04-29.md (13c11a9)"
  - "Patch proposals committed: designs/audit/mass_battle_patch_proposals_2026-04-29.md (1d9f864)"
  - "Terminology workplan committed: designs/audit/2026-04-29-terminology-conversion/00_workplan.md (PP-675, ED-759)"
  - "Topographic analysis Stages 1-4 EXECUTED 2026-04-29 (PP-676, ED-760). Outputs: 02_weakness_register.md + data/. 12 TOPO findings PROVISIONAL pending Jordan review. Three convergent observations: (1) Knot system under-edged in v1, (2) political-dynamics layer numerically confirmed disconnected, (3) several v1 edges genuinely-thin (real propagation gaps). Methodology limits explicit in register §0."
  - "Connections artifact v1 produced (not yet committed to repo — lives at /mnt/user-data/outputs/valoria_connections.jsx)"
  - "v1 has 31 nodes, 53 edges — relationship judgments need full re-audit per next-session directive"
  - "2 math failures still open: MATH-FAIL-01 (siege calibration impossible), MATH-FAIL-02 (H fixed contradiction)"
  - "27 provisionals still requiring resolution before Godot implementation"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold; pruning needed before terminology_canon entry added"

---

session_id: 2026-04-29-mass-battle-ners-cont
session_close: 2026-04-29
phase: "2 — ongoing"
status: extended audit session complete
last_stage: >
  cross-system interdependency stress testing across mass_battle, core dice, Thread, peninsular_strain,
  derived_stats, personal combat, strategic layer, victory conditions
next_action:
  skill: editorial
  description: >
    PROPAGATION REQUIRED (high priority — before any implementation):
    (1) ED-743 → propagate to victory_v30 §0.4 and peninsular_strain Step 4e (strike direct IP/Strain battle trigger)
    (2) RS → MS global replace in peninsular_strain_v30.md (RS = MS, terminology inconsistency only)
    (3) Campaign Supply: strike derived_stats §8.1 per-unit cost; replace with flat −100 per mass_battle §A.14b
    JORDAN DECISIONS (from this session, see designs/audit/mass_battle_interdependency_2026-04-29.md):
    (4) INTER-09d: Critical hit vs Overwhelming — same threshold? Confirm.
    (5) INTER-10c: §A.10 Thread Ob (flat 4) vs three-axis system — is flat Ob the total or Depth-only?
    (6) INTER-10d: Focus stat in mass battle — dead stat or unstated secondary function?
    (7) INTER-12b: "Discipline" naming collision — rename faction derived value (suggest Cohesion)
    (8) INTER-12e: Muster: Ob roll + Treasury cost both apply, or one only?
    (9) INTER-14a: military_advance Ob vs BG Battle — both fire or BG Battle supersedes?
    (10) INTER-14c: Accord during Occupation — frozen or erodes from Battle?
    PREVIOUSLY OUTSTANDING DECISIONS (still pending):
    (11) Mass battle decisions MB-01 through MB-08 (see mass_battle_patch_proposals_2026-04-29.md)
    (12) Intelligence stat restoration
    (13) LICENSE (GOV-08)
    (14) 1.1 Knot Formation, 1.2 Accord Propagation
blockers:
  - "ED-743 propagation (action, not decision)"
  - "RS→MS replacement in peninsular_strain (action, not decision)"
  - "Campaign Supply cost canonical conflict (action, not decision)"
  - "Multiple Jordan decisions from all three audit batches"
notes:
  - "Batch 3 committed: designs/audit/mass_battle_interdependency_2026-04-29.md (a50f098)"
  - "E-FAIL-01 CLOSED: output scaling and PP-233 are complementary layers, not conflicts"
  - "E-FAIL-02 CLOSED: Army Morale modifiers found in derived_stats §10.2"
  - "14 cross-system items confirmed consistent (Thread costs, TroopCount math, Domain Echo, etc.)"
  - "RS vs MS: same stat, terminology inconsistency only in peninsular_strain_v30"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold"

---

---
session_id: 2026-04-29-topographic-v2v3
session_close: 2026-04-29
phase: "topographic analysis v2 + v3 same-session"
status: complete
last_stage: >
  Topographic analysis v2 + v3 executed in same session. v2 (TF-IDF-primary): validation
  FAILED (Jaccard 0.222). v3 (multi-graph triangulation): validation VALIDATED (2/3
  structural properties). v3 corrected v2 flagship finding (corpus IS system-anchored,
  NPC Behavior is integration spine cite-deg 56). 84 tokens × 2940 paragraphs, 5 graphs,
  8 diagnostics. Combined v2+v3 weakness register at
  designs/audit/2026-04-29-topographic-analysis/02_weakness_register.md.
next_action:
  skill: editorial
  description: >
    Jordan review of v3 weakness register. Key v3 findings requiring decision:
    (1) NPC Behavior is corpus integration spine (cite-deg 56) — schedule audit pass;
    (2) Throughlines framework lacks formalized system-token coupling — propose
        adding "load-bearing systems" column to T-NN table;
    (3) Five Convictions + three Pressure Points are multi-graph isolates with zero
        recent editorial scrutiny — propose taxonomy doc promotion;
    (4) Vocabulary debt confirmed: Game Master concentrated in threadwork_v30 (11/16),
        Cultural Reformation in peninsular_strain_v30 (10/15), Coup Counter dispersed (7 docs);
    (5) v2 connections audit work item list updated in v3 §V3-10.
    PRIOR ITEMS still pending Jordan decision:
    - CI-01 Church Prominent definition (HIGH-PRIORITY, breaks Church CI generation)
    - PT-01, ACCT-01
    - Mass battle MB-01..08, INTER-10d/12b/14a/14d/14e/12e/17b/09d
    - Intelligence stat, LICENSE/GOV-08, §1.1 Knot Formation, §1.2 Accord Propagation
blockers:
  - "Jordan review of v3 weakness register findings"
  - "Prior session blockers (CI-01, PT-01, ACCT-01, all batches)"
notes:
  - "Same-session execution per Jordan directive 'review your review, revise workplan as a replacement, pursue'"
  - "Workplan v3 (this commit) supersedes v1 (commit ac8f55aa) and v2 (uncommitted)"
  - "v3 methodology validates corpus IS system-anchored — v2 framing was TF-IDF artifact"
  - "Combined v2+v3 register retains v2 sections as audit trail"
