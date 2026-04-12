# Valoria Session Log — Current

```yaml
session_id: 2026-04-09_SONNET_DIPL_BATCH2
session_close: 2026-04-09
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Diagnosed remediation needed: PP numbering collision (PP-506-511 taken by Graduated Seizure)
2. Rebuilt params_board_game.md with correct PP-512-524 numbering for all diplomacy patches
3. Added PP-512-524 to patch register
4. Added ED-370-373 to editorial ledger
5. Ran 8 unique scenario stress tests (Batch 2) — interdependency focus
6. Patched 4 new findings: PP-525-528
7. Pre-commit audit: 36/36 checks passed
8. Committed

## COMMITS THIS SESSION
- [this commit] — remediation PP-512-524 + batch 2 scenarios PP-525-528; 1 P1 + 3 P2 resolved

## KEY FINDINGS (BATCH 2)
P1 resolved: 1 (Diplomatic Alignment 'Parliamentary motion' undefined — PP-526)
P2 resolved: 3 (Crown-break trigger PP-525, Closed Pledge witnesses PP-527, Treaty lapse timing PP-528)
Clean scenarios: 4 (S8 Coalition Pivot, S11 Thread Stewardship, S12 Multi-CB, S14 Token Timing)

## PATCHES APPLIED THIS SESSION
PP-512–524: Diplomacy system (renumbered from PP-500-512 due to numbering collision)
PP-525: Crown-break trigger definition (Legionary or Phase 1 declaration)
PP-526: Diplomatic Alignment 'shared Parliamentary motion' = same-side voter effect
PP-527: Closed Pledge witnesses = factions at Accounting of revelation
PP-528: Crown Treaty lapse timing = Phase 1 of season after period ends

## OPEN EDITORIALS
ED-370: Hybrid personal scene -> BG Treaty bridge (P2)
ED-371: Coalition suppression dominant strategy confirmation (P2)
ED-372: Thread Liaison dissolution timing (P2)
ED-373: Token on Mandate-0 suspension (P3, provisionally applied PP-517)
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-09_SONNET_DIPL_AUDIT_PATCH
session_close: 2026-04-09
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Recovered + committed SIM-DIPL-01 (previous session commit failure)
2. Full audit (Modes A-D) of negotiations/alliances/treaties system
3. Identified best solutions for all 7 P1 + 13 P2 findings
4. Designed PP-500 through PP-512 (13 patches)
5. Stress tested all patches (pass criteria, NPC AI validation, edge cases)
6. Ran 7 unique scenario stress tests (2 new findings, both absorbed)
7. Pre-commit audit: 46/46 checks passed
8. Committed

## COMMITS THIS SESSION
- [recovery commit] 0316abd — SIM-DIPL-01 negotiations sim
- [this commit] — audit+patch diplomacy system PP-500-512; ED-370-373; 7 P1 resolved

## KEY FINDINGS
P1 findings resolved: 7 (all Crown Treaty structural issues + Coalition Pairs ghost factions)
P2 findings resolved: 18
New unique scenario findings: 2 (PP-503 simultaneous resolution, PP-504 Named Enemy)
Editorials remaining open: 4 (ED-370 Hybrid bridge, ED-371 coalition dominant strategy, ED-372 Liaison timing, ED-373 Token Mandate-0)

## PATCHES APPLIED THIS SESSION
PP-500: Crown Treaty Ob = ceil(target Mandate/2) min 1
PP-501: Crown Treaty consent — timing, NPC AI rule, refusal CB, 4-season period
PP-502: Crown Treaty target-break clause
PP-503: Open Pledge system (non-Crown binding diplomacy)
PP-504: Coalition Pairs table replacement (Guilds/Niflhel removed; 4 canonical pairs)
PP-505: Diplomatic Token military conflict definition + Mandate-0 suspension
PP-506: Valid suppression action definition for coalition bonus
PP-507: Casus Belli stacking cap + consumption rule
PP-508: Thread Liaison Allied scope restriction
PP-509: Diplomatic Token removal on Crown Treaty formation
PP-510: Missed Coalition Penalty threshold (at or above)
PP-511: Treaty betrayal cascade timing
PP-512: Solo/co-victory simultaneous declaration priority

## EDITORIALS RAISED THIS SESSION
ED-370: Hybrid personal scene -> BG Treaty bridge rule (P2)
ED-371: Coalition suppression dominant strategy confirmation (P2)
ED-372: Thread Liaison dissolution timing prospective vs retroactive (P2)
ED-373: Token on Mandate-0 faction suspension (P3, provisionally applied in PP-505)
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-09_SONNET_DIPL_AUDIT_PATCH
session_close: null
phase: IN PROGRESS
status: OPEN

## TASKS THIS SESSION
1. Recover + commit SIM-DIPL-01 (last session): COMPLETE
2. Audit diplomacy mechanics: IN PROGRESS
3. Identify best solutions, patch, stress test patches
4. Stress test new unique scenarios
5. Audit + commit

## COMMITS THIS SESSION
- [recovery commit] — [simulation] SIM-DIPL-01 negotiations/alliances/treaties; 7 P1, 13 P2 findings
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-08_SONNET_STR_PP476_498
session_close: 2026-04-08
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION

Stress test of all newly patched mechanics PP-476–498 coverage range.
Modes A + D + J across 13 mechanic clusters.

## COMMITS THIS SESSION
- [this commit] — [simulation] stress test PP-476–498 coverage; PP-478–492 applied; ED-343–351 raised

## KEY FINDINGS

P1 findings: 13 (7 editorial, 6 resolved by PP-478–492)
P2 findings: 18 (most resolved by PP-478–492; some editorial)
Gaps: 4 remaining (Soften source, Domain Echo source, AER full table, Weaver Thread pool)

## PATCHES APPLIED THIS SESSION
PP-478: Battle drawn-battle rule precedence (P2)
PP-479: Discipline floor + Fort garrison Discipline analog (P2)
PP-480: Assert mandatory for Church at TC 50–74 (P2)
PP-481: Löwenritter PI +1/Year-End recovery path (P1)
PP-482: Torben dissolution at Torben ≤ 2 on Crown elimination (P2)
PP-483: Torben Year-End modifiers — substitute Löwenritter stats (P2)
PP-484: Church capital T9 Conviction Yield exception (P1)
PP-485: Reconstitution failure Church Mandate cap + counter-action (P1)
PP-486: Weight-of-Numbers primary faction determination (P1)
PP-487: Weight-of-Numbers valid suppression action definition (P2)
PP-488: Ministry AP-tokens persist through faction elimination (P2)
PP-489: Captured General stacking rule (P1)
PP-490: Captured General Mandate −1 timing confirmation (P2)
PP-491: Cardinal schism rotation with dead Cardinals (P2)
PP-492: Conviction Yield Church velocity compensation at TC 30–49 (P1)

## EDITORIALS RAISED THIS SESSION
ED-343: Battle Ob formula (P1 — blocks degree table)
ED-344: T9 Conviction Yield intent confirmation
ED-345: Reconstitution failure Church passive gain + counter-action
ED-346: AER advancement control mechanisms
ED-347: Multi-Cardinal assassination cap
ED-348: Löwenritter post-coup starting territory
ED-349: Soften action — source unknown [GAP]
ED-350: Domain Echo mechanic — source unknown [GAP]
ED-351: Crown elimination + Hafenmark insta-win path

## REMAINING OPEN P1s (total across sessions)
P1-01: Overwhelming threshold (BG) — prior session
P1-03: Crown TCV threshold discrepancy (18 in params summary vs 16 in victory_architecture)
P1-04: Torben starting track (prior session)
P1-05: Seizure Ob formula confirmation (prior session)
STR-PP476-A-01 = ED-343: Battle Ob undefined (this session)
STR-PI-TC-A-02: No Conviction Yield targeting mechanic (design gap — low priority)

## NEXT ACTION

skill: valoria-orchestrator
action: Resolve ED-343 (Battle Ob formula — user decision required). Then resolve ED-348 (Löwenritter post-coup territory). Then resolve ED-351 (Hafenmark insta-win path). Then fetch Soften/Domain Echo source documents for remaining gaps.

blockers: [ED-343, ED-349, ED-350]
editorial_decisions_pending: [ED-343, ED-344, ED-345, ED-346, ED-347, ED-348, ED-349, ED-350, ED-351]
open_gaps_added: [STR-SOFTEN-01, STR-ECHO-01, STR-AER-A-01, STR-RM-A-01]
```

