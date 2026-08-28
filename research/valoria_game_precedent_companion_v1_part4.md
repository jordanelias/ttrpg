# Game Precedent Companion — Part 4: Reconcile and Unify

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: Parts 1–3 · joins to `valoria_systems_integration_master_v1_part4.md` §6

**Reading order:** [Part 1 · Corpus and Survey](valoria_game_precedent_companion_v1.md) → [Part 2 · Comparison, Complements, Synergies](valoria_game_precedent_companion_v1_part2.md) → [Part 3 · The Critique](valoria_game_precedent_companion_v1_part3.md) → [Part 4 · Reconcile and Unify](valoria_game_precedent_companion_v1_part4.md)

Part 3 judged each system against its precedent. This part does the two things that must follow:
**reconcile** the candidate imports against each other and against what Valoria already has, then
**unify** them into a small number of coherent moves rather than a list of bolt-ons.

The order matters. A precedent survey that ends in a list of twenty-four imports has not finished its
job — twenty-four independent additions to a tree already carrying 51 uncalled mechanisms is the
failure the integration master measured, arrived at from a new direction.

---

## §8 RECONCILIATION — where the imports collide

Seven collisions. Each is a place where two well-supported imports, taken independently, would
produce two mechanisms doing one job.

### R1 — Three accrual clocks want to be one

**The collision.** CK's levy entitlement accrues politically; HoMM's dwelling accrues by structure;
Valoria's AP accrues per season from `facility_tier`. Take all three and a settlement carries three
independent things-that-fill-up, each with its own rate, cap and consumer.

**Why it matters more than tidiness.** The settlement layer's documented death-spiral is arithmetic:
Π's restoring term saturates at ±1, so any accrual above 1.00/season pins the ceiling, and the
design's own six ambition clocks supply up to +3.0 before a single unserved need. **Three more
accrual sources is that failure three more times.**

**Reconciled:** *one accrual primitive, several typed consumers.* A place accrues at a rate that is a
property of what is built there; what the accrual is spendable *on* is typed — governance actions,
levy capacity, facility progress. One rate, one cap, one bifurcation analysis.

### R2 — Six borrowings land on the ledger and must not each bring a field

**The collision.** Grudge-on-denial, the demotion residual, NPC memory, motion history, durable fiscal
claims and the *relazione* all want the ledger. If each lands its own field the ledger stops being a
primitive and becomes six mechanisms sharing a filename.

**Reconciled:** all six are already expressible as `(kind, key, value, ttl)` over the closed five-family
enum. **The only schema change any of them needs is `provenance`** — the Shadow of War guard — and
that one change serves all six. A Compact is a `Debt` subtype, not a sixth family; the same discipline
applies to every one of the six.

### R3 — Three "effort over time" models occupy three different time horizons

**The collision.** Victoria 3's enactment clock, an AP budget, and the Persuasion Track are all
"a thing takes work to achieve", and building them without stating their scopes produces rivals.

**Reconciled**, and the political survey already supplies the frame — three clocks *deliberately out
of phase*:

| clock | horizon | what it rations |
|---|---|---|
| **Persuasion Track** | one scene | how a single motion resolves |
| **AP budget** | one season | how many motions you can raise at all |
| **Enactment clock** | several seasons | whether a motion that *passed* takes effect |

They are complements, not alternatives. Say so before either of the unbuilt two is scheduled, or they
will be built as competitors.

### R4 — Disclosure needs one owner or it reproduces JA2's split

**The collision.** If each system decides its own disclosure policy, Valoria gets the JA2 outcome
directly: a loved half and a resented half **in the same game**, distinguished by nothing but whether
the model was visible.

**Reconciled:** disclosure is a **contract owned once** and inherited by every surface — not a
per-system choice. See U-1.

### R5 — Class-gating is blocked by a name, not by code

**The collision.** Rewriting the troop-type gates from biography to class cannot be done while
*officer* means both "mass-battle unit commander" and "political rank-holder", because the gate has to
name a class and the class vocabulary is the collided one.

**Reconciled:** the naming pass is a **precondition of an import**, not a cleanup after it. Mass battle
keeps *officer*; the political ladder takes its own word.

### R6 — Custodian/holder collides with a ratified aggregate

**The collision.** Separating who *holds* a Mandate from who *controls* the holder introduces a third
claimant on one number: `holder_id`, `custodian_id`, and LPS-1's ratified rule that faction Mandate is
a **derived aggregate** over per-settlement acceptance with no setter at all.

