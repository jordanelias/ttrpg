# FABLE 5 ADVERSARIAL FINDINGS — PR #343 / 10_SUPERSEDING.md
Every finding below was read directly off disk by the reviewer. Line refs are `10_SUPERSEDING.md:N`
unless prefixed with a #342 doc number (`proposals/2026-08-29-valoria-from-scratch/NN_*.md:N`).

SCOPE (Jordan, mid-session): the seasonal loop is the subject. Mass battle, personal combat and
social contest are the three DEFERRED subsystems. Everything else — world state, clocks, pressures,
threats, churn, character generation, event generation, governance at every scale, advancement,
demotion, obligation, offices, occupations, petitions, orders, field investigation, parliament and
parliamentary debate, factions, competing beliefs, epistemics, memory, truth — is IN SCOPE.

## TIER 1 — FATAL

**A1 · THE POPULATION HAS NO INFLOW.** #342 `09:528-548` (§8.1 "On demand, never on a clock") ships a
**demographic envelope** per containment node — "counts by age band, marks bundle, capability
distribution, carried as cohort weight" — and "**Births and deaths move weights**", plus FIVE mint
triggers (event names them · a telling puts them in a ledger · they occupy a role or office · they
enter a Knot · individuated as decisive in a contest). 10_SUPERSEDING carries only the DE-individuation
half (`:209`, P7 `:654`) and ONE mint trigger (`:203`). `grep -ci birth|natality` = 0. P1 `:648` has
"bodies age and die" and nothing that adds. **A seasonal churn loop whose population is monotonically
non-increasing.** This alone falsifies `:14` "A reader who has never seen #342 can read this file alone
and have the whole design."

**A2 · CHARACTER GENERATION IS GONE.** #342 `02:742` gives Practice's producer as "generation (§8) and
caused advancement"; `02:739` gives Mark's producers as "admission, birth, succession, ordination,
grant". 10_SUPERSEDING specifies a producer for NONE of the person's six fields (§2). The design can
describe a person and cannot make one. #342 `09:537-548` even ships the hard half — minting draws
address/marks/capability/stance from the cohort plus its dispersion.

**A3 · CAUSED ADVANCEMENT IS GONE.** #342 `02:186-189` verbatim: "**Advancement is caused, never
ticked.** A practice gains a rank when an attempt at a standard above its rank resolves *and* one of:
it was witnessed by a person holding the practice higher (a master saw it), or it failed at a cost the
person actually paid. There is no experience clock. This is the precedent's refusal of the scheduled
recovery tick applied at person scale." 10_SUPERSEDING KEEPS §14 row 12 (the scheduled-recovery refusal)
and DROPS its person-scale application. `grep -ci advancement` = 0. **No character in the design can
improve.** Advancement/demotion is on Jordan's explicit list.

**A4 · §14 ROW 4's RULE REINVENTS A SHIPPED MECHANISM AND RELOCATES IT ONTO AN OBJECT THAT CANNOT HOLD
IT.** C-12's fix writes "the cohort's claim stores the construal spread its members would have produced,
and an individuating member DRAWS from it and never inherits it." #342 `09:541-548` already ships
exactly this and stores it in the RIGHT place — **at the channel, not the cohort**: "tellings are stored
*at the channel*, not per person, until individuation … **Handed, not copied:** each stored channel claim
carries the construal distribution … and the minted person draws from it rather than receiving the
cohort's reading — two brothers minted out of the same hamlet in the same season can hold opposite
construals of the same twenty-year-old proclamation." A cohort is DEFINED as persons sharing stance
(`:203`), so it cannot hold a spread by construction. #342's placement is correct; the relocation is the
defect. Also note the document applied its own "zero shipped instances" discipline (§7.2) to convening
conditions and never re-ran it on its own row-4 rule.

**A5 · `choose` HAS NO CHANNEL FOR NEEDS, AND NEEDS ARE THE MOTIVE FOR EVERY ACT.** `:181-190`:
subsistence and standing read **the world**; commitment and exposure read **the view**. P2 `:649`
computes needs "Pure, parallel, **never stored**". P4 `:651` is `choose(person, view)`. There is no path
from P2's output to P4's input that does not either (a) store needs on the person — P2 forbids it, §4.2
`:340` puts needs in the **Nobody** row — or (b) put world-derived scalars into the View, which §3.3
`:265` ("View is assembled, not filtered") and §14 row 2 forbid. **The design's central enforcement
mechanism has no channel for its central motivational input.**
> PROPOSED FIX (primitive-reducing, not additive): **a need is a sensation, and a sensation is a claim.**
> Mint needs at P2 as firsthand claims in the person's OWN ledger with source `firsthand(body)` — the
> §3.2 vocabulary already has the shape and forbids a null source. View assembly then picks them up by
> the ordinary salience rule, `choose` keeps its signature unchanged, "stale relative to the world" is
> automatic, and **the category "need" is deleted from the design** — it becomes a claim like everything
> else. This also makes hunger arguable at a sitting (§12), which the design wants and currently cannot do.

## TIER 2 — MECHANISM CONTRADICTIONS

**B1 · §6.4's CONFLICT RULE FORBIDS THE COMMONS.** `:664-666`: "Two acts conflict iff they share an
object and either mode is `exclude`, or both `alter` the same field" → routes to `contest`. §10.3
`:1049` requires "one boat among a harbour's forty" and §10.4 `:1096` sums "Σ (this season's resolved
condition deltas)". Under §6.4 all forty `alter` acts on `condition(harbour)` conflict pairwise. **The
tragedy-of-the-commons mechanism and the conflict rule are mutually exclusive as written.**
> FIX: the real criterion is **commutativity, and it is a property of the FIELD, not the act.** Declare
> it on the schema: `condition` is additive-alter (all writers apply, order-independent — which §5.5
> already demands); a succession pointer is exclusive-alter (contested). One word on a field definition
> instead of a case in the resolver, and §6.4's rule gets SHORTER.

