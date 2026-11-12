# Unification run — lane definitions and the shared output form

## Status: WORK ORDER (the run plan for `UNIFICATION_BRIEF.md`; resolves nothing at runtime; deleted when the stage closes)

**Shape.** Share the reading, fork the judgment (CLAUDE.md §10). Wave 1: five **read lanes** (Sonnet, high), each reading one family of proposals *in full* and writing one `unified/work/R<k>_READ.md` (the Layer 1 grading, the fact and term extracts, the dependency edges, the ruling check, the test 9 check). A Haiku extraction pass is not used: the families are 500 to 800 KB each, over a Haiku window, and a second reading of them would repeat the read. Wave 2: **Opus** U1 (owners, vocabulary, glossary, capability architecture) and U3 (conflict ledger, dependency order) work from the `R<k>_READ.md` files plus targeted reads; they *decide in their ledgers* and edit no proposal. Wave 3: **Opus rewrite lanes**, one per family, apply the Layer 1 verdicts and the U1/U3 decisions to their own family's files only (disjoint edit sets, so no collision). Wave 4: **Sonnet** U4 (index, traceability, fact check, document status) with `valoria-measure` counts. Wave 5: one **Fable** read-only verdict.

**Limit, stated once.** Audits (`audits/`, 65 files, 4.6 MB), digests and dossiers are read at heads, decision tables and the closure tables (`unified/U5_FINDINGS_CLOSURE_*`), not in full: their findings already have a disposition. The unification stage guarantees full reading of the *proposals* (the things that will be built), and says so in `README.md` and `U4_DOCUMENT_STATUS.md`.

## The read lanes

| lane | family | files under `proposals/` |
|---|---|---|
| R1 | PC, MB, DICE, GO | `03_*`, `04_*`, `10_*`, `11_*`, `26_*`, `27_*`, `29_*`, `30_GO_*`, `U5b_PC_*`, `U5b_MB_*`, `U5a_DICE_*`, `U5d_GO_*` |
| R2 | CORE, CHAR, SC, FI, ARCS, LACUNA, scene access | `01_*`, `02_*`, `05_*`, `08_*`, `12_*`, `13_*`, `19_*`, `28_*`, `U5a_CHAR_*`, `U5a_CORE_*`, `U5a_capability_home_and_two_inputs.md`, `U5a_tests_digest_additions.md`, `U5c_FI_*`, `U5c_SC_*` |
| R3 | FA, SE, WR, stances, story enablement | `06_*`, `07_*`, `09_*`, `30_WR_*`, `31_*`, `U5d_FA_*`, `U5d_SE_*`, `U5d_WR_*`, `U5d_STORY_*` |
| R4 | verbs and institutions | `14_*`, `15_*`, `U5b_VERBS_*`, `U5c_VERBS_*` |
| R5 | cross-cutting | `16_*`, `17_*`, `18_*`, `20_*`, `21_*`, `22_*`, `23_*` |

Every file under `proposals/` is in exactly one lane (a lane that finds a file in none, or in two, says so in its receipt). Ground truth for the tree is `main` at the working tree; implementation lane A's two commits (`unified/OWED_TO_UNIFICATION.md` §E) are unmerged.

## Read first (every lane)

`CLAUDE.md`; `proposals/2026-11-12-subsystem-audit-suite/UNIFICATION_BRIEF.md` (the nine tests, the closure rule); `AUDIT_BRIEF.md` (standing rules); `unified/DECISIONS_ANSWERED.md` (A-1 to A-91, **governing**); `unified/OWED_TO_UNIFICATION.md`; `architecture/meta/04_CODE_ARCHITECTURE.md` (and, for `modules/`, `architecture/holonic_ARCHITECTURE.md` §43, §45 to §47); `skills/layer-conformance/SKILL.md` (Lens B method); `audits/25_GROUNDING_ENGINE.md` (the engine-grounding refutations: where a proposal relies on a claim it refutes, say so); the closure tables for your family (`unified/U5_FINDINGS_CLOSURE_*`). Then every file of your family, in full.

## What each `R<k>_READ.md` contains (write the head and section 1 before you finish reading; append the rest)

1. **Layer 1 conformance rows** (test 7): `| proposal file | edit (symbol/file it adds or changes) | Layer 1 row (§ and quote) | grade STRUCTURAL/MECHANICAL/CONVENTION per 04 §0 | verdict CONFORMS/VIOLATES/AMBIGUOUS | rewrite that conforms, or the conflict with two options |`. Read both halves of a §A.2 row. A violation is never resolved by editing Layer 1.
2. **Ruling check**: every place a proposal contradicts, or is silent where it must follow, a ruling A-1 to A-91 (`file:section`, ruling, the correct reading, the edit). This is the re-read of the verb and other bodies the rulings landed after.
3. **Fact extract** (test 2): `| fact (number, roster, closed set, rule, schema) | value | proposed owner file + key | other proposal that also states or owns it | agree/conflict |`. Only facts a proposal *proposes or relies on*; not prose.
4. **Term extract** (test 1): `| term | meaning in this proposal | tree owner (descriptor_registry, names_index, VOCABULARY.md) or "none" | same word other meaning / other word same meaning, with files |`.
5. **Edges** (test 5): `| proposal id (file) | depends on (proposal files or code symbols; mark each EXISTS-IN-TREE / PROPOSED / MISSING) | files it edits | hash movers declared | lane tag (MB PC FI SC FA WR IN GO SE) | gate named? | cost class and tier named? |`. A dependency that exists neither in the tree nor in a proposal is listed MISSING.
6. **Claims for the fact check** (test 6): counts, measurements and findings stated more than once, or stated here and elsewhere in the suite: `| claim | file:section | value | conflicts with (file:section, value) |`.
7. **Test 9** (implementation-ready): per proposal, COMPLETE or INCOMPLETE with the missing parts (files and symbols, order, schema, call sites, named tests, gate as an execution artifact with expected reading, falsifier and control, hash movers, dependencies, lands-it, cost and tier). Where the missing part is decidable from the repository, write the completing text in a sibling section `7b` (exact edit, ready for the rewrite lane); otherwise say what blocks it.
8. **Receipt** (<= 200 words) in your reply: files read (count), rows per section, contradictions found, conflicts for Jordan (two options each), anything unread.

## Rules (all lanes)

Nothing deterministic; ground every claim in a file you opened (`file:line`); do not guess; mark assumptions `[ASSUMPTION: ... — basis]`. Read-only on everything except your own `unified/work/` file: no edit of a proposal, audit, code, canon, registry or ruling; no commit; no pytest; no Bash edits. A finding that needs no ruling is recorded for the rewrite lane; a finding that overwrites a `(RULED)` item or a ratified Layer 1 rule is listed with two options. One round: do not recurse.

## Wave 2 to 5 inputs (for the later prompts)

U1 reads `unified/work/R*_READ.md` sections 3 and 4 plus `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`; U3 reads sections 5 and 6 plus the closure tables and the conflict ledgers `U5_CONFLICTS_U5a.md`, `U5_CONFLICTS_U5c.md`; rewrite lanes read their family's section 1, 2 and 7b plus U1/U3's decisions; U4 reads everything under `unified/`.
