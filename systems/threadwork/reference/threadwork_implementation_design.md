# THREADWORK — IMPLEMENTATION DESIGN
## Status: PROPOSED
## Date: 2026-09-10
## Lane: WR · ED-WR-0010
## Authority: `canon/philosophy/RULINGS.md` governs wherever this document disagrees with it.

**What this is.** How threadwork resolves in the game, written after the philosophy rulings of
2026-09-07 and 2026-09-09 and against the *Valoria Unreality Suite* of 2026-09-06. It is
**reference** (§0.05): the code is the mechanism. What it is authoritative for is intent,
vocabulary, and the record of which decisions were taken and on what grounds.

**Citation convention.** A bare `§N.N` is a section of `canon/philosophy/` — the live
philosophical suite. This document's own sections are cited as `§N.N here`. The two numbering
schemes overlap and a cold reader cannot tell them apart without this line.

**What it replaces.** Nothing yet. `systems/threadwork/reference/threadwork_v30.md` remains the
head. This document says what its Part 3 has to become and why, and `CURRENT.md` is not moved
until that is ruled.

---

## 0. The verdict

**The rulings replaced the Coherence mechanism, and `systems/threadwork/sim/coherence.py`
implements the one they replaced.** `RULINGS.md` says so itself, in the plainest terms it uses
about code anywhere:

> Coherence is now a **distance** with a **stress-based yield point** … A track that depletes
> does not model that, so whatever implements it will need a different shape. Under §0.05 that
> is code's problem, not this suite's — but it follows from what was ruled.

Six clauses of the ruled model are absent from the live track, and the absences are not
refinements. There is one integer where the rulings require two quantities with different
remedies; recovery is unconditional where the rulings condition it on the environment; every
point comes back where the rulings say a permanent set never does; cost is keyed to scale alone
where the rulings make **direction** decide whether there is a cost at all; there is no
practitioner-side term where R-14 supplies one by name; and Coherence 0 un-sets when the integer
rises, where the rulings make the crossing a fact about a resting point that rest does not touch.

**And the same rulings settle three of the four questions the Unreality Suite ranked as
blocking** — Q-1, Q-4 and Q-11, leaving only Q-8, which is a commission rather than a question —
along with Q-7, which it had deferred. Two are settled in the direction the suite recommended,
on grounds it did not have. That is the salvage's shape: **the suite's instincts survive better
than its arithmetic.** Almost everything it priced is priced against the depleting track and
dies with it. Almost everything it *observed* stands, and several observations are now stronger
for having a canonical warrant instead of a contested empirical one.

Nothing here needs a ruling from Jordan. §7 records what was attacked to establish that.

---

## 1. The mechanism, specified

### 1.1 Two quantities, with different remedies

**This is the whole shape of the model** (§7.1), and everything else follows from keeping them
apart.

| | what it is | what moves it | what does not |
|---|---|---|---|
| **displacement** | present stress — how far current load has carried the configuration | time, rest, being mended, mending others | — |
| **resting point** | permanent set — the configuration a being holds once fully recovered | deliberate restorative threadwork aimed at the configuration carrying it | rest, however long |

A being's **position** is `resting_point + displacement`: the distance from the equilibrium
proper to being human as human. Coherence is that distance. It is **not a store that depletes**,
and the difference is not bookkeeping — a store makes the first operation as fraught as the
hundredth, which C-2 rules is the opposite of what the model is for.

> C-2, ruled: *"The idea of coherence loss is to prevent players/characters from spamming thread
> operations without penalty, so it's supposed to build up in increments or a big operation to
> discourage that player/character from doing it again without recuperation."*

That constrains the model from both sides at once, and both sides are load-bearing. **It must
bite** — displacement accumulates, and the accumulation is felt. **It must be answerable** —
recuperation is the designed response, so the model has to leave it genuinely available.

**Everyone has Coherence** (§4.3, ruled). Practitioners are distinguished by *spending* it, not
by having it — which is why drift propagates to family and community at all: they have the same
thing to lose. For someone who never operates and never stands near what exceeds, the variable
is simply quiet. **Architecturally that means lazy instantiation, not a practitioner registry**:
a being acquires a record the first time anything touches it, and the absence of a record is a
meaningful and cheap default rather than a gap.

### 1.2 Elastic, then plastic

> §7.1, ruled: *"A stress displaces the configuration. Below a threshold the displacement is
> elastic and the configuration returns. Above it, the configuration's own resting shape has
> moved, and no amount of rest brings it back."*

An event of magnitude `m` on a being whose current displacement is `d` and whose elastic range
is `R`:

- if `d + m ≤ R` — the whole of it is displacement. It returns.
- if `d + m > R` — the excess `(d + m) − R` moves the **resting point** outward by that amount,
  and displacement sits at `R`.

**Position is continuous through the yield.** The being is at `old position + m` the moment the
event resolves and settles back to the new resting point afterward. A model that reset
displacement at the yield would make the being *snap back* at the moment of their worst
experience, which is the opposite of what the section describes.

Four further rulings fix the model, and three of them close off a mechanism the materials
analogy would otherwise have supplied for free:

- **The elastic range is a constant of the being** (E-3). Permanent set relocates where rest
  sits without altering how far the being can be stretched from it and still return. **No work
  hardening and no embrittlement**: drift has no shape of its own — no accelerating slide, no
  hardened plateau ending in one catastrophic step. It is additive, and the tenth permanent set
  is the same kind of event as the first.
- **Only events deform** (E-4). A load held below the threshold leaves nothing behind, however
  long it is held. Living beside a Gap, inside a Warden zone or within a Locked Zone does not
  slowly reconfigure anyone. **There is no per-interval accrual term anywhere in this model**,
  and its absence is the design, not an omission.
- **Recovery is return over time, conditioned on the environment** (E-1). Time is the mechanism;
  **environmental equilibrium is the condition** — surroundings out of harmony give you nothing
  to return toward; mending accelerates without being required.
- **Sensitivity is independent of all of it.** Exposure teaches; stress deforms, and a
  practitioner can accumulate much of one with very little of the other.

⚠ **The asymmetry between the second and third is deliberate and §7.1 asks that it not be
smoothed.** Someone who lives beside a Gap takes no permanent set from living there, does not
heal there, and grows more sensitive for having been there. Nothing accumulates, nothing
returns, and perception sharpens. A "partial recovery in a bad place" term would be the obvious
kindness and it is exactly what the ruling excludes.