**B2 · `capacity(date)` IS DOUBLE-COUNTED — SPENT AT `carry` AND USED AS THE CAP AT `compose_agenda`.**
§8.2 `:876` charges carry "one item of the container's standing-date capacity" (faithful to #342
`05:176`). §4.3 `:399` and §8.4 `:931` use it as the admission cap — "admits the top `capacity(date)` of
what was carried" — and §4.3 `:399` asserts "Carried items may exceed capacity — seventeen seatholders,
eleven items". **If carry spends it, nothing can exceed it and compose_agenda has nothing to select
over** — and the convener's power, which §12.4 `:1275` calls "the cheapest real power in the game",
evaporates entirely.
> FIX: **`capacity(date)` is a SELECTION CAP, never a currency.** `carry` spends `seat_items` only. This
> also repairs §4.3's own thesis, which is currently false in kind: it claims "every price is denominated
> in one of exactly two quantities" while one of the two is not a price.

**B3 · `R ≤ 1 → automatic clean success` IS THE FAST PATH §14 ROW 8 FORBIDS.** §5.2 `:472-476` returns 0
and SKIPS the roll. §5.3's bands are a function of margin. Rolling at Obstacle 0 yields Costed (P≈0.6 at
Pool 1), Clean, or Overwhelming; the fast path returns Clean always. **It is an auto-resolve formula that
changes the outcome distribution, inside the one resolver, on a row §14 marks "Clear".**
> FIX: delete the branch. Resolve at Obstacle 0 like anything else and read the margin off the draw.
> Strictly simpler, removes a second path, and restores Costed Success at the low end where the design
> says (§2 `:199`) its low end is right.

**B4 · `transfer` HAS NO CONSERVATION PRECONDITION.** §11.2 `:1410-1413`: the only preconditions are
co-presence or a carrier act. §11.1 `:1372` states `stores` "may go negative: a shortfall is a debt". So
`transfer` with `stores(giver) < amount` **mints mouth-seasons from nothing.** Under §11.4's live choice
`stores` is the realm's denominator — an unbounded-below fungible transferable scalar is not money, it is
counterfeit, and it makes the §11.4 fork undecidable.
> FIX: `precondition: stores(hearth(giver)) ≥ amount`. One line, and §11.4's fork becomes honest.

