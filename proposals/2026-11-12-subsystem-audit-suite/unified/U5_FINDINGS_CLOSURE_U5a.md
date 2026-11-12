# U5a — findings closure: CORE, CHAR, DICE, tests, census (with the determinism sweep)

## Status: REFERENCE (a closure ledger for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: 601e715 (working tree), 2026-11-12. Closing lane: Fable unification-closure, family U5a.

**What this file is.** Every finding, resolution row, survivor and census row in the U5a documents ends here
with exactly one disposition (UNIFICATION_BRIEF.md, "Closure"). Dispositions:

| code | meaning |
|---|---|
| **RESOLVED-BY** | a proposal in `proposals/` carries the exact edit at the single owner and a gate (file and section named) |
| **SUPERSEDED** | a later finding or decision replaces it (cited) |
| **STALE-FALSE-POSITIVE** | the audit's own later evidence, or the tree at HEAD, shows the finding does not hold |
| **DISPUTED** | this lane's evidence is against it; the finding stays in its document, marked |
| **JORDAN** | survives the five-step ladder; two options stated |

**Resolve is a plan, not an edit.** Nothing here is executed against code, registries or canon. A carrying
proposal is an ordered set of instructions for a later implementation lane; where a finding had no carrying
proposal this lane wrote one under `proposals/U5a_*.md`.

**Scope read (second reader, in full).** `audits/01_CORE_audit.md`, `01_CORE_audit_addendum_B.md`,
`01_CORE_audit_addendum_C_tests.md`, `02_CHAR_audit.md`, `02_CHAR_audit_addendum_B.md`, `10_DICE_audit.md`,
`10_DICE_audit_addendum_B.md`, `16_PESSIMIST_{CORE,CHAR,DICE}.md`, `17_CENSUS_{C1A,C1B,REST}.md`,
`18_DETERMINISM_SWEEP.md`, `digests/DG_tests1..6.md`, and every proposal named `01_CORE_*`, `02_CHAR_*`,
`10_DICE_*`, `16_PESSIMIST_{CORE,CHAR,DICE}_*`, `17_CENSUS_*`, `18_DETERMINISM_*`. Coverage notes and
anything not checked are at the end (§Z).

