# 02 · THE WRIT AND THE WORD — how authority descends without broadcast

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · id: **ED-IN-0234**. Grade under `CLAUDE.md` §0.2: **`paper`** — nothing in this file
## executes. §C.5 names the artifacts that would move it, in order, and no row here may be cited as done.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *competing-considerations judgment,
## multi-doc synthesis*), against the working tree at 2026-09-17. The specification this file writes
## from was a read-only `fable` planning stage; the measurements in §0.2 were taken by this file's
## author **by running the harness**, not by quoting a prior pass. Every `path:line` below was opened at
## that line in this session; the **APPENDIX** lists the citations I inherited that were wrong and the
## four claims I inherited that were **false verifications**, all repaired.
## ⚠ Citation discipline, suite-binding: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, cited
## **`ARCH §Letter.Number`** and **never by line** — its lines have drifted twice. **`AX`** =
## `architecture/meta/01_AXIOMS.md`, cited `AX-n` or `AX §Letter.Number`. **`holonic §NN.N`** =
## `architecture/holonic_ARCHITECTURE.md`, with a line in parentheses as a finding aid only. A bare
## **`01`/`02`/`03`/`04`/`05`** means a file in **this** directory. `path:line` is for engine files only.
## This file's falsifiers are **`WW-n`** and its loops **`WW-L±n`**.
## Supersedes: round one's `01_SEATS_AND_POLICY.md` **policy half entire** — the `in_force` walk, the
## seven place-keyed clauses, `reach: all`, the `sit:` clause, the `ttl` lapse, and **RR-1**. Its **seat
## half** is `03`'s, not mine. Corrections to my own sources are **struck and kept**, never deleted.

---

> **Jordan, 2026-09-17, four rulings, in the order they arrived. All four bind this file.**
>
> **1 · on noise:** *"what reaches a hamlet better correspond to some degree what the Duke wrote down.
> yes there needs to be noise and slippage and interpretation, but the game can't function as a game
> where the player can feel their choices mattering if all dissemination of information is so noisy
> that it's moot."*
>
> **2 · on the medium:** *"A document from the Duke isn't like a game of telephone — the written letter
> in some form with fidelity would end up being directly given to the settlement leader."*
>
> **3 · on speed:** *"speed of a writ can be the same as word of it given that the message can be
> delivered directly as required to those who must implement it."*
>
> **4 · the principle, which is `RR-P`:** *"the player must have the sanctity of their
> choices/actions/decisions preserved in terms of the contents of those choices/actions/decisions
> themselves — the worldly churn is in how those contents are received and acted upon by others."*

> **And the two Layer-1 passages this file exists to apply**, `holonic §37.1` (:1282-1293) and
> `holonic §37.2` (:1297-1299), quoted whole in **§A.2** and never paraphrased:
>
> ```
> Dispensation := (id, issuer, proposition, scope, terms[])   -- NINE typed terms, no bare effect field
> ```
> *"It travels by being noticed, NOT DOWN A CHAIN OF POSTS."* · *"A published dispensation does not
> apply — it lands as a compliance contest, per relevant Rung, through `contest`, and SCOPE ENUMERATES
> EXECUTORS, NOT PLACES."* · *"Delivery is not assumed, and an executor who never received it is
> DISTINCT from one who received it and refused."* · *"The person's own need, plus capability, plus this
> new **claim**, yields an opening through the same `opening_set(person, view)` any act comes through…
> **No one authored an opportunity for anybody.**"*

---

# PART 0 · THE CONFORMANCE DIVISION, AND IT IS THE SPINE OF THIS FILE

**Almost none of what follows is new design.** `holonic §37.1` specifies the downward mechanism;
`ARCH §B.5` already ruled that `Dispensation` becomes a `Record` kind; `ARCH F.10` already picked
receiver-side distortion; the ratified program's positions 15 and 16 already instruct the fold and the
verb. What was missing is a **schema**, a **mover**, and a **deposit** — three things, and `ARCH F.15`
says so in terms: *"not an assumption so much as an absence: the entire downward mechanism has no
executable content, and `issue` produces a document nobody can comply with."*

**Read the three lists before reading a claim.** Do not credit a CONFORMANCE item as new design, and do
not read an EXTENSION as ratified.

## §0.1 · The three lists

**CONFORMANCE — ratified Layer 1 or a ratified program position, merely unbuilt. This file supplies no
design here; it supplies the missing content.**

| # | the item | where it is already ruled |
|---|---|---|
| C1 | `Petition` and `Dispensation` are **kinds of `Record`**, not types | `ARCH §B.5` — *"**Synthesis call — `Petition` and `Dispensation` become `Record` kinds.**"* |
| C2 | the fold's cost and benefit | `ARCH §B.5` — *"folding them in means `forge`, `destroy_record`, `hold` and `carry` reach them with no new rows, and two existence rows collapse into one"* · **Cost:** *"the nine typed dispensation terms become a schema for one Record kind and remain unspecified"* |
| C3 | a `Record` is held by a **`hold` Tenure**, one per object, never a field | `holonic §15` (:538) — `hold : Person → Office \| Rung \| Record \| Proposition`, **1 per object**, *"office-holding, tenancy, custody"* |
| C4 | one two-party verb moves a Record; it closes the giver's hold and opens the receiver's | ratified program **position 16** (`workplans/2026-09-11-reconciled-program_part2.md:452-455`) — *"One two-party verb (name it against `VOCABULARY.md` before adding the row): `own` + `hold:<record>` eligibility, writing the holder's `hold` closed and the receiver's open. This is the first verb in the vocabulary that moves a Record to another person — **without it no second person ever holds one**"* |
| C5 | the Record-kind fold, including the two `World` dicts and the two matrix rows | ratified program **position 15** (`_part2.md:439-443`) |
| C6 | distortion is **receiver-side** | `ARCH F.10` — assumed: *"receiver-side, per the chain's held-back closure"*; if wrong, *"`terms.distorted` needs a mutable emitter-side object, which §37.1 forbids"* |
| C7 | the implementer must pick a side and write it down | `holonic §37.4` — *"this document does not pick one … When you implement, pick one, write it down beside the code, and expect the choice to be revisited"* |
| C8 | scope enumerates **executors**, and an office-cluster has no place | `holonic §37.3` rows 3-4; and `engine/season/harness/probes.py:1148-1160` already asserts it on a `rung is None` Dicastery whose executors sit outside the settlement's subtree |
| C9 | an order **carries terms like a dispensation** | `ED-IN-0210` as **RULED by Jordan 2026-09-15** (`registers/editorial_ledger_in.jsonl:104`) |
| C10 | a Record's clock runs only while a living person holds it | `engine/season/loop/matter.py:73-78`, **already running** |

**EXTENSION — new, and each names the shipped thing it composes on rather than replacing.**

| # | the item | composes on |
|---|---|---|
| E1 | `record_kinds` — a per-kind `subject_matter` key schema, refused at the constructor | `Office.__post_init__`'s remit-act refusal, the precedent `engine/season/state/world.py:240-241` cites by name |
| E2 | `issue` as a `create_record` body with a kind and an address | `_eff_create_record` (`loop/effects.py:263-290`), which already mints the Record (`:284-285`) **and** the maker's hold (`:288-289`) |
| E3 | `give` and `_req_give` | `_eff_confer`'s close-priors-then-open shape (`loop/effects.py:118-126`), applied to a Record instead of an Office |
| E4 | the **one deposit rule** — holding a Record deposits a `content:<kind>` claim | the `document_key` channel, which already reads `changes[]` (`epistemic.py:331-333`), and the WITNESS deposit block (`loop/witness.py:270-279`) |
| E5 | `_told_content` returns a **lossy copy at `Partial`** | the told channel (`loop/witness.py:315-369`), whose deposit already exists and is **degree-blind** |
| E6 | `_derive_operand` reads `to`/`at`/`kind`/`amount` off a `content:` claim's value | `store_kind_of` (`decision/options.py:234-256`), which already reads a matter kind off a claim's predicate |

**DEPARTURE — this file overturns something. Two, and both are named as ruling requests in §C.6.**

| # | the departure | the request |
|---|---|---|
| D1 | `comply`, `evade / defy`, `refract` and `dispatch` are **deleted as rows**, which overwrites the *letter* of `ED-IN-0210`'s 2026-09-15 ruling while (I argue) keeping its substance | **RR-A** |
| D2 | `ARCH §B.5`'s *"nine typed dispensation terms … remain unspecified"* becomes *"a Proposition and an address"*, and `ARCH §C.6`'s mint table gains a content row | **RR-B**, owned by `05`, quoted here and **not edited** |

⚠ **`levy`'s deletion is NOT a departure and not part of RR-A.** It is `CLAUDE.md` §0 gate 5 — a state
write at a place with no contest is precisely the shape `holonic §37.3` row 2 forbids, and its own verb
row already confesses the eligibility was substituted off-register (`verb_table.yaml:359`). §A.19.

## §0.2 · What I measured today, rather than quoted

Per `CLAUDE.md` §0.1 pt 3 — *"'X is absent / dead / never fires': RUN the thing that would show
presence"* — and pt 4, *a number without a control is not a measurement*. Every figure below was taken
on **2026-09-17** by this file's author and **carries the command**.

| measured | value | command |
|---|---|---|
| verb rows · resolvable | **38 · 18** | `python -c "from engine.season.loop.driver import resolvable_verbs; from engine.season.data.verbs import VERB_TABLE; print(len(VERB_TABLE), len(resolvable_verbs()))"` |
| `@effect_for` bodies | **11** | `grep -c '@effect_for' engine/season/loop/effects.py` |
| `REQUIRES_PREDICATES` members | **5** — `confer, convene, dispatch, release, revoke` | `python -c "from engine.season.loop.predicates import REQUIRES_PREDICATES; print(sorted(REQUIRES_PREDICATES))"` |
| matrix rows · `Record` rows | **40 · 5** (`exists, forgery_quality, matured, stages, ttl`) | `grep -c '^  - kind:' engine/season/write_matrix.yaml`; `grep -n 'kind:    "Record"' -A1` |
| **`issue` is resolvable** | **False** — it writes `Dispensation.exists` and has no effect body | as row 1, printing `'issue' in resolvable_verbs()` |
| **`comply` / `evade / defy` / `refract` are resolvable** | **False, all three** — prose `requires` with no registered predicate | as above |
| **`dispatch` is resolvable** | **True**, and person-side **unformable** (`remit:dispatch` declines, `H-71`) | as above; `decision/options.py:163-165` |
| **`forge` is resolvable** | **False** — no effect body | as above |
| `w.records` / `w.dispensations` / `w.petitions` **at build** | **0 / 0 / 0** | `build_realm(0)`, then `len(w.records)` etc. |
| **`w.records` after ONE populated season** | **69** | `build_realm(0)`; `run(1, 0, w=w)`; `len(w.records)` |
| …their `kind` | **`text`, 69 of 69** | `Counter(r.kind for r in w.records.values())` |
| …their `subject_matter` | **`None`, 69 of 69** | `sum(1 for r in w.records.values() if r.subject_matter is not None)` → 0 |
| …their `forgery_quality` | **0, 69 of 69** | as above |
| …live `hold`s on them · distinct holders | **69 · 36** | a `w.tenures` filter on `t.object in w.records` |
| …their `rung` field holding a **person** id | **69 of 69** | `sum(1 for r in w.records.values() if r.rung in w.persons)` |
| live holds at build, by object class | **35 = 19 `Office` + 16 `Rung`** · **0 `Record`** | `Counter` over `t.kind == "hold" and t.live` |
| event histogram, one populated season | `claim.deposited 2175 · finding.none 85 · condition.worn 74 · **record.created 69** · proposition.uttered 54 · finding.made 52 · work.unavailable 38 · yield.taken 37 · stores.changed 37 · travel.blocked 23 · news.untold 22 · release.refused 18 · **transfer.refused 16** · speech.made 13 · **news.told 8** · travel.moved 3` | `Counter(e.kind for e in w.log)` |
| **`dispensation.issued` · `compliance.given` · `order.given` · `record.forged` · `transfer.made`** | **0 · 0 · 0 · 0 · 0** | the same histogram — **absent from it** |
| **the degree of every successful telling** | **`Partial`, 8 of 8** | `Counter((e.kind, e.degree) for e in w.log if e.kind in ('news.told','news.untold'))` → `{('news.untold','Failure'): 19, ('news.told','Partial'): 8, ('news.untold','Partial'): 2, ('news.untold','Success'): 1}` |
| claims by source, one populated season | `{firsthand: 2174, told_by: 1}` — **`inferred` 0, `firsthand_via_knot` 0** | `python -m engine.season.harness.populated 1` |
| `"inferred"` as a string literal in `engine/season/**.py` | **0 occurrences** (7 mentions, all prose) | `grep -rn '"inferred"' --include=*.py engine/season` |

> ### **RULED: the writ's CARRIER already runs sixty-nine times a season, and carries nothing.**
> This is the most important number in the file and it inverts the shape of the problem. A reader
> arriving at `ARCH F.15`'s *"the entire downward mechanism has no executable content"* will reach for a
> new object. **There is no new object to reach for.** `create_record` is one of the eighteen resolvable
> verbs, it is `own`-eligible so any person forms it, and it executes **69 times in the first season of
> the populated world** — minting 69 Records, held by 36 distinct persons, every one of `kind: "text"`
> with `subject_matter: None`. The custody relation runs. The maturation clock runs. The deposit channel
> runs. **What is missing is a kind, a payload, a mover, and a claim** — and each of the four is one
> edit to a body that already exists.

⚠ **AND THE `0 records` FIGURE IN CIRCULATION IS A BUILD-TIME COUNT PRESENTED WITHOUT ITS CLOCK.**
`AUDIT_VERDICT.md`'s measurement block reads *"0 records, dates, docket, crossings"*. That is true of
`build_realm(0)` **before the season runs** and false of the same world after it. I reproduced both; the
appendix records the repair. A session planning against `0 records` would conclude the Record family is
unreachable from any person's decision, **which is the opposite of the case.**

## §0.3 · Five claims this file does NOT make

1. **No latency, speed or distance parameter, anywhere.** Jordan ruled speed **equal** (epigraph 3).
   There is no travel-time model here and none is smuggled in as a fixture. §A.10.
2. **`Partial` never corrupts the writ.** The lossy copy is written into the **hearer's ledger** and
   touches no `Record` and no other person's ledger. §A.9.3.
3. **Seizure does not resolve.** Forced compliance needs a contest between the lord's men and the
   holder, and no provider supplies one. §A.18 states it as a LIMIT and does not dress it.
4. **`RR-P` is not settled.** Every claim here that leans on it says *under RR-P*. §A.20, §C.6.
5. **Nothing here is graded above `paper`.** §C.5. In particular **`dates: 0`** stays 0 until `convene`
   is formable, which is `03`'s and the proceedings build's, not mine.

## §0.4 · Round one's reading defect, named exactly, because it is instructive

Round one built `in_force(w, rung, clause)` — a walk from a rung up the containment ladder looking for an
ancestor whose live dispensation carried a clause, read at MATTER. It honoured `holonic §37.3` row 3
(*"a `scope` that enumerates places"*) by putting the scope on people, and then **broke rows 1, 2 and 4
at the read site**: a clause the Duke wrote became a condition the province satisfied, with no person in
between, no delivery, and no distinction between an executor who never heard and one who refused.
`AUDIT_VERDICT.md` made this MUST-BE-STATED-AS-A-LIMIT finding 1.

**The mechanical cause of the reading error is worth naming because it will recur.** §37.3 is a table of
**prohibitions**. §37.1, five lines above it, is the **specification**. A reader who opens §37 at the
table — which is what a grep for *"broadcast"* lands on — gets four things not to do and no thing to do,
and then designs the mechanism from scratch under four constraints. **Design under constraints produces
the nearest lawful shape to what you already had in mind.** Reading §37.1 first produces the shape the
architecture actually specifies, and it is not a walk at all:

> **a typed document, carried by a person, noticed by whoever notices it, answered by their own act.**

⚠ **This is `CLAUDE.md` §0.1 pt 3's *"as `F` says at `:L`"* row at the scale of a section.** Round one
cited §37.3 correctly, quoted it correctly, and honoured the wrong three quarters of §37 — because it
opened the part of the section that names the failure and not the part that names the mechanism.

---

# PART A · THE CLAIMS, EACH WITH ITS VERDICT

## §A.1 · THE PRINCIPLE — *the act is inviolate; the reception is not* · **UNDER RR-P**

**It is first in PART A because it governs every claim after it**, and because it is the one thing in this
suite that binds subsystems this file never touches.

**Jordan, verbatim:** *"This applies to the entirety of the game: the player must have the sanctity of
their choices/actions/decisions preserved in terms of the contents of those choices/actions/decisions
themselves — the worldly churn is in how those contents are received and acted upon by others."*

### §A.1.1 · The test, in one sentence

> ## **A draw may decide what HAPPENS. It may never decide what you MEANT.**

### §A.1.2 · The three boundaries, so the test cannot be over-read

1. **Narrowing the option set is legitimate.** `opening_set` (`engine/season/decision/options.py:35-104`)
   offering fewer candidates because the person lacks a form, an operand or a hold **is not corruption of
   intent — there was no intent yet.** Clause 5 of its own set comprehension (`:50`) —
   *"every operand `requires(verb)` names is DERIVABLE"* — removes candidates by the dozen and violates
   nothing.
2. **Failure is not corruption.** A refused or `Marginal` `transfer` moved nothing, **and the act as
   declared is still in the act store with its operands intact.** `_derive_operand`'s own measurement
   (`options.py:293-295`): *"21 of 723 transfers refused, 73 of 723 moves blocked"* — 94 acts that
   happened exactly as meant and achieved nothing.
3. **The forbidden shape is INTENT REASSIGNMENT:** any mechanism that rewrites the **operands**, the
   **verb** or the **referent** of an `Act` after `choose` returned it, or that lets a **witness's claim**
   stand in for the actor's declared content at RESOLVE.

### §A.1.3 · Where it already lives — the `Act`/`Claim` split, both opened

**`Act`** (`engine/season/state/carriers.py:332-365`) is **the actor's content**. Its `payload` is at
`:339`, and **nothing after DELIBERATE writes it**: `write_matrix.yaml:72-78` carries one `Act[]` row,
field `returned`, `steps: [DEL]`, `class: "ACTS"`, `by: "DELIBERATE writes nothing else"`, `emits: "—"`.
**One row, one step, and the `by:` cell is the prohibition already stated as data.**

**`Claim`** (`carriers.py:129-156`) is **a witness's reception**, and every field on it is reception-side:
`holder` (whose ledger), `source` (`firsthand | told_by | inferred | firsthand_via_knot`), `confidence`
(how much they credit it), `visibility`, `when`, `round`. Its docstring's first line: *"S20. Lives in the
HOLDER'S OWN ledger."*

> ### **RULED: the split is already built and the principle NAMES it. What `RR-P` adds is the
> PROHIBITION ON A BRIDGE — no mechanism may read a `Claim` and write an `Act`'s content.**
> The two carriers are 200 lines apart in one file; one is written at one step by one writer; the other
> is written at WITNESS by the fan; and **today no code path joins them in that direction.** The axiom
> would make that a property of the design rather than a fact about the current commit.
> ⚠ **And the asymmetry is not symmetric and must not be read as such:** an `Act` freely reads claims —
> clause 4 of `opening_set`, *"`requires(verb)` not KNOWN-FALSE from p's OWN claims"*, is exactly that,
> and `AX-2` requires it. **Claims into the decision: mandatory. Claims into the declared content:
> forbidden.**

