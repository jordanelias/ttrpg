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

---

# Jordan's answers and the decision register (read before PARTS 2–6)

While this lane was reading, two files appeared in `unified/`: `DECISIONS_FOR_JORDAN.md` (the suite's one
register of questions for Jordan, ids `D-nn`) and `DECISIONS_ANSWERED.md` (Jordan's answers of 2026-11-12,
ids `A-n`). They bind this closure:

- A row whose disposition is **JORDAN** cites its `D-nn` entry; this lane keeps no second numbering for a
  question the register already holds. Items the register does not yet hold are in
  `unified/U5_CONFLICTS_U5a.md` §2 as `J-U5a-nn`, each with two options, for the register lane to take up.
  The provisional ids used in PART 1 map as: **J-U5a-01 = D-11** (may a capability gate an act),
  **J-U5a-02 = D-09** (a scene: a budget slot or a short sequence), **J-U5a-03** = new (`04` D-51's debit
  receipt), kept under that id.
- **A-4 (D-03): a duel inside a battle is a nested contest.** F-CORE-07's "nothing recurses" stops being true
  when that lands; `U5a_CORE_owed_edits.md` §A row 1 is worded so the depth sweep returns with it.
- **A-5 (D-05): the bell curve everywhere. A-6 (D-06): score plus a base, floor five. A-7 (D-07): talent and
  training are two numbers.** All three were answered *against* what the DICE, CORE and CHAR proposals
  assumed (whole dice; the score is the pool; the larger of attribute and skill). PART 3 and
  `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` are written to the answers, and every proposal of this
  family that assumed otherwise carries a `Reconciled:` line (`unified/U5_CONFLICTS_U5a.md` §1).

---

# PART 2 · CHAR

## 2.1 `audits/02_CHAR_audit.md` — findings F-CHAR-01 … F-CHAR-15