**B5 · RESTORATION HAS NO SIZING RULE, AND THE IMPLIED ONE IS UNUSABLE.** §10.3 `:1035-1039` sizes only
damage: `Δ = − condition × f(degree) × share`. §10.4 `:1099` says only "restoration acts are positive".
Same multiplicative form ⇒ a site near 0 is near-unrestorable, which guts §10.1 `:1013`'s political
payoff ("*the seam must be restored* is a proposition, and the people whose practice used it are already
committed to it, so a political faction forms out of a physical fact").
> FIX, exact mirror, no new primitive: `Δ = + (1 − condition) × f(degree) × share`. Bounded by the same
> clamp, symmetric in form, gives a dead site a real road back, and keeps the anti-leverage property
> (still a fraction, still falls with N).

**B6 · P7's SALIENCE-RANKED EVICTION IS A FIFTH DECIDER-FREE CHANNEL, AND IT RUNS ON A SOCIAL QUANTITY.**
§13.2 `:1633-1643` licenses exactly four. P7 `:654` evicts "lowest salience" — and `salience` carries
`stanceweight` (§3.3 `:254`), so it is stance-derived. Exception 3 licenses *confidence decay*; eviction
is DELETION, not decay. §10.6 condition 1 `:1145` forbids a band edge over a social quantity; this is a
threshold over one, firing a permanent outcome, with no decider.
> AND IT DESTROYS §3.3's BEST INSIGHT. §3.3 `:262` says of the Templar "He is not hiding it and he is not
> lying; **he is not thinking of it.** … What is attenuated is **retrieval, not value**." Under
> stance-ranked eviction he eventually **genuinely does not have it** — motivated retrieval silently
> becomes motivated deletion.
> FIX: rank eviction by `confidence_live × recency` ONLY — the two clock quantities exception 3 already
> licenses. Forgetting stays epistemic; retrieval stays motivated; §3.3's sentence stays true.

## TIER 3 — UNIFORMITY, TYPING, PRIMITIVES

**C1 · `contest(container, prize, claimants)` HAS FOUR CALL SITES AND FOUR CLAIMANT TYPES.** §4.1 `:319`
claimants are **factions**; §6.4 `:666` they are conflicting **acts**; §9.2 `:1141` they are
`{enforcement, resistance}`; §10.3 `:1064` "whoever defends the site". The design's most-reused function
is untyped. FIX: claimants are always **a set of persons with a stake**; a faction, an act-side or a
defender resolves to that set before the call. One type, four sites, no branch.

**C2 · `Claim` AND `Proposition` ARE THE SAME PRIMITIVE TWICE.** §3.1 `:220` `Claim = (subject,
predicate, value, when, source, confidence, visibility)`; §12.1 `:1234` `Proposition = (mood, subject,
predicate, value, when, scope)` with "`HOLDS` is claim-shaped without the epistemic fields". FIX, bottom
-up: `Assertion = (subject, predicate, value, when)` · `Claim = Assertion + (source, confidence,
visibility)` · `Proposition = Assertion + (mood, scope)`. Then the `when`-interval collision rule is
defined ONCE on Assertion, and §3.1's collision and §12.1's "assertion and denial collide automatically"
become the same code instead of two statements of one rule — which is this document's own §0 rule.

**C3 · THE CLOSED PREDICATE VOCABULARY IS NEVER ENUMERATED.** §3.1 `:231` declares it CLOSED and makes
collision, entailment and relevance "functions of the predicate's *form*". **No form is listed anywhere
in the terminal document.** A closed set with no members is not closed; it is unspecified. Largest
implementability gap in the epistemics layer, and epistemics is on Jordan's list.

**C4 · `remit.acts` IS A "CLOSED SET OF FIVE" HOLDING SEVEN OPERATIONS.** §4.4 `:419-424`: issue,
determine, **confer/revoke** (two), dispatch, **convene** — which §4.4 `:428` then splits into two
operations (setting a date, `compose_agenda`). Five slots, seven operations.

**C5 · COHORTS GET A DIFFERENT VIEW RULE THAN PERSONS, IN THE DOCUMENT THAT FORBIDS THAT.** §2 `:205`:
"One type, not two: if a cohort were a different type, every mechanism would be written for one and not
the other." P3 `:650`: "K = 3 per cohort" against §3.3's `K = 7 + Focus + 2/Knot − penalty`. FIX: cohorts
hold no Knots by construction; a cohort's Focus is its distribution's mean; the general formula already
yields a small K. Delete the constant.

**C6 · `Focus` AND `Coherence` ARE READ BUT UNOWNED.** §3.3 `:252` reads both. §2's six fields carry
neither; §4.2's ownership table carries neither. #342 `02:747` owns Coherence explicitly (producer:
"drift + discrete writes"; carrier: the person; consumer: "mark reads, primaries, tellings,
individuation"). **§16 `:1871` makes Coherence-0 a live choice for Jordan about a quantity the document
never declares.** Another dropped owner (same class as A1-A3).

**C7 · A DEFINED SELECTOR WAS REPLACED BY AN ADJECTIVE.** §5.1 `:462` `Attribute[relevant](person)`
against #342 `02:190` `attr[triad_axis(attempt.practice)]`. `triad_axis` is a function; `relevant` is a
hope. Restore it.

**C8 · STANCE REFERENTS DO NOT COVER WHAT THE DESIGN DEPOSITS ON.** §2 `:176`: "persons, factions,
propositions and places". §8.2 `:911` deposits grudges on **containers** ("a claim naming only the
container deposits on the container"); §17.4 `:1940` notes **procedures** are missing. A hearth is a
container, not obviously a place. FIX that REMOVES a category: referent ∈ `Person | Faction |
Proposition | Container`, folding Place into Container (§1.2's ladder is the design's only spatial
structure), and procedure expressed as a Proposition per §17.4's own precedent answer.

**C9 · §4.1 SPECIFIES OWNERSHIP FOR FOUR OF SEVEN RUNGS.** Individual, Hearth, Community, Settlement
(`:296-320`). §1.2 `:98` names seven: "Person → Hearth → Community → Settlement → Territory → Province →
Realm". **Territory, Province and Realm own nothing.** "Governance and management at each scale" is on
Jordan's list; the design currently has governance at four scales and a naming convention at three.

**C10 · THE DETERMINISM SCHEME COVERS ONLY ATTEMPTS.** §5.5 `:559`: substreams from `(world seed, tick,
actor id, attempt discriminator)`. P1's rolls — `yield`'s `d10`, wounds festering, aging, death — have
no actor and no attempt, so the scheme does not reach the phase §6.3 licenses as a write class. FIX:
`(world seed, tick, subject id, purpose)`, where subject may be a site or a body. Generalises without
weakening order-independence.

**C11 · TWO DIE-READING SEMANTICS, UNDECLARED.** §5.1 `:456` counts successes (1–6 nothing, 7–9 one, 10
two). §11.1 `:1379` reads a raw uniform d10 as a magnitude in `(3 + d10)/8.5`. Two randomization
primitives in a document whose §5 is titled "one roll". Either license the second reading with its
reason (nature has no skill), or express `season_factor` as a pool and keep one die-reading in the engine.

**C12 · EIGHT PHASES ARE CALLED SEVEN.** `:54`, `:624`, `:641` say seven; the table `:647-654` lists
P0–P7 = eight.

**C13 · THE PHASE LIST CONFLATES "BARRIER" WITH "STEP" (optimization + modularity).** P0/P1/P5/P6 are
genuinely global (calendar, matter, resolve, witness). **P2/P3/P4/P7 are per-person pure maps.** Stating
the loop as **four global barriers + one per-person map** is faster (two fewer full-population passes;
needs and views never materialize as populations), more modular (the map is one function: person +
frozen snapshot → `(act, ledger delta)`), and it TIGHTENS §6.3: the three write classes are exactly the
three global phases that write, and the per-person map writes nothing but the person's own interior.
That is a stronger licence than §6.3 currently states.

**C14 · THE TWO ALLOWANCES SHOULD BE ONE, AND THAT DISSOLVES D-2 — THE DESIGN'S LARGEST OPEN RULING.**
§6.1's one act per season and §4.3's `seat_items` are both "a finite per-period spendable allowance
owned by an entity". Make `seat_items` an **earmarked sub-budget of acts** — hours spendable only on
sitting business — and: D-2's fork becomes "how large is the earmark", not "one act or several"; **the
D-16 cohort exploit prices itself** (individuating splits a cohort's weight, it does not mint act
budget); and §4.3's "two quantities" becomes one primitive with a tag. Combined with B2, the design goes
from three capacity-like objects to **one `Allowance(owner, period, size)` primitive and one selection
cap.** Largest primitive reduction available in this document, and it answers §16's largest open ruling
from architecture rather than escalating it — which is `CLAUDE.md` §0 test 5.

## TIER 4 — COVERAGE AGAINST JORDAN'S EXPLICIT LIST (seasonal loop in scope; MB/PC/SC deferred)

WELL SPECIFIED — containment ladder §1.2 · factions and actions §1.3/§8.7 · epistemics, memory, truth
§3/§13.4 (the strongest material in the suite) · petitions §8 · orders §9.3 · obligation §4.1
(`requisition`) · offices §4.4 · conflict §5/§6.4 · clocks §7 · competing beliefs §3.3/§13.4 ·
**parliamentary debate §12 — the stasis ladder plus twelve named faults with severities is the
best-specified object in the document and should be treated as the model the rest is held to.**

ABSENT OR ONE LINE — character generation (0) · advancement and demotion (0) · birth/natality (0) ·
occupations and roles distinct from office (0) · **field investigation** (one sentence, `:1712`,
asserted as "the engine's answer to its own epistemics, not a subsystem", with **no verb, no cost, no
resolution path**) · threats and pressures (plague 0, invasion 0, external threat generator 0; off-board
polities are §16's unresolved live choice) · **matter-event generation** (§13.2 exception 2 LICENSES
storms and §10.6 gates them; **nothing generates one**) · governance above Settlement (C9) · **`Venue`
has 17 parameters (§12.4 `:1268-1270`) and not one has a range, default or example value anywhere** —
in the document meant to be the ideal code shape, its most parameter-heavy object is entirely unvalued.

## TIER 1 (continued) — added after Jordan's scope clarifications

**A6 · NOTHING IN THE DESIGN CREATES A STRUCTURE. THE WORLD CAN ONLY LOSE THEM.** Verified by exhaustive
grep of 10_SUPERSEDING.md: there is no act that founds a settlement, builds a site, creates a container,
or establishes an office. (`establish` appears 14× and is ALWAYS the noun `establishment` — the persons
an office employs; `found`/`construct` are the ordinary English verbs, never the game verb.) §10 lets
`condition(site)` fall and (per B5, once sized) rise, but **no site ever comes into being**; §4.4 defines
an Office tuple with no constructor; §1.2's ladder has no act that adds a node. Combined with A1 (no
births): **every structural quantity in the design is monotonically non-increasing.**

