"""d.1 -- faction state sets a field unit's starting morale, on the SEASON path (plan position `20-iv`).

WHY THIS EXISTS. Jordan ruled (`ED-MB-0067`, second row) that faction state sets the morale baseline
when a battle is built from the strategic layer. `ED-MB-0068` built it on `game_state.Faction.Sta`
through `massbattle._faction_to_unit`; plan position `29b` deleted both, and this file
was red at collection until `20-iv` re-pinned it here, against `massbattle.resolve_field` -- the one
entry point left. Its first nine tests constructed a `Faction` and are in git at `5c5d8ec6`.


THE SOURCE NOW (`massbattle._morale_start`'s docstring has the argument): each side's weight-mean
stance toward its members' own faction, the row `_eff_march` writes a lost field's "decrease in
morale" onto (M4, `ED-IN-0279` clause (b)). The seam reads it (`seam/wrappers/mass_battle.py::
_side_stance`), `resolve_field` maps it onto canon's Morale ladder: base 5, one point per stance
unit, clamped to 1..7, half-up.

THE RE-PIN, value by value (old -> new). Each old value was a `Faction.Sta`; each new one the stance
that lands on the same morale under the new mapping, so the LADDER pins carry over and only the
input's name changed: Sta 2.0/6.0 -> 2/6 became stance -3.0/+1.0 -> 2/6; the clamp pair Sta 0.0 -> 1
and 7.0 -> 7 became stance -25.0 -> 1 and +25.0 -> 7 (the stance row type's own extremes, valence 5 x
weight 5); the half-boundaries Sta 3.5/4.5/5.5/2.5 -> 4/5/6/3 became stance -1.5/-0.5/+0.5/-2.5 ->
4/5/6/3; the garrison stub's flat 5 became the zero-stance control's flat 5 (`_GarrisonStub` had no
reader after `29b` and is deleted); the Sta sweep 0..7 (71 values) became a stance sweep -25..+25
(501 values). NEW: the end-to-end test at the bottom, which is the only one that shows the source is
SEASON state -- a real lost field moves the next field's morale-start.

SUBJECT, under CLAUDE.md §0.1 pt 5's load-bearing predicate: game math on the executable model (a
side's morale decides when its unit routs) and the implementation of a Jordan ruling.
"""
from __future__ import annotations

import random
from dataclasses import replace

import pytest

from modules.mass_battle import massbattle as MB

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.seam.wrappers import mass_battle as provider
from engine.season.seam.wrappers.mass_battle import field_input
from engine.season.state.carriers import Act


def _record(w, side_a, side_b, *, territory=None, fort_level=0.0, stance_a=0.0, stance_b=0.0,
            walls_dr=None, origin=None):
    """The record `resolve_field` takes since plan position `31c`: the host builder's (`field_input`) for
    the two sides -- the weight projection is the host's -- with the fight's facts set as this test
    states them. The keyword defaults are `resolve_field`'s own before the split (`origin` `None`, no
    crossing, since MB-05r replaced the always-`False` `river_crossing`)."""
    return replace(field_input(w, side_a, side_b, "r_valoria"), territory=territory, fort_level=fort_level,
                   stances=(stance_a, stance_b), walls_dr=walls_dr, origin=origin)


def _captured_units(monkeypatch, **kwargs):
    """Run `resolve_field` with `_run_and_grade` intercepted, returning the two Units it built --
    `test_mass_battle_resolve_field.py`'s technique, so the morale is read off the constructed
    Unit rather than inferred from a battle outcome at a scale that routs on contact."""
    captured = {}

    def fake(unit_a, unit_b, terrain, rng, walls_dr=None):
        captured["a"], captured["b"] = unit_a, unit_b
        return {"attacker_wins": True, "degree": "Success",
                "attacker_size_pct": 1.0, "defender_size_pct": 0.0}

    monkeypatch.setattr(MB, "_run_and_grade", fake)
    w = build_realm(0)
    MB.resolve_field(_record(w, ["p_npc_033"], ["p_npc_004"], **kwargs))
    return captured["a"], captured["b"]


