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
