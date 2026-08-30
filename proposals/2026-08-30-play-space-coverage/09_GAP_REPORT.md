# The gap and weakness report

## Status: ADJUDICATION (2026-08-30) — Fable 5, over six season lanes, ~56 probes, 64 matrix cells.
## Reads: `00_PLAN.md` · `01_ROSTER_AND_FINDINGS.md` · `02`–`07` (the seasons) · `08_coverage_matrix.md`
## Two headline claims below were re-verified by hand against the season documents rather than taken
## from the matrix lane's summary. This session has a record of synthesis introducing errors (§7).

---

## 1. The headline result

**The design gives people plenty to do and cannot give them what they want.**

| verdict | n | |
|---|---|---|
| RICH | 33 | 60% |
| THIN | 16 | 29% |
| BLOCKED | 4 | Jarnstal · Palaiologina · Mertha · Falkenrath |
| SPLIT | 1 | Torsvald — rich as investigator, blocked as advocate |
| SPECTATOR | 1 | Torben |

Sixty percent RICH reads well. **The second count is the one that matters: 19 of 55 characters
(35%) have a BLOCKED CORE — live acts, and a stated goal or defining arc with no act whose object it
is. Eleven of those nineteen are verdicted RICH.**

A rich option set against an unreachable want is **the single most common result in the exercise**,
and it is not a balance problem. It is what happens when a design specifies *how* people act with
great care and never checks that the things they are canonically trying to do are reachable by any
act it defines.

Worked instances, each from a different lane: Inge Baralta has eleven live acts and none touches the
article her whole claim turns on. Queen Lenneth is the richest character in her lane and her stated
goal needs a verb she cannot reach. Maret Uln's agency in her own defining conflict is zero. Yrsa
Vossen has seven verbs and her season reduces to *speak, and hope*. Cardinal Jarnstal has no act
whose object exists at all.

---

## 2. What correlates with bad play — and the answer is not what the design assumes

**Rung, office and caste-exclusion all fail as predictors.** Office points slightly the *wrong* way:
32% bad among holders, 47% among the postless — but the highest office in the game is THIN, the Queen
with no office is RICH, and a parliamentary clerk outreaches the King.

Three things do predict, and all three are actionable:

1. **Mode count, and whether one act dominates.** Every RICH character cites three or more live modes
   or four differently-shaped acts; every THIN one names the act that dominates it. This is the
   plan's own R-check, and it is the only clean separator in the data. **Dominance, not scarcity, is
   what makes a season thin.**
2. **Among office-holders: an empty or unreachable *establishment*, never a small remit.** Almud has
   the largest remit in the game and the thinnest reach. Himlensendt's establishment is `none`.
   Tormann is RICH precisely because his is the one Cardinal seat canon fills. **The design prices
   remit and forgets establishment.**
3. **Among the postless: possession of a channel, a custody, a gate, or a unique root.** Everyone who
   holds one is RICH — Lenneth, Almstedt, Strand, Thale, Heljason, Stenskald, Uln, Vedel, Hann,
   Solberg. Everyone who holds none is THIN or worse — Torben, the control, Mertha, Aldith, Vossen,
   Edeyja.

Two sub-correlates hold at 100% within their class: **alignment = none** (5 of 5 bad) and **rank 1**
(4 of 4 bad).

**And Thread Sensitivity is non-monotone**, which nothing in the design anticipates: below 30 you
cannot hold the informal channel at all, and far above the rendering floor you hold content nobody
can receive. The Warden-Chief at the highest living TS and the control at TS 4 are both structurally
inaudible, for opposite reasons.

---

## 3. The gaps that are DESIGN DEFECTS — fix these

Ordered by how much play they cost.

**D-1 · The floor. The control is THIN, and for two mechanical reasons.**
*Ordinary capability is an empty verb set, not a smaller pool* — verbs gate on a practice at rank 3+,
so a person holding none gets no acts, rather than worse odds at the same acts. And `mark_salience`
= 1.0 makes an unmarked person **inaudible in both directions**: their acts do not propagate and news
does not seek them. **This is the most important defect in the report.** A political design that only
works for the marked, the officed and the aligned does not work.

**D-2 · Two incompatible act economies.** One act per season versus a ten-act worked season, with the
reconciliation explicitly forbidden. Reached independently by three lanes. It is worth the difference
between the King being THIN and RICH, so it is not cosmetic — it decides the answer to the exercise's
central question.

**D-3 · Two of four need terms have no formula.** `need(commitment)` and `need(exposure)` are
specified nowhere. For a magnate the other two return zero, so **100% of a duke's motivation is
uncomputed.** The design's signature claim is that needs are computed rather than authored; half the
computation does not exist.

**D-4 · Relational is empty at Settlement and Territory.** Two consecutive rungs with no admission,
no exclusion, no judging set, no Knot. The only membership operation at Settlement is `expel`, a
coercive act — **nobody can be taken in.** Confirmed by 56 probes across six lanes failing to fill
it, which makes it the best-evidenced cell in the matrix.

**D-5 · A councillor has nowhere to stand.** Inner councils and jarl councils appear in no venue
table, so they can neither contest nor argue. This is the most populous character type in Valoria.

**D-6 · Conferral is a cycle in the Church**, so `sovereign_fraction` is undefined over every Church
office. My audit posed conferral as person-rooted versus office-rooted; **neither branch resolves a
cycle**, and canon's answer (an off-map Holy See) is the suite's other open question. The two open
items are entangled, not independent.

