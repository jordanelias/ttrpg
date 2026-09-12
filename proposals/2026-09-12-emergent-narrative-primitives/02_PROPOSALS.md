# Part B — the proposals, agonist and antagonist

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠ **ED-1094 does not apply to this file.** Merging it ratifies nothing. Every entry is a design
object for Jordan to accept, amend or refuse. Landing this directory changes no `## Status:` line,
no ledger row, no `CURRENT.md` row and no code.

**Method.** Each proposal is stated by an **agonist**, attacked by an **antagonist** holding the
agonist's output and not its reasoning, and closed by a **reconciliation** that carries the residual
rather than resolving it away. Where the antagonist won, the proposal is demoted or withdrawn in
place and the demotion is legible — `P2` and `P5` are both smaller than their first drafts, and the
section that was to be `P1` is now a measurement in §M.

---

## §0 · THE FINDING THAT REORDERED THIS FILE

The read-only interrogation produced one result that moved every other item, and it is **measured**,
not argued.

> **No question in the shipped grammar ever has another person as its referent — so no candidate
> ever has another person as its subject.**

The chain, at `file:line`: Q1's referents are docket matters (`queries/world_q.py:194-200`); Q2
admits a claim only if `c.subject == p.id or c.subject in mine`, and `mine` is the objects of a
person's own live tenures — rungs, offices, propositions (`:191, :213`); Q3 is a site band
(`:234-238`); Q4 is a proposition. A candidate then takes its subject **from the question**:

```python
for subject in q.referents:                              # decision/options.py:93
    …
    out.append(Candidate(verb, subject, why=q.source, …)) # decision/options.py:102
```

**Measured on this tree, 2026-09-12**, by instrumenting `opening_set` across the corpus run:

```
distinct person ids built across corpus:      3
opening_set calls                      :  6,714
candidates formed                      : 177,170
  subject == the asker                 :  17,400
  subject == a person OTHER than asker :        0
```

Person ids **do** reach candidate subjects — 17,400 times — and every one of them is the asker
naming themselves. **Across 177,170 candidates the engine never once forms a candidate directed at
another person.**

**Three consequences, and they are why this file is ordered as it is.**

1. **`W-F` as specified is a producer with no consumer.** `U5` writes a stance row
   `(referent = actor, valence, weight)` onto the **subject** of a contested act
   (`workplans/2026-09-09-r-execution-plan.md:1336`). `stance_toward(p, c.subject)` reads those rows
   against a candidate's subject (`decision/choose.py:302`). **A candidate's subject is never
   another actor.** The rows would accumulate and never be read. This is `SKILL.md` §3 disqualifier
   2 running in reverse — a producer whose consumer cannot see it.
2. **The reach bottleneck is not `tie / knot`'s missing effect.** `tie / knot` and `oblige` bind
   their Tenure to the **act's subject**, which is the question's referent — so even with effects
   they open edges to rungs and propositions, never to persons. `mine` cannot gain a person by any
   shipped route. **An earlier draft of this document proposed that effect as *the* reach channel.
   That was wrong and is corrected here rather than quietly narrowed.**
3. **`H-71` is a genuinely separate collision**, not a face of the same one — and closing it is
   necessary but not sufficient: its verbs' subjects are offices, and 0 of 143 cases carry an
   `office.post`.

---

## P1 · A PERSON-REFERENT ROUTE INTO DELIBERATE
### *one clause · the object every other item waits on*

**AGONIST.** Admit, at `queries/world_q.py:213`, a claim whose **subject is a Person id** as a
question, so that a candidate can carry another person as its subject.

That single clause is what makes the rest of the machine reachable. It is not a new system, a new
carrier, a new store or a new clock. It widens one predicate in one question source.

*Why it is lawful rather than an addition.* The precedent is in the same function: `W5` added **Q4
`need`** against §F1's *"exactly three sources, and by nothing else"* (`world_q.py:167-172`), because
without it *"an NPC with a standing ambition and a quiet season forms no candidates at all."* The
design documents point at this one directly — `references/design_rulings_2026-09-06.md:287-289`:
*"build the consumer that makes a person form a candidate **from what they came to believe**"* — and
`R-07` requires **relationships**, which have no field and, as §0 shows, no referent either. And
`AX-2` leaves exactly one door: `choose` receives no World, so **the ledger is the only route by
which one person can reach another**.

