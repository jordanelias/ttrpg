# U5c · SC — proceedings residue: the SC findings no proposal carried, as one ordered plan

## Status: PROPOSED (written by the U5c closure lane; a plan for a later implementation lane, executed by nobody here; not ratified by being written, `CLAUDE.md` §2)

Carries the SC-family rows of `unified/U5_FINDINGS_CLOSURE_U5c.md` whose carrier column reads **RES**, and
conflicts C-07 to C-11 of `unified/U5_CONFLICTS_U5c.md`. Each section is independent unless it says
otherwise. Sources: `audits/05_SC_audit.md` (G-05, G-15 to G-18, G-20, G-22, G-25, §6.1, §6.2),
`audits/05_SC_audit_addendum_B.md` (C-7, G-55), `audits/13_SC_contest_interrogation.md` (R-8, cells 8 to 10),
`audits/16_PESSIMIST_SC.md` (F-PES-SC-07, -08, -12; res. 4, 6; its list of what does not draw),
`audits/18_DETERMINISM_SWEEP.md` §3.

## What it changes in `engine/season/` at runtime

§1 to §3: nothing (text, a test fixture, a design-first item). §4: a failed determination is counted on the
case file, a bench asks once per sitting, and a lapsed or dismissed matter is not re-opened without
something new. §5: nobody opens a case on himself. §6: a bench of several votes seat by seat, in one
place. §7: one Event kind renamed. §8: nothing (a question for Jordan, with its two shapes). Declared
movers: §4 to §7, each in every world where its verb executes.

## §1 Register, requirement and pointer text (edits; no behaviour)

Order: one commit, `[editorial]`, after `05_SC_contest_record_on_event.md` lands (its test is cited by one
row).

