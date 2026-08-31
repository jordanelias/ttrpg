# 03 — Seasons: The Church of Solmund

## Status: FILED (2026-08-30) — coverage probe output, not design. Nothing here ratifies on merge.
## Lane 2 of the play-space coverage instrument (`00_PLAN.md`). Binding: `01_ROSTER_AND_FINDINGS.md`.
## Authority on mechanism: the merged suite `proposals/2026-08-29-valoria-from-scratch/`.
## Authority on persons: `references/npc_registry.yaml`, `systems/factions/faction_canon_v30.md`,
## `faction_politics_v30.md`, `canon/03_canonical_timeline.md`.
## **No new mechanisms.** Where a season could not be written, the gap is written instead.

---

## 0. What this lane had to decide before it could start

Four decisions, all forced, all stated so the seasons below can be read against them.

**0.1 One act, or ten?** Doc 09 §1.1: *"The tick is a season. Every person and every cohort commits
exactly one act per season."* Doc 14 §8: *"A worked season — Vaynard, one turn, **ten acts**, no
faction verbs,"* and doc 05 §3.1 spends "one of v's own acts for the season" on agenda composition as
though there were others. **The suite asserts both and reconciles neither.** This is not a footnote for
the Church: the Confessor's entire power is `confer`, `convene` and a veto, and whether he performs one
of those a season or all of them is the difference between a head of an institution and a bottleneck.
I write under **09's one-act rule**, because 09 owns the tick, and I state the other branch's verdict
wherever it differs. **Reported, not resolved.**

**0.2 The conviction-weight bridge does not exist.** Canon stores convictions as fractions summing to
~1 (`Faith 0.5, Authority 0.2`). The suite's stance weights run 0..5 and its thresholds are stated in
that space (*"a primary Conviction (weight ≥ 4)"*, doc 02 §5.1). **Neither corpus contains a
conversion.** I read a canon primary as suite weight 5 and a secondary as 3, and flag every number that
turns on it.

**0.3 FINDING 3 #2 (who is Cardinal of Justice) is not resolved here.** Both branches are written, in
§3, §4 and §7, and §7 is the probe.

**0.4 A naming collision between canon and suite that changes routing.** Canon (`faction_politics_v30`
§7.3) puts **Heresy Proceedings and the Inquisition** under *Doctrinal Adjudication* (Justice) and
**Templar deployment and enforcement** under *Defense of the Faith* (Fortitude). The suite (03 §8, 14
§5) routes a heresy denunciation to *Defense of the Faith* — describing it as a tribunal that hears
"the accused, if summoned… firsthand testimony and confession" — and treats *Doctrinal Adjudication* as
the interpretive chamber. **The two Dicasteries' functions are swapped relative to canon.** This is not
cosmetic: the suite's sharpest epistemic claim is that routing is set by an item's subject and is
therefore contestable, and the whole point of contesting it is that the channels have different fates
at the end. If the map from subject to channel is uncertain in the corpus, the router's choice is
uncertain too. **Reported, not resolved**; §9.1 shows the routing act under both labellings.

One invented person appears in this document, per FINDING 1's instruction to invent rather than borrow:
**Deacon Halvard Rusk**, who holds the correspondence seat of the Confessor's household. He is not
canon and must not be cited as canon.

---

## 1. FULL SEASON — Confessor Arne Himlensendt

### 1.1 Coordinates

**A · Rung:** Realm (his office's scope) — resident at Himmelenger (T9 per `npc_registry`; the timeline
at `canon/03_canonical_timeline.md:56` calls Himmelenger T14; a minor canon collision, noted).
**B · Office:** **office cluster, at the root of all four** — and the roster's only entry with
`establishment: none of his own` (14 §1.5). `binds = members-by-admission`. He binds nobody by presence.
**C · Alignment:** Church of Solmund, degree **5 (constitutive)**, **avowed**. *(Suite degree, inferred
from his role; canon states no degree because canon has no degree object.)*
**D · Marks:** caste-advantaged (ecclesiastical, Crown-Latinate reading); non-sensitive (`ts: null`);
Church standing 6+ — `rank` 6 by 05 §6.4, the joint-highest in the peninsula with a ducal house.

### 1.2 Opening state — the six person fields

- **Address:** Confessor's Residence / cathedral precinct / Himmelenger / Realm. Celibate, so his hearth's
  succession pointer terminates in him (04: the Church closes the lineage exit permanently).
- **Marks:** as above.
- **Capability:** **`stats: null` in the registry.** The head of the Church has no Focus, no Acuity, no
  Charisma on record. Doc 03 §4 makes the view budget `K = 7 + Focus`, so *his working set is not
  computable from canon*. I use 09's default K = 12 and flag it.
- **Stance:** Faith 0.5 primary, Authority 0.2 (registry); `self_other_initial 0.0`. `faction_canon_v30`
  §596 gives a variant — Faith 0.40 + Precedent 0.20 + Authority 0.15 — noting it was mapped from a
  *Cardinal Reichard profile*, which FINDING 3 #5 flags as a possible person-collision. Two conviction
  vectors for one man, from two live files.
- **Memory:** unspecified. Canon supplies no claim.
- **Ties:** one named channel — **Father Gustav Linder**, his agent inside the Crown Inner Circle
  (`npc_registry` NPC-034, "dual-loyalty"). Whether that tie is a **Knot** (a channel with bandwidth,
  TS-gated per 01 §2) or an ordinary tie is unstated, and it decides whether Linder's reports arrive
  intact and unbidden or as ordinary distorted tellings.

**Conspicuously not in the ledger:** `goals: null` (FINDING 2). And no `arc_trajectory`. The design's
answer is that needs are computed, so I compute them.

### 1.3 Computed needs (02 §6)

| need | arithmetic | urgency |
|---|---|---|
| SUBSISTENCE | `5 − floor(larder_days / (10 × mouths))`; the Church's holdings are tax-exempt by the Altonian containment grant and the cathedral precinct's larder is not scarce | **0** |
| STANDING | `5 × (1 − r) × care`, `care = max(stance[Honor].weight, stance[Identity].weight)/5`. His stance table holds **Faith and Authority**, and neither Honor nor Identity | **0** |
| COMMITMENT | `d × unmet × weight/5` = `5 × 1 × 5/5`. His faction's proposition — *(the peninsula, holds, Solmundan Orthodoxy, all-time, ought)* — is held unmet in his own ledger wherever parish density is low | **5** |
| EXPOSURE | the change in value of his reachable options under asserted terms — the Crown's levies (he is exempt), Vaynard's Path B (his benefices in Varfell go unfilled), the Baralta Crown Claim's approaching consecration | **≈3** |

**The head of the Church has exactly one urgent need, it is at maximum, and it is unsatisfiable by any
single act.** That is a correct and interesting result.