**Two consequences to build the interface around.** A veteran presents as further gone under
identical load and is *no more fragile*. And **a practitioner's history is exactly what tells you
how close they are**: the resting point *is* the tally.

### 1.3 Direction is the cost gate

Operations differ in their **direction relative to the futural-potential-legible** — whether the
resulting shape is one the configurations were tending toward anyway (§6.6). Three types, and
they are **categorically different, not points on one scale**:

| type | what it is | what it costs the practitioner |
|---|---|---|
| **restorative** | the result lies toward the equilibrium; once actualized it needs no holding | **negative** — it moves them toward their own equilibrium |
| **manipulative** | the result lies off the attractor; it stands only while held, and the holding is theirs | positive, for as long as the shape lasts |
| **destructive** | a configuration standing in harmony is removed or unmade | positive; the practitioner bears the severance, and the damage is not confined to the target |

**Restorative work does not merely cost nothing — it pays.** C-1 ruled this, and it is the single
largest change to how threadwork will feel to play. It needs no new mechanism: manipulation costs
because the practitioner is imbricated with a shape held against what its threads are oriented
toward, and the holding lives where the holder is; restoration holds nothing.

**Aim decides how deep it reaches.** Mending another moves the mender's *present displacement* —
the operation is aimed at the target, so the mender is drawn along rather than worked. Mending
**oneself**, or being mended by someone who aims at *you*, is what moves a **resting point**, and
C-1 names it: *"extremely difficult to do but possible."* *(The aim distinction is derived at
§6.8 and flagged there as derived; the ruling establishes that the floor is movable and names
self-mending as the hard case.)*

**Direction is a property of the operation's target, not of the verb.** §2.6 is explicit that
operations are distinguished by the practitioner's intended target configuration and never by
which dimension they move — foregrounding is impossible. So the seven v30 verbs stay as the
player-facing surface and **direction is computed per working from the target**, not looked up
from the verb's name. The same Weaving is restorative on a configuration oriented toward the
woven shape and manipulative on one that is not.

**And direction is a fact about the substrate, not about the practitioner's belief.** One who
misjudges it pays the rate the world charges, and nothing informs them in advance but diagnosis
and judgment. That is what makes tendency-reading the scarce asset rather than a convenience.

### 1.4 The practitioner-side term is resilience

> R-14, ruled 2026-09-09: *"the cost is their coherence, and their ability to prevent that cost
> stems from how resilient their spirit is, which is basically how strongly configured they are."*

Three things it is not, each of which the suite asserted at some point and each struck by R-14
by name: **not size** — how strongly a configuration coheres is what resists, and nothing here
is about how much of the weave one occupies; **not thread sensitivity** — reach and resilience
vary independently, and a great perceiver is not thereby hard to move; **not imbrication** — how
one is tied in determines what is *given* to one, not what one withstands.

**`Spirit` is the obvious candidate and the identity is mine, not the ruling's.** The v30 pool
is `(Spirit × 2) + History + Thread Pool Score`, and R-14 names *"how resilient their spirit
is"*. Reading the ruling's word as the sheet's stat costs no new axis and may be reading a
colloquial word as a technical one; it is a proposal, not a derivation.

⚠ **C-3 is retracted and everything derived from it is struck** — cost measured relative to the
practitioner's magnitude, *"there is no toughness term and there was never a place to put one"*,
magnitude-is-imbrication, *"sensitivity makes you better at doing and worse at being done to"*,
and the Einhir lattice as a larger vessel. R-14 says the opposite of the sentence in bold. Any
implementation that divides cost by a magnitude derived from reach has rebuilt the retraction.

The working's own contribution is unchanged: **type × scale** (D-5), with §6.6's direction test
deciding whether there is an operational cost at all. The practitioner-side term sits alongside
those, not in place of them.

### 1.5 The Leap: environment × duration

> D-5, ruled: **environment × duration, plus type × scale. Not inherent, not absent.**

During suspension the reflexive facing is not holding the configuration, so environmental
thread-forces act unresisted for the interval, and the configuration drifts in proportion to
`environmental force × duration`, less whatever the outward facing continues to hold. Then, at
or just after re-engagement, **knot feedback arrives**, weighted by operation type.

**Reconstitution fails when layer 2 cannot re-hold against the sum of the two** — which needs no
second roll, because that failure *is* the load exceeding the elastic range. One mechanism, not
two.

⚠ **Duration is a term inside an event and never across a life.** §7.1 rules that nothing
accumulates below the threshold, so time spent in a dangerous place with self-rendering intact
sums to nothing. What makes a Leap different is not that it is long but that it is *unresisted*:
the whole suspension is one load, and its length is that load's magnitude. **A practitioner is
not exposed for years. They are exposed for minutes, repeatedly.**

So *"is the Leap risky in itself?"* has no yes-or-no answer, and all four of the source suite's
contradictory claims come out true together. **The same Mending is free in a quiet place and is
not at a Gap margin — and nothing about the operation changed.**

### 1.6 What the bands read

The v30 band labels — Stable, Dissonant, Fragmented, Fractured, Severed — and their thresholds
stand. What changes is **what they read**.

**Every band reads present position, except the last.** Coherence failure is not a displacement
reading: it is the resting point having left the human band, and rest does not return anyone
from it. So a practitioner shows as Fragmented while a hard operation still has hold of them and
shows as Dissonant a month later, rested, without anything having been undone.

**A single observation therefore dates a practitioner's load, not their history.** Reading the
history means seeing where they *settle*. §7.4 states the instrument this gives a community, and
it is the right one to build the social layer on: **not the worst state a practitioner has been
seen in, but the best state they have been seen in lately.**

**Every band is written from the observer's side, and that is a consequence rather than a
stylistic choice** — what degrades is the capacity by which a being holds itself across time, so
the faculty that would register the degradation is the faculty degrading. §3.2 has the interface.

### 1.7 The crossing, and the four trajectories

Eventually the resting point leaves the band, and what has happened is not that the person was
damaged, emptied or reduced. **They became other.**

**Where irreversibility comes from — and it is not a floor that cannot move.** C-1 established
that a resting point *can* be brought back, and struck the editor's claim that nothing moves it.
What ends at the crossing is narrower and better: past the band, human is no longer where that
configuration tends, so working it back toward human is **restoring a remembered state**, which
§6.6's knife-edge makes *manipulation*. Before the crossing, bringing someone back is Mending;
after it, the identical-looking act is the one thing the discipline forbids. **Nothing about the
difficulty changed at the threshold. What changed is which operation it is.**

