# 04 · THE SEASON LOOP — six steps, four barriers, four write classes

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L2 — the loop.** The single most load-bearing document in this suite: `05_WORLD_CHURN.md`,
## `06_EMERGENT_NARRATIVE.md` and `07_THE_PLAYER_AND_THE_PERSON.md` are all elaborations of one step.

---

## §1 · THE LOOP, WHOLE, ON ONE PAGE

```
  ┌── CALENDAR ─────────── barrier 1 · fires occasions and DECIDES NOTHING
  │        dates come due · dockets form · option availability recomputed
  │
  ├── MATTER ───────────── barrier 2 · THE WORLD FREEZES AT ITS END
  │        events resolve FIRST · bodies · larders · yield · travel · wear
  │        NO social quantity moves here
  │
  ├── DELIBERATE ───────── a MAP, not a barrier · pure · any order · parallel
  │        choose(person, view, sensation) -> Act        ONE act per person
  │        reads the frozen world through TWO FLOATS and nothing else
  │
  ├── RESOLVE ──────────── barrier 3 · the ONLY writing step for acts
  │        five strata · touch-graph conflict · contests · sum-then-clamp-ONCE
  │
  ├── WITNESS ─────────── barrier 4 · THE JOIN
  │        global fan-out, ONE pass · then per-person deposit into OWN ledger
  │
  └── CENSUS ──────────── shares WITNESS's join
           reads the post-eviction ledger set ONCE · individuation · envelope
```

**Four barriers, six steps, and the counts differ for two reasons that are both structural:**
**DELIBERATE is a map, not a barrier**, and **CENSUS shares WITNESS's join** rather than opening its own.

---

## §2 · HOW IT NESTS IN THE TICK THAT ALREADY RUNS

There were three loops in circulation. Only one of them executes.

| source | shape | state |
|---|---|---|
| `engine/autoload/engine_clock.py` | **three phases: `SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY`** | **RUNS.** Pinned by a phase test and by byte-exact seeded goldens |
| the earlier design line | seven phases, `P0…P7` | retired — see below |
| this shape | **six steps, four barriers, four write classes** | proposed |

> **THE SIX STEPS ARE A REFINEMENT OF THE RUNNING THREE-PHASE TICK, NOT A REPLACEMENT.**
>
> | phase (executes today) | steps (the contract) |
> |---|---|
> | `SEASON_TICK` | **CALENDAR** |
> | `ACTION` | **MATTER · DELIBERATE · RESOLVE** |
> | `ACCOUNTING_BOUNDARY` | **WITNESS · CENSUS** |

**Why a refinement, on merit rather than on deference.** The three-phase spine is not adopted because it
shipped; it is adopted because **it is the right shape and the six steps genuinely nest inside it.** Its
`ACTION` body is **caller-supplied by design** — verified this pass, and the module says why: the
dispatch policy differs between a batch sim, an interactive session and a test injecting deterministic
acts. **That is exactly the seam MATTER/DELIBERATE/RESOLVE need**, and a replacement would have to
re-derive it.

**The seven-phase alternative is retired on its own terms, not by preference:** its `P7` writes were
unlicensed under its own three-write-class rule, its "SEVEN PHASES" header sat over an eight-row table,
and its WITNESS was not global — which makes its parallelism claim unsound rather than merely unproven.

### §2.1 The four nesting obligations — where an implementer will otherwise go wrong

These are not style notes. Each is a defect that would ship silently. [LANE C C1, LANE D A4]

1. **CALENDAR must not advance the season counter.** `engine_clock` is the **only** module permitted to,
   and it already does at `SEASON_TICK`. A six-step CALENDAR that advances a second time double-ticks
   the world.
2. **MATTER, DELIBERATE and RESOLVE live inside the ACTION callback.** They are not three new phases.
   Adding them as phases is the change the module's own docstring flags as non-neutral.
3. **CENSUS maps to `ACCOUNTING_BOUNDARY`, and the boundary's accounting body is currently called RAW,
   outside the emission drain.** That is deliberate and bounded **only because accounting emits nothing
   today.** **The first CENSUS emitter makes it unbounded**, so the drain topology is prerequisite work
   for step 9, not a footnote to it.
