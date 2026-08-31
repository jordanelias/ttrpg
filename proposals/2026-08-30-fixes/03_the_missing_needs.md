# 03 — The Two Missing Need Formulas

## Status: PROPOSED (2026-08-30) — a fix, not a system. Nothing here ratifies on merge.
## Fixes: `09_GAP_REPORT.md` **D-3** · collision register **S15** (and, as a consequence, **S5** and **S20**)
## Composes on: `01_substrate.md` §2, §3, §5.2 · `02_the_person.md` §6 · `04_hearth_and_community.md` §1.2, §4.1
## `05_up_stroke.md` §1.1, §6.2 · `06_down_stroke.md` §3, §4 · `07_alignment.md` §1.1–1.3 · `15_adjudications.md` A-1, A-1b, A-2
## Sibling fixes filed alongside: `01_the_floor.md` (D-1) · `02_the_act_economy.md` (D-2) · `04_relational_at_settlement.md`
## (D-4, D-5) · `05_the_blocked_cores.md` (the §1 headline). This document does not duplicate any of them.
## Adds no object and no act. Two formulas, one range reconciliation, and one matching predicate that is
## genuinely new and is named rather than hidden.

---

## 0. What is actually missing, which is not quite what the report says

D-3 says `need(commitment)` and `need(exposure)` "are specified nowhere." That is nearly right, and the
residue matters, because it changes the fix.

`02_the_person.md` §6 **does** carry four lines of pseudocode for both terms. They are not formulas, for
three separate reasons, and each reason is something this document has to supply:

| §6 says | why it does not compute |
|---|---|
| `unmet = 1 if the LEDGER holds a claim that p is unsatisfied` | *unsatisfied* is not a predicate anywhere in the suite. A proposition is `(mood, subject, predicate, value, when, scope)` (08 §1.1); nothing says when a ledger row **satisfies** one. |
| `urgency = abs(Δ in the value of the person's reachable options under the asserted terms)` | a description of a quantity, with no scale, no denominator, and no statement of which claims supply the terms. |
| both | **neither emits a proposition.** 05 §1.1 is explicit: *"a need is a pair `(proposition, urgency)` where the proposition is a specific change to some container's terms that would satisfy it."* `shortfall(p, prop)` ranges over that proposition. A need term emitting only a number puts nothing on the act menu. |

So the honest statement of D-3 is sharper than the report's: **half the motive engine emits urgencies with
no propositions attached, and `petition` — the design's entire up-stroke — never enters a magnate's act
menu, because there is nothing for `shortfall` to range over.** That is why the duke's motivation is
uncomputed even though a number (`0.91`) appears beside his name in `05 §1.1`.

Both formulas below therefore emit **pairs**, and §5 shows the arithmetic recovering the suite's own `0.91`
from ledger contents rather than from an assertion.

---

## 1. Two preconditions, settled minimally

### 1.1 The range (closes S5)

Four sites, three ranges. `04 §1.2` returns `[0,1]` plus an unbounded coercive tail; `05 §1.1` compares
urgency against a reach in `[0,1]`; `13 §1` reads the same object; `02 §6` says `0..5`.

> **Ruled: urgency is in `[0,1]`. The unbounded tail above 1.0 belongs to `subsistence` alone, because only
> the body can produce a want that outranks every stance a person holds. `02 §6`'s `0..5` is retained as a
> display band, `band = round(5·u)`, and is not the quantity.**

This is the smallest available choice: three of the four sites already use `[0,1]`, and `02 §6`'s own lines
are already roundings of a continuous product. Nothing else moves. The tail stays exclusive to subsistence
deliberately — a design in which fear or duty can exceed hunger is a design in which the larder stops being
the generator, and that is `04 §1.2`'s N-line.

### 1.2 Satisfaction is a unification, and it is new machinery — named rather than hidden

`unmet` needs a predicate that does not exist. 08 §1.1 gets *collision* for free — *"`when` is a mandatory
interval, so assertion and denial collide automatically"* — but collision is not satisfaction. A claim that
the gate now admits without reading heritage does not merely fail to collide with the demand that it
should; it **discharges** it.

```
unify(c, P)   — the claim row c and the proposition P agree on (subject, predicate, when∩, scope∩)
                and differ only in mood. Existing tuple, existing interval intersection.

agree(c, P)  in [0,1] — how much of what P demands the value c asserts actually delivers:
                1              if P's value is atomic and c asserts it
                0              if P's value is atomic and c asserts otherwise
                |c ∩ P| / |P|  if P's value is a SET or a quantity   (fractional satisfaction)
```

