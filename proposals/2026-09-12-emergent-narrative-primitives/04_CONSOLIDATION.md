# Part D — the three later documents, and the consolidation of all seven

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠⚠ **SUPERSEDED BY `proposals/2026-09-12-emergent-narrative-primitives-v2/` (same session, same
`ED-IN-0217`).** This set applied the wrong test: it disposed of mechanics on **architecture rules** and
**implementation facts** as though those refuse an idea, which they do not — and it never cited **`R2`**,
the ruling that makes every refusal *instrumental, not terminal* and requires each to be **argued** against
five terminal properties (`references/design_rulings_2026-09-06.md:37-50`). Its facts are largely sound and
its citations reproduce; **its verdicts do not follow from them.** Kept as the audit trail. Read
`…-v2/02_THE_RESCORE.md` for what changed and why, and `…-v2/01_THE_TEN.md` for the set that replaces this
one.


Three further documents, cut against the same ground Parts A–C verified at `file:line`, then all
seven consolidated into one frame.

---

## §1 · WHAT THE THREE DOCUMENTS ARE

Two are **earlier revisions of documents Parts A–C already audited**. One is **new and carries six
proposals that appear nowhere in the first four.**

| document | relationship | the count that establishes it | how to re-run it |
|---|---|---|---|
| *Thirteen Strategy Games… Analysis* — Stages 1–5, Clusters A–G, letter grades | **earlier draft** of the audited *Parts 1–6 / axes I–VII / primitives A1–H4 / rubric out of 40* revision | **0** provenance tags against **17** | `grep -c 'SOURCE: T[0-9]\|TIER-FLOOR'` on each |
| *Citizens, Settlements and Factions: A Systems Teardown of Nine* — five axes, ten transferables | **earlier draft** of the audited *Parts 1–7 / seven axes / eight graded transferables / nine directives* revision | **5** distinct `Axis N` against **7**; **0** `Part N` heads against **7** | `grep -o 'Axis [0-9IVX]\+' | sort -u | wc -l` |
| **Twenty Games, One Frame** — the reconciliation | **NEW.** Not a revision of anything audited | its six proposals — *The Lean Years · Slander · The Queen's Table · Two Ledgers · The Migrant Question · The Levy* — appear in **0 of the 4** audited documents, checked by name | `grep -il` each title across all seven |

**The seven sources are not in this repository**, so those counts are not re-runnable from the tree
alone. They are re-runnable by anyone holding the same files, and the files are pinned here by
SHA-256 prefix and byte length so that "the same files" is checkable rather than asserted:

| source | sha256 (first 16) | bytes |
|---|---|---|
| *Emergent Narrative in Games: A Cross-Medium Research Compendium* | `2f4cedecaeb5981b` | 68,573 |
| *Emergent Narrative: Mechanical Specifications* | `04e6f281fa0331fc` | 82,477 |
| *Thirteen Strategy Games* — audited revision | `8d9b26a67ac53d8c` | 103,473 |
| *Thirteen Strategy Games… Analysis* — earlier draft | `5ab41cb1447aa023` | 64,097 |
| *Citizens, Settlements and Factions — Nine Titles* — audited revision | `b0714ed1aa6b7314` | 76,432 |
| *…A Systems Teardown of Nine* — earlier draft | `73ebd4eb1f35fc65` | 52,113 |
| **Twenty Games, One Frame** — the reconciliation | `5cbb17cf8571d6ae` | 64,665 |

**So the teardowns were audited in their later and better-sourced revision, which is the right one to
audit.** What the three later documents add is the consolidation's own contribution: **six
cross-pollinated proposals, a nine-item asymmetry map, and a re-grading pass.** That is what §2–§4
treat.