4. **The per-tick emission cap spans BOTH phases**, because `next_tick()` runs last. CENSUS emissions
   count against the tick's cap. **And the cap RAISES rather than clamps** — a breach is a loud failure,
   not a silent truncation, which is the correct choice and must not be softened.

### §2.2 The step names are words, permanently

`CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS`. **Uppercase, English, no letter-number
spellings, ever.** A prior brief spelled the steps `B1 … M2` and cited review findings `B1` and `M1`
seventy-six lines away in the same file: **two namespaces, one token shape, one document.**

> ⊕ **AND THE PHASE-TO-STEP MAPPING IS DECLARED ONCE, IN THE CODE THAT OWNS THE PHASES** [LANE C F15].
> Two step vocabularies with no declared join is the same defect at the code seam. The mapping table in
> §2 belongs in `engine_clock`'s own docstring, where a session meets the phase names first.

---

## §3 · THE SIX STEPS, IN FULL

### CALENDAR — barrier 1

| | |
|---|---|
| **reads** | dates; live convening conditions; option-enabling claims |
| **writes** | dates, dockets — **CALENDAR class** |
| **refuses** | to decide any outcome; to read any person's ledger |

**It fires occasions and decides nothing.** A convening predicate may read **only** the holder's own
state, an R-1 compute-on-demand aggregate over its descendants, or the calendar — **never another
person's interior, and never a descendant's stored state.**

> **A VACANT DATE FIRES, ALLOCATES NOTHING, AND LAPSES. Vacancy is a tax, not a wall.**
>
> This one line is worth more than it looks. It is what produces **the famine nobody caused**: the
> tithe reckoning comes due, the office that would allocate the granary is empty, the date fires,
> nothing is allocated, and the shortage that follows traces to **no villain at all**. Cut it — make a
> vacant date block or fall back — and **every shortage in the game has a culprit**, which is the
> failure mode that turns a simulation back into a story someone wrote.

**Option availability is recomputed here**, and that is the whole of the mechanism that keeps a
suppressed grievance reachable later: a dormant row re-enters an option set by **one recomputation and
no decision.**

**Threats and pressures ride the convening condition:**

```
ConveningCondition := (id, holder, predicate, date_form, set_by, set_at)
   holder    in Rung | Office
   predicate : pure over the holder's OWN readable state, an R-1 aggregate, or the calendar.
               PUBLISHED AS A BAND, never as a trigger point.
   date_form : (venue, horizon, convener_office)
   set_by    : the person whose act attached it
```

**A threat is a published band predicate that schedules an occasion.** A famine coming, a seam running
out, a garrison's arrears compounding, a neighbour's density rising at your border. **It guarantees an
occasion, not a hearing** — which is the difference between a clock that fires an outcome and a calendar
that puts a decision in front of a person.

**Attaching one is an exercise of `convene` and costs the setter an act.** A fired date consumes the
convener's allowance and its items compete for that date's `capacity`. A vacant convener may not attach
a new condition **and does not stop existing ones firing.**

### MATTER — barrier 2; the world freezes at its end

| | |
|---|---|
| **reads** | frozen prior state; per-operation substreams |
| **writes** | matter, bodies, travel, the `yield` roll, envelope weights, `condition -= wear` — **MATTER class**; and the existence of **non-social** subjects |
| **refuses** | to destroy anything whose `(record-kind, field)` row is `social: true` |

> **EVENTS RESOLVE FIRST, BEFORE ANYONE CHOOSES. No social quantity moves here and no act's effect
> lands.**

**Why events go first, and it is not arbitrary.** If the harvest resolves after deliberation, everyone
chooses against a world that has not yet happened to them. **Putting MATTER before DELIBERATE is what
makes a bad season something you respond to rather than something you were warned about.**

**Three things this step owns and nothing else does:**

- **`yield`, once per season, here and nowhere else.** `yield(H) = base(H) x condition(site(H)) x
  season_factor`, and the site's identity is why `condition` had to stay per-Site.
- **`wear`, the world's entropy**, subtracted from `condition` in the **same units** — a fraction of full
  condition per season, per site kind. **Not weather, not a multiplier, not a roll.**
