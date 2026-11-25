"""Approach-policy probe -- does a state-reading approach policy beat never leaning, in any named matchup? (PB step 3's added gate.)

PB 03 §7 (the row between steps 2 and 3a): "a state-reading policy (press the wounded; guard when hurt) beats never-lean by more than
the interval in some named matchup, or the menu is not shipped." This file is that gate's instrument, beside `build_levers.py` and in
its shape (position-swapped decisive win share, Wilson 95%, crc32 seeding, a markdown table printed, `n` an argument).

THE MATCHUPS (PB §3's "named matchups"; the leaning fighter is the first kit, the foil the second). PB names the pairings in words only;
each is written here as a kit table, and this table is the one place the words become numbers. `L` is the fighter whose approach varies,
`O` the foil, who plans `normal` throughout. Armour tiers: light = cloth, heavy = plate (`core.TIER2MAT`). `end` 4 is the default.

| matchup (PB §3's words)                 | L                       | O                       |
|---|---|---|
| a dagger against an arming sword        | dagger, light           | arming, light           |
| against a low-Endurance opponent        | arming, light           | arming, light, end 2    |
| a lightly armoured fighter against plate| arming, light           | arming, heavy           |
| arming mirror                           | arming, light           | arming, light           |
| spear vs arming sword                   | spear, light            | arming, light           |
| arming sword vs dagger (the bind row)   | arming, light           | dagger, light           |
| mace mirror                             | mace, light             | mace, light             |
| rapier mirror                           | rapier, light           | rapier, light           |

THE POLICIES. A plan is `{phase: approach}` per party (`DuelRoundInput.plans`), here the one approach in all three phases.
  never-lean      `normal` every round (plans `{}`, which a missing phase reads as `normal`).
  state-reading   "press the wounded; guard when hurt", read each round off the states the loop holds:
                  foe carries a wound -> `aggressive`;  else I carry a wound -> `defensive`;  else `normal`.
                  "carries a wound" = `DuelRoundOutcome.wounds[id]['wounds'] >= 1` of the PREVIOUS round (the wound-tracker field `wounds`, the
                  count of wound gates crossed, lifted through `PersonalCombatInput.wound_quantities=('wounds',)`); round 1 has none.
                  Where both carry one, the foe's takes precedence (the listed order: press first).
  A fixed approach (`defensive`/`normal`/`aggressive`, the `leans` mode) plans that approach every round.

THE LOOP. `play` is `fight.py::fight`'s own loop over `fight_round` -- `DuelState`s and `prev_closed` threaded from each round's outcome, one
`wrapper.round_draw(fkey, r)` per round, `fkey = wrapper.fight_draw(rng)`, stopping on a felling, a yield, a tie of the yield rolls, or
`wrapper.DEFAULT_ROUNDS` -- with the one difference that it hands each round its `plans`. `fight` takes no plans, so it cannot be the loop; the
default mode's same-seed check runs `fight` itself beside `play(never-lean)` and reports whether they are one fight. No round is re-implemented.

THE INTERVAL. Each cell is Wilson 95% on wins / decided (decisive fights only, as build_levers). A difference is read by Newcombe's hybrid-score
interval on p1 - p2 (the two Wilson intervals combined), and `beyond` is printed `YES` where it excludes 0. The two arms of a comparison draw on
DISJOINT seeds (a different crc32 key per arm, so a different `Draw` stream and different fight keys), which is what makes the interval honest:
the same seed would hand both arms the same dice and the difference would be a function of the plans alone.

THE CONTROL. On a tree where no lean is built, nothing reads `plans`, so every arm is the same fight at a different seed: every `beyond` should
read `no` up to the interval's own false-positive rate (about one cell in twenty, so across six rows a lone `YES` is a reason to re-seed, not a
finding), and the same-seed check should read identical for every matchup. A difference that persists is the probe's, not the engine's.

CLI:
    python workbench/approach_policy_probe.py [n]            # state-reading vs never-lean, per matchup (default n 2000)
    python workbench/approach_policy_probe.py leans [n]      # each approach vs a normal foe, per matchup, with disengage events per fight
"""
import sys, os, zlib, dataclasses

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
from engine.dice_engine import draw
from engine.season.queries.inputs import DuelState, DuelRoundInput
from modules.combat import wrapper
from modules.combat import fight as entry
import fight_record

WILSON_Z = 1.96
from modules.combat.vocabulary import APPROACHES, PHASES   # PB §3's vocabulary, owned once (B16.05)

