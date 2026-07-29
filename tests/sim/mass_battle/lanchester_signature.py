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
import contextlib
import os, random, statistics

# Lanchester must be ON for the signatures to hold (default ON; assert explicitly).
os.environ.setdefault('LANCHESTER_ENABLED', '1')
os.environ.setdefault('PER_CELL', '0')

from mass_battle.config import BLOCK_SIZE   # [ED-MB-0050 / A6a] the annihilation threshold
from mass_battle.engine import (Subunit, Unit, run_battle,
                                SIDE_A_START_ROW, SIDE_B_START_ROW, LANCHESTER_ENABLED)
import mass_battle.core.state as _state   # [ED-MB-0050 / A6a] patched by _rout_disabled below

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


def _mk(shape, tier, faction, unit_type='melee', stance='balanced', instructions=()):
    ad = -1 if faction == 'A' else 1
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type='infantry', tier=tier,
                 starting_position=(sr, _LINE_ANCHOR.get(tier, 10)),
                 advance_dir=ad, unit_type=unit_type, instructions=tuple(instructions))
    # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md — "The v9 targets above use uniform
    #  Power=4, Command=4, Discipline=5, Morale=6 to isolate formation/unit_type effects"]
    # Verified by hand against that file 2026-07-29 (ED-MB-0049, A5a citation critic): the source
    # says exactly this, and it is also `gauge_mb.make_unit`'s default signature, so the harness and
    # the gauge share one baseline rather than two coincidentally-equal ones.
    p, cmd, disc, mor = 4, 4, 5, 6  # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §v9 targets — uniform P4/C4/D5/M6]
    return Unit(name=faction, faction=faction, power=p, command=cmd,
                discipline=disc, discipline_start=disc, morale=mor, morale_start=mor,
                subunits=[su], dr=1, stance=stance, speed='Standard')


