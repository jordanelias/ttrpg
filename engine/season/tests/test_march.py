"""`march` -- M4 build step 7 (`ED-IN-0279` clause (a)). The verb row, `_eff_march`, and the
full RESOLVE -> ENCOUNTER pipeline this session built to carry it. What each test proves, and
the control that stops it passing vacuously:

  1. END TO END, THROUGH THE REAL DRIVER, NOT A HAND-BUILT `Resolution`. A `march` act folds at
     RESOLVE (declares, writes nothing), then at ENCOUNTER (fights, writes on the LOSING side
     only) -- proven against `build_realm`'s own fixture, with both a cross-faction LOST
     scenario (the attacker's own army takes the casualties) and an UNOPPOSED one (nobody
     mustered to defend; no casualties on either side; since v9 IN-13 the army ARRIVES).
  2. THE WINNING SIDE IS NEVER WRITTEN, on either band -- Jordan's ruling on clause (b) is silent
     on the winner, and this is the falsifying check that it stays silent in the code too, not
     merely in the docstring.
  3. THE STANCE ROWS' SIGN AND TARGET: a grudge against the WINNING faction, a morale hit against
     the LOSER'S OWN faction, both at the fixed valence `-1.0` (`stance_from_loyalty`'s own
     shape) and the swept weight (`field_morale_weight`/`field_grudge_weight`, `H-148`).
  4. `Declared` WRITES NOTHING, and `Unopposed` WRITES NO CASUALTY OR STANCE -- `_eff_march` returns
     `NO_CHANGE` for `Declared` and for an `Unopposed` carrying no claimants, checked directly rather
     than inferred from the verb row's `writes:` cells. (Before v9 IN-13 `Unopposed` wrote nothing at
     all; it now writes the ARRIVAL, `test_declared_is_no_change_and_unopposed_changes_only_with_...`.)
  5. THE THREE `field_casualty_model` ARMS DIFFER, and `none`'s control isolates the write from
     the band exactly as `wound_harm_model`'s own `none` arm does.
  6. A CHOOSER-FORMED DECISION, NOT A HAND-BUILT `Act` -- plan position `28-ii` (M6, successor
     goldens). Every test above mints its `Act` by hand (`_march_act`);
     `test_a_real_chooser_forms_and_folds_a_march_that_reaches_a_real_field_battle` does not. It
     first confirms, off `decision.options.opening_set` directly, that a real (constructed)
     `Question` naming a settlement referent already forms a march `Candidate` under clause 3's
     pre-existing `q.referents` reading -- no arm, no widening, nothing march-specific, and no
     kind filter (clause 3 applies none; ANY Rung-kind referent would do the same, settlement is
     simply the referent this test uses) -- then builds the `Act` through the real
     `decision.choose.make_chooser`/`pack_scenes` machinery (the same functions
     `SeasonDriver.season()` calls), so `act.via` is READ OFF the chooser's own derivation rather
     than hand-set, and folds it through the same RESOLVE -> ENCOUNTER pipeline as every other
     test in this file -- proving a real settlement target reaches a real field battle end to end
     through the real chooser, not merely that a hand-authored payload can.

     ⚠ THIS TEST'S OWN CHOOSER IS RESTRICTED (`verbs=frozenset({"march"})`), SO IT DOES NOT
     RANK MARCH AGAINST ANY COMPETING CANDIDATE -- a Phase 3 terminal critique's finding,
     2026-09-30. `python -m engine.season.harness.aperture 1 0`, run against `build_realm(0)`
     through the real, UNRESTRICTED chooser (`verbs=resolvable_verbs()`, `populated.run`'s own
     call), is the STRONGER demonstration: march forms, is offered, is attempted and executes
     there too, competing against every other verb's real candidates, with zero constructed
     `Question` and zero hand-built `Act` anywhere in the run (`hole_register.yaml` H-175). Both
     stand together; this test still proves the chooser-vs-constructed-`Act` distinction
     end-to-end at the unit level, and aperture proves the same mechanism holds under the real,
     unrestricted chooser in natural play.
"""

import random
from types import SimpleNamespace

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import faction_prop_id
from engine.season.decision.choose import make_chooser
from engine.season.decision.options import opening_set
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop.effects import EFFECTS
from engine.season.queries import person_q as PQ
from engine.season.queries import world_q
from engine.season.seam.contest import Resolution
from engine.season.state import gate as G
from engine.season.state.carriers import Act, Person, Question, Rung, Sensation, Tenure, View
from engine.season.state.ids import H, draw_factory


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


