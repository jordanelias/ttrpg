# WR · Draws, not thresholds: the world's motions, its endings and a strand's conclusion

Reconciled: 2026-11-12, U5d closure — folded **A-54**, **A-47** and **A-57 / A-58**. A-54 confirms this file's one shape (eligibility by state, then a keyed draw on the shared ladder) for the world's motion; `16_PESSIMIST_GAME_the_world_draws.md`'s table form is withdrawn in its favour. A-47 agrees with edit 3 (an ending's selector is eligibility; the crossing decides nothing). The owed line for FA / MB ("`seize` on an occupation licence … must resolve by a draw against the place's resistance") is narrowed: land another faction holds passes on an aggressor's won march, and that win is the field's drawn end state (A-3), so no second draw is taken there; the line stands for unheld land and for an `Unopposed` entry.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-20) — `_seize_rung` takes no draw today (opened); the FA/MB item's premise is confirmed.

Written under the brief's **Standing rule (Jordan, 2026-11-12, emphatic): "We do not do deterministic"**:
every consequential outcome resolves by a draw with a graded, recoverable result; state sets the odds, the
draw sets the outcome; seeded replay, arithmetic bookkeeping (a clock's tick, conservation, an id) and
eligibility checks are not forbidden. Carries finding F-WR-24 of `audits/09_WR_audit_addendum_B.md` (§2.5).

**Supersedes,** in the first lane's files (which this lane does not edit): `09_WR_world_motion.md` edit 1's
*mechanism of the crossing* (the wound and its data row stand; the strain it sends is drawn, edit 1 below)
and edit 3's *reaching rule* (the settled-territory selector stands; reaching it is drawn, edit 3 below);
`09_WR_strand_conclusion.md` edits 1 and 2's *meaning of "terminal"* (both stand as eligibility; a terminal
move concludes only on its drawn degree, edit 4 below). `09_WR_story_instruments_that_can_fail.md` and
`09_WR_provided_arcs.md` resolve no outcome (readings and adjudication only) and are compliant as written,
except that the story-instrument `weather` arm should use the mean-one arm of
`09_WR_B_weather_with_memory_and_the_year.md` edit 2. This lane's own `_B` proposals were corrected in
place (§2.5 of the audit lists where).

## What it changes in `engine/season/` at runtime

