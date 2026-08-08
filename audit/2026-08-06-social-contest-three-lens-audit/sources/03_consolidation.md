# Consolidation — From Research to Encodable Systems
## Third document. Supersedes the mechanics of the first two; their research stands.

**On the requested handoff.** I can't route work to Claude Fable 5 and back to Opus 5. There's no tool in this session that dispatches to another model, and nothing in this conversation can hand a task to a different one — you're talking to Opus 5 throughout, and a Fable 5 request would in any case be liable to route back here under Anthropic's safeguards. More to the point, I shouldn't stage it. Labelling my own audit as an independent model's would manufacture exactly the false independence that the previous two documents flagged as `[SELF-AUTHORED — bias risk]`, and it would make the audit *less* trustworthy, not more. So §1 is a self-audit, tagged as one, and it names at the end what a genuinely independent reviewer would catch that I structurally cannot. If you want real independence, run this document past a separate session with no prior context and no attachment to the earlier work.

**What changed.** Single player. The player is one character whose authority varies — they may bind themselves, a settlement, a house, or a faction. That constraint is not a detail; it invalidates one mechanism outright, promotes a latent idea to the spine of the design, and makes the distillation below mandatory rather than desirable.

---

## §1 — Read-only audit of documents 1 and 2

`[SELF-AUTHORED — bias risk]` No changes made in this section. Findings ranked by consequence under the new constraint.

### Severe

**F1 — There is no mechanism for authority, and the brief now demands one.**
Both prior documents silently assume the player *is* the deciding body: they frame the *relatio*, they hold the veto, they order the survey. A character who "may have the authority to represent a settlement, a house, or a faction" is a different object. Nothing in P1–P45 answers: *may this character bind that body to this?* The nearest thing is the envoy-mandate gap in S8, which the second document correctly called "the component's central tension" and then confined to diplomacy. It is not a diplomacy mechanic. It is the game's spine. **This is the largest hole in the corpus.**

**F2 — P45 Shared Loss is invalid as specified.**
Finding A9 flagged it; the single-player confirmation kills it. Shared loss works in *The Republic of Rome* because it disciplines other humans who would otherwise obstruct forever. With one human, "the polity can fail and you lose" is a difficulty timer wearing a political costume — it disciplines nobody, because the AI factions have no reason to relent unless something makes them relent. The mechanism has to be rebuilt at the opposition layer, not the rules layer. §9 does that.

**F3 — Forty-five primitives, eight state graphs, and no resource economy is not encodable.**
Finding A5 was left open and it blocks everything downstream: P40 side payments and P44 positional pricing both presuppose a currency that was never defined, and P8's "costs an action" and P17's "consumes a session slot" were never established as the same or different resources. §3 closes this.

### High

**F4 — Most of the forty-five are configuration, not mechanism, and the corpus never says which.**
This is the finding that makes consolidation possible. P37 Split Command is not a rule; it is *a territory whose governing body has two seats with different competences*. P36 Charter is not a rule; it is *the configuration a body is given on acquisition*. P25 Quota is a field on a selection procedure. Presenting these at the same level as P7 Attack, which is a genuine branching resolution, made the design look like forty-five systems when it is closer to fourteen with thirty-one data tables. §2 performs the separation.

**F5 — The three role-shifting primitives demand three presentations each and the corpus budgets for one.**
Document 2, Finding 8: P1, P2, P3, P35 change role between systems. Standing is a modifier in seven systems and a gate in one; precedence is a state in diplomacy, a guard in parliament, a modifier elsewhere. Left as-is, each needs separate interface treatment. The fix is not to accept three presentations but to move the shift into *body configuration*, so that "standing gates entry here" is a property of the tribunal rather than an exception in the standing rules. §2 does this.

**F6 — S9 Selection is still missing.** Four graphs open with a stub; P4 and P24 are unreachable. Folded in as M14.

### Medium

**F7 — The enactment clock's numbers are Victoria 3's and were never re-derived.** Finding A4 stands, unaddressed. 100-day stages are wrong for a city council with two-month magistracies. §6 gives the structure with the parameters explicitly marked untuned.

**F8 — A2 is worse in single-player, not better.** The Inquisition's hidden evidence array was defended on the grounds that deduction is the defence's real game. Against a human inquisitor, guessing is social. Against an AI, an inferable array must be *authored* to be inferable, every time, or it reads as arbitrary. The abjuration ladder must therefore be visible at all times — asserted in document 2, still not specified. §7 specifies it.

**F9 — The three clusters share only two primitives, so "one vocabulary" was true but misleading.** Adjudication, administration, and exchange share standing and the record and nothing else. Document 1's composition rule 1 implied more unity than exists. §2's answer is that they share an *object* rather than a verb — see M3.

