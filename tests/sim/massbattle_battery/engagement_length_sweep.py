"""Does lengthening unit-vs-unit engagements let formation geometry complete a Cannae?

Two tests, both PER_CELL=1, infantry, all components wired:

 SWEEP — for the envelopment matchups, run ONE CONTINUOUS engagement of K ticks (no per-round
   position reset) and measure the rout-based decisive split + the casualty margin. 6 ticks =
   TICKS_PER_PHASE = 1 "round", so K/6 = rounds. Finds how many rounds an infantry envelopment needs.

 RESET-vs-CONTINUOUS — for H4, compare equal total tick budgets delivered as (a) one continuous
   engagement vs (b) N reset-each-round engagements (run_multi_turn_battle). Isolates whether the
   per-round reset_positions (the discrete-turn artifact) is what prevents the manoeuvre.

Run:
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python -u tests/sim/massbattle_battery/engagement_length_sweep.py
"""
import os, sys, random, json

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW, TICKS_PER_PHASE  # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle, run_multi_turn_battle  # noqa: E402

ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8,
          ('RefusedFlank', 3): 9, ('GappedLine', 3): 7}


def make_unit(shape, name, fac, command=5, **kw):
    adv = -1 if fac == 'A' else 1
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type=kw.get('troop_type', 'infantry'), tier=3,
                 starting_position=(row, ANCHOR.get((shape, 3), 10)), advance_dir=adv,
                 unit_type=kw.get('unit_type', 'melee'), instructions=kw.get('instructions', ()))
    return Unit(name=name, faction=fac, power=4, command=command, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=[su], dr=1,
                stance=kw.get('stance', 'balanced'), speed=kw.get('speed', 'Standard'))


def _winner(ua, ub):
    if ub.routed and not ua.routed: return 'A'
    if ua.routed and not ub.routed: return 'B'
    return 'draw'


def continuous(sa, sb, K, n=20):
    aw = bw = dr = 0; margin = []
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_unit(sa, 'A', 'A'); ub = make_unit(sb, 'B', 'B')
        a0, b0 = ua.hp_max, ub.hp_max
        run_battle(ua, ub, max_turns=K)
        w = _winner(ua, ub); aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
        margin.append((100 * (b0 - ub.hp) / b0) - (100 * (a0 - ua.hp) / a0))   # B_cas% - A_cas% (enveloper edge)
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, draw_pct=round(100 * dr / n, 1),
                cas_margin=round(sum(margin) / n, 1), A=aw, B=bw)


def reset_rounds(sa, sb, turns, n=20):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_unit(sa, 'A', 'A'); ub = make_unit(sb, 'B', 'B')
        r = run_multi_turn_battle(ua, ub, sa, sb, ANCHOR, max_battle_turns=turns)
        w = r['winner']; aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, draw_pct=round(100 * dr / n, 1), A=aw, B=bw)


MATCHUPS = {
    'H4 Horseshoe vs Arrowhead  (Cannae,  band 45-62)': ('Horseshoe', 'Arrowhead'),
    'H3 Horseshoe vs Line       (envelop, band 55-72)': ('Horseshoe', 'Line'),
    'H6 RefusedFlank vs Line    (oblique, band 48-60)': ('RefusedFlank', 'Line'),
}
LENGTHS = [18, 36, 72, 108, 144]   # ticks; /6 = rounds -> 3, 6, 12, 18, 24 rounds

if __name__ == '__main__':
    print(f"TICKS_PER_PHASE={TICKS_PER_PHASE} (1 round = {TICKS_PER_PHASE} ticks); engagement lengths in rounds: "
          + ", ".join(f"{K}t={K // TICKS_PER_PHASE}r" for K in LENGTHS))
    out = {'sweep': {}, 'reset_vs_continuous': {}}

    print("\n=== CONTINUOUS engagement-length sweep (rout-based decisive split) ===")
    for label, (sa, sb) in MATCHUPS.items():
        print(f"\n  {label}")
        out['sweep'][label] = {}
        for K in LENGTHS:
            r = continuous(sa, sb, K, n=20)
            out['sweep'][label][K] = r
            print(f"     {K//TICKS_PER_PHASE:>2} rounds ({K:>3}t):  decA={r['decA']:5.1f}  draws={r['draw_pct']:5.1f}%  cas-margin(B-A)={r['cas_margin']:+5.1f}")

    print("\n=== RESET vs CONTINUOUS at equal tick budget (H4 Horseshoe vs Arrowhead) ===")
    for rounds in (4, 6, 8):
        K = rounds * 18   # run_multi_turn_battle uses ~18-tick engagements per battle-turn
        cont = continuous('Horseshoe', 'Arrowhead', K, n=20)
        rst = reset_rounds('Horseshoe', 'Arrowhead', rounds, n=20)
        out['reset_vs_continuous'][rounds] = dict(continuous=cont, reset=rst, ticks=K)
        print(f"  {rounds} battle-turns (~{K}t):  CONTINUOUS decA={cont['decA']:5.1f} draws={cont['draw_pct']:5.1f}%   |   RESET-each-turn decA={rst['decA']:5.1f} draws={rst['draw_pct']:5.1f}%")

    with open(os.path.join(HERE, 'engagement_length_results.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote engagement_length_results.json")
