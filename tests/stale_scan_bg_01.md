# STALE MATERIAL SCAN — BG Params
## Date: 2026-04-02
## Trigger: User identified faction assignment errors; full scan ordered
## Source authority: designs/board_game/valoria_bg_v04.md (canonical BG ruleset)
## Secondary: designs/board_game/valoria_bg_v05_simulation_and_patches.md (corrections only)

## CRITICAL ERRORS

### Cat 1: Faction Assignments
WRONG in params: Guilds and Niflhel listed as playable with player victory conditions.
CORRECT (v04): Guilds = NPC only. Niflhel = NPC only.
CORRECT (v04): Playable = Crown, Church, Hafenmark, Varfell. Restoration Movement = optional 5th.
CORRECT (user): Ministry = NPC. Southernmost/Edeyja/Wardens = NPC conditional.
ACTION: Remove Guilds and Niflhel player victory conditions from params. Add Restoration Movement as full playable faction. Add Ministry as NPC (source doc needed).

### Cat 2: Starting Values
| Item | Params | v04 Correct |
|------|--------|-------------|
| TC start | 28 (P-32 patch) | 22 |
| Torben Loyalty start | 8 (my PG-09 error) | 3 (active from game start) |
| Torben Loyalty trigger | IP>30 activates clock | No such trigger — always active |
| PI start | 5 | 7 |
| Varfell Mandate | 4 | 3 |
| Elske | Not in params | Off-board card near T4, Loyalty 0-7 starts 4 |
| Church victory TC | 40 (PP-171 patch) | 70 (primary) |

### Cat 3: Church Victory (Critical patch error)
PP-171 changed Church Deed 4 from Control T1 to "Crown Mandate ≤ 2".
v04: Church Deed 4 = Control T1. Primary victory gate = TC ≥ 70.
PP-171 must be reverted. Church deeds must match v04.

### Cat 4: Crown Victory (Stale)
v04 Crown has 5 deeds (not 4). Deed 4 = PI ≥ 5. Deed 5 = Torben Loyalty ≥ 5.
PP-186 wrongly raised territorial requirement. Must revert.

### Cat 5: Varfell Victory (Wrong)
v04 Varfell paths: Intelligence Hegemony (VTM≥3, 3 territories, stats revealed), Southernmost Dominion (T12+T13, VTM≥3), Thread Supremacy (VTM=5, T12+T13+1 other, RS≥50).
My params had Intel stat-based deeds — these don't exist. Intel stat advancement (PP-173/176) was invented without canonical basis.

### Patches to Revert
PP-171: Church Deed 4 → REVERT to Control T1; TC≥70 primary victory
PP-172: Crown Deed 4 (IP escape clause) → REVERT; Crown has 5 deeds per v04
PP-173: Intel advancement → REVERT (no basis in v04)
PP-176: Varfell Deed 1 Intel≥5 → REVERT (no such deed in v04)
PP-186: Crown Deed 2 territories raised → REVERT to v04 spec (4 territories)

### Items Not in Params (Missing)
- Elske off-board card and Loyalty track (0-7, starts 4)
- Warden Emergence and Cooperation track (0-3)
- Löwenritter Coup Counter (0-4, threshold 4)
- Thread Resonance mechanics
- Patience Protocol (Varfell)
- Institutional Mandate triggers per faction
- Hollow Victory scoring
- Year-End accounting (4 seasons = Year-End; annual events)
- Ministry faction (NPC) — source doc not yet read
- Southernmost/Edeyja/Wardens NPC block (v04 B13 has it)
- Named Character Event deck
- Co-victory conditions

### TC 80 Sweep — Reconciliation Needed
v04/v05 P-23: "Hard cap: maximum 2 territory transfers per seizure event per faction"
My PP-183: cap at 4 territories/season (more generous)
v04 is authoritative — cap should be 2, not 4.

### Correct Items (no change needed)
- Dice system d10 ✓
- Ob minimum = 1 ✓
- Card-Hand system ✓
- AER starting value 2 ✓
- Conviction texts (Almud, Baralta, Vaynard) ✓
- Co-Movement Protocol PP-182 ✓ (design extension, not contradicted)
- RDT mechanics ✓
- Riskbreaker redesign from amendment2 — PARTIAL (v04 has different priority tree; needs reconciliation)
