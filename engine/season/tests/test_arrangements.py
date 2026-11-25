"""`data/arrangements.py` -- plan position `18` (PROC-A), part 3.

Falsifiers named by the source docs this position builds from (`21_RECONCILIATION.md` PHASE 2 step
6, `19_PLAN.md` step 11, `03_PARAMETERS.md` PART D): a fourteenth key fails naming the row; a
declared-disposal row with no quorum fails the load; a thirteenth (here: another, beyond the
seeded rows) arrangement loads with no code change; a speech-kind whose reachable bands name a band outside the ladder fails
to load. Scoped to the THIRTEEN rows (the NINE seeded games plus four new at B24p.03; three until v9 SC-03a, seven until v9 SC-04, eight until v10 SC-04; `arrangements.yaml`'s own header states why not all
twelve) and the SIX seeded speech kinds (same file, why not all ten).
"""

from __future__ import annotations

import textwrap

import pytest

from ..data import arrangements as A
from ..data import verbs as _verbs
from ..data.rosters import LADDER_RUNGS, load_yaml


def test_the_thirteen_arrangements_load():
    """THREE until v9 SC-03a, which seeded four `<tenure>` rows (`arrangements.yaml`'s header)
    once `detain` and `ban` became `tenure_kinds` members; EIGHT since v9 SC-04 seeded the fifth,
    `excommunication_deliberation`; NINE since v10 SC-04 seeded `negotiation` (a `consent` close); THIRTEEN since B24p.03 added `conversation`,
    `interrogation` (a questioning: the tree's old `interrogation` is now `examination`), `rally` and `audience`. The four dispose those two
    kinds and nothing else, each a `bench` close -- the loader stays green on them (the position's own falsifier clause)."""
    assert set(A.ARRANGEMENTS) == {"arbitration", "parliamentary_debate", "council_of_state",
                                   "legal_trial", "tribunal", "examination",
                                   "inquisition_hearing", "excommunication_deliberation",
                                   "negotiation", "conversation", "interrogation", "rally", "audience"}
    assert len(A.ARRANGEMENTS) == 13
    sc03a = ("legal_trial", "tribunal", "examination", "inquisition_hearing")
    assert {A.ARRANGEMENTS[r]["disposes"] for r in sc03a} == {"detain", "ban"}
    assert all(A.ARRANGEMENTS[r]["close"] == "bench" for r in sc03a)
    # §E.2's own differences, each locatable in the row: an examination's subject cannot appeal
    # (B24p.03: `order`, which said "when scripted", is gone; both rows are the one `inquisition` rite); the inquisition hearing is the same
    # with a bench, an appeal and documents interposed; the tribunal is the trial with an admitted floor and no appeal.
    assert A.ARRANGEMENTS["examination"]["rite"] == A.ARRANGEMENTS["inquisition_hearing"]["rite"] == "inquisition"
    assert A.ARRANGEMENTS["examination"]["appeal_basis"] == "none" != \
        A.ARRANGEMENTS["inquisition_hearing"]["appeal_basis"]
    assert (A.ARRANGEMENTS["tribunal"]["floor"], A.ARRANGEMENTS["legal_trial"]["floor"]) == \
        ("admitted", "open")
    # v9 SC-04: the fifth `<tenure>` row. #453 §8.1 reads excommunication as a `ban` (an opening), and it
    # shares the Church bench's kind with `inquisition_hearing`; its other keys are §E.2's own block
    # (03_PARAMETERS.md:648-654), each locatable: a closed, sealed (`records_dissent: false`) rank-ordered
    # deliberation with a ceremony interposed, appealable, reaching the realm.
    exc = A.ARRANGEMENTS["excommunication_deliberation"]
    assert exc["disposes"] == A.ARRANGEMENTS["inquisition_hearing"]["disposes"] == "ban"
    # v11 CR-34: the first `declared` row (C-7), `quorum: 2` -- `test_cr34_declared_disposal.py` reads the vote.
    assert (exc["close"], exc["quorum"], exc["floor"], exc["records_dissent"], exc["rite"],
            exc["appeal_basis"], exc["disposal_reach"]) == (
        "declared", 2, "closed", False, "default", "determine", "realm")        # B24.09: the one default rite, which the six judicial and deliberative rows name
    assert [r for r, row in A.ARRANGEMENTS.items() if row["close"] == "declared"] == [
        "excommunication_deliberation"]
    assert exc["interposed"] == ("procedure", "ceremony") and exc["term_required"] is True
    # v10 SC-04: `negotiation`, the one `consent` close (was `mutual`) -- the deciders are the parties, so no bench
    # (`bench_basis: none`); §E.2's block (03_PARAMETERS.md:553-565) read key by key. `records_dissent: false`
    # is the reading `excommunication_deliberation` makes for an old false+given pair (kept: the key the
    # source writes), cited rather than re-decided; `succession` is CR-35's and is absent.
    neg = A.ARRANGEMENTS["negotiation"]
    assert (neg["close"], neg["bench_basis"], neg["floor"], neg["records_dissent"], neg["venue_min_rank"],
            neg["term_required"], neg["appeal_basis"], neg["rite"], neg["disposes"],
            neg["disposal_reach"]) == ("consent", "none", "closed", False, "hearth", False, "none",
                                       "negotiation", "oblige", "room")
    assert neg["interposed"] == () and neg["admits"] == ("record", "testimony") and neg["quorum"] is None
    assert neg["records_dissent"] == A.ARRANGEMENTS["excommunication_deliberation"]["records_dissent"]
    assert "succession" not in A.ARRANGEMENTS
    arb = A.ARRANGEMENTS["arbitration"]
    assert arb["close"] == "bench" and arb["appeal_basis"] == "none"
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
          - id:               summons
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            admits:             [testimony]
            disposes:           oblige
            disposal_reach:     room
            standard:     plain
    """)
    arrangements, _ = _reload_with(extra)
    # v9 SC-03a: the seeded count is read, not pinned (it was `== 4` at three seeded rows).
    assert "summons" in arrangements and len(arrangements) == len(A.ARRANGEMENTS) + 1


def test_a_fifteenth_key_fails_naming_the_row():
    extra = textwrap.dedent("""
        arrangements:
          - id:               bad_row
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            admits:             []
            disposes:           none
            disposal_reach:     room
            standard:     plain
            scale:              settlement
    """)
    with pytest.raises(SystemExit, match=r"bad_row.*unknown key.*scale"):
        _reload_with(extra)


def test_a_declared_disposal_row_with_no_quorum_fails_the_load():
    extra = textwrap.dedent("""
        arrangements:
          - id:               vote
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          declared
            bench_basis:        determine
            floor:              closed
            records_dissent:    true
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            admits:             []
            disposes:           none
            disposal_reach:     room
            standard:     plain
    """)
    with pytest.raises(SystemExit, match=r"vote.*no `quorum:`"):
        _reload_with(extra)


def test_a_declared_disposal_row_with_a_quorum_loads():
    extra = textwrap.dedent("""
        arrangements:
          - id:               vote
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          declared
            bench_basis:        determine
            floor:              closed
            records_dissent:    true
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            admits:             []
            disposes:           none
            disposal_reach:     room
            standard:     plain
            quorum:             0.5
    """)
    arrangements, _ = _reload_with(extra)
    assert arrangements["vote"]["quorum"] == 0.5


def test_quorum_on_a_non_declared_row_fails_the_load():
    extra = textwrap.dedent("""
        arrangements:
          - id:               stray_quorum
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          bench
            bench_basis:        determine
            floor:              closed
            records_dissent:    false
            venue_min_rank:     hearth
            term_required:      false
            appeal_basis:       none
            interposed:         []
            admits:             []
            disposes:           none
            disposal_reach:     room
            standard:     plain
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
    reported = _verbs.arrangements_without_a_disposal_opener()
    assert reported == [], reported
    assert "parliamentary_debate" not in reported and "council_of_state" not in reported, (
        "a `Record`-disposing row is not asked of the tenure-kind opener map")


