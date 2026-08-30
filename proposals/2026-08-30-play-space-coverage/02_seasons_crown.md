# 02 — Seasons: THE CROWN HOUSEHOLD

## Status: FILED (2026-08-30) — Lane 1 output of the play-space coverage instrument. Ratifies nothing.
## Cell owned: **highest status, top of the ladder** — Realm rung, and Off-board.
## Authority: the merged suite (`proposals/2026-08-29-valoria-from-scratch/`) for mechanism; `canon/` and
## `references/npc_registry.yaml` for who these people are. **No new mechanism is proposed anywhere below.**

---

## 0. The finding that governs every season in this lane

Before any character: **the suite contains two incompatible act economies, and the contradiction lands
hardest on office-holders at the Realm rung.**

- `09_churning_world.md` §1.1: *"The tick is a season. **Every person and every cohort commits exactly
  one act per season.**"* Its N-line is explicit that unlimited acts destroy the collision the whole
  design exists to produce.
- `14_office_and_upper_rungs.md` §8: *"**A worked season — Vaynard, one turn, ten acts, no faction
  verbs.**"* — `convene`, `issue`, two `dispatch`es, `confer`, `revoke`, `carry`, `commit`, and more.

Doc 14 §1 forbids the obvious reconciliation in advance: *"An office adds **no verb to the game**… A
Duke and a hamlet fisher run the same `choose(person, view)` over the same act vocabulary."* If office
adds no verb it cannot add an act budget either. A third quantity, `seat_items`, exists (14 §1.3) but
governs only how many items a holder can *hear or carry at a sitting*, and is stated as a cost of
holding office rather than an allowance.

I write every season below on the **one-act rule**, because 09 owns the tick and states it as the
scarce thing. Where the ten-act reading would change a verdict I say so. It changes two: Almud goes
from THIN to arguably RICH, and Gerik Strand's canon trait becomes expressible at all.

**A second governing note: the conferral dilemma.** Doc 14 §6 states the *person-rooted* answer in
prose — the Löwenritter is *"an office cluster the King may petition and may not command"* — while
§3.3 requires the *office-rooted* one, since the root office's own warrant is external and must
terminate somewhere. Each season below declares which branch it assumes. **Kreutz's probe (§5.5) is
the one where the verdict itself flips**, and it is offered as adjudication input, not as a resolution.

---

## 1. KING ALMUD ALMQVIST — a monarch who can enter two rooms

**Coordinates.** A: **Realm.** B: **office, `binds = persons-by-presence`**, and root of a conferral
subtree that is small by construction. C: Crown faction at degree 5 *constitutive* (the proposition
**is** his seat), avowal *avowed*. D: caste-**advantaged** (Northern Einhir, Valorsmark); house
Almqvist, main line; church consecrated; **non-sensitive** — with the branch below.

### 1.1 Opening state — six fields, and what is conspicuously absent

**Address.** *Almud / Hearth of Almqvist / [court] / Valorsplatz / T1 / Valoria.* His containment path
terminates at the root, which under 14 §3.3 means his office's warrant is not conferred by anything
inside the world. It is Church consecration — *an instrument in somebody else's custody.*

**Marks.** `house = Almqvist (main)` · `office = King` · `church = consecrated` · `heritage = Northern
Einhir`. **What is absent is the load-bearing thing: he holds no deed mark of his own.** Doc 04 §3.4
computes `deed_weight` from persons whose claim of the founding service has `source == firsthand`, and
rules out inheritance in the same paragraph — *"nor inherit one, which is the same refusal read from
the other end."* Almud ascended in ~218 AG (canon timeline); the Secession settlement is 200 AG; game
start is 245 AG. He was not there. **The King cannot personally testify to the thing his office rests
on**, and every season the numerator falls as veterans in their late sixties die.

**Capability.** `stats: null` in the registry — a [GAP]. **It blocks almost nothing, and that is a
genuine vindication of doc 14 §1.2:** an act performed *by remit* draws its pool from the
establishment, not the holder. Almud's Focus is irrelevant to whether a levy is collected. It is
relevant to exactly one quantity, and that one matters: `K = 7 + Focus` (03 §4). **The size of the
King's mind is not recorded anywhere in canon.**

**Stance.** Canon primaries: Virtue 0.45, Authority 0.30; timeline: *"governance pragmatist with
ethical doubt about the caste. Complicit through cost-benefit, not malice."* Under doc 02 §3.4 that
is not a character note — it is a stance row on the caste order at **negative valence and low weight**,
sitting beside a heavily-weighted Authority row. §1.3 shows what the design does with it.

**Memory.** Reached by exactly three channels (03 §8): *"The Crown is reached by the household channel,
by a military-religious order's Grandmaster reporting directly on the order's own matters, and by the
Confessor."* In canon those three resolve to **Gerik Strand** (Lord Steward, canon-flagged
OVERPERFORMER — *"runs every important task"*), **Ehrenwall**, and **Father Gustav Linder**, whom canon
states is *"Himlensendt's agent inside Crown Inner Circle."* **Two of the King's three channels are
held by a man whose stated goal is his own indispensability and by a double agent.**

**Ties.** `form_knot` requires TS ≥ 30 on both sides (02 §4.2). Registry says TS 28; the timeline says
TS 0 and carries an explicit supersession row (*"Earlier: Almud TS 28 → **Almud TS 0.** 2026-04-11"*).
**I write around the contradiction rather than branching, because it is not load-bearing here: 28 and
0 are both below 30, so under either value Almud can never hold a Knot** — doc 02 §11.2 names him as
the worked example. It *is* load-bearing for one other act and I branch there: Thread Pool =
`floor(TS/10)` and 03 §9's rendering-facet floors are hard zeroes, so at TS 28 he registers low-floor
rendering facets at pool 2 and at TS 0 he registers none at all.

### 1.2 Computed needs — the arithmetic, per Finding 2

Doc 02 §6 gives four terms. Run them on a king.

| term | reads | value | why |
|---|---|---|---|
| SUBSISTENCE | the **world** | **0** | `5 − floor(larder_days / (10 × mouths))`. A royal larder is not Failing. The design's *principal generator of ordinary need* is structurally silent for him. |
| STANDING | world (peers) + ledger (expressed regard) | **≈0** | `peers = siblings in the person's community node`. Almud's community-rung siblings are his household. **His actual peers — three Dukes, a Confessor, a Grandmaster — are siblings in no container he shares, because the Realm is the root and has no parent.** And `care = max(w[Honor], w[Identity])/5`; canon gives him Virtue and Authority, naming neither, so `care → 0` and the term collapses twice over. |
| COMMITMENT | the **view** | **5** | `round(d × unmet × w/5)` = `round(5 × 1 × 5/5)`. Peninsular Sovereignty is his constitutive proposition; his ledger certainly holds it unsatisfied — four Dicastery clusters root at Cardinals, the Löwenritter at its Grandmaster, guild wardenships at their own chapters, Himmelenger wholly in the Church, Schoenland outside the peninsula (14 §6). |
| EXPOSURE | the **view** | small | The only standing term in his own scope that changes his options is the **Almud Free Bond** (13 §5) — his own Schoenland-era `OrdenanzaTerm` barring the Crown from fixing grain prices in its ports, *"a Province-rung term he has no unilateral office to touch."* |

