# 04 — Seasons: THE DUCHIES

## Status: FILED (2026-08-30) — Lane 3 output of the play-space coverage instrument. Nothing here ratifies on merge.
## Reads: `00_PLAN.md` (method, axes, §4 season shape, §5 discipline) · `01_ROSTER_AND_FINDINGS.md` (four binding findings)
## Authority on mechanism: `proposals/2026-08-29-valoria-from-scratch/` (01, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14)
## Authority on persons: `references/npc_registry.yaml`, `canon/03_canonical_timeline.md`
## Lane question: **is a Duke's season genuinely different from a Praefect's writ large?**

---

## 0. What I assume before the first season, and why

Four declarations. Three are branches I take without resolving; one is a fifth canon collision the
roster did not catch, reported per FINDING 3's convention.

**0.1 The conferral dilemma — I assume OFFICE-ROOTED, and mark where it matters.** The suite asserts
both and resolves neither (`00_INDEX §3.2`). It bites here in one place: `14 §1.5` makes **praefect** a
Crown appointment, revocable by the Crown, sitting on settlements *inside* Varfell and Hafenmark.
Office-rooted, a Crown succession hands the successor the power to revoke every praefect in both
duchies. Person-rooted, Almud's death leaves those praefectures with a **dead conferrer** —
irrevocable, unreplaceable, and both dukes governing settlements administered by men nobody living can
remove. Both are playable; they are not the same game. Full statement at F10.

**0.2 The act budget is contradicted inside the suite, and the contradiction lands on this rung.**
`09 §1.1`: *"Every person and every cohort commits exactly one act per season… it is the one
discretionary commitment."* `14 §8`: *"A worked season — Vaynard, one turn, **ten acts**"* — spending
`convene`, `issue`, two `dispatch`es, `confer`, `revoke`, `carry` and `commit`. And `seat_items` has
two owners: `14 §1.3` calls it the holder's own hours, `05 §3.1` calls it the container's capacity and
separately charges `compose_agenda` *"one of v's own acts for the season."* **I write both dukes at
one act per season, per `09`, because `09` owns the tick** — and record at F1 what changes if `14 §8`
is right, because this lane's answer depends on it more than on anything else in the design.

**0.3 A fifth canon collision, of FINDING 1's shape but at the level of mechanism.**
`04 §10`'s Trace A gives Duchess Inge Baralta *"a banked claim on the Crown seat (basis: **marriage**,
watch: any Crown vacancy)."* Canon (`03_canonical_timeline.md:143`) says she is **unmarried,
childless, heirless**. The suite's object survives — `04 §3.2` holds a banked claim at the
*claimant_hearth*, not the person, so the Baralta hearth may hold a marriage-basis claim from a prior
generation and Inge is its claimant as seat-holder. I take that reading. But it is a reading, the
suite does not state it, and the trace as written attributes to a canon person a claim basis her
canon facts forbid her to have created. Reported, not resolved.

**0.4 What canon supplies that the suite must be read against.** The Secession Wars ran ~195–200 AG;
game start is **245 AG**. Canon: *"Ducal authority cannot be unilaterally overridden"*; Hafenmark
retains parliamentary traditions; Varfell retains **territorial independence**; the Baralta family's
ducal status was earned through wartime deeds. The last clause is the one this lane keeps stubbing
its toe on, and §1 works it.

---

## 1. Duchess Inge Baralta of Hafenmark — FULL SEASON

### 1.1 Coordinates

| axis | value |
|---|---|
| **A · rung** | Province/Duchy (Hafenmark), with a hearth seat at the Baralta hearth |
| **B · office** | binds persons-by-presence · **convener** and **veto-holder** at the Hafenmark Court Parliament (`14 §5`, `08 §10`) · conferral basis **deed + kinship**, conferrer *nobody living*, **not revocable** (`14 §1.5`) |
| **C · alignment** | *(Inge Baralta, holds, the throne, on the next vacancy, **will**)* at degree 5 constitutive, **avowed** (`07 §1.1` names this proposition explicitly) · a second, *(the constitutional framework supersedes Church jurisdiction, **ought**)*, avowed |
| **D · marks** | caste-advantaged · non-sensitive (TS `[GAP]`) · house name Baralta, a deed-family mark · no guild grade, no Church standing |
| **E · modes reachable** | Institutional, Political-down, Argument, Material (mediated), Relational · **Coercive is thin** (canon Military 3, the lowest of the great factions) · **Epistemic is her binding constraint** |

Convictions: Precedent 0.50, Authority 0.30, self/other −0.30 (`npc_registry` NPC-050). Under the
suite these are stance rows, not a store (`07 §1.2`), and Precedent-primary is exactly the coefficient
that makes her a venue player rather than a coercive one.

### 1.2 Opening state — the six person fields, and what is conspicuously absent

Address, marks, capability, stance, memory, ties. Two absences do all the work.

**Absence one: the succession pointer leads nowhere.** `04 §1.1` holds `pointer` — three separable
lists, name / seat / holdings — at the hearth. Inge is unmarried and childless, so the *seat* list
has no default target. `04 §1.3`'s three outcomes then read, at her death: not one claimant with
capacity, and no office-holder who can bind claimants of a ducal seat (there is none — the Crown
cannot revoke a duchy, `14 §2.4`), which is **branch three: unresolved, held by whoever physically
holds it, re-opening at every standing date, depositing grievance each time. Open war.** Her own
death is a larger event for Hafenmark than Almud's is for the Crown, and it is a condition of her
person fields rather than a plot.

**Absence two: she has no world-read need at all.** `01 §2` splits needs into two that read the world
(subsistence, standing) and two that read the view (commitment, exposure). Her hearth is Provisioned,
so `need(subsistence) = clamp(0,1,(2.0 − margin)/2.0) = 0` and `04 §1.2`'s unbounded coercive term
never fires. Her `expected_standing` and `held_standing` are both at the ceiling, so
`need(standing) = (7−7)/3 = 0`. **Both formulas the suite actually wrote produce zero for her**, so
everything she wants comes from the two needs it names and never computes (F2). A magnate's entire
agenda is therefore a function of her ledger — a fine property with no arithmetic behind it.

**Ties.** Knots are TS-gated (`01 §2`); her TS is `[GAP]`. If she cannot form one, her only channels
are institutional — the profile `06 §2` says receives *sharp* decrees and *no* whispers.

### 1.3 Computed needs, with the arithmetic

- `need(subsistence)` = **0** · `need(standing)` = **0**. Both shown above.
- `need(commitment)` — the Crown proposition, unsatisfied. **No formula exists.** `05 §1.1` needs an
  `urgency(prop)` to compute `shortfall = urgency − reach`, and its own worked table hands Vaynard
  `urgency 0.91` with nothing deriving it. I assert Inge's as high, and say so, because the suite does.
