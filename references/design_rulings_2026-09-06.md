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
**`document_key` can never fire for anyone but the author.** ⚠ **REPAIRED 2026-09-07 (`ED-IN-0202`, PR #379)** — `_ch_document_key` now tests the subjects in `changes[]`, so the channel fires on acts. Kept as written because it is the argument that produced the repair; **it is no longer true of the tree.** And the second clause was narrower than it read: `H-84` blocks the RECORD route only. The STORE route is open and executed — a non-author holding the destination rung witnesses `transfer.made` (`test_r8_4_document_key_reaches_a_non_author_through_a_store`).

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

## R8 · PARTIAL OBSERVATION — every term of an observation is independently unknowable

> *"we need for misattribution/epistemics in general to have a way for someone to say 'I don't know
> the description of the person who did x' and 'someone looking like y did x' and so forth"*
>
> *"Or 'I saw this person doing y, but I don't know what y is'"*
>
> *"Eg they saw someone skulking around for no reason they could discern"*
>
> *"but I don't know why they were doing y"*

**Reading — these are one requirement, not four. `T-d` generalises.** `T-d` says attribution must be
a per-witness Claim rather than a field. Jordan's four statements say the same of *every other term*:
identity, act and motive are three separate claims, not three fields of one. A term that is its own
claim can be absent, partial, inferred or wrong; a term that is a slot can only be correct, wrong or
absent. **That distinction is the whole of the requirement.**

**What the deposit does today** (`shape.py:6336`): `Claim(cid, pid, subj, e.kind, True, …)`. The
predicate **is `e.kind`** — the engine's own verb token, handed to every witness verbatim. There is
no actor slot at all (not "unknown" — absent; `01_AXIOMS.md:319-330` already admits this: *"T-d is
currently a naming convention, not a mechanism"*) and no motive slot. So a witness today has perfect
knowledge of *what* and no capacity whatever for *who* or *why*.

### R8.1 · The shape that survives adjudication

**One claim per (witness, event)**, added beside the two existing deposits, not replacing them:

- **`subject`** — the changed thing when there is one, **else the rung the event happened at**
  (`_event_place`, `shape.py:4311`).
- **`predicate`** — `seen`.
- **`value`** — a frozen struct `{stratum, marks, who, why}`, each term `None` where the channel
  withholds it. `Claim.value` is already `Any` (`shape.py:2154`) and the tree already carries opaque
  payloads on `Act.payload`, `Tenure.payload` and `StateChange.spec`.

**Why the rung subject is the load-bearing half.** `questions_for` Q2 (`shape.py:3902`) fires only
when `c.subject == p.id or c.subject in mine`, where `mine = {t.object for t in p.tenures if t.live}`
(`:3883`) — and a person's `contain` Tenure has the person as subject and **a rung as object**
(`:3643`). So a `seen` claim subjected to the rung **raises Q2 for everyone standing in that rung**.
*Someone was skulking around the market and I could not tell why* propagates to the ward. The least
informative observation reaches the most correct listener set, out of machinery that already exists.

The four cases: **(1)** *no description* → `who=None, marks=()`. **(2)** *someone looking like y* →
`marks=(…,), who=None`, identification deferred. **(3)** *doing something I can't name* → `who` set,
`stratum` set, no verb token. **(4)** *skulking for no discernible reason* → `stratum` alone, `why=None`.

### R8.2 · What was tried and overturned — recorded so it is not re-proposed

The first shape minted a **sighting** — a per-(witness, event) id used as a `Claim.subject`, with the
observation split into up to six claims over that term. It is the more expressive shape and it was
**broken by adjudication on four counts, each verified by hand against the tree:**

1. **It severs the one live propagation route.** A sighting id is neither a person id nor a Tenure
   object, so **no member of the bundle can ever raise Q2** — and `occasioned_by`'s own docstring
   names `claim_landed` as *"the one propagation runs on"*. It would return `R3` to the 0-of-30 the
   tree measured before `H-79`.
2. **Its remedy for uneven bundle decay crosses `PART D` row 39** (`04_CODE_ARCHITECTURE.md:972`) —
   *"the comparator's signature takes `confidence` and `recency` and nothing else — STRUCTURAL by
   signature."*
3. **It mints six predicates nothing reads** — the same `ID-13` charge it levelled at `Person.marks`.
4. **Its own advantage has no consumer.** Per-term contestability needs an inference or recognition
   producer, which it deferred by name.

**Sequencing ruling: the sighting term earns its own id at the commit that builds a recognition or
inference producer, and not before.** Until then the struct is strictly better; at that point split
the struct into per-term claims. What the struct gives up, plainly, is per-term contestability — a
second witness's marks cannot contradict the first's `who`, and a later inference must *replace* the
struct rather than layer beneath it (`LedgerReader`'s newest-wins, `shape.py:1307`).

### R8.3 · The gate on all of it — `Claim.value` has exactly two readers

Every `.ledger` access in `shape.py` was enumerated (`:1229, 3125, 3660, 3860, 3901, 4011-4012,
4522-4532, 5461, 6429-6445`). They read `c.subject`, `c.predicate`, `c.source`, `c.confidence` and
`c.when`. **`Claim.value` itself is read in exactly two places in the whole loop:**

1. **`LedgerReader.read`** (`:1309`, `return best.value`) — and its consumers are closed at load:
   `_require_known_stem` (`:1311`) raises `SystemExit` on any predicate stem outside
   `REQUIRES_STEMS`, so a `seen` predicate is **refused at load** until it is declared.
2. **`agreement()`** (`:3989`, `c.value == own_by[c.predicate].value`) — an equality test, scoped to
   `person_predicates`.

Two consequences, and both are sharper than "nothing reads a description":

- **The struct must be declared before it can be deposited.** This is not a lint; it is a load-time
  refusal, and it is the correct one — it forces the roster row (`observation_terms`) that both
  shapes need anyway.
- **`agreement()` compares whole values**, so under the struct two witnesses who agree on `who` and
  differ on `marks` register as **disagreeing**. That is the concrete price of the deferred
  per-term split, stated in one line rather than in the abstract.

So the first thing to build is not the carrier but **the consumer — a person who forms a candidate
because of what they came to believe** — which is the same thing `R6` needs and did not have.
`R6`'s formulation stands: **propagation without reaction is a chronicle, not a game.**

### R8.4 · Four defects verified in passing, each load-bearing on `R5`–`R7`

| defect | site | what |
|---|---|---|
| ✅ **`document_key` cannot fire on any act — FIXED 2026-09-07 (PR #379)** | `shape.py:4356` vs `:5889` | the predicate tests `t.object == e.subject`; every fold-emitted Event sets `subject = a.actor`; no `hold` Tenure takes a person as object. The channel is reachable only for `MATTER`/`CALENDAR` events, which carry no verb and no actor. **`R5`'s bureaucratic mechanism is unreachable on acts** — not underused, unreachable. ⚠ **REPAIRED**: the predicate now reads `changes[]`. Two corrections to this row's own reasoning, both found by the adversarial pass on the fix: (1) *no `hold` takes a person as object* is right and load-bearing, but `hold` over a RUNG is common, so the reach is wider than *a Record or an Office*; (2) the channel now reaches a NON-AUTHOR on an act with no verb added — `_eff_transfer` subjects its `StateChange`s to the rungs, so a person holding the destination witnesses `transfer.made`. `H-84` blocks the RECORD route only. |
| **`Person.marks` is dead AND its matrix row is retired** | `shape.py:2367`; `write_matrix.yaml:358-370` | zero writers, zero readers anywhere in `engine/season/`. `matrix_row()` raises `Unspecified` on a retired row, so a gate write refuses today. Constructor assignment bypasses the gate, but `_entity_digest` is `repr(dataclass)` (`:2602`), so writing marks at world-build **moves every same-seed hash** — a re-baseline, not a red test. |
| **`Candidate.why` is written once and read nowhere** | `shape.py:2284`, written `:3289` | `why=q.source`; dropped at `pack_scenes`; `Act` carries no `why`. **The engine forgets the motive before the act executes**, which is why no witness could ever learn it. |
| **Q2's subject membership gates every future claim shape** | `shape.py:3902`, `:3883`, `:3643` | any new deposit whose subject is not a person id or a live Tenure object is inert on arrival. Design against this line first, not last. |

### R8.5 · Corrections

⚠ **The channel asymmetry runs the OPPOSITE way from the shape first proposed in session, and the
architecture already said so.** `08_DATA_AND_KEYS.md:104-105` — which carries a `RATIFIED`
status line on PR #371's branch, on a PR that has not merged — says verbatim: *"a co-located witness saw who acted; a document holder saw only that the document
changed."* A first draft of `R8` had eyewitnesses withholding identity and documents supplying it,
and sold that inversion as the result justifying the work. **It is wrong in both directions.** The
asymmetry is real, it is already ratified, and it points the other way: the eyewitness knows who and
not what; the record knows what and not who.

⚠ **`stratum` is injective on `movement` and therefore leaks the verb it is supposed to withhold.**
`verb_table.yaml` carries exactly one `stratum: "movement"` row — `move` (`:344`). A `stratum` term
is only genuinely uninterpreted where the stratum has several verbs (`social` has ten,
`binding_decision` eight).

⚠ **The `678 → 68` deposit figure quoted in session is a stale literal.** `PLAN.md:1838-1840` records
the current measurement as **`711 → 66`** and says so itself; the factor holds, the numbers moved.
`ledger_cap` remains 200 (`shape.py:1772`). The affordability constraint is unchanged: a per-witness
addition is affordable only under a narrow fan, which is why `+1` per witness-event and not `+6`.
---

## WHAT THESE RULINGS CLOSE

`F.32` (R1) · the Echo question, in both its factual (R6) and statistical (R7) forms, **with no axiom
moved** · the instant-vs-news-speed fork (R7). **The escalation count from the superseded plan is
stale: D5 was mooted by the canon dismissal, D6 is closed by R1.** Only `AX-5`'s fourth motion (R4
route 4) and the Godot key-types decision remain candidates, and both need §0's five tests run.

**R8 adds no escalation.** Its adjudication ran §0's five tests and returned none: the shape question
was answered by precedent and by architecture (test 4 and test 5), the eviction question was already
answered by `PART D` row 39 (test 3), and the sequencing question answers itself under `ID-13`. What
R8 leaves open is **work, not a ruling** — and it is one item, shared with `R6`: *build the consumer
that makes a person form a candidate from what they came to believe.* Until that exists, every
epistemic carrier this file names is a carrier without a reader.
