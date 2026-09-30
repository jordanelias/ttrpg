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

from engine.season.data.matrix import Step, WriteClass
from engine.season.decision.choose import make_chooser
from engine.season.decision.options import opening_set
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop.effects import EFFECTS
from engine.season.queries import world_q
from engine.season.seam.contest import Resolution
from engine.season.state.carriers import Act, Question, Sensation, View
from engine.season.state.gate import NO_CHANGE
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
    """
    w = build_realm(0)
    p = w.persons["p_npc_033"]
    q = Question("q:28ii_chooser_march", "need", ("set_s_036",))
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
