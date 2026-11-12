# 07 · SE — kernel repairs: amounts, the no-op wear write, the same-place move, arrival, and three stale pointers

## Status: PROPOSED

Carries findings F-SE-08, F-SE-10, F-SE-11 and resolutions R-SE-07 to R-SE-10 and R-SE-12 to R-SE-15 of
`audits/07_SE_audit.md`. Each item is an edit at one owner. None needs a ruling; each closes or narrows a
hole-register row by the five-step ladder, and the step is named.

## 1. What changes in `engine/season/` at runtime

| # | owner | runtime change | hash |
|---|---|---|---|
| A | `loop/effects_shared.py::_shift`, `_debit` | an amount that is not a positive whole number moves nothing; the act refuses | EQUAL in computed play (no computed act carries one) |
| B | `loop/matter.py`, the wear write | a Site whose wear is 0 is not written and emits no `condition.worn` | MOVER (declared): 248 fewer Events a season on the realm |
| C | `loop/effects_migration.py::_eff_move` | a move to where the mover already stands declines | MOVER (declared): 16 of 17 computed moves at seed 0 were this shape (H-329) |
| D | `loop/matter.py`, the travel pass | the `travel.ended` write carries what the arrival saw | MOVER (declared), behind a fixture shipped off |
| E | docstrings and pointer rows | none | none |

## 2. A · An amount is a positive whole number (H-306)

**Problem.** `_shift` and `_debit` (`loop/effects_shared.py:120-136`) apply any `amount`. The register row
measures: a `transfer` of −5 emits `transfer.made` and moves grain from receiver to giver; a
`requisition` of −5 leaves the seat's rung at −5; 2.5 is accepted; a `requisition` of 0 emits
`requisition.taken` and adds a `grain: 0` key. Stores are the economy's only ledger and yield its only
source (`effects_economy.py:220`), so a reversed or fractional move is a second source.

**Resolution (ladder step 5).** One owner already holds every store move; the rule goes there. Not at the
three effects (three copies), and not in the precondition (a typed cell cannot spell "whole").

**Edit.** `loop/effects_shared.py`:

```python
def whole_amount(amount) -> bool:
    """A store move's amount: a whole number of units, at least one. `bool` is refused (YAML `yes`)."""
    return isinstance(amount, int) and not isinstance(amount, bool) and amount >= 1
```

`_eff_transfer`, `_eff_exchange` (both amounts), `_eff_requisition`, `_eff_found` and `_eff_build` (each
price cell) return `NO_CHANGE` when it is false, before they build their `Change`, with one
`TRACE.decision` line naming the amount; the fold then emits the row's own refusal. `_shift` and
`_debit` themselves raise `InstrumentDefect` on a non-whole amount, so a new caller that skips the check
fails loudly rather than moving matter. `_eff_requisition`'s docstring sentence that a requisition of 0
is declined becomes true.

**Gate.** `engine/season/tests/test_in33_exchange.py` and `test_demand_delivery.py` gain the row's own
sweep (−5, 0, 1, 2.5, `True`) through the real fold on `harness/scarce.build`: only 1 moves stock; every
other value emits the refusal kind and leaves every rung's stores and the content hash equal to the
no-act arm. **Falsifier:** any of the four leaves a `kind: 0` key or a changed store. **Control:** the
shipped `scarce.main()` hashes (`d2730068…` named arm, `631b80ad…` unnamed, read at this commit) are
unchanged.

## 3. B · A wear of zero is not a write (F-SE-08)

**Problem.** `loop/matter.py:852-869` writes every Site every season. `wear_per_season` is 0 for
`dwelling` and `garrison`, so on the realm 248 of 322 `condition.worn` Events a season report a wear
that did not happen (read: 322 emitted in every season of every arm, while 248 Sites stand at 1000
after twenty seasons). Each is fanned to WITNESS. The same file states the rule it breaks, at the claim
decay pass (`:486-497`): *"AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
SUCCESS"*, and skips the write there.

