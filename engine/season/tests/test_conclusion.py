"""B11.74 (`19_LACUNA_conclusion_is_a_committed_assertion.md` R-19-03; FRES §7 (3)): A PROPOSITION CARRIES ITS SUPPORT.

`utter` commits a conclusion (a `concluded:<kind>` cell, B11.73's deposit to its maker) and the act carries `cites`, the claim ids and
Record ids the utterer cited; `_eff_utter` stores them as `Proposition.support`, and a cite he does not hold is refused before anything is
written. `HOLDS` is the mood a conclusion is uttered in. No computed act forms `utter` with a cite (typed `utter` is B25's), so these plant
the act and fold it through the real driver.
"""
from __future__ import annotations

from ..data.verbs import VERB_TABLE

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..decision.choose import make_ranker
from ..decision.options import opening_set, record
from ..epistemic import Seen
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q
from ..state.carriers import Act, Claim, Question, Record, Tenure, View
from ..state.ids import draw_factory

UTTERER, OTHER = "p_low", "p_mid"
SUSPECT, VICTIM = "p_other", "p_king"
CELL = "concluded:person.died"
_CONTENT = {"terms": "prop_x", "to": (OTHER,), "from": UTTERER}


def _world():
    """A utterer who holds one claim of his own and one Record on a live `hold`; a second person holds a claim and a Record he does not."""
    w = P.tiny_world()
    w.persons[UTTERER].ledger.append(Claim("c_mine", UTTERER, VICTIM, "person.died", True, 0, "firsthand", 100, "own"))
    w.persons[OTHER].ledger.append(Claim("c_his", OTHER, VICTIM, "person.died", True, 0, "firsthand", 100, "own"))
    w.records["r_mine"] = Record("r_mine", "Hh", "petition", subject_matter=_CONTENT)
    w.records["r_his"] = Record("r_his", "Hh", "petition", subject_matter=_CONTENT)
    w.add_tenure(Tenure("t_hold_mine", UTTERER, "r_mine", "hold", since=0))
    w.add_tenure(Tenure("t_hold_his", OTHER, "r_his", "hold", since=0))
    return w


