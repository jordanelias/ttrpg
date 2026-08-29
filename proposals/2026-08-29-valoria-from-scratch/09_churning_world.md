# 09 — The Churning World: the tick, the three fidelities, and the personal↔strategic seam

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: IN (cross-cutting) · Composes on: `01_substrate.md` (binding spine)
## Owns: T8 · the world tick · fidelity · the anti-leverage rule · the battle seam · latency · the compute budget

---

## 0. The one idea, and the three nulls it is aimed at

The substrate gives three signatures and one actor. This document says **when they run, how many
times, and at what resolution** — and it makes exactly one structural claim:

> **Fidelity is individuation depth. It is not a second engine, not a formula, and not a
> shortcut. The same seven-phase tick runs over the whole peninsula every season; the only thing
> that varies is how many of the persons inside it are held as records rather than as cohort
> weight.**

Everything below is that sentence made arithmetic. It is aimed at three of the corpus's nulls.

- **N-4 (auto-resolve calibration).** Twenty years unsolved because the played path is a *process*
  and the fast path is a *formula*; two different slices can only be made to agree on average. Here
  there is no second slice. F0 runs the same exchange loop with the same act vocabulary; it rolls
  cohorts instead of members, and it rolls them **variance-matched**, so the compression is exact to
  the second moment rather than merely to the mean. What remains lost is named in §3 and bounded.
- **N-3 (personal leverage across three orders of magnitude of N).** §4 gives a construction in
  which a person's share of a collective's outcome is a constant fraction at every N, by making
  personal contribution a **budget the collective owns and persons compete for**, not a quantity
  persons add. I claim a **bound**, not a solution, and §4.4 says exactly what the bound does not
  cover.
- **N-9 (no shipped NPC acts on knowingly false political information).** The tick's Phase 4 reads
  views and Phase 5 reads the world, and there is no phase in which those two touch. §11 traces a
  season where three separate persons act on three different false things and the world resolves all
  of it without noticing.

Every object below is a closed loop — *producer → carrier → consumer* — with an N-line. Objects I
considered and cut are in §12. §13 records two places where I believe the spine needs amending, and
does not silently diverge from it.

---

## 1. THE WORLD TICK

### 1.1 The unit, and the scarce thing

**The tick is a season.** Every person and every cohort commits **exactly one act per season.**

That is the whole action economy, and it is chosen because the spine already named the stake:
*politics is what happens when a person's container and a person's alignment want different things
from the same hour of their life.* If a person has unlimited acts, the container and the alignment
never collide — he serves both. One act per season makes the collision compulsory and free.

An act is not everything a person does in three months. It is the **one discretionary commitment**.
Subsistence, craft, worship and travel-in-progress are not acts; they are Phase 1, below, and they
happen to you.

- Closed loop: produced by `choose`; carried in the season's act queue; consumed by `resolve`.
- **Cut the one-act budget and you lose:** scarcity of attention, therefore the meaning of the word
  *priority*, therefore every dilemma in the game. A Free Master who can both stand for the guild
  seat and answer his Einhir cousin's petition is never Southern Einhir in any way that costs.

### 1.2 The seven phases

Phases run in order. **Within a phase, everything is simultaneous.** Nobody in Phase 4 sees anybody
else's Phase 4.

**Phase 0 — CALENDAR.** Advance the date. Fire due **standing dates** into the season's *docket*:
Goldenfurt's tithe reckoning, the Kettlemakers' Examination, the Hafenmark Parliament's sitting, a
truce's expiry, the Church's four Dicasteries' term openings. Recompute **option availability** —
which acts are legal for whom, given office, marks, place and the claims each person holds (§9 uses
this and needs nothing else).

**Phase 1 — SETTLE.** The only phase where the world changes with no act behind it, and it is
deliberately restricted to **metabolism**: larders consume against mouths; production resolves
against the settlement's Prosperity; wounds close or fester; bodies age and some die; travellers
advance one leg. *No social quantity moves in Phase 1.* No standing, no regard, no grievance, no
cohesion. That restriction is the refusal on scheduled recovery ticks, enforced by phase membership
rather than by discipline.

**Phase 2 — NEEDS.** Every person and cohort computes its need vector from its situation (larder vs
mouths, standing vs siblings-in-container, unmet stance commitments, exposure to a dispensation's
terms). Pure, parallel, no writes. Needs are never stored — the spine is right that a stored need is
a second copy of the world that can go stale.

**Phase 3 — VIEW.** Every person assembles a view: the top **K = 12** claims by salience from their
ledger. Cohorts assemble K = 3 from the channel claims at their address. Parallel, read-only.

**Phase 4 — CHOOSE.** `choose(person, view) -> act`, for everyone, from the frozen Phase-1 snapshot
and their own ledger. Parallel, no writes. The player's submission enters here and nowhere else.

**Phase 5 — RESOLVE.** `resolve(acts, world) -> events`. The only writing phase. Strata in §1.4.

**Phase 6 — WITNESS.** Events fan out by **presence and channel**; `witness(person, event) -> claim`
per person. Tellings resolved in Phase 5 land here as ledger deposits in the hearer.

**Phase 7 — RECKON.** Ledger housekeeping that is *in-world*, not bookkeeping: claim confidence
decays by the universal memory rule; ledgers over the cap **L = 200** evict their lowest-salience
rows (this is forgetting, and P-13 says forgetting is rendering failure, not a data limit);
cohorts whose stance spread has widened past honesty **individuate**; persons nobody remembers
**de-individuate** (§8.2).

### 1.3 What is simultaneous, and what that buys

**Reaction latency at person scale is one season.** Nobody reacts within a tick. If Praefect Aldwin
opens the granary to the Row and not the hamlet, the hamlet's answer is next season's act. This is
the single most important consequence of simultaneity and it is worth naming as a design result:
**surprise is structurally possible** because no policy can be written that says "if he does X, I do
Y, this turn." You must have anticipated, or you are late.

The exception, and the bridge to §2: **inside a contest, the tick subdivides.** A contest opens a
nested loop of **exchanges**, running Phases 3–6 over a smaller person set on a shorter clock.
Reaction inside a scene is one exchange. Fidelity is how deep that nesting individuates, and nothing
else.

### 1.4 Resolution strata, and why in this order

Phase 5 resolves in five strata. Every ordering decision here is a claim about the world, not a
convenience:

1. **Movement.** Presence changes first, because every stratum below asks *who was there*.
2. **Binding decisions.** Office-holders' rulings at the docket's standing dates; dispensations
   issued. These change **terms**, and a ruling made at the court's sitting is by construction the
   frame the season's other acts happen inside.
