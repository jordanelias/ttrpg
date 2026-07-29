"""mass_battle.lanchester_signature — P-L Lanchester signature regression tests.

Validates the two attrition laws the P-L substrate introduces, per the design spec
(mb_lanchester_design.md, section four):

  (1) LINEAR signature (melee): casualties ~ ENEMY strength IN CONTACT, frontage-capped,
      so a larger equal-quality force wins by a margin that scales with the size difference
      (the classic linear-law result — numerical superiority is a *linear* edge).
  (2) SQUARE signature (volley): aimed fire lifts the frontage cap, so the casualty-exchange
      ratio is SUPER-linear in the size ratio (N-squared concentration) — distinct from melee.
  (3) NO-ANNIHILATION invariant: battles still terminate by ROUT (the morale/rout system
      decides the end), not by attrition to zero. Lanchester FEEDS morale; it does not replace it.

Requires LANCHESTER_ENABLED on (the engine default). Run:
    PYTHONPATH=tests/sim python3 -m mass_battle.lanchester_signature

All numeric thresholds below are class-B TOLERANCES derived from validated P-L behaviour,
NOT canonical magnitudes; the SIGNATURES are the spec section-four validation plan.
"""
import os, random, statistics

# Lanchester must be ON for the signatures to hold (default ON; assert explicitly).
os.environ.setdefault('LANCHESTER_ENABLED', '1')
os.environ.setdefault('PER_CELL', '0')

from mass_battle.engine import (Subunit, Unit, run_battle,
                                SIDE_A_START_ROW, SIDE_B_START_ROW, LANCHESTER_ENABLED)

# --- signature thresholds (class-B tolerances; signatures per spec §4) ---
LINEAR_MIN_BIG_WIN  = 65       # [canonical: mb_lanchester_design.md §4(2) — linear sig: big-force win%; class-B tolerance]
LINEAR_MIN_CASDIFF  = 20       # [canonical: mb_lanchester_design.md §4(2) — linear sig: casualty diff (small−big); class-B tolerance]
SQUARE_MIN_RATIO    = 4        # [canonical: mb_lanchester_design.md §4(3) — square sig: cas-exchange ratio ≥ (size ratio)² at 2:1; class-B tolerance]
NOANNIH_MAX_CAS     = 60       # [canonical: mb_lanchester_design.md §4(4) — no-annihilation: winner-side casualty% ceiling; class-B tolerance]
BIG_TIER            = 4        # [canonical: mb_lanchester_design.md §4(2) — 2:1 size pair (Tier 4 = 800 vs Tier 2 = 200... here 400 vs 200 at company scale); class-B]
MIRROR_TIER         = 3        # [canonical: mb_lanchester_design.md §4(4) — equal-size mirror baseline; class-B]
SMALL_TIER          = 2        # exempt literal (2): the smaller force in the 2:1 pair
SEED_BASE           = 2000000  # [canonical: mb_lanchester_design.md §4 — deterministic seed base; class-B]
N                   = 100      # exempt literal (100): sample size per matchup

# [JUSTIFIED: deployment anchor columns for Line, copied from tests/sim/gauge_mb.py ANCHOR_MAP
#  ('Line',2)=10 / ('Line',3)=9 / ('Line',4)=8 — mechanism sourced (a per-tier deployment anchor is
#  a real engine concept), magnitudes INHERITED from the gauge and not independently derivable]
# ⚠ ED-MB-0049 (2026-07-29, A5a citation critic): this line previously read
#   `[canonical: mass_battle_v30.md §deployment — gauge ANCHOR_MAP]`. That citation DOES NOT RESOLVE.
#   `mass_battle_v30.md` has no `§deployment` section and no anchor-column table; the only "anchor"
#   hits in it are the Refused-Flank terrain line and settlement anchoring, neither of which is this.
#   Checked whether the values are derivable instead of cited — they are not: measured widths at the
#   shipped config are tier 1/2/3/4 = 3/5/5/7 cells, giving centres 12/12/11/11, so no single
#   centring rule produces 11/10/9/8 (tiers 3-4 sit one column left of it). Re-labelled JUSTIFIED,
#   which is what they are. The same unresolvable citation is still live at its ORIGIN,
#   `tests/sim/gauge_mb.py:60,64,65,66` — out of A5a's scope, filed not chased (Jordan's
#   2026-07-29 directive), see ED-MB-0049.
_LINE_ANCHOR = {SMALL_TIER: 10, MIRROR_TIER: 9, BIG_TIER: 8}  # [JUSTIFIED: gauge_mb.ANCHOR_MAP ('Line',2/3/4) — inherited, see the note above]


