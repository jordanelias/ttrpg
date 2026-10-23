# Social contest and proceedings — completion proposal (T05 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/2026-10-22-system-description-06-t05-social-contest.md` (T05), `…-00-overview.md` §3, §6 (OV); `research/game_precedent_suite/dispositions/D_T05.md` (D); `research/game_precedent_suite/THROUGHLINES.md` (TL); `proposals/2026-10-16-verbs/2026-10-16-verbs-11-lexicon-social-contest.md` (L11), `…-21-gap-register-sc-and-gv.md` (G21, SC half); `proposals/2026-10-21-v9-remediation/` parts 02–04 (REM2, REM3, REM4); `proposals/social_contest_consolidation_integration_v1.md` (CIP, kernel-era); `workplans/valoria_master_workplan_v9_part5.md` (P5: IN-12 step 5, §J); `skills/ners/SKILL.md`; code opened where cited.

Abbreviations: `VT` = `engine/season/verb_table.yaml`; `ROS` = `engine/season/rosters.yaml`; `FX` = `engine/season/data/fixtures.py`;
`EI` = `engine/season/loop/effects_information.py`; `WQ` = `engine/season/queries/world_q.py`; `PQ` = `engine/season/queries/person_q.py`;
`SIG` = `engine/season/seam/wrappers/sigma.py`; `ROLL` = `modules/social_contest/roll.py`; `HR` = `engine/season/hole_register.yaml`.
`D:#n` is row n of `D_T05.md`. Odds quoted are T05 §2.2's exact enumeration (pool 2: Ob 2 → F .74 · P .19 · S .07 · O 0; Ob 1 →
F .42 · P .32 · S .25 · O .01); every other number is a fixture value at HEAD or is marked `illustrative`.

**What HEAD already has, read at the call site.** `determine` is contested (`contests: "a proposition"`, VT:383) and opens the docketed
arrangement's disposal graded by band (EI:515-552); it reads no bench room: `a proposition` carries no `heard_by` (ROS:1318-1322), so
`SIG::resolve` passes no room (`SIG:256`), and the party brings no opposition (`SIG::_opposition_of`, no `verb_capability` key). `speak` is
contested on `a matter`, whose row says `heard_by: "bench"` (ROS:1323-1328), and writes `[]` at every band (VT:1166-1171). The room is
`reception_gain · reception + proof_step · proofs` (`ROLL:104`), `reception` the bench's signed regard for the *actor's* deeds (WQ:553-611),
`proofs` the actor's unmirrored deed claims about the opponent (WQ:613-648). `argue` exists and writes the hearer's pursuits (VT:131-166,
EI:556-582). `interrogate` is not a row: v9 IN-12 step 5's remainder, held on `HR` H-226 (P5:54-63; HR:4760). B-N (proceedings core) and
B-O (contested `determine`) landed as T05 describes; nothing below repeats them.

## §0 The genre loop

The yardstick is the dialogue, negotiation and court RPG (Disco Elysium, Griftlands, BG3, Kingdom Come, Guild 2/3, Ace Attorney, Triangle
Strategy, Suzerain): a person builds a case, brings it before someone who decides, argues under stakes, and loses forward, while the world
does the same unwatched. In this engine every opportunity is a choice of acts at DELIBERATE, paid in scene actions, leaving claims,
Tenures, Records or pursuits behind.

| # | play opportunity: what the person chooses · at what cost · with what lasting consequence | precedent | today | evidence grade |
|---|---|---|---|---|
| 1 | **Spread word.** `tell` a held claim to whoever stands with him · one action and a journey to the hearer · the claim lives in every present ledger, chained to him, decaying 5 a season | D:#59, D:#73, D:#28 (HAS); TL P27 | AFFORDED, for true claims only | RUNS-IN-LOOP (`news.told` 4 · 7 · 6, seeds 0 · 1 · 2) |
| 2 | **Change a mind.** `utter` a Proposition, then `argue` it to a hearer · two actions · his held pursuits move toward the arguer's, and his later choices with them | D:#26 (LACKS); TL P33, P23 | PARTLY | TESTS-ONLY (`argument.won` = `argument.lost` = 0; every computed `argue` refused on `exists:Proposition`, T05 §4) |
| 3 | **Bring a matter.** `petition` then `carry` (no seat), or `open_case` (a seat granted `determine`) · an action and a hold · the matter waits on a docket across seasons | D:#17 (HAS), D:#75 (CONTRADICTS) | PARTLY: `carry` never passes admission; Rung matters sit undeterminable | RUNS-IN-LOOP (`petition` 14 · 7 · 11, `open_case` 6 · 1 · 5); `carry` TESTS-ONLY |
| 4 | **Build a case.** Put what one knows before the bench: tell a judge of the party's deeds (violence counts only if a judge saw it), have a prisoner questioned · travel to the bench, actions · the verdict weighs it | D:#18, D:#46 (LACKS); TL TM07, P26 | ABSENT: the verdict reads neither party nor room (VT:384) | DESIGN-ONLY |
| 5 | **Plead, and lose forward.** `speak` to a docketed matter; a lost hearing gives ground the next hearing starts from · an action · the hearing persists between sittings | D:#6 (HAS), D:#66, D:#13 (LACKS), D:#20 (DIFFERS); TL P25, P04 | PARTLY: `speak` runs and writes nothing; nothing passes to `determine` (T05 §5d) | RUNS-IN-LOOP, degenerate (seed 0: three Failures) |
| 6 | **Judge and bind.** `determine` a docketed person: a graded `oblige`, `detain` or `ban`; `pardon` closes a restraint · a seat, an action · the party joins the seat's establishment | D:#22, D:#44, D:#45 (HAS); TL P29 | PARTLY: binds, reading nothing about the party | RUNS-IN-LOOP at seed 1 only (one Partial); `detain`/`ban` TESTS-ONLY |
| 7 | **Give one's word, and pay for breaking it.** `utter`, `commit`, `covenant`; `release` · actions · a Tenure others can see | D:#53 (HAS), D:#58 (LACKS); TL P14 | PARTLY: binding exists; breaking is free | RUNS-IN-LOOP thin (`commit` once at seeds 1, 2); `covenant` TESTS-ONLY |
| 8 | **Win a chamber.** Lobby voters one by one; the count decides | D:#25, D:#57, D:#19 (LACKS); TL P09, TM03 | ABSENT in the season | TESTS-ONLY (kernel `VoteAtClose`) |
| 9 | **Deceive, and be caught.** Speak a falsehood; catch a liar by what others hold | D:#21 (LACKS); TL P28 | ABSENT for speech (J-C-6); documents can lie (`forge`) | DESIGN-ONLY for speech |
| 10 | **The world unwatched.** Grievances become petitions, cases, hearings and verdicts with nobody choosing them | TL throughline 6; P5:63 (RS-23) | PARTLY: filing runs; verdicts almost never | RUNS-IN-LOOP for filing; one verdict in three seeds |

Rows 4 and 5 are where the genre lives and where the engine is emptiest: a case cannot be built and a hearing changes nothing. This file
closes 4 and 5 and the formation defects under 2, 3 and 6. Rows 7, 8 and 9 stay where other owners already hold them (§1).

## §1 Gap ledger