3. **Contested physical acts.** Violence, seizure, blockade-running, a march on a settlement.
4. **Uncontested material acts.** Work, build, carry goods, arrive.
5. **Social acts.** `tell`, `carry`, `argue`, `admit`, `commit`, `vouch`, `submit`. Last, because
   they are *about* what happened — and this ordering is exactly what makes a season's gossip be
   about that season's deeds.

### 1.5 Conflict between acts

Two acts conflict iff they **name a common object with incompatible modes.** Every act declares
`touches: {(object, mode)}` with mode ∈ `{read, alter, exclude}`. Conflict iff they share an object
and either mode is `exclude`, or both are `alter` on the same field.

Conflicts route to `contest(container, prize, claimants)` — the substrate's own function, unchanged.
Non-conflicting acts resolve independently and simultaneously; the vast majority of a season's
17,000 acts never touch each other.

**Ties break on a hash of (act-id, world-seed), never on rank, office, or list position.** A
rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet, and it would make
office worth more than it says it is worth.

- Closed loop: produced by `choose` writing `touches`; carried in the act queue's object index;
  consumed by the stratum resolver, which routes collisions to `contest`.
- **Cut the touches declaration and you lose:** the ability for two persons to want the same thing
  without a designer having listed the pair. Every collision becomes an authored case.

---

## 2. ONE RESOLVER, THREE FIDELITIES

### 2.1 The refusal, taken seriously

The corpus's first option is *don't build a second resolver at all.* Total War is the only precedent
with two paths and the only one with a twenty-year unsolved divergence. So I take the refusal
literally: **there is one function, `resolve`, and F0/F1/F2 are the same call with one integer
changed.**

And here is the honest finding that makes this affordable, which I want stated before the table
because it reframes the whole problem:

> **The three fidelities are not a performance feature.** §10's arithmetic shows a fully individuated
> battle costs ~5,000 `choose` calls, which is nothing. F0 exists because **the player cannot watch
> two hundred contests a season**, not because the machine cannot run them. Therefore the *correct*
> amount of difference between F0 and F2 is **as little as possible**, and any difference that
> exists must be justified by attention, not by cost.

### 2.2 The exchange loop (the process, once)

```
contest(place, sides, stake, fidelity):
  participants := persons present, individuated to depth D(fidelity);
                  everyone else held as cohorts
  repeat until terminal:
     for each participant:  view := assemble(K=12)          # Phase 3, nested
     for each participant:  act  := choose(participant, view) # Phase 4, nested
     resolve the exchange's act set                          # Phase 5, nested
     witness the exchange's events into participants         # Phase 6, nested
  terminal := one side's position destroyed
            | a named fault (evasion, self-contradiction, silence when pressed)
            | withdrawal
            | the clock (the standing date closes, night falls, the tide turns)
```

This loop is the *only* resolver in the game. A battle outside Stillhelm, the Masterpiece
Examination committee, a Dicastery of Doctrinal Adjudication hearing, and two brothers arguing over a
barn are the same call with different act vocabularies and different stakes.

### 2.3 The fidelity table — exactly what is dropped

| | **F2 PLAYED** | **F1 WITNESSED** | **F0 AUTO** |
|---|---|---|---|
| engine | the exchange loop | the exchange loop | the exchange loop |
| exchange count | full | full | **full** |
| claim budget K | 12 | 12 | **12** |
| act vocabulary | full | full | **full** |
| individuation depth D | every participant | ledger-named ∪ role-holders ∪ decisive ∪ Knot-partners | role-holders ∪ decisive ∪ Knot-partners |
| the rest are | — | cohorts | cohorts |
| cohort rolls | none | some | most |
| roll variance | native | **variance-matched** | **variance-matched** |
| player's own choice | every exchange | **branching exchanges only** | standing orders only |
| presented to the player | yes | partially | no |
| **dropped at this step** | — | the player's deliberation on exchanges where their option set does not branch | **the within-cohort identity of the interchangeable** |

Note what is **not** on the drop list at any step: exchanges, the claim budget, the act vocabulary,
the terminal conditions, the factor sheet, or the ability of any named person to die.

### 2.4 The variance-matched cohort roll — the actual mechanism

A cohort of weight *W* whose members each roll a pool *p* would, individuated, produce successes with
mean *W·μ(p)* and variance *W·σ²(p)*. Rolled once as a block with a bare mean, it produces the right
mean and **zero** variance — and that is precisely the "formula approximating a process" defect. So
the cohort rolls once, with the dispersion added back:

```
successes(C) = round( W·μ(p) + sqrt(W)·σ(p)·Z ),   Z ~ standard normal, clamped ±3
```

This is exact to the second moment by construction. The cost is *one* roll instead of *W*. The mean
is identical to the individuated run; **the variance is identical too**, which is the property that
twenty years of auto-resolve complaints were actually about — auto-resolve results feel wrong not
because they are biased but because they are **too close to the mean**, so the underdog never wins
and the rout never happens.

What is genuinely lost: **third and higher moments.** A block roll cannot produce the cascade where
one specific man's failure propagates. That is bounded in §2.5 and it is the only unbounded-looking
hole in the construction.

### 2.5 The two rules that bound the loss

**Rule A — decisive individuals are never in a cohort.** The individuation depth *D* always includes
any person whose act could produce a **named-subject event with downstream consequence**: an occupied
role, a Knot partner, an office-holder, anyone carrying a named object (a standard, a writ, the
Examination piece), anyone another participant's ledger names, and anyone whose act this exchange has
outcome variance above a threshold. So every cascade path is individuated at every fidelity, and the
cohort carries only interchangeable mass.

**Rule B — casualties individuate retroactively, but only into memory that already existed.** When a
cohort loses weight, the dead are named **only for persons already individuated in someone's
ledger.** If nobody knew his name, nobody notices he is gone — which is T4-correct and free. This is
also the whole answer to CK3's 24,000-character problem, arriving from the other direction (§8.2).

- Closed loop: produced by the exchange loop at any fidelity; carried as events with named subjects;
  consumed by `witness`, identically at all three fidelities.
- **Cut variance-matching and you lose:** upsets. Every auto-resolved contest returns the favourite,
  the Löwenritter never lose a skirmish they should have won, and the strategic layer becomes
  arithmetic the player can do in their head.

---

## 3. TESTING THE FAILURE MODE, NOT THE MEAN

The corpus's reframe is worth more than either pole and I adopt it whole: **do not tolerance-test the
mean.** The question is *does F0 ever produce a result a player who had played it would call
unrecognisable?* — a distribution-**shape** question. Three tests, in order of severity.

