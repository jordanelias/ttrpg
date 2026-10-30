# Stress test of the social contest subsystem and the debate surface of the season loop

## Status: **REFERENCE (2026-10-30).** A terminal pass whose verdict is the thing asked for, recorded beside the probes and logs that produced it (`CLAUDE.md` §0, the terminal-pass exception). It allocates no `ED`/`PP`, queues no work and changes no code. Every number below is read from a log in this folder; the logs are the audit record.

> **Asked (Jordan, 2026-10-30):** *"Stress test the subsystem as it currently stands then report accordingly"*, then *"we are supposed to be stress testing social contest subsystem specifically"*, then *"debate surface season loop still worthwhile"*, *"it doesn't require the number of seasons for testing or anything you assigned"*, and *"ensure you log what happens during stress test … for auditing"*.

## 0. What was tested, and what the result is

| surface | what it is | result in one line |
|---|---|---|
| **Module** `modules/social_contest/roll.py` | the live, registered σ-leverage roll (`obstacle`, `roll`) | **Held.** 75,132 edge-and-beyond inputs: no undocumented exception, no non-determinism, no global-RNG use, ceiling always respected. NaN/inf inputs flow through to NaN outputs unrefused |
| **Kernel** `systems/social_contest/sim/contest/` | the evaluated, not adopted, contest kernel | **Held under fuzz, with five findings.** 751,619 resolutions, no crash, no non-determinism under reseed; but it draws from the process-global RNG, fails on an empty panel and on a bad policy, and its proceedings differ enormously in how often the weaker side can win |
| **Season-loop debate surface** | `utter` / `argue` / `commit` / `oblige` / `convene` / `carry` / `determine` on `build_realm` | **Runs, and stays inert, and gets slower.** 13-14 seasons on seed 0: 0-1 matters determined, 4 commitments, 0 arguments; season cost grew 11.7×; the docket grew to 72 items, 43 of them empty slots that never fill |

## 1. Method, and what was deliberately not chosen

- **No chosen horizon or trial count.** The season-loop probe ticks each world until the *first* of: an exception, a season in which the log gained no event, or the caller's wall-clock budget. The social contest probe samples each section until its slice of the budget runs out and records the trial count `n` beside every rate. Seeds and seasons are therefore *outputs* of the run, not inputs. The one caller-supplied limit is the wall-clock budget.
- **Edge values** come from the code's own constants where it has them (`OB_MIN`, `Standing.START`, `Stasis.LADDER`, the `PROCEEDINGS` / `POLICIES` / `CANONICAL_ADJUDICATORS` keys) and otherwise from the edges of the field's type (0, 1, negative, huge, `None`, NaN, inf). They are inputs to try, not a claim about the legal domain.
- **Audit trail.** Each probe writes one flushed JSON line per event (`manifest` with HEAD, branch, Python and argv; `plan`; `section_start`; `season`; `seed_end`; `error` with the full traceback; a closing `summary`). Every anomaly carries the exact input and sampling seed, so it replays. `PYTHONHASHSEED=0` and `PYTHONUTF8=1` throughout.
- **Environment.** Windows 11, Python 3.14.4, native (no WSL), HEAD `79b7defa` on `parliament-resolution-design`, five probe processes running at once on one machine.

### Logs (all in this folder, all committed)

| file | probe | what it holds |
|---|---|---|
| `2026-10-30-stress-log-social-contest.jsonl` | `social_contest_stress.py` | suites, API edges, module grid, monotonicity, kernel fuzz, kernel properties. Includes the first suites attempt, which named a test file that does not exist, and the corrected rerun, so both are on record |
| `2026-10-30-stress-log-season-loop-base.jsonl` | `stress_probe.py` | shipped fixtures, seed 0, 13 seasons |
| `2026-10-30-stress-log-season-loop-rule-all.jsonl` | `stress_probe.py --rule all` | `question_aggregation_rule = all`, seed 0, 14 seasons |
| `2026-10-30-stress-log-season-loop-bench-quorum-3.jsonl` | `stress_probe.py --bench-quorum 3` | `bench_quorum = 3`, seed 0, 13 seasons |
| `2026-10-30-stress-log-season-loop-determinism.jsonl` | `stress_probe.py --determinism --seasons 2` | seed 0 built and run twice |

Reproduce: `python proposals/2026-10-29-parliament-and-debate/social_contest_stress.py --label X --budget-s 1800 --log OUT.jsonl` and `python proposals/2026-10-29-parliament-and-debate/stress_probe.py --label X --budget-s 2400 --log OUT.jsonl` (both from the repo root).