**So the interface must reclassify rather than refuse.** A mending aimed at a crossed being does
not fail and is not blocked — it resolves as manipulative, at manipulative rate, with
manipulative consequences. That is the setting's structural tragedy made mechanical, and §7.1
says why it will keep happening: *someone will always try to bring a crossed being back to who
they were, because that is precisely what love asks for, and it is precisely the remembered
state.*

**What follows is gated by reach at the moment of permanent loss** — not reach before, and not
any reach acquired after (§7.6). The gate does not re-open: a drifted being may go on being
exposed and go on gaining reach, and it will not thereby come to comprehend what happened to it.
And it gates **comprehension**, not only capability: a being of shallow reach does not merely
lack power, it lacks any grasp of what has happened to it and cannot form one.

| reach at the crossing | trajectory | what it is |
|---|---|---|
| below Relational | **freefall** | No capacity to threadwork oneself at the depth lost self-rendering required. The environment writes itself into them because nothing resists it. Consciousness persists. **This is not transcendence and it must not play as it.** |
| Relational | **persistence through others** | Identity becomes relational rather than personal. Their knots are structurally load-bearing — the relationships are holding the being together — and if one severs, part of what holds them goes with it |
| Structural | **reconstitution** | Self-maintenance is deliberate and continuous: functionally what a threadcut being does, except still spooled. Every moment is an operation and every operation strains the substrate |
| Foundational | **reconstitution and strain** | Comprehensive, self-consistent and enormously capable — and every moment involves threadwork at a depth that strains the substrate the way the Einhir lattice did, for self-maintenance. Benign in intention, catastrophic in structural effect |

**The breakpoints are already canonical mechanism.** They are `operations.DEPTH_TS_MINIMUM`'s —
the same four thresholds that gate what a practitioner can *operate on* gate what they *become*.
Nothing has to be invented here, and nothing should be.

**The endpoint is not one state.** It is a reach-gated set of structurally distinct trajectories,
and the distinction is structural rather than moral or narrative. None is a punishment and none
is a reward.

### 1.8 Reality-strain

> §7.5: strain is *"the summed difference, across everything affected, between what is held and
> where the configurations tend."*

A shape held off the attractor draws the fabric taut. Sustained long enough and deep enough it
produces the conditions the Calamity produced: anchor points strain, the fabric tears, and
incursions and gaps occur in the strained vicinity. **This is not a moral fact and not an
indictment** — such a being may be entirely benign in intention; the strain follows from what
they must do to continue existing.

**A being past the band, maintaining itself, is the limiting case rather than a separate
phenomenon.** Its layer 2 is gone, so there is nothing to absorb the load into its own
configuration; its self-maintenance is manipulative by definition, held against everything
around it, continuously. Solmund is the worked example, and the setting's central warning was
being demonstrated continuously for a generation in the one place nobody thought to look.

⚠ **One reading here is mine and it should be attacked first.** §7.5 flags an unresolved posit:
whether a manipulative operation's load is *split* — part absorbed as Coherence loss, part left
in the substrate — or whether all of it lands on the practitioner until Coherence 0 and strain
appears only there. **Both horns assume one quantity being divided, and the definitional sentence
above has no division in it.** A held shape *is* a difference from where the configurations tend;
the practitioner's Coherence cost is a *separate* consequence of holding, arriving through the
imbrication. Two consequences of one act, not two shares of one load. On that reading strain
accrues from any held manipulative shape, and the Coherence-0 case is the limit §7.5 says it is.

**Reject it and §7.5's ruled text survives untouched with its posit still open.** I take it
because §7.5's own definition is more specific than its opening argument, and because it is what
keeps the strategic loop in §3.3 here.

### 1.9 Others' holding, and why isolation is dangerous

The outward facing has two components, and distinguishing them settles several things at once
(§4.3): a **disposition** — renderability-as-human, a property of the configuration itself,
determinate whether or not anyone is present — and an **occurrent holding**, the actual
renderings other people are performing, which by §4.2 are threadwork *on* the practitioner and
genuinely hold their configuration.

So a practitioner alone has a determinate Coherence, and is held by layer 2 alone, without the
supplementary hold of others. **Other things equal, the isolated drift faster.** Communal life is
structurally protective, not merely comforting.

**Holding is not returning, and the distinction is load-bearing.** E-1 ruled that others
contribute to recovery by **mending** — threadwork — never by rendering. Both hold: rendering is
a process and can *resist*; what draws a displaced configuration back is time in surroundings at
equilibrium. **A community protects by holding and by mending, and those are two different things
it does.** In mechanism: witnesses damp an incoming load; they do not heal one.

### 1.10 What this changes in the live code, precisely

Stated at the granularity a later session can act on without re-deriving any of it.

| site | change |
|---|---|
| `systems/threadwork/sim/coherence.py` | `CoherenceState` gains the two quantities, the elastic range and the resilience term. `coherence` and `band` become **derived views** — the 0–10 integer is a projection of position, inverted and clamped, so every published threshold constant and `tools/export_game_constants.py` are untouched. A negative delta becomes a stress event; a positive delta becomes recovery, stopping at the resting point rather than at 10 |
| same | `check_coherence_zero_transition` stops un-setting. The crossing is a resting-point fact; "crisis resolves when coherence rises again" is the superseded model |
| same | new entry points the delta path cannot express: direction + scale + resilience for a working; environment × duration for a Leap; environment-conditioned rest; mending with an aim; the crossing, recording reach |
| `systems/threadwork/sim/operations.py` | `COHERENCE_COST_BY_SCALE` survives **as the manipulative column**, not as the whole model. `_resolve_operation` takes a direction rather than inferring cost from the verb. ED-871's Mending exemption stops being an exception and becomes an instance of the rule |
| `world.practitioners` | keeps its name and its snapshot contract. Renaming it is a cross-lane schema change, and the name is only inaccurate about *who* has Coherence |
| snapshots | an old one carries a single integer and cannot distinguish a floor from a load. Reconstruct conservatively; the superseded track licenses no claim either way |

**One hazard worth naming before anyone starts.** The projection makes the legacy integer a
**read-only view** — precisely §0.1 pt 1's read/write asymmetry, where writers become silent
no-ops. And `displacement` must never exceed the elastic range, or the next event reads the
overflow as fresh permanent set and converts it.