**The systematic finding underneath it.** STANDING resolves to 0 for *every ecclesiastical person in
canon*, because `care` reads only Honor and Identity and the ecclesiastical conviction template
(`faction_canon_v30`: Faith, Authority, Scholastic, Precedent, Virtue) contains neither. Meanwhile
`faction_politics_v30` §1.4 gives the Church a **seven-rung advancement ladder** with initiation duties,
examinations, investiture, a College of Prelates and a Cardinalate election. **The suite's needs
function gives no Church person any urgency to climb it.** A whole faction's career structure has no
motivational input. This is an empty cell, not a rescue opportunity, and it is listed in §11.

### 1.4 The view, and the claim that does not surface

K = 12, ranked by `recency × confidence_live × relevance × stanceweight`. His household channel (03 §8)
is Deacon Halvard Rusk, who dispositions most of what arrives; what reaches the top of Himlensendt's
view is what Rusk **surfaced**, framed, because a household intimate's claims carry high recency and
high stance weight.

**The claim he holds and does not think of.** Somewhere in his ledger sits a report — from a Temperance
assessor, or from a visitation register — that the territories with the fewest filled benefices are the
territories that produce the most reports of anomalous witnessing. `agreement(c) = −1` against his
Faith primary; `λ = obstinacy/5`; `stanceweight = clamp(1 + λ·(−1), 0.05, 2.0) → 0.05`. Its salience is
one twentieth of an agreeing claim of the same strength. It never enters the top twelve.

> He is not hiding it. He is not lying. **He is not thinking of it.**

That is 07 §7's suppression mechanism arriving as one multiplication in view assembly, and it is the
whole of *"sincerely devout, completely wrong."*

**And it collides with a known-open item.** Canon's Arc B (`faction_canon_v30` §688) is *"Cardinal of
Temperance presents Thread-adjacent scholarly findings Himlensendt cannot dismiss."* A scholarly
finding arrives as **testimony**. The NERS audit (16 §3.2) **retracted in part** the salience floor that
would let such a claim cross a hostile stance weight, and held the testimony half open. So: *canon's
principal redemption arc for the Church's head is currently unreachable under the suite's view
assembly.* **Reported as open, per the standing instruction; not patched.**

### 1.5 The option set — every act, and why each is legal

His remit (14 §1.1's closed five) is unusually thin for the largest office in the peninsula:

| remit act | available to him? | why |
|---|---|---|
| **issue** | **no** | 06 §1's `ExcommunicationTerm` is issued by a Dicastery's Cardinal. His office has no scope terms of its own. |
| **determine** | **no** | he holds no venue's decide rule. He holds a **veto** at Doctrinal Adjudication (14 §5) — which produces `CARRIED-WITHOUT-FORCE` (08 §6) and banks a permanent F2 contradiction hazard on him. |
| **confer / revoke** | **yes** | Cardinals, per 14 §1.5. This is his office. |
| **dispatch** | **no** | `establishment: none`. The existential is empty by construction. |
| **convene** | **contested** | `convene` sets a container's standing date. **An office cluster has no container** (07 §6.1). See §8. |

Ordinary person acts remain, and they are where his season actually lives: `tell` (a visitation, a
catechesis, a pastoral consolation); `requisition` on any Church member (07 §1.2 — an ask between two persons,
priced by the obstacle formula rather than gated by rank; the faction channel, not the office one, and
his real reach); `carry` a petition; `commit`; `counsel` through the
tie to Linder; `interview`; `research` — gated at the Archives, whose custodial seat is vacant (§6).

**Six live options this season.** (a) confer Temperance on Klapp; (b) confer Fortitude on Jarnstal;
(c) requisition Linder to *surface* a framing inside the Crown's household channel ahead of the
consecration question; (d) veto at Doctrinal Adjudication; (e) petition the Crown to keep the Church's
exemption; (f) go to a Grauwald hamlet and perform a visitation.

### 1.6 The choice, through the seven phases

He takes **(f)**. His need vector says COMMITMENT 5, his view's top-twelve is dominated by the parishes
his own channel reports as thinly served, and his `choose` reads that view and nothing else.

- **P0 CALENDAR** — Doctrinal Adjudication's visitation fires; the Grauwald tithe reckoning fires; the
  Crown Succession Contest's consecration date is on the docket but not due. Option availability
  recomputes: `confer` is legal for him at every seat, every season, and has been for years.
- **P1 SETTLE** — larders consume; the veterans of the Secession War are one season older, which is 14
  §6's deed presumption decaying under everyone.
- **P2 NEEDS** — as §1.3.
- **P3 VIEW** — twelve claims, all of them Rusk's or his own, none of them the correlation.
- **P4 CHOOSE** — `tell`, at a hamlet chapel in Grauwald whose benefice is unfilled.
- **P5 RESOLVE** — social stratum, last. The act is `tell(Arne, the children of the hamlet, e, e)` with
  `e = (the world, is-of-kind, essence-fixed-and-given, all-time)` at `confidence = credulity(child) ×
  regard(child → the man who buried her grandmother)` — high, early, **general** (07 §7).
- **P6 WITNESS** — divergent, with no special case: a neighbour deposits *he consoled her*; the child
  deposits *the thing I saw was a sin of the eye*; a Restoration sympathiser present deposits *he came
  to tell us what we saw was nothing*. One act, three predicates.
- **P7 RECKON** — the child's anomalous claim is now **resolved**, so it stops contributing to
  `ts_gain`, and her obstinacy resists re-opening it.

### 1.7 What propagates

**Neither stroke.** No dispensation was issued, so nothing travels down; no petition was raised, so
nothing travels up. The act changed no container's terms and appears in no record row. Its only
propagation is into the ledgers of the persons present, and its only consequence is an **absence** — a
claim that will not accumulate, in a person who will not become sensitive, in a territory whose
sensitivity map is the model's *output* rather than its input.

> **The Church's central harm is the one effect in the game that no instrument in the game can
> observe.** There is no gauge on the hamlet, no counter on the Church, no record row, and the man who
> caused it deposits *I comforted a frightened child* into his own ledger, at firsthand, correctly.

### 1.8 Diagnostic — **THIN**

Options exist and are legal. But the **R-check finds a structural dominance**, and it is his office's
own shape that produces it.

`confer` gives compounding gain: a filled Dicastery is an establishment, a courier relay, a benefice
graph, a custody, and a conferral subtree whose whole mass roots in him — it raises the numerator of
14 §6's `sovereign_fraction` for *his* root, which is the Church's stated victory operation. 14 §9's
"appoint the capable or the loyal" prices the compounding cost as **shadow standing rising in the
appointee**, and 07 §5.2's consequence is that the formal holder's capacity returns an empty
existential when he needs the appointee's people. **Himlensendt has no establishment and binds nobody
by presence, so he has no capacity that a Cardinal's shadow standing can empty.** The cost term is zero
*for this office specifically*.

So: compounding gain, no compounding cost. `confer` dominates every other act available to him by
shape, and the design's own criterion says so. Verdict **THIN**.

Two consequences worth carrying forward. First, under 0.1's ten-act branch the verdict flips to
**RICH**, because he confers *and* vetoes *and* requisitions in one season and the dominance stops
mattering — which is how much rests on that unreconciled sentence. Second, and sharper:
**FINDING 4's two vacant seats are not merely undocumented, they are mechanically anomalous.** The
design says the Confessor's dominant act, every season, at zero compounding cost, is to fill a
Cardinalate — and canon says two have stood open. Either the design is missing the cost, or canon is
missing an obstacle. §8 argues it is the design, and names the missing object.

### 1.9 Cells demonstrated live

`Realm × Institutional` (confer, at the root of four clusters) · `Realm × Epistemic` (the catechetical
`tell`, and the non-surfacing claim) · `Realm × Relational` (requisition at d=5 through a faction, by a
man with no establishment) · `office cluster × avowed × constitutive`.

---

## 2. FULL SEASON — Cardinal Aldric Tormann (Prudence / Temporal Affairs)

### 2.1 Coordinates

**A · Rung:** Realm-scope cluster root; acting at Territory and Community through benefices.
**B · Office:** office cluster root, `binds = members-by-admission`, **establishment: a Dicastery's
whole graph** (14 §1.5) — benefice-holders, collectors, assessors, and the courier relay 06 §2 names by
name. He is the only one of the five Church figures in this lane whose `dispatch` is non-empty.
**C · Alignment:** Church d=5 avowed; **and** the *party of Temporal Affairs* (07 §6.1) at d=5 —
proposition *(Church holdings, are, tax-exempt and tithed at the maximum, all-time, ought)*.
**D · Marks:** Church standing 6 (`rank` 6); heritage **SILENT in canon**; non-sensitive (`ts: null`).

### 2.2 Opening state

Canon gives him more than it gives the Confessor: **goals are stated** — *maximise Church wealth
throughput; aggressive tithe collection* — with the registry's own note that they were inferred from
role ("OPTIMISER"). Convictions **Order 0.5, Liberty 0.3**; `self_other +0.1`. Arc: *Parish Revolt, or PC
intervention; inadvertently funds the Church's charitable mission while undermining its cultural
authority.* Stats null, again.

**Conspicuously not in the ledger:** any claim about what his collection does downstream. His channel
(14 §5) hears **account rolls only**.

**His power bases** (07 §4), which is what a season for him is really about:
- **purchased 0.3** — the Altonian containment grant: tax-exempt religious lands, educational rights,
  archival authority (`canon/03_canonical_timeline.md:56`). *The cage became a school.*
- **bureaucratic 0.2** — the tithe and the education monopoly are chokepoints everyone routes through.
- **patronage 0.1**, **ideological 0.4** — the Church's support sets are two centuries old, so most
  persons in them were placed by persons now dead (07 §6).

`cuts_available = 4`; by 07 §4.2 a challenger needs a coalition, not a single cut.

### 2.3 Computed needs

SUBSISTENCE **0**. STANDING **0** — same arithmetic, same reason as §1.3, and Order and Liberty are
neither Honor nor Identity. COMMITMENT **5** on the party proposition and **5** on the Church's.
EXPOSURE **4** — three live term-changes touch his options: Vaynard's Path B (benefices unfilled means
the collection graph shrinks), Baralta's Hafenmark exemption (the party's own stake), the Crown's levy
demand ahead of the succession contest.