⚠ **A conflict the two nine-titles revisions carry between them, unresolved in either.** The earlier
states the Banished die-off period as **"~60–80 years later"**; the later as *"twelve to sixteen
in-game years."* These are not the same claim — the later figure is the in-game-years cycle at the
5:1 ageing ratio, the earlier the citizens' own lifespan. Both can be true of different quantities,
and **a reader taking either as "the cohort period" without the ratio will mis-size a loop by a factor
of five.** `[CONFLICT: cohort period — 60–80 years vs 12–16 in-game years — unresolved in the sources;
they appear to measure lifespan and cycle respectively]`

---

## §2 · THE CUT, RUN ON THE SIX NEW PROPOSALS

`skills/ners/SKILL.md` §2: propose the cut, name what dies. Each proposal is cut against the Valoria
ground Parts A–C verified at `file:line`. **The result inverts the consolidation's own ranking**, and
that inversion is this part's product.

### C · "The Queen's Table" — the document's **A−**, its self-declared strongest. **Valoria's most comprehensively refused.**

**GRADE: `paper`** — no component executes here, and three of five cannot.

Five components. **Three hit a distinct named refusal; one is inapplicable; one is a false N-line the
first four documents already produced.**

| component | verdict | the line that refuses it |
|---|---|---|
| Three inverse-linked global meters (**Standing · Patience · Suspicion**) | **REFUSED** | `state/carriers.py:579` — *"S10.1 — a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy. **EVERY ONE IS A QUERY**"*; `:586` — *"L3 — every aggregate is a function, never a field."* And Jordan's **R7**: *"no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED."* |
| **Patience** as a shared loss timer | **REFUSED — but on `T-a`/`L3` or `T-b`, never on `T-c`** | see the note below; the theorem matters more than the verdict here |
| **Reckonings** score the table and wipe the board | **REFUSED — the score and the automatic wipe, not the sitting** | `AX-6` (`01_AXIOMS.md:187-188`) — nothing becomes permanent without an author; `AX-3` (`:115`) licenses a clock only to **REMOVE**, never to REVISE. ⚠ A *convened* sitting that decides is lawful and is `H-32`/`W7`'s shape (`loop/effects.py:181-183`) |
| **Meta-progression** across runs | **INAPPLICABLE** | Valoria is one persistent campaign. A reset is a design change, not a primitive to adopt |
| **Rule-bound automatons** in Wakhan's mould | **FALSE N-LINE** — and it is Part A row 16 arriving from a second document, not a new one | `AX-1` + `architecture/PLAN.md:438` — every character runs the same `choose`; a player-only mechanism is forbidden. `View.__getattr__` raises on any world reach (`carriers.py:225-230`), so *cannot cheat* is structural **by type** |

⚠ **The loss timer is refused, and the axiom usually cited for it licenses it.** `T-c`
(`01_AXIOMS.md:304-316`) is *"every clock outside the three was wound by a nameable act, and
therefore has handles"* — and it states the consequence as the design's **best single property**: a
wound clock can be *"bribed, delayed, burned, or killed."* `T-c` therefore **admits** an authored
timer. The phrase *"a quantity advancing with no author"* belongs to **`AX-5`** (`:157-158`), not
`T-c`. So Patience is refused on exactly two available grounds, and both are narrower than the
sentence usually reached for:

1. **as a self-moving magnitude** — `T-a`/`L3` plus R7, which is the meters row again, and
2. **as an expiry that PRODUCES the loss** — **`T-b`** (`:284-286`): *"a threshold may change what
   can be chosen; it may never produce an outcome."*

**And the licensed form is already shipped.** A `Date` is written only by `convene`
(`write_matrix.yaml:98`, `loop/effects.py:188`), comes due in `loop/calendar.py:31`, and raises a Q1
question at `queries/world_q.py:196`. `effects.py:181-182` states the discipline in its own words:
*"`convene` puts a date on the calendar and stops, which is `L5`: a clock may not produce an
outcome."* **Valoria's answer to a shared deadline is a convened date with an author and handles —
which is what `T-c` promised, running.**

