# 05 — The Blocked Cores

## Status: DISPOSITION (2026-08-30) — a ruling on nineteen findings, not a fix. Nothing here ratifies on merge.
## Addresses: `09_GAP_REPORT.md` §1 — *19 of 55 characters have a BLOCKED CORE; eleven of the nineteen are RICH.*
## Reads: `08_coverage_matrix.md` §2.1 (the roll-up) and the six season documents behind it.
## Composes on: the merged suite, and on the two fixes filed alongside this — `03_the_missing_needs.md`
## and `04_relational_at_settlement.md`, and on `01_the_floor.md` (D-1) and `02_the_act_economy.md` (D-2),
## which are filed in the same directory and are not duplicated here. Adds no subsystem.

---

## 0. The result, before the reasoning

Nineteen characters have live acts and a stated want with no act whose object it is. Dispositions:

| disposition | n | share |
|---|---|---|
| **ACCEPT AS UNREACHABLE** — the want is out of the character's power, and that is correct and interesting | **10** | 53% |
| **SUPPLY AN ACT** — the want is legitimate and the design should reach it | **8** | 42% |
| **CANON DEFECT** — the want is stated in a form no design of this family could reach | **1** | 5% |

**And the eight SUPPLY verdicts are delivered by four edits, not eight.** Three of the four widen an
existing field; the fourth drops a precondition. **Zero new objects, zero new subsystems, and no act that
did not already exist under another name.**

| edit | delivers | also closes |
|---|---|---|
| **E1 · The addressable thing is a venue, not a container.** `Petition.respondent_container` widens to `respondent_venue`. | Jarnstal · Klapp · Palaiologina | **D-7** (the mispriced B-11 cost) · gives Baralta a legal move on article 3 |
| **E2 · The two need formulas** (`03_the_missing_needs.md`). No verb added at all. | Uln · Torsvald | **D-3** · **S20** |
| **E3 · `found_hearth` widens to `found`** — a portion may create a holding at any container, not only a hearth. | Wessel | **D-10** (no construction verb at any rung) · 13 §10's unpriceable fork |
| **E4 · `settle_in_full` loses its creditor precondition.** | Ems | **S8** · convergence **#22** (one lane used a verb another proved absent) |

**Three further blocked cores needed no edit at all, because a standing ruling had already answered them
and the lane did not have it.** Palaiologina's room was ruled allowed by **B-5**; Vossen's clock was already
in `08 §10`'s table; Mertha's vacancy follows `14 §2.4`'s own revocation-in-fact precedent.

So the honest sizing is: **of nineteen reported blocked cores, ten are the design working, one is a canon
artefact, three were answered by rulings already on the books, and the genuine backlog is four characters
behind three small edits.** The reporting was substantially the problem — and §7 argues that is a finding
about the instrument, not an excuse.

---

## 1. The one edit that does most of the work

### E1 · The addressable thing is a venue, not a container

Three of the nineteen are blocked by the same sentence, and the report already suspected it (D-7):

> **B-11**, accepted with its cost stated: *"'The Dicastery decided' is permanently inexpressible. Only 'the
> four persons holding these posts each did something.' **You cannot address a petition to a Dicastery**;
> you address it to a person, and that person can drop it."*

The first half is right and must stand — an institution must never be rendered as a speaker (T1). **The
second half does not follow from it.** `Petition(petitioner, proposition, respondent_container, backing)`
names a container for one reason: the container carries the standing date the petition must resolve before
(01 §5.3) and the door it must enter through. An office cluster has no node — but its root office
**convenes**, `convene` is one of 14 §1.1's closed five, and `14 §5`'s table already gives every Dicastery a
named convener and named standing dates.

> **A cluster has no container. It has a date and a door. The petition object was carrying the wrong field.**

The edit, entire:

```
Petition( petitioner, proposition, respondent_venue, backing )
   respondent_venue : a Venue in the sense of 14 §5 — (convener, enter, speak,
                      admissible_source, attendance_cost, standing_dates, decision_rule),
                      whose container field may be a containment node, an office, or NONE.
```

Nothing else moves. `carry`, `forward`, `amend`, `bundle` and `drop` are unchanged; the four choices are
still made by a named person at a named time, and a drop still deposits grievance naming him.

