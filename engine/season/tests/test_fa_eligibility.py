"""B21.60 -- a seat is held by an individual (`16_PESSIMIST_FA_B` edit 1, G1; R-04 who may sit).
B21.62 -- a war has two parties and a declarer who can wage it (edit 4, G4; the test before the last, on the realm).
B21.63 -- joining a faction is answered by the faction (edit 3, G3; the last test, on the realm).

`state/gate.py::may_sit` is the one predicate: the person exists and is not a cohort. `confer`'s and `succeed`'s preconditions and
the write gate's `conferral` and `claim` clauses all ask it, so a cohort is refused at the fold (`confer.refused`) where the gate
would raise. Later positions of the item chain (B21.61 to B21.63) add their arms to this file.
"""
from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..boot.realm import build_realm
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries import faction_q, world_q
from ..state import gate
from ..loop.driver import mint_token
from ..loop.sides import seat_named_by, sides_of
from .. import manifest
from ..seam.wrappers import sigma
from ..state.carriers import Act, Office
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_g3_not_yours import _gov_world, _hold

pytestmark = pytest.mark.usefixtures("seat_at_success")   # B21.14: a conferral is resisted by a draw; the write, not the draw, is this file's

SEAT, CONFERRER, VIA, INDIVIDUAL, COHORT = "off_reeve", "p_king", "off_crown", "p_mid", "c_crowd"


def _confer(w, d, to, aid):
    act = Act(id=aid, actor=CONFERRER, verb="confer", payload={"office": SEAT, "to": to}, via=VIA)
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


def test_cohort_cannot_be_named_heir():
    """G1: the King confers a seat on a cohort (a person at `weight > 1`): `confer.refused`, nothing opened. CONTROL: the same
    act, same seat, same seat exercised, on an individual: `tenure.opened` and he holds it."""
    w, d = _gov_world()
    P.plant_cohort(w, COHORT, "S", weight=3)
    assert w.persons[COHORT].is_cohort and not w.persons[INDIVIDUAL].is_cohort, "fixture: no cohort beside an individual"
    kinds = _confer(w, d, COHORT, "elig_cohort")
    assert "confer.bad_conferee" in kinds and "tenure.opened" not in kinds, kinds      # B21.80: the `conferee` clause's kind
    assert _hold(w, SEAT) is None, "a cohort was seated"
    kinds = _confer(w, d, INDIVIDUAL, "elig_person")
    assert "tenure.opened" in kinds and "confer.refused" not in kinds, kinds
    assert _hold(w, SEAT).subject == INDIVIDUAL, "the control: an individual conferee was not admitted"


CHURCH_SEAT = "off_confessor"


def _church_world():
    """`_gov_world` plus `off_confessor`, an unheld seat of the Church at `S` (the King's `off_crown` is Crown's)."""
    w, d = _gov_world()
    w.offices[CHURCH_SEAT] = Office(CHURCH_SEAT, "Confessor", "S", ["issue"], faction="Church of Solmund", conferral="appointed",
                                    revocation=w.offices[SEAT].revocation)
    assert w.offices[VIA].faction != w.offices[CHURCH_SEAT].faction and w.offices[VIA].faction == w.offices[SEAT].faction, "fixture"
    return w, d


def _confer_on(w, d, seat, to, aid):
    act = Act(id=aid, actor=CONFERRER, verb="confer", payload={"office": seat, "to": to}, via=VIA)
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


def _confer_terms(w, seat, to):
    """The obstacle terms of the roll the fold would deal for the King conferring `seat` on `to`: the fold's own derivation (`sides_of`,
    `seat_named_by`, the prize row's hearing) into `sigma.contest_input`, composed by the registered obstacle owner."""
    act = Act(id="elig_terms", actor=CONFERRER, verb="confer", payload={"office": seat, "to": to}, via=VIA)
    prize = VERB_TABLE["confer"].contests
    parties, subject, rung = sides_of(w, act, to, prize)
    row = manifest.resolve("contest", prize)
    inp = sigma.contest_input(w, parties, verb="confer", subject=subject, room=rung, via=VIA, heard_by=row["heard_by"],
                              seat=seat_named_by(w, act, prize))
    return dict(sigma._composed_terms(inp))


def test_cross_chain_term_reads_zero_at_control():
    """A `confer` across factions composes an obstacle that lists no `cross_chain` term at `cross_chain_step` 0 (the control, shipped: the
    obstacle of every `confer` is the one it had) and one step at 1; a `confer` inside one chain lists none at either."""
    w, _ = _church_world()
    shipped = w.fixtures
    assert shipped.get("cross_chain_step") == 0, "the shipped step is the control"
    assert "cross_chain" not in _confer_terms(w, CHURCH_SEAT, INDIVIDUAL), "a term listed at the control"
    w.fixtures = shipped.sweep("cross_chain_step", 1)
    across, within = _confer_terms(w, CHURCH_SEAT, INDIVIDUAL), _confer_terms(w, SEAT, INDIVIDUAL)
    assert across["cross_chain"] == 1.0, across
    assert "cross_chain" not in within, "a conferral inside one chain was priced"
    assert {k: v for k, v in across.items() if k != "cross_chain"} == within, "the step moved a term other than its own"