**Finding 2 is answered, and the answer is worse than a null.** His needs *are* derivable without
inventing a goal. But three of four terms return ~0 and the fourth returns the ceiling, unchanged,
every season, forever. **A need function that returns a constant is not a want; it is a mission
statement.** And note the omission the table makes visible: EXPOSURE has no row for *"my warrant is in
another institution's custody."* The single most consequential structural fact about the Crown — 14
§3.3's external warrant — generates **no need at all**, because it is a conferral basis and not a
dispensation term inside his scope.

### 1.3 The view — a claim he holds that does not surface

`salience = recency × confidence_live × relevance × stanceweight`, with
`stanceweight = clamp(1 + λ·agreement, 0.05, 2.0)`, `λ = obstinacy/5` (03 §4).

Almud holds, at low weight and negative valence, the row canon calls his ethical doubt. Suppose a
claim reaches him — from Lenneth's archive, or a dropped Southern Einhir petition surfacing through
Strand — asserting that the examination standards select on heritage at correlation ~0.8 (02 §1.3).
That claim *undermines* the most-weighted stance it touches, which for a man canon describes as
*complicit through cost-benefit* is the settlement-and-Authority row, not the doubt row. `agreement =
−1`; at obstinacy 3, `stanceweight = 1 − 0.6 = 0.4`; at obstinacy 5, **0.05**. Against a K of perhaps
eleven, it does not enter the twelve.

> **The King's ethical doubt about the caste is mechanically indistinguishable from not having it.**
> Nobody hid it from him and nobody lied. He is not thinking about it.

That is doc 03's headline mechanism working exactly as designed, aimed at the highest office in the
game, and it is the best single result the suite produces in this lane.

### 1.4 The option set — every act, and why each is legal

**By remit** (14 §1.1, closed set of five):

| act | legal? | what it is actually worth |
|---|---|---|
| `issue` | yes, at general scope (14 §3.3) | **Structurally dominated.** Reach is the thinnest per node in the game — 35 settlements plus Himmelenger and Schoenland against one household establishment. Where `enforcer_presence = 0`, 06 §3's compliance contest craters, and 12 §6.3 converts each witnessed non-compliance into a claim `(order of Almud, was_obeyed, false)` that lowers every witness's `will()` on the next order. **Gain decays; cost compounds and is contagious.** Doc 14 §9 runs four R-checks and never runs this one. |
| `determine` | yes, at the Crown's council | The council's `ENTER` is *"those the King summons"*, `SPEAK` is *"those the King names"*, `admissible_source` is *"whatever he will hear"*, and the decide rule is himself (14 §5). **A venue whose door, floor and verdict he owns cannot tell him anything he did not select for.** Combined with §1.1's channels, the Crown's council is an echo chamber by construction, and no rule says so. |
| `confer` | yes — praefectures, provincial governorships, his own reeves. α 0.8, β 2.0, γ 2.0, δ 0.5, *either term alone clears* (14 §2.3) | Real, and single-handed. But these offices **already root at him**, so conferring one moves `sovereign_fraction` by zero. |
| `revoke` | requires the office lie in his **conferral subtree** (14 §2.4) | **This is the emptiest cell in the lane.** He cannot revoke a duchy, a benefice, a Canon, a Cardinal, the Confessor, the Grandmaster, or a guild wardenship. *"A Crown that conferred few offices can revoke few offices."* |
| `dispatch` | yes, one establishment member | Under the one-act rule this is his whole season. One rider buys fidelity at one node (14 §3.1) and nothing anywhere else. |
| `convene` | yes — the realm's standing dates, and their order | 14 §5 calls this *"the cheapest real power in the game."* For Almud it is nearly worthless, because the room he convenes is the one whose verdict is already his. |

**As an ordinary person** (eligibility never consults office — 01 §2): `tell`/`lie`; `petition`;
`carry`; `commit`; `requisition` kin (Torben at 3.0 head→member, Elske at 2.0 parent↔adult-child,
Lenneth at 1.0 affine — 04 §1.4); `research`/`interview`/`surveil`/`reconstruct`; marry, foster,
`admit`. **`form_knot`: NO, permanently.**

**And this is where the top of the ladder turns out to be thin.** Run the venue table (14 §5) against
his marks and office:

- Hafenmark Court Parliament — `ENTER = seat-holders + their attendants`. **The Crown holds no seat.**
  The King of Valoria may enter the Parliament of Hafenmark only as somebody's attendant, may not
  speak, and the extraordinary sitting *on a Crown vacancy* is convened by Duchess Inge Baralta.
- Dicastery of Doctrinal Adjudication — `clerics in orders`. No.
- Dicastery of the Defense of the Faith — `the accused, if summoned`. No, and one hopes.
- Dicastery of Temporal Affairs — `benefice-holders and Crown envoys`. **Not him — his envoy.**
- Dicastery of Doctrine and Archives — `anyone with a register petition`. **Yes.**
- Löwenritter chapter sitting — `sworn brothers`. No.
- Masterpiece Examination — `the Row`. No.
- the Crown's council — his own.

> **The King can personally enter two rooms in the game: the one he owns, and the Church's archive.**

### 1.5 The choice, through the seven phases

**P0 CALENDAR.** The Realm's standing date is his to set. The **tithe reckoning** fires at the
Dicastery of Temporal Affairs — a date he does not set, at a venue he cannot enter.

**P1 SETTLE.** Metabolism only. Somewhere in Valorsmark and Grauwald, three more Secession veterans
die. `deed_weight` falls, and nothing reports it to anyone.

**P2 NEEDS.** SUBSISTENCE 0 · STANDING ≈0 · COMMITMENT 5 · EXPOSURE small. One live want.

**P3 VIEW.** K = 7 + Focus, **+0 for Knots, forever**. Twelve-ish claims, deposited by Strand, Linder
and Ehrenwall, ranked by a stance-weight term that attenuates anything arguing against the settlement.

**P4 CHOOSE.** The R-check names the fork honestly: `issue` is dominated; `confer` moves nothing;
`convene` and `determine` are self-referential. What is left is doc 14 §9's genuine timing fork —
**spend the deed presumption or hoard it** — where hoarding has *"zero cost and a gain that decays to
zero with certainty."* Spending converts a mortal asset into a record row citable forever as
`same-as-precedent` (08 §2). **Almud's one non-dominated act is to produce living Secession witnesses
at a venue while they live.**

He cannot. He is not one of them (§1.1), so his own grounds would be `told_by` and would grade low
under 08's proof table; he must find, name and bring the veterans — `research` and `interview`, one
act each, one per season — and then reach a venue that will hear sworn testimony on a Crown claim.
That venue is Hafenmark's Court Parliament. **He cannot enter it.**