**Two standing rulings license this rather than one, which is why it is a widening and not a proposal.**
`14 §5` already parameterises venues by convener and date rather than by node. And **B-5** already ruled that
*"a private negotiation is a venue with no container — ALLOWED."* The containerless venue is not new here; it
has been allowed since the adjudication register was written, and two lanes reported empty cells that it had
already filled.

**B-11's price survives exactly.** You still address a person — the convener — and he can still drop you.
What changes is only that the petition now has somewhere legal to be *filed*, so being refused is
distinguishable from having nowhere to ask. That distinction is 05 §5.1's whole up-stroke: *"the specific
injury of being heard and refused — which is the injury that actually makes politics."*

**Dominance check.** A Dicastery's door is `clerics in orders` / `benefice-holders` / `anyone with a register
petition`, so a layman still needs an intercessor with standing there — strictly harder than a settlement
petition, which is right. And the convener's drop is unchanged, so nothing about the power balance moves;
only the legality of asking does.

- *Loop.* Produced by 05 §1.1's shortfall as before; carried by named persons rung by rung as before;
  consumed by a decision at a venue — which may now be a room rather than a place.
- *N-line.* Cut it and every office cluster in Valoria — four Dicasteries, the Löwenritter, every
  trans-settlement guild, Niflhel — is politically unaddressable, so the design's entire up-stroke has no
  legal object against the peninsula's most institutionally mature bodies.

---

## 2. ACCEPT AS UNREACHABLE — ten

An unreachable want that is **acknowledged** is drama; one that is silent is a bug. Each of these is
recorded here so that it is acknowledged, with the named mechanism that closes it and, where one exists, the
adjacent want that is reachable.

### 2.1 King Almud Almqvist — the deed presumption, blocked at a venue his rival convenes

The room where a Crown claim is tested is entered by seat-holders and convened by the claimant against him.

**ACCEPT.** This is `14 §6` working exactly as derived: *"a Crown that conferred few offices can revoke few
offices,"* against a deed-monarchy whose warrant *"decays every season as veterans die and cannot be
renewed."* A king who could reach the room where his own legitimacy is tried would be a king whose
legitimacy did not depend on other people. **The one requirement is legibility:** he must be able to know
that Baralta convened it and ordered the items against him, which `witness` on a `convene` act supplies. If
that claim never reaches his ledger the block is silent, and then it *is* a bug.

*Note, and it matters for how this row is read.* Almud's THIN verdict is caused by **D-2**, not by this
block — his lane says so directly: *"under the ten-act reading the verdict moves toward RICH."*
`02_the_act_economy.md`, filed alongside, rules that the ten acts are his **reach** rather than his
allowance, which reaches the same verdict by a route that costs the design nothing. **So the fix for Almud
is already filed and it is not this one.** Do not treat his blocked core as his problem.

### 2.2 Queen Lenneth Almqvist — caste dismantlement by royal decree

Her canon goal needs `issue`; she holds no office.

**ACCEPT.** The matrix's own §3.1 is the argument: `issue`-by-presence, `arrest` and exclusive allocation are
the *only three* capabilities no postless character reached in 56 probes. *"Office is the only thing that
unlocks a stranger"* is the design's confirmed central claim, and a queen consort who could decree would
falsify it. Her want must route through a person, which is what her three live forks are for. **Her season is
the strongest vindication in the exercise of `14`'s claim that an office adds no verb, and it would be
undone by supplying her one.**

*Separate item, not this one.* Her political-up channel rests on `right of audience`, which is defined
nowhere — S10, convergence #9, three lanes. That is a design hole with a name and it is not a blocked core.

### 2.3 Princess Elske Almqvist — a banked claim with no venue she can reach

**ACCEPT**, and it is `04 §3.2`'s stated design read back verbatim: *"A banked claim confers no enforcement.
That is the whole of it."* A claim its holder could press from off-board would delete the reason banking
exists — a marriage would stop being an acquisition and become a win. Her exclusion from the extraordinary
sitting is the same fact as Almud's, one seat over.

### 2.4 Duchess Inge Baralta — article 3, blocked by another faction's vacant custody

**ACCEPT**, loudly. `08 §10.1` derives this as the Consecration Crisis and it is the suite's showpiece: two
contested successions composing into `CARRIED-WITHOUT-FORCE`, a record row everyone can cite, an F2 hazard on
every voter, and a `pattern` counter that makes the next attempt heavier. *"Nothing about that was authored."*

**And under E1 the block becomes legible and addressable without becoming soluble by her alone.** She may now
petition the Dicastery of Doctrine and Archives' venue — `admissible source: instruments only`, standing date
*on demand* — asking that the custody be filled. The Cardinal may drop it, and the drop names him. A want
blocked by a named person who can be asked is precisely the design's target state; a want blocked by a
vacancy nobody can address is not.

*Canon note.* V4: `04 §10` gives her a **marriage**-basis claim while canon says unmarried, childless,
heirless. Unresolved, and it changes which article she is strongest on.

### 2.5 Uta Falkenrath — no route from popular support to a heritable seat

`14 §10` refuses a mandate meter absolutely; `04 §8` pays a non-seat-holder `act_reach` 0.1 against 1.0.

**ACCEPT.** A mandate meter is the refused object — a container-level gauge with no knower — and refusing it
is right. **A commune leader cannot become a duke, and that is true of communes.** The lane's own arithmetic
is the proof rather than the complaint: ten backers equal one seat-holder against a chamber of seventeen, and
`score(f) = capacity × (1 + 0.5·norm)` cannot close that with norm alone.

*The adjacent reachable want, which her lane did not score.* `04 §8`'s third outcome — *several claimants and
no office binds them → UNRESOLVED, held by whoever physically holds it, re-opening at every standing date* —
is available to her, and it is what a commune actually does. She cannot take the seat. She can make it
unexercisable, permanently, at a cost that compounds on the holder. That is a real season and it is one
document over from where her lane looked.

*Canon note.* V12: canon authors a popular mandate the suite refuses categorically. Collision, not gap.

### 2.6 Halvar Brandt — every cut against the incumbent is in someone else's hand

**ACCEPT.** `07 §4`'s whole content is that a support set's *cuts* are what a challenger must land, and if the
incumbent's bases are held by third parties then the challenger's job is to move those third parties — which
is a coalition, which is `04 §8`'s own anti-dominance property: *"coalitions become necessary at scale,
without a coalition mechanic."* His lane read the queue and did not price the coalition.

*The adjacent reachable prize is one rung down and it is his.* A **chapter mastership** is conferred by three
sworn brothers on β = 3.0, deed only — exactly the currency he accumulates by doing his job. The Grandmastery
is a queue; the chapter is a strategy, and it is the rung from which the chapters' criterion can be moved.

### 2.7 Nessa Grindvold — blocked at the venue that names her

**ACCEPT**, and her own lane says it best: *"Not a gap: `14 §6`'s Crown made concrete, weak everywhere it must
ask and procedurally absolute in the one room it owns."* A legal representative with no procedural standing
at the court she is titled to is a **finding about the setting**, and it is dramatic rather than defective.
Her live move — the rung-4 venue objection, and forum-shopping into Hafenmark's Parliament whose seats the
Crown holds none of — is supported explicitly, which is the strongest thing the exercise says about the
design anywhere.

### 2.8 Orsk Tallow — perpetuity is not purchasable

**ACCEPT**, and record that the design already contains the nearest thing to what he wants, one document
over from where his lane looked.

An entrenchment *instrument* — a durability field on a charter — is the refused object: container state with
no knower, immune to the thing that actually destroys a privilege. But `04 §3.1` is titled **Entrenchment,
derived**, and it is exactly the mechanism his lane said did not exist:

```
entrenchment(h, H) = min(1, seasons_held(h, H) / 60)      # read off transfer events, stored nowhere
```

At `entrenchment ≥ 0.5` the identical reclaim act deposits grievance in every person of `h` **and** makes
every other holder infer that their own long-held holdings are reclaimable — *"not a threshold firing, but
two hundred hearths independently concluding they are next."*

> **Nobody can grant Tallow perpetuity, and time can.** Perpetuity you were given is revocable by the next
> office-holder; perpetuity you accumulated is politically expensive to take. That is the better object and
> it is already built.

*Honest residue.* `entrenchment` is defined over `(hearth, holding)`. A toll charter is a dispensation, so
reading it over a charter's term is a one-line extension of an existing derivation. That is a smaller
statement than *"there is no entrenchment instrument"* and it should replace it.

### 2.9 Doux Alexios Laskaris — zero of eleven acts has a Valorian container in scope

**ACCEPT**, and this is not a blocked core at all: it is a correctly-scoped foreign actor. His own lane
proved three indirect routes and concluded *"the suite already supplies the mechanism twice over without
having noticed that it did"* — a body standing in his hall, a supply term that moves a Valorian price with no
Valorian having heard of him, and a proposition travelling by telling with no member crossing the water. The
matrix's own §2.2 says the same from the other end: **off-board richness tracks scope-overlap, not distance.**

### 2.10 Mertha — a reversed apportionment

Her son is taken in the war-levy; no act reverses an apportionment; vacancies fire on death and he is alive
and absent.

**ACCEPT, for the want she actually holds.** It is a PRIVATE proposition naming a specific person
(05 §6.2), satisfiable by grace and only by grace, and *grace on a completed muster returns a man who has
already marched.* **A mother cannot un-conscript a son, and that is the entire grief.** Supplying an act
here would be supplying a happy ending.

**Two things reach her without touching that.** Under E2 she now holds a computed exposure need whose
satisfying proposition is *the levy ought not fall on this hearth at the next reckoning* — a different want,
reachable by petition, which moves her from BLOCKED to a live season. And §3.8 supplies the vacancy her mill
needs, which is the adjacent object, not the want.

---

## 3. SUPPLY AN ACT — eight, behind four edits

### 3.1 Osten Jarnstal — a candidate inside an office cluster has no up-stroke

**SUPPLY: E1.** He petitions the Dicastery of Fortitude's venue on its visitation date. The Cardinal — or the
Confessor, who holds the veto — may forward, amend, bundle or drop it, and the drop deposits grievance naming
him. He wanted a seat and had no legal act whose object it was; he now has the same act every hamlet fisher
has, into a harder room. **That is the correct outcome, not a generous one.**

### 3.2 Magnus Klapp — everything consequential gated on a `confer` he cannot pursue

**SUPPLY: E1**, identically — a petition into Doctrine and Archives' *on demand* date, `admissible source:
instruments only`, which happens to be the one class of evidence a cathedral archivist can actually produce.

**Second, separate block — CANON DEFECT, recorded here rather than counted twice.** His Awakening needs
`admitting_share`, which sums Convictions whose **construal sets** admit a rendering-side reading. *No
construal-set table exists in either corpus, for any Conviction* (V18, three lanes). The mechanism is fully
specified and its inputs are absent, so whether Scholastic ever wakes him is unanswerable. That is missing
data, not a missing act, and it is the only thing in the nineteen that is genuinely unbuilt-system-dependent.

### 3.3 Zoe Palaiologina — probe and press have no verbs

*Invade* is fully specified; everything below it is empty, so escalation is binary at the seam that most
needs it gradual.

**SUPPLY — and every piece already exists, including the ruling.** Her lane's diagnosis was that *"no chamber
has a foreign container, so 08's negotiation machinery has no room to run in."* **B-5 already ruled a venue
with no container ALLOWED.** The Off-board × Argument EMPTY cell contradicts a standing adjudication.

So, under E1's widening, an inter-realm parley is a venue row:

| venue | convener | ENTER | SPEAK | DECIDE | admissible source | standing dates |
|---|---|---|---|---|---|---|
| **an inter-realm parley** | whichever party sets the date | the principals and their attendants | principals and named envoys | unanimity of principals — a treaty binds nobody who did not sign (06 §7) | instruments and sworn testimony | on convening; expiry set by the instrument |

Then **press** is: convene it, table a motion whose proposition is *(Valoria, ought-to-cede X, before date
D)*, and back it with a **demonstration** — `Force` at low form (12's `seize`, `disperse`) at a border node,
performed inside 08 §8's exchange budget, whose entire function is to move the counterparty's estimate of
your willingness. **Probe** is an investigation act performed by the persons the parley puts in the room,
which is how a delegation has always been a probe.

**No new act. `Force` exists, the negotiation machinery exists, the containerless venue was ruled two
adjudications ago.** And escalation stops being binary because the demonstration's *size* is continuous,
which is the property the lane asked for by name.

*Dominance check.* Does the demonstration dominate invasion? Gain: the counterparty's estimate moves this
season. Cost: it is `Force` with `warrant: none` at somebody else's node, so it deposits witnessed claims
that arm every faction in scope — and `12`'s own reading is that a refused or resisted demonstration deposits
*(an order of X was not obeyed)* in every witness, which is contagious. Compounding both sides. Not dominant,
and it correctly makes the small move risky rather than free.

### 3.4 Maret Uln — agency zero in her own defining conflict

**SUPPLY: E2, and no verb is added.** Worked in `03_the_missing_needs.md` §5.2: her commitment row (0.364)
and her exposure row (0.272) sit within one act's reach of each other and move in opposite directions, so
every act she takes is a choice between them. Her dual loyalty stops being *permanently stable* and becomes
*currently satisfied* — the Vaynard row is 0.011 because he still holds Varfell, and jumps an order of
magnitude when he does not.

**This is the cleanest cross-document result in the three fixes: a blocked core closed by writing a formula
the design already claimed to have.**

### 3.5 Sigrid Torsvald — *minimise Thread collateral* has no act that advances it

**SUPPLY: E2, partially, and the residue is named.**

S20 states the cause precisely: `burden` reads *need, container stake and marks*, and Thread collateral is
none of the three, so her principled abort scores **low-burden** and costs her a degree. But once COMMITMENT
computes from the **view**, a harm only the member perceives *is* a need — because `unmet` is a ledger read.
Her covert proposition — *(Thread-sensitives, ought-not-be-harmed-by, the order's operations, all-time)* —
emits `u ≈ 1.0`: constitutive degree, maximal stance, no ledger row anywhere saying it is satisfied. That is
the highest single need row in the roster.

Then `burden = cost to the member's computed need + …` reads it. **Her abort scores high-burden and she keeps
her degree, with no edit to the burden term at all.** The view-read is what makes the private harm
expressible, which is the strongest argument available for why A-1's split was the right ruling.

