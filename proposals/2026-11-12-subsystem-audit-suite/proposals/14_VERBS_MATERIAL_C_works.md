# 14 · VERBS · MATERIAL · C — `found` and `build`: formed on their own works, asked about, drawn, and raised by `work`

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-05) — a keyed refusal cannot name an effect-side clause other than `write` (`data/verbs.py:945-967`); the `stores` key needs a named typed conjunct or falls under `write`.

Batch M-C of `audits/14_VERBS_MATERIAL.md` §18 (its §5, §6; `work` is §16 and its row is in
`14_VERBS_MATERIAL_A_mending.md` §4). Needs batch M-A §2 and `14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`
edit 2 (`Record.<kind>`). Does not re-open ED-IN-0297 (closed at option (B): works are authored rows of
`engine/season/venues.yaml: planned_works`). Reference under CLAUDE.md §0.05. Read at `84d2a02`.

## 1. What changes in `engine/season/` at runtime

`found` and `build` stop forming on petitions, texts, covers and sheets; each forms only on a works its
actor holds that plans the kind of thing that verb makes and has not yet made it. A master of an unmade
works is asked about it every season. The founding or building is drawn: it can cost more than the price,
or fail and lose part of it, and can be tried again. Declared hash mover.

## 2. The problem, with evidence

- `aperture 2 s`, seeds 0 / 1 / 2: `found` attempted 3 / 4 / 4, `build` 3 / 4 / 2, executed 0, every
  refusal `exists:works=0`.
- `mat_probe.py 2 4` (seed 2, four seasons): each row formed 819 times; 421 on a petition, 223 on a text,
  93 on a cover, 46 on a sheet, **36 on a works**; of the acts attempted, none named a works. The two
  authored works are held by `p_npc_020` (`works_hearth_auerheim`) and `p_npc_009`
  (`works_dwelling_court`); their paying rungs hold the price from season 1 (grain 40 and timber 10
  against a `works_cost` of 10). So the precondition, the cost and the effect are all satisfiable and the
  act is never taken: its two candidates sit among several hundred, and a wrong-plan candidate (a `found`
  on the dwelling works) would be refused by the effect for a reason the master can read off his own
  paper.
- Both effects are a fixed function of state (`loop/effects_founding.py::_eff_found`, `_eff_build`).

## 3. The exact edits, by owner

**(a) `engine/season/queries/world_q.py`.** `records_held_for_holding_rows` loses the works kind (its
other kind, `petition`, stays for `carry`). New, beside it:

```python
def works_unmade(w: World, p: Person) -> tuple:
    """((works id, plan kind), ...) for the works Records on `p`'s OWN live `hold` edges whose made thing
    (`loop/effects_founding._made_by`'s id, moved here as `made_id(rec, plan)` so one owner names it) is not
    yet in `w.rungs` / `w.sites`. His own paper and what his own works has made: the own-edge clause of
    FI-01's R-03."""
```

`questions_for`: (i) each such works is stamped `Record.works` (SOCIAL2-A's qualified class) on the
question he answers; (ii) one standing question per unmade works, `Question(f"q:works:{rid}",
"claim_landed", (rid,), <the id of his own content claim on it>)`, the docket question's shape (a matter
that waits until it is disposed of); a master with no content claim on his works (the authored ones,
minted with no Event) gets the `need` form, `Question(f"q:need:{rid}", "need", (rid,), rid)`, as a person
with a vacancy and no question does. No source is added. `[ASSUMPTION; medium; Jordan to correct; revert:
drop (ii), and the works waits on a referent coincidence]`

**(b) `engine/season/rosters.yaml`.** New roster, so the plan kind is read and never spelt:

```yaml
  works_verbs:
    source: "14_VERBS_MATERIAL_C: which verb makes which family of plan."
    values: {found: rung_kinds, build: site_kinds}
```

