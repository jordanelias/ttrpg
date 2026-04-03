# AUD-BG-01 — Board Game System Audit
## Date: 2026-04-02
## Modes: A (Formulas), B (Number Systems), C (Interaction Chains), D (Gaps), E (Principles), F (Playtest Burden), G (Cross-Mode)
## Source: params_board_game.md v0.5.4 + stage_bg_board_game_mode.md v0.8 + stage_bg_proposal_v02.md

### P1 Findings
| ID | Description | Resolution |
|----|-------------|------------|
| F-01 | Seasonal Accounting reference card absent — 13+ steps, 8/10 load, no guided structure | Open deliverable — PP-180 adds steps to params |
| GAP-BG-01 | TC 80 territorial seizure scope undefined — how many territories simultaneously? | Open — editorial decision required |
| GAP-BG-05 | BG Co-Movement Resolution Protocol absent — P-14 violation | Open — ED-086, design work required |

### P2 Findings
| ID | Description | Resolution |
|----|-------------|------------|
| A-02 | Trade Overwhelming near-unreachable at Prosperity 7 (5% at 5D vs Ob 3) | Design note — acceptable edge case at game start |
| B-01 | PI scale (0–10) vs TC/RS/IP (0–100) — reference material clarity needed | PP-180 adds explicit note |
| B-02 | Intel fractional +0.25 tracking — UX burden | PP-180 simplifies to token counter |
| C-01 | Church Excommunication Overwhelming effectively 0% under PP-179 | P2 — Success path complete; Overwhelming is bonus |
| C-02 | Church Deed 4 path — Excommunication Ob equals Crown Mandate; Crown recovery outpaces Church pressure | PP-180 reduces Excommunication Ob to max 4 |
| GAP-BG-02 | Drawn battles — beyond "stalemate, both Cohesion −1" undefined | PP-180 adds drawn battle rule |
| GAP-BG-03 | Policy Instrument (Crown) undefined | PP-180 adds definition |
| GAP-BG-04 | Co-Movement VTM effects at cap — no conversion | PP-180 adds rule |
| GAP-BG-06 | Restoration Organizing vs Weaving split not in params | PP-180 extracts from synthesis |
| G-01 | Thread Debt cross-mode (TTRPG Ob vs BG token) — no hybrid rule | PP-180 adds hybrid bridge rule |

### P3 Findings (noted, no patch)
| ID | Description |
|----|-------------|
| B-03 | BG stat floor 0 vs TTRPG attribute floor 1 — minor divergence acceptable |
| B-04 | RDT uses 0–6 scale unique to Hafenmark — acceptable faction asymmetry |
| B-05 | Torben Loyalty Clock 1–8 is unique scale — acceptable given narrative specificity |

### Systems Not Yet in Params (from amendment2 — extraction scheduled next session)
- Riskbreaker Pool and Priority Tree (GAP-BG-09)
- AER / Altonian Ecclesiastical Relationship (GAP-BG-10)
- RDT / Reformed Doctrine Track (GAP-BG-11)
- VTM full spec (GAP-BG-12)
- Crown Dominion alternate victory (GAP-BG-13)
- Church Dual Theocracy alternate victory (GAP-BG-14)
- Hafenmark Path A/B victories (GAP-BG-15)
These are design-complete in amendment2 but not yet authoritative in params.
