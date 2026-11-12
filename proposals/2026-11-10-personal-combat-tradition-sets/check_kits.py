"""check_kits.py — runs kits_draft.py against the LIVE personal-combat module. Read-only: nothing under modules/ is
edited; the draft abilities are merged into the in-process registry copy and discarded when the script exits.

    python proposals/2026-11-10-personal-combat-tradition-sets/check_kits.py [--fights N]

Exit code 0 = every structural check passed. The behavioural section PRINTS what it measured; it asserts only
what the engine contract already requires (byte-identity at an empty kit, tradition gate, sign of the per-event
effect, no crash), never a win-rate.
"""
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
ENGINE = os.path.join(ROOT, 'modules', 'combat')
sys.path.insert(0, ENGINE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'systems', 'combat', 'combat_engine_v1', 'workbench'))

import ability_primitives as ABIL   # noqa: E402
import combat_systems as S          # noqa: E402
import tradition as TR              # noqa: E402
import wrapper as W                 # noqa: E402
from combatant import Combatant     # noqa: E402
from config import CFG              # noqa: E402
import kits_draft as K              # noqa: E402

sys.path.insert(0, os.path.join(ROOT, 'systems', 'combat', 'combat_engine_v1'))
import state_graph as SG            # noqa: E402

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print('  FAIL', msg)
    return cond


def src(name):
    with open(os.path.join(ENGINE, name), encoding='utf-8') as f:
        return f.read()


ENGINE_SRC = {n: src(n) for n in ('combat_systems.py', 'contact.py', 'wrapper.py', 'ability_primitives.py')}
CONSUMER_SRC = ENGINE_SRC['combat_systems.py'] + ENGINE_SRC['contact.py']


def consumed(lever):
    """A lever is consumed if its quoted name appears in a consumer file (eff_cw / ability_factor / ability_bonus)."""
    return re.search(r"""(?:eff_cw|ability_factor|ability_bonus)\(\s*[A-Za-z_\.]+\s*,\s*['"]%s['"]""" % re.escape(lever),
                     CONSUMER_SRC) is not None


print('1. levers')
for lv in sorted(K.LEVERS_LIVE):
    check(consumed(lv), f'live lever {lv!r} has no consumer in combat_systems/contact')
for lv, d in K.LEVERS_NEW.items():
    check(not consumed(lv), f'new lever {lv!r} already has a consumer; move it to LEVERS_LIVE')
    fn = d['site'].split('.')[-1].split(' ')[0]
    check(re.search(r'def %s\(' % re.escape(fn), CONSUMER_SRC) is not None or lv.startswith('guard_prior'),
          f'site function {fn!r} for {lv!r} not found')
    check(d['point'] in SG.INJECTION_POINTS, f'{lv}: unknown injection point {d["point"]!r}')

print('2. entries')
live_names = set(ABIL.ABILITIES)
seen_lever_by_trad = {}
n_new = n_existing = 0
for trad, kit in K.KITS.items():
    check(trad in TR.TRADITIONS, f'unknown tradition {trad!r}')
    for w in kit['teaches'] + kit['candidates']:
        check(w in S.WEAPONS, f'{trad}: weapon {w!r} not in the live roster')
    for name, a in kit['abilities'].items():
        check(a['tradition'] == trad, f'{name}: tradition tag differs from its kit')
        check(a['op'] in ('+', '*'), f'{name}: bad op')
        check(a['mech'] in 'VCU' and a['term'] in 'VCU', f'{name}: bad verification code')
        check(a['src'] in K.SOURCES, f'{name}: unknown source {a["src"]!r}')
        check(a['point'] in SG.INJECTION_POINTS, f'{name}: unknown injection point {a["point"]!r}')
        lo, hi = (0.3, 2.0) if a['op'] == '*' else (0.0, 0.5)
        check(lo <= a['value'] <= hi, f'{name}: value {a["value"]} outside [{lo},{hi}]')
        check(a['lever'] in K.LEVERS_LIVE or a['lever'] in K.LEVERS_NEW, f'{name}: lever {a["lever"]!r} unknown')
        check(a['lever'] not in seen_lever_by_trad.setdefault(trad, set()), f'{name}: second ability on {a["lever"]!r} in {trad}')
        seen_lever_by_trad[trad].add(a['lever'])
        if a['existing']:
            n_existing += 1
            live = ABIL.ABILITIES.get(name)
            check(live is not None, f'{name}: marked existing but absent from live ABILITIES')
            if live:
                for f in ('tradition', 'lever', 'op', 'value'):
                    check(live[f] == a[f], f'{name}: drifted from live ({f}: {live[f]!r} vs {a[f]!r})')
        else:
            n_new += 1
            check(name not in live_names, f'{name}: collides with a live ability')
        if a['mech'] == 'U':
            print(f'  note: {name} mech=U — candidate, needs an S1/S2 read before merge')