`unify` is one matching routine over a tuple the substrate already carries. `agree` is a comparison the
substrate already needs for §3.3's assertion/denial collision, extended to sets. **This is the only new
machinery in this document, and it is a predicate, not an object.** Stating it is not optional: a session
implementing `need(commitment)` from the §6 pseudocode alone will invent an incompatible one.

---

## 2. `need(commitment)`

> *The gap between what a person has committed to and what that commitment currently demands of them — an
> unmet obligation to a proposition they hold.*

### 2.1 The formula

```
need(p, COMMITMENT):
  for each edge (p, f, d, avowal) with d > 0                       # 07 §1.2 — edges live on persons
    for each active proposition P of f                             # 07 §1.1 — the faction IS P
      emit ( P , u )   where

      u = w(d)/w(5)  ×  stance(p, P).weight / 5  ×  unmet(p, P)

      unmet(p, P) = 1                                  if p's LEDGER holds no row unifying with P
                  = 1 − confidence(c) · agree(c, P)    for the highest-confidence unifying row c
```

`w(d)` is 07 §1.2's table, unchanged and not re-weighted here: `0 · 0.15 · 0.40 · 1.00 · 1.60 · 2.20`.
`w(5) = 2.20` normalises to `[0,1]`. `stance(·).weight` is the one stance table of 01 §2, on `0..5`.

**Rows are ranked, never summed.** Each edge and each proposition emits its own row, and they compete for
the same act slot. Summing would make a man with six sympathies more driven than a sworn brother, which is
false about people and false about the setting.

### 2.2 Why it reads the view, and why that half is load-bearing

A-1 ruled commitment a view-read so that a treaty cannot change a person's wants before they have heard of
it. `unmet` is the whole of the view-read: a query against **p's own ledger**, and the substrate's §3.1
rule — that a view contains *nothing* rather than a blur — is what makes the default `unmet = 1`. A
Restoration member who has never heard whether any Einhir community governs itself feels the full weight of
the proposition. He is not uncertain; he simply has no row.

Three consequences fall out, none authored:

- **A lie can discharge a need.** `tell(speaker, hearer, "the gate now admits on work", as_asserted)`
  deposits a row that unifies with the Restoration's proposition. If the hearer's credulity and his stance
  toward the speaker carry it, his commitment urgency drops for as long as the row survives collision with
  the world. *The leader who says we have won* becomes a priced act with a real effect and a real failure
  mode, and nobody wrote it.
- **The two multipliers are not a double count, and the distinction is the point.** Stance is *what he
  wants*; degree is *what he has undertaken*. A man may hold a stance at 5 with no edge (he wants it and has
  promised nobody) or an edge at 5 with a decayed stance (he swore and stopped believing). The product makes
  both of those small and only the conjunction large — which is the mechanical shape of the sworn man who no
  longer acts and does not leave either, because departure is `commit(Δ = −d)` and costs him.
- **Fractional satisfaction gives a proposition a gradient.** A duke who has flipped two guild gates of
  twenty-one has moved his own need by two percent, which is why a reformer's second season looks like his
  first. Under an atomic `agree` he would feel nothing at all until the last gate fell, and reform would be
  motivationally invisible until it was complete.

### 2.3 Closed loop and N-line