def test_a_negotiation_reaches_eff_oblige_the_opener_of_the_kind_it_disposes(monkeypatch):
    """v10 SC-04: the seeded `negotiation` row (`close: consent`, was `disposal: mutual`; `disposes: oblige`) is only as good as
    its opener. Hand-built, end to end: the kind it disposes is opened by the real `oblige` act through
    the fold (`loop/effects_governance.py::_eff_oblige` -> `duty.taken`, one live `oblige` edge), and
    C-1 reads that opener. CONTROL: with `oblige`'s opener map emptied C-1 names the row (a `consent` row
    asks for `oblige`'s opener alone; `arbitration`, which `determine` opens `oblige` for, is named too, and so is `audience`, which disposes `oblige` too),
    so its absence from the report is the opener's."""
    from ..data.verbs import _OPENERS_FROM_EFFECTS
    from ..harness import probes as P
    row = A.ARRANGEMENTS["negotiation"]
    assert row["close"] == "consent" and row["disposes"] == "oblige"
    assert "negotiation" not in _verbs.arrangements_without_a_disposal_opener()
    w = P.tiny_world()
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "oblige", payload={"subject": "off_dicastery"})]
                                    if p.id == "p_low" else []))
    edges = [t for t in w.tenures if t.kind == row["disposes"] and t.subject == "p_low" and t.live]
    assert [t.object for t in edges] == ["off_dicastery"] and "duty.taken" in {e.kind for e in w.log}
    monkeypatch.setitem(_OPENERS_FROM_EFFECTS, "oblige", ())
    assert _verbs.arrangements_without_a_disposal_opener() == ["arbitration", "negotiation", "audience"]


