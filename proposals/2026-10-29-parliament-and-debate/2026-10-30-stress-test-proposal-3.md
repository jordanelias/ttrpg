# Stress test of Proposal 3, "Authority first"

## Status: REFERENCE (2026-10-30). A terminal pass whose verdict is the thing asked for (`CLAUDE.md` §0, the terminal-pass exception); it queues nothing and changes no tracked file. Every number below is read from a log in this folder.

**Verdict.** The proposal's *counts* are honest and its *mechanism* is not yet buildable as written. What held: the 31-seat authority grouping (19 / 7 / 5) recomputes exactly; 11 of its 14 quoted legitimacy figures reproduce to within rounding and the other three are high by 0.006 to 0.007; the church commit-share fallback (7 commits, 6 in T9, 1 in T1, zero in 14 of 16 populated territories) is exact; the worked-example arithmetic (0.82D is about 6 to 7 points of "meets" at 5D) holds. What broke, by execution on `build_realm(0)` and not by reading: (1) **Q1 as written does not let the church open a case outside T9**: a church seat re-anchored to the realm on `scope_rung` alone opened 0 of 19 cases in T1 and 0 of 4 in T4 (`case.unauthorized`), so worked example A and scenarios 2 and 3 die at step 1; the fix that does open them (`rung` as well) removes the very arm limit the warrant branch exists to enforce; (2) **the bench filter and the gate do not agree**: with only the bench filtered, the King leaves the bench and still determines a church-row matter (executed at quorum 1 and 3), and a gate that reads the row sees no row at write time (the docket is cleared in the same write); (3) **`defy` is a free move**: it strictly dominates appearing in 36 of 36 modelled cells, the summons it is supposed to answer cannot be defied (the case file is a kind-`text` Record held by the opener; `evade / defy` forms only on a held writ), and in 24 real seasons it was attempted 160 times and executed 0; (4) **the forum contest has no code to extend and, modelled, one equilibrium**: impasse; (5) legitimacy L is **identical across seeds 0 to 2** (one world, not three), reads exactly 0.50 for all four factions in half the territories, never falls below 0.50 for any polity faction, is undefined for the empty territory T15, and is computed at territory level while cases are heard at a settlement or hearth (76% of settlements have two residents or fewer). C1 (the deletions) is not green: 12 of 24 reachable test files go red across its five steps, including a load-bearing `module_contracts` row the audit called stale (S8).

---

## 0. Method, stop rules, files

Method is PR #530's: one flushed, fsynced JSON line per event; `manifest`, `plan`, `claim`, `trial`/`batch`, `result`, `fail`, `null`, `blocked`, `skipped`, `unverified`, `error`, `summary`. No chosen horizon or trial count: a run stops on the first of a crash, a quiet result or its wall-clock budget. Every rate carries n and a Wilson 95% interval; every comparison names a control and a falsifier. My own false starts are kept as `fail` or `error` lines (the roll-call entries beginning "my" or "first", and the three TypeErrors at the head of the seasons logs).

| file | what | stopped by |
|---|---|---|
| `stress_p3.py` | the one harness (sections A, A2, B, B2, C, D, E, F, F2, G, G2, H, Q1hash, S1, S1b, S2, S4, S5, S6, S7, S7b, skips, notes) | each section ran to its end; several crashed on a first attempt and were rerun (see roll-call) |
| `2026-10-30-stress-log-p3-authority.jsonl` | everything except the next two | all requested sections ended |
| `2026-10-30-stress-log-p3-authority-seasons-s{0,1,2}.jsonl` | real seasons, shipped chooser, one process per seed | **wall-clock budget (540 s)**, 8 seasons each; no crash, no quiet season |
| `2026-10-30-stress-log-p3-authority-worktree.jsonl` | C1 in a scratch worktree | all five steps ran; no timeout |

Fidelity statement (also §11): REAL = `build_realm(0..2)`, `world_q.opinion_of / residence_of / judging_set / ancestry`, `gate.purview_reaches / sits_over / may_determine`, `SeasonDriver.resolve` with hand-built acts on the real realm (`open_case`, `determine`, `pardon`, `issue`, `give`, `arrest`, `evade / defy`, `destroy_record`), the shipped chooser over real seasons, `sigma_leverage.p_success` and `roll_net`, the repo's test files. MODEL (evidence about the design, not the code) = the authority filter on `judging_set`, the row-reading `may_determine`, the payoff games, the Markov chains, the majority-of-n bench, the `weight × L` operand (P3 builds none of these).

## 1. Claims ledger

