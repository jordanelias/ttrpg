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
from mass_battle.resolution import start_trace, get_trace

# --- test fixtures (stress-harness inputs, NOT engine mechanics) ---
_PWR = 4; _CMD = 4; _DISC = 5; _MOR = 6; _DR = 1   # [class-B test-fixture: neutral mid-scale actor]
_EDGE_GAP = 16                                      # step-2 rescale (50-grid): fit 10k formation + closing gap
_COL = BATTLEFIELD_SIZE // 2                         # field-centre column (symmetric)
_ENGAGEMENT_TICKS = 18                               # [class-B one-engagement cap (3 phases), per run_battle]
_SEEDS = 20                                          # stress seeds per cell (harness loop count, not a mechanic)
_SKEW_FLAG = 5                                       # [class-B test-param: |A-B| wins above this flags asymmetry]


def make_unit(faction, troop='infantry', unit_type='melee', tier=4,
              shape='Line', instructions=(), speed='Standard', stance='balanced',
              power=None, command=None, discipline=None, morale=None, dr=None,
              troops=None, concentration=None):
    """Build a deployed test unit. 'A' starts near the high-row edge facing in; 'B' mirrors it.
    Stat args default to the module fixtures (None -> _PWR/_CMD/_DISC/_MOR/_DR); override to sweep.
    Set troops+concentration for a continuous-scale unit (footprint via footprint_for); both None -> tier path."""
    ad = -1 if faction == 'A' else 1
    row = (BATTLEFIELD_SIZE - _EDGE_GAP) if faction == 'A' else (_EDGE_GAP - 1)
    pwr = _PWR if power is None else power
    cmd = _CMD if command is None else command
    dis = _DISC if discipline is None else discipline
    mor = _MOR if morale is None else morale
    drv = _DR if dr is None else dr
    su = Subunit(shape=shape, troop_type=troop, tier=tier, starting_position=(row, _COL),
                 advance_dir=ad, unit_type=unit_type, instructions=instructions,
                 troops=troops, concentration=concentration)
    return Unit(name=faction, faction=faction, power=pwr, command=cmd,
                discipline=dis, discipline_start=dis, morale=mor, morale_start=mor,
                subunits=[su], dr=drv, stance=stance, speed=speed)


def _state(u):
    return dict(hp=round(u.hp / u.hp_max * 100, 1) if getattr(u, 'hp_max', 0) else 0,
                mor=round(getattr(u, 'morale', 0), 2),
                stam=getattr(u, 'stamina', None),
                rout=getattr(u, 'routed', False))


def _snapshot(unit_a, unit_b, tick):
    d = min((_atom_distance(sa, sb) for sa in unit_a.subunits for sb in unit_b.subunits),
            default=None)
    return dict(tick=tick, dist=d, A=_state(unit_a), B=_state(unit_b))


def trace_battle(unit_a, unit_b, ticks=_ENGAGEMENT_TICKS, mechanical=True):
    """Tick-by-tick mechanical trace of one engagement. Mutates the units (persistent state).
    With mechanical=True each tick's snapshot also carries the per-MECHANIC events (melee contest
    pools/sigma/nets/degrees, volley fire detail) from that tick, via the engine's passive
    observe-only trace collector (byte-exact; ON==OFF). Returns (trace, final_result);
    trace[0] is the pre-combat snapshot."""
    trace = [_snapshot(unit_a, unit_b, 0)]
    result = None
    for t in range(1, ticks + 1):
        if mechanical:
            start_trace(True)
        result = run_battle(unit_a, unit_b, max_turns=1)
        snap = _snapshot(unit_a, unit_b, t)
        if mechanical:
            snap['mech'] = [e for e in get_trace() if e['cat'] in ('melee', 'volley')]
        trace.append(snap)
        if unit_a.routed or unit_b.routed:
            break
    if mechanical:
        start_trace(False)   # leave the collector off after tracing
    return trace, result


def format_trace(trace):
    """Human-readable audit log of a trace_battle() result: per-tick state + per-mechanic detail."""
    out = []
    for s in trace:
        flag = ('  A-ROUT' if s['A']['rout'] else '') + ('  B-ROUT' if s['B']['rout'] else '')
        out.append(f"t{s['tick']:>2} d={s['dist']}  "
                   f"A hp{s['A']['hp']:>5} m{s['A']['mor']:>4} st{s['A']['stam']}  "
                   f"B hp{s['B']['hp']:>5} m{s['B']['mor']:>4} st{s['B']['stam']}{flag}")
        for e in s.get('mech', []):
            if e['cat'] == 'melee':
                out.append(f"        melee  pool A{e['a_pool']}/B{e['b_pool']}  "
                           f"sigma A{e['ns_a']:+}/B{e['ns_b']:+}  "
                           f"net A{e['a_net']}/B{e['b_net']}  deg A={e['a_deg']}/B={e['b_deg']}")
            elif e['cat'] == 'volley':
                out.append(f"        volley {e['shooter']}  d{e['d']} pool{e['pool']} "
                           f"net{e['net']}->dr{e['net_dr']} dens{e['dens']} loss{e['loss']}")
    return "\n".join(out)


