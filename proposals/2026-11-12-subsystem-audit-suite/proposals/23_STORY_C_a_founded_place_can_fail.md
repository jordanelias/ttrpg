# STORY-C — a founded place can fail: a hearth or community left empty is put to a draw each season, and may be abandoned

## Status: PROPOSED (one write-matrix cell is touched; named under "Where it meets Layer 1")

Source: `audits/23_STORY_ENABLEMENT.md` §2 row S-38, §4.2 G3; `16_PESSIMIST_SE.md` §3.5 (*"a founder's
town outgrows him, or dies with him: no settlement can be founded; no founded thing can end"*),
F-PES-SE-06, and its Jordan call J-3, whose option A sketches this mechanism in one sentence and builds
nothing. Composes on, and does not restate: `14_VERBS_MATERIAL_C_works.md` (`found` and `build` formed
on their own works and drawn), `14_VERBS_MATERIAL_A_mending.md` (`restore`, `work` drawn),
`07_SE_population_regrowth_B.md`, `14_VERBS_MILITARY_A_movement.md` (lodged, not housed),
`23_STORY_A_what_a_roll_leaves.md` (the stake step). Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

At ship, nothing (`lapse_draw` is `off`). With it on: each season at MATTER, a rung of a kind `found`
can make, under which nobody resides and no Site stands above condition zero, is put to one graded draw;
it stands, stands and loses part of what was staked on it, or is abandoned (the rung ends, what was left
of its stake returns to its parent). A declared hash mover only in worlds that hold such a rung.

## The problem, with evidence

- `loop/effects_founding.py::_eff_found` mints a Rung of the works' `plan` kind with **no Sites**
  (*"a founded hearth has no dwelling until one is BUILT"*), held by its founder, holding the staked
  `works_cost`; `_eff_build` mints a Site at condition 0. In the realm `found` executes 0 of 25 and
  `build` 0 of 15 (`16_PESSIMIST_GAME.md` §3.3); hand-built, a founding *"ends in an empty lot"*
  (`16_PESSIMIST_SE.md` §3.4).
- The only closer of a Rung is `_eff_raze` (`del w.rungs[rid]`, every live Tenure naming it closed),
  licensed by an occupation and limited to `raze_target_kinds`, a settlement. So a founded hearth has
  one outcome: it stands for ever, built or not, peopled or not. `H-166` limit 3 says it in the
  register's words: *"`w.rungs` now grows and nothing shrinks it"*.
- MAT-C makes the founding a draw. What becomes of the place afterwards is carried by no proposal
  (`audits/23_STORY_ENABLEMENT.md` §3, G3).

## The resolution, decided

A rule by **kind**, not by origin: no rule may ask whether a place "was founded" (that would special-case
an outcome's history), and the kinds `found` makes are a closed roster. An empty place of such a kind
does not fall at a count of seasons (a schedule, which the standing rule forbids); it is put to a draw
whose odds worsen the longer it stands empty and improve with what was staked on it and with its holder
being near. Ladder step 3 (PES-SE J-3 option A's own sentence: *"put to a draw each season, its odds
worsening the longer it stands empty; on a failure it ends and its stake returns to its parent"*) and
step 4 (`raze`'s cascade as the one way a Rung ends). It stays inside SE-9(a): no node of the settlement
registry can be closed by it. A town-scale founding and abandonment remain PES-SE J-3, Jordan's.

## Exact edits, by owner

**1. `engine/season/rosters.yaml` — `lapse_kinds`.**

```yaml
lapse_kinds:
  source: "STORY-C: the Rung kinds an empty place of which may be abandoned. The kinds `found` makes
           under strict ascent (a hearth under a settlement, a community under a territory); never a
           `raze_target_kinds` member, never a registry settlement or anything above one."
  values: ["hearth", "community"]
```

The loader refuses a member that is also in `raze_target_kinds`.

**2. `engine/season/loop/effects_founding.py` — one owner for a Rung ending.** The `perform` body of
`_eff_raze` (delete the Rung; set `until` on every live Tenure naming it) becomes
`_end_rung(w, rid) -> Callable`, called by `_eff_raze` (no behaviour change; hash EQUAL) and by edit 3.
The Layer 1 gap `_eff_raze`'s docstring records (Sites and Records whose `rung` field names the ended
Rung; `H-228`) is unchanged and not widened: a rung this pass may end has, by its own condition, no
resident and no standing Site.

**3. `engine/season/loop/matter.py` — `_lapse(w, token)`, after the wear pass**, skipped at
`lapse_draw == "off"`. For each Rung `r` of a `lapse_kinds` kind with no live `reside` or `contain` edge
of a Person naming it and no Site under it above condition 0:

- **Pool:** `lapse_pool`, plus one for each whole `works_cost` price of matter the rung still holds
  (what was staked on it and not spent), plus one where the holder of a live `hold` on `r` stands in
  `r`'s parent rung.
- **Obstacle:** `lapse_ob`, plus one for each `lapse_patience` seasons since `r` last had a resident or
  a Site above zero (or since it was minted, if never).
- One draw through the route DET-A gives the uncontested verbs, keyed on `(r.id, w.tick)`.

| band | writes | emits |
|---|---|---|
| Overwhelming, Success | nothing | — |
| Partial | one `stake_stores` step of the rung's matter moves to its parent rung, two-sided (`_shift`, the founding's own mover) | `stores.changed` |
| Failure | all remaining matter moves to the parent, two-sided; `_end_rung(w, r.id)` | `stores.changed`, `rung.abandoned` |

`rung.abandoned` is a new kind on the matrix row `(Rung, exists)`, beside `rung.razed`. Its `causes`
are the rung's own last `stores.changed` or minting Event, never `ROOT` (PES-SE-A edit 3's rule for a
MATTER death).

**4. `engine/season/data/fixtures.py`** — `lapse_draw = "off"` (control, SHIPPED) `/ "on"`;
`lapse_pool` (proposed 2), `lapse_ob` (proposed 1), `lapse_patience` (proposed 2 seasons), each with a
hole-register row graded `assumption` and a sweep `[ASSUMPTION; medium; Jordan to correct]`. At the
proposed values a fresh founding holding its stake and with its founder near rolls four dice against an
obstacle of 1, and the same lot four seasons empty, stripped and unheld rolls two against 3.

**5. Nothing for growth, and nothing for the founder.** A place with a resident or a standing Site is
never drawn for. It gets one when someone `build`s and `work`s there (MAT-C, MAT-A), when a migrant
lodges (MIL-A) or when a resident cohort regrows (`07_SE_population_regrowth_B.md`). No rule names the
founder: if he alone kept the place it weakens when he dies or leaves (the pool loses his term), and if
others came it is no longer drawn for at all.

## Where it meets Layer 1

- **`write_matrix.yaml`, the cell `(Rung, exists)`.** Its closer today is RESOLVE through `raze`. This
  proposal adds MATTER as a writer of that cell for `lapse_kinds` only. Layer 1's account of MATTER is
  the three motions (matter wears, memory decays, bodies fall, `09_WR` reads it so); an empty place
  going back to the land is matter wearing at the scale of a rung, and the write is material, not
  social (`state/world.py:64-107`: no social quantity moves at MATTER). That reading is this lane's
  `[ASSUMPTION; named for the Layer 1 reader, not decided by editing Layer 1]`.
- **If Layer 1 refuses a MATTER writer on that cell**, the same draw moves to RESOLVE as the effect of
  the holder's `release` of his `hold` on such a rung (he is asked about an empty holding each season,
  MAT-C's precedent for an unmade works), and an unheld empty place then stands until someone takes it
  up. That form needs no matrix edit and loses the ending nobody chose. The first form is proposed.

## The gate (execution artifact)

The valley fixture with one works whose plan is a `hearth` (`23_STORY_E` adds the row); 20 seeds,
8 seasons; arms `lapse_draw` off and on, with MAT-C and MAT-A on in both.

1. **Control.** `off`: no `rung.abandoned` at any seed; edit 2 alone leaves every pinned hash equal.
2. **Both outcomes.** `on`: among the seeds at which the founding executed, the rung stands at the end
   at some and is abandoned at others; among those where it stands, it is peopled or built at some.
3. **Never a schedule.** The season of abandonment differs between seeds; no rung with a resident or a
   Site above zero is ever drawn for (a count printed by the pass, expected 0).
4. **Conservation.** Realm matter by kind is equal before and after every abandonment.
5. **Census.** S-38 passes audit §6.1's clauses C1 to C6. Under C6's pinned rolls no rung is abandoned.

Story bar test (`engine/season/tests/test_storybar.py`): a planted log (`found` executed; no residence;
`stores.changed` out of the rung; `rung.abandoned` citing it) reads one S-38 with variant *abandoned*;
a plant with a `residence.changed` into the rung and no `rung.abandoned` reads variant *peopled*; a
plant whose `rung.abandoned` cites `ROOT` reads no S-38.

## The falsifier

- A settlement, or any rung not of a `lapse_kinds` kind, ended by this pass.
- A peopled or built place drawn for.
- Every empty founding abandoned in the same season across seeds: the draw is not keyed per rung and
  tick, or the obstacle is being read as a deadline.
- Matter lost at an abandonment.

## NERS reading

- **N.** Cut it and a founding has no second outcome, so MAT-C's draw decides only whether a lot
  appears, and `w.rungs` only grows. Holds bottom-up (an empty lot means something), top-down (the map
  can lose what play added), diagonally (the founder's nearness is a person's fact in a place's odds).
  Laterally it is narrowed: a place can already end by `raze`; this adds the ending nobody chose.
- **R.** With no player, a place somebody began is left and goes back to the land, or is taken up and
  grows. A player who founds must people it or keep near it. Complete at the extremes: a realm with no
  such rung runs the pass over nothing; a rung with nothing staked and nobody near is likeliest to go
  and can still stand a season.
- **S.** One owner for a Rung ending; the task-draw route already proposed; the founding's own mover
  for the stake; the stake step STORY-A defines. Calculations consistent with `found`'s own (the same
  price unit in the pool).
- **E, last.** One roster of two, one helper extracted, one pass, four fixtures, one kind, against the
  only second outcome a founding has. High.

## Cost class

Small build, one session; the matrix cell is the design-first part. Dark at control.

## Dependency edges

Needs first: MAT-C (a founding executes); DET-A (the task-draw route); `23_STORY_A` (`stake_stores`).
Feeds: `23_STORY_E`; PES-SE J-3 option A (this is its *"lapse"*, designed). Batch E-11 of the audit.
