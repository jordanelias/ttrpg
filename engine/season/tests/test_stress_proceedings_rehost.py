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

import inspect

from ..data import arrangements as A
from ..data.requires import REQUIRES_STEMS
from ..data.rosters import GENRES, INTERPOSITION_KINDS, LADDER_RUNGS, PROOFS
from ..data.verbs import VERB_TABLE
from ..queries import world_q
from ..state.world import World
from ..state.carriers import Rung
from ..harness.probes import tiny_world


def test_st03_the_bench_query_answers():
    """RE-HOSTS ST-03 (`00_DERIVATION.md` §A.4 / `04_VERBS.md` §B.2). The tracer's finding was
    `Query.judging_set` raising `Unspecified` unconditionally, on a two-parameter signature where
    the design specifies three. BOTH HALVES REVERSE: the live signature is
    `judging_set(w, venue, matter=None)` and it answers rather than raising."""
    live = list(inspect.signature(world_q.judging_set).parameters)
    assert live == ["w", "venue", "matter"], live
    w = tiny_world()
    seats = world_q.judging_set(w, "D")
    assert seats, "the bench Query still answers nothing -- ST-03 would still BLOCK"


def test_st04_there_is_an_occasion_to_attach_an_arrangement_to():
    """RE-HOSTS ST-04 (`08_SEAM.md` PART A / `03_PARAMETERS.md` PART D). The tracer's finding was
    that `arrangements.yaml` exists nowhere in the repo (`len(REPO.rglob('arrangements.y*ml')) ==
    0`) and that `Query.presence` was the only one of seven named functions with a live analogue.
    REVERSED IN PART: the file exists, loads, and carries real rows -- `genre_of` and a computed
    `latitude`/`reception` remain absent (PHASE 2/3 work, not this position's)."""
    assert A.ARRANGEMENTS_YAML.exists()
    assert A.ARRANGEMENTS, "arrangements.yaml exists but loads no rows"
    assert hasattr(world_q, "presence")
    # Honest about what is STILL absent, matching the old finding's own list where it still applies:
    still_missing = [n for n in ("occasion_at", "attendees_at", "genre_of")
                     if not hasattr(world_q, n)]
    assert still_missing == ["occasion_at", "attendees_at", "genre_of"], (
        f"one of these three now exists and this test is stale: {still_missing}")


def test_st08_the_scale_key_invariant_10_now_actually_fails_for_convene():
    """RE-HOSTS ST-08 (`03_PARAMETERS.md` §C.1 / `08_SEAM.md` D.2 invariant 10). The tracer's
    finding was that `convene` still carried `scale: 'settlement'`, the loader accepted it
    without complaint, and the ordinal replacement was inexpressible for want of a `venue`
    operand. ALL THREE REVERSE: the key is gone from the loaded row, and the replacement needed
    NO new operand -- `subject` already binds the rung (C-11, `21_RECONCILIATION.md:379`)."""
    convene = VERB_TABLE["convene"]
    assert not hasattr(convene, "scale") or True   # `VerbRow.scale` still exists as a dataclass
    # field (every row has one, defaulted); what ST-08 actually tested is the RAW YAML CELL, which
    # is what the loader reads BEFORE defaulting -- assert that directly.
    from ..data.files import VERB_TABLE_YAML
    from ..data.rosters import load_yaml
    raw = load_yaml(VERB_TABLE_YAML.read_text())
    cv = next(r for r in raw["verbs"] if r["verb"] == "convene")
    assert "scale" not in cv, f"`convene` still carries a raw `scale:` cell: {cv}"
    assert "rank" in REQUIRES_STEMS, "the ordinal replacement's stem was never declared"
    # And the ordinal actually refuses a person-rung venue, which is the whole point of the fix:
    w = World(world_seed=1)
    w.rungs["r_person"] = Rung("r_person", "person")
    from ..state.carriers import Act
    from ..loop.predicates import _req_convene
    assert _req_convene(w, Act(id="a1", actor="x", verb="convene", payload={"subject": "r_person"})) is False


