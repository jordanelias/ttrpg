# Valoria Session Log — Current

```yaml
session_id: 2026-04-12_SONNET_ED358_AUDIT
session_close: 2026-04-12
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Audited ED-358 "13-character NPC roster" — found to be false debt
2. All 13 NPCs documented in canonical params files
3. ED-358 struck; ED-358b added (Lenneth TS P3 only)
4. PP-574 committed

## FINDING
ED-358 was raised during a simulation session when some NPCs were provisional.
Subsequently documented: Cardinals (BG mechanics), Torben/Elske (loyalty tracks),
Maret Uln (PP-486), Almud/Baralta/Vaynard (faction leader profiles), Edeyja (Warden
mechanics), Lenneth (arc-dependent, documented as such).
Only genuine gap: Lenneth TTRPG TS (P3, non-blocking).

## P1 BLOCKERS: 0
## OPEN EDITORIALS: 1 (ED-358b, P3, non-blocking)
```

---


---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-12_SONNET_ALL_EDITORIAL_RESOLVED
session_close: 2026-04-12
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Resolved all remaining 28 open editorial items
2. PP-569-573: file patches for mechanical and worldbuilding resolutions
3. P1 blocker count: 0 (all 11 P1s resolved across this session batch)

## PATCHES (PP-569-573)
PP-569: ED-339/347/348 — Partition non-winner clarification; Cardinal cap none; Löwenritter T14 coup rule
PP-570: ED-316 — Weight-of-numbers Size > 2×Command Morale check [PROVISIONAL]
PP-571: ED-388 — Hafenmark Stability ≥ 3 gate on Parliamentary Sovereignty [PROVISIONAL]
PP-572: ED-391 — Crown+Hafenmark 4-season no-conflict co-victory condition [PROVISIONAL]
PP-573: ED-364 — Almud characterization updated [PROVISIONAL — for Jordan review]

## EDITORIALS RESOLVED (no patch needed — already in text or confirmed)
ED-080/081: Baralta/Vaynard conviction texts already defined.
ED-302/304/305/307: Confirmed decisions already in text.
ED-303: Rendering Stability name retained.
ED-308/309: Varfell/Baralta succession already resolved PP-486/487.
ED-349: Soften action struck as scope error.
ED-350: Domain Echo resolved PP-329.
ED-361: PI cascade already in text.
ED-362: Dissonant Thread already in text PP-502.
ED-363: PP-249 Overwhelming confirmed canonical.
ED-384: Varfell+RM aspirational — confirmed.
ED-386: arc/campaign not a systematic issue.
ED-387: Hafenmark path resolved PP-541.
ED-390: WC -1 Ob confirmed (not -2).

## FLAGGED FOR JORDAN REVIEW (all marked [PROVISIONAL])
ED-316: Weight-of-numbers trigger threshold and scale
ED-340: Vanguard identity, invasion route, elimination narrative
ED-358: 13-character NPC roster (full design required)
ED-364: Almud conviction text and characterization rewrite
ED-388: Hafenmark Stability gate (faction-feel)
ED-391: 4-season no-conflict condition (faction-feel)

## STATE
P1 blockers: 0
Open editorials: ~0 (all resolved or flagged [PROVISIONAL] for Jordan)
```

---


---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-12_SONNET_ED_BATCH_RESOLUTION
session_close: 2026-04-12
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Full audit and editorial resolution batch (PP-560-568)
2. 11 P1 blockers addressed (8 resolved, 3 flagged authorial)
3. 24 P2 items addressed (18 resolved, 6 flagged authorial)

## PATCHES APPLIED (PP-560 to PP-568)
PP-560: ED-313 — PI≤2 TC+2 does not apply when TC frozen. ED-314 — stale Seizure formula corrected.
PP-561: ED-342/343 — Crown+Hafenmark co-victory: Hafenmark TCV ≥ 12, Mandate ≥ 4 both factions.
PP-562: ED-344 — Royal Decree Fragmentation +2 Ob → +1 Ob.
PP-563: ED-345 — VTM TC contribution defined (+0.5/1/1.5 per season at VTM 3/4/5).
PP-564: ED-346 — Ministry Priority 3 → automatic procedural delay; AP-token consumed.
PP-565: ED-328+341 — Temperance AER advancement requires roll; AER decay added.
PP-566: ED-338 — Partition Pressure public marker mechanic.
PP-567: ED-351 — Discipline degradation: PP-320 Power-asymmetry struck; PP-251 canonical.
PP-568: ED-340 — Vanguard mechanics [PROVISIONAL].

## CLOSED WITH NO PATCH (already resolved in text or confirmed)
ED-312 (suppress defined), ED-315 (Echo cap exists), ED-317 (AMPLIFY=CROSS, Spent exit),
ED-329 (Torben correct), ED-353 (Command PP-504), ED-356 (Shield Wall PP-500),
ED-360 (confirmed), ED-383, ED-385, ED-389, ED-392.

## FLAGGED AUTHORIAL (require Jordan decision)
ED-308: Varfell succession / Maret Uln
ED-309: Baralta succession mechanic
ED-316: Weight-of-numbers for Size > Command units
ED-340: Vanguard identity/route/elimination narrative [PROVISIONAL applied]
ED-364: Almud characterization rewrite
ED-384: Varfell+RM co-victory aspirational vs bug
ED-387: Hafenmark passive victory path scope
ED-388: Hafenmark Stability gate
ED-391: Crown+Hafenmark 4-season no-conflict condition

## OPEN EDITORIALS REMAINING
See editorial_ledger.yaml. ~31 items remain open (primarily authorial worldbuilding,
session-specific balance confirmations, and older simulation debt).
```

---


---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-11_SONNET_AUDIT_ED_RESOLUTION
session_close: 2026-04-11
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Full cross-system mechanical audit (Modes A-G) post PP-548-554
2. 8 findings identified and patched
3. ED-370 through ED-378 resolved (9 editorial items)
4. PP-555 through PP-559 committed

## COMMITS THIS SESSION
- PP-548-554: Formula/range unification + Certainty redesign + PT rename
- PP-555-559: Audit findings + ED-370-378 resolution

## AUDIT FINDINGS (PP-555)
P1 resolved: 2
  - BG Commander bonus floor+1 → floor (pool bonus, not Ob); Military-0 now correctly 0D
  - RDT row-6 orphan merged into row-5; removed
P2 resolved: 3
  - RDT header stale 0-6 → 0-5
  - 'Conviction value' stale text → 'Piety value' (2 files)
  - params_threadwork Certainty PP-283 refs updated to PP-551; stale flag resolved

## EDITORIAL RESOLUTIONS (PP-556-559)
ED-370: Hybrid Diplomacy→Treaty bridge — personal success queues -1 Ob Echo (PP-556)
ED-371: Coalition suppression auto-trigger — confirmed as designed (PP-557)
ED-372: Thread Liaison dissolution — prospective only (PP-558)
ED-373: Diplomatic Token — suspended in submitted/vassal state (PP-559)
ED-374: Social modifiers — excluded from floor+1; damage components confirmed
ED-375: Progress tracks — 0-base category confirmed
ED-376: Parliament Integrity — 0-20 cumulative pressure meter confirmed
ED-377: Submission exception — Mandate-0 vassal state explicit exception to floor-1
ED-378: RDT 0-5 — step-6 merged into step-5; complete

## OPEN EDITORIALS (carried forward — pre-existing)
ED-383: Crown victory timeline (P2)
ED-384: Varfell+RM co-victory (P2)
ED-385: RS→PT erosion cascade (P2)
ED-386: Cultural Uprising arc definition (P3)
ED-387: Hafenmark passive victory path (P2)
ED-388: Hafenmark Stability gate (P2)
ED-389: Varfell Path A feasibility (P2)
ED-390: RM Phase 2 WC bonus (P3)
ED-391: Crown+Hafenmark co-victory (P2)
```

---


---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-11_SONNET_FORMULA_RANGE_UNIFICATION
session_close: 2026-04-11
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. PP-547: Mandate→Ob floor+1 for 6 instances in params_board_game (initial commit)
2. Cross-system range and formula audit (all canonical files)
3. Formula unification proposal — 24 confirmed changes across 5 files
4. Certainty track redesign: struck old epistemological track; new cosmological worldview journey (0-5 oscillating)
5. PP-548-554: Full commit — formula standardisation, naming, range fixes, Certainty, Ministry triggers

## COMMITS THIS SESSION
- PP-547: Mandate-Ob formula standardisation (params_board_game only — initial)
- PP-548-554: Full formula/range/naming/Certainty unification commit

## PATCHES APPLIED (PP-548 to PP-554)
PP-548: All stat÷2 Ob formulas → floor(stat/2)+1 in params_board_game (11 instances)
PP-549: PP-547 extension — params_factions, victory_arch, social_contest, mass_battle (9 instances)
PP-550: BG Commander bonus: floor(Military/3) max+2D → floor(Military/2)+1 (÷3 eliminated)
PP-551: Certainty track redesigned (old PP-289 struck; new 0-5 cosmological journey)
PP-552: CV (territory Conviction) renamed → PT (Piety Track) across all files
PP-553: Range fixes — PI 0-20, TC 0-75, TS cap 100, RS mode labels, Prosperity 1-7, RDT 0-5, clock_registry updated
PP-554: Ministry Mandate=0 triggers → Mandate≤1

## DESIGN DECISIONS LOCKED THIS SESSION
- floor(stat/2)+1 for all stat÷2 Obs and capacity derivations
- No ÷3 anywhere in the system
- Faction stats: 1-7, floor 1 (Stability: 0-7 for BG faction elimination only)
- Oscillating trackers: 0-5
- Territory Prosperity: 1-7
- Certainty: redesigned as Solmund→Thread cosmology journey (0-5)
- CV → PT (Piety Track) rename
- Social combat modifiers excluded from floor+1 (ED-374)
- Progress tracks: 0-base permitted (ED-375)
- PI as cumulative pressure meter 0-20 (ED-376, provisional)
- Submission Mandate-0 exception (ED-377, provisional)
- RDT 0-6 → 0-5 (ED-378, provisional)

## OPEN EDITORIALS (carried forward)
ED-370: Hybrid personal scene -> BG Treaty bridge (P2)
ED-371: Coalition suppression dominant strategy confirmation (P2)
ED-372: Thread Liaison dissolution timing (P2)
ED-373: Token on Mandate-0 suspension (P3)
ED-374: Social combat modifiers floor+1 exclusion (flagged)
ED-375: Progress track scale category (flagged)
ED-376: Parliament Integrity 0-20 classification (flagged, provisional)
ED-377: Submission Mandate-0 exception (flagged, provisional)
ED-378: RDT step-6 consolidation (flagged, provisional)
```

---


---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-11_SONNET_MANDATE_OB_FIX
session_close: 2026-04-11
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Applied PP-547: standardised all Mandate-derived Obstacle formulas to floor(Mandate / 2) + 1
   - 6 instances corrected in params_board_game.md
   - Raw Mandate and ceiling formulas both unified
   - PP-180 / PP-296 cap of 4 removed (formula is self-scaling)

## COMMITS THIS SESSION
- [patch] Mandate-Ob formula standardisation — PP-547

