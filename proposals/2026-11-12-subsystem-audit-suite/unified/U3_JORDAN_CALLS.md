# U3 — what survives the ladder for Jordan: one design question and one permission

## Status: REFERENCE (a decision register for the suite, in the form of `unified/DECISIONS_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12 (HEAD `181548b`). Lane: U3 (conflicts and order), unification wave 2.

**What this is.** Every item the read lanes, the closure tables and implementation lane A left for you was run
through the five checks (superseded by a later ruling; irrelevant; settled by a design document or a ratified
Layer 1 row; settled by precedent; what the architecture clearly needs). One design question survives: it is a
place where your rulings and a ratified Layer 1 sentence point different ways and no reading satisfies both.
One permission is also yours, and is not a design call. Everything else is in the **Not yours** table, each
with the check that settled it, so you can see nothing was dropped and reverse any of them on a word.

**How to answer.** "J-U3-01: take 1" (or 2), and "P-1: yes" (or no).

---

### J-U3-01 · May what a man sees others do move what he believes, by a draw? · WR, CHAR

**What the game does today.** A person's stand on a question (his convictions) moves only through the crisis of
faith, which the suite has made a drawn, witnessed event that fires when his own deeds have scarred him against
his creed. Nothing else moves a stand. Persons learn of one another's deeds constantly (about 1,500 resolved
acts in two seasons) and of one another's opinions almost never (nine tellings between cast members in the same
run). Cohorts hold no convictions at all.

**Why it is yours.** You asked for momentum: Varfell "neutral leaning Einhir with momentum building for Einhir
Revival", the populace being what gathers, cohort convictions able to move, and a regime as an unsaid pressure
from those around a man. The proposal that carries this lets a man's stand lean, by a draw, toward the creed of
those whose deeds he approves and away from the creed of those he resents. The ratified code architecture says
two things against it, in so many words: **"WITNESS never touches a conviction"** and **"evidence cannot move a
conviction"**. The first can be honoured by moving the draw to the step where a person acts; the second cannot be
honoured by any reading that still lets what he has seen move his stand, because what he has seen is evidence.
Your rulings ask for the movement; the ratified sentence forbids its source. That is a choice between two games,
and the Layer 1 sentence changes only by your amendment.

**The question.** May what a man has seen and been told of others' deeds be a term in a drawn change of his own
convictions?

**Option 1 — yes, as a term in his own drawn act, nowhere else.** The lean is drawn at the step where persons
act (the same place the crisis of faith is drawn), from his own regard for the doers and his own present
stands; the step that deposits what he learns never writes a conviction. To play: a lukewarm man near a
vanguard he admires drifts toward its cause across seasons; a firm man barely moves; a man who rejects the
caste order is hard to win for the royal order that carries it; a movement can rise, stall or collapse by what
its people are seen to do. Cost: one sentence of the ratified architecture ("evidence cannot move a conviction")
is amended to read "evidence enters a conviction only as a term in the person's own drawn act, never as a direct
write", text drafted by the unification stage and applied by you; the drift is a declared change to every seeded
result once its dial leaves zero.

**Option 2 — no; stands move only by the crisis and by a man's own choices.** The ratified sentence stands as it
is. Momentum is carried by what does not touch a conviction: who believes whom (credit along regimes), the felt
pressure of one's circle on choices (not on stands), and the crisis of faith. To play: a movement's support is
visible in what people do and whom they credit, but a man's creed changes only when his own deeds break him; the
Revival "gathers" as allegiance and behaviour, not as converted belief, and cohorts still hold no convictions.
Cost: none to the architecture; the populace-gathers reading of your A-91 (3) is not met as a change of
conviction.

**Recommendation.** Option 1. Your A-89 and A-91 (3) name a change in the populace's stands, and Option 1 is the
narrowest wording that delivers it while keeping the rest of the ratified rule (no direct write, no clock, drawn).

**If you do not answer.** The suite builds Option 1's machinery at the step where persons act, with its dial at
zero (no stand moves; every seeded result unchanged); the dial stays at zero until you answer.

**What waits on it.** The Revival's gathering (`31_WR_B` commit 1); cohort convictions (CR-107, `31_WR_B` commit 2);
the regime readings that report a movement's growth.