**Reconciled:** this one does not reconcile at the design level — **it is a ruling**, and it must be
taken before the custody import, not after. Building custody on top of a stat whose ownership is
already contested produces two unexecuted models instead of one.

### R7 — Idleness decay is Imperator's failure unless posts outnumber people

**The collision.** "Every game punishes idleness" (4/5) meets "test the down-direction against
best-case counter-investment" (Imperator). If the world has fewer posts than people — which it will —
then **some people are structurally idle**, and a flat decay is a bleed the player cannot out-invest.
That is Imperator's shipped defect exactly.

**Reconciled:** the decay rate must be a function of *available* posts, or the mechanic must target
only people who *were* posted and lost it. Either way the arithmetic check runs before the writer
lands.

---

## §9 UNIFICATION — four moves, not twenty-four imports

Each move absorbs a group of imports, resolves the collisions above, and states what it displaces.

### U-1 — The Disclosure Contract

**One rule, owned once, inherited everywhere: publish every input · show a band, never a number ·
never publish the trigger point.**

*Absorbs:* the 5/5 fuzzy-threshold convergence · JA2 v1.13's fix (which exposed the models rather than
changing them) · Shogun 2's visible band over a hidden precise value · R4.

*Displaces:* the unstated default, which in a no-GM engine means the player is told nothing.

*Cost:* **DOC.** No mechanics at all.

**Why it is first.** Valoria has no GM. Nobody narrates why a governor defected or why a motion
carried, and the survey's only direct evidence about that constraint is JA2 — where the *same game's*
social layer was loved and its tactical math resented, separated by nothing but visibility. Every
later import that shows a number inherits this contract; adopted late, each one arrives with its own
convention and the split is already in.

*Attached failure:* publishing the **trigger** as well destroys the mechanic — 5/5 lanes keep it
hidden. The contract is asymmetric on purpose.

---

### U-2 — One Accrual, One Ledger, One Budget

**Three primitives, each single-owned, each receiving several imports.**

| primitive | what it is | imports it absorbs |
|---|---|---|
| **Accrual** | a place fills up at a rate that is a property of what is built there; consumers are typed | CK's levy entitlement · HoMM's structure-driven accrual · the `facility_tier` writer · R1 |
| **Ledger** | durable memory keyed `(kind, key, value, ttl, **provenance**)` over the closed five families | Grudge-on-denial · the demotion residual · NPC memory · motion history · fiscal claims · the *relazione* · R2 |
| **Budget** | how many actions an actor may take this season — **never a modifier on a roll** | RoTK's per-officer domestic table · CK's anti-micromanagement caps · AP generalised · R3 |

*Displaces:* six bespoke memory stores; three rival accrual clocks; and — via the budget — the single
weighted `rng.random()` draw as the top-level driver of a faction's season.

*Cost:* **MOVES**, plus one schema change (`provenance`).

**The NERS constraint that makes it safe**, carried from the integration master: **the budget buys
actions, never modifiers.** One point in the Domain Action Resolver returns a flat 0.10; one added die
in the sigma engine returns roughly 0.204σ at pool 5 against 0.115σ at pool 18. A single currency
spendable in both is worth ~1.8× more on a small pool, and a player routes it wherever it pays. Buying
*actions* keeps the budget out of the resolution arithmetic entirely.

*Attached failure:* EU4 — a budget engineered not to bind is indistinguishable from no budget. Ship it
with a reachability bar and a control arm in which it is deliberately never engaged.

---

### U-3 — The person as a relationship ledger with a roster attached

**Invert how it has been built.** Part 3 §7.5's finding is that every surveyed personnel system is
primarily a relationship model *indexed* by a roster, and Valoria has authored the index and none of
the model. So the person object is defined by its edges first: who owes whom, who was passed over by
whom, who is whose client.

*Absorbs:* Old World's emitted ambitions (a person crossed with the houses around him) · Kremlin's
mortality clock · Kremlin × *piaoni*'s custodian/holder split · CK3-landless × DF × Shogun 2's
three-band demoted state · the 4/5 idleness convergence · `power_base` · R5, R6, R7.

*Displaces:* `if faction.name == 'Crown'` as faction personality. A faction's character comes from
who leads it, which is also what makes the two branchless factions distinguishable.

*Cost:* **RULING** (the schema, and the custody question in R6), then **MOVES**.

