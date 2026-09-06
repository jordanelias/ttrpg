# 06 · RESOLUTION — the person, the pool, the margin, and where a title enters

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

> **Jordan's two directions, which this file answers together:**
> *"They will have attributes that influence their efficacy, and convictions, ethos, stances, biases."*
> *"Characters can have titles that impact their standing and influence."*

---

# PART A · FOUR WORDS, FOUR DIFFERENT THINGS — AND ONLY TWO ARE FIELDS

**The design's first job here is to refuse to make all four into stats.** `§D.0`'s admission clause —
*what kind of assertion is this field making: DECLARED, THE CASE, or READ OFF?* — separates them
cleanly, and the separation is the mechanism.

| the word | what it is | where it lives | assertion kind |
|---|---|---|---|
| **convictions** | what a person holds **RIGHT** — weights over the closed moral axes | ⭐ **`Person.convictions`, a field that already exists** | **declared** — a person's own, moved by argument and consequence, never by evidence (`AX-3`) |
| **stances** | a person's posture toward a particular subject | ⭐ **`Person.stance`, a field that already exists**, read by `stance_toward` | **declared** |
| **ethos** | what **others** take a person to be — practical wisdom, virtue, goodwill toward the hearer | ⚠ **NOT A FIELD. It is claims in OTHER PEOPLE'S ledgers**, one per hearer, each of which may be wrong | **read off**, and read off differently by each hearer |
| **biases** | ⚠ **NOT A FIELD, AND MUST NEVER BECOME ONE** | the **divergence** between what a person holds and what is the case, plus the weights their convictions put on the axes | **neither — it is a gap**, and `§D.0` says a gap between kinds is the signature of a **Query**, not a field |

> ### **THAT `bias` HAS NO REPRESENTATION IS THE STRONGEST RESULT IN THIS FILE.**
> A biased adjudicator is not a person with a `bias: 0.4` field. **They are a person who holds claims
> that are false, and whose convictions weight the axes differently from their neighbour's** — and
> `AX-2` guarantees that *"a false conclusion is indistinguishable from a true one to the person
> holding it."* **The bias is real, it changes the finding, nobody can read it off them, and nothing
> stores it.**
>
> **What it costs to add the field instead:** a bias meter is a value with two owners — the person
> who has it and the observer who reads it — which is `G.2.1`'s *"you can name two"*, and it would
> make prejudice legible in a game whose whole epistemic layer exists to make it illegible.

⚠ **AND `convictions` IS FOUR OF THIRTEEN, WHICH THIS DESIGN DOES NOT FIX.** `rosters.yaml:145-157`:
*"#353 says 'the closed 13' and NEVER ENUMERATES THEM. `H-46` is graded `absent` for exactly that
reason and Jordan's 2026-09-02 ruling says it must STAY open."* **This design does not name the other
nine and must not.** A proceedings subsystem is precisely where a session would be tempted to invent
moral axes to make its adjudicators interesting. **`H-46` stays open; the mechanism works at four and
works at thirteen, because nothing branches on a member.**

---

# PART B · **WHAT DETERMINES THE POOL** — and the arrangement narrows it rather than changing it

> **Jordan, 2026-09-06:** *"the big question for me is what determines the actor's pool, and whether
> that pool changes based upon the kind of proceeding."*

**A draft refused this question and registered the refusal as principled (`P-06`). That was an
over-refusal**: the study does not supply *numbers*, but it supplies the **shape** of the answer, and
the shape is the interesting part.

## B.0 · What the pool may NOT be, before what it is

| refused | why |
|---|---|
| **a per-proceeding skill** — *Advocacy* at a trial, *Diplomacy* at an embassy | ⚠ **scripting drift with a schema's face.** It branches on the game's name, which is the one thing `03_PARAMETERS.md`'s closure claim forbids. **And it is the reflex answer**, which is why it is named first |
| **nine capacity stats** | the study: the nine are **not claimed independent**, no factor structure is attempted, and *"the count of nine is a judgment, graded as a synthesis-gloss"* |
| **an office bonus** | `§A.3`: *"a seat adds no verb and no modifier… the moment a seat carries a modifier, the seat is a stat, and taking the seat becomes an optimisation rather than a political act"* |
| **an attribute expression** off the current roster | `CLAUDE.md` §5 — the derived-stat schema is **IN FLUX**: ruled at ten, nine shipped, **the tenth unnamed**. And Jordan, 2026-09-05: *"ignore their use of attributes"* |

