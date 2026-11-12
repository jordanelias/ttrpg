# CORE — the reason for an act, kept where the act is kept

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row (VIOLATES as written at `deliberate.py:303`), §7, §7b-1, §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-C16, C3-N27; `unified/U3_DEPENDENCY_ORDER.md` node B09, §6.2). Layer 1 rewrite (`04` §A.2: `loop/deliberate` owns nothing and holds no token; §C.1: `scenes = deliberate(frozen)` is a map; PART D rows 41, 41a): Edit 2 no longer writes the Scene store from DELIBERATE — **RESOLVE**, which holds the ACTS token and the act store, stores each Scene as it appends that Scene's acts; DELIBERATE keeps returning its map and stores nothing. The departure of a stored `Scene.decided` field (if `U5a_CHAR_owed_amendments.md` §5 lands it) from `04` §B.9 is named (C3-C16). The scratch probe becomes named tests; the hash literal carries the B01 caveat; lands-it and tier added.

**Lands in batch:** B09. **Depends on:** `02_CHAR_reason_trail_and_small_edits.md` Part A (B09, the `watch` hook the chronicle line reads).

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_B.md` F-CORE-12, §6 (d). Read at `785bc62`.

## What it changes in `engine/season/` at runtime

No act, Event, write or draw changes. One record that exists during a season and is lost with the
driver is kept in `World`: the Scene an act was released in, with the question it answered.
`content_hash` is EQUAL if the Scene store is left out of the hash (edit 4, the decided default); it is
a declared mover if it is folded in.

## The problem, with evidence

`04` §B.9 types `Scene := (id, person, occasion : Question, place, interactions)` and makes it *what the
budget counts*. The code builds it and keeps it in `SeasonDriver.scenes`, a dict on the driver
(`loop/driver.py:322`), written at release (`loop/deliberate.py:303`), read once
(`loop/resolve.py:171`, for `causes[]`), cumulative by design (`driver.py:317-321`: the fold's record
must cross seasons) and in no `World` collection. This proposal keeps the lifetime and moves the home.
`resolved` and `act_of`, the two cumulative attributes beside it, are not moved here: each is derivable
from the act store and the log (`state/attribution.py`), and `scenes` is the one that is not.

`probe_reason.py` (headless world, seed 0, three seasons): the driver held 8, 18 and 28 Scenes after
each season; every one of 58 stored acts resolves its `scene` id only through that dict; 4 act-caused
Events cite the act alone because `_occasion_of` returns `[]` for an act on a standing occasion
(`resolve.py:181-184`); `Act` carries no field for its question. The chooser's deciding term (pursuit,
stance, or the draw) is computed by `decision/choose.py` and returned to nobody: `decision_spread`
recovers it only by re-running the ranking with the same seed.

So a world that is saved, ported or handed to a second driver cannot say why any past act was taken, and
a driver that runs a long campaign holds one Scene per act it ever released.

## The resolution

The act store is `causes[]`'s resolver-side home for Acts (`04` §B.9, *"`state/acts` is append-only,
resolver-side, and no person-side Query reaches it"*). The Scene is the Act's container and belongs
beside it. Nothing person-side may read it, for the same reason.

## Edits

### 1 · owner `engine/season/state/acts.py` — the Scene store

```python
class ActStore:
    def add_scene(self, sc: Scene) -> None      # append-only; refuses a repeated id, as `add` does for an Act
    def scene_of(self, act_id: str) -> Optional[Scene]
    def scenes(self) -> tuple                    # in release order
