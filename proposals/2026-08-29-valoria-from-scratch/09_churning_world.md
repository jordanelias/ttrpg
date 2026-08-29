# 09 — The Churning World: the tick, the three fidelities, and the personal↔strategic seam

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: IN (cross-cutting) · Composes on: `01_substrate.md` (binding spine)
## Owns: T8 · the world tick · fidelity · anti-leverage · the battle seam · latency · the compute budget

---

## 0. The one idea

The substrate gives three signatures and one actor. This document says **when they run, how many
times, and at what resolution**, and makes one structural claim:

> **Fidelity is individuation depth.** Not a second engine, not a formula. The same seven-phase tick
> runs over the whole peninsula every season; the only thing that varies is how many persons inside
> it are held as records rather than as cohort weight.

Aimed at three nulls. **N-4**: auto-resolve was never calibrated because a *process* and a *formula*
can only agree on average. There is no second slice here — F0 runs the same exchange loop and rolls
cohorts **variance-matched**, exact to the second moment, not just the mean (§2.4). **N-3**: §4 makes
personal contribution a **budget the collective owns and persons compete for**, not a quantity persons
add, which bounds leverage at a constant fraction of outcome at every N. I claim a bound, not a
solution, and §4.4 names what it misses. **N-9**: Phase 4 reads views and Phase 5 reads the world, and
no phase joins them; §11 traces a season where three people act on three false things and the world
resolves all of it without noticing.

Every object below carries a closed loop and an N-line. §12 is what I cut. §13 amends the spine
openly rather than diverging from it.

---

## 1. THE WORLD TICK

### 1.1 The unit and the scarce thing

**The tick is a season. Every person and every cohort commits exactly one act per season.**

The spine already named the stake: politics is the container and the alignment wanting different
things from the same hour of a life. Unlimited acts means the collision never happens — he serves
both. One act makes it compulsory and free. An act is not everything a person does in three months;
it is the **one discretionary commitment**. Subsistence, craft and travel-in-progress are Phase 1 and
happen *to* you.

- Loop: produced by `choose` → carried in the season's act queue → consumed by `resolve`.
- **Cut it and you lose:** scarcity of attention, therefore *priority*, therefore every dilemma. A
  Free Master who can both stand for the guild seat and answer his Einhir cousin's petition is never
  Southern Einhir in any way that costs.

### 1.2 The seven phases

Phases run in order. **Within a phase everything is simultaneous** — nobody in Phase 4 sees anybody
else's Phase 4.

**P0 CALENDAR.** Advance the date. Fire due **standing dates** into a docket: Goldenfurt's tithe
reckoning, the Kettlemakers' Examination, Hafenmark's Parliament sitting, a truce's expiry, a
Dicastery's term. Recompute **option availability** — which acts are legal for whom given office,
marks, place, and *the claims each person holds*. §9 needs nothing more than this line.

**P1 SETTLE.** The only phase that changes the world with no act behind it, restricted to
**metabolism**: larders consume against mouths, production resolves against Prosperity, wounds close
or fester, bodies age and die, travellers advance a leg. **No social quantity moves here** — no
standing, regard, grievance, or cohesion. The no-scheduled-recovery refusal is enforced by phase
membership, not discipline.

**P2 NEEDS.** Every person and cohort computes needs from its situation. Pure, parallel, never stored.

**P3 VIEW.** Top **K = 12** claims by salience per person; K = 3 per cohort, from the channel claims
at its address.

**P4 CHOOSE.** `choose(person, view) -> act`, everyone, against the frozen P1 snapshot and their own
ledger. The player's submission enters here and nowhere else.

**P5 RESOLVE.** `resolve(acts, world) -> events`. The only writing phase. Strata in §1.4.

**P6 WITNESS.** Events fan out by **presence and channel**; `witness` per person. Tellings resolved in
P5 land here as deposits in the hearer.

**P7 RECKON.** In-world housekeeping: claim confidence decays; ledgers over **L = 200** evict lowest
salience (this is forgetting — P-13 — not a data limit); cohorts whose stance spread widened
individuate; persons nobody remembers de-individuate (§8.2).

### 1.3 Simultaneity, and the scene

**Reaction latency at person scale is one season.** If Praefect Roth opens the granary to the Row and
not the hamlet, the hamlet's answer is next season's act. Consequence worth naming: **surprise is
structurally possible**, because no policy can say "if he does X, I do Y, this turn." You anticipated
or you are late.

The exception is the bridge to §2: **inside a contest the tick subdivides.** A contest opens a nested
loop of **exchanges** running P3–P6 over a smaller person set on a shorter clock. Fidelity is how deep
that nesting individuates, and nothing else.

### 1.4 Resolution strata, each with its reason

1. **Movement** — presence first, because every stratum below asks who was there.
2. **Binding decisions** — rulings at docket dates, dispensations issued. These change **terms**, and a
   ruling made at the court's sitting is by construction the frame for the season.
3. **Contested physical acts** — violence, seizure, blockade-running, a march.
4. **Uncontested material acts** — work, build, carry, arrive.
5. **Social acts** — `tell`, `carry`, `argue`, `admit`, `commit`, `vouch`, `submit`. Last, because they
   are *about* what happened. This ordering is what makes a season's gossip be about that season's deeds.

### 1.5 Conflict between acts

