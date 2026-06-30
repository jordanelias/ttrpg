"""mass_battle.engine — public API wrapper for the mass-battle engine.
Imports all modules and re-exports the full namespace, so `from mass_battle.engine import *`
(and the sim_mb_sigma.py shim) yields the same names the monolith exposed.
Also defines MECHANICS: a registry of canonical mechanic -> implementing symbol + toggle +
canonical source + status, with a self-test asserting every registered mechanic resolves."""
from mass_battle.config import *
from mass_battle.core.exchange import *  # [Stage-1] resolver layer: pool-assembly primitives
from mass_battle.core.state import *     # [Stage-1] resolver layer: morale/discipline/rout transitions
from mass_battle.core.attrition import * # [Stage-1] resolver layer: Lanchester attrition law
from mass_battle.core.contact import *   # [Stage-1] targeting + contact detection
from mass_battle.troop_types.registry import *  # [Stage-1] troop-type stats + gated roles
from mass_battle.geometry import *
from mass_battle.percell import *
from mass_battle.resolution import *
from mass_battle.orchestration import *

import mass_battle.config as _cfg
import mass_battle.core.exchange as _ce
import mass_battle.core.state as _cs
import mass_battle.core.attrition as _ca
import mass_battle.core.contact as _cc
import mass_battle.troop_types.registry as _tt
import mass_battle.geometry as _geo
import mass_battle.percell as _pc
import mass_battle.resolution as _res
import mass_battle.orchestration as _orch

# Re-export contract used by gauge_mb.py (and any external caller):
#   Subunit, Unit, run_battle, run_multi_turn_battle, run_multi_unit_battle,
#   SIDE_A_START_ROW, SIDE_B_START_ROW, plus the full mechanic surface via import *.

def _resolve(sym):
    for m in (_ce,_cs,_ca,_cc,_tt,_orch,_res,_pc,_geo,_cfg):
        if hasattr(m, sym): return getattr(m, sym)
    return None

# MECHANICS registry — name -> {fn, toggle (env var or None), source, status}
# status: WIRED | PARTIAL | STUB. Mirrors the completeness audit (designs/audit/.../mb_engine_completeness_audit.md).
MECHANICS = {
    # geometry / deployment
    "cell_layout":        {"fn":"oriented_pattern",      "toggle":None,        "source":"mass_battle_v30 §A.3b", "status":"WIRED"},
    "octagon_facing":     {"fn":"octagon_angle",         "toggle":None,        "source":"Jordan design (per-cell octagon)", "status":"WIRED"},
    "support_vector":     {"fn":"_support_along_vector", "toggle":None,        "source":"engine S4 seam", "status":"WIRED"},
    "cell_speed":         {"fn":"cell_speed",            "toggle":None,        "source":"precedents_warfare (Leuctra)", "status":"WIRED"},
    # resolution core
    "pool_roll":          {"fn":"roll_pool",             "toggle":None,        "source":"params/core.md", "status":"WIRED"},
    "degree":             {"fn":"compute_degree",        "toggle":None,        "source":"params/core.md", "status":"WIRED"},
    "sigma_net_boost":    {"fn":"_sigma_net_boost",      "toggle":"SIGMA_HEAD","source":"modifier_system_spec §2.1", "status":"WIRED"},
    "sigma_softcap":      {"fn":"_sigma_softcap",        "toggle":None,        "source":"modifier_system_spec §3.1", "status":"WIRED"},
    "morale_sigma":       {"fn":"_morale_sigma",         "toggle":"MORALE_FIX","source":"mass_battle_v30 §A.4 (du Picq)", "status":"WIRED"},
    "casualties":         {"fn":"distribute_casualties", "toggle":None,        "source":"mass_battle_v30 §A.4", "status":"WIRED"},
    # per-cell layer
    "column_grid":        {"fn":"build_column_grid",     "toggle":"PER_CELL",  "source":"derived_stats / Incr1-4", "status":"WIRED"},
    "fatigue":            {"fn":"_fatigue_sigma",        "toggle":"PER_CELL",  "source":"engine fatigue model", "status":"WIRED"},
    "defender_depth":     {"fn":"_defender_depth",       "toggle":"PER_CELL",  "source":"Jordan handoff depth-damping", "status":"WIRED"},
    "charge_shock":       {"fn":"_charge_shock_sigma",   "toggle":"PER_CELL",  "source":"mass_battle_v30 §A.8 + du Picq (Phase 3, ratified)", "status":"WIRED"},
    "envelopment_wrap":   {"fn":"_momentum_speed",       "toggle":"PC_REFUSE", "source":"Cannae/Adrianople (M3 wheel/wrap)", "status":"WIRED"},
    # orchestration / turn structure
    "assign_targets":     {"fn":"assign_targets",        "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "find_contacts":      {"fn":"find_contacts",         "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "engage":             {"fn":"resolve_engagements",   "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "cascade_order":      {"fn":"resolve_engagements_cascading","toggle":"CASCADING_ENABLED","source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "volley":             {"fn":"volley_phase",          "toggle":"VOLLEY_ENABLED","source":"mass_battle_v30 §A.7 Phase 2", "status":"WIRED"},
    "battle_turn":        {"fn":"run_battle",            "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "multi_turn":         {"fn":"run_multi_turn_battle", "toggle":None,        "source":"mass_battle_v30 §A.7", "status":"WIRED"},
    "rout":               {"fn":"rout_resolution",       "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "pursuit":            {"fn":"pursuit_damage",        "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "recall":             {"fn":"recall_check",          "toggle":None,        "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "morale_cascade":     {"fn":"discipline_check_cascade","toggle":None,      "source":"mass_battle_v30 §A.12", "status":"WIRED"},
    "between_turn_recovery":{"fn":"between_turn_recovery","toggle":None,       "source":"mass_battle_v30 §A.13", "status":"WIRED"},
    # attrition substrate (P-L) + command-only resolution (canon-structure, ED-899)
    "lanchester_attrition":{"fn":"_lanchester_strength","toggle":"LANCHESTER_ENABLED","source":"mb_lanchester_design.md §3 — linear melee / square volley (P-L)", "status":"WIRED"},
    "command_sigma_base": {"fn":"command_base_pool",   "toggle":"COMMAND_SIGMA_ENABLED","source":"ED-899 / Jordan 2026-06-02 — Command-only base; sets aside PP-233 Size pool", "status":"WIRED"},
    "command_derivation": {"fn":"derive_command",       "toggle":"COMMAND_SIGMA_ENABLED","source":"ED-899 — Command = f(Charisma primary, Cognition secondary)", "status":"WIRED"},
}

def mechanics_selftest():
    """Assert every registered mechanic resolves to a real symbol. Returns (ok, missing)."""
    missing = [name for name,spec in MECHANICS.items() if _resolve(spec["fn"]) is None]
    return (len(missing)==0, missing)

_mods = (_cfg,_ce,_cs,_ca,_cc,_tt,_geo,_pc,_res,_orch)
__all__ = sorted({n for _m in _mods for n in getattr(_m,'__all__',[])} | {"MECHANICS","mechanics_selftest"})