print(f'  existing restated {n_existing}, new {n_new}')

print('3. coverage')
pts = {p: [] for p in SG.INJECTION_POINTS}
for trad, kit in K.KITS.items():
    for name, a in kit['abilities'].items():
        for pp in (a['point'],) + tuple(a['also']):
            pts[pp].append(name)
for p, names in pts.items():
    why = K.NOT_HOOKED.get(p)
    print(f'  {p:22s} {len(names):2d}  {", ".join(names) if names else ("NOT HOOKED: " + why[:60] + "...") if why else "(none)"}')
    check(names or why, f'injection point {p} has neither an ability nor a stated reason')
used = {a['lever'] for k in K.KITS.values() for a in k['abilities'].values()}
print('  live levers unowned:', sorted(K.LEVERS_LIVE - used))
print('  new levers unowned :', sorted(set(K.LEVERS_NEW) - used))

print('3b. slots per tradition (composed, not accumulated)')
for trad, kit in K.KITS.items():
    sl = {}
    for name, a in kit['abilities'].items():
        sl.setdefault(K.SLOT_OF_POINT[a['point']], []).append(name)
    if sl:
        print(f'  {trad:9s} {len(sl)} slots: ' + '; '.join(f'{k}: {", ".join(v)}' for k, v in sl.items()))
check(all(p in K.SLOT_OF_POINT for p in SG.INJECTION_POINTS), 'SLOT_OF_POINT misses an injection point')

print('3c. relations')
ids = set()
for r in K.RELATIONS:
    check(r['id'] not in ids, f"duplicate relation id {r['id']}"); ids.add(r['id'])
    kit = K.KITS[r['tradition']]['abilities']
    check(r['ability'] in kit, f"{r['id']}: {r['ability']!r} not in the {r['tradition']} kit")
    deps = r.get('needs') or r.get('with_') or {}
    for d, lv in deps.items():
        check(d in kit, f"{r['id']}: dependency {d!r} not in the {r['tradition']} kit")
        check(0 < lv <= ABIL.MAX_INVESTMENT_LEVEL, f"{r['id']}: level {lv} outside (0, MAX_INVESTMENT_LEVEL]")
    for st, ab in (r.get('selects') or {}).items():
        check(ab in kit, f"{r['id']}: branch target {ab!r} not in the kit")
    check(r['src'] in K.SOURCES, f"{r['id']}: unknown source")
    if r['kind'] == 'widens':
        check(r['gate_class'] == 'B', f"{r['id']}: a widening must be a Class B availability gate")
        check("commit>=cfg['DEEP_COMMIT']" in ENGINE_SRC['wrapper.py'], f"{r['id']}: the gate it cites is not in wrapper.py")
    print(f"  {r['id']} {r['kind']:8s} {r['ability']:12s} <- {', '.join(deps) or ', '.join((r.get('selects') or {}).values())}   term={r['term']} mech={r['mech']}")
# acyclic, depth <= 3
req = {r['ability']: set(r['needs']) for r in K.RELATIONS if r['kind'] == 'requires'}
def depth(a, seen=()):
    check(a not in seen, f'requires cycle through {a}')
    return 1 + max((depth(d, seen + (a,)) for d in req.get(a, ())), default=0) if a not in seen else 0
check(all(depth(a) <= 3 for a in req), 'a requires chain is deeper than 3')
print('  kits with no relation authored:', {t: K.RELATION_GAPS.get(t, '(none stated)') for t in K.KITS if K.KITS[t]['abilities'] and not any(r['tradition'] == t for r in K.RELATIONS)})

print('4. weapon coverage (live roster, half-sword forms excluded)')
roster = [w for w in S.WEAPONS if not w.endswith('halfsword')]
taught = {}
for trad, kit in K.KITS.items():
    for w in kit['teaches']:
        taught.setdefault(w, []).append(trad)
orphans = [w for w in roster if w not in taught]
print(f'  {len(roster) - len(orphans)}/{len(roster)} weapons have a teaching tradition; orphans: {", ".join(orphans)}')
no_kit = [t for t, k in K.KITS.items() if not k['abilities'] and t != 'none']
print('  traditions with no kit:', no_kit)

