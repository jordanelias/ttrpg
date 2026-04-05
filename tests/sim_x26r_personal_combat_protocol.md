# SIM-X-26R — Personal Combat Re-simulation with Decision Protocols
## Date: 2026-04-04 | Mode: C+D | Protocols: SATISFY, MOMENTUM-HOARDER, MARTYR, RISK-AVERSE
## 7-Dimension Tag:
## Mechanics: Personal Combat | Mode: TTRPG | Temporal: PRES
## Tracks: Health, Wounds, Stamina, Momentum | Factions: None
## NPCs: Davan, Solmund, Maret | Archetypes: SATISFY, MOMENTUM-HOARDER, MARTYR, RISK-AVERSE

## Actors
- Davan: Pool 11D, Health 9, Stamina 6, weapon Long Heavy Blade TN7
- Solmund: Pool 14D, Health 10, Stamina 8, weapon Short Light Blade TN5, Momentum 2 (carry-in)
- Maret: Protection target (no pool — scene edge)

---
## RUN A: Davan [SATISFY] vs Solmund [MOMENTUM-HOARDER]

### Round 1
Davan: 6O/5D (satisficing — first split achieving P(hit)≥50%)
Solmund: 3O/11D (maximise defence; MOMENTUM-HOARDER never spends offensively)
Davan O (6D TN7) E[net]=1.8 vs Solmund D (11D TN7) E[net]=3.3 → No hit (expected)
Solmund O (3D TN5) E[net]=1.65 vs Davan D (5D TN7) E[net]=1.5 → No hit (marginal)
State delta: no hits, Momentum 2 unspent

### Round 2-4: Identical splits, identical outcomes (SATISFY does not adapt)
Cumulative: 0 hits (Davan), 0 hits (Solmund), Momentum 2 lost at session end

---
## RUN B: Davan [MARTYR→protect Maret] vs Solmund [RISK-AVERSE]

### Round 1
Davan: Interpose (1O/10D) — protocol requires protecting Maret above all
Solmund: 7O/7D (P(hit)≈58%, within RISK-AVERSE threshold <30% failure)
Resolution: Solmund hits Davan (P≈58%, expected). 1 Wound. Davan pool 10D.
Davan O (1D TN7) vs Solmund D (7D TN7): P(hit)≈2%. No hit.

### Round 2
Davan: 0O/10D (still protecting, 1 Wound already taken)
Solmund: 7O/7D (same, still viable)
Resolution: Solmund hits again (P≈58%). 2 Wounds. Davan pool 9D.

### Round 3
Davan: 0O/9D. Still no SURVIVAL-FLOOR trigger (Health not reduced by wounds per PP-232).
Solmund hits again (P≈58%). 3 Wounds. Pool 8D.
Cumulative: Davan 3 Wounds, 0 offensive output. Solmund 0 Wounds, 2 Momentum unspent.

---
## Findings

F01 [P2]: SATISFY+MOMENTUM-HOARDER → attritional stalemate. P(1+ Davan hit in 4 rounds)≈68% but expected=0.
F02 [P2]: Static loop confirmed. No state change possible at expected values under these protocols.
F03 [P2]: MOMENTUM-HOARDER self-defeating — 2 Momentum lost at session end with zero benefit over 4 rounds.
F04 [P1-GAP]: Interpose action undefined in combat_design_v1.md. MARTYR protocol requires it. → GAP-SIM-X-26R-G01
F05 [P2]: Sacrifice has no mechanical payoff. MARTYR takes 3 Wounds protecting Maret; system provides no Momentum gain, Belief trigger, or ally bonus. → ED-171

## Gaps
- GAP-SIM-X-26R-G01: Interpose/redirect mechanic undefined in personal combat
- GAP-SIM-X-26R-G02: SURVIVAL-FLOOR threshold (Health≤2) incompatible with wound-based pool system (PP-232 wounds reduce pool, not Health score)
