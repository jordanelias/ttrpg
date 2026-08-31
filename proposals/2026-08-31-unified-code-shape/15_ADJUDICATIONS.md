# 15 · ADJUDICATIONS — every ruling, its ground, its falsifier

## Status: PROPOSED (2026-08-31). **HELD BACK. These are design rulings taken by a session, not by
## Jordan, except where a Jordan ruling is quoted.** Nothing ratifies on merge.
## **Every ruling carries a falsifier: the observation that would show it wrong. A ruling without one
## is an opinion.**

---

## §1 · THE RULINGS

### R-1 · The shape is chosen on merit, and where the running tree already holds the best answer it is adopted **because it is best**

**Ruling.** Six things in the executing tree are adopted: the event log's invariant set · the
single-owner degree ladder with its demote-only extension · role resolution by string · per-operation
RNG substreams · **termination caps as required arguments with no default** · the exporter round-trip.

**Ground.** Each was examined and nothing better was proposed. **Not one is adopted for being
precedent** — the instruction is explicit that this shape is not bound to any.

**Falsifier.** A better answer for any of the six. **The most likely candidate is role-by-string, which
trades compile-time safety for a registry row**; if a typed alternative exists that keeps the swap-by-row
property, it wins.

**Cost.** Naming them as adopted invites the reading that the shape is a refactor. **It is not:** every
carrier, every edge, the loop's six steps and both epistemic and moral layers are greenfield. **CONFIDENCE: HIGH.**

### R-2 · The event log is the Event mechanism; it is NOT the Claim/witness/Query mechanism

**Ruling.** Compose `Event` onto the executing log. **Never build a second log.** Build `Claim`,
`witness` and the per-person ledger **fresh**.

**Ground.** The log is append-only, id-unique, referentially checked, cycle-free by construction and
content-hashed, and it runs default-on in every seeded campaign. **Observer resolution, per-observer
interpretation and the memory index exist only as pseudocode**, and the substrate's own docstring says
observer resolution is deliberately unimplemented **because the ordering rule it needs is unratified.**

**Falsifier.** Any executing per-person claim ledger or observer resolver in the tree; or the log being
dormant in default campaigns.

**Cost.** **Two sweeps reached opposite headlines and NEITHER survives whole.** *"Greenfield, not a
refactor"* is too strong; *"already canonical and executable"* is false for half the cluster.
**A reader who takes either headline whole will be wrong. CONFIDENCE: HIGH.**

### R-3 · The six steps are a refinement of the running three-phase tick

**Ruling.** `SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY` stays the mechanism; the six steps are the
contract implemented inside it. The seven-phase alternative is retired.

**Ground.** Verified this pass: three phases in that order, and **`ACTION`'s body is caller-supplied by
design** — which is exactly the seam the middle three steps need. The alternative's own header sat over
an eight-row table, its late writes were unlicensed under its own rule, and its fan-out was not global,
which makes its parallelism claim **unsound rather than merely unproven.**

**Falsifier.** The tick not running three phases in that order, or `ACTION`'s body not being
caller-supplied.

**Correction it forces.** A claim that this loop had no precedent is **false** — a canonical coarse
spine exists and this is its fine grain. **CONFIDENCE: HIGH.**

### R-4 · `Site` is a carrier and `condition` is primary state on it

**Ground.** An accumulator that reads its own previous value **is** primary state; a draw-weighted mean
over children has **no base case**; and node-keying collapses two sites into one scalar, yielding
**two wrong verb sets at once.** Base case supplied: at a Rung with no Sites, `condition` is
**undefined** and the verb gate does not fire.

**Falsifier.** Wrong if `condition` never reads its own previous value. **CONFIDENCE: HIGH.**

### R-5 · The Faction row is deleted; a faction is a Proposition plus its `commit` edges

**Ground.** Everything the row owned is derivable. Membership is `commit`; leadership, presence, density
and footprint are Queries; the persistent part is the immutable Proposition.

**Falsifier.** Any faction property **not** derivable from the proposition plus the commit set. The
candidate is stored institutional memory, which this shape homes in Records at a Rung.

