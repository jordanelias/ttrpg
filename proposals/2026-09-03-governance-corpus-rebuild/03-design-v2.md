# Valoria — The Governance Design, v2

**A rewrite of the v1 design after critique, against precedent, disciplined by its own principles.**

---

## What this is

v1 took 33 design documents and rebuilt them as a single coherent model: one owner per quantity, pure
derivation, one outcome type, one cross-scale carrier, a deterministic twelve-phase season. That
architecture was sound as **bookkeeping** and wrong as a **game**, in three specific ways:

1. **It could not run away.** ≈245 damping devices (clamp, cap, floor, saturating, mean-reverting) and
   **zero** amplifying ones. Every loop negative, every quantity bounded. A system like that
   converges — season 40 resembles season 30 — and the corpus wanted otherwise: it uses *escalat\**
   24 times and names two "anti-death-spiral floors", which you do not write unless you believe a
   spiral is reachable.
2. **It dropped two of the corpus's five territorial tiers.** `duchy` appears 5 times in v1 against
   48 in the corpus; **`sub-feature` appears zero times** against 16. Factions ended up as pointers
   floating free of the map, and every settlement of a type became mechanically identical.
3. **It had no object for what this game's politics is about.** Zero occurrences of `title`, one of
   `casus belli` — while the corpus builds six separate mechanisms (Casus Belli, the Crown Claim,
   succession, parliamentary transfer, insurgency promotion, ecclesiastical appointment) that are all
   one thing: **a claim on a title, prosecuted by one of several routes.**

Three of v1's headline slogans were also false, two of them contradicted by its own annex. They are
corrected here and the corrections are shown rather than quietly applied.

## What v2 changes

| | v1 | v2 |
|---|---|---|
| **Tiers** | 3 (settlement · province · peninsula) | **5** (realm · duchy · province · settlement · holding), with de jure and de facto separated |
| **Territory model** | a `controller` pointer | **titles**, each with a de jure parent, a de facto holder, a **liege** and a **vassal contract** |
| **Authority** | issued by whoever holds the province seat — which in a fractured province commands a *rival's* governor | routed along the **liege chain of the settlement's own holder** |
| **Acceptance** | Legitimacy and Popular Support both stored per settlement; polity events smeared "uniformly" across holdings | **split by grain** — `Legitimacy` at the polity, `PS` at the settlement. A coronation is one write, not twelve |
| **Mandate** | one derivation for every polity | **per-status** — territorial, presence-based, or embedded. The Church stops deriving its power from one settlement |
| **Political substance** | none | **claims** — persistent, accumulable, transferable, sometimes secret |
| **Settlement variety** | a `type` enum and a tier integer | **holdings conferring capabilities**; rules gate on capability, never on name |
| **Local politics** | NPC dispositions | **interest groups with approval and derived demands**; revolt is a coalition, not a die roll |
| **NPC ambitions** | advance privately, then fire | **schemes** with secrecy, joinable agents, and discovery as a resolution |
| **Does territory buy power?** | no — 8 provinces ≈ 3 provinces in army cap, votes and Mandate | **yes** — force limit, votes and income scale with holdings, and the cost of holding scales faster |
| **Loops** | ~245 damping, 0 amplifying | **6 negative · 3 positive regimes · 1 world-scale pressure controller · 2 scaling penalties · 5 ratchets**, all named and signed |
| **Anti-snowball** | none | **administrative strain** + the corpus's own unused GD-2 coalition trigger |
| **World pressure** | two peninsula clocks *decay when the map is quiet* — quiet begets quiet | **Π_world**, the settlement homeostat raised one tier and symmetric across all polities |
| **Feedback sign** | a settlement governed above its realm's average loses support until it sinks back | regression toward the realm's **legitimacy**, not its mean — the floor is kept, the ceiling dropped |
| **Content dependencies** | proper nouns in predicates | **roles, capabilities and relations only** — a grep-checkable rule |
| **Effect chaining** | "effects never fire effects" (false) | **generations** for depth, with a provable bound — *and* the corpus's fan-out budget kept, which v1 retired on a misreading of what it capped |
| **Derived state** | rebuilt twice a tick, so late-phase writes leave it stale | rebuilt after **every** commit point |
| **Simultaneity** | order-dependent and unspecified | **snapshot-then-apply**; mutual destruction reachable |
| **Explanation** | engine-facing determinism only | **preview and provenance** — the obligation a no-GM engine inherits |

## Method

1. **Critique** of v1 along six axes — hierarchical shape, ownership, nesting, dependencies, state
   changes, emergence — measured rather than asserted wherever a measurement was available, and run
   in parallel by an independent critic that never saw how v1 was produced.
2. **Precedent**, asking of each acclaimed game not "what is it like" but **what object exists in it
   that does not exist here, and what work does that object do**: Crusader Kings III (the title),
   Victoria 3 (the market's single ownership; radicalism), EU4 (estates as component-and-peer;
   orthogonal partitions), Democracy 4 (the simulation *is* a signed weighted graph), Shadow Empire
   (administrative strain), KOEI *Romance of the Three Kingdoms* (the officer roster), Frostpunk (the
   law ratchet), Into the Breach (total previewed resolution).
3. **Principles**, extracted from the design rather than imposed on it, each stated so it can be
   **failed** — with what it forbids and how to check mechanically that nothing forbidden is present.
4. **Audit** of the design against those principles. It found **seven violations, all in the design** —
   each a place where a general rule was stated and a shortcut taken for a specific case one or two
   sections later.
5. **An independent critic**, working from the same design and corpus with no sight of how either was
   produced, which found **nine more** — three of them behavioural bugs rather than statements,
   including one that routes a fractured province's orders to a rival's governor, and one where the
   self-audit had recorded a defect as a virtue.

All sixteen are corrected in the text that follows. The audit is retained at the end because the
*difference* between what the two methods found is the most useful result: **principles catch
contradiction; only tracing the mechanics catches error.** A design that is internally consistent and
does the wrong thing passes every test it can write about itself.

**[SELF-AUTHORED — bias risk.]** This critiques my own prior work. The failures I am least likely to
see are the ones following from what I optimised for, which was a *clean* model. Every finding of the
form "it is too clean" is therefore the one to trust least from me — which is why the largest is
stated as a count of words in my own document rather than as a judgement.

## Read this first if you read nothing else

Valoria is one idea — **authority is never held, only accepted, and is contested from above and below
at once** — instantiated at three scales that share no primitive. v1 unified the instantiation. v2
does three further things:

- gives the idea a **legal dimension** (de jure) distinct from its **control dimension** (de facto),
  so that legitimacy is a thing you can hold without power and power a thing you can hold without
  legitimacy — which is the entire subject matter;
- gives it **an object to fight over** that outlives any particular fight (the claim);
- and gives it **three ways to catch fire**, because a political simulation in which nothing
  compounds is a ledger with weather.

---

# Part 0 — The organizing principles

> These come first because everything after them is constrained by them. Each is stated so it
> can be **failed**, and the Audit at the end records the sixteen places where the design failed one
> and was changed.

A principle is only load-bearing if it can be **failed**. Every one below therefore states what it
forbids and how to check, mechanically, that nothing forbidden is present.

---

## TL-1 · Two facts, never one: **de jure** and **de facto**

**Statement.** Every territorial assertion is either a statement of *right* (de jure — slow, legal,
what a title means) or a statement of *control* (de facto — fast, contested, who is obeyed). No
quantity may conflate them, and every territorial quantity must declare which it is.

**Forbids.** A single `controller` field. A "province is fractured" boolean. Any rule that reads
ownership without saying which kind.

**Test.** Enumerate every territorial field. Each is tagged `dejure`, `defacto`, or `civic` (state of
the place itself, belonging to neither — Order, Prosperity, Π). **A field that cannot be tagged is
mis-modelled.**

**Rigour it exacts.** Fracture, secession, vacancy, occupation, promotion and legitimation stop being
six mechanics and become six readings of one gap. Victory becomes definable rather than countable.

## TL-2 · One owner per quantity; derived quantities have no writers

**Statement.** Each quantity has exactly one owning tier and one write path. If it is derived, nothing
writes it — writers write its inputs.

**Forbids.** "One writable tier" (the v1 slogan, which was false). Any second write path. Any stored
copy of a derived value.

**Test.** For every quantity, one owner row and one writer. For every derived quantity, a grep that
returns **zero** assignments. Accord and Mandate are the standing regression cases: the corpus wrote
each in nine and six places respectively while defining both as derivations.

**Rigour it exacts.** Save/replay is persist-the-owned, recompute-the-rest. Ordering bugs become
impossible to express rather than merely rare.

## TL-3 · One outcome type: `Degree`

**Statement.** Every resolution at every scale emits `Failure | Partial | Success | Overwhelming`.
The generator — margin resolver for structural checks, dice pools where variance is healthy — is
private to the scale that uses it.

**Forbids.** A consumer that branches on *how* an outcome was produced. A second outcome vocabulary.

**Test.** Every consequence table is keyed by `Degree` and by nothing else.

**Rigour it exacts.** The resolution method can change per scale without touching a single consumer —
which is what let the corpus migrate a third of its actions to a new resolver without rewriting the
consequence tables, and the reason the remaining two thirds are mechanical rather than a redesign.

## TL-4 · One cross-scale carrier: `Echo`

**Statement.** Nothing reaches from one scale to another except an Echo: a magnitude derived from a
Degree, gated by scope, clamped, targeted at a **scale**, applied at a commit.

**Forbids.** A subsystem reading another scale's state to modify it. A direct write across tiers.

**Test.** No write in the codebase targets a scale other than its own. Adding a tier requires adding a
link, not editing emitters — the corpus demonstrated this when the settlement tier was inserted and
the mechanism absorbed it unchanged.

## TL-5 · Roles, not identities

**Statement.** Every predicate, trigger, weight and condition references a **role, capability or
relation**. Never a proper noun.

**Forbids.** `has_subnational(RM)`. `Suppress(RM|Church)`. "the Church gets ⌊CI/20⌋". "Crown runs a
fragmentation check."