## 2. Findings

Severity is a judgment about the *game*, not the test: **FINDING** = a defect or a gap someone should decide on; **OBSERVATION** = true and worth knowing; **PASS** = an attack that failed.

### Social contest module (`roll.py`)

- **PASS: no undocumented failure.** 75,132 trials across the edges of every `SocialContestInput` field (pool −1 to 10,000; opposition `None`, negative, 1e9, inf, NaN; every ceiling including one below `OB_MIN`; leverage ±100 and NaN; hostile and favourable rooms; forgery). The only exception was the documented `ValueError` for a ceiling below `OB_MIN` (12,402 trials). Zero violations of: same seed gives same result, global `random` untouched when an `rng` is given, `ob` never above a valid ceiling.
- **PASS: monotone with tight intervals.** Success rate rises with pool (0.100 at pool 1 to 0.968 at pool 20, n between 389,200 and 1,294,200 per point) and falls with opposition (0.900 at Ob 0 to 0.001 at Ob 6). No significant violation on either axis.
- **OBSERVATION (corrected 2026-10-30): at a small pool, equal leverage readings are a rounding artifact, not a cap at one σ.** At pool 3 the success rate at leverage −2 is 0.05211 and at −1 is 0.05207; at +1 it is 0.68243 and at +2 is 0.68231 (n ≈ 1,000,000 each). This report first read that as `net_boost(capped=True)` clamping at ±1σ. It is not: the cap is `1.5·tanh(x/1.5)` (`M_MAX = 1.5`, `sigma_leverage.py:104,141`), which still moves between 1 and 2 (0.87σ → 1.31σ). The roll's net is a whole number and the boost is continuous, so at pool 3 both leverages land on the same integer threshold. Re-measured at pool 11 (n ≈ 145,000–200,000 per point): leverage −2 / −1 / +1 / +2 give 0.334 / 0.479 / 0.971 / 0.990, all different, and at pool 3 leverage +3 gives 0.8994 against 0.6816 at +2. Leverage saturates smoothly toward ±1.5σ, and its effect at small pools moves in whole-number steps.
- **OBSERVATION: non-finite inputs are not refused.** NaN or infinite operands produce NaN `net` (7,844 trials) and NaN `ob` (7,596) with no error. No finite input did. The host builder supplies these from `World`, so this is a guard question, not a live defect.
- **OBSERVATION: `rng=None` does not consume the process-global stream** (`random.seed(12345)` then `roll(inp, None)` leaves the next draw unchanged), so an unseeded call is not reproducible through `random.seed`.

### Social contest kernel (`build_contest` / `resolve_contest`)

