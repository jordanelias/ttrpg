# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_HYB_SIM_01
phase: Phase 11 — SIM-HYB-01 complete (complete hybrid session simulation)
status: CLOSED

completed:
  - SIM-HYB-01 "The Templar Crossing" — all modes run:
    - G4 (faction seasonal Season 2): TC 32→34, Church Mil 4→3, Varfell holds T6
    - G1 (BG Battle of T6): Church loses (~65% probability), Varfell defensive hold
    - K2 (Zoom In BG→HYB): GAP-K2-01 found and patched (PP-101 B.5)
    - C (full personal scene): Vaynard Thread op + debate with Klapp, stalemate
    - G3 (Threadwork): Overwhelming Leap 10D/Ob1, Object-scale Weaving, Gap averted, P-01 compliant
    - G2 (Debate): Klapp 11D vs Vaynard 7D, Church audience resistance=3, stalemate at Track=4
    - K2 (Zoom Out HYB→BG): state update clean
    - D (edge cases): 10 findings across 9 categories
    - J (cognitive load): Zoom In/Out = 14/10 (P1), Debate = 11/10 (P2)
    - L (precedents): 3 analogues checked; design drift flag vs BW Duel of Wits
    - M (flowchart): filed to designs/gm_ref_cp14/flowcharts/flowchart_templar_crossing.md

patches_applied:
  - PP-101 (P1): Practitioner rear vs front-line positioning + BG→TTRPG unit conversion (B.5)
    Commits: 343c99e (Session A), f477dfc (Session B)

params_fixed:
  - params_debate.md: AMPLIFY→COMPETITION, CROSS→DIVERGENCE (stale naming), SIM-DEBT-01→FULLY RESOLVED
  - params_mass_combat.md: PARAMS-GAP-04/05 noted as open

editorial_items_added:
  - ED-054: Evidence leverage mechanic in debate (P2)
  - ED-055: GM reference card for Zoom In/Out (P1 — cognitive load)
  - ED-056: Zoom In as TC win-delay exploit (P2)
  - ED-057: Unit ghost state during Zoom In window (P2)
  - ED-058: Debate stalemate forced resolution (P2)
  - ED-059: RS=0 at Zoom In — gap rule priority (structural)
  - ED-060: Composure restoration between debate scenes (P3)

p1_findings_open:
  - F-HYB-08: Military 1 faction no deployable unit in B.2 → PP-103 pending
  - F-HYB-09: Zoom In/Out cognitive load 14/10 → ED-055

params_gaps_open:
  - PARAMS-GAP-04: Mass combat pool split (Offence/Defence for unit-scale)
  - PARAMS-GAP-05: Mass combat Strength loss per excess success formula
  - PARAMS-GAP-06-MC: BG Battle Partial outcome undefined
  - BG Battle modifier (P-16 defender terrain bonus unconfirmed)

next_action:
  task: "PP-103: Military 1 faction unit gap — add Levy unit (CP 1) to B.2 or adjust minimum Military required for Zoom In. Then ED-055: draft GM reference card for Zoom In/Out."
  note: "No open P1 blockers in completed simulation. Two P1 findings from this sim still need patches (PP-103, ED-055). All debate calibration confirmed stable."
```