def test_st23_the_loaders_schema_is_the_thirteen_keys_19_plan_step_11_derives():
    """RE-HOSTS ST-23 (`03_PARAMETERS.md` PART D / §E.2), REINTERPRETED. The original asked
    whether a MARKDOWN DOCUMENT's header word matched its own schema block's key count -- a
    prose-consistency question, already corrected in `03_PARAMETERS.md` itself (its own header
    note dated 2026-09-07), and not an `engine.season` execution at all. Re-hosted as the
    question that IS an execution: does the LOADER's own declared schema carry the count
    `19_PLAN.md` step 11 derives (fifteen minus `registers`/`verdict_reasons`/`stakes_grade`, plus
    `quorum` = thirteen), and does a row missing one of them fail to load."""
    assert len(A._ARRANGEMENT_KEYS - {"id"}) == 13, sorted(A._ARRANGEMENT_KEYS)
    for stale in ("registers", "verdict_reasons", "stakes_grade"):
        assert stale not in A._ARRANGEMENT_KEYS, (
            f"{stale!r} is a DELETED key (19_PLAN.md step 11) and must not be schema-legal")
    assert "quorum" in A._ARRANGEMENT_KEYS


def test_st30_five_of_the_designs_six_rosters_now_exist_two_named_absences():
    """RE-HOSTS ST-30 (`03_PARAMETERS.md` §F.1 / `00_DERIVATION.md` §B.1). The tracer's finding
    was that NONE of the design's closed rosters existed in `rosters.yaml`. MOSTLY REVERSED:
    `ladder_rungs`, `interposition_kinds`, `genres`, `proofs` and `speech_kinds` (in
    `arrangements.yaml`, this position's own reasoned split -- see that file's own header) now
    load. `registers` is correctly ABSENT: `19_PLAN.md` step 11 deletes it from the design itself
    ("the roster never existed, ... the idea folds into aptness"), so its absence is not a gap.
    `standing_routes` WAS a real, named absence here (no membership grounded in the cited corpus within
    this position's scope); it LANDED at v9 SC-02 `22a` with `19_PLAN.md` PHASE 3 step 20 ("route
    erosion"), the step this note named, so the assertion is re-written in that commit rather than
    deleted: the roster now observes `route ∈ {dominance, prestige}`, `dominance` listing deed kinds
    and `prestige` the complement (no list of its own)."""
    from ..data.rosters import _ROSTERS
    # Exact membership is `test_arrangements.py`'s job (and, for `ladder_rungs`, its own); this
    # re-hosts ST-30's EXISTENCE claim, not a fourth re-typing of four rosters' own values.
    assert len(LADDER_RUNGS) == 6
    assert len(INTERPOSITION_KINDS) == 6
    assert len(GENRES) == 3
    assert len(PROOFS) == 4
    assert A.SPEECH_KINDS, "speech_kinds carries no rows"
    assert "registers" not in _ROSTERS, "a DELETED roster (19_PLAN.md step 11) reappeared"
    # Was `"standing_routes" not in _ROSTERS` ("standing_routes now exists -- this test and PROC-A's
    # own record are stale"); the roster landed at SC-02 `22a` (step 20), so the claim is now its shape.
    from ..data.verbs import DEED_KINDS
    routes = _ROSTERS["standing_routes"]
    assert set(routes["values"]) == {"dominance", "prestige"}, routes["values"]
    assert set(routes["kinds"]) == {"dominance"}, (
        "`prestige` is the complement of `dominance` and carries no list of its own")
    assert routes["kinds"]["dominance"] and set(routes["kinds"]["dominance"]) <= DEED_KINDS, (
        sorted(set(routes["kinds"]["dominance"]) - DEED_KINDS))


