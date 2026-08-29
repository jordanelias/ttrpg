# 04 — The Hearth and the Community

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: IN (cross-cutting) · Composes on: `01_substrate.md` §1, §2, §3, §4, §5
## Method: derived from the substrate. No prior design document, ruling, or existing module constrains it.

**What this document owns.** The two rungs that the substrate names and does not build: **Hearth** and
**Community**. Neither exists in the game's world material — "community" appears only as a loose word
for the Restoration Movement's operating level, the real sub-settlement tier is the *district*, and
there is no family object at all. So this is not a restoration. It is the construction of the two
rungs that make the ladder a ladder, and the reason they exist is one sentence: **a rung exists so
that peers can compete inside a shared container.** Hearths alongside each other in a community give
you noble houses and cadet branches. Communities alongside each other in a settlement give you guilds,
parishes, hamlets and the caste order.

**Reading key, inherited from the substrate.** Every object is stated as *producer → carrier →
consumer* and carries an N-line. Anything that cannot name a lost emergent possibility is in §11, cut.
Nothing here introduces a second actor type, a second resolver, or a decision function that sees the
world.

---

## 1. The Hearth

A hearth is a containment node holding persons. It owns three mechanisms and nothing else.

### 1.1 State

| held at the hearth | why it must be held rather than derived |
|---|---|
| `stores` — a scalar in **mouth-seasons** | it is the integral of past seasons; deriving it means replaying history every tick |
| `holdings` — the set of yield sources the hearth currently draws | this is the hearth's **stake**, and stakes are what containers hold |
| `seat` — the headship, and any office attached to it | likewise a stake, and it is contested, not owned |
| `pointer` — three separable transfer lists (name / seat / holdings) | §1.3 |
| `banked_claims` — dormant claims on seats elsewhere | §3.2; each is a standing date with a watch predicate |

That is the entire hearth. There is no prestige, no honour, no cohesion, no dynasty score. Everything
else about a lineage is read off event history — who married whom, who held what, when — because those
events already exist and a stored summary of them is a second copy that can disagree with the first.

### 1.2 The larder

**Producer:** the seasonal reckoning, a standing date every hearth carries.
**Carrier:** `stores`, a single scalar.
**Consumer:** every person in the hearth, through their computed subsistence need, which selects
which acts are worth taking.

```
mouths(h)   = Σ_{p ∈ h} appetite(p)          appetite: child 0.5 · adult 1.0 · elder 0.7 · pregnant 1.3
draw(h)     = Σ_{H ∈ holdings(h)} yield(H, season)
            − Σ_{d ∈ dispensations in scope} levy(d, h)
stores(h)  += draw(h) − mouths(h)                          (may go negative: a shortfall is a debt)
margin(h)   = stores(h) / mouths(h)                        seasons of cover — the only number read
```

`yield` is a roll, not a constant:

```
yield(H, season) = base(H) × season_factor(territory) × (3 + d10) / 8.5
```

which ranges 0.47×base to 1.53×base with mean exactly 1.0. **A bad season is `d10 ≤ 3`** — a 30%
event costing between a quarter and a half of a holding's contribution. `season_factor` is where the
strategic layer touches the kitchen: a blockade, a march through the fields, a territory's Order stat
collapsing, all move one multiplier that every hearth in scope feels without anyone authoring a
hardship.

**The bands, published; the trigger points, never.** (This is the one place the game must obey the
view-slice discipline, because there is no GM to explain a famine.)

| margin | band | what the player is shown |
|---|---|---|
| ≥ 4 | Provisioned | every input listed: holdings, yields, mouths, levies |
| 2–4 | Sufficient | same |
| 0.5–2 | **Thin** | same, plus which single input, if it moved, would drop the band |
| 0–0.5 | **Hungry** | same |
| < 0 | **Failing** | same, and the shortfall in mouth-seasons |

A person reads their *own* hearth's band exactly. They read another hearth's band only through claims
in their ledger, which is why a neighbour's hunger is a rumour and one's own is a fact.

**How the larder drives a person to act.** Need is computed, never stored:

```
need(p, subsistence) = clamp(0, 1, (2.0 − margin(hearth(p))) / 2.0)
                     + max(0, −margin(hearth(p)))          # the coercive term, unbounded
```

Zero at Sufficient, 1.0 at Hungry, and past 1.0 in shortfall. The second term is the one that matters:
above 1.0 the need outweighs *any* stance the person holds, which is how a devout man smuggles and a
proud one begs. There is no desperation flag; the number simply exceeds the aversions.

A hearth in need has exactly **four relief channels plus one refusal**, and they are deliberately
shaped so that none dominates:

| channel | gain shape | cost shape | dominance check |
|---|---|---|---|
| **Requisition kin** (§1.4) | immediate, large, *decays with repetition* | regard, *compounds* | not dominant because it is a crisis instrument, not income: it converts Failing→Thin once |
| **Petition** (substrate §5.1) | slow, uncertain, but it changes the **terms** — compounding | a carrier must be found, and being dropped deposits grievance | not dominant because it can be refused by a named person |
| **Take an opening** (substrate §5.2) | immediate, repeatable | accrues witnessed acts against your marks; publicity is not controllable | not dominant because the judging set is the cost and it grows |
| **Migrate** (§9) | resets the larder problem entirely | destroys standing; marks travel and standing does not | not dominant because it is the only irreversible one |
| **Commit to a rival proposition** | nothing this season | you become a target | this is what the other four leave behind when they fail |

None of these is a new act. All five already exist in the substrate. The larder's whole job is to
supply the *need term* that raises them out of the noise.

- **Cut the larder and you lose:** the generator of ordinary need. Every want in the game becomes
  political ambition, no one is ever driven by anything, and a bad harvest is a number on a province
  rather than a reason Torben's daughter takes the Löwenritter's oath.