| id | claim (one line) | disposition | carrier (file · section) | evidence |
|---|---|---|---|---|
| F-CHAR-01 | the ranking reads the verb and nothing about what the act would do | RESOLVED-BY | `02_CHAR_goal_lean_on_its_own_question.md` (the goal's lean on its own question); the names behind the lean: `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md`. Means-ends valuation proper stays design-first at workplan CL-THRUST B2.2 (`goal_stages`), not re-opened | probe 3: 36 of 46 cast hold one top verb across six referents |
| F-CHAR-02 | the departure from the optimum is the realm's, not the person's | RESOLVED-BY | `02_CHAR_resolve_and_temper.md`, with the test-retest gate added by `U5a_CHAR_owed_amendments.md` §1 (F-PES-CHAR-04 a) | probe 1: identical persons disagree in 70–74 % of readings; test-retest 60.7 % (pessimist) |
| F-CHAR-03 | the interior does not move | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` item 2 (regard in stance steps); relations: `02_CHAR_relations_have_a_ground.md` | probe 2: stance moved for 0 of 83 at two seeds; computed half median 0.051 |
| F-CHAR-04 | the scar runs away and its live reader fires on noise | RESOLVED-BY | `02_CHAR_scar_is_a_wound.md` (which amends item 1 of `02_CHAR_scar_cap_and_regard_unit.md`: C-U5a-06); what the crisis then does: `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` | median per-person maximum 41 in two seasons |
| F-CHAR-05 | four in ten resolved acts are refusals the actor could have foreseen | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md` (what his own state answers) and `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (what only the world answers). One finding from two lanes (= F-PES-CORE-01), merged: the first declines at formation, the second weighs a remembered refusal; neither bans a retry | 656 refusals of 1,529 resolved acts (seed 0); 62 % of refusals fail on a read the person can never hold |
| F-CHAR-06 | `decision_spread`'s headline cannot fail | RESOLVED-BY | `02_CHAR_resolve_and_temper.md` edit 4 | 83 of 83 under shipped, control and null |
| F-CHAR-07 | a population takes an individual's acts | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md` items 4–5; the wider question (a short verb list for populations) is D-73 and is not pre-empted | cohorts: `challenge` 60, `forge` 47 in two seasons; addendum B C-1 confirms the row |
| F-CHAR-08 | two scales in one sum; the stance term unbounded and signed by the wrong column | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` item 3 and Addendum (`regard_sign`), with the `stance_scale` fixture added by `U5a_CHAR_owed_amendments.md` §2 (F-PES-CHAR-04 b) | term variance 1.88 against 0.008; a class gap of 800 temperatures |
| F-CHAR-09 | knowledge is partial and almost never second-hand | SUPERSEDED | owner is the telling lane (FI / verbs SOCIAL): U5c's closure; no CHAR edit (the weighting is built and waits on volume) | 12 chained claims of 22,958 |
| F-CHAR-10 | the score's dot product sums in set order | RESOLVED-BY | `02_CHAR_resolve_and_temper.md` edit 3 | H-362 |
| F-CHAR-11 | nine person-side declines keyed by verb | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md` items 1–3 (= F-CORE-18's decision half) | `options.py:136-267` |
| F-CHAR-12 | Layer 1's frozen `PersonInterior` is not built | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 1 | `04` §B.2 row 2 against `deliberate.py:202` |
| F-CHAR-13 | the cast loader's docstring counts keys, not values | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` Part C | parse: `stats` 1, `ts` 10, `goals` 17 |
| F-CHAR-14 | condition reaches a choice only as a scene count; any `hold` earns the office bonus | RESOLVED-BY | the hold count: workplan IN-14, whose own override already narrows `offices` to holds with non-empty `granted_acts`; `02_CHAR_reason_trail_and_small_edits.md` B1 is that same edit and lands once, at IN-14 (merged duplicate, `unified/U5_CONFLICTS_U5a.md` §4). Condition in the score: `02_CHAR_what_an_act_risks.md` | H-330; `budget.py` |
| F-CHAR-15 | stale text at the owners | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` Part C; its two `requirements.yaml` `measured:` rewrites are folded into `01_CORE_requirements_reading_record.md` §1's `reading:` record (C-U5a-05) | lines cited in the finding |

## 2.2 `audits/02_CHAR_audit.md` §0A, §4, §5 — tables with no finding number

| item | disposition | carrier / reason |
|---|---|---|
| §0A "ruled, not yet built": deontology as a refusal | RESOLVED-BY | `16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` |
| §0A scar weight shift at threshold 2 (built, shipped at 0); H-187 | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §8 (the ordered flips, after the wound proposal's gate) |
| §0A risk appetite and horizon (ED-IN-0304; no carrier) | RESOLVED-BY | the term it scales: `02_CHAR_what_an_act_risks.md`; the carrier is CL-PERSON's open ask M40 (workplan), not pre-empted |
| §0A duty of office (CR-88) | RESOLVED-BY | input `02_CHAR_goal_lean_on_its_own_question.md`; the position is workplan CR-88 (B10-17b) |
| §0A attributes in a choice and on others (CR-93, CR-92); the ten attributes shipped off | RESOLVED-BY | `02_CHAR_capability_uses_table.md`; the switch and the cast content: U1 architecture §6 and `U5a_capability_home_and_two_inputs.md` Part C |
| §0A "where the sources disagree" (ten rows) | STALE-FALSE-POSITIVE (not findings: each row states which source the game follows) | the two with a consequence are F-CHAR-04 (scar cap) and F-CHAR-20 (survival); carried there |
| §0A limit (2): an NPC has no decider inside a contest | RESOLVED-BY | `01_CORE_one_scene_contract.md` as reconciled (C-U5a-03): `decide=None` asks the person's own decider; the appetite it reads: `02_CHAR_what_an_act_risks.md` |
| §4 a second scar model in `systems/characters/sim/conviction.py` | STALE-FALSE-POSITIVE (kept by ruling ED-IN-0283; unreached by the loop) | resolution 27; no edit |
| §4 dead or unreached readers (`rank`, `entrenchment`, `legitimacy`, `stability`, `beneficiary_of`, `violated_*`) | RESOLVED-BY | `legitimacy` / `stability` / `opinion` gain their reader in `02_CHAR_voices_and_the_room.md` Edit 5; the others are census rows (PART 4) |
| §5 NERS cuts (scar count; the realm-wide draw; `teller_weight`; goals as attention; the sheet) | RESOLVED-BY | each by the finding it restates (F-CHAR-04, -02, -09, -01; F-CORE-05) |
| §9 a playable character entry point | RESOLVED-BY | `11_GO_player_surface_contract_B.md` §8; `U5a_CORE_owed_edits.md` §F |
| §10 what the mass-battle intent needs from this lane | RESOLVED-BY | `02_CHAR_choice_alignment.md`; U1 architecture §9 (the officer's keys named on the mass-battle input: MB's edit, U5b) |

## 2.3 `audits/02_CHAR_audit.md` §6.1 — hole-register and workplan rows

| rows | disposition | carrier / reason |
|---|---|---|
| H-03, H-71, H-94, H-134, H-194, H-202, H-255, H-256, H-221, H-248, H-249, H-357, H-358 (closed or built) | STALE-FALSE-POSITIVE (as open items) | verified in code by the audit; no action |
| H-54, H-66, H-177/178/179/183, H-180, H-181, H-191, H-195, H-198, H-188, H-190, H-196, H-199 (open by design or declared absent) | STALE-FALSE-POSITIVE (as findings) | carried; H-66's and H-347's cells are now given a target by `16_PESSIMIST_CHAR_B…` |
| H-60 | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §9 (mark closed on the row) |
| H-73 | SUPERSEDED | by REM-44 (the row's own last sentence); resolution 28 |
| H-96 | RESOLVED-BY | `02_CHAR_resolve_and_temper.md` edit 5 |
| H-146 | RESOLVED-BY | `16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` |
| H-187 | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §8 |
| H-189, H-237 | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` Part C |
| H-192, H-193 | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` item 2 |
| H-200, H-239 | RESOLVED-BY | `02_CHAR_capability_uses_table.md` |
| H-253, H-289 | SUPERSEDED | FA's closure (U5d); CHAR's share is the goal lean |
| H-264 | SUPERSEDED | PC's closure (U5b) |
| H-268, H-272 | SUPERSEDED | SC's and FI's closures (U5c); the hearer's side of H-268 is `02_CHAR_which_ground_moves_whom.md` |
| H-283 | RESOLVED-BY | `02_CHAR_goal_lean_on_its_own_question.md` |
| H-330 | RESOLVED-BY | workplan IN-14 (see F-CHAR-14) |
| H-334, H-337, H-339 | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` item 3 and Addendum |
| H-346 | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md` |
| H-347 | RESOLVED-BY | `16_PESSIMIST_CHAR_B…` (four pursuits put `forge` first) |
| H-362 | RESOLVED-BY | `02_CHAR_resolve_and_temper.md` edit 3 |
| the 38 rows read at the dossier excerpt only | RESOLVED-BY | addendum B §B6.1 read each in full; closed at §2.7 below |
| CR-88, CR-89–91, CR-93, CR-92, CL-PERSON, CL-ATTR | RESOLVED-BY | their workplan positions; inputs named in the proposals above |

## 2.4 `audits/02_CHAR_audit.md` §6.2 — resolutions 1–30; §8 steps; §11 survivor

| # | resolution | disposition | carrier |
|---|---|---|---|
| 1 | scar: one count per (person, element) per season | SUPERSEDED | by addendum B's F-CHAR-17 (the cap bounds the rate, not the stock): `02_CHAR_scar_is_a_wound.md` keeps it as the `element` arm of one fixture (C-U5a-06) |
| 2, 3, 4 | regard in stance steps; clamp at `STANCE_MAX`; `regard_sign` column | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` items 2, 3, Addendum |
| 5, 6, 7, 8 | `resolve` named; `temper` hook; a temperature-0 column; `_AXES` order | RESOLVED-BY | `02_CHAR_resolve_and_temper.md` |
| 9, 10, 11 | one decline; decline what own state answers False; the cohort conjunct | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md` |
| 12, 13 | the goal term applies on the goal's own question | RESOLVED-BY | `02_CHAR_goal_lean_on_its_own_question.md` |
| 14 | attribute names as literals under `decision/` | RESOLVED-BY | `02_CHAR_capability_uses_table.md` (the uses table, as U1 architecture §3 adopts it) |
| 15 | alignment cells on choice values | RESOLVED-BY | `02_CHAR_choice_alignment.md` |
| 16 | an observer hook on the chooser; terms on the sheet | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` Part A; the stored deciding term: `U5a_CHAR_owed_amendments.md` §5 |
| 17 | `budget` counts seats | RESOLVED-BY | workplan IN-14 (merged duplicate) |
| 18 | `by_subject` ordering | RESOLVED-BY | `02_CHAR_reason_trail_and_small_edits.md` B2 |
| 19–25 | stale text; the worksheet outliving its landing | RESOLVED-BY | same file, Part C (22 and 23 through the `reading:` record, C-U5a-05) |
| 26 | frozen `PersonInterior` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §E row 1 |
| 27, 28, 30 | second scar model kept; H-73 closed; `decision_policy_v1.md` is not a chooser source | RESOLVED-BY · no edit (decided in the audit, steps 1 and 2) | — |
| 29 | NPC-034 / NPC-071 "no goal authored" | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §10 (a content row: `goals:` on the two cast rows; an authoring gap, not an engine need) |
| §8 step 10 | arm `scar_weight_shift`, then `refusal_axis` | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §8 |
| §8 step 12 | means and ends | RESOLVED-BY | workplan CL-THRUST B2.2 (design-first); not re-opened |
| §11 | can a person be wrong about himself? | JORDAN | D-47 |

## 2.5 `audits/02_CHAR_audit.md` §13 — provided characters

| case · need | disposition | carrier |
|---|---|---|
| NPC-088 a season of tracked state; NPC-012 unstated motive; NPC-035; NPC-005; NPC-008 | STALE-FALSE-POSITIVE (represented today) | the runs and reads the audit cites; each still needs `beats:` to be checked (`01_CORE_case_setup_and_beats.md`) |
| NPC-012 employer's evaluation; NPC-082 loyalty to a cause erodes | RESOLVED-BY | `02_CHAR_scar_cap_and_regard_unit.md` item 2; then workplan CR-88 (FA) |
| NPC-020 a private doubt; NPC-075 unrewarded labour | RESOLVED-BY | `02_CHAR_scar_is_a_wound.md`; `16_PESSIMIST_CHAR_A…`; the flips in `U5a_CHAR_owed_amendments.md` §8 |
| NPC-020, NPC-070 an armed institution reassesses loyalty in stages | SUPERSEDED | FA's closure (CR-88); edge: regard in steps first |
| NPC-021 faith challenged by facts | RESOLVED-BY | need restated as argument (the audit's reading); the hearer's side `02_CHAR_which_ground_moves_whom.md`; H-268 is SC's |
| NPC-002 range of action narrows to withdrawal | RESOLVED-BY | restated against #353 §9.2 as the budget (the audit's reading); withdrawal at the floor: `02_CHAR_what_an_act_risks.md` |
| NPC-004 a capacity he does not know he has | JORDAN | D-47 |
| NPC-089 one governor among graduated postures | RESOLVED-BY | `02_CHAR_choice_alignment.md`; more than one posture is MB content (U5b) |
| NPC-090 two officials shape one relationship | RESOLVED-BY | `02_CHAR_goal_lean_on_its_own_question.md` |
| NPC-031 the heir's relation to the regent | SUPERSEDED | FA's closure (IN-61; D-19) |
| NPC-034, NPC-071 | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §10 |
| NPC-086 evidence shown to an audience spreads | SUPERSEDED | FI's closure (H-272) |
| 16 cases wait on a player | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` Edit 4; the seated runner `11_GO_player_surface_contract_B.md` §8 |

## 2.6 `audits/02_CHAR_audit_addendum_B.md` — findings F-CHAR-16 … F-CHAR-22, corrections, returning findings

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| F-CHAR-16 | six authored cast-row facts are read by nothing | RESOLVED-BY | `02_CHAR_capability_definitions.md` Edit 4 (read, remove or mark, key by key); `resonant_style`'s reader: `02_CHAR_which_ground_moves_whom.md` | parse: `resonant_style` 18, `arc_trajectory` 36, `cultural_label` 43 |
| F-CHAR-17 | the scar's ladder cannot discriminate under any cap on its rate | RESOLVED-BY | `02_CHAR_scar_is_a_wound.md`; the fully scarred person: `U5a_CHAR_owed_amendments.md` §6 | 83 of 83 at the terminal rung by season three under the cap |
| F-CHAR-18 | the designed foils are not foils; no relation has a kind | RESOLVED-BY | `02_CHAR_relations_have_a_ground.md`; the patient of a deed: `U5a_CHAR_owed_amendments.md` §4 | `probe_foils.py`: the most alike pair of the Diamond is an opposed pair |
| F-CHAR-19 | the design's skill is a conditional effect with a level; the build's is a key at the default | RESOLVED-BY | U1 architecture §2–§4; `02_CHAR_capability_definitions.md` Edits 1–3 | 34 lifepath templates, 21 hold nothing |
| F-CHAR-20 | nothing a person risks reaches his choice | RESOLVED-BY | `02_CHAR_what_an_act_risks.md` | `score_terms` has no term reading `body` |
| F-CHAR-21 | the development sheet shows less than the creation sheet | RESOLVED-BY | `02_CHAR_capability_definitions.md` Edit 5 (with `01_CORE_capability_authoring_surface.md` Edit 6: one change to one dataclass) | `dataclasses.fields` |
| F-CHAR-22 | three dossier files are not character documents | RESOLVED-BY · no edit (decided in the audit, step 2) | B6.2 row 23 | — |
| C-1 … C-8 | corrections and confirmations to the first audit | RESOLVED-BY | C-1: `…offer_what_can_be_done.md`; C-2, C-3, C-5: reference, no edit; C-4: `…scar_is_a_wound.md`; C-6: `…capability_definitions.md` Edit 4; C-7: same, Edit 3; C-8: D-47 | — |
| B2.2 returning findings (six rows) | — | RESOLVED-BY | "zero person-scale change" = F-CHAR-03; "no scar decay" = F-CHAR-17 (the outflow, `scar_vindication`); the D6 scar gate is false now (STALE); the relational graph is doc-only = F-CHAR-18; legibility reversed = the reason trail; R-AI holds |
| B3.2 P1 … P10 (ten things asked of a chooser) | — | RESOLVED-BY | P1 goal lean + CR-88; P2 temper + pessimist B; P3 wound + pessimist A; P4 risk; P5 ground; P6 relations + `regard_sign`; P9 reason trail + voices; P7, P8, P10 built |
| B4 the character's side of the capability surface | — | RESOLVED-BY | U1 architecture (which adopts §B4 (c)'s field table); `02_CHAR_capability_definitions.md` |
| B5 internal voices and a community's opinion | — | RESOLVED-BY | `02_CHAR_voices_and_the_room.md`; a faculty's voice and a voice that was wrong are FI's (U5c) |

## 2.7 `audits/02_CHAR_audit_addendum_B.md` §B6.1 (38 register rows), §B6.2 (24 resolutions), §B6.3

| rows | disposition | carrier / reason |
|---|---|---|
| H-46, H-148, H-170 (stale text) | RESOLVED-BY | `02_CHAR_capability_definitions.md` Edit 6 |
| H-201, H-205, H-240 (closed), H-117 (superseded in its headline), H-38 (closed as corrected) | STALE-FALSE-POSITIVE (as open items) | read in full by the addendum |
| H-128 | RESOLVED-BY | `02_CHAR_scar_is_a_wound.md` (the actor is scarred by his own act, at the floor; the arm stays swept) |
| H-136, H-270, H-322, H-300, H-329 (acts formed that cannot succeed) | RESOLVED-BY | `02_CHAR_offer_what_can_be_done.md`; `16_PESSIMIST_CORE_a_refusal_is_remembered.md` |
| H-224 | RESOLVED-BY | `02_CHAR_voices_and_the_room.md` Edit 5 |
| H-233, H-343 | RESOLVED-BY | goal lean; reason trail |
| H-273, H-282 | RESOLVED-BY | `16_PESSIMIST_CHAR_B…` (the cells); `regard_sign` |
| H-58, H-85, H-121, H-160, H-165, H-171, H-175, H-203, H-204, H-229, H-271, H-277, H-280, H-286, H-313, H-316, H-317, H-328, H-361 | SUPERSEDED | by the owning lanes' closures (SE, FA, FI, SC, MB, WR: U5b, U5c, U5d); cross-listed by the addendum, no CHAR edit |
| B6.2 rows 1, 2 | RESOLVED-BY | `02_CHAR_scar_is_a_wound.md` |
| rows 3, 7 | RESOLVED-BY | `02_CHAR_which_ground_moves_whom.md` |
| rows 4, 5, 6, 13, 14, 18, 22, 24 | RESOLVED-BY | `02_CHAR_capability_definitions.md` Edits 1–6 |
| rows 8, 10 | RESOLVED-BY | `02_CHAR_relations_have_a_ground.md` |
| row 9 (is kin a ground the heir title reads?) | JORDAN | D-19 (who may claim the crown) holds the dynastic question; `kin` ships as a ground no rule reads |
| rows 11, 12 | RESOLVED-BY | `02_CHAR_what_an_act_risks.md` |
| rows 15, 16, 23 | RESOLVED-BY · no edit (decided in the audit) | a capability is never lost; an ability is not a fifth kind; a misfiled document stays |
| row 17 (combat abilities cannot be authored as data) | SUPERSEDED | PC's `03_PC_person_inputs_content.md` (U5b; by title) |
| rows 19, 20 | RESOLVED-BY | `02_CHAR_voices_and_the_room.md` |
| row 21 (the file for the capability definition: registry or rosters) | RESOLVED-BY | U1 architecture §1 (decided: C-U5a-08) |
| B6.3 | JORDAN | D-47 |

## 2.8 `audits/16_PESSIMIST_CHAR.md` — findings, resolutions, the two items for Jordan, lists

A = `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`; B = `…_B_a_pursuit_does_what_its_name_says.md`;
C = `…_C_the_stop_is_the_mans.md`.

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| F-PES-CHAR-01 | the names on a character do not predict his acts | RESOLVED-BY | B (signatures, then cells, then the loader's refusal) | a man of `love` alone tops `forge` in 266 of 276 readings |
| F-PES-CHAR-02 | nothing stops a man; armed, the gate stops everyone from walking | RESOLVED-BY | C items 1–3, 5; item 4 (the draw) decided on the standing rule and listed (D-28, D-26) | unarmed 0 of 46; armed 46 of 46 |
| F-PES-CHAR-03 | the only interior event is a fixed, inverted, silent conversion | RESOLVED-BY | A items 1–4; the roll decided on the standing rule and listed (D-27, D-26); who holds the claim reconciled (C-U5a-09) | the same six converts at both seeds |
| F-PES-CHAR-04 | between a certainty and a coin there is little room for a character | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §1 (test-retest gate on `02_CHAR_resolve_and_temper.md`) and §2 (`stance_scale` on `02_CHAR_scar_cap_and_regard_unit.md`) | test-retest 60.7 %; class gap 800 temperatures |
| F-PES-CHAR-05 | nobody is skilled, everybody fails, an opponent's skill is not in the roll | RESOLVED-BY | U1 architecture §4–§6 as rewritten to A-6 (score plus a base, floor five) and A-7 (two inputs, the opponent's among them); cast content `02_CHAR_capability_definitions.md`; calibration is SC's (U5c) | pool 2 for 46 of 46; 77 % Failure in play |
| F-PES-CHAR-06 | a man is wrong about the granary and about nothing else | SUPERSEDED | the telling lane and `10_DICE_believed_odds_have_a_prior.md` (PART 3); no CHAR edit | 296 of 312 false beliefs are store counts |
| F-PES-CHAR-07 | a want never ends | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §3 (the exact edit, addressed to `12_ARCS_arcs_as_staged_goals.md`, U5d's file) | 0 of 243 commitments ended |
| F-PES-CHAR-08 | what is done to a man does not decide what he thinks of who did it | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §4 (amends `02_CHAR_relations_have_a_ground.md`) | `give` and `tend` sit below `sabotage` and `lie` |
| F-PES-CHAR-09 | no reason survives, and for half of what persons do there was none | RESOLVED-BY | the two reason-trail proposals; the stored deciding term, the draw included: `U5a_CHAR_owed_amendments.md` §5 | `Act.reads` empty on 4,757 of 4,757 acts |
| F-PES-CHAR-10 | a realm of persons without wants is livelier than the shipped one | RESOLVED-BY | B (signatures name the verbs of harm and mercy) | `nopursuit` arm |
| F-PES-CHAR-11 | the most scarred man is the least changed | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §6 (amends `02_CHAR_scar_is_a_wound.md`) | `person_q.py:883` |
| F-PES-CHAR-12 | one man's paperwork scars the whole realm | RESOLVED-BY | B with `02_CHAR_scar_is_a_wound.md` | `x2_alone.py`: 83 of 83 scarred by one actor |
| res. 1–8 | (as F-PES-CHAR-01, -02, -03) | RESOLVED-BY | A, B, C | — |
| res. 9–12 | the four amendments | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §2, §3, §4, §6 | the audit named each amendment and left the amended file unedited; this lane wrote them |
| For Jordan 1 | the crisis rolls or it does not | RESOLVED-BY, listed | A (the roll), on the standing rule (ladder step 1: the later, general ruling); listed as D-27 under D-26 because it overwrites ED-IN-0261's G-Q6 | — |
| For Jordan 2 | the scruple is a line or a tendency | RESOLVED-BY, listed | C item 4, same ground; D-28 under D-26. The gate itself stays unarmed until armed by its own flip | — |
| §0 a pool of one die at the default obstacle has P(Success) exactly 0 | RESOLVED-BY | U1 architecture §4 (A-6's floor of five dice removes the case) | — |
| §5 false N-lines: `Person.conviction` nearly free; the creed's triggers are not about faith | RESOLVED-BY | `U5a_CHAR_owed_amendments.md` §7 (creed signatures on B's mechanism) | — |
| §5 false N-lines: believed-odds weighting; attributes; capability | RESOLVED-BY | U1 architecture §6 (content and the attribute switch); `02_CHAR_offer_what_can_be_done.md` (priced candidates form) | — |
| §5A stories that cannot happen | RESOLVED-BY / SUPERSEDED | persuaded: SC (U5c); learns a skill: U1 architecture §4; seat: FA (U5d); ambition ends: §3 above; tempted: C; forms a tie: `02_CHAR_relations_have_a_ground.md` (authored; an opener in play is the tie verb's, D-33); ages: D-15; deceived: U5c | — |

---

# PART 3 · DICE

**Read first.** Three of Jordan's answers decide what most of this part's proposals assumed the other way:
A-5 (the bell curve everywhere), A-6 (score plus a base, floor five, one rule for combat and everything
else), A-7 (talent and training are two inputs). The carriers below are therefore the DICE proposals **as
reconciled** (each carries a `Reconciled:` line), `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`, and two
plans this lane wrote: `proposals/U5a_capability_home_and_two_inputs.md` (**CAP**) and
`proposals/U5a_DICE_owed_edits.md` (**DOE**). MAP = `10_DICE_capability_axiom_map.md`.

## 3.1 `audits/10_DICE_audit.md` — findings F-DICE-01 … F-DICE-14

| id | claim (one line) | disposition | carrier (file · section) | evidence |
|---|---|---|---|---|
| F-DICE-01 | the engine is fed a constant: every social roll is two dice, no leverage | RESOLVED-BY | U1 architecture §4–§6; CAP Part B (the roll's two inputs) and Part C (cast content, the attribute switch); `10_DICE_advantage_sources_for_the_arcs.md` Edit A (the signed channel) | 568 graded rolls: 564 at pool 2, leverage 0.0 on all |
| F-DICE-02 | the default outcome is nothing and the top band cannot occur | SUPERSEDED | by A-6 (score plus a base, floor five): the pair (2 dice, Ob 2) no longer exists. The audit's own remedy (person-opposed rolls to Ob 1.0) stands as `10_DICE_one_score_two_roles.md` | `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` at the built regime |
| F-DICE-03 | holding a score makes a person easier to oppose | RESOLVED-BY | `10_DICE_one_score_two_roles.md` Edits A–B, as reconciled to A-7 (the score is the trained rank; the attribute is the second input, never folded by `max`) | E-07: 26.00 / 58.00 / 73.50 % |
| F-DICE-04 | four rolled verbs name no capability | RESOLVED-BY | U1 architecture §5 (one value per verb row, decided across CORE, DICE, SC and FA: C-U5a-11) | E-09 |
| F-DICE-05 | two samplers half a success apart | SUPERSEDED | by A-5: one sampler. `10_DICE_exported_face_rule_and_band_edges.md` Edit B's claim-correction and Edit C's three-name vocabulary are withdrawn (Reconciled); DOE §1 carries the move | E-06: Failure 38.59 against 46.42 % at pool 8, Ob 3 |
| F-DICE-06 | the advantage channel has one member, one sign, and sums to zero | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit A (signed); the `edge` rows of the uses table (U1 architecture §3); the wound: 3.2 below, F-DICE-16 | leverage 0.0 on 568 of 568 |
| F-DICE-07 | a second roller, and a ladder in two classes | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` Edits A, C, D as reconciled (mass battle composes on the owner; under A-5 the owner's roll is the bell-curve sampler, so the "byte-equal goldens" gate is replaced by one declared re-pin); DOE §1 | 6 of 10,000 tenth-step cells differ; the pessimist's swap test: 0 of 20,000 nets differ at whole pools |
| F-DICE-08 | three rules for a fraction of a die | SUPERSEDED | by A-5: the bell-curve sampler takes a fractional pool as it is; the rounding and the stochastic die are deleted with the whole-dice roll (same proposal's Edit B withdrawn) | E-05 |
| F-DICE-09 | the typed layer omits the facts every draw depends on | RESOLVED-BY | `10_DICE_exported_face_rule_and_band_edges.md` Edits A (band floors; the per-die pair asserted against the faces) and D (`LEVEL_SIGMA` exported), as reconciled: `FACE_NET` stays the derivation of the pair, exported as provenance only; DOE §1 names what the port reads | E-11: six scalars exported |
| F-DICE-10 | the room is a flat obstacle shift | RESOLVED-BY · no build (accepted in the audit, resolution 9) | the favourable half is D-29 (SC's: U5c); the sentence for H-215's `cite:` is DOE §3 row 1 | E-08 |
| F-DICE-11 | the extension seam is unreached by the loop and half open | RESOLVED-BY | DOE §3 rows 2–3 (context validated on entry; the dead `extension` parameter deleted) | E-04 |
| F-DICE-12 | half the advantage module's surface has no game caller | RESOLVED-BY | DOE §1 (under A-5 the Normal closed form becomes the odds function: `p_success` is no longer dead; `eff_ob`, `effective_ob`, `sigma_space_ob_shift` go with the kernel, SC-P2) | E-17 |
| F-DICE-13 | stale passages at the owner | RESOLVED-BY | DOE §3 row 5 | lines cited in the finding |
| F-DICE-14 | the chooser's odds answer for one verb, and "cannot say" reads as certain | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` Edits A–B; the fight's and field's believed estimate (Edit C) is PC's and MB's (U5b); the roll's record (Edit D) is merged into MAP's `fed_by` and SC-B's `Margin.terms` (U5c) | E-19: 102 figures of 4,929 queries |

## 3.2 `audits/10_DICE_audit_addendum_B.md` — corrections C-1 … C-8, findings F-DICE-15 … F-DICE-23, H-152

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| C-1, F-DICE-15 | three obstacle axioms for one ruling; the field is an opposed roll | RESOLVED-BY | MAP §A ("the contest form", `static` or `opposed_roll`) and §G edit 9; the floor reads `OB_MIN` (addendum §5.1 item 2, in DOE §1) | `orchestration.py:1308-1309` |
| C-2 | the first audit's research skip was a false absence | RESOLVED-BY · no edit | the three leads are used in F-DICE-16, -17, -18 | — |
| C-3, F-DICE-16 | the wound's penalty was ruled (+0.15 Ob per wound); the first proposal departed from it | RESOLVED-BY | addendum §5.4 as carried by DOE §2 (an obstacle term, `obstacle_terms: [wounds]`); `10_DICE_advantage_sources_for_the_arcs.md` Edits B–D withdrawn (Reconciled, C-U5a-12). The other channel (a level against) is D-08; the ruled form is taken unless Jordan answers otherwise | ED-PC-0005, ED-PC-0006 |
| C-4 | the roller proposal's `grep` falsifier cannot read one line | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` falsifier restated (Reconciled) | E-B02 |
| C-5, F-DICE-17 | one score, three pools | SUPERSEDED | by A-6: one pool rule, `max(pool_floor, score + addends + pool_add)`, at every site (U1 architecture §4; MAP §C's four per-site fixtures become two, Reconciled) | E-B03: equals succeed 28 % in the social roll, 63–68 % in the other two |
| C-6, H-152 | closed by a run (CP-T02-01) | RESOLVED-BY | DOE §3 row 6 (the register row's head and owner) | `probe_h152.py`, three arms with a mutation |
| C-7, F-DICE-18 | a field battle reads no person | RESOLVED-BY | MAP §D (the `field` site declared with no rows); the first rows are MB's (U5b); the form of fortune in a field is D-34 | E-B04: `MassBattleInput` byte-equal |
| C-8, F-DICE-21 | the field speaks sigma in die-equivalents and tires twice | SUPERSEDED | MB's closure (U5b); addendum §5.1 item 5 states the target | `config.py:306` |
| F-DICE-19 | below one die the sigma boost is a full die's | RESOLVED-BY | DOE §1 (under the one sampler a sub-one-die aggregate's spread and boost both scale with the root of the pool; the floor at one die is removed for aggregates) | E-B05 |
| F-DICE-20 | derived resources exist for one scene of one subsystem | RESOLVED-BY | MAP §A (`resource` is a declared role with its one instance). No formula is carried: Health's form is Jordan's own open ruling (AR-58, ED-IN-0347) and is not re-raised | `combatant.py:172-183` |
| F-DICE-22 | two unread tests are prose guards | RESOLVED-BY | `01_CORE_tests_delete_what_cannot_fail.md` row 1 (`test_knot_pool_formula.py`); `tests/valoria/test_fractional_pool.py` is deleted with its subject (DOE §1); this also closes addendum C's `[not adjudicated]` row on that file | — |
| F-DICE-23 | a skill's rank has no ceiling | RESOLVED-BY | U1 architecture §2 (`scale` on the definition row, read by `raised_capability`); CAP Part A | `effects_combat.py:262-268` |
| §5.1 items 1–6 | the shared roller meets mass battle's resolver | RESOLVED-BY | DOE §1 (items 1–5 restated for the one sampler); item 6's order against `11_GO_one_draw_owner.md` stands (one roller first, then GO's) and D-38 holds the keyed-draw question | — |
| §5.2 | the duel round from the dice side | SUPERSEDED | PC's closure (U5b): an approach is an `edge` row, never a pool rule | — |
| §5.3 | the weapon-carry cost is the `threshold` role, one leaf function | SUPERSEDED | PC's and MB's closures (U5b); the role is MAP §A's | — |
| §5.5 | order of landing | RESOLVED-BY | restated for the answers in CAP "Order" and DOE "Order" | — |
| §5.6 item 1 | the wound's channel | JORDAN | D-08 (default: as ruled) | — |
| §5.6 item 2 | what a score is worth outside a fight | SUPERSEDED | answered: A-6 | — |

## 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1–25, §11 survivor, §13 arcs

| item | disposition | carrier / reason |
|---|---|---|
| H-31 (regrade `ruled`), H-88 (close), H-98 (close; off R-09's `blocks:`), H-114, H-115 (heads say CLOSED) | RESOLVED-BY | DOE §3 rows 7–9 |
| H-152 | RESOLVED-BY | DOE §3 row 6 |
| H-244 | STALE-FALSE-POSITIVE (kept as a number; unexercised until a believed opposition exists) | `10_DICE_believed_odds_have_a_prior.md` is what exercises it |
| H-310 | SUPERSEDED | FI / SC (U5c) |
| H-312 | RESOLVED-BY | U1 architecture §5 (`interrogate: inquiry`) |
| H-126, H-127, H-213 | RESOLVED-BY | `10_DICE_one_score_two_roles.md` (H-127's scope); `16_PESSIMIST_DICE_soft_ceiling.md` (H-213); H-126's magnitude is re-read at the A-5/A-6 calibration (CAP Part B gate) |
| H-332, H-349, H-361; CP-T01-01 … -06; CR-17 | STALE-FALSE-POSITIVE (closed or not adjudicated here) | — |
| res. 1, 2 | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` Edits A, C, D (Reconciled) |
| res. 3, 4 | SUPERSEDED | A-5 (no whole-dice fraction rule) |
| res. 5 | SUPERSEDED | A-5 (the audit decided "leave the offset, narrow ED-833"; Jordan answered the other way) |
| res. 6, 7 | RESOLVED-BY | `10_DICE_exported_face_rule_and_band_edges.md` Edits A, D; one resolver name for all three providers (DOE §1) |
| res. 8, 10 | RESOLVED-BY | `10_DICE_one_score_two_roles.md` Edits A–B (Reconciled); the verb values: U1 architecture §5 |
| res. 9 | RESOLVED-BY | DOE §3 row 1 |
| res. 11, 12, 13, 14, 15, 16, 20 | RESOLVED-BY | DOE §3 rows 2–5, 7–10 |
| res. 17 | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit A |
| res. 18 | SUPERSEDED | by C-3 / F-DICE-16 (a wound is an obstacle term) |
| res. 19 (SCN-05 restated: a spend buys named levels) | RESOLVED-BY | same file, "The resolution" |
| res. 21 (`CLAUDE.md` §7) | RESOLVED-BY | `U5a_CORE_owed_edits.md` §G (the same sentence as T-22; merged) |
| res. 22 (mass battle's survivor-ratio labels use the ladder's four names) | SUPERSEDED | MB's closure (U5b); A-3 fixes the field's returned vocabulary (won, lost, drawn) |
| res. 23 | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` Edits A–B |
| res. 24 | SUPERSEDED | PC's and MB's closures (the `believed_estimate` role) |
| res. 25 | RESOLVED-BY | MAP §D (`fed_by`) with SC-B's `Margin.terms` (U5c): one record of a roll, proposed once |
| §11 survivor (which sampler non-combat rolls use) | SUPERSEDED | answered: A-5 (the audit's Option B). Every edit the audit wrote "for A" is reconciled |
| §9 "one roll as a decision"; §8 step 7 (a surface that prints odds) | RESOLVED-BY | `11_GO_player_surface_contract_B.md` (`Offer` rows carry odds; U5d) |
| §13 ARC-22, NSC-04, NSC-07, SCN-01, ARC-10 (four graded outcomes) | RESOLVED-BY | A-6 and U1 architecture §4 (the top band becomes reachable); band-distinct writes on `lie`, `speak`, `tell`, `interrogate` are SC's and FI's (U5c; = F-PES-DICE-01) |
| §13 ARC-18, ARC-17 | STALE-FALSE-POSITIVE (represented) | — |
| §13 ARC-06 (an implementation can fail on its own roll) | RESOLVED-BY | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (PART 6) |
| §13 SCN-04 (difficulty from a stored disposition) | SUPERSEDED | SC's obstacle proposal (U5c) |
| §13 ARC-53 (a wound persists; a faction's stat adds to its leader's roll) | RESOLVED-BY | DOE §2 (the wound term); the faction half is an `addend` over `Act.via` (FA's, U5d; D-12 holds whether office may add to a roll) |
| §13 NPC-085, SCN-12, SCN-04/07/LOOP-C, SCN-13 | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit E (each a named door waiting on another lane's state; not built ahead of its reader) |
| §13 SCN-05, SCN-02, ARC-23 | RESOLVED-BY / JORDAN | SCN-05: resolution 19. SCN-02 conflicts with ED-SC-0038 (named, SC's). ARC-23 (a skill required to attempt) is D-11 |
| §13 EMG-C2, NSC-05, SCN-08, NPC-052; EMG-X5, EMG-X7, SCN-07 (rate and table draws) | SUPERSEDED | WR's and CORE-side happenings closures (U5d); the mechanism (a keyed rate draw) exists |
| §13 NPC-001, NPC-004, NPC-075, ARC-22 (competence decides how she fares) | RESOLVED-BY | U1 architecture §6 (cast content) |
| §13 EMG-X6 | SUPERSEDED | SC (U5c) |
| §14, §15 | RESOLVED-BY | U1 architecture; `10_DICE_believed_odds_have_a_prior.md` |

## 3.4 `audits/16_PESSIMIST_DICE.md` — findings, lists, survivor

SOFT = `16_PESSIMIST_DICE_soft_ceiling.md`; TASK = `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`.

| id | claim (one line) | disposition | carrier | evidence |
|---|---|---|---|---|
| F-PES-DICE-01 | the degree changes no state (282 of 284 rolls) | SUPERSEDED | the verb lanes' closures (seven rows that write nothing in any band: SC, FI, verbs SOCIAL; U5c); the shape is `18_DETERMINISM_task_draw…` item 4 as reconciled | E-P6 |
| F-PES-DICE-02 | at the shipped pair "everything draws" means "little happens" | RESOLVED-BY | TASK (the unopposed stand-in, `plain`, the throughput reading and refusal to ship); applied to `18_DETERMINISM_task_draw…` item 3 and gate by this lane (Reconciled). The pool regime behind it is answered (A-6) | 16.5 % of today's effect at (2, 2.0) |
| F-PES-DICE-03 | the ceiling is a wall; every shipped forgery stands on it | RESOLVED-BY | SOFT (the cap's closed form follows the one sampler: DOE §1) | pools 1–12 read 10.00 % at their cap |
| F-PES-DICE-04 | a field is decided by a draw the dice engine never sees | JORDAN | D-34 (luck in battle: a hidden multiplier, or a named level) | friction's 5th–95th percentile 0.164–6.107 |
| F-PES-DICE-05 | a failed search is forgotten and retried; remembering alone changes nothing | RESOLVED-BY | DOE §4 (the actor-only deposit of `finding.none`, read by `refused_before` of `16_PESSIMIST_CORE_a_refusal_is_remembered.md`: the reader the control showed was missing). D-46 holds the neighbouring question for a missing person | 157 of 157 `finding.none` Events have no descendant; deposit alone: 19 of 42 against 20 of 47 |
| F-PES-DICE-06 | one die cannot succeed, and a zero cannot try | SUPERSEDED | A-6 (no person rolls under five dice); TASK for the unopposed rows | `band_odds(1, 2.0)` |
| F-PES-DICE-07 | the record of a roll is its band | RESOLVED-BY | MAP §D `fed_by` with SC-B's `Margin.terms` (U5c); the margin itself is on the record (under A-5 it is the continuous margin, not a settled integer) | 208 failures: by 1 ×76, 2 ×94, 3 ×33, 4 ×5 |
| F-PES-DICE-08 | the obstacle's floor reaches one term and not the sum | SUPERSEDED | `13_SC_tuning_tables.md` T1 (U5c) |  E-P1 |
| F-PES-DICE-09 | the field's four stat checks are bare binaries | SUPERSEDED | MB's closure (U5b) | `orchestration.py:2093-2166` |
| F-PES-DICE-10 | words: `argument.won` at Partial; a contest with one roller | SUPERSEDED | the verb table's owner lane (SC, U5c) | H-269 |
| §1.2 false N-lines | RESOLVED-BY | mass battle's roller: the one-roller proposal; `BandExtension` and the unused functions: DOE §1, §3; the top band and the three unused levels: A-6 and content | — |
| §1.2 "mechanisms that survive because nothing was tried": H-210's sweep arms are one arm; the 10 % floor is solved at no advantage; the two-roles gate has no row below Ob 1 | RESOLVED-BY | SOFT gate 3 (ordered words give ordered odds); DOE §3 row 11 (the floor is re-solved against the signed channel; the two-roles gate gains a row at an obstacle below 1) | — |
| §6 survivor (the form of fortune in a field) | JORDAN | D-34 | — |
| §7 corrections owed elsewhere | RESOLVED-BY / SUPERSEDED | 18-A: applied here (Reconciled). 13, SC-B: U5c (listed in `unified/U5_CONFLICTS_U5a.md` §3). The two `10_DICE_*` notes: DOE §3 row 11 | — |