def test_self_conferral_across_chains_refused():
    """G2: the King (`off_crown`, a Crown seat) confers an unheld seat of another faction (`off_confessor`, the Church's) on
    HIMSELF: `confer.refused`, nothing opened. CONTROL: he confers a seat of his own chain (`off_reeve`, Crown) on himself --
    admitted as today -- and the same Church seat on another person is admitted too (the rule is about the conferrer's own chain)."""
    w, d = _church_world()
    kinds = _confer_on(w, d, CHURCH_SEAT, CONFERRER, "elig_self_across")
    assert "confer.across_chains" in kinds and "tenure.opened" not in kinds, kinds      # B21.80: the `self_across_chains` clause's kind
    assert _hold(w, CHURCH_SEAT) is None, "he seated himself across chains"
    kinds = _confer_on(w, d, CHURCH_SEAT, INDIVIDUAL, "elig_other_across")
    assert "tenure.opened" in kinds and _hold(w, CHURCH_SEAT).subject == INDIVIDUAL, kinds
    kinds = _confer_on(w, d, SEAT, CONFERRER, "elig_self_within")
    assert "tenure.opened" in kinds and "confer.refused" not in kinds, kinds
    assert _hold(w, SEAT).subject == CONFERRER, "the control: a self-conferral inside one chain was not admitted"


HAFENMARK, VARFELL = "fac_hafenmark", "fac_varfell"


def _utter_war(w, d, actor, subject, value, aid):
    act = Act(id=aid, actor=actor, verb="utter", payload={"mood": "WAR", "subject": subject, "value": value})
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))]


def _wars(w):
    return [p for p in w.propositions.values() if p.mood == world_q.WAR_MOOD]


def _hafenmark_cast(w):
    """The Duchess (a Hafenmark member whose seat grants `dispatch`), a clerk (a Hafenmark member whose seat does not), and a stranger (no
    commit to Hafenmark or Varfell, no seat), each CHOSEN off the world's own `members` and grants, and a planted cohort."""
    ours = world_q.members(w, HAFENMARK)
    duchess = next(p for p in ours if gate.may_wage(w, p, HAFENMARK))
    clerk = next(p for p in ours if not gate.may_wage(w, p, HAFENMARK) and any(
        t.kind == "hold" and t.live and t.object in w.offices for t in w.persons[p].tenures))
    sides = set(ours) | set(world_q.members(w, VARFELL))
    stranger = next(p for p in sorted(w.persons) if p not in sides and not w.persons[p].is_cohort and not any(
        t.kind == "hold" and t.live and t.object in w.offices for t in w.persons[p].tenures))
    cohort = P.plant_cohort(w, "c_war_crowd", next(iter(w.rungs)), weight=3)
    assert w.persons[cohort].is_cohort and len({duchess, clerk, stranger, cohort}) == 4, "fixture: four distinct declarers"
    return duchess, clerk, stranger, cohort


def test_war_between_same_faction_refused():
    """G4: `WAR(Hafenmark, Hafenmark)` by the Duchess is refused (`utter.refused`), no Proposition minted and no war read. CONTROL: the Duchess's
    `WAR(Hafenmark, Varfell)` mints, so only the party pair decides."""
    w = build_realm(0)
    d = SeasonDriver(w)
    duchess, *_ = _hafenmark_cast(w)
    kinds = _utter_war(w, d, duchess, HAFENMARK, HAFENMARK, "elig_war_self")
    assert kinds == ["utter.refused"], kinds
    assert not _wars(w) and faction_q.at_war(w, HAFENMARK, HAFENMARK) is False, "a faction was set against itself"
    assert _utter_war(w, d, duchess, HAFENMARK, VARFELL, "elig_war_two") == ["proposition.uttered"], "the control: two parties did not mint"
    assert len(_wars(w)) == 1


