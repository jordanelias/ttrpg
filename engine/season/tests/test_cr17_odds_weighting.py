"""CR-17 (M1, AQ-X1 (b)) -- A PERSON'S BELIEVED CHANCE WEIGHTS THE PURSUIT TERM OF A CONTESTED CANDIDATE
(`decision/choose.py::odds_weight`, `Fixtures.odds_weighting`, H-248).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * TWO PERSONS WITH EQUAL PURSUITS, ONE WHOSE BELIEVED CHANCE OF THE BANDS THE `argue` ROW WRITES IN READS
    0.7 AND ONE 0.1, RANK THE SAME `argue` DIFFERENTLY AT `believed` AND ALIKE AT `none` -- through
    `make_chooser`'s real ranking. PLANTED FAILURE: `odds_weight` replaced by a factor of 1 reddens the
    first assertion (`test_the_planted_factor_of_one_reddens_the_difference`).
  * A PERSON WHOSE BELIEVED INPUT IS `None` RANKS IT, AND SCORES IT, EXACTLY AS AT `none`; an UNCONTESTED
    candidate is the same at both arms whatever the query says; a View with no query is the same as `none`.
  * THE FIGURE IS THE REAL READER'S: two persons whose pools differ (a registered addend, as
    `test_odds_of.py` does) get believed chances equal to `odds_of` mode (b) summed over the row's writing bands,
    the stronger higher, and their rankings part on it; the bands handed to the query are the row's own
    non-empty `writes:` lists, a proper subset of the ladder (else the weighting would be 1 by construction).
  * THE PLUMBING IS REAL: a driver season hands every person's View a callable `odds`, and the callable answers
    a real act (a float or `None`), taking the act and the bands (the person is bound to it).
  * THE ARM IS A ROSTER: an arm outside `rosters.yaml: odds_weightings` raises.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL, Degree
from engine.substrate.descriptors import PURSUITS

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam.wrappers import pool, sigma
from ..data.rosters import VERB_CAPABILITY
from ..state.carriers import Act, Candidate, Claim, Person

AXIS = "grandiose_humble"        # a pursuit axis the equal pursuits below project onto (asserted in the test)
RIVAL = "carry"                  # an uncontested verb: no `contests:`, so its pursuit term is never weighted
HEARER = "p_other"


def _arms(arm):
    return DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("odds_weighting", arm)


def _person(pid):
    p = Person(id=pid, name=pid)
    # roster-exempt: TEST FIXTURE pursuits -- the same vector for both persons, so only the odds can part them.
    p.pursuits = {n: 1.0 for n in PURSUITS}
    return p


@pytest.fixture
def cells(monkeypatch):
    """`argue` carries no alignment cell in the shipped table, so one is planted on the rebound binding (the
    `H-66` sweep's own seam): `argue` 1.0 on AXIS, the uncontested rival 0.4. At a believed chance `c` the
    argue pursuit term is `W * c` against the rival's `W * 0.4`, so the two parts at c = 0.4."""
    table = {ax: dict(row) for ax, row in V.ALIGNMENT.items()}
    table.setdefault(AXIS, {}).update({"argue": 1.0, RIVAL: 0.4})
    monkeypatch.setattr(V, "ALIGNMENT", table)
    return table


def _argue():
    return Candidate("argue", "prop_x", operands={"to": HEARER})


def _rival():
    return Candidate(RIVAL, "prop_x")


def _ranked(person, arm, odds, monkeypatch):
    """`make_chooser`'s real ranking of the two candidates for `person`, the View carrying `odds` (the
    `test_told_by_channel.py::_g2_ranked` shape: the option set is planted, `pack_scenes` is a spy)."""
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda p, view, q, fx: [_argue(), _rival()])

    def spy(p, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [c.verb for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    CH.make_chooser(_arms(arm), lambda *a: "act")(
        person, SimpleNamespace(question=object(), odds=odds), SimpleNamespace(), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"]


def _query(chance):
    """A believed-odds query that answers `chance` for every act and remembers what it was asked."""
    asked = []

    def odds(act, bands):
        asked.append((act.actor, act.verb, tuple(bands)))
        return chance
    odds.asked = asked
    return odds


def _assert_the_two_persons_part_at_believed(monkeypatch):
    sure, unsure = _person("p_sure"), _person("p_unsure")
    assert CH.deliberation_memo(sure, _arms("none"))[CH._AXIS_W][AXIS] > 0, "the equal pursuits project to nothing"
    at_believed = (_ranked(sure, "believed", _query(0.7), monkeypatch),
                   _ranked(unsure, "believed", _query(0.1), monkeypatch))
    assert at_believed[0] != at_believed[1], f"equal pursuits, odds 0.7 and 0.1, one ranking: {at_believed}"
    return at_believed


def test_equal_pursuits_rank_argue_differently_at_believed_and_alike_at_none(cells, monkeypatch):
    sure, unsure = _person("p_sure"), _person("p_unsure")
    at_believed = _assert_the_two_persons_part_at_believed(monkeypatch)
    # the person who believes he will win it ranks it above the rival; the one who believes he will not, below
    assert at_believed == (["argue", RIVAL], [RIVAL, "argue"])
    at_none = (_ranked(sure, "none", _query(0.7), monkeypatch), _ranked(unsure, "none", _query(0.1), monkeypatch))
    assert at_none[0] == at_none[1] == ["argue", RIVAL]            # the control: odds are not asked, the term is whole


def test_at_none_the_query_is_never_asked_and_the_score_is_the_old_one(cells):
    p = _person("p_sure")
    memo = CH.deliberation_memo(p, _arms("none"))
    odds = _query(0.1)
    scored = CH.score_terms(p, _argue(), _arms("none"), memo, odds)
    assert odds.asked == [] and scored == CH.score_terms(p, _argue(), _arms("none"), memo)
    assert scored[0] == memo[CH._AXIS_W][AXIS] * 1.0                # alignment 1.0, damp 1.0, factor exactly 1


def test_a_believed_input_of_none_ranks_and_scores_exactly_as_at_none(cells, monkeypatch):
    p = _person("p_unknown")
    asked = _query(None)
    assert _ranked(p, "believed", asked, monkeypatch) == _ranked(p, "none", None, monkeypatch)
    assert asked.asked, "the query was never asked: the None case did not run"
    memo = CH.deliberation_memo(p, _arms("believed"))
    for c in (_argue(), _rival()):
        assert CH.score_terms(p, c, _arms("believed"), memo, _query(None)) == CH.score_terms(p, c, _arms("none"), memo)
        # a View with no query at all is the same answer
        assert CH.score_terms(p, c, _arms("believed"), memo, None) == CH.score_terms(p, c, _arms("none"), memo)


def test_an_uncontested_candidate_is_unchanged_at_believed_whatever_the_query_says(cells):
    p = _person("p_sure")
    odds = _query(0.0)
    memo = CH.deliberation_memo(p, _arms("believed"))
    assert not VERB_TABLE[RIVAL].contests
    assert CH.score_terms(p, _rival(), _arms("believed"), memo, odds) == CH.score_terms(p, _rival(), _arms("none"), memo)
    assert odds.asked == []                                         # an uncontested verb is not even asked
    # a contested candidate IS weighted: at a chance of 0 the pursuit term vanishes, the stance term does not
    assert CH.score_terms(p, _argue(), _arms("believed"), memo, odds)[0] == 0.0
    assert odds.asked and odds.asked[0][1] == "argue"


def test_the_bands_asked_are_the_rows_own_writing_bands_and_a_proper_subset(cells):
    p = _person("p_sure")
    odds = _query(0.5)
    CH.score_terms(p, _argue(), _arms("believed"), CH.deliberation_memo(p, _arms("believed")), odds)
    row = VERB_TABLE["argue"]
    writing = tuple(b for b, written in row.writes_by_degree.items() if written)
    assert odds.asked == [("p_sure", "argue", writing)]
    assert 0 < len(writing) < len(row.writes_by_degree), "a weighting over every band, or none, is 1 by construction"
    # a contested verb that writes in no band is not weighted (nothing for the term to price)
    silent = [v for v, r in VERB_TABLE.items() if r.contests and not any(r.writes_by_degree.values())]
    assert silent, "no contested verb writes in no band: the case this branch covers does not run"
    ask = _query(0.3)
    assert CH.odds_weight(p, Candidate(silent[0], "x"), _arms("believed"), ask) == 1.0 and ask.asked == []


def test_the_planted_factor_of_one_reddens_the_difference(cells, monkeypatch):
    _assert_the_two_persons_part_at_believed(monkeypatch)            # green on the real weighting
    monkeypatch.setattr(CH, "odds_weight", lambda p, c, fx, odds: 1.0)
    with pytest.raises(AssertionError, match="one ranking"):
        _assert_the_two_persons_part_at_believed(monkeypatch)


def test_an_arm_outside_the_roster_raises(cells):
    p = _person("p_sure")
    with pytest.raises(Unspecified):
        CH.odds_weight(p, _argue(), DEFAULT_FIXTURES.sweep("odds_weighting", "certain"), _query(0.5))


# ---------------------------------------------------------------------------------------------
# THE REAL READER (CP-T01-03's mode (b)) AND THE PLUMBING
# ---------------------------------------------------------------------------------------------

def _world():
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    return w


def _believes_the_hearer(p):
    """REM-30's `verb_capability` row makes `argue` draw on the `argue` key, so the opposition of a person hearer is
    a belief the roller must HOLD (`sigma.believed_input`: none held -> unknown -> no figure), and nothing deposits one
    in a built realm. These readings need a figure, so the believer is handed the claim: the hearer's score 4, an
    obstacle of 2.0, which is what the module's own default reads for a hearer who holds no key."""
    p.ledger.append(Claim(id=f"c:{p.id}:{HEARER}", holder=p.id, subject=HEARER,
                          predicate=sigma.CAPABILITY_CLAIM + VERB_CAPABILITY["argue"], value=4, when=0,
                          source="told", confidence=5, visibility="own"))


def test_two_pools_give_two_believed_chances_and_two_rankings(cells, monkeypatch):
    w = _world()
    sure, unsure = w.persons["p_low"], w.persons["p_mid"]
    # roster-exempt: TEST FIXTURE addend -- one person's pool four dice above the other's (`test_odds_of.py`'s way).
    monkeypatch.setattr(pool, "POOL_ADDENDS", [lambda w_, who, verb: 4 if who.id == sure.id else 0])
    for p in (sure, unsure):
        p.pursuits = {n: 1.0 for n in PURSUITS}
        _believes_the_hearer(p)
    row = VERB_TABLE["argue"]
    bands = tuple(b for b, written in row.writes_by_degree.items() if written)
    place = {DEGREE_LABEL[d]: n for d, n in DEGREE_ORDINAL.items()}
    chance = {}
    for p in (sure, unsure):
        act = Act(f"a:{p.id}", p.id, "argue", payload={"subject": "prop_x", "to": HEARER})
        odds = sigma.odds_of(w, act, believer=p)
        assert odds is not None
        want = sum(odds[place[b]] for b in bands)
        assert sigma.believed_chance(w, p, act, bands) == want
        chance[p.id] = want
    assert chance[sure.id] > chance[unsure.id] + 0.2, chance
    # the rival's cell sits between the two chances (the pursuit weight scales both sides alike), so the real
    # figures part the rankings
    cells[AXIS][RIVAL] = (chance[sure.id] + chance[unsure.id]) / 2
    query = {p.id: sigma.believed_odds_query(w, p) for p in (sure, unsure)}       # each bound to its holder
    ranks = {p.id: _ranked(p, "believed", query[p.id], monkeypatch) for p in (sure, unsure)}
    assert ranks[sure.id] == ["argue", RIVAL] and ranks[unsure.id] == [RIVAL, "argue"], (chance, ranks)
    assert (_ranked(sure, "none", query[sure.id], monkeypatch)
            == _ranked(unsure, "none", query[unsure.id], monkeypatch))
    # a holder-bound query answers for its holder alone: asked about another's act it is `None`, not his belief
    other = Act("a:other", unsure.id, "argue", payload={"subject": "prop_x", "to": HEARER})
    assert query[sure.id](other, bands) is None


def test_another_modules_prize_and_a_foreign_actor_are_unknown_not_a_figure():
    w = _world()
    p = w.persons["p_low"]
    fight = Act("a:fight", p.id, "fight", payload={"subject": "p_mid"})
    assert sigma.believed_chance(w, p, fight, (DEGREE_LABEL[Degree.SUCCESS],)) is None   # the body is combat's, not the dice here
    argue = Act("a:argue", "p_mid", "argue", payload={"subject": "prop_x", "to": HEARER})
    assert sigma.believed_chance(w, p, argue, (DEGREE_LABEL[Degree.SUCCESS],)) is None          # another's pool is not his to know
    own = Act("a:argue2", p.id, "argue", payload={"subject": "prop_x", "to": HEARER})
    assert sigma.believed_chance(w, p, own, ("Felled",)) is None              # a band this ladder does not carry
    assert sigma.believed_chance(w, p, own, ()) is None                        # no band named, no figure


def test_a_driver_season_hands_every_view_a_working_query():
    w = _world()
    d = SeasonDriver(w)
    inner = CH.make_chooser(w.fixtures, lambda a, b, c: f"{a}:{b}:{c}", verbs=frozenset())
    views = []
    for who in w.persons.values():
        _believes_the_hearer(who)

    def watched(p, v, s, ask_budget):
        views.append((p, v))
        return inner(p, v, s, ask_budget)
    d.season(watched, None)
    assert views, "no person deliberated: the plumbing was not exercised"
    answered = 0
    for p, v in views:
        assert callable(v.odds)
        act = Act(f"a:{p.id}", p.id, "argue", payload={"subject": "prop_x", "to": HEARER})
        got = v.odds(act, (DEGREE_LABEL[Degree.SUCCESS],))
        assert got is None or 0.0 <= got <= 1.0
        answered += got is not None
    assert answered >= 1, "the query never answered a figure: it may be wired to a constant None"


# ---------------------------------------------------------------------------------------------
# THE SHIPPED ARMS, AND THE RE-DERIVED TEMPERATURE (H-96's rule, commit 2)
# ---------------------------------------------------------------------------------------------

def test_the_shipped_arms_are_the_falsified_ones():
    """`believed` ships because the falsifiers above pass (the B-E precedent); `none` stays selectable as the control."""
    assert DEFAULT_FIXTURES.get("odds_weighting") == "believed"
    assert CH.ODDS_WEIGHTINGS == frozenset({"none", "believed"})


def _strict_top_share(tau: float, seed: int = 0) -> tuple:
    """REM-12's split at the built realm (`decision_spread --decisions`), `(strict-top-decided, readings)` among persons holding a
    pursuit vector: the readings the draw did NOT decide (neither a tie it ordered nor a leader it overruled)."""
    from ..harness import decision_spread as DS
    w = DS._build(seed, False)
    w.fixtures = w.fixtures.sweep("choice_temperature", tau)
    sp = DS.read_decisions(w)["split"]
    return sp["read"] - sp["tie"] - sp["outvoted"], sp["read"] - sp["field_zero"]


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_tau_is_the_largest_grid_value_above_one_half_strict_top_decided_and_zero_is_the_argmax(seed):
    """H-96's re-derivation, executed at seeds 0-2 as the card reads them: the shipped tau reads MORE THAN ONE HALF of the
    vectored readings strict-top-decided, every grid value above it reads LESS, and tau 0 collapses to the argmax (every
    reading decided, no tie and no overruled leader). MEASURED, 0.05 -> 271 / 297 / 273 of 498, 0.1 -> 142 / 162 / 141.
    The test_u4 half of the rule is `test_season_shape.py::test_u4_the_choice_is_sampling_and_the_argmax_is_its_zero_temperature_control`."""
    shipped = float(DEFAULT_FIXTURES.get("choice_temperature"))
    grid = [0.0, 0.01, 0.02, 0.03, 0.05, 0.1, 0.25, 0.5, 1.0]
    assert shipped in grid, f"the shipped tau {shipped} is not on H-96's grid"
    decided, n = _strict_top_share(shipped, seed)
    assert n > 0 and decided * 2 > n, f"the shipped tau {shipped} reads {decided} / {n} strict-top-decided: not above one half"
    hotter = [g for g in grid if g > shipped]
    assert hotter, "no grid value above the shipped tau: the 'largest' half of the rule observes nothing"
    for g in hotter:
        d, m = _strict_top_share(g, seed)
        assert d * 2 <= m, f"tau {g}, above the shipped {shipped}, also reads above one half ({d} / {m}): the rule picks the largest"
    d0, n0 = _strict_top_share(0.0, seed)
    assert d0 == n0 > 0, f"tau 0 is not the argmax: {d0} of {n0} readings decided"


def test_none_and_tau_point_one_reproduce_the_parent_world_exactly(monkeypatch):
    """THE CARD'S CONTROL, executed (it was prose in go07 and weather): `odds_weighting` `none` and `choice_temperature` 0.1
    on `build_realm(0)`, one season, read the parent's (`f4b74ffa`'s) world: content hash `bdff0832...` and a log of
    10316 events (the figures `test_go07_canonical_digest.py` and `test_season_weather.py` record as the parent's). The
    shipped pair does not (685 acts, 11775), so the control can fail.

    The parent's world is re-pinned at every later DECLARED MOVER, each with the control that reads the old pin (the
    comments below). B10-11 RE-TAKE (CP-T03-09 and PC-10b left this pin unmoved, so it was red from `95f58adb`; closed at
    CR-87): the batch's movers are read IN PROCESS, both directions:
      * CR-87 at its revert (`test_cr87_violence_contexts.py::revert_cr87`, whose own control reproduces the pre-CR-87
        hashes), so the pin is the PC-10b tree's: `b8ac6025...` / 10869 (read on an export of `d2847e7b`, equal);
      * CP-T03-09's added row `capture` and PC-10b's re-shaped duel pair (`challenge`, `accept`) WITHHELD from the chooser's
        verbs: `a38516fb...` / 11505, the value the CP-T03-09 tree (an export of `95f58adb`) reads under the same
        withholding, so PC-10b moves nothing where no duel verb is chosen; on that tree `capture` alone withheld reads the
        old pin `edbc7442...` / 10435 exactly (CP-T03-09's own control, the go07 note's)."""
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)    # v11 CR-79 (the credit term, a later mover of the told deposit): reverted, so this pin reads its own item
    from .test_cr87_violence_contexts import revert_cr87
    revert_cr87(monkeypatch)
    # v11 CP-T03-04 (`arms` in the vocation range, a formation mover of every season) is read at its revert too
    # (`test_cp_t03_04_arms.py::revert_cp_t03_04`, whose own control reproduces the pre-item hashes), the same way.
    from .test_cp_t03_04_arms import revert_cp_t03_04
    revert_cp_t03_04(monkeypatch)
    # v11 CP-T03-07 (`Person.body_ceiling`, a schema mover of every realm, and the lasting mark), the same way.
    from .test_cp_t03_07_body_ceiling import revert_cp_t03_07
    revert_cp_t03_07(monkeypatch)
    from .test_cp_t03_08_tend_on_the_wounded import revert_cp_t03_08
    revert_cp_t03_08(monkeypatch)   # v11 CP-T03-08 (`tend` forms on the wounded, a formation mover of every season), the same way
    from .test_strife_flows import revert_cr78
    revert_cr78(monkeypatch)   # v11 CR-78 (the stamp of a held flow's stakes, flipped ON: a declared mover; unreverted this pin reads 3ef8bab1...), the same way
    # CP-T03-02 (`Event.ending` and the body Observation) and CR-85 (`faculty` for `history`) are declared movers of the
    # batch too, and each is read at its revert in process, as CR-87 and CP-T03-04 are (their own controls reproduce the
    # pre-item hashes); without them this pin read `be71a51c...` and never the PC-10b tree's.
    from .test_cp_t03_02_band_ending_and_body import revert_cp_t03_02
    from .test_cr85_faculty_replaces_history import revert_cr85
    revert_cp_t03_02(monkeypatch)
    revert_cr85(monkeypatch)
    from ..harness import populated as POP

    def season():
        w = POP.build_realm(0)
        w.fixtures = w.fixtures.sweep("odds_weighting", "none").sweep("choice_temperature", 0.1)
        POP.run(seasons=1, seed=0, w=w)
        return w

    w = season()
    # REM-31 re-pin (every fight deferred to ENCOUNTER; `the body`'s `step:`/`declares:` popped in process reads the old pair): was 60a80834... / 10323
    # REM-30 `verb_capability` rows re-pin (a DECLARED MOVER; the rows commit reverted in process reads the old pair): was 543e1e43... / 10421
    # v10 CP-T03-01 re-pin (the `individual` reads ride `Event.observed`; the log length does not move; the reads left off read 9c665fe8): was 9c665fe8...; CR-33 re-pin (NPC-088 holds `inquiry`; the log length does not move): was bd3d2492...; CR-20+CR-30 re-pin (Person repr, heritage rows; the log length does not move): was 1b7a72f4... (CR-86 re-pin: was bdff0832... / 10316)
    # v10 CP-T03-09 + PC-10b re-pin, B10-11 (the docstring's re-take): was edbc7442... / 10435 (CP-T03-09 alone: 2dec120f... / 10421)
    assert w.content_hash().startswith("b8ac6025"), w.content_hash()
    assert len(w.log) == 10869
    real = POP.resolvable_verbs
    monkeypatch.setattr(POP, "resolvable_verbs", lambda: frozenset(real()) - {"capture", "challenge", "accept"})
    c = season()
    assert (c.content_hash()[:8], len(c.log)) == ("a38516fb", 11505), (c.content_hash(), len(c.log))
    assert c.content_hash() != w.content_hash(), "withholding the batch's verbs moved nothing: the control observes nothing"
