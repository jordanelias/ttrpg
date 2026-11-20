# Census brief — identify everything broken, missing, unread, unwritten, dead; resolve so everything works

## Status: WORK ORDER (Jordan's direction of 2026-11-12: *"Fable to identify all broken and missing and not read and not written etc etc etc and resolve so everything works"*; not canon)

A one-off static census of the game code was run (`census/C1..C6`, built by a name-based script; every
row is a LEAD to verify at the call site, CLAUDE.md §0.1 pt 3):

- `census/C1_unreferenced_symbols.md`: top-level functions and classes the game code never names outside
  their own file (about 830).
- `census/C2_record_fields.md`: dataclass fields declared but never read and/or never written (72 of 740).
- `census/C3_registry_keys_no_code_names.md`: season registry keys no code names (14).
- `census/C4_event_kinds_emitted_without_consumer.md`: emitted event kinds with no named consumer.
- `census/C5_hole_register_stale_pointers.md`: hole-register `site:`/`owner:` pointers that no longer resolve.
- `census/C6_composition_targets_that_do_not_resolve.md`: composition and contract targets that do not.

## For each row, decide and resolve (do not park)

Verify at the call site (read the code that would use it; run a one-line probe where cheap). Then exactly
one of:

1. **Dead: delete.** Nothing needs it and no requirement, case, proposal or ruled design will. Give the cut
   test (what dies). Deletions are the cheap edits: write them as a deletion list with the exact symbols and
   files, grouped so a lane can land a batch with its test updates (CLAUDE.md §2: retiring something means
   deleting it and writing a `FORK:` row; give the row text).
2. **Broken: wire.** A requirement (R-01..R-09), a provided case, a ruled design, an accepted proposal in this
   suite, or Jordan's stated intent needs it, and the wire is cut (a field never written, an event
   never consumed, a verb never formed, a registry key never read). Write the missing writer or reader at the
   single owner, typed, Layer-1 conformant, with the gate that shows it works (an execution artifact) and
   the falsifier. This is the "so everything works" half: nothing is left declared and inert.
3. **Mislabelled: correct.** A stale pointer, a wrong comment, a retired name still cited: write the exact
   text correction.
4. **False positive.** The name-based census missed a dynamic use: say how it is reached (the `getattr`,
   the string-built key, the registry iteration) so the lead is closed with its evidence.

Also extend the census where the script cannot see: verbs that the corpus reports as having no
predicate/effect or never executing (`python -m engine.season.harness.corpus_run`, `register
--requirements`), records written but never read by anything downstream (follow the writers in
`write_matrix.yaml` to their readers), rosters with a closed set but no loader refusal, tests that
exercise code nothing calls, and documents that describe code that does not exist.

## Output and limits

`audits/17_CENSUS_<PART>.md` (verdict first; table: row, reading, decision, evidence) and proposals
`proposals/17_CENSUS_<PART>_*.md` (deletion batches with exact lists; wiring edits; corrections), ordered by
risk. Counts at the top: rows examined, dead, broken, mislabelled, false positive. Authority and limits as
`AUDIT_BRIEF.md`; Layer 1 conformance as `UNIFICATION_BRIEF.md` item 7; the suite's other proposals decide
what "needed" means (cite them). Edit only your own files; no commit; no pytest; no Bash edits of tracked
files outside the suite. Write early and append. Receipt <= 200 words.