def test_an_unopposed_march_arrives_and_writes_no_casualty_or_stance():
    """`set_s_003` (Crown-held, per `holder_faction_of`) musters nobody at all -- the same
    fixture fact `test_a_real_faction_that_musters_nobody_at_the_rung_is_unopposed` (the mass-
    battle provider tests) verifies independently. Unopposed takes no casualty and writes no stance.

    v9 IN-13 EXIT (i), the `Unopposed` arm: THE ARMY ARRIVES. Before the arrival this test asserted
    that nothing at all was written, and it would have kept passing while observing nothing about
    presence (§14.8); it now asserts the presence moved -- `mustered(w, set_s_003, fac_crown)` equals
    the claimants after the fold, and the origin is emptied -- beside the unchanged no-casualty half."""
    w = build_realm(0)
    assert world_q.holder_faction_of(w, "set_s_003") == "fac_crown"
    assert world_q.mustered(w, "set_s_003", "fac_crown") == []
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    assert attackers, "fixture: nobody to march"
    before_a = {pid: w.persons[pid].body for pid in attackers}
    # `build_realm` seeds each person's loyalty as a pre-existing stance row (`data/cast.py`'s
    # `stance_from_loyalty`), so "no new row" is what this checks, not "an empty list".
    before_stance = {pid: list(w.persons[pid].stance or []) for pid in attackers}

    act = _march_act("p_npc_033", "set_s_003", "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("field.unopposed", "Unopposed") in kinds
    assert ("army.arrived", "Unopposed") in kinds

    assert world_q.mustered(w, "set_s_003", "fac_crown") == attackers, "the army did not arrive"
    assert world_q.mustered(w, "set_s_014", "fac_crown") == [], "the army is still at its origin"
    for pid in attackers:
        assert w.persons[pid].body == before_a[pid], f"{pid} took casualties in an unopposed march"
        assert list(w.persons[pid].stance or []) == before_stance[pid], (
            f"{pid} gained a stance row from an unopposed march")
        assert w.persons[pid].travel_leg[-1] == "set_s_003", "the journey's leg was not laid"
    # ONE LEG PER MOVER: the leg id keys on the mover (`_relocate`), so two claimants moved by one act
    # get two distinct edges, not one id minted twice.
    legs = [t.id for t in w.tenures
            if t.kind == "contain" and t.object == "set_s_003" and t.live and t.subject in attackers]
    assert len(attackers) >= 2 and len(legs) == len(attackers) == len(set(legs)), legs


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


def test_a_march_on_an_unheld_settlement_arrives_rather_than_crashing_the_season():
    """v9 IN-13 EXIT (v), RE-PINNED: `field.unopposed` + `army.arrived`. An unheld settlement has no
    opposing holder, so `sides_of` names `subject = None` and the provider answers `Unopposed`; the
    army ARRIVES at unheld land and no title is written (who holds an unheld place is unruled, H-166).
    The season still does not crash -- the original falsifier, below, kept.

    ORIGINAL (M4): FALSIFIER for the crash `valoria-critic` found in the adversarial pass on this build, not
    anticipated while writing it: `march` on a settlement Rung with no HELD ancestor sent
    `sides_of`'s `subject=None` into `mass_battle.py::resolve()`, which reports that shape as
    `status="PARTY-GAP"` -- and `seam/contest.py` raised an uncaught `Unspecified` for ANY
    non-RESOLVED status, crashing `encounter()` and the whole season. `loop/resolve.py::_contest`
    then caught `Unspecified(needs="PARTY-GAP")` around the `contest()` call and folded it as a
    graceful refusal, the same shape the empty-`_parties` check produces. ⚠ SINCE v9 IN-13 an unheld
    target no longer reaches that catch at all (`mass_battle.py` answers `subject = None`
    `Unopposed`); the catch stays for the other wrappers' missing parties.

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
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    act = _march_act("p_npc_033", "set_s_037", "off_npc_033")
    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    assert ("field.unopposed", "Unopposed") in kinds and ("army.arrived", "Unopposed") in kinds, (
        f"expected an unopposed arrival, got {kinds}")
    assert world_q.mustered(w, "set_s_037", "fac_crown") == attackers
    assert world_q.holder_faction_of(w, "set_s_037") is None, "an arrival wrote a title (H-166)"


def test_a_won_field_writes_casualties_and_stance_on_the_defender_only():
    """FALSIFIER for a real, verified gap: `Won` (the ATTACKER wins, defenders lose) had NO
    execution coverage anywhere in this build. `test_a_lost_field...` above only exercises `Lost`,
    and `modules/mass_battle/massbattle.py`'s own disclosed limitation -- corpus-scale forces
    (single/double-digit `weight` sums) rout on contact regardless of size, so `attacker_wins`
    (hence `Won`) may be UNREACHABLE through a real fold at this fixture's scale -- measured
    directly: the 6-attacker/2-defender REVERSE of the scenario below still resolved `Lost`.
    Rather than guess at a fixture combination the engine's own scale limitation may make
    impossible, this constructs the `Resolution` directly, the same technique
    `test_declared_is_no_change_and_unopposed_changes_only_with_claimants_in_the_resolution` uses for
    the other two bands --
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


def test_declared_is_no_change_and_unopposed_changes_only_with_claimants_in_the_resolution():
    """v9 IN-13 EXIT (v), RE-WRITTEN: `Declared` returns `NO_CHANGE`; `Unopposed` returns NO_CHANGE
    only when its `Resolution` carries no claimants -- the old test passed `Resolution("Unopposed",
    {})`, which still returns NO_CHANGE after the arrival and so would keep passing while observing
    nothing (§14.8). With the claimants in the `Resolution`, `Unopposed` names each of them, whole,
    and writes no casualty; a claimant already present under the destination makes no journey."""
    eff = EFFECTS["march"]
    w = build_realm(0)
    act = _march_act("p_npc_033", "set_s_003", "off_npc_033")
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    assert eff(w, act, Resolution("Declared", {})) is G.NO_CHANGE
    assert eff(w, act, Resolution("Unopposed", {})) is G.NO_CHANGE
    with_claimants = Resolution("Unopposed", {"parties": {"claimants": attackers, "subject_members": []},
                                              "result": {"attacker_size_pct": 1.0}})
    change = eff(w, act, with_claimants)
    assert change is not G.NO_CHANGE
    assert [s.id for s in change.subjects] == attackers
    assert all(s.ref[3] is None and s.earns is None for s in change.subjects), (
        "a mover is named whole and earns every kind the band declares")
    # CONTROL, one change (the destination is where the army already stands): no journey, no change.
    home = _march_act("p_npc_033", "set_s_014", "off_npc_033")
    assert eff(w, home, with_claimants) is G.NO_CHANGE


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


def test_a_real_chooser_forms_and_folds_a_march_that_reaches_a_real_field_battle():
    """PLAN POSITION `28-ii` (M6, SUCCESSOR GOLDENS) -- THE GATE THIS SESSION WAS BUILT TO CLOSE:
    *"a battle executing from a real, chooser-formed decision"* (the retirement plan's own §6,
    `CLAUDE.md` §0.1 pt 3 row 4 -- a claim that a mechanism works must show the run, not the code
    path). Every other test in this file hand-authors its `Act`, including its `payload` and its
    `via`. This one does neither -- CORRECTED per the BATCH-CLOSE Phase-1 antagonist: the first
    writing of this test built `payload` off a real `Candidate` but then hand-set
    `Act(..., via="off_npc_033")`, which is exactly the hand-built-`Act` shape the retirement
    plan's gate sought to rule OUT, not demonstrate. `via` is now read off the real chooser's own
    derivation and asserted as a computed fact.

    `p_npc_033` (Crown, `off_npc_033`, `remit:dispatch`) is asked a real `Question` whose referent
    is `set_s_036` (Church of Solmund) -- the SAME cross-faction pair `test_a_lost_field_...`
    above hand-builds, chosen here so the falsifier is comparable rather than novel. Clause 3's
    PRE-EXISTING `q.referents` reading -- no march-specific arm, nothing added -- is what carries
    that referent into a real `Candidate`; nothing here supplies `subject` by hand.
    ⚠ v10 REM-27 (B10-06): `march` now declares `referent_class: Rung`, so it forms ONLY on an id the
    question carries as `Rung` (`Question.classes`, the partition `questions_for` stamps from
    `places_named` / `larders_in_purview`), never on a plain referent. The constructed Question
    therefore carries the settlement as a `Rung` pair, `test_migrate_capacity.py`'s shape; the stamp
    itself is `test_referent_class_stamps.py::test_rem27_*`'s.
    """
    w = build_realm(0)
    p = w.persons["p_npc_033"]
    q = Question("q:28ii_chooser_march", "need", ("set_s_036",), classes=(("set_s_036", "Rung"),))
    v = View(p.id, [], w.fixtures.get("view_k"), q)

    cands = opening_set(p, v, q, w.fixtures)
    march_cands = {c.subject: c for c in cands if c.verb == "march"}
    # FALSIFIER: the referent-named settlement forms a march Candidate under clause 3's own
    # `q.referents` reading, unaided -- clause 3 applies no kind filter, so any Rung-kind referent
    # would do the same. What this assertion rules OUT is a missing `operands_for` arm for march,
    # which this Question (constructed, not corpus-drawn) was never short of.
    # ⚠ CORRECTED, Phase 3 terminal critique, 2026-09-30: this comment used to say WHY the
    # natural corpus's `questions_for` sources never hand a person a workable referent was
    # UNMEASURED, full stop -- measured FALSE for `build_realm(0)`/`populated.run`:
    # `python -m engine.season.harness.aperture 1 0` shows march naturally forming, being
    # offered, being attempted and executing there, unaided, via the real unrestricted chooser
    # (see the module docstring's new note above and `hole_register.yaml` H-175). What remains
    # unmeasured is narrower and different: WHY `corpus_run`'s separate 143-case NPC/ARC corpus
    # specifically never supplies march a workable referent, confirmed still absent there by a
    # fresh `corpus_run` run this same session.
    assert "set_s_036" in march_cands, (
        f"the referent-named settlement never became a march Candidate subject; got "
        f"{sorted(march_cands)}")
    c = march_cands["set_s_036"]
    assert c.operands == {"subject": "set_s_036", "to": "set_s_036"}, c.operands

    # THE REAL CHOOSER, THROUGH `make_chooser`/`pack_scenes` -- NOT A HAND-BUILT `Act`. Restricting
    # the chooser's own `verbs=` to `{"march"}` leaves exactly one ranked Candidate (this
    # Question's one referent), so the sampler's own `len(ranked) < 2` short-circuit
    # (`choose.py::_sample_order`) makes the pick deterministic without a seeded tie-break --
    # confirmed by the scene/act-count assertion below rather than assumed.
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    chooser = make_chooser(w.fixtures, mint, verbs=frozenset({"march"}),
                           draw=draw_factory(w.world_seed, lambda: w.tick))
    scenes = chooser(p, v, Sensation(0), lambda: 1)
    assert len(scenes) == 1 and len(scenes[0].acts) == 1, (
        f"expected exactly one scene holding exactly one march act, got {scenes}")
    act = scenes[0].acts[0]
    assert act.verb == "march" and act.payload == {"subject": "set_s_036", "to": "set_s_036"}, (
        act.verb, act.payload)
    # `via` IS READ OFF THE CHOOSER'S OWN DERIVATION, NOT HAND-SET (the antagonist's finding).
    # `pack_scenes` names it through `exercised_seat`, the SAME walk `person_side_eligible`
    # admitted march through -- the first live `hold` Tenure of `p_npc_033`'s that grants
    # `dispatch` (march's own `remit:dispatch` eligibility cell, `verb_table.yaml`), which this
    # fixture seats at `off_npc_033`.
    assert act.via == "off_npc_033", (
        f"expected march to exercise the dispatch-granting seat, got {act.via!r}")

    # `/simplify`, BATCH-CLOSE Phase 2: NO before/after casualty loop here (dropped). This
    # chooser-formed act is NOT byte-identical to what `_march_act("p_npc_033", "set_s_036",
    # "off_npc_033")` would build -- the payload carries an extra `to` key (`{"subject", "to"}`
    # vs. `{"subject"}`) and the id is chooser-minted, not the literal `"m1"` -- but it reaches
    # the SAME two-settlement (`set_s_014`/`set_s_036`) mismatch and the same `field.lost`
    # outcome kind that `test_a_lost_field_writes_casualties_and_stance_on_the_attacker_only`
    # (above) exercises on its own, differently-swept fixture (that test sets
    # `field_grudge_weight` to `3`; this one uses the default), so re-deriving the full body-drop
    # assertions here would repeat, not add, falsifying power. The one thing THIS test proves that
    # the sibling test cannot is that a chooser-formed act reaches a real fight at all.
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    defenders = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    assert len(attackers) == 2 and len(defenders) == 6, (
        f"the fixture no longer gives a 2-v-6 mismatch here ({attackers}, {defenders}); "
        "pick an origin/target pair that still does")

    events = _fold_one(w, act, contest_max_depth=2)
    kinds = [(e.kind, e.degree) for e in events]
    assert ("march.declared", "Declared") in kinds
    # THE FALSIFIER: a REAL field battle, not merely a formed-and-declared attempt. `Lost` is the
    # ATTACKER's own outcome (`seam/ladder.py::field_degree`) at this fixture's 2-v-6 mismatch.
    assert ("field.lost", "Lost") in kinds, (
        f"expected a real field battle (`field.lost`), got {kinds} -- the chooser-formed act "
        "never reached a fight")


def test_a_real_fold_reads_the_targets_fortification_on_the_battle_path(monkeypatch):
    """PLAN POSITION `20-iv` -- `H-150` closes only if `fortification_of` is READ ON THE BATTLE
    PATH, so this asserts the call, at runtime, through the real driver's RESOLVE -> ENCOUNTER
    fold rather than by grepping a declaration (CLAUDE.md §0.1 pt 3 row 2). The count wraps the
    real function, so the fight itself is unchanged; it is called with the march's own target, and
    the field is fought (`field.lost`), not short-circuited. Before `20-iv` the count was 0."""
    calls = []
    real = world_q.fortification_of

    def counting(w_, rung_id):
        calls.append(rung_id)
        return real(w_, rung_id)

    monkeypatch.setattr(world_q, "fortification_of", counting)
    w = build_realm(0)
    events = _fold_one(w, _march_act("p_npc_033", "set_s_036", "off_npc_033"), contest_max_depth=2)
    assert ("field.lost", "Lost") in [(e.kind, e.degree) for e in events], "no field was fought"
    assert calls == ["set_s_036"], f"fortification_of was called {calls!r} on the battle path"


# =====================================================================================================
# v9 IN-13 (#453 §10.4 step 8) -- THE ARRIVAL: `march` RESOLVES PRESENCE. Exits (i)-(vii), the gate's
# `muster` basis, and the re-homed regard falsifier (#457 CARRY-INTERIOR / #445 P-1, via IN-18 G1).
# Every world is `build_realm(0)` driven through the real fold; `Won` is unreachable at fixture scale
# (`test_a_won_field_...` above), so a `Won` is either a constructed `Resolution` written THROUGH THE
# GATE (exit (i)) or the real fold over a module entry patched to report the attacker winning (exit
# (vii), the regard falsifier's `field.won` arm) -- the seam, the ladder, the effect and the gate real.
# MUTATIONS, run at the build 2026-10-16 (each RED, then restored GREEN): recorded in the commit.
# =====================================================================================================

CROWN, CHURCH = "fac_crown", "fac_church_of_solmund"


def _patch_won(monkeypatch, defender_pct=0.5):
    """The mass-battle module entry, patched to report the ATTACKER winning: an opposed field whose
    survivors the engine reports, so `field_degree` grades `Won` and `_eff_march` reads a real band."""
    from engine.season.seam.wrappers import mass_battle as MB
    # `**_`: since v9 IN-52 the adapter also hands the entry each side's fielded troops
    # (`troops_a`/`troops_b`, the levy-to-field feed); this patched field does not read them.
    entry = SimpleNamespace(fn=lambda inp, rng, **_: dict(attacker_wins=True, degree="Success",
                                                      attacker_size_pct=1.0,
                                                      defender_size_pct=defender_pct))
    monkeypatch.setattr(MB, "entry_for", lambda prize, module: (entry, None))


def _resolve_one(w, act):
    """Fold ONE uncontested act (here, `seize`) through the real driver's RESOLVE, into `w.log`."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _seize_act(target, actor="p_npc_020", via="off_npc_020", act_id="z1"):
    return Act(id=act_id, actor=actor, verb="seize", payload={"subject": target}, via=via)


def _seize_kinds(w, target, **kw):
    """The kinds one `seize` on `target` folds to (`_seize_act`'s keywords pass through)."""
    return [e.kind for e in _resolve_one(w, _seize_act(target, **kw))]


def _occupy(w, town, actor, via, **kw):
    """March `actor`'s army (exercising `via`) onto `town` through the real fold, and assert it ARRIVED."""
    kinds = [e.kind for e in _fold_one(w, _march_act(actor, town, via, **kw))]
    assert "army.arrived" in kinds, kinds


def _no_resident_crown(w):
    """FIXTURE EDIT, NAMED: `build_realm(0)` houses ONE Crown member, `p_npc_037`, in the Church's
    cathedral at `set_s_036`, so the Crown is ALREADY `mustered` there before any march -- and by the
    occupation Query (#453: a faction other than the holder's mustered at a settlement it does not
    hold) the Church's seat is seizable by a Crown seat at seed 0, with no field fought. Measured at
    IN-13's build; it is the Query as ruled, not a defect this file fixes. The exits that need the
    Crown's presence at `set_s_036` to be the ARRIVAL's doing re-house him at `set_s_002` (Crown) first,
    outside any write, so the cause is controlled."""
    assert world_q.mustered(w, "set_s_036", CROWN) == ["p_npc_037"], "fixture moved: re-read it"
    for t in w.persons["p_npc_037"].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_in13_037_moved", "p_npc_037", "b_s_002_cottage", "contain", w.tick))
    assert world_q.mustered(w, "set_s_036", CROWN) == []
    return w


# ---- EXIT (i) -----------------------------------------------------------------------------------------

def test_in13_exit_i_won_through_the_gate_leaves_the_claimants_mustered_at_the_target():
    """EXIT (i), the `Won` arm: a CONSTRUCTED `Resolution` (Won is unreachable at fixture scale), its
    `Change` written through the real gate at ENCOUNTER -- so the `muster` basis, not a bare `apply()`,
    admits the claimants' legs. `mustered(w, set_s_036, fac_crown)` equals the claimants after it.
    (The `Unopposed` arm at `set_s_003` is `test_an_unopposed_march_arrives_...`, above.)"""
    w = _no_resident_crown(build_realm(0))
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    defenders = world_q.mustered(w, "set_s_036", CHURCH)
    assert world_q.mustered(w, "set_s_036", CROWN) == [], "fixture: the Crown already stands there"
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    res = Resolution("Won", {"parties": {"claimants": attackers, "subject_members": defenders},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.5}})
    w.step = Step.ENCOUNTER
    w.frozen = False
    got = w.write("body", mint_token(w, WriteClass.ACTS), None, record_kind="Person", fieldname="body",
                  driver="Act", actor=act.actor, via=act.via, change=EFFECTS["march"](w, act, res))
    assert got, "the gate minted no receipt"
    assert world_q.mustered(w, "set_s_036", CROWN) == attackers
    assert world_q.mustered(w, "set_s_014", CROWN) == []
    assert world_q.mustered(w, "set_s_036", CHURCH) == defenders, (
        "`scaled_by_degree` floors at 1: a won field removes no defender")


def test_in13_exit_i_a_won_whose_army_already_stands_there_fells_without_an_arrival():
    """EXIT (i), the `Won` arm with NOBODY TO MOVE: the claimants already stand under the target
    (`p_npc_037`, the Crown member housed in the cathedral at `set_s_036`), so the band moves no one and
    the losers (the defenders) are touched -- `field.won` is published and `army.arrived` is NOT (a band
    that moved nobody earns its own kind alone, `_eff_march`'s `loser_earns`). A CONSTRUCTED `Resolution`
    through the real fold (`Won` is unreachable at fixture scale), the gate real."""
    w = build_realm(0)
    claimants = ["p_npc_037"]
    assert world_q.mustered(w, "set_s_036", CROWN) == claimants, "fixture moved: re-read it"
    defenders = world_q.mustered(w, "set_s_036", CHURCH)
    before = {pid: w.persons[pid].body for pid in defenders}
    res = Resolution("Won", {"parties": {"claimants": claimants, "subject_members": defenders},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.5}})
    d = SeasonDriver(w)
    w.step = Step.ENCOUNTER
    w.frozen = False
    kinds = [(e.kind, e.degree) for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                                 _march_act("p_npc_033", "set_s_036", "off_npc_033"), res)]
    assert ("field.won", "Won") in kinds, kinds
    assert not any(k == "army.arrived" for k, _ in kinds), kinds
    assert any(w.persons[pid].body < before[pid] for pid in defenders), "no defender was touched"
    assert world_q.mustered(w, "set_s_036", CROWN) == claimants


