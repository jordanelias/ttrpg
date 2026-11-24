"""Scale census — the fight's scale at the module level: how long a fight runs, how many blows wound, whether the lead turns.

The gate artifact of B15.03 (`29_DICE` item 29-3 with `U5b_PC_rulings_in_the_fight` §4): the pessimist's two scratch probes
(F1's 5,000-fight census and the Success-against-interval reading) as one workbench file. Not a CI row; its callers are that
item's gate (`python systems/combat/combat_engine_v1/workbench/scale_census.py`) and `tests/valoria/test_combat_opposed_rule_shape.py`,
which imports `play`, `read` and `Tally` so the reading of a fight lives once (the shape of `round_probe.py`).

A fight is played at module scale: `wrapper.fight` with the trace seam, arming sword and light armour, lethal terms, the
skill score the only thing the two sides differ in. The reading of one fight (`read`) is taken off the trace alone:
  turns            `turn_start` events (a round, A-101; the engine's name for it until PCR-3)
  wounds           `wound` events (a blow that took Health)
  rolls / fails    `roll` events / those banded `fail`
  bloodless        rounds (`turn_start` to `engagement_end`) holding no `wound` event
  winner_behind    the LEAD CHANGE: in a decided fight, the fighter the result gives the fight to dealt less cumulative damage than his
                   opponent at some wound (the result is the fight's as it ends, a turned felling and its riposte included: a fight the
                   riposte hands to the one who trailed counts). Chosen as the reading
                   that reproduces the control arm's 0.352 and the live arm's 0.452 at the plan's seeds' own scheme (the plan's
                   readers are scratchpad files, not in the tree).
  first_wins       the fighter who dealt the first wound is the fighter the result gives the fight to
  loser_blows      wound events on the fighter felled, when a fighter was felled (a death)
  felled_winner    the fighter who was NOT felled by the FIRST felling in the trace, when there was one: the fight's outcome BEFORE any riposte
                   (`UPSET_FLOOR`'s turned blow, ED-PC-0036, which is not the opposed rule): the first `wound` that felled a fighter, or the
                   first `finalblow_riposte` (the blow that would have felled its `by`-party, turned), whichever the trace holds first. `a_wins` reads it: the plan's better-fighter figures (0.923 at 7
                   against 3) are the first felling's, and the fight as it ends reads a little below them (the old flip read about 0.04
                   below at every cell, 0.879 at 7 against 3, measured). The lead change reads the result as the fight ends.

The two ARMS: `live` is the shipped tree; `control` is the 2026-08-14 scale put back by an override, `cfg=dict(CFG,
OPPOSITION_RATE=0.5)` and `core.DMG_SCALE` 1.55 (a module global, patched for the arm and restored).

CLI:
    PYTHONHASHSEED=0 python systems/combat/combat_engine_v1/workbench/scale_census.py [--arm live|control] [--n 5000] [--first 0] [--control-first 800000]
"""
import argparse
import contextlib
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
from engine.dice_engine import draw
from modules.combat import wrapper, combatant, config, core

KEY = "opposed_rule_shape"            # the seed key of every fight here; `draw.H2(KEY, seed)`
CONTROL_RATE, CONTROL_SCALE = 0.5, 1.55   # the 2026-08-14 fight: half the opponent's score, damage scale 1.55


@contextlib.contextmanager
def arm(name):
    """Yield the `cfg` of the named arm with its module-level scale in force; restore it on exit."""
    if name == 'live':
        yield config.CFG
    elif name == 'control':
        was = core.DMG_SCALE
        core.DMG_SCALE = CONTROL_SCALE
        try:
            yield dict(config.CFG, OPPOSITION_RATE=CONTROL_RATE)
        finally:
            core.DMG_SCALE = was
    else:
        raise ValueError(f"arm {name!r} is not 'live' or 'control'")


@contextlib.contextmanager
def no_yield():
    """B15.10: hold the yield roll at Success for the call -- nobody yields, is shaken or rallies -- and restore it on exit (the patch-and-restore
    of `arm`'s `core.DMG_SCALE`). The census reads the opposed rule, and whether a wounded man gives up is the yield roll's (A-24,
    `CFG['YIELD_OB']`: the person's, as the riposte is the designer's cap), so a fight is read to its felling, the fight the calibration windows
    were set on; the yield's own shares are `test_combat_yield_draw.py`'s. The roll draws nothing of the stream, so a fight here is the B15.09 fight."""
    real = wrapper._yield_roll
    wrapper._yield_roll = lambda c, terms, sigma, cfg, draw: 'success'
    try:
        yield
    finally:
        wrapper._yield_roll = real


def play(score_a, score_b, seed, cfg=None, weapon='arming', armor='light'):
    """One lethal fight, arming sword and light armour, A at `score_a`, B at `score_b`, on `seed`, read to its felling (`no_yield`).
    Returns (result, trace, A, B)."""
    A = combatant.Combatant('A', weapon=weapon, armor=armor, score=score_a)
    B = combatant.Combatant('B', weapon=weapon, armor=armor, score=score_b)
    trace = []
    with no_yield():
        result = wrapper.fight(A, B, cfg, draw.seeded(draw.H2(KEY, seed)), trace=trace.append)
    return result, trace, A, B


