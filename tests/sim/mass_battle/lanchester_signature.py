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

# anchor columns for Line at each tier [canonical: mass_battle_v30.md §deployment — gauge ANCHOR_MAP]
_LINE_ANCHOR = {SMALL_TIER: 10, MIRROR_TIER: 9, BIG_TIER: 8}


def _mk(shape, tier, faction, unit_type='melee', stance='balanced'):
    ad = -1 if faction == 'A' else 1
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type='infantry', tier=tier,
                 starting_position=(sr, _LINE_ANCHOR.get(tier, 10)),
                 advance_dir=ad, unit_type=unit_type)
    # historical infantry baseline [canonical: tests/sim/gauge_mb.py make_unit defaults]
    p, cmd, disc, mor = 4, 4, 5, 6
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


def run():
    assert LANCHESTER_ENABLED, "signatures require LANCHESTER_ENABLED=1"
    results = [check_linear(), check_square(), check_no_annihilation()]
    print("=== P-L Lanchester signature tests (PER_CELL=%s) ===" % os.environ.get('PER_CELL'))
    allok = True
    for name, ok, detail in results:
        allok = allok and ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name:26} {detail}")
    print(f"  => {'ALL PASS' if allok else 'FAILURES PRESENT'} ({sum(1 for _,o,_ in results if o)}/{len(results)})")
    return allok


if __name__ == '__main__':
    import sys
    sys.exit(0 if run() else 1)