**The finding.** The consolidation grades C highest *because* both halves are shipped and proven
elsewhere, and *because* it avoids the AI-competence problem rather than solving it. Both reasons are
sound and neither survives contact with this tree: the shipped halves are shipped in designs that
permit stored aggregates and a reset, and Valoria's answer to the AI problem is structural.

⚠ **One direction in which Valoria's automaton is *weaker* than Wakhan's, and it is an `E` finding.**
*Cannot cheat* is stronger by type than by rulebook. **Legibility is not.** Wakhan's automaton is
readable *because* it is a rulebook: a player can predict it. Valoria's `choose` separates only 2–7
of 22 candidates by conviction and orders the rest by draw
(`engine/season/hole_register.yaml:1281`), so an observer cannot reconstruct why an act was picked.
Against §0.06's **E** — *"allows the player to intuit complex outcomes from simple choices"* — Wakhan
passes and this tree does not yet. **A proposal's strength in its own corpus says nothing about its
adoptability here; and a refusal's strength says nothing about the axis it does not cover.**

### A · "The Lean Years" — **B+. Splits three ways, and one third is a genuine gain.**

**GRADE: `paper`** — four components; the one that is licensed is licensed and unbuilt.

| component | verdict | ground |
|---|---|---|
| Anonymous cohort-aged population, citizens unaddressable | **ALREADY PROPOSED, graded `paper`** | `proposals/2026-09-10-…/02_PROPOSALS_SUBSTRATE.md:142-254`. And `Rung.envelope` is the population carrier with zero writers; `Person.weight` is an *acting crowd* (S9.1), a different object |
| Eight hard-capped named stewards | **FALSE N-LINE on the cap** (Part A row 20, second document); **blocked on `H-71` for the seats** | `AX-5` + demand-driven CENSUS (`01_AXIOMS.md:172-181`) give a **derived** cap, which R7 prefers to a stipulated one. And **0 live `hold` tenures across 86 worlds** — see §5, which explains why that is not a fixture accident |
| Stewards paint work zones with caps | **REFUSED** | `AX-1` — *"a zone that allocates persons is nobody deciding."* Already cut at `proposals/2026-09-10-…/05_COLLISIONS_AND_RESIDUE.md:157-160` |
| A steward accrues a **following** among the cohort | **EXPRESSIBLE — as a Query, not a field** | R7 names this shape itself: *"holdings count and military capacity and influence are **Queries over `hold` and `commit` edges**."* A following is the same object. Stored, it is refused; derived, it is ruled in |
| ⭐ **Delegation risk *scheduled* rather than stochastic** | **LICENSED, VERBATIM — and subordinate to `T-o`** | `T-n`, `01_AXIOMS.md:1138-1142` — *"Some relations should not end at the holder's whim — a term of service… But an end condition nobody declared is a clock nobody wound, which `T-c` forbids. **So the opening act declares the terms.**"* A steward's term, declared at appointment, is that sentence |

**This is the consolidation's best transferable idea and it is not the one the document highlights.**
The document's own "what none of the twenty do" is *"delegation risk that is scheduled rather than
stochastic… you can read the year of your own coup off the population graph."* Valoria's axioms
license precisely that, and refuse the population graph it is read off.

**Where the term would live, stated exactly, because three sites disagree in emphasis.** `T-n` puts
the term on *"the Tenure's own `term`, set by the opening act"* (`01_AXIOMS.md:1157`); Layer 1 spells
it **`Tenure.term?`** — optional — at `04_CODE_ARCHITECTURE.md:183` row 14, alongside the single
generic `release` verb; and `engine/season/verb_table.yaml:421` records the declared-ends half as
**unbuilt**, in those words. `Tenure` today has no `term` field (`state/carriers.py:40-59`).