Every act declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`. Two acts conflict iff
they share an object and either mode is `exclude`, or both `alter` the same field. Conflicts route to
the substrate's `contest(container, prize, claimants)`, unchanged. Everything else resolves
independently; most of a season's 17,000 acts never touch.

**Ties break on a hash of (act-id, world-seed) — never on rank, office or list position.** A
rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet.

- Loop: `choose` writes `touches` → act queue's object index → the stratum resolver routes collisions.
- **Cut it and you lose:** two persons wanting the same thing without a designer having listed the pair.

---

## 2. ONE RESOLVER, THREE FIDELITIES

### 2.1 The refusal, taken literally

*Don't build a second resolver at all* is the first option, and Total War is the only precedent with
two paths and the only one with a twenty-year unsolved divergence. So: **one function, `resolve`, and
F0/F1/F2 are the same call with one integer changed.**

The finding that makes this affordable, stated before the table because it reframes everything: §10's
arithmetic shows a fully individuated battle costs ~9,600 `choose` calls, which is nothing. **F0
exists because the player cannot watch two hundred contests a season, not because the machine cannot
run them.** Therefore the correct difference between F0 and F2 is *as little as possible*, and any
difference must be justified by attention, never by cost.

### 2.2 The exchange loop — the process, stated once

```
contest(place, sides, stake, fidelity):
  participants := persons present, individuated to depth D(fidelity);
                  everyone else held as cohorts
  repeat until terminal:
     view := assemble(K=12) for each participant        # P3, nested
     act  := choose(participant, view) for each         # P4, nested
     resolve the exchange's act set                     # P5, nested
     witness the exchange's events into participants    # P6, nested
  terminal := a side's position destroyed | a named fault (evasion,
              self-contradiction, silence when pressed) | withdrawal
            | the clock (the date closes, night falls, the tide turns)
```

This is the only resolver in the game. A battle outside Stillhelm, the Masterpiece Examination
committee, a Doctrinal Adjudication hearing, and two brothers arguing over a barn are the same call
with different act vocabularies and different stakes.

### 2.3 The fidelity table — exactly what is dropped

| | **F2 PLAYED** | **F1 WITNESSED** | **F0 AUTO** |
|---|---|---|---|
| engine | the exchange loop | the exchange loop | the exchange loop |
| exchange count | full | full | **full** |
| claim budget K | 12 | 12 | **12** |
| act vocabulary | full | full | **full** |
| individuation depth D | every participant | ledger-named ∪ roles ∪ decisive ∪ Knot-partners | roles ∪ decisive ∪ Knot-partners |
| the rest are | — | cohorts | cohorts |
| roll variance | native | **variance-matched** | **variance-matched** |
| player's own choice | every exchange | **branching exchanges only** | standing orders only |
| presented | yes | partially | no |
| **dropped at this step** | — | the player's deliberation where their option set does not branch | **the within-cohort identity of the interchangeable** |

Not on the drop list at any step: exchanges, K, the act vocabulary, the terminal conditions, the
factor sheet, or the ability of any named person to die.

### 2.4 The variance-matched cohort roll

A cohort of weight *W* individuated produces successes with mean `W·μ(p)` and variance `W·σ²(p)`.
Rolled as a block on a bare mean it produces the right mean and **zero** variance — that is the
"formula approximating a process" defect exactly. So:

```
successes(C) = round( W·μ(p) + sqrt(W)·σ(p)·Z ),   Z ~ standard normal, clamped ±3
```

Exact to the second moment by construction, at the cost of one roll instead of *W*. Auto-resolve
results feel wrong not because they are biased but because they are **too close to the mean** — the
underdog never wins, the rout never happens. This is the fix, and it is arithmetic rather than tuning.

Genuinely lost: **third and higher moments** — the cascade where one specific man's failure
propagates. Bounded by two rules:

**Rule A — decisive individuals are never in a cohort.** *D* always includes anyone whose act could
produce a named-subject event with downstream consequence: an occupied role, a Knot partner, an
office-holder, anyone carrying a named object (a standard, a writ, the Examination piece), anyone
another participant's ledger names, and anyone whose act this exchange has outcome variance above a
threshold. Every cascade path is individuated at every fidelity; cohorts carry interchangeable mass only.

**Rule B — casualties individuate retroactively, into memory that already existed.** When a cohort
loses weight, the dead are named only for persons already in someone's ledger. If nobody knew his
name, nobody notices he is gone. T4-correct, free, and the same primitive that bounds population (§8.2).

- Loop: produced by the exchange loop at any fidelity → events with named subjects → `witness`,
  identically at all three fidelities.
- **Cut variance-matching and you lose:** upsets. Every auto-resolved contest returns the favourite,
  and the strategic layer becomes arithmetic the player does in their head.

---

## 3. TEST THE FAILURE MODE, NOT THE MEAN

Three tests, in severity order.

**T-S — SUPPORT, the hard gate.** Enumerate the *classes of named-subject event* F2 can produce:
`commander killed`, `role vacated`, `cohort routed`, `place taken`, `person captured`, `Knot
ruptured`, `standard lost`, `named fault conceded`. **Every class F2 can produce, F0 must be able to
produce.** If F2 can kill the commander and F0 cannot, F0 is broken however well the means agree. This
is the test twenty years of mean-calibration never ran. Rule A passes it.

**T-D — DISTRIBUTION SHAPE.** 200 runs at F2, 200 at F0, same world state, independent seeds; compare
by a two-sample shape statistic, never by means. Variance-matching passes it; a failure names *which*
moment was lost.

**T-F — F1 IS THE DANGEROUS TIER.** Structurally closest to scalar collapse, and the reason is precise:
**at F1 the player is present and their own choices are being auto-filled.** If standing orders are a
slider — *aggressive / balanced / cautious* — then the player's presence produces a worse result than
their absence, because a slider is the one place a scalar re-enters the decision path. So:

> **Standing orders are written in the same act vocabulary as F2 choices** — an ordered list of
> conditional acts over the player's own view:
> `1. if my flank cohort's chain is broken → rally` · `2. if Gerik is within reach and wounded →
> extract` · `3. if the van holds and the Row's cohort is unbroken → press` · `4. otherwise → hold`
> — and the after-action log names which order fired at which exchange.