### What the audit did not break

- **The historical research.** Nothing in document 1's §2 was found wrong. Stasis theory, the Venetian selection chain, *senatus auctoritas*, *piaoni*, the *missi*/*Sindici*/censor convergence, the *kandaka*→*kokudaka* shift, capitulary non-compliance, Ostrom's detection-versus-severity result — all sourced, all load-bearing, all survive.
- **The three-attack structure (P7).** Attacked as over-engineered for a single-player game; it holds. It is the only defence against the documented Burning Wheel collapse, and against an AI opponent it is *more* necessary, not less, because an AI will always find the dominant verb.
- **The record spine (P16).** Attacked as bookkeeping; it holds. It is the mechanism by which a single-player campaign accumulates political texture, and it costs almost nothing.
- **The call graph.** Attacked on the grounds that the calls might be cosmetic; they are not. Negotiation genuinely is a subroutine with three callers, and the S2↔S5 cycle genuinely is the design's most interesting structure.

### What an independent reviewer would catch and this pass cannot

1. **Whether any of this is fun.** Every audit so far has asked whether the design is historically true, internally consistent, and encodable. None has asked whether a player wants to spend forty hours doing it. That question is unanswerable from inside the design.
2. **Whether the stasis loop survives contact with an AI opponent.** I have argued twice that it does. I have no evidence. It has never been played.
3. **Whether the consolidation below is a distillation or an amputation.** I performed both the original expansion and this contraction; I am the wrong process to judge whether the thirty-one demoted primitives lost anything real.

---

## §2 — The distillation: fourteen mechanisms, thirty-one configurations

The separation rule, applied to every one of the forty-five:

> **A mechanism is code: it takes inputs and branches. A configuration is data: it sets a field on a mechanism.**
> If it can be written as a row in a table, it is not a mechanism.

All forty-five are accounted for — verified by script, no duplicates, no orphans.

| # | Mechanism | Absorbs | What it is |
|---|---|---|---|
| **M1** | **Standing** | P1 | Weight an actor carries in a named body. Per-body, spendable, earned. |
| **M2** | **Scope** | *(new)* | What this character may bind. The spine. See §4. |
| **M3** | **Concealed Value** | P11, P28, P31, P39 | Every contest has a hidden true number; actors hold an estimate with a band. |
| **M4** | **Probe** | P8, P29, P30 | Spend time to narrow one band. Critical question, inspection circuit, and sealed enquiry are one verb at three scales. |
| **M5** | **Claim** | P6 | Proposition with premises, warrant, provenance. |
| **M6** | **Attack** | P7 | Undermine, rebut, undercut. Three kinds, structurally distinct. |
| **M7** | **Gate** | P5, P9, P10, P19 | The ordered question stack, the burden token, the competence check, and the escape to another forum. |
| **M8** | **Floor** | P2, P12, P13, P14, P17, P20 | Who convenes, who frames, who speaks when, what gets put, who drafts, and the finite slot budget. |
| **M9** | **Block** | P15, P21 | Refusal to let a thing proceed. Veto and return-unsigned. |
| **M10** | **Record** | P3, P16 | Everything emitted, everything citable. A commitment is a record you made about yourself. |
| **M11** | **Clock** | P18, P26 | Durations at three tiers: session, enactment, term. |
| **M12** | **Compliance** | P32, P33, P34, P36 | Declare → decree → roll → detect → sanction, against a charter. |
| **M13** | **Settlement** | P35, P40, P41, P42, P43, P44 | Reservation, payment, scaled compromise, and the bind-or-not instrument choice. |
| **M14** | **Selection** | P4, P22, P23, P24, P25, P27 | How a body is constituted, and what investiture confers. |

**Demoted to configuration** (not lost — relocated):

| Was | Now |
|---|---|
| P2 Precedence | An ordering field on `Body.floor.order` |
| P3 Commitment | A `Record` with `subject = self` |
| P4 Immunity | An `Office.immunities` list, granted by M14 |
| P9 Burden | A `Gate.burden` field, set per body |
| P10 Forum Challenge | A `Gate` transition available when `Body.appealsTo` is non-empty |
| P19 Competence | A `Body.competences` set |
| P20 Drafting | An `Office.floorRole = drafter` |
| P22–P25, P27 | Fields on `Body.selection`: `method`, `threshold`, `quota`, `avoidance` |
| P26 Term | `Office.term`, a Clock tier |
| P28 Relazione | A `ConcealedValue` estimate object with slow decay and an owner |
| P29 Circuit | A `Probe` with `scale = territory` |
| P30 Sealed | A `Probe` with `visibility = sealed` |
| P34 Sanction | A `Compliance.sanctionLadder` table |
| P35 Hostage | An `Instrument` of `type = bond` |
| P36 Charter | The configuration a `Body` receives on acquisition |
| P37 Split Command | A `Body` with two `Office` seats of differing competence |
| P38 Nested Layers | `Body.parent` — a tree, not a mechanism |
| P42/P43 | `Instrument.binding` — false is the default (cheap talk), true requires a bond |
| P44 Positional Pricing | An `OfferArray.pricing = positional` flag |
| P45 Shared Loss | **Deleted.** Replaced by the faction model in §9. |

