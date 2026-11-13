# 16 · PESSIMIST · CORE — the nine's gate checks what it says it checks, and R-01/R-02 get a reading with a control

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-01) — this file is the carrier of R-01's and R-02's `measure:`; `01_CORE_requirements_reading_record.md` §2 (a second instrument for the same property) is withdrawn.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (P:1 AMBIGUOUS against `04` U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "reading record" → "requirement reading"; "knockout" → "removal test" (glossary *reading*, *knockout*); "knockout" → "removal test" (glossary *removal test*; file names keep their words); `knockout_arm` → `removal_arm`, `--knockout` → `--remove`, `test_knockout_replay_arm_reads_zero` → `test_removal_replay_arm_reads_zero`. A-101 round lane (2026-11-12, `master/pc_round/PC_ROUND_SPEC.md`, glossary §D *lap*, §K): "round" in this file (`(tick, round)`, "at one round") is the season's within-season pass (`Claim.round`), now called a **lap** in prose; the identifier keeps its name until the rename candidate PCR-4.
§G.3.1: the regex tightening is the stopgap, the typed `reading:` record of `01_CORE_requirements_reading_record.md`
replaces it on landing), §7/§7b (named tests replace `req_forge.py`; signatures; tier); U3 C3-K5 (this file keeps
R-01/R-02 `measure:`; `16_PESSIMIST_GAME_consequence_reading.md`'s `requirements.yaml` edit is withdrawn), C3-K7
(serial order on `harness/storybar.py`), B02; U1 glossary *knockout* (plain word "removal test", defined at the call
site). Changed: gate restated on committed tests; `drive`'s real signature used (the 7b text named a `drive(base, …)`
that the tree does not have, `harness/storybar.py:288`).

## Status: PROPOSED

Lands in batch: **B02** (IN). Depends on: `01_CORE_requirements_reading_record.md` (B02, lands first: edit 1
here is its stopgap). Serial edge (C3-K7): edits `harness/storybar.py` **first**, before
`09_WR_story_instruments_that_can_fail.md`.

Carries F-PES-CORE-04 and F-PES-CORE-05 of `audits/16_PESSIMIST_CORE.md` (§3, §1.2). Composes on
`01_CORE_requirements_reading_record.md` (F-CORE-03: a typed `reading:` record per row); it does not
replace it. Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

**Nothing in the loop.** Two edits to instruments under `engine/season/harness/` and two `measure:`
strings in `engine/season/requirements.yaml`. No content hash moves.

## The problem (evidence)

**(a) `register --requirements` passes a forged file** (`req_forge.py`; the tracked file untouched,
`register.REQUIREMENTS` pointed at a scratch copy):

| scratch copy | exit | prints |
|---|---|---|
| the shipped file (control) | 0 | `met 3 · not_met 1 · partial 5` |
| every row `status: met`, `measured: x` | **0** | `met 9` |
| the same, every `measure:` naming `python -m engine.season.harness.no_such_module` | **0** | `met 9` |
| the same, every `measure:` a pytest line with `-k 'zz_no_such_test or import'` | **0** | `met 9` |
| the same, every `measure: true` | **0** | `met 9` |
| positive controls: a status word off the roster; a `python <path>.py` naming a missing file; a `-k` matching nothing | 1, 1, 1 | the violation |

Two of these are holes in the check the docstring claims to make (`harness/register.py:631-701`), not
only the known limit that nothing executes a `measure:`:

- the existence check matches `python3?\s+([\w./-]+\.py)`. **Six of the nine shipped measures are
  `python -m engine.season.harness.<x>`** and match nothing, so they are not checked at all;
- the `-k` check passes when **any one** name in the expression occurs **anywhere** in the concatenated
  test sources (`any(("def test_" in src) and (n in src) for n in names)`), not as a test's name. `import`
  satisfies it.

`tools/m1_acceptance.py::row_nine_requirements` reads the same strings and CI runs the same command
(`.github/workflows/valoria-ci.yml:447`), so `met 9` would reach the milestone row.

**(b) R-01 and R-02's `met` rests on a reading with no working control** (F-CORE-03). The cheapest
reading that could show the property false is a counterfactual, and it was run here (`knock.py 0 2`,
`knock2.py`; §1.2 of the audit has the table): suppress one `choose()` call of one person in round 0 of
season 0, replay everything else, and count the other persons' acts that differ. It takes about two
minutes an arm on the realm and separates three things the present instrument cannot: a decision that is
cited and changes others, one that is cited by nobody and still changes others, and the floor set by the
chooser's own draw.

## The resolution, decided

Fix the two holes so the shape check is at least the check it describes. Give R-01 and R-02 a `measure:`
a session can run, with its control arms in the same command. Do not make the gate execute measures
(a 25-minute instrument does not belong in a 0.5-second check; F-CORE-03's requirement reading is the owner
of "when was this last run and on what tree").

## Exact edits, by owner