### §A.1.4 · Where this design already honours it, three places

| the mechanism | the reception churns | the act does not |
|---|---|---|
| the lossy `tell` (§A.10) | the **hearer's** copy loses an addressee or a number | the **teller's** ledger is untouched; the **Record** is untouched; the teller's `tell` act sits in the store as declared |
| the `content:` claim's operands (§A.13) | the executor may act on drifted numbers | **his** act then carries **his** operands, exactly as he meant them, and the Duke's writ is unchanged |
| `agreement` (`options.py:412`) | two claims on one cell disagree | neither act is rewritten — **the disagreement is scored, not resolved** |

### §A.1.5 · The test run back over round one — two hits, pointing opposite ways

**Hit 1 — `in_force(w, rung, clause)` read at MATTER violated it in the OPPOSITE direction: ZERO
reception churn.** A clause the Duke wrote became a condition the province satisfied **with no person in
between**. `AUDIT_VERDICT` already made this a limit on `holonic §37.3` grounds; **`RR-P` says why it was
wrong in principle**, and the diagnosis is the more useful one: the defect was not that the cascade was
noisy in the wrong place — **there was no reception at all**, so the act's content *became* the world's
state without passing through anybody's belief. **An act whose content is applied directly is not an
inviolate act; it is a fiat** — which is `ED-IN-0210` ruling 1 arriving from the other side:
*"verbs invoke mechanisms or interactions between a character and another entity/character. **they are
not fiats.**"*

**Hit 2 — the analyse-stage sketch of an EMITTER-SIDE `refract`** — *the issuer's terms bent by the rung
they pass through* — **would have been intent reassignment**: the Duke's operands rewritten en route.
**Dropped.** The lossy copy in this design sits on the receiver's `Claim` and never on the `Record`.

> ⚠ **AND HIT 2 IS ANSWERED BY LAYER 1 BEFORE `RR-P` REACHES IT, WHICH LOWERS RR-P's PRICE AND I SAY SO
> RATHER THAN CLAIMING THE AXIOM CARRIES THIS FILE.** `ARCH F.10` — *"refraction's side | **receiver-side**,
> per the chain's held-back closure | `terms.distorted` needs a mutable emitter-side object, which §37.1
> forbids"*. So the emitter-side sketch fails at `CLAUDE.md` §0 **gate 3** (a design document decided it)
> and needs no axiom. **`RR-P` is not load-bearing for this file's `tell` branch — `ARCH F.10` is.**
> RR-P is load-bearing for the *general* claim, across the subsystems `F.10` does not reach.

**No third hit.** Round one's seat model, surface law, cell law and causation worksheet decide **what is
SHOWN**, never **what was MEANT**.

### §A.1.6 · The cost, stated honestly

| what must be checked once RR-P is ruled | my reading, and it is a reading |
|---|---|
| contest resolution (`loop/resolve.py:355-555`) | **fine.** The sum-then-clamp at `:538-553` decides the **outcome band** and a write's magnitude; it never touches an operand. *"SUM ALL DELTAS, CLAMP ONCE. Clamping may not depend on arrival order"* |
| WITNESS (`loop/witness.py`) | **fine by signature.** It writes `Claim`s and appends to ledgers; it holds no `Act` to write |
| the degree-keyed write/emit columns (`ARCH §C.4`) | **fine.** A degree selects *which* of the row's declared writes happen. It does not edit the act |
| `_derive_operand` (`options.py:259-323`) | **fine, and it is the boundary.** It runs **before** `choose` returns, person-side. An operand derived at option-build time is the person's own; an operand rewritten after would be the violation |
| the **Godot port** | ⚠ **UNCHECKED.** Nothing in `godot/` was read against this, and `CLAUDE.md` §6 says a port never corrects its oracle in place. **Named as unchecked rather than assumed clean** |
| **combat, social contest, mass battle** | ⚠ **UNCHECKED, all three.** RR-P would bind them, and that is the whole reason it is an axiom request and not a note |
| `AX:66` — *"**There are SIX.**"* | **must be amended in the same edit.** A seventh axiom makes that sentence false |

**Filed as RR-P in §C.6**, with all five gates walked. **Nothing in this file is blocked on it**, and
every claim that leans on it says *under RR-P*.

## §A.2 · `holonic §37.1` ALREADY SPECIFIES THE MECHANISM — quoted whole

Opened at `architecture/holonic_ARCHITECTURE.md:1280-1299`, 2026-09-17, reproduced without elision:

```
### §37.1 The head's mechanism, and it is not a tree walk

Dispensation := (id, issuer, proposition, scope, terms[])   -- NINE typed terms, no bare effect field

> "It travels by being noticed, NOT DOWN A CHAIN OF POSTS. Publishing is a `tell`, so it distorts in
> transit, and what reaches the hamlet is often not what the Duke signed."
>
> "A published dispensation does not apply — it lands as a compliance contest, per relevant Rung,
> through `contest`, and SCOPE ENUMERATES EXECUTORS, NOT PLACES."
>
> "Delivery is not assumed, and an executor who never received it is DISTINCT from one who received
> it and refused."

### §37.2 Then nothing further is needed

The person's own need, plus capability, plus this new **claim**, yields an opening through the same
`opening_set(person, view)` any act comes through — **now evaluated over changed CLAIMED terms.**
**No one authored an opportunity for anybody.**
```

**Five commitments sit in those fourteen lines, and four of them are already code.**

| the commitment | its state in the tree |
|---|---|
| the dispensation is a **typed tuple**, not an effect | `Record` exists (`carriers.py:422-445`); the type is there and the **typing** is not |
| it **travels by being noticed** | `observers_for` (`epistemic.py:405`) and the five channels **are** the whole of "noticing", and they run: **2,175 `claim.deposited`** in one season |
| it **does not apply** — the answer is an act | `opening_set` (`options.py:35-104`) is the only route from a claim to an act, and it runs |
| **delivery is not assumed** | nothing today delivers anything, so the distinction is trivially preserved and trivially empty |
| **scope enumerates executors** | asserted by a shipped probe (`probes.py:1148-1160`) against `w.dispensations`, **which nothing else reads** |

> ### **RULED: the mechanism is specified; the gap is content, custody and a claim.** `ARCH F.15`
> classifies it correctly and I take the classification verbatim — *"not an assumption so much as an
> absence: the entire downward mechanism has no executable content, and `issue` produces a document
> nobody can comply with."* **An absence of content is filled by supplying content.** This file adds
> **one verb and one roster**; everything else is a payload for a body that already runs.

⚠ **One sentence of §37.1 is in apparent tension with Jordan's second ruling and must be handled, not
glossed.** §37.1 says *"Publishing is a `tell`, so it distorts in transit, and what reaches the hamlet is
often not what the Duke signed."* Jordan says *"A document from the Duke isn't like a game of telephone —
the written letter in some form with fidelity would end up being directly given to the settlement
leader."* **These are not in conflict, and the resolution is the whole design:** §37.1 describes
**publishing**, which is one channel, and never claims it is the only one. The line directly above it
puts the terms in **a typed object with an id** — and a typed object with an id is exactly a thing that
can be handed over intact. **So §37.1 describes THE WORD and specifies THE WRIT in the same breath, and
round one built neither.** Jordan's ruling adds no channel the architecture lacks; **it tells you which
of the two the *document* is.**

## §A.3 · THE NINE TYPED TERMS, SUPPLIED — and `ARCH F.15` closes

`ARCH §B.5`'s cost line is the open half: *"the nine typed dispensation terms become a schema for one
Record kind and remain unspecified."* `ARCH F.15` grades that absence and says what it blocks.

**The nine are not nine new fields.** `holonic §37.1`'s tuple has five slots and its comment says
**nine typed terms, no bare effect field**. The load-bearing half of that comment is the second clause:
whatever the terms are, they may not be *"a bare effect field"* — **the document may not carry a function
the engine applies.** The count is the chain's, and nothing in the chain lists them. So the schema is
derived from **what the five slots need in order to be answerable by an act**, and it lands at **three
authored keys plus five fields the carrier already has**:

| `holonic §37.1` slot | where it lives on a `Record` | why |
|---|---|---|
| `id` | **`Record.id`** (`carriers.py:425`) | already minted, already the hold's object, already the claim's subject |
| `issuer` | **the live `hold` at mint time**, and nothing else | `holonic §15` makes possession a Tenure, *"never a field on the Record"* (`effects.py:286-287`). The issuer is *whoever held it first*, which the act store and the `record.created` Event both name. **A stored `issuer` field would be a second home for a fact the Tenure already owns** — `AX-4` |
| `proposition` | **`subject_matter["terms"]`**, a `PropositionId` | `Proposition` (`carriers.py:467-477`) is `frozen=True`, mood-bearing and **immutable**. An `OUGHT` Proposition is exactly *what is owed*, per `AX §E.1.7`: *"**AN OATH IS AN UTTERANCE. WHAT IS OWED IS THE `OUGHT` PROPOSITION IT UTTERS.**"* |
| `scope` | **`subject_matter["to"]`**, a list of `PersonId \| OfficeId` | `holonic §37.3` row 3: **executors, never places** |
| `terms[]` | **`subject_matter["at"]`** plus the Proposition's own `subject`/`predicate`/`value`/`scope` | the Proposition carries the *what*; `at` carries the *where it is discharged* |
| — | `Record.forgery_quality` | genuine or not — §A.15 |
| — | `Record.stages` | the writ's own deadlines, act-declared (#353 §13.1), matured by MATTER **only while a living person holds it** (`matter.py:73-78`) |
| — | `Record.matured` | whole-record, **not per-stage** — the `AUDIT_VERDICT` limit, honoured |
| — | `Record.ttl` | declared, MAT-stepped, **no writer**, and §A.16 argues it must stay that way |

> ### **RULED: `Dispensation := (id, issuer, proposition, scope, terms[])` becomes**
> ### **`Record(kind="dispensation", subject_matter={terms: PropositionId, to: [PersonId|OfficeId], at: RungId})`,**
> ### **with the issuer carried by the `hold` and the identity by `Record.id`.**
> **Three authored keys — and the ban on a bare effect field is structural rather than promised:** a
> `Proposition` is `frozen=True`, so the OUGHT cannot be mutated into a function, and nothing in the
> engine can call it. **`ARCH F.15` closes on this schema.** ⚠ It closes **as a specification**, not as
> a build: the grade stays `paper` until `issue` mints one and a loader refuses a wrong key (§C.5 item 2).

⚠ **`ARCH §B.5`'s cost sentence becomes false when this lands, and I do not edit it.** It is RATIFIED
(ED-IN-0204). The replacement — *"the nine typed dispensation terms become **a Proposition and an
address**"* — is **RR-B**, owned by `05`, quoted at its `§` and left alone.

## §A.4 · EVERY FIELD OF THE `dispensation` RECORD, ONE AT A TIME

`Record` has **eight** fields (`carriers.py:422-445`). A writ uses all eight, and the reason each is right
is not the same reason twice.

### `id: str` (`:425`)
Minted as `d.get("record") or f"rec:{a.id}"` (`effects.py:273`), so a computed act gets an id derived from
the act's own id and a declared act may name one. **This is what every other mechanism names the writ
by:** the `hold` Tenure's `object`, the `content:` claim's `subject`, `destroy_record`'s payload,
`document_key`'s `changes[]` match. Immutable by absence of a writer — no matrix row names it after
`(Record, exists)`.

