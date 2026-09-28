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
    the falsifying check for claim 2 above, on a real fight rather than a hand-built degree.

    ⚠ `field_grudge_weight` AND `field_morale_weight` ARE SWEPT TO DIFFERENT VALUES HERE,
    DELIBERATELY -- both default to `1` (H-148), so an assertion using the DEFAULTS cannot tell
    which weight landed on which faction: `(fac_church_of_solmund, -1.0, 1)` and
    `(fac_crown, -1.0, 1)` are both present whichever way `winner_faction`/`loser_faction` were
    assigned. This is the exact gap `/code-review` found: a first writing of `_eff_march` swapped
    the two ternaries (`winner_faction = attacker_faction if attacker_lost else ...`, backwards),
    landing the grudge on the LOSER's own faction and the morale hit on the WINNER -- and this
    test, at the shared default, could not see it. Distinct weights make the two rows
    distinguishable by VALUE, not merely by presence."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_grudge_weight", 3)
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

    grudge_w = w.fixtures.get("field_grudge_weight")
    morale_w = w.fixtures.get("field_morale_weight")
    assert grudge_w != morale_w, "the two weights collided; this test can no longer discriminate"
    for pid in attackers:
        rows = {(ref, val, wt) for ref, val, wt in (w.persons[pid].stance or [])}
        assert ("fac_church_of_solmund", -1.0, grudge_w) in rows, (
            "no grudge row, AT THE GRUDGE WEIGHT, against the winning faction")
        assert ("fac_crown", -1.0, morale_w) in rows, (
            "no morale-hit row, AT THE MORALE WEIGHT, against the loser's own faction")
        assert ("fac_church_of_solmund", -1.0, morale_w) not in rows, (
            "the winning faction took the MORALE weight instead of the grudge weight -- "
            "winner_faction/loser_faction are swapped")
        assert ("fac_crown", -1.0, grudge_w) not in rows, (
            "the loser's own faction took the GRUDGE weight instead of the morale weight -- "
            "winner_faction/loser_faction are swapped")
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


def test_a_march_on_a_non_settlement_rung_refuses_h149_is_enforced():
    """FALSIFIER for the second gap `valoria-critic` found: `H-149` (`march_target_kinds`) closes
    the roster at `[settlement]`, and `verb_table.yaml`'s own `requires_typed_note` claimed
    `_eff_march` enforces it -- it did not; nothing read `MARCH_TARGET_KINDS` at all. A march on a
    hearth (a real, existing Rung -- `requires_typed`'s `kind: Rung` check passes) now refuses at
    the fight rather than running a battle scoped to one building."""
    w = build_realm(0)
    hearth = next(rid for rid, r in w.rungs.items() if r.kind == "hearth")
    act = _march_act("p_npc_033", hearth, "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("march.refused", None) in kinds, (
        f"expected a graceful refusal for a non-settlement target, got {kinds}")


def test_a_march_act_reaches_self_resolved_exactly_once_across_both_folds():
    """FALSIFIER for a real double-count `/code-review` found: RESOLVE's Declared fold and
    ENCOUNTER's real fold both call `_fold` for the SAME `Act` object, and `_fold`'s own
    `self.resolved.append(a)` had no guard against that -- unlike `w.acts.append`, which is
    DELIBERATELY idempotent on a repeated id for exactly this reason (two entry points, one act).
    `self.resolved` is what `harness/populated.py`'s `out["acts"]` counts (`len(d.resolved)`), so
    every march inflated that report by one. `_fold` now dedupes by id, matching `w.acts`'s own
    precedent."""
    w = build_realm(0)
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
    assert [a.id for a in d.resolved] == ["m1"], (
        "the Declared fold at RESOLVE should record the act exactly once")
    d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    assert [a.id for a in d.resolved] == ["m1"], (
        f"the act was recorded {len([a for a in d.resolved if a.id == 'm1'])} times after "
        "ENCOUNTER's real fold, not once")


def test_a_march_on_an_unheld_settlement_refuses_rather_than_crashing_the_season():
    """FALSIFIER for the crash `valoria-critic` found in the adversarial pass on this build, not
    anticipated while writing it: `march` on a settlement Rung with no HELD ancestor sent
    `sides_of`'s `subject=None` into `mass_battle.py::resolve()`, which reports that shape as
    `status="PARTY-GAP"` -- and `seam/contest.py` raised an uncaught `Unspecified` for ANY
    non-RESOLVED status, crashing `encounter()` and the whole season. `loop/resolve.py::_contest`
    now catches `Unspecified(needs="PARTY-GAP")` around the `contest()` call and folds it as a
    graceful refusal, the same shape the pre-existing empty-`_parties` check already produced.

    ⚠ `set_s_037`, NOT `r_valoria` (M4 review pass, second correctional finding). The first
    writing of this test used `r_valoria`, the campaign root -- kind `realm`, not `settlement`.
    Once `sides_of`'s target-kind check (`H-149`) landed, `r_valoria` refuses through THAT branch
    before ever reaching `holder_faction_of`, so this test stopped exercising the path it was
    written for: a settlement that IS the right kind and genuinely has no held ancestor.
    `set_s_037` is `build_realm(0)`'s one such settlement, asserted below rather than assumed."""
    w = build_realm(0)
    assert w.rungs["set_s_037"].kind == "settlement", (
        "set_s_037 is no longer a settlement; this test needs one that is")
    assert world_q.holder_faction_of(w, "set_s_037") is None, (
        "set_s_037 is held after all; pick a genuinely unheld settlement")
    act = _march_act("p_npc_033", "set_s_037", "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("march.refused", None) in kinds, (
        f"expected a graceful refusal, got {kinds} -- did the crash come back?")