def read(result, trace):
    """The reading of one fight, off its trace (see the module docstring for each name)."""
    turns = rounds_blooded = 0
    in_round = bloody = False
    first_down = None   # the fighter the first deciding felling (applied or turned) went to
    wounds, rolls, fails = [], [], 0
    for e in trace:
        k = e['kind']
        if k == 'turn_start':
            turns += 1; in_round = True; bloody = False
        elif k == 'wound':
            wounds.append(e); bloody = True
            if e['felled'] and first_down is None:
                first_down = e['victim']
        elif k == 'finalblow_riposte':
            first_down = first_down or e['by']   # the blow that would have felled him, turned: the deciding felling all the same
        elif k == 'roll':
            rolls.append(e['aggressor']); fails += e['degree'] == 'fail'
        elif k == 'engagement_end' and in_round:
            rounds_blooded += bloody; in_round = False
    winner = 'A' if result == 1 else 'B' if result == -1 else None
    behind = first = None
    if winner is not None and wounds:
        dealt, behind = {'A': 0, 'B': 0}, False
        for e in wounds:
            dealt[e['by']] += e['damage']
            behind = behind or dealt[winner] < dealt['B' if winner == 'A' else 'A']
        first = wounds[0]['by'] == winner
    return dict(felled_winner=('B' if first_down == 'A' else 'A') if first_down else None, turns=turns, bloodless=turns - rounds_blooded, wounds=len(wounds), rolls=len(rolls), fails=fails,
                wounds_by={s: sum(e['by'] == s for e in wounds) for s in 'AB'}, rolls_by={s: rolls.count(s) for s in 'AB'},
                decided=winner is not None, winner=winner, winner_behind=behind, first_wins=first,
                loser_blows=sum(e['victim'] == first_down for e in wounds) if first_down else None)


class Tally:
    """Reads `fights` fights of one cell and holds the sums; every share is a method."""
    def __init__(self, score_a, score_b, first=0, fights=1200, cfg=None):
        self.fights = fights
        self.rows = []
        for s in range(first, first + fights):
            result, trace, A, B = play(score_a, score_b, s, cfg)
            self.rows.append(read(result, trace))

    def _sum(self, key):
        return sum(r[key] for r in self.rows)

    def mean_turns(self):       return self._sum('turns') / self.fights
    def mean_wounds(self):      return self._sum('wounds') / self.fights
    def undecided(self):        return sum(not r['decided'] for r in self.rows) / self.fights
    def bloodless_turns(self):  return self._sum('bloodless') / self._sum('turns')
    def fail_share(self):       return self._sum('fails') / self._sum('rolls')

    def wounds_per_roll(self, side=None):
        """The attacker's wound events per roll event: pooled over both sides, or one side's own."""
        if side is None:
            return self._sum('wounds') / self._sum('rolls')
        return sum(r['wounds_by'][side] for r in self.rows) / sum(r['rolls_by'][side] for r in self.rows)

    def _decided_share(self, key):
        got = [r[key] for r in self.rows if r[key] is not None]
        return sum(got) / len(got)

    def lead_change(self):      return self._decided_share('winner_behind')
    def first_wounded_wins(self): return self._decided_share('first_wins')

    def a_wins(self):
        """Share of the fights with a felling that A won at the first felling, before any riposte (`felled_winner`)."""
        dec = [r for r in self.rows if r['felled_winner'] is not None]
        return sum(r['felled_winner'] == 'A' for r in dec) / len(dec)

    def two_blow_deaths(self):
        """Of the fights where a fighter was felled, the share where the loser took exactly two wounding blows."""
        deaths = [r['loser_blows'] for r in self.rows if r['loser_blows'] is not None]
        return sum(b == 2 for b in deaths) / len(deaths), len(deaths)


def success_vs_interval(cfg=None):
    """(damage of an arming sword's Success on light armour, the defender's Wound Interval) for default fighters."""
    A, B = combatant.Combatant('A'), combatant.Combatant('B')
    for c in (A, B):
        wrapper._init_live(c, cfg or config.CFG)
    return core.strike(A, B, 'success', cfg or config.CFG), B.wt.wi


def census(name, n, first, control_first):
    """Print UPR §4's five readings for `name`'s arm over `n` fights at `first`, the sampling controls over `n` at `control_first`."""
    with arm(name) as cfg:
        main = Tally(2, 2, first, n, cfg)
        ctl = Tally(2, 2, control_first, n, cfg)
        blow, wi = success_vs_interval(cfg)
    two, deaths = main.two_blow_deaths()
    two_c, deaths_c = ctl.two_blow_deaths()
    print(f"arm {name}: rate {cfg.get('OPPOSITION_RATE', core.OPPOSITION_RATE)}, DMG_SCALE {core.DMG_SCALE if name == 'live' else CONTROL_SCALE}; "
          f"{n} fights at seeds {first}.., controls at {control_first}..")
    print(f"| reading | bar | seeds {first}.. | control seeds {control_first}.. |")
    print("|---|---|---|---|")
    print(f"| 1 a Success vs the Wound Interval | within 1 | {blow} vs {wi} (diff {blow - wi}) | |")
    print(f"| 2 deaths on exactly two blows to the loser | below 70.0% | {100 * two:.1f}% of {deaths} | {100 * two_c:.1f}% of {deaths_c} |")
    print(f"| 3 mean wounding blows | above 3.2 | {main.mean_wounds():.2f} | {ctl.mean_wounds():.2f} |")
    print(f"| 4a lead-change share of decided fights | reported | {main.lead_change():.3f} | {ctl.lead_change():.3f} |")
    print(f"| 4b first-wounded-wins share of decided fights | reported | {main.first_wounded_wins():.3f} | {ctl.first_wounded_wins():.3f} |")
    print(f"| 5 undecided share | under 2% | {100 * main.undecided():.2f}% | {100 * ctl.undecided():.2f}% |")
    print(f"| (mean rounds) | | {main.mean_turns():.2f} | {ctl.mean_turns():.2f} |")


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--arm', default='live', choices=('live', 'control'))
    ap.add_argument('--n', type=int, default=5000)
    ap.add_argument('--first', type=int, default=0)
    ap.add_argument('--control-first', type=int, default=800000)
    a = ap.parse_args()
    census(a.arm, a.n, a.first, a.control_first)
