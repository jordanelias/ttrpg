# Workplan v12 — part 41: Batch B38-narrative-regimes, second half (handles from `B38.51`: `20_NARRATIVE_D`'s later commits through `U5d_SE_cohort_heavy_moves_and_caste` and `IS-B3-SE-02`; the Readings block; `B38.99`; the boundary row)

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree of branch `ccr-62958c70-0kjhsw`, read 2026-11-12; author lane A41 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B36 and this batch's first half will leave it; a symbol that does not exist in today's tree names the batch or item that makes it (DEPENDS ON). Symbols opened at this read (`grep -n` at the tree): `loop/resolve.py::_conviction_crisis`, `harness/populated.py::seat_cohorts`, `queries/world_q.py::vacancies`, `::questions_for`, `::_eras`, `::open_era`, `::_links`, `::_attach`, `::flows_in`, `::flows_known`, `::concluded_known`, `::engaged_poles`, `::opinion_of`, `::propositions_heard`, `::incompatible_span`, `::flow_capacity`, `::attention_key`, `::endings_reached`, `::side_against`, `::_concluded`, `::_content_matter`, `::faction_holding`, `::governing_hold`, `::check_strife_openers`, `::_stamped`, `CONTENT_OPENING_KINDS`, `CONCLUDING_KINDS`, `REALM_KIND`, `harness/loops.py::DECLARED_CYCLES`, `harness/strife.py::strands_block`, `LINK_WINDOW`, `harness/storybar.py::ARMS`, `::fork`, `::draw_seed_arm`, `harness/chronicle.py::lines`, `::consequence_chains`, `harness/corpus_run.py::attempts`, `state/gate.py::may_claim`, `TENURE_CLOSED`, `decision/options.py` (`withheld_verbs`), `state/carriers.py::is_cohort`, `::subject_of`, `data/verbs.py::DEED_KINDS`, `EVENT_KINDS`, `data/rosters.py::DEGREE_STEP`, `HEAD_SEAT`, `queries/person_q.py::regard`, `::stability`, `::legitimacy`, `::conviction_stand`, `::recent_claims`, `::opinion_terms`, `UNREST_KINDS`, `data/affiliations.py::conviction_map`, `data/cast.py::STANCE_MAX`, `engine/dice_engine/sigma_leverage.py::LEVEL_SIGMA`, `::net_boost`, `::levels_to_net_sigma`, `::roll_net_continuous`, `decision/questions.py::assemble`, `data/goals.py::_axis`, `references/descriptor_registry.yaml: affiliation_roster`. Absent at this read and made earlier in v12: `person_q.link_fit`, `world_q.circle_of`, `OPINION_LINKS`, `REGIME_CORES`, `FACTION_CREED`, `round_half_up` (this batch's first half: `30_WR_G`, `31_WR_A`), `pool_of` (`B04.24`), `null_scenes` (`B02.20`), `decision/sheet.py::Situation`, `::account`, `engine/season/tests/test_play_surface.py` (B34), `engine/season/harness/valley.py` (B12c), `engine/season/boot/realm.py` (B03c).

**What this part holds.** The second half of the one batch `B38-narrative-regimes` (lane WR), whose head (the batch block's first lines, its `GATE: Batch` lines, `REQUIREMENT`, `BATCH GATE`, the first half's dials) and first-half items are in another part, cited here by handle only. This part writes: the batch block's second-half lines (its dials, ids, the re-pin, its share of `C(B38)`, the serial edges of the whole batch, the estimate, its `UNDECIDED` list), the position table rows `B38.51` to `B38.99`, every item in full, the `## Readings` block, `B38.99` (re-pin and close readings, `V12_STRUCTURE_part4.md` E-1) and the boundary row. Landing order is U3 §1 item 38's, from "`20_NARRATIVE_D`'s later commits", corrected where a member's own `Lands in batch:` line, U3 §1.2's B38 row or `unified/U3_CONFLICT_LEDGER.md` C3-K7 (the serial order on `harness/storybar.py`) fixes it: `20_NARRATIVE_D` edits 3–4 → `31_WR_B` commits 1–2 → `30_WR_A` (with `09_WR_B_draws_not_thresholds` edit 4, the weather's era part, A-103's corrected row) → `30_WR_C` → `23_STORY_A` → `30_WR_D` commit 2 → `30_WR_E` → `IS-B3-FA-03` (a reading) → `31_WR_B` commit 3 (C3-K7: after `30_WR_E`) → `30_GO_F` with `IS-B3-GO-04` → `31_WR_C` (C3-K7: its storybar commit after `31_WR_B` commit 3) → `U5d_SE_cohort_heavy_moves_and_caste` → `IS-B3-SE-02` last. Two positions land at the batch's open, before the first half's `B38.01` (D-18, D-19): `B38.51` (the `riot` row's design) and `B38.52` (the goal rows' `axis:` content); the head's position table lists them first.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98). Armies: army, unit, army formation, unit formation; no size words (A-99, the MB lexicon). A *lap* is one pass of the season's scene budget and a *round* is one engagement of a fight (A-101); a fight's riposte is `finalblow_riposte` in code. Every source here was written before `PCR-4` (`B04.01`) and says `round` for the season's pass: the copied text keeps the source's word and each item says `NAMES:`. An *affiliation* is a thing a person may stand for; a *creed* is a faction's declared affiliations; a *regime* is a body of persons who stand for the same affiliations (glossary). The one acted on by a contested act is its *counterparty*; the person a verdict serves is the *beneficiary* (glossary *party*).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `S/` is `engine/season/`. A path under `engine/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. The builder is `S/boot/realm.py` after B03c (`CI-07`); the sources say `harness/populated.py`.

**Hash, read at the tree.** `World.content_hash()` (`S/state/world.py`) folds `_STATE_COLLECTIONS` (`persons`, `rungs`, `offices`, `sites`, `records`, `propositions`, `dates`), `_STATE_SEQUENCES` (`docket`), `tenures` and the log; `Era`, `Strand`, `Move` (`queries/world_q.py`, `NamedTuple`s computed per reading), `_Chain`, `View` and `Question` (built per deliberation) and `Fixtures` are not stored in any of them. So the fields this half adds to `Era`, `Strand`, `_Chain` and `View` are not encoding movers (D-04 reaches a *hashed* carrier only). No item of this half adds, removes or renames a field of a stored carrier.

---

## Batch B38-narrative-regimes, continued: the block's second-half lines

<!-- A41 block lines -->

### Position table, second half (rows `B38.51` to `B38.99`; the head's table carries the first half's rows; `B38.51` and `B38.52` are listed first there)

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B38.51 | the `riot` row's design | `U5d_SE_cohort_heavy_moves_and_caste` edit 3 (D-18) | DESIGN-FIRST | EQUAL | Batch B36 (lands at the batch's open, before B38.01) |
| B38.52 | the goal rows' `axis:` values, drafted and landed | U4 §3.4 DEP-NOCARRIER for `31_WR_C`; `V12_STRUCTURE_part2.md` §5.7 (D-19) | CONTENT | EQUAL | Batch B36 (lands at the batch's open, after B38.51) |
| B38.53 | a member who thinks ill of his own side finds its creed among his occasions | `20_NARRATIVE_D` edit 3 | BUILD | EQUAL | the first half's `20_NARRATIVE_D` commit 1 and `31_WR_A` commit 4 |
| B38.54 | leaving a creed or a head seat is a move of the era (A-46, narrow) | `20_NARRATIVE_D` edit 4 | POINTER (`B12a.05`) | — | Batch B12c |
| B38.55 | the sway draw at RESOLVE, dial at zero | `31_WR_B` commit 1 (A-92) | BUILD | EQUAL (`sway_gain` 0) | B38.53; the first half's `30_WR_G` commit 5, `31_WR_A` commits 1–4 |
| B38.56 | cohorts may take their holder's regime core at build, switch off | `31_WR_B` commit 2 | BUILD | EQUAL (`cohort_convictions` False) | B38.55 |
| B38.57 | the era: who rules and whether the realm is troubled; the turn rule | `30_WR_A` commit 1 (A-84, A-86) | BUILD | EQUAL | B38.56 |
| B38.58 | what a person believes the era to be | `30_WR_A` commit 2 | BUILD | EQUAL | B38.57; the first half's `20_NARRATIVE_C` commits 1–2 |
| B38.59 | the era's named conditions, each read as its emitter exists; A-103's row | `30_WR_A` commit 4 with the weather's era part (`dearth`) | BUILD | EQUAL | B38.57 |
| B38.60 | a strand concludes on its closing move's drawn degree | `09_WR_B_draws_not_thresholds` edit 4 | BUILD | MOVER(behaviour) | B38.59; Batch B07, Batch B12c |
| B38.61 | a vacant head seat is a mandatory question for those who may claim it, switch off | `30_WR_A` commit 3 (A-47) | BUILD | EQUAL (`era_mandatory_vacancy` False) | B38.57; Batch B10, Batch B21 |
| B38.62 | a strand is about its subject and its recent moves, switch at `all` | `30_WR_C` commit 1a | BUILD | EQUAL | B38.60 |
| B38.63 | the bounded link rule is flipped on | `30_WR_C` commit 1b | BUILD | MOVER(behaviour) | B38.62 |
| B38.64 | a strand's state: open, concluded, dormant, revived | `30_WR_C` commit 2 | BUILD | EQUAL | B38.63 |
| B38.65 | how far below the bar a failure fell | `23_STORY_A` edit 1 | BUILD | EQUAL | B38.64; Batch B05 |
| B38.66 | a staked row pays its stake by degree; the stakes roster | `23_STORY_A` edit 2 | BUILD | EQUAL (`shortfall_scale` off, no row staked) | B38.65 |
| B38.67 | a contested outcome is witnessed as done to its counterparty | `23_STORY_A` edit 3 | BUILD | MOVER(behaviour) | B38.66; Batch B11 |
| B38.68 | the attempts reader and the chronicle's six words | `23_STORY_A` edits 4–5 | BUILD | EQUAL | B38.67 |
| B38.69 | the estimate window and the renewed tie in `dues_unmet` | `30_WR_D` commit 1 | POINTER (the first half's `20_NARRATIVE_B` first commit) | — | — |
| B38.70 | nine feedback paths declared as LOOP rows | `30_WR_D` commit 2 | BUILD | EQUAL | B38.68; Batch B11F2 (CR-98's rows) |
| B38.71 | the cascade census: entrenched arm, fork lift, shapes E-01 to E-13, clauses C7 to C13 | `30_WR_E` | BUILD | EQUAL | B38.70; Batch B36 |
| B38.72 | a held seat still moves the spine (A-80) | `IS-B3-FA-03` | READING (R-1) | — | B38.71; Batch B21 |
| B38.73 | the cause gathers: LOOP row L17 and the regime gap words | `31_WR_B` commit 3 | BUILD | EQUAL | B38.71 |
| B38.74 | the `View` carries what the surfaces read | `30_GO_F` instruction 1 | BUILD | EQUAL | B38.73; Batch B34 |
| B38.75 | the marker, the stories, the portents, the recap, the added fields, standing to another | `30_GO_F` instructions 2–4 | BUILD | EQUAL | B38.74; B38.58, B38.62 |
| B38.76 | the names table and the chronicle's era, story and what an act left | `30_GO_F` instructions 5, 7 | BUILD | EQUAL | B38.75 |
| B38.77 | the end reveal, gated on the run's ending | `30_GO_F` instruction 6 with `IS-B3-GO-04` | BUILD | EQUAL | B38.76; Batch B34 |
| B38.78 | a voter's opinion of the claimant's side is one step in his draw | `31_WR_C` commit 1 | BUILD (SITE: B32's tables read first) | MOVER(behaviour), or none if B32 carried it | B38.77; Batch B32 |
| B38.79 | which affiliations a matter's thrust speaks to | `31_WR_C` commit 2 | BUILD | EQUAL | B38.78; B38.52 |
| B38.80 | which affiliations a strand's sides divide on; a body's lean | `31_WR_C` commit 3 | BUILD | EQUAL | B38.79; B38.73 |
| B38.81 | a stand in words, never a number | `31_WR_C` commit 4 | BUILD | EQUAL | B38.80 |
| B38.82 | the common people's heavy moves, as a roster | `U5d_SE` edit 1 (A-56) | BUILD | EQUAL | B38.81 |
| B38.83 | a cohort forms only those moves, switch off | `U5d_SE` edit 2 | BUILD | EQUAL (`cohort_moves_on` False) | B38.82 |
| B38.84 | the `riot` row | `U5d_SE` edit 3 | BUILD | MOVER(behaviour) | B38.83; B38.51 (HELD if B38.51 ended STOPPED) |
| B38.85 | caste practice tiers what a heritage earns, holds and is heard on, at 1.0 | `U5d_SE` edit 4 (A-41) | BUILD | EQUAL | B38.84 |
| B38.86 | vote blocks | `U5d_SE` edit 5 | POINTER (Batch B21: `U5d_FA_owed_edits` §4) | — | — |
| B38.87 | farm work | `U5d_SE` edit 6 (D-68) | POINTER (Batch B12c: CP-T08-01) | — | — |
| B38.88 | the heavy-move restriction is switched on | `U5d_SE` edit 2's flip | BUILD | MOVER(behaviour) | B38.85 |
| B38.89 | a hoarding steward is answered: the valley's A-80 reading | `IS-B3-SE-02` | BUILD (a test) | EQUAL | B38.88; Batch B12c |
| B38.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | every position of both halves |

<!-- A41 append point -->
