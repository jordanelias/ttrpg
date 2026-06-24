"""
stress_matrix.py — comprehensive one-factor-at-a-time (OFAT) stress matrix for personal combat.

Tests, IN ISOLATION with all else controlled, the marginal effect of:
  BLOCK 1  every character ATTRIBUTE (9), swept 1..7 vs a uniform-4 baseline.
  BLOCK 2  every DERIVED SCORE/STATISTIC, scaled x0.5 / x1.5 on one fighter, attributes held equal.
  BLOCK 3  every STATE-GRAPH COMPONENT (approach -> disengage), ABLATED, across a reference matchup panel.

Engine: the CANONICAL combat_engine_v1 (staged copy in _engine/ with two inert per-fighter isolation
hooks — derived_scale['pool'|'health'] — default empty so the mirror stays 50/50). Resolver d_sigma;
pool=max(5,History+6); additive-coupled damage x1.55; ED-1041 bilateral-Ob wounds.

Method: each cell = N fights, attacker/defender positions SWAPPED to cancel the first-mover edge, a fresh
seeded RNG per cell (reproducible). Primary metric = win% of the isolated fighter (Block 1/2) or the
matchup result delta vs the full engine (Block 3). max_bouts controls draw resolution (default 40).

Usage:  python stress_matrix.py [--n N] [--mb MAX_BOUTS] [--smoke] [--block 1,2,3] [--out results.json]
"""
import sys, os, json, copy, argparse, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests", "sim", "v32-combat-balance"))   # r1/r8/m1 substrate
sys.path.insert(0, os.path.join(HERE, "_engine"))                              # staged combat_engine_v1

import numpy as np
import config as C
import core, systems as S, tradition as TR
import wrapper
from combatant import Combatant

BASE = dict(strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, disp=4,
            weapon="arming", armor="light", tradition="none")
ATTRS = ["strength", "agi", "end", "cog", "att", "spirit", "focus", "history", "disp"]
SEED = 20260623


def mk(label, **ov):
    k = dict(BASE); k.update(ov)
    return Combatant(label, **k)


def _run(makeA, makeB, cfg, n, mb, seed):
    """A vs B, then swapped, returns dict win/loss/draw for A (the first builder)."""
    rng = np.random.default_rng(seed)
    aw = al = ad = 0
    for _ in range(n):
        r = wrapper.fight(makeA(), makeB(), cfg=cfg, rng=rng, max_bouts=mb)
        if r == 1: aw += 1
        elif r == -1: al += 1
        else: ad += 1
    for _ in range(n):                                   # swap positions: A is now the 2nd arg
        r = wrapper.fight(makeB(), makeA(), cfg=cfg, rng=rng, max_bouts=mb)
        if r == -1: aw += 1
        elif r == 1: al += 1
        else: ad += 1
    tot = 2 * n
    return dict(win=round(100 * aw / tot, 1), loss=round(100 * al / tot, 1), draw=round(100 * ad / tot, 1))


# ───────────────────────── BLOCK 1 — ATTRIBUTES ─────────────────────────
def block1_attributes(n, mb):
    rows = {}
    for a in ATTRS:
        rows[a] = {}
        for lvl in range(1, 8):
            res = _run(lambda a=a, lvl=lvl: mk("A", **{a: lvl}), lambda: mk("B"), C.CFG, n, mb, SEED)
            rows[a][lvl] = res["win"]
    return rows


# ───────────────────────── BLOCK 2 — DERIVED SCORES ─────────────────────────
# (a) derived scores reachable as a systems/core function whose FIRST arg is the actor → scale for label 'A'.
DERIVED_FNS = [
    ("resolution_pool*", None),   # special: via derived_scale['pool']
    ("health_full*", None),       # special: via derived_scale['health']
    ("reading", (S, "reading")), ("reflex", (S, "reflex")), ("reach_base", (S, "reach_base")),
    ("weapon_tempo", (S, "weapon_tempo")), ("leverage", (S, "leverage")), ("balance_eff", (S, "balance_eff")),
    ("conc_max", (S, "conc_max")), ("stamina_max", (S, "stamina_max")), ("str_demand", (S, "str_demand")),
    ("handling_penalty", (S, "handling_penalty")), ("legibility", (S, "legibility")),
    ("initiative_sigma", (S, "initiative_sigma")),
]

def _wrap_actor_fn(mod, name, factor):
    orig = getattr(mod, name)
    def patched(*args, **kw):
        v = orig(*args, **kw)
        c = args[0]
        if getattr(c, "label", None) == "A":
            return v * factor
        return v
    patched._orig = orig
    return patched

def block2_derived(n, mb):
    rows = {}
    for label, spec in DERIVED_FNS:
        rows[label] = {}
        for factor in (0.5, 1.5):
            if spec is None:                                   # pool / health via derived_scale hook
                ch = "pool" if "pool" in label else "health"
                makeA = lambda ch=ch, factor=factor: _scaled("A", {ch: factor})
                res = _run(makeA, lambda: mk("B"), C.CFG, n, mb, SEED)
            else:
                mod, name = spec
                orig = getattr(mod, name)
                setattr(mod, name, _wrap_actor_fn(mod, name, factor))
                try:
                    res = _run(lambda: mk("A"), lambda: mk("B"), C.CFG, n, mb, SEED)
                finally:
                    setattr(mod, name, orig)                   # always restore
            rows[label][factor] = res["win"]
    return rows

def _scaled(label, dscale):
    c = mk(label); c.derived_scale = dict(dscale); return c


