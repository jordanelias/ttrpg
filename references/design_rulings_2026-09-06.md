# DESIGN RULINGS — Jordan, 2026-09-06, this session. Authority, not inference.

## Status: **REFERENCE (CLAUDE.md §0.05). Nothing ratifies on merge; this file is a mechanism for nothing.**
## Lane: IN. Recorded 2026-09-06.

These were given in conversation and are recorded here because **nothing else in the tree carries
them**, and this repository keeps no context between sessions. Each is quoted verbatim, then given
the reading taken and the mechanism it lands on. Where a ruling and the code disagree, §0.05 governs:
the code is right and this file is stale.

> ### ⚠ WHERE THE CITED PATHS LIVE — read this before concluding a citation is broken.
> Most rulings below cite **`engine/season/…`** and **`architecture/…`**. **Neither tree exists on
> `main`.** Both were added by PR #371 (*"ADOPT IN FULL — the season loop becomes the system, in two
> layers"*, `ED-IN-0202`), which at the time of writing is **open, unmerged, two commits behind
> `main`, and had never had CI run on it**. Read those citations against branch
> `claude/issue-368-architecture-review-2nnilz`, not against `main`. A `shape.py:NNNN` reference is
> to `engine/season/shape.py` on that branch.
>
> Recorded because a cold reader who cannot find `engine/season/` will otherwise conclude these
> rulings cite nothing — and they cite a great deal.

---

## R1 · WAR SUPERSEDES THE CHARACTER — and the casus belli decides the exit

> *"war supersedes the character, typically, but if the casus belli is purely based upon the
> character running it, then the inheritors of that war will have justification in negotiating its end."*

**Reading.** The war is uttered THROUGH THE SEAT, so it survives its declarer and the successor
inherits standing (`T-o`). The casus belli is *what the Proposition says*. When it is personal to the
dead declarer, the inheritor gains **standing in a peace negotiation, not an automatic exit** —
standing, not a switch, which keeps the ending contestable rather than automatic.

**Closes `F.32`** (`04:1136`), which asked whose edge a war is and who may end it when the declarer
dies. It was the last surviving escalation before this ruling.

---

## R2 · THE FIVE PROPERTIES — the terminal criteria

> *"you have license to do whatever makes for the best game architecture. your only constraints are
> making this as dynamic and capable and flexible and emergent and persistent as possible."*

**Reading.** The ratified refusals become **instrumental, not terminal**. Each must be justified
against these five or changed. ⚠ **But most of them were derived to serve exactly these properties**,
so a naive reading reduces what it means to increase: *no target on an Event* exists because
misattribution is a feature (that IS emergence); *only a person acts* is why obstruction and
deception need no verbs (capability per unit of machinery); *no stored aggregate* is why a resolved
view cannot go stale (dynamism). **The null result — "examined, this refusal earns its place" — is a
real finding, and must be argued rather than deferred to.**

---

## R3 · PROPAGATION, ECHOES, RIPPLING, INTERIORITY, EXTERNAL PRESSURE

> *"we need to ensure propagation across scales and domain echoes and rippling all directions in a
> probabilistic world driven by character interiorities and compromised by external incidents and
> events and pressures."*

**Reading.** Six requirements which are ONE LOOP: an act resolves probabilistically (`R-09`) → writes
state through the gate with receipts (the Receipt primitive) → WITNESS deposits **claims** per
channel, so the fact propagates as imperfect per-person belief → claims reach later decisions through
the typed `requires` (`H-72`/`H-94`) → outcomes write **interiorities** (`H-62`, `W-F`) so the person
is CHANGED, not merely informed → changed interiorities alter what they choose (`R-08`) → the loop
closes. Cross-scale: an act via a seat carries scope (`H-108`); up-direction is a READ, down-direction
is a GATED WRITE.

**The strong result: this directive adds no work.** Every link is already a tier-0 register row. It
explains why that backlog is the backlog and reorders it by what the game needs.

