# 19 · LACUNA · 3 — Five results from one draw: conviction, partial, acquittal, mistrial, reversal; and the case thread the chronicle can retell

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — a telling *from a viewpoint* reads `account` (`11_GO_player_surface_contract_B.md` §4), not `world_q.projection`, which `17_CENSUS_C1A_01_deletion_batches.md` D2 deletes.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-17) — three changes. (1) The `voided` stage is written by the next `convene` that reads the refused Event, never on the refusal path (a refused act writes nothing). (2) Reversal: the appellate bench writes the `reversed` stage and the finding is told; the disposing seat's bench then closes the edge by its own `pardon`. The gate's `determination` basis closes a disposal only through the seat that is its object, and closing it from above needs a basis `04` §C.2 does not list. (3) "Open for the design pass" is answered: appeal on new grounds only (Jordan, A-39), read by the `fresh` conjunct of `U5c_SC_proceedings_residue.md` §4.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row (head CONFORMS; body R-19-08 and edit 4 VIOLATE), §2 rows A-37, §7, §7b-12, §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-L4, C3-Y9; `unified/U3_DEPENDENCY_ORDER.md` node B27, §4.1 rows 3 and 83). The body is brought to its head: R-19-08 and edit 4 no longer have the appellate `determine` write `Tenure.until`/`Tenure.degree` on another seat's disposal (`04` §C.2: the `determination` basis closes a disposal only through the seat that is its object) — the appellate bench writes the original case file's `reversed` stage and emits `matter.reversed`, and the disposing seat's bench closes the edge by its own drawn `pardon`; edit 2's refusal-path write is replaced by the next `convene`'s write (head 1; a refused act writes nothing, which settles its `[UNVERIFIED]`); problem 3's "`release` (oblige, by its owner, C-1's ruled price)" is struck (A-37: an imposed service ends by the bench's pardon or its term); the design pass's open questions are answered where the rulings answer them (A-39, new grounds only); `world_q.projection` → `account` (C3-L4; C1A_01 D2 deletes it); the chronicle line lands in B36 (U3 §4.1 row 83); named tests, lands-it and tier.

**Lands in batch:** B27 (R-19-07, R-19-08); R-19-09 in B36 with `09_WR_B_chronicle_that_tells.md`. **Depends on:** `05_SC_acquittal.md` (B27), `05_SC_evidence_and_rebuttal_B.md` (B24), `U5c_SC_proceedings_residue.md` §4 (B27; `fresh`, `new_items`), `17_CENSUS_C1A_01_deletion_batches.md` D2 (B03), `11_GO_player_surface_contract_B.md` (B34; `account`).

Reconciled: 2026-11-12, repair lane R-B (`unified/U6_VERDICT_AND_REPAIRS.md` finding 1) — reversal's three open design points are decided at R-19-08 and edit 4 (sibling row `reverse`, `eligibility: ["remit:determine"]`, `verb_table.yaml:33`; appellate bench on a higher rung; one appeal per rung), so the file no longer leaves a design pass open; the "design-first" cost-class label is removed.

## Status: PROPOSED (results 1-4 are edits on existing owners; reversal's shape is decided (R-B); the case thread is harness only)

Carries `audits/19_LACUNA_investigation_to_proceedings.md` §3 ("The verdict ladder"), §4.6 and resolutions
R-19-06 to R-19-09. Consumes `05_SC_acquittal.md` (SC-P6) unchanged, `05_SC_evidence_and_rebuttal_B.md`
(the `forgery_found` fault) and `09_WR_B_chronicle_that_tells.md` (the chronicle's owners). Precedent:
Lacuna has no court (T19 §LA: *"no courts or sentencing system found"*); its consequences cascade by
authored branching (Colbus devlog, page read). Ace Attorney's verdict is binary and authored (T19:173-216).
Valoria's verdict is a draw; this file names the results that draw already distinguishes and the two it
does not.

## What this changes in `engine/season/` at runtime

Results 1-3 change nothing beyond SC-P6 (which this file adopts). Result 4 (mistrial) adds one stage to the
case file when a sitting cannot close; declared mover wherever `determine` refuses on `bench` or `quorum`
with a case file present, or a side is struck entire. Result 5 (reversal) gives `arrangements.yaml:
appeal_basis` its first engine reader (today read only by `tests/test_arrangements.py:43-73`); a declared
mover wherever a disposal is appealed, which no computed play reaches until the chooser forms appeals.
The case thread is a rendering in `harness/chronicle.py`: nothing at runtime.

## The problem (evidence)

1. `determine` (`verb_table.yaml`) distinguishes four bands; at `Failure` it emits `matter.undetermined`
   and the matter is re-heard each season with no acquittal path (H-162 (c); SC-P6's evidence). SC-P6
   repairs this; this file adopts it and adds nothing to it.
2. A sitting that cannot decide (no bench, no quorum: `determine`'s `bench` / `quorum` conjuncts, keyed
   refusals `determine.refused`) leaves no mark on the case: the refusal Event exists, the case file does
   not record that a trial was attempted and failed. An accused cannot cite it; the chronicle cannot say it.
3. A disposal once opened can be closed by `pardon` (the bench's grace; for an imposed `oblige` too, which
   the convict may not release himself, A-37) or by its term, but nothing **reverses** a determination as
   wrong.
   `appeal_basis: determine` is carried on three rows (`arrangements.yaml:185`, `:242`, `:280`) and read by
   nothing; §E.2's *"appeal to a higher authority"* game is unseeded (`arrangements.yaml:45`).
4. The determination is witnessed, but no reading strings a case together: the chronicle picks by depth
   and prints no subject (`09_WR_B_chronicle_that_tells.md` problems 1-2).

## The resolution, decided

**R-19-06 · Conviction, partial, acquittal are the determine bands, as built plus SC-P6.** `Success` /
`Overwhelming` open the arrangement's disposal at that `degree`; `Partial` opens it at `degree: Partial`
(the lesser sentence; what a degree reader scales is H-162's and is not decided here); `Failure` dismisses
(SC-P6). No edit beyond SC-P6. Ladder step 1 (the row is built; SC-P6 takes H-162 (c)'s written revert).

**R-19-07 · Mistrial is a stage, not a band.** A mistrial is not a fourth way the draw can fall; it is the
draw not happening. Two causes: (a) `determine` refuses on its `bench` or `quorum` conjunct (eligibility:
whether the sitting may decide at all, the brief's carve-out); (b) every `for` item is struck origin-wide
by an `Overwhelming` impeachment (`forgery_found`, `05_SC_evidence_and_rebuttal_B` rule 1), which is the
outcome of a draw already made. In both, the case file gains `(tick, "voided", cause, act id)`; the matter
stays docketed (the standing court re-hears it, `world_q.sittings_before`). The accused may cite a
`voided` stage (a `record` kind item). Ladder step 5: the event exists, the record of it does not, and the
case file is the one owner of what happened in the proceeding (E-4).

**R-19-08 · Reversal is an appeal heard above, read from `appeal_basis`.** Design-first; the decided shape:
- A **petition whose `terms` name a disposal Tenure** (the convicted man, his kin, his advocate: anyone
  holding the petition) is `carry`'d to a bench whose rung is above the disposing seat's rung, and is
  admitted only where the disposing arrangement's `appeal_basis` is `determine` (eligibility; `none` makes
  the finding final, as the column already says, `arrangements.yaml:197`).
- The appellate `determine` is the same draw; its obstacle reads the original case file's stages as the
  items (filed, excluded, struck, voided) plus whatever the appellant files new.
- At `Success` / `Overwhelming` it writes `(tick, "reversed", act id)` on the original case file (an ACTS
  write by the determining judge under the `determination` basis; the case file is the proceeding's
  record) and emits `matter.reversed`, which WITNESS tells; it does **not** close the disposal, which is
  another seat's edge (`04` §C.2 lists no basis for closing it from above). The disposing seat's bench
  then closes the edge by its own `pardon`, a drawn act it forms on holding the reversal (the reversal is
  leverage for it, never a gate). At `Partial` it writes `(tick, "remitted", act id)` (the sentence found
  excessive; the disposing bench may lessen it by its own act) `[ASSUMPTION: the Partial band's stage
  name and reading — basis: the same one-owner rule as `reversed`]`; at `Failure` it **affirms**
  (`(tick, "affirmed", act id)`), and the disposal stands. Every band writes a stage (A-81).
- Reversal differs from `pardon` in what witnesses hold: a pardon is a deed of grace (the convict stays
  convicted in every ledger); a reversal is a determination that the first was wrong, so the original
  determiner's `reception` falls by the existing path (a told deed of his reversed finding) and the
  convict's deeds-judged reading clears where the reversal is held.
- Answered (head 3; A-39): an appeal is admitted **on new grounds only** — an excluded item, a voided stage,
  or a new item from a distinct source — read by the `fresh` conjunct and the `new_items` schema cell of
  `U5c_SC_proceedings_residue.md` §4 item 5 (one reader for both). Still open for the design pass (named,
  not decided): whether the appellate bench must be another seat or may be the same seat at a higher
  sitting; how many appeals a case admits beyond the new-grounds rule (proposed: one per rung).
  **Decided (repair R-B, ladder step 5; the first bullet already says the bench's rung is above the disposing
  seat's, so a same-seat appeal is excluded by that eligibility; the proposed count is taken):** the appellate
  bench is another seat on a rung above the disposing seat's, never the same seat at a higher sitting; a case
  admits at most one appeal per rung above the disposing seat's (a count of the case file's `reversed`/
  `remitted`/`affirmed` stages by rung, read with the `fresh` conjunct). Both are revertible to the previous
  open state by deleting this paragraph.

**R-19-09 · The case thread (harness).** `harness/chronicle.py` gains `case_thread(w, case_file_id) ->
list[line]`: from the determination (or dismissal, voiding, reversal) back through the case file's stages to
the first deed claim each filed item cites, printed with `subject_of` / `anchor_of` as
`09_WR_B_chronicle_that_tells` decides, and from a viewpoint where asked (`account`,
`11_GO_player_surface_contract_B.md` §4; `world_q.projection` is deleted by C1A_01 D2, C3-L4). Lands in B36
with the chronicle. It is how
the realm "retells" a case: who did it, who said so, on what, what the bench held, what later contradicted
it. Reads only; asserts the content hash unchanged after a render, as `test_in37_chronicle.py` does.

## Exact edits, by owner

1. `engine/season/loop/effects_information.py::_eff_determine` — none beyond SC-P6.
2. `engine/season/loop/effects_information.py`, the `convene` effect: the next `convene` of that venue reads
   the `determine.refused` Event keyed `bench` or `quorum` for a docket item that names a case file and
   appends `(tick, "voided", cause, refused act id)` under the case file's own `Subject.entity`
   (`fields=("stages",)`), as its own ACTS write. A refused act writes nothing (head 1; `04` §C.4: a
   refusal emits), so the refusal path is not edited.
3. `modules/social_contest/evidence.py::standing` (SC `_B` edit 3) returns, beside `faults`, a
   `voided: bool` when no `for` item stands after an origin-wide strike; the host writes the stage.
4. `engine/season/verb_table.yaml` — an appellate reading is a `petition` + `carry` with `terms` naming a
   Tenure, heard by a determining act whose `writes` are `Record.stages` at every band (the original case
   file's `reversed` / `remitted` / `affirmed` stage) and whose emits are `matter.reversed`,
   `matter.remitted`, `matter.affirmed`; it writes no `Tenure` cell. **Decided (repair R-B, ladder step 5):**
   the row is a sibling `reverse`, not `determine` on such a docket item. Its `eligibility` is `["remit:determine"]`
   (one of the four kinds `verb_table.yaml:33` names; `remit:<act>` is the form `arrest` and `confer` already use at
   `:173`, `:271`), so the loader needs no new kind and `determine`'s own row is untouched. The closing of the edge
   is the disposing bench's `pardon` (existing row; drawn).
5. `engine/season/arrangements.yaml` — `appeal_basis` gains its reader (the eligibility above); the
   unseeded *"appeal to a higher authority"* row is seeded with `disposes: Record` (it disposes the original
   case file's finding, not a person) once the reader exists.
6. `engine/season/harness/chronicle.py` — `case_thread` (R-19-09).

## Gate (execution artifacts)

On `build_hearing(seed)` with a case file, `PYTHONHASHSEED=0`:
- planted bands: `Success` opens the disposal, `Partial` opens it at `degree: Partial`, `Failure` emits
  `matter.dismissed` (SC-P6's gate, re-run);
- a bench with its quorum removed: `determine.refused` on `quorum`, and the case file carries one `voided`
  stage; the matter is still docketed; restoring the quorum lets the next sitting determine it;
- with every `for` item a Record of one forger's origin and an examiner holding the forged claim, over 200
  seeds the `voided` stage occurs in a share strictly between 0 and 1 and only on `Overwhelming`
  impeachments;
- reversal (the `reverse` row): a conviction under an arrangement with `appeal_basis: determine`,
  appealed above on new grounds, writes the `reversed` stage in a share strictly between 0 and 1 over 200
  seeds, and the edge closes only after the disposing bench's `pardon`; under `appeal_basis: none`, or with
  nothing new, the appeal is refused before the draw;
- `case_thread` on the determined case prints the determination, each filed item and the deed claim it
  cites; the content hash is unchanged by the render.

**Named tests** (new, `engine/season/tests/test_verdict_ladder.py`): `test_planted_bands_open_partial_and_dismiss`;
`test_a_quorumless_sitting_is_voided_by_the_next_convene_and_the_matter_stays_docketed`;
`test_voided_occurs_only_on_overwhelming_impeachment_in_a_share_strictly_between_0_and_1`;
`test_a_reversal_writes_a_stage_and_the_edge_closes_only_by_the_disposing_benchs_pardon`;
`test_an_appeal_without_new_grounds_is_refused`; and, in B36,
`engine/season/tests/test_in37_chronicle.py::test_case_thread_render_moves_no_hash`.

## Falsifiers

- If a `voided` stage appears on a matter that was determined, the void write runs on a decided sitting.
- If a reversal leaves the original determiner's `reception` unchanged in every judge who holds the
  reversal, the reversal is not being told and is indistinguishable from a pardon.
- If `appeal_basis: none` rows can be appealed, the reader is not wired.
- If an appellate act writes `Tenure.until` or `Tenure.degree` on a disposal whose object seat it does not
  exercise, the write gate's basis list has been widened (`04` §C.2) and the edit is wrong.

## NERS reading

- **N**: a trial with one terminal state is a clock (SC-P6's case); a trial that cannot fail to happen
  and cannot be overturned has no recourse, and *"recourse"* is one of the arcs' needs (ARC-04, *"defeat an
  accusation for the present while leaving the underlying case file intact and reopenable"*, as cited in
  SC-P6). Lateral: `pardon` exists, so reversal must earn its place by what witnesses hold (a wrong finding,
  not a grace), and it does.
- **R**: the convicted and their kin have a move; benches have a reputation that a reversal can cost;
  without a player, an NPC appeals and a high bench reverses a low one, a political story with no author.
- **S**: one draw at every bench; one case file; no second lifecycle; the chronicle reads owners WR names.
- **E**, last: one stage kind, one column given a reader, one harness function, against a proceeding that
  today has neither a record of failure nor a remedy.

## Cost class

R-19-06: none (SC-P6). R-19-07: small build. R-19-08: small build (its design pass is closed above by repair R-B; the
`opus` read below is the one read of the `reverse` row's `requires`). R-19-09: edit
(harness). Lanes: SC (owner), WR (chronicle), FA where an appellate seat is a faction's.

**Lands it and tier.** R-19-07 and R-19-08's built half in the B27 batch, `valoria-author` on `sonnet`
(`high`), with one `opus` read (with `ners`) of the `reverse` row's `requires` (the shape is decided above); R-19-09 in B36 on
`sonnet`; each batch's `methodology-close` once. **Hash movers.** Mistrial (wherever `determine` refuses on
`bench`/`quorum` with a case file); reversal (declared, once the chooser forms appeals).
