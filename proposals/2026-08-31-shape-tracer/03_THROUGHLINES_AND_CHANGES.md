# THROUGHLINES AND REQUIRED CHANGES — what the two tests jointly demand

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## Every row here was produced by EXECUTION, not by reading. The probe that found it is named.

---

## §1 · THE THROUGHLINES OF a:NPC

Seven demands recur across 27 characters from a copyist to a King. Each is stated as the thing the
engine must be able to do, with the probe that found it failing.

| | throughline | probes | who needs it |
|---|---|---|---|
| **N1** | **A person must be able to MAKE a thing, and HOLD it.** A made object must outlive the scene, be carryable, hideable, seizable, destroyable — and merely holding it must be actionable against you | `P28` `P29` `P10` | Carin (a copy), Peder (a register), Joren (survey data), Dalla (goods she vetted) |
| **N2** | **A person must be CHANGED by what happens to them.** An outcome must be able to move what someone holds right, not only what they hold true | `P4` `P27` | Himlensendt's faith, Sæmund's unrecognised sense, Torben's formation |
| **N3** | **Something must accumulate that does not also decay.** A ratchet — a quantity that only climbs | `P26` `P18` `P23` | Edeyja's patience, the army's judgement of Almud, Baralta's pressed claim, Sigrid's covert risk |
| **N4** | **Not acting must be visible.** Deliberate restraint must be distinguishable from absence | `P19` | Almud's doubt, Vaynard's non-commitment, Baralta's held hammer |
| **N5** | **A person must be worn by WHERE THEY ARE**, not only by what they do; and must eat | `P31` `P16` | Orm's thirty-one years, every postless person |
| **N6** | **Office must COST as well as enable.** The same act by a King and a copyist must not be equally cheap | `P21` | Almud, and the whole question of whether high office is interesting |
| **N7** | **Standing must be audience-relative.** A reputation held among people who can never publicly credit you needs a carrier | `P33` | Sigrid, Kolbrun, every covert actor |

---

## §2 · THE THROUGHLINES OF b:ARCS

| | throughline | probes | evidence |
|---|---|---|---|
| **R1** | **An arc needs a DURABLE CONDITION on a thing that gates later acts** — a case that ripens, an army that is stuck, a copy half-made | `A16` `A18` `A9` `P30` | the single most frequent structural absence in the corpus |
| **R2** | **Most arcs end at a threshold with nobody deciding** — and Law 1 forbids it | `A2` | **8 of 20**, measured; two arcs name *"nobody decides"* in their own text |
| **R3** | **An arc needs ambient drift in a SOCIAL quantity** — a mood souring because no one tended it | `A13` | `ARC-01`'s entire engine |
| **R4** | **The deed must be separable from the doer** | `P3` | 4 arcs |
| **R5** | **A person must be able to stop being an agent**, one way only | `A19` | `ARC-09`: *"the arc exists because the rule has no exit"* |
| **R6** | **A reserve held must differ from a reserve absent** | `A15` | 3 arcs |

---

## §3 · WHERE THE TWO TESTS MEET

**They are not two lists. Four demands appear in both, and that convergence is the finding** — the
lanes producing them were blind to each other and to the shape.

| joint demand | a:NPC form | b:ARCS form |
|---|---|---|
| **a durable, held, staged thing** | N1 — Carin's copy, Peder's register | R1 — a ripening accusation, a stuck army |
| **restraint must emit** | N4 — Almud's invisible doubt | R6 — Baralta's held hammer |
| **a ratchet** | N3 — Edeyja's patience, the army's judgement | R2 — what a threshold-ending was *for* |
| **change without a decider** | N2 — a conviction moves | R3/R5 — Klapp changes, a practitioner crosses zero |

**The last row is the deep one.** a:NPC wants a person changed by what happened to them; b:ARCS wants
a mood, a body and a capacity to change with nobody choosing. **Both press on the same seam: Law 4
lets the world change MATTER with no decider and forbids it for anything social or personal.** That
asymmetry is correct for polities and wrong for weather-in-a-person.

---

## §4 · THE REQUIRED CHANGES

Ordered by probes unblocked. Each states what it costs in objects, because the shape's own meta-rule
is that **a fix which adds a system has failed.**

### C1 · MAKE `Record` A LIVE CARRIER — *unblocks 7 probes, adds no type*
`Record` already exists (`02` §7.4) as *"the only non-person root-bearer"*, keepable at a Rung,
burnable, admissible at a venue. It is inert. Give it what it already implies:
- **created by an act** (a `create`-mode StateChange whose subject is a Record) → `P28`
- **held by a person**, via a `hold` Tenure whose object is a Record → `P29`, `P10`, and `01` §3.1's
  *custody* finally has a carrier
