"""v10 IN-45 (ii) (B10-06; M5 option (B)): `queries/world_q.py::works_sites` -- THE CHANNEL FROM A HELD WORKS TO THE
FABRIC `work` RAISES, one named term of REM-21's splice in `questions_for`.

WHY THE TERM EXISTS. After (i) (`venues.yaml: planned_works`) the masters hold a works Record and `found`/`build` form on
it, but `work` declares `referent_class: Site` and forms on a Site-classed referent only, and no question a master answers
is about the fabric his works names: `work` was formed for nobody (`aperture 4 s`, realm: formed 0). The term stamps, on
the question he answers, the Sites standing at his works' `at` rung of its `plan` kind -- `ceiling`'s own match.

THE FALSIFIERS AND THE CONTROL, each asked of the real splice, the real `opening_set`, the real fold and MATTER:
  * the term: the Steward (the dwelling works' master) is handed the Court's dwelling Site, the Duke (a `hearth` plan,
    a Rung kind that names no Site) and a stranger are handed none, and the built dwelling joins once `build` stands it.
  * the channel: the Site rides the Steward's question as `Site`-classed and `work` (and `restore`, the shared class)
    forms on it. CONTROL: with the term dropped he forms neither -- the pre-(ii) reading.
  * the residue, named: the shipped `dwelling` plan names a kind with no registered band floors (`band_floors.dwelling`
    is `{}` on purpose, `24d-i`), so `work`'s `floor` read is UNKNOWN and the fold refuses every `work` on a dwelling
    (`work.unavailable`), formed or not. The term is the channel; the cell is a second link.
  * execution: the same chain on a plan whose kind HAS band floors executes -- a `seam` works at the Court: `build`
    stands it at condition 0, MATTER ripens a term, and since a fabric at 0 clears no band floor (`work`'s cell:
    `condition >= floor`) the Steward first `restore`s it (no floor; the same `_rise`) until it clears, then `work`
    through the real fold raises it toward the ceiling (`site.worked`).
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.choose import _payload_of
from ..decision.options import opening_set, seat_of
from ..harness import populated as POP
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Act
from .test_in45_planned_works import _build, _fold, _kinds, _rows, _tick0

STEWARD, DUKE, STRANGER = "p_npc_009", "p_npc_020", "p_npc_030"
DWELLING_WORKS, SEAM_WORKS = "works_dwelling_court", "works_seam_court"
COURT_DWELLING, COURT_SEAM = "s_s_001_court_dwelling", "s_s_001_seam"
BUILT_DWELLING, BUILT_SEAM = f"dwelling:{DWELLING_WORKS}", f"seam:{SEAM_WORKS}"
#: a probe row beside the shipped two: a `seam` (a kind WITH band floors) planned at the Court, the Steward its master
SEAM_ROW = {"id": SEAM_WORKS, "kind": "works", "plan": "seam", "at": {"hearth": "S-001:court"},
            "rung": {"settlement": "S-001"}, "master": "off_lord_steward", "terms": 3}


def _formed(w, pid):
    """The first question `questions_for` hands `pid`, and the Candidates he forms on it."""
    p = w.persons[pid]
    q = world_q.questions_for(w, p)[0]
    return q, opening_set(p, assemble(p, q, 12), q, w.fixtures)


def _work_act(w, c, aid):
    """The act the chooser mints from Candidate `c` (`pack_scenes`: `_payload_of` and `seat_of`), the Steward's."""
    return Act(aid, STEWARD, c.verb, payload=_payload_of(c), via=seat_of(w.persons[STEWARD], c))


def test_works_sites_names_the_fabric_a_held_works_plans_and_nothing_else():
    """The Steward holds the dwelling works at the Royal Court: the Court's one dwelling Site is the fabric it names.
    The Duke holds a `hearth` plan, a Rung kind, which names no Site; a person holding no works is handed none. Once
    `build` stands the works' dwelling it joins the Steward's set, sorted by id."""
    w = POP.build_realm(0)
    d = _tick0(w)
    assert world_q.works_sites(w, w.persons[STEWARD]) == (COURT_DWELLING,)
    assert world_q.works_sites(w, w.persons[DUKE]) == ()
    assert world_q.works_sites(w, w.persons[STRANGER]) == ()
    out = _fold(w, d, Act(id="b1", actor=STEWARD, verb="build", payload={"subject": DWELLING_WORKS}))
    assert _kinds(out) == ["site.built"], _kinds(out)
    assert world_q.works_sites(w, w.persons[STEWARD]) == (BUILT_DWELLING, COURT_DWELLING)