**⚠ Cost, stated because it is the largest in the suite.** The running tree ships a faction stat-bag
written at **31 sites, 30 of which bypass the event log entirely.** **This ruling forbids that shape.**
The path is build-beside, flag-gate, golden-control, cut over — **never an in-place edit.**
**CONFIDENCE: HIGH on the architecture; the migration cost is real and is priced in `13`.**

### R-6 · The Partition's membership test is a schema column keyed on `(record-kind, field)`

**Ruling.** `social` is a static boolean on the **(record-kind, field)** pair, declared in the exported
schema and read by the resolver.

**Ground.** As a predicate over "subjects" the Partition **concedes a mixed class** — *a plague is
biology but it empties institutions* — and **"both" is not a partition.** Keyed on the field, a plague
is **several changes**, each answered separately: it may kill bodies and may not strike the village from
the roll. **The mixed class dissolves because there was never one change to classify.**

**Falsifier.** Any single field genuinely needing both drivers — which would reinstate the mixed class
at the level the column removes it. **CONFIDENCE: MEDIUM-HIGH.**

### R-7 · The modes are `create · alter · destroy`, and the coinages are dropped

**Ruling.** Drop `mint`/`efface`. **`mint` survives in exactly one place: `witness` MINTS a root token.**

**Ground.** The coinages were kept under protest on a **collision-avoidance** ground that does not
survive: these are **enum values**, not method names, and the one live "mint" offered as evidence of an
existing token is **an English comment.** With the ground gone, the two naming tests decide it
unopposed — *idiomatic in choosing*, and *idempotent in meaning* to a session with no context, which a
reader of `efface` cold does not get.

**Falsifier.** A real identifier collision for `create`/`destroy` in the port's namespace.
**CONFIDENCE: HIGH** — and it is cheap to reverse now and expensive later.

### R-8 · Fixed-point integers for `condition` and `stores`

**Ruling.** `int64`; `condition` on an **exported** scale, not a literal; `stores` in whole units;
coefficients as integer pairs; **round half-up on the non-negative magnitude with the sign applied
after**; sum then clamp once; band gates by cross-multiplication.

**Ground.** IEEE addition is not associative and **the band gate makes the difference observable** — a
one-ulp difference at a floor is a verb that exists in one ordering and not another, and a band crossing
is an **event people witness.** The sign rule is not pedantry: the two languages round negatives in
opposite directions, and **`wear` is a negative delta that fires every season on every site.**

**Falsifier.** No additive field ever both order-free-accumulated and band-gated. **CONFIDENCE: HIGH.**

### R-9 · The purity guarantee is *unreachable-by-name*, not *unwritable*

**Ground.** [engine] No module system, no visibility modifiers, no way to scope an identifier out of a
function body. **The port's own skeleton proves it** — resolver modules reach a global state object and
an event bus from inside their bodies, and one **writes to a field its own manifest declares
unwritable.**

**Falsifier.** GDScript acquiring a visibility modifier. **CONFIDENCE: HIGH.**

### R-10 · The degree ladder is four bands; a fifth is an amendment to the one owner

**Ruling.** The executing single owner implements four margin-based bands under a ruling that explicitly
ruled out the alternatives. **The design corpus's five-band ladder describing itself as shipped is
overturned.** A Disaster split is an amendment **made once, in that file** — never a parallel enum — and
coefficient tables key to the owner's enum.

**Ground.** Code is the formula. **Neither trace log recorded the collision**, which is why it is stated
loudly here. **CONFIDENCE: HIGH.**

### R-11 · Belief is about MORALS; what a person holds true is a Claim

**Ruling.** [Jordan, this session.] **`Belief` is a moral commitment** — a statement, backed by
Convictions, revised under **social** pressure, granting Momentum for aligned action. **What a person
holds true is a `Claim`.** The word *belief* is purged from this suite as an epistemic term.

**Ground.** The shipped object has a position, underlying convictions and a revision-pressure counter,
and is moved by social outcomes. **It has no evidence input at all.**

**Consequence.** `opening_set` is **claim-derived**, not "belief"; `norm_as_claimed`, not
"as believed"; interior-side floats, not "belief-side". **And WITNESS does not touch a Belief** — if
evidence could move one, investigation becomes moral re-engineering.