### 1.3 The succession pointer

The pointer is not one list. It is **three**, and separating them is the entire design, because a
lineage's politics is the gap between them.

| transfer | default rule | edited by |
|---|---|---|
| **the name** — the house mark | every person contained in the hearth at death already carries it, and keeps it | *nothing removes it* |
| **the seat** — headship, plus any office the hearth holds | cognatic-senior: eldest surviving issue, gender-blind, capability-weighted | disinheritance, legitimation, contest |
| **the holdings** — which yield sources the larder draws | follow the seat unless separately assigned | dowry, foster-portion, grant, reclaim |

**Death does not resolve succession.** It emits a **vacancy**: a standing date at a horizon (1 season
for an untitled hearth; 2 for a titled seat; 4 for a consecrated one, because a consecration needs a
consecrator). Between death and the date, `contest(hearth, seat, claimants)` is open — §8. The
default rule is a *presumption*, and presumptions are rebuttable at a venue.

Three outcomes, and only the first is quiet:

```
one claimant with capacity                       -> the presumption stands; transfer executes
two or more, and an office-holder can bind them  -> he decides; the losers deposit grievance toward HIM
two or more, and NO office binds them            -> UNRESOLVED. The seat is held by whoever physically
                                                    holds it, and the contest RE-OPENS at every
                                                    subsequent standing date, depositing grievance
                                                    each time. This is open war.
```

That third branch is why **a claim with no enforcement resolves to war, not to inheritance** — and it
is the same three lines whether the seat is a Kettlemaker's workshop or the Crown of Valoria.

**The interregnum, abolished by mechanism rather than by fiction.** Every dispensation in force was
issued by a person, and every compliance with it is a choice made against the complier's stance toward
that *issuer*. When the seat transfers, the issuer identity on every standing dispensation changes to
a person toward whom the compliers hold no formed stance. A **normal** succession replaces a stance
with a stance inherited from the predecessor via the name mark. A **contested** succession leaves the
new holder's stance column empty everywhere at once, which is precisely "every settlement's acceptance
re-opens for renegotiation." No new object; the effect is a consequence of the compliance term already
reading the issuer.

- **Cut the pointer and you lose:** any reason to plan past your own lifetime. Marriage stops being
  political, disinheritance is a mood, and no house has anything to lose that outlasts a man.

### 1.4 The obligation edge

**Producer:** birth, marriage, fostering, cohabitation — all acts.
**Carrier:** an edge between two persons, with a weight.
**Consumer:** `requisition`, an act that surfaces another person's act as *theirs to refuse*.

```
requisition(caller, called, act, terms) -> the act enters the called person's option set,
                                           weighted, and REFUSAL IS ALSO AN ACT
claim_weight(a→b) = base(relation) × cohab_factor × (1 + max(0, disposition(b→a)) / 5)
```

| relation | base |
|---|---|
| head → member of the same hearth | 3.0 |
| sibling within the same hearth | 2.0 |
| parent ↔ adult child, separate hearths | 2.0 |
| sibling, separate hearths | 1.5 |
| fostered-in ↔ fosterer (runs **both** ways) | 1.5 |
| affine (by marriage, first degree) | 1.0 |
| **main line head → cadet branch member** | **2.5** |
| **cadet branch member → main line head** | **1.0** |

The last two rows are asymmetric on purpose. The main line can requisition its cadets heavily; the
cadets can barely requisition upward. That one asymmetry is what makes cadet resentment mechanical
without a resentment stat existing anywhere.

```
strain(request) = cost_to_called(act) / capacity(called)  +  2 · conflict(act, stances(called))
comply_pressure = claim_weight(a→b) − strain(request)
```

The called person still *chooses*, from their own view (substrate §3 — there is no world argument).
`comply_pressure` only weights the option. Then the prices, which are what makes the edge finite:

```
on asking:    Δstance(b→a)  = −0.5 · max(0, strain − claim_weight)     # asking too much costs you even if he complies
on refusing:  Δstance(a→b)  = −0.3 · claim_weight                      # the refused party resents in proportion to his claim
if PUBLIC:    every p ∈ JS(request) applies their own stance toward the proposition "kin owe kin"
```

That last line is where the thirteen Convictions do real work with no new machinery: a judging-set
member whose primary Conviction is **Community** or **Honor** punishes the refusal; one whose primary
is **Liberty** or **Utility** may punish the *asking*. Same act, opposite deposits, no consensus
broadcast.

**The fork this creates is the one worth having.** An obligation edge is a finite asset. Spend it now
to pull a Failing larder up to Thin, or *bank* it — an unspent edge is capacity at a future vacancy,
because `contest` sums capacity over persons and a kinsman who owes you is a person whose act you can
requisition on the day. Gain-now versus leverage-later, with the same resource. Neither shape
dominates, because the crisis is real and so is the vacancy.

- **Cut the obligation edge and you lose:** the claim kin have on each other. Family becomes an address
  label; there is no such thing as a favour, a debt, or a brother who will not come.

---

## 2. Cadet branches, derived not authored

### 2.1 The derivation, in five lines

1. A non-heir marries or is granted a portion. `found_hearth(founder, portion, parent)` — an ordinary
   act, no new verb.
2. The new hearth's **seat** transfer does not lead to the main line's seat. Its **holdings** are the
   portion, which is smaller. Its margin is therefore structurally lower.
3. Its members keep the **name**, because nothing removes the name.
4. Therefore every judging set that reads them reads a house mark, and a house mark carries an
   *expectation* of standing:
   ```
   expected_standing(p) = Σ_{m ∈ marks(p)} recognised_weight(m, community's admission rule)
   need(p, standing)    = clamp(0, 1, (expected_standing(p) − held_standing(p)) / 3)
   ```