**A7 · JORDAN'S GUARANTEE — "each season the world changes, with or without the player" — IS NOT MET BY
THE FOUR LICENSED CHANNELS, BECAUSE ONE OF THEM IS INERT.** §13.2 `:1636-1641` licenses exactly four
non-act channels. Audited:
| # | channel | state |
|---|---|---|
| 1 | metabolism and nature | **live** — larders, bodies, `yield` |
| 2 | matter events (storm, siltation, worked-out seam) | ⚠ **INERT. §13.2 licenses it and §10.6 gates it with three conditions, and NOTHING GENERATES ONE.** There is no matter-event generator anywhere in the document. §10.4 `:1114` makes `condition` **act-only** by ruling (D-1), and §15.19 records the narrowing — so the one channel that could produce untouched material change was closed and its replacement was never written |
| 3 | memory confidence decay | live |
| 4 | calendar — lapse only | live |
So the guaranteed seasonal change, absent NPC acts, is: **larders draw down, bodies age and die, memories
fade, deadlines pass.** Every one is a decay. **As specified, the world can only run down.** NPC acts are
the real churn engine and they are genuine — but A1 removes their population's inflow, so even that decays.
> FIX (composes with B5 and A1, adds no new object): the matter-event generator is the **`season_factor`
> roll the design already ships** (`13:70-71`, §11.1). Let an extreme draw on that territory-scale roll be
> the event — a storm is a bad `season_factor`, already impermanent by construction, already nature's, and
> already inside a licensed write class (P1/matter). That is exception 2 restored with **zero new
> primitives** and no violation of D-1's act-only accumulator, because the event acts on `yield`, not on
> `condition`.

## TIER 4 (extension) — THE GENRE LINEAGE, MAPPED TO SEATS

Jordan names the lineage: grand strategy · strategy · 4X · RPG · city builder · political/economic
simulation · management · interactive fiction · detective · historical precedent. Each implies a seat.

| lineage | the seat in this design | state |
|---|---|---|
| **interactive fiction / political sim** | the sitting: stasis ladder + twelve named faults (§12) | **BUILT, and it is the best object in the suite** |
| **grand strategy** | the down-stroke: one order, thirty-five executors, reports-as-claims (§9.3) | **BUILT and excellent** |
| **political simulation** | petition, carriage, agenda, burial, expiry (§8) | **BUILT** |
| **detective** | field investigation | ⚠ **ONE SENTENCE** (`:1712`). The epistemics layer that would carry it is world-class and there is **no investigative verb, no cost, no resolution path.** The detective seat is the single largest built-adjacent opportunity in the design — everything it needs exists |
| **RPG** | advancement, character growth | ⚠ **GONE** (A3). #342 shipped `02:186-189` and it was dropped |
| **RPG / world churn** | character generation | ⚠ **GONE** (A2, A1). #342 shipped `09:528-548` and it was dropped |
| **city builder / management** | building, founding, infrastructure | ⚠ **ABSENT** (A6). Sites degrade and cannot be created |
| **4X** | expansion, founding, borders | ⚠ **ABSENT** (A6, C9). No act adds a node; three of seven rungs own nothing |
| **economic simulation** | market, price, exchange | ⚠ **STATED AS FAILING** by the document itself (§11.5, §15.6) — gift constructs, market does not |
| **strategy / threat** | external pressure, plague, invasion | ⚠ **ABSENT.** `threat`/`plague`/`invasion` = 0. Off-board polities are §16's unresolved live choice |
| **historical precedent** | caste at the second gate, cadet branches, hostage politics, non-delivery vs refusal | **BUILT, and it is the design's strongest claim to originality** |

**The pattern the table shows, and it is the review's central conclusion:** the design is superb at
**contest over what exists** and absent at **bringing things into existence**. Every seat it has built is
a seat about disputing, deciding, obstructing or interpreting; every seat it is missing is a seat about
making — a person, a rank, a building, a settlement, an event. That is one defect with eleven faces, not
eleven defects, and it is why A1/A2/A3/A6/A7 should be read as a single structural finding.

## ★ THE CENTRAL FINDING, RESTATED PRECISELY — supersedes the "creation" framing above

Jordan names the loop as five paired flows: *"things can be **built or destroyed**, people can be **born
or die**, ideas can be **disseminated or purged**, demands can **aggregate upwards**, directives can
**propagate downwards** — the world is always in flux."* Audited limb by limb against 10_SUPERSEDING:

