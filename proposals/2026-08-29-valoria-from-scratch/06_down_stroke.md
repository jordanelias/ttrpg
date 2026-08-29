# 06 — The Down-Stroke (Dispensation, Publication, and Openings)

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: T6 / S-DOWN · Composes on `01_substrate.md` §5.2. Does not re-derive it, does not contradict it.
## Method: derived, not adapted. No prior design document, ruling, or existing module constrains it.

**The failure this document exists to prevent.** A prior attempt built an opportunity mechanism that
required an office and a budget to receive. A person holding no post could not be reached by anything.
Downward effects terminated in place-owned gauges — an "unrest" number ticking on a settlement record
— and never touched a person. This is the single most diagnostic test in the brief: **an opportunity
must reach a person who holds no post, and it must not be authored for them.** Everything below is
built to pass that test, and every object is checked against it before it is allowed to exist.

The substrate already gave us the shape (§5.2): a `Dispensation` travels by being *noticed*, and an
opening is *computed*, never stored. This document is the full specification of noticing — publication,
distortion, compliance, targeting, patronage, treaty, and reach — because "it travels by being noticed"
is a sentence, and a sentence is not a mechanism until something can be run.

---

## 1. The Dispensation object

`Dispensation(issuer, proposition, scope, terms)`. **Issuer** is a person holding office — or two such
persons, for a treaty (§7). **Scope** is a list of containment nodes (§1 of the substrate: Hearth,
Community, Settlement, Territory, Province/Duchy, Realm — Valoria's three Duchies fill the Province
rung, and "Duchy" is simply this setting's name for it; the rung is a role, not a class). **Terms** is a
list of typed deltas to what a container permits, costs, or requires. There is no bare "effect" field.
Every term is one of:

| Term type | What it changes | Real example |
|---|---|---|
| `PriceTerm(good, multiplier)` | the cost of an act involving *good* | Goldenfurt's assize of bread, fixing the loaf below its scarcity price through a dearth |
| `ProhibitionTerm(act, exempt_marks)` | forbids an act, except for marked persons | conscription order forbidding fishing-boat departure, exempt: Löwenritter-chartered vessels |
| `LevyTerm(fraction, base)` | extracts a share at the next standing date | the grain levy funding the Baralta Crown Claim's counter-armament, `0.15 × hearth larder` |
| `ExemptionTerm(act, marks)` | waives a cost or prohibition for marked persons | Vaynard's Examination-fee waiver for Southern Einhir apprentices |
| `EntryStandardTerm(gate_delta)` | changes an admission gate's marks-test | the Kettlemakers raising the sponsorship bar after a caste-transgression scandal |
| `ExcommunicationTerm(person_or_faction)` | strips Church-conferred marks and standing at every node in scope | the Dicastery of Doctrinal Adjudication against a Southern Einhir Canon |
| `BlockadeTerm(node_pair, goods)` | prohibits transit of *goods* between two nodes | Almud's fleet closing Baralta's port to Altonian grain ships; Duke Vaynard's coastal blockade closing the Grauwald coast to salt (§4) |
| `TreatyClause(terms, collateral)` | any of the above, issued by two persons, with an optional bound act (§7) | the Elske–Alexios marriage treaty's trade-lane terms |
| `OrdenanzaTerm(rule)` | a settlement's own standing market/conduct rule | Goldenfurt's market-day weighing ordinance |

- Closed loop: **producer** — an office-holder's act, or two office-holders' joint act (treaty);
  **carrier** — publication (§2), then witness/claim like everything else; **consumer** — every person
  whose scope-membership and presence intersect a channel, as a claim that reweights their own
  `opening_set` (§4).
- **N-line:** cut the typed-terms table and every downward effect degenerates into a modifier on a
  hidden formula nobody in the world could name — you lose the ability to say *which specific thing
  changed* and therefore the ability for a person to reason about it, evade it, or exploit it.

---

## 2. Publication as telling, with distortion

A Dispensation does not write into ledgers. It is **published**, which means the issuer spends acts
activating channels, and each channel is a chain of ordinary `tell(speaker, hearer, claim, as_asserted)`
calls — the same primitive that carries a lie between two neighbours. There is no separate "broadcast"
function; §6 of the substrate refuses one, and this document does not reintroduce it under a new name.

| Channel | Reach | Speed | Fidelity | Excluded |
|---|---|---|---|---|
| Crier | everyone present in the settlement's market this cycle | same day | low — a short, compressed public cry; loses every term but the headline one | absentees, hamlets outside the wall, the illiterate reading nothing extra |
| Parish priest | congregants | next sermon (weekly) | moderate, coloured by the priest's own stance (Confessor Himlensendt's telling of a caste ruling is not neutral) | non-attendees, other faiths, Southern Einhir hamlets under-served by the Church's own gating |
| Guild notice | dues-paying members and apprentices | posted immediately, read at next chapter meeting | high on literal text, but requires literacy and chapter attendance | non-members, journeymen without standing to attend |
| Market gossip | whoever is present, decaying with distance from the crying-point | fast, but decays over days | low, and falling — each retelling compresses and edits | anyone who was not there to catch it fresh |
| Institutional relay (Löwenritter riders, the Church's Dicastery of Temporal Affairs couriers) | one settlement per rider per season | days, node to node | very high — carries the written text | any node without a garrison or parish network: the western-fjord pockets, Grauwald's outer hamlets |
| Knot | exactly one person | near-instant | high, but still filtered by the speaker's own stance | everyone who is not that one person |

**Distortion is not a separate system.** Every hop past the first is an ordinary `tell` performed by
whoever just heard it, to whoever they next talk to — a person's own credulity, obstinacy, and stance
toward the issuer decide what they retain and what they editorialize, exactly as §3.1's salience ranking
already computes. Two facts fall out for free:

1. **Terms drop before values distort.** A hearer under time pressure or low relevance-salience keeps
   the headline term (a price, a prohibition) and sheds the qualifiers (an exemption, a sunset date, a
   scope boundary) first — because those are exactly the low-salience terms a compressed retelling has
   no room for.
2. **Distortion compounds with hop count and falls with institutional relay.** A relay hop resets the
   chain to a fresh, correct source; a folk-gossip hop degrades it further. This is why the periphery —
   exactly the Southern Einhir hamlets and western-fjord pockets the setting already marks as
   under-served — receives worse decrees than the Löwenritter-garrisoned core, without a single line of
   code mentioning caste.

- Closed loop: **producer** — the issuer's publish act, choosing which channels to fund at which nodes;
  **carrier** — chained `tell` acts, first professional, then ordinary; **consumer** — every person who
  receives a resulting claim, correct or not.
- **N-line:** cut channel differentiation and a Duke's decree and a smuggler's whisper become
  indistinguishable — the exact broadcast the substrate refuses, reintroduced under a publication label.

---

## 3. Decree-with-compliance

A published Dispensation does not apply. It lands, per relevant node, as a **compliance contest** —
the same `contest(container, prize, claimants)` function that already resolves sibling rivalry (§4.1 of
the substrate), instantiated with `prize = compliance-at-this-node` and claimants `{enforcement,
resistance}`. No second resolver is introduced; the survey's clearest refusal (never build a second
resolver) is respected exactly.