⚠ **And for a `hold` specifically, `T-n` subordinates itself to `T-o`.** `01_AXIOMS.md:1171-1174`
names the defect in its own schema: *"`Seat.revocation` and `Tenure.term.closer` are two homes for
who may end this hold… **The Seat's is authoritative** — a term's closer names a basis, and the basis
resolves against the seat."* **Delegation is exactly the case where that correction bites**, since a
steward holds a seat. So the transferable is *"the opening act declares the term; the seat declares
who may end it"* — two fields at two owners — and a proposal naming only the first would reopen the
defect the axiom already closed.

### E · "The Migrant Question" — the document's **lowest-ranked**, *"most likely to be structurally broken."* **Carries the second transferable idea.**

**GRADE: `paper`** for the proposal; **`assumption`** for the one verb underneath it
(`verb_table.yaml:362`).

| component | verdict | ground |
|---|---|---|
| Per-settlement **approval threshold** governing immigration | **REFUSED** | a stored settlement aggregate — `carriers.py:579/586`, R7 |
| ⭐ **Population chooses where to live** | **PARTLY PRODUCED — the act runs; the choosing does not** | see below |
| "Who lives where" as the scored object | **EXPRESSIBLE — as a Query** | R7's shape again: derive it from where persons are, never push it onto a container |
| War destroys the contested thing, so it is a spoiling move | **PRODUCED** | `_eff_kill` deletes the Person and closes every Tenure naming them (`effects.py:308-418`) — the cost is already permanent and already propagates |

**What executes, precisely.** `move` is a table row (`verb_table.yaml:350-363`, `grade: assumption`),
`_eff_move` writes `Person.travel_leg` (`effects.py:240`), `budget.py:59` charges
`len(travel_leg) × budget_leg_penalty` so **distance already prices acts**, and a `travel.moved`
event appears in a recorded run (`engine/season/runs/TRACE.txt:2193`). The verb table carries the
measurement itself: *"measured over the 89 runnable corpus worlds, `move` EXECUTES 650 times and is
blocked 73"* — a `W-C` finding that struck an earlier "no case moves" cell in place.

⚠ **What does NOT execute is the choosing, and the distinction is the whole value of this row.**
`decision/options.py:307-310` binds the operand `to` — like `subject` and `site` — to **the
question's referent**: *"three cell-side names for the one thing the person was asked about."* A
person never supplies a destination of their own; the question supplies it, and `move` is then one of
~22 candidates ordered mostly by draw. No preference over places is carried anywhere: `stance` is
`[]` in every built world. **So what runs is *a person can be moved to what they were asked about*,
not *a person chooses where to live*.**

**The inversion the document proposes — expansion means attracting rather than taking — is the
direction Valoria's axioms already point, and the tree does not yet reach it.** Only persons act; a
person's movement is their own act; the aggregate is a Query. What is missing is not the verb but a
*reason* attached to a *place*, and one act by which a person makes another's move more likely —
which is a candidate directed at a person, and therefore `P1`. The document reached this inversion by
fusing two games and graded it most likely to break; here it is **compatible and contingent**, not
native.

### B · "Slander" — **B. One real gap, which the surrounding components hide.**

**GRADE: `paper`.** Most of this proposal is already placed on both sides of the ledger — and one
component is not placed anywhere, which is the finding.

**Shipped.** `Claim(id, holder, subject, predicate, value, when, source, confidence, scope, round)` in
the holder's own ledger; decay at MATTER (`claim_decay_per_season = 5` against
`confidence_default = 100`); five witness channels; *contested in transit* — `tell` declares
`contests: "a standing"` and resolves at a measured 21%.

⚠ **Not shipped, though the table declares it: the forgery channel.** `forge` declares
`writes: ["Record.exists", "Record.forgery_quality"]` (`verb_table.yaml:240`) and has **no entry in
`EFFECTS`** — the eleven registered effects are `confer · release · revoke · convene · move · work ·
create_record · destroy_record · kill/wound · utter · transfer` (`loop/effects.py`). The gate
`effected = not row.writes or v in EFFECTS` (`loop/driver.py:99`) therefore excludes it, so
`Record.forgery_quality` is never written by anything. `destroy_record` is registered but
`hole_register.yaml:845` (`H-75`) records that it *"CANNOT FIRE FOR ANY ACTOR"*. **Both halves of the
evidence-fabrication channel are declared and unreachable.**

