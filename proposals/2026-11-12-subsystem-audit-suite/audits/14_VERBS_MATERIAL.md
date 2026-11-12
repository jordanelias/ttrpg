# VERBS · MATERIAL — build-out of sixteen `uncontested_material` rows

## Status: REFERENCE (a verb build-out audit under `VERBS_BRIEF.md`; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 84d2a02 (working tree)

Work order: `VERBS_BRIEF.md`, FAMILY = MATERIAL. Verbs (rows of `engine/season/verb_table.yaml`, stratum
`uncontested_material`): `create_record`, `destroy_record`, `exchange`, `forge`, `found`, `build`,
`requisition`, `restore`, `sabotage`, `seize`, `survey`, `tend`, `research`, `reconstruct`, `transfer`,
`work`. They are the economy, settlement, record and knowledge verbs. The SE lane's audit, addendum and
proposals and the FI lane's bind this file; they are cited by path and not redone. The seven army rows of
the same stratum (`train`, `recruit`, `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`,
`order_unit`) are the MILITARY family's.

The exact edits are in five proposals, one per batch of the landing order (§18):
`proposals/14_VERBS_MATERIAL_A_mending.md` (`restore`, `work`, `sabotage`, `tend`, and the family's draw),
`_B_stores.md` (`transfer`, `exchange`, `requisition`), `_C_works.md` (`found`, `build`), `_D_paper.md`
(`create_record`, `destroy_record`, `forge`, `survey`, `seize`), `_E_knowledge.md` (`research`,
`reconstruct`). `[UNVERIFIED]` marks what was not checked. `[SE]`, `[FI]` mark a figure taken from that
lane's run and read at the line, not re-run.

## 0. Verdict and reading

### 0.1 Verdict

**One of the sixteen works as its plain meaning promises (`survey`); none is a stub; fifteen of the sixteen
resolve as a fixed function of state, which Jordan's standing rule of 2026-11-12 forbids.** Reach fails in
the same way for nine rows: the act forms on whatever the question is about (a person, a paper, a town)
and the fold refuses it for a reason the actor could have read (`sabotage` on a thing that is no Site,
`transfer` to the giver's own rung, `found` on a petition). Consequence fails for four more: `create_record`
mints a paper with nothing on it (238 of 238 `text` Records empty, seed 0, two seasons), `reconstruct`
states no conclusion, `research` grades and deposits nothing it read, `forge` falsifies a key almost no
decision reads. `restore` and `work` are the family's dead end: in three seeds and eight realm seasons
they formed for one person, on dwellings that were not worn, and were never attempted, while 74 of 322
Sites wore every season. Only `research` draws. The repair is one pattern applied sixteen times: form on
what the person knows he can act on, resolve by the one graded draw, pay out by degree, and name a failure
differently from a refusal.

### 0.2 What this is read against

- HEAD `84d2a02`, `PYTHONHASHSEED=0` on every run.
- Three seeded two-season realm readings of one instrument, `python -m engine.season.harness.aperture 2 s`:
  seed 0 (`scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`, the PHYSICAL lane's run of this tree, read at
  the line), seed 1 (`scratchpad/runs/VERBS_BINDING/aperture_2_1.txt`, likewise) and this lane's own
  seed 2 (`scratchpad/runs/VERBS_MATERIAL/aperture_2_2.txt`). Each control line reads `content_hash EQUAL`.
- This lane's probe `mat_probe.py SEED SEASONS` (same scratch directory): the shipped chooser on
  `build_realm`, spying `opening_set`; it writes nothing. Run at seed 0 for two seasons (hash
  `bacd687f…`, the CHAR audit's own seed-0 hash; its `create_record` count, 231, equals the aperture's) and
  at seed 2 for four.
- The corpus reading is quoted from the SE audit §1.4 `[SE]`.
- Three seeds are three trajectories, not a rate (CLAUDE.md §0.1 pt 4). Nothing below is a balance claim.

### 0.3 State today, one line per verb (realm, two seasons, seeds 0 / 1 / 2)

`formed` = persons who formed it; `att / ex / ref` = acts attempted, acts that emitted a declared kind,
acts refused. `draw` = whether any roll decides it.

| verb | formed | att | ex | ref | deciding read of the refusals (seed 0) | draw | verdict |
|---|---|---|---|---|---|---|---|
| `create_record` | 83 / 83 / 83 | 231 / 252 / 263 | all | 0 | — | no | **executes; writes an empty paper** |
| `destroy_record` | 0 / 0 / 0 | 0 | 0 | 0 | — (`withheld_verbs`) | no | **withheld by a switch** |
| `exchange` | 83 / 83 / 83 | 38 / 45 / 54 | 0 | all | 16 post-admission (`to` is `from`); the rest a side that is no rung | no | **forms but is refused** |
| `forge` | 83 / 83 / 83 | 66 / 73 / 71 | 31 / 34 / 40 | 35 / 39 / 31 | 32 post-admission (the subject coheres under no faction) | no | **executes; half refused on a readable reason; its lie is read by one consumer** |
| `found` | 63 / 64 / 62 | 3 / 4 / 4 | 0 | all | `exists:works=0` ×3 (a text or a petition) | no | **forms on the wrong paper; never on its works** |
| `build` | 63 / 64 / 62 | 3 / 4 / 2 | 0 | all | `exists:works=0` ×3 | no | as `found` |
| `requisition` | 18 / 18 / 18 | 1 / 5 / 10 | 0 / 1 / 5 | 1 / 4 / 5 | `clause:authority` | no | **executes rarely, one unit at a time** |
| `restore` | 1 / 1 / 1 | 0 | 0 | 0 | — | no | **unreachable (the dead end)** |
| `sabotage` | 83 / 83 / 83 | 38 / 31 / 38 | 0 | all | `exists:Site=0` ×38 | no | **forms but is refused** |
| `seize` | 5 / 4 / 3 | 9 / 5 / 1 | 0 | all | `clause:write` ×9 (the subject is a person) | no | **forms but is refused** |
| `survey` | 83 / 83 / 83 | 26 / 18 / 24 | 12 / 13 / 14 | 14 / 5 / 10 | 12 post-admission (no single faction) | no | **works; ungraded** |
| `tend` | 83 / 83 / 83 | 61 / 39 / 62 | 37 / 39 / 42 | 24 / 0 / 20 | `with=False` ×17, already whole ×7 | no | **executes, whole, on a world-gen artefact** |
| `research` | 63 / 64 / 62 | 71 / 95 / 67 | 20 / 19 / 19 found | 51 / 76 / 48 graded losses | — | **yes** | **draws; a find teaches nothing** |
| `reconstruct` | 83 / 83 / 83 | 84 / 91 / 113 | 82 / 89 / 110 | 2 / 2 / 3 | `claim.held=False` | no | **executes; states no conclusion** |
| `transfer` | 83 / 83 / 83 | 43 / 61 / 47 | 2 / 1 / 2 | 41 / 60 / 45 | 30 post-admission (`to` is `from`, or no rung) | no | **forms but is refused; the two that execute are a cohort paying itself** |
| `work` | 1 / 1 / 1 | 0 | 0 | 0 | — | no | **unreachable (the dead end)** |

From `mat_probe.py 0 2`: of 733 `forge` / `survey` / `reconstruct` / `create_record` formations each, 253
are on a Person, 204 on a settlement, 85 on a `text` Record; cohorts made 115 of 231 `create_record`, 47 of
66 `forge`, 24 of 38 `sabotage`; every executed `transfer` names the giver's own person-rung as `to`; every
`seize` attempt by the King names the King.

### 0.4 What binds the build-out (decided once, used by every section)

| # | decision | owner and source |
|---|---|---|
| D-1 | **Every material act is drawn.** One route, the one `research` already takes: `rosters.yaml: graded_inquiries`, renamed `graded_acts`, read by `loop/resolve.py::_grade` (draw keyed `H(seed, tick, actor, "roll:<verb>:<act id>")`), rolled by the one roller. No prize, no second claimant, no new resolver | AUDIT_BRIEF standing rule; ladder step 4 (`research`, `examine`, `surveil`) |
| D-2 | **Pool** `seam/wrappers/pool.py::faculty(w, actor, verb)`; the row names its `capability:` (the CORE column, `01_CORE_capability_authoring_surface.md` Edit 3). A capability supplies dice and gates nothing | #353 §9.2 as the table quotes it |
| D-3 | **Obstacle** = `difficulty` (the row's `difficulty:` column, `05_SC_obstacle_difficulty_and_modifiers_B.md`) + the named modifiers each section lists, composed by the one owner and recorded on the roll as terms | SC-B, adopted whole |
| D-4 | **Effects by degree** on one ladder, `Fixtures effect_share` (per-mille of the full magnitude: Overwhelming 1000, Success 700, Partial 350, Failure 0), read by one function, `loop/effects_shared.py::graded_amount`. This is the `f(degree)` term `_rise` left as the identity (H-164) | r2 `04` §A.6.5 as `_rise`'s docstring quotes it |
| D-5 | **A failure is not a refusal.** `emits_on_refusal` is the world declining an act it would not admit; a lost draw emits the row's own `<verb>.failed` kind, moves nothing irrecoverable, and the actor may try again | FI-04 §1's split (`inquiry.refused` against `finding.none`), applied to the family |
| D-6 | **Formation on what the person knows.** Each row forms on a classed referent a standing occasion stamps (`queries/world_q.py::questions_for`, `_stamped`), from the actor's own edges or own ledger, never from another's state (`08_FI_01_claim-sourced-referents.md` rule R-03). New non-collection classes follow `Detainee`'s precedent and the sibling lanes' (`Holding`, `Party`, `Matter`); Record sub-kinds follow `14_VERBS_SOCIAL2_A` edit 2 (`Record.<kind>`) | ladder step 4 |
| D-7 | **Populations.** A cohort takes the acts of a people (`restore`, `work`, `tend`, `transfer`, `exchange`, `found`, `build`) and not an individual's (`create_record`, `forge`, `sabotage` by `02_CHAR_offer_what_can_be_done.md` item 5; this file adds `survey`, `research`, `reconstruct`, `destroy_record`) | CHAR's conjunct, `relation: individual` of `actor` |

Superseded by D-1, and listed for the owning lanes (§17): the SE addendum's §3.3 row *"Governing acts do not
roll … the right one to keep"* and `07_SE_capability_rate_B.md`'s `magnitude: rate` (a skill now enters as
dice, which is how every other verb reads it); `03_PC_exits_withdrawal_recovery.md` Part C's fixed
`tend_fraction`.

Each section below has the nine parts the brief orders. Part 6 names the proposal that holds the row text.

## 1. `create_record`

1. **Premise.** *To write something down so that it outlasts the moment and can be handed on.* Chain: a
   person knows or plans something → writes it → a paper exists that he holds → whoever comes to hold it
   reads what it says → it can be given, cited, copied, forged, seized, burned.
2. **State today.** `eligibility: [own]`, no `requires`, flat `emits: [record.created]`, no refusal kind
   (`verb_table.yaml:327-337`). `loop/effects_information.py::_eff_create_record` mints through
   `_mint_document` the kind the payload declares, else `text`; a computed act carries no payload, so it
   mints `text` with `subject_matter` `None`. Reading: 231 / 252 / 263 attempted, all executed; at seed 0
   the realm ends two seasons with 238 `text` Records, **none with content**, each with a maker's `hold`
   (`mat_probe_s0_2.txt`); cohorts wrote 115 of the 231. Readers of a `text` Record's content: none (its key
   list is `[]`). What it does do: each paper is a live `hold`, which `decision/budget.py` counts toward the
   scene budget (FI-04 §4, H-92), and its stages mature at MATTER (NPC-088's one represented need). It is
   also the hand-built producer of `works` and `army` Records. **Executes; writes nothing anyone reads.**
3. **Build-out.** A computed `create_record` writes **an account**: what the writer holds about the thing
   the act is about. Formation: an individual, on a referent his own ledger holds a claim about, the claim
   copied onto the act at CHOOSE as `tell` copies its `said` (nothing to write is declined, `tell`'s T4
   rule). New record kind `account: [terms, said]`. Draw: pool `copying` (the capability Carin Vedel
   already holds), difficulty `plain`. Overwhelming and Success: a faithful account. Partial: a lossy one
   (the value drifted by the one drift rule, `person_q.drifted`, as a `Partial` telling's). Failure:
   `record.spoiled`, nothing minted. Declared kinds (`works`, `army`, `text`) pass through the same draw
   and differ only at Failure. Reader: whoever comes to hold an account holds its content as a told claim
   with the writer on its chain (`loop/witness.py`, the content deposit), so a letter carries news, a
   ledger carries a stock figure, a report carries a deed, and each can be cited as a `record` proof
   (`08_FI_05_evidence-interface_B.md` E-1). Costs: a scene. Forecloses nothing. Refusal: none (an untyped
   declared kind the roster lacks still raises at the mint). Reason trail: the Record's maker and the
   `said`'s chain.
4. **Scales and surface.** Person scale; it reaches settlement, faction and realm only by being carried
   (`give`), filed (`petition`, `carry`) or held by a seat. The player chooses what to write about (the
   referent) and, through `choice_sourced`, which held claim (FI-10's fix for `said`, `08_FI_02` §4); the
   engine resolves fidelity. An NPC forms it on any referent he knows something about and ranks it with
   his other candidates.
5. **Tuning hooks.** `copying` and its base attribute (`references/descriptor_registry.yaml: capabilities`);
   `Fixtures effect_share`; `rosters.yaml: record_kinds.account`; `Fixtures record_stage_term` (how long the
   writing takes, NPC-088).
6. **Exact edits.** `14_VERBS_MATERIAL_D_paper.md` §2.
7. **Gate and falsifier.** Seeded realm, two seasons: `account` Records with content > 0; after one `give`,
   the receiver's ledger holds the account's cell with the writer on the chain, and his candidate set on
   that subject differs from the control (the same seed with the content deposit off). Planted failure:
   mint the account without `said`; the receiver's ledger must show nothing new and the gate must go red.
8. **Cases.** NPC-088 (N2, N3, N7: the copied text is an object whose possession matters; today only N1
   and N9 are met); NPC-086 (N1: field data as a Record); NPC-090 (N1: a trade relationship on paper);
   NPC-085 (N2: precedent cited); ARC-15, NSC-01, NSC-04 (M-INFO: a report that differs from what is
   held).
9. **NERS.** N: without it no information leaves a person except by speech in the same room; from the
   top (M-REC, M-INFO), from the bottom (one kind, one deposit branch), laterally (it is `tell` on paper).
   R: letters, false letters, intercepted letters, with no player involved. S: `tell`'s copy rule, drift
   rule and chain. E, last: one kind and one copied operand against 238 blank papers. **Cut test:** remove
   it and `works`, `army` and every written proof lose their producer; merge it into `tell` and a telling
   can no longer be held, carried or burned.

## 2. `destroy_record`

1. **Premise.** *To destroy a document so that nobody can read it again.* Chain: a person holds a paper he
   wants gone → he destroys it → it no longer exists → those who knew of it may notice → the act itself can
   be found out.
2. **State today.** Typed (`existence` Record ∧ `held_by`), `own`-eligible, effect
   `_eff_destroy_record` deletes the Record and closes its holds. Formation is switched off:
   `Fixtures withheld_verbs` names it (H-156 option (a), `verb_table.yaml:338-359`). Formed 0 / 0 / 0.
   **Withheld; the effect is sound and deterministic.**
3. **Build-out.** Release it with a reason to form. Formation: an individual, on a Record of his own live
   `hold` whose content names him (class `Damning`: his own held papers, read through his own content
   claims, so R-03's own-edge clause). Draw: pool `copying` is wrong for burning; `capability: none`,
   difficulty `plain`, modifier `watch`: persons standing with him (`presence` at his rung, less one)
   times `Fixtures watch_step`. Overwhelming and Success: destroyed, the Event a covert kind
   (`record.destroyed` joins `rosters.yaml: covert_kinds`; a later `examine` of the place or `research` of
   a sibling paper can uncover the hand). Partial: destroyed and seen (`destroy.seen`, an ordinary
   witnessed kind naming him). Failure: `destroy.failed`, the paper survives and he was seen trying.
   Writes `Record.exists` at the three winning bands. Unlocks: a contest that cannot cite the paper;
   forecloses his own later use of it. Refusal `destroy.refused` stays for a hand-built act on a paper he
   does not hold.
4. **Scales and surface.** Person scale. The player picks the paper; the engine resolves whether it was
   clean. An NPC forms it only on papers that name him.
5. **Tuning hooks.** `Fixtures watch_step`; `rosters.yaml: covert_kinds`; `Fixtures withheld_verbs` (the
   control arm: restore the member).
6. **Exact edits.** `14_VERBS_MATERIAL_D_paper.md` §5.
7. **Gate and falsifier.** A two-person fixture: a holder of an account naming him destroys it at a
   planted `Success`; a hearing on that matter then finds no `record` item to cite (after FI-05-B), and an
   examiner's found deposit names him. Control: paper not destroyed, the item is cited. Planted failure:
   leave `record.destroyed` out of `covert_kinds`; the examiner must find nothing.
8. **Cases.** ARC-15 N4, N6 and NPC-086 N7 (e6: suppressing evidence changes a case); NPC-088 N3
   (possession as exposure).
9. **NERS.** N: the only sink for paper, and the only way to make evidence absent; R: the cover-up that
   is itself a trail; S: `sabotage`'s covert shape, one kind over. E, last: one stamp and one banded row.
   **Cut test:** remove it and every Record is permanent; merge it into `sabotage` and a Site verb would
   need a Record operand.

## 3. `exchange`

1. **Premise.** *To trade: give something of mine for something of yours.* Chain: two places hold unlike
   goods → a person at one offers → terms are struck → both stores move → each place has what it lacked.
2. **State today.** `own`; two `scalar_threshold` conjuncts (each side's stores cover its side); effect
   `_eff_exchange`, two `_shift`s. `to` binds the question's referent, `kind` the fixture
   (`default_store_kind`), `return_kind` and both amounts fixtures. Reading: 38 / 45 / 54 attempted, 0
   executed; at seed 0, 17 name the giver's own rung on both sides, 8 a Person, 11 a Record. CR-49 holds
   the formation half (`referent_class: Rung`, a `to != from` decline) and is unbuilt. **Forms but is
   refused; no price; no draw.**
3. **Build-out.** CR-49 as written, plus three things it does not carry. (a) What is offered and what is
   asked come from the trader's own ledger: `kind` is the matter his newest `stores:` claims show his own
   rung holding most of, `return_kind` the matter those claims show the other rung holding that his own
   holds least of; the fixtures stay as the fallback. (b) The destination is a place he knows holds stock
   (class `Market`: a Rung his ledger holds a positive `stores:` claim about, not his `from`). (c) **The
   degree is the price.** Draw: pool `trade` `[ASSUMPTION; Jordan's content; revert: none]`, difficulty
   `routine`, plus `opposition` when his ledger names a holder of the other rung (that person's score
   halved, the ruled divisor) and SC-B's `regard` term for that holder. Overwhelming: he gives `amount`
   and receives `return_amount` × 1500‰ (bounded by what the other side holds); Success: par; Partial:
   he receives × 500‰ (at least one unit); Failure: `exchange.failed`, no deal, nothing moves. Matter is
   conserved at every band. Amounts ride SE's `amount_shares` choice (`07_SE_arc_needs.md` §3 b).
   Unlocks dependency between unlike places (`07_SE_ground_and_granaries.md`).
4. **Scales and surface.** Person acting for a place (his own rung, or a seat's treasury through `via`,
   as `transfer`); settlement to settlement, duchy to duchy (ARC-20's gate as the SE addendum re-states
   it, R-SE-30). The player chooses partner, goods and share; the engine draws the terms.
5. **Tuning hooks.** `Fixtures exchange_terms` (the three per-mille figures); the `trade` capability;
   CP-T08-05's price, which replaces the par figure when it lands; a `covenant` whose terms name the two
   rungs (NPC-090; FA's) as a favourable modifier.
6. **Exact edits.** `14_VERBS_MATERIAL_B_stores.md` §3.
7. **Gate and falsifier.** Under SE's `ground` arm, seeds 0 to 2, three seasons: `exchange.made` > 0
   between two settlements whose endowments differ, and the importing settlement's hunger band differs
   from the control arm (exchange withheld). Planted failure: bind `return_kind` to `kind`; every act must
   decline at formation, not in the fold.
8. **Cases.** NPC-090 (N1); ARC-20; ARC-12 N1 and ARC-37 N1 (a supply chain that exists to be traced);
   NPC-007 N2.
9. **NERS.** N: trade is the channel BALANCE-005 names for the food dependency (SE addendum F-SE-22).
   R: a bad bargain and a good one from the same stock; routes that form with nobody watching. S: two
   `_shift`s, the family's draw. E, last: one class, two ledger reads, one terms table. **Cut test:**
   merge it into two `transfer`s and the two sides stop being one act, so a trade can half-happen.

## 4. `forge`

1. **Premise.** *To make a false document that passes for a true one.* Chain: a person has seen what a
   true one looks like → he makes one that says something false → someone holds it and acts on it → an
   examination may tell it from a true one → the forger is exposed or not.
2. **State today.** `own`; cell `own_ledger` of `subject` (he has heard of it); effect `_eff_forge` mints a
   `faction_sheet` on the subject's faction with the **forger written in as `head`**, at
   `Fixtures default_forgery_quality`. Reading: 66 / 73 / 71 attempted, 31 / 34 / 40 executed; of the
   refusals 32 / 36 / 28 are post-admission (the subject coheres under no single faction, which only the
   effect asks). Cohorts forged 47 of 66 at seed 0. What it says is fixed for every forger (F-FI-10);
   its one reader is the sheet consumer (a petition addressed to the false head); found deposits 0 at
   three seeds `[FI]`. **Executes; no draw; one lie for everybody.**
3. **Build-out.** A forgery is a false copy of a paper he holds. Formation: an individual, on a Record
   of his own live `hold` whose kind `rosters.yaml: forgeable_kinds` lists (`dispensation`, `petition`,
   `faction_sheet`, `account`), fanned over the persons he knows (`to`, the existing known-person fan):
   the forgery names that person where the true paper names another. Which key is falsified is data
   (`forged_key`, per kind: a sheet's `head`, a writ's or petition's `terms`, an account's `terms`), read
   as `_FORGED_SHEET_KEY` is read today. Draw: pool `copying`, difficulty `demanding`. The degree is the
   quality: Overwhelming `default_forgery_quality` + 1, Success the default, Partial one below (at least
   1), each written to `Record.forgery_quality`, which the examiner's obstacle already reads as its
   `subject` term; Failure: `forge.failed`, nothing minted. Consequences already wired: a forged writ is
   a warrant for `arrest` and `seize` and an order for `comply`; a forged petition can be carried; a
   forged account is a false proof; each can be impeached by a found `record.forged` (FI-05-B E-5.2).
   The faction-from-hearsay path (`survey`'s cell) leaves this row.
4. **Scales and surface.** Person scale, with faction and realm reach through what a writ commands. The
   player chooses the exemplar and whom the false paper names; the engine draws the quality. An NPC forms
   it only while he holds an exemplar.
5. **Tuning hooks.** `rosters.yaml: forgeable_kinds`, `forged_key`; `Fixtures default_forgery_quality`;
   `copying`; the examiner's `subject` term (SC-B).
6. **Exact edits.** `14_VERBS_MATERIAL_D_paper.md` §3.
7. **Gate and falsifier.** `08_FI_03`'s `inquiry_world`: a forged writ handed to its addressee produces a
   `comply` (or, held by a seat, an `arrest`) that the control (no forgery) lacks; an examiner's `research`
   at a planted `Success` deposits `(record, record.forged, True)`; with the quality raised by one the
   same roll fails. Planted failure: write quality 0 at every band; the examination must find at `Partial`.
8. **Cases.** NPC-004 (e6), NPC-086 N7, ARC-15 (e6), NSC-04.
9. **NERS.** N: the false paper is the detective precedent's central object and M-REC's rank-9 need.
   R: whom to frame is a choice; a crude forgery and a fine one differ in play. S: one mint, one quality
   field, one reader. E, last: a roster and a fan replace a hard-coded lie. **Cut test:** merge into
   `create_record` and a false paper would carry no quality for an examiner to beat.

## 5. `found`

1. **Premise.** *To found a new place where there was none.* Chain: someone plans it and gathers a stake
   → he founds it → a new rung exists under its parent, holding the stake, held by its founder → people
   can live there → the parent's capacity can grow.
2. **State today.** `own`; `referent_class: Record`; cell `existence` works ∧ `held_by`; effect
   `loop/effects_founding.py::_eff_found` mints the Rung, moves the `works_cost` stake two-sided and opens
   the founder's `hold`. Reading: 3 / 4 / 4 attempted, 0 executed, every refusal `exists:works=0`. At seed
   2 over four seasons the row formed 819 times, 36 of them on a works, and none of those was attempted
   (`mat_probe_s2_4.txt`); the two authored works' masters are `p_npc_020` and `p_npc_009`, and the paying
   rungs hold the price from season 1 (40 grain, 10 timber against 10). **Forms on the wrong paper; its
   own works is offered and never chosen; no draw.**
3. **Build-out.** Formation: `referent_class: Record.works` (SOCIAL2-A edit 2), narrowed by a stamp that
   offers only a works he holds that plans a Rung kind and has not yet founded (his own held paper: the
   own-edge clause). An unmade works is also a standing question for its master (the docket question's
   shape), so it is asked about rather than waiting on a referent coincidence. Draw: pool `labour`
   `[ASSUMPTION; revert: none]`, difficulty `demanding`. Overwhelming: founded, the whole stake arrives;
   Success: founded, 350‰ of the stake consumed in the settling; Partial: founded, 700‰ consumed;
   Failure: `found.failed`, no place, 350‰ of the stake lost, the works stands and may be tried again.
   Refusal `found.refused` stays for the scarcity case (the rung cannot pay), keyed `stores`.
4. **Scales and surface.** Person (the founder), settlement (the parent), faction (who holds it). The
   player chooses which works to found and when; the engine draws what the founding cost.
5. **Tuning hooks.** `rosters.yaml: works_cost`; `venues.yaml: planned_works` (Jordan's content; more
   rows are the producer, ED-IN-0297 option (B)); `Fixtures effect_share`.
6. **Exact edits.** `14_VERBS_MATERIAL_C_works.md` §2.
7. **Gate and falsifier.** Seeds 0 to 2, four seasons: `rung.founded` ≥ 1 at some seed and `found`'s
   wrong-kind refusals read 0 at all three; the founded hearth appears in `capacity`'s subtree. Control:
   `planned_works` emptied, hash equal to the no-works realm. Planted failure: stamp the works after it
   has founded; a second `found` must be refused and the gate must count it.
8. **Cases.** F-SE-12 (the world never grows); EMG-11 N2 (a finite per-place capacity); NPC-003.
9. **NERS.** N: the ruled throttle on population (ED-SE-0051) has no other lever. R: a founding that
   costs more than planned. S: `build`'s shape. E, last: a class qualifier, a stamp, a banded row.
   **Cut test:** merged with `build`, one verb makes two carriers under two gate bases (the table's own
   objection).

## 6. `build`

1. **Premise.** *To raise a structure.* Chain: a plan and materials at a place → the builder starts → a
   fabric stands at its first course → labour raises it over seasons → it houses, yields or defends.
2. **State today.** As `found`, minting a Site at condition 0 and consuming the price one-sided
   (`_eff_build`). Reading: 3 / 4 / 2 attempted, 0 executed, `exists:works=0`. **As `found`.**
3. **Build-out.** Formation as `found`, for a works that plans a Site kind. Draw: pool `craft`
   `[ASSUMPTION; revert: none]`, difficulty `demanding`. Overwhelming: the Site stands and 300‰ of the
   price is spared; Success: stands at the price; Partial: stands, with an overrun of 350‰ of the price
   where the rung can pay it, else as Failure; Failure: `build.failed`, no Site, half the price consumed.
   The Site always begins at condition 0 (r2's decision, kept); `work` raises it (§16). Those standing at
   the rung witness `site.built`, which is `work`'s occasion.
4. **Scales and surface.** Person and settlement. The player chooses what to build among the works he
   holds; the engine draws the cost.
5. **Tuning hooks.** `works_cost`; `site_kinds`; `planned_works`; the `craft` capability.
6. **Exact edits.** `14_VERBS_MATERIAL_C_works.md` §3.
7. **Gate and falsifier.** As `found`: `site.built` ≥ 1, then a `site.worked` on that Site by a person
   who stood there, then `capacity` of the rung higher than the control's. Planted failure: mint the Site
   at full condition; `work` must then be refused and the gate must say so.
8. **Cases.** NPC-083 (the governor's menu); SE addendum F-SE-19 (a barracks is built, so a realm can
   train); EMG-C3 N2's rising arm.
9. **NERS.** As `found`. **Cut test:** without it capacity, fortification and training Sites have no
   producer in play.

## 7. `requisition`

1. **Premise.** *An office takes goods from a place it governs, for the office's use.* Chain: a seat with
   reach over a place knows it holds stock → its holder demands a share → the place yields it, in whole or
   in part, or resists → the treasury fills → the people who were taken from remember who took.
2. **State today.** `remit:issue | presence:<rung>`; `referent_class: Rung` (stamp `larders_in_purview`);
   cell `basis: purview` ∧ `stores >= amount`, refusals keyed per clause; effect
   `loop/effects_governance.py::_eff_requisition`, one `_shift` into the seat's rung. Reading: 1 / 5 / 10
   attempted, 0 / 1 / 5 executed, each of one unit of grain; the refusals are `clause:authority` (the
   stamp offers larders to a seat granting any `Rung` row's act, and this row asks `issue`: at seed 2,
   `off_npc_084` three times). `requisition.taken` is an `UNREST_KINDS` deed `[SE]`. **Executes, rarely,
   at a size that changes nothing; no draw.**
3. **Build-out.** Formation: the stamp narrows to the seats that grant this row's own act (class
   `Larder`, not the shared `Rung`), so no candidate is formed that `authority` must refuse. Amount is
   SE's choice (`amount_shares`), the treasury SE's (`07_SE_treasury_granary_B.md`). Draw: `capability:
   none` (the office is the instrument; `faculty` adds the seat's weight where DICE gives it one),
   difficulty `routine`, plus `stakes` (the share asked, in thirds of the known stock, one step each) and
   SC-B's `regard` term read from the cohort that resides at the requisitioned rung toward the actor.
   Overwhelming: the full amount; Success: 700‰; Partial: 350‰ (at least one unit); Failure:
   `requisition.resisted`, nothing moves, witnessed at the place. The deed claim is deposited at every
   band (they tried to take it). Unlocks: relief, pay and a field's ration from one stock (SE addendum
   §4); forecloses the same grain for the place. Refusals keep their keys; `authority` becomes reachable
   only by a hand-built act.
4. **Scales and surface.** Seat (faction, duchy, realm) acting on a settlement or territory. The player
   chooses the place and the share; the engine draws what comes in. An NPC forms it through the stamp
   and ranks it; a standing levy is CP-T08-07's.
5. **Tuning hooks.** `amount_shares`; `Fixtures stakes_ob` (SC-B's table, a `requisition` row);
   `regard_step`; `effect_share`; the residing cohort's stance rows (CR-107's content).
6. **Exact edits.** `14_VERBS_MATERIAL_B_stores.md` §4.
7. **Gate and falsifier.** `harness/scarce.governed` with a second `amount_shares` member, seeds 0 to 19:
   the amount taken varies across seeds for one candidate (a spread, not one value), and the cohort's
   stance toward the steward after a `Failure` differs from after an `Overwhelming`. Realm: no
   `requisition.unauthorized` from a computed act in `aperture 2 s`. Planted failure: pin the degree; the
   spread must vanish and the gate must go red.
8. **Cases.** NPC-013 (N1), NPC-037 (N2), NPC-083 (N1, N4), ARC-46 N3.
9. **NERS.** N: the only way stock reaches a holder. R: a levy that comes in short; a place that refuses
   its lord, with a trail. S: `transfer`'s body, the family's draw. E, last: a narrowed stamp and a
   banded row. **Cut test:** merge into `seize` and a taking of goods and a taking of title share one
   licence, which the table split on purpose.

## 8. `restore` (the dead end, with `work`)

1. **Premise.** *To bring a worn or damaged thing back to good condition.* Chain: a fabric is worn or
   broken → someone who stands at it knows → he works on it → its condition rises, more or less → what it
   yields, houses or defends recovers.
2. **State today.** `own | presence:<site>`; `referent_class: Site`; cell `existence` Site ∧ `present_at`;
   effect `loop/effects_economy.py::_eff_restore` stages `_rise` (headroom to the ceiling times the
   commons' share, `f(degree)` the identity, H-164). Reading: formed for 1 person, attempted 0, at all
   three seeds. The cause, read at this HEAD (`mat_probe.py`): the row forms only when the first question
   a person answers is itself about a Site; the one person so asked formed it 10 times in two seasons
   (20 in four at seed 2), **every time on a dwelling**, a kind whose wear is 0 and whose
   `condition.worn` Event is F-SE-08's false report. Meanwhile 74 of 322 Sites (every harbour and seam)
   were below scale after every season, 154 to 644 `condition.worn` claims sat in ledgers, and no ledger
   held a `condition` reading. So the people who stand at a worn harbour hold the news and are never
   asked. `[UNVERIFIED: what changed since `24f`, when H-171 recorded 9 executions; SE audit F-SE-05
   names two candidates and this reading is consistent with the first, the `first` aggregation rule.]`
   **Unreachable; and one hand restores a ruin whole in one act with no draw.**
3. **Build-out.** Formation: class `Worn`, stamped by a standing occasion over the person's own ledger
   and own position: a Site standing where he stands whose newest fabric news in his ledger is a
   lowering kind (`rosters.yaml: fabric_news.lowers`: `condition.worn`, `condition.band_crossed`,
   `site.damaged`) and not a raising one (`raises`: `site.restored`, `site.worked`). A cohort stands at
   its settlement's rung, so the townsfolk are the ones offered their own harbour. Draw: pool `craft`,
   difficulty `routine`, plus `ruin`: one step per band floor the fabric stands below
   (`rosters.yaml: band_floors`; none for a kind with no floors), so repair is harder the worse it is
   (EMG-C3 N2). The rise is `_rise` times `graded_amount`: Overwhelming the whole headroom share,
   Success 700‰, Partial 350‰, Failure `restore.failed` and nothing moves. It still stages on the
   accumulator and clamps once. Refusal `restore.refused` remains for the stale belief (another hand
   mended it first), which now teaches him the condition he read (CP-T06-04). Readers downstream:
   `settlements.produce` (yield scales with condition), `fortification_of` (garrison condition),
   `capacity` once dwellings wear (H-307).
4. **Scales and surface.** Person and population at a settlement; its consequence is the settlement's
   yield and walls, and a faction's field. A steward cannot restore from afar: he must stand there or
   move someone to act (`issue`), which is the intended friction. The player chooses which worn thing to
   mend; the engine draws how far.
5. **Tuning hooks.** `fabric_news` (which kinds a person notices; the list without `condition.worn` is
   the control arm in which only a crossing or damage is an occasion); `band_floors`; `craft`;
   `effect_share`; the commons' `share` (H-164's unbuilt sweep, untouched).
6. **Exact edits.** `14_VERBS_MATERIAL_A_mending.md` §3. Needs `07_SE_kernel_repairs.md` §3 first (a wear
   of zero must stop emitting, or every dwelling is stamped `Worn`).
7. **Gate and falsifier.** `aperture 2 s`, seeds 0 to 2: `site.restored` > 0 at every seed, with at least
   two distinct degrees among the executed acts; mean harbour condition after two seasons above the
   no-acts arm's (SE's `se_probe.py … noacts`), and the season's `yield.taken` total above it. Control:
   `fabric_news.lowers: []` reproduces today's zero. Planted failure: stamp `Worn` from `w.sites`
   condition instead of the ledger; FI-01's silent-change test (a Site lowered with no Event) must move
   a candidate and go red.
8. **Cases.** EMG-C3 (N2: repair harder the worse it is, by a draw); NPC-075 (N1: an exhausting
   maintenance a person chooses to continue); NPC-083's menu; ARC-48; SE F-SE-18 (the falsifier it names:
   one quantity whose two arms both execute).
9. **NERS.** N: without the raising arm every binding arm is a ratchet (F-SE-18); holds top-down (R-05),
   bottom-up (the effect exists), laterally (`tend` is the same formula on a body). R: neglect becomes
   visible where a people is dead, fled or busy; a botched repair. S: one formula, one ladder. E, last:
   one stamp, one roster, one term. **Cut test:** remove it and wear, sabotage and siege are permanent.

## 9. `sabotage`

1. **Premise.** *To damage something on purpose, to hurt whoever depends on it, preferably unseen.*
   Chain: a person with a grievance stands at his enemy's works → he damages it → its condition falls →
   yield, walls or housing suffer → someone notices the damage and may or may not learn whose hand.
2. **State today.** `own | presence:<site>`; no `referent_class`; `restore`'s cell; effect
   `_eff_sabotage` stages `_fall` (the whole footroom share). Reading: 38 / 31 / 38 attempted, 0 executed,
   every refusal `exists:Site=0` (it forms on persons, towns and papers); cohorts made 24 of 38 at seed
   0. **Forms but is refused; if it ran, one saboteur would zero a fabric with certainty.**
3. **Build-out.** Formation: an individual, class `Resented`: a Site standing where he stands whose
   rung his own ledger names a holder of (`holders_named`, FI-01's reader) against whom he holds a
   stance row (`person_q.held_against`) or who is an `Enemy` (CR-87's war context). Draw: pool `craft`
   `[ASSUMPTION]`, difficulty `demanding`, plus `watch`: the sworn weight present at the rung
   (`world_q.guard_weight`) times `Fixtures watch_step`. Overwhelming: the full fall, unseen; Success:
   700‰, unseen; Partial: 350‰ and seen; Failure: nothing falls and he is seen. Unseen means the Event
   is `site.damaged`, which joins `covert_kinds`, so those present learn the fabric fell and an `examine`
   of the Site can uncover the hand; seen means `sabotage.seen`, an ordinary witnessed kind naming him.
   It lowers and never ends (ending is `raze`'s). Unlocks `restore`'s occasion for those present; exposes
   him to `arrest`, `challenge`, a stance row.
4. **Scales and surface.** Person scale act, settlement and faction consequence (a garrison weakened
   before a `march`: the MB seam reads `fortification_of`). The player chooses the target among what he
   resents where he stands; the engine draws the damage and whether he was seen.
5. **Tuning hooks.** `Fixtures watch_step`; `covert_kinds`; the stance rows that make a thing resented
   (CHAR's content); `effect_share`.
6. **Exact edits.** `14_VERBS_MATERIAL_A_mending.md` §5.
7. **Gate and falsifier.** A fixture of one town, one garrison, a holder and a man with a row against
   him, seeds 0 to 19: the garrison's condition after one act takes at least three distinct values across
   seeds; at the unseen bands no co-located ledger names the hand and an `examine` at a planted `Success`
   does; a later `march` on the town meets lower fortification than the control. Realm: `sabotage`'s
   `exists:Site=0` refusals read 0. Planted failure: emit `site.damaged` at every band; the seen arm must
   then name nobody and the gate must go red.
8. **Cases.** ARC-12 (N2, a hazard inside an arrangement, with the FI and WR lanes); ARC-37; NPC-075 N5
   (the cumulative damage others do); ARC-07.
9. **NERS.** N: the lowering arm that has an author. R: a man caught at it; a quiet ruin that someone
   must investigate. S: `_rise`'s mirror, `destroy_record`'s covert shape. E, last: one stamp, one banded
   row. **Cut test:** merged into `raze` (an occupier's ending of a place) it would need an army.

## 10. `seize`

1. **Premise.** *To take possession of something by authority, against its holder's will.* Chain: an
   office holds a warrant, or its force holds the ground → its holder takes the thing → the old holder's
   title ends and his begins, or the taking is resisted → the dispossessed and the bystanders know.
2. **State today.** `remit:issue`; cell `basis: purview` (keyed `authority`); formation
   `rosters.yaml: warrant_sourced` (a subject a held dispensation's `terms` names); effect `_eff_seize`
   (a Record, licensed by a held warrant naming **the Record**) or `_seize_rung` (a settlement, licensed
   by occupation). Reading: 9 / 5 / 1 attempted, 0 executed, all `clause:write`. At seed 0 every act
   names a **person** (17 of 19 formations; the King names himself six times): writs' terms name people,
   so the stamp offers people, and a person is neither a Record nor a settlement. **Forms but is refused,
   by construction.**
3. **Build-out.** A warrant naming a person licenses the taking of **his papers**. Formation: class
   `Record` (bare: any paper), stamped by an occasion over the actor's own held warrants and own ledger:
   the Records his ledger names the warranted person as holding (`holders_named`). The effect's licence
   widens from *the warrant names the Record* to *the warrant names the Record or its present holder*.
   The Rung half forms on class `Occupied`: a settlement or territory his own seat's faction occupies
   (his own force, the own-edge clause), H-232's missing stamp. Draw: `capability: none`, difficulty
   `routine`, plus `opposition` (the holder's score halved) and `watch` for a Rung. Record half:
   Overwhelming: taken, and the taker learns what else that person holds (an Observation per paper);
   Success: taken; Partial: not taken, the holder warned (`seize.resisted`, witnessed), the taker learns
   where it is; Failure: not taken, resisted, nothing learned. Rung half: Overwhelming and Success: the
   title passes; Partial: resisted, and the place's garrison Sites fall by 350‰ of `_fall`; Failure:
   resisted. Refusals stay keyed (`seize.unauthorized`, `seize.refused`).
4. **Scales and surface.** Seat scale; person (papers), settlement and territory (title). Composes with
   `arrest` (the person) and `march` (the ground). The player chooses what to take under which warrant;
   the engine draws whether he gets it.
5. **Tuning hooks.** `warrant_sourced`; `stakes_ob`; `watch_step`; `march_target_kinds`.
6. **Exact edits.** `14_VERBS_MATERIAL_D_paper.md` §6. The Rung half's stamp is shared with the PHYSICAL
   and MILITARY families (`march`, `raze`); CP-T09-04 carries `occupying_faction` and is not redone.
7. **Gate and falsifier.** `inquiry_world`: an investigator's seat issues a writ naming the forger and
   seizes the forged sheet at a planted `Success`; the sheet's `hold` is the seizer's and the next hearing
   can cite it. At a planted `Partial` the forger, warned, forms `destroy_record` or `give` on it the
   next round (the control, no seizure attempt, forms neither). Realm: `seize` formations name no person.
   Planted failure: keep `warrant_sourced` reading `terms` as the subject; the realm line must still show
   persons.
8. **Cases.** NPC-086, NPC-004, ARC-15 (evidence taken into custody); ARC-46 (the quiet seizure, with
   FA's seats); NPC-003 (held settlements).
9. **NERS.** N: without it evidence stays with whoever holds it and a won town changes nobody's title.
   R: a warned man; a raid that learns more than it sought. S: `give`'s body, `arrest`'s warrant. E, last:
   one widened licence and two stamps. **Cut test:** merged into `requisition`, title and goods share a
   licence; merged into `arrest`, papers and persons do.

## 11. `survey`

1. **Premise.** *To take stock of a power: who belongs to it, what it holds, who leads it.* Chain: a
   person has heard of a faction → he commissions or makes a survey → a dated paper states what was so →
   its holder plans on it → it goes stale.
2. **State today.** `own`; cell `own_ledger` of `subject`; effect `_eff_survey` mints a `faction_sheet`
   frozen from `faction_q.resolve`, complete and exact. Reading: 26 / 18 / 24 attempted, 12 / 13 / 14
   executed; refusals post-admission where the subject coheres under no faction (a paper, an
   uncommitted person). Its content is read: the sheet consumer, and the content deposit to its holder.
   **Works; exact with certainty; a third of attempts refused on a readable reason.**
3. **Build-out.** Formation: an individual, on a referent his own ledger gives a faction for (a person
   it names as committed, a rung it names a holder of, a faction's own Proposition he has heard): one
   person-side reader, `person_q.faction_named`, replaces the effect's decline as the formation test; the
   effect keeps the decline for a stale belief. Draw: pool `inquiry` (the existing key), difficulty
   `routine`, plus `opposition` when the faction's head is a person his ledger names. Overwhelming and
   Success: the full five-field sheet; Partial: `proposition` and `head` only, the three lists empty
   (H-169's proposal 14.1 bound, reached by degree); Failure: `survey.failed`, no paper. A Partial sheet
   is a true but thin document; nothing false is written (falsity is `forge`'s).
4. **Scales and surface.** Person acting on a faction, at any rung the faction holds. The player chooses
   whom to survey; the engine draws how much he learns.
5. **Tuning hooks.** The `inquiry` capability; `record_kinds.faction_sheet`; SC-B's opposition term.
6. **Exact edits.** `14_VERBS_MATERIAL_D_paper.md` §4.
7. **Gate and falsifier.** Realm, seeds 0 to 2: post-admission `survey.refused` reads 0 or the stale
   case only; both full and thin sheets occur; a holder of a thin sheet forms no petition addressed
   through `members` and a holder of a full one can. Planted failure: mint the full sheet at `Partial`.
8. **Cases.** NPC-086 (a surveyor's field data), ARC-54 N2, the "intelligence before action" chain (#7
   of the ten).
9. **NERS.** N: the only act that turns a faction (a view, `queries/faction_q.py`) into something a
   person can hold. R: thin intelligence acted on. S: the family's draw; `_mint_document`. E, last: one
   reader and a banded row. **Cut test:** merged into `research` it would need a paper to exist before
   anyone could learn of a faction.

## 12. `tend`

1. **Premise.** *To care for the hurt or sick so that they mend.* Chain: someone is hurt → a person with
   him knows it → he tends him → the body recovers, somewhat → the patient can act and fight again.
2. **State today.** `own`; `referent_class: Person` (stamp `wounded_with`, plus a question's own plain
   Person); cell `existence` Person ∧ `with`; effect `loop/effects_combat.py::_eff_tend` raises the body
   to its ceiling **whole**. Reading: 61 / 39 / 62 attempted, 37 / 39 / 42 executed. At seed 0 all 37
   executed acts are cohorts tending themselves after the season-0 hunger artefact (F-SE-03), and all 24
   refusals are named persons: 19 tending someone who is not with them, 5 tending themselves whole. H-304:
   resting erases a famine's mark in the season it falls. **Executes; certain and whole; a third refused
   on a readable reason.**
3. **Build-out.** Formation: class `Wounded` (non-collection), which `wounded_with` already computes
   from his own body and his own beliefs; the row stops forming on a question's plain Person, which is
   where both refusal families come from. Draw: pool `physic` `[ASSUMPTION; revert: none]`, difficulty
   `routine`, plus `wound`: one step per body band the patient is below whole (`band_floors.body`).
   Overwhelming: the whole headroom to his ceiling; Success: 700‰; Partial: 350‰; Failure:
   `tend.failed`, nothing moves. The effect writes a body Observation (`body_observed`, the helper
   `_eff_kill` uses), so a believer's stamp clears when the man is whole. This replaces
   `03_PC_exits_withdrawal_recovery.md` Part C's fixed fraction with the ladder. H-304 narrows (a starved
   body is no longer reset whole for certain) and does not close: hunger and wounds share one scalar, and
   splitting them is not this row's.
4. **Scales and surface.** Person to person, or a population to itself. The player chooses whom to tend
   among those he believes hurt; the engine draws the mending.
5. **Tuning hooks.** `physic`; `band_floors.body`; `effect_share`; `Person.body_ceiling` (the PC lane's
   lasting mark).
6. **Exact edits.** `14_VERBS_MATERIAL_A_mending.md` §6.
7. **Gate and falsifier.** `test_cp_t03_08`'s fixture, seeds 0 to 19: the patient's body after one act
   takes at least three values; after a whole mending no believer forms `tend` on him. Realm:
   `tend.refused` on `with=False` reads 0. Planted failure: drop the Observation; the healed man must
   still be stamped the next season.
8. **Cases.** ARC-53 N6 (a discrete recovery action); SCN-03 (two recoveries of different speed, by
   degree); NPC-034.
9. **NERS.** N: the body's only raising arm. R: a wound that lingers because the tending went badly. S:
   `restore`'s formula and ladder. E, last: a class and a banded row. **Cut test:** merged into
   `restore`, a Site verb would bind a Person.

<!-- more -->