**None of the numbers above are invented, and one is derived.** The band thresholds, the scale
weights and the reach breakpoints are the v30 design's, re-homed. The **elastic range** is
derived from §7.1's own worked sentence — *"a practitioner resting at Dissonant, pushed as far
as their range allows, arrives deeper into Fractured than a novice resting at Stable pushed
exactly as far"* — which a range of roughly four band-steps satisfies exactly and a smaller one
does not reach.

---

## 2. Salvage ledger — the Unreality Suite, 2026-09-06

Eleven documents reading the framework against the literature on derealization, the uncanny, the
surreal and hallucination. Written against the **five source documents**, three days before the
reorganization and the rulings. Not canon, and it never claimed to be.

**The pattern is the finding.** What the suite *observed* almost all survives. What it *priced*
almost all dies, because it is priced against a depleting track. And three of its six amendments
are now settled by ruling — two adopted in substance on better grounds than it had, one struck by
the very principle it cited.

**Verdicts.** **ADOPT** — as written. **ADOPT, CORRECTED** — the observation stands, the reasoning
or framing must change. **SUPERSEDED** — a ruling has since decided it. **DISCARD** — it does not
survive, for a canonical reason rather than a preference.

### 2.1 The ledger

| # | Item | Verdict | Why |
|---|---|---|---|
| **05 §5** | Coherence computed on the **observer's** side; no Coherence number shown to its owner, ever | **ADOPT**, and it gains a mechanism | §4.3's asymmetry of self-judgment grounds it: the self-presentation that is failing is what would be needed to perceive the failure. And the outward facing's *occurrent holding* raises it from a display rule to a **force** — witnesses damp an incoming load, and the isolated drift faster (§1.9 here). Two observers genuinely perceiving a third differently is not a bug |
| **01 §4, 02 A-1, 05 §2** | Drift rendered as **inconsistency between channels**, never as deviance toward a human norm | **ADOPT, CORRECTED** — keep the mechanism, drop the dependence on the contested evidence | §7.2's drift phenomenology *is* cross-channel disagreement — shadow against posture, presence against body, response against ordering — and §4.5 rules threadcut uncanniness "radically singular and alien", irreducibility and **"not a mirror"**, which is not a category-boundary account either. P-04 and P-10 forbid the deviance framing outright. The mechanism is now canon-native and needs no appeal to MacDorman |
| **05 §1** | **Insight never helps.** No dispel verb, no truesight, no see-through-the-illusion perk | **ADOPT** | §5.6 as re-ruled is sharper than the version the suite had: the knowledge "is not erased. It is **inert**: correct, repeatable, and unable to do any work." P-08's violation test forbids study-based access explicitly |
| **05 §7** | Two histories, **no reconcile path**: an immutable record of what was experienced beside a causal graph the world edits; orphans lose their parent and decay faster | **ADOPT, CORRECTED** — the framing must change, the structure survives | §2.7 rules disjunction **local and witnessed**: "nobody holds a true inner record against a changed public one." So this is not a private truth against a public lie — it is *what was pulled* out of step with *what was not*, and anyone not pulled can see it. §4.7 supplies the decay's reason: temporal depth is accumulated spooling, and removing the causal history removes it. The absence of a reconcile button is exactly right |
| **01 C-9, 05 §10, 03 WR-1** | **Felt presence** — wrapping as a relation with one end; an agent with no mesh that occupies the audio graph, is targeted by gaze solvers, pushes crowd flow, and is never revealed | **ADOPT** | §6.4 defines wrapping as frayed edges entangling with an entity — structurally a relation with one end — and the canon warrant stands alone without the clinical literature. "Never reveal it. There is no reveal to withhold" is the correct instruction |
| **03 §8, §11; 09 §7.1; 10 §4.1** | **Diagnosis returns structure and never content**, on a reach-banded ladder | **ADOPT** | P-09 is unchanged, and §6.7 rules that a pulled memory "does not vanish: it becomes an orphaned configuration" that a skilled diagnostician can detect. *Operations are provable; their contents are not* is the sentence to build the investigative layer on. The ladder's thresholds are the v30 TS bands |
| **10 §4.2** | Orphan signatures are legible to **non-sensitives**: authority that fails to register, a habit whose cause is missing, an institution routing around a functioning part | **ADOPT** | Follows from §4.7 plus P-08: the *effects* are ordinary facts about the world, and only the *reading* of them requires reach. This is what keeps a non-sensitive protagonist from being helpless, and it is the suite's best single piece of applied design |
| **10 §4.3, §1.4** | Honest irreconcilable witnesses are a **lead, not a dead end** — agreement on inventory with disagreement on sequence | **ADOPT** | §2.7's "they are not misremembering" makes this the correct forensic reading, and a legal system that defaults to *one of you is lying* has discarded its evidence. Note the empirical prop (ordering fails before inventory) is decoration; §2.7 carries it alone |
| **05 §13, 09 §8.8, 06 §3.2** | The **strategic loop**: threadwork → substrate tension → incursions → Accord drop → mandatory faction action → spent action economy | **ADOPT, CORRECTED** — see §2.2 below | §7.5 supplies the formula's shape and a better warrant than the suite had. The arithmetic dies with the track; the loop does not |
| **05 §14** | Four endgames keyed to reach, entered by continuing to play, with different verb sets | **ADOPT** — and it is now *ruled*, not extrapolated | §7.6's four reach-gated trajectories map to it one-for-one, and the breakpoints are `DEPTH_TS_MINIMUM`'s. The suite's own warning — freefall "is not transcendence, and it must not play like it" — is §7.6's word for word |
| **05 §0** | One perception function, no separate truth and perception paths | **ADOPT, CORRECTED** — delete the third internal term | It serves P-03 well, and §3.5's positional constitution supports it: what is given to a being follows from how it is imbricated. The `immersive_orientation` term was gated on A-4, which is now struck (below), so the gate fires: delete it, and `expectation` absorbs its role |
| **05 §12** | The **Leap made felt**: the player's own body model becomes visible, agency arrives mediated, and a failed reconstitution permanently desynchronizes one channel *as others compute it* | **ADOPT, CORRECTED** | §6.2 improves the presentation: the Leap "changes the *as*; it does not lift a veil", which is what opacification reads as. Correct the cost — a failed reconstitution is a **permanent set**, not a cosmetic flag |
| **02 A-6** | The practitioner's self-report is structurally **as-if** | **ADOPT** | §4.3's asymmetry grounds it without needing the clinical vocabulary. Register-level, no mechanics, and it pairs exactly with "no Coherence number, ever" |
| **02 A-2** | **Vastness** as a parameter separating awe from dread | **ADOPT, CORRECTED** — it is a *reading*, not a property of the encounter | §5.3 rules the signature **structurally identical** whenever the active stratum is exceeded, and §8.8 rules that the Church "reads this signature in the inverted register", naming the encounter itself as the vector. So valence is an institutionally and culturally formed reading of an invariant signature — which is stronger than the suite's version and needs no appeal to Keltner & Haidt. §5.5's caution binds: **equanimity does not reduce the encounter; it makes continuing possible** |
| **09 §12.5** | The **safety trap** — a society that succeeds at civil defence reduces its own practitioner supply, so it is either dangerous and capable or safe and declining | **ADOPT** | Follows from §5.4 unchanged: sensitivity develops through genuine confrontation, which concentrates where incursions and Locked Zones are. The suite's own bias note says it did not test this hard; the mechanism is canon and the consequence is real |
| **09 §4.4, §15** | **Sparsity**: build the network, do not knot the network; density caps; no generational accumulation at fixed sites | **ADOPT** | §8.1's ruled account is *precisely* this — "a configuration held only by a balance has nowhere to fall back to when the balance goes" — and §8.4's cascade runs through knots regardless of what tore them. The Einhir test is a good design instrument and survives its own document |
| **02 A-5** | **Configuration Damage** as a separate subject-side track | **SUPERSEDED — the problem is real, the solution is unnecessary** | §6.7 now rules that a manipulative operation imposes a shape the target's own layer 2 opposes, so **the target bears Coherence cost too**; and §4.3 rules that **everyone has Coherence**. The damage records on the same quantity, which also dissolves the naming collision the suite flagged as its own blocker |
| **02 A-4** | **Immersive Orientation** as a third practitioner axis | **SUPERSEDED — the slot was right, the occupant is dead** | The suite drafted it and recommended against ratifying, because its warrant was a construct whose measurement was formally disputed. R-14 has since supplied a third term with an author's ruling behind it: **resilience — how strongly configured they are**. Take the slot, discard the candidate. And note R-14 strikes *sensitivity* as the answer by name, which is what A-4 was reaching for |
| **02 A-3** | **Loosening** as a fourth named operation | **DISCARD**, and the reason is the suite's own citation | A-3's whole rationale is that "the intelligibility dimension has no operation aimed at it — an asymmetry the Inseparability Principle does not require." §2.6 rules that operations are distinguished **not by which dimension they primarily move — that is impossible — but by the practitioner's intended target configuration.** A verb minted to give a dimension its own operation is foregrounding, which is the one thing P-01 exists to forbid. The suite marked it `[EXTRAPOLATED]`; it should stay extrapolated and unbuilt |
| **03 §2** | The dimensional-signature table's **"Primary aim"** column, naming a dimension per operation | **DISCARD the column; keep the rows** | Same reason. What each operation *moves in all three dimensions* is good, useful and correct. What it "aims at" is not a dimension — it is a target configuration |
| **03 §3** | The Coherence cost schedule: `base(scale) + hold_intervals if opposed, 0 if aligned` | **DISCARD** | Arithmetic on a store. Three separate clauses fail: aligned work is not free but *restorative* and pays; there is no third column for destructive; and there is no practitioner-side term. The **scale weights** survive as §1.3's manipulative column |
| **06 §4, 09 §0.1** | The doctrine — "aligned operations cost nothing; the scarce asset is the reading of tendency" | **SUPERSEDED in shape, retained in conclusion** | Tendency-reading is still the scarce asset, and that survives intact. But the economy is not free-versus-expensive: it is **restores you / displaces you / severs you**, and a career of restorative work is not merely cheap, it is how a practitioner recovers. That inverts what a Warden's life looks like from the inside |
| **09 §0.2, §0.4** | The **alignment asymmetry** — "the substrate is tending toward decay in far more configurations than toward restoration", so threadwork suits war better than peace | **DISCARD** | Both of its readings quote formulations the rulings now forbid. See §3.3 |
| **06, 09, 10** | Every Coherence figure in the catalogues — "2 Coherence", "37 over nine years", the worked season's `6 → 3` | **DISCARD as arithmetic; keep as scenarios** | All of it prices a depleting track. The *situations* are excellent and should be re-priced: the knotted commander who cannot be relieved, the register the archive mended in good faith and thereby killed, the fleet the survey saved, the regiment nobody can billet |
| **10 §3.5** | A mob beats a threadcut being where a champion cannot — distributed simultaneous demands exceed a finite maintenance rate | **ADOPT, CORRECTED** — the finding stands, the reasoning needs §4.5's | The suite rested it on one clause of P-06 and flagged that as thin. §4.5 is the load-bearing version: **being configured is itself the work**, and only spooling yields the depth that makes a configuration cheaper to be — so the rate is finite *and never eases* |
| **05 §11** | Locked Zones as an unstructured field recombining the player's own recent perceptual history | **ADOPT, CORRECTED** — good presentation, wrong diagnosis | §8.5 rules a Locked Zone a place where **becoming has been precluded** — a substrate-side fact — and strikes the epistemic restatement the suite inherited ("the rendering cannot present what exists") by name. What is right is that **nothing accumulates there**, and that is what the presentation should carry |
| **05 §8** | Word alienation as a playable procedure — thirty repetitions, then the string re-renders | **ADOPT** as texture, **DISCARD** as a model of the barrier | §5.6 rules the barrier **inertness, not amnesia**, and P-08's corrected test fails any mechanic that makes non-sensitives *forget*. A decay curve that greys out a dialogue option is the wrong side of that line; the ritual itself is fine |
| **09 §14** | The institution list — Tendency Survey, Tension Register, Knot Registry, Working-Site Model, Assay, Attestation, Apprenticeship, Coherence Rota | **ADOPT** | Each follows from canon the rulings left standing, and the absences are the sharp part: **no academy, no published corpus, no non-sensitive regulator, no ministry that can be briefed** — all four forbidden by P-08 |
| **01 C-6** | Confrontation → sensitivity has no analogue in the literature and the nearest datum runs the other way | **ADOPT the disposition** | The suite's handling is right and should not be revisited: this is the framework's **principal act of invention**, a fictional premise rather than a defect, and not to be argued for from evidence. §5.5's account of what develops makes it a design claim, not a psychological one |