| # | claim (quoted or close) | where | test | result | n and interval | log |
|---|---|---|---|---|---|---|
| 1 | "church L is T9 .78, T8 .59, T14 .57, T1 .53, T3 .45, T4 .38, T2 .37; Crown L T9 .77, T14 .75, T1 .74, T3 .70, T2 .68, T5 .67, T4 .57" | §3.3 | A: rebuild L, seed 0 | **HELD** 11 of 14 within ±.005; **BROKE** 3 of 14 (church T9 .774, church T8 .584, Crown T14 .743; claimed .78, .59, .75) | 14 figures; residents per territory 4 to 19 | A fail lines |
| 2 | "territories peopled only by cohorts read .50" | §3.3 | A | **HELD**: 8 of 16 territories, all four factions exactly .50 | 8/16, [0.28, 0.72] | A |
| 3 | "166 `opinion_of` calls took 0.04 s" | §3.3 | A | **HELD** (332 calls in 0.038 s) | 1 build | A |
| 4 | commit share: "7 committed members, 6 in T9 and 1 in T1 ... zero in 14 of 16 territories" | §3.3 | A | **HELD** (14 of 16 populated; 15 of 17 incl. empty T15) | 7 commits | A |
| 5 | (implicit) L varies with the world seed | §3.3, brief | A2 | **NULL**: seeds 0, 1, 2 give identical L tables to 9 dp (content hashes differ, opinions do not) | 3 seeds = 1 sample | A2 |
| 6 | authority grouping 19 / 7 / 5; Crown 11 (Inner Circle 2, Ministries 1), Hafenmark 4, Varfell 4; church 7 | §3.1 | C | **HELD** exactly | 31 seats | C |
| 7 | determine holders: King, Queen, Senior Jarl, Skald-Chief; Confessor, Cardinal Justice, Senior Inquisitor all scoped T9; Hafenmark none; 32nd seat `off_npc_084` unscoped | §3.1 | C | **HELD** | 3 seeds | C |
| 8 | Q1 (scope anchor, rung stays T9): "the church may then judge anywhere"; worked example A step 1 "under Q1 it passes" | §3.4, §4 | B2 | **BROKE**: opens 0/19 T1, 0/4 T4 (scope only). Opens only when `rung` moves too (19/19, 4/4) | 3 seats x 23 targets | B2 |
| 9 | "case-opening reads purview from `Office.rung`" (assessors) | comparison §4 | B2 | **HELD** (assessors right) | as 8 | B2 |
| 10 | `judging_set` filtered by authority and `may_determine` "reads the row's authority" (one test) | §3.4, §5 | D | **BROKE**: bench-only filter leaves the King able to determine (M1); gate-side filter sees no row at write (`row_not_visible`) | 24 cells, n=1 each | D |
| 11 | "the church can judge only at T9 venues"; "the King sits on every church bench" | §3.1, ARM §I | S5 | **HELD**: church bench empty for 74/83 homes; King on the live bench for 82/83 | 83 persons | S5 |
| 12 | custody outside purview "executes directly" today | §3.5 | F | **HELD** (a `detain` on the church seat opened with no arrest, party outside its purview) | n=1 | F |
| 13 | "every church seat holding `dispatch` sits at T9 or T1"; King, Queen, Heir, Princess hold `dispatch` | §3.5, ex. A | F2 | **HELD** (4 church: 3 T9, 1 T1; 4 royal) | 25 holders | F2 |
| 14 | church warrant goes to "a polity seat at realm scope" | ex. A step 5 | F, F2 | **BROKE as built**: `issue` needs the issuer's purview to reach the executor; 1 of 16 polity dispatch holders is inside the Confessor's purview, and the Confessor's `issue` to the King was `issue.unauthorized`; `give` to the King was refused (not co-located). With `rung` realm the chain runs (`arrest.made`, edge on the church seat) | 16 holders | F2 |
| 15 | "`open_case`'s Record is the summons; `evade / defy` gains its reader" | §3.5 | F, G | **BROKE**: the case file is kind `text`, held by the opener; `evade / defy` on it is `compliance.impossible`; 160 real attempts, 0 executed | 160, [0, 0.023] | F, G |
| 16 | "The draw is not changed by defiance" (so what does defy cost?) | §3.5 | E | **BROKE as a design**: defy strictly dominates appear in 36/36 cells; a warrant's cost is x q x p_arrest | 36 cells, [0.90, 1.0] | E |
| 17 | "`arrest` was attempted 0 times" | §7 | G | **BROKE for seed 0** (4 attempts, 4 `arrest.refused`); held for seeds 1, 2 | 0/4, 0, 0 | G |
| 18 | "`determine` rolled 0 times" | §7 | G | **BROKE narrowly**: 65 attempts, 3 executed, all `matter.undetermined` | 3/65, [0.016, 0.127] | G |
| 19 | computed `open_case` names no row | §7 | G | **HELD**: `docket_named_arrangement` 0 at every season, 3 seeds | 24 seasons | G |
| 20 | second `open_case` on a docketed matter is refused; forum contest is a new branch | §3.6 | F2 | **HELD** (control): `case.refused` for the Crown's open after the church's | n=1 | F2 |
| 21 | `pardon` closes only edges on the exercised seat (a crown seat cannot end a church ban) | §3.7 | F | **HELD** (King: `pardon.refused`, ban stays; issuing seat: `ban.ended`) | n=1 | F |
| 22 | the appellate closure basis and forum branch work | §3.6, 3.7 | none | **UNTESTABLE**: unbuilt; only controls ran | | |
| 23 | "re-opening under the same authority ... wedging as it does today" | §3.7 | F2 | **HELD**: re-open executes, `determine.refused`, item stays docketed | n=1 | F2 |
| 24 | worked example A: 0.82D worth "about 7 points" at 5D; ARM .390 to .480 | §4 | E | **HELD**: 5.8 to 6.7 points at Ob 2.0 to 2.5; .3899 and .4797 | closed form | E |
| 25 | Q1 "would move every `build_realm` digest" | §9.3 | Q1hash | **HELD** (hash changes when 3 `scope_rung`s move) | 1 | Q1hash |
| 26 | "a royal person is involved" as a trigger | §3.6, Q3 | G, G2 | **NULL/qualified**: as matter subject in 4 of 23 opened cases (17%, [0.07, 0.37]); 0 of 21 carried petitions; 50 of 133 filed petitions name one (first 60 matter events per seed logged; seeds 0 and 1 truncated) | see S5 | G2 |
| 27 | C1 "green; fewer files" | §6 | H | **BROKE** for a bare deletion: 12 of 24 files red (0 at baseline); extension param clean | 24 files | worktree |
| 27a | assessors: kernel deletion breaks `test_sigma_leverage_parity` at import | comparison §4 | H | **HELD** (collection error, 901 tests); six more files also red | | worktree |
| 27b | audit: `module_contracts.yaml:448-470` is a stale legacy row | CA B-12, P3 §5 | H | **BROKE**: deleting it fails 54/65 + 9/13 fold tests | | worktree |
| 28 | legitimacy is "one calculation, not two ladders" and hostility lowers L | §9.1 S, §3.3 | A | **QUALIFIED**: polity L >= 0.50 in all 16 territories; only the church ever falls below (3 of 16) | 16 | A |

