# 01 — The Floor

## Status: PROPOSED (2026-08-30) — a fix to a design, not a new system. Nothing here ratifies on merge.
## Fixes: `09_GAP_REPORT.md` **D-1**, named there as "the most important defect in the report."
## Composes on (binding): `01_substrate.md` §2, §3; `02_the_person.md` §2.1–2.3; `03_knowledge_telling_investigation.md` §4, §5, §6; `04_hearth_and_community.md` §4.1; `15_adjudications.md` A-6 / A-6b
## Evidence: `2026-08-30-play-space-coverage/07_seasons_edges_and_ground.md` §II — the control's season, Alvid Bekk

**What this document is allowed to do.** Three edits, each to a formula or a gate that already exists.
It adds no object, no verb, no subsystem, and no act available to ordinary people that is not equally
available to a Duke. Two of the three edits make the design *smaller*: one deletes a gate and folds a
set of verbs back into the acts they were split from, one deletes a special case from a formula. The
third applies a ruling the register already made (A-6) and that never reached the document owning the
formula. **If a reader finishes this and cannot see what was removed, I have failed the brief.**

---

## 1. The defect is not a missing feature. It is three internal contradictions.

The gap report names two mechanisms. Both are places where the suite contradicts itself, which is why
the fix is subtraction rather than addition.

### 1.1 The rank-3 gate is a second class gate in a document that says it has exactly one

`02 §2.1`, on Thread Sensitivity: *"below TS 30 certain verbs do not exist for you at any rank. That is
P-08's inaccessibility, and it is **the one place this design gates a capability on something a person
cannot acquire**."*

`02 §2.3`, two hundred words later: *"At `rank ≥ 3` a practice adds verbs to the actor's option list,
and at rank ≥ 5 it adds verbs that cannot be attempted at all below that rank."*

That is a second class gate, and unlike the first it is undeclared. Its bite is exact and it is visible
on the control's sheet: **Alvid Bekk holds Cloth-work 2.** Against a person holding Cloth-work 0 she
differs by two dice on an attempt neither of them has a verb to make. A woman who has worked cloth
since childhood, one rank short of a threshold she has no route across, **mechanically has no craft at
all.**

### 1.2 The gate is a cliff, and the substrate refuses cliffs

`01 §1.4` refuses tiered factional growth on the ground that *"there is nothing to be discontinuous:
the same op, the same aggregation, the same read."* Rank 2 → 3 is exactly the discontinuity that
argument forbids, sitting on the other structure. One rank buys a whole verb; the two ranks below it
buy nothing at all.

### 1.3 The gate makes its own advancement rule unreachable

`02 §2.2`: *"A practice gains a rank when an attempt at a standard above its rank resolves and one of:
it was witnessed by a person holding the practice higher, or it failed at a cost the person actually
paid. There is no experience clock."*

Advancement requires attempting above your rank. For every verb the gate withholds, attempting above
your rank is precisely what you cannot do. **The ladder from 0 to 3 has no rungs.** A practice you do
not already hold at 3, you can never come to hold — by the design's own two rules read together.

### 1.4 `mark_salience` reads one referent kind out of the four the stance table has

`02 §3.1` establishes one stance table over four referent kinds — Person, Faction, Proposition, Place —
and argues at length that fusing them is correct *because every consumer reads the same two numbers*.
Publicity is a consumer, and it reads one kind:

```
mark_salience = 1 + 0.2 × (number of the ACTOR'S MARKS that any community member holds a strong stance toward)
```

Marks only. Not the proposition the act asserts, not the object it touches, not the place it happened.
So an act is audible in proportion to *who did it* and not at all in proportion to *what it was about*.
For a person with no house name, no grade and no stigma, the term is `1 + 0.2 × 0 = 1.0` for every act
she will ever perform, and `04 §4.1`'s own band table then reads: *"< 0.5 — the hearth, and whoever
holds a Knot."* She holds none. **Being ordinary is being inaudible, permanently, whatever she does.**

### 1.5 And one consequence that ties the two mechanisms together

`01 §2`'s fourth need term: `need(exposure)` is *"what a dispensation's terms do to your options."* It
is a functional of the option set. The control's season computes it at ≈ 0.4 and says why: *"her
reachable options number eight and almost none has a value any term can move."*

**An empty verb set zeroes a need term by construction.** One of the three zeros in the control's motive
engine is not a separate defect awaiting D-3's missing formulas; it is the first mechanism observed at
the other end of the tick. Fix the verb set and `need(exposure)` starts returning numbers without anyone
writing a formula for it.

