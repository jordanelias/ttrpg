# The decision layer — twelve inputs, three stages

## Status: PROPOSED — **HELD BACK FROM RATIFICATION-ON-MERGE IN FULL** (ED-1094 exception)

**Lane:** IN. **Ledger row:** ED-IN-0228. **Reads:** `interrogation.md` in this folder, which
establishes the measured state this design answers. **Nothing here is ratified by merging it.**

---

---

## §0 WHAT THE ADVERSARIAL PASS OVERTURNED — 2026-09-16, same day

Five structurally read-only critics attacked this document's claims. **Every finding below was
re-verified by hand against the tree.** The design is left standing with its defects marked rather
than quietly rewritten: three of its five preference terms are unbuildable as specified, and one
reproduces the exact defect it was written to repair.

| § | the claim | the defect | verified at |
|---|---|---|---|
| §1 | a decision has three stages | **A fourth runs first and dominates.** Question production precedes STANDING, and `question_aggregation_rule="first"` takes `qs[0]` — the question decides **801 of 1,068 deliberations** (ED-IN-0218). A stage-2 attention term cannot bias which question is answered under `first` | `data/fixtures.py`; `queries/world_q.py:159-248` |
| §2 | office/remit "**works today**" | **FALSE.** `remit:` declines unconditionally (`H-71`), `presence:` declines (`H-33`), `hold:<placeholder>` declines (`H-75`), and the verb table carries **no bare `hold`**. Only `own` admits. The one live channel from office to decision is the **budget bonus** | `decision/options.py:143-169`; `decision/budget.py` |
| §3.2 | `regard` is written by the witness channels | **WRITE-CLASS VIOLATION.** `(Person, stance)` is `steps: [RES]`, `class: ACTS`, `social: "true"` — **only an act at RESOLVE may write it.** WITNESS-side writing is an unmarked cell | `engine/season/write_matrix.yaml:204-209` |
| §3.4 | `interest = orientation · scope(c.verb)` | **INERT BY CONSTRUCTION — the defect this term was repairing.** `writes:` cells name record kinds, never rung kinds; the only rung-kind column is `scale:`, on 10 of 38 rows, **none of which executes**, failing loader invariant 10 and slated for deletion. `scope` is undefined for every candidate that forms → constant → `H-73` exactly. **And the sign is inverted**: with orientation ∈ [−1,+1] and scope ascending `person→realm`, a *self-aggrandizing* person scores *wide* acts higher — the opposite of this document's prose | `verb_table.yaml:66-75`; `hole_register.yaml` H-73 |
| §3.5 | `pursuit` needs a new `Ambition` carrier | **DUPLICATES A LIVE MECHANISM (§8).** A `commit` Tenure to an OUGHT Proposition already mints Q4 — *"that IS the ambition mechanism"*. What is genuinely missing is a **preference term over the live commit** and the four resolution states, not a new object | `requirements.yaml` R-06; `world_q.py:240-248` |
| §4 | build order starts at `H-62` | **The true first step is `W27` — the cast — plus a person-referent route.** Every writer this design needs is character creation, and *"NOTHING creates or develops a person"*. Measured: 177,170 candidates, 17,400 person-subject, **all of them the asker, zero another person** — so closing `H-62` leaves `regard` with almost nothing to read | `requirements.yaml`; ED-IN-0217; `registers/handoffs/HANDOFF_IN.md` |

⚠ **The §3.4 failure is the instructive one.** This document diagnosed `H-73` — *a term with no `c` in it cannot move a ranking* — and then specified a replacement term whose operand is absent on every executing verb, which makes it constant across candidates, which is `H-73`. Diagnosing a defect is not immunity from it. The check that would have caught it is one grep of the column the term reads.

⚠ **One miscite:** `rank_of` is `title_rank` (`data/rosters.py:315`).

⚠ **A word-choice hazard this document did not catch.** `rosters.yaml`'s question-source roster
already names the **ambition** source `need`, while Jordan's list uses *needs* for subsistence. Two
different things, one word, across a session boundary — `CLAUDE.md` §4.

---

## §1 The shape: a decision already has three stages, and they take different inputs

The mistake to avoid is a twelve-addend sum. Twelve terms in one score is unintuitable, and
`CLAUDE.md` §0.06's **E** is explicit that a design must *allow the player to intuit complex
outcomes from simple choices* — a property twelve weights destroy and three questions preserve.

The good news is that the season loop's decision path **already has three stages**. They are not
proposed here; they are named, and the twelve inputs are assigned to them.

