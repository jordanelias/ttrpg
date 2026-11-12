# Workplan v12 — part 43: batch B40-inst-scenarios

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `9c2c3ab` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A43 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B39 will leave it; a symbol that does not exist at `9c2c3ab` names the batch and source that makes it.

**What this part holds.** One batch of the FA lane, `B40-inst-scenarios`: the institutions' playables (the integrated scenario "The King's Bill" and the four families' standalones on FA's one runner, read by one report) and the four grounding plans' items that land here. Its members are U3 §1 item 40, in U3 §1.2's order: `15_INSTITUTIONS_SYNTHESIS_D` → `_BYZANTINE_F` → `_COLONIAL_E` → `_PAPACY_F` → `_BYZANTINE_grounding_mechanisms` → `_VENICE_grounding_E` → `_COLONIAL_grounding_F` → `_PAPACY_grounding_mechanisms` → `_SYNTHESIS_E`. No intake entry and no instruction item names B40 (`grep -n B40` over `master/eval/V12_INTAKE.md` finds only the edges B21b → B40 and B21c → B40; over `master/instructions/` only milestone and edge rows). A part cites another part's batch or item by handle only; the head's index maps a handle to its file.

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `proposals/<file>` is under that directory's `proposals/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`. A path under `engine/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. Short names for the members: SYN-D, BYZ-F, COL-E, PAP-F, BYZ-G, VEN-E, COL-F, PAP-G, SYN-E; for their kit sources (B32, B33): SYN-A, SYN-B, COL-A to COL-D, VEN-A to VEN-D, BYZ-A to BYZ-E, PAP-A to PAP-E.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers are an attribute, a skill and its skill score (A-98); the tree's `capability` identifiers keep their names. A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); nothing in this batch uses either. Copied source text is corrected where a later ruling retired its word, and the correction is said at the item: "fisc" → *treasury* (U4d; the report line is `treasury`), "obligee" → *sworn man*, `remove` → `distance` (D-U1-11k), a hired captain's "company" → *his men* (the MB lexicon: no size word), a chartered trading "company" → *chartered body*.

---

## Batch B40-inst-scenarios · lane FA · wave W22 · step S22 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B40-inst-scenarios
IN-FLIGHT ROW: registers/handoffs/HANDOFF_FA.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B21-fa-governance
GATE: Batch B21b-fa-war
GATE: Batch B21c-fa-seats
GATE: Batch B32-inst-kit
GATE: Batch B33-inst-economy-hands
GATE: Batch B39-procgen-and-cases
REQUIREMENT: every conjunct of R-01 to R-09, re-read on B40's closing tree (M5 closes here, `V12_STRUCTURE.md` §3; IS-A §12.1, M5 row: "all nine at B40") → all nine hold; no `status:` is edited (A-114: the one re-take that may move a row is B99). No row is moved by this batch's own items; what they serve is A-12, A-13, A-14, A-80 and the standing requirement that each subsystem plays alone (IS-A §12.1, the note under the milestone table: "A-12, A-13, A-14 (B32, B33, B40) … the standing requirement that each subsystem plays alone (B18, B27, B40)").
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; nothing past two seasons, D-17):
  `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines, each row's conjuncts read and holding (the M5 reading; a conjunct that does not hold is quoted with its tree, and the close is not failed by it: no item here targets one, so the reading is recorded for B98 and B99, `V12_STRUCTURE.md` §3);
  `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2 → the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines quoted before (`reading @<B39 close sha>`) and after; every verb built out at B39's close still built out (no verb row is edited here);
  `python -m pytest engine/season/tests/test_instruments.py engine/season/tests/test_inst_byz_g.py engine/season/tests/test_inst_ven_e.py engine/season/tests/test_inst_col_f.py engine/season/tests/test_inst_pap_g.py engine/season/tests/test_governance_spine_play.py engine/season/tests/test_case_on_the_realm.py -q` → all pass (`test_instruments.py` is U3 §1.3's B40 instrument, created in B32; the next four are created in this batch; the last two are B21's and B39's, re-run because B40.01 edits the runner and the case builder);
  B40.03's SYN-D gates 1 to 6 and 8 at two seasons, quoted with their controls (U3 §1.3 names no gate sentence for item 40; the batch gate is the union of the members' gates, `V12_STRUCTURE.md` §2.5), and SYN-E's whole-plan reading (B40.28);
  the realm content hash at seeds 0, 1, 2, one season → the values B40.99 re-pins; every hash-EQUAL item's control held (B40.01 to B40.11, B40.21, B40.26, B40.27);
  `python tools/export_composition.py --check` → exit 0 and `python tools/ci_sim_fabrication_check.py` → exit 0 (B40.02 adds a harness module; no new fixture);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits registries and `queries/`: the full gates, CLAUDE.md §0.4);
  the glossary rows the items name (*scenario*, *case*, *sworn*, *treasury*), read against the code they landed (STAGES "The glossary always matches" rule 2): a mismatch fails the close;
  "the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited" (`IS-A-12`).