def _won_fold(w, claimants):
    """A CONSTRUCTED `Won` over `claimants` folded through the real driver at ENCOUNTER -- the
    effect, the fold and the gate real (`Won` is unreachable at fixture scale)."""
    defenders = world_q.mustered(w, "set_s_036", CHURCH)
    res = Resolution("Won", {"parties": {"claimants": claimants, "subject_members": defenders},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.5}})
    d = SeasonDriver(w)
    w.step = Step.ENCOUNTER
    w.frozen = False
    return [(e.kind, e.degree) for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                                _march_act("p_npc_033", "set_s_036", "off_npc_033"), res)]


def test_in13_exit_i_a_won_never_moves_a_claimant_the_muster_basis_would_refuse():
    """EXIT (i), the gate's own question asked INSIDE the effect (`_eff_seize`'s precedent: an act the
    precondition admitted is never killed at the gate). Two arms, each through the real fold, each a
    `NotYours` that escaped `_fold` and ended the season before `_eff_march` asked `may_muster`:
      * a claimant the seat may NOT muster (committed to another faction): he stays where he is and
        the rest of the army arrives. (A closed marcher `hold` is NOT this arm: `_admits` refuses the
        ineligible marcher before the effect runs, `march.refused`, so no `NotYours` is reachable
        there.)
      * a claimant with NO HOME (no live `contain`): the gate admits only a re-home, a closure AND an
        opening, so he has nothing to close and stays where he is.
    CONTROL (no mutation of the world): the same two claimants, both housed and the hold live, BOTH
    arrive (exit (i) above)."""
    # a claimant the seat may not muster (someone uncommitted to the Crown, in its army)
    w = _no_resident_crown(build_realm(0))
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    assert attackers == ["p_npc_033", "p_npc_035"], "fixture moved: re-read it"
    outsider = "p_npc_001"      # housed elsewhere (a claimant already under the target is no mover)
    assert not G.may_muster(w, "p_npc_033", "off_npc_033", outsider)
    assert "set_s_036" not in world_q.ancestry(w, world_q.home_of(w)[outsider]), "fixture moved"
    kinds = _won_fold(w, attackers + [outsider])
    assert ("field.won", "Won") in kinds and ("army.arrived", "Won") in kinds, kinds
    assert world_q.mustered(w, "set_s_036", CROWN) == attackers
    assert "set_s_036" not in world_q.ancestry(w, world_q.home_of(w)[outsider]), "he was moved"
    # a claimant with no home
    w = _no_resident_crown(build_realm(0))
    for t in w.persons["p_npc_035"].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    assert world_q.mustered(w, "set_s_014", CROWN) == ["p_npc_033"]
    kinds = _won_fold(w, attackers)
    assert ("field.won", "Won") in kinds and ("army.arrived", "Won") in kinds, kinds
    assert world_q.mustered(w, "set_s_036", CROWN) == ["p_npc_033"]
    assert "set_s_036" not in world_q.ancestry(w, world_q.home_of(w).get("p_npc_035")), "he arrived"
    # CONTROL: nothing planted, both arrive
    w = _no_resident_crown(build_realm(0))
    _won_fold(w, attackers)
    assert world_q.mustered(w, "set_s_036", CROWN) == attackers


