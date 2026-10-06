# What else the game needs — outside forcing, its transmission to decisions, bounded escalation, and a story bar

## Status: RATIFIED AS INTENT (v9, ED-IN-0287) for the §4 handles whose class is not held; FORCE-BODIES, FORCE-FOREIGN, END-VICTORY and CAST-DISPOSITION's capability writer ratified as the plan's recommendation (RS-21) [medium; Jordan to correct]; CAST-POPULACE NOT ratified (its spread construal is held); §5 cuts stand; §6 superseded by v9's order; §7 item 1 answered [medium] (the Calamity is tensile, D-3), item 3 answered (a dated pin is a clock, T-c), item 5 is IN-06. Reference under `CLAUDE.md` §0.05.

> **SCOPE, STATED LOUDLY.** This document is **reference and a proposal** (CLAUDE.md §0.05): it
> resolves nothing at runtime, and if it were deleted the game would behave identically. It creates
> **no plan position**, allocates **no ID** and writes **no ledger row**. The one plan
> (`workplans/valoria_master_workplan_v8.md`) owns order; nothing here is scheduled. **Merging the PR
> that carries it does NOT ratify any item, cut, ordering or decision in §4–§7**, notwithstanding the
> merge-ratifies default (ED-1094): each is **held back** until it is built in code, at its owner, with a
> test that executes it. Every grade proposed here is `assumption` or `absent`; none is `ruled`.

- **Date:** 2026-10-04. **Lane:** IN (cross-cutting).
- **Authorship:** Claude, from a session that read Layer 1 (`architecture/meta/`), the master plan, the
  verb-gap proposal (#453/#455), the season loop's code paths named below, and ran the two scratch
  measurements of §8.
- **A handle** (`FORCE-WEATHER`, …) is a label for an item in this document. It is not a plan position
  and not an ID.
- **Forcing**, as this document uses the word: an input that changes the world's state in a tick
  without any person's decision in that tick and without any person having set it. Weather is one;
  an invading army is not (it is persons deciding).

---

## 1. Purpose, method and limits

**Purpose.** Jordan's nine intended drivers — drought and rainstorms with food security as a historical
driver of stability; an ongoing threat of invasion by an external empire; the Church ratcheting toward
seizing lands and theocracy; a monarch and two dukes vying with ever-rising stakes; Einhir heritage and
threadwork persecuted as heresy; the Calamity expanding if unmanaged; ambition, greed and conflict within
and between factions; Schoenland's external trade demands; royal succession crises — were put against
the engine as it is and as its documents say it should be. This document lists what the gap between
those leaves to plan and build.

**Method.** A NERS pass (`skills/ners/SKILL.md`, definitions at CLAUDE.md §0.06) on a hypothetical
completed engine: all nine requirements (`engine/season/requirements.yaml`) met, the 55-verb suite of
#453/#455 built with its readers, and no stubs. Each proposed item carries an **N-line** (what the game
can no longer do if it is cut) and a **false-N-line check** (does something already ruled in provide it),
because the pass's product is the cuts that turn out to be free (§5).

**Yardstick.** Jordan's terminal criteria, `references/design_rulings_2026-09-06.md` R2: *"making this as
dynamic and capable and flexible and emergent and persistent as possible."* R4 of the same file already
rules that *"the world must churn"* and that *"pressure that changes nobody's decision is scenery."*

**Limits.** §9 lists what was not read. The measurements are two seeds over at most three seasons; nothing
here speaks to season 30 against season 40.

---

## 2. The diagnosis

1. **The engine is persons-only agents on a passive substrate.** The world moves by AX-5's three
   motions (`architecture/meta/01_AXIOMS.md:164-196`) and each is a deterministic function of state:
   yield (`engine/season/loop/matter.py:489-490`), wear (`:553-587`), claim decay (`:235-265`).
2. **A system with no outside forcing and mostly damping loops converges.** ID-16
   (`architecture/meta/01_AXIOMS.md:616-702`) says so of this design, and `architecture/meta/07_DYNAMICS.md` §4 (`:95-123`) records that
   nothing bounds season-to-season feedback. The register declares four loops: two amplifying, both
   informational (H-102, H-112), and two damping (H-103, H-104).
3. **The nine intents are forcing plus escalation.** Four have an outside source (weather, empire,
   Calamity, Schoenland), one has an outside trigger (succession, through ageing), four are internal
   conditions (§3).