def _utter(w, aid: str, cites):
    """Fold one planted `utter` of the conclusion `(VICTIM, CELL, SUSPECT)` carrying `cites`; the Events the act caused."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    payload = {"proposition": f"prop_{aid}", "mood": "HOLDS", "subject": VICTIM, "predicate": CELL, "value": SUSPECT}
    if cites is not None:
        payload["cites"] = cites
    evs = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id=aid, actor=UTTERER, verb="utter", payload=payload)])
    return [e.kind for e in evs if e.causes and e.causes[0] == aid]


def test_a_conclusion_is_uttered_with_a_held_support():
    """A planted `utter` of the `concluded:` cell citing a claim and a Record he holds mints a Proposition whose `support` is exactly the cited
    ids, in the order cited; with no `cites` it is `()` (the control: the field is the act's, not a default made up). FALSIFIER: an effect that
    drops `cites` reads `()` on the first assert; one that stores the payload object reads a list, not a tuple, on the second."""
    w = _world()
    kinds = _utter(w, "u_held", ["c_mine", "r_mine"])
    assert "proposition.uttered" in kinds, kinds
    prop = w.propositions["prop_u_held"]
    assert prop.support == ("c_mine", "r_mine")
    assert isinstance(prop.support, tuple), "a Proposition is immutable: its support is a tuple, not the act's list"
    assert (prop.predicate, prop.value) == (CELL, SUSPECT)
    assert _utter(w, "u_bare", None) and w.propositions["prop_u_bare"].support == ()


def test_a_cite_the_utterer_does_not_hold_leaves_no_support():
    """A cite another person holds, and a cite nobody holds, each refuse the whole act at the fold: no Proposition, no `proposition.uttered`,
    no hold Tenure for the maker. The held-cite control in the same world is admitted, so the refusal observes the failure it excludes."""
    w = _world()
    for aid, cites in (("u_his_claim", ["c_mine", "c_his"]), ("u_his_record", ["r_his"]), ("u_nothing", ["c_nowhere"])):
        kinds = _utter(w, aid, cites)
        assert all(k in kinds for k in VERB_TABLE["utter"].emits_on_refusal) and "proposition.uttered" not in kinds, (aid, kinds)     # B21.16: `utter` refuses with its own kind
        assert f"prop_{aid}" not in w.propositions, aid
        assert not [t for t in w.persons[UTTERER].tenures if t.object == f"prop_{aid}"], aid
    assert "proposition.uttered" in _utter(w, "u_control", ["c_mine"])
    assert w.propositions["prop_u_control"].support == ("c_mine",)


# ======================================================================================
# B11.75 (`19_LACUNA_conclusion_is_a_committed_assertion.md` R-19-04, R-19-05; `proposals/v12_B11_a_conclusion_acted_on.md` §2): THE SUSPECT IS A CHOICE,
# AND `record` MAY PAIR A CONCLUDER.
# ======================================================================================
CONCLUDER, DEED, STRONG, WEAK = "p_low", "person.died", "p_other", "p_high"


def _two_suspects(strong_conf=90, weak_conf=30):
    """`tiny_world` where `p_low` holds two deaths of `p_king` (two seasons, so each sighting pairs with its own), the first seen to be done by `p_other` at
    `strong_conf`, the second by `p_high` at `weak_conf`: under `weigh_confidence` a claim weighs `confidence / confidence_default`, so the two suspects stand at
    support 0.9 and 0.3."""
    w = P.tiny_world()
    p = w.persons[CONCLUDER]
    stratum = next(iter(person_q._KIND_STRATA[DEED]))
    for n, (who, conf) in enumerate(((STRONG, strong_conf), (WEAK, weak_conf))):
        p.ledger.append(Claim(f"c_death{n}", p.id, VICTIM, DEED, True, n, "firsthand", conf, "own"))
        p.ledger.append(Claim(f"c_seen{n}", p.id, VICTIM, "seen", Seen(stratum=stratum, who=who), n, "firsthand", 100, "own"))
    return w, p


def _view(w, p):
    return View(p.id, [], w.fixtures.get("view_k"), Question("q_b1175", "claim_landed", (VICTIM,), ""))


def _reconstructs(w, p):
    v = _view(w, p)
    return [c for c in opening_set(p, v, v.question, w.fixtures) if c.verb == "reconstruct"]


def test_an_npc_names_the_weaker_suspect_in_a_share_strictly_between_0_and_half():
    """With a planted ledger naming two doers at support 0.9 and 0.3, an NPC concluder (the shipped chooser, a draw per seed) names the weaker in a share
    strictly between 0 and 1/2 over 200 seeds: the choice is a draw weighted by support (`choose.settle_conclusions`), so the less-supported suspect is
    sometimes named and never as often as the better supported. Each variant carries the claims that name him (`cites`). CONTROL in the same test: one
    suspect forms one Candidate carrying no rank (B11.73's act, unrenamed). FALSIFIER: a chooser that always takes the best-supported reads 0 weaker; one
    that ignores support reads about 1/2."""
    w, p = _two_suspects()
    cands = _reconstructs(w, p)
    assert {c.operands["concluded"][2]: c.operands["cites"] for c in cands} == {STRONG: ("c_death0",), WEAK: ("c_death1",)}, [c.operands for c in cands]
    solo, solo_p = _two_suspects()
    solo_p.ledger[:] = [c for c in solo_p.ledger if c.id in ("c_death0", "c_seen0")]
    (only,) = _reconstructs(solo, solo_p)
    assert only.operands["concluded"] == (VICTIM, DEED, STRONG) and "concluded_rank" not in only.operands, only.operands
    weaker = checked = 0
    for seed in range(200):
        rank = make_ranker(w.fixtures, verbs=frozenset({"reconstruct"}), draw=draw_factory(seed, lambda: 0))
        named = [c.operands["concluded"][2] for c in rank(p, _view(w, p))]
        assert len(named) == 1, (seed, named)      # one opportunity, one suspect: the other variant does not ride beside him
        checked += 1
        weaker += named[0] == WEAK
    assert checked >= 200 and 0 < weaker < checked / 2, (weaker, checked)


def _concluded_holder(w, told_doer, own_doer, teller="p_mid"):
    """`p_low` was told by `teller` that `told_doer` did the death of `p_king` (a told `concluded:` claim, the teller the last hop) and holds his own
    untold death of `p_king` with his own sighting naming `own_doer`."""
    stratum = next(iter(person_q._KIND_STRATA[DEED]))
    ledger = w.persons[CONCLUDER].ledger
    ledger.append(Claim("c_told_concl", CONCLUDER, VICTIM, f"concluded:{DEED}", told_doer, 0, "told_by", 100, "own", chain=(teller,)))
    ledger.append(Claim("c_own_death", CONCLUDER, VICTIM, DEED, True, 0, "firsthand", 100, "own"))
    ledger.append(Claim("c_own_seen", CONCLUDER, VICTIM, "seen", Seen(stratum=stratum, who=own_doer), 0, "firsthand", 100, "own"))


def test_record_re_grades_a_concluder_only_at_record_concluders_one():
    """`record_concluders` 1: a holder told a conclusion naming X by D, who then holds his own sighting naming Y of the same death, reads `record(p, D) < 1.0`;
    at 0 it reads 1.0 (the control: `told` admits cell predicates only). A holder whose own reading names the SAME doer reads above 1.0 at 1 (the pair
    agrees), and a holder who never held the conclusion reads 1.0 at both values (the pairing reads no ledger it may not). FALSIFIER: a build that leaves
    the told filter as it was reads 1.0 at 1; one that pairs another holder's ledger moves the never-held holder."""
    teller = "p_mid"
    wrong = P.tiny_world()
    _concluded_holder(wrong, STRONG, WEAK)
    wrong.persons["p_king"].ledger.append(Claim("c_k_death", "p_king", VICTIM, DEED, True, 0, "firsthand", 100, "own"))
    assert record(wrong.persons[CONCLUDER], teller, DEFAULT_FIXTURES.sweep("record_concluders", 0)) == 1.0, "the control reads no pair"
    assert record(wrong.persons[CONCLUDER], teller, DEFAULT_FIXTURES.sweep("record_concluders", 1)) < 1.0, "told one hand, he saw another: charged"
    for arm in (0, 1):
        assert record(wrong.persons["p_king"], teller, DEFAULT_FIXTURES.sweep("record_concluders", arm)) == 1.0, "never held the conclusion: unmoved"
    agreeing = P.tiny_world()
    _concluded_holder(agreeing, STRONG, STRONG)
    assert record(agreeing.persons[CONCLUDER], teller, DEFAULT_FIXTURES.sweep("record_concluders", 1)) > 1.0
    assert record(agreeing.persons[CONCLUDER], teller, DEFAULT_FIXTURES.sweep("record_concluders", 0)) == 1.0