### `rung: str` (`:426`)
**The place the document was drawn up.** `_eff_create_record` writes `d.get("rung") or a.actor`
(`effects.py:284`) — and **measured, 69 of 69 Records carry a PERSON id in this field.** That is a real
defect, invisible in this world because `build_realm` gives every person a same-id `person`-kind Rung, so
the person id *is* also a rung id and every reader answers plausibly. **I state it and do not fix it
here**, for one reason: `place_of` (`01`'s Query) prefers **the containing rung of the Record's live
holder** and falls back to `Record.rung` only for an **unheld** Record — so for a writ in somebody's hand
this field decides nothing. **The fix belongs with `place_of`, in `01`, and this file leaves it a number
to move.**

### `kind: str` (`:427`)
`"dispensation"`. Today a **free string** defaulting to `"text"` (`effects.py:284`) — measured `text`
69 of 69 — which round one correctly named an `ID-4` hazard. §A.5 closes it.

### `forgery_quality: int = 0` (`:428`)
0 for a genuine writ. §A.15 walks the forgery path, including the honest correction that this field has
**neither a reader nor a writer in execution**.

### `subject_matter: Any = None` (`:429`)
**The writ's content**, and the field the whole design turns on. Two properties, both already true and
both load-bearing:

- **It has NO matrix row.** The five `Record` rows are `exists`, `forgery_quality`, `matured`, `stages`,
  `ttl` (`write_matrix.yaml:245-277`; `hole_register.yaml:228` lists the same five as `H-22`'s
  `SCHEMA_ROW ×5`). `Record`'s own docstring says why: *"S30.1: it has NO Partition row, so every Record
  write is an unmarked cell — which this instrument reports rather than papering over."*
- **It is therefore written exactly once, inside `(Record, exists)`'s gate** (`effects.py:284-285`), and
  **never again by anything.**

> ### **RULED: "verbatim or not at all" is not a rule this design adds — it is a property
> `subject_matter` already has, because there is no row that would let anything write it twice.**
> A writ's content is set at creation and is immutable by **absence of a producer**. A later session that
> wants to amend a writ **must add a matrix row to do it**, and that addition is exactly where the
> question *"may a Duke edit a letter already in a reeve's hand?"* becomes visible. **The design's answer
> is no: you do not amend a writ, you issue another** — and the executor then holds two claims, which
> `agreement` (`options.py:412`) already pairs. ⚠ **This closes round one's unwritten
> same-`(rung, clause)` collision branch (`AUDIT_VERDICT` limit 9) BY CONSTRUCTION**, and §C.6 records
> RR-1 as closed at gate 2 for that reason.

### `ttl: Optional[int] = None` (`:430`)
Declared, `[MAT]`-stepped, on the `conditional_emission_rows` exemption (`matter.py:141`;
`state/world.py:385-387`), and **nothing decrements it.** §A.16 argues it must stay unwired, because a
document expiring on a clock nobody wound is a **fourth** world-motion and `AX-5` says three.

### `stages: list[tuple]` (`:431`)
`(due_tick, label, the act that wound the clock)`. **Act-declared** (#353 §13.1), defaulted from
`fixtures.record_stages_default = 3` / `record_stage_term = 1` (`data/fixtures.py:428-429`) when the act
declares none — which is `H-80`, declared and swept. For a writ these are **the deadlines the writ itself
sets**: *report by season 3*, *the levy standing three seasons*. MATTER matures them (`matter.py:65-109`)
and **refuses to mature a stage whose holder is gone or is not a person** (`:73-78`).

> ### **RULED: a writ that changes hands changes who must answer for its deadlines — and this is
> already shipped, in a line written for a different purpose.** `matter.py:73-78` reads the live `hold`
> and stops the clock when the holder is gone, with the reason at `:61-64`: *"a half-made copy now
> correctly STOPS if the copyist is jailed, which the MATTER-driven version gets wrong: A COPY THAT
> FINISHES ITSELF."* Compose `give` on it (§A.7) and you get, free: **the reeve who accepts the writ
> accepts its clock, and a writ nobody will take does not tick.**

### `matured: bool = False` (`:445`)
RULED by Jordan 2026-09-10, and **whole-record, not per-stage** — the carrier's own comment records the
ruling, and `AUDIT_VERDICT` limit 7 records that round one's `ceiling = matured/declared` read a per-stage
maturation this field cannot carry. **I make no per-stage claim.** A writ's `matured` means its **last**
stage matured; partial progress is readable only by walking `stages` against `w.tick`, which is a read,
not a field.

## §A.5 · `record_kinds` — the schema roster, and where the refusal lives

**The E-attack to answer first: `subject_matter: Any` is a schema hole**, and a design that puts the
writ's whole content in an untyped field has moved the problem rather than solved it. **Conceded**, and
answered by one roster and one constructor check.

```yaml
# engine/season/rosters.yaml — a TABLE, in the TABLES block (header :800-803) beside `site_kinds` (:805),
# because it is a MAPPING: `table()` reads these and `roster()` RAISES on them, so the two shapes
# cannot be confused at a call site.
  record_kinds:
    source: "`ARCH §B.5` — *Petition and Dispensation become Record kinds*. The keys are this
             proposal's (ED-IN-0234); the FOLD is ratified."
    row: H-22
    note: >-
      ⚠ THE KEYS ARE EXACT, NOT A MINIMUM. `Record.__post_init__` refuses a `subject_matter` whose
      key set is not its kind's, IN EITHER DIRECTION — a missing key and an extra key are the same
      defect, because an extra key is a second vocabulary and a missing one is an operand no reader
      can bind. Same polarity `eligibility_kinds` already carries against a fifth kind.
    values:
      dispensation: [terms, to, at]
      commission:   [seat, to]
      petition:     [terms, to, from]
      works:        [plan, at, stage]
      text:         []
```

**Where the refusal lives, decided at `CLAUDE.md` §0 gate 4 (precedent), not invented.**
`state/world.py:240-241` names the precedent in terms while justifying `add_tenure`'s own kind check:
*"That is the same failure shape `Office.__post_init__` already refuses for remit acts (§8: one rule,
applied at every constructor rather than at one)."* So:

```python
# engine/season/state/carriers.py, on Record
def __post_init__(self) -> None:
    require_member(self.kind, RECORD_KINDS, ...)          # `kind` stops being a free string
    keys, want = set(self.subject_matter or ()), set(RECORD_KINDS[self.kind])
    if keys != want:                                     # BOTH directions
        raise Forbidden(..., needs=f"exactly {sorted(want)}", law="ARCH §B.5 / ED-IN-0234")
```

⚠ **Three consequences, stated rather than left to be discovered.**

1. **`text: []` means every one of today's 69 Records stays lawful**, because `subject_matter` is `None`
   for all 69 and `set(None or ()) == set()`. **The migration is a no-op on the running world** — which
   is why this is an addition and not a schema break. *Falsifier:* `WW-2`.
2. **`_eff_create_record`'s `d.get("kind") or "text"` default survives untouched** (`effects.py:284`). A
   computed `create_record` keeps making `text` Records; only an act that *names* a kind reaches the new
   shapes. **No computed act is silently promoted into a writ.**
3. **This is +1 roster and I concede it as overhead** in §B.5's E ratio. The alternative — a
   `Dispensation` dataclass — is the thing `ARCH §B.5` **rejected**, with its reason: *"the chain's two
   separate non-carriers, each then needing its own existence row and custody semantics while being
   unreachable by the verbs the design already has for documents."*

## §A.6 · `issue` IS `create_record` WITH A KIND AND AN ADDRESS

**What exists.** `issue` (`verb_table.yaml:256-267`): `scale: province`, `stratum: binding_decision`,
`eligibility: [remit:issue]`, `requires: "scope enumerates executors, not places (§37.1)"`,
`writes: [Dispensation.exists]`, `emits: [dispensation.issued]`, `grade: ruled`. Its `writes_note` already
flags the defect: *"— (a Dispensation is not a state write — §37.3) || ⚠ W3, ON THE W2 AUDIT: as
`petition`. Part E's '(a Dispensation is not a state write)' is the bypass §1.4 hole 4 names, not a
licence for one."* **Measured: `issue` is not resolvable** — no effect body — and `dispensation.issued`
fires **0** times.

| cell | today | becomes | why |
|---|---|---|---|
| `writes:` | `["Dispensation.exists"]` | `["Record.exists"]` | position 15's own instruction (`_part2.md:440-441`); retires matrix row `(Dispensation, exists)` (`write_matrix.yaml:112-118`) |
| `emits:` | `["dispensation.issued"]` | **unchanged** | the kind names the *act*, not the carrier. `_ch_post_remit` and `_ch_chronicle` dispatch on `e.kind` against the verb table (`epistemic.py:353-354`, `:381-382`), so renaming it would change who witnesses |
| `requires:` | prose, no predicate → **not resolvable** | `requires_typed: {form: existence, of: subject, kind: Proposition}` | **the cell `commit` already carries** (`verb_table.yaml:119-122`). A writ requires its OUGHT to exist, and `utter` is the only maker of one (`:746-753`) — which is why the season can start: **54 Propositions at build**, measured |
| effect | none | `@effect_for("issue")` on the shared document body | one function, three registrations — §B.5 attack 4 |
| `eligibility:` | `["remit:issue"]` | **unchanged** | `03` closes its person side through the commission claim (`H-71`); I do not touch it |

```python
def _eff_document(kind):
    """ONE body, registered for `create_record`, `issue` and `petition`. `_eff_create_record`'s mint,
    hold and stage-default are unchanged; this supplies the kind and the validated subject_matter."""
    @effect_for(kind if kind != "text" else "create_record")
    def _body(w, a, res=None):
        d = a.payload if isinstance(a.payload, dict) else {}
        sm = _subject_matter_for(kind, a, d)     # refused by Record.__post_init__ if the keys are wrong
        return _eff_create_record(w, _with(a, {**d, "kind": kind, "subject_matter": sm}), res)
    return _body
```
For `dispensation`: `{"terms": _operand(a, "subject"), "to": list(d.get("to") or ()), "at": d.get("at")}`.

> ### **RULED: `issue` gains no mechanism of its own. It is `create_record` plus a kind, an address and
> a Proposition — and the Proposition is the act's own `subject`, which is the one operand a computed act
> already carries.** `_derive_operand` binds `subject` from the question's referent (`options.py:307-308`),
> so **an NPC holding a `content:` claim or a `need` about a Proposition can form a writ with no new
> operand channel.** That is `H-94`'s famine going **unfed** rather than fed.

⚠ **`to` is in the closed operand roster and `at` is NOT** (`rosters.yaml:1084` —
`[actor, subject, from, to, site, kind, amount, floor]`). So a **computed** `issue` binds `subject` and
`to` and **cannot bind `at`**. The consequence, unsoftened: **a computed writ addresses executors and
names no place of discharge** — `at: None` — and the executor's own `from` then binds
`containing_rung_of(p)` (`options.py:316-317`): *discharge it where you stand.* A **player** naming `at`
declares it and carries it. **I do not coin a ninth operand**, which `rosters.yaml:1078-1079` calls
*"filling `H-94` by keyword argument, which is the ruling `H-94` is waiting for and not a table edit."*

### §A.6.1 · `petition` is the same fold upward; `dispatch` is the same fold sideways

**`petition`** (`verb_table.yaml:395-405`) writes `Petition.exists`, and its `writes_note` carries the W3
finding that `writes: []` made the creation row *"INERT and creation still bypassed the gate."* It becomes
the shared body with `kind: "petition"` and `subject_matter = {terms, to, from}` — the grievance, whom it
is addressed to, who raises it — and it reaches a venue by **`give` up the ladder**, not by
`w.petitions`. **`carry`** (`:101-114`) keeps writing `(DocketItem, matter)` and is **not** the mover: it
puts a petition on a **docket**; `give` puts it in a **hand**. Two different acts, and the tree already
spells them apart.

**`dispatch`** — and here I correct my own specification. The plan I write from says *"`dispatch` is
`give` of a writ naming the dispatched."* ~~That conflates minting with handing.~~ **`ED-IN-0210` as
RULED by Jordan 2026-09-15 (`registers/editorial_ledger_in.jsonl:104`) says it exactly, and I take the
ruling's own words:** *"`dispatch` at person scale is `issue` with a person-scale referent, and the nine
dispensation terms Layer 1 records as an absence (04:1077) become the shared shape."*

> ### **RULED: `dispatch` folds into `issue` with `to: [<person_id>]`. The delivery is `give`, which is
> a different act and is not `dispatch`.** An order and a writ differ in **whom you name**, not in
> **what you do** — which is the ruling, reached from the ruling's own sentence rather than from the
> plan's paraphrase. §C.6's **RR-A** asks to delete the row on that ground.

## §A.7 · `give` — the H-84 verb, named

**H-84** (`engine/season/hole_register.yaml:1000-1011`), tier 0, kind `PRODUCER`, grade `absent`, owner
*"Part E — the verb that would do it"*:

> *"no verb in the resolvable vocabulary moves a Record to another person, so no second person ever holds
> one … What a Record still buys and a claim does not is PERSISTENCE IN SOMEONE ELSE'S HANDS."*

And `epistemic.py:311-317`, the `document_key` docstring, states the same thing and forbids the shortcut:

> *"⚠ WHAT THIS DOES **NOT** FIX, STATED HERE SO IT IS NOT READ AS FIXED: `H-84` … the STORE route above
> is open; the RECORD route is not … `H-84` forbids in terms inventing a `give_record` here to make a
> case pass. Nothing was invented."*

**The verb is ratified program position 16**, whose first clause is *"name it against `VOCABULARY.md`
before adding the row."* **Discharged:** `architecture/VOCABULARY.md` carries **no row** for *give*,
*grant*, *hand*, *convey* or *deliver* — measured
(`grep -n -i '\bgive\b\|\bgrant\b\|\bhand\b\|convey\|deliver' architecture/VOCABULARY.md` → no match),
so there is no collision to resolve. `CLAUDE.md` §4's **idiomatic in choosing** then decides it: *give* is
the word ordinary usage supplies for handing a thing to somebody, it is used that way outside this
repository, and a reader with no memory of the tree lands on its meaning. **`grant` is rejected** — it
reads as conferral and `confer` owns that. **`carry` is TAKEN** (`verb_table.yaml:101`) and means something
else. **`deliver` is rejected** as the noun-heavy coinage `CLAUDE.md` §4's `evacuate` case warns against.

```yaml
  - verb:        "give"
    stratum:     "social"
    eligibility: ["own", "hold:<record>"]
    requires:    "the actor holds the subject, and the receiver is present where the actor is"
    writes:      ["Tenure.until", "Tenure.since"]
    emits:       ["record.given"]
    emits_on_refusal: ["give.refused"]
    grade:       "ruled"
    source:      "ratified program position 16 (`_part2.md:452-455`); H-84; ED-IN-0234"
```

**Four cells need an argument, and one of them is an honest limit.**

1. **`eligibility: ["own", "hold:<record>"]` — position 16's own pair, kept verbatim.** Person-side,
   `hold:<record>` is a **placeholder** and therefore **declines** (`options.py:145-160`, `H-75`), and
   `own` admits at `:143-144`. Eligibility is a **disjunction**, so **`own` carries the verb person-side**
   and the `hold:` alternative is the resolver's tighter reading. This is exactly the structure `transfer`
   ships with (`own | hold:<store>`), which is measured resolvable and executes.
2. **`writes: ["Tenure.until", "Tenure.since"]` — two, one per side, exactly `confer`'s pair**
   (`verb_table.yaml:149`). `holonic §15`'s hold cardinality is **1 per object**, so the giver's hold
   *must* close; the design offers no joint custody. **Answering the plan's open question explicitly: yes,
   `give` requires release — and it is not a separate act, it is the same write pair.**
3. **`emits: ["record.given"]` — a new Event kind, and I name the cost.** `ARCH F.20b` records that the
   derived Event-kind roster is *specified and unbuilt*, so nothing admits a new kind and nothing has to;
   the honest statement is that this kind is admitted by the same non-mechanism that admits `news.told`.
   ⚠ **It must NOT reuse `record.created`**: `_ch_post_remit` and `_ch_chronicle` dispatch on `e.kind`
   against the verb table (`epistemic.py:353-354`, `:381-382`), so collapsing *giving* into *creating*
   would make **every seat with `remit:issue` witness every handover in the realm** — the place-blind
   broadcast this file and `01` both delete.
4. **`requires:` is PROSE with a registered predicate, and this is a LIMIT, decided at gate 4.** The first
   conjunct types cleanly — `{form: relation, of: subject, relation: held_by}`, which is `succeed`'s live
   cell (`verb_table.yaml:496-500`) and reads *"the actor holds the subject"* (`world_q.py:738-740`).
   **The second cannot be typed.** `Relation.check` pairs the `of:` operand with **the actor**
   (`data/requires.py:300-305`), and `present_at` asks *"is the ACTOR present at this site or rung"*
   (`world_q.py:741-744`) — **there is no stem for "are these two persons in the same place"**, and
   `REQUIRES_STEMS` (`data/requires.py:488-491`) is eight members:
   `exists, stores, condition, floor, contain.path, held_by, present_at, claim.held`.

> ### **RULED: `give` takes `release`'s and `revoke`'s route — prose `requires:` plus a registered
> predicate — and that is gate 4 (precedent), not a shortcut.** `release`'s own `requires_note`
> (`verb_table.yaml:431`) sets it and gives the reason: *"PROSE + A REGISTERED PREDICATE, LIKE `revoke`,
> AND NOT `requires_typed` — deliberately … adding an `any` combinator is a GRAMMAR CHANGE
> (`REQUIRES_STEMS` is closed and refuses an unknown stem at load)."* `_req_give` becomes the **sixth**
> member of `REQUIRES_PREDICATES` (measured today: five — `confer, convene, dispatch, release, revoke`).
> ⚠ **And it is the FIRST CELL TO TYPE if a person↔person co-location stem is ever ruled** — named here
> so a later session need not rediscover which cell was waiting. A stem's addition is checked **both
> ways** by `engine/season/tests/test_season_shape.py:507-528`: every declared stem is in the roster, and
> every rostered stem is one a reader dispatches on.

```python
@requires_predicate("give")
def _req_give(w: "World", a: "Act") -> bool:
    """The actor holds the subject, and the receiver is present where the actor is.
    Conjunct 1 is `succeed`'s `held_by`; conjunct 2 has no stem — see the row's `requires_note`."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    rid, to = d.get("subject"), _operand(a, "to")
    if rid not in w.records or to not in w.persons:
        return False
    if not any(t.kind == "hold" and t.subject == a.actor and t.object == rid and t.live
               for t in w.tenures):
        return False
    here = containing_rung_of(w.persons[a.actor])
    return here is not None and to in world_q.presence(w, here)


@effect_for("give")
def _eff_give(w, a, res=None):
    """`_eff_confer`'s shape (effects.py:118-126) over a Record instead of an Office: close every live
    hold on the object, open the receiver's. `holonic §15`: hold is 1 PER OBJECT."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    rid, to = d.get("subject"), _operand(a, "to")
    if rid not in w.records or not to:
        return {}
    closed = []
    for t in w.tenures:
        if t.kind == "hold" and t.object == rid and t.live:
            t.until = w.tick; closed.append(t.id)
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{rid}"), to, rid, "hold", w.tick)
    w.add_tenure(nt)
    return {"tenure.opened": [nt.id], "tenure.closed": closed}
```

⚠ **`_eff_confer`'s three hard-won lessons apply verbatim and I do not re-learn them.**
(a) An effect **mutates and returns the ids it touched; it does not call `w.write`** — *"a nested `w.write`
is a write inside a write, and returning `None` tells the fold nothing was touched, which makes it emit
the REFUSAL"* (`effects.py:96-100`). (b) The return is **per-kind**, because *"returning a flat list made
the fold publish `tenure.closed` anyway — a state change that did not happen"* (`:123-126`). (c) There is
**no `or a.actor` default** on `to`: *"A conferral onto nobody is a malformed act, not a self-conferral"*
(`:103-105`), and a *give* to nobody is the same defect.

## §A.8 · CARRIAGE IS A PERSON'S OWN JOURNEY — no co-movement write

**A writ travels because the person holding it walks.** `move` (`verb_table.yaml:361-374`) is measured
resolvable and executes — its own `requires_typed_note` records *"`move` EXECUTES 650 times and is blocked
73"* over the 89 corpus worlds, and the populated season measures **3 moves and 23 blocks**. **Nothing is
added to make a Record travel with its holder**, and that is the point:

- `place_of(record)` = the containing rung of its live holder, else `Record.rung` — `01`'s Query, promoted
  from `epistemic._event_place` (`:215-241`). **The document's place is a derived read of the custody edge,
  never a stored field.** `AX-4`: one owner.
- **No `Record.rung` update while held.** A writ carried from the chancery to a hamlet changes **no cell on
  the Record**. The only thing that moved is the holder's `contain` Tenure, which `move` already writes.
- **A blocked `move` leaves the writ where it was**, with the holder, and emits `travel.blocked` — **23 of
  26 movement attempts**, measured. **Delivery genuinely is not assumed** (`holonic §37.3` row 4), and the
  reason is not a delivery model: **it is that walking is hard.**

> ### **RULED: carriage costs a person and a season and adds no mechanism.** The writ's journey *is* the
> carrier's journey, and the only new write in the whole chain is the one `give` makes at the end of it.
> **This is `holonic §37.1`'s *"NOT DOWN A CHAIN OF POSTS"* satisfied structurally**: there is no chain, no
> relay, no queue, and **no object that represents a message in flight.** There is a man with a letter.

## §A.9 · THE ONE DEPOSIT RULE, AND ITS FOUR CONSUMERS

**A held document is a held belief.** At WITNESS, a person who comes to hold a Record deposits:

```python
Claim(id=H(w.world_seed, w.tick, pid, f"content:{rid}"),
      holder=pid, subject=rid, predicate=f"content:{rec.kind}",
      value=copy.deepcopy(rec.subject_matter), when=w.tick,
      source="firsthand", confidence=<the observation deposit's>, visibility="own", round=self.round)
```

**The trigger is a `hold`-on-Record appearing in the Event's `changes[]`** — the operand
`_ch_document_key` already reads (`epistemic.py:331-333`), so the deposit rule and the channel read **the
same primitive** and `CLAUDE.md` §8 is satisfied with no second owner. The branch sits where the
observation deposit runs (`loop/witness.py:270-279`).

**Why `firsthand`:** `ARCH §C.6`'s mint table gives `document_key` *"the change claims only. No
attribution"*, and this deposit carries **no attribution** — it says *this document says X*, never *the
Duke wrote X*. Who wrote it is a **separate** claim, minted `firsthand` by `co_located` if you watched him
seal it and `told_by` if somebody said so. **That separation is what makes a forgery playable** (§A.15).

⚠ **`ARCH §C.6`'s table has no row for a content mint, and I do not edit it.** RR-B, owned by `05`. The
honest statement of what this is: **a new deposit branch keyed on a hold, not a new channel mint** — a
channel decides *who* witnesses; this decides *what a witness who now holds the thing learns*. The two are
different axes, and `epistemic.py:319-329` already records that their interaction is unsettled.

### §A.9.1 · Q2 fires with no extension for the holder, and needs one clause for the hearer

`questions_for`'s Q2 (`queries/world_q.py:491-494`) tests `c.subject == p.id or c.subject in mine`, where
`mine = {t.object for t in p.tenures if t.live}` (`:471`) — **every object of every live tenure, which
includes every Record the person holds.**

| the person | does Q2 fire today? | why |
|---|---|---|
| the **issuer**, at the moment he issues | **yes, with no change at all** | he holds it; `c.subject` = the Record id ∈ `mine` |
| the **executor handed the writ** | **yes, with no change at all** | the same, one `give` later |
| the **executor who only HEARD of it** | **no** | his `told_by` claim's subject is a Record he does not hold and is not |

**So exactly one clause is added**, and `01` owns the Query it is added to. Q2's test becomes
`c.subject in R or place_of(w, c.subject) in R or any(x in R for x in named(c))`.

> ### **RULED: `named(c)` is read from `record_kinds`, not from the value's strings.** For a claim whose
> `predicate` starts `content:`, `named(c)` is the id set under the **addressee key its kind declares** —
> `to` for `dispensation`, `commission` and `petition`; **nothing** for `works` and `text`. A generic
> *"every id anywhere in the value"* would make a `works` plan's site ids into addressees and a petition's
> `from` into a summons. **The roster that types the schema is the roster that says which key addresses
> somebody**, which is one owner for both facts.

### §A.9.2 · Four consumers, and it is one rule

| the document | its `subject_matter` | what the claim makes believable |
|---|---|---|
| **`dispensation`** | `{terms, to, at}` | *I am named in a writ that says X* → the executor is asked (Q2), and `_derive_operand` reads his operands off it (§A.13) |
| **`commission`** | `{seat, to}` | *I hold a seat whose remit includes `issue`* → `person_side_eligible`'s `remit:` decline (`options.py:163-165`) is answered **from the holder's own ledger**. **`H-71` closes person-side** — `03` owns it |
| **`petition`** | `{terms, to, from}` | *somebody is aggrieved about X* → the receiver is asked, and the grievance is a thing he can act on or **visibly ignore** |
| **`works`** | `{plan, at, stage}` | *I know what I am building* — `04` owns it |
| **`text`** | `{}` | *I hold a document that says nothing* — the honest reading of today's 69, and the **control** in `WW-7` |

> ### **RULED: one branch, five kinds, and it REPLACES a rule rather than adding one.** Round one proposed
> a **new** conferral-claim deposit keyed on `e.kind` — `AUDIT_VERDICT` limit 8: *"the conferral claim's
> deposit is a NEW deposit rule, not a ride on the existing channel."* This is the same want, satisfied by
> the channel that was **already half-written for it**, and the commission is one of its consumers rather
> than its own mechanism.

## §A.10 · THE WORD — `tell`, and the loss function specified exactly

**What exists, measured.** `tell` (`verb_table.yaml:507-560`) is resolvable, `own`-eligible,
`contests: "a standing"`, `writes: []` at every degree band, and emits `news.told` at
**Overwhelming / Success / Partial** and `news.untold` at **Failure** (`:521-525`). The told channel
(`loop/witness.py:315-369`) deposits the teller's claim into each hearer's ledger with **the teller's own
confidence** (`:363`; `:304-310` argues why: *"Nothing in the chain states how much a hearing costs a
belief"*), source `told_by`, and **verbatim content** — `_told_content` (`:31-70`) returns
`LedgerReader(teller.ledger).latest_about(subj)` and the deposit copies its `subject`, `predicate` and
`value` unchanged (`:361-363`).

**Measured on the populated world, one season:** 30 tellings — 8 `news.told`, 22 `news.untold` — and
**exactly 1 `told_by` claim deposited**, because the exact-triple guard (`:349-350`) suppresses a telling
of something the hearer already holds. The docstring's own figure is the control: *"MEASURED over the 89
corpus worlds before this guard: 180 `told_by` claims, of which **175 were a triple the hearer ALREADY
HELD FIRSTHAND** … The honest figure with this guard is **5**."*

**And the number that decides this section: all eight successful tellings are at `Partial`.**

> ### **RULED: the `Partial` branch is not a speculative third path — it is where the ENTIRE word channel
> currently lands.** `Counter((e.kind, e.degree))` over one populated season: `('news.told','Partial'): 8`,
> and **no `news.told` at `Success` or `Overwhelming` at all.** A design that puts the slippage at
> `Partial` is putting it on the band the loop actually produces, **which is the difference between a
> mechanism and a garnish.**

⚠ **And `Event.degree` already exists** (`carriers.py:98`) and is assigned from the resolution
(`loop/resolve.py:150-155`, which records that it *"was a declared field NOTHING EVER ASSIGNED"* until
`W-E` closed it). **So the branch needs no new carrier field and no new plumbing** — it reads a field the
Event has carried since 2026-09-04.

### §A.10.1 · What may be omitted — exactly one addressee, and never the last

At `Partial`, the hearer's copy of a `content:<kind>` claim may lose **one id from the addressee key**
(`to`), and that is the only omission the loss function permits.

- **Exactly one, never two.** The band is not a dial.
- **Never the last remaining id.** If `len(to) == 1`, **no omission is made** and the drift branch
  (§A.10.2) is taken instead. Jordan's first ruling forbids the alternative in terms: *"the game can't
  function as a game where the player can feel their choices mattering if all dissemination of information
  is so noisy that it's moot."* **An empty `to` is a writ addressed to nobody, which is moot.**
- **Never an addition.** The lossy copy is a **strict subset** on that key. An added id would be the
  hearer's claim *inventing an executor*, which is §A.1's forbidden shape wearing a rumour's clothes.
- **Never the hearer himself, if he is named.** If `p.id in to`, the omission never removes `p.id` —
  because *"I was told the Duke named others"* is slippage, and *"I was told the Duke named others and not
  me"* is **the rumour deciding whether the hearer is bound**, which is a reception mechanism overwriting
  the act's content *about the hearer*. ⚠ I expect an attacker to press this clause and I concede its cost
  openly: **a rumour can never relieve you of a duty**, only mislead you about whose company you are in.

### §A.10.2 · What may drift — one numeric operand, inside a stated band

At `Partial`, **exactly one numeric operand inside the terms** may drift by at most
`fixtures.told_drift_band` (a fraction; content, declared, swept — the `H-80`/`H-94` shape).

- **Numeric only.** An id does not drift into another id — that is not slippage, it is **substitution**,
  and a rumour that renames the executor has authored a different order.
- **One, not all.** If the terms carry three numbers, **one** moves.
- **Bounded and signed.** `|after − before| ≤ ceil(band × |before|)`, and `after` **never crosses zero or
  changes sign**. *Two grain becomes three; two grain does not become minus two, and does not become twenty.*
- **The band is a fixture for the reason `data/fixtures.py:432-436` gives for `default_transfer_amount`:**
  direction ruled, magnitude open, is exactly a fixture.

### §A.10.3 · What may NEVER change — the clause Jordan's second ruling buys

| may never change | why |
|---|---|
| the claim's **`subject`** — the Record id | a rumour about a writ is a rumour about **that** writ. Change the subject and the hearer believes in a document that does not exist, **and can never travel to check it** |
| the claim's **`predicate`** — `content:dispensation` | the kind is what the hearer must know in order to act at all |
| **`terms`** — the `PropositionId` | `Proposition` is `frozen=True` (`carriers.py:467`) and immutable by §14. **The rumour may misremember a number; it may not misremember which OUGHT** |
| **`at`** — the rung of discharge | the place is the one term a hearer can verify **by walking there**. Drifting it makes the whole instrument unfalsifiable from inside the world |
| **any id that remains** in `to` | §A.10.1 |
| **the `Record` itself** | nothing in this branch touches `w.records`. **"Verbatim or not at all" is a property of the carrier** (§A.4), not a rule this branch obeys |
| **the teller's own ledger** | `_told_content` **reads** it and the branch writes the **hearer's**. ⚠ **This is `RR-P`'s test satisfied as an assertion, not as a promise:** the draw decided what the listener took away, never what the teller meant |
| **any other hearer's ledger** | the selection is per-hearer (§A.10.4), so one telling's losses are independent |

> ### **RULED: the writ's FIDELITY is protected and its RECEPTION is not, and the two are different
> objects in different stores.** Jordan's second ruling — *"the written letter in some form with fidelity
> would end up being directly given to the settlement leader"* — is satisfied by the **`Record`**, which
> has no writer after creation. Jordan's first ruling — *"there needs to be noise and slippage and
> interpretation"* — is satisfied by the **`Claim`**, which is per-holder by `AX-2` and lossy at `Partial`.
> **Neither ruling constrains the other, because the writ and the word are not two copies of one fact:
> they are a thing and a belief about it.**

### §A.10.4 · The selection is deterministic and consumes no draw

**Which addressee is dropped, which number drifts, and in which direction, are derived from
`H(world_seed, tick, hearer_id, f"told:{event_id}")`** — **the same hash the deposit already mints its
claim id from** (`loop/witness.py:361`).

- **No new randomness source.** `w.draw` (`state/world.py:177-181`) is a per-tick ordinal whose uniqueness
  contract is *"per DRAW, not per operation"*; spending one here would shift every subsequent draw in the
  season and change **every unrelated contest**. **The lossy copy must not perturb the stream.**
- **`H` is the owned mint** (`state/ids.py:16-22`), blake2b over `v1|seed|tick|subject|purpose`, and
  `tools/m1_acceptance.py` row 2 (*same seed → same `KeyLog.content_hash()`*) depends on exactly this
  property. Deriving the selection from `H` keeps the replay contract intact.
- **Per hearer, not per telling.** Two hearers of one telling lose **different** things, because `pid` is
  in the mix. **That is what makes a rumour fan out into disagreement rather than into one shared
  distortion** — and `agreement` (`options.py:412`) is already the instrument that scores it.

### §A.10.5 · The anomaly this branch must survive, measured

`Counter((e.kind, e.degree))` over one populated season returns **`('news.untold','Partial'): 2`** and
**`('news.untold','Success'): 1`** alongside the 19 at `Failure`. A *refusal* kind carrying a
non-`Failure` degree means the contest resolved and the fold refused after it. **I do not diagnose it
here** — it is not this file's item and I have not run the fix — but it decides the branch's guard:

> ### **RULED: the lossy branch keys on `e.kind == "news.told"` AND `e.degree == "Partial"`, both.**
> Keying on the degree alone would apply the loss function to three events that **transmitted nothing**.
> The existing code already tests the kind (`loop/witness.py:316`); the addition is the degree, and **the
> conjunction is what makes the branch correct in a world where the two are not equivalent.**
> **Falsifier `WW-9` asserts on exactly those three events**, which is `CLAUDE.md` §0.1 pt 2: an
> assertion that can observe the failure it excludes.

⚠ **One more conformance note that saves a future session a wrong turn.** The told channel skips a claim
whose predicate stem is in `LEDGER_DERIVED_STEMS` (`witness.py:333`), because *"`claim.held` answers from
ledger MEMBERSHIP, so storing it makes its own content true."* **`content` is not such a stem** — it is
not in `REQUIRES_STEMS` at all — so a `content:` claim **is** tellable, which is what the word channel
requires. Verified by opening both lists.

## §A.11 · SPEED IS NOT AN AXIS — the two channels, and what each buys

**Jordan's third ruling, verbatim:** *"speed of a writ can be the same as word of it given that the message
can be delivered directly as required to those who must implement it."*

| | **THE WRIT** | **THE WORD** |
|---|---|---|
| what travels | a **`Record`** | a **`Claim`** |
| fidelity | **verbatim or not at all** — no writer after creation (§A.4) | **lossy at `Partial`**: one addressee, one number, within a band (§A.10) |
| who is bound | **exactly whom you named** in `to` | **whoever hears**, and only as far as they believe it |
| **speed** | **the same** | **the same** |
| how it travels | a carrier's own `move`, then `give` | `tell`, over channels that already run |
| what it costs the issuer | **a person and their season** — one of ~5 acts (`holonic §26.3`, RULED) plus the carrier's whole journey | **nothing beyond the telling** |
| what it costs the receiver | nothing; **he may refuse to take it** | nothing |
| what it leaves behind | **physical evidence** — producible, checkable, forgeable, destructible, inheritable | **nothing** |
| its variance | arrived / not · when · genuine / forged · how many copies · in whose hands | omission · drift · who heard · what they already believed |
| how it is verified | **travel to the holder and witness the Record** (`co_located` + the deposit rule) | you cannot verify a rumour; you can only find the document |
| what it cannot do | reach somebody you did not name | **bind anybody** |

> ### **RULED: the two channels are distinguished by FIDELITY, ADDRESSING and EVIDENCE — never by speed,
> and there is no latency parameter anywhere in this design.** A writ is not the slow channel and the word
> is not the fast one; both arrive when the person carrying them arrives, and word arrives along channels
> that are already global at a barrier. **What the player buys by spending a season on a writ is not
> haste. It is a named executor, a term nobody can misremember, and a thing on the table when he denies
> it.**

⚠ **Why this matters more than it looks.** A speed axis is the one shape that would let the player
**optimise the channel** — spend the writ when you have time, the word when you do not — which collapses a
political decision into a scheduling one. **With speed equal, the choice is what kind of hold you want
over the outcome**, and that is a decision about the world rather than about the clock.

## §A.12 · INDEPENDENT ARRIVALS — and which lands first is itself a situation

**The two channels do not synchronise.** `tell` is an act, `give` is an act, and `H-54`'s hash decides which
question a budget-bounded person answers first (`hole_register.yaml:618`; `world_q.py:530-547`, which
measures *"the leading source is SHARED with at least one other question in 801 of 1,068 deliberations"*).
**Four cases, and each creates a decision nobody authored.**

### Case 1 — THE WORD FIRST, and the writ never comes
The reeve holds a `told_by` claim naming him and no document. Q2 fires on clause 3 (§A.9.1), so **he is
asked.** His operands come off the claim's value (§A.13) — which may be the lossy copy.

> **The decision:** act on hearsay, at operands that may have drifted, or wait for the paper. **Either way
> he is exposed:** comply on a rumour and the Duke's `document_key` sees a transfer that does not match his
> terms; wait, and the Duke sees nothing at all **and cannot tell him from a man who refused.**
> `holonic §37.3` row 4 is the whole of this: *"the distinction between never received and received and
> refused, which is the whole of enforcement drama."*

### Case 2 — THE WORD FIRST, then the writ
He acts on the rumour; the carrier arrives next season with the genuine terms. He now holds **two claims on
one `(subject, predicate)` with different values** — and the told channel's exact-triple guard
(`witness.py:345-350`) **deliberately lets this through**: *"A hearer who holds a DIFFERENT value for the
same cell is being contradicted, and that is the epistemic layer working — `agreement` pairs precisely
those."*

> **The decision:** he has already moved the grain. **Does he correct it, conceal it, or claim the rumour as
> his authority?** The design supplies **no reconciliation rule and needs none** — `agreement` scores the
> gap, `standing_of` reads it, and the man decides. ⚠ **`RR-P` is what makes this lawful rather than a
> corruption:** the earlier act is still in the act store with its operands intact (boundary 2). **He did
> what he did.**

### Case 3 — THE WRIT FIRST
He holds the document. The deposit rule gives him a **`firsthand`** `content:dispensation` claim at full
confidence, and `AX-2` does the rest: *nobody else in the world can read his ledger*, so **he is the
authority on what the writ says to everybody who cannot read it.** A later rumour arrives as a `told_by`
claim he already contradicts, and the guard suppresses it only if it is an exact triple.

> **The decision:** **what to tell people it says.** `tell` passes *his* claim (`witness.py:65-70`), so a
> holder who misreports the terms **is not lying to the engine** — he is telling the truth about his own
> ledger, and the gap is between his claim and the Record. **Anybody may travel to him and witness the
> document** (`co_located` + the deposit rule), and **that is the only check.** This is exactly the gap
> Jordan named: *the man holding the writ is the authority on what it says to those who cannot read it.*

### Case 4 — NEITHER ARRIVES
Nothing happens. **No question fires, no claim lands, and the Duke's writ sits in a carrier's bag in a
blocked pass** — **23 of 26 movement attempts blocked**, measured. `holonic §37.3` row 4 preserved by the
world simply being difficult.

> ### **RULED: which channel lands first is a SITUATION, not a race, and no rule orders them.** The engine
> supplies no arbitration between a rumour and a document, and none is wanted: **the arbitration is the
> executor's act**, which is `holonic §37.2` — *"The person's own need, plus capability, plus this new
> claim, yields an opening … No one authored an opportunity for anybody."*

## §A.13 · COMPLIANCE IS THE EXECUTOR'S OWN ACT

**There is no compliance mechanism.** The executor is asked a question, forms candidates from his own
claims, and acts — and the acts are ones the table already carries.

| what the writ demands | the executor's act | already? |
|---|---|---|
| matter moved | **`transfer`** (`verb_table.yaml:728-744`) | resolvable; measured **16 refusals and 0 successes** in the populated season |
| a duty undertaken | **`commit`** to the Proposition — the oath, `AX §E.1.7` | row at `:115-129`, `writes: ["Tenure.since"]`, **no effect body**; build item 1 |
| a duty refused, having been taken | **`repudiate`** (`:433-447`) | typed (`existence of subject kind commit`), **no effect body** |
| a thing built or mended | **`work`** on a `works` Record, then `restore` / `found` | `04`'s; `work` is resolvable and runs (**38 `work.unavailable`** in the season) |
| a seat filled | **`confer`** | resolvable; `03`'s |
| a person sent | **`issue`** naming him (§A.6.1) | the fold |
| **nothing** | **no act** | **and this is the one the surface must show** — §A.17 |

**How the operands reach the act.** `_derive_operand` (`options.py:259-323`) gains one branch family,
modelled on `store_kind_of` (`:234-256`), which already reads a matter kind off a claim's predicate:

```python
# When the question's referent is a `content:` claim, the operands are the WRIT's, not the fixtures'.
if (v := _from_content_claim(p, q, name)) is not None:   # name in (to, at, kind, amount)
    return v
```

⚠ **`from` stays `containing_rung_of(p)`** (`:316-317`) and is **not** read from the writ. Deliberate:
`AX-2` and the design both make *where you are* the actor's own state, and a writ that could name `from`
would let a Duke's document reach into a larder the executor is not standing in — **which is `levy`
(§A.20) with extra steps.**

> ### **RULED: `comply` is not a verb. It is `transfer`, or `commit`, or `work`, or nothing — and the
> closed operand roster is the PROOF rather than the obstacle.** `rosters.yaml:1074-1079` says of `comply`:
> *"It is the reason `comply` and `exchange` carry `requires_typed: none` … the first needs a DISPENSATION
> and … neither has a name here. Coining one would be filling `H-94` by keyword argument."* **Under this
> design nothing needs a `dispensation` operand.** The executor's act is `transfer`, whose operands —
> `from`, `to`, `kind`, `amount` — are **all in the closed eight**, and whose typed cell
> (`scalar_threshold`) already evaluates. **The operand gap closes by the verb that needed a ninth operand
> ceasing to exist.**

⚠ **And one thing the writ does NOT buy, stated plainly:** compliance is **not a distinguishable act**. A
`transfer` made in obedience and a `transfer` made for one's own reasons are **the same Event with the same
kind**. The issuer learns *that grain moved* (§A.17), never *that he was obeyed*. **I refuse to add a
compliance flag**, because a flag would be the act asserting its own motive, and `AX-2` puts motive in
nobody's reach — attribution is a per-witness Claim (`ARCH §C.6`, `holonic`'s `T-d`). **The Duke infers
obedience and may be wrong, which is the game.**

## §A.14 · MATTER READS NO POLICY — with the correction my source needed

**The claim I inherited is false as written, and I correct it rather than repeat it.** My specification says
*"`matter.py` touches no Record or Proposition — true today at `:30-296` and stays true."*
~~It does not touch a Record.~~ **It does.** `loop/matter.py:65-74` iterates `sorted(w.records)`, reads
`rec.stages`, and reads the live `hold` Tenure to find the holder; `:106-109` writes `matured` through the
gate. **Measured by opening the file.**

| MATTER reads, of a Record | MATTER does **not** read |
|---|---|
| the key set of `w.records` (`:65`) | **`subject_matter`** — not once, anywhere in the file |
| `rec.stages` (`:67-72`) | **`kind`** |
| the live `hold` on it (`:73-74`) | **any Proposition** — `grep -n 'proposition' loop/matter.py` → no match |
| and writes `matured` (`:106-109`) | **`forgery_quality`**, **`ttl`** |

> ### **RULED: MATTER reads a document's CLOCK and its CUSTODY, and never its CONTENTS — and that is
> exactly the property `holonic §37.3` row 2 requires.** *"applying a dispensation as a state write"* would
> delete *"the compliance contest, and therefore all political friction."* A barrier that reads `stages` and
> `hold` is reading **whether a deadline came and whether anyone is still carrying the thing**; a barrier
> that read `subject_matter` would be **the world enforcing the Duke's terms with nobody in between**,
> which is round one's `in_force` in a different file. **The invariant to keep is not "MATTER touches no
> Record" — it is "NO MATTER-CLASS WRITE IS A FUNCTION OF A DOCUMENT'S CONTENT."**
> *Falsifier:* `WW-11`, which greps the barrier for `subject_matter` and asserts zero — and **can observe
> the failure it excludes**, because that string is unique to the field.

⚠ **And this is where the MATTER half of round one dies.** `in_force(w, rung, clause)` and **every
place-scoped read of policy** are **struck**. There is no walk from a rung to an ancestor's clause. A
province does not satisfy a condition. **The only thing that happens between a writ and a larder is a
person deciding to move grain.**

## §A.15 · THE FORGERY PATH, END TO END — and the honest state of `forgery_quality`

**What exists, and my source overstated it.** My specification says `forgery_quality` is *"declared and
written by `forge` (`verb_table.yaml`) with no reader — a shipped producer awaiting a consumer."*
~~The producer is not shipped.~~ **Measured, 2026-09-17:**

| the artifact | state |
|---|---|
| `Record.forgery_quality: int = 0` | declared, `carriers.py:428` |
| matrix row `(Record, forgery_quality)` | `write_matrix.yaml:252-258` — `steps: [RES]`, `class: ACTS`, `by: DR-2`, **`emits: record.forged`** |
| verb row `forge` | `verb_table.yaml:247-255` — `writes: ["Record.exists", "Record.forgery_quality"]`, `grade: assumption`, **`emits: ["record.created"]`** |
| **`forge` is resolvable** | **False** — no `@effect_for("forge")` among the 11 |
| readers of `forgery_quality` anywhere in `engine/` | **zero** (`grep -rn forgery_quality --include=*.py` → the declaration, and one archived prototype under `proposals/`) |
| `forgery_quality != 0` in the populated world | **0 of 69** |

> ### **RULED: `forgery_quality` has neither a writer nor a reader in execution. It is a field, a matrix
> row and a table cell, and no code path reaches it.** The correct description is **a declared write with
> no body and no consumer** — three artifacts agreeing about a thing that never happens. ⚠ **And the matrix
> row and the verb row DISAGREE about the emission:** the row says the write emits **`record.forged`**;
> `forge`'s own `emits:` cell says **`record.created`**, and **no verb in the table emits `record.forged`.**
> Found by opening both. That is a `(kind, row)` divergence in the declared data, and **`WW-12` is its
> falsifier — a test that is RED on arrival.**

**The path, end to end, and every step is an act somebody takes.**

| # | who | act | what is written | what is believed |
|---|---|---|---|---|
| 1 | the forger | **`utter`** the OUGHT he wants the Duke to have said | `Proposition.exists` — `frozen`, so **the lie is permanent and has an author** (`AX-6`; `ARCH §B.6`: *"`utterer` is on it because AX-6 requires a permanent thing to have an author"*) | — |
| 2 | the forger | **`forge`** — the shared document body with `kind: "dispensation"`, `subject_matter` naming the executors he wants bound, and `forgery_quality > 0` | `Record.exists`, `Record.forgery_quality` · **the forger's own `hold`** (`effects.py:288-289`) | the deposit rule gives **the forger** a `firsthand content:dispensation` claim — **he believes his own forgery's terms, because a claim is about what a document SAYS, not about whether it is genuine** |
| 3 | the forger | **`move`**, then **`give`** | the hold passes | the mark gets a `firsthand content:dispensation` claim **identical in every field to a genuine one** |
| 4 | the mark | **`transfer`** / **`commit`** | the world moves | — |
| 5 | anybody | **`examine`** the Record (`verb_table.yaml:623`, resolvable; **52 `finding.made` / 85 `finding.none`** in one populated season) | — | ⚠ **and here is the gap: there is no consumer of `forgery_quality`**, so nothing an investigation act does can read it |

> ### **RULED: the forgery path is complete except for its last step, and the missing step is a CONSUMER,
> not a producer.** Every act in the chain exists as a row; two of them (`utter`, the investigation acts)
> are resolvable and run; `forge` needs the same one-line delegation `issue` gets; and the field is there.
> **What is absent is the read that makes a forgery detectable** — a contest of the examiner's capability
> against `forgery_quality`, emitting a degree. **I do not build it and I do not stub it**, for the reason
> `H-84`'s own row gives about inventing a verb to make a case pass. It is named as a **LIMIT** in §C.5 and
> it is **the cheapest genuinely new mechanism in this design's neighbourhood.**

⚠ **What the design DOES get today, free, and it is not small.** Because the deposit rule makes the claim
about *what the document says* and never about *who wrote it*, **a forged writ and a genuine writ are
indistinguishable in every executor's ledger — by construction, not by a flag.** Attribution is a separate
claim with its own source (`ARCH §C.6`: `co_located` mints it, `document_key` does not), so *"the Duke
wrote this"* is something you were **told** or **saw**, and **a forgery is caught socially long before it
is caught forensically**: the mark tells somebody, that somebody holds a contradicting claim about what the
Duke would say, `agreement` pairs them, and a man travels to ask. **That chain runs on shipped parts.**

## §A.16 · COPIES, DESTRUCTION, CUSTODY — and a writ does not lapse

### Copies
**A copy is the document body again, with the same kind and the same `subject_matter`, by somebody's hand.**
No new verb, no `copy_of` field, no link. Three consequences:

- **Copies are independent objects with independent custody.** Five copies of one writ are five Records,
  five holds, five maturation clocks and five `content:` claims when they land — **which is how one
  issuance reaches five executors from one chancery.**
- **Copies cost an act each** (~5 per season, `holonic §26.3`), and they are somebody's acts. **A Duke who
  wants ten hamlets bound spends his season, or his clerks' seasons, on ten documents.** *This is the whole
  answer to "why is a broadcast not free", and it needs no rule.*
- **A copy made by a clerk who misremembers is a forgery with `forgery_quality` set** — the same act, the
  same field, and **no distinction in the code between malice and error.** The design has one mechanism for
  both, which is right: **from the reeve's side they are identical.**

### Destruction
`destroy_record` (`verb_table.yaml:176-185`), **resolvable**, `eligibility: ["hold:<record>", "presence"]` —
both alternatives placeholder-or-unevaluable person-side, so **no computed act destroys a Record today** and
a declared one does. `_eff_destroy_record` (`effects.py:293-307`) removes the Record **and every `hold` on
it** — *"S15.3's rule that a tenure dies THROUGH the death of what it is over, never beside it."*

> ### **RULED: burning the writ is the real countermeasure, and it is already shipped.** The claim in the
> executor's ledger **survives** — `AX-5`'s fading removes **confidence** and never **value** (`AX-3`'s
> carve-out: *"A memory can dim to nothing and can never become a different memory"*) — so after the fire
> **he still believes what it said and can no longer prove it, and neither can the Duke.** That asymmetry
> **is** the enforcement drama §37.3 row 4 is about, produced by two shipped bodies.

### Custody, and the one cardinality that is unenforced
`holonic §15` (:538) says `hold` is **1 per object**. `add_tenure` (`state/world.py:223-258`) enforces the
**kind** roster (`:242-247`) and `contain`'s **direction** (`:248-256`) and **does not enforce that
cardinality.** `_eff_confer` maintains it behaviourally by closing priors (`effects.py:118-122`);
`_eff_create_record` mints exactly one; **nothing else checks.** `_eff_give` follows `confer`'s pattern.

> ### **RULED: `give` MAINTAINS the cardinality and does not ENFORCE it, and I say so rather than claiming
> a guard.** `04` and `05` carry the `add_tenure` hold-domain conjunct (round one's surviving argument);
> **the cardinality conjunct is a separate thing and is not in this design.** `CLAUDE.md` §8's *"a false
> claim of enforcement is worse than none"* — which `state/ids.py:5-7` states in those words about its own
> mint — is why this paragraph exists.

### A writ does not lapse, and `ttl` must stay unwired
`Record.ttl` is declared (`carriers.py:430`), `[MAT]`-stepped (`write_matrix.yaml:273-277`), exempt from the
must-name-a-kind rule via `conditional_emission_rows` (`state/world.py:385-387`; `matter.py:141`), and
**nothing decrements it.** Round one's UNIFICATION_LEDGER row 10 kept a `ttl` lapse as *"a named fourth"*
use of the emission rule. **I overturn it.**

> ### **RULED: `ttl` stays unwired, because a document expiring on a clock nobody wound is a FOURTH
> world-motion and `AX-5` says three.** `AX-5`: *"THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS: MATTER,
> BODIES, AND THE FADING OF MEMORY … Three is a stipulation. Two would be a different game; four would be
> a different game."* And `AX-5`'s CENSUS paragraph shows the shape of the only admissible defence —
> individuation survives because *"the demand is its author."* **A writ's expiry has no author.** So:
>
> | how a writ stops mattering | which of the three motions |
> |---|---|
> | somebody **burns** it | none — it is an act |
> | the issuer **issues another** | none — it is an act |
> | the holder **dies** and nobody takes it up | none — and `matter.py:73-78` already stops its clock |
> | **everybody forgets what it said** | **the fading of memory** — `AX-5`'s third motion, already running: `(Claim, confidence)` decays at MATTER (`matter.py:147-153`) |
>
> **So the answer to "how does a policy stop being in force" is: IT NEVER WAS IN FORCE. People believed it,
> and belief fades.**

⚠ **Round one's (b) is STRUCK:** ~~*"A policy falls out of force when its issuer dies, because `in_force`
requires a live hold"*~~ — **there is no `in_force`.** What survives of that section is **(a)**, *a works
stops when its maker dies* (`matter.py:73-78`, unchanged), and **(c)**, *the first season of a reign is
spent re-issuing* — **but for a different reason:** not because holds lapsed, but because **nobody yet
believes the successor's remit** (`03`'s commission claim, `H-71`) and because the dead man's writs name
executors who may have died or moved. **Re-issue becomes a choice rather than a repair**, which is the
better game and the honest reading. ⚠ **A dead duke's writ still binds whoever believes it** — and I state
that as an intended consequence rather than a leak.

⚠ **And round one's own LIMIT in that section is exactly what `give` closes.** It read: *"Because maturation
requires a live `hold`, a Record cannot change hands today … the smallest lawful route is widening
`confer`'s object domain."* **Superseded.** Widening `confer` would make one verb seat offices **and** pass
documents; **position 16's `give` is the ratified answer and costs the same row.**

## §A.17 · THE ISSUER LEARNS LATE — three routes and no fourth

**There is no report.** No acknowledgement object, no return channel, no status field. The Duke finds out
the way anybody finds out anything, and **there are exactly three ways.**

| # | route | the mechanism, shipped | what he learns |
|---|---|---|---|
| 1 | **`document_key` on his own holdings** | `_ch_document_key` (`epistemic.py:331-333`) reads `changes[]`, and `_eff_transfer` returns `[src.id, dst.id]` which `_apply_write` turns into `StateChange`s subjected to the **rungs** — *"a non-author, witnessing an act, through the bureaucratic channel"* (`:301-309`), pinned by `test_r8_4_document_key_reaches_a_non_author_through_a_store` (`engine/season/tests/test_season_shape.py:10322`) | **that grain moved into a store he holds.** Not that he was obeyed — §A.13 |
| 2 | **the carrier's `tell` on return** | the told channel; the carrier's claim is `firsthand` if he watched the reeve act | **what one man says he saw**, at that man's confidence, **lossy at `Partial`** |
| 3 | **his own travel** | `move`, then `co_located` witnesses whatever is happening — plus the deposit rule if the writ is handed back | **the truth, at the cost of a season** |

> ### **RULED: there is no fourth route, and the absence IS the design.** A reporting channel would be
> `holonic §37.3` row 4 inverted — assuming *delivery of the answer* — and would delete the thing that
> makes enforcement dramatic: **the Duke cannot distinguish a reeve who never got the writ from one who got
> it and did nothing.** Route 1 fires **only on success**; routes 2 and 3 cost somebody a season.
> **Silence is the default state of the instrument.**

**`03_THE_SURFACE.md` (STANDING) already has the cells for it**, and this file hands it three readings
rather than a new surface: **HELD** (who holds a copy), **STALE** (whose claim about it has decayed),
**UNHELD** (whom you named who never took one). ⚠ Round one's **compliance table** on that surface is
**struck** and replaced by those three readings; **`03` carries the strike, not this file, and I add no
surface.**

⚠ **H-92's first consumer is deleted and its second is this rule's own channel.** `decision/budget.py:57`
pays `budget_office_bonus` per live hold, so **a landholding buys scene actions**
(`hole_register.yaml:1108`) — and once a Record is a `hold`, **possessing documents would buy scene actions
too.** The term and its fixture (`data/fixtures.py:430`) are **deleted**; `04`'s build item owns the
falsifier. **I name it here because the deposit rule is what makes it urgent: 69 Records a season × a bonus
per hold is a budget that grows with paperwork.**

## §A.18 · EXECUTORS, NOT PLACES — `holonic §37.3`'s four prohibitions, one at a time

The table, opened at `architecture/holonic_ARCHITECTURE.md:1303-1308`, each row answered **on its own terms**
rather than in aggregate.

### Row 1 — **"broadcasting a dispensation to all descendants"** · deletes *"T3 and T6 both — everyone would receive identical, undistorted terms"*

**Round one's `reach: all` was this**, and `AUDIT_VERDICT`'s false-N-line list says so: *"the operand
carried only the broadcast §37.3 forbids."*

**Answered by construction, in three places at once.**

1. **`to` is a list somebody typed.** There is **no value of `to` that means everyone**, because the
   `record_kinds` schema types it as a list of ids and the constructor refuses a wrong key. **A writ naming
   the realm is a writ naming nobody.**
2. **Nothing in the engine walks from a writ to a set of people.** The only walk in the chain is `presence`
   inside `_req_give`, and it answers *who is standing here* — the carrier's problem, not the writ's.
3. **Reception is per-person and lossy.** Two hearers of one telling receive **different** terms (§A.10.4,
   the hash is keyed on `pid`), so *"identical, undistorted terms"* is unreachable **even for the people who
   do hear.** **The prohibition's own failure condition cannot be constructed.**

> **What it costs, and I state it rather than claiming it free:** reaching ten hamlets costs ten documents
> and somebody's ten acts (§A.16). **A Duke cannot address his realm.** He can address the men who can
> address it — **which is what a realm is.**

### Row 2 — **"applying a dispensation as a state write"** · deletes *"the compliance contest, and therefore all political friction"*

**Round one's MATTER read was this.** Answered by **the absence of a path** — §A.14's measurement: no
barrier reads `subject_matter`. The only writes in the whole chain are `(Record, exists)` at issuance,
`(Tenure, until/since)` at `give`, and `(Person, claim_ledger)` at WITNESS, **and none of the three is a
function of what the writ says.** The writ's terms are read in exactly one place: `_derive_operand`,
**person-side**, when building **that person's** candidates (§A.13). *Falsifier `WW-11`.*

> ⚠ **And the phrase *"compliance contest"* is NOT delivered, which I say rather than imply.** §37.1 says a
> published dispensation *"lands as a compliance contest, per relevant Rung, through `contest`."* **This
> design lands it as a QUESTION, not a contest** — Q2 on a `content:` claim — and the executor's answering
> act may or may not route to the seam depending on which verb he forms. `transfer` and `commit` are
> uncontested; a seizure would be contested and **has no provider** (§A.19). **That is a narrowing of
> §37.1, and it is `holonic §37.4`'s licence being spent: *pick one, write it down beside the code.*** The
> ground for picking: **a contest needs two claimants and a prize**, and *the reeve against the writ* has
> one claimant and a piece of paper. **A contest arrives the moment a second person cares** — §A.19.

### Row 3 — **"a `scope` that enumerates places"** · deletes *"office-clusters with `rung? = null`, which have no place"*

**`to` carries `PersonId | OfficeId` and never a `RungId`.** `at` carries a `RungId` and is **not** the
scope — it is where the terms are discharged, a property of the *obligation*, not of *whom it binds*. **The
two are different keys in the schema precisely so a reader cannot conflate them.**

**And the case the row protects is already asserted by a shipped probe** (`harness/probes.py:1148-1160`):

```python
off = w.offices["off_dicastery"];  assert off.rung is None
scope = ["p_low", "p_king"]        # p_king sits under the realm, outside S's subtree
...
"PASS: `rung? = null`, and SCOPE ENUMERATES EXECUTORS, NOT PLACES -- ... are outside the
 settlement's containment subtree entirely. A Dicastery, a chivalric order and a trans-settlement
 guild HAVE NO CONTAINMENT NODE, so R-1/R-2 do not govern this"
```

> ### **RULED: that probe's property transfers to `subject_matter["to"]` unchanged, and the probe IS the
> falsifier already written.** Today it asserts against `w.dispensations`, **which nothing else reads**;
> after the fold it asserts against the Record, and **the assertion does not change** — which is the test
> that the fold preserved the ratified property. *Falsifier `WW-5`.* ⚠ **And `holonic §38`'s lateral rule is
> why this matters beyond neatness:** an `Office` with `rung = null` is *"resolver-side … unreachable from
> `choose` by construction"*, so **a place-scoped writ could never reach a Dicastery, a chivalric order or
> a guild — the three institutions most likely to be interesting.**

### Row 4 — **"assuming delivery"** · deletes *"the distinction between never received and received and refused, which is the whole of enforcement drama"*

**Three distinct states, each readable from a different shipped fact, and NO FIELD distinguishes them:**

| the executor | what is true in the world | how the issuer could learn |
|---|---|---|
| **never received** | no `hold` on any copy, **no `content:` claim in his ledger** | only by travelling, or by the carrier reporting failure |
| **received and refused** | a live `hold`, a `firsthand content:` claim, **and no act** | only by travelling — route 1 never fires, because nothing changed |
| **received and complied** | the hold, the claim, **and a `transfer`** | route 1 fires (§A.17) |

**The distinction is structural** — an absent Tenure, a present Tenure with no consequent act, a present
Tenure with one — and **nothing in the design collapses the first two**, because the issuer's only automatic
channel fires on a **change**, and both of the first two are the absence of one.

> ### **RULED: all four prohibitions hold, and three of the four hold by CONSTRUCTION rather than by
> discipline.** Row 1: no value of `to` means everyone, and reception is per-person. Row 2: no barrier reads
> the content. Row 3: the schema separates addressee from place, and a shipped probe asserts it. **Row 4
> holds by the ABSENCE of a reporting channel — the one of the four a later session could break by adding a
> convenience** — so it is the one with a falsifier aimed at it (`WW-8`) and the one named **CONVENTION**
> rather than STRUCTURAL in §C.2.

## §A.19 · SEIZURE IS A LIMIT, AND IT IS NOT DRESSED

**A lord may not take what a man will not give.** There is no mechanism here for forced compliance, and the
reason is specific: seizure is a **contest** between the lord's men and the holder, and
`resolvable_verbs()`'s third gate excludes every contesting verb whose seam cannot be reached with two
claimants (`loop/driver.py:100-119`): *"a contested act needs a `subject` operand to name the second
claimant, and `operands_for` returns `{}` for an UNTYPED verb."*

| what would be needed | state |
|---|---|
| a verb whose `contests:` prize is the matter | **absent** |
| a registered provider for that contest | **absent** — `manifest/registry.py:82`'s registration is what the third gate reads |
| two claimants derivable person-side | **absent** — the `H-94`/`H-80` operand famine |
| a degree→outcome mapping for a seizure | **absent** |

> ### **RULED: seizure does not resolve, and `levy` is DELETED rather than kept as the
> seizure-without-a-contest that it is.** **The honest state of the design is that the writ's only
> enforcement is social** — visibility, standing, and the next writ naming somebody else. ⚠ **And that is a
> real R-CHOICE finding which I pre-commit rather than paper over** (§B.5): **silence beats refusal**,
> because an executor who does nothing is **visible and unpunished.** It stays a limit until a decision
> layer or a proceedings subsystem supplies a contest. **I manufacture no sanction.**

## §A.20 · `levy` IS DELETED NOW, AND NOT UNDER A RULING

`verb_table.yaml:348-360`. `scale: settlement`, `scale_note: "a levy moves a Rung's stores -- the rung IS
the subject"`, `eligibility: ["remit:issue", "presence:<rung>"]`, `writes: ["Rung.stores"]`,
`grade: assumption`. **Measured: not resolvable.** And its own row confesses twice:

- `eligibility_note`: the source cell carried a precondition inside the eligibility, *"so it NEVER MATCHED
  and a holder of the remit was silently refused."*
- `eligibility_substitution`: *"⚠ DECLARED 2026-09-03 rather than left silent. The source cell named
  `remit:levy`, and `levy` IS NOT IN `remit_acts` … W3 substituted `remit:issue` and wrote no note, which is
  an off-register fill under §42.2/G.4.8 … Either `levy` joins the roster (a ruling: it is a SEVENTH remit
  act) or `issue` is genuinely the remit a levy exercises."*

> ### **RULED at `CLAUDE.md` §0 gate 5 (the architecture decides where 1-4 are silent): `levy` is deleted,
> and it is not part of RR-A.** It is *a lord's hand reaching into a larder with nobody in between* — a
> `Rung.stores` write **at a place**, gated on presence, with **no counterparty and no contest**, which is
> `holonic §37.3` row 2 named and row 4 skipped. It is also **`ED-IN-0210` ruling 1** — *"verbs invoke
> mechanisms or interactions between a character and another entity/character. **they are not fiats**"* —
> with that row's own four fiat symptoms: *"a fiat needs no counterparty … a fiat cannot fail on the world's
> terms … a fiat is monotonic."* **What replaces it is `issue` + `give` + the reeve's own `transfer`** —
> three acts by two people where there was one act by one, and §A.21 walks it. ⚠ **And the open ruling its
> `eligibility_substitution` names — *is `levy` a seventh remit act?* — is answered by the deletion: there
> is no seventh remit act, and `remit_acts` LOSES a member rather than gaining one** (`dispatch`, §C.6 RR-A).

## §A.21 · THE FULL LIFE OF A WRIT, ACT BY ACT

**One writ, from the Duke's intention to the reeve's grain, with what is written and by whom at every step.**
Seasons are indicative; **every row is somebody's act out of ~5**, except the rows marked *(barrier)*, which
**nobody chose.**

| # | season | who | act / barrier | what is WRITTEN, and by which owner | what is BELIEVED, and by whom |
|---|---|---|---|---|---|
| 1 | 1 | the Duke | **`utter`** the OUGHT — *"the settlement of Hamn owes the duchy six grain"* | `(Proposition, exists)` · `_eff_utter` (`effects.py:423-436`) · frozen, immutable, authored (`AX-6`) | **nobody.** An utterance is not a telling |
| 2 | 1 | — | *(barrier: WITNESS)* | `(Person, claim_ledger)` for whoever was co-located | the men in the hall hold a `firsthand` claim that a Proposition was uttered |
| 3 | 1 | the Duke | **`issue`** — subject = the Proposition, `to = [<the reeve of Hamn>]`, `at = <Hamn>` | `(Record, exists)` · the shared document body → `_eff_create_record` · **and the Duke's own `hold`** (`effects.py:288-289`) | — |
| 4 | 1 | — | *(barrier: WITNESS)* | `(Person, claim_ledger)` **×2 rules**: the observation deposit for the co-located, **and the deposit rule for the new holder** | **the Duke holds `firsthand content:dispensation`** with value `{terms, to, at}`. He believes his own writ — **not trivial: it is what makes his Q2 fire on it next season** |
| 5 | 2 | the Duke | **`give`** the writ to a rider standing in the hall | `(Tenure, until)` the Duke's hold · `(Tenure, since)` the rider's · `_eff_give` | — |
| 6 | 2 | — | *(barrier: WITNESS)* | ledger deposits | **the rider holds the content claim, `firsthand`.** He can now read it, misreport it, or sell it |
| 7 | 2 | the rider | **`move`** toward Hamn | `(Person, travel_leg)`, `(Tenure, until/since)` · `_eff_move` | — · and `place_of(the writ)` now follows him, **with no write on the Record** |
| 8 | 2 | — | *(barrier: MATTER)* | `(Record, matured)` **if** a stage came due **and** the rider still holds it (`matter.py:65-109`; the holder check at `:73-78`) | — |
| 9 | 3 | the rider | **`move`** again — or `travel.blocked`, **23 of 26 attempts, measured** | — | — · **the writ has not arrived and nobody knows why** |
| 10 | 3 | the rider | **`tell`** somebody at an inn what he carries | **nothing** (`writes: []` at every band) | **at `Partial` — 8 of 8, measured — the hearer's copy loses one addressee or one number** (§A.10). **The rider's ledger is unchanged** |
| 11 | 4 | the rider | **`give`** to the reeve, co-located in Hamn | `(Tenure, until/since)` | — |
| 12 | 4 | — | *(barrier: WITNESS)* | ledger deposit | **the reeve holds `firsthand content:dispensation`, VERBATIM** — his copy is the Record's, because the deposit is a `deepcopy` of `subject_matter` and **not a retelling** |
| 13 | 5 | — | *(barrier: DELIBERATE)* | nothing — `(Act[], returned)` only | **Q2 fires for the reeve**, because the writ's id is in `mine` (`world_q.py:471`, `:493`) |
| 14 | 5 | the reeve | `opening_set` over that question; `_derive_operand` binds `to`/`at`/`kind`/`amount` **from the claim's value** and `from` from his own `contain` Tenure | nothing | his candidates now include a `transfer` **carrying the Duke's numbers** rather than `default_transfer_amount` |
| 15 | 5 | **the reeve** | **`transfer`** — or **`commit`** to the Proposition, or **`repudiate`**, or **nothing** | `(Rung, stores)` **×2, one per side** · `_eff_transfer` (`effects.py:438`) | — |
| 16 | 5 | — | *(barrier: WITNESS)* | ledger deposits | **the Duke witnesses it through `document_key`**, because the destination store is a rung he holds and `changes[]` names it (`epistemic.py:331-333`, `:301-309`) |
| 17 | 6 | — | *(barrier: MATTER)* | `(Claim, confidence)` decays for every claim in every ledger (`matter.py:147-153`) | **the reeve's belief about the writ begins to fade. The Record does not** |
| 18 | ⋯ | anybody | **`destroy_record`** | the Record **and every hold on it** (`effects.py:293-307`) | the claims survive, fading. **Nobody can prove anything** |

> ### **RULED: eighteen steps, and this design's contribution to them is FOUR things — a `kind`, three
> schema keys, one verb, and one deposit branch.** Every other write in the table is a body that exists,
> and for eleven of them **a body that ran in the populated world this session.** **That is what "compose
> on the primitive" looks like when it works** — and it is the strongest N-argument in this file: **cut any
> one of the four and the chain breaks at a named step.** Cut `give` and the writ never leaves step 5. Cut
> the deposit rule and step 13 never fires. Cut the schema and step 14 has nothing to bind. Cut the kind
> and step 12 deposits `content:text` with an empty value.

## §A.22 · WHAT A PLAYER ACTUALLY DECIDES

**Jordan's standing requirement is that a governing player must *explicitly set policies*.** Here is the
complete list of what "setting a policy" **is**, as decisions, with **no mechanism hidden behind any of
them.**

| the decision | the act | what it is not |
|---|---|---|
| **what to demand** | `utter` an OUGHT | not a clause from a closed list of seven |
| **whom to bind** | the `to` list on `issue` | not a reach operand, not a rung, **not *all*** |
| **where it is discharged** | `at` | not a scope, and not a place that is bound |
| **by what deadline** | `stages` on the writ | not a `ttl`, which does not tick (§A.16) |
| **how many copies, and by whose hand** | the document body, one act each | **not a broadcast** |
| **who carries each one** | `give`, then somebody's `move`s | not a delivery system |
| **whether to tell people as well** | `tell` | and it is **lossy**, and it is **free** |
| **whether to go yourself** | `move` | the only route to the truth (§A.17) |
| **whether to believe a rumour of somebody else's writ** | act on the claim, or wait | **the design's most common decision, because rumours are free and documents are not** |
| **whether to obey** | the executor's own act, or nothing | **not a `comply` verb** |
| **whether to forge** | `forge` | and **nothing today can catch you** (§A.15's limit) |
| **whether to burn it** | `destroy_record` | the real countermeasure |

> ### **RULED: twelve decisions, every one a named act by a named person, and not one of them a
> parameter.** ⚠ **And the honest caveat: three of the twelve are not formable by a COMPUTED act today** —
> `issue` and `forge` need bodies, and `at` is not in the closed operand roster so a computed writ carries
> `at: None` (§A.6). **A player naming operands reaches all twelve; an NPC reaches nine.** That asymmetry is
> `H-94`/`H-80` and it is not mine to close.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

## §B.1 · What this file adds — and `05`'s ledger is the single owner of the count

`skills/ners/SKILL.md`'s meta-rule: **a fix that adds a system has failed.** So every addition names the
removal it pays for, and **the net is `05`'s to state, not mine.** My contribution to its rows:

| kind | names | +n | pays for |
|---|---|---|---|
| verb row | **`give`** | 1 | `dispatch` (RR-A) — and it is **ratified position 16's verb, named** rather than invented |
| effect bodies | **the document body** (registered for `create_record`, `issue`, `petition`), **`give`**, **`commit`** | **3 functions / 5 registrations** | four rows that exist today with **no body** |
| predicate | **`_req_give`** | 1 | `_req_dispatch` (deleted) |
| roster | **`record_kinds`** | 1 | conceded as overhead in §B.5 |
| deposit rule | document content at WITNESS, **one branch** | 1 | **replaces** round one's new conferral-claim rule |
| `tell` loss function | **one branch** in `_told_content` | 1 | conceded as overhead in §B.5 |
| content (0) | `fixtures.told_drift_band` | 0 | data, not mechanism |

**My share: +8 by function, +10 by registration.** Against it, **from this file alone**: **−5 verb rows**
(`levy` now; `comply`, `evade / defy`, `refract`, `dispatch` under RR-A) · **−1 roster member**
(`remit_acts.dispatch`) · **−2 `World` collections** (`dispensations`, `petitions`) · **−2 matrix rows**
(`(Dispensation, exists)`, `(Petition, exists)`) · **−1 predicate** (`_req_dispatch`) · **−1 term + its
fixture** (`budget_office_bonus`). **−12 against +8.** `05` carries the suite net.

⚠ **The unit caveat, per `CLAUDE.md` §0.1 pt 4 — *a proposal that reports only the favourable unit fails*.**
Three of my additions are **bodies for rows that already exist**, which under a "names" unit count as +1
each and under a "systems" unit count as **0** — *a declared write acquiring its declared behaviour is not a
new system.* Under a systems unit my share is **+5 −8**. **Both are stated; neither is hidden.**

## §B.2 · What it makes unnecessary

| retired | why it is no longer needed |
|---|---|
| `in_force(w, rung, clause)` and **every place-scoped read of policy** | there is no place query. A writ names people (§A.18 row 3) |
| round one's **seven clause forms** | the terms are a `Proposition`, which is the general case of all seven and needs no eighth |
| round one's **uniformity rule** (`AUDIT_VERDICT` limit 6: *"has no checker"*) | **there is nothing to keep uniform:** `subject_matter` is typed by `record_kinds` and refused at the constructor |
| round one's **`sit:` clause** (limit 4: *cannot create a Date*) | a writ convenes nothing. `convene` is the only writer of `(Date, due_at)` and stays so |
| round one's **`draw: None` starvation** (limit 5) | there is no founding-policy inventory, because **there is no policy object the larder reads.** `04`'s `nearest_store` feeds the world |
| round one's **`reach: all`** | §A.18 row 1 |
| round one's **`ttl` lapse** | §A.16 — `AX-5` says three motions |
| round one's **same-`(rung, clause)` collision** (limit 9) and **RR-1** | §A.4 — two writs are two claims in one ledger, and `agreement` already pairs them |
| round one's **`ceiling = matured/declared`** (limit 7) | no per-stage claim is made anywhere here |
| a **`dispensation` operand** in the closed roster | §A.13 — **nothing needs one** |
| `comply` / `evade / defy` / `refract` — **three rows, none resolvable, measured** | §C.6 RR-A |
| `dispatch` and `remit_acts.dispatch` | §A.6.1 — `issue` with a person `to`, per `ED-IN-0210` |
| `w.dispensations`, `w.petitions`, and their two matrix rows | position 15 |
| `budget_office_bonus` (term + fixture) | §A.17 — a landholding, and now a bookshelf, buys scene actions |
| `levy` | §A.20 |

## §B.3 · One deletion is a PRECONDITION, not a tidy-up

**`budget_office_bonus` must go in the same commit as the deposit rule, or the deposit rule makes `H-92`
worse by a factor of 69.** `decision/budget.py:57` pays the bonus **per live `hold`**, and
`hole_register.yaml:1108` records the consequence: *"A `hold` TENURE OVER A RUNG IS READ BY TWO CONSUMERS
THAT WERE WRITTEN FOR OFFICES … so A LANDHOLDING BUYS SCENE ACTIONS."* **Measured: 69 Records held by 36
persons after one season.** Once a writ is a `hold`, **a scribe with a satchel gets more acts than a duke.**
The row's `cite` already gives the diagnosis: *"a sweep of all sixteen `t.kind == 'hold'` sites … found two
that treat every hold as an office."*

> ### **RULED: this is `CLAUDE.md` §0.1 pt 5's pattern-defect shape — *the broken code was correct when
> written and stopped working because something else changed* — and it EARNS its fix because the defective
> artifact is load-bearing on THE GAME** (a person's act budget). The fix is the narrow one: **delete the
> term and its fixture.** `04`'s build item owns the falsifier (`hole_register.yaml:176`'s planted-hold
> measurement: budget stays 5). ⚠ **No guard is built**, because a guard over *"is every hold-reader
> office-aware"* has **the readers themselves as its subject**, which pt 5's predicate excludes.

## §B.4 · Refused and deferred, each with the clause that refuses it

| refused | the clause |
|---|---|
| **a `Dispensation` dataclass** | `ARCH §B.5`'s rejected alternative, quoted at C2 |
| **an `issuer` field on `Record`** | `AX-4` — the `hold` owns it (`effects.py:286-287`) |
| **a `copy_of` link between copies** | nothing reads it, and `ARCH §B.6.1`'s rule applies: *"A stored roster drifts … a resolved one IS the edges"* |
| **a delivery / latency model** | Jordan's third ruling. §A.11 |
| **a reporting channel** | `holonic §37.3` row 4. §A.17 |
| **a compliance flag on an act** | `AX-2` and `ARCH §C.6` — motive is a per-witness Claim. §A.13 |
| **a `ttl` decrementer** | `AX-5`. §A.16 |
| **a seizure verb** | no contest provider, and `H-84`'s own rule against inventing a row to pass a case. §A.19 |
| **a `forgery_quality` reader** | a genuinely new mechanism (a contest of capability against secrecy), and not this file's. §A.15 — named as the cheapest new thing nearby |
| **a ninth operand named `dispensation`** | `rosters.yaml:1078-1079` — *"filling `H-94` by keyword argument"* |
| **an eighth `requires` stem for person↔person co-location** | `data/requires.py:1092-1094`'s closure argument; and `give` takes `release`'s precedent instead. §A.7 |
| **a per-stage `matured`** | the field is whole-record and Jordan ruled it. §A.4 |
| **a new Event carrier field for the degree** | `Event.degree` already exists (`carriers.py:98`) and is assigned at `resolve.py:150-155`. §A.10 |
| deferred: **`Act.via`** | ratified position 6 (`_part2.md:239-266`). Until it lands, `issue` resolves the seat from the actor's holds as `_eligible` does (`loop/resolve.py:52-57`). **`03` owns the interim and its retirement** |

## §B.5 · E, scored LAST and as a RATIO — and it FAILS if scored alone

`CLAUDE.md` §0.06: *"⚠ **E is never scored as an independent axis**: alone it is satisfiable by amputation,
so score it **last, as a ratio against what N and R found**. An audit that scores four axes and averages
them **rates an amputated design as elegant.**"*

**Scored alone this design is a triumph and the score is meaningless:** it deletes five verbs, two
collections, two matrix rows and a whole clause grammar, and replaces them with one verb. **That is the
amputation reading.** The ratio is the real score.

**The four E-attacks, in order, each answered or conceded.**

1. **`Record.subject_matter: Any` is a schema hole.** → **Answered** by `record_kinds` + the constructor
   refusal (§A.5). **Conceded: this is one more roster**, and it is +1 in the ledger.
2. **The `Partial` branch is a third path through `_told_content`.** → **Conceded, +1 branch.** The
   alternative — no lossy word at all — fails Jordan's first ruling. ⚠ **And the concession is smaller than
   it looks, measured:** the branch fires on **8 of 8** successful tellings, so it is not a rare path with a
   cost — **it is the common path.**
3. **`give` is +1 verb.** → **Answered:** it is ratified position 16's verb, named against `VOCABULARY.md`
   **as position 16 instructs**, and `dispatch` (−1) folds into `issue`. **Net 0 on rows.**
4. **Two effect bodies where one would do — `issue` and `petition` both delegating to
   `_eff_create_record`.** → ⚠ **CONCEDED AND DELETED IN AUTHORING.** §B.5's own rule is that the design
   fails E if the author cannot delete two of the conceded four, so I take this one: **`issue` and
   `petition` are REGISTRATIONS of ONE shared body** (§A.6), not two bodies. **One function, three
   registrations**, and the ledger reports **both numbers** (§B.1).

**The ratio.** Of my **8** additions (by function), N found **6** necessary by a named cut (§C.4's
N-lines): the kind, the schema as one roster, `give`, the deposit rule, the `commit` body, the loss
function. **2 are overhead I concede and do not delete**: `record_kinds` as a separate table rather than a
column on the verb table, and `_req_give` existing at all rather than being typed. **6/8.**

> ### **RULED: E passes as a ratio and would FAIL scored alone. The design's elegance is that FOUR edits
> reach EIGHTEEN steps (§A.21) — not that it deletes more than it adds, which is what amputation looks like
> from the inside.**

---

# PART C · THE THREE QUESTIONS

## §C.1 · WHO OWNS THIS? — one owner per value (`AX-4`)

| value | the one owner | the one writer |
|---|---|---|
| a writ's **identity** | `Record.id` | the document body, at creation, **once** |
| a writ's **content** | `Record.subject_matter` | the same call, **once**. **No matrix row exists that would let anything write it again** (§A.4) |
| a writ's **issuer** | the **first `hold`**, and the `record.created` Event's `causes[]` | `add_tenure` — `holonic §15.1`, *"Every Tenure is owned by its SUBJECT"* |
| a writ's **current holder** | the live `hold` Tenure | the document body (mint), `_eff_give` (pass), `_eff_destroy_record` (cascade) |
| a writ's **place** | **nothing stores it.** `place_of` derives it from the holder (`01`) | — |
| a writ's **schema** | `rosters.yaml: record_kinds` | a data edit; `Record.__post_init__` reads it |
| **what a person believes a writ says** | that person's `Claim`, in their own ledger | WITNESS — the deposit rule (`firsthand`) or the told channel (`told_by`) |
| the **loss band** | `fixtures.told_drift_band` | a fixture edit, swept |
| **which** addressee or number is lost | **nothing stores it** — derived from `H(seed, tick, pid, purpose)` (§A.10.4) | — |
| **whether a writ was obeyed** | **nobody.** It is an inference from Events, per witness (§A.13) | — |

⚠ **One value has two homes today and the second is DELETED, not reconciled:** `w.dispensations`
(`state/world.py:165`) and the `Record` store. Position 15's fold removes the first.
⚠ **And one I state as unowned rather than assigning:** `Record.rung` for a **held** Record is meaningless
(§A.4), and **69 of 69 carry a person id.** The field's real owner is `place_of`'s fallback, and **`01` owns
that Query.**

## §C.2 · WHAT CAN CHECK THIS? — `STRUCTURAL | MECHANICAL | CONVENTION`

**STRUCTURAL** = impossible to spell. **MECHANICAL** = a test or a constructor refuses it. **CONVENTION** =
a person must notice. Per `CLAUDE.md` §8 and `state/ids.py:5-7`: *a false claim of enforcement is worse than
none, because it stops the next reader from checking.*

| the property | grade | the check |
|---|---|---|
| a writ's content cannot be rewritten after issuance | **STRUCTURAL** | there is **no matrix row** for `subject_matter`, and `World.write` **requires** `record_kind`/`fieldname` (`state/world.py:183-184`). A write with no row is refused by the gate's own contract |
| the terms' OUGHT cannot be mutated | **STRUCTURAL** | `Proposition` is `@dataclass(frozen=True)` (`carriers.py:467`) |
| `subject_matter`'s keys match its kind | **MECHANICAL** | `Record.__post_init__`, **both directions** (§A.5) |
| `kind` is a rostered member | **MECHANICAL** | the same constructor |
| **no MATTER-class write is a function of a document's content** | **MECHANICAL** | `WW-11` — grep the barrier for `subject_matter`, assert 0. **The string is unique to the field**, so the assertion can observe the failure |
| scope enumerates executors, not places | **MECHANICAL** | `probes.py:1148-1160`, re-aimed at the Record (`WW-5`) |
| the teller's ledger is unchanged by a lossy telling | **MECHANICAL** | `WW-10`, on a `deepcopy` before and after |
| the lossy copy never adds an id and never empties `to` | **MECHANICAL** | `WW-9` |
| `give` closes the giver's hold | **MECHANICAL** | `WW-6` |
| a `Record` has at most **one** holder | ⚠ **CONVENTION** | `holonic §15` says 1 per object; **`add_tenure` does not check it** (§A.16). **Said plainly** |
| **delivery is not assumed** — *never received* ≠ *received and refused* | ⚠ **CONVENTION** | the three states are structurally distinct (§A.18 row 4), but **nothing stops a later session adding a convenience channel.** The one of §37.3's four that is not self-enforcing; `WW-8` is aimed at it |
| a forgery is indistinguishable from a genuine writ in a ledger | ⚠ **STRUCTURAL TODAY, AND FOR THE WRONG REASON** | it is indistinguishable because **nothing reads `forgery_quality`** (§A.15). **That is an absence, not a design property**, and it stops being STRUCTURAL the moment a reader exists |
| `RR-P`'s no-bridge prohibition | ⚠ **CONVENTION** | and this is why it is an **axiom request**: `ARCH F.13` records the same shape for the act store — *"The guard is a scan, and it is CONVENTION"* |

## §C.3 · WHOSE ACT MAKES IT HAPPEN? — every mechanism as execution

`CLAUDE.md` §0.2: *done means it runs*, and `AX-1`: *only a person acts*. §A.21 is the full answer; this is
its index, with the things that are **nobody's act** marked as such.

| mechanism | whose act |
|---|---|
| a writ exists | the issuer's **`issue`** |
| its terms exist | somebody's **`utter`** |
| it moves | a carrier's **`move`**, then somebody's **`give`** |
| it is believed | ⚠ **nobody's act** — WITNESS, a barrier |
| its terms are known second-hand | a teller's **`tell`** |
| its terms drift | ⚠ **nobody's act** — WITNESS, at the band the contest returned |
| it matures | ⚠ **nobody's act** — MATTER, and **only while a living person holds it** |
| it is obeyed | the executor's **`transfer` / `commit` / `work`** |
| it is disobeyed | ⚠ **no act at all**, and that is the point |
| it is forged | a forger's **`forge`** |
| it is burned | somebody's **`destroy_record`** |
| it is forgotten | ⚠ **nobody's act** — MATTER's claim decay, `AX-5`'s third motion |

> **Three barriers and no fourth**, and each is one of `AX-5`'s licensed motions or a join that writes only
> **beliefs**. **Nothing in this design is done by the engine on the world's behalf.**

## §C.4 · THE LOOPS, NAMED AND SIGNED (`ID-16`)

*"A model in which every loop is negative CONVERGES — season 40 resembles season 30 — and convergence is not
a design goal, it is what happens when a design has no other ideas."*

| # | name | the cycle | sign | damping |
|---|---|---|---|---|
| **WW-L+1** | **THE PAPER TRAIL** | a writ is held → the deposit rule makes its holder believe → he acts → the act emits → `document_key` reaches other holders → more claims about more documents | **+** | every step is an act out of ~5 · confidence decays at MATTER · **a Record can be burned** |
| **WW-L+2** | **RUMOUR** | a telling deposits → the hearer now holds a claim → `tell`'s `own_ledger` precondition is satisfied → he can tell it on | **+** | ⚠ the exact-triple guard suppressed **175 of 180** deposits, measured; **8 tellings → 1 claim** in the populated season. **This loop is damped almost to zero today, and that is a FINDING rather than a comfort** |
| **WW-L+3** | **DRIFT COMPOUNDS** | a `Partial` telling drifts a number → the hearer's onward telling passes **his** value → drift accumulates across hops | **+** | ⚠ **the loop Jordan's first ruling constrains.** Damping: **one number per hop**, bounded by the band, never sign-crossing; **and the writ is always there to be travelled to.** §A.10 exists to bound this loop, not to permit it |
| **WW-L+4** | **CUSTODY CONCENTRATES** | a man who holds documents is believed about them → he is given more → he holds more | **+** | `give` is somebody else's act, **and `budget_office_bonus` is deleted** (§B.3), so holding more buys nothing |
| **WW-L−1** | **THE COST OF REACH** | binding ten men costs ten documents and ten acts out of ~5 → fewer acts for anything else | **−** | the budget is fixed. **The total IS the damping** |
| **WW-L−2** | **SILENCE** | nobody acts on a writ → nothing is emitted → `document_key` never fires → the issuer learns nothing → he cannot direct the next writ | **−** | **converges on ignorance**, and the exit is an act: travel, or send somebody |
| **WW-L−3** | **FADING** | a claim's confidence decays → `LedgerReader.latest_about` prefers the recent and the confident → an old writ's terms stop being what anybody acts on | **−** | the rate is a fixture. ⚠ **And re-reading the Record restores nothing** — the deposit fires on a hold CHANGING, not on a re-read. **A named consequence: there is no way to refresh a belief about a document you already hold.** Stated as a limit |
| **WW-L−4** | **BURNING** | the document is destroyed → the claims survive → nobody can prove → fewer acts are taken on it | **−** | **terminal by construction**: a Record is destroyed once |

**Four positive, four negative — and the one to watch is WW-L+3.** Drift compounding across hops is the
exact failure Jordan's first ruling names, and **§A.10's clauses are its damping, stated as clauses rather
than as a hope**: one number, one addressee, never the last, never an id substitution, never an addition,
and the document always reachable.

⚠ **`ID-16`'s derived check is blocked** on the `requires` grammar being typed
(`engine/season/hole_register.yaml:1444` — *"one half of the cycle graph is data and the other is
English"*), **so this table is an authored claim, not a falsifiable one, and says so.**

## §C.5 · THE GRADE, AND WHAT WOULD MOVE IT

**`paper`.** `CLAUDE.md` §0.2: *done means it runs.* **Nothing in this file executes.** The four things that
would move it, in dependency order, each with its artifact **and its control**:

1. **`@effect_for("commit")`** — the smallest artifact in the suite, and the one `AUDIT_VERDICT` named:
   *"The whole difference is one artifact."* **Falsifier:** a seeded season where a person holding a
   `content:` claim naming a Proposition commits, and `Tenure.since` is set. **Control:** same seed, body
   absent, **no Tenure.** **Artifact:** the test plus a `headless.py` run's tenure count.
2. **`record_kinds` + the constructor refusal + the shared document body.** **Falsifier:** `issue` mints a
   Record whose `subject_matter` keys are **exactly** `[terms, to, at]`, and **a wrong key raises, in either
   direction.** **Control:** `create_record` with no kind still mints `text` with an empty value —
   **69 of 69 today, so the control IS the current world** and the migration is observably a no-op.
3. **`give` + `_req_give` + the deposit rule.** **Falsifier:** A gives R to co-located B; A's hold closed,
   B's open, B's ledger gains `content:dispensation` with **A's exact value**; B `move`s and `place_of(R)`
   follows. **Control:** a non-co-located `give` **refused**. **Artifact:** a three-season trace —
   issue → carry → give → claim.
4. **The `Partial` loss function.** **Falsifier:** at `Success` the hearer's value equals the teller's; at
   `Partial` it differs by **exactly one** omitted addressee **or** one drifted operand within the band;
   **the teller's ledger is byte-identical before and after** (RR-P's test as an assertion). **Artifact:**
   the test — and **it runs on the 8-of-8 tellings the populated season already produces**, so it needs no
   fixture world.

**The terminal artifact** is `python -m engine.season.harness.register --requirements` moving **R-04** off
`not_met`, whose `measured:` line reads *"the loop runs at person, settlement and realm only"* and
*"**The strategic layer has no expression in this model**"*. **Only a run may change that sentence.**

⚠ **Declared re-records.** Item 2 changes **no hash** (the `text` default is unchanged). **Items 1, 3 and 4
MOVE hashes** — item 1 mints Tenures, item 3 mints Tenures and claims, item 4 changes claim values in
**8 of 8** tellings. **Every golden through DELIBERATE, RESOLVE and WITNESS re-records**, and `CLAUDE.md`
§7 requires saying so: *"nothing verifies a golden re-pin was intended — so say plainly when you re-record
one."*

⚠ **And four limits that NO build item closes**, named so nobody reads them as scheduled: **seizure**
(§A.19, needs a contest provider) · **a `forgery_quality` reader** (§A.15, a genuinely new mechanism) ·
**refreshing a belief about a document you still hold** (WW-L−3) · **`ARCH F.18`, upkeep's source** —
untouched, still open, and **this file does not pretend the writ pays for anything.**

## §C.6 · RULING REQUESTS — two, each through `CLAUDE.md` §0's five-step gate

`CLAUDE.md` §0: *"`needs_jordan` means 'Jordan is the only person who can answer this', not 'nobody got
around to it'."* Every candidate was run **Superseded → Irrelevant → Design doc → Precedent → Architecture**,
and **the step that answered it is named.**

### RR-P · **the principle, as a candidate `AX-7`** · `needs_jordan: true`

| gate | outcome |
|---|---|
| 1 · superseded | **no.** Nothing supersedes a principle Jordan stated today |
| 2 · irrelevant | **no.** Its subject is every subsystem |
| 3 · a design document | **no.** `AX` carries six axioms and none says this. `AX-2` is about access to truth, `AX-3` about truth vs. right, `AX-4` about ownership — **none is about the integrity of a declared act** |
| 4 · precedent | **partial, and I record the part.** `ARCH F.10` decides receiver-side distortion, which answers **this file's** `tell` branch **without** the axiom; `ARCH §B.2`'s `F8` carve-out decides which ledger the fold may read. **Neither generalises**, and the general claim is what is being asked |
| 5 · architecture | **cannot take it.** Adding an axiom **amends ratified Layer 1** — including `AX:66`, *"**There are SIX.**"* — and gate 5 may not overwrite ratified canon |

**What is asked:** adopt *"the act is inviolate; the reception is not"* as **`AX-7`**, with the test
*a draw may decide what HAPPENS; it may never decide what you MEANT*, the three boundaries of §A.1.2, and
the `Act`/`Claim` split as its home. **What it would bind:** every subsystem, the port, and every future
resolution mechanism. **The cost, stated:** §A.1.6's table — four mechanisms read and judged clean,
**the port and the three retained subsystems UNCHECKED** — plus the `AX:66` amendment. **What is NOT
asked:** that anything in this file be blocked on it.

### RR-A · **fold the response verbs** · `needs_jordan: true`

**What is asked:** delete `comply`, `evade / defy`, `refract` and `dispatch` as verb rows, and
`remit_acts.dispatch` as a roster member.

| gate | outcome |
|---|---|
| 1 · superseded | **no.** Nothing supersedes `ED-IN-0210` |
| 2 · irrelevant | **no.** The rows are live data the loader reads |
| 3 · a design document | **no**, and worse than no: `holonic §37.1` says a dispensation *"lands as a compliance contest"*, and §A.18 row 2 records that this design **narrows** that to a question |
| 4 · precedent | **no.** No precedent deletes a row a ruling affirmed |
| 5 · architecture | **may not take it.** Gate 5 cannot overwrite a ruling, and `ED-IN-0210` (`registers/editorial_ledger_in.jsonl:104`, **RULED by Jordan 2026-09-15**) says: *"AN ORDER CARRIES TERMS LIKE A DISPENSATION, and `comply`/`evade`/`refract` answer both. The second option (no response verb) is REJECTED."* |

⚠ **THE COUNTER-ARGUMENT FIRST, BECAUSE IT IS STRONG.** Jordan was asked an either/or and chose the arm
that **keeps** the response verbs. Deleting them is the rejected arm arriving by a different route — **and a
session that has just designed a mechanism which makes three rows unnecessary ALWAYS believes those rows are
unnecessary.** That is exactly the bias the ruling defends against.

**The argument, which I believe answers it.** The ruling has two halves. **Half one — *an order carries
terms like a dispensation* — this design implements LITERALLY**: `dispatch` becomes `issue` with a person
`to`, which is the ruling's own next sentence. **Half two — *the response is a verb* — this design also
keeps**, and the verbs are `commit`, `repudiate`, `release`, `transfer` and `work`. **What it rejects is that
the response is a verb with no other job.** Three measured facts:

1. **None of the three is resolvable, measured**, and the reason is structural rather than a gap:
   `rosters.yaml:1074-1079` says `comply` cannot be typed because *"the entity is a DISPENSATION, and
   `requires_operands` is closed … with no name for one"*, and coining one *"would be filling `H-94` by
   keyword argument, which is the ruling `H-94` is waiting for."* **So keeping the rows requires a SECOND
   ruling to make them work.**
2. **`refract` is graded `absent`** with *"emitter- or receiver-side is absent, D18"*, and **`ARCH F.10` has
   since answered it receiver-side** — where distortion is a WITNESS deposit, **not a verb an actor forms.**
   A receiver-side `refract` is **a verb whose effect is to change one's own mind on purpose**, which is
   `AX-3`'s collision wearing a verb row.
3. **`dispatch` is resolvable and person-side unformable** (`remit:dispatch` declines, `H-71`), writes
   nothing, and emits `order.given` — **0 times, measured.**

**And the fork the ruling's earlier row raised is answered the same way.** `ED-IN-0210`'s original question
— *"are `dispatch` and `comply` two sides of one thing?"* — is **yes**: `tell`/`give` on one side,
`commit`/`repudiate`/the act itself on the other. ⚠ **I record a tension rather than picking the reading that
suits me:** an intermediate row (`editorial_ledger_in.jsonl:87`, 2026-09-13) recorded that fork as answered
by `ED-IN-0219` with *"NO, they are one producer and one member of the response triad, and the genuinely
two-sided pair is **dispatch/issue**"*, and Jordan's 2026-09-15 row then superseded the whole row. **The
`dispatch`/`issue` pairing that row names is exactly what §A.6.1 implements.** What **neither** row says is
whether the response **rows** survive the fold, **and that is the only thing being asked.**

**If Jordan declines RR-A**, this design still works: the three rows stay, unresolvable, as they are today,
and the writ mechanism is untouched. **RR-A is a cleanup that needs permission, not a dependency** — which
is why `05`'s build item for it is last and gated.

### Closed rather than escalated, with the gate that closed each

| candidate | gate | the closure |
|---|---|---|
| **RR-1** — does a nearer rung's clause or a higher rank win a policy collision? | **2, irrelevant** | there is no `in_force` walk and no place-keyed clause. Two writs naming one executor are two claims in one ledger; `agreement` (`options.py:412`) scores them and **his act resolves it.** §A.4 |
| `levy`'s deletion — is it a seventh remit act? | **5** | a state write at a place with no contest is `holonic §37.3` row 2. §A.20 |
| which side distortion sits on | **3** | `ARCH F.10`: receiver-side. §A.1.5 |
| where the `subject_matter` refusal lives | **4** | `Office.__post_init__`, the precedent `state/world.py:240-241` names. §A.5 |
| `give`'s typed vs. prose precondition | **4** | `release`/`revoke`'s route, `verb_table.yaml:431`. §A.7 |
| the verb's **name** | **4** | `VOCABULARY.md` has no row; `CLAUDE.md` §4's *idiomatic in choosing*. §A.7 |
| does a writ lapse on a clock? | **5** | `AX-5` says three motions. §A.16 |
| may `Record.subject_matter` be amended? | **5** | there is no matrix row, and **adding one is the visible place to ask.** §A.4 |
| is compliance a distinguishable act? | **3** | `AX-2` + `ARCH §C.6` — attribution is a per-witness Claim. §A.13 |
| how does the lossy branch get a degree? | **4** | `Event.degree` exists and is assigned (`resolve.py:150-155`). §A.10 |
| **H-84** | closed **by design** | `give`. §A.7 |
| **H-92** | closed **on both consumers** | `budget_office_bonus` deleted; `document_key` reading `changes[]` **is** the deposit rule's own channel. §B.3, §A.9 |
| **`ARCH F.15`** | closed **by design** | the schema. §A.3 |
| **`ARCH F.10`** | **already closed**; cited, not claimed | receiver-side |
| **not closed, and said so** | — | `ARCH F.18` (upkeep) · **seizure** · a `forgery_quality` reader · belief refresh (WW-L−3) · `Act.via` (position 6) · `H-94`/`H-80`'s operand famine · the `Record.rung` person-id defect · `ED-SE-0051` (RR-2, untouched) · `RR-3` (survives as `03` states it) |

⚠ **RR-B** — the RATIFIED `architecture/` sentences this suite makes false, including `ARCH §B.5`'s
*"remain unspecified"* and `ARCH §C.6`'s mint table — **is `05`'s, not mine.** I quote both at their `§`
(§A.3, §A.9) and **edit neither.** ⚠ **RR-C** (sequencing against the ratified program's order) is also
`05`'s; my §C.8 flags the Arc-2 items and does not argue the departure.

## §C.7 · THE FOUR STANDING REQUIREMENTS, TICKED ONE BY ONE

| Jordan's requirement | how this file meets it, or does not |
|---|---|
| **a governing player must explicitly set policies** | ✅ §A.22's twelve decisions, each a named act. ⚠ **Nine of twelve reachable by a computed act; three need declared operands** |
| **players need an interface** | ✅ **`03_THE_SURFACE.md` STANDS**, and this file hands it three readings rather than a new surface: **HELD / STALE / UNHELD** (§A.17). ⚠ Round one's compliance table is **struck**; `03` carries the strike. **I add no surface** |
| **a policy changes how a governed rung FUNCTIONS, not what a die shows** | ✅ **and more strongly than round one.** Nothing this file adds touches a roll. A writ changes **who is asked what**, which changes **which acts are formed**, which changes the world. **There is no modifier anywhere in this design** |
| **policies impact emergence** — *"a provincial policy on farming taxation may end up impacting a hearth"* | ⚠ **PARTIAL, and the missing half is `04`'s.** This file delivers the top of the chain — the Duke's writ, the reeve's belief, the reeve's `transfer` out of the settlement's stores. **The hearth feels it only if a hearth eats from those stores**, which is `04`'s `nearest_store` walk and its body write. **Neither half is a game on its own, and I do not claim the hearth** |

## §C.8 · THE ENGINE CHANGES, PER FILE, WITH ARC-2 FLAGS

Per-file detail is `05`'s; this is **my file's share**, so `05`'s table has a source. **Arc-2 flag** =
downstream of the Arc-2 gate (ratified positions 3–7) iff the item adds an `@effect_for` body or a Tenure
write whose subject is not the actor. **By the literal rule every effect body is flagged**; the argument for
building ahead is `05`'s **RR-C**, and each flagged item's artifact re-runs after G4.

| file | today | becomes | Arc-2 |
|---|---|---|---|
| `engine/season/rosters.yaml` | `remit_acts` (6, with `dispatch`) `:111-119` · no `record_kinds` | `remit_acts` minus `dispatch` · **NEW `record_kinds`** in the TABLES block beside `site_kinds` `:805` · **NEW `fixtures.told_drift_band`** | no |
| `engine/season/verb_table.yaml` | **38 rows, measured** · `issue` `:256` writes `Dispensation.exists` · `comply` `:130` · `evade / defy` `:220` · `refract` `:406` · `dispatch` `:197` · `levy` `:348` · `petition` `:395` writes `Petition.exists` | `issue`/`petition` re-keyed to `Record.exists`; `issue` gains `commit`'s typed cell · **NEW `give`** · `levy` deleted now · four rows deleted under RR-A → **38 → 34 → 35** | no |
| `engine/season/write_matrix.yaml` | **40 rows** · `(Dispensation, exists)` `:112-118` · `(Petition, exists)` `:224-230` | both deleted → **38**. ⚠ **No `(Record, subject_matter)` row is added** (§A.4), and the header's own stale counts `:47-54` get re-measured | no |
| `engine/season/state/carriers.py` | `Record` `:422-445`, **no `__post_init__`** | `__post_init__` validating `kind` and `subject_matter` keys | no |
| `engine/season/state/world.py` | `petitions` `:164`, `dispensations` `:165` | both deleted. ⚠ **`harness/invariants.py:70-72` must lose them in the SAME commit**, and `test_the_entity_set_covers_every_world_collection_a_tenure_can_name` pins that set to `World.__init__` — **so the deletion is checked** | no |
| `engine/season/loop/effects.py` | **11 bodies, measured** · `_eff_create_record` `:263-290` | **the shared document body** (registered for `create_record`, `issue`, `petition`) · **NEW `_eff_give`** on `_eff_confer`'s shape `:118-126` · **NEW `_eff_commit`** | **YES** |
| `engine/season/loop/predicates.py` | `REQUIRES_PREDICATES` = **5, measured** · `_req_dispatch` `:290-294` | **NEW `_req_give`** (sixth) · `_req_dispatch` deleted under RR-A | no |
| `engine/season/loop/witness.py` | `_told_content` `:31-70` verbatim · the told deposit `:315-369`, **degree-blind** | `_told_content` takes the Event's degree and returns a **lossy copy at `Partial`** · **NEW deposit branch** for a hold-on-Record in `changes[]`, beside the observation deposit `:270-279` | **YES** (a deposit, not a Tenure — flagged under the literal rule, argued cheap) |
| `engine/season/epistemic.py` | `_ch_document_key` `:260-333` · `_event_place` `:215-241` | ⚠ **untouched by me.** The deposit rule reads `changes[]` through the same primitive; **`place_of`'s promotion is `01`'s** | no |
| `engine/season/decision/options.py` | `_derive_operand` `:259-323` | **one branch family** reading `to`/`at`/`kind`/`amount` off a `content:` claim's value when the question's referent is one. **`from` UNCHANGED at `:316-317`** | no |
| `engine/season/decision/budget.py` · `data/fixtures.py` | `:57` pays `budget_office_bonus` per live hold · the fixture at `:430` | **term and fixture deleted** (§B.3) | no |
| `engine/season/harness/probes.py` | `f5` `:1148-1160`, `f18` `:1442-1452` build `w.dispensations`/`w.petitions` by hand | re-aimed at `Record`s. **`f5`'s assertion does not change** — which is the test that the fold preserved the ratified property | no |
| `architecture/` | `ARCH §B.5`, `§C.6`, `F.10`, `F.15` | ⚖ **RR-B, `05`'s. Quoted at their `§`. NOT EDITED** | — |

---

# PART D · FALSIFIERS

`ID-11` — ship the falsifier with the claim. `CLAUDE.md` §0.1 pt 2 — **an assertion must be able to observe
the failure it excludes.** Every row names what would be true if the claim were false, and says what it
asserts on.

| # | the claim | the falsifier, and what it can observe |
|---|---|---|
| **WW-1** | the writ's carrier already runs | run one populated season and count `record.created`. **If it is 0, this file's whole N-argument is wrong.** Measured **69**. *Control:* `build_realm(0)` alone → **0** — which is why the clock must be stated with the number |
| **WW-2** | `record_kinds` is a **no-op migration** on the running world | the same season after the constructor check lands: **69 Records, all `text`, all `subject_matter == None`, no raise.** A raise means the `text: []` schema is wrong. **Observes the failure because `set(None or ()) == set()` is the exact line under test** |
| **WW-3** | `issue` mints a writ with **exactly** its kind's keys | a declared `issue` naming `{terms, to, at}` mints one; one naming `{terms, to}` **RAISES**; one naming `{terms, to, at, reach}` **RAISES**. ⚠ **Both directions asserted** — a one-way check cannot see an extra key, and an extra key is a second vocabulary |
| **WW-4** | a writ's content cannot be rewritten | attempt `w.write("subject_matter", …, record_kind="Record", fieldname="subject_matter")` and assert the gate refuses **for want of a row**. **If it succeeds, §A.4's STRUCTURAL grade is false and drops to CONVENTION** |
| **WW-5** | scope enumerates **executors**, not places | `probes.py:1148-1160` re-aimed at a `Record`: `off.rung is None`, and the ids in `subject_matter["to"]` are **outside** `descendants(w, "S")`. **The assertion text does not change** — if it must change, the fold lost the property |
| **WW-6** | `give` moves custody and **nothing else** | A gives R to co-located B: A's hold `until == tick`, B's hold live, **`w.records[R]` byte-identical before and after** (compare a `deepcopy`). *Control:* a non-co-located `give` → `give.refused`, **and both holds unchanged** |
| **WW-7** | the deposit rule fires on the **hold**, not on the kind | after the `give`, B's ledger holds `content:dispensation` with **A's exact value**; and a `create_record kind: text` deposits `content:text` with `{}`. **The second is the control that says the branch is keyed on the hold** |
| **WW-8** | **delivery is not assumed** — the three states are distinct | three worlds, same seed: (a) never delivered, (b) delivered and no act, (c) delivered and complied. Assert **the issuer's ledger is IDENTICAL in (a) and (b)** and **differs in (c)**. ⚠ **This is §37.3 row 4's only mechanical check, and it is the one a later convenience channel would break** |
| **WW-9** | the `Partial` loss function is **bounded** | at `Partial`, the hearer's value differs from the teller's by **exactly one** omitted `to` id **or** one operand within `ceil(band × \|before\|)`; **`to` is never empty**, **never gains an id**, **never loses `p.id` when `p.id ∈ to`**; `terms`/`at`/`subject`/`predicate` are **equal**; **no sign change**. ⚠ **And it asserts on the three measured `news.untold` events at non-`Failure` degrees (§A.10.5) — that NO loss was applied to them**, which is the assertion that observes a degree-only guard |
| **WW-10** | the teller's ledger is **untouched** | `deepcopy` the teller's ledger before WITNESS and assert equality after. **RR-P's test as an assertion**, and it fails loudly if any future optimisation shares a `Claim` object between ledgers |
| **WW-11** | **no MATTER-class write is a function of a document's content** | assert `'subject_matter' not in open('engine/season/loop/matter.py').read()`. **The string is unique to the field**, so the assertion observes exactly the failure it excludes. *Control:* the same search for `stages` → **present**, which is the read that IS lawful |
| **WW-12** | the two `forge` declarations **disagree** | assert that `(Record, forgery_quality)`'s `emits` (`record.forged`) **appears on some verb's `emits:`** — **it does not today, so the test is RED on arrival.** ⚠ A test that PASSES here would mean I misread one of the two rows |
| **WW-13** | `give` is **resolvable** once its body and predicate land | `'give' in resolvable_verbs()`. *Control:* remove `_eff_give` → **False**, because the second gate reads `EFFECTS`. **This is the falsifier for "the verb executes", not for "the row exists"** |
| **WW-14** | the Duke learns **only** by the three routes | in WW-8's world (c), assert no claim about the transfer reaches the issuer with `source == "inferred"`, and **no claim reaches an issuer who holds no store on the path.** *Control:* `inferred` is **0 today, measured** — so a non-zero is the observable |
| **WW-15** | the writ's clock **follows custody** | a writ with a stage due at `t+2`, given away at `t+1`: **`matured` is set and `causes[]` chains to the giving.** The same writ whose holder is killed → **not matured**, and the TRACE note fires (`matter.py:76-77`) |
| **WW-16** | deleting the two `World` collections is **checked** | delete them and run `test_the_entity_set_covers_every_world_collection_a_tenure_can_name`: it **fails until `harness/invariants.py:70-72` drops them.** **The falsifier already exists in the tree and I did not write it** |
| **WW-17** | a writ **does not lapse** on a clock | run ten seasons with a writ whose `ttl` is 1: **`ttl` is unchanged and `record.expired` is never emitted.** *Control:* the holder's claim confidence **does** fall, and `claim.decayed` fires — **so the falsifier distinguishes "nothing fades" from "the right thing fades"** (§A.16) |

⚠ **Two claims in this file have NO falsifier, and I name them rather than leaving the list looking
complete.** (a) **`RR-P`'s no-bridge prohibition** — its check is CONVENTION (§C.2), and `ARCH F.13` records
the same limitation for the act store: *"The guard is a scan, and it is CONVENTION."* (b) **§C.4's loop
table** — `ID-16`'s derived check is blocked on the `requires` grammar, so **the signs are authored.**
**A falsifier I cannot write is worth more said than implied.**

⚠ **And none of the seventeen is licensed as a tree-wide GUARD.** `CLAUDE.md` §0.1 pt 5's predicate: a
pattern defect earns a guard only if the defective artifact is load-bearing on **the game** or on **a Jordan
decision.** WW-11 and WW-9 qualify (their subject is the engine's own behaviour); **WW-12 is a report, not a
guard**, and **WW-1's numbers are measurements, not a gate.** Nothing here proposes a checker whose subject
is another checker.

---

# APPENDIX · CITATION REPAIRS

`CLAUDE.md` §0.1 pt 3: *"A citation you have not opened is not a citation."* Every `path:line` above was
opened in this session. Below are the citations and claims **I inherited from my own specification** that
were **wrong** — corrected in the text and recorded here so the error is not re-imported. Round one's
unification pass took ~24 repairs and found three false verifications inside its own *"opened and found
CORRECT"* list; **these are mine, and four of them are the same shape.**

## The claims that were wrong on the merits — each verified the wrong half of itself

| I was told | actually | how the error was made | consequence if uncorrected |
|---|---|---|---|
| *"`matter.py` touches no Record or Proposition — true today at `:30-296` and stays true"* | ⚠ **FALSE of Record.** `loop/matter.py:65-74` iterates `sorted(w.records)`, reads `rec.stages` and reads the live `hold`; `:106-109` writes `matured`. **TRUE of Proposition** (`grep` → no match) | the **Proposition** half was checked and the **Record** half was assumed from it | a session would ship *"MATTER reads no Record"* as an invariant and a test would go red on arrival. **The true invariant is narrower and stronger: no MATTER write is a function of a document's CONTENT** (§A.14, `WW-11`) |
| *"`forgery_quality` is declared and **written by `forge`** … a shipped producer awaiting a consumer"* | ⚠ **the producer is not shipped.** `forge` has **no `@effect_for`** and **is not resolvable** (measured). The write exists as a table cell and a matrix row only | the verb row's `writes:` cell was read as **the behaviour** — §0.1 pt 3's *"X works today"* row, checked at the declaration instead of the call site | a build plan would schedule *"add a reader"* as the whole job when **both halves are missing** (§A.15) |
| *"`dispatch` is `give` of a writ naming the dispatched"* | ⚠ **`ED-IN-0210`'s ruling says `dispatch` is `issue` with a person-scale referent** (`editorial_ledger_in.jsonl:104`). **Minting and handing are different acts** | the ruling was **paraphrased rather than opened** | the fold would be built on the paraphrase and would **not implement the ruling** (§A.6.1) |
| *"0 records"* (`AUDIT_VERDICT.md`'s measurement block) | ⚠ **0 at `build_realm(0)`; 69 after ONE season.** Both reproduced this session | **a build-time count published without its clock** | **the exact inversion of this file's main argument** — a session would conclude the Record family is unreachable from a person's decision (§0.2) |
| *"`band_floors.body` is a SITE kind … the proposal must not conflate them"* | ⚠ **the roster says the opposite.** `rosters.yaml:814-815`: *"`body` IS NOT A SITE. It is `(Person, body)`'s band row, here because `band_floors` keys on THIS roster."* | a caution inherited from a reading of the roster's **`values:`** line without its **`note:`** | **`04`'s subject, not mine** — recorded here because I opened it while checking a neighbour, and a session inheriting the caution would build a second band scheme that `H-38` forbids |
| *"`Record.matured` is whole-record, not per-stage"* (`AUDIT_VERDICT` limit 7) | ✅ **CORRECT** — `carriers.py:445`, with Jordan's 2026-09-10 ruling transcribed at `:432-444` | — | **recorded as a verification that HELD**, because §0.1 pt 3 makes an unverified pass as suspect as an unverified fail |
| *"the told channel deposits at the teller's confidence"* | ✅ **CORRECT** — `witness.py:363`, with the reason at `:304-310` | — | as above |
| *"`_eff_create_record` mints the maker's hold at `:288-289`"* | ✅ **CORRECT**, and the **Record write is `:284-285`** — a different pair of lines | — | a session editing `:288-289` to add a kind would edit **the tenure, not the Record** |

## The line-number and pointer repairs

| cited as | actually | consequence if uncorrected |
|---|---|---|
| `carriers.py:429` for `Record.subject_matter` | ✅ **`:429`.** `:428` is `forgery_quality`, `:430` is `ttl`, `:431` is `stages`, `:445` is `matured` | the five are one screen apart, and round one's appendix records a session confusing `:429` with `stages` |
| `witness.py:31` for `_told_content` | ✅ as the `def`; the **return** is `:70` and the deposit branch it feeds is **`:315-369`**, with `news.told`'s test at **`:316`** | **the degree guard goes at `:316`, not at `:31`** |
| `epistemic.py:260` for `_ch_document_key` | ✅ as the `def`; **the predicate is `:331-333`** and the docstring runs seventy lines | a session *"reading `changes[]` at `:260`"* is reading a docstring |
| `epistemic.py:215` for `_event_place` | ✅; the **body** is `:229-241` | — |
| `epistemic.py:343` for `_ch_post_remit` | ✅; the **remit set is built at `:353-354`** | the place-blind-broadcast argument is about those two lines |
| `verb_table.yaml:465` for `restore`'s formula | ✅ as the `effect:` line; **`:461` is `writes:`** | — |
| `rosters.yaml:250-270` for `question_sources` | ✅; **the `values:` line is `:270`** | the roster edit is one line, not twenty |
| `rosters.yaml:805` for `site_kinds` | ✅, and it is inside the **TABLES** block whose header is **`:800-803`** — so **`record_kinds` is a TABLE, not a roster**, and `roster()` **raises** on it | putting it in the rosters block would make `table()` raise at the call site |
| `rosters.yaml:1084` for `requires_operands` | ✅ — `[actor, subject, from, to, site, kind, amount, floor]`, **eight**, and **`at` is not among them** | §A.6's computed-writ limit rests on exactly this |
| `data/requires.py:488-491` for `REQUIRES_STEMS` | ✅ — **eight** stems, and the closure is enforced by **a test** (`engine/season/tests/test_season_shape.py:507-528`), **not by a load refusal** | claiming a load refusal would be the false-enforcement claim `state/ids.py:5-7` warns about |
| `holonic:536-544` for the `hold` domain | ✅ — **`:538`** is the `hold` row, and **1 per object** is on it | that cardinality is the clause deciding `give` closes the giver's hold |
| `holonic:1301-1308` for §37.3 | ✅ — the table is `:1303-1308` and §37.1's quotes are `:1286-1293` | round one cited §37.3 and honoured the wrong three quarters of §37 (§0.4) |
| `_part2.md:438` for positions 15/16 | ✅ as the heading; **position 15's instruction is `:439-443`** and **position 16's is `:452-455`** | position 16's *"name it against `VOCABULARY.md`"* is at `:452` and **is the clause I had to discharge** |
| `ARCH:1077` for F.15 | ✅ today, and **cited as `ARCH F.15`** throughout per the suite convention — its lines have drifted twice | a section pointer survives an edit; a line does not |
| `AX:1319` for `§E.1.7` | ✅; **the ruling sentence is `:1327-1330`** | — |
| `hole_register.yaml:1000` (H-84) · `:1106` (H-92) · `:795` (H-71) · `:618` (H-54) | ✅ **all four**, opened. ⚠ And round one's appendix records that **`:1102` is H-91's `unblocks:` QUOTING H-71** — a quotation cited as a source. **I did not repeat it** | — |

## And one correction I made to my own design in authoring

**§B.5 attack 4 was conceded and then DELETED rather than carried.** My specification counts `issue` and
`petition` as **two** new effect bodies. They are **two registrations of ONE function** (§A.6), and the
ledger now reports **+3 bodies by function, +5 by registration**, with **both numbers stated.** §B.5's own
rule is that the design fails E if the author cannot delete two of the four conceded overheads;
**I deleted one and kept two, and say which.**

## What this file DROPPED, said plainly rather than left as a silent gap

Per `CLAUDE.md` §0 — a skipped step is stated, not implied. **Nothing in the spec's scope for this document
was dropped**, but two things it might have been expected to carry are **deliberately elsewhere**:

- **`_ch_post_remit`'s re-basing** (the place-blind remit channel → obligees co-located, minting `inferred`).
  It belongs with the seat model's `oblige` Tenure and is **`03`'s**, not mine; I cite the defect at §A.7
  where it constrains `give`'s Event kind, and I do not specify the repair. **Measured here for whoever
  takes it: `"inferred"` has 0 occurrences as a string literal in `engine/season/**.py`, and 0 claims carry
  it in the populated world.**
- **The per-file build order with sizes and dependencies.** `05` owns it; §C.8 supplies my file's rows and
  §C.5 supplies the four artifacts in dependency order, which is what `05` needs from me.

⚠ **And the close gate.** `python -m pytest tests/valoria -q -n auto` **was not run for this document**,
because this document changes no code — it is a proposal, held back in full, and `CLAUDE.md` §0.4 makes the
suite a **shipping** gate whose unit is a commit that ships behaviour. **Said aloud rather than implied**,
per §0's requirement that a skipped step be named: **no test was run, because nothing here executes, which
is also why the grade is `paper`.**
