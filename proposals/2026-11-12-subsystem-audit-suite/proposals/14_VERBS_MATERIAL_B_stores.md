# 14 · VERBS · MATERIAL · B — `transfer`, `exchange`, `requisition`: store moves that name a place, carry a size and are drawn

## Status: PROPOSED

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
forms no Candidate. `_derive_operand`: for a classed row that declares `shortfall_sourced`, `kind` and
`amount` are read from the newest shortfall claim about the bound `to` (today the reader keys on
`q.about` only, so a stamped rung gets the fixtures). `amount` then rides SE's `amount_shares`.

**Row** (unlisted columns unchanged):

```yaml
  - verb:        "transfer"
    referent_class: Needy
    distinct:    [from, to]
    capability:  none
    capability_note: "moving one's own stores draws on no skill; the draw is the carriage"
    difficulty:  plain          # + `carriage`: Fixtures carriage_step per `contain` edge on the ladder path from `from` to `to`
    writes:
      Overwhelming: ["Rung.stores", "Rung.stores", "Tenure.term"]
      Success:      ["Rung.stores", "Rung.stores", "Tenure.term"]
      Partial:      ["Rung.stores", "Rung.stores", "Tenure.term"]
      Failure:      []
    emits:
      Overwhelming: ["transfer.made", "term.renewed"]
      Success:      ["transfer.made", "term.renewed"]
      Partial:      ["transfer.made", "term.renewed"]
      Failure:      ["transfer.failed"]
    emits_on_refusal: ["transfer.refused"]
```

`data/fixtures.py`: `carriage_step=0.5` (swept 0 / 0.5 / 1; 0 is the control at which only the base
difficulty stands), and a table `delivery_share={"Overwhelming": 1000, "Success": 1000, "Partial": 700,
"Failure": 0}`: a delivery is whole at Success, which a magnitude is not, so it has its own row of the
same shape, read by the same `graded_amount` (one function; the table is its argument). `_eff_transfer`:
`moved = graded_amount(w, res, amount, table="delivery_share")`; `_shift(src, dst, kind, moved)`;
`_renewals(w, a, src.id, dst.id, moved)`. `rosters.yaml: obstacle_terms` gains `carriage`;
`graded_acts` gains `transfer`.

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
    writes:  {Overwhelming: ["Rung.stores", "Rung.stores"], Success: ["Rung.stores", "Rung.stores"], Partial: ["Rung.stores", "Rung.stores"], Failure: []}
    emits:   {Overwhelming: ["exchange.made"], Success: ["exchange.made"], Partial: ["exchange.made"], Failure: ["exchange.failed"]}
    emits_on_refusal: ["exchange.refused"]
```

`data/fixtures.py`: `exchange_terms={"Overwhelming": 1500, "Success": 1000, "Partial": 500}` (per-mille
of `return_amount` the actor receives for his `amount`; swept, with `1000/1000/1000` the control: par at
every winning band). `_eff_exchange`: `back = min(held by dst of return_kind, ceil(return_amount ×
terms[band] / 1000))`, at least 1; two `_shift`s as today. When CP-T08-05 gives a price, par is that
price and this table scales it. `graded_acts` gains `exchange`.

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
    capability_note: "the office is the instrument; `faculty` adds whatever weight DICE gives a seat"
    difficulty:  routine        # + `stakes` (stakes_ob.requisition per third of the known stock asked) + `regard` of the cohort residing at the rung
    writes:  {Overwhelming: ["Rung.stores", "Rung.stores"], Success: ["Rung.stores", "Rung.stores"], Partial: ["Rung.stores", "Rung.stores"], Failure: []}
    emits:   {Overwhelming: ["requisition.taken"], Success: ["requisition.taken"], Partial: ["requisition.taken"], Failure: ["requisition.resisted"]}
    emits_on_refusal:           # unchanged, keyed per clause
      eligibility: ["requisition.unauthorized"]
      authority:   ["requisition.unauthorized"]
      stores:      ["requisition.refused"]
      write:       ["requisition.refused"]
```

`_eff_requisition`: `_shift(src, dst, kind, graded_amount(w, res, amount))` (the magnitude ladder: what
the collectors bring in). `Fixtures stakes_ob` (SC-B's table) gains `requisition: 0.5`. The `regard`
operand is the stance toward the actor of the one cohort whose `reside` edge is the requisitioned rung
(`stance_toward`, its one owner); absent where no cohort or several reside there. `rosters.yaml:
unrest_kinds` `[UNVERIFIED: the roster's exact name; the SE audit cites `UNREST_KINDS`]` gains
`requisition.resisted`, so a place that refused its lord is a deed `stability` counts as a taking is.
`graded_acts` gains `requisition`.

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
  `transfer` whose `to` equals its `from` or is no rung. Control: `carriage_step` 0 and
  `delivery_share` all 1000 reproduce a whole delivery wherever the base difficulty is passed.
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
needing a player. S: three verbs, one body (`_shift`), one draw, one decline column; the delivery table
and the magnitude table are one function's two arguments, which is the one place this batch asks S to
tolerate a second row. E, last: three stamps, one column, two tables against three verbs that execute
between zero and five times a season.

## 8. Cost class

Small build, three declared movers. Thin in consequence until `07_SE_ground_and_granaries.md` and
`07_SE_treasury_granary_B.md` give places unlike stock and seats a treasury.
