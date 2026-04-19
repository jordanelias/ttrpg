## Three-Scale Resolution Model (PP-TBD)

Each season resolves in three layers, bottom-up:

1. **Settlement layer** (resolves first). Infrastructure actions: Church building construction,
   Guild trade operations, Crown ministerial placement, RM community organizing, governor
   appointments (including bishop appointments per PP-TBD). Settlement Order and Prosperity
   update. Black markets emerge (Order ≤ 1, no governor) or resolve (Order ≥ 3). Governor
   authority checks fire.

2. **Province layer** (resolves second). Fragmentation checks using updated settlement data.
   Accord recalculates from settlement Order floor-average. Province PV recalculates from
   settlement Prosperity weighted by controller alignment. Military movement along settlement
   adjacency graph. Mass battles resolve at settlement nodes. Territorial transfer.

3. **Peninsula layer** (resolves third). RS/CI/IP/PI/Strain clocks update from province-level
   events. Altonian pressure evaluated. Victory condition check against updated PV totals.
   Warden emergence. Season advances.

Control flows upward: settlement infrastructure → province Accord/PV → peninsula victory.
Pressure flows downward: peninsula events → province consequences → settlement disruption.


## Phase 4 Resolution Priority Order (v04 B4 — CORRECTED from stage_bg_proposal_v02 order)
| Priority | Order Type | Notes |
|----------|-----------|-------|
| 1 | Intel/Covert (Tribune) | Executes first; shapes information before other actions |
| 2 | Military (Legionary) — Battle | Battles resolve simultaneously per territory |
| 3 | Domain (Consul, Prefect, Architectus, Colonist) | Govern, Trade, Muster, March |
| 4 | Social (Senator) | Decree, Parliamentary Manoeuvre, Diplomacy |
| 5 | Thread operations (Pontifex, Weaver) | See PP-182 for three-dimensional auto-effects |
| 6 | Special/Unique Powers | Royal Decree, Excommunication, VTM ops, Sovereign Authority |
| 7 | Project advancement (Praetor) | Community Projects advance |

Within tier: descending Stability order. Ties: simultaneous.
NOTE: This corrects the stage_bg_proposal_v02 order (which put Thread Ops first). v04 is authoritative.


## Phase 5 Seasonal Accounting (v04 B4 — CORRECTED)
Execute in strict order:
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks: any faction with ≥2 attribute loss this season: Stability pool vs Ob = loss magnitude.
3. Advance Cooldown Track (all items −1 slot; at 0: return to hand).
4. Clock advances: RS baseline drift (−1 at Year-End/Winter only). CI per formula. IP per Altonian pressure table. PI changes.
4b. **Church Prominence update (ED-326):** Church player marks Prominent territories on faction mat — any territory where Church global Mandate exceeds that territory's controlling faction's global Mandate. Updated every Accounting. Used for: Counter-Narrative target eligibility, Seizure Ob formula, Piety Spread.
4c. **Accord checks:** (i) Each territory at Accord 1 without garrison (no military unit from controlling faction): Accord → 0. (ii) Each territory at Accord 0: Revolt — garrison fights Popular Uprising (Military vs Ob 2) or retreats; territory becomes Uncontrolled; Peninsular Strain +1. (iii) Passive normalisation: each territory with garrison AND no hostile action for 2 consecutive seasons: Accord +1 (cap 2).
4d. **Peninsular Strain update:** (i) If no inter-faction battles AND no Revolts this season: Strain −1 (min 0). (ii) If diplomatic resolution occurred (Treaty formed, Pledge honoured): Strain −1 (max one from this source/season). (iii) Apply Strain threshold effects.
4e. **Battle consequence accounting:** IP +2 if inter-faction battle occurred this season. RS adjustments from battles already applied during Phase 4 resolution.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: tokens >1 season old: RS −1/token. Serviced tokens: no drain; permanent residual RS −0.5 recorded.
7. Clear Thread Resonance markers (all factions reset).
8. Check threshold events: draw one Event Card per threshold crossed.
8b. Milestone Bonus check.
9. Warden Emergence check.
9b. Vaynard-Edeyja same-season rule: if Warden Emergence at Step 9 AND VTM ≥ 4 AND Varfell played Tribune Inward in T6: Warden Cooperation +1 immediately.
10. Warden Cooperation check.
10b. Torben/Elske Loyalty events: apply Loyalty changes.
11. [DISSOLVED — Hollow Victory totals no longer tracked. Step retained for numbering continuity.]
12. Victory condition check. Any faction meeting all its victory conditions for 2 consecutive Accounting steps declares victory. See designs/board_game/victory_v30.md §3 for all faction conditions. Co-victory pairings checked simultaneously (§4). Shared loss conditions checked first (§5).
13. Season marker advances. If Winter (every 4th season): Year-End Accounting (B11).


## Year-End Accounting (every 4th season = Winter, v04 B11)
1. Apply Year-End CI and RS fractions.
2. RS baseline drift −1 (annual world degradation).
3. Löwenritter (if active): raise one free unit; Prosperity −1.
4. Torben Loyalty Year-End modifiers: Crown PI ≥ 5 →+1; Crown upheld Mandate 2+ consecutive seasons →+1; Löwenritter PI ≥ 3 without Emergency Powers →+1.
5. Elske Loyalty Year-End modifiers.
6. Hollow Victory totals announced publicly.
7. Once-Per-Year effects trigger.
8. Age track (optional Long Campaign only).
9. Check CI Year-End fractions for threshold crossings.
10. Season resets to Spring. Campaign year advances.


## Accounting Phase Reference (PP-180 + v04 B4)
13-step sequence. See Phase 5 section above.
