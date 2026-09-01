# 00 · THE SEASON LOOP IS ALREADY HOLONIC — it does not say so, and three things are missing

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.

---

## §0 · SCOPE, STATED FIRST BECAUSE IT DECIDES WHAT COUNTS AS EVIDENCE

**The only sources are the design chain PR #337 → #352.** No file under `engine/`, no subsystem
`sim/`, and **no decision ratified before #337** is authority here — not as support, not as
precedent, not as an incumbent to defer to. We are building the season loop's logic **from scratch**
off that chain, and #351's `04_UNIFIED_SHAPE.md` is the head.

> ⚠ **THIS CUTS AN ARGUMENT THE CHAIN ITSELF MAKES, AND THE CUT IS DELIBERATE.** The head's parent
> suite rules (`15_ADJUDICATIONS.md` **R-2**) *"compose `Event` onto the executing log — never build a
> second log,"* and its **ground** is that the log *"runs default-on in every seeded campaign."*
> **Under this scope that ground is void**: an existing implementation is not a reason. R-2's
> *conclusion* survives on its own merits — **one log, not two, is right because two logs cannot share
> a `causes[]` chain** — but it is re-derived below rather than inherited, and where R-2 leans on
> execution it is not followed.
>
> The same cut applies wherever an in-chain document rests a claim on pre-#337 material: **the claim
> travels as that document's own proposal, at its own strength, and not as a ratification.**

---

## §1 · THE ANSWER, UP FRONT

**The proposition — self-sustaining containers running slices of the season loop, managed by wrappers
and a comprehensive key system — is, in its load-bearing part, WHAT THE HEAD ALREADY SPECIFIES. The
head just never uses the word, and never names the object.**

`01_THROUGHLINE.md` §2's **LAW 3** carries two module rules, and they are the container contract:

> **R-1.** *"A rung may read its own state and any message addressed to it. It may **not** read a
> sibling's state or a descendant's state directly. It **may COMPUTE an aggregate over its descendants
> ON DEMAND**; it may **not receive a pushed aggregate**, and it may **not store one.**"*
>
> **R-2.** *"A rung writes only its own state. **Upward influence is emitting an aggregate; downward
> influence is emitting a refraction. No module reaches through another.**"*

And §1's throughline table already names both directions as structure:

| | throughline | where the head makes it structural |
|---|---|---|
| **T5** | *"demands aggregate **UPWARD** and are filtered at a rung"* | Petition → `carry` → DocketItem → sitting, *"filtered by a **named person** who pays for the filtering"* |
| **T6** | *"large actions ripple **DOWNWARD**"* | a Dispensation *"is published as a `tell`, distorts in transit, and reaches a postless person through **their own** `opening_set`"* |

> ### **R-1 + R-2 + T5 + T6 IS A HOLONIC CONTAINER ARCHITECTURE, COMPLETE, IN THE HEAD, UNDER ANOTHER
> NAME.** One uniform container (`Rung`, one type, eight kinds, `02_ONTOLOGY.md` §2.2.1); each at once
> a whole and a part (`contain` is an edge, not node-parenting); influence aggregating up and
> refracting down; **and no reach-through.**

**So the question is not whether to adopt it. Three things are missing, and they are the work:**

| # | missing | where it goes |
|---|---|---|
| **M1** | **The word, and the object.** R-1/R-2 are stated as *module rules* in a laws document and then never appear again — no later document names the thing that enforces them. **A rule with no owner is a convention**, and the head's own `04_THE_SEASON_LOOP.md` §7 is scrupulous about which of its refusals are conventions | `02_THE_WRAPPER_LAYER.md` — the wrapper is that owner |
| **M2** | **A descent.** T5's *"filtered at a rung"* and T6's *"distorts in transit"* both require knowing, per module, what it may receive and emit. The head has no surface that answers that | `01_THE_CONTRACT_HIERARCHY.md` |
| **M3** | **The loop's steps mapped onto the ladder.** `04_THE_SEASON_LOOP.md` specifies six steps over *the world*; R-1/R-2 specify reads and writes over *a rung*. **Nothing joins them**, so it is currently undefined which steps run per-rung and which run globally | §3 and §4 of this document |

