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

CR-14 (the pooled census). Planted worlds and planted dicts; no realm count is asserted (V2):
  * a `need` scene about a goal id and one about a non-goal id read into the two scene rows, through
    `decision_spread.goal_class`, the one classifier;
  * the wrong-kind columns: a `restore` on a person id and a `carry` of a person id are the first
    class, a `restore` on an id in no collection is an absent subject, a `determine` with no
    DocketItem is the DocketItem column and not the first; a person is present until a death precedes
    the act; an admitted-then-refused act is the `after` class;
  * the death census (a MATTER death is `no act`; a killing `fight` names its verb; seats are the
    season's start's); pooling is asserted on planted per-seed dicts, and the command line's forms parse.
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


# ---------------------------------------------------------------------------------------------
# REM-11 -- WHY EACH REFUSAL REFUSED. Hand-built worlds; no realm count is asserted.

def _reading(w, d) -> dict:
    """`refusal_reading` over every act the world's store holds, keyed through `d.act_of`."""
    return A.refusal_reading(w, d, attempts(w, w.tick + 1))


def _restore_on_a_person():
    """`tiny_world`: a `restore` aimed at a PERSON (`p_mid`) where a Site belongs, beside a `transfer`
    refused for want of grain -- a refusal whose deciding read is not `exists:<Kind>=0`."""
    w, d = _world()
    _fold(w, d, Act(id="a_rem11_restore", actor="p_low", verb="restore", payload={"site": "p_mid"}))
    _fold(w, d, Act(id="a_rem11_tr", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 10 ** 6}))
    return w, d


def _migrate_into_a_full_rung():
    """The spine of `test_migrate_capacity.py`: `lr_hearth_b` houses one under one dwelling, so a
    newcomer's `migrate` is refused at the `write` clause after clearing its whole `requires`, beside
    a `speak` on a matter no docket names, refused at admission before the contest."""
    from .test_migrate_capacity import _fold as mig_fold
    from .test_migrate_capacity import _world as mig_world
    w, d = mig_world(lambda: governance_spine.build(0))
    mig_fold(w, d, Act(id="a_rem11_mg", actor="lp_hearth_a", verb="migrate",
                       payload={"to": "lr_hearth_b"}))
    mig_fold(w, d, Act(id="a_rem11_speak", actor="lp_hearth_a", verb="speak",
                       payload={"subject": "lp_community_a"}))
    return w, d


def test_rem11_a_restore_on_a_person_id_reads_exists_site_zero():
    """The deciding read of a `restore` aimed at a person is `exists:Site` = 0: the subject is not a
    Site. The `transfer` beside it is the control: it is refused on `stores:grain`, so only the
    `restore` is counted by `exists_zero`, and neither is a post-admission refusal (a read FAILED).

    MUTATION (run 2026-10-26, reverted): `_observed_of` returning `()` -- this test and the
    post-admission test below both red."""
    w, d = _restore_on_a_person()
    rd = _reading(w, d)
    assert rd["reasons"]["restore"] == {"last-read exists:Site=0": 1}, rd["reasons"]
    assert list(rd["reasons"]["transfer"]) == ["last-read stores:grain=>0"], rd["reasons"]
    assert A.exists_zero(rd["reasons"]) == 1
    assert rd["post_admission"] == {}, rd["post_admission"]


def test_rem11_a_migrate_into_a_full_rung_is_a_post_admission_refusal():
    """`migrate` clears its whole `requires` (every recorded read passes) and is refused at the
    `write` clause by the capacity throttle: counted `post-admission`, its reason the clause the row
    keys. The `speak` refused at admission is the control: a read failed, so it is not counted."""
    w, d = _migrate_into_a_full_rung()
    rd = _reading(w, d)
    assert rd["post_admission"] == {"migrate": 1}, rd["post_admission"]
    assert rd["reasons"]["migrate"] == {"clause:write": 1}, rd["reasons"]
    assert "speak" in rd["reasons"] and "speak" not in rd["post_admission"], rd


