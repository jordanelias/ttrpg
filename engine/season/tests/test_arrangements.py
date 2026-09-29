"""`data/arrangements.py` -- plan position `18` (PROC-A), part 3.

Falsifiers named by the source docs this position builds from (`21_RECONCILIATION.md` PHASE 2 step
6, `19_PLAN.md` step 11, `03_PARAMETERS.md` PART D): a fourteenth key fails naming the row; a
declared-disposal row with no quorum fails the load; a thirteenth (here: a fourth) arrangement
loads with no code change; a speech-kind whose reachable bands name a band outside the ladder fails
to load. Scoped to the THREE seeded games (`arrangements.yaml`'s own header states why not all
twelve) and the SIX seeded speech kinds (same file, why not all ten).
"""

from __future__ import annotations

import textwrap

import pytest

from ..data import arrangements as A
from ..data.rosters import LADDER_RUNGS, load_yaml


def test_the_three_seeded_arrangements_load():
    assert set(A.ARRANGEMENTS) == {"arbitration", "parliamentary_debate", "council_of_state"}
    arb = A.ARRANGEMENTS["arbitration"]
    assert arb["disposal"] == "bench" and arb["appeal_basis"] == "none"
    parl = A.ARRANGEMENTS["parliamentary_debate"]
    cos = A.ARRANGEMENTS["council_of_state"]
    # `03_PARAMETERS.md` §E.2: "the same shape, and the opposite trade" -- every difference between
    # the two is locatable in the row, which is PART D's own claim under test.
    assert parl["floor"] != cos["floor"]
    assert parl["records_dissent"] != cos["records_dissent"]
    assert parl["disposes"] == cos["disposes"] == "Record"
    assert parl["disposal_reach"] == cos["disposal_reach"] == "realm", (
        "council of state's `disposal_reach` is explicitly UNCHANGED from the parliament in the "
        "source (\"the deliberation is sealed, the decree is proclaimed\")")


def test_the_six_seeded_speech_kinds_load_and_only_impugn_motive_carries_a_cap():
    # `arrangements.yaml`'s `speech_kinds:` reuses `rosters.yaml: ladder_rungs` as its own six ids
    # (see that roster's own note); read it rather than re-typing the six names a third time.
    assert set(A.SPEECH_KINDS) == set(LADDER_RUNGS)
    for kind, row in A.SPEECH_KINDS.items():
        if kind == "impugn_motive":
            assert row["reachable_bands"] == ("Partial",), row
        else:
            assert row["reachable_bands"] == (), (
                f"{kind} carries an authored cap this position's sources do not state: {row}")


def _reload_with(extra_yaml_text: str):
    """Patch `A.ARRANGEMENTS_YAML.read_text` for one call by monkeypatching the module's own
    `_load`, the same patch point every sibling loader test in this package uses
    (`data.rosters.ROSTERS_YAML`, `data.verbs.VERB_TABLE_YAML`) -- see `data/__init__.py`'s own
    docstring on why a loader's path is the one legitimate external patch point."""
    doc = load_yaml(A.ARRANGEMENTS_YAML.read_text(encoding="utf-8"))
    extra = load_yaml(extra_yaml_text)
    merged = dict(doc)
    merged["arrangements"] = list(doc["arrangements"]) + list(extra.get("arrangements") or [])
    merged["speech_kinds"] = list(doc["speech_kinds"]) + list(extra.get("speech_kinds") or [])
    arrangements, kinds = {}, {}
    for r in merged.get("speech_kinds") or ():
        row = A._load_speech_kind(r)
        kinds[row["id"]] = row
    for r in merged.get("arrangements") or ():
        row = A._load_arrangement(r)
        arrangements[row["id"]] = row
    return arrangements, kinds


def test_a_fourth_arrangement_loads_with_no_code_change():
    """`19_PLAN.md` step 11's own artifact, run at this position's smaller seeded scale: "the
    thirteenth game loads with no code change." A well-formed new row, added as DATA ONLY, loads
    through the unmodified `_load_arrangement`."""
    extra = textwrap.dedent("""
        arrangements:
          - id:               examination
            disposal:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            order:              scripted
            proofs:             [testimony]
            disposes:           oblige
            disposal_reach:     room
    """)
    arrangements, _ = _reload_with(extra)
    assert "examination" in arrangements and len(arrangements) == 4


def test_a_fifteenth_key_fails_naming_the_row():
    extra = textwrap.dedent("""
        arrangements:
          - id:               bad_row
            disposal:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            order:              scripted
            proofs:             []
            disposes:           none
            disposal_reach:     room
            scale:              settlement
    """)
    with pytest.raises(SystemExit, match=r"bad_row.*unknown key.*scale"):
        _reload_with(extra)


def test_a_declared_disposal_row_with_no_quorum_fails_the_load():
    extra = textwrap.dedent("""
        arrangements:
          - id:               vote
            disposal:          declared
            bench_basis:        determine
            floor:              closed
            records_dissent:    true
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            order:              rank
            proofs:             []
            disposes:           none
            disposal_reach:     room
    """)
    with pytest.raises(SystemExit, match=r"vote.*no `quorum:`"):
        _reload_with(extra)


def test_a_declared_disposal_row_with_a_quorum_loads():
    extra = textwrap.dedent("""
        arrangements:
          - id:               vote
            disposal:          declared
            bench_basis:        determine
            floor:              closed
            records_dissent:    true
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            order:              rank
            proofs:             []
            disposes:           none
            disposal_reach:     room
            quorum:             0.5
    """)
    arrangements, _ = _reload_with(extra)
    assert arrangements["vote"]["quorum"] == 0.5


def test_quorum_on_a_non_declared_row_fails_the_load():
    extra = textwrap.dedent("""
        arrangements:
          - id:               stray_quorum
            disposal:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            order:              rank
            proofs:             []
            disposes:           none
            disposal_reach:     room
            quorum:             0.5
    """)
    with pytest.raises(SystemExit, match=r"stray_quorum.*quorum"):
        _reload_with(extra)


def test_a_speech_kind_whose_reachable_bands_name_a_band_outside_the_ladder_fails_to_load():
    extra = textwrap.dedent("""
        speech_kinds:
          - id:               fabricated
            genres:            [forensic]
            min_rank:           hearth
            reachable_bands:    [Legendary]
    """)
    with pytest.raises(SystemExit, match=r"fabricated.*reachable band.*Legendary"):
        _reload_with(extra)


def test_c1_is_a_report_not_a_refusal_and_is_honest_about_todays_state():
    """`21_RECONCILIATION.md` PHASE 2 step 6's C-1 check, as a REPORT (module docstring: refusing
    it today would make the loader vacuous, since `determine` opens nothing yet). MEASURED: every
    seeded row using a real tenure kind (`arbitration`, `disposes: oblige`) reports, because
    `oblige` has no opener either (`rosters.yaml: tenure_kinds`'s own note: "the other five
    empty") -- and a `Record`-disposing row is not in scope for a TENURE-kind opener check at all.

    FALSIFIER: this test goes red the day `determine` gains an effect that opens `oblige`, which
    is exactly the signal PHASE 2 step 11 landed and this position's own C-1 gap can be re-graded."""
    reported = A.arrangements_without_a_disposal_opener()
    assert reported == ["arbitration"], reported
    assert "parliamentary_debate" not in reported and "council_of_state" not in reported, (
        "a `Record`-disposing row is not asked of the tenure-kind opener map")