*Preconditions, both non-negotiable:* the **naming pass** (R5 — a `roles` field cannot be typed while
three words each mean two or three things), and the **NPE's own RNG substream**, without which the
loader's golden movement is unattributable.

*Attached failure:* CK3's ambient population — 24,000-character saves and two community mods pulling
in opposite directions. **Generate on demand, not on a clock**; load the 46 authored rows and build no
spawner. And Imperator on the idleness half, per R7.

---

### U-4 — Couple the scales, or stop claiming the differentiator

**The honest one.** Valoria's doctrine defines its Ω-clause *against* Mount & Blade's faction politics
versus character combat as the paradigm of mechanically isolated layers — and Part 3 §7.8 finds
Valoria currently sitting where M&B sits: one reachable handoff, one evaluable trigger, a bridge that
is default-OFF with no producer, and both leverage failure poles live in the same sixteen lines.

**There are two defensible options and Valoria is taking a third that has no precedent behind it.**

1. **Ship an explicit, imperfect crossing.** Every surveyed game either has no such seam or ships one
   it knows is imperfect. Concretely: close the accord echo (which needs a §5.5 outcome
   classification *and* a faction→settlement targeting rule — two rulings, not one field), and give
   the combat bridge a producer.
2. **Say the layers are adjacent rather than coupled**, and revise the doctrine that claims otherwise.

*Displaces:* the current third option — a flag whose off-state is indistinguishable from the seam not
existing.

*Cost:* **RULING**, then MOVES.

*Attached failure, and it is the hardest in the corpus:* **D3.** No precedent makes a personal actor's
contribution leverage-in-band from N=1 to N=1000+, and the two failure poles are *already coded* in
Valoria, sixteen lines apart, unreachable. **The guard belongs before the producer**, not after: a
personal→unit effect must be a fraction of the unit's own size or cohesion, never a flat amount.

---

## §10 THE MOVES AGAINST THE MASTER'S PROPOSALS

The integration master proposes four ways to organise Valoria. The four unified moves above are not a
fifth proposal — they are what the precedent contributes to each.

| Master proposal | What U-1…U-4 add | What the precedent warns |
|---|---|---|
| **P1 — Close the Circuits** | **U-1 is a free prerequisite** for P1 being *felt* rather than merely computed — eleven writers that the player cannot see the reasons behind are eleven invisible writers. And the master's "give the motion a subject" and the Football Manager import are **the same edit**, reached from code and from precedent independently | Imperator: each writer tested against best-case counter-investment before it lands. The grudge counter needs decay, from both directions |
| **P2 — Three Primitives** | **U-2 *is* P2**, reached from precedent instead of from code — and it corroborates the primitive choice from six independent borrowings on the ledger alone. It also supplies the accrual primitive P2 does not name, which is what gives `facility_tier` a writer | EU4's reachability bar; and the budget-buys-actions restriction, which both documents arrived at separately |
| **P3 — The Disposal** | Total War's twenty-year governor oscillation is the strongest available argument that **not every designed surface needs finishing**; Compton's rule attaches — *not everyone can be a main character* | The 2026-07-08 application of the same disposition method to 97 actions produced **zero top-level CUTs**. And the survey's null cuts both ways: with no convergent answer on the governor role, cutting Valoria's is as unsupported as finishing it |
| **P4 — A Person's Season** | **U-3 is P4's substrate**, and P4 is the best-precedented of the four — Old World, Kremlin, CK3-landless and the idleness convergence all presuppose exactly this shape | **U-4 is the warning P4 does not carry.** Building the person layer does not by itself couple the scales. M&B has both layers and is the corpus's own definition of isolation |

---

## §11 THE IMPORT REGISTER

The unified moves above are the proposal. This register is the mapping underneath them — every
candidate import, its source, its destination, its cost class, and **what it displaces**. It exists so
that a later session can check a claim rather than re-derive it.

Cost classes are the personnel master's, reused rather than re-coined: **DOC** (an edit) · **INERT**
(lands default-off, goldens byte-identical by construction) · **MOVES** (goldens shift; needs a re-pin
plus a `balance_oracle.py` control) · **RULING** (a decision, not a commit).

### §11.1 TIER 1 — imports that need no new object

These land on primitives Valoria already has. They are the cheapest real changes available and,
between them, they are most of the value in this document.

