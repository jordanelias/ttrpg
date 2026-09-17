# The seam — where the governance suite and the behaviour layer meet

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · **`ED-IN-0243`**
## Grade under `CLAUDE.md` §0.2: **`measured`** — every row below was opened at its cited line or executed on this tree. **No design in this file has run.**
## Subjects: `../2026-09-17-governance-and-holdings-r2/` (#408) and `../2026-09-16-conviction-decision-layer/` (#409). This file judges the SEAM between them and nothing inside either.

---

## The claim, in one line

**The two suites are one machine seen from opposite ends, and the behaviour layer is blocked on the
governance suite in a way neither document states.** #408/r2 builds **what reaches a person and what
they may do** — reach, the writ, the word, seats, matter, works. #409 builds **how a person chooses
among what reached them** — the score, the terms, the bases. #409's own synthesis §3 lists five
things it needs before its function can be built, and **two of the five are r2 deliverables**: *the
medium* (the second-hand channel, r2 item 8) and *the aperture* (10 of 38 verbs unformable
person-side, r2 items 1 · 10 · 11 · 12).

That is not a scheduling observation. It is what makes #409's own falsifier runnable:

> #409 `synthesis.md` §3: `P(inversion) = 1/(1 + e^{Δ/τ})` at the shipped `τ = 0.1` — a term changes
> what a character does at 95% only when it moves the score by **Δ ≥ 0.294**. *"Every term above
> needs a declared range against that floor."*

**A term has no range over an aperture that does not open.** `serves(candidate, item)` cannot
discriminate verbs when 10 of 38 never form; susceptibility cannot calibrate on a channel that
deposits one claim a season. Build #409 first and its terms are measured against a world that
supplies them nothing to move — every one reads below the floor for a reason that is about the
world, not the term. **r2 is the precondition for #409's falsifier, not merely its predecessor.**

And the converse is the weaker half, worth stating so the dependency is not read as symmetric: r2
without #409 builds a world that delivers rich input to a chooser that ranks it with an `alignment`
table one-third full and breaks ties alphabetically. That is a defect, not a blocker.

---

## §1 · What was measured, and how

Executed on this tree, 2026-09-17, on `main` at `ddc6b21`:

| measurement | value | instrument |
|---|---|---|
| verbs resolvable | **18** of **38** table rows | `engine.season.loop.driver.resolvable_verbs()` |
| declared but unresolvable | `carry · commit · comply · determine · establish · evade / defy · exchange · forge · issue · kill / wound · levy · oblige · open_case · petition · refract · repudiate · restore · succeed · thread_read · tie / knot` | same |
| question sources | `('date_due', 'claim_landed', 'band_crossed', 'need')` | `engine.season.state.carriers.QUESTION_SOURCES` |
| #409 register rows carrying a `ruling:` | **15**, of which **0 filled** | `adjudication_register.yaml`, parsed |
| person→rung holds where `in_holdings` is True | **0**, over every person × rung pair | `build_realm(0)` + `predicates.py:99-102`, executed |
| holds at build | **35** — 19 person-subject (**all** on Offices, none on Rungs) · 16 rung-object (**all** faction-subject) | same |
| questions by source, one populated season | `claim_landed: 583` · `need: 405` · **`date_due: 0`** · **`band_crossed: 0`**, over 230 `questions_for` calls | `harness.populated`, instrumented |

⚠ **The last three rows were taken by an independent verifier, not by this file's author**, against the
r2 plan's own claims. All three CONFIRMED. The verifier also found two defects in r2's
`EXECUTION_PLAN` and one in **this file**; they are recorded at §3.6 and §7 rather than quietly fixed.

Read at the line:

| fact | where |
|---|---|
| `Question` is frozen, `{id, source, referents, about}`, `source` refused off-roster | `engine/season/state/carriers.py:242-262` |
| `Candidate` is `(verb, subject, why, operands)`; operands **never partial** | `engine/season/state/carriers.py:264-289` |
| `(Person, body)` is `steps: [MAT, RES] · class: MATTER/ACTS · social: false` | `engine/season/write_matrix.yaml:161-168` |
| the six `Person` INTERIOR rows are `[RES] ACTS` — `axis_count · beliefs · convictions · scar · stance · coherence` | `engine/season/write_matrix.yaml:147-205` |
| the `told_by` deposit constructs a Claim with **no teller field** | `engine/season/loop/witness.py:361-363` |
| r2 declares H-71 closed by a **claim** about a held document | `../2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:794` |
| #409 puts H-71 to Jordan as **three** options | `../2026-09-16-conviction-decision-layer/adjudication_register.yaml`, CAT-6 |