- **Loop.** Produced at decision time from the person's own commitment edges and their own ledger rows;
  carried nowhere — recomputed, per 02 §6's refusal to store a need; consumed by `choose`'s option ranking,
  by 05 §1.1's `shortfall` (which needs the emitted proposition and had none), by 07 §1.2's `burden` term
  (*cost to the member's computed need*), and by the generator's constraint set.
- **N-line.** Cut it and an alignment edge is inert: joining a faction changes what a person may be *asked*
  and never what he *wants*, so every committed character is motivated only by his larder and his rank.
  Every magnate, every churchman and every movement leader falls to zero — which is the measured state D-3
  reports.

---

## 3. `need(exposure)`

> *The risk a person is carrying that they know about.*

### 3.1 The unification the design already needed

Two things wear the name **exposure** in the suite and have never been connected:

| | where | what it is |
|---|---|---|
| `exposure(edge)` | 07 §1.3 | `Σ over persons q holding a claim about a covert edge of confidence · hostility` — how blown a secret is |
| `need(exposure)` | 01 §2, 02 §6 | *what a dispensation's terms do to your options* |

They are the same shape: **a hazard, with a believed probability and a believed cost.** Treating them as one
term is what makes this a fix rather than an addition, and it is what the report's own framing asks for —
*the risk a person is carrying that they know about.*

Note also that `exposure(edge)` as written in 07 §1.3 is a **world read**: it sums over every person `q` who
holds a claim, including persons the subject has never met. That is A-2's banned object in a third disguise,
and A-1b named the missing distinction exactly — **world / view / another agent's interior.** Whether `q`
knows your secret is `q`'s interior. It reaches you only through a claim.

### 3.2 The formula

```
need(p, EXPOSURE):
  for each hazard h that p's own LEDGER names
    emit ( P_h , u )   where

    u = clamp(0, 1,  p̂(h) · loss(h) / worth(p) )

    p̂(h)    = p's OWN believed probability that h lands      — from ledger rows only
    loss(h) = EV(opening_set(p) | claims)  −  EV(opening_set(p) | claims ⊕ h)
    worth(p)= max( EV(opening_set(p) | claims), subsistence_floor(p) )
```

`opening_set` and its EV are 06 §4's routine, unchanged and not duplicated — *"a Dispensation changes
nothing about this routine; it changes `current_claims(person)`, and the routine, run again, returns a
different set."* The loss is the difference between the two runs, which 06 §4 was already computing and
discarding. `subsistence_floor(p)` is the person's own body and labour, which is never zero while they live;
without it the denominator vanishes at the exact bottom of the ladder (§7.2).

**Normalising by `worth(p)` is the design decision in this formula.** It means the same seizure terrifies a
man with one boat and barely moves a duke, and it means exposure is structurally the poor person's need
while commitment is structurally the committed person's — so the two are not computed on the same scale and
neither can dominate the other from above (§6).

### 3.3 The two hazard sources, both already in the corpus

**(a) Term hazards.** For each `Dispensation` claim in p's ledger whose `scope` contains p's address
(06 §1, §2 — publication is a telling, and it distorts):

```
p̂   = enforcer_presence AS P BELIEVES IT — the count of persons in the issuer's employ that p's own
      ledger names as present at his node, run through 06 §3's compliance term
P_h = ( the term, ought-not-apply-here, before the next standing date, OUGHT )
      — an exemption, a remission, a repeal: exactly the class of proposition 05 says people petition for
```

This is the term that pays for itself. **A decree nobody has been sent to enforce is not merely unenforced;
it is unfelt** — `p̂ ≈ 0`, so it generates no need, so nobody petitions against it and nobody evades it,
because nobody is afraid of it. 06 §8's reach cap, 14 §3.1's reach-as-persons, and *"a King's decree is the
least enforced instrument in the game"* all acquire a motivational expression they did not have, out of a
term that was already being computed for compliance.

**(b) Concealment hazards.** For each concealed thing p holds — a covert edge (07 §1.3), a `suppress`ed act,
an unavowed claim, an arrears balance (13 §8), a forged legitimation (04 §2.2):

```
perceived_exposure(p, x) = Σ over q such that P'S LEDGER holds a claim that q holds a claim about x:
                             confidence(p's claim about q's knowing) · hostility_as_p_reads_it(q → P)

p̂    = clamp(0, 1, perceived_exposure(p, x))
loss = Σ over m in JS of Δstance(m → p) under 04 §4.1, computed over the marks and stances
       P'S OWN LEDGER holds about those persons
P_h  = ( q, ought-not-hold, the claim )   — a PRIVATE proposition (05 §6.2), satisfiable by grace,
       by silence, or by a knife
```

That is 07 §1.3's formula with **one restriction** — the outer sum ranges over persons *p holds a claim
about*, not over all persons. The restriction is forced by A-1b rather than chosen, which is the best kind
of derivation available here: it is the same leak A-1, A-2 and A-1b each closed once, closed a fourth time
in the place nobody had looked.

Both the paranoid and the complacent fall out of it. A man whose ledger over-names his enemies carries a
crushing exposure need over a secret nobody is chasing; a man whose ledger is empty walks into an
investigation feeling nothing. Neither is a trait, and neither needed one.

### 3.4 The two hazard classes emit differently-shaped propositions, which is the anti-dominance result

A term hazard emits a **container-facing OUGHT**, which routes through 05 §1.1's `shortfall` to a
`petition`. A concealment hazard emits a **PRIVATE proposition naming one person**, which 05 §6.2 says is
satisfiable by grace only, and which therefore routes to `tell`, to requisition, to purchase, or to force.

**So exposure produces bribery and murder where commitment produces petitions** — one formula, two act
shapes, with the branch decided by which kind of hazard is on top of the ranked list. No act was authored
for either.

### 3.5 Closed loop and N-line

- **Loop.** Produced at decision time from the dispensation claims and concealment facts in the person's own
  ledger; carried nowhere; consumed by option ranking, by `shortfall`, by 07 §1.2's `burden`, and — via the
  emitted private propositions — by every act taken against a witness.
- **N-line.** Cut it and nobody in the game is ever afraid of anything they have not already been hurt by. A
  published decree motivates nobody until it is enforced against them; a covert operative feels no pressure
  until she is caught; concealment becomes free; and 07 §1.3's exposure/spend pairing becomes a bookkeeping
  fact with nobody who cares about it.

---

## 4. What the four terms look like together

| need | reads | emits | zero when |
|---|---|---|---|
| **subsistence** | the world (04 §1.2) | *the larder ought to be filled* | `margin ≥ 2` |
| **standing** | the world for the peer set, the ledger for the values (A-1b) | *the standing gap ought to close* | `care = max(Honor, Identity)/5 = 0` |
| **commitment** | the view | the faction's own proposition | no edge, no stance, or believed satisfied |
| **exposure** | the view | an exemption, or a private proposition naming a person | no hazard in the ledger, or `p̂ = 0` |

---

## 5. Three characters, with the arithmetic

Inputs are stated as ledger contents. Where the suite asserts a figure I try to recover it; where I choose
an input I say so.

### 5.1 Duke Magnus Vaynard — the magnate whose motivation was 100% uncomputed

`05 §1.1` hands him `urgency 0.91` on the proposition *the Masterpiece Examination's caste gate is abolished
across the realm*, with nothing deriving it. That is S15's whole complaint.

```
edge:    Path B, d = 5 (constitutive), avowed at publicity 2.0        w(5)/w(5) = 1.00
stance:  his own duchy's founding proposition, weight 5 / 5                     = 1.00
ledger:  21 guild gates named realm-wide. A firsthand claim, confidence 0.95, that
         2 of them now admit without reading heritage — the two his own Varfell
         dispensation reached (04 §5).
         agree = 2 / 21 = 0.0952
         unmet = 1 − 0.95 × 0.0952 = 0.9095

u(COMMITMENT, caste gate) = 1.00 × 1.00 × 0.9095 = 0.91
```

**The suite's own figure, recovered from ledger contents.** I do not claim these were the inputs `05 §1.1`
had in mind — it had none — only that plausible ones land on its number. And the arithmetic explains
something the suite asserted without deriving: his own reform barely moved his own need, because he flipped
two gates of twenty-one, and `04 §5` says the committees route the same exclusion through γ and δ anyway, so
even those two may not count.

```
u(EXPOSURE, Crown levy in scope):
  p̂    = his ledger names ~2 Crown agents reaching Varfell nodes he holds   → 0.15
  loss = arrears against the ducal larder, one reckoning                    → 0.06 × worth
  u    = 0.15 × 0.06 = 0.009 → 0.01

u(EXPOSURE, concealment) = 0   — he is avowed at publicity 2.0. Nothing is hidden.
u(SUBSISTENCE)           = 0   — margin ≥ 4
u(STANDING)              = 0   — care = max(Honor, Identity)/5 = 0 on his conviction vector
```

**Ranked: commitment 0.91 · exposure 0.01 · standing 0 · subsistence 0.** He is now motivated, entirely by a
term that did not previously exist, and the emitted proposition puts `petition` on his menu — the object
`05 §1.1`'s whole worked comparison depends on and could not previously produce.

### 5.2 Maret Uln — the covert operative whose agency in her own conflict was zero

The matrix's finding: *"her canon arc — dual loyalty, personal sympathy vs professional duty — resolves only
through somebody else's investigation. Her agency in her own defining conflict is zero,"* and S20 adds that
the burden term protects the arrangement, so it is permanently stable.

```
COMMITMENT — Restoration, d = 3 (member), covert
  w(3)/w(5) = 1.00 / 2.20 = 0.455
  stance    = 4 / 5        = 0.80
  ledger    = no row unifying with (Einhir communities, govern, themselves by consensus)
              → unmet = 1.00
  u = 0.455 × 0.80 × 1.00 = 0.364

COMMITMENT — her private edge to Vaynard, d = 2 (sympathiser)
  w(2)/w(5) = 0.40 / 2.20 = 0.182
  stance    = 3 / 5        = 0.60
  ledger    = he holds Varfell, confidence 0.90, agree = 1  →  unmet = 0.10
  u = 0.182 × 0.60 × 0.10 = 0.011

EXPOSURE — her covert Restoration edge
  perceived_exposure = (cell sister:  conf 1.00 × hostility 0.00)
                     + (a Goldenfurt informer she suspects: conf 0.40 × hostility 0.80)  = 0.32
  p̂    = 0.32
  loss = discovery costs the guild grade, the address and the marks (04 §9's exclusion),
         priced over the judging set she holds claims about                = 0.85 × worth
  u = 0.32 × 0.85 = 0.272

EXPOSURE — a Church visitation dispensation in scope, against a maximal mark_salience
  p̂ = 0.20 · loss = 0.50 × worth   →   u = 0.10
```

**Ranked: commitment(Restoration) 0.364 · exposure(covert edge) 0.272 · exposure(visitation) 0.10 ·
commitment(Vaynard) 0.011.**

Three things this produces that the matrix says do not exist:

1. **Her top two rows are within one act's reach of each other and pull in opposite directions.** Every act
   advancing the proposition raises somebody's claim about her; every act lowering exposure is an act not
   spent on the proposition. That is the covert operative's game, computed, per season, by her. *Her agency
   in her own defining conflict is no longer zero — it is the difference between 0.364 and 0.272.*
2. **The dual loyalty is latent, not stable.** The Vaynard row is 0.011 *because it is currently satisfied.*
   Threaten him and `unmet` jumps to ≈1, and the row goes to 0.109 — still under her Restoration row, but
   now competing with it. S20 said the burden term protects the arrangement, and it does: the burden term
   protects her from being *asked*. It never protected her from *wanting*, and until commitment computed
   there was nothing to want with.
3. **Exposure gives covert alignment the failure mode the matrix says it lacks** — *"no failure mode except
   discovery by a third party."* Now there is one that is hers: the exposure row rises with her own
   spending, and she can watch it rise.

### 5.3 Alvid Bekk — the unremarkable control

From the matrix: individual/hearth, rank 1, no alignment, no practice at rank ≥ 3, `mark_salience` 1.0,
margin 0.25 → Hungry, and *three of four needs return zero.*

```
SUBSISTENCE = clamp(0,1,(2.0 − 0.25)/2.0) = 0.875     # 04 §1.2, unchanged; matches the matrix
STANDING    = 0                                       # care = max(Honor, Identity)/5 = 0
COMMITMENT  = 0                                       # no edge — correctly: she has undertaken nothing

EXPOSURE — the fine from the landing
  p̂    = 0.70   her ledger names the reeve as present at the reckoning
  loss = 0.45 × worth   the fine takes her from Hungry to Failing
  u    = 0.315

EXPOSURE — tithe arrears approaching the distraint threshold (13 §8)
  p̂    = 0.35   she holds the priest's tolerance claims
  loss = 0.60 × worth   distraint takes the holding
  u    = 0.21

EXPOSURE — the quiet evasion, and Old Brun the ferryman who may have seen
  perceived_exposure = conf 0.50 × hostility-as-she-reads-it 0.30 = 0.15
  loss = 0.40 × worth   →   u = 0.06
```

**Ranked: subsistence 0.875 · exposure(fine) 0.315 · exposure(arrears) 0.21 · exposure(Brun) 0.06 ·
standing 0 · commitment 0.**

**The control goes from one live need row to four, and from one live term to two** — and the three exposure
rows emit three *different* satisfying propositions (remit the fine · forgive the arrears · Brun ought not
hold the claim), so `05 §1.1`'s `shortfall` puts three different petitions and one private approach on her
menu where before there was one act driven by hunger.

**This does not fix D-1, and must not be reported as if it did.** Her acts still do not propagate — that is
`mark_salience` = 1.0, untouched here. Her capability still yields no verbs — that is verb-gating at rank 3+,
untouched here. **Both of those belong to `01_the_floor.md`, filed alongside this**, and they remain the
report's priority. What changes here is only that the floor now *wants* four different things for four
different reasons — a mitigation of one symptom, from a document that was written for a different defect.

---

## 6. Dominance check

- **Petitioning.** The emitted propositions all route through `05 §1.1`'s `shortfall`, which is already
  checked, and whose gate is condition 2: the ledger must name a container as holding authority. Both new
  terms make more petitions *available*; neither makes any of them cheap. A petition still needs a carrier
  with standing and can still be dropped by a named man.
- **Lying to your own membership.** The commitment formula creates a new act with real force: assert
  satisfaction and your members' urgency falls. Not dominant — it is `tell`, so it is witnessable and
  traceable to a source row (01 §3.3); it decays as the world contradicts it (01 §3.2); and a leader caught
  doing it has spent his credulity weight with every member at once, because they all hold rows naming him.
  **But see §7.1 — it interacts badly with an unresolved item.**
- **Concealment.** Exposure makes hiding valuable, which is right, and makes it cost something *in the
  actor's own head*, which it did not before. Not dominant against avowal, because 07 §1.3 already prices
  the other side: a covert edge and a remit are near-incompatible, so concealment forecloses office.
- **Exposure against commitment.** The one real hazard was that exposure, bounded at 1 like everything else,
  would make every character a coward. The `worth(p)` denominator prevents it: exposure can only approach 1
  when the believed loss is the person's whole position, which is true of Bekk and false of Vaynard. **The
  two terms are computed against different denominators and therefore cannot dominate each other
  structurally** — which is why the duke is driven by his proposition and the fisher by her fine, with no
  class rule saying so.

---

## 7. WHAT THIS MIGHT BREAK

**7.1 The satisfying lie is stickier than it should be, and the reason is an open item.** Once `unmet` is a
ledger read, a *contradicting* claim from a hostile source runs into 03 §4's `stanceweight → 0.05` clamp —
convergence finding #1, six lanes of six. So a movement leader's comfortable lie is attenuated on the way
out by exactly the mechanism that buries every inconvenient truth. **This formula makes A-6b's unresolved
testimony half load-bearing on motivation, not merely on belief.** It was already a hole; it is now a hole
in the motive engine.

**7.2 Division by zero at the bottom of the ladder.** `worth(p)` is the denominator of every exposure row,
and a person who has been distrained, expelled and unhoused has an empty `opening_set`. The
`subsistence_floor(p)` term is what stops it, and it is doing real work rather than being defensive
punctuation — remove it and the poorest person in the game gets an unbounded urgency on every hazard.

**7.3 `unify` is genuinely new and it is this fix's soft spot.** Everything else here re-reads an existing
quantity. A matching predicate over `(subject, predicate, when∩, scope∩)` across a mood boundary has failure
modes nobody has explored: over-match and every faction's proposition is discharged by a vaguely related
rumour; under-match and `unmet = 1` forever, so every committed character is permanently maximal. **This is
the one place a second implementer will build something incompatible.**

**7.4 Cost.** `loss(h)` runs `opening_set` a second time per hazard per person per tick. A settlement of
individuated persons under three live dispensations enumerates options four times instead of once. Cohorts
(02 §7) absorb most of it — a cohort computes once at `weight` — but a crisis is exactly when a cohort
individuates, so the cost spikes precisely when the tick is already expensive.

**7.5 The range ruling touches published text.** `02 §6`'s `0..5` appears in that document and in anything
citing it. Recording it as a display band rather than deleting it is deliberate, so existing citations
resolve; but a reader who takes `0..5` as the quantity will over-weight every need term fivefold.

**7.6 Fractional `agree` makes a proposition's granularity mechanically load-bearing.** A proposition written
over 21 gates behaves differently from one written over "the caste order." Nothing in the suite governs how
coarsely a faction's proposition is written, and now the coarseness sets how fast a reformer feels his own
progress. That is a real authoring lever with no editorial rule behind it.

**7.7 Exposure reads `enforcer_presence` as the person believes it**, which is right, and which means a
character can be made compliant by a *rumour* of enforcers. That is good play, and it is also cheap for any
office-holder who works out that a false claim of a posted watchman is worth more than a watchman. It should
be cheap, for exactly the reason it is in the setting — flagged here so nobody later reads it as a bug.

---

*Two formulas, one range ruling, one matching predicate. No new object, no new act, no new field on a
person, nothing stored. Both terms read the view, per A-1, and both emit the `(proposition, urgency)` pair
`05 §1.1` requires and neither previously supplied.*
