"""Class-aware engine tuning surface for the workbench (WS-6, panel 1).

Aggregates the engine's parameters into one place, tagged by PROVENANCE CLASS so the workbench can guard
what must not be casually tuned and separate what is method-not-balance:

  A  CANONICAL    — params/core.md / m1 / r8 anchors (d10 EV/sigma, TN, decisive Ob, the 18-pt budget).
                    READ-ONLY in the workbench; changing these is a canon decision, not a tuning pass.
  B  SIM-SEED     — modifier_system_spec sigma-levels and soft-cap (m1). Tunable, not canonical.
  C  TUNABLE      — the live combat knobs (config.CFG) + the r8 per-point dsig seeds. The main surface.
  M  METHOD       — statistics, NOT game balance (trial counts, Wilson z). Shown apart.

Editing model (your decision: "scratch presets, promote on ratify"): the workbench never writes the
canonical files. A run applies a named SCRATCH OVERLAY onto a copy of config.CFG (fight() already takes a
cfg), so nothing global mutates. promote_diff() renders the overlay as a reviewable patch + a ledger stub;
the actual canonical write stays a deliberate, ratified step (Class A can never be in an overlay)."""
import sys, os, json, copy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import config
import core
import m1_dice_sigma_core as m1

try:
    import r8_parity_harness as r8
except Exception:
    r8 = None

_PRESET_DIR = os.path.join(os.path.dirname(__file__), 'presets')


def param_surface():
    """Return the class-aware parameter surface for the tuning panel."""
    A = {
        'per_die_mean_TN7': m1.PER_DIE[7][0],
        'per_die_sigma_TN7': m1.PER_DIE[7][1],
        'TN_standard': m1.TN_STANDARD,
        'decisive_Ob': core.DECISIVE_OB,
    }
    if r8 is not None:
        A.update(attr_average=r8.ATTR_AVG, attr_creation_max=r8.ATTR_MAX, attr_budget=r8.EXPECTED_BUDGET)
    B = {
        'sigma_minor': m1.LEVEL_SIGMA['minor'], 'sigma_moderate': m1.LEVEL_SIGMA['moderate'],
        'sigma_strong': m1.LEVEL_SIGMA['strong'], 'sigma_major': m1.LEVEL_SIGMA['major'],
        'soft_cap_ceiling': m1.M_MAX, 'sigma_n_coeff': m1.SIGMA_N_COEFF,
    }
    C = {k: v for k, v in config.CFG.items() if isinstance(v, (int, float))}
    M = {}
    if r8 is not None:
        M = {'opt_trials': r8.OPT_TRIALS, 'final_trials': r8.FINAL_TRIALS, 'wilson_z': r8.WILSON_Z,
             'band_lo': r8.BAND_LO, 'band_hi': r8.BAND_HI}
    return {
        'A': {'label': 'Canonical (read-only)', 'editable': False, 'params': A},
        'C': {'label': 'Tunable combat knobs (config.CFG)', 'editable': True, 'params': C},
        'B': {'label': 'Sigma-space sim-seeds (m1)', 'editable': True, 'params': B},
        'M': {'label': 'Method — not game balance', 'editable': False, 'params': M},
    }


def effective_cfg(overrides=None):
    """A copy of config.CFG with Class-C overrides applied. Only keys already in CFG are accepted (an unknown
    key is a typo, not a new mechanic — rejected). Never mutates the module global."""
    cfg = copy.deepcopy(config.CFG)
    bad = []
    for k, v in (overrides or {}).items():
        if k in cfg:
            cfg[k] = type(cfg[k])(v) if isinstance(cfg[k], (int, float)) else v
        else:
            bad.append(k)
    if bad:
        raise KeyError(f"unknown config key(s) (workbench rejects new knobs): {bad}")
    return cfg


def save_scratch(name, overrides):
    os.makedirs(_PRESET_DIR, exist_ok=True)
    path = os.path.join(_PRESET_DIR, f"{name}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(overrides, f, indent=2, sort_keys=True)
    return path


def load_scratch(name):
    path = os.path.join(_PRESET_DIR, f"{name}.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def promote_diff(overrides):
    """Render the scratch overlay as a reviewable patch against config.CFG + a ledger stub. Does NOT write
    anything — promotion to canon is a deliberate, ratified step (the workbench only proposes)."""
    base = config.CFG
    rows = []
    for k in sorted(overrides):
        if k in base and base[k] != overrides[k]:
            rows.append(f"  config.CFG['{k}']: {base[k]} -> {overrides[k]}")
    body = "\n".join(rows) if rows else "  (no changes vs current config.CFG)"
    ledger_stub = {
        "kind": "combat-tuning-promotion",
        "target": "designs/scene/combat_engine_v1/config.py (CFG)",
        "overrides": {k: overrides[k] for k in sorted(overrides) if k in base},
        "note": "PROPOSED via workbench scratch preset; ratify before writing to config.py (Class-C seeds).",
    }
    return {"patch": f"Proposed Class-C tuning patch:\n{body}", "ledger_stub": ledger_stub}


if __name__ == '__main__':
    s = param_surface()
    for cls in ('A', 'B', 'C', 'M'):
        print(f"[{cls}] {s[cls]['label']}: {len(s[cls]['params'])} params (editable={s[cls]['editable']})")
    cfg = effective_cfg({'ATTACKER_BIAS': 0.20})
    print("effective_cfg override OK: ATTACKER_BIAS =", cfg['ATTACKER_BIAS'], "(base", config.CFG['ATTACKER_BIAS'], ")")
