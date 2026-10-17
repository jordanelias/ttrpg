"""`data/arrangements.py` -- plan position `18` (PROC-A), part 3.

Falsifiers named by the source docs this position builds from (`21_RECONCILIATION.md` PHASE 2 step
6, `19_PLAN.md` step 11, `03_PARAMETERS.md` PART D): a fourteenth key fails naming the row; a
declared-disposal row with no quorum fails the load; a thirteenth (here: another, beyond the
seeded rows) arrangement loads with no code change; a speech-kind whose reachable bands name a band outside the ladder fails
to load. Scoped to the SEVEN seeded games (three until v9 SC-03a; `arrangements.yaml`'s own header states why not all
twelve) and the SIX seeded speech kinds (same file, why not all ten).
"""

from __future__ import annotations

import ast
import subprocess
import sys
import textwrap

import pytest

from ..data import arrangements as A
from ..data import files
from ..data.rosters import LADDER_RUNGS, load_yaml


def test_the_seven_seeded_arrangements_load():
    """THREE until v9 SC-03a, which seeded the four `<tenure>` rows (`arrangements.yaml`'s header)
    once `detain` and `ban` became `tenure_kinds` members. The four dispose those two kinds and
    nothing else, each a `bench` disposal -- the loader stays green on them (the position's own
    falsifier clause)."""
    assert set(A.ARRANGEMENTS) == {"arbitration", "parliamentary_debate", "council_of_state",
                                   "legal_trial", "tribunal", "interrogation",
                                   "inquisition_hearing"}
    sc03a = ("legal_trial", "tribunal", "interrogation", "inquisition_hearing")
    assert {A.ARRANGEMENTS[r]["disposes"] for r in sc03a} == {"detain", "ban"}
    assert all(A.ARRANGEMENTS[r]["disposal"] == "bench" for r in sc03a)
    # §E.2's own differences, each locatable in the row: an interrogation's subject cannot appeal
    # and speaks when scripted; the inquisition hearing is the same with a bench, an appeal and
    # documents interposed; the tribunal is the trial with an admitted floor and no appeal.
    assert A.ARRANGEMENTS["interrogation"]["order"] == A.ARRANGEMENTS["inquisition_hearing"]["order"]
    assert A.ARRANGEMENTS["interrogation"]["appeal_basis"] == "none" != \
        A.ARRANGEMENTS["inquisition_hearing"]["appeal_basis"]
    assert (A.ARRANGEMENTS["tribunal"]["floor"], A.ARRANGEMENTS["legal_trial"]["floor"]) == \
        ("admitted", "open")
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


def test_another_arrangement_loads_with_no_code_change():
    """`19_PLAN.md` step 11's own artifact, run at this position's smaller seeded scale: "the
    thirteenth game loads with no code change." A well-formed new row, added as DATA ONLY, loads
    through the unmodified `_load_arrangement`. (Named "another", not "a fourth": three rows were
    seeded when this was written and seven are now -- the row added is one beyond whatever is seeded.)"""
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
    # v9 SC-03a: the seeded count is read, not pinned (it was `== 4` at three seeded rows).
    assert "examination" in arrangements and len(arrangements) == len(A.ARRANGEMENTS) + 1


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
    is exactly the signal PHASE 2 step 11 landed and this position's own C-1 gap can be re-graded.

    ⚠ AND IT WENT RED, AS DESIGNED, AT PLAN POSITION `19` (U7-remit): `loop/effects.py::_eff_determine`
    opens the disposal `oblige`, the derived opener map reads `determine` beside `oblige`'s own opener,
    and `arbitration` leaves the report. Re-pinned to the empty report; the `Record`-disposing rows
    are still not asked. Whether C-1 should now become a LOAD REFUSAL -- the module docstring's reason
    for reporting (*"`determine` opens nothing today"*) no longer holds -- is left to this module's
    owner: `19` did not move the check, only made it pass."""
    reported = A.arrangements_without_a_disposal_opener()
    assert reported == [], reported
    assert "parliamentary_debate" not in reported and "council_of_state" not in reported, (
        "a `Record`-disposing row is not asked of the tenure-kind opener map")


# ---------------------------------------------------------------------------------------------
# v9 SC-08: the loader's cross-validation fires in PRODUCTION, not only under pytest. Observed in
# a fresh interpreter -- `sys.modules` of THIS process is polluted by the import at the top of this
# file, so only a subprocess can say what the headless run itself loads.
# ---------------------------------------------------------------------------------------------
_HEADLESS_PROBE = """
import sys
sys.path.insert(0, {root!r})
from engine.season.data import files
before = 'engine.season.data.arrangements' in sys.modules      # the control: files alone loads none
override = {override!r}
if override:
    # the loaders' patch point: `data/arrangements.py` binds `files.ARRANGEMENTS_YAML` at import
    from pathlib import Path
    files.ARRANGEMENTS_YAML = Path(override)
from engine.season.harness import headless
sys.argv = ['headless', '--case', 'NPC-088', '--seasons', '1', '--seed', '0']
rc = headless.main()
print(repr((before, 'engine.season.data.arrangements' in sys.modules, rc)))
"""


def _headless(override: str = ""):
    return subprocess.run([sys.executable, "-c", _HEADLESS_PROBE.format(
        root=str(files.REPO_ROOT), override=override)],
        capture_output=True, text=True, timeout=300, cwd=str(files.REPO_ROOT))


def test_the_headless_run_loads_the_arrangements_loader_and_the_probe_can_tell():
    """SC-08 EXIT. `requirements.yaml`'s headless command constructs a season with
    `data.arrangements` loaded (by `state/gate.py` and `loop/effects_information.py`, the two
    non-test importers). The probe also reads the module set BEFORE importing the harness, from a
    process that has imported only `data.files` -- the control showing `sys.modules` can observe
    the absence the assertion below would otherwise miss (CLAUDE.md §0.1 pt 2)."""
    proc = _headless()
    assert proc.returncode == 0, proc.stderr[-3000:]
    before, after, rc = ast.literal_eval(proc.stdout.strip().splitlines()[-1])    # our own probe's repr
    assert before is False, "the control is blind: `data.files` alone already loaded the arrangements"
    assert after is True and rc == 0
    assert "CONTENT HASH:" in proc.stdout       # a season was constructed, not an import alone


def test_a_planted_unknown_key_in_a_scratch_copy_makes_the_headless_run_refuse_naming_the_row(
        tmp_path):
    """SC-08 FALSIFIER. The tracked YAML is read, never written: a scratch copy carries a thirteenth
    key on the `arbitration` row, and the same headless run must exit non-zero naming the row and
    the key. The unplanted run beside it is the control that the refusal is the plant's and not the
    harness's -- and the asserted counts show both runs ran."""
    text = files.ARRANGEMENTS_YAML.read_text(encoding="utf-8")
    anchor = "  - id:               arbitration\n"
    assert text.count(anchor) == 1, "the plant has nowhere to go; the seeded row moved"
    scratch = tmp_path / "arrangements.yaml"
    scratch.write_text(text.replace(anchor, anchor + "    scale:             settlement\n"),
                       encoding="utf-8")
    assert scratch.read_text(encoding="utf-8") != text
    control = _headless(str(files.ARRANGEMENTS_YAML))
    planted = _headless(str(scratch))
    assert control.returncode == 0, control.stderr[-2000:]
    assert planted.returncode != 0
    assert "CONTENT HASH:" not in planted.stdout          # it refused before the season ran
    assert "arbitration" in planted.stderr and "unknown key" in planted.stderr \
        and "scale" in planted.stderr, planted.stderr[-2000:]