# THE MATCHUPS -- see the table in the docstring. (name, L's spec, O's spec)
MATCHUPS = (
    ('dagger vs arming sword',            dict(weapon='dagger', armor='light'),   dict(weapon='arming', armor='light')),
    ('vs low-Endurance opponent',         dict(weapon='arming', armor='light'),   dict(weapon='arming', armor='light', end=2)),
    ('light armour vs plate',             dict(weapon='arming', armor='light'),   dict(weapon='arming', armor='heavy')),
    ('arming mirror',                     dict(weapon='arming', armor='light'),   dict(weapon='arming', armor='light')),
    ('spear vs arming sword',             dict(weapon='spear', armor='light'),    dict(weapon='arming', armor='light')),
    ('arming sword vs dagger',            dict(weapon='arming', armor='light'),   dict(weapon='dagger', armor='light')),   # B16.06's bind row: the arming sword is the reach side that breaks the bind, so its `bind` lean is the one `disengage_attempt_p` reads (the spear row above never binds: it wins on approach)
    ('mace mirror',                       dict(weapon='mace', armor='light'),     dict(weapon='mace', armor='light')),
    ('rapier mirror',                     dict(weapon='rapier', armor='light'),   dict(weapon='rapier', armor='light')),
)


def _seed(key):
    """crc32, not hash() (PYTHONHASHSEED-salted): the same function and rationale as build_levers._seed."""
    return zlib.crc32(repr(key).encode()) % 9999


