# SE — the granary shares, the dearth is reported when it begins, and a death by hunger says so

Reconciled: 2026-11-12, U5d closure — folded the ladder-closed **D-69** (famine reports once; the never-stocked edge repaired). R2's last clause ("A ladder no rung of which has ever held the kind stays silent, as ruled") is rewritten: a cohort short for the first time on a ladder that never held the kind is reported once, at the first rung of its ladder, as a crossing from "no report yet"; thereafter silence, as the 2026-10-12 cadence has it. Edit 2 gains that arm; the shipped realm's season-0 ladders therefore report once each (a declared mover the original text did not have). J-1 is closed by it. Edit 4 (`tend` does not answer hunger) is owed to PC and composes with A-56 (`tend` is a cohort move).

## Status: PROPOSED

Source: `audits/16_PESSIMIST_SE.md` F-PES-SE-01, -03, -04; §1.2 A-1; resolutions R-PES-SE-01 to -04.
Read at `d161a61`. Reference only (`CLAUDE.md` §0.05). Lane SE; edit 4 is owed to PC.

It composes on, and does not replace: `07_SE_ground_and_granaries.md` (the endowment, the stocked
larders, the remainder walk `larder_walk`), `07_SE_treasury_granary_B.md` (where the relief stock sits),
`07_SE_population_census.md` R1 (the loss per head) and `16_PESSIMIST_GAME_the_world_draws.md` (the
severity of the loss, drawn). Those give a realm places that differ and a relief stock; this makes the
stock behave as a shared store and makes its failure a fact somebody can learn and a record can retell.

## What it changes in `engine/season/` at runtime

1. When a rung cannot feed everyone who draws on it, its stock is **shared in proportion to want**, the
   indivisible remainder by a keyed draw, where today the eater first in sorted id takes all.
2. A cohort that goes unfed **for the first time** at a rung that once held the kind is reported at that
   rung, whether the rung was drained inexactly, exactly, or in an earlier season. Today only the
   inexact drain reports.
3. A hunger fall and a hunger death carry their **cause** on the Event.
4. A cohort the larder cannot feed is **not restored by `tend`**.

No shipped hash moves at edits 1 to 3 in `build_realm`: every settlement there eats from its own rung in
surplus (one eater per rung, `total <= held`), and its season-0 ladders hold no key for any kind, which
edit 2 leaves silent as the ruling has it (H-160 limit 3). `harness/scarce.py` has one eater on the short
rung, so its draw is unchanged; its report set is unchanged (its dearth is an inexact drain). Edit 3
moves every hash in which a body falls by hunger (the cause list is part of the Event), a declared mover.
Edit 4 moves any run in which a short cohort is tended: the realm's season 1 (the season-0 fall is
tended there today).

## The problem, with evidence

All runs under `…/scratchpad/runs/PES_SE/`, `PYTHONHASHSEED=0`.