def test_in13_exit_i_lost_leaves_the_claimants_at_their_origin_r7():
    """EXIT (i), the `Lost` arm, PINNING #453 R-7 [ASSUMPTION; medium; Jordan to correct; revert:
    Jordan states that a routed army arrives, and this arm is re-pinned]: a real `field.lost` at
    `set_s_036` leaves `mustered(w, set_s_014, fac_crown)` equal to the claimants, and nobody arrives."""
    w = _no_resident_crown(build_realm(0))
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    events = _fold_one(w, _march_act("p_npc_033", "set_s_036", "off_npc_033"))
    kinds = [e.kind for e in events]
    assert "field.lost" in kinds and "army.arrived" not in kinds, kinds
    assert world_q.mustered(w, "set_s_014", CROWN) == attackers
    assert world_q.mustered(w, "set_s_036", CROWN) == []


# ---- EXIT (ii) -- H-151's own falsifier ---------------------------------------------------------------

def test_in13_exit_ii_h151_a_march_on_ones_own_occupied_settlement_is_unopposed():
    """H-151's FALSIFIER (`hole_register.yaml`, its `cite:`), EXPECTED OUTCOME `field.unopposed`: a
    constructed `Question` naming `set_s_001`, held by the actor's OWN faction with that faction's people
    present (at least two Crown) as its only defenders; the march is formed and packed by the REAL chooser and
    folded -- and it fights nobody: `field.unopposed`, the army arrives, and the Crown already there is
    untouched. Before IN-13 it fought the faction against itself. Since v10 REM-27 the settlement rides
    as a `Rung` pair (`march`'s `referent_class`; the plain referent alone no longer forms it)."""
    w = build_realm(0)
    present = world_q.mustered(w, "set_s_001", CROWN)
    assert world_q.holder_faction_of(w, "set_s_001") == CROWN and len(present) >= 2, present
    p = w.persons["p_npc_033"]
    q = Question("q:in13_h151", "need", ("set_s_001",), classes=(("set_s_001", "Rung"),))
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    chooser = make_chooser(w.fixtures, mint, verbs=frozenset({"march"}),
                           draw=draw_factory(w.world_seed, lambda: w.tick))
    scenes = chooser(p, View(p.id, [], w.fixtures.get("view_k"), q), Sensation(0), lambda: 1)
    (act,) = [a for s in scenes for a in s.acts]
    assert act.payload["subject"] == "set_s_001" and act.via == "off_npc_033"
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    before = {pid: (w.persons[pid].body, list(w.persons[pid].stance or [])) for pid in present}
    kinds = [(e.kind, e.degree) for e in _fold_one(w, act)]
    assert ("field.unopposed", "Unopposed") in kinds, kinds
    assert not any(k in ("field.won", "field.lost") for k, _ in kinds), kinds
    assert set(attackers) <= set(world_q.mustered(w, "set_s_001", CROWN))
    for pid in present:
        assert (w.persons[pid].body, list(w.persons[pid].stance or [])) == before[pid], (
            f"{pid}, of the marcher's own faction, was written as a defender")