### 2026-04-08 — BG Remaining SIM-DEBT (BG-03 through BG-06)
- Co-victory pairings: P1-08 (Crown+Hafen achievable S1-2 passively — ED-343), P2-07 resolved (PP-479 Partition conflict tracking)
- Faction unique actions: Cardinal Focus Temperance dominant (ED-328 still open); Challenge <structural confirmed; Royal Decree Fragmentation (ED-344); VTM TC contribution undefined (ED-345)
- Ministry NPC AI: Priority 3 dead at 4% (ED-346); Domain conflict rule (PP-480 applied)
- RS decay: system healthy over 20 seasons; WC >= 2 critical for long campaigns; RS/RM/Thread feedback loop confirmed as intended escalation
- New patches: PP-479 (Partition tracking), PP-480 (Ministry redirect)
- New editorials: ED-343 (P1 Crown+Hafen passive), ED-344 (Decree Fragmentation), ED-345 (VTM TC contribution), ED-346 (Ministry Priority 3)
- All SIM-DEBT-BG items complete (BG-01 through BG-06)
- Test output: tests/sim_bg_remaining_2026_04_08.md

### 2026-04-08 — Project State Evaluation + Resolution Execution
- Full project evaluation across all files (33 files fetched, all canonical sources read)
- PP-493: Territory reconciliation — victory_architecture remapped to geography_design.md numbering (45 T# refs, 5 old names). Starting TCV corrected: Crown 12, Hafenmark 8, Varfell 6, Church 3. Total TCV = 30.
- PP-494: Church Graduated Seizure — Pool = Influence + floor(TC/15), Ob = 7 − CV. Hard TC 75 gate removed. Church TCV ≥ 8. BALANCE-001 revised: Crown, Varfell, Hafenmark, Church all equal.
- PP-495: RM TTRPG Founding Gate — narrative gate (cultural shift + substrate strain + player engagement), floor session 6.
- PP-496: Clock registry created (designs/systems/clock_registry.md). Consolidates all tracks.
- PP-497: Inert Knowledge formalized in params_threadwork (P-08 compliance).
- P1-01 Overwhelming stale entries fixed (L1066, L1133 struck/updated per PP-249).
- canonical_sources.yaml: social_debate → social_contest_system_v2.md + params_contest.md.
- ED-343 collision resolved (Spy/Royal Guard renumbered to ED-360).
- ED-352/353/354 resolved. ED-355/356/357/358/359/360/361/362/363 flagged.
- Worldbuilding_integration_v3 old territory names fixed.
- Maret struck as NPC (ED-357). 12-character NPC roster flagged (ED-358).

## REMAINING OPEN P1s
ED-329: Torben Loyalty start/range — user decision required (recommend 3, 0–7)
ED-343: Battle Ob formula — user decision required (proposed: defender Military ÷ 2, min 1)

## OPEN EDITORIAL FLAGS (user decision required)
ED-355: Fort interaction with Church Seizure
ED-356: Crown starting TCV 12 vs threshold 16 — balance check
ED-357: Maret struck — archive references
ED-358: 12-character NPC development roster
ED-359: RM TTRPG Founding Gate session-6 floor review
ED-360: Spy vs Royal Guard interaction
ED-361: PI-CASCADE threshold values
ED-362: DISSONANT war-scale Thread rates
ED-363: P1-01 Overwhelming — confirm PP-249 final

## NEXT ACTION
skill: valoria-orchestrator
action: User decisions on ED-329 (Torben), ED-343 (Battle Ob), ED-355 (Fort+Seizure), ED-356 (Crown balance). Then: Church Graduated Seizure simulation. Then: NPC roster design (ED-358).
blockers: [ED-329, ED-343]
editorial_decisions_pending: [ED-329, ED-343, ED-355, ED-356, ED-357, ED-358, ED-359, ED-360, ED-361, ED-362, ED-363]

### 2026-04-08 — Batch Editorial Resolution
- PP-498: Torben Loyalty corrected to 3 (0–7). Summary table aligned with detailed section.
- PP-499: Battle Ob = defender Military ÷ 2 (round up, min 1).
- PP-500: Fort/Seizure resolved (Battle handles Fort, Seizure is political). Political Vacuum rule added (1-season delay on eliminated territory March).
- PP-501: PI thresholds defined (0–4/5–9/10–14/15–19/20+).
- PP-502: War-scale Dissonant Thread effects parameterized.
- PP-503: Co-Movement serialization rule.
- PP-504: TC seasonal cap confirmed (±3 Domain Actions, ±5 all sources).
- Maret Uln retained (ED-357 un-struck). NPC roster now 13 characters.
- ED-329/343/355/356/357/359/360/361/362/363 resolved. ED-358 remains flagged (NPC roster — user creative decisions).
- SIM-PI-CASCADE and SIM-DISSONANT now unblocked.

## REMAINING OPEN EDITORIAL
ED-358: 13-character NPC development roster (user creative decisions)

## REMAINING OPEN FLAGGED (prior sessions, not addressed this session)
See editorial_ledger.yaml — 35 flagged items total. Major categories:
- Baralta/Vaynard BG Conviction text
- RS track naming
- Several faction-specific mechanical confirmations from prior stress tests

## NEXT ACTION
skill: valoria-orchestrator
action: (1) Church Graduated Seizure simulation (PP-494). (2) PI-CASCADE simulation (PP-501). (3) DISSONANT simulation (PP-502). (4) NPC roster design session (ED-358).
blockers: none
editorial_decisions_pending: [ED-358]

### 2026-04-08 — NPC Roster Design
- 13-character NPC roster designed with structural compromises and behavioral AI flaws.
- Maret Uln retained (Varfell practitioner, dual RM loyalty).
- New NPCs: Haelgrund (Church Inquisitor, hidden TS 12), Torsvald (TS Riskbreaker, knows Lenneth),
  Brandt (Löwenritter officer, premature escalator), Feldhaus (Guilds, Thread-touched supply chain),
  Almstedt (Ministry, procedural obstructionist), Severin Almud (Crown Court, Altonian sympathies),
  Virke (Niflhel, unknowing Thread proliferation), Alexios Laskaris (Altonian Prince, loves Elske),
  Solberg (Schoenland, biased toward Crown), Prudence Cardinal (Church, charitable embezzlement).
- ED-358 resolved. All flagged for user review.
- Committed as designs/npcs/npc_roster.md.

### 2026-04-08 — NPC Roster v3 (cliché review)
- #9 Severin Almud struck. Replaced with Gerik Strand (Lord Steward) — vassal landowner from Feldmark, appointed minister, driven by structural insecurity. Historical echo: William Marshal.
- #10 Virke reframed as Virke family syndicate broker. Niflhel = colloquial name for criminal constellation, not coordinated faction. Historical echo: Medici branch managers.
- #11 Alexios Laskaris → Doux Alexios Laskaris. Greek/Macedonian naming for Altonia. Historical echo: Demetrios Palaiologos.
- Prudence Cardinal echo: Suger of Saint-Denis. Haelgrund: Bellarmine. Torsvald: Christine Granville. Brandt: Aetius. Feldhaus: Jacques Cœur. Almstedt: Byzantine logothetes. Solberg: Xenophon. Vossen: Luxemburg. Maret Uln: Sorge.
- 5 NPCs rewritten to purge cliché (Brandt, Virke, Solberg, Prudence Cardinal already fixed in prior commit; Severin fully replaced).

### 2026-04-08 — Historical Parallel Arcs (Batch 03)
- 8 arcs generated (Arcs 10-17) from historical parallels: Investiture Controversy, Year of Four Emperors, Romance of Three Kingdoms, Sengoku Japan, Byzantine court politics, Borgia papacy, Italian city-states, Sinigaglia.
- 16 event cards with mechanical triggers across all arcs.
- All arcs use existing NPCs: Almstedt, Haelgrund, Baralta, Brandt, Torsvald, Feldhaus, Virke, Vossen, Maret Uln, Vaynard, Severin Almud, Alexios Laskaris, Solberg, Prudence Cardinal. No new NPCs required.
- 8 gaps identified (GAP-ARC-10 through GAP-ARC-17). 6 editorial flags (ED-NEW-1 through ED-NEW-6).
- Cross-arc interaction table: 8x8 matrix documenting all arc intersections.
- Committed as gm_ref/arcs_10_17_historical.md.

### 2026-04-08 — Arc Reassignment (NPC Roster v3)
- NPC roster v3 reviewed: Severin Almud removed, Gerik Strand (#9) added, Hardar → Doux Alexios Laskaris (#11), Dalla Virke expanded (#10).
- Arcs 10-17 reassigned: Severin's COMMITMENT-LOCKED function absorbed by Strand's OVERPERFORMER + flattery vulnerability.
- Laskaris replaces Hardar (name/framing change, mechanics identical).
- Virke's Thread-touched supply chain now personal reputation — Arc 12 strengthened with DISCLOSE/CONCEAL choice.
- Arc 18 (The Stolen Steward) added: Strand-dedicated arc, Cromwell parallel, 2 new event cards.
- Total: 9 arcs, 19 event cards across batch.
- Committed as gm_ref/arcs_10_17_reassignment.md.

### 2026-04-08 — Almud Competence Revision
- King Almud reframed across all arcs: competent Bayesian ruler managing compound-clock problem, not passive or oblivious.
- Arc 11: Crown collapse is tragic (correct decisions, impossible load), not institutional incompetence. New event card: The King's Gambit (HOLD/STRIKE/TRANSITION choices at Stability 1).
- Arc 14: Church offer decision framed as calculated cost-benefit, not confusion. NPC AI decision matrix by Stability level.
- Arc 15: Almud has independent detection channels. New event card: The King's Patience (Almud holds leverage as latent intelligence asset).
- Arc 18: Strand reframed from "unwitting leak" to "monitored honeypot." Almud uses cultivation pattern as intelligence. Strategic Review replaces Discovery. Three-layer intelligence model.
- Informal Almud behavioral profile added for arc consistency. Full NPC entry flagged as [EDITORIAL].
- Recommendation: consolidate three-layer arc documents into single arcs_10_18_v2.md in next pass.
- Committed as gm_ref/arcs_almud_revision.md.

### 2026-04-08 — NPC Mode Interface + Edeyja disposition
- Mode interface matrix added to NPC roster: TTRPG/Hybrid/BG presence for all 13 NPCs.
- 8 new Event Cards designed (Haelgrund Investigation, Haelgrund Defection, Varfell Succession, Brandt Succession, Supply Chain Exposure, Strand Turned, Laskaris Flip, Parish Revolt).
- Edeyja's disposition toward peninsula politics clarified: factions are an environmental hazard, not political actors worth engaging with.
- All 13 NPCs active in ≥ 2 modes. 10 of 13 active in all 3 modes.

### 2026-04-08 — Assassination & Einhir Caste Revision
- Hunting Accident (E-01) woven into Arcs 10, 11, 15, 17. Key addition: accident-was-genuinely-accidental as a valid E-01 resolution (phantom conspiracy worse than real one).
- Einhir north-south caste dynamic woven into Arcs 10, 12, 13, 14, 18. Forgetting as caste enforcement mechanism identified.
- 2 new event cards: The Unanswered Question (Arc 11), The Southern Voice (Arc 14).
- 4 new editorial flags: ED-NEW-7 (Valn name), ED-NEW-8 (dedicated caste arc deferred), ED-NEW-9 (E-01 accidental option), ED-NEW-10 (Insurance File Varfell payload).
- Recommendation: consolidate all revision docs into single arcs_10_18_v2.md. Currently 4 separate files.
- Committed as gm_ref/arcs_assassination_einhir_revision.md.

### 2026-04-08 — NPC Roster Final + Deprecation Pass
- npc_roster_final.md committed as designs/npcs/npc_roster.md (replaces prior version).
- Major addition in final roster: tri-modal NPC presence (TTRPG/Hybrid/BG) with event cards and mode bridges for all 13 NPCs.
- Deprecation headers added to all superseded arc documents:
  - gm_ref/arcs_10_17_historical.md (uses v2 NPC names, superseded by revision chain)
  - gm_ref/arcs_10_17_reassignment.md (interim patch)
  - gm_ref/arcs_almud_revision.md (interim patch)
  - gm_ref/arcs_assassination_einhir_revision.md (interim patch, latest in chain)
- All deprecated files retained for historical record. Each has a DEPRECATED header naming its replacement.
- Next action: consolidate all arc revision documents into a single gm_ref/arcs_10_18_consolidated.md that incorporates all NPC roster final assignments, Almud competence, assassination thread, and Einhir caste dynamics.

### 2026-04-08 — Consolidated Arcs + Valn Terminology
- Valn/Valnese/Einhir terminology canonized: Valn = pre-Altonian Einhir name for the peninsula. Valnese = the people. Einhir = Thread-sensitive nation within the Valnese. Forgetting does not affect the name; using it is a political act. ED-NEW-7 RESOLVED.
- gm_ref/arcs_10_18_consolidated.md committed. Single authoritative arc document for Batch 03.
- Merges all content from 4 deprecated revision docs with all revisions applied in-place:
  - NPC roster final (Strand, Laskaris, Virke expanded, tri-modal)
  - Almud competence (Bayesian ruler, King's Gambit, King's Patience, Strategic Review)
  - Hunting Accident E-01 (woven into Arcs 10, 11, 15, 17; accident-as-truth option)
  - Einhir north-south caste (woven into Arcs 10, 12, 13, 14, 18; Forgetting as enforcement)
  - Valn/Valnese/Einhir terminology throughout
- All 4 deprecated files updated to point to consolidated doc.
- 9 arcs, 25 event cards, 8 gaps, 11 editorial flags (1 resolved: ED-NEW-7).

### 2026-04-08 — E-01 Resolved: Accidental Death
- E-01 (Hunting Accident) resolved as genuinely accidental. No perpetrator exists.
- designs/ttrpg/valoria_narrative_scenario_chains.md Arc 1 fully rewritten:
  - Discovery chain preserved (players still investigate, find faction-constructed false leads).
  - Full evidence (3+ of 4 trails cross-referenced) reveals absence of perpetrator.
  - Partial investigation produces confident wrong answers — false accusations mechanically damaging regardless of factual basis.
  - Accidental truth = most valuable political currency: every faction needs it buried, players hold leverage against all.
  - Almud's response: 1-season self-examination, then overcompensation or reconstructed caution.
  - Every faction's 27-year investment in the assassination narrative revealed as foundationless but load-bearing.
- gm_ref/arcs_10_18_consolidated.md updated: E-01 RESOLVED throughout. ED-NEW-9 and ED-NEW-10 marked RESOLVED.
- Arc 15 (King's Patience) and Arc 17 (Insurance File) updated to reflect accidental resolution.

### 2026-04-09 — Consolidation & Deprecation Pass
- 46 files moved to deprecated/ with DEPRECATED headers:
  - 19 superseded BG evolution files (bg_v01–v04, proposals, syntheses, improvements)
  - 4 gm_ref arc revision files (already had DEPRECATED headers, now physically moved)
  - 7 debate system files (superseded by social_contest_system_v2.md / PP-234)
  - 3 worldbuilding v1/v2 files (superseded by v3)
  - 5 root-level orphan files (workplan, gap register, patch proposals, scope map, project_instructions)
  - 6 stale flat skill files (superseded by dir-based versions)
  - 1 qwen ruleset (non-authoritative LLM output)
  - 1 empty `path` file (deleted)
- 20 compilation/v0.14 stage files: DEPRECATED headers added in-place, naming canonical replacements
- references/file_index.md fully rebuilt to reflect new structure
- No mechanical values changed — pure organizational cleanup
- Commit: fb5bf8865a8f373d8ca36e327ee125df3353e30e
- 8 files flagged for future editorial decision (batch_a–f status, lir_ff_impact, debate_ref_card rewrite)

### 2026-04-08 — NPC Character Analyses
- Deep character analysis for all 13 NPCs committed to designs/npcs/npc_character_analyses.md.
- Each analysis covers: dramatic function, internal contradiction, arc trajectory, thematic role relative to canon (P-01–P-15), historical parallel structural mapping, and behavioral AI consequence chain.
- Key findings: Haelgrund TS reveal is highest-impact personal scene in the roster; Feldhaus-Virke supply chain is highest-impact cross-faction link; Prudence Cardinal's optimisation loop is the most ironic mechanical interaction; Edeyja and Almstedt are fixed-point characters (others arc around them).

### 2026-04-08 — Comprehensive Arc Narrative Analysis
- All 18 arcs (Batches 01-03) evaluated on 5 criteria: emergence quality, table experience, mechanical grounding, NPC fidelity, thematic coherence (1-5 each).
- Portfolio average: 21.3/25. No arc below 18/25.
- Strongest arcs: Arc 1 (Unworked Clause, 23), Arc 3 (Hammer's Reserve, 23), Arc 5 (Quiet Fracture, 23), Arc 9 (Practitioner Who Stopped, 23).
- Weakest arcs: Arc 8 (What Guilds Know, 18), Arc 18 (Stolen Steward, 19).
- Best NPC showcase: Arc 12 (Chained Ships) — 4 NPC flaws interlocking to produce catastrophe.
- Key finding: Batch 03 emergence scores lower than 01-02 due to historical-parallel framework privileging deliberate action over system emergence. Arcs 10, 14, 18 recommended for reclassification as scenario triggers.
- Structural gaps: no arcs for Edeyja, mass combat, Thread operations, Southernmost/Warden, Altonian invasion, Torben succession. 5 NPCs never primary drivers.
- Priority actions: formalise 4 mechanical gaps, add checkpoints to 2 accumulation arcs, generate arcs for 5 uncovered NPCs and 5 uncovered arc types.
- Committed as gm_ref/arc_narrative_analysis.md.

### 2026-04-08 — Existing NPC Character Analyses
- Deep character analysis for 11 existing named NPCs committed.
- Covers: Almud (TS 28 proximity crisis), Lenneth (archive as ontological weapon), Torben (disputed inheritance), Elske (hostage with channels), Vaynard (collector who cannot touch), Baralta (invisible contradiction), Himlensendt (sincere wrong), Klapp (study→perception boundary), Olafsson (instrumentalist corruption), Jarnstal (soldier vs chain of command), Ehrenwall (ledger that never forgives).
- Key findings: Almud's TS 28 is the campaign's latent catalyst; Baralta's Ob 1 deviation cost means Hafenmark IS Baralta; Ehrenwall is the only NPC who cannot be influenced; Olafsson-Haelgrund vertical creates dual-pressure on Church from within.

### 2026-04-08 — Ruler Diamond Foil Analysis + Lenneth Redesign
- Foil diamond analysis: Almud-Lenneth-Baralta-Vaynard mapped across two axes (institutional risk tolerance, Thread engagement motivation).
- All 6 pairings analyzed: Lenneth↔Almud (marriage as stalemate), Lenneth↔Baralta (Catherine enthroned/contained), Lenneth↔Vaynard (archive vs collection), Almud↔Baralta (contradiction seen/blind), Almud↔Vaynard (passive/active TS), Baralta↔Vaynard (universalist/pragmatist).
- Lenneth redesign proposed: stoic queen of simmering conviction, presses Almud while not acting herself. Archive = search for proof that reform-from-above works (postponing the choice between convictions and privileges). Historical echoes: Catherine, Anna Comnena, Melisende.
- Lenneth-Vossen confrontation flagged as campaign's moral reckoning.
- Behavioral AI: RESEARCHER (defaults to more research when pressed to act).

### 2026-04-08 — Extended Foil Network
- Ruler diamond subjective perspectives: each ruler's view of the other three, grounded in conviction/resonant style/ethics, with historical anchors (Charles V, Anna Comnena, Justinian, Frederick II Stupor Mundi).
- 5 triangular foils: Lenneth-Vossen-Baralta (three women/cost of conviction), Almud-Ehrenwall-Himlensendt (king/general/priest), Vaynard-Maret-Lenneth (three Thread scholars), Baralta-Himlensendt-Klapp (three doctrinal speeds), Almud-Lenneth-Edeyja (three Thread levels).
- 5 paired foils: Vaynard-Olafsson (instrumentalist mirror), Lenneth-Torsvald (archive's two readers), Ehrenwall-Almstedt (two clocks), Strand-Baralta (merit and birth), Jarnstal-Brandt (two soldiers/two fixations).
- Key finding: Lenneth-Torsvald pairing implies the archive is a practitioner-development environment — if demonstrated through Torsvald's example, Lenneth's own TS development becomes narratively inevitable.
- Context approaching limit. Recommend new chat for further work.

### 2026-04-08 — Almud Characterization Error Identified
- All three NPC analysis docs contain ~33 instances of Almud-as-paralyzed characterization.
- User correction: Almud is shrewd, guarded, politically capable — not indecisive.
- New lore: Almud suspects his father was assassinated. This informs guardedness.
- Baralta comparison wrong: she governs a smaller scope, not better.
- ED-364 flagged P1: full rewrite required next session.
- Correction plan committed to designs/npcs/almud_correction_plan.md.

## CONTEXT LIMIT — SESSION CLOSE
This session: 17 commits, PP-493–504 (12 patches), 13 NPCs designed, 24 NPCs analyzed, foil diamond + extended network.
Next session priority: ED-364 Almud rewrite, then Church Graduated Seizure simulation.

### 2026-04-09 — ED-364 Almud Characterization Rewrite (P1-BLOCKER resolved)
- Rewrote Almud across 4 files (~41 passages):
  - npc_character_analyses_existing.md: Full rewrite. Manuel I Komnenos anchor. Assassination shadow. Strand-as-honeypot. Baralta scope comparison.
  - ruler_diamond_foil_analysis.md: Axis 2 corrected. All 6 pairings. Almud↔Baralta and Almud↔Vaynard renamed.
  - ruler_diamond_extended_foils.md: All 4 subjective perspectives. All 5 triangles/paired foils where Almud appears.
  - arcs_01_04_nongreedy.md: 8 paralysis→restraint corrections in Arc 1.
- ED-364 resolved. 2 P1-BLOCKERs remaining.

### 2026-04-09 — NPC Characterization Improvements
- Edeyja roster entry strengthened: added Hypatia historical echo, deontological ethics framework, P-08 barrier consequence.
- Almud correction plan archived as COMPLETE.
- NPC audit: all 13 roster NPCs verified for historical echo, behavioral AI, ethics, consequence specification.
- Remaining editorial items: Prudence Cardinal still unnamed (flagged ED-358), stat blocks deferred.

### 2026-04-09 — Stress Test: Church Graduated Seizure (PP-494)
- Modes A + D + J + L completed.
- 5 P1 findings, 7 P2 findings.
- ED-365 through ED-369 raised.
- GAP: Casus Belli mechanic undefined (referenced in PP-494, no definition anywhere).
- ED-355 (Fort Level / Graduated Seizure conflict) flagged as P1 (previously filed as ED only).
- Test output: tests/sim_graduated_seizure_SIM-GS-01.md

### 2026-04-09 — Stress Test: Mass Battle (SIM-MB-01)
- Modes A + D completed across full mass battle subsystem.
- 3 P1 findings (ED-351, ED-352, ED-353), 12 P2 findings, 3 P3 findings.
- ED-351 through ED-357 raised.
- PP-499 applied (Reserve text fix: Phase 4 → Phase 5).
- Test output: tests/sim_mass_battle_SIM-MB-01.md

### 2026-04-09 — Comprehensive NPC Characterization Audit
- Full audit of all 24 named NPCs across 8 criteria (complexity, cliché, emergence, arc interest, importance, precedent quality, cross-NPC interaction, mode coverage).
- Quantitative analysis: mention frequency, interaction network mapping, primary arc driver counts, cliché detection (25+ patterns — zero genuine positives).
- Tier 1 (exceptional): Haelgrund (39/40), Vaynard (38), Ehrenwall (37).
- Tier 2 (strong): Maret Uln (35), Almud (34), Baralta (34), Strand (33), Klapp (32), Almstedt (32), Laskaris (31).
- Tier 3 (solid): Torsvald (29), Virke (30), Feldhaus (27), Brandt (27), Prudence (28), Lenneth (28), Olafsson (27), Edeyja (27), Himlensendt (25), Vossen (24), Elske (24), Solberg (24), Jarnstal (24).
- Tier 4: Torben (22).
- Critical findings: (1) Lenneth has zero mechanical expression despite high narrative importance. (2) Almud has no BG mode presence. (3) Elske has mechanical impact but zero characterization. (4) Haelgrund-Torsvald parallel is the most valuable unwritten NPC interaction. (5) 5 NPCs lack historical echoes.
- 10 structural recommendations prioritised.
- Committed as designs/npcs/npc_comprehensive_audit.md.

### 2026-04-09 — Stress Test: Territory Operations Suite (SIM-TERR-01)
- Modes A + D + J + L across 7 mechanics: Casus Belli, Invading, Seizing, Claiming, Conceding, Trading, Developing.
- 14 P1 findings, 22 P2 findings.
- PP-500–PP-524 applied (25 patches).
- ED-370–ED-376 raised (7 editorials; ED-373 is P1 — Altonian Vanguard stats).
- KEY GAPS CLOSED: Casus Belli fully defined (PP-500,501), Diplomatic Transfer created (PP-505),
  post-Battle unit disposition defined (PP-506,519), three-faction conflict ruled (PP-503),
  race condition on Uncontrolled territory ruled (PP-502), Govern pool stat defined (PP-511),
  Graduated Seizure Fort Level added to Ob (PP-509), pre-TC 75 gate explicit (PP-507),
  Assert/Suppress suspended post-TC 75 (PP-523).
- Next: ED-373 (Altonian Vanguard stats) — P1 blocker for IP clock simulation.

### 2026-04-09 — Elske Characterization Integration (Audit Correction)
- User identified that Elske characterization work (conviction structure, independence paths, Torben tensions, Laskaris admiration/distrust) existed in stage13, Arc 10, Arc 6, Arc 20 but was not integrated into roster or analyses.
- npc_character_analyses_existing.md §4 fully rewritten: four specific tensions enumerated (resentment/duty, protect/exploit Torben, ambition/recoil, Laskaris admiration/distrust), three independence paths, succession states, Evidence resonant style, Anna of Byzantium echo.
- Audit corrected: Elske revised from 24/40 to 33/40 (Tier 2).
- Root cause: audit scored from roster/analyses files only, missing characterization distributed across arc files.

### 2026-04-09 — Editorial Resolution + Patch: SIM-GS-01 P1s
- PP-493, PP-494: retroactive register entries (territory renumber, Graduated Seizure)
- PP-506: Fort Level omitted from Seizure Ob (correct); garrisoned Battle-first rule (ED-355, ED-368 resolved)
- PP-507: Graduated Seizure available at any TC ≥ 15 — no post-75 gate (ED-365 resolved)
- PP-508: OW CV+1 consequence not cap-governed — PP-494 governs; PP-421 stale clause struck (ED-366 resolved)
- PP-509: Prominence assessed at seizure declaration (ED-367 resolved)
- PP-510: Casus Belli defined — one-season token, free Senator Outward + Legionary Ob-1 + coalition justification (GAP-CB resolved)
- PP-511: Mandatory Assert suspended post-TC 75; Assert optional-only in seizure phase (ED-369 resolved)
- ED-365 through ED-369 marked resolved in editorial ledger.
- params_board_game.md updated to v0.9.2.

### 2026-04-09 — Stress Test 2 + Audit + Final Patch
Stress Test 2 (post-patch PP-506-511):
- D2-P1: CB cascade from early seizure degrades Church Mandate systematically
- D5-P1: Battle Partial for garrison gate unresolved → raised ED-371
- F1-P1: Excommunication→Seizure chain exploit if Seizure is free action → raised ED-370 (upgraded to P1)
- 5×P2 additional findings

Audit:
- Completeness: 2 P1 gaps (Seizure Partial, Battle Partial), 2 P2 gaps
- Balance: self-regulating. CB creates timing dial favouring TC≥50 seizure.
- Canon: PASS (P-01–P-15 not applicable)
- Interaction: TD track 4 Ob modifier applies to GS formula — added to params

Final Patch:
- PP-512: Seizure Partial → Contention Marker mechanic
- PP-513: Battle Partial for garrison gate → Church loss, no Seizure
- PP-514: Seizure = free action (no card slot); Excommunication-chain Ob+1 anti-exploit
- PP-515: CB multi-source stacking permitted; 4-CB provisional
- ED-370, ED-371 resolved. ED-372, ED-373 flagged (P2).
- params_board_game.md updated to v0.9.3.

### 2026-04-09 — Stress Test Round 2: Territory Operations (SIM-TERR-02)
- New scenarios: CB under campaign conditions, Diplomatic Transfer exploitation,
  contested-territory cascade, post-Battle retreat chains, Graduated Seizure updated Ob table.
- TCV audit: found P1 errors in victory_architecture_v1.md §1 (T8=3 should be 4, T9=5 should be 3).
- 9 P1 findings, 22 P2 findings.
- PP-525–PP-537 applied (13 patches). ED-377–381 raised.
- KEY GAPS CLOSED: TCV table fixed (PP-525,526), dislodgement Battle roles defined (PP-527),
  retreat timing in multi-Legionary turn defined (PP-529), retreat destination = player choice (PP-530),
  DT consent withdrawal binding (PP-531), bilateral transfer atomic (PP-532), DT Token ownership
  clarified (PP-533), three-faction territory state ruled (PP-536).
- REMAINING P1 BLOCKERS: ED-373 (Vanguard stats), ED-377 (CV starting values).
- Next: designer input on ED-373 and ED-377 required before further clock/Church simulation.

### 2026-04-09 — Stress Test SIM-MB-02 + Patch Audit
- Provisional decisions: ED-351→PP-251 (2-condition trigger), ED-352→Power stat for Volley, ED-353→full Command per sub-unit.
- 9 scenarios run. 1 new P1 finding: ED-358 (§A.8 claim wrong — splitting always superior with full Command per sub-unit).
- PP-500 through PP-504 applied and committed.
- ED-351/352/353/356 resolved by patches. ED-358 raised.
- Test output: tests/sim_mass_battle_SIM-MB-02.md

### 2026-04-09 — Blocker Resolution SIM-MB-03 (ED-354/355/357/358)
- Provisional decisions on all 4 remaining mass battle P1 blockers.
- Stress tests passed. Post-patch validation passed.
- PP-505 through PP-508 applied.
- ED-354/355/357/358 resolved.
- Open mass battle P1 blockers: 0.
- Test output: tests/sim_mass_battle_SIM-MB-03.md


### 2026-04-10 — Comprehensive Multi-System Simulation Batch (SIM-COMPREHENSIVE-01)
Session: 2026-04-10_SONNET_COMPREHENSIVE_SIM
- Ran 9 simulations across 6 new/unrun systems + 3 unpatched P1 gaps.
- Batches: A (wound, AMPLIFY stalemate, Command cap), B (Calamity Radiation, Clock Registry, Victory Architecture race), C (co-victory pairings, RM Cultural Uprising calibration).
- P1 findings: 9 total (AMPL-01 stalemate, CMD-02 size cap, CR-01/02 BG/Hybrid radiation, CLK-03 PI thresholds, VIC-02 Crown timeline, VIC-06 Hafenmark dominance check, CO-02 Varfell+RM infeasibility, VIC-RM-01 Phase 1 conflict).
- Provisional patches: AMPL-01, CMD-01, CR-01, CR-02, CLK-01 (PI), VIC-01, VIC-RM-01.
- Gaps logged: 11 (GAP-CR-01/02, GAP-WOUND-01/02, GAP-AMPL-01, GAP-CLK-01/02/03, GAP-VIC-01/02, GAP-VIC-RM-01).
- Clean scenarios: 8 confirmed.
- Test output: tests/sim_comprehensive_batch_2026_04_10.md
- REMAINING P1 BLOCKERS: ED-373 (Vanguard stats), ED-377 (CV starting values) — unchanged from prior session.
- NEW BLOCKERS: GAP-CR-01 (RS decay season/year conversion), PI thresholds (CLK-03/provisional applied).

### 2026-04-10 — Balance Patches PP-540–546
- 7 balance patches applied to victory_architecture_v1.md.
- Solo victory paths: all normalised to 12–16 seasons. Crown −6 seasons (PP-540: TCV 16→14, rivals 3-of-3→2-of-3). Hafenmark +2 seasons (PP-541: TCV 12→13). Varfell C −2 seasons (PP-542: VTM 5→4). RM −2 seasons (PP-543: Phase 1 5→4 territories; also resolves F-VIC-RM-01 §3.5 vs PP-478 conflict).
- Co-victories: Crown+Hafenmark slowed +3 seasons (PP-544: PI 5→7). Varfell+RM made viable −8 seasons (PP-545: VTM 4→3, territories 4→3). Hafenmark+RM −6 seasons (PP-546: territories 4→3).
- All interaction checks passed. No condition inversions.
- Commit: balance

### 2026-04-11 — Deed-Monarchy, Altonian Containment, Caste Reconciliation, Ruler Diamond Repositioning

**Major lore decisions (all canonical):**

1. **Altonian containment of the Church** — British India parallel. Accommodation not suppression. Himmelenger (T14) as quarantine grant. Church incubated over 200 years. Church learns reverse-containment strategy. (ED-393)

2. **Deed-monarchy** — First Almqvist = Almud's father, military leader consecrated by Church. Carolingian model. Two generations to game start. Deed-presumption rebuttable. Cognatic succession native to deed-logic. (ED-394)

3. **Cadet branches as deed-families** — Political proximity from wartime service, not blood. (ED-395)

4. **Caste system** — Geographic gradient from Southernmost. Southern Einhir stigmatised. Structural exclusion from war coalition. Not formal law, but structural consequence. TS distribution follows caste gradient. (ED-397)

5. **Baralta** — Wants the Crown (active ambition). Unmarried, childless, heirless. Henry VIII parallel. Pure RM adversary. Would suppress RM more aggressively than Church. (ED-396)

6. **Almud** — TS 0. Governance pragmatist + ethical doubt. Not secret sympathiser. Discovery Event = rupture. Complicit through cost-benefit, not malice. (ED-398)

7. **Lenneth** — Institutional Einhir revivalist. Catherine the Great parallel. Crown as patron of cultural revival. Thread work eventual horizon. Lenneth↔Baralta = campaign-defining confrontation. (ED-399)

8. **Vaynard** — Southern Einhir heritage. Von Lohengramm parallel. Wants Church + Altonian residue expelled. TS from environmental exposure. Forgetting as political prison. (ED-400)

9. **Himlensendt** — Structural keystone. Consecration crisis with Baralta. Pastoral compassion = ethnic suppression. Vaynard = existential heretic. (ED-401)

10. **NPC roster caste-axis annotations** — All 13 roster NPCs assessed against caste system. Caste is load-bearing for entire NPC ecosystem. (ED-405)

**Files committed:**
- canon/03_canonical_timeline.md (major rewrite)
- designs/npcs/npc_character_analyses_existing.md (complete rewrite)
- designs/npcs/npc_roster_caste_annotations.md (new companion doc)
- canon/editorial_ledger.yaml (ED-393 through ED-407)
- session_log_current.md (this entry)

**Open editorial items from this session:**
- ED-403: Vossen position on Lenneth's programme / RM internal split (P2)
- ED-406: Ehrenwall succession assessment re Baralta (P2)
- ED-407: Himlensendt consecration crisis — which path? (P2)

**Files requiring follow-up rewrite (not in this commit):**
- designs/npcs/ruler_diamond_foil_analysis.md — all pairings need rewriting for new positions
- designs/npcs/ruler_diamond_extended_foils.md — all subjective perspectives need rewriting (especially Almud's view, which references TS 28 and Einhir sympathy)
- gm_ref/arcs_01_04_nongreedy.md — Arc 1 (Sovereign Constraint) needs reframing for new Almud
- gm_ref/arcs_05_09_batch02.md — check for Almud/Baralta characterisation dependencies
- designs/gm_ref_cp14/arcs/arcs_09_11_elske_baralta.md — Arc 9 needs consecration crisis addition

**Next session priority:** Rewrite ruler_diamond_foil_analysis.md and ruler_diamond_extended_foils.md for new positions. Then Arc 1 reframing.

### 2026-04-11 — Foil Analysis and Extended Foils Rewrite (commit 2)

- ruler_diamond_foil_analysis.md: Complete rewrite. All 4 axes, all 6 pairings repositioned for deed-monarchy, caste reconciliation, new ruler positions.
- ruler_diamond_extended_foils.md: Complete rewrite. All 4 subjective perspectives. Almud view corrected (TS 0, no sympathy, governance pragmatism). Himlensendt and Ehrenwall positions relative to diamond. 4 triangular foils.
- Next: Arc 1 reframing for new Almud (Sovereign Constraint → governance uncertainty).

### 2026-04-11 — Arc Reframing (commit 3)

- gm_ref/arcs_01_04_nongreedy.md: Arc 1 narrative reframed. "Almud knows it is wrong" → "Almud manages governance costs while privately doubting." Sovereign Constraint seed updated. Mechanical chain preserved (costs identical). Cross-arc references updated.
- designs/gm_ref_cp14/arcs/arcs_09_11_elske_baralta.md: Arc 9 Baralta characterisation updated (sovereign supremacy, not constitutional hygiene). Consecration crisis extension added (ED-407). Both consecration outcomes sketched with provisional mechanical implications.
- **Session total: 3 commits, 8 files modified/created, ED-393 through ED-407 (15 editorial items: 12 resolved, 3 open).**
- **Next session priority:** ED-403 (Vossen/RM internal split on Crown patronage), ED-406 (Ehrenwall succession assessment), ED-407 (consecration crisis path decision).

### 2026-04-11 — Stale Reference Cleanup + ED-403/406/407 Resolution (commit 4)

- gm_ref/arcs_10_18_consolidated.md: Fixed stale Almud TS 28 / Einhir sympathy / Belief 2 references.
- designs/gm_ref_cp14/arcs/arcs_01_04_rebuilt.md: Fixed stale Almud TS 28 / sympathises references.
- designs/npcs/ed_403_406_407_resolutions.md: New file — ED-403 (RM split mechanic), ED-406 (Ehrenwall succession assessment), ED-407 (consecration crisis conditional mechanic).
- canon/editorial_ledger.yaml: ED-403, ED-406, ED-407 resolved.
- **Session total: 4 commits, 12 files modified/created, ED-393 through ED-407 (15 editorial items, all resolved).**
- **No remaining open editorial items from this session.**

## CONTEXT LIMIT — SESSION CLOSE
This session: 4 commits. Deed-monarchy, Altonian containment, caste reconciliation, ruler diamond repositioning, all arc dependencies updated, all editorial items resolved.
Next session priority: Check arcs_05_09_batch02.md for any remaining stale Almud/Baralta references (none found in grep but full review recommended). Then simulate the consecration crisis mechanic (ED-407) to verify Church Stability thresholds produce balanced outcomes.

### 2026-04-11 — Baralta Crown Claim Mechanic + Consecration Crisis Simulation (commit 5)

- arcs_05_09_batch02.md: Full manual review — no stale references found. Clean.
- designs/mechanics/baralta_crown_claim_mechanic.md: New file. Crown Succession Contest, Stake Claim Domain Action, Consecration Crisis BG expression, simulation of three scenarios (early/mid/late game). Four editorial decisions made (ED-408 through ED-411), all provisional/flagged.
- **Key design finding:** The strategic sweet spot for Baralta is weakening Church to Stability 3 before claiming — creating tension between TC suppression interest and consecration preparation. Four preconditions for viable claim: Crown Mandate ≤ 2, PI ≥ 5, Church Stability ≤ 3, Hafenmark PI ≥ 4.
- **Session total: 5 commits. ED-393 through ED-411 (19 editorial items: 15 resolved, 4 provisional/flagged).**

### 2026-04-11 — Final Cleanup + Mechanical Gap Assessment (commit 6)

- references/file_index.md: Updated with 3 new files from this session.
- ED-412: Crown Einhir Revival Domain Action — provisional design for Lenneth's BG expression.
- ED-119 escalated to P1-BLOCKER: Lenneth full design now critical. Without it, Lenneth-Baralta confrontation (campaign-defining per new characterisation) has no mechanical expression.
- Varfell Church expulsion: no new mechanic needed — standard faction elimination covers it. Vaynard's agenda is characterisation driving standard play, not a unique mechanic.

## CONTEXT LIMIT — SESSION CLOSE (FINAL)
**This session: 6 commits. 21 editorial items (ED-393 through ED-412 + ED-119-URGENCY).**

Canonical changes made:
1. Altonian containment of Church (British India parallel, Himmelenger as quarantine grant)
2. Deed-monarchy (first Almqvist = Almud's father, military leader, Church-consecrated)
3. Caste system (geographic gradient, structural exclusion, TS distribution follows caste)
4. Baralta: wants Crown, Henry VIII sovereign supremacy, pure RM adversary, unmarried/childless
5. Almud: TS 0, governance pragmatism + ethical doubt, Discovery Event = rupture
6. Lenneth: institutional Einhir revivalist, Catherine the Great, sincere + strategic
7. Vaynard: southern Einhir heritage, von Lohengramm, Church expulsion agenda
8. Himlensendt: structural keystone, consecration crisis conditional on Church Stability
9. All NPC roster annotated for caste-axis impact
10. Crown Succession Contest + Baralta Stake Claim + Consecration Crisis BG mechanics

**Next session priority:** ED-119-URGENCY — Lenneth full design (stat block, TS development, BG Domain Action). Then simulate Crown Succession Contest to verify pool balances. Then Lenneth-Baralta confrontation mechanic.

### 2026-04-11 — Emergent Interdependent Arcs (commit 5)

- gm_ref/arcs_36_40_interdependent.md: New file. Five interdependent emergent arcs (36-40) with mandatory cross-dependencies.
  - Arc 36: The Tithe That Fed the Enemy (Prudence Cardinal tithe loop → RM recruitment → Church self-sabotage)
  - Arc 37: The Heresy in the Warehouse (Feldhaus/Virke supply chain → convergent investigations)
  - Arc 38: The Sandcastle Alliance (Laskaris/Solberg convergent IP suppression → shield collapse)
  - Arc 39: The Practitioner They Didn't Know They Had (Vaynard hidden TS growth → Discovery Event → Coherence burn)
  - Arc 40: The Weight That Broke the Balance (convergence of all four → institutional collapse → succession)
- canon/editorial_ledger.yaml: ED-408 through ED-412 added (5 new open items).
- Cross-arc interaction table maps 11 interdependencies. Convergence timeline: seeds seasons 1-2, converges seasons 7-8.
- Next: User review of ED-408-412. Simulate convergence timing.

### 2026-04-11 — Lenneth Full Design + Threadwork at Key Decision Points (commit 7)

- designs/npcs/lenneth_threadwork_design.md: New file. Lenneth stat block (TS 8 starting, Cognition 5, Spirit 4). Archive-based TS development path. Breakthrough condition. Cultural Revival Track (0-10 clock). BG mode expression.
- Threadwork applied to all ruler diamond decision points:
  - Almud Discovery Event: TS growth check at Ob 2, ~15% success at Spirit 3. Failure = unfileable memory. Success = existential rupture.
  - Baralta foreclosure: triple-barrier Ob 4 on TS growth. She will never perceive Thread reality. The most competent governor governing the wrong problem.
  - Vaynard's Forgetting prison: TS 20 (provisional). Can perceive but cannot communicate. Non-practitioner audience P(retaining testimony) ≈ 1-7%.
  - Lenneth's development: TS 8→20 (~Season 6) → 30 (~Season 11). Each threshold transforms her programme's scope.
  - Himlensendt's Lock encounter: P(Success) ≈ 25% at Spirit 5. Override condition for consecration crisis.
  - Caste as TS gradient: south = high TS + low Church + Forgetting resistance. North = low TS + high Church + Forgetting vulnerability.
- Key finding: "The settlement is self-consuming." Every faction's rational political actions contribute to RS degradation. The Einhir Catastrophe replicated politically.
- references/params_threadwork.md: Lenneth TS 72 dissolved, replaced with TS 8 + development path.
- ED-408-412 confirmed canonical. ED-413-418 created (6 new, 5 resolved, 1 open). ED-119/ED-119-URGENCY resolved.
- **Session grand total: 7 commits. ED-393 through ED-418 (26 editorial items: 23 resolved, 2 flagged-resolved, 1 open).**
- **Open: ED-416 (Almud stat block — Spirit value determines Discovery Event probability).**

## CONTEXT LIMIT — SESSION CLOSE
Next session: Almud stat block (ED-416). Then simulate the Cultural Revival Track to verify pacing (does Lenneth reach TS 30 before RS enters Fractured band? The timing determines whether the institutional bridge to Edeyja is available before the crisis becomes unrecoverable).

### 2026-04-11 — Comprehensive Narrative Analysis + Arc Library Audit + Corrections
Session: 2026-04-11_OPUS_NARRATIVE_AUDIT
- Comprehensive character/setting/arc analysis performed across full GitHub narrative corpus (~32 files fetched).
- Consolidated character cards produced for all principal NPCs (Almud, Lenneth, Baralta, Vaynard, Ehrenwall, Himlensendt, Elske) synthesizing distributed characterization across stage13, stage6, batch_d, canonical timeline, narrative scenario chains, and arc documents.
- Editorial additions proposed: Reinhardt archetype for Vaynard (user-confirmed), Catherine the Great for Lenneth (user-confirmed), Isabella I for Baralta (user-confirmed). Personal histories, Beliefs, ethical approaches, compromises, relationships, and inspirations added for all principals. 48 editorial items registered (ED-CHAR-01 through ED-CHAR-38, ED-ARC-01 through ED-ARC-04).
- Self-audit performed: identified P-08 violations (TS-as-inheritance for Almud and Vaynard mothers), dead-mother cliché ×2, Lenneth TS 5 contradiction with P-08/§10.1. Corrections recommended.
- Four new emergent arcs proposed and atomized: The Architect's Hand (Lenneth coup, Catherine parallel), The Babington Letters (conspiracy to install Elske), The Cathedral Blood (Pazzi conspiracy via Jarnstal independence), The Tudor Settlement (post-victory consolidation).
- All four arcs reformulated as fully emergent with NPC AI behavioral profiles, mechanical trigger conditions, mermaid flowcharts, and mode-dependent trigger tables.
- Trigger review performed: 6 mechanical errors corrected (Lenneth threshold too low, Elske Loyalty threshold meaningless, Cathedral TC too high, Niflhel presence undefined, detection paths too narrow, missing NPC AI).
- Comprehensive arc library audit: ~47 arcs across 13 documents assessed for emergence quality (47% Grade A, 38% Grade B, 15% Grade C, 0% scripted), mechanical consistency, and interdependencies.
- P1 corrections committed (a1ce5e02): IP 30→40 (Arc 20), TC 60→Graduated Seizure/TC 75 (Arc 13), Reach→Influence + Baralta Mandate ≥4 (Arc 9), Schoenland T15→T16 (Arc 25), Collision D invalidated by E-01.
- Threadwork probability analysis run on 13 key arc decision points. Critical finding: Crown Suppress TC was non-functional (~1% success rate). Fixed: PP-547 (6758b586) — Suppress Ob = Church Mandate ÷ 2 (round up, min 1).
- 7 P1 issues identified and 6 corrected. Remaining P1: Southernmost design-layer document (4 arcs depend on undefined mechanics), GAP-ARC-01 (Niflhel Quiet deployment RS/TT cause undefined).
- Duplicate/stale arc files identified for deprecation: valoria_emergent_campaign_arcs.md, valoria_emergent_arcs_experimental.md.
- Arc density management gap identified — no tool exists. Arc Priority Matrix proposed.
- 6 unexpected cross-arc interactions documented (Babington↔Hunting Accident, Cathedral↔Quiet Fracture, Lenneth coup↔Practitioner Who Stopped, Tudor↔Baralta dynasty, Framework Trap as permanent modifier, Empty Fort dual-nature under different crises).
- REMAINING P1 BLOCKERS: ED-373 (Vanguard stats), ED-377 (CV starting values), Southernmost design document, GAP-ARC-01.
- Next: simulate arc divergence on key roll outcomes; deprecate stale arc files; create Arc Priority Matrix for GMs.

## SESSION CLOSE — FINAL (2026-04-11)

**8 commits. 17 files modified/created. 26 editorial items (ED-393 through ED-418). 24 resolved, 1 open (ED-416: Almud stat block), 1 escalated and resolved (ED-119).**

### Commit Log
| # | SHA | Scope |
|---|-----|-------|
| 1 | 701eacf | Timeline, character analyses, roster annotations, ED-393-407 |
| 2 | da2e2c5 | Foil analysis + extended foils rewrites |
| 3 | abe1b1e | Arc 1 Almud reframing + Arc 9 consecration crisis |
| 4 | 9e763fb | Stale ref cleanup + ED-403/406/407 resolved |
| 5 | 26b7442 | Baralta Crown Claim mechanic + consecration simulation |
| 6 | f1a5e77 | File index + ED-412 + ED-119 escalation |
| 7 | 4660a27 | Lenneth full design + threadwork at decision points |
| 8 | (this)  | Propagation, file index, session close |

### Propagation Debt (for next session)
- params_board_game.md: Crown Succession Contest, Stake Claim DA, Consecration Crisis NOT YET INTEGRATED
- params_threadwork.md: Cultural Revival Track and Lenneth breakthrough condition NOT YET INTEGRATED (in design doc only)

### Next Session Priority
1. ED-416: Almud stat block (Spirit value determines Discovery Event probability)
2. Integrate Baralta Crown Claim mechanics into params_board_game.md
3. Simulate Cultural Revival Track pacing vs RS degradation (does Lenneth reach TS 30 before RS enters Fractured band?)


### 2026-04-11 — Arc Register Creation and Threadwork Simulation
Session: 2026-04-11_OPUS_ARC_REGISTER
- Created arc register from scratch — iterated through 6 versions.
- v1: 35 named arcs. v2: audit-corrected (Baralta→Hafenmark, TC suppression ≥4, RS cross-clock error removed, 11 arcs added). v3: recent commit review (Klapp→Temperance, Almud ED-364, Baralta Crown ambition, Lenneth-Baralta collision, Jarnstal drift, 8 NPC corrections). v4: abe1b1e review (ED-407 consecration mechanics) + 7 new emergent arcs from PP-428–442 and foil analysis + 2 new collisions (Succession/Einhir Triangles). v5: threadwork decision point analysis (8 decision points, 4 new arcs: Lock Distribution, Mending Trap, Lattice of Enemies, Overweaving Cascade). v6: branch simulation (7 key rolls, 2 new arcs: Governance Pause, Edeyja Burnout).
- Final count: 8 principal + 34 secondary + 19 tertiary + 12 NPC = 73 arcs + 7 collision scenarios.
- Key findings: Excommunication mechanic non-functional at game-start stats (GAP-ARC-05). Klapp Ob 2 is single most impactful Ob modifier. Ceiral Ritual 7% failure → endgame spiral. Edeyja burnout = hidden fail state. Mending structurally insufficient without WC + Community Weaving + Lock resolution. Endgame collective ops Belief-gated.
- Files committed: references/arc_register.md, tests/threadwork_decision_point_analysis.md, tests/arc_branch_simulation.md

- Delay vs preclusion evaluation: 6 of 7 key rolls reclassified as Pure Delay or Costly Delay. Only ARC-T05 (Ehrenwall Medicine) is True Preclusion. Klapp Ob 2 buys ~1-2 seasons, not permanent branch. Ceiral failure = Costly Delay (retryable, RS -8 + 2-season delay), not endgame spiral. GAP-ARC-05 reclassified as intentional gated mechanic. ARC-S32/S34 reframed as resource-exhaustion arcs.
- Key insight: failed Costly Delay rolls don't create new arcs — they accelerate existing arcs. Clocks don't branch on failure; they accelerate.
- Files: references/arc_register.md v7, tests/delay_vs_preclusion_evaluation.md

### 2026-04-11 — Emergent Interdependent Arcs Batch 2 (commit 6)

- gm_ref/arcs_41_45_interdependent.md: New file. Five arcs exploiting under-explored cross-system triggers:
  - Arc 41: The Inquisitor's Unravelling (Haelgrund TS 12 + calamity radiation at Fractured RS → self-discovery)
  - Arc 42: The Debate That Changed the World (contest system Thread co-movement → RS +1 from parliamentary speech)
  - Arc 43: The Battle That Ate the South (mass battle RS ×3 at T6 Stillhelm + calamity radiation cascade)
  - Arc 44: The Invisible Majority (triple-source CV erosion → RM Phase 1 threshold without RM action)
  - Arc 45: The Tutoring Demand That Started a War (IP ≥ 40 + depleted Crown + intelligence leak = zugzwang)
- 35 unique triggers catalogued (T-01 through T-35).
- 4 bidirectional destabilising loops identified.
- Full 10-arc convergence timeline mapped (seasons 1–11+).
- canon/editorial_ledger.yaml: ED-413 through ED-417 added (5 new items, 1 P1-BLOCKER: ED-416 RM hold mechanic).
- **Session total: 6 commits, 10 emergent arcs (36–45), ED-408 through ED-417 (10 editorial items: all open).**

## SESSION CLOSE

This session: 6 commits. Deed-monarchy continuation + 10 emergent interdependent arcs across 2 batches.
P1-BLOCKER: ED-416 (RM hold T9 mechanic — no Military stat, cultural displacement proposed).
Open editorial items: ED-408 through ED-417 (10 items).
Next session priority: Resolve ED-416 (P1-BLOCKER). Then simulate convergence timeline — stress test the 4 bidirectional loops for runaway conditions. Review ED-414 (debate RS frequency) as it affects RS balance across Arcs 42/43.