**T-S (SUPPORT — the hard gate).** Enumerate the *classes of named-subject event* the F2 process can
produce for a given contest: `commander killed`, `role vacated`, `cohort routed`, `place taken`,
`person captured`, `Knot ruptured`, `standard lost`, `named fault conceded`. **Every class F2 can
produce, F0 must be able to produce.** If F2 can kill the commander and F0 cannot, F0 is broken no
matter how well the means agree — and this is the test twenty years of mean-calibration never ran.
Rule A above is what passes it.

**T-D (DISTRIBUTION SHAPE).** Run the same contest 200× at F2 and 200× at F0 from the same world
state with independent seeds. Compare outcome distributions by a two-sample shape statistic, not by
means. Variance-matching (§2.4) is what passes this; a failure here means the compression lost a
moment and points at *which* one.

**T-F (F1 IS THE DANGEROUS TIER).** The corpus is right that F1 is structurally closest to scalar
collapse, and the reason is precise: **at F1 the player is present and their own choices are being
auto-filled.** If standing orders are a slider — *aggressive / balanced / cautious* — then the
player's presence produces a *worse* result than their absence would, because a slider is the one
place in the design where a scalar re-enters the decision path. So:

> **Standing orders are written in the same act vocabulary as F2 choices.** An ordered list of
> conditional acts over the player's own view, e.g.
> `1. if my flank cohort's chain is broken → rally`
> `2. if Gerik is within reach and wounded → extract`
> `3. if the van holds and the Row's cohort is unbroken → press`
> `4. otherwise → hold`
> and after the scene the log names which order fired at which exchange and why.

This is also the R answer for F1: standing orders are a real player artifact with real trade-offs
(order 2 above will cost you the press), not a difficulty setting.

**Legibility, since these scenes may never recur.** Every contest publishes, *before* the first roll,
a **factor sheet**: at most seven rows per side, each a signed contribution in pool dice with its
source named, plus a **band** for the likely outcome. The discipline, taken directly from the
corpus's cheapest steal:

> **Publish every input. Publish a band. Never publish the trigger point.**

Worked: a Crown levy contesting a Restoration barricade in Oastad shows
`+14 numbers · +6 the serjeants' drill · +3 Praefect Roth's Will (share 0.31) · −5 two seasons short
rations · −4 the ranks are 6-in-10 Southern Einhir and the proposition is caste enforcement · −3 the
serjeant's role is vacant and unfillable here · band: likely to break the line, unlikely to hold it
after.` Six rows, all readable, no trigger point.

- Closed loop: produced by the pool assembler as a by-product of building the pool; carried in the
  contest's opening event; consumed by the player's interface and by the after-action log.
- **Cut the factor sheet and you lose:** the player's ability to learn the model at all. Without a
  GM, an unexplained roll is indistinguishable from an arbitrary one, and N-6 wins.

---

## 4. THE ANTI-LEVERAGE RULE, AND AN HONEST ANSWER TO N-3

### 4.1 The rule, generalised past battle

The corpus's only concrete anti-leverage finding: *a personal→unit effect must be a fraction of the
unit's own size or cohesion, never a flat amount.* Generalised:

> **Fractional Contribution.** A person P acting on a collective C contributes
> `Δ(C) = φ(P,C) · Q(C)`, where `Q(C)` is C's own relevant quantity and `φ` is dimensionless.
> **No act anywhere in the game adds a flat amount to a collective.**

Applications, all of them the same line:

| P acts on C | Q(C) | what fractional means |
|---|---|---|
| Grandmaster Ehrenwall on a Löwenritter formation | its weight × its pool | she moves a fraction of the body, not +2 dice |
| Praefect on Goldenfurt's Order under riot | the settlement's own Order capacity | a strong town is steadied more, absolutely; equally, proportionally |
| Confessor Himlensendt preaching at a parish | the congregation's current stance mass | he moves a devout parish further and an indifferent one barely — no preaching an empty room into fervour |
| A backer on a petition | the petition's assembled weight | backing 401 adds less than backing 4 |
| A Restoration recruiter on a hamlet cohort | the cohort's existing grievance mass | **you cannot recruit where there is no grievance**, at any capability |

That last row is the rule doing real political work: it makes Yrsa Vossen structurally unable to
manufacture a revolt in a contented Valorsmark parish, and it makes Duke Magnus Vaynard's caste
grievance a *precondition* for the Restoration rather than an accelerant. No rule mentions either of
them.

### 4.2 Why constant φ is not enough, and the fix

If φ is a constant, one person's relative leverage is scale-invariant — good. But **the number of
persons who can contribute grows with N.** At N = 1000 there are thirty officers; thirty constant φ's
sum to thirty times one, and personal leverage inflates back out of band. That is the trap
Dominions' commander anchor and Total War's lord aura fall into from opposite sides.

So φ is **allocated from a budget the collective owns, not granted per person:**

```
Φ(C)   = Φ₀ · chain(C) · concord(C) · supply(C)          # the command budget, Φ₀ = 0.60
share(P,C) ∝ role_weight(role(P)) · standing(P, C),  Σ share = 1
φ(P,C) = Φ(C) · share(P,C)
```

- `Φ₀ = 0.60` — the ceiling on how much of any collective outcome persons may determine. **Forty
  percent of every outcome belongs to the mass, the ground and chance, at every N.**
- `chain(C)` ∈ [0,1] — the fraction of C's weight whose command path reaches an occupied role, where
  **each link requires the subordinate to hold a current claim naming their superior.** This is where
  `witness` enters the middle of a melee (§5.2).
- `concord(C)` = 1 − (mean |stance deviation toward the proposition at stake|)/5. Persons who disagree
  about *why* they are fighting fight worse, mechanically.
- `supply(C)` — larder satisfaction over two seasons, clamped.
- `role_weight` — commander 8, wing captain 2, serjeant 1, standard 1, scout 1, chaplain 1.

**The consequence is the whole result.** A commander of a warband with one captain holds
share ≈ 8/10 = 0.80. A commander of a levy with six captains and twelve serjeants holds
8/(8+12+12) = 0.25. **Personal leverage is inversely proportional to organisational depth, and
organisational depth is what grows with N.** So `φ` is bounded at every N by construction, not by
tuning.

### 4.3 How a person still matters at N = 1000

Not by adding to the outcome — that channel is closed. By **acting on the share graph**:

- Kill the man holding 0.25 and his share redistributes to whoever the command succession names —
  **at a cohesion cost, and only once someone has been told** (§5.2). A commander who dies unseen
  leaves his share *unallocated*, and `chain(C)` falls until the news travels.
- Turn him. A share-holder whose stance toward the proposition inverts drags `concord` down for the
  whole of the weight under him.
- Vacate a role you cannot refill. §5.3 makes this the sharpest lever in the game and makes it a
  caste question.
- Cut supply. `supply(C)` is the larder, which is the hearth rung, which is where a single smuggler
  with a boat operates.

