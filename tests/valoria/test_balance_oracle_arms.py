"""The season-side arms still construct, and the live pair still differs (plan position `28-i`).

WHY THIS EXISTS, and why it is not apparatus-guarding-apparatus. `engine/season/harness/arms.py`
is the n-seed two-arm balance instrument that replaces `tools/balance_oracle.py` for
`engine/season`-only mechanics — CLAUDE.md names the class of control this is (§0.1 pt 4), and
`rosters.yaml`'s `field_casualty_models` note names this SPECIFIC mechanic as one
`tools/balance_oracle.py` structurally could not observe. It is deliberately NOT a CI gate — a
realm build alone costs the better part of a second and a season run costs tens of seconds, so an
n>=10 comparison is minutes, not something CI should run on every push. The consequence, same as
the file it replaces, is that nothing executes the FULL comparison automatically — so this file
constructs and undoes every arm cheaply (milliseconds; no campaigns, no realms) and exercises the
live pair's actual write once, on a real fold, which is the falsifier CLAUDE.md §0.1 pt 4 demands:
"a number without a control is not a measurement."

WHAT MOVED, AND WHY (`arms.py`'s own module docstring has the full account). The old live pair,
`private_ladder`/`owner_ladder`, is retired rather than ported: verified against the live tree that
it is NOT season-reachable (`engine/season/seam/ladder.py`'s `degree_of` never calls
`systems.social_contest.sim.contest.resolver`; the season loop's own margin path imports
`engine.dice_engine.dice_engine.degree_from_net` directly), and porting it even as inert historical
code would add a NEW nested `engine -> systems` import `test_engine_does_not_import_systems.py`'s
`NESTED_BASELINE = 0` ratchet forbids. Its code survives at this commit's `FORK:` row in
`references/restructure_ledger.md` for `tools/balance_oracle.py`. The OTHER retired pair,
rounded-versus-fractional pool pair, was ported unchanged and has since been deleted with the
other two retired pairs; the record of all three is the `FORK:` row for `arms.py` in
`references/restructure_ledger.md`.

The live pair is now `field_casualty_model` — `total` (the pre-M4 control, "losing costs
everything") vs `scaled_by_degree` (the ruled default, `Person.body` scaled by the engine's own
survivor ratio and floored at 1). Both are read by exactly one call site,
`engine/season/loop/effects.py::_eff_march`, on a LOST field battle.
"""
from __future__ import annotations

from engine.season.data.rosters import FIELD_CASUALTY_MODELS
from engine.season.harness import arms as oracle


def test_the_live_arms_are_two_distinct_registered_fixture_values():
    """The construction-only check: exactly two arms, both real `field_casualty_models` members,
    and they differ. Two arms with the same value would be a fake control, not a null result —
    the same property `tools/balance_oracle.py`'s own test asserted of its arm count."""
    assert len(oracle.ARMS) == 2, f"expected exactly two arms, got {sorted(oracle.ARMS)}"
    values = set(oracle.ARMS.values())
    assert len(values) == 2, "the two arms have the same value; the comparison is a fake control"
    assert values <= set(FIELD_CASUALTY_MODELS), (
        f"arm value(s) {values - set(FIELD_CASUALTY_MODELS)} are not in the roster "
        f"({sorted(FIELD_CASUALTY_MODELS)})")


def test_two_proportion_z_generalises_the_equal_n_case():
    """`tools/balance_oracle.py`'s original assumed one shared `n`. This one takes two, and the
    equal-`n` call must reduce to exactly the old formula (checked against a hand-computed value)
    rather than silently changing what a shared-`n` caller gets."""
    z_new = oracle.two_proportion_z(30, 100, 40, 100)
    pooled = (30 + 40) / 200
    se = (pooled * (1 - pooled) * (1 / 100 + 1 / 100)) ** 0.5
    z_expected = (0.40 - 0.30) / se
    assert abs(z_new - z_expected) < 1e-9


def test_two_proportion_z_is_degenerate_safe():
    """An empty arm (zero acts) must not raise a `ZeroDivisionError` — the same defensive shape
    the original's pooled-rate guard had, extended to the new per-arm denominators."""
    assert oracle.two_proportion_z(0, 0, 5, 10) == 0.0
    assert oracle.two_proportion_z(5, 10, 0, 0) == 0.0
    assert oracle.two_proportion_z(0, 10, 0, 10) == 0.0   # pooled rate 0 -- degenerate


def test_an_arm_resolves_to_a_fixtures_and_a_build_half_against_literal_pairs():
    """CR-14 (iv): `run_arm` takes the shipped `field_casualty_model` string or a mapping with a
    `fixtures` half (swept onto the built world) and a `build` half (kwargs of `build_realm`). The
    one resolver is asked against LITERAL pairs, with no world built; swapping the halves in the
    resolver reds every assertion here but the empty mapping's."""
    resolve = oracle._resolve_arm
    assert resolve("total") == ({"field_casualty_model": "total"}, {})
    assert resolve({"fixtures": {"field_casualty_model": "total"}}) == (
        {"field_casualty_model": "total"}, {})
    assert resolve({"build": {"guards": True}}) == ({}, {"guards": True})
    assert resolve({"fixtures": {"field_casualty_model": "total"}, "build": {"guards": True}}) == (
        {"field_casualty_model": "total"}, {"guards": True})
    assert resolve({}) == ({}, {})


def test_an_arm_names_only_a_build_kwarg_or_a_fixture_half():
    """A build key `build_realm` does not take, or a third half, is refused by name before any world
    is built (a `TypeError` out of `build_realm` mid-run would name nothing)."""
    import pytest
    with pytest.raises(ValueError):
        oracle._resolve_arm({"build": {"seed": 3}})
    with pytest.raises(ValueError):
        oracle._resolve_arm({"fixture": {"field_casualty_model": "total"}})
    with pytest.raises(ValueError):
        oracle._resolve_arm(7)
    assert "seed" not in oracle.BUILD_KWARGS and "guards" in oracle.BUILD_KWARGS


def test_an_arm_naming_an_unregistered_fixture_is_refused_not_run_as_a_null_arm():
    """`Fixtures.sweep` writes any name; `run_arm` reads the name first (`Fixtures.get`), so a typo
    raises `Ungraded` instead of running an arm identical to its control."""
    import pytest
    from engine.season.gaps import Ungraded
    with pytest.raises(Ungraded):
        oracle.run_arm({"fixtures": {"field_casualty_modle": "total"}}, 1, 0, 1)


def test_the_shipped_arms_still_resolve_through_the_string_form():
    """`ARMS`, `main` and `two_proportion_z` are untouched: every shipped arm value is a `str` and
    resolves to the one fixture it always swept."""
    for model in oracle.ARMS.values():
        assert isinstance(model, str)
        assert oracle._resolve_arm(model) == ({"field_casualty_model": model}, {})