## B.1 · ⭐ **THE ANSWER: THE ARRANGEMENT DOES NOT CHANGE WHICH POOL YOU USE. IT CHANGES HOW MUCH OF YOURSELF YOU MAY BRING.**

**This is Fig. 4 and Fig. 12 read together, and it is the study's own finding rather than a design
choice.**

> **Fig. 4, the discretion gate:** *"Where the arrangement is tight — a scripted audience, a
> written-only channel, a fixed warrant, a role with no latitude — **capacities 3 through 9 barely
> operate, and capacities 1 and 2 do the work.** Where it is loose, the reverse."*
>
> **Fig. 12, the capacity map, reading the two rows:** *"**The bottom row survives a tight
> arrangement. The top row does not.**"*

**So the study already partitions the actor into two halves, and says which half a room switches
off:**

| | Fig. 12's row | what it is | does a tight room suppress it? |
|---|---|---|---|
| **what you BROUGHT** | **bottom row** — institutional classification · evidential discrimination · generative reframing · *memoria* | **preparation.** What you know, what you hold, what you can construct | **NO — it survives** |
| **what you DO IN THE ROOM** | **top row** — calibration of reception · elicitation · control of display · tempo · rank-calibration | **conduct.** Reading, asking, withholding, timing | ⭐ **YES — this is what interposition removes** |

```
pool  =  brought                      -- always live. Two keys, not nine.
      +  conduct × latitude(game)     -- live in proportion to what the arrangement allows
      floored at 1D                   -- ruled 2026-09-04; applies to the MEAN as well as the variance
      fractional throughout           -- continuous_engine_sample, never roll_pool
```

**Two `capability` keys. `Person.capability` is already a dict and its keys are content by `ID-12`, so
naming two rather than nine costs nothing and commits to nothing.**

## B.2 · What this buys, and why it is better than a skill-per-proceeding table

| | |
|---|---|
| ⭐ **it answers Jordan's second question with a derivation rather than a table** | **the pool does not change by proceeding kind. The multiplier does** — and the multiplier is `latitude`, which is itself derived from what the arrangement interposes (`03_PARAMETERS.md` §B.1). **Nothing anywhere branches on a game's name** |
| ⭐ **the interposition price becomes mechanical, and it is the measured one** | Fig. 24: every interposition device moves a setting leftward. **Here it literally multiplies away the half of you that operates in the room.** The leader-effect evidence — *present in autocracies, absent in democracies; 23.8% private vs 16.6% public* — **is a statement about the size of the person-effect, and the person-effect IS the pool** |
| **the corpus falls out** | the **written summary** is all *brought* and no *conduct* — which is exactly what a written channel is. The **envoy alone abroad** has both. **Liudprand at Constantinople** had his preparation and almost no conduct, and the *Relatio* is what he did with the half he kept |
| **it explains why the terminal steps are terminal** | rows 0 and 14 — entry and close — are **decisions about the encounter**, taken where the multiplier does not reach. **You cannot be interposed out of choosing whether to go** |
| **it keeps `§A.2`** | still nothing gates. A person with almost no *conduct* at a scripted audience **still rolls**, at the 1D floor |

## B.3 · ⚠ **THE ONE CONSEQUENCE THAT TOUCHES A RULING, PUT UP RATHER THAN TAKEN**

**If `latitude` multiplies the pool, it should come OUT of the obstacle's five terms** — otherwise one
parameter both sets how much of the actor is present **and** how hard the room is, which is `G.1.5`'s
signature: *a design with one quantity that both measures and decides.*

