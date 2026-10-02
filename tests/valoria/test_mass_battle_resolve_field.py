"""`systems/mass_battle/sim/massbattle.py::resolve_field` -- M3 of the `mc_v18`-retirement plan
(`ED-IN-0279`), the season-facing entry point `engine/season/seam/wrappers/mass_battle.py` calls.

Lives here, not in `engine/season/tests/`, because it needs `from systems.mass_battle...` at
module scope to reach `massbattle` directly for monkeypatching, and
`tests/valoria/test_engine_does_not_import_systems.py`'s `NESTED_BASELINE`/`BASELINE_TOTAL` ratchet
(zero `systems.*` imports anywhere under `engine/`, top-level or function-local) applies to
`engine/season/tests/` too -- `test_mass_battle_d1_morale_baseline.py` already imports `massbattle`
this same way from this same location; this follows that precedent rather than being new.

What this proves, and the control that stops it passing vacuously: `resolve_field` sums
`Person.weight` per side into `Subunit.troops` (army SIZE), against an INDEPENDENTLY-COMPUTED
total, and NEVER into `Unit.power` (a quality stat) -- verified by intercepting `_run_and_grade`'s
constructed Units, not by reading emergent battle outcomes off real corpus headcounts. An earlier
draft of this test tried the emergent-outcome route and found it unusable: at real corpus scale
(single/double-digit weights), the sum is far below this engine's own `SUBUNIT_ROUT_FLOOR`
calibration and both sides rout on contact regardless of who is stronger -- see
`massbattle.py::_MIN_TROOPS`'s own disclosure of that gap.
"""
from systems.mass_battle.sim import massbattle

from engine.season.harness.populated import build_realm
from engine.season.queries import faction_q


def test_resolve_field_sums_weight_per_side_into_troops_not_power(monkeypatch):
    captured = {}

    def fake_run_and_grade(unit_a, unit_b, terrain, world, walls_dr=None):
        captured["troops_a"] = unit_a.subunits[0].troops
        captured["troops_b"] = unit_b.subunits[0].troops
        captured["power_a"] = unit_a.power
        captured["power_b"] = unit_b.power
        return {"attacker_wins": True, "degree": "Success",
                "attacker_size_pct": 1.0, "defender_size_pct": 0.0}

    monkeypatch.setattr(massbattle, "_run_and_grade", fake_run_and_grade)
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    guilds = faction_q.resolve(w, "fac_guilds")
    massbattle.resolve_field(w, crown.members, guilds.members)

    assert captured["troops_a"] == sum(w.persons[p].weight for p in crown.members)
    assert captured["troops_b"] == sum(w.persons[p].weight for p in guilds.members)
    assert captured["troops_a"] != captured["troops_b"], (
        "control is vacuous if Crown and Guilds happen to weigh the same in this corpus")
    # Headcount must land on SIZE (`troops`), never on the quality stat (`power`) -- the mistake
    # an adversarial review caught: feeding weight into `power` would make a bigger army fight
    # better PER TROOP too, backwards of what more bodies means.
    assert captured["power_a"] == captured["power_b"] == massbattle._SEASON_FORCE_POWER


def test_resolve_field_does_not_crash_on_a_zero_weight_side():
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    # `Unit.total_troops() == 0` divides by zero deep in `orchestration.resolve_engagements`;
    # `_MIN_TROOPS` exists so a truly empty side does not reach that crash.
    result = massbattle.resolve_field(w, crown.members, [])
    assert result["degree"] in {"Overwhelming", "Success", "Partial", "Failure"}
