# 01 — The Machine Itself: the tick, the rungs, the degrees, the remit

## Status: INSTRUMENT (2026-08-30) — Lane 6 of the play-space coverage exercise. Ratifies nothing.
## Reads: `proposals/2026-08-29-valoria-from-scratch/` (17 documents), which is the authority.
## Composes on the suite; adds not one mechanism. Where a cell is empty, the emptiness is the output.

**What this document is for.** Seventeen seasons will be written by other lanes, each a sample point.
This is the reference frame that makes them comparable: what the machine does every season, what a
character at any rung can actually do, what a commitment degree licenses, and what an office adds.

**How to read the marks.** Every cell in View 2 carries one:

| mark | meaning |
|---|---|
| **NAMED** | the suite supplies specific acts; they are listed |
| **THIN** | an act exists but is trivial, dominated, gated shut for most persons, or unparameterised |
| **EMPTY** | nothing in the design fills the cell |
| **N/A** | meaningless by construction — and the construction is named |

A season that lands in a THIN or EMPTY cell should say so and stop. **No lane may invent an act to
fill one.** Two known-open items are reported here and left open: the **conferral dilemma**
(person-rooted vs office-rooted, `16 §6`) and the **testimony half of the salience floor**
(`16 §3.2`).

---

# VIEW 1 — THE TICK

**The unit is a season. Every person and every cohort commits exactly one act.** An act is not
everything a person does in three months; it is the one discretionary commitment. Subsistence, craft
and travel-in-progress happen *to* you in P1 (`09 §1.1`).

**Within a phase everything is simultaneous — nobody in Phase 4 sees anybody else's Phase 4.**

| | phase | what moves, and who acts | **what CANNOT move here** |
|---|---|---|---|
| **P0** | **CALENDAR** | the date advances; due **standing dates** fire into a docket — Goldenfurt's tithe reckoning, the Kettlemakers' Masterpiece Examination, Hafenmark's Parliament sitting, a Dicastery's visitation, a truce's expiry. Option availability is recomputed from office, marks, place **and the claims each person holds** | **nobody acts.** No person chooses anything. A latent act enters an option set here and is not performed here — `09 §9`'s whole fuse mechanism is one recomputation and no decision |
| **P1** | **SETTLE** | the only phase that changes the world with no act behind it, and it is restricted to **metabolism**: larders consume against mouths, production resolves against Prosperity, wounds close or fester, bodies age and die, travellers advance a leg | **no social quantity whatsoever** — not standing, regard, grievance, cohesion, or commitment. This membership rule *is* the refusal of scheduled recovery (`09 §8.3`). There is no phase in which a restoring timer could run, so a design that wanted one would have nowhere to put it |
| **P2** | **NEEDS** | every person and cohort computes needs from its situation. Subsistence and the peer *set* read the world; commitment, exposure and the regard *values* read the view (`15 A-1`, narrowed by `A-1b`) | **nothing is stored.** A need cannot be stale relative to its own inputs, and is *supposed* to be stale relative to the world. No decision here |
| **P3** | **VIEW** | top **K = 12** claims by salience per person (`K = 7 + Focus`, ± Knots and Coherence in `03 §4`); K = 3 per cohort, from the channel claims at its address | **no claim can be surfaced that is not in the ledger.** An empty ledger yields ignorance, not uncertainty — the option leaves the act list (`03 §4.1`). Motivated reasoning attenuates *retrieval*, never value |
| **P4** | **CHOOSE** | `choose(person, view) -> act`, everyone, against the frozen P1 snapshot and their own ledger. **The player's submission enters here and nowhere else. An NPC's choice enters here too, through the same function.** The player's only advantage is deliberation time | **no world argument, ever.** Not for the player, not for an NPC. No reaction to anything happening this season. No faction verb — a faction has none (`07 §2`); what looks like one is a person plus an attribution claim |
| **P5** | **RESOLVE** | `resolve(acts, world) -> events` — **the only writing phase**, and the only consumer of the true faction profile. Strata below | **no agent reads anything here.** The world sees everything because that is what the world is for (`15 A-5`); no person does |
| **P6** | **WITNESS** | events fan out by **presence and channel**; `witness(person, event) -> claim*`, one person at a time, depositing divergent construals. Tellings resolved in P5 land here as deposits in the hearer | **no consensus deposit** — structurally unavailable, because no function's signature permits it. A cohort deposit carries a *distribution* over construals, never one shared value (`16 §5`) |
| **P7** | **RECKON** | claim confidence decays; ledgers over **L = 200** evict lowest salience (this is forgetting, not a data limit); cohorts whose stance spread widened individuate; persons nobody remembers de-individuate | **the only clock-driven quantities in the game are matter, bodies, and the confidence of a memory.** Nothing social recovers, decays or upkeeps here either |

## The negative half is the design

Three refusals live in phase membership rather than in discipline, which is why they hold.

**No scheduled recovery.** Standing, regard, grievance, cohesion and commitment move only when an act
causes an event. Enforced by P1's membership: there is no phase where a restoring timer could run.
Consequently a governor does not decay on a timer — **he loses Goldenfurt by being forgotten**, because
`chain` counts only links whose subordinate's ledger *currently asserts* who decides here, and claim
confidence decays under the same universal rule that governs every memory (`09 §7`).

**Surprise is structural.** Reaction latency at person scale is one season. If the praefect opens the
granary to the Row and not the hamlet, the hamlet's answer is *next* season's act. No policy can say
"if he does X, I do Y, this turn." **You anticipated or you are late.** The one exception is the nested
loop: inside a contest the tick subdivides into **exchanges** running P3–P6 over a smaller person set
on a shorter clock — a battle, a Doctrinal Adjudication hearing, the Masterpiece Examination committee
and two brothers arguing over a barn are the same call with different act vocabularies.