At N = 1, the share graph has one node and this degenerates to "the person is the collective," which
is correct. The mechanism is continuous across the whole range because the graph is the same object
at both ends.

### 4.4 Is this solved, or bounded? — bounded, and here is what it does not cover

**What is proved.** Personal contribution as a *fraction of outcome* is invariant in N. That is an
identity in the construction, not a tuning result, and it holds from N = 1 to N = 10⁶.

**What is not proved, and I will not claim it.** That the *experience* of leverage holds at N = 1000.
The construction converts "add to the outcome" into "act on the share graph," and whether acting on a
share graph *feels* like personal agency is a question about **reach** — can the player find out who
holds 0.25, get near him, and act on him? — not about arithmetic. That is an access and investigation
problem (T9's territory), and this document does not solve it; it makes it the right problem.

**The falsifier.** Run a fixed player intervention (assassinate the highest-share officer) against
formations at N = 10, 100, 1000, 10000, and measure the shift in the contest's outcome distribution.
If the shift's *magnitude as a fraction of the distribution's own spread* is flat in N, the bound
holds. If it decays, `chain` is recovering too fast and the succession-by-witness rule in §5.2 is
mis-parameterised. If it grows, `role_weight` for commander is too high relative to depth.

- Closed loop: `Φ` and `share` are produced by the pool assembler from persons present and their
  command claims; carried nowhere (recomputed per exchange); consumed by `lead` and the factor sheet.
- **Cut the command budget and you lose:** the reason to keep a specific person alive at scale, and
  the distinction between a mob and a formation. Both collapse into "how many bodies."

---

## 5. THE BATTLE SEAM

### 5.1 The defect, at the root

The failure to avoid is a seam whose contract has **the faction fighting**: derive one field from a
faction's military stat, label the combatant with the faction id, and the commander becomes a doorman
whose attributes never reach the outcome. The root fix is a signature:

```
battle_contest(place, act_sets, stake) -> events
  reads : persons present — individuated and cohorts — with all six substrate fields
  reads : the command relation among them (the share graph)
  reads : the place — terrain, works, the settlement's Defense if it has one
  reads : each participant's stance toward the proposition at stake
  writes: events with NAMED SUBJECTS — deaths, woundings, role vacancies,
          the rout of a specific cohort, a capture, the place changing hands
  NEVER reads: a faction id · a faction military stat · a national strength number
```

**There is no army object and no battle object.** An "army" is a *faction footprint at a place plus a
share graph* — `presence(f, n)` from the substrate, plus a command relation over the persons in it.
A battle is a contest whose act vocabulary is `{strike, hold, flank, press, rally, yield, extract,
break}` and whose stake is the place and lives. It has no fields of its own, so there is nothing for
a faction stat to be written into.

This also satisfies ARCH R-5: a faction has no verbs. The Church of Solmund cannot fight. Grandmaster
Sigrid Ehrenwall can, with the persons who came when she called.

### 5.2 Losing a specific person, three ways

**(a) The share, and the succession that must be seen.** When a share-holder dies, the succession
rule names the next occupant of the role — but the share does not transfer until **the subordinates
hold a claim naming him.** `chain(C)` counts only links where the subordinate's ledger currently
asserts who commands him. So a commander killed in the open, in view of the line, costs one exchange
of `chain` degradation. A commander killed in a wood, at dusk, out of sight, leaves the share
unallocated until a runner is chosen, survives, and is believed — and `chain(C)` bleeds the whole
time. **`witness` doing load-bearing work in the middle of a melee is exactly T4 at the seam**, and
it is free because the machinery is the substrate's.

**(b) The Knots.** The setting is explicit: a partner's death is a rupture trigger. Rupture costs
Disposition → −3, mutual Composure damage, Coherence −1, and for a Close Knot a **Conviction scar**.
So a death in the line at Stillhelm propagates Coherence damage to a partner who is three provinces
away in Himmelenger, that same season, through a channel that exists for other reasons. That is T6
landing on one named person with no down-stroke mechanism invoked.

**(c) The claims.** Whatever he alone knew dies with him unless he told it or wrote it. §9 makes this
the whole latency model, and it is why *killing a man is a way of destroying information* — which is
what makes the 1218-AG hunting accident work as a design object rather than a plot point.

### 5.3 Role, not biography — and why that makes caste a battlefield mechanic

The refusal is exact: **gate on a class/role and losing a person is a promotion opportunity; gate on
"the officer with cavalry history" and one death costs you cavalry permanently.** So:

- A formation's act vocabulary is unioned from its **occupied roles**, never from persons'
  biographies. `flank` is legal iff a wing-captain role is occupied. `rally` iff a serjeant or
  standard is.
- A role is occupied by any present person meeting the role's **threshold**: a capability floor plus
  a **mark**.
- Killing the occupant *vacates* the role. Vacancy is filled in the next exchange by the
  highest-standing present person who meets the threshold. Capability is never lost permanently.

And now the setting does the rest, with no rule naming it. The mark half of the threshold is exactly
the per-institution rank gate the setting describes — caste is enforced by institutions, not by law,
so it is a gate per rung and per body:

| formation | serjeant's mark requirement | who can fill a vacancy in Grauwald, where the ranks are 6-in-10 Southern Einhir |
|---|---|---|
| Crown levy | Standing 3+ (public deeds or inner-circle sponsorship) | almost nobody present |
| Church-raised militia | Church standing | a Southern Einhir Canon is "a scandal" — so, nobody |
| Löwenritter | order-mark, caste-open | the best man present, in one exchange |
| Niflhel | none — caste-open by design, waterfront work needs Southern Einhir | anyone |

A Crown levy that loses its serjeant in Grauwald has a vacancy it **cannot fill**, and `chain(C)`
stays broken for the rest of the battle. A Löwenritter formation closes it in one exchange. Nothing
in the code says "caste"; the setting's institutional gates plus the general role mechanism produce
it. And it gives Duke Magnus Vaynard's anti-caste programme a **military payoff** — breaking the caste
system makes Varfell's levies more resilient than Valorsmark's — which is what makes the political
fight about something rather than about virtue.

- Closed loop: role thresholds are produced by the institution's own mark gates (which are persons'
  stances at an admission gate, per the substrate); carried on the role definition; consumed by the
  vacancy filler each exchange and by the factor sheet.
- **Cut role-gating and you lose:** promotion as a consequence of death, and the entire mechanism by
  which institutional exclusion shows up as a *capability* rather than as a flavour tag.

---

## 6. THE LEADER IS NOT A MODIFIER

A flat shift of size X on a d-pool is worth roughly `X / (0.8·√Pool)` — **more to a small pool than a
large one.** So a flat leader bonus is systematically worth more to a weak faction, which inverts
every intuition the strategic layer depends on. The in-band form is the corpus's: **change the option
set and the pool source, never add.**