### 2.4 The view, and the claim that does not surface

His view is filtered by a Dicastery proctor and composed of `QUANTITY(container, tithe, band)` rows off
the account rolls — high confidence, high relevance, arriving on a courier that resets distortion at
every hop (06 §2). It is the best-informed view in this document, **about exactly one kind of thing.**

The claim that does not surface: a parish priest's report that the last two reckonings in a Grauwald
hamlet produced no arrears *because the hearths sold seed grain*. `agreement = −1` against his stance
that the tithe is owed and collectible; stanceweight → 0.05. He holds it. He never sees it. Two
seasons later the arrears are structural and the priest's parish is the one canon's Parish Revolt arc
fires in — **produced, not authored**, and the mechanism is the same multiplication that runs
Himlensendt's blindness. One term, two Cardinals, two entirely different harms.

### 2.5 The option set

Every one of these is legal for him and illegal for the Confessor, which is the cell this season is for.

1. **`issue`** a `LevyTerm(fraction, base)` over the Prudence graph — raise the tithe share. Legal: it
   is his remit's `issue` over his cluster's scope.
2. **`dispatch`** an assessor to one named settlement. Legal: 14 §3.1. Buys **fidelity** — that
   settlement stops being a cohort in his ledger — at the price of one establishment member for the
   season.
3. **`convene`** the tithe reckoning at a settlement and **order its items** (05 §3.1). The cheapest
   real power in the game: three items ahead of the hamlet's remission petition kills it with seat
   capacity and never refuses it.
4. **`confer`** a benefice — 14 §2.3's single-assessor vector, α = **1.5**, his determination alone.
   Capable or loyal (14 §9). A Southern Einhir Canon here is *one man's attributable exception*, which
   is the definition of a scandal.
5. **`revoke`** a benefice, firing 06 §6's **patronage cascade**: every mark whose `source` names the
   revoked man is re-evaluated by the current judging set, one client at a time, publicly, by name.
6. **Negotiate** with Baralta over the Hafenmark exemption (08 §8). Cheap talk binds nothing; the
   binding instrument available to him is **consecration**, which 08 §8.4 prices as *the Church acquires
   a lever over both parties and both acquire an obligation to the Church's proposition.*
7. **`produce`** the Altonian grant charter as a G4 instrument at a venue — **and he cannot.** 08 §4.1
   grades an instrument G4 only when the object is *held in a declared custody*. The grant's custody is
   the Dicastery of Doctrine and Archives. **That seat is unfilled** (FINDING 4). No determinate
   custody, no G4, and the two-hundred-year-old charter that is the legal root of the Church's tax
   exemption and its education monopoly enters every chamber at the grade of a document nobody can
   vouch for. *The vacancy at Temperance is a live material cost to Prudence.*

### 2.6 The choice, through the seven phases

He takes **(1)**, the levy. It is his stated goal, his need vector, and his view.

- **P0** — the tithe reckoning fires at eleven settlements; option availability recomputes.
- **P1** — larders consume against mouths; the hamlets that sold seed grain are now short.
- **P2** — need, as above.
- **P3** — twelve account-roll claims; no parish reports.
- **P4** — `issue(Dispensation(Tormann, "the tithe is rendered at the higher share", scope = the
  Prudence graph's benefices, terms = [LevyTerm(fraction, hearth larder)]))`.
