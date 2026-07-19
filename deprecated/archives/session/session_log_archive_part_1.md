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