**The residue, stated rather than papered over.** Her *argument* route stays closed: the chapter sitting hears
witnessed deed only, and her rendering-side claims degrade on every deposit path (convergence #7, four
lanes). She moves from BLOCKED to *refuse-at-the-correct-price and petition*; she does not move to
*advocate*. That half waits on A-6b's unresolved testimony question and is not fixable here.

### 3.6 Yrsa Vossen — she cannot start a clock

**SUPPLY — and no edit was needed, which is the finding.**

Her lane's FINDING 2 was *"a faction cannot hold a standing date, so its leader can never start a clock."*
True of a faction, and **her cell is not one.** S6 records the collision — `01 §4` calls it a faction, `04 §7`
a community, `08 §10` a venue — and `04_relational_at_settlement.md` §6.6 resolves it by the design's own
precedent: **the Movement is a faction, a cell people live in is a community, and a cell that sits is a
venue.** Three objects, one person in all three, exactly the parish priest's shape in 14 §7.

`08 §10`'s table has carried the row all along: *Restoration consensus cell · judging set: every member
present · decision rule: no sustained objection · floor G0 · record custody: none.* A venue has a convener,
and a convener sets a standing date. **Vossen can start a clock inside her own cell**, binding nobody outside
it — which is precisely *"cannot bind, cannot be bound, and can be paralysed by one member: the price of its
virtue."*