- **P5** — **binding decisions** stratum, second: the terms change. Then publication, which is not one
  act but a choice of funded channels (06 §2): parish priest (moderate fidelity, *coloured by the
  priest's own stance*), Dicastery courier (very high fidelity, **one settlement per rider per season**),
  crier, guild notice.
- **P6** — deposit is by presence and channel. Where a benefice is unfilled — Grauwald's outer hamlets,
  the western fjords, exactly the map canon already draws — **there is no priest, so there is no
  channel.** The claim arrives late, by market gossip, with the qualifiers shed first (06 §2: *terms
  drop before values distort*), so what lands is the headline share and not the exemption.
- **P7** — confidence decays; ledgers evict; the hamlets that heard nothing hold nothing.

**Compliance is a contest, not an application** (06 §3). `enforcer_presence` is zero at every node with
no benefice-holder to send. Compliance craters *structurally*, not by a die. What it produces is
**arrears compounding toward the next standing date**.

### 2.7 What propagates

**Down**, to a person with no post: a hearth's larder falls, SUBSISTENCE urgency rises to 4, and the
`opening_set` recompute returns acts that were not worth taking last season — sell the boat, go to the
Row, run salt, listen to a Restoration sympathiser. Nobody authored an opportunity.

**Blame targets the wrong man, by arithmetic** (06 §5). The reckoning is performed by a named collector,
witnessed firsthand; Tormann is three tellings away at low confidence. Grievance commits against the
collector. And 05 §8.2: killing the collector clears the rows whose referent is the collector and none
of the rows whose referent is the office — *which part is larger was decided seasons earlier by the
grammar of a rumour.*

**Up**, next season: a remission petition, carried by the parish priest, addressed to… **Temporal
Affairs**, whose venue admits **account rolls only** (14 §5). Forty hamlet witnesses are not weighed at
that door; they are not admitted (08 §9.3: *the admission floor is not a term at all*). The petition
dies at the door of the Dicastery that caused it, and Tormann judges his own cause without a rule
saying he may.

### 2.8 Diagnostic — **RICH**

Seven live options with materially different consequences, and the R-check finds no dominance.
*Issue now vs dispatch for fidelity* runs 14 §9's enforce/tolerate fork with compounding on both arms.
*Capable vs loyal* at the benefice has a real failure mode on each side — a rival you built, or a cap
you hit. *Cheap talk vs consecration-as-instrument* pays cost up front against a benefit contingent on
a breach that may never come. *Revoke vs tolerate* fans out into N re-evaluations he does not control.

This is the richest cell the Church occupies, and the reason is exactly the one the design predicts:
**he is the only Cardinal in canon whose seat is unambiguously filled, and therefore the only one whose
establishment is non-empty.** Richness here is a function of occupancy, not of remit.

### 2.9 Cells demonstrated live

`Realm/Territory × Material` (the levy, the larder, arrears) · `Realm × Political-down` (issue,
publication, the compliance contest, the reach hole) · `Realm × Institutional` (confer, revoke, convene,
the patronage cascade) · `Realm × Argument` (the account-rolls-only door) · `binds = members-by-admission
with a real establishment`.

---

## 3. PROBE — Arnlod Olafsson, Cardinal of Justice *(registry branch)*

**Coordinates.** Realm-scope cluster root · office cluster with the Inquisition as establishment ·
Church d=5 avowed · Faith 0.6 / Authority 0.2 · `rank` 6 · caste-advantaged · non-sensitive.
Registry NPC-038, "Cardinal Justice (oversees Inquisition). Per Jordan 2026-05-08," and the registry
**explicitly overrides** the other source.

**Option set.** The widest remit of the four. `determine` at Doctrinal Adjudication — the venue with the
highest proof floor in the game (**G3**, all articles, article count 3, 08 §10). `issue` an
`ExcommunicationTerm`, which 06 §1 names as his Dicastery's instrument and which strips Church-conferred
marks *at every node in scope*, firing 06 §6's patronage cascade across every client those marks
sourced. `dispatch` Inquisitors — a real establishment. `convene` the visitation and order its items.
`confer` Canons and benefices in his subtree.

**The diagnostic finding.** His venue's `admissible_source` is **"Doctrine & Archives registers only"**
(08 §10; 14 §5 says "its own registers only"). Under either reading, the Inquisition can prove things
only out of an archive, and 03 §6.1 makes archives *the only non-person root-bearers* — the sole source
of **verified** rootprints in the design. **The custody of that archive is the seat that is unfilled.**
So: no determinate custody means no ground reaches G4, so articles do not clear a G3 floor, so the
sitting cannot close on the merits, so it closes at the exchange budget as `CARRIED-WITHOUT-FORCE`
(08 §6). His determinations bank pattern counters and F2 hazards and change no terms.

**Verdict: RICH** — five remit acts, an establishment, and materially different consequences per choice
— **with a structural hostage**: the most procedurally powerful office in the Church cannot produce a
binding disposition while the Temperance seat is empty. That is not a flaw in his season; it is the
vacancy probe biting a second Cardinal.

---

## 4. PROBE — Sæmund Haelgrund

**The contradiction, both branches.** `faction_canon_v30:570` seats him as **Cardinal of Justice**
("Inquisitor; TS 12 unrecognized"). `npc_registry` NPC-004 makes him **Field Inquisitor, deployed at
AP ≥ 3, TS 15**, and its own note says *"Field Inquisitor, NOT a Cardinal. Cardinal Justice = Arnlod
Olafsson."* One file contains the correction of the other, and they also disagree on his TS (12 vs 15).
**Not resolved.** Both branches probed:

**Branch A — Cardinal.** Coordinates and option set are §3's, with one difference that changes the
game: the head of the apparatus that finds heresy is himself, by his own institution's definition,
what it hunts — and *cannot know it*.

**Branch B — Field Inquisitor (registry).** Coordinates: Territory/Settlement · **office: none** — the
suite's post roster (14 §1.5) contains no inquisitorial post, so under the design he is a **member of a
Cardinal's establishment**, dispatched, not a holder. Alignment Church d=4 (sworn; `w(d) = 1.60` lowers every
requisition obstacle put to him). Marks: Church standing 3–4, **latent Thread-sensitive and
unread by anybody including himself**.

**Option set, branch B.** The full investigative act set (03 §6.1) is open to him and to anyone —
`examine`, `interview`, `surveil`, `research`, `reconstruct` — because *action eligibility never
consults office*. What is **not** open: `arrest`. 07 §10.2 computes it — `requires(arrest, P)` needs a
person holding a **binding post** at the node plus two who can lay hands on a man in a crowd. A Field
Inquisitor holds no binding post. **The existential is empty.** He can prove it and cannot take him.

**The probe this character is for: a man who cannot know what he is.** At TS 15, `P(register rendering
facet) = 0` below a facet's floor and `g(TS − floor) × admitting_share` above it — and
`admitting_share` sums his Convictions whose construal sets admit a rendering-side reading. Faith 0.6 +
Authority 0.2, an essentialist theology, is the paradigm rendering-blind vector, so his share is near
zero. When something *does* register, 03 §9's ledger-side degradation fires: the subject is a
configuration, his ledger has **no address** for that referent class, and what deposits is the nearest
thing he can hold — `CONDITION(the mill, wrong)` at 0.2. He calls it instinct because *the claim about
his own perception is itself degraded*. The design produces canon's "attributes Thread perception to
investigative instinct" with no rule about self-knowledge anywhere.