def _mk(shape, tier, faction, unit_type='melee', stance='balanced'):
    ad = -1 if faction == 'A' else 1
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type='infantry', tier=tier,
                 starting_position=(sr, _LINE_ANCHOR.get(tier, 10)),
                 advance_dir=ad, unit_type=unit_type)
    # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md — "The v9 targets above use uniform
    #  Power=4, Command=4, Discipline=5, Morale=6 to isolate formation/unit_type effects"]
    # Verified by hand against that file 2026-07-29 (ED-MB-0049, A5a citation critic): the source
    # says exactly this, and it is also `gauge_mb.make_unit`'s default signature, so the harness and
    # the gauge share one baseline rather than two coincidentally-equal ones.
    p, cmd, disc, mor = 4, 4, 5, 6  # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §v9 targets — uniform P4/C4/D5/M6]
    return Unit(name=faction, faction=faction, power=p, command=cmd,
                discipline=disc, discipline_start=disc, morale=mor, morale_start=mor,
                subunits=[su], dr=1, stance=stance, speed='Standard')


def _sweep(big_tier, small_tier, unit_type, stance='balanced'):
    """A = big force, B = small force, equal quality. Returns aggregate stats."""
    aw = ca = cb = ahp = bhp = 0
    cas_a, cas_b, hp_a, hp_b = [], [], [], []
    for s in range(N):
        random.seed(s + SEED_BASE)
        ua = _mk('Line', big_tier, 'A', unit_type, stance)
        ub = _mk('Line', small_tier, 'B', unit_type, stance)
        a0, b0 = ua.hp_max, ub.hp_max
        r = run_battle(ua, ub)
        aw += (r['winner'] == 'A')
        cas_a.append(100 * (a0 - ua.hp) / a0)
        cas_b.append(100 * (b0 - ub.hp) / b0)
        hp_a.append(100 * ua.hp / a0)
        hp_b.append(100 * ub.hp / b0)
    return dict(big_win=aw / N * 100,
                cas_big=statistics.mean(cas_a), cas_small=statistics.mean(cas_b),
                hp_big=statistics.mean(hp_a), hp_small=statistics.mean(hp_b))


def check_linear():
    """Melee 2:1 → big force wins decisively (frontage/durability linear edge)."""
    r = _sweep(BIG_TIER, SMALL_TIER, 'melee')
    casdiff = r['cas_small'] - r['cas_big']
    ok = r['big_win'] >= LINEAR_MIN_BIG_WIN and casdiff >= LINEAR_MIN_CASDIFF
    return ('LINEAR (melee 2:1)', ok,
            f"big_win={r['big_win']:.1f}%% (≥{LINEAR_MIN_BIG_WIN}) "
            f"cas_diff={casdiff:+.1f} (≥{LINEAR_MIN_CASDIFF})")


def check_square():
    """Volley 2:1 → cas-exchange ratio super-linear in size (square concentration)."""
    r = _sweep(BIG_TIER, SMALL_TIER, 'ranged', 'hold')
    ratio = r['cas_small'] / r['cas_big'] if r['cas_big'] > 0 else float('inf')
    ok = ratio >= SQUARE_MIN_RATIO
    return ('SQUARE (volley 2:1)', ok,
            f"cas_exchange small/big={ratio:.1f} (≥{SQUARE_MIN_RATIO}; linear law would give ~{BIG_TIER//SMALL_TIER})")


def check_no_annihilation():
    """Mirror → battle ends by rout, not annihilation (loser hp > 0, casualties bounded)."""
    r = _sweep(MIRROR_TIER, MIRROR_TIER, 'melee')
    worst_cas = max(r['cas_big'], r['cas_small'])
    loser_hp = min(r['hp_big'], r['hp_small'])
    ok = worst_cas <= NOANNIH_MAX_CAS and loser_hp > 0
    return ('NO-ANNIHILATION (mirror)', ok,
            f"max_cas={worst_cas:.1f}%% (≤{NOANNIH_MAX_CAS}) loser_hp={loser_hp:.1f}%% (>0)")