**The consequence.** Fourteen resolution functions and a set of data tables replaces forty-five prose entries and eight graphs. F5 dissolves: standing does not "shift role" — the tribunal simply has `entryGate: standing >= n` in its configuration, and the standing mechanism never learns about tribunals.

**Finding F9's answer.** The three clusters share standing and the record as *verbs*, but all three are built on M3 Concealed Value as an *object*. The hidden evidence array, the gap between declared and true yield, and a negotiator's private reservation value are the same thing in three costumes. That is why the clusters felt unrelated while behaving alike: they share a noun, not a verb. Unifying them on M3 is the single largest simplification in this document.

---

## §3 — The economy (closes A5)

Four resources. Nothing else is spendable.

| Resource | Fungible | Scale | Spent on | Earned by |
|---|---|---|---|---|
| **Time** | yes, universally | Segments. 1 hearing exchange = 1 segment; 1 floor speech = 1; 1 territorial circuit = 12 | Every action without exception | Never earned. Only allocated per Clock tier. |
| **Standing** | **no** — indexed per body | 0–100 per `(actor, body)` | Entry gates, blocks, calling out of turn, forcing a division | Winning a gate, honouring a record, vindication after inspection |
| **Coin** | yes | integer | Side payments, offices, bonds, campaigns, surveys | Assessment yield, trade, confiscation |
| **Obligation** | **no** — directional and personal | a debt from A to B, with a magnitude and an age | Nothing. Calling one in is **free** and **destroys it** | Doing something for someone at a real cost |

**The three rules that make this an economy rather than four counters:**

1. **Time is the only universal cost.** Every mechanism's actions cost segments and nothing else. This makes scarcity legible and makes M8's finite slot budget bite everywhere, not just on the floor.
2. **Standing does not convert to Coin and Coin does not convert to Standing** — not directly. Coin buys a *side payment* (M13), which buys an *outcome*, which may earn Standing. The laundering step is the game. A design that lets money buy respect has no politics in it.
3. **Obligation is the only resource that is destroyed by use and cannot be bought.** It is what makes a character worth knowing. Calling in a favour is free at the moment of use and costs you the favour forever, which is the correct shape: the reason you hesitate is that you only have one.

**Segment budget per Clock tier** — the numbers below are `[UNTUNED]` and exist so the structure is testable, not because they are right:

| Tier | Container | Segments | Refills |
|---|---|---|---|
| Session | one sitting of a body | 6–12, set by `Body.floor.slots` | On convening |
| Enactment | one measure in passage | 3–6 stages, 1 decision each | Per stage |
| Term | one office | 4–24 sessions, set by `Office.term` | On investiture |
| Life | one character | mortality roll from age | Never |

---

## §4 — M2 · Scope: the spine

Every binding act carries a scope. The player's character holds a **mandate** for each body they are attached to, and the mandate says what they may bind that body to without going back for authority.

```
Scope = SELF | SETTLEMENT | HOUSE | FACTION
```

| Scope | May bind | Repudiation looks like | Failure mode |
|---|---|---|---|
| **Self** | Own person, own coin, own standing | Impossible — you are the principal | Ruin is personal and total |
| **Settlement** | Local compliance, local declaration, local militia | Council disavows the agreement; the charter is unchanged | You are removed from the seat |
| **House** | House coin, marriages, bonds, house votes | Head of house repudiates; the counterparty keeps what they were given | The house disowns you; standing collapses in every body |
| **Faction** | Treaties, factional votes, war and peace | Faction assembly refuses ratification | Faction splits; you keep one fragment |

**The mechanism.**

```
bind(actor, body, terms):
    m = actor.mandate[body]                  # {scope, limits, expiry}
    if terms.within(m.limits):
        return BOUND                          # instrument takes effect immediately
    else:
        risk = repudiationRisk(body, terms, actor.standing[body], actor.records)
        return PROVISIONAL(risk)              # takes effect, may be reversed
```