**No hidden turn order.** Two acts conflict iff they share an object and either mode is `exclude` or
both `alter` the same field; conflicts route to `contest(container, prize, claimants)`. **Ties break
on a hash of (act-id, world-seed) — never on rank, office or list position**, because a rank-ordered
tiebreak is a hidden power stat that never appears on a factor sheet.

## The strata inside P5, and why they are ordered so

| | stratum | why it is here |
|---|---|---|
| 1 | **Movement** | presence first, because every stratum below asks who was there |
| 2 | **Binding decisions** — rulings at docket dates, dispensations issued | these change **terms**, and a ruling made at the court's sitting is by construction the frame for the season |
| 3 | **Contested physical acts** — violence, seizure, blockade-running, a march | they happen inside the terms just set |
| 4 | **Uncontested material acts** — work, build, carry, arrive | |
| 5 | **Social acts** — `tell`, `carry`, `argue`, `admit`, `commit`, `vouch`, `submit` | last, because they are *about* what happened. **This is what makes a season's gossip be about that season's deeds** |

That ordering is load-bearing beyond flavour: `09 §8.4` uses it as the composition convention for any
stance move in a season — accrual (strata 2 and 4) applies before mitigation (stratum 5), because
mitigation is answering and cannot resolve before the thing it answers. From a fully aggrieved floor,
maximum accrual then maximum mitigation nets **+3.02 per season** — recoverable in roughly two seasons,
at a price of sixteen act-slots, which is essentially a settlement's whole governing capacity.

**The tick's own gaps, for the record.** There is no phase in which an off-board polity acts without a
person; there is no phase in which a container decides; and P4 gives a King and a hamlet fisher exactly
one act each — the King's advantage is entirely in `own_acts` and `seat_items`, never in act count.

---

# VIEW 2 — THE RUNG VIEW

Eight rungs against the eight modes of play. **Off-board is split inside each cell**, because the
distinction between *an off-board person the model holds* and *an off-board polity with no person* is
where the design's one declared open question lives.

## Table A — Material · Epistemic · Political-up · Political-down