| flow | limb A | limb B |
|---|---|---|
| built / destroyed | ⚠ **ABSENT** — no act creates a site, container, office or settlement (A6) | **present** — §10.3 `alter`, §10.3 `exclude`, `12`'s `burn` |
| born / die | ⚠ **ABSENT** — no birth, no demographic envelope (A1) | **present** — P1 `:648` "bodies age and die" |
| disseminated / purged | **present and superb** — §3 tellings, §9.1 publication by presence and channel | ⚠ **ABSENT** — verified by grep: `purge` 0, `censor` 0, `recant` 0, `destroy_record` 0. `suppress` (5×) is only §8.7's *suppressed grievance* — a person's own unmet enabling claim, not an act on anyone else's ledger. `strike` (§12.2) kills a **ground at a venue**, which is a debate outcome, not an act on the world. **No act removes a claim from another person's ledger, destroys a record, silences a teller, or forces a recantation** |
| demands aggregate upward | **present and excellent** — §8 petition, backing, carriage | — |
| directives propagate downward | **present and excellent** — §9.3 one order, thirty-five executors | — |

**So the defect is NOT "no creation". It is sharper and worse:**

> **THE DESIGN HAS A RICH VOCABULARY FOR CHANGING THE STATE OF THINGS THAT EXIST, AND ALMOST NONE FOR
> CHANGING WHICH THINGS EXIST.** Stance, `condition`, standing, commitment, compliance, confidence — all
> richly movable by named persons. Persons, sites, offices, containers and claims — **none of them can be
> brought into or removed from the world by any act in the document.**

**And the proof is a three-item list.** The ONLY population-changing operations in all 2,017 lines are:
1. **death** — P1 `:648`, metabolism, decider-free
2. **de-individuation** — P7 `:654` / §2 `:209`, decider-free
3. **eviction of a claim** — P7 `:654`, decider-free (and see B6: it is a fifth unlicensed channel)
plus **individuation** (P7 `:654`), the single additive operation, which fires on "an event names one of
its members" (§2 `:203`) and is therefore also decider-free at the point of firing — and whose four other
shipped triggers and whole minting procedure were dropped from #342 `09:533-548` (A2).

> **ALL FOUR ARE DECIDER-FREE. THREE OF THE FOUR ARE SUBTRACTIVE.** In a design whose stated thesis is
> that **every active decision is made by a character**, and whose §13.1 rule is that **if no person acts
> the thing does not occur**, *no character can add or remove a single object from the world.* Existence
> is the one register the persons do not touch — and it is the register that empties on its own.

**This is why the coverage gaps cluster the way they do** (Tier 4): city builder, 4X, RPG-advancement and
detective are precisely the four lineages whose seat is an act that changes what exists — a building, a
settlement, a rank, a fact brought to light or buried. Each reads as a separate hole and all four are one.

**It is also why A7 bites.** Of §13.2's four licensed non-act channels, the three live ones are all decay,
and the fourth (matter events) is inert for want of a generator. The world's guaranteed seasonal change is
therefore **subtractive in every channel**, and the acts that would offset it do not exist.

**THE FIX IS ONE PRIMITIVE, NOT ELEVEN FEATURES** — and it is the bottom-up move the project asks for:

> Give the act vocabulary a fourth `touches` mode. §6.4 `:664` ships three — `read`, `alter`, `exclude`.
> Add **`mint`** and **`efface`**: an act may bring an object into the world or remove one from it, under
> the ordinary machinery — witnessed by presence (§1.4), contested where someone objects (§6.4),
> resolved in P5's acts class (§6.3, no new write class), sized by the same degree bands (§5.3).
>
> Then, with **no further mechanism**: `mint` a site is building · `mint` a person is birth, drawing from
> #342 `09:537-548`'s envelope · `mint` an office is establishment · `mint` a container is founding a
> settlement · `efface` a claim is the purge, the burned register, the forced recantation · `efface` a
> site is the razing that §10.3's `exclude` limb currently leaves unbounded (§15.17) · and **advancement
> is `mint` on a practice rank**, restoring #342 `02:186-189`'s caused-advancement rule as an instance of
> the general operation rather than a special case.
>
> **Two modes on an existing tuple close eleven gaps, four genre seats, and the asymmetry in three of
> Jordan's five flows** — and they close them *bottom-up*, as a property of the act primitive, rather
> than as eleven authored subsystems. That is the single highest-leverage change available in this
> document and it should be §6's rank 1.

## ★★ A8 · A FACTION CANNOT BE FOUNDED — and this is the sharpest instance of the central finding

Jordan, mid-session: *"Power is not static — power is something that happens. Factions are only as strong
as the people under their purview, and the extent to which those people can influence beyond themselves.
**All starting national royal factions may collapse in the game to be replaced with dynamically generated
ones.**"*

**FIRST, THE PRAISE, because §1.3 is a direct hit on the first half.** `:118-125`: *"Scale is derived and
gates nothing … Capacity to act at a node is not a property of size; it is the question **does this
faction hold a person who can act there** — which routes through persons."* `presence`, `density` and
`footprint` are derived, never stored; no roll takes size as a term; §14 row 9 forbids a `tier`/`level`
field. **That IS "power is something that happens," and it is the design working exactly as Jordan
describes.** Do not touch it.

**SECOND, THE DEFECT, and it kills the second half outright.** §1.3 `:129-132` ships **one** membership
operation: `commit(person, faction, Δdegree)`. Read its own worked cases:
- *"A **schism** is a subset whose commitment migrates to **a rival proposition**"* — the rival must
  already exist.
- *"a **merger** is members of A committing to **B**"* — B must already exist.
- *"**growth** into a national body is many commits"* — the body must already exist.

**Every case presupposes the target faction.** And a faction is *"a proposition plus a map from persons to
a degree of commitment. That is the entire object"* (`:113`). So founding a faction is minting a
**proposition** — and there is no operation anywhere in 2,017 lines that mints one. Verified:
- `:1490` — *"his stance **emits** a proposition"* — one clause inside a worked example in §11.5. No act,
  no cost, no witness, no `touches` entry, no phase. Not a mechanism.
- `:1742` — §14 row 9: *"The faction that **forms** out of a lost verb is an ordinary proposition plus
  commitments"* — asserts the forming and supplies no operation that forms it.
- #342 `02:746`, the object roll-up, gives the answer for the shipped design and it is fatal to the
  requirement: **`| Conviction signature | authored with each proposition |`** — **propositions are
  AUTHORED CONTENT.** A design in which every proposition is authored cannot dynamically generate a
  faction, by construction.

