"""RE-HOSTED, A NAMED SUBSET -- plan position `18` (PROC-A), part 5.

`proposals/2026-09-05-proceedings-subsystem/stress/stress_proceedings.py` (NOT
`2026-09-01-season-loop-tests/stress/` -- the plan's own citation is one directory off, corrected
here) targets `proposals/2026-09-01-season-loop-tests/tracer/shape.py`, which does not exist
(`references/restructure_ledger.md:1821-1822` -- it was absorbed into `engine/season/`). Its header
says "twenty-eight logical stress tests"; ST-01..ST-38 are its own case ids (`grep -c` confirms 38),
and `20_STRESS_TESTS.md`'s own summary line is *"38 stress tests · BLOCKED 14 · FAILED 13 · RAN 11 ·
28 findings"* -- 28 is the FINDINGS count (F-01..F-28), not the case count. Both this plan and the
old one inherited the stale header number verbatim; corrected rather than silently carried forward
(`CLAUDE.md` §0.1 pt 3).

⚠ TEN OF THIRTY-EIGHT, NAMED SCOPE-DOWN (five at plan position `18`; v9 SC-04 re-hosted five more -- `ST-09`,
`ST-10`, `ST-14`, `ST-15`, `ST-26` -- now that SC-01 (`speak`, the social-contest provider) and SC-03
(`determine`'s disposal, `via`, `release`) are built). Porting all 38 faithfully -- several are multi-step
narrative traces (`ST-31`, "one worked trial, step by step, until it stops"; `ST-35`/`ST-36`,
byte-identical replay and permutation) that would need the season driver, a populated bench and a
docketed matter all at once, which is more build than this position's remaining budget affords. The
first five below are the ones THIS position's own five parts directly resolve or reverse, so re-hosting
them is checking THIS commit rather than inventing new engine surface to trace through. Each is an
EXECUTION against a real `World`/`engine.season` API, per the old plan's own instruction, never a
manufactured pass: several assert the CURRENT tree's real, disclosed gaps (C-1, the games still
unseeded -- nine of twelve when written, five since v9 SC-03a, four since v9 SC-04) rather than a flattering result.

NOT PORTED, NAMED RATHER THAN SILENTLY DROPPED (28 of 38): `ST-01·02·05·06·07·11..13·16..22·24·25·27..29·
31..38`. v9 SC-04 tried to re-host only the cases SC-01/SC-03's machinery lets run against the real
`World` and left the rest, WITH THE REASON EACH CASE'S OWN `by=` TAG AND TITLE GIVE (read from
`stress_proceedings.py`'s decorators, NOT from an attempted re-host -- a reason below is a classification,
not a measurement):
  * NOT AN ENGINE EXECUTION (`by="document"`): `ST-06` (design prose against the old tracer's source
    text), `ST-13`, `ST-16`, `ST-17`, `ST-27` -- a re-host would compare two documents, or one document
    to a file that no longer exists, and call it a pass.
  * A STAND-ALONE PROBE, NOT THE WORLD (`by="probe-model"`): `ST-22`, `ST-24`, `ST-28`, `ST-29`, `ST-34`
    (the case this batch's composed obstacle touches most: a floored pool against it; classified, not attempted).
  * A DOCUMENT-COUNT / REGISTRY CHECK: `ST-37`, `ST-38`.
  * THE SEASON DRIVER END TO END, a worked narrative, replay or permutation: `ST-31`..`ST-33`, `ST-35`,
    `ST-36`, and `ST-05`
    (a fired Date docketing across two seasons).
  * NOT ATTEMPTED (a construction case whose machinery SC-04 did not examine, so no reason is claimed
    beyond that): `ST-01`, `ST-02` (the old seam's `contest` signature), `ST-07`, `ST-11`, `ST-12`,
    `ST-18`..`ST-21`, `ST-25`.
Re-hosting any of them against a tracer that does not exist would either fabricate a second tracer (out of
scope) or manufacture a pass against machinery not yet built (`CLAUDE.md` §0.1 pt 3 row 1's exact hazard)."""

from __future__ import annotations


from ..data import arrangements as A
from ..data.verbs import VERB_TABLE
from ..queries import world_q


# ---------------------------------------------------------------------------------------------
# v9 SC-04: FIVE MORE, each an execution against the real fold, gate and loaders on `probes.tiny_world`
# (`p_high` holds `off_duke`, the judging seat; `p_low`, `p_mid` live in `Hh`). The world, the fold and the
# acts are `test_u7_remit.py`'s and `test_sc01_speak.py`'s own helpers, imported, not re-typed.
# ---------------------------------------------------------------------------------------------
import dataclasses                                                       # noqa: E402

from ..data.rosters import DEGREE_BANDS                                 # noqa: E402
from ..state.carriers import Act as _Act                                 # noqa: E402
from ..state.carriers import Proposition, Tenure                         # noqa: E402
from .test_sc01_speak import _docket, _speak                             # noqa: E402
from .test_u7_remit import (                                             # noqa: E402
    JUDGE, OPENS, PARTY, SEAT, _determine, _edges, _fold, _kinds, _open, _petition, _world,
)


