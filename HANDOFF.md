# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. **Nothing surfaces this file automatically** — the
SessionStart banner that used to relay "Next actions" was retired 2026-08-21 with the rest
of the session machinery (ED-IN-0194), and `CLAUDE.md` §0.3 records the result of the
experiment it was the instrument for. Read this file, and your lane's, yourself.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

---

# ⭐ THE WORK ORDER — 2026-09-13 · **THE ONE ORDERED LIST. START HERE.**

**Jordan, 2026-09-13:** *"sort out all the open items into a legible order"*, after asking since the
beginning. This section is that list and it is the ONLY thing in this file that claims to be current —
every other dated section below is marked **WAS CURRENT** and is history. Five sections used to say
`⚠ CURRENT`, from four different dates; that is what made this file unreadable.

**Two rules that make the list trustworthy rather than merely tidy:**

- **Every row names the command that measures it.** Run the command; do not trust a number written
  here, including mine. Numbers below carry the date they were measured.
- **`CLAUDE.md` §0.2 — done means the behaviour EXECUTES.** Every row names its falsifier. If you find
  yourself authoring a document instead, you are in the loop §0.3 describes.

## ⚠⚠ THIS IS AN INDEX, NOT AN ORDER. THE ORDER IS RATIFIED AND LIVES ELSEWHERE.

**`workplans/2026-09-11-reconciled-program.md` — *"every live item, in one order, across every lane"*,
`## Status: RATIFIED 2026-09-12 (ED-IN-0215)`, 27 positions — IS THE SINGLE OWNER OF THE ORDER.**
The first draft of this section was a *third* ordering surface that did not name it, and an
adversarial pass overturned it on exactly that. **If you are choosing what to do next, open the
reconciled program.** What lives here is an index into it: where this session's work landed, and the
measured state of the tree that a reader needs before position 1 makes sense.

⚠ **AND THE RATIFIED ORDER PUTS ARC 2 FIRST, WHICH THIS SECTION ORIGINALLY HAD BACKWARDS.** Positions
3–7 are `G1a · G1b · G2 · G3 · G4` — the gate contract — *before* `U5` (10), `U6` (11) and
`H-62-rest` (12). `ED-IN-0212`'s reason: effects mutate inside the gate's `apply()` closure while
`04 §C.2:536` has the gate compute before/after itself, so **the gate's signature IS the effect
contract and 11 effects are already on the wrong one.** Anything that writes an effect — governance
verbs, the 20 silent verbs, antonym closers, `Tenure.term` — is downstream of that. A session that
starts with a verb is paying for the rewrite twice.

⚠ **ITS OWN STATUS LINE RECORDS A LIVE COLLISION**, and it is not this file's to settle:
*"§0's claim to be the single owner of the ORDER across all lanes is **contested** —
`workplans/2026-09-11-arc-sequence-spine.md` positions 2–15 remain independently actionable, and
`valoria_master_workplan_v7.md` §6 records that the collision is open and needs a commit rather than
a paragraph."*

⚠ **THE `measured:` BLOCKS IN `requirements.yaml` ARE STALE IN THE DIRECTION OF UNDERSTATING PROGRESS.**
Re-measured 2026-09-13 by `python -m engine.season.harness.corpus_run`: R-01's row says R3 passes
*"22/30 NPC and 34/59 ARC"*; the run prints **30/30 and 56/59**. R-08's row says candidate ties break
*"ALPHABETICALLY BY VERB"* with *"only 2–7 of 22"* candidates scoring; the tie is **broken by the draw**
(U4/H-96). `PLAN.md`'s `W27` proof bar — *"distinct executed sets > 2 (2 today)"* — read **25** before
this session and **43** after it. **Re-run the instrument before you plan against a row.**

⚠ **THREE CORRECTIONS AN ADVERSARIAL PASS MADE TO THE PARAGRAPH ABOVE, kept because each is a trap
the next reader would fall into as well.** (1) **R-08 is not stale in the direction claimed** — the
same row retracts itself at `requirements.yaml:452-463` and R-06 at `:396` already carries
*"7..11 of 28 -> 16..22 of 28"* from `U3`. A figure already written in the file was presented here as
a fresh re-measurement. (2) **"16..22 of 28" has a per-case denominator** — `corpus_run.py:579` prints
`sep[0][1]`, the FIRST case's candidate count, not a corpus-wide one. (3) **R-01's replacement has a
denominator clash**: 30/30 + 56/59 is out of **89 live worlds**, while `:265` and `:524` count *"84 of
143"* — **cases**. `requirements.yaml` carries **four mutually inconsistent R3 figures** (`:142`,
`:265`, `:333`, `:524`) and nothing says which is the baseline. That is the real finding, and it is
bigger than any one stale row.

---

## §1 · THE CENSUS — how many open items exist, so this order is known to be complete

| surface | open | where |
|---|---|---|
| requirement rows (**THE NINE**, ruled ED-IN-0204) | **4 `not_met` · 4 `partial`** (1 met) | `engine/season/requirements.yaml` · `register --requirements` |
| holes | **116 rows** — 44 tier-0, of which **10 are tier-0 `grade: absent`** | `engine/season/hole_register.yaml` |
| verbs | **20 of 38 have no predicate and no effect**; 5 foldable but never attempted; 2 always refused; **11 execute** | `corpus_run` → `WHERE THE 38 GO` |
| cases | **54 of 143 unrepresentable** (44 faction, 10 world) | `corpus_run` → `unrepresentable scales:` |
| `needs_jordan` ledger rows | **37 open**, of which **7 are self-contradictory** (`ED-PC-0015`…`0021`, all `ratified` and still flagged) | `registers/editorial_ledger*.jsonl` — ⚠ **fold to the LATEST row per id**; these are append-only and a naive count reads 41 |
| M1 junctures on the board | **7: 2 not_started · 1 blocked · 4 in_progress · 0 done** | `workplans/workplan_v6_progress.yaml` — **stale, see §4** |

---

## §2 · THE ORDER — do these in this sequence