# ---- EXIT (iii) -- interception -------------------------------------------------------------------------

def test_in13_exit_iii_an_arrived_army_intercepts_a_later_march():
    """EXIT (iii): the Crown relocates to Crown-held `set_s_003` in one `_fold_one` (`Unopposed`,
    arrives); a Church march on it in a second meets that army -- `Won` or `Lost`, not `Unopposed`.
    CONTROL, one change (no first fold): the same Church march on the empty `set_s_003` is
    `Unopposed`, so the interception is the arrival's doing."""
    church = _march_act("p_npc_013", "set_s_003", "off_npc_013", act_id="m_church")
    ctrl = build_realm(0)
    ctrl_kinds = [e.kind for e in _fold_one(ctrl, church)]
    assert "field.unopposed" in ctrl_kinds, ctrl_kinds
    w = build_realm(0)
    first = [e.kind for e in _fold_one(w, _march_act("p_npc_033", "set_s_003", "off_npc_033"))]
    assert "army.arrived" in first, first
    assert world_q.mustered(w, "set_s_003", CROWN), "nobody stands at set_s_003 after the arrival"
    second = [(e.kind, e.degree) for e in _fold_one(w, church)]
    assert any(d in ("Won", "Lost") for _k, d in second), second
    assert not any(d == "Unopposed" for _k, d in second), second