**Test.** **Grep the content layer for proper nouns.** Every hit is either a scenario declaration
(legitimate, and lives in the scenario file) or a defect. There is no third case.

**Rigour it exacts.** This game manufactures new factions at runtime. A rule naming the Church cannot
apply to an insurgency promoted in season 30, so every proper noun in a mechanic is a promise the
promotion machinery cannot keep.

## TL-6 · Uniform limits, uniformly suspended

**Statement.** Caps and bounds apply identically to every entity of a kind. Where a limit is
suspended, **the suspension is itself a uniform rule** attached to a named regime — never an exception
carved for one entity.

**Forbids.** "The cap is uniform, except for X." A per-faction ceiling. A bespoke bonus.

**Test.** Every cap has one value and one suspension rule. The corpus's own defence is the model:
faced with an argument for exempting its keystone territory it ruled "**the cap is uniform. No T9
bypass**", rejecting two proposals to special-case it.

## TL-7 · Every loop is named and signed

**Statement.** Every feedback loop in the design appears in the instability budget with a direction.
Negative loops keep the game playable; a small fixed number of positive regimes make it worth playing;
entry is legible and rare, exit is expensive and possible.

**Forbids.** An unlisted loop. A design in which nothing can run away. A runaway with no exit.

**Test.** Trace every quantity's inputs; every cycle found must appear in the budget. The v1 count —
≈245 damping devices, zero amplifying — is the failing case this principle exists to prevent.

## TL-8 · Effects commit in generations

**Statement.** Effects queued at phase entry commit together. Effects *produced* by that commit form
the next generation and commit at the start of the next phase owning their target scale. **A
generation never commits in the phase that produced it.**

**Forbids.** Inline application. An arbitrary depth cap. The claim that chaining does not occur.

**Test.** Chain depth is bounded by remaining phases and strictly decreasing — provable, not tuned.

## TL-9 · Simultaneity is snapshot-then-apply

**Statement.** Everything resolving simultaneously reads one immutable snapshot taken at phase entry
and writes only to the queue. Nothing in a simultaneous set observes another's result.

**Forbids.** Reading back a result inside the phase that produced it. A sort order that decides
outcomes.

**Test.** Permuting a simultaneous set changes nothing. **Mutual destruction must be reachable** — if
two armies cannot destroy each other, the set is being resolved sequentially somewhere.

## TL-10 · Rules gate on capabilities, never on kinds

**Statement.** What a place can do follows from what is built there. A rule tests
`has_capability(sea_route)`, never `type == Port`.

**Forbids.** Enum-keyed affordances. Hand-placed special locations.

**Test.** Every affordance traces to a holding. **The five starting friction points must be derived,
not authored** — a friction point is a settlement whose holdings confer capabilities on an
institution that does not hold it, and any settlement acquiring that shape becomes one.

## TL-11 · Claims are the durable political substance

**Statement.** Every assertion of right over a title is a `Claim`: persistent, accumulable,
transferable, and sometimes secret. War, votes, appointments, marriages, purchases and uprisings are
*prosecution routes*, selected by the claim's basis.

**Forbids.** A bespoke eligibility rule per mechanic. Casus Belli as a token divorced from what it is
a claim *to*.

**Test.** Every mechanic that transfers a title consumes a claim. Six corpus mechanics — CB, the
Crown Claim, succession, parliamentary transfer, insurgency promotion, ecclesiastical appointment —
must reduce to route selection over one object.

## TL-12 · The ratchets are enumerated

**Statement.** A fixed, listed set of things never move backward. Everything else is recoverable.

**Forbids.** An unlisted irreversibility. "Permanent" as an adjective in a consequence table.

**Test.** Every `irreversible` flag in every pipeline appears in the ratchet list. The list is short
enough to read.

## TL-13 · The engine owes an explanation

**Statement.** There is no referee, so the engine inherits the referee's second job. Before the player
commits, the full consequence chain is shown; after anything happens, the derivation path is
inspectable.

**Forbids.** A quantity that changes with no traceable cause. Hidden *arithmetic*.

**Test.** Every state change carries its provenance. Hidden actors are hidden in their **existence**
— "Order −1 from an unknown source" — never in their **arithmetic**.

**Rigour it exacts.** This is the principle that makes the clock layer a data graph rather than code:
you cannot explain what you cannot inspect.

---

# Part I — The shape

## The five tiers, restored

v1 modelled three scales. The corpus specifies five, and the two v1 dropped were carrying the
political content.

```
  REALM        Kingdom of Valoria            one, held by the monarch
    │                                        (+ foreign realms: Altonia, of which Schoenland is a part)
  DUCHY        Valorsmark · Hafenmark · Varfell        three, held by Dukes
    │          (+ Himmelenger: a duchy-tier title held by the Church, with one province)
  PROVINCE     14 in the duchy structure + 3 outside   the contest tier
    │
  SETTLEMENT   37                            the engine tier — the siege target
    │
  HOLDING      districts · harbours · mines · barracks · cathedrals · watchtowers · lodges
               not separately siegeable; taken with the parent
```

**Two facts attach to every territorial unit, and keeping them apart is the whole of the shape:**

- **de jure** — which parent it *belongs to*. Slow, legal, and the thing a title *means*.
- **de facto** — who is *obeyed* there. Fast, contested, and the thing an army changes.

A province is de jure in exactly one duchy, always. It is de facto controlled by whoever holds its
settlements. **Fracture is the gap between the two**; consolidation is closing it; the corpus's
"unification bonus" is the reward for closing it; a Casus Belli is a licence to close it by force.

This single distinction does work v1 needed five separate mechanisms for:

| corpus problem | v1 | v2 |
|---|---|---|
| Two incompatible fracture models (Greater/Lesser by PV share; geographic north/south with auto-merge) | punted to open questions | one model: de facto divergence from de jure. No sub-province naming needed — the province is de jure whole and de facto split |
| Himmelenger, Askeheim, Schoenland are three unexplained exceptions | three data rows | one rule each: Himmelenger is a **duchy-tier title held by a non-dynastic holder**; Askeheim has **no de jure parent** (unincorporated); Schoenland is **de jure in a foreign realm** |
| The Löwenritter arc | a bespoke four-state ladder | **a holder with de facto control and no title.** The ladder falls out of the gap widening |
| Insurgency → Promoted Faction | a bespoke pipeline terminus | **de facto control acquiring de jure standing.** Promotion *is* being granted or seizing a title |
| Province "becomes Uncontrolled" | a status enum | de facto holder = ∅ while de jure parent persists — which is why the title survives to be reclaimed |

**Why the duchy tier specifically.** Almud is simultaneously monarch of Valoria and Duke of
Valorsmark; Baralta holds Hafenmark; Vaynard holds Varfell. **The three secular factions are
duchies.** Without the tier, a faction is a floating pointer that appears on settlements, and there is
no structural difference between losing a province at your core and one at your edge, no seat to take,
no vassalage to grant or revoke, and no way to express the Kingdom's authority over the Dukes except
by writing it into each rule that needs it.

With the tier, one relation — *X holds a title whose de jure parent is held by Y* — expresses
vassalage, the monarch's overlordship, the Church's anomalous standing, and the Löwenritter's
grievance, and it is the same relation every time.

## Titles

A **title** is the object that a faction actually holds. Territory is what a title *contains*.

```
Title {
  id
  tier          : realm | duchy | province | settlement
  de_jure_parent: TitleId | ∅            -- ∅ only for a realm, or for unincorporated land
  holder        : PolityId | CharacterId | ∅
  liege         : TitleId | ∅            -- whose authority this holder answers to
  contract      : { levy, tax, obligations, autonomy }   -- what the liege may demand
  seat          : SettlementId | ∅
  contested_since, held_since : season
  created_by    : founding | grant | usurpation | partition | recognition
}
```

**`liege` and `contract` are the pair that make the tier do work**, and without them the tier is
decoration. The liege pointer is *not* the de jure parent: a title's de jure parent says where it
belongs; its liege says whom its holder obeys. Usually they agree. **The interesting states are
exactly where they do not**, and the corpus's central conflicts all live there.

### The authority rule — and the bug it fixes

> **Authority runs along the liege chain of the holder, never along the container.** A settlement's
> Directive comes from the liege of *its own holder's* title, not from whoever holds the province seat.

This is not a refinement; it repairs a live defect. The v1 model computed
`Provincial Authority = controller(province.seat)` and issued a Directive from it to **every**
settlement in the province. In a fractured province — the design's own central runtime case — that
means the seat-holder issues orders to a **rival's** governor, and that governor accrues suspicion
toward, and is recalled by, a faction they do not serve. The corpus is explicit that this is wrong:

> "Non-Seat-holders issue only settlement-level actions within settlements they hold."
> — `fractional_province_ownership_v30.md §2.5`

The same conflation produced a second defect: a revolt rule computing `Accord(p) = 0 → holder := ∅
for every member` over *all* members, so one faction's two ruined settlements strip a rival's
well-governed one. **Both are the same mistake — treating the geographic container as the chain of
command** — and both disappear once authority is a property of the title chain.

### The vassal's response is the settlement's response, one tier up

A duchy holder facing a demand from the realm has the same three options a governor has facing a
Directive: **comply · bargain · defy**, with the same suspicion accrual and the same escalation to
recall — which at this tier is a summons, and past a threshold, a revocation attempt.

This is the design's own thesis finally applied at the tier it was missing from. v1 claimed one
acceptance primitive instantiated at three scales, and the province instance had **no upper jaw** —
its "pressure from above" was a fragmentation check it rolled against itself. With titles, the
province's upper jaw is its liege, and the primitive is genuinely one mechanism at every tier.

Four consequences, each of which removes a special case from v1:

1. **A realm is a title, so a foreign power is not a special case — and the peninsula gets its upper
   jaw too.** Altonia is a realm; Schoenland is a province de jure within it. The Altonian invasion is
   a foreign realm prosecuting claims on Valorian provinces with the same machinery as everyone else,
   and "Invasion Pressure" becomes the readable state of that campaign rather than an unexplained
   global counter. v1 said the peninsula's tier above was "nothing"; it is Altonia, and the Vanguard
   advance — which ratchets while uncontested — is the one externally-driven escalation the design
   already had and did not recognise as one.