So he `dispatch`es a Crown envoy to the tithe reckoning at Temporal Affairs, to argue one benefice's
conferral root toward the Crown. One act, one node, one Cardinal who may simply drop it — 07 §6.1:
*"**You cannot address a petition to a Dicastery**; you address it to a person holding one of its
offices, and that person can drop it."*

**P5 RESOLVE.** The envoy's pool is the envoy's, not the King's (14 §1.2). Binding decisions resolve
before social acts (09 §1.4), so the Cardinal's determination frames the season.

**P6 WITNESS.** Whatever happened reaches Almud next season, through Strand, framed.

**P7 RECKON.** Confidence decays. `deed_weight` is lower than it was in P1 and no phase reports it.

### 1.6 What propagates

Up-stroke: nothing — the King is the top of the up-stroke, not a participant in it. Down-stroke: one
node, if the envoy carried. Neither, mostly. **The realm-scope instrument he owns and did not use is
the only thing that would have propagated far, and using it is the move that costs him authority.**

### 1.7 Diagnostic — **THIN**

Options exist and are legal, but the differences between them are near-cosmetic against the one want
the needs function returns. The R-check is decisive: `issue` is **structurally dominated** (decaying
gain, compounding and contagious cost); `confer` and `convene` return zero on the only live need;
`determine` is self-referential. The one act with genuinely different consequences — spending the
deed presumption — is **BLOCKED at the venue gate**, because the room where a Crown claim is tested is
entered by seat-holders and convened by the claimant against him.

Under the ten-act reading of doc 14 §8 the verdict moves toward RICH, because he could investigate,
convene, dispatch and confer in one season and compose them. **That is how much the unreconciled act
economy is worth: it is the difference between a playable monarch and a thin one.**

*Conferral branch assumed:* **person-rooted** (14 §6). Under office-rooted, his asks to Ehrenwall
become orders, `revoke` reaches the Löwenritter's chapters, and the season becomes THIN in the other
direction — one option dominating rather than none mattering.

### 1.8 Cells populated
Realm × Political-down (dominated) · Realm × Institutional/`confer` (live, inert) · Realm ×
Institutional/`revoke` (**near-empty**) · Realm × Epistemic (as a *consumer*, not an actor) · Realm ×
Relational (live — see §3, §4).

---

## 2. QUEEN LENNETH ALMQVIST — the most valuable probe in the roster

**Coordinates.** A: **Realm**, inside the royal hearth. B: **NONE.** C: Crown, avowed, high degree —
**and** an edge toward the Restoration's proposition (canon: *"Pro-Restoration — institutional
revivalist, allied with Yrsa Vossen"*), whose avowal is the season's real question. D: house Almqvist
by marriage; church communicant; heritage [GAP]; TS [GAP] — and the GAP decides her season.

### 2.1 Opening state, and the four asymmetries nobody authored

Canon is unusually generous: primaries **Equity 0.45, Liberty 0.25**; goals **"Einhir revival through
Crown authority"** and **"Caste dismantlement through royal decree"**; *"Archivist by training"*;
*"Lenneth archive awakened Torsvald's TS."*

Four facts fall straight out of the mechanism, and none of them was written for her:

1. **She holds no `office` mark, so `S_post` is empty and `licensed_standing = 0`; therefore
   `shadow(p,n) = standing(p,n)` (14 §1.4).** The Queen of Valoria is the design's purest case of
   **wholly unlicensed standing.**
2. **Doc 07 §5.2 then fires on the King.** When `shadow > 0` and the formal holder attempts an act
   whose `requires` predicate includes persons in her support set, *"`h`'s capacity returns **zero** —
   not a penalty, an empty existential. Repeat twice and `h`'s cheapest remaining act is
   **legalisation**."* **The design computes, from nothing but a subtraction, why a consort gets a
   regency** — and canon's registry already records the answer: *"Queen (Widow Regent if Almud
   eliminated)."* Nobody promoted anybody.
3. **The obligation edge runs 3:1 against her.** Doc 04 §1.4: head→member of the same hearth **3.0**;
   affine, first degree **1.0**. Almud can requisition his Queen at three times the claim weight she
   can requisition him. That asymmetry was written for cadet branches and lands on a marriage.
4. **She can out-think her husband.** `K = 7 + Focus + 2 per Knot consulted` (03 §4). Almud's Knot
   term is permanently zero. If Lenneth's TS ≥ 30, hers is not. **The Queen holds more of the realm in
   view at once than the King does**, and the gate is a threshold neither of them chose.

**What is conspicuously absent:** any `office`, any `remit`, any establishment, any seat, and — this
is the one that decides her — any definition of the phrase her whole political life depends on.

### 2.2 Computed needs

SUBSISTENCE **0** (royal larder). STANDING: peers are her siblings in the court community; `care =
max(w[Honor], w[Identity])/5` and canon names Equity and Liberty, so `care → 0` and the term collapses
exactly as it does for her husband. **COMMITMENT: live and high.** Two propositions — *(the peninsula's
Einhir practice, is restored, all-time, **ought**)* and *(the caste order, is dismantled, all-time,
**ought**)* — held at Equity weight 4–5, both unmet in her ledger, at whatever degree her Restoration
edge carries. At d=3, `round(3 × 1 × 5/5) = 3`; at d=4, **4**. EXPOSURE: every standing term that
touches the examination gates and the tithe.

**Two of four terms live, both from the polity, both reading the view.** She is the mirror of Almud:
he wants one thing at the ceiling forever; she wants two things whose satisfaction is measurable and
whose progress her own archive can measure.

### 2.3 The view, and the claim that does not surface

Her ledger's distinguishing content is **verified rootprints**. Doc 03 §6.1: archives are *"the only
non-person root-bearers"*, and `research` yields `told_by(record, …)` with verified roots and old
`when`. Doc 08 §0 then makes a recorded row an **instrument**, entering later sittings at proof grade
**G4**. **The Queen manufactures the highest-grade evidence in the game.**

The claim she holds that does not surface is not hers — it is what happens to hers when she hands it
over. Salience reads the *hearer's* stance weight on the subject (03 §4), not his regard for the
speaker; the speaker enters only once, at deposit, scaling confidence through `hear` (02 §3.2). So
**her intimacy buys reliable delivery and no salience.** Her ties to Almud are high-familiarity — 02
§4.1: a tie *"sets the probability and latency with which a claim reaches b"*, and explicitly not its
weight. A G4 instrument proving the correlation lands in the King's ledger at good confidence and is
then multiplied by 0.05 (§1.3). **The Queen's greatest asset — the King's ear — is worth nothing at
view assembly, and the design says so in a formula rather than in a sentence.**

### 2.4 The option set — the load-bearing section

