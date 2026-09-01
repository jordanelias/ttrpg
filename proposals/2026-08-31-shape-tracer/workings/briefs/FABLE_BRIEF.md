# COMPARATIVE ANALYSIS BRIEF — PR #350 against the 2026-06-28 archive

## THE QUESTION
> **Is the idealized code shape proposed in PR #350 missing anything, previously identified in
> `archives/audit/` and `designs/`, that still provides value now** — for NPCs, the world, factions,
> settlements and governance?

You are read-only by construction (no Write, no Edit, no Bash). Produce analysis, not edits.

## YOUR INPUTS

**1. PR #350 — the proposal under examination.** `/home/user/ttrpg/proposals/2026-08-31-unified-code-shape/`
17 numbered documents + `ADVERSARIAL.md`, `TRACE_REGISTER.md`. Merged 2026-08-31, **PROPOSED, HELD BACK
IN FULL, nothing ratified, nothing executes.** Orientation digest at `../PR350_DIGEST.md` — **the digest
is orientation only; verify against the primary documents before relying on any claim in it.**
Most relevant: `01_THROUGHLINE` (four laws), `02_ONTOLOGY` (types/fields), `03_OWNERSHIP` (who owns
every value), `04_THE_SEASON_LOOP`, `05_WORLD_CHURN`, `06_EMERGENT_NARRATIVE`,
`07_THE_PLAYER_AND_THE_PERSON`, `08_FUNCTION_SURFACE`, `15_ADJUDICATIONS` (rulings + what it overturns
+ what it escalates), `02` §10 (what it carries as open).

**2. The archive scrape.** `../lanes/LANE_*.md` — twelve structurally independent Sonnet lanes over the
frozen `v30-snapshot-2026-06-28` trees. Each carries FINDINGS (with `path:line` citations, status
markers and independent-rediscovery notes), DEAD ENDS (explicitly retracted material) and OPEN
QUESTIONS. The snapshot itself is readable at `../snapshot/{archives/audit,designs}/` if you need to
check a lane's citation — **do check the load-bearing ones; a lane can misread.**

**3. A Jordan ruling made today.** `../JORDAN_RULING_2026-08-31_SCENE_BUDGET.md` — the act budget is
**~5 playable scenes/actions per season, not 1.** PR #350 states one act per season, universally, in
bold, twice, as "the whole political economy". Treat the ruling as authoritative and the proposal as
wrong on this point.

**4. The live tree**, for the third disposition below. `/home/user/ttrpg/systems/`, `CURRENT.md`,
`references/module_contracts.yaml`, `audit/2026-07-05-emergent-narrative-engine/`. Note that a
narrative engine was RATIFIED 2026-07-05 and `systems/settlements/governance_play_redesign_v1.md`,
`systems/_architecture/governance_type_registry_v1.md` and `governance_ripple_substrate_v1.md` exist
live — some archive material may already have been carried forward.

## THE CENTRAL DISCIPLINE — THREE DISPOSITIONS, NOT TWO

For every archive finding that matters, decide which of these it is. **The third column is the
deliverable; the first two are what stops the deliverable being noise.**

| disposition | meaning | what to do |
|---|---|---|
| **COVERED** | PR #350 already provides it, possibly under a different name or by a better mechanism | say so in one line, name the section. **Do not report it as a gap.** |
| **SUPERSEDED** | the archive answer is worse, and PR #350's refusal of it is argued and correct | say so in one line. **A retracted or refuted archive claim is NEVER a gap** — the lanes' DEAD ENDS sections exist for this |
| **MISSING** | real, still-valuable, and PR #350 neither provides nor argues against it | **this is the finding.** Full treatment, below |

**And distinguish two kinds of MISSING**, because they cost differently:
- **MISSING-SILENT** — PR #350 does not mention it at all. The dangerous kind: the suite's own
  §16 admits **138 of 162 documents were never read**, so silence is not a decision.
