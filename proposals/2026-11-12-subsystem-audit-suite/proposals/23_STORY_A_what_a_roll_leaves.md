# STORY-A — what a roll leaves: the shortfall scales the loss, a stake is paid, the other party is named, an attempt can be counted

## Status: PROPOSED

Source: `audits/23_STORY_ENABLEMENT.md` §2 rows S-68 to S-71 and S-29, §4.2 G1; the four turns
`audits/16_PESSIMIST_DICE.md` §3.1 lists as *"never, as coded"* (the disaster, the success that costs,
the contest with a loser, the comeback). Composes on, and does not restate:
`05_SC_contest_record_on_event.md` (the settled margin on `Event.ending`),
`10_DICE_exported_face_rule_and_band_edges.md` (the band edges as exported facts),
`08_FI_06_testimony-names-a-hand.md` (the pairing that travels with a deed),
`02_CHAR_relations_have_a_ground.md` with PES-CHAR resolution 11 (`_bond` for every deed with a person as
patient), `02_CHAR_what_an_act_risks.md` (the chooser's risk term), `09_WR_B_chronicle_that_tells.md`.
Reference only (`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

At ship, nothing: no row declares a `stake:` and `shortfall_scale` is `off` (the control), so every
content hash is today's. With a row's `stake:` authored and the fixture on: a Partial on that row pays
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
    Overwhelming edges the dice engine exports (1 and 3 today: "3 or more is always overwhelming",
    mirrored). No number is typed here: both edges are read from the one owner."""
```

It reads the two edges from the dice engine's exported band edges
(`10_DICE_exported_face_rule_and_band_edges.md`), so the mirror cannot drift from the ladder. A
magnitude-bearing Failure write is multiplied by it exactly as a Success write is multiplied by
`DEGREE_STEP[band]`; a categorical Failure write (a deposit, an edge closed) is unchanged.

**2. `engine/season/verb_table.yaml` — an optional row key `stake:`; `rosters.yaml: stakes`;
`loop/effects_shared.py::_pay_stake`.**

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

```python
def _pay_stake(w: World, a: Act, res: Resolution, steps: int) -> list[Change]:
    """The row's declared `stake:` paid `steps` times, through the gate, on the actor (body), on the
    rung the act draws on (stores) or in each present witness's stance toward him (standing). Returns
    `[]` for a row with no stake, for `steps == 0`, and at `shortfall_scale == "off"`."""
```

The fold (`loop/resolve.py`, where it applies a row's band writes) calls `_pay_stake` after the row's
own effect with `steps = 1` at Partial and `steps = shortfall_step(res.result["settled_margin"])` at
Failure. The writes emit the matrix rows' own declared kinds (`body.changed`, `stores.changed`,
`stance.moved`), `argue`'s precedent for a second emitter; no kind is added. Fixtures in
`data/fixtures.py`, each with a hole-register row graded `assumption` and its sweep:
`shortfall_scale = "off"` (control, SHIPPED) `/ "on"`; `stake_body` (proposed: the hunger pass's own
`body_step`, so one step of a stake is one season's hunger); `stake_stores` (proposed one quarter of the
amount); `stake_standing` (proposed one deed step in the regard unit `02_CHAR_scar_cap_and_regard_unit.md`
fixes). `[ASSUMPTION; medium; Jordan to correct]` on all three sizes.

First rows to declare one, each replacing a per-row rule a suite proposal wrote (the row's owner lane
adopts the key; this file edits no row): `move`, `migrate` → `stake: body` (MIL-A's *arrives spent* is
the Partial step); `found`, `build` → `stake: stores` (MAT-C's *costs more, or loses part*);
`requisition`, `sabotage` → `stake: standing`. `02_CHAR_what_an_act_risks.md`'s cost term reads the same
key, so what the chooser fears and what the fold charges are one fact.

**3. `engine/season/data/verbs.py` — the counterparty is the patient of a contested outcome.** Derive,
at load, `PATIENT_OPERAND: dict[kind, operand]` from every row that declares `counterparty:`: each kind
in that row's `emits` (all bands) maps to the row's counterparty operand. WITNESS's pairing
(`08_FI_06`'s owner: the roster and reader that pair a deed with its hand) reads it, so a witness of
`argument.won` holds *(hearer, argument.won)* with `seen.who` the arguer, and the hearer's regard for
the arguer is moved by `_bond` as for any deed done to him. A derivation, not a list: a new contested
row is paired by declaring its counterparty. A Partial is held by both and has no loser.

**4. `engine/season/harness/corpus_run.py` — `attempts_on(w, actor, verb, subject) -> list`**, beside
`attempts` (the one owner of made and refused, over the act store): that actor's acts on that aim in
log order, each with its band and settled margin. A harness read. Nothing is deposited
(`rosters.yaml: undeposited_kinds`, ED-FI-0009, stands: a failed search is seen by nobody) and no
person-side reader is added: PES-DICE F-PES-DICE-05 measured, with a control, that a chooser weighing a
failed search changes nothing.

**5. `engine/season/harness/chronicle.py::lines`** prints, for a drawn act, one of six words read from
`Event.degree` and the kept margin: *triumph* (Overwhelming), *success*, *near thing* (Partial),
*narrow failure* (step 1), *failure* (step 2), *disaster* (step 3); and, where `attempts_on` returns
more than one act, *at the Nth attempt*.

## The gate (execution artifact)

`PYTHONHASHSEED=0`, the valley fixture and the realm (sizes: audit §6.1), arms `off` and `on`
(`shortfall_scale`, with the six rows above declaring their stake):

1. **Control.** `off`: every content hash equal to the pins; S-68 and S-69 read 0 in the census.
2. **The disaster is rare and occurs.** `on`: step 3 occurs at two seeds or more and on fewer than one
   failure in five; if it is commoner, the task is unfair, which is PES-DICE's finding F-PES-DICE-02
   and is fixed at `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`, not here.
3. **The price is paid in a value.** Every `_pay_stake` write has a receipt whose `delta` is not `None`
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

- A row with `stake:` whose Partial writes nothing, or whose Failure at step 3 pays the same as at
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
- **E, last.** One function, one row key, one roster of three, one derivation, two harness reads,
  against four story kinds and two private rules retired. High.

## Cost class

Small build, one session. Edits 4 and 5: edit.

## Dependency edges

Needs first: `05_SC_contest_record_on_event.md` (the margin on the Event); `18_DETERMINISM_task_draw_for_uncontested_verbs.md`
(so `move`, `found`, `requisition` draw at all); `10_DICE_exported_face_rule_and_band_edges.md`.
Feeds: MIL-A, MAT-C (their Partial prices become the stake); `02_CHAR_what_an_act_risks.md`;
`23_STORY_B` (a birth's deepest shortfall); `23_STORY_D` (shapes S-68 to S-71). Batch E-2 of the audit.