**And it predicts canon's diagnosis path.** Canon says a PC may diagnose him (Cognition vs Ob 2). Under
the suite that is a `tell` whose subject is **a person** and whose predicate is `MARKED(Sæmund,
sensitivity)` — a referent his ledger *does* have an address for. **So the diagnosis lands where the
perception cannot.** A man may be told what he is and still be unable to see what he sees. That is the
design working, precisely, and it is worth recording as a success rather than a gap.

**Verdict: RICH** in epistemic mode — five investigative acts with four distinct gain/cost shapes
(03 §6.2's R-check) — and **BLOCKED in coercive mode**, for the same empty existential that stops the
Defense of the Faith arresting a man in Riverside. The single verdict, per the rubric, is **RICH**; the
coercive block is reported inside it and appears in §11.

---

## 5. PROBE — Magnus Klapp, Temperance *candidate*

**Coordinates as canon leaves him.** Rung: Community/Settlement (a scholar at a cathedral archive) ·
**Office: none** — "candidate" is not a Holding · Church d=3–4 avowed · Convictions **Scholastic 0.35**,
Faith 0.25, `self_other −0.1` · caste-**neutral in practice** (`faction_politics_v30:660` says the
Temperance branch is caste-neutral because Klapp's scholarly focus transcends caste politics — the only
Church branch of which canon says this) · `ts: null` but "TS exposure via archive work."

**What he would hold if seated: Doctrine and Archives.** 08 §4.1 states it flatly — *the Church's
archival monopoly is the largest single power in the game and needs no rule saying so,* because that
Dicastery holds custody of the instruments every other faction's G4 grounds rest on. §2.5 and §3 have
already shown two Cardinals blocked by its absence.

**Option set unseated.** `research` (03 §6.1) — gated by an admission act at a community, held by
persons with stances, and he is inside that gate. `reconstruct` — free in the world, risky in his own
ledger. `tell` — including into a Dicastery's channel. `interview`. `carry` a petition. `commit`.
What he cannot do: `confer`, `revoke`, `determine`, `issue`, `dispatch`, or hold custody. **Custody is a
property of an office, and he has none**, so his reading of the registers deposits `firsthand(read_of
(object))` in *his* ledger and grades G2 for him and G1 for anyone he tells — never G4 for a chamber.

**The Scholar's Dilemma, mechanically.** `ts_gain(p) = κ · Σ confidence(c) × seasons_unresolved(c)` over
**unresolved** anomalous claims. His Scholastic primary is the one conviction in the ecclesiastical
vocabulary that does *not* deposit an early general explanation — a scholar's characteristic act is to
leave a thing unexplained. So his anomalies stay unresolved, and his TS rises from doing his job
correctly. Canon's "Klapp Awakening card" is that sum crossing a floor.

⚠ **And the data it needs does not exist.** `admitting_share` requires each Conviction's **construal
set** — which readings it admits. **No construal-set table exists in the suite or in canon, for any
Conviction.** The mechanism is fully specified and its inputs are absent, so whether Scholastic admits
a rendering-side reading — the single number that decides whether Klapp ever wakes — is unanswerable
from the corpus. Empty cell, §11.

**Verdict: THIN.** He has real epistemic acts and one dominant shape among them (`research`, the only
act in the game that yields verified rootprints), and every consequential thing about him is gated on
a `confer` act performed by another person, which he has **no act to pursue** (see §6). Unseated, the
most powerful office in the game is occupied by nobody and its candidate is a reader.

---

## 6. PROBE — Osten Jarnstal, Fortitude *candidate*

**Coordinates.** Rung: Realm-scope, notional · **Office: none** · Church d=4 · Faith 0.5, **Order 0.3**
(canon reads the Templar arm as Honor + Faith + Authority) · caste-advantaged; the Templar branch is
*structurally closed to Southern Einhir* (`faction_politics_v30:660`).

**The cell this probes: coercive mode inside an institution that holds no army — except it does.** Canon
gives the Fortitude arm Templar garrisons at Cathedral settlements under a strict defensive-only rule
(OFC-04). Under the suite that is a **military power base** (07 §4): *armed persons whose larders the
office fills.* Three things follow with nothing added:

1. **The characteristic cut is the larder, and it is held by another Cardinal.** Templar upkeep runs
   through **Temporal Affairs** — Tormann's establishment. 07 §4: interrupting the larder does not
   disperse armed men, *it makes them their own faction treating plunder as wages*; 14 §1.3 says the
   same in the office layer. **Canon's "Jarnstal Independence card" and "Jarnstal Drift" are that cut,
   derived rather than authored** — and the man who can fire it is the Cardinal whose season is §2.
   Two propositions, jointly unsatisfiable over one stake at one standing date, is 07 §6.1's four
   clusters at war, live and unscripted.
2. **Reach, not size, is the binding constraint.** 07 §10.2's worked case is the party of the Defense
   of the Faith, realm presence 3,100, **capacity zero** in a district three streets long. Coercion in
   the Church is not short of men; it is short of *persons holding binding posts where the act must
   happen*.
3. **Publicity is compulsory.** 14 §1.3: every act by remit runs at `venue_factor ≥ 1.0`. A covert edge
   and a remit are close to incompatible — which is why the Church's enforcement arm can never do
   quietly what Niflhel does nightly.

**Option set as canon leaves him: nearly empty, and this is the finding.** He holds no remit, so
`muster`, `garrison`, `deploy` and `dispatch` are all unavailable. He may `tell`, `commit`, `carry`,
`requisition` fellow members, `counsel` through a tie. **He may not petition for the seat.** A
`Petition` names a `respondent_container` — a containment node — and a Cardinalate sits at a
*realm-scope cluster root*, which is not a container (07 §6.1: an office cluster has no owning node,
so you cannot address a petition to it; you address a person). He may lobby the Confessor, which is
`tell` into a household channel that Deacon Rusk disposes.

> **A candidate for an office inside an office cluster has no up-stroke.** The design's whole
> political-up apparatus — petition, backing, carriage, the drop, grievance — has no legal object here.

**Verdict: BLOCKED.** He wants a seat and the design gives him no act whose object is the seat. What
remains (relational and epistemic lobbying) is real play, and it is play about being *noticed by one
man*, not about the office. On a named faction officer of the peninsula's most institutionally mature
body, that is a serious finding and it is reported as one.

---

## 7. STRUCTURAL PROBE A — the disputed seat

Canon contradicts itself about who is Cardinal of Justice (FINDING 3 #2). **I do not resolve it.** I ask
what the design says happens when two persons each hold a claim to one office and no custody is
determinate.

**7.1 The design expresses it for free, and the reason is a refusal.** 14 §1: *"There is no office
object holding a person. `Holding` lives on the person exactly as commitment edges do, and 'who holds
the praefecture' is a **query**, not a field."* A query over persons returns whatever rows exist —
**two**. Nothing anywhere declares a uniqueness constraint, because there is no object on which to hang
one. The same refusal that makes offices cheap makes a disputed seat free to state *and* impossible to
adjudicate by lookup.

**7.2 Who complies with whom.** 14 §2.2 answers directly and needs nothing new:

```
exercise(o, claimant) = Σ over nodes in scope of compliance_share(n, terms issued by claimant)
de_facto(o)           = argmax over claimants          # may be nobody, and often is
```

Compliance (06 §3) reads local stance toward **the issuer**, `enforcer_presence`, and the local judging
set. So the seat resolves **geographically and per-person**: Himmelenger complies with whoever the
Confessor's household surfaced; the Inquisitorial apparatus complies with whoever dispatches and pays
it; a Grauwald parish complies with whoever its priest heard from, three weeks late, headline-only. The
map of the disputed Cardinalate is the map of the channels — and a man sealing a paper and having a
crier read it is 14 §2.2's ordinary `tell` with `as_asserted = "by remit of the Cardinalate"`, which the
substrate already calls a **lie**: performed, placed, witnessed, traceable, and *effective until
contradicted*.

**7.3 How anyone finds out — and what decides it when nobody knows.** There is no registry to consult
(14 §2.2 is explicit that compliance *does not check one*). A third party's answer to "who is Cardinal
of Justice" is whatever their ledger holds. If it holds nothing, 03 §4.1's empty-view ladder fires:
**marks-based expectation at confidence 0.35**, read off visible marks through the asker's own stance
table. Canon supplies exactly the marks: the Cardinal's red robes, the scales of Justice, the ring, the
blue Justice trim on a Canon's cassock (`faction_politics_v30` §1.4). **Livery decides the disputed seat
in the ledger of everyone who has no better claim** — and it is deposited *with its root*, so it is
refutable by investigation like anything else. That is a genuinely satisfying answer and the design
produced it without being asked.

**7.4 The one venue that could settle it cannot.** A motion *"Olafsson holds the Cardinalate of
Justice"* at Doctrinal Adjudication requires 3 articles, each independently at **G3** (08 §10). The
conferral instrument's custody is **Doctrine and Archives** — the vacant seat. No determinate custody
means no G4, so the article fails its floor, so the sitting closes `CARRIED-WITHOUT-FORCE` for whoever
holds the assessors, banking an F2 hazard on everyone who spoke and incrementing a `pattern` counter
that makes the next attempt heavier. **This is structurally identical to 08 §10.1's Consecration
Crisis, and it was not written for it.** Two contested successions compose; nobody authored either
composition.

**7.5 What the design therefore says, plainly.** *Authority is observed compliance.* There is no fact of
the matter about who is Cardinal of Justice that any person in the world can consult; there is only who
is obeyed, where, and what each observer's ledger says. **The canon contradiction is not a bug the
design must be protected from — it is a state the design can hold.** That is the strongest vindication
of the substrate this lane found.

**7.6 What is at stake in the two branches, since they are not equivalent.** Under Olafsson, the Church's
judicial arm is headed by a Faith-primary administrator with no Thread sensitivity. Under Haelgrund, it
is headed by a **latent TS-15 man whose own perception is degraded on deposit** — the heresy-finding
apparatus run by what it defines as heresy, undetectable to its holder. Those are materially different
games and the choice is not an audit's. **Reported.**

---

## 8. STRUCTURAL PROBE B — the unfilled seats, written as a season

Two of four Dicasteries are vacant-or-candidate (FINDING 4). The design says an office vacancy is *a
standing date with claimants* (14 §2.1). Here is that season.

**8.1 Who convenes it — and the answer is nobody, by construction.** 14 §2.1's fourth consequence:
*"A conferral standing date opens at the horizon **the container carries** (1 season for a wardenship, 2
for a praefecture, 4 for a consecrated office)."* A Cardinalate's node is a **realm-scope cluster root**
(14 §1.5). An office cluster **has no owning node** (07 §6.1). A cluster therefore **carries no
calendar**, and no standing date opens. `convene` is a remit act, so only a person whose remit covers
the seat can set one — the Confessor.

> **A vacancy at a cluster root has no clock and no convener except the one man above it.** That is why
> two seats can stand open indefinitely without anyone failing at anything, and it is the mechanical
> explanation for FINDING 4 that neither corpus states.

**8.2 And it recurses at the top.** 14 §1.5 confers the Confessorate by *"the Cardinals in conclave,"*
14 §2.3 sets its rule at **three of four**. With Temperance and Fortitude empty and Justice disputed,
the conclave cannot reach three. **If the Confessorate empties, the Church has no lawful way to fill
it, and no lawful way to fill the seats that would make the conclave lawful.** Canon supplies a
different route — a **College of Prelates** of five, electing Cardinals by 2/3 supermajority with the
Confessor's endorsement, plus an off-map **Holy See** concurrence (`faction_politics_v30` §1.4, §1.4c).
**The suite has no Prelate rung and no Holy See.** Two incompatible conferral rules for the same office,
one in each corpus. **Reported, not resolved** — and note which way each fails: canon's route works and
is unrepresentable (a College is neither container nor faction nor cluster); the suite's route is
representable and deadlocks.

**8.3 The conferral vector does not exist for this office.** 14 §2.3's coefficient table has rows for a
praefecture, a benefice, a chapter master, a gate wardenship and the Confessorate. **There is no row for
a Cardinalate.** The one conferral this lane exists to examine is the one the table omits.

**8.4 Claimants, and what each brings.** Under the suite's `support(m, candidate) = α·Σ stance(m→marks)
+ β·performance + γ·Σ sponsors + δ·stance(m→candidate)`, with the assessor being the Confessor alone:

| seat | claimant | brings | reads against a Faith-primary assessor |
|---|---|---|---|
| Temperance | **Magnus Klapp** | Scholastic 0.35; caste-transcendent standing; custody of every G4 in the game | β high (canonical scholar); **α ambiguous** — the assessor's stance toward *Scholastic* is the whole question, and canon's Arc B says a Temperance Cardinal is the one person who could break him |
| Fortitude | **Osten Jarnstal** | Faith 0.5 / Order 0.3; the Templar arm; a military basis funded by another Cardinal | α high (mark-aligned), β unevidenced in canon, δ unstated |

Neither can *act* on the outcome (§5, §6): a candidate has no up-stroke to an office cluster. The
"standing date with claimants" has claimants who cannot appear at it, at a date that does not exist,
before an assessor whose coefficient row is unwritten.

**8.5 What happens to every dispensation the previous holder issued — and canon names no previous
holder.** 14 §2.1's first two consequences are keyed to a prior occupant: standing dispensations keep
their terms and lose their complier *at telling speed*; `S_post` empties and `licensed_standing` goes to
zero. For a seat vacant beyond living memory, both are empty, and the substrate's persistence rule
(01 §2) bites: *a person persists exactly as long as somebody remembers them*, so the last Cardinal of
Temperance has **de-individuated into a cohort**. His archival rules are still in force. Compliance
reads the local stance toward *the issuer* — and the issuer is no longer a person anyone's ledger names.

> **The Church's archive runs on standing terms issued by a man the world has forgotten, with no
> complier to lose and nobody entitled to revoke them.** The design has no object for this state. It is
> excellent fiction and an honest hole.

**8.6 The season, then, in seven phases.** P0: no conferral date fires, because none exists. P1: the
precinct eats; the archive's registers age and their facets decay (03 §6.1's `retention`). P2: Klapp's
COMMITMENT need rises, Jarnstal's likewise; neither generates a petition, because there is no
respondent container. P3: the Confessor's view holds twelve claims, none about the vacancies, because
nothing has been raised. P4: Klapp `research`es; Jarnstal `tell`s; Himlensendt performs a visitation.
P5: nothing binds. P6: three witnesses in a hamlet. P7: a register's facets fall below retention.

**The season passes and the seats stay empty. Nothing failed. Nobody was blocked by an opponent.** That
is the diagnostic: **SPECTATOR at the institutional layer** — not for a person, for a *structure*. The
richest untested structure in the design contains two offices that no act in the design can fill,
because the acts that fill offices are keyed to containers and this office has none.

**8.7 The conferral dilemma, reported.** §3.2 of the suite's index puts it as the one thing to settle
first. The Church is where it bites hardest, in both directions: **person-rooted**, every Cardinal's
`Holding` names Himlensendt as conferrer, so on his death every Church office in the peninsula names a
dead conferrer and the cluster's whole graph terminates at once — and the Crown's own consecration
warrant, which 14 §3.3 makes *external and in Church custody*, terminates with it. **Office-rooted**, the
office of Confessor performs the game's most consequential act (consecrating a king) and ruling B-11
forbids an institution performing it. **Not resolved here.**

**8.8 And a structural fact the suite does not state.** 14 §3.3 requires that *the conferral graph
terminate*. The Church's does not: the Confessor confers the Cardinals, and the Cardinals in conclave
confer the Confessor. It is a **cycle**. 14 §2.4 permits `revoke(r, office, holder)` when the office
lies in `r`'s conferral subtree — and in a cycle, each Cardinal lies in the Confessor's subtree *and*
the Confessor lies in each Cardinal's. **Revocation is symmetric**, which makes 14 §1.5's own entry for
the Confessor — "revocable by: conclave, contested" — the design half-noticing it. `sovereign_fraction`
(14 §6) is then undefined over every Church office, since no conferral path leaves the component. The
Church is the one body in Valoria whose authority has no root outside itself, and canon's answer — the
off-map Holy See — is precisely the suite's open question about *an off-board polity acting without a
person to carry it*.

---

## 9. What this lane tested hardest

### 9.1 Correspondence filtering: the routing act, performed

**Setup.** A denunciation of a Southern Einhir Canon arrives at Himmelenger. Sixty-one items reach the
Confessor's household this season; **Deacon Halvard Rusk** dispositions forty-four of them.
`filter_share(Rusk) = 44/61 = 0.72`. He holds no standing, binds nobody, confers nothing, and because
`choose(person, view)` has no world argument, **what he surfaces is what the Church knows.**

His three dispositions (03 §8) are not equal in cost. **Suppress** drops it, tells the petitioner
nothing, and deposits a record of the suppression *in his own ledger* — findable by `reconstruct`, which
is the only reason it is risky at all. **Surface** passes it framed, and is *more powerful and leaves
less trace*, because his construal arrives at the top of the principal's view. **Approve** attaches his
endorsement as a `SAID` row.

**Then the routing choice, which is the contestable one.** The channel an item enters is set by its
proposition's subject, so Rusk chooses the subject under which he writes it up:

| written up as | routes to | fate (suite labelling, 03 §8) | fate (canon labelling, §7.3) |
|---|---|---|---|
| heresy | Defense of the Faith | **ruinous** — a summons tribunal hearing confession | Templar enforcement — men, not a trial |
| a question of interpretation | Doctrinal Adjudication | survivable — G3 floor, articles, a Cardinal's determination | **the Inquisition and Heresy Proceedings** |
| a question of benefice and jurisdiction | Temporal Affairs | deferrable — account rolls only, next reckoning | same |

**Two findings.** First, under either labelling the *routing* is the decision and the Cardinal at the
end is not consulted about receiving it — which is the design's claim, demonstrated: a deacon outranks
four Cardinals on this item and no rule names the Dicasteries. Second, and damaging: **two of the three
branches lead to seats that are empty or disputed.** Route it to Fortitude and there is no Cardinal to
determine; route it to Justice and there are two claimants and no determinate custody. The router's
real menu is one live branch and two voids. *The vacancies do not merely leave posts unfilled; they
collapse the parallel-channel structure that is the Church's whole design interest.*

**Counter-play exists and none dominates** (03 §8): a **Knot** to the principal bypasses correspondence
entirely (cost: strain, and it is TS-gated, which is why the peninsula's deepest channel is the one
formal institutions cannot use); making the item **public** so the principal witnesses it (cost:
publicity binds him to respond and courts a hostile construal); suborning Rusk (cost: a man who now
holds something on you). And Rusk's own exposure is *one backer with an `interview` act*.

### 9.2 The office cluster's admitted cost — is it bearable?

07 §6.1 pays the price out loud: an office cluster has no owning node, so *"the Dicastery decided"* is
permanently inexpressible; only *"the four persons holding these posts each did something."*

**In the fiction, it is not merely bearable — it is better.** Nothing in this document wanted an
institutional speaker. Tormann's levy, Olafsson's determination, Rusk's routing and Himlensendt's
visitation are all sharper as named acts by named men, and 07 §6.1's dividend is real: four clusters
can be at war inside one Church with no institutional machinery, and §2 and §6 show it happening over
Templar upkeep.

**At the door, the cost was under-priced, and this lane found four consequences 07 did not name.**

1. **A petition cannot name a Dicastery as respondent** — no container, no `respondent_container`. So a
   grievance against a Dicastery has no legal up-stroke (§6).
2. **A cluster seat's vacancy opens no standing date**, because the horizon is carried by a container
   (§8.1). Vacancy has no clock.
3. **Custody is a property of an office**, so a cluster whose custodial seat is empty voids the G4
   grade of every instrument it holds — which is the archive every other faction's proof rests on
   (§2.5, §3, §7.4).
4. **The cluster's conferral graph closes into a cycle** with no external root (§8.8).

**Verdict: bearable for a Dicastery with a Cardinal; unplayable for a Dicastery without one.** Two of
four are without one at game start. The cost 07 accepted is not "the fiction must not render an
institution as a speaker" — it is "**an office cluster cannot be addressed, cannot be scheduled, and
cannot certify its own records when a seat is empty.**"

---

## 10. CELLS POPULATED

Mode of play (E) × rung (A), from the six characters and two structural probes above. A cell is listed
only where a season above actually demonstrates a legal act with a consequence.

| mode | cells this lane demonstrated | by whom |
|---|---|---|
| **Material** | Realm → Territory → Hearth: `LevyTerm`, arrears compounding, a hearth's larder falling | Tormann §2.6–2.7 |
| **Epistemic** | Realm: catechetical `tell` as a general explanation; a held claim that never surfaces (×2, two different harms) | Himlensendt §1.4/§1.6, Tormann §2.4 |
| **Epistemic** | Settlement/Territory: `examine`, `interview`, `surveil`, `research`, `reconstruct` by a person with **no office**; degraded deposit into a ledger with no address | Haelgrund §4 |
| **Epistemic** | Community: `research` as the only source of verified rootprints, gated by an admission act | Klapp §5 |
| **Political-down** | Realm: `issue` + publication by funded channel + the compliance contest + reach failure where benefices are unfilled | Tormann §2.6 |
| **Political-down** | Realm: the **routing** of an inbound item as itself a political act | Rusk §9.1 |
| **Argument** | Realm: `admissible_source` as a door (account rolls only; registers only); G3 floor; `CARRIED-WITHOUT-FORCE` as the normal Church outcome | Olafsson §3, Tormann §2.7, §7.4 |
| **Institutional** | Realm: `confer`/`revoke` at a cluster root; the patronage cascade; `convene` and agenda order as the cheapest real power | Himlensendt §1.5, Tormann §2.5, §9.1 |
| **Relational** | Realm: `requisition` at d=5 by a man with no establishment; a dual-loyalty agent in a rival's channel | Himlensendt §1.5 (Linder) |
| **Coercive** | *demonstrated only as a hole* — see §11 | Jarnstal §6, Haelgrund §4 |

Cross-cuts exercised: **B** — office cluster (all four), office cluster **with** an establishment
(Tormann, Olafsson) versus **without** one (Himlensendt), and **candidate = no office** (Klapp,
Jarnstal). **C** — degree 5 avowed, degree 4 sworn, and *two rival propositions held by the same person*
(Tormann: the Church's and Temporal Affairs' party's). **D** — Church standing as `rank` 6; livery as the
marks-based default that decides a disputed office (§7.3); latent, unread Thread sensitivity (§4).

---

## 11. CELLS I FOUND EMPTY

Every item is a place the design gave a Church character nothing to do, or gave the corpus no way to
answer. None is patched.

**Empty cells in the E × A matrix**

1. **Coercive × any rung, for the Church.** No inquisitorial or Templar **post** exists in 14 §1.5's
   roster, so the arm that canon builds two sub-ladders on has no binding power in the suite. `arrest`
   returns an empty existential (07 §10.2) for the Defense of the Faith and for a Field Inquisitor
   alike. The Church can prove and cannot take.
2. **Political-up × office cluster.** A candidate for a Cardinalate has no legal `Petition`, because a
   cluster is not a `respondent_container`. **Jarnstal is BLOCKED for exactly this reason** (§6), and so
   is any person with a grievance against a Dicastery (§9.2 #1).
3. **Institutional × vacant cluster seat.** No standing date opens; no convener exists but the office
   above; no conferral coefficient row exists for a Cardinalate (§8.1, §8.3).

**Objects the design names and does not supply**

4. **Construal sets.** `admitting_share` (03 §9) sums Convictions whose construal sets admit a
   rendering-side reading. **No construal-set table exists anywhere in either corpus**, so whether
   Klapp's Scholastic primary ever lets him wake is unanswerable (§5).
5. **A conviction-weight bridge.** Canon's fractions and the suite's 0..5 stance weights have no
   conversion, and every need arithmetic in this document depends on the mapping I stated in §0.2.
6. **Stats for the Church's leadership.** `stats: null` for Himlensendt, Tormann, Olafsson, Klapp,
   Jarnstal. `K = 7 + Focus` is therefore uncomputable for all five (§1.2).
7. **An issuer who is a cohort.** A dispensation whose issuer has de-individuated has terms in force and
   no complier to lose; compliance reads a stance toward a person nobody's ledger names (§8.5).
8. **The Church Attention Pool.** Canon's `AP` (Haelgrund deploys at AP ≥ 3; a copyist raises it) is a
   place-owned gauge, and the suite refuses those categorically (01 §6). The nearest suite object,
   `exposure(edge)`, is per-secret and per-observer, not per-territory. **AP has no home**, and
   Haelgrund's own deployment trigger therefore has no mechanism.
9. **A College of Prelates.** Canon's five-member electing body is neither container, faction, nor
   office cluster. The suite's Church has no rung between Canon and Cardinal (§8.2).
10. **The Holy See.** Canon's off-map concurrence for a Consecration is the suite's open question about
    off-board polities acting without a person to carry them, arriving inside the Church's own
    conferral graph (§8.8).

**Motivational and structural holes**

11. **STANDING urgency is 0 for every ecclesiastical person**, because `care` reads Honor and Identity
    and the ecclesiastical conviction template contains neither — against a canon Church career ladder
    of seven rungs (§1.3).
12. **The Church's conferral graph is a cycle** with no external root, making `revoke` symmetric between
    Confessor and Cardinals and `sovereign_fraction` undefined over Church offices (§8.8).
13. **Canon's Arc B for Himlensendt is currently unreachable**, because a scholarly finding arrives as
    testimony and the testimony half of the salience floor is **retracted and held open** (16 §3.2).
    Reported as open, per instruction.

**Contradictions carried, not resolved**

14. **One act or ten** per season for an office-holder (09 §1.1 vs 14 §8) — decides whether the Confessor
    is a head or a bottleneck, and flips his verdict from THIN to RICH (§0.1, §1.8).
15. **Who is Cardinal of Justice** (FINDING 3 #2), plus TS 12 vs TS 15 for Haelgrund. Both branches
    written (§3, §4, §7.6).
16. **Which Dicastery owns heresy** — canon and suite have the functions of Doctrinal Adjudication and
    Defense of the Faith swapped, which materially changes what routing an item *does* (§0.4, §9.1).
17. **Who confers a Cardinalate** — the Confessor alone (suite) or a College of Prelates by 2/3 with the
    Confessor's endorsement (canon) (§8.2).
18. **The conferral dilemma itself**, at its sharpest point: person-rooted kills the whole Church graph on
    one death and takes the Crown's consecration warrant with it; office-rooted has an institution
    consecrate a king (§8.7).

**Verdicts, in one line each.** Himlensendt **THIN** (one act dominates by shape; no compounding cost
exists for an office with no establishment). Tormann **RICH** (seven live options, four genuine forks —
and the only Cardinal canon seats outright). Olafsson **RICH**, hostage to a vacant custody. Haelgrund
**RICH** in epistemic mode, blocked in coercive. Klapp **THIN** (a reader; the game's largest office is
one `confer` away and he cannot reach it). Jarnstal **BLOCKED** (no act has his object). The unfilled
seats, as a structure: **SPECTATOR** — a season passes, nothing fails, and nothing can fill them.
