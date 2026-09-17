<!-- STATUS: PROPOSED — held back. A design, not a ruling. -->
<!-- AUTHORITY: none claimed. Supersedes nothing. -->

# How a Valorian decides — the synthesis

## Status: PROPOSED — HELD BACK

> ⚠ **Superseded in part by ED-IN-0232 (the Key substrate retired).** Owner:
> `references/restructure_ledger.md#the-key-substrate-retired-2026-09-16-ed-in-0232`, with the
> ledger row in `registers/editorial_ledger_in.jsonl`. Four claims in this directory died with it;
> `behaviour_census.md` carries the list, and the affected sentences are corrected in place.


Companion to `behaviour_census.md` (what exists), `behaviour_algorithms.md` (three architectures),
`formal_analysis.md` (what the evidence establishes) and `adjudication_register.yaml` (the open
rulings). Those four **analyse**. This one **synthesises**: it is the mechanism, not a classification
of considerations about the mechanism.

**§0.05 class: REFERENCE — and correctly so.** Jordan, 2026-09-17: *"you can totally make design
docs in proposals… the issue was with outdated design docs being located beside code."* Clause 2
scopes to `systems/**/*.md` being read by tools. A design document in `proposals/`, read by people,
is the right shape for a design.

---

## §1 The three fusions

Analysis produced nine categories, five stages and four operators. Synthesis collapses them. Three
fusions do the work, and each one removes a distinction the analysis was maintaining for no reason.

### 1.1 Claims are not a category — they are the medium

The census filed **claims** as one thing a character holds, beside convictions and commitments. That
is wrong, and the mistake is structural rather than clerical.

**Every other term is computed over believed state, never world state.** Whether a candidate serves
an ambition, whether it fits a value, who it benefits, what it will cost — each is read off the
actor's own ledger. The engine already enforces this and says so:

- a `View` carries `holder`, `claim_ids`, `question`, and **raises `Forbidden` on anything else**;
- `opening_set` clause 4 filters on *known-false from the person's OWN claims*, not on truth, so
  *"a person who wrongly believes the granary full still forms the Candidate, acts, and gets
  `transfer.refused` from the fold"*;
- Jordan, 2026-09-02: *"our understanding of all other words and actions is subjective and singular."*

So claims are not a term in the decision. **They are the space the decision happens in.** And
susceptibility at intake sets its refractive index — how far each thing you were told bends what you
then compute. That is why the testimony ladder (lord > peer > enemy) is not a special rule about
gossip: it is the calibration of the entire medium.

**What the fusion buys.** `claims` stops being a row that competes with `convictions` for a place in
the score, and becomes the thing all the other rows are evaluated *in*. One less term, one more
invariant.

### 1.2 The two bases and the commitments are one machine, instantiated three times

|  | the vector a character holds | the table the world supplies |
|---|---|---|
| **moral values** | 13 weights, projected to axes | `alignment[axis][verb]` |
| **temperament** | 7 axes, held directly | its own verb table |
| **commitments** | pressure per standing item | `serves(candidate, item)` |

**The same shape three times: a held vector, dotted with a table keyed on the candidate.** Not three
mechanisms — one, parameterised three ways.

This is the fusion with the most consequence, because it changes what the outstanding work *is*:

- **One implementation, not three.** One sparse-table discipline, one declared default, one loader
  refusal on an all-zero matrix, one answer to "what happens when a column is empty".
- **It relocates the binding defect.** `alignment` is 52 of 152 cells — a third full — and the other
  two tables do not exist. The machine is sound; its data is absent. **That is why the axis-count
  debate was never the question.** Seven axes against an empty table is seven columns of zero.
- **It explains the projection asymmetry.** Moral values need a projection because thirteen weights
  must reduce to axes; temperament and commitments are held at the axis already. The projection is
  an *implementation detail of one instantiation*, not a property of the machine — which is exactly
  why R7 binds one instantiation and not the others.

### 1.3 Exactly one term carries a minus sign

```
For each candidate c the gates admit:

    pull(c)  =  Σ_k  press(k) · serves(c, k)      what I am trying to reach or avert
             +  Σ_a  hold[a] · fit(c, a)          what I take to be right     (both bases)
             +  regard(subject(c))                who it is being done to
             +  orient · benefits_me(c)           for whose good

    cost(c)  =  demand(c) · (1 − courage)         what it will take out of me

    score(c) =  pull(c) − cost(c)
```