2. **The Church holds a duchy-tier title with one province.** That is precisely its historical
   anomaly — sovereign, small, and ranked alongside dukes — and it explains why Church expansion is
   *appointment* rather than conquest: it acquires settlement-tier titles by granting offices, not by
   marching.
3. **A settlement is a title too**, which is what makes Bishop Appointment, governorship and secession
   the same kind of event: a settlement-tier title changing holder by three different routes.
4. **Askeheim has no de jure parent and therefore cannot be won.** The corpus asserts this as a flat
   exception ("cannot be controlled by any faction"); here it is a consequence. And the healing path
   the corpus leaves open becomes a legible act: **incorporation** — creating a de jure parent for
   land that had none.

## What this does to victory

v1 reconciled the corpus's four incompatible victory statements into "11 of 15 provinces, sustained
2 seasons, fractional shares counting". That reconciliation survives, but the tier structure makes it
say something rather than count something:

> **Peninsular Sovereignty** = holding, de facto, the settlements that constitute a majority of the
> Kingdom's de jure provinces — 11 of the 15 that have a de jure parent inside the Kingdom — for two
> consecutive seasons.

The denominator stops being an unexplained constant. **15 = the 14 duchy provinces + Himmelenger**;
Askeheim is excluded because it has no de jure parent and Schoenland because its de jure parent is a
foreign realm. v1 derived this and had to state it as a reconstruction. In v2 it is the definition.

And it admits the game's most interesting end state, which v1 could not express: a faction can hold
eleven provinces **de facto** while another holds the Kingdom title **de jure**. That is not a bug to
be tie-broken — it is the Investiture Controversy, which is what this game is about, and it should be
a distinct terminal state with its own name.

---

# Part II — Ownership, stated correctly

## The rule v1 got wrong

v1's headline was **"one writable tier — every political write in the game lands on a settlement."**
That is false, and its own annex says so: provinces store stabilisation and vacuum windows, Attention,
Thread Debt, the trade-route token and temperament drift; polities store five stats, a hand, a mission
and offices; the peninsula stores the clocks. All are written every season.

The correct rule is the weaker one v1 also stated and then over-claimed past:

> **Every quantity has exactly one owner and exactly one write path. If it is derived, nothing writes
> it — the things that would have written it write its inputs instead.**

"One owner per quantity" is a real constraint. "One writable tier" is a slogan that happens to be
wrong, and the difference matters because the slogan invites people to push state down to the
settlement tier where it does not belong.

## What each tier owns

Every territorial field carries a tag — **dejure** (a statement of right), **defacto** (a statement of
control), or **civic** (a fact about the place itself, belonging to neither). *A field that cannot be
tagged is mis-modelled*, and applying the test moved two fields and sharpened a third.

| tier | owns (written) | derives (never written) |
|---|---|---|
| **Holding** | presence flag `civic`, condition `civic` | the capabilities it confers |
| **Settlement** | `Order` `Prosperity` `Defense` `Π` `PT` `ledger[]` `holdings[]` `interest_groups[].approval` — all `civic` · `L` `PS` `civic, relative to the current holder` · `holder` `defacto` · `governor` `defacto` · `needs[]` `directive` `civic` | Weight `W_s`, acceptance `q_s`, capability set, black-market and broker states |
| **Province** | `de_jure_parent` **dejure** · Attention · Thread Debt · temperament drift · trade-route tokens — all `civic` | **de facto holder**, `Accord = ⌊mean Order⌋` (`defacto`, derived from `civic` Order — the derivation is the bridge between the two), PV shares, fracture state, Prominence |
| **Title** (realm · duchy · province · settlement) | `holder` **defacto** · `de_jure_parent` **dejure** · `seat` · `contested_since` · `held_since` · offices attached | de facto extent, cohesion, the de jure/de facto gap |
| **Duchy** | *(a title — see above)* | — |
| **Realm** | title holder · succession law · standing laws | de facto extent, legitimacy of the holder |
| **Polity** | five stats · hand · mission · offices · treasury · claims held · relations | `Mandate`, aggregate `L`/`PS`, income, administrative load |
| **Peninsula** | the five clocks · campaign-arc state | band memberships, threshold proximity |
| **Character** | convictions · standing · renown · schemes · relations · holdings of office | capability, influence, exposure |

**Two fields failed the test and moved.** The vacuum and stabilisation windows sat on the province as
though they were facts about the land. They are **timers about a de facto transition**, so they belong
on the title, as `contested_since` and `held_since` — and the province stops carrying state about
events that happened to it.

**One field needed a qualifier, and the qualifier is real content.** `L` and `PS` are civic, but only
*relative to the current holder*: acceptance is not a property of a place alone, it is a property of a
place **under someone**. That is why conquest does not inherit them, and stating the tag is what
forced the semantics into the open.

## Acceptance has two grains, and v1 stored both at one

This is the correction with the largest consequences, and the corpus contains both the error and the
evidence against it.

**The corpus defines Legitimacy in polity-scale terms** — `settlement_layer_v30 (1).md:154`:

> "**Legitimacy (L), 0–7** — institutional/constitutional acceptance (slow-moving: **dynastic claims,
> papal bulls, constitutional authority**)."

Every example is a fact about a realm or a church. **It then stores L per settlement**, and bridges
the gap with a smear — `:175`:

> "Faction-level mission outcomes … apply their ΔL/ΔPS **to the faction's controlled settlements
> (uniformly, clamped 0–7)**"

v1 inherited this without examining it. The consequences are not cosmetic:

- **A coronation becomes twelve writes.** One polity-scale event is applied to every held settlement,
  each clipped by the per-source seasonal cap, and then re-aggregated through a saturating function
  whose output depends on how many settlements the faction happens to hold. **The same event has a
  different magnitude for a large faction than a small one**, in the wrong direction, and the corpus's
  own tuned thresholds stop being reproducible.
- **It erases within-faction variety** at exactly the grain the design wants settlements to differ.
- **It is the wrong thing conceptually.** A papal bull is not a fact about a village.

**The correction — split acceptance by grain:**

```
Polity.Legitimacy   0–7   STORED at the polity.  Written by polity-scale events only:
                          coronation · bull · succession · treaty · excommunication · deposition
Settlement.PS       0–7   STORED at the settlement. Written by local events only:
                          governance verbs · levies · sieges · card responses · interest-group swings

Mandate(f) = g( f.Legitimacy , W-weighted mean PS over f's holdings )
```

One coronation is now **one write**. A governor's good season is still a local write. And the two
inputs to Mandate are finally the two things Mandate was always trying to blend: *do they have the
right to rule*, and *do the people go along with it*.

## Mandate's derivation is per-status, and the corpus already knew

v1 derived Mandate from held settlements for every polity. That starves the two polities whose power
is not territorial:

- **The Church holds one settlement.** Its Mandate therefore derives from Himmelenger alone — the
  corpus's own sim lands it at 5 — while its actual reach is presence, piety and a confessional track
  across all thirty-seven. Worse, **Prominence** (the trigger for its entire seizure apparatus)
  compares that one-settlement figure against expanding territorial factions whose saturating
  aggregate climbs to 6–7. **The Church's central mechanic starves precisely as the game gets
  interesting**, and nothing in v1 noticed.
- The corpus **already solved this, once** — `:171`:

  > "**Restoration** is territoryless and operates at the **community** level via Presence markers, so
  > its L/PS live in its Presence localities … and T is summed over those localities."

It applied the presence-based derivation to the Restoration Movement and left the Church on the
territorial one. **Generalise it into a per-status strategy:**

| polity status | Mandate derives from |
|---|---|
| **territorial** (realm- or duchy-holding) | Legitimacy + W-weighted PS over held settlements |
| **confessional / movement** (presence-based) | Legitimacy + presence-weighted PS over settlements where `presence ≥ 1` |
| **embedded** (holds no title, acts through a host) | N/A until it holds a title — which is exactly the Löwenritter's grievance |

## Garrison-holder is not settlement-holder

The corpus's sharpest single situation — a Löwenritter garrison inside a Crown-held fortress — has no
object in v1, which encodes it as arithmetic on the Crown's Military stat. Separate them:

```
Settlement { holder : PolityId }          -- who governs
Garrison   { at: SettlementId, polity: PolityId, units: [...] }   -- who holds the swords
```

Once these are distinct, graduated autonomy stops being a bespoke four-state ladder and becomes the
readable consequence of a garrison whose polity is not the settlement's holder — and the same object
covers an allied army quartered in your capital, an occupying force, and a mercenary company that has
not been paid.

Two further things this table makes visible that v1's did not.

**Claims are owned by polities and characters, not by territory.** A claim on Gransol is not a fact
about Gransol; it is a fact about the claimant. That is why claims can be traded, inherited and
fabricated, and why they survive the loss of the thing claimed. v1 had nowhere to put them, which is
why it did not have them.

**Interest-group approval is settlement-owned.** It is the one genuinely new stored quantity in v2,
and it is what turns Π from an abstract scalar into a readable one (Part IV).

## Holdings — the differentiation layer v1 dropped

v1 contains **zero** occurrences of "sub-feature". The corpus has sixteen, and they are the reason one
settlement is not another.

```
Holding {
  kind      : harbour | mine | barracks | cathedral | chapel | market | seminary
            | watchtower | lodge | shrine | storehouse | gate | ruins
  parent    : SettlementId          -- never separately siegeable
  condition : intact | damaged | razed
  confers   : [Capability]
}
```

A **capability** is a permission, not a bonus: `sea_route`, `unit_production`, `piety_projection`,
`vision_extension`, `covert_meeting`, `resource_yield`, `assembly_seat`. Rules gate on capabilities and
never on settlement names:

- Sea routes attach to settlements with `sea_route` — which is why Valorsplatz↔Schoenland exists and
  why a naval expansion is *building harbours*, not editing an adjacency table.
