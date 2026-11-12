# WR · A chronicle that says what each act was about, starts from what closed, and breaks ties by rarity

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — `world_q.projection` / `witnessed` / `PersonProjection` are deleted by `17_CENSUS_C1A_01_deletion_batches.md` D2: the one typed per-person reading is `account` (the person's own ledger) and the host-side `receipt` of `11_GO_player_surface_contract_B.md` §3–§4. The focalized telling (R-32) is therefore a selection over `account`'s rows, marked `saw` or `inferred` from each row's own source, and never over `w.log`; nothing else in this proposal changes.

## Status: PROPOSED

Carries finding F-WR-14 of `audits/09_WR_audit_addendum_B.md` (§3.3), its resolutions R-28 and R-32, its
§2.2 correction 8, and step 2 of its §3.8. Evidence ids (EB-nn) are that file's §9; E-nn the first audit's.

## What it changes in `engine/season/` at runtime

**Nothing.** `harness/chronicle.py` is read outside the simulation and imported by nothing in the loop
(its own `tests/test_in37_chronicle.py` asserts the content hash, log length and write list are unchanged
by a render).

## The problem

`harness/chronicle.py` is a selection stage and not a telling (§3.3's table, EB-04):

1. **No line says what the act was about.** A line is `season · actor · verb · emitted kinds · answers n`
   (`:160-161`). The seed-0 render is `conceal → create_record → create_record → create_record`
   (`runs/WR/chronicle_s0_k2.txt`): concealing what, recording what, is not printed. Apparatus T06.Q1
   (Juul: a retelling that only recounts moves loses the system).
2. **The pick starts from depth, not from what closed** (`deepest_chain`, `:86-104`: "the first-logged act of
   maximal depth"). The Events a reader would call story (a death, a razing, a determination) end a
   rendered chain only by accident. Apparatus E12 (Labov via Ryan via Short: start at the most interesting
   final event and chain back).
3. **Ties go to the smallest act id** (`:18`, `:90`), an order of the mint and not of the story. Apparatus
   E10.Q1.
4. **It has no viewpoint.** It reads `w.log` and `act_of`, world truth. The focalized substrate exists and is
   unused: `queries/world_q.py:4374-4441`, `witnessed(w, pid)` and `projection(w, pid)` (PC-06 S-2, L-1),
   a person's own claims and the Events he holds evidence of having witnessed, as copies with `observed`
   and `ending` emptied. `witnessed` also lists a trail Event the person *inferred* from a finding
   (FI-03's two-cause deposit) beside those he saw, an open contract question its docstring records.

## The resolution, decided

- **"About" has two owners, by line kind (R-28).** An act line's subject is `state/carriers.py::subject_of(act)`
  (`:949`, "THE ONE READ"). An Event line's is `state/attribution.py::anchor_of(w, e)` (`:105`). `Event` has no
  `subject` field since G1b (`carriers.py:259-268`; H-107 closed), and nothing here may reintroduce one by
  reading the write call's `subject=` keyword off the log. A subject id is printed through the same
  `_name` the actor uses, so a person reads by name and a Rung, Office or Record by id.
- **The end of a chain is a close, defined structurally.** The pick's end is an act whose own Event writes
  a closing cell (`arc.CLOSE_CELLS`, declared by `09_WR_B_readings_of_closure_and_tension.md` edit 1); when
  several do, the rarest Event kind in the seed's log wins, then the latest season, then log order. When no
  act closed anything, the pick falls back to today's depth rule and the header says so.
- **Ties walking back are broken by rarity of the antecedent's verb within the seed**, then by log order.
  Wildermyth's repeat suppression (R8: an event becomes a quarter as likely each time it recurs) is the
  shipped form of "prefer the rare"; the act-id order is retired.
- **A focalized telling is a selection over `projection(w, pid)`, never over `w.log` (R-32).** This
  proposal adds only the flag that runs the same pick over one person's witnessed Events and marks each
  line `saw` or `inferred` (an Event among a `claim.deposited`'s causes beside a finding is `inferred`).
  The journal NM-W5 owes (CHAR, GO) composes on this; it is not built here.

## The edits (`engine/season/harness/chronicle.py`)

1. `lines()` gains an `"about"` field: `_name(persons, subject_of(act))` when the act has a subject, else
   `""`. `render()` prints it after the verb: `<actor> <verb> <about> | emitted …`.
2. `deepest_chain(rows)` keeps its signature for `--pick depth`; a new `closing_chain(rows, log, act_of)`
   is the default pick (`--pick close`), choosing the end as above and walking back with the rarity rule.
   Both are pure over their arguments, so the existing planted tests keep their meaning.
3. `--focus <pid>` (no default) restricts the rows to acts any of whose Events are in `witnessed(w, pid)`
   and tags each line `saw` / `inferred`. The header names the focalizer: `chronicle … focus=<pid>`.
4. The module docstring's THE PICK paragraph is rewritten to the rule above; the `[ASSUMPTION]` tag on
   CR-68's selection is kept.

`tools/ci_sim_fabrication_check.py`'s scope is unchanged by these: `--seed` and `--seasons` stay required.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2
PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 1 --seasons 6
python -m pytest engine/season/tests/test_in37_chronicle.py -q      # the covering file, at the close
```

Passes when: (1) the seed-0 render names, on every line with a subject, what was concealed or recorded;
(2) a planted `detain → determine → fight` with a death reads back from the death, three lines, three
subjects; (3) at seed 1, six seasons, the rendered chain ends on one of the closing Events EB-02 lists
(`person.died`, `matter.determined`, a `tenure.closed`) and not on an `utter`; (4) a planted pair of equal-
depth antecedents, one verb seen once and one seen fifty times, walks back through the rare one;
(5) `--focus` on a planted witness who saw one act and inferred another tags them `saw` and `inferred`;
(6) the existing hash-and-write-list test is green unchanged.

## The falsifier

A rendered line whose `about` names an id that is not the act's `subject` operand (a second reading of
"subject" crept in); a `--pick close` render at a seed with a death that does not end on it; a `--focus`
render containing an Event the focalizer holds no deposit for.

## NERS reading

- **N.** `04` §C.11's "why did that happen?" is answered today with who and when and not what. Without the
  subject, the reader test (§3.8 step 6, apparatus D7) cannot pass on any seed. Holds top-down (the seed's
  story) and bottom-up (one person's account).
- **R.** Starting from closes makes the no-player half's endings the telling's subject. The `saw` /
  `inferred` tag keeps the non-omniscient requirement visible in the telling.
- **S.** One subject read per line kind, the closing-cell set shared with the closure reading, the
  existing projection for the viewpoint. No second attribution rule.
- **E, last.** One field, one pick, one flag; the render becomes readable by someone who did not build it.
  High.

## Cost class

Small build (harness only), hash EQUAL. Depends on `09_WR_B_readings_of_closure_and_tension.md` edit 1
for `CLOSE_CELLS`; landing order: that edit first.