4. **`engine/season/` instantiates almost none of the outside sources.** No code or roster outside the case
   corpus names drought, rainstorm, calamity or empire; `invasion` appears in one prose line of
   `npcs.yaml`; `season_factor` is the constant 1.0 (`data/fixtures.py:399`); Schoenland has no rung by
   design (`harness/populated.py:532-541`); no harness path passes the actorless-event channel to
   `season()` except a probe (`harness/probes.py:1786`).
5. **The plan schedules one forcing item** — hunger, `24g` (gate J-6) — and none for weather, the Calamity,
   ageing or a foreign cast. THE NINE (R-01…R-09) test none of them, and **M2 has no instrument**
   (`master_workplan_v8.md:215-227`).
6. **Transmission is the weaker link.** Forcing matters only if it reaches decisions, and the links are
   off or cut: hunger is inert (`body_step=0`, `fixtures.py:520`; named persons are exempt from the larder
   draw, `matter.py:296-304`); a shortfall reaches only those standing at or holding the larder (H-160);
   stance has two writers, a seeded loyalty and the `march` outcome (H-62).

---

## 3. The nine intents, classed

| # | Class | Lawful carrier under Layer 1 | In `engine/season/` | Plan v8 | Left unplanned |
|---|---|---|---|---|---|
| 1 Weather, food | outside, non-agentive | matter motion | constant factor; chain to a shortfall claim runs | `24g` hunger only | the draw, a season-of-year, reach to governors |
| 2 Empire | outside, agentive | foreign persons | none | none | foreign cast, border, perception |
| 3 Church to theocracy | inside | accumulated seat and remit acts, creed commitment | creed gives members a standing question; `confer` and `establish` do not execute | #453 suite | bounded escalation loops |
| 4 Monarch and dukes | inside | `march`, `determine`, `seize`, grudge loop | leaders are persons; `march` executes | suite, G2 | stakes gain fixture |
| 5 Heresy | inside, couples to 6 | charge, `arrest`, `determine`, `ban`, `destroy_record` | one OUGHT proposition | suite; `proclaim` deferred | threadwork carrier |
| 6 Calamity | outside or consequence of acts (§4 `FORCE-HAZARD`) | matter motion plus thread operations | none | `33` (paper, Jordan-gated) | the law, re-expressed |
| 7 Ambition, greed | inside | pursuits, Q4, stance, `oblige` | the best-represented class | R-06, J-1 | disposition spread |
| 8 Schoenland | outside, agentive | foreign persons | no leader, template or rung | `covenant`; readers deferred | foreign cast |
| 9 Succession | trigger outside, crisis inside | bodies motion; `inheritance` basis | `succeed` thin; no ageing | R-5 unratified; `24g` P3 | ageing, illness |

---

## 4. What else needs planning and building

### 4.1 Outside forcing

**`FORCE-WEATHER` — a keyed seasonal draw on the yield term.**
- *Carrier:* AX-5 motion 1. R4 of the rulings file already names generative matter as arguably inside it.
- *Builds:* the draw at the existing yield step (`matter.py:489-490`); a season-of-year read off `tick`
  (no new field); H-26's distribution (constant 1.0 today, swept 0.5 / 1 / 2).
- *N-line:* cut it and food security cannot be an outside driver; yield varies only with site condition,
  which moved 998 → 996 over two seasons (§8).
- *Reader:* yield → stores → `world_q.subsistence_draw` → the shortfall observation
  (`matter.py:381-403`).
- *Control and falsifier:* `season_factor` held at 1.0 reproduces today's hash; with the draw on, a drought
  season leaves stores below the control arm's and a drained larder emits a `shortfall:` observation; the
  same seed twice gives one hash.
- *Not built:* a weather module. A host function in the yield step provides the same result (§5).
- *Gate:* the distribution's values are Jordan's parameters.

**`FORCE-BODIES` — ageing and illness through the bodies motion.**
- *Carrier:* AX-5 motion 2. Only hunger writes `Person.body` today (`matter.py:405-453`) and it is off.
  `24g` covers the hunger arm and demand-driven individuation. Ageing and illness appear only in proposal 5 of the
  unratified `proposals/2026-09-12-emergent-narrative-primitives-v2/`.
- *Builds:* one field (a birth tick) with the hazard as its reader (ID-13); one bodies write at MATTER
  emitting `person.died`, chained to its own prior emission.