*The other half — ACCEPT.* She cannot `carry` or remonstrate, because `carry` needs standing at the
respondent venue and she holds none anywhere. That is `04 §9`'s confirmed statement of what having no post
means, and it is also convergence #9's `right of audience` hole, which is a separate defect with its own
name.

### 3.7 Curate Wessel — no construction verb at any rung

He wants the Chapel upgraded to a Church, and *"the suite contains no construction verb at any rung — no
build, no endow, no found-an-institution, no consecrate-a-structure."* The lane is right, and it is not local
to him: `13 §10`'s own R-criterion table **prices a fork the option set cannot express** (*invest levy
income: granary vs. wall*).

**SUPPLY: E3, by widening the one creation act the corpus already has.**

`04 §2.1` calls `found_hearth(founder, portion, parent)` *"an ordinary act, no new verb,"* and its shape is
already the right one: **spend a portion of an existing holding to create a new object at a parent.** Widen
the parent and the created object:

```
found(founder, portion, parent)
   parent          : any containment node, not only a hearth
   created object  : a HOLDING at parent, entering parent's stake list
   the portion     : leaves founder's holdings permanently — 04 §1.2's larder, unchanged
```

A chapel becomes a church when a person spends a portion, the community's stake list gains a holding, and a
Cardinal confers a benefice at it — three existing operations in sequence. `13 §10`'s granary-versus-wall fork
becomes expressible in the same stroke.