# ---- EXIT (iv) is `test_a_march_on_a_non_settlement_rung_refuses_h149_is_enforced`, above, unchanged ---

# ---- the gate's `muster` basis ---------------------------------------------------------------------------

def _rehome(w, actor, via, pid, dest):
    """A bare gate write that re-homes `pid` to `dest` (`_relocate`'s pair), nothing else asked."""
    from engine.season.loop.effects_migration import _relocate
    act = _march_act(actor, dest, via, act_id="g1")
    w.step = Step.ENCOUNTER
    w.frozen = False
    return w.write("travel_leg", mint_token(w, WriteClass.ACTS), None, record_kind="Person",
                   fieldname="travel_leg", driver="Act", actor=actor, via=via,
                   change=G.Change((G.Subject.entity("persons", pid),),
                                   lambda: _relocate(w, act, dest, mover=pid)))


def test_in13_the_muster_basis_admits_a_member_and_refuses_everyone_else():
    """THE GATE, PLANTED AROUND THE EFFECT: a seat granted `dispatch` re-homes a member of its own
    faction (`muster`), and each one-change control is `NotYours` with the store put back -- a
    non-member, a seat with no `dispatch` grant, and no seat at all."""
    w = build_realm(0)
    assert G.may_muster(w, "p_npc_033", "off_npc_033", "p_npc_035")
    _rehome(w, "p_npc_033", "off_npc_033", "p_npc_035", "set_s_003")
    assert world_q.mustered(w, "set_s_003", CROWN) == ["p_npc_035"]
    # CONTROL for the "no `dispatch` grant" row below: `p_npc_036` is committed to the very faction
    # `off_npc_008` belongs to, so the grant is the ONLY thing that row changes (actor, seat and subject
    # move together, and would otherwise confound it with a faction mismatch).
    assert (world_q.faction_holding(w, "p_npc_036")
            == faction_prop_id(w.offices["off_npc_008"].faction) == CROWN)
    checked = 0
    for actor, via, pid, why in (("p_npc_033", "off_npc_033", "p_npc_013", "not a Crown member"),
                                 ("p_npc_008", "off_npc_008", "p_npc_036", "no `dispatch` grant"),
                                 ("p_npc_033", None, "p_npc_036", "no seat exercised")):
        before = world_q.home_of(w).get(pid)
        try:
            _rehome(w, actor, via, pid, "set_s_003")
        except G.NotYours:
            checked += 1
        else:
            raise AssertionError(f"re-homed {pid} with {why}")
        assert world_q.home_of(w).get(pid) == before, f"the store was not put back ({why})"
    assert checked == 3

    # The basis admits a RE-HOME and no other shape of `contain` write by the same seat for the same
    # member (`rehomed`: at least one closure and exactly one opening). Each is the muster-licensed
    # actor, seat and subject of the admitting row above, one change: (a) a PURE CLOSURE (an eviction
    # with no destination), (b) an OPENING with no closure beside it (a presence with nothing re-homed).
    def _gate_contain(pid, perform):
        w.step = Step.ENCOUNTER
        w.frozen = False
        return w.write("travel_leg", mint_token(w, WriteClass.ACTS), None, record_kind="Person",
                       fieldname="travel_leg", driver="Act", actor="p_npc_033", via="off_npc_033",
                       change=G.Change((G.Subject.entity("persons", pid),), perform))

    def _close(pid):
        for t in w.tenures:
            if t.subject == pid and t.kind == "contain" and t.live:
                t.until = w.tick

    pid = "p_npc_035"
    assert G.may_muster(w, "p_npc_033", "off_npc_033", pid)
    before = [(t.id, t.until) for t in w.tenures if t.subject == pid and t.kind == "contain"]
    try:
        _gate_contain(pid, lambda: _close(pid))
    except G.NotYours:
        pass
    else:
        raise AssertionError("a pure closure of a member's `contain` was admitted as a muster")
    assert [(t.id, t.until) for t in w.tenures if t.subject == pid and t.kind == "contain"] == before, (
        "the refused closure was not put back")
    _close(pid)                              # outside any write: the member now has NO live presence
    live_before = [t.id for t in w.tenures if t.subject == pid and t.kind == "contain"]
    try:
        _gate_contain(pid, lambda: w.add_tenure(Tenure("t_in13_open_only", pid, "set_s_003", "contain",
                                                       w.tick)))
    except G.NotYours:
        pass
    else:
        raise AssertionError("an opening with no closure was admitted as a muster")
    assert [t.id for t in w.tenures if t.subject == pid and t.kind == "contain"] == live_before, (
        "the refused opening was not put back")


# ---- EXITS (vi), (vii) -- `seize` widened to a Rung, licensed by occupation ---------------------------

def test_in13_exit_vi_seize_on_an_occupied_settlement_flips_its_holder():
    """EXIT (vi): the Crown marches on Hafenmark-held `set_s_016`, which no Hafenmark member defends
    (`Unopposed`: a capture, occupation); a Crown seat granted `issue` whose purview reaches it
    (`off_npc_020`, the realm) then seizes it -- `rung.seized`, and `holder_faction_of` reads the
    Crown there, the territory above untouched. CONTROL, one change (no march, so no occupation): the
    same seizure is refused and the holder stays."""
    ctrl = build_realm(0)
    assert world_q.holder_faction_of(ctrl, "set_s_016") == "fac_hafenmark"
    assert _seize_kinds(ctrl, "set_s_016") == ["seize.refused"]
    assert world_q.holder_faction_of(ctrl, "set_s_016") == "fac_hafenmark"

    w = build_realm(0)
    _occupy(w, "set_s_016", "p_npc_033", "off_npc_033")
    assert world_q.holder_faction_of(w, "set_s_016") == "fac_hafenmark", "an arrival wrote a title (R-6)"
    # CONTROLS, each one change from the admitted seizure below (the Crown stands at the same place,
    # the same seat and actor), each pinning an arm of `_seize_rung`'s decline: the territory above the
    # occupied town (the Crown is mustered under it too, and Hafenmark holds it -- since ED-IN-0306 phase 4 a
    # territory is a march target, so only OCCUPATION refuses: standing in a town is not standing at its territory), and a Crown-held town of the seizer's own faction (nothing to take). Each is refused at
    # the `write` clause and moves no title.
    assert world_q.mustered(w, "terr_T7", CROWN), "fixture: the Crown stands under the territory"
    assert w.rungs["terr_T7"].kind == "territory"
    assert world_q.holder_faction_of(w, "set_s_002") == CROWN
    for refused in ("terr_T7", "set_s_002"):
        assert _seize_kinds(w, refused, act_id=f"zc_{refused}") == ["seize.refused"], refused
    assert world_q.holder_faction_of(w, "terr_T7") == "fac_hafenmark", "the territory changed hands"
    assert world_q.holder_faction_of(w, "set_s_002") == CROWN
    out = _resolve_one(w, _seize_act("set_s_016"))
    assert [e.kind for e in out] == ["rung.seized"], [e.kind for e in out]
    assert world_q.holder_faction_of(w, "set_s_016") == CROWN
    assert world_q.hold_force(w, "set_s_016").subject == "p_npc_020"
    assert world_q.holder_faction_of(w, "terr_T7") == "fac_hafenmark", "the territory changed hands"