**Falsifier.** A mechanism in which evidence alone revises a Belief. **CONFIDENCE: HIGH** — Jordan-ruled.

### R-12 · A Proposition of mood `OUGHT` is an uttered Belief

**Ruling.** Adopted as the identification, not merely an analogy.

**Ground.** It grounds the entire political layer in a person: **a faction is somebody's morals, said
out loud, that other people signed.**

**Falsifier.** A faction proposition that no person could hold as a Belief — a purely factual banner.
**CONFIDENCE: MEDIUM-HIGH** — this is the suite's own inference, not a quoted ruling.

### R-13 · `Office.conferral` names the basis per office, and it retires an escalation

**Ruling.** `basis in { person_rooted, office_rooted, external }`, per office.

**Ground.** A warband's oath dies with its captain; a praefecture survives its holder; a see roots off
the map. **All three ship in one primitive**, and which an office uses is **world-authoring**.

**Consequence.** *"Is ecclesiastical office person-, office-, or externally-rooted?"* was escalated on
the ground that *the code is nearly identical and the game is not.* **With `basis` typed, the code is
identical, and the choice is one registry row per office.** The game question stays open; **nothing is
blocked on it.**

**Cost.** `sovereign_fraction` is total only over the office-rooted subgraph, **so it returns a pair and
every caller must handle a partial answer.** **Falsifier.** A caller needing a total answer over all
offices. **CONFIDENCE: HIGH.**

### R-14 · A conferral cycle is a first-class political condition, not an error

**Ruling.** An undefined sovereign fraction over a cyclic cluster is **play**, not a defect: no
determinate custody means the deciding article is ungradable for every claimant, which means the sitting
closes carried-without-force.

**Ground.** A defect filing against it was **withdrawn by its own author** once a lane supplied the
third reading. **Falsifier.** A consumer that cannot proceed on `undetermined`. **CONFIDENCE: MEDIUM-HIGH.**

### R-15 · The world-substrate hole closes as a `Site` kind, with zero new objects

**Ruling.** A substrate seam is a `Site`; its `condition` is the quantity; its `wear` is a params row.

**Ground.** Three independent arc lanes found the absence by three different routes, and **it is an
omission rather than a refusal** — every other absence in the design is argued for by name, and this one
has a **broken cross-reference** pointing at where it was supposed to be. A substrate's condition is
**the same class as larders and harvests**, which MATTER already ticks.

**Falsifier — and it is real.** Wrong if the metaphysics needs **one global scalar with no site
identity**. Then this is the wrong object and a new one is owed. **CONFIDENCE: MEDIUM-HIGH.**

### R-16 · Attention is one mechanism at two fidelities, and `forecast_mass` is cut

**Ruling.** `view()` and the Slate are the same `gate THEN rank` mechanism. **A player-only attention
module is forbidden** by the every-rung rule. `forecast_mass` is **cut for having no producer.**

**Falsifier.** A producer for `forecast_mass`; or an attention requirement at player fidelity that
cannot be expressed at NPC fidelity. **CONFIDENCE: HIGH on the unification, HIGH on the cut.**

### R-17 · Agentive actorless rows are specified and GATED

**Ruling.** The non-agentive channel ships. **An agentive row — an empire demanding a levy — is blocked
until a criterion exists that stops any actor being reclassified as weather.**

**Ground.** Law 1 says all actions are performed by characters; **an agentive actorless row is the one
shape that can eat that from inside.**

**Falsifier.** A criterion that draws the line. **CONFIDENCE: HIGH** — this is a hold, not a decision.

---

## §2 · WHAT THIS SUITE OVERTURNS