- **Death.** A named person's death is the one place a Person leaves existence without an act.

**Death's three rules, each of which is a mechanism rather than a note:**

1. **It sets `until = tick` on every Tenure the deceased held** — the only Tenure write in the MATTER class.
2. **It does NOT open the conferral Date.** The vacancy is a *fact*; the date is an *occasion*; CALENDAR
   is where facts become occasions. The following CALENDAR reads the vacancy and schedules the
   conferral at the horizon its date-holder carries. **Nothing observable changes, and no step writes
   outside its class.**
3. **It does NOT propagate. News travels.** Every standing dispensation the dead holder issued keeps its
   terms and **loses its complier as and when a claim of the death reaches each person.**

> **A WITHHELD DEATH-NOTICE IS THEREFORE ONE OF THE MOST POWERFUL ACTS IN THE GAME**, and no rule says
> so. It falls out of three rules that were each written for another reason.

**Birth is envelope weight, not a `create`.** The envelope advances, births add weight at the youngest
band, deaths remove it. **The envelope is matter and does not act.**

### DELIBERATE — a map, not a barrier

| | |
|---|---|
| **reads** | the frozen world **through `sense` only** (two floats); the person's own ledger via `assemble`; their own remits |
| **writes** | **nothing but the returned Act** |
| **refuses** | the World; another person's interior; any write at all |

**A pure map over persons. Any order. Fully parallel.** `opening_set` is **claim-derived** and can be wrong —
**a person may attempt what is not in fact available**, and discovering that the harbour silted by
attempting to ship from it is the mechanism by which the world's changes reach a person who was not
told.

**One act per person or cohort, universally.** No office, rank or holding changes it. An office's
throughput is its **establishment's** acts, and every establishment member is a person with one act,
their own ledger and the standing option to refuse.

> ⚠ **THREE HAZARDS INSIDE THE FROZEN MAP, EVERY ONE OF WHICH IS A SILENT DEFECT.**
>
> 1. **A lazily-built cache inside the map is a data race.** Freezing prevents writes to *state*; a
>    resolver-side Query that memoizes writes to a **cache** while N threads read it. Law 3's
>    barrier-scoped cache rule exists for exactly this, and *"compute on demand, never store"* reads to
>    most engineers as licensing a cache.
> 2. **A parallel map must not `append`.** Completion order is unspecified, so `acts.append(a)` produces
>    an array whose order varies run to run — and every downstream order inherits it: the stratum sort,
>    the delta accumulation, the conflict-graph build. **Pre-size to the person count and write
>    `acts[i]`.** This single line is the difference between the determinism claim holding and failing.
> 3. **No thread-local RNG, no re-seeding, no wall-clock read anywhere in the map.**

### RESOLVE — barrier 3

| | |
|---|---|
| **reads** | the declared Acts — `changes[]`, `reads[]`, `contests[]` — and the world |
| **writes** | **everything else** — **ACTS class**, including every act-caused `condition` delta |
| **refuses** | a per-actor special case (it has no `Person` parameter); a second resolver; a fallback when no person acts |

**Conflict is decided by the touch graph plus declared per-kind cardinality.** Two acts conflict iff
they share a subject and either **contests** it, **or** both `alter` the same `exclusive` field, **or**
both `create` edges that jointly break a declared cardinality.

**Five strata, resolved in order, and the order is load-bearing:**

| | stratum | why it is here |
|---|---|---|
| 1 | **movement** | presence first, because every stratum below asks who was there |
| 2 | **binding decisions** — rulings at dates, dispensations issued | these change **terms**, and a ruling made at the sitting is by construction the frame for the season |
| 3 | **contested physical acts** — violence, seizure, blockade-running, a march | they happen inside the terms just set |
| 4 | **uncontested material acts** — work, build, carry, arrive | |
| 5 | **social acts** — `tell`, `carry`, `argue`, `admit`, `commit`, `vouch`, `submit` | last, **because they are about what happened. This is what makes a season's gossip be about that season's deeds** |

**Ties break on `H(act_id, world_seed)` — never on rank, office or submission position.** A
rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet.