def test_rem11_dropping_the_observed_read_blinds_both_readings(monkeypatch):
    """THE MUTATION, IN THE SUITE: with the instrument's one read of `Event.observed` returning
    nothing, the `restore` has no deciding read and the `migrate` is no longer provably
    post-admission. Each reading is taken first with the read intact, so the change is what is
    observed and not the absence of a baseline."""
    wr, dr = _restore_on_a_person()
    wm, dm = _migrate_into_a_full_rung()
    assert _reading(wr, dr)["reasons"]["restore"] == {"last-read exists:Site=0": 1}
    assert _reading(wm, dm)["post_admission"] == {"migrate": 1}
    monkeypatch.setattr(A, "_observed_of", lambda event: ())
    assert _reading(wr, dr)["reasons"]["restore"] == {"no-read": 1}
    assert A.exists_zero(_reading(wr, dr)["reasons"]) == 0
    assert _reading(wm, dm)["post_admission"] == {}


def test_rem11_a_graded_loss_is_no_refusal_reason_and_is_never_post_admission():
    """A `research` that drew `Failure` (`finding.none`) cleared its reads: by reads alone it would be
    post-admission. `graded_loss` takes it out first, so it is its own reason. The control is the
    `research` refused at admission on a Record that is not there (same kind, no degree), which is a
    refusal with its own deciding read. (A fold that bypasses `d.resolve`, as `_lost_or_won_tell`
    does, leaves `d.act_of` empty and the act reads `no-event`: the instrument says so, not 0.)"""
    w, d, _ = _graded_research(failure=True)
    rd = _reading(w, d)
    assert rd["reasons"]["research"] == {"graded-loss": 1}, rd
    assert rd["post_admission"] == {}
    wa, da = _fi_world()
    _fi_resolve(wa, da, Act(id="a_rem11_res_gone", actor=FI_ACTOR, verb="research",
                            payload={"subject": "rec_none"}))
    ra = _reading(wa, da)
    assert list(ra["reasons"]["research"]) != ["graded-loss"], ra
    assert "no-event" not in ra["reasons"]["research"], ra
    wl, dl = _lost_or_won_tell("Failure")
    assert _reading(wl, dl)["reasons"]["tell"] == {"no-event": 1}


def test_rem11_kind_census_counts_by_act_and_names_the_declared_kinds_the_log_lacks():
    """`kind_census`: the kinds of a log against `EMITTED_KINDS` with the matrix's `emits:`. A fold
    of one `transfer` puts `transfer.made` in the log under one act; the declared kinds absent from
    it are named, and no kind in `never` is in the log."""
    w, d = _world()
    _fold(w, d, Act(id="a_rem11_tr_ok", actor="p_low", verb="transfer",
                    payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3}))
    c = A.kind_census(w, d)
    assert c["counts"]["transfer.made"] == {"events": 1, "acts": 1, "no_act": 0}, c["counts"]
    assert "transfer.made" not in c["never"] and "transfer.refused" in c["never"], c["never"]
    assert not set(c["never"]) & set(c["counts"])
    assert len(c["never"]) < c["declared"]


# ---------------------------------------------------------------------------------------------
# CR-14 -- THE POOLED CENSUS (i), THE ANSWERED-BY-SOURCE BLOCK (ii), THE DEATH CENSUS (iii), THE
# WRONG-KIND COLUMNS (v). Planted worlds and planted dicts assert RELATIONS; the realm readings are
# printed by the CLI and are never asserted here (V2).

def _need(about: str, qid: str = "q", source: str = "need"):
    from ..state.carriers import Question
    return Question(qid, source, ("p_x",), about)


def _scene_world(*occasions):
    """A stand-in for a driver after a season: only `scenes` is read by `scene_sources`."""
    return SimpleNamespace(scenes={f"sc{i}": SimpleNamespace(occasion=q)
                                   for i, q in enumerate(occasions)})


def _a_goal_id() -> str:
    from ..data import goals as goals_data
    return goals_data.goals()[0].id