# ───────────────────────── BLOCK 3 — STATE-GRAPH COMPONENTS ─────────────────────────
# Reference matchup panel (so a component's effect is visible where it should act).
PANEL = {
    "mirror":  (lambda: mk("A"),                      lambda: mk("B")),                       # fairness/draws
    "reach":   (lambda: mk("A", weapon="rapier"),     lambda: mk("B", weapon="arming")),      # measure
    "skill":   (lambda: mk("A", history=7),           lambda: mk("B", history=4)),            # pool/initiative
    "armour":  (lambda: mk("A", weapon="mace"),       lambda: mk("B", armor="heavy")),        # armour-defeat
}

# component -> cfg overrides that NEUTRALIZE it (approach -> closed -> outcome -> disengage)
ABLATIONS = {
    # approach phase
    "stop_hit":          {"STOPHIT_CHANCE": 0.0},
    "approach_displace": {"APPROACH_DISPLACE_K": 0.0, "APPROACH_DISPLACE_MAX": 0.0},
    "reach_reopen":      {"REOPEN_K": 0.0, "REOPEN_MAX": 0.0},
    "push_shove":        {"PUSH_AVAIL_P": 0.0},
    "standing_reach":    {"REACH_FRAC": 0.0},
    # closed exchange — read / initiative / commit
    "attacker_bias":     {"ATTACKER_BIAS": 0.0},
    "initiative_edge":   {"INIT_SIGMA_K": 0.0},
    "indes_steal":       {"INIT_STEAL_INDES": 0.0},
    "single_counter":    {"COUNTER_SELECT_BASE": 0.0},
    "overcommit":        {"COMMIT_EXPOSE_K": 0.0},
    "legibility":        {"LEGIB_SWING": 1.0, "LEGIB_THRUST": 1.0, "LEGIB_LUNGE": 0.0, "LEGIB_COMMIT_K": 0.0},
    "mental_fatigue":    {"MENTAL_FAT_READ_K": 0.0, "MENTAL_FAT_DEF_K": 0.0, "FOCUS_MENTAL_K": 0.0},
    "consistency_focus": {"FOCUS_CONSISTENCY_K": 0.0},
    "handling":          {"HANDLE_K": 0.0, "FATIGUE_HANDLE_K": 0.0},
    "tempo_fatigue":     {"TEMPO_FATIGUE_K": 0.0},
    "commit_disc":       {"FOOT_COMMIT_DISC_K": 0.0, "FOOT_STANCE_K": 0.0},
    # armour / wounds / stamina
    "armour_defeat":     {"ADEF_W": {"none": 0.0, "light": 0.0, "medium": 0.0, "heavy": 0.0}},
    "wound_ob":          {"WOUND_ATK_OB": 0.0, "WOUND_DEF_OB": 0.0},
    "oob":               {"OOB": 0},
    # outcome mapping / post-strike
    "riposte":           {"RIPOSTE_ON_FAIL": 0.0, "RIPOSTE_ON_NEUTRALIZE": 0.0},
    "bind":              {"WIND_BIND_P": 0.0, "BIND_HIT_P": 0.0},
    "displace_inside":   {"DISPLACE_P": 0.0},
    "poise_kuzushi":     {"POISE_BREAK_OVERCOMMIT": 0.0, "POISE_BREAK_BIND": 0.0, "POISE_BREAK_HIT": 0.0},
    "feint":             {"FEINT_ENABLE": False},
    "disrupt_focus":     {"DISRUPT_K": 0.0},
    # disengage / turn structure
    "burst":             {"BURST_MAX": 1},
}

def _cfg_with(over):
    cfg = copy.deepcopy(C.CFG)
    for k, v in over.items():
        cfg[k] = v
    return cfg

def block3_state_graph(n, mb):
    full = {name: _run(a, b, C.CFG, n, mb, SEED) for name, (a, b) in PANEL.items()}
    rows = {"_full_baseline": {m: full[m]["win"] for m in PANEL}}
    for comp, over in ABLATIONS.items():
        cfg = _cfg_with(over)
        rows[comp] = {}
        for m, (a, b) in PANEL.items():
            res = _run(a, b, cfg, n, mb, SEED)
            rows[comp][m] = round(res["win"] - full[m]["win"], 1)        # Δwin vs full engine (A's win%)
            if m == "mirror":
                rows[comp]["mirror_draw_delta"] = round(res["draw"] - full["mirror"]["draw"], 1)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--mb", type=int, default=40)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--block", default="1,2,3")
    ap.add_argument("--out", default=os.path.join(HERE, "results.json"))
    args = ap.parse_args()
    n = 30 if args.smoke else args.n
    blocks = set(args.block.split(","))

    # sanity: instrumentation inert (mirror ~50, draw low at mb)
    mir = _run(lambda: mk("A"), lambda: mk("B"), C.CFG, n, args.mb, SEED)
    out = {"meta": {"n_per_position": n, "max_bouts": args.mb, "seed": SEED,
                    "baseline": {k: BASE[k] for k in ATTRS} | {"weapon": "arming", "armor": "light"},
                    "mirror_sanity": mir}}
    print(f"[sanity] mirror win={mir['win']} draw={mir['draw']}  (expect ~50 / low)")

    if "1" in blocks:
        print("[block 1] attributes ..."); out["block1_attributes"] = block1_attributes(n, args.mb)
        json.dump(out, open(args.out, "w"), indent=2)
    if "2" in blocks:
        print("[block 2] derived scores ..."); out["block2_derived"] = block2_derived(n, args.mb)
        json.dump(out, open(args.out, "w"), indent=2)
    if "3" in blocks:
        print("[block 3] state-graph components ..."); out["block3_state_graph"] = block3_state_graph(n, args.mb)
        json.dump(out, open(args.out, "w"), indent=2)

    json.dump(out, open(args.out, "w"), indent=2)
    print(f"[done] wrote {args.out}")


if __name__ == "__main__":
    main()
