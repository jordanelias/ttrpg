# Stress test of proposal 1, "One draw, one roster"

## Status: REFERENCE (2026-10-31). A terminal pass whose verdict is the thing asked for (`CLAUDE.md` §0, the terminal-pass exception). It changes no tracked file and allocates no `ED`/`PP`. Every number is read from a log in this folder; line references are `file:line` of the JSONL.

**Verdict.** The arithmetic of proposal 1 is right and its two structural bets are not. All 17 probabilities it quotes reproduce to three places, the armature's closed form `E[margin] = 0.4N + 0.8√N·softcap(s) − Ob` matches 75 sampled cells for N ≥ 1, and the determinism test holds. But (1) its legitimacy index `L` is near zero or circular on the only real data there is: the Church's L is 0 in 14 of 17 territories, 0.084 pooled (7 of 83), every church commit belongs to an office-holder, and where a church bench can sit (T9) the committed are the church's own officers, two of them on the bench. (2) Moving reception into the judge's choice via `person_q.regard` cannot reward the speaker: every band of `speak` emits a kind with an identical alignment vector, so a win and a loss move regard identically (0 of 197 decided judges flip either way; 98.4% of judge/speaker pairs have no regard at all). (3) The `void` appeal needs three changes P1 does not list and cannot close another bench's edge. (4) R-11's "many matters" is refused 49 of 50 times by the live docket. (5) The channel rule is a type that forbids a field in two records; it does not stop one `commit` edge moving the dice twice and σ once. (6) Batch B1 is not "the same season, smaller": applied literally it leaves a world that cannot be built (`corpus_run.py:356`) and fails 14 of the 29 files that finished (38 tests, 2 files at collection); the variant that keeps the `VERB_CAPABILITY` map still moves the season's hash and fails 6 tests of `test_season_shape` and one of `test_engine_does_not_import_systems`. The model confirms that a ceiling of 3 makes an act against an equal succeed 98% of the time at 30D (it falls to 38% at 6D), and that σ carries 67% (5D) to 83% (12D) of the margin variance, which is the condition P1 §7 names for moving fit into the dice.

## Claims ledger

"Model" = my build of what P1 says it will build; "real" = the engine function or file named. n and Wilson 95% where a rate; log line numbers are in `…-stress-log-p1-one-draw.jsonl` (A), `…-batch1.jsonl` (B), `…-void.jsonl` (V).