*Dominance check.* Gain compounds: a holding yields every season, and a holding at a container gives you
standing at it. Cost compounds harder, and in two directions. The portion leaves your larder permanently —
04 §2.1's own arithmetic, *"its holdings are the portion, which is smaller; its margin is therefore
structurally lower."* And **a holding you gave a container is a holding the container's office-holder
allocates, not you**, because 04 §5 has no field for loyalty and never will. *The endower buys standing and
loses control*, which is the exact historical shape of a pious endowment. A rich man can create holdings; he
cannot create offices, and he cannot make the granary he built open for his friends.

### 3.8 Konrad Ems — the corruption has no verb

**Two halves, and the first is a scoring error.**

*The promotion — ACCEPT, mis-scored.* His lane's complaint is that *"the corrupt bailiff petitions for his
career through exactly the same funnel as the laundress."* That is a complaint about **equality**, not about
reachability. His route is `admit()` with the Crown's coefficients — α 0.8, β 2.0, γ 2.0, δ 0.5, *either term
alone clears the floor* — so a public deed **or** an inner-circle sponsor gets him to Valorsplatz, and as
`enforcer_presence` for a whole settlement he is better placed to manufacture a public deed than almost
anyone at his rank. Not blocked.

*The corruption — SUPPLY: E4.* This is real, it is large, and it is convergence **#22**: one lane had Thale
*"simply **buy**, because a broker is a person with a price"* and another proved no payment act exists between
unrelated persons anywhere in the corpus. S8 records the contradiction — `07 §4`'s purchased basis rises by
*"buy it"* while `13 §9` refuses a currency outright.