---

## 3. Gameplay, and where threadwork surfaces in the other subsystems

### 3.1 The loop at personal scale

The crossing already exists in code: `engine/cross_scale/handoff_rules.py` gives
Personal → Thread on a successful Leap, with contact duration starting on that round. §6.1 says
what that crossing *is*, and it is stronger than a scale change — **the Leap is not a technique
that happens to be required for operations; it is the crossing that makes an act an operation at
all.** An operation is threadwork that requires going beyond oneself as a finite ordinary human;
layer 2 is what holds one within that shape; so operating requires suspending it.

A working, in order:

1. **Read the tendency.** Free, and see §4.1 here. This is where the player's real decision is made,
   because it is the only thing that tells them which direction their intended result lies in.
2. **Choose the target configuration.** Not "which dimension" — that choice does not exist. The
   direction falls out of the target's relation to the equilibrium, and the player can be wrong.
3. **Leap.** The unresisted interval begins, and its load is `environment × duration`. In a place
   whose configurations stand in harmony this is nothing, however long it runs.
4. **Operate.** `type × scale ÷ resilience`, with type deciding whether there is a cost at all.
5. **Re-engage.** Knot feedback arrives, weighted by type.
6. **Reconstitution.** No separate roll: either the sum stayed inside the elastic range and the
   configuration returns, or it did not and the excess is a permanent set. *(§9.2 wants the
   "retention roll" renamed anyway. Under this model there is nothing left to name.)*

