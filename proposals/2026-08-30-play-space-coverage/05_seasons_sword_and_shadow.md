# 05 — Seasons: Sword and Shadow (Lane 4)

## Status: FILED (2026-08-30) — a coverage probe, not a design. Nothing here ratifies on merge.
## Lane 4 of the play-space coverage instrument (`00_PLAN.md`). Authority on mechanism: the merged
## suite at `proposals/2026-08-29-valoria-from-scratch/`. Authority on people: `canon/`, `references/npc_registry.yaml`.
## **No new mechanisms.** Where a season could not be written because the design lacks something, the gap is the output.

**The two cells this lane owns and nobody else touches:** *coercive play by a person who commands
sworn people rather than a levy*, and *covert play, where the point is that acts deposit no claims.*

---

## 0. Two rulings applied before the first season

**Niflhel is not a faction.** The strike (`CR-STRIKE-2026-04-19`, ED-707/ED-764) is authoritative and
this document treats it as settled. `faction_politics_v30.md` §2.6's four-arm ladder is stale text; so
is the timeline's live faction row. The named people survive: Kolbrun Thale still has waterfront
contacts, Tomas Vorn is still a Goldenfurt broker, Dalla Virke is a syndicate broker whom the registry
had already reassigned (`faction: Independent (Virke syndicate — Niflhel DISSOLVED)`). Canon's own
replacement is `settlement_layer_v30 §4.8`: *"Individual NPCs in specific settlements who sell
information. **Not coordinated** — each operates independently for personal profit."* That sentence is
the brief for §4 below, and it turns out to be a sharper test of the design than the contradiction was.

The merged suite names Niflhel in five places (07 §1.3, §10.2; 09 §5.3's serjeant table; 14 §4; 02
§4.2). Every one of those passages is making a claim about a **caste-open covert body on a waterfront**
and none of them needs the name. I have used the mechanism and dropped the name, and flag it here so a
later reader does not mistake the suite's usage for evidence against the strike.

**The Grandmaster's name is NOT resolved.** `npc_registry.yaml:721` says **Lisbeth Ehrenwall**
(`status: canonical`, NPC-070); `canon/03_canonical_timeline.md:145` says **Sigrid Ehrenwall**. I use
**Lisbeth**, for one reason and it is not authority-ranking: the timeline's variant is the first name of
**Sigrid Torsvald**, who is the *other* full season in this lane, and writing both under one first name
would make the epistemic asymmetry between them unreadable. The merged suite propagated the timeline's
version (doc 14 §1.5, §4, §6 all say "Sigrid Ehrenwall"), so a reader arriving from the suite should
know the two documents disagree. **Reported, not resolved.**

---

## 1. FULL SEASON — Grandmaster Lisbeth Ehrenwall

### 1.1 Coordinates

**A · rung** — her *address* is a containment node (Ehrenfeld Citadel, in the settlement of Ehrenfeld,
Valorsmark); her *office* is not on that ladder at all. Grandmaster is the **root of an office cluster**
(14 §4), a set of chapter offices at many nodes whose conferral paths meet at her. She stands at
Settlement and reaches at Realm.
**B · office** — cluster root, `binds = members-by-admission`. Her decisions bind persons who walked
through an admission gate. **She binds nobody by presence anywhere in the peninsula.**
**C · alignment** — avowed, at the top of the scale, toward the order's own proposition; and a second
edge, the oath: *(the Crown-as-institution, holds, the peninsula, all-time, **ought**)*.
**D · marks** — order-mark, caste-open; the post-mark of Grandmaster with conferrer = *the chapters'
sworn brothers*, basis **deed**; **TS 0** (registry), which is itself a read mark.

### 1.2 Opening state — the six person fields

| field | contents | what is conspicuously absent |
|---|---|---|
| Address | Ehrenfeld / Valorsmark / Valoria | nothing; ordinary |
| Marks | order-mark, post-mark(Grandmaster, conferrer = chapter sittings), **TS 0** | heritage is **SILENT** in canon — I do not invent one |
| Capability | **SILENT** (registry: `stats: null`); Certainty 4, resonant style Consequence | the pool she would roll — but §1.5 shows it barely matters, and that is a result |
| Stance | Order 0.60, Liberty 0.20, self/other −0.10; Voss's disposition toward her is −1 | no stance row toward Thread Sensitivity, ever |
| Memory | chapter reports, Crown correspondence, Kreutz's dual-allegiance traffic | **no rendering-side facet, in her whole life.** TS 0 sets `P(register) = 0` |
| Ties / Knots | Kreutz (liaison, allegiance pre-designated to Almud personally), Brandt, Torsvald | **zero usable Knot slots.** `form_knot` requires TS ≥ 30 **on both sides** (02 §4.2) |

That last row is the season. The suite calls a Knot *"the only channel by which a person holding no
post receives news, opportunity and obligation faster and cleaner than the crier"* — and its inverse is
that the deepest channel in the game is **unavailable to the commander of the realm's covert arm.** She
runs a covert branch through a channel she is constitutionally unable to use. Nothing wrote that; two
numbers (TS 0, TS ≥ 30) produced it.

### 1.3 Computed needs, with the arithmetic

Needs are computed each tick from her situation (01 §2), never stored, and they do not all read the
same thing.

- **subsistence — reads the WORLD.** Her establishment is *every chapter's riders* (14 §1.5) and an
  establishment eats (14 §1.3). `faction_canon_v30:372`: Löwenritter hold **no Mandate and no Wealth
  pre-coup**; the larders are filled by the Crown. So her subsistence need is not her own belly, it is
  `arrears(p)` on several thousand armed men she does not pay. Doc 12 §1.2: each season of arrears
  subtracts **0.20** from every rider's `will()`; three seasons is **−0.60**, more than the entire
  baseline of 0.30. Doc 12 §6.4 then runs to its end: unpaid armed men do not disperse, they become
  their own faction and treat plunder as wages.
  **Canon's authored "Graduated Autonomy" track (Loyal → Restless → Autonomous → Split) is that
  subtraction, three times.** I did not have to reach for it; it is `0.30 − 3 × 0.20`.