That is also F1's R answer: standing orders are a real artifact with real trade-offs (order 2 costs
you the press), not a difficulty setting.

**Legibility, since these scenes may never recur.** Every contest publishes, *before* the first roll, a
**factor sheet**: at most seven rows per side, each a signed contribution in pool dice with its source
named, plus a **band**. The discipline: **publish every input, publish a band, never publish the
trigger point.** A Crown levy contesting a Restoration barricade in Oastad shows
`+14 numbers · +6 the serjeants' drill · +3 Praefect Roth's Will (share 0.31) · −5 two seasons short
rations · −4 the ranks are 6-in-10 Southern Einhir and the proposition is caste enforcement · −3 the
serjeant's role is vacant and unfillable here · band: likely to break the line, unlikely to hold it after.`

- Loop: produced by the pool assembler as a by-product of building the pool → the contest's opening
  event → the player's interface and the after-action log.
- **Cut the factor sheet and you lose:** the player's ability to learn the model. With no GM, an
  unexplained roll is indistinguishable from an arbitrary one, and N-6 wins.

---

## 4. ANTI-LEVERAGE, AND AN HONEST ANSWER TO N-3

### 4.1 The rule, generalised past battle

> **Fractional Contribution.** A person P acting on a collective C contributes `Δ(C) = φ(P,C)·Q(C)`,
> where `Q(C)` is C's own relevant quantity and φ is dimensionless. **No act anywhere in the game adds
> a flat amount to a collective.**

| P acts on C | Q(C) | what fractional means |
|---|---|---|
| Grandmaster Ehrenwall on a Löwenritter formation | its weight × its pool | she moves a fraction of the body, not +2 dice |
| a praefect on Goldenfurt's Order under riot | the settlement's own Order capacity | a strong town is steadied more absolutely, equally proportionally |
| Confessor Himlensendt preaching at a parish | the congregation's current stance mass | he moves a devout parish far and an indifferent one barely — no preaching an empty room into fervour |
| a backer on a petition | the petition's assembled weight | backing 401 adds less than backing 4 |
| a Restoration recruiter on a hamlet cohort | the cohort's existing grievance mass | **you cannot recruit where there is no grievance**, at any capability |

The last row does real political work with no rule naming anybody: Yrsa Vossen structurally cannot
manufacture a revolt in a contented Valorsmark parish, and Duke Magnus Vaynard's caste grievance
becomes a *precondition* for the Restoration rather than an accelerant.

### 4.2 Why constant φ is not enough

A constant φ makes one person's leverage scale-invariant — good. But **the number of persons who can
contribute grows with N.** Thirty officers at N = 1000, thirty constant φ's, and personal leverage
inflates back out of band. That is the trap Dominions' commander anchor and Total War's lord aura fall
into from opposite sides. So φ is **allocated from a budget the collective owns**:

```
Φ(C)       = Φ₀ · chain(C) · concord(C) · supply(C)        # the command budget, Φ₀ = 0.60
share(P,C) ∝ role_weight(role(P)) · standing(P,C),   Σ share = 1
φ(P,C)     = Φ(C) · share(P,C)
```

- **Φ₀ = 0.60** — the ceiling on how much of any collective outcome persons may determine. Forty
  percent belongs to the mass, the ground and chance, at every N.
- **chain(C)** ∈ [0,1] — fraction of C's weight whose command path reaches an occupied role, where
  **each link requires the subordinate to hold a current claim naming their superior** (§5.2).
- **concord(C)** = 1 − (mean |stance deviation toward the proposition at stake|)/5. People who disagree
  about *why* they are fighting fight worse, mechanically.
- **supply(C)** — larder satisfaction over two seasons, clamped.
- **role_weight** — commander 8, wing captain 2, serjeant 1, standard 1, scout 1, chaplain 1.

**The result.** A commander of a warband with one captain holds share ≈ 8/10 = **0.80**. A commander of
a levy with six captains and twelve serjeants holds 8/(8+12+12) = **0.25**. Personal leverage is
inversely proportional to organisational depth, and organisational depth is what grows with N. φ is
bounded at every N **by construction, not by tuning**.

### 4.3 How a person still matters at N = 1000

Not by adding to the outcome — that channel is closed — but by **acting on the share graph**: kill the
man holding 0.25 and his share redistributes at a cohesion cost, and **only once someone has been
told** (§5.2); turn him and `concord` falls across all the weight under him; vacate a role that cannot
be refilled (§5.3); cut `supply`, which is the larder, which is the hearth rung, which is where one
smuggler with a boat operates. At N = 1 the share graph has one node and this degenerates correctly.
The mechanism is continuous across the range because the graph is the same object at both ends.

### 4.4 Bounded, not solved

**Proved:** personal contribution as a *fraction of outcome* is invariant in N. That is an identity in
the construction, holding from N = 1 to N = 10⁶.