def _sweep(big_tier, small_tier, unit_type, stance='balanced', instructions=()):
    """A = big force, B = small force, equal quality. Returns aggregate stats."""
    aw = ca = cb = ahp = bhp = 0
    cas_a, cas_b, hp_a, hp_b = [], [], [], []
    for s in range(N):
        random.seed(s + SEED_BASE)
        ua = _mk('Line', big_tier, 'A', unit_type, stance, instructions)
        ub = _mk('Line', small_tier, 'B', unit_type, stance, instructions)
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
    """Volley 2:1 → cas-exchange ratio super-linear in size (square concentration).

    [ED-MB-0050 / A6a] Scenario repaired: was `stance='hold'`, under which neither archer body ever
    closed and BOTH sides took 0.0% casualties — so the `inf` this reported was a 0/0 guard and the
    PASS was degenerate. `VOLLEY_STANCE` + `VOLLEY_INSTRUCTIONS` (balanced + kite) make the exchange
    actually fire while keeping melee engagements at zero; see the measurement table above.
    A `cas_big == 0` result is now reported as a FAILED PRECONDITION rather than as `inf`, because
    "nothing happened" must never again be able to pass a super-linearity check.
    """
    r = _sweep(BIG_TIER, SMALL_TIER, 'ranged', VOLLEY_STANCE, VOLLEY_INSTRUCTIONS)
    fired = r['cas_big'] > 0 or r['cas_small'] > 0
    if not fired:
        return ('SQUARE (volley 2:1)', False,
                "PRECONDITION FAILED — 0.0%% casualties on BOTH sides: no exchange occurred, so there "
                "is no ratio to test (this is what `inf` used to hide)")
    ratio = r['cas_small'] / r['cas_big'] if r['cas_big'] > 0 else float('inf')
    ok = ratio >= SQUARE_MIN_RATIO
    return ('SQUARE (volley 2:1)', ok,
            f"cas_exchange small/big={ratio:.1f} (≥{SQUARE_MIN_RATIO}; linear law would give "
            f"~{BIG_TIER//SMALL_TIER}) [cas big={r['cas_big']:.2f}%% small={r['cas_small']:.2f}%%]")


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
#
# ⚠ ED-MB-0050 (2026-07-29, A6a citation critic) — THE WHOLE BLOCK BELOW WAS MIS-CITED.
# Every constant here carried `[canonical: mb_lanchester_design.md §4 — …]`. That section is a
# FIVE-ITEM PROSE VALIDATION PLAN (re-tune to hold bands · a linear-signature row · a square-
# signature row · a no-annihilation invariant · re-validate both PER_CELL modes). It specifies NO
# trajectory protocol, NO tick budget, NO morale pin, NO fit grid, NO conserved-quantity method and
# NO exponent bars — the words "1.4" and "1.6" do not appear in it, and its only exponent statement
# is "linear melee / square volley per Jordan's confirm (not blended 1.5). Locked." The
# conserved-quantity apparatus is a LATER addition whose provenance was written to point at a
# section that does not contain it. Re-labelled `[JUSTIFIED: …]` — mechanism sourced (the linear/
# square split IS Jordan-confirmed in §6), magnitudes fitted here. Checked by hand against the
# actual file, not inferred. The four class-B tolerances at the top of this module are a WEAKER
# case of the same thing (§4 describes those two tests but names no numbers) — left in place and
# filed rather than swept, per §0.1 #5.
LIN_EXP_MAX = 1.4   # [JUSTIFIED: melee must fit linear, not square — the split is Jordan-confirmed in mb_lanchester_design.md §6; the 1.4 bar is a fitted tolerance, not a canonical magnitude]
SQ_EXP_MIN  = 1.6   # [JUSTIFIED: volley must fit square, not linear — same source for the split; the 1.6 bar is a fitted tolerance]
TRAJ_SEEDS  = 40    # [JUSTIFIED: exponent-fit sample size, chosen here; no external source]
TRAJ_TICKS  = 160   # [JUSTIFIED: tick budget for a no-rout trajectory, chosen here; no external source]
NO_ROUT_MORALE = 1e9   # [JUSTIFIED: a morale pin far above any reachable value — necessary but NOT sufficient to disable rout, see _rout_disabled]
# [JUSTIFIED: derived from BLOCK_SIZE, the engine's own annihilation threshold — see the note below]
# ⚠ ED-MB-0050 (2026-07-29, A6a): the old value was `TRAJ_FLOOR = 0.25`, tagged
#   `[canonical: mb_lanchester_design.md §4 — stop at 25% of one block remaining]`. TWO problems.
#   (1) THE STOP WAS UNREACHABLE. `bs = hp_max / size_max` measures BLOCK_SIZE (=100), so the stop
#       fired at hp<=25 — but `Unit.recalc_size` sets `size = floor(hp/BLOCK_SIZE)` and routs the unit
#       outright at `size == 0`, i.e. at hp < 100. The engine therefore ALWAYS annihilation-routed
#       ~4x before the trajectory's own floor could trigger. Measured with stochastic rout already
#       disabled: side B routed at ticks 36/35/36 with hp 97.3/97.1/98.9, size 0, agg_morale 1e9,
#       troop_total 400 (well above SUBUNIT_ROUT_FLOOR=80) — annihilation, not morale, not the
#       casualty break-point. This is a THIRD truncation mechanism, beyond the two plan-v2 A6a named.
#   (2) THE CITATION DOES NOT RESOLVE. `mb_lanchester_design.md` §4 is a five-item prose validation
#       plan; it specifies no trajectory protocol, no floor, no tick budget, no fit grid and no
#       exponent bar. See the block comment above LIN_EXP_MAX.
#   Repaired to the engine-derived threshold: stop while both sides still field at least one block,
#   which is the largest window in which the pure-attrition premise actually holds.
TRAJ_FLOOR_BLOCKS = 1.0
# [JUSTIFIED: scan grid widened 2026-07-29 (ED-MB-0050 / A6a) until the optimum is INTERIOR for both
#  arms — the previous ceiling of 2.51 was itself the reported "melee p=2.50" (see _best_exponent)]
# ⚠ The old ceiling was the finding. On the repaired, untruncated data the melee cv objective is
#   MONOTONE decreasing all the way to 2.50 (0.2075 at p=0.5 → 0.0318 at p=2.50), so "p=2.50" was
#   the grid edge, not an estimate — exactly as plan-v2 A6a says. Extending the grid resolves it:
#   melee has a clean interior minimum at p=3.20 (cv 0.00245) and volley at p=2.00 (cv 0.00327).
#   6.0 leaves ≥2.8 of headroom above the larger of the two, so the ceiling is no longer load-bearing.
FIT_P_LO, FIT_P_HI, FIT_P_STEP = 0.5, 6.01, 0.05  # [JUSTIFIED: scan range/step, chosen so the optimum is interior for both arms; no external source]
BIG_CV = 9.0   # [JUSTIFIED: sentinel for "no conservation at any p"; a magnitude large enough to lose every comparison, not a measured quantity]


