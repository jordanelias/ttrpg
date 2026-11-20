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

import pytest

from engine.season.data.rosters import FIELD_CASUALTY_MODELS
from engine.season.harness import arms as oracle
from engine.season.boot.realm import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.data.matrix import Step, WriteClass
from engine.season.queries import world_q


def _march_act(actor: str, target: str, via: str):
    from engine.season.state.carriers import Act
    return Act(id="m1", actor=actor, verb="march", payload={"subject": target}, via=via)


def _fold_one(w, act, contest_max_depth=2):
    """Fold ONE `march` act through the real driver, RESOLVE then ENCOUNTER — the same helper
    `engine/season/tests/test_march.py` uses to exercise this exact fixture, kept small here
    rather than imported cross-file (a test module is not a library)."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, contest_max_depth)
    return events


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


def test_the_total_arm_actually_changes_the_casualty_write():
    """THE FALSIFIER. Two arms that write the same body value are a fake control, not a null
    result — same kind of claim `tools/balance_oracle.py`'s ladder falsifier made, now on the
    mechanic that replaces it: a real `march` act, folded through the real driver against
    `build_realm`'s own fixture (`test_march.py`'s own worked 2-v-6 mismatch), must produce a
    DIFFERENT losing-side body under `total` than under `scaled_by_degree`.
    """
    attackers_before = None
    bodies = {}
    for arm_name in ("total", "scaled_by_degree"):
        w = build_realm(0)
        w.fixtures = w.fixtures.sweep("field_casualty_model", oracle.ARMS[arm_name])
        attackers = world_q.mustered(w, "set_s_014", "fac_valorsmark")
        defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
        assert len(attackers) == 2 and len(defenders) == 6, (
            f"the fixture no longer gives a 2-v-6 mismatch here ({attackers}, {defenders}); "
            "pick an origin/target pair that still does")
        if attackers_before is None:
            attackers_before = {pid: w.persons[pid].body for pid in attackers}
        act = _march_act("p_npc_033", "set_s_036", "off_spymaster")
        events = _fold_one(w, act, contest_max_depth=2)
        kinds = [(e.kind, e.degree) for e in events]
        assert ("field.lost", "Lost") in kinds, (
            f"this fixture no longer produces a LOST field battle for the arm to grade: {kinds}")
        # `total` drives body to 0 AND `_eff_march.perform()` removes the person outright
        # (`w.remove_person`, the same `body <= 0` precedent `_eff_kill` sets) — so a felled
        # attacker is simply ABSENT from `w.persons` afterwards, not present at body 0. Both are
        # "no body left"; a missing key reads as 0 here rather than raising `KeyError`.
        bodies[arm_name] = {pid: (w.persons[pid].body if pid in w.persons else 0)
                            for pid in attackers}

    for pid in attackers_before:
        assert bodies["total"][pid] == 0, (
            f"the `total` arm did not zero (or remove) {pid} — it has lost its grip on "
            f"`field_casualty_model` and any comparison run under it would be fake")
        assert bodies["scaled_by_degree"][pid] > 0, (
            f"the `scaled_by_degree` arm killed {pid} outright — a wound (never `total`) cannot "
            f"kill on this arm; it has lost its grip on the fixture")
        assert bodies["total"][pid] != bodies["scaled_by_degree"][pid], (
            f"{pid} took the same body write under both arms — the two arms are not distinguishable")


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


def test_b0360_run_arm_counts_the_field_events_at_a_fought_band():
    """B03.60: `run_arm` returns `fought`, the field Events at a fought band (`Won`/`Lost`; not
    `Declared`, `Unopposed` or `Invested`). Asked of hand-built logs with literal counts."""
    from types import SimpleNamespace as NS
    ev = lambda kind, degree: NS(kind=kind, degree=degree)
    log = [ev("field.won", "Won"), ev("field.lost", "Lost"), ev("field.unopposed", "Unopposed"),
           ev("march.declared", "Declared"), ev("field.lost", "Lost"), ev("fight.done", "Won")]
    assert oracle.fought_fields(NS(log=log)) == 3
    assert oracle.fought_fields(NS(log=log[2:4])) == 0
    assert "fought" in oracle.run_arm({"fixtures": {}}, 0, 0, 1)


def test_b0360_main_prints_not_computable_instead_of_a_z_at_zero_fought_fields(monkeypatch, capsys):
    """B03.60 falsifier: a z printed at zero fought fields. Both arms report zero fought fields and
    differing tallies, which would give a z; `main` must print NOT-COMPUTABLE and no z. Control: with a
    fought field in one arm the z is printed."""
    import collections

    def fake(model, n, base_seed, seasons, fought=0):
        t = collections.Counter({"self": 5 if model == "total" else 9, "other": 5})
        return {"tally": t, "acts": sum(t.values()), "seeds": n, "fought": fought}
    monkeypatch.setattr(oracle, "run_arm", fake)
    oracle.main(["--n", "1"])
    out = capsys.readouterr().out
    assert "NOT-COMPUTABLE" in out and "SIGNIFICANT" not in out
    monkeypatch.setattr(oracle, "run_arm",
                        lambda m, n, s, k: fake(m, n, s, k, fought=2 if m == "total" else 0))
    oracle.main(["--n", "1"])
    out = capsys.readouterr().out
    assert "NOT-COMPUTABLE" not in out


def test_b0360_fixture_flag_exposes_the_mapping_form():
    assert oracle._fixture_arms("field_casualty_model=total,none") == {
        "total": {"fixtures": {"field_casualty_model": "total"}},
        "none": {"fixtures": {"field_casualty_model": "none"}}}


@pytest.mark.parametrize("value, current, want", [
    ("2", 2, 2),                       # a numeric fixture takes its number
    ("2.5", 1.0, 2.5),
    ("2", 1.0, 2),                     # an int may stand for a float
    ("False", True, False),            # `bool("False")` is True: the value is parsed, never coerced
    ("True", True, True),
    ("total", "scaled_by_degree", "total"),     # a str fixture keeps the raw string
    (5, 2, 5),                         # an already-typed value passes through
    ("3", None, 3),                    # a fixture shipped as `None` (`refusal_axis`, ...) has no type to hold: the literal stands
])
def test_b0360_a_fixture_value_is_parsed_to_the_fixtures_own_type(value, current, want):
    got = oracle._typed_fixture("f", value, current)
    assert got == want
    assert type(got) is type(want)


@pytest.mark.parametrize("value, current", [
    ("maybe", True),                   # not a literal at all, and the fixture is not a str
    ("2", True),                       # an int where a bool lives
    ("True", 2),                       # a bool where an int lives
    ("2.5", 2),                        # a float where an int lives
    ("'x'", 2),                        # a str where an int lives
])
def test_b0360_a_wrongly_typed_fixture_value_is_refused_naming_the_fixture(value, current):
    with pytest.raises(ValueError, match="ceiling_per_pool"):
        oracle._typed_fixture("ceiling_per_pool", value, current)


def test_b0360_run_arm_refuses_a_wrongly_typed_fixture():
    with pytest.raises(ValueError, match="ceiling_per_pool"):
        oracle.run_arm({"fixtures": {"ceiling_per_pool": "maybe"}}, 1, 0, 1)


def test_b0360_a_fixture_pair_prints_its_z_even_at_zero_fought_fields(monkeypatch, capsys):
    """NOT-COMPUTABLE is the shipped `field_casualty_model` pair's verdict only: a fixture other than that one need
    not act through a fought field. A `--fixture` pair prints the z, with the fought counts beside it."""
    import collections

    def fake(model, n, base_seed, seasons):
        t = collections.Counter({"self": 50 if model["fixtures"]["obstacle_default"] == "2" else 150, "other": 50})
        return {"tally": t, "acts": sum(t.values()), "seeds": n, "fought": 0}
    monkeypatch.setattr(oracle, "run_arm", fake)
    oracle.main(["--n", "1", "--fixture", "obstacle_default=2,5"])
    out = capsys.readouterr().out
    assert "NOT-COMPUTABLE" not in out and "fought fields" in out
    assert "SIGNIFICANT" in out, out      # 50/100 against 150/200 pooled: well over the threshold
