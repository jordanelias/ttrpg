# WR — the Calamity strains, breaks by a draw, and stops where it is mended

Reconciled: 2026-11-12, U5d closure — folded **A-40** and **A-54**. A-40 rules the wearing-down a real condition of places with one Site per territory: edit 1's "pulled only by a broken Site of its own or a bordering territory" reads on that one Site per territory. The break draw of edit 2 is on the four-band ladder (as written). Edits 1–2 land before any non-zero `lattice_coupling` (`U5d_WR_owed_edits.md` §2 (a)).

## Status: PROPOSED

Source: `audits/16_PESSIMIST_WR.md` §2.2, F-PES-WR-02, F-PES-WR-11. Read at `d161a61`. Reference only
(`CLAUDE.md` §0.05). Lane WR (owner: `loop/matter.py::_lattice_strain` and the wear loop).

It amends one scheduled step of a sibling proposal and depends on two others:

- **amends** `09_WR_world_motion.md` edit 1's second commit (`lattice_coupling` 0 → 250 with the wound
  at Askeheim in place). The wound row and the build switch stand. The flip does not, until edits 1 and
  2 below land: run as scheduled it is the exponential of §"The problem".
- **depends on** `09_WR_B_threadwork_session_and_practitioner.md` (the Mend working, drawn, costing the
  practitioner by degree) for edit 3, and on `16_PESSIMIST_GAME_the_world_draws.md` (`wear_draw`) for the
  ordinary wear's own draw, which this proposal does not repeat.

## What it changes in `engine/season/` at runtime

Nothing while `lattice_coupling` ships at 0 (every edit is behind that weight; the control is byte
identical). With a non-zero weight: (1) a Site is pulled only by a **broken** Site (condition 0) of its
own or a bordering territory, not by any weaker one; (2) a Site strained into its lowest band beside a
broken one takes **one draw a season**, and the degree decides whether it breaks, holds, or knits;
(3) `restore` declines at a broken Site, which only a thread working raises; (4) a band crossing a
person witnesses at the place he stands raises a question that carries the Site.

## The problem, with evidence

`runs/PES_WR/p3_s0_k14_c250.txt` (seed 0, the cohort-only realm, nobody acting, weight 250, PROXY: one
dwelling in `terr_T1` set to 0 before season 0) and `p2_s0_k3_calamity.txt` (the same plant in the full
realm, the shipped chooser, three seasons):

- **It builds from anything.** With no source (`p1_s0_k60_lattice.txt`) the rule makes every wear-0 Site
  follow the wearing ones down 40 behind; with one cottage at 0 the realm's yield goes 4,810 → 3,510 →
  2,173 → 719 at seasons 0, 3, 7 and 13. The rule pulls toward the *weakest neighbour*, so the world's
  defining catastrophe is begun by whichever Site is worst.
- **It never breaks.** Fourteen seasons: 112 `condition.band_crossed`, no death, no body fall, no Event
  that marks a moment, `endings_reached == []`. The decay is exact arithmetic, the same at every seed.
- **Nobody answers it.** Played: after seasons 0, 1 and 2 the ring means are 725, 542, 405 (ring 0) and
  748, 559, 417 (ring 1), **equal to the unplayed arm to the unit**; 24 band crossings were emitted;
  `restore` was attempted 0 times and `work` 0 times; the executed-verb distance from the realm without
  a Calamity is 24, against 316 between two draws of the same realm. `verb_table.yaml`'s `restore` row
  states the cause: "no question the realm delivers carries a Site among its referents".
- **Its bound is free and certain.** `effects_economy.py::_eff_restore` stages `_rise`, an ungraded,
  costless rise: were it ever attempted, one person standing at the wound would end the Calamity in a
  season, every time.

## The resolution, decided

The setting's sentence is *a calamity builds and breaks, and the Thread can be mended at a cost*. Each
clause gets one owner and one draw.

