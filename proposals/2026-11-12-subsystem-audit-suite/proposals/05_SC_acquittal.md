# SC-P6 — a hearing can be lost by the bench: `determine` at `Failure` dismisses the matter

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-08) — the count of failed askings that dismisses a matter is one arrangement-row key, `ballots`, default 1 (`audits/05_SC_audit_addendum_B.md` G-55; `ED-IN-0288`'s intent: one failed asking dismisses unless the row says more). The addendum's proposed 3 is a value a row may author, not the default. A bench that failed asks again at most once per sitting, and a dismissed matter re-opens only on something new (`U5c_SC_proceedings_residue.md` §4).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-P6, §2 row A-81, §3 row `ballots`, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-03; `unified/U3_CONFLICT_LEDGER.md` C3-C11). The body now carries the head (`U5c_SC_proceedings_residue.md` §4, the reconciled text): `ballots` (default 1) is the count of failed askings that dismisses; edit 1 keeps `matter.undetermined` and adds `matter.dismissed`, each earned by its own receipt (the `failed` stage earns the first, the docket write the second), instead of deleting the first; edit 2 appends a `failed` stage every Failure and dismisses when the count reaches `ballots`; every band now names its durable write (A-81: the Failure band writes the `failed` stage); the whole-dice odds in the problem are marked history (A-5); the realm probe is a named test; lands-it and tier added.

**Lands in batch:** B27 (with `U5c_SC_proceedings_residue.md` §4). **Depends on:** plan position CR-61 (the docket item names its case file) `[PL]`; `05_SC_contest_record_on_event.md` (B05).

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-25) — edit 4's `[UNVERIFIED]` settled: the `(Record, stages)` matrix row names no verb, so no matrix edit is owed; the verb row's band list is where the pair is declared.

Source: `audits/05_SC_audit.md` F-SC-05; `engine/season/hole_register.yaml` H-162 clause (c), whose
stated revert this takes; `proposals/2026-10-03-verb-coverage-and-gap-fill.md` §9.6 (ratified as
intent, ED-IN-0288), which reads a failed determination as an acquittal (`DocketItem.matter`,
`matter.dismissed`).

## What it changes in `engine/season/` at runtime

A contested `determine` that grades `Failure` takes the matter off the docket and emits
`matter.dismissed`, where today it writes nothing, emits `matter.undetermined` and leaves the matter
to be re-heard every season. A declared mover in every world where a `determine` executes and fails
(`build_realm`, six seasons: `matter.undetermined` 2 at seed 0 and 2 at seed 1, against
`matter.determined` 1 and 2 and `matter.lapsed` 8 and 8; audit §12 run 6).

## The problem (evidence)