A provisional binding is **live** — the counterparty acts on it. If the body later repudiates, the counterparty keeps whatever was already transferred and the actor eats the consequences. This is the envoy who exceeds his instructions, generalized to every scale.

**Why this is the spine and not a feature.** Single player removes the opponent's cunning as the source of tension. What replaces it is *whether you can deliver what you promise*. Every negotiation, every treaty, every charter concession, every vote you pledge becomes a question about your own authority rather than about your opponent's. That is the correct tension for a character-scoped political game, and it is the only thing in this design that gets *more* interesting without a human across the table.

**Scope changes during play.** Rising from Self to House to Faction is the campaign arc. M14 Selection is how it happens; M10 Record is how it is lost.

---

## §5 — Data schemas

Written to be encoded directly. Enums in caps; optional fields marked `?`.

```
Actor {
  id
  house?              : HouseId
  age, mortalityBase
  offices             : [OfficeId]
  standing            : Map<BodyId, 0..100>
  mandate             : Map<BodyId, Mandate>
  coin                : int
  obligations         : [Obligation]        # both directions
  aims                : [Aim]               # 2-3; drives AI, shown for the player
  estimates           : Map<CVId, Estimate> # what THIS actor believes
}

Mandate { scope: SCOPE, limits: [LimitClause], expiry: ClockRef }

Obligation { from: ActorId, to: ActorId, magnitude: 1..3, incurredAt: ClockRef }

Body {
  id, parent?         : BodyId              # replaces P38 Nested Layers
  members             : [ActorId]           # ordered — see floor.order
  competences         : [COMPETENCE]        # replaces P19
  appealsTo?          : BodyId              # enables the forum escape in M7
  entryGate?          : Predicate           # e.g. standing >= 40 — replaces the P1 role-shift
  charter             : Charter             # replaces P36
  selection           : Selection           # replaces P22-P25, P27
  floor               : Floor               # replaces P2, P12, P13, P14, P17, P20
  gate                : GateConfig          # replaces P5, P9
  blocks              : [BlockRight]        # replaces P15, P21
}

Selection {
  method              : LOT | ELECTION | ALTERNATING | APPOINTMENT | HEREDITARY
  chain?              : [ChainStep]         # for ALTERNATING — the Venetian sequence
  threshold           : Fraction            # supermajority
  quota?              : {perHouse: int}
  avoidance           : bool                # barred where the holder has interests
  term                : ClockSpan
  confers             : [Immunity | Power]  # replaces P4
}
ChainStep { op: NARROW | WIDEN, method: LOT | ELECTION, from: int, to: int }

Floor {
  slots               : int                 # the scarce container
  order               : PRECEDENCE | SENIORITY | RANDOM | CHAIR
  convener            : [OfficeId]
  framer              : [OfficeId]
  drafter?            : OfficeId
  chairPutsMotions    : bool                # if true, motion order is a CHOICE
}

GateConfig {
  stases              : [CONJECTURE, DEFINITION, QUALITY, JURISDICTION]  # ordered subset
  burden              : ACCUSER | RESPONDENT | NONE | LOWER_STANDING
  escapeAllowed       : bool
}

Claim {
  id, proposition
  stasis              : STASIS
  premises            : [PremiseId]
  warrant             : SCHEME             # EXPERT | WITNESS | DOCUMENT | SIGN | PRECEDENT | CONSEQUENCE
  provenance          : CVRef              # what is concealed about its source
  vulnerabilities     : derived from warrant — see §6.2
}

ConcealedValue {                            # M3 — the unifying object
  id
  trueValue           : number | ItemSet
  kind                : EVIDENCE | YIELD | RESERVATION | DISPOSITION | CONDITION
  attributes          : [Attribute]         # each probeable separately
  decay               : rate                # estimates widen over time
}
Estimate { low, high, lastProbedAt: ClockRef, source: ActorId? }

Record {
  id, subject: ActorId | BodyId
  kind                : VERDICT | MOTION | OATH | INSTRUMENT | FINDING | REPUDIATION
  status              : IN_FORCE | VETOED | SUPERSEDED | BROKEN
  body, clockRef
  citableAs           : [STASIS]            # which stasis it can be played at later
}

Instrument {                                # M13 output
  terms, parties
  binding             : bool                # false = cheap talk (default)
  bond?               : {type: HOSTAGE|COIN|MARRIAGE|OATH, value, heldBy}
  scope               : SCOPE               # from M2 — what was actually bound
  provisional         : bool                # true if it exceeded the mandate
}

Charter {                                   # replaces P36; configures a governed body
  preservedBodies     : [BodyId]            # indirect rule
  declaredFields      : [FIELD]             # what the locality must report
  obligations         : [Obligation]
  sanctionLadder      : [Sanction]          # graduated — replaces P34
  detectionRate       : 0..1                # player-set, trades against severity
}
```

