# Institutions brief — author the design of how real political and religious institutions operate, adapted, commensurate, and expressed in play, with an implementation plan

## Status: WORK ORDER (Jordan's direction of 2026-11-12; not canon; resolves nothing until built and verified)

Jordan, in three messages: *"we will also need to properly author design based upon historical research how
the actual intricacies of our political and religious institutions operate eg Byzantine influence for
bureaucracy etc etc and implement plan"*; *"papacy and Rome, Venice and Medici era, Byzantine empire,
colonialism etc"*; *"all need to be adapted made commensurate expressed within play."*

## A fixed point from Jordan (2026-11-12)

*"Note that current kingdom royalty is because of nobility by deed/achievement, so it's something."*
In the world as it stands, a kingdom's royalty derives from nobility earned by deed and achievement, not from
a blood claim alone. Every institution design must reckon with this: how legitimacy and rank are won,
recognised, contested and lost by deed (what counts as a deed, who certifies it, what it costs to
claim it, how it passes or fails to pass to heirs, how a rival's deed unseats it), set against how the
historical institution handled birth, appointment, election, purchase and merit. Check what the tree
already says (`canon/`, the faction design set, `engine/season/offices.yaml`, the deeds and claims
machinery: `deeds_judged`, claims, the `Claim` ledger, succession `succeed`/`confer`) and extend it; do not
invent a parallel nobility system.

## What is asked

For each institution family assigned to you, from the historical research in the tree and any further
reading you can source honestly (the sourcing floor binds: shapes are the durable finding, specific
figures are leads; mark `[UNVERIFIED]` / memory-grade), author a design of **how the institution actually
works, in its intricacies**, then:

1. **Adapt** it to Valoria: the world (`canon/`; the Solmund canon; the Thread and the Mending; the
   factions and holdings that exist: `engine/season/offices.yaml`, `governance_spine.yaml`, `arrangements.yaml`,
   `rosters.yaml`, `npcs.yaml`, `data/affiliations.py`, `.designs/systems/factions/**`, the governance
   design documents), the nine requirements, the philosophy foundations P-01..P-15 (`valoria-canon-guard`
   skill; read `canon/`); name what you keep, what you change, and why.
2. **Make it commensurate**: expressed in the units the engine already uses, so that an institution's
   effects compose with every other mechanism rather than sitting beside it. One ladder of degrees, one pool
   and obstacle form (the obstacle is the task's difficulty plus all named modifiers), one set of scales
   (person, settlement, faction, realm), one clock/season cadence, one currency model; derived quantities
   from a single owner. A number you propose has a unit, an owner file and a sweep.
3. **Express it within play**: through verbs, seats, bodies, procedures, contests and venues that persons
   (player and NPC, through the one chooser) experience and use, and through consequences the world carries.
   For each piece of the institution: who acts, what verb, in which venue, with what roll and what
   modifiers (personality, affiliation, office, evidence, publicity), what is written, what other persons
   then read and decide differently because of it. No institution is a flavour text, a scripted event or a
   special-cased faction: it is built from persons in seats under procedures (CLAUDE.md scripting-drift
   rule; Layer 1's person-side rule). A fact the engine uses lives where code reads it (CLAUDE.md §0.05).
4. **Plan the implementation**: an ordered, gated plan against the present code: which registries and rows
   are added or changed (exact keys), which effects and predicates, which verbs gain behaviour (use the
   verb build-out lanes' proposals `proposals/14_VERBS_*` once present; do not redo them), what the
   playable scenario is (the standing playable-standalone requirement), the execution artifact that shows
   it works (a seeded run whose beats arise from persons' acts, with a control), the dependencies on other
   lanes, and the batches. Cost classes: edit / small build / design-first.

## For each institution, write

- **How it really worked** (sourced): structure, offices, procedures, sources of legitimacy and income,
  informal power (patronage, family networks, factions, ritual), how decisions were made and contested, how
  it decayed, how it was corrupted, how it projected power at distance, how it was resisted. The
  intricacies are the point: the actual mechanisms (for example sequences of clerks and seals and delays,
  election by lot and ballot, benefices and simony, credit networks, charters and monopolies), not a
  summary.
- **The play-facing model**: the primitives (seat, body, procedure, instrument/document, claim, obligation,
  patron-client edge, treasury/credit line, jurisdiction, sanction) and which exist already in the engine.
  Reuse first (CLAUDE.md §0: build bottom-up on the single-owner primitive; do not re-implement a rule that
  lives once). A new primitive needs the cut test (NERS: what dies without it).
- **Verbs and contests** it needs, mapped to the existing 67 verbs (`engine/season/verb_table.yaml`); a new
  verb only with the cut test and an entry shape as in `VERBS_BRIEF.md`.
- **Tuning dimensions**: venue, personality, affiliation, office, evidence, publicity, season (see the
  contest-interrogation lane's `audits/13_SC_contest_interrogation.md` when it exists; cite).
- **Emergent narrative it generates with no player**: the stories this institution produces by itself
  (schism, succession crisis, bureaucratic capture, banking collapse, interdict, colonial revolt), the
  conditions under which each arises, and the instrument that could show one happened and could fail.
- **Provided arcs and characters** that depend on it (`audits/12_ARCS_adjudication.md`).
- **Implementation plan** as above, and the decisions that survive to Jordan with two options.

## Limits and output

Authority as in `AUDIT_BRIEF.md` ("Authority granted"): you author and decide in proposal form; edit only
your own files; no commit; no pytest; no Bash edits of tracked files; no long `aperture` run. Read
`CLAUDE.md`, `AUDIT_BRIEF.md` in full, the FA lane's audit/addenda/proposals (`audits/06_FA_*`,
`proposals/06_FA_*`), the SC lane's, the SE lane's, the CHAR lane's NPC/chooser statement, and the digests
`digests/DG_*` for governance material (research, `.designs/systems/factions`, `.audit` governance entries).
Output: `audits/15_INSTITUTIONS_<FAMILY>.md` (the design and plan, verdict first) and proposals
`proposals/15_INSTITUTIONS_<FAMILY>_*.md` (the exact edits, in batches). Instrument output to
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/INST_<FAMILY>/`. Write early
and append. Receipt <= 200 words: files, institutions designed, primitives reused versus new, verbs
touched, the first playable scenario, decisions for Jordan.