**What the roll reads:**
- **enforcer_presence(node)** — is a person in the issuer's employ (gate warden, tithe collector,
  garrison officer) actually stationed or dispatched here this cycle? Zero if the issuer has no one to
  send (§8).
- **local judging-set stance** — the community's aggregate stance toward the proposition, derived on
  demand exactly as §4 specifies ("no council brain"), never stored.
- **distance** — containment path length from the issuing node, which interacts with §8's reach limits
  rather than acting as its own decay curve.

**What a failed compliance produces — never an exception:**

| Outcome | What happens |
|---|---|
| Partial compliance | some hearths pay/obey, others don't — resolved per hearth, not per settlement |
| Quiet evasion | the person acts as if the term were not in force; produces no event unless witnessed |
| Open defiance | a public act contradicting the term — always witnessed by whoever is present, guaranteed |
| Local countermanding | a local office-holder issues their *own* Dispensation narrowing or blunting the first — an ordinary act, not a special case |
| Arrears | the unmet levy/prohibition compounds toward the next standing date, raising the stakes there |

This is the setting's own precedent already run forward: Grauwald's outer hamlets evading the Crown
conscription order is not a bug to patch, it is the capitulary record — the same abuse re-prohibited
because the last prohibition was never actually enforced past the settlements the Crown could reach.