## OPEN EDITORIALS (carried forward)
ED-370: Hybrid personal scene -> BG Treaty bridge (P2)
ED-371: Coalition suppression dominant strategy confirmation (P2)
ED-372: Thread Liaison dissolution timing (P2)
ED-373: Token on Mandate-0 suspension (P3, provisionally applied PP-517)
```

---


---

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

### 2026-04-11 — Arc Register Build, Threadwork Simulation, Branch Analysis
Session: 2026-04-11_OPUS_ARC_REGISTER

**Created arc register (references/arc_register.md) — iterated through 7 versions:**
- v1–v2: 35→46 arcs. Audit-corrected 9 errors (Baralta→Hafenmark, TC suppression ≥4 not ≥5, RS cross-clock removed as non-canonical, Coup Counter increments corrected, Vaynard TK TC per-level, Baralta excommunication TC +4, Mass Battle ×3).
- v3: Recent commit review. 8 NPC corrections (Klapp→Temperance, Almud ED-364, Baralta Crown ambition, Lenneth Institutional Revivalist, Vaynard southern Einhir TS, Ehrenwall deed-logic, Jarnstal Fortitude, Himmensendt consecration crisis). 3 arcs added (Lenneth-Baralta Collision, Consecration Crisis, Jarnstal Drift).
- v4: abe1b1e review (ED-407 consecration mechanics). 7 new emergent arcs from PP-428–442 and foil analysis. 2 new collisions (Succession Triangle, Einhir Triangle).
- v5: Threadwork decision point analysis (8 decision points tested). 4 new arcs (Lock Distribution, Mending Trap, Lattice of Enemies, Overweaving Cascade).
- v6: Branch simulation (7 key rolls). 2 new arcs (Governance Pause, Edeyja Burnout). GAP-ARC-05 (Excommunication non-functional at baseline — reclassified as intentional gated mechanic).
- v7: Delay vs preclusion evaluation. 6/7 rolls reclassified as delays. Only ARC-T05 (Ehrenwall Medicine) is True Preclusion.

**Final register: 8 principal + 34 secondary + 19 tertiary + 12 NPC = 73 arcs + 7 collision scenarios.**

**Key findings:**
- Excommunication mechanic is a gated design: near-impossible at baseline, activates after Mandate erosion.
- Klapp Ob 2 (essentialist formation) buys Church ~1–2 seasons of structural integrity per failed check, not permanent preservation.
- Ceiral Ritual 7% failure is Costly Delay (retryable, RS −8 + 2-season delay), not endgame preclusion.
- Ehrenwall Medicine check (~47% failure) is the only True Preclusion roll — permanent, no retry, conditional on player choice.
- Mending Trap (ARC-S32) and Edeyja Burnout (ARC-S34) are resource-exhaustion arcs, not single-roll events.
- Failed Costly Delay rolls accelerate existing arcs; they do not create new branches.
- Lock Distribution at TK 4 (ARC-S31) is the highest-impact single player decision — 3–5 simultaneous Discovery Events.

**Files committed:**
- references/arc_register.md (v7, 808 lines)
- tests/threadwork_decision_point_analysis.md (204 lines)
- tests/arc_branch_simulation.md (303 lines)
- tests/delay_vs_preclusion_evaluation.md (189 lines)
- references/file_index.md (updated)
- session_log_current.md (this entry)

**Open items for next session:**
- ED-NEW-01: Tier assignments provisional — user review required
- ED-NEW-02: Revolution elder not canonised as named character
- ED-NEW-03: Elske TS development not established
- ED-NEW-04: 218 AG resolution reconciliation (accidental death vs E-01)
- GAP-ARC-01: Niflhel Quiet RS/Thread Tension cause
- GAP-ARC-02: IP generation formula (no canonical base rate)
- GAP-ARC-04: Baralta NPC personal stats conflicting between sources
- GAP-ARC-05: Excommunication gated mechanic (confirmed intentional)
- SIM-BRANCH-05: Edeyja burnout hidden fail state (ARC-S34)
- Lenneth zero mechanical expression (audit priority #1)
- Almud no BG expression (audit priority #2)
- Arcs S20, S21 NOT YET SIMULATED (CP14 arcs 34, 35)
- All NPC-ARC, ARC-S27–S34, ARC-T10–T19, Collisions A–G NOT YET SIMULATED

### 2026-04-11 — Simulation: Arcs 36-45 Batch (commit 7)

- tests/sim_arcs_36_45_batch.md: New file. Comprehensive simulation of Arcs 36-45.
  - Mode A isolation: Vaynard Spirit check (80-92% success), debate RS co-movement, mass battle probabilities.
  - Mode B interaction chains: tithe feedback loop, shield collapse timing, RS-radiation-Haelgrund loop, debate-RS-battle asymmetry, tithe self-reinforcement, Tutoring Demand trap.
  - Mode D edge cases: calamity radiation threshold error, Dissolution impossibility, P-01 debate compliance, Coup Counter inconsistency.
- **4 P1 findings:**
  - Arc 41 calamity radiation trigger off by 1 RS band (ED-420)
  - Arc 43 Dissolution mechanically impossible at T6 (ED-421)
  - Arc 44 Phase 1 timing requires 16-24 seasons not 9-10 (ED-422)
  - Coup Counter threshold inconsistency 3 vs 4 (ED-418)
- **7 P2 findings:** Parish Revolt dependency, Vaynard starting TS, Coherence burn narrative, debate RS frequency, convergence timeline, loop direction inversion, tithe loop non-termination.
- **8 mechanical gaps identified** (GAP-SIM-01 through GAP-SIM-08).
- canon/editorial_ledger.yaml: ED-418 through ED-425 added (8 items, 4 P1-BLOCKER).

## SESSION CLOSE

This session: 1 commit (simulation). 4 P1 findings requiring arc revision before the batch is playable.
Priority for next session:
1. Resolve ED-418 (Coup Counter threshold — quick fix, update params_factions to match params_board_game threshold 4)
2. Resolve ED-420 (Haelgrund territory — move to T5 Feldmark, revise Arc 41 narrative)
3. Resolve ED-421 (Replace Dissolution with Lock/Pull failures in Arc 43)
4. Resolve ED-422 (Establish CV erosion rates OR reframe Arc 44 as late-game)
5. Resolve ED-416 (RM hold T9 mechanic — still open from prior session)


---

## Session: 2026-04-11 — NPC Directory Consolidation

### Tasks completed
1. Consolidated `designs/npcs/` into canonical structure:
   - **`npc_roster.md`** (492 lines) — merged roster + caste annotations (§14 appended)
   - **`npc_character_analyses.md`** (333 lines) — Part One: roster NPCs + Part Two: ruler diamond & existing named NPCs
   - **`npc_foils.md`** (301 lines, new) — Part One: axis analysis + Part Two: subjective perspectives & extended foil network

2. Deprecated 8 files (deprecation banner added, content retained for audit trail):
   - `npc_roster_caste_annotations.md` → merged into roster §14
   - `npc_character_analyses_existing.md` → merged into analyses Part Two
   - `ruler_diamond_foil_analysis.md` → merged into foils Part One
   - `ruler_diamond_extended_foils.md` → merged into foils Part Two
   - `npc_comprehensive_audit.md` → superseded
   - `lenneth_threadwork_design.md` → content absorbed into roster + params_threadwork
   - `almud_correction_plan.md` → resolved, audit trail only
   - `ed_403_406_407_resolutions.md` → editorial resolutions absorbed

### Commit
- `deaf729ccf7a92948d1d0916956e79ca0bc2faa9`
- `[cleanup] Consolidate designs/npcs — roster, analyses, foils; 8 files deprecated`

### Post-commit checks
- `broken_dependency_checker.py`: 15 broken (pre-existing glob patterns — not introduced by this commit)
- `patch_propagation_checker.py`: 138 failures (pre-existing params propagation debt — not introduced)

### Open editorials carried forward
ED-370, ED-371, ED-372, ED-373 (as prior session)


## Session 2026-04-12 — Arc Audit Resolution

**Task:** Resolve audit findings from two-day arc collation + canon/NPC review.

**Completed:**
- ED-408 resolved: Prudence Cardinal named Aldric Tormann (npc_roster §13, arcs_36_40)
- ED-409 resolved: Torsvald Deniability Debt threshold = 3
- ED-410 resolved: Collection 1/season confirmed canonical (PP-168); no modification
- ED-411 resolved: Solberg recall → Schoenland Intel Ob 2 (PP-555 applied); IP threshold corrected 15→8
- ED-412 resolved: Convergence compression formula N + max(4, 8−N)
- Arc 40 partial convergence table added (4/4, 3/4, 2/4, 1/4 outcomes)
- Collision point 4 false positive documented (arc_narrative_analysis)
- Cross-Batch Collision Register added (arc_narrative_analysis)
- PP-556: Arc-specific Hybrid Zoom In trigger extension (zoom_in_out reference card)
- Ehrenwall Counter one-way ratchet documented as intentional (not a gap)
- Parish Revolt buildup: cross-referenced to existing roster Mandate erosion (no new mechanic)

**Proposals struck after full NPC/canon review:**
- Ehrenwall Counter decrement: STRUCK — contradicts documented characterisation ("The Ledger That Never Forgives"; never decrements is intentional design per npc_comprehensive_audit)
- Parish Revolt Stability −1 addition: STRUCK — creates destabilising stack on top of existing Mandate erosion; existing mechanism is sufficient
- Vaynard Intel escalation to TS growth: STRUCK — Intel already governs Collection roll (Intel vs Ob 2 per PP-168); TS growth is +1/use canonical; no additional modifier warranted

**Open items:** Vaynard full NPC roster entry (blocks Arc 39 simulation); TK track parameterization; Baralta roster entry; Zoom In arc-specific triggers to be added per-arc doc as work continues.


---

## Session: 2026-04-11 — Repository-Wide Consolidation (continued)

### Task: Consolidate all folders (except deprecated/) — mark deprecated

### Decisions made per folder

**tests/, references/, skills/, tools/, docs/, versions/**: No action — test archive, params system, skill SKILL.md structure, and utilities are all correctly structured. No consolidation applicable.

**gm_ref/**: No action — all arc files (arcs 01-04, 05-09, 10-18, 36-40, 41-45, narrative analysis) are current sequential batches. No overlaps.

**designs/setting/, designs/combat/, designs/contest/, designs/conviction_track/, designs/hybrid/, designs/mass_combat/, designs/mechanics/, designs/systems/**: Single-file folders or clean multi-file folders. No action.

### Commits

**Commit `8d08ef2`** — canon/ + compilation/v0.14/
- Deprecated 1 canon file: audit_threadwork_v24.md (superseded by v25)
- Deprecated 15 compilation/v0.14 stage files (superseded by design docs or params files)
- Kept: README, valoria_ruleset_v0.14.md, stage4_southernmost (only southernmost source), stage6_factions (only TTRPG factions source), stage11_scale_transitions (only source), stage12_campaign_modes (only source)

**Commit `a1168683`** — designs/board_game/ + designs/gm_ref_cp14/
- Deprecated 2 board_game files: faction_resolutions_2026_04_07.md, stress_test_report (absorbed; bg_v05 and victory_architecture are canonical)
- Kept: valoria_bg_v05_simulation_and_patches.md (canonical), victory_architecture_v1.md (canonical), valoria_map_v2.svg, varfell_path_b_redesign_ed311.md (open editorial ED-311)
- Deprecated 4 gm_ref_cp14/arcs (arcs 1-12, superseded by gm_ref/ arcs 1-18)
- Deprecated 10 gm_ref_cp14/dashboards (CP14 mechanics, outdated)
- Deprecated 3 gm_ref_cp14 other (workplan, zoom card, templar crossing flowchart)
- Kept: arcs 16-35 + experimental + campaign arcs (no gm_ref/ replacements exist)

**Commit `96c64d14`** — designs/ttrpg/ + designs/worldbuilding/ + designs/ root
- Deprecated 11 ttrpg/ files: all Phase 1 batch files (batch_a through batch_f, batch_ad_resolutions) + church_territorial_seizure, generation_tasks, lowenritter_faction_card, mechanical_tasks_and_patches, succession_mechanic
- Kept: threadwork_redesign_v25.md (canonical), edeyja_npc.md (canonical NPC), valoria_emergent_scenarios.md, valoria_narrative_scenario_chains.md (referenced by gm_ref arcs), threadwork_philosophical_reference.md (used by canon-guard skill)
- Updated SUPERSEDED.md to correctly document kept vs deprecated files
- Deprecated worldbuilding/editorial_comprehensive_review.md (absorbed into editorial ledger)
- Deprecated designs/cogload_reduction_strategies.md (superseded by cogload_moderate_target.md)

### Total deprecated this session extension: 48 files across 6 directories
### Post-commit checks: 15 broken (pre-existing glob patterns), 139 propagation failures (pre-existing) — no new issues introduced

### Open editorials carried forward
ED-311 (Varfell Path B — awaiting user review)
ED-370, ED-371, ED-372, ED-373 (carried from prior session)


---

## Session — 2026-04-13: Character Histories & Skill System Design

### Stage: Design — Character Creation / Skill Acquisition

### Summary
Designed and implemented the Character Histories lifepath system with SaGa-style skill sparking, 
Recall-as-skill-gatekeeper, and skill levels 1–3. Full Godot implementation committed to 
jordanelias/valoria-game.

### Key Decisions
1. **Lifepath structure:** 4-stage character creation (Origin → Formation → Vocation → Catalyst)
   - Origin: geography, culture, Certainty base, first Knot. 0 starting skills.
   - Formation: education/shaping, Certainty modifier, second Knot. 1 starting skill.
   - Vocation: profession, faction affiliation, third Knot. 2 starting skills.
   - Catalyst: inciting event, starting Belief, campaign hook. 0 starting skills.
   - Total starting skills: 3.

2. **Recall as gatekeeper (triple duty):**
   - Equip slots: max_equipped = Recall (1–7). Swap loadout between scenes.
   - Skill depth: Level 2 requires dice_bonus ≥ 3; Level 3 requires dice_bonus ≥ 5. Recall caps dice_bonus.
   - Learning speed: floor(Recall/2) bonus dice on spark checks.

3. **Coherence degrades equip slots:** Fragmented = −1 slot. Fractured/Severed = −2 slots. 
   Practitioners lose skill access — not just social/memory rolls — as Coherence drops.

4. **SaGa-style sparking:** Skills acquired through scene use, not menus.
   - Overwhelming at Ob 3+ → automatic spark
   - Success at Ob 3+ → Spirit + Recall/2, TN 7, Ob 1
   - Partial at Ob 2+ → Spirit + Recall/2, TN 7, Ob 2
   - Failure at Ob 3+ → Spirit + Recall/2, TN 8, Ob 1
   - Ob 1 → no check (routine)
   - Cross-History hybrid sparks for simultaneous use of 2+ Histories

5. **Skill levels 1–3:** Sparking prioritises level-ups over new skill acquisition.
   Level determines effect magnitude (per-level effect arrays in SkillData).

### Commits (jordanelias/valoria-game)
- `813f27b` — Initial History/Skill/Sparking system (10 files)
- `ab7c10a` — Recall as equip gatekeeper + skill levels 1–3 (9 files)

### Commits (jordanelias/ttrpg)
- Character Histories lifepath design doc: designs/characters/character_histories_lifepath.md

### New Editorial Items
- ED-374: Lifepath system requires user approval
- ED-375: Skill effects provisional — simulation required
- ED-377: Intuitive Threadwork + Co-Movement interaction open
- ED-378: Confirm 3 Knots is the right lifepath count
- ED-379: Can experienced characters have 2 Catalysts?
- ED-380: Southern Einhir Descendant +5 Thread Sensitivity at creation — Leap eligibility
- ED-381: Recall 1 = 1 equip slot — too punishing?
- ED-382: Coherence equip slot loss — player choice vs auto-drop?
- ED-383: Level 3 requiring Recall ≥ 5 — intentional specialist gate?

### Open editorials carried forward
ED-311 (Varfell Path B — awaiting user review)
ED-370, ED-371, ED-372, ED-373 (carried from prior session)

---

## Session: 2026-04-13 — NPC Behavior System Design

### Task
Design NPC ethical stances and resonance styles impacting AI decision trees, arc emergence, and behavior.

### Deliverables
1. **designs/systems/npc_behavior_system_v1.md** — Full design (860+ lines). Stance Triangles for 13 NPCs, BG Priority Trees for 9 factions, arc profiles, Resonant Style Contest integration, Framework Drift.
2. **tests/audit_npc_behavior_system.md** — 15 findings. All HIGH/MEDIUM resolved or flagged.

### New Editorial Items
ED-384 through ED-400 (17 items). P1-BLOCKER: ED-387.

### New Simulation Debt
SIM-NPC-01 through SIM-NPC-05.

### Open editorials carried forward
ED-311, ED-370–373, ED-374–383, ED-384–400.

### Consolidation commit — 2026-04-13
Merged character_histories_lifepath.md + character_histories_revision_pass.md into single canonical document.
- Starting skills: 5 (Origin 1, Formation 1, Vocation 2, Catalyst 1)
- Canon fix: 1D Forgetting misattribution corrected (Church suppression, not Forgetting)
- Generic entries rebuilt: 1F (Tideward/Ashmarket modifiers), 1H (Occupation Displaced / Calamity Orphan / Church Ward)
- 2D rebuilt as Empiricist; 2E Weapons Training changed from TN−1 to +1D Offence
- 5 new Vocations: Crown Farmer, Diplomat, Independent Criminal, Church Investigator, Löwenritter Patrol Officer (threadcut veteran)
- Catalysts specified: 4D faction-specific, 4F three specific Valorian conflicts, 4G GM-determines direction
- Thread-adjacent spark skills added to 4 non-practitioner Vocations
- Knot audit: 8 weak Knots rewritten for dramatic specificity
- Skill level principle: L1 base, L2 quantitative, L3 qualitative unlock (7 example skills mapped)
- 4E Leap Scar changed from −1 Ob to +1D (avoids OB_FLOOR interaction)
- Literacy model formalised by Formation
- Revision pass doc deleted (absorbed)


---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DEBATE_STRESS_TEST
phase: Phase 9 — Debate stress test (SIM-DEBT-01)
status: COMPLETE

completed:
  - SIM-D-01: Debate stress test Modes A+D+J+L. New calibration baselines established.
  - PP-097/098/099 PROVISIONAL: applied in-place to debate_system_redesign_v1.md.
  - SIM-D-02: Debate Mode C scenario — Himlensendt vs Baralta, Parliament.
  - PP-100 PROVISIONAL: §6.7 proposer/initiative decoupling clarified in-place.
  - ED-051 (P1): stage13 NPC debate stat block missing — Attunement, Focus, Poise, Bonds.
  - ED-052 (P2): NPC Composure formula mismatch — shorthand vs Poise+Bonds+3.
  - SIM-DEBT-01: RESOLVED.
  - debate_system_redesign_v1.md: v1.2

key_findings:
  - 3-exchange Formal Debate → Compromise ~95% at resistance 2 (structural design, not a flaw)
  - Resistance level is the dominant variable for track movement in short debates
  - Genre weight dominates pool-size adjustments up to ~+2D Memory bonus
  - DIVERGE produces 0 strain — Composure drain only in CLASH/COMPETITION
  - F-C-04 P1: NPC debate attributes missing — blocks authoritative NPC debate sims
  - F-C-06 P1: Novice debate time 9 min/exchange — GM reference card needed

next_action:
  task: "GM reference card for debate (one-page: §6.1 setup + §6.4 exchange flowchart + genre weight table). Addresses F-C-06 P1."
  note: "Or pivot to next simulation priority. Confirm with user."

commits_this_session:
  - 22a1f24: SIM-D-01 + PP-097/098/099 + params_debate + coverage_matrix
  - 1641078a: debate v1.1 in-place patches + propagation_map + session_log
  - [this]: SIM-D-02 + PP-100 + ED-051/052 + debate v1.2 + coverage_matrix + propmap + session_log
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SKELETON_CLEAN_2
phase: Phase 10 — bg_v05 → v0.6, threadwork → v2.6, skeleton-debt cleared
status: CLOSED

completed:
  - bg_v05 → v0.6: ST-BG-03/04/06/07/08/09 and ST-INT-01/05/06/09/10 applied in-place. PART THIRTEEN appendix eliminated. 981 → 1000 lines (net minimal growth because patches are now context notes, not appendix sections).
  - threadwork_v25 → v2.6: ST-TW-01–05 and R-54–R-68 applied in-place. Parts 10+11 appendix eliminated. 1059 → 1108 lines.
  - skeleton-debt register updated in file_index.md.
  - In-place patching rule now enforced in simulator Mode I and orchestrator.

skeleton_debt_remaining:
  - threadwork v2.6 → v3.0: Part 1 philosophical framing should move to a reference doc (separate from the mechanical spec). Low priority — Part 1 is useful reference for canon-guard.
  - compilation/v0.14/stage8_combat.md: Part Eleven appendix. Low priority — compilation layer.
  - compilation/v0.14/stage11_scale_transitions.md: PP-089/090 appended. Low priority.

next_action:
  task: "Begin simulation. stress test debate — SIM-DEBT-01 (Presence×2 pool recalibration)."
  note: "All high-priority skeleton-debt cleared. Design documents now internally consistent. Pipeline verified."
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DEBATE_STRESS_TEST
phase: Phase 9 — Debate stress test (SIM-DEBT-01)
status: IN PROGRESS

completed:
  - SIM-D-01: Debate stress test Modes A+D+J+L. Calibration baselines recalibrated.
  - PP-097 PROVISIONAL: DIVERGE+TIE → Tie rule fires (any interaction type). Applied in-place to debate_system_redesign_v1.md §6.4 DIVERGE block.
  - PP-098 PROVISIONAL: Regroup at Concentration=0 → consumes Spent without penalty. Applied in-place §6.4 Step 5.
  - PP-099 PROVISIONAL: Obscuring in Divergence → Doubt Marker; orientation_weight=1.0. Applied in-place §6.4 DIVERGE block.
  - debate_system_redesign_v1.md bumped to v1.1.
  - propagation_map.md updated with DEBATE section.
  - SIM-DEBT-01 PARTIALLY RESOLVED: Mode C scenario run still needed.

key_findings:
  - P(Overwhelming) doubled: ~25% old → ~60% new (symmetric 8D pools)
  - Exchanges to Rattled halved: 7-9 old → 3-5 new (Composure 9)
  - Track movement now consistent 1 step/exchange vs 0 often under old pool
  - F-D-01 P1 (PP-097): DIVERGE+TIE ambiguity — Tie rule takes priority
  - F-D-06 P2: Grand Debate + Corroboration ~90 resolution steps, no GM reference card

next_action:
  task: "Mode C debate scenario — Baralta vs Himlensendt, 3-exchange Formal Debate. Completes SIM-DEBT-01."
  note: "Read stage13_npcs.md for Baralta and Himlensendt stats before running. New pool: (Presence×2)+History."

commits_this_session:
  - 22a1f24: SIM-D-01 test file + patch_register PP-097/098/099 + params_debate recalibration + coverage_matrix
  - [this commit]: debate_system_redesign_v1.md v1.1 in-place patches + propagation_map + session_log
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SKELETON_CONTAINERS_FINAL
phase: Phase 8 — Skeleton rulesets, container pattern, broken dependency checker
status: CLOSED

completed:
  - tools/broken_dependency_checker.py: executable scanner for broken refs across propagation_map, canonical_sources, skill_registry, editorial_ledger. Exits 1 if broken. propagation_map Step C now references it.
  - Container pattern applied to params files: clean values file + separate history file. params_combat 113→80 lines, params_debate 141→88, params_mass_combat 203→136, params_threadwork 269→246, params_board_game 250→194. Each has container refs to patch_history and canonical_sources.
  - Skeleton ruleset principle and container pattern documented in project_instructions.md.
  - Project instructions: PAT/GraphQL bootstrap section at top of document.
  - Skeleton-debt flagged: debate Parts 1-4 (historical/philosophical), threadwork Part 1.

next_action:
  task: "Begin simulation. Priority: stress test debate (SIM-DEBT-01)."
  note: "All infrastructure complete. Pipeline verified. Project instructions ready."

commits_this_session:
  - bf2917b: canonical_sources + P-15 + project instructions
  - a256278: broken_dependency_checker + container pattern + skeleton docs
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_FINAL_REVIEW
phase: Phase 7 — Canon, clarity, canonical sources, project instructions
status: CLOSED

## SESSION SUMMARY

### Canon-guard analysis
- Amendment 01 (self-rendering) introduces three-layer being-persistence; Leap redefined; Coherence 0 TS-gated branching
- These were NOT in P-01-P-14. P-15 added to canon/02_canon_constraints.md
- Canon-guard updated with amendment integration workflow (auto-runs when any canon file changes)
- Canon-guard now reads canonical_sources.yaml to determine which document to validate

### Version authority
- references/canonical_sources.yaml created — maps every system to canonical source
- Rule: compilation_current:false = use design doc; compilation_current:true = compilation is correct
- Key reversals: combat and mass_combat now point to designs/ not compilation stage8
- simulator Read Protocol updated to check canonical_sources.yaml first (Step 0)

### Params fixes
- params_combat: source corrected to designs/combat/combat_design_v1.md
- params_mass_combat: source corrected (combat_design_v1 + mass_battle_v3)
- params_scale_transitions: version tag updated (stage11 updated April 2)

### Token efficiency
- The params abstraction IS working correctly. Skills read params (compact) not design docs (verbose).
- Simulator trimmed from 441 to 432 lines (duplicate version check removed).
- Efficiency note added to project instructions.

### Project instructions
- project_instructions.md rewritten. Key changes:
  - Removed "check Project Files first" (Project Files deprecated)
  - Added canonical_sources.yaml reference
  - Added simulation command vocabulary table
  - Added audit criteria coverage statement
  - Updated model routing table
  - Added compilation rules (lowest priority, when to compile)
  - Added open blockers summary

### Pipeline status
- 5/5 questions: YES (with honest note on broken-dependency detection)
- 12/12 checks passing
- All critical issues from review resolved

### Remaining honest limitations
- Propagation map broken-dependency detection: described but not executable code
- SIM-DEBT-01: debate calibration needs re-simulation with Presence×2 pool
- ED-048: Ceiral non-canon name in 22 files — awaiting canonical name from user

### next_action:
  task: "Run simulations. Priority: (1) stress test debate (SIM-DEBT-01), (2) stress test combat, (3) simulate hybrid scenario."
  note: "Pipeline verified and documented. Project instructions ready. Begin simulation work next session."

### commits_this_session:
  - a96161: simulation infra modes J/K/L/M (prior)
  - e4a276e: pipeline clarity fixes (prior)
  - 74836d8, 1a6ea6a: version check fixes (prior)
  - bf2917b: canonical_sources + P-15 + project_instructions (this close)
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_PIPELINE_VERIFIED
phase: Phase 6 — Pipeline review, clarity fixes, viability confirmed
status: CLOSED

## SESSION SUMMARY

### Pipeline review findings (4 blocking, 5 warnings, 1 note)

Blocking — all fixed:
- [1] Simulator Mode I: duplicate Step 7 → renumbered to Step 8
- [2] Skill registry: described non-existent Tier1/2/2.5 simulation skills — rewritten to reflect actual GitHub skills with simulation command routing table
- [3] State transfer spec: section 5 heading still said UNRESOLVED after ED-050 resolution — fixed
- [4] Simulator Mode G2: used old Rhetoric pool terminology — updated to (Presence×2)+History, Conviction Track, genre/orientation framing

Warnings — all fixed:
- [W1] Simulator version check referenced compilation/README.md — replaced with params version tag check
- [W2] Canon-guard path: canon/canon_constraints.md → canon/02_canon_constraints.md
- [W3] Compiler: old gap register reference → canon/editorial_ledger.yaml; output path fixed; designs-first note added
- [W4] Mechanic-audit Mode G: incomplete path to state_transfer_spec → full path added
- [W5] Session protocol: stale filename valoria_session_log.md → session_log_current.md

Note — communicated:
- Propagation map broken-dependency detection is described but not executable code; honest limitation

### Pipeline viability: CONFIRMED
12/12 checks passing after fixes.

### Commits this session:
- e4a276e: all pipeline fixes (skill_registry, simulator, audit, canon-guard, compiler, editorial-register, session_protocol, state_transfer_spec, propagation_map)
- 74836d8: first pass compilation/README fix
- 1a6ea6a: complete compilation/README removal

### next_action:
  task: "Run first simulation. Recommend: stress test debate (SIM-DEBT-01 — re-calibrate Presence×2 pool). Use simulator Mode G2 + Mode J (cognitive load) + Mode L (precedent)."
  note: "Pipeline is verified and ready. Every criteria dimension covered. All blocking issues resolved. Propagation is automatic."
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SIMREADY_FINAL
phase: Phase 5 — Simulation infrastructure complete and self-maintaining
status: CLOSED

## SESSION SUMMARY

### Completed
- ED-050 resolved: 7-phase mass battle. Offensive Thread = Phase 4 (between Manoeuvre and Engagement). Support Thread = Phase 6 Cascade step 4-5. All damage (Volley + Thread + Engagement) applied simultaneously at Phase 6 Step 1. BG has no battle-phase Thread. Propagated to mass_battle_v3, stage11, state_transfer_spec, params_mass_combat.
- Propagation map v2: self-maintaining with embedded AUTO-UPDATE PROTOCOL. Dependency rules by file type. Params-skill dependency map. New files and cross-references now detected and registered automatically at commit time via Step 6 of simulator Mode I. Never manually maintained again.
- Simulator Mode I updated: Step 6 = propagation map update before commit (mandatory). Step 7 = atomic commit (includes propagation_map). Step 8 = report.
- Orchestrator updated: propagation is automatic, not manual.

### Five questions answered
1. Simulations/tests/audits for all game modes/systems/mechanics: YES
2. Mechanical patches applied and flagged in patch registry: YES (Mode I enforced)
3. Editorial decisions identified, checked against ledger, added if missing: YES
4. Comprehensive results recorded against all criteria: YES (Modes A-M)
5. Changes propagated across all relevant documents: YES (self-maintaining propagation map)

### next_action:
  task: "Run simulations. Recommend starting with: stress test debate (SIM-DEBT-01 re-calibration with Presence×2 pool), then simulate a hybrid scenario for full cross-mode test."
  note: "Every sim run now commits findings immediately. Propagation map updates automatically. All five infrastructure questions are answered."

### commits_this_session:
  - 5b67b79: ED-050 resolved — 7-phase mass battle
  - 3349725: propagation map v2 + simulator Mode I + orchestrator update
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SIMINFRA_COMPLETE
phase: Phase 4 — Simulation infrastructure complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Simulator Modes J/K/L/M added:
    J: Cognitive load + time audit (decision count, lookup count, parallel tracks, novice/experienced/expert minutes)
    K: Cross-mode delta (K1: TTRPG/Hybrid/BG property table; K2: transition stress test against state_transfer_spec)
    L: Precedent comparison (8-game library, flag unjustified complexity)
    M: Narrative flowchart generator (branching nodes with state tracking, min 3 branches per node, 3 nodes deep, terminal state labels, GAP/DEAD-BRANCH flags, cross-mode mapping)
- mechanic-audit Mode G added: cross-mode consistency audit + transition point checks
- state_transfer_spec.md created: all variables at every mode boundary (TTRPG↔Hybrid, BG↔Hybrid, within-TTRPG Register Shifts), interruption protocols, invariants
- stage11 TT Multiplier column patched (T5-P1-01): obsolete column removed, reference to threadwork added
- ED-050 added: Thread→Mass timing conflict (T1-P1-01) — choose A/B/C
- Flowchart output directory: designs/gm_ref_cp14/flowcharts/

### Simulation command vocabulary (confirmed)
- "stress test [specific mechanic]" → Mode A + D + J + L (isolation, edge cases, cognitive load, precedent)
- "stress test [subsystem]" → Mode G-submode + D + J + K + L (full subsystem, cross-mode delta, load, precedent)
- "stress test [mode]" → all G-submodes for that mode — multi-session, orchestrator stages it
- "simulate [scenario]" → Mode C + M (full scenario + branching flowchart)
- "simulate [ttrpg/hybrid/boardgame]" → Mode C + G-suite + M — multi-session
- "audit [subsystem]" → mechanic-audit Modes A-G

### Full audit criteria coverage
- Crunch cascade ✓, Edge cases ✓, Regressions ✓, Failures ✓, Ambiguities ✓
- Overlap/repetition ✓, Incoherence ✓, Philosophy compliance ✓
- Meaningful actions ✓ (Mode C scenario output), Emergent gameplay ✓ (Mode M flowchart)
- Cognitive load ✓ (Mode J — NEW), Time consumed ✓ (Mode J — NEW)
- Precedent comparison ✓ (Mode L — NEW)
- Cross-mode interdependency ✓ (Mode K1 — NEW), Transition/zoom ✓ (Mode K2 — NEW)
- Narrative flowchart with branching ✓ (Mode M — NEW)

### Remaining editorial before full simulation clearance
- ED-050: Thread→Mass timing (P1) — blocks K2 transition test for mass battle Thread
- ED-001: Card-Hand system (P1-BLOCKER) — blocks BG compilation only
- 38 other open items (non-blocking for simulation)

### commits_this_session:
  - 2e4bf45: ED-047 debate pool resolved
  - 5719802: provisional decisions + sim infra
  - 6124d9f: session close phase 3
  - 3728b3a: Modes J/K/L/M + state_transfer_spec + Mode G + stage11 patch
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_BLOCKERS_SIMPREP
phase: Phase 3 — Blocker resolution, simulation infrastructure repair
status: CLOSED

## SESSION SUMMARY

### Completed
- ED-047 resolved: debate pool = (Presence × 2) + History. R-65 applied. SIM-DEBT-01 registered.
- ED-031 provisional: BG Overwhelming = Ob+1 (intentional divergence from TTRPG 2×Ob)
- ED-037 provisional: Volley TN 6 confirmed as intentional exception to universal TN 7
- ED-038 resolved: Coherence in mass battle = personal track (10→0, threadwork Part 3)
- ED-036 provisional: Altonian unit stats placeholder (Vanguard/Elite Guard/Thread Corps)
- Coverage matrix: F-11 resolved (ST-TW-02); F-27/F-30-33/F-43/F-52 provisioned; F-45 → ED-049
- PP-093-096 applied (provisional): stalemate, coup successor, TC cap, Stability recovery
- Simulator skill Mode I: enforced atomic commit protocol; path fix (sim_coverage_matrix→tests/coverage_matrix); SIM-DEBT section added; provisional decision protocol added
- Editorial register skill: provisional status added
- params_mass_combat: Altonian stats, ED-037/038 decisions applied
- params_board_game: ED-031 BG Overwhelming rule added
- ED-049 added: Church Stability brake scope (F-45, P2)
- Ledger: 49 items total — 40 open, 3 provisional, 2 resolved, 4 struck

### Simulation readiness
- Combat: READY
- Threadwork: READY
- Mass combat: READY (ED-037/038 resolved provisionally; Altonian stats provisional)
- Board game faction play: READY (ED-031 provisional; ED-001 Card-Hand still open but non-blocking for most tests)
- Debate: DEGRADED (SIM-DEBT-01 — pool change needs re-calibration; can simulate, results directional)
- Full hybrid campaign: READY for most scenarios (Altonian engagement provisional)

### next_action:
  task: "Simulate. Use Mode G suite (G1 mass combat, G2 debate, G3 threadwork, G4 faction play, G5 BG)."
  note: "Simulator Mode I is now enforced — every sim run commits findings immediately. Provisional decisions are marked in-text. SIM-DEBT-01 requires debate re-simulation with Presence×2 pool."
  remaining_editorials_blocking_simulation: [ED-001 (Card-Hand BG compilation only)]

### commits_this_session:
  - 2e4bf45: ED-047 resolved, R-65 applied, SIM-DEBT-01 registered
  - 5719802: provisional decisions + sim infrastructure repair
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DESIGN_CLEANUP
phase: Phase 2 — Design cleanup, three-mode framing, infrastructure
status: CLOSED

## SESSION SUMMARY

### Completed
- Catastrophic Failure / majority-1s override struck from BG system entirely
- Debate: quaestio deprecated; §6.0 context-sensitivity principle added; proceeding-type table expanded (private negotiation vs parliamentary vs tribunal); Parts 1-4 = reference only
- Debate: §6.10 added flagging R-66 vs stress-test pool conflict (ED-047, P1-BLOCKER)
- Threadwork: "Einhir ritual framework" → "Einhir framework" (ritual not canon)
- Threadwork: R-54–R-68 patches applied (Pull duration, Dissolution Ob, healing overweave, Pull floor, Lock drain cap, Mode 3 immunity, Fortification Pulling, institution RS drift)
- designs/combat/combat_design_v1.md created — TTRPG-baseline working document with three-mode framing; replaces stage8 as design-layer source; PP-086–092 + MT-01 faction unit rosters incorporated
- ED-047 (debate pool conflict blocker) + ED-048 (Ceiral non-canon — 22 files affected) added to editorial ledger
- Orchestrator: designs-first philosophy, three-mode framing, stale sweep at session start, compilation = lowest priority
- file_index: combat design added; propagation-pending section added (batch_ad_resolutions, succession, hybrid_gaps_resolved, generation_tasks); three-mode framing header
- designs/ audit completed: all files catalogued; batch_ad_resolutions.md has 11 approved decisions not yet propagated; generation_tasks flagged for user review; hybrid_gaps_resolved ready for integration

### GitHub state (committed)
- 7a3c2ce: all above changes (single atomic commit)

### next_action:
  task: "Resolve P1-BLOCKERs in priority order"
  priority_queue:
    - ED-047 (debate pool formula — P1-BLOCKER, blocks all debate simulation)
    - ED-048 (Ceiral canonical name — P1, blocks NPC/arc work)
    - ED-036 (Altonian unit stats — P1-BLOCKER, blocks hybrid Altonian engagement)
    - ED-038 (Coherence stat definition — P1, blocks mass_battle §A.10)
    - ED-001 (Card-Hand system — P1-BLOCKER, blocks BG compilation)
  note: "Use valoria-editorial-register Workflow A. After blockers: propagate batch_ad_resolutions.md decisions (G-038 treaty betrayal needs a home file), integrate hybrid_gaps_resolved.md into stage11."

### editorial_decisions_pending: 44 open (ED-001–046 minus struck; plus ED-047–048)
### blockers: ED-047, ED-036, ED-001

### commits_this_session:
  - d0ffda0: session close (prior)
  - 03e462b through ac99de5: infra (prior)
  - 7a3c2ce: design cleanup + three-mode framing
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_PATCH_INFRA
phase: Phase 1 — Stress Test Patches + Infrastructure
status: CLOSED

## SESSION SUMMARY

### Completed
- BG stress test patches (ST-BG-01–10, ST-INT-01–13) applied to bg_v05_simulation_and_patches.md
- Mass battle stress test patches (ST-MB-01–10) applied to mass_battle_v3.md
- Debate stress tests v1+v2 (D-01–v2-P04) compiled into debate_system_redesign_v1.md Part 6
- Threadwork mode index added + ST-TW-01–05 patches applied to threadwork_redesign_v25.md
- stage8_combat.md: PP-086–092 applied (P1-B11 + P2-B11 series)
- stage11_scale_transitions.md: PP-089 (hybrid phase order) + PP-090 (mid-siege conversion) applied
- patch_register.yaml: gap filled PP-086–092; PP-089/090 marked applied
- github_ops.py: GraphQL batch reader added (read_files_graphql)
- references/file_index.md: new repository index (all files, systems, status, dependencies)
- references/propagation_map.md: new cross-reference tracking system
- skills/valoria-editorial-register/SKILL.md: updated with dedup/consolidate/stale logic + Workflow E
- editorial_ledger.yaml: ED-031–046 harvested; ED-008,011,013,018 struck. 46 items total, 42 open, 4 struck.
- All 5 stale params files synced (params_combat, mass_combat, board_game, debate, threadwork)

### GitHub state (all committed)
- 8d8fd91: debate/bg/mass_battle/threadwork ST patches + github_ops GraphQL batch reader
- 133052e: stage8_combat PP-086–092 + patch_register gap filled
- 03e462b: file_index + propagation_map + editorial-register skill update
- e619c33: editorial_ledger ED-031–046 + consolidations/strikes
- 3775932: all 5 params synced + file_index stale section updated
- ac99de5: stage11 PP-089+PP-090 + patch_register applied status

### next_action:
  skill: valoria-editorial-register
  task: "Workflow A — resolve P1-BLOCKERs: ED-036 (Altonian unit stats), ED-038 (Coherence definition), ED-001 (Card-Hand system)"
  parameters:
    priority_queue: [ED-036, ED-038, ED-001, ED-031, ED-037, ED-044, ED-033]

### open_gaps_added:
  - "Params stale: stage3_thread_operations.md needs rewrite from threadwork_v25"
  - "Params stale: stage9_social.md needs rewrite from debate_system_redesign_v1.md Part 6"
  - "PP-089/090 applied to stage11; params_scale_transitions.md not yet re-synced"

### editorial_decisions_pending: 42 open items (ED-031–046 new; prior carry-forward)
  - P1-BLOCKERs: ED-036 (Altonian unit stats), ED-001 (Card-Hand system)
  - P1: ED-031,032,033,037,038,044

### blockers:
  - ED-036 (Altonian unit stats) blocks hybrid Altonian engagement at IP>=75
  - ED-001 (Card-Hand system) blocks BG stage_bg compilation
  - ED-038 (Coherence stat) blocks mass_battle_v3 §A.10

### commits_this_session:
  - 8d8fd91 through ac99de5 (6 commits)
```