**Not available, and this is the shape of the cell:** `issue` · `determine` · `confer` · `revoke` ·
`dispatch` · `convene`. All six remit acts, absent. **Her stated canon goal — *"caste dismantlement
through royal decree"* — names an instrument she has no act to reach.** She must move the one person
who holds it, whose view attenuates exactly the claims that would move him.

**Available, and three of them are real:**

- **`admit` — over the archive's gate.** Doc 03 §6.2 states that `research` is *"the only gated act,
  and its gate is an admission act at a community… held by persons."* Lenneth holds standing in the
  Crown's archive. **`admit` is an institutional act performed by a person with no office**, and it is
  precisely what canon records her having already done: *Lenneth archive awakened Torsvald's TS.* Doc
  14 §7 supplies the mechanism with nothing added — Thread Sensitivity grows from **unresolved**
  anomalous witnessing, and catechesis pre-resolves anomalies in advance. **Admitting a person to
  material catechesis never covered removes the pre-resolution.** She awakened a sensitive by opening
  a door, and required no TS of her own to do it.
- **`research`, then hand the instrument to a carrier.** Doc 02 §1.3's named counter-play to the caste
  order: *"correlation is measurable… ten years of grants against candidates' practice provenance…
  produces a claim with a firsthand root, which can be carried as a petition."* She can produce it.
  She cannot carry it — see the hole below.
- **`commit`, and choose the avowal.** Doc 07 §6: *"converting covert edges to avowed raises every
  observer's estimate at a node without changing capacity by one point. A real fork with a real cost,
  since avowed members lose standing wherever their marks collide with the proposition, and **there is
  no un-avow**."* An avowal by the **Queen** is the highest-publicity act available to anyone:
  `publicity = venue_factor × √witnesses × mark_salience`, at cathedral/parliament `venue_factor 2.0`
  and the highest `mark_salience` in the peninsula (04 §4.1). It moves **estimated** Restoration
  density at the realm root in every observer's ledger simultaneously, and adds **zero** capacity. It
  is irreversible. That is a genuinely non-dominated fork and it is hers alone.
- **`form_knot`** — if TS ≥ 30. Canon: `ts: null` [GAP]. With it, she holds the game's only
  channel that bypasses correspondence filtering, and her canon allies — Yrsa Vossen, Sigrid Torsvald
  — are exactly the people it would reach. Without it she is as channel-poor as her husband. **A [GAP]
  in one registry field is the difference between a rich season and a narrow one.**
- `petition` · `tell`/`lie` · `interview` · `reconstruct` · `requisition` (Almud at 1.0).

**THE HOLE.** Doc 05 §3.1's `carry` precondition reads: *"c holds STANDING at respondent_container(P)
— a seat, an office, **a right of audience**, or membership in its judging set."* **Nothing anywhere
in the suite defines who holds a right of audience.** For a Queen with no seat, no office and no
judging-set membership, that clause is the entire question of whether she has a political-up channel
at all. And her fallback is worse than undefined: the one Realm-rung venue she might attend, the
Crown's council, has `ENTER = those the King summons` and `SPEAK = those the King names`. **Her access
to the only room at her rung is granted per sitting by a man who can requisition her at 3.0.**

### 2.5 The choice, through the tick

**P0** — the Kettlemakers' Examination and the tithe reckoning are on the docket; neither is hers.
**P1** — nothing. **P2** — COMMITMENT 4, EXPOSURE live. **P3** — her view, uniquely, contains verified
archival rootprints nobody else holds. **P4** — the fork is real and three-way: `admit` a second
person to the archive (compounding, quiet, and it manufactures sensitives); `research` the grants
correlation and spend a season looking for a carrier who may drop it (05 §4 — dropping is an act by a
named person, and the grievance deposits on *her* backers, who are Southern Einhir journeymen she has
never met); or `avow` at publicity 2.0 and convert her whole standing into other people's estimates.
She admits. **P5** — an uncontested social act, resolved last in the stratum order. **P6** — witnessed
by the archive's own gatekeepers, who now hold a claim about whom the Queen lets in. **P7** — the
admitted person's anomalous witnessings begin accumulating unresolved.

### 2.6 What propagates

Neither stroke. **And that is the interesting part.** Her act propagates through the *conferral graph
of catechesis in reverse* (14 §7) — one more unresolved-anomaly path in a realm whose Church coverage
is the thing suppressing them. It is slower than a decree and it cannot be countermanded, because no
dispensation term names it.

### 2.7 Diagnostic — **RICH**, with a BLOCKED goal and an undefined channel

Three acts with materially different shapes of gain and cost, none dominating: `admit` (slow,
compounding, unobservable, and it grows the exact population the caste order exists to suppress);
`research` + carrier (produces the game's highest-grade evidence, and hands its fate to a man who may
silently drop it); `avow` (instant, maximal in perception, zero in capacity, irreversible). She is
the **richest character in this lane and she holds no office**, which is the strongest available
vindication of doc 14's claim that an office adds no verb.

Two findings against it. Her stated canon goal is **BLOCKED**: *caste dismantlement through royal
decree* requires `issue`, which she cannot reach by any act she owns, and the man who can has a view
that attenuates her evidence to one twentieth. And her political-up mode rests on an **undefined
precondition** (`right of audience`), with a fallback that is revocable at will.

*Conferral branch assumed:* **neither** — nothing in her season reads the conferral graph, which is
itself worth recording: the design's hardest open question does not touch its best character.

### 2.8 Cells populated
Realm × Epistemic (**strongly** — research, admit, the only archive) · Realm × Relational (commit,
avow, Knot-if-TS) · Realm × Institutional via `admit` at a gate she holds — **the only institutional
act in this lane performed with no remit** · Realm × Political-up **UNDEFINED** · Realm ×
Political-down **EMPTY** · Realm × Material **EMPTY** · Realm × Coercive **EMPTY**.

---

## 3. PRINCESS ELSKE ALMQVIST — an address outside every scope

**Coordinates.** A: **Off-board** — *Elske / Hearth of Laskaris / [Altonian court] / … / Altonia.* B:
none. C: Crown by birth, and a marriage-treaty relation; canon: *"Recruitable."* D: house Almqvist,
married out; **TS 0** (canon, `behavior_v30` table); `certainty: 3` — *"Truth disrupted by hostage
status and competing loyalties."*

### 3.1 Opening state — what a marriage did to her containment path

Marriage is an ordinary act that edits an address and a succession pointer (01 §4). Three consequences
are computed, not authored:

1. **Her address no longer reaches the Valorian root.** Doc 06 §1: a dispensation's `scope` is a list
   of containment nodes, and it lands on persons whose *address* is inside it. **No Valorian
   dispensation contains her.** EXPOSURE therefore returns nothing for every term the Crown issues.
   Her father's decrees are literally not about her.
2. **Her obligation edges survived the move, and one of them is startling.** Doc 04 §1.4: parent ↔
   adult child, separate hearths, base **2.0**; affine first-degree **1.0**. **The married-out
   daughter holds twice the claim on the King that his own wife does.** Defensible as blood-over-
   affinity, but nobody chose it — it falls out of a table written for cadet resentment.