RE-PIN: once, in B40.99's commit: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) at seeds 0 to 2 and the NPC-088 headless hash, read against B39's close (`reading @<sha>`); the commit says "re-pin: B40, behaviour movers B40.12, B40.14 to B40.20, B40.22 to B40.25 (content rows the realm builds: exit-audit keys, paired officers, seeded capitulations and commissions, the secretary order, the condotta form, the guild bench, the brotherhood, the clause keys `stage`, `after`, `over: any`, the wardship keep, the farm's `hardens`); the scenarios and the report move nothing".
IDS: ED-FA 0; H 0 (no item writes a ledger or hole-register row; B40.13's missing carrier goes to the receipt, `V12_STRUCTURE_part2.md` §5.7)
DIALS AT CONTROL: none (no setting ships at a control value; the `[ASSUMPTION]` amounts with sweeps in B40.03 to B40.08, B40.14 to B40.25 are authored values listed in the PR body for Jordan's correction at the merge, D-19, not settings)
C(B40-inst-scenarios): this batch's entries; the plan's head parts;
  `engine/season/harness/governance_spine.py` (`situation`, `situated`, `play`, `ending`, `digest`, `offered`, `loop_closed`: B21.72, B21.74, B21.76); `engine/season/harness/scenarios.py` (`SCENARIOS`, `run`, `Scenario`, `ENDING_KINDS`: B11, `IS-B2-CORE-01`, `IS-B3-GO-01`); `engine/season/harness/corpus_run.py` (`build_case`, the closed set of `setup` keys, the prehistory fold: B39, `12_ARCS_case_on_the_realm`); `engine/season/harness/storybar.py` (the `--pin-rolls` wrapper, B36, `23_STORY_D` edit 3; read only); `engine/season/harness/strife.py` (the report's kind; read only); `engine/season/harness/populated.py::run`; `engine/season/boot/realm.py::build_realm` (B03c); `engine/season/harness/headless.py`, `play_surface.py`; NEW `engine/season/harness/institution.py`; `engine/season/cases/exercises/` (NEW `INST-01.yaml`, `INST-BYZ-ROGA.yaml`, `INST-BYZ-CHANCERY.yaml`, `INST-COLONIAL-01.yaml`, `INST-COLONIAL-02.yaml`, `INST-PAPACY-01.yaml`; B33's `INST-VENICE-01.yaml`);
  `engine/season/offices.yaml`; `engine/season/rosters.yaml` (`office_bodies`, `tables.cooling_off`, `tables.eligible_from`, `tables.alignment`); `engine/season/arrangements.yaml` (`audit`, `debt_suit`, `conclave`, `inquisition_hearing`, `excommunication_deliberation`); `engine/season/instruments.yaml` (`forms`, `seeded`: B32); `engine/season/data/instruments.py` (B32); `engine/season/goals.yaml`, `engine/season/data/goals.py` (read: B40.13); `engine/season/queries/world_q.py` (`dues`, `clauses_binding`, `breaches`, `owed`, `audits_due`, `distance`, `establishment_of`, `endings_reached`); `engine/season/queries/person_q.py` (`kept`, `deeds_judged`, `legitimacy`); `engine/season/state/attribution.py` (`causing_act`, `actor_of`); `engine/season/state/carriers.py` (`Record.stages`, `Act.via`); `engine/season/loop/effects_information.py` (`_mint_document`); `engine/season/state/gate.py` (read: `purview_reaches`, `may_fill`; `judging_set` if B24 or B27 added it);
  the tests named in the items; instruments: `aperture`, `register`, `headless`, `storybar`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/export_composition.py`, `tools/ci_sim_fabrication_check.py`; `engine/season/tests/_realm_goldens.py`;
  read whole by the producer before B40.01: `proposals/15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1 to §3 (the case shape and the report are copied below; the file is the one place the three cuts' prose lives);
  the closing SHAs of B00, B01, B02, B12c, B21, B21b, B21c, B32, B33, B39 (and of B11, B21d, B24, B24a, B36, which close earlier in the schedule and are named by DEPENDS ON lines); the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_FA.md`, the skill and `methodology-close`).
PARALLEL: S22, alone in the plan (`V12_STRUCTURE.md` §2.3: S20 B38, S21 B39, S22 B40, S23 B98). No sibling; no merge position.
BACKGROUND RUN: the 200-seed arms (B40.04 gate 4's `--bands 200`, B40.08's 200-seed Confessor arm, B40.12's 200-seed exit-audit arm, B40.26's three 200-seed arms) are each sized on two small runs (seeds 0–1, then 0–3, at two seasons) at the batch's open, after B40.02 lands, launched in the background (`exec python -u … > log 2>&1`, the skill's CHECKPOINTS AND BASELINES), and read at their item's gate; each item's commit body records the wall time and worker count.
COST: small builds (one harness module, the runner's case reading, six case files) and content edits (registry rows), two clause-key builds (`stage`, `after`); producer `valoria-author` on `sonnet`, `high` (each member's own tier, R4 7b.0); `opus` reads SYN-D gates 1–3 and 8, BYZ-F gate 4's band table, COL-E gates 1–3 and 6, PAP-F's 200-seed arms, BYZ-G item 1's band table, VEN-E gates 2 and 4, COL-F gate 6, PAP-G item 5's arms, and B40.28.
EST: 16 h [estimate: `V12_STRUCTURE.md` §2.4's formula over this batch's 29 positions (0.4 h × 29 + 2.5 h for the close + 2 h for the 200-seed arms); §2.2's 6 h counted the nine members, not the commits they order (E-15)]

UNDECIDED (each reading taken is the one that changes less, `V12_STRUCTURE_part2.md` §5.1; for the receipt and H2):
  (U1) **B40's hash.** `V12_STRUCTURE.md` §2.2 and U3 §2.1 read B40 "EQUAL (0 of 9)"; the four grounding plans each say "EQUAL" only with their rows *absent* (U3 §3.1: "EQUAL absent", "EQUAL with rows absent"), and VEN-E says it outright: "With every row of this batch absent, nothing … With the rows present: one more form … content rows in `offices.yaml`, `rosters.yaml: office_bodies` and `arrangements.yaml`". Rows the realm builds move the realm's content hash. Taken: B40 is a behaviour mover with one re-pin (B40.99); H2's hash-mover table and §7.1 item 7's list of hash-EQUAL batches change. Whether a new optional clause key (`stage`, `after`, `within`) is an *encoding* mover (D-04) depends on whether `data/instruments.py`'s clause type is a dataclass `World.content_hash()` reaches; B40.18 and B40.22 open it first and declare which.
  (U2) **The edge B21d → B40.** PAP-F depends on CR-88's vacancy duty ("until it lands the case plants the question, never the outcome"); CR-88 is B21d's (the intake `:280`). B21d is not in B40's `after` list and not before it transitively (no batch between them names B21d). It closes at S15, before S22, so the schedule meets it; the graph does not. Taken: no `GATE: Batch B21d` line (the gate list is §2.1's); B40.08 carries the source's own fallback as a `STOPS IF`-free branch. For H2: adding B21d → B40 points forward (W14 → W22) and makes no cycle.
  (U3) **A third case base.** `12_ARCS_case_on_the_realm` (B39): "`base: realm` … or `base: template` … One builder per base; no third." SYN-D §1: "`base: realm | spine`". SYN-D is this batch's member and the later text; ARCS-01's rule is about not duplicating the cast. Taken: `build_case`'s `base` set gains `spine` (the spine fixture is an existing builder, `governance_spine.build`, not a third cast); the rule's sentence is not edited anywhere (a design document).
  (U4) **`setup.seats` against ARCS-01's `setup.offices`.** SYN-D's case shape has `seats:` ("`offices.yaml`-shaped rows the base lacks"); ARCS-01's closed set has `offices:` "as in CORE 02". One fact, one key: B40.01 opens the closed set at its turn and, if `offices:` takes `offices.yaml`-shaped rows, the case files write `offices:` where SYN-D writes `seats:` (said in each case item); otherwise `seats:` joins the closed set. `instruments:` and `stores:` join it either way; `seats_offered:` and `ends:` are top-level case keys.
  (U5) **Set-up under the pinned roll.** SYN-D: "Set-up acts resolve under the pinned roll, so the situation is the same at every seed." FA-P4's `situation` (B21.72, D-08): "a set-up act at tick 0 can come out otherwise … it reports the band its set-up act reached". Taken: a case file's `setup.prehistory` folds under the pin wrapper at `Success` (SYN-D, the member); FA-P4's four named situations stay unpinned and unedited ("FA-P4's three hand-written situations stay as they are").
  (U6) **A case as a row of the scenario registry.** `IS-B2-CORE-01` (4): "every later entry resolves names here and keeps no second mapping … `governance_spine play` keep[s] [its] command line and call[s] `run`"; B21.76 makes `play` call `scenarios.run` (or, under its `STOPS IF`, B23's first item does). A case id passed as `situation` must then be a `SCENARIOS` name, and `IS-B3-GO-01` refuses a row without `kinds` for every ending name. Taken: B40.01 registers one row per institutions case file, `kinds` mapping `no_seat` → `lost` (B21.76's `unseated`), every other ending → `drawn` (an institutional ending is a state of the world, not a win of every offered seat; `drawn` claims least; `IS-B3-GO-02` at B34 may split by the seat's side as it does `realm_ended`). If `play` still owns its loop at B40's base, the case id is resolved inside `situated` and no row is registered.
  (U7) **Where the case endings live.** SYN-D: "`ends: [<a Query name>]  # each a pure reader over Tenures and the log`", and "No file under `loop/`, `state/`, `queries/` … changes". BYZ-F edit 4: "Two end conditions, each a Query over Tenures, beside FA-P4's three". Taken: one mapping `CASE_ENDS` in `harness/governance_spine.py` beside B21.76's `ending`, filled by the case items in landing order.
  (U8) **Where BYZ-F's two endings land.** SYN-D (U3's first member) names `court_kept` and `court_lapsed` among INST-01's ends; BYZ-F edit 4 defines them. Taken: B40.03 defines them with BYZ-F edit 4's text and cites it; B40.04 uses them.
  (U9) **Endings SYN-D names and no file defines** (`bond_met`, `bond_lapsed`, `audit_determined`, `sentenced`, `no_seat`, `season_count`), and COL-E's and BYZ-F's chancery endings stated in prose: B40.03, B40.05 to B40.07 write each as a reader over the report line or ruling that names it, marked `[ASSUMPTION]`.
  (U10) **BYZ-G item 1's gate world.** "On the `roga` case file (proposal F) … plant a `revoke` of the treasurer"; `roga` is `base: spine` and the spine has no `off_lord_treasurer` (`governance_spine.yaml`'s rungs are `lr_*`; `grep -c off_ governance_spine.yaml` → 0). Taken: the gate runs on INST-01 (`base: realm`), whose base holds the three seats.
  (U11) **The Counting-House's gate.** VEN-D §5's case file is B33's (U3 places `15_INSTITUTIONS_VENICE_D` whole in B33), but its gate runs `harness/institution.py`, which B40.02 creates. By §5.8 that arm moves here: B40.09 (READING). If B33's author wrote the gate in B33 against a report that did not exist, the merge keeps one.
  (U12) **PAP-G item 5's form.** The source: "items 5 and 6 are runs of `harness/institution.py` quoted in the commit". Item 5's three gates need a planted second hearing, a concealed accuser and one case before two benches: folds, not scenario runs. Taken: a test file (`test_inst_pap_g.py`, `[ASSUMPTION: test name; the item creates it]`, E-3).
  (U13) **Endings past two seasons.** `roga`'s sworn terms mature in season 4 (BYZ-F edit 1); the farm's audit falls at its term; *the long vacancy* is three seasons empty (PAP-F). At two seasons (D-17) those endings cannot be reached. Taken (B21.74's precedent): each gate asserts what two seasons can show and reports the rest "against the source's span, not asserted (A-114: the longer reading is B99's)".
  (U14) **Hand-built folds and the two-season cap.** COL-F gates 2 and 3 set ticks `t + 4` and "six seasons" inside a hand-built test fold. Taken: D-17's cap binds season runs; a unit test that sets the world's tick runs no season and keeps the source's arithmetic (`[ASSUMPTION — basis: D-17 "No batch close before it runs past two seasons"; a fold over constructed ticks is not a run]`).
  (U15) **"Every contest resolves at its control band"** (the A-80 arm of SYN-D gate 8, BYZ-F gate 5, COL-E gate 6, PAP-F's last arm). No file defines the control band. Taken: the report's `--hold BAND` arm, through `23_STORY_D` edit 3's `--pin-rolls` wrapper (B36), with every gate passing `Failure` `[ASSUMPTION: the band at which a challenged position holds is Failure for the acting side — basis: SYN-D gate 8's own list, "no bond is met or sued, no levy is resisted or yielded beyond its control band, no audit is determined"]`.
  (U16) **Grouping (E-13).** SYN-D is three items (the runner, the report, the case), because its runner and report are read by every later case; BYZ-F edits 3 and 5 and COL-E's report table join SYN-D §3's report item (SYN-D: "edit 3's seven digest lines and edit 5's `bands=N` are lines and an option of the one report"); BYZ-F edit 4 joins B40.03 (U8); VEN-E edits 5 and 5b are one item (one form and the yard row it pays); COL-F edits 1, 6 and 8 are one item (one file, the report; one gate, 6).
  (U17) **PAP-F's player seat for the control arm** is the Crown's `confer`; the arm removes `tables.patronage`'s entry (PAP-B, B32). If B32 shipped the entry under another key, B40.08 opens it and writes the arm against what it finds.

Not in this batch, and where each is (each member's parts are dispositioned once, check 6): PAP-G item 1 (B32, with PAP-B), items 2, 3 (B33, with PAP-D), item 4 (B33, with PAP-E) — its own implementation block; PAP-G item 7 (the Crown's objection: "Design-first … nothing to build now … the SC lane's") and item 8 ("Content notes and referents (no edit)"): named non-carry, nothing executes; BYZ-G item 5 ("Design-first notes carried into batch G (nothing to build now)"): named non-carry, SYN-E's I-10 holds batch G; COL-F edit 7 ("No engine edit"; closed by A-41 and the synthesis): named non-carry; SYN-E's I-1 to I-8 (B32, B33, B39, by its own mapping) and I-10 (held design-first: schism, the kin-bar, unanimity, batch G): no item here, SYN-E "lands nothing"; VEN-D edits 1 to 4 (B33); VEN-D edit 5's readings: carried by B40.02's `bonds` and `lists` lines (SYN-D §3: "from which family reading … VEN-D").

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B40.01 | a case file is a scenario FA's runner plays | SYN-D §1 (the runner) | BUILD | EQUAL | Batch B39, Batch B21 |
| B40.02 | one report for every institution | SYN-D §1, §3 (the report); BYZ-F edits 3, 5; COL-E "The report" | BUILD | EQUAL | B40.01 |
| B40.03 | "The King's Bill", the integrated scenario, and its eight endings | SYN-D §2, gates 1–8; BYZ-F edit 4 | BUILD | EQUAL | B40.02; Batch B32, Batch B33 |
| B40.04 | `roga`: a court that cannot pay | BYZ-F edit 1, gates 1, 3, 4, 5 | BUILD | EQUAL | B40.03 |
| B40.05 | `chancery`: papers waiting in a hand | BYZ-F edit 2, gate 2 | BUILD | EQUAL | B40.04 |
| B40.06 | The Farm of the Southern Tolls | COL-E scenario 1, gates 1–6 | BUILD | EQUAL | B40.03; Batch B12c |
| B40.07 | The Katepano's Latitude | COL-E scenario 2 | BUILD | EQUAL | B40.06; Batch B21b |
| B40.08 | The Vacant Chair | PAP-F edits 1–3, gate | BUILD | EQUAL | B40.02; Batch B21 |
| B40.09 | The Counting-House read on the one report | VEN-D §5's gate (moved, §5.8) | READING | — | B40.02; Batch B33 |
| B40.10 | five readings of the court in the report | BYZ-G item 3 | BUILD | EQUAL | B40.04, B40.05 |
| B40.11 | an entered paper is a precedent file | BYZ-G item 4 | BUILD | EQUAL | Batch B33 |
| B40.12 | an exit audit on the seats that hold money or a frontier | BYZ-G item 1 | BUILD | MOVER(behaviour) | B40.03; Batch B33 |
| B40.13 | the treaty gate breeds its own offence | BYZ-G item 2 | BLOCKED (v12: a carrier is owed: the place-filtered `deed_doers` form in `data/goals.py`) | — | — |
| B40.14 | paired officers, near and far | VEN-E edit 1 | BUILD | MOVER(behaviour) | Batch B33 |
| B40.15 | the submission pact | VEN-E edit 2 | BUILD | MOVER(behaviour) | Batch B32 |
| B40.16 | the appointer answers: the audit's recital | VEN-E edit 3 | BUILD | MOVER(behaviour) | Batch B33 |
| B40.17 | the secretary order and the standing report | VEN-E edit 4 | BUILD | MOVER(behaviour) | B40.14 |
| B40.18 | the contract in phases; the yard's wage | VEN-E edits 5, 5b | BUILD | MOVER(behaviour) | Batch B32 |
| B40.19 | the pledge; the merchants' court | VEN-E edit 6 | BUILD | MOVER(behaviour) | B40.14; Batch B33 |
| B40.20 | the outside assent; the brotherhood | VEN-E edit 7 | BUILD | MOVER(behaviour) | B40.14 |
| B40.21 | the bearer, the declared figure, near and far, six stories | COL-F edits 1, 6, 8 | BUILD | EQUAL | B40.06, B40.14 |
| B40.22 | the lord's reward | COL-F edit 2 | BUILD | MOVER(behaviour) | B40.21 |
| B40.23 | the hostage's keep | COL-F edit 3 | BUILD | MOVER(behaviour) | B40.22 |
| B40.24 | the farm hardens | COL-F edit 4 | BUILD | MOVER(behaviour) | Batch B33 |
| B40.25 | the commission forbears war and treaty | COL-F edit 5 | BUILD | MOVER(behaviour) | B40.22 |
| B40.26 | three Church gates that need no edit | PAP-G item 5 | BUILD | EQUAL | Batch B33, Batch B24a |
| B40.27 | seven Church readings in the report | PAP-G item 6 | BUILD | EQUAL | B40.08 |
| B40.28 | the institutions plan's whole gate | SYN-E "Gate for the plan as a whole" | READING | — | B40.03 to B40.27 |
| B40.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B40.01 to B40.28 |

### B40.01 — a case file is a scenario FA's runner plays · SYN-D §1 (the runner) · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` "The resolution, decided" §1 (the case shape; "The runner is FA's"), "What it changes"; rulings A-10, A-12, A-14 (its first `Reconciled:` line); C3-C12; closes audit X-32 ("The four families state a scenario four ways").
- ADVANCES: none of the nine; the standing requirement (one scenario style, one runner, one code path) for the four institutions.
- INSTRUCTION:
  1. Site (§5.7 SITE): open `harness/corpus_run.py::build_case` (B39), its closed set of `setup` keys and its prehistory fold; open `harness/governance_spine.py::play`, `situated`, `situation` and `harness/scenarios.py::SCENARIOS` (B21.72, B21.76, B11). Record in the commit body: the closed set as found; whether `play` calls `scenarios.run` (B21.76 built) or still owns its loop (B21.76's `STOPS IF` fired and B23's first item carried it); whether `setup.offices` takes `offices.yaml`-shaped rows (U4).
  2. The case shape (SYN-D §1, copied): "The situation is a case file under `engine/season/cases/exercises/`, in ARCS-01's delta shape:
     ```yaml
     id:    <case id>
     base:  realm | spine            # an existing builder: populated.build_realm, governance_spine.build
     setup:
       seats:        [<offices.yaml-shaped rows the base lacks>]
       instruments:  [<instruments.yaml `seeded:`-shaped rows>]
       stores:       {<rung id>: {<matter kind>: <units>}}
       prehistory:   [{actor, verb, subject, ...}]     # folded through the real RESOLVE and WITNESS at tick 0
     seats_offered:  [<seat ids a player-proxy may take>]
     ends:           [<a Query name>]                    # each a pure reader over Tenures and the log
     span_seasons:   <int>
     ```
     A set-up act the fold refuses fails the build, naming the refusal (ARCS-01). Set-up acts resolve under the pinned roll, so the situation is the same at every seed; play is unpinned. A scenario may not pre-write its own ending: the loader refuses a prehistory act whose row writes a field an `ends` Query reads as terminal (ARCS-01's falsifier)." In `build_case`: `base` gains `spine` → `governance_spine.build(seed)` beside `realm` → `build_realm(seed)` (U3; `populated.build_realm` is `boot/realm.py::build_realm` after B03c); `instruments:` (applied through SYN-A's `seeded:` pass, the kit's one constructor, B32) and `stores:` (added to `Rung.stores` in `default_store_kind`'s shape, X-30) join the closed set; `seats:` is written `offices:` if step 1 found that key takes the same rows, else joins the set (U4); `seats_offered:` and `ends:` are top-level keys the loader validates (every seat id in `w.offices` after the delta; every `ends` name a key of `CASE_ENDS`). `setup.prehistory` folds under `23_STORY_D` edit 3's `--pin-rolls` wrapper at `Success`, imported from `harness/storybar.py`, not re-written (U5).
  3. "The runner is FA's. `harness/governance_spine.py::play(seed, seasons, situation, player, pick=None, world=…)` takes a case id as its `situation`; `situation()` builds the case's base and applies the delta. FA-P4's three hand-written situations stay as they are; nothing is added to that function for an institution." With B21.76 built, the case is reached through `situated(seed, <case id>)`, which calls `build_case` when `<case id>` names a file under `cases/exercises/` and the B21.72 table otherwise; `CASE_ENDS: dict[str, Callable]` is added beside `ending` (U7), empty here, each later case item filling the names it uses.
  4. One `SCENARIOS` row per institutions case file (U6), registered by a loop over `cases/exercises/INST-*.yaml` at import: `build = lambda seed, cid=cid: governance_spine.situated(seed, cid)`, `verbs = None`, `seat` the first id of `seats_offered`'s holder, `ending` the first of the case's `ends` that reads true, `role = None` (A-10: governance is the loop's own verbs), `kinds = {"no_seat": "lost", <every other name>: "drawn"}`, `unreached` read at landing as B21.76 (4) states, at two seasons. If step 1 found that `play` owns its loop, no row is registered and `situated` resolves the case id.
  5. Glossary: row *scenario* gains "an institutions scenario is a case file under `cases/exercises/` played by FA's runner"; row *case* (if absent): "case: a delta on an existing world (its base), with the acts that made it, as a legal case file states what is at issue".
- WHERE: `engine/season/harness/corpus_run.py` (`build_case`: the `spine` base, the closed set); `engine/season/harness/governance_spine.py` (`situated`, NEW `CASE_ENDS`, `play`'s situation lookup); `engine/season/harness/scenarios.py` (the institutions rows); `engine/season/tests/test_governance_spine_play.py`, `engine/season/tests/test_case_on_the_realm.py` (tests added); `unified/U1_GLOSSARY.md` (*scenario*, *case*).
- TESTS: written first, red (no `spine` base, no case lookup): in `test_case_on_the_realm.py`, `test_a_spine_case_builds_on_the_spine` and `test_a_case_stores_key_adds_to_the_named_rung` `[ASSUMPTION: test names; the item creates them]`; in `test_governance_spine_play.py`, `test_a_case_id_situation_reproduces_populated_run_after_the_same_tick0_acts` (SYN-D's control) and `test_a_refused_prehistory_act_stops_the_build_naming_it` `[ASSUMPTION: test names]`. B39's `test_a_setup_key_outside_the_closed_set_is_refused` and `test_a_prehistory_act_that_writes_a_terminal_beat_is_refused` stay green with the widened set.
- FALSIFIER and CONTROL: "A scenario whose opening state the fold could not produce (a set-up act refused)" builds; "The scenario needing any act the season loop cannot form" (SYN-D Falsifier). Control: "a run's `content_hash` equals the same seasons through `populated.run` with the same chooser on the same world after the same tick-0 acts (FA-P4's control)"; the realm hash at seed 0, one season, equal to B39's close (no case is built by `build_realm`).
- GATE: `python -m pytest engine/season/tests/test_case_on_the_realm.py engine/season/tests/test_governance_spine_play.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.scenarios season --seed 0 --seasons 2` → its hash equal to B39's reading (`reading @<sha>`).
- HASH MOVERS: none (harness).
- DEPENDS ON: V12 Batch B39 (`12_ARCS_case_on_the_realm`: `corpus_run.build_case`, the prehistory fold, the closed set); V12 B21.72, B21.74, B21.76 (`situation`, `play`, `world=`, `situated`, `ending`); V12 Batch B11 (`IS-B2-CORE-01`, `IS-B3-GO-01`: `SCENARIOS`, `kinds`); V12 Batch B36 (`23_STORY_D` edit 3: the `--pin-rolls` wrapper; closes before B40 through B38); V12 Batch B32 (SYN-A: the `seeded:` pass); EXISTS-IN-TREE `harness/governance_spine.py::build`, `harness/populated.py::run`, `engine/season/cases/exercises/`.
- GLOSSARY: *scenario*, *case* (step 5).
- NAMES: `populated.build_realm` → `boot/realm.py::build_realm` (B03c, CI-07); `populated.run` stays in `harness/populated.py`.
- COST and TIER: small build (harness); `sonnet`, `high`.
- LANDS IT: B40's `valoria-author` producer, `isolation: worktree`; `Item: B40.01`, `[skip ci]`.

### B40.02 — one report for every institution · SYN-D §1, §3 with BYZ-F edits 3, 5 and COL-E's report · BUILD · HASH EQUAL
- SOURCE: SYN-D "The resolution, decided" §1 ("The report is one module"), §3 "The report" (the table and `--bands N`); `proposals/15_INSTITUTIONS_BYZANTINE_F_playable_scenarios_and_reading.md` "Exact edits" 3 (the seven lines) and 5 (`--bands N`); `proposals/15_INSTITUTIONS_COLONIAL_E_scenario.md` "The report"; `proposals/15_INSTITUTIONS_VENICE_D_houses_charters_and_content.md` "Exact edits" 5 (its readings are rows of this report); C3-C12; closes VEN-D edit 5 (no `counting_house.py`).
- ADVANCES: none of the nine; the legibility half of the standing requirement for the four institutions; A-80's instrument for the four scenarios.
- INSTRUCTION:
  1. NEW `engine/season/harness/institution.py` (SYN-D §1, copied): "`python -m engine.season.harness.institution <case> <seasons> <seed> [--bands N]`, output to a path the caller gives. Read-only; `harness/strife.py`'s kind; no assertion that a story occurs; not a guard and not a standing corpus." The path is `--out PATH`, required `[ASSUMPTION: flag name; the source says only "a path the caller gives"]`. No default for seed or seasons (the file sits inside `tools/ci_sim_fabrication_check.py`'s scope, B21.72's precedent). It builds and runs the case through B40.01's `situated` and the one loop (`scenarios.run`, or `play` if it owns its loop), the shipped chooser in every seat unless a policy is named.
  2. The lines (SYN-D §3, copied): "One line per reading, each a fold over `w.log`, `w.tenures`, `w.records`, `Rung.stores` and, for the person-side readings, a named person's own ledger. A line whose subject does not exist in the world is omitted."

     | line | read from | from which family reading |
     |---|---|---|
     | `treasury` — stores, the bill due this year, the shortfall, per paying seat | `Rung.stores`; `upkeep_owed`; termed `oblige` edges | BYZ-F |
     | `sworn` — renewed, matured, live, per paying seat | `term.renewed`, `term.matured` | BYZ-F |
     | `collected` — rendered, taken, partial, resisted, per place, each with its term list | `requisition.*` Events | BYZ-F; COL-E |
     | `carried` — transfers between places by band and what arrived | `transfer.*` Events | COL-E |
     | `dignities` — held, conferred, resisted, provisional | `tenure.opened` on dignity rows; `appointment.resisted` | BYZ-F |
     | `hands` — entered, held over, returned by a clerk, returned by the clock, per body or seat; the busiest hand's share | `document.*` Events; "returned by the clock" read when read (an unentered `hand:` stage whose due has passed; BYZ-C as reconciled) | BYZ-F |
     | `instruments` — per live instrument: form, parties, `dues` stamped, acts occasioned by one, `kept` as each party reads it | `dues`; `occasioned_by`; `person_q.kept` | COL-E |
     | `bonds` — minted, reckoning by band, extended, lapsed, handed on; the largest share of a bench with a live edge to one person | `debt` Records; the lapse read from `world_q.owed` after the last stage's `term.matured` (VEN-B; no `debt.lapsed` kind); `record.given`; `owed_to` | VEN-D |
     | `lists` — per list seat: enrolled, lapsed by term; `lot.seen`, `lot.empty`; council holders in order | `oblige` Tenures; `lot.*` | VEN-D |
     | `seats` — per faction named: who holds which seat; each `confer`, `revoke`, `succeed` with its band, its `Act.via` and its term list | `tenure.*`; the contest Events | PAP-F; BYZ-F |
     | `certificates` — Records carrying `recites`, by keeper; tellings of recited deeds by keeper; the mean chain term of `legitimacy` per founding seat | `w.records`; `tell` Events citing a held Record; `person_q.legitimacy` over the cast | SYN-B gate 4 |
     | `sanctions` — sentences by band; writs published and their `force`; answers by band; releases by excused and unexcused men | `ban.opened`; `dispensation.issued` of form `avoidance` or `interdict`; `compliance.*`; `tenure.closed` on `oblige` | PAP-D |
     | `hearings` — per arrangement row: opened, by whom, bench, proofs weighed, band | `case.opened`; `determine` Events | COL-E; PAP-F |
     | `commensuration` — the roll routes used; bands seen per verb; term names seen; matter kinds moved; maturations on each of the two clocks | the Events' own records | audit §7.6 |
     | `conflicts` — the readings of audit §6, each as a count and the chain that made it | the folds named there | audit §6 |

     (SYN-D's first line reads `fisc`; it is `treasury`, the U4d rename, as BYZ-F edit 3's own example line is.) Added from BYZ-F edit 3, the one line SYN-D's table lacks: "`accession     claimed 0 · contested 0 · provisional 0 ;  recall  closed 0 · resisted 0`". The print form is BYZ-F's, e.g. "`treasury          <rung>: grain 2 · bill due this year 5 · shortfall 3     (default_store_kind)`", "`sworn         renewed 1 · matured 1 · live 3            (per paying seat)`".
  3. Added from COL-E "The report" (lines the table above does not already carry): "the establishment of the conferred seat against the grantor's local establishment" (`world_q.establishment_of`); "petitions filed naming the seat or its holder; residence changes out of the ground" (`petition.filed`, `residence.changed`); "levies attempted through the conferred seat, each with its band and term list" (Events of `requisition.*` with `Act.via` the seat), as `collected`'s per-seat split.
  4. `--bands N` (SYN-D §3 with BYZ-F edit 5): "runs the case at seeds `0..N-1` under the shipped chooser and prints, for each drawn verb, the frequency of each band beside the control (a task row under `task_draw_arm: off`; a contest row under the pinned roll). It asserts nothing." BYZ-F: "for each drawn verb (`confer`, `revoke`, `carry`, `requisition`, `succeed`)". "No test file is added for the report (CLAUDE.md §0.1 pt 5: its subject is the game's draws and its reader is a person deciding a tuning value)."
  5. Three arms every family gate reads, each an option of the one report: `--pin-rolls BAND` (the planted failure of SYN-D gate 5 and COL-E gate 5: every roll at `BAND`, through `23_STORY_D` edit 3's wrapper, imported); `--hold BAND` (the A-80 arm, U15: the same wrapper on contested draws only, with a per-seed, per-season line "the count of acts whose question cites an Event of the case's named party or an instrument of the case", read off each executed act's question referents through the reason trail; "The count is the story census's instrument (`23_STORY_D`, the entrenched-world arm); this gate reads it, it does not define it"); `--control` (SYN-D gate 4: the case's `setup.instruments` emptied and the realm's `seeded:` rows absent, through SYN-A's own switch if B32 shipped one, else a scoped override restored in `try/finally`, B21.72's `SUCCESSIONS` precedent; every fixture at control).
- WHERE: NEW `engine/season/harness/institution.py`; `references/ci_checks_registry.yaml` is not edited (an instrument, not a check).
- TESTS: none new for the report (SYN-D's own sentence, quoted above); the accretion pass keeps the module: its caller is the plan's named invocation (every family gate in this batch) and `headless` in the player's seat.
- FALSIFIER and CONTROL: "A report line that cannot name the `Act.via` of a conferral or the clause of a `due`" (SYN-D Falsifier). Control: running the report changes no hash: `content_hash` after `institution INST-01 2 0` equals the same case through `scenarios.run` (or `play`) with no report (a reader writes nothing).
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.institution INST-BYZ-ROGA 1 0 --out <scratch>` exits 0 once B40.04 lands (read there); here: `python -c "import engine.season.harness.institution as m; print(m.__doc__.splitlines()[0])"` → the module imports; on a planted spine world with no instrument, the `instruments`, `bonds`, `certificates` lines are omitted (`[ASSUMPTION: read by a one-line script in the commit body; no test file, per the source]`).
- HASH MOVERS: none (harness).
- DEPENDS ON: V12 B40.01; V12 Batch B36 (`--pin-rolls`); V12 Batch B07 (`task_draw_arm`); V12 Batches B32, B33 (`dues`, `kept`, `owed`, `debt`, `lot.*`, `document.*`, the `hand:` stage, `recites`); V12 Batch B09 (the reason trail, `ActStore.scene_of`); EXISTS-IN-TREE `harness/strife.py` (the kind), `queries/world_q.py::establishment_of`, `queries/person_q.py::legitimacy`, `data/fixtures.py` `default_store_kind`.
- GLOSSARY: *treasury* (the line's name, the U4d loan-word row: "fisc" rejected).
- COST and TIER: small build (harness); `sonnet`, `high`.
- LANDS IT: B40's producer; `Item: B40.02`, `[skip ci]`.

### B40.03 — "The King's Bill", the integrated scenario, and its eight endings · SYN-D §2, gates 1–8, with BYZ-F edit 4 · BUILD · HASH EQUAL
- SOURCE: SYN-D §2 "The scenario: 'The King's Bill'" (the case, the shown, the chosen table, the seats, the three cuts), "Gate (execution artifacts)" 1–8, "Falsifier"; BYZ-F "Exact edits" 4 (`court_lapsed`, `court_kept`); rulings A-80 (gate 8), A-12, A-14; C3-C12.
- ADVANCES: none of the nine; the integrated playable of the institutions (every crossing of audit §5.2 played, not designed).
- INSTRUCTION:
  1. NEW `engine/season/cases/exercises/INST-01.yaml`, SYN-D's case, copied (with `seats:` as U4 decides at B40.01):
     ```yaml
     id:    INST-01
     base:  realm
     setup:
       seats:
         - {id: off_house_case_lender, post: "Family Head", rung: {venue: "<the guildhall NPC-007 is homed in>"},
            body: null, faction: "Guilds", remit_acts: [issue, confer], conferral: null, revocation: null,
            holder: "NPC-007"}                                   # until batch I-8 authors it in offices.yaml
       instruments: []                                           # the realm's own seeded rows (I-3): two `homage`, one `immunity`
       stores:
         r_valoria:        {grain: 4}                            # the treasury: less than the year's bill   [ASSUMPTION; sweep ×{0.5, 1, 2}]
         duchy_hafenmark:  {grain: 12}
         duchy_varfell:    {grain: 12}
         terr_T9:          {grain: 10}                           # inside the immunity
         set_s_012:        {grain: 12}                           # Stillhelm
         <the lender's hearth>: {grain: 10, salt: 6}
       prehistory:                                               # each through the fold, pinned
         - {actor: <two cast persons with a deed the King holds a claim of>, verb: oblige, subject: off_king}
         - {actor: NPC-020, verb: confer, subject: off_dignity_2a, to: <the first>,  cites: <his deed>}
         - {actor: NPC-020, verb: confer, subject: off_dignity_3a, to: <the second>, cites: <his deed>}
     seats_offered:  [off_king, off_duchess_hafenmark, off_house_case_lender, <a hearth head of set_s_013>, off_cardinal_justice]
     ends:           [court_kept, court_lapsed, bond_met, bond_lapsed, audit_determined, sentenced, no_seat, season_count]
     span_seasons:   8
     ```
     "Stores are in `default_store_kind` (audit X-30). Every number is `[ASSUMPTION]` content with a sweep; the only requirement on them is that the treasury is short of the bill and the other chests are not." The angle-bracket entries are resolved at the item's open from the B39 realm and named in the commit body: the guildhall NPC-007 is homed in; the two cast persons with a deed the King holds a claim of (read from the realm's ledgers after B39's prologue); the lender's hearth; a hearth head of `set_s_013`. If B33's VEN-D content already authored `off_house_case_lender` in `offices.yaml` ("until batch I-8 authors it"), the case's `seats:` row is dropped and the commit says so. `off_dignity_2a`, `off_dignity_3a` are BYZ-A's dignity seats (B32); if they bear other ids there, the case names them.
  2. The eight endings, each in `CASE_ENDS` (B40.01, U7), a pure reader over `w.tenures`, `w.records` and `w.log` for the player's seat `seat`:
     - `court_lapsed` (BYZ-F edit 4): "of the terms ever sworn to the player's seat, more than half have matured unpaid."
     - `court_kept` (BYZ-F edit 4): "the season count is reached and none has."
     - `bond_lapsed`, `bond_met`: a `debt` Record to which the seat's holder is a party has its last stage's `term.matured` with `world_q.owed` above 0 (lapsed) or at 0 (met) (the report's `bonds` line: "the lapse read from `world_q.owed` after the last stage's `term.matured` (VEN-B; no `debt.lapsed` kind)") `[ASSUMPTION: definition; SYN-D names the ending only]`.
     - `audit_determined`: a `determine` Event under the `audit` arrangement row (COL-E's ending "an `audit` is determined") `[ASSUMPTION]`.
     - `sentenced`: a `ban.opened` whose subject is the seat's holder (SYN-D's consequences row, "an excommunicated king") `[ASSUMPTION]`.
     - `no_seat`: FA-P4's "the player holds no seat (`w.seat_holds(player)` empty)".
     - `season_count`: the season count is reached.
  3. The three cuts (SYN-D, copied): "| 1 | tax, borrow, leave unpaid, honour | I-1 to I-4 | · | 2 | the farm and its audit; writs through the Ministries' hand | I-5, I-7 | · | 3 | the levy in Himmelenger, the sentence, the answers; a suit before a Church bench | I-6 (the Church on its ground), I-7 |". In the suite's one order I-1 to I-8 are B32 and B33 (SYN-E's mapping), so all three cuts are live at B40's base: the gates below read cut 3.
- WHERE: NEW `engine/season/cases/exercises/INST-01.yaml`; `engine/season/harness/governance_spine.py` (`CASE_ENDS`: eight readers).
- TESTS: in `engine/season/tests/test_governance_spine_play.py`, first, red (no readers): `test_court_lapsed_reads_a_planted_majority_of_matured_unpaid_terms`, `test_court_kept_reads_none_matured_at_the_count`, `test_bond_lapsed_reads_owed_above_zero_after_the_last_stage` `[ASSUMPTION: test names; the item creates them]`, each on a planted log.
- FALSIFIER and CONTROL (SYN-D, copied): "A scenario whose opening state the fold could not produce (a set-up act refused). An ending reached at the control arm with the same frequency and by the same chain as at the live arm: the instruments did nothing. A report line that cannot name the `Act.via` of a conferral or the clause of a `due`. The scenario needing any act the season loop cannot form." Control: gate 4 and gate 6 below.
- GATE (SYN-D's, at `PYTHONHASHSEED=0`, seeds 0 to 9, **two seasons** ("eight seasons" in the source; A-114), the shipped chooser in every seat; each a run of `python -m engine.season.harness.institution INST-01 2 <seed> --out <path>` with the arm named):
  1. "The bill is met in more than one way. Across the seeds at least three of the six ways in the table are attempted by the King's seat-holder, and at least two different `ends` are reached." At two seasons the ways attempted are asserted; the endings are reported against the source's eight-season span and not asserted (U13).
  2. "A crossing occurs. In at least one seed-season an act by a person who is not the King is `occasioned_by` an Event of his: a duke's `petition` or `release`, the house's `give` of the bond, a hearth's `migrate`, a churchman's `open_case`."
  3. "The two parties to one instrument disagree somewhere (`15_INSTITUTIONS_COLONIAL_E` gate 2): in at least one seed-season the two readings of `kept` on one instrument differ."
  4. "Control. The same seeds with the realm's `seeded:` rows absent, the case's instruments absent and every fixture at control: no `dues` stamped, no `breaches` offered, and `content_hash` equal to the base realm's after the same stores delta." (`--control`.)
  5. "Planted failure. Every roll pinned to Success: gates 1 to 3 must then give one ending and one chain at every seed. If they still vary, the variety came from somewhere other than the draws and the reading is void." (`--pin-rolls Success`.)
  6. "One code path. `content_hash` of each all-NPC run equals `populated.run` on the same world after the same tick-0 acts."
  7. "Playable by a person. At `harness/headless.py` in the King's seat, four policies (tax hard; borrow and pay; borrow and default; farm and neglect) reach different endings on some seed, and any two of them are told apart by their distribution of endings over twenty seeds each. Manual; the close's reading, not a test's." At two seasons; reported against the eight-season span (U13).
  8. "Entrenchment moves the world (A-80; C3-C12). An arm in which every contest resolves at its control band, so every position holds … The report prints, per seed and season, the count of acts whose question cites an Event of the King's or an instrument of the case (a petition, a `tell`, a `migrate`, an `evade / defy`, a `release`). Expected reading: non-zero in every seed and rising while the bill stays unmet … Control: the same seeds with the case's instruments absent." (`--hold Failure`, U15; the control `--hold Failure --control`.)
  Every gate over a draw states its share over the named seeds with `assert checked >= 10` in the reading script quoted in the commit.
- HASH MOVERS: none (a case file and harness readers; the realm build is unchanged).
- DEPENDS ON: V12 B40.01, B40.02; V12 Batches B32, B33 (the kit's forms, `dues`, `kept`, `breaches`, `owed`, the `homage` and `immunity` seeded rows, the `audit` row, BYZ-A's dignity seats, the `debt` Record, the Ministries' hand); V12 Batch B39 (the prologue, the realm's ledgers); V12 Batch B21b (IN-36's march cap, the `march` way of a duke's answer); V12 Batch B24a (CR-60, CR-61: a Church bench that judges, cut 3); EXISTS-IN-TREE `off_king`, `off_duchess_hafenmark`, `off_cardinal_justice` (`engine/season/offices.yaml`).
- GLOSSARY: none new (*scenario*, B40.01).
- COST and TIER: small build (a case file, eight readers); `sonnet`, `high`; one `opus` read of gates 1 to 3 and 8 (SYN-D's implementation block).
- LANDS IT: B40's producer; `Item: B40.03`, `[skip ci]`.

### B40.04 — `roga`: a court that cannot pay · BYZ-F edit 1, gates 1, 3, 4, 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_BYZANTINE_F_playable_scenarios_and_reading.md` "The resolution, decided", "Exact edits" 1 (`INST-BYZ-ROGA.yaml`), "Gate" 1, 3, 4, 5, "Falsifier"; rulings A-21, A-80; C3-C12; closes F-FA-07 for the court ("there is no FA scenario, digest or end condition").
- ADVANCES: none of the nine; the Byzantine family's first standalone (the court, the treasury).
- INSTRUCTION:
  1. NEW `engine/season/cases/exercises/INST-BYZ-ROGA.yaml` (`base: spine`; "its set-up acts are `setup.prehistory`"). "On `build(seed)`'s thirteen seats, with the player at `lr_realm`'s seat", the set-up acts in order (BYZ-F, copied):

     | set-up act (in order) | by | makes |
     |---|---|---|
     | `establish` × 4 at the realm rung, rows `dignity: 4, 3, 3, 2`, `upkeep: 3, 2, 2, 1`, `body: null`, faction `faction x` | the Sovereign's seat | four dignity seats |
     | `transfer` of 1 unit of `default_store_kind` from his hearth to the realm rung, then `oblige` to the Sovereign's seat | each of the two Dukes | two real deeds (`transfer.made`) the Sovereign holds claims of; two termed oaths (`oblige_term`: mature in season 4) |
     | `transfer` of 2 units of `default_store_kind` to the realm rung, and no oath | the Count of chain `a` | a larger deed that no dignity cites, by a man not sworn |
     | `confer` of the grade-4 and one grade-3 seat, each citing that Duke's gift | the Sovereign's seat | two dignities held, two vacant |
     | stores | the three gifts; the builder's endowment for the duchies | the realm rung holds 4 against a first-year bill of 5; each duchy rung holds 6 |

  2. Site (BYZ-F's two `[UNVERIFIED]` lines, §5.7 SITE): open `loop/predicates.py::_req_establish` and record whether it accepts `dignity` and `upkeep` as founding operands. Branch (a), it does: the four rows are `establish` acts in `setup.prehistory`. Branch (b), it does not: "the four rows are authored … under the case's `setup.seats`, which is data and no branch". Open the spine persons' hearth stores: if a Duke's hearth holds nothing to give, "the case's `setup.stores` seeds them".
  3. `ends: [court_lapsed, court_kept, no_seat, realm_ended, season_count]` (BYZ-F edit 4's two "beside FA-P4's three": the player holds no seat, `world_q.endings_reached` non-empty, the season count; `court_lapsed`, `court_kept` are B40.03's readers; `realm_ended` is `IS-B2-CORE-02`'s `season_ending` name for `endings_reached`, added to `CASE_ENDS` here as a reader over it); `seats_offered: [<lr_realm's seat>]`; `span_seasons: 8` (BYZ-F's gate 3).
  4. "*What the player is shown each season* (FA-P4's `offered`, grouped by remit act, plus the digest): the bill and when it falls; the treasury; each sworn man, his grade, his term's maturity and his regard as the player's own ledger gives it; the persons whose deeds the player holds and who hold no dignity; the candidates `requisition` (per duchy, with the amount his shortfall claim names), `transfer` (per payee), `confer` (per vacant row and known deed)." No code: `offered` (B21.72, or `IS-B3-FA-02`'s replacement at B34) and B40.02's lines print it.
- WHERE: NEW `engine/season/cases/exercises/INST-BYZ-ROGA.yaml`; `engine/season/harness/governance_spine.py` (`CASE_ENDS`: `realm_ended`); `engine/season/governance_spine.yaml` only in branch (b) of step 2 if the rows cannot be case data (BYZ-F names it as the fallback home).
- TESTS: none new (BYZ-F: "Named test: none; the gates are runs of … `harness/institution` … quoted in the commit").
- FALSIFIER and CONTROL (BYZ-F, copied): "Remove the stipend rows' `upkeep`: the `treasury` line's bill reads the default and `court_lapsed` is unreachable at the scripted non-payer if the default is 0; the scenario then has no stakes, which the gate reports as a failure. Plant a situation built by direct assignment (a `hold` appended without the gate): gate 3's hash comparison fails." ("fisc" → `treasury`, U4d.)
- GATE (`PYTHONHASHSEED=0`; two seasons, A-114):
  1. "A scripted callback that pays nobody ends `roga` on `court_lapsed`; one that taxes both duchies each season until paid ends it on `court_kept` at some seeds and not at others (collection is drawn), and the seeds are reported; the auto chooser prints a non-empty digest in every season." At two seasons no sworn term has matured (`oblige_term`: season 4), so the two endings are reported against the source's span, not asserted (U13); asserted: a non-empty digest in every season, and the `treasury` line's shortfall above 0 at the non-payer's second season.
  3. "`content_hash` after eight seasons of `roga` under the auto chooser equals the same world run through `populated.run` with the same chooser" — after two seasons ("eight" in the source; A-114).
  4. "`institution INST-BYZ-ROGA 8 0 --bands 200`: for `requisition` and `confer`, no band is empty and none exceeds 0.9 in the live arm; the control arm is a single band." Run as `institution INST-BYZ-ROGA 2 0 --bands 200` (A-114), sized and launched in the background (the block's BACKGROUND RUN); `assert checked >= 200` in the reading.
  5. "Entrenchment (A-80; C3-C12). An arm of `roga` in which every contest resolves at its control band (positions hold: no levy beyond the control, no dignity resisted). The report prints, per seed and season, the count of acts whose question cites the bill, a matured oath or an unhonoured deed (petitions, `release`s, `tell`s). Expected reading: non-zero in every seed (an unpaid court is a referent others act on)." `--hold Failure` (U15), seeds 0 to 4.
- HASH MOVERS: none (a case on the spine; the realm and the spine's own build are unchanged).
- DEPENDS ON: V12 B40.01 to B40.03; V12 Batch B32 (BYZ-A: `dignity`, `dignity_grades`; the dignity `confer` draw, BIND_C, B21), V12 Batch B33 (BYZ-B: `upkeep`, `upkeep_owed`, `oblige_term` in use); EXISTS-IN-TREE `harness/governance_spine.py::build`, `governance_spine.yaml` (`lr_realm`), `data/fixtures.py` `default_store_kind`, `oblige_term`.
- GLOSSARY: none.
- COST and TIER: small build (a case file); `sonnet`, `high`; one `opus` read of gate 4's band table (BYZ-F's block).
- LANDS IT: B40's producer; `Item: B40.04`, `[skip ci]`.

### B40.05 — `chancery`: papers waiting in a hand · BYZ-F edit 2, gate 2 · BUILD · HASH EQUAL
- SOURCE: BYZ-F "Exact edits" 2 (`INST-BYZ-CHANCERY.yaml`), "Gate" 2; rulings A-13, A-21; BYZ-C (B33: a seat as a hand, `passes_through`, `carry`).
- ADVANCES: none of the nine; the Byzantine family's second standalone (the chancery).
- INSTRUCTION:
  1. NEW `engine/season/cases/exercises/INST-BYZ-CHANCERY.yaml` (`base: spine`), BYZ-F, copied: "The spine has no body. One `office_bodies` member is needed for a hand; `faction x`'s fixture cannot invent one (`governance_spine.yaml`'s own header: an invented body 'FORGES canon'). So the hand is a seat (proposal C, edit 1): the case's `setup.seats` gives the Sovereign's row `passes_through: [{seat: lo_territory_a}]`, and the player is the Lord of chain `a`. Set-up (`setup.prehistory`): the Sovereign `issue`s three writs at tick 0 (to the Count of `a`, the Count of `b`, and the Mayor of `a`); the Mayor of `a` files a `petition` addressed to the Sovereign. The writs' terms reach their addressees with the news of issue (A-21); what waits in the hand is the entered instrument." The Sovereign's row is an existing spine row: the case states its `passes_through` as a delta on that row (`setup.seats` / `offices:` per U4, keyed by the row's id).
  2. "*Shown:* each paper in his hand, its maker, its addressee, its terms, its age and the season it returns; his scene budget. *Chosen:* which to `carry` (a draw each), which to leave." No code (B40.02's `hands` line; FA-P4's `offered`).
  3. `ends: [no_seat, realm_ended, season_count]` (BYZ-F's table: "recalled, kept, FA's three": recalled is FA-B4's `recall` ending, the player holding no seat, B21.74; kept is the count reached) `[ASSUMPTION: the mapping of "recalled" and "kept" to these readers]`; `seats_offered: [lo_territory_a]` `[ASSUMPTION: the Lord of chain a's seat id is the `lr_territory_a` rung's seat, named at the item's open]`; `span_seasons: 8`.
- WHERE: NEW `engine/season/cases/exercises/INST-BYZ-CHANCERY.yaml`.
- TESTS: none new.
- FALSIFIER and CONTROL: BYZ-F's planted failure for the hand (I-5's, SYN-E): "delete `passes_through` from the court's row (the lag is zero)" → no paper is held over in any seed. Control: `content_hash` of an all-NPC two-season run equals `populated.run` on the same world after the same tick-0 acts.
- GATE (`PYTHONHASHSEED=0`, two seasons): 2. "A scripted callback that carries nothing ends `chancery` with every writ returned by the clock and, where the Sovereign's `revoke` then forms and draws Success, on FA-B4's recall; one that carries everything it can shows entered, held-over and returned papers across seeds." Seeds 0 to 4; the `hands` line quoted per seed; whether the recall occurs at two seasons is reported, not asserted (U13).
- HASH MOVERS: none.
- DEPENDS ON: V12 B40.01, B40.02, B40.04; V12 Batch B33 (BYZ-C: `passes_through`, `hands_open`, `carry` at a hand, "returned by the clock"); V12 B21.74 (`recall`); EXISTS-IN-TREE `governance_spine.yaml` (`lr_territory_a`).
- GLOSSARY: none.
- COST and TIER: small build (a case file); `sonnet`, `high`.
- LANDS IT: B40's producer; `Item: B40.05`, `[skip ci]`.

### B40.06 — The Farm of the Southern Tolls · COL-E scenario 1, gates 1–6 · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_COLONIAL_E_scenario.md` "Scenario 1 — The Farm of the Southern Tolls" (ground, setup delta, choices, legibility, stakes), "Gate" 1–6, "Falsifier for 'playable alone'"; its first `Reconciled:` line ("the farm's maker in the integrated playable is `off_king` … the conferred seat carries `audit_at_exit: audit`"); rulings A-80; C3-C10, C3-C12; D-U1-11k (`distance`).
- ADVANCES: none of the nine; the colonial family's standalone, and the integrated playable's second cut.
- INSTRUCTION:
  1. NEW `engine/season/cases/exercises/INST-COLONIAL-01.yaml`, COL-E's delta, copied, in SYN-D's case shape (`base: realm`):
     ```yaml
     id: INST-COLONIAL-01
     scale: territory
     setup:
       instruments:
         - form: farm
           maker_seat: off_lord_treasurer
           grant_ground: terr_T6
           to: <a cast case id resident in the capital>      # the farmer; [ASSUMPTION: content]
           amounts: {advance: 6, rent: 3}                      # units of `default_store_kind`; [ASSUMPTION; sweep ×{0.5, 1, 2}]
       stores:
         set_s_012: {grain: 16}                                # until SE's `ground` endowment lands; `coin` has no producer
         set_s_013: {grain: 7}
     seats_offered: [the conferred Farmer seat, off_lord_treasurer, a hearth head of set_s_013]
     ```
     `base: realm` is added (SYN-D's shape); `scale: territory` is kept only if B39's closed set holds a `scale` key, else dropped and the commit says so. The conferred seat carries `audit_at_exit: audit` (the first `Reconciled:` line). The farmer and the hearth head are named at the item's open from the B39 realm.
  2. `ends`, from COL-E's three: "the farm's term matures and an `audit` is determined (four bands)" → `farm_audited`; "the Farmer's hold closes before term (recall, release, death, a field)" → `farm_closed_early`; "six seasons elapse (MAX_SEASONS)" → `season_count`; `span_seasons: 6`. `farm_audited` and `farm_closed_early` are readers added to `CASE_ENDS` over the conferred seat's `hold` and the `audit` row's `determine` Event `[ASSUMPTION: the reader names; COL-E states the endings in prose]`.
  3. The choices are the existing verbs' candidates (COL-E: "each is an existing verb's candidate, so an NPC in the seat chooses among the same"): the farmer's `move`, `requisition`, `survey`, `transfer` (pay his men; send the rent "rolled at `distance` 2"), remit, answer a petition; the grantor's grant, own levy, `dispatch`, open the `audit`, renew; a hearth head's `conceal`, `petition`, testimony, `migrate`, oath. No code.
- WHERE: NEW `engine/season/cases/exercises/INST-COLONIAL-01.yaml`; `engine/season/harness/governance_spine.py` (`CASE_ENDS`: `farm_audited`, `farm_closed_early`).
- TESTS: none new (COL-E: "Named test: none; the gates are runs of the report quoted in the commit").
- FALSIFIER and CONTROL: "A human at `harness/headless.py` in the farmer's seat, offered the season's candidates, can reach each of the four audit endings on some seed by choosing differently (press hard and forge the accounts; press hard and be honest; remit; abscond). If two of those policies cannot be told apart by their outcome distributions over 20 seeds each, the choice is not a choice and the scenario fails. That reading is manual and is the close's, not a test's." Control: gate 4.
- GATE (COL-E's, "Seeds 0–4, six seasons, `PYTHONHASHSEED=0`, the NPC chooser in every seat", run at **two seasons** (A-114); `institution INST-COLONIAL-01 2 <seed>`):
  1. "Varied outcomes from one fixture: across the five seeds at least two different audit dispositions occur (counting 'not opened' as one), and at least one levy lands in each of three bands." The levy bands are asserted; the audit dispositions need the farm's term and are reported against the six-season span (U13).
  2. "The two ledgers disagree somewhere: in at least one seed-season the grantor's and the grantee's `kept` differ in sign or size."
  3. "Consequence is read downstream: at least one act by a person who is neither party is `occasioned_by` an Event of the farm (a petition, a migration, an oath)."
  4. "Control: the same seeds with the instrument absent: no Farmer seat, no levy through it, and the realm hash equals the base realm's at each season." (`--control`.)
  5. "Planted failure: every roll's band forced to Success. Conditions 1 and 2 must then fail; if they still pass, the variety was coming from somewhere other than the draws and the reading is void." (`--pin-rolls Success`.)
  6. "Entrenchment moves the world (A-80; C3-C12): an arm in which every contest resolves at its control band (positions hold: no levy beyond its control band, no audit determined). The report prints, per seed and season, the count of acts by persons who are neither party whose question cites an Event of the farm (petitions, `conceal`, `migrate`, oaths elsewhere). Expected reading: non-zero in every seed … Control: the instrument absent." (`--hold Failure`, U15.)
  "Five seeds are five trajectories. No rate, no balance claim, no tuning value is taken from them (CLAUDE.md §0.1 pt 4)."
- HASH MOVERS: none (a case file; the realm build is unchanged).
- DEPENDS ON: V12 B40.01 to B40.03; V12 Batch B32 (COL-A: the `farm` form, `dues`, `kept`, `breaches`), V12 Batch B33 (COL-B `distance`; COL-C the `audit` row, `audits_due`; SYN-B's ledger), V12 Batch B12c (`07_SE_valley_scenario`: SE's stores at seat rungs; `07_SE_treasury_granary_B`); EXISTS-IN-TREE `off_lord_treasurer` (`offices.yaml`).
- GLOSSARY: none.
- COST and TIER: small build (a case file, two readers); `sonnet`, `high`; one `opus` read of gates 1 to 3 and 6 (COL-E's block).
- LANDS IT: B40's producer; `Item: B40.06`, `[skip ci]`.

### B40.07 — The Katepano's Latitude · COL-E scenario 2 · BUILD · HASH EQUAL
- SOURCE: COL-E "Scenario 2 — The Katepano's Latitude", "Landing order for the family" row 7 ("C-5 scenario 2 | E | 3; FA-B1; MB field; ED-IN-0317 | none"); COL-F edit 5's last seeded bullet ("This is what gives the second scenario its hold on the Katepano", B40.25); D-U1-11k.
- ADVANCES: none of the nine; the colonial family's second standalone (distance and a far governor).
- INSTRUCTION:
  1. NEW `engine/season/cases/exercises/INST-COLONIAL-02.yaml` `[ASSUMPTION: case id; COL-E names the scenario, not the file]`, `base: realm` (`build_realm(S, foreign=True)`, the shipped default: `harness/populated.py:1015` `foreign: bool = True`), no `setup` delta beyond "the court seat (`…_B_distance.md` §4)" which COL-B lands in B33 (if B33 shipped it only under a case, the row is this case's `offices:` delta and the commit says so). COL-E, copied: "Seats offered: `off_katepano`, `off_altonian_court`, `off_king`. The court issues orders and hears only what somebody travels to tell it (orders are rolled at `distance` 3); the Katepano may `march` through T3, offer a `tribute` or a `wardship` by `covenant` to a Crown seat, or `construe` an order that arrived open to reading."
  2. `ends`: "the roster's (`peninsular_sovereignty`, `theocracy`, `reabsorption`), her recall, six seasons" → `realm_ended` (B40.04's reader over `world_q.endings_reached`), `recalled` (her `hold` on `off_katepano` closed by `revoke`) `[ASSUMPTION: reader name]`, `season_count`; `span_seasons: 6`.
- WHERE: NEW `engine/season/cases/exercises/INST-COLONIAL-02.yaml`; `engine/season/harness/governance_spine.py` (`CASE_ENDS`: `recalled`).
- TESTS: none new.
- FALSIFIER and CONTROL: COL-E states none of its own for scenario 2; SYN-D's "The scenario needing any act the season loop cannot form" applies. Control: `content_hash` of an all-NPC two-season run equals `populated.run` on the same world (SYN-D gate 6; scenario 2's delta adds no row of its own).
- GATE (`PYTHONHASHSEED=0`, seeds 0 to 4, two seasons): `institution INST-COLONIAL-02 2 <seed>` exits 0 and prints the `hearings`, `carried` and `instruments` lines with the Katepano's acts; the control above equal; which of `march`, `covenant`, `construe` she forms is reported per seed, not asserted (`[ASSUMPTION: gate; COL-E's gate is the family's and reads scenario 1]`).
- HASH MOVERS: none.
- DEPENDS ON: V12 B40.06; V12 Batch B11 (CR-29: the border), V12 Batch B21 (FA-B1, `06_FA_war_lives_in_seats_B`), V12 Batches B19, B20 (MB's field, closed before B40 through B22 → B38 → B39), V12 Batch B21b (IN-36: ED-IN-0317's march cap, the intake `:249`); V12 Batch B33 (COL-B §3–§5: reach rows, the court seat `off_altonian_court`, the ending row); EXISTS-IN-TREE `off_katepano`, `off_king` (`engine/season/offices.yaml`), `rosters.yaml` `peninsular_sovereignty`.
- GLOSSARY: none.
- COST and TIER: small build (a case file, one reader); `sonnet`, `high`.
- LANDS IT: B40's producer; `Item: B40.07`, `[skip ci]`.

### B40.08 — The Vacant Chair · PAP-F edits 1–3, gate · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_PAPACY_F_playable_vacant_chair.md` "The resolution, decided" (situation, who the player may be, stakes, end, legibility), "Exact edits" 1–3, "Gate", "Falsifier", "What is missing today"; rulings A-5, A-14, A-15, A-36, A-80; C3-C12, C3-L9 (`patronage` is a table entry).
- ADVANCES: none of the nine; the Church's standalone (its own people decide something that lasts).
- INSTRUCTION (PAP-F "Exact edits", copied):
  1. "`engine/season/cases/exercises/INST-PAPACY-01.yaml` (SYNTHESIS-D §1's case shape): `base: realm`; `setup.prehistory: [{actor: <the holder of off_cardinal_prudence>, verb: release, subject: off_cardinal_prudence}]`; `seats_offered: [off_confessor, <each seated or sworn Church person>, off_king]`; `ends: [chair_filled, chair_contested, long_vacancy]`; `span_seasons: 3`. The runner is FA-P4's `play(seed, seasons, situation=<case id>, player, world="realm")` (`world` is FA-B4's keyword, not this file's); no flag is added to `governance_spine.py`."
  2. "No digest filter: the one report's `seats` line prints the Church of Solmund's seats (SYNTHESIS-D §3)."
  3. "No edit under `loop/`, `state/`, `queries/`, `decision/`, `data/`."
  4. The three endings in `CASE_ENDS` (PAP-F "End"): `chair_filled` — "the chair is held on a hold that is not provisional: *filled*, with by whom and through which seat"; `chair_contested` — "it is held provisionally at the last season"; `long_vacancy` — "three seasons pass with it empty".
  5. CR-88 (U2): open `world_q` and `verb_table.yaml` at the item's open for CR-88's vacancy duty (B21d). If it landed, nothing more. If it did not, PAP-F's own fallback: "a planted question carrying the vacancy (the scenario may plant the *question*, never the outcome)", as one `setup.prehistory` entry that deposits the question and no tenure write; the commit says which.
- WHERE: NEW `engine/season/cases/exercises/INST-PAPACY-01.yaml`; `engine/season/harness/governance_spine.py` (`CASE_ENDS`: the three).
- TESTS: none new (PAP-F: "Named test: none; the gates are runs of the report quoted in the commit").
- FALSIFIER and CONTROL (PAP-F, copied): "A run whose ending is fixed by the seat-holder's identity alone (the same holder in every seed whatever the draw). A digest line that cannot name the `Act.via` of a conferral. The scenario needing any act the season loop cannot form." Controls below.
- GATE (PAP-F's, `PYTHONHASHSEED=0`, at **two seasons** (`span_seasons: 3` in the source; A-114)):
  - "`python -m engine.season.harness.institution INST-PAPACY-01 3 s`, `s` in 0-4, all-NPC: each run ends in one of the three endings and prints which. Across the five seeds at least two different endings or two different holders occur" — run as `INST-PAPACY-01 2 s`; `long_vacancy` cannot be reached in two seasons and is reported, not asserted (U13).
  - "With a player-proxy as the Confessor choosing a fixed conferee by policy: over 200 seeds the conferee is seated in some, seated provisionally in some and resisted in some (the draw), and the share seated is higher for a conferee the Cardinals regard well than for one they do not (two arms, exact odds printed)." Background run; `assert checked >= 200` per arm.
  - "Control 1: the same seeds with no vacancy planted: no `tenure.opened` on the seat."
  - "Control 2: `content_hash` of each all-NPC run equals `populated.run` on the same world after the same tick-0 act."
  - "Control arm (patronage): the seat's `tables.patronage` entry removed: at some seed the Crown's seat fills the chair. With it: never." (U17.)
  - "Entrenchment (A-80; C3-C12): an arm in which every contest resolves at its control band … The report prints, per seed and season, the count of acts whose question cites the vacancy, a refused candidacy or a rival's petition (petitions, `argue`, `tell`, `covenant` offers). Expected reading: non-zero in every seed". (`--hold Failure`, U15.)
- HASH MOVERS: none.
- DEPENDS ON: V12 B40.01, B40.02; V12 Batch B21 (FA-P4's `play`, `14_VERBS_BINDING_C`'s `confer` draw, FA-B4's `world=`); V12 Batch B32 (PAP-A, PAP-B: `tables.patronage`, `may_fill`, the ballot tally with PAP-G item 1's floor); V12 Batch B21d (CR-88, not a gate edge: U2); V12 Batch B37 (A-15's natural death, the second opening; closes at S16); EXISTS-IN-TREE `off_cardinal_prudence`, `off_confessor`, `off_king` (`engine/season/offices.yaml`), `harness/play_surface.py::dispatching_chooser`, `state/gate.py::may_fill`.
- GLOSSARY: none.
- COST and TIER: small build (a case file, three readers); `sonnet`, `high`; one `opus` read of the 200-seed arms (PAP-F's block).
- LANDS IT: B40's producer; `Item: B40.08`, `[skip ci]`.

(B40.09 is a READING: no body and no commit of its own; its text is Readings R1, at the batch's end, read at B40.99.)

### B40.10 — five readings of the court in the report · BYZ-G item 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` "Item 3. Five readings added to the scenario report (no game code; with F)", its gate, "Exact edits, by file and owner" row 3; U5d closure Part 7.2 (§14 item 4 closed: no barred order).
- ADVANCES: none of the nine; four court stories made visible or visibly absent.
- INSTRUCTION: in `harness/institution.py` (B40.02), four lines, each "one line of the report … computed from the log, with what would show the story did not occur" (BYZ-G's table, copied; the fifth row is omitted, as the source says):

  | reading | computed from | it fails when |
  |---|---|---|
  | **who stayed away** | for each sitting under `acclamation` (proposal E), the sworn of the conferring seat not present at the venue that tick | attendance is total in every seed (presence carries no choice) |
  | **what the hand took** | `transfer` Events received by a holder of a `passes_through` seat from the makers of instruments then in that hand | no such transfer in any seed, or no difference in entry rate between papers with and without one |
  | **the servant after the reign** | after a `succeed` on a seat, the `revoke`s by the new holder against seats on its `passes_through`, split by whether each old holder also holds a dignity | the split shows no difference over seeds |
  | **what he kept** | stores at rungs a departed hand's holder moved goods to, before and after his `hold` closed | — (a count; reported, not gated) |
  | **the lord who outgrew his minister** | — | "omitted: §14 item 4 is closed with no barred order (`U5_FINDINGS_CLOSURE_U5d.md` 7.2), so no chamberlain class exists to read" |

- WHERE: `engine/season/harness/institution.py` (four lines).
- TESTS: none new (BYZ-G: "items 1 and 3 are runs of `harness/institution.py` quoted in the commit").
- FALSIFIER and CONTROL: each line's "it fails when" column. Control (BYZ-G): "the same lines on the base realm print zeros (no `passes_through`, no `acclamation`)".
- GATE: "The report prints the first two on `chancery` and `roga` at seeds 0 to 19": `PYTHONHASHSEED=0 python -m engine.season.harness.institution INST-BYZ-CHANCERY 2 <s>` and `INST-BYZ-ROGA 2 <s>`, s = 0 to 19, two seasons (A-114) → the *who stayed away* and *what the hand took* lines present and quoted per seed; the control lines on the base realm (`--world realm`, B21.74) → zeros.
- HASH MOVERS: none.
- DEPENDS ON: V12 B40.02, B40.04, B40.05; V12 Batch B32 (BYZ-E: `acclamation`, its audiences), V12 Batch B33 (BYZ-C: `passes_through`, the hand); V12 Batch B21 (`succeed`, `revoke` draws).
- GLOSSARY: none.
- COST and TIER: small build (harness); `sonnet`, `high` (BYZ-G: "effort … `high` (items 3, 4)").
- LANDS IT: B40's producer; `Item: B40.10`, `[skip ci]`.

### B40.11 — an entered paper is a precedent file · BYZ-G item 4 · BUILD · HASH EQUAL
- SOURCE: BYZ-G "Item 4. The register as a precedent file (a gate, no edit; with C and SC's cited evidence)", "Exact edits" row 4; C3-C10 (a held Record cited is a `proofs` level).
- ADVANCES: none of the nine; shows that BYZ-C's "the entry is the proof" and SC's cited evidence compose.
- INSTRUCTION: "Nothing is added. Proposal C makes an entered instrument a sealed Record a hand's holder holds; SC's cited evidence (`05_SC_evidence_and_rebuttal*.md`, the SC-P8 the audits cite) lets a held Record be filed as an item, which enters the roll as a `proofs` level (C3-C10). The plan is to show that the two compose." One test fixture: NEW `engine/season/tests/test_inst_byz_g.py` (the source's named file, "for the hand-built gates of items 2 and 4"), a planted hearing on the spine: "A planted hearing before the Sovereign's seat on a petition to amend the founding papers, two arms over 200 seeds: the clerk cites an entered instrument he holds; he cites nothing."
- WHERE: NEW `engine/season/tests/test_inst_byz_g.py`.
- TESTS: `test_a_cited_entered_instrument_moves_the_recorded_proofs_level` and `test_all_four_bands_occur_in_both_arms` `[ASSUMPTION: test names; the item creates them]`, each over dice seeds 0 to 199 with `assert checked >= 200`; read green (a composition of landed parts) and red with the citation dropped from the clerk's filing (the planted failure).
- FALSIFIER and CONTROL: "Equal levels: an entry is not citable and proposal C's 'the entry is the proof' is prose." Control: the arm that cites nothing.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_g.py -q` → pass: "The recorded `proofs` levels differ between arms (no draw needed to see it) and all four bands occur in both."
- HASH MOVERS: none (a test).
- DEPENDS ON: V12 Batch B33 (BYZ-C: the entered instrument, a sealed Record a hand's holder holds); V12 Batch B24 (`05_SC_evidence_and_rebuttal_B`, `12_ARCS_cited_evidence`: a held Record filed as an item; `world_q.hearing`); V12 Batch B05 (OBS: the `proofs` level); EXISTS-IN-TREE `harness/governance_spine.py::build`.
- GLOSSARY: none.
- COST and TIER: small build (a test fixture); `sonnet`, `high`.
- LANDS IT: B40's producer; `Item: B40.11`, `[skip ci]`.

### B40.12 — an exit audit on the seats that hold money or a frontier · BYZ-G item 1 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ-G "Item 1. Audit at exit on the seats that hold money or a frontier (content; after B)", "Exact edits" row 1; rulings A-13 (D-13: "a seat may declare … an exit audit"); synthesis X-12, X-13; C3-C10.
- ADVANCES: none of the nine; A-13 (a fiscal officer's departure has a reckoning).
- INSTRUCTION: "Use the kit's one encoding (synthesis X-12: key `audit_at_exit: <arrangement id> | null`, row `audit`, occasion 'any close of a hold on such a row'). This proposal only names the Byzantine seats that declare it:"
  ```yaml
  # engine/season/offices.yaml — added to three existing rows, nothing else on them changes
    - id: off_lord_treasurer      # NPC-037; the treasury of proposal B
      audit_at_exit: audit
    - id: off_katepano            # NPC-089; the frontier post of proposal D
      audit_at_exit: audit
    - id: off_kommerkiarios       # NPC-090; the treaty gate
      audit_at_exit: audit
  ```
  "`[ASSUMPTION; medium; Jordan to correct — which seats. Revert: delete the three lines.]` The two foreign seats are audited by the far superior's seat (`off_altonian_court`, synthesis X-13), which is who 'may open' under X-12's rule; whether that seat's holder does is his own choice." "Nobody is made to open it: `audits_due` offers the referent and the chooser decides (VENICE-C §4)." Listed in the PR body as an authored value for Jordan (D-19).
- WHERE: `engine/season/offices.yaml` (`off_lord_treasurer`, `off_katepano`, `off_kommerkiarios`: one key each).
- TESTS: none new (BYZ-G: item 1's gate is a run of the report).
- FALSIFIER and CONTROL (BYZ-G, copied): "If the referent appears in a seed where the hold did not close (the `revoke` drew Failure), the occasion is wrong. If a case opens in every seed in which the hold closed, the engine is docketing (a trigger, not a person). If the verdict distribution is the same with and without recorded collections, the hearing reads nothing and the item is decoration." Control: "the three lines absent, `content_hash` equal to" the same run without them.
- GATE (`PYTHONHASHSEED=0`): on INST-01 (`base: realm`; the source names `roga`, whose spine base has no `off_lord_treasurer`: U10), "seeds 0 to 199: plant a `revoke` of the treasurer in season" 1 ("season 4" in the source; two seasons, A-114), read at season 2: "an `audits_due` referent naming her on the questions of those who may open, in every seed in which the `revoke` closes the hold; an `open_case` under `audit` in some seeds and not all (a person's choice); over the seeds where a case opened, verdict bands none empty and none above 0.9; in the arm where she collected nothing, her side's opponent files no `proofs` item of her collections." Background run; `assert checked >= 200`. The realm hash at seed 0, one season, recorded (moved only where a covered hold closes).
- HASH MOVERS: every seeded run in which a hold on one of the three seats closes (an `audit` referent formed; a case opened). Declared; B40.99's one re-pin.
- DEPENDS ON: V12 Batch B32 (VEN-C: the `audit_at_exit` key, a table row), V12 Batch B33 (COL-C: the `audit` row, `world_q.audits_due`; BYZ-B: a treasurer who has collected; COL-B: `off_altonian_court`); V12 B40.03 (the gate world); EXISTS-IN-TREE the three rows in `engine/season/offices.yaml`.
- GLOSSARY: none.
- COST and TIER: edit (content); `sonnet`, `medium` (BYZ-G); one `opus` read of the band table.
- LANDS IT: B40's producer; `Item: B40.12`, `[skip ci]`.

### B40.13 — the treaty gate breeds its own offence · BYZ-G item 2 · BLOCKED (v12: a carrier is owed: the place-filtered `deed_doers` form in `data/goals.py`)
- SOURCE: BYZ-G "Item 2", "Exact edits" row 2; `proposals/15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger.md` "Exact edits" 4 and its `[UNVERIFIED]` block (the place filter "is requested, not built here"); U4 §3.4 (BYZ_G: "INCOMPLETE: item 2 blocked").
- What is missing: the row `goal_kommerkiarios_side_roads` "**ships off** until `data/goals.py` gains the place filter PAPACY-C requests for its own `deed_doers` row (deeds whose claim subject lies under a named rung); with the filter, the row's `under:` names the treaty ground." No item in v12 builds that form (`grep -l "place filter"` over this directory's parts and `master/instructions/` finds none at this read), and `goals.yaml` has no switch by which a row ships off (`grep -n "enabled\|active:" engine/season/goals.yaml` → none). Owner: `data/goals.py`'s owner (CHAR; `12_ARCS_arcs_as_staged_goals`).
- What lands when the carrier exists (BYZ-G, copied): the row
  ```yaml
    - id: goal_kommerkiarios_side_roads
      org: {seat: off_kommerkiarios}
      text: the Kommerkiarios acts against whoever he knows to have traded past the treaty's gate
      object: {kind: deed_doers, kinds: [<the breach kind of the treaty staple>]}
      pursuits: {stability: 0.6, justice: 0.3, wealth: 0.1}
      derives: {from: goal_kommerkiarios_treaty_order, kind: establishes}
      source: >-
        INST-BYZ-GROUNDING item 2. [ASSUMPTION; medium; Jordan to correct -- the weights and that the
        strictness is a goal at all. Revert: delete the row.]
  ```
  with `kinds:` the success kind of the act the `staple` row's `forbears` clause names ("the loader refuses a kind outside `data/verbs.py::DEED_KINDS`"); gate: "Hand-built on the realm with `foreign=True`: one person holds a claim of a breach by a merchant; the Kommerkiarios is told it. Over 200 seeds his chooser forms `open_case` against the merchant in some seeds and not all … *Control:* the row absent: no such case forms in any seed"; falsifier: "The case forming in every seed (a trigger, not a person), or forming against persons he holds no claim about"; test file `engine/season/tests/test_inst_byz_g.py` (B40.11's).
- LANDS IT: no commit in B40; the receipt and B40.99's commit body name the missing carrier.

### B40.14 — paired officers, near and far · VEN-E edit 1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` "Edit 1 — the paired officers, near and far (M-1, M-2)", "Exact edits, by owner" row 1, "Gate" 1, 2; rulings A-13 (the U5d line: "content on the three ruled seat facts"); C3-L9 (`cooling_off` is a table entry).
- ADVANCES: none of the nine; a subject place has two voices to the centre.
- INSTRUCTION (VEN-E, copied): "On every subject settlement where D authors a rector, **two** rows on the same anchor, both `conferral: appointed`, `revocation: rung_above_in_holdings`, `term: 8`, `audit_at_exit: audit`, and a `tables.cooling_off` entry of 8, each holding a `commission` (the kit's form):
  ```yaml
  - id: off_<place>_justice        # post label is Jordan's (names_index); functional here
    remit_acts: [open_case, determine, issue]
  - id: off_<place>_captain
    remit_acts: [dispatch, convene, requisition]     # the garrison and the purse
  ```
  Remits are disjoint by construction (the loader already refuses nothing here; the convention is content). **Near and far** is a convention on the author, stated once in the file's header comment and enforced by nothing: a place whose conferring seat stands one territory hop away gets the pair; a place farther off (Schoenland's line seat, any seat beyond a border) gets one row holding both remits. No reader." The places are read at the item's open from VEN-D's rector rows (B33) and listed in the commit body; D's single rector row on a near place is replaced by the pair (the `commission` seeded rows follow the seat ids). "The combined seat is the stronger one and is what the colonial lane's 'over-mighty warden' reading watches." Each new seat's post label is a placeholder listed in the PR body for Jordan (names_index).
- WHERE: `engine/season/offices.yaml` (the pair rows; the header comment); `engine/season/rosters.yaml` (`tables.cooling_off`: one entry per new seat); `engine/season/instruments.yaml` (`seeded:` `commission` rows re-pointed to the new seat ids, if B33 seeded one per rector).
- TESTS: none new for the rows (content; VEN-E's test file is for gates 3, 4, 6).
- FALSIFIER and CONTROL: "For 'the pair generates disagreement': gate 2 printing identical lines in both arms across the three seeds." Control (VEN-E gate 1): "with batch E's rows absent, `build_realm(0)` and a one-season run hash EQUAL to the post-D hash" (B39's close reading, `reading @<sha>`).
- GATE (`PYTHONHASHSEED=0`): `python -m engine.season.harness.register --check` → exit 0 and the offices loader accepts the rows (`build_realm(0)` builds); VEN-E gate 2: "a spine fixture with one subject town, seeds 0 to 2, eight seasons, the chooser in both seats. Report per season the claims each officer `tell`s the conferring seat about the town and whether any pair has opposite content; report the centre's next act toward the town. Control: the same town with one combined officer. **A reading, not a pass mark;** it fails as an instrument if the two arms print the same lines." Run at two seasons (A-114) on the Counting-House case (`INST-VENICE-01`, VEN-E's block: "gates 2 and 5 are runs of `harness/institution.py` on the Counting-House case"), the pair placed on `lr_settlement_a` through the case's `offices:` delta, and the control arm a second case file `INST-VENICE-01-ONE.yaml` with one combined row `[ASSUMPTION: the arm's form and file name; the source names the arm only]`.
- HASH MOVERS: the realm build hash (new seats and their seeded commissions on every place D authors a rector). Declared; B40.99.
- DEPENDS ON: V12 Batch B33 (VEN-D: the rector rows, the `{venue:}` anchor, `INST-VENICE-01.yaml`); V12 Batch B32 (SYN-A: the `commission` form; VEN-C: `tables.cooling_off`, `audit_at_exit`); V12 B40.02 (the report).
- GLOSSARY: none.
- COST and TIER: edit (content); `sonnet`, `medium`; one `opus` read of gate 2 (VEN-E's block).
- LANDS IT: B40's producer; `Item: B40.14`, `[skip ci]`.

### B40.15 — the submission pact · VEN-E edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 2 — the submission pact (M-3)", "Exact edits" row 2.
- ADVANCES: none of the nine; a conquered commune holds terms its superior can breach.
- INSTRUCTION (VEN-E, copied): "No new form. The subject commune's head seat holds, at build, a seeded Record of the kit's existing form `capitulation` (terms on which a place was given up) made by the superior's seat, whose `forbears` clauses bind the grantor: `tenure.closed` by `revoke` and `tenure.opened` by `confer` over the commune's own seats, and `requisition.taken` over the place. The colonial lane's readers do the rest: a rector who levies inside the pact is rolled as any levy, is witnessed, and stands as a breach in the commune's members' `kept` … One row in `seeded:` per subject commune D authors; `grade: assumption`." The communes are read from VEN-D's rows at the item's open and listed in the commit body.
- WHERE: `engine/season/instruments.yaml` (`seeded:`: one `capitulation` row per subject commune).
- TESTS: none new.
- FALSIFIER and CONTROL: a rector's levy inside the pact leaves the commune members' `kept` unchanged (the pact binds nothing). Control (VEN-E gate 1): the rows absent, the realm hash at seed 0, one season, equal to B39's close.
- GATE: `python -m pytest engine/season/tests/test_instruments.py -q` → pass (the `seeded:` loader accepts the rows, SYN-A's refusals unchanged); `build_realm(0)` → the commune head seats each hold one live `capitulation` Record (a one-line script, quoted).
- HASH MOVERS: the realm build hash (one seeded Record per subject commune). Declared; B40.99.
- DEPENDS ON: V12 Batch B32 (COL-A, SYN-A: the `capitulation` form, `seeded:`, `kept`, `breaches`); V12 Batch B33 (VEN-D: the subject communes).
- GLOSSARY: none.
- COST and TIER: edit (content); `sonnet`, `medium`.
- LANDS IT: B40's producer; `Item: B40.15`, `[skip ci]`.

### B40.16 — the appointer answers: the audit's recital · VEN-E edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 3 — the appointer answers; the inspection is seen (M-4, M-5)", "Exact edits" row 3, "Gate" 3; its second `Reconciled:` line (the `[UNVERIFIED]` resolved at the tree); `04` §B.9.
- ADVANCES: none of the nine; appointment costs the appointer something.
- INSTRUCTION (VEN-E, copied): "**The recital.** The Record the `audit` row mints at Partial (the admonition), and the `ban`'s or `oblige`'s opening claim at Success and Overwhelming, carry in `recites` the id of the seat through which the audited hold was conferred, read from the hold's opening Event's causing act: `state/attribution.py::causing_act(w, e).via` (opened: `causing_act` returns the whole `Act` for exactly this question …; `Act.via` is `state/carriers.py` …; the mint is resolver-side, so the act-store read is lawful, `04` §B.9). One line where the row's disposal builds the Record's content (owner: the single document mint, `loop/effects_information.py::_mint_document`, as COL-C uses it). `recites` is the kit's existing content key (SYN-A edit 1); this is its fourth use." "**Who reads it.** Nobody by rule. A person who holds the Record holds a deed of the appointer's (he seated a man the bench condemned); `person_q.deeds_judged` values it as it values any deed." "**The inspection as theatre** is a reading, not an edit: COL-C's row already sits on the governed ground with `floor: open`. The gate below reports the governed cohort's regard for the conferring seat's holder before and after a sitting, against a control row with `floor: sealed`." (Line numbers into files edited at or before B03a dropped, §5.4.)
- WHERE: `engine/season/loop/effects_information.py` (the `audit` disposal's content build in `_mint_document`'s caller: one line); NEW `engine/season/tests/test_inst_ven_e.py` (the source's named file, gates 3, 4, 6).
- TESTS: in the new file, written first, red (no recital): `test_the_audit_record_recites_the_conferring_seat` and `test_deeds_judged_differs_for_a_holder_of_the_record` `[ASSUMPTION: test names; the item creates them]`.
- FALSIFIER and CONTROL: "Planted failure: drop the recital and the two values are equal." Control: an audit sitting at Failure mints no recital (only Partial, Success, Overwhelming carry it).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_e.py -q -k recite` → pass: "a hand-built `audit` sitting forced to Partial; the minted Record's `recites` holds the conferring seat's id; `deeds_judged(p, conferrer)` for a person given the Record differs from the same person without it." The theatre reading: on `INST-COLONIAL-01` (B40.06) at seeds 0 to 4, two seasons, the governed cohort's regard for the conferrer before and after a sitting, and against a `floor: sealed` control row, quoted.
- HASH MOVERS: every seeded run with an `audit` sitting at Partial or better (the Record's content). Declared; B40.99.
- DEPENDS ON: EXISTS-IN-TREE `state/attribution.py::causing_act`, `state/carriers.py::Act.via`, `loop/effects_information.py::_mint_document`, `queries/person_q.py::deeds_judged`; V12 Batch B33 (COL-C: the `audit` row and its disposal); V12 Batch B32 (SYN-A edit 1: `recites`).
- GLOSSARY: none.
- COST and TIER: small build (one line at the mint and its test); `sonnet`, `high` (VEN-E: "`high` for edits 3 and 5").
- LANDS IT: B40's producer; `Item: B40.16`, `[skip ci]`.

### B40.17 — the secretary order and the standing report · VEN-E edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 4 — the secretary order and the standing report (M-6, M-7)", "Exact edits" row 4; C3-L9 (`eligible_from` is a table), C3-C10 (a held report is a `proofs` level); U1 glossary *roll* (a membership is a **list**).
- ADVANCES: none of the nine; a non-noble route up with a ceiling (the source's NERS: **narrowed**, "the first to drop if the batch must shrink").
- INSTRUCTION (VEN-E, copied):
  1. "One list seat `off_<republic>_citizen_roll` (`binds: members_by_warrant`, `remit_acts: [issue]`), distinct from the council's list. One body `"Chancery"` in `office_bodies`. Two secretary seats on it: `conferral: appointed` by the head seat, **no `term`**, `remit_acts: [issue]`, and a `tables.eligible_from` entry naming `off_<republic>_citizen_roll`; every council seat's `tables.eligible_from` entry stays the council's list, so a secretary can never be drawn for one. That is the ceiling, and it is one existing table (VENICE-C §2 as reconciled)."
  2. "The college's written menu (audit §1.4) is `issue`d through a secretary's seat: the drafter is not the proposer. No mechanism: `Act.via` already names the seat."
  3. "**The standing report.** The `commission` form's `due` (`record.given every 4, to: grantor_rung`, SYN-A) is the report. This edit states what the Record is and where it rests: a `survey` product of the place, `give`n to the Chancery's rung, where the secretary holds it with its predecessors. The successor may be `give`n it; a held report of a place is a `proofs` level on his graded acts there (leverage, C3-C10) … It fades as every claim fades (`01_CORE_claim_fade_as_read.md`); it can be seized, concealed, forged (FI's verbs)." No code for step 3: the `due` exists (SYN-A); the item writes the `commission` row's `source:` note naming the report.
  `<republic>` is VEN-D's republic seat prefix, read at the item's open; post labels are placeholders for Jordan (PR body).
- WHERE: `engine/season/offices.yaml` (the list seat, two secretary seats); `engine/season/rosters.yaml` (`office_bodies`: `"Chancery"`; `tables.eligible_from`: three entries); `engine/season/instruments.yaml` (`forms.commission`'s `source:` string).
- TESTS: none new.
- FALSIFIER and CONTROL: a secretary drawn for a council seat (the ceiling leaks). Control (VEN-E gate 1): the rows absent, the realm hash at seed 0, one season, equal to B39's close.
- GATE (`PYTHONHASHSEED=0`): `build_realm(0)` builds; `python -c` over `may_seat` / the lot's eligibility (VEN-C, B32) for each secretary against each council seat → False for every pair, quoted; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: the realm build hash (three seats, one body). Declared; B40.99.
- DEPENDS ON: V12 Batch B32 (VEN-C: `tables.eligible_from`, `selection: lot`; SYN-A: `commission` and its `due`); V12 Batch B33 (VEN-D: the republic's council and list seats); V12 B40.14 (the same file, its rows first).
- GLOSSARY: none (*list* is the glossary's word for a membership roll).
- COST and TIER: edit (content); `sonnet`, `medium`.
- LANDS IT: B40's producer; `Item: B40.17`, `[skip ci]`.

### B40.18 — the contract in phases; the yard's wage · VEN-E edits 5 and 5b · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 5 — the contract in phases; arrears; the works' wage (M-8, M-9)", "Exact edits" rows 5, 5b, "Gate" 4.
- ADVANCES: none of the nine; a hired captain's reserve season in which buying him is lawful.
- INSTRUCTION:
  1. Site (§5.7 SITE; U1): open `data/instruments.py`'s clause type and record whether it is a dataclass that `World.content_hash()` reaches (a `Record` field, `state/world.py::_object_head`). If it is, a new clause field is an encoding mover (D-04) and this item's HASH line reads MOVER(encoding) in its commit.
  2. `engine/season/instruments.yaml: forms`, the form (VEN-E, copied):
     ```yaml
       - id: condotta                # a hired captain's contract with an employer's seat
         made_by: covenant
         grantor_act: dispatch       # the employer's seat must be one that can send men
         term: 4                     # the bound stage, in seasons
         renewal: grantor            # the employer's option opens the reserve stage
         due:
           - {by: grantor, kind: transfer.made, every: 1, to: grantee_rung}     # pay; half in the reserve stage
         forbears:
           - {by: grantee, kind: duty.taken,     over: named}        # bound stage only: no second employer
           - {by: grantee, kind: march.declared, over: grant_ground} # for `term` seasons after lapse
         lapse: stands
         hardens: false
         grade: assumption
         source: "15_INSTITUTIONS_VENICE.md §17.2 item 8; CGR:110, :208"
     ```
  3. "**The one build:** a form's clause may carry `stage: <n>` (default: every stage), read by `world_q.clauses_binding` against the Record's current stage (`Record.stages`, matured at MATTER, exists). With it, the second `forbears` row binds after the last stage and the first does not bind in the reserve stage: an offer taken there is no breach." The loader (`data/instruments.py`) refuses an unknown stage (VEN-E "Cost class": "the loader's refusal of an unknown stage"). The two `forbears` rows above gain `stage:` values accordingly at the item's open, from `Record.stages`' labels. "If the key is refused, the fallback is two forms (`condotta`, `condotta_reserve`) and a `covenant` at the turn; the story survives, the single document does not."
  4. "**Arrears** need no edit: the employer's missed `due` is a breach in the captain's `kept`; his `release` then costs him no regard …, and the next acts of a released captain and his men are the chooser's: `oblige` elsewhere, or `requisition` at the settlement he resides in." (The source's size word for the captain's men is replaced: the MB lexicon's no-size-word rule.)
  5. Edit 5b: "**The works' wage**: the yard seat D authors carries `upkeep: 2` (twice the fixture default; sweep {1, 2, 3}; owner the row), so its establishment is the costliest standing charge on its chest." Listed for Jordan in the PR body (D-19).
- WHERE: `engine/season/instruments.yaml` (`forms`: `condotta`); `engine/season/data/instruments.py` (the clause key `stage`, its refusal); `engine/season/queries/world_q.py` (`clauses_binding`: the stage branch); `engine/season/offices.yaml` (the yard seat's `upkeep`); `engine/season/tests/test_inst_ven_e.py`.
- TESTS: in `test_inst_ven_e.py`, first, red (no `stage`): `test_a_rival_oblige_in_the_bound_stage_is_a_breach`, `test_the_same_oblige_in_the_reserve_stage_is_not`, `test_a_march_on_the_employers_ground_after_lapse_is_a_breach`, `test_an_unknown_stage_is_refused_at_load` `[ASSUMPTION: test names; the item creates them]`.
- FALSIFIER and CONTROL: "For 'the reserve stage is a real window': gate 4's planted failure not reddening." Control (VEN-E gate 1): with the form unused, the realm hash at seed 0, one season, equal to the previous item's.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_e.py engine/season/tests/test_instruments.py -q` → pass. VEN-E gate 4: "a hand-built fold over three stages: in the bound stage a rival `oblige` deposits a breach in the employer's `kept`; in the reserve stage it does not; after lapse a `march.declared` on the employer's ground does. Planted failure: remove `stage` from the first `forbears` row and the reserve-stage case deposits a breach." (A fold over constructed ticks, no season run: U14.)
- HASH MOVERS: the yard seat's `upkeep` moves every seeded run that charges its chest; `condotta` moves nothing until a `covenant` of that form is made. Declared; B40.99.
- DEPENDS ON: V12 Batch B32 (COL-A, SYN-A: `forms:`, `dues`, `kept`, `world_q.clauses_binding`, the `covenant` mint); V12 Batch B33 (VEN-D: the yard seat; the captain's `oblige`, "as D §1 has it"); EXISTS-IN-TREE `state/carriers.py` `Record.stages`.
- GLOSSARY: row *condotta* (if absent): "condotta: a hired captain's contract with an employer, in a bound stage then a reserve stage, as the Italian *condotta* was" (STAGES rule 3: a new word with its owner, `instruments.yaml: forms`).
- COST and TIER: small build (one clause key, one reader branch, the loader's refusal) and content; `sonnet`, `high`; one `opus` read of gate 4.
- LANDS IT: B40's producer; `Item: B40.18`, `[skip ci]`.

### B40.19 — the pledge; the merchants' court · VEN-E edit 6 · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 6 — the pledge; the merchants' court (M-10, M-11)", "Exact edits" row 6, "Gate" 5, 6; D-5 ("there is no lien and no creditor verb; possession is the security").
- ADVANCES: none of the nine; credit with a security and a second forum.
- INSTRUCTION (VEN-E, copied):
  1. "**The pledge is composed and needs no edit.** At the making of a `debt` the debtor `give`s the creditor a bearer instrument he holds; at discharge the creditor `give`s it back … The chooser must be able to *form* the pair, which is `14_VERBS_SOCIAL2_A`'s formation rule (an act forms on what the actor holds and knows); this edit adds a gate that it does."
  2. "**The merchants' court.** One row beside proposal B's `debt_suit`:
     ```yaml
     - id: guild_debt_suit           # the same matter before the guild's own bench, in its own hall
       # every key as proposal B's `debt_suit` (opened at 15_INSTITUTIONS_VENICE_B edit 6), except:
       venue_min_rank:  hearth       # sits in the guildhall, not the town's court
       disposal_reach:  body         # the judgment is heard by the guild, not the settlement
     ```
     The thirteen keys have no key that names a bench by body; a bench is `bench_basis: determine` read at the venue. So the guild's bench is the `determine` seats that sit at the guildhall: the row needs one guild seat with `determine` in its remit anchored there (`rung: {venue: "<guildhall>"}`, D's anchor form), which this edit adds beside D's `off_house_*` rows." The row copies `debt_suit`'s keys from `arrangements.yaml` at the item's open (no key invented).
  3. Site (VEN-E's `[UNVERIFIED]`, §5.7 SITE): open the judging set the hearing uses (`state/gate.py::judging_set` is not in the tree at `9c2c3ab`; read whatever B24 or B27 landed for "the judging set at a venue") and record whether a hearth venue's set leaves out the commune's `determine` seats "whose purview contains that hearth by containment". If it does not, "the two benches have the same members and this row is held until SC's venue work can tell them apart": the row is not added, the guild seat is, and the commit says so.
- WHERE: `engine/season/arrangements.yaml` (`guild_debt_suit`); `engine/season/offices.yaml` (one guild seat with `determine`, `{venue:}` anchor); `engine/season/tests/test_inst_ven_e.py`.
- TESTS: in `test_inst_ven_e.py`, first: `test_the_two_benches_band_shares_differ_with_spread` (gate 6) and `test_a_pledge_folds_given_discharged_returned_and_given_lapsed_kept` (gate 5's hand-built case) `[ASSUMPTION: test names; the item creates them]`.
- FALSIFIER and CONTROL: "For 'the research's shape transfers at all': if, on the Counting-House fixture, no chooser in any seed ever takes a pledge, hires in reserve, sues in the guild's court or opens an audit, the mechanisms are expressible and unplayed, and the finding is about the chooser's candidates (CHAR's `02_CHAR_offer_what_can_be_done.md`), not about this batch." Control: `debt_suit` unchanged; the realm hash with the two rows absent equal to the previous item's.
- GATE (`PYTHONHASHSEED=0`): `python -m pytest engine/season/tests/test_inst_ven_e.py -q` → pass: gate 6, "400 seeded `determine` draws of one hand-built suit before each bench; the band shares differ and both have spread" (`assert checked >= 400` per bench); gate 5, "on the Counting-House fixture, seeds 0 to 2, twelve seasons, count `debt` mintings in whose season the debtor `give`s the creditor a bearer instrument. The gate is that the count is reported and that at least one hand-built case folds (given, discharged, returned; given, lapsed, kept). If the seeded count is zero in all seeds, that is recorded as a formation gap for the SOCIAL verb lane, not hidden." — the seeded count at **two seasons** ("twelve" in the source; A-114), `institution INST-VENICE-01 2 s`, s = 0 to 2.
- HASH MOVERS: the realm build hash (the guild seat); every seeded run with a guild suit. Declared; B40.99.
- DEPENDS ON: V12 Batch B33 (VEN-B: `debt`, `debt_suit`, `world_q.owed`; VEN-D: the guildhall, `off_house_*`, the `{venue:}` anchor, `INST-VENICE-01`); V12 Batch B25 (`14_VERBS_SOCIAL2_A`: formation on what is held and known); V12 Batch B24 (the hearing's bench at a venue); V12 B40.14 (`offices.yaml`, its rows first).
- GLOSSARY: none.
- COST and TIER: edit (content) and a gate; `sonnet`, `medium`; one `opus` read of gate 6's two band tables.
- LANDS IT: B40's producer; `Item: B40.19`, `[skip ci]`.

### B40.20 — the outside assent; the brotherhood · VEN-E edit 7 · BUILD · HASH MOVER(behaviour)
- SOURCE: VEN-E "Edit 7 — the outside assent; the body of the excluded (M-12, M-13)", "Exact edits" row 7; A-14 (a body's assent is a ballot of draws on its members).
- ADVANCES: none of the nine; a guild statute binds the town only by a justice's answer; a release valve for the excluded (narrowed, VEN-E's NERS).
- INSTRUCTION (VEN-E, copied):
  1. "**The outside assent is composed, on one condition of anchoring.** A guild's statute is an `issue` through its head seat. Where that seat is anchored at the guildhall (a `hearth`, D's `{venue: …}` form), its purview is the hall and, one edge deep, its sworn members (`purview_reaches`): the statute addresses members only. To bind the town it must be `issue`d through a seat whose purview contains the town, so the guild's head `petition`s the commune's justice seat (edit 1) and that holder's answer (issue it, issue it altered, refuse) is the ratification: an ask, rolled, with `obligation` as a level and `regard` as a term. No row and no key. **The condition:** D anchors `off_guild_roll` at `{duchy: "Hafenmark"}`, whose purview by containment is every Hafenmark settlement; a statute issued through *that* seat needs no assent. This edit therefore asks one content decision of D's rows: the guild's **rule-making** remit (`issue`) sits on the hall's head seat, and the duchy-anchored roll seat keeps only the warrant. `[ASSUMPTION; Jordan or FA to correct: it narrows a remit D authored.]`" The edit: `off_guild_roll`'s `remit_acts` loses `issue`; the guildhall head seat's gains it. Listed in the PR body.
  2. "A brotherhood: one `community`-rung body in `office_bodies` (`"Brotherhood"`, faction as its town's), a list seat by warrant, a head seat `conferral: elected`, `term: 4`, a `tables.eligible_from` entry naming its own list, `remit_acts: [issue, convene]`, an establishment and a chest as any house. Three rows. Nothing ties it to the council; that is the point." The town is VEN-D's republic town, read at the item's open.
- WHERE: `engine/season/offices.yaml` (`off_guild_roll`'s remit; the hall head seat's remit; the brotherhood's list and head seats); `engine/season/rosters.yaml` (`office_bodies`: `"Brotherhood"`; `tables.eligible_from`: one entry).
- TESTS: none new.
- FALSIFIER and CONTROL: a statute issued through the hall seat addresses a non-member of the town (the anchoring condition failed). Control (VEN-E gate 1): the rows absent, the realm hash at seed 0, one season, equal to B39's close.
- GATE (`PYTHONHASHSEED=0`): `build_realm(0)` builds; a one-line script over `purview_reaches` → the hall head seat reaches the hall and its sworn members and not the town's other residents; `off_guild_roll`'s remit no longer holds `issue`; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: the realm build hash (the brotherhood's seats; the moved remit changes which `issue` candidates form). Declared; B40.99.
- DEPENDS ON: V12 Batch B33 (VEN-D: `off_guild_roll`, the guildhall's head seat, the `{venue:}` anchor); V12 Batch B32 (VEN-A: `obligation` as a level; VEN-C: `tables.eligible_from`, `conferral: elected`); EXISTS-IN-TREE `state/gate.py::purview_reaches`; V12 B40.14 (the commune's justice seat, edit 1).
- GLOSSARY: none.
- COST and TIER: edit (content); `sonnet`, `medium`.
- LANDS IT: B40's producer; `Item: B40.20`, `[skip ci]`.

The batch continues at B40.21 in this part's continuation file (`_cont`). Last item written in this file: B40.20.