# ── [ED-MB-0050 / plan-v2 A6a] The two repairs that make this harness measure what it claims ──
#
# REPAIR 1 — the no-rout pin did not disable rout. `NO_ROUT_MORALE = 1e9` is a MORALE pin, but
# `core.state._stochastic_break` keys on the CASUALTY FRACTION and never reads morale at all
# (`return loss_frac >= bp`, where bp is drawn in the [ROUT_ONSET_FRAC, ROUT_CAP_FRAC] band). That
# mechanism landed 2026-07-23 (ED-MB-0031) and defaulted ON 2026-07-25 — one day before the audits —
# and silently invalidated every exponent this file produces. Measured before the repair: 40/40 melee
# trajectories routed, fit window 30 ticks of 160. `PC_STOCHASTIC_ROUT` is the flag that owns that
# break-point, so the pin is completed by turning it off FOR THE TRAJECTORY WINDOW ONLY — the other
# three checks are statements about SHIPPED behaviour and keep rout on (check_no_annihilation is
# literally "the battle ends by rout", which would be vacuous without it).
#
# REPAIR 2 — the volley scenario never fired. `stance='hold'` early-returns from all steering, spawn
# separation is 19 rows and VOLLEY_MAX_RANGE is 8, so neither archer body ever closed: measured 0
# melee engagements AND 0.0 volley loss over 10 battles — the `cas_exchange=inf` in check_square is a
# 0/0 guard, not a super-linear result. Repaired by changing the SCENARIO, not `hold` semantics
# (plan-v2 D4: `hold` is load-bearing for freeze_wings / the refused flank / STANCE_COMMITMENT, and
# `STANCE_SPEED_MOD['hold'] = -99` independently zeroes `step`, so it is a two-gate change).
# `stance='balanced'` + the existing `kite` band-seeking primitive, reused verbatim — no new
# mechanism, no new magnitude.
#
# The scenario choice is MEASURED, not assumed. Over 10 battles each:
#     hold                : melee engagements   0, volley loss a=0.00   b=0.00     ← nothing happens
#     balanced            : melee engagements  69, volley loss a=16.42  b=71.85    ← CONTAMINATED
#     balanced + kite     : melee engagements   0, volley loss a=49.97  b=243.53   ← pure volley
# `balanced` alone closes to contact and mixes the melee law into a square-law test, which is exactly
# what this check must not do. `balanced + kite` holds the band and exchanges only fire.
VOLLEY_STANCE = 'balanced'
VOLLEY_INSTRUCTIONS = ('kite',)


@contextlib.contextmanager
def _rout_disabled():
    """Turn the casualty-fraction break-point OFF for the enclosed block, then restore.

    Patches the name where it is READ (`core.state`), because that module star-imports the constant
    from config and consults its own module global at call time. Restores unconditionally, so a
    raising body cannot leak a disabled rout into the checks that need it on.
    """
    prev = _state.PC_STOCHASTIC_ROUT
    _state.PC_STOCHASTIC_ROUT = False
    try:
        yield
    finally:
        _state.PC_STOCHASTIC_ROUT = prev


