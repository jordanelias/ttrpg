# STORY-E — the first playable for stories: *The Lean Year*, a valley, a granary, an old lord, two claimants, a bench and a forged sheet

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` (§9). Nothing here is deleted. The valley is also the first playable for an era that ends: the old lord's death is a change of RULE, the two claims are one strand whose subject is the seat, and the lean year is the condition `dearth` (`30_WR_A`). A seated player there is shown the marker, the vacancy as a mandatory question, the claims as one named story, news filed under its story and a recap at each season's turn (`30_GO_F_the_plot_as_the_player_is_shown_it.md`); its seat test (`--stories --seat`) is run on this fixture. Chains K-1 and K-2 of `30_WR_E` §1 are the two this scenario can complete.

Reconciled: 2026-11-12, U5d closure — folded **A-54**, **A-56**, **A-50** and **A-51**. The lean year's harvest is a draw on the four-band ladder with the steward's skill in the pool; the valley's cohorts answer want by the heavy moves (petition, migrate, work, tend, comply or refuse, riot); starting stores may be drawn within the fixture's bounds. As a scenario on the valley fixture it declares its own year and may run a prologue shorter than the realm's five years only as a named fixture choice, stated in its header; the realm's rule is five.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row lean_year CONFORMS (valley files MISSING until SE lands), §2 rows `persons` ages (A-15, A-51) and prehistory (A-81, A-30), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-K10; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-09, D-U1-10; `unified/U1_GLOSSARY.md` "census"; `unified/U3_DEPENDENCY_ORDER.md` §1 item 39, §3.1). Changed: (1) ages are authored as `age_years:` and converted by the builder through `22_HAPPENINGS_A` edit 1's one writer of `Person.born` (`-len(SEASONS_OF_YEAR) × age_years`; C3-K10, D-U1-10): `age: 68` read as seasons would have made a nine-year-old heir two years old; (2) the rows' key names, marked `[UNVERIFIED beyond those proposals' heads]`, were read against `07_SE_valley_scenario.md`'s `valley.yaml` sketch (`persons` carry `lives:`, `seats` carry `rung:`, `remit:`, `holder:`, `lives:`) and corrected to them; two collisions with SE's rows are resolved (SE's `p_reeve` lives in the harbour town, so this file's seam-village head is `p_seam_reeve`; SE already declares `off_steward`, so this file adds one key to it instead of redeclaring it); the keys SE's rows do not carry (`age_years`, `conferral`, `sworn_to`, a seat with several `holders`) are listed for SE's loader; (3) the U5d line's "the steward's skill in the pool" reads, by D-U1-09, as named levels for the place's draw (the place rolls, the steward is not the roller); (4) the prehistory forge's quality is that act's keyed draw (A-30), not authored; (5) "the census" is the story count (glossary); (6) tests named; (7) dependency, batch and tier lines.

Depends on: `07_SE_valley_scenario.md` (B12; `valley.yaml`, `harness/valley.py`, absent from the tree until then); `08_FI_07_shortest-playable-case.md` (B11); `14_VERBS_BINDING_C_turnover.md` (B21); `05_SC_playable_hearing_B.md` (B24); `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` (B37; `age_years` and the `born` writer); `23_STORY_D_story_census_and_gate.md` (B36); `30_GO_F_the_plot_as_the_player_is_shown_it.md` (B38); `12_ARCS_case_on_the_realm.md` (B39, the prehistory fold); `23_STORY_B`, `23_STORY_C` (B39) for cuts 2 and the upper hearth's ending.
Lands in batch: B39 (lane SE; all lanes meet), last item; rows and preset one commit, each cut's gate read in the batch that lands its stories.
Tier: sonnet / high.

## Status: PROPOSED

Source: `audits/23_STORY_ENABLEMENT.md` §7. Composes on, and does not restate:
`07_SE_valley_scenario.md` (`engine/season/valley.yaml`, `harness/valley.py`: three towns unlike in
endowment, one granary, one seat, a planned works), `12_ARCS_case_on_the_realm.md` (the prehistory
fold: a setup may contain acts and never an outcome), `19_LACUNA` §6 and `08_FI_07_shortest-playable-case.md`
(the inquiry-to-hearing case), `05_SC_playable_hearing_B.md`, `22_HAPPENINGS_A`, `_B`,
`14_VERBS_BINDING_C_turnover.md`, `23_STORY_A` to `_D`. Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

**Nothing in the loop, the modules or the realm.** It adds rows to one fixture world and a preset to
its harness. The scenario runs the unmodified `SeasonDriver`, the registered modules and the shipped
chooser; a played seat is `harness/play_surface.dispatching_chooser(auto, {pid: callback})`. The played
and the unplayed valley are one code path by construction, and no hash of any other world moves.

## The problem, with evidence

- Each lane's standalone exercises its own subsystem (the valley for settlements, the spine for
  governance, the inquiry world and the hearing for FI and SC, the vacant chair for the Church), which
  is the standing requirement. A story crosses them, and nothing plays the crossing at a size a reader
  can hold: SYN's *The King's Bill* is the realm, eight seasons, 83 persons.
