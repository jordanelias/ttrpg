# 06 — Seasons Without Office

## Status: FILED (2026-08-30) — a play-space probe. Nothing here ratifies on merge, and nothing here is design.
## Lane 5 · POWER WITHOUT OFFICE. One FULL season (Vossen), nine PROBE seasons.
## Authority: `proposals/2026-08-29-valoria-from-scratch/` on mechanism; `canon/` + `references/npc_registry.yaml` on people.
## Binding rulings (Jordan, 2026-08-30): Niflhel is not a faction. The Guilds are not one faction —
## "just a loose collective of economic factions," with no single leader because there is no single proposition.

---

## 0. What this lane owns, and the two things it is testing

Every other lane has a fallback. A duke who cannot argue can `issue`; a Cardinal who cannot persuade
can `revoke`; a praefect who cannot win a vote can drop the item. **Nobody in this document can do any
of that.** The design's central claim — *a faction is a proposition plus a commitment map, it has no
verbs of its own, and capacity routes through persons* — is either true here or it is a sentence.

Two structural probes, stated up front so the reader can check whether I answered them:

> **PROBE A.** Can several small, overlapping, uninstitutional factions be **expressed** and **act**,
> purely through the persons holding them? Annika Feldhaus and Frieda Kessler are the clean test:
> two guild figures, opposed propositions, no body above either, competing for the same stakes at the
> same standing dates.

> **PROBE B.** Are the Restoration's **presence markers** a genuine fork or a trap? The design's
> account is that `avow` raises every observer's *estimate* at a node without changing capacity by one
> point, at a real cost, with no un-avow.

Both are answered in §7 and §8, after the seasons that produce the evidence.

---

# PART I — THE FULL SEASON

## 1. Yrsa Vossen — Restoration Movement

### 1.1 Coordinates

| axis | value |
|---|---|
| **A · rung** | footprint is Realm-wide and upward-closed; **her own address is SILENT** — see §1.2 |
| **B · office** | **none**, and not even *binds-members-by-admission*. Her cell's decision rule is *no sustained objection* (`08 §10`), so her only binding power over the movement is a **veto**, which every other member also holds |
| **C · alignment** | d=5 **constitutive** toward *(Einhir communities, govern, themselves by consensus, all-time, **ought**)* · **avowed**, irreversibly |
| **D · marks** | cultural label `varfell_alpine` — **canon does not mark her Southern Einhir** · no guild grade, no Church standing, no house name · Thread sensitivity **contested: TS 25 (registry) or TS 0 (`npc_behavior_system_v1 §2.6`)** |

Two of those four cells are the season, so take them first.

### 1.2 Opening state — the six person fields, and what is conspicuously absent

**Address: null.** `npc_registry.yaml` gives Vossen `territory: null`, `birthplace: null`, `age: null`.
The substrate's own table (`01 §2`) opens with *Address — without it there is no rung, no
jurisdiction, no aggregation.* It is the first mandatory field, and the leader of one of the
peninsula's major factions does not have one.

This is not repairable by picking a village. Four things in the nine-part shape go undefined the
moment address is null:

1. `hears(p, act)`'s second clause — *shares the actor's community address* — has no set to range over,
   so **her judging set cannot be computed.** Every act she takes is read by her marks (`04 §4.1`),
   and there is nobody standing there to read them.
2. `standing(p, n)` is computed from a support set `S(p, n)` at a node (`07 §4`). No node, no `S`, no
   standing — and the **need** for standing reads *the world*, not her view (`01 §2`), so it is
   supposed to be the one need she cannot be wrong about.
3. Her larder. `mouths(h)`, `draw(h)`, `margin(h)` need a hearth. She has none in canon.
4. `carry(c, P)`'s precondition — *c holds standing at the respondent container* — is unevaluable.

I may not invent biography, so I write the season on what survives: the acts whose legality is a
**person-read** rather than an address-read — `tell`, `avow`, `commit`, `requisition`, `back` and the
veto. Not nothing, and §1.5 shows it is not much.

**Marks.** She is `varfell_alpine`, **not** Southern Einhir. `04 §6` sets the Restoration cell's
admission gate at **α = 0.0** — the only gate in the peninsula that does not read heritage — so she is
admitted to her own movement on a coefficient that ignores the mark she lacks. That is an unremarked
advantage and the beginning of §8's asymmetry.

**Thread sensitivity — both branches, because the season changes.** The registry says TS 25 with the
note *above practitioner threshold, below the Forgetting resistance gate*. `npc_behavior_system_v1 §2.6`
says **TS 0, Non-practitioner**. I do not resolve it. What matters is that **both branches fail the
same gate**, and it is the most consequential gate in this document:

> `02 §4.2`: a Knot requires **TS ≥ 30 on both sides**. `form_knot` needs Disposition +5, TS ≥ 30 both,
> Bonds ≥ 5, a free slot.

25 < 30. 0 < 30. **Yrsa Vossen can never hold a Knot, on either branch of the contradiction.** And
canon corroborates it from a second direction: Community Weaving "requires a practitioner TS 30+
affiliated" (`insurgency_pipeline_v30`, `conviction_track_v30 §5.3`), and `worldbuilding_v30 §8`
states outright that Elder Kaldring at TS 22 *cannot anchor Community Weaving*.

### 1.3 FINDING 1 — the design's stated reason the Restoration works does not reach its leader

`01 §2` says of Knots: *"the deepest informal channel, being TS-gated, gates them IN… why the
Restoration's weaving works with no wealth and no soldiers."* `07 §1.3` says a covert requisition needs
a channel that deposits no claim into a judging set, ordinary asking is witnessable, so *"a covert cell
recruits and requisitions along Knots… **A covert faction's capacity is therefore bounded by its
members' Bonds.**"*

Put those together with the gate. **The Restoration's covert operating capacity runs entirely through
its Southern Einhir members — who carry the higher TS baseline — and structurally excludes Yrsa Vossen
and Aldric Hann, both below 30.** The movement's two named visible leaders are the two people in it who
cannot use the channel the design says the movement runs on.

**This is not a defect.** It is the sharpest available demonstration that capacity routes through
persons rather than leadership, and it produces canon's own claim — *"visibility as vulnerability… she
cannot lead from hiding"* (`npc_roster_v30 §3`) — with no authoring, because she is mechanically
incapable of the covert channel and has only the open one. But it has a consequence nobody has written
down: **every account of a Restoration act that runs through Vossen personally is wrong.** She does not
run cells and cannot requisition covertly.

### 1.4 Computed needs, with the arithmetic

Four need kinds (`01 §2`), two reading the world and two reading her view.