| stage | the question it answers | type | where it lives today |
|---|---|---|---|
| **1 · STANDING** | *What is this person entitled and equipped to do at all?* | boolean per `(person, verb)` | `decision/options.py::person_side_eligible` over `rosters.yaml:eligibility_kinds` |
| **2 · OCCASION** | *What is in front of them, and what can they coherently attempt given what they hold true?* | a set of candidates | `opening_set` clauses 3–5, `Question.referents`, `epistemic.py::belief_contradicts` |
| **3 · PREFERENCE** | *Of what is available, which do they want?* | a scalar per candidate | `decision/choose.py::score` |

A player reads their character down that ladder: *what may I do · what is in front of me · what do
I want*. Each stage asks one question. That is where the elegance has to come from, because it
cannot come from the count of inputs.

### 1.1 Two of the twelve sit in two stages, deliberately

**(10) obligations and duties** splits, and the split is the repair of `interrogation.md` F4:

- **office permits** — a remit makes a verb available that is otherwise unavailable. **Stage 1.**
- **duty pulls** — what the institution rewards you for doing is not what you may do; it is what
  you are drawn to do, and it is separable from what you personally value. **Stage 3.**

That is `npc_behavior_system_v1.md`'s Stance Triangle distinction, quoted in full at
`interrogation.md` F4: Conviction **determines what the NPC wants to do**, Ethical Framework
**determines what the NPC is rewarded for doing**. Restoring it as a stage-3 term rather than as a
second conviction roster is what keeps *a devout man serving a cynical institution* representable
without reopening the roster war.

