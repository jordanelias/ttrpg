# Lane 6 — Edges and Ground

## Status: FILED (2026-08-30) — coverage-instrument output. Nothing here ratifies on merge.
## Authority: the merged suite (`proposals/2026-08-29-valoria-from-scratch/`) on mechanism; canon on people.
## Binding: `00_PLAN.md` §4 (season shape), §5 (discipline); `01_ROSTER_AND_FINDINGS.md` FINDING 1.
## Jordan 2026-08-30: Niflhel is not a faction. The Guilds are a loose collective of economic factions.

**What this lane owns.** The two places a political design is most likely to be thin: the **edges**
(off-board, and the far end of Thread Sensitivity) and the **ground** (people with no leverage). Two
seasons at full depth — Doux Alexios Laskaris, and an invented control — and eleven probes.

**One naming note, discharged up front.** FINDING 1 binds: canon's person is the person, and where a
lane needs a commoner it invents a name rather than borrowing one. The control is **Alvid Bekk**, who
appears nowhere in `references/npc_registry.yaml`, `references/proper_noun_registry.yaml`, or any live
surface. Her household names (Nils, Rannveig, Gerd) are likewise new.

**One address contradiction, reported and not resolved.** The Goldenfurt slice
(`systems/settlements/goldenfurt_slice/`) places S-006 Goldenfurt in **Kronmark province, Valorsmark /
Crown duchy, Provincial Authority = the Crown**. The merged suite's worked traces place Goldenfurt in
**Grauwald / Varfell** throughout (01 §7, 02 §9, 05 §4, 05 §10). These are different towns wearing one
name. I use canon's address for canon's people and the suite's mechanisms for everything else, and I
flag every place the difference changes an answer. It changes one: who Alvid's praefect answers to.

---

# I · FULL SEASON — Doux Alexios Laskaris

## 1. Coordinates

