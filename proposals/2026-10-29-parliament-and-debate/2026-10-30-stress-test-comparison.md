# Stress tests of the three proposals: what held, what broke, what it changes

## Status: REFERENCE (a terminal pass whose verdict is the thing asked for; it queues no work)

Jordan asked for each proposal to be stress-tested, and to **log all failures, nulls, etc.** Three testers each built an
executable model of one proposal on the real engine pieces and the real `build_realm` data, applied that proposal's
first batch to a scratch worktree, and kept every failure, null, blocked, skipped and unverified item as a flushed
JSONL line (PR #530's convention). The per-proposal reports hold a claims ledger, the eight dimensions, a
fidelity statement and a **complete roll-call** of every logged non-success: `2026-10-30-stress-test-proposal-1.md`
(about 148 roll-call lines), `-2.md` (76) and `-3.md` (56); logs `2026-10-30-stress-log-p{1,2,3}-*.jsonl` (about 4,250
lines in all) and the harnesses `stress_p{1,2,3}*.py`. Nothing here ran a full season of any proposal, because none is
built: the evidence is of two kinds, **real** (engine functions, real data, repository test files) and **model** (the
tester's reading of what the proposal would build), and each report labels which result is which.

## 1. Verdict

**No proposal survives its stress test intact. Each one's arithmetic held and each broke on existing code.** The dead
core every assessor named was confirmed by running it, and three failures turned out to be common to all three.

## 2. Failures common to all three (found independently by each tester)

| finding | evidence |
|---|---|
| **The first batch is not green.** Deleting the kernel directory (16 tracked files, not the 18 each proposal says) breaks 6 to 7 test files, including `test_sigma_leverage_parity` (a collection error that loses all 901 parity tests), `test_import_cycle_game_state_npe`, `test_engine_does_not_import_systems`, `test_band_extension_seam`, `test_structure_audit` and `test_degree_ladder_single_owner`; `export_sim_params --check` goes red. P3's first batch reddens 12 of 24 files; P1's items 3 and 4 applied literally redden 14 of 29 and `build_realm(0)` raises `SystemExit` once `VERB_CAPABILITY` is emptied | P1 `...-batch1.jsonl`; P2 `...-batches.jsonl`; P3 `...-worktree.jsonl` |
| **Legitimacy (R-36) has no live content.** P1's commit-share L is 0 in 14 of 17 church territories and 11 of 17 crown ones, and is circular (in T9, the only church bench, 6 of 9 residents are committed and all are church officers, two of them on the bench). P3's `opinion_of` L reads exactly 0.50 for all four factions in 8 of 16 territories, no polity faction ever falls below 0.50, and an empty territory (T15) is undefined (`opinion_full = 0` raises). Seeds 0, 1 and 2 give the **same** realm: n = 1 world, not 3. No Church goal engages `solmund_orthodoxy` (`goals.yaml`), so a resident's orthodoxy cannot raise piety | P1 `-one-draw.jsonl`; P3 `-authority.jsonl` |
| **A second case on a docketed matter is refused**, so R-11's many matters about one party, a forum detour and a second authority's case all fail: 50 matters on one party leave 1 docketed and 49 refused (P1); 3 of 3 row pairs (P2); the same for P3's forum contest | `effects_information.py` (the refusal now sits near :368 on current main) |
| **No appeal path exists.** `void` is not in `DISPOSABLE_KINDS`, so `open_case` refuses a docket item under a void row (P1); a second seat's `pardon` on a lower bench's `ban` is refused (P1); a crown `pardon` on a church ban is refused (P3) | `effects_governance.py:335-349` |
| **The King or Queen sits on 319 of 319 non-empty benches** (Wilson [0.988, 1.0]); no bench is church-only; church seats reach the T9 subtree only | P2 `-world.jsonl` |
| **Computed play never determines.** 13 cases opened and `determine` executed 0 times across 3 seeds × 2 seasons (20 refused) (P2); `determine` attempted 65 times and executed 3 times, all `matter.undetermined`; `arrest` attempted 4 times, all refused (P3). Two proposals' "0 attempts" claims were therefore wrong by small counts | P2, P3 season logs |
| **Capability is authored for nobody**: 0 of 83 persons; P1's example row gives only three distinct pools (4, 5, 6.5) | P1 `-one-draw.jsonl` |
| **Citations drift.** 7 of 18 spot-checked citations in P2 missed their line, five of them in `effects_information.py` by about 25 lines; main moved between the commit the proposals cite and the one the testers used | P2 report |

**Held in all three:** the closed-form arithmetic (P1: all 17 quoted probabilities to three places, the 61% and 65%
failure against an equal, and `E[margin] = 0.4N + 0.8√N·softcap(s) − Ob` across 75 sampled cells, max |z| 3.21);
same-seed determinism (P3: stream hash and content hash identical over 2 seasons); the authority grouping (19 polity,
7 church, 5 party-only recomputed exactly from `offices.yaml`); church commit share (7 commits, 6 at T9).

## 3. Proposal by proposal

**Proposal 1.** *Broke:* the legitimacy index (above); the regard link, where every band of `speak` emits a kind with
the identical alignment vector, so a win and a loss move regard identically (0 of 197 decided triples flip, [0, .019],
and the belief term P1 intends is not in the tree, logged `unverified`); the channel rule, which holds at field level
but not at source level (2 of 7 church commit edges move two or more channels, 6 of 7 move L, so P1's "set one weight
to 0" falsifier still passes while a double read persists); the closed form below 1D (the engine floors at 1D; the
formula gives −.31 to −.55 where the draw gives +.096; NaN, negative and N = 0 pools floor silently). *New, from the
ceiling it uses:* with a ceiling of 3 the chance of meeting an equal is non-monotone in pool (.45 at 1D, .38 at 6D,
.74 at 12D, .98 at 30D; without a ceiling it keeps falling to .25), the aptness price vanishes at 12D, and the S27.4
refusal now applies to actors with N below 1.5. *Held:* sigma carries .67 of margin variance at 5D and .83 at 12D,
which is exactly the condition under which the armature said reception should move into the dice.

**Proposal 2.** *Broke:* the case-file carrier (MATTER does not mature a stage whose holder is away even after the
holder returns; burning the file stalls nothing because `determine` reads only the docket; `forge` cannot forge a
case file; anyone with `create_record` can overwrite its whole agenda by naming its id; `seize` does work); the
forum detour; the parliament row, which `open_case` cannot open; and "six stages cost six closing acts" (at most 5
draws, 3 to 5 on any plea path). *Pace:* a deny plea reaches disposal 4.3%, 10.1% and 66.0% of the time at 2D, 5D and
12D, against 26%, 38% and 79.6% for one draw (38%, 49%, 87% if Partial re-dockets). *Plea:* denial is weakly dominant
in 21 of 27 configurations and strictly in 20; conceding the fact alone is best in 0 of 81 even at a season cost of
0.15; a reward on concession (the control) moves the best option away from denial in 47 of 81 cells, though the
live ceiling clips an obstacle-routed reward to nothing in 6 of 9. *R-24:* collapsing unwatched contests to the
terminal stage shifts the outcome distribution by total variation above 0.05 in 52 of 54 configurations.

**Proposal 3.** *Broke:* case-opening (a church seat re-anchored on `scope_rung` alone opens 0 of 19 cases in T1 and 0
of 4 in T4; moving `rung` too opens them but removes the arm limit the warrant branch exists to enforce); the bench
and the gate (a bench-only authority filter lets the King still determine a church-row matter; a gate that reads the
docketed row finds none at write time because the same write clears the docket; quorum counts 5 members where 3 can
act); the summons (the case file is a text Record, so `evade`/`defy` on it returns `compliance.impossible`: 160
attempts in 24 real seasons, 0 executed); a church `issue` of a warrant to the King (`issue.unauthorized`, because
only 1 of 16 polity dispatch holders lies in the Confessor's purview). *Dominance:* `defy` is strictly cheaper than
appearing in 36 of 36 cells and stays so with a chooser that serves warrants; in the forum contest impasse is the
only pure equilibrium; the polity row beats the church row in 15 of 15 sampled cells (forum shopping). *Royal
party:* a Crown seat-holder is the subject of 4 of 23 opened cases (17%, [0.07, 0.37]); royal persons are 4.8% of the
population, so R-34's trigger fires rarely.

## 4. What it changes

- **The recommendation stands in direction and narrows in content.** The stress tests do not reverse the NERS and
  season-loop ranking (Proposal 1 as the base), but they remove the grounds for three of its distinctive parts:
  commit-share legitimacy (broken), the regard link (untestable on the tree), and the `void` appeal (no path). They
  also break the two pieces borrowed from Proposal 3: the warrant branch and the appellate closure basis cannot run
  until case-opening purview and the summons are repaired.
- **Legitimacy (R-36) cannot be built on current content in any of the three forms.** It needs content authored first
  (a Church goal that engages orthodoxy; L over deeds and stances, not commit share) and a defined value for empty
  and zero-denominator cases. This is a content gap before it is a design choice.
- **The deletion batch needs re-scoping before anyone builds it:** 16 files; regenerate `sim_params.json` and
  `value_pointer_links.json` (hand edits failed); repoint the parity test (895 of 901 tests remain); and **do not
  delete the kernel row in `references/module_contracts.yaml` (:448-470)**: P3's tester found it is not merely
  stale; deleting it fails 54 of 65 `test_u7_remit` tests and 9 of 13 `test_sc01_speak` tests, because the contest
  dispatch maps `a matter` to `social_contest` through it. **[CORRECTION: the code audit (finding B-12) called that
  row stale.]**
- **The dead core stays first.** Computed `open_case` naming its row, `determine` firing, a speech reaching a
  judgment, petitions addressed to others, and a decline the world can see are prerequisites for all three, and the
  stress tests show each failing in the shipped realm.
- **Two decisions get sharper.** G1 (the ceiling): the non-monotone equals curve above is the cost of a ceiling of 3
  that the proposals did not state. And a new one: **should legitimacy be authored content first?**

## 5. Nulls and limits, in one place (the roll-calls are complete)

Skipped or untestable, each logged with its reason: a larger realm (`build_realm` maxes at 83 persons); the eight
kinds end to end (no kind reaches a computed proceeding with a row); seizing a case file in Proposal 3's design; a
party with no capability (none authored: a null); throughput in Proposal 3 (no measured per-stage probability; with
q = 0 route B is disposed in 0 of 6,000 chains); `value_pointer_links.json` and the full CI-check suite (not run);
`test_season_shape.py` in Proposal 2 (a 15,000-line suite that ran over 7 minutes). Run times exceeded the 25-minute
budget in two cases because two test files alone take 773 s and 349 s. The testers' own faults are kept in the logs as
`fail` and `error` lines (a harness `KeyError`; a deleted first log, reconstructed from console output; a `sed`
one-liner that corrupted a harness; a first pass that blamed the wrong step for the contract-row failures). No critic
or `fable` pass was run on the stress tests (one round only). `[CONFIDENCE: medium]` on the cross-proposal
reading: the three testers used different fixtures and models, so a figure in one report is not comparable to a
figure in another without checking the model it came from.