**Note on `estimates`.** Every actor holds their own estimate of every concealed value they have any line on. This is one map per actor, not a global fog — it is what makes M4 Probe meaningful and what makes a stolen *relazione* worth stealing.

---

## §6 — Resolution functions

Fourteen. Every one takes an actor, a body, and a cost in Time, and returns a state change plus zero or more Records.

### 6.1 M1 Standing · M10 Record

```
standing(actor, body) -> 0..100
  base = office weight + house weight in this body
  + Σ records where subject == actor and status == IN_FORCE and body in record.audience
  - Σ records where subject == actor and status == BROKEN
  ± obligations owed to members of this body
```

Standing is derived, not stored. **Records are the ledger.** A commitment kept raises it in every body that witnessed the record; a commitment broken lowers it in every body that can cite the record. This is why M10 absorbs P3: honouring or breaking a commitment is a status change on a record, and the standing function reads it for free.

```
cite(actor, record, stasis) -> Claim
  requires record.status != SUPERSEDED
  requires stasis in record.citableAs
  cost: 1 segment
  yields a Claim with warrant = PRECEDENT and provenance = public (unconcealed)
```

**A vetoed motion is citable and has no force.** That is the whole of *senatus auctoritas*, in two lines.

### 6.2 M5 Claim · M6 Attack — the anti-collapse table

Each warrant scheme is vulnerable to a different attack. **This table is the design.** It is the reason no single verb dominates, and it is the direct answer to the documented Burning Wheel failure.

| Warrant | Undermine (hit a premise) | Rebut (hit the conclusion) | Undercut (hit the inference) |
|---|---|---|---|
| **WITNESS** | **strong** — the witness was elsewhere, is interested, is unreliable | weak | moderate — testimony of this kind proves less than claimed |
| **DOCUMENT** | moderate — the document is forged, altered, misdated | weak | **strong** — the document says something, but not this |
| **EXPERT** | weak | weak | **strong** — the authority is out of field, disputed, or biased |
| **SIGN** (inference from circumstance) | moderate | moderate | **strong** — the sign admits another explanation |
| **PRECEDENT** | weak | **strong** — a contrary precedent, later or higher | moderate — the case is distinguishable |
| **CONSEQUENCE** (this will lead to X) | moderate — the causal premise fails | **strong** — a worse consequence the other way | moderate |

```
attack(actor, claim, kind) -> outcome
  cost: 1 segment
  eff = table[claim.warrant][kind]                    # STRONG | MODERATE | WEAK
  roll = standing(actor, body) modifier + eff modifier
  on success:
    UNDERMINE -> remove one premise; claim survives if others remain
    REBUT     -> both claims stand; body weighs them at resolution
    UNDERCUT  -> premises stand and stop supporting the conclusion
  on failure: burden does not move; 1 segment lost
```

**Authoring invariant, from finding A1.** In any hearing's claim draw, no single attack kind may be optimal for more than 40% of claims. Enforce at content-build time; this is checkable by script and should be.

### 6.3 M3 Concealed Value · M4 Probe

```
probe(actor, cv, attribute, mode) -> narrows actor.estimates[cv]
  cost: by scale
    QUESTION  1 segment      # a critical question at the table
    ENQUIRY   1 segment      # sealed; deniable; result is private
    CIRCUIT   12 segments    # an inspection tour; result is public and performs legitimacy
  narrowing = f(actor's competence, cv.attributes[attribute].opacity, mode)
  if mode == CIRCUIT: also emit Record{kind: FINDING} and raise local legitimacy
  if mode == QUESTION: also move the Gate burden to the questioned party
```

One verb, three scales. The critical question, the sealed denunciation, and the *Sindici Inquisitori* circuit differ only in cost, visibility, and side effect.

```
decay(cv, elapsed): estimate.band widens by cv.decay * elapsed
```

Decay is what makes the standing report worth maintaining and what makes yesterday's intelligence a liability.

### 6.4 M7 Gate

```
gate(body, contest):
  s = contest.stases.head
  loop:
    actor = whoever acts
    action in {playClaim, attack, probe(QUESTION), escape}
    if action == escape:
       requires body.gate.escapeAllowed and body.appealsTo != null
       concedes every stasis already passed
       move contest to body.appealsTo, reset to JURISDICTION, re-evaluate claims
    if both sides pass or the burden holder cannot act:
       resolve s in favour of the non-burden holder
       if accuser carried: advance to next stasis
       else: terminate in respondent's favour
```