**The minimal fix drops a precondition rather than adding an act.** `13 §8` already has:

```
settle_in_full(hearth, creditor) — pay owed + arrears in stores, before the reckoning,
                                   at the going price (13 §4)
```

That is already a transfer between two parties, priced in goods at the season's price. **The creditor
relation is the only thing making it a debt act.** Drop it:

```
convey(from, to, goods, quantity)   —  stores(from) −= q ; stores(to) += q,
                                       valued at 13 §4's price, witnessable, and depositing
                                       a claim naming both parties
```

**`13 §9`'s refusal survives intact**, and that is why this is the right shape: what moves is *goods at the
season's price*, not a token. You cannot hoard purchasing power in Valoria — only grain, which rots, and iron,
which is heavy. The purchased power base `07 §4` already names becomes reachable without a currency existing.

*Dominance check.* `convey` is witnessable — a cart moves — and deposits a claim naming both parties, so
Tallow's bribe is findable exactly as his forestalling is (convergence #14: *discovery is proportional to a
rival's actual spend*). And `07 §4` gives the purchased basis **the cheapest named cut in the game**: outbid,
or devalue the instrument with a dispensation. **A purchased position is the most fragile one there is**,
which is why canon's corrupt bailiff is a character rather than a winner.

*Adjacent, for Mertha (§2.10) — vacancy by absence, D-9, found by two lanes.* `04 §1.3` emits a vacancy on
death only. `14 §2.4` already rules the general case for offices: *"an office whose `exercise` is zero across
its whole scope for two standing dates is vacant in the only sense that matters, and the world will have
noticed before any venue has."* **Apply the existing ruling to hearth seats, unchanged**, at the horizon table
04 §1.3 already publishes (1 season untitled, 2 titled, 4 consecrated). Mertha's mill emits a vacancy; she is
a claimant, and the strongest one, because she is the person physically holding it. Prince Torben is the same
fix at the other end of the ladder.