Edits 1 and 2 are **declared hash movers** behind a control: with the new fixtures at their control values
the realm is byte-identical (wear exactly the kind's rate; the body step exactly `body_step`). Edits 3 and 4
change readings: edit 3 changes what `endings_reached` reports (no consumer halts on it), edit 4 what
`flows_in` marks terminal, which reaches `flow_stakes` through `concluded_known` (the first lane's declared
mover, re-measured).

## The problem (F-WR-24)

Read at HEAD, the world's consequential outcomes are fixed functions of state:

| outcome in the fiction | how it resolves today | where |
|---|---|---|
| a Site wears; a use closes when its condition crosses a floor | wear is exactly `fixtures.wear(kind)` + the lattice pull, every season; the crossing is a comparison | `loop/matter.py:852-870`; `rosters.yaml:1905-1912` |
| the Calamity's strain reaches a neighbour | the lattice coupling is arithmetic over neighbours' conditions | `matter.py::_lattice_strain`; first lane's world-motion edit 1 |
| a hungry cohort weakens | a short draw lowers the body by exactly `body_step` (10) | H-125; `modules/settlements/subsist` (SE's module) |
| a petition is forgotten | a matter lapses at exactly `docket_lapse` seasons | H-356; `world_q.lapsing_items` (SC's subject) |
| the realm is won or lost | an ending is reached when a count crosses (all territories held; all Sites fallen) | `world_q.py:2675-2683`; first lane's world-motion edit 3; this lane's R-26 (now corrected) |
| a strand concludes | its latest move's *kind* is terminal | `world_q.py::flows_in`, `:5212-5213`; first lane's strand-conclusion edits 1, 2 |

Each is something that "could go either way for the people in the fiction". None draws. The weather factor
(`season_factor_of`), illness (`illness_rate`) and every contested verb that rolls already comply; they are
the precedent.

## The resolution, decided

One shape everywhere, the engine's own: **eligibility by state, then a keyed draw on the shared ladder
(`dice_engine.degree_from_net`, the one owner), whose pool and obstacle are set by state, and whose four
bands grade the result.** Keyed draws (`ids.draw_factory`) keep seeded replay; a draw inside a Query is
keyed by `(seed, tick, subject, purpose)` and advances no ordinal (`season_factor_of`'s precedent).

## The edits

### Edit 1 · wear is drawn (`loop/matter.py`, `data/fixtures.py`; WR's)

Per Site per season, one keyed draw `draw_factory(world_seed, tick)(site.id, "wear")`; obstacle from the
kind's wear row plus the lattice pull (strain makes bad seasons likelier, not certain), pool a fixture row.
Bands: Overwhelming 0, Success half the rate, Partial the rate, Failure twice the rate. A wear-0 kind draws
nothing (eligibility: nothing wears it). The crossing stays a comparison on the drawn condition: the
outcome was the draw. Fixture `wear_draw: False` (control) is today's exact rate; `True` is the arm.
Recoverable: `restore` raises condition and the next season draws again. `[ASSUMPTION; medium; Jordan to
correct]` for the band multipliers. This is also the Calamity's form: the wound's strain enters only as
obstacle on its neighbours' wear draws, so a front advances unevenly and can stall.

### Edit 2 · the hungry body is drawn (listed for SE, `modules/settlements/subsist`; the shape stated)

On a short draw, a keyed draw per cohort with obstacle from the shortfall's depth (how far the larder fell
short of want) and pool from the cohort's own body: Overwhelming 0, Success half `body_step`, Partial
`body_step`, Failure twice. Control: exactly `body_step`. H-125's own question ("is starvation a season or a
campaign") then has a spread for an answer, not a single number.

### Edit 3 · endings are reached by draws (`queries/world_q.py::_ending_edges`; WR's, beside the first lane's edit 3)

Every `endings` row: its selector is **eligibility** (the holds or Sites stand as the row says), and then a
keyed draw `draw_factory(world_seed, tick)("realm", f"ending:{name}")`. For a holds row: pool from the
seasons the condition has stood (computed from the antecedent Events' ticks, no stored counter) and the
share of holds opened by an act; obstacle a fixture row plus the holds the condition reads that no act opened (inherited at build,
so conquest counts for more than inheritance). The
draw is the condition's: Success or Overwhelming reaches the ending; Partial reports `near`; Failure does
not reach it this season. For a `site_band` row, as
`09_WR_B_weather_with_memory_and_the_year.md` edit 4. A reported ending still "emits no Event, halts
nothing and writes nothing"; what changes is that standing at the condition makes an ending likely, not
certain, and keeps the season-by-season possibility that the realm holds on (recoverable).

### Edit 4 · a strand concludes on a drawn degree (`queries/world_q.py::flows_in`; WR's, amending the first lane's edits 1, 2)

The first lane's two rules stand as **eligibility**: an opening move is never terminal; a content-opening
kind does not conclude at the person reading. A move eligible as terminal concludes its strand only when
its Event's drawn `degree` (`Event.degree`, set by the resolving roll) is Success or Overwhelming; at
Partial the strand stays open with the move recorded (a contested settlement, which a later act may
reopen); at Failure the move is not terminal. A terminal-eligible kind whose Event carries **no** degree
(its verb resolves without a roll) concludes nothing, and is listed for the verb's owner: the verb must
roll (the standing rule), not be read as a conclusion. `Move.terminal` becomes
`bool(term(e, a)) and not opening and e.degree in CONCLUDING_DEGREES`, with
`CONCLUDING_DEGREES = ("Success", "Overwhelming")` declared once beside `CONCLUDING_KINDS`.

### Listed for other lanes (not edited here)

- **SC:** `docket_lapse` (H-356) as a draw per season past a matter's age (odds rising with age, falling
  with petitions renewed), not a fixed age.
- **PC / CHAR:** death by body (`Person.exists` written when the body passes its last floor) through a
  drawn crossing; `F-PC-04`'s certain kill is the same class.
- **FA / MB:** `seize` on an occupation licence (the first lane's world-motion edit 2) must resolve by a
  draw against the place's resistance; `_seize_rung` does not roll today (grounded, 25 G-20: `loop/effects_information.py:1038-1075` takes no draw and reads no degree, and `seize` is not among the 11 contested rows or the 3 graded ones, so it takes the uncontested fold).
- **B10-15:** CP-T07-08's breach as a draw (`09_WR_B_threadwork_session_and_practitioner.md`).
- **B10-18:** CP-T10-02's exposure at a leg's end as a draw.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.strife 3 0 1 2 --strands
python -m pytest engine/season/tests/test_in35_lattice_coupling.py engine/season/tests/test_in27_endings.py \
       engine/season/tests/test_strife_flows.py -q                     # covering files, at the close
```

Passes when: (1) every control reproduces `build_realm(0)` and the one- and two-season pins; (2) under
`wear_draw: True`, two harbours of equal condition and kind diverge within four seasons at some seed, and
the realm's mean wear over eight seasons at three seeds lies within the control's rate ± its own spread;
(3) a planted world meeting a holds row's condition reaches it at some seeds and not others over 200 seeds,
and more often the longer the condition has stood; (4) a planted strand ending on `matter.determined` at
Partial reads open, and at Success reads concluded; (5) `closes … threshold=` in
`09_WR_B_readings_of_closure_and_tension.md` falls by the wear crossings once edit 1 is on.

## The falsifier

Any outcome above that is identical across 200 seeds at a fixed eligible state (the draw collapsed into a
threshold); any outcome reached while ineligible (the eligibility leaked); a control arm whose hash moves.

## NERS reading

- **N.** The standing rule is Jordan's; what N adds is that a world whose ruin, victory and conclusions
  arrive on schedule is a countdown (F-WR-13's shape), and a drawn world is not. Holds top-down (realm
  endings), bottom-up (one Site's season), laterally (SC's lapse, PC's death, FA's seizure share the one
  shape) and diagonally (a strained neighbour's bad draw making a famine).
- **R.** A good position sometimes loses: a well-kept harbour can fail a season, a dominant faction can
  fail to close the realm this year. Completeness: every extreme still rolls.
- **S.** One ladder, one mint, one shape (eligibility, then odds, then four bands) for every motion;
  calculations consistent in methodology with every contested verb.
- **E, last.** Four draw sites and one declared tuple against the six deterministic outcomes of the table.
  High.

## Cost class

Edit 1: small build (one draw, one fixture). Edit 2: small build, SE's. Edit 3: small build. Edit 4: edit.