Burden placement is `body.gate.burden`. Four values give four wholly different scenes with one function:

- `ACCUSER` → accusatorial court
- `RESPONDENT` → inquisitorial hearing
- `LOWER_STANDING` → political tribunal
- `NONE` → **negotiation.** With no burden token, the gate stops adjudicating and starts sequencing an agenda: is there a dispute, what is it about, what is it worth, who may settle it.

That last line is the finding from document 2 §11 made executable. **Negotiation is not a separate system.** It is `gate()` with `burden = NONE` handing off to `settle()`.

### 6.5 M8 Floor · M9 Block

```
floor(body, session):
  slots = body.floor.slots
  convene: requires actor.office in body.floor.convener
  frame:   requires actor.office in body.floor.framer
           -> sets the question; may attach a draft (if body.floor.drafter)
  while slots > 0:
    speak(full)      -> 1 slot, plays a Claim
    assent(speaker)  -> 0 slots, adds standing weight to that motion
    consume()        -> 1 slot, adds nothing        # obstruction
    callOutOfTurn(x) -> 1 slot, costs standing, honours or slights x
    putMotion(m)     -> if body.floor.chairPutsMotions: CHAIR CHOOSES which and in what order
  slots exhausted -> session expires, business dies
```

`chairPutsMotions` must never be automated. It is the chair's principal power and the reason the office is worth holding.

```
block(actor, target) -> Record
  requires right in body.blocks with scope covering target
  cost: standing, always non-zero
  VETO           -> target carried but status = VETOED; citable, no force
  RETURN_UNSIGNED-> target not transmitted; actor takes a personal risk roll
                    (the low-ranking refusal aimed upward)
```

### 6.6 M11 Clock

Three tiers, running concurrently and deliberately out of phase.

```
tick():
  session.slots--                                  # minutes
  for each enactment e: e.stage()                  # months
  for each office o: o.term--                      # years
  for each actor a: mortalityRoll(a)               # a life
```

```
enactment.stage():                                  # [UNTUNED — see F7]
  success += Σ clout(supporters);  stall += Σ clout(opponents)
  duration *= measureClassMultiplier / legitimacyFactor
  if stallRoll(): setbacks++
  if setbacks >= cap: FAIL, lock this measure for cooldown
  mobilisation += attemptPressure       # attempting a reform grows its opposition
  if mobilisation > threshold: escalate to the faction model (§9)
```

### 6.7 M12 Compliance

```
cycle(territory):
  declare()      -> locality reports declaredValue; trueValue is a ConcealedValue
  assess()?      -> optional; costs coin + segments; provokes resistance from
                    everyone whose declaration was understated; on success the
                    declared value is replaced by a survey figure
  decree(rule)   -> promulgates; NO direct effect
  for each locality:
     comply = roll(disposition, distance, agent present, bond held, standing)
     -> COMPLIANT | EVADING (undetected) | DEFIANT (open)
  probe(CIRCUIT) -> reveals the declared/true delta on EVADING localities
  sanction(delta)-> charter.sanctionLadder, graduated by seriousness and context
```

**The dial that matters.** `charter.detectionRate` is player-set. High detection permits low, cheap sanctions and yields stability; low detection forces savage sanctions and yields less stability for more cost. Make both visible. This is Ostrom's result and it is the design's clearest piece of procedural argument.

### 6.8 M13 Settlement

```
settle(parties, contest) -> Instrument
  each party has a ConcealedValue of kind RESERVATION
  offer/counter: 1 segment each
  sidePayment(coin | office | marriage | precedence):
      requires target position is buyable — SOME ARE NOT (see §9 aims)
  overlap = testOverlap(reservations)               # private to each party
  if no overlap: IMPASSE
      the only exit is to change an outside option, WHICH CANNOT BE DONE AT THE TABLE
  on agreement:
      terms = scaleCompromise(terms, costPaidByWinner)
      binding = false                               # DEFAULT
      if a bond is lodged: binding = true
      scope, provisional = bind(actor, principal, terms)   # M2
```

Three rules, in priority order: **non-binding is the default**; **impasse is broken elsewhere, not here**; **the winner concedes in proportion to what winning cost.**

### 6.9 M14 Selection

```
constitute(body):
  match body.selection.method:
    LOT          -> draw from eligible pool
    ELECTION     -> vote; requires threshold
    APPOINTMENT  -> by an office with the competence
    HEREDITARY   -> by house succession
    ALTERNATING  -> for step in chain:
                      NARROW by LOT     : pool.size -> step.to
                      WIDEN  by ELECTION: electors choose step.to names, threshold applies
                      >>> the player may spend Standing / Coin / Obligation AT EACH STEP <<<
  apply quota (max per house), avoidance (bar those with interests)
  invest(): grant selection.confers — powers and immunities — for selection.term
```