_REMAP = {'A': 'B', 'B': 'A', 'draw': 'draw'}   # run_battle winner is by arg-POSITION; remap to config when args are swapped


def _one_battle(tier, seed, swap, a_kw, b_kw):
    """One battle: configA (a_kw overrides) vs configB (b_kw overrides). swap=False -> configA is
    unit_a (drawn first); swap=True -> configA is unit_b (drawn second). Returns
    (winner_by_CONFIG, configA_hp_pct)."""
    random.seed(seed)
    a = make_unit('A', tier=tier, **a_kw)
    b = make_unit('B', tier=tier, **b_kw)
    if not swap:
        r = run_battle(a, b, max_turns=_ENGAGEMENT_TICKS); win = r['winner']
    else:
        r = run_battle(b, a, max_turns=_ENGAGEMENT_TICKS); win = _REMAP[r['winner']]
    return win, (a.hp / a.hp_max * 100 if a.hp_max else 0)


def config_sweep(tier, a_kw=None, b_kw=None, n_seeds=_SEEDS, cancel_order=True):
    """configA(a_kw) vs configB(b_kw) across seeds; wins tallied by CONFIG. a_kw/b_kw are make_unit
    overrides (e.g. {'discipline': 6}); None -> {} (the make_unit baseline). cancel_order=True
    (default) runs each seed in BOTH arg-orders so the second-mover RNG-order bias cancels in
    measurement -> a residual A/B win gap is a REAL config effect, not the order artifact.
    Returns dict(a_wins, b_wins, draws, a_hp_mean, a_hp_std, skew, trials)."""
    a_kw = a_kw or {}; b_kw = b_kw or {}
    orders = (False, True) if cancel_order else (False,)
    wins, hp = [], []
    for s in range(n_seeds):
        for swap in orders:
            w, h = _one_battle(tier, s, swap, a_kw, b_kw)
            wins.append(w); hp.append(h)
    aw = wins.count('A'); bw = wins.count('B'); dr = wins.count('draw')
    return dict(a_wins=aw, b_wins=bw, draws=dr,
                a_hp_mean=statistics.mean(hp), a_hp_std=statistics.pstdev(hp),
                skew=abs(aw - bw), trials=len(wins))


def mirror_sweep(tier, n_seeds=_SEEDS, cancel_order=True, **unit_kw):
    """Identical configs A vs B (config_sweep with a_kw == b_kw == unit_kw). A symmetric engine ->
    ~50/50 by config with cancel_order; the small-pool A_hp variance is the other signal."""
    return config_sweep(tier, a_kw=dict(unit_kw), b_kw=dict(unit_kw),
                         n_seeds=n_seeds, cancel_order=cancel_order)


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


def ners_dimensions(n_seeds=_SEEDS):
    """NERS stress dimensions beyond mirror symmetry, via order-cancelled config_sweep:
    modifier impact across scale (non-uniformity), a stat response curve (threshold-cliff check),
    and edge->advantage scaling (runaway / loop-gain). configB advantage in percentage points =
    (configB_wins - configA_wins) / trials. Prints a report."""
    def gap(r):
        return 100 * (r['b_wins'] - r['a_wins']) / r['trials']
    tiers = sorted(TROOPS_PER_TIER)
    print("=== NERS modifier impact across scale (configB advantage pp; scale-invariant => uniform) ===")
    for stat, base in (('power', _PWR), ('discipline', _DISC), ('morale', _MOR)):
        cells = [f"t{t}:{gap(config_sweep(t, b_kw={stat: base + 1}, n_seeds=n_seeds)):>+4.0f}" for t in tiers]
        print(f"  +1 {stat:<10}: " + "  ".join(cells))
    print("=== NERS discipline response curve, top tier (smooth => no threshold cliff) ===")
    top = tiers[-1]; prev = None
    for d in range(_DISC - 2, _DISC + 3):
        g = gap(config_sweep(top, a_kw={'discipline': _DISC}, b_kw={'discipline': d}, n_seeds=n_seeds))
        step = f"  step{g - prev:>+4.0f}" if prev is not None else ""
        print(f"  configB disc{d}: {g:>+4.0f}pp{step}"); prev = g
    print("=== NERS edge -> advantage, top tier (proportional => damped, not a runaway loop) ===")
    for dp in (1, 2, 3):
        print(f"  +{dp} power: {gap(config_sweep(top, b_kw={'power': _PWR + dp}, n_seeds=n_seeds)):>+4.0f}pp")


if __name__ == '__main__':
    stress_suite()
    print()
    ners_dimensions()