def test_cr14_a_need_scene_about_a_goal_and_one_about_a_non_goal_read_into_the_two_rows():
    """A `need` question about a goal id and one about an id that is no goal, planted as scenes, land
    in the two scene rows P2 splits `need` into; a `claim_landed` scene and a scene with no occasion
    are the controls (not `need`). The goal class is `decision_spread.goal_class`, the one classifier.

    MUTATION (run 2026-10-27, reverted): `class_label` returning `q.source` alone -- both `need`
    scenes read into one row, `need_goal` reads 0 and the split assertions red."""
    from ..harness import decision_spread as DS
    goal = _a_goal_id()
    d = _scene_world(_need(goal, "q1"), _need("rec_not_a_goal", "q2"),
                     _need("p_x", "q3", "claim_landed"), None)
    got = A.scene_sources(d)
    assert got["scenes"] == 4 and got["need"] == 2 and got["need_goal"] == 1, got
    assert got["rows"][("need", "org goal")] == 1 and got["rows"][("need", "other need")] == 1, got
    assert got["rows"][("claim_landed", "-")] == 1 and got["rows"][("none", "-")] == 1, got
    assert A.goal_class is DS.goal_class, "aperture must call the lifted classifier, not a copy"


def test_cr14_mutation_classifying_through_the_source_alone_blinds_the_split(monkeypatch):
    goal = _a_goal_id()
    d = _scene_world(_need(goal, "q1"), _need("rec_not_a_goal", "q2"))
    assert A.scene_sources(d)["need_goal"] == 1                 # the baseline, read first
    monkeypatch.setattr(A, "class_label", lambda q: q.source)
    assert A.scene_sources(d)["need_goal"] == 0                 # the split is gone: the test above reds


def test_cr14_class_label_is_goal_class_with_an_org_goal_collapsed():
    from ..data.rosters import FACTION_BY_PROP
    assert A.class_label(_need("prop_somebody")) == "own want"
    assert A.class_label(_need(next(iter(FACTION_BY_PROP)))) == "creed"
    assert A.class_label(_need(_a_goal_id())) == "org goal"
    assert A.class_label(_need("rec_not_a_goal")) == "other need"
    assert A.class_label(_need("anything", source="claim_landed")) == "-"


def test_cr14_a_deliberation_with_no_question_is_its_own_row_and_the_rows_sum_to_the_rule_count(realm):
    """The deliberation table's within-instrument control, on the 1-season realm the module fixture
    holds: its rows plus `none` sum to the shipped rule's deliberation count. `checked` guards the
    sum against reading an empty table."""
    assert sum(realm["answered"].values()) == realm["deliberations"], (
        realm["answered"], realm["deliberations"])
    assert realm["deliberations"] > 0
    assert len(realm["per_rule"][realm["shipped_rule"]]) == realm["deliberations"]
    assert all(isinstance(k, tuple) and len(k) == 2 for k in realm["answered"])
    sc = realm["scenes"]
    assert sum(sc["rows"].values()) == sc["scenes"] and sc["need_goal"] <= sc["need"]
    assert realm["news"]["told"] >= 0 and realm["news"]["untold"] >= 0


# -- (v) the wrong-kind columns -----------------------------------------------------------------

def _wk_world():
    """The world of `test_in45_carry._filed` (a petition filed by `p_low` about `p_mid` before the
    Duke's bench), with four planted attempts folded through the real driver: a `restore` aimed at
    a person (`p_mid`), a `restore` aimed at an id in no collection, a `carry` of a PERSON id where
    a Petition belongs, and a `determine` of a person nothing docketed. Returns `(w, d, rows, rd,
    cast)`."""
    from .test_in45_carry import DUKE, PARTY, SEAT, _filed
    from .test_u7_remit import JUDGE
    from ..data.fixtures import DEFAULT_FIXTURES
    w, d = _filed(DEFAULT_FIXTURES.sweep("pool_default", JUDGE["pool_default"]))
    cast = frozenset(w.persons)
    for key, verb, who, payload in (
            ("a_wk_restore_person", "restore", DUKE, {"subject": PARTY, "site": PARTY}),
            ("a_wk_restore_nowhere", "restore", DUKE, {"subject": "zz_nowhere", "site": "zz_nowhere"}),
            ("a_wk_carry_person", "carry", "p_low", {"subject": PARTY, "petition": PARTY}),
            ("a_wk_determine", "determine", DUKE, {"subject": PARTY})):
        _fold(w, d, Act(id=key, actor=who, verb=verb, via=SEAT, payload=payload))
    rows = attempts(w, w.tick + 1)
    rd = A.refusal_reading(w, d, rows)
    return w, d, rows, rd, cast


