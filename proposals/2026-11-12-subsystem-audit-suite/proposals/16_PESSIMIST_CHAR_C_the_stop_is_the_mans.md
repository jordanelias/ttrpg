# CHAR (pessimist) C — the stop is the man's: a scruple with a closed set, one scale, a draw and a trace

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — item 4 (the draw) is **no longer held**: Jordan's answer A-24 (D-28) makes a scruple a drawn tendency; `scruple_temperature` ships above 0 when the gate is armed, and the threshold arm is the control. Arming the gate is its own flip (`U5a_CHAR_owed_amendments.md` §8).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-24 / D-28: the Status and "For
Jordan" closed; the shipped temperature stated as an assumption; A-34: `Scene.forgone` is not a belief), §1 (item 5:
`Scene.forgone` lands only with its reader, ID-13; `scruple.overridden` rides `Act.scene`, not `payload`, and is declared
in the verb table so inv. 7 derives it; the Event names no subject, `04` §B.9 `:433`), §7/§7b (tests, tier); U3 B10,
§6.2 (`c2_stopped.py` not in the repository). Changed: Status line, item 4's heading, item 5's carrier, the edits
table's last rows, the gate, "For Jordan".

## Status: PROPOSED (A-24 taken: item 4, the draw, is no longer held; arming the gate is its own flip, `U5a_CHAR_owed_amendments.md` §8)

Lands in batch: **B10** (IN/CHAR). Depends on: `01_CORE_reason_trail_in_the_act_store.md` (B09; the reader of
`Scene.forgone` lands in the same commit as the field), `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md`
(B10, before this), `U5a_CHAR_owed_amendments.md` (B10; §8 is the arming).

Written by the CHAR pessimist lane (`audits/16_PESSIMIST_CHAR.md`, F-PES-CHAR-02). Ratifies nothing;
reference under `CLAUDE.md` §0.05. It is the build of H-146's remaining position (arming the ruled
deontological refusal, ED-IN-0261), which cannot be armed as it stands.

## What this changes in `engine/season/` at runtime

With `refusal_axis` unset (shipped) nothing: hash EQUAL. It changes what happens when the gate is armed:
which verbs it may refuse (a closed set, data), the scale the person's threshold is read on, whether the
refusal is a threshold or a draw (fixture, control = threshold), and that a refusal that cost the person
his first choice leaves a trace on the `Scene`.

## The problem, with evidence

Premise: *a man pursues what he wants and is stopped by what he believes.* `c2_stopped.py`, seed 0, 46
cast, six referents, temperature 0, `PYTHONHASHSEED=0`:

| arm | readings | persons with any candidate refused | refused, by verb | readings where the gate took his TOP act |
|---|---|---|---|---|
| shipped (`refusal_axis: None`) | 276 | 0 | none | 0 |
| armed (`deontological_instrumental`) | 276 | **46 of 46** | `transfer` 276, `move` 276, `forge` 276, `reconstruct` 276, `exchange` 276, `survey` 270, `lie` 37, `challenge` 6 | 53 (he then takes `create_record` 30, `surveil` 17, `survey` 6; score given up: median 0.045) |

Shipped, nothing stops anybody. Armed, everybody is stopped from the same things, and the things are
moving house, handing something over and trading. Three defects, each at a named line:

1. **The set is not "certain actions".** `options.py::refuses` refuses *"only a verb the axis ENGAGES"*,
   and the instrumental pole's cells are the means-to-an-end verbs (`transfer` +0.6, `exchange` +0.6,
   `move` +0.5, `work` +0.4) beside the wrongs (`forge` +0.8, `lie` +0.5). No cut on the cell separates
   `move` (+0.5) from `lie` (+0.5).
2. **Two scales.** The threshold is `project(p)[axis]`, a projected weight whose size depends on how many
   pursuits the registry happened to author (cast range −0.395 to +0.306, median −0.020); it is compared
   with an alignment cell on ±1. The most instrumental person in the realm (+0.306) still refuses five
   verbs outright. NERS S: *calculations consistent in methodology*.
3. **Silent and certain.** A refused candidate is never formed (`options.py:170`), so nothing records
   that he wanted it; and the refusal is a fixed function of state, which the standing rule of
   2026-11-12 forbids for a thing that could go either way (a man tempted).

## The resolution, decided

Ladder: step 3 gives the shape (ED-IN-0261: deontology is a refusal, the weight is a threshold); steps 4
and 5 give the rest.