**The Venetian chain, encoded.** `chain = [N30, N9, W40, N12, W25, N9, W45, N11, W41]`. It is playable because the spend decision recurs at every step and the sortition between steps destroys whatever the last spend bought. A player holding twelve of the great council has a real but non-deterministic chance at each stage and must decide, at every widening, whether to commit now or hold for the next.

**Investiture is where Scope changes.** Winning an office is how a character moves from Self to Settlement to House to Faction — and losing one, or being repudiated, is how they fall back.

---

## §7 — Three loops replace eight graphs

The eight state graphs collapse to three, because the eight were three clusters wearing different configuration.

**Loop A · Contest** *(was S1 Court, S2 Tribunal, S3 Inquisition, S4 Negotiation)*

```
frame -> gate(stasis loop: claim / attack / probe / escape) -> resolve -> settle -> record
```
Configured by `body.gate.burden` (four values → four scenes), `body.entryGate`, and whether the evidence ConcealedValue is visible to one side or both.

**Loop B · Assembly** *(was S5 Parliament)*

```
convene -> frame -> floor(speak / assent / consume / put) -> divide -> block? -> enact(clock) -> record
```
Configured by `body.floor` and `body.blocks`. Loop B calls Loop A when it prosecutes an officeholder; Loop A calls Loop B when a contest needs ratification. **The cycle is preserved deliberately.**

**Loop C · Dominion** *(was S6 Settlement, S7 Territory)*

```
charter -> declare -> assess? -> decree -> comply -> probe(CIRCUIT) -> sanction -> renegotiate?
```
Configured by `charter` and by `body.parent` for scale. There is no separate settlement and territory loop; a territory is a body whose members are bodies.

**The three loops touch at exactly two points**, and both were computed findings rather than design choices:

1. **The bond.** Loop A produces an `Instrument` with a bond; Loop C reads it as a guard on every compliance roll. Diplomacy manufactures what governance spends the campaign enforcing.
2. **The record.** All three loops emit Records; all three read Records. The record spine is the only thing every loop shares, and it is nearly free.

---

## §8 — The eight old systems, as configuration

Proof that the distillation loses nothing. Each former state graph is now a row.

| Old system | Loop | `gate.burden` | `entryGate` | Evidence CV visible to | Distinctive config |
|---|---|---|---|---|---|
| **S1 Court** | A | `ACCUSER` | none | both | `selection.avoidance = true`, `quota` set, `escapeAllowed = true` |
| **S2 Tribunal** | A | `LOWER_STANDING` | `standing >= n` | both, provenance concealed | `blocks: [VETO]`, `floor.chairPutsMotions = true`, `appealsTo` set |
| **S3 Inquisition** | A | `RESPONDENT` | none | **tribunal only** | `escapeAllowed = false`, sanction ladder visible at all times, relapse guarded on a prior OATH record |
| **S4 Negotiation** | A | **`NONE`** | none | neither | `stases` used as agenda; terminates in `settle()` unconditionally |
| **S5 Parliament** | B | — | quorum | — | `floor.slots` finite, `floor.drafter` set, `blocks: [VETO, RETURN_UNSIGNED]`, enactment clock on |
| **S6 Settlement** | C | — | — | declared vs true | `body.parent` set; no sub-bodies |
| **S7 Territory** | C | — | — | declared vs true | `body.parent` = faction; members are bodies; two office seats of differing competence |
| **S8 Diplomacy** | A + B | `NONE` | precedence | neither | `settle()` output has `scope` from M2; recall emits a slow-decay estimate owned by the sender |

**Two things this table makes obvious that eight graphs concealed.**

- **S1 and S3 differ in exactly two fields.** Burden and evidence visibility. Everything else that felt different — the theatre, the withheld names, the abjuration — is content authored on top of two switches.
- **S8 is not a system.** Diplomacy is Loop A with `burden = NONE` and a precedence entry gate, wrapped in Loop B for ratification, with an M2 scope check on the output. Its distinctiveness is entirely in the *content* — postings, ceremonies, standing reports — not in the rules.

---

## §9 — The opposition model (replaces P45)

Single player means the design's political pressure must come from factions that plan. This is where the deleted shared-loss condition goes.

**Each faction holds:**