---

# Valoria Session Log — Updated

```yaml
session_close: 2026-04-01
checkpoint: hybrid_sim_arcs_31_35
completed_stages:
  - valoria-editorial-register skill created and committed (skills/valoria-editorial-register/SKILL.md)
  - editorial_ledger.yaml populated: 21 harvested items (ED-001–021) + 9 new (ED-022–030) = 30 total
  - Arcs 31–35 generated (designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md)
  - Simulation Mode C+G for Arcs 31+33 (tests/simulation_report_arcs_31_33.md)
  - Patches PP-159–163 added to patch_register.yaml
next_action:
  skill: valoria-editorial-register
  task: "Resolve editorial decisions — start with P1-BLOCKERs: ED-027 (Poise attribute), ED-030 (Thread combat vs Mode 3), then ED-001 (BG-E-30 Card-Hand system)"
  parameters:
    priority_queue: [ED-027, ED-030, ED-001, ED-008, ED-011, ED-012, ED-013, ED-016, ED-018, ED-020]
    consolidate_first: [[ED-011, ED-027], [ED-005, ED-021], [ED-009, ED-010]]
open_gaps_added:
  - "GAP-ARC31-SIM-01: Focus/NPC attributes missing from stage13_npcs — all NPC profiles need Focus + Attunement values"
  - "GAP-ARC31-02: Grand Debate quaestio Ob per phase not specified (currently assumes Ob 1)"
  - "GAP-ARC33-SIM-02: Southernmost entity stat blocks (Mode 3) not in compilation"
  - "GAP-ARC34-01: Vaynard TK5 independent action clause missing from TK track"
  - "GAP-ARC35-01: Klapp CE track trigger criteria need formalisation (which objects qualify)"
editorial_decisions_pending:
  - "ED-027: Poise attribute → Focus mapping (P1-BLOCKER — blocks debate compilation)"
  - "ED-030: Thread combat vs Mode 3 entities — pool split or separate roll (P1-BLOCKER)"
  - "ED-001: Card-Hand system adoption (BG-E-30, P1-BLOCKER — carries from prior session)"
  - "ED-008: Niflhel formal Debate access"
  - "ED-011: Concentration attribute (Focus vs Poise)"
  - "ED-012: Audience Disposition win-condition scope (all Formal vs Grand only)"
  - "ED-013: Grand Debate role alternation — who gets extra proposition"
  - "ED-016: Military stat → unit quality mapping confirmation"
  - "ED-018: Commander bonus formula confirmation"
  - "ED-020: Pulling general command capacity — intended tactical option?"
  - "ED-022: Forced Unmask vs Register Shift from external disruption"
  - "ED-023: Vaynard TK5 operational capability vs knowledge-brokerage"
  - "ED-024: Southernmost Mode 3 entity stat blocks needed"
  - "ED-025: Almud Torben yield — scene vs automatic"
  - "ED-026: Klapp Trajectory determination + Discovery Event intervention"
  - "ED-028: Forgetting dissolution — dramatic vs silent"
  - "ED-029: Purpose tracking in Southernmost"
blockers:
  - "ED-027 (Poise attribute) blocks debate system compilation"
  - "ED-030 (Thread vs Mode 3 combat) blocks Southernmost encounter simulation"
  - "ED-001 (Card-Hand system) blocks all BG Tier 1 work — carries from prior session"
simulation_coverage:
  - "SIM-ARC31-C01: Arc 31, Modes C+G1+G2+G4 — 7 findings, 4 patches"
  - "SIM-ARC33-C01: Arc 33, Modes C+G3 — 4 findings, 1 patch"
  - "Remaining: Arcs 32, 34, 35 not yet simulated — next session priority after editorial pass"
commits_this_session:
  - "507ce0c7: skills/valoria-editorial-register/SKILL.md (new skill)"
  - "d690b177: canon/editorial_ledger.yaml (initial population, 21 items)"
  - "eb0edf0d: designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md (arcs 31-35)"
  - "466d6391: tests/simulation_report_arcs_31_33.md (simulation report)"
  - "0497c387: canon/patch_register.yaml (PP-159–163)"
  - "1d96469a: canon/editorial_ledger.yaml (ED-022–030)"
```