- **standing — reads the WORLD.** `standing(p,n)` is computed from her support set. Her bases (07 §4):
  **merit/deed** (chapter sittings, whose `admissible_source` is *witnessed deed only*, 14 §5) and
  **military** (armed persons whose larders are filled). Two bases → `cuts_available = 2`, and by 07
  §4.2 a challenger needs a coalition landing ⌈k⌉ = 2 cuts in one standing-date window.
  **But the military cut is not held by any rival — it is held by her paymaster.** The Crown fires it by
  simply not paying, and doc 07 says that cut *"manufactures a hostile faction that has military
  capacity."* The King's only lever against her is the one that arms her against him.
- **commitment — reads her VIEW.** Order 0.60 against the oath's proposition. Unsatisfied only if she
  *believes* the peninsula's order unheld — which is a question about what reached her ledger.
- **exposure — reads her VIEW.** A Crown levy dispensation reaches her as a claim; her options are
  recomputed over changed terms.

### 1.4 The view, and the claim that does not surface

P3 assembles at most **K = 12** claims, ranked by `recency × confidence × relevance × stance weight`.
Her docket this season: the Crown's request that Löwenritter riders garrison a Grauwald settlement and
disperse a gathering; Kreutz's report; a chapter's arrears complaint; Brandt on Altonian movements;
**Haldorsen's mission report at confidence ≈ 0.9, firsthand**; and, somewhere far down, **Torsvald's
report at confidence ≈ 0.2**.

Torsvald's report is a rendering-side claim, and doc 03 §9 is unambiguous about what happens to it on
deposit into a TS 0 ledger: the subject — a *configuration* — has **no address in that ledger**, so the
claim degrades on deposit. Subject replaced by the nearest referent Ehrenwall does have (the place),
predicate by the nearest available form, value collapsed to a band: `CONDITION(the mill, wrong)` at
0.2. Haldorsen's competing claim is `MISSION(complete)` at 0.9 firsthand, from an Authority-styled
officer with certainty 5, aligned with an Order-0.60 stance.

**On confidence alone Haldorsen outranks Torsvald 4.5:1, before stance weight is applied.** Her claim
does not make twelve. It sits in the greyed-out panel doc 03 §10 provides: *you know this and you are
not thinking about it.* Raise Ehrenwall's Focus to the ceiling, give her Torsvald's report **in
Torsvald's own hand**, and nothing changes — the barrier is in the receiving ledger's referent space
and has no organ anyone can open.

### 1.5 The option set, and why each act is legal

| act | legal because | note |
|---|---|---|
| `convene` a chapter sitting; **order its items** | remit act (14 §1.1); the convener's agenda power (14 §5) | the cheapest real power she holds — three items ahead of yours kills your petition with seat capacity, not refusal |
| `confer` a chapter mastership | remit; conferral is `admit()` (14 §2.3) with the Löwenritter vector **α 0.2 · β 3.0 · γ 0.3 · δ 0.3, any two of three** | **caste-openness is this row, not a policy.** β = 3.0 on witnessed deed against α = 0.2 on marks means a Southern Einhir brother clears on deed alone |
| `revoke` a chapter mastership | it lies in her conferral subtree (14 §2.4) | |
| `dispatch` riders / Riskbreakers | remit act = `requisition` on an establishment member | the pool rolled is **the dispatched man's**, never hers (14 §1.2) |
| `issue` a dispensation | remit — but `binds = members-by-admission` | **she cannot issue anything binding on a town.** See the gap below |
| `carry` a report to the King | she is one of **three unfiltered channels** to the Crown (03 §8) | no chamberlain, no steward, no Confessor between her and Almud |
| **refuse** a royal request | the King did not confer her office; 14 §6 — *"an office cluster the King may petition and may not command"* | see §1.6 |
| `commit` / `avow` at publicity ≥ 1.0 | any person may | an office-holder **cannot act quietly** (14 §1.3) |
| `form_knot` | **ILLEGAL.** TS 0 | the one act on this list she is structurally barred from |
| act at `visibility = concealed` | available for non-remit acts only | every act *by remit* runs at `venue_factor ≥ 1.0` |

**The gap this table exposes.** Canon puts the **Knights of the Peace** and the **Royal Guard** under
the Löwenritter umbrella (`faction_politics_v30` §2.1), and both bind persons *by presence* — a Knight
of the Peace deposits `arrest` on a fisher who admitted him to nothing. Under the suite her remit cannot
reach that: `binds = members-by-admission` is what a cluster root has. The only construction the suite
allows is that those men hold a **second, Crown-conferred office** alongside their order-mark — two
conferral roots on one person, which is precisely doc 14 §4's akıncı case, and it produces with nothing
added the Royal Marshal's canonical grievance (Voss at −1 toward her: *"the Order answers to its own
Grand Master, not to the Crown chain"*). The design covers it. What it does not cover is who pays for
it, which is §1.8.

### 1.6 The choice and its resolution, through the seven phases

**P0 CALENDAR.** A chapter sitting falls due at Ehrenfeld. So does the Crown's standing date at which
the Grauwald request is put. Option availability recomputes.
**P1 SETTLE.** Metabolism only. The riders eat; the Crown's coin is one season late; `arrears` ticks to
1 in two chapters. No social quantity moves here — by phase membership, not by discipline.
**P2 NEEDS.** As §1.3.
**P3 VIEW.** As §1.4. Torsvald's claim is crowded out.
**P4 CHOOSE.** One act, and the tick gives her exactly one. Three shapes are available: comply with the
Crown by dispatching riders; refuse; or convene her chapter and spend the season on the arrears. She
**refuses, and carries the refusal to the King herself** through her unfiltered channel — which is one
act, because a refusal delivered in person is a `tell`.
**P5 RESOLVE.** Stratum 2 (binding decisions), before contested physical acts and before social acts.
Nothing physical happens. The event is a sentence spoken in a room.
**P6 WITNESS.** Divergent, per person, and this is where the season's weight lands. Doc 12 §6.3: office
is a mark plus a binding power, and **binding power is not stored — it is observed compliance.** Every
witnessed refusal deposits `(order of Almud, was_obeyed, false, when, firsthand)` into every witness's
ledger, and `will()` reads that ledger at ±0.15 per point of `obeyed_claims`. The refusal is witnessed
by the Crown council — Voss, Reichard, Thale, Linder, Kreutz — at publicity 2.0.
**P7 RECKON.** Confidences decay. Nothing is forgotten yet.

