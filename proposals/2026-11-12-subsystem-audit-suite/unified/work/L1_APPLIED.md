# L1_APPLIED — running record of the Layer 1 amendment lane (A-97)

## Status: WORK RECORD (the Layer 1 amendment lane, 2026-11-12; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted with `unified/work/` when v12 is adopted)

Authority: Jordan, `unified/DECISIONS_ANSWERED.md` A-97 (*"Layer 1: make amendments as required"*) and A-96
(J-U6-01 Option A). Drafts: `unified/U3_LAYER1_AMENDMENTS.md`. Every edit below follows a ruling A-n; none edits
Layer 1 to match code.

## Method and conventions followed

- **Convention read at the heads.** `04` and `hol` carry their amendments as `⚠ AMENDED <date> (Jordan-directed,
  <ids>): <what>` on the `## Status:` line (2026-10-03, 2026-10-28) and in place, keeping the superseded text legible
  (`04:150` "This line read …"; `04:331` "⚠ AMENDED: `dates[]` DELETED …"; `04:1026` "CONSTRUCTION AMENDED, GRADE
  UNCHANGED"; rev. 2's rule: *"nothing is overwritten silently"*). Followed: each in-place edit says `⚠ AMENDED
  2026-11-12 (Jordan, A-n; A-97, node L1-An)` and quotes what the text read.
- **`hol` is append-only in this lane.** `engine/season/harness/register.py::verify_citations` checks every
  `hole_register.yaml` `cite:` quote against `hol` AT the cited line (±6). Inserting a line in `hol` would move
  every later citation, so every `hol` amendment is appended to an existing line; no `hol` sentence is replaced
  and no line is added. Baseline before any edit: `python -m engine.season.harness.register --verify-citations`
  → `CITATIONS: all resolve`, exit 0.
- **`04` new lines kept to the minimum** so the suite's `04:NNN` citations stay valid as far as possible: one new
  PART D row (52, A-96) placed after row 51, and one note line in §C.4 (A-96). Line shifts are recorded per node.
- **Other `architecture/` files** (the stage documents 00–10, `ARCHITECTURE_V2.md`, `PLAN.md`; all `## Status:
  RATIFIED`, Layer 1) are not amended in substance; where one restates an old rule as live, a one-clause pointer
  is appended to that line naming the node (append-only, for the same citation reason).
- **Ledger rows.** The ledger's superseding-row convention (ED-IN-0149 precedent, restated in `ED-MB-0016`'s
  2026-10-26 row: *"The earlier row is NOT rewritten; an id's effective status is its LAST row"*) puts a
  superseding row under the SUPERSEDED id with `supersedes_row: true`. Followed for A-22, A-24, A-77, A-85.
  One new id is allocated from `references/id_reservations.yaml` (IN `next_free` 358 → 359): `ED-IN-0358`, the
  record of this Layer 1 amendment, as every earlier Layer 1 amendment carries one (ED-IN-0284/0285, 0302/0303).
  `[ASSUMPTION: the orchestrator asked for new ids for the successors; the ledger's own convention is a same-id
  superseding row; taken because a new id would leave the old id's effective status (its last row) unchanged.
  Revert: re-key the four rows to fresh ids.]`

## Per node

Line numbers are after this lane's edits. `04` gained exactly one line (PART D row 52 at `:1082`), so every `04` line
up to `:1081` is where the suite cites it and every line after moved by +1 (PART E step 13 `:1130` → `:1131`; PART F
rows +1). `hol`, `01`, `03`, `10` and `ARCHITECTURE_V2.md` gained no line. Every in-place edit quotes what the text read.

| node | ruling | files and lines changed (both halves named first) | restatements amended or annotated | the sentence a contradicting code arm is now checked against |
|---|---|---|---|---|
| `L1-A3` | A-3 | `04:777` §C.5 provider line; `04:786` crossing row; row 24 `:1050` | `04:182` (adapter row's return cell); row 30 `:1057`; `hol:1407` §39.4 | `04:786`: the subsystem returns a `Margin`, or (the field provider only) an end state from `won · lost · drawn`; anything else has not met the contract |
| `L1-A4` | A-4 | `04:182` §A.2 adapter row, reads column; row 22 `:1048` | `hol:1684` §44.3 *decides* | `04:182`: callables supplied for persons, declared once as a class, carry no token and no store handle |
| `L1-A72` | A-72 | row 19 `04:1045`; `hol:1396` §39.3 (appended to the heading line) | `04:775` "NO DEFAULT" holds unamended (the value is a fixture, not a default); `hol:1377`, `:1442`, `:1882`, `04:902` hold (all say "no default", still true) | row 19: `max_depth` has no default; its value is the fixture `contest_nesting_cap` = 1 |
| `L1-A9` | A-9 | `04:662` §C.4; row 36 `:1065`; row 41a `:1071` | row 29 `:1056`; F.26 `:1227`; `hol:974` §27.1, `:1125` §32 item 3; `ARCHITECTURE_V2.md:753` H-30 | `04:662`: `acts = flatten(canonical_order(scenes))`, within a scene the chooser's order |
| `L1-A64` | A-64 | row 36 `04:1065` | F.26 `:1227`; `hol:974` §27.1, `:1166` §33; `ARCHITECTURE_V2.md:753` | row 36: rank is a declared weight of a keyed precedence draw, never a sort key |
| `L1-A12` | A-12 | `04:331` tuple gains `modifier?`; `:332` NEVER line; `:351` invariant; row 33 `:1062` | `hol:430` §11.1 (covers `:434`); `01_AXIOMS.md:978` §D.6, `:1635`; `03_VERBS_AND_LOOPS.md:34` §A.3 (heading marks its argument, `:39-42`, superseded); `ARCHITECTURE_V2.md:446` | row 33: one modifier column, `modifier?`, read off `Act.via` by the `office` source; it helps a roll and gates nothing |
| `L1-A13` | A-13 | `04:331` tuple gains `passes_through?`, `hand_term?`, `audit_at_exit?` | row 11 `:1037` checked, holds (none names a holder) | `04:331`: three optional facts, absent = as today, no fourth key |
| `L1-A20` | A-20 | `04:460` `at_war`; row 48 `:1078` | F.32 `:1233` answered; `10_FACTIONS_AND_DEPLOYMENT.md:73`; `01_AXIOMS.md:1374`, `00_THE_METHOD.md:166` checked: they say "an owned edge" without naming whose, so they are narrowed, not contradicted | `04:460`: live `commit`s by a holder of a seat of either party that may muster |
| `L1-A29` | A-29 | PART E step 13 `04:1131` | row 29 holds (the three named quantities stay integers); `hol` §46.1 `:1790` (sensation, float32-exact, integer-domain parity) and §48 (fixed point for `condition`, `stores`) checked: narrower constraints on other quantities, not contradicted | step 13: the hash under the float contract (`+ - * /`, `sqrt`, `fmath.py`). `[NOTE: engine/dice_engine/fmath.py does not exist in the tree; the step names it as unbuilt]` |
| `L1-A30` | A-30 | `04:927` §C.12 row; rejection 4 `:953`, `:959`; row 35 `:1064` | `hol:1153` §33, `:1832` §49 ("never a shared re-seeded generator") hold; `04:211` ids "no allocator, no counter" holds (ids, not draws) | row 35: no counter across keys; `n` is part of the key. `[CHANGED FROM DRAFT: the census figure "18,702 keyed draws" was not carried into Layer 1, unverified by this lane; the draft's "the draw (built)" became "the draw", because `World.new_draw` (`state/world.py:1632`) is still a per-tick ordinal counter]` |
| `L1-A62` | A-62 | row 51 `04:1081` | §B.9 `:449` holds; `hol` §26.3 holds | row 51's falsifier: `budget()` after a refused act differs from after a made one; a refusal Event's `changes[]` stays empty |
| `L1-A92` | A-92 | `04:251` §B.2 invariant; row 18 `:1044` | `hol:122` §2 T2, `:362` §9.3; `01_AXIOMS.md:146` AX-3; `ARCHITECTURE_V2.md:330` | `04:251`: evidence enters a conviction only as a term in the person's own drawn act at RESOLVE |
| `L1-A96` | A-96 | NEW PART D row 52 `04:1082`; §C.3 `:654`; §A.2 `loop/encounter` `:177` | row 1 `:1026`, row 41 `:1070`, PART D count note `:1088`; `hol:1194`, `:1197` §34.1; `01_AXIOMS.md:78` AX-1 | row 52 (see below) |
| `L1-A96b` | A-96 | §C.2 `04:619` (one clause appended to the `founding` line); row 10a `:1036` | — | §C.2's `detention` clause |
| banners | A-97 | `04:3`, `hol:3`, `01_AXIOMS.md:3`, `03_VERBS_AND_LOOPS.md:3`, `10_FACTIONS_AND_DEPLOYMENT.md:3`, `ARCHITECTURE_V2.md:3` | — | `## Status: RATIFIED` unchanged in every file |

### L1-A96 — the drafted node (PART D row 52; grade MECHANICAL / MECHANICAL, CONVENTION on the closed set)

Narrowest wording taken: **one** act, named, formed at ENCOUNTER on the Failure band of the access draw to a guarded
target; actor the guard (a `PersonId`, so row 1's type construction stands and row 1 is annotated, not rewritten);
the first of the guard roster that admitted the draw, in its declared order, never by rank (row 36 kept); `via` the
seat he is sworn to; `causes[]` the failed act; the guard's `choose` not called; **no keyed draw consulted** for it
(no scene fought, no wound dealt, so "always" holds); through the gate like any act; witnessed like any act. A second
engine-formed act is stated to be a Layer 1 amendment, never a data row or a body branch (rows 27/27a's scripting-drift
line). Row 41 is annotated: the formed act is not a decision. Grade: MECHANICAL (one formation site; one planted-Failure
test asserting exactly one `capture`, its actor and its `causes[]`, and none on Success or Partial). The PART D counting
rule was re-run by script on the amended table: 57 entries, 52 numbered rows, 27 whose Python grade begins STRUCTURAL;
the count note at `:1088` says so. `[ASSUMPTION: a numbered row 52 rather than a lettered row beside 41, because the
exception amends two non-adjacent rows (1 and 41) and a numbered row after 51 moves the fewest cited lines]`.

### L1-A96b — the gate basis, and the proposal's edit 8 (the orchestrator's mid-task question)

**Checked:** `04` §C.2 (`:604-620`) lists the Tenure-write bases. Every seat-authorized one has the actor seated in
`via` (T-o and `conferral` resolve against the seat the actor holds; `renewal` and both `determination` arms say "actor
seated"). The code's `warrant` basis (`state/gate.py:277-289`, `may_warrant` `:980-1002`, returned at `:1424-1430`) is
not in §C.2 at all (`gate.py:157-164` records that §C.2 "still enumerates nine" and is Jordan's); it needs the actor
seated in `via` and a grant carrying `dispatch`. The formed `capture`'s `detain` is an edge whose subject is the
attacker (`may_warrant(w, actor, via, t.subject)`, `:1429`), so T-m cannot admit it; the guard is an unseated cohort
(proposal 22_C, its point 1), so `warrant`, T-o, `conferral` and `determination` cannot either. **No existing basis
serves.**

**Edit 8 (an "oath" arm inside `may_warrant`) is not the right shape and should not be built.** It widens `warrant`, a
seat-authority predicate with several callers (`arrest`, `capture`, `seize` effects), for every caller: any person
sworn to a seat and standing where a prisoner lives would pass the gate's custody basis on his lord's seat, whether or
not an engine-formed act is in play. That is a general authority no ruling grants (A-22 makes sworn men the
RECIPIENTS of a seat's orders, not exercisers of its seat), and the arm would also skip `warrant`'s purview conjunct.
The proposal's own claim (*"no `arrest`, `capture` or `seize` act of an unsworn actor passes by this basis"*) is true
and beside the point: the widening is to sworn actors.

**Applied instead (`L1-A96b`):** one **causation-bound** clause in §C.2, `detention`: *a Failure of the access draw to
a guarded target this same encounter took admits the OPENING of the one `detain` on the attacker that the engine-formed
`capture` writes, actor the guard that act names, `via` the seat he is sworn to.* It has the shape of `handover`, T-n
and the cascade (admitted by its cause, observed, not claimed) and admits that one write of that one act; `warrant` is
unchanged. Row 10a (the PART D twin of §C.2) names it. Grade: MECHANICAL at the gate (row 10a's). **For the proposal
(not edited here):** replace edit 8 with a `tenure_write_basis` clause returning `DETENTION` when the write's cause is
the formed act of an access-draw Failure (the gate needs that cause handed to it, as `revoked`/`released` are handed by
`refuse_unauthored`), and drop the oath arm. `[ASSUMPTION: the gate can be told the cause by the ENCOUNTER caller the way
`refuse_unauthored` hands it the batch sets; not verified against `World.write`'s signature]`.

**Found, not applied:** `04` §C.2 does not list five bases the code returns (`WARRANT`, `SEIZURE`, `MUSTER`, `CESSION`,
`CLAIM`), while row 10a says §C.2 "is the current, complete enumeration". No ruling A-n owes that update (it is the
IN-44 row's, "Jordan does"), so A-97 does not reach it; the conflict is named here and in `ED-IN-0358` for Jordan.
`U5d_FA_land_and_seats_pass_on_a_won_march.md` e1's `conquest` basis is the same class (no ruling applied it).

### Ledger rows (append only; no earlier row edited; no `registers/archive/` file touched)

| node | row | file |
|---|---|---|
| `L1-A22` | `ED-IN-0256` superseding row, 2026-11-12 (its original is `editorial_ledger_in_archive.jsonl:172`) | `registers/editorial_ledger_in.jsonl` |
| `L1-A24` | `ED-IN-0261` superseding row; the words "rolls nothing" are the code's (`queries/person_q.py:904`), not the ledger's, and the row says so | `registers/editorial_ledger_in.jsonl` |
| `L1-A85` | `ED-IN-0352` superseding row: (3) gains "except where Jordan rules that a draw reads a strife level; the first is A-68" | `registers/editorial_ledger_in.jsonl` |
| (record) | `ED-IN-0358`, new: the Layer 1 amendment (A-96, A-97) | `registers/editorial_ledger_in.jsonl`; `references/id_reservations.yaml` IN `next_free` 358 → 359 |
| `L1-A77` | `ED-MB-0016` superseding row: zero when 27C's first arm passes; `lanchester_signature.py`'s LINEAR band edited once in B19 | `registers/editorial_ledger_mb.jsonl` (MB `next_free` unchanged at 82: no new MB id) |

### Held (not Layer 1; A-97: "canon rewordings and the ratified strife master … stay held until named")

`L1-A84` (the strife master, a design document), `L1-A17` (canon lines 76, 90, 96), `L1-A60` (the 2026-07-08 directive,
unlocated), `L1-A26` (a `CODE` node: `degree_from_net`'s docstring, rewritten in B05).

### Checks run (actual output)

- `python tools/ci_naming_check.py` → exit 0, "Naming check: no new use of a deprecated name."
- `python tools/validate_ed_citations.py` → exit 0, "0 citation-integrity violation(s); 9 deferred; 318 open-reference info."
- `python tools/currency_consistency_check.py` → exit 1, `[CURRENCY DRIFT: 7]`, all seven "CURRENT.md stamp 2026-11-04
  predates head …" for files this lane did not touch (`strife.py`, `world_q.py`, `canonical_sources.yaml`,
  `restructure_ledger.md`, …): pre-existing, not caused here.
- `python -m engine.season.harness.register --verify-citations` (the one tool that parses `hol` by line, and
  `ARCHITECTURE_V2.md`/`PLAN.md` by presence) → before: "CITATIONS: all resolve"; after: "CITATIONS: all resolve".
- `python -m engine.season.harness.register --check` → exit 1 before and after, output byte-identical (`diff` empty;
  the R2 violations are pre-existing).
- `python tools/tests_for_diff.py` → the branch diff against `main` is 715 files, so it names the full suites (no
  narrowing). Per CLAUDE.md §0.4 only the tests that read `architecture/` at runtime were run:
  `pytest engine/season/tests/test_season_shape.py -k "w1_ or cr45 or citation or register or architecture_v2 or
  discharge"` → 9 passed (the four CR-45 items that read `files.SOURCE_353_MD`, the two W1 citation tests, W4, two W9).
  No `tools/*.py` reads `04` or `hol` structurally (grep of `tools/` for `04_CODE_ARCHITECTURE`/`holonic_ARCHITECTURE`
  returns no reader); the other test hits name `architecture/` in docstrings only.
- **Falsifier greps** (old wording of each rule, over `architecture/`, excluding lines carrying `AMENDED 2026-11-12`):
  `returning a winner|never a winner` → 0; `depth cap has NO DEFAULT` → 0; `rank never breaks a tie` → 0;
  `upkeep, dates\[\], exists` → 0; `hash in the integer domain` → 0; `RandomNumberGenerator|RNG \(unbuilt\)|no counter,
  no service|threaded like` → 0; `debited \*\*at RESOLVE|carrying the debit` → 0; residual hits, each annotated on the
  adjacent line of the same item: `hol:1123` (A-9, note on `:1125`), `hol:434` and `03:41` (A-12, under annotated
  headings `hol:430`, `03:34`), `01:144` and `hol:361` (A-92, notes on `:146`, `:362`), `01:77` (A-96, note on `:78`).
  Hits judged NOT restatements: `01:1697` (a treaty, not war); `ARCHITECTURE_V2.md:262`, `PLAN.md:304`, `hol:1444`,
  `hol:2002` ("no reaction inside a season" vs the nested contest seam, D16, a different reaction).
