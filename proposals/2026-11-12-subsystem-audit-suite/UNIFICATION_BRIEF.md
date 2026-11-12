# Unification brief — the suite is one whole, commensurate throughout, and compliant with the code architecture

## Status: WORK ORDER (Jordan's direction of 2026-11-12: *"ensure all documents in our suite are commensurate with each other, i.e. that we are a unified whole with code architecture compliance"*; not canon)

The suite was produced by many lanes working in parallel, each told to cite and not redo the others. That
yields overlap and contradiction: two homes for one table, six shapes for one player view, a duel round and
a mass-battle loadout that must share one rule, an evidence interface from two sides, a Layer 1 rule that
the stated intent appears to cross, clocks placed at the wrong step. The unification stage removes them. It
runs after the producing lanes (audits, addenda, verbs, institutions, implementation lane A) have finished,
and it edits the suite's own documents to make them agree. It changes no code and no canon.

## What "commensurate" and "unified" mean here, as tests

1. **One vocabulary.** A term means one thing across the suite and the tree: the same word for the same
   primitive (seat, body, claim, record, receipt, band, degree, faculty, capability, approach, venue,
   loadout, unit, subformation), no two names for one thing, no one name for two. The glossary is built
   from the tree's own owner (`references/descriptor_registry.yaml`, `names_index.yaml`, the Layer 1
   vocabulary: `architecture/VOCABULARY.md`) and the suite's usage; where the suite coined, it says so or
   uses the plain word (CLAUDE.md §4, word choice).
2. **One owner per fact.** Every number, roster, closed set and rule the suite proposes names its single
   owner file and key; no two proposals put one fact in two files (the known case: the capability
   definition home, `rosters.yaml` versus `descriptor_registry.yaml`); consumers read the owner.