## S1. Extremes

- **L formula.** `clamp01(NaN)` is **1.0**, the most favourable value (`min(1.0, nan)`); `opinion_full = 0` raises `ZeroDivisionError`; `opinion_full < 0` inverts the sign (a friendly territory reads hostile); `1e-9` saturates to 1.0, `1e9` reads 0.5. The proposal states `[ASSUMPTION; revert 1.0]` and no range. Territory T15 has no residents: the mean is 0/0.
- **Pool operand.** 864 cells of `pool x L x weight x Ob` (pool 0, 1, 2, 5, 12, 30, -1, NaN; L 0, .5, 1, NaN, -1, 2; weight 0, 2, 3, 1e6, -2, NaN): 0 non-finite and 0 exceptions. My first reading ("NaN poisons") was wrong and is logged: a NaN pool becomes the 1D floor (`max(1.0, nan)`), a NaN obstacle returns NaN. Effect of the weight-2 term, L 0 to 1, at Ob 2.5: pool 0 +6.2 points, pool 1 +17.0, pool 5 +16.7, pool 12 +5.3, **pool 30 +0.4**.
- **Bench of n** (MODEL, independent identical judges, majority): n = 1 .588, 2 .346 (exact tie .485), 7 .687, 21 .795. Real benches are 0, 2, 4 or 5 persons (S5). A bench of 2 is worse than a bench of 1.
- **Matters per party.** 50 `open_case` acts on one party: 1 opened, 49 refused (1/50, [0.004, 0.105]). R-11 (many matters per party) is not reachable and P3 does not change that.
- **Unknown row**: `case.refused`. **Missing authority**: Guilds, Löwenritter, Restoration read `parties`; authority `parties` has an empty bench for 83 of 83 homes, so a bench-disposal row assigned `parties` (the seeded `arbitration`) can never be determined. **Seat with no holder** (King vacated): the bench at T1 drops to 1, `is_royal` reads three persons.

## S2. Distributions and sensitivity (MODEL on real `p_success`)

