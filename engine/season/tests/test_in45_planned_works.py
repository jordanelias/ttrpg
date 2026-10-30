"""v10 IN-45 (B10-06; M5 taken, option (B)): WORKS AUTHORED AS WORLD DATA -- `venues.yaml: planned_works`,
minted by `harness/populated.py::mint_planned_works` at the end of `build_realm`.

WHY THE BLOCK EXISTS. A works is a `Record` of kind `works`, and in computed play nobody declares one
(`create_record` is untyped and mints `text`, which `found`, `build` and `work` never name), so before the block
`found` and `build` formed for nobody and `work` stayed refused. The reader mints each row through
`EFFECTS["create_record"]` -- the effect a master's own act runs -- so a planned works is the Record a declaring act
would leave at tick 0, and no operand is coined (the act carries only keys `create_record` already reads).

THE FALSIFIERS AND THE CONTROL, each asked of the real builder, the real fold and the real MATTER barrier:
  * the control: the realm built with an EMPTY block differs from the shipped realm by exactly the rows' Records and
    their masters' `hold` edges -- and by nothing else (no person, rung, site, office or other tenure moved).
  * the rows are what `found` and `build` take: folded through the real gate, the Duke's `found` of his works makes
    a hearth under Auerheim and the Steward's `build` stands a dwelling at the Royal Court at condition 0; a person
    who is not the master is refused on the same works.
  * the planted failure: the SAME rows authored `kind: text` mint Records neither verb can name -- the master holds
    no works, `works_for` finds none, and `found`/`build` form for nobody (the realm-level run of the same plant is
    `aperture 4 0`'s, recorded in the commit).
  * MATTER ripens a planned works's terms with `ROOT` as their cause: a Record minted without a fold has no
    `record.created` Event and no act in the act store to name, and a stage naming its own id as winder is an
    unresolvable cause the gate refuses (seen red when the winder was the row id).
  * every refusal the reader owns, each one clause from a row that mints.
"""

from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..gaps import Unspecified
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Act
from ..state.ids import ROOT

HEARTH_WORKS, DWELLING_WORKS = "works_hearth_auerheim", "works_dwelling_court"
DUKE, STEWARD = "p_npc_020", "p_npc_009"          # off_duke_valorsmark's holder; off_lord_steward's


def _rows(*mutations):
    """The shipped `planned_works` rows, each passed through `mutations` (callables `row -> row`)."""
    out = []
    for row in POP._load(POP.VENUES)["planned_works"]:
        for m in mutations:
            row = m(row)
        out.append(row)
    return out


def _build(monkeypatch, rows):
    """`build_realm(0)` with the venues file's `planned_works` replaced by `rows` (`[]` is the control arm)."""
    real = POP._load

    def load(rel):
        d = real(rel)
        return {**d, "planned_works": rows} if rel == POP.VENUES else d
    monkeypatch.setattr(POP, "_load", load)
    return POP.build_realm(0)


def _tick0(w):
    """The realm's tick-0 MATTER barrier -- the first yield, which stocks the settlements the works pay from."""
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


# ======================================================================================
# 1 -- THE SHIPPED BLOCK, AND ITS CONTROL
# ======================================================================================

