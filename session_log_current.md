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
