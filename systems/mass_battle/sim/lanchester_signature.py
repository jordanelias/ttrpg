"""systems.mass_battle.sim.lanchester_signature — P-L Lanchester signature regression tests.

Validates the two attrition laws the P-L substrate introduces, per the design spec
(mb_lanchester_design.md, section four):

  (1) LINEAR signature (melee): casualties ~ ENEMY strength IN CONTACT, frontage-capped,
      so a larger equal-quality force wins by a margin that scales with the size difference
      (the classic linear-law result — numerical superiority is a *linear* edge).
  (2) SQUARE signature (volley): aimed fire lifts the frontage cap, so the casualty-exchange
      ratio is SUPER-linear in the size ratio (N-squared concentration) — distinct from melee.
  (3) NO-ANNIHILATION invariant: battles still terminate by ROUT (the morale/rout system
      decides the end), not by attrition to zero. Lanchester FEEDS morale; it does not replace it.

Requires LANCHESTER_ENABLED on (the engine default). Run from the repo root (no PYTHONPATH needed --
`-m` puts cwd on sys.path automatically; verified 2026-09-27, ED-MB-0070 -- this line previously read
`PYTHONPATH=tests/sim`, stale residue from before the 2026-08-24 port):
    python3 -m systems.mass_battle.sim.lanchester_signature

All numeric thresholds below are class-B TOLERANCES derived from validated P-L behaviour,
NOT canonical magnitudes (the one exception, LINEAR_BIG_WIN_BAND, is the cited DLEDB plateau); the
SIGNATURES are the spec section-four validation plan.
"""
import contextlib
import os, statistics

# Lanchester must be ON for the signatures to hold (default ON; assert explicitly).
import dataclasses  # noqa: E402
from systems.mass_battle.sim import variant  # noqa: E402
# [B17.12] the engine is built from a config: this script's own defaults (the per-cell layer off), over any variable its caller
# exported, over the shipped config. The engine reads no process variable.
variant.install(variant.cfg_from_environ(os.environ, base=dataclasses.replace(variant.DEFAULT, PER_CELL=False)))

from modules.mass_battle.config import BLOCK_SIZE, TROOPS_PER_TIER   # [ED-MB-0050 / A6a] the annihilation threshold
from systems.mass_battle.sim.engine import (Unit, Army, run_battle,
                                SIDE_A_START_ROW, SIDE_B_START_ROW, LANCHESTER_ENABLED)
import modules.mass_battle.core.state as _state   # [ED-MB-0050 / A6a] patched by _rout_disabled below
import modules.mass_battle.orchestration as _orch  # [B19.09] observed (not altered) by _melee_pair_counter below
from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import rngsource  # noqa: E402