- **MISSING-ARGUED** — PR #350 explicitly refuses or deletes it, and the archive shows the refusal
  costs more than the suite priced. This is the higher-value kind when it is real, and the easiest
  place to be wrong, so hold it to a higher bar.

## WHAT COUNTS AS VALUABLE — five kinds, roughly in descending order

1. **A MEASUREMENT or a CALIBRATED NUMBER** where PR #350 says it has none. The suite grades 11 of 25
   parameters ASSUMPTION and calls the `wear`:restoration ratio "a measurement, not a ruling, and
   nothing has been run". An archive figure that was actually simulated is worth more than any
   argument, **provided you check whether the archive number was measured or asserted.**
2. **A MECHANISM that closes something PR #350 carries as OPEN** (`02` §10 lists nine; `15` §3 lists
   four escalations). If the archive already answered one, that is a direct hit.
3. **A FAILURE MODE the archive found by running or by hard analysis** that PR #350's shape would
   reintroduce. Death spirals, degenerate win conditions, runaway exclusion loops, self-defeating
   victory conditions — the archive contains several found empirically.
4. **A GOVERNANCE MECHANIC with no counterpart in the shape.** PR #350 compresses governance to
   Office + Tenure + Proposition + Query. The archive holds detailed designs for occupation windows,
   treaty negotiation phases, parliamentary motion types, franchise, succession splits, fractional
   province ownership, crown claims. Ask per mechanic: **does the shape's ontology GENERATE it, or
   merely fail to forbid it?** Those are different answers and the distinction is the whole analysis.
5. **A STRUCTURAL INSIGHT** the shape would benefit from — especially an independent rediscovery,
   which the repo treats as its most bankable signal.

## HOW TO BE WRONG, AND HOW NOT TO BE

- **Do not credit the archive for having a document.** `CLAUDE.md` §0.05: prose is reference, code is
  mechanism. An archive design that was never built is not thereby superior to a proposal that was
  never built — both are prose. Value is in the CONTENT.
- **Do not resurrect a DEAD END.** Each lane names what was refuted and by what. Check before elevating.
- **Do not treat a rich mechanic as automatically worth keeping.** PR #350's meta-rule is *a fix that
  adds a system has failed*, and its N-line test — **name the emergent possibility lost if this is
  cut** — is the right test. Apply it to every archive mechanic you propose restoring. The suite found
  six FALSE N-lines this way; expect some archive mechanics to fail the same test.
- **Do not double-count.** The archive and the suite sometimes describe the same mechanism in different
  vocabulary (e.g. "Domain Echo" vs the seam; "derive Mandate from settlements" vs Law 3). Vocabulary
  difference is not a gap.
- **State your confidence and what would overturn each finding.** A finding without a falsifier is an
  opinion (`15`'s own standard).

## OUTPUT FORMAT
```
## FABLE LANE <ID> — <axis>

### VERDICT IN THREE SENTENCES

### PART 1 — MISSING (the deliverable), ranked by value
**M-<ID>-<n> — <title>**
- WHAT THE ARCHIVE HAS: substance + citation (lane finding id AND the underlying path:line)
- WHERE PR #350 STANDS: MISSING-SILENT or MISSING-ARGUED; if argued, quote the refusal and its section
- WHY IT STILL HAS VALUE: against the five kinds above
- ITS N-LINE: the emergent possibility lost if this stays out. If you cannot name one, say so and
  DOWNGRADE the finding — that is the test working
- COST TO ADOPT: does it add an object/system, or does it compose on what the shape already has?
- CONFIDENCE + FALSIFIER

### PART 2 — COVERED / SUPERSEDED (one line each)
So the reader can see what you considered and dismissed, and why.

### PART 3 — WHERE PR #350 IS AFFIRMATIVELY WRONG
Places the archive shows a proposal claim to be false, not merely incomplete. Cite both sides.

### PART 4 — THE SHARPEST THING YOU FOUND
One item, argued at length.
```
Density over breadth. Verify before asserting.
