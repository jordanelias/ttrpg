# THE UNIFIED SHAPE — reconciled from a:NPC and b:ARCS, adversarially audited

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## Every claim below is either an execution or a citation. Where it is neither, it says so.

> **What this is.** PR #350 proposed an idealized code shape. Two tests were then run against it by
> execution — a season for 27 named NPCs from a copyist to a King, and a playthrough of 50 arcs —
> and two structurally-independent read-only audits attacked the results. **This document is what
> survives.** It is not PR #350 amended. It is written as if from scratch, and where it keeps
> something it says why that thing earned its place.
>
> **The one commitment not up for revision:** *characters are the primary drivers of world churn.*
> Everything below is downstream of it, and §2's fifth law is the first time this suite states the
> mechanism that makes it true rather than asserting it.

---

## §1 · THE MEASUREMENT THIS RESTS ON

| | a:NPC | b:ARCS |
|---|---|---|
| cases | 27 named NPCs | 50 arcs |
| result | **22 BLOCKED · 4 NOT-ASSESSED · 1 DEGRADED · 0 PLAYABLE** | **39 BLOCKED · 10 NOT-ASSESSED · 1 PLAYABLE** |
| top blockers | `P36` budget (5) · `A4` provenance (4) · `P29` custody (3) · `F6` sittings (3) | `A2` endings (10) · `A13` drift (8) · `P34` hidden tally (7) · `P4` convictions (7) |

**527 need-rows, 65 probes, 79 acts and 334 class-checked writes.** Case verdicts are advisory;
probe verdicts are hard. **226 needs did not route and are reported as `UNMAPPED` rather than
passed**, and 14 cases are `NOT-ASSESSED` rather than graded.

**Four instrument defects were found and fixed during the run, every one of which flattered the
shape**, and the fourth was found by an audit that had never seen my reasoning. They are catalogued
in `01_TEST_A_NPC.md` §5. The rule they cost me: **when a route is wrong, read what it was catching
before you cut it** — the mis-catch is usually a capability the probe set does not have. `P34` and
`P36`, two of the four most consequential findings in this document, arrived that way.

---

## §2 · THE LAWS

Four are PR #350's, two of them amended. **The fifth is new, and it is the load-bearing one.**

### L1 · The person is the only actor. *(unchanged — and it passed)*