*What it buys, named against the requirements rather than asserted.* `R-01` and `R-02` (both
`not_met`) block on `W-F`; `W-F`'s consumer is dead without this. `R-07`'s *attitudes and
relationships* cannot exist while no candidate names a person. `R-08`'s *inclination breaks a tie*
is `stance_toward`, which cannot fire toward anyone.

**ANTAGONIST.** Four attacks, and the fourth lands.

1. *"This is `H-84` renamed."* — **Fails.** `H-84` is that no verb moves a **Record**; this is
   about which **claims raise questions**. `H-84` narrowed in 2026-09-03 precisely because a telling
   already deposits a claim without a Record moving. Different object, different hole.
2. *"It re-opens the salience refusal — you are choosing which claims matter."* — **Fails, and the
   distinction is the one `07_DYNAMICS.md:182-184` itself draws.** The refusal is on ranking by
   *importance*. A predicate on the **subject's type** is a bound on *who could be concerned*, which
   is the bound the same sentence licenses.
3. *"It makes a person omniscient about other persons."* — **Fails.** The claim still has to be in
   that person's **own ledger**, deposited by the fan-out they were actually in. Nothing widens what
   they know; it widens what they may form a candidate about.
4. **"It will flood the candidate set, and the flood has a measured denominator."** — **This one
   lands.** 177,170 candidates already form across the corpus against a budget of 5 scene-actions
   per person. Admitting every witnessed actor as a referent multiplies the referent set by the cast
   and the person still gets five actions. `H-54` takes **one question per person per season**, so
   the new class competes for the single slot rather than adding one, and `H-111` — *whether a
   failure should occasion a decision* — gains stake it did not have. **Content hashes move and R3
   moves with them.**

**RECONCILIATION.** The proposal stands and **its scope does not**. What is proposed here is the
clause; **which claims qualify is the `CLAUDE.md` §0 step-5 call, and it must be argued in the
landing commit rather than settled in this document.** The two candidate readings — *every witnessed
actor* versus *a narrower predicate* (a live tenure, a prior telling, a named subject) — differ by
roughly the size of the cast, and the antagonist's denominator is the reason the narrow reading
should be tried first.

**Falsifier, already run and reading the wrong way today:** instrument `opening_set` over the corpus
and count candidates whose subject is a person other than the asker. **It must read zero now** — it
does, over 177,170 candidates — **and non-zero after.**

**Residual.** This makes a person *formable-about*. It does not make them *reacted to*: that is
`H-62`, and `R6` is the standing warning — *"propagation without reaction is a chronicle, not a
game."* P1 is the channel; `W-F` is the reaction; **neither works without the other, and the tree
currently has the second planned and the first unnamed.**

⚠ **THE STRONGEST WARRANT FOR THIS CLAUSE IS NOT AN ARGUMENT BUT A CONFORMANCE GAP, AND IT IS ENTIRELY
RATIFIED.** Four steps, each cited, no design judgment between them:

1. **A `Tenure` is owned by its subject.** `state/carriers.py:387-388` quotes the class's own
   docstring — *"S15 — THE ONE EDGE. Owned by its SUBJECT (S15.1)"* — and `:378`: *"a Person owns every
   Tenure whose subject they are."*
2. **A `hold`'s subject must be a Person.** Ratified Layer 1,
   `architecture/meta/04_CODE_ARCHITECTURE.md:181` row 12: `hold` with a Proposition subject →
   **"`hold`'s subject is a Person, only"**, reasoned *"an edge whose subject cannot act is not a
   relation."*
3. **A computed act's subject is its question's referent.** `decision/options.py:307-310` — `subject`,
   `to` and `site` are *"three cell-side names for the one thing the person was asked about."*
4. **No question source produces a person as a referent** — the measurement above.

**Therefore no computed act can create a `hold`, and the measured *0 live `hold` tenures across 86
worlds* is not a thin fixture but the arithmetic of steps 2 and 4.** Layer 1 already requires a Person
subject; the running grammar cannot supply one. **P1 is the clause that makes ratified Layer 1
satisfiable**, which is a stronger claim than the agonist above makes for itself, and it moves this
proposal from *a good idea* to *a Layer-1/Layer-2 conformance repair* — the one category `CLAUDE.md`
§0's step-5 gate says to take without escalating.

---

## P2 · `tie / knot`'s EFFECT BODY — AS TWO DIRECTED EDGES, WITH ITS NOTE CORRECTED
### *demoted from this document's first draft; still worth landing, and second*