**Companion files.** Conflicts decided: `unified/U5_CONFLICTS_U5a.md`. The one capability authoring
architecture: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`. New carrying proposals:
`proposals/U5a_*.md`.

**Reading the tables.** "Proposal" names a file under `proposals/` of this suite unless a path is given;
"§" is that file's own section. "Evidence" is the audit's citation as re-read by this lane, not re-run
(no pytest and no code edit in this stage); a row whose evidence this lane could not re-read is marked
`[not re-opened]`.

---

## Carriers that are not suite proposals

Two kinds of carrier appear below beside suite proposals, each for a stated reason:

- **A position of the active master workplan** (`workplans/valoria_master_workplan_v11*.md`: IN-14, CR-07,
  CR-08, CR-98, NM-W9, IN-44, SC-P2's kernel retirement). CLAUDE.md §2 allows one active plan per lane and
  forbids an item sitting in two plans, so where the audit's fix *is* an existing position the closure cites
  the position and the suite adds only its input (a precondition, a measurement, a Layer-1 ground), written
  in `proposals/U5a_CORE_owed_edits.md`. No second schedule is created.
- **`proposals/U5a_CORE_owed_edits.md`**, written by this lane: the resolutions the CORE audits decided as
  "an edit to the row / the site" with no proposal file, gathered as one ordered, executable plan.

---

# PART 1 · CORE

## 1.1 `audits/01_CORE_audit.md` — findings

| id | claim (one line) | disposition | carrier (file · section) | evidence |
|---|---|---|---|---|
| F-CORE-01 | the log is mostly memory-fade bookkeeping; cost grows with history | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` · Edits 1–5, Gate | growth probe, seed 0, 8 seasons: `claim.decayed` 938 of 1,164 new entries in season 7 (audit §3, §12). Pessimist re-read on the realm: 34,837 fades in three seasons (`16_PESSIMIST_CORE.md` §1.4). Residue accepted, not a finding: the `claim.deposited` half (35,115) stays, it is `loop/witness`'s declared emission (`04` §A.2) and readers filter by kind |
| F-CORE-02 | the corpus runs one template 143 times and checks no case need | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` · Resolution, Edits 1–5 | `corpus_run` seed 0: `RUNS-UNDECLARED 103 · SPAN-UNAUTHORED 40`; `exercises`: 35/292 NPC, 0/611 ARC |
| F-CORE-03 | THE NINE's statuses are strings; R-01/R-02 `met` lack a control | RESOLVED-BY | record shape: `01_CORE_requirements_reading_record.md` §1. R-01/R-02 measure: `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` edits 2–3 (the knockout arm), with `01_CORE_tests_shipped_world_falsifiers.md` rows 1–2 as the standing tests. The reading record's own §2 (`chronicle --propagation`) is reconciled away: conflict C-U5a-01 | `register.py:631-701` executes nothing; the pessimist's knockout arms read 0 / 0 / 236 / 309 / 634 (a null, a dose order, a ceiling) |
| F-CORE-04 | in computed play 72 % of graded acts fail and almost nothing is told | RESOLVED-BY | core's share: `01_CORE_case_setup_and_beats.md` (cast capability in `setup:`); the capability cause: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §5 (the five undeclared contested rows) and `01_CORE_capability_authoring_surface.md` Edit 8; the telling share is SC's (U5c) and is cross-listed only | corpus seed 0: Failure 1,552 of 2,152; `told_by` 64 of 93,760; addendum B C4 adds three causes |
| F-CORE-05 | the play surface is a seam with no client | RESOLVED-BY | `11_GO_player_surface_contract_B.md` §8 (the transcript runner in `harness/play_surface.py`); stop conditions added by `U5a_CORE_owed_edits.md` §F; the single-scene entry: `01_CORE_one_scene_contract.md` Edit 4 | no `input(` under `engine/season`; `dispatching_chooser` has test callers only |
| F-CORE-06 | the round count caps a budget the design varies by office | RESOLVED-BY | workplan IN-14 (B10-16, delegated-ruled); suite input `U5a_CORE_owed_edits.md` §H | `driver.py:479`, `deliberate.py:287`. Layer-1 note: the office term departs from `04` §A.3 row 15 by a ledgered revert (`ED-IN-0246`, HANDOFF_IN "Build-order item 4 REVERTED"); not re-raised |
| F-CORE-07 | the contest depth cap decides nothing | RESOLVED-BY | `U5a_CORE_owed_edits.md` §A row 1 (strike H-87's sweep as a fake control; keep the signature, `04` D-19) and §B row 4 (`_contest` emits on `ContestError`) | hash identical at depth 1, 2, 3, 7 (seed 0, 2 seasons) |
| F-CORE-08 | size: the mechanism is proportionate, the prose is not | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B rows 1–3 (the four stale comments). The rest is accepted with no artifact: per file touched for another reason, no sweep, no guard (CLAUDE.md §0.1 pt 5) | `sloc.py`: 13,982 executable game lines; four stale claims cited at their lines |
| F-CORE-09 | per-access scans on the hot path; `TRACE` grows unbounded | RESOLVED-BY | `U5a_CORE_owed_edits.md` §C | `world.py:455-471`; pessimist E-04 was OOM-killed holding `TRACE.rows` (corroboration; cause not isolated) |
| F-CORE-10 | the seam reads provider results by key presence; combat seeds its own generator | RESOLVED-BY | typed outcomes: `03_PC_typed_outcome_one_door.md`, `04_MB_typed_outcome_and_one_path.md` (U5b's files, cited by title; bodies not opened by this lane); the generator: `11_GO_one_draw_owner.md` (U5d's, title only). The audit's own decision stands until those land: no `ContestResult` type before a fourth provider shape | `seam/ladder.py:247-264`; `seam/wrappers/combat.py:388-397` |
| F-CORE-11 | two gate conformance gaps (H-145 closure-write receipt; H-220 no kind check at append) | RESOLVED-BY | H-220: `U5a_CORE_owed_edits.md` §E row 2. H-145: workplan NM-W9 (B10-19, HELD), which `16_PESSIMIST_CORE_the_record_holds_what_changed.md` Edit 1 leaves to that row by name | `world.py:1394-1395,1494`; `log.py:64-101` |

## 1.2 `audits/01_CORE_audit.md` §6.1 — hole-register and workplan rows

Rows the audit verified or carried with **no action** are not open claims and are grouped; a row with an
action is closed by the resolution that carries it (§1.3).

| rows | audit's verified status | disposition | carrier / reason |
|---|---|---|---|
| H-01, H-02, H-50, H-81, H-83, H-86 | closed in code | STALE-FALSE-POSITIVE (as open items) | evidence at the cited lines; no action |
| H-06, -07, -08, -09, -11, -26, -93, H-20, -74, -80, H-29, -53, H-39, H-76, -77, -78, -124 | open by design (declared, swept fixtures) or carried | STALE-FALSE-POSITIVE (as findings of this audit) | carried unchanged; each row's own `site:`/`sweep:` is its record |
| H-23, -28, -35, -36, -37 | ruled, binding | STALE-FALSE-POSITIVE (not re-raised) | AUDIT_BRIEF ground rule 6 |
| H-10 | open, live | RESOLVED-BY | F-CORE-06's carrier (IN-14) |
| H-12 | closed; cause of F-CORE-01 | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (the ruling is kept: the write is removed, not the emission rule) |
| H-24, H-30, H-47, H-48, H-56, H-59, H-82 | misgraded / wrongly filed / superseded / empty cite | RESOLVED-BY | `U5a_CORE_owed_edits.md` §A rows 2–8 |
| H-25 | open | RESOLVED-BY | workplan CR-98 (B11-F2) with F-CORE-21's input, `U5a_CORE_owed_edits.md` §D |
| H-44, H-109, H-254, H-344, H-153, H-154, H-63 (`speak`'s values) | other lanes' mechanisms | SUPERSEDED | by the owning lane's closure (FA: U5d; SC: U5c); cross-listed only |
| H-49 | open: `(Person, weight)` has no runtime writer | SUPERSEDED | by workplan CR-08 (B10-18, STATE BUILD: the CENSUS writer). The audit's resolution 13 (mark the row `unproduced`) contradicts that decided position and is withdrawn: conflict C-U5a-02 |
| H-52, H-57, H-61 | closed by IN-43 | STALE-FALSE-POSITIVE | carried |
| H-75 | open: `hold:<kind>` placeholder declines | STALE-FALSE-POSITIVE (no row needs it today, `[UNVERIFIED]` in the audit) | returns with the first row that needs it |
| H-89, CR-07 | open; the `scale:` column has no reader | RESOLVED-BY | workplan CR-07 (B10-Z, HELD on its pre-flight) with the precondition and Layer-1 ground in `U5a_CORE_owed_edits.md` §E row 3 |
| H-145, H-220 | open | RESOLVED-BY | as F-CORE-11 |
| B10-18b (CR-46…CR-54) | open; base figure stale | RESOLVED-BY | the card's own order (CR-46 re-reads first); the audit's figure (23 of 67 executed, seed 0) is the input, `U5a_CORE_owed_edits.md` §A row 9 |
| IN-14, CR-98, CR-99, NM-W9 | open | RESOLVED-BY | their workplan positions; inputs as above |
| IN-18, IN-44, IN-58, IN-30, IN-32, IN-36, IN-48, IN-52, CL-MGMT, CR-95, CR-97, CR-100…105, NM-W4…W8 | carried, not opened | STALE-FALSE-POSITIVE (as findings) | the audit made no claim about them |

## 1.3 `audits/01_CORE_audit.md` §6.2 — resolutions 1–22

| # | resolution | disposition | carrier |
|---|---|---|---|
| 1 | fading becomes a read | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` |
| 2 | typed `setup:` / `beats:` per case | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` |
| 3 | integer `span_seasons` plus `ongoing:` | RESOLVED-BY | same · Edit 5 |
| 4 | the runner seats a declared policy proxy | RESOLVED-BY | same · Edit 4 |
| 5 | one typed `reading:` per row | RESOLVED-BY | `01_CORE_requirements_reading_record.md` §1 |
| 6 | R-01/R-02 re-pointed to a reading with a planted control | SUPERSEDED | by the knockout reading (`16_PESSIMIST_CORE_the_nine_gate…` edits 2–3) and the realm tests (`01_CORE_tests_shipped_world_falsifiers.md` rows 1–2); C-U5a-01 |
| 7 | R-05's figure follows the tree | RESOLVED-BY | `01_CORE_requirements_reading_record.md` §1 (the example row) |
| 8 | depth cap: keep the refusal, strike H-87's sweep | RESOLVED-BY | `U5a_CORE_owed_edits.md` §A row 1 |
| 9 | H-30 regraded `measured` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §A row 2. Note: the pessimist measured that this order decides about 1 act in 175 (F-PES-CORE-09); the regrade's cite carries that figure |
| 10 | H-47 refiled: row present, producer absent | RESOLVED-BY | §A row 3 |
| 11 | H-48 closed as never built | RESOLVED-BY | §A row 4 |
| 12 | H-59 closed, superseded by H-57 | RESOLVED-BY | §A row 5 |
| 13 | H-49: mark the matrix row `unproduced` | SUPERSEDED | by workplan CR-08 (the CENSUS writer is the decided build); C-U5a-02 |
| 14 | H-56's held half closed as irrelevant until nesting exists | RESOLVED-BY | §A row 6 |
| 15 | H-82 regraded `measured` | RESOLVED-BY | §A row 7 |
| 16 | H-24's cite filled | RESOLVED-BY | §A row 8 |
| 17 | four stale comments corrected | RESOLVED-BY | §B rows 1–3 |
| 18 | `World._subsistence_shortfall` initialised and described truly | RESOLVED-BY | §B row 5 |
| 19 | `sigma.resolve` refuses when handed no `rng` | RESOLVED-BY | §B row 6 (with addendum B C5's second site, `modules/combat/wrapper.py:565`, named for the PC lane) |
| 20 | `_contest` emits the refusal on `ContestError` | RESOLVED-BY | §B row 4 |
| 21 | retire the `scale:` column | RESOLVED-BY | workplan CR-07; `U5a_CORE_owed_edits.md` §E row 3 |
| 22 | a headless play loop | RESOLVED-BY | `11_GO_player_surface_contract_B.md` §8; `U5a_CORE_owed_edits.md` §F |

## 1.4 `audits/01_CORE_audit.md` §11 — survivor

| survivor | disposition | carrier | reasoning |
|---|---|---|---|
| the fading of memory: a logged write per claim (B: one aggregated `ledger.faded` per person per season) or a read (A) | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (Option A) | Does not survive the ladder. Step 4: the tree's own precedent (a crossing emits, a level does not; L5). Step 5 and Layer 1 itself: `04` §G.2.5, a recomputable value is not stored. No Layer-1 row is overwritten: H-12's ruling (a MATTER *write* emits) is kept because the write is removed, and D-39's comparator signature is unchanged. Option B stays in the proposal as the named revert |

## 1.5 `audits/01_CORE_audit.md` §13 — provided arcs and characters

| case(s) · need | disposition | carrier |
|---|---|---|
| all 143 · the case's own cast, seats, relations, records exist | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` (`setup:`) |
| all 143 · each `season_requires` need is checked by a run | RESOLVED-BY | same (`beats:` with an off-arm) |
| all · one person's act is cited by another's later Event | STALE-FALSE-POSITIVE (not a gap: represented) | corpus R3 143/143; the realm reading 134 / 141 / 162 against 0 (addendum C §3) |
| all · persons hold different things | STALE-FALSE-POSITIVE (represented, structurally) | `carriers.py:504-509` |
| cases turning on being *told* | SUPERSEDED | by SC's and CHAR's closures (U5c; PART 2 here for the chooser's share) |
| ARC-44, EMG-C4, EMG-C3, EMG-X8, ARC-20 · long spans | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` Edit 5 (lift `MAX_SEASONS`) |
| 86 cases · prose spans | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` Edit 5 |
| 26 cases · `needs_deadline` | RESOLVED-BY | same (`setup.dates`) |
| 91 cases · `ends_when` | RESOLVED-BY | same (a terminal beat); endings that are binding decisions are FA's (U5d) |
| 52 cases · `ends_when: never` | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (affordability) |
| 16 cases naming a player | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` Edit 4 |
| NPC-088 · labour ripening over seasons | STALE-FALSE-POSITIVE (represented) | headless run: `record.created` 4, `term.matured` 5 |
| NPC-088 · possession has consequences `[UNVERIFIED]` | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` Edit 5 (NPC-088 is the first case given `beats:`; the need is read there) |
| memory across seasons | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` |
| arcs ending in a ruling, a battle or a duel | SUPERSEDED | by FA, MB, PC closures (U5d, U5b) |
| all · persons differ in what they can do | RESOLVED-BY | `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (cast rows) with `01_CORE_case_setup_and_beats.md` (`setup.cast.capability`) |
| needs wrongly stated: prose spans; `UNCLEAR:` rows | RESOLVED-BY / STALE | spans: as above; `UNCLEAR:` rows are the source's own admission and stay unrouted (no claim to close) |

## 1.6 `audits/01_CORE_audit_addendum_B.md` — findings F-CORE-12 … F-CORE-23

| id | claim (one line) | disposition | carrier (file · section) | evidence |
|---|---|---|---|---|
| F-CORE-12 | the reason for an act (occasion, on whose behalf, deciding term) is not in the world | RESOLVED-BY | `01_CORE_reason_trail_in_the_act_store.md` Edits 1–5 (occasion, stored with the Scene); the deciding term: `02_CHAR_reason_trail_and_small_edits.md` Part A (`watch`) | `probe_reason.py`: driver holds 8/18/28 Scenes; 4 act Events cite the act alone. Made more urgent by `16_PESSIMIST_CORE.md` §1.2 pt 3 (an uncited scene still changes 236 acts) |
| F-CORE-13 | one module is a playable scene, three are calls | RESOLVED-BY | `01_CORE_one_scene_contract.md` Edits 1–4, reconciled with `11_GO_player_surface_contract_B.md` §6 (C-U5a-03) and `05_SC_playable_hearing_B.md` edit 4 (C-U5a-04) | `seam/wrappers/combat.py:394-395`; `mass_battle.py:361-363` |
| F-CORE-14 | a governance refusal cannot say which clause refused; four predicates crash on a list operand | RESOLVED-BY | `01_CORE_predicates_name_their_clause.md` Steps one and two | `probe_predicates.py`: four `TypeError`; 21 bare `return False` |
| F-CORE-15 | the capability a roll reads has one reader and six authors | RESOLVED-BY | `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (the decided home and schema); `01_CORE_capability_authoring_surface.md` Parts one and two as reconciled there | inline census: 11 contested verbs, 9 with a capability row; Endurance default 1 / 4 / 4 |
| F-CORE-16 | the verb table's `scale:` column is refused by Layer 1 in terms | RESOLVED-BY | workplan CR-07 (B10-Z, HELD); precondition and order in `U5a_CORE_owed_edits.md` §E row 3 | `04` §A.3 row 4, §B.13 #10; 15 rows carry the key at this tree (the workplan entry says 13 and says "the count drifts"); CR-07's own pre-flight: `Act.via.scope` missing on 19 of 309 acts through one seat, `off_npc_084` |
| F-CORE-17 | a refusal is priced and the price leaves no receipt (`04` D-51's falsifier fails) | JORDAN | J-U5a-03 (`unified/U5_CONFLICTS_U5a.md`); the register refile is `U5a_CORE_owed_edits.md` §A row 10 | `probe_refusal_receipts.py`: 27 refusal Events, 0 with `changes[]`. Two Layer-1 sources decide it differently (`04` D-51 wants a debit receipt; #353 `:877`, `:912-913`, ruled at H-28: budget is a Query, "without anybody storing a number") |
| F-CORE-18 | a verb's facts live in its row and in fourteen rosters keyed by verb | RESOLVED-BY | the capability roster: U1 architecture §3 (a `capability:` column on the verb row); the declines: `02_CHAR_offer_what_can_be_done.md` (F-CHAR-11) | `data/verbs.py:1191-1895`; fourteen loaders for twenty-seven facts |
| F-CORE-19 | stale counts and claims at the owners; S27.4's second site | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B rows 7–12 | lines cited in the finding |
| F-CORE-20 | a need propagates to the one who could meet it and is not met | RESOLVED-BY | `01_CORE_unmet_need_is_attended_first.md` (attention order) with `02_CHAR_goal_lean_on_its_own_question.md` (the ranking's half); the joint gate is in the first file | `harness.scarce`, seed 0, four seasons: no relief unassisted; ordering experiment gives relief at 1 of 3 seeds |
| F-CORE-21 | the loop check passes on six cycles of 39,482 and cannot see the loops that run away | RESOLVED-BY | workplan CR-98 (B11-F2) with the input in `U5a_CORE_owed_edits.md` §D | `harness.loops`: +4, −2, ?39,476 |
| F-CORE-22 | `arms` cannot tell a null from a fake control | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B row 13; the dead pair leaves by `01_CORE_tests_delete_what_cannot_fail.md` row 5 | `arms.py:288-310` prints no count of fought fields |
| F-CORE-23 | the provided corpus is loaded through a repair routine and one case is gone | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B rows 14–15 | `load_cases`: 8 defects; `ARC3.yaml` recovered 0 rows |
| (corroboration) | `interactions.py` works around F-CORE-12/14; `run_cases.grade` says `PLAYABLE` for "declared tokens resolve" | RESOLVED-BY | F-CORE-12 and F-CORE-14's carriers; the rename: `U5a_CORE_owed_edits.md` §B row 16 | `interactions.py:250-251`; `run_cases.py::grade` |

## 1.7 `audits/01_CORE_audit_addendum_B.md` §3 — corrections C1 … C8

| # | correction | disposition | carrier / note |
|---|---|---|---|
| C1 | four driver attributes are cumulative by design | RESOLVED-BY | `01_CORE_reason_trail_in_the_act_store.md` (moves `scenes`; `resolved`, `act_of` stay, derivable). The first audit's §1.1 sentence is marked superseded by this correction |
| C2 | `DevelopmentSheet` body verified; shows no attributes or odds | RESOLVED-BY | `01_CORE_capability_authoring_surface.md` Edit 6 (attributes); odds and terms: `11_GO_player_surface_contract_B.md` (`Offer`) |
| C3 | provider return: two rows of `04` disagree; code follows the later ruling | SUPERSEDED | by the 2026-09-03 ruling and `ED-IN-0279` (ladder step 1); `04`'s marker is workplan IN-44's (B10-Z). B4 third disposition, named at `seam/ladder.py:151` |
| C4 | three further causes of the default pool | RESOLVED-BY | U1 architecture §5–§6 (undeclared rows; cast rows); `02_CHAR_capability_definitions.md` for the cast content |
| C5 | a second unseeded-generator fallback at `modules/combat/wrapper.py:565` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B row 6 (season side) ; the module line is PC's (U5b), named there |
| C6 | retiring `scale:` is a conformance edit | RESOLVED-BY | as F-CORE-16 |
| C7 | an end a player can read exists in design, half in code | RESOLVED-BY | `U5a_CORE_owed_edits.md` §F |
| C8 | `choose` receives the live `Person`, not a frozen `PersonInterior` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 1 (with F-CHAR-12, PART 2) |

## 1.8 `audits/01_CORE_audit_addendum_B.md` §4 — Layer-1 reading (rows that depart)

Rows the addendum read as *conforms* need no closure. The departures:

| spec row | reading | disposition | carrier |
|---|---|---|---|
| §B.2 row 2, §C.3 frozen `PersonInterior` | departs | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 1 (change the code; B4 default) |
| §A.3 row 15 no office bonus | departs, ledgered | SUPERSEDED | `ED-IN-0246` and HANDOFF_IN's "Build-order item 4 REVERTED"; IN-14 is delegated-ruled. Not re-raised. `04`'s marker is IN-44's |
| D-51 a refusal Event carries the debit's receipt | behaviour holds, construction does not | JORDAN | J-U5a-03 |
| §B.13 #7, D-25 the log accepts no kind off the derived roster | departs at `EventLog.append` (H-220) | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 2 |
| §B.13 #10, §A.3 row 4 `scale:` | departs | RESOLVED-BY | workplan CR-07; §E row 3 |
| §C.5, D-24 against §C.4 (provider returns) | two spec rows | SUPERSEDED | as C3 |
| §C.12 rejection 5 (refusal as a returned value; PROPOSED) | 586 `raise` in non-test `engine/season` | STALE-FALSE-POSITIVE (a reading, not a departure: the row is PROPOSED) | the count is carried to the GO lane's port-cost reading (U5d); no edit here |
| §4.4 typed outcome on two of four providers | departs | RESOLVED-BY | as F-CORE-10 |
| §4.4 no standalone entry | gap | RESOLVED-BY | `01_CORE_one_scene_contract.md` Edit 4 |

## 1.9 `audits/01_CORE_audit_addendum_B.md` §5 (d), §6 (c), §7 — tables with no finding number

| item | disposition | carrier / reason |
|---|---|---|
| §5 (d) a first rank in a skill is worse than none | RESOLVED-BY | U1 architecture §4 (`untrained:`); `01_CORE_capability_authoring_surface.md` Edit 9 |
| §5 (d) five of eleven contested rolls name no capability | RESOLVED-BY | U1 architecture §5; same file Edit 8 |
| §5 (d) attribute plus skill / attribute caps skill | STALE-FALSE-POSITIVE (ruled: CR-20, the larger of the two) | accepted |
| §5 (d) no derived resource from an attribute on the season side | SUPERSEDED | PC's and CHAR's closures (`02_CHAR_scar_is_a_wound.md` for the body; U5b for the module) |
| §5 (d) traits, talents, flaws have no carrier | RESOLVED-BY | U1 architecture §2 (`kind: trait` is a closed-set member with no reader until a use row names one; no trait system is invented) |
| §5 (d) skill atrophy | STALE-FALSE-POSITIVE (the audit: "none worth building now") | no action |
| §5 (d) opposed roll | STALE-FALSE-POSITIVE (ruled 2026-08-14: static opposition) | accepted |
| §5 (d) help, teamwork, tools | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` (the roster's second members) |
| §5 (d) a capability gates an action | JORDAN | J-U5a-01 |
| §5 (d) derived statistics | SUPERSEDED | CHAR's closure (PART 2) |
| §6 (c) four narrowings of the chooser's field (`withheld_verbs`, the once-per-season filter, `question_aggregation_rule: first`, `scenes_per_round: 1`) | RESOLVED-BY | `withheld_verbs`: workplan B10-18b CR-52/CR-53; the aggregation: `01_CORE_one_scene_contract.md` Edit 5 (the player is shown all his questions); the other two are declared swept fixtures and carry no finding |
| §7.1 the slate (design) against the per-person question (code) | RESOLVED-BY | resolution 20, same Edit 5 |
| §7.1 Domain Echo tables | SUPERSEDED | by Layer 1 §B.6.1 (no stored aggregate); resolution 21 |
| §7.1 "Where were you?" retrospective scenes; progressive revelation; `explain` unbuilt | SUPERSEDED | `11_GO_player_surface_contract_B.md` (`account`, `receipt`) is the carrier (U5d); the core's share is F-CORE-12 |
| §7.1 end of a life | RESOLVED-BY | `U5a_CORE_owed_edits.md` §F |
| §7.1 RNG-1 | RESOLVED-BY | §B row 6 |
| §7.1 termination across seasons | RESOLVED-BY | CR-98, §D |
| §7.2 forked resolution core unguarded | STALE-FALSE-POSITIVE | the parity golden is asserted by `sim-regression` (addendum §7.2 row 1) |
| §7.2 sixteen "no rng" fallbacks | RESOLVED-BY | §B row 6 (two remain) |
| §7.2 sixteen ladder producers | STALE-FALSE-POSITIVE | one owner at HEAD; three seam ladders ruled |
| §7.2 "the masters exist, the code does not read them" | RESOLVED-BY | does not return for rosters; its falsifier is the capability gate (U1 architecture §8: delete the block and the load must refuse) |
| §7.2 near-identical instances (returning finding) | RESOLVED-BY | F-CORE-02's and F-CORE-15's carriers |
| §7.2 J-1, J-5 (a playable season; choice surfaces) unanswered | RESOLVED-BY | F-CORE-05's and F-CORE-13's carriers |
| §7.2 J-7 emergence made visible | RESOLVED-BY | F-CORE-12's, F-CORE-01's carriers |
| §1 reading: `institution_of` runs for cases with no roster row (`04` G.2.6 shape) `[UNVERIFIED]` | STALE-FALSE-POSITIVE (recorded by its author as a reading, not a finding) | no action |

## 1.10 `audits/01_CORE_audit_addendum_B.md` §8 — resolutions 1–29; §9 — survivor

| # | resolution | disposition | carrier |
|---|---|---|---|
| 1, 2 | Scenes stored in the act store; a standing-occasion act's occasion is the Scene's | RESOLVED-BY | `01_CORE_reason_trail_in_the_act_store.md` Edits 1–3 |
| 3 | the deciding term: CHAR's `watch` hook | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` Part A |
| 4, 5 | one referent read; every refusing branch names its clause; the clause may key the refusal | RESOLVED-BY | `01_CORE_predicates_name_their_clause.md` |
| 6 | frozen `PersonInterior` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 1 |
| 7 | `scale:` | RESOLVED-BY | workplan CR-07; §E row 3 |
| 8 | provider return ambiguity | SUPERSEDED | by ruling; IN-44 |
| 9 | D-51 refiled in the register; build nothing | JORDAN | J-U5a-03 (the refile itself: §A row 10) |
| 10, 11 | one scene contract; a standalone scene runner | RESOLVED-BY | `01_CORE_one_scene_contract.md` |
| 12–15 | capability block; verb-row column; five rows declared; acquisition rule | RESOLVED-BY | U1 architecture; `01_CORE_capability_authoring_surface.md` |
| 16 | Endurance default written three times | RESOLVED-BY | same file, Edit 7; U1 architecture §7 |
| 17 | the told-claim attribute and the Thread-Sensitivity stems are uses | RESOLVED-BY | `02_CHAR_capability_uses_table.md` |
| 18 | stale counts and dead declaration | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B rows 7–11 |
| 19 | the play loop's caller contract | RESOLVED-BY | `11_GO_player_surface_contract_B.md` §8 (it seats `take_ranked`, which cannot exceed budget); §F |
| 20 | the player is shown all his questions | RESOLVED-BY | `01_CORE_one_scene_contract.md` Edit 5 |
| 21 | Domain Echo closed | SUPERSEDED | by Layer 1 |
| 22 | an end a player can read | RESOLVED-BY | §F |
| 23 | unmet need ordered first inside tier 1 | RESOLVED-BY | `01_CORE_unmet_need_is_attended_first.md` |
| 24 | the loop check declares the chooser and the interior writers | RESOLVED-BY | CR-98; §D |
| 25 | `arms` prints fought fields, refuses a z at zero, gains `--fixture` | RESOLVED-BY | §B row 13 |
| 26 | six corpus files normalised; repair path deleted | RESOLVED-BY | §B row 14 |
| 27 | `report.emit`'s `TRACE` import and step list | RESOLVED-BY | §B row 15 |
| 28 | `PLAYABLE` renamed `DECLARED-PRESENT` | RESOLVED-BY | §B row 16 |
| 29 | S27.4's fold arm and `Act.obstacle`/`Act.pool` deleted | RESOLVED-BY | §B row 12; corroborated unexercised by `16_PESSIMIST_CORE.md` §2 |
| §9 | may a capability gate an act? | JORDAN | J-U5a-01 |

## 1.11 `audits/01_CORE_audit_addendum_C_tests.md` — findings and resolutions T-01 … T-22

T1 = `01_CORE_tests_one_golden_owner.md`; T2 = `01_CORE_tests_delete_what_cannot_fail.md`; T3 =
`01_CORE_tests_shipped_world_falsifiers.md`.

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| F-TEST-01 | no test asserts a requirement on a played world at the shipped configuration | RESOLVED-BY | T3 rows 1–3, 8; the red-today falsifiers named there are gates of other proposals (R-04: FA's; R-07 attitude: `02_CHAR_choice_alignment.md`; R-09: U1 architecture §9 gate) | realm probe seeds 0–2: 134 / 141 / 162 against 0 with WITNESS cut |
| F-TEST-02 | one trajectory pinned in six files; 20 of 28 hash tests read a world nobody plays | RESOLVED-BY | T1 A–C | `probe_hash_pins.py` |
| F-TEST-03 | corpus count pins cannot separate a re-roll from a regression | RESOLVED-BY | T1 D | the re-pin log at `test_season_shape.py:9199` |
| F-TEST-04 | two test files whose subject is archived prose | RESOLVED-BY | T2 rows 1–2 | `test_knot_pool_formula.py` green on a formula the code deleted |
| F-TEST-05 | R-07's measure begins with a substring test | RESOLVED-BY | T2 rows 3–4 | reachability probe: `World` reachable from `v` and `ask_budget` |
| F-TEST-06 | the invariant sweep runs on a world with no office | RESOLVED-BY | T3 row 4 | headless: 0 offices; realm: 34 |
| F-TEST-07 | three loops assert on whatever they are handed | RESOLVED-BY | T3 row 5 | `probe_vacuity.py`: `mustered -> []` green |
| F-TEST-08 | the dice golden is 58 % rows the engine refuses or contradicts | RESOLVED-BY | T1 E (ordered after SC-P2's kernel retirement for `TestPoolAwareDegree`) | 1,758 rows, 735 live |
| F-TEST-09 | eight tests assert a substring of source text | RESOLVED-BY | T2 row 3 | §7 table |
| F-TEST-10 | a test keeps a retired symbol importable; a standing non-strict `xfail` | RESOLVED-BY | T2 rows 5–6 (row 6 is MB's file; U5b lands it) | run: `XFAIL` |
| F-TEST-11 | thirteen skips on an absent combat engine | RESOLVED-BY | T3 row 6 | nine sites in `test_season_shape.py`, four other files |
| F-TEST-12 | tests kept green by reverting a shipped change; one escape hatch | RESOLVED-BY | T3 rows 7–9 | `revert_cr87`, `revert_cp_t05_02`, `… or fixed.events == 0` |
| T-01 … T-07 | deletions and the R-07 measure | RESOLVED-BY | T2 rows 1–7 | — |
| T-08 … T-11 | one golden owner; revert stacks deleted; count pins deleted; dead golden rows deleted | RESOLVED-BY | T1 A–E | — |
| T-12 | kernel tests in `engine/tests` follow SC-P2 | SUPERSEDED | `05_SC_sc05_kernel_retirement.md` / its `_B` (U5c decides which stands) | — |
| T-13 … T-21 | shipped-world falsifiers; strengthened loops; skips to fails; reverted fixtures replaced | RESOLVED-BY | T3 rows 1–9 | — |
| T-22 | `CLAUDE.md` §7's sentence on `engine/tests/` goldens is stale | RESOLVED-BY | `U5a_CORE_owed_edits.md` §G (a Layer 0 edit, the orchestrator's; the exact sentence is given) | `engine/tests/goldens/` holds one pure-function table |
| §3 R-04 / R-07 (feeling, attitude) / R-09 (separation) have no shipped-world falsifier | — | RESOLVED-BY | T3's "Not written here" list names each as the gate of its owning proposal; see F-TEST-01 | — |
| §4 `[not adjudicated]` `tests/valoria/test_fractional_pool.py:39` (a sampled mean at `abs=0.05` on a 0.2 quantity) | — | RESOLVED-BY | PART 3 (DICE), row "test strength" | — |
| §4 `[not adjudicated]` MB `approx` on conservation claims; PC ten all-conditional loops | — | SUPERSEDED | U5b's closure (MB, PC test strength); listed in `unified/U5_CONFLICTS_U5a.md` §3 as handed across | — |
| §1 reading shortfall: about 120 season and 85 valoria test files scanned, not read | — | STALE-FALSE-POSITIVE (a declared coverage limit, not a finding) | the digests `DG_tests1..6` are the second reading; PART 5 | — |

**Dependency inside the three test proposals and against the pessimist's.** T1 C deletes revert-stacked hash
tests; `16_PESSIMIST_CORE_the_record_holds_what_changed.md` and `01_CORE_claim_fade_as_read.md` each re-pin
every hash. Order: T1 lands first (one owner, three literals), so each later mover re-records one file.
`16_PESSIMIST_CORE_no_stored_plan.md` deletes `test_u2_the_inputs_fingerprint_is_complete_for_the_skip_it_licenses`,
which addendum C §3 counts among R-03's falsifiers; R-03 keeps `test_u2_a_deposit_in_one_round_…` and its two
plant controls, and its `measure:` (`-k test_u2_`) still selects them, so no R-row loses its falsifier.

## 1.12 `audits/16_PESSIMIST_CORE.md` — findings, resolutions, survivor, lists

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| F-PES-CORE-01 | a refusal does not teach: 41 % retried, 96 % of retries refused | RESOLVED-BY | `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (reads present confidence through `01_CORE_claim_fade_as_read.md`'s one function once that lands; dependency noted at both heads) | `run_dump.py 0 3`; `p34.py 0 2`: 8 % retry where the failing read is deposited, 57 % where not |
| F-PES-CORE-02 | no receipt carries a value | RESOLVED-BY | `16_PESSIMIST_CORE_the_record_holds_what_changed.md` Edit 1 | 36,586 of 36,586 `delta=None` |
| F-PES-CORE-03 | the interior (scar, conviction crisis) is not in the log | RESOLVED-BY | same file Edit 2; consistent with `11_GO_player_surface_contract_B.md` §7 (presentation is triggered by the seated person's rows, never by a log Event such as `scar.taken`) | 3,914 of 40,494 receipts on no Event, all `Person.scar` |
| F-PES-CORE-04 | the nine's gate accepts `met 9` on a module that does not exist | RESOLVED-BY | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` Edit 1 | `req_forge.py`: arms B, C, D exit 0 |
| F-PES-CORE-05 | propagation is real, saturates, and mostly leaves no edge | RESOLVED-BY | same file Edits 2–3 (the reading); the unrecorded influence: F-CORE-12's carriers | knockout arms 0 / 0 / 236 / 309 / 634 / 625 |
| F-PES-CORE-06 | a scene has no internal order and one occupant | JORDAN | J-U5a-02; `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` (held; Option B's edits) | 120 of 525 scenes fold in order; 62 of 87 counterparties busy |
| F-PES-CORE-07 | the stored plan tail is never used | RESOLVED-BY | `16_PESSIMIST_CORE_no_stored_plan.md` | 0 of 1,137 releases from a stored queue; cut reproduces four hashes |
| F-PES-CORE-08 | an old Event's place is wherever its actor is now | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B row 17 (`event_place_at`), read first by the reason trail's chronicle line; `08_FI_04_small-edits.md` touches the same function for another case (U5c; ordered, not conflicting) | 39 of 831 season-0 act Events answer a different place a season later |
| F-PES-CORE-09 | the five strata and fold order decide almost nothing | STALE-FALSE-POSITIVE (as a defect: the audit takes no fix; the strata are ruled) | the figure (1 act in 175) is the input `18_DETERMINISM_rival_acts_in_one_fold.md` asked for; PART 6 | `ordp.py 0 1` |
| F-PES-CORE-10 | at `scene_budget = 0` MATTER's Events are witnessed by nobody | RESOLVED-BY | `U5a_CORE_owed_edits.md` §B row 18 (the fixture refuses `< 1` where it is read) | `extremes.py` |
| res. 1–6 | (as F-PES-CORE-01 … -05, -07) | RESOLVED-BY | the five proposals | — |
| res. 7 | an old Event's place read at `e.emitted_at` | RESOLVED-BY | §B row 17 | — |
| res. 8 | `scene_budget < 1` refused | RESOLVED-BY | §B row 18 | — |
| survivor | is a scene a budget unit (A) or a short sequence (B)? | JORDAN | J-U5a-02 | — |
| §2 false N-lines: stored plan tail; `Receipt.delta/.spec/.mode` | RESOLVED-BY | `…no_stored_plan.md`; `…the_record_holds_what_changed.md` (fill, not amputate) | — |
| §2 false N-line: the retry licence (pays 4 times in 309) | RESOLVED-BY | `…a_refusal_is_remembered.md` (a weight, not a ban; the licence stays) | — |
| §2 false N-lines: the five strata; fold order | STALE-FALSE-POSITIVE (ruled structure, one sort key) | as F-PES-CORE-09 | — |
| §2 unexercised: CENSUS (`person.demanded` never emitted) | SUPERSEDED | by the population proposals that give individuation a producer: `07_SE_population_census.md`, `21_PROCEDURAL_B_cast_and_seats.md`, `21_PROCEDURAL_D_world_cards_and_churn.md` (U5d; titles and a grep for `individuat`, bodies not opened) | — |
| §2 unexercised: the `obstacle > 2 × pool` fold arm; `act.ineligible`, `act.refused`, `attempt.refused` | RESOLVED-BY | the fold arm: §B row 12 (deleted; the live site is `sigma.py:543`). The three kinds are the fold's fallback kinds (`04` F.20b): no action | — |
| §2 S: nothing weights a Candidate by the chance it is admitted | RESOLVED-BY | `…a_refusal_is_remembered.md` (`admission_weight`, `odds_weight`'s sibling) | — |
| §2 R at extremes: 40 rounds emit `travel.blocked` 108 times | RESOLVED-BY | same (the retry weight) | — |
| §3 readings of R-01 … R-09 | RESOLVED-BY | the readings enter each row's `reading:` record (`01_CORE_requirements_reading_record.md` §1); statuses are not moved by this suite | — |
| §4.3 dead ends: 19 verbs never attempted; 100 of 178 Event kinds never emitted | SUPERSEDED | R-05 `not_met` is the standing record; the verbs lanes' closures (U5b, U5c, U5d) carry each verb | — |
| §6 stories it cannot tell: an errand; a conditional scene; a retold magnitude; an inner change; two people occupied; a person entering; an ending | RESOLVED-BY / JORDAN | magnitude and inner change: `…the_record_holds_what_changed.md`; conditional scene and occupancy: J-U5a-02; errand: `…a_refusal_is_remembered.md` frees the scenes, the errand itself (go and find him) is CHAR's `02_CHAR_offer_what_can_be_done.md`; entering: the population proposals; ending: §F and FA's endings (U5d) | — |
