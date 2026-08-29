# 15 — The Adjudication Register

## Status: PROPOSED (2026-08-29) — rulings made during the design, recorded so they can be attacked.
## Method: each lane was instructed to raise a CHALLENGE rather than silently diverge from the spine.
## This is what was raised and how it was decided. A challenge answered by "the spine wins" is not a
## win for the spine — three of the first seven went the other way and the spine was amended.

**Why this document exists.** A design written by many hands diverges silently unless divergence is
made expensive and disagreement is made cheap. Every lane was told: if the substrate strains under
what you need, say so in a marked section — do not quietly work around it. Seven challenges came
back. Four amended the spine. Recording the losers matters as much as the winners, because a
challenge that was rejected for a bad reason is the thing a later reader most needs to re-open.

---

## A. Challenges that AMENDED the spine

### A-1 · Needs must read the VIEW for the polity terms — ACCEPTED, spine amended
*Raised by 02 (the person).*

The substrate said needs are computed rather than stored, so "a person's wants change the instant the
world does." That is right for the body and **wrong for the polity**. Left standing it breaks T4
inside the needs function: a treaty would change the wants of every person in its scope before any of
them had heard of it — no lie, no telling, no channel, and the signature rule defeated by a helper.

**Ruling: split by source.** Subsistence and standing read the world (you feel hunger; their faces
are in front of you). Commitment and exposure read the view (you must believe the proposition unmet;
you must have heard of the decree, in whatever version reached you). The corrected claim is stronger
than the original: **needs are never stale relative to the person's view, and are supposed to be
stale relative to the world.**

*Why this is the most important ruling in the register:* it shows the signature rule can be defeated
by a function that never takes a `World` parameter, merely by reading one transitively. The type
discipline is necessary and not sufficient, and every derived quantity has to be audited for the same
leak.

### A-2 · The faction profile was a back door — ACCEPTED, spine amended
*Raised by the adversarial pass, not by a lane.*

The substrate computed a faction's presence/density/footprint by rolling up **actual** membership —
including the secret commitments it explicitly permits — and fed the result to perception and threat
assessment, which are decision inputs. That is a derivation of true state reaching a decision without
passing through `witness`: the substrate's own banned object, in aggregate form. Its N-line was false
too: a small faction being underestimated *emerges from* incomplete ledgers, and a true-state profile
makes underestimation harder rather than possible.

**Ruling: two profiles, one readable.** The **true profile** is readable by nobody — it exists for
bookkeeping and tests. Each observer holds an **estimated profile** built from their own claim
ledger. Covert membership is absent from an estimate until somebody's claim names it, so
underestimation becomes the default rather than a special case.

### A-3 · Individuation had no inverse — ACCEPTED, spine amended
*Raised by 02.*

Cohorts individuate into persons; nothing turned persons back. A long campaign therefore accumulates
persons monotonically — the unbounded-population failure, reached by a different route than the one
the design already refused.

**Ruling, adopted as stated because the formulation is better than the problem required:** a person
re-merges when they hold no Knot, no office, no live petition, and **no other person's ledger names
them**. That is: *a person persists exactly as long as somebody remembers them.* The survivors of a
hundred-year campaign are precisely the ones who mattered to someone, arrived at by reference-counting
the world's memory rather than by a cull or an authoring budget.

### A-4 · The Knot's Thread-Sensitivity gate is a deliberate caste asymmetry — ACCEPTED, spine amended
*Raised by 02.*

The substrate names the Knot as how a person with no post gets news — but the setting gates Knots on
TS ≥ 30, so roughly half the peninsula cannot form one.

**Ruling: keep the gate and state it, because the asymmetry is the design.** Every formal institution
gates Southern Einhir *out*; the deepest informal channel, being TS-gated and TS being
heritage-correlated, gates them *in*. That is why Niflhel recruits on the waterfront and why the
Restoration's weaving functions with no wealth and no soldiers. It is now written down specifically so
that a later reader does not "fix" the gate and delete the reason.

---

## B. Challenges DECIDED, spine unchanged

### B-1 · The admission parameter vector is container state — ALLOWED, as a stake
*Raised by 04 (hearth and community).*

04 holds `(α, β, γ, δ, aggregation_rule)` at the community, while the substrate's list of what a
container may hold is "stakes, judging sets and dates."

**Ruling: it is a stake, and the test is met on all three counts** — it is contested, it is allocated
at standing dates, and factions fight over it exactly as they fight over grain. Duke Magnus Vaynard's
entire anti-caste programme is, mechanically, a dispensation editing β for the guilds of Varfell.