| # | Import | From | Into | Cost | **Displaces** | Attached failure |
|---|---|---|---|---|---|---|
| **I-1** | **Publish every input · publish a band, not a number · never publish the trigger point** | JA2 v1.13 (exposed the models rather than changing them) · Shogun 2's visible band over a hidden value · the 5/5 threshold convergence | A presentation rule binding every surface that will ever show the player a reason | **DOC** | The unstated default, which in a no-GM engine is "the player is told nothing" | JA2 itself: the *same game*'s tactical math was resented where it was opaque, while its social layer was loved |
| **I-2** | **Recorded defeat** — a motion carried and vetoed persists with no force and full citability | Roman *senatus auctoritas*; *"very few games have this and it is nearly free"* | `systems/social_contest/sim/parliamentary_vote.py`, as a Record with `status=vetoed` | **MOVES** (small) | Nothing. It is additive by construction — it converts a discarded outcome into an object | None found; it survived the survey's own adversarial attack |
| **I-3** | **Give the vote a specific slate event to resolve** | Football Manager (every fixture is specific, three fidelities of one engine) | `engine/cross_scale/parliamentary_bridge.py::_derive_vote` | **MOVES** | The generic per-season roll — `motion_id = f"parl_s{season}"` with no subject | Total War: a fast path that is a *different algorithm* diverges and gets exploited both ways. Keep one engine, several entry points |
| **I-4** | **A Grudge tag written the moment a figure is passed over or demoted** | CK's council-seat denial (−40 opinion), scaled down | The appointment flow, via `systems/settlements/sim/ledger.py::ledger_add` | **MOVES** | `select_censure_target`'s "highest Legitimacy", whose own docstring says it is a placeholder *because no relationship signal exists* | Shadow of War: the tag needs **provenance bound to the causing event**, or a convenience path can forge the relationship. And a counter with no decay is an unbounded ramp |
| **I-5** | **Scaled compromise** — the winner concedes in proportion to what winning cost | Burning Wheel *Duel of Wits*, in print since 2002 | `systems/social_contest/sim/contest/resolver.py` | **MOVES** | Clean win/lose at the scene scale | The documented complaints about that system concern **manoeuvre balance, never the compromise rule** |
| **I-6** | **Pre-roll gap detector** — past a declared pool ratio, fast-path to a single opposed resolution | *Duel of Wits* collapsing to "the bigger number wins fast" at 21-vs-11 | The same resolver | **MOVES** | The staged path running in a band where it changes nothing | Assert the staged path moves the outcome distribution by more than a stated tolerance *in the band where it runs* — if not, the apparatus is decorative there |
| **I-7** | **Band-probability floor** — a checked-in test computing all four band probabilities across the practical pool range | Blades in the Dark's P(fail) falling 50% → 1.6% from N=1 to N=6, no floor | `tests/valoria/`, against `dice_engine.degree_from_net` | **DOC** (a test) | Nothing; it is a guard | The Partial band collapses monotonically because its window is a fixed one-success width over a spread growing as √N. **No obstacle derivation cures that** — only a band width that scales with the pool |
| **I-8** | **Investigation output caps a contest's ceiling** | Triangle Strategy's pre-vote intelligence gate, softened | `dice_engine.BandExtension` — declares a named policy whose only power is `may_overwhelm` | **MOVES** | The current state, in which the investigation and contest lanes do not touch at all | TS's own hard *"wrong appeal = flat fail"* is scripting drift. Take the veto-an-Overwhelming form only |
| **I-9** | **Gate troop types on officer CLASS, not biography** | Total War: Three Kingdoms (Strategists unlock ranged and siege) | `faction_politics_v30.md §1.5`'s two existing gates | **DOC** now, MOVES after the person exists | *"a named officer with Cavalry History"* — biography-gating | Gate on a class and losing a person means promoting another; gate on biography and losing one person costs you cavalry **permanently** |
| **I-10** | **Two-tier defeat severity** — a commander's loss destroys the retinue only if the whole army also routs | Total War: Three Kingdoms | Mass-battle outcome handling | **MOVES** | The current unconditional "a destroyed unit loses all Experience permanently", Valoria's harshest rule | None found; it softens a rule in a principled direction |

**Why these ten and not others.** Every one lands on a module that exists and runs, or on a test file.
None requires the person object, the unit object, or a ruling. **I-1 is free and is the highest-value
row in the document** — it is the only surveyed answer to the legibility-versus-depth problem (D2)
that no shipped title in the genre has solved, and in a no-GM engine it is a constraint rather than a
preference.

---
### §11.2 TIER 2 — imports blocked on one of two shared objects