- `need(exposure)` — live: the Church tithe runs through Hafenmark under the Dicastery of Temporal
  Affairs' `LevyTerm` (`13 §7`), and every settlement in her duchy is administered by a
  **Crown-conferred praefect** she cannot revoke (`14 §1.5`, §2.4).

`reach` is *"max over her own acts of expected satisfaction, taken over her VIEW."* Her act menu is
large; her reach on this proposition is not, and §1.5 is why.

### 1.4 The view, and one claim she holds that does not surface

`03 §4` / `01 §3.1`: K = 12 claims, ranked by `recency × confidence × relevance × stance weight`. Her
working set this season, from a duchy most of whose settlements report to her as cohort rows rather
than named persons (`14 §3.1`):

1. The Crown's consecration warrant sits in Church custody, and **two of four Cardinal seats are
   candidates rather than occupants** (FINDING 4) — so custody at the Dicastery of Doctrine and
   Archives is indeterminate *today*.
2. Her silver mine's `draw()` has trended down for three reckonings (`13 §5`).
3. Hafenmark's harbour channel: the Parliament voted the dredging levy down a generation ago, as
   popular tax relief (`13 §5`).
4. The count of living Secession War veterans in her own ledger — the numerator of
   `deed_weight(Almqvist, Crown)` (`04 §3.4`).

**The claim that does not surface** is (2) read correctly. Her ledger holds *the mine's draw is down*;
it does not hold *the seam is depleting*, because `13 §5` never publishes the depletion rate —
*"discoverable only by investigation."* Her stance weight ranks the mine below the Crown Claim, and
that one multiplication (`01 §3.1`) is what keeps it under the K-line. **She is funding a
counter-armament against a seam she has not measured.**

### 1.5 The option set — every act, and why each is legal. **The gaps live here.**

| # | act | legality | what it reaches |
|---|---|---|---|
| 1 | `convene` the Court Parliament and **order its items** | `14 §1.1` remit act; she is its convener (`14 §5`) | *"the cheapest real power in the game"* — three items ahead of yours kills yours by seat capacity, at no cost |
| 2 | **veto** a carried motion → `CARRIED-WITHOUT-FORCE` | `08 §10` names the Duchess as the veto-holder | strips force; **does not strike the record row**, which stays citable and leaves an F2 hazard on everyone who voted |
| 3 | `issue` a dispensation over Hafenmark — a dredging `LevyTerm`, a `PriceTerm`, an `OrdenanzaTerm` | `14 §1.1`, `06 §1` | subject to the reach cap: publication-with-enforcement consumes one establishment member per node (`06 §8`) |
| 4 | `confer` a provincial **sub-remit** — a reeve, a territory governor | `14 §3.2` | buys reach and manufactures shadow standing in the same act |
| 5 | `revoke` inside her conferral subtree | `14 §2.4` | **her own appointees only.** Not the praefects, not a benefice |
| 6 | `dispatch` a household member to a node | `14 §1.1` | buys *fidelity* — that node stops being a cohort in her ledger (`14 §3.1`) |
| 7 | `carry` / `amend` / `bundle` / `drop` at a standing date | `05 §3.2` | her seat items |
| 8 | **`legitimate`** a cadet Baralta into the hearth's seat list | `04 §2.2` — *"inserts a person into the seat list at a declared degree"* | the only act that closes absence one |
| 9 | marry, and bank a claim | `04 §2.2`, §3.2 | forecloses nothing; costs a season |
| 10 | `commit` at degree, avowedly, at publicity 2.0 | `07 §1.2`, `04 §4.1` | she already has |
| 11 | `tell` / `lie` at the Parliament | `01 §3.3` | including a false assertion of remit (`14 §2.2`) |

**And now the hole, which is the whole point of writing the table out.** Canon's Inge wants the
Crown. `08 §10.1` composes that want: a Crown Succession Contest is a motion with **five separately
proved articles** — descent · deed · **consecration consent** · no prior conceded record · the
cognatic-senior capacity test. Article 1 is ungradable for *everyone* because Altonia destroyed the
records. Article 3 requires an instrument in the Church's custody, and *"if the Church's own
succession is contested, there is no determinate custody, so no ground can be graded G4, so article 3
cannot reach the floor for any claimant."* Per FINDING 4, custody **is** indeterminate at game start.

So: which of her eleven acts touches article 3?

**None.** She cannot confer a Cardinal (the Confessor does, `14 §2.3`), cannot revoke one (not her
subtree), cannot convene a Dicastery (its Cardinal does), holds no benefice, and sits in neither the
conclave's committee nor any Dicastery's judging set. `14 §5`'s door rules exclude her from three of
the four Dicastery venues outright — Doctrinal Adjudication enters *clerics in orders*, Doctrine and
Archives enters *anyone with a register petition* — leaving her one door, at which she may enter and
must find a Canon to speak.

**On the single article that decides her single stated goal, a named faction leader has a zero-length
option set.** She is not a SPECTATOR overall — the table above is eleven live acts — but she is a
spectator *on her own victory condition*, and that is worth more than a global verdict.

There is exactly one exception and it is instructive. `08 §4.1`: a G4 instrument is *"attackable by
attacking the custody chain — forgery, substitution, or an unattested copy,"* and `04 §2.2` says an
uncontested assertion made by whoever holds the record *"is deposited into every ledger as genuine
until a contradicting claim arrives."* So the design does give her a route to article 3 — **acquire a
person inside the Dicastery of Doctrine and Archives.** That is `07 §2`'s existential over persons: a
recruitment and investigation problem. It is not an office act, it is not a Duchy-rung act, and it is
by a distance the most interesting thing on her list.

### 1.6 The choice, through the seven phases

She takes act 8. **She legitimates a cadet Baralta into the seat list**, at the Parliament's
quarterly sitting.

- **P0 CALENDAR.** The Parliament's quarterly date fires; so do the tithe reckoning at two settlements
  and the mine's dues reckoning.
- **P1 SETTLE.** Larders consume; the mine's `base(H)` silently decrements again (`13 §5`); the
  harbour accrues silt. No social quantity moves — `09 §1.2` enforces that by phase membership.
- **P2 NEEDS.** Both computed needs return 0. The act is driven entirely by an uncomputed one.
- **P3 VIEW.** K = 12. The mine claim ranks 14th and does not enter.
- **P4 CHOOSE.** Her one act — so this season she does not convene an agenda, does not issue the
  dredging levy, and does not dispatch anyone.
- **P5 RESOLVE.** Legitimation is an **assertion** (`04 §2.2`) at `venue_factor` 2.0. Not adjudicated
  here; *done*, and contestable later.
- **P6 WITNESS.** `publicity = 2.0 × √(witness count) × mark_salience`, hers at the top of the scale:
  every seat-holder, then Hafenmark's communities within a season or two. The judging set deposits
  divergently — her Precedent- and Authority-primary councillors read *the succession is secured*; her
  commune constituency reads, through `04 §4.1`'s marks term, *a cadet was raised over persons with
  standing*. Every cadet Baralta hearth at `need(standing)` 1.0 now holds a claim that the ladder moved
  for someone else.