**Asked for by name in R7's own yield list.** Propaganda (utter a competing Proposition), cover-ups
(`destroy_record`, or simply not telling), the intercepted dispatch, the messenger who never arrives,
delayed news as distance, and *"rumour vs record graded by `Claim.confidence`, which exists and
already decays."*

**Blocked by two things Parts A–C name.** `source` is a channel label, not a speaker (Part B `P3`);
and a belief about a person cannot raise that person's question, so *discrediting a source* cannot
become an act directed at the source (Part B §0).

⚠ **AND ONE COMPONENT IS UNPLACED: WHAT TRAVELS IS THAT A TELLING HAPPENED, NEVER WHAT WAS SAID.**
A witnessed telling deposits, at `loop/witness.py:137`:

```python
c = Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own", self.round)
```

Three of those arguments close the channel slander needs:

| argument | what it is | consequence |
|---|---|---|
| `e.kind` as the **predicate** | the event kind — `news.told` (`verb_table.yaml:511-513`) | *"B is a traitor"* and *"B is a saint"* deposit the **same predicate** about B. The content is not in the claim |
| `True` as the **value**, hard-coded | not the teller's assertion, not the fold's finding | **a claim minted from a telling is never false.** A lie cannot be deposited as believed-true-and-wrong, which is the object slander is |
| `conf = confidence_default` | the fixture, read once per barrier (`:75`) | **news does not attenuate in transit.** Third-hand arrives at the same confidence as an eyewitness, and decay is a function of age alone |

The subject *does* travel — `epistemic.py:180-182` rules on that deliberately: *"A claim minted from
a telling is about WHAT WAS TOLD; the teller is not the news."* So the tree carries **who a telling
was about** and drops **what was claimed about them, whether it was true, and how far it has come.**
Content lives in world `Proposition`s, which are shared and therefore not plantable, or in W-B
observations, which are each person's own reads. **No shipped act puts a specific, false, attenuating
assertion about a person into another person's ledger.**

**That is an `S` defect, not a missing system**, and §0.06's `S` is the criterion that catches it:
*mechanics interact cleanly with other interdependent mechanics*, and *calculations consistent in
methodology*. Confidence is modelled as decaying with **age** and not with **transmission**, while the
design's stated yield — *"rumour vs record graded by `Claim.confidence`"* — presumes the second. Two
different notions of the same quantity meet at one field.

**It is also one object short of proposals already in the set, which is why it needs no sixth
proposal.** A speaker in `source` is `P3`; an act directed at a person is `P1`. What this component
adds is the *third* argument — a predicate and a value carried from the telling rather than from the
event kind — and it is recorded here as a named gap rather than proposed, because the two objects
before it decide its shape.

### D · "Two Ledgers" — **B+. The pool is refused; one mechanic rides `W-F`.**

**GRADE: `paper`.**

- A private reserve beside `Rung.stores` is **a second store with no owner**; `Rung.__setattr__`
  raises on undeclared fields. **Refused.**
- "Public liability feeding **unrest**" is a stored aggregate. **Refused.**
- *"The mechanism producing value is the mechanism producing threat"* is the consolidation's
  Directive 9, and Valoria's instance already exists: **`commit`** — a standing ambition that is both
  Q4's only question source and a permanent obligation. It is **not resolvable**, which is the gap.
- ⭐ *"Auditing a delegate who was loyal makes them less so"* **is `H-62`'s shape exactly** — an
  interior write keyed to an outcome. It needs no new object; it rides `W-F` and, per Part B §0, the
  person-referent clause before it.