# --- signature thresholds (class-B tolerances; signatures per spec §4) ---
# [ED-MB-0045 superseding row, item (1)] ONE band for the big-force win quantity. It replaces the
# one-sided floor `LINEAR_MIN_BIG_WIN = 65`, which passed every win rate from 65 to 100, including the
# 100.0% this check reads with friction off (MB_FRICTION=0). The pair fought is BIG_TIER vs SMALL_TIER =
# 800 vs 200 troops, i.e. 4:1 (config.TROOPS_PER_TIER), so the band is the DLEDB "3:1+" plateau
# MB_FRICTION_SIGMA is calibrated against (config.py): 74-83%, "plateaus, never certain". Above the top
# edge is the certainty friction exists to remove; below the bottom edge is a collapse toward a coin flip.
# Both fail; the floor could fail only the second.
LINEAR_BIG_WIN_BAND = (74, 83)   # [canonical: audit/2026-07-22-mass-battle-stress-test/dg6_friction_resolution.md §3 "Historical decisiveness bands" — Dupuy DLEDB attacker win-rate, "74–83% at 3:1+"; the force-ratio calibration table is §4]
LINEAR_MIN_CASDIFF  = 20       # [canonical: mb_lanchester_design.md §4(2) — linear sig: casualty diff (small−big); class-B tolerance]
SQUARE_MIN_RATIO    = 4        # [canonical: mb_lanchester_design.md §4(3) — square sig: cas-exchange ratio ≥ (size ratio)² at 2:1; class-B tolerance]
NOANNIH_MAX_CAS     = 60       # [canonical: mb_lanchester_design.md §4(4) — no-annihilation: winner-side casualty% ceiling; class-B tolerance]
BIG_TIER            = 4        # [canonical: mb_lanchester_design.md §4(2) — size pair; TROOPS_PER_TIER makes Tier 4 = 800 vs Tier 2 = 200, i.e. 4:1 in troops (frontage 7 v 5 cells), NOT 2:1; check_square reads the same pair; class-B]
MIRROR_TIER         = 3        # [canonical: mb_lanchester_design.md §4(4) — equal-size mirror baseline; class-B]
SMALL_TIER          = 2        # exempt literal (2): the smaller force of the pair
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
    su = Unit(shape=shape, troop_type='infantry', tier=tier,
                 starting_position=(sr, _LINE_ANCHOR.get(tier, 10)),
                 advance_dir=ad, unit_type=unit_type, instructions=tuple(instructions))
    # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md — "The v9 targets above use uniform
    #  Power=4, Command=4, Discipline=5, Morale=6 to isolate formation/unit_type effects"]
    # Verified by hand against that file 2026-07-29 (ED-MB-0049, A5a citation critic): the source
    # says exactly this, and it is also `gauge_mb.make_unit`'s default signature, so the harness and
    # the gauge share one baseline rather than two coincidentally-equal ones.
    p, cmd, disc, mor = 4, 4, 5, 6  # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §v9 targets — uniform P4/C4/D5/M6]
    return Army(name=faction, faction=faction, power=p, command=cmd,
                discipline=disc, discipline_start=disc, morale=mor, morale_start=mor,
                units=[su], dr=1, stance=stance, speed='Standard')


def _sweep(big_tier, small_tier, unit_type, stance='balanced', instructions=()):
    """A = big force, B = small force, equal quality. Returns aggregate stats."""
    aw = ca = cb = ahp = bhp = 0
    cas_a, cas_b, hp_a, hp_b = [], [], [], []
    for s in range(N):
        with rngsource.using(draw.seeded(draw.H2("lanchester_signature", s + SEED_BASE))):
            ua = _mk('Line', big_tier, 'A', unit_type, stance, instructions)
            ub = _mk('Line', small_tier, 'B', unit_type, stance, instructions)
            a0, b0 = ua.hp_max, ub.hp_max
            r = run_battle(ua, ub)
            aw += (r['winner'] == 'A')
            cas_a.append(100 * (a0 - ua.hp) / a0)
            cas_b.append(100 * (b0 - ub.hp) / b0)
            hp_a.append(100 * ua.hp / a0)
            hp_b.append(100 * ub.hp / b0)
    return dict(big_win=100 * aw / N,
                cas_big=statistics.mean(cas_a), cas_small=statistics.mean(cas_b),
                hp_big=statistics.mean(hp_a), hp_small=statistics.mean(hp_b))


def check_linear():
    """Melee 4:1 in troops (800 v 200) → big force wins decisively but not certainly (frontage/durability
    linear edge, banded by friction): big_win inside LINEAR_BIG_WIN_BAND, casualty difference above its floor."""
    r = _sweep(BIG_TIER, SMALL_TIER, 'melee')
    casdiff = r['cas_small'] - r['cas_big']
    lo, hi = LINEAR_BIG_WIN_BAND
    ok = lo <= r['big_win'] <= hi and casdiff >= LINEAR_MIN_CASDIFF
    return ('LINEAR (melee 4:1)', ok,
            f"big_win={r['big_win']:.1f}% (in [{lo}, {hi}]) "
            f"cas_diff={casdiff:+.1f} (≥{LINEAR_MIN_CASDIFF})")