# ---------------------------------------------------------------------------------------------
# v9 SC-04: FIVE MORE, each an execution against the real fold, gate and loaders on `probes.tiny_world`
# (`p_high` holds `off_duke`, the judging seat; `p_low`, `p_mid` live in `Hh`). The world, the fold and the
# acts are `test_u7_remit.py`'s and `test_sc01_speak.py`'s own helpers, imported, not re-typed.
# ---------------------------------------------------------------------------------------------
import dataclasses                                                       # noqa: E402

from engine.dice_engine.dice_engine import DEGREE_LABEL                  # noqa: E402

from ..state.carriers import Act as _Act                                 # noqa: E402
from .test_sc01_speak import _docket, _speak                             # noqa: E402
from .test_u7_remit import (                                             # noqa: E402
    JUDGE, OPENS, PARTY, SEAT, _determine, _edges, _fold, _kinds, _open, _petition, _world,
)

_BANDS = frozenset(DEGREE_LABEL.values())


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
    assert e.degree in _BANDS and e.kind in row.emits_at(e.degree), (e.kind, e.degree)
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
            assert len(out) == 1 and out[0].degree in _BANDS, [(e.kind, e.degree) for e in out]
            seen.add(out[0].degree)
            folded += 1
    assert folded == 40 and len(seen) >= 2, (folded, sorted(seen))


def test_st14_a_verdict_is_a_tenure_its_determiner_opened_and_disposes_has_a_writer():
    """RE-HOSTS ST-14 (`00_DERIVATION.md` §A.6). The tracer's finding (F-14, blocking): `determine` can
    GRADE a Tenure and cannot OPEN one, so *`disposes:` NAMES A WRITE AND HAS NO WRITER*. REVERSED by v9
    SC-03: `_eff_determine` opens the kind the docketed row `disposes:`. Asked of every seeded row that
    disposes a Tenure kind -- the six, `excommunication_deliberation` (SC-04's row) among them -- through the
    real fold: the matter is docketed under the row, a strong judge determines it, and ONE live edge of
    exactly the row's kind appears, owned by the party, on the seat exercised, graded at the band the
    contest decided, and no edge of any other disposal kind. The loop asserts it asserted (six rows).
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
        out = _fold(w, d, _determine("dt"))
        assert _kinds(out) == ["matter.determined"] and out[0].degree in OPENS, (name, _kinds(out))
        edge, = _edges(w, row["disposes"])
        assert edge.live and edge.degree in OPENS, (name, edge)
        assert all(not _edges(w, other) for other in disposal_kinds if other != row["disposes"]), (
            name, [(t.kind, t.subject) for t in w.tenures if t.object == SEAT])
        checked += 1
    assert checked == 6, checked
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
    `release` is in the verb table, writes `Tenure.until`, and the convict discharges the `oblige` the bench
    opened (`tenure.closed`, the edge no longer live). BOUNDED, and observed so: the same party's `release`
    of a `ban` the same bench opened is REFUSED (a restraint is not the holder's to discharge), so the
    discharge above is the `oblige`'s and not any edge's -- the control that makes the closure observable
    as a distinction."""
    assert "release" in VERB_TABLE
    closers = sorted(v for v, r in VERB_TABLE.items() if "Tenure.until" in (r.writes or ()))
    assert "release" in closers, closers
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    duty, = _edges(w, "oblige")
    assert duty.live
    out = _fold(w, d, _Act(id="rl", actor=PARTY, verb="release", payload={"subject": SEAT}))
    assert _kinds(out) == ["tenure.closed"] and not duty.live, _kinds(out)
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc", arrangement="tribunal", petition=_petition(w)))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    ban, = _edges(w, "ban")
    out = _fold(w, d, _Act(id="rl", actor=PARTY, verb="release", payload={"subject": SEAT}))
    assert _kinds(out) == ["release.refused"] and ban.live, _kinds(out)