### F · "The Levy" — **B+. Three halves, each already disposed.**

**GRADE: `paper`.**

- The ageing pyramid → **already proposed, `paper`** (2026-09-10), and `Rung.envelope` has no writer.
- *"Permanently removes whatever fraction dies"* → **already shipped and stronger**: `_eff_kill`
  deletes the Person **and** closes every Tenure naming them, so a death already propagates into the
  office ladder.
- *"A visible repayment date"*, the pyramid as primary interface → **refused** by §C.11
  (`04_CODE_ARCHITECTURE.md:765`): *"The engine owes the ARITHMETIC of what the character already
  holds, and nothing else."* R7: the player sees their character's **estimate**, never the true
  aggregate.
- The derived idea the document rates its best — *timing your war against a rival's demographic
  trough* — requires reading a rival's aggregate, which is the same refusal.

---

## §3 · THE ASYMMETRY MAP, CUT

The consolidation's nine asymmetries (A1–A9) are its structural contribution. Scored against the
tree, **two are already-Valoria, one is already-better-in-Valoria, and the rest are refused or
already-filed.**

| # | the transfer it proposes | verdict here |
|---|---|---|
| **A1** | give allegiance a delay | **already the design, ruled.** R7: *"legitimacy falls where the news has reached, at the speed news travels, suppressible/deniable/forgeable."* Valoria's allegiance is *nothing but* delayed — it travels as claims that decay |
| **A2** | zone + delegate together | **half refused** — the zone is `AX-1`; the delegate is `H-71` |
| **A3** | conscription that removes a cohort, not a number | rides the `paper` cohort |
| **A4** | a settlement game that scores standing rather than survival | **refused** — a score is a stored campaign aggregate |
| **A5** | the **graduated agent layer** — *"before building an agent layer, specify what its half-strength setting is"* | ⭐ **FALSE N-LINE on one dial** (Part A row 26, second document). `fixtures.py:328` sweeps `fan_out_mode` over `total / all_five / presence_only`, and `observers_for` **refuses an unrecognised mode** (`epistemic.py:404-409`) so that sweep can never silently read its control. The second dial does not carry the property — see below |
| **A6** | ephemerality solved by meta-progression | inapplicable — no reset |
| **A7** | a dual-use private/public pool | refused — see `D` |
| **A8** | scarce named agents over an abundant populace | `H-71` + the `paper` cohort |
| **A9** | **belief with provenance** — *"nothing in twenty titles models where a belief came from except The Guild 2 and Tropico"* | ⭐ **Valoria is already in the category the consolidation calls nearly empty across twenty games.** `Claim` carries `source`, `confidence` and `when` by construction. What it lacks is a *speaker* in `source` — Part B `P3`, one argument |

**A5 is the sharpest reversal in this part, and it is a reversal on one dial rather than two.** The
consolidation's most actionable lesson, derived from three shipped failures — The Guild 3's disabled
citizens, Tropico's shack-squatting, Bannerlord's unconsumed traits — is *build a graduated agent
layer with a working half-strength setting.* `fan_out_mode` is exactly that: three declared arms and a
loader that refuses a fourth, which is the property whose absence caused all three failures.

⚠ **`choice_temperature` is not a second instance, and the tree says so about itself.** It is a bare
float read at `decision/choose.py:220`; `Fixtures.get` refuses an **unregistered name**
(`fixtures.py:43-50`) and never an **out-of-sweep value**, so there is no refusing loader on its arm
set. And its control arm is disputed between two surfaces:

- `decision/choose.py:141-147` — *"`tau == 0` SHORT-CIRCUITS TO THE OLD PATH, AND THE ARM VALIDATES
  THE PLUMBING RATHER THAN THE SAMPLER… Stated plainly because both prior plans named the `tau = 0`
  arm as the sampler's control and neither noticed."*
- `engine/season/hole_register.yaml:1278` — still describes `0` as *"the pre-U4 argmax kept as the
  control."*