**Not proved, and not claimed:** that the *experience* of leverage holds at N = 1000. The construction
converts "add to the outcome" into "act on the share graph," and whether that feels like agency is a
question about **reach** — can the player find out who holds 0.25, get near him, act on him? That is an
access and investigation problem (T9's territory). This document does not solve it; it makes it the
right problem.

**The falsifier.** Run a fixed intervention — assassinate the highest-share officer — against formations
at N = 10, 100, 1000, 10000 and measure the shift in the outcome distribution *as a fraction of that
distribution's own spread*. Flat in N: the bound holds. Decaying: `chain` recovers too fast and the
succession-by-witness rule is mis-parameterised. Growing: commander `role_weight` is too high relative
to depth.

- Loop: Φ and share produced by the pool assembler from persons present and their command claims →
  carried nowhere, recomputed per exchange → consumed by `lead` and the factor sheet.
- **Cut the command budget and you lose:** the reason to keep a specific person alive at scale, and the
  difference between a mob and a formation. Both collapse into "how many bodies."

---

## 5. THE BATTLE SEAM

### 5.1 The defect, at the root

The failure to avoid is a seam whose contract has **the faction fighting** — derive a field from a
faction's military stat, label the combatant with the faction id, and the commander is a doorman whose
attributes never reach the outcome. The fix is a signature:

```
battle_contest(place, act_sets, stake) -> events
  reads : persons present — individuated and cohorts — with all six substrate fields
  reads : the command relation among them (the share graph)
  reads : the place — terrain, works, the settlement's Defense if it has one
  reads : each participant's stance toward the proposition at stake
  writes: events with NAMED SUBJECTS — deaths, woundings, role vacancies, the rout of a
          specific cohort, a capture, the place changing hands
  NEVER reads: a faction id · a faction military stat · a national strength number
```

**There is no army object and no battle object.** An "army" is a *faction footprint at a place plus a
share graph* — `presence(f,n)` from the substrate plus a command relation. A battle is a contest whose
act vocabulary is `{strike, hold, flank, press, rally, yield, extract, break}` and whose stake is the
place and lives. It has no fields of its own, so there is nothing for a faction stat to be written
into. ARCH R-5 holds: the Church of Solmund cannot fight. Grandmaster Sigrid Ehrenwall can, with the
persons who came when she called.

### 5.2 Losing a specific person, three ways

**(a) The share, and a succession that must be seen.** When a share-holder dies the succession rule
names the next occupant — but the share does not transfer until **the subordinates hold a claim naming
him**, because `chain` counts only currently-asserted links. A commander killed in the open, in view of
the line, costs one exchange of degradation. A commander killed in a wood at dusk leaves his share
*unallocated* until a runner is chosen, survives and is believed — and `chain` bleeds throughout.
`witness` doing load-bearing work in the middle of a melee is T4 at the seam, and it costs nothing new.

**(b) The Knots.** A partner's death is a rupture trigger: Disposition → −3, mutual Composure damage,
Coherence −1, and for a Close Knot a **Conviction scar**. A death in the line at Stillhelm propagates
Coherence damage to a partner three provinces away in Himmelenger, that same season, through a channel
that exists for other reasons. T6 landing on one named person with no down-stroke mechanism invoked.

**(c) The claims.** Whatever he alone knew dies with him unless told or written. §9 makes this the whole
latency model, and it is why killing a man is a way of destroying information.

### 5.3 Role, not biography — and why that makes caste a battlefield mechanic

Gate on a class and losing a person is a promotion opportunity; gate on "the officer with cavalry
history" and one death costs you cavalry permanently. So a formation's act vocabulary is unioned from
its **occupied roles**, never from biographies: `flank` is legal iff a wing-captain role is occupied,
`rally` iff a serjeant or standard is. A role is occupied by any present person meeting a **capability
floor plus a mark**. Killing the occupant *vacates* the role; vacancy is filled next exchange by the
highest-standing qualified person present. Capability is never permanently lost.

The mark half is exactly the setting's per-institution rank gate — caste enforced by institutions, not
law, therefore a gate per rung and per body:

| formation | serjeant's mark requirement | who fills a vacancy in Grauwald, where the ranks are 6-in-10 Southern Einhir |
|---|---|---|
| Crown levy | Standing 3+ via public deeds or inner-circle sponsorship | almost nobody present |
| Church-raised militia | Church standing | a Southern Einhir Canon is "a scandal" — nobody |
| Löwenritter | order-mark, caste-open | the best man present, in one exchange |
| Niflhel | none — caste-open by design; waterfront work needs Southern Einhir | anyone |

A Crown levy that loses its serjeant in Grauwald has a vacancy it **cannot fill**, and `chain` stays
broken for the rest of the battle; a Löwenritter formation closes it in one exchange. Nothing in the
code says "caste" — the institutional mark gates plus the general role mechanism produce it. And it
gives Duke Magnus Vaynard's anti-caste programme a **military payoff**: breaking the caste system makes
Varfell's levies more resilient than Valorsmark's. That is what makes the political fight about
something rather than about virtue.

- Loop: role thresholds produced by each institution's own admission gates (persons' stances at a
  community gate, per the substrate) → carried on the role definition → consumed by the vacancy filler
  each exchange and by the factor sheet.
- **Cut role-gating and you lose:** promotion as a consequence of death, and the mechanism by which
  institutional exclusion shows up as *capability* rather than as a flavour tag.

---

## 6. THE LEADER IS NOT A MODIFIER

A flat shift of size X on a d-pool is worth ≈ `X / (0.8·√Pool)` — **more to a small pool than a large
one** — so a flat leader bonus is systematically worth more to a weak faction, inverting every intuition
the strategic layer depends on. The in-band form:

> **The leader operator.** `lead(P, C, act)` does exactly two things.
> **(a) OPTION SET** — `vocabulary(C) ∪= practices(P)` for this exchange.
> **(b) POOL SOURCE** — on the fraction `φ = Φ(C)·share(P,C)` of C's weight, that weight's roll draws
> the named attribute **from P instead of C's own mean**. The remaining `1−φ` rolls its own.
> **No third thing. No addend. There is no leadership stat.**

Direction check: substitution moves `W·φ·(P's attribute − C's mean)`, proportional to W. As a fraction
of an outcome also proportional to W it is **constant in N** — the exact inverse of the flat-bonus
pathology. And it makes cohesion mean something plain: `Φ·share` is *how much of this body is thinking
with its commander's head*.

