# STORY-B — a house continues: a marriage as an instrument, a birth by a draw, a majority, and the minority that makes a regency

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. A minority is a **standing of the era's RULE** (`rosters.yaml: era_rule_standings`: `held`, `vacant`, `minority`, `captive`; `30_WR_A_the_era_is_a_named_period.md`): a head seat held by one under `majority_age` opens an era of that standing, and it lands as a row of that file's commit 4 with this file's edit 4. A coming of age is a tick (bookkeeping) and decides nothing: it opens a **mandatory scene** for the regent and the heir (A-47), and what follows is the regent's `release` or refusal and the heir's `succeed`, each drawn; a regent who holds on is a usurpation others may answer. The house's succession is LOOP row L9 and chain K-1.

Reconciled: 2026-11-12, U5d closure — folded **A-15**, **A-51**, **A-19** and **A-44**, and reconciled the two premises this lane assumed. (1) Natural death and `majority_age` go live: A-15 orders the cast's ages authored, which is the condition edit 4's loader refusal names (`majority_age > 0` only when the cast rows carry ages), so `majority_age` ships on with the ages and is no longer a control waiting on a decision; the regency rule of edit 4 is then reachable from the first natural death. `majority_age` is in seasons and "sixteen years" needs the year's owner (`20_NARRATIVE_E` edit 1). (2) The prologue is five years, not one (A-51): minors placed by the generator age five years before play; a marriage formed in the prologue may stand at tick 0; with `birth_rate` at its control no child is born in the prologue, and A-51 orders no births or ageing pass, so births stay behind `birth_rate` 0 and remain the one question of this file for Jordan (J-1), unchanged. Edit 4's "the nearest living title" reads the set of titles of the deed race (A-19): a minor's title is one of several and a regent's provisional hold yields to the race's winner at Partial. Generated kin (A-44) are who a marriage and a house are made of.

## Status: PROPOSED (one on-switch is Jordan's: `audits/23_STORY_ENABLEMENT.md` §8.2 J-1)

Source: `audits/23_STORY_ENABLEMENT.md` §2 rows S-07 and S-05, §4.2 G2; `16_PESSIMIST_GAME.md` §6
(*"a birth, a marriage, a coming of age (no verb, no clock: persons never increase)"*);
`16_PESSIMIST_CORE.md` §6 (*"a person entering the world"*). Composes on, and does not restate:
`15_INSTITUTIONS_COLONIAL_A_instruments.md` and `15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` (the one
registry `engine/season/instruments.yaml` and its forms), `13_SC_draw_for_unrolled_contests.md` (the
`covenant` draw), `21_PROCEDURAL_B_cast_and_seats.md` (the one person generator, `age_bands`),
`21_PROCEDURAL_D_world_cards_and_churn.md` PG-7 (individuation at CENSUS), `22_HAPPENINGS_A_…` (authored
ages; the illness bout), `22_HAPPENINGS_B_…` and `14_VERBS_BINDING_C_turnover.md` (the provisional
hold), `07_SE_population_regrowth_B.md` (its reading of Layer 1 §25 and §29).
Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

At ship, nothing: `birth_rate` is 0.0 and `majority_age` is 0 (nobody is a minor), no `marriage`
instrument is seeded, and every hash is today's. With them on: two persons may be bound by a marriage,
formed by `covenant` and drawn; a co-resident couple is put to one draw a year for a child; a child is a
Person with an age who is offered no act until his majority; a hold opened while a nearer title belongs
to a minor is provisional until that minor comes of age.

## The problem, with evidence

- Persons never increase: no verb, effect or clock mints one after the build (`16_PESSIMIST_GAME.md` §6;
  `16_PESSIMIST_CORE.md` §4.3). PG-7's arrival individuates a person out of a cohort; it gives a house
  no child.
- `Person.born` is 0 for 83 of 83 (`21_PROCEDURAL_B`; `data/fixtures.py:692`, `age_at_build=0`), so no
  one is young or old and "of age" has no meaning.