**AGONIST.** `tie / knot` (`verb_table.yaml:707-716`) is `grade: ruled`, has **no precondition at
all** (`requires: "—"`), writes one field (`Tenure.since`) and emits `bond.formed`. It fails exactly
one of `resolvable_verbs()`'s three gates (`loop/driver.py:72-83`): it has no effect body. The
primitive it would compose on already exists and is specified —
`_open_tenure(w, subject, obj, kind)`, idempotent, returning touched ids, `[]` on an already-live
edge so the fold's write-nothing guard emits the row's refusal.

**And the effect must open two directed edges, not one.** `04_CODE_ARCHITECTURE.md` §A.3 — *"Fifteen
differences from the chain"* — row 9 at `:178`:

| # | the chain | this | forced by |
|---|---|---|---|
| 9 | `tie`/`knot` stored once on the lower id | **two directed edges**; strain is a Query | §E.1.3 |

`01_AXIOMS.md` §E.1.3 gives the argument: stored once on the lower id, *"the **other** person owns
nothing and by `T-m` cannot end a relation they are inside. **Whether you can walk away from a bond
would depend on an id comparison**, which is not a thing the fiction can express."* The ruled shape —
*"two directed edges, each owned by its subject. A tie is a **regard**, and regard was never
symmetric"* — buys one case free that D1 §VII.6 rates the most narratively potent epistemic
mechanic: ***"I have cut you off and you do not know it."***

**`engine/season/verb_table.yaml:711` still carries the superseded rule** — `requires_note: "stored
once, on the lower id (§15.1)"`. Nothing executes a note, so this is not a misbehaving mechanism. It
is a superseded instruction sitting exactly where whoever writes the effect will read it, and an
effect written from it would implement the rule Layer 1 corrected. **Correct it in the same change.**

**ANTAGONIST.** Three attacks; two land.

1. *"This is the reach channel — it is P1's job and P1 is cheaper."* — **Lands, and it demoted this
   proposal.** §0 shows `tie / knot` binds its Tenure to the act's subject, which is a question
   referent, which is never a person. **Without P1, this effect opens edges to rungs and
   propositions and changes nothing about who can reach whom.** This document's first draft had it
   the other way round.
2. *"It is not free — name the cost."* — **Lands.** The bodies are ~60 lines for the group, and the
   tree has already measured what landing them costs: **six red tests, five of which are honest
   re-pins of sets that grew by exactly these verbs, and a sixth that is not a number** — a test
   asserting there are exactly two distinct executed-set signatures *"differing by `tell` alone"*,
   which becomes four. That is **a structural claim falsified in the good direction**, and the plan
   is explicit that it must be *"argued rather than edited"*, because `CLAUDE.md` §7 names
   re-pinning as the uncontrolled path.
3. *"Two edges violate `AX-4`'s one-owner rule."* — **Fails.** §E.1.3 answers it in advance: the two
   edges are two **regards**, each owned by its subject; **strain** is the *interaction* of two
   owners' values and by `T-a` is a **Query**, stored nowhere. The counter-argument is named in the
   axiom and survives there.

**RECONCILIATION.** Land it **after P1**, in the same arc, with the note corrected and the sixth
test argued rather than bumped. On its own it is a verb becoming resolvable; with P1 it is the
relationship channel D1 §VI.1 and D3's opinion family both require.

**Residual.** `oblige` sits in the same group and `carry` becomes reachable only **after `petition`
executes** — sequence `petition` before `carry`. And ⚠ **do not route `_eff_confer` through
`_open_tenure`**: conferral is open-and-close on a single-holder row, while duties and designations
are additive — the same `writes:` column, a different operation.

---

## P3 · THE DEPOSIT STAMPS THE ACT, NOT THE CHANNEL
### *one argument · and scoped down from its first draft*

**AGONIST.** `witness.py:121` mints every claim as `src = "firsthand_via_knot" if via_knot else
"firsthand"`. That is a **channel** label. The roster already declares four values —
`[firsthand, told_by, inferred, firsthand_via_knot]` (`rosters.yaml:112-119`) — and `told_by` and
`inferred` are written **only by probes**. So **a telling and a murder deposit identically-sourced
claims**, and nothing downstream can tell a thing someone told you from a thing you saw.

Make `src` depend on the witnessed Event: where the depositing Event is a telling and the depositor
is not the actor, `src = "told_by"`.