```
Faction {
  aims          : [Aim]           # 2-3, VISIBLE to the player
  redLines      : [Position]      # UNBUYABLE — no side payment moves these
  threatModel   : Map<ThreatId, 0..100>   # private assessment of danger
  concessionCurve: f(perceivedThreat) -> willingness 0..1
  patience      : segments before they act unilaterally
}
Aim { object, urgency, expiresWith: ActorId? }   # dies with its holder
```

**How it replaces shared loss.** There is no global lose condition. Instead, every faction's willingness to concede is a function of its private threat assessment. When a genuine common danger rises — a foreign army, a famine, a fiscal collapse — thresholds are crossed at different times for different factions, and they become tractable one at a time. The player's craft is knowing whose threshold has been crossed and buying agreement in that window.

This does three things the old mechanism could not:

1. **It makes obstruction end for a reason** rather than because a timer said so.
2. **It makes threat assessment a ConcealedValue** — you do not know how frightened they are, so M4 Probe has a target in the political layer, not just the evidentiary one.
3. **It gives the player something to do with a crisis other than survive it.** A crisis is a negotiating window.

**Red lines are the answer to finding C3** (the CK3 critique: if affection can be raised high enough, structure stops mattering). Every faction has 1–2 positions no payment reaches. `sidePayment()` checks red lines before anything else and fails flatly. Some conflicts must be positional.

**Aims expiring with their holder** is the Old World device and it is the pacing mechanism for a character-scoped campaign: the faction's demands change when its leading figure dies, which resets the negotiating landscape without any authored event.

---

## §10 — What is settled, what is open

**Closed by this document:**

- `[CLOSED: A5 resource economy]` — four resources, §3.
- `[CLOSED: A3 too many primitives]` — fourteen mechanisms, thirty-one configurations, §2.
- `[CLOSED: F5 role-shifting]` — moved into body configuration; the mechanisms no longer special-case.
- `[CLOSED: F6 missing selection system]` — M14, §6.9, including the encoded Venetian chain.
- `[CLOSED: A9 / F2 shared loss in single-player]` — replaced by the faction model, §9.
- `[CLOSED: F1 authority]` — M2 Scope, §4.

**Still open:**

`[GAP: enactment parameters — F7. The structure is right; every number in §6.6 is [UNTUNED] and was borrowed at the wrong scale. Derive them from your session length, not from Victoria 3.]`
`[GAP: interface — three loops and fourteen mechanisms is tractable, but nothing here specifies what a player looks at. A system this dense fails on legibility long before it fails on balance. This has now been flagged in three consecutive documents and remains untouched.]`
`[GAP: the claim corpus — the anti-collapse table in §6.2 works only if authored claims are distributed across warrant types. The 40% invariant is stated and not enforced. Write the checker before writing the claims.]`
`[GAP: A2 / F8 — the inquisitorial array must be authored to be inferable, every time. Against an AI this is a content burden with no procedural substitute, and no authoring guidance exists.]`
`[GAP: whether it is fun — unanswerable from inside. Prototype Loop A on paper with twenty claims and four bodies before writing a line of code.]`

**Build order**, by shared surface rather than by interest:

1. **M10 Record + M1 Standing.** Everything reads them; standing is derived from records, so they are one job.
2. **M3 Concealed Value + M4 Probe.** The object all three loops share.
3. **Loop A with `burden` as a parameter.** Four scenes for the price of one, and it exercises M5, M6, M7, M13.
4. **M2 Scope.** Wrap every binding act. Cheap once M10 exists.
5. **M14 Selection.** Unblocks four bodies that currently begin with a stub.
6. **Loop B**, then **Loop C**. Both reuse everything above.

### Audit trail

`[READ: political-mechanics-primitives.md, political-state-graphs.md, interrogation-output.txt — the 45→14 mapping was verified by script for exhaustiveness and non-overlap before being written: 45 accounted, 0 duplicates, 0 orphans]`
`[SELF-AUTHORED — bias risk] §1 is a self-audit and cannot be otherwise in this session; the requested model handoff is not available and staging it would have been worse than declining it. The specific residual risk: I performed the original expansion to 45 and this contraction to 14, so I am poorly placed to judge whether the 31 demotions lost anything real. Test by attempting to configure a scene the old primitives supported and the new schema cannot express.`
`[CONFIDENCE: high — the 45→14 mapping is verified and the schemas are internally consistent. medium — the M6 warrant/attack vulnerability table, which is a design assertion resting on argumentation theory rather than on play data. low — every numeric parameter, all of which are marked [UNTUNED].]`
`[PASS-3: audit performed read-only; distillation verified by script; six prior open findings closed; five remain open and are named. The largest change to the corpus is M2 Scope, which did not exist before this turn and which the new constraint made mandatory.]`