5. `need(p, standing)` is the gap between what everyone reads off you and what you hold. **That gap is
   ambition**, computed, and it is why no ambition trait exists: a trait would be a second copy of this
   number that could disagree with it.

A cadet branch member is therefore a person with a permanently non-zero standing need and no
inheritance path to close it. They must seek standing elsewhere. There are six exits, each an
**admission gate** (§6), each with a genuinely different shape:

| exit | gate | grants | costs | why not dominant |
|---|---|---|---|---|
| **Church** (parish → Canon, under a Dicastery) | strongly weighted on marks | standing + a Cardinal's patronage | celibacy: your own seat transfer terminates | closes the lineage exit permanently |
| **Guild** (the Masterpiece Examination) | committee stances on marks | Free Master → burgher → a seat at the settlement | 7–12 seasons, a fee, repeated failure possible | slow, and the fee competes with the larder |
| **Löwenritter** | caste-open; weighted almost entirely on deed | a mark that *outranks* the house name | the oath binds to Crown-as-institution, not bloodline — so you may not serve your own house's claim | fast, and it forecloses exit 5 |
| **Restoration cell** | consensus of the cell | no standing anyone recognises; real capacity | you become a target and your mark becomes a liability | negative standing, high capacity — an inversion, not a ladder |
| **Marriage** | the other hearth's head | a *new* seat list to stand in, plus a dowry | your degree in your own line drops | transfers a claim rather than creating one |
| **A knife** | none | removes a person from a seat list | witnessed → the judging set; unwitnessed → a claim with no findable root | unbounded downside, and the substrate's corroboration rule means an unsolved killing stays askable forever |

That last row is the shape of the 1218-AG hunting "accident." A killing whose firsthand root nobody
holds is given, by substrate §3, a single synthetic root shared by every retelling — so the story told
three hundred times corroborates exactly once, and the perpetrator is not *hidden by an author*, he is
**unreachable by evidence**. A field investigation that finds a genuine second root flips it.

### 2.2 The four family acts are edits, not systems

| act | edit to the larder | edit to the pointer | edit to the edges |
|---|---|---|---|
| **foster out** | −1 mouth here, +1 there | none | creates a 1.5 edge **both ways**; the child's judging set becomes the host community's |
| **dowry** | moves a holding from A's `holdings` to B's | removes that holding from A's seat transfer; the bride's degree in A's seat list drops one | affine edges at 1.0 |
| **disinheritance** | none | removes a person from the **seat** list only | **edges persist** — which is why disinherited kin keep requisitioning |
| **legitimation** | none | inserts a person into the seat list at a declared degree | creates full same-hearth edges retroactively |

Four acts, three fields, no new object. Note the two loaded asymmetries.

**Disinheritance does not remove the name.** So a disinherited son carries a house mark, is read by
every judging set as owing standing 3, and holds standing 0. His `need(p, standing)` is the maximum
the formula produces. That is the pretender, generated by an omission rather than by an author.

**Legitimation is an assertion, and assertions can be forged.** It is an act, performed by a person, at
a time, and it is witnessed or it is not. In a vacancy window, whoever holds the record can assert a
legitimation, and **if uncontested it is deposited into every ledger as genuine until a contradicting
claim arrives** — substrate §3.2, no cap on belief. Discovery flips legitimacy retroactively because
the ledger row names its source. The Church's Dicastery of Doctrine and Archives holds the records;
Altonia destroyed the Almqvist records. The consequence falls out with no rule: **a claim whose
firsthand roots were destroyed can be asserted forever and corroborated never.** That is why
ancient-blood claims on the Valorian throne are moot and why the deed-presumption is the only
presumption left standing.

### 2.3 The shapes it produces

**Varfell and Hafenmark house intrigue** is §2.1 run forward across two hundred hearths. Each cadet
hearth's members carry a maximal standing gap, an asymmetric obligation edge that lets the main line
tax them and not the reverse, and six exits with different costs. Nothing needs to be written per
house. Duke Magnus Vaynard's anti-caste position is not a personality: it is what a duke computes when
his duchy's cadet hearths are systematically routed toward the two caste-open gates (Löwenritter,
Niflhel) and therefore into capacity he does not command.

**The Baralta Crown Claim** is §3.2 plus §1.3's third branch, and it is worked in §10.

---

## 3. Lineage across lifespans

The problem: a hearth outlives its members, but the substrate forbids container memory. The resolution
is that almost every lineage quantity is **derived from event history that already exists** — transfers,
marriages, fosterings — and the only things stored are stakes and dates, which is what containers are
allowed to hold.

### 3.1 Entrenchment, derived

```
entrenchment(h, H) = min(1, seasons_held(h, H) / 60)          # 60 seasons ≈ one generation
```

Read off the holding's transfer events. Reclaiming a holding:

- **entrenchment < 0.5** — an **administrative act**. The seat-holder issues a dispensation; the hearth
  complies at a rate set by its stance toward him; done.
- **entrenchment ≥ 0.5** — the identical act instead deposits a grievance stance in every person of `h`
  **and** — this is the mechanism, not a crisis object — every other hearth that witnesses it draws the
  inference `inferred(claims…)` that *their own* long-held holdings are reclaimable. That inference is a
  legitimate substrate claim source. It is what turns one reclaim into a rebellion: not a threshold
  firing, but two hundred hearths independently concluding they are next.

- **Cut entrenchment and you lose:** the difference between a landlord collecting and a landlord
  provoking. Every reclaim costs the same, so nobody hesitates and nothing ever becomes irreversible.

### 3.2 Banked claims