- *N-line, narrowed:* cut it and natural vacancy and finite tenure vanish. Succession crises survive,
  through violence.
- *Control and falsifier:* an age step of 0 reproduces today; a seat-holder's death by age raises vacancy
  claims for those in reach.
- *Gate:* whether J-6 covers ageing and illness; the rates.

**`FORCE-HAZARD` — the Calamity, re-expressed.**
- *Source of the law:* the Mending Stability scalar (0–100, start 60, −1 per year;
  `systems/overview/sim/ms_track.py`), unplugged because it writes `world.clocks`, which the season
  `World` lacks (plan `33`). Distance effects from Askeheim (T15) are in `calamity_radiation_v30.md`
  (quarantined; intent only).
- *Why re-express:* a stored 0–100 scalar and a yearly decay are an aggregate and an unwound clock
  (T-a, T-c).
- *Builds:* one coupling rule in the existing wear loop for the lattice sites, on existing site kinds if the
  band table can key on territory; Mending as persons' acts (the `restore` arm); the effect per territory
  as a Query over band floors; a `+` LOOP row bounded by Mending. Band crossings already emit and are
  witnessed (`matter.py:36-82`).
- *N-line:* cut it and the Calamity "expands if unmanaged" only as a script. The only new content is the
  coupling rule; the stored scalar is a free cut.
- *Needs:* thread operations as a carrier, so strain can be an act's consequence (H-85, plan `33`).
- *Timescale:* at −1 per year from 60, an unmanaged scalar needs about 240 ticks to reach Rupture
  [inference]. It matters within a campaign only if thread operations accelerate it.
- *Control and falsifier:* unmanaged arm — lattice condition falls and band crossings reach territories in
  order of distance; managed arm stabilizes; coupling weight 0 reproduces today.
- *Gate:* a ruling — matter motion, or a consequence of acts (canon P-07, `canon/02_canon_constraints.md:49`)
  — and the baseline's sign, which the code and the trajectory document give differently for different
  periods [UNVERIFIED that they reconcile].

**`FORCE-FOREIGN` — an external empire and Schoenland as persons.**
- *Carrier:* AX-1. A foreign actor is a person using the same verbs.
- *Builds:* a foreign roster (data); foreign rungs and a border (T16 is omitted by design today); seats,
  pursuits and ledgers; crossing as travel legs; perception channels at the border.
- *N-line:* cut it and invasion and trade demands are scheduled occasions — a clock (T-c) that cannot
  respond to the realm's perceived weakness.
- *Control and falsifier:* with the cast on, a foreign `march` reaches the mass-battle seam against a
  realm settlement through the real chooser, with no hand-built act; off, byte-identical to today.
- *Gate:* identity, convictions and leaders are Jordan's content. Canon gives Schoenland and the Guilds no
  leader or template (`engine/season/rosters.yaml`, faction notes).
- *Not built:* a scheduled arrival.

### 4.2 Transmission, escalation, cast, seams