def test_st09_a_speak_reaches_resolve_and_emits_and_a_seatless_person_speaks():
    """RE-HOSTS ST-09 (`04_VERBS.md` §B.1). The tracer's finding was that a `speak` folded and emitted a
    kind naming it, by the LIVE row, with `writes: []`, and that *eligibility is `own`, so a person holding
    no seat speaks -- there is no spectator mode*. THE STANDING HALF HOLDS; WHAT CHANGED is that the row now
    has a typed docket cell and four degree-keyed emissions, so the emission is the band's. The speaker
    holds no seat (asserted, not assumed), the matter is docketed, and the one Event the speech emits names
    the speech act and carries the band its kind belongs to.
    CONTROL (one clause away): the same speech BEFORE the matter is docketed emits `speech.unheard` and no
    degree -- so the emission above is the docket's reading, not every `speak`'s."""
    row = VERB_TABLE["speak"]
    w, d = _world()
    held = [t for t in w.tenures if t.subject == "p_low" and t.kind == "hold" and t.live]
    assert held == [], held                       # the speaker sits in no seat
    before = _fold(w, d, _speak("st09_pre"))
    assert _kinds(before) == ["speech.unheard"] and before[0].degree is None
    _docket(w, d)
    out = _fold(w, d, _speak("st09"))
    assert len(out) == 1, _kinds(out)
    e = out[0]
    assert e.degree in DEGREE_BANDS and e.kind in row.emits_at(e.degree), (e.kind, e.degree)
    assert "st09" in e.causes, e.causes           # the Event names the act that caused it


def test_st10_a_contested_speak_reaches_a_provider_and_comes_back_graded():
    """RE-HOSTS ST-10 (`04_VERBS.md` PART C / `08_SEAM.md`). The tracer's finding was the seam REFUSING a
    contested `speak` -- `Unspecified`, *no provider and no margin* (F-10, blocking). REVERSED: `speak` is
    `contests: a matter`, the prize is routed to a provider, and the fold returns a graded Event instead of
    raising. Asked of the real fold across a spread of speakers' dice, so that more than one band occurs and
    the grading is observed to VARY (a constant degree would be a provider that answers nothing): the loop
    asserts it asserted, and that it saw at least two bands.
    CONTROL: the row names a prize, and the roster `contest_subsystems` has a provider for it."""
    assert VERB_TABLE["speak"].contests == "a matter"
    from ..data.rosters import roster_map
    prizes = roster_map("contest_subsystems", "prizes")
    assert "a matter" in prizes, sorted(prizes)
    seen, folded = set(), 0
    for pool in (1, 2, 4, 8):
        w, d = _world()
        w.persons["p_low"].capability = {"copying": pool}
        _docket(w, d)
        for i in range(10):
            out = _fold(w, d, _speak(f"st10_{pool}_{i}"))
            assert len(out) == 1 and out[0].degree in DEGREE_BANDS, [(e.kind, e.degree) for e in out]
            seen.add(out[0].degree)
            folded += 1
    assert folded == 40 and len(seen) >= 2, (folded, sorted(seen))


def test_st14_a_verdict_is_a_tenure_its_determiner_opened_and_disposes_has_a_writer(monkeypatch):
    """RE-HOSTS ST-14 (`00_DERIVATION.md` §A.6). The tracer's finding (F-14, blocking): `determine` can
    GRADE a Tenure and cannot OPEN one, so *`disposes:` NAMES A WRITE AND HAS NO WRITER*. REVERSED by v9
    SC-03: `_eff_determine` opens the kind the docketed row `disposes:`. Asked of every seeded row that
    disposes a Tenure kind -- the seven, `excommunication_deliberation` (SC-04's row) and `negotiation` (B10-13 SC-04's) among them -- through the
    real fold: the matter is docketed under the row, a strong judge determines it, and ONE live edge of
    exactly the row's kind appears, owned by the party, on the seat exercised, graded at the band the
    contest decided, and no edge of any other disposal kind. The loop asserts it asserted (seven rows; six before the B10-13 pin commit's `negotiation`).
    THE HALF THAT IS STILL OPEN: the two `Record`-disposing rows (`parliamentary_debate`, `council_of_state`)
    have no writer -- `open_case` REFUSES to dock under them (`case.refused`), asserted below, so the gap is
    observed and not skipped."""
    from ..state.gate import DISPOSABLE_KINDS
    disposal_kinds = ("oblige", "detain", "ban")
    checked, record_rows = 0, []
    for name, row in sorted(A.ARRANGEMENTS.items()):
        w, d = _world(**JUDGE)
        if row["disposes"] not in DISPOSABLE_KINDS:
            record_rows.append(name)
            assert _kinds(_fold(w, d, _open("oc", arrangement=name))) == ["case.refused"], name
            continue
        assert _kinds(_fold(w, d, _open("oc", arrangement=name, petition=_petition(w)))) \
            == ["case.opened"], name
        if row["disposal"] == "declared":
            # v11 CR-34: a declared row needs its `quorum` of the bench's live commits to an OUGHT about the party
            # naming the kind it disposes; `tiny_world`'s bench is the Duke alone, so the row is read at quorum 1
            # and he is the one vote (the clause itself is `test_cr34_declared_disposal.py`'s).
            monkeypatch.setitem(row, "quorum", 1)
            w.propositions["prop_vote"] = Proposition("prop_vote", "OUGHT", PARTY, row["disposes"], True, 0)
            w.add_tenure(Tenure("cm_vote", "p_high", "prop_vote", "commit", since=0))
        out = _fold(w, d, _determine("dt"))
        assert _kinds(out) == ["matter.determined"] and out[0].degree in OPENS, (name, _kinds(out))
        edge, = _edges(w, row["disposes"])
        assert edge.live and edge.degree in OPENS, (name, edge)
        assert all(not _edges(w, other) for other in disposal_kinds if other != row["disposes"]), (
            name, [(t.kind, t.subject) for t in w.tenures if t.object == SEAT])
        checked += 1
    assert checked == 7, checked      # B10-13 pin commit (SC-04's `negotiation` row): was 6
    assert record_rows == ["council_of_state", "parliamentary_debate"], record_rows