**The arithmetic of what she has just done.** She spent no coin, broke no law, moved no man, and lowered
the willingness of every person who saw it on the King's *next* order — which makes the next refusal
likelier, which is witnessed by more people. Doc 12: *"authority collapses the way a bank run does."*
**The Grandmaster's refusal is the most contagious single act available to anyone in this roster**, and
it is free to her, because the King holds no cut against her that does not arm her.

**What the Crown can actually do about it.** Requisition, not command:
`obstacle = base + burden − 2·w(d) − regard(her→Almud)/2 − conviction_bonus`. At sworn (d = 4), `2·w(d)`
is **−3.2**; at constitutive (d = 5) it is **−4.4 and no offer term enters the check at all.** So the
King's ask is cheap and can still fail, and no amount of money changes the second case.

### 1.7 What propagates

**Up-stroke:** her report, carried by her, unfiltered, into the King's view — the design's clearest case
of a person bypassing a correspondence channel by holding a channel of their own.
**Down-stroke:** nothing. Her `issue` binds members-by-admission; the Grauwald hamlet never hears any of
it. **A Grandmaster's decision does not reach a commoner except through a man on a horse.**
**Sideways, and furthest:** the refusal claim, by ordinary witnessing, into five inner-circle ledgers and
onward by `tell` as far as those five choose. It travels further than anything she could order.

### 1.8 Diagnostic — **RICH**, with one structural finding against the suite

Several live options with materially different consequences: refuse (free now, arms the arrears cliff),
comply (spends `sever`), convene and spend the season on her own house, confer a Southern Einhir chapter
master on deed alone — a Path-B-shaped act performed by an Order-primary conservative for reasons that
have nothing to do with Vaynard's.

**R-check.** Refusal's gain is immediate and compounds through `obeyed_claims`; its cost is the
paymaster's goodwill, which compounds through `arrears` toward a cliff at three seasons. Compliance's
gain is the coin continuing; its cost is `sever`. Both arms compound on both sides. **Neither
dominates.** Passes.

**The `sever` result, which is this lane's best emergent finding.** Doc 12 §1.2:
`sever = max(1.00 kin/Knot, 0.80 × community share, 0.50 × heritage share)`, weighted −0.55. The
Löwenritter is **caste-open**, so an order to disperse a Southern Einhir gathering is given to a body
containing Southern Einhir brothers, for whom `sever = 0.50` → **−0.275 of willingness**, enough on its
own to put an otherwise-obedient man under the 0.50 line. Doc 09 §5.3 credits the *same* caste-openness
as a battlefield advantage: a Crown levy that loses a serjeant in Grauwald cannot refill the role
(`Standing 3+ via public deeds or inner-circle sponsorship` — *almost nobody present*), while a
Löwenritter formation closes it in one exchange, because its role gate is `order-mark, caste-open`.

> **The same field makes the order the only body that can hold a Grauwald battle line and the least
> willing body to police a Grauwald street.** Caste-openness is a military asset and a coercive
> liability, out of one column, with no rule naming caste. Neither the suite nor canon says this; it
> falls out of `sever` and the role gate read together.

**The finding against the suite, reported not resolved.** Doc 12 §2.1 offers two channels for armed
force: **Levy** (authorised by dispensation, routed by containment, high `sever`, fails by refusal) and
**Retinue** (authorised by *a person's own coin*, routed by alignment, low `sever`, fails by arrears).
The Löwenritter is **neither**: routed by alignment, paid by a third party. Both columns assume the
payer and the orderer are the same person, and doc 12 §9.1's levy/hire R-check inherits that assumption.
Split them and the fork's cost analysis is wrong in both arms — the commander gets low `sever` without
carrying the arrears risk, and the paymaster carries the arrears cliff without the ability to give an
order. **That is a missing third column, and it is exactly the object canon calls the Autonomy track.**
I am not writing it. The gap is the finding.

**The conferral dilemma, live — and narrowed.** The suite's NERS audit (16 §6) names this character as
its evidence that conferral must be **office**-rooted: *"the military order sworn to the Crown as
institution, not the bloodline — a warrant that is meaningless if conferral is personal."* Writing her
season shows that **the evidence does not bear that weight.** Her warrant does not run through the Crown
under *either* answer: the Grandmastership is conferred by the chapters' sworn brothers on a deed basis,
so the King is not in her conferral subtree and cannot revoke her whether conferral roots at persons or
at offices. What the oath actually is, in this design, is an **alignment edge plus a stance row** — a
degree on one edge, setting `2·w(d)` in a requisition obstacle. Its wording is not a legal fact.

So the dilemma is **untouched and still open** (the sovereignty query, the praefect who becomes
irrevocable to the next king, the Crown across a succession) — but one of the two pieces of evidence
cited for the office-rooted answer is spent. **Reported. Not resolved. Not decided.**

### 1.9 Cells populated
`Realm-scope cluster root` × `Coercive` · `Institutional` · `Relational` · `Political-up`.
`binds members-by-admission` demonstrated as *materially different from* binds-by-presence.
`Realm-scope cluster root` × `Political-down`: **demonstrated CLOSED** — she has a remit and it reaches
nobody who did not join.

---

## 2. FULL SEASON — Sigrid Torsvald, TS Riskbreaker (Covert)

### 2.1 Coordinates

**A · rung** — Individual, mobile. Her address this season is a Baralta dock district; her containment
parent is wherever she is quartered, and it changes.
**B · office** — **none.** The Riskbreaker "ladder" is not an office under this design: a remit's acts
are performed at `venue_factor ≥ 1.0`, and *"a covert edge and a remit are close to incompatible"*
(14 §1.3). She binds no one.
**C · alignment** — two edges on one person: Löwenritter, **avowed**, at member/sworn; and the
Riskbreaker proposition — canon's *"hidden conviction: Valoria (nation as idea)"* → *(Valoria, endures,
as an idea, all-time, **ought**)* — held **covert**, at **d = 4 sworn**, the degree that may be
requisitioned *for acts against her own container's interest.*
**D · marks** — **TS 35**, Thread Pool `floor(35/10) = 3`; Utility 0.40, Honor 0.20; heritage SILENT.