3. **The banked claim is real and it is not hers to spend.** Doc 06 §7's collateral table: *"Marriage
   — binds two houses' successions together."* Cognatic-senior succession is canon (*capability over
   gender*). So the Laskaris hearth now holds a pointer into the Almqvist succession, and doc 04 §3.4
   makes the timing explicit for the **Baralta Crown Claim** — *"a banked marriage claim presented at a vacancy
   against a deed-presumption whose witnesses are gone."* **Altonia holds the same instrument and does
   not even need the witnesses to die; it needs a vacancy and a child.**

**Absent:** any office, any establishment, any seat, and — decisively — any Knot. `form_knot` requires
TS ≥ 30 both sides; canon gives her **TS 0**. **The design's best cross-border channel is unavailable
to the one person positioned to use it.**

Also absent: any home for `certainty: 3`. The suite's six person fields have no analogue of canon's
Truth/certainty rating. The nearest is `credulity`, which doc 02 §3.2 pins to exactly one reader and
warns must never acquire a second.

### 3.2 Needs, view, and option set

SUBSISTENCE 0 · STANDING: her peers are now Altonian courtiers, and expressed regard toward a
foreign-married princess is a ledger read she has few rows for · COMMITMENT: undefined, `goals: null`,
`convictions.primary: null` [GAP] · EXPOSURE: **zero from Valoria by construction**, live from
Altonian terms — which is exactly how doc 06 §7's worked trace strips Torben's honoured-guest mark
with a *local* dispensation.

Her option set, honestly enumerated:

| available | not available |
|---|---|
| `tell` / `lie` across the seam — she is the only person in the game with high-familiarity ties in both courts | all five remit acts |
| `interview`, `surveil`, `reconstruct` at the Altonian court | `carry` — no carrier of hers holds standing at a Valorian container except her father and the Queen |
| `petition`, if a carrier can be found | `form_knot` — TS 0 |
| `commit` — canon calls her recruitable | any venue: Hafenmark needs a seat, the Dicasteries need orders or a benefice, the chapter sitting needs an oath |
| `requisition` Almud at 2.0 | `research` at a Valorian archive — the gate is a person, and she is not present |
| migration home (P1 advances travellers) — but it breaches the collateral | |

**The one-directional channel.** Her value looks like an intelligence conduit and is half of one.
`witness` takes vantage (01 §3.3): she can witness Alexios's court and cannot witness a Valorian
customs officer taking a reimposed duty — which is exactly why doc 06 §7 routes the breach discovery
through a **merchant-captain** and not through her. She is an excellent channel *out of* Altonia and a
poor one into it.

### 3.3 Diagnostic — **THIN**

Options exist and **one dominates by shape.** Every act she owns except one is Epistemic — telling,
interviewing, reconstructing — and telling is cheap, repeatable, high-value, and risks only being
caught (03 §3.2). Her one non-epistemic asset, the banked succession claim, has **no venue she can
reach**: she cannot enter Hafenmark's Parliament, and the extraordinary sitting on a Crown vacancy is
convened by the rival claimant.

The off-board question this lane was asked to touch — *may an off-board polity act without a person to
carry it* — gets a partial answer here rather than a resolution: **for Altonia it does not arise,
because Altonia has a person, and she is a Valorian princess with an obligation edge to the King at
2.0.** That is a vindication of person-routed capacity, not a closure of the open item.

*Conferral branch assumed:* **neither.** Her season never reads the conferral graph.

### 3.4 Cells populated
Off-board × Epistemic (live, one-directional) · Off-board × Relational (live — marriage, succession
pointer, requisition across the seam) · Off-board × Political-up **BLOCKED at the carrier** ·
Off-board × Political-down **NULL by address** · Off-board × Argument, Material, Coercive,
Institutional — **all four EMPTY.** Off-board is 2 modes of 8.

---

## 4. PRINCE TORBEN ALMQVIST — the null vector

**Coordinates.** A: **Realm**, inside the royal hearth. B: none. C: **none — no faction edge at any
degree.** D: house Almqvist, main line, heir apparent; caste-advantaged; TS [GAP].

**Canon placement, and a divergence I must report.** The timeline puts Torben *"at Royal Court;
Altonia eyeing him as leverage,"* with the tutoring demand triggering at **IP 30** against a current
IP of **20 (Dormant)**. The merged suite instead places him at the Altonian court as treaty collateral
— twice, in `14 §2.2` and `06 §7`. That is FINDING 1's shape: **the suite borrowed a canon name and
gave it an incompatible life.** I write canon's Torben, at the Royal Court, with the hostage state as
the thing that has *not yet happened*.

### 4.1 Opening state — six fields, four of them empty

Address: inside Almud's hearth, where Almud is head. Marks: `house = Almqvist (main)`, heir. Memory:
a boy's ledger. Ties: household. Capability: `stats: null`. **Stance: `convictions.primary: null`,
and canon says so deliberately** — *"Convictions intentionally undefined at game start — emerge during
play"* (ED-618, emergence window Seasons 1–8).

### 4.2 Computed needs — all four terms return zero

| term | value | derivation |
|---|---|---|
| SUBSISTENCE | **0** | royal larder |
| STANDING | **0** | `urgency = round(5 × (1−r) × care)`, `care = max(w[Honor], w[Identity])/5`. Both rows are undefined, so both weights are 0. **`care = 0` annihilates the term regardless of how his peers regard him.** |
| COMMITMENT | **0** | `round(d × unmet × w/5)`; he holds no faction edge, so `d = 0` |
| EXPOSURE | **≈0** | the delta in the value of his own reachable options; a boy at court has few options for a term to change |

**Every need term returns zero.** `choose(person, view) → act` still offers him the full act
vocabulary — eligibility never consults office — but there is **no ranking signal**, and doc 09 §1.5
supplies the fallback: *"Ties break on a hash of (act-id, world-seed)."* The engine's answer to *what
does the heir apparent do this season* is **a hash.** That is worse than inaction; it is arbitrary
action wearing agency's clothes.

### 4.3 The deadlock — and it is arithmetic, not judgement

Can he acquire a stance and break out? Doc 02 §3.4 seeds a row when a person meets a proposition they
have no row for:

```
seed_valence = clamp( round( Σ_c sig[c]·stance[c].valence / Σ_c |sig[c]| ), −5, +5 )
seed_weight  = max_c ( |sig[c]| > 0 ? stance[c].weight : 0 ) − 1
```

**The seed is computed from Conviction rows. His Conviction rows are the ones that are absent.** So
every proposition he meets seeds at valence 0 and `seed_weight = 0 − 1 = −1`, clamped to 0. Then doc
02 §3.3: `resist = 1 + obstinacy + weight`, and `Δvalence = round(pressure / resist)` — a zero-weight
row is movable, but only by pressure, and the pressure sources are: a witnessed event **contradicting
a stance** (he has none), a **telling** (which deposits a claim, not a stance), an **unmet
stance-commitment** (he has none), and **cost paid for a stance** (weight only).

