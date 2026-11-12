# NARRATIVE-E — the year and the reason: a calendar that exists, an occasion that keeps its ground, and a crisis of faith that is drawn and seen

## Status: PROPOSED (edit 3 is HELD for Jordan: it overwrites `ED-IN-0261`'s ruled "rolls nothing")

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-06, F-NARR-08, §5 (the reason trail's three losses), §7.5.
Three small edits at three owners, grouped because each supplies one line a narrator needs (when; on
what occasion; what broke). Reference only (`CLAUDE.md` §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime

- **Edit 1:** nothing at shipped fixtures. `season_of_year` returns 0 to 3 in place of `None`;
  `season_factor_of` still returns the bare constant while `season_factor_draw` is `()`. Hash EQUAL.
- **Edit 2:** nothing. A `Question` (not world state, never hashed) carries one more tuple that no
  function under `decision/` reads. Hash EQUAL, formations unchanged.
- **Edit 3 (held):** with `crisis_arm: rule` (control) nothing. With `drawn`: a crisis of conviction is
  resolved by a keyed draw and emits `conviction.moved`. A declared mover in every realm season in
  which a person reaches the threshold (6 / 8 / 8 persons in four seasons at seeds 0 to 2).

## The problems, with evidence

1. **The calendar exists only when it rains.** `world_q.season_of_year` (`:1169-1175`) is
   `tick % len(season_factor_draw)`, and that fixture is the *weather* arm, shipped `()`. So the engine
   has no season of the year at shipped values (the CALENDAR line of every run in the audit's E-N04
   prints `season_of_year=None`), a chronicle can print only a season index (WR F-WR-14), and any rule
   counted in years (FA's seat terms, `06_FA_seat_terms_by_body_B.md`: "a year of four seasons") must
   restate the number. Two facts, one owner: how long a year is, and how the weather varies in it.
2. **A stamped referent forgets why it was stamped.** `world_q._stamped` (`:3836-3851`) writes
   `(id, class)`. Eleven terms feed it (`questions_for`, `:4260-4267`). 262 / 290 / 298 executed acts in
   four seasons (17%) took their subject from a stamped referent; for none can the record say whether
   the seat was vacant, heard of, or at stake in a rising.
3. **A creed breaks by rule, in silence.** `loop/resolve.py::_conviction_crisis` (`:690-733`): "Nothing
   is emitted"; `person_q.conviction_after_crisis` (`:900-…`): "THE ENGINE CHOOSES PER CASE, BY A RULE OVER
   STATE … AND ROLLS NOTHING", and under the shared column "folds the HIGHER-held creed into the lower".
   `write_matrix.yaml:246` declares `emits: conviction.moved` with "No producer". 6 / 8 / 8 persons'
   convictions changed in the audit's runs; no Event, claim or chronicle line records any of them.

## The resolutions, decided

1. **The year is a roster; the weather reads it.** Ladder step 5 (a second copy of one fact: §0.05
   clause 3). 2. **The ground rides beside the class.** Ladder step 4 (`Question.classes` is itself the
   precedent: a parallel partition added so "neither side's formations move the other's"). 3. **A crisis
   is a thing that could go either way for the person, so it is drawn; and it happened, so it is an
   Event.** Ladder step 1 against step 1: the standing rule (2026-11-12) supersedes a ruled "rolls
   nothing" (2026-10-06) only if Jordan says the rule reaches it; hence held.

## Exact edits, by owner

**1. The year.**
- `engine/season/rosters.yaml`: an ordered roster `seasons_of_year`, `values: [spring, summer, autumn,
  winter]`, `ordered: true`, with the note that its length is the year (`data/fixtures.py:235` already
  speaks of "two years at four seasons"); names `[ASSUMPTION; medium; Jordan to correct]`.
- `engine/season/queries/world_q.py::season_of_year`: `return w.tick % len(SEASONS_OF_YEAR)`; never
  `None`. `season_factor_of` (`:1178-1205`): its control test becomes `if not table: return base` (it
  reads `season_of_year(w) is None` today), and `season_factors_by_rung`'s the same; a non-empty
  `season_factor_draw` whose length is not the roster's is refused at the fixture's validation, naming
  both. Old behaviour at `()` is preserved line for line.
- WR's `09_WR_B_weather_with_memory_and_the_year.md` defines the year as `tick //
  len(season_factor_draw)`; it should read the roster instead (listed for WR; one owner).

**2. The ground.**
- `engine/season/rosters.yaml`: a closed roster `occasion_grounds`, one member per stamp term, in
  splice order: `vacancy, seat_named, writ_held, record_held, place_named, matter_awaiting,
  larder_in_purview, holding_to_found, own_referent, works_site, proposition_heard, stage, wounded,
  flow_stake, detainee, enemy` (and `own_side`, `flow_within` when D and CR-100 land).
- `engine/season/state/carriers.py::Question`: `grounds: tuple = ()`, pairs `(id, ground)`, refused
  unless each ground is rostered. Not read by `referents_for`.
- `engine/season/queries/world_q.py::questions_for` / `_stamped`: each term's ids are passed with the
  term's roster name, and `_stamped` fills `grounds` for the pairs it keeps (the first, as today).
- Nothing under `decision/` reads it (a test asserts the candidate sets are equal with the field
  filled and emptied). Its readers are the Scene store (`01_CORE_reason_trail_in_the_act_store.md`) and
  the chronicle's `why` (`09_WR_story_instruments_that_can_fail.md` edit 5; `09_WR_B_chronicle_that_tells.md`).

**3. The crisis (held).**
- `engine/season/data/fixtures.py`: `crisis_arm="rule"`, roster `crisis_arms: [rule, drawn]`.
- `engine/season/loop/resolve.py::_conviction_crisis`: at `drawn`, for each person the rule would
  move, one keyed draw `draw_factory(w.world_seed, lambda: w.tick)(pid, "crisis")` on the shared ladder
  (`dice_engine.degree_from_net`, the one owner). Pool: the intensity of the affiliation in crisis (how
  firmly it was held). Obstacle: the scar count on it less `SCAR_CRISIS_AT − 1` (how far past the
  threshold the wounds have run). Bands: **Overwhelming** the creed holds and its count is set back to
  `SCAR_WEIGHT_SHIFT_AT` (faith renewed under trial); **Success** it holds, nothing written; **Partial**
  its intensity falls by one; **Failure** the ruled branch (`conviction_after_crisis`, unchanged).
- The same write emits `conviction.moved` when the vector changes (the kind the matrix already
  declares), subject the person. The docstring's objection ("an Event here would deposit claims about
  every observer") is answered by scope: it is deposited to the person himself, and to others only
  through the notice draw of `18_DETERMINISM_notice_is_a_draw.md` (a change of heart is not public).
- `[ASSUMPTION; medium; Jordan to correct; revert: `crisis_arm: rule`]` for the pool, the obstacle and
  the four bands.

## The gates (execution artifacts)

1. Edit 1: `build_realm(0)` and the one- and two-season pins EQUAL; `season_of_year` reads 0, 1, 2, 3,
   0 over five ticks; with WR's weather arm on, the three-hash equality of `test_season_weather.py`
   holds at `()`.
2. Edit 2: pins EQUAL; a three-season run at seeds 0 to 2 in which every executed act whose subject
   came from a stamped referent prints a ground (today: none can), and the distribution over grounds is
   reported per seed.
3. Edit 3: `rule` reproduces the pins; at `drawn`, seeds 0 to 4, four seasons: all four bands occur
   over the pooled crises; the same seed twice gives the same crises; `conviction.moved` count equals
   the count of changed vectors; a draw-seed arm (`storybar --draw-seeds`) changes which persons break.

## The falsifiers

- Edit 1: any hash moving at `()`.
- Edit 2: a candidate set that differs with `grounds` filled.
- Edit 3: one band taking every crisis (the pool and obstacle are mis-scaled; re-sweep), or
  `conviction.moved` reaching every co-present ledger (the scope leaked).

## NERS reading

- **N.** Without 1 the game cannot say "in the autumn of the second year" and every yearly rule
  restates four. Without 2 a sixth of all acts have a subject and no occasion. Without 3 the one event
  in which a person's inner life changes is unrecorded and uniform. Each holds in more than one
  direction: 1 is read by weather (WR), terms (FA) and the telling; 2 by CORE, WR and CHAR; 3 by CHAR's
  scar, `20_NARRATIVE_A`'s regimes (a broken creed changes whom he credits) and the telling.
- **R.** 3 is the no-player half directly: who keeps faith under what he has seen is drama with nobody
  acting. Complete: a person with no conviction, or below the threshold, is untouched.
- **S.** One year, one owner; one ground per stamp; the crisis on the same ladder as every other draw.
- **E, last.** Three edits of a few lines each against three lines of every chronicle. High for 1 and
  2; 3 is high if Jordan lifts the ruling and nil if not.

## Cost class

Edit (1, 2). Small build (3), after Jordan's word.

## Dependency edges

- **WR:** `09_WR_B_weather_with_memory_and_the_year.md` (reads the year roster),
  `09_WR_B_chronicle_that_tells.md` and `09_WR_story_instruments_that_can_fail.md` edit 5 (print the
  ground and the season).
- **CORE:** `01_CORE_reason_trail_in_the_act_store.md` (keeps the Question that carries `grounds`).
- **FA:** `06_FA_seat_terms_by_body_B.md` (terms in years).
- **CHAR:** `02_CHAR_scar_is_a_wound.md` (fewer, heavier scars make crises rarer and edit 3's draw
  matter more); `02_CHAR_reason_trail_and_small_edits.md`.
- **DETERMINISM:** `18_DETERMINISM_notice_is_a_draw.md` (edit 3's scope); the sweep's code list does not
  hold this site, so it is an addition to it.
- **Plan:** CR-100 (`flow_within` becomes a ground).