---

## §2 · THE CONFLICT — one, and it is a ruling collision

**H-71, at CAT-6 against r2 `03` §A.11.** The two suites answer the same hole by different routes,
and only one of them knows the other exists.

| | |
|---|---|
| **#409 CAT-6** | offers Jordan **three** arms: `1` decline (status quo, no person forms a governance verb) · `2` the grant rides on the **hold Tenure's payload** · `3` through **`sense()`** (costs a third Sensation scalar, which `S18.2` rules to exactly two) |
| **#408 r2 `03` §A.11** | *"**RULED:** the grant is a CLAIM about a HELD DOCUMENT, and H-71 closes on both sides"* — the commission `Record` minted by `confer`, answering `person_side_eligible`'s `remit:` decline **from the holder's own ledger** (`options.py:163-165`) |
| **the collision** | r2's route is **not on CAT-6's menu.** It is a fourth arm. Ruled from the register alone, Jordan chooses among three options while a fourth sits built in the sibling directory |

**This is not a disagreement about the answer — it is a defect in the question.** Both suites want the
same thing (a seated person who knows their remit, person-side, without a new Sensation scalar), and
**Nobody needs to lose.** What must not happen is CAT-6 being ruled on a stale option set.

> ⚠ **TWO CORRECTIONS TO THIS SECTION'S FIRST DRAFT, AND THE SECOND CHANGES WHAT THE MENU COSTS.**
>
> **(a)** `~~r2's arm is arm 2 relocated, and keeps AX-2 untouched the same way~~` → **the two are not
> equivalent.** Arm 2's claim is **non-violation** — *"it reaches no `World`"* (`hole_register.yaml:807`).
> Arm 4's is **conformance**: `AX-2` reads *"what they hold **may be false**"*, and `03:785-787` builds
> the revoked-man case deliberately, so a holder can believe a remit he no longer has. **Arm 4 produces
> the behaviour the axiom exists for; arm 2 satisfies its letter.** Calling them equivalent flattened
> the one difference that should decide the ruling.
>
> **(b) ARM 2'S CARRIER IS BEING DELETED BY THE SIBLING SUITE.** `(Tenure, payload)` is deletion-ledger
> row 13 in `05` — *"**No producing verb**… `ARCH §B.8` prescribes its replacement"* — and `03:744`
> files *"the grant on `Tenure.payload` | the 2026-09-16 sweep | **REFUSED — retired**"*. So choosing
> arm 2 now costs **un-deleting a field that ratified `ARCH §B.8` prescribes deleting** — an
> `RR-B`-shaped amendment, not a menu choice. **That is not a reason to refuse arm 2; it is a price
> that must be on the sheet**, and it was on neither suite's.

> **Disposition: the question is repaired, not escalated twice.** CAT-6 gains r2's route as **arm 4**,
> stated in r2's own words with its citation, and the three original arms stand. Jordan rules once,
> over four options, with the knowledge that one of them has a build item attached
> (`EXECUTION_PLAN` item 11, gated on items 5 and 10).

---

## §3 · THE FIVE FORCED ORDERINGS — same code, two suites, neither aware of the other

None of these is a contradiction. Every one of them is two edits to one object, wanted by two
documents written a day apart, where **building them separately means the second rewrites the
first's lines and invalidates the first's falsifier.**

### 3.1 · `witness.py:315-369` — the told channel

- **r2 item 8** rewrites `_told_content` to return a **lossy copy at `Partial`** (`02` §A.10, E5).
- **#409 CAT-3** needs the **teller's identity** on the deposited Claim, because the ruled
  susceptibility ladder (lord > peer > enemy) has nothing to calibrate without it. The constructor at
  `:361-363` writes `(id, holder, subject, predicate, value, when, "told_by", confidence, "own",
  round)` — **no teller**, and `Claim`'s dataclass carries no field for one, so the omission is
  structural rather than local to this call site.
  > ⚠ **`~~witness.py:358 has the teller in scope~~` → `:316`.** `:358` is prose inside a dedup
  > comment; the teller is **`_act.actor`**, in scope at `:316` (`pid != _act.actor`). A `_teller`
  > Person lookup stood at `:317-320` and was removed 2026-09-16 as never-read. **So CAT-3 is one
  > extra positional argument, not a lookup — cheaper than either suite prices it.**