**D-7 · The B-11 cost was mispriced.** Accepting that "the Dicastery decided" is inexpressible also
made it **unpetitionable** — a petition needs a respondent container and a cluster has no owning
node. That removes a whole direction of play against every institution, not just a turn of phrase.

**D-8 · Dominance defects the audit missed.** `confer` dominates for the Confessor because its
compounding cost is zero for an office with no establishment. The realm-scope decree is dominated for
the King. `tell` dominates for Vossen. Inspired avowal is priced nowhere, and inspiration is Vossen's
whole method.

**D-9 · Vacancy-by-absence is empty at every rung.** Prince Torben and a miller's widow's missing son
are the same hole, found by two lanes independently.

**D-10 · Material is empty for anyone holding nothing.** No wage, no coin, no sell-labour, no payment
between unrelated persons, no construction verb at any rung. A person with no holding has no material
mode at all.

---

## 4. The gaps that are CORRECT — do not "fix" these

An instrument that reports every hole as a defect is useless. Four are the design working.

- **Political-down and Institutional are empty for the postless.** That is what having no office
  *means*. Vossen's seven verbs against an office-holder's ten, with the five missing being exactly
  the five office verbs, is the cleanest confirmation in the exercise that "an office adds no verb"
  is true.
- **A struck institution is indistinguishable from a live one from the inside.** Every consumer reads
  persons; no decision function reads a registry. Jordan's Niflhel ruling and the design's faction
  model agree, independently — canon deleted a compression artefact, and the design says compression
  artefacts live in observers.
- **Several small overlapping economic factions work better than one guild would have.** As one body
  their disagreement would have had to be a stability number, which the substrate refuses. And the
  structure replicates unbidden inside the Restoration.
- **Off-board actors are served in proportion to scope-overlap, not distance.** That is the right
  shape; Laskaris being mute across the water is a consequence of scope, not a bug.

---

## 5. NOT THE DESIGN'S FAULT — roster and canon defects

Recorded so they are not miscounted as design gaps. **54 collisions were found, 43 new to this
exercise.** The ones that changed a season:

- **The suite borrowed two canon names and gave them incompatible lives** (Maret Uln, Gerik Strand).
  Still unfixed; renaming across the worked traces is a separate job.
- **Goldenfurt's province is contradicted** — Kronmark under the Crown, or Grauwald under Vaynard.
  Two lanes hit it independently. It re-points every Goldenfurt grievance trace at a different person.
- **Canon and the suite have two Dicasteries' functions swapped**, which changes what routing does.
- **Canon names no guild warden**, yet he holds the agenda, the Examination's convenership and its
  veto, and decides five economic seasons.
- **Stats are null for all five churchmen**, so the view budget is literally uncomputable for any of
  them. Many registry rows are thinner than the behaviour files behind them — Hann's fields are in
  the behaviour system and absent from the registry.
- **Niflhel's strike left stale text** in a faction document and the timeline, which generated a false
  contradiction until Jordan ruled.

---

## 6. Convergence — 22 findings reached by lanes that could not see each other

Independent rediscovery is the strongest signal this process produces. The largest:

| finding | lanes |
|---|---|
| **the claim that does not surface** — motivated reasoning burying the decisive claim | **6 of 6** |
| the TS ≥ 30 Knot gate closing on exactly the people who most need the channel | 5 |
| **the convener holds the cheapest real power in the game** | 5 |
| `care` zeroing the standing need at both ends of the ladder | 4 |
| rendering-side degradation on every path | 4 |
| the act-economy contradiction | 3 |
| vacancy-by-absence | 2 |

Two are recorded as **disagreements rather than convergence** — two lanes reached opposite verdicts on
Thale and on Realm × Relational — and one is a convergence-by-collision: one lane had a character
"simply buy" a verb another lane proved absent.

---

## 7. What I got wrong, and what that says about this process

Recorded here because the report would be dishonest without it, and because the pattern is more
instructive than any single error.

**Of seven audit dispositions, two were applied, then two, then three — each round found more.** I
reported all seven to Jordan as settled after the first round. Worse:

- **My audit cited an object that does not exist.** "The event-class parity list" appears only in my
  own audit document; a critic had written something else and I renamed it in synthesis to a phrase
  matching nothing in the suite.
- **A-6 was zero-applied, and I reported the wrong half as done.** The firsthand floor I ruled never
  reached the formula that owns salience.
- **A-4's reasoning was wrong in its consequence.** I kept the Knot TS gate on the argument that it is
  why the Restoration works. Both the Restoration's named leaders are below the gate.
- **A-1 needed a three-way distinction** — world / view / another agent's interior — and I drew a
  two-way one.
- **I cited Ehrenwall's oath as evidence for office-rooted conferral.** Her warrant reaches her under
  either branch; she does not bear the weight.

The defect class is constant: **a finding recorded as decided is not decided until it is applied, and
nothing checked application against record.** I am deliberately proposing no validator for it. This
repository has a documented pathology of answering process failures with apparatus, and the honest
response is to name the failure and stop.

---

## 8. What to do first

1. **Settle conferral** — and note it is now a three-way question, not two, because of the cycle.
2. **Reconcile the act economy.** It decides the answer to the exercise's central question and three
   lanes independently flagged it.
3. **Fix the floor (D-1).** Verb gating and mark salience, in that order. Nothing else in this report
   matters as much.
4. **Write the two missing need formulas (D-3).** Half the motive engine is absent.
5. **Sweep the blocked cores.** For each of the nineteen, either supply an act whose object is the
   character's stated want, or accept explicitly that the want is unreachable and say so in canon.
   **Do not leave it implicit — that is how a rich option set hides an unplayable character.**