def test_the_shipped_rows_mint_one_works_each_held_by_the_seat_they_name(monkeypatch):
    """The two shipped rows are a `hearth` plan at Auerheim (S-002) and a `dwelling` plan at the Royal Court
    (`b_s_001_court`): each is a `works` Record `{plan, at}` with `at` resolved from its anchor, kept at the
    paying rung, three terms from tick 1 (`record_stage_term`), and held by the person who holds the seat the
    row names -- the maker's `hold`, which is what makes him the master `found` and `build` ask for."""
    w = POP.build_realm(0)
    works = {r.id: r for r in w.records.values() if r.kind == world_q.WORKS_KIND}
    assert sorted(works) == [DWELLING_WORKS, HEARTH_WORKS], sorted(works)
    hearth, dwelling = works[HEARTH_WORKS], works[DWELLING_WORKS]
    assert hearth.subject_matter == {"plan": "hearth", "at": "set_s_002"} and hearth.rung == "set_s_002"
    assert dwelling.subject_matter == {"plan": "dwelling", "at": "b_s_001_court"} and dwelling.rung == "set_s_001"
    assert [s[:2] for s in hearth.stages] == [(1, "term1"), (2, "term2"), (3, "term3")]
    assert world_q.hold_force(w, HEARTH_WORKS).subject == DUKE
    assert world_q.hold_force(w, DWELLING_WORKS).subject == STEWARD
    assert w.offices["off_duke_valorsmark"] in [w.offices[t.object] for t in w.tenures
                                                if t.kind == "hold" and t.live and t.subject == DUKE
                                                and t.object in w.offices]
    assert [r.id for r in world_q.works_for(w, "b_s_001_court", "dwelling")] == [DWELLING_WORKS]
    assert [r.id for r in world_q.works_for(w, "set_s_002", "hearth")] == [HEARTH_WORKS]


def test_control_an_empty_block_changes_nothing_but_the_rows_records_and_their_holds(monkeypatch):
    """THE CONTROL: with `planned_works: []` the realm is the realm before the block (the base
    `build_realm(0).content_hash()`, read in the commit); against it the shipped realm gains EXACTLY the two
    Records and the two `hold` edges on them -- no person, rung, site, office, proposition or other tenure
    moved, and the content hash differs."""
    control = _build(monkeypatch, [])
    monkeypatch.undo()
    shipped = POP.build_realm(0)
    assert not [r for r in control.records.values() if r.kind == world_q.WORKS_KIND]
    assert sorted(set(shipped.records) - set(control.records)) == [DWELLING_WORKS, HEARTH_WORKS]
    assert set(control.records) <= set(shipped.records)
    for store in ("persons", "rungs", "sites", "offices", "propositions"):
        assert sorted(getattr(shipped, store)) == sorted(getattr(control, store)), store
    new = [t for t in shipped.tenures if t.id not in {c.id for c in control.tenures}]
    assert sorted((t.object, t.kind, t.subject) for t in new) == [
        (DWELLING_WORKS, "hold", STEWARD), (HEARTH_WORKS, "hold", DUKE)], new
    assert len(shipped.tenures) == len(control.tenures) + 2
    assert control.content_hash() != shipped.content_hash()


def test_the_hearth_anchor_names_a_building_by_its_settlement_and_slug_and_a_ghost_refuses():
    """The fifth anchor form (`{hearth: "<code>:<slug>"}`) is one more line at the building mint site: the
    resolver is unchanged, resolves the Royal Court, and still refuses what is not indexed."""
    w = POP.build_realm(0)
    assert POP.resolve_anchor(w, w._anchors, {"hearth": "S-001:court"}) == "b_s_001_court"
    assert POP.resolve_anchor(w, w._anchors, {"settlement": "S-001"}) == "set_s_001"
    for ghost in ({"hearth": "S-001:no_such_building"}, {"hearth": "b_s_001_court"}):
        with pytest.raises(Unspecified):
            POP.resolve_anchor(w, w._anchors, ghost, "a probe")


# ======================================================================================
# 2 -- THE ROWS ARE WHAT `found` AND `build` TAKE (THE REAL FOLD, THE REAL GATE)
# ======================================================================================