| handle | what | N-line (what dies) | falsifier or control | gate |
|---|---|---|---|---|
| `CARRY-INTERIOR` | stance and conviction writers from outcomes (H-62; telling workplan G1, G2 in `workplans/2026-10-01-telling-workplan.md`; cells commit J-1) | forcing changes options but not dispositions: no legitimacy, no feud | after a lost field or famine, stance rows change for witnesses, not only participants; weight 0 is the control | J-1 |
| `CARRY-SHORTFALL` | shortfalls reach governors by reach and purview (H-160); the hunger arm live (`24g`) | scarcity never becomes a political fact | a governor's `questions_for` holds the claim and a candidate forms in `harness/scarce.py`'s world | J-6 value |
| `CARRY-STABILITY` | legitimacy and stability as Queries over stance and claims, no stored value (ruling R7) | "food security drives stability" has no object | the Query's reader is a person's own windowed estimate (§C.11), plus the instrument of `STORY-BAR` | none |
| `BOUND-LOOPS` | a signed LOOP row with a bound for every new amplifier; build H-106's derived check, which no plan position schedules | an amplifier added with no way to say whether it converges or runs away (events once went 207 → 896 → 3,389, `architecture/meta/07_DYNAMICS.md:179-186`) | the derived cycle set equals the declared set on the shipped tree | none |
| `BOUND-STAKES` | a gain fixture for `score`'s stance term (it has none); the grudge closer `forgive`; G2 | the dukes' and Church's "ever-rising stakes" have no tunable rate | sweep at 0 / 1 / 3 beside the field weights (`fixtures.py:565-566`) | values: Jordan |
| `BOUND-ATTENTION` | resolve the hold-to-budget ceiling: an office-holder's sixth scene is unspendable (`loop/deliberate.py:84-111`; H-92) | power cannot buy attention, so seats do not compound | one live `hold` moves releasable scenes 5 → 6; control is today | answered by S26.3 (budget varies by office); needs H-92's records-mint-budget repair first |
| `BOUND-PAPER` | a sink or reader for Records and Propositions (`Record.ttl` has none; `destroy_record` was never attempted) | paper accumulates linearly, 79 → 240 records in three seasons (§8) | records per season flatten under the sink arm | ID-14 (open implies close) |
| `STORY-BAR` | the M2 instrument: cross-person antecedent share and chain-depth distribution per season, N seeds, forcing on against off | no way to know whether the engine produces stories at all | baseline 9.3% and depth ≤5 (§8) | none |
| `STORY-READ` | an observer outside the simulation that finds arcs in the cause graph (proposal 1 of that same set, the chronicle render) | stories exist and nobody can find one; Layer 1 forbids salience ranking inside the sim | a render of one seed's chain that a reader can follow | proposal 1's own objection (form unproven) |
| `STORY-SOAK` | a long-horizon run: ledgers reach the 200-claim cap, eviction is already active in season 2, and per-season cost rose from 13 s to 169 s | ID-16's "season 40 resembles season 30" is untested | `harness/soak.py` exists and grades nothing; add flat cost per season and non-convergence of the act mix | none |
| `CAST-POPULACE` | a cohort's internal spread (F.19; proposal 13 of that same set) and pursuits for the 37 cohorts | riots, flight and conversion are single decisions; cohort seats throw no hooks | a cohort splits on one claim | Jordan (construal) |
| `CAST-DISPOSITION` | alignment cells for `tell`, `give`, `speak`, `march` and the new verbs; the convictions' correlation (ED-IN-0214, Jordan's); a capability writer (`train`); combat parties beyond `end` (`seam/wrappers/combat.py:108-120`) | outcomes vary by position and information, not by person | distinct executed sets (existing instrument), and a contest roll that varies by person | ED-IN-0214 |
| `SEAM-LADDER` | one degree ladder: mass battle returns a margin, or its field bands are a declared narrowing extension (`architecture/meta/03_VERBS_AND_LOOPS.md:286`; `engine/season/seam/wrappers/mass_battle.py` docstring) | two ladders for one quantity (§0.06 S) | `degree_of` has no third branch | none |
| `SEAM-CLOCK` | one unit, the season: yearly rates (the scalar's −1 per year, upkeep) become per-season rates | calculations inconsistent in methodology across the new producers | one conversion, one owner | none |
| `END-VICTORY` | an ending and victory vocabulary (GD-1; H-176; `ENDINGS_CLASSIFIED.yaml`); thresholds re-expressed as persons' choices (T-b) | no terminal for the ratchets | an ending reached by choices only | Jordan |

---

## 5. Cuts — what not to build

Each is a false N-line: something already ruled in provides what it would add, or Layer 1 refuses it.

- **The stored MS scalar and any stored stability value** (GD-1's "Political Stability"). Site conditions and
  stance rows are the carrier; a Query reads them (T-a).
- **A scripted invasion or other dated pin as a default.** A clock (T-c). Foreign persons provide the threat.
- **Hazard-rate thresholds that produce an outcome** (T-b). A crossing may change options, never act.
- **A weather module wrapper.** The host function provides it.
- **A "lattice-node" site kind**, unless the band table cannot key on territory.
- **`proclaim`, `steal`, `execute`** stay as #455 left them: deferred or refused.
- **An arc, story or thread carrier inside the simulation** (ED-IN-0225).

---

## 6. Order the dependencies suggest (not a schedule)

1. **Measure first:** `STORY-BAR` with a forcing-off arm. Every later item then has a control.
2. **The shortest chain on existing carriers:** `FORCE-WEATHER`, `CARRY-SHORTFALL`, `24g`.
3. **Disposition and bounds:** `CARRY-INTERIOR`, `BOUND-LOOPS`, `BOUND-STAKES`.
4. **Bodies** (`FORCE-BODIES`, after J-6), then **foreign cast** (`FORCE-FOREIGN`, after Jordan's content).
5. **The Calamity** (`FORCE-HAZARD`), after the threadwork re-plug and its ruling.
6. **Cast, seams, ending** in parallel with 3–5; `STORY-SOAK` throughout.

---

## 7. Decisions only Jordan can make

Each survived CLAUDE.md §0's five tests (superseded, irrelevant, answered by a design document, by
precedent, by architecture).

1. **The Calamity's class:** a matter motion, or a consequence of thread operations (canon P-07); and its
   baseline sign. Two defensible options give materially different games.
2. **Ageing and illness in J-6's scope.**
3. **May the scenario pin dates** (an authored occasion, a clock) for historical events? Recommendation: no
   default; use the foreign cast and fixtures.
4. **Foreign cast content,** including T16.
5. **The threadwork re-plug** (A-24), already Jordan's.
6. **The ending vocabulary** (GD-1; H-176).

Answered elsewhere, so not escalated: `BOUND-ATTENTION` (S26.3 says budget varies by office),
`BOUND-PAPER` (ID-14), `SEAM-LADDER` (`architecture/meta/03_VERBS_AND_LOOPS.md:286`).

---

## 8. Evidence

Every figure is `[SCRATCH, NOT COMMITTED]`: descriptive baselines from a throwaway script over
`populated.build_realm(seed)` driven by `SeasonDriver.season` with
`make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(...))` and
`subsistence=probes.SUBSIST`, tree `d686eb8`. They are baselines, not results: no control arm exists until
the `FORCE-*` items do. Committed instruments: `python -m engine.season.harness.aperture 1 0`
(`resolvable_verbs()`: 34 of 44) and `python tools/m1_acceptance.py --summary` (NOT MET, nine
requirements 2/9).

| measure | reading |
|---|---|
| acts per season, 83 persons | seed 0: 692, 707; seed 1: 649, 674, 734 |
| acts ending in the row's refusal kind (two seasons, seed 0) | 935 of 1,425 attributable (66%); 26 of the 1,425 never entered `resolved` |
| verbs with a non-refusal outcome | 22 of 44; ten attempted and never succeeded (`build commit confer establish found give levy migrate revoke work`); twelve never attempted |
| events, two seasons, seed 0 | 26,296; 23,950 (91%) are `claim.deposited` or `claim.decayed` |
| antecedent of an act, cumulative to season 2 | none 979 (69%); own act only 218 (15%); another person's act 132 (9.3%); a world event 96 (6.7%) |
| cross-person chain depth, season 2 cumulative | {1: 1,293; 2: 95; 3: 27; 4: 9; 5: 1}; the maximum was 5 in season 1 |
| stores total | seed 0: 4,810 → 9,268; seed 1: → 13,708 (no sink) |
| records and propositions | seed 0: 79 → 159 and 112 → 171; seed 1: records → 240 |
| mean site condition | 998 → 996 |
| claims held after two seasons | 11,490, after 15,927 deposits (4,437 evicted at the 200-claim cap) |
| deaths | seed 0: 0; seed 1: 2, 1, 0 |
| season wall time | 13 s, then 79–115 s, then 169 s (two to three concurrent processes on four cores) |

Recipe for the antecedent rows: for each Event in `w.log`, take `driver.act_of[e.id]` as its act; an act's
antecedent acts are `act_of[c]` for each cause `c` of its Events; classify by whether the antecedent's actor
differs.

---

## 9. What was not verified

- **Not read:** `calamity_radiation_v30.md` beyond its header; `canon/03_canonical_timeline.md`; the
  event-deck proposal beyond its header; the bodies of `effects_economy.py` and `effects_migration.py`;
  most of `effects_governance.py` and `effects_information.py`; `01_AXIOMS.md` beyond AX-1…7 and
  ID-16…18; `04_CODE_ARCHITECTURE.md` outside §C.11, Part D and Part F.
- **Not run:** `resolution-diagnostic` (no draw was stressed); any run longer than three seasons; any
  run with a forcing item on.
- **Inference, not measurement:** the Calamity's 240-tick horizon; that completion raises the cross-person
  share; that the cohorts' missing pursuits make them dead seats.
- **Dated figures** in §3 (`confer` 70/0, `establish` 19/0, `march` 16/16) are `requirements.yaml` R-04's
  readings of an earlier tree, not re-measured here.
