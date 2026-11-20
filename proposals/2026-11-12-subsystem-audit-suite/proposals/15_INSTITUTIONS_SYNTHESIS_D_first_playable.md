# INST-SYN-D — the first playable of the institutions together: "The King's Bill"; one scenario style; one report

Reconciled: 2026-11-12, U5d closure — folded **A-12**, **A-14** and **A-10**: the first playable is a scenario on the season loop (no module); its ballots are draws on each voter inside the presiding act; a seat in it may carry a modifier once the kit authors one. No step changes.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (SYN_D: CONFORMS), §2 (A-80 row), §7 (INCOMPLETE: the A-80 arm), 7b.0, 7b.7; `U3_CONFLICT_LEDGER.md` C3-C12 (one entrenched-world arm, read by `23_STORY_D`); `U3_DEPENDENCY_ORDER.md` (B40; the I-n batches mapped to the handles); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11k (`remove` → `distance`); `U1_GLOSSARY.md` *scenario*. Changed: gate 8 (A-80); the borrowing and roll report lines read the lapse when read and say "list" (VENICE-B, -C as reconciled); `remove` → `distance`; the batch names. In new text the standalone setup is a **scenario**; its YAML is the scenario's case file (ARCS-01's file shape); `situation` stays the name of FA-P4's argument.

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B40** (institutions scenarios, FA), first (`U3_DEPENDENCY_ORDER.md` §1 item 40). Depends on: `06_FA_playable_scenario.md` (B21, the runner), `12_ARCS_case_on_the_realm.md` (B39, the case delta and tick-0 prehistory), and the kit's batches B32 and B33 (every cut's content). This file's "I-n" batch names are SYNTHESIS-E's; in the suite's one order I-1 to I-8 fall in B32 and B33 (SYNTHESIS-E's mapping) and the prehistory in B39, so every cut runs after B39. Lane tag: FA. Tier: `sonnet` (harness), effort `high`; one `opus` read of gates 1 to 3 and 8. Named test: none (its own sentence, CLAUDE.md §0.1 pt 5); the gates are runs of `python -m engine.season.harness.institution INST-01 8 <seed>` quoted in the commit. The `counting_house.py` probe `U3_DEPENDENCY_ORDER.md` §6 lists is not written and is no gate here (§1). Standing sentences: *Pool*, *Failure writes*, *Draw keys* — the scenario adds no roll, no row and no draw; each is the composed proposals' (A-6 to A-8, A-81, A-30). *Entrenchment* — gate 8 (A-80).

Source: `audits/15_INSTITUTIONS_SYNTHESIS.md` §6, §7.6, §9.3; the standing requirement of
`AUDIT_BRIEF.md` (playable alone, one code path, integrated, no GM). Merges the first cuts of
`15_INSTITUTIONS_BYZANTINE_F` (`roga`), `15_INSTITUTIONS_VENICE_D` §5 (The Counting-House),
`15_INSTITUTIONS_COLONIAL_E` (The Farm of the Southern Tolls) and `15_INSTITUTIONS_PAPACY.md` §11's
third scenario (The Sentence) into one scenario on the realm. Composes on `06_FA_playable_scenario.md`
(FA-P4: `play`, `situation`, `digest`, `offered`), `06_FA_shortest_loop_B.md` (FA-B4: `world="realm"`),
`12_ARCS_case_on_the_realm.md` (a case is a delta; prehistory through the fold). Batch I-9 of
SYNTHESIS-E, which is B40 in the suite's one order. Ratifies nothing.

## What it changes in `engine/season/` at runtime

