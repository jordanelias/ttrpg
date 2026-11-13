# CHAR — a scar is a wound, not a tally: who can be scarred, by how much of a violation, how often, and how one heals

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §4) — amended by `U5a_CHAR_owed_amendments.md` §6 (F-PES-CHAR-11: a fully scarred person's shift is not skipped). The scar write's Event is `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 2 (`scar.taken`, logged, fanned out to nobody).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (CONFORMS, one open fact), §2 row A-24/A-47, §7, §7b-T; `unified/U1_GLOSSARY.md` *scar*; `unified/U3_CONFLICT_LEDGER.md` C3-Y8; `unified/U3_DEPENDENCY_ORDER.md` node B10, §6.2). Changed: "the thresholds, the crisis and the dormant readers are untouched" is reworded to the rulings — a crossing of 3 is the **trigger of a drawn, seen crisis of faith** (A-24; `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`) and a threshold opens, never decides (A-47); the open fact is settled at the tree (`write_matrix.yaml:263-270`: `(Person, scar)` is `steps: [RES, ENC]`, `class: ACTS`, a field write the gate admits in either direction; its `emits` names `scar.taken` only, so vindication's decrement declares `scar.healed` on the same row, `[ASSUMPTION]`); in the body the count is a **scar** (glossary; the title stays); the scratch probe becomes a named test; lands-it and tier.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-2 item; `20_NARRATIVE_A_stands_for.md` edit 5): the `primary` arm's affiliation threshold is `person_q.stands_for` (one owner), `scar_affiliation_floor` is not added; the writer of `stands_for` (B10 before B38) is marked `[ASSUMPTION]` in the `person_q.py` edit.

**Lands in batch:** B10, co-landing with `02_CHAR_scar_cap_and_regard_unit.md` (one fixture `scar_season_cap`, C-U5a-06; C3-Y8). **Depends on:** `16_PESSIMIST_CORE_the_record_holds_what_changed.md` (B09, `scar.taken`).

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, F-CHAR-17, C-4).
Ratifies nothing. Reference under `CLAUDE.md` §0.05. It **amends item 1** of
`02_CHAR_scar_cap_and_regard_unit.md` (the first lane's season cap), which it keeps as one arm; it
does not touch that proposal's items 2 and 3.

## What this changes in `engine/season/` at runtime

Four fixtures, each shipped at a control that reproduces today's hashes, on the one scar writer
(`loop/resolve.py::_scar_witnesses`) and the one predicate (`queries/person_q.py::_held`,
`_pursuits_violated_by`). Flipping any of them is a declared hash mover. The thresholds (1, 2, 3) and the
dormant readers are untouched; a crossing of 3 is the trigger of a drawn, seen crisis of faith (A-24;
`16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`), never its decision (A-47: a threshold opens,
it does not decide).

## The problem, with evidence

`ED-IN-0261` rules a three-rung ladder. The writer gives one count per observer per violated element
per act. The first lane measured the result (median per-person maximum 41 in two seasons) and
proposed a cap of one count per (person, element) per season.

**That cap bounds the rate and not the stock.** `probe_scar_stock.py` (a scratch script, not in the
repository; restated by the named test below) (`build_realm`, shipped chooser, four seasons, `PYTHONHASHSEED=0`), counting the seasons in which each (person, element)
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
| 1 | `scar_hold` | `any` (today: held above zero) | `primary` | only a person's **primary** elements can be scarred: the fewest top-weighted pursuits whose weights sum to at least `scar_primary_mass` (0.6, PP-684's lower bound for the primary band), and affiliations the person stands for (`person_q.stands_for`, intensity 3 or more of 5) |
| 2 | `scar_lean_floor` | `0.0` (today: the sign test) | `0.2` | an act violates a pursuit only when `pursuit_lean(verb, e) < −floor`; swept 0, 0.2, 0.4 |
| 3 | `scar_season_cap` | `None` | `person` | at most one count per person per season, on the element most violated (largest weight × \|lean\|, ties by name). The first lane's arm, `element` (one per person per element), is the middle point of this fixture's sweep |
| 4 | `scar_vindication` | `off` | `on` | a witnessed act whose lean on a primary element is above `+scar_lean_floor` removes one count from that element, never below 0, at most once per person per season |

H-128 (is the actor scarred by his own act?) is answered at the same site: at the live arms the
shipped `False` (he is an observer like any other) is the reading that makes a man who breaks his own
primary the first to be scarred by it. The arm stays swept.

## Exact edits, by file and owner

- **`queries/person_q.py`** (owner of the predicate). `_held(weights, violated, floor_rule)` takes the
  rule: `any` as today; `primary` computes the primary set once per person per call from
  `p.pursuits` (sort by weight descending, name ascending; take until the sum reaches
  `scar_primary_mass`) and, for affiliations, from `person_q.stands_for(p, "stands")` (`20_NARRATIVE_A_stands_for.md`
  edit 1: held above the scale's midpoint, which on the `0-5` scale of `references/descriptor_registry.yaml`
  is intensity 3 or more). This file writes no second threshold and adds no `scar_affiliation_floor`
  (`20_NARRATIVE_A` edit 5: one owner). This file lands in B10 and `stands_for` in B38, so whichever lands first
  writes the function. `[ASSUMPTION: this file, landing first, writes `stands_for` with the `"stands"` arm
  only, and `20_NARRATIVE_A` edit 1 then adds the `any` arm, the `held_readings` roster and the fixture —
  basis: `20_NARRATIVE_A`'s cost-class paragraph leaves the writer to whichever lands first; B10 precedes
  B38; reversible by moving the function body into either file.]`
  `_pursuits_violated_by(verb, floor=0.0)` compares against `−floor`; a twin
  `_pursuits_upheld_by(verb, floor)` returns the elements with lean above `+floor`. `broken_by`
  and a new `upheld_by` pass the fixtures through. No `World`.
- **`loop/resolve.py::_scar_witnesses`** (owner of the write). Reads the four fixtures. Under a cap,
  it keeps a per-season set of persons already counted (`person`) or (person, element) pairs
  (`element`) on the driver, cleared at the season's first barrier, and for `person` picks the one
  element by the rule above. Under vindication it writes `−1` on upheld primaries through the same
  gated write, before the violations of the same act. The `(Person, scar)` row (`write_matrix.yaml:263-270`,
  `steps: [RES, ENC]`, `class: ACTS`) admits the write in either direction; its `emits` gains `scar.healed`
  for the decrement so the log's derived roster accepts it (`04` §B.13 invariant 7) `[ASSUMPTION: the kind's
  name]`.
- **`data/fixtures.py`**: the four fixtures and `scar_primary_mass` (no `scar_affiliation_floor`: the affiliation threshold is `stands_for`'s), each
  with its hole-register row under H-128's precedent (declare, default, sweep).
- **`harness/`**: no new instrument. The gate is the named test below (the scratch probe restated).

## The gate (an execution artifact)

Seeds 0, 1, 2; eight seasons; shipped chooser. (a) Every control arm reproduces today's one- and
two-season hashes. (b) At the four live arms together, the share of cast persons with some element
at 3 or more after eight seasons lies strictly between 0 and 1 at every seed, and persons who reach
it differ in their primaries from persons who do not. (c) At least one count falls by vindication
in the run. Named tests (new, `engine/season/tests/test_scar_stock.py`): `test_every_control_arm_reproduces_todays_hashes`
(a); `test_at_the_live_arms_the_share_at_three_lies_strictly_between_0_and_1` (b, seeds 0–2, eight seasons);
`test_vindication_lowers_a_count_at_least_once` (c).

## The falsifier

At the live arms, after eight seasons, every person or no person is at 3 or more: the ladder still
does not discriminate, and the floors are wrong or the trigger needs the design's stricter gate (a
contest lost on that belief). Or (c) reads zero falls at three seeds: the outflow is unreachable and
is deleted, not kept dormant.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** Top-down (ED-IN-0261's ladder needs separable rungs), bottom-up (the writer already has the
  projection and the lean), lateral (the dormant weight shift and refusal axis can be armed only on a
  count that separates people). Without it, arming either moves everyone at once.
- **R.** A person's scars become his: the zealot is scarred by what the merchant shrugs at. The
  no-player half: a creed erodes in one house and hardens in another without anyone watching.
  Completeness: the stock is bounded at both ends.
- **S.** One predicate, one writer; the same `pursuit_lean` the consequence mover uses, so "violates"
  and "moves toward" are one ladder.
- **E.** Four fixtures on two functions. The cost is one sort per person per scarring act. A reader
  can say it in a line: only what you chiefly live for can scar you, and seeing it honoured heals.

## Cost class

Small build (two functions, one writer, fixtures), then four flips, each after its own reading.

**Lands it and tier.** The B10 batch with the scar cap, an IN `valoria-author` session on `sonnet` (`high`),
closed by B10's `methodology-close` once. **Hash movers.** None at the controls; each flip declared.