**One roll, one obstacle.** An attempt at `Obstacle > 2 x Pool` is **refused, and the season is still
spent** — which makes overreach a visible social fact rather than a silent no-op.

**Additive fields are summed ONCE and clamped ONCE**, never clamped as they go. §5 is why that is not
sufficient on its own.

### WITNESS — barrier 4, the join

| | |
|---|---|
| **reads** | this season's Events; presence, channels, Knots |
| **writes** | **one person's own ledger, and only their own** — **INTERIOR class** |
| **refuses** | a collection signature; writing another person's ledger; consensus |

> **FAN-OUT IS GLOBAL AND ONE PASS; DEPOSIT IS PER-PERSON. No signals, no subscription table.**

**Two steps, and the split is what makes it both fast and honest:**

```
WITNESS step 1 — global, one pass:  for each event, compute its observer set from the presence index
                                    built at the MATTER barrier. No signals. No per-person scan.
WITNESS step 2 — per person, any order: witness(person, event) -> Claim[], deposited into that
                                    person's own ledger and no other.
```

**A Knot deposit REUSES the event id**, so corroboration **fails closed** rather than manufacturing a
second sighting. **Five repeaters are not five sources**, and that is what makes a whisper network
something to investigate rather than something to count.

**Eviction ranks on `confidence_live x recency` ONLY, never on salience** — otherwise motivated
retrieval becomes **motivated deletion**, and a person forgets precisely what they would rather not
know. Retrieval ranks differently, on purpose.

> ⚠ **AND THE ONE HONEST GATE ON THIS STEP.** The executing substrate deliberately does **not**
> implement observer resolution, and its own docstring says why: the ordering rule that would make
> `compute_observers` deterministic is **proposed and unratified**, and *implementing it first would
> bake in hash-order nondeterminism* [LANE D A4, verified].
>
> **So WITNESS carries a real precondition, not a caveat: the observer-order rule is ratified — a
> deterministic, order-preserving enumeration — BEFORE the fan-out is built, or the loop's determinism
> claim is false from its first commit.** The rule is short and already drafted; what is missing is a
> ratification, not a design.

### CENSUS — shares WITNESS's join

| | |
|---|---|
| **reads** | the post-eviction ledger set, **once**, against a single snapshot |
| **writes** | individuation and de-individuation; envelope-weight reconciliation — **MATTER class** |
| **refuses** | scheduled population generation |

> **DEMAND-DRIVEN ONLY. Nothing generates without a demand, and no clock generates anything.**

A person is created when something needs them to exist — *the praefect fines a smuggler and the engine
must produce one* — and is then made consistent with the address, marks and history they must already
have had. **A world that manufactures people on a schedule accumulates them without bound**; the
surveyed precedent reached twenty-four thousand characters in late saves and had to throttle the tail.

**Why CENSUS reads once, against one snapshot.** Without a step that reads a single snapshot,
**order independence is unachievable no matter how the map is written** — individuation decisions would
depend on the order ledgers were written in.

**And the de-individuation predicate is one integer, not a scan** (`02` §2.1.2). At `L = 200` claims per
ledger the scan is 200·N² comparisons a season, and the counter costs nothing because WITNESS already
visits every deposit and every eviction.

---

## §4 · THE FOUR WRITE CLASSES, AND THE MATRIX

**`CALENDAR · MATTER · ACTS · INTERIOR`.**

> **RULED: A WRITE CLASS IS NOT A PHASE — and the running code already practises this.** The accounting
> boundary today both drains action-phase deferred applies **and** accepts immediate applies from
> accounting emissions. **One write class, two phases writing it, by ratified design.** So this is not a
> novelty of the proposal; it is how the only running barrier already behaves.