**Resolution (ladder step 4: the file's own precedent).**

**Edit.** Inside the Site loop, before the write:

```python
        wear = w.fixtures.wear(s.kind) + pull.get(s.id, 0)
        if wear <= 0 or s.condition <= 0:
            continue                      # nothing wears: no write, no `condition.worn` (the claim-decay rule, above)
```

`rosters.yaml: wear_per_season`'s note (*"so every dwelling emits"*) and `harness/populated.py:1229-1232`'s
comment are corrected in the same commit. The second clause stops a Site already at 0 re-emitting.

**Gate.** `test_season_weather.py`'s realm pins re-recorded, said plainly in the commit; a new assertion
in `test_works_founding.py`: a world of one dwelling and one harbour emits exactly one `condition.worn`
per season. **Falsifier:** a `condition.worn` whose receipt has `before == after`. **Control:** a kind at
wear 10 emits as before; the lattice arm (`lattice_coupling` 500) still writes a wear-0 Site it pulls.

## 4. C · A move to where the mover stands is not a move (H-140)

**Problem.** `_eff_move` re-opens the `contain` leg and appends to `travel_leg` whatever the destination.
Read at this commit (`se_who.py 0 2`, seed 0, two seasons): all 11 executed cohort moves and 3 of 4
executed named moves name the mover's own rung; each costs the mover a scene for the rest of the season
(`decision/budget.py` reads `len(travel_leg)`) and is witnessed as `travel.moved`.

**Resolution (ladder step 4).** The tree has decided this shape twice: `_eff_migrate` declines a
destination the migrant already lives in (`effects_migration.py:204-209`), and a self-transfer is
refused as a no-op. `move` follows `migrate`.

**Edit.** In `_eff_move`, after the ladder check:

```python
    if home_of(w).get(a.actor) == dest:
        TRACE.decision(f"a move to where the mover already stands -> {a.actor} into {dest!r}", "H-140",
                       chose="change nothing, so the fold emits the row's refusal",
                       alternatives=["re-open the same leg under a new id (a digest move published as travel)"])
        return NO_CHANGE
```

`home_of` is imported from `queries/world_q` (already this file's source for `residence_of`). The row's
refusal stays `travel.blocked`; the formation side (a `to` that is the mover's own rung should not form)
is CR-49's shape applied to `move` and is the CHAR lane's (`decision/options.py`), cross-listed.

**Gate.** `test_migrate_capacity.py` gains the pair (same place refuses; one rung up moves).
**Falsifier:** `aperture 2 0` still shows a `travel.moved` whose destination equals the mover's rung
before the act. **Control:** a move between two rungs is byte-identical.

## 5. D · Arriving teaches the traveller the place (H-327)

**Problem.** After a move the traveller holds claims about himself and none about where he is.

**Resolution (ladder step 4).** MATTER already attaches what it read to the write that occasioned it:
the shortfall (`matter.py:647-649`) and the stock report (`_stock_report`). The arrival is MATTER's
`travel.ended` write (`:839-843`).

**Edit.** That write gains `observed=_arrival_report(w, pid, mode)`, where `mode` is a fixture
`arrival_report` (`off`, shipped; `on`) and the report is at most two `Observation`s about the rung the
traveller now stands in: `(rung, "stores:<default_store_kind>", units)` exactly as `_stock_report`
builds it, and `(rung, "held_by", holder id or None)` read through `world_q.governing_hold`. WITNESS
deposits them to the write's witnesses, the traveller among them. No new kind, no new channel.
[UNVERIFIED: that `held_by` is a predicate `LedgerReader` already reads; if it is not, the report ships
the stores line only and the holder line waits on H-195's `holder` operand.]

**Gate.** A test on `probes.tiny_world`: a person who moves from the hearth to the settlement holds, the
season after, a claim about the settlement's stores he did not hold before; with the fixture off he
holds none and the hash is the base. **Falsifier:** the claim appears in a co-located resident's ledger
only.

## 6. E · Pointers that have gone stale

| where | reads | should read | why |
|---|---|---|---|
| `systems/settlements/__init__.py` docstring | the geography file is *"read by `modules/mass_battle/terrain.py`"* | read by `engine/season/data/geography.py` (the host), handed to the module on `MassBattleInput.geography` | `data/geography.py:1-15`; the module opens no file |
| `registers/handoffs/HANDOFF_SE.md`, Open row 1 | *"the producer waits on ED-IN-0297"* | ED-IN-0297 closed at M5 (B); works are authored `venues.yaml: planned_works` rows; the residue is that no computed act declares one | `workplans/…_part14.md` AM-E-15; `venues.yaml:156-198` |
| `engine/season/requirements.yaml`, the settlement-management scale `note:` | *"in the realm only `restore` executes"*; *"`found`, `build` and `work` are formed and refused because no computed act declares a works"* | at this commit `restore` and `work` are attempted 0 times in three seasons at seed 0; `found` and `build` are refused on `exists:works`; `migrate` and `transfer` execute | `aperture 3 0` (audit §12) |
| `engine/season/harness/populated.py:1229` | *"NOTHING READS A DWELLING YET"* | `capacity` reads it (`world_q.py:1856`), called by `has_room` | the comment's own next sentence |

## 7. NERS reading (one for the set)

- **N.** Each cuts a false report: a reversed move called a gift, a wear called a wear, a journey to
  nowhere called travel. Cut the repairs and the witness layer keeps depositing claims about things that
  did not happen, which every reader above it inherits.
- **R.** Completeness at the extremes (negative, zero, fractional); the traveller's learning gives the
  no-player half one more way for knowledge to move.
- **S.** A and C apply rules the tree already applies to siblings, so one quantity stops having two
  treatments.
- **E, last.** Five edits of under ten lines each.

## 8. Cost class

Edit (A, B, C, E); small build (D). Three declared movers, each its own commit, each re-recorded once.