3. **One unit and one scale.** Quantities that meet are commensurable: the same ladder of degrees, the
   same pool and obstacle form (obstacle = the task's difficulty plus all named modifiers), the same
   scale names (person, settlement, faction, realm), the same cadence (season, step), the same units for
   fatigue, speed, cost, regard, standing. A proposal that introduces a second ladder, unit or clock for a
   quantity an owner already has is a defect.
4. **One interface per edge.** Where two lanes meet (evidence between fieldwork and social contest; the
   duel round and the mass-battle field; the player view between lanes and the port; capability between
   dice, character and every consumer; campaign layer between governance, settlements and mass battle),
   there is one typed interface, named once, and each side cites it.
5. **One order.** All proposals sit in one dependency graph with one landing order and one gate per batch;
   no cycle; every dependency named in a proposal exists as a proposal or as code.
6. **No contradiction of fact.** Counts, measurements and findings agree wherever they recur, or the
   difference is explained (a different seed, a different head); a finding retracted in one document is not
   relied on in another; an old claim an audit shows false is marked.
7. **Layer 1 conformance, graded.** Every proposal is checked against `architecture/meta/04_CODE_ARCHITECTURE.md`
   (and, for modules, `architecture/holonic_ARCHITECTURE.md` §43 and §45–§47; `architecture/10_FACTIONS_AND_DEPLOYMENT.md`
   and the rest of Layer 1 where relevant) with the `skills/layer-conformance/SKILL.md` method (Lens B: grade
   each finding STRUCTURAL / MECHANICAL / CONVENTION per that document's §0, read both halves of a §A.2 row).
   A proposal that violates a Layer 1 row is rewritten to conform, or listed as a conflict between Jordan's
   stated intent and a ratified rule with the two options (as with auto-resolve and unit class); it is never
   resolved by editing Layer 1 (CLAUDE.md §0.05: a spec edited to match its implementation checks nothing).
8. **Stated intent honoured.** Each of Jordan's statements (the nine requirements, playable standalone and
   integrated, no dead ends, computed play must reach, personal combat and mass-battle intent, NPC/chooser
   intent, detective/noir precedent, institutions and the nobility-by-deed fixed points, capability
   authoring, verbs working) is traced through the suite to the proposals that carry it, and gaps are
   named.


## Closure rule and the extended authority (Jordan, 2026-11-12: *"Fable permission to resolve all issues/gaps/findings as required while ensuring commensurate"*)

Fable lanes may now **resolve every issue, gap and finding in the suite** as required, and must do so
**commensurately** (the eight tests above). Resolve means: decide it (five-step ladder), write or amend the
proposal that carries the exact edit at the single owner, and edit the suite documents that contradict the
decision. It is still proposal form for code, registries and canon (no lane edits code, canon, a registry or
a ruling; implementation lanes land proposals); a resolution that would overwrite ratified canon, a `(RULED)`
item or a ratified Layer 1 rule is written as a proposal AND listed with its two options for Jordan.

**Closure.** Every finding in every audit and addendum (`F-*`, `G-*`, `R-*`/resolution rows, census rows,
pessimist findings, happenings, determinism items, survivors) ends with exactly one disposition, recorded in
`unified/U5_FINDINGS_CLOSURE_<FAMILY>.md` (a table: finding id, one-line claim, disposition, carrying
proposal file and section, evidence): **RESOLVED-BY** (a proposal that carries the exact edit and gate),
**SUPERSEDED** (by a later finding or decision; cite), **STALE / FALSE-POSITIVE** (evidence at HEAD),
**DISPUTED** (your evidence; the finding stays, marked), or **JORDAN** (two options; survives the ladder).
A finding with no carrying proposal gets one written by the closing lane, so that nothing is left open
without a reason. Duplicates across lanes are merged under one decision and cross-referenced. Closure
families: U5a CORE, CHAR, DICE, tests, census; U5b PC, MB, verbs MILITARY/PHYSICAL; U5c SC, FI, LACUNA,
verbs SOCIAL/BINDING/MATERIAL; U5d FA, SE, WR, GO, institutions, ARCS, narrative, procedural, happenings,
determinism, pessimist (all scopes), story enablement.

## The unification lanes (each edits only the suite directory, never code or canon)

- **U1 Owners, vocabulary and the authoring surface.** The fact-to-owner ledger for every proposal; the
  suite glossary; the single capability/skill/ability/aptitude/trait authoring architecture (reconcile the
  CORE, DICE, CHAR, SC, FI, SE, WR, PC and MB capability proposals into one: one file, one schema, one
  reader interface; decide the home); the one player-view shape the GO lane needs. Output:
  `unified/U1_OWNERS_AND_VOCABULARY.md`, `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`,
  `unified/U1_GLOSSARY.md`.
- **U2 Layer 1 conformance matrix.** Every proposal, each of its edits, against Layer 1, graded. Output:
  `unified/U2_LAYER1_CONFORMANCE.md` (a table: proposal, edit, Layer 1 row, verdict, rewrite or conflict)
  and in-place rewrites of non-conforming proposals (note each rewrite at the proposal's head).
  Partition by proposal family across lanes (U2a PC/MB/DICE/GO, U2b SC/FI/CHAR/CORE/ARCS, U2c FA/SE/WR/
  verbs/institutions) and merge.
- **U3 Conflicts and order.** The cross-proposal conflict ledger (each contradiction: the documents, the
  claim, the decision, the ladder step, the edit made to the losing document) and the single dependency
  graph and landing order with batch gates, across every proposal and the implementation lanes. Output:
  `unified/U3_CONFLICT_LEDGER.md`, `unified/U3_DEPENDENCY_ORDER.md`.
- **U4 Index, traceability and consistency of fact.** The suite index and reading order
  (`README.md`), the intent-traceability matrix (item 8), the cross-document fact check (item 6), the
  list of retracted/stale claims, and a status table of every document (draft/complete/superseded). Output:
  `README.md`, `unified/U4_TRACEABILITY.md`, `unified/U4_FACT_CHECK.md`, `unified/U4_DOCUMENT_STATUS.md`.

After the unification lanes: the holistic audit and the codebase improvement proposal (organization,
centralization, efficiency, modularity), the instruction suite (the nine requirements and each subsystem
running well alone), and the agonist/antagonist write-up, each built on the unified documents.

## Rules for every unification lane

Read `CLAUDE.md`, `AUDIT_BRIEF.md` and `architecture/meta/04_CODE_ARCHITECTURE.md` first. Read every
document you are checking, in full: you are the second reader; sampling is a defect. Edit only files in
`proposals/2026-11-12-subsystem-audit-suite/`. When you rewrite a proposal to remove a contradiction, keep
its author's authorship line, add a `Reconciled:` line (what changed, why, which ledger entry), and never
delete another lane's finding; a finding you consider wrong is marked disputed with your evidence. No
commit; no pytest; no Bash edits of tracked files outside the suite. Write early and append. Receipt
(<= 200 words): files, contradictions found and resolved, conflicts left for Jordan with two options each,
documents you could not check.