1. **`engine/season/harness/register.py::check_requirements`**
   - a `python -m <module>` head: resolve `<module>` with `importlib.util.find_spec`; absent is a
     violation, with the same wording as the missing-file case;
   - the `-k` case: collect the test names once (`re.findall(r"def (test_\w+)", src)`); **every**
     identifier in the expression not under a `not` must be a substring of at least one test name;
   - a head matching none of `python <path>.py`, `python -m <module>`, `pytest … -k` is a violation
     (*"the measure is not a command this check can find"*), which closes `measure: true`.
   - The `-k` rule in code: `names = re.findall(r"[A-Za-z_]\w*", expr)`, drop `and`/`or`/`not` and every
     identifier directly under a `not`; each remaining name must be a substring of some name in
     `re.findall(r"def (test_\w+)", src)` over the test files named before `-k`.
   - **This edit is a stopgap** (`04` §G.3.1: a check is as strong as the representation it checks; a regex
     over a prose `measure:` string is the weak form). When `01_CORE_requirements_reading_record.md`'s typed
     `reading:` record (an `argv` list) has landed, the check reads the record and these regexes are deleted in
     that commit.
2. **`engine/season/harness/storybar.py`** — beside `draw_seed_arm` (same shape, same `fork`, same
   `drive`). Definition, written in the function's docstring and the `--help` text (CLAUDE.md §4): *a
   removal test: suppress one person's choice at one round and count how many of the other
   persons' acts differ from the unperturbed copy.* Signatures: `drive(seed, seasons, arm, cap=None,
   on_season=None, world=None, draw_seed=None, wrap_chooser=None)` (the existing signature,
   `storybar.py:288`, plus one keyword; `wrap_chooser(chooser) -> chooser`, default `None` = today);
   `removal_arm(base, seasons: int, who: str, when: tuple[int, int]) -> dict[tuple, int]`.
   `removal_arm(base, seasons, who, when)` runs the copy with the chooser wrapped to return
   no scene for person `who` at `(tick, round) == when`, and returns the multiset of the *other*
   persons' `(actor, tick, round, verb, opportunity, executed|refused)`; a `--remove PERSON` CLI
   switch prints, against the unperturbed copy: acts differing, persons affected, by `(season, round)`,
   with three control lines in the same output — **replay** (nobody removed: must be 0), **a cohort's
   scene**, and **`--draw-seeds`'s existing arm** (the floor). `drive` gains one optional parameter
   (`wrap_chooser`), default `None`, the shipped reading unchanged. About 40 lines; no new module.
3. **`engine/season/requirements.yaml`** — R-01 and R-02 `measure:` re-pointed to
   `python -m engine.season.harness.storybar --remove <most-cited person> --base-seed 0 --seasons 2`,
   keeping the corpus `R3` line as a second measure in the comment. The statuses are **not** changed by
   this proposal: what the reading supports is in the audit (§1.2, §3) and is Jordan's to read.

## Gate (an execution artifact, §0.2)

`req_forge.py` and `knock.py`/`knock2.py` were lane scratch and are not in the repository
(`U3_DEPENDENCY_ORDER.md` §6.2); the batch's first commit writes the forge as a committed test, and the gate
reads it:

- NEW `engine/season/tests/test_check_requirements.py` (a planted scratch `requirements.yaml` through
  `monkeypatch.setattr(register, "REQUIREMENTS", scratch)`; `register.REQUIREMENTS` exists,
  `harness/register.py:628`): `test_all_met_with_missing_module_exits_nonzero` (arm B),
  `test_k_expression_naming_only_import_is_refused` (arm C), `test_measure_true_is_refused` (arm D),
  `test_shipped_file_exits_zero` (the control). Command:
  `python -m pytest engine/season/tests/test_check_requirements.py -q`; expected: 4 passed. Written red
  against today's `check_requirements` for arms B-D (the defect), green after edit 1. (Arm A, a bare relabel
  to `met` with honest measures, still exits 0: that is the limit F-CORE-03's requirement reading addresses, and
  this proposal says so rather than claim it.)
- `python -m engine.season.harness.storybar --remove <most-cited person> --base-seed 0 --seasons 2`: the
  replay line prints 0 differing acts and the baseline hash; the knocked-out line is reported (the audit's
  seed-0 figure came from a scratch probe and is a comparison, not the expected reading). A planted case in
  `engine/season/tests/test_storybar.py` (exists): `test_removal_replay_arm_reads_zero`.

## Falsifier

The replay control prints a non-zero difference (the wrapper perturbs the run, and every figure in §1.2
is void), or arm B still exits 0.

## NERS reading (E last)

- **N.** The nine are the acceptance surface (`requirements.yaml`'s own words). A gate over them that
  accepts `met 9` on a module that does not exist is the one check whose failure would be invisible.
- **R.** Not a play mechanic; R is not scored.
- **S.** `removal_arm` uses `draw_seed_arm`'s method (one built world, forked, one thing varied), so
  the two readings are comparable line for line.
- **E.** Three predicates tightened and one function beside its sibling.

## Cost class

Edit (register), small build (storybar). No golden moves. Hash movers declared: none. Tier: `sonnet`, effort
`high` (no judgment node). Lands it: B02, after `01_CORE_requirements_reading_record.md`; one commit for edit 1
with its test file, one for edit 2, one for edit 3. The removal test costs about two minutes an arm and is a
manual instrument wired into no gate.

## Note on §0.1 pt 5

No guard is proposed. `check_requirements` exists and is already CI's; this makes its existing claim
true. `removal_arm` is a reading, wired into no gate.