| option | what it says |
|---|---|
| ⭐ **A — latitude in the POOL only** *(recommended)* | *an interposed room does not become harder to persuade; it becomes a room where **who you are matters less**.* That is the study's claim, stated exactly. The obstacle keeps **four** terms: reception, the rung, register fit, proofs told |
| **B — latitude in BOTH** | an interposed room is harder **and** flattens the person. Defensible for a ceremony, and it double-counts |
| **C — latitude in the OBSTACLE only** *(the current ruling)* | interposition makes the room harder for everyone equally — **which is the one thing the leader-effect evidence says it does not do** |

**This directory implements C, because C is what was ruled on 2026-09-06, and records A as the
recommendation with the evidence for it.** Registered `P-29`. **It is one line either way.**

> ### ✅ **RULED 2026-09-06 BY JORDAN: *"pool only it is."* OPTION A. THE THREE-WAY CONTRADICTION IS CLOSED.**
>
> **What the file did before this ruling, stated once so the record is honest:** `latitude` appeared in
> BOTH places — §B.1's pool and §C.1's obstacle — which is **option B**, the one this section calls a
> double-count. The text said it implemented **C** and recommended **A**. Three answers to one question.
>
> **The ruling takes A, and the decisive argument is not the one this section led with.** It is not that
> B double-counts (true but weak). It is **who interposition helps**:
>
> | | a WEAK speaker | a BRILLIANT speaker |
> |---|---|---|
> | **A — pool only** | ⭐ **helped** — the multiplier removes the half of them that was bad. *A duke who speaks badly is carried by his rank* | **hurt** — the brilliance is multiplied away |
> | **B — both** | hurt once | **hurt twice** |
>
> **A compresses the variance between people. That IS the leader-effect finding** — present in
> autocracies, absent in democracies; 23.8% private vs 16.6% public — which is a statement about **the
> size of the person-effect**, not about how hard the room is. **B reverses it**, punishing the
> incompetent hardest. **C — harder for everyone equally — is the one thing the evidence rules out.**
>
> ⭐ **AND A IS MULTIPLICATIVE WHERE MULTIPLICATION BELONGS.** Every flat obstacle term swings a weak
> speaker far more than a strong one (`§C.2`, `1/√pool`, `P-27`). Scaling a *pool* is proportional by
> construction and has no such asymmetry.
>
> **THE OBSTACLE THEREFORE HAS FOUR ROOM TERMS: reception · the rung · register fit · proofs told.**
> Every *"five terms"* statement in this directory is off by one at the base and is corrected where it
> is load-bearing. `P-29` closes.
> Raised by the playability relay's lane B as an out-of-lane observation and confirmed here.
> **`latitude` appears in BOTH places:** §B.1's pool is `brought + conduct × latitude(game)`, and
> §C.1's obstacle carries `± latitude` as its **first term**. That is exactly option **B**, three
> rows above, annotated *"an interposed room is harder **and** flattens the person … and it double-counts."*
>
> **So this file states three different answers to one question: it implements B, says it implements
> C, and recommends A.** `G.1.5`'s signature — *a design with one quantity that both measures and
> decides* — is not a hazard this section flags; it is a defect this section has.
>
> ### ⚠ **AND THE RULING CARRIES A CONSTRAINT, IN JORDAN'S WORDS: *"ensure you don't go so far as to
> deprive player of a chance at winning."*** §B.3a below is that constraint discharged.

## B.3a · ⭐ THE DEPRIVATION CONSTRAINT — *"don't go so far as to deprive player of a chance at winning"* (Jordan, 2026-09-06)

**The ruling's own risk, named by the person who made it.** Under A, a heavily interposed room
multiplies `conduct` toward zero. If nothing else held the pool up, a speaker in a scripted,
office-and-procedure-interposed audience would roll at the floor against an obstacle that has not
shrunk — **which is not a hard game, it is a wasted turn wearing a game's clothes.** Four things stop
it, and only the last needs building.

**1 · ⭐ `brought` IS NOT MULTIPLIED, AND THAT IS THE WHOLE ANSWER.** The pool is
`brought + conduct × latitude`. Interposition strips the half of you that **operates in the room** and
leaves the half you **walked in with** entirely intact.

