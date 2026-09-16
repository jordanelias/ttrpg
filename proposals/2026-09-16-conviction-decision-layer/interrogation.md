# Convictions and conviction axes — the interrogation

## Status: PROPOSED — **HELD BACK FROM RATIFICATION-ON-MERGE IN FULL** (ED-1094 exception)

**Lane:** IN (cross-cutting: `engine/season/decision/`, `systems/characters/`, `systems/npcs/`).
**Ledger row:** ED-IN-0228.
**Companion:** `decision_layer_v1.md` in this folder — this document says what is wrong; that one
says what to build.
**Occasion:** Jordan, 2026-09-16 — *"Let's interrogate convictions and conviction axes. We need to
have a decision making layer that incorporates the following: ambitions; needs; fears; memories;
worldly understanding (epistemic); moral values; religious values; self interest vs public
interest; character opinions; obligations and duties (faction, office); ethnicity/caste;
job/profession/educational background."*

---

## §0 Verdict

**Convictions are carrying the entire decision layer alone, and they are not shaped to carry it.**

Two independent failures, each measured:

1. **The decision function has three terms and two of them are dead.** What ranks a person's
   options today is one term — conviction weights against a sparse verb table. Of the twelve
   inputs Jordan names, **one is live and load-bearing.**
2. **The four-axis basis those convictions project through carries 1.85 independent directions,
   not four.** Nearly 70% of the variance across the thirteen authored rows lies along a single
   direction, and the fourth axis carries 2.6%.

These compound. A single scoring term would be survivable if it were expressive; a degenerate
basis would be survivable if it were one input among twelve. Together they produce what the corpus
already measures: people who differ on paper and choose alike.

**The answer is not to fix the matrix.** It is to stop asking one input to be the whole of a
person's judgment. §4 sets out what that does to the open escalation.

---

## §1 What a decision is today, in code

`engine/season/decision/choose.py::make_chooser` — the season loop's decision policy, and the only
one that executes:

```
score(c) = Σ_axis conviction[axis] · alignment(c.verb, axis)   # term 1
         + stance_toward(p, c.subject)                          # term 2
         + urgency(s.subsistence)                               # term 3
```

`conviction[axis]` is computed, not stored: `Σ_conv p.convictions[conv] · projection[conv][axis]`,
where `projection` is `conviction_axis_matrix_v30.md` §2's 13×4, transcribed verbatim.

Ahead of the score, `decision/options.py::opening_set` decides what is even a candidate, on four
clauses: the verb exists; `person_side_eligible`; the subject is a referent of the question; and
the verb's precondition is not KNOWN-FALSE from the person's own ledger.

**So a decision already has more than one stage.** `person_side_eligible` decides what a person is
entitled to attempt; the remaining clauses decide what is in front of them and what they can
coherently attempt given what they hold true; `score` decides which of those they want. Three
questions, already separated in the code. `decision_layer_v1.md` §1 names them and assigns the
twelve inputs across them, which is the whole of its architecture.

What the code does not have is twelve inputs.

---

## §2 Six findings, worst first

### F1 — Two of the three scoring terms cannot move a decision

**Term 3 is inert by construction.** `urgency(subsistence)` has no `c` in it. It is added
identically to every candidate, so it cannot change the ranking, cannot change which candidates
survive the budget, and cannot change their order. Registered as `H-73`;
falsifier `test_w5_f2s_third_term_cannot_change_any_decision`, which also asserts that `urgency`
actually varies, so the claim is about the design and not about a stub.

**Term 2 is inert in fact.** `stance_toward` sums `(referent, valence, weight)` rows off
`Person.stance`. Nothing writes that field. Measured on this tree, 2026-09-16:

```
PYTHONPATH=. python -c "
from engine.season.harness import populated as P
w = P.build_realm(0, cap=12); P.run(seasons=2, seed=0, w=w)
ps = list(w.persons.values())
print('stance rows', sum(len(p.stance) for p in ps),
      '| beliefs', sum(len(p.beliefs) for p in ps),
      '| ledger claims', sum(len(p.ledger) for p in ps),
      '| capability', sum(1 for p in ps if p.capability),
      '| marks', sum(len(p.marks) for p in ps),
      '| tenures', sum(len(p.tenures) for p in ps))"
```

→ `stance rows 0 | beliefs 0 | ledger claims 580 | capability 0 | marks 0 | tenures 70`.

Twelve people, two full seasons, 580 claims deposited, and **not one stance row**. The cause is
already registered: `hole_register.yaml` `H-62` — *"NO PART E VERB WRITES ANY `Person` INTERIOR
FIELD. `(Person, convictions)`, `(Person, beliefs)`, `(Person, scar)`, `(Person, axis_count)` and
`(Person, stance)` are all `social: true` — only an act may write them — and the verb table carries
no act that does."*