| axis | value |
|---|---|
| **A · rung** | **Off-board.** Doux (provincial governor) at a Province rung of the *Altonian* containment tree. His path to root terminates in the Altonian Emperor, not in Valoria. |
| **B · office** | binds persons by presence — **inside Altonia**. Also a conferrer: he holds the root of a small office cluster (his own establishment, his court's posts). |
| **C · alignment** | Altonia, avowed. Degree is the question: **constitutive to the House of Laskaris, member at most to the imperial proposition** — which is what "sandbag imperial directives" means in the substrate's vocabulary. |
| **D · marks** | `heritage = Altonian` (open) · `house = Laskaris, main` (attested) · `office = Doux` (attested) · caste-advantaged everywhere he stands · **`sensitivity` is a canon [GAP]** (`npc_registry.yaml:270`, `ts: null`) |
| **E · modes reached** | Material · Political-down · Institutional · Relational · Argument. **Not** Political-up, **not** Coercive, in either case *toward Valoria*. |

Canon goals (`npc_registry.yaml:281`): protect Elske's safety · maintain province stability ·
**sandbag imperial directives**. Convictions: Virtue 0.50 primary, Authority 0.20.

## 2. Opening state — the six fields, and what is conspicuously absent

Address, marks, capability and stance are ordinary for a great magnate. Two fields carry the season.

**Ties.** He is married to Princess Elske Almqvist, who is `ts: 0` (`npc_registry.yaml:399`). Doc 02
§4.2 gates `form_knot` on **TS ≥ 30 on both sides**. So *the marriage that the entire Altonian–Valorian
relationship rests on cannot be a Knot.* The deepest channel in the design is unavailable to the
peninsula's most important couple, and what they have instead is `tie(a,b) = (familiarity,
last_contact, channel_class)` — a rolled, latent, distortable channel like any other. Nothing in the
suite notices this; it falls out of one threshold meeting one canon stat.

**Memory.** His ledger's Valorian rows come from three sources and no others: Elske, Prince Torben, and
returning Altonian merchant-captains (the exact channel 06 §7's own worked trace uses to deliver him a
treaty breach). He holds **no** claims deposited by a crier, a parish, a guild notice, or an
institutional relay inside Valoria, because 06 §2's relay clause requires *his institution's presence at
the node* and he has none.

**Conspicuously absent:** any standing at any Valorian container. Doc 05 §3.1's `carry` precondition is
"c holds STANDING at respondent_container(P)". He holds none, anywhere, at any rung, in Valoria.

## 3. Computed needs

- **SUBSISTENCE** — reads the world; his province's larders are sound. **0.**
- **STANDING** — reads the world for who his peers are (the Emperor's other governors) and his *own
  ledger* for what they have shown him. He is a Doux who is visibly soft on a frontier the capital
  wants pressed. Peers with at least one expressed-regard claim: eleven. `r` ≈ 0.3, `care = max(Honor,
  Identity weight)/5` — Virtue at 0.50 primary maps to weight 5 → `care` 1.0. **urgency = round(5 × 0.7
  × 1.0) = 3.**
- **COMMITMENT** — reads the *view*. The imperial proposition (press the frontier) is one he holds at
  member degree with a **negative** stance row. Doc 07 §3.4's seed rule means his specific row has
  drifted off the Authority Conviction that seeded it. Unmet, and he does not want it met. **0 as a
  driver, and a standing liability at every requisition.**
- **EXPOSURE** — reads the view. One live dispensation in scope: an imperial directive on the frontier
  posture. `urgency = |Δ in the value of his own reachable options|`. Complying costs him Elske's
  safety and the province's stability at once. **urgency 3.**

His two live needs are **standing among imperial peers** and **exposure to an imperial directive**, and
they point in opposite directions. That is the whole season, computed, with nothing authored.

## 4. The view, and the claim that does not surface

K = 12 by salience (09 §1.2 P3). Top rows: the directive's text; the merchant-captains' report of a
new Valorian duty; Elske's own account of her brother's court; Torben's household expenses; three
imperial peers' letters; the harvest.

**The claim that does not surface:** a captain told him, two seasons back and at confidence 0.4, that a
Varfell duke is agitating to expel Church and Altonian residue from his duchy (07 §10.1's Vaynard
proposition). Salience = recency × confidence × **relevance to the pending decision** × stance weight.
Its relevance to *the frontier-posture directive* is low; its stance weight is low because he holds no
row for a Varfell internal question. It ranks about nineteenth and never enters his choose. Vaynard's
programme is the single largest threat to Altonian interests in the peninsula and Laskaris will not
think of it this season — not because he was deceived, but because his ledger ranked it correctly
against the question he was actually asked.

## 5. The option set — the load-bearing section

| act | legal because | reaches Valoria? |
|---|---|---|
| **Publish the directive at full fidelity, with enforcer_presence** | 06 §2, §8 — he holds the relay | no |
| **Publish it thin** — crier only, no riders, no relay reset | 06 §2/§8: reach is *a count of persons the issuer employs*; spending none is not an act | no |
| **Issue a Dispensation scoped to his own court**, targeting Torben | 06 §7's worked trace, verbatim | **yes — through one body** |
| **Breach or honour the marriage treaty's trade-lane terms** | 06 §7: a treaty is a Dispensation with two issuers and no enforcement field | **yes — through a price** |
| **Confer / revoke offices in his establishment** | 14 §2.3 `admit()` at the conferring office | no |
| **Argue at an Altonian venue** | 14 §5's three gates, in his own tree | no |
| **`tell` Elske; `tell` a captain** | 01 §3.3 — always available | yes, weakly |
| **Address Almud directly** | 05 §6.4: `gap = rank(respondent) − rank(petitioner)`; ducal house = 6 both sides, gap 0, direct address permitted | **yes, if he is present** |
| ~~`carry` a petition into a Valorian container~~ | **no standing at any of them** | — |
| ~~publish into Valoria~~ | **every channel in 06 §2 requires presence he lacks** | — |
| ~~`contest` a Valorian prize~~ | 04 §8's capacity sums `act_reach` over persons *at the container* | — |
| ~~coerce~~ | 12 §7 names it itself: *"Altonia's leverage over Prince Torben is a patronage and Knot attack on one person. There is no military expression of it at all."* | — |

**Sandbagging is not an act.** It is the *absence* of a publication spend. 06 §8's Territory Reach Cap
makes each publication-with-enforcement consume one of a finite set of dispatchable persons; declining
to spend them deposits nothing in anyone's ledger, produces no event, and is therefore invisible to
`witness`. An imperial auditor cannot investigate what did not happen — he can only count what did, and
counting absences is not among 03's investigation acts. **The design gives Laskaris a perfect,
undetectable form of disobedience, and gives his sovereign no instrument against it.** That is either
the best thing in this season or a hole, and I report it rather than deciding.

## 6. The choice, through the seven phases

**P0 CALENDAR.** The trade-lane clause carries a standing date at the season's close. Option
availability recomputes; nothing new becomes legal.
**P1 SETTLE.** Larders, production, travel. A captain's ship completes a leg.
**P2 NEEDS.** Standing 3 · Exposure 3, opposed.
**P3 VIEW.** K = 12 as above.
**P4 CHOOSE.** He publishes the directive to his two coastal settlements at full fidelity and to the
five inland nodes not at all — spending two riders of the seven the office employs. The frontier is
posted; the interior is not. To the capital's ledger, the directive is published.
**P5 RESOLVE.** Two publication events. No Valorian object is touched by any act of his this season.
**P6 WITNESS.** Altonian persons deposit. **Zero Valorian ledgers receive a row naming Laskaris.**
**P7 RECKON.** Confidence decays. His unspent riders are not state; there is nothing to carry forward.

## 7. What propagates

Down-stroke, entirely inside Altonia, at two of seven nodes. Toward Valoria: **nothing this season.**
The Laskaris claim on the Valorian succession (04 §3.2) remains banked, dormant, costless, and invisible
to `resolve` — waiting on a vacancy predicate he does not control and cannot hasten from where he
stands.

## 8. Diagnostic — **RICH at home, and structurally mute across the water**

**Verdict: RICH.** Five modes live, several forks with materially different consequences, and the
R-check finds no dominance: publishing thin buys a season and accrues an exposure that rises with
repetition, while publishing full costs Elske's safety immediately — a genuine crossover, not a
foregone conclusion.

**The boundary is the finding, and it is sharp.** Of his eleven live acts, **zero have a Valorian
container in their scope.** He reaches the peninsula by exactly three routes, and each is worth naming
because together they are the design's real answer to its own open question:

1. **Through a body standing in his hall.** Elske and Torben are Valorian persons at a Valorian-relevant
   address that happens to be inside his scope. A dispensation over his own court binds them. This is
   what 06 §7 already demonstrates and it is the only *direct* channel.
2. **Through a supply term.** Closing a lane is a prohibition on *his own* merchants; the flow drops;
   13 §4's `supply(good, s)` loses an `import_flow` addend at a Valorian port; the price runs; every
   hearth in scope recomputes `opening_set`. **He moves a Valorian fisher's option list without a single
   Valorian person having heard of him.**
3. **Through a proposition.** 05 §5.1: *"A proposition is a claim, and claims travel by telling
   independently of any member travelling."* Altonian accommodation is already a live cleavage inside
   the Crown (`faction_canon_v30.md:548`). Altonia-as-faction can therefore hold Valorian members and
   act through their `act_reach`, with nobody crossing the water.

## 9. REPORTED, NOT RESOLVED — the actorless-pressure question

`00_INDEX.md` §3.3 and `15_adjudications.md` §D hold this open: *may an off-board polity exert pressure
without a person to carry it?* Laskaris narrows it and does not close it.

**What the season shows is already answered.** Routes 2 and 3 above are real, computed, and require no
Valorian actor. A price is not an act and a proposition is not a member. So the naive form of the
question — *"can Altonia matter without an agent in Valoria?"* — is **yes**, and the suite already
supplies the mechanism twice over without having noticed that it did.

**What remains genuinely open is narrower and harder.** All three routes require *some* modelled
Altonian person: a merchant to stop sailing, a captain to carry a telling, a Doux to sign. The
unanswerable case is a change in the off-board polity's **interior** that no modelled person produced —
an imperial succession, a defeat in the east, a new Emperor's temper. Two branches, and they are
different games:

- **Simulate Altonia's interior.** Then "off-board" is a fiction: it is on-board at low fidelity, it
  costs a cohort budget, and the question dissolves.
- **Author Altonia's state and let it deposit claims.** Then a change with no `choose` behind it enters
  ledgers, which is exactly `01_substrate.md` §6's banned object — *"any broadcast that deposits the
  same value into many persons"* — arriving through a border instead of a back door.

The choice is between paying for a second peninsula and permitting one authored actor. **Not this
lane's call.**

---

# II · FULL SEASON — the control: Alvid Bekk

> **This is the season every other season in the exercise is measured against.** No office, no
> alignment, no notable marks, no Knot, ordinary capability, an ordinary larder. No lucky break, no
> patron, no dramatic event. I have not rescued her and I have not written a plot.

## 1. Coordinates

| axis | value |
|---|---|
| **A · rung** | Individual / **Hearth** / Community. Her address: *Alvid / Hearth of Bekk / the ford-side parish congregation / Goldenfurt / Kronmark / Valorsmark.* |
| **B · office** | **none.** No post, no seat, no right of audience, no committee. |
| **C · alignment** | **none, at any degree, to anything.** Not sympathy. The commit map holds no row for her. |
| **D · marks** | `heritage = Central Einhir` (open, 0.9) · `church = communicant` (attested) · `house` none · `grade` none · `office` none · `sensitivity = none`, TS 4. **Caste-advantaged only in the negative sense: she is not excluded because she is not read.** |
| **E · modes reached** | see §5 — 2 of 8 modes live at any strength |

**Which community?** This is not a trivial question and the answer is a finding. Doc 04 §7's community
roster has seven parameterisations: craft guild, Einhir hamlet, Crown-Latinate quarter, parish
congregation, Restoration cell, Löwenritter chapter, Niflhel crew. Alvid is in none of six — she has no
guild grade, no stigmatised heritage, no wall-side privilege, no alignment, no oath. **The only rule in
the roster that admits her is the parish's, "every hearth in a district, by presence."** So for a person
with nothing, the Church is structurally the only community they have, and the parish priest is by
default their judging set, their gate, and their intercessor. Curate Wessel's probe (§III) is therefore
not adjacent to Alvid's season; it is inside it.

⚠ **And that same rule collides with single-parent containment.** A Kettlemaker's hearth is contained in
Kettlemakers' Row *and* falls inside a parish district by presence. Doc 01 §1.1 forbids two parents;
doc 01 §4 says "a parish is a community"; doc 04 §7 makes its membership rule presence-based over a
district. Those three cannot all hold. **Reported, not resolved.**

## 2. Opening state, and what is conspicuously not there

**Hearth of Bekk.** Alvid 34 (adult 1.0) · Nils her husband, a hired carter at the ford landing (1.0) ·
Rannveig, his mother (elder 0.7) · three children, 11, 7 and 3 (0.5 × 3 = 1.5). **`mouths` = 4.2.**

**Holdings:** one — a rented garden strip on the outfield with a pig-right on the common,
`base(H) ≈ 2.6` mouth-seasons.

**Capability:** Str 3 End 4 Agi 3 / Foc 3 Acu 4 Wil 4 / Att 3 Cha 2 Bonds 3. Practices: `Cloth-work 2`
(provenance: Hearth of Bekk, her mother; idiom: none recorded) · `Marketing 1`. Coherence 8, Whole.
Convictions: Community w4 (primary), Order w3, Faith w3, Precedent w2. Credulity 3, obstinacy 2.

**Read that capability line again, because it is the mechanical definition of "ordinary."** Doc 02 §2.3:
a practice at **rank ≥ 3** adds verbs to the actor's option list; at rank ≥ 5 it adds verbs unreachable
below that. **Alvid holds nothing at rank 3.** She therefore has *no reach terms at all* — her option
list is the bare universal list with nothing added by anything she can do well. Ordinary capability is
not a smaller pool. It is an empty verb set.

**Knots:** slots = `floor(Bonds/2)+1 = 2`. Both empty, and **permanently unfillable**: `form_knot`
requires TS ≥ 30 on both sides and she is TS 4. Doc 02 §11.2 states the consequence and asks that it not
be "fixed": *"the Knot is how a person with no post gets news… half the peninsula cannot form one."*
Alvid is that half. The design's own named channel for the unposted is closed to her by a number she was
born with.

**Conspicuously not there:** a house mark, a grade, an alignment row, a banked claim, an obligation edge
to anyone who holds anything, a sponsor, and — the one that decides her season — **any mark toward
which any member of her community holds a strong stance.**

## 3. Computed needs — with the arithmetic, and the three that come back zero

`yield(H, season) = base × season_factor × (3 + d10)/8.5`. `d10 = 6` → `2.6 × 1.0 × 1.059 = 2.75`.
Levies in scope: the Crown grain levy plus the parish tithe ≈ **0.5**.
`draw = 2.75 − 0.5 = 2.25`. `stores += draw − mouths = 2.25 − 4.2 = −1.95`; opening 3.0 → **1.05**.
`margin = 1.05 / 4.2 = 0.25` → **Hungry** (04 §1.2's band 0–0.5).

`need(subsistence) = clamp(0,1,(2.0 − 0.25)/2.0) + max(0, −0.25)` = **0.875.**

⚠ **Two owners, one need.** Doc 04 §1.2 (restated verbatim by 13 §1) gives `need(subsistence)` on a
0–1+ scale from `margin`. Doc 02 §6 gives it on a **0–5** scale from `larder_days`. Different formulas,
different ranges, no reconciliation anywhere, and doc 05 §1.1's `shortfall = urgency − reach` compares
it against a `reach` in [0,1]. Which one the option ranking reads is undetermined, and the answer
changes whether subsistence dominates every other need or is merely comparable to them. Reported.

⚠ **The larger arithmetic problem: Nils's wages are not in the formula.** In the fiction, carting at the
ford landing feeds roughly a third of this hearth. `draw(h) = Σ_{H ∈ holdings} yield(H) − Σ levy` has no
term for it, and 13 §9 explicitly refuses a currency (*"the stake was never how much money, it was whose
mouths get fed"*). Doc 12 §6.4 asserts wage-fed hearths exist — *"a hired man's hearth produces nothing;
his needs are computed from a larder that the coin was filling"* — and no document anywhere supplies the
producer. **There is no `sell labour`, no wage as a yield term, no unit to denominate one.** With the
missing third restored, `margin ≈ 0.62` and the hearth is **Thin**, not Hungry. The design cannot
represent the difference, and the difference is a band.

The other three need terms:

- **STANDING.** `peers` = her siblings-in-container: about 140 hearths in the parish district.
  `regard(peer)` reads **her own claims about how each peer has shown regard** — she holds such claims
  about nine people. `r` ≈ 0.55 among those nine. `care = max(stance[Honor].weight,
  stance[Identity].weight)/5 = 1/5 = 0.2`. **urgency = round(5 × 0.45 × 0.2) = 0.**
- **COMMITMENT.** `for each faction f at commit degree d` — **the loop body never executes.** She holds
  no faction. **0, structurally, forever, unless she commits.**
- **EXPOSURE.** `|Δ in the value of her own reachable options under the asserted terms|`. Her reachable
  options number eight (§5) and almost none has a value any term can move: she owns no boat, crosses no
  boundary, holds no grade, sits no examination, carries no goods. A bread `PriceTerm` and the grain
  `LevyTerm` move it. **urgency ≈ 0.4.**

> **Three of the design's four need terms return zero or near-zero for an ordinary person, and the
> entire motive engine reduces to one number: her larder.** That is the floor problem, stated
> arithmetically. STANDING is gated on holding Honor or Identity at weight ≥ about 2 — a Conviction
> profile the setting seeds into cadets, guildsmen and nobles and not into her. COMMITMENT is gated on
> already being in a faction. EXPOSURE is gated on having options worth changing. The design is at its
> most generous to people who already have something, and it says so in its own formulas.

## 4. The view, and the claim that does not surface

K = 12 (09 §1.2). Her ledger holds about sixty rows. What surfaces: the granary opens at the reckoning;
bread is dearer; a named reeve collected the levy in the square; her sister Gerd in Oastad has a spare
bed; the carting work is short; the curate preached on the tithe; the ford toll rose; five neighbours'
faces.

**What does not surface.** Twelve days ago, coming back late along the bank, she saw two men land sacks
below the ford. It is in her ledger: `(a landing below the ford, at night, this season, firsthand, 0.9)`
— **a firsthand root**, and under 01 §3 independence is measured on firsthand roots. It is the only
independent corroborator in Goldenfurt for a claim about Tomas Vorn's traffic, and three parties would
pay for it: Bailiff Ems, who wants leverage; Curate Wessel, who wants a denunciation; Magistrate Hedda
Vorn, who wants it buried.

Salience = recency (0.6) × confidence (0.9) × **relevance to the pending decision** (feeding five
mouths: about 0.05) × **stance weight** (she holds no row on smuggling: 0). It ranks about fortieth.

> **The poorest person in the town holds the most valuable claim in it, and the design guarantees she
> will never surface it — because salience is weighted by relevance to *her* decision, and her decision
> is always about food.** This is not a bug. It is 01 §3.1 working exactly as specified, and it is the
> single most important structural fact about the ground: *the bottom of the ladder is where the roots
> are, and root-holding is not an act.*

## 5. The option set — every act available, and why

Against the plan's eight modes. This is the load-bearing table and the gaps are in it.

| mode | available to Alvid | closed, and by what |
|---|---|---|
| **Material** | hoard (a null act — she performs no release; she has no surplus) · migrate (04 §9) | **forestall** needs stores to buy a yield outright (13 §4) · **smuggle / carry a route** needs presence at both ends or a Knot (13 §4) · **settle_in_full** needs stores (13 §8) · **sell her labour** — no verb exists · **build** anything — no verb exists |
| **Epistemic** | `tell` · `conceal` / lie · `examine` what is in front of her | **research** needs an archive and literacy · **Thread-Read** needs Thread Pool ≥ 1, she is TS 4 · **reconstruct / surveil** at any useful scale needs acts she cannot spare |
| **Political-up** | `back` a petition (free inside her own judging set, 05 §2.2) · **supplication** at gap 3 — carried, *and* through an intercessor whose own gap is ≤ 2 · `carry` into the parish only | **remonstrance** requires standing at an institution with a registered right of remonstrance (05 §6.1) — she has standing at none · `carry` at every rung above her community |
| **Political-down** | comply · evade (06 §3's quiet evasion, producing arrears) | issue · publish · refract — all require office |
| **Argument** | plead at the parish, over the parish's own stake | every venue above it: 14 §5's gates are standing-gated and she has standing at none |
| **Coercive** | a knife (04 §2.1's sixth exit), unbounded downside | levy · muster · arrest · suppress — all office |
| **Relational** | `requisition` kin (04 §1.4) · **foster out** a child (04 §2.2) · marry a child, later | **form a Knot — permanently closed, TS 4** · admit / exclude — she sits on no committee |
| **Institutional** | **nothing. Zero of five.** | confer · revoke · convene · appoint · charter — office begins at the Settlement rung (01 §4) |

**Eight live acts.** Count what that means against the design's own claim (01 §2): *"A person with no
office can still act. Every act is offered to every person."* That is true and it is hollow. Every act
is offered; `requires(act) ⊆ capability ∪ marks ∪ ties` filters, and she has an empty verb set, three
marks of which two are absences, and no Knot. **Her rank is 1** by 05 §6.4's default clause — no office,
no grade, no Church standing above communicant.

**Her only legal route to a decision-maker runs through the priest.** `gap = rank(magistrate 4) −
rank(Alvid 1) = 3` → supplication only, must be carried, **and requires an intercessor whose own gap to
the respondent is ≤ 2**. Sister Aldith is a lay almoner: rank 1, and cannot intercede. Old Brun is a
ferryman: rank 1. The parish priest is rank 3, gap 1. **Curate Wessel is the only person in Goldenfurt
who can legally carry Alvid Bekk's voice to the magistrate — and Wessel's other job is informing the
Himmelenger Inquisitor.** Nobody wrote that. It is a rank table meeting a canon dossier.

## 6. The choice and its resolution, through the seven phases

**P0 CALENDAR.** The parish tithe reckoning and the settlement granary opening fire onto the docket.
Option availability recomputes; nothing new becomes legal for her.
**P1 SETTLE.** The larder settles: Hungry. Her cloth-work and Nils's carting are metabolism, not acts —
09 §1.1 puts subsistence and craft in P1, so **her working day is not her turn**.
**P2 NEEDS.** Subsistence 0.875 · standing 0 · commitment 0 · exposure 0.4.
**P3 VIEW.** As §4. The landing does not surface.
**P4 CHOOSE.** One discretionary commitment. She requisitions her sister Gerd, in Oastad, to foster the
seven-year-old for a year.
`claim_weight(Alvid→Gerd) = base(sibling, separate hearths) 1.5 × cohab 1.0 × (1 + max(0, +2)/5) = 2.1`.
`strain = cost_to_called/capacity + 2·conflict = 0.35 + 0 = 0.35`.
`comply_pressure = 2.1 − 0.35 = 1.75`, strongly positive. Gerd chooses, from her own view, to comply.
Price on asking: `−0.5 × max(0, 0.35 − 2.1) = 0` — **the ask costs her nothing.**
**P5 RESOLVE.** The boy's address changes. `mouths` 4.2 → 3.7. Two obligation edges at 1.5, **both
ways**.
**P6 WITNESS.** `publicity = venue_factor × √(witnesses) × mark_salience`. A private dwelling is 0.2;
three witnesses; `mark_salience = 1 + 0.2 × (marks any community member holds a strong stance toward)` =
**1 + 0.2 × 0 = 1.0**. `publicity = 0.2 × 1.73 × 1.0 = 0.35` → below 0.5: *"the hearth, and whoever
holds a Knot."* She holds none.

> **The most consequential act of her life is witnessed by three people and reaches nobody.** Doc 04
> §4.1 presents `mark_salience` as a caste effect — Maret Uln's transgression travels twice as far as an
> unmarked neighbour's. Read from the other end it says: **being ordinary is being inaudible.** The
> unmarked person's charity, grievance and injury all propagate at the floor value, in both directions,
> forever.

**P7 RECKON.** Confidence decays; the ledger is nowhere near L = 200. She persists as an individuated
person only because Gerd's ledger and five neighbours' ledgers name her (01 §2, 02 §7: *a person
persists exactly as long as somebody remembers them*). Had she done nothing this season and had those
rows aged out, she would **de-individuate back into a cohort.** Note the shape of that rule from below:
**the cheapest way for an ordinary person to stay a person is to do something people talk about**, and
what people talk about is transgression. The reference-count bound is correct and it quietly selects for
the criminal over the quiet.

## 7. What propagates

Neither stroke. −0.5 mouths here, +0.5 there; two edges created; one child's judging set changed. No
container's terms move, no norm recomputes differently, no petition exists, no faction gains a degree.
**Total propagation of the control's season: one hearth-to-hearth transfer, one rung wide, zero rungs
up.**

## 8. Diagnostic — **THIN**

**Verdict: THIN**, and the R-check names the dominance explicitly.

**One option dominates.** Of eight live acts, exactly one changes the number her season is actually
about (`mouths`): **foster out**. And 04 §2.2's table prices it at **nothing** — the larder column reads
"−1 mouth here, +1 there," the pointer column reads "none," and the edge column records that it *creates
1.5 edges in both directions*, which is a net gain. Gain-shape: immediate, material, and **repeatable
while children remain**. Cost-shape: **unpriced**. That is the banned shape from the wrong side — an
undominated gain against an absent cost — and it is bounded only by how many kin will take a child.
Every other arm in her set is slower (petition), worse (migrate, which resets a larder and destroys a
standing she does not have), catastrophic (the knife), or free-and-inert (back, tell, hoard).

**What is genuinely live and worth saying.** She is not a SPECTATOR. `back` and `tell` feed 05 §9's
`value(attempt) = P(grant)·U + (1 − P(grant))·G` — the grievance-capital term that makes a losing
petition campaign build the thing that wins without petitions. Her stance rows are real inputs to
`norm()`, `capacity()` and `carriage_mass()`. She is *aggregable*. But aggregable is what the design
does with her, not what she does.

**The honest summary of the floor.** The design gives an ordinary person acts, and gives her almost
nothing to decide. Three of four needs are structurally zero; her capability adds no verbs; her marks
make her inaudible; the channel the design names for the unposted is closed to her by birth; her only
legal voice runs through a priest who reports on the town; her most valuable knowledge cannot surface;
and her best act is unpriced. **A design that only works for people with names, offices, factions or
marks does not work, and this season is what that looks like from inside.**

## 9. Cells populated

Individual × {Material, Epistemic, Relational, Political-down, Coercive-at-maximum} · Hearth ×
{Material, Relational} · Community × {Political-up (back, plead), Epistemic (tell)}. **Nine of
sixty-four. Institutional: zero at every rung. Argument: one cell, at the smallest venue in the game.**

---

# III · PROBES

## Foreign

### Zoe Palaiologina — Katepano, frontier governor (`proposed`)

**Coordinates.** Off-board · binds-by-presence in Altonia · Altonia, avowed, high degree · Identity 0.50
/ Authority 0.30, "sincere imperialist" (`npc_registry.yaml:964`). Canon function: **decides whether
Altonia probes, presses, or invades.**

**Option set.** *Invade* is fully specified: 12 §7's muster → march → battle → siege, every part built
from existing objects, with foraging as hundreds of coercive acts against named hearths. *Probe* and
*press* have no verbs. A probe is an investigation act requiring presence she does not have. A press is
a dispensation she cannot publish into a scope she does not hold (06 §2's every channel needs presence).
A demand backed by force needs a shared venue, and 14 §5's venues are institution-scoped: **there is no
inter-realm venue anywhere in the suite**, so 08's negotiation machinery has no room to run in.

**Diagnostic — BLOCKED.** Her stated function is a three-way choice and the design supplies one arm. The
gap is nameable precisely: **there is no coercive-diplomatic act between "issue a dispensation in your
own scope" and "muster and march."** No ultimatum, no demonstration, no border incident, no reprisal
short of war, no demand. That absence is what makes escalation binary at the one seam where the setting
most needs it gradual.

**The one thing the design gets exactly right about her.** Her decision reads her *view*, and her view
of Valoria is built from merchants' and Doukas's tellings and nothing else. **The person who decides
whether there is a war holds the worst-corroborated ledger in the peninsula** — and 01 §3's
corroboration rule means a rumour retold through the same chain supports her inference exactly once.

### Stephanos Doukas — Kommerkiarios, trade prefect at the Schoenland interface (`proposed`)

**Coordinates.** Off-board, but with an office **whose scope includes a node the on-board world touches**
— 09 §10 counts Schoenland among the containment nodes. Precedent 0.50 / Order 0.30.

**Option set.** `examine` incoming cargo (producing firsthand roots, which is what an enforcement office
manufactures) · `LevyTerm` and `BlockadeTerm` within his scope · cite an ancient clause in argument at a
port venue where Solberg also stands · 06 §8's Cordon-Complete makes him an **AND**-term in anyone
else's chain, so a single bribed or absent captain at his node voids a cordon elsewhere.

His stated function — enforcing ancient treaties — lands squarely on 08 §4.1's graded proof, which is
computed from claim sources. A two-century-old clause proves at whatever grade its document's provenance
supports, and 09 §9 makes a written claim persist at a place and be found by `search`. Note the irony
the suite hands him: 04 §2.2 records that **Altonia destroyed the Almqvist records**, and Altonia's own
trade prefect is the peninsula's leading citer of ancient text.

**Diagnostic — RICH.** Material, epistemic, argument and political-down all live, with real forks. He is
the only foreign character in this lane who is rich, and the reason generalises: **the design is
generous to an off-board actor exactly in proportion to how much of their office's scope overlaps a node
the on-board world also occupies. Distance is not the variable. Scope-overlap is.**

### Rikard Solberg — Schoenland factor

**Coordinates.** Off-board origin, present at Valorian ports · **no office** · Independent — no faction
row · Utility 0.30 / Order 0.30 · goals: stable trade, avoid escalation, return home eventually.

**Option set.** He is the person 13 §4 was written for. `import_flow(r, good, season)` is the sum of
individual acts, each a person running the carry EV over a route they can reach. **Withdrawing a route
is a material act with political consequence, available to a person holding no office** — supply falls,
price rises, every hearth in scope recomputes `opening_set`, and a praefect's granary contest gets
harder. He also has `tell` into two realms' merchant channels, `back`, and — for "return home" —
`migrate`, which costs a standing he actually has.

**Diagnostic — RICH, bounded.** He is the suite's success case: real strategic reach with no post,
entirely computed. The bound is honest and named by 09 §4.4 (*personal leverage is bounded, not solved*):
his withdrawal moves `import_flow` by **his own volume**, so in a trade of a hundred factors he moves one
percent. Rich because the lever is real; bounded because it is a share, not a switch.

## The Southernmost wardens — the far end of Thread Sensitivity

### Edeyja — Warden-Chief, TS 75–80

**Coordinates.** Community rung (the wardens share a roof, a judging set and an assessment gate — a
containment community, not an alignment) · **no office** (`edeyja_npc.md`: *"Not a public figure. Not a
political actor"*) · Warden 0.40 / Precedent 0.20, Coherence 9 · goals: maintain substrate stability,
protect practitioners, continue the work.

**The probe: can a person at TS 75 communicate anything at all to the peninsula?**

03 §9 answers it and the answer is architectural. A rendering-side claim's subject is a **configuration**
— a referent class for which a non-sensitive's ledger *has no address*. Degradation is a property of
**deposit into that ledger**, so it fires on **every** path without any path knowing about it: `tell`,
`read_of(record)`, `reconstruct`'s inference, `examine`'s registration, **and the Knot's unbidden
deposit**. What arrives is `CONDITION(the place, wrong)` at 0.2. Nobody lied; nobody disbelieved; the
information did not survive the type conversion. Between sensitives above the floor it transmits
perfectly. P-13, exactly as canon states it, with no organ anyone could open.

**Three consequences the suite has not stated, and they are the probe's output.**

1. **She cannot petition — and not because she is refused.** 05 §1.1's second precondition is a claim
   naming a container with authority over the proposition; she can hold that. But the *proposition* has
   a configuration for its subject, so it degrades on deposit into every carrier's ledger. **Her petition
   is not dropped. It is unintelligible.** 05 enumerates forward / amend / bundle / drop / lapse. There
   is no *received and not understood*, and it is the only outcome available to her.
2. **The warden faction has a membership ceiling set by physiology.** A faction is a proposition plus a
   commitment map, and `commit` requires holding the proposition. Below the floor nobody can hold hers.
   07's whole apparatus — degrees, avowal, `capacity`, `power_base`, exposure — applies to the wardens
   correctly and every roll-up returns the canon count: single digits to low teens.
3. **The Knot gate and the rendering floor are set at different heights, and the gap between them is a
   population.** `form_knot` needs TS ≥ 30 on both sides; the Southernmost floor is *"set highest"*
   (03 §9). So every practitioner between TS 30 and that floor **can hold the channel and cannot hold the
   content** — they receive her crises as poetry through the one channel in the game that does not
   distort. That band is where the Restoration's practitioners sit.

**Diagnostic — THIN, and the isolation is mechanical rather than tragic.** She has real acts — Thread
ops, Mending, `examine`, assess and admit an arrival, hold a Knot with a northern practitioner — and
they matter. But every option that would *change her situation* is closed by the same floor, and the
differences between her available options are cosmetic against a losing trend she can measure and cannot
report. Canon says it in one line and the suite reproduces it exactly: *she needs help she cannot ask
for from people who don't know she exists.* **She is a destination, not an actor.** Playable — for
whoever reaches her. Not playable as her.

### Orm — Second Senior Warden, TS 60, thirty-one years at the Southernmost

**Coordinates.** Same community, no office, Warden **0.60** / Equity 0.20, TS 60, goals: *"The work. Only
the work."* His option set is Edeyja's minus the assessment authority.

**The finding.** At Warden 0.60 the work is a **constitutive** commitment (07 §1.2, degree 5): the
proposition holds a Conviction-primary slot and *"no offer term enters the refusal check at all."* Doc 02
§3.3's hysteresis has hardened it for thirty-one years of survived contradiction — `weight += 1` every
time the world failed to move him. `choose(person, view)` therefore returns the same act every season,
not because the engine is deterministic but because his stance table has become so.

**Diagnostic — THIN.** Options exist; one dominates absolutely. The sharper description, which the
rubric has no cell for: **he acts every season and chooses in none.** That is worth reporting as a
property rather than a defect — the design's own mechanism for making a person incorruptible (weight as
hysteresis, plus degree 5's missing offer term) is the same mechanism that makes them unplayable, and it
will fire identically on Grandmaster Ehrenwall's oath and on any Conviction the setting wants absolute.

## Goldenfurt ground

> ⚠ The six dossiers in `systems/settlements/goldenfurt_slice/npc_cast.md` are written in a *governance*
> vocabulary — AP verbs, `fires_card`, ambition `progress +1 each season`, Π homeostat, Disposition ±1 —
> with no counterpart in the merged suite, and its authored numbers are design-only. The translation is
> itself the probe, and one result is uniform: **every NPC's "autonomous advance +1/season" is a
> scheduled tick, which the suite refuses in three places** (02 §2.2 no experience clock; 04 §11 no
> scheduled restoration of standing; 09 §1.2 P1 admits metabolism only). What replaces it is `needs()`
> recomputed each season. **The cast survives translation. Their clocks do not.**

### Hedda Vorn — Magistrate

**Coordinates.** Settlement · binds persons by presence · no faction · β-conduct, "the law is the only
shield the weak have" · wants a provincial-magistrate seat and a parliamentary voice · **secretly shields
her brother Tomas.**

**Option set.** Wide. She allocates the granary (13 §3 — and the allocation *does not divide*, so every
opening is exclusive and manufactures a loser by construction). She confers gate wardenships (14 §2.3,
`δ = 1.5`, her determination alone). She holds court, which is a venue with a computed proof grade
(08 §4.1). She may `carry` and, if her charter names her, `compose_agenda` (05 §3.1) — the quiet power to
keep an item off a list for four sittings running. Her ambition is `contest(province, office,
claimants)`, whose score reads `capacity × norm × leverage`, all three of which she can work on by name.

**Her secret is an omission, and the suite handles that correctly.** She is not passing a mark and holds
no covert alignment edge. What she does is *not spend an investigation act*. 02 §1.2: *"Exposure is never
automatic… it rises only when a specific named person spends an investigation act."* A non-act deposits
nothing, so there is no seam. Her exposure route therefore has to run through someone else's firsthand
root — Old Brun's, or Alvid Bekk's — and that is exactly how the ground and the office rung connect.

**Diagnostic — RICH.** Five modes live, a genuinely exclusive material decision every cycle, and a
vulnerability that is discoverable rather than hidden.

### Curate Wessel — parish priest, secret informer

**Coordinates.** Community (the parish) · rank 3 · Church, avowed; informer, private · wants the Chapel
upgraded to a Church.

**What he is, mechanically, and it is larger than his dossier suggests.** He is a **channel** (06 §2:
parish priest, moderate fidelity, *coloured by the priest's own stance*). Every dispensation reaching his
congregation arrives in his version. That is a free, unlimited, weekly act of refraction over the only
community a person like Alvid has — and, per §II §5, he is also the **only legal intercessor** by which
anyone at rank 1 in his parish can address the magistrate. He sponsors into `support()`'s γ term. His
informing is an ordinary `tell` up an institutional relay, witnessable by the couriers.

**And his stated ambition is unreachable.** Upgrading a Chapel to a Church is *building a thing*, and
**the suite contains no construction verb at any rung** — no build, no endow, no found-an-institution, no
consecrate-a-structure. `found_hearth` is the only creation act in the corpus. This is not local to
Wessel: 13 §5 describes a dredging levy that must be "actively funded" and 13 §10's R-check prices a fork
*"invest levy income: granary vs. wall"* — **the R-criterion table prices a fork the option set cannot
express.** Every ambition of the form *make this place have a thing it does not have* is currently
inexpressible.

**Diagnostic — THIN.** Rich in exactly one act, which he performs by default and never has to choose;
BLOCKED on the goal canon gives him.

### Bailiff Konrad Ems — Crown levy agent

**Coordinates.** Settlement · Crown ministry · α-outcomes · wants a posting to Valorsplatz · corrupt.

**He is `enforcer_presence`.** 06 §3 makes a published dispensation land as a compliance contest whose
first term is *"is a person in the issuer's employ actually stationed here this cycle"*, and 06 §8 makes
the Crown's reach a **count of dispatchable persons**. Konrad is one of them. That is genuine structural
importance — and 14 §6's *"a King's decree is the least enforced instrument in the game"* is a statement
about how few Konrads there are.

**Both of his defining features terminate in missing mechanisms.**

- **The promotion.** A posting is a conferral: `admit()` with the Crown's coefficients (α 0.8, β 2.0,
  γ 2.0, δ 0.5, either term alone clears). He needs a public deed or an inner-circle sponsor. His route
  is a report — a `tell` up a relay to a respondent whose stance toward him is unformed, across a rank
  gap of three or four. **The corrupt bailiff petitions for his career through exactly the same funnel
  as the laundress in §II**: supplication, carried, through an intercessor. His entire advantage over her
  is one rank step and one institutional channel.
- **The corruption.** Taking Orsk Tallow's coin has no verb. 13 §9 refuses a currency outright; 07 §4's
  `purchased` power base says it rises by *"buy it"* at a cadence of *"money"*. **Those two documents
  contradict each other, and neither supplies a transfer act.** The only stores-moving acts in the corpus
  are `requisition` (kin edges only), `distrain` (creditor only) and `settle_in_full` (debtor only).
  There is no payment between two unrelated persons.

**Diagnostic — THIN.** Mechanically load-bearing, personally unexpressible.

### Mertha, Old Brun, Sister Aldith — the "petition generators"

Canon calls these three single-mention hooks. **The design makes them something else, and it is not more
play.**

**All three are rank 1** (05 §6.4's default clause), so all three are confined to supplication, carried,
through an intercessor who is Wessel. All three have the control's option set: eight acts, three dead
need terms, `mark_salience` 1.0, no Knot. The design does not distinguish them from Alvid Bekk by
anything except what is in their ledgers — and that is the whole finding.

**Old Brun, ferryman.** He holds the same object Alvid does and holds more of it: **firsthand roots**
about who crosses at night. Under 01 §3, independence is measured on firsthand roots, and a rumour with
no findable origin gets one synthetic root shared by every retelling — so Brun is not one voice among
many, he is the *only* corroborator, and a story about Tomas Vorn corroborates exactly once without him
and twice with him. Three parties want it. His decision — tell Ems, tell Hedda, tell nobody, or lie — has
materially different consequences and is a real fork. **But it is one fork, once.** The season he spends
his root he becomes the control. **Diagnostic — THIN**, and the finding generalises: *the design gives a
bottom-rung person genuine richness at exactly the moment they spend the one scarce claim they hold, and
returns them to the floor immediately afterward.*

**Mertha, miller's widow.** Her son is taken in the war-levy. Two mechanical facts.
(a) Her want is a PRIVATE proposition (06 §6.2 — it names a specific person), so it is satisfiable by
grace and only by grace, and grace on a completed muster returns a man who has already marched.
(b) Sharper: 04 §1.3's succession machinery fires on **death** and emits a vacancy. Her son is *alive and
absent*. **There is no mechanism anywhere for a seat whose holder is living and away** — the mill's
holdings follow a pointer to a person who cannot work them, `draw` collapses for a reason no formula
models, and no vacancy opens because nobody died. Conscription, hostage-taking, imprisonment and exile
all produce this state, and **Prince Torben is the same gap at the top of the ladder.**
**Diagnostic — BLOCKED.** She wants a reversal of an apportionment (12 §2.2, an act by a named person)
and the design contains no act that reverses one.

**Sister Aldith, lay almoner.** Lay, so no office and rank 1; the parish's tithe is allocated by the
priest, so she holds no prize. What she does have is real and slow: she is present at relief
distributions at `venue_factor` 1.0, she is in the judging set of everyone she feeds, and she deposits
claims about the hungry into ledgers that would otherwise hold no rows about them. That makes her a
**norm-mover** by the Restoration's own method (04 §5: *they do not attack the norm, they change the
membership*), one stance at a time. **Diagnostic — THIN.** She can move `norm(parish, ·)` and she cannot
bind anyone, and the two facts do not connect within a human lifespan.

**The answer to the probe.** They are not petition generators in this design. **They are root-holders**,
and root-holding is not an act — it is a property of a ledger that becomes valuable only when someone
with standing spends an investigation act on them. The bottom of the ladder has play in it, and the play
belongs to whoever comes down looking.

---

# CELLS POPULATED

| rung | Material | Epistemic | Pol-up | Pol-down | Argument | Coercive | Relational | Institutional |
|---|---|---|---|---|---|---|---|---|
| **Individual** | Alvid (hoard, migrate) | Alvid, Brun (roots) · Edeyja, Orm (Thread-Read) | Alvid (back) | Alvid (comply / evade) | — | Alvid (the knife) | Alvid (requisition, foster) | — |
| **Hearth** | Alvid, Mertha | — | — | — | — | — | Alvid (edges), Mertha | — |
| **Community** | — | Wessel (channel) · Aldith (norm) · Edeyja (assess) | Alvid (plead at parish) | Wessel (refract) | Alvid (parish stake) | — | Aldith · Edeyja (admit) | Wessel (sponsor, γ) |
| **Settlement** | Vorn (granary, exclusive) | Vorn, Ems (investigate) | Vorn (carry, compose_agenda) | Vorn, Ems (issue, enforce) | Vorn (court) | Ems (`enforcer_presence`) | Vorn (kin, shield) | Vorn (confer wardenship) |
| **Territory** | Doukas (levy, blockade at the interface) | Doukas (examine) | — | Doukas | Doukas (port venue) | — | — | — |
| **Province** | — | — | — | Laskaris (publish / refract) | Laskaris (Altonian venue) | — | Laskaris (marriage, hostage) | Laskaris (confer at home) |
| **Realm** | Solberg (route withdrawal, bounded) | Palaiologina (worst ledger, highest stake) | — | — | — | Palaiologina (invade only) | Laskaris (banked claim) | — |
| **Off-board** | Laskaris (treaty → supply → price) · Solberg | Laskaris (captains) | **EMPTY** | Laskaris (own scope only) | **EMPTY between realms** | Palaiologina, at one value | Laskaris | Laskaris (own tree only) |

# CELLS I FOUND EMPTY

1. **Institutional × every rung below Settlement.** Zero of five acts. The two new rungs the design was
   built to add have no institutional play at all.
2. **Material × any rung, for a person with no holding.** No `sell labour`, no wage term in `draw()`, no
   coin. 12 §6.4 asserts wage-fed hearths; nothing produces one. 13 §9 refuses the unit.
3. **Material × Settlement and above — construction.** No build, endow, found-an-institution or
   consecrate-a-structure verb exists anywhere. 13 §10 prices an investment fork the option set cannot
   express, and Wessel's canon ambition is unreachable.
4. **Material × any rung — payment between unrelated persons.** No `pay`, `buy`, `bribe`, `hire` or
   `sell`. 07 §4's `purchased` basis rises by *"buy it"*; 13 §9 deletes the unit it would be denominated
   in. Direct contradiction, unreconciled.
5. **Political-up × Off-board.** No off-board person can `carry`, because `carry` needs standing at the
   respondent container and standing does not travel (04 §9). Elske and Torben hold none either.
6. **Argument × Realm-to-Realm.** No inter-realm venue. 08's negotiation machinery has no room to run in
   between two sovereigns, so diplomacy is a treaty signed in one room or nothing.
7. **Coercive × Off-board, below invasion.** No ultimatum, demonstration, border incident, reprisal or
   demand backed by force. Palaiologina's canon three-way choice has one arm.
8. **Epistemic × any rung, for a Southernmost-floor claim into a below-floor ledger.** Correct by design
   (P-13), and it deletes the entire up-stroke for the wardens. 05's outcome enumeration has no
   *received and not understood*.
9. **Relational × Knot, for the roughly half of the peninsula below TS 30.** Named by 02 §11.2 and
   deliberate. The control is in it, and so is Elske, and so is the royal marriage.
10. **Vacancy-by-absence, at every rung.** Death emits a vacancy; conscription, hostage-taking,
    imprisonment and exile do not. Mertha's son and Prince Torben are the same hole at opposite ends of
    the ladder.
11. **A community's own admission vector.** `(α, β, γ, δ)` is editable by a dispensation from Settlement
    or above (04 §5; Vaynard's Path B). `contest` can in principle put it up as a stake, but **no act is
    named by which a winner writes it.** A guild cannot lower its own bar.

**Collisions found while populating, reported and not resolved:** two owners and two ranges for
`need(subsistence)` (02 §6 vs 04 §1.2 / 13 §1) · the parish congregation as a presence-based community
against single-parent containment (01 §1.1 vs 01 §4 vs 04 §7) · `purchased`'s money against 13 §9's
refusal of currency · Goldenfurt's address (canon Kronmark / Crown vs suite Grauwald / Varfell) ·
04 §12.4's own flagged per-hearth standing date.

**The one sentence this lane exists to deliver.** The control has eight acts and almost nothing to
decide: three of four needs are structurally zero, her capability adds no verbs, her marks make her
inaudible, the design's named channel for the unposted is closed to her by birth, her only legal voice
runs through the man who informs on her town, her most valuable claim can never surface, and her best
act is unpriced. **The floor is THIN, and no amount of richness at the top repairs it.**
