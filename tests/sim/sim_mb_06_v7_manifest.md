# SIM-MB-06 v7 Module Manifest
# Iteration: v6 → v7 (Phase E tip support + tension F surfaced)
# Date: 2026-05-12

## ADDED IN v7

### Tip support constraint (Jordan-directed Phase E)
Each cell with speed > min_speed_in_atom cannot advance more than
TIP_SUPPORT_GAP offsets past the slowest non-zero-speed cell.
Currently affects Arrowhead only (tip speed 2, base speed 1).

Globals:
- TIP_SUPPORT_ENABLED = True
- TIP_SUPPORT_GAP = 2 (default — no behavioral change for current matchups;
  X=1 produces tight-wedge behavior, see below)

## RESULTS

### Where tip support fires
- X=1: tight wedge — Arrowhead's tip stays 1 offset ahead of base.
  - Arrowhead vs Horseshoe: 17% → 63% winrate (tip arrives in formation)
  - Cannae (Horseshoe vs Arrowhead): 65% → 33% (Arrow no longer self-isolates,
    breaks through Horseshoe's thin center)
  - Arrowhead T2 vs Line T2: 4% → 34%
- X=2: no behavioral change at T3 (tip naturally wouldn't exceed 2-offset gap
  in typical engagement before contact); some constraint at T2
- X=3: no behavioral change

### Where tip support FAILS to help
- Arrowhead T3 vs Line T3: 0% at all X values
- Arrowhead T4 vs Line T4: 0% at all X values

## NEW TENSION F (surfaced by Phase E)

The pool formula structurally penalizes narrow attackers.

When Arrowhead T3 tip (1 cell) hits Line T3 front (5 cells):
- a_engaged = 1, a_max_width = 9 → a_engage_frac = 0.11
- b_engaged = 3, b_max_width = 5 → b_engage_frac = 0.60
- Arrowhead pool ≈ base × 0.11 ≈ 1 die
- Line pool ≈ base × 0.60 ≈ 4 dice
- Line outrolls 4:1 against the tip cell

Historically a wedge CONCENTRATES force at a narrow point — the entire
tactical concept. The current sim treats narrow contact as "less of your
unit fighting", which is the opposite of the historical mechanic.

Possible fixes (queue for Phase F):
- (F-i)   Use min(a_eng, b_eng) as shared engagement-zone width for both
- (F-ii)  Add Arrowhead tip-specific pool bonus that compensates for thin engagement
- (F-iii) Redefine engage_frac as engagement intensity, not unit-width fraction
- (F-iv)  Use contact-zone-width (independent of either atom's max_width)

## STATUS

EXPLORATORY. v7 commits the mechanic infrastructure; actual values held at
defaults that preserve v6 behavior. Tension F documented as the next clear
priority for atom architecture promotion.

ED-814 remains canonical mechanic. Atom architecture not yet ratified.