One-at-a-time around pool b, Ob 2.5, weight 2, L .55 (points of P(meets); log `tornado`): at 2D the largest mover is +1 sigma (+30.6) then L 0 to 1 (+22.0), weight 0 to 3 (+18.2), church L T9 vs T2 (+9.4), one die (+11.2), `opinion_full` 1 to 3 (-4.2). At 5D: sigma +31.3 / -30.5, +1 Ob -19.2, L 0 to 1 +16.6, T9 vs T2 +6.7, one die +7.6. At 12D: -1 sigma -29.9, +1 Ob -10.2, L 0 to 1 +5.3, T9 vs T2 +2.1. At 30D everything is under 1.4 points except -1 sigma (-7.5). **The armature's claim that sigma dominates holds** (sigma / L ratio 2.1, 5.0, 7.5, 9.5 at 2, 5, 12, 30D); it is also the reason `weight x L` is the weakest lever the proposal adds: at the pool where most contests sit (5D) the T9-versus-T2 difference is 6.7 points, at 12D 2.1, at 30D 0.15.
The closed form is the armature's continuous pool; the live `roll_net` rounds the pool and reads .60 at 5D against .50 (n = 20,000, [0.593, 0.607]): a 10-point gap that is the armature's, not P3's.
Kinds: roll-level P(meets) at 2 / 5 / 12D: K3a royal tribunal (King w3, L .74) .425 / .660 / .889; K3b church at T9 .351 / .620 / .877, at T2 .247 / .561 / .861; K4 bench of one .144 / .500 / .844. **Unverified**: the eight kinds end to end over many seeds, because no kind reaches a computed proceeding (S4, S5).

## S3. Dominance and corridors (MODEL)

1. **Accused: appear versus defy.** Cost of appearing = P(sentence); cost of defying = P(sentence) x q x p_arrest, where q is the chance a polity dispatch holder serves the warrant. Over pool 2, 5, 12 x L .37, .78, 1.0 x q 0, .25, .5, 1: defy is strictly cheaper in **36 of 36** cells ([0.90, 1.0]). At q = 0, the measured chooser (4 `arrest` attempts in 24 seasons, 0 made), defying removes the whole sentence. To make appearing a choice, the contempt cost must equal P x (1 - q x p_arrest): .25 to .88 custody units at q = 0 and .13 to .31 at q = 1, depending on pool and L (log `contempt_cost_needed_for_indifference`). The proposal builds no such cost.
2. **Forum contest as a normal form** (payoff +1 own forum, 0 impasse, -1 other's). Committing to the other's forum is dominated by silence and by committing to your own; silence is weakly dominated by committing to your own; **(commit own, commit own) is an impasse and is the only pure equilibrium**. (The log labels weak dominance "strictly"; corrected in a `fail` note.) Every non-royal forum matter therefore ends undecided, which R-1 permits but a world that "churns" does not want as its only outcome.
3. **Bringing a royal person in.** P3's default makes the polity bench decide when a royal person is a party. Petitions that name a royal person are 50 of 133 filed petitions (38%, [0.30, 0.46]); 4 of 83 persons are royal (4.8%). Being the subject of a royal petition is cheap and, by R-34's rule, moves the forum to the polity. A corridor, not a dominance: it is open to anyone, at the price of one `petition`.
4. **Forum shopping by L.** In all five territories sampled (T1, T2, T4, T9, T14) at 2, 5 and 12D, the polity row (King weight 3, L .57 to .77) beats the church row (weight 2, L .37 to .78) on the accuser's odds: margins 1.3 to 15.9 points (log `forum_shopping_argmax`; 15 of 15 cells). The church row is never the better forum for an accuser, even in T9. "Pick the authority with the larger weight x L" is a lookup, and its answer is always the polity.
Options inherited unchanged from the armature (speech kinds, the plea) are not enumerated (`skipped`).

## S4. Throughput and pace

Acts needed (scene budget 5 per person per season; one tick per season): A polity tribunal 2 (`open_case`, `determine`); B church custody outside T9 3 (+ `arrest` by a second actor); C B plus an appeal 7 (+ `petition`, `carry`, appellate `determine`, closure); D forum contest then A 6. No route exceeds one person's budget; the dependency chain across persons is the limit.
Real rates (3 seeds x 8 seasons): `open_case` attempted 72, opened 28 (39%, [0.29, 0.50]), `case.unauthorized` 12 (17%, [0.10, 0.27]), `case.refused` 32 (44%, [0.34, 0.56]); `determine` attempted 65, executed 3 (4.6%, [0.016, 0.127]), all `matter.undetermined`; `pardon` 45 attempted, all `pardon.refused`; `arrest` 4 attempted, 0 made; `carry` 295 attempted, 24 `petition.carried`.
MC over stage chains (n = 6,000 per cell; p_stage = chance the chooser forms the stage in a season, real `p_success` for the rolls). At p_stage .2, one stage per season: route A disposed within 2 / 4 / 8 / 16 seasons .02 / .12 / .35 / .70; **route B with q = 0 is disposed in 0 of 6,000 at every horizon** (control: q = 1 gives .34 by 16 seasons); route C with q = 1 gives .005 by 16. Chaining stages inside a season (5 rounds) lifts A to .46 / .81 / .98 / 1.0 and B (q = 1) to .13 / .49 / .89 / 1.0. Stalls are the rule when the arm is not served.

## S5. Real data (`build_realm`, 83 persons, 17 territories, 37 settlements)

- **Legitimacy L** (seed 0; seeds 1 and 2 identical): Crown 0.50 to 0.77 (median .57), Hafenmark 0.50 to 0.80 (.56), Varfell 0.50 to 0.71 (.53), Church 0.37 to 0.77 (median **.50**). Exactly .50 in 8 of 16 territories for every faction. Below .50: church only, 3 of 16 (T2 .367, T3 .450, T4 .379); no polity faction anywhere. Omitted from the proposal's lists: church T5 .548, Crown T8 .630. Weighting residents by `Person.weight` (cohorts are weight 2) moves L by up to .04 to .07, and the proposal does not say which it means.
- **Which venue.** Persons live at 37 settlements and 46 hearths; no case is heard "at" a territory. At settlement level 28 of 37 (76%, [0.60, 0.87]) have two residents or fewer, and church L ranges .30 to .77 across them. L at a hearth is the accused's own opinion. P3 does not say which rung's L the draw reads.
- **Benches.** Distinct bench size over 83 homes, live rule: 0 (1), 2 (61), 4 (12), 5 (9). Polity filter: 0 (1), 2 (70), 4 (12). Church filter: 0 for **74 of 83 (89%, [0.81, 0.94])**, 3 for 9. Church with Q1 scope: 0 for 1, 3 for 82. `parties`: 0 for 83. Hafenmark has no determining seat; its polity bench is the King and Queen.
- **Who can open a case**: polity 82/83 homes, church 9/83 (10.8%, [0.06, 0.19]). **A forum contest (two authorities able to open on one matter) can exist for those 9 homes only**, all in T9.
- **Royal party** (G2, 3 seeds x 8 seasons): see claim 26. For computed petitions the subject and the addressee are the same person (H-94), so "party" and "addressee" are one count.

## S6. Failure injection (real fold)

Kill the opener mid-proceeding: the docket item survives and another church seat determines it (`matter.determined`); the dead actor's act is `act.ineligible`. Revoke the seat: `determine.refused`, item kept. Vacate the church bench: the King still determines a church-row matter (live code reads no row). Vacate every determining seat: `determine.refused`, item kept. **Burn the case file**: `record.destroyed`, then `determine` still executes; the case file is not load-bearing for the determination (relevant to the "summons" claim and to Proposal 2's case file). Two authorities on one matter: the second is `case.refused`. Party with no capability: **NULL**, none is authored. Compare with P3 §9.1 ("an empty bench ... leave the matter on the docket, never a refusal"): the matter stays, but a `determine.refused` Event is emitted, so "never a refusal" is false for the bench. Not run: seizing the case file (`skipped`).