**Builds:** strain flows from what is broken, so it has a source and a direction and stops when the
source is mended. **Breaks:** by a draw whose odds the surrounding fabric sets, emitting an Event with a
before and an after. **Mended at a cost:** by the working the threadwork module resolves, never by a
free certain act. Ladder step 5 for the rule change (the docstring's own stated bound, "holding a ring
stops the front", is unreachable under the weakest-neighbour rule because no ring can be held against
arithmetic), step 4 for the draw (`body_hazard`'s keyed draw in the same barrier) and for the decline
(`_eff_migrate` declining a destination that changes nothing).

## The edits

### Edit 1 · only the broken pull (`engine/season/loop/matter.py::_lattice_strain`)

Old (`:190-195`):

```python
near = [n for u in (t, *sorted(borders.get(t, ()))) for n in by_terr.get(u, ()) if n != sid]
if not near:
    continue
gap = max(0, w.sites[sid].condition) - max(0, min(w.sites[n].condition for n in near))
```

New:

```python
broken = [n for u in (t, *sorted(borders.get(t, ()))) for n in by_terr.get(u, ())
          if n != sid and w.sites[n].condition <= 0]
if not broken:
    continue
gap = max(0, w.sites[sid].condition)          # the pull is toward a hole in the fabric
```

No new field: a Site at 0 *is* the broken Site (the wound row of `09_WR_world_motion.md` edit 1 is
built at 0). Ordinary uneven wear no longer propagates; a realm with nothing broken couples nothing.

### Edit 2 · the break is drawn (`loop/matter.py`, the wear loop; `data/fixtures.py`; `write_matrix.yaml`)

After the wear write, for each Site that (a) has a broken neighbour by edit 1's reading and (b) stands
below the lowest floor of its kind (`band_floors`; for a kind whose cell is `{}`, below
`rupture_band`), one keyed draw (`draw_factory(w.world_seed, lambda: w.tick)(site.id, "rupture")`),
resolved on the one ladder (`seam/ladder.py`, `degree_from_net`):

- *Pool (the strain upon it):* the count of broken Sites in its own and bordering territories, capped at
  `rupture_pool_cap`.
- *Obstacle (what holds it):* `rupture_base` + the number of its own territory's Sites standing in
  their top band (sound fabric beside it resists).

| the strain's degree | the Site | write on `(Site, condition)` at MATTER |
|---|---|---|
| Overwhelming, Success | **breaks**: condition → 0 | emits `site.ruptured`, cause the wear Event; witnessed like every MATTER emission |
| Partial | holds | none |
| Failure | **knits**: recovers one season's pull | emits `condition.worn` with a positive delta (the fabric held) |

Fixtures, each `[ASSUMPTION; medium; Jordan to correct]` with its hole row: `rupture_band=100`,
`rupture_base=2`, `rupture_pool_cap=6`. `write_matrix.yaml`'s `(Site, condition)` MAT row gains the kind
`site.ruptured`. L5 is kept: this is matter's licensed clock writing its own cell; no social row is
written and nobody is made to act.

### Edit 3 · a broken Site is mended only by a working (`loop/effects_economy.py::_eff_restore`)

One decline, beside the existing `site is None` decline:

```python
if site.condition <= 0 and w.fixtures.get("lattice_coupling"):
    return NO_CHANGE        # -> restore.refused: a hole in the fabric is not repaired with mortar
```

The Mend of `09_WR_B_threadwork_session_and_practitioner.md` (drawn, its cost to the practitioner
modulated by degree) is then the one act that raises a broken Site, which is the setting's premise in
one rule. Until that module lands the weight stays 0, so this decline is unreached and nothing is
orphaned.

### Edit 4 · a crossing he stands beside raises a question about the place (`queries/world_q.py::questions_for`)

Owner: CORE's file; listed here with its gate because the Calamity is inert without it. A new claim in a
person's ledger whose Event is a `condition.band_crossed` or `site.ruptured` anchored on a Site at the
rung he stands on is stamped as a `Site`-classed referent (`own_referents_of_class`, REM-21's term), so
`restore` (and, at a broken Site, the Mend) forms for him. The `restore` row's own note measures the
absence: "attempted 0/0/0 — no question the realm delivers carries a Site among its referents".

## The gate that shows it worked

`engine/season/tests/test_in35_lattice_coupling.py`, on `build_realm` with the wound planted and the
weight at 250, nobody acting, fourteen seasons, seeds 0 and 1:

- the realm's yield at season 13 **differs between the two seeds** and is above 719 in both (the front
  advances only by drawn breaks);
- at least one `site.ruptured` is emitted in at least one seed, and its season differs between seeds;
- with the source raised above 0 at season 5 (PROXY) and no other Site broken, the ring means at season
  13 equal their season-5 values less ordinary wear (the front stops where it is mended);
- at weight 0 the season is the base hash (the control).

Played, three seasons, the wound planted: `restore` or the Mend is attempted at least once by a person
standing at a crossed Site, in at least one of two seeds.

## The falsifier

`runs/PES_WR/p3_calamity.py 0 14 250` and `… 1 14 250` printing the same ring table (4,810 → 719) at both
seeds after the change. Before it, they do (the rule takes no draw).

## NERS reading

- **N.** Cut the break and the Calamity is a slope with no event on it; cut the broken-only rule and it
  has no source and no stop. From the other directions: bottom-up (the keyed draw, the cell and the
  crossing Event exist), lateral (`body_hazard` is the same shape for persons), diagonal (a broken Site
  halves a harbour's yield, which is the dearth the SE and FA lanes' verbs wait for), vertical (a
  rupture in a territory is an occasion at the realm scale that only a practitioner at the personal
  scale can answer).
- **R.** The no-player half is the point: places break, unevenly and at different times, with nobody
  watching, and each break is an Event a narrator can date. Completeness: a realm with nothing broken
  couples nothing; a realm wholly broken draws nothing; the weight at 0 is today.
- **S.** One ladder for the break; `restore` and the Mend are separated by eligibility, not by a second
  arithmetic; the pull keeps the parallel-map read of the barrier's opening conditions.
- **E** (last): one changed comprehension, one draw block, one decline, one stamped referent, three
  fixtures. A player can say it in a sentence: *what is broken pulls on what is near it, the strained
  may give way, and only a working closes the hole*.

## Cost class

Edits 1 and 3: edit. Edit 2: small build. Edit 4: small build at CORE's owner. The weight's flip is a
declared hash mover and its own commit, after the threadwork module.