---

## 2. What an ordinary person holds that is scarce

The gap report's §2 is the strongest clue in the exercise and it should be read literally. Among the
postless, four holdings predict RICH: **a channel, a custody, a gate, or a unique root.** Everyone
holding one is RICH; everyone holding none is THIN or worse.

| holding | who has it | how it is obtained | Alvid Bekk |
|---|---|---|---|
| **channel** | Gerik Strand, Thale, Maret Uln | a Knot (TS ≥ 30 both ends), or an office's relay | **no** — TS 4, both slots permanently unfillable |
| **custody** | Queen Lenneth (the archive), the Dicastery of Doctrine and Archives | conferred by an institution | **no** |
| **gate** | Almstedt (the agenda), any committee seat | conferred by admission | **no** |
| **root** | Old Brun — and, found by the exercise and left unpriced, **Alvid** | **minted by being there** | **yes** |

**Three of the four are conferred and one is minted, and the one that is minted is minted at the
bottom.** That sentence is this document's whole positive claim, and every part of it is already in the
suite:

- `03 §5`: *"**`witness` is the only operation that MINTS a root token.**"* Not `tell`, not `research`,
  not `reconstruct`, and not a Knot deposit — which reuses the originating event's id precisely so that
  bonded partners cannot manufacture support. There is exactly one mint in the game and it requires a
  body at a place at an hour.
- `08 §4.1`: grade is a pure function of root structure. **G2** is one firsthand claim; **G3**,
  *Corroborated*, is two claims whose firsthand roots **differ**; and `08 §4.2`'s article count must be
  met by grounds that each independently reach the venue's floor, because grade does not average. A
  second root is not a bonus. It is the difference between a ground that stands and a ground struck
  permanently.
- `14 §1.3`: an office-holder **cannot act quietly** — every act by remit runs at `venue_factor ≥ 1.0`.
  The powerful are therefore structurally absent from the places where scarce roots are minted: the
  night landing below the ford, the sickbed, the back kitchen, the road. What they send instead is
  their establishment, and an establishment is made of ordinary persons.

The control's season states the consequence and then walks past it: *"the poorest person in the town
holds the most valuable claim in it… the bottom of the ladder is where the roots are, **and
root-holding is not an act**."*

**The closed loop, which needs no new object:**

- **Producer** — `witness(person, event) → claim`, the game's only mint, requiring presence.
- **Carrier** — the `firsthand(e)` row in that person's ledger, and the opaque rootprint that travels
  with every telling of it (`03 §5`).
- **Consumer** — `support(C)` counts distinct root tokens → `corroboration_multiplier` → `08 §4.1`'s
  grade → a venue's admission floor → a disposition: a fine remitted, an article proved, a custody
  attacked.

**N-line — cut the ordinary person's root and you lose:** any reason a person above the ladder's middle
ever needs a person below it for anything but compliance. `interview` and `surveil` have no targets
worth their exposure, G3 is reachable only by people who can afford to be in two places at once, and
every transaction between rungs runs downward. The peninsula becomes a set of magnates acting on each
other over the heads of a population that is scenery.

**This needs no mechanism. It needs three formulas to stop suppressing it**, which is §§3–5.

---

## 3. EDIT 1 — rank supplies dice. It does not gate a verb.

**Delete the "Reach — verbs" half of `02 §2.3`.** Replace it with nothing; fold the verbs it named back
into the acts they were split from.

```
option_list(p, n) = { a ∈ ACTS : eligible(p, a, n) }

eligible(p, a, n) consults:   remit               (14 §1.1 — office)
                              marks               (grade, house, Church standing, office; 02 §1)
                              place               (presence; 09 §1.4 stratum 1)
                              the claims p holds  (03 §4.1 — you cannot act on what you do not know of)
                              class gates         — of which there is EXACTLY ONE: Thread Sensitivity
                          and NOT practice rank.

pool(p, a) = attr[triad_axis(a)] + practice[a].rank + thread_pool      (unchanged, 02 §2.3)
```

Every act formerly listed as "added at rank 3" or "added at rank 5" folds back into its base act as a
**declared standard**: `commission on speculation` stops being a verb Bergthor Kelm cannot see and
becomes a standard of `commission` that anyone may declare and almost nobody can meet. The resolver
already prices standards (doc 10). **The act vocabulary gets shorter.**