Rows addressed: every LACKS row (16: #1, #5, #12, #13, #18, #19, #21, #25, #26, #34, #46, #48, #57, #58, #60, #66), every DIFFERS row D
marks as a risk or that bears on the odds question (7: #3, #4, #11, #20, #43, #49, #62) and the one CONTRADICTS row that is a game defect
(#75): **24**. The other CONTRADICTS rows (#30, #31, #37-#40, #71-#74) correct repo prose about precedent and are edit targets in other
files, not game gaps. DIFFERS rows resting on a ruling (#2, #33, #36, #42, #47) are not re-raised.

| gap | rows | what is missing, in engine terms | disposition |
|---|---|---|---|
| A · the verdict reads nothing | #18, #19, #57 | `determine` rolls pool 2 against Ob 2 for every party (VT:384); the bench's knowledge of the party and the hearing never enter | **CP-T05-01** (the bench's regard for the party enters the verdict); **CP-T05-02** (the remembered hearing enters it). #19 and #57 are closed in their verdict half: `reception` sums every seated judge, each through his own pursuits (WQ:553-611), so the bench is multi-member and agenda-bearing without a ballot. The ballot itself is gap F |
| B · failure leaves nothing, and repeats free | #5, #66, #13 | a failed `tell` re-forms at the same odds in the same season, because its Failure kind is its refusal kind (VT:1282, VT:1326-1329); a lost hearing is forgotten by the verdict | #5 → **CP-T05-03**. #66, #13 (proceedings half) → **CP-T05-02**: a turned speech counts against its side in the bench's memory. #13's regard half (a public loser regarded worse) → the existing CELL-VALUE AND COSINE PASS ask (P5:427, JQ-3's annex): `argue` is uncelled (ROS:3062-3067) and `speak`'s one cell (ROS:3414, "presses a docketed matter") reads the same at every band, through `align_kind`'s fall-back to the emitting verb (`data/verbs.py:1731-1743`), so a won and a lost hearing are regarded alike; their winning and losing kinds need separate `deed:` cells. This file authors no cell value. #13's fight half (a failed argument provokes a duel) → declined here, an interface demand on PC (§5) |
| C · persuasion never executes | #26 | no computed `argue` has a Proposition subject | **CP-T05-04** (formation class). The precedent's binary flip is declined: 5, architecture — pursuits are continuous weights and the sampler is the threshold; a flip beside the 10 % move would be a second ladder for one quantity (S) |
| D · docket formation | #75, #34 | `open_case` dockets Rungs that `determine` can never take off (D:#75); wrong-kind formations are charged a scene (D:#34) | #75 → **CP-T05-04** (`open_case` forms on a Person). #34 → REM-23, REM-24, REM-25 (`commit`, `petition`, `carry`) plus **CP-T05-04** (`argue`, `open_case`); a hand-built act keeps its refusal, which is the person's feedback. "Aptness priced, not refused" (RULED 2026-09-06) governs speech kinds, which nothing here builds |
| E · nobody can be questioned | #46 | `interrogate` has no row (H-226) | the row → v9 IN-12 step 5 (H-226's route is the orchestrator's). What an interrogation leaves → **CP-T05-05** (it counts as a hearing of the matter) |
| F · no vote, no address to many | #25, #48 | no counted `commit`; no audience operand | #25 declined: 1, superseded by v9's own hold — SC-01 step 11's vote-quorum conjunct waits on J-4 and `HR` H-161 (`workplans/valoria_master_workplan_v9_part2.md:249`; remediation part 01:228, "No item"), with L11 M12's `cardinality` count. #48 declined: 3, L11 Suite 2 parks `preach` on an audience operand, and the closed eight operands carry no set |
| G · speech cannot lie | #21 | `said_of` passes held claims only (`HR` H-198) | Jordan ask, existing: J-C-6 (L11 §3.9). Not re-raised. CP-T05-01 and CP-T05-02 are built so either answer works: a lie, if ruled in, enters the same ledgers the verdict reads |
| H · persons do not differ | #1, #3 | `Person.capability` empty on every realm person, pool 2 (SIG::_pool_of) | Jordan ask, existing: J-13's remainder (§J.2 rank 1, P5:348) with JQ-2 (REM4:32-55). Not re-raised. CP-T05-01 and CP-T05-02 make *parties* differ by what the bench knows of them, through the obstacle; J-13's "latitude enters through the pool only" binds latitude, and the room is already an obstacle term (ROLL:104), so neither item crosses it |
| I · promises cost nothing; no political currency | #58, #60 | `release` of a `commit` costs nothing modelled (`HR` H-205) | #58 → the CELL-VALUE pass (existing ask, as gap B): `commitment.ended` needs its own `deed:` cell so witnesses regard a broken word; FA owns `covenant`'s readers (§5). #60 declined: 5, architecture — the scene budget is the one throttle (TL P05, HAS); a second currency would be a second ladder for one resource, and budget inflation by holds is H-92's (GV) |
| J · the played contest and its odds | #4, #11, #12, #43, #49, #62 | in-contest choice exists only in the kernel; no odds reach the player; computed choosers never estimate the room | #4, #43 → **T01 CP-T01-03** (orchestrator ruling R1: one odds function): its `odds_of(w, act)` composes `ROLL::obstacle` on the same record the roll reads, so the player's Act interface shows the TRUE odds, room terms of CP-T05-01/02 included (AX-7, `architecture/meta/01_AXIOMS.md:299-304`). WQ:525-532 forbids *decision code* from reading the room; it does not bind the player's display. #62 → T01's `estimated_odds` (mode b, believed inputs only, AX-2): SC's bench estimate is a caller of it, not a third function; whether expected success enters the NPC score is AQ-X1, carried by T01 §6, not asked here. #11, #12 declined: 1, the kernel's retirement timing is Jordan's (SM-15) and the roll is kept by ruling (`ROLL:16-18`; ED-SC-0037). #49 declined: 3, signed per-choice increments are a display, which the brief excludes; the odds half is T01's |
| K · the accused has no voice | #20 | a docketed party never forms a `speak` on his own matter (VT:1165, `opening_set`'s contested-verb rule) | **CP-T05-02** (iii): a new column, `subject_may_be_self`, waives `opening_set`'s self-subject decline (`decision/options.py:261`) for `speak`, so the party may answer for himself; a third-party advocate for the defence is not built (§7) |

Outcome count, each row under its primary disposition: closed by a CP item **10** (#5, #13, #18, #19, #20, #26, #46 with v9's row,
#57, #66, #75); closed by named remediation items **1** (#34: REM-23, REM-24, REM-25, with CP-T05-04); existing Jordan asks **4** (#1, #3
→ J-13/JQ-2; #21 → J-C-6; #58 → the CELL-VALUE pass); routed to a sibling proposal's item **3** (#4, #43, #62 → T01 CP-T01-03, paper
like this file); declined **6** (#11, #12, #25, #48, #49, #60). New Jordan asks: **0**. #13 is split three ways and counted once.

## §2 Items

Five items. Every one binds **Layer 2** (the game code and the data `engine/season/` reads at runtime); none adds a guard, a store
on a Record or Person, or a resolver. Every new number is a fixture in `FX` (the one Python owner) with an `HR` row of kind NUMBER,
swept with a control arm that reproduces today. Summary first, blocks after.

| item | what it adds | owner artifacts | primitives | size | hash at control |
|---|---|---|---|---|---|
| CP-T05-01 | the verdict hears the bench: `determine` contests `a matter`; the room gains the bench's regard for the opponent | VT, `SIG::contest_input`, `queries/inputs.py::SocialContestInput`, `ROLL::obstacle`, FX, HR | P23, P11, P27, P01 | S | mover (the prize move alone reads a room) |
| CP-T05-02 | the bench remembers the hearing, and the accused may answer: a Query over the bench's ledgers of `speak` outcomes enters the verdict's room; a docketed party may form `speak` on himself | WQ (one Query), VT (`speak`'s column), `data/verbs.py` (one loader rule), `decision/options.py:261` (one condition), SIG, `SocialContestInput`, `ROLL::obstacle`, FX, HR | P25, P04, P03, P27 | M | equal for the Query at `hearing_step` 0; mover for the self-plea formations |
| CP-T05-03 | a failed telling is realised: `tell`'s refusal gets its own kind | VT, `data/verbs.py` (`KIND_VERB`), the readers of `news.untold` | P07 | S | mover |
| CP-T05-04 | formation: `argue` classed `Proposition`, `open_case` classed `Person`; a docket question puts docketed matters a person knows of before him as plain referents for `speak` and `determine` | VT (`referent_class`), WQ (one question in `questions_for`) | P24 (formation as typed gate) | S | mover per row |
| CP-T05-05 | questioning is part of the hearing: `interrogate` (once v9 builds it) contests `a matter`, so a prisoner who breaks or holds out moves the case | VT (`interrogate`'s `contests:` cell) | P25, P23 | S | equal until `interrogate` executes |

### CP-T05-01 · The verdict hears the bench

- **What it adds.** (i) `determine`'s `contests:` moves from `"a proposition"` to `"a matter"` (VT:383-384), the prize whose row already
  says `heard_by: "bench"` (ROS:1323-1328). No prize row changes; `a proposition` keeps `argue` alone. The room is then read at the act's
  place, as for `speak` (`SIG:253-256`). (ii) A third room operand, `opposed`: the bench's signed regard for the **opponent**, read by the
  existing `WQ::reception(w, opponent, venue)` (WQ:553-611) with the opponent in the speaker's slot. It is carried raw by
  `SIG::contest_input` (SIG:178-183) beside `reception`, and is `0.0` where the opponent is the actor or no person (the rule `proofs`
  already states, WQ:633). (iii) `ROLL::obstacle`'s room becomes
  `reception_gain · reception + proof_step · proofs − opposed_gain · opposed` (today `ROLL:104`). One formula for every prize a bench hears:
  `speak` gains the term too, so pressing a matter against a man the bench disvalues is easier, and against one it values harder.
- **Owner artifacts.** VT (one cell and its note); `queries/inputs.py::SocialContestInput` (one field, default `0.0`, the no-room
  reading); SIG (one read); ROLL (one term); FX `opposed_gain` with an HR row (NUMBER, swept `0` control / `0.5` / `1.0`).
- **Primitives.** P23 (seeded draw against a difficulty), P11 (pairwise regard, here judge to party), P27 (what the bench was told),
  P01 (a signed sum over holders). Template TM07 (testimony to verdict), whose verifier half is refused by axiom (D_T06:22) and is not
  built: the bench weighs what it holds, true or not.
- **Reads / writes.** Reads each seated judge's own ledger through `PQ::attributed_deeds` and `PQ::deed_term` (the reads `reception`
  already makes); writes nothing new. `determine`'s writes (VT:385-389) are unchanged; only its band distribution moves.
- **Joins.** GV: the bench is `WQ::judging_set` unchanged. FI: an inquiry's findings and `forge`'s documents reach judges' ledgers by
  existing deposits; nothing is asked of FI. PC: a killing or a wounding is a deed judges value through `deed:person.died` and
  `deed:body.changed` cells (ROS:3423-3424, 3485-3486); nothing is asked of PC. NP: each judge's valence is his own pursuits.
- **Decision handed to the chooser.** Whom to tell what, before the verdict; which bench to bring the matter before (its members'
  memories differ). **Unwatched:** every verdict in the realm now reads what that bench happens to know of the party, so two parties
  docketed alike fare differently, and a judge who saw the deed binds more readily than one who did not.
- ⚠ **Hearsay does not name a doer of violence, and this item keeps that rule.** A told copy of a `PAIRED_KINDS` claim names nobody
  (`PQ::attributed_deeds`, PQ:145-148): measured at HEAD the paired kinds are `body.changed`, `contest.undecided`, `finding.made`,
  `person.died`, `pursuit.moved`, `tenure.closed` (`PQ:190`, read by import). So a killing reaches the verdict through `opposed` only if
  a judge saw it; a witness who tells the judge of it moves nothing here, and moves the verdict instead by pleading (CP-T05-02). Unpaired
  deeds (a forged Record, a filed petition, a seizure) reach the bench by telling. Loosening the rule would change who counts as a doer
  in every reader of `attributed_deeds` (`reception`, `proofs`, `deeds_judged`, the scar), an asymmetry hazard this file does not take.
- **Falsifier.** A hand-built world: one judge holds one firsthand deed claim of the party's that his pursuits disvalue, at a magnitude
  giving `opposed_gain · opposed ≤ −1.0`; a second world identical but for that claim. At `opposed_gain = 1.0`, `determine`'s composed
  obstacle is 1.0 in the first and 2.0 in the second (the floor `OB_MIN` 1 and ceiling 2, `ROLL::obstacle`). The item is wrong if the
  two obstacles are equal, or if `argue`'s obstacle in the same worlds moves (its prize hears no room). **Under the derived-ceiling arm**
  (T01 CP-T01-06: the ceiling is the highest Ob at which a Success is still possible for the actor's pool, `2 · pool − 1` as filed, 3 at
  pool 2; never below `OB_MIN`, per the orchestrator's ruling R2): a third world where the judge *values* the deed at
  `opposed_gain · opposed ≥ +1.0` reads 3.0 against 2.0, which the shipped ceiling clips to 2.0. That half is observable on the derived
  arm only.
- **Control.** Three arms on seeds 0-2, two seasons, plus the hand-built worlds, **each run under both ceiling arms** (shipped `2`;
  derived, CP-T01-06): A today; B prize moved, `opposed_gain = 0`; C prize moved, `opposed_gain = 1.0`. Read per `determine` act the
  composed obstacle and band, and per `speak` the same. It can observe the failure: B against A isolates the prize move (the judge's own
  `reception` and `proofs` now read); C against B isolates the new term; derived against shipped isolates the hostile half. With T01's
  CP-T01-04 (the margin's fraction settled by the act's own draw) a room below 1.0 moves odds too, so the null reading in §7 holds only
  on the arm without it. ⚠ The realm forms one `determine` in three seeds (T05 §0), so the realm arms are weak and the hand-built
  worlds decide; say so in the commit.
- **Declared hash movers.** Arm B moves every world in which a `determine` rolls at a bench whose `reception` of the judge or whose
  `proofs` is non-zero; arm C also moves `speak`. T01 CP-T01-06 lists `determine` and `speak` among its movers (R2); with this item the
  bench room on `determine` is one of the things its derived arm un-clips. **Revert:** the prize cell; the field; `opposed_gain = 0`.
- **Assignment hazard (§0.1 pt 1).** No field's getter changes source. The composed obstacle is a pure function of the record; its one
  owner is `ROLL::obstacle`, and `test_sc01_obstacle_ceiling.py` already fails if a host-side obstacle returns (`queries/inputs.py:54`).

### CP-T05-02 · The bench remembers the hearing, and the accused may answer

- **What it adds.** (i) One Query, `WQ::hearing(w, matter, venue)`: over the seated bench (`judging_set`), the claims each judge holds
  whose subject is `matter` and whose predicate is a band kind of a row contesting `a matter` (read off those rows' own keyed `emits:`,
  never a second table: `speak`'s four, VT:1172-1176; after CP-T05-01, `determine`'s; after CP-T05-05, `interrogate`'s). Each counts
  `remove_weight(c.source) · c.confidence / full · DEGREE_STEP[band]` (`data/rosters.py:851`; `speak`: carried +2, advanced +1, held 0,
  turned −1), where a kind a row emits at more than one band counts 0 (`matter.determined` is emitted at three bands, VT:393-395, and
  the matter leaves the docket with it; `matter.undetermined`, Failure only, counts −1: a hearing the bench did not carry). The sign is
  **−1 where the act was the party's own** (the sighting's `who` is the matter), +1 otherwise. Positive is the case against the party. The method is `reception`'s (remove, confidence, a sum over the bench), so one
  hearing and one regard are weighed alike (S). (ii) A fourth room operand, `hearing`, carried by `SIG::contest_input` for a bench-heard
  prize, and `ROLL::obstacle`'s room gains `+ hearing_step · hearing`, so after CP-T05-01 `determine` reads it. (iii) A new row column,
  `subject_may_be_self: true` [coined here: *a contested row whose opponent is its `subject` may be formed by that subject on himself*],
  declared on `speak` alone. What bars a plea today is not a counterparty clause (`speak` declares no `counterparty:`, VT:1165, so the
  fold's self clause never fires, `loop/resolve.py:314-321`) but `opening_set`'s self-subject decline, `if opposes_subject and subject ==
  p.id` (`decision/options.py:261`, `subject_is_opponent` at :343-352). The column waives that one line for the row declaring it; the
  loader admits it only on a row `subject_is_opponent` reads as contested against its subject (no `counterparty:`), as it admits
  `counterparty_may_be_self` only where the fan reaches (`data/verbs.py:691-703`). `confer`'s `counterparty_may_be_self` is NOT the
  column: the loader refuses it on a row with no counterparty the known-person fan fills. So a docketed party forms a `speak` on his own
  matter: a plea. `choose.py:106`'s stance-polarity term reads his stance toward himself, which no stance row names (0) [UNVERIFIED].
  His opponent is then himself, so `opposition` is `None` and the obstacle starts at
  `obstacle_default`; `proofs` and `opposed` read `0.0` for a self-opponent (WQ:633's rule); `reception` is the bench's regard for him.
- **Why a Query and not a tally on the docket.** A written tally was drafted and cut at §3: the bench's memory of the hearing already
  exists in the judges' ledgers (WITNESS deposits every `speak` outcome to those present, T05 §2.3), it can be told onward, contested
  and forgotten (MATTER decay), and a stored tally would be the knowledge kept on the thing known (NERS §3, disqualifier 1).
- **Owner artifacts.** WQ (the Query); VT (`speak`'s column and note); `SocialContestInput` (one field); SIG (one read); ROLL (one term);
  FX `hearing_step` with an HR row (NUMBER, swept `0` control / `0.5` / `1.0`).
- **Primitives.** P25 (attrition-pool contest: a two-sided bar, Bannerlord's persuasion bar, Ace Attorney's gauge), P04 (the case
  advances across sittings), P03 (old pleading fades with the claims that carry it), P27.
- **Reads / writes.** Reads judges' ledgers and `speak`'s row; writes nothing. `speak` stays `writes: []` at every band (VT:1166-1171),
  so REM-06's third conjunct is still met by `determine`, not by `speak`.
- **Joins.** GV: a sitting (`convene`, REM-28 for its refusals) is where speaker and bench share a place; no interface change. NP: none.
  FI: none. The chooser lane: `speak`'s one alignment cell (ROS:3414) now prices a plea as well as a prosecution; whether that cell is
  right for a plea is the CELL-VALUE pass's.
- **Decision handed to the chooser.** Whether to plead, where (before the judges, or to a hearer who will tell them), and when: a turned
  speech is remembered against its side, so a weak speaker who presses can hurt his own case. The accused chooses whether to answer.
  **Unwatched:** persons who know a matter is docketed speak to it (CP-T05-04's docket question); judges present remember; the verdict reads it.
- **Falsifier.** A hand-built world: two judges co-located with three speeches on one docketed party (Success, Success by others; one
  Failure by the party himself). `hearing` = 2 × (1 + 1) firsthand, and the party's turned plea counts −1 × −1 = +1 per judge, so
  `hearing` = 6 at full confidence; at `hearing_step = 0.5` the verdict's room gains 3.0 and the obstacle sits at the floor. The item is
  wrong if `hearing` reads the same with the judges absent at the speeches (nothing was witnessed), or if the party's carried plea counts
  toward the case against him. **The plea itself, first:** a person docketed, holding the docketing claim, whose question carries his
  own matter, forms `speak {subject: himself}` under `subject_may_be_self` and forms none with the column removed (`options.py:261`
  declines it); a hand-built plea admitted by the fold rolls with `opposition` `None` and `proofs` 0. The item is wrong if the
  Candidate forms without the column (the decline is elsewhere) or fails to form with it.
- **Control.** `hearing_step = 0` against `0.5` on the hand-built world and seeds 0-2, **under both ceiling arms** (shipped `2`; derived,
  T01 CP-T01-06): at `0` every `determine` band is today's by construction; at `0.5` a `determine` whose bench holds `hearing ≥ 2` must
  show a lower obstacle on both arms, and one whose bench holds `hearing ≤ −2` (the party's pleas won) a higher obstacle on the derived
  arm only (the shipped ceiling clips it). Read also, in the realm, the number of
  bench-held `matter.*` claims per docketed matter: a zero there is a **null result to report**, meaning speakers and benches never share
  a place, not a pass.
- **Declared hash movers.** (i)+(ii) equal at `hearing_step = 0`. (iii) moves every world in which a docketed party is offered his own
  matter (new formations). **Revert:** the column; `hearing_step = 0`; the Query has no other reader.
- **[UNVERIFIED].** Which id a `speak` Event's deposits name: the matter by the empty-changes fallback (EI:509-514 says a `determine`
  Failure's claim lands on the party, which supports this) or the speaker by the `actor` rule (`epistemic.py:188`). `Claim` carries no event id (`state/carriers.py:291-319`), so if
  the deposit names the speaker the Query cannot find the matter, and the build must first make `speak`'s deposit name its matter
  through `claim_subjects`' rule roster (H-79), a declared rule choice, not a field. Conversely, if the deposit names the matter,
  `PQ::attributed_deeds` (an unpaired kind's claim is its subject's deed, PQ:144-145, `HR` H-192) already counts every speech about the
  party as the party's own deed, valued by `speak`'s cell, so CP-T05-01's `opposed` would count the hearing a second time; the build
  excludes the band kinds of `a matter`'s rows from `opposed` [ASSUMPTION; medium; revert: accept the double count and halve nothing]. Also: a told copy carries no `seen`
  (`PQ::attributed_deeds`, PQ:146-148), so a plea heard second-hand counts with the pressing sign [ASSUMPTION; medium; revert: told
  copies count 0].

### CP-T05-03 · A failed telling is realised

- **What it adds.** `tell`'s `emits_on_refusal` (VT:1326-1329, keys `holds`, `hearer`, `counterparty`) names a new kind,
  `tell.refused`; the Failure band keeps `news.untold` (VT:1282). The loop already drops a realised act until the next season
  (`loop/driver.py:443, 488-503`; `loop/deliberate.py:305-340`) and counts an act realised when none of its Events is a refusal kind, so a
  failed telling stops re-forming at the same odds within the season, as a failed `argue`, `speak` or `determine` already does
  (VT:160-162, 1176-1178, 396-399). Two kinds on a contested keyed row are lawful since K-02's party-gap fold edit (VT:201, `arrest`).
  The U1 note that the row "introduces no new event kind" (VT:1288-1292) is superseded and says so.
- **Owner artifacts.** VT; `data/verbs.py::KIND_VERB` (the new kind maps to `tell`).
- **Primitive.** P07 (change lockout after a failed attempt; Victoria 3's failed-law cooldown is the closest member).
- **Reads / writes.** None new. ⚠ **The read side is the hazard here:** a kind string read in several places changes meaning. The
  readers of `news.untold` outside tests at HEAD are `epistemic.py`, `decision/options.py`, `loop/witness.py`, `queries/person_q.py`,
  `data/verbs.py`, `seam/__init__.py`, `harness/corpus_run.py`, ROS, `engine/season/requirements.yaml` and HR (grep). Each must be read
  and told whether it meant the refusal or the loss before the split lands; `ctl/control.py`'s REF list (T05 §0a) is an instrument and
  is re-read, not edited to fit.
- **Joins.** None. FI's graded inquiries borrow `tell`'s roll, not its row; unchanged.
- **Decision handed to the chooser.** A failed telling costs the opportunity for the season: tell someone else, tell something else, or
  wait. **Unwatched:** rumour no longer grinds through by repetition inside one season.
- **Falsifier.** A hand-built world: a teller fails a `tell` of one claim to one hearer in round 1; in round 2 no identical Candidate
  forms. Today it does (T05 §5c, `p_npc_086`'s second `tell` drew `news.told`). Also: an absent hearer still emits a refusal and the
  Candidate re-forms next round.
- **Control.** Seeds 0-2, two seasons: `tell` attempts and `news.told` per season, before and after. A fall in `news.told` is the price
  and is reported.
- **Declared hash movers.** Every world in which a `tell` fails. **Revert:** the kind.

### CP-T05-04 · Formation for the proceedings verbs: two classes and one docket question

- **What it adds.** (a) On REM-21's stamper registry (REM2:324-359; it must land first), two `referent_class` declarations in VT, each
  REM-22's shape and each the carrier's own type name (ROS:613-614): `argue` → `Proposition` (the arguer's own uttered Propositions reach
  his question through the maker's hold, VT:307); `open_case` → `Person` (REM-24's class). **`argue`'s class is this item's;** T02's
  CP-T02-05 stamps `argue` (and REM-23's `commit`) under the same `Proposition` class and cites this item, so there is one class, one
  stamp and one owner per row. (b) For `speak` and `determine`, **no class**: a class must be the referent's own type, and a docketed
  matter's type is `Person` (or, for a legacy item, `Rung`), so a `DocketItem` class would carry persons under a name that is not their
  type, and `determine`'s `party` conjunct (VT:361-366) needs the Person. Instead `WQ::questions_for` gains the sitting question's
  sibling (WQ:2621-2631): one standing question per person whose **plain referents** are the docketed matters whose docketing Event
  (`case.opened`, `petition.carried`) his own ledger holds a claim of, the ledger test `sittings_before` makes (WQ:276-305), under the
  same `claim_landed` source. Both rows keep forming on plain referents, so nothing is narrowed: the sitting route (a judge holding
  `date.fired` but no docketing claim) is untouched, which a class would have dropped (`state/carriers.py:484-485`). Decision code still
  receives ids only (AX-2).
- **What each closes.** `argue` executes at all (D:#26: 10, 17, 18 formed at seeds 0-2, every one refused). `open_case` stops docketing
  Rungs `determine` can never take off (D:#75); a hand-built act may still docket a Rung, which a later `Record` disposal (L11 M5) needs.
  `speak` and `determine` **reach** dateless docketed matters a person knows of, not only a sitting's (`sittings_before` asks only about a
  fired Date, which seed 0 never writes). **Not closed:** `speak` still forms on undocketed plain referents and is refused there (seed 0:
  22 formed, 18 `speech.unheard`, T05 §4); removing that needs a decline no carrier type can express, and is left as a residue.
- **Owner artifacts.** VT (two columns and notes); WQ (one question in `questions_for`, beside the sitting question).
- **Primitive.** P24 (a deterministic gate decides what may be attempted, before any draw).
- **Reads / writes.** The question reads `World.docket` and the person's ledger; writes nothing.
- **Joins.** NP/the chooser: none beyond REM-21. GV: the bench. FA: `argue` moving members' pursuits now reaches faction members. T02:
  CP-T02-05 cites (a).
- **Decision handed to the chooser.** None new: it removes choices that could never succeed and adds matters a person could act on,
  which is what makes rows 2-6 of §0 reachable in computed play at all.
- **Falsifier (per row).** A question carrying a Proposition and a person forms `argue` on the Proposition only; a question about a Rung
  and a person forms `open_case` on the person only; a person holding `case.opened` of a dateless docketed matter is asked about it and
  forms `speak` on it, and one holding no such claim is not asked; a judge holding `date.fired` and no docketing claim still forms
  `determine` from the sitting question.
- **Control.** `aperture 1 s`, s = 0, 1, 2, on the base commit (REM-22's protocol). **Stopping rule (agreeing with T02's):** if
  `argument.won` + `argument.lost` stays 0 after `argue`'s class, record the residue (no Proposition reaches an arguer's question) and
  do not widen the `Proposition` stamp beyond what REM-21 and T02's CP-T02-05 define (T02 drops `release` from it on the same rule).
- **Declared hash movers.** One per row; one for the docket question. **Revert:** each column; the question.

### CP-T05-05 · Questioning is part of the hearing

- **Depends on** v9 IN-12 step 5 building `interrogate` (P5:63) by whichever of H-226's routes the orchestrator takes (HR:4760). This
  item does not choose the route and does not repeat the row; it gives the row a product, which #453 left `writes: []` at every band
  (H-226's `default`: "`confession.made` is no event kind").
- **What it adds.** One cell: `interrogate`'s `contests:` names `"a matter"`, the prize whose rows CP-T05-02's `hearing` reads. The row
  reads a docketed charge already (P5:64, "the petition the docket names"), so it is a hearing of a docketed matter held in custody;
  its band kinds (its builder's names) are then remembered by the bench present on the one ladder, like `speak`'s. ⚠ For `hearing` to
  read them they must be one kind per band, as `speak`'s are: a kind emitted at several bands counts 0 (CP-T05-02 (i)). That is a
  requirement on the row's builder, stated here so the row is not built with one `confession.made` at two bands. A prisoner who breaks moves the case
  against him; one who holds out moves it back. `interrogate` stays `writes: []`; the bench room it now reads (`heard_by`) makes a
  prisoner the bench disvalues easier to break.
- **What was drafted and dropped.** Depositing the prisoner's own deed claims into the interrogator's ledger: a told copy of a killing
  names nobody (CP-T05-01's hearsay rule, PQ:145-148), so the deposit would carry the claim and lose the doer.
- **Owner artifacts.** VT (`interrogate`'s `contests:` cell and note). Nothing else.
- **Primitives.** P25, P23 (with P29 through `determine`).
- **Joins.** GV: `arrest` opens the `detain` (VT:167-204) `interrogate` reads; `pardon` closes it. FI: `interview` (R-07, the
  non-custodial row) is untouched.
- **Decision handed to the chooser.** Arrest, question, then judge: the seat's holder chooses the order and whom. **Unwatched:** a seat's
  agents arrest, question and bind with no player; the arrest-to-verdict chain closes inside one seat.
- **Falsifier.** A hand-built world: a detained, docketed party; `interrogate` at Success with one judge present; `hearing` for that
  party reads +1 (or +2 at Overwhelming) and the verdict's obstacle at `hearing_step` 0.5 falls by 0.5 (or 1.0). Wrong if `hearing` is
  unchanged, or moves with no judge present.
- **Control.** The same world at `hearing_step = 0`: every `determine` band is unchanged.
- **Declared hash movers.** None until `interrogate` executes; then every world where it rolls. **Revert:** the cell.

## §3 NERS

Method per `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. The pass is over this file's five items and the drafts cut on the way.

### N — the cut test, item by item

| item | N-line (cut it and the game cannot …) | attack run | verdict |
|---|---|---|---|
| CP-T05-01 | … let what the bench knows of a man decide whether it binds him: every party faces the same .26 (D:#18; T05 §5d) | *Does CP-T05-02 carry it?* No: the hearing Query reads hearings, not deeds. *Does `speak`'s room carry it?* No: `determine` and `speak` are separate rolls and nothing passes between them (T05 trap 2). *Is it a flat bonus (disqualifier 5)?* No: a signed sum over the bench's own ledgers, zero where the bench knows nothing. Directions: top-down (a lord's judge acts on what he saw), lateral (judges tell one another of unpaired deeds), diagonal (an inquiry's finding reaches a bench), horizontal (a judge's pursuits value a rival faction member's deeds); bottom-up and vertical hold only for unpaired deeds, since a told killing names nobody | **N HOLDS** (narrowed in two directions by the hearsay rule) |
| CP-T05-02 | … let pleading change a verdict, or let a lost hearing cost its side anything the next sitting starts from; and the accused cannot answer | *Disqualifier 1, the carrier already exists:* fired against the first draft (a `tally` on the case Record), which was cut for it; the Query reads the existing carrier, the judges' ledgers. *Disqualifier 3, already cut:* L11 M7's stasis `issue` rung is a richer store for the same job, never built; this replaces it with no store. Walk without the item: a plea reaches the bench's ledgers (WITNESS) and nothing reads it there, so the step "the verdict weighs the hearing" has nothing to name | **N HOLDS, NARROWED**: the hearing counts only where speaker and bench share a place or the speech is told on; in the realm that may be almost never (§7) |
| CP-T05-03 | … make a failed telling cost the opportunity, as every sibling contested row's failure does | *Is it pacing only?* It changes no outcome a single act can reach; it changes per-intention odds (T05 §5c: 1 − .74^k by repetition). The S defect (one contested row whose loss is its refusal) survives any attack: siblings disagree in method | **N HOLDS, NARROWED** to S (consistency), lateral direction (gossip) |
| CP-T05-04 | … run `argue` at all, keep the docket determinable, or let a person speak to or judge a matter he knows is docketed | *Do REM-23..25 carry it?* They class `commit`, `petition`, `carry`, `found`, `build` only. Without it, CP-T05-01 and CP-T05-02 have inputs nobody forms | **N HOLDS** |
| CP-T05-05 | … let a prisoner's breaking or holding out move the case against him | *Does `speak` carry it?* A speech is the speaker's, before the bench; questioning is the seat's, in custody, and is the only hearing a detained man cannot avoid. *Disqualifier 2, no producer?* The producer is v9's row, not yet built. One direction (top-down: seat over prisoner) | **N HOLDS, NARROWED**, and conditional on v9 building `interrogate` (H-226); one cell, ordered last, and the first cut if that row stays unbuilt |

**Cuts taken during drafting (false N-lines and rejected additions):**

- *A written `tally` on the case Record, moved by `speak`.* FALSE N-LINE (disqualifier 1): the judges' ledgers already hold every
  witnessed hearing, and can be told, contested and forgotten. It would also have added a field, a write-matrix row, a docket key and an
  effect body. Replaced by CP-T05-02's Query.
- *A reader for the six speech kinds (L11 M8).* Cut: `tell` to a judge (evidence, CP-T05-01) and `speak` (rhetoric, CP-T05-02) already
  move two different states, which is Guild 2's split (D:#18) and the menu-collapse test COMP-1 warns of (G21 SC-G51). A kind menu over
  the same two states adds choices that differ only in magnitude. The roster stays loaded data, DESIGN-ONLY, as today.
- *The stasis `issue` rung (L11 M7, SC-G12, SC-G29).* Cut for CP-T05-02: one signed sum on the one ladder carries persistence between
  sittings without a ladder of positions.
- *A confession that hands the interrogator the prisoner's deed claims (a `teller: counterparty` channel column).* FALSE N-LINE: a told
  copy of a paired deed names no doer (PQ:145-148), so it would carry the claim and lose who did it. Replaced by CP-T05-05's one cell.
- *Separate `deed:` cells for winning and losing kinds, and for `commitment.ended`.* Not an item: cell values are a judgment the
  producer does not own (ROS:3057-3060, `covenant`'s reason); routed to the CELL-VALUE pass (§1 gaps B, I).
- *A binary persuasion flip (Triangle's threshold), and a defence advocate row.* Cut: a second ladder for pursuits (S); a second row over
  `speak`'s kinds whose side the witnessed claim cannot carry (C3: the judge must be able to know whose side a speech took; he can
  know the speaker was the party, which is all CP-T05-02 (iii) reads).

### R

- **R-WORLD.** Every seated judge in the realm now carries a verdict-relevant memory, so cases differ by who saw what, unwatched: a
  killing seen by the bench is bound more often than one it never heard of; a party's own plea, made where the bench sits, can save
  him; a seat that arrests and questions closes its own case. These are hooks the world throws with nobody choosing.
- **R-PLAYER** (a seat a player can occupy: any person). Choices that were absent: whom to tell before the hearing, where to plead,
  whether to answer one's own case, whether to press with a weak voice. *Remove the alternatives:* if pressing always helped, pleading
  would be a corridor; a turned speech counting against its side keeps it a gamble at the shipped odds (F .74 at Ob 2).
- **Completeness at the extremes.** No bench, or a bench knowing nothing: every term is 0.0 and the verdict is today's (no break). A
  bench that loves the party: under the shipped `obstacle_ceiling` 2 (`ROLL::obstacle`'s stated property; FX:419) the hostile half is
  clipped, so good standing, a winning plea and a defence cannot raise a verdict's obstacle above 2. **This incompleteness is not this
  file's to fix:** the ceiling has one owner, T01 CP-T01-06 (ruling R2), whose derived ceiling (3 at pool 2 as filed) un-clips it. With
  CP-T01-06 the defence half is complete; without it, it is not, and both readings are run (§2 controls).

### S

- **One room formula** for every bench-heard prize: today `speak` reads a room and `determine` reads none, two methods for one hearing;
  after CP-T05-01 both read the same four terms. **One ladder:** `hearing` uses `DEGREE_STEP`, the steps `argue` and `determine` already
  read (VT:155, EI:535). **One weighting:** `hearing` weighs remove × confidence as `reception` does.
- **Pauses correctly.** A proceeding stays one act per hearing and one per verdict; no DELIBERATE nests in RESOLVE (H-56's held half is
  untouched); the interval between sittings is where others act (tell the bench, arrest, flee).
- **Zoom.** The bench is `judging_set` at any rung above the person tier; nothing here is settlement-only.

### E (scored last, as a ratio)

- **E-OVERHEAD, counted.** In: 2 prize cells (`determine`'s moved, `interrogate`'s set), 2 room operands (`opposed`, `hearing`), 1
  Query (`hearing`; `opposed` reuses `reception`), 2 fixtures, 1 new column (`subject_may_be_self`, on `speak` only) with its loader rule, 2 class columns
  on existing classes and 1 question beside the sitting question, 1 event kind (`tell.refused`). Out: nothing deleted; 1 drafted store,
  1 drafted reader, 1 drafted ladder, 1 drafted deposit channel and 1 drafted class (`DocketItem`, not a carrier type) cut before filing.
  No verb added, no store added, no resolver touched. The vocabulary grows by one kind and one column name.
- **E-LEGIBILITY.** The outcome is predictable from the choice without running the engine: "the judge binds a man more readily if he
  saw or was told what the man did, and if the hearing he remembers went against the man." Opaque part: the magnitudes (two fixtures
  and the integer net, T05 §2.2: a room below 1.0 does nothing), which a player cannot see.
- **Ratio.** High against what N and R found: rows 4 and 5 of §0 go from ABSENT/inert to afforded with no new store. The weakest ratio
  is CP-T05-03 (a kind split whose gain is pacing and consistency), kept for S.

## §4 One season, after

All names are roles; numbers are `illustrative` unless they are T05 §2.2's enumerated odds or a shipped fixture.

1. **Before the season.** A cottar witnessed a reeve kill her brother (a firsthand `person.died` deed claim, paired, `seen.who` the
   reeve). The reeve holds the same deed (he did it).
2. **Round 1.** She files `petition {to: reeve, subject: reeve}` (H-94 still addresses it to its subject) and `carry`s it (REM-25): the
   docket item names the reeve. She holds the `petition.carried` claim, so CP-T05-04's docket question puts the docketed reeve before her.
3. **Round 2.** She travels to the hall where the district's judge sits (one leg) and `tell`s him her claim. Partial or better
   (P(≥ Partial) .26 at Ob 2) and the judge holds a told copy; it names no doer (a killing is a paired kind, CP-T05-01's hearsay rule),
   so `opposed` does not move. **If it fails**, CP-T05-03 bars that telling until next season. Either way the telling is not her lever.
4. **Round 3.** At the hall she `speak`s to the matter, pressing it: Success (P .07 at Ob 2). The judge, present, holds
   `matter.advanced` about the reeve: `hearing` +1.
5. **Round 3, unwatched.** The reeve, if he holds a claim of his matter's docketing, is offered it (CP-T05-04) and answers
   (CP-T05-02 (iii)). He draws Failure: `matter.turned`, his own plea, which counts +1 against him in the judge's memory. Had he drawn
   Success, `hearing` would have fallen by 1.
6. **Round 4.** The judge, offered the dateless docketed reeve (CP-T05-04), forms `determine`. His room: `hearing` = 2 at full
   confidence; `opposed` 0 (he saw nothing of the reeve's); at `hearing_step` 0.5 the room is 1.0 and the obstacle reaches the floor 1:
   F .42 · P .32 · S .25 · O .01 against today's .74 · .19 · .07 · 0. Had the judge himself seen the killing, `opposed` alone could do the
   same (illustrative). A Partial or better opens an `oblige` on the reeve, owned by him, on the judge's seat, carrying `oblige_term` 4
   (FX:892), graded with the band; the matter leaves the docket. A Failure emits `matter.undetermined`, which the judge remembers as −1
   for the next attempt: the case is weaker for having failed once.
7. **What the world did unwatched.** Elsewhere a judge whose ledger holds nothing about the party before him rolls at Ob 2, as today.
   The reeve's kinsmen, present at the hall, hold his turned plea and may tell it to a second judge. Next season the cottar's barred
   telling re-opens. Were the reeve arrested and questioned (CP-T05-05, once v9 builds `interrogate`), his breaking would count as a
   further hearing against him.

What this walk does **not** have in computed play at HEAD: step 2's petition against a killer is RS-23's EXIT, blocked on H-194, H-209
and H-225 (P5:63); until those land, the cottar's grievance does not form the petition unaided.

## §5 Order and dependencies

**Within the proposal.** CP-T05-04 first (after REM-21, and beside REM-23..25 in RB-2a), because the other items need their verbs
formed; CP-T05-01 next (it opens the room the others write into); CP-T05-02 after CP-T05-01 (its operand rides the same record);
CP-T05-03 at any point (independent); CP-T05-05 last, after CP-T05-02 and after v9 IN-12 step 5 builds `interrogate`. Each item is its own commit with its
own hash declaration.

**What it needs from other subsystems (interface, as expected).**

| from | interface needed | why |
|---|---|---|
| v9 remediation (RB-2a) | REM-21's stamper registry; REM-23, REM-24, REM-25 landed | CP-T05-04 composes on the registry; the petition route needs `carry` to form |
| v9 IN-12 step 5 (SC/GV) | an `interrogate` row on H-226's chosen route, reading a live `detain` | CP-T05-05 has no row to attach to otherwise |
| GV | `convene` executing more than once in five (REM-28's reading of its refusals) | sittings are where speaker and bench share a place, which CP-T05-02's hearing needs |
| PC | `challenge` able to form against a person whose `argument.lost` or `matter.turned` against oneself one holds | D:#13's fight half (a failed contest provoking a duel); declined here, offered to PC |
| FA | `covenant`'s deferred readers (`_renewals`, `mustered`, VT:311) | §0 row 7's broken-word half; SC's `commit` is shared |
| T01 (odds owner, ruling R1) | `odds_of(w, act)` composing `ROLL::obstacle` on the same record, so the player's true odds include `opposed` and `hearing`; `estimated_odds(p, c)` for NPCs on believed inputs, which SC's bench estimate calls (not a third function); CP-T01-06's derived ceiling, with `determine` and `speak` on its mover list | D:#4, #43, #62; the defence half (§3 R). Whether expected success enters the NPC score is AQ-X1 (T01 §6), not asked here |
| T09 (factions) | its counterparty-ties obstacle term ("M10") is a demand on `ROLL::obstacle` (ruling R10); it is observable only on the derived-ceiling arm | §7 |
| T08 (settlements) | its tax edict's `defy` depends on REM-2B (restoring IN-09's `evade / defy`); that is the only demand on SC, and it is REM-2B's scheduling, not an SC item | — |
| T06 (fieldwork) | cites CP-T05-03 (the `tell` Failure/refusal split) and J-C-6 if ruled in; drops its JA-1 for T01 CP-T01-06 (R2). No change here | — |
| the CELL-VALUE pass (P5:427) | separate `deed:` cells for `argue`'s and `speak`'s winning and losing kinds, and for `commitment.ended` | D:#13's regard half, D:#58 |
| NP | none beyond `PQ::stance_toward` and pursuits as they stand | — |

**What it gives them.** GV: verdicts that read the party and the hearing, so a seat's justice differs by what it knows. FI: a consumer
at the bench for every finding and every forged document (D:#31's "investigation and contest do not touch" stops being true). FA and
NP: a reachable writer of `Person.pursuits` (`argue` executing), so faction members can be talked round. PC: a killing becomes evidence.

## §6 Jordan asks and rulings touched

**New asks: none.** Each candidate was answered by the ladder:

| candidate | answer (step) |
|---|---|
| Should a verdict read the party's whole record or only deeds tied to the charge? | 5, architecture: no charge carrier exists (H-227; a computed charge waits on a `mood` source), so the party is the matter and his attributed deeds are the evidence; `proofs`' own named limit says the same (WQ:625-627) |
| Should the defence half bite under the shipped ceiling? | 1, superseded by a sibling owner: the ceiling is T01 CP-T01-06's (ruling R2; H-213's own row records step 5 answered it, `HR`:4601); this file states its controls under both arms and changes no ceiling |
| Should the accused be able to speak? | 4 and 5: IN-53 D2's `counterparty_may_be_self` is the precedent for waiving a self-exclusion by a declared row column (it cannot be reused: `data/verbs.py:691-703` refuses it on a row with no fanned counterparty); VT:1165 records the bar as a LIMIT, not a ruling, so the sibling column `subject_may_be_self` takes it |
| A vote / a chamber | 1: v9 holds it (SC-01 step 11 on J-4, H-161) |
| Adopt the kernel, or a played contest | 1: SM-15 is Jordan's and the roll is kept by ruling (`ROLL:16-18`) |
| A threshold flip for persuasion; a political currency; speech kinds | 5, architecture (§3 cuts) |
| Address a population (`preach`) | 3: L11 Suite 2 parks it on an audience operand |

**Existing asks and rulings these items touch, not re-raised:** J-C-6 (may a person lie; L11 §3.9) — nothing here depends on the answer;
J-13's remainder with JQ-2 (what sets a person's pool; REM4:32-55) — CP-T05-01 and CP-T05-02 vary outcomes by party through the
obstacle and leave the pool alone; ED-SC-0037 and `ROLL:16-18` ("KEEP THIS ROLL") — every item rolls through `social_contest.roll`;
ED-SC-0033 clause (3) (the obstacle has one owner) — both new terms are composed in `ROLL::obstacle` only; ED-IN-0210 ruling 1 (verbs
are not fiats) — a confession deposits what the prisoner holds and writes nothing of his will; R-10 (`carry` → `lodge`) — REM-25's
hash move is the row's next, where L11 asks the rename to ride; H-221 (`pursuit_shift`) unchanged; "aptness priced, not refused"
(RULED 2026-09-06) untouched, since no speech-kind reader is built. CIP (2026-08, kernel-era) is superseded in its kernel scope by
the roll ruling; its Jordan quote (CIP-14, 2026-08-06: audiences "carry out their impressions of the characters after the social
contest in the world") is intent for CP-T05-02 and the CELL-VALUE demand, cited for intent only.

## §7 Risks and what this deliberately does not do

**Risks.**

- **The realm may show nothing.** At HEAD the room bites only at 1.0 or more (T05 §2.2: the net is an integer); T01's CP-T01-04 (the
  margin's fraction settled by the act's own draw) removes that, so the integer-net null holds only on the arm without it. Realm
  magnitudes of `reception` are unmeasured (T05 §9); speakers and benches may rarely share a place; `determine` formed twice in seed 0.
  Each control reports a null as a null. The hand-built worlds carry the falsifiers.
- **The shipped ceiling clips the defence.** Under `obstacle_ceiling` 2 = `obstacle_default`, a favourable bench, a won plea or good
  standing cannot raise a verdict above Ob 2: only the case against the party bites. T01 CP-T01-06's derived ceiling (ruling R2) is the
  arm that shows the defence half; this file runs both arms and owns neither.
- **Any further obstacle term is clipped the same way.** T09 asks for a term reading the counterparty's ties or regard (its "M10"). That
  is a demand on this subsystem's obstacle owner, `ROLL::obstacle` (ruling R10), not an item here; at the shipped ceiling (default 2 =
  ceiling 2) a term that raises the obstacle is clipped and invisible, so T09's term needs the derived-ceiling arm to be observable.
- **Character as evidence.** `opposed` reads every deed of the party's the bench holds, not the charged one (`proofs`' named limit, H-216).
  A man of ill repute is bound more easily for anything. Deliberate (no charge carrier), and the first thing a charge reader would narrow.
- **The judge's own standing enters his verdict.** Moving `determine` to `a matter` makes `reception(judge)` and `proofs(judge, party)`
  read (arm B of CP-T05-01's control isolates it). A judge his fellow judges regard binds more easily; on a one-judge bench the term is 0.
- **CP-T05-03 lowers `news.told` volume**, so the information loop the whole engine runs on (OV §5.2 row 1) thins; reported, not hidden.
- **CP-T05-02's speaker-side reading rests on `seen.who`**, which a told copy lacks (§2 [UNVERIFIED] and [ASSUMPTION]).
- **Testimony of violence does not reach the verdict as evidence.** A told killing names nobody (PQ:145-148), so a witness moves a
  verdict on a killing only by pleading (CP-T05-02) or by being a judge. Kept on purpose; changing it moves every reader of
  `attributed_deeds`. It is the one place where the genre's "present the evidence" is narrower here than in Guild 2 or Ace Attorney.

**Does not do.** Design any screen, or build an odds function: the player's true odds are T01 CP-T01-03's (R1, AX-7), which reads
this file's room terms through `ROLL::obstacle`; `test_sc02_reception.py` and WQ:525-532 keep the room out of *decision code* only.
Adopt, call or extend the Bout kernel. Build a `lie`, a vote, a speech-kind reader, an issue ladder, a `Record` disposal (L11 M5) or a
third-party advocate. Change `pool_default`, `obstacle_default` or any capability source; the ceiling is T01 CP-T01-06's. Author an alignment cell
value. Build `interrogate`'s row or choose H-226's route. Touch the Key substrate (retired), `mc_v18`, `.designs/` or `.audit/`.
Read or assert any Godot engine version.