- **`ttl` decremented at MATTER**, emitting expiry → `A9`
- **a `stage` that MATTER advances**, gating which acts are available → `A16`, `A18`, `P30`

> **N-line:** cut it and a copyist cannot make a copy, a clerk's custody is not power, an accusation
> cannot ripen while you do nothing, an army cannot be stuck, and no work takes longer than a season.

### C2 · GIVE THE MORAL LAYER ITS MOTION — *unblocks 2 probes, adds one counter*
A **per-Conviction scar counter**: interior primary state, written at WITNESS, monotone. Crisis fires
when any single Conviction crosses a threshold, and the crisis roll consults **only convictions the
person actually weights**.
> This is simultaneously **C3's ratchet**, and it fills write-matrix rows the suite owes regardless
> (`ADVERSARIAL.md` row 15). `02` §5.5 already promises the mechanism; this is its content.

### C3 · ADMIT ONE BOUNDED RATCHET — *unblocks 3 probes, adds no object if C2 lands*
Law 3 forbids stored **aggregates**. It should not forbid a **monotone per-person tally of things
that happened to you**. Scars, grudges borne, harms witnessed — these are not aggregates over other
people's state; they are a person's own history, and history does not un-happen.
> **This is a bounded, named amendment to Law 3, not its abandonment.** The bound: a ratchet may only
> count events in the holder's own ledger, and may never be a Query's substitute.

### C4 · MAKE ABSTENTION EMIT — *unblocks 2 probes, adds no type*
`choose` returning nothing produces an `abstain` Event naming what was declined. Restraint becomes
witnessable, and therefore chargeable.
> **N-line:** without it a King's sustained refusal to decide is indistinguishable from his absence,
> and a held reserve is indistinguishable from an empty hand.

### C5 · SPLIT THE DEED FROM THE DOER — *unblocks 1 probe, adds one field*
An Event carries what happened; **attribution is a separate per-witness claim.** Then witnessing an
act need not reveal its actor, and a false attribution is possible — which the epistemic layer
already wants.

### C6 · LET A PERSON CEASE TO BE AN AGENT — *unblocks 1 probe, adds one predicate*
DELIBERATE consults `may_choose(person)` before handing them the map. One-way crossings only.

### C7 · STANDING AS A QUERY OVER A NAMED AUDIENCE — *unblocks 1 probe, removes a scalar*
`Sensation.standing` is currently one global scalar — *what everyone reads off you*. Make it
`standing(person, audience)`. A covert reputation is then expressible, and the global reading is just
the audience `everyone`.

### C8 · MATTER TOUCHES PEOPLE, NOT ONLY PLACES — *unblocks 2 probes, adds no type*
A MATTER pass over persons contained at a Rung: draw subsistence from `stores`, take condition from
the Sites they stand beside. `02` §8.1 already says subsistence *"happens to you at MATTER"*; nothing
does it.

### C9 · THE AMBIENT-SOCIAL QUESTION — **ESCALATED, NOT PROPOSED**
Eight arcs and one whole character arc need a **social** quantity to drift with nobody deciding.
Law 4 forbids exactly this, correctly, because it is what stops a storm deposing a governor.
**Three options, and this test does not pick one:**
- **(a)** accept the cost: 8 arcs lose their engine, and the design says so out loud;
- **(b)** amend Law 4 to admit a narrow decider-free social drift — with a criterion, or the
  Partition's whole force evaporates;
- **(c)** re-express ambient drift as **many small acts** — the populace is cohorts, cohorts are
  persons at weight > 1, and a mood souring is people choosing differently. **This is the option
  most consistent with the shape's own laws, and it is the most expensive to run.**

> **This is a Jordan decision.** It is the one place where the tests demand something a law forbids
> and the substitute is not obviously cheaper than the loss.

---

## §5 · WHAT THE TESTS DO **NOT** ASK FOR

Stated because a change-list is judged by what it refuses.

- **No stored aggregate.** Every ratchet in C3 is a person's own history, never a sum over others.
- **No threshold that fires an outcome.** `A2`'s FORBIDDEN is the shape working; C4 makes *what
  people do about a crossing* legible instead.
- **No second resolver, no faction verb, no per-entity branch.** Nothing in 47 cases needed one.
- **No new guard, validator or checker.** The one apparatus this work licenses is the tracer itself,
  and it is load-bearing on the game rather than on this repository's process.

---

## §6 · WHAT ARRIVED AFTER THIS LIST WAS WRITTEN