**What still shapes an option set — and this is the better claim.** `14 §1` argues that an office *adds
no verb*: it makes ordinary acts eligible where they otherwise are not. This edit is the same argument
applied to capability, and it makes the design's political statement cleaner than the one it replaces:
**your option set is shaped by your social position — your marks, your remit, where you are standing,
what you have been told — and not by how good you are.** A journeyman may attempt the Free Master's
commission; what stops him is the *guild's* rule, which is `04 §4.2`'s admission machinery, six
persons' stances and a grade mark — a gate with a holder, a price and a grievance, exactly as `03 §6.2`
promises every gate in this design is.

The one gate that survives is the one the design declared. Alvid Bekk cannot Thread-Read at TS 4, this
season or in thirty years, and that stays true.

**What it costs, immediately and in the right direction.** `02 §2.2`'s advancement rule becomes
reachable at rank 0, which it currently is not. Alvid may declare a standard above Cloth-work 2, fail
it, pay for the failure and advance — the only advancement route the design has, which the gate was
closing against exactly the people who most need it.

**Dominance check.** This adds no gain-shape; it widens a set. Gap report §2's finding 1 —
*"dominance, not scarcity, is what makes a season thin"* — points the same way: every RICH character
cites three or more live modes or four differently-shaped acts. Widening Alvid's set moves her toward
that criterion and away from the one act (`foster out`) that currently dominates her. The hazard is that
a widened set contains a *new* dominant act; §8 audits it.

---

## 4. EDIT 2 — publicity and attention read the stance table, not the actor's marks

**Replace `mark_salience` with the same sum taken over the referent kinds the stance table already
carries.** The name goes with it, because the term is not about marks.

```
referents(act) = marks(actor) ∪ { proposition(act) } ∪ objects touched ∪ { place }
                 — exactly the four referent kinds of 02 §3.1's one table

act_salience(act) = 1 + 0.2 × | { r ∈ referents(act) : ∃ p ∈ JS(act) with |stance(p, r).valence| ≥ 3 } |

publicity(act)    = venue_factor × √(witness_count) × act_salience(act)     (04 §4.1, otherwise unchanged)
```

And the same generalisation in the other direction, on the attention floor inside `04 §4.1`'s `hears()`:

```
θ(p, act) = θ(p) / ( 1 + 0.2 × | { r ∈ referents(act) : |stance(p, r).valence| ≥ 3 } | )
```

One change, two directions, and both are the removal of a special case: publicity was reading one
referent kind out of four, and attention was reading none.

**Worked twice on the control's own season — and the first case is the control on my own fix.**

*Her foster-out.* Referents: her three marks (no member of the ford-side congregation holds a strong
stance toward any of them), `prop: fostering a child to kin` (nobody), her sister Gerd, the hearth.
Strong referents: **0**. `act_salience = 1.0`. `publicity = 0.2 × √3 × 1.0 = 0.35`. Below 0.5. **The
most consequential act of her life still reaches nobody.** The fix does not raise a floor; an
unremarkable act stays unremarkable — and if it did not, the fix would be a notability stat in disguise.

*Her telling about the ford.* She tells Bailiff Konrad Ems what she saw twelve days ago, at the landing,
with four people in earshot. Referents: `prop: the ford traffic` (Ems +5, Magistrate Hedda Vorn −5,
Curate Wessel +4), Tomas Vorn as the claim's object (strong on all three), the ford itself (contested
since the toll rose), her heritage mark (0). Strong referents: **3**. `act_salience = 1.6`.
`publicity = 1.0 × 2.0 × 1.6 = 3.2` → `04 §4.1`'s top band: *settlement-wide, and along every Knot
immediately.* **The unmarked woman is heard across Goldenfurt, because of what her act was about and
not because of who she is.**

**The price arrives with the audibility, out of the same term.** Hedda Vorn is inside that band. Alvid
does not get amplification; she gets *exposure* — and `04 §4.1`'s judging-set deposits are divergent by
construction, so the same publicity that carries Ems's +3 carries the magistrate's −4 and hands a woman
who was previously beneath notice a named enemy holding a rank-4 office. No new cost mechanism was
needed, because publicity has never been a gain. It is an amplifier of an act's own sign.

**The caste effect the original term existed for is unharmed.** Maret Uln's transgression still travels
twice as far as her neighbour's, because her heritage mark is a referent toward which half of Varfell
holds `|valence| ≥ 3` — it enters the sum as a mark, in the first clause, unchanged. What changes is
that a mark is no longer the *only* way into the sum. Duke Magnus Vaynard still cannot act quietly north
of his fjords. The Confessor's visitation is still loud.

