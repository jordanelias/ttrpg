"""
sim/mc_v18.py — Top-level strategic simulator runner — orchestrator only, ≤200 lines target

Canon source: canon/02_canon_constraints.md §B (GD-1, GD-2, GD-3); designs/architecture/campaign_architecture_v30.md
Game Design constraints applicable: GD-1, GD-2, GD-3
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Replaces tests/sim/v17-integration/mc_v17.py (39k chars monolith). v17 archived in place; v18 is the new modular line. Implementation pending across all subpackage modules)]

Dependencies:
  - sim/autoload/* (all autoload services)
  - sim/peninsular/season
  - sim/peninsular/accounting
  - sim/autoload/victory

Entry points:
  - run_campaign(seed: int = 0, max_seasons: int = 100) -> CampaignResult
  - run_balance_sweep(n_campaigns: int = 1000, base_seed: int = 0) -> SweepResult

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def run_campaign(seed: int = 0, max_seasons: int = 100):
    raise NotImplementedError("sim/mc_v18.py — Pass 2l armature stub")


def run_balance_sweep(n_campaigns: int = 1000, base_seed: int = 0):
    raise NotImplementedError("sim/mc_v18.py — Pass 2l armature stub")
