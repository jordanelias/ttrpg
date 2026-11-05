"""v10 CR-30: `Person.heritage` -- descent as a read-off field, and the `marks` term's carrier.

FALSIFIER (the plan's): a hand-built world where an actor of `heritage: southern_einhir` acts before a co-located
witness -- the witness's `seen` claim reads `marks == ("southern_einhir",)` and `who == actor`; an unauthored
actor's reads `()`. PLANTED FAILURE: `_term_marks` returning `()` reddens the first assertion (run below, and
`test_the_planted_failure_...` shows the observation the assertion makes).

ALSO: a cast row naming an unrostered heritage is refused; a play-time write is refused by the gate; the exporter
refuses an `engages:` value that is not a `concerns:` key; the authored values are canon's two descents and the
rows whose own text states a birthplace -- and silence is `None`.

THE CONTROL (a) and the mover (b) are measured with `build_realm(0)` twice over two seasons and recorded in the
CR-30 commit body, not asserted here: an event list is no pin (CLAUDE.md §0.1 pt 5).
"""
import pytest

from engine.season import epistemic
from engine.season.data import cast
from engine.season.data.matrix import matrix_row
from engine.season.data.rosters import SEEN_PREDICATE
from engine.season.gaps import Unspecified
from engine.season.loop.driver import mint_token
from engine.season.state.gate import WriteClass
from engine.season.state.world import Step
from engine.substrate import descriptors
from .test_in12_conceal import DUKE, WATCHER, _convene, _witness, _world

SOUTH = "southern_einhir"


def _seen_marks(heritage):
    """The `(marks, who)` of the one `seen` claim `WATCHER` holds after `DUKE` convenes at the place they share."""
    w, d = _world()
    w.persons[DUKE].heritage = heritage
    out, _e = _convene(w, d)
    _witness(w, d, out)
    seen = [c.value for c in w.persons[WATCHER].ledger if c.predicate == SEEN_PREDICATE]
    assert len(seen) == 1, f"the co-located witness holds {len(seen)} `seen` claims: the comparison is vacuous"
    return seen[0].marks, seen[0].who


# ======================================================================================
# THE FALSIFIER
# ======================================================================================

def test_a_co_located_witness_sees_the_actors_heritage_true_beside_who():
    assert _seen_marks(SOUTH) == ((SOUTH,), DUKE)
    assert _seen_marks("altonian") == (("altonian",), DUKE)


def test_an_unauthored_actor_reads_nothing_describable():
    assert _seen_marks(None) == ((), DUKE)


def test_the_planted_failure_a_term_marks_returning_nothing_reads_empty_and_not_the_heritage(monkeypatch):
    """The first assertion above can observe the failure it excludes."""
    monkeypatch.setitem(epistemic.TERM_READERS, "marks", lambda w, e, act: ())
    assert _seen_marks(SOUTH) == ((), DUKE) != ((SOUTH,), DUKE)


# ======================================================================================
# THE ROSTER, THE READER AND THE GATE
# ======================================================================================

def test_the_roster_is_the_five_and_engages_only_rostered_concerns():
    assert descriptors.HERITAGES == ("northern_einhir", "central_einhir", "southern_einhir", "altonian",
                                     "schoenlander")
    assert descriptors.HERITAGE_ENGAGES == {SOUTH: "einhir", "altonian": "altonia"}
    assert set(descriptors.HERITAGE_ENGAGES) <= set(descriptors.HERITAGES)
    assert set(descriptors.HERITAGE_ENGAGES.values()) <= set(descriptors.AFFILIATION_CONCERNS)


@pytest.mark.parametrize("engages", [{SOUTH: "narnia"}, {"martian": "einhir"}])
def test_the_exporter_refuses_an_engagement_that_is_no_concern_or_no_member(monkeypatch, engages):
    import sys
    sys.path.insert(0, "tools")
    import export_descriptors as ed
    real = ed.ci_common.load_yaml

    def planted(path, default=None):
        reg = real(path, default=default)
        reg["heritage_roster"]["engages"] = engages
        return reg
    monkeypatch.setattr(ed.ci_common, "load_yaml", planted)
    with pytest.raises(SystemExit):
        ed.build()


@pytest.mark.parametrize("raw", ["martian", "Southern_Einhir", "", 3, ["altonian"], True])
def test_a_cast_row_naming_an_unrostered_heritage_is_refused(raw):
    with pytest.raises(Unspecified):
        cast.heritage_of({"id": "X", "heritage": raw})


def test_no_row_no_key_and_null_are_unauthored():
    assert cast.heritage_of({}) is None and cast.heritage_of({"id": "X"}) is None
    assert cast.heritage_of({"id": "X", "heritage": None}) is None
    assert cast.heritage_of({"id": "X", "heritage": "altonian"}) == "altonian"


def test_the_carrier_has_no_matrix_row_and_the_gate_refuses_a_write():
    with pytest.raises(Unspecified):
        matrix_row("Person", "heritage")
    w, _d = _world()
    w.persons[DUKE].heritage = SOUTH
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("heritage", mint_token(w, WriteClass.ACTS),
                lambda: setattr(w.persons[DUKE], "heritage", "altonian"),
                record_kind="Person", fieldname="heritage", driver="Act")
    assert w.persons[DUKE].heritage == SOUTH, "the refused write landed"


# ======================================================================================
# THE VALUES: canon first, then a row's own stated birthplace; silence is None
# ======================================================================================

#: `{case id: heritage}` -- the whole authored set, pinned so a value added without a ground reddens here.
AUTHORED = {"NPC-020": "northern_einhir",      # canon/03_canonical_timeline.md:138, King Almud: "Northern Einhir"
            "NPC-052": "southern_einhir",      # canon/03_canonical_timeline.md:144, Duke Magnus Vaynard: "Southern Einhir heritage"
            "NPC-011": "altonian",             # the row's own `birthplace: Altonia`
            "NPC-012": "schoenlander"}         # the row's own `birthplace: Schoenland`


def test_the_cast_authors_exactly_the_grounded_rows_and_every_value_is_a_member():
    got = {cid: cast.heritage_of(r) for cid, r in cast.load().items()}
    assert len(got) == 46
    assert {cid: h for cid, h in got.items() if h is not None} == AUTHORED
    assert set(AUTHORED.values()) <= set(descriptors.HERITAGES)
    # the two canon rows are the persons canon names
    assert cast.name_of(cast.row("NPC-020")) == "Almud Almqvist" and cast.name_of(cast.row("NPC-052")) == "Magnus Vaynard"
    assert cast.row("NPC-011")["birthplace"] == "Altonia" and cast.row("NPC-012")["birthplace"] == "Schoenland"