> **So the requirement Jordan just stated — starting royal factions collapse and are REPLACED BY
> DYNAMICALLY GENERATED ONES — is not merely unbuilt. It is unreachable under §1.3 as written**, because
> the only membership operation cannot create the thing it commits to, and the only source of
> propositions in the lineage is authoring.

**AND IT GUTS THE DESIGN'S FLAGSHIP EMERGENCE CLAIM.** §10.1 `:1013-1016` is the passage the whole
option-removal inversion is sold on: *"'the seam must be restored' is a proposition, and the people whose
practice used it are already committed to it, so **a political faction forms out of a physical fact with
no authoring at all**."* That sentence is **false as the document stands** — the faction forms only if a
proposition can come into being without authoring, and nothing in the design lets one. The single most
celebrated emergent behaviour in the suite rests on the one missing primitive.

**FIX — the same two modes, no new object.** `mint` a Proposition is founding a faction; `efface` a
Proposition is a faction dissolving. Both go through the ordinary act machinery: performed by a named
person (so §1.1's one-actor rule holds), witnessed by presence (so others learn of the new banner by
telling, at telling speed, exactly like a dispensation), contested via §6.4 where someone objects,
resolved in P5. Then:
- §10.1's claim becomes **true**: the smith whose verb died performs `mint(proposition: "the seam must be
  restored")` — an act, from his own need, with no authoring — and the others `commit` to it as §1.3
  already specifies.
- Jordan's collapsing-royal-faction requirement becomes reachable: the old proposition loses commitment
  to zero across its members (§1.3's departure, already shipped) and a named claimant **mints** a new one.
- **The conviction signature stops being authored** and becomes what it should be — derived from the
  minting person's own stance at the moment of the act, which is exactly the design's own "compute, never
  assign" discipline (§5.1) applied one level up.

**Add Proposition to the population-changing audit in ★:** it is a fifth object no act can create or
destroy, and unlike the other four it has **no decider-free channel either** — persons, claims, sites and
cohorts at least change population by death, eviction or individuation. **A proposition, once absent, can
never come to exist by any route in the document.**

## ★★★ THE TWO TRAJECTORY TESTS — Jordan's reachability probe, run

Jordan, mid-session: *"A player could start the game as a Duke or King and wind up years later being the
**leader of a powerless faction with no real holdings**. A player could start the game as an
**Investigator** and wind up years later being the **leader of a shadow faction that controls the realm
through a puppet ruler**."*

These are reachability probes over long-arc **identity change**, which is the game. Decomposed, the two
trajectories need **seven transitions**. Audited against `10_SUPERSEDING.md`:

| # | transition | state |
|---|---|---|
| 1 | **lose an office** | ✅ **WORKS** — §4.4 `:416` ships `revocation` in the Office tuple; `confer/revoke` is in `remit.acts` `:424`; §8.6 prices vacancy |
| 2 | **gain an office** | ✅ **WORKS** — conferral, §4.4/§4.5, and §4.5's office-rooted recommendation makes the chain resolve |
| 3 | **lose holdings** | ⚠ **UNREACHABLE except by dying** (A10) |
| 4 | **gain holdings** | ⚠ **UNREACHABLE** (A10) |
| 5 | **found a faction** | ⚠ **UNREACHABLE** (A8) |
| 6 | **lead a faction** | ⚠ **NO REFERENT** (A9) |
| 7 | **change occupation** (Duke → faction chief; Investigator → shadow chief) | ⚠ **NO OBJECT** (A11) |

> **Two of seven.** The design supports acquiring and losing a post, and supports none of the other five
> moves the trajectories are made of.

### A9 · A FACTION HAS NO LEADER, AND BOTH TRAJECTORIES END IN ONE
Verified by grep: `founder` 0 · `leadership` 0 · `spokesman` 0 · `head_of` 0. The word `leader` occurs
twice (`:435`, `:440`) and **both are §4.4's "a leader is not a modifier"**, about office pools. §1.3
`:113` is explicit: a faction is *"a proposition plus a map from persons to a degree of commitment.
**That is the entire object.**"*
**The refusal is CORRECT and must not be repaired by adding a field** — a stored leader is the tier field
§14 row 9 forbids, wearing a different name. **But the design owes a derivation and does not have one.**
> **FIX, in the design's own idiom:** leadership is a **query, never a field**, exactly like `presence`,
> `density`, `footprint` (§1.3) and `sovereign_fraction` (§4.5). Define
> `principals(f, n) = members with an address inside n who are `eligible` to act there (07:180-182),
> ranked by commitment degree × backing they can raise`. Then *"leader of a powerless faction"* is a true
> sentence about a man at the top of a query whose result set is small and whose members hold nothing —
> which is precisely Jordan's fallen Duke — and *"leader of a shadow faction"* is the same query over a
> faction whose memberships are secret. **No new state, and it composes on §1.3's existing roll-up.**

### A10 · `holdings` IS DEAD STATE — NO ACT IN THE DOCUMENT MOVES PROPERTY
- `holdings` occurs **twice** (`:307`, `:352`) and **both are descriptive** — the cadet-branch narrative,
  and a quotation of #342 `04:29-37`'s two-stake table. **No act reads it, writes it, or moves it.**
- `transfer` (§11.2 `:1410`) moves *"amount in the SAME `stores` scalar, mouth-seasons"* — **food, not
  property.**
- The Dispensation's typed term table (§9.1 `:1123-1125`) has nine members — `PriceTerm`,
  `ProhibitionTerm`, `LevyTerm`, `ExemptionTerm`, `EntryStandardTerm`, `ExcommunicationTerm`,
  `BlockadeTerm`, `TreatyClause`, `OrdenanzaTerm` — and a dispensation is defined as *"a change to what a
  container **permits, costs or requires**"*. **There is no grant, enfeoffment, confiscation or forfeiture
  term, and by its own definition a dispensation cannot move property at all.** Verified: `confiscat` 0 ·
  `enfeoff` 0 · `dispossess` 0 · `seize` 0.
- The only route by which a holding changes hands is the hearth's **succession pointer** on death (§4.1
  `:302`) — **decider-free, and it is the fourth subtractive decider-free channel in the ★ audit.**