- **Id order.** `kernel.py` K2: two towns of weight 2 on one territory rung holding grain 4, salt 2
  (half of what both want). The town first in sorted id takes grain 4, salt 2; the other takes nothing
  and falls 60. The module feeds eaters in the order it is handed (K2's second case), and the host
  hands it sorted pids (`queries/world_q.py:1386`), so which town starves is a fixed function of its id.
- **The unreported town.** The same run: `SubsistOutcome.shortfalls` is `()`. The first eater drained
  the rung to exactly 0, the second eater's walk found no rung holding more than 0 and recorded
  `source None`, and `subsist` marks a rung drained only for a cell with a source
  (`modules/settlements/subsist.py`, the `if src is not None: drained…` branch).
- **Across seasons.** K7: a granary stocked with exactly two seasons of one town's need feeds it twice,
  ends at 0 with nobody short, and from the third season the town falls 60 a season with no report,
  ever. One unit more in the granary and the report fires once, in the third season.
  `runs/SE/se_ground.py:20` stocks its granaries at whole seasons of deficit *less one unit*.
- **The death.** `pes_noacts.py famine 0 6`: eleven cohorts die of hunger in season 2; the first death
  Event has `causes` of length 1 and `observed=()`. `loop/matter.py::_die` chains to an earlier
  *death* of the same person, else `ROOT`; the hunger `body.changed` chains to the cohort's own previous
  `body.changed`, else `ROOT` (`matter.py:699-705`).
- **`tend`.** `pes_play.py {0,1} 2 fail`: 41 of 44 starving cohort-seasons end at body 1000; cohort
  `tend` executed 21 and 20 times against 0 in the fed arms (hole row H-304).

## The resolution (decided)

**R1. A short rung is shared.** For each kind, in rounds: every eater with want left points at the first
rung on its ladder that holds any of the kind at the start of the round and that it has not yet drawn
from this draw. Per rung, if the claims fit, each takes its claim; if they do not, each takes
`held × claim // total` and the units left over go one each, in the order of a permutation the host
draws for the season, to claimants still short. Under `larder_walk: first` (shipped) there is one round;
under `through` (the first lane's R4) rounds repeat until one moves nothing. Sharing is the store's
arithmetic (conservation: the takes sum to what was held); the remainder is the one thing that could go
either way, so it is drawn (the standing rule). Ladder step 5; the rejected alternative is a full keyed
shuffle of who eats first, which keeps winner-takes-all and only changes the winner.

**R2. The crossing is the cohort's, not the store's.** A cohort short of a kind this season that was not
short of it at the last MATTER has crossed into dearth. The crossing is reported at the first rung on
its ladder whose stores carry the kind (at any value, 0 included: the key is written when a rung first
holds the kind and survives its emptying), with the subtree gap the module already computes. A ladder
no rung of which has ever held the kind stays silent, as ruled. Ladder step 3: `matter.py:629` already
says *"The emission is the CROSSING into dearth, not the state"*; this makes the code agree with its
own sentence. Whether a chronic dearth should speak again is `audits/16_PESSIMIST_SE.md` §6.2 J-1 and
is not decided here.

**R3. Hunger is a cause.** The hunger `body.changed` cites the last `stores.changed` at the rung the
cohort was short at (R2's rung), else what it cites today. The death cites the fall that brought it.
No reader in the loop branches on a cause, so nothing a person does changes; a chronicle, a claim's
provenance and an ending classifier can now read *died of hunger at X*.

**R4. Food, not nursing, mends hunger.** `tend` declines a cohort that the larder, as it stands, would
leave unfed at the next draw. An eligibility read (a Query over the present world), not a new state.

## Edits

### 1 · `engine/season/queries/inputs.py::LarderInput`, `queries/world_q.py::_larder_parts`, `modules/settlements/larder.py::larder_draw`

`LarderInput` gains `order: tuple = ()`: the eaters' pids in the season's drawn order. The host fills it:

```python
keyed = draw_factory(w.world_seed, lambda: w.tick)
order = tuple(keyed("larder", "remainder").sample(sorted(cohort_pids), len(cohort_pids)))
```

`()` is the control arm (remainder in host order) and reproduces today's remainder rule for tests that
plant it. `larder_draw`'s body becomes the round loop of R1. Its cell keeps today's shape
`(kind, want, take, src)` under `first`; under `through` it is the first lane's list of `(src, take)`,
unchanged by this proposal. The module still draws nothing: the permutation arrives on its typed input.

### 2 · `queries/inputs.py::SubsistInput`, `queries/world_q.py::subsist_input`, `modules/settlements/subsist.py::subsist`, `loop/matter.py`

`SubsistInput` gains `short_before: tuple = ()` — `((pid, (kind, …)), …)` projected from
`World._subsistence_shortfall` (the field's first loop reader) — and `once_held: tuple = ()` —
`((rung, (kind, …)), …)`, the kinds each ladder rung's `stores` carries a key for.

In `subsist`, after the existing `drained` pass:

```python
before = {pid: frozenset(kinds) for pid, kinds in inp.short_before}
held_once = {rung: frozenset(kinds) for rung, kinds in inp.once_held}
ladders = dict(inp.larder.ladders)
for row in draw.rows:
    for kind, want, take, src in row.cells:
        if take >= want or src is not None or kind in before.get(row.pid, ()):
            continue                      # fed; or already counted as drained; or not a crossing
        at = next((r for r in ladders.get(row.home, ()) if kind in held_once.get(r, ())), None)
        if at is not None:
            drained.setdefault(at, set()).add(kind)
```

`shortfalls` is then computed as today. In `loop/matter.py`, `short_seen[rung]` rides the rung's larder
write where one exists this barrier (today's path). Where the rung has no write this barrier (it was
already empty), the Observation rides the `body.changed` write of the first short cohort homed under
it, by `observed=` on that write. With `body_step` at 0 there is no such write and the crossing is
unreported, which the control arm's note should say. `[UNVERIFIED: that WITNESS's seat channel routes
an Observation by its subject rung when it rides a Person's write; `loop/witness.py::SEAT_CHANNEL` was
not opened. If it routes by the written subject, the edit there is to route by `Observation.subject`.]`

### 3 · `loop/matter.py` (the hunger pass and `_die`)

```python
prior_b = (w.last_emission_of("stores.changed", short_at[pid])      # R2's rung, where there is one
           or w.last_emission_of("body.changed", pid, written=True))
…
if fall.body_after <= 0:
    _die(w, token, pid, cause=fell.id if fell else None)
```

and `_die(w, token, pid, cause=None)` writes `causes=[cause] if cause else ([prior_d] if prior_d else
[ROOT])`. The bodies-clock caller passes nothing and is unchanged.

### 4 · `loop/effects_combat.py::_eff_tend` (owed to PC)

After the `p is None` decline:

```python
if p.is_cohort and any(take < want for row in world_q.subsistence_draw(w).rows
                       if row.pid == who for _k, want, take, _s in row.cells):
    return NO_CHANGE                      # -> `tend.refused`: the larder cannot feed them
```

An effect-body decline, on `_eff_move`'s precedent for a condition the typed cells cannot spell. The PC
lane's `03_PC_exits_withdrawal_recovery.md` Part C makes `tend` a graded draw; this decline sits in
front of it and does not touch it.

## Gate (execution artifacts)

`engine/season/tests/test_hunger.py` and `test_demand_delivery.py` are the files covering the edits.

1. Two cohorts of weight 2 on one rung holding grain 4, salt 2: each takes grain 2, salt 1; each falls
   30; `shortfalls` names the rung with the gap (grain 4, salt 2). Control: the rung holding grain 8,
   salt 4: both fed, no report.
2. Three cohorts on a rung holding 4 grain: takes sum to 4; over 200 season keys the cohort receiving
   the odd unit varies (the falsifier for "drawn": one cohort receiving it 200 of 200).
3. K7 replayed through `subsist`: the exact-multiple granary reports once, in the season the town first
   goes unfed, at the granary rung; never again while the dearth lasts. Control: a ladder with no key
   for the kind reports nothing (the ruled silence).
4. `pes_noacts.py famine`-shaped world with the highland rungs stocked for one exact season: every death
   Event's `causes[0]` is a `body.changed` whose `causes[0]` is a `stores.changed` at a highland rung.
5. `pes_play.py 0 2 fail` re-run: cohort `tend` on a short cohort refused; highland bodies fall season
   on season. Control: the fed arm unchanged.
6. `build_realm(0)`, three seasons, barrier-only: content hash equal to base at edits 1 and 2.

## Falsifier

After these edits, the fail arm of `pes_play.py` should show at least one shortfall claim held by a
person in a realm whose highland rungs were once stocked. If it still shows none, the break is in
WITNESS's routing or the chooser's attention and this proposal did not reach it.

## NERS (`CLAUDE.md` §0.06; E last)

- **N.** Cut R1 and a dearth at a shared store has one arbitrary victim and no shared hardship; cut R2
  and a store authored in whole seasons starves its towns unseen; cut R3 and no record can say why a
  town died; cut R4 and no town can decline. Each holds bottom-up (the cohort), top-down (the holder who
  must learn of it), vertically (the first lane's seat-rung granary is a shared store by construction)
  and laterally (the chronicle and ending instruments read causes).
- **R.** A short granary now produces a region of thin towns, not one dead one: more seats under
  pressure at once, and a draw at the margin. The no-player half gains its first settlement hook: a
  reported crossing.
- **S.** One draw record still feeds MATTER's writes and `demanded`/`delivered`. `tend` and hunger stop
  being two ladders for one body in opposite directions each season.
- **E.** Two input fields, one loop rewritten in place, one branch, one parameter, one decline; no new
  Event kind, verb, store or table. The vocabulary is unchanged.

## Cost

Small: one module function, three host sites, one effect. No content.
