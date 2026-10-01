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
`engine.autoload.dice_engine.degree_from_net` directly), and porting it even as inert historical
code would add a NEW nested `engine -> systems` import `test_engine_does_not_import_systems.py`'s
`NESTED_BASELINE = 0` ratchet forbids. Its code survives at this commit's `FORK:` row in
`references/restructure_ledger.md` for `tools/balance_oracle.py`. The OTHER retired pair,
`_ARMS_POOL`, imports nothing from `systems/` and is ported unchanged, same status as before:
historical record, importable, not wired into `ARMS`. (`_ARMS_FLOOR` and `_ARMS_BOUNDS` were ported
with it and DELETED at plan position `29b`, 2026-10-01: they patched `Faction.adjust` and
`descriptors.faction_bounds`, both deleted with the faction layer.)

The live pair is now `field_casualty_model` — `total` (the pre-M4 control, "losing costs
everything") vs `scaled_by_degree` (the ruled default, `Person.body` scaled by the engine's own
survivor ratio and floored at 1). Both are read by exactly one call site,
`engine/season/loop/effects.py::_eff_march`, on a LOST field battle.
"""
from __future__ import annotations

from engine.season.data.rosters import FIELD_CASUALTY_MODELS
from engine.season.harness import arms as oracle
from engine.season.harness.populated import build_realm
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
        attackers = world_q.mustered(w, "set_s_014", "fac_crown")
        defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
        assert len(attackers) == 2 and len(defenders) == 6, (
            f"the fixture no longer gives a 2-v-6 mismatch here ({attackers}, {defenders}); "
            "pick an origin/target pair that still does")
        if attackers_before is None:
            attackers_before = {pid: w.persons[pid].body for pid in attackers}
        act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
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


def test_the_retired_pair_definitions_still_import():
    """The retired comparison is kept as the record of what the old behaviour WAS — same
    status `tools/balance_oracle.py` gave it. Constructing it is enough to prove the symbols
    resolve. (Three pairs stood here until `29b` deleted `_ARMS_FLOOR` and `_ARMS_BOUNDS`.) `_contest_ladder_arm` (`private_ladder`/`owner_ladder`) is NOT among them; see
    `arms.py`'s own module docstring for why it has no surviving code in this tree at all (its
    record is the `FORK:` row for `tools/balance_oracle.py`, not a fourth retired dict here)."""
    for attr in ('_ARMS_POOL',):
        retired = getattr(oracle, attr)
        assert len(retired) == 2, f"{attr} should keep both arms of its pair"
        for setup in retired.values():
            setup()()
    assert not hasattr(oracle, '_ARMS_CONTEST_LADDER'), (
        "the contest-ladder pair was deliberately not carried into engine/season/ — "
        "see the module docstring; do not resurrect it here without re-checking both findings")