**M3 is the one that decides whether the proposition's "containers run slices of the loop" is right or
wrong, and the answer is: two of the six steps, and only two.** §4.

---

## §2 · THREE THINGS ARE CALLED "HOLONIC" AND THEY HAVE DIFFERENT ANSWERS

| | the claim | verdict |
|---|---|---|
| **H1 · holonic STRUCTURE** | one uniform container type at every scale; the ladder is data, not a type tree | **ALREADY TRUE and it is the head's best structural property.** §2.1 |
| **H2 · holonic CONTRACTS** | every module declares its I/O against one descent a reader can walk | **THE WORK, and the whole of the context-management win.** M2 |
| **H3 · holonic EXECUTION** | each container runs its own slice of the season loop, self-sustaining | **TWO STEPS YES, FOUR STEPS NO — and no container gets a clock.** §4 |

### §2.1 H1 is already true, and two documents say it without citing each other

`02_ONTOLOGY.md` §2.2.1 gives `Rung.kind ∈ { person, hearth, community, settlement, territory,
province, duchy, realm }` — **eight kinds, one type** — and `10_GODOT_4_6.md` §5.2 rules the
consequence for the port:

> *"the ladder is a directory tree and a `Rung.kind` enum. **It is not a type hierarchy**… **one rung
> type, instantiated at every rung, means a mechanism written for elites is automatically available to
> populations.**"*

**That is the holonic property stated as a payoff rather than as a principle, which is the better way
to state it.** And it is what makes M1 cheap: because there is one container type, the wrapper that
owns R-1/R-2 is **one implementation, not eight.**

⚠ **The `person` rung is the case that tests it and the head pre-empts the objection:** *"the `Rung`
of kind `person` is the **address slot**, and the `Person` is who stands in it."* **Generalise that
sentence to all eight and it becomes §3's C2.**

### §2.2 H2 is where the context argument actually lives

> **THE CONTEXT WIN COMES FROM THE CONTRACT DESCENT, NOT FROM THE RUNTIME TOPOLOGY.**
>
> A session that can descend to one module and read what it may receive, what it may emit, and what it
> owns has bounded its context **without reading the world, the loop, or a sibling.** That is the win,
> and **it needs no change to the season loop at all.**
>
> A runtime split into self-scheduling containers buys **parallelism**, which is not a context
> property — and §4 shows it costs the loop's only termination story.

---

## §3 · WHERE THE PROPOSITION AND THE HEAD COLLIDE — FOUR PLACES

### C1 · "Self-sustaining container" versus **four global barriers**

`04_THE_SEASON_LOOP.md` §5 states what order-independence rests on. **Four of the five survive any
container split; the first does not:**

| # | rests on | survives a container split? |
|---|---|---|
| 2 | **no shared allocator** — ids from `H(world_seed, tick, subject_id, purpose)`; *"there is no id service, no counter, and nothing to serialise on"* | **yes** |
| 3 | the act array canonicalized by a content-derived key before resolution | **yes** |
| 4 | sum-then-clamp-once | **yes** |
| 5 | **fixed-point integers** — *"integer addition is associative and commutative, so order independence stops being a claim and becomes a fact"* | **yes** |
| **1** | **the world is frozen from the end of MATTER to the start of RESOLVE** | ⚠ **NO** |

**A barrier is global by definition.** Give each container its own clock and there are no longer four
barriers but N×4, and the freeze holds only *within* a container: a `choose` running in container A's
DELIBERATE reads a world container B's MATTER has already moved. **Law 2 does not catch this** — the
person is not omniscient, they are reading a world at an undeclared time.