> **The leader operator.** `lead(P, C, act)` does exactly two things:
> **(a) OPTION SET** — `vocabulary(C) ∪= practices(P)` for this exchange.
> **(b) POOL SOURCE** — on the fraction `φ = Φ(C)·share(P,C)` of C's weight, that weight's roll draws
> the named attribute **from P instead of from C's own mean**. The remaining `1−φ` rolls its own.
> **There is no third thing, and there is no addend.**

Check the direction: substitution moves `W·φ·(P's attribute − C's mean)`, which is proportional to W.
As a fraction of an outcome that is also proportional to W, it is **constant in N** — the exact
inverse of the flat-bonus pathology. And it makes cohesion mean something in plain language:
`Φ·share` is *how much of this body is thinking with its commander's head.*

**Commander.** Option set: a commander who holds the `feint` practice makes `feint` legal for cohorts
under his share; without him it is not in the vocabulary at all, and no amount of numbers substitutes.
Pool source: the cohorts fight with their own Strength and Endurance and **his Will and Focus**, on
the φ fraction. A levy under Ehrenwall rolls its own bodies and her nerve.

**Governor (praefect, ducal reeve, gate warden).** Option set: which **dispensations** they may issue
at the settlement's standing dates — and that set is gated by office *and* by what the container's
judging set will tolerate, so a praefect who has spent his regard cannot issue what he could last
season. Pool source: when Goldenfurt resists a shock — a dearth, a riot, a Restoration barricade — the
settlement's Order roll draws its Focus/Acuity component from the governor on the φ fraction, where
here `Φ` is *administrative* cohesion: do the ward-holders' ledgers currently name him, has he been
present, does he speak Einhir. A governor who has not appeared in four seasons has `chain` near zero
and contributes nothing, without a single absence timer (§7.4).

**Negotiator (envoy, advocate, Dicastery proctor).** Option set: which **stasis rungs** they may
occupy in an argument — deny the act / deny the label / admit-and-justify / challenge the venue. A
negotiator without the Precedent conviction and without a legal mark cannot open the jurisdiction
rung *at all*, which is why Hafenmark's Parliament sends the men it sends. Pool source: an envoy
substitutes their own Attunement and Charisma **for their absent principal's standing** — which is
what an envoy *is*. And their presence changes who may be a **respondent** to a petition, which is an
option-set change one rung up: sending Elske to Almaic Kyriakos makes the Doux a legal respondent for
Almud's merchants, and nothing else does.

- Closed loop: produced by a person choosing `lead` (which spends their act); carried in the
  exchange's pool assembly; consumed by the roll and shown on the factor sheet as a named row.
- **Cut the leader operator and you lose:** any reason for a specific named person to be at a specific
  place, and the difference between sending Ehrenwall and sending an equally-skilled stranger.

---

## 7. THE PLAYER IS ONE PERSON

### 7.1 What they are

A person record. Address, Marks, Capability, Stance, Memory, Ties. One act per season. The same
`choose(person, view) -> act`. **The interface is the view, rendered** — there is no second function
and no second data path.

### 7.2 What they get that an NPC does not: deliberation time, and only that

An NPC's `choose` runs a bounded policy over K = 12 ranked claims. The player may sit with the same
twelve claims for an hour, re-read their whole ledger, chase provenance, and plan four seasons out.
**That is the entire player advantage, and it is a large one** — a player who models other persons'
views will consistently out-plan a bounded policy. It is also the *right* advantage for this game,
because it is an advantage at exactly the thing the game is about.

### 7.3 What they do NOT get

- **No world argument.** Ever. The map shows what the ledger asserts.
- **No omniscient map.** A province they have had no news from displays the **last claim they hold**
  about it, with its date and its source visible. **Stale claims render as current**, because that is
  what a belief is. The date is shown; staleness is not flagged. If Duchess Inge Baralta's banner
  still flies over Oastad on your map, it is because that is the last thing you were told.
- **No pause-the-world.** The tick runs whether or not the player submits. **A player who does not
  act has chosen `abide`.**
- **No event feed.** Events reach the player through `witness`, exactly like everyone. The "news" is
  their ledger's new rows, with sources.
- **No extra acts, no extra reach, no faction-level verbs.** The player commands what their share
  graph says they command.

### 7.4 Ignorance must cost — four mechanisms, none of them a timer

**(1) Your act is evaluated against the world, not your view.** Petition the wrong respondent because
your ledger still names Aldwin in a seat he lost last season, and the petition is carried to a man
with no power to answer it: the carrier spends regard, you get nothing, and the backers learn only
that it failed. This costs nothing to implement — it falls out of the signature rule.

**(2) Standing dates pass without you.** The docket is published by telling, not by notification. If
no one told you the Kettlemakers' Examination sits this autumn, you do not contest it, and the seat
goes to whoever did. A real prize, lost silently.

**(3) Your holdings forget you — by memory decay, not a governance meter.** `Φ` for a settlement is
built on `chain`, and `chain` counts only links where the subordinate's ledger **currently asserts**
who decides here. Claim confidence decays in Phase 7 by the same universal rule that applies to every
memory in the game. Below the assertion floor, the ward-holders stop counting you as the answer, and
their share redistributes to whoever *is* present. **You lose Goldenfurt by being forgotten.** This
passes the no-scheduled-recovery refusal on a technicality that is not a technicality: the decay is
on the *knower's* confidence, a property of memory, and it makes ignorance grow rather than restoring
anything on a cadence. The mitigation is not a timer either — send a telling. A letter, a factor, a
Knot. That costs an act slot, yours or a client's, and it can be intercepted, delayed or forged.

**(4) Your allies petition you, and the drop is charged to you personally.** An ally's need becomes a
petition; if you are in Himmelenger it reaches a container you are not at; the carrier drops it;
grievance deposits toward **you by name.** You come home to an injury you were never given the chance
to answer. That is T8's sharpest edge and it is why the world not needing you is a threat rather than
a boast.

- Closed loop: produced by the ordinary act/witness/decay machinery with no player-specific code;
  carried in other persons' ledgers; consumed the day the player next needs those persons.
- **Cut the ignorance cost and you lose:** any reason to be anywhere, and therefore the meaning of
  travel, delegation, and the whole strategic-layer question of *where do I spend my presence*.

---

## 8. CHURN WITHOUT CONTENT AUTHORING

### 8.1 Generate persons on demand, never on a clock

CK3's ambient model mints six or seven parentless sixteen-year-olds a month and reaches 24,000
characters in late saves. The refusal is absolute: **the clock never mints a person.**