**(1) ambitions** splits the same way: an ambition decides what counts as an occasion worth
attending to (**stage 2** — `player_agency_v30.md` §2.3's *"the Scene Slate prioritizes
opportunities that intersect with active Convictions"*), and it biases the choice among those
occasions (**stage 3**).

---

## §2 The twelve, assigned

### Stage 1 — STANDING (3)

| # | input | mechanism | state |
|---|---|---|---|
| 10a | office / remit | `hold` and `remit` Tenures | ⚠ **CORRECTED (§0): does NOT gate person-side.** The live channel is the budget bonus |
| 11 | ethnicity / caste | — | needs a ruling (§5 J2) |
| 12 | job / profession / training | — | needs a ruling (§5 J2) |

### Stage 2 — OCCASION (3)

| # | input | mechanism | state |
|---|---|---|---|
| 4 | memories | `Person.ledger`, deposited by the witness channels | **works today**, fires 0× at the shipped setting |
| 5 | worldly understanding | `belief_contradicts` over the same ledger | as above |
| 1a | ambition-as-attention | — | needs the carrier (§4 step 4) |

### Stage 3 — PREFERENCE (8)

| # | input | term | state |
|---|---|---|---|
| 6 | moral values | `value` | **live** — the only live term |
| 7 | religious values | `value` (Faith) + stage 2 (Truth) | half; Truth has no carrier |
| 9 | character opinions | `regard` | live, never written |
| 3 | fears | `regard`, negative | same repair as (9) |
| 2 | needs | `relief` | inert; needs a candidate argument |
| 8 | self vs public interest | `interest` | authored, unread |
| 10b | duty-as-pull | `interest` | deleted by PP-684 §6 |
| 1b | ambition-as-pull | `pursuit` | absent |

---

## §3 The preference score

```
score(c) =  w_value    · Σ_axis value[axis] · align(c.verb, axis)
         +  w_regard   · regard(p, c.subject)
         +  w_relief   · relief(p, c)
         +  w_interest · interest(p, c)
         +  w_pursuit  · pursuit(p, c)
```

**Five terms, not twelve**, because the twelve inputs are not twelve independent quantities — they
are twelve things a person is, entering through five channels.

### 3.1 `value` — (6) and half of (7). Unchanged in shape.

`Σ_conv p.convictions[conv] · projection[conv][axis]`, against the sparse alignment table. This is
term 1 today and nothing here changes it.

⚠ **(7) is already correctly split by the existing model, and that is worth saying rather than
repairing.** A religious *value* — how much a person weights ecclesiastical order — is the **Faith**
conviction, and it is already in this term. A religious *belief* — which metaphysics is true, the
Solmund-orthodoxy pole or the Thread-truth pole — is **Truth**, ruled 0–5 engine-internal with
qualitative bands to the player (ED-IN-0075), and it is a claim about the world, so it belongs in
stage 2 beside the ledger. Valoria separates devotion from doctrine. What is missing is only the
carrier: no `Person` field holds Truth.

### 3.2 `regard` — (9) and (3). One repair serves both.

`stance_toward` already sums `(referent, valence −5..+5, weight 0..5)` rows. An **opinion** is such
a row; a **fear** is such a row at strongly negative valence and high weight. Factor (3) wants no
new primitive.

**What it wants is `H-62` closed:** acts must write interiors. Today nothing does, and the
measurement in `interrogation.md` F1 is `0` stance rows after two seasons.

The write rule follows the witness channels that already exist: a person who witnesses an act
deposits a claim about it (this runs), and an act whose outcome falls on them or on what they hold
also writes a valenced row naming its actor. Aversion is accumulated regard, which is why one
mechanism carries both.

### 3.3 `relief` — (2). The repair of the inert term.

`urgency(subsistence)` is inert because it has no `c` in it (`H-73`). The repair is not to delete
it but to give it the argument it is missing:

```
relief(p, c)  :=  how far c's declared outcome reduces p's own deficit
```

`write_matrix.yaml`'s Degree-keyed `writes` column already declares what a verb's outcome writes.
A person's deficits are `body` against the fixture scale and their subsistence. So `relief` reads
two things that already exist and authors no new table. **`H-73` closes when this lands**, and its
falsifier is the existing one run in reverse: a decision must now move across subsistence scales.

### 3.4 `interest` — (8) and (10b). Derived, not authored.

```
interest(p, c)  :=  orientation(p) · scope(c.verb)
```

- **`orientation(p)`** is `conviction_taxonomy_v30.md` §3's `[−1, +1]` scalar, with its drift law
  in §3.2. It is **already authored on 28 of the 46 entries** of `references/npc_registry.yaml` as
  `self_other_initial`, and §3.3 supplies the default for the rest (`0.0`, most NPCs in
  `[−0.2, +0.2]`). Nothing needs inventing; it needs a field and a reader.
- **`scope(c.verb)`** — the widest rung the verb's declared writes can land on, read off the verb's
  own row. `rosters.yaml:rung_kinds` is already an **ordered** roster (`person · hearth · community
  · settlement · territory · province · duchy · realm`, loaded by `data/rosters.py::RUNG_KINDS` with
  `ordered=True`), and `title_rank` already reads a title's ordinal in it as *"higher governs wider"*,
  so the ladder this term measures along exists and is single-owned.

⚠⚠ **THE FIRST DRAFT OF THIS TERM READ THE SUBJECT'S RUNG, AND IT WOULD HAVE RAISED.** It said
*"`containing_rung_of` already computes the placement"*. It does not: that function returns the
object of **the actor's own** live `contain` Tenure — where *they* are — and there is no
person-side route to an arbitrary subject's rung. `AX-2` binds every file under `decision/`: no
`World`, as an import, a name, an attribute or a string, enforced by path (`04:1046`). `View`
carries `("holder", "claim_ids", "question")` and its `__getattr__` raises **`Forbidden`** on any
other name — *"choose() reached for world state through its View"*. `Sensation` is ruled to exactly
two scalars (S18.2). So the world position of a candidate's subject is not reachable from inside a
decision, by construction, and a term that needed it would have failed at the first call.

**The cost of the repair is real and is not netted off.** Reading scope off the verb makes *who
benefits* a property of the **kind of act**, not of **this act's target**: giving grain to one's own
hearth and giving it to a rival duchy score alike. Two ways to recover the instance, neither taken
here:

  * a `benefits:` cell on the verb row naming which operand receives — a data edit in a table that
    already carries `writes:`, `requires:` and `eligible:`, and AX-2-clean because the verb table is
    already imported by `decision/`; or
  * the rung arriving through the person's **own claims**, so that a person's sense of who benefits
    is a belief that can be wrong. That is the better game and the larger build, and it is the same
    channel stage 2 already uses.

A self-aggrandizing person then scores narrow acts higher and a self-sacrificing one scores wide
acts higher, **from the same option set, with the same convictions.** That is what separates Cesare
Borgia from a public-spirited magistrate in §2.3's own example, and it is the single cheapest
source of between-person variety available — because the data is already written down.

**(10b) duty-as-pull rides this term**, with the institution as the beneficiary: a person holding a
Tenure has their institution's rung as a second centre of interest, weighted by the tenure. That is
the Ethical Framework axis restored as a *weight on whose benefit counts*, not as a rival roster of
values — which is what made PP-684 §6's merge look reasonable and was the wrong repair.

⚠ **`npc_behavior_v30.md` §2 already carries authored values for this term, in the shape it wants
— for most of the roster, not all of it.** Counted: **17** `§2.x` entries, **12** carrying an
Ethical Framework row, **9** of those written as an obstacle modifier rather than as a bare label.
King Almud's is *"Aligned: −1 Ob on public, visible, virtuous action. Contradictory: +1 Ob on
covert/expedient action."* A modifier on acts of a kind is a preference term, which is why
restoring the axis here costs little new authoring for the nine and leaves eight entries to write
rather than a roster to invent.

### 3.5 `pursuit` — (1). The largest new surface, and a rename.

An **Ambition** is `(referent, direction, invested, state)`, where `state ∈ {live, fulfilled,
failed, transformed, unresolved}` — `player_agency_v30.md` §2's four resolution states, unchanged.
`pursuit(p, c)` is non-zero when a candidate advances a live ambition's referent; the same
predicate drives stage-2 salience.

⚠ **THE OBJECT EXISTS AND IS MISNAMED.** `player_agency_v30.md` §2 calls this a *Conviction*, and
§2.1 asserts that it and the 13-weight vector *"serve the same function"*. They do not
(`interrogation.md` F3). Under `CLAUDE.md` §4 — **idempotent in meaning, idiomatic in choosing** —
one word carrying two objects across a session boundary is the failure that rule exists to prevent,
and the worked example it cites (`evacuate`) cost three surfaces and two PR bodies.

**Rename it `Ambition`.** The word is ordinary, it is used this way outside this repository, and it
is Jordan's own word for the input (2026-09-16). "Conviction" is then free to mean exactly the
thirteen. This is **work, not an escalation** — §4's rule is ruled (ED-IN-0179) and the collision
is measured — but it edits a CANONICAL document's vocabulary, so it lands as a proposal with its
reasoning rather than as a sweep.

### 3.6 The weights are fixtures, and this document states none

`w_value … w_pursuit` are **not written here and must not be.** `CLAUDE.md` §0.05: a value the
engine uses lives where code reads it — a typed artifact under `engine/engine_params/` behind an
exporter, or a single Python owner — never in prose. `H-66` already holds the weighting question
for the existing term, and §G's discipline binds weights rather than structure. The words are
**`ARCHITECTURE_V2.md` §F2's**, quoted inside `H-03`'s `cite:` and attributed there rather than
here — *"grade: assumption. **The shape is ruled** (§3 L1, §9, §26); only the weighting is open"*.

Each weight enters as a fixture with a register row and a sweep, and the sweep is the measurement
that says whether the term earned its place. A number written into this document would be a second
home for it, rotting independently of the code.

---

## §4 Build order

Each step is measurable when it lands, and no step invalidates an earlier one.

**1 · Close `H-62` — acts write interiors.** The keystone. It makes term 2 live, gives (3) and (9)
their home, and its shape is already supplied (`#358` rev.2 §C.4 / §F.20a's Degree-keyed `writes`
column). *Falsifier:* the stance-row count in `interrogation.md` F1 goes non-zero, and the corpus's
distinct-executed-set count moves. Nothing downstream is worth building first, because two of the
five terms read state nothing writes.

**2 · `Person.orientation` + the `interest` term.** Seeded from `npc_registry.yaml`'s existing
`self_other_initial`; beneficiary derived from the rung spine. The cheapest large gain in the list —
authored data, an existing spine, one new field, no new table. *Falsifier:* two people with
identical convictions and opposite orientation rank the same option set differently.

**3 · `relief(p, c)`.** Closes `H-73`. *Falsifier:* a decision moves across subsistence scales,
which the existing test asserts it cannot.

**4 · Ambitions.** Rename, carrier, stage-2 salience and the `pursuit` term. Largest authorial
surface; it is fourth because it is the only one requiring new authored content per character.

**5 · `Person.truth`.** (7)'s doctrinal half. Ruled already (ED-IN-0075), and **authored already**
— **12 of `npc_behavior_v30.md` §2's 17 entries** carry a Truth value with its band (King Almud:
*"3 (Questioning) — already cracking"*). Only the carrier is missing. Fifth because it is small and
blocks nothing.

