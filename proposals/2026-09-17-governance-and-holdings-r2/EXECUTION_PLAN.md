# EXECUTION PLAN — the round-two suite, compressed to what you do

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL, like everything in this directory.** Landing an item here ratifies nothing; it makes a behaviour run.
## Lane: `IN` · shares **`ED-IN-0233`** with `01` and `05`. Allocates no id and introduces **no claim of its own.**
## What this is: **`05_LEDGER_AND_BUILD.md` §A.4, streamlined into a working sheet.** Every row below is `05`'s, dependency-sorted, stripped to *what you change · what proves it ran · what would show it wrong.* **Where this and `05` disagree, `05` wins** — it carries the reasoning, the citations and the controls, and this file carries none of them.
## What this is NOT: a second design. It adds no item, moves no dependency and changes no count. If you find something here that is in no sibling, that is a defect in **this** file.

---

## The only test that closes an item

`CLAUDE.md` §0.2: **a juncture is done when the behaviour EXECUTES.** Not when this file has a tick
in it, not when a `## Status:` line flips. Every row below therefore carries an **execution
artifact** — a run that prints something — and a **control**, because a number without one is not a
measurement (§0.1 pt 4). **Nothing in this table marks a juncture done.** Something running it does.

---

## THE CRITICAL PATH — six commits, and not one of them needs a ruling

This is the whole of what unblocks the suite. Do these in any order except where noted; each is its
own commit with its own close-gate run.

| # | do this | size | proves it ran |
|---|---|---|---|
| **1** | **`@effect_for("commit")`** — mint the Tenure `verb_table.yaml`'s `commit` row already declares | **S** | `resolvable_verbs()` **18 → 19**; a `commit` Tenure in a seeded season |
| **16** | **`add_tenure`'s hold-object guard**, and re-home the 16 faction rung-holds to persons | **S** | `build_realm` builds with **0** faction-subject holds; a faction→Rung `hold` now raises |
| **4** | **Delete `budget_office_bonus`** | **S** | planted hold → budget stays **5**; the other two budget terms still move |
| **3a** | **`nearest_store`** + the per-eater draw | **M** | `census` before/after on the 37/211 split |
| **3b** | The **body write**, the shared `_crossings`, `remove_person` — *after 3a* | **M** | empty-root run: bands crossed **and** the budget histogram moves |
| **2a** | **`reach`** · `place_of` · two question sources deleted · `w.crossings` deleted · `occasioned_by` reduced to one route | **M** | the question histogram, same seed, with the golden re-record **declared** in the message |

> ### Item 1 is the one to do first, and it is ~12 lines.
> `AUDIT_VERDICT.md`'s own verdict: *"the whole difference is one artifact — `@effect_for("commit")`."*
> `commit` is **Q4 `need`'s producer**, and `need` is already **81 questions** on the populated world —
> every one of them hand-minted by the harness, because **no act can make one today.** After item 1, a
> person can. Nothing else in the suite buys that much for that little.
>
> ⚠ **The trap in it:** an effect body that touches nothing makes the fold emit the **refusal**. The
> body must return the object it opened.

> ### ⚠⚠ Item 16 is a PRECONDITION, not a tidy-up, and this reverses the plan's own order.
> Measured on `build_realm(0)`: all 19 person-subject holds are on **Offices**, all 16 rung-holds are
> **faction**-subject, and `in_holdings` is therefore **false for every person over every rung.** A
> seat whose `revocation` is `"holdings"` refuses **every** revocation, forever, *and looks exactly
> like a working precondition while doing it.* So **item 10 depends on item 16** — land 10 first and
> you ship a row that cannot execute when reached.

---

## The whole order

**Bold deps are the ones that bite.** `fix` in the last column means the item sits outside the
ratified 27-position order and repairs something already there.

