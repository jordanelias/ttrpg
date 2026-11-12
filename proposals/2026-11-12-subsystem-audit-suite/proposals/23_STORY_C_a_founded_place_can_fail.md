# STORY-C — a founded place can fail: an untended, unpeopled founding decays by the world's own draws and is closed

## Status: PROPOSED

Source: `audits/23_STORY_ENABLEMENT.md` §2 row S-38, §4.2 G3; `16_PESSIMIST_SE.md` §3.5 (*"a founder's
town outgrows him, or dies with him: no settlement can be founded; no founded thing can end"*), F-PES-SE-06
and its Jordan call J-3 (option A's second outcome for a hearth). Composes on, and does not restate:
`14_VERBS_MATERIAL_C_works.md` (`found` and `build` formed on their own works, drawn, raised by `work`),
`14_VERBS_MATERIAL_A_mending.md` (`restore`, `work` drawn), `16_PESSIMIST_GAME_the_world_draws.md` (wear
drawn per Site), `07_SE_population_regrowth_B.md`, `14_VERBS_MILITARY_A_movement.md` (lodged, not
housed). Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

At ship, nothing (`founded_lapse` is `off`). With it on: a rung that `found` made, every Site of which
stands at condition zero and under which nobody resides, is closed at MATTER. A declared hash mover only
in worlds where a founding has executed and then been left.

## The problem, with evidence

- `found` executes 0 of 25 in the realm and makes hearths and communities only (SE-9(a): the settlement
  registry gains no node); hand-built, a founding *"ends in an empty lot"* (`16_PESSIMIST_SE.md` §3.4).
- Nothing ends a founded rung but `raze`, which needs an occupation (`16_PESSIMIST_SE.md` §3.1 S6). So
  the one story a founding could tell, *it throve or it failed*, has one outcome: it stands for ever, at
  whatever condition, peopled or not.
- MAT-C makes the founding itself a draw. What happens after is not carried by any proposal
  (`audits/23_STORY_ENABLEMENT.md` §3, G3).

## The resolution, decided

No new draw and no new clock. A founded place is a Site on the wear the world already applies, and
PES-GAME's proposal makes that wear a draw per Site; MAT-A makes each mending a draw. Left untended, the
Site falls; tended, it holds. What this proposal adds is the bookkeeping at the end: a rung with nothing
standing and nobody living in it stops being a place. That is not a threshold deciding an outcome (the
standing rule): everything that could go either way for the people in the fiction, the wear and the
mending, was drawn before it, exactly as `_die` at body zero follows the drawn falls of a body (ladder
step 4: `loop/matter.py::_die`; `raze`'s tail). It keeps SE-9(a): only what `found` makes can be closed
this way, and no settlement of the registry is touched. A town-scale founding and its abandonment remain
PES-SE J-3, Jordan's.

## Exact edits, by owner

**1. `engine/season/loop/effects_founding.py` — expose `raze`'s tail.** The part of `_eff_raze` that
closes every edge under a rung and leaves its residents placeless becomes
`_close_rung(w, rung_id, causes) -> list[Change]`, called by `_eff_raze` (no behaviour change; hash
EQUAL) and by edit 2. One owner for "a place ends".

**2. `engine/season/loop/matter.py` — `_lapse_founded(w, token)`, after the wear pass.** For each rung
that a works Record names as founded (the `founded` stage `_eff_found` writes on its works; no new field
on the rung): if every Site under it stands at condition 0 and no Person's `reside` or `contain` edge
names it, call `_close_rung` with `causes` the last `condition.worn` Event of its last Site, and emit
`place.abandoned`, a kind declared on the matrix row `raze` already writes. Skipped at
`founded_lapse == "off"`.

**3. `engine/season/data/fixtures.py`** — `founded_lapse = "off"` (control, SHIPPED) `/ "on"`, with a
hole-register row graded `assumption`. **The loader refuses `"on"` unless the wear draw of
`16_PESSIMIST_GAME_the_world_draws.md` is on**: under today's uniform wear (10 a season for every Site)
the season a neglected founding reaches zero is arithmetic from its starting condition, and the lapse
would be a schedule. The refusal is the licensed form (a loader's refusal per data family, §0.05).

**4. Nothing for growth.** The other outcome needs no rule of its own: a founded hearth with a dwelling
Site above its lowest band is a place a migrant may be housed (MIL-A's Partial is *lodged, not housed*;
its Success is housed), and a cohort that resides there regrows by `07_SE_population_regrowth_B.md`.
Listed for those two lanes: neither names a founded hearth and neither excludes one.

**5. Nothing for the founder.** No rule mentions him. If he alone tended the place, it decays when he
dies or leaves; if others came, it does not. That is the story, and it is not written anywhere.

## The gate (execution artifact)

The valley fixture, which holds one authored works; 20 seeds, 8 seasons; arms `founded_lapse` off and on
(with MAT-C, MAT-A and the wear draw on in both).

1. **Control.** `off`: no `place.abandoned` at any seed; edit 1 alone leaves every hash equal.
2. **Both outcomes.** `on`: among the seeds at which the founding executed, the founded rung stands at
   the end at some and is closed at others; among those where it stands, it is peopled at some.
3. **The cause is on the record.** Every `place.abandoned` has a `condition.worn` among its causes, and
   that Site's history shows no executed `restore` or `work` in the two seasons before.
4. **Census.** S-38 passes audit §6.1's clauses C1 to C6. Under C6's pinned rolls (every mending a
   Success) no founding is abandoned at a seed where anyone tended it.

Story bar test: a planted log (`found` executed; four `condition.worn` on its Site to zero; no residence
under it; `place.abandoned`) reads one S-38 with variant *abandoned*; with a `residence.changed` into
the rung planted before the last wear, no `place.abandoned` may be emitted and the variant reads
*peopled*.

## The falsifier

- A registry settlement closed by this pass: the works stage is not what selects.
- A peopled founding closed; a founding at condition above zero closed.
- `founded_lapse` on with uniform wear accepted by the loader.
- Every founding abandoned in the same season across seeds: the wear draw is not reaching these Sites.

## NERS reading

- **N.** Cut it and a founding has no second outcome, so `found`'s draw decides only whether a lot
  appears. Holds bottom-up (a Site that reaches zero means something) and top-down (the map can lose
  what play added). Laterally it is narrowed: a place can already end by `raze`, and this adds the
  ending nobody chose.
- **R.** With no player, a place somebody began is left and goes, or is taken up and grows. A player
  who founds must keep it. Complete: a founding with no Site is closed at once only if unpeopled; a
  realm with no founding runs the pass over nothing.
- **S.** One owner for a place ending; the wear and mending draws already proposed; one existing matrix
  row. No second ladder: condition is the quantity, as it is for every Site.
- **E, last.** One extracted helper, one short pass, one fixture and one kind, against the only second
  outcome a founding has. High.

## Cost class

Edit to small build; one session. Dark at control.

## Dependency edges

Needs first: MAT-C (a founding executes); `16_PESSIMIST_GAME_the_world_draws.md` (the wear draw, by
edit 3's refusal); MAT-A (mending as a draw). Feeds: `23_STORY_E` (the seam village's new hearth);
PES-SE J-3 option A (this is its *"lapse"*, without the per-season odds that file sketches: the odds are
the wear's and the mending's). Batch E-11 of the audit.
