#!/usr/bin/env python3
"""Partition the degree-of-success ladders into behavioural equivalence classes.

WHY. `audit/2026-08-11-divergence-audit` §3.1 reports 16 producers, 6 vocabularies and 5
incompatible Overwhelming formulas, and the merged plan holds the "which convention is
canonical" ruling (#0) as the gate on the whole degree family. But "16 producers" is a count of
CODE SITES, not of DECISIONS. Two sites that spell the same bands differently are a rename; two
that put the bands in different places are a design question. Only the second kind needs a
ruling, and nothing had measured which was which.

WHAT THIS MEASURES. Every ladder that is a function of (net, ob) is evaluated over the integer
domain and its output normalised to an ORDINAL BAND (0 Failure .. 3 Overwhelming), which strips
spelling entirely. Ladders that produce identical band surfaces are then one decision, however
many ways they are spelled.

THE FUNCTIONS ARE IMPORTED, NOT TRANSCRIBED. Re-typing each ladder here would measure my copy
and agree with itself — the ED-IN-0132 F1 defect ("a claim's guard was weaker than the claim,
and the two were weak in the SAME way"). Where a module cannot be imported cleanly its ladder is
REPORTED AS EXCLUDED rather than reconstructed.

Run: python3 audit/2026-08-12-degree-vocabulary-census/degree_census.py
"""
import importlib.util
import itertools
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, REPO)

# Ordinal bands. `opposing` has only three; its 'Meets' is the SUCCESS band by its own docstring.
FAIL, PARTIAL, SUCCESS, OVER = 0, 1, 2, 3
VOCAB = {
    'failure': FAIL, 'fail': FAIL, 'Failure': FAIL,
    'partial': PARTIAL, 'Partial': PARTIAL,
    'success': SUCCESS, 'Success': SUCCESS, 'Meets': SUCCESS,
    'overwhelming': OVER, 'Overwhelming': OVER,
}


def norm(v):
    """Any vocabulary -> ordinal band. Unknown spellings raise rather than defaulting."""
    if isinstance(v, int) and not isinstance(v, bool):
        return v
    s = getattr(v, 'value', v)
    if s in VOCAB:
        return VOCAB[s]
    raise KeyError(f'unmapped degree label {v!r}')


def _load(rel, name):
    path = os.path.join(REPO, rel)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


LADDERS, EXCLUDED = {}, {}


def register(label, rel, loader):
    try:
        LADDERS[label] = loader()
    except Exception as e:                                   # noqa: BLE001
        EXCLUDED[label] = f'{rel}: {type(e).__name__}: {e}'


# ── canon ──────────────────────────────────────────────────────────────────────────────
def _canon():
    m = _load('engine/autoload/dice_engine.py', 'dice_engine_probe')
    return lambda net, ob: norm(m.degree_from_net(net, ob))


register('canon dice_engine:94', 'engine/autoload/dice_engine.py', _canon)


def _threadwork_ops():
    m = _load('systems/threadwork/sim/operations.py', 'tw_ops_probe')
    return lambda net, ob: norm(m._compute_degree(net, ob))


register('threadwork operations:134 (additive ob+3)',
         'systems/threadwork/sim/operations.py', _threadwork_ops)


def _threadwork_opposing():
    m = _load('systems/threadwork/sim/opposing.py', 'tw_opp_probe')
    return lambda net, ob: norm(m._degree_label(net, ob))


register('threadwork opposing:87 (3 bands, Meets)',
         'systems/threadwork/sim/opposing.py', _threadwork_opposing)


def _faction():
    m = _load('systems/factions/sim/faction_action.py', 'fa_probe')
    # ob is PRE-SUBTRACTED at the call sites (:520 `net = _successes(pool, rng) - ob`),
    # so to compare on the shared (net, ob) domain the same subtraction is applied here.
    return lambda net, ob: norm(m._degree(net - ob))


register('faction_action:97 (ob pre-subtracted)',
         'systems/factions/sim/faction_action.py', _faction)


def _mb_canon():
    sys.path.insert(0, os.path.join(REPO, 'tests', 'sim'))
    m = _load('tests/sim/mass_battle/resolution.py', 'mb_res_probe')
    return lambda net, ob: norm(m.compute_degree(net, ob))


register('mass_battle resolution:89 (J2 canon, eps)',
         'tests/sim/mass_battle/resolution.py', _mb_canon)


def _mb_twin():
    # By-path loading trips a circular import (units <-> massbattle). Importing it as the
    # package module it really is lets Python resolve the cycle the normal way.
    import importlib
    m = importlib.import_module('systems.mass_battle.sim.massbattle')
    return lambda net, ob: norm(m.compute_degree(net, ob))


register('massbattle:640 (twin, no eps)',
         'systems/mass_battle/sim/massbattle.py', _mb_twin)


def _combat():
    E = os.path.join(REPO, 'systems', 'combat', 'combat_engine_v1')
    sys.path.insert(0, E)
    m = _load('systems/combat/combat_engine_v1/core.py', 'combat_core_probe')
    return lambda net, ob: norm(m.degree(net, ob))


register('combat core:57 (continuous, -0.5)',
         'systems/combat/combat_engine_v1/core.py', _combat)


