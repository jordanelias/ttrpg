# Stress test of Proposal 2, "Staged proceeding"

## Status: REFERENCE (2026-10-30). A terminal pass whose verdict is the thing asked for, recorded beside the harness and the logs that produced it (`CLAUDE.md` §0, terminal-pass exception). It allocates no `ED`/`PP`, queues no work and changes no tracked file. Every number is read from a log in this folder.

Subject: `2026-10-30-social-contest-proposal-2-staged-proceeding.md` (**P2**). Harness: `stress_p2.py`. Logs: `2026-10-30-stress-log-p2-staged-{model,world,batches}.jsonl`. HEAD `404e8023`, Python 3.13.17, `PYTHONHASHSEED=0`, Linux, a shared machine at load 5 to 10 (wall times are not benchmarks).

## 0. Verdict

P2's one distinctive claim is that a proceeding's position can live on the case file, so that burning, seizing, forging or orphaning the file stalls the proceeding inside the world. **On the existing code that claim is true of exactly one thing, MATTER's maturation of a stage, and even there it does not "resume".** `determine` never reads the file, so burning it stalls nothing; the `forge` verb cannot forge a case file (it mints a faction sheet); any person with `create_record` can overwrite the file's whole agenda by naming its id; and a stage whose due tick passes while its holder is away never matures, ever. P2's forum-detour showcase (two benches each holding an item about one man) is refused by the live second-case rule in 3 of 3 row pairs, and the escape (docket the subsidiary question under another id) produces an item `determine` can never close. Its K6 parliament row cannot be opened by the case-file route at all, because `open_case` declines both Record-disposing rows. On pace, the model on the real band probabilities says staging does not stall cases (open mass is gone inside 20 seasons in every configuration tested except two named below); it **thins** them: a Failure at `admit` or `proof` ends the file, so at equals only 4 to 10% of 2D to 5D staged cases reach a disposal against 26 to 38% for one draw (66% against 80% at 12D), and a disposal that does arrive takes 1.3 to 2.1 seasons on average under the sitting rule and 3.4 to 4.3 under the season-per-stage rule. P2's own arithmetic is off: the six-stage row costs at most five closing draws and on any plea path of its own plea table three to five, never six. The assessors' plea finding holds only partly: denial is weakly dominant in 21 of 27 accuser-burden configurations, but justification beats it in 6 (a 12D accuser, or a 12D respondent against a 5D accuser), and conceding the fact alone is strictly dominated in 26 of 27 even at a season cost of 0.15. Collapsing an unwatched contest to its terminal stage moves the outcome distribution by more than 0.05 in total variation in 52 of 54 configurations. P2's own falsifier is met: three seeds, two seasons each, 13 cases opened by computed play, `determine` executed 0 times. In the scratch worktree S1's "pure deletions" are not green: the kernel deletion alone turns 6 test files and the `sim_params` exporter check red, deleting the H-80 stages moves both pinned-hash tests before S4 is reached, and P2's S4 key does move the pins as it says, but also reddens two docket-shape tests it does not name; its S2 (not S4) moves them too.

## 1. Claims ledger

Result codes: HELD, BROKE, NULL, BLOCKED, UNTESTABLE. Counts marked "exact" are exact computations over the engine's integer net pmf (no sampling; the pmf is checked against `roll_pool` in the control, `model.control`), so they carry no interval; samples carry n and a Wilson 95% interval. "Log line" is `file:line` in the named log; `m` model, `w` world, `b` batches.

