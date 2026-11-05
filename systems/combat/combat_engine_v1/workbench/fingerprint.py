"""Module fingerprint (PC-11): a MEASUREMENT of the personal-combat module's seeded behaviour, not a guard.

Run it before an edit to `modules/combat/` and again after: if the edit was meant to move no fight, the two
IDENTITY HASHES are equal. It asserts nothing about the engine and fails nothing; it prints.

  python systems/combat/combat_engine_v1/workbench/fingerprint.py [--fights N] [--json]

WHAT IT HASHES
  identity hash  : sha256 over, for each of the 3,000 seeded fights (12 matchup families x 250), the record
                   (result, A.damage, B.damage, wounds, felled) serialised with sorted keys. `A.damage` is the
                   tracker's `cumulative_damage`. Event-kind counts are NOT in it (a trace change must not read as a
                   fight change; PC-13 adds event kinds).
  WEAPONS hash   : sha256 of the sorted-key serialisation of `weapons.WEAPONS` (every baked key included, so an
                   authored literal the bake overwrites must leave this equal).
  CFG hash       : the same for `config.CFG` (it moves when a CFG key is deleted, by design).
  event counts   : per-kind counts over all fights, reported only.

Families vary kits, armour, skills/traditions/equipped abilities, duel terms and a declared yield. Every fight
has its own `random.Random(seed)`, so a family's rows do not depend on its neighbours. Stdlib only.

BLIND TO: code no family reaches, and state that moves no outcome (stamina, poise, initiative, concentration, trace
content), and a draw that moves no outcome (a trailing draw no later roll reads). Equality says no REACHED fight moved,
not that deleted code was dead: that is the static argument's job. An inserted mid-fight draw shifts every later draw
in that fight's own `Random` and is almost always visible.

THE FALSIFIER: two runs on an unchanged tree must print the same identity hash; if they differ the instrument
cannot see, and nothing measured with it means anything.
"""
import sys, os, json, hashlib, random
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', '..', '..', 'modules', 'combat'))
import wrapper, config, weapons                      # noqa: E402  (flat names; the module has no package)
from combatant import Combatant                      # noqa: E402

FIGHTS_PER_FAMILY = 250

# (name, A kwargs, B kwargs, fight kwargs). `yield_turn`/`yield_by` build a wrapper.Yield for the fight.
FAMILIES = [
    ('mirror_arming_light',     dict(weapon='arming', armor='light'),   dict(weapon='arming', armor='light'), {}),
    ('rapier_v_longsword_med',  dict(weapon='rapier', armor='none'),    dict(weapon='longsword', armor='medium'), {}),
    ('longsword_v_greatsword_h', dict(weapon='longsword', armor='heavy'), dict(weapon='greatsword', armor='heavy'), {}),
    ('spear_v_sabre_med',       dict(weapon='spear', armor='medium'),   dict(weapon='sabre', armor='medium'), {}),
    ('poleaxe_v_mace_heavy',    dict(weapon='poleaxe', armor='heavy'),  dict(weapon='mace', armor='heavy'), {}),
    ('dagger_v_katana_light',   dict(weapon='dagger', armor='light'),   dict(weapon='katana', armor='light'), {}),
    ('guandao_v_staff_none',    dict(weapon='guandao', armor='none'),   dict(weapon='staff', armor='none'), {}),
    ('trad_kits_equipped',      dict(weapon='katana', armor='light', tradition='japanese', equipped=['shinogi']),
                                dict(weapon='longsword', armor='light', tradition='german',
                                     equipped={'zwerchhau': 1.0, 'ringen_am_schwert': 0.5, 'indes': 1.0}), {}),
    ('skilled_asymmetric',      dict(weapon='estoc', armor='medium', strength=6, agi=6, end=6, cog=5, att=5, spirit=4,
                                     focus=6, history=6, disp=6, tradition='italian', equipped=['mezzo_tempo', 'misura'],
                                     skills={'attack': 0.5}),
                                dict(weapon='falchion', armor='medium', strength=3, agi=3, end=3, cog=2, att=2,
                                     spirit=2, focus=2, history=2, disp=2), {}),
    ('terms_blood',             dict(weapon='arming', armor='light'),   dict(weapon='sabre', armor='light'),
                                dict(terms='blood')),
    ('terms_yield',             dict(weapon='longsword', armor='medium'), dict(weapon='sabre', armor='medium'),
                                dict(terms='yield')),
    ('declared_yield_short',    dict(weapon='arming', armor='none'),    dict(weapon='arming', armor='none'),
                                dict(yield_turn=3, yield_by='A', max_bouts=4)),
]
assert len(FAMILIES) == 12


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), default=repr)


def _sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def run_family(index, fam, n):
    name, ka, kb, fk = fam
    rows, kinds = [], Counter()
    for i in range(n):
        A, B = Combatant('A', **ka), Combatant('B', **kb)
        kw = {}
        if 'terms' in fk:
            kw['terms'] = fk['terms']
        if 'max_bouts' in fk:
            kw['max_bouts'] = fk['max_bouts']
        if 'yield_turn' in fk:
            kw['yield_decl'] = wrapper.Yield(A if fk['yield_by'] == 'A' else B, turn=fk['yield_turn'])
        rng = random.Random(1000003 * (index + 1) + i)
        trace = []
        prev_trace, wrapper._TRACE = wrapper._TRACE, trace.append
        try:
            result = wrapper.fight(A, B, rng=rng, **kw)
        finally:
            wrapper._TRACE = prev_trace
        kinds.update(e['kind'] for e in trace)
        rows.append(dict(family=name, i=i, result=result,
                         A_damage=A.wt.cumulative_damage, B_damage=B.wt.cumulative_damage,
                         wounds=[A.wt.wounds, B.wt.wounds], felled=[bool(A.felled), bool(B.felled)]))
    return rows, kinds


def measure(per_family=FIGHTS_PER_FAMILY):
    all_rows, kinds, fam_hash = [], Counter(), {}
    for idx, fam in enumerate(FAMILIES):
        rows, k = run_family(idx, fam, per_family)
        all_rows.extend(rows); kinds.update(k)
        fam_hash[fam[0]] = _sha(_canon(rows))[:16]
    decided = sum(1 for r in all_rows if r['result'] != 0)
    return dict(fights=len(all_rows), decided=decided,
                identity_hash=_sha(_canon(all_rows)),
                weapons_hash=_sha(_canon(weapons.WEAPONS)),
                cfg_hash=_sha(_canon(config.CFG)),
                family_hash=fam_hash, event_counts=dict(sorted(kinds.items())))


if __name__ == '__main__':
    n = FIGHTS_PER_FAMILY
    if '--fights' in sys.argv:
        n = max(1, int(sys.argv[sys.argv.index('--fights') + 1]) // len(FAMILIES))
    out = measure(n)
    if '--json' in sys.argv:
        print(json.dumps(out, indent=1, sort_keys=True))
    else:
        print(f"fights          {out['fights']} ({out['decided']} decided)")
        print(f"identity hash   {out['identity_hash']}")
        print(f"WEAPONS hash    {out['weapons_hash']}")
        print(f"CFG hash        {out['cfg_hash']}   (moves when a CFG key is deleted)")
        for k, v in out['family_hash'].items():
            print(f"  family {k:26s} {v}")
        print("event counts (reported; not in the identity hash):")
        for k, v in out['event_counts'].items():
            print(f"  {k:18s} {v}")