def _fork():
    m = _load('skills/valoria-dice-model/valoria_dice.py', 'vd_probe')
    return lambda net, ob: norm(m.classify_outcome(net, ob))


register('valoria_dice:45 (FORK, Ob-10)', 'skills/valoria-dice-model/valoria_dice.py', _fork)

# ── the three inline additive `ob+3` sites are NOT separate ladders ─────────────────────
# mass_seizure:264, collective:166 and knots:226 are inline copies of the SAME rule as
# threadwork/operations:134. They are counted in the "sites" column, not as distinct decisions.
INLINE_COPIES_OF = {'threadwork operations:134 (additive ob+3)':
                    ['systems/factions/sim/mass_seizure.py:264',
                     'systems/threadwork/sim/collective.py:166',
                     'systems/fieldwork/sim/knots.py:226']}

NETS = range(-4, 26)
OBS = range(1, 21)
INT_DOMAIN = [(n, o) for n in NETS for o in OBS]

# THE FRACTIONAL DOMAIN IS NOT OPTIONAL, and leaving it out produced a WRONG ANSWER on the
# first run of this instrument. On integers alone, `combat core:57` groups with the two
# mass-battle ladders into one equivalence class — because a -0.5 continuity correction is
# INVISIBLE at integer nets, which is precisely the domain where it does nothing. The combat
# resolver is continuous (`roll_net_continuous`), so integers are the one domain it is never
# actually evaluated on. Quarter steps split the class: combat diverges from canon in 5.6% of
# cells, first at net=0.25 ob=1. A class computed on the wrong domain is a merge recommendation
# that silently changes behaviour — the exact defect this census exists to prevent.
FRAC_DOMAIN = [(i / 4, o) for i in range(-8, 81) for o in range(1, 11)]
DOMAIN = INT_DOMAIN + FRAC_DOMAIN


def surface(fn):
    out = {}
    for n, o in DOMAIN:
        try:
            out[(n, o)] = fn(n, o)
        except Exception as e:                               # noqa: BLE001
            out[(n, o)] = f'ERR:{type(e).__name__}'
    return out


def main():
    print('=' * 78)
    print('DEGREE-LADDER BEHAVIOURAL EQUIVALENCE CENSUS')
    print(f'domain: {len(INT_DOMAIN)} integer cells + {len(FRAC_DOMAIN)} quarter-step cells '
          f'= {len(DOMAIN)} total; vocabulary normalised to ordinal bands')
    print('=' * 78)

    if EXCLUDED:
        print('\nEXCLUDED (could not import — reported, not reconstructed):')
        for k, v in EXCLUDED.items():
            print(f'  {k}\n      {v}')

    surfaces = {k: surface(f) for k, f in LADDERS.items()}
    print(f'\n{len(surfaces)} ladder(s) evaluated.\n')

    # equivalence classes over the whole surface
    classes = []
    for name, s in surfaces.items():
        for cls in classes:
            if surfaces[cls[0]] == s:
                cls.append(name)
                break
        else:
            classes.append([name])

    print('-' * 78)
    print(f'EQUIVALENCE CLASSES: {len(classes)}  (from {len(surfaces)} importable ladders)')
    print('-' * 78)
    for i, cls in enumerate(classes, 1):
        print(f'\n  CLASS {i}:')
        for n in cls:
            print(f'      {n}')
            for extra in INLINE_COPIES_OF.get(n, []):
                print(f'         + inline copy: {extra}')

    # DOMAIN SENSITIVITY, reported rather than hidden: a class that exists on one domain and
    # not the other is a merge that would change behaviour where the code actually runs.
    def partition(cells):
        cls = []
        for name in surfaces:
            sub = {k: surfaces[name][k] for k in cells}
            for c in cls:
                if {k: surfaces[c[0]][k] for k in cells} == sub:
                    c.append(name)
                    break
            else:
                cls.append([name])
        return cls

    ints, fracs = partition(INT_DOMAIN), partition(FRAC_DOMAIN)
    print(f'\n  integer domain alone : {len(ints)} class(es)')
    print(f'  fractional alone     : {len(fracs)} class(es)')
    print(f'  combined (the answer): {len(classes)} class(es)')
    if len(ints) != len(classes):
        print('  ⚠ the integer domain UNDER-COUNTS: a continuity correction is invisible there.')

    # pairwise disagreement, and WHERE it starts
    print('\n' + '-' * 78)
    print('PAIRWISE DISAGREEMENT (cells differing / total, and the lowest-ob example)')
    print('-' * 78)
    names = list(surfaces)
    for a, b in itertools.combinations(names, 2):
        diff = [(k, surfaces[a][k], surfaces[b][k])
                for k in DOMAIN if surfaces[a][k] != surfaces[b][k]]
        if not diff:
            print(f'\n  IDENTICAL  {a}\n          == {b}')
            continue
        (n, o), va, vb = sorted(diff, key=lambda t: (t[0][1], t[0][0]))[0]
        pct = 100.0 * len(diff) / len(DOMAIN)
        print(f'\n  {len(diff):4d}/{len(DOMAIN)} ({pct:4.1f}%)  {a}\n'
              f'                    vs {b}'
              f'\n        first divergence: net={n} ob={o} -> {va} vs {vb}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
