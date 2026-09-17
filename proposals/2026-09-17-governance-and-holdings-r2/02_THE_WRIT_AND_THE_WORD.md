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
> `holonic §37.2` (:1297-1299), quoted whole in §A.1 and never paraphrased:
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