---

# Valoria Session Log — Archive

> Historical record. Do NOT read on session start. Read session_log_current.md instead.

# Valoria Session Log
## Initialized: 2026-03-25

---

```yaml
session_close: 2026-03-24
checkpoint: pre-CP14 (infrastructure)
completed_stages:
  - "Philosophical Foundations document (canonical)"
  - "Initial ruleset audit (2 documents vs Foundations)"
  - "6-attribute proposed ruleset with co-movement, Taint reframe, gate wounds"
  - "Faction leader profiles (Baralta, Vaynard, Almud, Lenneth)"
  - "Theocracy Clock, Inquisitor/Riskbreaker mechanics, Church heresy investigation"
  - "Monte Carlo stress tests → 28 patches applied to CP10"
  - "Skill ecosystem (6 skills, 7 reference files)"
  - "CP14 compilation workplan (18 stages, 7 batches)"
  - "Pre-CP14 audit value assessment (19 delta items)"
  - "Game system analysis (33 systems, tiered recommendations)"
  - "Three-dimensional co-movement redesign (Version C selected)"
  - "Skeleton stress tests R1-R3 (30 scenarios, 40 rulings)"
  - "Archetype substitution analysis (30 scenarios × 6+ archetypes)"
next_action:
  skill: orchestrator
  task: "Phase 1 design work"
```

---

```yaml
session_close: 2026-03-25
checkpoint: comprehensive workplan (replaces CP14 workplan)
completed_stages:
  - "Systematic review of all work (2-day audit)"
  - "Gap register reconciliation (17 → 40 items)"
  - "Patch log population (83 tracked changes)"
  - "Canon constraints updated for Version C"
  - "Workplan revision memo"
  - "Session log initialized"
  - "4 blocking editorial decisions resolved (G-003, G-004, G-010, G-017)"
  - "Design intent established: ethical frameworks, endgame, political axes, mode-specific branching"
  - "Circles/Resources editorial: tied to Histories + factions, degradable"
  - "Board game foundational review: identified all missing systems"
  - "Gap register expanded (40 → 82 items, 38 need design from scratch)"
  - "Comprehensive workplan produced (5 phases, 24-40 sessions estimated)"
next_action:
  skill: valoria-orchestrator (update needed)
  task: "Phase 1 Batch A — TTRPG core gap design"
  input: valoria_comprehensive_workplan.md
gaps_resolved:
  - "G-003 (round duration)"
  - "G-004 (pool split)"
  - "G-010 (10 attributes)"
  - "G-017 (action economy)"
gaps_opened:
  - "G-025 through G-065 (40 new gaps from systematic review)"
editorial_pending:
  - "G-027: board game player count"
  - "G-024: Lenneth TS path"
  - "G-012: Virtues/Vices merge"
  - "Batch D: all faction ethical framework mappings"
blockers:
  - "Phase 1E blocked on Phase 1D"
  - "Phase 2 blocked on Phase 1"
```

---

```yaml
session_close: 2026-03-25T02
checkpoint: S3 (gap register consolidated, editorial decisions)
completed_stages:
  - "Gap register consolidated (82 → 108 items)"
  - "22 new hybrid gaps (G-074–G-095)"
  - "5 consolidation candidates pre-resolved (Push cut, Maxims cut, etc.)"
  - "Reach system editorial (Short/Long/Projectile)"
  - "Zone-based combat editorial (TTRPG zones, board game territory-adjacency)"
  - "Board game player count resolved (2-5 + solo)"
  - "Lenneth TS path resolved (scholarly research)"
  - "Virtues & Vices cut"
  - "Hybrid architecture resolved (phase-separated, GM scenario engine)"
  - "Intelligibility system editorial (Taint → 10→0 countdown)"
  - "Faction ethical frameworks assigned (all 7 + sub-groups)"
  - "Fibonacci group bonus confirmed"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch A design — begin comprehensive workplan execution"
  input: valoria_gap_register_consolidated.md + valoria_comprehensive_workplan.md
```

---

```yaml
session_close: 2026-03-25T03
phase: 1
batch: A+B+C+D
completed_stages:
  - "Batch A designed (7 gaps: G-053, G-040, G-054, G-048, G-034, G-047, G-052)"
  - "Batch A editorial resolved: Approach Training 8CP, half-CP refund on Grief failure, single Circles track"
  - "Batch B designed (6 gaps: G-033, G-035, G-036, G-046, G-056, G-045)"
  - "Batch C designed (8 gaps: G-041, G-042, G-043, G-038, G-039, G-037, G-044, G-055)"
  - "Batch C editorial resolved: faction creation = narrative prereqs only, Altonian vassalage valid"
  - "Treaty betrayal mechanic designed: betrayed gets Stability -1 (2 seasons) + casus belli + Grievance Marker; betrayer gets Influence -1 (2 seasons) + Mandate +1 (1 season) + individual Reputation damage"
  - "Batch D designed (4 gaps: G-019, G-020, G-032, G-022 — integrated faction identity packages for all 7 factions)"
  - "Batch D editorial resolved: Private Collection transfers as institutional asset (shocking); Niflhel permanently decentralized"
  - "Nine political axes designed as GM narrative tool (not tracked numerically)"
gaps_resolved_this_session:
  - "G-053 (CP spending menu)"
  - "G-040 (Inspiration acquisition/recovery)"
  - "G-054 (Circles/Resources redesign)"
  - "G-048 (Resources degradation — subsumed into G-054)"
  - "G-034 (Fortification/base building)"
  - "G-047 (Siege mechanic)"
  - "G-052 (Player/GM transition guide)"
  - "G-033 (Army levy/mustering)"
  - "G-035 (Officer recruitment/caps/maintenance)"
  - "G-036 (Defection/cross-faction recruitment)"
  - "G-046 (Unit composition/formation)"
  - "G-056 (Supply lines/logistics)"
  - "G-045 (Knights Templar organization)"
  - "G-041 (Non-leader faction membership)"
  - "G-042 (Faction creation by players)"
  - "G-043 (NPC faction elevation)"
  - "G-038 (Alliance/treaty/betrayal)"
  - "G-039 (Casus belli/war justification)"
  - "G-037 (Territory governance after conquest)"
  - "G-044 (Altonian presence pre-invasion)"
  - "G-055 (Southernmost expedition)"
  - "G-019 (Ethical framework expression — integrated into faction cards)"
  - "G-020 (Leader vs institution — integrated into faction cards)"
  - "G-032 (Asymmetric faction powers — Unique Actions)"
  - "G-022 (Nine political axes)"
gaps_opened:
  - "Löwenritter faction identity (not currently a faction — needs package or sub-faction status)"
  - "Axis 10: Succession (Almud → compromised heir — nature of compromise TBD)"
  - "Named Revolution elder NPC (optional, flagged)"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch E — Board game design (14 gaps). Requires Löwenritter and Succession editorial first."
  input: batch_d_designs.md (faction identity packages as foundation for board game faction cards)
editorial_pending:
  - "Löwenritter: full faction, Crown sub-faction, or officer pool?"
  - "Succession axis: nature of heir's compromise (Niflhel? Thread-sensitive? Church-captured? Other?)"
  - "Named Revolution elder NPC (optional)"
blockers:
  - "Batch E (board game) ready to start — depends on Löwenritter decision"
  - "Batch F (hybrid+endgame) blocked on Batch E"
  - "Phase 2 (compilation) blocked on Phase 1"
output_files:
  - "batch_a_designs.md"
  - "batch_bc_designs.md"
  - "batch_d_designs.md"
```

---

```yaml
session_close: 2026-03-25T05
phase: 1
batch: D (supplement — 8th faction)
completed_stages:
  - "Löwenritter designed as full 8th faction with partial sheet (Military, Stability, Influence, Intelligence)"
  - "Coup trigger mechanic designed (4 conditions, Domain Action roll, attribute transfer from Crown)"
  - "Ethical framework assigned: Deontological Honor Code"
  - "Unique Action designed: Martial Law (with post-coup variant)"
  - "Grandmaster Sigrid Ehrenwall NPC created"
  - "Canon compliance verified (P-01, P-05, P-07, P-14)"
  - "System update requirements documented (faction count, board game, political axes, clock interactions)"
editorial_resolved:
  - "Löwenritter: full 8th faction, partial sheet in peacetime, full sheet on coup"
  - "Löwenritter loyalty: Crown as institution, not monarch"
  - "Church territory: begins holding territories at TC ~80"
  - "Almud's children: daughter married to Altonian Duke (border territory); son in Royal Court with Altonian tutoring pressure (1.5x invasion clock if refused)"
  - "Restoration Movement: non-TS leaders (scholars, guild members) as loose coalition"
  - "Southernmost Council: not publicly active in Restoration — occupied with Thread Wounds"
editorial_pending:
  - "Succession mechanic (Almud's son/Altonian pressure clock) — designed but not yet formalized"
  - "Named Restoration Movement NPCs — to be generated"
  - "Axis 10 (Succession) — to be formalized with heir mechanic"
  - "Niflhel primus inter pares (carried from S4)"
  - "Varfell Private Collection transfer (carried from S4)"
gaps_resolved_this_session:
  - "Löwenritter faction identity (opened S4, resolved S5)"
next_action:
  skill: orchestrator
  task: "Remaining pre-Batch-E work: succession mechanic, Restoration NPCs, then Batch E (board game, 14 gaps)"
  input: lowenritter_faction_card.md + batch_d_designs.md
output_files:
  - "lowenritter_faction_card.md"
```

---


```yaml
session_update: 2026-03-25T05b
completed_stages_addendum:
  - "Succession mechanic designed (Torben Loyalty Clock, 8->0 countdown)"
  - "Tutoring Demand trigger: IP 30"
  - "Covert contact mechanic: Intelligence Ob 3 to freeze loyalty decay 1 season"
  - "Retrieval options tiered by loyalty range (diplomatic/covert/military)"
  - "Elske backup heir pathway designed (four-way endgame)"
  - "Axis 10 formalized"
  - "Faction interaction map for succession (all 8 factions)"
  - "IP acceleration math verified (+10 IP delta over 10 seasons)"
  - "Canon compliance checked (P-01, P-07, P-09, P-12)"
editorial_resolved_addendum:
  - "Tutoring demand begins at IP 30"
  - "Covert contact can slow loyalty decay (Intelligence Ob 3/season)"
gaps_resolved_addendum:
  - "Axis 10 (Succession) — formalized with full mechanic"
output_files_addendum:
  - "succession_mechanic.md"
```

---


```yaml
session_update: 2026-03-25T05c
phase: 1
batch: E (board game — complete)
completed_stages:
  - "G-026: Turn structure (5-phase season: Planning/Negotiation/Reveal/Resolution/Accounting)"
  - "G-025: Order Set (7 universal + restricted + faction-specific replacements; 3 orders full-sheet, 2 partial)"
  - "G-059: Simultaneous order placement (clockwise rotation, dummy tokens)"
  - "G-060: Resolution priority (12-tier priority table, Influence tiebreak)"
  - "G-029: 15 territories designed (names, start control, Prosperity, Fortification, special properties, adjacencies)"
  - "G-028: Victory conditions per faction (8 primary + secondary scoring + shared TT loss)"
  - "G-050: Event deck (13 clock events + 10/20 seasonal events designed)"
  - "G-051: Season wheel (Spring/Summer/Autumn/Winter modifiers)"
  - "G-057: Thread operations (Weave/Investigate/Harvest + 15 Co-Movement Cards)"
  - "G-049: Negotiation (informal non-binding + formal Treaty procedure + max 2 treaties)"
  - "G-030: Component specification (full list: board, 8 faction sheets, tokens, decks, dice, reference cards)"
  - "G-031: NPC AI expansion (3-priority decision tree per faction + escalation rules)"
  - "Lowenritter integrated into all board game systems (partial sheet, post-coup full sheet)"
  - "Succession mechanic integrated (Torben Loyalty track as component)"
gaps_resolved_this_session:
  - "G-025 (Order Set)"
  - "G-026 (turn structure)"
  - "G-028 (victory conditions)"
  - "G-029 (territory differentiation)"
  - "G-030 (components)"
  - "G-031 (NPC AI)"
  - "G-049 (negotiation)"
  - "G-050 (event deck)"
  - "G-051 (season wheel)"
  - "G-057 (Thread operations)"
  - "G-059 (simultaneous placement)"
  - "G-060 (resolution ordering)"
editorial_minor:
  - "Territory names may need editorial pass (functional but placeholder-quality)"
  - "Varfell victory condition (3 artifacts) may need tuning"
  - "10 remaining seasonal event cards to write"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch F (hybrid + endgame, 3 gaps) — then Phase 1 complete"
  input: batch_e_designs.md + batch_d_designs.md + succession_mechanic.md + lowenritter_faction_card.md
output_files:
  - "batch_e_designs.md"
  - "lowenritter_faction_card.md"
  - "succession_mechanic.md"
```

---


```yaml
session_close: 2026-03-25T05-final
phase: 1
status: PHASE 1 COMPLETE — all 38 design gaps resolved
completed_stages:
  - "Lowenritter faction card: 8th faction, partial sheet (Mil/Stab/Inf/Int), coup trigger, Martial Law, Deontological Honor Code"
  - "Grandmaster Sigrid Ehrenwall NPC created"
  - "Succession mechanic v2: Torben Loyalty Clock (floors at 1), Tutoring Demand at IP 30, covert contact"
  - "Elske Almqvist: full NPC with Conviction (Family vs Self-Determination), Resonant Style (Evidence), three independence paths, seven succession scenarios"
  - "Church territorial seizure mechanic: TC 80 threshold, per-territory roll vs variable Ob, counter-play options"
  - "Batch E complete: 13 board game gaps (turn structure, Order Set, 15 territories, victory conditions, event deck, season wheel, Thread ops, negotiation, components, NPC AI, simultaneous placement, resolution ordering)"
  - "Batch F complete: 3 hybrid+endgame gaps (timing table, endgame conditions all modes, mode branching catalogue)"
  - "Phase 1 Design: ALL 38 gaps resolved across Batches A-F"
editorial_resolved:
  - "Lowenritter: full 8th faction, partial sheet peacetime, full sheet on coup"
  - "Lowenritter partial sheet: Military, Stability, Influence, Intelligence"
  - "Church territory seizure: per-territory roll at TC 80, not blanket takeover"
  - "Cognatic succession, male-heir priority"
  - "Torben Loyalty floors at 1 (Altonia never lets him renounce)"
  - "Elske: torn, recruitable by multiple factions, can seize independence with support"
  - "Tutoring Demand triggers at IP 30"
  - "Covert contact slows Torben loyalty decay (Intelligence Ob 3/season)"
  - "Almud has two children: Elske (married to Altonian Duke), Torben (Royal Court)"
  - "Church does not hold territories until TC 80"
  - "Restoration Movement: non-TS leaders, loose coalition (NPCs deferred)"
  - "Southernmost Council: not publicly active in Restoration"
editorial_pending:
  - "Territory names editorial pass (functional but placeholder)"
  - "Varfell victory condition tuning (3 artifacts)"
  - "10 remaining seasonal event cards"
  - "Named Restoration Movement NPCs"
  - "Niflhel primus inter pares (carried from S4)"
  - "Varfell Private Collection transfer (carried from S4)"
gaps_resolved_this_session:
  - "Lowenritter faction identity"
  - "Axis 10 (Succession)"
  - "G-025 (Order Set)"
  - "G-026 (turn structure)"
  - "G-028 (victory conditions)"
  - "G-029 (territory differentiation)"
  - "G-030 (components)"
  - "G-031 (NPC AI)"
  - "G-049 (negotiation)"
  - "G-050 (event deck)"
  - "G-051 (season wheel)"
  - "G-057 (Thread operations)"
  - "G-059 (simultaneous placement)"
  - "G-060 (resolution ordering)"
  - "G-018 (hybrid timing table)"
  - "G-021 (endgame conditions)"
  - "G-023 (mode branching catalogue)"
  - "Church territorial seizure (TC 80)"
next_action:
  skill: orchestrator
  task: "Phase 2 — Compilation. Assemble all designs into two documents (TTRPG ruleset + board game ruleset). 28 compilation stages estimated."
  input: >
    All design files: batch_a_designs.md, batch_bc_designs.md, batch_d_designs.md,
    batch_e_designs.md, batch_f_designs.md, lowenritter_faction_card.md,
    succession_mechanic.md, church_territorial_seizure.md.
    Plus existing ruleset checkpoint (valoria_ruleset_checkpoint_13.docx),
    Philosophical Foundations, Mechanics.docx.
  prerequisites:
    - "Resolve remaining editorial items (territory names, Varfell victory, event cards, Restoration NPCs, Niflhel/Varfell carried items)"
    - "Or defer them to Phase 2 in-line"
blockers:
  - "None — Phase 2 can begin"
output_files:
  - "lowenritter_faction_card.md"
  - "succession_mechanic.md (v2)"
  - "church_territorial_seizure.md"
  - "batch_e_designs.md"
  - "batch_f_designs.md"
```

---


```yaml
session_update: 2026-03-25T05d-final
completed_stages_addendum:
  - "Canonical timeline committed: 45 AG game start, TC 22, all chronological conflicts resolved"
  - "Church territorial seizure mechanic committed (TC 80, per-territory roll vs variable Ob)"
  - "Batch F committed (hybrid timing, endgame, mode branching)"
  - "6 document-level conflicts resolved (year, TC, children, rank, TT rationale, heir name)"
  - "Lowenritter starting values added to faction table (Mil 5, Int 3, Stab 5, Inf 3)"
  - "Schoenland documented as spoiler actor (not a faction)"
  - "Edvar retired as heir name — Torben canonical"
editorial_resolved_addendum:
  - "Game start: 45 AG (not 102 AG)"
  - "TC starting value: 22 (Church predates secession, consolidated post-war)"
  - "Timeline is canonical for setting chronology, supersedes checkpoint references"
output_files_addendum:
  - "valoria_canonical_timeline.md"
  - "church_territorial_seizure.md"
  - "batch_f_designs.md"
standing_editorial:
  - "E-01: Perpetrator of ~18 AG assassination — TBD"
  - "E-03: In-world name for AG calendar — TBD"
```

---




---

# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-full-compile
phase: 2
status: Phase 2 COMPLETE — all 16 TTRPG stages compiled; full document assembled
completed_stages:
  - Stage 1: Core Engine
  - Stage 2: Characters
  - Stage 3: Thread Operations
  - Stage 4: Southernmost
  - Stage 5: Clocks (TT/TC/IP)
  - Stage 6: Factions
  - Stage 7: Territories
  - Stage 8: Combat
  - Stage 9: Social Systems
  - Stage 10: Advancement
  - Stage 11: Scale Transitions
  - Stage 12: Campaign Modes
  - Stage 13: NPCs + Institutional Actors
  - Stage 14: GM Tools
  - Stage 15: Thread Spell Catalog
  - Stage 16: Reference Materials