*Why it is lawful, and this is the precise part.* The deposit **is** a gated write —
`witness.py:145` calls `w.write("claim_ledger", WriteClass.INTERIOR, …)`. But the gated pair is
**`(Person, claim_ledger)`**, not `(Claim, source)`: `write_matrix.yaml:168-174`, steps `[WIT]`,
class `INTERIOR`, `social: false`, with the warrant *"DR-3 · §20 makes `witness` the only minter,
**and it is not an act**."* A `Claim`'s own fields are set at construction, **upstream of the gate**.
So this touches no matrix row, needs none, and cannot refuse. **And that is exactly what keeps it
clear of `H-62`:** P3 is not an act writing an interior — it is the declared minter stamping what it
already mints. `H-62`'s six rows are all `social: true`; this one is `social: false` *because witness
is not an act*.

*What it buys.* R7's own yield list asks for it by name — *"rumour vs record graded by
`Claim.confidence`, which exists and already decays"* — and that grading is unreachable while every
claim is firsthand. It also breaks a measured dominance: `utter` and `tell` share `eligibility:
["own"]`, and for the intent *another person comes to hold something* `utter` reaches it with no
precondition and no contest while `tell` carries a typed precondition and resolves at 21%
(`verb_table.yaml:735-742` against `:504-515`). A `told_by` stamp is a purchase **only a telling can
buy**.

**ANTAGONIST.** Two attacks; the first lands hard.

1. **"You claimed this revives `standing_of`. It does not."** — **Lands, and it cut this proposal in
   half.** `agreement` pairs claims **by predicate** and only over a roster —
   `own_by = {c.predicate: c for c in own if c.predicate in PERSON_PREDICATES}` (`options.py:434`) —
   and that roster is `[heritage, grade, church_standing, office, residence]` (`rosters.yaml:232-241`).
   `witness.py:133` mints `predicate = e.kind`; the `W-B` channel mints `stores:<kind>`, `condition`,
   `contain.path:<to>`. **Neither ever mints a person predicate**, `PERSON_PREDICATES` has exactly one
   consumer, and **nothing writes `Person.marks`.** So `paired == 0` always and `standing_of` returns
   `condition_scale` **whether or not anything is stamped `told_by`.** Reviving it needs **three**
   producers, not one. See §M2.
2. *"Then it buys nothing."* — **Fails.** It buys the distinction itself, in every ledger, at one
   argument: hearsay becomes separable from testimony for any later reader, which is the precondition
   D3 calls *belief-with-provenance* and grades *"the most interesting primitive in the set."*

**RECONCILIATION.** Proposed **without** the `standing_of` claim. The claim that may be made is
**"hearsay becomes distinguishable from firsthand"**; the claim that must be stated as a limit is
**"`standing_of` becomes live"** — it does not, and §M2 says what would be needed.

**Residual.** Sufficiency has a second condition this document did not measure: a telling reaches a
person as a claim *about themselves* only where they are among that telling's observers under the
shipped `all_five` fan-out. Necessary; sufficient only there.

---

## P4 · `UPSET_FLOOR` — LET THE SEAM ACCEPT `wound_state`
### *a deletion, not an addition · PC lane · answerable by precedent*

**AGONIST.** D1 §II.5 recommends Meier's RNG massage as the mechanism that makes randomness read as
fate. **Valoria shipped it** — `combat_engine_v1/config.py:295`, `UPSET_FLOOR=0.05`, applied at
`wrapper.py:493` — **and `H-119` measured what it cost**: over 300 seeded fights *the reported winner
is the FELLED fighter in 6.06%*, cross-confirmed at 28 of 595 losers not at health 0. The code's own
comment concedes it: *"no in-model event corresponding to the reversal."*

D1's own VII.2 is the test that condemns it: *"A dwarf who does not haul the stone because he is
praying is a character. A unit that does not move because of pathfinding failure is a bug."* Here
the winner is the fighter the model felled, and nothing in the model accounts for it.

**The seam returns two degree surfaces and names the second as the source.** Accept `wound_state` —
which is what the seam's own docstring already says — and the contradiction closes with no new
object.

**ANTAGONIST.** *"`UPSET_FLOOR` is Jordan's, tagged `[DESIGNER RULE — Jordan]` and ED-PC-0036.
Touching it overturns a ruling."* — **Half lands, and the halves must be kept apart.** The
*disposition* is Jordan's and is not in question: the 95% cap is a stated videogame design choice
and this document does not propose removing it. The *defect* is not a disposition — it is two
surfaces of one seam disagreeing — and `H-119` itself records it as **answerable by precedent
rather than escalation**, on Jordan's 2026-09-04 ruling that the combat engine determines the result
and the caller accepts it.