| # | change | size | depends on | proves it ran | gate |
|---|---|---|---|---|---|
| 1 | `@effect_for("commit")` | S | — | `resolvable_verbs()` 18→19 | Arc-2 **YES** · pos 14 |
| 2a | `reach` · `place_of` · two sources · `w.crossings` · `occasioned_by` → one route | M | — | question histogram + declared golden re-record | fix |
| 2b | CALENDAR `emits="date.fired"`, `subject=venue` | S | 2a | a planted date deposits a claim in the convener's ledger | fix |
| 3a | `nearest_store` + the per-eater draw | M | — | `census` before/after | fix |
| 3b | body write · shared `_crossings` · `remove_person` | M | **3a** | bands **and** budget both move on an empty-root run | fix |
| 4 | delete `budget_office_bonus` | S | — | planted hold → budget 5 | pos 14 |
| 5 | **the Record-kind fold** — `record_kinds` + its refusal · `issue`/`petition` bodies · 2 matrix rows + 2 `World` dicts deleted · the deposit rule | **L** | 2a | a season log with a `content:dispensation` claim in the issuer's ledger | Arc-2 **YES** · pos 15 |
| 6 | `give` + body + `_req_give` + release-before-mint | M | **5** | a three-season trace: issue → carry → give → claim | Arc-2 **YES** · pos 16 |
| 7 | content-claim operands; Q2's third clause | M | **5, 6** | candidates with writ-derived operands > 0 | pos 19 |
| 8 | `tell` at `Partial` deposits a lossy copy | S | 5 | `Full` → identical; `Partial` → one omitted `to` or one drifted operand | fix |
| 9 | obligees co-located mint `inferred` · `oblige` body · `establishment_of` rewritten with a caller · `Office.establishment` deleted | M | 1 | claim-source histogram: `inferred` **0 → N** | Arc-2 **YES** · pos 19 |
| 10 | **`offices.yaml`** — bases as rostered values · both predicates rewritten · four title helpers + `is_title` + the `titles` roster deleted · holders seated · purview corrected | **L** | **4, 16** ⚠ | `resolvable_verbs()` and the VERBS-ONLY-REFUSED line both change | pos 6 (rides) |
| 11 | commission `Record` on `confer`; person-side `remit:` via the claim | M | **5, 10** | the H-71 test goes RED and is rewritten to assert the claim | Arc-2 **YES** · pos 19 |
| 12 | **`works`** kind · `work` advances `stage` · `restore` body · **`found`** + body · `(Rung\|Site, exists)` get a producer | **L** | **5** | `census` shows one more rung; a Site's condition rises | Arc-2 **YES** · pos 7/24 |
| 13 | RR-A's four verb deletions + `remit_acts.dispatch` | S | **`RR-A` ruling** | row count 35; `resolvable_verbs()` loses `dispatch` | pos 19b (deleted) |
| 14 | the 13 field deletions + `judging_set` + `conferral_path` | S | **9, 10** | `matrix_rows_without_a_field`, before and after | fix |
| 15 | `Act.via` + F3 | **L** | **positions 3–5** | position 6's own | **THE GATE** · pos 6 |
| 16 | `add_tenure` hold-object guard + 16 faction holds re-homed | S | — ⚠ **before 10** | 0 faction-subject holds at build | pos 12 |

**Ledger: net −17 engine objects, 39 removed against 22 added.** `05` §A.1 owns that arithmetic and
names the five things the plan miscounted. **Do not quote −20 from anywhere.**

---

## What is blocked, and on what

| blocked | by | can you start? |
|---|---|---|
| item **13** | **`RR-A`** — folding the four response verb rows overwrites `ED-IN-0210`'s letter | **No.** Jordan's |
| item **15** | ratified **positions 3–5** | No — and it is the Arc-2 gate itself |
| item **10**'s `holdings` branch | item **16** | Yes, once 16 lands (16 depends on nothing) |
| **everything else** | nothing | **Yes, today** |

**Six ruling requests sit with Jordan** — `RR-P` (the principle as a candidate `AX-7`), `RR-A`,
`RR-B` (eight sentences of ratified `architecture/`), `RR-C` (this order departs from the ratified
one), plus `RR-2` and `RR-3` carried from round one. **Only `RR-A` blocks an item.** `05` §C.4 is
their single ledger; do not re-open them here.

---

## Six traps, each measured rather than feared

1. **An effect body that touches nothing emits a refusal.** Item 1's body must return what it opened.
2. **`revocation: "holdings"` is unsatisfiable today** — 0 person→rung holds. Item 16 first, or item
   10 ships a branch that refuses always.
3. **The two deleted question sources contribute 0 questions** (measured). That is what makes item
   2a's control an identity: every unit of movement is REACH's, none of it the deletion's.
4. **Item 2b is unobservable on the populated world** — `w.dates` is empty after a season, because
   `convene` never forms. Plant a date or it proves nothing.
5. **`band_floors.person` refuses at load.** `band_floors["body"]` already is the person's table and
   `budget.py` reads it live. Two documents planted this independently and both got the refusal.
6. **A falsifier that iterates and finds nothing must assert that it asserted** (§0.1 pt 2) — a loop
   whose body never ran is indistinguishable from a passing test. `LB-10c` is the live case.

---

## Cadence, because a reader of a build order is the person about to get this wrong

`CLAUDE.md` §0.4: **the full suite is a CLOSE step, not an inner loop.**

```sh
python -m pytest tests/valoria/test_<the one file>.py -q   # mid-item: seconds
python -m pytest tests/valoria -q -n auto                  # ONCE, before each commit: ~2m36s
```

Each item is **one commit**, so the gate runs once per item. Red re-runs the failing file only.
`tools/valoria_local.py --staged` never runs pytest — run it freely.

---

## Where the detail lives

| you want | read |
|---|---|
| the reasoning, citations, controls and costs per item | **`05_LEDGER_AND_BUILD.md` §A.4** |
| the deletion arithmetic | `05` §A.1 |
| the ruling requests through §0's five-step gate | `05` §C.4 |
| why the design is shaped this way at all | `README.md`, then `01`–`04` |
