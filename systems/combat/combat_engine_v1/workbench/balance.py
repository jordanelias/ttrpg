"""Variable-balancing harness (scene-combat WS-8) — the instrument the methodology runs through.

Three sweeps, each reusing the canonical fight() with an optional Class-C scratch-cfg (so a tuning pass can
measure its own effect), all position-swapped + Wilson-CI'd to the repo's parity discipline:

  1. weapon_matchup_table   — each weapon vs a uniform baseline opponent (combat_analysis §2 format).
  2. attribute_parity_table — raise ONE attribute a point, measure the marginal win-rate (combat_analysis §1).
  3. tradition_field_table  — each tradition's UNCONDITIONAL win-rate vs the field (the C1 target: flat).

Method constants (trial count, Wilson z, acceptance band) are imported from r8_parity_harness (Class-M, the
single source) — not re-declared. CLI:  python workbench/balance.py [weapon|attr|tradition|all] [n]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import random
import zlib
import wrapper, config


def _seed(key):
    """Deterministic per-cell seed (run-to-run reproducible). `hash()` is PYTHONHASHSEED-salted, so a matrix used as
    the re-baseline reference must NOT seed from it (audit finding). crc32 of the repr is stable across processes."""
    return zlib.crc32(repr(key).encode()) % 9999
from combatant import Combatant
import presets
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../tests/sim/v32-combat-balance'))  # measurement harness reaches into the FROZEN v32 validation station BY DESIGN (dev tooling; doctrine container-hygiene exclusion, ED-1085)
import r8_parity_harness as r8   # Class-M method constants: FINAL_TRIALS, WILSON_Z, BAND_LO/HI

WEAPONS = ["rapier", "arming", "longsword", "greatsword", "sabre", "dagger",
           "paired_short", "spear", "staff", "mace", "poleaxe",
           # morphology-rearch Phase C (2026-07-02): the 40 weapons added by the catalogue expansion, now
           # primitive-composed (elements/guards/mode_elements — see designs/scene/combat_engine_v1/weapons.py).
           # longsword_halfsword/estoc_halfsword excluded — auto-switch FORMS, never a starting loadout (matches
           # the existing exclusion note above for the original 11).
           "yari", "kama_yari", "dangpa", "bear_spear", "ranseur", "spetum", "partisan", "naginata", "glaive",
           "guandao", "podao", "fauchard", "bardiche", "sparr_axe", "voulge", "guisarme", "ji", "bec_de_corbin",
           "lucerne_hammer", "goedendag", "katana", "tachi", "odachi", "tsurugi", "changdao", "nandao", "jian",
           "scimitar", "pulwar", "shamshir", "szabla", "cinquedea", "flamberge", "estoc", "falchion", "rondel",
           "main_gauche", "stiletto", "misericorde", "hook_sword"]
TRADITIONS = ["none", "german", "italian", "spanish", "japanese", "chinese", "filipino", "english"]
ATTRS = ["strength", "agi", "end", "cog", "att", "spirit", "focus", "history", "disp"]


def _wilson(w, n, z=r8.WILSON_Z):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = w / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = (z * (p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def winrate(specA, specB, cfg, n, seed=0):
    """Position-swapped decisive win-rate of A vs B (cancels first-mover). Returns (p, lo, hi, decided, draws)."""
    rng = random.Random(seed)   # stdlib RNG (engine contract post ED-1085)
    aw = dec = draws = 0
    half = n // 2
    for i in range(n):
        swap = i >= half
        X = _mk(specB if swap else specA)
        Y = _mk(specA if swap else specB)
        r = wrapper.fight(X, Y, cfg, rng)
        if swap:
            r = -r
        if r == 1:
            aw += 1; dec += 1
        elif r == -1:
            dec += 1
        else:
            draws += 1
    p, lo, hi = _wilson(aw, dec)
    return p, lo, hi, dec, draws


def _mk(spec):
    kw = {k: spec[k] for k in ATTRS if k in spec}
    return Combatant(spec.get('label', '?'), weapon=spec.get('weapon', 'arming'),
                     armor=spec.get('armor', 'light'), tradition=spec.get('tradition', 'none'), **kw)


def weapon_matchup_table(cfg=None, n=600, baseline='arming'):
    cfg = cfg or config.CFG
    rows = []
    for w in WEAPONS:
        p, lo, hi, dec, _ = winrate({'weapon': w}, {'weapon': baseline}, cfg, n, seed=_seed(w))
        rows.append((w, round(100 * p, 1), round(100 * lo, 1), round(100 * hi, 1)))
    rows.sort(key=lambda r: -r[1])
    return {'baseline': baseline, 'n': n, 'rows': rows}


def attribute_parity_table(cfg=None, n=600):
    cfg = cfg or config.CFG
    rows = []
    base = {a: (4 if a in ('strength', 'agi', 'end') else (4 if a == 'disp' else 3)) for a in ATTRS}
    for a in ATTRS:
        up = dict(base); up[a] = base[a] + 1
        p, lo, hi, dec, _ = winrate(up, base, cfg, n, seed=_seed(a))
        rows.append((a, round(100 * p, 1), f"+{round(100*p-50,1)}pp"))
    rows.sort(key=lambda r: -r[1])
    return {'n': n, 'rows': rows}


def tradition_field_table(cfg=None, n=400):
    """Each tradition's unconditional win-rate averaged over the field of all traditions (mirror-checked)."""
    cfg = cfg or config.CFG
    rows = []
    for t in TRADITIONS:
        ps = []
        for opp in TRADITIONS:
            p, *_ = winrate({'weapon': 'arming', 'tradition': t}, {'weapon': 'arming', 'tradition': opp},
                            cfg, n, seed=_seed((t, opp)))
            ps.append(p)
        rows.append((t, round(100 * (sum(ps) / len(ps)), 1)))
    rows.sort(key=lambda r: -r[1])
    return {'n': n, 'rows': rows}