### 2.2 Opening state

Ledger: mission claims, `SAID` rows from three interviews, and a class of rows nobody else in her chain
of command holds — **rendering-side facets**, registered because `P(register) = 0 if TS < floor(f)` and
her 35 clears floors her colleagues cannot.

**Conspicuously absent:** any claim she could *hand upward intact*. And any Knot partner inside her own
institution. `form_knot` requires **TS ≥ 30 on both sides**. Ehrenwall is TS 0. Haldorsen is TS 0. Almud
is TS 0. Her partners must come from the TS ≥ 30 minority, which in this setting skews **Southern
Einhir** — the population every formal institution gates out.

> **The covert operative's only high-bandwidth channel runs, by arithmetic, to the people her own order
> is least able to admit.** Formal exclusion and informal advantage on one threshold (02 §4.2), pointed
> at a character canon never wrote it for.

### 2.3 Computed needs

- **subsistence — WORLD.** Fed by the order. Not pressing, which is exactly what makes her available for
  a mission at all.
- **standing — WORLD.** Her support set is small and covert. A covert edge deposits no membership claim
  into a judging set, so **most of her support set is invisible to the standing computation any observer
  runs** — including hers.
- **commitment — VIEW.** Utility 0.40 against a proposition she holds covertly. And her canon goal
  *"minimise Thread collateral"* is a stance row toward a referent **nobody else in her order has an
  address for.**
- **exposure — VIEW.** She holds the requisition, so it is in her view — and separately
  `exposure(actor, operation)` (03 §7), the paired counter that rises per extraction and falls per
  `cover` act.

### 2.4 The view, and the claim that does not surface

Her K = 12 is dense with `SAID` rows, and the one claim that never leaves it is the mirror of
Ehrenwall's: the thing she holds that **cannot be transmitted at all**, in any direction, by any act on
her list.

She could tell it — `tell` degrades on deposit. She could write it and file it in an archive —
`research` → `read_of(record)` degrades on deposit, on the same rule: *"whether it arrived from a
speaker's mouth, off a page in the Dicastery archive, or out of the hearer's own inference."* She could
Knot it — no partner at TS ≥ 30 in her chain. She could argue it at the chapter sitting — its
`admissible_source` is **witnessed deed only** (14 §5), so a document cannot enter the room, and a deed
witnessed by one sensitive corroborates exactly once, because corroboration is measured on distinct
firsthand roots.

### 2.5 The option set, and where it stops

**Available, and richly — the epistemic mode is the best-served cell in this lane.** `examine` (Acuity
against `retention(f) = base × 2^(−age/halflife) × (1 − concealment_spend)`) · `interview` (which leaks:
it deposits `INTENDS(you, investigate X)` in the subject's ledger, tellable onward) · `surveil` (slow,
quiet, accrues exposure to *her*) · `research` (gated by an admission act held by persons) ·
`reconstruct` (root identification — the act that resolves an opaque token to a named person) ·
**`Thread-Read`** (pool 3 + Attunement: prior configurations, a person's Conviction-primary, the
orphaned configuration left by memory-pulling, Knot residue — *and it produces claims most people cannot
be told*) · `plant` · `tell` with `as_asserted ≠ held` · `form_knot` with a qualifying partner · `cover`
against exposure · any of it at `visibility = concealed`, at a reduced pool and more time.

**Not available — and each is closed by a different mechanism.** What she wants is for Thread collateral
to *count*.

- She cannot **petition** it. A petition is a proposition and must be `carry`-ed by a named person at
  each rung; every non-sensitive carrier's ledger degrades the subject on deposit. It arrives one rung up
  as *something is wrong at the mill*, at 0.2, and is dropped — not maliciously, and the dropper could
  not tell you what he dropped.
- She cannot **argue** it. No venue in doc 14 §5 admits her evidence: the chapter hears witnessed deed;
  Doctrine and Archives hears **instruments only**; the Defense of the Faith hears firsthand testimony
  and confession — and testimony is the half of the salience floor the suite's own audit (16 §3.2)
  records as **held open, not patched.**
- She cannot **refuse without paying for it**, and this is the sharpest hole in the lane.

> **The requisition `burden` term cannot represent her.** `burden = cost to the member's computed need +
> 2 × harm to the member's container's stake + 3 × marks the act collides with.` Thread collateral is
> none of the three: not her need, no harm to her container's stake, colliding with no mark. So her
> refusal scores as a **low-burden refusal**, and 07 §1.2 is explicit — *"refuse at low burden and the
> edge drops a degree."* **Every time she aborts for the reason canon says defines her, the design
> charges her a degree of commitment.** Four aborts and she is below the degree that can be dispatched
> to the places where she is the only person who can see anything.

That is a real mechanism gap, it is load-bearing on the game rather than on apparatus, and I am not
patching it. The burden term reads three sources of harm; the setting's central asymmetry produces a
fourth.

### 2.6 The choice and its resolution