Everything in `pull` is about what an act **achieves**. `cost` is the only thing about what it
**takes**. That is the whole reason courage is a modifier and not a weight, and the distinction is
not cosmetic in this engine: **Valoria resolves by drawing, so a term that moves the obstacle and a
term that moves the preference are different objects.** `cost` belongs on the Ob; `pull` belongs on
the pool. Under a purely additive score the two would collapse and the distinction would be
invisible — which is how prior work lost it.

**And the sign is what makes characters differ in kind rather than in degree.** An altruist has a
large `orient` term inside `pull`; a coward has a large `cost`. They are independent, so the same
person can be both — which is the character the earlier merge of fear-into-commitments would have
made inexpressible.

---

## §2 What the synthesis closes

Two of the four cells the analysis left open close by inspection once the fusions are made.

**`humble ↔ vain` is not two quantities sharing a name.** It is `regard` inverted, entering `pull`
through `regard(subject(c))` **when the subject is the actor themselves**. A vain character weights
acts that put him in front of witnesses; a humble one does not. No new term, no second stage — and
`standing_of` already computes the quantity it reads.

**`piety`'s stage is answerable rather than open.** If piety is a held vector over value-like things,
it is a **third instantiation of §1.2's machine** and sits inside `hold[a]` beside the other two. If
instead it gates what a devout character may attempt, it never reaches this function at all and lives
at the aperture. The question stops being *"where does piety go?"* and becomes *"is piety held, or
does it permit?"* — which is a question Jordan can answer in a sentence.

Two remain genuinely open and the synthesis does not pretend otherwise: whether `orient` belongs in
`pull` or at commitment (modulating what counts as a win rather than what gets chosen), and whether
profession is a gate or — per Jordan's own gloss, *"the kind of knowledge and possibly connections
they have"* — simply claims and regard under another name.

---

## §3 What it costs

The synthesis does not make the work smaller. It makes it **one kind of work instead of three**.

| | what is needed |
|---|---|
| **the tables** | `alignment` filled past a third; a temperament table authored; `serves` authored. Three tables, one discipline. |
| **the held vectors** | temperament on `Person`; `press` per commitment; `orient` the scalar; `courage`. All Person-interior, so all **one ruling** — STR-1. |
| **and one that is NOT that ruling** | ⚠ `benefits_me(c)` needs a **beneficiary per candidate**, and a `Candidate` carries only `(verb, subject, why, operands)`. This is a Candidate-schema problem, not a Person-interior write, so STR-1 does not cover it — and ED-IN-0232 made it **larger**, not smaller, by retiring the `beneficiary` role the register had called a bridge. Priced separately because the row above would otherwise imply orientation is already paid for. |
| **the medium** | the second-hand channel carries nothing today: 580 claims, 100% firsthand, `tell` resolving 9 times and depositing 0. Susceptibility has nothing to calibrate until that runs. |
| **the aperture** | 10 of 38 verbs unformable person-side. Every governance verb. The gates decide what the function is even offered. |

**And one number governs all of it.** `P(inversion) = 1/(1 + e^{Δ/τ})` at the shipped `τ = 0.1`: a
term changes what a character does at 95% only when it moves the score by **Δ ≥ 0.294**. Every term
above needs a declared range against that floor. A term that cannot clear it is decoration, however
well-motivated.

---

## §4 What would show this wrong

- **The one-machine claim (§1.2)** fails if any of the three needs a fundamentally different
  operation — if `serves` cannot be a table keyed on the candidate, for instance, because whether an
  act serves an ambition depends on world state rather than on the candidate alone.
- **The medium claim (§1.1)** fails if any term must read world state to be computed. Find one and
  claims are a term after all.
- **The single-minus-sign claim (§1.3)** fails if a second quantity turns out to be about cost rather
  than achievement. Fatigue would be one; so would risk of exposure, if exposure is a cost rather
  than a thing regard weighs.
- **The whole function** fails the moment any term's range is measured and found below 0.294 at the
  shipped temperature.

**Not claimed:** that the terms are complete, that the weights are right, or that this is the only
function consistent with the findings. It is the smallest one that holds all of them at once.
