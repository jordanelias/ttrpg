# Valoria subsystem audit and unification suite — index and reading order

## Status: REFERENCE (the suite's index; resolves nothing at runtime, CLAUDE.md §0.05; not canon; names no number the code reads)

Written by unification lane U4c on 2026-11-12. Counts below are those of `unified/U4_DOCUMENT_STATUS.md` at its generating run; re-run that table rather than trusting a figure here.

## 1. What the suite is

A set of design documents produced on 2026-11-12 by many parallel Fable lanes and then made to agree with one another. Nothing in it is canon and nothing in it is built: it changes no code, no canon, no registry and no ruling (`UNIFICATION_BRIEF.md`, "Closure rule"). It holds, in this order of production:

1. **Dossiers and digests** of the tree (script-built indexes and coverage extracts), read before the audits.
2. **Audits** (`audits/`): per-subsystem audits and their addenda (CORE, CHAR, PC, MB, SC, FA, SE, FI, WR, DICE, GO, ARCS), the verbs, the institutions, the pessimist audits, the census, the determinism sweep, narrative churn, procedural generation, happenings, story enablement, two grounding passes, and the later lanes 26 to 31 (mass-battle history, command, scene access, the one opposed rule, eras and regimes, house stances).
3. **Proposals** (`proposals/`): 300 files, each an ordered, executable set of edits for a later lane (exact files and symbols at the single owner, the order, the gate, the falsifier, the declared hash movers, the dependencies, what lands it, cost class and tier: `AUDIT_BRIEF.md`, last section). Every one is `PROPOSED`; 293 are live (a batch builds them), 7 are superseded.
4. **Unification** (`unified/`): Jordan's rulings, the owner and vocabulary ledgers, the conflict ledger, the single dependency order, the closure tables that give every audit finding one disposition, and the traceability and fact-check ledgers.

Its purpose is the input to workplan v12 (`STAGES.md` step 6): v12 takes the batches of `unified/U3_DEPENDENCY_ORDER.md` as its spine and adds what that file says it lacks.

## 2. Status vocabulary

Two vocabularies, never mixed.

- **A document's status class** (this index and `unified/U4_DOCUMENT_STATUS.md`): LIVE-PROPOSAL (a batch builds it; test 9 COMPLETE), INCOMPLETE-LIVE (a batch builds it; something in it is undecided, unwritten or content-owned), SUPERSEDED (named successor), REFERENCE-AUDIT (an audit, census list, closure table or conflict ledger whose findings are dispositioned), DIGEST, WORK-ORDER (deleted when its stage closes), and REFERENCE (the rulings record, glossary, owner ledgers, research notes; one class added to the six the work order named).
- **A finding's disposition** (`unified/U5_FINDINGS_CLOSURE_U5a.md` to `_U5d.md`, one row per finding): RESOLVED-BY (a proposal carries the exact edit and gate), SUPERSEDED, STALE / FALSE-POSITIVE, DISPUTED, JORDAN (two options, survives the ladder).
- **The `## Status:` line on a file** is the file's own word (PROPOSED, REFERENCE, RECORD, WORK ORDER, WORK LEDGER, WORK FILE, WORK LIST, SUPERSEDED by `X`). A `Status:` line does not make a mechanism (CLAUDE.md §0.05): done means the behaviour executes (§0.2), and nothing here executes.
- **Head lines** on a proposal: `Reconciled:` (what a unification or closure lane changed, with the ledger entry), `Folded:` (a later finding or ruling merged in, nothing deleted), `Grounded:` (an engine-grounding pass settled a mark against the tree).
- **Handles**: `B00` to `B41` are batches of `U3_DEPENDENCY_ORDER.md` (`B13` unused); a handle is one batch with one close.

## 3. Reading order