| # | claim | where | test | result | n / interval | log |
|---|---|---|---|---|---|---|
| 1 | `Record.stages` on the case file that `open_case` mints can carry the agenda | P2 3.1 | declared P2's six labels on a real `open_case` (tiny_world; build_realm(0) Senior Inquisitor) | HELD (labels are not validated at all: `banana` and `''` accepted) | n=1 each, deterministic | w `world.w1.A`, `world.w1b.open` |
| 2 | MATTER does not mature a stage whose holder is gone | 3.1, flowchart | holder deleted / hold closed at the stage's due tick | HELD for that stage | n=2 variants + 1 realm replication | w `world.w1.C_holder_gap` |
| 3 | "a seated one resumes it" (an empty bench halts the agenda) | 9a | holder returns the next tick | **BROKE**: the stage due during the absence never matures (matter.py matures only at `due == w.tick`) | 3 of 3 runs | w `world.w1.C_holder_gap`, `world.w1b.holder_gap` |
| 4 | "a burnt, seized or orphaned file stalls the proceeding inside the world" | 1, flowchart | `destroy_record` then `determine` | **BROKE** on existing code: `determine` still executes (docket is the only thing it reads) | n=1 tiny_world; realm burn confirms the docket item survives | w `world.w1.D_burn` |
| 5 | the file can be "forged" | flowchart, 7, 8 Q2 | `forge` verb on the case file | **BROKE**: `forge.refused` (it mints a faction sheet) | n=1 | w `world.w1.E_forge_verb` |
| 6 | (not claimed by P2) overwrite of the agenda | 8 Q2 | `create_record` naming the existing id, by a stranger, a clerk, the holder | new finding: agenda replaced in 3 of 3 actors, no seat, no warrant | 3 of 3, Wilson [0.44, 1.0] | w `world.w1.E_create_record_overwrite` |
| 7 | the file can be seized | flowchart, 3.7 | planted hold, warrant, `seize` | HELD (`record.seized`, hold moves; the file keeps maturing for its new holder) | n=1 | w `world.w1.F_seize` |
| 8 | the forum detour docket-items "jurisdiction over this clerk" so two benches each hold an item about one man | 4 (example 2), 3.5, 9b(3) | `open_case` twice on one matter under (royal, church), (royal, royal), (tribunal, excommunication) | **BROKE**: `case.refused` 3 of 3 | n=3 pairs, Wilson [0.44, 1.0] | w `world.w2.second_case_same_matter` |
| 9 | a subsidiary item can be written (referred; a question taken up) | 3.5 | dock under the case file's id, then `determine` | **BROKE**: docks, then `determine.refused`: a wedge | n=1 | w `world.w2.subsidiary_as_record_matter` |
| 10 | today's wedge exists, and P2's transition ends it | 3.6 | open, determine, re-open, determine | wedge reproduced (HELD that it exists); P2's fix is unbuilt (UNTESTABLE) | n=1 | w `world.w2.reopen_wedge` |
| 11 | K6 `[admit, licence]` on a case file | 4, 3.1 | `open_case` under all eight rows | **BROKE** for the two Record-disposing rows (`parliamentary_debate`, `council_of_state`): `case.refused`; the other six open and determine | 8 rows | w `world.w2.eight_rows` |
| 12 | "six stages costs six closing acts" | 3.2 | count draws on the flowchart's rules | **BROKE**: at most 5 (plea has none); 3 to 5 on the plea table's paths | exact | m `model.draw_count` |
| 13 | a six-stage trial takes ~3 seasons and most of a judge's scene budget | 7 Weakest 1 | chain, B=5 and B=2, sitting vs season-per-stage | mixed: B=5 never binds (4 draws); seasons come from Partial detours: mean 1.3 to 2.1 seasons given a disposal (12D to 2D, sitting), 3.4 to 4.3 under season-per-stage; B=2 binds | exact | m `model.pace_q0` |
| 14 | staging reaches disposal about as often as one draw (implicit) | 3.2, 7 | chain vs P1 baselines A (Partial ends) and B (Partial re-dockets) | **BROKE**: 4.3 / 10.1 / 66.0% (2D/5D/12D, live ceiling, no forum challenge) against 26 / 38 / 79.6% (A) and 38 / 49 / 87% (B) | exact | m `model.pace`, `model.pace_q0` |
| 15 | Partial "either pushes a stage or writes a docket item", cap optional | 3.5 | forced-Partial act (`impugn_motive` is Partial by construction) | **BROKE** (gap): open mass 1.0 forever without a cap | exact | m `model.pace.forced_partial` |
| 16 | S27.4 interplay (not discussed by P2) | n/a | chain with Ob above twice the pool | 24 of 648 grid cells stall for ever (uncapped 2D vs 12D, ob 6 > 4) | exact | m `model.pace` |
| 17 | assessor: denial is weakly dominant for the respondent where the accuser bears the burden | comparison 4 | payoff model deny/concede/justify, 27 configs | **partly HELD**: deny weakly dominant 21/27 (78%), strictly 20/27; justify wins 6/27 (accuser 12D under the live ceiling for any respondent; accuser 12D v respondent 5D or 12D at ceiling 3; respondent 12D v accuser 5D at the live ceiling); concede-only strictly dominated 26/27 | exact, 27 configs | m `model.plea.summary` |
| 18 | control: conceding rewarded | (brief) | judgment Ob + delta (0.5, 1, 2) on concede | a reward flips the best option away from deny in 47 of 81 (ceiling, accuser, respondent, reward-route) cells; routed through the obstacle it is clipped to nothing under the live ceiling in 6 of 9 | exact | m `model.plea.control_reward.summary`, `model.plea.ceiling_clip` |
| 19 | season cost makes conceding worthwhile | (brief) | cost 0.05 and 0.15 per adjournment | NULL: concede is best in 0 of 81 (27 configs x 3 costs) | exact | m `model.plea` |
| 20 | "concede the fact, fight on justification" is a real choice (R's intuit) | 7 | same model | **BROKE** as written: the concession half is dominated; the justification half is a real choice only for strong respondents | exact | m `model.plea.summary` |
| 21 | collapsing to the terminal stage breaks AR B30 "same draw" | 8 Q3 | chain full vs terminal-only | HELD, and understated: TV > 0.05 in 52 of 54 configs (max 0.99995, min 0.0); the per-act draw value is keyed by `H(seed,tick,subject,purpose)` so it can still be identical (UNVERIFIED) | exact | m `model.collapse.summary`, `model.collapse.b30_nuance` |
| 22 | armature H.2: sigma dominates dice at high pools | AR H.2 (P2 3.2 inherits) | exact net pmf, +1.5 sigma vs +1/2/3 dice, pools 2,5,12,30 | HELD: at 12D sigma 1.5 lifts P(meets) .394 to .796, three extra dice to .558; Ob-equivalent 4.0 (exact) vs 3.17 (closed form) | exact | m `model.sigma_channel` |
| 23 | "the pinned season hashes in S4's row move once" | 9c, 6 | `case` key added to `_docket_item` in a scratch worktree, then pytest | HELD for `BASE_HASHES[1]`, `[2]` and 3 of 3 go07 seeds; `[0]` unmoved; 2 unclaimed docket-shape tests red | n=3 seeds, deterministic | b `batches2.S4_case_key_alone`, `batches3.seed_hashes` |
| 23b | S1 "suite green with fewer files" | 6 | S1a to S1e in the worktree, baseline green | **BROKE**: 6 test files + 1 exporter check red on the kernel deletion alone; S1d moves the pins; S1e red in `test_arrangements` | 15 files | b `batches.S1a`, `batches2.S1d_alone`, `batches2.S1e_alone` |
| 24 | S2 moves nothing pinned | 6 (S2 row lists no re-pin) | `pool_default` 3 and 5 on seed 0, one season | **BROKE**: the pinned one-season hash moves under both (81be20df, b9d6534d vs 873525df) | n=2 arms, control reproduces the pin | w `world.s2_proxy` |
| 25 | falsifier: "S8's count of case files whose head moved, over three seeds" | 7 | 3 seeds x 2 seasons, shipped chooser | **MET**: 13 cases opened, 20 `determine.refused`, 0 determined, 0 heads moved | 6 seed-seasons | w `world.w5.falsifier` |
| 26 | "a stage with no seated decider wedges until its file matures (lapse, R-1)" | 9a, 4 (K4) | seat hold closed / judge deleted, 6 ticks | **BROKE**: the docket item is still there six ticks later in 2 of 2 injections (file matured in one, never in the other; control determines and clears it) | n=2 + control | w `world.w3.injection` |
| 27 | the King and Queen sit on every bench; `stage_of` + `decider_basis` repairs it | 3.4, AR I.7 | `judging_set` over every non-person rung, seeds 0, 1, 2 | HELD (the defect); the repair is unbuilt | 319 of 319 non-empty benches per seed, Wilson [0.988, 1.0]; 0 church-only benches | w `world.w4.king_on_every_bench` |
| 28 | the opener and the closer are separable seats (admit by an accusing seat) | 4 (K3 row) | `open_case` and `determine` eligibility | BROKE: both are `remit:determine` | 2 verbs | w `world.w4.eligibility` |
| 29 | same seed twice is identical | 9c, AR | seed 0 one season twice; pin control; seeds 1, 2 against go07 BASE | HELD | 3 seeds + 1 rerun | w `world.w5.determinism`, `world.w5.pin_control` |
| 30 | "citations are file:line, opened" | header | 18 citations opened | 7 missed (5 in `effects_information.py`, off by about 25 lines; `test_season_weather.py` 378 vs 382; one harness false-miss on `gate.py`) | 18 | m `model.cite` |

## 2. S1 to S8

### S1 Extremes

*Real code* (`world.w2.real_extremes`, `model.extremes`): an unknown row, a list-valued row: `case.refused` (HELD, no exception). A missing party: `case.unauthorized`. **Empty stage list: accepted, and the file gets 3 default stages** (the H-80 stand-in fills in, so an act that declares `[]` is overridden). A NaN due tick and a negative due tick: accepted, 1 stage each (no validation). 50 stages: accepted. Stage labels are unvalidated on the file (claim 1). Pool -1, 0, 1, 5, 12, 30 with an aptness price as an extra obstacle term (`forgery_quality` is the real additive operand): all computed; pool <= 0 rolls as 1D; **a NaN price gives a NaN obstacle that S27.4 does not refuse (`nan > 2*pool` is False) and the ladder grades as Failure**: a silent stage failure from a price with no domain (`model.extremes.nan_ladder`). *Model*: an empty stage list disposes of itself; a row without a terminal stage disposes when its list runs out; neither is addressed by P2 (it puts the unknown-id refusal in the loader). Obstacle above any ceiling: the live ceiling 2 removes the question for every pool >= 1; uncapped, 24 of 648 grid cells stall for ever on S27.4. Skipped: zero and huge weights, legitimacy 0 and 1, bench sizes 1/2/7/21 (armature operands P2 inherits and does not change; logged `skipped`). One matter, many matters: `open_case` refuses a second item on a docketed matter (claim 8), so "1 to 50 matters per party" is one.

### S2 Distributions and sensitivity

One-at-a-time sweeps on P(disposed within 3 seasons) (exact). At an unfavourable base (K3, 5D v 5D, uncapped; disposal 1%): J .489, P .244, leverage .244, row .230, ceiling .063, plea .034, scene budget .0046, regime .0046, forum-raised .0031, referral .0017. At a favourable base (K3, 8D v 5D, live ceiling, no forum challenge; disposal 35.7%): **J .979, leverage .822, row .369, opposition .285, forum-raised .262, ceiling .224, plea .140, scene budget .125, regime .125, referral .051**. So the inputs that move a staged proceeding most are the same two a single draw has (the closer's pool and the leverage), then the number of gates; the staged design's own parameters (budget, regime, referral) are the weakest movers. Leverage moves in whole-number steps at these pools (-1.0 and -0.5 give the same value; 0.5 and 1.0 give the same), so the sub-integer sigma sweep the armature promises is flat (R-8's integer path). Sigma versus dice: claim 22. The armature's falsifier "share of outcome variance by channel across seeded realms" is UNTESTABLE (`null`): no producer feeds sigma, so a seeded realm has zero sigma variance.

### S3 Dominance and corridors

Claims 17 to 20. Accuser bears burden, as written (no reward, no season cost), 27 configs (3 ceilings x accuser 2/5/12D x respondent 2/5/12D): deny weakly dominant 21 (strictly 20); justification best in 6 (accuser 12D against any respondent at the live ceiling; accuser 12D against a 5D or 12D respondent at ceiling 3; a 12D respondent against a 5D accuser at the live ceiling); concede-only strictly dominated in 26 (tied in the one degenerate cell where nothing can be lost). Respondent bears the burden: deny weakly dominant in 18 of 27. **Corridors:** (1) `concede_fact` alone has no case in which it is best at any pool, any ceiling, any season cost up to 0.15; it is a dominated option the roster carries. (2) The plea is a real decision only when the proof stage is near-certain against the respondent (a 12D accuser) or the respondent's own justification draw is strong (12D): elsewhere denial wins, so the choice is a corridor for those two cases and a lookup otherwise. (3) Under the live ceiling 2, a conceding reward routed through the obstacle is clipped away in 6 of 9 configurations, so the usual lever for "make conceding pay" is dead until the ceiling (G1) is lifted or the reward is paid after it (the control arm "post" shows the flip). The brief's other corridors (`defy`, silence in a forum contest; "pick the apt speech kind") are P3/AR objects and not P2's; skipped.

### S4 Throughput and pace

Model (my transition table = the flowchart's right column; closing draw = the closer's pool against Ob from `roll.obstacle`, graded by `degree_from_net`; exact DP over seasons). Headline, equal parties (J = P), live ceiling, deny plea, sitting rule with scene budget 5, no forum challenge (`model.pace_q0`; `model.pace` carries the forum-raised variant):

| closer | P(disposal ever) | P(disposed within 1 / 3 seasons) | mean seasons given disposal | P(3+ seasons given disposal) | P1 one draw, Partial ends | P1 one draw, Partial re-dockets |
|---|---|---|---|---|---|---|
| 2D | 4.3% | 1.8% / 3.7% | 2.15 | 30% | 26.0% | 38.2% |
| 5D | 10.1% | 5.5% / 9.5% | 1.72 | 17% | 38.0% | 48.7% |
| 12D | 66.0% | 50.4% / 65.5% | 1.29 | 4.5% | 79.6% | 87.4% |

(Scene budget 2 raises the mean to 2.8 / 2.5 / 2.2 seasons; the season-per-stage reading of P2's Q1 gives 4.3 / 3.8 / 3.4 and puts every disposal beyond season 2.) Where the rest goes at 5D: 51% dismissed at `admit`, 28% "not proved" at `proof`, 11% undetermined at `judgment` (live ceiling, q=0). **Staging is attrition, not stall:** open mass is zero by 20 seasons in every configuration tested. Stalls exist in two places only: the forced-Partial act (claim 15) and S27.4 refusal (claim 16), where the case never leaves its stage and the Event log stays silent (a refused act emits nothing). With a favourable closer (12D v 2D, live ceiling, no forum challenge) disposal is 82.8% and 69% of cases are disposed in season 1, so a staged row is not slow when the closer is strong; the cost P2 names (pace) is real only under the season-per-stage reading or a scene budget below the draw count. **Real data:** in 6 seed-seasons computed play opened 13 cases, every one docketed under arrangement `None` (claim 25); no stage can move.

### S5 Real data (`build_realm` seeds 0, 1, 2)

Seats with a live `determine` grant: 8 per realm (Church of Solmund 3: Senior Inquisitor, Confessor, Cardinal of Justice; Crown 2: King, Queen; Varfell 2; Guilds 1), all seated. The structure is **identical across the three seeds** (the seed changes draws, not the cast or the seats), so these are three copies of one distribution, not three samples. Benches (non-person rungs, `judging_set`): realm 1 (size 2), duchy 3, territory 17, settlement 37, community 60, hearth 211; empty bench in 1 territory (5.9%), 1 settlement (2.7%), 2 communities (3.3%), 6 hearths (2.8%). **The King or Queen sits on 319 of 319 non-empty benches** and no bench is church-only; church seats reach 19 rungs, all in the T9 subtree. 82 of 83 persons have a bench over their home. A Senior Inquisitor opened a case under the royal row `legal_trial` on a T9 cohort in build_realm(0): nothing ties the seat's authority to the row. Legitimacy index, authority groupings and `stage_of` do not exist; the quantities P2 would compute from them are UNTESTABLE.

### S6 Failure injection

Claims 3, 4, 5, 6, 7, 8, 9, 10, 26. Judge removed, seat hold closed, bench vacated: `determine.refused` (seat revoked) and `act.ineligible` (judge deleted); the docket item survives six further MATTER ticks in both injections (in the seat-closed run the file matured meanwhile; in the judge-deleted run it never did, because its holder was the judge); the stage list is untouched. A second case on a docketed matter: refused every time, whatever the rows. A party with no capability: the shipped judge (2D v Ob 2) determined 20 of 60 (33%, Wilson [0.23, 0.46]) in `w3.no_capability_determine`. The lapse P2 leans on ("lapse when the file matures open, R-1") has no reader in the tree (`unverified`).

### S7 Determinism and scale

Seed 0, one season, twice in one process: identical hash `873525df...`, equal to go07's pinned `BASE[0].new`; seed 1 and seed 2 one-season hashes equal their pinned values; seed 0 two seasons equals `BASE_HASHES[2]` (`9e71dfe9...`). Wall time per season on the shared machine: 13.5 to 41 s for season 1 and 38 to 76 s for season 2 (the growth PR #530 reported; P2 does not build anything that changes it). A large realm: there is none (`build_realm` has only `cap`, smaller); skipped.

### S8 Scratch-copy batches

Scratch worktree at HEAD `404e8023` (detached; removed at the end, `git worktree list` confirms). Each file run alone with `python -m pytest <file> -q`; **baseline first: all 15 files and both hash tests green before any change (red = 0)**, so every red below is caused by the step. The full suite was not run. Attempt 1 applied S1a to S1e cumulatively; **its S1e patch was my defect** (a regex left `data/arrangements.py` with an IndentationError), which invalidated attempt 1's S1e and S4 results; both were redone alone on a reset worktree (batches2), and the false start is kept in the log (`error batches.attempt1`).

| step (P2 section 5/6) | applied | result |
|---|---|---|
| S1a delete the kernel `systems/social_contest/sim/contest/` (16 files) | `git rm -r` | **6 test files red besides the kernel's own wrapper**: `test_sigma_leverage_parity.py` (collection error: imports the kernel's `degree_extension`; the golden JSON is untouched), `test_import_cycle_game_state_npe.py` (asserts exactly three cycles; one was the kernel's), `test_engine_does_not_import_systems.py` (1 of 16), `test_band_extension_seam.py` (1 of 10), `test_structure_audit.py` (1 of 30: the `module_contracts` `sim_module` join), `test_degree_ladder_single_owner.py` (1 of 4); `engine/tests/test_contest_kernel.py` goes red (P2 says it "goes with the kernel": HELD). `tools/export_sim_params.py --check` goes red (control in the unmodified tree: rc 0). Not red: `test_tn7_always`, `test_balance_oracle_arms`, `test_social_contest_module`, `test_sc01_obstacle_ceiling`, `test_arrangements`, `test_u7_remit`, `test_sc01_fired_slot`, `test_in45_carry`. `value_pointer_links.json` (5 rows) and the full `ci_checks` were not run: unverified. |
| S1b the unreachable `degree_ladder` fallback; S1c `contest()`'s unread `extension` | edits | NULL: 0 newly red among the 6 files that could reach them (parity, band_extension, degree_ladder, sc01_obstacle, social_contest_module, u7_remit) |
| S1d delete the H-80 placeholder stages from `open_case` case files | `open_case` mints with the act's declared stages only | **red**: `test_u7_remit.py` (1 of 65: asserts the file's stages) and **both pinned-hash tests**: seed 0 one season `873525df` becomes `40cf9490`, two seasons `9e71dfe9` becomes `c7c86c67`, go07 seed 0 `new` becomes `40cf9490`; acts (599) and census unchanged, so it is a hash-only move. P2 says its hashes re-pin at **S4**; here they move in **S1** |
| S1e fold away `records_dissent` and `venue_min_rank` (rows and loader) | exact-text edit (second attempt) | loader imports (8 rows); `test_arrangements.py` **5 of 12 red** (its fixture row `examination` still carries the keys and the loader refuses unknown keys); `test_u7_remit` and `test_sc01_fired_slot` green. The "fold" is a repoint into `disposal_reach` and `admit`, which are S3/S5 objects: S1 cannot do it as a deletion |
| S4 the `case` key in `_docket_item` | one key, `None` in computed play | **pinned hashes move, as P2 says (HELD)**: `BASE_HASHES[1]` `873525df` to `16812b6f`, `[2]` `9e71dfe9` to `9a4dd477`; `[0]` (the build hash) does not move. go07 `BASE` seed 0 `new` becomes `16812b6f`; seeds 1 and 2 one-season hashes also move (`a8572f82`, `f192935a`; 3 of 3 seeds), with log lengths (9378, 11960, 9726) equal to the pins' counts. **Unclaimed:** `test_sc01_fired_slot.py` (4 of 10) and `test_u7_remit.py` (2 of 65) assert the exact docket dict and go red; `test_in45_carry`, `test_seen_claim`, `test_referent_class_stamps` stay green |
| S2 (proxy) | `pool_default` 3 and 5, seed 0, one season | the pinned one-season hash moves under both: **P2's S2 row lists no re-pin**; the comparison's "S2 moves every computed roll" HELD (claim 24) |

Against the claims: P2 expects "suite green with fewer files" at S1: **BROKE** (6 test files, 1 exporter check, plus 3 more pins and a unit test if the H-80 deletion is counted in S1); it names two pinned hashes and misses two docket-shape tests and the S1d and S2 movers; the assessors' list (parity test import, the four row keys, the `test_arrangements` pin) is confirmed in each of its three parts. The cite for the pins is off by four lines (`test_season_weather.py:382-384`).


## 3. Fidelity statement

**REAL:** `engine.dice_engine` (die rule, `degree_from_net`, `net_boost`), `modules.social_contest.roll.obstacle` and `roll`, the effects `open_case`, `determine`, `destroy_record`, `create_record`, `forge`, `give`, `seize`, MATTER's maturation, the gate, the `tiny_world` and `build_realm` worlds, the shipped chooser and `SeasonDriver.season`, `judging_set`, the eight shipped arrangement rows, test files run in a scratch git worktree (`git worktree add ... HEAD`, removed at the end). **MODEL (mine, evidence about the design not the code):** every stage list, transition table, plea payoff, the sitting rule, the collapse comparison, and the "hold gone" injection by deleting a person or closing a tenure by hand. The chain uses the closer's pool and Ob from `obstacle()`; it assumes one pool and one Ob at every stage, a forum challenge probability, and that Failure at `admit`/`proof` ends the file as P2's flowchart says. The stage-aptness price, the `case` key's reader, the transition function, `stage_of` and `decider_basis` are unbuilt, so no result here is a result about them. The seize test hand-plants the other holder (the verb `give` was refused across rungs). S2's effect is proxied by `pool_default`.

## 4. What would overturn each finding

- Claims 3 to 6, 26: a MATTER change that matures overdue stages, a `determine` conjunct that reads the file (P2's S5), a lapse reader, and a `create_record` decline for an existing id would each reverse a BROKE; a test that fails without them is the observable.
- Claim 8, 9: a second-case rule keyed on (matter, row) rather than matter; or a typed subsidiary matter that `determine` can close.
- Claims 12 to 14, 21: a different transition table (Failure at `admit` not ending the file) or stage draws that share one pool; the chain is mine.
- Claims 17 to 20: a different severity scale, a respondent-burden row, or a conceding reward built into `judgment`; the model reports the break-even rather than asserting one.
- Claim 24: if S2 is built without touching any computed pool (it is the whole point of S2 that it does), the proxy is the wrong instrument.
- Claim 25: a chooser that offers `determine` (P2's S8).

## 5. Failures and nulls: the complete roll-call

Generated from the three logs by reading every line whose kind is `fail`, `error`, `blocked`, `null`, `skipped` or `unverified` (the generator is not part of the harness; its output is below unedited except for column truncation at 420 characters). `m` is `...-p2-staged-model.jsonl`, `w` is `...-world.jsonl`, `b` is `...-batches.jsonl`; the number is the line. The false starts are in it: the model's first attempt (`KeyError: 'FAILURE'`, whose own file I removed before the rerun; the line is reconstructed), the world section's first w1 (`TypeError`, my field named `kind`), w1 rerun 1 (holder removed a tick early, `give` refused), and the batches' first S1e patch (IndentationError) with the S4 result that ran after it. Runs stopped on: the model by finishing (exact computation, no sampling horizon); the world section by finishing its parts (286 s of a 900 s budget); the batches by finishing (617 s of 1500 s, then 140 s and 60 s follow-ups). Seed and season counts were not chosen: the real-world season runs are 3 seeds x 2 seasons because the 25-minute budget on a shared machine ended there, which is stated, not a horizon. The chains stop on a quiet window (open mass changing by under 1e-12 over 6 seasons, three times) or at 400 seasons; the two stall cases (forced Partial, S27.4 refusal) stop on quiet with open mass 1.0.

### fail (56)
| log:line | section | text |
|---|---|---|
| model:2 | model | first attempt wrong (enum name case), corrected in the rerun below (DE.degree_from_net(...).name) |
| model:671 | model.pace.forced_partial | P2 says "Each Partial either pushes a stage or writes a docket item" and "A cap is optional row data" (3.5); with a Partial-capped act and no cap the case never leaves its stage |
| model:729 | model.collapse | collapsing to the terminal stage changes the outcome distribution by TV>0.05 in 52 of 54 configs, so a collapsed unwatched contest is a different game from a staged one even with the identical terminal draw |
| model:1969 | model.extremes.stage_shapes | an empty stage list is treated as an immediate disposal (a case file with no agenda disposes of itself); P2 says the loader refuses an unknown stage id but is silent on an empty list or a list with no terminal stage |
| model:2093 | model.draw_count | the six-stage royal row costs at most 5 closing draws (plea has none) and, on any single plea path of P2's own plea table, 3 to 5 (4 with a forum challenge); never six. With a scene budget of 5 a judge can close every stage of a sitting in one season, so the pace cost the proposal names comes only from Partial adjournments, not from stage count |
| model:2150 | model.cite | engine/season/loop/effects_information.py:143 does not carry '_declared_stages'; the token is first at line 170 |
| model:2152 | model.cite | engine/season/loop/effects_information.py:162 does not carry '_docket_item'; the token is first at line 189 |
| model:2154 | model.cite | engine/season/loop/effects_information.py:274 does not carry 'open_case'; the token is first at line 2 |
| model:2156 | model.cite | engine/season/loop/effects_information.py:341 does not carry 'docketed'; the token is first at line 29 |
| model:2158 | model.cite | engine/season/loop/effects_information.py:419 does not carry '_eff_determine'; the token is first at line 344 |
| model:2165 | model.cite | engine/season/state/gate.py:245 does not carry 'DISPOSABLE_KINDS'; the token is first at line 159 |
| model:2167 | model.cite | engine/season/tests/test_season_weather.py:378 does not carry 'BASE_HASHES'; the token is first at line 382 |
| world:12 | world.w2.second_case_same_matter | a second open_case on a docketed matter is refused (case.refused); two benches cannot each hold an item about one man |
| world:14 | world.w2.second_case_same_matter | a second open_case on a docketed matter is refused (case.refused); two benches cannot each hold an item about one man |
| world:16 | world.w2.second_case_same_matter | a second open_case on a docketed matter is refused (case.refused); two benches cannot each hold an item about one man |
| world:19 | world.w2.subsidiary_as_record_matter | a subsidiary item docketed under a Record id is accepted by open_case but determine refuses it: the item is a wedge, never decided |
| world:31 | world.w2.eight_rows | open_case refuses ['council_of_state', 'parliamentary_debate'] (disposes: Record), so the case-file agenda P2 hangs K6 on cannot be created for a parliament |
| world:42 | world.w3.injection | seat_hold_closed: the docket item is still there 6 ticks after the file matured; nothing lapses a docketed matter |
| world:44 | world.w3.injection | judge_deleted: the docket item is still there 6 ticks after the file matured; nothing lapses a docketed matter |
| world:76 | world.w5.falsifier | P2's own falsifier is met: computed play on three seeds closes no stage (determine/undetermine executed 0 times) |
| world:95 | world.w1.C_holder_gap | a stage whose due tick passes while its holder is absent NEVER matures, even after the holder returns (matter.py matures only at due == w.tick); the agenda does not "resume" on a seated holder, it is dead for good |
| world:97 | world.w1.C_holder_gap | a stage whose due tick passes while its holder is absent NEVER matures, even after the holder returns (matter.py matures only at due == w.tick); the agenda does not "resume" on a seated holder, it is dead for good |
| world:100 | world.w1.D_burn | burning the case file does not stall anything in the existing code: determine still executes against the docket item |
| world:103 | world.w1.E_forge_verb | the forge verb cannot forge a case file (it mints a faction sheet only) |
| world:105 | world.w1.E_create_record_overwrite | p_other (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:107 | world.w1.E_create_record_overwrite | p_low (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:109 | world.w1.E_create_record_overwrite | p_high (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:120 | world.w1 | RERUN 1 of w1 had two harness defects: (1) the holder was removed one tick early so the stage that went unmatured was stage 1 (due tick 1), not stage 2 as the log text says; the phenomenon is the same but the labels in rerun 1 are off by one; (2) `give` of the case file was refused (receiver not present where the giver is), so the seize test was BLOCKED in rerun 1. Rerun 2 follows with the timing fixed and the file h |
| world:134 | world.w1.C_holder_gap | a stage whose due tick passes while its holder is absent NEVER matures, even after the holder returns (matter.py matures only at due == w.tick); the agenda does not "resume" on a seated holder, it is dead for good |
| world:136 | world.w1.C_holder_gap | a stage whose due tick passes while its holder is absent NEVER matures, even after the holder returns (matter.py matures only at due == w.tick); the agenda does not "resume" on a seated holder, it is dead for good |
| world:139 | world.w1.D_burn | burning the case file does not stall anything in the existing code: determine still executes against the docket item |
| world:142 | world.w1.E_forge_verb | the forge verb cannot forge a case file (it mints a faction sheet only) |
| world:144 | world.w1.E_create_record_overwrite | p_other (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:146 | world.w1.E_create_record_overwrite | p_low (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:148 | world.w1.E_create_record_overwrite | p_high (not necessarily the holder) overwrote the case file's whole agenda with create_record naming the existing id; no seizure, no warrant, no seat |
| world:159 | world.w1b.holder_gap | real-realm replication of the holder-gap: stage due at tick 2 never matures after the holder returns at tick 3 |
| batches:45 | batches.S1a | engine/tests/test_contest_kernel.py goes red after the kernel deletion |
| batches:46 | batches.S1a | engine/tests/test_sigma_leverage_parity.py goes red after the kernel deletion |
| batches:47 | batches.S1a | tests/valoria/test_import_cycle_game_state_npe.py goes red after the kernel deletion |
| batches:48 | batches.S1a | tests/valoria/test_engine_does_not_import_systems.py goes red after the kernel deletion |
| batches:49 | batches.S1a | tests/valoria/test_band_extension_seam.py goes red after the kernel deletion |
| batches:50 | batches.S1a | tests/valoria/test_structure_audit.py goes red after the kernel deletion |
| batches:51 | batches.S1a | tests/valoria/test_degree_ladder_single_owner.py goes red after the kernel deletion |
| batches:70 | batches.S1d | engine/season/tests/test_u7_remit.py goes red after deleting the H-80 placeholder labels from open_case case files |
| batches:71 | batches.S1d | engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes goes red after deleting the H-80 placeholder labels from open_case case files |
| batches:72 | batches.S1d | engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest goes red after deleting the H-80 placeholder labels from open_case case files |
| batches:74 | batches.S1e_keys | a mechanical removal of records_dissent and venue_min_rank from the loader and the eight rows leaves the loader unimportable; the fold into disposal_reach / admit gate is a repoint, not a deletion |
| batches:78 | batches.S1e | engine/season/tests/test_arrangements.py goes red after removing records_dissent and venue_min_rank |
| batches:92 | batches2.S1d_alone | engine/season/tests/test_u7_remit.py::test_19_open_case_puts_the_matter_on_the_docket_and_the_reader_now_sees_it red after S1d alone (deleting the H-80 placeholder stages from open_case case files) |
| batches:93 | batches2.S1d_alone | engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes red after S1d alone (deleting the H-80 placeholder stages from open_case case files) |
| batches:94 | batches2.S1d_alone | engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest red after S1d alone (deleting the H-80 placeholder stages from open_case case files) |
| batches:104 | batches2.S4_case_key_alone | engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes red after the `case` docket key alone |
| batches:105 | batches2.S4_case_key_alone | engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest red after the `case` docket key alone |
| batches:106 | batches2.S4_case_key_alone | engine/season/tests/test_sc01_fired_slot.py red after the `case` docket key alone |
| batches:107 | batches2.S4_case_key_alone | engine/season/tests/test_u7_remit.py red after the `case` docket key alone |
| batches:118 | batches2.S1e_alone | engine/season/tests/test_arrangements.py red after folding away records_dissent and venue_min_rank (mechanical removal from rows and loader) |

### error (4)
| log:line | section | text |
|---|---|---|
| model:1 | model | FIRST HARNESS ATTEMPT (kept false start): bands() mapped str(Degree) to a title-case name; the real ladder returns the enum Degree.FAILURE, so every call raised KeyError("FAILURE") and the model section died before computing anything -- KeyError: 'FAILURE' |
| world:8 | world.w1_case_file | Log.w() got multiple values for argument 'kind' -- TypeError: Log.w() got multiple values for argument 'kind' |
| world:81 | world.w1 | FIRST HARNESS ATTEMPT of w1 (above) died on my own bug: a log field named `kind` collided with the line kind; w1 produced no result in attempt 1. Rerun 1 follows. -- TypeError: Log.w() got multiple values for argument 'kind' |
| batches:86 | batches.attempt1 | attempt 1 S1e regex patch broke data/arrangements.py (IndentationError at line 174: a dangling `repr_fn=list)`); S1e and S4 results of attempt 1 are INVALID and are redone below, each step alone on a reset worktree -- HarnessDefect: attempt 1 S1e regex patch broke data/arrangements.py (IndentationError at line 174: a dangling `repr_fn=list)`); S1e and S4 results of attempt 1 are INVALID and are redone below, each ste |

### blocked (1)
| log:line | section | text |
|---|---|---|
| world:111 | world.w1.F_seize | give did not move the file (see F_give events) -- give did not move the file (see F_give events) |

### null (7)
| log:line | section | text |
|---|---|---|
| model:1922 | model.sigma_channel.variance_share | the armature falsifier "share of outcome variance by channel across seeded realms at 5D and 12D" -- found:  |
| model:2144 | model.sigma_channel.variance_share | the armature falsifier "share of outcome variance by channel across seeded realms at 5D and 12D" -- found:  |
| world:101 | world.w1.D_burn.matter | MATTER run after the case file is destroyed -- found: no exception, no term.matured for the dead id |
| world:140 | world.w1.D_burn.matter | MATTER run after the case file is destroyed -- found: no exception, no term.matured for the dead id |
| batches:108 | batches2.S4_case_key_alone | engine/season/tests/test_in45_carry.py after the `case` key -- found: passes: the key does not move it |
| batches:109 | batches2.S4_case_key_alone | engine/season/tests/test_seen_claim.py after the `case` key -- found: passes: the key does not move it |
| batches:110 | batches2.S4_case_key_alone | engine/season/tests/test_referent_class_stamps.py after the `case` key -- found: passes: the key does not move it |

### skipped (6)
| log:line | section | text |
|---|---|---|
| model:1975 | model.extremes | zero and huge weights, legitimacy 0/1, empty bench, bench of 1/2/7/21 -- reason: those operands belong to the armature (weights column, L, count Query), which P2 inherits and does not change; no P2-specific code path exists to run them against. The real-code empty-bench/seat probes are in the world section (S6). |
| world:79 | world.w5.large_realm | a large realm -- reason: build_realm has only `cap` (smaller) and a fixed roster of 81-83 persons; no larger realm exists to build (populated.py build_realm docstring) |
| world:171 | world.s4_impasse | K2 negotiation impasse (both parties must commit to the same terms) and a judge who never acts as a stall case -- reason: arrangements.yaml has no negotiation row and `disposal: mutual` has no reader (armature F; confirmed: the eight shipped rows are all disposal: bench), so there is no impasse to run; the judge who never acts is observed in computed play instead (world.w5.falsifier: 0 determinations in 6 seed-season |
| world:172 | world.s3_forum_contest | the brief's `defy` and silence in a forum contest; 'pick the apt speech kind' as a lookup -- reason: P2 has no forum contest object (its forum is a stage closed by the bench's determine on the respondent's plea, covered by world.w2 and model.plea); the speech-kind lookup is AR/P1/P3 territory. Not run. |
| world:173 | world.s1_bench_sizes | bench of 1, 2, 7, 21; legitimacy 0 and 1; zero and huge office weights -- reason: armature operands that P2 inherits unchanged; the shipped realm has benches of size 0, 2, 4, 5 only (world.w4.bench_reach), so 1, 7 and 21 cannot be built from real data and a hand-built bench would test the armature, not P2 |
| batches:9 | batches | engine/season/tests/test_season_shape.py -- reason: first attempt included it (a grep hit); it is a 15,000-line season-shape suite that only mentions the kernel path in a comment (line 15021) and ran >7 min on a shared machine at load 9; killed and removed from the list. The killed attempt's baseline results for the first 2 files are in the log above |

### unverified (2)
| log:line | section | text |
|---|---|---|
| model:731 | model.collapse.b30_nuance | that the judgment draw value is identical across fidelities -- needs a built stage-aware purpose key; not buildable here |
| world:46 | world.w3 | the lapse itself (docket item removed when the case file matures open) -- no code reads Record.matured to remove a DocketItem; P2 builds no lapse reader in S1-S8 either |
