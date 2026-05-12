# SIM-MB-06 v6 Phase C Battery Output (with halt-cell fix + facing)

==============================================================================
SIM-MB-06 v6 Phase C — pool formula variants
==============================================================================

[TEST 1] Composite atoms vs Uniform Line T3 — KEY metric
(Current Bii baseline gives composite ~2.7% — should normalize to 35-50%)
  baseline   composite-A vs uniform-Line-T3-B  A:  5.0%  B: 85.0%  D: 10.0%  t=7.9
  C-i        composite-A vs uniform-Line-T3-B  A: 81.7%  B: 10.0%  D:  8.3%  t=7.4
  C-ii       composite-A vs uniform-Line-T3-B  A: 38.3%  B: 43.3%  D: 18.3%  t=7.8

[TEST 2] Lethality control — Line T3 vs Line T3 (target: 3-6 turn mean)
  baseline   Line-T3 mirror                 A: 53.8%  B: 45.0%  D:  1.2%  t=9.7
  C-i        Line-T3 mirror                 A: 53.8%  B: 45.0%  D:  1.2%  t=9.7
  C-ii       Line-T3 mirror                 A: 53.8%  B: 45.0%  D:  1.2%  t=9.7

[TEST 3] Shape matrix — Arrowhead vs Line, Horseshoe vs Line
  baseline   Arrowhead vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=7.5
  baseline   Horseshoe vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=6.4
  C-i        Arrowhead vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=7.5
  C-i        Horseshoe vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=6.4
  C-ii       Arrowhead vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=7.5
  C-ii       Horseshoe vs Line              A:  0.0%  B:100.0%  D:  0.0%  t=6.4

[TEST 4] Cannae — Horseshoe vs Arrowhead (expected to stay ~2-10% — fix is B-ii)
  baseline   Horseshoe-A vs Arrowhead-B     A: 62.0%  B: 38.0%  D:  0.0%  t=8.5
  C-i        Horseshoe-A vs Arrowhead-B     A: 62.0%  B: 38.0%  D:  0.0%  t=8.5
  C-ii       Horseshoe-A vs Arrowhead-B     A: 62.0%  B: 38.0%  D:  0.0%  t=8.5

==============================================================================
INTERPRETATION:
- C-i drops troop-frac → small atoms get full pool (may overcorrect)
- C-ii floors at 50% → small atoms get min(troop-weighted, 50%-floor)
- Pick variant where Test 1 normalizes AND Tests 2-3 don't break
==============================================================================