The world holds a **demographic envelope** per containment node — counts by age band, marks bundle,
and capability distribution, carried as cohort weight. Births and deaths move *weights*. A person
**record** is minted only when one of five things happens:

1. an event names them, 2. a telling puts them in someone's ledger, 3. they occupy a role or office,
4. they enter a Knot, 5. they are individuated as decisive in a contest.

Minting draws address from the cohort, marks from the cohort plus its within-cohort variation,
capability from its distribution conditioned on whatever the naming event implies, and stance from
its aggregate plus dispersion. **Memory is the trick that makes on-demand minting consistent:**
tellings are stored *at the channel*, not per-person, until individuation — so a person minted in
season 40 is handed the claims their address's channels would have deposited, replayed cheaply. They
have a plausible past because their *channel* has a real one.

### 8.2 Reabsorption — the bound CK3 lacked

A person record **de-individuates** in Phase 7 when they hold no role, no Knot, no stance above the
commitment threshold, and **no other person's ledger names them.** Their state folds back into the
cohort as a weight adjustment.

The flow is bidirectional, and the standing population is therefore bounded by **how many people
anyone remembers** — which is the correct bound, is in-world meaningful, and needs no cap constant.

- Closed loop: produced by the mint triggers; carried as a person record; consumed by every system,
  and returned to the cohort by the Phase-7 sweep.
- **Cut on-demand individuation and you lose:** the ability for anyone to matter who was not
  important when the world was made. Every consequential person becomes one the designer minted.

### 8.3 No scheduled recovery, stated as a phase rule

> **The only clock-driven quantities in the game are matter, bodies, and the confidence of a memory.
> Every social quantity — standing, regard, grievance, cohesion, commitment — moves only when an act
> causes an event.**

Enforced by Phase 1's membership, not by discipline. A timer that restored standing on a cadence
would convert a consequence system into a treadmill; there is no phase in which such a timer could
run.

**The suppression rule, without a flag.** A coercive act that "solves" an unrest event does **not**
change the aggrieved persons' stance toward the proposition. It adds a stance toward *acting on it* —
fear — and fear decays by the same witnessed-presence rule as everything else. Meanwhile the original
grievance claim sits in the ledger at full confidence and is **told to children** along the hearth's
transmission edge. Next time it fires, the backers already hold the claim, so the petition assembles
in one season instead of four. **A lower trigger threshold, with no threshold object anywhere.**

### 8.4 No mechanism engineered not to fire — the recoverability test, run

The test: **maximum available mitigation against maximum accrual; is the net recoverable?** Stance
`s ∈ [−5,+5]`; all moves fractional, `Δs = g·λ·(target − s)`, where `λ` is the fraction of the cohort
who *learn of it*. Subject: the Southern Einhir hamlet cohort outside Goldenfurt, weight 400.

| | act | g | λ | target | factor on distance |
|---|---|---|---|---|---|
| **accrual** | 4 petitions dropped | 0.25 | 0.70 | −5 | (1−0.175)⁴ = 0.463 |
| | granary opened to the Row only | 0.20 | 0.90 | −5 | 0.820 |
| | *combined* | | | | **0.380** |
| **mitigation** | governor `appear` at the hamlet | 0.15 | 0.60 | +1 | 0.910 |
| | 3 petitions carried and won | 0.25 | 0.50 | +1 | 0.670 |
| | 12 standing-holders `vouch` | — | 0.80 agg. | +1 | 0.700 |
| | *combined* | | | | **0.427** |

From a fully aggrieved `s = −4.5`: mitigation gives `+1 − (5.5 × 0.427) = −1.35`. Accrual then gives
`−5 + (3.65 × 0.380) = −3.61`. **Net +0.89 per season with both at maximum.**

**Verdict: it fires, and it is recoverable, and the recovery costs everything.** Sixteen act-slots —
the governor, three carriers, twelve standing-holders — is essentially the entire governing capacity
of Goldenfurt for the season. Nothing else gets done: no granary work, no wall, no trade. Which raises
next season's needs, which raises next season's petitions. So the mechanism avoids both poles: not
EU4's estates (mitigation genuinely works), not Imperator's governors (it is not unavoidable). And
the *actually* dominant line is not to spend sixteen slots on remedy but to **stop dropping
petitions** — which costs the carriers their standing with their own judging sets, which is a
different person's problem, which is politics.

**R check on the carrier's fork.** CARRY gains the backers' regard and costs the opposing judging
set's; DROP is the inverse. Both are durable stance rows; **neither decays on a clock**, so neither
has decaying gain against compounding cost. The only asymmetry is `λ_drop = 0.70 > λ_grant = 0.50` —
the aggrieved talk more — which is emergent from the telling system rather than tuned, and is a nudge,
not a dominance. Which way the fork resolves depends on the carrier's *address*: Burgher Aldwin Roth,
a Kettlemaker, carrying an Einhir hamlet's petition faces an opposing set that is his own community.
The fork is decided by who you are, which is the correct answer.

---

## 9. LATENCY — decided up front, and it needs no new object

A substrate with no cross-season transport forecloses sleeper consequences, delayed reprisal and
slow-travelling news wholesale. So the decision is made here, explicitly, and the finding is that
**latency requires no object at all:**

> **A latent act is a stance toward a proposition of the form `act(…)`, held above the commitment
> threshold, whose act is not in the person's option set until they hold an enabling claim.**

Phase 0 recomputes option availability from claims. Phase 4's `choose` ranks by stance. That is the
entire fuse mechanism, and it is two things the substrate already has.

### 9.1 The four rulings

| | ruling |
|---|---|
| **May persist indefinitely** | claims; stance rows (including act-propositions); Knots and their strain; claims written to a **physical carrier** — a document, which persists past its writer at the place it is kept and is found by a `search` act; contingent claims on occupied seats banked at a marriage. |
| **May fire late** | any act whose enabling claim arrives late. Reprisal, blackmail, a debt called in, a dormant claim on a seat admitted the season its vacancy is *believed*. There is no maximum delay. |
| **Carries a dormant flag** | **nothing.** There is no flag object. Dormancy *is* an act-proposition with an unmet enabling claim — one mechanism, not two. |
| **May never persist** | (a) the world's true event record, as anything an agent can read — the spine's refusal, unamended; (b) a dead person's ledger, unless told or written; (c) **an act from a dead bearer.** A latent act whose bearer dies is inherited or lost: if he told it — a claim plus an obligation edge — it re-forms in the hearer with the hearer's own stance and their own fuse. Otherwise it dies with him. |

That last line is what makes assassination a real solution to a real problem, and what makes
**telling someone your secret** a deliberate, dangerous, irreversible act.

### 9.2 The 1218-AG hunting accident, carried sixty years