def test_in13_exit_vi_control_an_occupied_unheld_settlement_is_nobodys_to_seize():
    """EXIT (vi)'s third decline (`holder is None`: H-166, who holds an unheld place is unruled), asked of
    the EFFECT: at seed 0 no seat's purview reaches `set_s_037`, so the fold refuses the act earlier
    (`seize.unauthorized`, the `authority` conjunct) and the arm is unobservable through it. The Crown
    marches on and occupies it (`army.arrived`, `mustered` there), the effect declines (`NO_CHANGE`);
    CONTROL, one change (the town is Hafenmark-held, `set_s_016`, occupied the same way): the same
    effect, actor and seat returns a `Change`, so the decline is the unheld arm's and not the occupation's."""
    unheld, held = build_realm(0), build_realm(0)
    assert world_q.holder_faction_of(unheld, "set_s_037") is None
    for w, town in ((unheld, "set_s_037"), (held, "set_s_016")):
        _occupy(w, town, "p_npc_033", "off_npc_033")
        assert world_q.mustered(w, town, CROWN), "the Crown does not stand there"
    assert EFFECTS["seize"](held, _seize_act("set_s_016")) is not G.NO_CHANGE
    assert EFFECTS["seize"](unheld, _seize_act("set_s_037")) is G.NO_CHANGE


def test_in13_exit_vi_control_a_seat_holder_committed_to_another_faction_takes_nothing():
    """`_seize_rung`'s fourth decline [ASSUMPTION; medium]: the title it writes is the ACTOR'S OWN hold,
    read back as `faction_holding(actor)`. `p_npc_020` sits in the Crown seat `off_npc_020` and the Crown
    occupies `set_s_016` (exit (vi)'s path), but his `commit` is moved to Hafenmark: the effect declines
    and the act is refused with the holder unmoved. CONTROL, one change (his commit left on the Crown):
    the same act is `rung.seized`."""
    def occupied(commit_to):
        w = build_realm(0)
        _occupy(w, "set_s_016", "p_npc_033", "off_npc_033")
        if commit_to != CROWN:
            for t in w.persons["p_npc_020"].tenures:
                if t.kind == "commit" and t.object == CROWN and t.live:
                    t.until = w.tick
            w.add_tenure(Tenure("t_in13_020_commit", "p_npc_020", commit_to, "commit", w.tick))
        assert world_q.faction_holding(w, "p_npc_020") == commit_to
        assert w.offices["off_npc_020"].faction == "Crown" and G.may_seize(
            w, "p_npc_020", "off_npc_020", "p_npc_050", "set_s_016")
        return w
    w = occupied("fac_hafenmark")
    assert _seize_kinds(w, "set_s_016") == ["seize.refused"]
    assert world_q.holder_faction_of(w, "set_s_016") == "fac_hafenmark"
    w = occupied(CROWN)
    assert _seize_kinds(w, "set_s_016") == ["rung.seized"]


def test_in13_a_retaking_closes_the_seizers_hold_under_the_seizure_basis(monkeypatch):
    """THE CLOSURE HALF OF THE RUNG SEIZURE (the gate's `seizure` clause widened to a Rung): after the
    Crown occupies and seizes `set_s_016` (exit (vi)'s path), Hafenmark marches back (`p_npc_050`, the
    module entry patched to a `Won`: the Crown army there is opposed and stays, `scaled_by_degree`),
    and its seat `off_npc_050` (granted `issue`, purview over its duchy) seizes the town again: the
    Crown seizer's `hold` CLOSES under `seizure` -- not `T-m`, he is not the actor -- and Hafenmark's
    opens. One live `hold` on the settlement after."""
    w = build_realm(0)
    _fold_one(w, _march_act("p_npc_033", "set_s_016", "off_npc_033"))
    assert _seize_kinds(w, "set_s_016") == ["rung.seized"]
    first = world_q.hold_force(w, "set_s_016")
    _patch_won(monkeypatch)
    _occupy(w, "set_s_016", "p_npc_050", "off_npc_050", act_id="m_back")
    bases = []
    real = G.tenure_write_basis

    def spy(*args, **kw):
        out = real(*args, **kw)
        bases.append((args[1].subject, args[2] is None, out))
        return out
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    out = _resolve_one(w, _seize_act("set_s_016", actor="p_npc_050", via="off_npc_050", act_id="z2"))
    assert [e.kind for e in out] == ["rung.seized"], [e.kind for e in out]
    assert ("p_npc_020", False, G.SEIZURE) in bases, bases
    assert not first.live and world_q.hold_force(w, "set_s_016").subject == "p_npc_050"
    assert world_q.holder_faction_of(w, "set_s_016") == "fac_hafenmark"


