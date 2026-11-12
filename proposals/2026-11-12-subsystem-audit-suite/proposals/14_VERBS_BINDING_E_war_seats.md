# VB-E — the war seats' two acts: an order of battle where a field will be fought, a town yielded by a draw

Reconciled: 2026-11-12, U5d closure — folded the land rulings (**A-57, A-58, A-65, A-66**) at the coordinator's direction (this file is the BINDING lane's; its verdict rows are closed by U5c). A yielded town is the aggressor's win by concession (A-3), so `_eff_surrender`'s cession carries the seats anchored on the place in the same write (`U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 2: `_take_hold(..., seats=…)`); edits 7–8 gain those seat edges in `writes`. At Failure (`surrender.rejected`) the field goes ahead; its end state decides who stands on the ground, and a winner then chooses to seize, occupy or withdraw (A-66). `Front`'s definition is unchanged.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-25) — edit 9's audience is the `heard_by: residents` cell on the `a holding` prize row, with `toward: to`, read by the one audience function (`U5c_VERBS_residue_and_governance_owner.md` §2); `contest_input` names no verb.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — applied `unified/U3_CONFLICT_LEDGER.md` C3-C5 (`unified/work/R4_READ.md` 7b.3: a matured Partial cession leaves the place unheld; nothing re-opens the surrenderer's hold), C3-L12 with C3-L7 (title and seats pass only by an act whose actor has a basis: the U5d head line's "seats in the same write" is superseded; see "The land" below), C3-C11 (A-81), A-30 keys, U3 batch B23 and its dependencies, R4 7b.0 block. The U5d head line above is kept as history; where it and this line disagree, this line follows the later decisions C3-L7 and C3-L12.

## Status: PROPOSED

Lands in batch: B23 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), with `U5d_FA_land_and_seats_pass_on_a_won_march.md`; E3's two unwithhold commits each a separate declared mover inside B23.
Depends on: `14_VERBS_PHYSICAL_B_field_and_ruin.md` (B22: fields fought, `siege.pressed` produced); `06_FA_levy_through_the_seat_B.md`, `06_FA_remit_grant_by_row.md` (B21); `04_MB_playable_field_scenario.md` (B20); `U5d_FA_land_and_seats_pass_on_a_won_march.md` (B23: the seats' `revocation: holder_of_rung`, C3-L7); `U5c_VERBS_residue_and_governance_owner.md` §2 (B07: the `a holding` row, `toward: to`); `14_VERBS_BINDING_C_turnover.md` edit 2 (B21: `_provisional_term`).
Lane: FA. Tier (R4 7b.0 (1)): E1, E3 `sonnet` producer, effort `high`; E2 (the contested row) `sonnet` producer with one `opus` read of the 40-seed band table. Test file: `engine/season/tests/test_vb_e_war_seats.py` (one function per gate; the existing `test_cp_t04_07_surrender.py` stays the effect's unit test).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the surrenderer's trained score (A-6), talent as levels (A-7), a wound a level against the roll (A-8). The `surrender` draw takes `H(w.world_seed, w.tick, <actor id>, "surrender.holding")` (A-30).

**The land (C3-L7, C3-L12; A-58, A-66).** `_eff_surrender` (T, `loop/effects_information.py:1092`) cedes the
**rung's** hold to the receiver through `_take_hold` (T, `:978`), a handover of the surrenderer's own hold.
It does not write the seats anchored on the place: their holders are other persons, and `04` §C.2 lists no
basis by which the surrenderer's act closes their holds. Those seats pass by the **receiver's** own later
act, exactly as after a won field: each such seat row carries `revocation: holder_of_rung`
(`U5d_FA_land_and_seats_pass_on_a_won_march.md` e1 as rewritten by C3-L7), so the receiver, now holding
the rung, closes and claims them through the existing revocation and claim bases, or chooses not to
(A-66: seize, occupy without seizing, withdraw). `_take_hold` gains no `seats=` argument from this file.

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
   `confer`. The seat edges are not in these `writes` (see "The land" above). **Durable write of the
   Failure band (A-81; C3-C11):** `surrender.rejected` is witnessed by the place's residents (the
   `reception` audience) and the besieger's men present, and deposits a claim of it to each; the field
   then goes ahead.
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
  after O/S `holder_faction_of(place)` is the receiver's faction; after Partial the receiver's termed hold
  matures at `provisional_term` and the place stands unheld (`holder_faction_of(place)` is `None`): a
  vacant holding, claimable by `seize`, `establish` or a later cession, and the surrenderer may re-take it
  only by his own act (C3-C5; `04` §B.8 T-n: a matured term only closes); after Failure the field is
  fought. The anchored seats do not move with the cession; a receiver who then forms the seat step moves
  them, and one who does not leaves them with their holders.

## Falsifier

Stamp every known Rung as `Front`/`Besieged`: refusals return. Pin the roll: one band only. A test that
reads `holder_faction_of(place)` equal to the surrenderer's faction after a Partial term matures fails
(no basis re-opens his hold). Unwithhold
before P-B: both rows form for nobody (empty stamps), which is the reading that shows P-B is the
dependency, not this file.

## What it does not do

It does not make fields happen (P-B), decide who commands (FA-P2, FA-B2), set terms of surrender (the
covenant route), or change how the field reads an order (MB).

## NERS reading

N: without them a commander's only war decision is to march, and every siege is a battle or a ruin. R: a
town may refuse its lord's surrender; a provisional cession lapses into an unheld place both sides may
contest. S: the same named-class route
and Partial shape as VB-A to VB-D; one roll owner. E (last): two ledger reads and one band map.

## Cost class

Small once P-B has landed: two classes and stamps, one prize, one contested row, one optional `term`
parameter, two unwithhold commits.
