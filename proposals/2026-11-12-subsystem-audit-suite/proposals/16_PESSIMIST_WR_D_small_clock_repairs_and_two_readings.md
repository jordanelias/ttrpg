# WR — three small repairs to the clocks and two readings the story instruments lack

Reconciled: 2026-11-12, U5d closure — folded **A-40** and **A-47**. Edit 2 (`thread_read` forms on a Site) agrees with A-40 (one Site per territory). Edit 1 (a Date due in the past fires; `<=`) is a clock's tick and opens a question; where the question is one of the threshold arcs it is mandatory (A-47) and decides nothing by itself.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS: CALENDAR reads the tick and
does not advance it, `04` PART D 45), §2 (A-47 consistent), §7/§7b (the test files located in the tree: the CALENDAR file
is `engine/season/tests/test_sc01_fired_slot.py`; `tests/test_referent_class_stamps.py` does not exist and the
referent-class formation test is `engine/season/tests/test_in12_step9.py`, CP-T03-08's; tier); U3 B36, C3-K7 (serial
order on `harness/storybar.py`: after `09_WR_B_readings_of_closure_and_tension.md`, before `20_NARRATIVE_F_story_inventory_and_gate.md`),
§6.2 (`p4_small.txt`, `p2_*` and `p2_play.py` are lane scratch, not in the repository). Changed: the gates' file names
and test names, the cost line.

## Status: PROPOSED

Lands in batch: **B36** (WR). Depends on: `09_WR_B_readings_of_closure_and_tension.md` (B36; edit 4 lands with its
`by_act` / `by_clock` split), `09_WR_B_threadwork_session_and_practitioner.md` (B35; what edit 2's reading finds),
`16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 4 (B12; the Site referent edit 2 forms on). Serial edge
(C3-K7): edits `harness/storybar.py` after `09_WR_B_readings_of_closure_and_tension.md`, before `20_NARRATIVE_F`.

Source: `audits/16_PESSIMIST_WR.md` F-PES-WR-01, -04, -05, -09. Read at `d161a61`. Reference only
(`CLAUDE.md` §0.05). Lane WR. Five edits, each small, none a guard: three at a clock or a verb row, two
inside harness readers that already exist.

## What it changes in `engine/season/` at runtime

- Edit 1: a Date whose `due_at` has passed unfired fires at the next CALENDAR barrier, once. No committed
  world holds such a Date, so every base hash is expected EQUAL (asserted, not assumed).
- Edit 2: `thread_read` forms only on a place. It stops forming on Records and persons; with today's
  questions it then forms nowhere (declared: sideways, not progress), until a question carries a Site.
- Edit 3: nothing (a decided non-edit, recorded so the question is not re-raised).
- Edits 4 and 5: nothing at runtime; two readings in `harness/`.

## Edit 1 · CALENDAR fires what is due, not only what is due today (`loop/calendar.py:48`)

**Problem.** `if d.get("due_at") != w.tick: continue`. `runs/PES_WR/p4_small.txt` (PROXY: three Dates
planted at tick 2 on a seated venue, due at ticks 1, 2 and 3; four seasons, nobody acting): the two due
at 2 and 3 fire; the one due at 1 reads `fired=False` at ticks 3, 4, 5 and 6 and never forms a slot. A
computed `convene` always schedules `w.tick + 1` (`effects_governance.py:448`), so computed play does not
reach it; a `when` chosen by a player's host, a builder that starts mid-campaign and a planted corpus Date
do. MATTER met the same comparison twice and changed it both times, in its own words: "`<=`, NOT `==`,
AND ONCE" (CR-55, `matter.py:340`) and "`<=` and not `==`: a term that should have matured at a barrier
this world skipped … still lapses at the next one rather than living forever" (`:419-421`). Two siblings
on one comparison, read two ways, is the S defect.

**Old:**

```python
if d.get("due_at") != w.tick:
    continue
```

**New:**

```python
due = d.get("due_at")
if d.get("fired") or due is None or due > w.tick:
    continue
```

**Gate.** `engine/season/tests/test_sc01_fired_slot.py` (exists; the file covering CALENDAR's Dates) gains
`test_due_date_in_the_past_fires_once`: P4's three planted Dates (the scratch `p4_small` plant, written in the test)
all read `fired=True` after two barriers, each exactly one `date.fired`; and every committed golden is unmoved
(`report` / `delta HEAD`, `PROBE FLIPS 0`).
**Falsifier.** A Date fired twice, or a base hash that moves.

## Edit 2 · `thread_read` is aimed at a place (`engine/season/verb_table.yaml`, the `thread_read` row)

**Problem.** `runs/PES_WR/p2_*`: the verb executes 2 to 8 times a run; its subjects are Records (2, 5,
1, 1 across four arms) and persons (1, 2, 1, 3), once the reader himself in a small world, never a Site
or a rung; every finding carries no degree and observes only the reader's own gate
(`thread_sensitivity` 75, `.gate` 30); `rosters.yaml:3295-3296` says such a finding "reaches the row and
finds nothing". A reading of the Thread that is pointed at a letter and reports its own precondition is
not a smaller version of the premise; it is a different act under the premise's name.

**Edit.** The row gains `referent_class: Site`, on `restore`'s precedent (REM-22, the same file, with
the same declared consequence). With `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 4 (a
crossing a person stands beside carries the Site) the verb then forms where the fabric is strained, for
the four people who clear the gate. What it *finds* there is the `threadwork.read` entry of
`09_WR_B_threadwork_session_and_practitioner.md` (R-21), drawn; until that lands a formed reading still
finds nothing, and that is said in the row's note rather than hidden.

**Gate.** `engine/season/tests/test_in12_step9.py` (exists; it tests that a row declaring a `referent_class` forms
only on a referent carried as that class, CP-T03-08; the earlier name `tests/test_referent_class_stamps.py` is not a
file in the tree) gains `test_thread_read_forms_on_a_site_and_not_on_a_record`: a practitioner standing at a Site
named by his question forms `thread_read` on it; a question naming a Record forms none. **Falsifier.** A `thread_read` in any realm run whose subject is not a Site.

## Edit 3 · CALENDAR stays, and is marked unproven (no code edit)

`runs/PES_WR/p2_s0_k3_calendar.txt`: with barrier 1 removed for three seasons the realm's executed-verb
distance from the shipped arm is 38, against 316 between two chooser draws of the shipped realm; no
story reading moves. The cut is free today. It is **not taken**: the dated sitting is where a playable
hearing suspends (`05_SC_playable_hearing_B.md`) and where a determination is supposed to occur, and
both are other lanes' builds in progress. Decided at ladder step 5: keep the barrier; its N-line is
recorded as resting on `determine` executing (SC F-SC-01), and edit 5 gives the cheap reading that says
when it has become true.

## Edit 4 · the turn: who closed what another opened (`harness/storybar.py`)

**Problem.** No instrument reads a reversal. `runs/PES_WR/p2_play.py` part (e) does, in forty lines: for
every non-`contain` Tenure closed in the run, the act that opened it and the act that closed it, classed
as closed by its own subject, by another person, or by a clock. Three seasons, the shipped realm: at
seed 0, 19 edges closed, all 19 by their own subject, against 1,138 left open; at seed 1, 14 and 14,
against 1,160; **closed by another person's act: 0 at both seeds**; one death caused by an act (a
`capture`, seed 1). `revoke` 0 of 6, `seize` 0 of 14. The reading sees closures and sees the killing, so
the zero is observed and not unread.