| # | do this | closes | falsifier | size |
|---|---|---|---|---|
| ~~1~~ | ✅ **DONE 2026-09-13** — the counterparty. Each person now holds their OWN Proposition naming another PERSON, with the case's own want | R-06 · R-07 · half of `W27` | **acts** naming another person **0 → 256**; distinct behaviours **25 → 43** | **S** |
| **2** | **The cast.** Port `harness/populated.py`'s per-case cast into `build_at` — one named person per case, seated by institution | `W27` · R-06 · R-07 · `A3` | `build_at` seats > 3 named people; `RANKING DISCRIMINATION` moves | **M** |
| **3** | **`H-71`.** 5 verbs are foldable and never attempted. ⚠ *Downstream of Arc 2* | R-05 · `H-71` (tier 0) | `test_no_person_can_choose_a_governance_verb_and_h71_is_why` **reddens** | **M** |
| **4** | **The 20 silent verbs.** 20 of 38 carry no predicate and no effect | R-05 · `H-62` (tier 0) | `WHERE THE 38 GO`: the 20 shrinks | **L** |
| **5** | **The six antonyms.** `ED-IN-0210` Ruling 2; none of the 9 verbs exists | R-05 · relations that end | the 9 appear in `verb_table.yaml` and execute | **M** |
| **6** | **`Tenure.term`.** `T-n`'s unbuilt half — `Tenure` has `until`, not `term` | R-05 · relations that lapse | a `Tenure` matures a declared term at a later tick | **M** |
| **7** | **The strategic layer.** 54 of 143 cases unrepresentable; the loop runs at person/settlement/realm only | R-04 · `W10` · `W13` | `unrepresentable scales:` shrinks below 54 | **XL** |

### 1 · THE COUNTERPARTY — one authored value, then the authoring
`engine/season/harness/corpus_run.py:297` — `Proposition("prop_x", "OUGHT", ids[chain[0]], "a standing
ambition", True, 0)`. The third argument is a **rung** id and the fourth is **one string for all 143
people**. Make the subject a **person** and every committed person's Q4 question refers to a person.
**MEASURED 2026-09-13 THROUGH THE SEASON DRIVER, WITH A CONTROL** — 27 NPC cases run end to end in
both arms:

| arm | acts | naming another person |
|---|---|---|
| control — `prop_x.subject` = a **rung** | 443 | **0** |
| arm — `prop_x.subject` = a **person** | 638 | **168** |

⚠ **THE EFFECT IS LARGER THAN THE CLAIM THIS REPLACES.** The previous text said *"same 84 candidates —
the **referent** changed"*. At the ACT level the count is not the same: **acts rise 44%**, because
person-subject questions open verbs that were unreachable. The candidate-level figure could not be
reproduced — reconstructing `assemble`/`opening_set` by hand raises `Ungraded`, and a first attempt
that appeared to confirm it had silently passed `View=None`. **Use the driver, not a reconstruction.**

Nothing is added — `Proposition.subject` is an unconstrained `str`, and `decision/options.py` resolves
`subject`/`to`/`site` to that one referent. **Q4 is the only door**: Q2's guard
`c.subject == p.id or c.subject in mine` bars the others.

⚠ **19 OF 46 NPC CASES DO NOT BUILD AT ALL** — they are faction-scale and `build_at` refuses them.
That is R-04 (item 7) reaching into items 1 and 2: whatever the cast work achieves, it reaches 27 of
46 NPC cases until the re-scale lands. The order below does not currently account for that.
**Traces to** `ED-IN-0210` Ruling 1 — *"verbs invoke mechanisms or interactions between a character and
another entity/character. they are not fiats."*
⚠ **The one-line change is not the deliverable.** Deciding *which* Propositions name persons in which
cases is. `harness/populated.py` already does this for the 46 NPC cases (`wants_of` reads the case's
first `core` need; `concerns_of` resolves `who_acts`), which is why item 2 follows immediately.

### 2 · THE CAST — `W27`, narrowed to the NPC lane
`build_at` still does `for n, pid in enumerate(("p_a", "p_b", "p_c"))` — three anonymous people, same
rung, all 143 worlds. **Every number in R-01, R-02, R-06 and R-08 was measured on that.** `§0.1 pt 4`:
a number without a control is not a measurement.
The machinery exists and is proven: `harness/populated.build_realm` seats **46 named people across 26
buildings** from `who_acts` and the corpus's own names, and is wired into no gate. The work is porting
it per-case into `build_at`.
⚠ **`PLAN.md` makes `W27` depend on `W28` (143 authored `cast:` blocks). That does not bind the 27
NPC cases that build** — `populated.py` resolves a cast without authored blocks (11 named ties, 15 institutional).
`W28` remains required for the 97 ARC cases, which name situations, not people.
⚠ **`PLAN.md`'s stated proof bar is spent**: *"distinct executed sets > 2 (2 today)"* reads **25**.
Use `RANKING DISCRIMINATION` and the R-06/R-07 rows instead.

### 3 · `H-71` — 5 verbs built and unreachable
`hole_register.yaml` `H-71`, **tier 0, `grade: absent`**. §F1 clause 2 evaluates eligibility
person-side; `remit:<act>` cannot be, because the person holds the `hold` Tenure while the **office**
owns the remit. `person_side_eligible` declines every `remit:` alternative unconditionally, so a verb
whose ONLY eligibility is a remit is unreachable **even where the actor genuinely holds the office
whose remit names the act**. `H-71`'s own `unblocks:` says **9 of 32 verbs — 8 remit-ONLY, plus
`levy`**; the in-tree falsifier scopes to `stratum == "binding_decision"` with all-`remit:`
eligibility and asserts `>= 7`.