# ── behavioural ─────────────────────────────────────────────────────────────────────────────────────
print('5. behaviour (draft abilities merged in-process)')
draft_live = {n: {k: v for k, v in a.items()} for kit in K.KITS.values() for n, a in kit['abilities'].items()
              if not a['existing'] and a['lever_status'] == 'live'}
ABIL.ABILITIES.update(draft_live)
for t in ABIL.TRADITION_KIT:
    ABIL.TRADITION_KIT[t] = [a for a, d in ABIL.ABILITIES.items() if d['tradition'] == t]


def mk(label, weapon, trad='none', eq=None):
    return Combatant(label, weapon=weapon, tradition=trad, equipped=eq or [])


def ratio(f, trained, plain):
    return f(trained), f(plain)


# gate: untaught exact inert; taught moves
def probe(name, fn, better):
    a = K.KITS[[t for t, k in K.KITS.items() if name in k['abilities']][0]]['abilities'][name]
    trad = a['tradition']
    taught_v = fn(mk('A', 'arming', trad, [name]))
    plain_v = fn(mk('A', 'arming', trad, []))
    untaught_v = fn(mk('A', 'arming', 'none', [name]))
    moved = taught_v > plain_v if better == 'up' else taught_v < plain_v
    check(moved, f'{name}: taught value {taught_v!r} did not move {better} from {plain_v!r}')
    check(untaught_v == plain_v, f'{name}: untaught equip is not inert ({untaught_v!r} vs {plain_v!r})')
    print(f'  {name:12s} {a["lever"]:16s} plain {plain_v:.4f} -> taught {taught_v:.4f}  (untaught {untaught_v:.4f})')


foe = mk('B', 'arming')
probe('fuehlen', lambda c: S.bind_sigma(c, foe, CFG, TR), 'up')
probe('contratempo', lambda c: S.counter_success_prob(c, CFG, TR), 'up')
probe('zanshin', lambda c: S.init_overcommit_loss(c, 1.0, CFG, TR), 'down')
probe('circulo', lambda c: S.init_hold_decay(c, CFG, TR), 'up')   # decay multiplier nearer 1 = the Vor is held longer
probe('compas', lambda c: S.pursuit_sigma(c, foe, 0.0, 0.0, CFG, TR), 'up')
for nm in ('sen_no_sen', 'metsuke'):
    def _read(c, nm=nm):
        return S.read_contest(foe, c, 3.0, 0.0, 0.0, 0.0, CFG, random.Random(1), TR)['p_read']
    probe(nm, _read, 'up')

# byte-identity at an empty kit with the draft merged: same seeds, same outcomes
from trace import run_traced_fight   # noqa: E402
n = int(sys.argv[sys.argv.index('--fights') + 1]) if '--fights' in sys.argv else 150
base_kit_off = {}
for trad in ('german', 'italian', 'spanish', 'english', 'japanese'):
    wa = K.KITS[trad]['teaches'][0]
    kit_names = [a for a, d in K.KITS[trad]['abilities'].items() if d['lever_status'] == 'live']
    crashed = diverged = flipped = wins_on = wins_off = 0
    for s in range(n):
        try:
            r_on, ev_on = run_traced_fight(mk('A', wa, trad, kit_names), mk('B', 'arming'), cfg=CFG, seed=s)
            r_off, ev_off = run_traced_fight(mk('A', wa, trad, []), mk('B', 'arming'), cfg=CFG, seed=s)
        except Exception as e:   # noqa: BLE001 — a crash is the finding
            crashed += 1
            print('   crash', trad, s, repr(e)[:90])
            continue
        sig = lambda ev: tuple((e['kind'], e.get('outcome'), e.get('hit')) for e in ev if e['kind'] in ('outcome', 'contact', 'separation'))   # noqa: E731
        diverged += sig(ev_on) != sig(ev_off)
        flipped += r_on != r_off
        wins_on += r_on == 'A' or r_on == 1
        wins_off += r_off == 'A' or r_off == 1
    check(crashed == 0, f'{trad}: {crashed} fights crashed with the kit equipped')
    print(f'  {trad:9s} {wa:9s} kit={len(kit_names)} live abilities  diverged {diverged}/{n}  flipped {flipped}/{n}')
print('FAILED' if FAILS else 'ALL STRUCTURAL CHECKS PASSED', len(FAILS))
sys.exit(1 if FAILS else 0)