**RECONCILIATION.** Filed as an **observation for the PC lane**, not as IN-lane work: this session
allocates an IN id and touches no PC file. Whoever takes it should either apply the massage *before*
`WoundTracker` writes, or have the seam read `wound_state` — and should not remove the constant.

**Residual.** Not re-measured this session; `H-119`'s 6.06% is the register's figure, cited as such.

---

## P5 · THE WARRANT FOR `W-F`'s MAGNITUDES
### *narrowed sharply by the interrogation; what survives is smaller than it looked*

**AGONIST.** `U5`/`W-F` is specified to the YAML and says of itself: *"**The magnitudes are INVENTED
and this row is what makes that lawful**,"* with a sweep of `[declared, none, doubled]` and no
evidential basis for `declared`. The documents are a precedent catalogue; supply the basis.

**ANTAGONIST.** *"The tree already warrants the direction without them, and the documents disown
exactly the part it lacks."* — **Lands, and it is most of this proposal.**

The direction is already ruled here: `AX-3` — *"Argument and consequence move what is held right"*
(`01_AXIOMS.md:114`); `H-62`'s supplied shape — *"an interior write is a **consequence of an
outcome**"*; and the band order is ruled at `dice_engine.py:49-52`. **Adopting a precedent catalogue
for direction imports nothing the tree lacks.** And adopting it for magnitude imports what the
catalogue itself disowns — D3 §7.2: *"a catalogue of **folk models**… **not** acceptable for any
claim about a specific constant."*

**RECONCILIATION.** Two directions survive, and only two:

1. **An outcome moves the *subject's* stance toward the *actor*** — which is `W-F`'s own shape, and
   the documents corroborate rather than establish it.
2. **Monotone in band** — Overwhelming ≥ Success ≥ Partial. The ladder is ruled; this is arithmetic
   on it.

**One further direction is corroborated and worth recording, because it converts an arbitrary plan
choice into a warranted one.** D1 §VI.2: *"decay governs the episode; permanence governs the arc.
A system with only decaying state cannot produce an arc; a system with only permanent state cannot
produce an episode."* Valoria decays `Claim.confidence` at `5` per season against a default of `100`
— a memory fades over ~20 seasons — and `W-F` proposes stance with **no** decay. **That split is
Dwarf Fortress's**, which D1 rates the only configuration with all five properties. The plan chose
it; the document says why it is right.

**What stays open, and the split matters:**

- `[OPEN — Jordan tuning]` — every `stance_delta` cell (four bands × the two contested verbs), the
  weight column, and size relative to `condition_scale`.
- `[OPEN — Jordan]`, as a **design call and not a tuning** — **the sign of `Failure`**: whether a
  lost telling *sours* the listener or writes nothing. `Failure: []` is lawful
  (`verb_table.yaml:525-530`) and **no line in the tree rules a negative interior write**. Two
  defensible answers; materially different games.

**Residual.** The sweep tests only that verdicts *move*, not that any magnitude is *right*. No
instrument in the tree can grade a stance magnitude, and this document does not pretend one exists.

---

## P6 · `tell` SHOULD CARRY THE CLAIM IT ALREADY REQUIRES

### *one payload field and one deposit branch · the seam where a telling loses its content*

**AGONIST.** `tell`'s precondition and its effect disagree about whether a telling has content, and
the precondition is the one that is right.

The verb requires the teller to **hold a claim on the subject** — `verb_table.yaml:499`, and
`_req_tell` verbatim: `any(c.subject == subj for c in teller.ledger)`. So at the moment of speaking,
the teller demonstrably holds `(subject, predicate, value, confidence)`. The verb then declares
`writes: []` at every degree and emits `news.told` (`:505-513`), and the witness layer deposits, at
`loop/witness.py:137`:

```python
c = Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own", self.round)
```

Three of the claim's fields are filled from the *event* rather than from the *claim the verb just
required*:

| field | filled with | what the teller actually held |
|---|---|---|
| `predicate` | `e.kind` → the string `news.told` | `is_traitor`, `grade`, `complied` — the thing asserted |
| `value` | hard-coded `True` | the teller's assertion, which may be false |
| `confidence` | `confidence_default`, read once per barrier (`:75`) | the teller's own confidence, already decayed by age |

