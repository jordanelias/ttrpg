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


_REMAP = {'A': 'B', 'B': 'A', 'draw': 'draw'}   # run_battle winner is by arg-POSITION; remap to config when args are swapped


def _one_mirror(tier, seed, swap, unit_kw):
    """One mirror battle at (tier, seed). swap=False: configA is unit_a (drawn first);
    swap=True: configA is unit_b (drawn second). Returns (winner_by_CONFIG, configA_hp_pct)."""
    random.seed(seed)
    a = make_unit('A', tier=tier, **unit_kw)
    b = make_unit('B', tier=tier, **unit_kw)
    if not swap:
        r = run_battle(a, b, max_turns=_ENGAGEMENT_TICKS); win = r['winner']
    else:
        r = run_battle(b, a, max_turns=_ENGAGEMENT_TICKS); win = _REMAP[r['winner']]
    return win, (a.hp / a.hp_max * 100 if a.hp_max else 0)


def mirror_sweep(tier, n_seeds=_SEEDS, cancel_order=True, **unit_kw):
    """Identical configs A vs B across seeds; wins tallied by CONFIG.

    cancel_order=True (default): each seed is run in BOTH arg-orders and counted by config, so the
    known second-mover RNG-stream-order bias (the engine defect, fix deferred per decision C) CANCELS
    in measurement -- the engine itself is left byte-exact. A symmetric engine then gives ~50/50 by
    config; a residual config win-rate gap here is a REAL effect, not the order artifact. This is the
    valid symmetry / small-pool-variance stress tool.

    cancel_order=False: single arg-order (configA first) -- EXPOSES the raw order skew (diagnostic).

    Returns dict(a_wins, b_wins, draws, a_hp_mean, a_hp_std, skew, trials)."""
    orders = (False, True) if cancel_order else (False,)
    wins, hp = [], []
    for s in range(n_seeds):
        for swap in orders:
            w, h = _one_mirror(tier, s, swap, unit_kw)
            wins.append(w); hp.append(h)
    aw = wins.count('A'); bw = wins.count('B'); dr = wins.count('draw')
    return dict(a_wins=aw, b_wins=bw, draws=dr,
                a_hp_mean=statistics.mean(hp), a_hp_std=statistics.pstdev(hp),
                skew=abs(aw - bw), trials=len(wins))


def stress_suite():
    """Default stress suite: mirror symmetry (order-cancelled) + small-pool variance across tiers."""
    print("=== mirror symmetry + small-pool variance (Line, %d seeds, order-cancelled) ===" % _SEEDS)
    print("    (identical configs A vs B, wins by config over BOTH arg-orders: expect ~50/50)")
    for tier in sorted(TROOPS_PER_TIER):
        r = mirror_sweep(tier, cancel_order=True)
        raw = mirror_sweep(tier, cancel_order=False)
        mark = "  <-- RESIDUAL ASYMMETRY" if r['skew'] > _SKEW_FLAG else ""
        print(f"  tier{tier} pool{TROOPS_PER_TIER[tier]:>4}: "
              f"A{r['a_wins']}/B{r['b_wins']}/D{r['draws']} ({r['trials']} trials)  "
              f"A_hp mean={r['a_hp_mean']:>3.0f} std={r['a_hp_std']:>2.0f}  "
              f"cancelled-skew={r['skew']}{mark}   [raw 1-order skew={raw['skew']}]")
    print("    raw skew = the known second-mover RNG-order bias (engine defect; fix deferred per decision C).")
    print("    cancelled-skew ~0 confirms the engine is otherwise symmetric and the measurement is now valid.")


if __name__ == '__main__':
    stress_suite()
