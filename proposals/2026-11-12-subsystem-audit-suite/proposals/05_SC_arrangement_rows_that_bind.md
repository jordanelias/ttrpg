# SC-P4 — arrangement rows that bind: a band-keyed `disposes:`, and unread keys leave with the batch

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-08) — two row keys are added by other files and are read here as members of the same row: `ballots` (the count of failed askings that dismisses, default 1; `05_SC_acquittal.md`) and `disposes_to: petition` (`U5c_SC_proceedings_residue.md` §8; Jordan, A-38: a verdict serves the petitioner or a seat he names).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-P4 (AMBIGUOUS in spec), §2 row A-80, §7, §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-C12). Changed: the departure from Layer 1 is named at the site (`ban` and `detain` are disposal kinds the code already ships beyond `04` §B.8's tenure-kind list; this edit extends the union; B4's third disposition; `04` is not edited); A-80's entrenched-world control is cited (C3-C12); "What it does not do" is brought up to `05_SC_acquittal.md` as reconciled (a Failure now writes the `failed` stage and counts toward dismissal, A-81); the readers named for the key review are the reconciled ones; lands-it and tier added.

**Lands in batch:** B27. **Depends on:** plan positions CR-60, CR-61 and B10-18c's close (edit 5) `[PL]`; `05_SC_acquittal.md` (B27).

## Status: PROPOSED

Source: `audits/05_SC_audit.md` F-SC-06, §13 (ARC-10, ARC-21, ARC-31, EMG-X6); hole rows H-281, H-162.

## What it changes in `engine/season/` at runtime

For a matter docketed under a row whose `disposes:` is a band map, `determine` opens the Tenure kind
its band names (today: one kind for the three writing bands). Every seeded row keeps a scalar
`disposes:`, so no seeded world moves until a row is re-authored (a data edit, each a declared mover).
The second half deletes arrangement keys nothing reads; it changes no behaviour by construction.

## The problem (evidence)

1. **A verdict has grades and one consequence.** `loop/effects_information.py::_eff_determine`
   opens `ARRANGEMENTS[row]["disposes"]` at `Overwhelming`, `Success` and `Partial` alike (`:614`,
   `_disposal` `:677-703`); the band survives only as `Tenure.degree`, whose one reader
   (`queries/faction_q.py:146`) filters to `t.kind == "commit"` (grep for `.degree` readers under
   `engine/season/` at `601e715`: that line, the hash and the gate's diff, nothing else). The provided
   arcs state the need as core:
   ARC-21 *"more than two outcome tiers, each with a categorically different consequence set"*;
   ARC-10 *"fully reversing a punishment, merely reducing its severity, or leaving the punishment
   standing"*; ARC-31, EMG-X6.
2. **Ten of thirteen keys are read by nothing.** Readers under `engine/season/` (non-test): `disposes`
   (`effects_information.py:429, :614`; `state/gate.py:274`), `disposal` and `quorum`
   (`queries/world_q.py:731, :4685`). No reader: `bench_basis`, `floor`, `records_dissent`,
   `venue_min_rank`, `term_required`, `appeal_basis`, `interposed`, `order`, `proofs`,
   `disposal_reach` (grep at `601e715`; H-281 names four of them). `speech_kinds` (six rows) has no
   reader at all.
3. **The rows that are read are reached by hand only.** A computed `open_case` writes
   `DOCKET_ARRANGEMENT: None` (`effects_information.py:412-418`), so every computed disposal is
   `UNDECLARED_DISPOSAL` (`oblige`). That half is the plan's (CR-60, CR-61: exit *"docket items
   naming a row above 0"*) and is not re-proposed here.

## The resolution, decided

**(a) `disposes:` may be a map from band to kind** (ladder step 5: the band is already the key
`verb_table.yaml` uses for `writes:`/`emits:`; one more band-keyed cell is the table's own method,
not a new one). **(b) A key with no reader when B10-18c closes is deleted in that close commit**
(ladder step 4: `rosters.yaml: record_kinds`' own note, *a kind lands WITH the reader that needs it*;
`CLAUDE.md` §0.05, a fact code does not read is not yet a fact).

## Exact edits, by owner

1. `engine/season/data/arrangements.py::_load_arrangement` — accept `disposes:` as a scalar (today)
   or a mapping whose keys are a subset of the writing bands (`DEGREE_BANDS` minus the band whose
   `determine` `writes:` cell is empty — read off `VERB_TABLE`, not spelt) and whose values pass the
   scalar's own check; normalise to a mapping `{band: kind}` in the returned row (a scalar becomes the
   same kind at every writing band). Refuse a map naming a band `determine` does not write at.