- **PASS: robust under fuzz.** 751,619 resolutions over every proceeding, every adjudicator type, a panel of 1, 2, 3 and 9, every policy pair, and sides from `int` through `dict` with extreme standing and evidence weights. Zero exceptions, every return the documented `((band, reason), bout)` shape, zero results that differ when the same seed is replayed. Median resolution 0.24 ms, p99 1.6 ms, max 23 ms. `mechanics_selftest()` returns `(True, [])`; the three stub games return the documented `StubResult`; the kernel's own tests pass (`engine/tests/test_contest_kernel.py`, 1 passed in 27.6 s).
- **FINDING: it draws from the process-global RNG.** The global stream advanced in 646,997 of 751,619 first resolutions (86%). This is the known SC-05 reason it is not adopted (`roll.py`'s docstring; `04` PART D row 35 wants a per-act generator). Stated here with a rate: any in-process use perturbs unrelated randomness.
- **FINDING: three bad-input paths are not handled.** An empty `Panel` raises a bare `ZeroDivisionError`; a policy that returns `None` raises `AttributeError: 'NoneType' object has no attribute 'kind'`; an unknown policy name raises a message-less `KeyError`. A policy that raises propagates unchanged. Unknown proceeding, unknown adjudicator, unknown game, a bad side type and `use_tracker` with a prebuilt venue are all refused with clear messages.
- **FINDING (design question): proceedings differ hugely in how often the weaker side can win.** With faculty 1 against faculty 4 (n between 37,600 and 207,500 per proceeding), the weaker side's share of *decided* contests is: casual_dispute 21.6%, personal_appeal 21.6%, guild_arbitration 12.3%, private_negotiation 8.6%, church_tribunal 3.2%, royal_audience 1.0%, grand_contest 0.06%, formal_contest 0.04%. The stronger side won more in both seats in every proceeding. Whether near-deterministic formal and grand contests are intended is a design call.
- **FINDING (design question): most outcomes in several proceedings are not a side.** With equal sides the share of contests that end in a decided `a`/`b` is: formal_contest 0.6%, grand_contest 1.4%, royal_audience 15.1%, church_tribunal 34.2%; the rest are `committee`. The kernel emits four band families (`a`/`b`/`draw`, `A_decisive`/`B_decisive`, `A_total`/`B_total`, `committee`), so any consumer has to handle all of them.
- **FINDING (design question): church_tribunal is seat-asymmetric.** With equal faculty, side A wins 84.2% of decided contests (95% interval 83.7 to 84.8; A 15,997, B 2,993, n = 55,580). Every other proceeding's equal-side interval contains 0.5. This may be the intended petitioner/accused advantage; the kernel does not say.

### Season-loop debate surface

All three variants reached one seed only: a season costs minutes, so the budget ended the seed before a second began. That is stated, not hidden: these are **seed 0, 13 to 14 seasons**, not a population.

- **PASS: deterministic.** Seed 0 built and run twice for 2 seasons: identical event counts, identical content hash (`920da131…`). The first two seasons of the base run also match (docket 5 then 11, dates 4 then 11), so it holds across processes.
- **FINDING: season cost grows without bound in what was measured.** Wall time per season in the base run: 33, 70, 111, 148, 158, 162, 173, 205, 247, 295, 330, 325, 387 seconds, an 11.7× rise over 13 seasons, with the event log growing only about 30,000 events a season (282,575 to 347,446 at the last three readings). Five processes shared the machine for the whole run, so the absolute times are not a benchmark; the growth is. It is the same shape `soak.py` was written to catch and it was not stopped by a quiet world (no season was ever event-free).
- **FINDING: the docket fills with slots that never empty.** Docket items grew 5, 11, 18, 25, 34, 44, 49, 55, 61, 64, 67, 71, 72; empty slots grew 0, 4, 11, 17, 23, 32, 34, 38, 41, 41, 43, 43, 43. By season 13, 43 of 72 items are empty slots, and dates went from 4 to 51. This is the "sittings without matters" finding in `2026-10-29-reasons-to-convene.md`, now seen at a 13-season horizon rather than 4: nothing prunes the docket and nothing back-fills it.
- **OBSERVATION: the vote chain stays inert.** Over 13 seasons, base: 4 `commitment.made`, no `argument.*` event of any kind, 0 `matter.determined`, 18 `determine.refused`, 0 `rung.ceded`, 161 `duty.taken`, 86 `petition.filed`. With `bench_quorum = 3`: 6 commitments and 1 matter determined. This extends the resolution design's four-season reading (§2A) to thirteen seasons without changing its conclusion.
- **FINDING: the surface depends on `question_aggregation_rule`.** Under `all`: 3 `date.scheduled` against 51 (base), `duty.taken` 0 against 161, `petition.filed` 48 against 86, `give.refused` 45 against 37. Sittings and oaths collapse when every question is answered instead of one per round.

### Test infrastructure

- **OBSERVATION: `engine/season/tests/test_social_contest_module.py` cannot pass on native Windows.** 9 of 10 tests in the file set pass; the failing one builds its allowed-file list with forward slashes and compares it with `os.path.relpath` output, which uses backslashes on Windows. The "stray" files it reports are exactly the allowed ones in backslash form (`engine\dice_engine\...`). Not run on POSIX here, so that it passes there is inferred, not observed.
- **OBSERVATION: the probe's first suites attempt named `engine/season/tests/test_contest_kernel.py`, which does not exist**, and ran `_kernel_tests.py` under pytest, which collects nothing (it is a standalone script that `engine/tests/test_contest_kernel.py` wraps). Both attempts and the corrected rerun are in the log.

## 3. Limits, stated

- Season-loop results are **one seed**; none of them is a distribution. The probe is built to visit more seeds when given more budget, or run in parallel with less contention.
- Five concurrent processes inflate every absolute time. Ratios within a run are safe; comparisons across machines are not.
- The kernel is not adopted, so its findings are findings about a candidate, not about the shipped game. Only the module and the season loop are live.
- Nothing downstream of the module's `Margin` (`degree_from_net`, the seam adapter, the fold) was stressed.
- Windows only. The hang guard (`faulthandler`) was armed and never fired; stderr was empty for every run.
- No mutation testing, so "no violations found" says the checks as written did not fail, not that no check could be written that would.
