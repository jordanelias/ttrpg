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

# PART B · EFFICACY — the pool, and why a seat is not in it

> **`§A.2`: eligibility is never capability. Skill decides how WELL a thing goes, never whether it may
> be attempted.** And `§D.1.1`: `capability` *"supplies dice at RESOLVE and gates nothing."*

**Jordan's word is *efficacy*, and it maps exactly onto the one thing `capability` is licensed to
do.** No new attribute carrier is proposed: `Person.capability` is already a dict on the class
(`shape.py:2368`), and **which keys it carries is content by `ID-12`.**

```
pool(actor, act)  :=  capability[<the key this act draws on>]   +  the draw
```

⚠ **THIS DESIGN NAMES NO CAPABILITY KEYS AND SUPPLIES NO WEIGHTS.** The study is explicit that it
records failure *types* exhaustively and *frequencies* not at all, and that no located work supplies
numbers for these steps. **Inventing a rhetoric stat here would be the fabrication `§0.1` point 4
exists to catch.** Registered `10_LOOPS_AND_GAPS.md` `P-06`, `assumption`-grade, with an injection
site and a three-point sweep (`ID-6`).

## B.1 · Where a title enters — and it is NOT the pool

**`§A.3` is categorical: *a seat adds no verb and no modifier*, because *"the moment a seat carries a
modifier, the seat is a stat, and taking the seat becomes an optimisation rather than a political
act."*** And `§D.7`: **there is no `Title` type** — a title *is* a rank, which is the ordinal of a
seat's domain in the containment roster.

**So a title cannot make a person speak better. Jordan's direction is that it affects *standing and
influence*, and both of those are the HEARER'S side of the exchange, not the speaker's.**

| the study says | the mechanism |
|---|---|
| Fig. 1: standing determines **whether either of the other layers gets a hearing** | rank enters the **obstacle**, never the pool |
| Fig. 3: an ascribed position is **contested procedurally, before any content** — seating, order of speaking, forms of address | `arrangement.order: rank` sorts the nested run **by the ordinal**. *"Precedence is a public ruling delivered without a word"* |
| ▣ bounded by elaboration: **position dominates an inattentive room and merely tilts an attentive one** | the weight rank carries in the obstacle is scaled by how much the room is **attending**, which is a property of the arrangement |
| ▣ bounded in time: **low standing suppresses reception NOW and not reliably later** | ⭐ §D below — and it needs no mechanism at all |

> ### **SO A TITLE BUYS TWO THINGS AND NEITHER IS A BONUS.**
> **It buys ORDER** — where you are called, which at a rank-ordered proceeding is a public ruling on
> your standing before you say anything. **And it buys RECEPTION** — the obstacle your speech faces
> before hearers who read that rank off you. **Neither touches your pool, and a fool with a duchy is
> still a fool who is heard first.**

---

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

## C.0 · ⚠ **THE FIRST VERSION OF THIS PART WAS THE DEFECT THE ENGINE EXISTS TO KILL**

A published draft wrote:

```
margin := pool(speaker) − obstacle(latitude, reception, the rung, register fit, proofs told)
```

**Five terms, all modifying the obstacle. That is the retracted form, and it is retracted by name.**

> `§11.2`: **"ADVANTAGE IS A μ-SHIFT. IT IS NOT AN Ob REDUCTION… `base_Ob` and TN are never
> modified."** The earlier `Eff_Ob = base_Ob − eff_σ·σ_N` form *"drove effective Ob below 1, violating
> P-232 (Ob minimum 1)"* and was **F1, resolved by ED-884.** *"Treat a document that describes
> advantage as an Ob reduction as **stale**."*
>
> And the failure mode is exact: **"a flat `+X` to net or `−X` to Ob that is not σ_N-scaled gives
> `Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools, the exact non-uniformity this engine exists to
> kill, re-imported through a bonus."**

⭐ **AND THE DIRECTION OF THE ERROR IS THE OPPOSITE OF WHAT THE STUDY SAYS.** A flat obstacle reduction
is **strongest for the weakest speaker**. The study's finding is the reverse — *"position dominates an
inattentive room and merely tilts an attentive one"* — so the draft's model would have made a title
disproportionately powerful in exactly the rooms where the study says it counts least. **The engine's
uniformity is not a constraint on the design here; it is the design's own claim, already enforced.**

## C.1 · The correct shape — one draw, and the five terms are σ-LEVELS

```
pool       = the actor's capability                    FRACTIONAL · floored at 1D · continuous_engine_sample
base_Ob    = the opposing side's corresponding score / 2, plus specific modifiers   ⚠ NEVER MODIFIED
net_σ      = levels_to_net_sigma(advantages, disadvantages)      ⭐ THE FIVE TERMS LIVE HERE
net_boost  = soft_cap(net_σ) · σ_per_die · √N          soft_cap(σ) = M_MAX·tanh(σ/M_MAX), M_MAX = 1.5
p_success  = 1 − Φ( (base_Ob − (μ·N + net_boost)) / (σ_per_die·√N) )
margin     = net − Ob   →   degree_from_net   →   Overwhelming | Success | Partial | Failure
```

**So the five things a draft called obstacle terms are five signed σ-levels**, aggregated by
`levels_to_net_sigma`, boosting the **roll**:

| σ-level | sign | source |
|---|---|---|
| **latitude** | − as interposition rises | Fig. 4, derived from `interposed[]` |
| **reception** | + or − | Fig. 3 + Fig. 25 — what the hearers read off the speaker, **including rank** |
| **the rung** | + as the ladder is descended | Fig. 5 — a lower rung is a smaller claim |
| **register fit** | ± | Fig. 8 |
| **proofs told so far in this run** | + | Fig. 6 + `S8` |
| **the licence veto** | ⚠ **not a σ-level — a DEMOTION** | Fig. 26. `§E.3`: an extension may only narrow |

## C.2 · What the engine gives this design for free, and it is a great deal

| the engine already does | the study already wanted it |
|---|---|
| ⭐ **UNIFORM LEVERAGE.** `σ_per_die·√N` cancels in the z-score, so **`Δz = soft_cap(net_σ)` at every pool size and every TN** — measured `Δz = 0.874174` across pools {0.5, 1, 4, 9, 16, 25} at `net_σ = 1.0` | **a title changes WHETHER YOU ARE HEARD, not how well you speak.** Fig. 1's three layers, enforced arithmetically: an advantage helps a poor speaker exactly as much as a good one |
| ⭐ **THE SOFT CAP.** `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` — advantages **saturate** | ⭐ **THIS IS OVERSHOOT, ALREADY IN THE ENGINE.** `S3`: the named fault across seven traditions is *excess of a virtue*. Past the cap, piling on buys **nothing**, and the scene was still spent |
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