**So the precondition reads the claim and the effect discards it.** What propagates is *that a telling
happened, about B, and it is true*. `epistemic.py:180-182` rules deliberately that the **subject**
travels — *"A claim minted from a telling is about WHAT WAS TOLD; the teller is not the news"* — and
the subject is the only part that does.

**The carrier needs no change.** `Claim.predicate` is `str` and `Claim.value` is `Any`
(`state/carriers.py:142-143`) — free-typed, deliberately.

**And the harness already constructs exactly the claims this would produce, as its own specification
of required behaviour:**

| probe | `tests=` | what it hand-builds |
|---|---|---|
| **P4** `S3-L2` | *"a character must be able to believe something false and act on it as if true"* | `("p_high", "is_loyal", True, "firsthand")` **and** `("p_high", "is_loyal", False, "told_by")` |
| **P16** `S20` | *"how a character is seen must be able to differ between people who know different things"* | `is_traitor True/told_by` against `is_traitor False/firsthand`; returns *"legitimacy is PER-KNOWER and **flips at TELLING speed**"* |
| **P22-class** | a false report of compliance | `complied True/told_by` against `complied False/firsthand` |

⚠ **Every one of those probes is graded `by="construction"`.** They pass by building the ledger by
hand. **No telling in the running loop can produce any of them** — a telling produces
`news.told / True / 100`. P16's PASS text asserts that legitimacy *"flips at TELLING speed"*; the
ledger it asserts it on is one no telling could write. `CLAUDE.md` §0.1 pt 2 — *an assertion must be
able to observe the failure it excludes* — is the rule that makes this a finding rather than a
preference.

**The proposal:** put the teller's held claim in the `news.told` payload, and at the deposit branch for
that event kind read `predicate` and `value` from it instead of from `e.kind` and `True`. Derive the
deposited confidence from the teller's, constrained to be **non-increasing**.

**ANTAGONIST.** Four attacks. Two land and reshape it; two fail.

1. **"`writes: []` is CORRECT and this breaks it."** — `epistemic.py:107`: *"THIS EXISTS BECAUSE A
   TELLING CHANGES NOTHING. `tell` declares `writes: []` — correctly."* **This lands as a constraint
   and it is the right one.** The carry must not enter the write matrix. It belongs in the **event
   payload and the deposit branch** — the epistemic seam — leaving `tell` writing nothing, exactly as
   ruled. The proposal is scoped accordingly.
2. **"Bystanders would learn the content."** — **This lands, and it exposes a larger absent object.**
   The five channels are `post_remit, co_located, witness_key, document_key, chronicle`
   (`rosters.yaml:110`). **None of them is an addressee.** A `tell` has no receiver operand, so under
   any fan-out mode the people who learn are the people *present or keyed*, never the person told.
   P6 therefore cannot deliver *"I told you, privately, and only you."* A sixth channel is a separate
   and larger object and is **not** proposed here.
3. **"The confidence function is invented — this is `P5`'s defect again."** — **Fails as an
   objection to the shape, holds against any number.** The write is interior, into the holder's own
   ledger, which `L3` clause 1 permits in terms. What is unwarranted is a *magnitude*, so no magnitude
   is proposed: the constraint is `deposited ≤ teller's`, the function is a fixture graded
   `assumption`, swept, **with a loader that refuses an unregistered arm** — `A5`'s lesson
   (`04_CONSOLIDATION.md` §3) applied to the dial this proposal introduces.
4. **"It is a false N-line — `Claim` already carries predicate and value."** — **Fails, and inverts.**
   Disqualifier 1 asks whether the carrier exists *and the possibility survives the cut*. The carrier
   exists and is correctly typed; the possibility does not survive, because **nothing produces a
   content-bearing predicate from an act.** That is disqualifier **2**, no producer — and `P6` is the
   producer. An object whose carrier is right, whose type is right, whose precondition already reads
   the source data and whose harness already asserts the result is the opposite of an addition.

**RECONCILIATION.** Proposed at the **emit/deposit seam only**, with three parts and a named residual.

- **The carry.** `news.told`'s payload gains the teller's claim; the deposit branch for that kind
  reads `predicate` and `value` from it. `tell` keeps `writes: []`.
- **The attenuation.** Deposited confidence is a function of the teller's, constrained non-increasing,
  injected as a swept `assumption` fixture with a refusing loader. **No number is proposed.**
- **The falsifier**, per §0.1 pt 3: a test that runs a telling through the loop and asserts the
  deposited claim's predicate is **not** `news.told` and its value is the teller's. There is no
  `by="run"` probe grade — the four are `construction / convention / no-signature / probe-model` — so
  this belongs in `tests/valoria`, where it can observe the failure. **Its outcome today is RED**, and
  that is the artifact this proposal rests on.
