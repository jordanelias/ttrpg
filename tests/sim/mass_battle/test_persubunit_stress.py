"""Per-subunit rout / morale / discipline + troop-taxonomy stress regression.

Exercises the per-subunit machinery at its extremes (small/degenerate pools, all-routed,
broken sections, deep over-erosion, stat-spread mixes, the typed constructor) — the
multi-subunit behaviour the single-subunit byte-exact gauge (bat.py) does NOT cover.
Byte-exactness of the homogeneous gauge is asserted separately by bat.py (its DIGEST line).

Run:  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
      python3 tests/sim/mass_battle/test_persubunit_stress.py
Exit 0 = all pass.  [canonical: designs/provincial/mass_battle_v30.md §A.4, §A.12, §B.2]
"""
# Regression for the per-subunit work -- ED entries logged in the ledger.  [canonical: canon/editorial_ledger.jsonl]
import os, sys

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/sim')
# allow direct in-package run too:
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mass_battle.orchestration import (  # noqa: E402
    Subunit, Unit, subunit_combat_pool, morale_check_phase, rout_resolution,
    discipline_check_phase, reset_morale_between_battles, stats_for, TROOP_TYPE_STATS,
    SIDE_A_START_ROW, SIDE_B_START_ROW)

_FAILS = []


def _ok(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")
    if not cond:
        _FAILS.append(name)


def mk_su(tt='infantry', shape='Line', tier=1, col=8, fac='A', **kw):
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    adv = -1 if fac == 'A' else 1
    return Subunit(shape=shape, troop_type=tt, tier=tier, starting_position=(row, col),
                   advance_dir=adv, **kw)


def mk_unit(subs, command=4, discipline=5, morale=6, power=4, fac='A'):
    return Unit(name='T', faction=fac, power=power, command=command, discipline=discipline,
                discipline_start=discipline, morale=morale, morale_start=morale, subunits=subs, dr=1)


def test_of_type_presets():
    print("S1 — of_type reproduces §B.2 presets; unknown inherits; override wins; ranged via kw")
    for tt, exp in TROOP_TYPE_STATS.items():
        su = Subunit.of_type(tt, 'Line', 1, (SIDE_A_START_ROW, 8))
        _ok(f"S1 {tt}", (su.power, su.discipline, su.morale, su.morale_start)
            == (exp['power'], exp['discipline'], exp['morale'], exp['morale']))
    unk = Subunit.of_type('griffon_rider', 'Line', 1, (SIDE_A_START_ROW, 8))
    _ok("S1 unknown -> None (inherit)", (unk.power, unk.discipline, unk.morale) == (None, None, None))
    ov = Subunit.of_type('levy', 'Line', 1, (SIDE_A_START_ROW, 8), power=9, morale=7)
    _ok("S1 override beats preset", ov.power == 9 and ov.morale == 7 and ov.discipline == 1)
    rg = Subunit.of_type('archers', 'Line', 1, (SIDE_A_START_ROW, 8), unit_type='ranged')
    _ok("S1 ranged: stats from preset, role via kw", rg.unit_type == 'ranged' and rg.power == 3)


def test_all_routed_unit_routs():
    print("S2 — all sub-units routed -> unit routs; routed sub-unit pool 0")
    a, b = mk_su('heavy_infantry', col=8), mk_su('levy', col=9)
    u = mk_unit([a, b]); a.routed = b.routed = True; u.derive_rout()
    _ok("S2 unit routs", u.routed is True)
    _ok("S2 routed pool 0", subunit_combat_pool(u, a) == 0 and subunit_combat_pool(u, b) == 0)


def test_single_subunit_morale0_routs():
    print("S3 — single sub-unit eroded to Morale 0 routs")
    a = mk_su('levy', col=8, morale=1, morale_start=6); u = mk_unit([a], morale=1)
    a.erode_morale(1)
    rout_resolution(u, mk_unit([mk_su('levy', col=8, fac='B')], fac='B'), 0)
    _ok("S3 sub-unit routed", a.routed is True)
    _ok("S3 unit rout derived", u.routed is True)


def test_extreme_spread():
    print("S4 — Levy(D1) + Knights Templar(D6): pool differentiates; levy breaks, templar holds")
    lv = Subunit.of_type('levy', 'Line', 1, (SIDE_A_START_ROW, 8))
    kt = Subunit.of_type('knights_templar', 'Line', 1, (SIDE_A_START_ROW, 9))
    u = mk_unit([lv, kt], command=6)
    _ok("S4 templar pool > levy pool", subunit_combat_pool(u, kt) > subunit_combat_pool(u, lv))
    for _ in range(3):
        lv.erode_morale(1)
    _ok("S4 levy routs, templar holds", lv.eff_morale <= 0 and kt.eff_morale > 0)
    u.derive_rout()
    _ok("S4 unit holds (templar up, agg morale > 0)", u.routed is False)


def test_cohesion_guard():
    print("S5 — drained cells -> cohesion finite, no div-by-zero")
    a = mk_su('levy', col=8); u = mk_unit([a])
    a.cell_troops = {k: 0.0 for k in a.cell_troops}
    _ok("S5 cohesion finite", a.cohesion >= 0.0)
    _ok("S5 agg_morale finite", isinstance(u.agg_morale(), (int, float)))
    morale_check_phase(u, mk_unit([mk_su('levy', col=8, fac='B')], fac='B'), 0)
    _ok("S5 morale_check_phase no crash on 0-cohesion sub-unit", True)


def test_command_zero():
    print("S6 — Command 0 -> derive_rout routs all")
    a, b = mk_su('heavy_infantry', col=8), mk_su('cavalry', col=9)
    u = mk_unit([a, b], command=0); u.derive_rout()
    _ok("S6 unit routed", u.routed is True)
    _ok("S6 all sub-units routed", a.routed and b.routed)


def test_cascade_no_double_count():
    print("S7 — cascade_morale_hit: mixed own/inherit, no double-count")
    own = mk_su('heavy_infantry', col=8, morale=5, morale_start=6)
    inh = mk_su('levy', col=9)
    u = mk_unit([own, inh], morale=6); u.cascade_morale_hit(2)
    _ok("S7 unit.morale hit once 6->4", u.morale == 4)
    _ok("S7 own sub-unit 5->3", own.morale == 3)
    _ok("S7 inherit sub-unit sees 4", inh.eff_morale == 4)


def test_broken_scope():
    print("S8 — broken sub-unit (Disc 0) -> own pool 0, siblings fight (broken-scope fix)")
    a = mk_su('levy', col=8, discipline=0); b = mk_su('heavy_infantry', col=9, discipline=5)
    u = mk_unit([a, b])
    pa, pb = subunit_combat_pool(u, a), subunit_combat_pool(u, b)
    _ok("S8 broken pool 0 + flagged", pa == 0 and a.broken)
    _ok("S8 unit NOT broken on one section down", u.broken is False)
    _ok("S8 healthy sibling fights", pb > 0)
    a2 = mk_su('levy', col=8, discipline=0); b2 = mk_su('light_infantry', col=9, discipline=0)
    u2 = mk_unit([a2, b2]); subunit_combat_pool(u2, a2); subunit_combat_pool(u2, b2)
    _ok("S8 all broken -> unit.broken", u2.broken is True)
    s = mk_su('levy', col=8, discipline=0); us = mk_unit([s])
    _ok("S8 single-subunit disc0 -> unit.broken (byte-exact)", subunit_combat_pool(us, s) == 0 and us.broken)


def test_deep_erosion():
    print("S9 — over-erosion far past 0: deeply negative, no crash, rout idempotent")
    a = mk_su('levy', col=8, morale=2, morale_start=6); u = mk_unit([a])
    for _ in range(9):
        a.erode_morale(1)
    _ok("S9 deeply negative no crash", a.eff_morale <= -5)
    other = mk_unit([mk_su('levy', col=8, fac='B')], fac='B')
    rout_resolution(u, other, 0); rout_resolution(u, other, 1)
    _ok("S9 routed idempotent", a.routed and u.routed)


def test_restore_cap():
    print("S10 — restore_discipline capped at nominal start")
    a = mk_su('heavy_infantry', col=8, discipline=4, discipline_start=4); mk_unit([a])
    a.degrade_discipline()
    _ok("S10 degrade 4->3", a.eff_discipline == 3)
    for _ in range(3):
        a.restore_discipline()
    _ok("S10 restore capped at 4", a.eff_discipline == 4)


def test_fidelity_own_loss():
    print("S11 — Discipline degrades from the sub-unit's OWN loss, not the unit's (roll-input fidelity)")
    def su3(tt, col):
        return Subunit(shape='Line', troop_type=tt, tier=3, starting_position=(SIDE_A_START_ROW, col),
                       advance_dir=-1, discipline=5, discipline_start=5)
    s0 = su3('heavy_infantry', 8); s1 = su3('levy', 9)
    a = Unit(name='A', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[s0, s1], dr=1)
    bsu = Subunit(shape='Line', troop_type='heavy_infantry', tier=3,
                  starting_position=(SIDE_B_START_ROW, 8), advance_dir=1, discipline=5, discipline_start=5)
    b = Unit(name='B', faction='B', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[bsu], dr=1)
    for k in s0.cell_troops:                 # gut s0's own troops; s1 stays fresh
        s0.cell_troops[k] *= 0.5
    a.hp = s0.cur_troops + s1.cur_troops      # unit-level loss large -> OLD code would degrade BOTH
    discipline_check_phase(a, b, 0)
    _ok("S11 gutted sub-unit degrades from own loss", s0.eff_discipline == 4)
    _ok("S11 fresh reserve NOT degraded from sibling loss", s1.eff_discipline == 5)


def test_of_type_wiring():
    print("S12 — of_type construction (as make_mixed_unit now builds) draws B.2 presets (taxonomy wiring)")
    kt = Subunit.of_type('knights_templar', 'Line', 1, (SIDE_A_START_ROW, 8))
    _ok("S12 canonical type draws preset", (kt.power, kt.discipline, kt.morale) == (5, 6, 6))
    ov = Subunit.of_type('knights_templar', 'Line', 1, (SIDE_A_START_ROW, 8), discipline=3)
    _ok("S12 caller override beats preset", ov.discipline == 3 and ov.power == 5)
    inf = Subunit.of_type('infantry', 'Line', 1, (SIDE_A_START_ROW, 8))
    _ok("S12 non-canonical inherits", (inf.power, inf.discipline, inf.morale) == (None, None, None))


def test_between_battle_reset():
    print("S13 — reset_morale_between_battles: Morale resets, Discipline persists, rout clears (campaign boundary)")
    own = mk_su('heavy_infantry', col=8, morale=6, morale_start=6, discipline=5, discipline_start=5)
    inh = mk_su('levy', col=9)                                    # inherits unit morale/discipline
    u = mk_unit([own, inh])
    own.erode_morale(9); own.degrade_discipline(); own.degrade_discipline()   # own morale -3, disc 5->3
    u.morale = 0; u.derive_rout()                                 # whole unit routs (agg morale <= 0)
    pre_disc_own = own.eff_discipline
    assert u.routed and own.routed
    reset_morale_between_battles(u)
    _ok("S13 unit morale reset to start", u.morale == u.morale_start)
    _ok("S13 own-subunit morale reset to start", own.eff_morale == own.eff_morale_start)
    _ok("S13 inherited subunit morale follows unit", inh.eff_morale == u.morale_start)
    _ok("S13 rout/broken cleared (unit+subunits)", not (u.routed or u.broken or own.routed or inh.routed))
    _ok("S13 Discipline persists (not reset)", own.eff_discipline == pre_disc_own and pre_disc_own == 3)


def test_drift_per_subunit_discipline():
    print("S14 — check_drift uses per-subunit Discipline: low-disc subunit drifts to Line, high-disc keeps shape")
    lo = mk_su('heavy_infantry', shape='Arrowhead', col=8, discipline=3, discipline_start=3)   # below Arrowhead min
    hi = mk_su('heavy_infantry', shape='Arrowhead', col=9, discipline=5, discipline_start=5)   # at/above min
    u = mk_unit([lo, hi])
    u.check_drift()
    _ok("S14 low-disc subunit drifted to Line (own Discipline below shape min)", lo.shape == "Line")
    _ok("S14 high-disc subunit kept its shape", hi.shape == "Arrowhead")


def test_advance_per_subunit_discipline():
    print("S15 — advance_cells uses per-subunit Discipline: low-disc subunit advances less than high-disc sibling")
    def mk(disc, col):
        return Subunit(shape='Line', troop_type='heavy_infantry', tier=2,
                       starting_position=(SIDE_A_START_ROW, col), advance_dir=-1,
                       discipline=disc, discipline_start=disc)
    tgt = (SIDE_A_START_ROW - 8, 8)
    hi = mk(5, 8); lo = mk(2, 9)
    for s in (hi, lo):                                    # the run_battle pattern: each subunit on its OWN Discipline
        s.advance_cells(s.eff_discipline, tgt, enemy_cells=None)
    hi_adv = max([abs(v) for v in hi.cell_offsets.values()] + [0])
    lo_adv = max([abs(v) for v in lo.cell_offsets.values()] + [0])
    _ok("S15 high-disc subunit advanced", hi_adv > 0)
    _ok("S15 low-disc subunit advanced less than high-disc", lo_adv < hi_adv)
    hi2 = mk(5, 8); lo2 = mk(2, 9)
    for s in (hi2, lo2):                                  # contrast: a SHARED (old, unit-level) Discipline
        s.advance_cells(5, tgt, enemy_cells=None)
    same = (max([abs(v) for v in hi2.cell_offsets.values()] + [0])
            == max([abs(v) for v in lo2.cell_offsets.values()] + [0]))
    _ok("S15 under shared (old) Discipline both advance equally — confirms the fix changes multi-subunit behavior", same)


def main():
    for fn in (test_of_type_presets, test_all_routed_unit_routs, test_single_subunit_morale0_routs,
               test_extreme_spread, test_cohesion_guard, test_command_zero, test_cascade_no_double_count,
               test_broken_scope, test_deep_erosion, test_restore_cap,
               test_fidelity_own_loss, test_of_type_wiring, test_between_battle_reset,
               test_drift_per_subunit_discipline, test_advance_per_subunit_discipline):
        fn()
    print(f"\n=== {('ALL PASS' if not _FAILS else str(len(_FAILS)) + ' FAIL')} ===")
    if _FAILS:
        print("FAILURES:", _FAILS)
    return 1 if _FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
