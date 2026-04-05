# VALORIA CROSS-MODE SIMULATION (NON-OPTIMAL ACTORS)
## SIM-IDs: SIM-X-26, SIM-X-27, SIM-X-28 | Date: 2026-04-04

---

## SIM-X-26 TTRPG Personal Combat

Actors: Davan Rekk (12D, Stamina 5, TN 7 Long Heavy Blade, 1 wound). Non-optimal: fixed 8D offence / 4D defence every round.
Solmund Vael (12D, Stamina 8, TN 5 Short Light Blade). Non-optimal: hoards Momentum, never spends.

Round outcomes (most likely):
| Round | Davan hit | Solmund hit | Davan Stamina | Solmund Momentum |
|-------|-----------|-------------|--------------|-----------------|
| 1 | Miss (~35%) | Stamina -1 | 4/5 | 0 |
| 2 | Miss | Stamina -1 + Overwhelming | 3/5 | 1 (hoarded) |
| 3 | Miss | Stamina -1 | 2/5 | 2 (hoarded) |
| 4 | Miss | Stamina -1 | 1/5 | 2 (wasted) |

Findings:
F-26-01: TN differential > pool size. 8D TN7 offence vs 6D TN5 defence: attacker hit rate ~35%. TN 5 weapon gives Solmund structural defence advantage.
F-26-02: Momentum hoarding is strictly dominated. Resets per session; unspent = pure loss. No mechanic discourages hoarding.
F-26-03: Stamina exhaustion threshold undefined. Scene hit Stamina 1 with no resolution trigger. [GAP-SIM-X26-01]
F-26-04: Fixed allocation without adaptation is punished. Healthy.
F-26-05: 2 unspent Momentum would have ended fight Round 3. Hoarding cost: ~2 extra rounds.

---

## SIM-X-27 Hybrid Domain Season

State: RS=50, TC=44, IP=35. Crown M4 Sta3. Church I6. Varfell Mil5.
Non-optimal: Church delays TC leverage 2 phases. Crown targets Guilds (Ob4, P~6%) not Varfell (Ob3, P~28%). PC Mira uses indirect social move (narrative flag, 1-season lag).

Phase outcomes:
| Phase | Church | Crown | Notable |
|-------|--------|-------|---------|
| 1 | Wealth partial (no change) | Guilds attack failure | Guilds I +1 (NPC) |
| 2 | Influence partial | Mandate partial | TC idle |
| 3 | Parliamentary Motion success Crown M -1 | Stability +1 | TC 44->42 |

End: Crown M3 Sta4. Church TC42. Guilds I5. Varfell-Lowenritter uncontested.

Findings:
F-27-01: TC timing window exists. Delay gave Crown recovery window (Crown failed anyway). System healthy; urgency under-incentivised.
F-27-02: Failed Domain Actions carry no blowback. 6% success action = pure opportunity cost. Consider minor Stability/Standing cost on failure.
F-27-03: Social moves produce 1-season lag vs direct Domain Action. Mechanically sound.
F-27-04: Conservative play produced identical end-state. No faction capitalised on delay window. Aggression under-incentivised.
F-27-05: RS natural decay undefined. [GAP-SIM-X27-01 - carried SIM-H-01]

---

## SIM-X-28 BG Multi-Faction Turn

State (Turn 4): Crown M4 I4 W3 Mil4 Sta4 | Church M5 I5 W5 Mil4 Sta5 Std4 | Hafenmark M4 I4 W6 Mil3 Sta4 | Varfell M4 I4 W4 Mil4 Sta4 | Guilds M3 I4 W6 Mil2 Sta5.
Coalition: Church+Hafenmark pact triggers at both Influence 6. Neither prioritises it.

Phase outcomes:
| Phase | Crown | Church | Hafenmark | Varfell | Guilds |
|-------|-------|--------|-----------|---------|--------|
| 1 | Military +1 W-1 | Wealth +1 | Wealth +1 (cap7) | Stability +1 | Wealth partial |
| 2 | Military +1 W-1 | Influence +1 (->6) | Military +1 | Territory fail (Ob6) | Influence partial |

Accounting: Crown W1 -> Sta -1. Church Std +1 (cap5). Coalition: Church I6 Hafenmark I4 - pact NOT triggered.

End: Crown M4 I4 W1 Mil6 Sta3 | Church M5 I6 W6 Mil4 Sta5 Std5 | Hafenmark M4 I4 W7 Mil4 Sta4 | Varfell M4 I4 W4 Mil4 Sta5 | Guilds M3 I4 W6 Mil2 Sta5

Findings:
F-28-01: Crown Military 6 vs no threat = local optima trap. System produces no reward; Wealth depletion visible and correct.
F-28-02/03: Hafenmark Influence 4 (needed 6) blocks pact. Local optima blocked mutually beneficial coalition. Salience problem.
F-28-04: Varfell Stability above crisis threshold - consolidation dead action. No soft-cap on safe-stat over-investment.
F-28-05: Guilds Wealth at cap; marginal value ~0. Diminishing returns above 5 not confirmed. [GAP-SIM-X28-01]
F-28-06: Crown W1 -> Sta -1 accounting. Self-inflicted; system consequence correct.
F-28-07: Church I6 but Hafenmark I4 - coalition partial fulfilment undefined. [GAP-SIM-X28-02]
F-28-08: Varfell territory Ob 4 (Phase 1) -> Ob 6 (Phase 2) after Crown buildup. P: ~27% -> <2%. Timing sensitivity real and healthy.

---

## Cross-Mode Summary

| Finding | Mode | Type |
|---------|------|------|
| TN differential > pool size in combat | TTRPG | Mechanical note |
| Momentum hoarding dominated; no incentive | TTRPG | Design gap |
| TC/initiative delay under-incentivised | Hybrid/BG | Design consideration |
| Failed Domain Actions no blowback | Hybrid | Design consideration |
| Coalition salience low; local optima dominate | BG | Design concern |
| No soft-cap on safe-stat over-investment | BG | Design gap |
| Timing sensitivity on territory contests | BG | Healthy |
| RS decay rate undefined - P1 all modes | All | P1 gap |
| Coalition partial fulfilment undefined | All | P2 gap |

---

## Gaps Registered

| Gap ID | Description | Mode | Priority |
|--------|-------------|------|----------|
| GAP-SIM-X26-01 | Stamina exhaustion threshold undefined | TTRPG | P2 |
| GAP-SIM-X26-02 | Momentum between-scenes carry undefined | TTRPG | P2 |
| GAP-SIM-X27-01 | RS natural decay rate not in params (carried SIM-H-01) | All | P1 |
| GAP-SIM-X27-02 | Presence vs Charisma attribute not confirmed | TTRPG | P2 |
| GAP-SIM-X28-01 | BG diminishing returns above Wealth 5 not confirmed | BG | P2 |
| GAP-SIM-X28-02 | BG coalition pact partial fulfilment undefined | BG | P2 |
