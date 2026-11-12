# VB-E — the war seats' two acts: an order of battle where a field will be fought, a town yielded by a draw

## Status: PROPOSED

Source: `audits/14_VERBS_BINDING.md` §0.2, §7 (`marshal`), §8 (`surrender`); batch E, the last. Depends on
`14_VERBS_PHYSICAL_B_field_and_ruin.md` (PHYSICAL P-B: fields fought, `siege.pressed` produced),
`06_FA_remit_grant_by_row.md` (FA-P2: only commanding seats hold `dispatch`), `06_FA_levy_through_the_seat_B.md`
(FA-B2) and MB's `04_MB_playable_field_scenario.md` (the field that reads the order). Edits none of them.

## What it changes in `engine/season/` at runtime

1. `marshal` forms only on a place where the asker's side may fight (a named class `Front`).
2. `surrender` forms only on a place a siege presses this season within the asker's seat's purview (a
   named class `Besieged`), and becomes contested: the town yields, yields provisionally, or will not.
3. Both rows leave `withheld_verbs` (`data/fixtures.py:1157`), each a separate declared mover.

Nothing moves until (3); (3) lands only after P-B, because before it neither row has an occasion
(`siege.pressed` never emitted; fields fought 0, `audits/14_VERBS_PHYSICAL.md` §0.3).

## The problem (evidence)

- Both rows are withheld (eligible 26, formed 0 at seeds 0 and 1). Their notes say why: *"formable, it
  moves every seeded season"* — on the shared `Rung` class they would form on every known place and be
  refused (`marshal`) or declined by the effect (`surrender`: *"THE COST, STATED: Candidates form and are
  refused"*).
- `surrender` cedes with certainty once its effect's tests pass; the standing rule wants it drawn.
- `marshal` writes paper; whether a line follows its order is the field's draw (MB), so it stays
  uncontested (audit §0.2's stated exception).

## The resolution, decided

Formation from the occasion the actor can read (ladder step 4, `Detainee`'s route), as in VB-A and VB-B:
both stamps read only his own ledger (AX-2), so they compose nothing new world-side.

- `Front`: places named by a `march.declared` claim in his ledger whose target is held by his faction or
  whose marching side is his faction, within his seat's purview.
- `Besieged`: places named by a `siege.pressed` claim of this season in his ledger, within his seat's
  purview.

`surrender` drawn (audit §0.2): prize `a holding` (new), no person opponent, `difficulty` `routine` +
`reception` (audience: the place's residents, toward the receiver's faction). O/S cede; Partial cedes with
the receiver's hold termed (`_provisional_term`, VB-C edit 2); Failure: `surrender.rejected`, no write,
the field goes ahead.

## Exact edits, by owner

**Commit E1 — `marshal` formation.**

1. `data/verbs.py`: `FRONT_CLASS = "Front"`; `rosters.yaml: referent_classes` adds `Front` with a note.
2. `queries/world_q.py`: `fronts_known(w, p) -> tuple`, from his own ledger's `march.declared` claims
   (target and side read through the claim's content, `content_said`), filtered by `purview_reaches` of a
   seat he holds granting `dispatch`; `questions_for` appends its pairs to the classed tuple.
3. `verb_table.yaml`, `marshal`: `referent_class: Front`, note naming VB-E and its revert
   (`referent_class: Rung`).

**Commit E2 — `surrender` formation and draw.**

4. `data/verbs.py`: `BESIEGED_CLASS = "Besieged"`; `rosters.yaml: referent_classes` adds it.
5. `queries/world_q.py`: `sieges_known(w, p) -> tuple`, his ledger's `siege.pressed` claims made on this
   tick or the season's, filtered as above; appended to the classed tuple.
6. `rosters.yaml: contest_subsystems.prizes`: add `"a holding"` (the `a seat` row's fields).
7. `verb_table.yaml`, `surrender`: `referent_class: Besieged`; `contests: "a holding"`; `difficulty:
   routine`; writes `["Tenure.until", "Tenure.since", "Tenure.term"]` at O/S/P, `[]` at Failure; emits
   `place.surrendered` at O/S/P, `surrender.rejected` at Failure; `emits_on_refusal` flattened to
   `surrender.refused` under every key (contested-row rule). `Tenure.term` is check-only at O/S, as on
   `confer`.
8. `loop/effects_information.py::_eff_surrender` → `_take_hold(..., term=_provisional_term(w, a))` at
   `Partial`; `_take_hold` gains an optional `term` passed to the `Tenure` it opens (one constructor).
9. `seam/wrappers/sigma.py::contest_input`: `reception` audience = the residents of the place
   (`reside` edges on it), toward the receiver's faction (`faction_holding(receiver)`).

**Commit E3 — unwithhold, after P-B.**

10. `data/fixtures.py:1157`: drop `"marshal"` (one commit) and `"surrender"` (a second); each re-pins the
    realm hash with its reading recorded.

## Gate (execution artifact)

- E1+E3 (`marshal`): after P-B, a seeded realm run where a field is fought and `field_input` reads an
  `order_of_battle` for at least one side; planted: flip that order's `role`, and the field's degree or
  casualties move. Formed persons are only those with a `Front` referent.
- E2+E3 (`surrender`): after P-B, a run with a `siege.pressed`; across 40 seeds all four bands occur;
  after O/S `holder_faction_of(place)` is the receiver's faction; after Partial the receiver's hold
  matures and the place reverts at `provisional_term` unless re-taken; after Failure the field is fought.

## Falsifier

Stamp every known Rung as `Front`/`Besieged`: refusals return. Pin the roll: one band only. Unwithhold
before P-B: both rows form for nobody (empty stamps), which is the reading that shows P-B is the
dependency, not this file.

## What it does not do

It does not make fields happen (P-B), decide who commands (FA-P2, FA-B2), set terms of surrender (the
covenant route), or change how the field reads an order (MB).

## NERS reading

N: without them a commander's only war decision is to march, and every siege is a battle or a ruin. R: a
town may refuse its lord's surrender; a provisional cession can fall back. S: the same named-class route
and Partial shape as VB-A to VB-D; one roll owner. E (last): two ledger reads and one band map.

## Cost class

Small once P-B has landed: two classes and stamps, one prize, one contested row, one optional `term`
parameter, two unwithhold commits.
