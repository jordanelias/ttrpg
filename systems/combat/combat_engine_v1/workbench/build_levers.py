"""Build-lever instrument — what a PLAYER can change about a fighter, and what each change is worth.

`workbench/balance.py` sweeps the three things the balance methodology owns (weapon, attribute, tradition)
and it builds its combatants through `balance._mk`, which forwards only the nine attributes plus
weapon/armour/tradition. That leaves four of the engine's build inputs unmeasurable by it: **skills**
(`c.skills`), **learned techniques and their invested level** (`c.equipped`), **cross-training**
(`c.known_traditions`), and **asymmetric armour** (balance.py's armour matrix always puts both fighters at
the same tier). Those four are exactly the customization surface, so this file measures them.

Method is balance.py's, unchanged: one factor varied against an otherwise-identical opponent,
position-swapped to cancel the first-mover artifact, decisive −1/0/+1, Wilson 95% CI, deterministic crc32
seeding. The reference is 50 — `mirror()` re-establishes it on demand rather than asking the reader to
trust it (arming/light reads 50.5/50.8/50.8 at n=2000 over seeds 0/1/7).

**Read the CI, not the point estimate.** A single cell at n=600 carries roughly ±4pp, at n=200 roughly
±7pp. Most of this file's abilities rows are *inside* that floor, and that is the finding — not a
measurement to be quoted as a small positive effect.

CLI:
    python workbench/build_levers.py [all|skills|abilities|disposition|armour|familiarity|archetypes|mirror] [n]
"""
import sys, os, random, zlib

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import wrapper
from config import CFG
from combatant import Combatant

WILSON_Z = 1.96          # same constant balance.py imports from r8_parity_harness (Class-M method)
BASE = dict(weapon='arming', armor='light', tradition='none')
SKILL_AXES = ('bind', 'parry', 'dodge', 'balance', 'technique', 'grab')   # every axis c.skill() is called on
_POST_INIT = ('known_traditions',)   # read off the Combatant via getattr, not accepted by __init__


def _seed(key):
    """crc32, not hash() — hash() is PYTHONHASHSEED-salted and would make these tables irreproducible
    run-to-run. Same function and rationale as workbench/balance.py's _seed."""
    return zlib.crc32(repr(key).encode()) % 9999