| # | owner file | edit | source |
|---|---|---|---|
| 1 | `engine/season/requirements.yaml`, the social-contest scale row | replace `in_loop: 'seam unbuilt'` and *"4 of 45 verb rows declare `contests:`"* with the measured reading: the roll is in the loop through seven prize-routed rows and three graded inquiries; three determinations in twelve seed-seasons at seeds 0 and 1 | G-05 |
| 2 | `engine/season/hole_register.yaml` H-276 | close; cite `sigma.py:210` (a self-plea has no opposition) and commit `c627426a` | G-15 |
| 3 | same, H-120 | close: every prize row is claimed | G-16 |
| 4 | same, H-226 | rewrite the head to the residue: `interrogate` is a resolvable row; it forms only where a live `detain` exists (none in the realm) | G-17 |
| 5 | same, H-131 | close the open half: a write window cannot outlive its write (`World.write`'s `finally: self.gate.close()`) | G-18 |
| 6 | same, H-113 | index status closed (`resolve.py:533`, `row.emits_at(_degree)`) | audit §6.1 |
| 7 | same, H-132, H-142, H-261, H-353 | re-file under FA; H-137, H-141, H-143 under CORE; H-228 under SE (a `lane:` or filing note, as the register carries it) | audit §6.1 |
| 8 | same, H-56 | carried by `05_SC_sc05_kernel_disposition_B.md` edit 5; listed here so the commit is one | G-37 |
| 9 | `proposals/2026-09-05-proceedings-subsystem/README.md`, Status | strike *"Nothing exists in `engine/season/` until SC-01"*; point at `registers/handoffs/HANDOFF_SC.md` | G-20 |
| 10 | `workplans/valoria_master_workplan_v11_part5.md`, SC-02 | record that its hold is a merge-default approval (`ED-1094`), not a ruling; release with CP-T05-01 and CP-T05-02 (i) as re-sourced by `05_SC_playable_hearing_B.md` edit 2 | audit §6.2 |
| 11 | `registers/editorial_ledger_sc.jsonl` | one row recording that R-31 to R-41 (`PD/…primitives-and-kinds.md` §1) are quoted intent, not ledgered rulings; a second for the relayed clarification of 2026-11-12 on the obstacle, with the reading `U5c_SC_one_obstacle_form.md` takes. Orchestrator's allocation (`references/id_reservations.yaml`) | addendum C-7, §B8 |

Gate: `python -m engine.season.harness.register --requirements` exits 0; `python tools/valoria_local.py`
green. Falsifier: any of rows 2 to 6 whose cited line does not say what the row claims at the landing
commit (open the line; a citation not opened is not a citation).

## §2 THE BAR is re-pinned on shipped fixtures (G-22, F-SC-12)

Depends on `05_SC_playable_hearing_B.md` edit 9 (`governance_spine.build_hearing`).

1. `engine/season/tests/test_sc01_the_bar.py`: replace the world found by sweeping 1,815 runs at
   `pool_default` 30 with `build_hearing(seed)` at `DEFAULT_FIXTURES`; assert, over seeds 0 to 39, that
   `matter.determined` and `matter.dismissed` each occur at some seed, and that the determining Event's
   `ending` carries `terms`. Assert it checked 40 worlds (`CLAUDE.md` §0.1 pt 2).
2. Delete `BAR_FIXTURES` and its *"OFF THE SWEEP"* note.

Gate: the file green on the landing commit; red with the roll pinned to Success (the instrument can see a
verdict that cannot be lost). Hash: none (a test).

## §3 The bundle: one act, several matters (G-25; design-first)

`ED-SC-0038` rules per-matter outcomes. One docket item per matter already gives one margin per matter. A
bundle is several docket items opened by one act and tried at one sitting. Design-first on CR-61 (the case
file names its matters). The plan the design pass must fill: (a) `open_case`'s payload may carry
`matters: (id, …)`; `_eff_open_case` appends one docket item per matter, all naming one case file;
(b) a sitting tries each item in docket order through the same entry; (c) a condition between matters is a
row of the case file, not code. Gate: a hand-built world in which one sitting binds on one matter and
dismisses another, each with its own `terms`. Not scheduled before B10-18c closes.

## §4 A hearing ends: the count, one asking per sitting, and what may be re-opened (C-08; F-PES-SC-07; PES-SC res. 4)

This section is the reconciled text of `05_SC_acquittal.md`; that file carries a `Reconciled:` line
pointing here. Depends on CR-61 (the docket item names its case file), as that file already says.

**Decided.** Three statements were in conflict: `05_SC_acquittal.md` (the first failed `determine`
dismisses), the SC addendum's G-55 (the count that dismisses is a row key, default 3, after P4 §3.5's
repair (e)), and `19_LACUNA_verdict_ladder_and_reversal.md` (acquittal at `Failure`, *"SC-P6 unchanged"*).
Ladder step 3: #453 §9.6, ratified as intent (`ED-IN-0288`), reads a failed determination as an acquittal;
P4 is a proposed design. So the key exists and its default is 1.

1. `engine/season/arrangements.yaml` and `data/arrangements.py`: key `ballots` (an integer of 1 or more;
   default 1; added to `_ARRANGEMENT_KEYS`; refused below 1). No seeded row changes. A row that wants the
   Venetian shape authors 3.
2. `engine/season/verb_table.yaml`, `determine`, band `Failure`: `writes: [Record.stages,
   DocketItem.matter]`, `emits: [matter.undetermined, matter.dismissed]`. Each kind is earned by its own
   receipt (the pattern `_eff_pardon` uses for `_RESTRAINT_ENDED`): the `failed` stage alone earns
   `matter.undetermined`; the docket write earns `matter.dismissed`.
3. `engine/season/loop/effects_information.py::_eff_determine`, the `Failure` branch (before any
   disposal is built, as `05_SC_acquittal.md` edit 2 orders): append `(tick, "failed", a.id)` to the case
   file; if the file now carries `ballots` `failed` stages since its last `opened` stage, also append
   `(tick, "dismissed", a.id)` and write every docket item naming the party back to `matter: None`.
