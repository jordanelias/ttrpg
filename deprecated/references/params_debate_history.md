<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY references/params_contest.md — history of superseded params. Do not use as a mechanical reference. Retained for audit trail only. -->

# params_debate — Patch History
## Container: references/params_debate.md
## Auto-maintained — appended by valoria-orchestrator on patch application
## Do not read this file in simulations — it is history, not values

---

## COMPILED MECHANICS SUMMARY (from debate_system_redesign_v1.md Part 6, 2026-04-02)

### Key Formulas
Presence modifier = floor((Presence − 3) / 2) → +0/+1/+2
Focus defence = floor(Focus / 2) → passive, no roll
Composure = Poise + Bonds + 3
Concentration = Focus + Presence (depletes −1/exchange, −1 extra on loss)
Attunement read pool = Attunement only (no History)
Memory bonus = +2D for specific named verifiable citation (binary)

### Conviction Track
Scale 0–10. Side A wins ≥7, Side B wins ≤3, compromise 4–6.
Audience resistance = avg Stability − 1 (min 0).
Movement: effective_margin = floor(margin × genre_weight × orientation_weight).
If effective_margin > resistance → Δ = effective_margin − resistance. Else 0.
Divergence uses half successes: floor((successes/2) × weight).

### Genre Weights
Primary genre: ×1.0. Others: ×0.5 base. Ethical mode adjusts one genre +0.5.
Crown: Present +0.5. Church/Hafenmark: Past +0.5. Varfell/Restoration: Future +0.5.
Guilds: GM picks. Range: 0.5/1.0/1.5.

### Strain
Strain = margin + 1 + Presence_modifier. Reduced by floor(Focus/2).
Rattled at strain ≥ Composure: −2D, lose Focus defence.

### Interaction Types
CLASH (same genre, opposite orientation): standard resolution.
COMPETITION (same genre, same orientation): reduced strain (margin−1 min 1).
DIVERGENCE (different genre): half-successes, no strain, initiative stays.
OBSCURING win: no tracker movement; place Doubt Marker (−2 to opponent's next effective_margin).
TIE: both take 1 strain, tracker +1 toward initiative holder.

### Asymmetric Proceedings
Disadvantaged party faces halved resistance (round up) for their tracker movement.


### R-65 — Practitioner Weaving Bonus
TS 30–59: +1D to debate pool. TS 60–89: +2D. TS 90+: +3D.
Declare before rolling. Visible action. Church may call Heresy Investigation.
Coherence check Ob 1 after exchange.
TTRPG/Hybrid only. No BG equivalent.

### SIM-DEBT-01
Stress tests v1+v2 calibrated against Cognition+History pool. With Presence×2 pool:
- High-Presence characters now dominate (Presence 7 = 14D base vs Cognition 7 = 7D base)
- Strain, Composure, tracker values need re-verification
- Re-simulation required before treating calibration values as final

## PENDING EDITORIALS
- ED-044: Obscuring as pure denial — confirm design intent (P1)
- ED-041: Niflhel social mode scope (P2)
- ED-042: Grand Debate role alternation (P2)
- ED-043: Corroboration in Church Tribunal (P2)
- ED-045: Genre pivot mid-debate (P2)
