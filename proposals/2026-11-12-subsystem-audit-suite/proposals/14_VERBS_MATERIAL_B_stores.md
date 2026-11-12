# 14 · VERBS · MATERIAL · B — `transfer`, `exchange`, `requisition`: store moves that name a place, carry a size and are drawn

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-21, C-22) — `carriage` is the roster member `distance` (`U5c_SC_one_obstacle_form.md` §2). Each row takes the route shape with flat `writes:` scaled by `task_fraction`, or declares `contests:` where two bands write different cells (`U5c_VERBS_residue_and_governance_owner.md` §1).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.2, 7b.4; F-R4-01, F-R4-08, F-R4-09): the three rows take shape (a) (flat `writes:`/`emits:`, magnitude through `graded_amount` on `task_fraction`, the failed draw in `emits_on_refusal`'s `draw` clause); `carriage`/`carriage_step` → OBS member `distance` with its fixture `distance_step` (U1 D-U1-11k, R-22), landed here as the member's first reader (OBS §4 step 6+); `delivery_share` is a sweep arm of `task_fraction`, not a second table (D-U1-11l); `exchange_terms` stays as the row's own content table (it scales the rate, a different quantity; U1 §3 "cost / price"); `graded_acts` → `graded_tasks` (D-U1-11i); `requisition.rendered` (BYZ_B) left to the landing order (C3-Y7); `distinct` is added to the loader's closed key set (R4 §1.2, N5); C3-R7 (G-13's fallback is the plan); A-81 (C3-C11), A-30, U3 batch B12, R4 7b.0 block.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_4b_DONE.md` "For another lane", MATERIAL-B item): Partial's remainder is read by `bills_due`, not deposited. `requisition.rendered` stays open (carried to the v12 stage, `W3_MOPUP_DONE.md`).

## Status: PROPOSED

Lands in batch: B12 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `14_VERBS_MATERIAL_A_mending.md` and the SE kernel, treasury and arc-needs proposals in the same batch (C3-D6).
Depends on: `18_DETERMINISM_task_draw_for_uncontested_verbs.md` items 1, 2, 4 (B07; C3-R1); `14_VERBS_MATERIAL_A_mending.md` §2 (B12: `graded_amount`); `U5c_SC_one_obstacle_form.md` §2 and `05_SC_obstacle_difficulty_and_modifiers_B.md` (B05: `distance` with `distance_step`, `stakes`, `regard`, `opposition`); `07_SE_arc_needs.md`, `07_SE_kernel_repairs.md`, `07_SE_treasury_granary_B.md` (B12).
Lane: SE. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; one `opus` read of each gate's spread. Test file: `engine/season/tests/test_vm_mat_b_stores.py` (one function per §6 gate; `harness/scarce.py` and `aperture 2 s` called inside it).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's trained score in the row's `capability:` (A-6; `pool_default` while none); talent as levels (A-7); a wound a level against the roll (A-8); the requisitioner's exercised seat helps only as the `office` level (D-U1-01), never as dice. Every draw takes `H(w.world_seed, w.tick, <actor id>, "<verb>.task")` (A-30). **A-81:** each failed draw's refusal Event (`transfer.failed`, `exchange.failed`, `requisition.resisted`) is witnessed by those present at the giving rung and deposits a claim of it to each; `requisition.resisted` is also a dominance deed `stability` reads (§4).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-13) — the roster the unrest kinds live in is `rosters.yaml: standing_routes: kinds: dominance` (`UNREST_KINDS` is its alias in `queries/person_q.py:517`); the name is corrected in place and the wider reach of the edit is stated.

Batch M-B of `audits/14_VERBS_MATERIAL.md` §18 (its §15, §3, §7). Needs batch M-A §2 (the family's draw).
Cites and does not redo: plan position CR-49 (`workplans/valoria_master_workplan_v11_part4.md:417`),
`07_SE_arc_needs.md` §3 b (the amount as a choice), `07_SE_treasury_granary_B.md` (where a treasury sits),
`07_SE_kernel_repairs.md` §2 (a whole amount), `05_SC_obstacle_difficulty_and_modifiers_B.md`. Reference
under CLAUDE.md §0.05. Read at `84d2a02`.

## 1. What changes in `engine/season/` at runtime

A store move is formed toward a place the mover knows of and has a reason to send to, never toward the
thing his question happens to be about; what arrives is drawn. Conservation is untouched: every band
moves whole units through `_shift`, and what does not arrive never left. Declared hash mover.

## 2. `transfer`

**Problem.** `mat_probe.py 0 2`: 43 attempted, 2 executed; 24 name the giver's own rung as `to`, 13 a
Person, Record or Proposition; the 2 that execute move one grain into the giver's own person-rung.

**Stamp.** `rosters.yaml: referent_classes` gains `Needy` (occasion-only, non-collection).
`queries/world_q.py`, new:

```python
def places_in_need(w: World, p: Person) -> tuple:
    """The rungs `p` has a reason to send stores to, from his OWN ledger and OWN edges, sorted, each once,
    never the rung he would give from (`containing_rung_of`, or a held seat's `seat_rung`):
      (a) a rung his newest claim of a `shortfall:<kind>` predicate is about, or his newest `stores:<kind>`
          claim puts at 0;
      (b) `Record.rung` of an unmade works on his own live `hold` (the rung `_cost` pays from);
      (c) where a person he knows to be obliged to a seat he holds stands (`ledger_names`, `home_of`)."""
```

**Formation.** `decision/options.py::opening_set`: a row may declare `distinct: [from, to]` (a column,
CR-49's *read from a row column, never from the verb's name*); a bag whose two named operands are equal
forms no Candidate. `data/verbs.py` adds `distinct` to the loader's closed set of row keys (unknown keys
are refused at load, `04` §B.13) and refuses a `distinct` member that is not an operand the row binds. `_derive_operand`: for a classed row that declares `shortfall_sourced`, `kind` and
`amount` are read from the newest shortfall claim about the bound `to` (today the reader keys on
`q.about` only, so a stamped rung gets the fixtures). `amount` then rides SE's `amount_shares`.

**Row** (unlisted columns unchanged):

```yaml
  - verb:        "transfer"
    referent_class: Needy
    distinct:    [from, to]
    capability:  none
    capability_note: "moving one's own stores draws on no skill; the draw is whether it arrives"
    difficulty:  plain          # + `distance` (OBS member 20): Fixtures distance_step per `contain` edge on the ladder path from `from` to `to`
    writes:  ["Rung.stores", "Rung.stores", "Tenure.term"]   # shape (a): one magnitude
    emits:   ["transfer.made", "term.renewed"]
    emits_on_refusal: {draw: ["transfer.failed"], <each derived clause>: ["transfer.refused"]}   # MAT_A §2 row 5 note
```

`_eff_transfer`: `moved = graded_amount(w, res, amount)` (the one table `task_fraction`: whole at
Overwhelming and Success, half at Partial, rounded up to whole units); `_shift(src, dst, kind, moved)`;
`_renewals(w, a, src.id, dst.id, moved)`. `delivery_share` 1000 / 1000 / 700 / 0 is a **sweep arm** of
`task_fraction` (D-U1-11l, C-23), not a fixture of its own. `distance` is OBS §2's member 20 with its one
fixture `distance_step` (`0.5`, swept 0 / 0.5 / 1; control 0; NUMBER row in `hole_register.yaml`): a member
lands with its first reader (OBS §2), and this batch (B12) is the first to land of its readers (`transfer`
here, `comply` in B28, `move`/`migrate` in B22, the institutions' `remove` folded into it), so the member
and its fixture land in this commit and no later proposal adds them again. `graded_tasks` gains `transfer`.

## 3. `exchange`

CR-49 lands as written with two changes: the class is `Market`, not the shared `Rung` (so `migrate`,
`march` and `convene` gain no formations), and the self-trade decline is the `distinct: [from, to]` column
above.

```python
def markets_known(w: World, p: Person) -> tuple:
    """The rungs, other than the one he would give from, about which `p`'s newest `stores:<kind>` claim for
    some kind is positive. Class Market. His own ledger only."""
```

`_derive_operand`, for a row declaring `stock_sourced: [kind, return_kind]` (a roster line beside
`shortfall_sourced_operands`): `kind` is the matter his newest `stores:` claims about `from` put highest;
`return_kind` is the matter his claims about `to` put positive that his claims about `from` put lowest,
and never `kind`; either falls back to its fixture (`default_store_kind`, `default_return_kind`) when he
holds no such claim. So a trader offers what his place has and asks for what it lacks.

```yaml
  - verb:        "exchange"
    referent_class: Market
    distinct:    [from, to]
    capability:  none           # `trade` when authored
    difficulty:  routine        # + `opposition` and `regard` (SC-B) of the holder his ledger names for `to`, when it names one
    writes:  ["Rung.stores", "Rung.stores"]   # shape (a): one exchange; the band scales its rate
    emits:   ["exchange.made"]
    emits_on_refusal: {draw: ["exchange.failed"], <each derived clause>: ["exchange.refused"]}   # MAT_A §2 row 5 note
```

`data/fixtures.py`: `exchange_terms={"Overwhelming": 1500, "Success": 1000, "Partial": 500}` (per-mille
of `return_amount` the actor receives for his `amount`; swept, with `1000/1000/1000` the control: par at
every winning band), with a NUMBER row in `hole_register.yaml`. It is the row's own content table: it
scales the **rate** of return, a different quantity from `task_fraction`'s share of an amount, so it is
not a second share table (U1 §3 "cost / price": a row that departs names its own per-mille table).
`_eff_exchange`: `back = min(held by dst of return_kind, ceil(return_amount × terms[band] / 1000))`, at
least 1; two `_shift`s as today. When CP-T08-05 gives a price, par is that price and this table scales
it. `graded_tasks` gains `exchange`.

## 4. `requisition`

**Stamp.** `rosters.yaml: referent_classes` gains `Larder`. `queries/world_q.py::larders_in_purview` is
stamped twice: as `Rung` exactly as today (so `migrate`, `march` and `convene` do not move), and as
`Larder` for the subset reached by a seat of his that grants **this row's own act** (`issue`), read off
the row (`VERB_TABLE["requisition"].eligibility`), never spelt. Measured need: at seed 2 four of ten
computed requisitions were `requisition.unauthorized`, each formed for a seat granting `dispatch` or
`convene` only.

```yaml
  - verb:        "requisition"
    referent_class: Larder
    capability:  none
    capability_note: "the office is the instrument: the exercised seat helps as the `office` level read off its row's `modifier:` (U1 D-U1-01), never as dice"
    difficulty:  routine        # + `stakes` (stakes_ob.requisition per third of the known stock asked) + `regard` of the cohort residing at the rung
    writes:  ["Rung.stores", "Rung.stores"]   # shape (a): one magnitude
    emits:   ["requisition.taken"]
    emits_on_refusal:           # keyed per clause, as in the tree (`verb_table.yaml:1037-1041`), plus the draw
      eligibility: ["requisition.unauthorized"]
      authority:   ["requisition.unauthorized"]
      stores:      ["requisition.refused"]
      write:       ["requisition.refused"]
      draw:        ["requisition.resisted"]
```

`15_INSTITUTIONS_BYZANTINE_B` e5 asks for `requisition.rendered` at Overwhelming. That would make two bands
emit different kinds and move the row to shape (b) (`contests: "a task"`). This file lands first (B12)
with the flat kind; if the kind is adopted, BYZ_B's batch (B33) converts the row (C3-Y7). The kind's name
is U1's and is not decided in U1's ledger at this reading.

At Partial the requisition moves half (`task_fraction`, rounded up to whole units; BYZ_B request 2 asks for at
least 1). The remainder still owed is not deposited by `_eff_requisition`: BYZ_B's `world_q.bills_due(w, p)`
reads it when read (`loop/witness` is the one writer of claims, `04` §A.2), so this row writes only the moved
amount.

`_eff_requisition`: `_shift(src, dst, kind, graded_amount(w, res, amount))` (the magnitude ladder: what
the collectors bring in). `Fixtures stakes_ob` (SC-B's table) gains `requisition: 0.5`. The `regard`
operand is the stance toward the actor of the one cohort whose `reside` edge is the requisitioned rung
(`stance_toward`, its one owner); absent where no cohort or several reside there. `rosters.yaml:
standing_routes: kinds: dominance` `[GROUNDED, 25 G-13: there is no roster `unrest_kinds`. `UNREST_KINDS` is an alias, `queries/person_q.py:517` `UNREST_KINDS = DOMINANCE_KINDS`, and `DOMINANCE_KINDS` is `roster_map("standing_routes", "kinds")["dominance"]`, `data/rosters.py:1001`. Adding a kind there adds it to every reader of dominance, not to `stability` alone]` gains
`requisition.resisted`, so a place that refused its lord is a deed `stability` counts as a taking is.
`graded_tasks` gains `requisition`.

## 5. Order of landing

1. `distinct:` column and its loader check (hash EQUAL until a row declares it).
2. `transfer` (with `places_in_need`); 3. `requisition` (with `Larder`); 4. `exchange` (CR-49's slot in
   B10-18b, after CR-48 as that card orders).
Each is its own declared mover. CR-49's exit clause (re-read `confer` and `oblige` against their pre-item
counts; a fall to 0 reverts the position alone) applies to all three, since each frees or takes scenes.

## 6. Gate and falsifier

- **`transfer`.** `python -m engine.season.harness.scarce`, named arm, extended to seeds 0 to 19: grain
  delivered > 0 and a second claim-sourced `transfer.made` (the two things F-SE-04's falsifier names),
  and the delivered amount takes more than one value across seeds. Realm, `aperture 2 s`: no attempted
  `transfer` whose `to` equals its `from` or is no rung. Control: `distance_step` 0 and `task_fraction`
  at its control arm `1 / 1 / 1 / 0` reproduce a whole delivery wherever the base difficulty is passed.
- **`requisition`.** `scarce.governed` with `amount_shares: [250, 1000]`: for one candidate the amount
  taken varies across seeds 0 to 19; the cohort's stance toward the steward differs after
  `requisition.resisted` and after `requisition.taken`. Realm: no computed `requisition.unauthorized`.
- **`exchange`.** Under SE's `ground` arm, seeds 0 to 2, three seasons: `exchange.made` > 0 between two
  settlements of unlike endowment; the importer's hunger band differs from the arm with `exchange`
  withheld (`Fixtures withheld_verbs`).
- **Conservation, at every band.** Total stores of each kind over all rungs are equal before and after
  every act of the three verbs (the W3 audit's weighing, as `F10` asserts it).
- **Planted failures.** Stamp the giver's own rung as `Needy`: the realm line must show self-transfers
  again. Bind `return_kind` to `kind`: no `exchange` may form. Pin the degree: each spread collapses.

## 7. NERS reading (E last)

N: play leaves the realm's stores where no play leaves them, to within four units of 13,690 (SE audit
§1.4); from the governor's side nothing he does is sized, from the place's side nothing answers him. R:
relief that arrives short, a levy that is resisted, a bargain that goes badly, each with a trail and none
needing a player. S: three verbs, one body (`_shift`), one draw, one decline column, one share table
(`task_fraction`); `exchange_terms` scales a rate, not a share. E, last: three stamps, one column, one
content table against three verbs that execute between zero and five times a season.

## 8. Cost class

Small build, three declared movers. Thin in consequence until `07_SE_ground_and_granaries.md` and
`07_SE_treasury_granary_B.md` give places unlike stock and seats a treasury.