# --- conserved-quantity exponent guard (the rigorous law check) ---
# A no-rout attrition trajectory must conserve A^p−B^p with p≈1 for melee (linear law)
# and p≈2 for volley (square law). This catches law-contamination the win%/cas-diff
# checks above miss (e.g. the Size-based pool emerges at p≈1.7, failing LIN_EXP_MAX).
LIN_EXP_MAX = 1.4   # [canonical: mb_lanchester_design.md §4 — melee must fit linear (p≤1.4), not square; class-B tolerance]
SQ_EXP_MIN  = 1.6   # [canonical: mb_lanchester_design.md §4 — volley must fit square (p≥1.6), not linear; class-B tolerance]
TRAJ_SEEDS  = 40    # [canonical: mb_lanchester_design.md §4 — exponent-fit sample; class-B]
TRAJ_TICKS  = 160   # [canonical: mb_lanchester_design.md §4 — max no-rout ticks; class-B]
NO_ROUT_MORALE = 1e9   # [canonical: mb_lanchester_design.md §4 — huge morale disables rout for pure-attrition measurement; class-B]
TRAJ_FLOOR  = 0.25     # [canonical: mb_lanchester_design.md §4 — stop at 25%% of one block remaining; class-B]
FIT_P_LO, FIT_P_HI, FIT_P_STEP = 0.5, 2.51, 0.05   # [canonical: mb_lanchester_design.md §4 — exponent scan grid; class-B]
BIG_CV = 9.0   # [canonical: mb_lanchester_design.md §4 — CV sentinel (no conservation); class-B]


def _trajectory(big_tier, small_tier, unit_type, stance, diag=None):
    """Mean A/B hp trajectories over TRAJ_SEEDS no-rout battles.

    `diag` (a dict) collects the A5a falsifier evidence: how many trajectories routed despite the
    NO_ROUT_MORALE pin, how many ticks each ran, the fit window that survived, and the non-vacuity
    counter. It is pure observation — nothing in it feeds the fit.
    """
    import statistics
    if diag is None:
        diag = _new_diag()
    series = []
    for s in range(TRAJ_SEEDS):
        random.seed(s + SEED_BASE)
        # [ED-MB-0049 / plan-v2 A5a] The morale pin, swept onto its single owner.
        #
        # This was `ua.morale = ua.morale_start = NO_ROUT_MORALE`, a BARE absolute write — the exact
        # silent-no-op class that confounded the retracted PC_CELL_MORALE measurement (ED-MB-0042):
        # `eff_morale` reads the cells once seeded and never falls back to the scalar, so under the
        # flag this pin would set nothing, bodies would rout mid-signature, and the Lanchester
        # exponent would be fitted on TRUNCATED battles. `Unit.set_morale` is the owner; unseeded
        # (the shipped default) it reduces exactly to `unit.morale = value`, so this is
        # behaviour-identical at PC_CELL_MORALE=0 and correct at =1.
        #
        # ⚠ CARVE-OUT: `morale_start` stays a BARE write and must. It is non-cellular — there is no
        # `cell_morale_start`, `eff_morale_start` derives from the subunit/unit scalar, and no owner
        # exists or should. It is whitelisted in `test_morale_write_sweep._CELL_OWNED['morale']`
        # rather than exempted by silence. Written on its own line, deliberately: the sweep guard is
        # a line-anchored regex and could not see it inside the old `x = _mk(...); x.morale = ...`
        # compound statement — adding this file to the guard's scope without splitting the line
        # would have produced a guard that passes because it cannot look, not because it is clean.
        ua = _mk('Line', big_tier, 'A', unit_type, stance)
        ua.set_morale(NO_ROUT_MORALE)
        ua.morale_start = NO_ROUT_MORALE
        ub = _mk('Line', small_tier, 'B', unit_type, stance)
        ub.set_morale(NO_ROUT_MORALE)
        ub.morale_start = NO_ROUT_MORALE
        bs = ua.hp_max / ua.size_max
        tr = []
        routed_here = False
        for _ in range(TRAJ_TICKS):
            run_battle(ua, ub, max_turns=1)
            tr.append((ua.hp, ub.hp))
            # [ED-MB-0049 / A5a falsifier] The pin's WHOLE PURPOSE is "no rout, pure attrition".
            # Record whether it held, per trajectory, instead of assuming it. `checked` is the
            # non-vacuity counter (§0.1 #2): a loop that only asserts conditionally must assert
            # that it asserted, or an empty loop reads as a pass.
            diag['checked'] += 1
            if ua.routed or ub.routed:
                routed_here = True
            if ua.hp <= TRAJ_FLOOR * bs or ub.hp <= TRAJ_FLOOR * bs or ua.routed or ub.routed:
                break
        if routed_here:
            diag['routed_trajectories'] += 1
        diag['ticks'].append(len(tr))
        series.append(tr)
    L = min(len(x) for x in series)
    A = [statistics.mean(series[s][t][0] for s in range(TRAJ_SEEDS)) for t in range(L)]
    B = [statistics.mean(series[s][t][1] for s in range(TRAJ_SEEDS)) for t in range(L)]
    diag['fit_window'] = L
    return A, B


