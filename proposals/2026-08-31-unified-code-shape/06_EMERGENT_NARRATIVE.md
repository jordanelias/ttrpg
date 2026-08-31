# 06 · EMERGENT NARRATIVE — a story is a provenance chain you can walk

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L3.** This document contains **no narrative engine, no quest object, no story grammar and
## no authored arc.** If it did, it would have failed. What it contains is the four mechanisms that make
## a story happen anyway, and the one register that says how anything reaches a decider.

---

## §1 · THE CLAIM, AND THE EVIDENCE THAT IT IS NOT WISHFUL

> **A story in this game is not generated. It is what a provenance chain looks like when you read it
> backwards.**

Every Event carries `causes[]` — the ids of the Events that caused it. Every Claim carries a source
naming the Event or the speaker it came from. **So the arc is already in the log, as a walkable graph,
before anyone thinks about narrative at all.** An arc is a **projection** over that graph, not a
structure maintained beside it.

**This is a strong claim and it was tested rather than asserted.** A 55-arc corpus written years earlier
— stories the old machinery produced with ambient tracks, faction-wide scalars and thresholds firing
with nobody deciding — was scored against a design of this shape by three lanes that could not see each
other:

| verdict | count |
|---|---|
| **REPRODUCED-BETTER** | **40** |
| REPRODUCED | 2 |
| TRANSFORMED | 22 |
| **LOST** | **10** |
| NEVER-WORKED (in the original, either) | 9 |

**MECHANISM: no, on essentially the entire corpus. STORY: reproduced or improved in 42 of 74.**

> **The scaffolding hypothesis is confirmed.** The old machinery — ambient tracks drifting with no
> actor, faction-wide scalars, thresholds firing with nobody deciding — **was scaffolding around stories
> that survive without it, and usually improve.**

**And the ten losses are not noise. They are one loss, ten times**, and §6 says what it is and what this
shape pays for it.

---

## §2 · THE FOUR MECHANISMS, AND NOT ONE OF THEM IS A NARRATIVE SYSTEM

| # | mechanism | what it produces | where it lives |
|---|---|---|---|
| 1 | **the provenance chain** | the arc itself, walkable, after the fact | `causes[]` on every Event |
| 2 | **ambition** | why a person keeps pushing at one thing for twenty seasons | a Proposition + `INTENDS` claims + **derived** progress |
| 3 | **the candidate + the cast gate + the rank** | how anything at all reaches a decider | §4 |
| 4 | **collision** | why two people who both want good things end up enemies | two Propositions with intersecting `when` and incompatible values |

**Everything else people call narrative machinery is refused**, and §7 lists what covers each refusal.

---

## §3 · AMBITION — a want with an object, derived at read

**Jordan's ruling requires that an ambition have an OBJECT, not only a magnitude.** *Their ambitions
within that world are the regions that drive conflict* — and **two people with identical standing gaps
must be able to want incompatible things.** A scalar drive cannot do that; two people with the same
number want the same amount of nothing in particular.

> **And the want is not a new object: a Proposition of mood `OUGHT` IS AN UTTERED BELIEF** (`02` §5.5.2).
> **What a person is pursuing is what they hold right, said out loud** — which is why it can be argued
> with, committed to by others, and betrayed by its own author.

```
the want      := a Proposition (mood OUGHT) — an uttered Belief, immutable once said
the pursuit   := INTENDS(person, proposition) claims in that person's own ledger
the progress  := DERIVED AT READ, never stored:
                     progress(P) = sum over terms i of  w_i * [ term_i holds now ]
the drive     := Sensation.standing — the gap between what everyone reads off you
                     and what you hold. THAT GAP IS AMBITION, computed.
```

**Four properties, each of which is the reason a different failure does not happen:**

- **`progress` is derived at read, so it cannot go stale and cannot be initialised and forgotten.** It is
  a sum over **terms that are ordinary world conditions** — a Tenure existing, a condition band, a mark
  held, a Record present — so **any act by anyone moves it**, including acts by people who have never
  heard of the ambition.
- **Therefore obstruction needs no verb.** A stranger who takes the seat you needed has obstructed you
  without an `obstruct` act existing, without knowing you exist, and without the resolver branching on
  anything. **This is the single best property in the whole narrative layer** — it is what makes a rival
  emerge rather than be assigned.
- **Progress is published as BANDS, never as a number and never as a forecast.** A forecast is a
  threshold in a costume: it tells the player the future, which makes the future the world's property
  rather than theirs.
