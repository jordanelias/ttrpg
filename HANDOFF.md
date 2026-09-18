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

**`workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3 IS THE SINGLE PLAN.** If you are choosing what to do next, open it — and start at its **§3.1 · START HERE**, which names the next three in order.

⚠ **AMENDED 2026-09-18 (`ED-IN-0253`) ON JORDAN'S INSTRUCTION — *"I need one single clearly defined plan"*.** The order was spread over five surfaces; it is now on one. The contested-ownership note in that file's own `## Status:` line is CLOSED, `valoria_master_workplan_v7.md:16`'s open ORDER collision is CLOSED, and the arc-sequence spine, the governance build order and the gather's `05_THE_ORDER.md` are subordinated to it as CONTENT owners. **No position number changed** and §3.4 maps every folded item, so no citation dangles. §3 now carries a `STATE` column that is execution-bound per `CLAUDE.md` §0.2 — `DONE` means something ran it — and §3.3 records the five items that landed 09-17/18, **two of which do not affect the game yet and are marked `DONE·INERT` rather than done.**

**Everything this section used to argue moved to `workplans/2026-09-13-work-order.md` on 2026-09-17 (`ED-IN-0242`):** why Arc 2 comes first, the live ownership collision its status line records, and the warning that `requirements.yaml`'s `measured:` blocks understate progress and carry four mutually inconsistent R3 figures. All three are about the ORDER or about an INSTRUMENT, and neither is what a continuity index is for.

## §1 · THE CENSUS — how to count the open items, so this order is known to be complete

⚠ **THE NUMBERS THAT USED TO BE QUOTED HERE ARE GONE, AND THAT IS THE FIX (RULED by Jordan,
2026-09-17).** Verbatim: *"anything that gets pulled up frequently cannot be hard coded with
numbers/values/dates."* This file is read at the start of every session, so a quoted count is wrong
from the next commit onward and **a stale census defeats this section's own purpose** — it makes an
order look complete when it is not. The snapshot is preserved verbatim in
`registers/handoffs/HANDOFF_archive.md`; what belongs here is the INSTRUMENT.

**Every row already named its instrument, which is why this repair costs nothing.** Run the
command; do not trust a transcription — and note that this file's own warning below records that
`requirements.yaml`'s `measured:` blocks understate progress and that it carries **four mutually
inconsistent R3 figures**, so the numbers removed here were already known-unreliable.

| surface | count it with | where the fact lives |
|---|---|---|
| requirement rows (**THE NINE**, ruled `ED-IN-0204`) | `python -m engine.season.harness.register --requirements` | `engine/season/requirements.yaml` |
| holes | `python -m engine.season.harness.corpus_run` | `engine/season/hole_register.yaml` |
| verbs — predicate/effect coverage | `python -m engine.season.harness.corpus_run` | the verb table it reads |
| cases — unrepresentable scales | `corpus_run` → its `unrepresentable scales:` line | same run |
| `needs_jordan` ledger rows | `grep -c '"needs_jordan": true' registers/editorial_ledger*.jsonl` | `registers/editorial_ledger_<lane>.jsonl` |
| M1 junctures on the board | `python tools/m1_acceptance.py --summary` | `workplans/workplan_v6_progress.yaml` — ⚠ hand-edited, DOC-DERIVED, bookkeeping not evidence (§0.2) |

## §2 · THE ORDER — and the seven units' detail

**Order:** the reconciled program §3, above. **Detail — `file:line`, measured arms with controls,
falsifiers, and the item → position mapping:** `workplans/2026-09-13-work-order.md`.
⚠ **Do not re-inline it here** (`ED-IN-0242`): it is unit content, it has an owner, and it was four
times the size of everything else in this file.

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
`workplans/2026-09-18-governance-settlement-behaviour-plan.md`'s record defect naming this row is spent with it.

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
   append-only rows to the latest per id gives 37. Against that, `2026-09-18-governance-settlement-behaviour-plan.md`
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

**This heading is load-bearing** — `tools/currency_consistency_check.py` fails without it.

| what you want | where it is |
|---|---|
| **the ordered work list** | **§2 · THE ORDER above.** It is ratified; start there |
| what is genuinely Jordan's | §3 above |
| bookkeeping debt that is not work | §4 above |
| this lane's open markers | `registers/handoffs/HANDOFF_<LANE>.md` — each live file now opens with an index of every open marker it carries, verbatim |
| the dated narrative that used to sit here | `registers/handoffs/HANDOFF_archive.md`, indexed below |