def test_the_masters_found_and_build_execute_on_the_planned_works_and_a_stranger_is_refused():
    """After the tick-0 yield the paying settlements hold the stake and the timber. The Duke's `found` of
    his works makes a `hearth` Rung under Auerheim (`rung.founded`, his `hold` on it, the grain staked out of
    `set_s_002`); the Steward's `build` stands a `dwelling` Site at the Royal Court at condition 0 (`site.built`,
    the timber consumed out of `set_s_001`). CONTROL: the Steward is not the hearth works' master, the Duke is
    not the dwelling works' -- each is refused on the other's works, and nothing is made."""
    w = POP.build_realm(0)
    d = _tick0(w)
    assert w.rungs["set_s_002"].stores.get("grain", 0) >= 10 and w.rungs["set_s_001"].stores.get("timber", 0) >= 10
    rungs, sites = len(w.rungs), len(w.sites)
    assert _kinds(_fold(w, d, Act(id="x1", actor=STEWARD, verb="found", payload={"subject": HEARTH_WORKS}))) \
        == ["found.refused"]
    assert _kinds(_fold(w, d, Act(id="x2", actor=DUKE, verb="build", payload={"subject": DWELLING_WORKS}))) \
        == ["build.refused"]
    assert (len(w.rungs), len(w.sites)) == (rungs, sites)
    grain = w.rungs["set_s_002"].stores["grain"]
    out = _fold(w, d, Act(id="f1", actor=DUKE, verb="found", payload={"subject": HEARTH_WORKS}))
    assert _kinds(out) == ["rung.founded"], _kinds(out)
    founded = w.rungs[f"hearth:{HEARTH_WORKS}"]
    assert founded.kind == "hearth" and founded.stores.get("grain") == 10
    assert w.rungs["set_s_002"].stores["grain"] == grain - 10
    assert world_q.hold_force(w, founded.id).subject == DUKE
    timber = w.rungs["set_s_001"].stores["timber"]
    out = _fold(w, d, Act(id="b1", actor=STEWARD, verb="build", payload={"subject": DWELLING_WORKS}))
    assert _kinds(out) == ["site.built"], _kinds(out)
    built = w.sites[f"dwelling:{DWELLING_WORKS}"]
    assert (built.rung, built.kind, built.condition) == ("b_s_001_court", "dwelling", 0)
    assert w.rungs["set_s_001"].stores["timber"] == timber - 10


def test_matter_ripens_a_planned_works_terms_with_root_as_their_cause():
    """A Record minted without a fold has no `record.created` Event and no act in the act store, so its stage's
    winder is `ROOT` (the setting planned it). Run the realm's first two MATTER barriers: the first term of each
    works ripens at tick 1 and the log's `term.matured` Events cite `ROOT` -- not the row id, which the gate
    refuses as an unresolvable cause (`Forbidden`, seen when the winder was `rid`) -- and the second chains to
    the first."""
    def ripened(rid):
        return [e for e in w.log if e.kind == "term.matured" and any(c.subject == rid for c in e.changes)]

    w = POP.build_realm(0)
    d = _tick0(w)
    w.tick = 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    first = {rid: ripened(rid) for rid in (HEARTH_WORKS, DWELLING_WORKS)}
    assert all(len(evs) == 1 for evs in first.values()), {k: len(v) for k, v in first.items()}
    assert all(e.causes == [ROOT] for evs in first.values() for e in evs), \
        [e.causes for evs in first.values() for e in evs]
    assert world_q.matured_terms(w, HEARTH_WORKS) == 1 == world_q.matured_terms(w, DWELLING_WORKS)
    w.tick = 2
    d.matter(mint_token(w, WriteClass.MATTER), [])
    second = ripened(HEARTH_WORKS)
    assert len(second) == 2 and second[1].causes == [second[0].id], [e.causes for e in second]
    assert world_q.matured_terms(w, HEARTH_WORKS) == 2


# ======================================================================================
# 3 -- THE PLANTED FAILURE: THE SAME ROWS AUTHORED `kind: text`
# ======================================================================================

