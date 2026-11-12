# SC-P4 — arrangement rows that bind: a band-keyed `disposes:`, and unread keys leave with the batch

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-08) — two row keys are added by other files and are read here as members of the same row: `ballots` (the count of failed askings that dismisses, default 1; `05_SC_acquittal.md`) and `disposes_to: petition` (`U5c_SC_proceedings_residue.md` §8; Jordan, A-38: a verdict serves the petitioner or a seat he names).

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
3. `engine/season/state/gate.py::DISPOSABLE_KINDS` — union over the map's values.
4. `engine/season/arrangements.yaml` — no row changes in this proposal. The first re-authoring is
   content (Jordan's or a later position's), e.g. `legal_trial: {Overwhelming: ban, Success: detain,
   Partial: oblige}`; it is named here only as the falsifier's fixture.
5. At B10-18c's close: for each of the ten keys above and `speech_kinds`, either cite the reader that
   landed (CR-59 `appeal_basis`; CR-62 the plea ids; SC-P3's proofs filter may read the row's
   `proofs`), or delete the key from `_ARRANGEMENT_KEYS`, the loader body and every row. The
   transcription survives where it came from (`proposals/2026-09-05-proceedings-subsystem/
   03_PARAMETERS.md` §E.2).

## Gate (execution artifact)

`engine/season/tests/test_arrangements.py`: a hand-docketed matter under a band-mapped row, folded at
three planted margins, opens three different Tenure kinds; a scalar row opens one. Content hashes of
`build_realm(0)` at 0, 1 and 2 seasons are unchanged by edits 1–3.

## Falsifier

A fourth planted margin at `Failure` opens nothing (the map cannot reach the band the row does not
write at). If any seeded hash moves at edits 1–3, a scalar row was not normalised to itself.

## What it does not do

It gives `Failure` no consequence (H-219, H-221: design-first; ARC-21's *"a failed formal challenge
… must weaken the challenging institution"* stays unrepresented and is listed in audit §13). It
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
