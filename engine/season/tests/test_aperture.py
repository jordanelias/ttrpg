"""Plan position `★` -- THE APERTURE RE-MEASUREMENT. `harness/aperture.py` is the populated-realm
formability-and-execution instrument the plan names as the gate's first step (*"the instrument does
not exist ... it is this gate's first step, not a separate position"*).

⚠ THESE TESTS PIN THE INSTRUMENT, NEVER ITS NUMBERS. What a populated season forms and executes is
the measurement, and it moves every time the game does; pinning it would be a golden nobody has
argued is correct (`CLAUDE.md` §0.1 pt 5, and `harness/populated.py`'s own *"THIS TABLE IS THE
BASELINE, NOT A REGRESSION CHECK"*). What is pinned is what makes the numbers mean anything:

  * THE CONTROL -- the measured arm ends in the same `content_hash()` and act count as
    `populated.run`, the owner, on a second world from the same seed. So the chooser/barrier
    watching observed the season without moving it, and the figures ARE `harness.populated 1`'s.
    `World.content_hash` folds every state collection and the log (`H-118`), which is what lets
    this equality observe a perturbation rather than merely the act count;
  * THE COUNTERFACTUAL IS HONEST -- re-aggregating a person's delivered questions under the shipped
    rule reproduces the question the real chooser received, at every deliberation, so the other
    rules' rows differ from it by the rule alone;
  * THE FUNNEL IS CLOSED -- no act reaches the fold for a verb the chooser never offered that
    person, so `attempted` is a subset of what this instrument watched being offered;
  * TWO READINGS OF "SEATED" AGREE -- `aperture.seats` against the builder's own `_office_census`.

REM-10 (`corpus_run.attempts`, the ATTEMPT census). The funnel's `attempted`/`executed`/`refused` read
the ACT STORE (`w.acts`), which holds a contested act refused at admission that `SeasonDriver.resolved`
never does. Hand-built worlds (`probes.tiny_world`), no count of a realm run asserted:
  * AN ADMISSION-REFUSED `speak` AND AN UNCONTESTED REFUSED `transfer` are both attempted and refused;
    the `speak` is NOT in the fold set, which is what makes the first assertion able to fail;
  * `attribute` and `attempts` agree on every act the fold set holds;
  * `unrowed_acts` counts a verb that is no table row; `foreign_kinds` a logged kind outside both
    columns of the act's row;
  * `graded_loss` (HR-8): a lost `tell` (`news.untold`, `Failure`) and a `Failure` `research`
    (`finding.none`) are graded losses; an admission-refused `research` (`finding.none`, degree
    `None`), a Success `tell` and a refused `transfer` are not; every graded loss is also a `both` act.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from ..data.matrix import Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..harness import aperture as A
from ..harness import governance_spine, populated
from ..harness import probes as P
from ..harness.corpus_run import (_attribute_acts, attempts, attribute, foreign_kinds,
                                  graded_loss, graded_losses, unrowed_acts)
from ..loop.driver import SeasonDriver, mint_token
from ..seam import Resolution
from ..state.carriers import Act, Claim, Said
from .test_fi01_graded_inquiries import ACTOR as FI_ACTOR
from .test_fi01_graded_inquiries import REC as FI_REC
from .test_fi01_graded_inquiries import _resolve as _fi_resolve
from .test_fi01_graded_inquiries import _world as _fi_world
from .test_u7_remit import _fold, _world


@pytest.fixture(scope="module")
def realm():
    return A.measure_world(populated.build_realm, 0, 1)


def test_aperture_the_measured_season_is_the_populated_season(realm):
    c = realm["control"]
    assert c["acts"] == realm["acts"], (
        f"populated.run resolved {c['acts']} acts and the instrumented season {realm['acts']}: the "
        "two arms are different experiments, so nothing the instrument reports is the populated "
        "season's. Check that `instrumented_season` still builds its driver and chooser exactly as "
        "`populated.run` does")
    assert c["hash"] == realm["hash"], (
        "the instrumented season ended in a different world than `populated.run` on the same seed "
        "-- the watching PERTURBED the run. `opening_set`/`assemble`/`aggregate_questions` must stay "
        "pure for this instrument to exist")


def test_aperture_the_counterfactual_rules_reproduce_the_real_call(realm):
    assert realm["per_rule"], "no deliberation was recorded -- the chooser wrapper never ran"
    n = {len(rows) for rows in realm["per_rule"].values()}
    assert len(n) == 1, f"the aggregation rules saw different deliberation counts: {n}"
    assert realm["rule_mismatch"] == 0, (
        f"{realm['rule_mismatch']} deliberation(s) where re-aggregating the delivered questions under "
        f"the shipped rule ({realm['shipped_rule']!r}) did not give the question the chooser "
        "received. The other rules' rows then differ by more than the rule")


def test_aperture_no_act_enters_the_fold_unoffered(realm):
    stray = sorted((pid, v) for pid, c in realm["attempted"].items() for v in c
                   if v not in realm["formed"].get(pid, ()) or v not in realm["foldable"])
    assert realm["attempted"], "no act was attributed -- `corpus_run.attribute` saw nothing"
    assert not stray, (
        f"acts reached the fold for verbs the chooser never offered their actor: {stray[:5]}. An "
        "act is entering by a route this instrument does not watch, so its funnel undercounts "
        "`formed`/`offered`; watch that route before reading the per-holder table")


def test_aperture_seats_agrees_with_the_builders_own_census():
    """SEATS, not persons: `build_realm` seats NPC-020 twice since `13d-iii` (the King and the Duke
    of Valorsmark), so the per-holder table has fewer keys than the census has seats -- the SUM of
    its lists is what must equal `seated`."""
    w = populated.build_realm(0)
    table = A.seats(w)
    seats = sum(len(offs) for offs in table.values())
    assert seats == w._office_census["seated"], (
        f"`aperture.seats` finds {seats} seats over {len(table)} persons and `build_realm` seated "
        f"{w._office_census['seated']}")
    assert len(table) < seats, "no person holds two seats: the sum and the key count are not told apart"


def test_aperture_the_spine_gives_the_per_holder_table_its_population():
    """`workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3.8b: *"13 holders at 7
    distinct depths in one world, so 're-take it per holder' has a population rather than an
    anecdote"*. Asserted through the instrument's own readers, so a spine that stops seating or a
    `seat_depth` that stops walking shows here rather than as a short table."""
    m = A.measure_world(governance_spine.build, 0, 1)
    assert m["control"]["hash"] == m["hash"], "the instrument perturbed the spine season"
    assert len(m["seats"]) == len(governance_spine.spec()) == len(m["persons"]), (
        f"{len(m['seats'])} seated of {len(m['persons'])} persons over "
        f"{len(governance_spine.spec())} declared rungs -- every spine rung seats one holder")
    depths = [m["depth"][o] for offs in m["seats"].values() for o in offs]
    assert None not in depths, "a spine seat has no rung, so the table cannot say how deep it sits"
    # Every depth from the root down is populated: the table has a holder at each level, which is
    # the property the per-holder re-take needs. The COUNT of levels is the spine test's to pin.
    assert sorted(set(depths)) == list(range(max(depths) + 1)), sorted(set(depths))
    assert any(A.seat_gated(r) for r in VERB_TABLE.values()), (
        "no verb-table row is seat-gated; `seat_gated` parses nothing, so the per-holder funnel "
        "has no columns")


# ---------------------------------------------------------------------------------------------
# REM-10 -- THE ATTEMPT CENSUS AND THE GRADED LOSS. Hand-built worlds; no realm count is asserted.

def _rows(w) -> dict:
    """`{act id: (made, refused)}` by `attempts`, over every tick this world has run."""
    return {a.id: (made, no) for a, made, no in attempts(w, w.tick + 1)}


def _lost_or_won_tell(band: str):
    """`tiny_world` with `p_low` holding a firsthand cell, one `tell` to `p_mid` folded at `band`
    (the pick the seam would make, as `test_told_by_channel._g6_world` folds it). Returns `(w, d)`."""
    w = P.tiny_world()
    w.persons["p_low"].ledger.append(Claim("c_rem10_held", "p_low", "Hh", "stores:grain", 8, 0,
                                           "firsthand", 37, "own"))
    d = SeasonDriver(w)
    act = Act(id=f"a_rem10_tell_{band}", actor="p_low", verb="tell",
              payload={"subject": "Hh", "to": "p_mid", "said": Said("Hh", "stores:grain", 8, 37, ())})
    w.step = Step.RESOLVE
    ok, kinds, _ = d._admits(w, act, VERB_TABLE["tell"])
    assert ok, f"the tell was refused at admission ({kinds}); the fold never ran"
    w.acts.append(act)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(band, {}))
    w.log.extend(out)
    return w, d


def test_rem10_attempts_counts_an_admission_refused_speak_and_an_uncontested_refusal():
    """A `speak` on a matter no docket names is refused `speech.unheard` at admission, before the
    contest, and never enters `SeasonDriver.resolved`; a `transfer` of more than the actor holds is an
    UNCONTESTED refusal that does. `attempts` reads the act store and counts both as attempted and
    refused. The assertion that the fold set lacks the `speak` is what lets the first one fail: the
    old reading (`attribute`, over `d.resolved`) does not see it.

    MUTATION (run 2026-10-26, reverted): `attempts` pointed at `d.resolved` -- the `speak` assertion
    reds."""
    w, d = _world()
    _fold(w, d, Act(id="a_rem10_speak", actor="p_low", verb="speak", payload={"subject": "p_mid"}))
    _fold(w, d, Act(id="a_rem10_tr", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 10 ** 6}))
    rows = _rows(w)
    assert rows["a_rem10_speak"] == ((), ("speech.unheard",)), rows
    assert rows["a_rem10_tr"] == ((), ("transfer.refused",)), rows
    # the instrument could see the failure: the fold set holds the refusal but not the `speak`
    fold_set = {a.id for a, _, _ in attribute(w, d, w.tick + 1)}
    assert fold_set == {"a_rem10_tr"}, fold_set


def test_rem10_attribute_and_attempts_agree_on_every_act_the_fold_set_holds():
    """THE CONTROL. `attempts` is `attribute`'s rule over a larger set: on each act both hold, the
    `(made, refused)` pair is the same. `checked` guards the loop against reading nothing."""
    w, d = _world()
    _fold(w, d, Act(id="a_rem10_speak", actor="p_low", verb="speak", payload={"subject": "p_mid"}))
    _fold(w, d, Act(id="a_rem10_tr_no", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 10 ** 6}))
    _fold(w, d, Act(id="a_rem10_tr_ok", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3}))
    n = w.tick + 1
    wide = {a.id: (m, r) for a, m, r in attempts(w, n)}
    narrow = {a.id: (m, r) for a, m, r in attribute(w, d, n)}
    assert set(narrow) < set(wide), (sorted(narrow), sorted(wide))
    checked = 0
    for aid, pair in narrow.items():
        assert wide[aid] == pair, (aid, wide[aid], pair)
        checked += 1
    assert checked >= 2
    assert {m for m, _ in narrow.values()} != {()}, "no executed act: the agreement is vacuous"
    # and `attribute` still takes the fold-set shape the callers that stay on it pass
    one = next(a for a in d.resolved if a.id == "a_rem10_tr_ok")
    assert [(m, r) for _, m, r in attribute(w, SimpleNamespace(resolved=[one]), n)] == [wide[one.id]]
    assert _attribute_acts(w, [one], n) == attribute(w, SimpleNamespace(resolved=[one]), n)


def test_rem10_unrowed_acts_counts_a_verb_that_is_no_table_row():
    w, d = _world()
    assert unrowed_acts(w) == 0
    w.acts.append(Act(id="a_rem10_zz", actor="p_low", verb="zz_not_a_row"))
    assert unrowed_acts(w) == 1
    assert "a_rem10_zz" not in _rows(w), "an act with no row has no (made, refused) to report"


def test_rem10_foreign_kinds_names_a_logged_kind_outside_both_of_the_rows_columns():
    """`transfer.made` caused by a `speak` act: the kind is in neither of `speak`'s columns. Built by
    folding a `transfer` and re-reading the log against an act store that names it as a `speak`."""
    w, d = _world()
    _fold(w, d, Act(id="a_rem10_tr_ok", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3}))
    assert foreign_kinds(w) == {}, foreign_kinds(w)       # the control: nothing foreign in a clean fold
    sp = Act(id="a_rem10_speak", actor="p_low", verb="speak", payload={"subject": "p_mid"})
    w.acts.append(sp)
    ev = next(e for e in w.log if e.kind == "transfer.made")
    ev.causes = [*ev.causes, sp.id]
    assert foreign_kinds(w)[("speak", "transfer.made")] == 1, foreign_kinds(w)


def _graded_research(failure: bool):
    """A `research` on the Record folded through the real driver, swept over act ids until one draws
    `Failure` (`finding.none`, degree `Failure`) or a finding band (`finding.made`)."""
    for n in range(80):
        w, d = _fi_world()
        out = _fi_resolve(w, d, Act(id=f"a_rem10_res_{n}", actor=FI_ACTOR, verb="research",
                                    payload={"subject": FI_REC}))
        assert len(out) == 1, [(e.kind, e.degree) for e in out]
        if (out[0].degree == "Failure") == failure:
            return w, d, out
    raise AssertionError("80 act ids never drew the band asked for")


def test_rem10_graded_loss_counts_a_lost_tell_and_a_failed_inquiry_and_nothing_else():
    """HR-8. A lost `tell` (`news.untold`, `Failure`) and a `Failure` `research` (`finding.none`) are
    graded losses, counted by `graded_loss` and `graded_losses`, and are `both` acts. A `research`
    on a Record that is not there is refused at admission with the SAME kind and no degree: it is
    `both` (the kind is in both columns) and NOT a graded loss. A Success `tell` is neither. A
    refused `transfer` has no kind in both columns.

    MUTATION (run 2026-10-26, reverted): the `degree == "Failure"` test dropped from `graded_loss` --
    the admission-refused `research` reads as a graded loss and this test reds."""
    # -- the lost tell, and the Success tell beside it as the control
    w, _ = _lost_or_won_tell("Failure")
    (lost,) = graded_losses(w, w.tick + 1)
    assert lost.verb == "tell" and _rows(w)[lost.id] == (("news.untold",), ("news.untold",))
    ws, _ = _lost_or_won_tell("Success")
    assert graded_losses(ws, ws.tick + 1) == []
    assert list(_rows(ws).values()) == [(("news.told",), ())], _rows(ws)
    # -- the failed inquiry
    wf, _, outf = _graded_research(failure=True)
    assert (outf[0].kind, outf[0].degree) == ("finding.none", "Failure")
    (gl,) = graded_losses(wf, wf.tick + 1)
    assert gl.verb == "research" and _rows(wf)[gl.id] == (("finding.none",), ("finding.none",))
    # -- the finding band is not a loss
    wm, _, outm = _graded_research(failure=False)
    assert outm[0].kind == "finding.made" and graded_losses(wm, wm.tick + 1) == []
    # -- the admission-refused research: a refusal, `both`, and NOT a graded loss
    wa, da = _fi_world()
    outa = _fi_resolve(wa, da, Act(id="a_rem10_res_gone", actor=FI_ACTOR, verb="research",
                                   payload={"subject": "rec_none"}))
    assert [(e.kind, e.degree) for e in outa] == [("finding.none", None)]
    assert _rows(wa)["a_rem10_res_gone"] == (("finding.none",), ("finding.none",))
    assert graded_losses(wa, wa.tick + 1) == [], "an admission refusal (degree None) read as a graded loss"
    assert not graded_loss(Act(id="x", actor="p", verb="research"), outa)
    # -- a refusal with no kind in both columns
    wt, dt = _world()
    _fold(wt, dt, Act(id="a_rem10_tr_no", actor="p_low", verb="transfer",
                      payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 10 ** 6}))
    assert graded_losses(wt, wt.tick + 1) == []
    # -- the reader itself, on a synthetic Failure: every refusal-kind Event must carry it
    ev = lambda kind, degree: SimpleNamespace(kind=kind, degree=degree)
    a = Act(id="x", actor="p", verb="tell")
    assert graded_loss(a, [ev("news.untold", "Failure")])
    assert not graded_loss(a, [ev("news.untold", "Failure"), ev("news.untold", None)])
    assert not graded_loss(a, [ev("news.told", "Success")]) and not graded_loss(a, [])


def test_rem10_every_graded_loss_is_also_a_both_act(realm):
    """THE CONTROL on the new reader: a graded loss has a kind in both columns, so `graded` can never
    exceed `both`. Checked on the hand-built losses and, per verb, on a populated season's own dict."""
    checked = 0
    for w in (_lost_or_won_tell("Failure")[0], _graded_research(failure=True)[0]):
        both = {a.id for a, made, no in attempts(w, w.tick + 1) if made and no}
        losses = {a.id for a in graded_losses(w, w.tick + 1)}
        assert losses and losses <= both, (losses, both)
        checked += len(losses)
    assert checked == 2
    assert all(n <= realm["both"].get(v, 0) for v, n in realm["graded"].items()), (
        realm["graded"], realm["both"])
    assert realm["unrowed"] == 0, "an act in the store names a verb no table row has"