- `verb_table.yaml` `determine`: `Failure` writes `[]` and emits `matter.undetermined`
  (`data/verbs.py` parse, printed in audit §12). The sitting question is standing, so the same judge
  is asked again each season (`queries/world_q.py::sittings_before`: *"ONE CONVENE IS A STANDING
  COURT"*).
- H-162 (c), in the register's own words: *"a docketed person is re-heard each season until a
  non-Failure draw disposes of him and there is NO ACQUITTAL PATH … the contest decides WHEN a
  docketed person is disposed of and at what degree, never WHETHER."*
- At the shipped pair (pool 2, obstacle 2) one attempt binds with probability 0.26 (exact:
  0.74 / 0.19 / 0.07 / 0.00; whole-dice history under A-5, the reading the audit took). With `docket_lapse` 4 the only way an accused is not bound is the
  docket outlasting the bench's attempts (`matter.lapsed`). No act of the accused, no proof and no
  speech changes that (F-SC-05).
- The provided arcs need the other outcome as a first-class result: ARC-04 (important) *"a formal
  contest must be able to defeat an accusation for the present while leaving the underlying case file
  intact and reopenable later"*; ARC-21 (core) *"a failed formal challenge against a power-holder
  must weaken the challenging institution … not simply leave the state unchanged"*.

## The resolution, decided

Take H-162 (c)'s revert (ladder step 3: #453 §9.6 is the design document, ratified as intent; the
tree's departure is an `[ASSUMPTION; medium]` with this revert written beside it). The dismissal
names the case file as the subject it moves, so the write is a real one and the case stays
reopenable.

## Exact edits, by owner

0. `engine/season/arrangements.yaml` and `data/arrangements.py`: the key `ballots` (an integer of 1 or
   more; default 1; added to `_ARRANGEMENT_KEYS`; refused below 1). No seeded row changes
   (`U5c_SC_proceedings_residue.md` §4 item 1).
1. `engine/season/verb_table.yaml` `determine`, band `Failure`: `writes: [Record.stages,
   DocketItem.matter]`, `emits: [matter.undetermined, matter.dismissed]`. Each kind is earned by its own
   receipt (the pattern `_eff_pardon` uses for `_RESTRAINT_ENDED`): the `failed` stage alone earns
   `matter.undetermined`; the docket write earns `matter.dismissed`. `matter.undetermined` keeps its
   readers (`loop/witness.py:383`'s keyed-kinds comment, the `deed:matter.undetermined` alignment cell
   `loop/effects_information.py:604` cites, the `undeposited_kinds` note in `rosters.yaml`).
2. `engine/season/loop/effects_information.py::_eff_determine` — branch on `res.degree` FIRST (H-162
   (c): the body opens a disposal whenever it runs). At `Failure`: build
   `Change((Subject.entity("records", <case file id>, fields=("stages",)),), perform)` where `perform`
   appends `(tick, "failed", a.id)` to the case file; if the file now carries `ballots` `failed` stages
   since its last `opened` stage, it also appends `(tick, "dismissed", a.id)` and writes every docket item
   naming the party back to `matter: None` (the slot survives, as at a disposal). No Tenure is opened;
   `consequence_pursuits` is not called (H-221 stays as it is). With `ballots` 1 the first Failure
   dismisses (`ED-IN-0288`'s intent). A bench that failed asks again at most once per sitting, and a
   dismissed matter re-opens only on something new (`U5c_SC_proceedings_residue.md` §4 items 4–5).
3. The case file's id: for a matter that rose from a petition it is the item's `DOCKET_PETITION`
   (written today by `carry`). For an `open_case`d matter the item must name the file it minted —
   CR-61's edit (B10-18c: *"`determine`'s precondition asks for the held case file"*). **Dependency:
   this proposal lands after CR-61**; before it, only petition-borne matters can be dismissed and the
   rest decline (`NO_CHANGE` → `determine.refused` on the write clause), which the gate test pins.
4. `engine/season/write_matrix.yaml` — no new row: `(DocketItem, matter)` and `(Record, stages)` are
   `[RES]` ACTS cells already (`determine` writes the first today, `carry` the second).
   `[GROUNDED, 25 G-25]`: the matrix needs no edit, the verb row does. The `(Record, stages)` row is
   `steps: [RES]`, `class: ACTS` and names no verb (its keys are `kind, field, steps, class, social, by,
   emits`), so it admits any RESOLVE act whose row lists the pair; `determine`'s `writes:` today lists
   `Tenure.since`, `DocketItem.matter`, `Tenure.degree`, `Person.pursuits` by band and not
   `Record.stages`, so the band that writes the dismissal gains it in `verb_table.yaml` (edit 1's row).

## Gate (execution artifact)

`engine/season/tests/test_u7_remit.py` section 10: a planted `Failure` margin on a petition-borne
matter leaves no docket item naming the party, a `matter.dismissed` Event whose `changes` name the
petition, no new Tenure, one `failed` and one `dismissed` stage at `ballots` 1, and a second `open_case` on
the same party carrying something new is admitted (reopenable; without it, refused on `fresh`). The realm
reading (audit §12 run 6's script is scratch, not in the repository) is written as
`engine/season/tests/test_proceedings_residue.py::test_failed_determinations_dismiss_in_the_realm`: seeds
0–1, six seasons, `matter.dismissed` above 0 where `matter.undetermined` reads 2 and 2 today, and
`matter.lapsed` below its present 8 and 8.

## Falsifier

A planted `Success` margin on the same world must still open the disposal and emit
`matter.determined` (the branch must not swallow the binding bands). A `Failure` on an `open_case`d
matter before CR-61 must refuse and leave the docket untouched; if it clears the docket with no
receipt, the write has no named subject (ID-9) and the edit is wrong.

## NERS reading

- **N**: without it a hearing has one terminal state and a clock. Top-down a trial needs two
  verdicts; bottom-up the band already distinguishes them; lateral, combat and the field both have a
  losing side.
- **R**: the accused can win; a failed prosecution is an event others witness and remember
  (*emergent hooks without player involvement*: the acquitted man, the humiliated bench).
- **S**: the docket clears by the same write a disposal uses; no second lifecycle.
- **E**: one band cell and one branch.

## Cost class

Edit, after CR-61 (design input: what, if anything, a dismissal costs the bench is H-219/H-221's and
is not decided here).

**Lands it and tier.** The B27 batch with `U5c_SC_proceedings_residue.md` §4, an SC `valoria-author` session
on `sonnet` (`high`), closed by B27's `methodology-close`. **Hash movers.** Every world where a `determine`
fails (declared).