**"All directions" is §0.06's six** — top-down · bottom-up · vertical · diagonal · lateral ·
horizontal — and is a falsifier, not a flourish. Current floor: `DISTINCT EXECUTED SETS 2` over 89
worlds, later-decision divergence ~4%.

---

## R4 · THE WORLD MUST CHURN

> *"world must churn"*

**Lands on `F.20` — the world only decays.** `Rung.exists` and `Site.exists` have **zero producers**.
Nothing founds, builds or grows. Four routes; three need no axiom moved and all four are unbuilt:
(1) churn by NPC action — `AX-1`-native, needs the 26 non-executing verbs alive; (2) churn by matter
— generative harvest/growth/founding, arguably inside `AX-5` motion 1; (3) churn by authored occasion
— `F.31`'s world-generation roster, already called lawful, entirely unbuilt; (4) spontaneous
generation with no author — **this is a fourth motion and needs `AX-5` amended**, and its cost is that
an unauthored change is uncontestable and unwitnessable.

⚠ **Do not answer churn with a clock.** `T-c`, `D-17`/`D-21` refuse a quantity advancing with no author.

**Churn's falsifier is the same one: pressure that changes nobody's decision is scenery.**

---

## R5 · FACT IS DOCUMENTED AND BORNE BUREAUCRATICALLY, NOT ONLY REMEMBERED

> *"not every fact of the world or record of event lives in memory — much of it is documented and
> borne bureaucratically."*