## S7. Determinism and scale

Same seed twice, 2 seasons each: 28,665 events, identical event-stream hash (`db05856f...`) and content hash (`9e71dfe9...`) (n = 2 reps; 55 to 57 s each under load from other processes). The L index costs 0.036 s at 685 tenures, 0.17 s at 6,850, 0.95 s at 34,250 (4 factions x 83 persons; roughly linear in tenures). A larger realm cannot be built: 83 persons is `build_realm`'s maximum (`cap` only reduces) (`skipped`).

## S8. Scratch-copy batch C1

P3's C1 is the §5 "Deletes first" list. Applied cumulatively in a scratch worktree of HEAD, each step running only the files it can reach, no `-x` so counts are whole. **Results: see the table below, filled from the worktree log.**

P3's C1 is the §5 "Deletes first" list: the kernel directory, four row keys (`bench_basis`, `appeal_basis`, `venue_min_rank`, `records_dissent`), `judging_set`'s `matter` parameter, the stale kernel identity row (`module_contracts.yaml:448-470`), and `contest()`'s `extension`. I applied them cumulatively in a scratch worktree of HEAD and ran only the files each step can reach (24 distinct files, none the full suite), without `-x` so counts are whole. **Control: all 24 files green before any edit (0 red).** No repointing was applied (the proposal says nine sites need repointing and lists none), so this is the cost of the deletions as a first half.

