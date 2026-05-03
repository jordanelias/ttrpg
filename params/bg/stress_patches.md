## BG Stress Test Patches (2026-04-08)
<!-- PATCHES APPLIED: PP-470-PP-475 -->


## Total TCV Correction (PP-470)
Canonical Total TCV = **29** (corrected from stated 30).
Recount: T1(5)+T2(1)+T3(2)+T4(1)+T5(1)+T6(1)+T7(1)+T8(4)+T9(3)+T10(2)+T11(1)+T12(3)+T13(1)+T14(2)+T15(0)+T17(1) = 29.
Total Domination (TCV >= 28) leaves 1 uncaptured TCV (any single TCV-1 territory).


## Restoration Senate Market Restriction (PP-471)
Restoration Movement may not purchase Legionary cards from Senate Market.
Military 0 makes Muster invalid (PP-039). Legionary cards are unplayable in hand.


## Piety Yield Dead Zone — Explicit Note (PP-473)
**Church-controlled territories produce zero Piety Yield.**
Church Prominence = Church L > controlling faction L. When Church controls a territory, Church IS the controlling faction. Church L > Church L = False = not Prominent = no Piety Yield.
Implication: Post-CI 75 seizure removes territories from Piety Yield pool. Plan accordingly.


## AER >= 3 and Parliamentary Challenge — Independence Clarification (PP-474)
AER >= 3 (PP-203) and Parliamentary Challenge (PP-431-COR) are independent:
- AER >= 3 bypasses Hafenmark Structural Suppression (passive -1/season from Baralta L >= 4).
- Parliamentary Challenge is a card action; fires when played regardless of AER.
- When AER >= 3 is active: structural is already negated; Challenge's "replaces structural" clause has no practical effect on structural. Challenge still fires and produces its degree-table CI result.


## Submission + PS 0 Ruling (PP-475 / audit Q1 ratification 2026-05-02)
If Submitting faction's halved PS = 0: **Submission supersedes Faction Collapse.** (Per audit Q1: submission is populist capitulation; institutional collapse is a separate Faction Collapse pathway.)
Submitted faction remains as vassal with PS 0. PS-0 effects apply (institutional L may persist; Submission is populist; Faction Collapse pathway via L 0 + Stability 0 separately tracked). Faction does not enter Faction Collapse (which requires Stability 0 at Accounting end per I-04/P-15, not L 0 or PS 0).


## Restoration Movement — Founding Mechanic (PP-478)
<!-- RM is NOT a playable faction in BG-only mode. -->
<!-- In Hybrid mode, RM emerges mid-campaign via Founding if conditions are met. -->

### RM Status by Mode
| Mode | RM Status |
|------|-----------|
| BG only | Not a playable faction. Presence markers are environmental tokens (GM/table). No player controls RM. No RM solo or co-victory. |
| Hybrid | Not present at game start. Emerges via Founding event. Once founded: playable by PC's controlling player (or GM if NPC-founded). |

### Popular Will (PW) Track
Range 0–5. Public track (placed near MS clock). Starts at 0. Belongs to no faction.

**Advances +1 when:**
- ≥ 2 territories simultaneously have PT ≤ 1 AND no Church Heresy Investigation is active in any of them (checked at Accounting).
- A PC performs a successful Community Organising or Community Weaving personal scene in a PT ≤ 1 territory (Zoom In result).

**Regresses −1 when:**
- Church executes a successful Heresy Investigation in a PT ≤ 1 territory.
- CI ≥ 60 at Accounting (while CI ≥ 60: PW regresses −1/season automatically).

Floor: 0. Ceiling: 5.

### Founding Trigger (all three at any Accounting, Hybrid mode only)
| Condition | Threshold |
|-----------|-----------|
| PW track | ≥ 3 |
| Territories with PT ≤ 1 | ≥ 3 |
| MS | ≤ 60 |

### Founding Procedure
Founding Agent declared (PC with communal Conviction, or named NPC at GM discretion).
Roll: Founding Agent's Influence vs Ob = CI ÷ 10 (round up, min 1, max 5).

