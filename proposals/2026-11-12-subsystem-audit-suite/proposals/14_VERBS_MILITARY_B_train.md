# VERBS · MILITARY · B — `train`: a season's lesson that may or may not take

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **Layer 1**: `train` emits three kinds across its bands, so it declares `contests: "a task"` (residue §1, shape (b)); the roster is `graded_tasks`. (2) **A-5, A-7**: one sampler; the pool is the teacher's trained score in the vocation by the one pool rule (as written), and his governing attribute gives talent levels. (3) **A-25**: `learner_regards_teacher` is a named level for the roller. (4) The capability table Edit 2 extends is U1's (`references/descriptor_registry.yaml`, the `trained_at` column there), and the first-rank rule is `01_CORE_capability_authoring_surface.md` Edit 9 as U1 §4 keeps it. A-63: a lesson occupies the pupil as any interaction occupies its counterparty (CORE's edit with A-9's scene order; this row's once-a-season key is unchanged). A-11 stands: training gates no act. A-2: a drilled cohort is a person at weight; no unit is trained.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head line applied to the body (`unified/work/R4_READ.md` §1.3, 7b.5): Edit 1 declares `contests: "a task"`; Edit 2's `graded_inquiries` line deleted (the prize binds the roll); `learner_regards_teacher` is a `favour` level (C3-C10); the `learner_rank` difficulty becomes the named level `routine` (D-U1-04) and the remaining modifiers are listed for U1 as non-members of OBS §2 (INCOMPLETE, as MIL_A's); the `trained_at` column's home is U1's capability rows (`references/descriptor_registry.yaml: capabilities`, D-U1-07); Edit 3's `[UNVERIFIED]` settled at the tree (`loop/resolve.py:450-451`: a band whose `writes:` is `[]` never calls the effect, so `_eff_train` needs no Partial/Failure branch and no event-only change); C3-N25 explained (aperture's `formed` counts persons, `att` counts acts: `harness/aperture.py:709-713`); A-81, A-30, U3 batch B22, R4 7b.0 block. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "vocation" → "capability" and "key" (for a capability) → "rank" in prose (glossary *capability*, *key*).

## Status: PROPOSED

Lands in batch: B22 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `14_VERBS_MILITARY_A_movement.md` (Edit 6, the `with` deposit).
Depends on: `01_CORE_capability_authoring_surface.md` Edit 9 (B04); `05_SC_obstacle_difficulty_and_modifiers_B.md` and `U5c_SC_one_obstacle_form.md` (B05); `U5c_VERBS_residue_and_governance_owner.md` §1 and `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4 (B07); U1's capability surface (`trained_at`).
Lane: MB. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; one `opus` read of reading (iii). Test file: `engine/season/tests/test_vm_mil_b_train.py` (one function per §4 reading; the scratch probe `probe_army.py` is restated as reading (ii)'s function, U3 §6.2's rule).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the teacher's trained score in the capability (A-6); talent as levels from the governing attribute (A-7); a wound a level against the roll (A-8). The draw takes `H(w.world_seed, w.tick, <actor id>, "train.task")` (A-30). **A-81:** Partial and Failure write no cell; `training.practised` is counted by `practice` for the learner (a durable read of the deposit) and `training.fruitless` is witnessed by teacher and pupil (a claim of it to each), so no lesson is a still scene.

Batch M-B of `audits/14_VERBS_MILITARY.md` (§3.3, §5.3). Source: F-VM-01; the M-CAP row of
`audits/12_ARCS_adjudication.md` ("`train` attempted and never executed"); `AUDIT_BRIEF.md` "Standing
rule". Depends on `01_CORE_capability_authoring_surface.md` Edit 9 (a first rank is never a loss),
which it adopts and does not restate. Nothing is ratified by being written.

## 1. What it changes in `engine/season/` at runtime

1. `train` forms only on a person the question names (the actor himself included).
2. An admitted lesson is resolved by one draw: the teacher's skill in what is taught against the
   learner's present rank and the circumstances. A rank is gained on the two upper bands, a practice
   credit on the third, nothing on the fourth.
3. A cohort trained in `arms` is a drilled levy: the cohort person's rank is the datum the field
   reads as the quality of troops drawn from it (the read is MB's, its audit §14 and step 8).

Declared movers: formation (the class), and every executed `train`.

## 2. The problem (evidence)

- `aperture 2 0`, realm: formed 83 (persons who formed it; the instrument's `formed` column counts
  persons, its `att` column acts, `harness/aperture.py:709-713`, so attempted may exceed formed),
  attempted 85, executed 0, refused 85: `exists:Person=0` 39 (the
  subject is the question's referent, whatever it is), `with=False` 33, and 13 that cleared the cell
  and were declined by the effect because the subject holds no rank in the capability.
- `probe_army_s0.txt`: 2 of 83 persons hold any capability key (both `inquiry`). Self-training
  `arms` and `copying` with no key: `train.refused`. With `{arms: 2}`: `capability.raised`,
  `{arms: 3}`, with certainty (`loop/effects_combat.py::_eff_train`, `raised_capability`).
- `corpus_run`: `train` only refused; the ranking excludes it (no celled alignment axis), so where
  it forms it ties and is taken by the draw among ties, not for a reason.

## 3. Exact edits, by owner

**Edit 1 — `engine/season/verb_table.yaml`, the `train` row (`:1898`), final text of the changed
columns** (eligibility, beneficiary, cell and their notes stand):

```yaml
    referent_class: Person
    contests:    "a task"        # shape (b): three kinds across the bands (VRES §1)
    difficulty:  routine
    referent_class_note: "14-VM-B: FORMED ONLY ON A `Person`-CLASSED REFERENT -- the person the question he answers is about, himself included (`queries/world_q.py::own_referents_of_class`). The class removes the 39-of-85 formations on a Record, a place or a Proposition and claims no execution. The teacher's own capability is NOT read here: capability gates nothing (#353 §9.2, probe P11). REVERT: delete this column."
    writes:
      Overwhelming: ["Person.capability"]
      Success:      ["Person.capability"]
      Partial:      []
      Failure:      []
    writes_note: "14-VM-B: ONE RANK ON THE TWO UPPER BANDS (`raised_capability`, minting per `01_CORE_capability_authoring_surface.md` Edit 9). Partial writes nothing and emits `training.practised`, a kind `queries/world_q.py::practice` counts as a good result for the LEARNER in the capability carried (CR-18's addend), so a lesson that did not take still leaves him readier. Failure: `training.fruitless`. At the ceiling of the capability's scale the effect declines (`train.refused`, the read `(subject, capability:<kind>, <rank>)` on the Event). [ASSUMPTION; medium; Jordan to correct; revert: the flat write.]"
    emits:
      Overwhelming: ["capability.raised"]
      Success:      ["capability.raised"]
      Partial:      ["training.practised"]
      Failure:      ["training.fruitless"]
    emits_on_refusal: ["train.refused"]
```

**Edit 2 — `engine/season/rosters.yaml`.**

- *(W3-4a: the `graded_inquiries` line is deleted; `train` is a contest row on the `a task` prize.)*
- The pool key is the capability the act carries (`vocation_sourced: {train: kind}`, unchanged): the
  roll's input builder reads the one pool reader (`pool.py`, over `sigma_leverage.pool_of`, D-U1-08) on
  `a.payload[kind]` for a row `vocation_sourced` names, and `verb_capability` gains no `train` line. One
  clause in `seam/wrappers/sigma.py::contest_input` (the one input builder), reading the roster, never
  the verb's name.
- Obstacle and leverage, through the one composer:

  | verb | difficulty | obstacle terms | leverage (A-25) |
  |---|---|---|---|
  | `train` | `routine` | `learner_rank` (the subject's effective rank in the capability, 1 at least) · `self_taught` (subject is the actor) · `no_training_place` (no Site or venue of a kind the capability row's `trained_at` lists where they stand) · `teacher_no_better` (the actor's rank does not exceed the subject's; not applied to self-teaching) | `learner_regards_teacher`: a `favour` level (a positive stance row of the subject toward the actor; C3-C10) |

  `[ASSUMPTION; medium; Jordan to correct]` for each number. **INCOMPLETE (blocked on U1, as MIL_A's
  five):** the four obstacle terms are not members of OBS §2's closed roster; U1 decides which become
  members and which fold into existing ones (`learner_rank` reads the subject's trained score, the
  operand `opposition` reads for a person opposite, so folding it there would make the lesson opposed).
  Until then they ship absent (0): the control is `routine`.
- U1's capability rows (`references/descriptor_registry.yaml: capabilities`, D-U1-07; the authoring
  surface of `01_CORE_capability_authoring_surface.md` as U1 re-homed it) gain one optional column,
  `trained_at: [site or venue kinds]` (`arms: [barracks, garrison]`, `copying: [archive]`; content,
  Jordan's). Until that column lands the term reads an empty list and applies everywhere.

**Edit 3 — `engine/season/loop/effects_combat.py::_eff_train(w, a, res)`.** Structure:

```python
who, key = _operand(a, "subject"), _operand(a, VOCATION_SOURCED[a.verb])
p = w.persons.get(who)
if p is None or key not in VOCATIONS:            return NO_CHANGE          # as now
raised = raised_capability(p, key)               # mints per CORE Edit 9; None at the ceiling
if raised is None:                               return NO_CHANGE
return Change((Subject.entity("persons", who, fields=("capability",)),), set_capability)
```

*(W3-4a: the earlier `[UNVERIFIED]` Partial/Failure branch is removed.)* The effect is reached only at
Overwhelming and Success: `loop/resolve.py:450-451` computes `row.writes_at(degree)` and calls the effect
only when that list is non-empty, so a `Partial: []` or `Failure: []` band emits its kind and never runs
`_eff_train` (`Subject.event_only` does not exist in the tree and is not needed).

**Edit 4 — `engine/season/queries/world_q.py::practice`.** Its set of counted kinds gains
`training.practised`, read off the `train` row's `Partial` emit (`VERB_TABLE["train"].emits_at`),
never a literal; the credit is the subject's, in the capability the causing act carried.

**Edit 5 — alignment.** `rosters.yaml: tables.alignment` cells for `train` are CHAR's to author
(`02_CHAR_choice_alignment.md`); until they exist the row stays out of the corpus ranking, which this
proposal does not change and names as the reason a realm person will train rarely.

**Not edited:** the opportunity key (one lesson per learner a season stands); P-08 (Thread
Sensitivity stays outside `VOCATIONS`); the `with` deposit (proposal A, Edit 6), on which the 33
absent-pupil refusals depend.

## 4. Gate and falsifier

- **Execution artifact.** (i) `aperture 2 s`, s = 0 to 2, after CORE Edit 9 and proposal A:
  `capability.raised` is out of the never-emitted list at one seed at least; `train`'s refusals read
  0 on `exists:Person`. (ii) A hand-built lesson through the fold on `build_realm(0)`, 200 seeds of
  the draw (the probe's shape, `scratchpad/runs/VERBS_MILITARY/probe_army.py`): all four bands
  occur; the learner's pool after a first rank is not below `pool_default`. (iii) The same lesson
  with a teacher holding the key at 5 against one holding none: the share of the two upper bands
  differs beyond sampling error at n 200 (a reading of mechanism, same-run control; not a balance
  claim). (iv) Downstream: a learner who gained a rank in `argue` rolls a pool one larger in his next
  `argue` (the roll's recorded pool; the bell-curve sampler, A-5, reads the pool as a count of dice).
- **Control.** `Fixtures practice_cap: 0` and the `contests:` column removed (flat write): every
  admitted lesson raises one rank (today's certainty), which is what the edit removes.
- **Falsifier (planted).** `_eff_train` ignoring `res.degree`: (ii) shows two bands only. The
  `teacher_no_better` row at 0: (iii) shows no difference. `training.practised` left out of
  `practice`'s kinds: a Partial lesson leaves the learner's next pool unchanged.

## 5. Cases

SCN-05, NPC-087, -032, -006, -009 (stage 4 of the adjudication's order); ARC-23 N2 (a rarely used
skill someone did or did not invest in); the adjudication's §14 "Advancement" row (training by
another, a ceiling). Each needs a person whose rank differs from another's *because of seasons
spent*; (iii) and (iv) are that, read from a run.

## 6. NERS reading (E last)

- **N.** From below, every pool reads `faculty`. From above, a faction's drillmasters and barracks
  become its soldiers' quality. Laterally, bleeding (`_grown`) and practice already raise skill;
  this is the deliberate third. Remove it and nobody can become what he has not yet done.
- **R.** Characters are customised by where they spend seasons; a poor teacher wastes them; with no
  player, masters make pupils and levies are drilled or left raw. Complete at the extremes: the
  ceiling refuses with a reason; an untaught first rank costs nothing it should not.
- **S.** The lesson's roll is the roll the skill itself uses; the Partial band is the practice
  rule, not a second progress counter.
- **E, against that.** One column, one `contests:` cell, four obstacle terms and one level, one kind in
  `practice`.
  "A good teacher, a proper hall and a willing pupil make it likely" is predictable from the row.

## 7. Cost class

Small build, after CORE Edit 9 and SC-B's composer. Two declared movers (formation; execution).
