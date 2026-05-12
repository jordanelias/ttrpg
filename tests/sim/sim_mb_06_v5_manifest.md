# SIM-MB-06 v5 Module Manifest
# Scope: atom architecture exploration — 15×15 unit grid w/ shaped atoms,
#        25×25 battlefield w/ 5-cell buffer, per-cell movement,
#        side-mirrored patterns, contact-based engagement (Bii pool formula)
#
# Status: EXPLORATORY — not yet canonical. Multiple design tensions surfaced
# (Cannae envelopment failure, composite pool penalty, tip support absent)
# still need design pass before promotion to canonical mechanic.
#
# Iterations covered v1→v5:
#   v1: 3×3 macro-column model (abandoned — composition crushes distribution)
#   v2: spillover engagement (broken — still deadlocked on disjoint macro-cols)
#   v3: movement-driven contact (broken — atoms pass through each other)
#   v4: 21×21 battlefield + halt-on-contact (Cannae winrate 3%)
#   v5: per-cell movement + Bii pool + orders + side-mirror
#       + 25×25 buffer (current state)
#
# Validated mechanics carried from SIM-MB-05:
#   - ED-811 degree-gated symmetric (workplan v1.1 §2.1)
#   - ED-815 Discipline as formation coherence
#   - ED-816 shape modifiers (Arrowhead +2 tip, Horseshoe wings/center, etc.)
#   - ED-817 drift-to-Line cascade
#
# Open design decisions documented in visualization §07-08:
#   - B-ii: wings target point behind enemy (for envelopment)
#   - C-i/ii: pool formula rebalance (small-atom penalty)
#   - E: tip support / formation cohesion penalty