The setting requires a twenty-year-old secret that surfaces, whose perpetrator is deliberately
unresolved. Traced through the mechanism, with nothing added:

1. The event happened in 1218. It is in the world. **No agent can read it.**
2. A huntsman witnessed it and deposited `(Almqvist-the-first, killed_by, X, 1218, firsthand, 0.9)`.
3. He told no one — or told one person under a Close Knot, or **wrote it.** A written claim has a
   physical carrier and a place. The place a sixty-year-old written accusation would be kept is the
   **Dicastery of Doctrine and Archives**, because the Church holds the archival monopoly it was
   granted under the Altonian containment grant. That is where the cage-became-a-school is load-bearing.
4. He dies. His ledger dies with him. **Only the document survives.**
5. Sixty years on, a person performs `search(archive)` at F2 — a field investigation, first-class,
   T9. The claim enters their ledger with source `firsthand(document)`, `when = 1218`, confidence high
   because the document's provenance is checkable and its independence root is its own.
6. They `tell` it. Credulity and stance-toward-speaker roll at each hearer.
7. **The contradiction is automatic**, because claim identity is a tuple with a mandatory interval:
   the 1218 claim collides with every claim asserting the deed-monarchy's founding was clean. It does
   not need a designer to notice.
8. Every person whose stance is grounded on that legitimacy now holds a contradiction; obstinacy sets
   how many more it takes. And **every act-proposition fused on "if I come to believe the throne was
   taken by murder" enters its bearer's option set that season** — including Duchess Inge Baralta's
   Baralta Crown Claim, banked at her marriage, dormant, and now legal. If the Church's own succession
   is contested in the same window, the consecration crisis composes with it, because both are
   propositions before overlapping standing dates.

**And if nobody wrote it and the huntsman told nobody, the perpetrator is unknowable forever.** The
world holds a fact no agent can ever reach. That is not a gap; it is the design's most extreme
statement of T4, and it is the reason the perpetrator can be left unresolved without the engine
needing a placeholder.

- Closed loop: produced by `witness` at the original event; carried by a person's stance table, or by
  a physical document at a place; consumed by Phase 0's option-availability recomputation the season
  the enabling claim lands.
- **Cut latency and you lose:** every consequence that outlives its cause. No reprisal, no
  revelation, no inherited grudge, no dynastic claim, and the campaign has a memory of exactly one
  season.

---

## 10. WHAT "THE WORLD IS 100% RESOLVED" HONESTLY MEANS

**Target: a season tick in ≤ 2 s on a mid-range machine.** A fifty-year campaign is 200 ticks ≈ 7
minutes of simulation, which is affordable.

**The population is not the record count.** Modelled population of the peninsula: ~1.2 million as
*weight*. Records:

| | count | basis |
|---|---|---|
| containment nodes | ~1,500 | 3 duchies · 14 provinces · 35 settlements + Himmelenger + Schoenland · districts · ~800 community nodes (guild rows, Einhir hamlets, Crown-Latinate quarters, parishes, Restoration cells) · hearths individuated on demand |
| **cohorts** | **~9,600** | ~800 communities × ~4 marks bundles × ~3 stance buckets |
| **individuated persons** | **3,000–6,000 typical, 8,000 soft ceiling** | bounded by §8.2: you exist as a record while someone remembers you |
| **acts per tick** | **≤ 17,600** | ≤8,000 persons + ~9,600 cohorts, one each |
| ledger cap L | 200 / person, 20 / cohort | eviction is forgetting (P-13) |
| view assembly | ~2 × 10⁷ comparisons worst case | 17,600 × ranked top-12 of ≤200, ranking maintained incrementally |
| **witness deposits** | **≤ 120,000 / tick** | see below |
| contests | 0–3 battles, 20–200 social | see below |

**Witness fan-out is the real cost, and the cohort is what tames it.** An event's witness set is the
persons present plus the channels it touches, and **a channel deposits into a cohort as one claim, not
into its members.** The crier's proclamation of a ducal dispensation in Goldenfurt deposits ~6 cohort
claims and ~40 individuated claims — not 12,000. When a cohort member later individuates, they
inherit the cohort's channel claims (§8.1). This is the same primitive doing three jobs.

**Contest cost, and the honest finding.** A battle at F0: 12 exchanges × ~70 participants (20 cohorts
+ 15 individuated per side) = **840 `choose` calls.** At F2, fully individuated at 400 a side: 12 ×
800 = **9,600 calls** plus presentation. Both are trivial. **The compute case for auto-resolve is
weak, and that is the point** (§2.1): F0 exists for the player's attention, not the CPU, which is
precisely why the only thing it is permitted to vary is individuation depth.

### 10.1 What the design does when the budget is exceeded, in order

1. **De-individuation sweep** — fold the least-remembered person records back into their cohorts,
   lowest salience first.
2. **Ledger eviction** at L — people forget. In-world correct; costs nothing but knowledge.
3. **Cohort coarsening** — merge cohorts whose stance buckets have converged; reversible the moment a
   spread widens or an event names a member.
4. **Exchange budget per contest**, last resort: cap total exchanges across a season's contests and
   spend them on the contests with the highest outcome variance. Note this degrades *terminal
   conditions*, so it is the last thing to give and the first to restore.

### 10.2 What is refused, absolutely

> **There is no simulation radius.** No region is paused, frozen, sampled, or run on a different
> model because the player is elsewhere. A distant province is cheap because it is **coarse**, not
> because it is **stopped.**

Every shipped mitigation for this problem in the genre is a radius, and a radius is a direct
contradiction of T8 — the world would churn *near the player*, which is the same thing as not
churning. The four steps above are all resolution reductions, all reversible on demand, and all
applied uniformly across the map without reference to where the player is standing.

---

## 11. WORKED TRACE — one season, no player present

**The player** is a Free Master of the Kettlemakers in Goldenfurt (Grauwald, Varfell), Southern
Einhir by heritage, who passed the Masterpiece Examination nine years ago. They are in Himmelenger,
two seasons into petitioning the Dicastery of Temporal Affairs for a guild tithe exemption. Their
shop is held by their apprentice **Gerik Strand**, who is this autumn's Examination candidate.

**Autumn 1281.**

**Phase 0 — CALENDAR.** Goldenfurt's tithe reckoning fires. The Kettlemakers' Examination sits (it
sits every third autumn). Journeyman **Halvard Uln**, kin of Maret Uln, holds a stance at +5 toward
the proposition `reprisal(the committee's speaker)`; its enabling claim — *the Examination rejected
another Southern Einhir candidate* — does not yet exist, so the act is not in his option set.

**Phase 1 — SETTLE.** Grauwald's autumn is wet. Harvest resolves short. Fourteen hearths in the
Einhir hamlet outside the wall fall below mouths. The player's shop larder is fine; Gerik's own hearth
is one of the fourteen. Nothing social moves.