- The Church's four "independent axes" become four holdings with piety and seizure-obstacle
  capabilities, and the four-axis table is data.
- The five starting friction points stop being hand-placed: **a friction point is a settlement whose
  holdings confer capabilities on an institution that does not hold the settlement.** S003 Valorsplatz
  Cathedral is Church-capable inside a Crown-held capital. That is a *derived* condition, and any
  settlement that acquires the same shape becomes a new friction point without anyone authoring one.

**This is what makes the map worth reading.** Without holdings, every settlement of a type is
mechanically identical and the strategic layer is about how many you hold. With them it is about which.

---

# Part III — The Claim

## Six mechanics, one object

v1 has zero occurrences of `title` and one of `casus belli`. The corpus builds six mechanisms that are
all the same thing:

| corpus mechanic | what it is |
|---|---|
| **Casus Belli** — generated by events, held, consumed on use, expiring | a claim licensing war |
| **Baralta Crown Claim** / Consecration Crisis | a claim on the realm title |
| **Succession Contest** — blood claim, contender strength, heir Disposition ≥ +3 | competing claims on a polity's leadership |
| **Parliamentary Transfer** of a province | a claim prosecuted by vote instead of by army |
| **Insurgency → Promoted Faction** | a claim acquiring recognition |
| **Bishop / Ecclesiastical Appointment** | a claim on a settlement's governance, prosecuted administratively |

```
Claim {
  subject     : TitleId                                  -- what is claimed
  claimant    : PolityId | CharacterId
  basis       : blood | conquest | charter | office | recognition | fabrication
  strength    : Clamped<0,5>
  origin      : season, event                            -- provenance, for the ledger
  expires     : season | never
  secrecy     : public | private                         -- a fabricated claim can be secret
  prosecutable_by : {war, vote, appointment, marriage, purchase, uprising}
}
```

**Basis determines which routes are open**, and that one table replaces six bespoke eligibility rules:

| basis | war | vote | appointment | marriage | purchase | uprising |
|---|---|---|---|---|---|---|
| blood | ● | ● | | ● | | |
| conquest | ● | | | | | |
| charter | | ● | ● | | ● | |
| office | | ● | ● | | | |
| recognition | ● | ● | ● | ● | ● | |
| fabrication | ● | | | | | ● |

