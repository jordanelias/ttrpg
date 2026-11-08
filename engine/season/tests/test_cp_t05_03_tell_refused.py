"""v10 CP-T05-03 (batch B10-13; home T05 §2 CP-T05-03, `-08` AM-D-04): A FAILED TELLING IS REALISED.

`tell`'s `emits_on_refusal` names `tell.refused`; the Failure band keeps `news.untold` on `emits:` alone. The loop
counts an act realised when none of its Events is on the row's `emits_on_refusal` (`loop/driver.py`), and
`loop/deliberate.py::_drop_what_was_already_done` drops a realised opportunity until the next season. So a LOST
telling (the contest ran and went against the teller) stops re-forming within the season, as a lost `argue` does,
and a REFUSED one (an absent hearer) still re-forms, because a later round's world may have made its precondition
true.

  * FALSIFIER: one teller, one claim, one present hearer, the roll forced to Failure: the telling is attempted once
    in the season. CONTROL: an absent hearer is refused as `tell.refused` and the same Candidate is formed again in
    a later round (the refusal is not realised).
  * PLANTED FAILURE (run 2026-11-08, reverted): the row's refusal kind put back to `news.untold` (`revert_cp_t05_03`)
    -- the lost telling re-forms every round and the first test reds on its own count. That arm is also run in the
    suite, as the control that the count can see a re-formation.
  * THE CONSEQUENCE STATED: `news.untold` is no longer a refusal kind, so a claim of it is a deed (`is_deed`), valued
    by `tell`'s alignment as `argument.lost` is by `argue`'s; `tell.refused` is no deed.
"""
from __future__ import annotations

import dataclasses

from ..data import verbs as _verbs
from ..data.verbs import DEED_KINDS, KIND_VERB, REFUSAL_KINDS, VERB_TABLE
from ..harness import probes as P
from ..harness.play_surface import dispatching_chooser
from ..loop.driver import SeasonDriver
from ..manifest import MODULE_ENTRIES
from ..queries import person_q as PQ
from ..queries import world_q
from ..queries.inputs import Margin
from ..queries.person_q import said_of
from ..state.carriers import Act, Claim, Scene
from ..state.ids import H

TELLER, SUBJECT = "p_low", "Hh"
PRESENT, ABSENT = "p_mid", "p_king"          # `p_mid` stands in `Hh` with the teller; `p_king` in `R`


def revert_cp_t05_03(monkeypatch):
    """The split OFF, in process: `tell`'s every refusal is `news.untold` again (the one kind both the refusal and
    the lost telling shared), so a lost telling is a refusal and is not realised. Other tests that pin a pre-item
    trajectory call it."""
    row = VERB_TABLE["tell"]
    monkeypatch.setitem(VERB_TABLE, "tell", dataclasses.replace(
        row, emits_on_refusal=("news.untold",),
        refusals_by_clause={k: ("news.untold",) for k in row.refusals_by_clause}))
    # the two sets derived from the table at import (`is_deed` reads them), and `world_q`'s by-value import of one
    refusal = (REFUSAL_KINDS - {"tell.refused"}) | {"news.untold"}
    deeds = DEED_KINDS - {"news.untold"}
    monkeypatch.setattr(_verbs, "REFUSAL_KINDS", refusal)
    monkeypatch.setattr(_verbs, "DEED_KINDS", deeds)
    monkeypatch.setattr(world_q, "DEED_KINDS", deeds)


def _season(monkeypatch, hearer, degree_net):
    """One season in which the teller is handed the SAME `tell` of his one claim to `hearer` every time he is
    asked, and nobody else chooses anything; the contest is forced to `degree_net` against obstacle 2. Returns
    the world and the `tell` Events in log order."""
    w = P.tiny_world()
    d = SeasonDriver(w)                  # constructed first: the registrar fills the module table
    w.persons[TELLER].ledger.append(
        Claim("c_held", TELLER, SUBJECT, "stores:grain", 8, 0, "firsthand", 80, "own"))
    said = said_of(w.persons[TELLER].ledger, SUBJECT, w.fixtures)
    real = MODULE_ENTRIES["social_contest.roll"]
    monkeypatch.setitem(MODULE_ENTRIES, "social_contest.roll", dataclasses.replace(
        real, fn=lambda inp, rng: Margin(net=degree_net, ob=2)))
    asked: list = []

    def tell(p, v, s, ask_budget, auto):
        asked.append(1)
        aid = H(w.world_seed, w.tick, p.id, f"act:tell:{SUBJECT}:{hearer}")
        return [Scene(H(w.world_seed, w.tick, p.id, f"scene:cp_t05_03:{len(asked)}"), p.id,
                      [Act(aid, p.id, "tell", payload={"subject": SUBJECT, "to": hearer, "said": said})])]

    d.season(dispatching_chooser(P.NOCHOOSE, {TELLER: tell}), question=None,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert len(asked) >= 2, f"the teller was asked {len(asked)} time(s): the control cannot see a re-formation"
    return w, [e for e in w.log if e.kind in ("news.told", "news.untold", "tell.refused")]


def test_a_lost_telling_is_not_formed_again_in_the_season(monkeypatch):
    w, evs = _season(monkeypatch, PRESENT, 0)
    assert [(e.kind, e.degree) for e in evs] == [("news.untold", "Failure")], [(e.kind, e.degree) for e in evs]


def test_the_control_with_the_split_off_the_lost_telling_is_retried_each_round(monkeypatch):
    revert_cp_t05_03(monkeypatch)
    w, evs = _season(monkeypatch, PRESENT, 0)
    assert len(evs) >= 2 and {e.kind for e in evs} == {"news.untold"}, [(e.kind, e.degree) for e in evs]


def test_a_refused_telling_to_an_absent_hearer_is_refused_and_re_forms_next_round(monkeypatch):
    w, evs = _season(monkeypatch, ABSENT, 0)
    assert len(evs) >= 2, [(e.kind, e.degree) for e in evs]
    assert {e.kind for e in evs} == {"tell.refused"} and all(e.degree is None for e in evs), evs


def test_a_won_telling_is_unchanged_and_realised(monkeypatch):
    w, evs = _season(monkeypatch, PRESENT, 3)
    assert [e.kind for e in evs] == ["news.told"], [(e.kind, e.degree) for e in evs]


def test_the_kinds_the_split_declares():
    row = VERB_TABLE["tell"]
    assert set(row.emits_on_refusal) == {"tell.refused"}, row.emits_on_refusal
    assert tuple(row.emits_by_degree["Failure"]) == ("news.untold",), row.emits_by_degree
    assert KIND_VERB["tell.refused"] == "tell" and KIND_VERB["news.untold"] == "tell"
    assert "tell.refused" in REFUSAL_KINDS and "news.untold" not in REFUSAL_KINDS
    assert "news.untold" in DEED_KINDS and "tell.refused" not in DEED_KINDS
    refused = Claim("c_ref", "p_other", TELLER, "tell.refused", True, 0, "firsthand", 100, "own")
    lost = dataclasses.replace(refused, id="c_lost", predicate="news.untold")
    assert not PQ.is_deed(refused) and PQ.is_deed(lost)