def test_st15_an_adjudicator_acts_as_a_seat_and_a_private_opinion_is_not_a_determination():
    """RE-HOSTS ST-15 (`10_LOOPS_AND_GAPS.md` P-03). The tracer's finding (F-15, blocking): `Act` has no
    `via`, so *an adjudicator's determination is indistinguishable from a private opinion by the same
    person*. REVERSED: `Act.via` is a field, and the same `determine`, by the same judge, is a
    determination exactly when it is made THROUGH the seat he sits in. Three acts on worlds that differ in
    one clause: (1) via the judging seat -- executes; (2) the same judge, `via=None` -- refused, the private
    opinion; (3) a person who holds no seat, via that seat -- refused, a seat is not a string anyone may
    write. (1) is the control for (2) and (3): it is what a refusal excluding nothing would have failed to
    distinguish."""
    assert "via" in {f.name for f in dataclasses.fields(_Act)}
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]            # (1)
    assert _edges(w, "oblige")
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    out = _fold(w, d, _determine("dt_priv", via=None))                               # (2)
    assert _kinds(out) == ["determine.refused"] and not _edges(w, "oblige"), _kinds(out)
    out = _fold(w, d, _determine("dt_other", actor="p_low"))                         # (3)
    assert _kinds(out) == ["determine.refused"] and not _edges(w, "oblige"), _kinds(out)
    assert world_q.docketed(w, PARTY), "a refused determination took the matter off the docket"
    # the SAME world, the matter still docketed: the judge through his seat determines it -- so the two
    # refusals above were the missing seat's, not a world that could not determine at all.
    assert _kinds(_fold(w, d, _determine("dt_seat"))) == ["matter.determined"] and _edges(w, "oblige")


def test_st26_release_exists_so_a_duty_a_proceeding_imposes_can_be_discharged():
    """RE-HOSTS ST-26 (`04_VERBS.md` §B.5 / `ID-14`). The tracer's finding (F-26): `release` was ABSENT, so
    a duty a finding imposes was closable only by `repudiate` or a seat-holder's revocation. REVERSED:
    `release` is in the verb table and writes `Tenure.until`. B21.07 (A-37, VRES §4: an imposed service ends
    by the bench's `pardon` or its term, as detention and banishment do) OVERWRITES the convict's price that
    ST-26 first observed here: the party's `release` of the `oblige` the bench opened is now REFUSED
    (`_req_release`'s clause on an edge a determination opened), the edge still live, and so is his `release`
    of a `ban` the same bench opened (a restraint is not the holder's to discharge). What `release` closes
    is an edge the actor opened himself (`test_vb_a_formation.py`'s control)."""
    assert "release" in VERB_TABLE
    closers = sorted(v for v, r in VERB_TABLE.items() if "Tenure.until" in (r.writes or ()))
    assert "release" in closers, closers
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    duty, = _edges(w, "oblige")
    assert duty.live
    out = _fold(w, d, _Act(id="rl", actor=PARTY, verb="release", payload={"subject": SEAT}))
    assert _kinds(out) == ["release.refused"] and duty.live, _kinds(out)
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc", arrangement="tribunal", petition=_petition(w)))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    ban, = _edges(w, "ban")
    out = _fold(w, d, _Act(id="rl", actor=PARTY, verb="release", payload={"subject": SEAT}))
    assert _kinds(out) == ["release.refused"] and ban.live, _kinds(out)