def test_two_sides_differing_only_in_stance_get_different_morale_starts(monkeypatch):
    """(a) stance -3.0 vs +1.0 -> `morale_start` 2 and 6, and morale == morale_start."""
    u_low, u_high = _captured_units(monkeypatch, stance_a=-3.0, stance_b=1.0)
    assert u_low.morale_start == 2, f"stance -3.0 should give morale_start 2, got {u_low.morale_start}"
    assert u_low.morale == u_low.morale_start, "morale and morale_start must agree at battle start"
    assert u_high.morale_start == 6, f"stance +1.0 should give morale_start 6, got {u_high.morale_start}"
    assert u_high.morale == u_high.morale_start, "morale and morale_start must agree at battle start"
    # (F9) what ROUT reads downstream is the subunit's `eff_morale`, which falls through to the
    # Unit's scalar while the subunit sets none -- a refactor giving the subunit its own morale
    # preset would silently stop reading the derived value while the two asserts above kept passing.
    assert u_low.subunits[0].eff_morale == 2, "subunit eff_morale did not inherit morale_start"
    assert u_low.subunits[0].eff_morale_start == 2, "subunit eff_morale_start did not inherit"


@pytest.mark.parametrize('stance, expected', [(-25.0, 1), (25.0, 7)])
def test_boundary_stances_clamp_to_the_morale_ladder(stance, expected):
    """(b) The stance row type's own extremes (`(referent, valence -5..+5, weight 0..5)`, so one
    row spans -25..+25) land on canon's Morale ladder ends: never 0 (rout fires at morale <= 0, so
    a side cannot start routed) and never above 7."""
    assert MB._morale_start(stance) == expected, (
        f"stance={stance} should give morale_start {expected}, got {MB._morale_start(stance)}")


@pytest.mark.parametrize('stance, expected', [(-1.5, 4), (-0.5, 5), (0.5, 6), (-2.5, 3)])
def test_half_boundary_rounding_is_symmetric_not_banker_rounded(stance, expected):
    """(b2) Python's bare `round()` is round-half-to-even: `round(4.5) == 4` but `round(3.5) == 4`.
    A side's MEAN stance reaches an exact .5 in ordinary play -- half the side lost a field at
    `field_morale_weight` 1 -- so every .5 must round the same way (half-up)."""
    got = MB._morale_start(stance)
    assert got == expected, (
        f"stance={stance} should round half-up to {expected}, got {got} "
        f"(bare round() would give {round(MB._MORALE_START_BASE + stance)})")


def test_zero_stance_is_the_pre_change_flat_five(monkeypatch):
    """(c) THE CONTROL. A side whose members hold no stance toward their own faction -- every side
    in the shipped world, where no field has been lost -- starts at the flat 5 every unit started
    at before `20-iv`, so nothing this position changed moves a world that has fought no field."""
    u_a, u_b = _captured_units(monkeypatch)
    assert (u_a.morale_start, u_a.morale) == (5, 5), f"default side_a moved: {u_a.morale_start}"
    assert (u_b.morale_start, u_b.morale) == (5, 5), f"default side_b moved: {u_b.morale_start}"


def test_resolve_field_is_still_deterministic_under_a_fixed_seed():
    """(d) Same-seed determinism through the season entry point, with a non-zero morale and a
    fortified territory so both new inputs are inside the replayed battle."""
    def _run(seed):
        w = build_realm(0)
        att = world_q.mustered(w, "set_s_014", "fac_crown")
        dfn = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
        return MB.resolve_field(_record(w, att, dfn, territory="T9", fort_level=1.0,
                                        stance_a=-1.0, stance_b=0.0), rng=random.Random(seed))

    r1, r2 = _run(12345), _run(12345)
    assert r1 == r2, f"same-seed resolve_field diverged: {r1} vs {r2}"
    # vacuous if resolve_field silently no-op'd -- the shape a real resolution produces (§0.1 pt 2)
    assert set(r1) == {'attacker_wins', 'degree', 'attacker_size_pct', 'defender_size_pct'}
    assert r1['degree'] in ('Overwhelming', 'Success', 'Partial', 'Failure')