- **It lapses.** A pursuit with no act behind it for long enough drops out. **Without lapse the queue
  becomes immortal clutter**, and every character accumulates a museum of things they once wanted.

**N-line.** Cut the ambition object and a person's motivation is their larder and their rank. Every
magnate, every churchman and every movement leader falls to zero — **which is the measured state**: the
two need terms that would supply the rest were specified nowhere, so for a magnate **100% of motivation
was uncomputed.**

**And the fifth property, which is the setting's own:** because the want is a Proposition, **a lie can
discharge it.** Telling a committed man *the gate now admits on work* deposits a row that unifies with
his faction's proposition; if his credulity and his stance toward the speaker carry it, **his urgency
drops for as long as the row survives collision with the world.** *The leader who says we have won*
becomes a priced act with a real effect and a real failure mode, **and nobody wrote it.**

---

## §4 · THE SLATE — how anything is put in front of a decider

**This is the least-closed hole in the design line and the most-worked mechanism in the corpus, and the
two facts are about the same thing:** the machinery exists, in detail, with proofs — and the design head
that needed it never read it.

### §4.1 One mechanism, two fidelities — not a player module

> ⊕ **RULED: attention is ONE mechanism instantiated at every rung, not a player-facing module.**
> A system instantiated at a rung must be instantiable at **every** rung it claims. **A player-only
> attention module is forbidden by that rule**, and building one is how a design acquires an elite-only
> politics through the back door.

| | NPC fidelity | player fidelity |
|---|---|---|
| the pool | claims in the ledger | candidates emitted at the boundary |
| **the gate** | the claim is in the ledger at all | `witness.channel` is one of **five** and non-empty |
| **the rank** | `salience(c)` | `cast_score(c)` |
| the budget | `K = 7 + Focus + 2 per Knot consulted − Coherence penalty` | `B` opportunities per season |
| depth | n/a | `depth_score`, which decides **render depth among the cast and NEVER entry** |

**The two are the same shape — `gate THEN rank` — and the gate is never traded against the rank.**

### §4.2 The cast gate — knowability is a GATE, salience is a RANK

> **A candidate is cast only if it is knowable. Salience never buys knowability, and knowability never
> substitutes for salience. Composed as `gate THEN rank`, never summed, never traded off.**

**Five witness channels, no sixth:** `post_remit` · `co_located` · `witness_key` · `document_key` ·
`chronicle`. **A candidate fitting none of the five is shaded, whatever it scores.**

**Three consequences that make this a mechanic and not a filter:**

1. **Misperception reaches the surface; the world's state does not.** A witness-borne candidate is built
   from the **witness's claim**, and **the proposition it names may simply fail to obtain.** What is
   shown is the claim with its provenance, never the world's state.
2. **A barred candidate is not suppressed — it arrives thinner.** A Thread-constituted situation reaching
   a non-sensitive is cast through its **surface effects** — the failing harvest, the sick cattle — with
   the Thread-level payload absent. **The player sees that something is happening and cannot see what.**
   That is *inaccessibility, not suppression*, which is what the canon constraint asks for.
3. **The gate is disclosed as an input; the trigger is not.** A player may inspect **which channel**
   carried an item and reason about the channels they lack. **The score, the threshold and the budget
   arithmetic stay hidden.** Publish the inputs, never the trigger.

**And the one thing this forbids outright:** a candidate may **not** be cast on the strength of its
salience alone. **Mandatory rows bypass RANKING; they do not bypass the CAST GATE** — and every existing
mandatory trigger is knowability-satisfied by construction, so the exemption costs nothing.

### §4.3 The two scores, and why the severance is load-bearing

```
cast_score(c)  = meaningfulness(c) x inertia(c) x scale_weight(c.scale)      # REALIZED terms only
   meaningfulness(c) = durability(c) x tie_proximity(c, viewer) x identity_touch(c)

depth_score(c) = cast_score(c) x imminence(c.horizon.band)                   # depth ONLY, never entry
```

> **Casting keys on the tie-graph and REALIZED state only. Forecast and imminence govern render depth,
> never which futures are impelled at the player.** Collapse the two and the engine starts pushing
> futures at the player, which is the failure that turns a churning world into a story with a plot.

**`tie_proximity` is derived centrally, never supplied by the emitter.** That is what makes
**viewer-rooting** hold for every emitter without every emitter having to know who is watching.

