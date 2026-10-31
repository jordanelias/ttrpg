# Stress-test findings, attributed: the proposal, or the season loop

## Status: REFERENCE (2026-10-31). A terminal pass on PR #536's reports, recorded beside them (`CLAUDE.md` §0, terminal-pass exception). It sorts existing findings by where the fault lies; it allocates nothing, queues nothing and changes no other file.

Sources: `2026-10-30-stress-test-comparison.md` and `-proposal-{1,2,3}.md`. `P1#n`, `P2#n`, `P3#n` are the claim numbers in each report's ledger. Evidence labels are the reports' own (real = engine code or data run; model = the tester's build of the proposal). Four engine sites were opened here: `matter.py:339-345`, `effects_information.py:355-368`, `effects_governance.py:335-349` and `world_q.py:567-` (`judging_set`); the S27.4 gate was only located (`harness/probes.py:2773` probes it; the `sigma.py:273` line the reports cite was not opened). Everything else is taken from the reports as written.

## The test

**Engine-side** if the finding survives deleting all three proposals: it is a fact about `engine/season/` code or the data it loads, and it would constrain any proposal or the shipped game. **Proposal-side** if it survives replacing the engine with a perfect one: a wrong claim, an arithmetic error, an omission, an unlisted dependant, a dominated option or a formula without a domain. **Seam** is the third case: an engine fact that the proposal's text asserts otherwise or omits; the engine half belongs in §1, the proposal half in §2. **Neither**: the instrument (§4).

---

## 1. Engine-side (stands with every proposal deleted)

### 1a. Code

| # | fact | where | hit |
|---|---|---|---|
| E1 | `open_case` refuses a second case on a docketed matter. **Deliberate:** the comment at `effects_information.py:355-361` says the refusal prevents a wedge. 50 matters on one party leave 1 docketed. | `:368` | P1#10, P2#8, P3#20 |
| E2 | No appeal path. `void` is not in `DISPOSABLE_KINDS`; `determine` has no void site; `pardon` closes only edges whose object is the exercised seat (documented as the closure basis). A crown `pardon` on a church ban is refused. | `:362-363`; `effects_governance.py:335-349` | P1#9, P3#21 |
| E3 | `open_case` cannot open the two Record-disposing rows (`parliamentary_debate`, `council_of_state`). | `DISPOSABLE_KINDS` | P2#11 |
| E4 | **Computed play does not reach a determination.** Computed `open_case` names no row (`docket_named_arrangement` 0 in 24 seasons). Real seasons: P1 6 opened / 0 determined; P2 13 opened / 0 determined (3 seeds × 2 seasons); P3 65 `determine` attempts, 3 executed, all `matter.undetermined` (3 × 8 seasons); `arrest` 4 attempted, 0 made; `pardon` 45 attempted, all refused; `carry` 295 attempted, 24 carried. | season logs | P1#16, P2#25, P3#17-19 |
| E5 | MATTER matures a stage only when `due == w.tick` and a live holder exists. A stage due while its holder is away never matures, even after the holder returns. | `matter.py:339-345` (opened) | P2#3 |
| E6 | `determine` reads the docket only. Burning the case file stalls nothing; `forge` mints a faction sheet, so it cannot forge a file; any person with `create_record` can overwrite a case file's agenda by naming its id (3 of 3 actors). A lapse reader ("lapse when the file matures open") does not exist. | `_eff_determine` | P2#4-6, 26; P3 S6 |
| E7 | Case-file declarations are unvalidated: stage labels accepted (`banana`, `''`), an empty stage list is replaced by 3 default stages, NaN and negative due ticks accepted, 50 stages accepted. | `open_case` | P2 S1 |
| E8 | `open_case` reads purview from `Office.rung`, not `scope_rung`. Church seats open 0 of 19 in T1 and 0 of 4 in T4 on `scope_rung` alone. | `gate.purview_reaches` | P3#8, 9 |
| E9 | The determination write clears the docket in the same write, so a gate that reads the docketed row finds none. `judging_set` takes a `matter` argument and ignores it (`world_q.py` docstring says so); opener and closer are both `remit:determine`. | `world_q.py:567-` | P3#10; P2#28 |
| E10 | `issue` requires the issuer's purview to reach the executor: 1 of 16 polity dispatch holders lies inside the Confessor's purview. `give` is refused across rungs. | gate | P3#14 |
| E11 | `evade`/`defy` form only on a held writ. The case file is a kind-`text` Record; 160 attempts, 0 executed (`compliance.impossible`). | effects | P3#15 |
| E12 | Nothing ties a seat's authority to a row: a Senior Inquisitor opened a royal-row `legal_trial` on a T9 cohort. No authority concept exists in the tree. | `open_case` | P2 S5 |
| E13 | Draw numerics: the pool floors silently at 1D (NaN, −3, 0 and −6 alike); infinity gives `inf` rolls and NaN `p_success`; a NaN obstacle is not refused by S27.4 (`nan > 2·pool` is False) and grades as Failure; leverage moves in whole-number steps at these pools (the sub-integer σ sweep is flat); `roll_net` rounds the pool (.60 at 5D against .50 for the continuous form). | `dice_engine`, `sigma.py` | P1#5, P2 S1-S2, P3 S2 |
| E14 | The S27.4 gate refuses an act whose obstacle exceeds twice the pool. | `sigma.py` | P1 S1 |
| E15 | `determine` disposes on Partial as shipped (it writes `Tenure.since`); an empty bench emits `determine.refused`. | effects | P1 S4; P3 S6 |
| E16 | Tree couplings. The kernel's removal reddens 6-7 files (`test_sigma_leverage_parity` is a collection error losing 901 tests; `test_import_cycle_game_state_npe` pins exactly three cycles). The `module_contracts.yaml:448-470` row is load-bearing: its `sim_module` path is stale, its existence is not (54 of 65 `test_u7_remit` and 9 of 13 `test_sc01_speak` fail without it). `test_arrangements` pins the eight rows and the key set; `test_season_shape` pins the load-time exit count (83) and `BASE_HASHES`; two test files take 773 s and 349 s. | tests, contracts | all three |

### 1b. Content (data the engine loads)

| # | fact | hit |
|---|---|---|
| C1 | Seeds 0, 1 and 2 build the same realm; 83 persons is the maximum. Every "three seeds" result is n = 1 realm. | P1#19, P3#5 |
| C2 | Capability is authored for 0 of 83 persons. | P1#13, #18; P3 S6 |
| C3 | Commits are sparse and held by officers: church 7 of 83 (6 in T9, 1 in T1); Crown 11 of 83, 10 by office-holders. In T9, 6 of 9 residents are committed, all church officers, 2 on the bench. No Church goal engages `solmund_orthodoxy`. | P1#1; P3#4 |
| C4 | `opinion_of` reads exactly 0.50 for all four factions in 8 of 16 territories; no polity faction falls below 0.50; T15 has no residents. 28 of 37 settlements (76%) have two residents or fewer. | P3#2, #28, S5 |
| C5 | Every band of `speak` emits a kind with one alignment vector (`grandiose_humble` −0.4), so regard cannot depend on the draw's outcome (0 of 197 decided triples flip; 98.4% of judge/speaker pairs have no regard). | P1#8 |
| C6 | The King or Queen sits on 319 of 319 non-empty benches; no bench is church-only; church seats reach 19 rungs, all in the T9 subtree; the church bench is empty for 74 of 83 homes. Hafenmark has no determining seat. | P2#27, P3#11 |
| C7 | Authority `parties` has an empty bench for 83 of 83 homes (Guilds, Löwenritter and Restoration read `parties`). | P3 S1 |
| C8 | No producer feeds σ, so a seeded realm has zero σ variance. | P2 S2 |

**What §1 adds up to.** E1-E4, E6, E8-E11 and C1-C6 are the "dead core" the comparison (§4) names. E1 is deliberate by the code's own comment, and E2 is documented in `pardon`'s docstring as the closure basis: constraints a proposal must plan around, not defects. E4-E6 and E11 are gaps in the existing implementation.

---

## 2. Proposal-side (survives a perfect engine)

### Proposal 1, one draw

| claim | fault | kind |
|---|---|---|
| L = share of residents holding a live commit | circular by construction: the committed are the institution's own officers, and the index is made of the people it weights; granular in 1/n | design (P1#1; the zero values are §1b C3) |
| "Entering two channels is impossible by construction"; falsifier "set one weight to 0" | holds at field level only; 2 of 7 church commits move two or more channels; the zero-weight falsifier still passes while L moves | design (P1#6, #7) |
| Regard link moves a judge with the draw | its premise is the verb table of C5; the belief term it intends ("disposition operand") is not in the tree, so it is `unverified`, not broken | premise (P1#8, #20) |
| Ceiling 3 "binds only where an opponent exceeds 6D" | equals curve is non-monotone: .45 at 1D, .38 at 6D, .74 at 12D, .98 at 30D; aptness price vanishes at 12D; with E14, an actor under 1.5D is refused against Ob ≥ 2-3 | design choice (G1), P1#11 |
| Pool typed float, "fractional pool"; closed form from the armature | no domain stated; the closed form is wrong below 1D against E13 | omission; armature premise |
| Failed `speak` deposit, bench `quorum` counting, missing-`authority` default | not stated; the silence-versus-speak sign flips on the first | omission (P1 S3, S1) |
| `void` appeal | needs three changes it does not list (`DISPOSABLE_KINDS`, a `_disposal` void site, a second-seat closure basis) | unlisted dependant on E2 (P1#9) |
| R-11 "many docket items per sitting" | false on E1 | claim contradicted by engine (P1#10) |
| B1 "suite green; same season, smaller" | literal items 3-4 leave a world that cannot be built (`corpus_run.py:356`); the variant that spares `VERB_CAPABILITY` moves the one-season hash (`873525df` → `521e36d9`) and reddens 6 `test_season_shape` tests it does not list; its B2 test "pools vary" fails on its own default (3 distinct pools) | scoping (P1#15, #18) |
| σ carries .67-.83 of margin variance | triggers P1's own condition (§7) to move fit into the dice; ranges are the tester's | self-triggered falsifier (P1#12) |

### Proposal 2, staged proceeding

| claim | fault | kind |
|---|---|---|
| "Six stages cost six closing acts" | at most 5 draws (the plea has none); 3-5 on any plea path | arithmetic (P2#12) |
| Staging pace | a Failure at `admit` or `proof` ends the file: deny-plea disposal 4.3 / 10.1 / 66.0% at 2D / 5D / 12D against 26 / 38 / 79.6% for one draw. Attrition, not stall | design (model) (P2#14) |
| "Each Partial pushes a stage or writes a docket item; a cap is optional" | without a cap, forced Partial never leaves its stage (open mass 1.0) | gap (P2#15) |
| Plea table | denial weakly dominant in 21 of 27 configurations (strictly 20); conceding the fact alone best in 0 of 81, even at a 0.15 season cost | design (P2#17, #19, #20) |
| Unwatched contest collapses to the terminal stage (R-24) | outcome distribution shifts by TV > 0.05 in 52 of 54 configurations | design (P2#21) |
| Empty stage list; row with no terminal stage; NaN aptness price | an empty list disposes itself; a NaN price grades as a silent Failure; the proposal puts only the unknown-id refusal in the loader | omission (P2 S1) |
| Forum detour; subsidiary item; K6 parliament row | built on a second case on one matter (E1) and on rows `open_case` cannot open (E3) | seam (P2#8, #9, #11) |
| Case-file carrier: burn, seize or orphan "stalls the proceeding inside the world" | holds only for `seize`; all else follows E5-E6 | seam; the claim was false of the tree (P2#3-5) |
| Batches | S1 "pure deletions" is red (kernel, then the H-80 stages move both pinned hashes in S1, not S4); S2 moves the one-season hash with no re-pin listed; the S4 `case` key reddens `test_sc01_fired_slot` (4 of 10) and `test_u7_remit` (2 of 65) unlisted | scoping (P2#23-24) |
| Its own falsifier ("count of case files whose head moved") | met: 0 heads moved | proposal's falsifier tripped by E4 (P2#25) |
| 18 file:line citations | 7 missed their line, five in `effects_information.py` by about 25 lines | provenance (P2#30); main moved |

### Proposal 3, authority first

| claim | fault | kind |
|---|---|---|
| Q1: re-anchor the church seat on `scope_rung`, leaving `rung`; "the church may then judge anywhere" | opens 0 of 19 (T1) and 0 of 4 (T4); moving `rung` opens them but removes the arm limit the warrant branch exists to enforce | specified on the wrong field (E8) (P3#8) |
| Bench filter and `may_determine` "read the row's authority" | filtered at the bench only, the King still determines a church-row matter; a gate-side reader sees no row (E9); quorum counts 5 members where 3 can act | design (P3#10) |
| "`open_case`'s Record is the summons; `evade`/`defy` gains its reader" | premise false (E11) | seam (P3#15) |
| "The draw is not changed by defiance" | `defy` strictly cheaper than appearing in 36 of 36 cells, and still with a warrant-serving chooser; no contempt cost is built | design (P3#16) |
| Forum contest | the only pure equilibrium is impasse; the polity row beats the church row in 15 of 15 sampled cells, so the church is never the better forum | design (model) (P3 S3) |
| Church warrant to "a polity seat at realm scope" | `issue.unauthorized` (E10) | seam (P3#14) |
| L index | undefined for T15 (0/0); `clamp01(NaN)` = 1.0; `opinion_full` < 0 inverts the sign; computed at territory level, cases are heard at a settlement or hearth, and the rung and the `Person.weight` weighting are unstated (up to .04-.07); 3 of 14 quoted figures are high by .006-.007 | domain and omission (P3 S1, S5, #1) |
| "Never a refusal" for an empty bench; `arrest` attempted 0; `determine` rolled 0 | the empty bench emits `determine.refused` (E15); the other two are from PROBE §3 and fail over 24 seasons (4 attempts; 65 attempted, 3 executed) | claim contradicted (P3#17, #18) |
| Authority map | `parties` bench empty for 83 of 83, so the seeded `arbitration` row can never be determined (C7) | grouping gap |
| Royal-party trigger (R-34) | fires rarely: a Crown seat-holder is the subject of 4 of 23 opened cases (17%); royal persons are 4.8% of the population; being a petition's subject costs one `petition` | outcome, qualified (P3#26) |
| C1 deletions "green" | 12 of 24 files go red across five steps; repeats the audit's "stale row" | scoping (P3#27) |

### Shared upstream, not one proposal

The armature's closed form `E[m] = 0.4N + 0.8√N·softcap(s) − Ob` holds for N ≥ 1 and fails below 1D (the engine floors the pool); its continuous pool is not what `roll_net` implements. The earlier code audit's finding B-12 ("stale legacy row") is wrong (E16); the comparison already carries the correction.

---

## 3. Held (no fault on either side)

P1: all 17 quoted probabilities; the 61% / 65% figures against an equal; the closed form for N ≥ 1; same-seed determinism. P2: determinism; `seize` works; the pinned-hash movement P2 predicted for S4. P3: authority grouping 19 / 7 / 5; church commit share; worked-example arithmetic (.390 to .480); same-seed stream and content hashes; Q1's predicted hash move.

---

## 4. Neither: the instrument

- **One realm, not three** (C1) and no larger realm exists: every rate has n = 1 fixture. Intervals describe the draws, not realm variety.
- **Three fixtures, three models.** A figure in one report is not comparable to another without checking its model (the comparison already says so).
- **Horizons differ**: P2 ran 3 seeds × 2 seasons; P3 ran 3 × 8. A zero over two seasons does not contradict a count over eight.
- **Not run:** the full suite, `value_pointer_links.json`, the full CI checks, `test_season_shape` in P2 (over 7 minutes), the eight kinds end to end. No critic pass.
- **Tester faults, kept in the logs**: harness `KeyError`; a deleted first log; a `sed` that corrupted a harness; a first pass that blamed the wrong step for the contract-row failures; a relative log path; an IndentationError patch that invalidated P2's first S1e and S4 results (redone).
- **Citation drift.** The proposals cite one commit and the testers ran `404e8023`; main had moved.

`[CORRECTION: comparison §2, "Two proposals' '0 attempts' claims were therefore wrong by small counts"]` P2's report records its own claim as **met**, not wrong (P2#25: 13 opened, 0 determined, over two seasons). Only P3's two figures are contradicted (P3#17, #18), over eight seasons. Both proposals quote the zero from PROBE §3, so the origin is the probe's horizon, not either proposal.

`[UNVERIFIED]` The reports disagree on whether a refused act is silent: P2 S4 says a refused act emits nothing; P3 S6 says `determine` emits `determine.refused`. They may differ by refusal site (the S27.4 gate against the determine write); not checked.

`[ASSUMPTION: E-rows rest on real runs — each report labels its results real or model; this pass re-ran none of them and re-opened only the four sites listed at the head]`