**Consequence.** The live decision function is one term wide. Every candidate whose `(verb, axis)`
pair is absent from the sparse alignment table scores identically, and the residual order is
settled by the draw (`U4`/`H-96`, Plackett–Luce via Gumbel) — which is an honest tie-break, not a
judgment. A person's history, office, needs and opinions do not reach the decision at all.

### F2 — The four axes are not four

Reproduce: `python -m engine.season.harness.conviction_spread`.

| direction | variance | share | cumulative |
|---|---:|---:|---:|
| 1 | 0.4620 | 69.8% | 69.8% |
| 2 | 0.1489 | 22.5% | 92.3% |
| 3 | 0.0338 | 5.1% | 97.4% |
| 4 | 0.0174 | 2.6% | 100.0% |

**Effective axes (participation ratio): 1.85 of 4.** Pairwise, every axis correlates with every
other: hierarchical × traditional `r = +0.743`, sacred × traditional `+0.685`, sacred ×
instrumental `−0.772`, traditional × instrumental `−0.660`, sacred × hierarchical `+0.426`,
hierarchical × instrumental `−0.212`. The sign pattern is uniform — *hierarchical, sacred* and
*traditional* are three readings of deference to an inherited order, and *instrumental* is that
same direction reversed. What the basis actually spells is **defers ↔ calculates**, plus a weak
second direction and two axes' worth of rounding.

The knock-on, from `conviction_spread`'s other half: the mean of the thirteen rows is (traditional
+0.285, sacred +0.215, hierarchical +0.200, instrumental −0.062) at magnitude 0.414, and **nine of
thirteen convictions lie within 60° of it** — Warden +0.97, Identity +0.95, Faith +0.94, Precedent
+0.93, Honor +0.89, Community +0.86, Virtue +0.80, Authority +0.79, Order +0.64. Only Liberty
(−0.90), Utility (−0.65), Equity (−0.37) and weakly Scholastic (+0.10) are different characters.

⚠ **`conviction_axis_matrix_v30.md` §2.2 asks the opposite question and must not be answered as
written.** It reserves a *fifth* axis in case the 4-axis collapse of Community-vs-Identity proves
load-bearing. The spectrum says the matrix cannot support the four it has; adding a fifth column
to a basis with 1.85 directions in it would author a new coordinate, not a new distinction.

### F3 — "Conviction" names four different objects, two of them in CANONICAL documents

| sense | object | home | status |
|---|---|---|---|
| (a) | a 13-element weight vector over value-frames | `conviction_taxonomy_v30.md` §2 | CANONICAL |
| (b) | a player-authored **one-sentence intention** that resolves Fulfilled / Failed / Transformed / Unresolved | `player_agency_v30.md` §2 | CANONICAL |
| (c) | a per-territory 0–5 popular-belief stat (the Piety Track's former name) | `conviction_track_v30.md` | live |
| (d) | the social-contest track, since renamed Persuasion Track | `name_collision_database.yaml` | renamed |

(a) and (b) are **not the same object**, and `player_agency_v30.md:71` asserts that they are:
*"Vocabulary unification: Player Convictions and NPC Convictions share the same name because they
serve the same function."* A weight vector is a standing disposition; *"I will discover what
Haelgrund is hiding from the Church"* is an intention with an object, an obstacle and a resolution
state. They cannot be the same field.

**And sense (b) is Jordan's factor (1), ambitions.** So two of the twelve inputs are currently
spelled with one word, and the one that runs is the other one.

`CLAUDE.md` §4's idempotence test — *reading the word cold, in a later session, must yield the same
meaning* — fails inside the corpus's own canon. Already recorded as **P15** in
`proposals/2026-08-23-competing-vocabularies-index.md` (unratified).

### F4 — The self/institution axis was deleted, and it is factor (10)

`npc_behavior_system_v1.md:17–21` types the Stance Triangle as **three** attributes, verbatim:

> **Conviction** — the NPC's operative worldview. What they believe grounds value. **Determines
> what the NPC wants to do.**
>
> **Ethical Framework** — inherited from the NPC's faction. What the institution incentivises.
> **Determines what the NPC is rewarded for doing.**
>
> **Resonant Style** — the argument form that bypasses the NPC's defenses. … **Determines how the
> NPC can be moved.**

⚠ **The compressed two-line rendering of this passage in
`proposals/2026-08-23-competing-vocabularies-index.md` §5 is that document's paraphrase, not the
source's wording, and it should not be re-quoted as if it were.** The distinction it draws is
nevertheless exactly the source's.

The two are separately authored per NPC. `npc_behavior_v30.md` §2.1: King Almud holds **Primary
Conviction `Order`** *and* **Ethical Framework `Virtue (Crown)`**, the second written as an
obstacle modifier — *"Aligned: −1 Ob on public, visible, virtuous action. Contradictory: +1 Ob on
covert/expedient action."* (Whether that modifier currently fires is disputed inside the corpus;
see the end of this finding.)