def test_war_utterance_without_a_waging_seat_is_not_a_declaration():
    """G4: a cohort's, a stranger's and a clerk's `WAR` between Hafenmark and Varfell is refused; the Duchess's mints. The same stranger's
    utterance of another mood is admitted (a call for war is an ordinary utterance)."""
    w = build_realm(0)
    d = SeasonDriver(w)
    duchess, clerk, stranger, cohort = _hafenmark_cast(w)
    for who in (cohort, stranger, clerk):
        assert _utter_war(w, d, who, HAFENMARK, VARFELL, f"elig_war_{who}") == ["utter.refused"], who
    assert not _wars(w), "a refused utterance minted a WAR Proposition"
    ordinary = Act(id="elig_ordinary", actor=stranger, verb="utter", payload={"mood": "OUGHT", "subject": HAFENMARK, "value": VARFELL})
    assert [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [ordinary])] == ["proposition.uttered"], "another mood was refused"
    assert _utter_war(w, d, duchess, HAFENMARK, VARFELL, "elig_war_duchess") == ["proposition.uttered"], "the control: the Duchess's war"
    assert len(_wars(w)) == 1 and _wars(w)[0].subject == HAFENMARK


RESTORATION = "fac_restoration_movement"


def _do(w, d, actor, verb, payload, aid):
    act = Act(id=aid, actor=actor, verb=verb, payload=payload)
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))]


def _admission(w, d, who, joiner, tag):
    """`who` utters an `OUGHT` naming `joiner` and the Restoration Movement, then commits to it -- the admission, as a member makes it."""
    said = _do(w, d, who, "utter", {"mood": "OUGHT", "subject": joiner, "value": RESTORATION}, f"elig_{tag}")
    return said + _do(w, d, who, "commit", {"subject": f"prop:elig_{tag}"}, f"elig_{tag}_c")


def test_non_member_commit_refused_without_admission():
    """G3: the King's `commit` to the Restoration Movement with no admission is refused (`commitment.refused`); a rank-and-file member's
    admission does not stand (an admission is an `OUGHT` naming him and the faction, `commit`ted to by a member WHO MAY ADMIT: the head seat's
    holder or a seat that confers), the leader's does: `commitment.made`. The default is incompatible: a man who still belongs to Valorsmark
    is refused whatever stands, and is admitted once he leaves (his own `release`). CONTROL: a member's re-commit and a `commit` to a
    Proposition that is no faction's are unchanged."""
    w = build_realm(0)
    d = SeasonDriver(w)
    king = next(p for p in w.persons if any(t.kind == "hold" and t.live and t.object == "off_king" for t in w.persons[p].tenures))
    ours = world_q.members(w, RESTORATION)
    admitter = next(p for p in ours if gate.may_admit(w, p, RESTORATION))
    rank_and_file = next(p for p in ours if not gate.may_admit(w, p, RESTORATION))
    liege = next(p for p in world_q.members(w, "fac_valorsmark") if p != king and p not in ours)   # a Valorsmark man who joins no faction else
    assert king not in ours and {king, liege} <= set(world_q.members(w, "fac_valorsmark")), "fixture"

    def joins(who):
        return who in world_q.members(w, RESTORATION)

    # the King leaves Valorsmark by his own release, so the default pair no longer stands between him and the Movement
    assert "commitment.ended" in _do(w, d, king, "release", {"subject": "fac_valorsmark"}, "elig_leave")
    assert _do(w, d, king, "commit", {"subject": RESTORATION}, "elig_join_bare") == ["commitment.refused"] and not joins(king)
    assert _admission(w, d, rank_and_file, king, "weak") == ["proposition.uttered", "commitment.made"]
    assert not world_q.admission_stands(w, king, RESTORATION), "a rank-and-file member's admission stood"
    assert _do(w, d, king, "commit", {"subject": RESTORATION}, "elig_join_weak") == ["commitment.refused"] and not joins(king)
    assert _admission(w, d, admitter, king, "strong") == ["proposition.uttered", "commitment.made"]
    assert _do(w, d, king, "commit", {"subject": RESTORATION}, "elig_join") == ["commitment.made"] and joins(king), "the admitted man was refused"
    # a standing admission serves nobody who still belongs to an incompatible faction
    assert _admission(w, d, admitter, liege, "liege") == ["proposition.uttered", "commitment.made"]
    assert world_q.admission_stands(w, liege, RESTORATION), "the admission did not stand"
    assert _do(w, d, liege, "commit", {"subject": RESTORATION}, "elig_join_incompat") == ["commitment.refused"] and not joins(liege)
    assert "commitment.ended" in _do(w, d, liege, "release", {"subject": "fac_valorsmark"}, "elig_leave_liege")
    assert _do(w, d, liege, "commit", {"subject": RESTORATION}, "elig_join_liege") == ["commitment.made"] and joins(liege)
    # CONTROL: a member's re-commit is no joining, and a `commit` to a Proposition no faction owns is asked of nobody
    assert _do(w, d, admitter, "commit", {"subject": RESTORATION}, "elig_recommit") == ["commitment.made"]
    assert _do(w, d, king, "commit", {"subject": "prop:elig_weak"}, "elig_plain") == ["commitment.made"], \
        "a commit to a non-faction Proposition was asked an admission"