`decision/options.py::opening_set`: a row named in `works_verbs` forms only on a `Record.works` referent
whose `plan` (read from the person's own content claim on the works, `held_record_claims`; for an
authored works with no claim, from `works_unmade`'s pair carried on the stamp) is a member of the roster
that row maps to. That is the person-side reading of `_eff_found`'s and `_eff_build`'s first decline.

**(c) `engine/season/verb_table.yaml`** (unlisted columns unchanged):

```yaml
  - verb:        "found"
    referent_class: Record.works
    capability:  none          # `labour` when authored
    difficulty:  demanding
    writes:
      Overwhelming: ["Rung.exists", "Tenure.since", "Rung.stores"]
      Success:      ["Rung.exists", "Tenure.since", "Rung.stores"]
      Partial:      ["Rung.exists", "Tenure.since", "Rung.stores"]
      Failure:      ["Rung.stores"]
    emits:
      Overwhelming: ["rung.founded"]
      Success:      ["rung.founded"]
      Partial:      ["rung.founded"]
      Failure:      ["found.failed"]
    emits_on_refusal:
      requires: ["found.refused"]
      stores:   ["found.short"]
      write:    ["found.refused"]

  - verb:        "build"
    referent_class: Record.works
    capability:  none          # `craft` when authored
    difficulty:  demanding
    writes:
      Overwhelming: ["Site.exists", "Rung.stores"]
      Success:      ["Site.exists", "Rung.stores"]
      Partial:      ["Site.exists", "Rung.stores"]
      Failure:      ["Rung.stores"]
    emits:
      Overwhelming: ["site.built"]
      Success:      ["site.built"]
      Partial:      ["site.built"]
      Failure:      ["build.failed"]
    emits_on_refusal:
      requires: ["build.refused"]
      stores:   ["build.short"]
      write:    ["build.refused"]
```

The refusals become keyed (invariant 4's per-clause half, `requisition`'s shape): `stores` is §27.1's
scarcity channel (*the second builder on an emptied store gets a different Event*), now told apart from a
malformed act. `[GROUNDED, 25 G-05: the loader refuses it. A keyed row keys exactly its failable
clauses, a derived set: `eligibility`, each NAMED top-level typed conjunct, `write`, `counterparty`
(`data/verbs.py:945-967`); a key outside the set is refused as a kind nothing reads. So `stores` is
keyable only as a named typed conjunct (the stem exists, `data/requires.py:852`); as the effect's decline
`_cost`'s shortfall is reported under `write`.]`

**(d) `engine/season/data/fixtures.py`.** One table, per-mille of the plan's `works_cost`:

```python
    works_outlay={"found": {"Overwhelming": 0,   "Success": 350,  "Partial": 700,  "Failure": 350},
                  "build": {"Overwhelming": 700, "Success": 1000, "Partial": 1350, "Failure": 500}},
```

For `found` it is the share of the stake **consumed** (the rest arrives in the new Rung, two-sided, as
today); for `build` the share of the price consumed (one-sided, as today). The control is `found` all 0
and `build` all 1000 with Failure refused, which is today's arithmetic. `[ASSUMPTION; medium; Jordan to
correct; swept]`

**(e) `engine/season/loop/effects_founding.py`.** `_cost(w, rec, plan, res)` returns the payer and, per
kind, `(consumed, carried)` whole units from the table (`ceil`), declining when the payer cannot meet the
band's total, except that a `Partial` the payer cannot meet is priced as `Failure` (the row's own text).
`_eff_found`: at a winning band mint the Rung, its `contain`, the founder's `hold`; `_shift` the carried
part into it and `_debit` the consumed part; at Failure only the `_debit`, naming the payer, earning
`found.failed`. `_eff_build`: at a winning band mint the Site at condition 0 and `_debit` the outlay; at
Failure only the `_debit`. Both keep every other decline. `rosters.yaml: graded_acts` gains both.

## 4. Order of landing

1. SOCIAL2-A edit 2, with the correction `audits/14_VERBS_MATERIAL.md` §17.2 lists (both pairs stamped).
2. (a)(i), (b), and the class on both rows: formation only (declared mover; wrong-kind formations stop).
3. (a)(ii), the standing question.
4. (c), (d), (e): the draw.
5. `work` (`14_VERBS_MATERIAL_A_mending.md` §4).
More `planned_works` rows are Jordan's content and are what makes the batch visible at realm scale.

## 5. Gate and falsifier

- **Execution artifact.** `mat_probe.py s 4` re-run at seeds 0 to 2: `found` and `build` form only on a
  works of their own plan family (the subject-class line reads `Record:works` alone), `rung.founded` or
  `site.built` ≥ 1 at some seed, then `site.worked` on the built Site, then `world_q.capacity` of the
  court's rung above the control's. Across seeds 0 to 19 on a one-works fixture the stores left at the
  payer take three or more values.
- **Control.** `planned_works: []` reproduces the no-works realm hash (the block's own control).
- **Falsifiers.** A `found` formed on a works that plans a Site kind. A second `found` from one works
  executing. A fabric minted above condition 0. Stores of any kind created (the payer's debit must equal
  consumed plus carried at every band).
- **Planted failure.** Drop (a)(ii): if the gate still passes at every seed the question was not needed
  and is deleted; if `found` and `build` return to zero attempts, the reading is recorded and the lean is
  CHAR's and CORE's (`audits/14_VERBS_MATERIAL.md` §17.2).

## 6. NERS reading (E last)

N: the realm ends every run with the rungs and Sites it began with (SE F-SE-12), and the ruled bound on
population growth is housing (ED-SE-0051), which only these two verbs make. R: a founding that eats its
stake, a build that overruns, a hall begun by one man and raised by others. S: the family's draw; one
cost reader for both verbs; the stamp is `writs_held`'s shape. E, last: one stamp, one roster, one table
and two banded rows, against 819 formations a run that could not execute.

## 7. Cost class

Small build. Declared mover. Lanes: SE; CHAR and CORE for whether the formed act is chosen.