**P0.** No standing date binds her; covert play has none (§5). **P1.** Metabolism. **P2.** Needs as
above. **P3.** View. **P4 CHOOSE.** She is dispatched into Riverside to identify who is selling Crown
dispatch schedules. Her one act is `surveil`, chosen over `interview` deliberately: interview is fast and
**leaks**, its gain decaying sharply as `INTENDS(you, investigate)` spreads and people close up; surveil
is slow, its cost compounds through her own exposure, and its gain — firsthand root tokens — is
permanent and is the only thing that raises corroboration support. **P5 RESOLVE.** Stratum 3, contested.
The world emits facets: ordinary ones, and a rendering-side flare on a person at the ford. **P6
WITNESS.** She registers both classes. Haldorsen, working the same district at TS 0, registers only the
first — *at identical vantage*. **P7 RECKON.** Nothing evicts; her ledger is well under L = 200.

Two operatives, one street, one night, neither lying, and they now disagree about what happened. Doc 03
§2's first corollary is that *"two honest witnesses can agree on every fact and disagree on every
conclusion"* — here they do not even agree on the facts, because one of the two ledgers has no address
for half of them.

### 2.7 What propagates

Her firsthand root tokens propagate **into her own ledger and nowhere else on the rendering side**. The
ordinary half of her report propagates upward at full fidelity. **She is a channel that passes exactly
the information her institution already had a way to use.**

### 2.8 Diagnostic — **SPLIT: RICH as an investigator, BLOCKED as an advocate**

Both halves are the verdict; reporting only the first would be a brochure.

**RICH:** six investigative acts with genuinely different shapes of gain against cost (03 §6.1's R-check
holds — interview leaks, surveil compounds exposure, research yields the only *verified* rootprints,
reconstruct risks her own ledger), plus concealment with a real fork (extract fast and be found, extract
slow and be late) and an exposure/spend pairing that fires only when a rival actually spends.

**BLOCKED:** her stated goal — *minimise Thread collateral* — has **no act in the design that advances
it.** Not one. She can perceive it; she cannot petition it, argue it, requisition against it, or refuse
on it without being charged. Every closure is individually correct and the intersection is a wall. Her
one live route is **institutional and slow**: get a person with TS ≥ 30 into her order's decision path,
so that a claim she holds has somewhere to land. That is a multi-season objective, it is legible, and it
is genuinely produced by the substrate rather than authored — which is a credit to the design and does
not undo the block.

**This lands squarely on a known-open item, and I report rather than resolve it.** 16 §3.2: the
testimony half of the salience floor is held open, and *"the formula and the gloss diverge exactly where
the game is most active."* Torsvald is that divergence with a name on it.

### 2.9 Cells populated
`Individual` × `Epistemic` — the densest cell in the lane.
`Individual` × `Relational` (Knots, TS gate live on both endpoints).
`covert avowal` × `sworn degree` demonstrated as a working pair on one person alongside an avowed edge.
`Individual` × `Argument` — **demonstrated EMPTY for this character**, by three independent venue rules.

---

## 3. PROBES

### 3.1 Halvar Brandt — Officer, Lions' Table; Ehrenwall-succession candidate

**Coordinates.** Settlement/Realm; office = a chapter office inside the cluster, `binds
members-by-admission`; avowed; order-mark; Honor 0.35, Authority 0.25; TS **[GAP]**; goals *"counter
Altonian threat", "strengthen peninsular defenses"*; birthplace Halvardshelm.

**Option set.** `carry` a petition into a chapter sitting or up the Crown channel; be `dispatch`ed; vote
at a chapter sitting (decide rule: *any two of three who witnessed*); accumulate **witnessed deed**,
which is the only currency the conferral vector reads (β = 3.0) and the only evidence the venue admits;
`commit`; requisition his own subordinates.

**Diagnostic — THIN.** The succession he is a candidate for is conferred on a **deed** basis at a venue
that hears deed only, so his entire advancement play is one act repeated: *be seen soldiering in front
of sworn brothers.* His options differ cosmetically. And the accelerant is unavailable to him: 07 §4
says you rise by cutting the incumbent, and Ehrenwall's two bases are **merit/deed** (whose criterion
belongs to the chapters, not to him) and **military** (whose cut — the larder — is held by the Crown).
**Every cut against the incumbent is in someone else's hand**, so the successor's optimal play is to wait
for a death he cannot cause, which is not a strategy but a queue. Against Altonia he holds no seat at the
Crown council and no reach of his own; he can carry a petition and be dispatched. THIN, and one step from
SPECTATOR on the axis he was written for.

### 3.2 Vidar Haldorsen — Riskbreaker, TS 0 (`proposed`)

**Coordinates.** Identical to Torsvald's on A, B and C. Different on D: **TS 0**, Honor 0.60, Authority
0.20, certainty 5, resonant style Authority.

**Option set.** Torsvald's list **minus** `Thread-Read` and **minus** `form_knot`. Strictly smaller.

**Diagnostic — RICH**, and the reason is uncomfortable enough to state plainly. He runs the same
investigative surface at full effect, and the two acts he lacks produce claims that, inside his
institution, **nobody can use anyway.** Meanwhile every claim he deposits upward arrives **undegraded,
firsthand, at high confidence, from an Authority-styled officer** — so at P3 view assembly his account
outranks hers on all four salience factors at once. Canon calls him a *"pre-germ-theory surgeon —
perceptual limitation, not malice."* The design agrees and adds what canon does not: **the perceptually
limited operative is the institutionally more effective one**, because the ledger above him cannot hold
what the other one saw. P-03 running in the direction nobody praises it for.

### 3.3 Kolbrun Thale — Crown Spymaster (Schattendienst)

**Coordinates.** Realm; office (Minister — an establishment; `binds` its own members); avowed Crown;
Liberty 0.30, Utility 0.30; **Truth 3, the lowest in the inner circle**; rumoured Southern Einhir,
unconfirmed; TS **[GAP]**; `goals: null` in the registry.

**Option set — the fullest covert surface of anyone here.** `dispatch` her establishment; `interview`,
`surveil`, `research`, `reconstruct` at `visibility = concealed`; `plant`; `tell` with `as_asserted ≠
held` (Truth 3 makes this her default rather than her exception); **`withhold`** — 03 §7's second
application site, an office-holder applying concealment to *the channel their office is the normal
carrier for*, which for a spymaster is the entire job; `requisition` at low degree from contacts, or
simply **buy**, because a broker is a person with a price and not a member.