| Degree | Starting Stats (L+PS seeded equal per PP-686 v2; flagged: RM is statless per PP-460, see TODO note below) | Presence Markers |
|--------|---------------|-----------------|
| Overwhelming | L 2, PS 2, Influence 3, Wealth 1, Military 0, Stability 4 | 3 markers in PT ≤ 1 territories |
| Success | L 1, PS 1, Influence 2, Wealth 1, Military 0, Stability 3 | 2 markers |
| Partial | PW +1. Not founded. Retry next Accounting. | — |
| Failure | PW −1. Church gets 1 free Heresy Investigation. Cannot retry until PW resets to ≥ 3. | — |

**Post-founding card hand:** 2× Praetor, 1× Pontifex, 1× Recess.
**NPC-founded RM AI priority:** PT reduction > Presence spreading > Founding Agent protection > Weaving.

### Community Organising (Restoration, post-Founding)
Pool: 1D base + 1D per adjacent territory with RM Presence marker (PP-460). Failure: no Stability cost. Retry next season.

### BG-Only Mode Notes
- PW track not used.
- RM co-victories (Varfell+RM, Hafenmark+RM) not available.
- "5 players only" restriction struck — RM is not a player faction in any player-count BG game.


### RM Status by Mode
| Mode | RM Status |
|------|-----------|
| BG only | Not a playable faction. Presence markers are environmental tokens (GM/table). No player controls RM. No RM solo or co-victory. |
| Hybrid | Not present at game start. Emerges via Founding event. Once founded: playable by PC's controlling player (or GM if NPC-founded). |


### Popular Will (PW) Track
Range 0–5. Public track (placed near MS clock). Starts at 0. Belongs to no faction.

**Advances +1 when:**
- ≥ 2 territories simultaneously have PT ≤ 1 AND no Church Heresy Investigation is active in any of them (checked at Accounting).
- A PC performs a successful Community Organising or Community Weaving personal scene in a PT ≤ 1 territory (Zoom In result).

**Regresses −1 when:**
- Church executes a successful Heresy Investigation in a PT ≤ 1 territory.
- CI ≥ 60 at Accounting (while CI ≥ 60: PW regresses −1/season automatically).

Floor: 0. Ceiling: 5.


### Founding Trigger (all three at any Accounting, Hybrid mode only)
| Condition | Threshold |
|-----------|-----------|
| PW track | ≥ 3 |
| Territories with PT ≤ 1 | ≥ 3 |
| MS | ≤ 60 |


### Founding Procedure
Founding Agent declared (PC with communal Conviction, or named NPC at GM discretion).
Roll: Founding Agent's Influence vs Ob = CI ÷ 10 (round up, min 1, max 5).

| Degree | Starting Stats (L+PS seeded equal per PP-686 v2; flagged: RM is statless per PP-460, see TODO note below) | Presence Markers |
|--------|---------------|-----------------|
| Overwhelming | L 2, PS 2, Influence 3, Wealth 1, Military 0, Stability 4 | 3 markers in PT ≤ 1 territories |
| Success | L 1, PS 1, Influence 2, Wealth 1, Military 0, Stability 3 | 2 markers |
| Partial | PW +1. Not founded. Retry next Accounting. | — |
| Failure | PW −1. Church gets 1 free Heresy Investigation. Cannot retry until PW resets to ≥ 3. | — |

**Post-founding card hand:** 2× Praetor, 1× Pontifex, 1× Recess.
**NPC-founded RM AI priority:** PT reduction > Presence spreading > Founding Agent protection > Weaving.


### Community Organising (Restoration, post-Founding)
Pool: 1D base + 1D per adjacent territory with RM Presence marker (PP-460). Failure: no Stability cost. Retry next season.


### BG-Only Mode Notes
- PW track not used.
- RM co-victories (Varfell+RM, Hafenmark+RM) not available.
- "5 players only" restriction struck — RM is not a player faction in any player-count BG game.