> **So a Duke can be stripped of his post and cannot be stripped of his lands.** Trajectory 1's *"no real
> holdings"* is unreachable by any act, which also means confiscation, attainder, enfeoffment, dowry,
> conquest and the entire material stake of every noble intrigue in the setting are inexpressible.
> **FIX, which COLLAPSES TWO SYSTEMS INTO ONE and is historically exact for the period:** `Holding` is
> already an edge on the person for offices — `:367` `Holding := (person, office, since, conferrer)`.
> **Widen its second field: `Holding := (person, office | site, since, conferrer)`.** Then a fief *is* an
> office, `confer`/`revoke` in `remit.acts` are already grant and confiscation, `:367`'s *"Who holds the
> praefecture is a query, not a field"* becomes *who holds the manor* on the same query, and §4.5's
> conferral-basis ruling covers land tenure for free. **One field widened; no new verb, no new term type,
> no new object** — and it deletes the orphan `holdings` stake rather than adding to it.

### A11 · "INVESTIGATOR" IS NOT A SEAT
`occupation` 0 · `profession` 0 (already filed as Tier 4). *Field investigation* is **one sentence**
(`:1712`) asserting it is *"the engine's answer to its own epistemics, not a subsystem"* — **with no
verb, no cost, no resolution path, and no phase.** Trajectory 2's **starting seat does not exist**, and it
is the seat the detective lineage is played from.

### ✅ AND THE PRAISE, WHICH IS LARGE — TRAJECTORY 2's CONTROL MECHANISM IS THE DESIGN AT ITS VERY BEST
*"Controls the realm through a puppet ruler"* needs no new mechanism whatsoever, and the reason is the
design's deepest structural choice. Because `choose : (Person, View) -> Act` **takes no `World`** (§1.4
`:151-160`), the ONLY way to move another person's act is to change what he believes — so you feed the
puppet claims, and **his own `choose` produces the acts you wanted, from his own ledger, for his own
reasons.** He is not a puppet object with a controller field; he is a man acting on what he was told.
§4.2 `:344` — *"**Nothing anywhere stores control**"* — and §13.4's *"credit is constructed entirely out
of claims"* mean the shadow ruler's power is exactly a fact some people hold and others deny.
> **Puppet rule is fully expressible in the shipped design and requires nothing added.** That is a
> striking success and the review must say so: the hard half of trajectory 2 is DONE, and only its
> endpoints — being an Investigator, founding the faction, leading it — are missing.

**What the trajectory test adds to the central finding:** every one of the five failures is a
*population* or *ownership* change, and every one of the two successes is a *state* change on an object
that already exists. **The seven-transition table is the ★ finding measured on Jordan's own two arcs**,
and it should be §1's closing evidence.

## ★★★ TRAJECTORY TEST, EXTENDED — transitions 8 and 9 (Jordan, added after the first run)

*"Other transition: **lose a faction (be deposed)**, **acquire a faction**."*

Both are transitions of the SAME object A9 found has no referent, and the result is the strongest
evidence yet that the proposed fix set is right-sized rather than invented.