These are not individually expensive. They are blocked on the same two missing objects, which is why
the objects — not the imports — are what get scheduled.

### Blocked on **the person**

| # | Import | From | Into | **Displaces** | Attached failure |
|---|---|---|---|---|---|
| **I-11** | **Ambitions emitted from a person crossed with the houses around him, expiring on death** | Old World; Kremlin supplies the mortality clock (K6) | Faction action selection | The `if faction.name == 'Crown'` personality branch — **swap two factions' names in the starting table today and the campaign is unchanged** | None found. It answers "what does this character want" generatively and at no authoring cost |
| **I-12** | **Idleness costs something** | 4/5 lanes (JA2 docks morale *and* town loyalty after three days; TK's "give them something to do"; CK's 2%/month) | A person state that degrades under neglect | An unassigned person being **inert rather than restless** | Imperator: test the down-direction against the **best-case** counter-investment. If the fastest mitigation still nets negative, the mechanic is broken, not hard |
| **I-13** | **Custodian separable from holder** — controlling a Mandate-bearing figure without deposing them | Kremlin (influence over politicians, never ownership) × Ming *piaoni* (K3); already named in the roster research as the sharpest architectural gap | `custodian_id` distinct from `holder_id` | Deposition as **the only** way to control a Mandate-bearer | None found. It is the X1 convergence — five independent systems — landing on a gap Valoria's own research already named |
| **I-14** | **The three-band demoted state**, carrying tags forward | CK3's landless track × DF's consequence-free demotion × Shogun 2's bands (K1) | `succeed_governor`, which already sweeps the ledger and lets durable tags survive — **and has zero callers** | Demotion as a debuff. *"A demoted officer that merely loses bonuses is a subtraction, and subtractions are not play"* | Both poles at once: CK3 says it must be its own game; DF says a comeback that resets to zero is a reset button |
| **I-15** | **Drafting right** — the clerk who drafts outranks the minister who signs | Ming *piaoni* | The motion pipeline, once seats are held by people | Nothing. It is the best available answer to *"why would a player care about a clerkship"* | None found; models bureaucratic power with **no power stat** |

### Blocked on **the unit record**

Valoria has none: `Faction` has no unit list, `Territory` has only a `garrison` boolean, and Muster
writes `faction.Mil` directly. **Price the schema once, not the three mechanics.**

| # | Import | From | Into | **Displaces** | Attached failure |
|---|---|---|---|---|---|
| **I-16** | **Garrison as an assignment on existing units** | 4/4 convergence — JA2 · Brigandine · Unicorn Overlord · Total War | `Territory.garrison`, a boolean written once and read once | A garrison **troop type**, which none of the four built | Open fork: JA2's garrison units *can* move offensively, and it is a major feature. Decide |
| **I-17** | **Levy and professional as different economies** | 4/4 — CK (levies cost **zero** gold, rationed politically and temporally; men-at-arms cost gold + prestige + maintenance *while unraised*, tripling when fielded) · Shogun 2 as a starting-stat delta · JA2 pricing the bought channel strictly worse on economics | `_try_muster` | One Muster — **already the professional model wearing a generic label**, since ED-FA-0009's grounding is Wallenstein, a contractor paid regardless | Splitting a ratified action is a canon change. Valoria's own Templar exception is the precedent that it can be done once; the question is whether one is the right number |
| **I-18** | **Proximity-at-rout** — what survives is what was near the commander when he withdrew | Brigandine (*"the commander is a reusable chassis; the army under him is the consumable"*) | Mass-battle rout handling, which already models cells, facing and Discipline | An unconditional loss rule | None found; Valoria already has the chassis half (officers incapacitated or captured, never killed) |

---
### §11.3 TIER 3 — imports that need a ruling first