**Under the ruling her canon line reads better, not worse.** *"Only inner-circle member with any Niflhel
contacts"* becomes *the only one with contacts*, and the design already says what those are: persons
holding covert edges to small propositions, reached along ties. She needs no institution to work
through. She needs names.

**One apparent contradiction, which resolves.** Doc 14 §1.3 says an office-holder cannot act quietly —
but the rule is scoped to acts **by remit**, at `venue_factor ≥ 1.0`. Her non-remit acts take
`visibility = concealed` like anyone's. A spymaster is expressible: she issues in public and
investigates in private. **Flagged as resolved-on-inspection so a later reader does not re-file it.**

**The one genuinely open input.** Whether she holds **Knots** depends on her TS, which is `[GAP]` — and
her heritage rumour is precisely a rumour about a higher TS baseline. So: *the peninsula's rumour about
the Spymaster's ancestry is, mechanically, a rumour about whether her apparatus has bandwidth or only
latency.* Canon and mechanism meet exactly here and canon declines to say. **Diagnostic — RICH** if she
is TS ≥ 30; **THIN** if she is TS 0, in which case every channel she has is a witnessable ordinary tie
and the whole apparatus runs on exposure management alone.

### 3.4 Dalla Virke — syndicate broker

**Coordinates.** Settlement/Territory; no office; **Independent (Virke syndicate)**; Utility 0.30, Honor
0.30 — canon's gloss is *"honour among operators — your word is your network"*; goals: maintain the
network, protect personal trust relationships; arc: *personal loyalty to partners vs family directives;
third conflict with family triggers enforcement.*

**Under the design, with nothing added.** The Virke syndicate is a **faction**: proposition *(the Virke
word, binds, those who give it, all-time, ought)*, edges **private** rather than covert — discoverable by
witnessing a requisition honoured, or by being told. Her family is her **hearth**, and 01 §4 gives kin an
**obligation edge**: *kin may requisition each other's acts, at a cost in regard that scales with how
unreasonable the demand is.*

So her authored arc is two requisitions landing on one hour of one life — the tick allows exactly one
discretionary act per season — and canon's "third conflict triggers enforcement" needs no counter: three
refused kin requisitions cost regard three times, and enforcement fires when the family's own `will()` on
a `Force` act against her crosses 0.50. Nothing authored, and the counter deleted.

**Diagnostic — RICH.** She is also the strongest single piece of evidence that the strike costs the
design nothing: a broker with no institution behind her, who loses not one option.

### 3.5 Tomas Vorn — Goldenfurt broker, brother of Magistrate Hedda Vorn

**Coordinates.** Community/Settlement; no office; covert; caste and TS **[GAP]**; convictions *"the river
feeds who the Crown forgets" · "blood before the writ"*; canon: *"leveraged to a broker — not fully his
own man"*; his sister *"has quietly looked away."*

**Under the ruling, the leverage resolves cleanly to a person.** It is either a **debt** — 07 §4's
*purchased* basis, a transferable instrument whose cut is *outbid it, or devalue it with a dispensation
changing its terms* — or a covert commitment edge at d ≥ 3 to a two-person proposition. Either is a real
object; neither needs an institution.

**His play.** Night runs at `visibility = concealed`, which is `Force(seize, warrant none)` plus an
ordinary opening computed from changed terms; `exposure` rises per extraction and falls per `cover` act;
discovery is `1 − exp(−pressure × exposure/θ)` — so **a season he takes nothing is a season he cannot be
found however hard anyone looks**, and a season nobody investigates is safe however much he takes.

**And his sister is the mechanism canon says she is.** Hedda holds the settlement court's channel, so her
*"quietly looked away"* is `suppress` at a channel (03 §8) — *"the petitioner is not told; a record of
the suppression is deposited **in the holder's own ledger**, which makes it findable."* Canon calls her
brother *"her single point of failure."* The design produces exactly that and names the route: Old Brun
the night-ferryman is a **firsthand root**; one `interview` yields a `SAID` row; `reconstruct` resolves
the root to Tomas; a second reconstruct over Hedda's dispositions finds the suppression.

**Diagnostic — RICH.** Note what this probe demonstrates: **the entire Goldenfurt smuggling structure
survives the strike untouched**, because none of it ever needed the institution. It needed one creditor,
one ferryman, and one sister with a channel.

---

## 4. THE STRUCTURAL PROBE — a covert waterfront with no institution at all

### 4.1 Can several small, unnamed, overlapping covert factions be expressed without any being authored?

**Yes, and the design does not have to be stretched to do it**, because a faction is *identified by its
proposition* (07 §1.1) — not by a name, a charter, a head, a registry row or a size. *"There is no
found-a-faction operation… the faction begins at the first `commit`."*

Three of them along one Baralta dock street, none authored, all overlapping:

| | proposition | edges | avowal |
|---|---|---|---|
| f₁ | *(the ford's night tolls, belong-to, those who work it, all-time, **ought**)* | 4 — a broker, two dockhands, a ferryman | private |
| f₂ | *(this crew, does-not-speak-to, the Bailiff, all-time, **ought**)* | ~20, mostly d = 1 sympathy | covert |
| f₃ | *(the debt, is-owed-to, the creditor, before the thaw, **will**)* | 2, at d = 5 | covert |

One man holds an edge in all three, at three degrees with three avowals, and no object had to be created
for any of it. `presence` and `density` are recomputed sums; `capacity` is an existential over persons;
`requires(act, P)` is a predicate over person-sets. **Every consumer reads persons, so a faction with no
name reads identically to one with a name.**

What outsiders see is the interesting half. Nobody — *members included* — computes the true profile.
`estimate(f, n | o)` sums only the memberships in **that observer's ledger**, weighted by that observer's
confidence, and a rumour retold three times corroborates exactly once. So the Crown Spymaster's ledger
holds **one** referent for the waterfront, and the waterfront is three propositions with an overlapping
membership. Her estimate is not a poor measurement of one thing; it is a measurement of a thing that does
not exist.

### 4.2 Is a struck institution distinguishable, from the inside, from a live one?

**No — and that is the correct answer, not a shrug.** It is a result about the design's faction model
rather than about canon, so I state it as one.

Enumerate every consumer of the faction object and ask which could tell the difference. `presence` and
`density` are sums over edges · `capacity` is an existential over persons · `eligible` never consults the
faction · `requisition` reads **one** edge · `contest` resolves through a claimant's best-placed member ·
`standing` reads support sets · the argument system reads only the proposition. **Not one of them reads a
registry, a charter, a head, or a name.** The true profile has exactly one consumer (`resolve`, for
revolt density) and no `choose` may take it.

So for every `choose(person, view)` on that waterfront, *"Niflhel exists"* and *"Niflhel does not exist"*
are the **same world-state**. Striking the institution deletes nothing any person could have acted on.

**The one asymmetry, and it is the whole payoff.** The difference is visible **only from outside**,
because a name is a *referent*, and referents are what estimated profiles aggregate over, what stance
rows point at, and what an argument attacks. With the name struck:

- no observer can hold `HOLDS_STANCE(x, Niflhel)`, so no threat assessment can read the waterfront as one
  actor;
- no Inquisitor can attack the proposition, because there is no single proposition — there are three,
  each small and each individually boring;
- no `contest` can name it as a claimant, so it can never be *defeated*. It can only be **absent**, and
  07 §9 says everyone can see it was absent.

**So the strike removed exactly one capability: the ability of outsiders to treat a waterfront as one
thing.** And the design's own position is that this was never a fact about the world — it was compression
performed inside observers' ledgers. **Canon deleted a compression artefact, and the design says
compression artefacts live in observers, not in the world. The strike and the design agree.**

### 4.3 Does the Knot-slot bound still bite? — **It bites, and the suite states the wrong reason.**

The claim under test (07 §1.3): *"A covert requisition needs a channel that deposits no claim into a
judging set, and ordinary asking is witnessable. A Knot is not… a person holds at most `floor(Bonds/2)+1`
of them. A covert faction's capacity is therefore bounded by its members' Bonds, never by its presence,
which is why a national body cannot be run covertly."*

**Test 1 — do slots bound membership?** No. Bonds run 1..7, so slots are `floor(B/2)+1 ∈ {1,2,3,4}`. A
connected covert graph over *n* members needs *n−1* edges, each costing one slot at each end, so a
**chain** in which every interior member spends 2 of their ≥ 2 slots connects an arbitrarily large
network. **The slot cap does not cap size.** As stated, this is not the operative bound.

**Test 2 — what actually bounds it?** Three things, all already in the suite:

- **Diameter in seasons.** One act per person per season, so a covert requisition traverses one hop per
  tick. A Knot graph of diameter 5 delivers an order five seasons after it was given — after the standing
  date it was about. That is a hard bound on national covert action and it is real.
- **Strain.** `bandwidth(k) = max(0, 2 − floor(strain/3))`; +1 strain per counsel extraction; −1 per
  season **only if an `invest` act was performed**. 02 §4.2 runs it: one use per season is sustainable
  indefinitely, two is an overdraft, **three ruptures inside two seasons** — and a rupture hands a former
  partner the membership claim at regard −3, *"the same event as a discovery, arriving through the
  channel the secrecy depended on."*
- **The TS ≥ 30 gate on both endpoints**, which makes the covert graph's vertex set a minority of the
  peninsula, skewed Southern Einhir.

**Test 3 — and here is where the stated argument actually breaks.** *"Ordinary asking is witnessable"* is
false as an absolute. Doc 03 §7 gives **every** act a `visibility ∈ {open, discreet, concealed}`, and *"a
concealed act emits no facets to witnesses below a vantage-and-capability threshold."* A `requisition` is
an act. **So a concealed requisition is available to anyone at all** — TS 0, Bonds 1 — at the cost of a
reduced pool, more time, and exposure accrual. That is a second covert channel the Knot argument does not
account for, and it is precisely the channel Kolbrun Thale and Tomas Vorn must be using, since neither is
guaranteed a Knot.

**Verdict on the claim: the conclusion is true and the stated reason is wrong.** A national body cannot
be run covertly — but the binding constraint is the **exposure/spend pairing**, not Bonds:
`exposure += extraction_weight` per extraction, and `P(discover | I) = 1 − exp(−pressure × exposure/θ)`.
National-scale extraction means a large `extraction_weight` against every investigator's pressure at once,
and `cover` buys it back only by spending the tempo the network existed to gain. That is a real ceiling
with the right shape, and it holds for TS 0 conspirators too.

**Why the misattribution matters, and it is not pedantry.** A later reader who "fixes" the slot count
changes nothing. A reader who relaxes TS ≥ 30, or softens strain, or drops the `invest` requirement,
deletes the bound the suite *thinks* it has — while the bound it actually has sits in a different
document under a different name, unprotected by the sentence that claims to protect it. **Reported as a
defect in the stated derivation, not patched.**

---

## 5. Does covert play hold up? — Yes, with four named thin spots

**It holds up.** The covert surface is genuinely built: `avowal` on the edge rather than a "known %" on
the secret; exposure derived from what knowers hold rather than stored; discovery proportional to a
rival's actual spend with both failure poles cleared (patience is safe, and the world does not audit you
for free); concealment with a real R-fork; cover identities as ordinary cover-tellings; and a discovery
cost computed from the observers rather than from the secret, so one identical exposure ruins a Free
Master and costs an Oastad fisherman nothing. A design built on witnessing does work when nobody
witnesses, because the *absence* of a claim is a first-class state rather than a masked truth.

**The four thin spots, in descending order of what they cost the game.**