```
Claim(claimant_hearth, seat, basis, watch)
basis ∈ { cognatic-senior, marriage, deed, grant, forged }
watch  = a predicate on a vacancy at `seat`
```

A banked claim is **dormant**: it does nothing, costs nothing, and is invisible to `resolve`. On a
vacancy whose watch predicate matches, its holder becomes a claimant in `contest`. Because holding one
is free, lineages accumulate them, and a marriage is therefore always partly an acquisition. Princess
Elske's marriage to Doux Alexios Laskaris banks a Laskaris claim on the Valorian succession that will
sit inert for decades and fire on one death — which is exactly why Altonia now eyes Prince Torben, who
is the *counter-bank*: a fostered hostage is a claim-with-a-body.

**A banked claim confers no enforcement.** That is the whole of it. At the vacancy, what decides is
`contest`'s capacity term, which routes through persons. Basis without capacity produces §1.3's third
branch: war.

- **Cut banked claims and you lose:** marriage as politics, and any reason for a house to plan across
  three generations toward a seat it does not hold.

### 3.3 Precedent leverage, derived

```
leverage(h, seat) = Σ over past holders of `seat`, most recent first:
                        1.00  if a person contained in h (or married out of h) held the seat
                        0.60  if h placed a spouse into the holder's hearth
                        0.30  if h placed a fostered child into the holder's hearth
                        0.00  otherwise
                    each term × 0.85^(intervening holders in whom h placed nothing)
```

Nothing stored — it reads the seat's transfer history and the marriage and fostering events. Two
consequences fall out that are worth the formula on their own:

1. **It decays by demographic failure, not by violence.** A lineage that fails to place a daughter,
   spouse or fostered child for one generation loses its precedent term without anyone having attacked
   it. Nobody has to be beaten; the family simply stops appearing in the record.
2. **It is readable by investigation.** Someone can go and count the marriages. That satisfies the
   discipline that a power source's vulnerability must be discoverable by the player rather than
   opaque, and it makes a lineage's strength an *investigable fact* (T9) instead of a stat.

### 3.4 The deed presumption, and why it is rebuttable

The first Almqvist earned the throne by Secession War command with no blood claim. So:

```
deed_weight(line, seat) = Σ over service events attributed to `line` at the seat's founding,
                          each weighted by the number of LIVING persons holding a firsthand-rooted
                          claim of that event
```

Because the weight is proportional to living firsthand witnesses, **the deed presumption decays every
season as veterans die**, and it cannot be renewed, because you cannot manufacture a firsthand root
for a war that has ended. Ducal houses are cadet and deed families; their presumptions are decaying on
the same clock. Succession is cognatic-senior — a *presumption*, which means it wins by default when
unopposed and is rebutted at a venue by argument. There is no rule anywhere saying deed-presumption is
rebuttable. It is rebuttable because presumptions are, and because its numerator is mortal.

**This is the Baralta Crown Claim's timing, and nobody authored it.** Duchess Inge Baralta does not
need a new claim; she needs the last men who saw the Secession War to die, and then a banked marriage
claim presented at a vacancy against a deed-presumption whose witnesses are gone.

---

## 4. The Community

A community is a containment node holding hearths. It owns two mechanisms.

### 4.1 The judging set

**Producer:** any act resolving at a locus. **Carrier:** nothing — it is computed at resolve time.
**Consumer:** each member's stance table, receiving one deposit each.

```
JS(act) = { p : hears(p, act) }

hears(p, act) ⟸  p was present at the locus                                      firsthand
              ∨  p shares the actor's community address ∧ publicity(act) ≥ θ(p)  ambient
              ∨  p holds a Knot with someone in the above                        one hop, no roll, no decay
              ∨  a telling reached p                                             rolled, distorted, traceable
```

Only the second clause is new; the other three are substrate. `θ(p)` is a per-person attention floor —
a person with a large hearth and a Thin larder has a high θ and hears less gossip, which is a real and
free class effect.

**Publicity — what makes an act public:**

```
publicity(act) = venue_factor × √(witness_count) × mark_salience(actor)

venue_factor:  private dwelling 0.2 · workshop 0.5 · market, gate, square 1.0
               standing date (court, examination, tithe reckoning) 1.5 · cathedral, parliament 2.0
mark_salience  = 1 + 0.2 × (number of the actor's marks that any community member holds a strong stance toward)
```

`mark_salience` is the quiet one. A person carrying a house name, a Free Master's grade, or a Southern
Einhir heritage mark inside a Crown-Latinate quarter is simply **talked about more** — their acts
propagate further in *both* directions. Maret Uln's transgression reaches twice as far as an identical
act by an unmarked neighbour, and so does her charity. That is a structural caste effect produced by
nothing but visibility.

**How far word travels** — hop decay, not a radius. Each telling multiplies confidence by
`credulity(hearer) × stance_weight(hearer→speaker)` and distorts the value toward the speaker's stance.
Below confidence 0.15 a claim is not worth a hearer's telling budget and travel stops.

| publicity | reaches | by |
|---|---|---|
| < 0.5 | the hearth, and whoever holds a Knot | 1 hop |
| 0.5–1.0 | the community, within 1 season | ambient + 2 hops |
| 1.0–1.5 | adjacent communities in the same settlement by season 2 | 3–4 hops, visibly distorted |
| ≥ 1.5 | settlement-wide, and along every Knot immediately | standing dates are where reputations are actually made |

**What the judging set does** — converts one act into many small, *divergent* regard changes:

```
for each p ∈ JS(act):
    Δstance(p → actor) = Σ_{m ∈ marks(actor)} stance(p, referent(m)) · salience(m, act)
                       + stance(p, proposition(act))
                       + credulity-weighted confidence of p's claim about what happened
```