**And it corrects a selection pressure the control's season flagged and could not fix.** `07 §II P7`:
*"the cheapest way for an ordinary person to stay a person is to do something people talk about, and
what people talk about is transgression… the reference-count bound is correct and it quietly selects
for the criminal over the quiet."* Under the old term an ordinary person's only route to publicity was
witness count and venue — a crime in a square. Under this one, **charity at the granary during the
Goldenfurt reckoning is as audible as theft from it**, because both touch the same contested
proposition. The selection pressure goes to neutral without anyone adding a rule about virtue.

---

## 5. EDIT 3 — apply A-6's firsthand floor, which was ruled and has no owner

This is not a proposal. `15_adjudications.md` A-6 ruled it, and A-6b records that it was never applied:
*"the accepted half of A-6 is a ruling with no owner in the design… Carrying it into 03 is outstanding
work, not a settled fact."* The gap report §7 lists it among its own zero-applied dispositions.

In `03 §4`, the salience formula, on the `firsthand` source class only:

```
salience(c) = recency × confidence_live × relevance × stanceweight              # told_by, inferred — UNCHANGED
salience(c) = max( that product, recency(c) × confidence_live(c) )              # firsthand — A-6's floor
```

**Why it is the third edit and not the first.** The control's landing claim currently scores
`0.6 × 0.9 × 0.05 × 0.05 ≈ 0.0014` and ranks about fortieth of sixty. Under the floor it scores
`max(0.0014, 0.54) = 0.54` — and A-6b is right that this is a floor on *ranking*, not a guarantee of
inclusion. It now competes against her other recent firsthand claims, which are also floored: bread is
dearer (≈ 0.95), the reeve collected in the square (≈ 0.9), the carting is short (≈ 0.9). It lands
somewhere in the low teens against K = 12. **That is a fix which nearly works, and shipping it alone
would be worse than useless.**

What carries it over is EDIT 1, through the `relevance(c, q)` term. Relevance is measured against the
pending decision, and the pending decision is drawn from the option set. With the rank gate deleted and
`act_salience` making the telling consequential, *what to do about the landing* is a live option with a
real value — so relevance rises off 0.05 and the stance-weighted product itself climbs. The floor is
what holds the claim in contention long enough for that to happen at all.

**The three edits are one fix, and each is insufficient alone.** EDIT 1 gives her acts whose objects
exist. EDIT 3 lets the claim those acts are about reach her own working set. EDIT 2 lets the act, once
taken, be heard by anyone who cares. Ship any one and the season barely moves; ship all three and the
loop closes: *presence mints a root → the floor surfaces it → the widened option set makes acting on it
worth ranking → the act's referents make it audible → someone who wants it comes looking.*

---

## 6. The control's season, re-run

Alvid Bekk. Same hearth, same larder, same TS 4, same rank 1, same absence of house, grade, alignment
and Knot. Nothing has been given to her.

| | before | after |
|---|---|---|
| live acts | 8 | ~13 — every act whose only bar was rank, at base standard |
| differently-shaped acts | 2 (a transfer, a plea) | 4 — material/craft, epistemic-with-a-price, political-up, relational |
| `need(exposure)` | ≈ 0.4 | real, and moved by the ford toll, the grain levy, the bread price and the guild's idiom clause |
| the ford claim | 40th of 60, unreachable | in contention, and relevant once acting on it is an option |
| her foster-out's reach | the hearth | the hearth — **unchanged, correctly** |
| her telling's reach | she had no reason to | settlement-wide, and it makes her an enemy |
| dominance | `foster out` dominates: material, immediate, repeatable, unpriced | no single act dominates; `foster out` is still unpriced and still a defect (§8) |

**What has not changed, and should not have.** She is still Hungry. She is still rank 1, so `05 §6.4`
still puts her at `gap = 3` to Magistrate Hedda Vorn — supplication only, carried, through an
intercessor whose own gap is ≤ 2 — and in Goldenfurt that is still **Curate Wessel and nobody else**,
and Wessel still informs for the Himmelenger Inquisitor. Her Knot slots are still permanently empty.
The parish is still her only community. The caste structure is untouched. What has changed is that she
now holds something the men on the other side of it want, and a voice that carries when she spends it.