| # | transition | state NOW | state UNDER THE PROPOSED FIXES |
|---|---|---|---|
| 8 | **lose a faction (be deposed)** | ⚠ **no referent.** You cannot be deposed from a position that does not exist (A9). There is no leader field to clear, and no verb that clears one | ✅ **FREE — and it needs no verb at all.** Under A9's derived leadership, deposition is not an operation: it is **the query returning someone else.** Members `commit` away from you (§1.3's shipped operation, degree to zero is departure), or your backing collapses (§8.2's `regard_cost`/`regard_gain`, shipped), and a rival tops `principals(f, n)`. **Nothing is deposed; the ranking changes.** That is exactly Jordan's *"power is not static — power is something that happens"* |
| 9 | **acquire a faction** | ⚠ **partial and accidental.** `commit(person, faction, Δdegree)` ships (§1.3 `:129`), so you can join and deepen — but with no leadership referent there is nothing to acquire, and with no `mint` you cannot take a faction and **redirect** it, since redirection means a new proposition (§1.3 makes a schism *"a subset whose commitment migrates to a rival proposition"*, which must already exist) | ✅ **TWO CASES, BOTH CLOSED, AND THEY ARE CORRECTLY DIFFERENT.** *Acquire as-is* = `commit` + raise backing until you top the query. **Already shipped; needs only A9's derivation.** *Acquire and redirect* = `mint` a new proposition and carry the members' commitments to it. **Needs A8's `mint` — and it SHOULD be the harder of the two**, because taking a body and turning it to a new purpose is a schism you are performing on your own faction, which is the more consequential political act and the design is right to price it higher |

> **THE RESULT THAT MATTERS.** Nine transitions, and the two new ones required **no new fix**. Both are
> closed by A8 (`mint`/`efface` on a Proposition) and A9 (leadership as a query) — the two fixes already
> on the table — and one of them, **deposition, closes with no mechanism whatsoever**: it becomes an
> emergent consequence of two operations the design already ships. A fix set that absorbs new
> requirements without growing is the signature of a correct primitive; a fix set that needs a new rule
> per requirement is a feature list. **This one absorbed two and grew by nothing.**

### THE NINE-TRANSITION TABLE, FINAL

| # | transition | now | after A8 + A9 + A10 |
|---|---|---|---|
| 1 | lose an office | ✅ | ✅ |
| 2 | gain an office | ✅ | ✅ |
| 3 | lose holdings | ⚠ death only | ✅ A10 — `revoke` on a widened `Holding` |
| 4 | gain holdings | ⚠ | ✅ A10 — `confer` on a widened `Holding` |
| 5 | found a faction | ⚠ | ✅ A8 — `mint` a Proposition |
| 6 | lead a faction | ⚠ | ✅ A9 — `principals(f, n)` query |
| 7 | change occupation | ⚠ | ⚠ **STILL OPEN** — A11; needs the occupation object, and it is the one gap the three fixes do not close |
| 8 | **be deposed** | ⚠ | ✅ A9 — **free, no verb** |
| 9 | **acquire a faction** | ⚠ partial | ✅ A9 (as-is) + A8 (redirect) |

**Two of nine now; eight of nine after three fixes, none of which adds an object.** The residue is
transition 7, and it is Tier 4's occupation gap — the honest statement of what is still unbuilt.

## ★★★★ A12 · THE CONTAINMENT TREE IS STRUCTURALLY IMMUTABLE — "Kingdom absorbs a Duchy" is unreachable

**Jordan's correction to transition 9:** *"Acquire as in **integrate another faction into your own**, e.g.
**Kingdom absorbs a Duchy**."* That is annexation, not leadership takeover, and it changes the answer
completely — because in this design's ontology **a Kingdom and a Duchy are not factions.** §1.2 `:98`:
*"Person → Hearth → Community → Settlement → Territory → Province → **Realm**"*. A Duchy is a Province or
Territory; a Kingdom is a Realm. **Absorbing a Duchy is re-parenting a containment node.**

**Verified by grep — there is no operation that changes the containment tree's structure:**
`annex` 0 · `seced` 0 · `conquer` 0 · `vassal` 0 · `absorb` 0 · `border` 0 · `reparent` 0.
The only address-changing act in the document is **Admission**, and §4.1 `:312-313` scopes it precisely:
*"an act by persons who already hold standing, **changing another person's address** and conferring a
mark."* **A person's address. Never a node's parent.**

> **So the containment tree — the design's single load-bearing structure, the thing §1.2 calls "the
> derivation everything else rests on" — can have no node added (A6), no node removed, and no node
> re-parented. It is fixed at world creation forever.**

**What that makes inexpressible:** annexation, conquest, secession, partition, independence, vassalage,
personal union, the elevation of a settlement to a territory, the collapse of a realm into its provinces
— **every border change in the game.** For a design whose lineage Jordan names as grand strategy and 4X,
this is the genre's central verb, and there is no trace of it. It also silently caps §4.5's
`sovereign_fraction(root)`: the *"root-plurality"* it carefully handles as *"a political condition rather
than an invariant"* can never actually arise, because nothing can change what is under a root.

**And it explains a gap already filed.** §4.1 `:296-320` specifies ownership for four of seven rungs and
stops at Settlement (C9). Territory, Province and Realm own nothing **because nothing happens to them** —
there is no act at those rungs to own anything for. C9 is not an omission; it is the visible end of A12.

> **THE FIX, AND IT COLLAPSES THREE SYSTEMS INTO ONE PRIMITIVE.** A10 proposed widening `Holding :=
> (person, office, since, conferrer)` to `office | site`. Extend the observation one step and the real
> primitive appears — **the design already has ONE shape and spells it three times:**
>
> | shipped edge | subject | object |
> |---|---|---|
> | `Holding := (person, office, since, conferrer)` `:367` | person | office |
> | commitment edge `commit(person, faction, Δdegree)` `:129` | person | faction |
> | the hearth's **succession pointer** `:302` | node | node |
>
> All three are *a dated, conferred, revocable relation between a subject and a thing*, and §4.2 already
> files two of them in the same table cell (*"`Holding` edges and commitment edges"* `:336`).
>
> **Generalise once:** `Tenure := (subject, object, since, conferrer, degree?)` where
> `object ∈ Office | Site | Node | Faction`. Then, with **no new verb anywhere**:
> - `confer`/`revoke` on `Office` = appointment and dismissal (**shipped, unchanged**)
> - `confer`/`revoke` on `Site` = enfeoffment and confiscation (**closes A10**)
> - `confer`/`revoke` on `Node` = **annexation and secession** (**closes A12 — Kingdom absorbs Duchy**)
> - `commit` on `Faction` = the shipped membership operation with its degree (**unchanged**)
>
> **One edge primitive, four object kinds, and the two verbs already in `remit.acts` `:424`.** Annexation
> becomes what it historically was — a conferral, performed by a named person exercising a remit,
> witnessed, contestable, and refusable by the man being annexed, whose compliance is §9.2's ordinary
> contest. **Nothing is added to the engine; three special cases are deleted from it.**

**REVISED transition 9.** *Acquire = integrate another faction/polity into your own.* Two cases, and the
design gets one right already:
- **Faction absorption** — ✅ **already correct and on-thesis.** §1.3 `:130`: *"a **merger** is members of
  A committing to B."* It is many person-decisions, not an operation on factions, which is exactly the
  no-aggregate discipline. **Do not add a merge verb; §14 row 9 and §1.3 already forbid it and are right.**
- **Polity absorption (Kingdom ← Duchy)** — ⚠ **unreachable**, and closed by `Tenure` above.

### THE NINE-TRANSITION TABLE, CORRECTED AND FINAL

| # | transition | now | after the fixes |
|---|---|---|---|
| 1 | lose an office | ✅ | ✅ |
| 2 | gain an office | ✅ | ✅ |
| 3 | lose holdings | ⚠ death only | ✅ `Tenure`/`revoke` |
| 4 | gain holdings | ⚠ | ✅ `Tenure`/`confer` |
| 5 | found a faction | ⚠ | ✅ A8 `mint` a Proposition |
| 6 | lead a faction | ⚠ no referent | ✅ A9 `principals(f, n)` query |
| 7 | change occupation | ⚠ | ⚠ **STILL OPEN** — A11 |
| 8 | be deposed | ⚠ no referent | ✅ A9 — **free, no verb; the query returns someone else** |
| 9a | absorb a faction | ✅ **already right** — merger is many `commit`s | ✅ unchanged |
| 9b | **absorb a polity** | ⚠ **unreachable** — the tree is immutable | ✅ **A12 `Tenure`/`confer` on a Node** |

**Three of ten now. Nine of ten after four fixes — `mint`/`efface`, `principals`, `Tenure`, and the
matter-event generator — none of which adds an object to the engine, and `Tenure` REMOVES two.**