Read the rows and the corpus's own politics falls out. The Church prosecutes by **appointment**
because its claims are `office`-based — which is exactly why Bishop Appointment is Ob 1 and
uncontested ("the bishop is already there running the church; the appointment is formalising what is
already happening") and why Mass Seizure, a `conquest` prosecution, is the moment it stops being a
partner in governance. Hafenmark prosecutes by **vote** because its claims are `charter`-based; that is
its whole identity. Varfell prosecutes by **war**. The Restoration Movement has no claims at all until
it acquires `recognition`, which is precisely what promotion means.

## What becomes simpler

- **Casus Belli duration**, which the corpus never specifies and v1 could not fix, is now `expires` on
  a claim, and different bases expire differently: conquest claims decay, blood claims do not.
- **A promoted insurgency has something it did not have before** — recognition-based claims on the
  provinces it holds. That is the mechanical content of "promotion", which v1 left as a status flag.
- **Fabrication is a scheme** (Part IV), and a fabricated claim that is discovered before it is
  prosecuted is worse than useless: it is a grievance handed to the target. That is a whole class of
  play v1 had no room for.
- **The Baralta arc stops being bespoke.** It is one character accumulating strength on a blood claim
  against the realm title while the Consecration route determines whether a rival's claim gains
  `recognition`.
- **Treaties become claim instruments.** A treaty that cedes a province is the transfer of a title; a
  guarantee is a conditional claim on the guarantor's behalf; a betrayal generates a `recognition`
  claim for the injured party. The corpus's treaty-expiration mechanic — its best-validated
  balance lever — becomes "claims created by this treaty lapse", which is why lapse hurts.

## Vacancy is not a transfer

A title whose holder is `∅` **persists, and every claim on it survives**. That is precisely why an
Uncontrolled province is dangerous rather than empty: it is *claimed by several parties and held by
none*, and the insurgency pipeline's trigger — "2+ contiguous territories at Uncontrolled status,
sustained 2 consecutive seasons" — is the corpus noticing that a vacuum with claimants in it does not
stay a vacuum.

## Claims are the durable political substance

This is the object v1 most lacked, and its absence is why v1 felt like an accounting system. Claims
**persist** (they outlive the loss of the thing claimed), **accumulate** (a faction with six dormant
claims is dangerous in a way its stat line does not show), **transfer** (by marriage, inheritance,
treaty, sale), and **can be secret**. Nothing else in the design has all four properties, and a
political game needs at least one thing that does.

---

# Part IV — Agents: blocs, schemes, and the officer network

The corpus's best generative material is here, and v1 preserved its shape while draining its content.
Three changes, each small in structure and large in what it produces.

## 1 · Local Actors become interest groups

v1 kept the corpus's NPC dossier — convictions, ambition, trajectory, leverage, knots — and modelled
the settlement's politics as a set of **dispositions**: scalars that go up and down. Dispositions do
not generate politics. **Blocs with demands do.**

```
InterestGroup {
  kind      : Landed | Mercantile | Clerical | Commons | Martial | Restorationist
  approval  : Clamped<-3,+3>          -- toward the settlement's current holder
  weight    : derived from the settlement's holdings and Prosperity
  demands   : [Demand]                -- derived from settlement state, not authored
  leader    : CharacterId | ∅          -- a Local Actor speaks for them, or nobody does
}
```

Each settlement carries three or four of the six, with weights derived from its holdings: a Port with
a market has Mercantile weight; a Cathedral has Clerical; a Barracks has Martial. **The composition of
a settlement's politics is a consequence of what is built there**, which is what makes holdings
matter twice.

**Demands are derived, never authored.** `Prosperity` falling raises a Commons demand for relief;
a Guild charter unhonoured raises a Mercantile demand; `PT` falling raises a Clerical demand for
suppression; a Levy raises a Martial demand for compensation and a Commons demand against
conscription. The governance verbs each *serve* some demands and *offend* others, and the method
choice the corpus is so proud of — Treasury vs Guild charter vs Corvée — is exactly a choice of
**which bloc to pay and which to disappoint**.

**This is what Π was always summarising.** v1 carried Π as a scalar with five undefined terms. In v2:

```
Π = Σ over groups of  weight × max(0, −approval)   +  Σ unserved demands × urgency
    + Σ active schemes targeting this settlement   −  releases this season
```

Every term is now a thing the player can see and act on, and the pressure number stops being an
oracle. When Π is 8 the player can read *who* is angry, which is the difference between a warning
light and a political situation.

**And revolt becomes what it historically is.** Not a die roll against Order, but *a coalition*: two
or more groups whose combined weight exceeds a threshold, at approval ≤ −2, with a leader. The
composition of the coalition determines what the revolt *wants* — a Clerical–Commons rising is a
religious revolt, a Mercantile–Landed one is a constitutional crisis — and therefore what settles it.

**A coalition does not seize a title; it generates a claim.** The leader acquires a
`recognition`-basis claim on the settlement, and the uprising route prosecutes it. This is a better
model than the shortcut, and the difference is visible in play: a secession can be **bought off** by
satisfying the claim, and a *failed* secession leaves the claim standing — which is how grievances
actually behave, and how the next rising already has its casus belli.

## 2 · Ambitions become schemes, which can be discovered

The corpus's NPC ambition has goal, method, timeline and progress, and advances every Accounting
whether or not the player engages. v1 kept this exactly. **It is three-quarters of a scheme, and the
missing quarter is the one that matters.**

```
Scheme {
  agent     : CharacterId
  target    : CharacterId | TitleId | SettlementId
  intent    : advance_to_office | fabricate_claim | defect | expose | murder
            | suborn | organise | embezzle
  method    : lawful | factional | covert | violent
  progress  : Clamped<0,5>
  secrecy   : Clamped<0,5>            -- NEW
  agents    : [CharacterId]           -- NEW: others who have joined
  discovered_by : {PolityId}          -- NEW
}
```

Three additions and the mechanic changes character entirely:

- **Secrecy decays** as progress rises — the closer a plot is to firing, the more people know. So the
  window in which a scheme is both dangerous and invisible closes on its own, and *investigation* has
  something to find.
- **Others can join**, which is how a lone ambitious Magistrate becomes a faction. Joining is what
  the corpus's Knots relational graph is *for* and never quite gets used for.
- **Discovery is a resolution, not an event** — a contest between the investigator's relevant
  capability and the scheme's `secrecy`, emitting a `Degree` like everything else:
  **Overwhelming** reveals the scheme, its agents *and* its patron; **Success** reveals the scheme;
  **Partial** reveals that *something exists* without its content — the "Order −1 from an unknown
  source" that tells a player there is something to find; **Failure** alerts the schemer, who gains
  secrecy. In v1 an ambition advanced in private and then fired. Here, learning about it in time is
  the whole of the play, and the `Investigate` verb — which v1 kept as one of eight and gave nothing
  distinctive to find — becomes the counter-intelligence layer the game needs.

**Discovery also feeds the ledger.** An exposed scheme writes a `Grudge` on the schemer and a
`Precedent` on the governor who exposed them; a scheme exposed and *sheltered* writes a `Debt`. The
four ledger families the corpus invented finally have a mechanism that produces them at volume.

## 3 · The officer network

The corpus cites KOEI *Romance of the Three Kingdoms* by name and then models people as dispositions
attached to settlements. What ROTK actually has is a **roster**: officers are the unit of politics,
they hold offices, they carry loyalty, and **when loyalty fails they defect with what they hold**.

Valoria has all the parts — Standing 0–7 ladders across four factions and seven sub-offices, named
inner circles, Knots, caste, Disposition. What it lacks is the edge that makes them a network:

```
Office {  attached_to: TitleId,  rank: 0..7,  holder: CharacterId,  granted_by: CharacterId  }
```

**Offices are owned by the title they attach to** — not by the polity and not by the character. A
polity *derives* its roster from the titles it holds; a character derives their offices from a reverse
index. One fact, one home. It also makes conquest a political event rather than a map update: when a
title changes hands, **its offices travel with it**, and the new holder inherits a staff whose
loyalties were bought by someone else.

`granted_by` is the whole mechanism. It makes patronage a graph: who raised whom. And it gives
defection a *shape* — when a patron falls, their clients are exposed; when a patron defects, the
question is which clients follow. **Defection cascades run along patronage edges**, and that is the
corpus's "faction split" mechanic arriving for free instead of being authored per faction.

It also makes the player's own rise legible. Climbing the Standing ladder is acquiring a patron and
then acquiring clients, and the moment the player has more clients than their patron is the moment the
succession machinery starts pointing at them — which is exactly the arc `player_agency_v30` describes
as "risen from nobody to contender through accumulated deeds" and never mechanises.

---

# Part V — The instability budget

## The problem, measured

Across v1 and its executable annex: **≈ 245 damping devices** (`clamp` 92, `cap` 95, `floor` 43,
`saturating` 6, `ceiling` 4, `bounded` 3, `mean-revert` 2) and **zero amplifying ones** (`spiral`,
`positive feedback`, `amplif*`, `compound`, `escalat*`, `snowball` — all zero). The word `runaway`
occurs twice, both times to say runaway is prevented.

A system in which every quantity is bounded, every loop is negative, and every cross-scale effect is
clamped at ±2 **converges**. Season 40 resembles season 30, the player learns the equilibrium, and the
world runs out of things to do to them. That is not stability; it is inertia, and I built it by
optimising for a clean model.

The corpus wanted otherwise. It uses *escalat\** 24 times, *spiral* 6, *compound* 9, and states the
principle outright:

> "**Resolve Tension A while ignoring Tension B finds Tension B has escalated.** This is the
> historically accurate dynamic: states rarely face one crisis at a time."
> — `early_game_ignition_analysis.md:142`

It also names two "**anti-death-spiral floors**" — and you do not floor a death spiral unless you
believe one is reachable.

## The rule

> **Every feedback loop in the design is named, signed, and budgeted. The negative loops keep the
> game playable. A small, fixed number of positive loops make it worth playing. Entry to a positive
> loop is rare and legible; exit is expensive and possible.**

A design that cannot list its loops cannot tune them. Here is the list.

## First: territory has to compound, or the counterforces have nothing to push against

The correction that must come before the regimes, because without it they are counterforces to a force
that does not exist.

**In v1, holding eight provinces is barely different from holding three.** Army size is capped at the
Military stat (0–7). Parliamentary votes equal Mandate (0–7). Mandate itself saturates by
construction, so the tenth province adds almost nothing. **Territory does not convert into power**,
which means there is no overextension, no snowball, and therefore no rise-and-fall cycle for any
counterforce to govern. v1 presented this as a virtue and it is the reason nothing in it moves.

Every acclaimed game in this tradition lets holdings compound and makes the *cost of holding* compound
faster. That asymmetry is the whole engine:

| | holdings buy you | holding costs you |
|---|---|---|
| **CK3** | levies, income, titles to grant | vassal opinion penalties and faction strength that scale with realm size |
| **EU4** | development, manpower, force limit | aggressive expansion accruing per conquest, decaying slowly, forming coalitions above a threshold |
| **Shadow Empire** | production, recruitment | administrative capacity consumed per zone, and capacity is finite |

**So: let the caps scale with what is held, and let the costs scale faster.**

```
force_limit(f)  = base + ⌊Σ over held settlements of (Prosperity + FacilityTier) / 4⌋
votes(f)        = Mandate + ⌊de jure provinces held / 3⌋
income(f)       = Σ settlement Prosperity          (already linear — keep it)

against

strain(f)       = load − capacity        (below; superlinear in the de jure gap)
regard drift    = every polity's regard for f falls by ⌊provinces held / 4⌋ per season
directive load  = one Directive per held settlement per season, drawn from a finite pool
```

**The uniform caps survive and change role.** TL-6 exists to stop *special cases*, not to stop growth:
a cap that applies identically to everyone is still uniform when its value is a function of holdings.
What v1 did was use uniform caps as the *only* counterforce, which is what froze the game. Caps stay
as the anti-special-case rule; scaling costs become the anti-snowball.

## The negative loops — these keep, and they are correct

| loop | mechanism | why it must stay |
|---|---|---|
| **Legitimacy ↔ acceptance** | polity Legitimacy raises the *floor* on settlement PS recovery, and low PS drags the aggregate | stops one bad province dragging a realm down — **without punishing a good one** (see below) |
| **Saturating Mandate** | `clamp(round(7·T/(T+K))), K = 6` | the tenth loyal hamlet is worth less than the first city |
| **Π homeostat** | draws Opportunity cards when quiet, bleeds on resolution | anti-stall in both directions |
| **Seasonal caps** | ±5 CI all sources, ±3 from actions, ±2 per faction stat | nothing moves faster than the player can read |
| **Echo clamp ±2** | cross-scale magnitude bound | one scene cannot decide a war |
| **Accord passive normalisation** | +1 per quiet garrisoned season, cap 2 | conquered ground settles if left alone |

### The one negative loop that was signed wrong

v1 kept the corpus's Mandate↔L/PS feedback as written:

> `q_s ≤ Mandate(f) − 1 → L +1;  q_s ≥ Mandate(f) + 1 → PS −1`

Read the second clause. **A settlement governed above its realm's average loses Popular Support every
season until it sinks back.** A player who lifts a settlement to acceptance 7 inside a Mandate-3
faction is penalised, every season, for succeeding. And because the two clauses are asymmetric — the
laggard gains *Legitimacy*, the leader loses *Popular Support* — the realm's L inflates and its PS
deflates by construction, regardless of play.

The corpus is candid about the intent: it calls the loop "mean-reverting / stabilizing" and reports
that the coupled system "converges over 30 seasons under mission shocks (**no runaway**)". v1 quoted
that as a virtue. **Convergence is not a design goal; it is what happens when a design has no other
ideas.**

**Correction — keep the floor, drop the ceiling:**

```
q_s ≤ Legitimacy(f) − 2  →  PS +1     (the realm's standing lifts its worst places)
q_s ≥ Legitimacy(f) + 1  →  no effect  (excellence is not taxed)
```

Regression toward the realm's *legitimacy* is defensible — a well-regarded crown does help a sullen
province. Regression toward the realm's *mean* is not, because it makes the mean an attractor and
governing well a waste of Administration Points.

## The positive loops — three, and they are the game

Each is **off by default**, entered by a legible condition, and exited at a price. While a regime is
live, its driving quantity's feedback flips sign.

**The suspension rule is uniform, and this matters more than the regimes themselves.** An earlier
draft raised the CI cap from ±5 to ±8 for the confessional cascade and admitted in its own margin that
this "breaks the uniformity rule". It did. The rule is generalised instead of the exception being
carved:

> **An armed regime raises the seasonal cap on its own driving track by 60%, rounded down, for its
> duration.** One rule, identical for every regime, present and future.

±5 → ±8 now *falls out* for R-2 rather than being asserted for it, and R-1 and R-3 get the same
treatment on their own tracks. Uniformity survives and the cascade still gets its speed, which is all
the special case was ever buying.

### R-1 · Legitimacy collapse

```
ENTRY   a polity's Mandate ≤ 2 while it holds ≥ 3 provinces de facto
        (weak authority over more ground than weak authority can hold)

LOOP    low Mandate → settlements' L/PS drift DOWN toward it, not up
        → lower aggregate → lower Mandate
        → interest-group approval falls with it
        → coalitions form → Order falls → Accord falls → provinces vacate

SUSPENDS  the Mandate ↔ L/PS mean-reversion, which now points downward
EXIT    Mandate ≥ 4 for two consecutive seasons, by any means
        — or the realm partitions and each fragment starts clean
FLOOR   the corpus's own anti-death-spiral floor: Stability cannot pass 0,
        so collapse ends in partition, never in an unplayable state
```

This is the corpus's own instinct made mechanical. It is why over-expansion is punished, and it is the
loop that makes the Löwenritter's grievance dangerous rather than decorative.

### R-2 · Confessional cascade

```
ENTRY   ∃ polity p : p.has_track(confessional) ∧ p.track ≥ 60
        ∧ |{settlement titles held by p conferring piety_projection}| ≥ 2

LOOP    piety_projection → PT rises in adjacent settlements
        → appointment eligibility spreads (a capability test, never a faction test)
        → each appointment raises p's track → widens eligibility further

EXIT    a coalition (R-3) reduces p's piety-projecting holdings below the entry line,
        or p's own confessional instrument is turned back against it
```

Exactly one polity currently has a confessional track. **That is a scenario fact, not a rule** — and
the distinction is load-bearing, because this game promotes new factions at runtime and a regime keyed
to a named faction could never arm for a Restorationist theocracy or a promoted insurgency with a
confessional programme, both of which the corpus builds toward.

The corpus supplies every component of this loop — the Geneva trap, Piety Yield, appointment at Ob 1,
the cubic CI curve — and then caps it into a gentle ramp. The cascade is what those components are
*for*.

### R-3 · Coalition against the leader

```
ENTRY   a polity holds ≥ 8 of the 15 de jure provinces, or holds the realm title
        while a rival holds ≥ 5 de facto

LOOP    the leader's holdings → GD-2 mandatory threat response fires in every
        polity whose de jure land the leader holds de facto
        → their claims against the leader gain +1 strength per season
        → prosecuting those claims is cheaper (shared casus belli)
        → losses reduce the leader's Mandate → which feeds R-1

EXIT    the leader drops below the entry line, or buys off members individually
        (each purchase costs a title, which is why it is expensive)
```

**This is the anti-snowball the design entirely lacked**, and the corpus already contains its
trigger: GD-2's "mandatory threat response" sits unused in the insurgency pipeline. Nothing in v1
made winning harder. Here, the eleventh province is the hardest one to take, which is the shape every
game in this genre needs and none of them gets for free.

## The pressure primitive exists at one scale and must exist at three

The design's own thesis is that one acceptance primitive and one pressure primitive are instantiated
at every scale. **The pressure primitive is instantiated once.** At settlement scale, Π is a genuine
two-sided homeostat: it injects Opportunity and Ambition cards when the settlement is quiet and bleeds
off when crises resolve — anti-stall *and* anti-runaway, exactly as the corpus specifies.

At peninsula scale the design built only the anti-runaway half, and then signed the other half
backwards. Two of the five clocks **decay when the map is quiet**:

```
ΔIP      … − [IP > 20 ∧ count(provinces with Accord ≤ 1) = 0]
ΔTurmoil … − 1 [∀ controllable p : Accord ≥ 2]
```

**Quiet reduces pressure, which produces more quiet.** That is the anti-stall term with its sign
inverted: a stable map actively drains the two clocks whose job is to make a stable map interesting.
Combined with saturating Mandate and capped everything, this is the mechanism by which v1's late game
goes still.

**Correction — raise Π one tier, symmetrically:**

```
Π_world = Σ over polities of unresolved claims × strength
        + Σ over provinces of (de jure ≠ de facto)
        + Σ armed regimes
        + Σ over polities of |grievances| held against them
        − releases (crises resolved, claims satisfied, titles legitimated)

draw   1 + ⌊Π_world / 4⌋  peninsula cards per season, family-weighted by band,
       exactly as the settlement deck draws
```

Three properties make this legitimate rather than a director's thumb on the scale:

- **It is symmetric.** Π_world reads the state of *every* polity and draws against all of them. It
  cannot target the player, which is what would make it scripting under TL-9.
- **Its terms are the design's own objects** — unresolved claims, de jure/de facto gaps, armed
  regimes, grievances. It is a *summary* of the political situation, not an injected difficulty knob,
  and like settlement Π it can be read: when Π_world is high the player can see which claims and which
  gaps are driving it.
- **It fixes the sign.** A quiet map has claims sitting unprosecuted and gaps sitting unlegitimated,
  so Π_world *rises* during quiet and the deck starts offering. A busy map spends them, and Π_world
  falls. That is the corpus's own anti-stall logic — "the world starts offering rather than
  threatening, but it never stops moving" — applied where v1 left it out.

## Administrative strain — the second anti-snowball

Borrowed from Shadow Empire, and cheap here:

```
load(polity)     = Σ over held titles of  tier_weight × (1 + de_jure_gap)
capacity(polity) = base + Σ over settlements of FacilityTier + offices filled by competent holders
strain           = max(0, load − capacity)
```

Strain costs one Administration Point per two points, realm-wide, and raises the obstacle on every
Domain Action by `⌊strain/3⌋`. **Growth is self-limiting through a mechanism the player can see and
plan against**, rather than through the AI happening to gang up. It also gives the Ministry — a
faction the corpus defines as pure civil service and gives almost nothing to do — its reason to exist:
it is the capacity engine, and capturing it is how you grow past your own competence.

Note the `de_jure_gap` term: holding land that is de jure someone else's costs **more** to administer
than holding your own. Conquest is expensive to keep, legitimation is the discount, and that is why
claims are worth prosecuting rather than merely holding.

## The ratchets

A fixed, enumerated set of things never move backward. Everything else is recoverable. The list is the
union of every irreversibility in the design — including the `irreversible` flags declared by
pipelines, which an earlier draft left out of a list that claimed to have three entries:

| ratchet | mechanism |
|---|---|
| **Ledger tags** | Precedent · Grudge · Debt · Reputation. They expire but never reverse, and they survive succession — the corpus is explicit and it is right. |
| **Standing laws** | succession law, the parliamentary settlement, ecclesiastical privilege: chosen once, changeable only by a crisis that costs more than the law does. The Frostpunk lesson — an irreversible path through a small tree generates more campaign identity than a large tunable state. |
| **Incorporation** | land given a de jure parent stays land. The map can grow; it cannot shrink. |
| **Terminal pipeline states** | every `irreversible` flag, enumerated rather than remembered: Split · Promoted Faction · Scheme fired · Title destroyed. |
| **Claims extinguished by fulfilment** | a prosecuted claim is consumed and does not regenerate on the same basis. Grievance can recur; *that* grievance cannot. |

Five, and the list is now derivable by grep rather than by memory — which is what a principle about
enumeration has to be able to promise.

## The budget, stated

**Six negative loops · three positive regimes · one world-scale pressure controller · two scaling penalties · five ratchets.**

That is the whole dynamical content of the design, and it fits on a page — which is the point. A
system whose loops cannot be listed cannot be tuned, and a system with only negative loops cannot
surprise anyone.

---

# Part VI — Dependencies as data

## Where v1's claim was false

v1 claimed "no subsystem names another". True of its code; false of its content, which is where it
matters. Its own exemplar card carries `settlement.has_subnational(RM)` as a trigger predicate, and
its directive generator maps `Counter-threat → Suppress(RM|Church)`. **Named factions inside rules is
exactly the scripting drift the design's own throughline forbids**, and content is where a rule
system actually rots.

## Roles, not identities

Every predicate references a **role** or a **relation**, never a name.

| forbidden | required |
|---|---|
| `has_subnational(RM)` | `∃ inst : presence(inst) ≥ 2 ∧ hostile(inst, holder)` |
| `Suppress(RM \| Church)` | `Suppress(argmax_inst threat(inst, self))` |
| "Crown runs a fragmentation check" | any holder of a province with de facto divergence |
| "Church gets ⌊CI/20⌋ bonus" | any polity with a confessional track, of which there is currently one |

The test is mechanical: **grep the content layer for proper nouns.** A rule containing one is either
a scenario (fine, and belongs in the scenario file) or a bug (a mechanic that will not generalise to
a faction that emerges mid-campaign — which this game creates by design).

This matters more here than in most games because Valoria **manufactures new factions at runtime**.
An insurgency promoted in season 30 must be able to use every rule that mentions the Church, or the
promotion is cosmetic.

## The clock layer is a graph, and should be authored as one

The five peninsula clocks — CI, Altonian, Strain, PI, MS — plus the tracks that feed them are a
signed, weighted, lagged influence network, and nothing else. Author them as one:

```
Edge { from: NodeRef, to: NodeRef, sign: ±, weight: Rational, lag: seasons, condition: Predicate? }
```

`Node` is any measurable: a clock, a derived aggregate, a count of provinces in a state. Then:

- the whole clock layer is a data file, and adding a track is adding rows;
- the engine is an evaluator with a fixed cap per node per season, so the uniform caps survive;
- and — the reason this is worth doing at all — **the game can show the player the path**. "Your
  Altonian pressure rose because two provinces fell below Accord 2, which fired GD-2 in Varfell,
  whose muster raised the border count." A no-GM engine has removed the person whose main job was
  answering *why did that happen*, and an inspectable graph is the only honest replacement.

## What stays procedural, and why

An influence graph cannot express sequence, and this game genuinely needs sequence. These stay as
procedures with ordered steps and branch predicates:

**Sieges · successions · votes · seizures · contests · scheme resolution · battles.**

The division is not aesthetic. A procedure is required wherever the *order* of sub-steps changes the
outcome — a siege where relief can arrive between assaults, a vote where declarations precede
counting. Everything else, meaning everything that is a rate or an equilibrium, is an edge.

## Pipelines remain data

The five pipelines v1 correctly identified as one — Löwenritter autonomy, insurgency promotion,
succession, NPC schemes, RM emergence — stay a single interpreted type, now with the fields Part V
requires:

```
Pipeline {
  subject, states, advance_rate, promote: Predicate → State, demote: Predicate → State,
  irreversible: {State},
  regime: RegimeId | ∅        -- NEW: which instability regime, if any, this pipeline can trigger
  on_enter: [Effect]
}
```

`regime` is the one addition, and it is what stops the positive loops from being special cases: a
pipeline reaching a state that carries a regime *arms* that regime, and the regime's own exit
condition disarms it. Löwenritter reaching **Split** arms R-1 in the Crown. The Church's second
acquired settlement arms R-2. A polity crossing eight provinces arms R-3.

---

# Part VII — The tick, corrected

The twelve-phase structure survives. Two things in it were wrong.

## What v1 got wrong about effects

v1 retired the corpus's Cascade Depth Cap on the grounds that **"effects never fire effects within a
phase"**. That is false of v1's own tick, which states that "PH-08 onward are Accounting phases that
apply their own effects at the end of each phase through the same commit routine". A threshold crossed
in PH-09 fires a pipeline in PH-10 which emits effects which commit. That is an effect firing an
effect, and the cap was retired on a premise the design does not honour.

**The correct rule, stated so it is checkable:**

> Effects are applied in **generations**. Within one phase, all effects queued at entry commit
> together; effects *produced* by that commit form the next generation and commit at the **start of
> the next phase that owns their target scale**. A generation never commits in the phase that
> produced it. The chain therefore has depth at most the number of remaining phases, which is
> bounded by twelve and monotonically decreasing.

This bounds chain *depth* provably rather than by an arbitrary limit of three, and without the false
claim that chaining does not happen.

**But depth was never what the corpus's cap was capping, and v1 retired it on a misreading.** The rule
reads:

> "Maximum **3 immediate mechanical effects per card play resolution step.** Additional effects
> **queue to next Accounting**." — `clocks.md` › Cascade Depth Cap

That is a **fan-out** budget with a deferral, not a depth limit — a pacing throttle that stops one
card play from resolving six things at once and spreads the remainder across seasons.
`parliament.md` depends on it explicitly, staggering treaty-betrayal consequences across four windows
"keeping each step within the Cascade Depth Cap of 3". v1's generations fix addresses depth and
silently discards the pacing.

**Keep both, and say which is which:**

```
DEPTH   bounded structurally by generations — no cap needed, and none is set
FAN-OUT budgeted: at most 3 effects from one resolution commit in its own generation;
        the remainder defers to the next generation in priority order
```

The deferral is what makes a six-effect card *unfold* over two or three seasons instead of landing
as a wall of numbers, and that unfolding is the pacing the corpus was protecting. Authored staggering
— the treaty-betrayal case — is then expressible as explicit generation targets rather than as a
side-effect of a cap.

## What v1 left unfinished: simultaneity

v1 inherited "battles resolve simultaneously per territory" with casualties read back inside the phase,
which is order-dependent and undefined. **Resolve it the way simultaneity is always resolved:
snapshot, then apply.**

> All simultaneous resolutions in a phase read the **same immutable snapshot** taken at phase entry
> and write to the effect queue. Nothing in a simultaneous set observes another's result. Mutual
> destruction is therefore possible and correct — two armies can destroy each other, two claimants
> can both die.

**And the snapshot is rebuilt after every commit point, not twice a tick.** v1 rebuilt derived state
at two phases only, which produces a specific and nasty class of bug: pipelines that run late in the
tick write *holders* — an insurgency forming, a secession, a realm partitioning — and the phases after
them keep reading the pre-split aggregates. In v1's own ordering, **a realm that partitions in the
pipeline phase has both halves' settlements pulled toward its pre-partition Legitimacy in the very
next phase.** Rebuilding after each commit is cheap — the derivations are pure and already asserted
twice — and it is what makes "derived state is never stale" a property rather than an aspiration.

That last consequence is a feature. Games that resolve simultaneous actions sequentially quietly
privilege whoever the sort order favoured; this does not.

## Preview — the obligation a no-GM engine takes on

The corpus's central design fact is that there is no referee. v1 treated that as a constraint on
authoring (every rule must be evaluable). It is also an **obligation**: the referee's other job was
explaining the world, and nothing in v1 replaces it.

> **Before the player commits an action, the engine shows the full consequence chain of that action
> under the current snapshot** — every effect, at every scale, through every generation, with the
> derivation path for each.

This is achievable precisely because of the properties the design already has: one commit point,
pure derivation, seeded determinism, generations that terminate. Preview is not an extra system; it
is a second read of the machinery that already exists.

Two bounds on it, and they are the interesting ones:

- **Hidden actors stay hidden in their existence, never in their arithmetic.** The preview shows
  "Order −1 from an unknown source" where a covert presence is at work. The player learns there is
  something to find — which is what makes `Investigate` worth an Administration Point.
- **Other agents' declarations are not shown**, because they are simultaneous. The player previews
  the consequence of their own action against a world that has not yet moved, and the gap between
  that preview and the outcome *is* the strategic uncertainty. This is where Valoria differs from a
  fully-previewed tactical game, and it is the right place to differ.

## The tick, unchanged in shape

```
PH-01 OPEN         season flags, budgets, snapshot taken
PH-02 WORLD        needs opened, Π recomputed, directives issued, schemes advance, cards drawn
PH-03 ORDERS       every polity and PC declares against the snapshot
PH-04 PERSONAL     scenes resolve (pool mode); Echoes queued
PH-05 SETTLEMENT   directive responses, AP verbs, card responses — queued
PH-06 PROVINCE     declared actions in tier order; battles simultaneous against the snapshot
PH-07 COMMIT       generation 1 commits, in (scale, path, key) order, under caps
PH-08 DERIVE       de facto extents, Accord, PV, Mandate, aggregates — no writes to primitives
PH-09 CLOCKS       the influence graph evaluates; bands cross
PH-10 PIPELINES    every state machine steps; regimes arm and disarm
PH-11 SETTLE       feedback, decay, expiry, strain, Π release
PH-12 CHECK        rupture, then victory; year-end sub-tick; season advances; state hash
```

**The invariant, restated correctly** (v1's version over-claimed):

> No phase writes a quantity that a later phase derives. Phases PH-02–06 write only to the effect
> queue. PH-07 and each Accounting phase commit their own generation. PH-08 writes only derived
> state and reads only owned state. Effects produced within a phase belong to the next generation.

---

# Audit — the design against its own principles, then against a stranger

## Violations found, and the corrections

### V-1 · R-2 names a faction in a mechanic — TL-5

The Confessional cascade regime reads: `ENTRY  CI ≥ 60 AND the Church holds ≥ 2 settlement titles it
did not hold at campaign start`, and its LOOP and EXIT name the Church twice more. **Three proper
nouns inside the instability budget** — written one section after the principle forbidding exactly
that.

It is not cosmetic. This game promotes new factions at runtime; a regime keyed to the Church cannot
arm for a Restorationist theocracy or a promoted insurgency with a confessional programme, which is a
game state the corpus explicitly builds toward.

**Correction.** The regime keys on a *role*:

```
R-2 · Confessional cascade
ENTRY   ∃ polity p : p.has_track(confessional) ∧ p.track ≥ 60
        ∧ |{settlement titles held by p that confer piety_projection}| ≥ 2
LOOP    piety_projection capability → PT rises in adjacent settlements
        → appointment eligibility spreads (a capability test, not a faction test)
        → each appointment raises p's track → widens eligibility
EXIT    coalition reduces p's piety-projecting holdings below the entry line,
        or p's own confessional instrument is turned against it
```

Currently exactly one polity has a confessional track. **That is a scenario fact, not a rule**, and
the distinction is the whole point.

### V-2 · R-2 suspends a cap for one entity — TL-6

The draft raised the CI cap from ±5 to ±8 while the regime was live, and admitted in its own margin
that this "breaks its own uniformity rule". Under TL-6 as stated, a suspension must itself be uniform.

**Correction.** Generalise the suspension instead of exempting the entity:

> **An armed regime raises the seasonal cap on its own driving track by 60%, rounded down, for its
> duration. One rule, applying identically to every regime, present and future.**

±5 → ±8 falls out for R-2 rather than being asserted for it. R-1 and R-3 get the same treatment on
their own tracks. The uniformity survives *and* the cascade gets its speed, which is what the special
case was trying to buy.

### V-3 · The ratchet list is incomplete — TL-12

Part V names "three things that never move backward" — ledger tags, standing laws, incorporation —
while `Pipeline.irreversible: {State}` lets every pipeline declare irreversible states. Split,
Promoted Faction, and an NPC having acted are all ratchets outside the list.

**Correction.** The list is the union, and it is stated as such:

| ratchet | mechanism |
|---|---|
| Ledger tags | expire, never reverse; survive succession |
| Standing laws | changeable only by a crisis costing more than the law |
| Incorporation | land given a de jure parent stays land |
| **Terminal pipeline states** | every `irreversible` flag, enumerated: Split · Promoted Faction · Scheme fired · Title destroyed |
| **Claims extinguished by fulfilment** | a prosecuted claim is consumed and does not regenerate on the same basis |

Five, and the list is now derivable by grep rather than by memory — which is what TL-12's test asks
for.

### V-4 · The ownership table does not tag its territorial fields — TL-1

TL-1's test requires every territorial field to be tagged `dejure`, `defacto` or `civic`, and states
that an untaggable field is mis-modelled. Part II's table tags none of them.

**Correction.** Tag them, and one field fails the test:

| field | tag |
|---|---|
| province `de_jure_parent`, duchy/realm `de_jure_parent` | **dejure** |
| title `holder`, settlement `holder`, province de facto holder | **defacto** |
| `Order` `Prosperity` `Defense` `Π` `PT` `interest_groups[].approval` `ledger[]` `holdings[]` | **civic** |
| `Accord` | **defacto** (derived from civic Order — the derivation is the bridge between the two) |
| `L` / `PS` | **civic**, but they measure acceptance *of a specific holder* |
| ~~`vacuum` / `stabilisation` windows~~ | **fails the test** |

`L` and `PS` needed the qualifier, and that qualifier is real content: acceptance is not a property of
a place alone, it is a property of a place *under a holder*, which is why conquest does not inherit
it. Stating the tag forced the semantics.

The vacuum and stabilisation windows are worse: they are **timers about a de facto transition**, and
they were sitting on the province as though they were facts about the land. **Correction:** they move
onto the *title* as `contested_since` and `held_since`, where they belong, and the province stops
carrying state about events.

### V-5 · Offices have two homes — TL-2

`Office { title, rank, holder, granted_by }` in Part IV, and "a polity stores its five stats, its
hand, its mission and **its offices**" in Part II. One fact, two owners.

**Correction.** **Offices are owned by the title they attach to**, not by the polity and not by the
character. A polity *derives* its office roster from the titles it holds; a character derives their
offices from a reverse index. This also fixes a subtler thing: when a title changes hands, its offices
travel with it, which is what makes conquest a political event rather than a map update.

### V-6 · Not every title transfer consumes a claim — TL-11

Part III asserts that six mechanics reduce to route selection over one `Claim`. Part IV then
introduces **secession by interest-group coalition**, which transfers a settlement title and consumes
no claim. Vacancy (`holder = ∅`) is likewise undefined against the principle.

**Correction.** Both are brought under it:

- **Secession creates a claim before it transfers anything.** A coalition at approval ≤ −2 with a
  leader generates a `recognition`-basis claim held by that leader; the uprising route prosecutes it.
  This is better than the shortcut: it means a secession can be *bought off* by satisfying the claim,
  and that a failed secession leaves a live claim behind — which is how real grievances behave.
- **Vacancy is not a transfer.** A title with `holder = ∅` persists, and every existing claim on it
  survives. That is precisely why an Uncontrolled province is dangerous: it is not empty, it is
  *claimed by several parties and held by none*.

### V-7 · Two resolutions do not emit a Degree — TL-3

Scheme **discovery** is described in Part IV as "an event", and interest-group approval shifts are
described as consequences of verbs. Neither passes through the one outcome type.

**Correction.** Both become resolutions:

- **Discovery** is a contest — the investigator's relevant capability against the scheme's `secrecy` —
  emitting a Degree: *Overwhelming* reveals the scheme, its agents and its patron; *Success* reveals
  the scheme; *Partial* reveals that something exists without its content (the "Order −1 from an
  unknown source" of TL-13); *Failure* alerts the schemer, who gains secrecy.
- **Approval shifts** are the *consequences* of a verb's Degree, not independent events — which is
  already how the ledger works, and makes the method choice (Treasury / Guild charter / Corvée)
  read its result off the same ladder as everything else.

## What the audit did not find

The principles were also applied where they might have been expected to fail and did not, and this is
worth recording so the clean areas are on the record:

- **TL-4 (one cross-scale carrier).** Every new mechanism in this rewrite — claims, schemes, interest
  groups, strain — emits at its own scale and reaches others only by Echo. Nothing needed changing.
- **TL-8 (generations) and TL-9 (snapshot-then-apply).** Both were written *in response* to failures
  found in v1 rather than extracted from it; they hold throughout.
- **TL-7 (every loop named).** Tracing the inputs of every quantity introduced here produced no cycle
  absent from the budget. The strain loop is negative and listed; the claim-accumulation loop feeds
  R-3 and is listed.
- **TL-10 (capability gating).** The five starting friction points derive correctly from holdings and
  are no longer authored, which was the specific thing the principle was written to force.

## What this exercise demonstrates

The seven violations share a shape: **each is a place where the design stated a general rule and then
took a shortcut for a specific case one or two sections later.** R-2 named a faction; the cap was
raised for one track; the ratchet list was written from memory; offices were filed under whoever was
being discussed; secession skipped the claim; discovery skipped the ladder.

None of these would have been found by re-reading, because each is locally reasonable. They were found
by **turning the design's own regularities into tests and running them against it** — which is the
only reason to make principles explicit at all. A principle that cannot fail anything is decoration.

---

## Second pass — the independent critic

The self-audit above found seven violations. An independent critic, working from the same design and
the same corpus with no sight of how either was produced, found **nine more that the self-audit
missed**, three of them behavioural bugs rather than statements. All nine are corrected in the text
above; they are recorded here because the pattern of what one method finds and the other does not is
the most useful output of the exercise.

## What it found that the principles did not

**1 · Authority routed through the wrong object — a live bug.** `Provincial Authority =
controller(province.seat)`, with a Directive issued to *every* settlement in the province. In a
fractured province the seat-holder therefore commands a **rival's** governor, who accrues suspicion
toward a faction they do not serve and is recalled by it. The corpus forbids this in terms —
"Non-Seat-holders issue only settlement-level actions within settlements they hold" — and the
self-audit did not catch it because **the design's text is consistent; only its behaviour is wrong.**

**2 · The same conflation in the revolt rule.** `Accord(p) = 0 → holder := ∅ for every member`,
computed over all members including rivals'. One faction's two ruined settlements strip a rival's
well-governed one.

**3 · Legitimacy is stored at the wrong grain.** The corpus defines L in purely polity-scale terms —
"dynastic claims, papal bulls, constitutional authority" — then stores it per settlement and smears
polity events across holdings "uniformly". A coronation becomes twelve clipped writes whose aggregate
magnitude depends on faction size. **The self-audit recorded this loop as a virtue.**

**4 · The Church's central mechanic starves.** Its Mandate derives from one settlement while its power
is presence across thirty-seven, and Prominence — the trigger for its whole seizure apparatus —
compares that figure against expanding territorial factions. The corpus had already solved this for
the Restoration Movement and not generalised it.

**5 · Territory does not compound.** Eight provinces buy the same army cap, vote cap and near-identical
Mandate as three. The anti-snowball the self-audit was proud of adding was **a counterforce to a force
that did not exist.**

**6 · The mean-reversion punishes good governance.** A settlement above its realm's average loses
Popular Support every season until it sinks back; the asymmetry inflates L and deflates PS regardless
of play. The self-audit listed this in the *negative loops that are correct* table.

**7 · Two peninsula clocks decay when the map is quiet**, so quiet produces more quiet — the anti-stall
term with its sign inverted, at the two scales where the design had no Π at all.

**8 · The Cascade Depth Cap was a fan-out budget, not a depth limit.** It caps effects per card play
and defers the remainder — pacing, which another corpus document explicitly depends on. Both the v1
design and the self-audit retired it as though it capped depth.

**9 · Derived state goes stale mid-tick.** Pipelines write holders late in the tick; later phases read
aggregates rebuilt two phases earlier. A realm that partitions in the pipeline phase has both halves
pulled toward its pre-partition legitimacy in the next.

## What this says about the method

The two passes fail in opposite directions, and neither is redundant.

**The principles found violations of the design's own stated rules** — a proper noun in a mechanic, an
un-uniform suspension, an incomplete list, an untagged field, a double home, a skipped claim, a
resolution outside the ladder. Every one is a **local inconsistency between two passages**, and the
method that finds them is exactly what it looks like: turning statements into tests and grepping.

**The independent critic found places where the design is internally consistent and behaviourally
wrong.** Authority routed through the container reads perfectly; it just commands the wrong governor.
Legitimacy stored per settlement is a coherent schema; it just makes a coronation's magnitude depend
on faction size. Mean-reversion is a well-formed loop; it just taxes success.

**Principles catch contradiction. Only tracing the mechanics catches error.** A design that is
internally consistent and does the wrong thing will pass every test it can write about itself, which
is the strongest argument for the relay — and the reason the self-audit's seven findings, taken alone,
would have produced a confident and defective document.

One more thing the critic caught that neither method was aimed at: **three of v1's numbers disagree
across its own documents** — Accord's promotion threshold is ≥4 in the corpus, ≥2 in one annex and
"widen the range so ≥4 is reachable" in the main text, and the province-value formula gains a
unification bonus in one document and loses it in another. These are the residue of reconciling a
corpus by hand, and they are the kind of thing only a reader who did not write it will look for.

---

# What this costs, and what is still open

## What v2 costs

**More objects.** v1 had one territorial entity; v2 has titles, holdings, claims, schemes, offices and
interest groups. That is six new types against roughly forty saved special cases, and the trade is
worth making only because each new type **absorbs** mechanics rather than sitting beside them: the
claim absorbs six, the title absorbs five, holdings absorb the friction points and the Church's four
axes, interest groups absorb the revolt roll and give Π its terms.

**More authored content.** Capability-gated rules need holdings authored on 37 settlements; interest
groups need weights; claims need starting distributions. This is content work that v1 avoided by
having fewer distinctions — and it is the *right* kind of work, because it is authoring rather than
engineering, and it is what the corpus's own event-card schema was already asking for when it
generalised eight hard-coded rows into a card set.

**A much harder tuning problem, and this is the real price.** v1 could not produce a bad campaign
because it could not produce a dramatic one — every quantity bounded, every loop negative, the whole
thing convergent by construction. v2 lets territory compound, lets three regimes flip loop signs, and
raises a pressure controller to world scale. **It can now genuinely misbehave**: a runaway that never
exits, a coalition that forms too early, a confessional cascade that ends the game at season 30.

That is the correct trade — an inert system cannot be tuned into an interesting one, while an
excitable one can be damped — but it is not a free one. It means the design now *requires* simulation
to find its thresholds, where v1 merely recommended it. The three regime entry conditions, the
scaling exponents on force limit and strain, and Π_world's band edges are all unvalidated numbers,
and none of them can be set at all until the campaign-length question below is answered.

## What is still genuinely open

Five, where v1 had six. Three of v1's were closed by the structure rather than by fiat; two new ones were opened by it — which is the honest shape of a rewrite that adds machinery.

**1 · Does the player govern a settlement or a realm?**
Unchanged from v1 and still the biggest. The AP loop is intimate and settlement-scaled; the Stature
progression runs to "multiple provinces … competes for peninsular sovereignty". Titles make the
transition *expressible* — the player acquires settlement titles, then a province title, then
vassals — but they do not decide whether the AP economy scales up or is early-game content that gives
way to something else.

**2 · How much of the map is de jure fixed?**
De jure drift is the knob that decides whether conquest can ever become legitimate. Set it slow and
the map is a permanent grievance; set it fast and conquest launders itself in a decade. Both are
defensible games. The corpus has no opinion because it lacked the distinction.

**3 · Is the Restoration Movement wrong about the world?**
Unchanged, and now sharper: schemes and claims give RM a way to act politically without Thread
capability, so the revelation arc's mechanical consequence is whether its claims can ever acquire
`recognition` basis. The story question and the mechanical question remain the same question.

**4 · Do holdings compound linearly or superlinearly?**
v2 makes territory buy power and makes the cost of holding grow faster — but the *shapes* of those two
curves decide the whole macro-game. Linear power against superlinear cost gives a game with a natural
ceiling that every faction approaches and none passes, which is stable and possibly dull. Superlinear
power against superlinear cost gives a knife-edge: the leader is always about to either run away with
it or collapse. Both are real games; the corpus has no opinion because it had neither curve.

**5 · Campaign length.**
The corpus states the problem and does not solve it: "The existing clocks assume a 13–15 year game …
games may last 20–30 years. **Clocks must be recalibrated.**" Every threshold, sustained-N trigger and
fuse window is tuned to an assumption the corpus has already disowned. **Settle this first** — it
turns most remaining balance questions into arithmetic, and the three instability regimes cannot be
tuned at all until it is fixed.

## Closed by the rewrite

- **The fracture model** — the two competing schemes were the same mechanism; de jure/de facto
  divergence replaces both, and no sub-province naming is needed.
- **The victory denominator** — 15 is no longer an undocumented constant but a definition: the
  provinces with a de jure parent inside the Kingdom. Askeheim has none; Schoenland's is foreign.
- **Whether Askeheim is reachable** — it is, by **incorporation**: creating a de jure parent for land
  that had none. That is a legible act with a cost, not a deferred contingency.

## The one thing to build first

Not the tick, and not the resolver — both are well-specified and neither is in doubt.

**Build the title tree and the claim registry**, with de jure and de facto separated, and put the
existing corpus's fourteen provinces and thirty-seven settlements into it. Everything else in this
design attaches to those two structures: strain reads the de jure gap, the coalition regime reads
title counts, secession generates claims, promotion grants titles, victory counts de facto holdings
of de jure provinces, and the Löwenritter's entire arc is a holder without a title.

They are also the smallest pieces. Fourteen provinces and one kingdom is a tree with sixteen nodes.