> **Nothing in the suite writes a first weighted stance row for a person generated without one, except
> generation itself — and canon forbids generating his.**

Doc 02 §8's generator *would* fill them, from the node's cohort stance centroid, which is precisely
what canon's `cultural_label: valorian_court` field is for. **The suite's generator forecloses canon's
emergence window on contact.** The two documents are each internally consistent and jointly
unimplementable.

And the deadlock is self-sealing. `form_knot` requires Disposition +5 — i.e. `stance[person].valence`
at maximum (02 §4.2). Torben's valence toward everyone is 0 and has no mechanism to rise. **He cannot
form the channel that would give him the news that would give him a stance.**

### 4.4 The one live seam, which does not rescue him

There is exactly one path by which the design writes Torben a first stance row, and it is worth
naming precisely because it is the only one. Doc 04 §1.4's obligation edge, head→member of the same
hearth, claim weight **3.0**:

```
on asking:   Δstance(b→a) = −0.5 · max(0, strain − claim_weight)
```

If Almud requisitions his son for an act whose strain exceeds 3.0 — and `strain = cost/capacity +
2·conflict(act, stances)`, where a boy's capacity is small — **Torben's stance toward his father takes
a negative write.** That is the first row in his table, and it is negative by construction.

> **The heir apparent's only mechanically available route to having an interior is resentment of his
> father, and it requires his father to spend an act over-asking.**

That is an extraordinarily good fit for canon's Arc E and the Royal Assassination Fuse. It is also,
diagnostically, the opposite of agency: his interior is written by somebody else's act, in one
direction only.

### 4.5 Diagnostic — **SPECTATOR**

I am forbidden from rescuing this and I will not. All four computed need terms return zero; his stance
table cannot acquire a weighted row by any mechanism the suite contains; his Knot channel is gated
behind a valence he cannot reach; he holds no office, no seat, no faction edge, and no `research`
gate. He is acted upon — by Altonia's tutoring demand at IP 30, by the suite's hostage clause, by his
father's requisition — and the engine chooses his own act with a hash.

**The design renders being-acted-upon correctly, as `requisition`, and does not render being a
person.** That is the finding, and it is not a canon gap: canon *asked* for a character whose
convictions emerge in play, and the suite has **no conviction-emergence mechanism** to meet the ask.

*Conferral branch assumed:* **neither** — although note that under a **person-rooted** answer, Torben
inherits nothing that can be conferred, since his father's office names no living conferrer; and 14
§2.2 says the vacancy's characteristic act is a **lie about who you are**, naming Torben explicitly.
His playable season, if he has one, is in an interregnum he does not act in.

### 4.6 Cells populated
Realm × **nothing.** Realm × Relational appears only as the *object* of another person's
`requisition`. This is the lane's empty cell, and it sits on the heir to the throne.

---

## 5. PROBE SEASONS — the Crown Inner Circle

Coordinates, option set, diagnostic. No full trace.

### 5.1 Wilhelm Voss — Royal Marshal
**A:** Realm. **B:** office, binds-by-presence over the Crown's military establishment. **C:** Crown,
avowed. **D:** court marks; Order 0.35 / Authority 0.25; Truth 4; `goals: null`.
**Options.** `dispatch` (his establishment); `apportion` a levy at each rung it refracts through (12
§2.2); raise a **retinue** on the alignment channel instead (12 §2.1); `determine` at no venue he
convenes; ordinary person acts.
**The constraint that defines him.** The levy routes through *containment* — territory → settlement →
community → hearth — and the territories' apportioners in Varfell and Hafenmark hold **ducal** offices
the Crown did not confer. The retinue routes through *coin*, which is Reichard's. **Voss's capacity is
a conjunction over two other people's offices and he holds neither**, and 12 §2.2's refusal branch
closes the loop: *"The levy is enforced by a levy, and usually cannot be."*
**Diagnostic — THIN.** One mode (Coercive), one act (muster), whose success is decided outside his
conferral subtree. He has no second mode: no venue, no archive, no gate, no channel.

### 5.2 Annalie Reichard — Lord Treasurer
**A:** Realm. **B:** office. **C:** Crown, avowed. **D:** Precedent 0.35 / Authority 0.25; Truth 5;
`goals: null`. Registry flags a possible person-collision with a struck "Cardinal Reichard" — **I do
not resolve it; nothing in this probe depends on it**, since either reading leaves the Lord Treasurer
in the Crown circle.
**Options.** `dispatch` collectors; devalue a purchased instrument (07 §4's purchased-basis cut,
which requires a *dispensation changing its terms* — and she cannot `issue`); `determine` if a venue
names her; ordinary acts.
**The empty cell she stands in.** Doc 13 owns material life at the **hearth** (larder) and the
**settlement** (granary, stake, prices, slow fuses). Doc 14 §1.3 gives an office an *upkeep* drawn
from *"the tithe share, the levy, the gate's fees."* **There is no realm-rung material object
anywhere in the suite.** A Lord Treasurer has no treasury to hold. Her real instrument is the **Almud
Free Bond** (13 §5) — and it is a term she cannot countermand.
**Diagnostic — THIN.** Her mode has no object at her rung; she operates entirely by proxy through
settlement-rung reeves. **Material × Realm is the cleanest empty cell in this lane.**

### 5.3 Kolbrun Thale — Spymaster
**A:** Realm. **B:** office. **C:** Crown avowed **plus** covert edges through Niflhel contacts;
rumoured Southern Einhir. **D:** Liberty 0.30 / Utility 0.30; **Truth 3, lowest in the circle**.
**Options.** `surveil`, `interview`, `reconstruct`, `plant` (03 §6.1) — all first-class and all
available to anyone; concealment as a field on every act (03 §7); covert requisition along **Knots**,
if TS permits; `filter_share` on the intelligence channel (03 §8).
**The fork that makes her rich, and the design states it against her by name.** Doc 14 §1.3, cost 2:
*"Every act by remit is performed at `venue_factor ≥ 1.0`… **An office-holder cannot act quietly.**
This is the real price, and it is why Niflhel's recruiters hold no office and the Burned hold no post:
a covert edge and a remit are close to incompatible."* So Thale chooses **per act** between reach
(by remit, public, establishment pool) and quiet (as a person, private, her own pool), and cannot have
both. Non-dominated in both directions.
**Second live structure.** Rumoured Southern Einhir at the top of the realm is doc 02 §1.2's
`Passing`, read by `attention = |stance|` — *a reader's bigotry is exactly their attention* — with doc
02 §5.2's trap behind it: **passing degrades the capacity to pass**, since each concealment opposing a
primary Identity conviction costs a Coherence step and Dissonant reads presented marks at −1.
**Diagnostic — RICH.** Two live modes (Epistemic, Relational-covert), a genuine per-act fork, and a
compounding personal cost with a named failure state.