def test_the_site_rides_the_masters_question_and_work_forms_on_it_but_not_without_the_term(monkeypatch):
    """The Court dwelling is stamped on the Steward's question as `Site`-classed and `work` forms on it -- and `restore`,
    which declares the same class. CONTROL: the splice with `works_sites` returning nothing is the pre-(ii) question,
    on which neither forms (formed 0 in the realm); and the Duke, whose works names no Site, forms neither."""
    w = POP.build_realm(0)
    _tick0(w)
    q, formed = _formed(w, STEWARD)
    assert (COURT_DWELLING, "Site") in q.classes, q.classes
    on_site = {c.verb for c in formed if c.subject == COURT_DWELLING}
    assert {"work", "restore"} <= on_site, on_site
    assert not [c for c in _formed(w, DUKE)[1] if c.verb in ("work", "restore")]
    monkeypatch.setattr(world_q, "works_sites", lambda w_, p_: ())
    q0, formed0 = _formed(w, STEWARD)
    assert (COURT_DWELLING, "Site") not in q0.classes
    assert not [c for c in formed0 if c.verb in ("work", "restore")], [(c.verb, c.subject) for c in formed0]


def test_a_dwelling_works_forms_work_and_the_fold_refuses_it_for_want_of_band_floors():
    """THE NAMED RESIDUE: the term hands the Steward `work` on the built dwelling and on the Court's old one, and the fold
    refuses both -- `work`'s `floor` read has no band floors for a `dwelling` (`band_floors.dwelling` is `{}`), so the
    cell is UNKNOWN and not admitted, with the fabric untouched. A kind with floors does not share it (the next test)."""
    w = POP.build_realm(0)
    d = _tick0(w)
    _fold(w, d, Act(id="b1", actor=STEWARD, verb="build", payload={"subject": DWELLING_WORKS}))
    w.tick = 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert w.fixtures.get("band_floors")["dwelling"] == {}
    q, formed = _formed(w, STEWARD)
    for site in (BUILT_DWELLING, COURT_DWELLING):
        (c,) = [c for c in formed if c.verb == "work" and c.subject == site]
        act = _work_act(w, c, f"w_{site}")
        assert not d._admits(w, act, VERB_TABLE["work"])[0], site
        before = w.sites[site].condition
        assert _kinds(_fold(w, d, act)) == ["work.unavailable"] and w.sites[site].condition == before


def test_work_executes_through_the_fold_on_a_works_whose_kind_has_band_floors(monkeypatch):
    """THE CHAIN, folded by the real fold: a `seam` works planned at the Court (a probe row beside the shipped two), the
    Steward its master. He `build`s it (condition 0); MATTER ripens its first term (tick 1: the ceiling is a third of
    the scale); the `work` his own question forms on the built seam raises it by the works' rise (`_rise`: the headroom
    to the ceiling shared among those standing at the Court) -- `site.worked`. The Court's old, full-condition seam
    (its rung is the settlement, not the Court: not named) is not offered; the built one is the only fabric named."""
    w = _build(monkeypatch, _rows() + [SEAM_ROW])
    d = _tick0(w)
    assert world_q.works_sites(w, w.persons[STEWARD]) == (COURT_DWELLING,)       # the seam works names no Site yet
    assert _kinds(_fold(w, d, Act(id="b1", actor=STEWARD, verb="build", payload={"subject": SEAM_WORKS}))) \
        == ["site.built"]
    built = w.sites[BUILT_SEAM]
    assert (built.rung, built.condition) == ("b_s_001_court", 0)
    w.tick = 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert world_q.matured_terms(w, SEAM_WORKS) == 1
    scale = w.fixtures.get("condition_scale")
    ceiling = world_q.ceiling(w, built)
    assert ceiling == scale // 3
    num, den = world_q.share(w, built)
    floor = min(w.fixtures.get("band_floors")["seam"].values())
    q, formed = _formed(w, STEWARD)
    # A FABRIC AT CONDITION 0 CLEARS NO BAND FLOOR, so `work` (`condition >= floor`) is not admitted on a site `build` has
    # just stood; `restore` has no floor and is how a first course is raised -- both form on the built seam.
    (c,) = [c for c in formed if c.verb == "work" and c.subject == BUILT_SEAM]
    assert not d._admits(w, _work_act(w, c, "w0"), VERB_TABLE["work"])[0]
    (r,) = [c for c in formed if c.verb == "restore" and c.subject == BUILT_SEAM]
    assert _kinds(_fold(w, d, _work_act(w, r, "r1"))) == ["site.restored"]
    assert built.condition == (ceiling * num) // den
    assert _kinds(_fold(w, d, _work_act(w, r, "r2"))) == ["site.restored"] and built.condition >= floor
    # NOW IT CLEARS THE FLOOR AND `work` EXECUTES, raising the fabric toward the ripened term's ceiling.
    before = built.condition
    assert d._admits(w, _work_act(w, c, "w1"), VERB_TABLE["work"])[0]
    assert _kinds(_fold(w, d, _work_act(w, c, "w1"))) == ["site.worked"]
    assert before < built.condition <= ceiling, (before, built.condition, ceiling)
    assert not [c for c in formed if c.verb == "work" and c.subject == COURT_SEAM]