def test_a_hold_disposing_row_is_reported_by_c1_until_determine_can_open_a_hold(monkeypatch):
    """v9 SC-04's `succession` row (`disposes: hold`, so a rival's petition over a VACANT throne can be
    docketed and `determine`d) is NOT SEEDED, and this is why, executed: the row is well-formed and loads
    through the unmodified loader, but `determine` has no site that opens a `hold` -- `_disposal` constructs
    `oblige`, `detain` and `ban` only -- so C-1's report names it. Seeding it today would also put `hold` in
    `state/gate.py::DISPOSABLE_KINDS`, admitting a bench's opening of a `hold` on its own seat that no
    effect produces, and let `open_case` dock a matter `determine` declines forever (the wedge
    `_eff_open_case` guards).

    CONTROL: the shipped rows report nothing (`[]`), so the report below is the planted row's.
    FALSIFIER: this goes red the day a `determine` site opens a `hold` -- the opener map then reads
    `determine` beside `hold`'s other openers and the report is empty again. That is the signal to seed
    the row (IN-61 builds the tribunal route; `state/gate.py`'s determination clause also asks the
    edge's object to be the judging seat, which a vacant throne is not -- a judge cannot sit one)."""
    from ..data.verbs import _OPENERS_FROM_EFFECTS
    extra = textwrap.dedent("""
        arrangements:
          - id:               succession
            rite:               trial
            turns:              [2, 5]
            authority:          polity
            reason_lean:        0
            close:          bench
            bench_basis:        determine
            floor:              admitted
            records_dissent:    true
            venue_min_rank:     duchy
            term_required:      false
            appeal_basis:       none
            interposed:         [procedure]
            admits:             [record, testimony]
            disposes:           hold
            disposal_reach:     realm
            standard:     plain
    """)
    monkeypatch.setitem(A.DISPOSAL, "hold", A.DISPOSAL["oblige"])    # B24p.03: a row must name a `disposal:` row; the hold has none shipped (the planted row is the question)
    arrangements, _ = _reload_with(extra)
    row = arrangements["succession"]
    assert row["disposes"] == "hold" and row["close"] == "bench"      # it loads
    assert _verbs.arrangements_without_a_disposal_opener() == []              # the control
    monkeypatch.setitem(A.ARRANGEMENTS, "succession", row)
    assert _verbs.arrangements_without_a_disposal_opener() == ["succession"]
    assert "determine" not in (_OPENERS_FROM_EFFECTS.get("hold") or ()), _OPENERS_FROM_EFFECTS.get("hold")