⚠ **THE FIVE-NAME LIST THIS ENTRY FIRST CARRIED WAS WRONG IN TWO PLACES, which is precisely the
failure its own "do not re-derive" warning is about — so the correction stays.** The set
`{confer, convene, destroy_record, dispatch, revoke}` is right as *"foldable but never attempted"*
(`corpus_run`'s `WHERE THE 38 GO`), but the LABEL was false for two of them:
**`dispatch` has no effect body at all** (`effects.py:88-89`: *"`dispatch` needs none: Part E gives it
`writes: []`, so an order is an EMISSION and nothing else"*), and **`destroy_record` has no `remit:`
alternative**, so `H-71`'s mechanism cannot be why it is unreachable — its eligibility is
`["hold:<record>", "presence"]` and it declines on **both**, which is **`H-75`**, a different hole.
⚠ **Do not re-derive `H-71`.** Three sessions have now independently "found" it, this entry included.

### 4 · THE 20 SILENT VERBS — R-05's main body
`WHERE THE 38 GO`, measured 2026-09-13: **20 have no predicate and no effect**, 5 are item 3, 2 are
always refused (`work`, `examine` — no question these worlds raise refers to a Site), **11 execute**.
The SHAPE comes from `H-62` (tier 0): an interior write is a consequence of an outcome, declared in
`write_matrix.yaml`'s Degree-keyed `writes` column. The column exists; the rows do not.
⚠ **BUT `H-62` IS NOT R-05's BLOCKER and this entry first implied it was.** `H-62` is
`kind: PRODUCER ×5` over **Person interior fields** (`convictions`, `beliefs`, `scar`, `axis_count`,
`stance`) and `requirements.yaml` assigns it to **R-06 and R-08**. **R-05's own `blocks:` is
`[W10-core, H-65, H-94]`** — none of which appears anywhere in this order. Writing 20 predicates
closes `H-62` only for those verbs that write a Person interior field.

### 5 · THE ANTONYM RESIDUE — and it is THREE cases, not six, and NOT six new verbs
⚠⚠ **THIS ENTRY ORIGINALLY INSTRUCTED A LAYER-1 VIOLATION AND THE CORRECTION IS THE ENTRY.** It read
*"the six antonyms… none of the 9 verbs exists… falsifier: the 9 appear in `verb_table.yaml` and
execute"*, citing `ED-IN-0210` Ruling 2. The nine spellings ARE absent — that fact checks out. **The
disposition does not**, and the successor was not cited:

- **`ED-IN-0211`**, `status: closed`, filed the same day *to adjudicate ED-IN-0210*: *"**THE ANTONYM
  CLOSERS ARE NOT SIX NEW ROWS**… Jordan's six names remain useful as the IDIOM for what each closure
  means; **they are not six rows**. `establish <-> abolish` is the one genuinely uncovered case"*, and
  *"the antonym half is real and **already spelled by `release`**."*
- **`01_AXIOMS.md`**: *"**CLOSURE IS NOT A VERB. IT IS A CONSEQUENCE OF OWNERSHIP.** Asking *which
  verb ends an `oblige`* is the wrong question."*
- **`04_CODE_ARCHITECTURE.md` row 14**: *"four closing verbs missing | **one `release` verb**,
  eligibility `own`, generic over kind."*
- **`release` EXISTS, `grade: "ruled"`**, `domain: [hold, commit, oblige, succeed, tie, knot]`, and
  executes in 15 of the 89 live worlds (20 acts over the 27 NPC cases, measured 2026-09-13).

So **WAIVE, DEPOSED, FRAY and LOOSEN name closures `release` performs today** — "relations stay
one-way" is false for `oblige`, `succeed`, `tie` and `knot`. ED-IN-0210's premise (*"grep release finds
nothing"*) was true on 2026-09-10 and falsified by a merge on 2026-09-11.

**THE GENUINE RESIDUE IS THREE:** `issue`↔RESCIND · `petition`↔WITHDRAW/DENY · `establish`↔ABOLISH.
`ED-IN-0211` names the **precondition** for the first two: the Petition/Dispensation carrier conflict
(`04:180` row 11 against `write_matrix.yaml:224`/`:112`). `utter` stays unpaired by §14 — a Proposition
is immutable.

### 6 · `Tenure.term` — `T-n`'s unbuilt half
**Verified 2026-09-13: `Tenure` carries `(id, subject, object, kind, since, until, degree, payload)` —
there is no `term`.** `until` is a hard end, not a declared term. MATTER already matures act-declared
stages at a later tick and stops if the maker is gone; the same branch on a `Tenure` is the change.
`T-o` constrains it: the opening act declares *when*, the **Seat** declares who may end it early.

### 7 · THE STRATEGIC LAYER — R-04
**54 of 143 cases unrepresentable**: 44 at faction scale, 10 at world. The loop runs at person,
settlement and realm only, so the half of the premise that fuses personal with strategic has no
expression in the head. `W28`'s `world` half is already decided and not escalated (`PLAN.md`: a
`world` case is ≥2 realm Rungs under a shared container). **XL, and it should follow 1–6, not precede
them** — a strategic layer over three anonymous people measures nothing.

---

## §3 · GENUINELY JORDAN'S — the only rows that survive `CLAUDE.md` §0's five-step test

| ruling | question | gates |
|---|---|---|
| **`ED-1051`** | `engine_clock`'s doc home — the temporal spine has `doc: null`. Reopened 2026-09-11 by an antagonist pass: the closure cited `04:137` for `port/`, and **`engine/season/port/` does not exist** | M3's G0 |

⚠ **`ED-IN-0210`'s FORK CAME OFF THIS LIST 2026-09-15 — RULED, NOT DROPPED.** Jordan: *"AN ORDER
CARRIES TERMS LIKE A DISPENSATION … The second option (no response verb) is REJECTED."* The ledger's
last row for that id reads `status: ruled`, `needs_jordan: false`, `jordan_decision: 2026-09-15`
(`registers/editorial_ledger_in.jsonl`), and an id's effective status is its LAST row. ⚠ **The
ruling does not make 19b buildable** — `dispatch` is blocked by `H-71`
(`engine/season/hole_register.yaml`, `tier: 0`, `grade: absent`, `owner: unassigned`), whose own
`unblocks:` reads *"9 of 32 verbs cannot be formed person-side — 8 remit-ONLY, plus `levy`"*, so no
run moves until it closes. ⚠ A handoff elsewhere says FIVE; the register says nine, and the register
is the surface with the falsifier (`test_no_person_can_choose_a_governance_verb_and_h71_is_why`,
which goes RED the day the hole closes). Read the register, not the cached figure.
Neither surface named the other; this note is where they meet.
`workplans/2026-09-11-reconciled-program.md`'s record defect naming this row is spent with it.

⚠ **`ED-WR-0011` IS NOT ON THIS LIST AND THIS ENTRY FIRST PUT IT HERE.** The ledger carries a SECOND
row under that id: `status: ruled`, `needs_jordan: false` — *"OI-05 RULED BY JORDAN, 2026-09-13…
**THIS IS OPTION A OF THE TWO THE ROW ITSELF DRAFTED**… Season-tick generation = **none**, which is a
RULING rather than a deferral."* Option A **is** the generator answer, so the question is closed, not
deferred. `ED-SE-0051`/E-1 (*matter only, or matter plus hearth capacity?*) is still open on the
settlements side and is still the same question's sibling.

⚠ **AND `ED-IN-0210`'s FLAG IS DELIBERATE, NOT STALE.** §4 below first listed it as
self-contradictory (`ruled` + still flagged) and *"closing on citation alone"*. It is `ruled` **for
its three rulings** and carries, in the same row, *"THE OPEN FORK (needs_jordan) — ARE `dispatch` AND
`comply` TWO SIDES OF ONE THING? … **NOT ESCALATED BY DEFAULT: it survives section 0's five tests**"*;
`ED-IN-0211` closes with *"the one live fork it adjudicated stays open on ED-IN-0210, **which keeps
needs_jordan**."* Clearing it would have deleted a live escalation.

## §4 · NOT WORK — bookkeeping debt, named so it is not mistaken for the list above

1. **The `needs_jordan` queue has NO INSTRUMENT, and four surfaces give four answers.** This row
   asserted "37 open / 7 contradictory" against this section's own rule that *every row names the
   command that measures it* — and it named a glob. Measured by hand on 2026-09-13 the count is
   **41, 51 or 77 depending on the predicate** (all-files / non-archive / any-status), and folding
   append-only rows to the latest per id gives 37. Against that, `2026-09-11-reconciled-program.md`
   (RATIFIED) measured **108 open / 158 flagged** on 2026-09-11, and this file's own 2026-09-10
   section reads 151/105 then 153/106. Position-1 closures have been landing, so a fall is real —
   **but no number here has a control, which is §0.1 pt 4 on this row's own terms.** The honest
   statement is: *the queue is large, it is falling, and the reconciled program's position 1 is the
   committed instrument for draining it.*
   What IS verified: `ED-PC-0015`…`ED-PC-0021` are `ratified` and still flagged — RBNI rows awaiting
   a BUILD, not a decision. **PC lane; not this lane's to close.**
2. **`workplans/workplan_v6_progress.yaml` is stale and it feeds a gate.** Its 7 junctures describe
   `.gd` work from the Godot/`mc_v18` era — `DomainActionSystem.gd`, `ChronicleLayerV30.gd`,
   `GameDirector.gd`. It is the input to the one `m1_acceptance` row that greens by editing a word.
   Per §0.2 that is a **board defect**, not a work item.
3. **`harness/populated.py` is not on the MILESTONE instrument's path** — and the first draft of this
   row said *"wired into no gate"*, which is false. `engine/season/tests` (a CI suite) carries
   `test_the_populated_world_is_not_everybody_in_one_room`, which builds the realm and asserts the
   cast size, a six-level rung ladder and that no building holds half the population; a second test
   proves it reads the roster rather than re-deriving. What is true is narrower: **no `corpus_run` or
   `register --requirements` path consults it**, so the numbers the milestone reports still come from
   the three-person world. Item 2 is what closes that.

## Next actions — where they live, 2026-09-17 (`ED-IN-0240`)

**This heading is load-bearing and must not be removed again:**
`tools/currency_consistency_check.py` fails without it, because *"nothing relays this file
automatically any more, so a missing heading loses the continuity surface rather than blanking a
banner."* The 2026-09-17 trim deleted it along with its dated bullets; this is the repair, and the
section is now a POINTER HUB rather than a log — which is the point of the trim.

| what you want | where it is |
|---|---|
| **the ordered work list** | **§2 · THE ORDER above.** It is ratified; start there |
| what is genuinely Jordan's | §3 above |
| bookkeeping debt that is not work | §4 above |
| this lane's open markers | `registers/handoffs/HANDOFF_<LANE>.md` — each live file now opens with an index of every open marker it carries, verbatim |
| the dated narrative that used to sit here | `registers/handoffs/HANDOFF_archive.md`, indexed below |

**Do not append a dated bullet here.** A next-action belongs in the work order if it is ordered work,
or in its lane's handoff if it is lane work. This section exists to route a reader, and a log grown
back under it is how root reached 20,417 tokens against a 4,000 cap.

## What NOT to do, in order of how much time it has cost before

1. **Do not build a guard.** `CLAUDE.md` §0.1 pt 5's predicate: a defect in an artifact load-bearing
   only on this repository's *process* is evidence the artifact **can be wrong without cost** — delete
   it or accept it, and **write nothing**. Apparatus outnumbers game, so a session that reads apparatus
   mints apparatus.
2. **Do not re-derive a measured hole.** Check `hole_register.yaml` and the requirement row's
   `measured:` block **first**. Two sessions have now independently "found" `H-71`.
3. **Do not read the ledger only as code and canon.** Four of fourteen proposals written on 2026-09-12
   turned out to execute or answer `ED-IN-0210`, ruled **two days earlier**. **Read
   `registers/editorial_ledger*.jsonl` for the fortnight before you start.**
4. **Do not run the full pytest suite after each edit** (§0.4). One file mid-session; the full gate
   **once**, at the close, with `-n auto`.
5. **Do not cache a requirement count** anywhere, including in this file. Run the instrument.

## The lane handoffs were split on 2026-09-13 — closed work lives beside them (`ED-IN-0221`)

Jordan: *"why don't you just hive off all closed IN work into its own document"* … *"tbh it's applicable
to all handoffs"*. Four lanes were split, **verbatim and proved lossless** (the two files' line multisets
partition the original exactly, checked against `git HEAD`):