def _wilson(w, n, z=WILSON_Z):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = w / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = (z * (p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def _newcombe(a, b):
    """Newcombe's hybrid-score interval for p_a - p_b from two `_wilson` triples: (difference, lo, hi)."""
    (p1, l1, u1), (p2, l2, u2) = a, b
    d = p1 - p2
    return d, d - ((p1 - l1) ** 2 + (u2 - p2) ** 2) ** 0.5, d + ((u1 - p1) ** 2 + (p2 - l2) ** 2) ** 0.5


# ── policies: a function of (my id, foe id, last round's wounds) -> this round's plan for me ──────────────────
def never_lean(me, foe, wounds):
    return {}


def state_reading(me, foe, wounds):
    """Press the wounded; guard when hurt. `wounds` is the last round's `DuelRoundOutcome.wounds` (`{id: {'wounds': k}}`), `None` before round 1."""
    carries = lambda pid: bool(wounds) and (wounds.get(pid) or {}).get('wounds', 0) >= 1
    ap = 'aggressive' if carries(foe) else 'defensive' if carries(me) else 'normal'
    return {ph: ap for ph in PHASES}


def fixed(approach):
    plan = {ph: approach for ph in PHASES}
    return lambda me, foe, wounds: dict(plan)


def play(rec, rng, policies, cfg=None):
    """One fight of `rec`, `fight.py::fight`'s loop over `fight_round` with each round's `plans` taken from `policies` (one per claimant, in order).
    Returns (result +1/-1/0, disengage events, rounds). The record must carry `wound_quantities=('wounds',)` for a state-reading policy to see a wound."""
    a_id, b_id = rec.claimants
    states, wounds, prev_closed, result, rounds, disengages = (DuelState(), DuelState()), None, False, 0, 0, 0
    fkey = wrapper.fight_draw(rng)
    for rnd in range(1, wrapper.DEFAULT_ROUNDS + 1):
        plans = (policies[0](a_id, b_id, wounds), policies[1](b_id, a_id, wounds))
        out = entry.fight_round(DuelRoundInput(fighters=rec, states=states, plans=plans, round=rnd, prev_closed=prev_closed),
                                wrapper.round_draw(fkey, rnd), cfg=cfg)
        rounds += 1
        disengages += sum(1 for e in out.trace if e.get("kind") == "disengage")
        states, wounds, prev_closed = out.states, out.wounds, out.closed
        loser = out.felled or out.yielded
        if loser is not None:
            result = -1 if loser == a_id else 1
            break
        if any(e.get("kind") == "fight_result" for e in out.trace):   # the yield rolls tied: unresolved
            break
    return result, disengages, rounds


def _record(spec_l, spec_o, swap):
    """The record with L in claimant slot A (or B where `swap`), the wound quantity lifted. Returns (record, L's id, O's id)."""
    pl, po = fight_record.party_of_spec(spec_l, 'L'), fight_record.party_of_spec(spec_o, 'O')
    pa, pb = (po, pl) if swap else (pl, po)
    rec = dataclasses.replace(fight_record.record_of(pa, pb), wound_quantities=('wounds',))
    return rec


def run(spec_l, spec_o, pol_l, pol_o, n, seed):
    """n fights, position-swapped (the second half puts L in slot B), on one stream keyed by `seed`. Returns a dict: L's wins, decided, undecided,
    disengage events, rounds -- over all n fights."""
    rng = draw.seeded(draw.H2("approach_policy_probe", seed))
    wins = dec = dis = rds = 0
    half = n // 2
    for i in range(n):
        swap = i >= half
        rec = _record(spec_l, spec_o, swap)
        pols = (pol_o, pol_l) if swap else (pol_l, pol_o)
        r, d, k = play(rec, rng, pols)
        if swap:
            r = -r
        wins += r == 1
        dec += r != 0
        dis += d
        rds += k
    return dict(wins=wins, decided=dec, n=n, dis=dis, rounds=rds)


def _cell(res):
    p, lo, hi = _wilson(res['wins'], res['decided'])
    return p, lo, hi


def _pct(t):
    return f"{100 * t[0]:.1f} ({100 * t[1]:.1f}-{100 * t[2]:.1f})"


def _diff(a, b):
    d, lo, hi = _newcombe(a, b)
    return f"{100 * d:+.1f} ({100 * lo:+.1f} to {100 * hi:+.1f})", ('YES' if lo > 0 or hi < 0 else 'no')


def same_seed_check(spec_l, spec_o, n, seed):
    """The same fights (same stream, same swap) played three ways: `fight.py::fight` itself, `play` never-lean, `play` state-reading. Returns
    (fights where play(never-lean) == fight, fights where state-reading == never-lean, n). With no lean built both are n."""
    rng_f, rng_n, rng_s = (draw.seeded(draw.H2("approach_policy_probe", seed)) for _ in range(3))
    loop = pol = 0
    for i in range(n):
        swap = i >= n // 2
        rec = _record(spec_l, spec_o, swap)
        pols_n = (never_lean, never_lean)
        pols_s = (never_lean, state_reading) if swap else (state_reading, never_lean)
        rf = fight_record.result_of(entry.fight(rec, rng_f))
        rn = play(rec, rng_n, pols_n)[0]
        rs = play(rec, rng_s, pols_s)[0]
        loop += rf == rn
        pol += rn == rs
    return loop, pol, n


def policy_table(n):
    print(f"\n### State-reading policy vs never-lean, L's win share against a `normal` foe (n={n} per arm, decisive fights, position-swapped)")
    print("policy: foe carries a wound -> aggressive; else I carry one -> defensive; else normal (the tracker's `wounds` >= 1, last round). "
          "Arms on disjoint seeds; interval Wilson 95%, difference Newcombe 95%.")
    print("| matchup | never-lean win% (CI) | state-reading win% (CI) | state - never (CI) | beyond | decided n/s | same-seed: loop=fight, state=never |")
    print("|---|---|---|---|---|---|---|")
    for name, sl, so in MATCHUPS:
        nv = run(sl, so, never_lean, never_lean, n, _seed((name, 'never-lean')))
        st = run(sl, so, state_reading, never_lean, n, _seed((name, 'state-reading')))
        a, b = _cell(st), _cell(nv)
        dtxt, beyond = _diff(a, b)
        k = min(n, 200)
        loop, pol, kk = same_seed_check(sl, so, k, _seed((name, 'same-seed')))
        print(f"| {name} | {_pct(b)} | {_pct(a)} | {dtxt} | {beyond} | {nv['decided']}/{st['decided']} | {loop}/{kk}, {pol}/{kk} |", flush=True)


def leans_table(n):
    print(f"\n### Each approach (L plans it in every phase) vs a `normal` foe (n={n} per arm, decisive fights, position-swapped)")
    print("Arms on disjoint seeds; interval Wilson 95%; `vs normal` is Newcombe 95% of (this approach - normal). `disengage`/fight counts every `disengage` "
          "event (clean or pursued) of both fighters; `undecided` is the share of fights with no winner.")
    print("| matchup | approach | win% (CI) | vs normal (CI) | beyond | disengage/fight | rounds/fight | undecided% |")
    print("|---|---|---|---|---|---|---|---|")
    for name, sl, so in MATCHUPS:
        cells, base = {}, None
        for ap in ('normal',) + tuple(a for a in APPROACHES if a != 'normal'):
            res = run(sl, so, fixed(ap), never_lean, n, _seed((name, 'leans', ap)))
            cells[ap] = res
            if ap == 'normal':
                base = _cell(res)
        for ap in APPROACHES:
            res = cells[ap]
            c = _cell(res)
            dtxt, beyond = ('--', '--') if ap == 'normal' else _diff(c, base)
            print(f"| {name} | {ap} | {_pct(c)} | {dtxt} | {beyond} | {res['dis'] / n:.3f} | {res['rounds'] / n:.2f} | "
                  f"{100 * (n - res['decided']) / n:.1f} |", flush=True)


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    args = sys.argv[1:]
    mode = 'leans' if args and args[0] == 'leans' else 'policy'
    nums = [a for a in args if a.isdigit()]
    if len(args) > (2 if mode == 'leans' else 1) or (args and mode == 'policy' and not nums):
        print("usage: approach_policy_probe.py [n]  |  approach_policy_probe.py leans [n]")
        sys.exit(2)
    n = int(nums[0]) if nums else 2000
    (leans_table if mode == 'leans' else policy_table)(n)