compilation_progress: 16/16 TTRPG stages complete
assembly_output: compilation/valoria_ttrpg_complete.md (244KB, ~4,100 lines, commit a45b6525)
notes:
  - Stage 15 contains Thread Spell Catalog only (not equipment — weapons in stage 8, dissolution residue in stage 3)
  - CP13 Corruption track excluded (not canon per user)
  - Taint track references flagged for canon-guard pass — stage 3 §5.10 uses "Taint Track" header; canonical mechanic is CD (Coherence Degradation)
  - Heart/Poise attribute references in stages 3, 9 use old 9-attribute names; stage 1 uses canonical 10-attribute set — cross-stage inconsistency requires canon-guard pass
  - 4 EDITORIAL flags remain in assembled document (see below)
canon_guard_issues_flagged:
  - §5.10 header reads "Taint Track" — should read "Transformation and Epistemic Seduction — Coherence Degradation"
  - Stage 3 Leap pool uses "Heart" — should use canonical attribute (Focus or Spirit per 10-attr set)
  - Stage 9 Composure formula uses "Poise + Heart" — neither in 10-attr set; needs resolution
  - Stage 2 Inspiration cap references "Heart score" — needs attribute substitution
editorial_pending:
  - Renown permission table (Renown 1-10 tiers) — only data point is Renown 6
  - Varfell Private Collection transfer (PC takeover scenario)
  - Niflhel primus inter pares decision
  - Revolution named elder NPC contact (optional)
  - Territory names (batch_e placeholder vs design doc names)
  - Varfell victory condition tuning
  - 10 remaining seasonal event cards (of 20 total)
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak)
  - Revolution named NPC stat blocks (Edith Varn)
next_action:
  stage: Stage 17 (Canon Guard Pass)
  task: Systematic canon-guard review of assembled document — resolve attribute name inconsistencies, remove Taint references, verify all 14 canon constraints
  model: Sonnet 4.6
  input_file: compilation/valoria_ttrpg_complete.md
  priority_issues:
    - Heart/Poise → canonical 10-attr equivalents (Focus, Spirit, Presence, Bonds)
    - §5.10 Taint Track header → CD
    - Composure formula in stage 9
    - Inspiration cap attribute in stage 2
output_files:
  - compilation/stage15_spell_catalog.md committed (d29b845f)
  - compilation/stage16_reference.md committed (bb85580e)
  - compilation/valoria_ttrpg_complete.md committed (a45b6525)

---

# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-checkpoint14
phase: 2
status: Checkpoint 14 compiled and committed

completed_this_session:
  - Stage 17 canon guard pass (all P1-P14 constraints verified)
  - 6 mechanical patches applied to valoria_ttrpg_complete.md
  - 17 hybrid gaps resolved (G-075, G-079–G-095)
  - §12.3 Hybrid Mode rewritten with all resolved gap content
  - §12.9 Hybrid Consequence Rules added (new section)
  - Checkpoint 14 exported: compilation/valoria_ruleset_checkpoint_14.md

commits:
  - stage17_canon_guard.md: 8526e934
  - valoria_ttrpg_complete.md (stage 17 patches): f318f7ee
  - designs/hybrid_gaps_resolved.md: 6e543b5c
  - valoria_ttrpg_complete.md (hybrid additions): 38a0fe31
  - compilation/valoria_ruleset_checkpoint_14.md: 2115df16

canonical_decisions_locked:
  thread_op_pools:
    Leap: Attunement + History bonus
    Contact_Duration: Focus score (rounds)
    Wound_disruption: Focus check TN 7 Ob 1
    All_ops_Weave_Pull_FR: Spirit + History bonus
  composure: Presence + 6 (range 7-13)
  debate_pool: Cognition + History bonus
  battle_engine: Officer Cognition (attack) + Presence (cohesion/rally); initiative Cognition
  personal_combat_manoeuvres: Agility
  inspiration_cap: Spirit score (no derived name)
  coherence_track: individual 10-0 (10=fully coherent, 0=monstrous NPC)
  thread_stability: campaign-arc 20-0 (20=stable, 0=crisis)
  hybrid_session_structure: Personal (90-150min) → Strategic → Cascade
  hybrid_pacing: 1 session minimum per season
  hybrid_fog_of_war: 4 qualitative states; exact for own faction; Intel always hidden
  hybrid_handoffs: batch to Cascade; GM ledger
  hybrid_zoom_in: player-involved only
  hybrid_cascade: 5-step sequence, GM-only
  hybrid_resources_wealth: threshold = 2x rolled; below = stressed
  hybrid_flashback: Personal phase only
  hybrid_pc_death: Crisis penalty; take over loyal NPC or succession; no new characters
  hybrid_faction_collapse: continue as personal character; lose faction dice bonuses
  hybrid_downtime: concurrent with Strategic phase
  hybrid_advancement: board game successes generate CP
  hybrid_knot_gating: gated by in-scene discovery

editorial_pending:
  - Renown permission table (tiers 1-10)
  - Varfell Private Collection transfer
  - Niflhel primus inter pares
  - Revolution named elder NPC
  - Territory names (batch_e placeholders)
  - Varfell victory condition tuning
  - 10 remaining seasonal event cards
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak)
  - Revolution named NPC stat blocks (Edith Varn)

next_action:
  recommended: Board game mode compilation (Phase 2 remaining deliverable) OR Phase 3 simulation
  model: Sonnet 4.6
  note: G-093 Resources/Wealth formula (2x vs 2x-1) flagged for Phase 3 stress testing

model_routing_notes: Sonnet 4.6 throughout — canon guard, hybrid gap resolution, compilation
---
session_close: 2026-03-26
checkpoint: 14-editorial
model: claude-sonnet-4-6
completed_stages:
  - Cross-reference audit CP14 TTRPG vs BG (10 passes, 62 findings)
  - P1 editorial resolution (7 items)
  - P2/P3 editorial round (16 items A-P)
  - Full correction push to both CP14 and BG

commits:
  cp14: 2325655348e0
  bg: c49141521803

corrections_applied:
  cp14:
    - Territory names: all 15 canonical
    - Forced Resolution -> Locking and Snapping throughout
    - Rattled: wound-equivalent track (-1D per accumulation)
    - Coherence: full spec with Coherence 2 consult, Coherence 0 monstrous, saving attempt rule
    - Monstrous entities: excess undifferentiated Thread via gaps
    - Knots: +1 Strain for +2D -> +2 strain for +3D; presence/narration required; closer bonds = higher capacity
    - Domain Ob: direct (1-7), pool adds faction stat if leadership position held
    - Co-movement: d10 replacing d6, no supplements, TPS added to all Thread pools
    - TPS = TS / 10 (round down)
    - Renown: full 0-10 table
    - Vaynard: Ambition Track (0-100), TK 4-5 redesigned, TS via collection
    - Vaynard victory: Path A (all 15) or Path B (10+ territories + Stillhelm + TK5 + TS75+)
    - Niflhel: four competing networks with supremacy mechanic
    - Eidur Sjostrom and Hakan Reusfoldt NPCs added
    - TC pause threshold: Stability <= 4
    - Attribute pool: 31 points
    - S-16 through S-20 seasonal events added

editorial_still_pending:
  - S-08 Einhir site name
  - E-01 assassination perpetrator
  - Vaynard Private Collection transfer procedure
  - Niflhel Supremacy seasonal resolution procedure
  - Coherence 0 saving attempt procedure

next_action:
  recommended: Phase 3 simulation or CP15 compilation
  model: Sonnet 4.6



---

session_close: 2026-03-27
checkpoint: 14-sim-prep
model: claude-sonnet-4-6
completed_stages:
  - Identified all mechanics directly impacted by editorial decisions committed 2026-03-26
  - Mapped 12 mechanic groups requiring re-simulation
  - Discovered P1 attribute pool inconsistency (§2.2 vs §14.1/§12)
  - Prepared full simulation routing table and handoff

p1_finding:
  issue: Attribute pool contradiction
  location_1: "§2.2 — 31 points distributed across 10 attributes"
  location_2: "§14.1 (Session Zero checklist) — 18 attribute points"
  location_3: "§3772 (GM checklist) — 18 attribute points"
  location_4: "§12 (hybrid) — 18 attribute points"
  action_required: Propagate 31 to all checklist references before next push

mechanics_flagged_for_simulation:
  - id: M-11/M-12/M-13/M-14/M-15
    change: TPS (=TS÷10 round down) added to all Thread operation pools
    test_modes: [A_isolation, B_interaction]
  - id: M-16/M-17/M-18
    change: Co-movement d10 replacing d6; History Resonance and Flashback removed from co-movement
    test_modes: [A_isolation, D_edge_cases]
  - id: M-26
    change: Coherence renamed Intelligibility (10->0); effects table revised; separate Coherence track retained
    test_modes: [A_isolation, B_interaction_with_Knots, D_edge_cases]
  - id: M-32
    change: Knot Call = +2 strain for +3D; closer bonds = higher strain capacity
    test_modes: [B_interaction, D_edge_cases]
  - id: M-03_Composure
    change: Rattled = wound-equivalent track (-1D per mark, cumulative); Composure resets after each Rattled
    test_modes: [A_isolation, D_edge_cases]
  - id: M-42
    change: Domain Ob = direct target stat (1-7, no division); pool adds faction stat if leadership held
    test_modes: [A_isolation, B_interaction, C_scenario]
  - id: M-36
    change: Renown 0-10 full permission table; Debate bonuses at tier 5/6/7/8
    test_modes: [A_isolation, B_interaction_with_Debate]
  - id: M-47_Vaynard
    change: Ambition Track (0-100, 5 thresholds); TK system redesigned; TS via originary lock collection
    test_modes: [A_isolation_full_range, C_scenario]
  - id: M-44_Niflhel
    change: Four-network Supremacy Mechanic at seasonal accounting
    test_modes: [A_isolation, C_endgame_scenario]
  - id: M-46_TC
    change: TC pause threshold changed from Stability <= 5 to Stability <= 4
    test_modes: [A_boundary, C_scenario]
  - id: M-43_seasonal
    change: S-16 through S-20 added (five new event triggers)
    test_modes: [C_scenario, D_interaction_with_existing_events]

commits: {}

editorial_still_pending:
  - S-08 Einhir site name (deferred)
  - Co-movement d10 table in BG (uses card system; d10 is TTRPG only)
  - E-01 assassination perpetrator (intentionally unresolved)
  - Vaynard Private Collection transfer procedure (design pending)
  - Niflhel Supremacy seasonal resolution full procedure (design pending)
  - Coherence 0 saving attempt procedure (design pending)

next_action:
  task: Run full simulation suite on all 12 mechanic groups above
  skill: valoria-simulator
  modes: [A_isolation, B_interaction, C_scenario, D_edge_cases]
  priority_order:
    1: TPS across all Thread ops (Mode A)
    2: Co-movement d10 (Mode A + D)
    3: Intelligibility x Knot strain interaction (Mode B)
    4: Rattled stacking (Mode A + D)
    5: Domain Ob + leadership pool (Mode B with faction stats)
    6: Renown x Debate (Mode B)
    7: Vaynard Ambition Track full range (Mode A)
    8: Niflhel Supremacy endgame (Mode A + C)
    9: TC pause at Stability <= 4 (Mode C)
    10: Seasonal events S-16-S-20 (Mode C)
  output_file: tests/valoria_stress_tests_batch3.md
  also_repair: Propagate attribute pool = 31 to §14.1 and §12 checklist references in CP14
  model: Sonnet 4.6

---

session_close: 2026-03-27
checkpoint: 14-sim-prep
model: claude-sonnet-4-6
completed_stages:
  - Identified all mechanics directly impacted by editorial decisions committed 2026-03-26
  - Mapped 12 mechanic groups requiring re-simulation
  - Discovered P1 attribute pool inconsistency (§2.2 vs §14.1/§12)
  - Prepared full simulation routing table and handoff

p1_finding:
  issue: Attribute pool contradiction
  location_1: §2.2 — 31 points distributed across 10 attributes
  location_2: §14.1 (Session Zero checklist) — 18 attribute points
  location_3: §3772 (GM checklist) — 18 attribute points
  location_4: §12 (hybrid) — 18 attribute points
  action_required: Propagate 31 to all checklist references before next push

---

session_close: 2026-03-27
checkpoint: 14-editorial-complete
model: claude-sonnet-4-6
completed_stages:
  - BUG-004 verified complete (stage13 clean)
  - stage3 full Stage17-P3 propagation: pool formulas, CD->ThS, FR->Locking/Snapping, §5.6 degree table
  - stage2 GAP-UC-03-A Devout targeting ruling; Locking/Snapping name fix
  - F-32 coup counter (Option A): stage6, stage13, CP14
  - F-33 Martial Law (Option A): stage6, CP14
  - F-34 TC80 seizure procedure (user ruling): stage6, CP14
  - GAP-UC-03-A Devout targeting (Option A): stage2, CP14
  - F-33B simulation: Option B rejected (2x P1, 1x P2 vs no advantages)

commits:
  stage3: 27f9335a484e
  stage6: 94695c70e70e
  stage13: 13ffa7265870
  stage2: 68fed70656e5
  cp14: a83904a1a1d3
  f33b_sim: 765fb5e24512

editorial_decisions_resolved:
  F-32: Coup Counter 0-3, three named triggers, never decrements
  F-33: Martial Law Option A (secondary Military Ob 2 check; Covert Ob 3 for others; exit Ob = Military/2)
  F-34: Church Mandate vs owner Mandate/2; flat TC +1/+3/+5 on seizure; no per-season accrual; counter-play options
  GAP-UC-03-A: Devout provides no protection from being targeted; experiences result without understanding cause

editorial_still_pending:
  - S-08 Einhir site name
  - E-01 assassination perpetrator
  - Vaynard Private Collection transfer procedure
  - Niflhel Supremacy seasonal resolution procedure
  - Coherence 0 saving attempt procedure
  - F-31: Devout bypass at TS 0-9 (fix note — Haiku-tier, mechanical)

f33b_verdict: Option A correct. Option B introduces P1 exit-condition gap and P1 coup-as-weapon dominant strategy.

next_action:
  task: Batch 5 — core combat engine M-01 through M-09
  skill: valoria-simulator
  mode: A_isolation then B_interaction
  note: 30 mechanics still untested; combat engine is foundational; start here
  model: Sonnet 4.6

---
session_close: 2026-03-27
checkpoint: post-batch6-simulation
model: claude-sonnet-4-6
completed_stages:
  - Batch 6 simulation complete: History Resonance, Push/Certainty blast radius, Diagnosis standalone, Co-Movement Cards BG, Impression Track, Reading Exchange, Defection (gap status confirmed), Fortification, BG Turn Structure, Victory Conditions, Hollow Victory
  - P1 fix applied: Reading Exchange Ob=1 + degree mapping (stage9 §9.4)
  - Impression Track + Knot Crisis priority rule added (stage2 §4.7)
  - Fortification construction Domain Action added (stage8 §8.4)
  - BG FORTIFY order added (stage_bg B5)
  - BG mid-phase clock game-end check added (stage_bg B4)
  - G-111 through G-114 closed same session
  - G-115 closed: Church VC = TC≥60 + Himmelenger + Valorsplatz; expansion lock TC≥40

editorial_pending:
  - G-115: Church victory condition — is Church intentionally unwinnable in standard play, or should TC≥80 be changed to TC≥60?
  - B6-VC-03: 2-player NPC order reduction (2 instead of 3) may undermine clock tension
  - Co-Movement cards CM-11 through CM-20 (BG-E-01)
  - Varfell TK 5 consequence (BG-E-02)
  - S-08 Einhir site name; E-01 perpetrator; Niflhel primus inter pares; territory names; Restoration NPCs

gap_register_delta:
  closed: G-111 (RE Ob), G-112 (IT+Knot), G-113 (Fortification build), G-114 (BG mid-phase)
  open: G-115 (Church VC editorial)

commits:
  - tests/valoria_stress_tests_batch6.md: Batch 6 sim results
  - compilation/stage9_social.md: Reading Exchange Ob fix
  - compilation/stage2_characters.md: IT+Knot Crisis priority
  - compilation/stage8_combat.md: Fortification construction
  - compilation/stage_bg_board_game_mode.md: FORTIFY order + mid-phase check

simulation_coverage_summary:
  batches_complete: [B5-ModeA, B5-ModeB, B6]
  mechanics_tested: M-001 through M-009 (M-005 eliminated), History Resonance, Push, Diagnosis, Co-Movement BG, Impression Track, Reading Exchange, Fortification, BG Turn Structure, Victory Conditions
  mechanics_pending: M-010 through M-056 (Thread ops, faction, combat specifics), Defection (design pending G-036)
  p1s_total_found: 5 (M002-01 fixed, M009-01 fixed, B03-01 fixed, B07-01 fixed, B6-RE-01 fixed)
  all_p1s_closed: true

next_action:
  task: Continue simulation — M-010+ (Thread ops, faction mechanics, combat specifics)
  all_editorial_blockers_cleared: true
session_close: 2026-03-27
checkpoint: post-infrastructure-overhaul
model: claude-sonnet-4-6
completed_stages:
  - Rewrote project_instructions.md — lean protocol, inline router, item-by-item GitHub reads
  - Created tools/model_router.html — auto-routing artifact for Haiku/Sonnet/Opus inline
  - Session start now reads only 3 files: session_log_current, gap_register (P1 count), workplan (phase/stage)
  - All Haiku/Opus tasks route through artifact inline; no session branching required

commits:
  - project_instructions.md: full rewrite
  - tools/model_router.html: new file

next_action:
  task: Phase 3 simulation — BG-specific mechanics M-62–64, M-67–70, M-72, M-74–75; full-scenario Mode C; then S-10/S-11/S-12
  all_reconciliation_tasks_complete: true
  p1_open_design: 40 items

---

```yaml
session_id: 2026-03-27T13
phase: Phase 3 (Simulation) — Batch 11 complete + replay
status: PP-086–091 committed; mass combat replay validates PP-086/087/091

completed_this_session:
  - PP-086–091 drafted and pushed (6 P1 fixes)
  - Mass combat replay (The Field at Harskeld): 5-round engagement, Crown vs. Varfell
  - PP-086 (base damage): validated
  - PP-087 (Formation Break stacking): validated
  - PP-091 (Artillery Bombard): validated

patch_count: 91 total (33 P1, 47 P2, 10 P3, 1 design)
next_action: M-036 (Parliamentary Vote) and M-037 (Grand Debate isolation)
```

---

session_id: 2026-03-27T14
phase: Thread Operations Redesign (philosophical + mechanical)
status: v2.5 FINAL DRAFT — canon-compliant, stress-tested, ready for Sonnet-tier simulation