**Two surfaces give one quantity two meanings**, which is §0.06's `S` — *calculations consistent in
methodology with other mechanics* — failing on the dial this asymmetry holds up as exemplary. The
lesson arrives already learned on `fan_out_mode`; on `choice_temperature` it is still owed, and the
half of A5 that is genuinely ahead of the case law is the half with the refusing loader.

---

## §4 · THE SEVEN DOCUMENTS, ONE FRAME

**4.1 · One sentence.** *Across seven documents and thirty-three titles, every store-shaped primitive
is already a carrier in this tree; every scheduler, meter and ranker is refused by a ratified line;
and the two ideas that transfer are both ones their own authors ranked low.*

**4.2 · The tally, with its counting convention stated, because two conventions give two numbers.**

A primitive can recur across documents. Counting **objects** asks how many distinct mechanics were
cut; counting **instances** asks how many times a document proposed one. Both are reported.

| | per object | per instance | |
|---|---|---|---|
| **False N-lines** | **27** | **30** | Part A's 27 rows, partitioned 16 / 7 / 3 / 1 by disqualifier. The three later documents add **no new object**: `C`'s automaton is row 16, `A`'s steward cap is row 20, `A5`'s half-strength dial is row 26 — same objects, same citations, proposed again by a different author |
| **Proposals cut** | **12** | **18** | 6 in the audited *Thirteen Strategy Games* revision, 6 in the consolidation; the earlier draft re-proposes 6 of the first set under two changed titles. **0 adoptable as specified, on either convention** |
| **Genuinely transferable ideas** | **2** | **2** | `A`'s scheduled delegation term (`T-n`, subordinate to `T-o`) · `E`'s person-chooses-where-to-be (`move` runs; the choosing does not) |
| **Mechanisms Valoria has that the corpus rates rare or absent** | **3** | | belief-with-provenance (`A9`) · a graduated agent layer with a refusing loader (`A5`, on `fan_out_mode` only) · stale information as the default read |
| **Gaps named and not proposed** | **2** | | a predicate and value carried from a telling (`§2 B`) · `choice_temperature`'s disputed control arm (`§3`) |

**The distinct ratified lines the seven documents' proposals ran into — nine, not six.** The count
matters because each is a separate place a designer must go to reopen a decision:

| line | where | what it refuses |
|---|---|---|
| `AX-1` | `01_AXIOMS.md` | a non-person actor — zones that allocate, directors, storytellers |
| `AX-3` | `:115` | a clock that REVISES rather than removes |
| `AX-5` | `:151-165` | a fourth world motion; a quantity advancing with no author |
| `AX-6` | `:187-188` | permanence without an author |
| `T-b` | `:284-286` | a threshold that PRODUCES an outcome — the ground for a loss timer |
| `L3` / `R7` | `carriers.py:579,586` | every stored social aggregate, at every scale |
| `§C.11` | `04_CODE_ARCHITECTURE.md:765` | the engine showing more than the character's own arithmetic |
| the salience refusal | `07_DYNAMICS.md:182-184` | memory ranked by importance |
| `ED-IN-0011` | ledger | *never a meter* |

⚠ **`T-c` is NOT on that list, and it is the one most often reached for.** It *licenses* an authored
clock — *"bribed, delayed, burned, or killed"* — and the tree ships the licensed form as a `convene`d
`Date`. Citing `T-c` against a timer inverts it. See §2 `C`.

**4.3 · Why the transfer rate is so low, stated without euphemism.** These documents catalogue
designs in which **the world acts on the player** — timers, storytellers, directors, meters that
drift, thresholds that fire, scores that accumulate. Valoria's first axiom is that **only a person
acts**, and its decisive ruling is that **no magnitude is ever pushed.** A corpus of thirty-three
games selected for rich systems is therefore, for this tree, largely a catalogue of refusals — and
knowing *which* refusals, with the line that carries each, is worth more than an adoption would have
been.