| need | reads | value |
|---|---|---|
| **subsistence** | the world | **UNCOMPUTABLE** — no hearth, no larder (§1.2) |
| **standing** | the world | **UNCOMPUTABLE** — no container, no siblings, no `S(p,n)` |
| **commitment** | **her view** | dominant, and computed below |
| **exposure** | **her view** | live: she holds claims about Church Attention toward her |

Two of her four needs are undefined, and the two that survive both read her **view**. The leader of a
peninsula-wide movement wants exactly what her twelve most salient claims tell her to want.

**The commitment need.** `shortfall = urgency − reach` (`05 §1.1`). Her proposition decomposes, per
`14 §6`, into the only operation on the sovereignty fraction available to a faction with no Mandate,
wealth or soldiers: **shrink the denominator; dissolve offices with binding power so that no root can
hold them.** `reach` is the best act on her own menu, and that menu is seven verbs, none of which
dissolves an office. **Shortfall is near-maximal and permanently open** — the same permanently-hot
condition `05 §1.1` finds in cadet branches, reached from the opposite end of the ladder.

**And one emergent consequence.** View assembly ranks the top K = 12 claims by `recency × confidence
× relevance × stance weight` (`01 §3.1`), and stance weight is the motivated-reasoning term. Her stance
toward her own proposition is maximal by definition. So the claims that surface for her, every season,
are systematically those arguing *for* the proposition and *against* the containers refusing it.
**The design's own T3 multiplication makes a movement leader more radical than her information
warrants, with no radicalisation mechanic, and it does so harder the more committed she is.**

### 1.5 The view, the option set, and the claim that does not surface

**Her working set.** Twelve claims: tellings from cell members about refusals at territory courts, one
about a Church visitation, her own memory of a sitting.

**The claim that does not surface.** She holds, from Hann, *(cell at Stillhelm, is-compromised, an
informer among them, this season, told_by(Hann), confidence 0.55)*. Its stance weight is negative
against her proposition, so `03 §10`'s disclosure panel renders it exactly as designed — *greyed out,
"you know this and you are not thinking about it."* That panel makes her signature failure legible
without a trait, and it is the best thing in the suite for a character of this shape.

**THE OPTION SET**, exhaustive rather than illustrative — every act available to her, and why legal.

| # | act | legality | what it costs |
|---|---|---|---|
| 1 | **`tell(prop)`** — assert the proposition to a hearer | universally legal; `01 §3.3` — telling is an act, available to any person | one act; deposits `SAID` naming her, forever |
| 2 | **`avow`** — convert a covert edge to avowed, hers or by inspiring another's | `07 §1.3`; the presence marker | §8. Irreversible |
| 3 | **`commit(person, f, Δ)`** — her own degree; already 5 | `01 §1.4`; one operation, both directions | nothing at 5 |
| 4 | **`requisition(her, member, act, node)`** — ask a d≥3 member to act | `07 §1.2`; the *only* channel from a faction to an act | obstacle rises with the member's burden; **open channel only — no Knot** (§1.3) |
| 5 | **`back(P, mode)`** — lend her stance to someone else's petition | `05 §2.1`; needs a claim that P exists and a positive stance | public backing deposits into every judging set she is in |
| 6 | **`admit`** into a cell | `04 §4.2`, `04 §6`: α=0.0, δ=2.0, **unanimity, any member may block** | she is one voice of many |
| 7 | **the veto** | `08 §10`: *no sustained objection* | free, and symmetric — everyone has it |

Seven verbs, against the ten in `14 §8`'s office-holder table. **The five missing are `issue`,
`determine`, `convene`, `confer` and `drop` — every one an office verb, and exactly the five the design
says office adds.** Claim tested; claim held.

**Four things she cannot do that are not about office**, which is where the gaps are:

- **She cannot `carry`.** `05 §3.1` requires standing at the respondent container — a seat, an office,
  a right of audience, or membership in its judging set. She holds none anywhere. Her proposition
  enters a container only through someone else.
- **She cannot `remonstrate`.** `05 §6.1` requires standing at an institution with a registered right
  of remonstrance: the Hafenmark Parliament, a guild's Free Masters in assembly, a Dicastery, a duchy's
  court. She has standing at none. **She is confined to supplication for life** — able to beg for
  grace, structurally unable to contest a measure. The document names this as the caste consequence
  produced by one precondition and no caste rule. It applies to a faction leader.
- **She cannot Thread-Read.** Pool is `⌊TS/10⌋ + Attunement` (`03 §6.1`). At TS 25 that is 2 dice plus
  Attunement; at TS 0 it is Attunement alone. Under the registry branch she is a weak practitioner;
  under the behavior branch she is not one. Neither branch reaches the Weaving gate.
- **She cannot set a deadline.** This is §1.6.

### 1.6 FINDING 2 — a faction cannot hold a standing date, so its leader can never start a clock

`01 §5.3`: *"**Containers** carry standing dates… A standing date makes a proposition contestable,
because petitions and dispensations addressing the same proposition before the same date are in conflict
and both sides know when the argument ends."* A faction is not a container, and `05 §3.1` makes the
agenda-setter an **office** — `convener(container)` is *the office named by the container's charter as
holding `compose_agenda`*. A Restoration cell has no charter and no office, by ideology.

**So the whole class of politics that exists because two sides know when the argument ends is
unreachable from inside this lane.** Vossen's proposition can only be contested at somebody else's date,
in somebody else's venue, entered by somebody else's carrier, ordered by somebody else's convener. She
cannot force a reckoning; she can only wait for one and hope to be on the list.

There is an internal collision in the suite here, and I report it without resolving it. `04 §7`'s
community roster lists **Restoration consensus cells** as a community with standing dates *"whenever
the cell agrees to meet"* — a schedule with no scheduler — and `08 §10` lists the cell as a **venue**,
which by `14 §5`'s tuple requires a convener. But `01 §4` rules that *a cell people belong to while
living elsewhere is a faction*, and Greta Saatfeld's cell is drawn from several hamlets. It cannot be
both. The three documents disagree, and the disagreement decides whether the Restoation can hold a
date at all.

### 1.7 The choice, through the seven phases

She takes **act 1**: `tell` the proposition, at a market, openly. Trace it.

- **P0** — no date of hers fires (§1.6). **P1** — her larder is uncomputable; nothing moves.
  **P2** — commitment need near-maximal, from her view. **P3** — twelve claims; the Stillhelm warning
  is not among them. **P4** — `choose(person, view) → tell`; she does not see the informer.