completed_this_session:
  - Critical philosophical evaluation of threadweaving mechanics against Foundations
  - 6 editorial decisions resolved (ThS/Intelligibility merge, Gap proximity, FR asymmetry, Spooling level, Gap closure reclassification, Threadcut rendering)
  - Foundational reframe: Leap as rendering suspension, not rendering expansion
  - Foundational reframe: threads as oscillation of three axes, not objects with properties
  - Foundational reframe: beings ARE drawings-from-ground (spooling IS what beings are)
  - Einhir principle stated as design principle (game rewards restraint, punishes ambition)
  - Full threadweaving redesign document produced (v2.5, ~930 lines)
  - 4 systems replaced: Intelligibility + ThS + Taint → Coherence (10→0); TT → Rendering Stability (100→0)
  - 1 new operation type: Mending (substrate repair, Attunement + Focus + TPS pool)
  - Diagnosis repositioned before Leap (last act of rendering)
  - Diagnosis gains trajectory perception (scale-gated)
  - Threadcut beings: observer-dependent rendering, Rendering Strain, De-actualisation
  - Over-actualisation hazard added to Weaving at Relational+ scale
  - FR Lock gains chronic consequences (RS drift, adjacent Ob penalties)
  - 18 extreme chain stress tests across 3 batches
  - 30 patches applied (numbered P-01 through P-30)
  - 2 canon audits: 14/14 PASS + 3/3 philosophical claims INTEGRATED
  - Board game: Mend order added, Co-Movement deck expanded 15→18, degree table for all Thread orders
  - Hybrid: Coherence tracking, Lock chronic registration, Mending cross-mode rules

editorial_decisions:
  - ThS + Intelligibility merged into Coherence (10→0)
  - Gap proximity: no benefit (excess being is catastrophe, not resource)
  - FR Lock vs Dissolution: asymmetric (chronic vs acute), not equal
  - Spooling: Level 1 (framing only)
  - Gap closure: new operation type Mending (not Weaving, not FR Dissolution)
  - Threadcut rendering: observer-dependent at baseline, can render beyond ceiling at cost of accelerated exhaustion
  - Taint track: eliminated. Dissolution residue = accelerated Coherence loss.
  - TT renamed Rendering Stability, inverted (100→0)
  - Solmund → Solmund (logged for Haiku batch, not yet applied)
  - AG → AS calendar (logged for Haiku batch)
  - Church of Solmund → Church of Solmund (logged for Haiku batch)

output_files:
  - designs/threadweaving_redesign_v25.md (main design document)
  - tests/threadweaving_stress_tests_batch1.md
  - tests/threadweaving_stress_tests_batch2.md
  - tests/threadweaving_stress_tests_batch3.md
  - canon/canon_review_threadweaving_v24.md
  - canon/canon_reaudit_threadweaving_v25.md

deferred_tasks:
  - "Solmund rename (all files) — Haiku-tier"
  - "AG → AS calendar rename — Haiku-tier"
  - "Sonnet-tier simulation: Coherence degradation curves, FR Lock chronic drift, Mending pool probability, over-actualisation impact, Diagnosis-before-Leap combat timing, threadcut De-actualisation"
  - "Mode 2 stat block vs D-18 ruling verification"
  - "Board game RS track integration (Co-Movement deck rewrite)"
  - "Hybrid mode branching catalogue update"
  - "Compilation: new Stage 3 Thread Operations chapter"

blockers: []

next_action:
  task: Sonnet-tier simulation of v2.5 mechanics (Coherence curves, Mending pools, combat timing)
  model: Sonnet
  input: designs/threadweaving_redesign_v25.md

---

session_id: 2026-03-27T18
phase: Thread Operations Redesign — Simulation Batch 2
status: Batch 2 complete. 3 P1, 6 P2, 2 P3. Editorial decisions needed on F-03 and F-04.

completed_this_session:
  - Stress test batch 2: Collective Operations, Past-Oriented Pulling, Involuntary Leap, Opposing Ops
  - 11 new findings (SIM2-F-01 through SIM2-F-11)
  - Gap register updated: +11 items
  - Output: tests/sim_threadweaving_v25_batch2.md

critical_findings:
  - SIM2-F-03 (P1): Past-Oriented Pulling recency Ob table absent from v2.5 — blocks play
  - SIM2-F-04 (P1): Past-Oriented Pulling pool (Spirit+History only) makes TS irrelevant to execution
  - SIM2-F-09 (P1): Involuntary-to-voluntary-extension bypasses concealment — exploit

editorial_decisions_needed:
  - SIM2-F-04: Add TPS (or TPS/2) to Past-Oriented Pulling pool? Or add rationale note?
  - SIM2-F-03: Reproduce recency Ob table in §2.4 (from prior ruleset — needs source)

deferred_tasks:
  - Resolve editorial decisions on SIM2-F-03 and SIM2-F-04
  - Mechanic-audit patches for SIM2-F-03, F-04, F-09 (P1s)
  - P2 patches: SIM2-F-01, F-02, F-05, F-08, F-10, F-11
  - Haiku batch: Solmund rename, AG→AS, Church rename
  - Stage 3 compilation (pending all patches)

blockers:
  - SIM2-F-03: recency Ob table source unknown — need prior ruleset or user input
  - SIM2-F-04: design decision required before patching

next_action:
  task: Editorial decisions on SIM2-F-03 and SIM2-F-04
  model: Current (user decision)

---

session_id: 2026-03-27T25
phase: Phase 2 Compilation — Stage 3 Thread Operations COMPLETE
status: Stage 3 compiled, canon-guard passed, report written. No open P1 findings.

completed_this_session:
  - Applied final SIM7 patches (9 patches including Foundational Pull, threadcut external ops)
  - Assembled Stage 3 Thread Operations from threadweaving_redesign_v25.md
  - Reformatted to compilation structure (§5.0–§5.8, Part Five numbering)
  - Stripped design-doc framing; cleaned migration notes; fixed cross-references
  - Canon-guard pass: 14/14 PASS, 0 violations, 0 PARTIAL
  - Compilation report written: stage3_compilation_report.md
  - Stage 3 pushed: 78,201 chars, 826 lines (was 38,597 chars pre-v2.5)

stage3_stats:
  old_size: 38597 chars
  new_size: 78201 chars
  patches_applied: 52
  canon_guard: PASS 14/14
  open_p1: 0
  open_p2: 12 (non-blocking, logged in §5.8)
  open_p3: 10

compilation_progress:
  stages_complete: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, BG]
  stage3_was_outdated: true (pre-v2.5)
  stage3_now: current (v2.5, fully patched)
  note: Infrastructure audit (valoria_infrastructure_audit.md) indicates all 17 TTRPG stages + BG already compiled. Stage 3 was the only outdated one. Phase 2 compilation may be complete.

deferred_tasks:
  - Haiku batch: Solmund rename (all files), AG→AS calendar rename, Church of Solmund→Church of Solmund
  - Stage 4 cross-reference: SIM5-F-08 (RS threshold at Southernmost)
  - P2 items in §5.8 — assign to relevant downstream stages for polish pass
  - Verify other stages don't reference old Stage 3 terminology (TT, ThS, CD, Intelligibility)

next_action:
  task: Haiku rename batch OR verify compilation completeness across all stages
  model: Haiku (renames) / Sonnet (verification)

---

session_id: 2026-03-27T_THREADWEAVING_FINAL
phase: Phase 2 Compilation — Stage 3 Thread Operations complete
status: CLOSED — all work committed to GitHub

## SESSION SUMMARY

### What was accomplished
- Full philosophical and mechanical redesign of Thread Operations (v2.5) stress-tested and compiled
- 8 simulation batches run (64 total findings)
- 52 findings patched into designs/threadweaving_redesign_v25.md
- Stage 3 Thread Operations recompiled from 38,597 → 78,201 chars
- Canon guard: 14/14 PASS, 0 violations

### Key design decisions made this session
1. ThS/Intelligibility/CD/Taint → Coherence (10→0, unified track)
2. Thread Tension (TT) → Rendering Stability (RS, 100→0, inverted)
3. Diagnosis repositioned before Leap (last act of rendering)
4. Mending added as new operation type (substrate repair, not thread operation)
5. Coherence cap: −1 per operation maximum (all degree table costs absorbed)
6. Past-Oriented Pulling pool: Spirit + History + TPS÷2
7. Lock removal Ob: (original TS ÷ 10) − 2, minimum 1
8. §9.7 threadcut interference: capped at +4 (not uncapped)
9. Mending Ob ceiling: 8 (regardless of stacked modifiers)
10. Residue Coherence: Option C (−1 at Object/Personal; absorbed at Relational+)
11. FR Lock immediate RS cost: −1/−2/−3 (was −2/−3/−4)
12. Foundational Past-Oriented Pulling: Einhir framework required, +2 Ob, RS ×3
13. Threadcut beings: can perform external Thread operations at cost of +1 Rendering Strain each
14. Collective Leap: all practitioners roll own Leap; Anchor failure = lattice never forms
15. RS Critical: 2–4 season endgame; Mandate 0 = Faction Fracture

### GitHub state (all committed)
- designs/threadweaving_redesign_v25.md — fully patched (100,790 chars)
- compilation/stage3_thread_operations.md — recompiled v2.5 (78,201 chars)
- compilation/stage2_characters.md — SIM8-F-07/08 patches applied
- compilation/stage3_compilation_report.md — canon guard report
- tests/sim_threadweaving_v25.md — batch 1
- tests/sim_threadweaving_v25_batch2.md
- tests/sim_threadweaving_v25_batch3.md
- tests/sim_threadweaving_v25_batch4.md
- tests/sim_threadweaving_v25_batch5.md
- tests/sim_threadweaving_v25_batch6.md
- tests/sim_threadweaving_v25_batch7.md
- tests/sim_threadweaving_v25_batch8.md
- tests/mechanic_audit_sim_patches.md
- valoria_gap_register_consolidated.md — updated (~226 items)
- session_log_current.md — this close
- session_log_archive.md — prior session appended

### Open items (non-blocking)
P2 (12): SIM2-F-01, SIM3-F-02/03, SIM4-F-02, SIM5-F-08, SIM6-F-02/04, SIM7-F-04, SIM8-F-02/03/09/10
P3 (10): SIM2-F-06, SIM3-F-05, SIM4-F-05, SIM5-F-09, SIM6-F-01/07/08, SIM7-F-02/05, SIM8-F-01
All logged in §5.8 of compiled Stage 3.

### Editorial pending (unchanged from prior session)
- Territory names
- Varfell victory tuning
- 10 seasonal event cards
- Restoration NPCs
- Niflhel primus inter pares
- Varfell Private Collection transfer
- E-01 (assassination perpetrator)
- E-03 (AG calendar name — now blocked on AG→AS rename batch)

### Deferred tasks (next session)
1. Haiku batch: Solmund rename (all files), AG→AS calendar, Church of Solmund→Church of Solmund
2. Cross-stage terminology check: Stages 4–17 may reference old TT/ThS/CD terms
3. Stage 4 cross-reference: SIM5-F-08 (RS threshold +1 Ob at Southernmost)
4. Phase 3 gate: simulation coverage matrix now runnable against compiled Stage 3

### Resume instruction for next session
Read session_log_current.md. Phase 2 compilation is complete (all 17 TTRPG stages + BG compiled; Stage 3 now current). Priority 1: Haiku batch renames (Solmund, AG→AS, Church). Priority 2: Cross-stage terminology audit for TT/ThS references in Stages 4–17.

---

session_id: 2026-03-28T_BATCH_RESOLUTIONS
phase: Phase 2 Compilation — combat testing in progress (TTRPG); BG/Hybrid Thread commits pending
status: OPEN — batch resolutions committed; combat testing ongoing

## SESSION SUMMARY

### What was accomplished
- 37 gap register items resolved via PP-094–PP-130
- All derived from canon constraints + compiled stages — no editorial approval required
- valoria_patch_proposals.md updated (PP-094–PP-130 appended)
- valoria_gap_register_consolidated.md updated (status log appended)

### Resolutions by category
- Social system: G-099 (mid-Debate incapacitation), G-100 (Renown scope)
- Faction/political: G-101–G-104, G-111–G-114, G-131, G-132 (Stability floor), G-136 (TC brake fix)
- Faction stats: G-133 (Niflhel Intel=6), G-115 (archetype stat blocks)
- Thread operations: G-116–G-118, G-125, G-127–G-130, SIM2-F-03/04/09, SIM5-F-02/07, SIM6-F-03/05/10, SIM7-F-03/07/08/09/10, SIM8-F-09/10
- Mass combat: G-135 (damage formula)
- NPC: G-129 (Torben TLK drain rate)
- Documentation/asymmetry: SIM3-F-02/03 (Crown/Hafenmark Thread asymmetry — intentional, now documented)

### Key design decisions
- PP-109: Dissolution Residue drains Certainty (not Coherence) — resolves SIM5-F-07 by proxy
- PP-114: Stability floor removed; Faction Fracture at Stability 0 for 2+ seasons; Crown/Church exception defined
- PP-118: Church Stability TC brake standardised to ≤3 (was ≤4/≤5 conflict between stages)
- PP-107: Past-Oriented Pulling complete — recency table, degree table, accessibility note, Foundational scale protocol
- PP-100: Devout Discovery Event bypass rewritten to theological confrontation (not TS-gated witnessing)
- PP-104: GEN-03/06/07 stat blocks written (Inquisitor, Riskbreaker, Knight Templar)

### GitHub state (all committed)
- valoria_patch_proposals.md — PP-094–PP-130 appended
- valoria_gap_register_consolidated.md — batch resolution log appended, ~37 items marked Resolved/Closed

### Still open (not resolved this session)
- P1 remaining design: G-025–G-033 (board game architecture — requires more design context)
- Sim-derived P2 open: ~51 items (SIM-F series, various)
- Hybrid design: 14 items (G-078–G-095 series)
- Rename batch (Solmund/AG→AS/Church): still deferred
- Cross-stage terminology audit (TT/ThS/CD refs Stages 4–17): still deferred
- Editorial pending: unchanged (8 items)

### Combat testing status (user-reported)
- TTRPG combat system under active test
- Thread changes committed
- BG/Hybrid mode commits pending (user handling)

### Resume instruction for next session
Read session_log_current.md. Phase 2 complete; Phase 3 simulation underway. 37 gaps resolved this session (PP-094–PP-130). Next priorities: (1) compile resolved patches into relevant stages (Stage 3, 5, 6, 8, 9, 13); (2) deferred Haiku rename batch; (3) cross-stage terminology audit. P1 board game design gaps (G-025–G-033) remain unstarted and block BG compilation stages.

---

session_id: 2026-03-28T_BATCH_RESOLUTIONS
phase: Phase 2 Compilation — combat testing in progress (TTRPG); BG/Hybrid Thread commits pending
status: OPEN — batch resolutions committed; combat testing ongoing

## SESSION SUMMARY

### What was accomplished
- 37 gap register items resolved via PP-094–PP-130
- All derived from canon constraints + compiled stages — no editorial approval required
- valoria_patch_proposals.md updated (PP-094–PP-130 appended)
- valoria_gap_register_consolidated.md updated (status log appended)

### Resolutions by category
- Social system: G-099 (mid-Debate incapacitation), G-100 (Renown scope)
- Faction/political: G-101–G-104, G-111–G-114, G-131, G-132 (Stability floor), G-136 (TC brake fix)
- Faction stats: G-133 (Niflhel Intel=6), G-115 (archetype stat blocks)
- Thread operations: G-116–G-118, G-125, G-127–G-130, SIM2-F-03/04/09, SIM5-F-02/07, SIM6-F-03/05/10, SIM7-F-03/07/08/09/10, SIM8-F-09/10
- Mass combat: G-135 (damage formula)
- NPC: G-129 (Torben TLK drain rate)
- Documentation/asymmetry: SIM3-F-02/03 (Crown/Hafenmark Thread asymmetry — intentional, now documented)

### Key design decisions
- PP-109: Dissolution Residue drains Certainty (not Coherence) — resolves SIM5-F-07 by proxy
- PP-114: Stability floor removed; Faction Fracture at Stability 0 for 2+ seasons; Crown/Church exception defined
- PP-118: Church Stability TC brake standardised to ≤3 (was ≤4/≤5 conflict between stages)
- PP-107: Past-Oriented Pulling complete — recency table, degree table, accessibility note, Foundational scale protocol
- PP-100: Devout Discovery Event bypass rewritten to theological confrontation (not TS-gated witnessing)
- PP-104: GEN-03/06/07 stat blocks written (Inquisitor, Riskbreaker, Knight Templar)

### GitHub state (all committed)
- valoria_patch_proposals.md — PP-094–PP-130 appended
- valoria_gap_register_consolidated.md — batch resolution log appended, ~37 items marked Resolved/Closed

### Still open (not resolved this session)
- P1 remaining design: G-025–G-033 (board game architecture — requires more design context)
- Sim-derived P2 open: ~51 items (SIM-F series, various)
- Hybrid design: 14 items (G-078–G-095 series)
- Rename batch (Solmund/AG→AS/Church): still deferred
- Cross-stage terminology audit (TT/ThS/CD refs Stages 4–17): still deferred
- Editorial pending: unchanged (8 items)

### Combat testing status (user-reported)
- TTRPG combat system under active test
- Thread changes committed
- BG/Hybrid mode commits pending (user handling)

### Resume instruction for next session
Read session_log_current.md. Phase 2 complete; Phase 3 simulation underway. 37 gaps resolved this session (PP-094–PP-130). Next priorities: (1) compile resolved patches into relevant stages (Stage 3, 5, 6, 8, 9, 13); (2) deferred Haiku rename batch; (3) cross-stage terminology audit. P1 board game design gaps (G-025–G-033) remain unstarted and block BG compilation stages.


---

session_id: 2026-03-29T_PHASE0_INFRASTRUCTURE
phase: Phase 0 (Infrastructure) — steps 0.1–0.18 complete
status: CLOSED — user actions 0.19–0.22 pending
---

session_id: 2026-03-29T_COMBAT_SIMULATION
phase: Combat System Design — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Full combat system redesigned and simulated from scratch
- Binary weapon system confirmed: Light/Heavy × Cut/Blunt × Short/Long
- TN gradient: LightCut 5/6, HeavyCut+LightBlunt 6/7, HeavyBlunt 7/8
- Versatile weapon category removed
- Establish Distance: TN7 vs opponent offence successes; auto-succeeds if opponent not attacking
- Feint vs Establish Distance: direct contest (feint TN-1 vs TN7), tie goes to feint
- Initiative: structural (correct range) > hit-and-not-hit > Agi Ob2 roll
- Disarm: offence vs defence; retrieve on TN7 vs opponent offence successes
- Stamina system: OOB + Full Guard both give opponent +2D
- Critical hits: excess >= 3, weapon modifier doubled
- Mass mismatch penalty: -1 defensive success when Light splits vs Heavy (not Full Guard, not Long-at-Close)
- Wound system: Variant B selected — HP=End (flat), armour=DR per weapon type
- DR table: varies by weapon type vs armour tier (LightCut/HeavyCut/LightBlunt/HeavyBlunt)
- Long weapons at Close zone: -1D offence, half damage, type unchanged
- Group combat: zone collapse (first closer opens zone for allies) + Fibonacci bonus
- Historical manual analysis: Fiore, Silver, Liechtenauer, Talhoffer, Meyer
- Simulation: 400+ matchups, 2000 fights each, randomised character parameters
- Key finding: offence% has near-zero correlation with winning (r≈0.01)
- Heavy weapons confirmed as situationally powerful — correct in armoured and group contexts