**4.4 · What this part adds to the proposal set — and it is small by design.**

Neither transferable idea is a new proposal. Both **attach to items Part B already carries**:

- **`A`'s scheduled term** attaches to **`P2`** (`tie / knot`'s effect body). `T-n` says the opening
  act declares the terms; a `Tenure` carries no `term` field (`carriers.py:40-59`), and
  `verb_table.yaml:421` records this as unbuilt. So *if* a term field is ever added, the warrant is
  `T-n`, the shape is *declared at the opening act, never a clock*, and for a `hold` the closer
  belongs to the **Seat** per `T-o`. **Recorded as a warrant, not proposed as work.**
- **`E`'s person-chooses-where-to-be** attaches to **`P1`** (the person-referent clause). A person can
  already `move`; what they cannot do is supply their own destination or form a candidate *about
  another person*, which is what makes "court someone away" inexpressible.

**No new `needs_jordan` row from this part, and no new object.** What it adds to the set is two
warrants, a `[CONFLICT:]`, and **two named gaps** — a predicate and value carried from a telling, and
`choice_temperature`'s disputed control arm. The first of those two became **`P6`** once its site was
read; the second is **`M4`**. The set stands at **six proposals, four measurements and one refusal**.

---

## §5 · WHY NO PERSON HOLDS A SEAT — THE RATIFIED CHAIN

Three of the six proposals above break on a seat nobody occupies: `A`'s eight stewards, `D`'s audited
delegate, `A2`/`A8`'s scarce named agents. Parts A–C measured the fact — **0 live `hold` tenures
across 86 worlds**. The chain that forces it is short, entirely ratified, and closes the question of
whether that zero is a fixture accident.

1. **A `Tenure` is owned by its subject.** `state/carriers.py:387-388` quotes the class's own
   docstring: *"S15 — THE ONE EDGE. Owned by its SUBJECT (S15.1)"*, and `:378` — *"a Person owns every
   Tenure whose subject they are, so office-holding, body and travel are all the person's own state."*
2. **A `hold`'s subject must be a Person.** Ratified Layer 1, `04_CODE_ARCHITECTURE.md:181` row 12:
   `hold` with a Proposition subject → **"`hold`'s subject is a Person, only"**, reasoned *"an edge
   whose subject cannot act is not a relation."*
3. **A computed act's subject is its question's referent.** `decision/options.py:307-310` — `subject`,
   `to` and `site` are *"three cell-side names for the one thing the person was asked about."*
4. **No question source ever produces a person as a referent.** Measured: **177,170 candidates ·
   17,400 carrying a person id · every one the asker naming themselves · zero naming anyone else.**

**Therefore no computed act can create a `hold`.** Not because the fixture is thin, but because
ratified Layer 1 requires a Person subject at step 2 and the running grammar cannot supply one at
step 4. **The zero is a conformance gap between Layer 1 and Layer 2, and `P1` is the clause that
closes it** — which is a stronger warrant for `P1` than Part B claims for itself, since it makes the
proposal the thing ratified canon already demands rather than a new idea.

---

## §6 · WHAT THIS PART DOES NOT ESTABLISH

- **The relationship claims in §1 are not re-runnable from the tree**, because the seven sources are
  not in it. They are re-runnable against the pinned hashes with the commands given.
- **Letter grades are the documents' own** and are reported, never endorsed. `skills/ners/SKILL.md`
  §11: *"the form is the audit's business; the values are not."*
- **No component of any of the six proposals was executed.** Every `GRADE` row above reads `paper` for
  that reason, and the two `assumption` grades belong to tree objects, not to the proposals.
- **The `[CONFLICT:]` in §1 is unresolved** and cannot be resolved from either source.
- **Whether `Patience` self-decrements in its own design is unread** — the refusal above does not
  depend on it, since both available grounds refuse a shared loss timer either way.