- **N-line:** cut compliance and reinstate instant-global-decree — the single most common error the
  precedent survey names — and geography, garrisons, and the whole caste-and-periphery texture of the
  setting stop mattering to whether a decree does anything at all.

---

## 4. The opening — computed, never stored

There is exactly one routine, and it is the same routine that lists any person's available acts at any
time, not a new one keyed off Dispensations:

```
opening_set(person) = { act ∈ AllActs
                       : requires(act) ⊆ capability(person) ∪ marks(person) ∪ ties(person)
                       and EV(act | current_claims(person)) > EV(baseline | current_claims(person)) }
```

A Dispensation changes nothing about this routine. It changes `current_claims(person)` — one more row
in the ledger, deposited by publication (§2) — and the routine, run again, returns a different set.
**Worked case, the substrate's own:**

Torvald Fiskersen, Southern Einhir, no post, lives at the fjord's edge outside Stillhelm, on the
Grauwald coast. His fields: `capability` includes *owns a boat*; `ties` includes a Distant Knot with a
smuggler cousin in Schoenland waters. Duke Vaynard's blockade publishes:

```
Dispensation(issuer   = Vaynard,
             proposition = "cut Grauwald's salt supply",
             scope    = [Grauwald coast],
             terms    = [BlockadeTerm(node_pair = (Grauwald coast, external salt sources),
                                      goods     = {salt})])
```

**The term stops the flow; it does not name a price** — an earlier draft of this trace encoded the
blockade as `PriceTerm(salt, ×3.5)`, which is the issuer decreeing the *consequence* of his own act.
That is the authored outcome this whole document exists to refuse, sitting in the one trace built to
prove nothing was authored. A duke can close a coast. He cannot decree what salt will then be worth,
and the difference is the entire down-stroke.

The ×3.5 is therefore an **output**. Doc 13 §4 owns it: `price = base_value × demand/supply`, and the
blockade removes the `import_flow` term from Grauwald's `supply`. Grauwald's own coastal holdings never
produced salt (13 §2), so supply collapses toward zero against unchanged mouths and the local price runs
up to roughly 3.5× base over the following season — a number nobody wrote down, reached by a formula
that would have produced 1.8 or 9.0 from different holdings and would produce **1.0 in a settlement that
makes its own salt**, where the identical decree is politically inert.

The crier's cry reaches Torvald three days late and mangled (§2); his cousin's Knot-tell reaches him the
same night, intact. Before the claim landed, `EV(smuggling run) < EV(fish as usual)`. After it lands, he
runs doc 13 §4's carry EV over the route he can actually reach:

```
EV(run) = (price(destination) − price(origin) − transport_cost) × volume − p(interception) × penalty
```

**And the direction is INTO the blockaded coast, not out of it** — the earlier draft had him running
salt *to* Schoenland, which is backwards on its own numbers: salt is dear at home precisely because the
blockade made it scarce there, so the profitable act is to buy cheap in Schoenland waters and land it on
the Grauwald coast at ×3.5. A blockade is worth running *inward*. That is what a blockade is, it is what
every blockade in history has produced, and here it falls out of a subtraction rather than out of
anybody's intent. `opening_set(Torvald)` now contains *land Schoenland salt on the Grauwald coast*.
**Nobody authored this for him.** No opportunity object was created, targeted, or rolled for him; his
own capability, his own tie, and one new claim, run through the routine every person is already run
through, produced it — and Vaynard, who wanted Grauwald starved of salt, has manufactured the exact
incentive that supplies it.