| written thing | CALENDAR | MATTER | DELIBERATE | RESOLVE | WITNESS | CENSUS |
|---|---|---|---|---|---|---|
| `Date`, `DocketItem` | **yes** | no | no | **yes** (`carry`, `convene`) | no | no |
| larders, `stores` | no | **yes** | no | **yes** (`transfer`, `levy`) | no | no |
| bodies, ageing, death | no | **yes** | no | no (killing is an **act**) | no | no |
| travel legs | no | **yes** | no | **yes** (movement) | no | no |
| `yield` | no | **yes, only here** | no | no | no | no |
| envelope weight | no | **yes** | no | no | no | **yes** |
| `condition(site)` | no | **yes — `wear` ONLY** | no | **yes — act deltas, only here** | no | no |
| `Tenure` | no | **yes** (`until` on death) | no | **yes** (`confer`/`revoke`/`create`/`destroy`) | no | no |
| carrier existence | no | **yes** (death) | no | **yes** (`create`/`destroy`) | no | **yes** (individuation) |
| `stance` | no | no | no | **yes** | no | no |
| the claim ledger | no | no | no | no | **yes, own only** | no |
| the returned `Act` | no | no | **yes** | — | no | no |

**Any unmarked cell is a write-class violation**, and the guard that earns its existence is a
**write-sweep over the accumulator's call sites** — the pattern this repository already proved on a
cell-owned field: grep the field's **assignments**, not its readers, and fail on a *new* bare assignment.

> ⊕ **DECLARED INTERIM VIOLATION, named here so nobody "fixes" it without the control.** Until the
> reorder in `13_EXECUTION.md`, the accounting body performs **MATTER-class work at the boundary.** The
> move is golden-changing and needs a two-arm control. **Moving code to satisfy a table, without the
> control, is the exact failure `CLAUDE.md` §0.1 point 4 forbids.**

---

## §5 · ORDER INDEPENDENCE, AND EXACTLY WHAT IT RESTS ON

**The claim.** Within DELIBERATE, persons may be processed in any order or in parallel. Within WITNESS,
deposits may be made in any order.

**What it rests on — five things, and the fifth is the one that was wrong:**

1. **The world is frozen** from the end of MATTER to the start of RESOLVE.
2. **No shared allocator.** Ids come from `H(world_seed, tick, subject_id, purpose)`. **There is no id
   service, no counter, and nothing to serialise on** — which is the same mechanism, not a second one.
3. **The act array is canonicalized before resolution** — sorted by a content-derived key, never by
   completion order.
4. **Sum-then-clamp-once**, so clamping cannot depend on arrival order.
5. ⚠ **AND ON FIXED-POINT ARITHMETIC.**

> ### THE PART THAT WAS WRONG, AND WHY IT MATTERS MORE THAN IT SOUNDS
>
> **Batching delivers CLAMP-order independence. It does not deliver SUMMATION-order independence.**
> [engine] IEEE float addition is **not associative**: three deltas of `+0.3, −0.5, +0.3` applied to a
> field sitting at `0.9` land on different last-bit values under different orders.
>
> **And this architecture makes that difference observable rather than cosmetic.** `verbs(w, site, c) =
> { v : condition(c) >= floor(v) }` is a **band gate on the summed value**, so a one-ulp difference at a
> floor is **a verb that exists in one ordering and not in another** — and a band-edge crossing is an
> **Event that people witness.**
>
> **This repository has already paid for this exact defect class once**: a one-ulp aggregate error
> crossed a damage-degree boundary while its own identity test passed.
>
> **The fix is fixed-point integers** (`10_GODOT_4_6.md` §4): `condition` as an int on `COND_SCALE`,
> `stores` in whole units, coefficients as integer pairs. **Integer addition is associative and
> commutative, so order independence stops being a claim and becomes a fact** — and the structural test
> can then assert **bit-identity** rather than approximate equality, which is the only assertion that
> can *observe* the failure it excludes.
>
> **The honest fallback, if fixed point is ever refused:** a canonical summation order over the five
> strata plus the hash tiebreak makes the result **reproducible**. But then the honest word is
> **canonically ordered**, not *order-independent*, and every document must change the word.

---

## §6 · DETERMINISM ACROSS THE LOOP

| | |
|---|---|
| **the seed** | one `world_seed` per campaign |
| **substreams** | every roll draws from `H(world_seed, tick, subject_id, purpose)` — **never a shared, re-seeded generator** |
| **replay** | identical seed + identical code ⇒ identical event log ⇒ identical content hash |
| **the artifact** | a content hash over the log, already existing and already pinned |