> ⊕ **AND ONE TERM IS CUT ON ITS OWN N-LINE** [LANE B]. `forecast_mass` appears in the ranking and
> **has no producer anywhere in the corpus.** An object with no producer cannot name what is lost by
> cutting it. **Cut it.** `depth_score` reduces to `cast_score x imminence` until something produces it.

**Integer basis points throughout, integer division, no floats.** Not decoration: **this ordering
crosses the port**, and float accumulation order differs between the two languages. *(Note the
independent convergence — the attention layer reached the same fixed-point conclusion as the resolution
layer, from a different direction, for a different reason.)*

### §4.4 Truncation, and the property that makes it safe

The Slate truncates to the budget in a fixed order — **mandatory, then engaged, then fresh, then
persisting** — with **caps that are independent of the score.**

**Score-independent caps are the monotonicity condition**, and monotonicity is what stops a player's own
action from evicting the thing they acted on. Without it, attending to an item can push it off your own
slate next season, which reads as the world losing interest **because** you cared.

**Inertia is derived from the log, not stored.** A situation that was on your slate last season is
recognisably the same situation this season **because its `candidate_id` is a content hash that
deliberately excludes the season** — so identity persists without any store, and attention does not
strobe.

### §4.5 The funnel, and the number that is the whole point

Roughly **190–200 candidates resolve per season**; **6 reach the slate**; **4 are acted on.** Over a
50-season campaign: **~9,750 candidates resolve, ~300 surface, ~200 are played.**

> **The player sees about 3% of what happens and acts on about 2%. One hundred percent of it resolves.**
>
> **That ratio IS the design.** Every other mechanism in this suite increases what the world produces;
> without the funnel that increase reaches the player as **volume** — a hundred true, caused,
> well-provenanced things a season, **none of which is worth reading because all of them arrived.**

**And the surplus is the point, not an overflow to be minimised.** Choosing what to attend to **is** the
gameplay.

---

## §5 · THE CANDIDATE CONTRACT — the six rules, each naming its failure

Every emitter satisfies this, and an emitter is **any** step that can produce something a person might
attend to: a world event, an ambition firing, a vacancy, a petition dropped, a band crossed.

| # | rule | the failure it prevents |
|---|---|---|
| **C-1** | **`provenance` required and non-empty** — the id of the Event that caused it | a situation appearing for no reason. **In a game with no GM, this is the property that makes the whole layer trustworthy** |
| **C-2** | **`witness` required and non-empty**, one of five channels | a salient thing the player cannot know about leaking through the surface |
| **C-3** | an emitter supplies **realized-state terms only** | world-visible imminence; **never publish the trigger** |
| **C-4** | `resolver_ref` names a module that already exists and resolves it **at both fidelities** | **a second, cheaper resolution path** — the seam every player community in the genre finds and exploits |
| **C-5** | `responses` are 3–5 ids from `resolver_ref`'s **declared** option set | verb creep: a candidate that could invent responses routes around the cap |
| **C-6** | an emitter **emits**; it never presents, ranks, or checks the budget | **the reason this is one function and not eight competing ones.** An emitter that drew its own per-place quota and presented it is how a 37-place world manufactures 75 undifferentiated demands |

**`informational: true` is the one exemption, and only from C-4/C-5:** a crossing fact — *a village grew,
a bloc formed, a presence crossed a band* — is **news, not a situation.** Rendered, never resolved,
capped separately so news cannot crowd out decisions.

---

## §6 · WHAT THIS SHAPE CANNOT DO, STATED BEFORE SOMEONE DISCOVERS IT

> ⚠ **AN EARLIER DRAFT OF THIS SECTION READ *"the ten LOST arcs are one loss, ten times"*, AND THAT IS
> THE EXACT CONFLATION A SOURCE LANE NAMES AND FORBIDS.** That lane wrote: *"the seven LOST arcs share
> one blocker, and it is **not thresholds** … the corpus has been conflating them,"* and asked for
> **two independent findings** instead of one. Overstating a cost is not a safe error: **priced at ten
> arcs it looks like the largest concession in the design, and that is the argument someone will later
> use to re-admit thresholds.** They are two findings.

### §6.1 · Finding one — the threshold refusal, and what it actually costs