| lane | was | live now | closed |
|---|---|---|---|
| **IN** | 129,964 | **72,652** | `HANDOFF_IN_closed.md` 59,890 |
| **MB** | 25,882 | **7,982** | `HANDOFF_MB_closed.md` 19,439 |
| **PC** | 25,631 | **15,044** | `HANDOFF_PC_closed.md` 11,772 |
| **SC** | 16,296 | **6,836** | `HANDOFF_SC_closed.md` 10,640 |

Re-derive any of it with **`python tools/verify_handoff_split.py`**, which also re-proves the partition.
**101,741 tokens of finished narrative left the orientation surfaces**; MB, PC and SC are now under their
20k cap and IN is honestly still over, its residue being genuinely unresolved material. Each live file
opens with an **index of what moved**, flagging units that contain imperative language, so a standing
order inside finished work is one file-open away rather than buried. **Read the live file; never orient
from a `_closed.md`.**

⚠ **THIS FILE WAS DELIBERATELY NOT SPLIT, and the reason is a false positive worth knowing.** The
predicate detects *unresolved-item* markers (`needs_jordan`, `[OPEN]`, `HELD`, `BLOCKED`, `TODO`,
`awaiting`). **Instructional content carries none of those by nature** — it tells you what to do rather
than tracking an open item — so a dry run classified the build order above as closed and would have moved
it out. Worse, this file's `## Next actions` mixes dated session narrative with **summaries of Jordan's
canon rulings** (TN 7, the universal degree bands, one resolver for d10 probability, `DECISIVE_OB` is
dead). Deciding where a ruling record belongs is a judgment call, not a mechanical move, so it was left
alone. At ~16.6k this file is still readable, which is what IN at 130k was not.