**6 · Stage-1 kinds for (11) and (12).** Last, because it is ruling-blocked (§5 J2).

---

## §5 What needs Jordan — three items, and the rest is work

`CLAUDE.md` §0's five tests applied. Everything that could be answered by a later ruling, by a
design document, by precedent or by what the architecture obviously wants has been answered above
and is **not** listed here.

### J1 — ED-IN-0214, re-framed

The open row asks whether the 13×4 should be re-centred and offers **(a)** leave it or **(b)**
recalibrate. `interrogation.md` §4 argues a third option — **(c) leave the matrix and stop asking
it to carry the decision** — on the ground that the matrix's measured degeneracy (1.85 effective
axes) costs what it costs only because convictions are the only live term. **Recommended: (c).**
Two defensible readings lead to materially different games, and (b) overwrites 52 individually
argued canon cells, so this stays Jordan's.

### J2 — A fifth and sixth eligibility kind, or none

`rosters.yaml:eligibility_kinds` states its own rule: *"adding a fifth kind is a DESIGN CHANGE — a
new way to make a verb unavailable to someone — and not a table edit, so it needs a ruling before
it needs an entry."* Factors (11) caste and (12) profession are gates by their nature. The fork:

- **gate them** — new kinds, and a caste or a trade genuinely closes verbs; or
- **weight them** — no new kinds, and caste and training bias the score instead, so a person may
  attempt anything and is merely bad at, or disgraced by, the wrong things.