C1–C9 above were drafted against **20 arcs**. The corpus then doubled to 50 and two independent
read-only passes ran over the result. **Three of the nine change materially, and one of them changes
because the list was aimed at the wrong target.** This section is kept separate rather than folded
in, so that what the list said before the evidence arrived stays legible.

### 6.1 · C9 is probably mis-framed — the corpus wants a SUMMONS, not a drift

C9 escalated a trilemma: accept the loss, amend Law 4, or re-express ambient drift as many small
acts. That framing assumed the corpus wants **a social quantity to change with nobody deciding**.
Measured across fifty arcs, it mostly does not.

| how the arc closes | n |
|---|---|
| a person chooses | 20 |
| a roll resolves it | 9 |
| never, by design | 10 |
| **a threshold fires with nobody deciding** | **8** |
| unclear | 3 |

**8 of 50, not 8 of 20.** But the same pass found **19 of 50 arcs are `forced_by_threshold: yes`** —
a counter crossing *forces the moment*, and then a person chooses. In the lanes' own words: *"the
patron is **forced** to choose publicly among defend/abandon/extract"*, *"the head of state's
**forced** choice is made (act, abdicate, or be replaced)"*, *"whose ceiling **issues a formal
ultimatum**"*, *"background cultural track bottoms out … **forcing** an Emergence crisis"*.

> **The corpus does not want the counter to ACT. It wants the counter to COMPEL SOMEONE TO ACT.**
> Law 1 forbids only the first.

So there is a **fourth option C9 did not list**: a crossing produces a **summons** — a thing at a
venue that a named person must now answer, whose refusal is itself witnessable by C4. The shape
already carries an unused `oblige` edge kind. The obstacle is real and must be cleared honestly:
`(Tenure, hold)` is `social: true`, so an Event may **not** write an obligation onto a person. The
candidate is that the crossing writes a **Record at a venue** — matter-side, `social: false` — which
the person's own `choose` then sees. **Whether that composes or merely launders a social write
through a matter object is exactly what the adversarial audit was asked to break**, and this
section does not assume the answer.

### 6.2 · C3 gains a constraint it did not have, and a much stronger evidence base

The new probe `P34` is the third-largest arc blocker (7 arcs). Five arcs independently want a
quantity that

1. climbs from the person's **own** ordinary acts, taken for ordinary reasons;
2. is **not readable by that person**;
3. **fires** on crossing.

C3 as drafted covers (1) and is silent on (2) and (3). Both additions matter: (2) is interior state
whose owner is not its reader, which is a genuinely new epistemic position in a suite built on
*nobody is omniscient*; (3) is `A2`'s forbidden threshold wearing a hat **unless the firing produces
somebody else's Act** — which is 6.1's summons again, arriving from the other direction. The two
findings are one finding.

### 6.3 · One genuinely missing primitive that no change on this list names

An independent clustering of the 95 unrouted `core` needs found roughly a third are restatements of
C1–C9 (**19 of them the `Record` alone**, which is the strongest possible confirmation that C1 is
aimed right) and about nine need no engine capability. Of the genuine remainder it identified
exactly one candidate primitive:

> **An ordered periodic settlement pass with capped, contested shared capacity.**

Raised independently by `ARC-R19` and `EMG-11`, and it is **`P35`'s hole seen from the other side**:
`resolve(Act[], World) -> Event[]` applies acts independently, so two people cannot contend for one
scarce thing in one season. A blocker cannot hold a line; helping one claimant cannot starve
another; a shortfall cannot produce a *pending* state. **Scarcity is what makes politics, and the
shape currently has none of it at the moment of resolution.**

This is the hardest item on the page, because the obvious fix — group acts by target inside
`resolve` — is a second resolver, and the shape's own meta-rule forbids that.

### 6.4 · Two clusters that look like demands and are not

Recorded because a change-list is judged by what it refuses, and both are large enough to be
tempting:

- **branching named outcomes (11 needs)** — arcs want a resolution to produce three or more
  categorically different named results. This is an **authoring convention over `Record`**, not a
  primitive. Nothing is missing.
- **a hidden per-person bias (9 needs)** — nine cases each want *this one NPC* to carry a private
  modifier. That is C3 plus a visibility rule, repeated nine times in different dress. Building a
  "hidden modifier system" for it would be **scripting drift with a registry.**

And one that is neither: the **political-escalation cluster (8 needs)** — forced dilemmas,
letter-versus-spirit compliance, cross-thread interruption — is **scene dramaturgy**. It is what a
designer does with the primitives, and no primitive is missing for it.