> ### **SO INTERPOSITION DOES NOT DEPRIVE THE PLAYER. IT CONVERTS THE PROCEEDING FROM A PERFORMANCE
> GAME INTO A PREPARATION GAME.**
> A ceremony strips your bearing and leaves your dossier. The counter to a room that will not let you
> perform is to have **done the work beforehand** — the research, the examination, the proofs gathered,
> the people reached in the seasons before the sitting. **Those are acts the player already had, and
> this ruling is what makes them pay.** The corpus says the same thing about the written summary: it is
> *all `brought` and no `conduct`*, which is exactly what a written channel is.

**2 · The 1D floor holds the mean as well as the variance** (ruled 2026-09-04). The pool cannot reach
zero, so a person who tries something they are bad at **still rolls** — `§A.2`.

**3 · ⭐ THE σ-CHANNEL IS UNIFORM, AND THAT IS THE ENGINE'S OWN ANSWER TO THIS EXACT PROBLEM.**
`Δz = soft_cap(net_σ)` at **every pool size** — measured `0.874174` across pools 0.5→25. **Bought
advantage helps a 1D speaker exactly as much as a 16D one**, which is the property no flat obstacle
term has. So a player stripped of conduct **can still buy their way back into contention**, and the
thing they buy it with is something they did — a promise made in front of the bench, a debt opened.