def _trajectory(big_tier, small_tier, unit_type, stance, diag=None, instructions=()):
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
        ua = _mk('Line', big_tier, 'A', unit_type, stance, instructions)
        ua.set_morale(NO_ROUT_MORALE)
        ua.morale_start = NO_ROUT_MORALE
        ub = _mk('Line', small_tier, 'B', unit_type, stance, instructions)
        ub.set_morale(NO_ROUT_MORALE)
        ub.morale_start = NO_ROUT_MORALE
        # [ED-MB-0050 / A6a] Floor against BLOCK_SIZE, the engine's annihilation threshold, not
        # against a fraction of it — see TRAJ_FLOOR_BLOCKS.
        hp_floor = TRAJ_FLOOR_BLOCKS * BLOCK_SIZE
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
            # [ED-MB-0050 / A6a] Order matters, and getting it wrong is how "40/40 routed" stayed
            # ambiguous. Reaching the attrition floor is a CLEAN stop — the trajectory has run out
            # of the regime it was measuring. `Unit.recalc_size` also flips `routed` at that same
            # moment (size hits 0 just below one block), so testing `routed` first would score every
            # clean termination as a precondition violation. A violation is a rout that happens
            # while BOTH sides are still above the floor: that is the pin failing to do its job.
            at_floor = ua.hp <= hp_floor or ub.hp <= hp_floor
            if (ua.routed or ub.routed) and not at_floor:
                routed_here = True
            if at_floor or ua.routed or ub.routed:
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
    """Scan p for the exponent that best conserves A^p − B^p; return (p, cv, identifiable).

    [ED-MB-0050 / A6a] `identifiable` is the third return value and it is the point of this repair.
    An argmin that lands on a grid ENDPOINT is not an estimate — it is the statement "the objective
    was still improving when I stopped looking". Reporting one as a number is how `melee p=2.50`
    (the old FIT_P_HI of 2.51) entered the record as an engine property, survived two audits, and
    got quoted in a handoff. The scan now reports whether the optimum is interior, and
    `check_law_exponents` refuses to pass on a non-identifiable fit however favourable its value.
    """
    import statistics
    pts = [(a, b) for a, b in zip(A, B) if a > 0 and b > 0][1:]
    grid = []
    p = FIT_P_LO
    while p <= FIT_P_HI:
        C = [a**p - b**p for a, b in pts]
        m = statistics.mean(C)
        grid.append((round(p, 2), statistics.pstdev(C) / abs(m) if m else BIG_CV))
        p += FIT_P_STEP
    if not grid:
        return None, BIG_CV, False
    i = min(range(len(grid)), key=lambda k: grid[k][1])
    return grid[i][0], grid[i][1], 0 < i < len(grid) - 1


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
    # [ED-MB-0050 / A6a] Both repairs applied here: rout genuinely disabled for the fit window, and
    # the volley arm using a scenario in which an exchange actually occurs.
    with _rout_disabled():
        pm, cvm, idm = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'melee', 'balanced',
                                                   diag=dm))
        pv, cvv, idv = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'ranged', VOLLEY_STANCE,
                                                   diag=dv, instructions=VOLLEY_INSTRUCTIONS))
    # Identifiability gates the verdict, not just the presentation: a fit whose optimum sits on a
    # grid endpoint carries no information about the exponent, so it can neither pass nor be quoted.
    ok = idm and idv and pm <= LIN_EXP_MAX and pv >= SQ_EXP_MIN
    def _fmt(name, p, cv, ident, bar):
        return (f"{name} p={p:.2f} {bar} cv={cv:.5f} "
                f"[{'identifiable' if ident else 'NOT IDENTIFIABLE — argmin on a grid endpoint'}]")
    return ('LAW EXPONENTS (linear/square)', ok,
            _fmt('melee', pm, cvm, idm, f"(≤{LIN_EXP_MAX} linear)") + '  ' +
            _fmt('volley', pv, cvv, idv, f"(≥{SQ_EXP_MIN} square)"),
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