*Dominance check on that.* It creates an act — **make a rival absent** (hostage, conscription, imprisonment,
exile) — as an alternative to killing him. Gain: the same vacancy without 04 §2.1's unsolved-killing hazard.
Cost: he is *alive*, so he can return, contest, and name you, and `12`'s `expel` is witnessed. Absence
dominates killing on risk and is dominated on finality — a genuine fork, and it is the exact fork the
setting's hostage politics needs.

---

## 4. CANON DEFECT — one

### 4.1 Annika Feldhaus — a revelation the epistemics forbid

At TS 0 the discovery that her supply chain carries Thread-touched goods degrades on *every* deposit path —
telling, reading, inference, witness — into *(the goods, condition, wrong)* at confidence 0.2. **Raise her
Focus, literacy, archive access and patronage to the ceiling and nothing changes** (V20).

**CANON DEFECT**, and the classification matters. What is blocked is not a *want* — her want is maximum
revenue for the Compact, which is entirely reachable and which makes her one of the best-served characters in
the exercise. What is blocked is an **authored arc beat**: a scene in which a PC diagnoses the merchandise and
reveals it. That beat is written in a delivery vocabulary the design refuses on principle, for a person the
refusal is specifically about.

Her lane reached the right disposition already: *"the design converts canon's revelation scene into a fact
she can only learn materially — revenue falling, households sickening, a Dicastery inquest into her ledgers.
A better story, and a change canon has to accept. **Report it; do not patch it.**"*

**And this is a category the matrix conflated.** An arc beat is not a want. Counting one as a blocked core
inflates the number and, worse, invites a fix for a thing that is working.

---

## 5. Dominance sweep across the whole disposition

Every act supplied above is checked in place; collected here so the interactions are visible.

| supplied | dominates? | why not |
|---|---|---|
| **petition into a cluster venue** (E1) | no | the door is `clerics in orders` / `benefice-holders`; a layman needs an intercessor with standing there, which is strictly harder than a settlement petition. The convener's drop is unchanged. |
| **the two need terms** (E2) | no | computed against different denominators; commitment is the committed person's need and exposure the exposed person's, so neither can outrank the other structurally. Worked in `03` §6. |
| **the demonstration** (§3.3) | no | `Force` with no warrant at another realm's node deposits witnessed claims that arm every faction in scope, and a resisted demonstration deposits *(an order was not obeyed)*, which is contagious. Compounding on both arms. |
| **`found`** (E3) | no | the portion leaves your larder permanently, and the holding you created is allocated by the container's office-holder, not by you. You buy standing and lose control. |
| **`convey`** (E4) | no | witnessable, deposits a claim naming both parties, and the purchased basis has the cheapest cut in the game. The most fragile position money can buy. |
| **vacancy by absence** (§3.8) | no | it beats killing on risk and loses on finality, because the man comes back and can name you. A fork, not a strict improvement. |

**One interaction worth flagging.** E1 and `04_relational_at_settlement.md` §6.4 both widen where a petition
may be filed. Together they make **forum-shopping** materially cheaper across the whole game: a petitioner
refused at one venue may now try a cluster venue, an inter-realm parley, or a neighbouring settlement court.
`08 §2`'s rung-4 objection was built for exactly this and is the right counter, but nobody has costed how a
first refusal enters a second venue's record — and `08 §6`'s recorded defeat plus its `pattern` counter may
now fire in rooms they were not written for.

---

## 6. The count, restated honestly

**10 accept · 8 supply · 1 canon defect.** The report asked whether most are unreachable, which would mean
the design is fine and the reporting was the problem, or whether most need acts, which would be a real
backlog.

**Neither, and the split is close to even — but the sizing is not.** The eight SUPPLY verdicts are four
edits, three of which widen an existing field and one of which removes a precondition. And **three of the
eight required nothing at all**: B-5 had already allowed Palaiologina's room, `08 §10` already held Vossen's
venue row, and `14 §2.4` already ruled Mertha's vacancy case for offices.

So the true backlog behind the headline finding is **four characters and three small edits** — Jarnstal and
Klapp behind E1, Wessel behind E3, Ems behind E4 — plus two more (Uln, Torsvald) delivered as a by-product of
a fix that was already the report's priority #4.