**Edit.** `storybar.py` gains `turns(w, act_of) -> dict` with exactly that classification
(`{"by_subject": n, "by_another": n, "by_clock": n, "deaths_by_act": n}`), printed on the per-seed line
beside the executed summary. It reads the Tenure store, the log and `act_of`; it grades nothing and
stores nothing, as the module's header requires. It is the third column of the `by_act` / `by_clock`
split `09_WR_B_readings_of_closure_and_tension.md` edit 1 adds, and lands with it.

**Gate.** `engine/season/tests/test_storybar.py` (exists): `test_turns_counts_a_revocation_by_another`: a planted
world in which A confers and B revokes reads `by_another == 1`; the same world with A revoking his own grant reads 0.

## Edit 5 · a cut arm and the noise floor beside every comparison (`harness/storybar.py`)

**Problem.** `storybar.ARMS = ("off",)`; `09_WR_story_instruments_that_can_fail.md` adds forcing arms
(mechanisms switched *on*). Nothing switches a mechanism *off*, and nothing prints how far two draws of
one realm lie apart, so a comparison between arms cannot be told from noise. `draw_seed_arm` already
exists in the module (`:406`) and is not printed beside an arm comparison.

**Edit.** (a) `ARMS` gains `no_calendar` (the driver's CALENDAR step returns `[]`), composed as the
forcing arms are. (b) `compare` prints, per pair of arms, the L1 distance of the executed-verb counts
and, once per seed, the same distance between two draw seeds of the first arm. A reader then sees
`no_calendar 38 · noise 316` and knows what it means.

**Gate.** `engine/season/tests/test_storybar.py`: `test_no_calendar_arm_emits_no_date_fired` and
`test_compare_prints_a_nonzero_noise_line` on `build_realm`. **Falsifier.** The arm's distance exceeding the noise at two seeds once
`determine` executes is the signal that edit 3's N-line has become true; that is a reading, not a
blocking check.

## NERS reading (the five together)

- **N.** Edit 1: cut it and a sitting scheduled a season late is lost forever, silently. Edit 2: cut it
  and the setting's one executing thread verb keeps reading letters. Edits 4 and 5: cut them and the
  project still cannot say whether anything turned, or whether an arm differs from itself.
- **R.** Edit 1 is completeness at an extreme (a skipped barrier). Edits 4 and 5 serve the half with no
  player in it: they are how its absence is seen.
- **S.** Edit 1 makes the three clock comparisons one methodology. Edit 2 gives `thread_read` the
  referent grammar `restore` already has.
- **E** (last): three lines, one row key, two small functions.

## Cost class

Edits 1, 2: edit. Edits 4, 5: small build in an existing harness module. No guard, no new file. Tier: `sonnet`,
effort `high`. Hash movers declared: none expected for edit 1 (asserted); edit 2 moves any world in which
`thread_read` formed on a Record or a person (sideways, declared); edits 4-5 none. Lands it: B36, one commit per
edit; command `python -m pytest engine/season/tests/test_sc01_fired_slot.py engine/season/tests/test_in12_step9.py engine/season/tests/test_storybar.py -q`.