1. **Covert play has no venue, therefore no clock, and is closed out of two modes entirely.** Every venue
   in the design is a public room with `enter`/`speak` predicates, a record custody and a standing date,
   and 01 §5.3 says the standing date is the whole of *why* politics is timed — *"two sides know when the
   argument ends."* A covert faction has none. Against the mode axis:
   **Material · Epistemic · Coercive · Relational — open.**
   **Political-up — open at a price:** a d ≥ 2 member may `carry` the faction's proposition, avowing the
   *proposition* while leaving the *edge* covert and raising every observer's estimate. A real fork.
   **Argument — closed to the faction, open to a member in propria persona.**
   **Political-down and Institutional — hard-closed.** A covert faction cannot `issue`, `confer`,
   `revoke`, `convene` or `charter`, because all five are remit acts and *"a covert edge and a remit are
   close to incompatible."* This may be exactly right, and it is still the largest empty region either of
   my two cells contains: **a covert faction can act, and can never legislate, adjudicate, or set a
   deadline.**
2. **`admitting_share` is named and never supplied.** 03 §9 makes registration of a rendering-side facet
   `g(TS − floor) × admitting_share(witness)`, where `admitting_share` sums *"Convictions whose construal
   sets contain a rendering-side reading."* **No construal-set table exists for any Conviction anywhere in
   the suite.** So the formula carrying P-03, P-08 and P-13 cannot be evaluated for a single canon
   character — Torsvald's Utility 0.40 / Honor 0.20 yields no answer. A missing table, not a missing
   mechanism; report it as the table.
3. **The requisition `burden` term cannot represent a harm only the member perceives** (§2.5). It reads
   the member's need, the member's container's stake, and the member's marks. The setting's central
   asymmetry produces a fourth kind of harm, and the formula charges a degree of commitment for acting on
   it.
4. **The armed-force channel table has two columns and canon's principal army is in neither** (§1.8) —
   alignment-routed, third-party-paid. Both arms of doc 12 §9.1's levy/hire R-check assume the payer and
   the orderer are one person.

**One near-miss that resolves on inspection**, recorded so it is not re-filed: an office-holder *can* act
covertly, because 14 §1.3's publicity rule is scoped to acts **by remit**. Thale issues in public and
surveils in private.

---

## 6. CELLS POPULATED

| rung (A) | mode (E) | by whom | note |
|---|---|---|---|
| Realm-scope cluster root | **Institutional** | Ehrenwall | confer/revoke/convene on a deed vector; `admissible_source` gating a whole caste *in* by accident |
| Realm-scope cluster root | **Coercive** | Ehrenwall | `Hold` over sworn men rather than a levy; `sever = 0.50` on a caste-open body |
| Realm-scope cluster root | **Political-up** | Ehrenwall | an unfiltered channel to the King, held by the person and not by the post |
| Realm-scope cluster root | **Relational** | Ehrenwall | requisition, refusal, and the contagion of a witnessed refusal |
| Individual (mobile) | **Epistemic** | Torsvald, Haldorsen, Thale | six acts, four cost shapes; the lane's densest cell by a distance |
| Individual | **Relational** | Torsvald | Knots with the TS ≥ 30 gate live on both endpoints |
| Settlement / Community | **Material** | Vorn, Virke | smuggling as a computed opening; a debt as a purchased basis |
| Settlement / Community | **Coercive** | Vorn | `Force(seize, warrant none)` at concealed visibility |
| Hearth | **Relational** | Virke | the kin obligation edge colliding with a faction edge over one act |
| Settlement | **Epistemic** | Hedda Vorn, as the mechanism | `suppress` at a channel, self-recording, therefore findable |
| Realm | **Political-down** | Thale | `withhold` — concealment applied to the channel an office normally carries |
| covert × unnamed × overlapping | **all of the above** | the Riverside three | three factions, no author, no name, no head, no registry row |

## 7. CELLS I FOUND EMPTY

1. **`covert alignment` × `Political-down`** — hard-closed. A covert faction cannot `issue`; no remit is
   compatible with a covert edge.
2. **`covert alignment` × `Institutional`** — hard-closed. No `confer`, `revoke`, `convene`, `charter`.
3. **`covert alignment` × `Argument`** — closed to the faction. No venue admits a claimant with no
   standing date, no record custody, and no person willing to `enter` and `speak` as its representative.
   Reachable individually only by avowing, which is irreversible.
4. **`Realm-scope cluster root` × `Political-down`** — empty for Ehrenwall specifically. Her remit binds
   members-by-admission, so **no decision she makes reaches a person who did not join her order.** The
   commander of the realm's standing army has no downward channel to a commoner except a man on a horse.
5. **`Individual` × `Argument`, for a claim whose subject is a configuration** — empty by three
   independent mechanisms (deposit-side degradation, corroboration on distinct firsthand roots, and
   `admissible_source`). This is the testimony half of the salience floor showing up as a person.
6. **`Realm` × `Relational` for a TS 0 principal** — Ehrenwall, Almud and Haldorsen have **zero** Knot
   slots. The design's own *"only channel by which a person holding no post receives news"* is unavailable
   to roughly half the peninsula, deliberately (02 §11.2) — which means the informal channel is closed at
   exactly the rungs where the formal channel is most heavily filtered.
7. **The third armed-force column** — alignment-routed, third-party-paid. Empty not because nobody stands
   in it, but because doc 12 §2.1's table has two columns and canon's principal army is in neither.
8. **The `burden` slot for a harm only the member can perceive** — empty, and the formula defaults it to
   zero, which converts a principled refusal into a cheap one.

---

## 8. Discipline note

Two things this lane was told to report and not resolve, and did not resolve: **the conferral dilemma**
(narrowed — one of the two pieces of evidence the suite's audit cites for the office-rooted answer does
not bear weight, because the Grandmaster's warrant reaches her from the chapters under *either* answer;
the dilemma itself is untouched) and **the Grandmaster's name** (Lisbeth used, Sigrid noted, the suite's
propagation of the timeline variant flagged). One thing it was told to treat as settled, and did:
**Niflhel is not a faction.** No character was rescued: Brandt is THIN and one step from SPECTATOR,
Torsvald is BLOCKED on the thing that defines her, and both stand as written.