**Do not append a dated bullet here** — a log grown back under this heading is how root reached
five times its cap. Ordered work goes in the reconciled program; lane work in its lane's handoff.

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

## The lane handoffs, and what is where

**Read root `HANDOFF.md` AND your lane's `registers/handoffs/HANDOFF_<LANE>.md` — nothing relays either automatically (`CLAUDE.md` §1).** Each live lane file opens with an index of every open marker it carries, verbatim; the dated narrative behind those markers is in its `_history` sibling and the finished work in `_closed` (`ED-IN-0221`, `ED-IN-0240`). The full rationale for the split moved to `registers/handoffs/HANDOFF_archive.md` (`ED-IN-0242`).

## Known-red on arrival, so you do not debug your container

`tests/valoria/test_forked_status.py` fails **two** tests on a **shallow** clone — the `FORK:` rows name
commits the checkout cannot reach. `cat .git/shallow` settles it in one command. Everything else in
`tests/valoria` is green (**1779 passed**, 2026-09-13).

## ⚠ DATED NARRATIVE MOVED OUT — the index, 2026-09-17 (`ED-IN-0240`)

**The dated narrative below moved to** `registers/handoffs/HANDOFF_archive.md`, verbatim and in order — the destination that file has declared since 2026-07-08 ("*frozen archive of pruned HANDOFF.md narrative; grows by archival, not editing*"). **Every open marker they carried is reproduced here verbatim.** Four of them were already titled `WAS CURRENT`.

**What deliberately did NOT move:** THE WORK ORDER (ratified, and the thing this file exists to point at), `What NOT to do`, `Known-red on arrival`, the lane-split pointer, and the RULING RECORDS — *"do not re-raise"*, the closed ruling agenda, the resolver architecture, faction stats, the withdrawn apparatus section, standing state. `ED-IN-0221` found that deciding where a ruling record belongs is a judgment call rather than a mechanical move, and that is still true.

| newest date | markers carried | unit |
|---|---|---|
| 2026-09-10 | `BLOCKED` | ⚠ WAS CURRENT — 2026-09-10 (later) · ARC 1 HAS LANDED. ARC 3 IS LARGELY UNBLOCKED; ONLY |
| 2026-09-10 | `BLOCKED` `needs_jordan` | ⚠ WAS CURRENT — 2026-09-10 · U1–U10 is ARC 3, and Arcs 1 and 2 are its precondition (IN |
| 2026-09-10 | `needs_jordan` | 📋 2026-09-10 — the blocking-rulings queue measured (ED-IN-0208, all lanes) |
| 2026-09-06 | `HELD` | ⚠ WAS CURRENT — 2026-09-06, PR #373 · the proceedings subsystem owns all social contests |
| 2026-09-06 | — | ⚠ WAS CURRENT — 2026-09-04, PR #368 |
| 2026-08-27 | — | ⚠ WAS CURRENT — 2026-08-27 |
| 2026-08-25 | — | Prior — 2026-08-25 |
| 2026-07-08 | — | History |
| 2026-08-23 | `HELD` `SUSPENDED` `needs_jordan` | Next actions |
| 2026-08-19 | `BLOCKED` `PARKED` `needs_jordan` | 2026-08-19 — build the game; `done` means it runs (history; superseded by THE WORK ORDER |
| 2026-08-18 | `BLOCKED` `HELD` | 2026-08-18 — `proposals/2026-08-18-next-session-handoff.md` (history; was "READ SECOND") |
## RULINGS AND STANDING STATE — do not re-raise any of these

These were `###` subsections of a `## Next actions` head whose dated bullets moved to the archive (index above). They are kept, and they need a parent heading of their own: each one records a ruling or a standing prohibition, not a tracked item.


**The bodies moved to `registers/handoffs/HANDOFF_archive.md`; the PROHIBITION is the load-bearing half and it is here.** Do not re-raise any of these — open the archive only if you need the reasoning behind one.

| ruling / standing prohibition — DO NOT RE-RAISE |
|---|---|
| Ruled and landed — do not re-raise | 318 |
| The ruling agenda is CLOSED — ruled 2026-08-14, do not re-raise | 565 |
| Resolver architecture — RULED 2026-08-15 | 771 |
| ✅ PARTLY RULED 2026-08-23 — faction stats (asked 2026-08-15, ruled 2026-08-23) | 867 |
| ⛔ WITHDRAWN 2026-08-19 — this section used to hand out apparatus work as "no ruling ne | 352 |

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