### Files pushed
- compilation/valoria_combat.docx — complete combat system write-up

### Simulation files (local /home/claude/)
- combat_v6.py through combat_v11.py — progressive rule iterations
- combat_v8_matrix.py — full weapon×armour matrix

### Key decisions
- No versatile weapons
- No medium weapon category
- Cut/Blunt as primary damage type axis (not weight alone)
- STR stays in damage formula
- No bind mechanic (too granular)
- No cutting/blunt TN split beyond weight
- Puncture not a separate axis
- Heavy weapons situationally powerful, not generally dominant

### Resume instruction
Combat system complete and compiled. Next: group combat simulation (Fibonacci + zone
collapse together), then push combat mechanics into main compilation checkpoint.
Pending user actions 0.19-0.22 from Phase 0 still outstanding.

---

session_id: 2026-03-29T_COMBAT_GROUP_SIM
phase: Combat Group Simulation — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Group combat simulation: Fibonacci + zone collapse (sim_combat_group.py)
- Rescue / multi-engagement simulation (sim_combat_rescue.py)
- Tie Up / bind exhaustive proposition testing (sim_combat_tieup.py)
- Exhaustive group combat matrix (sim_combat_exhaustive.py)
- v11 single combat sim with mass mismatch penalty (sim_combat_v11.py)

### Key findings
- 3v1 universally decisive (99-100%) regardless of weapon/armour
- 2v1 is the tactically interesting zone — weapon type and armour matter
- LightCut vs Heavy armour at 2v1: only 56% attacker win (contested)
- HeavyBlunt is correct weapon for armoured targets at any numerical parity
- 3v2 produces 40-87% draw rate — parallel engagements resolve simultaneously
- Survival/rescue window: 2-3 rounds (after round 3, 75-80% of losers have fallen)
- HeavyCut dominates 1v1 (75% vs LightCut); HeavyBlunt is armoured specialist
- Tie Up mechanic not needed — Option A accepted (system correct without it)
- Mass battle abstraction confirmed: Fibonacci → flanking modifier,
  zone collapse → formation break, rescue → reserve timing,
  weapon type → unit specialisation, DR → unit armour rating

### Files pushed
- tests/sim_combat_group.py
- tests/sim_combat_rescue.py
- tests/sim_combat_tieup.py
- tests/sim_combat_exhaustive.py
- tests/sim_combat_v11.py
- compilation/valoria_combat.docx (previous session)

### Design notes logged
- Mass battle abstraction: 5 unit stats + 2 rolls per engagement
- Heavy armoured elite unit holds 2v1 vs wrong weapon type (56%)
- Requires 3v1 or correct weapon (HeavyBlunt) to break reliably
- Reserve timing critical: 2 battle turns = rescue window

### Resume instruction
Combat system fully simulated and validated. Next:
- Integrate group combat mechanics into valoria_combat.docx
- Design mass battle unit stat block (weapon type, armour tier,
  pool/cohesion, DR, Fibonacci modifier)
- Phase 0 user actions 0.19-0.22 still pending

---

session_id: pending
phase: pending
status: OPEN

## RESUME FROM
See session_log_archive.md — last block: 2026-03-29T_COMBAT_GROUP_SIM

## NEXT ACTIONS
1. Integrate group combat into valoria_combat.docx
2. Design mass battle unit stat block (5 stats + 2 rolls)
3. Phase 0 user actions 0.19-0.22 still pending


---

```yaml
session_close: 2026-03-29
checkpoint: Thread Operation Catalog expanded
completed:
  - "stage15_spell_catalog.md expanded (24 → ~95 operations, 72 → 464 lines)"
  - "Coverage added: combat, mass combat, debate, faction actions, siege, collective ops, board game orders, Southernmost, monstrous entities"
  - "Mending operations: 0 → 8 entries"
  - "Past-Oriented Pulling: 1 → 6 entries"
  - "TS Mastery Bonus rule: +1 per 20 TS above min, cap +3, TS 100 uncapped (+2 additional = +5 at Object/Personal)"
  - "TS minimums corrected to Stage 3 authoritative values (30/50/70)"
  - "Canon compliance verified P-01 through P-14"
  - "Pushed to GitHub: commit 78d5597dcc48"
new_rules:
  - "TS Mastery Bonus (universal rule, catalog header)"
editorial_pending:
  - "PO-06: The Great Unwinding (campaign-endpoint Past-Oriented Pulling)"
  - "CO-04: The Great Working (campaign-endpoint collective operation)"
  - "W-42: Crowd Coherence in Debates (Thread manipulation of audience)"
  - "W-51: Mandate Reinforcement via Weaving (political power balance)"
  - "FR-L-05: Locked Institution chronic severity (-2/season)"
  - "W-06c: Mode 3 conventional Dissolution immunity"
next_action:
  - "Integrate TS Mastery Bonus into stage3_thread_operations.md"
  - "Stress test Mastery Bonus at TS 100 across operation types"
  - "Resolve 6 editorial flags"
```
---
session_id: pending
phase: pending
status: OPEN

## RESUME FROM
See session_log_archive.md — last block: 2026-03-29T_COMBAT_GROUP_SIM

## NEXT ACTIONS
1. Mass combat unit stat block — specific values (pool sizes, cohesion thresholds,
   morale mechanics) flagged [EDITORIAL] in stage8_combat.md §8.9
2. Phase 0 user actions 0.19-0.22 still pending
3. Integrate remaining gap register items per workplan


---

session_id: 2026-03-29T_THREADWEAVING_COMBAT_SIM
phase: Threadweaving × Combat Simulation
status: CLOSED

## SESSION SUMMARY

### Completed
- Stress test matrix v2 reconstructed: 35 cells, 6 clusters (A–F)
- Comprehensive simulation: 31 cells tested, 13 P1, 13 P2, 5 P3 findings
- Extreme stress tests: 18 break attempts, 12 P1, dominant strategies identified
- Narrative stress tests: 4 multi-system scenarios (debate→combat→thread→faction)
- 23 patches drafted (PP-131–153), reviewed for conflicts (zero found), committed
- 6 gap resolutions (GP-01–06) resolving all threadweaving×combat blocking gaps
- 5 edge case rulings formalized
- Wound system redesigned (PP-131): continuous HP track, -1D/wound, carryover damage
- E-06 editorial ruling (Personal Lock in combat) fully integrated

### Key design findings
- Personal Pull is dominant combat Thread operation (0 Coherence, -2D, scene duration)
- Personal Dissolution is 70% assassination at optimized stats (no resistance roll)
- Practitioners dominate every system they touch; cost is world-state degradation (RS, TC, Coherence)
- Rock-paper-scissors confirmed: practitioners beat structures, fighters beat unprotected practitioners, Church politics beat practitioners' long-term interests
- Thread operations during Debates are powerful and nearly undetectable
- Contact windows carry across system transitions (Debate→Combat) seamlessly

### Files pushed
- valoria_patch_proposals.md (PP-131–153 + GP-01–06 appended)
- tests/sim_thread_combat_matrix_v2.md
- tests/sim_thread_combat_comprehensive.md
- tests/sim_thread_combat_extreme.md
- tests/sim_thread_combat_narrative.md

### Editorial pending (8 items)
1. Personal Pull balance (0 Coherence, -2D, scene duration)
2. Personal Dissolution lethality (resistance roll?)
3. Heal loop mitigation (Overweave acceleration)
4. Pull stacking floor (half base pool?)
5. Mass Lock RS drain cap
6. Weaving effect on Debates (+2D or +1D)
7. Structural Pulling vs Fortification resistance
8. Catastrophic TC surge Accounting bypass

### Resume instruction
Read session_log_current.md. 8 editorial decisions block further simulation. PP-131 invalidates all prior combat sim data — re-simulation needed after editorial resolution. Opus-tier work (E-05, E-06 downstream, F-06) deferred until editorial on items 1-2.

---

session_id: 2026-03-30T_GM_REF_P1
phase: open
status: PHASE_1_COMPLETE

## SESSION SUMMARY
GM Reference Suite Phase 1 complete. 10 mechanical deliverables committed to gm_ref/.

## FILES COMMITTED
- gm_ref/gm_reference_workplan.md — full workplan
- gm_ref/d01_cascade_consequence_reference.md — clock thresholds + cross-effects
- gm_ref/d02_seasonal_accounting_form.md — offline accounting worksheet
- gm_ref/d03_gm_dashboard.md — live state reference
- gm_ref/d04_gap_escalation_table.md — Gap age → Mend Ob + severity tables
- gm_ref/d05_coherence_band_track.md — band penalties + fallout tables
- gm_ref/d06_thread_operation_resolution_card.md — operation procedure + co-movement mechanical layer
- gm_ref/d07_npc_state_cards.md — 9 principal NPCs with clocks, Beliefs, triggers
- gm_ref/d08_knot_registry_template.md — per-practitioner Knot tracking form
- gm_ref/d09_comovement_matrix_skeleton.md — 18-cell matrix skeleton (Opus fill pending)
- gm_ref/d10_framing_process_skeleton.md — 4-step improvisation process (Opus fill pending)

## NEXT ACTION
Phase 2 — Opus tasks (4 artifacts, sequential):
1. D-11: Fill co-movement matrix narrative cells (d09 skeleton → complete)
2. D-12: Fill framing process philosophical content (d10 skeleton → complete)
3. D-13: Write 8–12 annotated examples (split-register format)
4. D-14: Write 4–6 counter-examples

Phase 2 requires user to initiate each Opus artifact. Tasks 1+2 can run in parallel.
Phase 3: assemble complete suite after all Phase 2 outputs approved.

## OPEN ITEMS
- D-07 NPC state cards: faction stat values left as blanks (fill from live Dashboard)
- D-09/D-10: all [OPUS] sections are explicit placeholders, clearly marked
- Solmund rename (Solmund→Solmund) not yet applied to new gm_ref files — apply at Phase 3 assembly

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_LIR_FF_BG_DESIGN
phase: Phase 14 — LIR/FF design + BG Fail Forward + comparative simulation
status: COMPLETE

completed:
  - Confirmed existing glossary.md (built prior session) — no rebuild needed.
  - Resolved all 5 LIR/FF editorial items (ED-085 through ED-089, PROVISIONAL).
  - Designed BG Fail Forward system: PP-177 (Partial = Minor complication, player choice; Failure = Moderate, mandatory; Severe tier for Ob>=4).
  - Designed cross-mode LIR/FF applicability note: PP-178.
  - Designed Hybrid zoom-boundary FF rule: PP-180.
  - SIM-FF-01: 4-season comparative simulation (Run A no FF vs Run B with FF).
  - Verdict: FF produces significantly richer emergent gameplay. Run B generated 2 new inter-faction tensions, PI change, Stability change vs zero state changes from 5 Failures in Run A.
  - PP-177, PP-178, PP-180 applied to params_board_game.md.
  - PP-177 added to params_board_game_history.md.
  - Patches PP-177/178/180 added to patch_register.yaml.
  - ED-085 through ED-089 added to editorial_ledger.yaml.
  - Simulation SIM-FF-01 committed to tests/sim_bg_ff_01.md.
  - tests/coverage_matrix.md updated.

key_design_decisions:
  PP-177: Fail Forward BG operationalisation — Partial = Minor complication (player choice: Standing -1 or PI +1). Failure = Moderate (action-type specific, mandatory). All Domain Actions covered. Battle excluded.
  PP-178: LIR/FF cross-mode note — Debate exempt from LIR; Thread irreversibility governs over LIR; BG action-economy = LIR-equivalent.
  PP-180: Hybrid zoom-boundary FF — personal complication carries to faction scale.
  ED-085: Govern Success/Partial/Overwhelming distinction confirmed (Provisional).
  ED-086: Domain Action Overwhelming = Success effect only unless stated otherwise (Provisional).
  ED-087: Parliamentary Manoeuvre Partial — PP-170 "no effect" preserved as Minor choice option.
  ED-088: Debate exempt from LIR — confirmed.
  ED-089: Thread irreversibility governs over LIR — confirmed.

flags_for_user_review:
  - ED-085: Confirm Govern Partial = Prosperity +1 (with Minor complication)
  - ED-086: Confirm Domain Action Overwhelming = Success effect only (no bonus)
  - ED-087: Confirm Parliamentary Manoeuvre Partial = Minor complication (with "no effect" as choice)

open_design_gaps_from_sim:
  - GAP BG-FF-01: Govern Partial base effect — resolved via ED-085 (Provisional)
  - GAP BG-FF-02: Domain Action Overwhelming bonus — resolved via ED-086 (Provisional)

next_recommended:
  - Compile updated BG Domain Action reference card incorporating FF complication column
  - Simulate 12-season game with FF to assess long-run compounding
  - User review of ED-085, ED-086, ED-087 to confirm or adjust
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-03T_WORLDBUILDING_V3_CANON_AUDIT
phase: CANON AUDIT COMPLETE
status: AWAITING EDITORIAL REVIEW

## CANON AUDIT OF WORLDBUILDING v3
- 0 canon violations (P-01 through P-15 all pass)
- 3 editorial items can be closed immediately (ED-NEW-02, ED-NEW-03, ED-NEW-04) — canonical sources already answer them
- 5 pre-existing repo inconsistencies discovered (Reach/Influence stale name, Baralta TC threshold, Piety undefined, territory numbering, ED-007 misleading status)
- 1 new content flag (Almaic Kyriakos has no canonical basis — lore-only)
- Jarnstal Counter is a valid new formalisation of stage13 narrative

## ITEMS TO CLOSE
- ED-NEW-02: Magnus Vaynard (canonical timeline governs)
- ED-NEW-03: Inge Baralta (all canonical docs use Inge)
- ED-NEW-04: Confessor = personal title, Holy See = office (both canonical)

## PRE-EXISTING INCONSISTENCIES FOUND
1. Stage13 uses "Reach" instead of "Influence" (stale stat name)
2. Baralta TC suppression: stage6 says Mandate 4+, stage13 says above 5
3. "Piety" referenced in stage13 — undefined mechanic
4. Territory numbering conflict between stage7 and PP-199
5. ED-007 status "resolved" but no fourth Cardinal was created

## Gate: PASS

next_session_start:
  priority_1: "User reviews v3 + canon audit. Approves/rejects editorial items."
  priority_2: "Close ED-NEW-02, ED-NEW-03, ED-NEW-04."
  priority_3: "Fix pre-existing inconsistencies (Reach→Influence, Baralta threshold, Piety→Mandate)."
  priority_4: "On approval: propagate v3 mechanics to stage6, stage13, params."
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-03T_TOKEN_EFFICIENCY_REVIEW
phase: CLOSED
status: CLOSED

completed:
  - Reviewed past week of sessions via recent_chats (20 sessions)
  - Identified bootstrap retry waste as primary fixable inefficiency
  - Applied 3 fixes to skills/valoria-orchestrator/SKILL.md:
    - Anti-pattern #7: bootstrap without python3 heredoc wrapper
    - Session Start Step 1: curl replaced with read_files_graphql
    - Task Routing Step 3: curl replaced with read_files_graphql
  - Noted: token % by session unavailable — claude.ai API returns content only, no usage metrics

commits:
  - 9f692c5: anti-pattern #7 + curl->graphql in task routing
  - e834847: curl->graphql in session start step 1

unfixable_by_file_edits:
  - Session consolidation (user behaviour)
  - Batch ops as scripts vs inline (execution-time judgment)

next_session_start:
  priority_1: "Resume from prior session priorities — see previous log."
  note: "No open blockers introduced this session."
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-06T_SONNET_REVIEW_1
phase: SESSION IN PROGRESS
status: TASKS 1-3 COMPLETE — PENDING COMMIT
last_commit: 732d4f6

## TASKS COMPLETED THIS SESSION
1. Full-spectrum review of victory_architecture_v1.md — 21 flags identified
2. params_board_game.md propagation:
   - §Victory Conditions replaced with pointer to victory_architecture_v1.md
   - §Hollow Victory Deed table struck (P-32 narrative qualifier applies)
   - §Co-Victory Pairings updated to conditions-based language
   - Accounting Step 12 rewritten (Deed Tokens → 2-consecutive-Accounting check)
   - TC 80 → TC 75 throughout (PP-421, FLAG-5 resolved)
   - §TC Starting Value stale paragraph fixed (was contradicting itself)
   - Formal Crown Treaty added to Ob Reference table (PP-423)
   - Warden Cooperation bonus effects added (PP-426)
   - Prominence mechanic defined (PP-417)
   - Warden Recognition (WR) track added (PP-425)
3. state_transfer_spec.md updates:
   - TC Win-Delay Rule replaced by Victory Condition Check — Hybrid (PP-420)
   - CV row added to Variables that TRANSFER table (PP-419)
   - CV Domain Echo added to Zoom Out table (PP-419)
4. victory_architecture_v1.md v3:
   - All territory T-numbers remapped to PP-199 (PP-408, FLAG-15)
   - Crown TCV threshold 18→16 (PP-409, gap restored to +6)
   - TC 75 confirmed canonical throughout
   - CV action cap clarified (PP-416)
   - Church Seizure: Prominence mechanic added, AEA territory corrected to T14
   - RM RS threshold confirmed ≥ 40 (PP-415)
   - Varfell Path B provisional (ED-311 flagged for user review)
5. ED-311 filed: Varfell Path B redesign — 3 options prepared for user review
6. PP-408 through PP-426 registered

## USER DECISIONS MADE THIS SESSION
- TC threshold: TC 75 canonical (FLAG-5 / ED-NNN-A resolved)
- CV cap: consequences not cap-governed (FLAG-4 resolved)
- Varfell B: reduce conditions — ED-311 document prepared, awaiting choice of option A/B/C
- RM RS ≥ 40: confirmed canonical

## REMAINING WORK
Priority 1:
  - ED-311: User must choose Varfell Path B option (A/B/C) from varfell_path_b_redesign_ed311.md
  - params_board_game propagation: §Starting Values TC note still says "TC 80 = Territorial Seizure" (fixed in this session to TC 75 — verify in commit)

Priority 2 (from prior session, unchanged):
  - SIM-DEBT: Full faction-AI simulation of TCV balance (Monte Carlo validated thresholds but not multi-faction interaction)
  - SIM-DEBT: TC pacing simulation (analytical estimate ~S18 to TC 75)
  - SIM-DEBT: Community Weaving feedback loop (CV + RS dual effect)
  - ED-080/081: Baralta and Vaynard BG Conviction text
  - ED-308: Varfell succession
  - ED-309: Baralta succession
  - ED-298/299: Resentment token + coalition enumeration — propagation pending
  - ED-300/301: Domain Echo + TS/Coherence orthogonality — propagation pending