**Commander.** Option set: a commander holding the `feint` practice makes `feint` legal for cohorts
under his share; without him it is not in the vocabulary and no quantity of numbers substitutes. Pool
source: cohorts fight with their own Strength and Endurance and **his Will and Focus** on the φ
fraction. A levy under Ehrenwall rolls its own bodies and her nerve.

**Governor (praefect, ducal reeve, gate warden).** Option set: which **dispensations** they may issue at
the settlement's standing dates — gated by office *and* by what the judging set will tolerate, so a
praefect who has spent his regard cannot issue what he could last season. Pool source: when Goldenfurt
resists a shock — dearth, riot, a Restoration barricade — the Order roll draws its Focus/Acuity component
from him on the φ fraction, where Φ is *administrative* cohesion: do the ward-holders' ledgers currently
name him, has he been present, does he speak Einhir. A governor absent four seasons has `chain` near
zero and contributes nothing, with no absence timer anywhere (§7.4).

**Negotiator (envoy, advocate, Dicastery proctor).** Option set: which **stasis rungs** they may occupy
— deny the act / deny the label / admit-and-justify / challenge the venue. Without the Precedent
conviction and a legal mark they cannot open the jurisdiction rung *at all*, which is why Hafenmark's
Parliament sends the men it sends. Pool source: an envoy substitutes their own Attunement and Charisma
**for their absent principal's standing** — which is what an envoy is. And their presence changes who may
be a **respondent** to a petition, an option-set change one rung up: sending Princess Elske to Almaic
Kyriakos makes the Doux a legal respondent for Almud's merchants, and nothing else does.

- Loop: produced by a person choosing `lead`, spending their act → carried in the exchange's pool
  assembly → consumed by the roll and shown as a named factor-sheet row.
- **Cut it and you lose:** any reason for a specific named person to be at a specific place, and the
  difference between sending Ehrenwall and sending an equally-skilled stranger.

---

## 7. THE PLAYER IS ONE PERSON

**What they are.** A person record: Address, Marks, Capability, Stance, Memory, Ties. One act per
season. The same `choose(person, view) -> act`. **The interface is the view, rendered.**

**What they get that an NPC does not: deliberation time, and only that.** An NPC's `choose` runs a
bounded policy over K = 12 ranked claims. The player may sit with the same twelve for an hour, re-read
their ledger, chase provenance, plan four seasons out. That is the entire advantage — and it is large,
because a player who models other persons' views will consistently out-plan a bounded policy. It is
also the right advantage, being an advantage at exactly the thing the game is about.

**What they do NOT get.** No world argument, ever. No omniscient map — a province they have had no news
from displays the **last claim they hold**, with its date and source visible; **stale claims render as
current**, because that is what a belief is. The date is shown; staleness is not flagged. If Duchess
Inge Baralta's banner still flies over Oastad on your map, it is because that is the last thing you were
told. No pause-the-world: the tick runs whether or not you submit, and **a player who does not act has
chosen `abide`.** No event feed — news is your ledger's new rows, with sources. No extra acts, no extra
reach, no faction-level verbs.

**Ignorance must cost, and here are four mechanisms, none of them a timer.**

1. **Your act is evaluated against the world, not your view.** Petition a respondent your ledger still
   names in a seat he lost last season, and the petition is carried to a man with no power to answer:
   the carrier spends regard, you get nothing, the backers learn only that it failed. Free — it falls
   out of the signature rule.
2. **Standing dates pass without you.** The docket is published by telling, not notification. If no one
   told you the Examination sits this autumn you do not contest it, and the seat goes to whoever did.
3. **Your holdings forget you — by memory decay, not a governance meter.** `chain` counts only links
   whose subordinate's ledger *currently asserts* who decides here; claim confidence decays in P7 by the
   same universal rule that governs every memory in the game. Below the floor the ward-holders stop
   counting you as the answer and their share redistributes. **You lose Goldenfurt by being forgotten.**
   The mitigation is not a timer either — send a telling. A letter, a factor, a Knot. It costs an act
   slot, yours or a client's, and it can be intercepted, delayed or forged.
4. **Your allies petition you, and the drop is charged to you by name.** If you are in Himmelenger the
   petition reaches a container you are not at, the carrier drops it, and grievance deposits toward
   *you*. You come home to an injury you were never given the chance to answer. That is T8's sharpest
   edge, and it is why a world that does not need you is a threat rather than a boast.

- Loop: produced by the ordinary act/witness/decay machinery with no player-specific code → carried in
  other persons' ledgers → consumed the day the player next needs those persons.
- **Cut the ignorance cost and you lose:** any reason to be anywhere, therefore the meaning of travel,
  delegation, and the whole strategic question of *where do I spend my presence*.

---

## 8. CHURN WITHOUT CONTENT AUTHORING

### 8.1 On demand, never on a clock

CK3 mints six or seven parentless sixteen-year-olds a month and passes 24,000 characters late. **The
clock never mints a person here.** The world holds a **demographic envelope** per containment node —
counts by age band, marks bundle, capability distribution, carried as cohort weight. Births and deaths
move *weights*. A **record** is minted only when: an event names them · a telling puts them in someone's
ledger · they occupy a role or office · they enter a Knot · they are individuated as decisive in a
contest.

Minting draws address from the cohort, marks from the cohort plus its variation, capability from its
distribution conditioned on whatever the naming event implies, stance from its aggregate plus dispersion.
**Memory is the trick that makes it consistent:** tellings are stored *at the channel*, not per person,
until individuation — so a person minted in season 40 is handed the claims their address's channels would
have deposited. They have a plausible past because their *channel* has a real one.