Note the first term. **The act is read through the actor's marks.** The same act — a Southern Einhir
woman using Thread sensitivity to find a lost child — deposits +2 from the child's mother and −3 from a
Knight of the Peace, from one resolve, with no consensus broadcast anywhere. This is not caste as a
difficulty slider. It is caste as a *reading*, which is why it changes when the readers change.

- **Cut the judging set and you lose:** reputation as a thing that happens to you rather than a stat you
  own. Nobody can be shamed, nothing is embarrassing, and there is no rung between the hearth and the
  town where people who know your face can hold you to something.

### 4.2 Admission

**Producer:** persons who already hold standing in the community. **Carrier:** the mark it confers and
the address change it makes. **Consumer:** every subsequent judging set, admission gate, and
`expected_standing` computation that reads that mark.

```
admit(committee, candidate, community) -> event conferring a mark and (optionally) an address

support(m, candidate) = α · Σ_{k ∈ marks(candidate)} stance(m → referent(k)) · weight(k)
                      + β · performance(candidate, the admission act itself)
                      + γ · Σ_{s ∈ sponsors} standing(s) · staked_regard(s)
                      + δ · stance(m → candidate)

verdict = aggregation_rule(community) over { support(m) : m ∈ committee }
```

**α, β, γ, δ are weights and never signs.** Every sign in this system comes from a person's stance.
That single constraint is what stops the caste gate from being a special case: a committee is not
"biased against Southern Einhir" by rule; its members hold stances, and α says how much those stances
matter next to the work.

The community holds `(α, β, γ, δ, aggregation_rule)` and the roster of who may sit on a committee. It
holds nothing else. §5 argues why this is a stake rather than container memory.

---

## 5. No container state

A community stores no norm, no cohesion, no reputation, no unrest, and no memory.

```
norm(community, proposition) = Σ_{p ∈ community} weight(p) · stance(p, proposition)  /  Σ weight(p)
weight(p) = 1 + standing(p)          standing = marks recognised by THIS community's admission rule
```

Computed on demand, at the moment something reads it, from persons who are named.

**What this buys, concretely.** When the Kettlemakers disapprove of admitting Southern Einhir
journeymen, that number is forty men's stances. Two old masters die of the flux, three journeymen
fostered in the hamlet are admitted, and the number moves — **without anyone having decided to change a
norm, and without a norm-change event existing.** It also means the Restoration Movement's "Community
Weaving" is not a special faction ability: they do not attack the norm, they change the membership, and
the norm follows because the norm was never anything else. And a player can move it one person at a
time, by name, by Knot, at a market stall.

Conversely, a settlement cannot be "made loyal." There is no field to write.

**What a container honestly does hold**, and this is the complete list:

| held | why it is not container memory |
|---|---|
| **stakes** — the granary share, the seat, the holdings, the workshop rights | contested, allocated at dates, physically held by persons |
| **the rule for computing a judging set** | a rule, not a roster; the roster is recomputed each act |
| **standing dates** — the examination, the tithe reckoning, the vacancy, the truce's expiry | a schedule, readable by everyone, holding no opinion |
| **the admission parameter vector `(α, β, γ, δ, rule)`** | see below |

The parameter vector is the one I want to be honest about. It is state at a container, and the
substrate's list is "stakes, judging sets and dates." **I claim it is a stake** — it is contested, it is
allocated at standing dates, and factions fight over it exactly as they fight over grain. Duke Magnus
Vaynard's Path B *is* a dispensation raising β for guilds in Varfell. It is flagged again in §12.

And the counter-move falls straight out, which is the best evidence the object is real: **raising β
changes no one's stance**, so a committee that wanted to exclude routes the same exclusion through γ
(no Free Master will sponsor him) and δ (personal dislike, unfalsifiable). *A caste-breaking law is
evadable through the terms it does not name.* Nobody designed that. It is what happens when you write
one formula and let a duke edit one coefficient.

---

## 6. The admission gate is where caste lives

Caste in this setting is informal, uncodified, and enforced by rank-gating **per institution**. Per
institution means **per community**, which means it lives in exactly one formula, `support()`, with one
parameter vector per community and no exceptions anywhere.

| community | committee | α marks | β deed/work | γ sponsor | δ personal | aggregation | mark conferred |
|---|---|---|---|---|---|---|---|
| Craft guild — the **Masterpiece Examination** | Free Masters present | 1.0 | 1.0 | 0.5 | 0.5 | majority with support > 0 | Free Master → burgher eligibility |
| Parish → Canon (**Church of Solmund**) | the priest + a Dicastery assessor | **1.5** | 0.5 | 1.0 | 0.3 | the assessor alone | communicant; at grade, Canon |
| **Löwenritter** chapter | three sworn brothers who witnessed the deed | 0.2 | **3.0** | 0.3 | 0.3 | any two of three | Sworn — supersedes the house name |
| **Niflhel** | one recruiter, in private | 0.2 | 1.0 | 0.0 | **1.5** | that one recruiter | a **concealed** mark |
| **Restoration cell** | every member | **0.0** | 0.5 | 0.5 | **2.0** | unanimity; any member may block | no mark; a concealed alignment |
| **Crown**, Standing 3+ | the King, or two of the inner circle | 0.8 | **2.0** (public deeds) | **2.0** | 0.5 | either term alone clears the floor | Standing 3 |
| **Einhir hamlet** | the elder heads | **2.0** (residence + heritage) | 0.0 | 0.5 | 1.0 | consensus of heads | hamlet address; heritage read as authentic |

Read the caste behaviour off the coefficients, not off any rule:

- **The guild is where the bias bites hardest** because α and β are equal: excellent work exactly
  cancels a moderate prejudice, and the committee's composition decides. Change three masters and the
  same candidate passes with the same masterpiece. That is why the Masterpiece Examination is the
  documented site of guild bias and why it is *fixable by attrition* rather than by law.