- **P7 RECKON.** Confidence decays; the seat-list row is permanent world state and the *claim* of it
  is not.

### 1.7 What propagates

**Down-stroke: none** — legitimation issues no terms. **Up-stroke: none** — no petition was carried.

What propagates is neither stroke. It is the **judging set** (`04 §4.1`), and, one rung out, the
`banked_claims` register: `04 §3.2`'s watch predicate on the ducal vacancy now has a claimant with
capacity where it had none, and every rival cadet branch's claim is worth less against a named
competitor than against an empty pointer. Reach: Hafenmark's communities by ambient publicity; the
Crown and Varfell only if somebody tells them, which nobody has yet done.

**And the thing that did not propagate is the finding.** A duchess spent her season's one act and
changed the terms of exactly zero containers. Under `06 §9`'s own test — query any postless person's
`opening_set` before and after — this season is silent, because it issued no dispensation.
Legitimation is a Hearth-rung act performed by a Duchy-rung person, and the ladder carried it
nowhere.

### 1.8 Diagnostic — **RICH, with a BLOCKED core**

Eleven legal acts with materially different consequences; a genuine fork between securing the seat
and pursuing the Crown; a second genuine fork between dredging and arming. That is RICH.

But her *stated goal* is BLOCKED at article 3 by a vacancy in another faction's office cluster, with
no act in her set that touches it, and the only route the design offers runs through recruitment and
forgery rather than through anything a duchy does.

**R-check — does any option dominate by shape of gain against shape of cost?**

- *Legitimate a cadet* — gain: closes branch three at her death; **compounds**, because the heir
  accumulates standing and precedent leverage (`04 §3.3`) from the day it is signed. Cost: the cadet
  is now a claimant with capacity *while she lives*, and `07 §5.2` says shadow standing above zero
  makes her cheapest future act legalisation. Also compounds. **Not dominant.**
- *Wait, per `14 §9`* — the suite calls hoarding the deed presumption *"zero cost and a gain that
  decays to zero with certainty"* and derives her whole strategy from it. **It is wrong here.**
  `04 §3.4` counts living **firsthand** witnesses; canon roots the **Baralta** ducal status in the same
  Secession-era deeds, and `14 §1.5` gives its conferrer as *"nobody living — deed at the Secession
  War."* The war ended 45 years ago, so a firsthand witness is at least sixty — and **the numerator
  decaying under the Almqvists is the same numerator decaying under the Baraltas.** Waiting dissolves
  the warrant for her own office at the same rate. What survives the clock is her purchased and
  bureaucratic mass (`07 §4.1`), not the deed. A race between two decays, scored by the suite as free.
- *Dredge or arm* (`13 §5`) — dredging: compounding gain (a route half the peninsula's grain relies
  on), flat cost. Arming: flat gain (one claim window), compounding cost (a depleting seam). Neither
  dominates; the crossing point is whether anyone investigates the seam. **The design has tied her
  duchy's economy to an investigation act nobody has performed.** That is good design working.

### 1.9 Cells populated

`Duchy × Institutional` · `Duchy × Argument` (as convener and veto-holder) · `Duchy × Relational`
(legitimation, a Hearth act reached from the Duchy rung) · `binds-persons-by-presence × constitutive
avowed alignment` · `caste-advantaged × house name × no Church standing`.

---

## 2. Duke Magnus Vaynard of Varfell — FULL SEASON

### 2.1 Coordinates

| axis | value |
|---|---|
| **A · rung** | Province/Duchy (Varfell), hearth seat at the Vaynard hearth |
| **B · office** | binds persons-by-presence · conferral **deed + kinship**, conferrer *nobody living*, **not revocable** (`14 §1.5`) · canon: *"Varfell retains territorial independence"* — see §2.5 |
| **C · alignment** | *(the caste order ought to be broken)* at degree 4–5, **avowed at publicity 2.0** (`14 §8` writes this act explicitly) · *(the Church and Altonian residue ought to be expelled from Varfell)*, avowed |
| **D · marks** | **Southern Einhir heritage** — the caste-excluded mark, worn by a duke · **Thread-sensitive** from environmental exposure (canon) · house name Vaynard |
| **E · modes reachable** | all eight, and this is the point: Vaynard is the one character in this lane who is simultaneously caste-advantaged by office and caste-excluded by mark |

Convictions: Equity 0.35, Utility 0.30, self/other −0.40 (NPC-052) — sincerity, instrumentality and
ego, as three stance rows.

### 2.2 Opening state, and what is conspicuously absent

`04 §4.1`'s `mark_salience` counts the actor's marks any community member holds a *strong* stance
toward. His runs at maximum in a Crown-Latinate quarter and near its floor in an Einhir hamlet, so the
same act *travels twice as far* in the places most hostile to it — and `14 §1.3` charges every
act-by-remit at `venue_factor ≥ 1.0` on top. **A Southern Einhir duke cannot act quietly anywhere
north of his own fjords.**

What is absent: **an establishment large enough for his scope.** `14 §9`'s own accrual case is Varfell
— *"twelve settlements, a ducal household of nine dispatchable persons."* Under `06 §8`'s reach cap,
nine nodes get publication-with-enforcement, three get `enforcer_presence = 0` and crater
structurally, and the western-fjord pockets get folk gossip degraded by hop count with nothing to
reset it.

### 2.3 Computed needs

Same shape as Inge's and same hole: `need(subsistence) = 0`, `need(standing) = 0`, and everything he
does is driven by the two needs nobody computed. `05 §1.1`'s worked table is *about him* and assigns
`urgency 0.91` to *the Masterpiece Examination's caste gate is abolished across the realm*, with
`reach 0.44` and `shortfall 0.47` — identical to a hamlet fisher's shortfall on a granary, which is
the suite's own demonstration that the function does not consult post. The 0.91 is asserted.

The table's `reach 0.44` deserves reading, because it is honest and damaging: *"he can issue a
dispensation in scope Varfell — half the guilds sit outside it, and the Church's gate is not his."*
His duchy is not a big enough container for his want.

### 2.4 The view — reach as blindness

`14 §3.1` is the strongest idea in the suite for this rung and it is what makes Vaynard's view
different in kind from a praefect's: *"a node nobody reports from produces no firsthand claims in the
office-holder's ledger… a settlement with no dispatched person, no relay, and no petitioner who got
through is literally a cohort in the Duke's view — one row, coarse, stale, carrying nobody's name."*

With nine dispatchable persons over twelve settlements plus the fjord pockets, **most of Varfell is
one row per node in his ledger.** He does not have a blurred picture of Stillhelm; he has no picture
of Stillhelm. `03`'s empty view is ignorance, not uncertainty (`01 §3.1`).

