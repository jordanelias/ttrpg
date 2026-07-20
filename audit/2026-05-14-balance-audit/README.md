# 2026-05-14 Balance Audit — Parts 6-13

13-part bottom-up granular emergent balance audit. Methodology: Monte Carlo
agent-based simulation with canonical rule verification, sensitivity analysis,
character-scale decoupling, historical-precedent mechanic design.

## Deliverables in this directory

| File | Content |
|------|---------|
| `part6_bottom_up_v3sim_2026-05-14.md` | Bottom-up MC v3 with 10 rule violations (corrected in Part 7) |
| `part7_canonical_v5sim_2026-05-14.md` | Canonical-verified v5 simulator results |
| `part8_sensitivity_synthesis_2026-05-14.md` | Q-1/Q-3/Q-4 sensitivity sweeps; leverage ranking |
| `part9_character_decoupling_2026-05-14.md` | Almud vs Crown decoupling (scale-layer surfacing) |
| `part10_crown_initiative_design_2026-05-14.md` | Crown Initiative card design (3 modes; historical anchors) |
| `part11_throughline_meta_audit_2026-05-14.md` | PP-674 framework audit + vetting block for Crown Initiative |
| `part12_v8_refutation_2026-05-14.md` | Symmetric-analog-cards hypothesis refuted |
| `part13_integrated_balance_solution_2026-05-14.md` | RC-v1 ratification slate + asymmetric balance hypothesis |
| `*_results_2026-05-14.json` | Raw sim output data per part |

## Deferred follow-up

Simulator source code (`mc_v3.py` through `mc_v10.py`, `crown_initiative_sim.py`,
`char_decoupling.py`) is in this audit chain but NOT committed here.
sim_fabrication_check requires `# [canonical: path §section]` comments on every
mechanical constant. To be added in next iteration; simulator sources held in
working session pending citation pass.

## Key findings summary

Canonical v5 sim baseline: Crown 22.8% / Church 51.4% / Hafenmark 19.6% / Varfell 6.2%
(15/15 victory threshold; consent=0.5; cap=6; 36 seasons).

Editorial slate (priority-ordered by sensitivity leverage):
- Q-1 Treaty consent rate (each 25pp shifts Crown ~10pp)
- Q-11 Excommunication recovery via Coronation Renewal Mode III
- Q-21 Ecclesiastical Appointment throttle to every-other-arc
- Co-Victory partition threshold at 11/15

Proposed mechanics (Part 10/11/13):
- Crown Initiative (3 modes, PP-674 vetted)
- Vaynard's Settlement (post-conquest consolidation)
- Vaynard's Hall (military-court L-gain)
- Charter of Liberties (revised — pure W cost)
- Treaty Expiration rule (40%/arc lapse)

Asymmetric balance hypothesis: Crown 35-45% / Church 20-30% / Hafenmark 15-25% / Varfell 10-20%
(reflecting canonical starting territory split 6/4/1/4 per peninsular_strain_v30 §2.1).

Throughline coverage: extends N2, N6, T4, T9, T-15a; preserves N1, N5. No breaks.
Meta-throughline: Μ-α primary, Μ-δ secondary; М-1/М-4/М-5/М-6 extended.
No failure-lexicon violations across 13 parts.
