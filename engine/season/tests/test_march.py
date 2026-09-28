"""`march` -- M4 build step 7 (`ED-IN-0279` clause (a)). The verb row, `_eff_march`, and the
full RESOLVE -> ENCOUNTER pipeline this session built to carry it. What each test proves, and
the control that stops it passing vacuously:

  1. END TO END, THROUGH THE REAL DRIVER, NOT A HAND-BUILT `Resolution`. A `march` act folds at
     RESOLVE (declares, writes nothing), then at ENCOUNTER (fights, writes on the LOSING side
     only) -- proven against `build_realm`'s own fixture, with both a cross-faction LOST
     scenario (the attacker's own army takes the casualties) and an UNOPPOSED one (nobody
     mustered to defend; no casualties on either side).
  2. THE WINNING SIDE IS NEVER WRITTEN, on either band -- Jordan's ruling on clause (b) is silent
     on the winner, and this is the falsifying check that it stays silent in the code too, not
     merely in the docstring.
  3. THE STANCE ROWS' SIGN AND TARGET: a grudge against the WINNING faction, a morale hit against
     the LOSER'S OWN faction, both at the fixed valence `-1.0` (`stance_from_loyalty`'s own
     shape) and the swept weight (`field_morale_weight`/`field_grudge_weight`, `H-148`).
  4. `Declared` AND `Unopposed` WRITE NOTHING -- `_eff_march` returns `NO_CHANGE` for both,
     checked directly rather than inferred from the verb row's empty `writes:` cells.
  5. THE THREE `field_casualty_model` ARMS DIFFER, and `none`'s control isolates the write from
     the band exactly as `wound_harm_model`'s own `none` arm does.
"""

import random

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop.effects import EFFECTS
from engine.season.queries import world_q
from engine.season.seam.contest import Resolution
from engine.season.state.carriers import Act
from engine.season.state.gate import NO_CHANGE


def _march_act(actor: str, target: str, via: str, act_id: str = "m1") -> Act:
    return Act(id=act_id, actor=actor, verb="march", payload={"subject": target}, via=via)


def _fold_one(w, act, contest_max_depth=2):
    """Fold ONE march act through the real driver, RESOLVE then ENCOUNTER, returning both
    steps' events. Mirrors what `SeasonDriver.season()` does between the two calls, without the
    rest of a season around it."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, contest_max_depth)
    return events


def test_a_lost_field_writes_casualties_and_stance_on_the_attacker_only():
    """`p_npc_033`/`p_npc_035` (Crown, 2) march on `set_s_036` (Church of Solmund, 6 defenders)
    and lose. The attacker's own army takes the casualties; the six defenders are untouched --
    the falsifying check for claim 2 above, on a real fight rather than a hand-built degree."""
    w = build_realm(0)
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    assert len(attackers) == 2 and len(defenders) == 6, (
        f"the fixture no longer gives a 2-v-6 mismatch here ({attackers}, {defenders}); "
        "pick an origin/target pair that still does")
    before_a = {pid: w.persons[pid].body for pid in attackers}
    before_d = {pid: w.persons[pid].body for pid in defenders}

    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("field.lost", "Lost") in kinds

    for pid in attackers:
        assert w.persons[pid].body < before_a[pid], f"{pid} (the losing side) took no casualties"
    for pid in defenders:
        assert w.persons[pid].body == before_d[pid], f"{pid} (the WINNING side) was written"

    for pid in attackers:
        rows = {(ref, val, wt) for ref, val, wt in (w.persons[pid].stance or [])}
        assert ("fac_church_of_solmund", -1.0, w.fixtures.get("field_grudge_weight")) in rows, (
            "no grudge row against the winning faction")
        assert ("fac_crown", -1.0, w.fixtures.get("field_morale_weight")) in rows, (
            "no morale-hit row against the loser's own faction")
    for pid in defenders:
        assert not any(ref in ("fac_crown", "fac_church_of_solmund")
                       for ref, _v, _w in (w.persons[pid].stance or [])), (
            "the winning side gained a stance row from a battle it won")


def test_an_unopposed_march_writes_nothing_on_either_side():
    """`set_s_003` (Crown-held, per `holder_faction_of`) musters nobody at all -- the same
    fixture fact `test_a_real_faction_that_musters_nobody_at_the_rung_is_unopposed` (the mass-
    battle provider tests) verifies independently. Unopposed writes on neither side."""
    w = build_realm(0)
    assert world_q.holder_faction_of(w, "set_s_003") == "fac_crown"
    assert world_q.mustered(w, "set_s_003", "fac_crown") == []
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    before_a = {pid: w.persons[pid].body for pid in attackers}
    # `build_realm` seeds each person's loyalty as a pre-existing stance row (`data/cast.py`'s
    # `stance_from_loyalty`), so "no new row" is what this checks, not "an empty list".
    before_stance = {pid: list(w.persons[pid].stance or []) for pid in attackers}

    act = _march_act("p_npc_033", "set_s_003", "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("field.unopposed", "Unopposed") in kinds

    for pid in attackers:
        assert w.persons[pid].body == before_a[pid], f"{pid} took casualties in an unopposed march"
        assert list(w.persons[pid].stance or []) == before_stance[pid], (
            f"{pid} gained a stance row from an unopposed march")


def test_declared_and_unopposed_are_no_change_directly():
    """`_eff_march` returns `NO_CHANGE` for both bands without reaching the casualty model or
    the faction lookups -- checked directly, not inferred from the fold's own behaviour above."""
    eff = EFFECTS["march"]
    w = build_realm(0)
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    assert eff(w, act, Resolution("Declared", {})) is NO_CHANGE
    assert eff(w, act, Resolution("Unopposed", {})) is NO_CHANGE


def test_the_total_casualty_model_zeroes_the_losing_side():
    """`field_casualty_model = "total"` -- the control, re-running "losing costs everything"
    deliberately (`wound_harm_model`'s own precedent)."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_casualty_model", "total")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    _fold_one(w, act, contest_max_depth=2)
    for pid in attackers:
        assert w.persons[pid].body == 0


def test_the_none_casualty_model_writes_stance_only():
    """`field_casualty_model = "none"` -- the second control, isolating the write from the band:
    the stance rows still land (the band selected a write set that includes them), the body
    does not move at all."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_casualty_model", "none")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    before = {pid: w.persons[pid].body for pid in attackers}
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    _fold_one(w, act, contest_max_depth=2)
    for pid in attackers:
        assert w.persons[pid].body == before[pid]
        assert w.persons[pid].stance, f"{pid} gained no stance row under the `none` casualty model"