- A regency exists in the suite only as the consort's claim landing at Partial (HAPP-B item 4), and
  HAPP-B states that it does not *"decide a minority"*. The provided corpus names a consort with standing
  and no action economy and a house that is *"unmarried, childless, heirless"* (`22_HAPPENINGS.md` §1.5).

## The resolution, decided

A marriage is an instrument, not a verb: COL-A's registry is the closed set of forms a `covenant` can
take, and a `kind` operand on `tie` would be a scale-local dialect (SOC2-D's own reasoning). A birth is
the bodies clock (Layer 1 §25: births and deaths at MATTER) and the Person is individuated at CENSUS
(PG-7's precedent). A majority is an age read by eligibility, which the standing rule excludes from
draws. Ladder steps 4 and 5.

## Exact edits, by owner

**1. `engine/season/instruments.yaml` — the form `marriage`** (a row in SYN-A's registry; the key names
are that file's).

```yaml
marriage:
  parties:   [Person, Person]          # each party's own act; for a party under majority_age, his guardian's
  terms:     {bearer: <one of the parties>}   # authored at formation; the party the birth draw's costs fall on
  dues:      []
  kept:      "both parties live"
  ends_on:   ["a party's death", "release by either party (a deed against the other)"]
  ties:      true                      # counts as a tie for VEN-A's `obligation` term between the parties and their houses' heads
```

Formed by `covenant` on this form (formation: SOC1-A; the draw: `13_SC`; pool the proposer's standing
and what his house offers, obstacle the other party's interest and his house head's regard). Reader:
`queries/person_q.py::spouse_of(w, p) -> Optional[str]`, a pure read of live `marriage` instruments
naming `p`. Authored marriages of the cast are seeded as instruments by the builder from a `spouse:` key
on the cast row `[content; Jordan's names]`.

**2. `engine/season/loop/matter.py` — `_births(w, token)`, on the bodies clock**, once a year (the tick
the year roster of `20_NARRATIVE_E` edit 1 marks as the year's turn), for each live `marriage` whose
parties share a `reside` object and whose `bearer` is of an age inside `fertile_ages`:

- taken at all with chance `birth_rate` (keyed draw on `(instrument id, tick)`; 0.0 ships);
- then one graded draw. Pool: `birth_pool`, plus one where the home settlement's hunger band is `fed`.
  Obstacle: `birth_ob`, plus one per `age_bands` step of the bearer above `fertile_peak`, plus one per
  body band the bearer stands below the top, plus one where the home is short.

| band | writes | emits |
|---|---|---|
| Overwhelming | two births queued | `person.born` ×2 |
| Success | one birth queued | `person.born` |
| Partial | one birth queued; the bearer falls one body band (the stake `body`, one step, `23_STORY_A`) | `person.born`, `body.changed` |
| Failure | nothing; at `shortfall_step` 3 the bearer falls one body band | — · `body.changed` |

A queued birth is a row on the instrument's `stages`, read by CENSUS. If Jordan rules that the world's
own motion draws by tables and not by the ladder (PES-SE J-2), these four rows are that table and the
same inputs are its weights.

**3. `engine/season/loop/census.py` — individuation.** For each queued birth, the one person generator
(`21_PROCEDURAL_B`'s `generate_person`) mints a Person with `born = w.tick`, `reside` at the bearer's
home, pursuits and conviction drawn between the parents' (the generator's lifepath with `parents=`), and
no capability. WITNESS deposits the birth to those present; everyone else learns by telling. The
`person.born` kind is declared on the matrix row individuation already writes `[UNVERIFIED: PG-7's
emitted kind; reuse it if one exists]`.

**4. A majority.** `data/fixtures.py`: `majority_age` (seasons; 0 = nobody is a minor, the control,
SHIPPED until HAPP-A edit 1 authors the cast's ages; proposed sixteen years).
- `decision/options.py`: a person under `majority_age` is offered no row (the declared-aperture column
  of `02_CHAR_offer_what_can_be_done.md`, value `[]`), so a child costs no deliberation.
- `loop/effects_governance.py::_eff_succeed`, `_eff_confer`: while the nearest living title in
  `rosters.yaml: successions` for a seat belongs to a person under `majority_age`, a hold opened on that
  seat by anyone else at Success or Partial is written with `_provisional_term` ending at the minor's
  majority (VB-C's one term constructor): that hold is the regency. At Overwhelming the hold is full:
  the claimant has displaced the child, and the Event is witnessed as a deed done to the minor
  (`23_STORY_A` edit 3). What the claim wins is therefore still the draw's: a regent, or a usurper.
- `loop/matter.py`: at the tick a person reaches `majority_age`, `person.came_of_age` (a clock's tick,
  bookkeeping), deposited to his household. It is an occasion for him (his own `succeed` becomes
  formable and is drawn against the regent as any claim is, VB-C) and for the regent.

## The gate (execution artifact)

The valley fixture with one seeded marriage and one minor heir who comes of age in the fifth season;
20 seeds, 8 seasons; arms `birth_rate` 0.0 and 1.0, `majority_age` 0 and on.

1. **Control.** Both at control: content hash equal to the pin; no `person.born`.
2. **Births occur and can fail to.** On: a birth at some seeds and none at others; at least three of
   the four bands' outcomes across seeds.
3. **A child is a person.** Each child has a `born`, a `reside` edge, parents who hold a claim of the
   birth, and zero acts while under age.
4. **The regency ends more than one way.** Across seeds: the heir's claim at his majority seats him at
   some, is contested at others, and at one or more the regent's hold is confirmed first by his own
   `succeed` or was full from the start (the child displaced).
5. **Census.** S-07 and S-05 pass audit §6.1's clauses C1 to C6.

Story bar test: a planted log (a `covenant` of form `marriage`, a `person.born` citing it, a
`person.came_of_age`, a `succession.claimed` by the same person) reads one S-07 and one S-05; without
the instrument Event the birth is unparented and reads no S-07.

## The falsifier

- A birth with `birth_rate` 0.0; a child offered a candidate; a hold opened over a minor's title with no
  term: each is a wiring failure of one edit.
- `majority_age` on while `age_at_build` is 0: every holder is a minor and every hold provisional. The
  loader refuses `majority_age > 0` unless the cast rows carry ages (the licensed form: a loader's
  refusal per data family).
- The same couple bearing at every seed: the draw is not keyed on the tick, or `birth_rate` is read as
  a threshold.

## NERS reading

- **N.** Cut it and a house is a fixed list that only shortens; a regency has no child at its centre;
  alliances cannot be sealed by a match. Holds top-down (dynasties), laterally (the instrument registry
  gains one form and no verb), vertically (a household is the scale below a faction). Bottom-up it is
  weak inside a short campaign, where a newborn does nothing: the minority and the match carry it there.
- **R.** With no player, houses join, grow and fail. Customisation: a player chooses a match. Complete
  at the extremes: a realm with no marriages draws nothing; a bearer at body zero is not drawn for.
- **S.** One clock (bodies), one generator, one term constructor, one registry. It pauses nothing and
  adds no scale.
- **E, last.** One form, one pass on an existing clock, one call to an existing generator, one fixture
  and one cap, against three stories and the supply of every later succession. Middling to high; lower
  if campaigns stay short.

## Cost class

Small build. Edit 1 is a data row once I-1 lands. Edits 2 and 3 are design-first on J-1.

## Dependency edges

Needs first: SYN's batch I-1 (the registry); `13_SC_draw_for_unrolled_contests.md`; HAPP-A edit 1
(ages) and its bout; `20_NARRATIVE_E` edit 1 (the year); `21_PROCEDURAL_B` (the generator); VB-C
(`_provisional_term`); `23_STORY_A` (the stake step). Feeds: HAPP-B (a minor among the titles); VEN-A
(a marriage as a tie); `23_STORY_E`. Batch E-5 of the audit.