**In the band where it was measured — eighteen arcs — three end at a counter reaching a number with
nobody deciding, and lose their ending. Thirteen end at a scheduled sitting and survive**, because a
sitting has a **named convener** who can be bought, delayed or killed. **In another lane's band the
threshold refusal costs NOTHING.**

> **The loss belongs to the VARIABLE, not to the threshold.**

**The threshold's real job in the old corpus was to be the world's own agency: the one actor that is not
a person.** Law 1 refuses that, deliberately. What partially substitutes:

| substitute | what it does | what it does not do |
|---|---|---|
| material need at MATTER | makes inaction expensive | does not force a decision |
| confidence decay | **you lose a settlement by being forgotten** | does not force a decision |
| dormant rows re-arming at CALENDAR | keeps a suppressed grievance reachable | does not force a decision |

**None of the three FORCES a position. They make holding one more expensive.** That is the trade, and it
is taken with open eyes.

### §6.2 · Finding two — the LOST arcs, and they are NOT one loss

**Ten arcs were scored LOST across three lanes, and they do not share a blocker.** The source lane that
holds seven of them says so outright: *"the seven LOST arcs share one blocker, and **it is not
thresholds**."* Those seven die on **a world-substrate quantity the design did not have (five)**, or on
**an actor it could not instantiate (two).**

| how many | what they die on | this suite's disposition |
|---|---|---|
| **five** | **the world-substrate hole** | **CLOSED** — a Thread seam is a `Site` and its `condition` is the quantity (`05` §3), with zero new objects |
| **two** | **an off-board actor that cannot be instantiated** | **GATED, deliberately** — an agentive actorless row is blocked until a criterion exists (`05` §4.4) |
| **one** | a closure-axis loss in the eighteen-arc band | §6.1 |
| the rest | a third lane's band | not re-adjudicated here |

> **So the honest price of Law 1 is NOT ten arcs.** Five are recovered by a closure this suite makes
> three documents away; two are held behind a gate it declares; **and conflating all ten into a single
> threshold loss would overstate the cost of the design's central refusal by roughly a factor of
> three.**

### §6.3 The sharpest unmeasured claim in the whole design

**Nothing measures whether confrontations arrive at all.** The old corpus guaranteed convergence by
**authoring** it — a trigger inventory and a season-by-season timeline. This shape guarantees only that
**if** crises converge, a standing date forces them to fight.

> **There is a recoverability check and NO convergence check. That is the sharpest unmeasured claim in
> the suite, and this document states it rather than closing it.**
>
> **And it deliberately proposes no instrument for it**, because the correct question first is *whether
> a convergence measure is about the GAME or about the PROCESS.* A measure that reports *"this campaign
> produced four collisions"* to a designer is about the process, and this repository has a documented
> pathology of answering process failures with apparatus. **If convergence is a game property, it is a
> property of `wear`, the act budget and the date calendar — and it is settled by running campaigns, not
> by building a checker.**

### §6.4 The uncomfortable calibration result, and the rule it produced

**The two acts that reproduce the corpus's flagship arc are the two acts a play-space audit filed as
DOMINANCE DEFECTS.** Fix them, and the arc stops being producible.

> **RULED: apply R at seats a player can occupy. Everywhere else, a dominant act is a PORTRAIT.**
>
> An act that dominates an **NPC's** menu is not a robustness failure — **it is characterisation.** A
> zealot *should* accumulate relentlessly and without deliberating; that is who he is, and **the design
> reproducing it from his stance table rather than from a script is a success, not a bug.**
>
> **But this cuts both ways, and the second half is load-bearing:** it makes *"is this seat playable?"*
> a question that must be answered **per seat** before R can be applied at all. A dominant act at a seat
> the player can occupy is a real defect. **The same act, at the same seat, is a defect or a portrait
> depending on an answer nobody has written down yet.**

---

## §7 · WHAT THIS DOCUMENT REFUSES, AND WHAT COVERS EACH REFUSAL