- **The Church is strongly gated** because α = 1.5 with a *single* assessor. One person's stance decides,
  and there is no majority to dilute it. A Southern Einhir Canon is "a scandal" — not because a rule
  says so, but because the arithmetic makes it a one-man exception, and an exception attributable to a
  named man is the definition of a scandal. Confessor Arne Himlensendt is sincerely devout and
  completely wrong precisely here: his pastoral compassion enters δ as a genuine positive and his
  essentialist stance enters α as a larger negative, in the same sum, from the same man.
- **The Löwenritter is caste-open** because β = 3.0 **drowns** the mark term rather than reversing it.
  Nobody there is unprejudiced. The deed simply outweighs them.
- **Niflhel is caste-open by design** through δ, not through α. A recruiter's need is waterfront and
  covert access; his stance toward a Southern Einhir dockworker is therefore *positive*, and the same α
  that excludes at the guild includes here — because **α is a weight and the sign came from a person.**
  One formula, opposite outcome, zero special cases.
- **The Crown** gates Standing 3+ behind public deeds **or** inner-circle sponsorship, which is the `either
  term alone clears the floor` rule. Both terms are scarce for a hamlet person: deeds need a venue with
  publicity ≥ 1.5, and sponsors must stake regard with a judging set that reads the candidate's marks.
- **The Restoration cell** sets α = 0.0 and δ = 2.0 with a unanimity block. It is the only gate in the
  peninsula that does not read heritage — and it is also the only one where a single member's grudge is
  absolute. It is not a kinder institution; it is a differently-shaped one.

---

## 7. The community roster of the setting

One object, seven parameterisations. Nothing below is a subclass.

| community | contains | its stake | its standing dates |
|---|---|---|---|
| **Kettlemakers' Row** and the craft guilds | the hearths of masters and journeymen | workshop rights, the guild's share of the market, its burgher seats | the Masterpiece Examination; the dues reckoning |
| **Einhir hamlets** (Grauwald, Stillhelm, Oastad, the western fjords) | hearths of shared heritage outside the wall | commons, fishing grounds, the granary share they are last in line for | the tithe reckoning; the elders' sitting |
| **Crown-Latinate quarters** | hearths inside the wall | the better wards, proximity to the court, the gate's protection | the court's sitting |
| **Parish congregations** | every hearth in a district, by presence | the parish's tithe, the school, the burial ground | the feast days; the Dicastery's visitation |
| **Restoration consensus cells** | persons drawn from three hamlets and two guilds, by alignment | nothing material — presence markers only | whenever the cell agrees to meet |
| **Löwenritter chapters** | sworn brothers, quartered | the chapter house, the Crown's warrant | the chapter's sitting |
| **Niflhel dockworker crews** | those recruited, concealed | the waterfront itself | none published; that is the point |

Two of these are worth naming as demonstrations. A **parish congregation** is the Church's presence at
the rung where it actually touches a person — the Dicastery of Temporal Affairs sets a levy and the
Dicastery of the Defense of the Faith sends an assessor, but what a hamlet fisher meets is a priest who
sits in his judging set every week. A **Restoration cell** is a community whose admission gate is
consensus instead of a masters' vote — same object, one parameter row — and whose members are contained
elsewhere, which is exactly the point: it is a *faction* (alignment) that also functions as a community
(admission + judging) for those it admits, and the friction between those two addresses is the game.

---

## 8. Sibling competition

```
contest(container, prize, claimants) -> allocation event
prize ∈ { the stake, the regard of the container's members, the container's offices }
claimants: factions — sets of persons at degrees. THEY NEED NOT BE SIBLINGS IN THE TREE.
```

Resolved at the container's standing date, never continuously. **Container control is not a scalar
field on the container.** Every board game that models contested power is built on an entity that is
contested rather than owned, and this is that: the container holds the *prize*, and who holds the prize
is an event history, not an attribute.

```
capacity(f, container, prize) = Σ_{p ∈ f} act_reach(p, container, prize) × degree(p, f)

act_reach(p, ·, office) = 1.0  if p holds a vote or seat under the container's rule
                          0.3  if p can carry a petition into it
                          0.1  otherwise
act_reach(p, ·, stake)  = p's ability to physically take, hold, or deny the thing
act_reach(p, ·, regard) = publicity-weighted, so one visible person can outweigh twenty quiet ones
```

Three modifiers, all derived elsewhere, none new state:

```
score(f) = capacity(f) × (1 + 0.5 · norm(container, proposition(f)))        §5
                       × (1 + 0.3 · leverage(f's hearth, seat))            §3.3, office prizes only
```

Outcome, identical at every rung:

```
one claimant clears the floor                        -> allocated; losers deposit grievance toward the WINNER
several, and an office-holder can bind them          -> he decides; losers deposit grievance toward HIM
several, and no office binds them                    -> UNRESOLVED; held by whoever physically holds it;
                                                        re-opens at every subsequent standing date,
                                                        depositing grievance each time -> open war
```

Two properties worth stating because they are arithmetic rather than rules:

- **Coalitions become necessary at scale, without a coalition mechanic.** When one claimant's capacity is
  large, no single rival can clear the floor, and the only claimant that can is a faction assembled from
  two previously separate ones — which requires persons to `commit` across a proposition boundary, which
  costs them regard in their own judging sets. Power is never dominant; it is expensive to unwind, and
  the cost is paid by whoever waited.
- **Claimants need not be siblings.** The hearths of a community contest precedence and marriages; the
  communities of a settlement contest the granary and the seats; and a Restoration cell drawn from three
  hamlets and two guilds contests **the same seat through the same function**, because capacity sums over
  persons and asks nothing about where they are contained. That is why a faction must never be a tier.