**Explicit refusal.** This document does not define a `Quest`, `Opportunity`, or `Contract` object with
a `target_person` field. Such an object requires an author to decide, per person, that this is the
moment they get something interesting to do — which is exactly how a churning world stops churning and
turns back into hand-placed content. The opening is not offered. It is the ordinary consequence of
recomputing an ordinary routine over a world that changed.

- **N-line:** cut the recompute-on-claim discipline and the down-stroke dead-ends in place-owned gauges
  again — the precise failure this document exists to reverse.

---

## 5. Targeting order — a shock lands on named local actors first

E. P. Thompson's finding is not a rule to bolt on; it falls out of `witness` for free. A grain-price
spike caused by a distant levy produces two kinds of claim in a hamlet's ledgers: a **firsthand**
witnessed claim naming the local miller who raised his toll to cover it, and a **hearsay** claim, several
tells removed, naming the Duke who set the levy. Salience is `recency × confidence × relevance`
(§3.1), and a firsthand local claim beats a low-confidence distant one on every term. **Blame targets
whoever is closest in the witnessed causal chain, not whoever is actually responsible.**

Concretely: when Vaynard's grain levy (funding his counter-armament against Baralta's Crown Claim)
lands on a Row settlement, the tithe reckoning is performed by a named reeve, and it is the reeve's
public act — collecting, weighing, sealing the sacks — that every present townsperson witnesses
firsthand. Anger commits as grievance against **the reeve**, and against the grain merchant who was
seen forestalling stock ahead of the reckoning, long before it commits against Vaynard. This composes
directly with §5.1's petition machinery: a hostile faction forms and its first target is whoever the
salience-ranked claims name — the reeve — and only if the reeve is cleared, dead, or the underlying
scarcity persists past that does grievance route upward through a rejected petition toward the office
that actually set the term.

- **N-line:** cut this and every downward shock becomes an abstract "unrest +1" with no face attached —
  exactly the "lands on a man" requirement S-DOWN was written to test.

---

## 6. The patronage cascade

This needs no new object, and stating why is the point. A **mark** — Free Master standing, a Church
benefice, a guild sponsorship — is conferred by an admission act (§4), and like any claim it carries a
`source`: the specific person or judging set that granted it. That source pointer *is* the patron field;
it was already implicit in the claim tuple's provenance.

