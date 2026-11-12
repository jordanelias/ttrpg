# CHAR — a scar is a wound, not a tally: who can be scarred, by how much of a violation, how often, and how one heals

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, F-CHAR-17, C-4).
Ratifies nothing. Reference under `CLAUDE.md` §0.05. It **amends item 1** of
`02_CHAR_scar_cap_and_regard_unit.md` (the first lane's season cap), which it keeps as one arm; it
does not touch that proposal's items 2 and 3.

## What this changes in `engine/season/` at runtime

Four fixtures, each shipped at a control that reproduces today's hashes, on the one scar writer
(`loop/resolve.py::_scar_witnesses`) and the one predicate (`queries/person_q.py::_held`,
`_pursuits_violated_by`). Flipping any of them is a declared hash mover. Nothing else moves: the
thresholds (1, 2, 3), the crisis and the dormant readers are untouched.

## The problem, with evidence

`ED-IN-0261` rules a three-rung ladder. The writer gives one count per observer per violated element
per act. The first lane measured the result (median per-person maximum 41 in two seasons) and
proposed a cap of one count per (person, element) per season.

**That cap bounds the rate and not the stock.** `probe_scar_stock.py` (`build_realm`, shipped
chooser, four seasons, `PYTHONHASHSEED=0`), counting the seasons in which each (person, element)
count rose, which is what the cap would leave:

| after season | seed 0: persons with some element at 3 or more | median elements at 3 or more | seed 1 |
|---|---|---|---|
| 1 | 0 of 83 | 0 | 0 of 83 |
| 2 | 0 of 83 | 0 | 0 of 83 |
| 3 | **83 of 83** | 9 | **82 of 82**, median 11 |
| 4 | 83 of 83 | 11 | 82 of 82, median 12 |

(Hashes after seasons 1 and 2 equal the first audit's, so the runs are the same runs. First-order
reading: decisions held fixed.) Under the cap everyone reaches the terminal rung together in season
three. The first lane's gate (*"median per-person maximum after four seasons ≤ 4"*) passes at exactly
this reading.

**Two causes, both in the predicate.**

1. *Everyone holds everything.* `_held` admits an element *"held above zero"*, and `data/cast.py`
   refuses a cast row with fewer than all fifteen pursuits. Read on `build_realm(0)`: the median cast
   person's largest weight is 0.5, his third 0.08, his eighth 0.035, his smallest 0.02, and all 37
   cohorts hold pursuits. A pursuit a person holds at 0.02 scars him as readily as the one he holds
   at 0.5.
2. *Any size of violation counts.* `_pursuits_violated_by` is a sign test: `pursuit_lean(verb, e) <
   0`. H-128's own cite calls it *"a CANDIDATE READING under review, unswept"*.

And there is no outflow: a count only rises. The surviving 2026-08-08 audit recorded the same of the
retired engine (*"there is no Scar decay anywhere … converges every long-lived NPC to permanent
crisis"*) and proposed the mirror, vindication; it was held, never ruled.

**What the design meant** (ARCHIVED-NOT-CANON, for intent only). A scar is rare by construction: a
Belief revised only by a decisive contest won in the hearer's own style on that Belief, or a
witnessed Thread operation capped at *"1 Scar per season … per NPC"*; scars on background
convictions (weight 0.2 to 0.4) are *"muted"*, and only a primary's scars change behaviour
(`conviction_track_v1` §2, PP-718).

## The resolution, decided

Ladder: step 3 for the shape (the design's primaries, its per-person cap), step 5 for the outflow.
Each value is `[ASSUMPTION; medium; Jordan to correct]` and reverts alone.

| # | fixture | control (ships) | proposed live | what it does |
|---|---|---|---|---|
| 1 | `scar_hold` | `any` (today: held above zero) | `primary` | only a person's **primary** elements can be scarred: the fewest top-weighted pursuits whose weights sum to at least `scar_primary_mass` (0.6, PP-684's lower bound for the primary band), and affiliations held at intensity 3 or more of 5 |
| 2 | `scar_lean_floor` | `0.0` (today: the sign test) | `0.2` | an act violates a pursuit only when `pursuit_lean(verb, e) < −floor`; swept 0, 0.2, 0.4 |
| 3 | `scar_season_cap` | `None` | `person` | at most one count per person per season, on the element most violated (largest weight × \|lean\|, ties by name). The first lane's arm, `element` (one per person per element), is the middle point of this fixture's sweep |
| 4 | `scar_vindication` | `off` | `on` | a witnessed act whose lean on a primary element is above `+scar_lean_floor` removes one count from that element, never below 0, at most once per person per season |

H-128 (is the actor scarred by his own act?) is answered at the same site: at the live arms the
shipped `False` (he is an observer like any other) is the reading that makes a man who breaks his own
primary the first to be wounded by it. The arm stays swept.

## Exact edits, by file and owner

- **`queries/person_q.py`** (owner of the predicate). `_held(weights, violated, floor_rule)` takes the
  rule: `any` as today; `primary` computes the primary set once per person per call from
  `p.pursuits` (sort by weight descending, name ascending; take until the sum reaches
  `scar_primary_mass`) and from `p.conviction` (intensity at or above `scar_affiliation_floor`).
  `_pursuits_violated_by(verb, floor=0.0)` compares against `−floor`; a twin
  `_pursuits_upheld_by(verb, floor)` returns the elements with lean above `+floor`. `broken_by`
  and a new `upheld_by` pass the fixtures through. No `World`.
- **`loop/resolve.py::_scar_witnesses`** (owner of the write). Reads the four fixtures. Under a cap,
  it keeps a per-season set of persons already counted (`person`) or (person, element) pairs
  (`element`) on the driver, cleared at the season's first barrier, and for `person` picks the one
  element by the rule above. Under vindication it writes `−1` on upheld primaries through the same
  gated write, before the violations of the same act.
- **`data/fixtures.py`**: the four fixtures and `scar_primary_mass`, `scar_affiliation_floor`, each
  with its hole-register row under H-128's precedent (declare, default, sweep).
- **`harness/`**: no new instrument. The gate is read by the existing storybar or a scratch probe of
  the shape used here.

## The gate (an execution artifact)

Seeds 0, 1, 2; eight seasons; shipped chooser. (a) Every control arm reproduces today's one- and
two-season hashes. (b) At the four live arms together, the share of cast persons with some element
at 3 or more after eight seasons lies strictly between 0 and 1 at every seed, and persons who reach
it differ in their primaries from persons who do not. (c) At least one count falls by vindication
in the run.

## The falsifier

At the live arms, after eight seasons, every person or no person is at 3 or more: the ladder still
does not discriminate, and the floors are wrong or the trigger needs the design's stricter gate (a
contest lost on that belief). Or (c) reads zero falls at three seeds: the outflow is unreachable and
is deleted, not kept dormant.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** Top-down (ED-IN-0261's ladder needs separable rungs), bottom-up (the writer already has the
  projection and the lean), lateral (the dormant weight shift and refusal axis can be armed only on a
  count that separates people). Without it, arming either moves everyone at once.
- **R.** A person's wounds become his: the zealot is wounded by what the merchant shrugs at. The
  no-player half: a creed erodes in one house and hardens in another without anyone watching.
  Completeness: the stock is bounded at both ends.
- **S.** One predicate, one writer; the same `pursuit_lean` the consequence mover uses, so "violates"
  and "moves toward" are one ladder.
- **E.** Four fixtures on two functions. The cost is one sort per person per scarring act. A reader
  can say it in a line: only what you chiefly live for can wound you, and seeing it honoured heals.

## Cost class

Small build (two functions, one writer, fixtures), then four flips, each after its own reading.