**The Leap window is the assassination window, and the counter costs nothing.** Layer 2 is
suspended and the practitioner is locatable but visibly *off*. The cheapest counter-threadwork
capability a faction can field is an ordinary soldier told what to look for — which is why
serious operations are prepared off-site, and why threadwork is a strategic instrument here
rather than a tactical one.

### 3.2 What the player sees, and what they never see

**Never a Coherence number.** §4.3: the apperceptive self-presentation that is failing is the
same one that would be needed to perceive the failure. A practitioner cannot fully judge their
own Coherence, so a meter that shows it to its owner contradicts the mechanic it is displaying.

What the player gets instead is **other people**, and this is the design, not a compromise.
Others register it first, through the labour of trying to apprehend a drifting person as a
unified human subject. Two observers describe the same practitioner differently — not in opinion,
in what they perceived — and neither is mistaken, because rendering is positional (§3.5). The
player learns their own drift the way the fiction says they must: from a shopkeeper who stops
meeting their eye.

**And the community's instrument is the one to surface: not the worst state a practitioner has
been seen in, but the best state they have been seen in lately.** That reads the resting point,
which is the tally, and it is legible to everyone including them, in the quiet after.

**Drift is rendered as inconsistency between channels and never as deviance.** Features that do
not agree with each other — a shadow that does not match a posture, a presence occupying more
space than a body, a response that addresses what was meant rather than what was said. Never
features that fail to match a human norm. This is simultaneously what §7.2 describes and the only
ethically defensible way to render a mechanic that scores how readably human a person appears.

### 3.3 The strategic loop, and where it already has a home

**Threadwork raises substrate tension in the province; tension produces incursions; incursions
drop Accord; low Accord forces the local faction into mandatory military or governing response;
mandatory actions consume slots before anything else is scheduled.** A benign, competent,
powerful practitioner destabilizes the region by existing, and the simulation makes that
something the player watches happen on a map rather than something a document asserts.

**The home for it is `systems/threadwork/sim/rendering.py`, which is a wired stub.**
`apply_rs_strain` and `check_calamity_threshold` are declared and unimplemented; the world clocks
they would feed — Turmoil, and MS at `systems/overview/sim/ms_track.py` — are live and already
ticking. **That stub is the single highest-value piece of unbuilt threadwork in the tree**,
because it is the one place the personal scale and the strategic scale actually meet.

**Two corrections to the shape the suite proposed.** Strain accrues from a **held** manipulative
shape rather than from discrete operations, which is what makes holding a debt rather than a
purchase. And a being past the band maintaining itself is the limiting case, not a special rule.

**Mending Stability survives as it is.** The v30 settlement consequences — Weaving → Order,
Mending → Prosperity, Lock → Defense, capped at ±1 per settlement stat per season — are keyed to
verbs, and under §6.6 they should be keyed to **direction**: it is restorative work that raises
Prosperity, whatever verb performed it, and manipulative work that a settlement pays for.

### 3.4 Where it appears in each subsystem

