"""
sim/provincial/tactic_cards.py — Tactic card pool + faction-restricted modifiers

Canon source: designs/provincial/mass_battle_v30.md §A.7 (tactic-card mechanism);
              designs/audit/2026-05-17-v18-integration/integration_plan_v18.md §1.4
              (card-pool contents BLOCKED on contamination audit per Jordan
              diagnosis 2026-05-17)
Game Design constraints applicable: GD-1
Status: [BLOCKED — Phase 7 stub 2026-05-18. Canonical name reserved per
         mass_battle_integration_v30.md §4.1 Step 1 sub-step 3. Card-pool
         CONTENTS pending contamination audit; only the canonical name +
         empty container ship in C2 scope.]

The mass-battle engine (massbattle.py) ports without referencing this dict —
v22 does not have FACTION_TACTIC_CARD_POOL_MODIFIERS. The empty stub here
reserves the canonical name and import path for the post-audit content authoring
pass; the mechanism (apply card effects) ports later when contents are unblocked.

Dependencies:
  - (none — pure data; future revisions will import from massbattle for effect-apply hooks)

Entry points:
  - FACTION_TACTIC_CARD_POOL_MODIFIERS: dict  — empty until contamination audit completes
"""
from __future__ import annotations


# [BLOCKED: contamination audit per integration_plan_v18 §1.4]
# Per Jordan diagnosis 2026-05-17: prior card-pool authoring may contain
# Claude-overreach contamination. No content authored here until audit produces
# verified pool definitions. The canonical name is reserved so downstream
# importers can begin wiring without circular-blocking on contents.
FACTION_TACTIC_CARD_POOL_MODIFIERS: dict = {}
