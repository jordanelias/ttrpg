# SC — pessimist audit: NERS, premise and emergent narrative, of the social contest and proceedings

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `modules/social_contest/`, `systems/social_contest/`, the contest seam (`engine/season/seam/`),
the arrangements and venues, the proceedings verbs (`petition`, `carry`, `open_case`, `convene`, `speak`,
`determine`), the evidence-and-argument pipeline with fieldwork (`audits/19_LACUNA_investigation_to_proceedings.md`),
the obstacle as the task's difficulty plus all modifiers, and five premise sentences of a contest. The
SC lane's audits (`05_SC_audit.md`, `05_SC_audit_addendum_B.md`, `13_SC_contest_interrogation.md`) and
the LACUNA lane (`19_…`) are cited, not redone. Everything measured here is new work unless a lane is
named. All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_SC/`.

Short names: `es/` = `engine/season/`; `K/` = `systems/social_contest/sim/contest/` (the kernel the
loop does not run).

**PARTIAL FILE — written early and appended (PESSIMIST_BRIEF: "write early and append"). Sections
below this line are filled as the runs complete; a section that reads `[PENDING]` was not reached.**

## 0. Verdict

[PENDING — provisional, before the runs: the prior lanes establish that the live social contest is one
166-line roll under a correct seam, that every realm roll is pool 2 against obstacle 2, and that a
proceeding rarely closes. This lane tests the five premise sentences by execution.]

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the five sentences are the orchestrator's; the
boundary is the social-contest provider, its seam, and the proceedings verbs). **Contamination
declared:** the ordinary account O below was written after reading the SC lane's audits (which
describe the code) and `modules/social_contest/roll.py`, and before opening the seam, the effects, the
queries or the verb rows. No blind predictor was available to this lane (no `Agent` tool). O is
therefore written strictly from the words of each sentence; where a prediction leans on what a prior
audit said, the run decides, not the reading.

### 2.0 The ordinary account (O), written before the code was opened

**P1 — "A petitioner with a good case before a friendly bench usually wins."**

| # | link | O: what a player expects (a run could contradict it) |
|---|---|---|
| P1.1 | a petitioner petitions | anyone with a grievance may; the petition names what is asked and of whom; a trace exists |
| P1.2 | the petition comes before a bench | within about a season it is heard by a definite set of sitters; a petition nobody hears is visibly unheard |
| P1.3 | "a good case" | quality is a property of what the petitioner holds and cites (proofs, witnesses, the truth of the matter); ordered: more and better support, better odds; no support is worse than some |
| P1.4 | "a friendly bench" | the sitters' regard for the petitioner moves his odds; ordered: friendly > neutral > hostile; each sitter counts |
| P1.5 | "usually" | P(win) with a good case and a friendly bench is well above one half and below one; the 2×2 is ordered: good+friendly > good+hostile, bad+friendly > bad+hostile |
| P1.6 | "wins" | what he asked for is granted and the grant changes something he can point to; losing is a visible dismissal, not silence |
| P1.7 | bounds | a bench of one; no bench (no hearing, and he can tell); the petitioner sitting on his own bench is refused or recused |

**P2 — "A lie is caught more often by someone who knows the truth."**

| # | link | O |
|---|---|---|
| P2.1 | a liar says a falsehood to a hearer | the liar holds otherwise than he says; one act, with author, hearer and content |
| P2.2 | the hearer believes or catches it | two visibly different outcomes; a draw decides |
| P2.3 | "someone who knows the truth" | a hearer who holds the contradicting fact firsthand catches the lie materially more often than one who holds nothing; ordered: firsthand > hearsay > nothing |
| P2.4 | caught | the hearer does not take up the falsehood, knows he was lied to, thinks less of the liar, and can say so to others |
| P2.5 | not caught | the hearer now holds the falsehood and can act on it or pass it on |
| P2.6 | "more often" | never always, never never: a knowing hearer is sometimes fooled (he doubts himself), an ignorant one sometimes suspicious |
| P2.7 | neighbours and bounds | a skilled liar is caught less than a clumsy one; telling the truth to one who knows it is not "caught"; a lie about the hearer himself is the knowing case |

**P3 — "A hearing ends."**

| # | link | O |
|---|---|---|
| P3.1 | a hearing begins | a matter is put before sitters at a time and place |
| P3.2 | it is heard | the parties (or their advocates) speak, and what is said is part of the hearing |
| P3.3 | it is decided | the bench reaches a decision in bounded time: a season or two, not indefinitely |
| P3.4 | it ends | one of several named terminal states (granted, dismissed, convicted, acquitted); each is visible and distinguishable; ended-by-lapse is not the same word as ended-by-verdict |
| P3.5 | it stays ended | the same matter is not asked again of the same bench without something new (an appeal, new evidence) |
| P3.6 | bounds | the accused dies or leaves; the judge dies; no quorum; a hundred matters on one docket; each is an ending or a visible suspension, never a silent forever |

**P4 — "A verdict changes standing."**

| # | link | O |
|---|---|---|
| P4.1 | a verdict exists, about a person | it names who, by whom, on what matter, how firmly |
| P4.2 | "standing" | the person's position among others: what he may do (bound, detained, banned, owing), how he is regarded, what he holds |
| P4.3 | changes — against him | a conviction lowers it: a restriction others enforce or regard others hold |
| P4.4 | changes — for him | an acquittal clears him, and costs the accuser something |
| P4.5 | others learn and act on it | people who hear of the verdict treat him differently in at least one act they then take |
| P4.6 | proportion | a firmer verdict changes more than a narrow one |
| P4.7 | reversal | a pardon, a release or an appeal undoes it, visibly |

**P5 — "An NPC argues against an NPC and one of them is moved."**

| # | link | O |
|---|---|---|
| P5.1 | two NPCs who differ on something are together | the argument has a subject they hold differently |
| P5.2 | one argues, with no player | the decision layer offers it and someone takes it |
| P5.3 | the other resists | with his own skill and his own commitment to his position; a zealot is harder than a waverer |
| P5.4 | "one of them is moved" | either the hearer (the arguer prevails) or the arguer (he is answered and gives ground): in every decided argument somebody's position changes, and it is recorded whose and to what |
| P5.5 | being moved matters | the moved person later does something he would not otherwise have done |
| P5.6 | the reason is readable | the record says on what ground he was moved |
| P5.7 | bounds | arguing the same point again and again does not grind anyone down for free; arguing with oneself is refused |
