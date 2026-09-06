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
pool  =  brought                      -- DERIVED, not a key (§B.1a). A Query over what you hold
                                         on this matter, × `composure`. Always live; never multiplied
                                         by latitude -- preparation survives any room
      +  conduct                      -- DERIVED. `eloquence` × latitude(game), FLOORED (§B.3c),
                                         modulated by your role. Never multiplied to zero
      floored at 1D                   -- ruled 2026-09-04; the MEAN as well as the variance

   -- THREE attributes on the sheet: eloquence · discernment · composure.
   -- `discernment` is NOT DICE. It gates the fidelity of the read (§B.1c) -- the fog of war.
      floored at 1D                   -- ruled 2026-09-04; applies to the MEAN as well as the variance
      fractional throughout           -- continuous_engine_sample, never roll_pool
```

⛔ **AMENDED 2026-09-06 — FOUR KEYS, §B.1a.** This read *"Two `capability` keys … naming two rather
than nine costs nothing and commits to nothing."* **The reasoning was right and the number was a
floor, not a ceiling** — `Person.capability` is a dict whose keys are content, so the cost argument
cuts both ways. Jordan lifted the constraint (*"you're allowed to venture duplicates of what exists
there if it makes sense here"* — the earlier ban was contamination-avoidance, not a design position),
and running the test over this subsystem's own six contested acts returns **three attributes** —
`eloquence` · `discernment` · `composure` — **with `brought` and `conduct` DERIVED from them and from
what the world already holds.** An aggregate cannot be a field, so the two halves of the pool are
Queries and never sheet values.

## B.1a · ⭐ THREE ATTRIBUTES AND TWO DERIVED SCORES — the roster, from this subsystem's own act set (Jordan, 2026-09-06)

> **Jordan, lifting the earlier constraint:** *"we're precluding the existing attribute roster in
> repository to avoid contamination. You're allowed to venture duplicates of what exists there if it
> makes sense here."*
>
> **And naming the surface himself:** *"social attunement/reading the room, comporting oneself
> appropriately, presenting and speaking and acting in a convincing manner, knowing what to expect and
> how to use your evidence and anticipate your opponent's evidence, maintaining composure and dignity
> in light of attack and failures."*

**Two was a floor, not a ceiling — and the two it named were the wrong KIND of thing** — `Person.capability` is a dict whose keys are content, so naming
more costs nothing structurally. **The test a key must pass: two acts in THIS subsystem's own set would
draw differently, and currently draw the same.** Run across the six contested acts, it returns four.

> ### ⛔ **AND `brought` AND `conduct` ARE NOT KEYS. THEY ARE DERIVED.** *(Jordan: "brought and conduct
> are derived scores/aggregates since they involve so many factors that you've identified already like
> standing and amount of evidence etc")*
>
> **The design's own rule forces this and a draft of this section broke it.** An aggregate **cannot be
> a field** — a **Query is its licensed form** (`T-a`, and §B.3's aggregates ruling). `brought` sums
> the claims you hold on this matter, their source and confidence, the records in your hand and which
> proofs this arrangement admits. **Every one of those is already in the world model.** A number on a
> sheet standing in for them is a second home for facts the world already carries.
>
> ⭐ **AND DERIVING IT IS THE BETTER GAME, NOT A CONCESSION:** it makes preparation **something you
> DID in prior seasons** rather than something you bought at character creation. The dossier is real,
> it was assembled by acts, and it can be burned.

**THREE LAYERS, and only the middle one is on the sheet.**

| | | |
|---|---|---|
| **1 · what the world holds** | your claims on this matter (source · confidence · when) · the records you hold · your seat and edges · what the arrangement admits as proof | already in the model |
| **2 · THE ATTRIBUTES** — irreducible, not derivable from world state | ⭐ **`eloquence`** — presenting, speaking and acting convincingly · ⭐ **`discernment`** — whether your live read of this room is true · ⭐ **`composure`** — steadiness: using what you prepared, and holding under attack | **`Person.capability`**, three keys |
| **3 · derived, computed at entry, stored nowhere** | **`brought`** = what you hold **× composure** — *"the ability to make use of what you've prepared, remember it under pressure"* · **`conduct`** = `eloquence` **× latitude** (floored, §B.3c), modulated by your role in the room | **Queries.** The two halves of the pool |

⭐ **`composure` therefore does the work in BOTH halves, coherently:** it is why you can *use* what you
brought, and it is what resists being read and pressed. **That is one quality — self-command — and the
corpus already grades its failure as terminal-once-seen** (*visible effort*, *anxiety displayed*).

⭐ **`discernment` enters NEITHER half.** It is not dice at all — it gates the fidelity of what you are
told about the room (§B.1c). **So of three attributes, one is never rolled.**

**The same shape the design already uses for `standing`** — *a Query, season-local, owned by nobody,
stored nowhere.* `brought` and `conduct` join it.

**Where the five acts land, and four of them needed no new key** — because the study's own two-row
partition had already named those capacities: `examine`, `research` and `reconstruct` are `brought`
(evidential discrimination, memory, inference); `interview` is `conduct` (elicitation). **`surveil` was
the one act neither covered** — *"present at the place, for a declared interval"*, contesting *what is
done unseen*.

> ### ⭐ **AND `surveil` IS COMPOSURE, NOT PERCEPTION.** *(Jordan: "'patient watcher' speaks towards
> composure")*
> **The hard part of surveillance is not noticing — it is STAYING.** Anyone watching a door for a
> season sees who goes through it; what separates people is whether they keep watching, without
> leaving, without being drawn off, without being seen. **That is self-command, and it gives composure
> one coherent shape rather than two stapled together: sustaining, and resisting.**

## B.1b · `conduct` feeds `reception`, with a lag — the brilliant speaker's actual payoff

**`reception` is composed from the hearers' claims about the speaker — and those claims come from what
they witnessed him do.** Every act deposits into every present ledger.

```
conduct  ->  a better band  ->  a better thing witnessed  ->  better claims about you
                                                          ->  a lower `reception` term NEXT time