Nothing on the game path. It adds one case file and one read-only report, and makes FA's runner read a
scenario from a case file. No file under `loop/`, `state/`, `queries/`, `decision/` or `data/` changes; a
run's `content_hash` equals the same seasons through `populated.run` with the same chooser on the same
world after the same tick-0 acts (FA-P4's control).

## The problem (evidence)

- Each family has a scenario that exercises it alone and none that makes two institutions meet. The
  crossings of audit §5.2 are therefore designed and unplayed.
- The four families state a scenario four ways (audit X-32): set-up acts written in Python in
  `harness/governance_spine.py` (`15_INSTITUTIONS_BYZANTINE_F` edits 1, 2); command-line flags
  (`15_INSTITUTIONS_PAPACY_F` edit 1); rows added to the spine fixture plus a reading script
  `counting_house.py` (`15_INSTITUTIONS_VENICE_D` edits 4, 5); a case file under `cases/exercises/` plus
  a report `harness/institution` (`15_INSTITUTIONS_COLONIAL_E`). Four digests would print four subsets of
  the same log.
- Every reading of a drawn procedure is a distribution; one seed is a trajectory (CLAUDE.md §0.1 pt 4).

## The resolution, decided

### 1. One scenario style: a scenario is data, a runner and a report

Ladder step 4 (`12_ARCS_case_on_the_realm.md`: a case is a delta on a base; `06_FA_playable_scenario.md`:
one runner) and step 5.

- **The situation is a case file** under `engine/season/cases/exercises/`, in ARCS-01's delta shape:

  ```yaml
  id:    <case id>
  base:  realm | spine            # an existing builder: populated.build_realm, governance_spine.build
  setup:
    seats:        [<offices.yaml-shaped rows the base lacks>]
    instruments:  [<instruments.yaml `seeded:`-shaped rows>]
    stores:       {<rung id>: {<matter kind>: <units>}}
    prehistory:   [{actor, verb, subject, ...}]     # folded through the real RESOLVE and WITNESS at tick 0
  seats_offered:  [<seat ids a player-proxy may take>]
  ends:           [<a Query name>]                    # each a pure reader over Tenures and the log
  span_seasons:   <int>
  ```

  A set-up act the fold refuses fails the build, naming the refusal (ARCS-01). Set-up acts resolve under
  the pinned roll, so the situation is the same at every seed; play is unpinned. A scenario may not
  pre-write its own ending: the loader refuses a prehistory act whose row writes a field an `ends` Query
  reads as terminal (ARCS-01's falsifier).
- **The runner is FA's.** `harness/governance_spine.py::play(seed, seasons, situation, player, pick=None,
  world=…)` takes a case id as its `situation`; `situation()` builds the case's base and applies the
  delta. FA-P4's three hand-written situations stay as they are; nothing is added to that function for
  an institution.
- **The report is one module**, `engine/season/harness/institution.py`
  (`15_INSTITUTIONS_COLONIAL_E`'s, widened): `python -m engine.season.harness.institution <case>
  <seasons> <seed> [--bands N]`, output to a path the caller gives. Read-only; `harness/strife.py`'s
  kind; no assertion that a story occurs; not a guard and not a standing corpus.

Reconciled: `roga` and `chancery` are case files with `base: spine` (their set-up acts move from Python U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fisc" → "treasury" (glossary loan words).
into `setup.prehistory`); The Vacant Chair is a case file with `base: realm` whose one prehistory act is
the holder's `release`; The Counting-House is a case file with `base: spine` whose seats, stores and
instruments are its delta, and `counting_house.py` is not written; The Farm of the Southern Tolls is
already this shape. `15_INSTITUTIONS_BYZANTINE_F` edit 3's seven digest lines and edit 5's `bands=N` are
lines and an option of the one report.

### 2. The scenario: "The King's Bill"

```yaml
id:    INST-01
base:  realm
setup:
  seats:
    - {id: off_house_case_lender, post: "Family Head", rung: {venue: "<the guildhall NPC-007 is homed in>"},
       body: null, faction: "Guilds", remit_acts: [issue, confer], conferral: null, revocation: null,
       holder: "NPC-007"}                                   # until batch I-8 authors it in offices.yaml
  instruments: []                                           # the realm's own seeded rows (I-3): two `homage`, one `immunity`
  stores:
    r_valoria:        {grain: 4}                            # the treasury: less than the year's bill   [ASSUMPTION; sweep ×{0.5, 1, 2}]
    duchy_hafenmark:  {grain: 12}
    duchy_varfell:    {grain: 12}
    terr_T9:          {grain: 10}                           # inside the immunity
    set_s_012:        {grain: 12}                           # Stillhelm
    <the lender's hearth>: {grain: 10, salt: 6}
  prehistory:                                               # each through the fold, pinned
    - {actor: <two cast persons with a deed the King holds a claim of>, verb: oblige, subject: off_king}
    - {actor: NPC-020, verb: confer, subject: off_dignity_2a, to: <the first>,  cites: <his deed>}
    - {actor: NPC-020, verb: confer, subject: off_dignity_3a, to: <the second>, cites: <his deed>}
seats_offered:  [off_king, off_duchess_hafenmark, off_house_case_lender, <a hearth head of set_s_013>, off_cardinal_justice]
ends:           [court_kept, court_lapsed, bond_met, bond_lapsed, audit_determined, sentenced, no_seat, season_count]
span_seasons:   8
```

Stores are in `default_store_kind` (audit X-30). Every number is `[ASSUMPTION]` content with a sweep; the
only requirement on them is that the treasury is short of the bill and the other chests are not.

**What the player in `off_king` is shown each season** (FA-P4's `offered`, plus the report): the bill and
when each sworn term falls due; the treasury; each instrument he is party to with `kept` as his own ledger
reads it; the persons whose deeds he holds and who hold no dignity; for each resolved act of his, its
term list.

**What he chooses**, all ordinary candidates of existing verbs:

| way to meet the bill | acts | which institution it crosses into | what follows by somebody else's choice |
|---|---|---|---|
| tax a duchy | `requisition` at `distance`, against the cohort's `regard` and the `homage` the cohort knows of | the ducal house | the duke's `breaches` occasion: `petition`, withhold the relief, `release` (he is `excused`), `march` |
| borrow | `petition` the house head; `covenant` (a `debt`); later `transfer` at each stage, or not | the house | the reckoning; a lapse; the bond told, or handed on; with cut 3, a suit before a Church bench |
| farm the southern tolls | `covenant`, form `farm`, to a person he knows | the grantee and the people of Stillhelm | the farmer's levies and rent; petitions; migration; an `audit` when his hold closes |
| levy in Himmelenger | `requisition` in `terr_T9` | the Church | a churchman's `open_case`; a sentence; an `avoidance` whose addressees are his own sworn men |
| leave men unpaid | no act | his court | terms mature; the unpaid are out of his purview |
| honour instead of pay | `confer` a dignity on a creditor or a duke's man | the court | a larger bill next year |

**Seats to play, and why each is a game.** The King (the table above). The Duchess (a levy inside her
duchy is offered to her as a breach: bear it, bargain, or leave). The house head (lend or refuse, at what
amount and payable where; present the bond, extend it, hand it to someone who can use it). A Stillhelm
hearth head (pay, hide, petition, testify, leave). In cut 3, a Church bench member (open the case or not;
ballot; publish or not).

**Three cuts.**

| cut | adds | needs batches |
|---|---|---|
| 1 | tax, borrow, leave unpaid, honour | I-1 to I-4 |
| 2 | the farm and its audit; writs through the Ministries' hand | I-5, I-7 |
| 3 | the levy in Himmelenger, the sentence, the answers; a suit before a Church bench | I-6 (the Church on its ground), I-7 |

### 3. The report

One line per reading, each a fold over `w.log`, `w.tenures`, `w.records`, `Rung.stores` and, for the
person-side readings, a named person's own ledger. A line whose subject does not exist in the world is
omitted.

| line | read from | from which family reading |
|---|---|---|
| `fisc` — stores, the bill due this year, the shortfall, per paying seat | `Rung.stores`; `upkeep_owed`; termed `oblige` edges | BYZ-F |
| `sworn` — renewed, matured, live, per paying seat | `term.renewed`, `term.matured` | BYZ-F |
| `collected` — rendered, taken, partial, resisted, per place, each with its term list | `requisition.*` Events | BYZ-F; COL-E |
| `carried` — transfers between places by band and what arrived | `transfer.*` Events | COL-E |
| `dignities` — held, conferred, resisted, provisional | `tenure.opened` on dignity rows; `appointment.resisted` | BYZ-F |
| `hands` — entered, held over, returned by a clerk, returned by the clock, per body or seat; the busiest hand's share | `document.*` Events; "returned by the clock" read when read (an unentered `hand:` stage whose due has passed; BYZ-C as reconciled) | BYZ-F |
| `instruments` — per live instrument: form, parties, `dues` stamped, acts occasioned by one, `kept` as each party reads it | `dues`; `occasioned_by`; `person_q.kept` | COL-E |
| `bonds` — minted, reckoning by band, extended, lapsed, handed on; the largest share of a bench with a live edge to one person | `debt` Records; the lapse read from `world_q.owed` after the last stage's `term.matured` (VEN-B; no `debt.lapsed` kind); `record.given`; `owed_to` | VEN-D |
| `lists` — per list seat: enrolled, lapsed by term; `lot.seen`, `lot.empty`; council holders in order | `oblige` Tenures; `lot.*` | VEN-D |
| `seats` — per faction named: who holds which seat; each `confer`, `revoke`, `succeed` with its band, its `Act.via` and its term list | `tenure.*`; the contest Events | PAP-F; BYZ-F |
| `certificates` — Records carrying `recites`, by keeper; tellings of recited deeds by keeper; the mean chain term of `legitimacy` per founding seat | `w.records`; `tell` Events citing a held Record; `person_q.legitimacy` over the cast | SYN-B gate 4 |
| `sanctions` — sentences by band; writs published and their `force`; answers by band; releases by excused and unexcused men | `ban.opened`; `dispensation.issued` of form `avoidance` or `interdict`; `compliance.*`; `tenure.closed` on `oblige` | PAP-D |
| `hearings` — per arrangement row: opened, by whom, bench, proofs weighed, band | `case.opened`; `determine` Events | COL-E; PAP-F |
| `commensuration` — the roll routes used; bands seen per verb; term names seen; matter kinds moved; maturations on each of the two clocks | the Events' own records | audit §7.6 |
| `conflicts` — the readings of audit §6, each as a count and the chain that made it | the folds named there | audit §6 |

`--bands N` runs the case at seeds `0..N-1` under the shipped chooser and prints, for each drawn verb, the
frequency of each band beside the control (a task row under `task_draw_arm: off`; a contest row under the
pinned roll). It asserts nothing. No test file is added for the report (CLAUDE.md §0.1 pt 5: its subject
is the game's draws and its reader is a person deciding a tuning value).

## Gate (execution artifacts)

`PYTHONHASHSEED=0`; seeds 0 to 9; eight seasons; the shipped chooser in every seat.

1. **The bill is met in more than one way.** Across the seeds at least three of the six ways in the
   table are attempted by the King's seat-holder, and at least two different `ends` are reached.
2. **A crossing occurs.** In at least one seed-season an act by a person who is not the King is
   `occasioned_by` an Event of his: a duke's `petition` or `release`, the house's `give` of the bond, a
   hearth's `migrate`, a churchman's `open_case`.
3. **The two parties to one instrument disagree somewhere** (`15_INSTITUTIONS_COLONIAL_E` gate 2): in at
   least one seed-season the two readings of `kept` on one instrument differ.
4. **Control.** The same seeds with the realm's `seeded:` rows absent, the case's instruments absent and
   every fixture at control: no `dues` stamped, no `breaches` offered, and `content_hash` equal to the
   base realm's after the same stores delta.
5. **Planted failure.** Every roll pinned to Success: gates 1 to 3 must then give one ending and one
   chain at every seed. If they still vary, the variety came from somewhere other than the draws and the
   reading is void.
6. **One code path.** `content_hash` of each all-NPC run equals `populated.run` on the same world after
   the same tick-0 acts.
7. **Playable by a person.** At `harness/headless.py` in the King's seat, four policies (tax hard;
   borrow and pay; borrow and default; farm and neglect) reach different endings on some seed, and any
   two of them are told apart by their distribution of endings over twenty seeds each. Manual; the
   close's reading, not a test's.
8. **Entrenchment moves the world (A-80; C3-C12).** An arm in which every contest resolves at its
   control band, so every position holds (no bond is met or sued, no levy is resisted or yielded beyond
   its control band, no audit is determined). The report prints, per seed and season, the count of acts
   whose question cites an Event of the King's or an instrument of the case (a petition, a `tell`, a
   `migrate`, an `evade / defy`, a `release`). Expected reading: non-zero in every seed and rising while
   the bill stays unmet (held positions are referents others act on). The count is the story census's
   instrument (`23_STORY_D`, the entrenched-world arm); this gate reads it, it does not define it.
   Control: the same seeds with the case's instruments absent.

## Falsifier

- A scenario whose opening state the fold could not produce (a set-up act refused).
- An ending reached at the control arm with the same frequency and by the same chain as at the live arm:
  the instruments did nothing.
- A report line that cannot name the `Act.via` of a conferral or the clause of a `due`.
- The scenario needing any act the season loop cannot form.

## The standing requirement, point by point

| point | The King's Bill |
|---|---|
| a situation | a bill larger than the treasury, a year to meet it, and five other chests that are each somebody's |
| real choices | six ways to meet it, each through a different institution |
| choices change what happens | terms renew or mature; a duchy is breached or spared; a bond is met or lapses; a people are farmed or not; a sentence is risked or not |
| consequences | a duke excused of his oath; a house holding a king's paper; a farmer with more men than his grantor; an excommunicated king |
| an ending | eight Queries; a stable continuation in every case (the world runs on) |
| one code path | the season loop on the realm through `play_surface`; a case file, tick-0 acts, a reader |
| integrates | every act is the loop's own write; entered from a running season the same situation is an ordinary year |
| no GM | the bill, the bands, the occasions and the endings are Queries |

## NERS reading

- **N.** Without it the institutions are four games that never meet, and every crossing in the audit is
  prose. From above: a king's year. From below: a hearth under a farmer. Laterally: a duke and a banker
  each holding paper against the same throne. Diagonally: a parish's answer to a writ deciding a
  vassal's oath.
- **R.** Six strategies, five seats, eight endings; an all-NPC run produces the conflicts of audit §6 or
  shows that it does not. Complete at the extremes: a king who does nothing ends on `court_lapsed`; one
  who can pay ends on `court_kept`; neither crashes.
- **S.** One runner, one report, one case shape for every institutional scenario; it enters and leaves
  by the loop's own acts; SC's hearing is entered by a docket and returned from by a disposal.
- **E, last.** One case file and one report module replace two situations in Python, one fixture
  extension, three command-line flags and two reading scripts.

## Cost class

Small build (the report; the runner reading a case file); the case is an edit. Harness only.
