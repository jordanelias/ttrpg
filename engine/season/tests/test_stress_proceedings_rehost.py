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

⚠ FIVE OF THIRTY-EIGHT, NAMED SCOPE-DOWN. Porting all 38 faithfully -- several are multi-step
narrative traces (`ST-31`, "one worked trial, step by step, until it stops"; `ST-35`/`ST-36`,
byte-identical replay and permutation) that would need the season driver, a populated bench and a
docketed matter all at once, which is more build than this position's remaining budget affords. The
five below are the ones THIS position's own five parts directly resolve or reverse, so re-hosting
them is checking THIS commit rather than inventing new engine surface to trace through. Each is an
EXECUTION against a real `World`/`engine.season` API, per the old plan's own instruction, never a
manufactured pass: several assert the CURRENT tree's real, disclosed gaps (C-1, the unseeded nine of
twelve games) rather than a flattering result.

NOT PORTED, NAMED RATHER THAN SILENTLY DROPPED (33 of 38): `ST-01·02·05·06·07·09..22·24..29·31..38`.
Most need `speak`/`determine` resolution machinery (`19_PLAN.md` PHASE 2 steps 11-16), the docket
reader (PHASE 2 step 10, this position's own explicitly-deferred docketing decision) or the season
driver end to end -- none of which this position's five parts build. Re-hosting them against a
tracer that does not exist would either fabricate a second tracer (out of scope) or manufacture a
pass against machinery not yet built (`CLAUDE.md` §0.1 pt 3 row 1's exact hazard)."""

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
    `standing_routes` is a REAL, NAMED absence -- no concrete membership was found grounded in the
    cited corpus within this position's scope (`19_PLAN.md` PHASE 3 step 20, "route erosion",
    not this position's five parts)."""
    from ..data.rosters import _ROSTERS
    # Exact membership is `test_arrangements.py`'s job (and, for `ladder_rungs`, its own); this
    # re-hosts ST-30's EXISTENCE claim, not a fourth re-typing of four rosters' own values.
    assert len(LADDER_RUNGS) == 6
    assert len(INTERPOSITION_KINDS) == 6
    assert len(GENRES) == 3
    assert len(PROOFS) == 4
    assert A.SPEECH_KINDS, "speech_kinds carries no rows"
    assert "registers" not in _ROSTERS, "a DELETED roster (19_PLAN.md step 11) reappeared"
    assert "standing_routes" not in _ROSTERS, (
        "standing_routes now exists -- this test and PROC-A's own record are stale")