| # | claim (quoted) | where in P1 | test | result | n, interval | log |
|---|---|---|---|---|---|---|
| 1 | L is a share of residents holding a live commit; "if laity commits are sparse, L is near 0 everywhere … B4 must measure first" | §3.7 | `build_realm` seeds 0-2, Crown and Church, per territory | **BROKE** as a usable index (P1's flagged risk is real) | Church 7/83 = .084 [.041, .164]; 14 of 17 territories L = 0; Crown 11/83 = .133 [.076, .222], 11 of 17 L = 0; seeds identical | A: legitimacy lines |
| 2 | 17 quoted probabilities (.390, .201, .687 … .580) | §3.3, §4.1, §4.2, §9a | real `p_success`, tolerance .0006 | **HELD** 17/17 | exact | A: quoted_numbers |
| 3 | "an act against an equal fails 61% at 5D (65% at 10D)" | §8 Q5 | `p_success` | **HELD** .6101, .6537 | exact | A: equals |
| 4 | closed form `E[m] = 0.4N + 0.8√N·softcap(s) − Ob` | §3.3 via AR D.1 | model draws (real `roll_net_continuous`, `net_boost`) against form and `p_success`, 75 cells | **HELD** N ≥ 1; **BROKE** N < 1 | max \|z\| 3.21; p_success outside Wilson in 7 of 225 intervals (11 expected) | A: closed_form |
| 5 | fractional pool, sub-1D | AR D.1 | N = 0, .25, .5 | **BROKE**: engine floors mean and spread at 1D; formula gives −.31 to −.55 where the draw gives +.096 | n = 40,000 each | A: closed_form.sub1D |
| 6 | "entering two channels is impossible by construction"; "no two [producers] read the same edge family" | §3.2 | disjoint fields (HELD); real `commit` edges flipped one at a time under P1's producers | field-level **HELD**; source-level **BROKE** | 2 of 7 church commits move ≥ 2 channels, 6 of 7 move L; control (guilds) 0 of 4 | A: channels |
| 7 | the falsifier "set one field's row weight to 0 and assert only that producer's reads stop" | §3.2 | zero `factions`, flip a commit | **BROKE** (insensitive): L still moves | 1 case | A: channels.zero_weight_falsifier |
| 8 | regard "acts in the decider's own choice"; best speaker rewarded | §3.3, §7 | real `align_kind`; real `regard` over 12,000 (judge, A, B) triples | **BROKE** | decided flips 0/197 [0, .019] for success and for failure; ties 11,803/12,000 | A: regard |
| 9 | appeal row `disposes: void` closes the lower edge | §3.6, §5 | real loader, `open_case`, `determine`, `pardon` in a scratch worktree | **BROKE** (3 breaks) | 1 each | V |
| 10 | R-11 met "as one matter per draw, many docket items per sitting" | §7 | real `open_case` × 1, 2, 5, 50 on one party | **BROKE** | 1 of 50 docketed | A: failure.many_matters_one_party |
| 11 | ceiling 3 "binds only where an opponent exceeds 6D" | §8 Q2 | `p_success` vs equal, 1D-30D, with and without; real S27.4 line | number **HELD**; consequences **BROKE** (S2, S3) | exact | A: equals_curve, extremes |
| 12 | "if sweeps show σ's share … exceeds dice at 12D, fit belongs in dice" | §7 | variance by channel, three range scales | **TRIGGERED** (model ranges) | σ share .67 (5D), .83 (12D) at base ranges | A: sigma_share |
| 13 | "capability is unauthored for all 83 persons" | §7 | `Person.capability` count | **HELD** | 0/83 | A: bench |
| 14 | church bench only at T9; King/Queen sit on church venues | §4.1, AR F | `judging_set` per venue + authority map | **HELD** | 1 church venue of 21; polity seats also on it | A: bench |
| 15 | B1 "suite green; same season, smaller" | §6 | 31 test files, scratch worktree, 6 cumulative states | **BROKE** | S8 | B |
| 16 | B1 "sys.modules after a season holds no systems.social_contest" | §6 | one real season, control and B1 | **NULL**: already true at HEAD | 1 | B: control/lite |
| 17 | B1 "same-seed content_hash equal twice" | §6 | two builds each, control and B1-lite | **HELD** (and the two states differ) | 2 + 2 | B |
| 18 | "pools vary by person across `build_realm(0)`" (B2 test) | §6 | model row, 83 persons | **BROKE** under P1's own default: 3 distinct pools, evidence 0/3000 pairs | 83; 0/3000 [0, .0013] | A: bench |
| 19 | determinism of a real season | S7 | seed 0 × 2, 2 seasons | **HELD** | hash equal; seed 1 differs | A: real |
| 20 | emergent loops 9b (failing faith, parliament, border bargain) | §9b | needs the choice layer and a moving L | **UNTESTABLE** | — | A: kinds, regard |

## S1 Extremes

- **Pool.** The draw floors any pool at 1D silently: N = −3, NaN, 0 and −6 (a negative standing weight) all give the same draw (mean margin −1.588, 2.55% meets). Infinite N yields `inf` rolls and `p_success` NaN. P1 §3.2 types the pool as a float and states no domain; PR #530 found the same of NaN opposition (A: closed_form.nonfinite, extremes.weights).
- **Weights.** Zero weights give the 4D default; 1e9 gives certainty (p = 1.0); NaN and negative totals floor; none is refused (A: extremes.weights).
- **Obstacle.** Real `obstacle()` refuses a ceiling below `OB_MIN` (0, 0.99), accepts 1.0. P1's ceiling 3 and the live S27.4 line (`ob > 2 × pool`, `sigma.py:273`) interact: with ceiling 3 an actor with N < 1 is refused outright against any opponent above 4D (Ob > 2) and one with 1 ≤ N < 1.5 against an opponent of 6D or more (Ob 3): of 9 opponent values, 8 refused at N = 0, 6 at .5, 5 at 1 and 1.25, none from 1.5 up. Without a ceiling the refusals continue at every pool (1 of 9 at 30D). R-16 says priced, never refused. The `fail` line's own wording ("4D or more") is looser than the grid; the correction is a `result` line after it (A: extremes.S27_4, obstacle_grid, S27_4.correction).
- **L.** At L = 0 the seat term vanishes on both sides and everyone is 4D (p = .4013 against an equal); at L = 1, a 7D seat-holder meets .6473 against a 4D party and .4624 against another seat-holder (A: extremes.L).
- **σ.** `net_boost` saturates at ±2.68 net (5D) from 1e9; NaN propagates to NaN p. Against Ob 6 at 5D, σ at its limit gives .231, at s = 1.5 only .137 (A: extremes.sigma).
- **Benches.** Real benches top out at 4 (one venue, T16, has none). Modelled iid judges at p = .4386: strict majority is .4386 (1), .1924 (2, with an exact tie of .4925), .3677 (7), .2838 (21). P1 does not say how members' degrees count against `quorum` (A: extremes.bench).
- **Matters per party.** 1, 2, 5, 50 attempted: 1 docketed each time, 49 refused (A: failure.many_matters_one_party).
- **Unknown row / missing authority / no holder.** A real `open_case` naming an unknown arrangement declines (`case.refused`). The real loader rejects `authority:` today as an unknown key; what a row without it means is unstated. A vacated seat leaves an empty bench and `determine.refused` (A: extremes.*, failure.judge).

## S2 Distributions

Model draws, real engine, n = 60,000 per cell (±.004 at p ≈ .5). Rows are P1 §4's kinds with its weights; the 2D/5D/12D columns scale the actor; opposition scales with it and the ceiling 3 binds from 7D up. "meets / succeeds".

| kind | 2D | 5D | 12D |
|---|---|---|---|
| K1 dyadic influence | .206 / .045 | .596 / .377 | .894 / .813 |
| K2 negotiation | .534 / .211 | .468 / .263 | .871 / .780 |
| K3 royal tribunal (Duke's defence) | .324 / .102 | .288 / .132 | .740 / .612 |
| K3 heresy (inquisitor, L = .2) | .430 / .143 | .387 / .200 | .739 / .612 |
| K4 petition (written) | .145 / .028 | .503 / .290 | .843 / .742 |
| K5 panel member `determine` | .432 / .146 | .389 / .198 | .742 / .613 |
| K6 parliament speech | .281 / .073 | .685 / .469 | .932 / .870 |
| K7 display | .147 / .027 | .499 / .287 | .843 / .741 |

K1, K2, K6 and K7 end in a person's choice, which P1 builds in B5; no outcome distribution beyond the draw band is computable (`unverified`, four lines).

**The ceiling inverts the status quo.** Against an equal, P(meets) falls 0.450 (1D) → 0.380 (6D), then with ceiling 3 climbs: .462 (7D), .654 (10D), .742 (12D), .919 (20D), .980 (30D). Without a ceiling it keeps falling to .247 at 30D. "The world resists change" is true only for pools under 7D (A: equals_curve).

**Sensitivity (one at a time, 5D vs equal, base .390).** +0.5σ of fit or circumstance: +.190; +1.5σ fit: +.416; L .2 → .9: +.145; +1D from any of the five dice sources: +.090 (they are perfectly substitutable); opponent +1D: −.102; aptness +1 Ob: −.102; ceiling removal: 0 at this point. Half a σ is worth 1.49 dice at 2D, 2.12 at 5D, 3.21 at 12D (A: kinds.sensitivity, sigma_vs_dice).

**σ dominance (AR H.2).** Over a ±3D dice swing, ±1.5 Ob of opposition and σ inputs summing to ±2: σ share .67 at 5D, .83 at 12D; at half and at double the σ range, .74/.88 and .50/.69. The dice carry equal variance only if σ is confined to ±0.70 (5D) or ±0.44 (12D) σ-units (A: sigma_share). Ranges are mine; the direction holds at all three scales.

## S3 Dominance and corridors

- **Speech kind.** The apt kind strictly dominates the inapt at 2D and 5D for every swept price (.5, 1, 2). At 5D the price is capped by the ceiling, so +.5, +1 and +2 all cost .1019. At 12D versus an equal, opponent/2 = 6 ≥ ceiling 3: the inapt kind costs nothing (p = .742 both). "Pick the apt kind" is a lookup at small pools and irrelevant at large ones (A: dominance.speech_kind, ceiling_hides_aptness).
- **Silence vs speaking.** If a failed `speak` deposits nothing, speaking weakly dominates silence at every pool (EV +.145, +.160, +.505 at 2D, 5D, 12D). If a failure deposits −0.25, EV is +.0022, +.0078, +.441: nearly neutral at small pools. P1 does not state which (A: dominance.silence_vs_speak; `unverified`).
- **Acting against an equal** fails 57%, 61%, 67% at 2D, 5D, 12D without a ceiling; with P1's ceiling 3 the 12D figure is 26% (A: dominance.status_quo, equals_curve).
- `defy` / forum silence: **skipped**, P1 has neither.

## S4 Throughput and pace

A bench disposal needs a Success-or-better `determine` in P1's reading (Partial re-dockets). Expected sittings, one per season: pious church (judge 6.7D v party 4D) 2.28 (P within 4 sittings .90); weak church 4.01 (.68); default 4D v 4D 5.24 (.57); 2D judge 38.6 (.10); 12D judge 1.35. If Partial also disposes, as the shipped `determine` does, 1.59 / 2.16 / 2.49 / 6.92 / 1.19. A forensic proceeding needs 3 acts minimum, inside the budget of 5; seasons, not acts, are the cost (A: pace). Real play, seed 0, two seasons: 33 `speech.unheard`, 6 `case.opened`, 8 `determine.refused`, 0 `matter.determined`, one `speak` Success and one Failure executed (A: real.season). Stalls: vacated bench → `determine.refused`; judge removed → `act.ineligible`.

## S5 Real data

- **Legitimacy (claim 1).** Seeds 0, 1 and 2 give identical rosters, commits and L, so n = 1 independent realm. Church: L > 0 in 2 of 17 territories (T1 1/19 = .053; T9 6/9 = .667). Crown: 5 of 17 (T1 .316, T14 .333, T2 .077, T8 .25, T9 .111). Of 11 Crown commits 10 belong to office-holders, 1 to laity; of 7 church commits all 7 do. In T9, 6 of 9 residents are committed, all six hold church-faction offices, 2 sit on the bench. L is granular (steps of 1/n, n = 1 to 19) and is made of the people it weights. Example B's L = .7 for the crown is .11 in T9 and 0 in 11 of 17 territories (A: legitimacy.*).
- **Benches.** 21 candidate venues: one empty (T16), one with a church `determine` seat (T9, where polity seats also sit), 20 with polity seats; 0 of 83 persons have capability (A: bench).
- **Dice distribution.** Under P1's example row, 83 persons yield three distinct pools {4, 5, 6.5}. Evidence (P1's own-ledger deed claims about the opponent): 0 of 3000 sampled pairs at tick 0 [0, .0013] (A: bench.dice_distribution, evidence_density).

## S6 Failure injection

Real code through `test_u7_remit`'s helpers: removing the seat, removing the judge, vacating every seat each turn a determining case into a refusal or `act.ineligible`, no crash; control `matter.determined` (A: failure.judge, failure.control). A second `open_case` on a docketed matter is refused whatever the authority, so P1's appeal "to a row of another authority" has no docket path (A: failure.two_authorities_one_matter). Seizing a case file: skipped, P1 has none.

## S7 Determinism and scale

Seed 0 built and run twice for two seasons: content hash `9e71dfe9…` both times, event counts equal; seed 1 differs (control). Season wall time 16.6-18.9 s (first), 37-38 s (second), build 0.5 s, on a machine running other jobs. No larger realm exists (`build_realm` builds the authored roster); skipped (A: real).

## S8 Scratch-copy batches

Scratch worktree at `404e8023`; P1's B1 items applied in states; the affected test set is 31 files; `-x` per file; control = P0 (all pass; `test_season_shape` takes 773 s and `test_engine_does_not_import_systems` 349 s alone, so my first 150-420 s limits timed them out: indeterminate, not broken).

| state | applied | files failing |
|---|---|---|
| P0 | none | 0 (control) |
| P1a | `git rm` the kernel (16 files; P1 says 18) | 7: kernel test, **`test_sigma_leverage_parity` (collection error; unlisted by P1)**, import-cycle, band-extension seam, structure audit, degree-ladder owner, export-sim-params |
| P1b2/b3 | module_contracts row → none; both JSON files regenerated (not hand-edited: first attempt failed 2 tests, kept); kernel test deleted; parity repointed (drops 2 defs, 895 of 901 tests remain) | 3: import-cycle, band-extension seam, degree-ladder owner |
| P1c | items 2 and 5 (reception/proofs, 4 record fields, room term; `bench_basis`, `records_dissent`, `written_only`) | 6 (+ `test_arrangements`, `test_sc02_reception`, `test_stress_proceedings_rehost`); `sim_params.json` 287 → 256 constants |
| P1d | items 3 and 4 literally | **14 files, 38 failing tests, 2 files fail at collection**; `build_realm(0)` itself raises `SystemExit` |
| P1d minus the `VERB_CAPABILITY` deletion ("lite") | all of B1 except that map | season runs; one-season hash differs from control; `test_season_shape` 6 failed / 216 passed (control 222 passed, 773 s); `test_engine_does_not_import_systems` 1 failed / 15 passed (control 16 passed, 349 s) |

Counts at P1d without `-x`: arrangements 5, social_contest_module 1, obstacle_ceiling 6, speak 2, reception 13, 22b 1, rehost 1, in12_step9 4, import_cycle 1, band_extension 1, balance_oracle_arms 2, degree_ladder 1, plus `the_bar` and `u8_cast_fields` uncounted (collection). `test_season_shape::test_h115…` (the pinned count of load-time exits) fails at 82 vs 83 as soon as item 5 removes the `records_dissent` `raise SystemExit`. `the_bar` and `u8_cast_fields` die at collection with the `VERB_CAPABILITY` `SystemExit`. Compared with the assessors: they said the parity test breaks and four row keys appear 44 times across three files; both hold. P1's "nine dependants" is the right order of magnitude (10 files edited, deleted or regenerated, counting `test_engine_does_not_import_systems`, whose probe resolves a kernel symbol, and the module_contracts row); `test_season_shape` (6 tests) is on neither P1's list nor the assessors'; "suite green" is not reachable inside B1.

**(d) The `void` appeal, tried in a second scratch worktree.** After the one edit P1 lists (add `void` to `_DISPOSES_LITERALS`, one appeal row) the loader accepts it (9 rows). Then: `open_case` under the void row is refused (`case.refused`) because `void` is not in `DISPOSABLE_KINDS` (`effects_information.py:362-363`; control `tribunal` opens); `determine` on a hand-planted void item gives `determine.refused` and opens nothing; and a second seat's `pardon` on the lower bench's `ban` is refused while the lower seat's own `pardon` closes it (`ban.ended`), the closure-basis gap at `effects_governance.py:335-349` (V).

## Fidelity statement

**Real:** `engine/dice_engine` (`p_success`, `net_boost`, `roll_net_continuous`, `soft_cap`, `degree_from_net`), `modules/social_contest/roll.py::obstacle`, `build_realm(0..2)` worlds and their commits, offices, residences, ledgers; `world_q` (`members`, `judging_set`, `residence_of`, `enclosing_territory`, `docketed`), `person_q.regard`, `data.verbs.align_kind`; the real `open_case`, `determine` and `pardon` acts in `engine/season/tests/test_u7_remit.py`'s world; the arrangements loader; 31 test files in a scratch worktree; two full seasons.
**Model (evidence about the design, not the code):** the `Dice`/`Obstacle`/`Leverage` records and their composition; the producers (faction, standing, fit) and `legitimacy_share` over commit edges; the authority map (Crown = polity, Church of Solmund and Holy See/Cardinal bodies = church); the row weights (P1's own placeholders); the judge's disposition rule (sign of regard difference); iid benches; the ranges in the σ-share test; every B1 edit beyond `git rm` (written by the harness from P1 §5, logged verbatim). Seeds 0-2 are one realm. Not tested: the disposition operand, `commit_count`, `mutual`, computed `open_case`, the `speak` deposit; none exists.

## What would overturn each finding

1. L: a laity-heavy roster (commits for residents who hold no office) or a different L (P1's named revert, mean `person_q.legitimacy`, was not measured: `unverified`). 2. Regard: a deed kind with band-dependent alignment (an authored `deed:` cell per band), or the belief term P1 intends; with it a flip rate is a parameter. 3. Channels: producers that read disjoint edges. 4. `void`: the three listed edits plus a second-seat closure basis. 5. R-11: a docket keyed on (party, matter). 6. B1: moving items 3 and 4 into B2 with the producers, and regenerating rather than editing. 7. σ share: tighter σ ranges (≤ ±0.44 at 12D). 8. Ceiling findings: a different ceiling or deletion (Jordan's G1).

## FAILURES AND NULLS (complete roll-call)

Generated by `python proposals/2026-10-29-parliament-and-debate/stress_p1.py --rollcall <the four logs>`.

- `2026-10-30-stress-log-p1-one-draw.jsonl:31` **null** [legitimacy] no resident-level commit is toward a *territory-local* piety: the instrument counts `commit` edges to fac_* Propositions only; `person_q.legitimacy` (the stance/deed estimate that is P1's own named revert) was NOT measured here
- `2026-10-30-stress-log-p1-one-draw.jsonl:32` **unverified** [legitimacy] P1's revert arm (mean of person_q.legitimacy over residents) was not measured: it needs a holder id per authority and reads other ledgers (F8); only the commit-share L that P1 chose is measured
- `2026-10-30-stress-log-p1-one-draw.jsonl:47` **fail** [closed_form] sampled margin disagrees with the closed form or with p_success
- `2026-10-30-stress-log-p1-one-draw.jsonl:75` **fail** [closed_form] sampled margin disagrees with the closed form or with p_success
- `2026-10-30-stress-log-p1-one-draw.jsonl:87` **fail** [closed_form] sampled margin disagrees with the closed form or with p_success
- `2026-10-30-stress-log-p1-one-draw.jsonl:90` **fail** [closed_form] sampled margin disagrees with the closed form or with p_success
- `2026-10-30-stress-log-p1-one-draw.jsonl:104` **fail** [closed_form] sampled margin disagrees with the closed form or with p_success
- `2026-10-30-stress-log-p1-one-draw.jsonl:118` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.0 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:120` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.25 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:122` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.5 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:126` **fail** [closed_form.nonfinite] pool -3.0 accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:128` **fail** [closed_form.nonfinite] pool nan accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:130` **fail** [closed_form.nonfinite] pool inf accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:166` **fail** [channels] P1 §3.2 says the producers are chosen so no two read the same edge family; in the model built from P1's own table, 2/7 single `commit` edges move >=2 channels (faction dice, L inside standing dice, sigma fit all read `commit`)
- `2026-10-30-stress-log-p1-one-draw.jsonl:172` **fail** [regard.alignment] every band of `speak` emits a kind with the SAME alignment vector (grandiose_humble -0.4 only), so a person's regard for a speaker cannot depend on whether the speech succeeded; a Success and a Failure move regard identically
- `2026-10-30-stress-log-p1-one-draw.jsonl:177` **fail** [regard.judge] a judge whose disposition is sign(regard(A)-regard(B)) responds identically to a successful and a failed speech by A: 0 of 12000 triples differ
- `2026-10-30-stress-log-p1-one-draw.jsonl:179` **unverified** [regard.belief_term] P1's 'disposition operand' (the judge chooses from the deposits at their confidence) is not in the tree (decision/ has no disposition operand: PROBE 2.3, AR I.12). A flip rate for it would be my parameter (beta) times the deposit,
- `2026-10-30-stress-log-p1-one-draw.jsonl:209` **fail** [dominance.ceiling_hides_aptness] at 12D versus an equal, opponent/2=6 >= the ceiling 3, so the aptness price is clipped away by the ceiling: every speech kind is equally apt
- `2026-10-30-stress-log-p1-one-draw.jsonl:213` **unverified** [dominance] what a FAILED `speak` deposits (confidence by degree) is not stated by P1; under reading A speech weakly dominates silence at every pool (a corridor: 'always speak'); under B the sign of EV depends on pool. Whichever P1 builds dec
- `2026-10-30-stress-log-p1-one-draw.jsonl:214` **skipped** [dominance.defy_forum] `defy` and silence in a forum contest (assessors: P3)
- `2026-10-30-stress-log-p1-one-draw.jsonl:220` **error** [kinds] Log.w() got multiple values for argument 'kind'
- `2026-10-30-stress-log-p1-one-draw.jsonl:236` **fail** [failure.many_matters_one_party] 2 matters about ONE party: 1 docketed, 1 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:238` **fail** [failure.many_matters_one_party] 5 matters about ONE party: 1 docketed, 4 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:240` **fail** [failure.many_matters_one_party] 50 matters about ONE party: 1 docketed, 49 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:248` **fail** [failure.two_authorities_one_matter] a second open_case on the same matter is refused by the live code regardless of authority; P1's appeal path ('petition plus carry to a row of that authority', a docket item for the SAME matter under ANOTHER authority) needs `docke
- `2026-10-30-stress-log-p1-one-draw.jsonl:249` **skipped** [failure.case_file] seize or burn the case file
- `2026-10-30-stress-log-p1-one-draw.jsonl:250` **skipped** [failure.defy] a judge who never acts
- `2026-10-30-stress-log-p1-one-draw.jsonl:283` **null** [legitimacy] no resident-level commit is toward a *territory-local* piety: the instrument counts `commit` edges to fac_* Propositions only; `person_q.legitimacy` (the stance/deed estimate that is P1's own named revert) was NOT measured here
- `2026-10-30-stress-log-p1-one-draw.jsonl:285` **unverified** [legitimacy] P1's revert arm (mean of person_q.legitimacy over residents) was not measured: it needs a holder id per authority and reads other ledgers (F8); only the commit-share L that P1 chose is measured
- `2026-10-30-stress-log-p1-one-draw.jsonl:367` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.0 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:369` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.25 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:371` **fail** [closed_form.sub1D] the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N=0.5 (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not
- `2026-10-30-stress-log-p1-one-draw.jsonl:375` **fail** [closed_form.nonfinite] pool -3.0 accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:377` **fail** [closed_form.nonfinite] pool nan accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:379` **fail** [closed_form.nonfinite] pool inf accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard
- `2026-10-30-stress-log-p1-one-draw.jsonl:417` **fail** [channels] P1 §3.2 says the producers are chosen so no two read the same edge family; in the model built from P1's own table, 2/7 single `commit` edges move >=2 channels (faction dice, L inside standing dice, sigma fit all read `commit`)
- `2026-10-30-stress-log-p1-one-draw.jsonl:423` **fail** [regard.alignment] every band of `speak` emits a kind with the SAME alignment vector (grandiose_humble -0.4 only), so a person's regard for a speaker cannot depend on whether the speech succeeded; a Success and a Failure move regard identically
- `2026-10-30-stress-log-p1-one-draw.jsonl:428` **fail** [regard.judge] a judge whose disposition is sign(regard(A)-regard(B)) responds identically to a successful and a failed speech by A: 0 of 12000 triples differ
- `2026-10-30-stress-log-p1-one-draw.jsonl:430` **unverified** [regard.belief_term] P1's 'disposition operand' (the judge chooses from the deposits at their confidence) is not in the tree (decision/ has no disposition operand: PROBE 2.3, AR I.12). A flip rate for it would be my parameter (beta) times the deposit,
- `2026-10-30-stress-log-p1-one-draw.jsonl:460` **fail** [dominance.ceiling_hides_aptness] at 12D versus an equal, opponent/2=6 >= the ceiling 3, so the aptness price is clipped away by the ceiling: every speech kind is equally apt
- `2026-10-30-stress-log-p1-one-draw.jsonl:464` **unverified** [dominance] what a FAILED `speak` deposits (confidence by degree) is not stated by P1; under reading A speech weakly dominates silence at every pool (a corridor: 'always speak'); under B the sign of EV depends on pool. Whichever P1 builds dec
- `2026-10-30-stress-log-p1-one-draw.jsonl:465` **skipped** [dominance.defy_forum] `defy` and silence in a forum contest (assessors: P3)
- `2026-10-30-stress-log-p1-one-draw.jsonl:495` **unverified** [kinds] the outcome is a person's own choice reading what the draw moved; P1 B5 builds that choice (disposition/matter term/`commit_count`); no outcome distribution is computable beyond the draw band
- `2026-10-30-stress-log-p1-one-draw.jsonl:496` **unverified** [kinds] the outcome is a person's own choice reading what the draw moved; P1 B5 builds that choice (disposition/matter term/`commit_count`); no outcome distribution is computable beyond the draw band
- `2026-10-30-stress-log-p1-one-draw.jsonl:497` **unverified** [kinds] the outcome is a person's own choice reading what the draw moved; P1 B5 builds that choice (disposition/matter term/`commit_count`); no outcome distribution is computable beyond the draw band
- `2026-10-30-stress-log-p1-one-draw.jsonl:498` **unverified** [kinds] the outcome is a person's own choice reading what the draw moved; P1 B5 builds that choice (disposition/matter term/`commit_count`); no outcome distribution is computable beyond the draw band
- `2026-10-30-stress-log-p1-one-draw.jsonl:522` **fail** [failure.many_matters_one_party] 2 matters about ONE party: 1 docketed, 1 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:524` **fail** [failure.many_matters_one_party] 5 matters about ONE party: 1 docketed, 4 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:526` **fail** [failure.many_matters_one_party] 50 matters about ONE party: 1 docketed, 49 refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)
- `2026-10-30-stress-log-p1-one-draw.jsonl:534` **fail** [failure.two_authorities_one_matter] a second open_case on the same matter is refused by the live code regardless of authority; P1's appeal path ('petition plus carry to a row of that authority', a docket item for the SAME matter under ANOTHER authority) needs `docke
- `2026-10-30-stress-log-p1-one-draw.jsonl:535` **skipped** [failure.case_file] seize or burn the case file
- `2026-10-30-stress-log-p1-one-draw.jsonl:536` **skipped** [failure.defy] a judge who never acts
- `2026-10-30-stress-log-p1-one-draw.jsonl:541` **fail** [extremes.S27_4] with P1's ceiling 3, S27.4 (ob > 2 x pool) REFUSES an act outright for every actor with N below 1.5 (largest refused N=1.25) facing an opponent of 4D or more (Ob >= 2): P1 uses 3 and says it 'binds only where an opponent exceeds 6
- `2026-10-30-stress-log-p1-one-draw.jsonl:548` **fail** [extremes.weights] negative standing -10 (total < 0): the draw accepts a non-finite or negative pool total without refusal (floors/propagates silently)
- `2026-10-30-stress-log-p1-one-draw.jsonl:550` **fail** [extremes.weights] NaN standing: the draw accepts a non-finite or negative pool total without refusal (floors/propagates silently)
- `2026-10-30-stress-log-p1-one-draw.jsonl:552` **fail** [extremes.weights] inf standing: the draw accepts a non-finite or negative pool total without refusal (floors/propagates silently)
- `2026-10-30-stress-log-p1-one-draw.jsonl:570` **unverified** [extremes.missing_authority] a row with no `authority:` / a body or faction spelling missing from the `authorities:` map: P1 §3.7 states neither a default nor a refusal; `legitimacy_share` of an unmapped authority is undefined
- `2026-10-30-stress-log-p1-one-draw.jsonl:578` **skipped** [real.large_realm] a large realm
- `2026-10-30-stress-log-p1-one-draw.jsonl:587` **fail** [equals_curve] with ceiling 3 the odds of an act against an EQUAL are non-monotone in pool: they fall to 0.3797 (N=6D) then climb to 0.98 at 30D, so 'the world resists change' (61% fail at 5D) holds only for small pools and inverts for masters; 
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:7` **fail** [P0] engine/season/tests/test_season_shape.py timeout in phase P0
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:43` **fail** [P1a] engine/tests/test_contest_kernel.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:45` **fail** [P1a] engine/tests/test_sigma_leverage_parity.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:47` **fail** [P1a] engine/season/tests/test_season_shape.py timeout in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:61` **fail** [P1a] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:63` **fail** [P1a] tests/valoria/test_engine_does_not_import_systems.py timeout in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:65` **fail** [P1a] tests/valoria/test_band_extension_seam.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:69` **fail** [P1a] tests/valoria/test_structure_audit.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:71` **fail** [P1a] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:73` **fail** [P1a] tests/valoria/test_export_sim_params.py fail in phase P1a
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:93` **fail** [P1b] engine/tests/test_sigma_leverage_parity.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:95` **fail** [P1b] engine/season/tests/test_season_shape.py timeout in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:109` **fail** [P1b] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:111` **fail** [P1b] tests/valoria/test_engine_does_not_import_systems.py timeout in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:113` **fail** [P1b] tests/valoria/test_band_extension_seam.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:118` **fail** [P1b] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:120` **fail** [P1b] tests/valoria/test_export_sim_params.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:122` **fail** [P1b] tests/valoria/test_link_values_pointers.py fail in phase P1b
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:132` **fail** [P1b] FALSE START, KEPT: phase P1b hand-edited sim_params.json and value_pointer_links.json (deleting entries that name the kernel). Two tests then failed (test_export_sim_params::test_sim_params_current, test_link_values_pointers::test
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:141` **fail** [P1b2] engine/tests/test_sigma_leverage_parity.py fail in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:143` **fail** [P1b2] engine/season/tests/test_season_shape.py timeout in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:157` **fail** [P1b2] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:159` **fail** [P1b2] tests/valoria/test_engine_does_not_import_systems.py timeout in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:161` **fail** [P1b2] tests/valoria/test_band_extension_seam.py fail in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:166` **fail** [P1b2] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1b2
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:186` **fail** [P1b3] engine/season/tests/test_season_shape.py timeout in phase P1b3
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:200` **fail** [P1b3] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1b3
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:202` **fail** [P1b3] tests/valoria/test_engine_does_not_import_systems.py timeout in phase P1b3
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:204` **fail** [P1b3] tests/valoria/test_band_extension_seam.py fail in phase P1b3
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:209` **fail** [P1b3] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1b3
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:223` **error** [P1c] 2026-10-29-parliament-and-debate/stress_p1_b1.py", line 170, in drop
    i = s.index(start_marker); j2 = s.index('\n\n', i) + 2
ValueError: substring not found

- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:236` **skipped** [P1c] engine/season/tests/test_season_shape.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:237` **skipped** [P1c] tests/valoria/test_engine_does_not_import_systems.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:242` **fail** [P1c] engine/season/tests/test_arrangements.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:249` **fail** [P1c] engine/season/tests/test_sc02_reception.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:252` **fail** [P1c] engine/season/tests/test_stress_proceedings_rehost.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:257` **fail** [P1c] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:259` **fail** [P1c] tests/valoria/test_band_extension_seam.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:264` **fail** [P1c] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1c
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:281` **skipped** [P1d] engine/season/tests/test_season_shape.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:282` **skipped** [P1d] tests/valoria/test_engine_does_not_import_systems.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:287` **fail** [P1d] engine/season/tests/test_arrangements.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:289` **fail** [P1d] engine/season/tests/test_social_contest_module.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:291` **fail** [P1d] engine/season/tests/test_sc01_obstacle_ceiling.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:294` **fail** [P1d] engine/season/tests/test_sc01_speak.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:296` **fail** [P1d] engine/season/tests/test_sc01_the_bar.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:298` **fail** [P1d] engine/season/tests/test_sc02_reception.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:300` **fail** [P1d] engine/season/tests/test_sc02_22b_consequence_and_forgery.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:302` **fail** [P1d] engine/season/tests/test_stress_proceedings_rehost.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:304` **fail** [P1d] engine/season/tests/test_in12_step9.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:307` **fail** [P1d] engine/season/tests/test_u8_cast_fields.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:309` **fail** [P1d] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:311` **fail** [P1d] tests/valoria/test_band_extension_seam.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:314` **fail** [P1d] tests/valoria/test_balance_oracle_arms.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:317` **fail** [P1d] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1d
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:331` **error** [end-state] 088.yaml: cast entry 'Carin Vedel': `capability:` keys no verb draws on: ['copying'] (`rosters.yaml: verb_capability` names []) -- nothing would ever read them

- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:338` **skipped** [P1d-noX] engine/season/tests/test_season_shape.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:339` **skipped** [P1d-noX] tests/valoria/test_engine_does_not_import_systems.py: run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:344` **fail** [P1d-noX] engine/season/tests/test_arrangements.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:346` **fail** [P1d-noX] engine/season/tests/test_social_contest_module.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:348` **fail** [P1d-noX] engine/season/tests/test_sc01_obstacle_ceiling.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:351` **fail** [P1d-noX] engine/season/tests/test_sc01_speak.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:353` **fail** [P1d-noX] engine/season/tests/test_sc01_the_bar.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:355` **fail** [P1d-noX] engine/season/tests/test_sc02_reception.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:357` **fail** [P1d-noX] engine/season/tests/test_sc02_22b_consequence_and_forgery.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:359` **fail** [P1d-noX] engine/season/tests/test_stress_proceedings_rehost.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:361` **fail** [P1d-noX] engine/season/tests/test_in12_step9.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:364` **fail** [P1d-noX] engine/season/tests/test_u8_cast_fields.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:366` **fail** [P1d-noX] tests/valoria/test_import_cycle_game_state_npe.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:368` **fail** [P1d-noX] tests/valoria/test_band_extension_seam.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:371` **fail** [P1d-noX] tests/valoria/test_balance_oracle_arms.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:374` **fail** [P1d-noX] tests/valoria/test_degree_ladder_single_owner.py fail in phase P1d-noX
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:386` **fail** [P1d-end-state] B1 as written (items 1-6, including item 4 "the two-row VERB_CAPABILITY map") leaves a world that CANNOT BE BUILT: build_realm(0) raises SystemExit from engine/season/harness/corpus_run.py:356 (cast entry NPC-088 `capability: copy
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:393` **fail** [comparison] P1 section 6 B1 says it "runs after it: the same season, smaller". One season of seed 0 gives content_hash 873525dfb363231695cefb17ad4b17a1 at HEAD and 521e36d9066c80e912cfa6e859128944 with B1 applied minus the VERB_CAPABILITY del
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:394` **null** [comparison] P1 B1 observable "sys.modules after a season holds no systems.social_contest": loaded-module list after one real season of seed 0, at unmodified HEAD (control) and with B1 applied (lite)
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:398` **fail** [lite-long] tests/valoria/test_engine_does_not_import_systems.py::test_a_value_role_still_fails_on_an_attribute_that_does_not_exist fails once the kernel is deleted: it resolves the composition target systems.social_contest.sim.contest:A as i
- `2026-10-30-stress-log-p1-one-draw-batch1.jsonl:399` **fail** [lite-long] engine/season/tests/test_season_shape.py: 6 failed / 216 passed with B1 applied except the VERB_CAPABILITY deletion (control: 222 passed). The file is not on P1 section 5-6 list of touched tests; P1 section 9c lists test_sc01_obst
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:10` **fail** [] `open_case` declines a docket item naming the void row: `ARRANGEMENTS[row]['disposes'] in DISPOSABLE_KINDS` (effects_information.py:362-363) and `void` is not a disposable kind; P1 §5's change list does not touch `DISPOSABLE_KINDS
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:13` **fail** [] `determine` on a hand-planted void item opens nothing and closes nothing (the real `_disposal` has no void site); the lower edge is untouched
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:15` **unverified** [closure_basis] the lower bench did not open a detain at this seed (judge draw); the closure test below is vacuous
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:17` **error** [] FIRST ATTEMPT, KEPT: (1) the child process wrote its lines to a RELATIVE log path resolved inside the worktree (cwd=worktree), so the parent log showed no child lines; the lines above this one were copied here by hand from the wor
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:21` **error** [] SECOND ATTEMPT, KEPT: a sed one-liner I used to patch the harness (`s|a[...]||` meant as a no-op) was an ACTIVE REGEX and deleted the letter pairs "ak","a'" etc. throughout stress_p1_void.py; the run crashed with FileNotFoundError
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:29` **fail** [] `open_case` declines a docket item naming the void row: `ARRANGEMENTS[row]['disposes'] in DISPOSABLE_KINDS` (effects_information.py:362-363) and `void` is not a disposable kind; P1 section 5's change list does not touch `DISPOSABL
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:32` **fail** [] `determine` on a hand-planted void item opens nothing and closes nothing (the real `_disposal` has no void site); the lower edge is untouched
- `2026-10-30-stress-log-p1-one-draw-void.jsonl:35` **fail** [] a second seat (the appeal bench) cannot close the lower bench's restraint: `pardon` closes only edges whose OBJECT is the exercised seat (effects_governance.py:335-338,348); the lower edge's object is the lower seat

## Logs and harnesses

`…-stress-log-p1-one-draw.jsonl` (model, real data, extremes; attempt 1 lines 1-252 kept, attempt 2 from line 253, the equals-curve run from line 581), `…-p1-one-draw-batch1.jsonl` (S8), `…-p1-one-draw-void.jsonl` (d). Harnesses: `stress_p1.py`, `stress_p1_b1.py`, `stress_p1_b1_modules.py`, `stress_p1_void.py`. Stop reasons: every sampled cell stopped at standard error < .004 or its slice; the main run stopped when all sections finished (72 s, then 1.5 min with seasons); B1 states stopped when every file finished or hit its per-file limit.

Worktrees removed (`git worktree remove --force`, then `prune`); `git status` shows only the new files of this report, its three logs and four harnesses.