⚠ **AND THIS RULING COLLIDES WITH A RATIFIED RETIREMENT, WHICH IS WHY IT CANNOT WAIT.**
`architecture/PLAN.md:723` retires `(Person, capability)` and `(Person, marks)` as **dead rows**,
because they *"carry `emits:` kinds **no Part E verb produces**"*; `meta/01_AXIOMS.md:831` records the
same retirement. Both are carriers Jordan's (11) and (12) would put to work, and **their
deadness has the same single cause as `stance`'s inertness — nothing writes them.** Step 1 of §4
removes that cause. Retiring two rows for want of a writer, in the same period as a request that
supplies them a purpose, is a decision worth taking deliberately rather than by schedule.
**Recommended: hold the retirement of those two rows until J2 is ruled.**

### J3 — Whether to un-merge PP-684 §6

§3.4 restores the institution-vs-self axis as a *weight on whose benefit counts*, which does not
reopen the roster. That may be enough. If it is not — if the Ethical Framework needs to be a
first-class per-faction object again, which is what `character_canon_v30.md` D2 has been holding
open by keeping the labels — then PP-684 §6's alias is overwritten, which is ratified canon either
way.

⚠ **And D2 cannot be cited as evidence for either side**, because it contradicts itself on whether
the label's obstacle modifiers are live (`interrogation.md` F4's closing note: `:50` superseded,
`:427` live, `:385` grading the row CONFLICTED). Settling that contradiction is part of this
ruling, not a precondition of it.

### Not escalations

- **The rename to Ambition** (§3.5) — answered by §4's word-choice rule, ED-IN-0179.
- **The five weights** (§3.6) — a sweep under `H-66`, not a ruling.
- **Whether (3) fears need a primitive** — answered by the architecture: `stance` already types it.
- **Whether (7) needs its own term** — answered by the existing model, which splits devotion from
  doctrine correctly.

---

## §6 The objection this design has to survive

**"Twelve inputs is not elegant."** Under §0.06's **E** — *logically simple; no unnecessary
overhead; allows the player to intuit complex outcomes from simple choices* — that objection is
the right one to raise, and it is the reason for §1's shape rather than a flat sum.

Two answers, and the second is the load-bearing one:

1. **Twelve inputs, three questions.** A player asks *what may I do · what is in front of me · what
   do I want*, in that order. Nobody holds twelve weights in their head; everybody holds three
   questions.
2. **Twelve inputs, three new fields.** `orientation`, `truth`, `ambitions`. Everything else rides
   a carrier that already exists and is currently dead — `stance` for opinions and fears, `ledger`
   for memory and understanding, `tenures` for obligation, `body` and `Sensation` for need,
   `convictions` for value. **Most of this work is connecting state the game already carries, not
   adding state.** That is the difference between a design that grows the model and one that pays
   off what the model already owes, and it is why `H-62` is step 1 rather than step 6.

⚠ **E is scored last and as a ratio against what N and R found** (§0.06), so this section is not a
claim to have passed it. A full pass belongs to the `ners` skill, which owns the method. What is
claimed here is narrower and checkable: the design adds three fields and five terms, and the stage
structure is read off the code rather than imposed on it.