def _new_diag():
    return {'checked': 0, 'routed_trajectories': 0, 'ticks': [], 'fit_window': 0}


def _best_exponent(A, B):
    import statistics
    pts = [(a, b) for a, b in zip(A, B) if a > 0 and b > 0][1:]
    best_p, best_cv = None, BIG_CV
    p = FIT_P_LO
    while p <= FIT_P_HI:
        C = [a**p - b**p for a, b in pts]
        m = statistics.mean(C)
        cv = statistics.pstdev(C) / abs(m) if m else BIG_CV
        if cv < best_cv:
            best_p, best_cv = round(p, 2), cv
        p += FIT_P_STEP
    return best_p


def check_law_exponents():
    """Rigorous: melee must conserve the LINEAR difference (p≤1.4), volley the SQUARE
    difference (p≥1.6). Requires the Command-only base (COMMAND_SIGMA on); the Size-based
    pool contaminates melee to p≈1.7 and FAILS this guard by design.

    [ED-MB-0049 / A5a] Returns a fourth element: the per-arm PRECONDITION diagnostic. An exponent
    fitted on trajectories that ROUTED is fitted on truncated data and is not an estimate of
    anything — so the precondition is reported next to the number, never assumed behind it (G4:
    verify the instrument before quoting its number).
    """
    dm, dv = _new_diag(), _new_diag()
    pm = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'melee', 'balanced', diag=dm))
    pv = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'ranged', 'hold', diag=dv))
    ok = pm <= LIN_EXP_MAX and pv >= SQ_EXP_MIN
    return ('LAW EXPONENTS (linear/square)', ok,
            f"melee p={pm:.2f} (≤{LIN_EXP_MAX} linear) volley p={pv:.2f} (≥{SQ_EXP_MIN} square)",
            {'melee': dm, 'volley': dv})


def run():
    assert LANCHESTER_ENABLED, "signatures require LANCHESTER_ENABLED=1"
    results = [check_linear(), check_square(), check_no_annihilation(), check_law_exponents()]
    print("=== P-L Lanchester signature tests (PER_CELL=%s) ===" % os.environ.get('PER_CELL'))
    allok = True
    for row in results:
        name, ok, detail = row[0], row[1], row[2]
        allok = allok and ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name:26} {detail}")
        # [ED-MB-0049 / A5a] The precondition diagnostic, printed BESIDE the number it qualifies.
        # A rout-truncated fit is not an estimate; quoting the exponent without this line is how
        # `melee p=2.50` entered the record as an engine property (G4).
        for arm, d in (row[3] if len(row) > 3 else {}).items():
            n = TRAJ_SEEDS
            assert d['checked'] >= n, (
                f"non-vacuity: the {arm} trajectory loop ran {d['checked']} ticks over {n} seeds — "
                f"fewer than one tick per seed means the precondition was never actually observed")
            flag = 'OK' if d['routed_trajectories'] == 0 else 'PRECONDITION VIOLATED'
            print(f"           {arm:>7} no-rout pin: {flag} — "
                  f"{d['routed_trajectories']}/{n} trajectories routed, "
                  f"fit window {d['fit_window']} ticks "
                  f"(min/median/max per-seed ticks "
                  f"{min(d['ticks'])}/{statistics.median(d['ticks']):.0f}/{max(d['ticks'])})")
    print(f"  => {'ALL PASS' if allok else 'FAILURES PRESENT'} ({sum(1 for r in results if r[1])}/{len(results)})")
    return allok


if __name__ == '__main__':
    import sys
    sys.exit(0 if run() else 1)
