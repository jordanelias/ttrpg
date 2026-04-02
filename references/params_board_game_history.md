# params_board_game — Patch History
## Container: references/params_board_game.md
## Auto-maintained — appended by valoria-orchestrator on patch application
## Do not read this file in simulations — it is history, not values

---

## PATCH SUMMARY (ST-BG series, applied 2026-04-02)

### PP-033 — Catastrophic Failure Replaces Failure Degree
Catastrophic Failure is a fifth degree that REPLACES Failure. Not additive.

### PP-034 — Drawn Battles
Equal net successes: both sides Cohesion −1, hold position, no territory change.

### PP-035 — Hollow Victory Scope
Hollow Victory applies to Deed-counting factions only (Hafenmark, Guilds).
Restoration (RS-based) and Crown/Löwenritter (mandate-based) are excluded.

### PP-036 — Policy Instrument Definition (Crown)
Crown bonus action at Mandate ≥ 4. Any standard action. Once/season. Not interruptible by Parliamentary Manoeuvre.

### PP-037 — Co-Movement VTM at Cap
VTM effects blocked by once/season cap or VTM max (7): convert to +1D on following season's Tribune action (max +2D total).

### PP-038 — BG vs TTRPG Pool Size
BG aggregates (sum of all Martial). TTRPG uses per-unit pools. Not statistically equivalent by design.

### PP-039 — Military 0 + Muster
At Military 0: Muster actions produce no units and may not be taken.

### PP-040 — BG Unit TS (Southernmost)
Default TS=0. Restoration+Weaver: TS=30. Varfell VTM≥2: TS=30. Church Templar: TS=0 (doctrine).

### PP-041 — Military Loss Timing
TTRPG: immediate. BG: queues to Accounting. Hybrid: TTRPG timing during battle.

### PP-042 — Military Victory and TC/RS
Military victory alone produces no TC or RS change. Thread operations during battle produce standard RS changes.

### PP-043 — Wound Penalties in Hybrid
Wound Ob penalties apply to PC's CR checks in TTRPG mass battle. Do NOT reduce BG commander bonus (Military÷3 calculation).

## DEGREE TABLE — BG SPECIFIC
## [PROVISIONAL: Overwhelming threshold per ED-031]
| Net Successes | Degree |
|---|---|
| ≥ Ob + 1 (surplus ≥ 1) | Overwhelming |
| = Ob exactly | Success |
| Ob − 1 | Partial |
| ≤ 0 | Failure |

Note: TTRPG parent uses 2×Ob for Overwhelming. BG uses Ob+1 (more achievable).
This is intentional — BG is a strategic abstraction. Review during playtesting.
No Catastrophic Failure category (struck 2026-04-02).

## PENDING EDITORIALS BLOCKING FULL SYNC
- ED-001: Card-Hand system (P1-BLOCKER) — prevents full stage_bg sync
- ED-031: PROVISIONAL — BG Overwhelming = Ob+1 surplus. Intentional divergence from TTRPG 2×Ob. Strategic abstraction warrants more achievable threshold.
- ED-032: TC 80 seizure scope (P1)
- ED-033: Commander bonus formula (P1)
- ED-034: Ceiral Ritual scale asymmetry (P2)
- ED-035: Muster output in BG context (P2)
- ED-036: Altonian unit stats BLOCKER
- ED-039: Military seasonal cap pooling (P2)