The decisive evidence that the object is real rather than a filing convenience is what 04 found
falling out of it unbidden: **raising β changes nobody's stance**, so a committee that wants to
exclude routes the same exclusion through γ (no Free Master will sponsor him) and δ (personal dislike,
unfalsifiable). *A caste-breaking law is evadable through the terms it does not name.* A parameter that
generates that is not bookkeeping.

The proposed fallback — holding the vector on an office instead — is **rejected**, because the
caste-open institutions that matter most (a Restoration cell, a Niflhel recruiter) have no single
office-holder, and the fallback would make them inexpressible.

### B-2 · Standing is community-relative — ALLOWED, and it belongs to 04
*Raised by 04.*

Marks are a person's field; standing is not, and 04 needed one. Its derivation makes standing a
*reading* of marks under a particular community's admission rule, so the same man is Standing 3 in his
hamlet and Standing 0 across the wall.

**Ruling: correct, and the relativity is load-bearing rather than incidental.** A single global
standing number would make migration an escape from caste, which the setting explicitly denies —
marks travel and standing does not. Keep it derived; do not promote it to a stored field, or it
becomes a second copy of the marks that can disagree with them.

### B-3 · `mark_salience` gives marks a second effect — ALLOWED
*Raised by 04.*

Marks affect how an act is *judged* (through the judging set's reading) and, in 04, additionally how
far word of the act *travels*.

**Ruling: allowed, because the second effect is not a duplicate of the first.** Without it a house
name changes how you are judged but not how much you are talked about — and half the observable
behaviour of an aristocracy is the second thing. It also produces a real structural effect for free:
a marked person's charity propagates exactly as far as their transgression.

### B-4 · Per-hearth standing dates may not be standing dates at all — SPLIT
*Raised by 04, flagged rather than hidden, and the flag was correct.*

A seasonal larder reckoning on every hearth means the number of "standing dates" scales with the
number of hearths, which strains the substrate's account of a standing date as a *scheduled
contestable moment*.

**Ruling: they are two different things and the word was doing double duty.** A contestable moment is
one where a **prize is allocated among claimants** — the examination, the court's sitting, the tithe
reckoning, a vacancy, a truce's expiry. A larder reckoning allocates nothing and has no claimants; it
is bookkeeping, and it ticks **once per cohort**, with only an individuated hearth carrying its own.
The distinguishing test, which is now the rule: *if it has no claimants, it is not a standing date.*

---

## C. The orchestrator's own error, recorded because it is the most instructive one here

### C-1 · The architecture note contradicted the spine, and both were declared binding
Nine lanes were told to compose on the substrate **and** on an architecture note written by the
orchestrator. The note asserted that a faction's scale is "the smallest containment node spanning its
members" — the exact hypothesis the substrate rejects by name, and rejects correctly. It also said a
rung module "receives aggregates," which imports a per-tick push flow the design does not have and
would have re-created the stored aggregate state the whole architecture exists to abolish.

**Ruling: the spine wins on any conflict, and the note was corrected in place.** Aggregates are
computed on demand; a module may compute over its descendants when asked and may not receive pushes.

**Why it is recorded rather than quietly fixed:** the failure mode is specific and it will recur. An
orchestrator who writes a synthesis document *and* dispatches work against it has manufactured a
second source of truth, and the lanes cannot tell which one is wrong. The mitigation is not "be more
careful" — it is that **the spine is a file the lanes read and the orchestrator's notes are not
binding on anyone.** Any future note of this kind should say, in its own first line, that it loses
every conflict.

---

## D. Two decisions taken by the design that a prior process had escalated to Jordan

These are recorded because the earlier critique had marked them as needing a human ruling, and this
design decides them structurally instead. They should be re-opened if either decision is wrong; they
should not be re-opened merely because they were once escalated.

| question, as escalated | how the design answers it |
|---|---|
| **May a false belief ever determine an outcome outright, or only bias weighting inside a cap?** | It determines outcomes outright, and no cap exists, because there is nothing to cap: `choose(person, view)` never sees true state, so a belief is not a bias term added to a real value — it *is* the value the decision reads. Correction comes from collision with the world. The question dissolves rather than being answered. |
| **Is "community" a required rung?** | Answered by Jordan directly this session, and further than the question asked: community *and* family are first-class rungs. Recorded here only so a reader of the old escalation finds its disposition. |

The third escalated question — whether an off-board polity may act through an actorless world event —
is **not** decided here and is genuinely open. The design's answer would be that it may not, because
every agentive pressure must trace to a person; but the setting's Altonia and Schoenland exert real
pressure from off the map, and "generate a person to carry it" and "allow an actorless pressure" are
materially different games. That is a live design choice, not an oversight.
