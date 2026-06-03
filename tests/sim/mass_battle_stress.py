"""Mass-battle stress-test + mechanical logging harness.

NON-INVASIVE by design: it drives the engine tick-by-tick via run_battle(max_turns=1)
-- the canonical multi-turn driver -- and snapshots unit state after each tick, leaving
the validated engine completely untouched. Verified byte-exact: run_battle(N) produces
identical final state to N x run_battle(1) (so a per-tick trace faithfully represents the
real engagement). Because the engine is not modified, this harness can never change a
result -- it can only observe.

Two layers:
  trace_battle()  -> per-tick mechanical trace (hp / morale / stamina / distance / rout):
                     an auditable record of WHY a single engagement resolved as it did.
  mirror_sweep()  -> symmetry + small-pool-variance stress signal. Identical units fight as
                     A vs B; a symmetric, emergent engine should give ~50/50 win rates and
                     bounded outcome variance. Side-skew or exploding variance is a defect.

Run:  PER_CELL=1 PYTHONPATH=<dir-containing-mass_battle> python3 -m mass_battle_stress
"""
import statistics
import random
from mass_battle.engine import Subunit, Unit, run_battle
from mass_battle.orchestration import _atom_distance
from mass_battle.config import BATTLEFIELD_SIZE, TROOPS_PER_TIER

# --- test fixtures (stress-harness inputs, NOT engine mechanics) ---
_PWR = 4; _CMD = 4; _DISC = 5; _MOR = 6; _DR = 1   # [class-B test-fixture: neutral mid-scale actor]
_EDGE_GAP = 9                                       # [class-B test-param: start gap from each edge]
_COL = BATTLEFIELD_SIZE // 2                         # field-centre column (symmetric)
_ENGAGEMENT_TICKS = 18                               # [class-B one-engagement cap (3 phases), per run_battle]
_SEEDS = 20                                          # stress seeds per cell (harness loop count, not a mechanic)
_SKEW_FLAG = 5                                       # [class-B test-param: |A-B| wins above this flags asymmetry]


def make_unit(faction, troop='infantry', unit_type='melee', tier=4,
              shape='Line', instructions=(), speed='Standard', stance='balanced'):
    """Build a deployed test unit. 'A' starts near the high-row edge facing in; 'B' mirrors it."""
    ad = -1 if faction == 'A' else 1
    row = (BATTLEFIELD_SIZE - _EDGE_GAP) if faction == 'A' else (_EDGE_GAP - 1)
    su = Subunit(shape=shape, troop_type=troop, tier=tier, starting_position=(row, _COL),
                 advance_dir=ad, unit_type=unit_type, instructions=instructions)
    return Unit(name=faction, faction=faction, power=_PWR, command=_CMD,
                discipline=_DISC, discipline_start=_DISC, morale=_MOR, morale_start=_MOR,
                subunits=[su], dr=_DR, stance=stance, speed=speed)


def _state(u):
    return dict(hp=round(u.hp / u.hp_max * 100, 1) if getattr(u, 'hp_max', 0) else 0,
                mor=round(getattr(u, 'morale', 0), 2),
                stam=getattr(u, 'stamina', None),
                rout=getattr(u, 'routed', False))


def _snapshot(unit_a, unit_b, tick):
    d = min((_atom_distance(sa, sb) for sa in unit_a.subunits for sb in unit_b.subunits),
            default=None)
    return dict(tick=tick, dist=d, A=_state(unit_a), B=_state(unit_b))


def trace_battle(unit_a, unit_b, ticks=_ENGAGEMENT_TICKS):
    """Tick-by-tick mechanical trace of one engagement. Mutates the units (persistent state).
    Returns (trace, final_result). trace[0] is the pre-combat snapshot."""
    trace = [_snapshot(unit_a, unit_b, 0)]
    result = None
    for t in range(1, ticks + 1):
        result = run_battle(unit_a, unit_b, max_turns=1)
        trace.append(_snapshot(unit_a, unit_b, t))
        if unit_a.routed or unit_b.routed:
            break
    return trace, result


def format_trace(trace):
    """Human-readable audit log of a trace_battle() result."""
    out = []
    for s in trace:
        flag = ('  A-ROUT' if s['A']['rout'] else '') + ('  B-ROUT' if s['B']['rout'] else '')
        out.append(f"t{s['tick']:>2} d={s['dist']}  "
                   f"A hp{s['A']['hp']:>5} m{s['A']['mor']:>4} st{s['A']['stam']}  "
                   f"B hp{s['B']['hp']:>5} m{s['B']['mor']:>4} st{s['B']['stam']}{flag}")
    return "\n".join(out)


def mirror_sweep(tier, n_seeds=_SEEDS, **unit_kw):
    """Identical units A vs B across seeds. A symmetric engine -> ~50/50 wins, bounded A_hp std.
    Returns dict(a_wins, b_wins, draws, a_hp_mean, a_hp_std, skew)."""
    rows = []
    for s in range(n_seeds):
        random.seed(s)
        a = make_unit('A', tier=tier, **unit_kw)
        b = make_unit('B', tier=tier, **unit_kw)
        r = run_battle(a, b, max_turns=_ENGAGEMENT_TICKS)
        rows.append((r['winner'], a.hp / a.hp_max * 100 if a.hp_max else 0))
    aw = sum(w == 'A' for w, _ in rows)
    bw = sum(w == 'B' for w, _ in rows)
    dr = sum(w == 'draw' for w, _ in rows)
    hp = [h for _, h in rows]
    return dict(a_wins=aw, b_wins=bw, draws=dr,
                a_hp_mean=statistics.mean(hp), a_hp_std=statistics.pstdev(hp),
                skew=abs(aw - bw))


def stress_suite():
    """Default stress suite: mirror-match symmetry + small-pool variance across tiers."""
    print("=== mirror-match symmetry + small-pool variance (Line, %d seeds) ===" % _SEEDS)
    print("    (identical A vs B: expect ~50/50 and bounded variance; side-skew = defect)")
    for tier in sorted(TROOPS_PER_TIER):
        r = mirror_sweep(tier)
        mark = "  <-- SIDE-SKEW" if r['skew'] > _SKEW_FLAG else ""
        print(f"  tier{tier} pool{TROOPS_PER_TIER[tier]:>4}: "
              f"A{r['a_wins']}/B{r['b_wins']}/D{r['draws']}  "
              f"A_hp mean={r['a_hp_mean']:>3.0f} std={r['a_hp_std']:>2.0f}  "
              f"skew={r['skew']}{mark}")


if __name__ == '__main__':
    stress_suite()