- **Residual, stated because it bounds the gain.** Without an addressee channel a telling still
  reaches the present rather than the told. P6 makes news **content-bearing, falsifiable and
  attenuating**; it does not make it **directed**. Directedness is `P1`'s axis and a sixth channel's,
  not this one's.

**What it moves.** `R-07` and `R-08` (`partial`) — a person can hold a false belief acquired from
another person and act on it, which is `R-08`'s *"decisions must not be omniscient"* at the belief
layer rather than the sampler layer. It is the one proposal in this set that makes **a lie** a thing
the engine can represent.

---

## §M · MEASUREMENTS HANDED OVER — not proposals

Three results that are load-bearing and that **need no ruling and admit no one-object repair**.
Under `CLAUDE.md` §0 a finding that needs no ruling is fixed in this commit or dropped; these are
neither fixable here nor droppable, so they are handed over as measurements with their instruments.

**M1 · The top outcome band is mathematically unreachable, and the structural half is not the
numbers.** Exact enumeration over all 100 two-die outcomes at the shipped fixtures, through the
**discrete** `roll_net` the season seam imports: **FAILURE 74% · PARTIAL 19% · SUCCESS 7% ·
OVERWHELMING 0%.** Reachable nets are `[-2 … +4]`, so the maximum margin is `+2` against a band
needing `≥3`. Pool 3 is the smallest that admits it. Against this, D1 §I.2 measures PbtA and Blades
holding the complication band at **41–45% across the entire competent range**.

**The boundary, stated precisely because getting it wrong in either direction is the failure.** The
*ladder* is Jordan's, ruled 2026-08-14 — at pool 2 no obstacle ≥ 2 reaches Overwhelming, and that is
arithmetic on a ruling, not a defect. The *values* `pool_default=2` / `obstacle_default=2` are
Jordan's tuning, graded `assumption` (`H-126`/`H-127`). **What is structural, and is the audit's
business, is that there is no competence *range* at all:** `Person.capability` has one writer and it
zeroes, so one fixture is the whole cast's pool; `lev` is `0.0` with no producer. **A two-die cast
*should* never overwhelm. The defect is that everyone is a two-die cast** — `SKILL.md` §3
disqualifier 2, no producer, not a number.

**M2 · `standing_of` is `H-116` at a second site.** `agreement` pairs on `person_predicates`; the
deposit side mints event kinds; the two vocabularies are disjoint, so `paired == 0` in every run and
`Sensation`'s second scalar is a constant for every person in every world. `epistemic.py:74-82`
records the identical shape already measured and repaired elsewhere — *"over 4,800 deposited claims
**the two vocabularies were DISJOINT**… The predicate is **DERIVED from the form** now… so there is
**one namespace** and the write side has a name to aim at."* That is the repair direction and it has
a precedent; the repair itself needs **three** producers and is not one object.

**M3 · The two engines disagree about whether a sub-season timestep exists.** `engine/mc_v18.py`
runs a complete second season loop through `engine_clock.run_tick`, whose docstring claims to be
*"the only module that may advance the season counter"* while `loop/driver.py:201` claims *"exactly
one `season()`"*; and `engine_clock.py:6-7` implements a spec stating *"There is no sub-season fixed
timestep"* — which `engine/season/` has. ⚠ **This corrects a commissioned pass**, which called
`mc_v18` a second *clock*. Under `T-c`'s definition it is not: the scene round advances nothing and
`w.tick` moves once. It is a second **owner** of one clock, and a second **world** — an uncarried
vertical direction and a §7.3 *calculations consistent in methodology* defect, which is `R-04`.

**M4 · Two surfaces give `choice_temperature`'s control arm two different meanings.**
`decision/choose.py:141-147` states that the `tau = 0` arm *"SHORT-CIRCUITS TO THE OLD PATH, AND THE
ARM VALIDATES THE PLUMBING RATHER THAN THE SAMPLER… Stated plainly because both prior plans named the
`tau = 0` arm as the sampler's control and neither noticed."* `engine/season/hole_register.yaml:1278`
still describes `0` as *"the pre-U4 argmax kept as the control."* Under §0.05 the code is the
mechanism, so the register row is the stale surface — but **the two are not interchangeable for
anyone reading the sweep**, and §0.1 pt 4 makes a control arm that measures the wrong thing a
measurement defect rather than a documentation one. Related: `Fixtures.get` refuses an unregistered
**name** (`data/fixtures.py:43-50`), never an out-of-sweep **value**, so unlike `fan_out_mode` this
dial has no refusing loader on its arm set. Handed over because naming the sampler's true control is a
`U4` judgment, not a one-line repair.