**The claim he holds that does not surface:** `07 §3`'s worked underestimate is his — *"Vaynard's
estimate of the Restoration in Grauwald is density 0.02 — two men caught. The truth is 0.19 across
four hamlets."* Its two constituent claims are three seasons stale, and they sit in his K = 12 above
better claims because their `confidence` was firsthand at deposit and nothing has contradicted them.

### 2.5 The option set — and the finding that Varfell is not one office

Vaynard's eleven acts are Inge's eleven with two substitutions: he holds no parliamentary veto, and
he holds a coastal blockade (`06 §4`'s worked `BlockadeTerm` is his). But the interesting question at
this rung is not *what acts* — it is *whom they reach*, and Varfell's answer is different from
Hafenmark's.

Canon: **"Varfell retains territorial independence."** `npc_registry` gives a **Jarl Council** whose
members are *Senior Jarl of the Western Highlands* and *Military Jarl* — territory office-holders
binding persons by presence. If those jarldoms were conferred by Vaynard, they lie in his conferral
subtree and `14 §2.4`'s `revoke` reaches them. If they are heritable deed-seats like his own — which
is what "territorial independence" says — then **they have no living conferrer either**, and:

- `revoke` cannot reach them (`14 §2.4`, conferral subtree);
- `dispatch` cannot reach them, because dispatch is `requisition` on an **establishment** member
  (`14 §1.1`) and a peer office-holder is not establishment;
- so his only channels to his own council are `requisition` through a faction edge (`07 §1.2`),
  `convene` plus argument (`08`), and `tell`.

**Varfell is therefore not a duchy in the sense Hafenmark is. It is a confederation of
non-revocable seats whose duke has no institutional channel to his own council.** The suite does not
say this; it falls out of `14 §1.5` + `14 §2.4` + canon's one clause, and it is the single largest
structural difference between the two duchies in this lane. It also means `14 §9`'s "maximum
mitigation" answer for Varfell — *delegate five territory sub-remits* — is unavailable over ground the
jarls already hold, because you cannot carve a sub-remit out of scope you do not hold the remit for.

### 2.6 The choice, through the seven phases — **reform as an act**

He takes the act the roster asked me to probe. He `issue`s a dispensation over Varfell whose terms
are an `EntryStandardTerm(gate_delta)` raising **β** — the deed/work coefficient — at every guild
admission gate in the duchy, bundled with the `ExemptionTerm` `06 §1` names as his (*"Vaynard's
Examination-fee waiver for Southern Einhir apprentices"*).

This is Path B expressed as an admission coefficient, exactly as `04 §12`'s challenge says: *"Duke
Magnus Vaynard's whole Path B is a dispensation editing β."*

- **P0.** The Masterpiece Examination's date is on the docket at three Varfell settlements; so is the
  tithe reckoning, the Church's `LevyTerm` collecting inside his duchy through offices he cannot
  revoke (`13 §7`, `14 §2.4`).
- **P1–P3.** Larders; the fjord pockets roll a bad `season_factor`. Needs zero and zero plus the
  uncomputed one. View K = 12, most of the duchy present as cohorts.
- **P4.** `issue`. One act — so **this season he does not publish it with enforcement anywhere**,
  because publication-with-enforcement consumes establishment per node (`06 §8`).
- **P5.** `06 §3`: *a published Dispensation does not apply* — it lands per node as a compliance
  contest reading `enforcer_presence`, local judging-set stance, and distance.
- **P6.** Publication as telling, distorting. `06 §2`'s first free consequence fires against him —
  *"terms drop before values distort"*: the headline (*the gate is open to Einhir hands*) survives
  every hop, the qualifiers shed first. **What reaches the western fjords is stronger than what he
  signed.**

### 2.7 What propagates, and the consequence he did not intend

Next season the Free Masters of the Row sit an examination. `04 §5` states the counter-move as a
property of the object, not a rule: *"raising β changes no one's stance, so a committee that wanted to
exclude routes the same exclusion through γ (no Free Master will sponsor him) and δ (personal dislike,
unfalsifiable). **A caste-breaking law is evadable through the terms it does not name.**"*

The candidate's `performance` is 4.0 and now weighted higher. His `γ` is 0 because no Free Master will
stake regard. His `δ` is negative from four masters. `support` stays under zero for the majority.
**Refused, lawfully, under the duke's own reform.**

And here is the second-order consequence, which is derived and which I did not have to invent, because
`07 §7` states the general shape: *"any faction whose implementation acts deposit an early, general,
high-confidence explanation into the ledgers of persons in its scope forecloses whatever inferences
that explanation pre-empts — including inferences no member has ever considered."*

Vaynard's publication is exactly that act. It deposits, into every Southern Einhir ledger in Varfell,
a general high-confidence claim: *the gate is open.* When the candidate is refused, `03 §4`'s view
assembly finds his anomaly **already resolved** by a higher-confidence general explanation — *the
gate is open, therefore the refusal was about my work* — and `06 §5`'s targeting order puts the blame
where the witnessed causal chain is shortest: on the four masters, by name, firsthand, not on the
distant duke whose levy or law set the terms.

So: **no petition is raised**, because `05 §1.1`'s condition 2 requires a ledger claim naming a
container as holding authority over the proposition, and the candidate's ledger now says the authority
already acted. Nothing travels up. Nothing reaches Vaynard's nine dispatchable persons. Nothing enters
his K = 12.

**Duke Vaynard's reform suppressed the grievance that would have told him the reform failed.** He will
believe it worked for as long as nobody investigates, and `14 §3.1` says his ledger over those nodes
is a cohort row. That is the consequence he did not intend, it is the same mechanism `07 §7` uses for
the Church's unwitting suppression of Thread Sensitivity, and it is running against a duke who is
himself Thread-sensitive.

**And the third order, which `14 §7` states outright:** if Path B succeeds and the Church's residue
leaves Varfell, benefices go unfilled, catechesis stops depositing early general explanations, and
**TS emergence in Grauwald, Stillhelm, Oastad and the western fjords rises over a generation.** The
duke who wants Einhir revival gets more Thread-sensitive Einhir, and the caste marks that exclude
them get more salient. He did not intend that either.

### 2.8 Diagnostic — **RICH**

Genuinely several live options with materially different consequences, at least one of which — the
`EntryStandardTerm` — produces a consequence that inverts its intent through three separate mechanisms
none of which were written for it. This is the best-served character in the lane.

**R-check.** `14 §9` runs *enforce or tolerate* and *appoint the capable or the loyal* and finds
neither dominant; both apply to him unchanged. The fork this season adds is **reform by coefficient
versus reform by appointment**: `14 §8` notes he can instead `confer` a provincial sub-remit on a
capable Southern Einhir reeve — *"Path B expressed as an appointment rather than a speech"*. Gain from
the coefficient: broad, cheap, **evadable**, and it decays to nothing the moment a committee routes
around it. Gain from the appointment: narrow, one node, **unevadable**, and it *compounds* because the
appointee's shadow standing rises from the day it is signed. Cost from the coefficient: near zero, and
that is precisely why it is worthless. Cost from the appointment: one man who becomes a root on
Vaynard's death (`07 §5.3`). **Neither dominates, and the shapes are genuinely different — this is the
R-criterion passing on a fork the design did not set up deliberately.**

### 2.9 Cells populated

`Duchy × Political-down` (the live one) · `Duchy × Institutional` · `Duchy × Coercive` (levy
apportionment, `12 §2.2`) · `Duchy × Material` (the `BlockadeTerm`, mediated) · `caste-excluded ×
Thread-sensitive × binds-persons-by-presence` — **the cell nobody else in the roster occupies.**

---

## 3. PROBE SEASONS

Coordinates, option set, diagnostic. The question for all seven is the one the brief names: *a person
on an inner council has standing and proximity but may hold no office that binds anyone.*

### 3.1 Torvi Heljason — Legal Advisor to Baralta (Precedent 0.70, Evidence style)

**Coordinates.** Duchy rung · **office: NONE.** Advising binds nobody, and `14 §1` requires
`remit.binds ∈ {members-by-admission, persons-by-presence}` — an advisor has neither. Alignment:
Hafenmark's proposition at high degree, avowed. Marks: caste-advantaged, no house name of note.

**Option set.** `carry` at the Parliament (she holds standing at the container, `05 §3.1`'s
precondition); `tell`; be `dispatch`ed as **establishment**; sit in the judging set; `commit`.

**Two derivations make her more powerful than her title.**

First, `14 §1.2`: an act by remit draws its pool from *the dispatched establishment member actually
performing it*, not from the office-holder. So when Inge argues a precedent at her own Parliament,
**Torvi's Precedent 0.70 and Evidence style are the pool.** She is not a bonus on the Duchess; she is
the roll.

Second, `07 §5.2` + `14 §1.4`: `licensed_standing` sums only contributions routed through a remit.
**Torvi holds no remit, so her licensed standing is zero and her entire standing is shadow.** `07 §5.2`
then fires structurally: an act of Inge's whose `requires` predicate names persons in Torvi's support
set returns an *empty existential* if Torvi is not with her — an absence, not a penalty. Twice, and
Inge's cheapest remaining act is **legalisation**: a dispensation naming Torvi's function. **A
councillor with no office is the design's own generator of new offices.** Her power_base is
`07 §4`'s **bureaucratic** — *"a clerk at standing 1 who reads every petition outranks a minister"* —
cut by *"a single bypass, used publicly once."*

**Verdict: RICH.** Not for the length of her act menu, which is short, but because two quantities she
does not control ratchet her toward an office, and the cut that removes her is one public act.

### 3.2 Olaf Geirson — Military Commander, Hafenmark Inner Council (Order 0.70, Consequence style)

**Coordinates.** Duchy rung · office: **ambiguous, and the ambiguity is the finding.** `12 §3`'s
battle signature has `commander: person` as a *role in a contract*, not an office; `12 §1` says
outright *"there is no coercive apparatus. There are armed persons who are standing there and may or
may not do what they are told."* Nothing in `14 §1.5`'s post roster is a military command.

**Option set.** Give an `Order` — *"a dispensation addressed to named persons rather than a scope"*
(`12 §6.1`); choose a gambit if a battle exists (`12 §3.1`); `requisition`; `tell`; `carry`.

**The diagnostic.** His entire power is `Hold(n, targets, giver) = Σ reach(p) × will(p, …)`, and
`will()` reads `stance(p → giver)` — **the giver, not the office.** So if Inge orders, the willingness
is computed toward Inge; if Olaf orders, toward Olaf. His one accumulating asset is
`obeyed_claims(p, Olaf) ∈ −3..+3`, worth ±0.15, which builds and collapses through the claim ledger
and nowhere else (`12 §6.3`): *"one public refusal in front of sixty people lowers sixty people's
willingness on the next order."*

Canon gives Hafenmark **Military 3**, the lowest of the great factions. Under `13 §2` that is a
computed band, not a stored dial — an *output* of a duchy whose power_base is purchased and
bureaucratic. And `12 §1.2`'s `sever` term applies against his own city: a Hafenmark watch ordered
against Hafenmark communities loses `0.55 × 0.80 = 0.44` of every man's willingness.

**Verdict: THIN.** He has a real act — the `Order` — but every consequence of it is computed from
other people's stances toward him personally, he holds no remit that survives his own reputation, and
his single accumulating quantity is a ±0.15 term. The one thing that would make him distinct — a
standing command that binds — is the thing `12 §1` refuses on purpose.

### 3.3 Uta Falkenrath — Commune Representative, Banneret (*proposed*; Community 0.50, Precedent 0.30)

**Coordinates.** Duchy rung · office: none · canon arc: *"succession candidate if Baralta falls
(popular mandate)."*

**The finding.** `14 §10` refuses *"a legitimacy, authority, or mandate meter"* absolutely. So the
mechanism canon assigns her does not exist in this design, and what replaces it must be
`04 §8`'s `contest(container, prize, claimants)` with the ducal seat as prize:

```
capacity(f, container, prize) = Σ act_reach(p, container, prize) × degree(p, f)
act_reach(p, ·, office) = 1.0  if p holds a vote or seat under the container's rule
                          0.3  if p can carry a petition into it
                          0.1  otherwise
```

Commune members hold no seat at the Court Parliament (`14 §5`: ENTER seat-holders and attendants;
SPEAK seat-holders only), so they score **0.1 each** — ten to equal one seat-holder, against a prize
whose contest also multiplies by `(1 + 0.3 · leverage(hearth, seat))`, a term reading past placements
her hearth has none of.

**The design has no route from popular support to a heritable seat.** Arguably correct for a monarchy
— but Uta's stated arc is unreachable by arithmetic rather than by opposition.

**Verdict: BLOCKED on her stated arc; THIN otherwise.** She keeps one valuable act: `04 §5`'s norm
mechanism — *"they do not attack the norm, they change the membership, and the norm follows"* — and
`norm` enters `contest` as `score(f) = capacity × (1 + 0.5 · norm)`. She can move a multiplier she
cannot benefit from.

### 3.4 Björn Holdar — Senior Jarl of the Western Highlands, Varfell (Warden 0.70)

**Coordinates.** **Territory rung**, not Duchy · office: binds persons-by-presence · conferral basis
**disputed by §2.5's branch** — if heritable, no living conferrer and Vaynard cannot revoke him.

**Option set.** The full five-act remit at his own territory, subject to his own reach: `issue`,
`determine`, `confer`, `dispatch`, `convene`. Plus `carry` into Varfell's own standing dates, plus
refusal — and refusal is the interesting one, because a jarl Vaynard cannot revoke, refusing an order,
is `12 §6.2`'s **overt refusal in front of everyone**, which deposits `(order of Vaynard, was_obeyed,
false)` into every witness's ledger and lowers every subsequent order's willingness.

**Verdict: RICH — and identical in shape to Vaynard's own season at smaller scope.** That is the
lane's question answered inside a probe: a Senior Jarl's option set is a Duke's option set with a
smaller `scope_node` and a shorter establishment list. Note that `12 §1.2`'s
`conviction_weight(p, {Authority, Order, Duty-of-post})` reads nothing from Warden, so his primary
conviction buys him no willingness anywhere.

### 3.5 Ingrid Stenskald — Skald-Chief, Varfell Jarl Council (Community 0.70, Solidarity style)

**Coordinates.** Territory/Duchy rung · **office: none** · marks: Einhir-traditional, no house name.

**Option set.** `tell`, at high publicity. That is it, and it is more than it sounds.

`04 §5`: `norm(community, proposition) = Σ weight(p) · stance(p, proposition) / Σ weight(p)`, computed
on demand, *"and a player can move it one person at a time, by name, by Knot, at a market stall."*
`04 §8`: `score(f) = capacity(f) × (1 + 0.5 · norm(container, proposition(f)))`. A skald whose acts
carry at `venue_factor 1.0–1.5` across many communities is the design's only broad lever on `norm`,
and `norm` is worth up to **+50% capacity** in every contest at those containers.

What she cannot do: bind anyone, gate anything (what she moves is stances and estimates, and `01 §1.3`
is explicit that those gate no option), or reach anyone outside a telling chain.

**Verdict: RICH, slowly.** Pure Epistemic + Relational with zero Political-down, and the design pays
that mode properly through one multiplier. She is also the counter-example to the idea that office is
what matters at this rung: she holds none and moves the largest single coefficient in `contest`.

### 3.6 Njal Torberg — Military Jarl, Varfell (*proposed*; Identity 0.60, Honor 0.20)

Canon: *"Fights for Einhir, not Vaynard personally. Fracture line if Vaynard's ego diverges from the
cause."*

**The probe the roster asked for — alignment diverging from office — and the design answers it in one
line, then contradicts the character.** `12 §1.2`:

```
will = 0.30 + 0.08 × stance(p → giver) + 0.06 × stance(p → proposition)
     + 0.10 × conviction_weight(p, {Authority, Order, Duty-of-post}) + … 
```

Loyalty to the **person** is weighted 0.08 (range ±0.40); loyalty to the **cause** is weighted 0.06
(range ±0.30). **The formula says the man outweighs the cause by 4:3**, for a character whose entire
canon identity is the reverse. And the third term reads only Authority, Order and Duty-of-post — Njal's
convictions are Identity and Honor, so he draws **nothing** from it.

Worked: Vaynard's ego diverges. `stance(Njal → Vaynard)` falls to −3; `stance(Njal → the Einhir
proposition)` stays +5. Then `will = 0.30 − 0.24 + 0.30 + 0.00 = 0.36` — the **comply badly** band
(`12 §6.2`): *"the act performed slowly, partially, or at the wrong address."* Not the refusal his
canon promises; a shrug. Push the giver term one point further and he crosses 0.30 into refusal, at
which point `12 §6.2` gives him a choice between **overt** and **covert** refusal by his own exposure
calculus — and covert refusal (*agrees, does nothing*) is the one that matches "conditional loyalty to
the cause."

**Verdict: RICH, with a coefficient objection.** The mechanism reaches the character; the weighting
runs against him. Reported per §5's Finding 5 — this is not a bug to patch here, it is a claim about
human motivation encoded as two constants, and the setting has a named character who denies it.

### 3.7 Maret Uln — Varfell intelligence operative, TS ~50, Southern Einhir of the western fjords

**CANON'S PERSON, per FINDING 1.** Not the Goldenfurt kettlemaker the suite's traces use. This is the
most interesting cell in the lane and it deserves more than the others.

**Coordinates.** A · rung: **Community** (a western-fjord hamlet) by address, but operating across
Varfell as her patron's **establishment** — and those are different rungs, which is the point.
B · office: **none.** Being an intelligence operative is not a remit; it is being `dispatch`ed.
C · alignment: **two edges** — Vaynard's proposition at some degree, private; the Restoration
proposition at low degree, **covert** (`07 §1.3`). D · marks: Southern Einhir (caste-excluded),
Thread-sensitive at TS ~50, no house name, no guild grade, no Church standing.

**Four derivations, each of which changes what she is.**

1. **Her TS is what makes her covert alignment possible at all.** `07 §1.3`: *"a covert requisition
   needs a channel that deposits no claim into a judging set, and ordinary asking is witnessable. A
   **Knot** is not… A covert faction's capacity is therefore bounded by its members' Bonds."* And
   `01 §2`: Knots are TS-gated, so *"roughly half the peninsula cannot form one."* At TS ~50 she can.
   **The same mark that excludes her from every formal institution is the one that opens the only
   channel a covert commitment can run on.** The suite states this as the reason Niflhel recruits on
   the waterfront; it applies to her exactly and nobody wrote it for her.

2. **Her cover is a function of her marks, and it fails geographically.** `mark_salience` is near zero
   in the fjords and maximal in a Crown-Latinate quarter, so **she is operationally invisible where
   Vaynard needs no intelligence and maximally visible where he does** — a constraint on the whole
   Varfell intelligence apparatus, derived from one publicity formula.

3. **PP-486's succession fallback has exactly one mechanism, and performing it destroys her.** She is
   not Vaynard's kin. `14 §2`: a duchy's vacancy resolves by `04`'s succession pointer, a **hearth**
   field, and `04 §1.3`'s seat list is edited by four acts only — dowry, disinheritance,
   **legitimation**, contest. So a non-kin succession fallback is available through precisely one act:
   Vaynard `legitimate`s her into the Vaynard hearth's seat list (`04 §2.2`, *"inserts a person into
   the seat list at a declared degree; creates full same-hearth edges retroactively"*). And that act
   (a) is an **assertion**, forgeable and contestable; (b) is witnessed at `venue_factor` up to 2.0 if
   performed at a standing date; and (c) **adds the house name Vaynard to her marks**, which raises her
   `mark_salience` permanently and everywhere. **Vaynard cannot make Maret Uln his heir without ending
   her usefulness as an operative**, and the only way to have both is to legitimate her *secretly*,
   which `04 §2.2` says is exactly the shape a vacancy-window forgery takes. The design produced a
   genuine dilemma at this cell with no authoring.

4. **Her defining dual loyalty has no resolution she controls, and that is a weakness.** `07 §1.2`:
   requisition's obstacle carries `burden = cost to computed need + 2 × harm to the member's
   container's stake + 3 × marks the act collides with`, and — the load-bearing clause — *"refuse at
   low burden and the edge drops a degree; **refuse at high burden and it does not.**"* The Restoration
   proposition is *(Einhir communities govern themselves by consensus)*, which `14 §6` classes as
   *"shrink the denominator to nothing: dissolve offices with binding power."* Any Restoration
   requisition asking her to act against Varfell's intelligence apparatus carries maximal `harm to the
   container's stake`, so it fails **and costs her nothing.** She stays a covert member at her degree
   forever, and her canon arc — *"Dual loyalty — personal sympathy vs professional duty"* — resolves
   only through **somebody else's investigation** (`07 §1.3`). **Her agency in her own defining
   conflict is zero**, and it gets worse if she takes the duchy: she would then hold an office her own
   faction's proposition negates, protected from ever being asked to act on it by the same rule.

**Option set.** `tell` / `lie` / `conceal`; the investigation acts (`03 §6.1`) — and `03 §6.2` says
these are *"playable with no office"*, which is the whole of her job; `commit`; requisition along a
Knot; refuse; be dispatched; migrate.

**Verdict: RICH in the epistemic mode, BLOCKED on her own arc.** Three of the four derivations above
are the design working at its best. The fourth is a real hole: **a covert commitment held by a person
whose container's stake is large is permanently stable, because the burden term protects it — so
covert alignment near the top of the ladder has no failure mode except discovery by a third party.**

---

## 4. IS DUCHY SCALE GENUINELY DISTINCT FROM SETTLEMENT SCALE?

The lane's assigned question. The honest answer is **partly, and less than the design claims.**

`14 §3` sets the test itself: *"A rung is a role, not a class. So each rung above Settlement must own
a mechanism the rung below does not — otherwise it is a filing level and should be cut."* It then
awards Territory **reach** and Province/Duchy **delegation**.

**Delegation fails that test.** `14 §3.2` defines it as
`subremit(parent, acts' ⊆ acts, scope' ⊆ scope) -> a new Office whose conferrer is parent`. Now read
`14 §1.5`'s own post roster: a **gate warden** is an office at a settlement, binding persons by
presence, conferred by the **praefect**, with an establishment of two to five watchmen, revocable by
the praefect. That is a proper subset of the praefect's acts over a proper subset of his scope,
conferred by him, revocable by him. **It is a sub-remit, performed at Settlement, by the suite's own
table.** Province/Duchy does not own delegation; Settlement already runs it.

Strip that away and what is genuinely distinctive at Duchy scale is a short list:

| claimed distinction | verdict |
|---|---|
| a larger act vocabulary | **false.** `14 §8`'s table is explicit: the fisher and the Duke run the same acts. `05 §1.1` runs the same shortfall function on both and lands them on the *same number*, 0.47 |
| delegation / sub-remit | **false.** Runs at Settlement (above) |
| reach as a first-class problem | **TRUE, and it is the strongest one.** `14 §3.1`: past the establishment count, a node *is* a cohort row in the holder's ledger. A praefect standing in his own settlement never faces this. A duke's structural blindness is a mode of play that does not exist below him |
| all material acts are mediated | **TRUE.** A praefect allocates the granary himself (`13 §3`). A duke cannot; he can only issue a term that changes what the allocator does, or replace the allocator. Every material act at Duchy scale is therefore *also* an institutional or relational act |
| the office is attached to a hearth seat | **TRUE, and under-exploited.** `14 §3.2`: a Duchy's vacancy resolves by `04`'s succession pointer. So a duke's **family acts are office acts** — marriage, legitimation, disinheritance move the duchy. A praefect's marriage moves nothing |
| non-revocability | **TRUE, but negative.** A duchy is an office with no living conferrer. It is a real difference in *threat model* — a praefect plays against a revoker, a duke against a venue and a knife — and it changes which acts are rational, not which acts exist |

**So the reduction is: a Duchy is a Settlement office with (a) a coarse ledger, (b) mediated material
acts, (c) a hearth seat fused to it, and (d) no living conferrer.** Two of those four — the ledger and
the hearth fusion — are genuinely new modes of play. The other two are magnitude and absence.

**And the act budget decides whether even that is enough.** Under one act per season, a duke's season
is a choice among four move-shapes — issue a term, move a person into or out of an office, spend a
seat item at a venue, or edit the hearth's pointer — and both FULL seasons above pay the cost: Inge
legitimated an heir and therefore did not convene, issue or dispatch; Vaynard issued a reform and
therefore could not publish it with enforcement anywhere. That is a sharp game, and it is also close
to **THIN**: four shapes, one pick, two of them cosmetically different in most seasons. Under
`14 §8`'s ten acts a duke's season is plainly richer than a praefect's — and the reason would be *an
unstated scaling of the act budget by office*, contradicting `14`'s own founding claim that an office
*"adds no verb to the game"*.

**Stated plainly, as the brief asks:** Duchy-scale play is not Settlement-scale play with a larger
stake — it has two mechanisms of its own — but it is *closer to that* than the design's rung-ownership
argument claims, and the size of the gap between them is currently set by an unresolved contradiction
about how many acts a person gets in a season.

---

## 5. FINDINGS

Each is argued in full in the season it came out of; the citation is the argument.

**F1 — The act budget is contradicted between `09 §1.1` (one act per season) and `14 §8` (a ten-act
worked season for the same character), and `seat_items` has two owners (`14 §1.3` the holder's hours,
`05 §3.1` the container's capacity).** §0.2, §4. **This is the highest-value item here:** settle it and
this lane's central question has an answer; leave it and both answers are defensible from one suite.

**F2 — Two of the four computed needs have no formula, and they are the only two a magnate has.**
`01 §2` names subsistence, standing, commitment, exposure; `04` computes the first two; nothing
computes the last two. For a duke both computed needs return **0** (§1.2), so 100% of a magnate's
motivation comes from the uncomputed half — and `05 §1.1`'s own worked table hands Vaynard
`urgency 0.91` with nothing deriving it. The design computes a fisher's want exactly and must
hand-author a duke's.

**F3 — Inge Baralta's stated goal is unreachable and no act of hers touches the blocker.** Article 3
of a Crown Succession Contest needs consecration consent, an instrument in Church custody, which is
indeterminate at game start (FINDING 4) and therefore ungradable for every claimant (`08 §10.1`).
None of her eleven acts reaches the Church's conferral graph (§1.5). **The most interesting thing a
duke can do — put a person inside the Dicastery of Doctrine and Archives — is not a Duchy-rung act.**

**F4 — `14 §9` scores "hoard the deed presumption" wrongly for Baralta.** Canon
(`03_canonical_timeline.md:90`) and `14 §1.5` root the **Baralta ducal office** in the same
Secession-era deed with the same dead conferrer, so the numerator decays for her too. Waiting is a race
between two decays, not the free option the suite's R-check scores it as (§1.8).

**F5 — `12 §1.2` weights loyalty-to-person above loyalty-to-cause, 0.08 to 0.06, and a canon character
denies it.** Njal Torberg *"fights for Einhir, not Vaynard personally"*; the formula makes the man
worth 4:3 against the cause and gives an Identity/Honor character nothing from the conviction term.
The result is a shrug where canon promises a fracture (§3.6).

**F6 — Varfell is structurally not a duchy in the sense Hafenmark is, and no document says so.** If the
jarldoms are heritable deed-seats — which is what canon's *"Varfell retains territorial independence"*
says — Vaynard can neither `revoke`, `dispatch`, nor sub-remit over his own Jarl Council (§2.5), and
`14 §9`'s "maximum mitigation" answer for Varfell is unavailable over ground the jarls hold.

**F7 — A covert commitment held by a person with a large container stake is permanently stable.**
`07 §1.2`'s *"refuse at high burden and it does not [drop a degree]"* means Maret Uln's dual loyalty
can move only through a third party's investigation (§3.7.4). Covert alignment high on the ladder has
exactly one failure mode and its holder has no agency in it.

**F8 — There is no route from popular support to a heritable seat.** `04 §8` pays `act_reach` 1.0 for a
seat-holder and 0.1 for everyone else, and `14 §10` refuses a mandate meter — so Uta Falkenrath's canon
succession path is unreachable by arithmetic (§3.3). Defensible for a monarchy; it should be a stated
position rather than an emergent one, because canon has a named character whose arc depends on it.

**F9 — `04 §10`'s Trace A gives Inge a marriage-basis banked claim her canon facts forbid her to have
created.** Survivable by reading `04 §3.2` literally (claims are held at the *hearth*), which the suite
does not state. §0.3 — FINDING 1's shape at the level of mechanism.

**F10 — The conferral dilemma's consequence at this rung.** Person-rooted: a Crown succession leaves
every praefecture inside both duchies with a dead conferrer, irrevocable and unreplaceable.
Office-rooted: a Crown succession is simultaneously a contest for thirty-odd settlement offices *inside
two duchies whose dukes cannot touch them*. Reported per `00_PLAN §5`; not resolved.

---

## 6. CELLS POPULATED

| A · rung | E · mode | demonstrated by |
|---|---|---|
| Province/Duchy | **Institutional** | Baralta: `convene`, `confer` a sub-remit, `revoke` inside subtree, `legitimate`. Vaynard: `confer` on a Southern Einhir reeve |
| Province/Duchy | **Political-down** | Vaynard's `EntryStandardTerm` + `ExemptionTerm` over Varfell; his `BlockadeTerm` on the Grauwald coast |
| Province/Duchy | **Argument** | Baralta as convener and veto-holder at the Hafenmark Court Parliament; `CARRIED-WITHOUT-FORCE` |
| Province/Duchy | **Relational** | legitimation as a Duchy-rung act, because the ducal office is attached to a hearth seat |
| Province/Duchy | **Material (mediated)** | the silver mine's ore-grade fuse; the harbour's siltation; the dredging levy that was voted down |
| Province/Duchy | **Coercive** | levy apportionment by a named person at every rung; the levy that cannot be enforced by a levy |
| Territory | **Political-down / Institutional** | Björn Holdar — a Duke's option set at smaller scope |
| Territory→Community | **Epistemic** | Ingrid Stenskald moving `norm`, the largest coefficient in `contest`, holding no office |
| Community | **Epistemic (covert)** | Maret Uln: investigation acts playable with no office; a Knot as the only unwitnessable channel |
| Duchy · **no office** | **Argument / Institutional-adjacent** | Torvi Heljason: all standing is shadow, so the design ratchets her toward an office |
| **caste-excluded × Thread-sensitive × binds-persons-by-presence** | — | Vaynard — occupied by nobody else in the eighteen |
| **caste-excluded × TS × covert alignment × contingent claim on a duchy** | — | Maret Uln — the rarest cell in the roster |

---

## 7. CELLS I FOUND EMPTY

1. **Province/Duchy × Epistemic, as an act.** Ledger coarseness is the best idea at this rung
   (`14 §3.1`), and there is **no act that buys fidelity except `dispatch`** — which competes directly
   with enforcement for the same nine persons. No survey, no census, no correspondence net, no
   commissioned inquiry (`03 §8`'s correspondence filtering is written at household scale). The mode is
   live at the rung and has one verb.

2. **Province/Duchy × Political-up, laterally.** A duke petitions the Realm by spending a seat item,
   and that is all. There is no instrument by which one duke asks another for anything except a treaty
   (`06 §7`, two office-holders issuing jointly), so **duke-to-duke is a treaty or nothing.** Inge and
   Magnus are canon's *"total opposition"* foil pair and share no channel that is not a joint
   dispensation or a venue.

3. **Any act by which a duke reaches inside another faction's conferral graph.** F3's blocker. Not a
   Duchy-rung gap alone — it is the general shape: the conferral graph is a graph, and there is no
   `contest` over an edge of it short of a venue whose custody is the thing in dispute.

4. **`need(commitment)` and `need(exposure)` at any rung.** F2. Empty everywhere; **fatal only here**,
   because it is the only half a magnate has.

5. **A councillor's own standing date.** The Hafenmark Inner Council and the Varfell Jarl Council are
   named in canon and appear in **no venue table** — `14 §5` and `08 §10` between them list nine
   chambers and neither council is one. A council with no standing date has no prize, no judging-set
   rule and no decision rule, so under `04 §8` it cannot `contest` anything and under `08` it cannot
   argue. **The two most populous named bodies in this lane are not venues.** Every probe in §3 had to
   be written at a venue somebody else convenes.

6. **Non-revocable office-holder against non-revocable office-holder.** Vaynard versus his jarls (F6),
   Inge versus a legitimated cadet who will not stand down. `04 §1.3`'s third branch — *"held by
   whoever physically holds it, re-opens at every standing date"* — is named "open war" and then never
   given a resolution path short of `12`'s battle seam. Between "re-opens forever" and "battle" there
   is nothing, and that is precisely the register the setting says it lives in (`12 §4`).

7. **A Duchy-rung act that changes a person's `opening_set` without an establishment member to carry
   it.** `06 §8`'s reach cap plus one act per season means a duke's down-stroke reaches nine nodes at
   most and usually fewer; everything past that craters (`06 §3`). **The down-stroke's advertised reach
   and a Duchy's actual reach differ by a factor of the establishment size**, and nothing closes the gap
   except hiring people you must then keep paying (`07 §4`, the military basis).

---

*Written against the merged suite as authority on mechanism and canon as authority on persons. No
mechanism is proposed here; every gap above is reported as a gap. Two branches were assumed and
declared (§0.1, §0.2) rather than resolved. No character was rescued.*