```

### 2 · owner `engine/season/loop/resolve.py` (and `loop/deliberate.py:303`, `loop/resolve.py:171`, `loop/driver.py:322`)

`loop/deliberate.py` keeps returning its `Scene` map exactly as `04` §C.1 draws it and stores nothing (its
line `:303`, `self.scenes[sc.id] = sc`, is deleted with `SeasonDriver.scenes`). `loop/resolve.py::resolve`,
which holds the ACTS token and the act store, calls `w.acts.add_scene(sc)` for each Scene of its `scenes`
argument immediately before it appends that Scene's acts (`w.acts.append`, `resolve.py:1033`). `_occasion_of`
reads `w.acts.scene_of(a.id)`; `epistemic._term_why` (the one other reader of `Scene.occasion`) reads the
same accessor. A write from DELIBERATE would be a store write by a step that holds no token, on the frozen
world, and order-sensitive on a repeated id (`04` PART D rows 41, 41a).

### 3 · the deciding term — owned by the CHAR lane's proposal, not this one

`02_CHAR_reason_trail_and_small_edits.md` Part A gives the chooser an observer hook (`watch`) through
which a reader receives the ranked order, the score terms and the sampled order at the moment of
decision, with no carrier and no field. That is the owner of *which term decided*, and this proposal
adds no field for it. The two fit: the hook supplies the deciding term while the process runs, and the
Scene store (edits 1–2) is what the hook's reader keys its record on after the season ends. What stays
unrecorded under both is the deciding term of a past season in a reloaded world; if that is wanted it
is one optional attribute on the stored Scene, stamped by the watcher's caller, and is not built here. If
`U5a_CHAR_owed_amendments.md` §5's `Scene.decided` lands, it is a field beyond `04` §B.9's `Scene` record
(`(id, person, occasion, place, interactions)`; the code's names differ, `state/carriers.py:602-632`): the
departure is named at `Scene`'s docstring with its one reader (`harness/chronicle.py`) under B4's third
disposition, and `04` is not edited (C3-C16).

The standing-occasion case needs no new field: the stored Scene's `occasion.source` and
`occasion.about` are the record, and `causes[]` stays `[act]` (an occasion that is no Event is not a
cause; `_occasion_of`'s rule is kept).

### 4 · owner `engine/season/state/world.py::content_hash` — not folded

The Scene store is left out of the digest `[ASSUMPTION; medium; Jordan to correct; revert: fold it]`.
Ground: a Scene is a function of the seed and the world that produced it, a Question is *"never
hashed"* by its own docstring (`carriers.py:538-539`), and folding it would re-pin every golden for a
record that changes no outcome. The port carries it as data beside the log.

### 5 · owner `engine/season/harness/chronicle.py` — the reader

`--chains` prints, per act, `for: <occasion.source> <occasion.about>` (and the deciding term where the
CHAR proposal's watcher supplied one). This is the first reader, so the store is not a dead carrier
(`04` ID-13).

## Gate (an execution artifact)

`probe_reason.py` (a scratch script, not in the repository) is restated as new tests in
`engine/season/tests/test_scene_store.py`: `test_the_driver_holds_no_scenes`; `test_every_stored_act_answers_scene_of`
(58 of 58 on the headless world, seed 0, three seasons, at the audit's reading); `test_a_fresh_driver_answers_a_season_0_acts_question`
(a second `SeasonDriver(w)` prints the same `for:` line); `test_hash_equal_with_the_scene_store_unfolded`
(the content hash at seed 0 after three seasons equals the base tree's: `383206baa7e7807e28cd609d2bb5f080` is
`main`'s reading at the working tree; re-read on the batch's base, C3-N27). The existing
`engine/season/tests/test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` is the falsifier of the
Layer 1 rewrite: a store write inside DELIBERATE turns it red.

## Falsifier

Construct a fresh driver on the three-season world and ask for a season-0 act's question. `None` falsifies
the edit. A changed content hash falsifies edit 4's claim.

## NERS reading

- **N.** From the narrative's side (top-down) a reason is what turns a causal chain into a story; from
  the act's side (bottom-up) the record already exists and is thrown away. Lateral: `epistemic._term_why`
  already needs it within the season. Removing it costs every "because" a chronicle could print.
- **R.** The no-player half: a world that generates drama unobserved must be able to say afterwards why
  each thing was done. Completeness: a long campaign no longer grows a driver-side dict.
- **S.** No calculation changes. It pauses correctly: nothing is read during DELIBERATE.
- **E (last).** One accessor replaces one dict.

## Cost class

Edit (four files). Hash EQUAL.

**Lands it and tier.** The B09 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B09's
`methodology-close` once. **Hash movers.** None (edit 4: not folded; control: the base tree's hash).