def test_planted_failure_rows_authored_kind_text_mint_records_neither_verb_can_name(monkeypatch):
    """The same two rows with `kind: text` mint two text Records (the shape a computed `create_record` mints):
    no `{plan, at}`, so `works_for` finds nothing, the masters' held-Record stamp is empty, and `found` and `build`
    form for nobody -- the failure the block exists to end. CONTROL: the shipped `works` rows stamp each master
    his works. The REALM reading of this plant (`aperture 4 0`: `found` and `build` attempted 0 times) is in the
    commit."""
    text = _build(monkeypatch, _rows(lambda r: {**r, "kind": "text"}))
    monkeypatch.undo()
    assert sorted(r.id for r in text.records.values() if r.kind == "text") == [DWELLING_WORKS, HEARTH_WORKS]
    assert not [r for r in text.records.values() if r.kind == world_q.WORKS_KIND]
    assert world_q.works_for(text, "set_s_002", "hearth") == []
    assert world_q.works_for(text, "b_s_001_court", "dwelling") == []
    for master in (DUKE, STEWARD):
        assert world_q.records_held_for_holding_rows(text, text.persons[master]) == ()
    real = POP.build_realm(0)
    assert world_q.records_held_for_holding_rows(real, real.persons[DUKE]) == (HEARTH_WORKS,)
    assert world_q.records_held_for_holding_rows(real, real.persons[STEWARD]) == (DWELLING_WORKS,)


# ======================================================================================
# 4 -- THE READER'S REFUSALS, EACH ONE CLAUSE FROM A ROW THAT MINTS
# ======================================================================================

def _row(**over):
    return {"id": "works_probe", "kind": "works", "plan": "hearth", "at": {"settlement": "S-003"},
            "rung": {"settlement": "S-003"}, "master": "off_lord_steward", "terms": 2, **over}


def _control(monkeypatch):
    w = _build(monkeypatch, [])
    monkeypatch.undo()
    return w


def _mint(w, *rows, **kw):
    return POP.mint_planned_works(w, list(rows), w._anchors, w._office_census["authored"], **kw)


def test_a_well_formed_row_mints_and_each_malformed_one_refuses(monkeypatch):
    w = _control(monkeypatch)
    assert _mint(w, _row()) == ["works_probe"]
    assert w.records["works_probe"].subject_matter == {"plan": "hearth", "at": "set_s_003"}
    bad = {
        "a misspelt key": {**{k: v for k, v in _row().items() if k != "terms"}, "term": 2},
        "a missing key": {k: v for k, v in _row().items() if k != "master"},
        "an unpriced plan": _row(plan="settlement"),
        "a plan that is no kind": _row(plan="cathedral"),
        "no terms": _row(terms=0),
        "boolean terms": _row(terms=True),
        "an unknown master seat": _row(master="off_nobody"),
        "an `at` that names no rung": _row(at={"settlement": "S-999"}),
        "a paying rung that names no rung": _row(rung={"hearth": "S-001:nowhere"}),
        "a row that is not a mapping": ["works_probe"],
    }
    w = _control(monkeypatch)       # one world for the whole loop: every refusal is raised before `change.apply()`,
    for why, row in bad.items():    # and each pass asserts the world unmoved, so a leak still fails at the row that caused it
        before = (len(w.records), len(w.tenures))
        with pytest.raises(Unspecified):
            _mint(w, row)
        assert (len(w.records), len(w.tenures)) == before, f"{why}: a refused row left something behind"
    # an id a Record already carries: the probe row minted once, then again under the same id on another target
    w = _control(monkeypatch)
    _mint(w, _row())
    before = (len(w.records), len(w.tenures))
    with pytest.raises(Unspecified):
        _mint(w, _row(at={"settlement": "S-004"}, rung={"settlement": "S-004"}))
    assert (len(w.records), len(w.tenures)) == before


def test_a_second_live_works_on_one_target_refuses_and_a_partial_cast_skips_a_missing_master(monkeypatch):
    """`create_record` declines a second live works on one `(plan, at)` (the effect's own `NO_CHANGE`); the reader
    surfaces it as a refusal instead of dropping the row. A `cap`-shortened cast skips a row whose master's seat was
    not seated, as the per-case loops skip their absent -- and a complete cast refuses the same row."""
    w = _control(monkeypatch)
    _mint(w, _row())
    with pytest.raises(Unspecified):
        _mint(w, _row(id="works_probe_again"))
    assert "works_probe_again" not in w.records
    w = _control(monkeypatch)
    ghost = _row(master="off_nobody")
    assert _mint(w, ghost, partial=True) == [] and "works_probe" not in w.records
    with pytest.raises(Unspecified):
        _mint(w, ghost)