- **Complementary, not competing.** One is about *what* survives the telling, the other about *who*
  told it. **Both belong in one edit**, and r2's own falsifier for item 8 (`Full` → identical;
  `Partial` → one omitted `to` or one drifted operand) is strictly stronger with the teller present.

### 3.2 · the aperture — a denominator r2 moves under #409

- **#409 CAT-6 evidence**, `[E]`: *"10 of 38 verbs are unformable person-side — every governance verb:
  `confer, convene, destroy_record, determine, dispatch, establish, issue, levy, open_case, revoke`"*.
- **r2 moves both halves of that fraction**: item 1 mints `commit` (**measured 18 → 19** resolvable),
  item 10 rewrites both eligibility predicates and seats holders, item 12 adds `found` and gives
  `restore` a body, item 13 deletes `dispatch` and three response rows.
- **So every aperture number in #409 dies on r2's execution** — including the one its own STR-4 leans
  on (*"Volume is bounded by referents; VARIETY is bounded by the gate"*). **r2 IS the gate change.**
- ⚠ **This is the row most likely to be mis-read as harmless.** It is not a stale-citation problem:
  #409's CAT-6 question and STR-4's conclusion are both *inferences from the aperture being shut*.
  Re-open it and the inferences need re-taking, not re-citing.

### 3.3 · `Question` — r2 subtracts sources where #409 asks to add fields

- **r2 item 2a** deletes `date_due` and `band_crossed` (measured at **0 questions each** after a
  populated season), adds `reach`, and reduces `occasioned_by` to one route.
- **#409 STR-4** asks whether `Question` needs a **type** dimension beyond provenance —
  *"`claim_landed` covers a threat, a gift, an insult and a rumour identically"* — and warns that
  `aggregate_questions` **re-mints** the question, so *"every new field needs its own FOLD RULE, and
  per-referent roles cannot survive the union at all."*
- **They agree in direction.** STR-4's measured finding — *"adding question sources cannot fix
  variety"* — is an independent argument **for** r2's deletion, arrived at from the other end. But
  both edit `carriers.py:242` and `queries/world_q.py::questions_for`, and STR-4's fold-rule warning
  is a live constraint on r2's `reach` source that r2 does not carry.

### 3.4 · `Candidate.operands` — DEMOTED: a coupling to one OPTION, not to the question