| subsystem | how threadwork appears |
|---|---|
| **`systems/combat`** | **The Leap is a prepared action and never a combat action.** The window is long enough to lose a fight in, and damage taken inside it lands on the reconstitution. Against a **drifting** opponent the ladder is a real difficulty curve and it is canon-derived: at Dissonant their responses address intent rather than movement, so *feinting fails and directness works* — a teachable counter that follows from §7.2's own wording. Against a **threadcut being**, attrition does not work and distributed simultaneous demands do, because being configured is itself the work and the rate is finite and never eases (§4.5). **Never Past-Pull one**: it has no spooled past to be pulled toward, so the operation leaves a Gap where the configuration was (§8.4a) |
| **`systems/social_contest`** *(the proceedings subsystem)* | **A Dissonant practitioner wins the room and loses the record.** Answering the position behind the words is devastating in a negotiation and is an exhibit in a proceeding. Their **self-report is structurally as-if**, so advocacy attacks the *outward* facing and never cross-examines the practitioner on their own state — the honest answer available to them is that it was *as though* it were sound. And **two honest irreconcilable witnesses are a finding, not a credibility contest**: a court here cannot default to *one of you is lying* without discarding its evidence |
| **`systems/mass_battle`** | **Terrain prepared before the battle is the decisive use, and it is invisible below Structural reach** — a campaign decided by threadwork looks, to everyone including the historians, like a campaign decided by good roads. **No battlefield lattices**: force distributes by topology rather than by sum, disagreement at the knots damages both target and practitioners, and a practitioner whose contact closes mid-operation loosens what they held. A structure that degrades exactly when it is needed. **Holding a formation's cohesion is manipulative and permanent** — released, it routs; maintained, it is a debt and a unit nobody can billet |
| **`systems/settlements`** | Thread perception is already settlement-modulated (+1 Ob in Cathedral settlements, −1 in Outposts near Askeheim), which is §8.8's prophylaxis expressed as terrain. Add the **occurrent holding**: a practitioner among people is held, and one alone is not. Isolation is a mechanical hazard, not a mood. **Wrapping accumulates in rooms** a practitioner uses repeatedly, until every entrant reports a presence with no content — a detection surface with no perpetrator |
| **`systems/factions`** | **Threadwork is an accelerant, never a victory path**, and its own consequences suppress the Accord it needs. Two traps worth building: the **record problem** — political power rests on documents, precedent and lineage, all retained history, and threadwork degrades the substance of the authority it is used to acquire; and **doctrinal loosening**, which drives piety down and manufactures an anti-Church formation that, by §8.8's own logic, sits *outside the prophylaxis* and therefore produces sensitives at a higher rate than any established faction. A faction that uses it as an economic weapon is manufacturing a thread-capable insurgency |
| **`systems/fieldwork`** | `knots.py` already charges Coherence on rupture — the only cross-subsystem production call site — and under the ruled model that is right, because a rupture is an **event** and events are the only thing that deforms. Knots are also the propagation channel and are **distance-independent**: a drifting practitioner who leaves stops straining the local rendering and keeps pulling on knotted kin. **Exile does not protect the people who love them** |
| **`engine/season`** | Strain per province per season; Locked Zones that do not heal because the process that would undo them is the one precluded; incursions by mode, where **Mode 2 is an event with nothing to fight** and Mode 1 deteriorates on its own so the cordon is the answer and the exposure is the hazard |
| **`systems/npcs`** | Drift propagates tridimensionally through every knot, at magnitudes individually below notice. In a household, exposure **branches** — one member develops sensitivity, one is reconfigured, one cannot hold it — and the framework has no variable that predicts which. **Leave it unexplained.** §1.1's epistemic charter makes an honest gap a legitimate finding, and the suite's own proposed predictor is the axis that R-14 superseded |

### 3.5 The dramatic engine is the knife-edge, not spectacle

The suite worried, correctly, that its economy made optimal play quiet: aligned work is free and
invisible, opposed work is expensive and legible, so a competent house does small invisible things
and the fiction goes flat. **Under the rulings the pressure sits somewhere better.**

**Two workings look identical from outside and are categorically different.** Restoring the
harmony configurations tend toward — whatever that turns out to be — is restorative and safe at
any scale, up to and including Mending a whole province. Restoring a **remembered** state, or an
intended one, is a shape the practitioner chose, and holding configurations there is manipulation;
at provincial scale, sustained, it is the Calamity's mechanism exactly.

**And the temptation is precise, and it is not a temptation to do evil.** Someone restoring a
ruined province will have in mind what it looked like before, and will want that. *Wanting it is
what converts the work.* The discipline Mending requires is to restart the tending and let it go
where it goes, which may not be anywhere anyone remembers.

That is the game's central choice and it recurs at every scale — a province, a household, a
person past the band whom someone loves. **It will keep happening, because it is precisely what
love asks for.** Spectacle is not what this system has to offer; this is.

---

## 4. Three of the suite's open questions, closed by ruling

### 4.1 Q-1 — Diagnosis is perception, and it costs nothing

The suite ranked this its single highest-leverage open item — *"one sentence in the Foundations
settles it"* — because under the contact reading every read damages what it examines and every
diagnostic institution it proposed becomes unaffordable. **§6.1 supplies the sentence.** An operation is threadwork that requires **going beyond oneself
as a finite ordinary human** — which is why every operation requires a Leap. And R-16 separates
seeing from working in the same breath: *"the more of a thread you can see, the more you can
manipulate."* Perceiving further outside the human band is what reach *is* (R-13); it moves no
threads and crosses nothing. **Diagnosis is not an operation, so P-01 and P-11 do not reach it,
and it costs nothing.** The suite assumed this and flagged the assumption everywhere; it can stop
flagging it.

**Consequence, and it is the shape of the whole discipline:** reading is free and working is dear,
so prognosis outranks operation at every level — a medical order built around diagnosis with
intervention as a minor terminal step, a commander who reads and does not work, a guild whose
mastery is prognostic and whose journeyman skill is operative. That inversion follows from the
cost structure rather than from taste.

### 4.2 Q-7 — There *is* a third practitioner term, and it is resilience

The suite drafted an Immersive Orientation axis, and then recommended against ratifying it,
because its warrant was a construct whose interpretation had been formally disputed. That was the
right call on the evidence it had. **R-14 has since supplied the term with an author's ruling
behind it:** the cost is Coherence, and what prevents it is *how resilient their spirit is, which
is basically how strongly configured they are.* The slot the suite identified was real; the
candidate it declined to seat is superseded rather than vindicated.

### 4.3 Q-11 — Accelerated decay is destructive, and both of the suite's readings are struck

The suite ranked this second only to Q-1, because it decides whether harm is cheaper than help,
whether sieges are defendable, and whether threadwork wins wars. It offered two readings of the
old §16.1 and could not choose:

- **Reading A** — the substrate is tending toward decay, so accelerating it is aligned and free.
  Grounded on *"what the substrate's own spooling would resume given sufficient time."*
- **Reading B** — the rendering performs continuous work holding the configuration up, so
  knocking it down opposes that. Grounded on the rendering's *"continuous, unconscious work to
  maintain the configuration in its stable shape."*

**Both grounds are now forbidden formulations, and the question dissolves rather than resolving.**
P-07's new second clause fails Reading A's sentence by name — *does any rule give spooling a
direction, something it "would resume", was "already moving toward", or does "given sufficient
time"? → FAIL.* And §3.4 answers Reading B directly: *"Not the rendering's, either."* **The
orientation belongs to the threads** (R-12): they are naturally and fundamentally oriented toward
being in equilibrium with all other threads, and that is what they are *like* rather than
something they do.

**§6.6's third type is the answer, and a binary aligned/opposed model had no room for it.**
Destroying a configuration that stands in harmony with others breaks that harmony, leaves the
configurations that depended on it off the attractor, and the practitioner bears the severance —
with the damage not confined to the target. **So harm is not free**, which is what the suite
recommended, on grounds it did not have.