**She is not RICH by rescue.** She is RICH by the exercise's own criterion — four differently-shaped
acts, no dominance — and her season now states a dilemma the old one could not: *spend the root, and to
whom.* Ems will pay in a levy assessment. Wessel will pay in intercession and will also pass it to the
Inquisitor. Hedda Vorn will pay to have it never spoken, and she is the person who decides the fine
Alvid's own petition would contest. Withholding costs a season and keeps it worth something. **Old
Brun's fork — "the season he spends it he becomes the control" — is now every ordinary person's fork,
and it is a fork rather than a wall.**

---

## 7. What I refused to build

Each was considered and cut, and each is a way this brief could have been satisfied by authoring.

- **A verb, or a set of verbs, for the postless.** The failure the brief names. It breaks *one actor,
  composed primitives*, and would make a Duke's acts a proper superset of nothing — the shape `14 §1`
  exists to refuse.
- **A witness market, a testimony object, an informant contract.** All three already exist as
  compositions. `interview` (`03 §6.1`) is how the powerful come asking, and it already deposits
  `INTENDS(you, investigate X)` into the target, which is how Alvid learns Ems needs her. Her answer is
  `tell`, `conceal`, a lie, or silence. If she wants terms, `08 §6`'s accord with `record_custody =
  none` is a two-party agreement whose breach costs only regard with those who learn of it. Nothing is
  missing.
- **A floor on `mark_salience`, or a minimum publicity.** A floor makes every act audible, destroys
  `04 §4.1`'s bands, and hands quiet people the aristocracy's amplification for free. EDIT 2's worked
  foster-out is the test I held myself to: an unremarkable act must stay unremarkable.
- **A notability, obscurity or renown scalar.** `04 §11` already refuses a prestige currency and `01 §6`
  refuses faction-wide reputation, for the same reason: a number with no holder of an opinion.
- **Lowering the TS ≥ 30 Knot gate.** Five lanes converged on that gate as a problem and `02 §11.2` asks
  explicitly that it not be "fixed". It is also not D-1: Alvid's inaudibility is a formula reading one
  referent kind, not a threshold. Leave it. If it is wrong it is wrong on its own evidence.
- **A `sell labour` verb, a wage, or a construction act.** Real absences — the control's season shows
  Nils's carting feeds roughly a third of that hearth with no term in the formula for it, and the
  difference is a whole larder band. That is **D-10**, it belongs to `13_material_life.md`, and taking
  it here would be scope drift dressed as thoroughness.

---

## 8. Dominance audit of the fix itself

Per `14 §9`'s R-criterion: an option is structurally dominant when its gain compounds against a cost
that decays or is absent.

**Spending a root.** *Gain:* one-shot, and it is spent — `03 §5`'s support counts *distinct* tokens, so
telling the same root to a second buyer adds nothing to anyone's grade, and the second buyer knows it.
*Cost:* compounds — you are named as source in every downstream `told_by` rootprint, you are audible to
the person who wanted it buried (EDIT 2), and `03 §7`'s exposure accrues to whoever is now investigating
you. Decaying gain against compounding cost. **Not dominant; if anything the conservative play is to
hold.**

**Withholding a root.** *Gain:* the option stays open and its price can rise as a standing date nears.
*Cost:* compounds — `03 §6.1`'s `retention(f)` decays the physical facets that would corroborate you, so
your reachable G3 degrades toward a bare G2 while you wait, and somebody else may mint the second root.
A real race, both arms priced. **Not dominant.**

**Declaring a standard above your rank (EDIT 1).** *Gain:* compounds — advancement, which is the only
route the design has. *Cost:* compounds — you fail publicly at a `publicity` that EDIT 2 has just made
responsive to what the attempt was about, and `04 §4.1`'s judging set deposits the failure into everyone
who heard. The Masterpiece Examination is the extreme case and is already priced that way.

**Touching a contested referent to be heard (EDIT 2).** Not an act — a property of acts. It amplifies
sign, not value, and `03 §5`'s synthetic-root rule caps repetition: one story told three times
corroborates once, and every retelling of a rumour hashes to the same σ. There is no way to manufacture
audibility by volume.

**The act that still dominates, and it is not mine.** `foster out` remains what the control's season
found: material, immediate, repeatable while children remain, and priced at nothing in `04 §2.2`'s own
table. This fix does not repair it; it surrounds it with acts of comparable value, which flips a THIN
verdict without closing the defect. **Say so plainly rather than let the verdict change hide it.**

---

## WHAT THIS FIX MIGHT BREAK

Honest list. Each is a place elsewhere in the suite this puts under pressure, whether or not it breaks
outright.

1. **`02 §2.3`'s N-line loses half its subject.** The section claims *"the capable person changes the
   option set and the pool source, never adds a flat bonus."* After EDIT 1 the first clause is false and
   only the pool-source clause survives. The clause is worth keeping as the *office* claim (`14 §1`) and
   worth deleting as the *capability* claim — and somebody must actually edit doc 02 rather than leave
   two documents disagreeing. **A ruling that does not reach the formula's owner is what A-6 already did
   to this suite once.**

2. **`02 §2.3`'s worked example needs re-homing, and it is load-bearing on the guild.** The Free Master
   / journeyman `commission on speculation` example becomes a grade gate held by the Kettlemakers rather
   than a rank gate held by the resolver. Better placed — but somebody must then write which guild rules
   gate which standards, and the risk is that this quietly becomes a table of authored permissions. It
   should be a **dispensation** issued by the guild warden and contestable at the guild's standing date,
   or it is the caste table under another name.

3. **Doc 10's standard ladder inherits work it may not have.** EDIT 1 moves the whole of *how hard is
   this for someone who cannot do it* onto the resolver's standards. If those bands are coarse, an
   unpracticed attempt at a master's standard will read as merely unlikely rather than hopeless, and the
   fix will have converted a hard gate into a soft one *too* softly. This is the edit's real risk and it
   is measurable: run an unpracticed attempt at a rank-5 standard and read the band.

4. **`04 §12`'s challenge 3 is answered, and the answer costs that section its argument.** It defends
   `mark_salience` as a necessary addition to the substrate's account of marks: *"without it, a house
   name changes how you are judged but not how far word of you travels."* After EDIT 2 the term is not
   about marks, and the defence must be rewritten — marks become one of four referent kinds and the
   aristocratic effect a consequence rather than a premise. The behaviour survives; the argument for it
   does not.

5. **Publicity gets more expensive to compute, and the cost is per-act-per-hearer.** `act_salience`
   quantifies over the judging set, which `04 §4.1` already did — but `θ(p, act)` now varies per person
   *and* per act, where θ was previously per person. `09 §10`'s budget covers ~17,000 acts a season;
   this multiplies an inner loop rather than an outer one, and somebody should check it against
   `11_code_shape.md`'s per-tick budget rather than take my word for it.

6. **A-6b's unresolved half becomes more exposed, not less.** EDIT 3 applies the firsthand floor and
   leaves testimony under the 0.05 clamp — exactly the half A-6b says was never resolved. With firsthand
   claims floored, the *gap* between what you saw and what you were told widens, so 09's original case —
   *a sixty-year-old revelation must move people who do not want to be moved* — gets harder, not easier.
   This fix makes an open question more urgent. It does not answer it.

7. **It pushes on D-3 without fixing it.** `need(exposure)` starts returning real numbers because the
   option set widened, so the two need terms that *do* have formulas will now dominate a commoner's
   motive engine even harder relative to `need(commitment)` and `need(standing)`, which still have none.
   A duke's motivation stays 100% uncomputed. **This fix improves the floor and widens the distance
   between the floor and the ceiling, in the one place the design most needs them to be the same
   machine.**

8. **It does not touch `care`, and `care` is a four-lane convergence.** `need(standing)` still returns 0
   for Alvid because `care = max(stance[Honor].weight, stance[Identity].weight)/5 = 0.2`, and the
   Conviction profile supplying Honor or Identity is seeded into cadets, guildsmen and nobles. Two of the
   control's three zeroes survive this document. I fixed the one caused by the defect I was given and
   left the other two where they belong.

9. **The parish collision the control's season reported is still open, and this fix leans on it.** EDIT 2
   quantifies over `JS(act)`, and Alvid's judging set is her parish congregation — whose membership rule
   is presence over a district, which `07 §II §1` shows cannot coexist with single-parent containment for
   a Kettlemaker's hearth. My worked numbers assume the parish is her community. Resolve it the other way
   and the ford-side congregation is not a community, Alvid has none, and **she has no judging set for
   `act_salience` to quantify over at all.** This is the largest single dependency in this document, and
   it is somebody else's ruling.

10. **It makes the ordinary person worth investigating, which arms every inquisitor in the setting.**
    Once roots at the bottom are reachable and audible, `surveil` and `interview` against commoners
    acquire a payoff they did not have — and the two bodies best resourced to spend acts that way are the
    Himmelenger Inquisition and Niflhel. That is the correct consequence and it is not a comfortable one:
    this fix gives the powerless a voice and simultaneously gives the powerful a reason to come for them.
    Nothing in the suite currently prices what an Inquisitor's sustained attention does to a hamlet.