When the granting patron falls — disgraced, excommunicated, executed, stripped of office — nothing
writes a demotion. Instead, **the original admission act is simply re-evaluated**, once per client,
using the same community judging-set mechanism that granted it, now reading the community's *current*
stance (which has just shifted, because the patron's fall is itself a witnessed event that moved every
member's stance toward the patron and, by association, toward what the patron sponsored). One political
event — a Free Master caught in a caste-transgression case, in the shape of Maret Uln and Gerik Strand
— fans out into N separate re-evaluations, each a real act with its own outcome: some sponsored
apprentices keep their standing because their own record independently satisfies the judging set; others
lose it, publicly, by name, at the next standing date.

- Closed loop: **producer** — the patron's fall event; **carrier** — the same admission-act mechanism,
  re-run per client whose mark's source names the fallen patron; **consumer** — each client, whose
  eligibility, marks, and next opening_set are recomputed individually.
- **N-line:** cut it and a political fall produces only a scalar penalty to the fallen person — no
  ripple with other names on it, and no reason a client would ever fear, court, or avenge their patron.

---

## 7. Treaties, and why they do not bind

A treaty is nothing but `Dispensation(issuer=(A, B), proposition, scope, terms)` where both issuers hold
office and either may act against the terms at any time. **There is no enforcement field.** This is
Diplomacy's refusal taken whole: cheap talk is the default, and everything interesting about a treaty
follows from the fact that nothing stops either party from breaking it.

**Breach** is not a flag. It is any ordinary act, by either issuer or their agent, whose resolved event
contradicts a treaty term. And critically: **a breach nobody witnesses is not a breach yet.** The true
event happened in the world's real state, but until `witness` deposits a claim naming it against that
specific treaty term, the wronged party's `choose()` has nothing to read — it is, for every purpose that
matters to play, not yet a betrayal. It can surface later, retroactively, through a field investigation
(T9) that reconstructs the claim's true root — the same mechanism that makes the forged-succession-edict
precedent work here without a new object.

**What makes an instrument genuinely binding:** something already-costly is bundled into the treaty as
collateral, using a mechanism the substrate already owns — never a new enforcement object.

| Collateral mechanism | How it binds | Setting example |
|---|---|---|
| Hostage / fosterage | a named person's address changes into the counterparty's containment scope (an ordinary migration act) — breach puts *that person* at risk, and their obligation edge to their own hearth is now leverage | Prince Torben at the Altonian court |
| Church consecration | the Church stakes its own excommunication power on enforcing the clause — failing to act costs the Church prestige, so it has skin in the outcome | a Crown succession settlement consecrated by the Dicastery of Doctrinal Adjudication |
| Pledged holding | a settlement's stake (its granary, its garrison) is pledged as surety, seizable on witnessed breach | a border fortress pledged against a truce |
| Marriage | binds two houses' successions together — breach damages both hearths' succession pointers, not just one issuer's reputation | Elske–Alexios |

**Worked trace — a realm-scale clause, a person with no office, next season.** Elske marries Alexios;
the treaty opens Altonia trade, with Torben relocated to Alexios's court as collateral. Some seasons
later, under pressure from Duke Vaynard's anti-caste agitation at home, Almud quietly reimposes a duty
on Altonian grain ships. Nobody at Alexios's court witnesses the reimposition directly — until a
returning Altonian merchant-captain files a firsthand claim through his own guild's channel: *new duty
collected, unannounced*. That claim, reaching Alexios, is the breach — not the act itself, which
happened unwitnessed weeks earlier and did nothing to anyone's `choose()` until this moment. Alexios
does not adjust a diplomacy number. He acts on his one piece of real leverage: he issues a local
Dispensation, `scope = [Altonian court], terms = [ProhibitionTerm(leave_court)]`, stripping Torben's
"honoured guest" mark. Torben — who holds no office in this transaction and never signed anything —
receives this as a firsthand claim, because he lives there, and his own `opening_set` recomputes under
house arrest: flee (spend his one sympathetic courtier Knot), petition his sister Elske (`carry`-ing it
up through her household), or comply and quietly build a tie to the Schoenland traders who profit from
exactly this kind of rupture. A realm-scale clause changed what one unoffic'd person does next season,
entirely through witnessed breach and a second, targeted Dispensation — no modifier, no meter.

- **N-line:** cut collateral and every treaty is equally worthless, which means the choice to *pay* for
  a binding instrument stops being a choice — the entire expensive-exception structure the corpus
  insists on collapses into "treaties don't matter," which is a different and worse claim than "treaties
  aren't automatically enforced."

---

## 8. Reach limits

Reach is not a distance number. It is a count of persons the issuer actually employs, and an
institutional-presence fact about each node.

- **Territory Reach Cap.** The issuer's office employs a finite number of dispatchable persons — riders,
  gate wardens, garrison officers. Each publication-with-enforcement at a node consumes one for the
  season. Past that count, additional scope nodes get publication-without-enforcement (a claim lands,
  `enforcer_presence = 0`, compliance craters structurally) or no dedicated publication at all beyond
  whatever folk channels happen to carry it. This is not a debuff; it is the literal fact that Duke
  Vaynard does not have thirty-five riders.
- **Cordon-Complete.** Where a Dispensation's actual purpose requires a *chain* of nodes to jointly
  enforce (a coastal blockade meant to starve Grauwald of salt; a quarantine cordon around a Locked
  Zone), the benefit is an **AND** across every member node's own compliance status, not a sum. One
  captain at Oastad bribed or absent, and salt flows through the gap regardless of how well Stillhelm
  and Grauwald individually comply — the whole chain's benefit fails at its weakest link.
- **Relay/Beacon.** Institutional couriers (Löwenritter riders, the Church's Dicastery of Temporal
  Affairs) carry a Dispensation node-to-node at high fidelity, but only between nodes that already have
  that institution's presence — a garrison, a parish. Each relay hop *resets* distortion to a fresh
  correct source rather than compounding it, which is why the Löwenritter-served core receives sharp
  decrees while the western-fjord pockets and outer Einhir hamlets — the setting's own periphery —
  receive whatever folk gossip eventually carries there, degraded by hop count with nothing to reset it.

- **N-line:** cut reach-as-persons-and-presence and a Duke governs thirty-five settlements as
  effortlessly as one, erasing the exact institutional-and-geographic texture (garrisons, parishes,
  caste-correlated periphery) the setting is built from.

---

## 9. The structural warning

*"No surveyed precedent defends a cross-scale bridge whose default state is indistinguishable from its
absence."* This down-stroke must fail loudly if it fails at all, and it must be checkable from world
behaviour alone, without reading source:

**Signs it is working.** Pick any person with no post inside a Dispensation's scope, N seasons after
publication. Query their claim ledger for a row citing the proposition — it should exist, with a
`source` naming a channel. Their `opening_set`, queried before and after, should differ in exactly the
acts the new terms touch (more smuggling-shaped acts appear at border settlements after a blockade,
without anyone authoring "the smuggling event"). Petitions referencing the proposition should appear at
the next standing date, carried or dropped by named persons. Compliance failures should produce
witnessed events — fines, seizures, public defiances — that are themselves fresh claims, closing the
loop back into §3.1's ranking.

**What silent death looks like.** A Dispensation is issued and its term-deltas write cleanly into a
container's term table — but publication is skipped, stubbed, or silently fails to resolve any channel.
No claim is ever deposited. Every person's `opening_set` is computed correctly, against exactly the same
claims they had before, forever. The world displays a decree that exists nowhere any person's ledger
can find it. This is worse than a bug that throws — it is a decree that is technically "in the world"
and behaviourally identical to one that was never issued, which is precisely the corpus's warning stated
about this exact seam. The one-line test in §4's worked case — query the ledger, not the world state —
is the whole defence against it.

---

## 10. R-criterion check on every fork this document introduces

| Fork | Gain shape | Cost shape | Verdict |
|---|---|---|---|
| Comply vs. evade a levy | flat avoided cost per season evaded | detection probability rises with consecutive seasons of arrears; penalty on capture = accumulated arrears × multiplier, plus a targeting-order hit naming you a forestaller | **Real fork.** Flat gain against *rising* expected cost creates a genuine stopping-time decision, not dominance either way. Per the View Slice steal, the player sees arrears and a qualitative risk band, never the exact detection threshold. |
| Issuer's channel budget: crier vs. institutional relay | relay gives high fidelity | relay is gated by pre-existing institutional presence at the target node, not purchasable in the abstract; crier is available everywhere but degrades with distance | **Real fork**, not dominance — relay cannot simply outbid crier into a settlement with no garrison or parish, so the "better" option is unavailable exactly where it would otherwise dominate. |
| Patron's client: seek a new patron vs. stand alone on accrued merit | seeking a patron: known upfront regard cost, resets exposure to zero | standing alone: no upfront cost, but a roughly flat per-standing-date risk of losing the mark until independently confirmed | **Real fork** — a one-time insurance premium against a bounded, non-compounding risk. Neither arm decays or compounds against the other. |
| Issuer: honour vs. breach a treaty | breach: flat recurring gain (recouped tariff, etc.) each season undetected | honour: flat recurring opportunity cost (forgone revenue); breach, once witnessed, produces a persistent reputational claim that does not expire and poisons future treaty negotiations broadly, with discovery probability rising the more often breach is repeated | **Real, situational fork** — genuinely favours breach under acute desperation (Almud under Vaynard's pressure) and honour under a long time horizon needing future partners. Not structurally dominant either way; this is the desired shape, not a defect to fix. |

No fork above exhibits the banned shape (decaying gain against compounding cost, which makes one arm
structurally dominant). Where a naive reading might suspect dominance — evasion, breach — the actual
cost term is *expected* cost rising with exposure time under uncertainty, which produces a real
crossover decision rather than a foregone conclusion, and is deliberately shown to the player only as an
input and a band, never as the exact threshold, per the corpus's own answer to a world with no GM to ask.