PP-684 §6 then maps the philosophical-tradition labels — *Categorical Imperative, Virtue Ethics,
Divine Command, Epistemic Reason, Rawlsian, Military Honor* — into the 13-Conviction set
(`Virtue Ethics → Virtue`, `Divine Command → Faith`, and so on). Those labels are the vocabulary
the Ethical Framework column is written in, so the migration folds an institutional axis into a
personal one.

The vocabularies index names the cost: *"this destroys the most legible dramatic engine in the
corpus: a devout man serving a cynical institution. Collapsed to one axis, every character becomes
internally consistent, and every institutional-betrayal arc in the roster loses its mechanism."*

Jordan's factor (10) — obligations and duties, faction and office — **is that deleted axis.** It
was not missing from the design; it was merged away.

`character_canon_v30.md` **D2** kept the labels rather than dropping them — *"retain as descriptive
disposition tag … mechanical Ob modifiers stay attached to the label since they're live in
engine"*, with a standing instruction *"do not silently re-derive Ob modifiers from conviction
vector — that's a separate cycle."* That instinct was right and is unratified.

⚠ **AND THAT DOCUMENT CONTRADICTS ITSELF ON WHETHER THE MODIFIERS ARE LIVE**, which is reported
rather than resolved here: `:50` records the label-derived Ob modifiers as **SUPERSEDED**
(PP-686 §3.7's triadic calculation replaces them) while `:427` keeps them *"live in engine"*, and
`:385` grades the row **CONFLICTED** in its own words. Whether an Ethical Framework currently
moves an obstacle is therefore not answerable from canon, and this proposal does not assume
either reading.

### F5 — Self-Other orientation is fully authored and entirely unread

Factor (8) is the best-specified of the twelve and the least connected:

- **Defined** — `conviction_taxonomy_v30.md` §3: a scalar in `[−1, +1]`, with an attribution
  formula (§3.1), a drift law (§3.2) and initial values (§3.3). §2.3 makes the design argument
  explicitly: Cesare Borgia and a public-spirited magistrate share high Utility; what separates
  them is *for whom* they instrumentalize.
- **Registered** — `descriptor_registry.yaml` carries `orient.self_other`, `by_reference`.
- **Authored** — `references/npc_registry.yaml` carries a `self_other_initial` on **28 of its 46**
  character entries. (An earlier draft of this document said *every* entry; counted, it is 28 —
  `grep -c 'self_other_initial:' references/npc_registry.yaml` against
  `grep -cE '^\s*- id: NPC-' references/npc_registry.yaml`.)
- **Read by** — nothing. `grep -rn "self_other" --include="*.py" .` returns no reader. There is no
  field for it on `Person`.

The most dramatically load-bearing scalar in the character model is authored on a clear majority of
the named roster and read by nothing.

### F6 — Three of the twelve are eligibility questions, and eligibility is closed at four kinds

`engine/season/rosters.yaml:eligibility_kinds` → `[own, remit, hold, presence]`, with a standing
note in the file itself:

> *"Adding a fifth kind is a DESIGN CHANGE — a new way to make a verb unavailable to someone — and
> not a table edit, so it needs a ruling before it needs an entry."*

Factors (10) office and duty, (11) ethnicity and caste, and (12) profession and training are
naturally **gates** — *may this person do this at all* — rather than weights. Only (10) has a
partial route in today, through `hold` and `remit` Tenures. (11) exists in prose only
(`faction_politics_v30.md`'s caste ladders; `conviction_taxonomy_v30.md` §5's cultural-background
templates, authored per character as `cultural_label` and read by nothing). (12) has a carrier —
`Person.capability` — that is **ruled to gate nothing**: `#353` §9.2, *"capability supplies dice
and GATES NOTHING… the only class-shaped gate in the design is Thread Sensitivity"*, verified by
probe `P11`.

So three of the twelve cannot enter the present architecture at all without a ruling.

---

## §3 The twelve, inventoried

**Read the last column first.** *Live* means the decision path reads it and it varies.

| # | Jordan's input | authored where | carrier on `Person` | reaches a decision? | state |
|---|---|---|---|---|---|
| 1 | **ambitions** | `player_agency_v30.md` §2 (as "Convictions"); `npc_registry.yaml:goals` | — | no | **absent in code** |
| 2 | **needs** | `Sensation.subsistence`; `body` | `body` (+ `Sensation`) | term 3 | **inert** (no `c`; `H-73`) |
| 3 | **fears** | — | — | no | **absent everywhere** |
| 4 | **memories** | `Person.ledger` (Claims), `claim_sources.told_by` | `ledger` | `opening_set` clause 4 | **live as a gate**, fires 0× at the shipped channel setting |
| 5 | **epistemic** | `engine/season/epistemic.py`, witness channels | `ledger` | same as (4) | same |
| 6 | **moral values** | `conviction_taxonomy_v30.md` §2 | `convictions` | term 1 | **live — the only one** |
| 7 | **religious values** | Faith conviction; **Truth** 0–5 (ED-IN-0075), authored per named NPC in `npc_behavior_v30.md` §2 | `convictions` only | Faith, via term 1 | **half** — Truth is authored and has no carrier |
| 8 | **self vs public** | taxonomy §3; `npc_registry:self_other_initial` | — | no | **authored, unread** (F5) |
| 9 | **character opinions** | `Person.stance` `(referent, valence, weight)` | `stance` | term 2 | **live but never written** (F1) |
| 10 | **obligations / duties** | `player_agency_v30.md` §3; Tenure/Office; the deleted Ethical Framework | `tenures` | eligibility `hold`/`remit` | **partial — gates, never weights** |
| 11 | **ethnicity / caste** | `faction_politics_v30.md`; `cultural_label` templates | — | no | **prose only** |
| 12 | **job / profession / education** | `Person.capability`; Scholastic conviction | `capability` | no — ruled to gate nothing | **present, inert** |

**Tally: 1 live and load-bearing · 2 live but empty or inert · 2 live as a gate that never fires ·
7 with no reader.**

⚠ **Two of the seven need no new primitive, and that is the good news in this table.**

- **(3) fears** is a `stance` row at strongly negative valence. `stance` already types
  `(referent, valence −5..+5, weight 0..5)`; a fear is an aversion to a referent, which is what
  that row says. Factor (3) does not want a new field — it wants `H-62` closed.
- **(9) opinions** wants the same thing. One repair serves both.

---

## §4 What this does to ED-IN-0214

`ED-IN-0214` (open, `needs_jordan: true`) escalates one question — whether the 13×4 should be
**re-centred** — and offers two options: **(a)** leave it, because the setting's moral world is
genuinely conservative and the four dissenters are meant to be the interesting minority; **(b)**
recalibrate so the thirteen span the basis evenly, overwriting 52 individually argued canon cells.

**Both options assume convictions are the decision layer. They are only that by accident.**

The row's own measurement is the tell: separating the thirteen from the four axes raised ranking
discrimination from 7–11 to 16–22 of 28 candidates, **and distinct executed sets fell 40 → 27**.
A change that made people's preferences sharper made the world do fewer different things. That is
the signature of a single-input score: sharpening the one input concentrates everyone onto the
same small set of high-scoring verbs, because there is no second input to pull them apart.

So there is a third option, and it is the one this interrogation recommends:

> **(c) Leave the matrix. Stop asking it to carry the decision.**
>
> The degeneracy costs what it costs because convictions are the only live term. As one preference
> input among five, a 1.85-dimensional value basis is *appropriate*: a person's morals should place
> them coarsely and their needs, obligations, opinions and interests should separate them finely.
> Two people with near-identical conviction vectors then differ by what they owe, what they want,
> whom they like and what they lack — which is how people differ.
>
> (b) would spend a ratified canon document — every cell of which is argued from a period source
> in `conviction_axis_matrix_v30.md` §3 — to buy discrimination that a second input supplies for
> free, and F2 says it could not buy much: you cannot re-centre thirteen rows into four directions
> when the columns they are written in span 1.85.

**This does not close ED-IN-0214.** It changes what the row is asking, and the option it should be
asking about is not in its list. Jordan rules.

---

## §5 What this interrogation did not establish

- **Whether the four axes should be replaced rather than de-weighted.** The spectrum says the
  basis is ~2-dimensional; it does not say the right two names are *defers ↔ calculates* and
  whatever direction 2 is. Naming direction 2 requires reading the eigenvector, which
  `conviction_spread` does not currently return.
- **How much each proposed input would actually move a decision.** No arm was run, because eleven
  of the twelve have no reader to sweep. The first measurable version of that question arrives
  with the first new term; `decision_layer_v1.md` §4 orders the work so that each step is
  measurable when it lands.
- **Whether (11) caste should gate or weight.** F6 establishes that it cannot enter today. It does
  not establish which it is — that is a design call in `decision_layer_v1.md` §5.