def test_in13_exit_vii_an_opposed_won_removes_no_defender_and_the_seizure_is_admitted(monkeypatch):
    """EXIT (vii): an OPPOSED `Won` at `set_s_036` at the shipped `scaled_by_degree` model (the
    module entry patched to report the attacker winning), which removes no defender -- the Church is
    still mustered there -- then `seize` on it: ADMITTED, since the licence asks only that the seat's
    faction be mustered there. CONTROL, one change (a `Lost` instead, unpatched): the army stays home,
    and the same seizure is refused."""
    assert build_realm(0).fixtures.get("field_casualty_model") == "scaled_by_degree"
    ctrl = _no_resident_crown(build_realm(0))
    lost = [e.kind for e in _fold_one(ctrl, _march_act("p_npc_033", "set_s_036", "off_npc_033"))]
    assert "field.lost" in lost, lost
    assert _seize_kinds(ctrl, "set_s_036") == ["seize.refused"]

    _patch_won(monkeypatch)
    w = _no_resident_crown(build_realm(0))
    defenders = world_q.mustered(w, "set_s_036", CHURCH)
    kinds = [(e.kind, e.degree)
             for e in _fold_one(w, _march_act("p_npc_033", "set_s_036", "off_npc_033"))]
    assert ("field.won", "Won") in kinds and ("army.arrived", "Won") in kinds, kinds
    assert world_q.mustered(w, "set_s_036", CHURCH) == defenders, "a won field removed a defender"
    assert _seize_kinds(w, "set_s_036") == ["rung.seized"]
    assert world_q.holder_faction_of(w, "set_s_036") == CROWN


def test_in13_h212_a_resident_occupies_the_church_seat_at_seed_0_with_no_field_fought():
    """H-212's cite, EXECUTED rather than inspected: on an UNMODIFIED `build_realm(0)` (no
    `_no_resident_crown` edit) the Crown is already `mustered` at the Church's `set_s_036` through its
    resident `p_npc_037`, so the Crown seat granted `issue` whose purview reaches the town (`off_npc_020`,
    the realm) seizes it with no march and no field. CONTROL, one change (the resident re-housed away, the
    fixture edit the exits above use): the same act is refused."""
    w = build_realm(0)
    assert world_q.mustered(w, "set_s_036", CROWN) == ["p_npc_037"]
    assert world_q.holder_faction_of(w, "set_s_036") == CHURCH
    ctrl = _no_resident_crown(build_realm(0))
    assert _seize_kinds(ctrl, "set_s_036") == ["seize.refused"]
    assert _seize_kinds(w, "set_s_036") == ["rung.seized"]
    assert world_q.holder_faction_of(w, "set_s_036") == CROWN


# ---- THE RE-HOMED REGARD FALSIFIER (#457 CARRY-INTERIOR `:161`, #445 P-1; IN-18 G1) ------------------

def _leaning_pursuit(kind):
    from engine.season.data.pursuits import to_axes
    from engine.season.data.rosters import PURSUITS
    for e in sorted(PURSUITS):
        if PQ._lean(to_axes({e: 1.0}), kind):
            return e
    raise AssertionError(f"no pursuit leans on {kind!r}: the falsifier would be vacuous")


def _plant_witness(w, kind, where):
    """A person who does NOT fight: committed to no faction (so never mustered on either side), no
    stance toward anyone, pursuits leaning on `kind`, standing in `where` -- the field's place."""
    pid = "p_in13_witness"
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")
    w.add_tenure(Tenure("t_in13_w_in", pid, where, "contain", 0))
    w.add_tenure(Tenure("t_in13_w_home", pid, where, world_q.RESIDE_KIND, 0))
    w.persons[pid].pursuits = {_leaning_pursuit(kind): 1.0}
    return pid


def _witnessed_field(monkeypatch, won):
    """A march by `p_npc_033` on `set_s_036`, folded and WITNESSED by the real driver; the witness
    stands where the marcher is after the field (his origin building on a loss; on a win the
    settlement rung itself, where the arrival puts the army -- co-location is an exact-place test,
    `epistemic._ch_co_located`)."""
    if won:
        _patch_won(monkeypatch)
    kind, where = ("field.won", "set_s_036") if won else ("field.lost", "b_s_014_barracks")
    w = build_realm(0)
    wid = _plant_witness(w, kind, where)
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    act = _march_act("p_npc_033", "set_s_036", "off_npc_033")
    evs = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
    evs = evs + d.encounter(mint_token(w, WriteClass.ACTS), evs, 2)
    assert kind in [e.kind for e in evs], [e.kind for e in evs]
    w.log.extend(evs)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), evs)
    return w, w.persons[wid], kind


def _regard_falsifier(monkeypatch, won):
    w, wit, kind = _witnessed_field(monkeypatch, won)
    fx = w.fixtures
    jg = float(fx.get("judged_gain"))
    assert jg > 0, "the shipped judged gain is the treatment; 0 is the control"
    # Every firsthand DEED claim about the marcher -- the band's kind, and on `Won` the arrival beside
    # it (`army.arrived` is a deed of the same act) -- and the band's own among them.
    deeds = [c for c in wit.ledger if PQ.is_deed(c) and c.subject == "p_npc_033" and c.firsthand]
    assert any(c.predicate == kind for c in deeds), (
        f"the witness holds no firsthand {kind} deed about the marcher: "
        f"{[(c.subject, c.predicate) for c in wit.ledger]}")
    assert PQ.stance_toward(wit, "p_npc_033") == 0.0, "a stored stance would confound the reading"
    regard = PQ.regard(wit, "p_npc_033", fx)
    # THE DEED IS THE CAUSE: the regard moved by exactly judged_gain x the deeds' valence, and with
    # those claims taken out of the ledger it is the stored half again.
    judged, _told = PQ.deeds_judged(wit, "p_npc_033", fx.get("scar_weight_shift"))
    assert judged != 0.0 and regard == jg * judged, (regard, judged)
    kept = list(wit.ledger)
    wit.ledger = [c for c in kept if c not in deeds]
    assert PQ.regard(wit, "p_npc_033", fx) == 0.0, "something besides the deed moved the regard"
    wit.ledger = kept
    # CONTROL, weight 0 (#457 `:161`): the judged gain at 0 reads the stored half exactly.
    assert PQ.regard(wit, "p_npc_033", fx.sweep("judged_gain", 0)) == 0.0


def test_in13_regard_a_witness_who_did_not_fight_reads_a_lost_field_on_the_marcher(monkeypatch):
    """THE RE-HOMED FALSIFIER, `field.lost` arm: after a lost field, a witness who did not fight (in no
    side's army, no stance) reads a CHANGED regard at read toward the side the deed names -- G1 judges a
    deed for its DOER, the claim's subject, so a `field.lost` moves regard toward the MARCHER, who lost
    -- and the change is the deed's alone; weight 0 (`judged_gain`) is the control."""
    _regard_falsifier(monkeypatch, won=False)


def test_in13_regard_a_witness_reads_a_won_field_on_the_winning_side(monkeypatch):
    """The same falsifier on `field.won` (the DEFENDERS' lost field): the marcher is now the WINNING
    side, and the witness at the field reads a changed regard toward him."""
    _regard_falsifier(monkeypatch, won=True)