def _wilson(w, n, z=WILSON_Z):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = w / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = (z * (p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def build(spec):
    """A Combatant from a plain build spec. `known_traditions` is set after construction because the engine
    reads it via getattr (cross-training is an optional fighter-layer attribute, not a constructor field)."""
    kw = {k: v for k, v in spec.items() if k != 'label' and k not in _POST_INIT}
    c = Combatant(spec.get('label', '?'), **kw)
    for k in _POST_INIT:
        if k in spec:
            setattr(c, k, spec[k])
    return c


def duel(A, B, n, seed=0, cfg=None):
    """Position-swapped decisive win-rate of build A vs build B. Returns (win%, lo, hi, decided)."""
    cfg = cfg or CFG
    rng = random.Random(seed)
    aw = dec = 0
    half = n // 2
    for i in range(n):
        swap = i >= half
        X = build(B if swap else A)
        Y = build(A if swap else B)
        r = wrapper.fight(X, Y, cfg, rng)
        if swap:
            r = -r
        if r == 1:
            aw += 1; dec += 1
        elif r == -1:
            dec += 1
    p, lo, hi = _wilson(aw, dec)
    return round(100 * p, 1), round(100 * lo, 1), round(100 * hi, 1), dec


def _hdr(title):
    print(f"\n### {title}")
    print("| lever | win% | 95% CI | decided |")
    print("|---|---|---|---|")


def _row(name, A, B, n):
    p, lo, hi, dec = duel(A, B, n, seed=_seed(name))
    print(f"| {name} | {p} | {lo}-{hi} | {dec}/{n} |", flush=True)
    return p


# ── the sweeps ────────────────────────────────────────────────────────────────────────────────────
def mirror(n=2000):
    """The fairness control. A mirror cell must sit at ~50 — a mirror that drifts off 50 is a bug, not a
    finding (combat_balancing_methodology §2). Run this before trusting any row below."""
    _hdr(f"Mirror fairness control (n={n} per cell, expect ~50)")
    for spec, name in ((dict(weapon='arming', armor='light'), 'arming/light'),
                       (dict(weapon='longsword', armor='heavy'), 'longsword/heavy'),
                       (dict(weapon='rapier', armor='none'), 'rapier/none')):
        for seed in (0, 1, 7):
            p, lo, hi, dec = duel(dict(spec), dict(spec), n, seed=seed)
            print(f"| {name} seed {seed} | {p} | {lo}-{hi} | {dec}/{n} |", flush=True)


def skills(n=600):
    """Per-axis skill investment vs an untrained twin. `c.skills` is a free-form dict of per-axis biases and
    is UNCAPPED at the engine layer (combatant.skill() returns skills.get(axis, 0.0)) — bounding it is a
    character-gen/economy job that does not exist yet."""
    _hdr(f"Skill axes (+1 on one axis vs an untrained twin, n={n})")
    for ax in SKILL_AXES:
        _row(f'skill {ax} +1', dict(BASE, skills={ax: 1.0}), dict(BASE), n)
    _row('skill bind +2', dict(BASE, skills={'bind': 2.0}), dict(BASE), n)
    _row('skill bind +3', dict(BASE, skills={'bind': 3.0}), dict(BASE), n)
    _row('skills +1 on all six', dict(BASE, skills={a: 1.0 for a in SKILL_AXES}), dict(BASE), n)


def abilities(n=600):
    """Learned techniques at graded investment (ED-PC-0024), the tradition ACCESS gate (ED-PC-0028), and
    cross-training. Expect these rows inside the noise floor: the ED-PC-0023 adversarial review already
    established the ability layer's aggregate win-rate edge is ~0 and its real effect is per-fight texture
    (tests/valoria's test_levers_add_texture_without_shifting_balance is the instrument for that claim)."""
    KAT = dict(weapon='katana', armor='light', tradition='japanese')
    GER = dict(weapon='longsword', armor='light', tradition='german')
    _hdr(f"Ability investment levels (n={n})")
    for lvl in (1.0, 2.0, 4.0, 8.0):
        _row(f'shinogi L{lvl} (katana mirror)', dict(KAT, equipped={'shinogi': lvl}), dict(KAT), n)
    _row('shinogi L4 + bind skill 2', dict(KAT, equipped={'shinogi': 4.0}, skills={'bind': 2.0}), dict(KAT), n)
    for lvl in (1.0, 4.0):
        _row(f'indes L{lvl} (longsword mirror)', dict(GER, equipped={'indes': lvl}), dict(GER), n)
        _row(f'staerke_schwaeche L{lvl}', dict(GER, equipped={'staerke_schwaeche': lvl}), dict(GER), n)
    _row('german full kit L2 (indes+staerke+zwerchhau+ringen)',
         dict(GER, equipped={'indes': 2.0, 'staerke_schwaeche': 2.0,
                             'zwerchhau': 2.0, 'ringen_am_schwert': 2.0}), dict(GER), n)
    _row('UNTAUGHT shinogi L4 on a german (access gate -> inert)',
         dict(GER, equipped={'shinogi': 4.0}), dict(GER), n)
    _row('cross-trained (german+japanese) shinogi L4 on longsword',
         dict(GER, equipped={'shinogi': 4.0}, known_traditions=('german', 'japanese')), dict(GER), n)
    _row('cross-trained (german+japanese) shinogi L4 on katana',
         dict(weapon='katana', armor='light', tradition='german', equipped={'shinogi': 4.0},
              known_traditions=('german', 'japanese')),
         dict(weapon='katana', armor='light', tradition='german'), n)


def disposition(n=600):
    """Temperament (disp 1-7, 4 = neutral). config.py states the design intent as 'BOTH poles cost'
    (aggression risks overcommit, caution bleeds the Vor); this sweep is what tests that claim."""
    _hdr(f"Disposition vs neutral disp=4 (n={n})")
    for d in (1, 2, 3, 5, 6, 7):
        _row(f'disp {d}', dict(BASE, disp=d), dict(BASE, disp=4), n)


def armour(n=600):
    """ASYMMETRIC armour — the case balance.py's armour matrix cannot show, because it always puts both
    fighters at the same tier. Note what the engine reads: `c.armor` is consumed only as the TARGET's
    protection (select_mode, armor_defeat_sigma, reach_threat, the percussion-transmit table). No site
    charges the wearer for it — there is no mass, tempo, stamina or mobility cost."""
    _hdr(f"Armour choice, same weapon, asymmetric protection (n={n})")
    for a in ('light', 'medium', 'heavy'):
        _row(f'armour {a} vs none (arming)', dict(BASE, armor=a), dict(BASE, armor='none'), n)
    for a in ('medium', 'heavy'):
        _row(f'armour {a} vs light (arming)', dict(BASE, armor=a), dict(BASE, armor='light'), n)
    _row('rapier heavy vs rapier none', dict(BASE, weapon='rapier', armor='heavy'),
         dict(BASE, weapon='rapier', armor='none'), n)
    _row('poleaxe heavy vs poleaxe none', dict(BASE, weapon='poleaxe', armor='heavy'),
         dict(BASE, weapon='poleaxe', armor='none'), n)


def familiarity(n=600):
    """Tradition-vs-tradition with NO abilities equipped. With the imposition gate retired (ED-PC-0023) and
    the channel-weight vector removed (2026-06-29), an ability-less tradition differs from another ONLY
    through traditions.familiarity() feeding WARINESS_K. This sweep is the size of that residual."""
    _hdr(f"Tradition familiarity, no abilities equipped (n={n})")
    _row('german vs chinese (unfamiliar, 0.85 both ways)',
         dict(BASE, tradition='german'), dict(BASE, tradition='chinese'), n)
    _row('german vs italian (adjacent, 0.93)',
         dict(BASE, tradition='german'), dict(BASE, tradition='italian'), n)
    _row('german vs none (familiarity 1.0 both)',
         dict(BASE, tradition='german'), dict(BASE, tradition='none'), n)


def archetypes(n=600):
    """Whole builds vs the neutral baseline — the composed question a player actually asks. Each archetype
    stacks its own weapon, armour, attributes, skills and kit; the spread between them is the honest
    measure of how much build identity currently survives into outcomes."""
    _hdr(f"Composite archetypes vs the neutral baseline arming/light/none/no-skill (n={n})")
    _row('duellist: rapier, agi5 att4, dodge+parry 1, italian kit L2',
         dict(weapon='rapier', armor='light', tradition='italian', agi=5, att=4,
              skills={'dodge': 1.0, 'parry': 1.0},
              equipped={'mezzo_tempo': 2.0, 'misura': 2.0}), dict(BASE), n)
    _row('binder: longsword, str5 cog4, bind2 tech1, german kit L2',
         dict(weapon='longsword', armor='light', tradition='german', strength=5, cog=4,
              skills={'bind': 2.0, 'technique': 1.0},
              equipped={'indes': 2.0, 'staerke_schwaeche': 2.0}), dict(BASE), n)
    _row('armour-breaker: poleaxe, str5 end5, tech1, heavy armour',
         dict(weapon='poleaxe', armor='heavy', tradition='none', strength=5, end=5,
              skills={'technique': 1.0}), dict(BASE), n)
    _row('grappler: dagger, str5, grab2 balance1, german ringen L3',
         dict(weapon='dagger', armor='light', tradition='german', strength=5,
              skills={'grab': 2.0, 'balance': 1.0},
              equipped={'ringen_am_schwert': 3.0}), dict(BASE), n)
    _row('reach specialist: spear, agi5, balance1, no tradition',
         dict(weapon='spear', armor='light', tradition='none', agi=5,
              skills={'balance': 1.0}), dict(BASE), n)


SWEEPS = {'skills': skills, 'abilities': abilities, 'disposition': disposition,
          'armour': armour, 'familiarity': familiarity, 'archetypes': archetypes}

if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    if which == 'mirror':
        mirror(n if len(sys.argv) > 2 else 2000)
    elif which == 'all':
        for fn in SWEEPS.values():
            fn(n)
    elif which in SWEEPS:
        SWEEPS[which](n)
    else:
        print(f"unknown sweep {which!r}; expected one of: mirror, all, {', '.join(SWEEPS)}")
        sys.exit(2)