Priority 3:
  - BALANCE-002/003/005: P2 monitoring items
  - Remaining Galbados→Solmund corrections in ~40 non-canonical files
  - SIM-DEBT-01: Contest recalibration with (Presence×2)+History

## KEY FILES MODIFIED THIS SESSION
  designs/board_game/victory_architecture_v1.md (v3 — territory renumbering, TC 75, CV cap)
  designs/board_game/varfell_path_b_redesign_ed311.md (NEW — for user review)
  references/params_board_game.md (Victory Conditions, Hollow Victory, Co-Victory, Step 12, TC 75, Prominence, WR track, WC effects, Treaty Ob)
  skills/valoria-orchestrator/references/state_transfer_spec.md (TC Win-Delay Rule replaced, CV transfer added)
  canon/editorial_ledger.yaml (ED-311 added)
  canon/patch_register.yaml (PP-408 through PP-426 added)
```

---

# Valoria Session Log — Current

```yaml
session_id: 2026-04-13_SONNET_UNVERIFIED_RESOLUTION
session_close: 2026-04-13
phase: COMPLETE
status: CLOSED

## TASKS COMPLETED THIS SESSION
1. Resolved all 11 [UNVERIFIED] items (U-01 through U-11) against fetched sources
2. Rebuilt arcs 47, 51, 55 from scratch (broken causal chains)
3. Corrected arcs 48, 49, 54 (threshold refs, WC Ob removal, reframing)
4. Confirmed arcs 46, 50, 52, 53 with minor corrections
5. Committed fully resolved canonical doc: arcs_46_55_resolved.md

## RESOLUTION FINDINGS (critical)
U-01: Elske Loyalty has NO Coup Counter link. Correct triggers (stage6 §8.9): TC ≥ 40 unopposed,
      Torben Loyalty ≤ 2-3, Crown loses 2+ territories without military response.
      Coup Counter ceiling = 3 (stage6), fires at 3. Arc 47 rebuilt.
U-02: RS thresholds confirmed: Strained 79-60, Fragile 59-40, Fractured 39-20, Critical 19-1.
      No thresholds at 50 or 40. RS 60 = already Strained at campaign start.
U-03: Coherence thresholds do not broadcast wrongness to non-practitioners.
      Close Knots sense wrongness at Coherence 7-5 (Dissonant). Non-practitioners
      observe via Thread Sensitivity perception table (TS 10-29 = vague unease), not Coherence.
U-04: WC confirmed effects: +1D Thread ops (WC≥1), RS decay halved (WC≥2), RS +2/season (WC 3).
      NO Domain Action Ob reduction. Arc 49 rebuilt without WC Ob claim.
U-05: Experience at Focus 1 carries ZERO Coherence cost (§3.2 confirmed). Arc 51 rebuilt:
      no Coherence decay from Experience. New mechanism: perceptual gap without recovery pressure.
U-06: P-01 co-movement requires an operation. Experience = no operation = P-01 not triggered.
U-07: PI per-action amounts not specified in any source. Design gap surfaced.
U-08: Domain Action pool confirmed: personal roll + faction stat bonus dice if holding leadership.
      Wound penalty propagates to personal pool → Arc 53 mechanically confirmed.
U-09: No named "Read Intel" Domain Action. Varfell Private Collection (Intel vs Ob 2) is canonical
      mechanic. Standard Domain Action rules cover general Intel-based observation.
U-10: Guild Favour moves ONLY on Guild Economic Leverage Failure (-1 in territory).
      Crown/Church Domain Actions do NOT trigger Guild Favour changes. Arc 55 rebuilt.
U-11: No named Guild ethical framework in fetched sources. "Mercantile efficiency" was invented.

## ARCS REBUILT (causal chains replaced)
Arc 47: Correct Coup Counter triggers substituted for fabricated Elske link
Arc 51: Rebuilt around perceptual gap and forcing event (not Coherence decay from Experience)
Arc 55: Rebuilt around confirmed Guild Favour trigger (Leverage Failure only, not Crown/Church actions)

## DESIGN GAPS SURFACED FOR JORDAN
1. PI per-action contribution table not specified anywhere
2. Guild Favour restoration mechanic not documented

## COMMITS THIS SESSION
SHA 0d6f2ba: arcs_46_50_batch07.md (original)
SHA cf47ede: arcs_51_55_batch08.md (original)
SHA 75fd3bb: arcs_46_55_consolidated.md (post-critique)
SHA 88e9a72: session log (post-critique)
[THIS COMMIT]: arcs_46_55_resolved.md (canonical — fully resolved)

## P1 BLOCKERS: 0
## OPEN PROVISIONAL: PP-571 (Hafenmark Stability gate — Jordan review pending)
## OPEN DESIGN GAPS: 2 (PI per-action table, Guild Favour restoration)

## RESUME INSTRUCTION
Next session: invoke orchestrator per normal protocol.
All arcs 46-55 are now mechanically clean and canon-compliant.
Outstanding: Design gap decisions on PI per-action amounts and Guild Favour restoration.
```

---

session_id: test
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: done
next_action: confirm
blockers: []

---

session_id: peninsular_strain_v1
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

session_id: peninsular_strain_propagation
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

session_id: faction_stability_military_tc_redesign
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: sim_validated_20_20_tests
next_action:
  skill: confirm_with_jordan
design_docs_produced:
  - faction_layer_v30.md
  - faction_layer_v30_infill.md
  - military_layer_v30.md
  - tc_political_redesign_v30.md
sim_file: /home/claude/valoria_sim.py
sim_tests: 20/20_passing
sim_results_bg: TC_THEOCRACY_53pct CROWN_TREATY_14pct TIMEOUT_32pct avg_13.3y
sim_results_hybrid: TC_THEOCRACY_45pct CROWN_TREATY_16pct TIMEOUT_39pct avg_14.5y
crown_collapse_rate: 3.4pct
hafenmark_collapse_rate: 27.8pct
patches_proposed:
  - PP_402_REPEALED
  - PP_403_REPEALED_except_Suppress_exception
  - TC_runs_0_to_100_no_freeze
  - unit_cap_Military_times_2_plus_3
  - BG_battle_pool_sum_Martial_plus_commander_bonus
  - Spiritual_Weight_per_territory
  - Conditional_TC_passive
  - Church_TC_political_legitimacy_bonus
gaps_next_session:
  - territory_Prosperity_not_seeded
  - Lowenritter_post_coup_AI
  - Varfell_VTM_path
  - Parish_Cathedral_upgrades
  - Hafenmark_RDT_TD_tracks
  - ED_NEW_TC_10_church_victory_threshold
  - ED_NEW_TC_11_seizure_ob_post_milestone
  - all_docs_pending_PP_numbers
blockers: []

---

session_id: peninsular_strain_integration
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

session_id: peninsular_strain_full_propagation
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

session_id: peninsular_strain_harmonization
session_close: 2026-04-15
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

session_id: peninsular_strain_cross_session_integration
session_close: 2026-04-15
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

---

# Valoria Session Log — Current

session_id: holistic_audit_2026-04-15
session_close: 2026-04-15
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []

## TASKS THIS SESSION
1. Unzipped 4 archives, inventoried 30+ extracted files + 15 uploaded docs
2. Pulled all v30 design docs, params files, registers, canon constraints from GitHub
3. Reviewed editorial ledger (ED-535:542), patch register (271 active, 326 archived)
4. Cursory review of 20+ conversations over 9 days (April 6-15)
5. Holistic audit (486 lines) — 15 sections covering metaphysics, formula consistency, faction balance, NPC completeness, calibration, all systems
6. Clock registry staleness report — 23 stale items across 6 categories
7. Systems workplan (665 lines) — skeleton/infill strategy, file index, audit structure for all 18 systems
8. Interactive interdependency matrix (18x18, 5 interaction types, 6 compound chains)
9. RSE critique (robustness/smoothness/elegance) of all 18 systems
10. ED-543:547 registered (clock stale P1, P-03 model P2, Zoom In P1, RM actor P2, fieldwork cost P3)

## COMMITS
- f4b6feed: designs/audit/valoria_holistic_audit.md, valoria_systems_workplan.md, clock_registry_staleness_report.md, editorial_ledger ED-543:547
- 1e4713e3: designs/audit/valoria_rse_critique.md
- this commit: session close

## KEY FINDINGS
- 7 systems complete (Core, Combat, Thread, Victory, Geography, Calamity, Character)
- 3 systems need targeted fixes: Social Contests, Fieldwork, Clocks
- 3 systems need significant work: Scale Transitions (P1), Mass Combat, Faction Layer UI
- clock_registry_v30.md is most urgently stale file (23 items)
- Only 5 Zoom In triggers for 120+ arcs — #1 videogame design gap
- PP-632 and Accord gate are the two design quality benchmarks
- Interactive matrix widget should NOT go in Project Files (4K tokens per message); store in repo tools/

## NEXT SESSION PRIORITIES
1. Resolve J-7 (0-4 territory scale), J-8 (CI milestones), J-9 (Spiritual Weight)
2. Update clock_registry_v30.md (17 safe changes from staleness report)
3. Run ED-538 and ED-539 compound simulations
4. Write 20-30 Zoom In triggers for videogame (ED-545)

## ADDITIONAL COMMIT
- designs/audit/valoria_how_to_play.md — complete campaign guide

## ADDITIONAL COMMIT 2
- designs/systems/player_agency_v30.md — Beliefs, Duties, Scene Slate, Stature Progression

## SESSION: 2026-04-16 (player-world bridge)

### TASKS COMPLETED
1. File reorganization: 14 loose files renamed/moved, 3 duplicates deleted (ffe51d6)
2. Player-world bridge overview: 326 lines, 11 systems audited, rated W→P and P→W (d6fc20e)
3. Bridge Part 1 revision package: Renown track, mechanical Scene Slate, companion specification, 22-item implementation sequence

### COMMITS
- ffe51d6: [editorial] file reorganization
- d6fc20e: [editorial] player-world bridge overview
- this commit: Part 1 revision package (Renown + Scene Slate + Companions)

### NEXT SESSION PRIORITIES (ordered)
1. Apply Part 1 revisions to player_agency_v30.md (rename Beliefs→Convictions, add Renown §5.4, replace §4.2)
2. Create companion_specification_v30.md as new canonical file
3. Priorities 3-5 from bridge overview: NPC Outreach, mandatory Zoom In, fieldwork extensions
4. Priorities 6-8: Obligations, Scar visibility, Accord pathways, combat bridge
5. Priorities 9-10: CV presentation, mass combat aftermath
6. Holistic W→P / P→W review of all revised documents
### ADDITIONAL COMMITS (same session)
- player_agency_v30.md revised: Beliefs→Convictions rename, mechanical Scene Slate (7-step algorithm), NPC Outreach generation, opportunity resolution table, §5.4 Renown Track (0-10), Conviction symmetry with NPC system
- companion_specification_v30.md created: formation, departure, scene participation, combat/contest/fieldwork/Thread integration, Domain Echo threshold modification, faction feedback loop, arc integration
- canonical_sources.yaml updated with companion_specification entry
### BRIDGE PRIORITIES 3-4 APPLIED
- scale_transitions_v30.md: §4.3 extended with 6 mandatory Zoom In triggers, 5 world-state triggers, §4.4 Where Were You retrospective scenes, §7 Sufficient Scope extended
- npc_behavior_v30.md: §8.11 NPC Personal Outreach Generation — outreach/demand conditions, scene structure, volume control
### BRIDGE PRIORITIES 5-6-8 APPLIED
- fieldwork_v30.md: Investigation Synthesis via Reconstruct (4-degree completion mechanic), §5.9 NPC-Initiated Social Engagement (outreach/demand scene rules)
- social_contest_v30.md: §6.1 Obligations (binding post-contest commitments with violation consequences), §6.2 Conviction Scar Visibility, §6.3 Chain Contests (compromise→follow-up, max 3 chains)
- combat_v30.md: §13 Combat World Bridge — Domain Echo on named NPC combat, Combat Reputation cascade (0-6+ scale), Death Cascade (5-step consequence chain)
### BRIDGE PRIORITIES 7-9-10 APPLIED
- peninsular_strain_v1.md: §2.7 personal-scale Accord pathways (6 player actions → Accord change), §2.8 Accord environmental legibility (4-level description table)
- conviction_track_v30.md: §11 CV presentation layer — CV change environmental events, Church AP player-facing indicators (5-level table), TC milestone presentation (4 thresholds)
- mass_battle_v30.md: PART D mass combat world bridge — §D.1 post-battle consequence scenes (3 choices), §D.2 named unit officers (profile, disposition, death rules), §D.3 player morale effect

ALL 10 BRIDGE PRIORITIES NOW APPLIED. Next: holistic W→P / P→W review.
### HOLISTIC REVIEW COMPLETE
- All 10 bridge priorities applied across 7 commits
- Holistic W→P / P→W review: 0 systems Weak on either axis (was 4 Weak W→P, 4 Weak P→W)
- 600 lines added to 10 files. No new mechanical vocabulary introduced.
- 7 remaining gaps identified (all P2-P3)
- Bridge architecture: Scene Slate (W→P) + Domain Echo (P→W) + Companions (emotional) + Obligations (temporal) + Environmental legibility (ambient)

last_stage: done
next_action:
  skill: confirm with Jordan
### SETTLEMENT LAYER SPECIFICATION
- 36 settlements across 17 provinces (Seat, City, Town, Fortress, Port, Cathedral, Mine, Outpost)
- Dual-authority governance: Provincial Authority + Settlement Governor
- Subnational faction management (Church cathedrals, Guild markets, Löwenritter fortresses, RM outposts, Warden posts)
- Player progression: Settlement Governor (Renown 3) → Multi-Settlement (5) → Provincial Authority (7) → National Actor (9)
- Faction emergence (local→national in 5 stages) and collapse (national→city-state→dissolution)
- Military granularity: Assault/Siege/Bypass at settlement level, Fortress chokepoints
- Extended timeline: IP halved, Generational Shift clock (age penalties at Year 10/20/30), cross-generational play
- Province Accord derived from settlement Order averages
- 9 open editorial items (ED-SETT-01 through 09)
- 14-file propagation map
### SETTLEMENT-BRIDGE UNIFICATION
- 15 conflicts identified and resolved between settlement layer and bridge revisions
- 8 editorial items resolved (ED-SETT-03/05/06/07/08/09, ED-COMP-04, ED-SETT-10)
- Unified 3-layer architecture: World Physics (strategic) ↔ Settlement Physics (institutional) ↔ Player Physics (personal)
- 10-file revision spec produced
- Mutual constitution principle: every action at every scale produces consequences at the other two scales

last_stage: done
next_action:
  skill: confirm with Jordan

---

session_id: sim_batch_4_2026-04-16
session_close: 2026-04-16
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []
resolutions_this_session:
  - ED-585: Church victory condition revised — TC ≥ 65 + Accord ≥ 3 in ≥ 3 non-capital territories confirmed
  - ST-11: Fieldwork stress test — Structural investigation 4 scenes, correct pacing
  - ST-12: Thread edge cases — Lock reversal trivial for low-TS Locks; Pull vs Dissolve undocumented
  - ST-13: Varfell three paths validated — Path B < A < C timeline, soft deadline at TC 80
  - ST-14: RM arc — Phase 1 correct; Phase 2 critical gap (PT ≤ 1 holding condition unreachable)
  - ST-15: Löwenritter coup sequence — 7 cascading consequences all correct
  - ST-16: Strain 7-10 — Crisis band mass Revolt cascade; Collapse bans Church victory
  - ST-17: Dissolution/Lock cascade — net RS −6 from 3-Lock episode, correctly irreversible
  - ST-18: Companion departure arc — 3 Scars in 4 seasons, appeal correct
  - ST-19: 30-season campaign — generational shifts handled by existing mechanics
  - ST-20: 5-system simultaneous — no conflicts
files_modified:
  - tests/sim_batch_4_2026-04-16.md (new)
  - canon/editorial_ledger.yaml (ED-588/589/590 added; resolved items archived)
  - tests/coverage_matrix.md (SIM4-01 through SIM4-09; confirmations)
open_items:
  - ED-542 Battle consequences propagation gap (P2)
  - ED-586 Arc behavioral state vs Priority 6 contradiction (P2)
  - ED-587 Stability Crisis Zoom In trigger (P2)
  - ED-588 RM Phase 2 holding condition PT ≤ 1 unreachable (P1) — NEW
  - ED-589 RM Presence marker mechanics undefined (P1) — NEW
  - ED-590 Apply Church victory revision to victory_v30 §3.2 (P1) — NEW
  - All P2 EDs from SIM4 batch

---

session_id: sim_companions_2026-04-16
session_close: 2026-04-16
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
blockers: []
resolutions_this_session:
  - SIM-COMP: campaign-length skeleton simulations for all 12 playable NPCs complete
files_modified:
  - tests/sim_companions_2026-04-16.md (new)
  - canon/editorial_ledger.yaml (ED-591 through ED-600 added; next_id: 601)
  - tests/coverage_matrix.md (SIM-C-01 through SIM-C-16; 8 confirmed; 4 SIM-COMP debt)
open_items:
  - ED-542 Battle consequences propagation gap (P2)
  - ED-586 Arc behavioral state vs Priority 6 contradiction (P2)
  - ED-587 Stability Crisis Zoom In trigger (P2)
  - ED-588 RM Phase 2 holding condition PT <= 1 unreachable (P1)
  - ED-589 RM Presence marker mechanics undefined (P1)
  - ED-590 Apply Church victory revision to victory_v30 §3.2 (P1)
  - ED-591 Torsvald §2 entry absent (P1) — NEW
  - ED-592 Arc profiles absent for Vossen, Hann, Torben, Ehrenwall, Maret Uln (P1) — NEW
  - ED-593 Almud companion BG faction effect undefined (P2) — NEW
  - ED-594 Torben companion + Coup Loyalty paradox (P2) — NEW
  - ED-595 Dual companion simultaneous Outreach unspecified (P2) — NEW
  - ED-596 Multi-source Knot strain stacking absent (P2) — NEW
  - ED-597 Edeyja Arc C RS drain rate unspecified (P2) — NEW
  - ED-598 §5.0b stable TS 30-49 exemption ambiguous (P3) — NEW
  - ED-599 Torben companion mechanical bonuses undocumented (P3) — NEW
  - ED-600 Officer companion rival-recruit counter-incentive unformalized (P3) — NEW
  - SIM-COMP-01 Arc profile sims for 5 companions (pending ED-592)
  - SIM-COMP-02 Multi-practitioner Knot strain stacking stress test
  - SIM-COMP-03 Companion departure rate calibration (validate ~75% S30)
  - SIM-COMP-04 Torsvald full sim (pending ED-591)