def tradition_context_matrix(cfg=None, contexts=('arming', 'longsword', 'rapier', 'sabre', 'spear'), n=150):
    """C1 contextual-balance test (WS-8 section 5): does the tradition ranking FLIP across weapon-contexts? For
    each context weapon, every fighter wields that weapon and we measure each tradition's field-average win-rate.
    If the leading tradition VARIES by context (each leads in some context, none is globally dominant), the
    unconditional spread is legitimate context-conditional balance — 'each fighter has a preferred paradigm' — not
    a flat-balance failure. Returns {weapon: [(tradition, win%), ... sorted]}."""
    cfg = cfg or config.CFG
    out = {}
    for wpn in contexts:
        rows = []
        for t in TRADITIONS:
            ps = []
            for opp in TRADITIONS:
                p, *_ = winrate({'weapon': wpn, 'tradition': t}, {'weapon': wpn, 'tradition': opp},
                                cfg, n, seed=_seed((wpn, t, opp)))
                ps.append(p)
            rows.append((t, round(100 * sum(ps) / len(ps), 1)))
        rows.sort(key=lambda r: -r[1])
        out[wpn] = rows
    return out


def _md_context(m):
    out = ["### Tradition x weapon-context — C1 test (does the leader FLIP across contexts?)",
           "_If each tradition leads in SOME context, the unconditional spread is context-conditional, not dominance._",
           "| context | leader | win% | runner-up | spread |", "|---|---|---|---|---|"]
    for wpn, rows in m.items():
        sp = round(rows[0][1] - rows[-1][1], 1)
        out.append(f"| {wpn} | **{rows[0][0]}** | {rows[0][1]} | {rows[1][0]} ({rows[1][1]}) | {sp}pp |")
    leaders = {rows[0][0] for rows in m.values()}
    out.append(f"\n_distinct leaders across {len(m)} contexts: **{len(leaders)}** ({', '.join(sorted(leaders))})_")
    return "\n".join(out)