## Known-red on arrival, so you do not debug your container

`tests/valoria/test_forked_status.py` fails **two** tests on a **shallow** clone — the `FORK:` rows name
commits the checkout cannot reach. `cat .git/shallow` settles it in one command. Everything else in
`tests/valoria` is green (**1779 passed**, 2026-09-13).

### What landed 2026-08-27, and the one thing that moved output

Four commits. **Three were byte-identical and that was the point of each.** The evidence trail is
`registers/session_records/2026-08-27/` — two campaign captures and what they measure — and the
instrument is `tools/campaign_output_probe.py`, promoted out of `/tmp` where it had spent the
session licensing three commits.

| ED | what | output |
|---|---|---|
| **ED-IN-0199** | `engine/autoload/engine_clock.py` exists. `propagation_spec_v1.md` §O.1 has said since 2026-07-02 that engine_clock owns the tick composition; the module did not exist, `season.run_season` held the ordering, and the scheduler's two phase calls sat *inside* the ACTION phase's body. `next_tick()` left the scheduler in `_PHASE_ACTION` for all of accounting, and `keys.py` defers an `apply` on exactly that condition. | **identical** |
| **ED-SC-0031** | The ninth degree ladder — `sigma_leverage.degree`, the one the 2026-08-12 census missed — migrates to `dice_engine.degree_from_net`. | **MOVED** |
| **ED-SC-0032** | The injection seam: `dice_engine.BandExtension`. The contest's de-saturation rule leaves the engine for the subsystem that owns it and is injected by its wrapper. | **identical** |
| **ED-PC-0057** | The 40% covert-plate-killer ceiling is **abolished** (Jordan: *"stop arbitrary fiat capping"*). No replacement threshold. | n/a (test-only) |

**The ED-SC-0031 move is not a balance result.** Six of eight campaigns change winner at n=8;
`tools/balance_oracle.py` at n=120 per arm shows max |z| = 0.80 against a 1.96 threshold. Six
goldens were re-pinned on that basis. Full table in the session record.

### ⚠ POST-MERGE AUDIT (2026-08-27) — "are all decisions logged, ratified and propagated?"

Asked after #334 merged. **The answer was no, in three ways**, all now fixed. Recording the
result rather than only the fix, because each is a class this repo will hit again.

1. **A DUPLICATE ED ID SHIPPED.** The ceiling abolition was filed as `ED-PC-0041`, which had been
   allocated on 2026-07-29. `next_free` for PC read **57**; I filed 0041. CLAUDE.md §4 says read
   `next_free` and allocate THAT — never max+1, never a number you reasoned to. Renumbered to
   **ED-PC-0057** and propagated. **Nothing in CI cross-checks a lane's allocated ids against its
   pointer**, which is why a merged PR carried it; the audit was a one-line Python script.
2. **TWO JORDAN RULINGS WERE RECORDED NOWHERE.** A grep for their own words returned zero files:
   *"one faction write mechanism"* and *"key contracts and module contracts etc need to be
   explicitly defined in a centralized hierarchical manner"*. Both were given in the same
   conversation as "one degree ladder", which drew four commits. **The shape to watch: a ruling
   delivered alongside another, and satisfied by the tree's current state, is the one that gets
   silently dropped** — nobody decides against it, it just never becomes a work item.
   → **ED-FA-0038** (executed: the faction-write ruling was already substantially true, so what
   landed is the guard that was missing) and **ED-IN-0200** (ruled, NOT executed, filed `open`).
3. **PRE-EXISTING, NOT MINE, RECORDED NOT FIXED:** six duplicate ids in the IN ledger
   (`0012, 0013, 0016, 0029, 0149, 0162`, all July–August). CLAUDE.md §4 documents 0012/0013;
   the other four are undocumented. Not touched — the ED-306 precedent §4 cites says merged
   ledger lines are not rewritten unilaterally.

**The one gap left open by this audit:** no gate checks ledger ids against `id_reservations.yaml`.
A ~10-line test would have caught (1) and (3). It is not written here because minting a guard is
governed by §0.1 pt 5's predicate, and an id-allocation checker is load-bearing on this
repository's process rather than on the game — the predicate's own worked-example exclusion. The
honest disposition is that this class recurs and is cheap to detect, and that the predicate says
not to mint the guard. **Flagged for Jordan as a genuine tension, not resolved by me.**

### THE HIGHEST-VALUE WARNING FROM THIS SESSION

**ED-SC-0032 broke `tools/balance_oracle.py` and nothing caught it.** Moving `degree` out of the
engine left the oracle's arm reading `SL.degree`, so the default invocation raised AttributeError.
That is the instrument CLAUDE.md §7 names as *the* campaign-level balance control, and the one
whose n=120 run had licensed the previous commit's six golden re-pins — disabled by that commit's
own successor, found by an adversarial pass rather than by anything automated.

**The cause generalises and is the thing to carry forward: a deliberately-uncalled instrument has
no freshness relationship to the code it measures.** The oracle is not a CI gate on purpose (240
campaigns, ~13 min) and that is still right — but "not a gate" was silently doing the work of "not
tested at all". `tests/valoria/test_balance_oracle_arms.py` now constructs both arms and asserts
they band differently; it runs zero campaigns and costs milliseconds. **If you add another
deliberately-uncalled instrument, add its liveness test in the same commit.**

### Cross-lane items now OPEN

