# 19 · LACUNA · 3 — Five results from one draw: conviction, partial, acquittal, mistrial, reversal; and the case thread the chronicle can retell

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — a telling *from a viewpoint* reads `account` (`11_GO_player_surface_contract_B.md` §4), not `world_q.projection`, which `17_CENSUS_C1A_01_deletion_batches.md` D2 deletes.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-17) — three changes. (1) The `voided` stage is written by the next `convene` that reads the refused Event, never on the refusal path (a refused act writes nothing). (2) Reversal: the appellate bench writes the `reversed` stage and the finding is told; the disposing seat's bench then closes the edge by its own `pardon`. The gate's `determination` basis closes a disposal only through the seat that is its object, and closing it from above needs a basis `04` §C.2 does not list. (3) "Open for the design pass" is answered: appeal on new grounds only (Jordan, A-39), read by the `fresh` conjunct of `U5c_SC_proceedings_residue.md` §4.

## Status: PROPOSED (results 1-4 are edits on existing owners; reversal is design-first; the case thread is harness only)

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
3. A disposal once opened can be closed by `pardon` (detain, ban: clemency, the bench's grace) or
   `release` (oblige, by its owner, C-1's ruled price), but nothing **reverses** a determination as wrong.
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
- At `Success` / `Overwhelming` it **closes the disposal** (`Tenure.until`, as `pardon`'s write) and writes
  `(tick, "reversed", act id)` on the original case file; at `Partial` it reduces the disposal's `degree`
  by one band; at `Failure` it **affirms** (`(tick, "affirmed", act id)`), and the disposal stands.
- Reversal differs from `pardon` in what witnesses hold: a pardon is a deed of grace (the convict stays
  convicted in every ledger); a reversal is a determination that the first was wrong, so the original
  determiner's `reception` falls by the existing path (a told deed of his reversed finding) and the
  convict's deeds-judged reading clears where the reversal is held.
- Open for the design pass (named, not decided): whether the appellate bench must be another seat or may
  be the same seat at a higher sitting; how many appeals a case admits (proposed: one per rung, bounded by
  the rung ladder).

**R-19-09 · The case thread (harness).** `harness/chronicle.py` gains `case_thread(w, case_file_id) ->
list[line]`: from the determination (or dismissal, voiding, reversal) back through the case file's stages to
the first deed claim each filed item cites, printed with `subject_of` / `anchor_of` as
`09_WR_B_chronicle_that_tells` decides, and from a viewpoint where asked (`world_q.projection`). It is how
the realm "retells" a case: who did it, who said so, on what, what the bench held, what later contradicted
it. Reads only; asserts the content hash unchanged after a render, as `test_in37_chronicle.py` does.

## Exact edits, by owner

1. `engine/season/loop/effects_information.py::_eff_determine` — none beyond SC-P6.
2. `engine/season/loop/resolve.py` (the refusal path for `determine`'s `bench` / `quorum` conjuncts): where
   the docket item names a case file, append the `voided` stage under the case file's own `Subject.entity`
   (`fields=("stages",)`), as SC-P6's dismissal write does. `[UNVERIFIED]`: whether a refusal path may
   write; if the fold forbids writes on refusal (likely: *"failure emits, never raises"*), the voiding is
   written instead by the next `convene` of that venue reading the refused Event — a design-first choice
   recorded here, not taken.
3. `modules/social_contest/evidence.py::standing` (SC `_B` edit 3) returns, beside `faults`, a
   `voided: bool` when no `for` item stands after an origin-wide strike; the host writes the stage.
4. `engine/season/verb_table.yaml` `determine` — an appellate reading is not a new row: an `appeal` is a
   `petition` + `carry` with `terms` naming a Tenure, heard by `determine`. The row's `writes` gains
   `Tenure.until` at `Success` / `Overwhelming` and `Tenure.degree` at `Partial`, keyed on a docket item
   whose `DOCKET_PETITION`'s terms name a live disposal (design-first: whether this belongs on `determine`
   or a sibling row `reverse` with `remit:determine`; the sibling is cleaner for the loader's write
   matrix and is the recommended reading).
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
- reversal (after the design pass): a conviction under an arrangement with `appeal_basis: determine`,
  appealed above, closes the disposal at `Success` in a share strictly between 0 and 1 over 200 seeds;
  under `appeal_basis: none` the appeal is refused before the draw;
- `case_thread` on the determined case prints the determination, each filed item and the deed claim it
  cites; the content hash is unchanged by the render.

## Falsifiers

- If a `voided` stage appears on a matter that was determined, the void write runs on a decided sitting.
- If a reversal leaves the original determiner's `reception` unchanged in every judge who holds the
  reversal, the reversal is not being told and is indistinguishable from a pardon.
- If `appeal_basis: none` rows can be appealed, the reader is not wired.

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

R-19-06: none (SC-P6). R-19-07: small build. R-19-08: design-first, then small build. R-19-09: edit
(harness). Lanes: SC (owner), WR (chronicle), FA where an appellate seat is a faction's.