def test_a_won_field_writes_casualties_and_stance_on_the_defender_only():
    """FALSIFIER for a real, verified gap: `Won` (the ATTACKER wins, defenders lose) had NO
    execution coverage anywhere in this build. `test_a_lost_field...` above only exercises `Lost`,
    and `systems/mass_battle/sim/massbattle.py`'s own disclosed limitation -- corpus-scale forces
    (single/double-digit `weight` sums) rout on contact regardless of size, so `attacker_wins`
    (hence `Won`) may be UNREACHABLE through a real fold at this fixture's scale -- measured
    directly: the 6-attacker/2-defender REVERSE of the scenario below still resolved `Lost`.
    Rather than guess at a fixture combination the engine's own scale limitation may make
    impossible, this constructs the `Resolution` directly, the same technique
    `test_declared_and_unopposed_are_no_change_directly` already uses for the other two bands --
    `_eff_march`'s own logic does not care where a `Resolution` came from, only what `res.degree`
    and `res.result` say."""
    w = build_realm(0)
    eff = EFFECTS["march"]
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    before_a = {pid: w.persons[pid].body for pid in attackers}
    before_d = {pid: w.persons[pid].body for pid in defenders}
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    res = Resolution("Won", {
        "parties": {"claimants": attackers, "subject_members": defenders},
        "result": {"defender_size_pct": 0.4},
    })
    change = eff(w, act, res)
    change.apply()  # bypassing the gate's own receipt-minting, which this test does not need

    for pid in attackers:
        assert w.persons[pid].body == before_a[pid], f"{pid} (the WINNING side) was written"
    for pid in defenders:
        assert w.persons[pid].body < before_d[pid], f"{pid} (the losing side) took no casualties"

    for pid in defenders:
        rows = {(ref, val, wt) for ref, val, wt in (w.persons[pid].stance or [])}
        assert ("fac_crown", -1.0, w.fixtures.get("field_grudge_weight")) in rows, (
            "no grudge row against the winning faction (the attacker)")
        assert ("fac_church_of_solmund", -1.0, w.fixtures.get("field_morale_weight")) in rows, (
            "no morale-hit row against the loser's own faction (the defender)")
    for pid in attackers:
        assert not any(ref in ("fac_crown", "fac_church_of_solmund")
                       for ref, _v, _w in (w.persons[pid].stance or [])), (
            "the winning side gained a stance row from a battle it won")


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
    deliberately (`wound_harm_model`'s own precedent).

    ⚠ `remove_person` ON `body <= 0`, `_eff_kill`'s OWN PRECEDENT, ADDED IN THE M4 REVIEW PASS
    (`/code-review` finding): the first writing of `total` left a living person recorded at body
    0, a state `_eff_kill` never produces. The person is gone from `w.persons`, not merely
    zeroed."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_casualty_model", "total")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    _fold_one(w, act, contest_max_depth=2)
    for pid in attackers:
        assert pid not in w.persons, f"{pid} still recorded, at body 0, instead of removed"


def test_the_none_casualty_model_writes_stance_only():
    """`field_casualty_model = "none"` -- the second control, isolating the write from the band:
    the stance rows still land (the band selected a write set that includes them), the body
    does not move at all.

    ⚠ `assert w.persons[pid].stance` ALONE WOULD PASS VACUOUSLY -- `build_realm` pre-seeds every
    person's loyalty as a stance row (`data/cast.py::stance_from_loyalty`), so a truthy `stance`
    is true BEFORE the march runs and proves nothing about what `_eff_march` wrote. Checking the
    two SPECIFIC new rows against a before/after snapshot, on `wound_harm_model`'s own precedent
    for isolating "the write happened" from "the value moved", is the falsifying version
    (`/code-review` finding on the M4 diff)."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_casualty_model", "none")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    before_body = {pid: w.persons[pid].body for pid in attackers}
    before_stance = {pid: list(w.persons[pid].stance or []) for pid in attackers}
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    _fold_one(w, act, contest_max_depth=2)
    grudge_w = w.fixtures.get("field_grudge_weight")
    morale_w = w.fixtures.get("field_morale_weight")
    for pid in attackers:
        assert w.persons[pid].body == before_body[pid]
        after_new = {(r, v, wt) for r, v, wt in (w.persons[pid].stance or [])} - set(before_stance[pid])
        assert after_new == {
            ("fac_church_of_solmund", -1.0, grudge_w),
            ("fac_crown", -1.0, morale_w),
        }, f"{pid} gained {after_new}, not exactly the grudge/morale pair, under the `none` model"