**The design is in better condition than the number 19 suggests.** It is not in *good* condition on the
report's other findings: D-1 (the floor), D-2 (the act economy) and D-6 (the conferral cycle) are untouched
here and are all larger than this.

---

## 7. What the instrument got wrong, and why that is not an excuse

Ten of nineteen "blocked cores" are the design working, and three more were answered by rulings already on
the books. That is 13 of 19, and it deserves a cause rather than a shrug.

**The cause is that a lane cannot see the adjudication register while it is writing.** Every one of the three
already-answered cases was a lane correctly reading its own documents and reaching a conclusion a ruling had
overturned: B-5 for the containerless venue, `08 §10` for the cell, `14 §2.4` for revocation-in-fact. The
report's own §7 names the same defect class from the other side — *"a finding recorded as decided is not
decided until it is applied, and nothing checked application against record."*

**And there is a second cause, which is the instrument's own axis.** The matrix scored *"a stated goal with no
act whose object it is"* without distinguishing:

| what was counted | what it is |
|---|---|
| a want the character holds | a blocked core |
| an arc beat an author wrote for them | not a want at all (Feldhaus) |
| a want that is correctly out of their power | the design working (ten of nineteen) |
| a want reachable one document over | a reading miss (Falkenrath's third branch, Brandt's chapter, Tallow's entrenchment) |

**No validator is proposed for either cause.** The report declined to propose one for the same reason and it
was right to: this repository answers process failures with apparatus, and the honest response is to name the
failure. The usable half is narrower and needs no tooling — **a lane sweeping for blocked cores should read
`15_adjudications.md` first**, because three of its nineteen findings were closed there before the sweep
began.

---

## 8. WHAT THIS MIGHT BREAK

**8.1 E1 is a widening of the object B-11 was reasoning about, and B-11's price is now carried by prose
rather than by a type.** Before, *you cannot address a Dicastery* was enforced by `Petition` demanding a
container. Now the type permits it and the discipline — *the fiction must never render an institution as a
speaker* — is a sentence. Every venue row must carry a **named convener**, and a row without one silently
reintroduces the institutional speaker B-11 refused.

**8.2 The inter-realm parley has no enforcement and no jurisdiction.** Its decision rule is unanimity of
principals because `06 §7` says a treaty binds nobody who did not sign. So the room exists and produces
instruments nobody can compel. That is historically right and it means every parley can be entered in bad
faith at zero cost — `08 §8.4`'s cheap-talk default now runs at the one seam where it is least checked by a
judging set, because a foreign counterparty is in nobody's.

**8.3 `found` gives the design a way for material wealth to become political standing**, which it deliberately
did not have. The endowment route is slow and lossy, so it is probably fine; but combined with E4's `convey` a
rich outsider can now buy goods, convey them, and found a holding at a container he has no address in. Whether
`found` should require standing at the parent is a real question and I have not answered it — I have left the
act as permissive as `found_hearth` was, which may be too permissive one rung up.

**8.4 `convey` and E4 sit on top of an unresolved contradiction rather than resolving it.** S8 is `07 §4`
against `13 §9`, and I have taken `13 §9`'s side (no currency) while giving `07 §4` the transfer it needs.
That is coherent, and it is still a ruling on a live collision made inside a disposition document, which is
not where rulings belong.

**8.5 Vacancy-by-absence changes the value of every hostage in the setting.** Prince Torben's whole meaning is
that he is a claim with a body. Under the fix, his absence from the Valorian court for four standing dates
emits a vacancy against whatever seat he holds — which may be exactly right, or may hand Altonia a lever
nobody costed. It fires on the King's own household first.

**8.6 The dispositions in §2 are rulings, and ten of them close a want permanently.** If any is wrong, the
failure mode is silent: a character stays unplayable and the record now says that is intended. The three most
attackable are **Falkenrath** (I claim `contest`'s third branch is her real season; her lane did not), **Brandt**
(I claim the chapter is his prize; canon points him at the Grandmastery), and **Tallow** (I claim derived
entrenchment answers a want stated as a charter, which is a substitution, not a satisfaction).

---

*Nineteen dispositions. Ten accept, eight supply, one canon defect. Four edits, three of them widenings and
one a removed precondition; no new object, no new subsystem, and three of the eight supplied by rulings that
were already on the books.*