| rung | **Material** | **Epistemic** | **Political-up** | **Political-down** |
|---|---|---|---|---|
| **Individual** | **NAMED** — work (hands into the larder), *take an opening* (the recomputed `opening_set`: a smuggling run priced by `EV = (price(dest) − price(orig) − transport) × volume − p(interception) × penalty`), `forestall`, hoard (an absence of release), `settle_in_full`, `migrate`, theft as `Force(seize, warrant none)` | **NAMED, richest cell in the design** — `examine`, `interview`, `research`, `surveil`, `reconstruct`, **Thread-Read**, plus `tell` / lie (four deltas: lie, overclaim, false witness, invention) / `plant` / `cover` / passing / `counsel` through a Knot. Every one available to any person; eligibility never consults office | **NAMED** — raise a `petition`, `back` public or concealed, `supplicate`, withdraw. Gated by form: `gap ≥ 3` means supplication only, carried, through an intercessor whose own gap is ≤ 2 | **NAMED at the receiving end** — comply, comply badly (`will` 0.30–0.50), quiet evasion, open defiance, and **refract**: retelling a dispensation is an ordinary `tell`, so terms drop before values distort. **`issue` is not available: no remit** |
| **Hearth** | **NAMED, and it is the generator** — `stores`, `draw`, `mouths`, `margin` in mouth-seasons; `holdings`; requisition kin; dowry; foster out; `distrain` as a creditor; arrears; banked claims | **THIN** — the hearth owns transmission across time and **owns no epistemic act**. Dormant grievance rows and suppression scars are inherited by a rule nobody performs (`floor(scars/2)`, magnitude preserved); telling a grievance to children is an ordinary `tell`. A document kept at a hearth is found by an ordinary `search` | **N/A, by construction** — the hearth is not a respondent container. It has no seat, no convener, and (`15 B-4`) its larder reckoning is **not a standing date** because it allocates nothing among claimants. An unmet need inside a hearth is answered by `requisition`, which is Relational | **EMPTY at the issuing end** — `06 §1` admits Hearth as a legal dispensation *scope*, and **no office in the whole post roster has hearth scope**, so nothing can be issued there. The hearth head's instrument is an ask that may be refused |
| **Community** | **THIN allocator** — real stakes (workshop rights, the guild's market share, its burgher seats; the commons and fishing grounds; the granary share the hamlet is last in line for) allocated only by the generic `contest`, plus a guild warden's dues-reckoning `LevyTerm`. The exclusive "never both" allocation rule is written for the *settlement* | **NAMED** — the **judging set** is the default hearing mechanism (`hears` by presence, ambient publicity above θ, one Knot hop, or a telling); publicity = `venue_factor × √witnesses × mark_salience`; **common voice** is admissible at G0 on a candidate's fitness; the guild register is a custody | **NAMED** — carry into the elders' sitting or the guild board; the warden or elder is the convener and composes the agenda | **NAMED, with a flagged structure** — a guild warden `issue`s an `EntryStandardTerm`, binding **members-by-admission** only. `14 §11.1` flags that the substrate puts office first at Settlement; if that is upheld, wardens and priests become conveners with agenda power and **no remit** |
| **Settlement** | **NAMED, richest material rung** — the granary opening at the tithe reckoning, allocated **exclusively** (highest-scoring claimant takes the full stock before the next sees a measure); the market's stalls; the levy exemption; the assize of bread as a `PriceTerm` | **NAMED** — the crier; the praefect's roll as record custody; market gossip; the settlement court's admissible sources (firsthand plus oath-helping, *n* independent G1 roots → G3) | **NAMED, the worked case** — `carry`, `forward`, `amend`, `bundle` (conjunctive or generalizing, which converts PRIVATE → COMMON), `drop` stated or silent, and lapse, which is nobody's act at all | **NAMED, richest** — `issue` binding **persons-by-presence**: `ProhibitionTerm`, `OrdenanzaTerm`, `ExemptionTerm`, the granary allocation; `determine` at the court; the gate |
| **Territory** | **NAMED** — the reckoning rate set at the territory court; levy `apportion(node, quota)` at every rung by a named person; `import_flow` along routes that exist because a person judged them worth carrying | **NAMED, and the best mechanism in the suite** — `dispatch` buys *fidelity*: a node nobody reports from produces no firsthand claims, so it is **literally a cohort in the office-holder's ledger**. Relay hops reset distortion; folk hops compound it | **NAMED** — the Grauwald territory court hears eleven items against seventeen seatholders; the ducal proxy holds `compose_agenda`, and an omitted petition **is a drop and deposits as one** | **NAMED** — the reeve; publication with or without enforcement; the **Territory Reach Cap**, which is not a distance term but a count of riders |
| **Province / Duchy** | **NAMED** — duchy-scope `LevyTerm`, `BlockadeTerm` (the Grauwald coast closed to salt), the ducal mine's `base(H)` depletion, a dredging levy voted down a generation ago and silting a harbour ever since | **NAMED** — the ducal household channel (chamberlain → steward → Duke), where `filter_share` is derived volume and an under-steward at 0.6 **structurally outranks ministers while holding no standing whatever**; a retained Parliament is a second, competing channel | **NAMED** — the Hafenmark Court Parliament; **remonstrance**, requiring standing at an institution with a registered right, and its four-step escalation ladder (remonstrance → letter of command → iterated remonstrance → session of enforcement in person) | **NAMED, richest** — the full term vocabulary at duchy scope, plus `convene` and the ordering of items, which kills a petition with seat capacity rather than with a refusal |
| **Realm** | **NAMED but thin by arithmetic** — the general-scope dispensation and the Crown household's own stake. **The largest remit in the peninsula has the thinnest reach per node**, so *a King's decree is the least enforced instrument in the game*; levies must be **asked** for, because the territories' stakes are held by ducal offices the Crown did not confer | **NAMED, and the largest power in the game** — the Church's archival monopoly: the **Dicastery of Doctrine and Archives** holds custody of the instruments on which everyone else's G4 grounds rest. Three channels reach the Crown (household, a Grandmaster reporting on her order's own matters, the Confessor) and a dynastic fight is over which one a claim about an heir travels down | **THIN for anyone below a duke** — the Realm's seats are three ducal proxies, four Cardinals and the Crown. **There is no mid-rank mass to coalesce**, so a demand that must reach the Realm has no route but through one of eight persons, and `16 §4.3` records that the drop's counterweight is elected-seat-shaped and does not bind appointed office | **NAMED** — the general-scope dispensation; the realm's standing dates; `ExcommunicationTerm` from a realm-scope cluster |
| **Off-board** | **NAMED through a person** — Doux Alexios Laskaris issues in his own court; Schoenland waters supply the salt a blockade makes profitable; Altonian grain ships and the Almud Free Bond. **EMPTY without one** — no mechanism lets an off-board polity move a price, a route or a levy with nobody carrying it | **NAMED through a person** — a returning merchant-captain's firsthand claim through his own guild's channel is what *constitutes* a treaty breach; Prince Torben's presence is a claim source. **EMPTY without one** | **NAMED only with an envoy** — sending Elske to Almaic Kyriakos **makes the Doux a legal respondent** for Almud's merchants, and nothing else does. **EMPTY otherwise**: with no envoy there is no off-board respondent, and no up-stroke runs *from* off-board into the peninsula at all | **NAMED through a person** — Alexios's `ProhibitionTerm(leave_court)` reaches Torben, who holds no office and signed nothing. A treaty is two office-holders issuing jointly. **EMPTY without a person** |

## Table B — Argument · Coercive · Relational · Institutional