> **THE MEASURED HAZARD IS REAL AND IT IS THE REASON FOR SUBSTREAMS.** Drawing from the campaign RNG in
> a new place **shifts every downstream draw** — which is how *adding two NPCs* was observed to move a
> seeded winner. **A person loader that draws from the shared stream moves every golden in the
> repository for reasons that have nothing to do with the people it added.**

**`purpose` must be unique per DRAW, not per operation**, or two draws inside one act collide. And
**`H` is an owned, versioned mix — never a built-in `hash()`**, whose value is not a cross-version
contract.

**Every change that moves a golden carries a two-arm control:** flag-OFF **byte-identity including the
log hash** as one arm, and an n≥100-campaign balance comparison as the other **where the change is
campaign-reachable**. **A change that is campaign-unreachable makes both arms identical by construction,
and running it there would be a fake control** — saying so is part of the discipline, not an excuse.

---

## §7 · WHAT THE LOOP REFUSES — AND WHETHER THE REFUSAL IS MECHANICAL

**A refusal only a reader enforces is a convention.** Both kinds are listed, and the distinction is the
point. Overstating this column is the failure mode; **today, before anything is built, every row is a
convention, because nothing runs.**

| refusal | enforcement once built |
|---|---|
| `choose` sees no World | **mechanical in Python** (absent parameter + World-first Queries). **Convention + token-scan in GDScript**, permanently |
| `resolve` sees no Person | **mechanical** — absent parameter |
| no decision function reads the event log | **mechanical** — an AST clause in the same probe |
| DELIBERATE writes nothing | **mechanical** — the return shape, plus the order-independence test |
| `witness` never takes a collection | **convention with a named check** — the collection signature is writable in GDScript, and a prior draft's claim that it is *"a type error"* was withdrawn |
| no write outside the matrix | **mechanical if the write class is a parameter of the store API**; convention otherwise. **Make it a parameter** |
| **no fallback: if no person acts, the social thing does not occur** | **mechanical** once the personnel gate lands — and it is a Jordan ruling, not a preference |
| a vacant date lapses rather than blocking | **mechanical in CALENDAR** |
| an attempt at `Ob > 2 x Pool` is refused, season spent | **mechanical in RESOLVE** |
| eviction never ranks on salience | **mechanical in the comparator** |
| a Knot deposit reuses the event id | **mechanical in the deposit constructor** |
| nothing generates without a demand | **convention** — there is no clock to remove, but nothing stops one being added |
| no scheduled social recovery | **structural by phase membership** — there is no step in which a restoring timer could run, so a design that wanted one **has nowhere to put it** |
| CALENDAR decides nothing | convention |
| no petition ends by a fact about the world | convention |
| **no second resolver, no auto-resolve formula, no fast path** | **convention — and this is the highest-value conventional cell in the entire shape** |
| `sense()` returns exactly two floats | convention — the named residual risk |

> **THE LAST ROW BUT ONE IS THE ONE TO WATCH.** Every other refusal here either has a mechanism or has a
> cheap test. *No second resolver* has neither: it is enforced by a person noticing. It is also the
> refusal whose violation is most tempting, most locally reasonable, and most catastrophic — and the
> only honest thing to do is to name it as the weak point rather than to claim a guarantee.

---

## §8 · WHAT THE LOOP DOES NOT CONTAIN, DELIBERATELY

- **No phase in which a container decides.** Every decision has a person's id on it.
- **No phase in which an off-board polity acts without a person.** Off-board pressure enters as an
  **Event** (`05_WORLD_CHURN.md` §4), which is why it needs no phase of its own.
- **No reaction inside a season.** Reaction latency at person scale is **one season**. If the praefect
  opens the granary to one quarter and not another, the other's answer is **next season's act**.
  **You anticipated, or you are late.**
- **No hidden turn order.** Ties break on a hash. Rank never breaks a tie.
- **No step for the three deferred subsystems.** A contest **subdivides** the tick at RESOLVE
  (`09_THE_SEAM.md`) — running the same steps over a smaller person set on a shorter clock. **A battle,
  a hearing, an examination committee and two brothers arguing over a barn are the same call with
  different act vocabularies**, and that is the entire integration story.