- **P5 RESOLVE.** Social acts resolve **last** (`09 §1.4`), so a season's talk is about that season's
  deeds. `publicity = venue_factor × √(witness_count) × mark_salience`: market 1.0 × √40 ≈ 6.3 ×
  `mark_salience` ≈ 1.4 ≈ **8.8**, far past the ≥ 1.5 band — settlement-wide, and along every Knot
  immediately. *Other people's* Knots, never hers.
- **P6 WITNESS.** Divergent deposit (`01 §3.3`): *she named what was done to us* in a hamlet ledger,
  *open heresy in the market* in a Church informer's. One act, two predicates. **P7** — decay, eviction.

**What propagates.** Up-stroke: nothing — she carried nothing, because she cannot carry. Down-stroke:
nothing — she issued nothing, because she has no remit. **Neither stroke.** What propagates is the
third thing, and it is the only transport she has: a *proposition travelling as a claim*.

`05 §5.1` is explicit that this suffices: *"A proposition is a claim, and claims travel by telling
independently of any member travelling. A hamlet with no cell, holding Yrsa Vossen's proposition at
confidence 0.4 plus a fresh grievance whose referent that proposition addresses, produces commits."*
Her act does not reach a container. It reaches **ledgers**, and where a dormant grievance row's re-arm
predicate matches (`05 §8.1`), it converts stance into commitment somewhere she has never been.

### 1.8 The diagnostic

> **VERDICT: THIN — and it is thin in a specific, reportable way rather than a vague one.**

Not SPECTATOR. She has seven legal acts, one of them (`tell`) with genuine peninsula-scale consequence,
and the design gives a real account of how a person with nothing moves a world. `07 §8` names her to
make the point: a leader contributes three things, none a modifier — her eligibility makes acts *exist*
where she stands; a contest through her draws its pool from *her* capability; her regard lowers her
members' requisition obstacles. All three are live.

But run the **R-check** — does any option dominate by shape of gain against shape of cost?

| option | gain shape | cost shape |
|---|---|---|
| `tell` the proposition publicly | **compounds**: each telling seeds commits at nodes she never visits; refusals elsewhere raise `G`, the grievance-capital term (`05 §9(b)`), which does not decay | flat and small: one act, plus Church Attention that only converts to harm if somebody spends investigation acts (`03 §7`) |
| `requisition` a member | one act at one node | obstacle + the member's burden, and every ask she loses drops an edge |
| `back` someone's petition | conditional on a carrier existing | judging-set deposits |
| `admit` | one member | one voice among unanimity |
| `avow` / inspire avowal | §8 | §8 |

**`tell` dominates, because the alternatives are gated on things she does not have.** Gain compounds;
cost is flat; and there is no counterweight in her column the way `05 §9(d)` supplies one for a dropping
carrier (a perpetual dropper loses his seat — she has no seat to lose). The design's own dominance-
breaker for repeated asking, *refusal produces an asset*, raises the value of her preferred act rather
than lowering it.

Her season is: **speak, and hope.** A coherent and even a moving game, and the right game for Rosa
Luxemburg. It is one option deep. **THIN by the plan's own definition.**

**Three empty cells this season proves rather than asserts**, none of which any other lane will hit,
because everyone else has a post to fall back on:

- **no address** → four of nine season sections undefined (§1.2);
- **no standing date** → she can never start a clock (§1.6);
- **no Knot, ever** → the movement's own covert channel excludes its leader (§1.3).

### 1.9 Cells populated

`Epistemic × Realm` (proposition-telling with no carrier) · `Relational × Community` (admit, at α=0.0) ·
`Relational × Individual` (commit at d=5) · `Argument × —` **attempted and BLOCKED**: no venue admits her
to speak. `Political-up` reached **only as backing**, never as carriage. `Political-down`,
`Institutional`, `Coercive`, `Material`: **empty, structurally**.

---

# PART II — THE RESTORATION PROBES

## 2. Aldric Hann — RM visible leadership

**Coordinates.** A: Community/Settlement, street-level. B: none. C: d=5, avowed (canon puts him in
*visible* leadership). D: TS **0**, non-practitioner; lower Charisma than Vossen, higher Circles in
logistics and street networks.

**A correction to my own brief.** I was told all his canon fields are null. **They are not.** The
*registry* row is; `npc_behavior_system_v1 §2.7` gives him Equity/Autonomy, Consequence then Evidence
styles, TS 0, Truth 3, and two beliefs: *"The movement needs infrastructure, not speeches — I will build
what Yrsa inspires"* and *"Every cell that is compromised is a community that suffers."* The registry's
own issue log records the resolution at item 12 and even *it* disagrees with the behavior file on his
secondary. **A registry-propagation hole, not a canon hole.**

