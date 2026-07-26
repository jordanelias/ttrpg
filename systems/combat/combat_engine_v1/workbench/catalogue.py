"""catalogue.py — the complete value + mechanics catalogue for the personal-combat engine.

WHY THIS IS GENERATED, NOT WRITTEN. A hand-authored catalogue of ~50 derived quantities across 51 weapons is
~2,000 numbers that go stale on the first constant change, and this repo has already paid for hand-maintained
numbers three times (the ED-PC-0040 meta-review: "quantitative claims written faster than they were measured").
So the catalogue is a QUERY. Two halves, both sourced from the code itself:

  (1) MECHANICS — each quantity's formula/behaviour, taken from the live function's own docstring. The docstrings
      in this engine are maintained and provenance-tagged ([SIM-CALIBRATE] / [FIAT] / [ASSERTED] / ED refs), so
      quoting them beats paraphrasing them: the catalogue cannot drift from the code because it IS the code's
      own account of itself.
  (2) VALUES — every per-weapon quantity evaluated for all 51 startable weapons against a NEUTRAL fighter, plus
      the coupling matrix over all four armour tiers and the constant tables.

HONEST SCOPE. A quantity is per-weapon-tabulated only if it is a pure function of (weapon [+ neutral fighter]).
PAIRWISE quantities — anything taking (aggressor, defender) or (longer, shorter) — have no per-weapon value by
construction; they are listed in the mechanics half with their inputs and explicitly marked, never silently
dropped. The header states the partition so a reader knows what is NOT tabulated and why.

NEUTRAL FIGHTER. Attributes at the balance.py baseline (str/agi/end 4, rest 3, disp 4), no skills, no equipped
techniques, no tradition, light armour, grip 0 (open measure, as-issued), full swing room. Every value below is
therefore "this weapon in a neutral hand" — the weapon's own contribution, isolated from the build.

CLI:
    python workbench/catalogue.py            # everything (markdown to stdout)
    python workbench/catalogue.py mechanics  # the formula/docstring half only
    python workbench/catalogue.py values     # the per-weapon tables only
    python workbench/catalogue.py coupling   # the head x armour coupling matrix only
    python workbench/catalogue.py constants  # core tables + the full CFG surface
    python workbench/catalogue.py --json     # machine-readable dump of the value half
"""
import sys, os, json, inspect

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import core
import combat_systems as S
import weapon_physics as WP
import geometry as G
import weapons as W
import capabilities as CAP
from config import CFG
from combatant import Combatant

TIERS = ('none', 'light', 'medium', 'heavy')
NEUTRAL = dict(strength=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3, history=3, disp=4)


def roster():
    """The startable roster: every weapon record that is not an auto-switch FORM (records carrying a `base`)."""
    return [n for n, r in W.WEAPONS.items() if 'base' not in r]


def _fighter(name, armor='light'):
    return Combatant('x', weapon=name, armor=armor, **NEUTRAL)


def _safe(fn, *a, **k):
    """Evaluate a derivation, returning an error token if it is not defined for this weapon. A missing value is
    REPORTED, never silently coerced to 0 — a missing value and a zero value are different findings."""
    try:
        return fn(*a, **k)
    except Exception as e:
        return f"ERR:{type(e).__name__}"


def _fmt(v):
    if v is None:
        return "--"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.3f}".rstrip('0').rstrip('.') if abs(v) < 1e4 else f"{v:.3g}"
    if isinstance(v, (list, tuple, set)):
        return " ".join(sorted(str(x) for x in v))
    return str(v)


def _q(fn):
    """The function's own docstring, flattened — the mechanics text for a quantity."""
    return " ".join((inspect.getdoc(fn) or "(no docstring)").split())


