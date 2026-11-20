# CENSUS C1B · wires: two readings that are tested and that nobody can run, and one gap in a carried wire

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row C1B_02 CONFORMS, §7 COMPLETE but for the tier; `unified/U3_DEPENDENCY_ORDER.md` §1 item 36, §3.1, §4.1 row 87, §5.1 rows `arc.py` and `aperture.py`; `unified/U5_CONFLICTS_U5a.md` C-U5a-17). Changed: W-3 is marked decided (reading 1, now in `09_WR_threadwork_module.md`'s own `Reconciled:` line); the dependency, batch and tier lines. One U3 row corrected at the tree: §4.1 row 87 and §1 item 36 move "W-2" to B39 as "the `arc.py` build-on-case item"; W-2 edits `aperture.py` only and depends on nothing in `12_ARCS_case_on_the_realm.md` (U3's own file census orders `aperture.py` B36 → B37), while the `arc.py` item is W-1, which builds on no case. The order constraint the cut expresses is that `12_ARCS_case_on_the_realm.md`'s `match_beats` (B39) lands after W-1's entry. So both W-1 and W-2 land in B36.

Depends on: `09_WR_threadwork_module.md` (B03; W-3's reading carried there); `09_WR_B_threadwork_session_and_practitioner.md` (B35); `09_WR_B_readings_of_closure_and_tension.md` (B36, which also edits `arc.py`: W-1 lands after it in B36). `12_ARCS_case_on_the_realm.md` (B39) depends on W-1, not the reverse.
Lands in batch: B36 (lane IN), W-1 and W-2 one commit each.
Tier: sonnet / high.

## Status: PROPOSED

Carries `audits/17_CENSUS_C1B.md` §3.2. Of the 23 rows read as broken, 20 are already carried and are
not restated here: the threadwork oracle (18 rows) by `09_WR_threadwork_module.md` and
`09_WR_B_threadwork_session_and_practitioner.md`; the army presets (2 rows) by
`04_MB_playable_field_scenario.md` (MB R-07). This file writes the two wires no document carries (W-1,
W-2) and names one gap in a carried wire (W-3).

## What it changes in `engine/season/` at runtime

**Nothing in the loop.** Two harness files gain a printed reading (`harness/arc.py`,
`harness/aperture.py`). Both are driver-side readers of a finished world: no world write, no registry,
no module, no state. Content hash EQUAL by construction.

## W-1 · the arc reader gets an entry (`engine/season/harness/arc.py`)

**Problem.** `read_arcs` and its one real clause-(1) predicate, `ambition_thrusts`, are called by
`engine/season/tests/test_cl_thrust_b01_arc_reader.py` and by nothing else (`grep -rn "read_arcs("` over
`engine tools proposals`: the test file only). `arc.py` has no `__main__`. Every other reader in the
harness is run as `python -m engine.season.harness.<name>`; this one can only be reached by writing a
probe by hand, which is how `audits/09_WR_audit.md` R-10 got its count. Two suite proposals build on the
file (`12_ARCS_case_on_the_realm.md` adds `match_beats`; `09_WR_B_readings_of_closure_and_tension.md`
edits it), so its reading has to be something a session can run and quote.

**Edit, at the single owner.** Append to `arc.py`:

```python
def main(argv=None) -> int:
    """`python -m engine.season.harness.arc --seed S --seasons N`: persons with an arc, by four readings."""
    import argparse
    from . import storybar as SB            # lazy, as `read_arcs` already imports it: storybar builds the realm
    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--seasons", type=int, required=True)
    ap.add_argument("--arm", choices=SB.ARMS, default=SB.ARMS[0])
    ap.add_argument("--cap", type=int, default=None)
    args = ap.parse_args(argv)
    w, d, _bounds = SB.drive(args.seed, args.seasons, args.arm, args.cap)
    on = ambition_thrusts(w)
    read = read_arcs(w, d, on)
    print(f"arc seed={args.seed} seasons={args.seasons} arm={args.arm} cap={args.cap}")
    print(f"  actors                       {len(read.persons)}")
    print(f"  no predicate (control)       {read_arcs(w, d).count()}")          # must be 0
    print(f"  on an ambition's thrust      {read.count()}")
    print(f"  shuffled-causes null         {read_arcs(w, d, on, log=shuffled_causes(w.log, args.seed)).count()}")
    print(f"  rosters ignored (upper bound) {read_arcs(w, d, on, unrestricted=True).count()}")
    print(f"  on-thrust acts behind a death {sum(len(v) for v in read.deaths.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Same argument names and the same `SB.drive` call as `harness/chronicle.py:204-227`, so the two readers
are run alike. No new function: `read_arcs`, `ambition_thrusts` and `shuffled_causes` exist and are
tested. Seed and seasons are required, as `chronicle` requires them.

**Gate (execution artifact).** `PYTHONHASHSEED=0 python -m engine.season.harness.arc --seed 0 --seasons 2`
exits 0 and prints, on today's tree (measured by hand for this proposal, audit §5 run 4): actors 83;
control 0; on an ambition's thrust 21; shuffled null 1; rosters ignored 53.

**Falsifier.** The control line. `read_arcs(w, d)` with no predicate must read 0 for every seed; a
non-zero control means the reader counts acts that are on no thrust. And the null: if the shuffled
count is not well below the real one across seeds 0 to 4, the reading is not about causes.

**What the entry does not settle.** `ambition_thrusts` carries its own `[ASSUMPTION; medium; Jordan to
correct: a thrust is an ambition]` (`arc.py:55-58`), and WR R-10 reads the 21 as utterances, not
climbs, until the thrust ladder has content. The entry makes that number reproducible; it does not make
it mean more.

## W-2 · `foreign_kinds` is printed where `unrowed_acts` is (`engine/season/harness/aperture.py`)

**Problem.** `corpus_run.foreign_kinds(w)` counts, per `(verb, kind)`, the Events that name an act in
`causes[]` and whose kind is in neither of that act's row's columns (`emits`, `emits_on_refusal`): what an
act's Events say that its verb row does not declare. It is the executed form of the question census C4
asks by name-matching. Its sibling, `unrowed_acts`, is in `aperture`'s measured dict (`aperture.py:583`)
and printed (`:1005`). `foreign_kinds` has tests (`test_aperture.py:225-230`) and no reader.

**Edit.**

- `aperture.py:125`: add `foreign_kinds` to the `from .corpus_run import …` line.
- `aperture.py:583`: add `"foreign": {f"{v} -> {k}": n for (v, k), n in sorted(foreign_kinds(w).items())},`
  beside `"unrowed"` (string keys, because the dict is also pooled and reported).
- `aperture.py:1005`, after the UNROWED line:
  `out.append(f"  FOREIGN  Events of a kind the acting verb's row declares in neither column: {m['foreign'] or 'none'}")`.
- `pool_worlds` (`aperture.py:793`): sum `foreign` across seeds as it sums `wrong_kind` (a Counter over
  the string keys).

**Gate.** `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 3 0` prints the FOREIGN line.
Measured for this proposal (audit §5 run 5): the populated realm, seed 0, 3 seasons, 2,630 acts and
74,510 events: `none`, with UNROWED 0. One seed, so a count.

**Falsifier.** `test_aperture.py:230` already plants `("speak", "transfer.made")` and reads 1, so the
reading can see what it excludes. If the line ever prints a pair, a verb row's `emits` is short of what
the effect writes, and the correction is the row in `engine/season/verb_table.yaml`, not the reader.

## W-3 · a gap in a carried wire: collective and opposed workings move without an entry

`09_WR_threadwork_module.md` moves `systems/threadwork/sim/collective.py` and `opposing.py` to
`modules/threadwork/` and changes their signatures to `tuple[Practitioner, ...]` (edit 2). It adds one
composition row, `threadwork.work`; the addendum's proposal makes it three (`work`, `read`, and the
session's). None is for a working by several practitioners or against one. After the move both files
are what they are today, reached by `tests/valoria/test_threadwork_mending_parity.py` alone, now inside
`modules/`, where "registered module" means reached by a composition row.

**Decision (ladder step 4: the rule `09_WR_B_threadwork_session_and_practitioner.md` itself cites as
`ID-13`, "a role no caller requires is not declared"; this lane did not open `ID-13` at its source).**
They do not get a composition row until a host needs one. So the WR proposal must say
which of two things is true, and this lane's reading is the first:

1. **They are inputs to `work`, not entries.** A collective working is `WorkingInput` with
   `helpers: tuple[Practitioner, ...]`; an opposed working is `WorkingInput` with
   `opposed_by: Optional[WorkingInput]`. `work` calls the two files' arithmetic. One entry, one outcome
   record, and the session proposal's contact loop reaches both as soon as a second practitioner is in
   the scene. The two files then have a caller on the day they move.
2. They stay behind in `systems/threadwork/sim/` as oracle until a verb needs them, and only
   `operations.py` and `coherence.py` move.

Either removes the state "moved into `modules/` and still test-only". This is an edit to another lane's
proposal, so it is listed for the unification stage (U3), not made here.

**Decided (`unified/U5_CONFLICTS_U5a.md` C-U5a-17): reading 1.** `09_WR_threadwork_module.md`'s head now
reads edit 2 as moving `collective.py` and `opposing.py` as inputs to `work` through
`WorkingInput.helpers` and `WorkingInput.opposed_by`, with no composition row of their own. Nothing in this
file is built for W-3.

## NERS reading

- **N.** W-1 and W-2 add no mechanism: each prints a reading that already exists and is tested. Cut
  them and the readings stay unreachable except by hand-written probes, which is the present state.
- **R.** Neither touches play. Both serve the no-player half indirectly: they are how a session sees
  whether persons' acts form arcs and whether a verb's Events match its row.
- **S.** W-1 uses `chronicle`'s arguments and `storybar.drive`; W-2 uses `aperture`'s existing block.
  No second way to run a reader, no second report.
- **E, last.** About 25 lines in `arc.py`, 4 in `aperture.py`, against two readings made runnable.

## Cost class

Edit (both). Covering tests at the close: `engine/season/tests/test_cl_thrust_b01_arc_reader.py`,
`engine/season/tests/test_aperture.py`.