- **r2 item 7** rebinds operands from content claims (`_derive_operand` binding `to`/`at`/`kind`/
  `amount` from a claim's value), gated on items 5 and 6.
- **#409 synthesis §3** prices `benefits_me(c)` **separately** from STR-1 precisely because it is a
  Candidate-schema problem: *"a `Candidate` carries only `(verb, subject, why, operands)` … and
  ED-IN-0232 made it **larger**, not smaller, by retiring the `beneficiary` role the register had
  called a bridge."*
- The carrier docstring makes the coupling sharp: **operands is never partial** — *"a form whose
  operands cannot all be bound forms NO Candidate"*. A beneficiary added as a fifth field after item 7
  rewrites the binder twice and re-opens that invariant twice.

> ⚠ **AND THIS ROW IS DEMOTED, ON THE RULING PASS'S OBJECTION, WHICH IS CORRECT.** The forced ordering
> follows from **the option the register LED WITH** — a fifth `Candidate` field — not from the question
> CAT-2 asks. **A beneficiary declared as a static `verb_table.yaml` column never touches
> `_derive_operand` at all**, and on that option r2 item 7 and CAT-2 are fully independent.
> `~~forced ordering~~` → **a conditional one, live only if CAT-2 is ruled toward the carrier.** S5
> (state the invariant where the binder is touched) is worth doing either way and costs a line; the
> *ordering* is not owed until the ruling lands.

### 3.5 · the told-channel control — two instruments, one number

| suite | measurement | instrument |
|---|---|---|
| **#409** `formal_analysis.md` M3 | 580 claims after two seasons, **100% firsthand**; `tell` resolved 9, deposited **0** | 12-person harness |
| **#408 r2** `01`/`02` | 2175 claims after one season — **2174 firsthand, 1 `told_by`** | `python -m engine.season.harness.populated 1` |

**Not a contradiction — two instruments, same qualitative finding** (the second-hand channel is
effectively dead). But M3 is the natural **before-control** for r2 item 8, and `CLAUDE.md` §0.1 pt 4
wants one instrument in both arms. Fix the instrument before item 8, or item 8's control is a
comparison between two different experiments — **which is the exact confound ED-MB-0042 was retracted
for.**

### 3.6 · `standing_of` — the seventh, and it was invisible to a keyword search

**FOUND BY THE VERIFIER, NOT BY THIS FILE'S AUTHOR, AND IT IS THE MOST INTERESTING OF THE SEVEN**
because of *how* it was missed rather than *that* it was.

- `engine/season/decision/options.py:443-465` — **`standing_of`** reads
  `[c for c in p.ledger if c.subject == p.id and c.source == "told_by"]` and runs `agreement(told,
  own)`, diffing `c.value` against the person's own firsthand claims over `PERSON_PREDICATES`
  (`rosters.py:356`).
- **That is the exact field r2 item 8 rewrites** — `_held.value` / `_held.predicate` on the `told_by`
  Claim built at `witness.py:361-363`.
- **And it is #409 CAT-9's own cited carrier.** The register names it twice, independently of this
  file: at CAT-3 (*"the one live consumer of provenance is `decision/options.py:461`"*) and at CAT-9
  (*"⚠ ALREADY BUILT AND UNRECOGNISED … **MEASURED: it returns 1000** — the maximum-gap default — for
  all 12 persons, because its `told_by` input is empty"*).
- **Item 8's own falsifier licenses exactly the drift that moves it**: `Partial` → *"one omitted `to`
  or one drifted operand"*, and the drift lands in `c.value`, which is what `agreement()` diffs.

> **So item 8 does not only feed CAT-3's testimony ladder, as §3.1 says. The moment it populates
> `told_by` it also unfreezes CAT-9 — a different category, a different carrier, a different pending
> ruling — moving it off a 1000-for-everyone default as a SIDE EFFECT, and no falsifier for that side
> effect is written anywhere in either suite.**

⚠ **Why §3.1 missed it: it looked at the WRITER and never at the OTHER READER of the same write.**
That is the shape to carry forward — a seam point is not a pair of documents wanting one object, it is
**every consumer of an object one document changes.**

### 3.7 · `Person.beliefs` — r2 deletes a carrier while #409 debates the word it carries

**FOUND BY THE RULING PASS. Neither suite knows.**

- **#409 STR-5** files `belief` as carrying **six live senses** inside the decision layer and asks which
  keeps the word — a `CLAUDE.md` §4 idempotency failure, and it blocks CAT-3 and CAT-4, which both
  borrow the term.
- **r2 deletes one of those senses' carrier outright.** `(Person, beliefs)` is deletion-ledger row 14
  in `05` — *"**No producing verb**"* — and `write_matrix.yaml:52-54` quotes `#358 rev.2 §D.1.1` for
  the reason: ***"`Person.beliefs` is DELETED — a belief is a `commit` to an OUGHT, not a field."***
  `beliefs` is also one of the 24 terms r2's vocabulary ledger counts OUT.
- **So the vocabulary question gets smaller while it is being asked**, and it gets smaller by an
  argument — *a belief is an act, not a field* — that is itself a position on STR-5. **STR-5 should be
  ruled knowing one of its six senses has already lost its field in the sibling suite.**

---

## §4 · WHAT IS NOT A COLLISION — recorded because it is the one a reader will expect

**STR-1 (*"nothing may write a Person's interior"*) does NOT bind r2 item 3b's body write.**

`write_matrix.yaml:161-168` files `(Person, body)` as `steps: [MAT, RES] · class: MATTER/ACTS ·
social: false`. STR-1's subject is the six rows at `[RES] ACTS` — `axis_count · beliefs · convictions ·
scar · stance · coherence` — which is the tier-0 `H-62` the matrix header calls *"one hole, not six"*.
`body` is not among them. **r2's body write is licensed by the ratified matrix and needs no STR-1
ruling.**

> ⚠ **THE CONCLUSION ABOVE IS RIGHT AND ITS FIRST DRAFT'S VOCABULARY WAS WRONG, LOAD-BEARINGLY SO.**
> This section called those six rows *"the **INTERIOR** class"*. **MEASURED over `write_matrix.yaml`'s
> literal `class:` column: 22 `ACTS` · 6 `MATTER` · 6 `MATTER/ACTS` · 3 `CALENDAR/ACTS` · 1 `CALENDAR` ·
> 1 `INTERIOR` · 1 unset** — and **the single `INTERIOR` row is `(Person, claim_ledger)` at `[WIT]`**.
> The header (`:14-17`) gives the derivation the loader asserts: `CAL→CALENDAR`, `MAT→MATTER`,
> `RES→ACTS`, `WIT→INTERIOR`, `CEN→MATTER`, `DEL→ACTS`.
>
> **`~~the INTERIOR class~~` → `ACTS`, and the difference inverts the reading.** `INTERIOR` is the class
> **no act may touch**; `ACTS` is the class an act is **licensed** to write. Filing the six as
> `INTERIOR` turns a standing licence into a prohibition — **which is precisely what makes STR-1 look
> like a live design call when it is not.** Read correctly, STR-1's option 1 (*"a verb at RESOLVE
> writes it"*) is not one of three choices: **it is the matrix's existing prescription with its
> producers missing**, which is what `H-62` says in its own shape field. That is how the ruling pass
> closes STR-1 at gate step 3 rather than sending it to Jordan — **and the close was only available
> once the class name was right.**

This was the collision this pass expected to find and it does not exist. It is filed here so a later
session does not spend the search again, and because a null result is a result (`CLAUDE.md` §0.1 pt 4:
*"asymmetric skepticism is a bias, not a defence"*).

**Also not a collision — the cores are disjoint.** Across r2's five documents, `choose.py` appears 0
times, `alignment` once incidentally, `temperament`/`courage`/`susceptib*`/`τ` **zero times**. #409
touches no seat, writ, matter or larder. Only the seam collides.

> ⚠ **AND THAT ARGUMENT IS METHODOLOGICALLY INCOMPLETE, WHICH §3.6 PROVES ON THIS FILE'S OWN BODY.**
> An independent verifier re-ran the count without trusting it and **reproduced the six figures
> exactly** — so the numbers are not wrong. But a **term-frequency check cannot find a coupling that
> shares no terms**, and `standing_of` is precisely that: a live code-level intersection between the
> two suites in a function whose vocabulary overlaps #409's not at all.
> **`~~disjoint~~` → DISJOINT ON VOCABULARY, which is not disjoint on code objects.** The cores are
> still separate designs; the claim that a grep establishes it is retired.

---

## §5 · The asymmetry that sets the order, and it is not a preference

| | **#408 / r2** | **#409 / behaviour layer** |
|---|---|---|
| status | `PROPOSED`, held back in full | `PROPOSED`, held back in full |
| rulings outstanding, **as written** | **6** (`RR-P · RR-A · RR-B · RR-C · RR-2 · RR-3`) | **15 rows, 0 filled** |
| rulings outstanding, **after `RULINGS.yaml`** | **5** — `RR-3` closes at step 3 | **4** — `CAT-6 · STR-2 · STR-5 · STR-6` |
| blocked items | **2** of 16 — item 13 (on `RR-A`), item 15 (on ratified positions 3–5), **+ item 11 on `CAT-6`** | — |
| buildable today | **yes — 13 of 16 items**, six of them on the critical path | **partly, and that is new** |
| execution artifact under §0.2 | none yet; item 1 is ~12 lines and produces one | none yet |

⚠⚠ **THIS TABLE'S FIRST DRAFT SAID `~~#409 is buildable NOWHERE~~` AND THAT IS NO LONGER TRUE —
THE UNIFICATION ITSELF IS WHAT CHANGED IT.** `RULINGS.yaml` ran all 21 questions through `CLAUDE.md`
§0's five-step gate and **closed 12 of them**, eight of the nine `CAT-*` rows among them. The single
largest claimed gate fell first:

> **STR-1 closes at step 3, and the close was only available once §4's class-name error was fixed.**
> The register states the person-interior write as a **prohibition** — *"nothing MAY write a Person's
> interior"*. The ratified matrix says the opposite: each of the six rows is `steps: [RES]`,
> `class: "ACTS"`, **with its own `emits:` kind** (`axis.incremented`, `belief.revised`,
> `coherence.changed`, `conviction.moved`, `scar.taken`, `stance.moved`). **They are a LICENCE nobody
> has taken up, not a ban** — which is what `H-62` says in its own shape field. So STR-1's "option 1"
> was never one of three designs; it is the design already prescribed, with its producers missing.

**What remains genuinely Jordan's on the #409 side is four questions, and they are one shape:**
`CAT-6` (H-71, shared with r2), `STR-2` (which axes the moral-value basis carries), and
`STR-5`/`STR-6` (the vocabulary — escalated as **one decision over five words**: `belief`,
`conviction`, `piety`, `temperament`, `stance`/`Disposition`).

**So the order is still forced, but by a smaller margin and for a better reason.** r2 remains
buildable today and needs nobody. #409 is no longer a question set — it is a design whose tables and
held vectors are now unblocked, waiting on an axis roster and a naming pass rather than on a
structural ruling nobody had taken.

---

## §6 · What this file does NOT do

Per `CLAUDE.md` §0's test — **does this document create work for a future session?** — this file
explains a judgment about **two artifacts that already exist** and creates no work of its own. It
allocates no build item, opens no queue and names no deliverable. The build order is `01`; the ruling
sheet is `RULINGS.yaml`. **If this suite dies, this file dies with it.**

It also takes no position inside either suite. r2's design choices are r2's; #409's categories are
#409's. ~~**Six seam points, one repair each**~~ → **EIGHT examined, SEVEN live** — §2's conflict plus
§3.1, §3.2, §3.3, §3.5, §3.6 and §3.7, with §3.4 demoted to a conditional. That is the whole of the remit. ⚠ **The count was wrong in this file's first draft and is corrected in place
rather than silently**: §3.6 was found by the verifier after the six were written, and a completeness
claim that has already failed once is worth leaving visible. **`BO-4` in `01` is the standing
falsifier for an eighth.**

---

## §7 · Defects found in the SUBJECT suites, reported rather than repaired

This file judges a seam and does not edit either suite. Two defects surfaced during verification and
are recorded here for whoever builds the item:

1. **`EXECUTION_PLAN` Trap 5 and item 3b cite `engine/season/loop/budget.py`, which does not exist.**
   The reader of `band_floors["body"]` is **`engine/season/decision/budget.py:63-75`** (the live read
   is at `:73`). The substance is unaffected — `body` is already the person's table and a `person` key
   is redundant — but a builder following the path hits nothing.
2. **"`band_floors.person` refuses at load" is imprecise.** No validator cross-checks a table's cell
   keys against its declared `keys:` roster at import; `table()` (`data/rosters.py:241-258`) returns
   whatever cells exist. A `band_floors["person"]` access would be a plain `KeyError` **at the access
   site**, not a graceful refusal at load. The trap is real; its mechanism is not what the plan says.

3. **r2 `05` §C.4 cites `editorial_ledger_in.jsonl:104` for `ED-IN-0210`; the file had 96 lines.** The
   live row is `:84`, with earlier rows at `:53` and `:73`. ⚠ **The general defect is worth more than
   the citation:** a lane ledger is **append-only and last-row-wins**, so grepping one and taking the
   FIRST hit reads a superseded status as current. Two of the ruling pass's own ten source corrections
   were this same mistake.
4. **#409's `ED-WR-0011` pairing rider on `RR-2` is stale, by that same rule.** `:11` carries the quote
   both suites lean on; **`:12`, same day, is `status: ruled` / `needs_jordan: false`** — Jordan ruled
   option A. **So `RR-2` is rulable alone now, scoped to populations**, and the pairing that held it is
   discharged.
5. **#409 names its entire second basis `temperament`, and the word is already taken.**
   `references/descriptor_registry.yaml:298` carries `temp.*`, *"5 territory temperaments"*, scope
   `territory/faction`, sourced to a head `CURRENT.md:30` declares live. **MEASURED: `temperament` and
   `piety` each appear in 0 files under `engine/season/`** — vacant in code, occupied in reference.
   ⚠ **This is the identical two-scales-one-word failure STR-6 catches for `piety` and misses for
   `temperament`**, and `CLAUDE.md` §4's idempotency rule is the one it breaks: a later session reading
   `temperament` cold cannot tell which scale is meant.

⚠ **None is fixed here.** `CLAUDE.md` §0.05 clause 3 — edit the owner and re-derive — makes 1–3 r2's
to correct in r2, and `EXECUTION_PLAN` says `05` wins on any disagreement; 4 and 5 are #409's.
**Filed, not patched.**