### 5.4 Father Gustav Linder — the double agent, and the suite's unnamed worked example
**A:** Realm. **B:** office **in two clusters at once** — a benefice rooted at a Cardinal, and a seat
in the Crown's inner circle. **C:** Church, avowed; the Confessor's agency inside the Crown, **covert**.
**D:** Faith 0.60 / Authority 0.20; **Truth 5, highest in the circle**.
**Options.** The three channel dispositions (03 §8): **approve** (pass with endorsement attached as a
claim), **suppress** (drop it; the petitioner is not told; a record deposits *in his own ledger*, which
is the only reason it is risky), and **surface** (pass it *framed* — *"more powerful than suppressing
and leaves less trace"*).
**The suite wrote his season without naming him.** Doc 03 §8: *"A Confessor is the channel to a
monarch's conscience, and sincerity is not a mitigation: his construal selection runs on a
Conviction-primary of Faith, so the reading he attaches is the one under which **suppression is
pastoral care**."* Linder is the terminal of that channel at Faith 0.60.
**Where the conferral dilemma does NOT bite, worth recording as a control.** Doc 14 §2.4: revocation
requires the office lie in the revoker's conferral subtree. Almud can revoke Linder's **Crown seat**
and cannot touch his **benefice**, under *both* branches — the benefice roots at a Cardinal either
way. **The King can expel him from the room and not from the Church.**
**Diagnostic — RICH.** Three dispositions per item, each with a different trace signature, exposure
that is exactly one `interview` by one backer, and two conferral roots that cannot both be cut.

### 5.5 Theodor Kreutz — Royal Guard Captain / Löwenritter liaison
**A:** Realm. **B:** office (Crown-conferred). **C:** Löwenritter relation; **canon: *"Pre-designated
allegiance to Almud personally. His removal triggers Löwenritter Autonomy escalation toward Split."***
**D:** Order 0.35 / Authority 0.25, `cultural_label: lowenritter_military`; Truth 4.
**This is the conferral dilemma incarnate, and the verdict flips on it.**

| branch | what happens on Almud's death | verdict |
|---|---|---|
| **person-rooted** | Kreutz's allegiance is to a person. 07 §5.3's patronage fragmentation fires: *"When the root dies, every conditioned contribution voids in one event."* The Löwenritter's warrant, being sworn to *Crown-as-institution*, terminates nowhere — so the order's own root is Ehrenwall, and Kreutz's Crown tie is severed while his order tie is not. **Canon's Split escalation is reachable.** | **RICH** |
| **office-rooted** | The office persists across the vacancy; the `Holding` edge transfers to the successor; the Löwenritter's institutional oath binds to the same institution it always did. **Canon's Split escalation cannot fire.** | **THIN** |

**Reported, not resolved.** Canon's own stated arc trajectory for this character is reachable on
**only one** of the two branches. That is a concrete input to the ruling and it is the most useful
thing this probe produces. One man holds both halves of the dilemma: his allegiance is *personal*
(person-rooted) and his order's oath is *institutional* (office-rooted), simultaneously, in canon.

### 5.6 Peder Almstedt — Chief Parliamentary Clerk
**A:** Settlement-to-Realm, wherever the business routes. **B:** office — **and the most powerful one
in this lane.** **C:** Crown/Ministry, avowed. **D:** Order 0.40 / Precedent 0.20; goals: *"Maintain
procedural correctness"*, *"Block radical action through procedure."*
**Options.** `compose_agenda` (05 §3.1) — an act, costing one of his own acts for the season, whose
input is *"the petitions v HOLDS A CLAIM OF — not the petitions that exist"*, and whose omissions
**are drops and deposit as drops**. Plus the channel dispositions of 03 §8.
**The two sentences the suite wrote for him.** Doc 07 §4, bureaucratic basis: *"volume filtered, not
rank — **a clerk at standing 1 who reads every petition outranks a minister**."* And doc 14 §5: *"The
convener holds the cheapest real power in the game… a convener who puts three items ahead of yours has
spent nothing and killed your petition… which is why the guild warden and the **Dicastery's clerk**
matter more than their remits suggest."*
**His cut, and it is the cheapest in the table.** *"A single bypass, used publicly once. S empties,
because its members were never loyal — only routed."*
**A GAP.** Canon does not say **which** parliament he clerks. If it is Hafenmark's Court Parliament,
he is a Crown officer composing the agenda of Duchess Baralta's venue — which is doc 14 §4's
jurisdictional case, stasis rung 4, *this chamber may not hear it*. If it is a Crown ministry body,
he is composing an agenda for a room whose decide rule is the King. **The two readings give different
games and the registry is silent.**
**Diagnostic — RICH**, and the finding beside it: **the design serves the clerk better than the King.**
Almstedt's `compose_agenda` reaches more outcomes per act than any of Almud's six remit acts, and it
costs him nothing but the act.

### 5.7 Gerik Strand — Lord Steward (canon's, per FINDING 1)
**A:** Realm, the royal household. **B:** office. **C:** Crown, avowed. **D:** Authority 0.30 /
Utility 0.30; goals *"Efficient Crown administration"*, *"Maintain personal indispensability"*;
canon flag **OVERPERFORMER** — *"runs every important task"* — and flattery-vulnerable at −1 Ob on
social actions acknowledging competence.
**Options.** `filter_share` on the household channel — the first of the King's three channels, and
under the OVERPERFORMER flag the one carrying most of the traffic; `dispatch` within the household;
the three dispositions; ordinary acts.
**He is the sharpest test of §0's contradiction.** *"Runs every important task"* is **impossible**
under 09 §1.1's one act per season and **trivial** under 14 §8's ten-act season. A canon trait about
act throughput cannot be represented until the act economy is settled.
**His second goal has a mechanical implementation that succeeds by construction.** *Maintain personal
indispensability* is 07 §5.2's shadow standing, grown deliberately: shadow > 0, the principal's
capacity returns an empty existential twice, and *"`h`'s cheapest remaining act is **legalisation**"*
— the King's cheapest response to an indispensable steward is **to give him a larger office**.
**And the King's counter is shut by a threshold.** Strand's basis is bureaucratic; its cut is *a
single public bypass*. The bypass available to a principal is a **Knot** to the source — *"a channel
with bandwidth that bypasses correspondence entirely"* (03 §8) — and Almud, at TS 28 or TS 0, can
never form one. **The King's only clean route around his own steward is TS-gated shut.**
**A canon→suite mapping gap this probe exposes.** Canon expresses NPC flaws as **obstacle
modifiers** (flattery: −1 Ob). Doc 02's opening commitment is *"nothing here is a modifier"*, and 14
§1.2 and 12 §3.1 both refuse flat shifts on arithmetic grounds. **Canon's entire flaw/vulnerability
system has no home in the suite**, and it hits at least Strand and Almstedt (*"cognition-heavy social
contest target"*).
**Diagnostic — RICH.** He holds the channel, the shadow, and the only basis whose cut his principal
cannot execute. He is the person who actually runs the Crown.

---

## 6. CELLS POPULATED

E × A, from the eleven seasons above. **LIVE** = demonstrated by a season with a legal act and a
material consequence.

| mode | **Realm** | **Off-board** |
|---|---|---|
| **Material** | **EMPTY** — see §7.1 | EMPTY |
| **Epistemic** | **LIVE, and the richest cell in the lane** — Lenneth's archive and `admit`; Thale's surveil/conceal fork; Linder's three dispositions; Strand's filter share | **LIVE but one-directional** — Elske tells out of Altonia and cannot witness into Valoria |
| **Political-up** | LIVE for Dukes and clerks; **DOMINATED for the Crown** (every required ask routes through a person who may silently drop it); **UNDEFINED for the Queen** (`right of audience`) | **BLOCKED at the carrier** |
| **Political-down** | LIVE but **structurally dominated** — realm-scope `issue` has decaying gain and compounding, contagious cost | **NULL by address** — no Valorian scope contains her |
| **Argument** | **LIVE for two rooms only.** The King can personally enter his own council and the Dicastery of Doctrine and Archives. Every other venue's `ENTER` predicate excludes him | EMPTY |
| **Coercive** | LIVE but **conjunctive** — Voss's levy routes through ducal apportioners outside the Crown's conferral subtree | EMPTY |
| **Relational** | **LIVE, and it is the Crown's strongest mode** — marriage (Elske), fosterage/collateral (Torben), kin requisition at 3.0/2.0/1.0, `commit` and `avow` (Lenneth) | **LIVE** — the marriage binds two successions and survives the address change |
| **Institutional** | **SPLIT.** `confer` LIVE but inert on the only live need; `convene` LIVE but self-referential; `admit` LIVE **with no remit at all** (Lenneth's archive gate — the lane's best result); **`revoke` NEAR-EMPTY** | EMPTY |

**Cross-cuts demonstrated.** B = *none* at the highest status (Lenneth) is **richer** than B =
*highest office* (Almud) — the strongest available vindication of doc 14's "an office adds no verb."
C = *covert* at Realm is live and self-limiting (Thale, Linder). D = *caste-advantaged +
non-sensitive* is the most **channel-poor** combination in the game, and it is what the King and both
his children carry.

---

## 7. CELLS I FOUND EMPTY

Ordered by how much they cost.

**7.1 Material × Realm is empty.** Doc 13 owns the larder (hearth) and the granary/stake/prices
(settlement). Doc 14 §1.3 gives an office an *upkeep* drawn from settlement-rung stakes. **No
realm-rung material object exists**, so the Lord Treasurer of Valoria has nothing to hold and can act
only by proxy through reeves. This is not a gap in a character; it is a gap in the E × A grid.

**7.2 `revoke` at Realm is near-empty, and the conferral dilemma decides how near.** The King cannot
revoke a duchy, a benefice, a Canon, a Cardinal, the Confessor, the Grandmaster or a guild wardenship.
Under the **office-rooted** branch he reaches the Löwenritter and the picture changes materially.
**Reported, not resolved.**

**7.3 The Realm rung has no defined peer set, so STANDING returns zero at the top of the ladder.**
Doc 02 §6 computes STANDING over *"siblings in the person's community node."* The Realm is the root
and has no parent, so a King's actual peers — three Dukes, a Confessor, a Grandmaster — are siblings
in no shared container. `care` collapses the term a second time for anyone whose primaries are not
Honor or Identity. **Two of four need terms return zero for every high-status character in this lane.**

**7.4 EXPOSURE has no row for a warrant held in another institution's custody.** The Crown's defining
structural fact — 14 §3.3's external consecration — is a *conferral basis*, not a dispensation term in
scope, so it generates **no computed need**. The design cannot make the King want the thing his office
depends on.

**7.5 `carry`'s "right of audience" is undefined everywhere.** Doc 05 §3.1 lists it as one of four
ways to hold standing at a respondent container. Nothing in the suite says who has one. **For a person
of the highest standing with no office it is the entire question of whether a political-up channel
exists**, and the fallback — the Crown's council — admits by the King's summons, per sitting.

**7.6 No mechanism writes a first weighted stance row for a person generated without Convictions.**
The seeding formula (02 §3.4) reads Conviction rows to produce a seed; with none, `seed_valence = 0`
and `seed_weight` clamps to 0; every pressure source in 02 §3.3 requires an existing stance, an
existing commitment, or deposits a claim rather than a stance. Doc 02 §8's generator would fill them
from the node's cohort centroid — **which forecloses canon's ED-618 emergence window on contact.**
The one live path is a negative write from an over-ask on the obligation edge.

**7.7 The suite carries two incompatible act economies** (§0), and it is worth one act per season per
Realm-rung office-holder, which is the difference between Almud THIN and Almud RICH, and between
Gerik Strand's canon trait being expressible and not.

**7.8 Canon's `certainty`/Truth stat has no home in the six person fields.** It is authored for
Thale (3), Voss (4), Kreutz (4), Reichard (5), Linder (5) and Elske (3, *"disrupted by hostage
status"*) — six of my eleven — and the nearest suite field, `credulity`, is pinned by 02 §3.2 to
exactly one reader with a warning against a second.

**7.9 Canon's flaw system is expressed as obstacle modifiers, which the suite refuses on principle.**
OVERPERFORMER, flattery −1 Ob, *cognition-heavy social contest target*. Docs 02, 12 §3.1 and 14 §1.2
all refuse flat shifts by the same arithmetic. Nothing has been supplied in their place.

**7.10 The obligation table has no row for a non-head parent and a minor child in the same hearth.**
Doc 04 §1.4 gives head→member 3.0, parent↔adult-child-separate-hearths 2.0, and affine 1.0. **Lenneth
cannot requisition Torben at any weight the table defines.** The Queen has no mechanical claim on her
own son inside her own house.

**7.11 An off-board address is outside every scope, so four modes are empty for anyone who marries
out.** Political-down is NULL by construction, Political-up is blocked at the carrier, and Argument,
Material, Coercive and Institutional have no object. **Off-board is 2 live modes of 8.**

**7.12 Two suite/canon collisions the seasons ran into.** Torben's location (suite: Altonian court as
collateral; canon: Royal Court, with the tutoring demand triggering at IP 30 against IP 20) — FINDING
1's shape, reported not repaired. And Almud's TS: I wrote **around** the 28-vs-0 contradiction for the
Knot claim, because both values sit below the ≥30 gate and the answer is identical either way; I
**branch** it for Thread-Read and rendering-facet registration, where `floor(TS/10)` gives pool 2
against pool 0 and 03 §9's floors are hard zeroes. The timeline additionally carries an explicit
supersession row dated 2026-04-11 naming TS 0 as the later value; **I record it and do not rule on it.**