- **Cut `contest` and you lose:** the reason a rung exists. Peers stop competing inside a shared
  container, and the ladder becomes a filing system.

---

## 9. Migration and exclusion

`migrate(person, destination)` is an act requiring admission at the destination or the founding of a
hearth there.

| travels with you | does not |
|---|---|
| capability | **standing** — it is derived from the *destination's* recognised marks, so it is recomputed, usually to zero |
| **every mark, including heritage** — which is why migration does not escape caste | judging-set regard: the destination holds no stance toward you, and absence is not neutrality |
| **Knots** — bandwidth survives distance; that is what a Knot is for | obligation edges, which decay: `claim_weight × 0.6` per rung of separation |
| your degree in the seat list you left | the larder — you leave the holdings behind |

**What being an outsider means, per rung:**

| rung | outsider means | mechanical bite |
|---|---|---|
| Hearth | no obligation edge | relief channel 1 is closed; a bad season has no crisis instrument |
| Community | not in the judging set, and no one holds a stance toward you | your claims have no corroborators, so you lose every argument that turns on provenance; and a petition needs a **carrier**, and no one will spend regard on a stranger |
| Settlement | no office-holder's constituency includes you | dispensations still bind you, because scope is presence |
| Territory and above | you appear only in a faction's density profile | you are read as a threat by a Duke who has never met you |

**The asymmetry is the whole of it.** The down-stroke reaches you by *presence*. The up-stroke needs a
*person*. So an outsider is fully bound and structurally mute — bound by every levy, able to voice
nothing — and that state is computed, not assigned. It is also, exactly, the Restoration's recruiting
profile: high grievance, no carrier, no gate that will take them, and one community in the peninsula
whose α is zero.

**And exclusion is not free.** A community that excludes an insider does not remove him from the
container — he still sleeps there, still hears everything, still appears in `mouths` and in the tithe.
What changes is that his capability leaves the community's `capacity` in every contest, his stance
leaves the norm, and his Knots become channels *out*. **An excluded member is a leak with no loyalty**,
and that sentence is a consequence of the judging set being computed from who hears rather than from who
belongs. §10's second trace prices it.

---

## 10. Two worked traces

### Trace A — a cadet's larder, two rungs up, in eleven seasons

**S1.** Erland Baralta-Ström, second son of a cadet Baralta hearth in Hafenmark. Marks: house name
Baralta (`expected_standing` 3), Northern Einhir, no guild grade. Held standing 0. `need(standing)` =
(3−0)/3 = **1.0**, the maximum the formula produces, and it has been 1.0 his whole adult life.

**S2.** The hearth's two holdings roll `d10` = 2 and 4 → yields 0.59× and 0.82× base. `draw` falls
below `mouths`. `margin` 3.1 → **1.4, Thin**.

**S3.** Erland requisitions the main line's head — a cadet-to-main edge, `claim_weight` **1.0**. The ask
is a grain transfer: `strain` 1.8. `comply_pressure` = −0.8. The head refuses, from his own view, and
the refusal deposits `Δstance(Erland → head) = −0.3`. Publicly, at a hearth reckoning:
`publicity` 0.5 → the cadet hearths of the Ström district hear it. Four of them hold a Community
Conviction and deposit against the head; two hold Precedent and deposit against Erland for asking.

**S4–S6.** The guild route is closed (no apprenticeship, and the Masterpiece fee competes directly with
`mouths`). Erland takes the **Löwenritter** gate: β = 3.0, α = 0.2. His marks are nearly irrelevant
there and his deed at a bridge crossing is witnessed by three sworn brothers. Two of three support.
**Sworn.** He gains a mark that outranks his house name, and an oath binding him to Crown-as-institution
rather than bloodline.

**S7.** Duchess Inge Baralta holds a banked claim on the Crown seat (basis: marriage, watch: any Crown
vacancy). Her `leverage(Baralta, Crown)` is high — four placements across three reigns. Her `capacity`
must route through **persons with `act_reach` at the Realm rung**, and Erland, now Sworn, is one of the
few Baralta-named persons who has any. He counts in the sum at degree × reach.

**S8.** But his stance toward the Baralta claim is now **negative**: the oath is to the institution, and
his own house's claim is precisely what it forbids him to serve. His `degree(Erland, Baralta faction)`
falls to near zero. Inge's precedent term is large and her capacity term is hollow — a fact she cannot
see, because she reads a **profile** and not a ledger.

**S9–S10.** She waits, which is the correct play: `deed_weight(Almqvist, Crown)` decays every season as
Secession War veterans die, and no one can manufacture a firsthand root for a finished war.

**S11.** The vacancy fires. Two claimants: cognatic-senior presumption on a decayed deed, and a banked
marriage claim with a hollow capacity term. The venue that could bind them is a Church-consecrated
coronation — and the Church's own succession is contested, so **no office-holder can bind**. Branch
three: unresolved, held by whoever physically holds it, re-opening at every standing date, grievance
each time. That is the Crown Succession Contest and the Consecration Crisis, produced by a `d10` roll of
2 in season 2 and one boy's oath in season 6.

### Trace B — the Kettlemakers exclude, and pay eight seasons later

**S1.** Maret Uln, Southern Einhir, journeyman in Kettlemakers' Row, sits the **Masterpiece Examination**.
Seven Free Masters. α = β = 1.0, γ = 0.5, δ = 0.5, majority with `support > 0`.

- `performance` = **4.0** (excellent work; nobody disputes it).
- marks term: `Σ stance(m → Southern Einhir heritage) × weight`. Four masters hold strong negative
  stances (−4.8 each), three hold mild ones (−2.6).