No institution acts. No faction acts. No threshold acts. An institution acts by a named person at a
venue, and *"the Church excommunicates"* is not spellable while *"the Confessor, at a venue, issues"*
is. **Verified by execution** — `P1` (a postless person acts), `P9`/`P20` (an order is the
subordinate's own choice, refusable), `A7` (an institution acts as one body), and above all `P12`:
a stranger takes the seat Maret Uln needed and her ambition progress moves `1.0 → 0.0` with **no
`obstruct` verb, no knowledge of Maret in the stranger's decision, and no branch in the resolver.**

> **`P12` is the best property in the shape and both tests confirm it.** Keep the law that produces it.

### L2 · Nobody is omniscient, and the signature is what enforces it. *(unchanged)*

`choose` never receives a `World`. Not by discipline — by type. A person decides from a `View` built
of their own claims, which may be wrong, and `P5` verifies that a false conclusion is
indistinguishable from a true one to the person holding it.

### L3 · Every aggregate is a function, never a field. *(AMENDED — the bound is a closed roster)*

The original is right and both tests confirm it: a stored `unrest` is a lie that outlives its
reasons. But **fourteen cases across both suites need a quantity that only climbs**, and the shape
had none.

The amendment as first drafted said *"a monotone tally is permitted if it counts only events in the
holder's own ledger."* **An adversarial audit broke it in one move**, and the break is worth stating
because it is the failure mode of every bound of this kind:

> Define a per-cohort monotone counter *harms witnessed*. Every increment is an event in the
> holder's own ledger, so the bound is satisfied. Now `Query`-sum it over the cohort's members. That
> is stored, monotone, **never-decaying** unrest in all but name — **worse than the field L3 banned,
> because the banned field could at least go down.**

**The bound that holds is a closed roster, not a provenance rule.**

> **L3, amended:** a monotone counter may exist **only per `(Person, axis)` where `axis` is drawn
> from a roster closed by canon** — the Conviction roster, which `02` §5.5 already declares *"canon — a closed roster"*.
> It counts only events in that person's own ledger, and it is never a Query's substitute.

*Unrest* is not a canon axis, so the reconstruction fails by construction rather than by discipline.
This is what makes it a bound: **you cannot spell the violation.**

### L4 · Every state change is partitioned by subject, asymmetrically. *(unchanged — and the pressure on it was mis-read)*

`social: true` on a `(record-kind, field)` means **only an act may write it**; `social: false` means
either an act or the world may. The world may silt a harbour; it may not sour a town's mood.

Both tests appeared to press hard on this, and `A13` is the second-largest arc blocker at 8. **The
pressure is real and smaller than it looked**, for two reasons §8 develops: most of what looked like
demand for ambient social drift is demand for *ambient social forcing*, which L5 supplies; and the
suite already ships a licensed decider-free social-adjacent motion nobody had noticed.

### L5 · THE EDGE LAW — **new, and it is what lets stories end**

> **Any monotone quantity may, on crossing a declared edge, change WHAT MAY BE CHOSEN AND BY WHOM —
> including to nothing. The crossing emits and is witnessable. It may never write a social row, and
> it may never produce an outcome.**
>
> **And every clock that moves such a quantity was set by a nameable act — so it can be bribed,
> delayed, burned, or killed.**

**The first paragraph is a promotion, not an invention.** `05` row 8 already says a band-edge
crossing is *"an emission, not a write"*, and `01` already says *"a band edge changes an option set,
never a roll term and never an outcome."* That sentence sits in the suite as a CALENDAR detail. **It
is in fact the single primitive that answers every ending, crisis, ripening and exit in both
corpora** — band edges, a Record's stages gating acts, a conviction reaching crisis, a practitioner
crossing zero and ceasing to be an agent, and the arc endings themselves. Stating it once as a law
is what turns seven special cases into one.

**The second paragraph is the anti-scripting rule stated positively, and it is the reason this
document exists.** It is what makes *"characters drive the churn"* mechanical rather than
aspirational. A quantity that advances on its own with no author is a **shadow actor**: unbuyable,
undelayable, unkillable — exactly the kind of actor L1 forbids, arriving through a side door. A
quantity whose clock was wound by a named person's act has handles. **Every handle a player has on
an institution is a handle on the person who set its clock.**

The suite already owns this and files it as a footnote — `05` row 11b: an act-created Record's term
maturing is *"the creating act's own declared term ripening … calling it an event hides who set the
clock."* **L5 makes row 11b the general rule.**

---

## §3 · THE EDGE LAW WORKED, THREE TIMES

A law is worth what it does to cases. All three are executed cases from the corpus.

### 3.1 · An arc that ends at a counter, with nobody deciding — `ARC-09`

*"The practitioner's tracked personal resource reaches its irreversible zero-point — an automatic,
unrecoverable transition that nobody decides and that has no exit mechanic."* The purest
threshold-ending in the corpus, and `A2` reports it **FORBIDDEN**.

Under L3-amended plus L5 it runs, and **nothing was relaxed**:

1. Every operation she performs spends the resource. **Her own act writes her own interior state** —
   a monotone tally on a closed axis, legal under L3-amended.
2. She rations at a floor she chooses. Her `choose` returns weaker acts. `P25` already passes this
   exact behaviour: *her divided stance is her interior and nobody may read it.*
3. Concealment is free, because interior state is unreadable and investigation is the only route —
   which is `ARC-09`'s own stated need, so the epistemic refusal **is the arc's mechanism, not its
   enemy**.
4. **The crossing.** `may_choose(person)` is a Query over the tally. Her last spending act — *hers* —
   carries the total over the edge. DELIBERATE stops handing her the map; the option set collapses
   to empty; **the crossing emits, so it is discoverable by investigation.**

**No Event wrote a social row. No counter fired an outcome.** *"The transition nobody decides"* is
the accumulated residue of decisions she made. **That is L1 arriving at its own conclusion, not an
exception to it.**

> **The general rule this yields, and it is the crispest thing either test produced:**
> **a threshold ending is recoverable exactly when the crossing quantity lives in the ender's own
> ledger.** It is lost exactly when the quantity is ambient-social — and that residue is §8.

### 3.2 · A case that ripens against you while you do nothing — `A16`, and my own error

The Inquisitors' case against Maret Uln advances *"on its own procedural timetable regardless of
whether anyone acts."* My first change-list said: give `Record` a `stage` that **MATTER advances**.

**An adversarial audit killed that clause and it was right.** `05` §5: *"EXACTLY THREE QUANTITIES
ARE CLOCK-DRIVEN: matter, bodies, and the confidence of a memory. No fourth may be added."* A
Record's stage is a fourth. Worse, the fiction of a case advancing **is not weather** — it is clerks
filing, witnesses deposed, a tribunal scheduled. It is the definition of human society, and `05`
§4.4 already blocks exactly this shape for off-board polities as *"an actor's decision rendered as
weather."*

> **I had resolved C9's escalated question locally, silently, and on the side the laws refuse —
> through a Record-shaped door, under a label that said "adds no type".**

The lawful version costs less and produces a better game. **The Inquisitor's `open_case` act
declares the stages and their terms.** MATTER matures terms; each maturation is *a person's past act
ripening*, with `causes[]` pointing at the act that wound the clock. Every capability survives:

- the case still ripens while Vaynard does nothing — **because the Inquisitor is not doing nothing**;
- the army still cannot stand down — the failed check's resolution deposited the condition with its
  own clearing terms;
- Carin's half-made copy still spans seasons — **and now correctly *stops* if Carin is jailed**,
  which the MATTER-driven version gets wrong: a copy that finishes itself.

And the arcs get materially better by the suite's own argument. `06` §6.1 observes that arcs ending
at a **sitting** survive *because a sitting has a named convener who can be bought, delayed or
killed.* An act-declared term gives every accusation the same handles: **bribe the clerk who set the
term, burn the Record that carries it, kill the man who must renew it.**

### 3.3 · A crossing that forces a decision — the finding that dissolves most of the bill

50 arcs, each classified from its own lane's `ends_when` string by a pass that saw nothing else:

| how the arc closes | n |
|---|---|
| a person chooses | **20** |
| a roll resolves it | 9 |
| never, by design | 10 |
| **a threshold fires with nobody deciding** | **8** |
| unclear | 3 |

**8 of 50, not the 8 of 20 the smaller sample reported** — a correction in the shape's favour. But
the same pass found **19 of 50 arcs are `forced_by_threshold: yes`**: a crossing forces the moment,
and *then* a person chooses. *"The patron is **forced** to choose publicly among
defend/abandon/extract."* *"The head of state's **forced** choice is made — act, abdicate, or be
replaced."* *"Whose ceiling **issues a formal ultimatum**."*

> **The corpus does not want the counter to ACT. It wants the counter to COMPEL SOMEONE TO ACT.**

L5 supplies exactly this and nothing more: a crossing **changes what may be chosen and by whom**. A
king whose army's judgement crosses an edge finds his option set rewritten — *act, abdicate, or be
replaced* — with the old options gone. **No social row is written. No outcome is produced. He still
chooses**, and under §4's abstention rule his refusal to choose is itself an act that others witness
and charge him for.

**This is the summons, and it is not a new object.** It is L5 applied to an edge whose quantity lives
in someone's ledger.

---

## §4 · WHAT THE SHAPE IS

### 4.1 · Carriers — five identity-bearing kinds, one of them promoted

**`Person` · `Rung` · `Office` · `Site` · `Record`** are mutable and identity-bearing.
**`Proposition`** is identity-bearing and immutable. **`Tenure`** is the one edge, with seven kinds
(`hold, contain, commit, oblige, succeed, tie, knot`).

**`Record` is promoted from inert noun to live carrier — the single highest-leverage change in this
document.** It unblocks seven probes across both tests, and an independent clustering of the 95
unrouted `core` needs found **19 of them are the `Record`**, by far the largest cluster. It gets:

| | what | licensed by |
|---|---|---|
| **created by an act** | a `create`-mode StateChange whose subject is a Record | `04` §4's matrix already carries *carrier existence · RESOLVE · yes (create/destroy)* |
| **held by a person** | a `hold` Tenure whose object is a Record | extends `hold`'s domain; **overturns `03` §1.3's "a Record is Rung matter"**, which is why `P29` reports COLLISION |
| **a `ttl`** | decremented at MATTER, emitting expiry | `05` row 11a, verbatim |
| **act-declared terms** | stages whose maturation is *the creating act's own term ripening* | `05` row 11b, **not** a MATTER-advanced stage (§3.2) |
| **it gates, and it taxes** | a held Record may make others' acts *unavailable* **or more costly**, and may be the sole route to a function | six independent cases; this is `01` §3.1's *custody* finally carrying weight |

**Honest price, because the first draft under-counted it:** two new fields, a `(Record, …)` Partition
row (the suite currently has **none**, so every Record write is an unmarked cell), an opened kind
roster (`{register, charter, deed, roll, letter}` does not contain `copy`, `truce` or `accusation`),
and one overturned ruling. Each defensible; *"adds no type"* was not the whole bill.

### 4.2 · The act economy — **~5 acts per season, and triage is the game**

`choose(Person, View, Sensation) -> Act` returns **one** act, and the loop calls it **once per person
per season** — asserted by execution, not by reading. Against the stated player model of **~5
playable scenes and so ~5 actions**, the shape is out by a factor of five, and **the factor is not
the finding.**

> **The finding is that with one act nobody ever chooses what to LEAVE UNDONE.** A King facing four
> simultaneous pressures who can substantively address two of them, with the other two compounding,
> is doing the thing that high office *is*. At one act per season a King's scarcity is identical to a
> copyist's.

`P36` is the largest blocker on the NPC side (5 cases). The change:

```
choose : (Person, View, Sensation) -> Act[]        # ordered, bounded by budget(person)
budget : (Person, View)            -> int          # a Query — office, condition, distance travelled
```

The budget is a **Query, never a field** (L3), so a wounded duke gets fewer acts than a healthy one
without anybody storing a number. The list is **ordered**, so what he did first is legible when a
season's later acts are foreclosed by its earlier ones.

> ⚠ **A budget above one voids a fix the suite is currently relying on.** `14` records the
> petition-spray defect as *"closed — PROVISIONALLY by one act per person."* At ~5 that is void, and
> **petition spray is open again.** It should be re-answered by cost — a petition consumes budget and
> a refused petition costs standing with the venue — not by a cap.

### 4.3 · Contention — the one primitive nothing else on the list names

`resolve(Act[], World) -> Event[]` applies acts **independently**. So two people cannot contend for
one scarce thing in one season: a blocker cannot hold a line, helping one claimant cannot starve
another, and a shortfall cannot produce a *pending* state. Raised independently by `P35` and by two
unrelated case families in the unrouted set.

> **Scarcity is what makes politics, and the shape has none at the moment of resolution.**

The obvious fix — group acts by target inside `resolve` — is a second resolver, and the shape's own
meta-rule forbids that. **The minimal fix is not a new function; it is a fold.**

```
resolve : (Act[], World) -> Event[]     # unchanged signature
                                        # ordered fold: each act sees the world its predecessors left
order   : (Act[], World) -> Act[]       # a Query. Declared, inspectable, no new state
```

Sequence, not simultaneity. Scarcity then falls out for free — the second claimant on an emptied
granary gets a *different Event* because the granary is already empty — and **no act needs to know
that another act existed**, which is `P12`'s property preserved at the level of resources.

### 4.4 · Absence, attribution, and provenance — three separate facts

**One epistemic commitment**, and it folds four separate findings:

1. **`causes[]` is required and non-empty.** `resolve()` currently emits Events with `causes=[]`.
   It is a:NPC's joint-top blocker, and the suite rests its narrative layer, audit trail and arc
   model on this edge — *"the arc itself."* **The substrate of the entire emergent-narrative claim
   is declared and never populated.** The suite already imposes exactly this constraint on
   Candidates, so extending it to Events is composition, not invention.
2. **Attribution is a per-witness Claim, not a field on the Event.** The Event carries *what
   happened*; *who did it* is something each witness concludes, may be wrong about, and may not
   conclude at all. Covert action and false attribution both become expressible; five arcs need it.
3. **Absence is an occurrence.** DELIBERATE synthesizes `Act(verb="abstain", payload=<the declined
   candidate>)` for an unused act slot — **not** an Event emitted by `choose` returning nothing,
   which is unlawful because DELIBERATE admits no writes at all.
4. **And it is gated.** Emit only where a **live candidate above the salience floor was declined**.
   An empty opening set is absence and emits nothing. **Without this gate every idle person emits
   every season and the very distinction abstention exists to draw is erased at volume** — a
   fisher's empty season and a King's held doubt would read identically.

### 4.5 · Standing, agency, wear

- **`standing(person, audience)`**, not one global scalar. A covert reputation becomes expressible;
  the global reading is the audience `everyone`. This **deletes** a scalar rather than adding one,
  and it resolves an internal contradiction — `07` already computes standing *"among his
  siblings-in-establishment"*.
- **`may_choose(person)`** consulted at DELIBERATE — a Query over a closed-axis tally (L3), so it is
  an instance of the ratchet rather than a new mechanism. One-way crossings only.
- **MATTER touches persons**, not only places: subsistence drawn from `stores`, condition taken from
  the Sites you stand beside. Bodies are one of L5's three licensed clocks, so this is sanctioned
  world-driving, not a new exception. The suite already promises it and nothing does it.
- **A dead person's holds read as vacant.** `A12` finds a dead king still holds the crown, because
  `(Tenure, hold)` is `social: true` and an Event may not write it. **No Partition change is needed:
  make `holds` derived-valid** — a Tenure whose holder no longer exists reads as vacant, by L3,
  because *holds* is a Query gated on existence. **Existence is matter; possession is social; a
  social fact predicated on an existence fact should never be stored truth.** Succession is then
  people acting on a vacancy, which is L1.

---

## §5 · WHAT THIS SHAPE REFUSES

A proposal is judged by what it declines. Each of these was demanded by cases and is refused.

| refused | why | what pays |
|---|---|---|
| **a stored aggregate** | L3. Every ratchet is one person's own history on a canon axis, never a sum over others | nothing — the Query is the aggregate |
| **a threshold that fires an OUTCOME** | L1/L5. A crossing may rewrite an option set; it may not decide | 8 of 50 arcs, honestly (§8) |
| **a MATTER-advanced Record stage** | a fourth clock-driven quantity, and an institution's diligence rendered as weather | nothing — act-declared terms do the work better (§3.2) |
| **a second resolver, a faction verb, a per-entity branch** | scripting drift. Nothing in 78 cases needed one | nothing |
| **a "hidden modifier system"** | nine cases each want *this one NPC* to carry a private bias. That is the ratchet plus a visibility rule, nine times in different dress. A registry for it **is scripting drift with a registry** | nothing |
| **branching-outcome machinery** | eleven needs want three-plus named results from one resolution. That is an authoring convention over `Record`, not a primitive | nothing |
| **scene-device machinery** | eight needs — forced dilemmas, letter-versus-spirit compliance, cross-thread interruption — are dramaturgy. It is what a designer does with primitives | nothing |
| **a new guard, validator or checker** | the only apparatus this work licenses is the tracer, which is load-bearing on the game rather than on this repository's process | nothing |

---

## §6 · WHAT IS STILL OPEN

### 6.1 · The ambient-social question — **narrowed to something much smaller, and still Jordan's**

`A13` blocks 8 arcs: a social quantity drifting toward a pole **from the absence of anyone acting**.
It was escalated as a trilemma. **Three of those framings were wrong and the fourth option is nearly
free.**

- **It is not an *ending* problem.** §3.3 shows 19 of 50 arcs want *forcing*, which L5 supplies.
  Under **every** option — including amending L4 — the threshold-*endings* do not come back, because
  §5 refuses them separately. So the question buys pressure, not endings.
- **`ARC-02` does not belong on the table.** Klapp's spontaneous capability returns **UNSPECIFIED,
  not FORBIDDEN** — the suite has **no Partition row for `(Person, capability)` at all**, so one
  cannot even ask. **Rule it `social: false`** — a trained sense is a body-fact, and bodies are a
  licensed clock — and the arc dissolves without touching L4. *An unmarked cell is not a law conflict.*
- **The cheapest lawful option was never on the list.** The suite **already ships** a decider-free
  social-adjacent drift: **claim-confidence decay and eviction at the ledger cap** — rows 9 and 14,
  INTERIOR, no decider, and memory is one of the three licensed clocks. `05` says it outright:
  *"He loses the town **by being forgotten**."* **A culture dying of neglect IS cohort ledgers
  forgetting it.** Zero new objects, no amendment to any law. The `A13` probe never attempted this
  route — it only tried writing `stance` at MATTER — so its FORBIDDEN is real and **not exhaustive
  of the lawful expressions.**

> **The question that actually reaches Jordan is now one sentence:**
> **may a social quantity sink by neglect alone — as memory already does — and is a person acting on
> witnessed loss enough to turn that sinking into a crisis?**
>
> If yes, `A13` costs nothing and no law moves. If no, 8 arcs lose their engine and the design says
> so out loud. **This is a genuine design call between materially different games**, and it is the
> only one in this document.

### 6.2 · Specification debts — named because the change list dropped them silently

- **`judging_set_rule`** is a named `Rung` field that **no document specifies**, so nothing is
  decided at a sitting. Blocks 3 NPC cases and caps two probes at PARTIAL.
- **Witness channels** — WITNESS as specified fans every Event to every person, so nothing said in
  private is private. This is what makes §4.4's gate load-bearing rather than fastidious.
- **A termination argument per self-feeding loop.** Four arcs plus the King are spirals; nothing
  bounds one.
- **The arc corpus numbers two series identically.** Root `arcs_16_19.md` and `gm_ref/arcs_10_18.md`
  both use 16, 17 and 18 for different stories, with no reconciliation note. Any tool indexing arcs
  by bare number silently merges or discards one of each pair — including any re-run of the
  ending measurement in §3.3. Needs a ruling on which series is canonical, not a shape change.

---

## §7 · THE FALSIFIERS

Per `CLAUDE.md` §0.1 point 3, a result claim carries the test that would show it wrong.

| claim | falsifier |
|---|---|
| L5's act-declared terms replace a MATTER-advanced stage with no loss | produce one `A16`/`A18`/`P30` case whose timetable has **no plausible clock-setting person or antecedent act**. The strongest candidate is a battle-born condition, and even there the resolving contest is the antecedent act |
| L3's roster bound cannot be spelled around | attempt the cohort *harms-witnessed* reconstruction against `(Person, Conviction-axis)`, roster closed by canon. It fails because *unrest* is not a canon axis. If it succeeds, this bound is also wrong |
| the ~5-act budget is a real gap and not a reading | `test_tracer_is_honest.py` asserts by execution that the loop calls `choose` exactly once per person per season. If that ever returns more, `P36` is obsolete |
| `causes[]` is empty in the specified loop | `A4`, executed. It walks the chain backwards and finds nothing |
| abstention must be gated | run `A15` against a build with ungated abstention: a fisher's empty season and a King's held doubt produce identical Events |
| the endings distribution | re-run the classification over the 50-arc corpus **after** namespacing the collided arc numbers (§6.2). Both counts change if the collision is resolved the other way |

**And the standing weakness, stated rather than hidden:** 226 of 527 needs did not route. A separate
pass read the 95 graded `core` and found roughly a third restate changes already on this page, about
nine need no engine capability, and one genuine primitive was missing — which is §4.3. **That is the
honest coverage claim.** At 78 cases keyword routing is at its ceiling; a larger corpus needs the
lanes to emit a capability tag rather than prose a runner greps.
