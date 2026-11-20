# STORY-A — what a roll leaves: the shortfall scales the loss, a stake is paid, the other party is named, an attempt can be counted

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` (A-80, A-81). Nothing here is deleted. This file is the carrier of the Failure row of `30_WR_D_momentum_and_its_brakes.md` §3 (what each scene outcome writes, and what that write is toward): the stake paid and the counterparty named are the durable write a failed contested act must leave, and through them the attempt is held against its maker by its counterparty (toward the strand), scars the one pressed across a fault line (toward the regime) and lowers a failed claimant's standing (toward the era). It is also what makes a held position a source of motion: LOOP row L14 and census shape E-13 ("another means") read this file's Failure Event as their opening. The no-null-scene reading (`30_WR_E` clause C9) counts a Failure with no such write as a defect.

Reconciled: 2026-11-12, U5d closure — folded **A-5**, **A-38** and **A-9**. The settled margin that `SHORTFALL_STEP` reads is the one sampler's (A-5: the bell curve everywhere), so its step edges are set at the calibration with the sampler, not on whole successes. Edit 3 (a contested row's outcome kinds name the counterparty) composes with A-38: a verdict names the petitioner, or a seat he names, as the party it serves. With A-9 a scene's later step may hang on the band and shortfall of the one before, so "the success that costs" can be answered inside the scene. No step is removed.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row what_a_roll_leaves (edit 2 AMBIGUOUS; 1, 3-5 CONFORMS), §2 rows edit 1/gate 2 (A-5, A-6) and edit 3 (A-38), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-L14, C3-L1; `U5c_VERBS_residue_and_governance_owner.md` §1; `unified/U1_GLOSSARY.md` "party" ("patient" → counterparty); `unified/U3_DEPENDENCY_ORDER.md` §1 item 38, §3.1, §5.1 rows `chronicle.py`, `corpus_run.py`, `effects_shared.py`, `test_storybar.py`). Changed: (1) edit 2 follows C3-L14, which takes neither of R5's two options: there is no `stake:` row key and no `_pay_stake` payer; each staked row declares `contests: "a task"` and writes its stake in its Partial and Failure cells (shape (b), VRES §1; invariant 12 allows it, so no loader exception), and `rosters.yaml: stakes` stays as the content table those cells read; (2) edit 1's docstring loses "1 and 3 today" (the edges are set at the calibration with the A-5 sampler, and the margin is quantised to milli-units at the ladder, C3-L1); gate 2's "fewer than one failure in five" is re-measured on that margin; (3) vocabulary: the one acted on is the **counterparty** (`verb_table.yaml: counterparty:`), not the "patient"; the proposed `PATIENT_OPERAND` is `COUNTERPARTY_OPERAND`; A-38's "party served" is the **beneficiary**, `16_PESSIMIST_SC_C`'s, a different person; (4) edit 3 states where the claim's subject is derived (at WITNESS from the act's operand, through the act store; the Event stays targetless, `04` §B.9 `:433`); (5) tests named; (6) dependency, batch and tier lines. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "patient" → "counterparty" (glossary *party*); "settled margin" → "margin" (glossary *margin*, A-5).

Depends on: `05_SC_contest_record_on_event.md` and `10_DICE_exported_face_rule_and_band_edges.md` (B05); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (B07; the staked rows draw, and its item 5 lets a row move from `task` to a contest); `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 1 (B09; gate 3's `delta`); `02_CHAR_relations_have_a_ground.md`, `02_CHAR_what_an_act_risks.md` (B10); `08_FI_06_testimony-names-a-hand.md` (B11; the pairing owner); `07_SE_valley_scenario.md` (B12; the valley fixture of the gate).
Lands in batch: B38 (lane IN), after `30_WR_C` and before `30_WR_D` (`U3_DEPENDENCY_ORDER.md` §1 item 38); edits 1-3 one commit each (each hash-equal at `shortfall_scale: off` and with no row staked), edits 4-5 one commit (harness).
Tier: opus for the shape (b) reading (taken above); sonnet / high for the code and tests.

## Status: PROPOSED

Source: `audits/23_STORY_ENABLEMENT.md` §2 rows S-68 to S-71 and S-29, §4.2 G1; the four turns
`audits/16_PESSIMIST_DICE.md` §3.1 lists as *"never, as coded"* (the disaster, the success that costs,
the contest with a loser, the comeback). Composes on, and does not restate:
`05_SC_contest_record_on_event.md` (the margin on `Event.ending`),
`10_DICE_exported_face_rule_and_band_edges.md` (the band edges as exported facts),
`08_FI_06_testimony-names-a-hand.md` (the pairing that travels with a deed),
`02_CHAR_relations_have_a_ground.md` with PES-CHAR resolution 11 (`_bond` for every deed with a person as
counterparty), `02_CHAR_what_an_act_risks.md` (the chooser's risk term), `09_WR_B_chronicle_that_tells.md`.
Reference only (`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

At ship, nothing: no row declares a stake cell and `shortfall_scale` is `off` (the control), so every
content hash is today's. With a row's stake cells authored and the fixture on: a Partial on that row pays
one step of the stake while still achieving; a Failure pays one, two or three steps by how far the dice
fell short; and the outcome Events of every contested row are witnessed as done *to* the counterparty.
Each is a declared hash mover for worlds in which such a row executes. Edits 4 and 5 are harness reads
and move nothing.

## The problem, with evidence

- The margin is computed and dropped. `degree_from_net` (`engine/dice_engine/dice_engine.py:236-248`)
  reads `margin = net - ob` and returns a band; the 208 realm failures PES-DICE counted were 76, 94, 33
  and 5 at one to four below and are one Event kind (`16_PESSIMIST_DICE.md` §3.1).
- A failure costs its maker nothing but the slot. Static read of `engine/season/verb_table.yaml`
  (`runs/STORY/p1_rows.txt`): of the 11 rows with `contests:`, Failure `writes` is `[]` or absent on 11,
  Partial writes on 2 (`arrest`, `determine`), and Overwhelming equals Success in `writes` and `emits`
  on 9.
- A contest has one roller and no loser: `argument.lost` is the arguer's own failure; the person argued
  against gains, loses and records nothing (`16_PESSIMIST_DICE.md` §3.1); a fight's log names no winner
  (`16_PESSIMIST_PC.md` §3.3).
- The suite already holds per-row instances of a price: MIL-A's Partial *"arrives spent"*, MAT-C's
  founding that *"can cost more than the price, or fail and lose part of it"*. Each is written inside
  its own effect body. Two ladders for one quantity is an S defect even where each is correct (§0.06).

## The resolution, decided

One rule for what a draw costs, at the owner of the ladder's magnitudes; one derivation of who a
contested outcome was done to; two harness reads. No band is added and `degree_from_net` is not edited:
the degree ladder is single-owned by ruling (2026-08-14), so a fifth band would overwrite it (ladder
step 3). A shortfall is the same draw read one step further, in the ladder's own units.

## Exact edits, by owner

**1. `engine/season/data/rosters.py` — `shortfall_step`, beside `DEGREE_STEP` (`:1111`).**

```python
def shortfall_step(settled_margin) -> int:
    """HOW FAR BELOW THE BAR A FAILURE FELL, in the ladder's own units. 0 for a margin at or above 0
    or `None`; 1 for -S < m < 0; 2 for -O < m <= -S; 3 for m <= -O, where S and O are the Success and
    Overwhelming edges the dice engine exports, mirrored. No number is typed here: both edges are read
    from the one owner, in the units the ladder grades in (integer milli-units of the margin,
    C3-L1)."""
```

It reads the two edges from the dice engine's exported band edges
(`10_DICE_exported_face_rule_and_band_edges.md`), so the mirror cannot drift from the ladder. Under A-5
the margin is continuous before it is quantised, so the three steps are real intervals; the edges
are set at the calibration with the A-5 sampler, not on whole successes. A
magnitude-bearing Failure write is multiplied by it exactly as a Success write is multiplied by
`DEGREE_STEP[band]`; a categorical Failure write (a deposit, an edge closed) is unchanged.

**2. A staked row is a contest row of shape (b); `rosters.yaml: stakes` is the table its cells read**
(C3-L14; `U5c_VERBS_residue_and_governance_owner.md` §1). Each staked row declares `contests: "a task"`
(the prize row VRES §1 adds to `rosters.yaml: contest_subsystems.prizes`) and carries Degree-keyed
`writes:`, its Partial and Failure cells including the stake's cell (`(Person, body)`, `(Rung, stores)` or
`(Person, stance)`, the cell its `stakes` member names). `04` §B.13 invariant 12 (`:504-506`) is this shape's
own rule, so the loader needs no exception and `data/verbs.py:848-851` is unedited. The size of a stake
write is `step × n`, `step` read from the member's fixture and `n` = 1 at Partial and
`shortfall_step(settled margin)` at Failure, through one pure size reader beside `shortfall_step`,
`data/rosters.py::stake_amount(member, degree, settled_margin) -> int`, which the row's effect calls for
its declared cell [ASSUMPTION: medium; the size reader's name and placement — basis: `shortfall_step`'s
own placement beside `DEGREE_STEP`; it computes a size and pays nothing]. A row that adopts a stake moves
from `18_DETERMINISM_task_draw_for_uncontested_verbs.md`'s `task` class (shape (a)) to a contest (18-A
item 5 lets the row's owner move it), because two of its bands then write different cells. The earlier
draft's `stake:` row key and `loop/effects_shared.py::_pay_stake` payer are withdrawn (C3-L14: no loader
expansion, no payment beside the row's declared writes).

```yaml
# rosters.yaml
stakes:
  source: "STORY-A: what an actor puts down on a drawn act. A closed set; each member names the one
           matrix cell it is paid in and the fixture that sizes one step."
  values:
    body:     {cell: [Person, body],  step: stake_body}      # a fall on the body ladder
    stores:   {cell: [Rung, stores],  step: stake_stores}    # a share of the amount the act moves or prices
    standing: {cell: [Person, stance], step: stake_standing} # the regard of those present for the actor
```

The fold selects `row.writes_at(degree)` and calls the row's effect with it (`loop/resolve.py:450`,
`:967`); the stake cell is written there on the actor (body), on the rung the act draws on (stores) or in
each present witness's stance toward him (standing), sized by `stake_amount`, which returns 0 at
`shortfall_scale == "off"` and at a Success or Overwhelming. The writes emit the matrix rows' own declared
kinds (`body.changed`, `stores.changed`, `stance.moved`), `argue`'s precedent for a second emitter; no kind
is added. Fixtures in
`data/fixtures.py`, each with a hole-register row graded `assumption` and its sweep:
`shortfall_scale = "off"` (control, SHIPPED) `/ "on"`; `stake_body` (proposed: the hunger pass's own
`body_step`, so one step of a stake is one season's hunger); `stake_stores` (proposed one quarter of the
amount); `stake_standing` (proposed one deed step in the regard unit `02_CHAR_scar_cap_and_regard_unit.md`
fixes). `[ASSUMPTION; medium; Jordan to correct]` on all three sizes.

First rows to declare one, each replacing a per-row rule a suite proposal wrote (the row's owner lane
adopts the stake cells and the shape (b) move; this file edits no row): `move`, `migrate` → the `body`
stake (MIL-A's *arrives spent* is the Partial step); `found`, `build` → the `stores` stake (MAT-C's
*costs more, or loses part*); `requisition`, `sabotage` → the `standing` stake.
`02_CHAR_what_an_act_risks.md`'s cost term reads the same declared stake cells, so what the chooser
fears and what the fold charges are one fact.

**3. `engine/season/data/verbs.py` — the counterparty is the one a contested outcome was done to.**
Derive, at load, `COUNTERPARTY_OPERAND: dict[kind, operand]` from every row that declares `counterparty:`:
each kind in that row's `emits` (all bands) maps to the row's counterparty operand. WITNESS's pairing
(`08_FI_06`'s owner: the roster and reader that pair a deed with its hand) reads it, deriving the claim's
subject from the act's operand through the act store (which WITNESS may read, `04` §A.2 `:180`), so the
Event itself stays targetless (`04` §B.9 `:433`): a witness of `argument.won` holds *(hearer,
argument.won)* with `seen.who` the arguer, and the hearer's regard for the arguer is moved by `_bond` as
for any deed done to him. A derivation, not a list: a new contested row is paired by declaring its
counterparty. A Partial is held by both and has no loser. (The counterparty is the one acted on; A-38's
party a verdict serves is the **beneficiary**, owned by `16_PESSIMIST_SC_C`; two different persons.)

**4. `engine/season/harness/corpus_run.py` — `attempts_on(w, actor, verb, subject) -> list`**, beside
`attempts` (the one owner of made and refused, over the act store): that actor's acts on that aim in
log order, each with its band and margin. A harness read. Nothing is deposited
(`rosters.yaml: undeposited_kinds`, ED-FI-0009, stands: a failed search is seen by nobody) and no
person-side reader is added: PES-DICE F-PES-DICE-05 measured, with a control, that a chooser weighing a
failed search changes nothing.

**5. `engine/season/harness/chronicle.py::lines`** prints, for a drawn act, one of six words read from
`Event.degree` and the kept margin: *triumph* (Overwhelming), *success*, *near thing* (Partial),
*narrow failure* (step 1), *failure* (step 2), *disaster* (step 3); and, where `attempts_on` returns
more than one act, *at the Nth attempt*.

## The gate (execution artifact)

Tests: NEW `engine/season/tests/test_stake.py`: `test_row_without_stake_pays_nothing`,
`test_partial_pays_one_step`, `test_failure_pays_shortfall_steps` (steps 1 to 3),
`test_success_never_pays`, `test_shortfall_edges_are_read_from_the_dice_engine_not_copied` (sweep the
Overwhelming edge to 4 and check step 3 moves), `test_scale_off_reproduces_pinned_hash`,
`test_staked_row_loads_as_shape_b_with_no_loader_exception`; and `test_counterparty_is_derived_from_the_row`
for edit 3. The story-bar plants below are tests in `engine/season/tests/test_storybar.py` (exists).

`PYTHONHASHSEED=0`, the valley fixture and the realm (sizes: audit §6.1), arms `off` and `on`
(`shortfall_scale`, with the six rows above declaring their stake cells):

1. **Control.** `off`: every content hash equal to the pins; S-68 and S-69 read 0 in the census.
2. **The disaster is rare and occurs.** `on`: step 3 occurs at two seeds or more and on fewer than one
   failure in five, re-measured on the A-5 sampler's quantised margin (the "one in five" was set on whole
   successes and is read again at landing); if it is commoner, the task is unfair, which is PES-DICE's
   finding F-PES-DICE-02 and is fixed at `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`, not here.
3. **The price is paid in a value.** Every stake write has a receipt whose `delta` is not `None`
   (needs `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 1); the sum paid differs between
   seeds.
4. **A loser exists.** For each contested row that executes: at least one witness claim whose subject
   is the counterparty; the counterparty's computed regard for the actor differs, after the Event, from
   the same world with edit 3 off.
5. **Census.** S-68, S-69, S-70 pass audit §6.1's clauses C1 to C6; S-71 passes C1 to C3 and C5.

Story bar test (`engine/season/tests/test_storybar.py`, the file `20_NARRATIVE_F` opens): a planted
Failure Event with margin −3.5 on a staked row reads *disaster* and one S-68; the same plant at −0.5
reads *narrow failure* and no S-68; with the stake's receipt removed, no S-68.

## The falsifier

- A row with stake cells whose Partial writes nothing, or whose Failure at step 3 pays the same as at
  step 1: edit 2 is not wired.
- `shortfall_step` returning 3 for a margin of −2.9 after the dice engine's Overwhelming edge is swept
  to 4: the edge was copied, not read.
- A Success that pays a stake: the rule leaked upward.
- Gate clause 4 passing with edit 3 off: the regard moved for another reason and the pairing is unread.

## NERS reading

- **N.** Cut it and four turns DICE names stay impossible, and MIL-A's and MAT-C's prices stay two
  private rules. Holds bottom-up (the row), top-down (the chronicle's words), laterally (the chooser's
  risk term reads the same key), diagonally (a duel's loser and an argument's are named by one
  derivation). It does not hold for a row with nothing to lose, and such a row declares no stake.
- **R.** A bad position still wins sometimes and now loses by degrees; a careful person can decline a
  staked act (strategy); the no-player half gains failures that leave marks. Complete at the extremes:
  a margin of `None` (an undrawn act) pays nothing; a body at zero cannot pay and the write is refused
  by the gate as any no-op is.
- **S.** One ladder read both ways; one stake rule for every row; existing kinds; the pairing owner
  FI-06 already names. Pauses nothing.
- **E, last.** One function, one size reader, one roster of three, one derivation, two harness reads,
  against four story kinds and two private rules retired. High.

## Cost class

Small build, one session. Edits 4 and 5: edit.

## Dependency edges

Needs first: `05_SC_contest_record_on_event.md` (the margin on the Event); `18_DETERMINISM_task_draw_for_uncontested_verbs.md`
(so `move`, `found`, `requisition` draw at all); `10_DICE_exported_face_rule_and_band_edges.md`.
Feeds: MIL-A, MAT-C (their Partial prices become the stake); `02_CHAR_what_an_act_risks.md`;
`23_STORY_B` (a birth's deepest shortfall); `23_STORY_D` (shapes S-68 to S-71). Batch E-2 of the audit.