**And the carve-out is sharper than the one it proposed.** The suite excepted *"what the rendering
has already ceased to hold"*, which imports Reading B's mechanism. The canonical version is
simpler: a configuration standing in harmony with **nothing** has no harmony to sever. A corpse, a
structure past holding, a crop already lost — unmaking these breaks nothing, because nothing was
depending on them to hold its own shape. *(Derived from §6.6's definition; reject it and §6.6
stands untouched.)*

**Verdict on the suite's §0.2 alignment asymmetry:** discarded. *"Threadwork is structurally
better suited to war than to peace"* rests entirely on Reading A. **What survives is the reverse,
and it is more interesting:** restorative work is the free kind, it is *restorative to the
practitioner*, and it is safe at any scale — so the largest free surface is medicine, and a
practitioner's career is sustained by the work that heals rather than eroded by the work that
harms.

---

## 5. Still open, and where each now sits

| suite item | status |
|---|---|
| **Q-2** — can a title or claim be knotted? | Open. §6.4 permits knotting generally and §2.1 composes thoughts and concepts from threads; nothing rules on institutional objects. A design call |
| **Q-3** — does the Church retain adepts? | Open, and §8.8 sharpens the case *against*: the prophylaxis is formation into an orientation whose preconditions are unavailable, and **the most devout are the most thoroughly immunized**. An inner tradition stays permitted (§8.9) |
| **Q-4** — CD and History Resonance magnitudes | **Dissolved.** The regenerated P-11 names neither, and §10's regeneration removed numbers from the constraint table on principle: a constraint may require that an effect be Coherence-indexed; it may not name a threshold |
| **Q-5** — does a Restoration Movement have thread capability? | Open, and the most interesting unexplored consequence of §8.8: anti-Church formation is formation *outside* the prophylaxis, so such populations should produce sensitives at a higher base rate than any established faction — making the prophylaxis's own failure mode the setting's engine of new practitioners |
| **Q-8** — the case that breaks the framework | Open, and a commission rather than a question. The suite's nine casebook entries all resolve cleanly, which is evidence the schema is generative and equally evidence they were written to fit it. **§7.5's strain posit is the other one**, taken at §1.8 here rather than left open |
| **Q-12** — does aligned acceleration compound across generations? | Open, and the rulings make it *sharper* rather than closer. §6.6 makes restorative operations non-corrosive **at any scale** because nothing is held. But the Einhir were not opposed at every step either — what they held was *a refinement their configurations did not tend toward*. So the question is whether a directed programme restores a harmony or imposes a chosen one: **§6.6's knife-edge at civilizational scale**, and the economic question of the setting |

---

## 6. What must not be built

Each of these contradicts something ruled, and each was reachable from the suite's own material.

- **A Coherence meter its owner can read** (§4.3), or **a track that depletes and refills**
  (`RULINGS.md`, and it is what the live code does).
- **A cure, a therapy track, or a stabilizing item for drift.** Recovery is time in an environment
  at equilibrium, accelerated by mending, and it is elastic only. Nothing repairs a permanent set
  but restorative threadwork aimed at the configuration carrying it.
- **A mechanic that makes non-sensitives forget** (P-08: the barrier is **inertness, not
  amnesia**), or **a dispel verb, truesight, or any percept resolved by knowing better** — insight
  is real and inert.
- **Clean, undetectable memory erasure** (P-09). A pull displaces; the absence has an edge; the
  displaced configuration orphans and decays.
- **An alignment axis, a corruption track, or an arc from good to evil.** Drift is **amoral in the
  strict sense** — being moral requires being human, so it departs from the register in which
  better and worse apply rather than failing within it. Grading it is a category error, not a
  kindness withheld.
- **Uncanniness from category ambiguity, or drift rendered as deviance.** Channel inconsistency,
  always.
- **A fourth operation minted to give the intelligibility dimension one of its own** (§2.6);
  **a stat block for a Mode 2 event** (P-05 — there is nothing to kill); **Coherence applied to a
  threadcut being** (P-06 — layer 2 is absent by structure, not degraded).
- **Freefall played as transcendence.** §7.6 says so in those words.

*(The suite's safety requirements — photosensitivity thresholds, an opt-out group for the
perceptual manipulations, the dehumanization constraint — are adopted unchanged.)*

---

## 7. Escalation — none, and what was attacked to establish it

Five candidates were worked through the CLAUDE.md §0 gate and each was answerable without Jordan.
Recorded so a later session does not re-open them by drift.

- **Whether accelerated decay is aligned** (Q-11) — *superseded*: both readings quote formulations
  P-07 and §3.4 now forbid, and §6.6's third type is the answer. §4.3 here.
- **Whether Diagnosis costs** (Q-1) — *answered by a design document*: §6.1's criterion plus
  R-16's separation of seeing from working. §4.1 here. **A third practitioner axis** (Q-7) —
  *superseded* by R-14. §4.2 here.
- **Whether awe and dread belong to the encounter or to a reading of it** — *answered*: §5.3 rules
  the signature structurally identical, §8.8 rules the Church's reading an inversion of it. A
  cultural variable, not a stimulus parameter, and §5.5 binds the limit: equanimity does not
  reduce the encounter.
- **Whether §7.5's strain load is split** — *answered by what makes sense for the architecture*,
  and taken rather than escalated because §7.5's own definitional sentence has no division in it.
  Flagged at §1.8 here as the reading to attack first, with what would falsify it.

**Two things do remain for the author:** whether this design is adopted, and whether
`threadwork_v30.md` Part 3 is edited in place or superseded. `CURRENT.md` is unchanged until then.

```
[READ: canon/philosophy/ 00–10 + RULINGS.md + README.md, in full; valoria-unreality-suite/ 00–10,
  in full; systems/threadwork/sim/{coherence,operations}.py; threadwork_v30.md head;
  engine/cross_scale/handoff_rules.py; module_contracts.yaml threadwork rows]
[DERIVED, not ruled — reject any and the ruling behind it survives: the elastic-range default
  (§1.10 here); §7.5's strain reading (§1.8); the destructive carve-out (§4.3); direction per
  working rather than per verb (§1.3)]
[CONFIDENCE: high — §1 and §2, which restate rulings and carry a canonical reason per verdict.
  medium — §3.4 here, which extends canon into subsystems it does not address: design, not derivation]
[SELF-AUTHORED — bias risk: §2 adopts or corrects far more of the suite than it discards, which is
  what a reader should test first; and §3.4 here reads threadwork into seven subsystems without having
  read their heads in full, so a collision with a live design there is likelier than I can see]
```
