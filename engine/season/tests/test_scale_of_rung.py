"""`rosters.yaml: scale_of_rung` -- plan position `20-ii` (U9/R-04)'s vocabulary mapping, problem
(1) of the two the position's own instruction names. See the roster row's `note:` for problem (2)
(representability), which this mapping does not solve and which `harness/corpus_run.py::rescales`
(covered by `test_the_corpus_runs_and_the_ranking_cannot_discriminate` in `test_season_shape.py`)
does instead.

What each test proves:
  1. THE DOMAIN IS EXACTLY `RUNG_KINDS` -- every rostered rung kind gets a scale and no other key
     appears, checked by set equality rather than "is non-empty".
  2. THE FALSIFIER FOR (1): `_check_scale_of_rung` is a function, not an inline `if`, precisely so
     a drifted mapping (a missing rung, an extra key) can be planted and watched refuse.
  3. EVERY VALUE IS ONE OF CANON'S FIVE SCALES -- `Object` through `Structural`, from
     `scale_transitions_v30.md` §2 (quarantined; read for vocabulary only, `CLAUDE.md` §1/§0.05).
  4. `Object` IS UNREACHABLE, AND THAT IS THE STATED GAP, NOT AN ACCIDENT -- no rung sits below
     `person` on the containment ladder, so nothing maps to canon's sub-personal "one item, one
     wound" scale. Asserting this directly is what stops a future edit silently inventing a filler.
  5. TWO GROUNDED SPOT CHECKS, cited to the Scope column's own examples: `person` is canon's
     literal example of `Personal` ("one person"); `duchy` appears BY NAME in `Territorial`'s
     example ("a duchy, a district"); `realm` is the rung above `duchy`, canon's "kingdom".
  6. `04 PART D` ROW 28's OWN FALSIFIER ("a branch on a rung-kind member ... re-run the seeded
     season with `rung_kinds` extended by a synthetic kind ... any test that moves branched on a
     member"), SCOPED TO WHAT THIS POSITION ACTUALLY ADDS -- see the two tests' own docstrings
     for what is built and what is deliberately not, and why.
"""
import pytest

from engine.season.data import rosters as R
from engine.season.data.rosters import RUNG_KINDS, SCALE_OF_RUNG, _check_scale_of_rung
from engine.season.gaps import Forbidden, Unspecified
from engine.season.harness import corpus_run as C
from engine.season.harness import run_cases as RC

CANON_SCALES = {"Object", "Personal", "Relational", "Territorial", "Structural"}


def test_scale_of_rung_domain_is_exactly_rung_kinds():
    assert set(SCALE_OF_RUNG) == set(RUNG_KINDS)
    assert SCALE_OF_RUNG, "control is vacuous if the mapping is empty"


def test_check_scale_of_rung_refuses_a_missing_rung():
    drifted = dict(SCALE_OF_RUNG)
    del drifted["realm"]
    with pytest.raises(Unspecified):
        _check_scale_of_rung(drifted, RUNG_KINDS)


def test_check_scale_of_rung_refuses_an_extra_key():
    drifted = dict(SCALE_OF_RUNG)
    drifted["faction"] = "Structural"
    with pytest.raises(Unspecified):
        _check_scale_of_rung(drifted, RUNG_KINDS)


def test_check_scale_of_rung_accepts_the_shipped_mapping():
    # Control: the function must NOT raise on the roster it actually loaded.
    _check_scale_of_rung(SCALE_OF_RUNG, RUNG_KINDS)


def test_every_value_is_one_of_canons_five_scales():
    assert set(SCALE_OF_RUNG.values()) <= CANON_SCALES, (
        f"a rung maps to {set(SCALE_OF_RUNG.values()) - CANON_SCALES}, not one of canon's five")


def test_object_is_unreachable_by_design():
    """`Object` ("one item, one wound") is sub-personal; nothing in `rung_kinds` sits below
    `person`, so no rung maps to it. If this ever fires, either a rung was invented below
    `person`, or the mapping started fabricating a filler for a scale nothing here reaches."""
    assert "Object" not in set(SCALE_OF_RUNG.values())


def test_person_is_personal_and_duchy_and_realm_are_territorial_and_structural():
    # Grounded spot checks -- `person` is canon's own example of `Personal`; `Territorial`'s own
    # example names `duchy` by word ("a duchy, a district"); `realm`, one rung above `duchy`, is
    # canon's "kingdom" (`Structural`).
    assert SCALE_OF_RUNG["person"] == "Personal"
    assert SCALE_OF_RUNG["duchy"] == "Territorial"
    assert SCALE_OF_RUNG["realm"] == "Structural"