1. **The briefs** (suite root): `AUDIT_BRIEF.md` (the standing rules, including the charge that every recommendation carries instructions to code it), `STAGES.md` (the order of the remaining work and what it ends in), `UNIFICATION_BRIEF.md` (the nine tests and the closure rule), then the lane briefs as needed (`CENSUS_BRIEF.md`, `IMPLEMENTATION_BRIEF_A.md`, `INSTITUTIONS_BRIEF.md`, `PESSIMIST_BRIEF.md`, `VERBS_BRIEF.md`).
2. **The rulings A-1 to A-93**: `unified/DECISIONS_ANSWERED.md` (governing; A-93 is the last). Companions: `unified/DECISIONS_FOR_JORDAN.md`, `unified/DECISIONS_QUICKSHEET.md`, `unified/U1_JORDAN_CALLS.md`, `unified/U3_JORDAN_CALLS.md` (what still waits on Jordan).
3. **The unified ledgers**, in this order: `unified/UNIFICATION_RUN.md` (how the stage ran), `unified/U1_OWNERS_AND_VOCABULARY.md`, `unified/U1_GLOSSARY.md`, `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (owners, words, the one capability surface), `unified/U3_CONFLICT_LEDGER.md` (each contradiction and its decision), `unified/U3_DEPENDENCY_ORDER.md` (the landing order), `unified/U5_FINDINGS_CLOSURE_U5a.md` to `_U5d.md` with `unified/U5_CONFLICTS_U5a.md` and `_U5c.md` (every audit finding's disposition), `unified/OWED_TO_UNIFICATION.md` (what other lanes reported owed), `unified/U4_DOCUMENT_STATUS.md` (this lane's table and the test 9 census), `unified/U4_TRACEABILITY.md` (Jordan's stated intent traced to proposals; test 8) and `unified/U4_FACT_CHECK.md` (counts and findings that recur; test 6). The last two were written by sibling lanes at the same time as this index; this lane named them and did not read them.
4. **The proposals, by batch order**: `unified/U3_DEPENDENCY_ORDER.md` §1 lists each batch's members in landing order and §2.1 gives the batch table; the table in section 5 below counts them. File names begin with a number that is the producing lane (`01_CORE` to `31_WR`) or `U5a`–`U5d` (a closure lane's own proposals); the family is the second token. Read a proposal's head first (`Reconciled:` lines, the `Lands in batch:` and `Depends on:` lines), then its `Exact edits`, gate and falsifier.
5. **The audits, at heads and closure tables**: `audits/` (numbering: 01 to 13 subsystem audits with `_addendum_B`, 14 verbs, 15 institutions, 16 pessimist, 17 census, 18 determinism, 19 to 23 lacuna, narrative, procedural, happenings and story, 24 to 25 grounding, 26 to 31 the later lanes). Start with `audits/25_GROUNDING_ENGINE.md`: it settles what the suite claims about the engine.
6. **Digests, dossiers, census** only when a claim needs its evidence.

## 4. Directories

| directory | files | holds |
|---|---|---|
| `root` | 10 | the eight briefs and run plans |
| `proposals` | 300 | 300 proposals (PROPOSED); 7 superseded; 47 INCOMPLETE-LIVE |
| `audits` | 65 | the audits and addenda |
| `census` | 6 | six leads lists C1 to C6 (unreferenced symbols, record fields, registry keys, event kinds, stale hole-register pointers, unresolved composition targets) |
| `digests` | 51 | 51 coverage digests of repository areas (`DG_*`) |
| `dossiers` | 13 | 13 script-built per-subsystem dossiers, THE NINE, and a cross-cutting file |
| `unified` | 24 | the rulings, ledgers, closure tables, glossary, owed list, research maps, this lane's table and index |
| `unified/work` | 13 | read-lane outputs `R1_READ.md` to `R5_READ.md` and the wave-3 rewrite lanes' records `W3_*_DONE.md` (work files, deleted when the stage closes) |
| `..` | 15 | 15 research files the suite added under the repo's `research/` (grounding notes on game precedent and mass-battle history); the rest of `research/` predates the suite |

## 5. The batches (counts of live proposals per handle)

| handle | lane | wave | live proposals |
|---|---|---|---|
| B00-ids | IN | W0 | 0 |
| B01-laneA | IN | W1 | 1 |
| B02-tests | IN | W2 | 7 |
| B03-hygiene | IN | W3 | 12 |
| B04-capability-home | IN | W3 | 8 |
| B05-one-roll | IN | W4 | 16 |
| B06-keyed-draw | IN | W5 | 4 |
| B07-task-draw | IN | W6 | 4 |
| B08-scene-order | IN | W3 | 2 |
| B09-memory | IN | W7 | 9 |
| B10-character | IN | W8 | 17 |
| B11-fi-readers | FI | W9 | 13 |
| B12-world-motion-and-ground | SE+WR | W10 | 24 |
| B14-pc-outcome | PC | W5 | 5 |
| B15-pc-calibration | PC | W9 | 6 |
| B16-pc-round | PC | W10 | 2 |
| B17-mb-scale | MB | W6 | 4 |
| B18-pc-content | PC | W11 | 2 |
| B19-mb-field-calibration | MB | W10 | 11 |
| B20-mb-orders | MB | W11 | 4 |
| B21-fa-governance | FA | W9 | 15 |
| B22-mb-armies | MB | W12 | 7 |
| B23-land | FA | W13 | 4 |
| B24-sc-hearing | SC | W10 | 8 |
| B25-fi-questioning | FI | W11 | 5 |
| B26-fi-inquiry | FI | W12 | 6 |
| B27-sc-proceedings | SC | W11 | 6 |
| B28-social-verbs | SC | W12 | 5 |
| B29-pc-custody | PC | W11 | 0 |
| B30-mb-nested | MB | W12 | 1 |
| B31-mb-loadout-economy | MB | W12 | 3 |
| B32-inst-kit | FA | W12 | 10 |
| B33-inst-economy-hands | FA | W13 | 13 |
| B34-go-surface | GO | W11 | 4 |
| B35-wr-thread | WR | W13 | 4 |
| B36-wr-story-instruments | WR | W14 | 7 |
| B37-happenings | IN | W11 | 4 |
| B38-narrative-regimes | WR | W15 | 18 |
| B39-procgen-and-cases | WR | W16 | 11 |
| B40-inst-scenarios | FA | W17 | 9 |
| B41-go-port-gate | GO | W12 | 2 |

A proposal whose sections land in several batches is counted once, under the batch U3 §3.1 gives it; `U4_DOCUMENT_STATUS.md` shows its "+part" batches. B00 and B01 carry no proposal of their own (B01 is implementation lane A rebased).

## 6. Limits, stated honestly

- **Audits are read at heads, decision tables and the closure tables, not in full** (`unified/UNIFICATION_RUN.md`, "Limit, stated once"; the closure lanes read audits at decision tables and most proposals at head and runtime statement only, `unified/OWED_TO_UNIFICATION.md` §C). The unification stage guarantees a full reading only of the proposals (the read lanes R1 to R5), and `unified/U4_DOCUMENT_STATUS.md` §3.2 says what its own census opened.
- **Implementation lane A's code is unmerged.** Two commits, `e5d6ab9` and `c5bf18a`, on a local branch off `main` at `1424aa7`; not pushed. Jordan's A-93 lets the first code batch (B01) push its rebased branch; until it does, the suite reads `main`, and B01 renumbers its hole-register row (`unified/OWED_TO_UNIFICATION.md` §E; `unified/U3_DEPENDENCY_ORDER.md` §1 item 2).
- **About 210 `[UNVERIFIED]` lines remain from the engine-grounding lane**, in nine groups (`unified/OWED_TO_UNIFICATION.md` §C; `audits/25_GROUNDING_ENGINE.md` §5). They are claims about the engine that no lane opened; each is a first step for the batch that depends on it. The proposals themselves carry further `[UNVERIFIED]` marks with a fallback written (counted per file in `U4_DOCUMENT_STATUS.md`).
- **Audits 24 to 31 have no closure table of their own**, so the closure rule's "exactly one disposition per finding" was not checked for them (`U4_DOCUMENT_STATUS.md` §5).
- **Research is partly memory-grade**: mass-battle history rests on two fully read sources and does not establish pre-1700 foot pace, formation-change times, bout length, break threshold, dead-to-wounded ratio, desert and regroup proportion or second-weapon cost (`unified/OWED_TO_UNIFICATION.md` §C).
- **Nothing here executes.** CLAUDE.md §0.2: a juncture is done when the behaviour runs. The test 9 census is a reading of documents; the batches' gates are the first execution.
- **Layer 1 text and canon rewordings owed by Jordan's rulings are listed, not applied** (the list is in `unified/work/W3_MOPUP_DONE.md`, "Carried to the v12 stage").
- **Known stale lines in the ledgers** (carried, not fixed, because the order barred edits to those files): `U3_DEPENDENCY_ORDER.md` §1 items 4 and 11 (and §3.1) still say `06_FA_hygiene` has two declared movers and name `crisis_draw: off`, where the proposals now say none and `crisis_arm: rule`; `U5_FINDINGS_CLOSURE_U5a.md` still says `occupied` (`unified/work/W3_MOPUP_DONE.md`).

## 7. Where the v12 stage picks up

`STAGES.md` steps 3 to 7 follow unification: the holistic audit and codebase improvement proposal (3), the instruction suite (4), the evaluation of workplan v11 and the gap register (5, penultimate), the master suite and workplan v12 (6, final), and the agonist/antagonist write-up (7). Inputs the v12 author takes as given and adds to:

- `unified/U3_DEPENDENCY_ORDER.md` §1 (the ordered list), §2 (batch table, waves, lane schedule), §5 (the file census, with the serial edges) and §6 (tests and probes a gate names that the tree does not hold). That file says what v12 must still add: the requirement map, per-batch runtime estimates, context sets and `methodology-execute` boundary rows. It also records that positions of workplan v11 named as dependencies (CR-, CP-T-, IN-, B10- ids) are MISSING until step 5 dispositions them.
- `unified/U4_DOCUMENT_STATUS.md` §3.4: the INCOMPLETE-LIVE proposals, each with its missing part and owner (values that are Jordan's, names U1 has not decided, carriers no proposal writes). v12 does not accept an item that lacks instructions to code it (`STAGES.md`, standing constraints), so these are returned to their owners or carried as design-first items with the reason stated.
- `unified/U3_JORDAN_CALLS.md`, `unified/U1_JORDAN_CALLS.md` and `unified/DECISIONS_FOR_JORDAN.md`: what still waits on Jordan.
- `unified/work/W3_MOPUP_DONE.md`, "Carried to the v12 stage": the owed corrections to the U1 and U3 ledgers and the owed Layer 1 text.
- B00 (id allocation) first, then B01 (implementation lane A rebased), which is the precondition for the spine of B02 onward.