- **[PC — the big one] Derive Ob from the DEFENDER.** Jordan, 2026-08-15: Ob is *"their
  corresponding score/2 plus whatever specific modifiers exist for them in that instance"*, and
  `DECISIVE_OB` is dead. The sequence is settled and is the opposite of the obvious one: **derive
  Ob first, THEN combat's bands migrate.** This is genuine new mechanism, it is the last declared
  HOLD in `tests/valoria/test_degree_ladder_single_owner.py`, and it is what makes guandao reach
  47.5% on its own merits. The fiat ceiling that stood in its way is gone. See `HANDOFF_PC.md`.
- **[IN] §4.1's drain topology is NOT implemented.** `engine_clock.run_tick` calls
  `run_accounting` RAW — the shape `propagation_spec_v1.md` §4.1 explicitly names as its rejected
  earlier draft ("that was unbounded"). Bounded today only because accounting emits no Keys.
  Closing it is Phase E and is blocked on **R-1** (the D.6 double-count) and **R-4** (ORD-3
  observer ordering). See `HANDOFF_IN.md`.
- **[IN] ~38 flow-skeleton `file:line` anchors were re-based +5** when `module_contracts.yaml`
  grew a composition role. That preserves each anchor's existing offset and nothing more. An
  adversarial sample of 23 found **12 already stale** by larger, non-uniform offsets. **Nothing in
  CI validates a `.md` anchor's CONTENT** — `test_flow_skeletons` checks only symbol proximity.
  Repairing them is bounded but separate; a partial repair would present the unsampled remainder
  as verified.
- **[FA/WR] The parliamentary bridge's shut-out set has taken three values** under three unrelated
  mechanic changes (`{'Hafenmark'}` → `set()` → `{'Church'}`). That is evidence the property
  "the spine can eliminate a faction" tracks the seed, not the spine. Only ever measured at
  n=8/seed-42. Settling it needs the n≥100 arm.
- **[SC] The seam has exactly one consumer.** `PoolDesaturation` is the only `BandExtension` in
  the tree, so its contract ("veto the top band, nothing else") is proven by hostile probes rather
  than by a second real user. Expect that power to be what comes under pressure when a second
  subsystem wants an extension; widen it by ruling and ledger entry, never by convenience.

### Rulings received 2026-08-27, all executed or accepted

Recorded verbatim in the `RULINGS` block at `tests/valoria/test_degree_ladder_single_owner.py`,
which is now the single home for the degree-ladder rulings — it exists because ED-SC-0032 nearly
deleted its own authority (removing the HELD entry that was the *only* in-tree record of the
ruling authorising its shape).

1. *"so plan to resolve it then if you know what to do!"* → the injection seam. **Executed.**
2. *"yes accept. if you don't have enough dice you don't have enough dice"* → a pool-2 contest can
   never resolve Overwhelming. **Accepted, settled, not to be re-raised.**
3. *"dude guandao not being able to hit 47.5% on its own merits is fucked up. stop arbitrary fiat
   capping"* → the 40% ceiling. **Abolished**, and it **overrode a sequencing objection I had
   raised** — recorded rather than dropped, because the objection was about convenience and the
   ruling is about whether the thing should exist.

---


## ⚠ DATED NARRATIVE MOVED OUT — the index, 2026-09-17 (`ED-IN-0240`)

**11 units, 9,265 tokens** of dated narrative moved to `registers/handoffs/HANDOFF_archive.md`, verbatim and in order — the destination that file has declared since 2026-07-08 ("*frozen archive of pruned HANDOFF.md narrative; grows by archival, not editing*"). **Every open marker they carried is reproduced here verbatim.** Four of them were already titled `WAS CURRENT`.

**What deliberately did NOT move:** THE WORK ORDER (ratified, and the thing this file exists to point at), `What NOT to do`, `Known-red on arrival`, the lane-split pointer, and the RULING RECORDS — *"do not re-raise"*, the closed ruling agenda, the resolver architecture, faction stats, the withdrawn apparatus section, standing state. `ED-IN-0221` found that deciding where a ruling record belongs is a judgment call rather than a mechanical move, and that is still true.

