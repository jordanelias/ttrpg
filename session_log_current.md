# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_BG_STALE_CORRECTION
phase: SESSION CLOSED
status: COMPLETE

## CRITICAL FINDING
User identified that factions were wrong: Guilds and Niflhel had been given player victory
conditions; they are NPC-only. I had not read v04 (canonical BG ruleset) before patching.

## STALE SCAN FINDINGS (tests/stale_scan_bg_01.md)
Full inventory of errors. Key items:
- Faction list: Guilds/Niflhel listed as playable (WRONG). Removal of their player VCs.
- TC starting value: 28 (params) → 22 (v04 canonical)
- PI starting value: 5 → 7
- Torben Loyalty start: 8 (my error) → 3, active from game start, no IP trigger
- Varfell Mandate: 4 → 3; Varfell Wealth: 4 → 3
- Elske: off-board card near T4 (not on board, not in params at all)
- Church primary victory: TC ≥ 70 (not 40 as PP-171 set)
- Church Deed 4: Control T1 (not "Crown Mandate ≤ 2" which PP-171 wrongly introduced)
- Crown: 5 deeds (not 4); Deed 4 = PI ≥ 5; Deed 5 = Torben Loyalty ≥ 5
- Varfell victories: 3 paths based on VTM+territories+stats (not Intel stat advancement)
- Phase 4 priority order: Intel→Military→Domain→Social→Thread→Unique→Project (not Thread first)
- TC 80 cap: 2 transfers/event (v04/v05 P-23), not 4 (PP-183 was too generous)

## PATCHES REVERTED OR CORRECTED
PP-171: Church Deed 4 REVERTED to Control T1; Church victory = TC≥70 all deeds
PP-172: Crown IP escape clause REVERTED; Crown has 5 deeds per v04
PP-173: Intel advancement REVERTED (no basis in v04; Varfell victories don't use Intel stat)
PP-176: Varfell Deed 1 Intel≥5 REVERTED
PP-183: TC80 cap corrected from 4 to 2 (v04/v05 P-23)
PP-186: Crown Deed 2 territories REVERTED to 4 (v04 correct)

## PP-188: COMPREHENSIVE CORRECTION
All corrections applied in single params rewrite. canonical_sources updated to v04 as authoritative.

## OPEN GAPS
ED-088 (P1): Ministry faction — user confirmed NPC but no design doc found anywhere.
Cannot design until source located or user provides spec.

## WHAT IS STILL VALID
PP-179: Overwhelming = 2×Ob ✓ (v05 confirms dice corrections)
PP-182: Co-Movement Protocol ✓ (design extension, not contradicted)
PP-181: AER, RDT, TD, VTM, Riskbreakers, Conviction texts ✓ (v04 confirms all)
PP-178: Trade Network Investment ✓ (novel design, not contradicted)
PP-177: Card-Hand system ✓ (v04 B3 uses it)
PP-180: Accounting reference steps, AP ceiling, Drawn battle, Policy Instrument ✓

## COMMITS
bd4232b: stale_scan_bg_01 report
0af61e52: PP-188 params correction (comprehensive rewrite)
2db16124: patch register + ED-088 + canonical_sources

## DESIGN-DEBT REMAINING
DESIGN-DEBT-BG-01: Reconcile all design docs into single canonical spec
DESIGN-DEBT-BG-03: Ministry faction NPC block (blocked on source)

## WHAT NEEDS TO HAPPEN NEXT
1. Resolve ED-088 (Ministry source) — user must provide.
2. Re-run balance analysis on correct faction set (Crown/Church/Hafenmark/Varfell only + Restoration as 5th).
3. Re-run simulations with correct starting values (TC=22, PI=7, Torben=3).
4. Verify Restoration Movement as full playable faction — are its mechanics player-grade?

next_session_start:
  priority_1: "User to identify Ministry faction source document or provide design brief."
  priority_2: "Re-run balance analysis BAL-BG-02 on correct faction set with correct starting values."
  priority_3: "Verify Restoration Movement player-grade mechanics (currently written as NPC default in v04 B5 — does it have sufficient player-facing complexity?)."
  priority_4: "TTRPG open items: ED-053 Composure, GAP-TTRPG-04 Belief CP, GAP-TTRPG-G1/G2."
```
