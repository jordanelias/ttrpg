# LANE BRIEF — archival scrape for enduring design value (NPCs · world · factions · settlements · governance)

## WHERE THE FILES ARE
The two archived trees have been checked out of git tag `v30-snapshot-2026-06-28` into:

    /tmp/claude-0/-home-user-ttrpg/78360267-ece4-57b1-8568-be13abd76bad/scratchpad/snapshot/
        archives/audit/...
        designs/...

Read them with ordinary file tools. They are a **frozen 2026-06-28 snapshot**; both trees were later
dissolved (`designs/` retired 2026-07-19 into `systems/`; the audit corpus largely evacuated
2026-08-05). Nothing you read is live. That is the point: you are prospecting a graveyard for
design work that was done, was real, and may never have been carried forward.

## THE QUESTION YOU ARE ANSWERING
> What did this material establish, propose, discover or problematise — about **NPCs, the world,
> factions, settlements, and governance** — that still has design value today?

"Still has value" is not "was implemented" and not "was ratified". A sharply-stated *problem* that was
never solved has value. A mechanism that was designed, costed and then dropped for reasons that no
longer apply has value. A structural insight — "X must be derived, never stored", "Y and Z are the
same object" — has value independent of the doc that carried it.

## SCOPE — five subjects, and a hard exclusion
IN SCOPE: NPC modelling and behaviour · the world and its churn/geography/decay · factions, their
politics, stats and actions · settlements and territory · governance, offices, mandate, legitimacy,
succession, treaties, franchise, parliamentary/political process.

OUT OF SCOPE, and do not spend budget on it: personal combat mechanics, weapon/armour physics, mass
battle tactical resolution, social-contest tactical resolution, dice/pool arithmetic, UI chrome,
repository process/tooling/CI/audit-apparatus. **Exception:** include such material *only* where it
bears directly on one of the five subjects (e.g. how mass battle consumes a faction's military stat;
how a social contest writes back to an office's legitimacy). Report the seam, not the system.

## HOW TO WORK
- **Breadth first, then depth.** Index your assigned files, grep for the five subjects, then read the
  high-yield files properly. You will not read everything; say what you skipped and why.
- **Quote the substance, not a gloss.** "Defines settlement prosperity" is worthless. "Prosperity is
  recomputed each season as f(trade_access, unrest, garrison) and is explicitly NOT stored — the doc
  argues a stored value desynchronises from its inputs within two seasons" is the deliverable.
  Carry the actual rule, the actual formula, the actual structure, the actual number.
- **Cite `path:line` or `path` §section for every finding.** A finding without a citation is dropped.
- **Record status verbatim.** If a doc says `## Status: SUPERSEDED` or `[RETRACTED]` or `PROPOSED`,
  quote it. This corpus contains material that was explicitly withdrawn, and a downstream analyst
  resurrecting a retracted claim is the single worst outcome of this exercise.
- **Note independent rediscovery.** If two files in your lane that plainly did not read each other
  reach the same finding, say so and name both. That is the strongest signal available.
- **Do not read `/home/user/ttrpg/proposals/`.** A current proposal exists that this work will be
  compared against; your independence from it is the whole reason you are being run separately.
  Reading the live tree for orientation is fine; reading that directory is not.

## OUTPUT FORMAT — exactly this, no preamble
```
## LANE <ID> — <your lane name>

### COVERAGE
files_assigned: N | files_opened: N | files_read_closely: N
skipped: <what and why, one line each>

### FINDINGS   (8–25, ranked most valuable first)
**F-<ID>-<n> — <short title>**
- SOURCE: <path>:<line|§section>
- CATEGORY: ontology | mechanism | derivation | governance | settlement | faction | npc | world-churn | narrative | player-agency | seam | problem-only
- SUBSTANCE: 2–5 sentences carrying the actual content
- WHY IT MAY STILL MATTER: 1–2 sentences
- STATUS IN DOC: <verbatim status marker, or "none">
- REDISCOVERED IN: <other files in your lane that independently reach it, or "single source">

### DEAD ENDS
Material that looks valuable but is explicitly retracted, superseded or refuted *within these docs*.
Name it, cite it, say what killed it. Short entries.

### OPEN QUESTIONS NEVER ANSWERED
Decisions these docs flag as unresolved and that you find no resolution for in your lane. Cite each.
```
Aim for 1,500–3,000 words. Density over completeness. Your report is read by an analyst who cannot
see your files.
