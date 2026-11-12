# NARRATIVE-E — the year and the reason: a calendar that exists, an occasion that keeps its ground, and a crisis of faith that is drawn and seen

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. Edit 1 (the year) is read by the player's marker and recap (`30_GO_F_the_plot_as_the_player_is_shown_it.md`: `View.calendar`, `EraMarker.year`) and by the era condition `dearth` (the realm-rung spell of the year, `30_WR_A` commit 4). Edit 2 (a question's ground) is shown on the slate as `AskedRow.ground`, beside two fields that file adds (`mandatory`, `story`); the roster `occasion_grounds` needs no new member for them. Edit 3's Event (`conviction.moved`) gains three readers: a person's move between regimes (`30_WR_B` commit 2's `moved` line), an era turn when the person is the head seat's holder (`30_WR_B` commit 3), and the edge of a regime moving from core to fringe (`30_WR_G` §3). The reason trail of this lane's §7.5 gains items 8 to 10 in `30_GO_F` (which story the act was a move of; whether it turned the era; what it left behind).

Reconciled: 2026-11-12, U5d closure — folded **A-24**, **A-51** and **A-54**. Edit 3 (held for Jordan; a crisis of conviction drawn and seen) is ruled (the ladder's D-27 under A-24) and is merged under `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`, the one emitter of `conviction.moved`: this file keeps the reason line a narrator reads and writes no second draw. Edit 1 (a roster owns the year; the weather reads it) becomes load-bearing: A-51's five-year prologue and every age in seasons (`majority_age`, `min_parent_age`, the authored ages) are counted on this roster's year, which must therefore be declared at ship and not left to a weather table that ships `()` (`queries/world_q.py::season_of_year`). The weather that reads the year draws on the four-band ladder (A-54).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row the_year_and_the_reason (1, 2 CONFORMS; 3 superseded; ID-13 for edit 2), §2 rows edit 3/Status (A-24, A-30) and edit 1 (A-51, A-15, A-75), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-K2, C3-K11; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-10, §4 row F-43; `unified/U3_DEPENDENCY_ORDER.md` §1 items 13 and 38, §4.1 row 43). The body now follows the head. Changed: (1) edit 3's draw, its band table and the `crisis_arm` fixture are struck from this file: the crisis is drawn and seen (A-24) and `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` is its one emitter and owns its one switch (U1 F-43 names that switch `crisis_arm`); this file keeps only the reason line a narrator reads off CHAR_A's `conviction.moved` Event; the Status line's hold is gone (A-24 overwrote `ED-IN-0261`'s "rolls nothing"); problem 3 stays as the finding; (2) edit 1 is the one owner of the year (D-U1-10: four seasons by `ED-IN-0332`, RULED; only the four names are an assumption) and lands at the head of B12 (C3-K11), before the regrowth, the weather and A-51's five-year prologue that read it; every other file reads `len(SEASONS_OF_YEAR)` and states no "4"; (3) edit 2's field lands in one commit with its first reader (`04` ID-13); (4) tests named; (5) dependency, batch and tier lines.

Depends on: edit 1: nothing (it lands first in B12). Edits 2 and the reason line: `01_CORE_reason_trail_in_the_act_store.md` (B09, keeps the Question), `09_WR_B_chronicle_that_tells.md` and `09_WR_story_instruments_that_can_fail.md` (B36, the chronicle's `why`), `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (B10, the `conviction.moved` Event).
Lands in batch: edit 1 at the head of B12 (lanes SE and WR; hash-equal); edit 2 and the reason line in B38 after `20_NARRATIVE_D` (hash-equal).
Tier: sonnet / high.

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-06, F-NARR-08, §5 (the reason trail's three losses), §7.5.
Three small edits at three owners, grouped because each supplies one line a narrator needs (when; on
what occasion; what broke). Reference only (`CLAUDE.md` §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime

- **Edit 1:** nothing at shipped fixtures. `season_of_year` returns 0 to 3 in place of `None`;
  `season_factor_of` still returns the bare constant while `season_factor_draw` is `()`. Hash EQUAL.
- **Edit 2:** nothing. A `Question` (not world state, never hashed) carries one more tuple that no
  function under `decision/` reads. Hash EQUAL, formations unchanged.
- **Edit 3 (the reason line):** nothing. The crisis draw and its `conviction.moved` Event are
  `16_PESSIMIST_CHAR_A`'s (B10); this file adds only the narrator's one-line `why` read off that Event.
  Hash EQUAL.

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
   Event.** Jordan's A-24 ruled it (drawn and seen), superseding `ED-IN-0261`'s "rolls nothing"; the
   draw and the Event are carried by `16_PESSIMIST_CHAR_A`, the one emitter of `conviction.moved`; this
   file keeps the reason line.

## Exact edits, by owner

**1. The year.**
- `engine/season/rosters.yaml`: an ordered roster `seasons_of_year`, `values: [spring, summer, autumn,
  winter]`, `ordered: true`, with the note that its length is the year (`data/fixtures.py:235` already
  speaks of "two years at four seasons"; the length is `ED-IN-0332`, RULED, D-U1-10); the four names
  `[ASSUMPTION; medium; Jordan to correct]`. **The one owner of the year:** A-51's five-year prologue
  (`5 × len(SEASONS_OF_YEAR)`), every age in seasons (`majority_age`, `min_parent_age`, the authored ages
  of `22_HAPPENINGS_A`) and every yearly term read `len(SEASONS_OF_YEAR)`; no file states "4". The
  overview oracle's `SEASONS_PER_YEAR` (`systems/overview/sim/ms_track.py:49`) is read by nothing in
  `engine/season` or `modules/` and is left to that oracle's retirement (D-U1-10).
- `engine/season/queries/world_q.py::season_of_year`: `return w.tick % len(SEASONS_OF_YEAR)`; never
  `None`. `season_factor_of` (`:1178-1205`): its control test becomes `if not table: return base` (it
  reads `season_of_year(w) is None` today), and `season_factors_by_rung`'s the same; a non-empty
  `season_factor_draw` whose length is not the roster's is refused at the fixture's validation, naming
  both. Old behaviour at `()` is preserved line for line.
- WR's `09_WR_B_weather_with_memory_and_the_year.md` defines the year as `tick //
  len(season_factor_draw)`; it reads the roster instead (listed for WR; one owner). The same for
  `16_PESSIMIST_WR_C_illness_on_the_body_ladder.md` (`born = -4 × age` → `-len(SEASONS_OF_YEAR) × age`),
  `06_FA_seat_terms_by_body_B.md` ("a year of four seasons" → "a year, `20_NARRATIVE_E` edit 1") and
  `07_SE_population_regrowth_B.md` ("twenty seasons" → "five years of the declared year") (C3-K11; each
  for its own rewrite lane).

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
  filled and emptied). Its readers are the Scene store (`01_CORE_reason_trail_in_the_act_store.md`,
  which keeps the Question, B09) and the chronicle's `why` (`09_WR_story_instruments_that_can_fail.md`
  edit 5; `09_WR_B_chronicle_that_tells.md`, B36). **`04` ID-13 (a field with no reader at landing is not
  carried):** the field lands in B38 in one commit with the chronicle line that prints the ground, so it
  has a reader the day it exists.

**3. The reason line (the crisis itself is `16_PESSIMIST_CHAR_A`'s).**
- No draw, fixture or switch is written here. The crisis draw, its bands, its `conviction.moved` Event
  and its one switch (named `crisis_arm`, U1 F-43) are owned by
  `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (B10); a second draw here would be a
  second ladder for one quantity and a key with no act in its purpose (two crises of one person in one
  tick would share it).
- What stays: the narrator's one-line `why`, read off CHAR_A's `conviction.moved` Event (which
  affiliation broke, into what, after which scars), printed by the chronicle beside the season of the
  year (edit 1) and the ground (edit 2). The three readers named in this file's first Folded paragraph
  read the same Event.

## The gates (execution artifacts)

Tests: `engine/season/tests/test_season_weather.py` (exists) gains
`test_season_of_year_reads_zero_to_three_at_shipped_fixtures` and
`test_nonempty_season_factor_draw_of_wrong_length_is_refused`; NEW
`engine/season/tests/test_question_grounds.py`: `test_candidate_sets_equal_with_grounds_filled_and_emptied`,
`test_every_stamped_executed_act_prints_a_ground`.

1. Edit 1: `build_realm(0)` and the one- and two-season pins EQUAL; `season_of_year` reads 0, 1, 2, 3,
   0 over five ticks; with WR's weather arm on, the three-hash equality of `test_season_weather.py`
   holds at `()`.
2. Edit 2: pins EQUAL; a three-season run at seeds 0 to 2 in which every executed act whose subject
   came from a stamped referent prints a ground (today: none can), and the distribution over grounds is
   reported per seed.
3. The reason line: every `conviction.moved` Event in a four-season run at seed 0 prints one `why` line
   in the chronicle; the gates of the crisis draw itself are `16_PESSIMIST_CHAR_A`'s.

## The falsifiers

- Edit 1: any hash moving at `()`.
- Edit 2: a candidate set that differs with `grounds` filled.
- The reason line: a `conviction.moved` Event with no `why` line, or a `why` line with no Event.

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
  2; 3's mechanism is CHAR_A's, and the reason line costs one chronicle line.

## Cost class

Edit (1, 2, 3).

## Dependency edges

- **WR:** `09_WR_B_weather_with_memory_and_the_year.md` (reads the year roster),
  `09_WR_B_chronicle_that_tells.md` and `09_WR_story_instruments_that_can_fail.md` edit 5 (print the
  ground and the season).
- **CORE:** `01_CORE_reason_trail_in_the_act_store.md` (keeps the Question that carries `grounds`).
- **FA:** `06_FA_seat_terms_by_body_B.md` (terms in years).
- **CHAR:** `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (the crisis draw and the
  Event the reason line reads); `02_CHAR_scar_is_a_wound.md`; `02_CHAR_reason_trail_and_small_edits.md`.
- **DETERMINISM:** `18_DETERMINISM_notice_is_a_draw.md` (who notices a crisis: CHAR_A's scope).
- **Every reader of the year:** `16_PESSIMIST_WR_C`, `07_SE_population_regrowth_B.md`,
  `21_PROCEDURAL_C_prologue_and_case_seeds.md` (the prologue), `22_HAPPENINGS_A` (ages), `23_STORY_B`
  (`majority_age`), `23_STORY_E` (`age_years`).
- **Plan:** CR-100 (`flow_within` becomes a ground).