| newest date | markers carried | tokens | unit |
|---|---|---|---|
| 2026-09-10 | `BLOCKED` | 574 | ⚠ WAS CURRENT — 2026-09-10 (later) · ARC 1 HAS LANDED. ARC 3 IS LARGELY UNBLOCKED; ONLY  |
| 2026-09-10 | `BLOCKED` `needs_jordan` | 2,330 | ⚠ WAS CURRENT — 2026-09-10 · U1–U10 is ARC 3, and Arcs 1 and 2 are its precondition (IN  |
| 2026-09-10 | `needs_jordan` | 527 | 📋 2026-09-10 — the blocking-rulings queue measured (ED-IN-0208, all lanes) |
| 2026-09-06 | `HELD` | 480 | ⚠ WAS CURRENT — 2026-09-06, PR #373 · the proceedings subsystem owns all social contests |
| 2026-09-06 | — | 1,136 | ⚠ WAS CURRENT — 2026-09-04, PR #368 |
| 2026-08-27 | — | 137 | ⚠ WAS CURRENT — 2026-08-27 |
| 2026-08-25 | — | 655 | Prior — 2026-08-25 |
| 2026-07-08 | — | 572 | History |
| 2026-08-23 | `HELD` `SUSPENDED` `needs_jordan` | 1,486 | Next actions |
| 2026-08-19 | `BLOCKED` `PARKED` `needs_jordan` | 1,035 | 2026-08-19 — build the game; `done` means it runs (history; superseded by THE WORK ORDER |
| 2026-08-18 | `BLOCKED` `HELD` | 333 | 2026-08-18 — `proposals/2026-08-18-next-session-handoff.md` (history; was "READ SECOND") |

## RULINGS AND STANDING STATE — do not re-raise any of these

These were `###` subsections of a `## Next actions` head whose dated bullets moved to the archive (index above). They are kept, and they need a parent heading of their own: each one records a ruling or a standing prohibition, not a tracked item.

### Ruled and landed — do not re-raise

- **Jordan's ruling session landed 2026-08-14 (PR #311, ED-IN-0187/0188).** The **degree ladder** is
  single-owned by `degree_from_net` in `engine/autoload/dice_engine.py` and reads the **margin**
  (net − ob): ≥3 Overwhelming, ≥1 Success, [0,1) Partial, <0 Failure. The Ob-scaled 2×Ob bar, the
  PP-232 floor and the Ob-20 exception are **ruled out**. **Faction actions roll d10** through
  `sigma_leverage`; the d6/4+ convention is gone. `CONQUEST_MIN_MIL` is deleted.
  ⚠ **Behaviour changed:** a roll clearing zero but falling far short used to read Partial and now
  reads Failure. Six seeded-campaign goldens moved, each re-recorded with its cause.
- **Mass battle: the canon question is CLOSED and has been since 2026-08-03 (J2).** Canon is
  `tests/sim/mass_battle/` (11,269 lines, ~30 modules — the big one). `systems/mass_battle/sim/`
  (2,385 lines) is retired but still runs the live campaign until `faction_action.py` migrates.
  J2 is recorded at `systems/mass_battle/sim/__init__.py`. **Five independent audit lenses re-raised
  this as open in August because `CURRENT.md` narrated the tension twice.** That narration is now
  deleted. If you find yourself about to file it again, read the `__init__.py` header first.

### The ruling agenda is CLOSED — ruled 2026-08-14, do not re-raise

**Corrected 2026-08-15 (ED-IN-0191).** This section previously listed Q1b/Q4/Q5/Q6/Q7 as *"open
and needing Jordan"*. **They were already ruled when it was written.** PR #312 (ED-IN-0185, flipped
`proposed` → `ruled`) records Jordan's verbatim answers; I wrote this section without them and
rebuilt the exact T5 trap the assessment had just named — a settled ruling re-surfaced as open
work, in the one section the SessionStart banner reads. The verbatim answers live in `ED-IN-0185`
and in the banner on `audit/2026-08-14-five-lens-repo-assessment/01_plan.md` §2. Read those, not a
paraphrase.

| Q | Ruling (Jordan, verbatim where short) | State |
|---|---|---|
| Q1a | CURRENT.md history: *"a delete. only include instructions to read most current commits, and where to read registers/logs/indexes"* | **EXECUTED** (ED-IN-0189) |
| Q1b | *"b generate, never hard code"* — the head-per-subsystem table | **RULED, not executed** |
| Q2 | *"3 or more is always overwhelming"*; a met-but-not-exceeded obstacle is a partial | bands **EXECUTED**; the **score/2 obstacle derivation is wired nowhere** — the largest outstanding piece |
| Q3 | *"d10 always using fractional dice and fractional obstacles, sigma leveraged"* | d10+sigma **EXECUTED**; ⚠ **fractional DICE are not implemented** — `roll_net_continuous` does `int(round(pool))`, so pools are still whole dice and only the *result* is fractional |
| Q4 | *"b"* — blanket-mark historical-resolves-at-fork, checker verifies format | vocabulary + freeze gate **EXECUTED** (ED-IN-0188, ED-IN-0190); the **433-citation sweep is not done** |
| Q5 | *"chunk as per a, just ensure you have a companion index for them"* — numbered continuation, full file frozen, **plus a companion index** | **RULED, not executed** |
| Q6 | *"restore"* — CLAUDE.md §5–§7; plus *"q6 active"* for the lane | lane **ACTIVATED** (ED-GO-0001); ⚠ **the §5–§7 restore is NOT done** — 327 dangling citations across 176 files |
| Q7 | *"it will be 10 attributes, and delete the code that blocks itself from being ported as that is stale"* | **RULED, not executed.** The roster ships **nine** today; **the tenth is UNNAMED** — naming it is the workshop, the count is not |

### Resolver architecture — RULED 2026-08-15

Jordan, in session. These close the two HELD degree sites and set the extension pattern.

- **ONE resolver for all d10 probability.** Rolls are adjusted by **standard deviation (sigma)** —
  that is our word; "volatility" is used nowhere. `engine/autoload/sigma_leverage.py` is the sigma
  surface, `engine/autoload/dice_engine.py` owns the ladder.
- **TN 7 — "a roll of 7 or higher is a success"**, equivalently "above 6". Both readings were in
  circulation; they are the same rule and the ambiguity is now closed at the owner. **No constant
  changed.** ~~TN 6/7/8 (Controlled/Standard/Desperate) remains canon as a *situational* scale.~~
  ⚠ **SUPERSEDED 2026-08-25 — Jordan, verbatim: "TN7 always. Never change TN anywhere ever."** There
  is no situational scale and no other TN. A varying difficulty is an **Ob**, never a TN. Enforced in
  code, not prose: `engine/autoload/dice_engine` raises on any other value, and
  `tests/valoria/test_tn7_always.py` fails on a re-introduction (ED-IN-0196, ED-MB-0066).
- **All weapons are TN 7** — "now that we have a physics engine". Weapon speed is carried by the
  physics (reach, mass, percussion authority, recovery), never by the TN. ⚠ The engine **already**
  did this (`core.py:46`, `TN = SL.TN_STANDARD`); the per-weapon TN 5–8 existed only in prose and is
  corrected.
- **Degree bands are universal.** Failure below Ob · Partial from Ob to Ob+1 · Success at Ob+1 or
  more · Overwhelming at Ob+3 or more. This is exactly what `dice_engine.degree_from_net` already
  implements, so **the ladder itself needs no change** — only the systems that bypass it.
- **No system keeps its own bands.** Where a system genuinely needs a modification, the **wrapper
  injects the engine** so the change is clean and visible — never a private re-banding.
- **`DECISIVE_OB` is dead** — *"stupid as hell … Ob should be determined by your opponent more than
  anything"*. Combat's fixed Ob of 3 goes; the obstacle becomes the opponent's **score/2 plus that
  instance's modifiers**.

**THE SEQUENCE MATTERS AND IS COUNTER-INTUITIVE.** Combat is *not* migrated bands-first. Derive Ob
from the defender **first**, then the owner's ladder applies directly. `core.py`'s own docstring
predicted this: calibrating against the fixed-Ob form first "would be work thrown away". Both HELD
entries in `tests/valoria/test_degree_ladder_single_owner.py` now record the ruling and this order;
delete a HELD entry when its migration lands, not before.

**Not yet executed:** the combat Ob derivation + band migration (PC lane, a real redesign with a
measured balance delta — Jordan: migrate, measure, **report before tuning**), and the
`sigma_leverage.degree` migration (flips `degree(3,3)` from 2 to 1, pinned by 151 groundup tests and
`_kernel_tests.py`). Also still open: **fractional dice** (`roll_net_continuous` does
`int(round(pool))`).

_(The two HELD degree sites that previously sat here as needing Jordan are **RULED** — see the
section above. Nothing on the ED-IN-0185 agenda is awaiting a decision.)_

### ✅ PARTLY RULED 2026-08-23 — faction stats (asked 2026-08-15, ruled 2026-08-23)

> **Jordan ruled two of the four calls below. Read this box before the evidence, which is preserved
> as it stood when the question was asked.**
>
> * **Call (1) — which roster.** RULED: **"Legitimacy is a base."** `fac.legitimacy` is declared in
>   `references/descriptor_registry.yaml` and bound to the `Faction.L` field. The roster is **six**
>   on both sides; the 5-vs-6 disagreement below is closed.
> * **Call (4) — is the scale 0–7 or 1–7, uniformly.** RULED: **"Influence can be 0."** Uniformly
>   **0–7**. This supersedes ED-IN-0029's Influence floor of 1, so the inconsistency the evidence
>   below calls out as deciding "whether a faction can present a zero obstacle" is resolved — it can.
> * Jordan's rationale, which is what makes call (1) a change of model rather than a reversal:
>   *"now that we're using continuous, we don't have to worry near as much either as we can just
>   aggregate these stats as opposed to weird derivations."*
>
> **STILL OPEN — calls (2) and (3), and they are not touched by the above:**
> * **(2) is Mandate a base stat or derived from settlement L/PS.** Still derived. `fac.legitimacy`
>   is NOT Mandate, and the ruling does not make Mandate a base stat. ⚠ The code stores Mandate *as*
>   `Faction.L` in places (`parliamentary_bridge` still comments *"Mandate == Faction.L pre-LPS-1"*),
>   so what is settled is that the FIELD is a declared descriptor with declared bounds — not what
>   every call site writing it means. That conflation is ED-FA-0004 and is still open.
> * **(3) does Treasury exist separately from Wealth.** Untouched.
>
> Wired in `ca0ff0c`; supersessions recorded in `registers/supersession_register.yaml`.

The evidence below is preserved AS ASKED (2026-08-15) and is deliberately not rewritten — it is the
record of what was put to Jordan. Where it states the roster as 5 or Influence as 1–7, read the box
above.

**The registry and the code disagree about what a faction *is*.**

| | Roster |
|---|---|
| `references/descriptor_registry.yaml` declares **5** | Influence (1–7) · Wealth (0–7) · Military (0–7) · Intel (0–7) · Stability (0–7) |
| `engine/autoload/game_state.py` implements **6** | `L` · `Sta` · `W` · `I` · `Mil` · `intel` |

The conflict is `L`. The registry's own note says **"Mandate is a size-weighted derived aggregate of
settlement L/PS — NOT a base attribute."** The code stores Mandate *as* the base scalar `Faction.L`.
That is ED-FA-0004, still open.

**Three things exist only in comments, never as code:** `Treasury`, the Mandate formula
`7T/(T+6)`, and the per-settlement L/PS → Mandate pipeline. `Faction` has `W` (Wealth) and no
Treasury; whether those are the same thing is undecided.

**The registry's cited source is gone** — `engine/params/factions/stats_1_7_scale.md` was evacuated
2026-08-05 (resolves at fork `c451bcb`).

**Why this now matters more than it did:** obstacles are ruled to be **score/2 plus modifiers**, so
the faction stat roster *is* the faction obstacle surface. A 0–7 stat yields obstacles 0–3.5, and
**Influence is 1–7 while every other stat is 0–7** — that inconsistency decides whether a faction can
present a zero obstacle.

**The calls:** (1) which roster — the declared 5, the coded 6, or another; (2) is Mandate a base stat
or derived from settlement L/PS; (3) does Treasury exist separately from Wealth; (4) is the scale
0–7 or 1–7, uniformly.

### ⛔ WITHDRAWN 2026-08-19 — this section used to hand out apparatus work as "no ruling needed"

It listed tracks **B–E** of `audit/2026-08-14-five-lens-repo-assessment/01_plan.md` — owner-in-code
sweeps, gate-perimeter widening, `sys.path.insert` governance across 131 test files, vocabulary
entries — under the heading *"Open and agent-executable — no ruling needed"*. Every item is
audit-sourced work on this repository's own machinery, pre-authorised for any session that read
this file. That is precisely the T3 carrier CLAUDE.md §0.3 describes, sitting in the continuity
surface, and it is now excluded twice over: by §0's selection term (work is this session's work only
if Jordan asked this session, or it traces to an open M1 juncture — none of B–E does) and by §0.1
pt 5 (the artifacts are load-bearing only on process). **Do not take this work. Do not restore this
section.** The plan file still exists if a human ever wants it.