### 8.2 Reabsorption — the bound CK3 lacked

A record **de-individuates** in P7 when it holds no role, no Knot, no stance above the commitment
threshold, and **no other person's ledger names it.** Its state folds back into the cohort as weight. The
flow is bidirectional, so the standing population is bounded by **how many people anyone remembers** —
the correct bound, in-world meaningful, needing no cap constant.

- Loop: mint triggers → a person record → every system → returned to the cohort by the P7 sweep.
- **Cut on-demand individuation and you lose:** anyone mattering who was not important when the world was
  made. Every consequential person becomes one a designer minted.

### 8.3 No scheduled recovery, and suppression without a flag

> **The only clock-driven quantities in the game are matter, bodies, and the confidence of a memory.
> Every social quantity — standing, regard, grievance, cohesion, commitment — moves only when an act
> causes an event.**

Enforced by P1's membership. There is no phase in which a restoring timer could run.

**Suppression.** A coercive act that "solves" an unrest event does **not** change stance toward the
proposition. It adds stance toward *acting on it* — fear — which decays by the same witnessed-presence
rule as everything else. Meanwhile the grievance claim sits in the ledger at full confidence and is
**told to children** along the hearth's transmission edge. Next time it fires the backers already hold
the claim, so the petition assembles in one season instead of four. **A lower trigger threshold with no
threshold object anywhere.**

### 8.4 No mechanism engineered not to fire — the recoverability test, run

Maximum available mitigation against maximum accrual. Stance `s ∈ [−5,+5]`; all moves fractional,
`Δs = g·λ·(target − s)`, `λ` = the fraction who *learn of it*. Subject: the Southern Einhir hamlet cohort
outside Goldenfurt, weight 400.

| | act | g | λ | target | factor on distance |
|---|---|---|---|---|---|
| **accrual** | 4 petitions dropped | 0.25 | 0.70 | −5 | (1−0.175)⁴ = 0.463 |
| | granary opened to the Row only | 0.20 | 0.90 | −5 | 0.820 |
| | *combined* | | | | **0.380** |
| **mitigation** | governor `appear` at the hamlet | 0.15 | 0.60 | +1 | 0.910 |
| | 3 petitions carried and won | 0.25 | 0.50 | +1 | 0.670 |
| | 12 standing-holders `vouch` | — | 0.80 agg. | +1 | 0.700 |
| | *combined* | | | | **0.427** |

From a fully aggrieved `s = −4.5`: mitigation gives `+1 − (5.5 × 0.427) = −1.35`; accrual then gives
`−5 + (3.65 × 0.380) = −3.61`. **Net +0.89 per season with both at maximum.**

**Verdict: it fires, it is recoverable, and the recovery costs everything.** Sixteen act-slots — the
governor, three carriers, twelve standing-holders — is essentially Goldenfurt's entire governing capacity
for the season. No granary work, no wall, no trade; which raises next season's needs, which raises next
season's petitions. Neither pole: mitigation genuinely works (not EU4's estates), and it is not
unavoidable (not Imperator's governors). The *actually* superior line is not to spend sixteen slots on
remedy but to **stop dropping petitions** — which costs the carriers their standing with their own
judging sets, which is a different person's problem, which is politics.

**R check on the carrier's fork.** CARRY gains the backers' regard and costs the opposing judging set's;
DROP is the inverse. Both are durable stance rows and **neither decays on a clock**, so neither has
decaying gain against compounding cost. The only asymmetry is `λ_drop = 0.70 > λ_grant = 0.50` — the
aggrieved talk more — emergent from the telling system rather than tuned, and a nudge, not a dominance.
Which way the fork resolves depends on the carrier's *address*: Burgher Aldwin Roth, a Kettlemaker,
carrying an Einhir hamlet's petition faces an opposing set that is his own community. The fork is decided
by who you are.

---

## 9. LATENCY — decided up front, and it needs no new object

> **A latent act is a stance toward a proposition of the form `act(…)`, held above the commitment
> threshold, whose act is not in the person's option set until they hold an enabling claim.**

P0 recomputes option availability from claims; P4's `choose` ranks by stance. That is the entire fuse
mechanism, built from two things the substrate already has.

| | ruling |
|---|---|
| **may persist indefinitely** | claims; stance rows including act-propositions; Knots and their strain; claims written to a **physical carrier** — a document persists past its writer at the place it is kept and is found by a `search` act; contingent claims on occupied seats banked at a marriage |
| **may fire late** | any act whose enabling claim arrives late — reprisal, blackmail, a debt called in, a dormant claim on a seat admitted the season its vacancy is *believed*. No maximum delay |
| **carries a dormant flag** | **nothing.** There is no flag object; dormancy *is* an act-proposition with an unmet enabling claim |
| **may never persist** | the world's true event record as anything an agent can read (the spine's refusal, unamended); a dead person's ledger unless told or written; and **an act from a dead bearer** — a latent act whose bearer dies is inherited or lost: if he told it (a claim plus an obligation edge) it re-forms in the hearer with the hearer's own stance and fuse, otherwise it dies with him |

That last line makes assassination a real solution to a real problem, and makes **telling someone your
secret** a deliberate, dangerous, irreversible act.