```

**So `reception` is not your attribute at any instant. It is the accumulated record of your conduct as
other people saw it** — which is precisely where eloquence pays, and it pays across seasons rather than
inside one turn. Mid-run it also compounds: each band deposits as you go.

## B.1c · ⭐⭐ `discernment` IS THE FOG OF WAR — and it gates FIDELITY, never AVAILABILITY

> **Jordan:** *"Why are we not having our attributes act as a 'fog of war' for decision making? Someone
> who is less astute than another may not make the right choice even if they knew the proceeding
> overall."*

⛔ **This corrects a real defect.** A draft of this file held that aptness is *the player's* judgment
rather than the character's — **which means a dull character played by a clever player picks
perfectly.** That is player skill substituting for character skill, and it is not acceptable.

**The lawful fix is not gating options** — `if skill < N: return []` is refused by name (`R-9`).

> ### **EVERY LAWFUL MOVE IS ALWAYS AVAILABLE. `discernment` DETERMINES WHETHER WHAT YOU ARE TOLD
> ABOUT THE ROOM IS TRUE.**
> **And the primitive already exists: `Misread` emits identically to `Read`.** The investigation rows
> deposit at the **same confidence with the wrong value** on a misread — `AX-2` doing real work. **The
> same shape applies to the pre-speech read**, which is Fig. 17's four reads. **The player still
> chooses; they choose on the character's information, because there is no other kind.**

**Three things it reads, all of the form *is what I believe about this room true?*:**

| | Jordan's phrasing |
|---|---|
| **has this body settled · is it attentive · has it already decided** | *"reading the room"* |
| ⭐ **can the opponent run my proof back** — the mirror test, which the player must GUESS | *"anticipate your opponent's evidence"* |
| **which misreading my manner invites HERE** (Fig. 8's 7→7) | *"comporting oneself appropriately"* |

> ### ⭐⭐ **AND THE UI IS THE HALF THAT MAKES IT FEEL LIKE A CHARACTER RATHER THAN A GATE.**
>
> **Jordan:** *"the limitations of the character can impose limitations on the player. with the right
> UI, this will feel natural."*
>
> **This is licensed by `07_THE_GAME.md`'s existing rule rather than an exception to it.** The engine
> owes *the arithmetic of what the character already holds*. **A read is something the character
> holds** — so it is owed, and it is owed **as they hold it**, including when it is false.
>
> **Two rules follow, and the first is the whole discipline:**
>
> 1. ⛔ **A MISREAD MUST BE PRESENTED INDISTINGUISHABLY FROM A TRUE READ.** No hedge, no *"you are not
>    certain"*, no confidence bar. **The moment the UI marks a read as unreliable, the player routes
>    around the character** and the fog is gone. This is the same rule the investigation rows already
>    live under — `Misread` emits identically to `Read`, at the same confidence, with the wrong value.
> 2. **Nothing is greyed out.** Every lawful move stays selectable. What differs between a sharp
>    character and a dull one is **what the room is described as**, not what the list contains.
>
> ⭐ **AND WHAT MAKES THE LIMITATION READ AS CHARACTER RATHER THAN AS PUNISHMENT IS THAT IT CAN BE
> PLAYED AGAINST.** A player who suspects their own read can `interview` someone who was there, send an
> advocate whose discernment is better, or spend a season reaching a bench member before the sitting.
> **A limitation you can act against is characterization; one you can only suffer is a gate.** The
> player learns their character reads rooms badly the way a person does — **by being wrong and finding
> out afterwards** — never by being shown a number.

⚠ **The challenge it has to survive is inside Fig. 17, and the figure splits it for us.** *What kind of
body is this* — expediency to a parliament, fact to a court — is **institutional classification, which
is `brought`.** *Has it already decided* is a live read of **this** room, today. **That is Jordan's
distinction exactly: a person may know the proceeding overall and still misread the one in front of
them.**

## B.1d · `composure` owns `obstinacy`, which the design named and left with no owner

`interview` declares `contests: "a disposition"` **against `obstinacy`** (`04_VERBS.md` §B.3.2) — and
**nothing in the design supplies obstinacy.** It is the defensive half of *"maintaining composure and
dignity in light of attack and failures"*, sitting unclaimed.

**What composure resists:** being read (`interview`), the fear press's habituated boost (§F.2 of
`18_FINDINGS.md`), and a standing band crossing. **What it sustains:** `surveil`.

⭐ **AND LOSING IT IS ITS OWN WITNESSED FAILURE, which the corpus states directly.** Fig. 3's erosion
list carries *"visible effort — TERMINAL once seen"*; Fig. 9's Q1 carries *"anxiety displayed; the
accuser's framing accepted"*. **Composure does not change how a failure is read. Losing composure IS a
failure, and it is witnessed** — which is the corpus's shape #1 (*failure is the move read as a signal
about the mover*) applied to the one attribute that is visible while you use it.

## B.1e · What this roster still refuses

**A per-proceeding skill** — a *negotiation* stat and a *trial* stat is pair-count growth (`§0.06`).
**An office bonus** — a title gates access and shapes how you are read, and never adds dice.
**An `aptness` attribute** — with `discernment` doing the fog of war, aptness stays a term you avoid by
knowing the room, and the knowing is now the character's. **A `reception` attribute** — standing is
what others hold, one ledger at a time, and any of them may be wrong. ⭐ **And `brought` or `conduct`
AS SHEET VALUES** — they are aggregates over standing, evidence, records and role, and an aggregate
that becomes a field is the exact defect `T-a` names.

## B.2 · What this buys, and why it is better than a skill-per-proceeding table

| | |
|---|---|
| ⭐ **it answers Jordan's second question with a derivation rather than a table** | **the pool does not change by proceeding kind. The multiplier does** — and the multiplier is `latitude`, which is itself derived from what the arrangement interposes (`03_PARAMETERS.md` §B.1). **Nothing anywhere branches on a game's name** |
| ⭐ **the interposition price becomes mechanical, and it is the measured one** | Fig. 24: every interposition device moves a setting leftward. ~~**Here it literally multiplies away the half of you that operates in the room.**~~ ⛔ **STRUCK 2026-09-06 — see §B.3c. The measurement says the constrained condition RETAINS ~70% of the person-effect; "multiplies away" overshoots it. It DISCOUNTS that half, and `latitude` is floored.** The leader-effect evidence — *present in autocracies, absent in democracies; 23.8% private vs 16.6% public* — **is a statement about the size of the person-effect, and the person-effect IS the pool** |
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

## B.3b · ⭐ AND THE BRILLIANT SPEAKER IS STILL REWARDED — the ruling changes WHICH brilliance pays, and AMPLIFIES the kind that survives (Jordan, 2026-09-06)

> *"although I still want the brilliant speaker to be rewarded for brilliance"*

**The worry is legitimate and it is sharper than it looks.** Brilliance pays in full wherever latitude
is high — a negotiation and an arbitration both carry `interposed: []`, so `conduct` is entirely live.
But **the high-stakes rooms are the interposed ones**: the trial interposes a person and a procedure,
the tribunal an office and a procedure, the audience heavy staging, the appeal a written-only order.
**If interposition flattened brilliance, the flagship games would reward nothing about the person.**

**It does not, and §B.3a's *preparation game* framing — while true — understates it.**

> ### **INTERPOSITION REMOVES BRILLIANCE-AS-EXECUTION AND LEAVES BRILLIANCE-AS-JUDGMENT ENTIRELY INTACT.**
> The multiplier hits the **pool** — *how much of your capability is present in the room.* It does not
> touch **which move you choose**. And the obstacle is composed of four terms a good speaker can
> *avoid paying*:
>
> | the term | what avoiding it is |
> |---|---|
> | **aptness** | choosing the speech kind this genre and this rung admit. ⭐ **The term is the same size for everyone; the brilliant speaker simply does not pay it** |
> | **proofs told** | knowing which proof to spend, when, and whether they can mirror it |
> | **the rung** | descending only when forced, and never unannounced |
> | **reception** | unchangeable in the room — but changeable in the seasons before it |

**And this is the study's own finding, not an accommodation.** The capacity map says it directly:
*"the bottom row survives a tight arrangement. The top row does not: where latitude is low, capacities
1 and 2 do the work and the rest barely operate."* **Capacity 2 is knowing where on the line you are
standing and which capacities this arrangement leaves live.** That is judgment, and the study puts it
in the row that *survives*.

> ### ⭐⭐ **AND THE MECHANICS AMPLIFY IT RATHER THAN MERELY PERMITTING IT.**
> `Δz = X/(0.8·√pool)` — **an obstacle point moves the band MORE for a small pool than a large one.**
> That is the `1/√pool` asymmetry, and here it works *for* the design instead of against it:
>
> **In a tight room, avoiding an obstacle term is worth MORE than it is in an open one.** The same
> apt-move choice that saves a fraction of a band at a negotiation saves a larger one at a scripted
> audience. **Interposition therefore does not suppress judgment — it raises the price of getting it
> wrong and the return on getting it right.**

**So the duke carried by his rank still loses** — to a speaker with half his pool who picks the apt
move at the right rung with an unmirrorable proof, because the duke pays three terms the other does
not, **and at his opponent's smaller pool those terms bite harder.**

**What is genuinely lost, stated so the ruling is not oversold:** a *performer* — someone whose gift is
bearing, timing and delivery — is muted by a ceremony, and no term gives that back. **That is correct
and it is the device working**: a ceremony exists to make the person matter less, and the corpus's
whole account of interposition is that this is what such rooms are *for*. **The remedy available to
that player is not mechanical — it is to choose a different room, which is the entry decision, the
largest lever in the game.**

⚠ **This is now a load-bearing claim and it gets a falsifier, not a paragraph.** `M-8`: at a fixed
seed, a high-`conduct` speaker taking an INAPT move at low latitude must lose to a low-`conduct`
speaker taking an APT one — **and the margin between them must be LARGER at low latitude than at
high.** If it is not, judgment is not amplified and this section is wrong.

## B.3c · ⭐⭐ `latitude` HAS A FLOOR, AND THE FLOOR IS WHAT THE EVIDENCE SAYS (Jordan, 2026-09-06)

> *"we still need a brilliant speaker to be rewarded because if that is the player who is invested in
> their character being a brilliant speaker, then the game has stripped away their investment"*

**This is correct, it beats §B.3b's answer on its own terms, and checking the evidence shows the fault
was mine rather than the ruling's.** §B.3b says brilliance-as-judgment survives — true, and it stacks
below. But *"choose a different room"* is no answer to a player who built a brilliant speaker and finds
the trial, the tribunal, the audience and the appeal all muting them. **That is stripping an
investment, and the design does not get to call it fidelity.**

> ### **AND IT IS NOT FIDELITY. THE MEASUREMENT SAYS *REDUCED*, NOT *ELIMINATED*, AND I HAD BEEN
> READING IT AS ELIMINATED.**
>
> The one **magnitude** in the corpus is Quigley, Chirico & Baù 2022 (`01_THE_STUDY.md:150-151`):
> private firms **23.8%** of variance in return on assets against public firms' **16.6%**.
>
> ### **16.6 / 23.8 ≈ 70%. THE CONSTRAINED CONDITION RETAINS ROUGHLY SEVENTY PER CENT OF THE
> PERSON-EFFECT.** *(the ~70% figure is one of the numerics the adversarial pass verified against the
> study, `13_ADVERSARIAL.md:82`)*
>
> **That is a modest discount. It is nowhere near an erasure — and a `latitude` that reaches zero
> overshoots the finding it claims to implement.**

⛔ **§B.2's own line is therefore struck as written.** It read *"here it literally multiplies away the
half of you that operates in the room"* — **and "multiplies away" is the overshoot.** The measured
claim is that it *discounts* that half. **Nothing in the corpus measures a person-effect going to zero
in a bounded encounter**; the *"present in autocracies, absent in democracies"* contrast is about
leaders' effects on national outcomes over years, which is not a speaker in a room and cannot carry a
zero here.

> ### **SO: `latitude ∈ [LATITUDE_FLOOR, 1]`, with the floor injected, declared and swept — and the
> sweep's centre is the measured ~0.7, not 0.**
> A brilliant speaker **keeps most of their brilliance in every room in the catalogue**, including the
> most heavily interposed one. **Their investment is discounted, never stripped.**

**This is the same shape as the two floors the design already has** — the 1D pool floor on the mean as
well as the variance, and canon's obstacle floor of 1. **A quantity that can reach zero deletes a
player's choices; this design floors such quantities on principle, and `latitude` was the one place it
had forgotten to.**

**What now stacks, in order, for a player who built a brilliant speaker:**

| in the most interposed room in the catalogue | they keep |
|---|---|
| **the pool** | ⭐ **~70% of their conduct advantage** — the measured discount, not an erasure |
| **the obstacle** | **every term they avoid by judgment** — aptness, the proof they chose, the rung they held (§B.3b) |
| **the leverage** | the σ-channel, **uniform at every pool size**, bought with a debt they opened |
| **the entry** | the choice of room, the arbiter, whether to go or send — the largest lever in the game |

⚠ **M-8 is extended accordingly, and it is the falsifier for Jordan's constraint stated exactly:**
**the high-`conduct` speaker must beat the low-`conduct` one at EVERY latitude including the floor**,
all else equal. If they do not, the floor is too low. **A player's investment showing up nowhere is a
failure of the design, not a finding about interposition.**

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

## C.1 · The shape — **RULED: the terms compose the obstacle, and as of the pool-only ruling there are FOUR**

> **Jordan, on the original five-term model:** *"your presentation of obstacle makes sense to me."*

**So the terms are obstacle composition, and they are floored at 1.** ⛔ **They were five; `latitude` left for the pool on 2026-09-06 (§B.3c), so there are FOUR.** That is the ruling; it is
implemented here; and the section below records what remains genuinely constrained and what would show
the call wrong.

```
pool      = the actor's capability          FRACTIONAL · floored at 1D · continuous_engine_sample
base_Ob   = the opposition's corresponding score / 2
         ⛔ ± latitude -- REMOVED 2026-09-06 by the pool-only ruling (§B.3c). Latitude
            multiplies `conduct` in the POOL and appears here NO LONGER; carrying it in
            both places was option B, the double-count. FOUR room terms remain.
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
exist for them in that instance**"* (Jordan, 2026-08-14). Four named modifiers, each sourced to a
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