def weapon_armour_matrix(cfg=None, n=600, baseline='arming', armours=('none', 'light', 'medium', 'heavy')):
    """The four-state weapon x armour matrix (the README's 'A0 unarmoured -> A3 full plate'), which the single-tier
    weapon_matchup_table did NOT actually instrument. Each weapon vs the uniform baseline with BOTH fighters at the
    SAME armour tier, swept across tiers: a weapon's win% ARC across armour is its CONTEXTUAL SIGNATURE — the
    duel-vs-battlefield principle (methodology §5) made measurable. A pure cutter collapses vs plate (the edge
    glances off); a percussion/gap-thrust weapon INVERTS (poor unarmoured, decisive vs harness). Balance here is
    NOT a flat column — it is each weapon's arc landing where its physical primitives + the armour-mitigation matrix
    (core.coupling / systems.armor_defeat_sigma) put it. Returns {'baseline','n','armours','rows':[(w, [p...],
    [(lo,hi)...]) ...]} sorted by the UNARMOURED (A0) win-rate.
    NOTE: sweeps the module-level WEAPONS list (the 11 startable weapons); `longsword_halfsword` is excluded — it is a
    derived auto-switch FORM (mit dem kurzen Schwert), never a starting loadout. Seeds are deterministic (_seed)."""
    cfg = cfg or config.CFG
    rows = []
    for w in WEAPONS:
        ps, cis = [], []
        for a in armours:
            p, lo, hi, dec, _ = winrate({'weapon': w, 'armor': a}, {'weapon': baseline, 'armor': a},
                                        cfg, n, seed=_seed((w, a)))
            ps.append(round(100 * p, 1)); cis.append((round(100 * lo, 1), round(100 * hi, 1)))
        rows.append((w, ps, cis))
    rows.sort(key=lambda r: -r[1][0])
    return {'baseline': baseline, 'n': n, 'armours': list(armours), 'rows': rows}


def _md_weapon_armour(m):
    A0, A3 = m['armours'][0], m['armours'][-1]
    hdr = " | ".join(m['armours'])
    out = [f"### Weapon x armour matrix vs {m['baseline']} (both fighters same tier, N={m['n']}/cell, sorted by {A0})",
           f"_A weapon's ARC is its contextual signature; the {A0}->{A3} swing (delta) shows whether it is a "
           f"duel weapon (falls), a battlefield/armour weapon (rises), or context-flat._",
           f"| weapon | {hdr} | {A0}->{A3} |", "|---|" + "---|" * (len(m['armours']) + 1)]
    for w, ps, _cis in m['rows']:
        delta = round(ps[-1] - ps[0], 1)
        arrow = "rises" if delta > 6 else ("falls" if delta < -6 else "flat")
        out.append(f"| {w} | " + " | ".join(f"{p}" for p in ps) + f" | {delta:+} ({arrow}) |")
    return "\n".join(out)


def _md_weapon(t):
    out = [f"### Weapon matchup vs {t['baseline']} (uniform-4, light armour, N={t['n']} position-swapped)",
           "| weapon | win% | 95% CI |", "|---|---|---|"]
    out += [f"| {w} | {p} | {lo}–{hi} |" for w, p, lo, hi in t['rows']]
    return "\n".join(out)


def _md_attr(t):
    out = [f"### Marginal attribute value (raise one point from baseline, N={t['n']})",
           "| attribute | win% | marginal |", "|---|---|---|"]
    out += [f"| {a} | {p} | {m} |" for a, p, m in t['rows']]
    return "\n".join(out)


def _md_trad(t):
    flat = max(r[1] for r in t['rows']) - min(r[1] for r in t['rows'])
    out = [f"### Tradition unconditional win-rate vs the field (arming, N={t['n']}/cell) — C1 target: flat",
           f"_spread = {round(flat,1)}pp (parity band +/-2–3pp at N~3000)_",
           "| tradition | uncond. win% |", "|---|---|"]
    out += [f"| {a} | {p} |" for a, p in t['rows']]
    return "\n".join(out)


def run_all(cfg=None, n=400):
    cfg = cfg or config.CFG
    return {'weapon': weapon_matchup_table(cfg, n), 'attr': attribute_parity_table(cfg, n),
            'tradition': tradition_field_table(cfg, max(200, n // 2))}


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    if which in ('weapon', 'all'):
        print(_md_weapon(weapon_matchup_table(n=n)) + "\n")
    if which in ('attr', 'all'):
        print(_md_attr(attribute_parity_table(n=n)) + "\n")
    if which in ('tradition', 'all'):
        print(_md_trad(tradition_field_table(n=max(200, n // 2))) + "\n")
    if which in ('context', 'all'):
        print(_md_context(tradition_context_matrix(n=max(120, n // 3))) + "\n")
    if which in ('armour', 'armor', 'matrix'):
        print(_md_weapon_armour(weapon_armour_matrix(n=n)) + "\n")
