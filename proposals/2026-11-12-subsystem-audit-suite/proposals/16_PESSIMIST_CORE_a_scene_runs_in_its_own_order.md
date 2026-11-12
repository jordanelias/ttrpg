# 16 · PESSIMIST · CORE — a scene runs in its own order, and its second step may depend on its first

## Status: PROPOSED — **held back: needs Jordan** (it re-keys the fold order #353 §27 ratifies; the two options are below and in `audits/16_PESSIMIST_CORE.md` §6)

Carries F-PES-CORE-06 of `audits/16_PESSIMIST_CORE.md` (§1.1). Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

Under Option B: RESOLVE folds each scene's interactions contiguously and in the order the chooser
composed them, and an interaction may declare that it is attempted only if the one before it reached a
named band. Scenes are ordered among themselves by the present key (stratum, then the content hash), read
off each scene's first interaction. Under Option A: nothing.

## The problem (evidence; `build_realm(0)`, two seasons, hash `bacd687f…`)

- `loop/resolve.py:51-58` sorts every act of a round by `(stratum_of(a), H(seed, tick, actor,
  "order:verb:act id"))` over one global array. The scene an act belongs to is not a key.
- 525 scenes with two or three folded interactions: **120 (23%) fold in the scene's own order**, which is
  what chance gives. A scene composed `create_record, challenge, utter` resolves in whatever order the
  hash deals.
- All of a scene's interactions are chosen before any resolves (`decision/choose.py::pack_scenes` returns
  the whole `Scene`), so no interaction can be conditional on the outcome of an earlier one.
- **R-09's statement** (`requirements.yaml:1567`): *"chains of events within a scene are probabilistic,
  not deterministic."* There is no chain within a scene: the unit has no internal order and no internal
  dependence, so the requirement's subject does not exist in the engine. The row's `partial` is measured
  on whether a roll reaches a single act.
- The strata, which are what the global order protects, decided nothing at seed 0: with every act in one
  stratum, 0 of 821 acts changed outcome in a season; with the hash order reversed inside each stratum,
  1 of 175 round-0 acts did (`ordp.py 0 1`).

## The two options (a Jordan call: they are different games)

**Option A — a scene is a budget unit, and stays one.** Keep the global order. A scene is "one to three
things a person does this round, simultaneously with everyone else's". Then R-09's wording is re-pointed
at chains *across* scenes (round to round), the word *scene* is defined at both sites (CLAUDE.md §4) as a
budget unit with no internal order, and the play surface must not show a player his three picks as a
sequence. Cost: an edit to two definitions. What is lost: the tabletop scene (*I question him; if he
breaks, I accuse him; if not, I leave*), which is the unit the detective and trial precedents in
`AUDIT_BRIEF.md` are made of.

**Option B — a scene is a short sequence (this proposal's edits).** The chooser's order is the order of
resolution, and a later step can hang on an earlier one's band. Then R-09 has a subject: a three-step
scene is a chain of up to three draws, each conditioning the next. What is lost: the property that all
acts of a round fold over one array keyed only by stratum and hash (#353 §27; the roster `strata` in
`architecture/meta/08_DATA_AND_KEYS.md:16`), and with it the guarantee that a `movement` act anywhere
precedes a `social` act anywhere. Measured, that guarantee decided no outcome in a season.

**This lane's recommendation: B**, on three grounds: R-09 is a ruled requirement and has no subject
under A; the standing rule (*a thing that could go either way goes by a draw*) wants more chained draws,
not fewer; and the ordering it gives up is, by execution, not doing anything. It is Jordan's because it
edits what Layer 1 ratifies.

## Exact edits, by owner (Option B)

1. **`engine/season/loop/resolve.py::_canonical_order`** — order *scenes*, then flatten:
   key each scene by `(stratum_of(first interaction), H(seed, tick, actor, "order:scene:<scene id>"))`;
   an act with no scene (`a.scene is None`, the pre-`W17` bare Act) is its own one-act scene, so every
   existing caller and probe is unchanged. `encounter.py` imports the same function and inherits it.
2. **`engine/season/state/carriers.py::Act`** — one optional field, `after: Optional[tuple] = None`:
   the bands of the scene's previous interaction at which this one is attempted (`None`: always, today's
   behaviour). Read by the fold only.
3. **`engine/season/loop/resolve.py::resolve`** — before folding an act whose `after` is set, read the
   degree the previous interaction of its scene just produced (the driver has `self.act_of` and the
   Events in hand); outside the named bands, emit the row's refusal kind for a new clause
   `sequence` (`refusals_by_clause`), so the skipped step is in the log and costs its slot.
4. **`engine/season/decision/choose.py::pack_scenes`** — when packing a contested interaction followed
   by one on the same subject, set `after` from the row's own `writes_by_degree` (the bands in which the
   first wrote anything). No verb is named; the rule reads the row.
5. **`architecture/meta/`** (Layer 1; only on Jordan's ruling) — the §27 order restated as *strata and
   hash over scenes*.

## Gate (an execution artifact, §0.2)

| reading (`build_realm(0)`, two seasons) | today | passes when |
|---|---|---|
| multi-interaction scenes folded in their own order | 23% | 100% |
| acts with `after` set that were skipped because the prior step missed its band | — | greater than 0, and each has a logged refusal with clause `sequence` |
| control: `after` never set and one-act scenes only (`interactions_per_scene = 1`) | — | content hash equal to today's at that fixture |
| the `ordp.py` strata-cut arm re-run | 0 flips | reported, whatever it is |

## Falsifier

At `interactions_per_scene = 1` the hash moves: the re-keying changed more than the order within scenes.

## NERS reading (E last)

- **N.** Cut within-scene order (today's state) and what dies is the chain R-09 names. From the top
  (the requirement), from the bottom (the chooser already composes an order that is then discarded), and
  laterally (the fight module resolves exchanges in order inside one act; a scene is the same idea one
  level up): three directions.
- **R.** A scene whose second step is conditional is the smallest unit in which a person's plan can go
  wrong in the middle, with nobody watching.
- **S.** *Zooms out and in*: a scene becomes the same shape as a bout (ordered exchanges, each a draw).
- **E.** One sort key and one optional field, against a unit whose name promises an order it does not
  have.

## Cost class

Design-first (a ruling), then a small build. Golden re-record at any fixture with more than one
interaction per scene: say so plainly.
