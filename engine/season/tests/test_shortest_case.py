"""B11.72 (`08_FI_07` §2 (a), FRES §2 row 8): `examine` FORMS ON A PLACE HE HAS HEARD OF.

`examine` is classed on a Site (`verb_table.yaml`) and no question the realm delivers carries a Site among its referents, so it formed
nowhere. Its `site` is now choice-sourced (`rosters.yaml: choice_sourced`, `ledger_ranges`): the range is the ids his OWN ledger presents as a
Site, read person-side with no World. Whether he stands there is the fold's (`present_at`), and a man who does not is refused.
"""
from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..decision.options import opening_set
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..seam import Resolution
from ..state.carriers import Act, Claim, Question, View

HEARD, NOT_A_SITE = "site_harbour", "Hh"      # `tiny_world`: a Site in `S`; a hearth. `p_low` stands in `Hh`, not at the harbour.


def _examines(w, pid="p_low"):
    p = w.persons[pid]
    q = Question("q_b1172", "claim_landed", ("p_mid",), "")
    return [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures) if c.verb == "examine"]


def test_examine_forms_on_a_site_he_has_heard_of():
    """§2 (a): "a planted investigator who holds a claim about a Site and stands elsewhere forms it and is refused". He holds one firsthand reading
    of the harbour's condition and one of a hearth's grain, and stands at the hearth: `examine` is offered on the harbour alone (the hearth is no
    Site his claims present), carries it as `site`, and the fold refuses it on `present_at` with the row's one kind. FALSIFIER: the bag naming a
    place he is not at is the CP-T06-04 presence-aware decline's case, not this range's. CONTROL: with no claim about a Site he forms none."""
    w = P.tiny_world()
    assert _examines(w) == [], "control: a man who has heard of no Site forms no `examine`"
    p = w.persons["p_low"]
    p.ledger.append(Claim("c_site", p.id, HEARD, "condition", 1, 0, "firsthand", 80, "own"))
    p.ledger.append(Claim("c_hearth", p.id, NOT_A_SITE, "stores:grain", 8, 0, "firsthand", 80, "own"))
    got = _examines(w)
    assert [(c.subject, c.operands.get("site")) for c in got] == [(HEARD, HEARD)], got
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    act = Act(id="a_examine", actor=p.id, verb="examine", payload={"subject": HEARD, **got[0].operands})
    w.acts.append(act)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution("Success", {}))
    assert [e.kind for e in out] == ["inquiry.refused"], [e.kind for e in out]