def check_square():
    """Volley 4:1 in troops (800 v 200) → cas-exchange ratio super-linear in size (square concentration).

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
        return ('SQUARE (volley 4:1)', False,
                "PRECONDITION FAILED — 0.0% casualties on BOTH sides: no exchange occurred, so there "
                "is no ratio to test (this is what `inf` used to hide)")
    ratio = r['cas_small'] / r['cas_big'] if r['cas_big'] > 0 else float('inf')
    ok = ratio >= SQUARE_MIN_RATIO
    return ('SQUARE (volley 4:1)', ok,
            f"cas_exchange small/big={ratio:.1f} (≥{SQUARE_MIN_RATIO}; linear law would give "
            f"~{TROOPS_PER_TIER[BIG_TIER]//TROOPS_PER_TIER[SMALL_TIER]}) [cas big={r['cas_big']:.2f}% small={r['cas_small']:.2f}%]")


def check_no_annihilation():
    """Mirror → battle ends by rout, not annihilation (loser hp > 0, casualties bounded)."""
    r = _sweep(MIRROR_TIER, MIRROR_TIER, 'melee')
    worst_cas = max(r['cas_big'], r['cas_small'])
    loser_hp = min(r['hp_big'], r['hp_small'])
    ok = worst_cas <= NOANNIH_MAX_CAS and loser_hp > 0
    return ('NO-ANNIHILATION (mirror)', ok,
            f"max_cas={worst_cas:.1f}% (≤{NOANNIH_MAX_CAS}) loser_hp={loser_hp:.1f}% (>0)")


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
#       fired at hp<=25 — but `Army.recalc_size` sets `size = floor(hp/BLOCK_SIZE)` and routs the unit
#       outright at `size == 0`, i.e. at hp < 100. The engine therefore ALWAYS annihilation-routed
#       ~4x before the trajectory's own floor could trigger. Measured with stochastic rout already
#       disabled: side B routed at ticks 36/35/36 with hp 97.3/97.1/98.9, size 0, agg_morale 1e9,
#       troop_total 400 (well above UNIT_ROUT_FLOOR=80) — annihilation, not morale, not the
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
# trajectories routed, fit window 30 ticks of 160. `MB_STOCHASTIC_ROUT` is the flag that owns that
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
#
# [B19.09, `04_MB_cr12_linear_law` step 1] ...for an 18-tick rout-on battle only. Over the no-rout
# TRAJECTORY the band broke: the kiters spend their MB_VOLLEYS_START stock (one volley per firing tick)
# by about tick 12, and an empty kiter closes to melee by design (`Unit._kite_goal`'s `eff_volleys > 0`
# test, F7 / ED-MB-0067). Measured seeds 0-1 at PER_CELL=0, shipped stock: first melee pair at tick 14,
# 21 and 69 melee ticks; stocked: 0 melee ticks, the band held at distance 5 to the floor. The cause is the
# empty quiver, not the field's width, so a wider field or a `hold` screen would not hold it (the screen
# would itself be the melee pair). The trajectory therefore stocks each shooter for its whole window
# (`_trajectory`, TRAJ_TICKS volleys: it fires at most once a tick), as the morale pin and `_rout_disabled`
# remove the other mechanisms that end the pure-attrition regime early; and `_melee_pair_counter` makes
# the precondition observed, not assumed: one melee pair in the volley trajectory and the row is INVALID.
VOLLEY_STANCE = 'balanced'
VOLLEY_INSTRUCTIONS = ('kite',)


@contextlib.contextmanager
def _rout_disabled():
    """Turn the casualty-fraction break-point OFF for the enclosed block, then restore.

    Patches the name where it is READ (`core.state`), because that module star-imports the constant
    from config and consults its own module global at call time. Restores unconditionally, so a
    raising body cannot leak a disabled rout into the checks that need it on.
    """
    prev = _state.MB_STOCHASTIC_ROUT
    _state.MB_STOCHASTIC_ROUT = False
    try:
        yield
    finally:
        _state.MB_STOCHASTIC_ROUT = prev


@contextlib.contextmanager
def _melee_pair_counter(diag):
    """[B19.09] Count the melee pairs the engine resolves inside the block, into `diag`.

    Wraps the two resolvers on `orchestration`, where `run_battle` looks them up AT CALL TIME (its own
    docstring: a patch there is seen), and counts the `pairs` each tick hands them: the contacts the
    tick resolves as melee. Pure observation: the wrapped call's arguments and result pass through
    untouched. Only the outermost call counts, so a cascading resolver that calls the plain one is one
    tick, not two. Counting the resolver's INPUT, not a trace event inside it, keeps the count honest
    when the melee pair's body is rewritten (B19.10-B19.12 move and replace it; the resolvers stay).
    Restores unconditionally.
    """
    names = ('resolve_engagements_cascading', 'resolve_engagements')
    saved = {n: getattr(_orch, n) for n in names}
    depth = [0]

    def _wrap(fn):
        def counted(unit_a, unit_b, pairs, *args, **kwargs):
            if depth[0] == 0 and pairs:
                diag['melee_ticks'] += 1
                diag['melee_pairs'] += len(pairs)
            depth[0] += 1
            try:
                return fn(unit_a, unit_b, pairs, *args, **kwargs)
            finally:
                depth[0] -= 1
        return counted
    for n in names:
        setattr(_orch, n, _wrap(saved[n]))
    try:
        yield diag
    finally:
        for n in names:
            setattr(_orch, n, saved[n])


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
        with rngsource.using(draw.seeded(draw.H2("lanchester_signature", s + SEED_BASE))):
            # [ED-MB-0049 / plan-v2 A5a] The morale pin, swept onto its single owner.
            #
            # This was `ua.morale = ua.morale_start = NO_ROUT_MORALE`, a BARE absolute write — the exact
            # silent-no-op class that confounded the retracted MB_CELL_MORALE measurement (ED-MB-0042):
            # `eff_morale` reads the cells once seeded and never falls back to the scalar, so under the
            # flag this pin would set nothing, bodies would rout mid-signature, and the Lanchester
            # exponent would be fitted on TRUNCATED battles. `Army.set_morale` is the owner; unseeded
            # (the shipped default) it reduces exactly to `unit.morale = value`, so this is
            # behaviour-identical at MB_CELL_MORALE=0 and correct at =1.
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
            # [B19.09] A shooter's stock for the whole window (see the note above VOLLEY_STANCE): its
            # single subunit inherits the Army's pool, and it fires at most once a tick. Ranged only, so
            # the melee arm is untouched.
            if unit_type == 'ranged':
                ua.volleys = ub.volleys = float(TRAJ_TICKS)
            # [ED-MB-0050 / A6a] Floor against BLOCK_SIZE, the engine's annihilation threshold, not
            # against a fraction of it — see TRAJ_FLOOR_BLOCKS.
            hp_floor = TRAJ_FLOOR_BLOCKS * BLOCK_SIZE
            tr = []
            routed_here = False
            for _ in range(TRAJ_TICKS):
                with _melee_pair_counter(diag):
                    run_battle(ua, ub, max_ticks=1)
                tr.append((ua.hp, ub.hp))
                # [ED-MB-0049 / A5a falsifier] The pin's WHOLE PURPOSE is "no rout, pure attrition".
                # Record whether it held, per trajectory, instead of assuming it. `checked` is the
                # non-vacuity counter (§0.1 #2): a loop that only asserts conditionally must assert
                # that it asserted, or an empty loop reads as a pass.
                diag['checked'] += 1
                # [ED-MB-0050 / A6a] Order matters, and getting it wrong is how "40/40 routed" stayed
                # ambiguous. Reaching the attrition floor is a CLEAN stop — the trajectory has run out
                # of the regime it was measuring. `Army.recalc_size` also flips `routed` at that same
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
    return {'checked': 0, 'routed_trajectories': 0, 'ticks': [], 'fit_window': 0,
            'melee_ticks': 0, 'melee_pairs': 0}


def _best_exponent(A, B):
    """Scan p for the exponent that best conserves A^p − c·B^p, c free; return (p, lof, identifiable, c).

    [B19.09, `04_MB_cr12_linear_law` step 1] The fit was `A^p − B^p`, equal coefficients, and so could
    not tell a linear law with a rate edge from a super-linear one: under an EXACT linear law in which
    the bigger body kills faster (more columns in contact), A falls slower than B, and only p > 1 makes
    the equal-coefficient difference constant (the design's synthetic, 7:5 columns: 1.45 / 1.35 / 1.30
    as B falls to 300 / 200 / 100). With c free the rate ratio lives in c and the law's SHAPE in p: for
    each p, c is the least-squares slope of A^p on B^p, and `lof` = 1 − r² of that line is the share of
    A^p's variation the conserved line does not explain. Scale-free (no division by the conserved
    quantity, which a free c can drive to zero), and exactly 0 for a law of that exponent at any c.
    Chosen over normalising each side's loss rate by its engaged columns because it needs no reading of
    the engine's contact geometry (whose definition B19.12 rewrites as `engaged_files`) and because it
    absorbs every rate edge, not only frontage: quality, arc and support move c, never p.
    A line of non-positive slope (one side gaining as the other loses) conserves nothing: BIG_CV.

    [ED-MB-0050 / A6a] `identifiable` is the third return value and it is the point of this repair.
    An argmin that lands on a grid ENDPOINT is not an estimate — it is the statement "the objective
    was still improving when I stopped looking". Reporting one as a number is how `melee p=2.50`
    (the old FIT_P_HI of 2.51) entered the record as an engine property, survived two audits, and
    got quoted in a handoff. The scan now reports whether the optimum is interior, and
    `check_law_exponents` refuses to pass on a non-identifiable fit however favourable its value.
    """
    pts = [(a, b) for a, b in zip(A, B) if a > 0 and b > 0][1:]
    grid = []
    p = FIT_P_LO
    while p <= FIT_P_HI and len(pts) > 2:
        X = [b**p for _, b in pts]
        Y = [a**p for a, _ in pts]
        mx, my = statistics.fmean(X), statistics.fmean(Y)
        sxx = sum((x - mx) ** 2 for x in X)
        syy = sum((y - my) ** 2 for y in Y)
        sxy = sum((x - mx) * (y - my) for x, y in zip(X, Y))
        if sxx > 0 and syy > 0 and sxy > 0:
            grid.append((round(p, 2), max(0.0, 1 - sxy * sxy / (sxx * syy)), sxy / sxx))
        else:
            grid.append((round(p, 2), BIG_CV, None))
        p += FIT_P_STEP
    if not grid:
        return None, BIG_CV, False, None
    i = min(range(len(grid)), key=lambda k: grid[k][1])
    return grid[i][0], grid[i][1], 0 < i < len(grid) - 1 and grid[i][1] < BIG_CV, grid[i][2]


def check_law_exponents():
    """Rigorous: melee must conserve the LINEAR difference (p≤1.4), volley the SQUARE
    difference (p≥1.6). Requires the Command-only base (COMMAND_SIGMA on); the Size-based
    pool contaminates melee to p≈1.7 and FAILS this guard by design.

    [ED-MB-0049 / A5a] Returns a fourth element: the per-arm PRECONDITION diagnostic. An exponent
    fitted on trajectories that ROUTED is fitted on truncated data and is not an estimate of
    anything — so the precondition is reported next to the number, never assumed behind it (G4:
    verify the instrument before quoting its number).

    [B19.09] Two rows, not one: the melee and the volley exponent are separate verdicts (the melee bar
    is read after B19.12; the volley row has its own validity). The volley row reads INVALID, never
    PASS or FAIL, when its trajectory resolved a melee pair, or when the counter saw no melee pair in
    the melee arm either (a counter that cannot see presence cannot report absence).
    """
    dm, dv = _new_diag(), _new_diag()
    # [ED-MB-0050 / A6a] Both repairs applied here: rout genuinely disabled for the fit window, and
    # the volley arm using a scenario in which an exchange actually occurs.
    with _rout_disabled():
        pm, lm, idm, cm = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'melee', 'balanced',
                                                      diag=dm))
        pv, lv, idv, cv = _best_exponent(*_trajectory(BIG_TIER, MIRROR_TIER, 'ranged', VOLLEY_STANCE,
                                                      diag=dv, instructions=VOLLEY_INSTRUCTIONS))
    # Identifiability gates the verdict, not just the presentation: a fit whose optimum sits on a
    # grid endpoint carries no information about the exponent, so it can neither pass nor be quoted.
    melee_row = ('LAW EXPONENT (melee)', idm and pm <= LIN_EXP_MAX,
                 _fmt_fit(pm, lm, idm, cm, f"(≤{LIN_EXP_MAX} linear)"), {'melee': dm})
    if dv['melee_ticks'] or not dm['melee_ticks']:
        why = (f"{dv['melee_pairs']} melee pairs on {dv['melee_ticks']} ticks of the volley trajectory"
               if dv['melee_ticks'] else "the counter saw no melee pair in the melee arm either")
        volley_row = ('LAW EXPONENT (volley)', 'INVALID',
                      f"INVALID — {why}; the fit is not a volley law and is not quoted", {'volley': dv})
    else:
        volley_row = ('LAW EXPONENT (volley)', idv and pv >= SQ_EXP_MIN,
                      _fmt_fit(pv, lv, idv, cv, f"(≥{SQ_EXP_MIN} square)"), {'volley': dv})
    return melee_row, volley_row


def _fmt_fit(p, lof, ident, c, bar):
    if p is None:
        return "no fit (fewer than three usable points)"
    return (f"p={p:.2f} {bar} c={c if c is None else round(c, 3)} lof={lof:.2e} "
            f"[{'identifiable' if ident else 'NOT IDENTIFIABLE — argmin on a grid endpoint'}]")


def check_frontage_control():
    """[B19.09] The fit's own control: an EXACT linear law with the trajectory pair's frontage edge must
    read "linear".

    Built from the melee arm's own pair (`_mk`, BIG_TIER v MIRROR_TIER): each side's starting hp and its
    columns. Each step A loses one hp per column of B and B one per column of A, so A − (w_B/w_A)·B is
    conserved exactly: the linear law, with the bigger front killing faster. Read through `_best_exponent`
    on every window from the start to each block boundary down to the trajectory floor (BLOCK_SIZE,
    TRAJ_FLOOR_BLOCKS), since the engine's fit window ends wherever its first seed hits the floor. The
    row passes only if every window is identifiable and at or below LIN_EXP_MAX. The step size is the
    synthetic's time unit, not a game magnitude: the law's shape does not depend on it.
    """
    ua = _mk('Line', BIG_TIER, 'A')
    ub = _mk('Line', MIRROR_TIER, 'B')
    wa = len({c for sub in ua.units for (_, c) in sub.cells()})
    wb = len({c for sub in ub.units for (_, c) in sub.cells()})
    a, b = float(ua.hp_max), float(ub.hp_max)
    floor = TRAJ_FLOOR_BLOCKS * BLOCK_SIZE
    A, B = [a], [b]
    while b - wa > floor - 1e-9:
        a, b = a - wb, b - wa
        A.append(a)
        B.append(b)
    readings, ok = [], True
    end = B[0] - BLOCK_SIZE
    while end >= floor:
        reached = [i for i, x in enumerate(B) if x <= end + 1e-9]
        n = reached[0] + 1 if reached else len(B)   # the last window ends at the last step above the floor
        p, _lof, ident, _c = _best_exponent(A[:n], B[:n])
        ok = ok and ident and p is not None and p <= LIN_EXP_MAX
        readings.append(f"→{B[n - 1]:.0f} p={p:.2f}{'' if ident else ' (NOT IDENTIFIABLE)'}")
        end -= BLOCK_SIZE
    ok = ok and bool(readings)
    return ('FRONTAGE CONTROL (synthetic)', ok,
            f"exact linear law, {wa}:{wb} columns, B {B[0]:.0f} " + ', '.join(readings)
            + f" (≤{LIN_EXP_MAX}) reads {'linear' if ok else 'NOT linear'}")


def run():
    assert LANCHESTER_ENABLED, "signatures require LANCHESTER_ENABLED=1"
    results = [check_linear(), check_square(), check_no_annihilation(), *check_law_exponents(),
               check_frontage_control()]
    from modules.mass_battle import config as _mb_cfg
    print("=== P-L Lanchester signature tests (PER_CELL=%s) ===" % _mb_cfg.PER_CELL)
    allok = True
    for row in results:
        name, ok, detail = row[0], row[1], row[2]
        # [B19.09] A row's verdict is PASS, FAIL or a named status (INVALID); only PASS passes.
        status = ok if isinstance(ok, str) else ('PASS' if ok else 'FAIL')
        allok = allok and status == 'PASS'
        print(f"  [{status}] {name:28} {detail}")
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
                  f"{min(d['ticks'])}/{statistics.median(d['ticks']):.0f}/{max(d['ticks'])}); "
                  f"melee pairs {d['melee_pairs']} on {d['melee_ticks']} ticks")
    npass = sum(1 for r in results if r[1] is True)
    print(f"  => {'ALL PASS' if allok else 'FAILURES PRESENT'} ({npass}/{len(results)})")
    return allok


if __name__ == '__main__':
    import sys
    sys.exit(0 if run() else 1)