- sponsors: none. No Free Master will stake regard on her.
- support = **−0.8** for four masters, **+1.4** for three. Three of seven. **Refused.**

**S2.** `publicity` = 1.5 (standing date) × √11 witnesses × `mark_salience` 1.4 = high. The Row hears,
both adjacent quarters hear, and it reaches the hamlet through her Knot with **Gerik Strand** in one hop,
undistorted, that evening.

**S3.** Maret's grievance stance toward the Row and toward the four masters *by name* is deposited. She
does not migrate: her hearth is here, her larder is here. She is contained in the Row and excluded from
it. `weight(Maret)` in `norm(Row, ·)` is 1 + standing 0 = 1; her stances are now hostile and still count.

**S4.** She commits to a **Restoration cell** at degree 2 — α = 0.0, the only gate in Goldenfurt that does
not read her heritage. Gerik, whose Niflhel mark is concealed, does not; his own admission went through
δ, and his recruiter's interest was precisely her kind of access.

**S5–S7.** Two masters die of the flux. Three journeymen fostered in the hamlet are admitted elsewhere on
performance. `norm(Row, "admit Einhir journeymen")` — recomputed, never stored — has moved from −0.6 to
−0.1. Nobody voted. The membership changed and the number followed.

**S8.** The tithe reckoning. The Row's burgher must carry a petition for a levy exemption into the
settlement court, and `capacity(Kettlemakers, Goldenfurt, the stake)` sums `act_reach × degree` over
persons. Maret is not in it, and neither are the eleven hamlet backers who would have lent their stance
to a guild that had taken her. The Restoration cell, whose members are drawn from three hamlets and two
guilds, backs a rival proposition at the same date with capacity the Row cannot match on its own. The
Row loses the exemption.

The price of a refusal in season 1 was paid by a different man, at a different rung, in a different
currency, in season 8, and nothing scripted the connection. It runs through `support()` → grievance
stance → `commit` → `capacity()`, four functions that were all needed anyway.

---

## 11. What this document refuses

Each was considered and cut because no N-line could be written, or because a cheaper object already
reaches the same emergence.

- **A lineage or dynasty object separate from the hearth.** Entrenchment, precedent leverage and deed
  weight are all derived from transfer, marriage and fostering events that exist regardless. A stored
  dynasty score is a second copy of history that can disagree with history.
- **An ambition, resentment or pride trait.** Ambition is `expected_standing − held_standing`. A trait
  would be a second copy of that gap, and it could drift out of agreement with the marks everyone reads.
- **A caste modifier on any roll.** Caste is (a) a weight α on a mark term whose *sign* comes from a
  person's stance, and (b) `mark_salience` in publicity. A −2 would make it a difficulty slider and
  therefore unchangeable by anything a player could do to a person.
- **A community cohesion, guild reputation, or hamlet unrest scalar.** Derived from member stances, or it
  is dead state that reads as mechanism.
- **A succession crisis object.** A crisis is the third branch of `contest` plus grievance deposits. An
  object would let the world have a crisis nobody decided to have.
- **A marriage market.** Marriage is `found_hearth` + a dowry edit + a banked claim. A market would
  price what should be argued over.
- **A prestige or honour currency.** Regard is per-person toward a referent. A currency has no holder of
  an opinion and cannot be lost in one quarter and kept in another.
- **A scheduled restoration of standing.** Standing changes only by admission, exclusion, or death. A
  cadence that heals it converts a consequence system into a treadmill.
- **An inheritance auto-resolver.** Succession emits a vacancy and opens a contest. Resolving it
  automatically is the same error as a treaty that binds automatically: it deletes the only interesting
  case.
- **A hearth-level or community-level memory, council, or elders' brain.** Containers hold stakes,
  judging-set rules, dates, and the admission parameters. Persons hold everything else.

---

## 12. CHALLENGE — where I believe I have strained the spine

Stated openly rather than diverged silently.

1. **The admission parameter vector is container-held state.** The substrate's list is "stakes, judging
   sets and dates." I hold `(α, β, γ, δ, aggregation_rule)` at the community and argue it qualifies as a
   **stake**: it is contested, it is allocated at standing dates, and factions fight over it exactly as
   they fight over grain — Duke Magnus Vaynard's whole Path B is a dispensation editing β. If that
   reading is rejected, the fallback is to hold the vector on the community's *seat* (the office of
   guild warden, parish assessor, chapter master) rather than on the community, which is strictly worse
   for the caste-open institutions that have no single office-holder, and I would rather be told than
   guess.

2. **I supply a `standing` derivation the substrate does not name.** Marks are in the person's field
   list; standing is not. I define `standing(p, community) = Σ recognised_weight(mark, that community's
   admission rule)` — deliberately *community-relative*, so the same man is Standing 3 in his hamlet and
   Standing 0 across the wall. If standing is meant to be a mark in its own right rather than a reading
   of marks, migration and exclusion both change shape, and §9's table is the part that would move.

3. **`mark_salience` in publicity gives marks a second effect beyond the judging set's reading.** I
   believe this is necessary — without it, a house name changes how you are *judged* but not how far word
   of you *travels*, and half the observable behaviour of an aristocracy is the second thing. But it is
   an addition to the substrate's account of marks, not a consequence of it.

4. **One thing I could not close and am flagging rather than hiding.** The seasonal reckoning is a
   standing date on every hearth, which means the number of dates in the world scales with the number of
   hearths. The substrate treats standing dates as scheduled contestable moments; a per-hearth
   subsistence tick is arguably a different animal wearing the same name. The honest reading is that a
   cohort's larder ticks once for the cohort, and only an individuated hearth carries its own date — but
   the boundary between "this reckoning is a contestable moment" and "this reckoning is bookkeeping" is
   not one I can draw from the spine alone.