| refused | because | what does the job |
|---|---|---|
| a narrative engine | a story that is generated is a story someone wrote | the provenance chain, read backwards |
| an authored per-person opportunity or quest object | **a churning world turns back into content** | `opening_set` recomputed from need + capability + the terms they hold a claim of |
| an arc object, an arc state machine, an arc registry | an arc is a projection; a projection with a store goes stale | `causes[]` |
| a stored `progress` gauge or clock on an ambition | dead state that reads as mechanism | derived at read over world terms |
| a forecast shown to the player | it makes the future the world's property rather than the player's | **bands, never numbers; imminence governs depth, never entry** |
| a `credence` or `information` store on the thing known | knowledge with no knower cannot be planted or refuted | the per-person claim ledger |
| a convergence timeline or trigger inventory | the world would churn on rails | gates over state, rate-bounded (§6.1 states the cost) |
| a **sixth** witness channel | five are checkable; a sixth is where "the player just knows" gets in | shade it |
| `forecast_mass` | **no producer anywhere in the corpus** | cut, per its own missing N-line |
| a player-only attention module | forbidden by the every-rung rule | one mechanism, two fidelities (§4.1) |
| a second, cheaper resolution path for anything on the slate | **the twenty-year unsolved divergence in this genre** | C-4 |

---

## §8 · THE NARRATIVE LEDGER — every emergent opportunity, its mechanism, its N-line

**This is the catalogue the shape must carry.** Each row names a thing that can happen with nobody
authoring it, the mechanism that produces it, and what is lost if the mechanism is cut.

| # | what can happen | mechanism | N-line: lost if cut |
|---|---|---|---|
| 1 | **the famine nobody caused** | vacant date fires, allocates nothing, lapses | every shortage acquires a culprit; systemic tragedy is unreachable |
| 2 | **the withheld death-notice** | `until` at MATTER + per-person claim arrival gating every consequence | death becomes a global fact; information politics dies |
| 3 | **hostage politics — make him absent instead of killing him** | vacancy-by-absence as a convening condition over presence | removal-from-play collapses to murder |
| 4 | **revolt with no revolt meter** | grievance is a stance row; `commit` cheapened by grievance; coercive presence vs raisable force, all Queries | revolt needs a gauge, and a gauge is dead state |
| 5 | **the world creates an opportunity nobody authored** | a non-social `create` — a landslide exposes a seam — then a faction forms around working it | all novelty is authored content |
| 6 | **the village that legally exists after everyone died** | the Partition: an event kills bodies, only an office strikes the roll | world churn deletes politics instead of creating it |
| 7 | **forgery, and retroactive legitimacy collapse** | `plant` mints a root; `reconstruct` flips legitimacy **at telling speed, for exactly who learns** | documents are decoration; investigation has no prize |
| 8 | **burial is safe but never free** | `compose_agenda` costs an act; an omitted petition **is a drop and deposits as one when its backers learn** | petitions become a queue; filtering stops being a choice |
| 9 | **power without a post** | a channel, a custody, a gate or a unique root; the establishment acts; standing-by-leave | elite-only politics; **S-DOWN fails by construction** |
| 10 | **discovering the harbour silted by trying to ship from it** | `opening_set` is claim-derived; `verbs` is truth; the attempt resolves as discovery | omniscience re-enters through the interface |
| 11 | **two sincere witnesses who can never settle it** | per-person `witness`; construal divergence; reports are claims | the epistemic layer idles |
| 12 | **five repeaters are not five sources** | a Knot deposit **reuses the event id**; corroboration counts **distinct** roots and fails closed | rumour launders into corroboration; verification play dies |
| 13 | **deposition with no deposition system** | `leaders()` returning somebody else next season | leadership becomes a field; coups need a subsystem |
| 14 | **a rival who never heard of you** | ambition progress derived over world terms; obstruction needs no verb | rivalry must be assigned |
| 15 | **suppression breeds return at magnitude** | scars ratchet the arming threshold; dormant rows cleared only by terms | suppression is a delete |
| 16 | **prejudice as a refutable default, not a stored penalty** | empty-ledger defaults + mark legibility in each observer's own table | caste becomes an obstacle modifier |
| 17 | **the doctrine fight about how to tend the world** | two `OUGHT` Propositions over one site class collide automatically | Jordan's flux ruling has conflict but no carrier for it |
| 19 | **the hypocrite, and the movement discredited by its founder** | a faction's Proposition is an **uttered Belief**, so the founder's acts are checkable against it by anyone holding both claims | a faction's banner is authored rather than somebody's morals; nobody can fall short of their own stated position |
| 18 | **a season in which the interesting thing is what you did NOT get to** | one act per person, universally | scarcity disappears; refusal, delay and obstruction stop mattering |

**Eighteen rows, and not one of them is a feature.** Every one is two or three primitives meeting. **That
is what emergence means here, and it is the only test this document accepts: if a row needs a mechanism
of its own, the row is content and does not belong in an engine.**