# ── the per-weapon quantity registry ──────────────────────────────────────────────────────────────
# (column, group, callable(name, weapon_dict, combatant) -> value, source function whose docstring documents it)
QUANTITIES = [
    # -- L0 stored primitives (weapons.py) --
    ("hands",           "L0 stored",   lambda n, w, c: w['hands'],        None),
    ("mass_kg",         "L0 stored",   lambda n, w, c: w['mass'],         None),
    ("head_len_m",      "L0 stored",   lambda n, w, c: w['head_len'],     None),
    ("grip_len_m",      "L0 stored",   lambda n, w, c: w.get('grip_len'), None),
    ("head",            "L0 stored",   lambda n, w, c: w['head'],         None),
    # -- L1 geometry.bake() --
    ("curvature",       "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['curvature'], None),
    ("point_conc",      "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['point_concentration'], None),
    ("cross_sect",      "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['cross_section'], None),
    ("edge_keen",       "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['edge_keenness'], None),
    ("cut",             "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['cut'],       G.cut_factor),
    ("thrust",          "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['thrust'],    G.thrust_factor),
    ("gap",             "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['gap'],       None),
    ("halfsword",       "L1 geometry", lambda n, w, c: G.bake(w['geometry'])['halfsword'], G.can_halfsword_thrust),
    # -- L2 weapon_physics --
    ("heft",            "L2 physics",  lambda n, w, c: WP.heft(w),                  WP.heft),
    ("agility",         "L2 physics",  lambda n, w, c: WP.agility(w),               WP.agility),
    ("perc_auth",       "L2 physics",  lambda n, w, c: WP.percussion_authority(w),  WP.percussion_authority),
    ("punct_press",     "L2 physics",  lambda n, w, c: WP.puncture_pressure(w),     WP.puncture_pressure),
    ("handling",        "L2 physics",  lambda n, w, c: WP.handling(w),              WP.handling),
    ("hand_guard",      "L2 physics",  lambda n, w, c: WP.hand_guard(w),            WP.hand_guard),
    ("blade_guard",     "L2 physics",  lambda n, w, c: WP.blade_guard(w),           WP.blade_guard),
    ("spine",           "L2 physics",  lambda n, w, c: WP.spine(w),                 WP.spine),
    ("edge_lines",      "L2 physics",  lambda n, w, c: WP.edge_lines(w),            WP.edge_lines),
    ("grab_hazard",     "L2 physics",  lambda n, w, c: WP.grab_hazard(w),           WP.grab_hazard),
    ("edge_vibr",       "L2 physics",  lambda n, w, c: WP.edge_vibration(w),        WP.edge_vibration),
    ("distraction",     "L2 physics",  lambda n, w, c: WP.distraction(w),           WP.distraction),
    ("facing_pref",     "L2 physics",  lambda n, w, c: WP.facing_pref(w),           WP.facing_pref),
    ("hilt_mass",       "L2 physics",  lambda n, w, c: WP.hilt_assembly_mass(w),    WP.hilt_assembly_mass),
    ("rev_grip_perc",   "L2 physics",  lambda n, w, c: WP.reversed_grip_percussion(w), WP.reversed_grip_percussion),
    ("grip_choke_max",  "L2 physics",  lambda n, w, c: WP.grip_choke_max(w),        WP.grip_choke_max),
    ("grip_travel_max", "L2 physics",  lambda n, w, c: WP.grip_travel_max(w),       WP.grip_travel_max),
    ("def_parry",       "L2 physics",  lambda n, w, c: WP.defense_affinities(w)['parry'], WP.defense_affinities),
    ("def_dodge",       "L2 physics",  lambda n, w, c: WP.defense_affinities(w)['dodge'], None),
    ("def_wind",        "L2 physics",  lambda n, w, c: WP.defense_affinities(w)['wind'],  None),
    # -- L3 systems (weapon + neutral fighter) --
    ("reach_base",      "L3 systems",  lambda n, w, c: S.reach_base(c, CFG),         S.reach_base),
    ("wield_heft",      "L3 systems",  lambda n, w, c: S.wield_heft(c, CFG),         S.wield_heft),
    ("weapon_tempo",    "L3 systems",  lambda n, w, c: S.weapon_tempo(c, CFG, 0.0),  S.weapon_tempo),
    ("close_tempo",     "L3 systems",  lambda n, w, c: S.close_tempo(c, CFG, 0.0),   S.close_tempo),
    ("leverage",        "L3 systems",  lambda n, w, c: S.leverage(c, CFG),           S.leverage),
    ("recoverability",  "L3 systems",  lambda n, w, c: S.recoverability_factor(c, CFG), S.recoverability_factor),
    ("lunge_quality",   "L3 systems",  lambda n, w, c: S.lunge_quality(c, CFG),      S.lunge_quality),
    ("str_demand",      "L3 systems",  lambda n, w, c: S.str_demand(c, CFG),         S.str_demand),
    ("close_unwield",   "L3 systems",  lambda n, w, c: S.close_unwieldiness(c, CFG), S.close_unwieldiness),
    ("choke_ctrbal",    "L3 systems",  lambda n, w, c: S.choke_counterbalance(c, CFG), S.choke_counterbalance),
    ("rear_clear",      "L3 systems",  lambda n, w, c: S.rear_clearance(c, CFG),     S.rear_clearance),
    ("arrest_impulse",  "L3 systems",  lambda n, w, c: S.arrest_impulse(c, CFG),     S.arrest_impulse),
    ("affords_hs",      "L3 systems",  lambda n, w, c: S.affords_halfsword(w),       S.affords_halfsword),
    ("afforded_heads",  "L3 systems",  lambda n, w, c: sorted(S.afforded_heads(w)),  S.afforded_heads),
    ("adef_cap",        "L3 systems",  lambda n, w, c: core.adef_cap(w, CFG),        core.adef_cap),
    ("thrust_auth",     "L3 systems",  lambda n, w, c: core.thrust_authority(w['head_len']), core.thrust_authority),
]

# PAIRWISE by construction — no per-weapon value exists. Listed, never silently dropped.
PAIRWISE = [
    S.reach_sigma, S.bind_sigma, S.armor_defeat_sigma, S.reach_threat, S.represent_measure_p,
    S.stophit_sigma, S.pursuit_sigma, S.true_time_edge, S.approach_displace, S.reopen_prob,
    S.disengage_attempt_p, S.disengage_clean_p, S.tempo_pressure, S.initiative_sigma,
    S.init_emphasis_sigma, S.mode_sigma, S.read_contest, S.commit_depth, S.assemble_net_sigma,
    S.attack_sigma, S.defence_sigma, S.overcommit_exposure, S.counter_select, S.indes_steal_amount,
    S.percussion_stagger, S.close_rate, S.approach_step, S.legibility, S.select_mode,
    core.strike, core.damage, core.resolve, core.coupling, core.cut_thrust_arm,
]

# Fighter-dependent (not weapon-dependent) — the BUILD surface, catalogued for completeness.
FIGHTER_ONLY = [
    S.reading, S.reflex, S.balance_eff, S.anti_overcommit, S.consistency, S.mental_fatigue,
    S.poise_regen, S.poise_factor, S.disp_lean, S.stance_stability, S.handling_penalty,
    S.act_cost, S.init_hold_decay, S.init_overcommit_loss, S.init_steal_factor,
    S.grip_target, S.facing_target, S.range_utilization, core.resolution_pool, core.degree,
]


def _groups():
    seen, out = set(), []
    for _c, g, _f, _s in QUANTITIES:
        if g not in seen:
            seen.add(g); out.append(g)
    return out


# ── emitters ──────────────────────────────────────────────────────────────────────────────────────
def values(as_json=False):
    names = roster()
    data = {n: {col: _safe(fn, n, W.WEAPONS[n], _fighter(n)) for col, _g, fn, _s in QUANTITIES}
            for n in names}
    if as_json:
        return data
    out = []
    for g in _groups():
        cols = [col for col, grp, _f, _s in QUANTITIES if grp == g]
        out.append(f"\n### {g} — per-weapon values (neutral fighter, grip 0, full room)\n")
        out.append("| weapon | " + " | ".join(cols) + " |")
        out.append("|---" * (len(cols) + 1) + "|")
        for n in sorted(names):
            out.append(f"| {n} | " + " | ".join(_fmt(data[n][col]) for col in cols) + " |")
    return "\n".join(out)


def coupling_matrix():
    """Damage coupling for every afforded head x armour tier, plus which head select_mode actually picks.

    This is the table that exposes the A7 finding: the native cut tokens return an IDENTICAL coupling for every
    weapon at a given tier, because core.coupling ignores `eff` for straight_cut/curved_cut."""
    out = ["\n### Coupling matrix — `core.coupling` per afforded head x armour tier\n",
           "_`selected at` lists the tiers where `select_mode` actually picks that head. Selection can differ "
           "from the highest raw coupling: the comparator also applies `close_efficacy` and the T_vuln exposure "
           "discount (see A7b in the defect register)._\n",
           "| weapon | head | none | light | medium | heavy | selected at |",
           "|---|---|---|---|---|---|---|"]
    for n in sorted(roster()):
        w = W.WEAPONS[n]
        c = _fighter(n)
        heads = S.afforded_heads(w)
        sel = {}
        for t in TIERS:
            r = _safe(S.select_mode, c, t, True, CFG, measure_gap=0.0)
            sel[t] = r[1] if isinstance(r, tuple) else r
        for hd, v in sorted(heads.items()):
            cells = [_fmt(_safe(core.coupling, hd, t,
                                perc=v[3] if v[3] is not None else core.PERC_AUTH_REF,
                                gap_prec=v[2], eff=v[0],
                                thrust_auth=core.thrust_authority(w['head_len']),
                                eff_cut=(v[6] if len(v) > 6 else None),
                                eff_thrust=(v[7] if len(v) > 7 else None)))
                     for t in TIERS]
            picked = " ".join(t for t in TIERS if sel[t] == hd) or "—"
            out.append(f"| {n} | {hd} | " + " | ".join(cells) + f" | {picked} |")
    return "\n".join(out)


def mechanics():
    out = ["\n## Mechanics — every derivation, in its own words\n",
           "_Each entry is the live function's own docstring. Provenance tags ([SIM-CALIBRATE] / [FIAT] / "
           "[ASSERTED] / ED refs) are the code's, not this document's._\n"]
    for g in _groups():
        out.append(f"\n### {g}\n")
        for col, grp, _fn, src in QUANTITIES:
            if grp != g or src is None:
                continue
            out.append(f"- **`{col}`** — `{src.__module__}.{src.__name__}`\n  > {_q(src)}\n")
    out.append("\n### Pairwise quantities — NO per-weapon value exists (by construction)\n")
    out.append("_These take two fighters (aggressor/defender, longer/shorter) or a full strike context. They are "
               "listed so the catalogue's coverage is honest: they are excluded from the value tables because a "
               "single weapon has no value for them, not because they were overlooked._\n")
    for f in PAIRWISE:
        out.append(f"- **`{f.__module__}.{f.__name__}({', '.join(inspect.signature(f).parameters)})`**\n  > {_q(f)}\n")
    out.append("\n### Fighter-dependent quantities (the BUILD surface, not the weapon)\n")
    for f in FIGHTER_ONLY:
        out.append(f"- **`{f.__module__}.{f.__name__}({', '.join(inspect.signature(f).parameters)})`**\n  > {_q(f)}\n")
    return "\n".join(out)


def constants():
    out = ["\n## Constant tables (`core.py`)\n"]
    for nm in ('HEAD_MODE', 'DELIVERY', 'RESIST', 'TIER2MAT', 'GAP_EXPOSURE', 'PEN_THR', 'QUAL',
               'COVERAGE_GAP', 'DECISIVE_OB', 'PERC_AUTH_REF', 'PERC_AUTH_REF_SOFT', 'CUT_AUTH_REF',
               'THRUST_AUTH_REF', 'GAP_PREC_REF', 'PEN_DEFICIT_K'):
        if hasattr(core, nm):
            out.append(f"- **`core.{nm}`** = `{getattr(core, nm)}`")
    out.append("\n## Affordance gates (`capabilities.py`)\n")
    names = sorted(roster())
    for k, v in CAP.CAPABILITIES.items():
        allowed = [n for n in names if CAP.allowed(k, n)]
        out.append(f"- **`{k}`** @ `{v['node']}` — **{len(allowed)}/{len(names)}** weapons\n"
                   f"  - needs: {v['needs']}\n"
                   f"  - allows: {', '.join(allowed)}\n")
    out.append("\n## Tunable surface (`config.CFG`)\n")
    out.append(f"_{len(CFG)} entries. Class-C (calibrated against the harness, not canon) unless the code tags "
               f"them otherwise._\n")
    out.append("| constant | value |")
    out.append("|---|---|")
    for k in sorted(CFG):
        out.append(f"| `{k}` | `{CFG[k]}` |")
    return "\n".join(out)


def header():
    return (f"# Personal-Combat Value & Mechanics Catalogue (GENERATED)\n\n"
            f"**Generated by** `systems/combat/combat_engine_v1/workbench/catalogue.py` — **do not hand-edit.**\n"
            f"Regenerate with `python workbench/catalogue.py > <path>`.\n\n"
            f"**Neutral fighter:** str/agi/end 4, all else 3, disp 4, no skills, no techniques, no tradition, "
            f"light armour, grip 0 (as-issued), full swing room. Values are the weapon's own contribution, "
            f"isolated from the build.\n\n"
            f"**Roster:** {len(roster())} startable weapons (auto-switch half-sword FORMS excluded). "
            f"**Per-weapon quantities:** {len(QUANTITIES)}. "
            f"**Pairwise (no per-weapon value by construction):** {len(PAIRWISE)}. "
            f"**Fighter-dependent:** {len(FIGHTER_ONLY)}. "
            f"**Tunables:** {len(CFG)}.\n\n"
            f"`--` means the derivation is undefined for that weapon; it is never coerced to 0 "
            f"(a missing value and a zero value are different findings). `ERR:*` means the derivation raised.\n")


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    if '--json' in sys.argv:
        print(json.dumps(values(as_json=True), indent=1, default=str)); sys.exit(0)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    print(header())
    if mode in ('all', 'mechanics'):
        print(mechanics())
    if mode in ('all', 'values'):
        print("\n## Values — every per-weapon quantity\n")
        print(values())
    if mode in ('all', 'coupling'):
        print(coupling_matrix())
    if mode in ('all', 'constants'):
        print(constants())
