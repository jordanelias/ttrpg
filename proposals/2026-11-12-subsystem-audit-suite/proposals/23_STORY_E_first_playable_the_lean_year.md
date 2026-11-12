# STORY-E — the first playable for stories: *The Lean Year*, a valley, a granary, an old lord, two claimants, a bench and a forged sheet

Reconciled: 2026-11-12, U5d closure — folded **A-54**, **A-56**, **A-50** and **A-51**. The lean year's harvest is a draw on the four-band ladder with the steward's skill in the pool; the valley's cohorts answer want by the heavy moves (petition, migrate, work, tend, comply or refuse, riot); starting stores may be drawn within the fixture's bounds. As a scenario on the valley fixture it declares its own year and may run a prologue shorter than the realm's five years only as a named fixture choice, stated in its header; the realm's rule is five.

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
- The census (`23_STORY_D`) needs a world cheap enough for 20 seeds (a realm season cost the pessimist
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
  - {id: p_lord,     age: 68, home: set_field}                # the old lord; authored one body band below the top
  - {id: p_heir,     age: 9,  home: set_field}                # his grandchild, under majority_age
  - {id: p_mother,   age: 31, home: set_field}                # the heir's mother, the lord's son's widow
  - {id: p_nephew,   age: 34, home: set_harbour}              # of age; a following in the harbour town
  - {id: p_steward,  age: 47, home: set_field}                # keeps the granary
  - {id: p_reeve,    age: 52, home: set_seam}                 # head of the seam village
  - {id: p_judge_a,  age: 58, home: set_field}
  - {id: p_judge_b,  age: 44, home: set_field}
  - {id: p_judge_c,  age: 39, home: set_harbour}
seats:
  - {id: off_valley_lord, over: terr_valley, holder: p_lord, basis: inheritance}
  - {id: off_steward,     over: set_field,   holder: p_steward, sworn_to: off_valley_lord}
  - {id: off_bench,       over: terr_valley, holders: [p_judge_a, p_judge_b, p_judge_c], remit: [determine]}
  - {id: off_valley_heir,    holder: p_heir}                  # three titles with no remit of their own
  - {id: off_valley_dowager, holder: p_mother}
  - {id: off_valley_cadet,   holder: p_nephew}
successions:
  off_valley_lord: [off_valley_heir, off_valley_dowager, off_valley_cadet]   # HAPP-B's shape: a set of claimant titles
relations:        # `02_CHAR_relations_have_a_ground`: each seeds a stance row and the holder's own claim
  - {of: p_nephew, to: p_steward, ground: "an old wrong", sign: -1}
  - {of: p_reeve,  to: p_steward, ground: "the field", sign: -1}
planned_works:
  - {id: works_upper_hearth, kind: works, plan: hearth, at: set_seam, rung: set_seam, master: p_reeve, terms: 3}
prehistory:       # folded through the real RESOLVE and WITNESS before tick 0, with the scenario's seed
  - {actor: p_steward, verb: forge,    subject: "a sheet granting the seam field to off_steward"}
  - {actor: p_reeve,   verb: petition, subject: "the seam field", to: off_bench}
```

The forged sheet starts in the steward's own hold. Whether it ever reaches the bench, an examiner or a
rival is play.

Key names follow SE's `valley.yaml` and ARCS's `setup.prehistory` (`[UNVERIFIED beyond those proposals'
heads]`; the loader's closed key set is theirs). The three towns' endowments, the granary and the
weather are SE's rows, unchanged. Nothing above states what anyone will do.

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
| the steward convicted, acquitted, or dead | a disposal edge on him; `matter.dismissed` on his case; `person.died` |
| the upper hearth peopled, or abandoned | a `reside` edge under it; `rung.abandoned` |
| a stable continuation | eight seasons with none of the above |

**3. Three cuts, by what has landed** (the audit's §7 table): cut 1 after batch E-3 (the year: 11
stories), cut 2 after E-5 (the seat: 10 more), cut 3 after E-7 (the wrong: 12 more). A cut is the same
world and command; the stories outside it print `n/a` in the census.

## The gate (execution artifact)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 20 --seasons 8 --arms control on --stories --world valley
PYTHONHASHSEED=0 python -m engine.season.harness.valley --lean-year --seed 0 --seasons 8 --play p_steward
```

With the shipped chooser in every seat (first command), at the third cut:

1. at least 12 distinct stories occur across the 20 seeds, and each that occurs meets clauses C1 to C6
   of the audit's §6.1;
2. at least four distinct endings occur; no more than three seeds share one story set and one ending;
3. in the control arm (every batch fixture at control) the census reads only the control shapes;
4. planted failure: with `--pin-rolls Success` the seeds agree on the ending, or the variety was not the
   draws';
5. a played seat changes the ending: for each of four seats (the steward, the nephew, the mother, the
   reeve) one played run at seed 0 whose ending differs from the unplayed seed 0; control: the same
   seed with the callback returning the chooser's own pick has the unplayed hash.

Story bar test: the scenario's loader test plants an outcome in the setup (a `hold` for the nephew on
`off_valley_lord` at tick 0) and must be refused.

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