def _wk_by_act(w, d, rows, rd, cast) -> dict:
    """`{act id: the one class it fell in}`: each refused planted act is classed ALONE, by narrowing
    `rows` to it, so a class is read per act and not inferred from a count."""
    out = {}
    for row in rows:
        got = A.wrong_kind(w, d, [row], rd["post_acts"], cast)
        if got["refused"]:
            (cls,) = [c for c, n in got["classes"].items() if n]
            out[row[0].id] = cls
    return out


def test_cr14_wrong_kind_a_site_wanted_a_person_found_counts_in_the_first_class():
    """The four planted attempts: a `restore` on a person id is a Site wanted and a Person found (the
    first class); on an id in no collection, an absent subject; a `carry` on a person id wants a Petition
    (a Record sub-kind) of a subject in another collection (the first class); a `determine` on a person
    with no DocketItem is the DocketItem column and NOT the first class. Each refused act falls in
    exactly one class, so the classes sum to the refused acts.

    MUTATION (run 2026-10-27, reverted): the `DocketItem` branch dropped -- the `determine` reads
    `other` and the docket assertion reds; the first-class tuple emptied -- the first assertion reds."""
    w, d, rows, rd, cast = _wk_world()
    got = A.wrong_kind(w, d, rows, rd["post_acts"], cast)
    by_act = _wk_by_act(w, d, rows, rd, cast)
    assert by_act["a_wk_restore_person"] == "collection", by_act
    assert by_act["a_wk_restore_nowhere"] == "absent", by_act
    assert by_act["a_wk_carry_person"] == "record_in_collection", by_act
    assert by_act["a_wk_determine"] == "docket", by_act
    c = got["classes"]
    assert c["collection"] >= 1 and c["record_in_collection"] >= 1 and c["absent"] >= 1 and c["docket"] >= 1
    first = sum(c[k] for k in A.WRONG_KIND_FIRST)
    assert first == sum(1 for k in by_act.values() if k in A.WRONG_KIND_FIRST) == 2
    assert "docket" not in A.WRONG_KIND_FIRST and "absent" not in A.WRONG_KIND_FIRST
    assert sum(c.values()) == got["refused"], (c, got["refused"])
    assert got["refused"] == sum(1 for _, _, no in rows if no) and got["attempted"] == len(rows)
    assert len(by_act) >= 4, "the loop read fewer than the four planted refusals"


def test_cr14_wrong_kind_a_person_counts_present_until_a_death_precedes_the_act():
    """A person is present at an act when he is in the pre-season cast and no `person.died` naming
    him precedes the act's first Event. `restore` aimed at `p_other` is a Site wanted: alive, a
    wrong collection (first class); aimed at him after his death is logged, he lives in no collection
    the run left and the subject reads absent. (`tiny_world` gives each person a Rung of his own id; the
    death removes it with him, which the second assertion relies on.)"""
    from ..data.matrix import Step as _Step
    from ..state.ids import ROOT

    def run(die_first: bool):
        w, d = _world()
        cast = frozenset(w.persons)
        if die_first:
            w.step = _Step.MATTER
            w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_other"),
                    record_kind="Person", fieldname="exists", driver="Event",
                    emits="person.died", subject="p_other", causes=[ROOT])
        _fold(w, d, Act(id="a_wk_late", actor="p_low", verb="restore",
                        payload={"subject": "p_other", "site": "p_other"}))
        rows = attempts(w, w.tick + 1)
        rd = A.refusal_reading(w, d, rows)
        return A.wrong_kind(w, d, rows, rd["post_acts"], cast)["classes"]

    alive, dead = run(False), run(True)
    assert alive["collection"] == 1 and alive["absent"] == 0, alive
    assert dead["absent"] == 1 and dead["collection"] == 0, dead