---

## §R · THE ONE THING TO REFUSE

**Salience-ranked memory** — and it is listed because it will read as obviously good to anyone who
has just read these documents and this evidence.

It is seductive because **the tree records the symptom it appears to cure**: `HANDOFF_IN.md:2521`
notes a person *"observed forgetting a fact and resuming the blocked behaviour"* once the ledger
evicted at 200. Every reader will reach for *keep what matters*.

Against the tree: the comparator is `c.confidence * (c.when + 1)` (`witness.py:245`), **STRUCTURAL by
signature** (`04_CODE_ARCHITECTURE.md:972` row 39), and the reason is not tidiness —
`07_DYNAMICS.md:182-184`: *"Bound it by importance and you have built salience-ranked memory, which
is a narrator deciding what matters — **the actor the design exists to refuse.**"* The same symptom
was **already fixed once, lawfully**, by channel predicates (678 → 68 deposits). And forgetting is
**load-bearing fiction**, not a bug: *"He loses the town by being forgotten… what happens when nobody
spends a scene renewing the claim."*

A ledger that protects important claims deletes that mechanic and reintroduces an omniscient ranker
through the one field `AX-2` keeps private.

**Residual.** The **cap** is an `assumption` fixture. A reader who wants less forgetting turns
`ledger_cap`, which is Jordan's tuning — **never the comparator.**

---

## §S · THE SET AT A GLANCE

| | what it is | size | waits on | moves |
|---|---|---|---|---|
| **P1** | a person-referent route into DELIBERATE | **one clause** | nothing | the consumer for `W-F`; **makes ratified Layer 1's `hold` satisfiable**; `R-01`/`R-02`/`R-07`/`R-08` |
| **P2** | `tie / knot`'s effect, as two directed edges, note corrected | one effect body (~60 lines), six re-records | **P1** | `R-05`; the relationship channel |
| **P3** | the deposit stamps the act, not the channel | **one argument** | nothing | hearsay ≠ testimony; breaks the `utter`/`tell` dominance |
| **P4** | `UPSET_FLOOR` — accept `wound_state` | a deletion | — | an attribution contradiction measured at 6.06%. **PC lane** |
| **P5** | the warrant for `W-F`'s magnitudes | prose, two directions | `W-F` | converts *invented* into *warranted* for two cells; one **design call** surfaced |
| **P6** | **`tell` carries the claim it already requires** | one payload field, one deposit branch, one swept fixture | nothing | **a lie becomes representable**; news attenuates; `R-07`/`R-08`. Makes `P4`/`P16`'s `by="construction"` assertions reachable by the loop |
| **M1–M4** | measurements handed over | — | — | no ruling, no one-object repair |
| **§R** | the refusal | — | — | — |

**Ordering, since three of the six now interact.** `P1` first — it is the conformance repair and every
reach-shaped item waits on it. `P3` and `P6` are independent of `P1` and of each other, and they
compose: `P3` puts a **speaker** in `source`, `P6` puts **content and attenuation** in `predicate` /
`value` / `confidence`. Landed together, a claim acquired from another person carries *who said it,
what they said, whether it is true, and how far it has travelled* — which is the whole of
belief-with-provenance, and `04_CONSOLIDATION.md` §3 `A9` records that the corpus finds it in **two of
twenty titles**. `P2` after `P1`. `P5` rides `W-F`. `P4` is the PC lane's.

**Nothing here adds a system, and P6 does not change that.** Five of the six proposals are a clause,
an argument, an effect body composing on an existing primitive, a deletion, and a payload field read at
one branch. **No new `needs_jordan` row is filed** (`03_PROVENANCE.md` §6); one genuinely open **design
call** is surfaced inside P5 and attaches to a plan Jordan already owns.

**Two named gaps are deliberately NOT proposed**, because each is one object short of a proposal above
and its shape is decided by that object: an **addressee channel** (a sixth witness channel, so a
telling reaches the told rather than the present — `P6`'s residual), and a **`Tenure.term`** field
(`04_CONSOLIDATION.md` §2 `A`, withdrawn to a warrant because `verb_table.yaml:421` already records it
as a located scope decision).