| rung | **Argument** | **Coercive** | **Relational** | **Institutional** |
|---|---|---|---|---|
| **Individual** | **NAMED, and THIN for the excluded** — `plead`, `press`, `descend`, `produce`, `object_to_venue`, `yield`, plus negotiation's `propose` / `counter` / `probe` / `withdraw` / `execute`. **Exclusion in Valoria is at the second gate, not the first**: a Southern Einhir fisher may walk into the Goldenfurt court and may not *speak* unless a person with standing carries him. The room is open; the floor is not | **NAMED, and open to everyone** — `Force(actor, targets, form, warrant)`, form ∈ seize · restrain · strike · burn · expel · disperse · kill, warrant ∈ office · custom · none. The duel, the barn burned at night, the knife as a cadet's sixth exit, and `refuse_levy` | **NAMED, hard-gated** — `form_knot` needs Disposition +5, Bonds ≥ 5, a free slot (`floor(Bonds/2)+1`) **and TS ≥ 30 on both sides, so roughly half the peninsula can never form one**; `counsel`, `invest`, rupture. Ordinary ties carry tellings and are ungated | **N/A, with one exception** — `confer`, `revoke` and `determine` require a remit. The single institutional act a person with no office holds is `convene`: *he can call his kin to a table* |
| **Hearth** | **EMPTY — a real prize with no room** — the seat is contestable at a vacancy standing date and **the venue tables contain no hearth venue**. `04 §1.3`'s third branch is exactly the absence of one: *two or more claimants and no office binds them → held by whoever physically holds it, re-opening every standing date.* **That branch is "there is no venue," and it resolves to war** | **THIN** — the hearth's coercive instruments are `refuse_levy` and naming *which member goes*, which is how a grudge gets a man killed at no cost to the man holding the grudge. There is no hearth-level force object, correctly, since force is a sum over persons | **NAMED, richest relational rung** — marry, `found_hearth`, foster out (a 1.5 edge **both ways**), dowry, disinherit (which removes the seat and **not the name**, generating the pretender), legitimate (an assertion, therefore forgeable), `requisition` on an asymmetric edge — main line → cadet 2.5, cadet → main line 1.0 | **NAMED, and strangely shaped** — the seat's transfer is cognatic-senior, gender-blind, capability-weighted. **It is the one conferral in the game performed by nobody**: a presumption, rebuttable at a venue. `14 §1.5`'s last two rows — Duke and King, conferred by *nobody living* — are this case escalated to a realm |
| **Community** | **NAMED, richest** — the **Masterpiece Examination** (floor G4 on the work, **G0 on the candidate's fitness**, which is how caste is reproduced by a parameter rather than by malice); the **Löwenritter chapter sitting**, which hears **witnessed deed only** and is therefore caste-open in fact rather than by policy; the Restoration consensus cell (G0, unanimity, one member blocks, no record custody) | **NAMED** — `Hold(n, targets, giver) = Σ reach(p) × will(p, …)` over `armed_present`, which includes forty Kettlemakers who own billhooks; a guild's discipline of its own (`strike`/`expel`, warrant `custom(guild grade)`); exclusion | **NAMED, richest** — `admit(committee, candidate, community)` with `(α, β, γ, δ)` **weights that are never signs**: guild α = β = 1.0 (bias exactly cancels excellence, fixable by attrition); Church α = 1.5 with a *single* assessor (a Southern Einhir Canon is one man's attributable exception, which is the definition of a scandal); Löwenritter β = 3.0 (the deed drowns the mark); Niflhel δ = 1.5 (caste-open through a recruiter's instrumental need); Restoration α = 0.0 with a unanimity block. Plus exclusion, which does not remove the man — **an excluded member is a leak with no loyalty** | **NAMED** — the Free Masters confer the wardenship at a sitting (merit, revocable by the same sitting); a Cardinal confers a benefice (patronage, revocable by that Cardinal); three sworn brothers confer a chapter mastership on **deed**; editing the community's `(α, β, γ, δ)` vector is itself a dispensation, and it is Duke Vaynard's whole Path B |
| **Settlement** | **NAMED** — the Goldenfurt settlement court: enter = anyone present, speak = office-holders and any person **carrying** a petition, decide = the praefect determines with assessors' stances weighting it, floor G1 with oath-helping | **NAMED, richest** — the watch; `disperse` with warrant `office`; arrest as `restrain`; the gate. And the finding that governs the rung: **`sever` makes locally-raised force structurally unable to suppress locally** — twenty watchmen are `Hold ≈ 12` against the hamlet and `≈ 36` against a market riot, from the identical roster | **EMPTY, and it is a hole** — the settlement has **no admission gate and no judging set of its own**; both are community mechanisms. So at the rung whose stake is genuinely zero-sum, there is **no consensual membership operation at all**: nobody can be taken into a settlement, and the only way out is `expel`, a *coercive* act. An outsider at this rung is fully bound by every dispensation, because scope is presence, and structurally mute, because the up-stroke needs a person | **NAMED** — the praefect confers the gate wardenship (patronage, his determination, δ = 1.5); the court's own sitting confers the magistrate; the praefect convenes the court and orders its items |
| **Territory** | **THIN — the venue is unparameterised** — the Grauwald territory court has seat weights (ducal proxy 5, praefects 2, Free Masters 1, Church 3) and an item capacity of eleven, and appears in **neither** `08 §10`'s chamber table **nor** `14 §5`'s venue table. It has no stated admission floor, decision rule, admissible source, coupling depth, veto or record custody | **NAMED** — apportionment at every rung by a named person whose stances read the children's marks; the garrison; dispatch. The refusal cascade is complete: absorb, coerce (which needs `Hold` against one's own neighbours, so usually cannot), or report the shortfall | **EMPTY** — no judging set, no admission gate, no Knot mechanism, no obligation edge. The only relational instrument that touches a territory is a marriage between the hearths of persons who hold offices there, which is a *hearth* act | **NAMED** — the territory office confers the reeve; `dispatch` on an establishment member; sub-remits carved downward |
| **Province / Duchy** | **NAMED, rich** — the Hafenmark Court Parliament: enter = seat-holders and their attendants, speak = seat-holders only, decide = majority of seats, floor G2, Crown instruments privileged, **the Duchess holds a veto that produces CARRIED-WITHOUT-FORCE** — a motion that changes no terms, is fully citable, enters later sittings at G4, and banks a permanent F2 contradiction hazard on the vetoer | **NAMED, richest** — the muster's two channels (levy through containment, retinue through alignment); the march, whose foraging is `Force(seize, warrant none)` against named hearths, so **you cannot march through the territory you are liberating**; the siege, ended by hunger or by one man at a gate; `battle_contest`, which never reads a faction id | **NAMED, but borrowed** — dynastic marriage, fosterage as collateral, banked claims, the ducal household. **Every one of these is a hearth mechanism performed by a person who happens to hold ducal office.** No relational mechanism is owned by this rung | **NAMED, richest** — `subremit(parent, acts' ⊆ acts, scope' ⊆ scope)`, which buys reach and **manufactures the sub-holder's shadow standing in the same act**; `confer`; `revoke` **within the conferral subtree only**; `convene` and the ordering of items |
| **Realm** | **NAMED, rich, one venue unspecified** — the Crown Succession Contest (article count **5**, each separately proved: descent · deed · consecration consent · no prior conceded record · the cognatic-senior capacity test); the four Dicasteries, each with its own floor, custody and veto. **The Crown's council is the unparameterised one**: enter = those the King summons, speak = those he names, decide = the King, admissible source = *whatever he will hear* | **THIN by construction, and deliberately** — the Crown may issue a general levy and must **ask** for the men: territorial stakes sit with ducal offices it did not confer, and the Löwenritter's conferral root is Grandmaster Sigrid Ehrenwall, whose oath runs to **Crown-as-institution**, which is why she may lawfully refuse the King. Separately: **the Church cannot fight** — the Defense of the Faith's only military path is requisitioning a Templar from a basis two rungs up and marching him in, which converts a police matter into a caste incident | **THIN, borrowed again** — conclave, consecration and dynastic marriage. The relational play at Realm is hearth play with larger stakes | **NAMED, and defined by what it cannot do** — the Crown confers **appointed** offices (praefectures, provincial governorships, its own reeves) and sets the realm's standing dates. It **cannot revoke a duchy** (it did not confer it), **cannot revoke a benefice** (the path runs to a Cardinal), and **cannot consecrate itself** (the root office's warrant is external and sits in Church custody). `sovereign_fraction(root)` is a query over a graph, currently low |
| **Off-board** | **THIN** — cross-realm argument runs only through the private negotiation venue (`container = none`, judging set = the parties, unanimity, both veto, floor G1, no record custody unless an instrument is executed). **There is no chamber with a foreign container** anywhere in either venue table, so a dispute between the Realm and Altonia has no forum and no third-party judging set | **EMPTY for a polity, NAMED for a person** — `12 §7` is explicit that Altonia's leverage over Prince Torben "has no military expression at all". An off-board polity's coercion reaches the peninsula only as persons who came, and no mechanism supplies them | **NAMED, and the two instruments that reach here are both relational** — hostage/fosterage (a containment address moves into the counterparty's scope) and marriage (two hearths' succession pointers edited, breach undoable). Nothing else in the binding-instrument table crosses the map | **EMPTY as reach into the peninsula** — Himmelenger's offices root wholly in the Church and Schoenland's root **outside the peninsula entirely**, which is stated as a fact about the sovereignty fraction and given **no mechanism by which that external root confers, revokes or acts**. An off-board person may confer freely inside his own court |

## What the matrix says, before the seasons are written

**The Hearth and the Community are the richest rungs for a person with no office**, and the design
knows it. **Settlement and Territory are where the rung view thins**: the Settlement owns the most
contested material stake in the game and owns no membership operation; the Territory owns *reach*,
which is excellent, and owns nothing relational and no parameterised venue.

**The Realm rung is thin in exactly two modes and rich in two others.** Political-up and Coercive are
structurally thin there — eight carriers, no mid-rank mass, and an apparatus the Crown must ask for.
Epistemic and Institutional are the richest cells in the design, and they belong to the Church rather
than the Crown, because custody of the instruments and the root of the conferral graph are the two
positions that scale.

---

# VIEW 3 — THE ALIGNMENT VIEW

A faction is **a proposition plus a map from persons to a degree of commitment**. `Edge = (person,
faction, degree, avowal, since, cause)`. Edges live on persons; membership is a query. There is one
operation, `commit(person, faction, Δdegree)`, run in both directions.

## Degrees, and what each licenses

| d | name | `w(d)` | what it licenses | what it costs to refuse |
|---|---|---|---|---|
| 0 | none | 0 | — degree 0 *is* deletion; departure needs no operation | — |
| 1 | sympathy | 0.15 | will not testify against a member; may be told cell-safe claims; stance weight applies at view assembly | nothing; nobody has asked |
| 2 | sympathiser | 0.40 | may be asked for material, shelter, carriage at low cost; may `carry` a petition of the faction's proposition | refusal at **low** burden drops the edge a degree |
| 3 | member | 1.00 | may be **requisitioned** for acts inside their ordinary capability; may `avow` | as above, and the refusal is now visible to the asker |
| 4 | sworn | 1.60 | may be requisitioned for acts **against their own container's interest** | **refusal is witnessed by every d ≥ 3 member** |
| 5 | constitutive | 2.20 | the proposition holds a Conviction-primary slot; **no offer term enters the refusal check at all** | refusal is a **Coherence event** |

**The ask is one function, and the licence is priced continuously by it:**

```
requisition(asker, member, act, node)
  obstacle = base(act) + burden − 2·w(d) − regard(member→asker)/2 − conviction_bonus
  burden   = cost to the member's computed need
           + 2 · harm to the member's container's stake
           + 3 · marks the act collides with
```

Refuse at **low** burden and the edge drops a degree; refuse at **high** burden and it does not — so a
faction asking the impossible loses nobody, and one asking the trivial and being refused has learned
something true. Nobody buys Odd Uln off his oath, not because the number is large but because **the
offer term is absent from the formula**.

⚠ **REPORTED, NOT RESOLVED — the licence column is live in two contradictory states.** `07 §1.2` ships
the table above as a gate. `16 §2.2` **cuts the column and keeps the degree**, on the ground that the
obstacle formula already prices asks continuously and the two copies can disagree — the table forbids
requisitioning a sympathiser outright while the formula would clear one at high regard. What survives
the audit's cut is exactly two discrete things: **degree 5's absent offer term, and the avowal gate.**
Both documents are in the suite. A season that leans on a degree-2 refusal being *illegal* rather than
*expensive* is standing on the contested half.

## Degree × avowal

| | **avowed** | **private** | **covert** |
|---|---|---|---|
| **what makes it so** | an act deposited the membership claim into the person's judging set by the ordinary witnessing path | no public claim; discoverable by witnessing a requisition honoured, or by being told | members additionally perform concealment acts and may `tell` a **cover claim** — an assertion of a different edge, or of none |
| **d 1–2** | raises every observer's *estimate* at a node **without changing capacity by one point** — this is what the Restoration's presence markers are, and it is a real fork with a real cost | the ordinary state of a sympathiser: bread slipped, nothing said | cheap and nearly free; the shallow end an informer is recruited from |
| **d 3–4** | Duke Vaynard commits at degree 4 to *(the caste order ought to be broken)* **at publicity 2.0** and pays for it in every Crown-Latinate quarter's judging set at once | the interesting middle: capacity exists, exposure is derived and rises only under investigation | **bounded by Knot slots.** A covert requisition needs a channel that deposits no claim into a judging set; ordinary asking is witnessable and a **Knot** is not. A person holds at most `floor(Bonds/2)+1` |
| **d 5** | the strongest and most brittle position: the proposition holds a Conviction-primary slot and every observer knows which one | **THIN — unworked.** A Conviction is a stance row at maximal generality, and stance is unreadable except through a claim, so a covert constitutive commitment is expressible. Nothing in the suite works one | as private, plus the concealment acts. Rupture of the Knot that carried it delivers the discovery through the channel the secrecy depended on |

## What discovery costs, and who pays it

**Exposure is derived, never stored:** `exposure(edge) = Σ over persons q holding a claim about it of
confidence(q's claim) × hostility(q → the proposition)`. It **rises only when an investigation spends
acts**, because acts are the only thing that puts claims in ledgers, and `P(discover | I) = 1 −
exp(−pressure(I,S) × exposure(S) / θ)`. **Exposure 0 → P = 0 at any spend** (a concealment you never
extract from is never found). **Spend 0 → P = 0 at any exposure** (the world does not audit you for
free). There is no clock on either side.

**And the cost of a discovery is computed from the observers, not from the secret.** One identical
discovery — *this man is Restoration at degree 3* — costs a Goldenfurt Free Master his committee seat,
costs an Oastad fisherman nothing because his neighbours are sympathisers already, and makes a
Southern Einhir Canon a scandal at Himmelenger, where marks and proposition collide in every observer's
table at once. One mechanism, three outcomes, no faction-wide reputation number.

## What covert forecloses

- **Office.** Every act by remit is performed at `venue_factor ≥ 1.0`, so an office-holder's judging set
  is the whole settlement. **An office-holder cannot act quietly.** A covert edge and a remit are close
  to incompatible — which is why Niflhel's recruiters hold no office and the Burned hold no post.
- **Scale.** Covert capacity is bounded by its members' **Bonds**, never by its presence — so
  **a national body cannot be run covertly**, and Niflhel is small on purpose. Because Knots gate on
  TS ≥ 30 and TS is heritage-correlated, a covert faction is necessarily Southern-Einhir-weighted:
  every formal institution gates them out and the deepest informal channel gates them in.
- **Being treatied with.** A body with no record custody and no office whose holder binds a member can
  execute nothing in the binding-instrument table except a hostage or a marriage — which is why the
  Restoration Movement cannot be treatied with, from an ideological commitment producing a mechanical
  fact with no rule naming it.

## The empty cells in this view

- **There is no un-avow and no recantation.** Avowal converts covert edges to avowed and `07 §6` says
  plainly *there is no un-avow*. Departure is degree → 0 with no operation — but the **claims** about
  the membership persist in every ledger that holds them, and no act retracts one.
- **A faction cannot expel a member.** `commit` is performed **by the person**. Nothing lets a faction
  set someone else's degree to zero. A cell that discovers an informer can kill him (`Force`), and it
  cannot remove him.
- **Committing has no stated price in act-slots.** Every person commits one act per season; whether
  `commit` consumes it is nowhere stated.

---

# VIEW 4 — THE OFFICE VIEW

```
Office  := (post, node, remit, conferral, revocation, establishment, seat_items, upkeep)
remit   := (acts[], scope_node, binds)
binds   ∈ { members-by-admission, persons-by-presence }
Holding := (person, office, since, conferrer)      # an edge on the PERSON
```

There is no office object holding a person. *Who holds the praefecture of Goldenfurt* is a query, and
**nothing anywhere stores control.**

## An office adds no verb

`remit.acts` is drawn from a closed set of **five**, each an ordinary act made eligible somewhere it
otherwise is not: **issue** (a `tell` with terms), **determine** (one person's decision at a venue whose
decide rule names him), **confer / revoke** (`admit()` and its negation, over an office), **dispatch**
(`requisition` on an establishment member), **convene** (setting a standing date and ordering its items).

**Two substitutions, and no third thing.**

- **OPTION SET.** `eligible(p, act, n)` consults the remit. The praefect can `issue` at Goldenfurt;
  Torben the fisher cannot. **Neither of them rolls differently for anything.**
- **POOL SOURCE.** When an act is performed by remit, the pool is drawn from the **establishment** —
  the named persons the office employs — not from the holder: `pool(act by remit) = capability of the
  dispatched establishment member(s) actually performing it`. Duke Vaynard's Focus is irrelevant to
  whether the Grauwald levy is collected; the pool is the reeve's, and the reeve has a larder, a stance
  toward Vaynard, and kin in the hamlet he is collecting from. **Choosing which of your people performs
  the act is the whole of a leader's tactical choice, and it is a choice between pools.**

**Why never a modifier, in one line of arithmetic.** A flat shift of size X on a pool roll is worth
`X / (0.671·√Pool)` — **more to a small pool than a large one** — so a flat office or leader bonus is
systematically worth more to the weaker side, backwards from every intent anyone has when adding one.

## Four remits, concretely

| | **Praefect** (Goldenfurt) | **Guild warden** (Kettlemakers) | **Cardinal** (one of four) | **Duke** (Vaynard / Baralta) |
|---|---|---|---|---|
| node · binds | settlement · **persons-by-presence** | community · **members-by-admission** | realm-scope cluster root · **members-by-admission** | duchy · **persons-by-presence** |
| conferred by · basis | the Crown · patronage | the Free Masters at a sitting · merit | the Confessor · patronage | **nobody living** — deed at the Secession War + kinship |
| revocable by | the Crown | the same sitting | the Confessor, at a Dicastery venue | **not revocable** — only contested at a venue |
| establishment | the watch, the granary keeper | the guild's beadles | a Dicastery's whole graph | household, provincial appointees |
| what the remit ADDS | `issue` over Goldenfurt (assize of bread, prohibitions, the granary allocation at the tithe reckoning); `determine` at the settlement court; `confer` the gate wardenship; `dispatch` the watch; `convene` the court and order its items | `convene` the Masterpiece Examination and order its items; `issue` an `EntryStandardTerm` and the dues-reckoning `LevyTerm`; `determine` at the guild board; `confer` grades by admission | `confer`/`revoke` benefices and canonries **down the whole cluster** — the power no container has; `determine` at his own Dicastery, with the Confessor holding a veto; `convene` the visitation or the summons; `issue` (the tithe `LevyTerm`, an `ExcommunicationTerm`) | `issue` over the duchy subject to reach; `determine` at any venue naming him; **`subremit`** and `confer` it; `dispatch`, which also buys **fidelity**; `convene` and order the items; four seat items at the Realm |
| what the pool becomes | the watch's, the granary keeper's, the reeve's. Where Goldenfurt resists a shock, the Order roll draws Focus/Acuity **from him on the φ fraction**, where Φ is *administrative* cohesion — do the ward-holders' ledgers currently name him, has he been present, does he speak Einhir | the beadles'; and at the Examination, the eleven Free Masters' own votes, which he does not cast | the Dicastery's assessors, registrars and Canons; the archival Cardinal's real instrument is **custody**, not a pool at all | the reeve's, the riders', the household's — never his own |
| what it **cannot** add | a bonus to any roll; the fact of being obeyed (binding power is *observed compliance*, and one public refusal lowers sixty people's willingness); `Hold` against his own neighbours; the power to revoke a benefice | anything over the Einhir hamlet outside the wall — his decisions reach **nobody who did not consent at a gate**; no arrest, no levy on non-members. `14 §11.1` flags that his office may not exist at all if the substrate's "office first at Settlement" is read strictly | **an army** — the Church of Solmund cannot fight; and **an owning node**: *"the Dicastery decided"* is permanently inexpressible, so a petition must be addressed to a **person**, who can drop it | **reach** — nine dispatchable persons against twelve settlements means four get publication without enforcement and compliance craters structurally; the power to revoke a benefice; the power to make a levy collect itself |
| what an equal person **cannot** do | allocate the granary exclusively; put an item on the court's list or keep it off; make the gate wardenship somebody's | set the Examination's agenda and its entry standard — **the convener holds the cheapest real power in the game**, spending nothing and killing a petition with seat capacity | confer a benefice, and therefore hold the patronage tree whose cut fans out into N simultaneous demotions | carve a remit and confer it — **and manufacture a rival's shadow standing in the same act** |

## The two binding kinds, and the cluster

**`binds = members-by-admission`** means the bound persons walked through a gate and consented there —
the Masterpiece Examination, a benefice, a chapter's oath. **`binds = persons-by-presence`** means the
Einhir hamlet outside the wall, which admitted the praefect to nothing. Settlement is where office
*first* exists in the substrate's sense because it is the first rung whose stake is zero-sum across
communities that did not admit each other — the first place binding-by-presence is a coherent thing to
want.

**An office cluster** is `{ o : conferral_path(o) reaches root }` — a query, never a stored set. It has
**offices and holders, not members**; its distinctive power is that **the root can `revoke` down the
whole graph**, which no container can do; its distinctive vulnerability is the patronage cut, which
voids every conditioned contribution in one event. Valoria's clusters: the four **Dicasteries** (roots:
four Cardinals); the **Löwenritter** (root: Grandmaster Sigrid Ehrenwall, warrant from
Crown-as-institution rather than from the King personally, **which is why she may lawfully refuse
him**); a guild present in three settlements (root: the mother chapter's warden); and **Niflhel**, whose
conferral graph is itself concealed, so that discovering *who appointed whom* is the investigation that
unmakes it.

And the jurisdictional politics is free: a cluster office sitting at a containment node whose own
office-holder did not confer it **is** the argument system's fourth stasis rung — *this chamber may not
hear it*. Nobody wrote a jurisdiction system.

## What holding costs

**Publicity** (every act by remit at `venue_factor ≥ 1.0` — an office-holder cannot act quietly),
**seat items** (holding two offices does not double a day), **upkeep** (an unpaid establishment does not
disperse; it becomes a faction and treats plunder as wages), and **licensed standing**:
`licensed_standing` is the part of your support set routed through the post, `shadow = standing −
licensed_standing`, and a man with a large office and no personal following has `shadow ≈ 0` and
**cannot survive losing the post**.

## ⚠ THE CONFERRAL DILEMMA — reported, not resolved

> **Is conferral rooted in persons or in offices?**

**Person-rooted:** dead conferrers terminate the graph, the sovereignty query that all five factions'
victory conditions operate on is undefined across most of it, a praefect becomes as irrevocable to the
next king as a duchy is, and **the Crown cannot be played across a succession.**

**Office-rooted:** the graph resolves, but an institution performs the game's most consequential act,
which ruling `B-11` forbids outright.

**The suite asserts both and resolves neither.** Its own evidence for the office-rooted answer is the
Löwenritter oath — sworn *to the Crown as institution, not the bloodline* — a warrant that means
nothing if conferral is personal. Two defensible answers, materially different games. **Every season
that turns on a revocation, a warrant, or a succession is standing on this.**

Five further items in `14 §11` and `16 §4.3` bear on this view and are likewise open: office's
existence at the Community rung; whether the conferral coefficient vector sits at the conferring office
or the container; whether doc 08 or doc 14 owns a venue's door; whether Province and Duchy are one role
or a fixed ladder; and **whether a cohort may be conferred an office** (a village that appoints "its
elders" with no named person has no mechanism, and `14 §11.6` says so).

---

# THE CELLS I COULD NOT FILL

Ranked by how load-bearing each is.

1. **Off-board × Material, Epistemic, Political-up/down, Coercive, Institutional — EMPTY without a
   person.** The design's own declared open question. Most load-bearing because Altonia and Schoenland
   exert real pressure from off the map, `sovereign_fraction`'s denominator includes Himmelenger and
   Schoenland, and **Schoenland's offices are stated to root outside the peninsula with no mechanism by
   which that root acts.** "Generate a person" and "allow an actorless pressure" are different games.
2. **Institutional × Realm and × Duchy — the conferral dilemma.** Not empty; **ambiguous**, which is
   worse, because everything at Settlement and above reads it and both readings are in the tree.
3. **Relational × Settlement and × Territory — EMPTY.** Two consecutive rungs with no admission, no
   exclusion, no judging set, no obligation edge, no Knot mechanism. At the rung whose stake is most
   contested, the only membership operation is `expel`, a **coercive** act. Nobody can be *taken in* to
   a settlement.
4. **Faction expulsion — EMPTY.** `commit` is the member's own act, so a faction cannot remove anyone.
   An exposed informer can be killed and cannot be expelled, and the suite never says that is the
   answer.
5. **Argument × Hearth — EMPTY room for a real prize.** The seat is contestable at a vacancy and there
   is no hearth venue anywhere in either venue table. `04 §1.3`'s third branch *is* the absence of a
   venue, and it resolves to war — which means every succession with no binding office-holder skips the
   entire argument layer.
6. **Argument × Territory, and the Crown's council — THIN, unparameterised.** The Grauwald territory
   court has seat weights and an item cap and appears in neither venue table; the Crown's council's
   admissible source is *whatever he will hear*. Two of the rooms where the largest stakes are decided
   have no stated floor, decision rule or custody.
7. **Political-up × Realm — THIN.** Three ducal proxies, four Cardinals and the Crown: no mid-rank mass
   exists to coalesce, so a demand reaching the Realm passes through one of eight persons — and
   `16 §4.3` records that the drop's counterweight is elected-seat-shaped and **does not bind appointed
   office**, which is exactly the Crown-appointed praefect the worked example uses.
8. **The commitment-degree licence table — LIVE IN TWO STATES.** `07 §1.2` asserts it; `16 §2.2` cuts
   it. A season that treats a degree-2 refusal as *illegal* rather than *expensive* is on the contested
   half.
9. **The un-avow / recantation gap — EMPTY.** No act retracts an avowal; departure is degree → 0 and
   every claim about the membership survives it, in ledgers nothing can reach.
10. **The testimony half of the salience floor — OPEN by ruling.** A firsthand claim gets a floor;
    testimony stays clamped. Since a sixty-year-old revelation out of the Dicastery of Doctrine and
    Archives **arrives as testimony**, this bears on the entire Epistemic column at Realm.
11. **Epistemic × Hearth — THIN.** The hearth owns transmission across time and owns no act: dormant
    rows and scars are inherited by a rule nobody performs.
12. **Political-down × Hearth — EMPTY at the issuing end.** Hearth is a legal dispensation scope and no
    office in the roster has hearth scope.
13. **Coercive × Hearth — THIN.** Refusal, and naming which member goes to the levy.
14. **Material × Community — THIN allocator.** Real stakes, no named allocation function of its own;
    the exclusive-allocation rule is written for the settlement.
15. **Relational × Province/Duchy and × Realm — NAMED but borrowed.** Marriage, fosterage and banked
    claims are hearth mechanisms performed by persons who hold high office. No upper rung owns a
    relational mechanism, which is why marriage is the only instrument that crosses the map.
16. **Argument × Off-board — THIN.** No venue has a foreign container, so a Realm–Altonia dispute has no
    forum and no third-party judging set; only private negotiation and its instruments.
17. **A cohort conferred an office — EMPTY**, and `14 §11.6` says it could not be closed from the spine.
18. **Individual × Institutional — N/A by construction**, correctly, with `convene` over kin as the sole
    exception. Recorded so no lane reads it as an oversight.
19. **Bookkeeping, but it will trip a lane:** the suite carries **two Aldwins at Goldenfurt** — Praefect
    Aldwin Storr (`14 §5`, `05 §4`) and Burgher Aldwin Roth the Kettlemaker (`09 §11`) — and `09 §8.4`
    additionally calls the praefect "Praefect Roth". Name the office, not the man, unless you have
    checked which document you are citing.