**The 1218-AG hunting accident, carried sixty years.** (1) The event happened; **no agent can read it.**
(2) A huntsman witnessed it and deposited `(Almqvist-the-first, killed_by, X, 1218, firsthand, 0.9)`.
(3) He told no one — or told one person under a Close Knot, or **wrote it**. A written claim has a
physical carrier and a place, and the place a sixty-year-old accusation would be kept is the **Dicastery
of Doctrine and Archives**, because the Church holds the archival monopoly granted under the Altonian
containment grant. The cage-became-a-school is load-bearing here. (4) He dies; his ledger dies with him;
only the document survives. (5) Sixty years on someone performs `search(archive)` at F2 — a field
investigation, first-class, T9 — and the claim enters their ledger, `when = 1218`, confidence high because
the document's provenance is checkable and its independence root is its own. (6) They `tell` it;
credulity and stance-toward-speaker roll at each hearer. (7) **The contradiction is automatic**, because
claim identity is a tuple with a mandatory interval: the 1218 claim collides with every claim asserting
the deed-monarchy's founding was clean. No designer needs to notice. (8) Obstinacy sets how many more
contradictions each holder needs — and **every act-proposition fused on "if I come to believe the throne
was taken by murder" enters its bearer's option set that season**, including Duchess Inge Baralta's
Baralta Crown Claim, banked at her marriage, dormant, now legal. If the Church's own succession is
contested in the same window, the consecration crisis composes with it, because both are propositions
before overlapping standing dates.

**And if nobody wrote it and the huntsman told nobody, the perpetrator is unknowable forever.** The world
holds a fact no agent can ever reach. That is the design's most extreme statement of T4, and it is why
the perpetrator can be left deliberately unresolved without the engine needing a placeholder.

- Loop: produced by `witness` at the original event → carried by a person's stance table, or by a physical
  document at a place → consumed by P0's option-availability recomputation the season the enabling claim
  lands.
- **Cut latency and you lose:** every consequence that outlives its cause. No reprisal, no revelation, no
  inherited grudge, no dynastic claim — and a campaign with a memory of exactly one season.

---

## 10. WHAT "100% RESOLVED" HONESTLY MEANS

**Target: a season tick in ≤ 2 s on a mid-range machine.** Fifty years = 200 ticks ≈ 7 minutes of
simulation. Modelled population ~1.2 million **as weight**; the record count is far smaller.

| | count | basis |
|---|---|---|
| containment nodes | ~1,500 | 3 duchies · 14 provinces · 35 settlements + Himmelenger + Schoenland · districts · ~800 community nodes (guild rows, Einhir hamlets, Crown-Latinate quarters, parishes, Restoration cells) · hearths on demand |
| **cohorts** | **~9,600** | ~800 communities × ~4 marks bundles × ~3 stance buckets |
| **individuated persons** | **3,000–6,000 typical; 8,000 soft ceiling** | bounded by §8.2 — you exist as a record while someone remembers you |
| **acts per tick** | **≤ 17,600** | ≤8,000 persons + ~9,600 cohorts, one each |
| ledger cap L | 200 / person, 20 / cohort | eviction is forgetting (P-13) |
| view assembly | ~2 × 10⁷ comparisons worst case | 17,600 × top-12 of ≤200, ranking maintained incrementally |
| **witness deposits** | **≤ 120,000 / tick** | see below |
| contests | 0–3 battles, 20–200 social | see below |

**Witness fan-out is the real cost, and the cohort tames it.** An event's witness set is the persons
present plus the channels it touches, and **a channel deposits into a cohort as one claim, not into its
members.** A crier's proclamation of a ducal dispensation in Goldenfurt deposits ~6 cohort claims and ~40
individuated claims — not 12,000. A cohort member who later individuates inherits the cohort's channel
claims (§8.1). One primitive, three jobs.

**Contest cost.** F0 battle: 12 exchanges × ~70 participants (20 cohorts + 15 individuated a side) = **840
`choose` calls.** F2 fully individuated at 400 a side: 12 × 800 = **9,600** plus presentation. Both
trivial. **The compute case for auto-resolve is weak, and that is the point** (§2.1).

**When the budget is exceeded, in order:** (1) **de-individuation sweep** — fold the least-remembered
records back into cohorts, lowest salience first; (2) **ledger eviction** at L — people forget; (3)
**cohort coarsening** — merge cohorts whose stance buckets converged, reversible the moment a spread
widens or an event names a member; (4) last resort, an **exchange budget** across the season's contests,
spent on the highest-variance ones — noting this degrades *terminal conditions*, so it is the last thing
to give and the first to restore.

> **There is no simulation radius.** No region is paused, frozen, sampled, or run on a different model
> because the player is elsewhere. A distant province is cheap because it is **coarse**, not because it is
> **stopped.** Every shipped mitigation in the genre is a radius, and a radius contradicts T8 outright —
> a world that churns only near the player is a world that does not churn. All four steps above are
> resolution reductions, reversible on demand, applied uniformly without reference to where the player
> is standing.

---

## 11. WORKED TRACE — one season, no player present

The player is a Free Master of the Kettlemakers in Goldenfurt (Grauwald, Varfell), Southern Einhir by
heritage, who passed the Masterpiece Examination nine years ago. They are in Himmelenger, two seasons into
petitioning the Dicastery of Temporal Affairs for a guild tithe exemption. Their shop is held by their
apprentice **Gerik Strand**, who is this autumn's Examination candidate.

**Autumn 1281.**

**P0 CALENDAR.** Goldenfurt's tithe reckoning fires. The Kettlemakers' Examination sits (every third
autumn). Journeyman **Halvard Uln**, kin of Maret Uln, holds a stance at +5 toward
`reprisal(the committee's speaker)`; its enabling claim — *the Examination rejected another Southern
Einhir candidate* — does not exist, so the act is not in his option set.

**P1 SETTLE.** Grauwald's autumn is wet; harvest resolves short. Fourteen hearths in the Einhir hamlet
outside the wall fall below mouths, Gerik's among them. The shop's larder is fine. Nothing social moves.

**P2 NEEDS.** Fourteen hearths compute unmet food. Gerik computes two: feed his hearth, and pass. Praefect
Roth computes a need to be *seen* to have fed the town.