def test_a_synthetic_rung_kind_with_no_scale_refuses_at_the_mapping():
    """`04 PART D` row 28, THE HALF THAT IS THIS POSITION'S OWN: `rung_kinds` EXTENDED by a
    synthetic kind, unmapped by `scale_of_rung`, must be caught -- not by a season silently
    misbehaving, but by `_check_scale_of_rung` refusing loudly at the boundary this position
    actually owns. This is the SAME check `test_check_scale_of_rung_refuses_a_missing_rung`
    exercises from the other side (a key `SCALE_OF_RUNG` has and `RUNG_KINDS` does not); this
    test exercises "a member `RUNG_KINDS` gained and `SCALE_OF_RUNG` does not cover" -- the
    literal shape `04`'s falsifier describes, since `scale_of_rung`'s own mapping IS the code
    that would otherwise need a branch per member."""
    extended = tuple(RUNG_KINDS) + ("_planted_rung",)
    with pytest.raises(Unspecified):
        _check_scale_of_rung(SCALE_OF_RUNG, extended)


def test_extending_rung_kinds_at_the_top_of_the_ladder_is_not_a_clean_no_op_and_that_is_shown_not_assumed():
    """`04 PART D` row 28's OWN WORDING ("re-run the seeded season with `rung_kinds` EXTENDED by a
    synthetic kind AND PERMUTED") DOES NOT CLEANLY APPLY TO `rung_kinds` SPECIFICALLY, AND THIS
    IS DEMONSTRATED RATHER THAN ASSUMED, because a demonstrated limit is worth more than a test
    that would have passed by accident. `rung_kinds` is `#353 §10`'s CONTAINMENT LADDER, and its
    ORDER IS THE DEFINITION: `corpus_run.build_at`'s `chain = order[order.index(scale):]` walks
    from a case's own scale to the LAST element of the list, so appending ANYTHING after `realm`
    -- the only place a "new, unused" member could go without renumbering the other seven -- adds
    a NEW OUTERMOST CONTAINER above every case's chain, unconditionally, for every scale from
    `person` up. That is `build_at` doing exactly what its own docstring says (the chain reaches
    the top of the ladder), not a hardcoded branch on a member's name -- but it means "extend and
    confirm nothing moves" is not a valid test of THIS roster the way it is of an unordered one
    (`tenure_kinds`, `test_jordan_a_roster_edit_is_a_data_edit_and_nothing_else` above). Proven
    here rather than skipped silently: appending a synthetic kind after `realm` and re-running a
    realm-scale case raises `Forbidden` at `Rung.__init__` (`state/carriers.py::S10`) the instant
    the new top container is built, because THAT accessor is a third, separately-imported binding
    of `RUNG_KINDS` this test does not also patch -- which is itself the finding: at least three
    modules (`data.rosters`, `harness.corpus_run`, `state.carriers`) hold independent import-time
    copies of this roster, so "the season" has no single point to extend it at. `PERMUTING` two
    EXISTING members is worse, not better: it would silently swap which rungs are ABOVE and BELOW
    each other in the ladder `build_at` walks, changing a case's build in a way `04 §B.13`'s own
    ordering rule (order is semantic where a ladder is being described) says is CORRECT to move,
    not a defect to catch. `SCALE_OF_RUNG`'s own falsifier above is the version of row 28 that
    DOES apply cleanly to this position's own new code -- a member with no scale refuses at load,
    which is the loudest form "no branch on a member" can take for a mapping rather than a ladder."""
    extended = tuple(RUNG_KINDS) + ("_planted_rung",)
    npc = RC.load_cases("NPC")
    realm_case = next(c for c in npc if c.get("scale") == "realm")
    with pytest.raises(Forbidden):
        with monkeypatch_module(C, "RUNG_KINDS", extended), \
             monkeypatch_module(R, "RUNG_KINDS", extended):
            C.run_case(realm_case, 0, "NPC")


class monkeypatch_module:
    """A tiny context-managed attribute swap, used here rather than the `monkeypatch` fixture
    because this test's own point is raising INSIDE a `with`, before any fixture teardown would
    run -- and a bare `try`/`finally` around one `pytest.raises` block is clearer than threading
    the fixture through it."""
    def __init__(self, mod, name, value):
        self.mod, self.name, self.value = mod, name, value

    def __enter__(self):
        self.old = getattr(self.mod, self.name)
        setattr(self.mod, self.name, self.value)

    def __exit__(self, *exc):
        setattr(self.mod, self.name, self.old)