> ### **THE RESOLUTION, AND IT COSTS NOTHING: A CONTAINER PARTITIONS A BARRIER'S BODY. IT NEVER OWNS A LOOP.**
>
> This is not a compromise; it is what two of the six steps already are. `04` §1 declares DELIBERATE
> *"a MAP, not a barrier · pure · any order · parallel"* and WITNESS *"global fan-out, ONE pass."*
> **The holon partitions work inside a phase, and the phase boundary is the only synchronisation point
> in the design.**
>
> And the head already licensed exactly this shape of concession, at exactly this granularity —
> `01_THROUGHLINE.md` LAW 3: *"A Query MAY be cached. The cache is built **AT A BARRIER**, is
> READ-ONLY until the next barrier, and is **DISCARDED there**. Nothing inside a parallel map builds
> one."* **Barrier granularity is the design's existing answer to "how do containers cooperate without
> storing anything."** R-1's *"compute an aggregate over its descendants on demand"* is affordable
> because of it.

### C2 · "Self-sustaining" versus **`04` §8: "No phase in which a container decides"**

`04_THE_SEASON_LOOP.md` §8's first row: *"**No phase in which a container decides.** Every decision has
a person's id on it."* A container that "sustains itself" is one refactor from being an actor, and it
is the most tempting refactor in the design, because a rung is exactly where intuition puts *"the
settlement decides to ration."*

> **RESOLUTION — a container owns STATE and SCHEDULE. It never owns a DECISION.**
>
> **Every rung is an address slot** (§2.1). A `Rung` owns `matter`, `dates[]`, `stake[]`, `envelope`,
> `judging_set_rule` — **arrangements, not choices.** Every choice that happens *at* a rung is
> `choose(person, view, sensation)` for a named person standing in it.
>
> **And it is enforced the way the head enforces everything else — by a parameter list.**
> `08_FUNCTION_SURFACE.md`: *"The enforcement in this shape is not a rule anyone remembers. It is a
> parameter list that fails."* **No container appears in `choose`'s signature**, so a deciding
> container would have to be passed one, and that fails at the call site.

**T5 is the worked example and it is already right:** demands aggregate upward *"filtered at a rung"*
— **and the filter is a named person who pays for the filtering.** The rung is where the filtering
happens; the person is who does it. **That distinction is the whole of C2.**

### C3 · The key system — **one log, re-derived rather than inherited**

The proposition asks for *"a comprehensive key system."* **The head has one and it is not called
that.** From scratch, on chain sources only:

| the piece | the head |
|---|---|
| the record of what happened | `Event`, a row in an **append-only** log with enforced invariants — id uniqueness, referential integrity on `causes[]`, cycle-freedom, a content hash (`10_GODOT_4_6.md` §6) |
| provenance | **`causes[]`, required and NON-EMPTY** (#351 §4.4) — measured as the gap: *"the substrate of the entire emergent-narrative claim, declared and never populated"* |
| who saw it | `witness(Person, Event) -> Claim[]`, per-person, **with no collection signature to call** (T3) |
| what a person believes about it | `Claim`, in the holder's **own** ledger; attribution is a per-witness Claim, **never a field on the Event** (#351 §4.4) |

> **The holonic addition is ONE RULE, and it is R-2 turned into a contract:**
>
> ### **A KEY CROSSING A RUNG BOUNDARY IS EITHER AN AGGREGATE (UP) OR A REFRACTION (DOWN). NOTHING ELSE CROSSES.**
>
> Not a state write, not a pushed value, not a reach-through read. R-1 already forbids the pushed
> aggregate (*"may not receive a pushed aggregate"*); R-2 already names the two legal emissions. **What
> is missing is that nothing owns the check** — which is M1, and `02_THE_WRAPPER_LAYER.md` §3.

**And one log, not two — re-derived without appealing to what executes.** Two logs cannot share a
`causes[]` chain, so an Event in log A can never name an Event in log B as its cause; T3's multiple
perspectives on one event and the head's arcs-as-provenance-chains both break at the seam. **This is
also why `09_THE_SEAM.md` §2 refuses a *"subsystem-specific key type family"* as one of its four
leaks.** Same rule, one scale down.

### C4 · **R-1's on-demand aggregate** versus **#351's L3 clause 2**

**The one place two in-chain documents genuinely pull against each other**, and a wrapper author meets
it on day one.

- **R-1** (#350): a rung *"may COMPUTE an aggregate over its descendants ON DEMAND."*
- **L3 clause 2** (#351, the head): *"no resolver-side Query may aggregate per-person tallies across
  holders."*

**They are compatible, and the boundary has never been drawn.** L3 clause 2 exists because the earlier
bound did not bind: define a per-`(Person, axis)` monotone counter — legal, since every increment is in
the holder's own ledger — then `Query`-sum it over a cohort. *"That is stored, monotone,
**never-decaying** unrest in all but name — **worse than the field L3 banned, because the banned field
could at least go down.**"*

> ### **THE BOUNDARY, STATED ONCE:**
> **A rung's on-demand aggregate may compose over STRUCTURAL EDGES — `commit`, `contain`, `hold`,
> `succeed`, `oblige`, `tie`, `knot` — freely and at any depth.**
> **It may NEVER sum a monotone per-person tally across holders.**
>
> **Structural-edge aggregation cannot reconstruct the ratchet**, because an edge is not monotone: an
> edge can be destroyed, and `Tenure.until` (`02` §4.4) is what makes its destruction a fact. **A count
> of live `commit` edges falls when people leave** — which is `03_OWNERSHIP.md` §1.1's point exactly:
> *"a faction collapses when people leave, with no dissolution mechanism, because there is nothing left
> to be the faction."*
>
> **And it is checkable, which is why the head chose a read-side rule:** *"grep the resolver for a
> Query that crosses holders"* — *"where a provenance rule is not."* **A wrapper is the one place that
> grep has a fixed address.**

---

## §4 · H3 — WHICH STEPS A CONTAINER MAY RUN

### §4.1 Two of six, and the head already wrote both that way

| step | per-rung or global? | why |
|---|---|---|
| **CALENDAR** | **GLOBAL barrier** | dates come due world-wide; *"CALENDAR must not advance the season counter"* twice |
| **MATTER** | **PER-RUNG, joined at the barrier** | `wear`, larders, `yield`, travel are all **rung-local by ownership** (`03_OWNERSHIP.md`: `Rung` owns `matter`; `Site` owns `condition`). **Nothing in MATTER crosses a rung boundary**, so the partition is free — and the barrier at its end is what freezes the world |
| **DELIBERATE** | **PER-PERSON, and the head says so** | *"a MAP, not a barrier · pure · any order · parallel"* |
| **RESOLVE** | **GLOBAL barrier** | acts contend for scarce things across rungs; #351 §4.3's ordered fold **needs one order**, and a per-container fold has none |
| **WITNESS** | **GLOBAL, one pass, and the head is emphatic** | *"global fan-out, ONE pass"*. The head's own retirement of the seven-phase alternative was that *"its WITNESS was not global — which makes its parallelism claim unsound rather than merely unproven"* |
| **CENSUS** | **shares WITNESS's join** | by construction |

> **So "containers run slices of the season loop" is TRUE of MATTER and DELIBERATE, and FALSE of the
> other four** — and it is true of those two **as a partition inside a global barrier**, never as a
> container's own loop.

### §4.2 The one nesting form, and it is already specified

`09_THE_SEAM.md` §1: *"**A contest is the season loop, nested.** It attaches at exactly one place —
**RESOLVE** — where a conflict subdivides the tick and runs the same steps over a smaller person set on
a shorter clock."* And `04` §8: *"**A battle, a hearing, an examination committee and two brothers
arguing over a barn are the same call with different act vocabularies**, and that is the entire
integration story."*

**That is a self-sustaining container running a slice of the loop — the proposition's own request,
already designed.** Its four bounds are what any future container form must inherit: **one attachment
point**; **four lines across the boundary and a fifth is a leak**; **a depth cap that is a required
caller-supplied argument with NO DEFAULT** ([engine] exceeding GDScript recursion depth is *"a CRASH,
not a catchable error"*); **registration by registry row, resolved at boot** — *"a missing provider is
a startup failure with a name in it, not a `null` three seasons into a campaign."*

### §4.3 Why no container gets a clock — the in-chain argument

**The head has no termination proof, and says so.** #351 §6.2 lists as an open specification debt:
*"**A termination argument per self-feeding loop.** Four arcs plus the King are spirals; **nothing
bounds one.**"*

**What does exist is the barrier structure itself.** Four global barriers per tick bound within-tick
propagation to one pass, because nothing emitted after a barrier can re-enter the step before it — and
`04` §8 makes the consequence a design commitment rather than an accident: ***"No reaction inside a
season. Reaction latency at person scale is one season… You anticipated, or you are late."***

> **Per-container clocks delete that bound.** With no shared tick there is no "the barrier", so an
> emission from container A can re-enter container B's already-passed step in what is, from B's side,
> the same season. **A→B→A within one season is exactly the spiral #351 says nothing bounds** —
> and the barrier structure is the only thing currently standing between the design and it.
>
> **You do not spend the only bound you have to buy parallelism you did not need.** `10` §1.1 prices
> the parallelism separately: `WorkerThreadPool.add_group_task` over DELIBERATE, available since
> **Godot 4.0**, *not* version-load-bearing. **The map is already parallel. The clock buys nothing.**

### §4.4 The verdict

| form | verdict |
|---|---|
| a container **partitioning MATTER or DELIBERATE**, joined at the global barrier | **YES — and the head already writes both that way** |
| a **nested contest** at RESOLVE, four lines, no-default depth cap | **YES — the only nesting form** |
| a container running **CALENDAR, RESOLVE, WITNESS or CENSUS** on its own | **NO — §4.1** |
| a container with **its own clock** | **NO — §4.3** |
| a container that **decides** | **NO — C2** |
| a **per-scale or per-subsystem key family** | **NO — C3, and `09` §2's fourth leak** |

---

## §5 · THE HEAD'S OWN TEST, RUN ON THIS PROPOSAL

`01_THROUGHLINE.md` §6 requires four questions of any proposed addition, in order. **A proposal that
exempts itself from the head's admission test is asking for a licence the head refuses everyone else.**

**1 · N — name the emergent possibility lost if the wrapper is cut.**
> **Cut it and R-1/R-2 become unenforceable, so a rung reads a descendant directly.** The head names
> that consequence itself: *"A cross-rung read is the single easiest way to destroy **T5 and T6**,
> because **once the realm can read a person directly there is no reason for the ladder to exist and
> every intermediate rung quietly becomes decoration.**"* **The lost possibility is the middle of the
> ladder** — provincial and territorial politics as anything other than a label on a map.

**2 · Is the N-line FALSE — does something already ruled in provide it?**
> **Partly, and this is the honest half.** The `Rung`'s *ownership* already does a lot: a rung owns
> `matter` and no social aggregate, so most cross-rung reads have nothing to read. **What ownership
> does not provide is the check on emissions** — nothing in the head stops a module emitting a Key
> whose target is two rungs away, which is R-2's *"no module reaches through another"* with no owner.
> **So the N-line survives, narrowed: the wrapper earns its place on the emission side, not the
> ownership side.** M1's scope shrinks accordingly, and `02_THE_WRAPPER_LAYER.md` is written to it.

**3 · E as a ratio, never a fourth averaged axis.**
> **The wrapper adds one object per subsystem and no new state.** It is the smallest thing that can own
> an emission check, and §4's refusals delete four candidate powers from it. Distilling further —
> making the check a convention instead of an object — is exactly the *"refusal only a reader
> enforces"* the head's `04` §7 flags as its weak point.

**4 · R at seats a player can occupy.**
> **The wrapper is invisible to every seat and must stay so.** It changes no option set, adds no verb,
> grants no bonus. **If a player can tell which wrapper handled their act, it has become a decider and
> C2 has been broken.** That is the sharpest available test of this whole proposal and it is §8's
> first falsifier.

---

## §6 · WHAT THIS REFUSES

| refused | why | what pays |
|---|---|---|
| **a per-container clock** | §4.3 — it deletes the only within-tick bound the design has, against a debt #351 already flags as unbounded | intra-season parallelism beyond the phase map. **Nothing else** — the DELIBERATE map is already parallel at Godot 4.0 |
| **a container that decides** | C2; `04` §8; LAW 1 | nothing — every decision a rung "wants" belongs to a person standing in it |
| **a second nesting form beside `contest()`** | `09` §2 *"no second resolver"*, which `04` §7 calls *"the highest-value conventional cell in the entire shape"* | nothing measured — the seam already covers battle, hearing, committee, and two brothers over a barn |
| **a key family per subsystem or per scale** | C3; `09` §2's fourth leak | nothing — a subsystem varies by a **declared extension** (`09` §3), not by a fork |
| **a wrapper that holds state** | it becomes a second owner of a value `03_OWNERSHIP.md` already assigns — that document's §1.3 gap 4 reproduced deliberately | nothing — a wrapper's job is emissions, not storage |
| **mirroring the ladder in the type system** | `10` §5.2 — [engine] GDScript's `class_name` namespace is **flat and global**; there is one `Person`, project-wide | nothing. The ladder is a directory tree and a `kind` enum |
| **a new guard, validator or dashboard** | the only checks named anywhere here are the two in `01` §5.2, both load-bearing on the port | nothing. **This proposal creates no directory outside its own** |

---

## §7 · WHAT IS OPEN

**Nothing here is escalated.** Under the head's own scoping the two candidate escalations both
dissolve: *"where does `Event` live"* is answered from scratch in C3 (one log, because two cannot
share a `causes[]` chain), and *"is the architecture holonic"* is answered by R-1/R-2 already being in
the head. **What remains is unfinished specification, and it is named rather than flagged.**

- **#351 §6.2's termination debt is the real blocker and this proposal does not close it.**
  *"Four arcs plus the King are spirals; nothing bounds one."* §4.3 shows the barrier structure is the
  only bound and that a container clock removes it — **that is an argument for not making things
  worse, not a termination proof.** A spiral inside one tick is still unbounded.
- **`judging_set_rule` is unspecified** (#351 §6.2), *"so nothing is decided at a sitting"* — and T5's
  *"filtered at a rung"* runs through it. **The upward half of the holonic story has a hole at exactly
  the point where filtering happens.**
- **WITNESS as specified fans every Event to every person** (#351 §6.2), so nothing said in private is
  private. A wrapper does not fix this and must not be presented as fixing it.
- **The act budget** (#351 §4.2) — one act versus ~5 with `budget()` a Query — is the head's own
  unpriced reversal and is untouched here. **Nothing in this proposal depends on which way it goes.**

---

## §8 · FALSIFIERS

**Nothing in this document executes**, which is a weaker position than #351's and is the first thing to
say about it. Each claim carries the test that would show it wrong.

| claim | what would prove it wrong |
|---|---|
| §5 · **the wrapper is invisible to every seat** | one seat, one season, where a player's option set, roll, or outcome differs by which wrapper handled the act. **If this ever fires, the wrapper has become a decider and C2 is broken** — this is the sharpest test of the whole proposal |
| §1 · R-1+R-2+T5+T6 is a complete container architecture | a holonic property the four do not supply, that the proposition needs. The candidate is *termination*, and §7 concedes it |
| §2.1 · H1 is already true | a `Rung.kind` in `02` §2.2.1 needing its own type. `person` is the candidate and `02` §2.2.1 pre-empts it: the rung is the address slot, the `Person` stands in it |
| §4.1 · exactly two steps partition per-rung | a MATTER or DELIBERATE operation that must cross a rung boundary within its own step, or a CALENDAR/RESOLVE/WITNESS/CENSUS operation that never does |
| §4.3 · a container clock deletes the only bound | a per-container scheme that still yields *"no reaction inside a season"* — the head's stated latency commitment — without a shared tick |
| C3 · one log, two cannot work | a two-log design where an Event in A names an Event in B in `causes[]` and the chain still walks. **`10` §6's invariants are what make this hard** |
| C4 · structural-edge aggregation cannot rebuild the ratchet | an aggregation over `commit`/`contain`/`hold` that is monotone in a quantity no one's ledger holds. `Tenure.until` should forbid it; if it does not, the boundary needs a third clause |
| §5 · the N-line survives narrowed | show that the head already owns the **emission-side** check — that something already stops a module emitting past its parent. **If it does, M1 is void and this proposal is one document shorter** |