**Phase 2 — NEEDS.** The fourteen hearths compute an unmet food need. Gerik computes two: feed his
hearth, and pass. Praefect Roth computes a need to be seen to have fed the town.

**Phase 3 — VIEW.** Gerik's twelve claims include: from the player, *"if the Examination goes against
you, do not answer it"* (`told_by(player)`, 0.9, salience-boosted because his stance toward the player
is +4); from Halvard, *"the committee is set against us"* (`told_by(Halvard)`, 0.5). Burgher **Aldwin
Roth**'s twelve include a claim deposited last season by a guild rival: *"your Free Master is in
Himmelenger petitioning the Church against Goldenfurt's tithe"* — a distortion of the truth, which is
that the player is petitioning *for* the guild's exemption. Nobody has corrected it. Nobody is here to.

**Phase 4 — CHOOSE.** Gerik: `submit_masterpiece`. The five committee Free Masters: their votes.
Three hold stance toward the mark *Southern Einhir* at −2 or worse. Aldwin, whose stance toward the
player was +3, reads the rival's claim as disloyalty to the settlement, drops to −1, and votes
against. Halvard: `abide` — his act is still not legal. Praefect Roth: `issue_dispensation` — open the
granary to the walled communities, not the hamlet, because the Kettlemakers' judging set would punish
feeding the hamlet while the Row goes short.

**Phase 5 — RESOLVE.** *Movement:* nothing relevant. *Binding decisions:* the granary dispensation is
issued at the tithe reckoning; the Examination resolves as `contest(Kettlemakers, Free Master grade,
{Gerik})` — 3–2 against. *Contested physical:* none. *Uncontested material:* fourteen hearths spend
nothing. *Social:* the committee's speaker announces the result.

**Phase 6 — WITNESS.** Gerik deposits `(Examination, rejected, me, autumn-1281, firsthand, 1.0)` and,
because his obstinacy is low and Halvard's rumour was salient, **an inference**: `(Aldwin Roth,
turned_against, my master, …, inferred, 0.6)`. Halvard witnesses the announcement — **his enabling
claim now exists, and `reprisal` enters his option set for next season.** The hamlet cohort witnesses
the granary dispensation as `(Praefect Roth, fed the Row and not us, …)`; stance toward Roth moves
fractionally from −1 to −2.0. A Restoration cell member in the hamlet deposits, and will `tell` in the
spring.

**Phase 7 — RECKON.** Six hamlet persons `commit` at low degree to the cell over the following two
seasons. The cell's density at Goldenfurt rises. Confidence on every claim naming the player as
present in Goldenfurt decays another step; three ward-holders' assertions of who decides in the Row
drop below the floor, and their share redistributes toward Roth.

**What the player comes home to, in spring.** They have a Close Knot with Gerik, so across the winter
they felt strain accrue and Coherence drop — **a state, not a telling.** Something was wrong; nothing
said what. On arrival, they learn it from Gerik, in Gerik's version, which includes at 0.6 confidence
and delivered as fact that Aldwin Roth turned on them. Their first act home is likely to be against
Roth — on an inference from a rumour that was itself a distortion, none of which anyone lied about.

**The bill for one season's absence, itemised.** One Free Master seat not gained, and the guild vote
that came with it. One ally turned by a false claim that one `tell` before departure would have
prevented. One reprisal armed that one act slot would have disarmed. Six new Restoration commitments
inside the player's own community, which will appear in the next threat assessment attached to the
Row — and therefore to the player's name. And three ward-holders who have quietly stopped believing
the player decides anything in Goldenfurt.

**Nothing above was authored.** Every step is the six person fields, the two relations, the three
signatures, the seven phases, and the fractional contribution rule.

---

## 12. REFUSED, under E-as-a-ratio

- **A second resolver, an auto-resolve formula, or a battle model.** One exchange loop. §2.
- **An army object, a faction military stat, or any national strength scalar.** §5.1.
- **A leadership stat or any flat leader bonus.** §6 — the arithmetic makes it worth more to the weak.
- **A morale bar, an unrest meter, or a cohesion field on a container.** `Φ` is derived per contest
  from persons, claims and larders. Stored, it would be a second copy that can disagree.
- **A grievance threshold, an unrest trigger point, or a revolt gauge.** §8.4.
- **A dormant-flag object.** §9 — dormancy is a stance with an unmet enabling claim.
- **A simulation radius, a distance LOD, or a "background" model for distant provinces.** §10.2.
- **A notification feed, a quest log, or an event inbox for the player.** §7.3.
- **A standing-orders slider.** §3 T-F — it is the one place a scalar could re-enter the decision path.
- **A "cavalry history" style biographical capability gate.** §5.3 — gate on role, always.
- **A scheduled recovery, decay, or upkeep tick on any social quantity.** §8.3, enforced by Phase 1's
  membership.
- **An initiative or turn-order stat.** §1.5 — ties break on a seeded hash, never on rank.

---

## 13. CHALLENGE — two places the spine needs amending, stated rather than diverged from

**(1) `resolve` must take an act SET, not one act.** The spine writes `resolve(act, world) -> event`.
Conflict resolution (§1.5) is impossible under that signature: to know that two acts touch the same
granary, the world must see both. I propose `resolve(acts, world) -> events`. This weakens nothing —
the constraint the signature rule exists to enforce is that *agents* cannot see true state, and the
world seeing everything is what the world is for. But the change must be made explicitly, because a
singular signature would push conflict handling into a per-act pre-pass, which is where a hidden turn
order gets born.

**(2) Salience needs a floor, or motivated reasoning becomes total and correction becomes
unreachable.** The spine ranks claims by `recency × confidence × relevance × stance weight`, and says
this gives T3 for one multiplication — which is elegant and true. But if stance weight is an
unbounded multiplier and stance can be strong, then a person with a hard stance can never surface the
claim that argues against it, at any confidence. Their obstinacy is then never tested, and §3.2's
promise that *"correction comes from collision with the world"* is unreachable in principle — the
collision happens and the claim never enters a view. The design needs the correction path, and this
document leans on it directly (Aldwin's false claim must be correctable; the 1218 revelation must be
able to move people who do not want it to).

Proposed amendment: salience is `max(stance-weighted score, floor)` where
`floor = recency × confidence` for claims with `source = firsthand`. A thing you saw yourself,
recently, with high confidence, **always** makes it into your twelve. You may still refuse to believe
it — that is obstinacy's job, and obstinacy is the right place for the resistance — but you cannot
fail to *consider* it. This keeps motivated reasoning as a strong bias and stops it becoming an
epistemic prison, and it costs one `max`.