| step | edit | files run | red after | what failed |
|---|---|---|---|---|
| 1 | delete `systems/social_contest/sim/contest/` (16 tracked files, not 18; the 31 in the log include `__pycache__`) | 10 | **7** | `test_contest_kernel` (1/1); `test_sigma_leverage_parity` (**collection error**, all 901 tests lost; the assessors' finding); `test_import_cycle_game_state_npe` (1/1); `test_engine_does_not_import_systems` (1 of 16; this file takes 190 s); `test_band_extension_seam` (1 of 10); `test_structure_audit` (`test_module_contracts_sim_module_join_is_exact`); `test_degree_ladder_single_owner` (1 of 4). Green: `test_social_contest_module`, `test_tn7_always`, `test_balance_oracle_arms` |
| 2 | remove the four keys from `arrangements.yaml` (32 lines) and the loader | 3 | **2** | `test_arrangements` 5 of 12 failed (it pins the eight rows and the key set); `test_stress_proceedings_rehost` 1 of 10 (`..._thirteen_keys_...`). `test_u7_remit` stays green (65). The loader imports and returns 8 rows |
| 3 | drop `judging_set`'s `matter` parameter and its one caller | 3 | **2** | `test_u7_remit::test_19_judging_set_and_the_gate_read_one_bench`; `test_stress_proceedings_rehost::test_st03_the_bench_query_answers` (plus step 2's). `test_sc02_reception` green |
| 4 | delete the module_contracts row (23 lines, exactly the cited 23) | 5 + 2 | **3** | `test_flow_skeletons` 5 of 95 (`anchors_resolve[characters, mass_battle, social_contest ...]`). **And the fold breaks**: `test_u7_remit` 54 of 65 and `test_sc01_speak` 9 of 13 fail with `contest_subsystems maps 'a matter' to 'social_contest', which is in no module contract`. My first pass missed this (it ran only the contract-reading tests; logged as a `fail`) |
| 5 | drop `contest()`'s `extension` parameter | 2 | **0 new** | with the contract row restored (5b) the two files are green except step 3's one test; with the row deleted again (4b) the 54 + 9 return. The unread-parameter claim holds; the "stale row" claim does not |

Tally: **12 of the 24 files go red at some step** (kernel, parity, import-cycle, no-subsystem-import, band-extension, structure-audit, ladder-owner, arrangements, rehost, u7-remit, flow-skeletons, sc01-speak). The proposal's C1 "green" is false for a bare deletion; the assessors named one of these twelve. The assessors' "the four keys appear 44 times across three test files" does not reproduce: 30 literal occurrences in one test file (`test_arrangements.py`), 57 in `engine/` and `tests/` together; a second file fails on the key count. The audit's "stale legacy row" at `module_contracts.yaml:448-470` is load-bearing: its `sim_module` path is stale, its existence is not. Claims that are UNTESTABLE here: that a repointing of the nine sites returns the twelve to green, and the "one `FORK:` row per deletion" (a ledger convention, not a test). Stop: all five steps ran; no file hit the 240 s timeout (slowest 193 s). Worktree removed.

## 11. Fidelity statement

REAL: `build_realm`; `world_q.opinion_of`, `residence_of`, `ancestry`, `judging_set`, `place_of`, `docketed_under`; `gate.purview_reaches`, `sits_over`, `may_determine`; the fold (`SeasonDriver.resolve`) on the real realm for `open_case`, `determine`, `pardon`, `issue`, `give`, `arrest`, `evade / defy`, `destroy_record`, `world.write`; the shipped chooser over 24 real seasons; `sigma_leverage.p_success`, `roll_net`, `net_boost`; the repo's own test files in a scratch worktree. MODEL, all labelled in the logs: the authority filter, the row-reading gate, `weight x L` as a pool operand, the legitimacy index (computed outside the fold, not as a barrier index), the payoff games, the Markov chains, the independent-judges majority. Hand-built facts: the `open_case` payloads naming an arrangement (computed play names none), the `scope_rung` / `rung` patches that emulate Q1, one hand-planted warrant `hold` (F2c, logged `unverified`), the quorum fixtures. Not exercised at all: the forum branch, the warrant branch, the appellate closure basis, the expulsion rule, the `evade / defy` reader, the continuous pool; none exists.

## 12. What would overturn each finding