| # | Import | From | The ruling it needs | **Displaces** |
|---|---|---|---|---|
| **I-19** | **The enactment clock** — a measure is a multi-stage process with running success, discrete setbacks, a failure state with cooldown, and **an opposition that grows because you attempted it** | Victoria 3 | Whether Parliament becomes an entity with state. Five ongoing Sanction statuses, two durable constructive-motion outcomes, seat tenure and an agenda have **no field anywhere** | A passed motion taking effect instantly. ⚠ **V3's parameters do not transfer** — the 100-day stage and class multipliers are tuned for 1836–1936 nation-states. The structure transfers; the tuning does not, and only the structure was researched |
| **I-20** | **Shared loss** — the polity itself can fail and everyone loses | The Republic of Rome | Whether Valoria has a campaign-terminal failure state at all. The designed Second Calamity is contract-declared with zero code | Obstruction having no ceiling. ⚠ In single-player this disciplines **AI factions**, so its cost is an AI problem, not a rules problem — harder than the survey acknowledged |
| **I-21** | **The Charter of Submission** — conquest produces a negotiation, not a colour change | Venice's *dedizione* (subject cities kept statutes, exemptions, guild privileges and councils in exchange for loyalty and appellate supremacy) | How much the Entry Terms fork should carry. It already exists and is **the only authored rule anywhere that seeds settlement Legitimacy** | Ownership transferring immediately on conquest, skipping the designed three-season Occupation phase entirely |
| **I-22** | **Accrual as a property of a built structure in a place** | Heroes of Might and Magic (**not surveyed** — see Part 1 §2.13) | Whether this double-counts against CK's entitlement model (I-17). It is the shape that would give `facility_tier` — an authored progression axis **nothing ever raises** — a writer | `facility_tier` sitting at 0 on all 37 settlements forever, flattening the whole progression axis |
| **I-23** | **Ship an explicit, imperfect crossing rather than a default-off flag** | The null: **no surveyed precedent defends a bridge whose default state is indistinguishable from its absence.** Every game either has no such seam or ships an imperfect one | Which of the two to ship. `DISPATCH_COMBAT_BRIDGE` is default OFF and has no producer even when ON — dead twice over | The current third option, which has no precedent behind it |
| **I-24** | **Consent priced per muster, with a revolt-adjacent floor** | JA2's Kerberus charge (0.1/regular, 0.15/veteran, **globally** not to the receiving sector) × RoTK VIII's order gates (K9) | Scope, so the two do not double-count. *"A population in open revolt will not hand you soldiers"* is a different claim from *"you govern badly here"* | Muster costing only Wealth — and costing **0.01 Wealth** at that, per the master's defect finding |

---
### §11.4 The refusals, bound to the module that would otherwise drift

A refusal is only useful attached to the place the drift would happen.

| Refuse | Why | Bound to |
|---|---|---|
| **CK3's ambient population model** | 6–7 parentless sixteen-year-olds monthly, 24,000-character late saves, two community mods pulling in **opposite** directions, Paradox's own fix throttling the low-value tail. **Generate on demand, not on a clock** | The NPC loader. Load the 46 authored rows; do not build a spawner |
| **A second resolver of any kind** | Dominions and Mount & Blade achieve consistency by never offering one. Total War is the only precedent with two paths and the only one with a twenty-year unsolved divergence | `massbattle.py:37-50`'s survivor-ratio degree map, which **says in its own comment** that it is not the canonical ladder. Reconcile it or register it — self-disclosure is doing the work of a guard and none of the work of a fix |
| **Contradiction-matching as a primary political resolution** | One correct pair per round; excellent tension, **zero political modelling** — and in a political trial the winner is often the side whose evidence is worse | Any fieldwork→contest bridge. Keep *inventory-as-argument* and drop the rest |
| **Manoeuvre sets differentiated by damage output** | Players found the two highest-damage verbs and stopped; Rebuttal went unused because too much beat it | The contest resolver's manoeuvre set, if one is ever authored. Manoeuvres must differ in **what they change about the state of the argument** |
| **Relationship modifiers large enough to dissolve structural conflict** | CK3: opinion bonuses paper over structural factors, so *"you can generally succeed at things kings wanted to do but were unable to pull off"* | The grudge/disposition scale, whatever it becomes. **Some conflicts must be positional and unbuyable** |
| **Three Kingdoms' "Administrator" as vocabulary** | Solves the wrong half. *Governor* is canonical, in code, and carries residence semantics TK's Administrator lacks | The naming pass. The overloaded word is **officer** |
| **A scheduled recovery tick** to fix a one-directional ladder | Promotion and demotion should be caused by **specific events, never scheduled**. A timer that restores Standing on a cadence converts a consequence system into a treadmill — the Imperator failure with the sign flipped | Any fix for Coherence's or Standing's missing up-direction |
| **"We have the Key substrate" as "we have emergent narrative"** | The one sentence the dossier asks be carried verbatim. Physics has graphics; **nothing equivalent exists for mood, grudge, loyalty or ambition**, and every mechanism that "solves" it narrows scope instead | Any milestone claiming emergent narrative. Budget **expression** as a line item in the same milestone as the substrate |

---