| # | overturned | why |
|---|---|---|
| 1 | *"zero design objects exist in the engine; greenfield, not a refactor"* | **half wrong** — the Event half exists and executes (R-2) |
| 2 | *"the Event/Claim/Query cluster is already canonical AND executable"* | **half wrong** — Claim/witness/Query are pseudocode, blocked on an unratified ordering rule (R-2) |
| 3 | *"`resolve` is already wired via the contract registry"* | the resolver field is a **strategy label**; the registered roles have incompatible signatures |
| 4 | **the five-band degree ladder as shipped** | the live owner implements four (R-10) |
| 5 | **the collision register is complete** | **five live-code meanings were missed**, including a tactical stance in running code |
| 6 | *"`mint`/`efface` must be kept for collision-avoidance"* | the ground is vacuous; the one cited occurrence is an English comment (R-7) |
| 7 | **the anti-flat-modifier constant `0.671`** | the executing owner has **`0.800`** — a die model without a botch face. **Found by two independent lanes** |
| 8 | *"the fractional-pool rounding defect is live"* | **fixed on 2026-08-21**; two logs are stale on it |
| 9 | *"a single project setting caused most of the compile errors"* | **the executed baseline four lines below the cited passage says the opposite** — the setting cleared zero broken scripts |
| 10 | *"belief" as the word for what a person holds true* | **Belief is about morals** (R-11) |
| 11 | *"the query catalogue is 23 rows"* | asserted in three places; **the count is contested and this suite marks its own catalogue as its own count** |
| 12 | *"matter events were licensed with nothing generating one"* | **broken by an antagonist** — a generator existed; the true claim is narrower |
| 13 | *"`opening_set` returns Acts"* | it returns **candidates**; typing it as acts makes the option set authored |
| 14 | *the Partition is decidable over subjects* | it concedes a **mixed class**; keying on `(record-kind, field)` is what dissolves it (R-6) |
| 15 | a fabricated citation above the frozen ceiling | **appears nowhere in the repository**; caught by a blocking gate |

---

## §3 · WHAT ESCALATES

**Five tests run in order before anything escalates: superseded · irrelevant · answered by a design
document · answered by precedent · answered by what makes sense for the architecture.**
**Most pending decisions are not Jordan's, and preserving a dead question is how a queue forms.**

### Closed here, with the test that closes them — do not re-escalate

| candidate | closed by |
|---|---|
| conferral rooting, including the ecclesiastical case | **test 5** — `Office.conferral.basis` makes all three expressible with **no code difference** (R-13) |
| the `leaders` comparator | **test 5** — faction-as-Proposition forces a commitment-derived comparator; adopt and record |
| the world-substrate object | **test 5** — a `Site` kind, zero new objects (R-15) |
| the tenth attribute | **test 5** — the roster is a **registry read**, so naming it is one row and blocks nothing |
| the degree ladder's band count | **test 3** — the code is the formula (R-10) |
| the act economy | **test 4** — reached independently by three routes |
| `mint`/`efface` | **test 5** (R-7) |
| the `wear` : restoration ratio; `season_factor`; the burden coefficient | **not rulings — MEASUREMENTS.** A number without a control is not a measurement, in either direction |

### The four that survive all five

> **1 · WHICH SEATS ARE PLAYABLE.** **R cannot be scored until this is answered per seat**, and it
> decides whether a dominated flagship instrument is a **defect** or a **portrait**. It is a question
> about the game, not the engine, and no document can answer it. **This is the highest-value
> escalation in the suite** because it unblocks an entire axis of the audit.

> **2 · STATE OWNERSHIP AND THE AUTOLOAD TABLE.** Already reserved in the governing port spec and
> **now forced**: the purity fix and the shipped singleton pattern are direct opposites.
> **Recommendation: rule the design's way** — autoloads presentation-only, world passed by parameter.
> **Until it is ruled, no port work touching state ownership starts.**

> **3 · THE SAVE MODEL.** Two incompatible load paths ship in the corpus. **Recommendation: the
> snapshot is the save; the log is retained for provenance and history; re-run-from-seed stays a test
> device.** One sentence to rule, a rewrite to leave. **Flagged loudly because it amends a
> Jordan-vetoable spec that says the opposite.**

> **4 · THE ENGINE VERSION — and the fork is MISLABELLED.** Nothing in this shape needs 4.6; two things
> need ≥4.4 and ≥4.5. **The real question is 4.3 versus ≥4.5.** New facts: the 4.6 side's one
> authoritative citation **points at a file that does not exist**; the 4.3 side has a declared project
> file, a CI pin and **two executed headless runs**; and **under a later ruling the compile baseline is
> void until re-measured.** The cheapest thing that prices it is **one headless run.**

**Twenty-plus candidates reduced to four.**
