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

---

## AUDIT 2026-04-02 — GAP-FILL PATCHES (PP-112 through PP-122)

### PP-112 — Remove Struck Majority-1s Override
Majority-1s override (P-12) struck from params. All rolls: standard degree table only.

### PP-113 — Stat Ceilings and Floors
Faction stats floor 0, ceiling 7. Standing 0-10.

### PP-114 — IP Post-80 Escalation [PROVISIONAL]
IP 81-89: Vanguard +1 territory/season. IP 90-99: Altonian Mil +2. IP 100: shared defeat.

### PP-115 — PI Threshold Table [PROVISIONAL: ED-055]
PI 0 = dissolution + coup. 6-tier table added.

### PP-116 — TC Seasonal Cap + Ceiling [PROVISIONAL: ED-056]
Domain Actions +-3. All sources +-5. Seizure exempt. TC ceiling 100 cosmetic.

### PP-117 — Faction Collapse Exit [PROVISIONAL: ED-053]
1 season + no hostile actions + Govern Ob 2 Success. Auto-exit Season 2: Stability 1, Mandate 0.

### PP-118 — Simultaneous Catastrophe [PROVISIONAL: ED-054]
RS Rupture Step 6 takes precedence. Restoration Step 5 victory pre-empts.

### PP-119 — BG Unit Cohesion [PROVISIONAL]
Levy 3, Infantry 4, Elite 5, Cavalry 4, Artillery 3, Thread Corps 4. Track 0-6.

### PP-120 — No BG Coherence Cost [PROVISIONAL: ED-057]
BG Thread ops: no Coherence. Hybrid: PC Coherence via Cascade Step 3.

### PP-121 — Reformed Settlement Penalty Permanent [PROVISIONAL: ED-058]
+1 Ob Diplomacy vs Hafenmark permanent. No reversal mechanic.

### PP-122 — CP Awards in Hybrid [PROVISIONAL]
CP +1 on BG Domain Action if Belief declared. BG-only: no CP.

### PP-177 — Fail Forward (BG Domain Actions) [PROVISIONAL: ED-085, ED-086, ED-087]
Fail Forward operationalised for BG mode. Partial = goal achieved + Minor complication (player choice of Standing −1 or Public Instability +1). Failure = goal not achieved + Moderate complication (action-type specific, mandatory). Severe tier added for Ob ≥ 4 Failures (Moderate + Stability −1). Parliamentary Manoeuvre Partial supersedes PP-170 "no effect" ruling — player may choose "no effect" as their Minor option.

### PP-178 — LIR/FF Cross-Mode Applicability Note [PROVISIONAL: ED-087b]
Let It Ride (LIR): TTRPG = full; Hybrid = full for PCs / action-economy for units; BG = action-economy-enforced (one slot per season).
Fail Forward (FF): TTRPG = Hard Moves §13.5; Hybrid = Hard Moves for PCs / PP-177 for units; BG = PP-177 complication table.
Debate exchanges: explicitly exempt from LIR (each exchange = new fictional state).
Thread operation irreversibility: Thread rules govern; LIR does not add further restriction.

### PP-179 — BG Overwhelming Degree Table (applied prior session)
See patch_register.yaml PP-179. Not a FF patch.

### PP-180 — Hybrid Zoom-Boundary FF Rule [PROVISIONAL: ED-087c]
When a PC Failure in TTRPG/Hybrid mode produces a zoom transition to faction scale, the complication carries forward as: −1 Ob modifier on the faction's next relevant Domain Action OR Standing −1 consequence (GM choice based on fiction). Complication is not discarded at the scale boundary.