- The story count (`23_STORY_D`) needs a world cheap enough for 20 seeds (a realm season cost the pessimist
  lanes 30 to 190 seconds on the loaded machine; `16_PESSIMIST_CHAR.md` §3.5).

## The resolution, decided

One scenario on the valley fixture, extended by rows; not a third case base (`12_ARCS_case_on_the_realm`
allows `realm` and `template` and no third: this is a scenario beside `harness/scarce.py`, and it
borrows only that proposal's prehistory fold). Roles, no canon names. The setup names persons, seats,
stores, one works, ties and prehistory acts; it names no outcome and no act after tick 0 (ARCS's
falsifier, applied: a setup key whose row writes a field an ending reads is refused by the loader).
Ladder step 3 (ARCS; the standing requirement), step 4 (the valley and the spine as fixture worlds).

## Exact edits, by owner

**1. `engine/season/valley.yaml` — rows added** (the file SE's proposal creates; its banner *a test
fixture, not canon* covers these).

```yaml
persons:          # roles; the builder names them by `21_PROCEDURAL_E`'s grammar or leaves ids
  - {id: p_lord,       age_years: 68, lives: set_field}       # the old lord; authored one body band below the top
  - {id: p_heir,       age_years: 9,  lives: set_field}       # his grandchild, under majority_age
  - {id: p_mother,     age_years: 31, lives: set_field}       # the heir's mother, the lord's son's widow
  - {id: p_nephew,     age_years: 34, lives: set_harbour}     # of age; a following in the harbour town
  - {id: p_steward,    age_years: 47}                         # keeps the granary; `lives:` is SE's seat row's
  - {id: p_seam_reeve, age_years: 52, lives: set_seam}        # head of the seam village (SE's `p_reeve` is the harbour town's)
  - {id: p_judge_a,    age_years: 58, lives: set_field}
  - {id: p_judge_b,    age_years: 44, lives: set_field}
  - {id: p_judge_c,    age_years: 39, lives: set_harbour}
seats:            # SE's row `off_steward` (rung terr_valley, remit [issue], holder p_steward) is not redeclared: it gains `sworn_to` only
  - {id: off_valley_lord, rung: terr_valley, holder: p_lord, lives: set_field, conferral: inheritance}
  - {id: off_steward, sworn_to: off_valley_lord}              # one key added to SE's row
  - {id: off_bench,       rung: terr_valley, holders: [p_judge_a, p_judge_b, p_judge_c], remit: [determine]}
  - {id: off_valley_heir,    holder: p_heir}                  # three titles with no remit of their own
  - {id: off_valley_dowager, holder: p_mother}
  - {id: off_valley_cadet,   holder: p_nephew}
successions:
  off_valley_lord: [off_valley_heir, off_valley_dowager, off_valley_cadet]   # HAPP-B's shape: a set of claimant titles
relations:        # `02_CHAR_relations_have_a_ground`: each seeds a stance row and the holder's own claim
  - {of: p_nephew,     to: p_steward, ground: "an old wrong", sign: -1}
  - {of: p_seam_reeve, to: p_steward, ground: "the field", sign: -1}
planned_works:
  - {id: works_upper_hearth, kind: works, plan: hearth, at: set_seam, rung: set_seam, master: p_seam_reeve, terms: 3}
prehistory:       # folded through the real RESOLVE and WITNESS before tick 0, with the scenario's seed
  - {actor: p_steward,    verb: forge,    subject: "a sheet granting the seam field to off_steward"}
  - {actor: p_seam_reeve, verb: petition, subject: "the seam field", to: off_bench}
```

The forged sheet starts in the steward's own hold; its quality is that `forge`'s keyed draw (A-30), not
authored. Whether it ever reaches the bench, an examiner or a rival is play.

Key names follow SE's `valley.yaml` (`07_SE_valley_scenario.md`: `persons` carry `lives:`, `seats` carry
`rung:`, `remit:`, `holder:`, `lives:`) and ARCS's `setup.prehistory` (`{actor, verb, subject}`,
`12_ARCS_case_on_the_realm.md` §3 item 3). Keys this file needs that SE's rows do not carry: `age_years`
(read through `22_HAPPENINGS_A` edit 1's writer: `Person.born = -(age_years × len(SEASONS_OF_YEAR))`),
`conferral`, `sworn_to`, `holders` (a seat with several holders) and the `to:` of a prehistory petition;
SE's loader admits them in its closed key set or refuses them by name (listed for the SE lane). The three
towns' endowments, the granary and the weather are SE's rows, unchanged. Nothing above states what anyone
will do.

**2. `engine/season/harness/valley.py` — `lean_year(seed, seasons, play=None)`**: `build(seed)` with
the rows above, the prehistory folded by the function ARCS adds to `harness/corpus_run.py`, then
`run`. `sheet(w)` gains the lines a seat needs: who is believed to hold the seat and the granary, what
the granary holds as the seat believes it, who is ill, what is on the bench's docket, each open due.
`endings(w, d) -> list`, each a Query over Tenures and the log:

| ending | reads |
|---|---|
| the seat held in full | a live `hold` on `off_valley_lord` with no term |
| a regency confirmed, or lapsed | a termed `hold` on it whose term was removed, or matured |
| the valley thinned | summed cohort weight at or under half its tick-0 value |
| the steward convicted, acquitted, or dead | a disposal edge on him; `matter.dismissed` on his case (a kind not declared at the tree; prints `n/a` until its carrier lands, `23_STORY_D`); `person.died` |
| the upper hearth peopled, or abandoned | a `reside` edge under it; `rung.abandoned` |
| a stable continuation | eight seasons with none of the above |

**3. Three cuts, by what has landed** (the audit's §7 table): cut 1 after batch E-3 (the year: 11
stories), cut 2 after E-5 (the seat: 10 more), cut 3 after E-7 (the wrong: 12 more). A cut is the same
world and command; the stories outside it print `n/a` in the story count.

## The gate (execution artifact)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 20 --seasons 8 --arms control on --stories --world valley
PYTHONHASHSEED=0 python -m engine.season.harness.valley --lean-year --seed 0 --seasons 8 --play p_steward
```

With the shipped chooser in every seat (first command), at the third cut:

1. at least 12 distinct stories occur across the 20 seeds, and each that occurs meets clauses C1 to C6
   of the audit's §6.1;
2. at least four distinct endings occur; no more than three seeds share one story set and one ending;
3. in the control arm (every batch fixture at control) the story count reads only the control shapes;
4. planted failure: with `--pin-rolls Success` the seeds agree on the ending, or the variety was not the
   draws';
5. a played seat changes the ending: for each of four seats (the steward, the nephew, the mother, the
   reeve) one played run at seed 0 whose ending differs from the unplayed seed 0; control: the same
   seed with the callback returning the chooser's own pick has the unplayed hash.

Story bar test: the scenario's loader test plants an outcome in the setup (a `hold` for the nephew on
`off_valley_lord` at tick 0) and must be refused. Tests: NEW `engine/season/tests/test_lean_year.py`:
`test_setup_that_plants_an_outcome_is_refused`, `test_played_seat_with_own_pick_equals_unplayed_hash`
(clause 5's control), `test_endings_are_queries_over_tenures_and_log`, `test_age_years_converts_through_the_year_roster`.
The `--lean-year` flag of the second command is part of edit 2 (`harness/valley.py`'s entry).

## The falsifier

- The same ending at 18 of 20 seeds: the build decides it (the lord's body, the stores), and a row is
  an outcome in disguise.
- A story that occurs only where a prehistory act named its subject and no other: scripting drift;
  remove the act and it must still be able to occur by another route, or it is not this scenario's.
- Clause 5 failing for every seat: a player's choice changes paper, as GAME found of the realm.

## NERS reading

- **N.** Cut it and the stories are gated only on the realm, at five seeds, where a reader cannot hold
  the world. It holds from the six directions as an exercise: each scale and three subsystems meet in
  one valley.
- **R.** With no player it must produce a different year at different seeds; with one, any of seven
  seats is playable and none is privileged.
- **S.** One fixture world, one runner, one census, one prehistory fold; zooms from a season's harvest
  to a single exchange in a hearing with no second path.
- **E, last.** About forty rows of fixture and one preset, for 33 stories on one page. High.

## Cost class

Edit (rows) and small build (the preset and `endings`); one session per cut.

## Dependency edges

Needs first: `07_SE_valley_scenario.md`; `12_ARCS_case_on_the_realm.md` (the prehistory fold);
`23_STORY_D`. Cut 1: batch E-3. Cut 2: E-4, E-5 (`23_STORY_B` for the minor heir). Cut 3: E-6, E-7.
`23_STORY_C` for the upper hearth's ending (E-11; until then that ending prints `n/a`). SYN's *The
King's Bill* remains the realm's first playable and is not merged.