def test_morale_start_is_monotone_and_bounded_across_the_whole_stance_range():
    """(e) Every tenth of a stance unit across one row's whole span, -25..+25: monotone
    non-decreasing and inside [1, 7] throughout. A loop that asserts conditionally asserts that it
    ran (CLAUDE.md §0.1 pt 2)."""
    checked = 0
    prev = None
    for tenth in range(-250, 251):
        m = MB._morale_start(tenth / 10.0)
        assert 1 <= m <= 7, f"stance={tenth / 10.0} produced out-of-ladder morale_start {m}"
        if prev is not None:
            assert m >= prev, f"morale_start fell as stance rose to {tenth / 10.0}: {prev} -> {m}"
        prev = m
        checked += 1
    assert checked >= 501, f"the stance sweep only checked {checked} values -- it did not run"


def test_a_lost_field_lowers_the_next_fields_morale_start_end_to_end(monkeypatch):
    """(f) THE SOURCE IS SEASON STATE, SHOWN BY THE WRITER AND THE READER MEETING. `p_npc_033`'s
    Crown army (2) marches on `set_s_036` (Church of Solmund, 6) through the real driver --
    RESOLVE then ENCOUNTER, `test_march.py`'s `_fold_one` -- and loses: `_eff_march` writes
    `(fac_crown, -1.0, field_morale_weight)` on each attacker. The SAME two men then take the
    field again, through the provider, and their unit starts at `5 - field_morale_weight`, while
    the winners, who wrote nothing, start at 5. Swept to weight 3 so the move is not a one-point
    coincidence. Before `20-iv` both starts were the literal 5 whatever had happened."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_morale_weight", 3)
    morale_w = w.fixtures.get("field_morale_weight")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    assert len(attackers) == 2 and len(defenders) == 6, (
        f"the fixture no longer gives a 2-v-6 mismatch ({attackers}, {defenders})")
    assert provider._side_stance(w, attackers) == 0.0, "the attackers held a morale row before any fight"

    d = SeasonDriver(w)
    w.step, w.frozen = Step.RESOLVE, False
    act = Act(id="m1", actor="p_npc_033", verb="march", payload={"subject": "set_s_036"},
              via="off_npc_033")
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    assert ("field.lost", "Lost") in [(e.kind, e.degree) for e in events], (
        "the first field was not fought and lost; the writer never ran")
    assert provider._side_stance(w, attackers) == -1.0 * morale_w, (
        f"the losers' mean stance toward their own faction is {provider._side_stance(w, attackers)}, "
        f"not -{morale_w}")

    captured = {}

    def fake(unit_a, unit_b, terrain, rng, walls_dr=None):
        captured["a"], captured["b"] = unit_a.morale_start, unit_b.morale_start
        return {"attacker_wins": False, "degree": "Failure",
                "attacker_size_pct": 1.0, "defender_size_pct": 1.0}

    monkeypatch.setattr(MB, "_run_and_grade", fake)
    r = provider.resolve(w, attackers, ["c"], "a field", subject="fac_church_of_solmund",
                         rung="set_s_036", rng=random.Random(1))
    assert r["status"] == "RESOLVED" and r["unopposed"] is False, f"the second field was not fought: {r}"
    assert captured["a"] == 5 - morale_w, (
        f"the beaten side starts the next field at morale {captured['a']}, not {5 - morale_w}")
    assert captured["b"] == 5, f"the winners started at {captured['b']}, not the untouched 5"


def _starts_at_gain(monkeypatch, gain):
    """MB-03's observer: every faction's mustered side at every settlement of `build_realm(0)`, fought as
    the attacker against the Church's six at `set_s_036` through the host builder and the module entry
    (`field_input` -> `resolve_field`) with the `field_morale_loyalty_gain` fixture swept to `gain`.
    Returns `({(settlement, faction): (attacker loyalty, attacker morale_start)}, defender morale_start)`,
    read off the constructed Units (`_run_and_grade` intercepted, as `_captured_units` does)."""
    captured = {}

    def fake(unit_a, unit_b, terrain, rng, walls_dr=None):
        captured["a"], captured["b"] = unit_a.morale_start, unit_b.morale_start
        return {"attacker_wins": True, "degree": "Success",
                "attacker_size_pct": 1.0, "defender_size_pct": 0.0}

    monkeypatch.setattr(MB, "_run_and_grade", fake)
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_morale_loyalty_gain", gain)
    defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    factions = sorted({world_q.faction_holding(w, pid) for pid in w.persons} - {None})
    out, defender = {}, set()
    for rung in sorted(r for r, v in w.rungs.items() if v.kind == "settlement"):
        for fac in factions:
            side = world_q.mustered(w, rung, fac)
            if not side:
                continue
            rec = field_input(w, side, defenders, "set_s_036")
            assert rec.loyalty_gain == gain, f"the swept gain did not reach the record: {rec.loyalty_gain}"
            MB.resolve_field(rec)
            out[(rung, fac)] = (rec.loyalties[0], captured["a"])
            defender.add(captured["b"])
    assert len(defender) == 1, f"one defending side started at several values: {defender}"
    return out, defender.pop()


def test_at_loyalty_gain_zero_every_side_starts_at_five(monkeypatch):
    """MB-03 (`ED-MB-0078`'s superseding row), THE CONTROL: at `field_morale_loyalty_gain` 0 -- the
    shipped default -- every side of the built realm starts at the flat 5, whatever its build-time
    loyalty row, because no field has been lost (option (a), battle history only). The loyalty is
    READ (the sides' means differ, asserted) and multiplied away, so this observes the gain, not an
    unread input."""
    assert build_realm(0).fixtures.get("field_morale_loyalty_gain") == 0, "the shipped gain moved off 0"
    starts, defender = _starts_at_gain(monkeypatch, 0)
    assert len(starts) >= 20, f"only {len(starts)} sides were fought -- the sweep did not run"
    assert len({loyalty for loyalty, _ in starts.values()}) >= 2, "every side read one loyalty"
    assert defender == 5, f"the defenders started at {defender} at gain 0"
    moved = {k: v for k, v in starts.items() if v[1] != 5}
    assert not moved, f"sides moved off 5 at gain 0: {moved}"


@pytest.mark.parametrize("gain, crown, church", [(0.4, 6, 7), (0.7, 6, 7)])
def test_a_positive_loyalty_gain_starts_factions_with_different_rows_apart(monkeypatch, gain, crown, church):
    """MB-03, THE FALSIFIER'S OTHER HALF: at each non-control arm, two factions whose loyalty rows
    differ start apart. The Crown's two at `set_s_014` hold a side mean of 2.0 toward their creed's
    utterer, the Church's six at `set_s_036` 4.0: at 0.4, 5 + 0.8 -> 6 against 5 + 1.6 -> 7; at 0.7,
    5 + 1.4 -> 6 against 7.8 -> 8 clamped to 7 (the ceiling). RE-DERIVED at v9 FA-05 (B-X): the Crown's mean was 0.5
    (measured 2026-10-12, gains 0.4 and 1 -> starts 5 and 6) before the Crown goal row added a stance
    toward the King beside the creed row `_side_stance` sums (`stance_toward` sums every row naming the
    referent). At gain 1 the Crown now reaches the ceiling with the Church, so the second arm moved to
    0.7, where the two still start apart. Across every side of the realm the start never falls as
    loyalty rises (no battle history at build, so loyalty is the only term)."""
    starts, defender = _starts_at_gain(monkeypatch, gain)
    loyalty, start = starts[("set_s_014", "fac_crown")]
    assert loyalty == 2.0, f"the Crown side's loyalty moved ({loyalty}); re-derive the pinned starts"
    assert (start, defender) == (crown, church), (
        f"gain {gain}: Crown and Church started at {(start, defender)}, not {(crown, church)}")
    ordered = sorted(starts.values())
    checked = 0
    for (l0, m0), (l1, m1) in zip(ordered, ordered[1:]):
        assert m0 <= m1, f"gain {gain}: loyalty {l0} -> {l1} lowered the start {m0} -> {m1}"
        checked += 1
    assert checked >= 19, f"only {checked} side pairs were compared"
