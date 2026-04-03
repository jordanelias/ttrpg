# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_COMBAT_AUDIT
phase: SESSION CLOSED
status: COMPLETE

## WORK COMPLETED
Combat mechanic audit — Modes A–G (formula, number systems, interaction chains,
gap detection, core principles, playtest burden, cross-mode consistency).

## FINDINGS SUMMARY
P1: 8 findings (blocks play)
P2: 19 findings (ambiguity/asymmetry)
P3: 6 findings (polish)
Output: tests/audit_combat_2026-04-02.md

## P1 FINDINGS
GAP-CMB-01: Tie Up "disadvantage" undefined
GAP-CMB-02: Feint "next exchange" timing undefined
GAP-CMB-03: Health formula conflict (design doc §7 vs params_core)
GAP-CMB-04: Critical Hit rule absent from design doc §5 (params only)
GAP-CMB-05: PP-086 mass damage "net successes over Ob" ambiguous
GAP-CMB-13: ED-033 commander bonus — 3 conflicting formulas (pre-existing)
GAP-CMB-17: Rescue action — no mechanical resolution for interposition
G-P1-01: Anti-Armour keyword — referenced in §5 BG note, defined nowhere

## KEY P2 FINDINGS
- Fibonacci cap conflict: design doc "5th+" vs params "8+"
- Dodge action: params only, absent from design doc §4
- Versatile weapons: design doc only, absent from params_combat
- Mass combat round: >90s, >4 lookups (P1 playtest burden threshold)
- Cover, ranged zone: no BG translation documented

## COMMITS THIS SESSION
audit/simulation: combat audit Modes A–G — GAP-CMB-01–17, G-P1-01

next_session_start:
  priority_1: "Resolve GAP-CMB-03: confirm Health formula (End or End+6)."
  priority_2: "Resolve GAP-CMB-04: add Critical Hit rule to design doc §5."
  priority_3: "Resolve GAP-CMB-17: define Rescue mechanical resolution."
  priority_4: "Resolve GAP-CMB-01: define Disadvantage for Tie Up."
  priority_5: "Resolve G-P1-01: define Anti-Armour keyword for BG layer."
  priority_6: "Resolve GAP-CMB-02: define Feint next exchange timing."
  priority_7: "Resolve GAP-CMB-05: clarify PP-086 mass damage wording."
  priority_8: "Escalate ED-033 (commander bonus) for editorial decision."
```
