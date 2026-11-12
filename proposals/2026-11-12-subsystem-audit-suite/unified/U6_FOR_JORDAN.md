# Decisions for Jordan raised by the U6 repairs — where a carrying proposal and a ruling's letter part

## Status: REFERENCE (a decision register for the suite, in the form of `DECISIONS_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: U6 repair lane R-C (finding 5 of `U6_VERDICT_AND_REPAIRS.md`, and its spot-check of rulings against their carrying proposals).

**What this is.** A ruling in `DECISIONS_ANSWERED.md` whose carrying proposal does not do what the ruling's words
say, where the repair lane could not edit the proposal to the ruling without breaking a ratified Layer 1 rule.
Each entry gives what the ruling says, what the proposal does and why, two options with what each feels like and
costs, a recommendation, and what the suite does if you say nothing. Everything the five-step ladder (CLAUDE.md
§0) could answer was edited in the proposal instead and is not listed here.

---

### J-U6-01 · A failed attempt on a guarded target: is the attacker always caught and detained? · PC, FI

**What you ruled (A-16).** *"gated by grievance plus hatred below a threshold, reaching a guarded target is a
draw, failure means caught and detained"*.

**What the proposal does.** On a Failure of the access draw the attacker's attack ends, it is witnessed (the
Event `fight.stopped`), and the guard, a person who now holds a claim of it, may form `capture` or `arrest` on
the attacker with his own choices, one act later. So the attacker is usually caught and detained, but not on
every Failure: the guard may choose something else, may not be there, or may fail his own draw.

**Why it does that.** In the ratified code architecture a seat is not an agent: an act is always a person's
act, formed by that person's own chooser (`04` PART D row 1, `Act.actor : PersonId`; PART D row 41, no decision
outside `choose`). The failed act is the attacker's own; nothing in it can write the attacker into custody, and
making the engine form the guard's act for him is a decision taken outside his choices.

**Option A — always caught and detained.** On a Failure the engine forms the guard's `capture` on the
attacker in the same encounter, without consulting the guard's own choices. *Feels like:* a failed assassin is
always taken; the rule is easy to predict. *Costs:* a Layer 1 amendment (an engine-formed act on a named
outcome, against PART D rows 1 and 41 and the "nothing fires" standing rule); one more exception the port
carries.

**Option B — caught and detained by the guard's own act (as the proposal stands).** *Feels like:* a failed
assassin is usually taken, and sometimes escapes because the guard was bribed, frightened, loyal to the
attacker or simply elsewhere, which is itself a story and a lead for an investigation. *Costs:* "caught" is
a likely result rather than a certain one; the proposal's gate must show it follows in most planted cases.

**Recommendation.** B. It keeps Layer 1 as it stands and keeps every outcome a person's choice and a draw,
which is the suite's standing rule; A-16's words are read as "a failure exposes the attacker to capture by the
guard", and the proposal's test `test_failure_emits_fight_stopped_and_writes_no_custody` already plants a
guard who then forms `capture` or `arrest`.

**If you do not answer.** B, as built.

**Blocks.** Nothing before batch B37; the answer changes one clause of
`proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (the Failure row) and, for A, one Layer 1
amendment row.

**Sources.** `DECISIONS_ANSWERED.md` A-16; `proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md`
(the Failure row and the paragraph under the band table); `U6_VERDICT_AND_REPAIRS.md` finding 5;
`unified/work/R5_READ.md` §1 (options (A) and (B)).