**One item from it survives, because it is the opposite of apparatus** — it is engine code on the
critical path of M1 juncture 1, which is why the board now names it as the increment:

- **The largest unimplemented piece of the #311 ruling:** obstacles as score/2 plus modifiers is
  **wired nowhere** (`engine/autoload/dice_engine.py:118-123` says so itself). Paired with
  fractional dice pools (`sigma_leverage.py:284` still does `int(round(pool))`). See the board.

### Standing state

- **M1 (one playable season) — 0 of 7 junctures done.** Junctures 1–2 have no owning design doc at
  all (`domain_actions`). Board: `workplans/workplan_v6_progress.yaml`, refreshed 2026-08-14.
- **Of the 25 commits before #311, 19 were IN-lane infrastructure.** The repo's own assessment of
  that period: *"instrumented the disease more than it cured it."* Weigh a new instrument against
  that before building one.
- **~121 ledger items are flagged `needs_jordan`** across the lanes (IN 29, SE 23, SC 17, FA 15,
  flat 14, PC 9, MB 8, FI 3, WR 1). Re-raising a settled one costs more than leaving one unruled.
- **ID protocol unchanged:** the flat `ED-NNNN` sequence is FROZEN at ceiling `ED-1096`. All new EDs
  are `ED-<LANE>-NNNN` from `references/id_reservations.yaml`'s `lane_ids` — read `next_free`,
  allocate, bump, co-commit. Never max+1.