2. `engine/season/loop/effects_information.py::_eff_determine` — `kind = row_map[res.degree]` where
   `res` is present; a hand-built call with no contest takes the map's `Success` entry (the scalar
   case is unchanged). `_disposal` is unchanged (one literal `Tenure(...)` per kind).
3. `engine/season/state/gate.py::DISPOSABLE_KINDS` — union over the map's values. **Layer 1, named at the
   site:** `04` §B.8's tenure-kind list does not name `ban` or `detain`; the code already ships both as
   disposal kinds (the `determination` basis, `04` §C.2) and this edit extends the union. The spec row is
   behind the code; under `skills/layer-conformance` B4's third disposition the departure is recorded in
   `DISPOSABLE_KINDS`'s docstring, and `04` is not edited (CLAUDE.md §0.05).
4. `engine/season/arrangements.yaml` — no row changes in this proposal. The first re-authoring is
   content (Jordan's or a later position's), e.g. `legal_trial: {Overwhelming: ban, Success: detain,
   Partial: oblige}`; it is named here only as the falsifier's fixture.
5. At B10-18c's close: for each of the ten keys above and `speech_kinds`, either cite the reader that
   landed (`appeal_basis`: `19_LACUNA_verdict_ladder_and_reversal.md` and CR-59; CR-62 the plea ids;
   `proofs`: the admission filter of `13_SC_tuning_tables.md` T5 and `05_SC_evidence_and_rebuttal_B.md`;
   `ballots`, `disposes_to`: `05_SC_acquittal.md`, `U5c_SC_proceedings_residue.md` §8), or delete the key from `_ARRANGEMENT_KEYS`, the loader body and every row. The
   transcription survives where it came from (`proposals/2026-09-05-proceedings-subsystem/
   03_PARAMETERS.md` §E.2).

## Gate (execution artifact)

`engine/season/tests/test_arrangements.py`: a hand-docketed matter under a band-mapped row, folded at
three planted margins, opens three different Tenure kinds; a scalar row opens one. Content hashes of
`build_realm(0)` at 0, 1 and 2 seasons are unchanged by edits 1–3.

Named tests (added to `engine/season/tests/test_arrangements.py`, exists):
`test_a_band_mapped_disposes_opens_the_kind_its_band_names`, `test_a_scalar_disposes_normalises_to_itself`,
`test_a_map_naming_a_band_determine_does_not_write_at_is_refused`.

**Control for A-80.** A-79 makes positions hold; A-80 requires entrenchment still to move the world. The
control arm is the entrenched-world arm carried by `28_CORE_scene_access_A_occupancy_and_precedence.md`
gate row 12, `28_CORE_scene_access_C_the_petition_that_waits.md` gate row 7 and
`23_STORY_D_story_census_and_gate.md` (C3-C12).

## Falsifier

A fourth planted margin at `Failure` opens no Tenure (the map cannot reach the band the row does not
write at; the Failure band's own write is the `failed` stage of `05_SC_acquittal.md`). If any seeded hash moves at edits 1–3, a scalar row was not normalised to itself.

## What it does not do

It gives `Failure` no disposal: a Failure writes the case file's `failed` stage and counts toward
dismissal (`05_SC_acquittal.md`, `ballots`), so it is never a still band (A-81); what a failed challenge
costs the challenging institution (H-219, H-221; ARC-21's *"a failed formal challenge … must weaken the
challenging institution"*) stays design-first and is listed in audit §13. It
does not make a `Record`-disposing row determinable (`parliamentary_debate`, `council_of_state`):
that needs the `resolution` Record kind (CR-36/CR-37, B10-17).

## NERS reading

- **N**: without it a verdict's degree changes a field nothing reads. With it, how well the bench is
  persuaded changes what happens to the man (top-down: verdicts differ; bottom-up: the band exists;
  diagonal: governance reads `detain`/`ban` already — `sides_of` excludes a prisoner from a muster).
- **R**: categorically different outcomes from one draw; authored per institution in data.
- **S**: the same band-keyed cell the verb table uses; no second ladder, no band table.
- **E**: one loader branch, one index, one set union.

## Cost class

Edit (items 1–3); the key deletion is an edit at a batch close.

**Lands it and tier.** The B27 batch, an SC `valoria-author` session on `sonnet` (`high`), closed by B27's
`methodology-close`; edit 5 at B10-18c's close. **Hash movers.** None at edits 1–3 (control: every seeded
row scalar); each row re-authored to a band map is a declared mover.