**Sources.** `proposals/31_WR_B_the_revival_gathers.md` commit 1 and its Layer 1 note; `architecture/meta/04_CODE_ARCHITECTURE.md:250-251` (§B.2) and AX-3; `unified/DECISIONS_ANSWERED.md` A-24, A-83, A-89, A-91 (3); `unified/work/R3_READ.md:75`, `:407`; `unified/U3_CONFLICT_LEDGER.md` C3-L6.

---

### P-1 · Permission: push implementation lane A's branch (not a design call)

Implementation lane A's two commits (the duel chain reaches play; persons hold scores) sit on a local branch,
unpushed, as the lane was told. They were built on a base thirteen code commits older than the tree the suite
reads, and one of their register rows takes a number another row already holds. The order in
`U3_DEPENDENCY_ORDER.md` rebases them as its first code batch (B01), renumbers the row, and re-records their pins
on the current tree. **The question:** may that batch push the rebased branch and open its pull request? Until
you say so, B01 and everything after it waits. **Sources.** `unified/OWED_TO_UNIFICATION.md` §E;
`unified/U3_CONFLICT_LEDGER.md` C3-A1, C3-A2.

---

## Not yours (settled by the five checks; reversible on your word)

| question a lane raised for you | answer | what settled it |
|---|---|---|
| Does holding a seat buy extra scenes each season (the shipped office bonus)? | No: the bonus is removed; an office's reach grows by its establishment (clerks, paper-hands), rank speeds access (precedence) and modifies rolls | the ratified code architecture refuses an office bonus by name (`04` §A.3 row 15), later than the design that carried it; your A-12, A-13, A-64 (C3-L8) |
| May the Seat record gain patronage, eligibility and cooling-off fields and a fourth way of filling (`lot`)? | No new Seat fields: carried as data on the seat's arrangement rows; `lot` is a value of the filling roster | the ratified Seat record and your A-13's three facts (C3-L9) |
| Should some acts rank their candidates by what the act concerns (the addressed paper, the damning paper, the grievance)? | No new score term: the matter shapes which candidates are offered; regard and alignment rank them | the ratified choice score and your A-83 (pressure through existing channels, never a trigger) (C3-L10) |
| Do fled and injured men drift back by a new seasonal motion of the world, or by persons' acts? | Neither: the recovered share is computed when an army's strength is read, by a keyed draw on rest, supply and place; an act writes it in | precedent (forgetting computed when read; a term's lapse computed when read) (C3-L11) |
| After a won march, is seizure automatic or the victor's act? | His act (seize, occupy without seizing, or withdraw), taken in the same scene | your A-65 and A-66 ("their choice") (C3-L12) |
| How do seats pass with the land without a new kind of write? | The seats anchored on a holding name its holder as the one who may revoke them; the victor's seizure exercises that | the ratified write gate's complete list of bases (C3-L7) |
| May a person who appears in play (a birth, an arrival) be born with a full interior? | No: he is minted with the census's fields and grows his pursuits and knowledge by his own acts and what he witnesses | the ratified writer table; a newborn with few pursuits is the intended game (C3-L13) |
| May a task row declare a "stake" the loader expands? | Not needed: a row whose bands write different things already declares itself a contest with a task, which the architecture allows | precedent (the two shapes of a drawn act with nobody opposite) (C3-L14) |
| Is a roll's margin a real number (against the ratified integer margin)? | It is computed as one and stored as whole thousandths before the band is read; nothing in play changes | the ratified integer rule, kept true at no cost (C3-L1) |
| Does the float log survive "no recorder"? | No: the port is checked against the oracle by vectors, as the draws already are | the port gate's own replacement of the draw log (C3-L3) |
| May the player's screen read his own act's outcome from the world (a host-side receipt)? | No: the outcome reaches him as his own firsthand knowledge, which the screen reads | the ratified rule that the screen shows what the character holds (C3-L4) |
| The items the closure tables still mark for you (a refused act's receipt; the busy counterparty; luck in battle; one question or a list; named births; the parliament; the fight's obstacle, the nesting cap, who may raze, marching without a war; the four lane-29/30/31 items) | each answered by you | A-62, A-63, A-59/A-77, A-48, A-75, A-76, A-71/A-79, A-72, A-73, A-74, A-84 to A-86, A-91 (`U3_CONFLICT_LEDGER.md` §10) |