def test_cr14_wrong_kind_an_admitted_then_refused_act_is_the_after_class_not_a_wrong_kind():
    """`migrate` into a full rung clears its whole `requires` and is refused at the `write` clause
    (REM-11's post-admission); the `speak` beside it is refused at admission on a read that failed.
    The post-admission act is the `after` class, and the classes sum to the refused acts."""
    w, d = _migrate_into_a_full_rung()
    rows = attempts(w, w.tick + 1)
    rd = A.refusal_reading(w, d, rows)
    got = A.wrong_kind(w, d, rows, rd["post_acts"], frozenset(w.persons))
    assert got["classes"]["after"] == sum(rd["post_admission"].values()) >= 1, got
    assert sum(got["classes"].values()) == got["refused"]


# -- (iii) the death census ---------------------------------------------------------------------

def test_cr14_death_census_places_a_matter_death_in_its_season_with_the_seat_held_at_its_start():
    """`p_high` holds `off_duke` at the season's start and dies at MATTER: no killing act (`no act`),
    one seat-holder victim, the seat read as of the START. A second reading with `marks` taken AFTER the
    death shows no seat -- the instrument reads what it is handed, which is what makes the first able to
    fail. A world with no death counts none."""
    from .test_h206_a_death_at_matter_is_witnessed import HOLDER, OFFICE, _die_at_matter, _world as dworld
    w = dworld()
    d = SeasonDriver(w)
    assert A.seats(w), "fixture: nobody holds a seat"
    assert A.death_census(w, d, [(len(w.log), A.seats(w))])["deaths"] == []     # no death yet
    start = [(len(w.log), A.seats(w))]
    _die_at_matter(w)                       # `World.write` logs the Event itself
    got = A.death_census(w, d, start)
    assert got["deaths"] == [{"victim": HOLDER, "season": 0, "verb": "no act", "seats": [OFFICE]}], got
    assert got["events"] == 1
    late = A.death_census(w, d, [(len(w.log) - 1, A.seats(w))])
    assert late["deaths"][0]["seats"] == [], late


def test_cr14_death_census_names_the_killing_acts_verb_through_the_act_map():
    """A `fight` that kills (`wound_harm_model = total`) is a death by `fight` -- the verb of the act
    `d.act_of` ties the `person.died` Event to. Skipped where the personal-combat engine is absent
    (as the test it follows is); `checked` guards the scan against finding no kill."""
    from .test_h206_a_death_at_matter_is_witnessed import (HOLDER, _killing_act_index,
                                                           _world as dworld)
    i = _killing_act_index()
    assert i is not None, "no act id in range killed p_high; the census would be vacuous"
    w = dworld()
    w.step = Step.RESOLVE
    w.fixtures = w.fixtures.sweep("wound_harm_model", "total")
    d = SeasonDriver(w)
    start = [(len(w.log), A.seats(w))]
    w.log.extend(d.resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id=f"h206_{i}", actor="p_near", verb="fight",
                                payload={"subject": HOLDER})], w.fixtures.get("contest_max_depth")))
    got = A.death_census(w, d, start)
    assert [x["verb"] for x in got["deaths"]] == ["fight"], got
    assert got["deaths"][0]["victim"] == HOLDER and got["deaths"][0]["seats"], got


# -- (i) pooling and the command line -----------------------------------------------------------

def _vc(**kw):
    base = {k: 0 for k in A.VERB_COLUMNS}
    return {**base, "refused_as": kw.pop("refused_as", {}), **kw}


def test_cr14_pool_verb_counts_sums_every_column_and_every_refused_as_kind():
    """Planted per-seed dicts, one verb missing from the second: every column is the sum, a verb
    one seed lacks counts 0 there, and `refused_as` sums per kind. The per-seed dicts are not mutated."""
    s1 = {"tell": _vc(att=5, ex=2, ref=3, both=1, graded=1, elig_s=2, refused_as={"news.untold": 3}),
          "work": _vc(att=7, ex=7)}
    s2 = {"tell": _vc(att=4, ex=1, ref=3, both=2, graded=2, refused_as={"news.untold": 1, "x": 2})}
    before = repr((s1, s2))
    got = A.pool_verb_counts([s1, s2])
    assert got["tell"]["att"] == 9 and got["tell"]["ex"] == 3 and got["tell"]["ref"] == 6
    assert got["tell"]["both"] == 3 and got["tell"]["graded"] == 3 and got["tell"]["elig_s"] == 2
    assert got["tell"]["refused_as"] == {"news.untold": 4, "x": 2}
    assert got["work"]["att"] == 7 and got["work"]["ref"] == 0
    totals = A.verb_totals(got)
    assert totals["att"] == 16 and totals["ref"] == 6
    assert repr((s1, s2)) == before