**Derived proposition.** Under `07 §1.1` identity *is* the proposition, so a different proposition is a
different faction. Vossen's is *(Einhir communities, govern, themselves by consensus, ought)*; Hann's is
operational — *(the movement's cells, remain, uncompromised, ought)*. **Hann therefore leads a second
faction with heavy membership overlap**, which `07 §10.1 S15` handles directly: two propositions not
jointly unsatisfiable, so both may requisition the same persons.

**And then they are opposed over one act.** Presence markers are `avow`, and avowal is irreversible.
Under Hann's proposition **every avowal is a compromise** — an avowed member can no longer be asked to
act covertly (`07 §1.3`) and his cell's security falls. Under Vossen's, avowal is the movement's only
growth instrument. **Jointly unsatisfiable over one stake — whether a given member avows.** Two
overlapping factions, no institution above either, incompatible over one act. **That is the
Feldhaus/Kessler probe running again inside the Restoration, and it was not authored:** it falls out of
two sentences of canon belief text passed through `07 §1.1`.

**Act menu.** `interview` (his logistics Circles *are* `03 §6.1`'s interview graph), `surveil`, `plant`,
`reconstruct` (the only act that finds *who* lied rather than *that* someone did), `requisition`,
`commit`, `tell`. He **cannot** hold a Knot (TS 0), so his counter-intelligence runs on witnessable
channels — precisely the exposure his own proposition is about.

> **VERDICT: RICH.** Four investigative acts with four different shapes of gain against cost
> (`03 §6.2`'s R-check applies unmodified), a live opposition to his own leader that the design
> generates rather than scripts, and a real irony the mechanism produces on its own: **the man whose
> proposition is cell security is barred from the only unwitnessable channel in the game.**
>
> That his season is richer than his leader's is itself a finding.

**Cells populated.** `Epistemic × Community`, `Epistemic × Settlement`, `Relational × Individual`,
`Political-up` as backing only.

---

## 3. Uwe Askeland — Buditel, hedge-school teacher (proposed)

**Coordinates.** A: Hearth / Community, southwest. B: none. C: RM, degree ≥ 2, **covert**. D: Community
0.50 / Equity 0.30, Solidarity; caste position unstated.

**What he probes: epistemic play as resistance.** The design handles it better than anything else in
this lane, with zero new mechanism.

`07 §7` derives the Church's unintended suppression of Thread sensitivity entirely from `tell`.
Catechesis deposits a general explanation into children with **high credulity and high regard**, so it
lands *early*, at *high confidence*, and it is **general** — one explanation pre-resolves an unbounded
family of anomalies *in advance*, so `ts_gain` never accumulates. `03 §9` supplies the second half:
`admitting_share` is the share of a witness's Convictions whose construal sets admit a rendering-side
reading, and catechesis concentrates Conviction in rendering-blind construals.

**Askeland is the identical call with the sign flipped.** An Einhir general explanation whose construal
set *admits* rendering-side readings raises `admitting_share` in the same children the parish would have
narrowed, and leaves anomalies unresolved so they feed `ts_gain`. The measurable output is **higher TS
emergence in the southwest a generation later** — exactly the geography canon asserts. Nobody wrote
"education is resistance"; it is one construal set against another in one formula.

**His safety is structural, not lucky.** `publicity = venue_factor × √n × mark_salience`, and a private
dwelling is **0.2**: nine children in a kitchen ≈ 0.2 × 3 × 1.2 ≈ **0.7**, the band that reaches the
community and no further. And `03 §7` makes discovery proportional to a rival's **actual investigation
spend**, with exposure rising only on extraction. **The hedge school is safe until a named person
spends acts on it** — which is what a Field Inquisitor is for.

**THE GAP, and it is a real one.** `09 §1.1`: *every person commits exactly one act per season.* And
`tell(speaker, hearer, claim, as_asserted)` names **one hearer**. So either:

- (a) `tell` may take a **cohort** as hearer — in which case Askeland teaches a hamlet in a season, and
  the suppression-inversion above operates at real scale; or
- (b) it may not — in which case **a teacher cannot teach a class**, his lifetime reach is one hearer
  per season, and twenty years of hedge-schooling is eighty children, peninsula-wide.

`09 §1.2` P3 gives cohorts their own K=3 view "from the channel claims at its address," which implies
claims *can* deposit into a cohort. But nothing states that `tell` accepts one, and the difference is
two orders of magnitude in the only faction-growth channel the Restoration has. **The suite is silent.
I report it as an empty cell rather than filling it.**

> **VERDICT: RICH — conditional on the cohort question.** Under reading (a), the best cell in my lane:
> a person with no office, no coin and no post running the Church's own suppression mechanism backwards
> and changing a province's Thread demography. Under reading (b), **THIN**, because one hearer a season
> cannot move anything and his season becomes a nice scene with no consequence.

**Cells populated.** `Epistemic × Hearth` (the only entry in that cell across this lane),
`Epistemic × Community`, `Relational × Hearth`.

---

## 4. Carin Vedel — copyist of suppressed Einhir texts (proposed)

**Coordinates.** A: Individual / Community. B: none. C: RM, covert. D: Liberty 0.60 / Equity 0.20,
Evidence style. Canon: *"each copy takes weeks, possession is a heresy charge, no press to seize."*

**What she probes: the instrument — a written claim has a physical carrier and a place, survives its
writer, and is found by a search act.** Four results, three good and one empty.

**(1) Her copies are worth one proof grade less than the Church's, and nobody wrote that rule.**
`08 §4.1`: **G4 Instrument** requires a claim rooted `firsthand(read_of(object))` *where the object is
held in a **declared custody***. A hidden copy has none, so reading it deposits an ordinary firsthand
claim → **G2**; two independently-rooted copies → **G3**. That is the ceiling. Meanwhile the Dicastery
of Doctrine and Archives holds custody of the instruments everyone else's G4 grounds rest on.
**Suppressing a text and devaluing a text are the same operation** — take away its custody and its grade
falls one rung, permanently, in every chamber.

**(2) Her life's work is unreadable in principle by half her audience.** `03 §9`, P-08: a rendering-side
claim's subject is a *configuration*, a referent class a non-sensitive's ledger **has no address for**,
and degradation is a property of **deposit** on *every* path — the document says so about hers exactly:
*"give him the sensitive's own written testimony, in the sensitive's own hand, and nothing changes…
The document is intact; the reader is not equipped to hold what it says."* She is copying, at weeks per
copy, under a heresy charge, a thing most of the peninsula cannot receive. **The setting's central
tragedy, delivered by a type conversion.**

**(3) She is discovered by an act, never by a clock.** A book is a high-retention facet at a place
(`03 §6`). `examine` finds it; `research` cannot, because research is gated by an admission act and her
copies are the peninsula's one archive with **no admission gate** — which is precisely the operation
`14 §6` names as the Restoration's victory condition, shrinking the denominator of institutional
control.

**(4) THE EMPTY CELL — what a root token resolves to after its person is gone.** `01 §2`: *"a person
persists exactly as long as somebody remembers them"*, and one with no Knot, office, live petition or
ledger entry naming them re-merges into a cohort. Vedel is covert by design; being named is the thing
she avoids. But her copies carry **root tokens minted by her copying act**, and `01 §3.3` rules that
corroboration fails closed — *no null source, no untraceable claim*. So `reconstruct` on a copy fifty
years on must resolve a root to a person the world has reabsorbed, and **the suite never says what that
returns.** A small hole with a sharp point: it decides whether a martyr can be found by investigation
after she is forgotten, which is the whole dramatic proposition of a Lollard copyist.

> **VERDICT: RICH.** Three live acts (copy, place, conceal), each with a different shape of cost; a
> proof-grade consequence produced by the absence of custody rather than by a rule; and a P-08
> interaction that gives the character her tragedy for free. One genuine empty cell.

**Cells populated.** `Epistemic × Individual`, `Epistemic × Community`, `Material × Individual` (the
copies are objects with a place and a retention).

---

## 5. Greta Saatfeld — RM cell elder, Goldenfurt, posing as a farm-widow

**Coordinates.** A: Community (an Einhir hamlet) — but see the address collision below. B: none; her
cell binds by unanimity, so again only a veto. C: d≥4, **covert**, with a **cover claim** (`07 §1.3`:
covert members may `tell` an assertion of a different edge or of none — *farm-widow* is that telling,
performed, rollable, catchable). D: Einhir heritage (canon), β-conduct, TS unstated.

**An address collision I report rather than resolve.** Canon sites Goldenfurt in **Kronmark province,
Valorsmark/Crown duchy, Provincial Authority = the Crown** (`goldenfurt_slice/npc_cast.md`,
`valoria_geography_v30.yaml` S-006, *"tolled river-ford town; Guild toll dispute is the settlement's
defining tension"*). The merged suite consistently sites Goldenfurt in **Grauwald territory, Varfell,
under Duke Vaynard**. Under my binding, canon owns places, so Saatfeld's respondent container is a
Crown praefecture and her duke is not Vaynard. Every trace in the suite that routes a Goldenfurt
grievance to Vaynard resolves to a different person under canon.

**What she probes: covert alignment at community scale, and the presence marker.** Her canon ambition
is *grow RM Presence to three Kronmark settlements*, which maps onto commits at three nodes.

**FINDING — canon's cell-resilience rule is forbidden by the suite, and the suite reproduces its effect
anyway.** `settlement_layer_v30 §577`: *"If RM has Presence markers in ≥ 3 settlements within a
province, Church/Crown suppression actions against RM in that province take +1 Ob."* That reads a
**density** and modifies an **obstacle**. `07 §3` forbids it in terms: *"Nothing that decides an outcome
reads either profile… Size buys being noticed."*

The suite's substitute is available and better. Suppression is `Force(…, disperse, warrant=office)`
(`12 §4`) and it *requires Hold*, where `hold(n, tgt) = Σ martial × readiness × compliance` and
compliance is **the output of a decision, not a stat** (`05 §5.2`). A cell spread over three settlements
presents **three separate existentials**: at each node the suppressor needs a person with a binding post
*there* who will comply against *those* neighbours. `07 §10.2` runs exactly this case and finds capacity
**zero** for a faction of three thousand in a three-street district; marching a Templar in from two rungs
up *"converts a police matter into a caste incident."*

**Distributed cells are harder to suppress, exactly as canon says, computed from persons rather than
from a marker count.** Canon's +1 Ob is a summary of the mechanism, not the mechanism — worth saying,
because it is the kind of rule a port would transcribe.

**Her fork this season.** Canon has her escalate on *neglect*, not only on force: blocked without force,
she shifts to deeper-covert cell-export — `commit` chains along channels depositing no claim into a
judging set, i.e. **Knots**, which her Einhir heritage makes available to her and not to Vossen (§1.3).
Her cover claim's risk is `interview`, which *"deposits INTENDS(you, investigate X)"* in the hearer's
ledger, tellable onward — so Curate Wessel questioning her neighbours is itself an event her cell can
witness.

> **VERDICT: RICH.** Five distinguishable acts (commit, export, cover-tell, shelter, block-by-veto),
> a genuine two-sided exposure fork under `03 §7`'s paired counters, and a real relationship between
> her heritage mark and her operational reach.

**Cells populated.** `Relational × Community`, `Epistemic × Community` (concealment and cover-telling),
`Material × Hearth` (the farm is her cover and her larder), `Coercive × —` **empty by her own β conduct
and by the design's `will()` gate**.

---

# PART III — THE ECONOMIC FACTIONS

## 6. Five persons, at least four propositions, and no body above any of them

Written as Jordan ruled them: **not one faction.** Canon supports it from three directions —
`faction_state_authoring_v30` enumerates six canonical factions and the Guilds are **not among them**;
`factions_personal_v30 §280` describes a *rotating* Guildmaster Council with no single leader;
`faction_politics_v30 §546` calls the guild layer *dual-parented*. What canon actually holds is a **set
of overlapping propositions held by named merchants** — which is what `07 §1.1` says a faction is.

### 6.1 Annika Feldhaus — the Artisans' Compact

**Coordinates.** A: Settlement/Territory, `hafenmark_procedural`. B: **binds members-by-admission** —
the Compact's own admissions, and nothing beyond. C: d=5 to her own proposition; avowed. D: guild
grade, Utility 0.50 / Community 0.10, self-other **+0.10**, **TS 0**.

**Proposition.** *(the Compact's members, are-secured-by, maximum revenue, all-time, **ought**)*.

**Power base** (`07 §4`), and the point of naming it is that each basis names a different cut:
**purchased** ~0.4 (transferable instruments — the Compact's contracts), **bureaucratic** ~0.3
(everything routes through her), **merit** ~0.3 (guild grade). Three bases → `cuts_available = 3`, and
by `07 §4.2` a challenger needs a coalition landing ⌈k⌉ cuts in one standing-date window. She is not
single-handedly removable, and consolidation made her *more* vulnerable, not less — which is the
property the design says is not a balance patch.

**The BLOCKED sub-cell, and it governs her canon arc.** Her supply chain includes Thread-touched goods
through the Virke network; she has TS 0 and *"no conceptual framework for Thread metaphysics"*; the
authored arc is that a PC diagnoses the merchandise and reveals it.

Under `03 §9`, **that revelation cannot be delivered to her by telling, reading, inference or witness.**
It degrades on *every* deposit path into the nearest referent she holds: *(the goods, condition, wrong)*
at confidence 0.2. Raise her Focus, literacy, archive access and patronage to the ceiling and nothing
changes. So the design **converts canon's revelation scene into a fact she can only learn materially** —
revenue falling, households sickening, a Dicastery inquest into her ledgers. A better story, and a
change canon has to accept. **Report it; do not patch it.**

> **VERDICT: RICH, with one genuinely BLOCKED channel.** She has material acts at three rungs, a
> three-basis position with three named cuts, and an arc whose trigger the epistemics forbid — which
> is the design working, loudly.

### 6.2 Frieda Kessler — Zunftmeisterin, in opposition

**Coordinates.** A: Community/Settlement. B: **binds members-by-admission**, her own Zunft. C: d=5;
avowed. D: guild grade — and therefore, crucially, **standing at an institution with a registered right
of remonstrance**. Community **0.70**, Solidarity.

**Proposition.** *(the guild's mandate, outranks, the guild's revenue, all-time, **ought**)*.
Canon: *"Internal opposition to Feldhaus. Pushes Mandate over Wealth."*

**Power base: ideological, mass ≈ 1.0.** By `07 §4` that means **exactly one cut** — a hypocrisy, a
witnessed act by her contradicting the proposition, deposited into her supporters' ledgers, firing on
everyone holding that Conviction *simultaneously* and irreversibly. Hardest to obtain, cheapest to
fire.

**Which makes Kessler and Vossen the same object.** `07 §6`'s own table gives the Restoration
`ideological 1.0` and *"its cut: a hypocrisy — and nothing else, holding neither coin nor swords."*
A Zunftmeisterin in a Hafenmark guild hall and a peninsula-wide movement leader have **identical
vulnerability topology**. That is the design's central claim — two brothers and a national church are
one object — demonstrated in a cell nobody built it for.

**And the difference that matters.** `05 §6.1` lists *a guild's Free Masters in assembly* among the
institutions with a registered right of remonstrance. **Kessler may remonstrate. Vossen may not.**
Same power base, same cut, same conviction weight — and one of them can contest a measure while the
other can only beg for grace. The whole caste consequence, visible inside one lane, produced by one
precondition.

> **VERDICT: RICH.** She holds the contesting instrument, the carrying instrument (`carry` at her own
> assembly), the admission instrument, and the one-cut vulnerability that makes her interesting to
> attack.

### 6.3 Nessa Grindvold — guild advocate at the Crown court

**Coordinates.** A: Realm, by attendance only. B: none. C: guild-aligned, avowed. D: Liberty 0.50 /
Scholastic 0.30, Evidence style; `hafenmark_procedural`.

**The finding is a door.** `14 §5`'s venue table, the last row: **the Crown's council** — convener King
Almud; **ENTER**: those the King summons; **SPEAK**: those the King names; **DECIDE**: the King
determines; **admissible source**: *whatever he will hear*. Every gate is one man's discretion.

And `05 §6.1`'s list of institutions carrying a **registered right of remonstrance** — Hafenmark
Parliament, a guild's Free Masters in assembly, a Dicastery, a duchy's court — **does not include the
Crown's council.**

> **So the venue Grindvold is defined by admits no remonstrance, and she has no right of audience in
> it.** She is confined to supplication, which `05 §6.1` says *presupposes the giver's right to give* —
> an act of submission, read as such — for a woman whose brief is defending guild autonomy *against*
> Crown regulation. She must perform deference to contest deference.

Not a gap: `14 §6`'s Crown made concrete, weak everywhere it must ask and procedurally absolute in the
one room it owns. **Her live move is the venue objection** — `08 §2` rung 4, *this chamber may not hear
it*, which concedes substance to buy a delay. Forum-shopping is first-class: she holds standing at the
Free Masters' assembly and, through the Compact's seats, reach into Hafenmark's Parliament, whose
decision rule is a majority of seats the Crown holds none of.

> **VERDICT: RICH by re-venuing; BLOCKED at the venue that names her.** The design supports the escape
> explicitly, which is the strongest thing I can say about it. The reportable item is that a canon role
> titled *legal representative at Crown court* describes a post with no procedural standing.

### 6.4 Joren Bergvall — guild surveyor

**Coordinates.** A: Territory / Off-board (at sea). B: none. C: guild-aligned. D: Scholastic 0.60 /
Utility 0.20, Evidence.

**Canon:** *"Has data proving the southern sea route is physically blocked, not politically. Undermines
the Varfell conspiracy narrative. Fra Mauro archetype."* An investigation with an economic payoff.

**His grade ceiling, computed.** His survey is `examine(place)` → `firsthand` facets → **G2**. Two
independently-rooted surveys → **G3**. **G4 requires a declared custody** (`08 §4.1`), and the only
custodies in the venue table are the Church's registers, the praefect's roll, and the **guild
register** — which is the one he can reach, and which is held by a warden (§6.6).

**And the sharp result: he cannot refute the rumour in a chamber.** What he disproves is a *conspiracy
narrative* — **G0 common voice**, synthetic-root, which `08 §4.1` calls *"below most floors… nothing
needs to attack it."* There is no venue at which a G0 proposition is the motion.

> **A rumour cannot be defeated in a room. It can only be out-graded somewhere else.**

Correct rather than a hole, with a cost worth saying: the narrative goes on operating in **judging
sets** — where decisions are actually made — while his G3 sits in a register nobody reads.

**The economic payoff needs no office.** `13 §4`'s `import_flow` is the sum of individual acts, each a
person running `EV = (price(dest) − price(origin) − transport_cost) × volume − p(interception) ×
penalty`. If the route is *physically* blocked, `transport_cost` is effectively infinite and every act
premised on opening it politically has an EV computed from a false claim. **Bergvall's survey, told into
the right ledgers, changes the expected value of a whole class of acts for everyone who believes him** —
capacity with no coin, post or seat, delivered by depositing a better-rooted claim.

> **VERDICT: RICH.** Four investigative acts with genuinely different cost shapes, a real economic
> consequence carried by a claim, and one honest structural limit (G0 is unattackable) that the design
> names itself.

### 6.5 Orsk Tallow — Goldenfurt grainmaster

**Coordinates.** A: Settlement (Goldenfurt, Kronmark). B: none — he is a factor, not a magistrate.
C: guild-aligned, avowed; **purchased** relationship with Bailiff Konrad Ems. D: guild grade,
α-outcomes. Rival of the magistrate **Hedda Vorn**.

**Canon's four-step escalation, mapped act by act, with nothing added:**

| canon step | suite act | citation |
|---|---|---|
| Guild lobbying | `back` / supplication, and getting a seatholder to `carry` | `05 §2`, `05 §3.1`, `05 §6.1` |
| Bribery of Konrad Ems | a **purchased** contribution to a support set; Ems's compliance is a decision, not a stat | `07 §4`, `12 §1.2` |
| Hoarding-as-leverage | *"Hoarding needs no new mechanism at all. A hearth simply performs no release act; `stores` accumulates by default. Its only cost is exposure."* | `13 §4` |
| Engineered shortage | `forestall(person, good, s)` — removes intercepted yield from `supply` this season | `13 §4` |

**Four authored escalation steps, four existing acts, zero additions.** That is the single strongest
vindication in this document, and it comes from a minor NPC's dossier rather than from a design trace.

**And the counter is priced without anyone pricing it.** `forestall` is *"high-δ… a strong,
publicity-scaled negative stance the instant it is caught"*, and `06 §5`'s targeting order blames the
grain merchant seen forestalling **before** the duke who set the levy. **Tallow's strongest move makes
him the first person a rising comes for.** Genuine fork.

**THE FINDING — his stated ambition is unbuyable.** He wants a **perpetual** charter. `07 §5.4` makes a
charter a **dispensation**; `07 §4`'s purchased basis has as its characteristic cut *"outbid, or
**devalue the instrument with a dispensation changing its terms**"*; `14 §2.4` makes revocation ordinary.

> **Perpetuity is not purchasable in this design.** Any charter he wins is as durable as the next
> office-holder's willingness to leave it alone. He can have the toll; he cannot have *forever*.

Not obviously wrong — `13 §6`'s Almud Free Bond outlived its issuer by two generations because nobody
countermanded it — but **a four-season canon ambition resolves to the same object as an ordinary decree,
with no additional prize.** There is no entrenchment instrument, and this is the character who wants one.

> **VERDICT: RICH in method, BLOCKED in its stated end.** Every step to the charter is playable; the
> charter's advertised property does not exist.

### 6.6 THE EMPTY CELL AT THE CENTRE OF THE ECONOMIC LANE

Feldhaus and Kessler contest at the guild's sitting. Bergvall's survey reaches G4 only through the
guild register. Tallow's lobbying needs an item on a list.

**All three route through the guild warden — and canon names no guild warden.**

`14 §1.5` puts the guild warden on the post roster: conferred by the Free Masters at a sitting, on a
**merit** basis, revocable by the same sitting. `14 §5` makes him the **convener** of the Masterpiece
Examination and gives him the venue's veto. `05 §3.1` names the guild board's warden as the holder of
`compose_agenda`, and calls that *"the cheapest real power in the game… a man who can keep an item off
the list for four sittings running has more power over Grauwald than most of the men who vote on it."*

**Canon names five guild figures and not the one whose office decides all five of their seasons.**
That is the largest single hole this lane found, and it is not a hole in the design — it is a hole in
the roster, at exactly the coordinate the design says matters most.

---

# PART IV — THE TWO STRUCTURAL PROBES, ANSWERED

## 7. PROBE A — can several small overlapping uninstitutional factions act? **PASS.**

Feldhaus and Kessler, checked against the machinery rather than asserted.

**Are they two factions?** Necessarily. `07 §1.1`: *identity is the proposition, and nothing else
identifies a faction.* Maximum-revenue and mandate-over-revenue are different propositions, and no
operation could fuse them — `07 §5` deletes merge, split, promote and found-at-size in favour of
`commit` in two directions.

**Are they positionally opposed?** `07 §8`'s test: *jointly unsatisfiable over one stake at one
standing date*, and **the satisfiability test contains no regard term**. At the dues reckoning, funding
a relief measure out of the Compact's revenue satisfies Kessler's proposition and violates Feldhaus's.
Same stake, same date, jointly unsatisfiable. **Opposed, and no amount of mutual regard dissolves it** —
which is the refusal `07 §8` exists to enforce.

**Can each act with no institution?** `capacity(f, node, act) = ∃P ⊆ members(f) with address ⊆ node
such that requires(act, P) holds, all eligible, all passing requisition.` An existential over persons.
Feldhaus's set at the sitting is non-empty; Kessler's is non-empty; **`presence` does not appear in the
formula**, so neither needs to be larger, and neither needs a charter, a head, or a registry row.

**Can they contest each other?** `contest(container, prize, claimants)` (`04 §8`), with `07 §9`'s
binding: claimants are factions, **resolution runs through each claimant's best-placed member**, and a
claimant with an empty existential is **absent rather than defeated — and everyone can see it was
absent.** Two persons, two propositions, one prize, one function.

**Does anything break?** One honest cost, which `07 §6.1` already names: *"the fiction must never render
an institution as a speaker."* **"The Guilds decided" is permanently inexpressible**, and so is a
petition addressed to the Guilds — you address a person, and that person can drop it. Under Jordan's
ruling that is not a cost; it is the correct output.

> **PROBE A PASSES, and it passes better than a unitary Guild would have.** With one body, Feldhaus
> and Kessler's disagreement would have had to be a *stability* number on a faction sheet — which is
> exactly the dead gauge `01 §6` refuses. As several small factions it is two propositions, two
> existentials, and one `contest` call. **This is the strongest available vindication of "a faction is
> a proposition plus a commitment map, and has no verbs of its own."**
>
> **And it replicates.** §2 found the identical structure inside the Restoration — Vossen's proposition
> against Hann's, jointly unsatisfiable over whether a member avows, no institution above either — from
> two sentences of canon belief text. A structure that appears twice, unbidden, in one lane is a
> property of the object rather than a happy case.

## 8. PROBE B — are presence markers a genuine fork or a trap? **GENUINE — with a defect in *who pays*.**

`07 §6`: presence markers are `avow` used deliberately, converting covert edges to avowed; this *"raises
every observer's estimate at a node without changing capacity by one point. A real fork with a real cost,
since avowed members lose standing wherever their marks collide with the proposition, and there is no
un-avow."*

**Does the gain exist?** An estimate must actually buy something or this is a trap by construction.
It buys three things, all traceable:

1. **Other persons' choices.** `07 §3`'s own worked case: the Kettlemakers have 140 avowed at density
   0.31 and *capacity zero* at the Court Parliament — *"the praefect negotiates anyway: his estimate
   reads density."* Estimates change decisions, and decisions are the whole game.
2. **Recruitment salience**, which `07 §3` names as a consumer of the estimated profile. An avowal is a
   high-publicity firsthand deposit of the proposition, and `05 §5.1`'s spontaneous-emergence path
   needs exactly that: the proposition arriving as a claim at usable confidence where a dormant
   grievance row's re-arm predicate matches.
3. **Compliance against the movement.** `12 §1.2`: `hold(n, tgt)` is a sum over armed persons whose
   `compliance` is a decision each of them makes about *these* neighbours. A watch that now believes
   its neighbours are numerous computes differently, and the watch lives in the town.

**Does the cost exist?** Heavily, and irreversibly. `07 §1.3`: one identical discovery *"costs a
Goldenfurt Free Master his committee seat… costs an Oastad fisherman nothing… and makes a Southern
Einhir Canon a scandal."* Avowal also **closes the covert channel for that person forever**, so every
marker converts an operative into a symbol; and `03 §7` gives no cover, since avowal is extraction with
`cover` unavailable.

**Both arms are real and the shapes are right.** Gain compounds slowly and saturates; cost is immediate,
durable, irreversible. Not dominated in either direction.

> **BUT — the sign of the fork is set by the avower's marks, and the decision is taken by someone
> whose marks are different.**

Vossen holds no guild grade, no Church standing, no house name and no office. She has **nothing to lose
at any judging set**, so her own avowal cost is ≈ 0. A Free Master's is his livelihood. **The person who
inspires an avowal always pays less than the person who performs it, and the gap is exactly the marks
the movement exists to protest.**

Does the design price that? **Only on one of the two paths.**

- **Requisitioned avowal is priced.** `07 §1.2`: `burden = cost to the member's computed need + 2 × harm
  to the member's container's stake + **3 × marks the act collides with**`. That third term is the
  Free Master's seat, and it enters the obstacle. The ask gets harder exactly where it should.
- **Inspired avowal is not priced anywhere.** A member who hears the proposition told at publicity 8.8
  and avows *on their own act* runs `choose(person, view)` over their own ledger. The burden term never
  fires, because no requisition happened. Nothing routes that cost back to the person whose telling
  produced it.

And Vossen's canonical method is **inspiration**, not requisition: Solidarity primary, *"her commitments
are relational"*; `07 §8` says a leader *"changes the option set and the pool source, never a modifier"*.
She is defined as the person who makes acts exist for other people.

> **VERDICT ON PROBE B: a genuine fork, correctly shaped, with one unpriced path.** The presence marker
> is not a trap for the movement. **It is a trap for the marked member, and the leader who sets it off
> is charged nothing and told nothing.** I am not proposing a fix — that would be designing — but the
> asymmetry is real, it is the load-bearing dynamic of the only faction in the game with no wealth and
> no soldiers, and it is currently invisible to the person taking the decision.

---

# PART V — THE MATRIX

## 9. CELLS POPULATED

Modes (`00_PLAN §2 E`) against rungs (axis A), from these ten seasons only.

| mode | cells this lane demonstrates live |
|---|---|
| **Material** | Hearth (Saatfeld's farm as cover and larder) · Individual (Vedel's copies as objects with a place and a retention) · Settlement (Tallow: hoard, forestall) · Territory (Feldhaus's Compact supply chain; Bergvall's `import_flow`) |
| **Epistemic** | **Individual** (Vedel: copy, conceal) · **Hearth** (Askeland's teaching — the only entry in this cell) · Community (Askeland, Vedel, Saatfeld's cover-telling, Hann's interviews) · Settlement (Hann's surveillance; Bergvall's survey) · Territory (Bergvall's route) · **Realm** (Vossen's proposition travelling as a claim with no carrier) |
| **Political-up** | Community (Saatfeld) · Settlement (Tallow's lobbying; Kessler's carriage) · Province (Grindvold at Hafenmark) · Realm (Grindvold's supplication at the Crown council) — **and `back` without `carry` at every rung, which is the lane's characteristic shape** |
| **Argument** | Community (Kessler at the Free Masters' assembly — remonstrance) · Province (Grindvold; venue objection at stasis rung 4) · Settlement (Bergvall's G3 grounds) |
| **Relational** | Individual (`commit` at every degree) · Hearth (Askeland) · Community (Vossen and Saatfeld: `admit` at α=0.0, δ=2.0, unanimity) |
| **Institutional** | **Community only** — `admit` into a cell or a Zunft, and Feldhaus/Kessler's members-by-admission binding. **Nothing above Community, for anyone in this lane.** |
| **Coercive** | **populated but unexercised.** `Force(actor, targets, form, warrant=none)` is legal for every person at every rung (`12 §4`), and not one of these ten takes it — Vossen and Saatfeld by β-conduct and stated conviction, the rest by EV. That the design leaves the act *available* to the powerless and lets them decline it is the correct shape. |
| **Political-down** | **EMPTY AT EVERY RUNG, FOR THE ENTIRE LANE.** |

## 10. CELLS I FOUND EMPTY

**Structurally empty, and correctly so — this is the lane's definition:**

1. **`Political-down` × every rung.** `issue` requires a remit; `determine` requires a decide-rule
   naming you; `confer` and `revoke` require a conferral path. Ten characters, none eligible. The
   design says this out loud (`14 §1.2`, `14 §8`) and it is the honest shape of power without office.
2. **`Institutional` × Settlement and above.** Same reason. `admit` at Community is the whole of it.

**Empty and reportable — the design has nothing here, and that is the finding:**

3. **A faction cannot hold a standing date** (§1.6). Containers carry dates; `compose_agenda` is an
   office; a Restoration cell has neither. **No one in this lane can start a clock.** And the suite
   collides with itself on whether a cell is a container at all — `01 §4` says faction, `04 §7` lists
   it in the community roster with standing dates, `08 §10` treats it as a venue.
4. **A person with a null address is unrepresentable.** Vossen's `territory`, `birthplace` and `age`
   are null, and address is the substrate's first mandatory field. Four of the nine season sections go
   undefined: judging set, standing, larder, carriage precondition.
5. **`tell` may or may not take a cohort as hearer** (§3). Two orders of magnitude in the only growth
   channel the Restoration has, and the suite never says.
6. **What a root token resolves to after its person has been reabsorbed** (§4). De-individuation says a
   person persists only as long as somebody remembers them; corroboration says there is no null source.
   A copyist's manuscripts outlive her name, and the suite does not say what `reconstruct` returns.
7. **There is no entrenchment instrument** (§6.5). Tallow's *perpetual* charter is not purchasable,
   because any charter is a dispensation and any dispensation is countermandable. His stated ambition
   has no object.
8. **Inspired avowal is unpriced** (§8). Requisitioned avowal carries `3 × marks the act collides with`
   into the obstacle. Inspired avowal carries nothing, and inspiration is the RM leader's whole method.
9. **A G0 proposition cannot be the motion at any venue** (§6.4). A rumour is unattackable in a chamber
   and goes on operating in judging sets. I read this as correct with an unstated cost.

**Empty in the roster rather than in the design — canon holes with mechanical consequences:**

10. **No guild warden is named anywhere in canon** (§6.6), and he holds `compose_agenda`, the
    Examination's convenership and its veto. He decides all five economic seasons.
11. **Aldric Hann's registry row is null while the corpus is not** (§2). `npc_behavior_system_v1 §2.7`
    has his convictions, styles, TS, Truth and two beliefs; the registry's own issue log records the
    resolution and disagrees with the behavior file on his secondary conviction.
12. **Vossen's Thread Sensitivity is contradicted** — TS 25 (registry) versus TS 0 (behavior file). I
    wrote both branches; **both fail the Knot gate at 30 and both fail canon's Community Weaving gate at
    30**, so the season is branch-independent. It would not be for any character near the threshold.
13. **Goldenfurt's province is contradicted** between canon (Kronmark, Crown duchy) and the merged suite
    (Grauwald, Varfell, under Vaynard). Every suite trace routing a Goldenfurt grievance to Vaynard
    resolves to a different person under canon.
14. **Canon's RM Cell Resilience rule (+1 Ob at ≥3 settlements) reads a density and modifies an
    obstacle**, which `07 §3` forbids in terms. The suite reproduces its effect through per-node
    existentials instead. Report, do not port.