**1. A closed set of refusable verbs, in data.** `rosters.yaml: pursuit_axes`, beside `refusing_pole`:

```yaml
refusable:                       # the "certain actions" ED-IN-0261 gates; a verb not listed is never refused
  deontological_instrumental: [forge, lie, "evade / defy", construe]
  # [ASSUMPTION; medium; Jordan to correct: content. `destroy_record`, `sabotage`, `conceal`, `raze`,
  #  `seize` join when they carry a cell on this axis (16_PESSIMIST_CHAR_B, step 2).]
```

`data/rosters.py::refusable(axis)` loads it (a verb off `VERB_TABLE` or with a zero cell on the axis is
refused at load, on `refusing_pole`'s precedent); `options.refuses` returns False for a verb outside it.

**2. One scale.** `options.refusal_tolerance` returns the axis's SHARE of the person's projected vector,
`project(p)[axis] / ‖project(p)‖` (0.0 for a zero vector), which lies on ±1 as a cell does. Read through
`data/pursuits.py::to_axes`, the one owner; `_AXES` order for the norm (first audit F-CHAR-10).

**3. A margin, not a boolean.** `options.scruple(verb, axis, tolerance) -> float`: how far the cell
sits past the tolerance toward the refused pole (0.0 when it does not, or for a verb outside the set).
`refuses` becomes `scruple(...) > 0` and keeps its callers.

**4. The draw (A-24: ships).** New fixture `scruple_temperature` (control 0: today's threshold; swept
0.1 / 0.2 / 0.4). Shipped value `0.2` when the gate is armed `[ASSUMPTION: the proposal's own gate arm —
basis: gate 4; Jordan did not give a value; revert: 0, the threshold]`. At a non-zero value the candidate is struck with probability
`1 − exp(−margin / scruple_temperature)`, on the person's own draw keyed
`scruple:<verb>:<subject>` (the chooser's `draw`, keyed by candidate as `choice:` is, so a fork stays
attributable). A large margin is refused nearly always and never certainly; a small one usually gives
way.

**5. The trace.** The gate moves from `opening_set` (before scoring) to `make_ranker` (after scoring,
before the sample), so the struck candidate's score is known. Where a struck candidate out-scored the
candidate that leads the released scene, the `Scene` carries it: `Scene.forgone: tuple[(verb, subject,
margin)]` (a new field on the carrier; owner `state/carriers.py`, the CORE lane; cross-listed with
`01_CORE_reason_trail_in_the_act_store.md`, which owns where a reason is stored). The field lands in the
same commit as that file's reader (ID-13, `04` `:401`: a field with no reader is not carried). Where a
candidate with a positive margin is NOT struck and the act resolves, the fold emits `scruple.overridden`
(degree none, the act among its causes; an `Event` has no subject field, `04` §B.9 `:433`, so the actor is
reached through the act in `causes`, which WITNESS reads from the act store, `04` `:180`): the person and
those present hold a claim that he did what he holds wrong. The fold finds the margin on `a.scene.forgone`
and the act's own entry (the `Act.scene` field, `04` `:426`), not in `payload`. `scruple.overridden` is
declared in `verb_table.yaml`'s emission columns so loader inv. 7 (`04` `:500`) derives it into the
Event-kind roster. `02_CHAR_scar_is_a_wound.md`'s trigger list may name that kind; this proposal does not
write a scar. `Scene.forgone` is the chooser's record of what was given up, not a belief the person holds
about himself (A-34 builds self-knowledge narrowly; this file adds none).

## Exact edits, by owner

| file | edit |
|---|---|
| `engine/season/rosters.yaml` | `pursuit_axes.refusable` (above) |
| `engine/season/data/rosters.py` | `refusable(axis)` loader and its two load-time refusals |
| `engine/season/decision/options.py` | `refusal_tolerance` returns the share; `scruple`; `refuses` composes on it; the gate at `:170` is removed from `opening_set` |
| `engine/season/decision/choose.py::make_ranker` | after `_scores` is built: strike by `scruple` (threshold or draw), collect `forgone`; `release` passes it to the `Scene` |
| `engine/season/data/fixtures.py` | `scruple_temperature=0` (control; `0.2` shipped when armed, item 4), hole row (id from `references/id_reservations.yaml` `next_free`), sweep 0 / 0.1 / 0.2 / 0.4 |
| `engine/season/state/carriers.py` | `Scene.forgone: tuple = ()` (CORE's file; cross-listed; lands with the reader of `01_CORE_reason_trail_in_the_act_store.md`) |
| `engine/season/verb_table.yaml`, `loop/resolve.py` | `scruple.overridden` declared in the emission columns and emitted by the fold where `a.scene.forgone` gives the act's own candidate a positive margin (carrier: `Act.scene`, not `payload`) |
| `engine/season/harness/interactions.py:311-313` | reads `scruple` in place of `refuses` (it prints the gate per verb today) |

## Gate (an execution artifact)

`c2_stopped.py` was lane scratch, not in the repository (U3 §6.2); its readings are committed first as
NEW `engine/season/tests/test_scruple.py`: `test_unarmed_hash_equal` (gate 1),
`test_refusable_set_is_closed_and_cell_nonzero` (item 1's load refusals),
`test_armed_threshold_refuses_some_not_all_and_never_move_transfer_exchange` (gate 2),
`test_share_not_projected_weight_is_the_tolerance` (gate 3),
`test_draw_strikes_some_not_all_at_margin_005_and_08` (gate 4; 200 draws keyed `scruple:<verb>:<subject>`),
`test_forgone_scores_exceed_released_lead` (gate 5). Command: `python -m pytest engine/season/tests/test_scruple.py -q`.
The table in "The problem" is the producing lane's evidence. Readings, seeds 0 and 1:

1. Unarmed: 0 refused, hash `bacd687f` after two seasons at seed 0.
2. Armed, threshold: the number of persons with any candidate refused is strictly between 0 and 46, and
   no person is refused `move`, `transfer` or `exchange`.
3. Armed, threshold: among the persons refused `forge`, the median share on the axis is lower (more
   deontological) than among those who are not: the stop tracks the man.
4. Armed, with the draw at 0.2, 200 draws of one person on one situation: a candidate at margin 0.05 is
   struck in some and not all; one at margin 0.8 is struck in most and not all.
5. One season armed: at least one `Scene.forgone` entry exists, and for each the forgone candidate's
   score exceeds the scene's first act's.

## Falsifier

Gate 2 fails if the share still puts everyone on one side of the listed cells (then the cells, not the
scale, are wrong, and the repair is 16_PESSIMIST_CHAR_B's). Gate 3 fails if the refusal is still a
property of the table.

## NERS reading (E last)

- **N.** Today the gate is a free cut: unarmed it does nothing, armed it removes the same five verbs for
  everybody, which a row deletion would do as well. With a personal threshold it is the only mechanism
  by which a want is refused by its own holder, and it is needed from every direction the premise is
  read in: the person (his line), the pair (one forges, the other will not), the realm (who can be
  bought), the record (what he gave up).
- **R.** Variety of approach: the same want reached by different acts because one man will not lie.
  The no-player half: `scruple.overridden` is a secret another person can hold.
- **S.** One scale for threshold and cell; the draw is the chooser's own, keyed as its sibling is; the
  trace rides the carrier the occasion already rides.
- **E.** One list, one division and one exponent, against a mechanism that is ruled, built, documented
  across a hundred lines, and cannot be switched on.

## Cost class

Small build. Items 1 to 3 are an edit and can land alone (they make H-146 armable). Item 5 needs CORE's
carrier field. Hash movers declared: none unarmed; every seeded result once armed (the arming flip,
`U5a_CHAR_owed_amendments.md` §8, is its own commit). Tier: `sonnet`, effort `high`; the refusable list is
content (ASSUMPTION, CHAR content pass). Lands it: B10, after `_CHAR_B`; order of edits 1 → 2 → 3 (hash-equal),
then 5 with the reason-trail reader, then 4's fixture at the control.

## For Jordan (CLOSED by A-24 / D-28, 2026-11-12: Option B, a scruple is a drawn tendency; the threshold is the control arm. Kept as the finding.)

ED-IN-0261 (RULED) words the gate as a threshold: *"the weighting is a threshold for certain actions"*.
The standing rule of 2026-11-12 says no consequential outcome is a fixed function of state. Option A:
the threshold stands (`scruple_temperature` stays 0); a man's line is exact, his refusals are
predictable from his sheet, and the only way he crosses it is for his pursuits to move. Option B: the
draw ships; a man's line is a tendency, the same man sometimes gives way, and giving way is an event
with witnesses. A is a game of knowable characters; B is a game of temptation.