def _pw(seed, never, **over):
    """A planted per-world dict carrying only what `pool_worlds` reads."""
    zero = {c: 0 for c in A.WRONG_KIND_CLASSES}
    m = {"seed": seed, "reasons": {"tell": {"clause:x": 2}}, "post_admission": {"tell": 1},
         "kinds": {"declared": 9, "never": never, "counts": {"k": {"events": 3, "acts": 2, "no_act": 1}}},
         "wrong_kind": {"attempted": 10, "refused": 6, "classes": {**zero, "collection": 2, "other": 4},
                        "by_verb": {"tell": {"collection": 2}}, "other_detail": {"no-read": 1}},
         "deaths": {"events": 1, "deaths": [{"victim": f"v{seed}", "season": 0, "verb": "fight",
                                              "seats": []}]},
         "answered": {("need", "creed"): 3, ("none", "-"): 1}, "deliberations": 4,
         "scenes": {"scenes": 5, "rows": {("need", "org goal"): 2}, "need": 2, "need_goal": 2},
         "news": {"told": 1, "untold": 2}}
    m.update(over)
    return m


def test_cr14_pool_worlds_sums_counts_and_intersects_the_kinds_never_emitted():
    """Counts add over the planted seeds; the declared-kinds line is the kinds ABSENT FROM EVERY
    seed's log (an intersection, so a kind one seed emitted is not in it)."""
    a, b = _pw(0, ["k1", "k2", "k3"]), _pw(1, ["k2", "k3", "k4"])
    p = A.pool_worlds([a, b])
    assert p["kinds"]["never"] == ["k2", "k3"], p["kinds"]
    assert p["kinds"]["counts"]["k"] == {"events": 6, "acts": 4, "no_act": 2}
    assert p["reasons"] == {"tell": {"clause:x": 4}} and p["post_admission"] == {"tell": 2}
    assert p["wrong_kind"]["attempted"] == 20 and p["wrong_kind"]["refused"] == 12
    assert p["wrong_kind"]["classes"]["collection"] == 4 and p["wrong_kind"]["classes"]["other"] == 8
    assert p["wrong_kind"]["by_verb"] == {"tell": {"collection": 4}}
    assert p["wrong_kind"]["other_detail"] == {"no-read": 2}
    assert p["deaths"]["runs"] == 2 and [x["seed"] for x in p["deaths"]["deaths"]] == [0, 1]
    assert p["answered"] == {("need", "creed"): 6, ("none", "-"): 2} and p["deliberations"] == 8
    assert p["scenes"]["scenes"] == 10 and p["scenes"]["need_goal"] == 4
    assert p["news"] == {"told": 2, "untold": 4}
    assert sum(p["answered"].values()) == p["deliberations"], "the pooled rows keep the sum control"
    # the pooled dict prints through the same printers as one world's
    text = "\n".join(A.cr14_blocks(p))
    assert "SUM CONTROL" in text and "-> OK" in text and "runs 2" in text


def test_cr14_the_original_positional_form_and_the_seeds_form_parse():
    """`aperture <seasons> <seed>` is unchanged; `aperture <seasons> --seeds S [S ...]` adds the
    pooled form with `seasons` positional; a bare `--seeds`, a non-numeric seed and a positional seed
    beside `--seeds` are refused."""
    assert A.parse_args([]) == (1, [0], False)
    assert A.parse_args(["2", "0"]) == (2, [0], False)
    assert A.parse_args(["3"]) == (3, [0], False)
    assert A.parse_args(["2", "--seeds", "0", "1", "4"]) == (2, [0, 1, 4], True)
    for bad in (["2", "--seeds"], ["2", "--seeds", "a"], ["2", "0", "--seeds", "1"]):
        with pytest.raises(ValueError):
            A.parse_args(bad)
    assert A.main(["2", "--seeds"]) == 2