**Reading — and the architecture already models this.** Three of the five WITNESS channels are
bureaucratic rather than memorial (`rosters.yaml:406-410`): `document_key` (*the person holds a live
`hold` Tenure over the Event's subject*) · `post_remit` (*holds an office whose remit covers the verb*)
· `chronicle` (*a binding_decision verb — a matter of record, public because institutional*). Only
`co_located` is memory-of-presence. Falsifiability is built too: `Record` carries `stages`, `ttl`,
`matured` and **`forgery_quality`**, and `forge`/`create_record` share `record.created` **so a
document's holder cannot tell**.

**AND IT IS DEAD ON ONE ROW.** `H-84`, tier 0: *"no verb in the resolvable vocabulary moves a Record
to another person, so no second person ever holds one."* Measured: *"the bailiff still forms ZERO
questions, because the per-change subject is the RECORD and the only person holding it is its maker."*
**`document_key` can never fire for anyone but the author.**

**TWO PERSISTENCES, and the plan must carry both distinctly:** ENGINE persistence (snapshot, save,
load, the log) and **DIEGETIC persistence** — what the world itself holds, in objects that outlive
the witnesses and can be moved, copied, forged, seized and burned. The second is a game mechanic.

---

## R6 · THE DOMAIN ECHO IS A FACT, NOT A MAGNITUDE

> *"the domain echo means that something that happens at one scale — like someone important dying in a
> duel — is recorded as a factual event that changes the state of all other subsystems as required. if
> the governor of a settlement dies in a duel, the game needs to record factually that the settlement
> is now absent a governor."*

**This is NOT the refused Echo** (*a magnitude derived from a Degree… targeted at a scale, applied at
a commit*). Different object; the refusal does not reach it; **no axiom moves.**

**Traced, and already built except one link:** `kill / wound` → seam → degree `Felled` → **`_eff_kill`
writes `(Person, body)`, `(Person, exists)` AND `(Tenure, until)`** (`shape.py:5165`), whose docstring
quotes §15.3: *"a plague that kills the praefect ends his tenure THROUGH THE DEATH; a storm cannot
touch it"* → who holds an office is **derived from live `hold` Tenures**, never stored → **every
subsystem that asks now gets "nobody"**, with no push and no copy to desync.

⚠ **VERIFIED 2026-09-06.** `Office` (`shape.py:2438-2450`) carries `id, post, rung, remit_acts,
scope_rung, binds, conferral, revocation, establishment, dates, upkeep` and **no `holder` field** —
§D.7's refusal of *"two homes for one fact"* holds in the code.

⚠⚠ **AND A CORRECTION TO MY OWN FIRST SHARPENING OF THIS ROW, WHICH WAS WRONG.** I wrote that no
named Query exists and the derivation is duplicated inline, and recommended naming one. **`Query.hold_force(w, obj)`
EXISTS** — `shape.py:3151-3158`, a named static method that additionally enforces S15's cardinality
(*"`hold` is 1 PER OBJECT"*) and RAISES on a second live hold. The inline comprehension I cited at
`:3154` is **the body of that function**, not a duplicate call site. I grepped for the pattern, found
the definition, and concluded the definition was a duplication. **There is no one-rule-lives-once
defect here; the rule lives once and is guarded.** The correct symbol for R6's chain is
`Query.hold_force`, not `holder()`.

⚠ **THE MISSING LINK, AND IT IS THE PLAN'S SPINE: THE FACT PROPAGATES AND NOTHING REACTS TO IT.**
Nothing forms a Question about a vacant office. `question_sources` carries Q1–Q3 plus Q4 `need` and
**none is "a world-fact changed in a way that concerns me."** The probe named *"a vacancy opens the
succession occasion"* is `by="construction"` — asserted, not produced. So the governor dies, the
office empties, and no ambitious person forms a candidate.

> **PROPAGATION WITHOUT REACTION IS A CHRONICLE, NOT A GAME.**

Constraint on the fix: **`choose` receives no World**. A person cannot notice a world-fact directly —
it must reach them through their ledger or their View. So R5 and R6 are the same mechanism.

---

## R7 · NORMATIVE AGGREGATES PROPAGATE AT THE SPEED OF NEWS ⭐ THE DECISIVE RULING

Given the fork — **echo model** (battle lost → legitimacy −2 everywhere, instantly, uniformly) versus
**architecture model** (only those who LEARN of it revise; legitimacy falls where the news has
reached, at the speed news travels, suppressible/deniable/forgeable) — Jordan ruled:

> *"yeah this is better"*

**RULED: no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED.**

The six quantities he named are all Queries, and the three that feel most statistical are Queries
**over interiors**: holdings count and military capacity and influence are Queries over `hold` and
`commit` edges; **legitimacy, the leader's standing and populace morale are Queries over
`stance`/`convictions`.** So the reason a magnitude carrier feels necessary is that **`H-62` is open**
— if no stance moves when the army dies, legitimacy cannot fall out of anything.

**Three consequences:**
1. **`H-62` is unavoidable and first-rank.** Nothing moves until a verb writes an interior.
2. **The news channels are load-bearing**, so `H-84` is one of only two roads by which legitimacy can
   move at all. `H-62` + `H-84` ARE this ruling's mechanism.
3. **⚠ THERE IS NO SINGLE FACTION-LEGITIMACY NUMBER.** It is a field over the population, so **a ruler
   can be wrong about their own standing.** This composes exactly with `§C.11`'s explanation contract
   — the engine owes the player *the arithmetic of what their character already holds* — so the player
   sees their character's ESTIMATE, never the true aggregate. §C.11 becomes structural, not a courtesy.

**It makes trajectory EASIER:** what a player is shown is their character's belief about a trend — a
windowed read over that person's own ledger, bounded and already inside the epistemic contract. The
unbounded world-wide trend Query may not need to exist.

**The yield, which justifies `H-62`+`H-84` to any later reader — none of these is a feature to build:**
propaganda (utter a competing Proposition) · cover-ups (`destroy_record`, or not telling) · the
intercepted dispatch (`H-84`'s *seize*) · the messenger who never arrives (a `move` by a killable
person) · delayed news as distance (`travel_leg`, `travel.moved` exist) · rumour vs record graded by
`Claim.confidence`, which exists and already decays (`claim.decayed`).

---

## WHAT THESE RULINGS CLOSE

`F.32` (R1) · the Echo question, in both its factual (R6) and statistical (R7) forms, **with no axiom
moved** · the instant-vs-news-speed fork (R7). **The escalation count from the superseded plan is
stale: D5 was mooted by the canon dismissal, D6 is closed by R1.** Only `AX-5`'s fourth motion (R4
route 4) and the Godot key-types decision remain candidates, and both need §0's five tests run.
