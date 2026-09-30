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
"""
import pytest

from engine.season.data.rosters import RUNG_KINDS, SCALE_OF_RUNG, _check_scale_of_rung
from engine.season.gaps import Unspecified

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
