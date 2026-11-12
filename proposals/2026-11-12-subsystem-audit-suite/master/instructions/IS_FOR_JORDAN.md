# Instruction suite — items for Jordan

## Status: REFERENCE (a decision register in the form of `unified/DECISIONS_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

**What this is.** `master/INSTRUCTION_SUITE_ORDER.md` asks each instruction lane to list here what survives
the five-step ladder (CLAUDE.md §0): what the game does today, one question, the options with how each
plays, a recommendation, and what the suite assumes meanwhile. One section per lane; a lane with nothing
to list adds nothing. Entries are `J-IS-<lane>-nn`.

---

## Lane IS-B2 (SC, FI, CORE, CHAR)

Read at `b07fc1c`. One entry. Everything else this lane met was answered by the ladder and is recorded in
`IS_B2_SC_FI_CORE_CHAR_part2.md` §4.1 ("Decided by the ladder"): a player-created person (closed: creating
is picking a seated person), the negotiation's opening verb (`covenant`), the default rite's burden map
(a data row, marked as an assumption).

### J-IS-B2-01 · Can a skill be lost? · CHAR (item `IS-B2-CHAR-04`; `unified/U4_TRACEABILITY.md` G-10)

**What the game does today.** A person's rank in a skill (the tree's `Person.capability`) only rises or
stays. The skill authoring architecture written this session keeps that: *"A capability is never lost (no
loss rule exists; adding one is a new growth rule, which is code and a decision)"*
(`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2). A wound or fatigue lowers what a person can do on
the day, as a level against the roll (A-8), and passes when he recovers; his rank is untouched.

**Why it is asked.** Your charge for the authoring surface lists what a definition must say: how a skill is
*"gained, lost, trained and opposed"* (`AUDIT_BRIEF.md:158-160`). Three of the four have a carrier. *Lost*
has none, and no ruling, precedent or design document in the tree settles whether you meant it as a rule
to build or as an example of what tabletop conventions cover.

**The question.** Should a skill a person stops using fall over time?

**Option A — no; a skill, once learned, stays (as now).** A veteran who has not fought for ten years fights
at his old rank; only wounds, age and illness (A-15) take from him, and they act on the roll, not on what
he knows. Simple to read on the sheet: a number that never goes down. Nothing to build.

**Option B — yes; a skill may lapse through disuse.** Each skill's definition row says whether it lapses.
For one that does, a person who has not used or trained it in a season draws once on his rank, on the one
keyed draw; most seasons nothing happens and sometimes the rank falls by one. The retired duellist is
rusty, the clerk who became a soldier forgets his law, and keeping a skill up becomes a reason to act
(a source of the worldly motion A-80 asks for). It costs a season-by-season draw per held skill, a number on
the sheet that can fall without a visible cause unless the account shows it, and one calibration (the
rate). Built as data: a closed sibling of `grows_by`, `lapses_by: [none, disuse]`, behind a rate that ships
at zero; a declared mover when the rate is raised.

**Recommendation.** A now. B is cheap to add later as one data column and one draw, and nothing built this
session forecloses it; adding it before the cast has authored skills (item `IS-B2-CHAR-03`) would be
calibrating a loss against ranks that do not yet exist.

**What the suite assumes meanwhile.** A: batch B04 lands `grows_by: [train, practice, use, fixed]` with no
lapse rule and no reserved column.