- Claim 8 (Q1 does not open T1/T4): `open_case` reading `scope_rung` for admission, or Q1 specified as re-anchoring `rung` as well and the arm limit restated as a separate datum.
- Claim 10: a row-bearing argument to `may_determine` that survives the same-write docket clearing (e.g. the authority stamped on the disposal edge's grant), shown by the M3 cells reading executed = False for the King.
- Claim 15 and 16: a defiance cost (a contempt edge, a `ban`, or a suspicion carrier ED-FA-0021 names) and a summons that is a held writ; the E table with the cost added would read "appear" better in some cell.
- Claims 1 to 5: a different `opinion_of` state (the proposal's script is not saved; mine reproduces 11 of 14) or weighted means.
- The sweep findings (S2): a campaign-level instrument; none exists (`CLAUDE.md` §7).
- Claim 26: the royal rate is from 24 seasons of the shipped chooser, which forms few cases; a chooser that petitions the King more would move it.

## 13. FAILURES AND NULLS (complete roll-call)

56 lines across the five logs (13 of them are the claim-level BROKE verdicts, restated as `fail` lines by section `verdicts`; the underlying evidence lines are in the cited sections). Duplicated `notes` lines are from running that section twice (the second run was not needed; both kept).

| log | line | kind | section | what |
|---|---|---|---|---|
| p3-authority-seasons-s0 | 7 | error | sec_G | TypeError: _tee_resolve.<locals>.resolve() takes 2 positional arguments but 3 were given |
| p3-authority-seasons-s1 | 7 | error | sec_G | TypeError: _tee_resolve.<locals>.resolve() takes 2 positional arguments but 3 were given |
| p3-authority-seasons-s2 | 7 | error | sec_G | TypeError: _tee_resolve.<locals>.resolve() takes 2 positional arguments but 3 were given |
| p3-authority-worktree | 2 | blocked | H | no such section in this harness version  |
| p3-authority-worktree | 18 | fail | H | first H launch ran the baseline with test_engine_does_not_import_systems.py (a slow subprocess-import test, 3+ CPU minutes, listed three times across the phase sets) and engine/season/tests/test_season_shape.py (5+ CPU minutes; it |
| p3-authority-worktree | 73 | fail | H | my phase 4 ran only the contract-reading tests, so it MISSED that deleting the module_contracts `social_contest` row breaks the fold: the phase 5 files (u7_remit 54 of 65, sc01_speak 9 of 13 failed) read `contest_subsystems maps ' |
| p3-authority-worktree | 74 | fail | H | claim: the kernel is "18 files" (P3 5, CA B-1)  |
| p3-authority | 11 | fail | A | Church of Solmund terr_T9: claimed 0.78, reproduced 0.774 |
| p3-authority | 12 | fail | A | Church of Solmund terr_T8: claimed 0.59, reproduced 0.584 |
| p3-authority | 19 | fail | A | Crown terr_T14: claimed 0.75, reproduced 0.743 |
| p3-authority | 29 | fail | A | territories ['terr_T15']: L undefined (0/0) |
| p3-authority | 93 | null | A2 | L_tables_equal_across_seeds: legitimacy_table() for seeds 0,1,2 compared entry by entry to 9 dp |
| p3-authority | 149 | fail | B | my first B harness shared one world per variant across seats: the Confessor, Cardinal Justice and King rows at T9 (and every row of the Q1_scope_and_rung variant after the first seat) read `case.refused` because the Senior Inquisi |
| p3-authority | 321 | blocked | F | church issue of a warrant produced no dispensation Record (see F2_issue_warrant events); first blocker is the issue precondition at the fold  |
| p3-authority | 330 | fail | F | F4 as first written is not the wedge test: F3 had pardoned the ban, so the re-open and second determine both executed (determine_again = matter.determined) and the docket was empty when the second authority tried to open. F2 stopp |
| p3-authority | 336 | unverified | F2 | King's hold on the church warrant hand-planted because give was refused (not co-located); delivery step not exercised  |
| p3-authority | 345 | fail | S1 | opinion_full=0.0: ZeroDivisionError |
| p3-authority | 380 | unverified | S2 | the eight kinds end to end over many seeds: no kind runs from a computed case today (computed open_case names no row, G logs), so a seeded distribution of a whole kind would be a distribution of my model, not of the code  |
| p3-authority | 405 | error | sec_S6 | InstrumentDefect: World.remove_person('p_npc_004') was called with no gate write open. AX-4 (`04:115`, 'one write path that applies the write and returns a receipt') re |
| p3-authority | 410 | fail | S1 | my S1 grid note said a NaN operand "poisons p_success". The grid found 0 non-finite cells in 864, so that reading was wrong for NaN in the POOL position: max(1.0, nan) is 1.0, so a NaN pool is silently the 1D floor.  |
| p3-authority | 411 | fail | S1 | my S1 first-attempt S6 call `remove_person` outside a write window raised InstrumentDefect (AX-4); S6 was rerun through World.write (see S6 lines after this one)  |
| p3-authority | 416 | error | sec_S6 | Forbidden: [FORBIDDEN] (Person, exists) written in class MATTER at RESOLVE; the matrix says ACTS  @S30.2 |
| p3-authority | 424 | error | sec_S7 | InstrumentDefect: w.tenures is a READ-ONLY VIEW over the subjects that own the Tenures (S15.1). Use w.add_tenure(t) -- it routes by subject to the owner. Mutating the c |
| p3-authority | 431 | error | sec_S6 | Forbidden: [FORBIDDEN] Event '7f594174b8f21f88' (person.died) names cause(s) that resolve to nothing: ['root']  @S19.4  needs: each cause to be a prior Event id, |
| p3-authority | 434 | fail | S7 | first S7 cost probe did `w.tenures.append(...)`; w.tenures is a read-only view (S15.1) and raised InstrumentDefect after the determinism half had run. Rerun through w.add_tenure.  |
| p3-authority | 438 | skipped | S7 | large realm build_realm seats every authored case: 83 persons is the maximum (cap only reduces; foreign=True adds 2 offices). No larger world exists to build; scale is extrapolated from the tenure-inflation line, not run |
| p3-authority | 459 | error | sec_G2 | TypeError: Log.w() got multiple values for argument 'kind' |
| p3-authority | 526 | fail | E | my E dominance labels: in `forum_contest_normal_form` I tagged a dominance "strictly" when the dominating strategy was >= everywhere and > somewhere. That is WEAK dominance in the textbook sense. Read every "strictly" in P_dominat |
| p3-authority | 527 | fail | S6 | my `kill_judge_mid_proceeding` trial logged `docket_still_has_party` AFTER the second church judge had already determined the matter, so False there means "determined", not "lost". The evidence the item survived the opener's death |
| p3-authority | 528 | fail | G | my first G run (all three seeds) crashed on the first season: the resolve() tee did not forward the driver's third positional argument. Fixed and rerun; the first-attempt errors are the first lines of each seasons log.  |
| p3-authority | 529 | fail | G | my G run stopped on --budget-s (540 s), not on a crash or a quiet world, at 8 seasons per seed; wall_s of each season grew with the docket; three seeds ran concurrently with other work, so absolute times are inflated (ratios withi |
| p3-authority | 534 | skipped | misc | S3: denial in a staged plea a Proposal-2 mechanism (stage list, plea act); Proposal 3 has no plea stage, so there is no option set to enumerate |
| p3-authority | 535 | skipped | misc | S3: "pick the apt speech kind" as a lookup speech kinds and aptness price belong to the shared armature (ARM B2), which Proposal 3 does not change (P3 3.3: "the armature's draw, unchanged"); nothing P3-specific to test |
| p3-authority | 536 | skipped | misc | S3: expected payoff at 2D/5D/12D for every actor option done for the three option sets P3 adds (accused appear/defy, forum commit/silent, forum shopping) in section E; options inherited unchanged from the armature are not enumerat |
| p3-authority | 537 | skipped | misc | S6: seize the case file `seize` needs a held warrant Record naming the Record and a seat granted seize; the case file is a kind-text Record whose `seize` path is not reachable from P3; burn was run instead (S6 burn_case_file) |
| p3-authority | 538 | skipped | misc | S6: second case on a docketed matter, two authorities open one matter run in section F2 (F4c): case.refused for the second opener; the real code has no forum branch |
| p3-authority | 539 | skipped | misc | S2: each worked example and each of the eight kinds over many seeds (seeded end to end) no kind reaches a computed proceeding with a row today (computed open_case names none: G logs docket_named_arrangement = 0), and P3's forum, w |
| p3-authority | 540 | skipped | misc | S8: running the full suite or CI jobs forbidden by the brief; only the files each C1 step can reach were run |
| p3-authority | 541 | skipped | misc | worked example A (4): Partial "leaves a docket matter (R-17)" run indirectly: the live determine opens the edge on Partial (writes Tenure.since for Partial) so Partial does not leave a docket matter in the live code; not re-derive |
| p3-authority | 544 | fail | E | my E dominance labels: in `forum_contest_normal_form` I tagged a dominance "strictly" when the dominating strategy was >= everywhere and > somewhere. That is WEAK dominance in the textbook sense. Read every "strictly" in P_dominat |
| p3-authority | 545 | fail | S6 | my `kill_judge_mid_proceeding` trial logged `docket_still_has_party` AFTER the second church judge had already determined the matter, so False there means "determined", not "lost". The evidence the item survived the opener's death |
| p3-authority | 546 | fail | G | my first G run (all three seeds) crashed on the first season: the resolve() tee did not forward the driver's third positional argument. Fixed and rerun; the first-attempt errors are the first lines of each seasons log.  |
| p3-authority | 547 | fail | G | my G run stopped on --budget-s (540 s), not on a crash or a quiet world, at 8 seasons per seed; wall_s of each season grew with the docket; three seeds ran concurrently with other work, so absolute times are inflated (ratios withi |
| p3-authority | 558 | fail | verdicts |   |
| p3-authority | 559 | fail | verdicts |   |
| p3-authority | 560 | fail | verdicts |   |
| p3-authority | 561 | fail | verdicts |   |
| p3-authority | 562 | fail | verdicts |   |
| p3-authority | 563 | fail | verdicts |   |
| p3-authority | 564 | fail | verdicts |   |
| p3-authority | 565 | fail | verdicts |   |
| p3-authority | 566 | fail | verdicts |   |
| p3-authority | 567 | fail | verdicts |   |
| p3-authority | 568 | fail | verdicts |   |
| p3-authority | 569 | fail | verdicts |   |
| p3-authority | 570 | null | verdicts | None: the forum branch, warrant branch, appellate closure basis, expulsion rule and evade/defy reader are not in the tree (grep of loop/ and state |