**4 · The arrangement is VISIBLE** (`07_THE_GAME.md`'s owed column). The player **sees** the room is
interposed before spending the turn. A thin dossier walked into a ceremony is an informed decision that
loses, not a trap.

> ### ⚠ **THE ONE ASYMMETRY THAT COULD STILL DEPRIVE, AND IT IS NOW A MEASUREMENT.**
> **The obstacle is floored at 1 and CEILINGED AT NOTHING.** The pool has a floor; the composed
> obstacle has no cap. So the shape that would break the ruling is not low latitude — it is a composed
> obstacle growing without bound against a floored pool.
>
> **The check:** at the **minimum lawful pool** against the **maximum plausible composed obstacle**,
> `p_success` must not be effectively zero. **If it is, the remedy is (a) the σ-channel must be
> REACHABLE in that room — advantage must be buyable there — or (b) the obstacle takes a ceiling.**
> Registered as the deprivation floor, and it is a blocking check on shipping the composed obstacle,
> not an advisory one.

## B.4 · What is still `assumption`-grade, now narrowly

**Not *"the pool is unspecified"* — that was the over-refusal. What is open is two magnitudes:**

| | grade |
|---|---|
| the two `capability` key **names** | content (`ID-12`) — a data edit, not a decision |
| **how `latitude` maps to a multiplier** — is a maximally interposed room `×0`, or `×0.25`? | ⚠ **`assumption`. Inject, declare, sweep three points** (`ID-6`). ⭐ **`×0` is wrong and the study says why**: capacities 1 and 2 *"do the work"* in a tight room — they do not stop |
| the split between `brought` and `conduct` at world-gen | content |

⭐ **AND THE FLOOR IS WHAT MAKES THE MULTIPLIER SAFE.** *"1D is floor"*, applied to the mean as well as
the variance. **However tight the room, the actor is still there and still rolls** — which is the
difference between a proceeding and a cutscene.

# PART C · THE DRAW — **rewritten against the σ-leverage engine, which refutes the first version**

> **Jordan, 2026-09-06, directing this section:** *"To what extent is the designed system probabilistic
> instead of deterministic? Please now refer to the sigma-leverage resolver for its use of standard
> deviation, dice pools rolling against obstacles, and use of fractional dice and fractional
> obstacles."*
>
> ⚠ **This is the one place this directory reads outside `proposals/`, and it does so on that
> instruction.** The sources are `skills/valoria-resolution-diagnostic/SKILL.md` §11 and the API it
> names. **Behaviour is quoted from that document, not restated from memory**, and where it says a
> claim is *ruled and implemented nowhere*, this file says so too.

## C.0 · ⚠ **THE ROUND TRIP, RECORDED IN FULL — because the middle position was mine and it was wrong**

| | position | verdict |
|---|---|---|
| **1 · the draft** | `margin := pool − obstacle(latitude, reception, rung, register, proofs)` — five terms composing the obstacle | ⭐ **RIGHT, and restored at §C.1** |
| **2 · my "correction"** | *`base_Ob` — **NEVER MODIFIED***; all five terms rewritten as σ-levels | ⚠ **OVERREACH.** It read a narrow constraint on **advantage** as a blanket prohibition on **obstacles** |
| **3 · the ruling** | Jordan, 2026-09-06: *"I'm fine with Ob being modified by things. **+modifiers means it's already being modified, so that note warning is insane**."* and, on the draft, *"your presentation of obstacle makes sense to me"* | **implemented** |

**The ruling is right and the tree says so twice over — I cited both sources and then contradicted
them.**

> **The ruling itself contemplates modifiers.** Jordan, 2026-08-14: an obstacle rolled against a
> character or faction is *"their corresponding score/2 **plus whatever specific modifiers exist for
> them in that instance**."*
>
> **And canon P-232 is a FLOOR, not a prohibition:** *"Ob minimum 1; **no modifier may reduce Ob
> below 1**."* **A rule forbidding a modifier from reducing Ob below 1 presupposes that modifiers
> reduce Ob.** A blanket *never modified* contradicts the canon it was citing.

### C.0.1 · What is actually forbidden, stated at its true width

**One thing, and it is narrow: σ-LEVERAGE ADVANTAGE may not be spent as an Ob reduction.**

```
FORBIDDEN   Eff_Ob = base_Ob − eff_σ·σ_N        # F1, resolved by ED-884
LAWFUL      base_Ob = defender_score/2 + specific modifiers,  floored at 1   # the RULING
LAWFUL      net_boost = soft_cap(net_σ)·σ_per_die·√N          # advantage, as a μ-shift
```

**Two reasons, and only one of them still bites:**

| the reason F1 gave | still live? |
|---|---|
| the Ob-reduction form *"drove Effective Ob below 1 — violating P-232"* | ✅ **live.** A σ-scaled subtraction is unbounded below; a **composed** Ob is built up and floored |
| it *"made the Overwhelming threshold `2·Ob` nonsensical when Ob went negative"* | ⚠ **moot.** The ladder now reads the **margin** (`net − ob`), not `2·Ob` |
| ⭐ **and the one F1 did not lead with, which is the strongest** | **uniformity.** A flat Ob shift gives `Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools. A σ-level gives `Δz = soft_cap(net_σ)` at **every** pool size |

**So the constraint is about WHERE AN ADVANTAGE ENTERS, not about whether an obstacle can be
composed.** ⚠ **And `eff_ob()` / `effective_ob()` are a P-232-floored DISPLAY helper** — *"not
resolution"* — so the finding to look for is a caller **resolving** on `eff_ob` rather than on
`p_success`.

### C.0.2 · ⚠ A second stale claim, corrected

A draft of this file said the Ob derivation is *"implemented nowhere — every call site still passes a
hand-set Ob."* **The tree corrected that clause on 2026-09-05 (ED-IN-0202) and the draft repeated the
retracted version** — *a fact about the tree stated as timeless*, which is `G.3.3`'s named defect.

**What is true is narrower:** `coronation_renewal_ob` implements `floor(Church.L / 2) + 1` **exactly**;
Royal Progress derives its Ob from **the standing gap**; and ⭐ **the tribunal derives under formal
grounds.** What is missing is a **single owner** — most sites hand-set, the three opposed sites
disagree, and `parliamentary_transfer`'s `L+2` contradicts the ruling while being stated as canon.
**Reconciling them is a systems ruling and is SUSPENDED by Jordan (2026-08-21).**

> ⭐ **AND THE TRIBUNAL PRECEDENT MATTERS TO THIS DIRECTORY MORE THAN ANY OTHER FACT IN IT.** A
> proceeding-shaped Ob **already derives from formal grounds somewhere in the tree.** This design does
> not have to invent the shape; it has to not contradict it. Registered `P-25` as *follow the tribunal,
> do not re-derive.*

## C.1 · The shape — **RULED BY JORDAN, 2026-09-06: the five terms compose the obstacle**

> **Jordan, on the original five-term model:** *"your presentation of obstacle makes sense to me."*

**So the five terms are obstacle composition, and they are floored at 1.** That is the ruling; it is
implemented here; and the section below records what remains genuinely constrained and what would show
the call wrong.

```
pool      = the actor's capability          FRACTIONAL · floored at 1D · continuous_engine_sample
base_Ob   = the opposition's corresponding score / 2
            ± latitude          — what the arrangement interposes            (Fig. 4)
            ± reception         — ⭐ COMPOSED FROM THE HEARERS' OWN CLAIMS ABOUT THE SPEAKER
                                  AND THEIR CONVICTIONS ON THIS MATTER'S AXES.  Resolver-side,
                                  hidden from every decision by T-f.   (Figs. 3, 25; and see
                                  15_WHY_IT_IS_A_GAME.md PART C — this is what stops the
                                  proceeding being computable)
            ± the rung          — what is being asked for                    (Fig. 5)
            ± register fit      — which misreading this manner invites       (Fig. 8)
            ± proofs told so far in this run                                 (Fig. 6, S8)
            FLOORED AT 1        — canon P-232: "no modifier may reduce Ob below 1"
margin    = net − Ob   →   degree_from_net   →   Overwhelming | Success | Partial | Failure
veto      = the licence conditions (Fig. 26) — demote-only
```

**This is the ruling's own shape**: *"their corresponding score/2 **plus whatever specific modifiers
exist for them in that instance**"* (Jordan, 2026-08-14). Five named modifiers, each sourced to a
figure, each a property of **how hard this is in this room** — which is what an obstacle is.

### C.1.1 · The ONE thing that is still forbidden, and it is not this

**σ-leverage advantage may not be spent as an Ob reduction** — `Eff_Ob = base_Ob − eff_σ·σ_N`, F1,
resolved by ED-884. **That is a statement about the σ-channel, not about obstacles**, and the two do
not collide here: the five terms above are **composed into** `base_Ob` and floored, not **subtracted
from** it by an unbounded σ-scaled term.

**So the design carries both channels, and the rule for which is which is one line:**

| | |
|---|---|
| **compose into `Ob`** | anything that is a property of **how hard this is** — the opposition's score, what the room interposes, what is being asked for, what has already been produced |
| **enter as a σ-level** | anything the engine already treats as a **level of advantage** in σ-units, reached through `levels_to_net_sigma` → `net_boost` |

⚠ **AND `eff_ob()` / `effective_ob()` REMAIN DISPLAY-ONLY.** A caller that **resolves** on `eff_ob`
instead of `p_success` has reintroduced the retracted form. That finding is unaffected by this ruling.

### C.1.2 · What this call costs, recorded so it can be revisited rather than re-argued

**An Ob modifier's probabilistic impact scales as `1/√pool`** — `Δz = X/(0.8·√pool)`. So the five terms
**matter more to a weak speaker than a strong one.** That is the non-uniformity the σ-layer exists to
remove *from advantage levels*, and it is being accepted here for *obstacle composition*.

**Two readings, and I record that I first argued the wrong one:**

| | |
|---|---|
| ⚠ **what a draft argued** | that reception-in-Ob makes a title *disproportionately* powerful for a poor speaker, contradicting *"position dominates an inattentive room and merely tilts an attentive one"* |
| ⭐ **why that was probably backwards** | the study's *inattentive/attentive* axis is about **the room's elaboration**, not the speaker's skill. **A duke who speaks badly being carried by his rank, while a brilliant commoner is not, is the fiction the corpus actually describes** — Mi Zixia, Liudprand's seating, *the asking is itself evidence*. The `1/√pool` behaviour delivers exactly that |

> **The falsifier, so this is a call and not a preference:** sweep the five terms at pools {1, 4, 9, 16}
> and check whether a rank advantage swings a weak speaker's band **more** than a strong one's. **If it
> does and that reads wrong in play, the term to move to the σ-channel is `reception` alone** — not
> the other four, which are properties of the room and of the claim rather than of the person.
> Registered `P-27`.

## C.2 · What the engine gives this design for free, and it is a great deal

| the engine already does | the study already wanted it |
|---|---|
| **UNIFORM LEVERAGE** on the σ-channel — `Δz = soft_cap(net_σ)` at every pool size and every TN (measured `0.874174` across pools 0.5→25 at `net_σ = 1.0`) | ⚠ **available and not used by the five terms**, which are Ob composition by ruling (§C.1). It is the channel to move `reception` into if `P-27`'s sweep says so |
| **THE SOFT CAP** on the σ-channel — `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` | ⚠ **the design's overshoot ceiling is therefore NOT the soft cap** — it is `P-232`'s **Ob floor of 1**, which is what stops a speaker composing their way to a free win. **`S3`'s *excess of a virtue* is carried by the floor, not by the cap**, and that is a weaker guarantee: a floor binds only at the bottom, while `tanh` bites everywhere. Registered `P-28` |
| ⭐ **THE WHOLE-SUCCESS-WIDE `Partial` WINDOW** (`0 ≤ margin < 1`) — *"what keeps Partial reachable; on point-equality Partial would essentially never fire against a fractional Ob"* | **`Partial: []` is the speech that moved nothing** — the design's most-needed band, and the fractional-Ob analysis says it only exists because the window is a whole success wide |
| **THE 1D POOL FLOOR** — ruled 2026-09-04, *"1D is floor"*, applied to the **mean as well as the variance** | `§A.2`: *"a person who tries something they are bad at is the engine working."* **An incompetent speaker still rolls** |
| **FRACTIONAL Ob IS STRICTLY MONOTONIC** — `Ob 1.4 ≢ 1.6` | a room is not a step function. **Half a point of resistance is a real difference** |

## C.3 · ⚠ Two things this design must NOT do, both named by the diagnostic

1. **Never route a fractional pool to `roll_pool`.** *"`roll_pool` is the discrete path and keeps
   `int(round(pool))`, correctly — a fractional pool routed to `roll_pool` is a finding"* (**P-v**).
   A proceeding's pool is fractional, so it goes to `continuous_engine_sample`.
2. **Never resolve on `eff_ob()`.** *"`eff_ob()` / `effective_ob()` are DISPLAY ONLY… a caller that
   resolves on `eff_ob` instead of `p_success` has reintroduced the retracted form — **that** is the
   finding to look for."* ⚠ **And it is a live temptation here**, because a player-facing screen wants
   to show *how hard this is* — which is exactly what `eff_ob` is for and exactly what must not decide
   anything.

## C.4 · What is still open, said at the diagnostic's own strength

⚠ **THE OBSTACLE'S DERIVATION IS A RULING AWAITING EXECUTION, NOT AN ACCOMPLISHED FACT.** Jordan ruled
2026-08-14 that an Ob rolled against a character or faction is *"their corresponding score/2 plus
whatever specific modifiers exist for them in that instance"* — and **"every call site in the tree
still passes a hand-set Ob."** So this design **names the derivation and cannot claim it runs**.

**And it must say whose score.** In a contested speech the opposing party's; where nobody opposes — an
audience with a sovereign — **the hearer's**. That is a design call, stated as one, and registered
`P-25`.

⚠ **`P-01` IS THEREFORE REWRITTEN AND LARGELY DISSOLVED.** A draft called the band edges *absent, no
default, a ruling between this and running.* **They are none of those things:** `degree_from_net` is
*"THE ladder, single owner for every scale"*, its four bands are ruled and pinned by a parity golden,
and `H-31` grades the margin model **`assumption` with a default and a four-point sweep** — not
`absent`. **What remains is `P-06`: which `capability` key feeds the pool, and the σ-level magnitudes
— and `ID-6` says inject, declare and sweep those rather than escalate them.** Done at `P-06`.

---

# PART C.5 · **HOW PROBABILISTIC IS IT? — one draw per interaction, and nothing else**

> ### **THE ANSWER: EXACTLY ONE THING IN THIS SUBSYSTEM IS STOCHASTIC, AND IT IS THE DRAW.**

| deterministic | stochastic |
|---|---|
| eligibility — four kinds, a disjunction | |
| `requires` — seven typed forms; a precondition holds or it does not | |
| who is in the room — **whoever travelled** | |
| the arrangement — a data row read at load | |
| the order of speaking — `arrangement.order` | |
| the rung the matter stands at — a fold over this run's own emissions | |
| **refusals** — scarcity, obstruction, an unseated determiner, a speech with no occasion | |
| what WITNESS deposits, to whom, through which channel | |
| the veto — the licence conditions either hold or they do not | |
| | ⭐ **`continuous_engine_sample(pool)` against `base_Ob`, once per interaction** |

**So a six-interaction hearing contains six draws and several dozen deterministic decisions.** The
uncertainty is concentrated at exactly the point the fiction puts it — *how well did that land* — and
nowhere else.

⭐ **AND IT IS SEEDED, SO IT IS DETERMINISTIC ON REPLAY.** The seam seeds from
`H(world_seed, tick, actor, prize, cause)`, following `combat_seam.py`'s discipline — *"a contest is
reproducible exactly as every other draw in this instrument is"*. **The same season replays
byte-identically, including the hash.** Probabilistic in the fiction; deterministic in the record.

> ### **WHY THIS RATIO IS THE RIGHT ONE, AND IT IS THE STUDY'S ARGUMENT RATHER THAN A PREFERENCE**
> The study's central finding is that **the actor's failures are not perceptual and not random** —
> *"the perception is available and does not govern the action."* **A design that rolled for whether
> you noticed the room, whether you remembered the precedent, or whether you kept your temper would
> be modelling the half of the variance that is not there.** What is genuinely uncertain is **how a
> room takes a thing**, and that is one number, drawn once, against a resistance somebody else's
> attributes set.
>
> ⚠ **The honest cost: a player who plays well can still lose every draw**, and the design offers no
> mitigation — no re-roll, no fate point, no escalating bonus. **The soft cap makes that worse on
> purpose**, since advantage saturates at `M_MAX = 1.5`. Whether that is too harsh is a play question
> and `P-26` records it as one.

# PART D · WHAT A LOSS COSTS, AND THE TWO BOUNDS THAT NEED NO MECHANISM

**The `writes` above are the whole of the cost, and the recoverability grading (Figs. 11, 21) is what
decides which write it is.**

| grade | what it writes | why it is that |
|---|---|---|
| **FREE** | **nothing** — the unused proof, the unspent objection, the construction not needed | *"they cost nothing; the corpus holds that they are hoarded"* — an act not taken emits nothing |
| **COSTLY** | `Person.stance`, and claims into every witness's ledger | recoverable at a **visible** price — visible because it was witnessed |
| **TERMINAL** | a `Tenure` closed, or a `commit` severed | **no later step repairs it**, and no interposition absorbs it (Fig. 24) |

## D.1 · The two bounds on reception, which the study adds and which cost nothing

**▣ Bounded by elaboration.** *Position dominates an inattentive room and merely tilts an attentive
one.* **Mechanism: the weight of the reception term scales with the arrangement's attention** — which
is a property the arrangement already carries through `genre` and `latitude`. **No key is added.**

**▣ Bounded in time — and this is free in the most satisfying way.** *"Low standing suppresses
reception NOW and does not reliably suppress it LATER. A speaker with no standing may still place an
argument that outlives the discount on its source."*

> ### **THE MECHANISM IS THAT THE DEPOSIT DOES NOT DEPEND ON THE DEGREE.**
> A speech emits an Event; **WITNESS fans it out to everyone present regardless of how it went**; each
> deposits claims into their own ledger. **So a speaker who is dismissed still puts the claim into
> every ledger in the room** — and what decays afterwards is the claim's **confidence**, on `AX-3`'s
> licensed carve-out (*fading REMOVES, never REVISES*), not its content.
>
> **Nothing is added for this. It is what the loop already does**, and it means the lowest-standing
> person in the room can still change what everybody knows — which is `AX-2` paying for itself, and
> the reason a public debate with `disposal: none` is worth playing.
