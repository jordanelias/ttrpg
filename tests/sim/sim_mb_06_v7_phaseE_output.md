# SIM-MB-06 v7 Phase E Output

==============================================================================
SIM-MB-06 v7 Phase E — tip support constraint
==============================================================================

[TEST 1] Arrowhead vs Line — KEY metric for tension E
Baseline: 0% (tip races forward, dies isolated).
  OFF (baseline): Arrowhead-A vs Line-B          A:  0.0%  B:100.0%  D:  0.0%  t=7.3
  X=1 strict: Arrowhead-A vs Line-B              A:  0.0%  B:100.0%  D:  0.0%  t=8.1
  X=2 moderate: Arrowhead-A vs Line-B            A:  0.0%  B:100.0%  D:  0.0%  t=7.3
  X=3 loose: Arrowhead-A vs Line-B               A:  0.0%  B:100.0%  D:  0.0%  t=7.3

[TEST 2] Line vs Line mirror (no fast cells — should be unchanged)
  OFF (baseline): Line-A vs Line-B               A: 50.0%  B: 48.3%  D:  1.7%  t=9.4
  X=1 strict: Line-A vs Line-B                   A: 50.0%  B: 48.3%  D:  1.7%  t=9.4
  X=2 moderate: Line-A vs Line-B                 A: 50.0%  B: 48.3%  D:  1.7%  t=9.4
  X=3 loose: Line-A vs Line-B                    A: 50.0%  B: 48.3%  D:  1.7%  t=9.4

[TEST 3] Cannae — Horseshoe vs Arrowhead (tip support changes Arrow dynamics)
  OFF (baseline): Horseshoe-A vs Arrowhead-B     A: 65.0%  B: 35.0%  D:  0.0%  t=8.6
  X=1 strict: Horseshoe-A vs Arrowhead-B         A: 33.3%  B: 66.7%  D:  0.0%  t=8.5
  X=2 moderate: Horseshoe-A vs Arrowhead-B       A: 65.0%  B: 35.0%  D:  0.0%  t=8.6
  X=3 loose: Horseshoe-A vs Arrowhead-B          A: 65.0%  B: 35.0%  D:  0.0%  t=8.6

[TEST 4] Arrowhead vs Horseshoe — does tip support help Arrowhead break through?
  OFF (baseline): Arrowhead-A vs Horseshoe-B     A: 16.7%  B: 81.7%  D:  1.7%  t=8.2
  X=1 strict: Arrowhead-A vs Horseshoe-B         A: 63.3%  B: 35.0%  D:  1.7%  t=8.8
  X=2 moderate: Arrowhead-A vs Horseshoe-B       A: 16.7%  B: 81.7%  D:  1.7%  t=8.2
  X=3 loose: Arrowhead-A vs Horseshoe-B          A: 16.7%  B: 81.7%  D:  1.7%  t=8.2

[TEST 5] Tier sweep — Arrowhead vs Line at T2, T3, T4
  OFF (baseline): Arrowhead T2 vs Line T2        A:  4.0%  B: 96.0%  D:  0.0%  t=5.1
  X=1 strict: Arrowhead T2 vs Line T2            A: 34.0%  B: 56.0%  D: 10.0%  t=5.7
  X=2 moderate: Arrowhead T2 vs Line T2          A: 34.0%  B: 56.0%  D: 10.0%  t=5.7
  X=3 loose: Arrowhead T2 vs Line T2             A:  4.0%  B: 96.0%  D:  0.0%  t=5.1
  OFF (baseline): Arrowhead T3 vs Line T3        A:  0.0%  B:100.0%  D:  0.0%  t=7.4
  X=1 strict: Arrowhead T3 vs Line T3            A:  0.0%  B:100.0%  D:  0.0%  t=8.1
  X=2 moderate: Arrowhead T3 vs Line T3          A:  0.0%  B:100.0%  D:  0.0%  t=7.4
  X=3 loose: Arrowhead T3 vs Line T3             A:  0.0%  B:100.0%  D:  0.0%  t=7.4
  OFF (baseline): Arrowhead T4 vs Line T4        A:  0.0%  B: 74.0%  D: 26.0%  t=14.2
  X=1 strict: Arrowhead T4 vs Line T4            A:  2.0%  B: 60.0%  D: 38.0%  t=14.7
  X=2 moderate: Arrowhead T4 vs Line T4          A:  0.0%  B: 74.0%  D: 26.0%  t=14.2
  X=3 loose: Arrowhead T4 vs Line T4             A:  0.0%  B: 74.0%  D: 26.0%  t=14.2

==============================================================================
INTERPRETATION:
- X=1 strict: tip can be 1 ahead, very tight cohesion
- X=2 moderate: tip can be 2 ahead, allows wedge formation
- X=3 loose: tip can be 3 ahead, close to unconstrained
- Pick gap value that rescues Arrowhead vs Line without breaking Cannae
==============================================================================
