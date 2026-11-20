# GAME — an act on a standing occasion names the Event that opened it

Reconciled: 2026-11-12, U5d closure — folded **A-47** and **A-33**. A mandatory scene opened by a threshold carries as its cause the Event that armed the last stage, by this file's rule. An act formed on a vacancy cites the seat's news; it does not cite the death unless the actor holds a claim of it (A-33). No step changes.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS: an Event id in `causes[]` is
resolver-side and reaches no person), §7/§7b (COMPLETE but for the tier: tier and the loader constant's name added); U3
B09, §6.2 (`x2_death.py`, `x2b_death_detail.py` are scratch; the gate's test plants the death itself); U1 glossary
*occasion* (the Event that opened a standing occasion is its **opening Event**). No body text changed beyond those lines.

## Status: PROPOSED

Lands in batch: **B09** (IN), after `16_PESSIMIST_CORE_the_record_holds_what_changed.md` in that batch's order. Depends on:
nothing unlanded (`World.last_emission_of`, `_occasion_ids`, the `strife_kinds` loader check exist);
`01_CORE_reason_trail_in_the_act_store.md` (B09) is independent and compatible (below).

Source: `audits/16_PESSIMIST_GAME.md` F-PES-GAME-03; premise 2.1 link 4. Read at `4995824`. Reference
only (`CLAUDE.md` §0.05); not ratified by being written. Lane IN (cross-cutting; the owner is
`engine/season/loop/resolve.py`).

## What it changes in `engine/season/` at runtime

The `causes[]` of every Event folded from an act that was formed on a **classed referent** (a vacancy,
a seat told of, a writ held, a matter awaiting, a larder in purview, a wounded person, a detainee, a
flow stake) gains one id: the Event that opened that standing occasion, where the log holds one. Today
such an act's Events cite the act alone. No act, write, draw or eligibility changes. A declared hash
mover (an Event's `causes` is hashed); the control arm is a fixture that returns today's `[]`.

## The problem, with evidence

`loop/resolve.py::_occasion_ids` returns `[]` when the act's subject is a classed referent and not a
plain one (the Batch B-I close, F1: *"an act on a classed referent answers the standing occasion, not the
question it rode on … such an act gets `[ROOT]`"*). The reasoning is right about the *question*: the
question the vacancy was stamped onto is unrelated. It is wrong about the *occasion*: the vacancy has an
opening Event, and that Event is the reason for the act.

Measured (`runs/PES_GAME/x2b_death_detail.py 0 1 4 p_npc_020`, seed 0): the King dies at MATTER
(`person.died`, then `tenure.closed` naming `off_king` and `off_duke_valorsmark`); the season after, the
Prince's `succeed` executes and its `succession.claimed` Event has `causes == [his own act]`. The 43
`confer` attempts on the vacant seats over three seasons carry the same. A reader of the log (the
chronicle, the arc reader, the story bar, the strand linker, a narrator in the port) cannot say *the
Prince took the throne because the King died*; `x2_death.py` finds 19 acts descending from the death by
`causes[]` and none of them is the succession.

The class is wide. `queries/world_q.py::questions_for` stamps classed referents from fifteen sources
(`vacancies`, `seats_named`, `writs_held`, `records_held_for_holding_rows`, `places_named`,
`matters_awaiting`, `larders_in_purview`, `holdings_to_found`, `own_referents_of_class`, `works_sites`,
`propositions_heard`, `stage_referents`, `wounded_with`, `flow_stakes`, `detainees_held`). These are the
occasions of `succeed`, `confer`, `comply`, `evade / defy`, `determine`, `requisition`, `tend`,
`interrogate`, `found`, `build`: the acts that close a story. In the WR lane's six-season run at seed 0
(`runs/WR/probe_s0_k6.txt`, storybar's own split) 1,361 of 5,483 acts have no antecedent at all.

## The resolution (decided)

An act on a classed referent cites **the last Event written about that referent, of a kind its class
declares**, and nothing when the log holds none (a seat vacant since the build keeps `[]`, which is
true: nothing in the log opened it).

Ladder step 4 (precedent): `World.last_emission_of(kind, subject, written=True)` is the tree's chaining
primitive (IN-56, H-129), used by MATTER for exactly this purpose (*"a licensed clock's next tick names
its previous one"*). The same primitive, asked of a standing occasion.

## Edits

### 1 · owner `engine/season/rosters.yaml` — one roster, data

```yaml
# the Event kinds that OPEN a standing occasion of each referent class, most specific first
standing_occasion_opened_by:
  Office:    [tenure.closed, office.established]
  Record:    [dispensation.issued, petition.filed, record.created]
  Person:    [body.changed]            # `wounded_with`
  Detainee:  [person.captured, arrest.made]
  Rung:      [stores.changed, rung.seized]
  Site:      [condition.band_crossed]
  Proposition: [proposition.uttered]
```

`[ASSUMPTION; medium; Jordan to correct]` the kind lists are this proposal's reading of each source's
docstring; the loader (`data/rosters.py`) exposes it as `STANDING_OCCASION_OPENED_BY` and refuses a kind
that is not an `emits` of some verb row or a MATTER/CALENDAR kind, by the check that already validates
`strife_kinds`. Verify at landing: `rg -n "STANDING_OCCASION_OPENED_BY" engine` returns the loader constant and
`_occasion_ids`' read.

### 2 · owner `engine/season/loop/resolve.py::_occasion_ids` — the one branch

```python
    if (subj and subj not in getattr(occ, "referents", ())
            and any(r == subj for r, _ in getattr(occ, "classes", ()))):
        if not w.fixtures.get("standing_occasion_cause"):          # control arm: today's `[]`
            return []
        cls = next(c for r, c in occ.classes if r == subj)
        for kind in STANDING_OCCASION_OPENED_BY.get(cls, ()):
            eid = w.last_emission_of(kind, subj, written=True)
            if eid is not None and eid != a.id:
                return [eid]
        return []
```

Resolver-side (RESOLVE may read the log's index; no person-side Query is touched, so `04` §A.2's
no-`World`-under-`decision/` holds). One id at most, so `causes[]` does not fan.

### 3 · owner `engine/season/data/fixtures.py` — `standing_occasion_cause`, graded `assumption`, shipped `True`

The control (`False`) reproduces every base hash.

## Gate (an execution artifact, §0.2)

`engine/season/tests/test_in53_vacancy_need.py` (the file that covers `_occasion_ids` on a vacancy;
`test_in50_refusals_carry_the_occasion.py` covers the refusal half and gains the mirror assertion)
gains one test: build the governance spine, end the holder of a seat that
`rosters.yaml: successions` names (the bodies hazard at 1 for that person, as `x2_death.py` does), run
two seasons; assert a `succession.claimed` Event exists **and** that its `causes` contains the id of the
`tenure.closed` Event naming that seat; assert the loop asserted (`checked >= 1`). Control arm
(`standing_occasion_cause: False`): the same run, `causes == [act id]`, and the world hash equals the
base hash.

Falsifier: the test fails if the branch returns `[]` (today's code), and the control fails if the
fixture is ignored.

## NERS

- **N.** Cut it and the chronicle cannot read any closing act's reason; every instrument that walks
  `causes[]` (storybar, chronicle, arc, strife's links, the port's narrator) under-reads the game's
  consequences by construction. From the other directions: bottom-up (the index already exists),
  lateral (MATTER already chains this way), top-down (R-01's meaning is this edge).
- **R.** The no-player half: a death now has a readable consequence without anyone watching.
- **S.** One methodology with MATTER's chaining; no second causal channel.
- **E** (last, as a ratio): one roster, one branch, one fixture, for the reason of every closing act.

Cost class: edit. Depends on nothing. `01_CORE_reason_trail_in_the_act_store.md` (the Scene store) is
compatible and independent: it keeps the *question*; this keeps the *opening Event*. Tier: `sonnet`, effort
`high`. Hash movers declared: every Event folded from an act on a classed referent (`causes` is hashed); the
control `standing_occasion_cause: False` reproduces every base hash. Lands it: B09, one commit (roster, branch,
fixture, test); command `python -m pytest engine/season/tests/test_in53_vacancy_need.py engine/season/tests/test_in50_refusals_carry_the_occasion.py -q`
(both exist).