4. **One asking per sitting.** `determine`'s typed cell gains a conjunct `sitting`: the case file carries
   no `failed` stage whose tick is at or after the tick of the sitting's `date.fired`. Refusal kind
   `determine.refused`, keyed `sitting`. With `ballots` 1 it cannot bind (a failure dismisses); it is what
   stops a bench with `ballots` 3 asking three times in one fold.
5. **The re-opening rule.** `open_case` and `carry` gain a typed conjunct `fresh`: the matter has no case
   file or petition whose newest stage is `dismissed` or `lapsed` within `docket_lapse` seasons, unless
   the act carries `cites` (`05_SC_evidence_and_rebuttal_B.md`) naming a held item that is not among that
   file's `filed` or `excluded` stages. Refusals `case.refused` and `carry.refused`, keyed `fresh`. A
   person who holds a claim of the dismissal or lapse does not form the act
   (`02_CHAR_offer_what_can_be_done.md`'s one decline, read off the conjunct).
6. `engine/season/loop/matter.py`, the lapse pass: when it lapses an item that names a case file or a
   petition, append `(tick, "lapsed", <date id>)` to that Record's stages in the same write.
   `[UNVERIFIED: that `(Record, stages)` admits the MATTER step in `write_matrix.yaml`; MATTER already
   matures stages, so the cell is expected `world_or_act`; the loader's refusal at import is the check.]`

Gate: `runs/PES_SC/p3_hearing_ends.py` re-run: (a) `k` determinations in one fold bind the party at most
once per sitting; (b) at `ballots` 1 a planted `Failure` leaves no docket item naming the party and one
`dismissed` stage; at 3, two planted failures leave the item and two `failed` stages, the third
dismisses; (c) after a lapse or a dismissal, `open_case` on the same party is refused on `fresh`, and the
same act carrying one new held item is admitted; (d) `05_SC_acquittal.md`'s own gate, with its last clause
read as (c). Falsifier: a planted `Success` that does not open the disposal; a second `determine` at one
sitting that reaches the roll; a re-opened matter with nothing new. Hash: declared mover wherever a
`determine` fails or a matter lapses.

## §5 Nobody opens a case on himself (PES-SC res. 6); where a petition goes (res. 5)

1. `engine/season/verb_table.yaml`, `open_case`: `counterparty: subject`. The fold's existing counterparty
   clause refuses `subject == actor`, and `opening_set`'s person-side self decline stops the act forming
   (`interview`'s precedent in `14_VERBS_SOCIAL2_A` edit 5). Gate: `realm_sc.py 1 4` re-run shows no
   `case.opened` whose party is its actor (two of eight today). Hash: declared mover.
2. Petition formation is not edited here: `14_VERBS_SOCIAL2_B_a_word_with_content.md` §3, as reconciled,
   fans `to` over the holders the petitioner's own ledger names for the seats over his home. That is the
   person-side form of PES-SC res. 5 (which proposed `judging_set`, a world read).

## §6 A bench of several votes seat by seat, in one place (C-11; F-SC-20; 13 §4 cell 9; sweep C-14)

Two proposals each gave the ballot a home: `13_SC_draw_for_unrolled_contests.md` (a host loop in
`_eff_determine` calling the seam once per member) and `05_SC_playable_hearing_B.md` (the module's close,
`HearingOutcome.ballots`). One owner (`CLAUDE.md` §8): the module.

1. A `determine` on a row whose `disposal` is `declared` always resolves through `social_contest.hearing`,
   also at `sitting_exchanges` 0.
2. At the close, each `Seat` draws once: his own pool against the closing obstacle, with leverage from a
   source `lean` (one `lean_level` per live public commit of his for the motion as aggressor, per commit
   against as defender; `world_q.declared_votes` returns the per-member counts that fill `Seat.lean`).
   `lean` joins `advantage_sources` after `custody` (`U5c_SC_one_obstacle_form.md` §3).
3. A ballot at Success or better is a vote for; at Failure against; at Partial an abstention. The provider
   sets `veto` when the votes for, weighted by `Seat.weight`, do not reach the row's `quorum`; the ladder
   then takes the minimum (`04` §C.5: a veto can only demote), so the determining act folds at `Failure`
   and §4 applies.
4. `engine/season/verb_table.yaml`, `determine`: the `vote` conjunct (`world_q.declared_votes` as a hard
   precondition) is deleted in the same commit. The count is no longer a gate; it is the odds.
5. `13_SC_draw_for_unrolled_contests.md` edits 3 and 4 are superseded by this section.

Gate: a planted `declared` sitting of five seats with commits three for and two against, 200 seeds: the
matter carries at some seeds and fails at others; with one seat's weight doubled the share that carries
moves. Falsifier: a sitting whose outcome is the same at every seed. Hash: declared mover wherever a
`declared` row is docketed (none in computed play today).

## §7 A won argument over an agreeing hearer is not "refused" (F-PES-SC-12)

`engine/season/verb_table.yaml`, `argue`: `emits_on_refusal` keyed, with `write: [argument.moot]` (new
kind; the other clauses keep `argument.refused`). Today a Success whose write declines (the hearer holds
no pursuit, or already stands where the arguer does) is emitted as `argument.refused` at degree Success.
Lands with `16_PESSIMIST_SC_D_an_argument_moves_someone.md`, which touches the same row. Gate:
`p5_argue.py` (e): 0 `argument.refused` at degree Success. Hash: declared mover.

## §8 Who a verdict is for (PES-SC, for Jordan): the two shapes, so either answer can be built

- **A, as ruled (C-1):** the disposal is the party's edge on the seat exercised. Nothing to build.
- **B:** a won case gives the petitioner something. It is not one row key: `oblige` runs from a person to
  a seat (`04` §B.7), so a remedy to a person is either a store movement the bench orders (a `transfer`
  from the party's rung to the petitioner's, opened as a disposal kind `damages` beside `oblige`,
  `detain`, `ban`, with its `stakes_ob` row) or a hold the bench passes (`give`'s handover basis). Both
  are design-first and both add a member to `DISPOSABLE_KINDS`. B changes what C-1 ruled about the edge's
  object, so it waits for Jordan.

## §9 The four things that did not draw (C-10), in one table

| what | decided | carrier |
|---|---|---|
| what a hearer believes once a telling lands | a reading over held items, not an outcome; the outcomes are the deposits, which are drawn (the telling's band; notice, `18_DETERMINISM_notice_is_a_draw.md`). No draw is added at read: a read is not an Event, and a belief drawn per read would give one person two beliefs in one season. The reading itself is repaired so it can come out either way as deposits vary | `16_PESSIMIST_SC_B` (confidence in the one comparator); `16_PESSIMIST_SC_E` edit 1 |
| whether a bench that failed may ask again | once per sitting; counted toward dismissal | §4 items 3 and 4 |
| whether a lapsed or dismissed matter may be re-opened | eligibility (something new), then the docketing draw for `carry` | §4 item 5; `14_VERBS_SOCIAL1_D` §1 |
| whether a convict may discharge an imposed service | he may attempt it (C-1's ruled price, not re-raised); whether he gets free is a draw | `U5c_VERBS_residue_and_governance_owner.md` §4 |

Docketing itself: `carry` is drawn (`14_VERBS_SOCIAL1_D` §1); `open_case` on one's own bench is a remit
act and is not (LACUNA §5; `convene`'s class).

## Layer 1 reading

§4: every write is an ACTS write by the determining judge under the `determination` basis or a MATTER
maturation citing the declaring act (`04` §B.8 T-n); no new gate basis. §6: the per-seat draws are margins
inside one provider call; no seat's state is written; the demotion uses the existing `veto` (`04` §C.5,
PART D row 23). §5: a counterparty column, no code. Grade of each: MECHANICAL (the loader and the gate
refuse the other shape), except §4 item 5's person-side decline (CONVENTION until its test).

## Cost class

§1, §5, §7: edit. §2, §4: small build. §6: inside `05_SC_playable_hearing_B.md`'s build. §3, §8:
design-first.