**P3 VIEW.** Gerik's twelve include, from the player, *"if the Examination goes against you, do not answer
it"* (0.9, salience-boosted by his +4 stance), and from Halvard, *"the committee is set against us"* (0.5).
Burgher **Aldwin Roth**'s twelve include a claim a guild rival deposited last season: *"your Free Master is
in Himmelenger petitioning the Church against Goldenfurt's tithe"* — a distortion of the truth, which is
that the player is petitioning *for* the guild's exemption. Nobody has corrected it. Nobody is here to.

**P4 CHOOSE.** Gerik: `submit_masterpiece`. The five committee Free Masters: their votes — three hold
stance toward the mark *Southern Einhir* at −2 or worse; Aldwin, at +3 toward the player, reads the rival's
claim as disloyalty to the settlement, drops to −1, and votes against. Halvard: `abide`; his act is still
illegal. Praefect Roth: `issue_dispensation` — the granary opens to the walled communities, not the hamlet,
because the Kettlemakers' judging set would punish feeding the hamlet while the Row goes short.

**P5 RESOLVE.** *Binding:* the dispensation issues at the tithe reckoning; the Examination resolves as
`contest(Kettlemakers, Free Master grade, {Gerik})` — 3–2 against. *Material:* fourteen hearths spend
nothing. *Social:* the committee's speaker announces the result.

**P6 WITNESS.** Gerik deposits `(Examination, rejected, me, autumn-1281, firsthand, 1.0)` and, his obstinacy
being low and Halvard's rumour salient, **an inference**: `(Aldwin Roth, turned_against, my master, …,
inferred, 0.6)`. Halvard witnesses the announcement — **his enabling claim now exists, and `reprisal` enters
his option set for next season.** The hamlet cohort deposits `(Praefect Roth, fed the Row and not us, …)`;
stance toward Roth moves −1 → −2.0. A Restoration cell member in the hamlet deposits, and will `tell` in
the spring.

**P7 RECKON.** Over the following two seasons six hamlet persons `commit` at low degree to the cell; its
density at Goldenfurt rises. Confidence on every claim naming the player as present decays another step;
three ward-holders' assertions of who decides in the Row fall below the floor, and their share redistributes
toward Roth.

**What the player comes home to in spring.** They hold a Close Knot with Gerik, so across the winter they
felt strain accrue and Coherence drop — **a state, not a telling.** Something was wrong; nothing said what.
On arrival they learn it from Gerik, in Gerik's version, which includes at 0.6 confidence and delivered as
fact that Aldwin Roth turned on them. Their first act home is likely to be against Roth — on an inference
from a rumour that was itself a distortion, none of which anyone lied about.

**The bill for one season's absence.** One Free Master seat not gained, and its guild vote. One ally turned
by a false claim that a single `tell` before departure would have prevented. One reprisal armed that one act
slot would have disarmed. Six new Restoration commitments inside the player's own community, which will
appear in the next threat assessment attached to the Row — therefore to the player's name. Three ward-holders
who have quietly stopped believing the player decides anything in Goldenfurt.

Nothing above was authored. Every step is the six person fields, the two relations, the three signatures,
the seven phases, and the fractional contribution rule.

---

## 12. REFUSED, under E-as-a-ratio

A second resolver, an auto-resolve formula, or a battle model (§2). An army object, a faction military stat,
or any national strength scalar (§5.1). A leadership stat or any flat leader bonus (§6). A morale bar,
unrest meter, or cohesion field stored on a container — Φ is derived per contest from persons, claims and
larders, and stored would be a second copy that can disagree. A grievance threshold, unrest trigger point or
revolt gauge (§8.4). A dormant-flag object (§9). A simulation radius, distance LOD, or "background" model for
distant provinces (§10). A notification feed, quest log, or event inbox for the player (§7). A standing-orders
slider (§3, T-F) — the one place a scalar could re-enter the decision path. A biographical capability gate
(§5.3) — gate on role, always. A scheduled recovery, decay or upkeep tick on any social quantity (§8.3),
enforced by P1's membership. An initiative or turn-order stat (§1.5) — ties break on a seeded hash.

---

## 13. CHALLENGE — two amendments to the spine, stated rather than diverged from

**(1) `resolve` must take an act SET.** The spine writes `resolve(act, world) -> event`. Conflict resolution
(§1.5) is impossible under that signature: to know two acts touch the same granary, the world must see both.
I propose `resolve(acts, world) -> events`. This weakens nothing — the constraint the signature rule exists
to enforce is that *agents* cannot see true state, and the world seeing everything is what the world is for.
But it must be made explicitly, because a singular signature pushes conflict handling into a per-act pre-pass,
which is where a hidden turn order gets born.

**(2) Salience needs a floor, or correction becomes unreachable in principle.** The spine ranks claims by
`recency × confidence × relevance × stance weight` and gets T3 for one multiplication — elegant and true. But
if stance weight is unbounded and stance can be strong, a person with a hard stance can never surface the
claim that argues against it, at any confidence. Their obstinacy is then never tested, and §3.2's promise that
*"correction comes from collision with the world"* cannot be kept: the collision happens and the claim never
enters a view. This document leans on that correction path directly — Aldwin's false claim must be
correctable; the 1218 revelation must be able to move people who do not want it to.

Proposed: salience = `max(stance-weighted score, floor)`, where `floor = recency × confidence` for claims with
`source = firsthand`. A thing you saw yourself, recently, with high confidence **always** makes your twelve.
You may still refuse to believe it — that is obstinacy's job, and obstinacy is the right place for the
resistance — but you cannot fail to *consider* it. Motivated reasoning stays a strong bias and stops being an
epistemic prison, for the cost of one `max`.
