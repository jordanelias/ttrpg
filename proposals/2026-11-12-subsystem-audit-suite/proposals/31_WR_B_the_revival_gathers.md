# WR-31-B — the Revival gathers: a stand moves by a draw when a man takes in what one of a creed has done, so a cause can rise, stall or collapse

## Status: PROPOSED (the form is decided; its four numbers are `[ASSUMPTION]` and set at calibration; nothing here was built)

Source: Jordan, 2026-11-12, **A-89**: *"varfell neutral leaning Einhir with momentum building for Einhir Revival"*; A-24 (a conviction moves by a draw), A-83 (the unsaid pressure of one's own), A-80, A-81, A-88, A-90. `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` F-31-07, F-31-08. Reference only (`CLAUDE.md` §0.05). Lane WR with CHAR; owner files `engine/season/loop/witness.py`, `queries/person_q.py`, `data/fixtures.py`, `harness/populated.py`.

Composes on, and restates none of: `31_WR_A` (the rows, the cores, `opinion_links`, a faction's `creed:` signs, `closeness`, `core_standing`), `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (the emitter and Event kind `conviction.moved`), `30_WR_G` commit 5 (`world_q.circle_of`), `20_NARRATIVE_D` (the public `creed:` row), `02_CHAR_resolve_and_temper.md`, `30_WR_D` (LOOP rows), CR-107 (cohort convictions).

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | `person_q.sway_odds` and the sway draw at the claim deposit in `loop/witness.py`, behind `Fixtures sway_gain` | EQUAL at 0 (control, shipped first); above 0 a **declared mover** for every person who takes in a deed by a member of a faction with a `creed:` row |
| 2 | cohorts take their holder's regime core at build, each half settled by a keyed draw, behind `Fixtures cohort_convictions` | EQUAL at `False`; `True` a **declared build-hash mover** |
| 3 | LOOP row **L17 the cause gathers** in `hole_register.yaml`; `storybar --regimes` prints each core's gap and its word | EQUAL |

No counter, no clock, no trigger. No house, movement or person is named in code.

## The problem, with evidence

- A-89 asks for a trend, and nothing in the engine moves a stand except the crisis, which is a fixed function of the build (`16_PESSIMIST_CHAR_A` §1: the same six persons at every seed). In this lane's two-season run at seed 1 with the cast's new values, five persons were rewritten by it, each to `einhir_restoration` or `solmund_orthodoxy` at 3 to 5 from a value of 1 or 2 (P-31-8): the only "drift" the shipped engine has runs against the persons' own stands.
- The five principals of Varfell already stand at 4 or 5 on the tradition pole (`references/npc_registry.yaml`, their own rows). They cannot be the ones gathering. The house's leaners are its populace, and a cohort holds no conviction at all (`engine/season/cohorts.yaml:106-107`: "a cohort gets NO goals and NO convictions"; CR-107 held).
- Persons learn of each other's deeds constantly and of each other's opinions never: 1,529 resolved acts in two seasons at seed 0 against nine tellings between cast members (P-31-7). A mechanism that waits for a man to be told another's creed will not run; one that reads what he makes of what he sees will.

## The resolution, decided

**A man's stand on a question leans, by a draw, toward the creed of those whose deeds he approves and away from the creed of those whose deeds he resents.** One rule, for every person, creed and pole.

1. **The occasion** is a claim of a deed landing in his ledger (seen or told), where the doer is another person whose faction carries a `creed:` row (`31_WR_A` commit 4). No clock: no deed taken in, no draw.
2. **What he reads** is his own: his regard for the doer once this deed is judged (`person_q.regard`, his ledger and weights), and his own stands. The doer's side and that side's public creed are handed down resolver-side as two values, as `world_q.opinion_of` hands down `regarded` (`world_q.py:3055-3062`); he never reads the doer's convictions.
3. **Which pole** is drawn among the creed's poles, weighted by his room to move on each.
4. **The draw** is the one sampler's four-band ladder (A-5). **Pool**: `sway_pool` dice, plus dice for how strongly he regards the doer, plus one if the doer is of his circle (`circle_of`: the pressure of his own, A-83), plus or minus the links (`opinion_links`: a step the link favours gains dice, a step against it loses them). **Obstacle**: how firmly he already stands on that pole, plus his temper. So a lukewarm man near a vanguard he admires moves readily; a firm man is hard to move; a man who rejects the caste is hard to win for the royal order that carries it (A-87's "due to caste", as odds).
5. **The bands.** Overwhelming: one step toward the creed's sign (away, if he resents the doer), and it shows: `conviction.moved` reaches those present. Success: one step, known to himself. Partial: no step. Failure: if he already stood against that creed's sign he **hardens** one step further against it; otherwise nothing. Values stay in 0 to 5.
6. **Seeded at the start state, not scripted.** Varfell's momentum is the configuration `31_WR_A` authors plus commit 2: a vanguard at the ceiling, a populace seeded at the core (leaning), a public creed, and little of the Church nearby (`canon/03_canonical_timeline.md:100`: "lower Church penetration"). Whether it builds is then what happens: a lord's deed the valley approves pulls it on; a levy or a lost field it resents pushes it back; an inquisitor's arrest seen by people who resent him moves them **away from the Church's signs**, which is toward the Einhir on both poles (A-88, A-90), unless they are devout, in which case it confirms them. The same rule runs in Hafenmark toward its own creed and in the Church's flock toward orthodoxy.
7. **The prologue** (A-51, five simulated years) runs with the same fixture, so a realm can start with the trend already in its ledgers.

**Entrenchment and stillness (A-80, A-81).** A held stand is the obstacle, and it produces: the Failure band's hardening (an attempt on the firm makes them firmer, so a counter-core grows as a cause grows), the visible convert (a deed others judge), and the man pulled apart by a link, whose next step either way is a story. The draw rides a deposit that has already written a claim, so no occasion is still.

## Instructions to code

Tier: commit 1 third tier (opus) for the placement and the pool's composition, with a second-tier critic; commits 2 and 3 second tier.

**Commit 1 (control EQUAL; above 0 a declared mover).**
1. `engine/season/data/fixtures.py`: `sway_gain=0.0` (the switch and the regard scale: dice per unit of `|regard| / STANCE_MAX`; swept `0` control, SHIPPED / `2` / `4`), `sway_pool=2` (swept `1 / 2 / 3`), `sway_hold=2.0` (obstacle per unit of `|conviction_stand|`; swept `1 / 2 / 3`), `sway_link=1` (dice per unit of link lean; swept `0` control / `1`). Four NUMBER rows in `hole_register.yaml`, each `[ASSUMPTION; medium; Jordan to correct; revert: sway_gain 0]`. The obstacle's base and the temper term come from the one obstacle composer (`02_CHAR_resolve_and_temper.md`), not from a number here.
2. `engine/season/queries/person_q.py`, beside `link_fit`:

```python
def sway_odds(p: Person, creed: dict, toward: int, in_circle: bool, regard_unit: float, fx) -> tuple:
    """((pole, direction, pool, obstacle), ...) for every pole of `creed` ({affiliation: -1 | 1}, a faction's
    public row) on which `p` has room to move one step in `direction = toward * creed[pole]`.
    pool = sway_pool + round(sway_gain * abs(regard_unit)) + (1 if in_circle else 0)
           + round(sway_link * sum(sign * conviction_stand(p, frm) * direction for (frm, to, sign) in OPINION_LINKS if to == pole))
    obstacle = the composer's base + sway_hold * abs(conviction_stand(p, pole)) + his temper term.
    `toward` is +1 when `regard_unit` > 0, -1 when below, and () when it is 0. Reads `p` only (AX-2)."""
```

3. `engine/season/loop/witness.py`, in the deposit path that already calls `_credit` (`:240-262`), after the claim is in the hearer's ledger: when `fx.get("sway_gain")` is not 0, the claim records a deed (`data/verbs.py::DEED_KINDS`, `:1492`), and `world_q.faction_of(w, doer)` has a `FACTION_CREED` row: compute `regard_unit = regard(hearer, doer) / STANCE_MAX` and `in_circle = doer in circle_of(w, hearer)`; ask `sway_odds`; pick one row by a keyed weighted draw (weight: his room on that pole); roll the row's pool against its obstacle with the season's keyed sampler under the key `("sway", tick, round, hearer, claim.id)` (A-30: one draw per key); apply the band of §5 through `conviction_map` (the one validator); on Overwhelming or Success emit `conviction.moved` with `{pole, before, after, on_account_of: claim.id}` (the Event kind `16_PESSIMIST_CHAR_A` declares; Success carries `visibility: own`). One sway draw per deposit; a cohort hearer draws as any person.
4. `engine/season/write_matrix.yaml`: `Person.conviction` gains the WITNESS writer beside RESOLVE's crisis; `verb_table.yaml` is untouched (no verb).
5. Tests, `engine/season/tests/test_sway.py` (new): `test_sway_gain_zero_is_byte_identical`; `test_no_deed_taken_in_no_draw` (a person whose ledger gains nothing in a season has the conviction he began with); `test_a_firm_stand_meets_a_higher_obstacle_than_a_lukewarm_one`; `test_a_resented_doer_moves_him_away_from_that_side_s_signs`; `test_a_link_against_the_step_lowers_its_pool` (a person at `caste_order` 0 offered a step toward `royal_order`); `test_failure_hardens_only_one_who_already_stood_against`; `test_the_step_stays_on_the_scale`; `test_the_draw_is_keyed` (same seed, same step; a different seed over 20 planted deposits does not give the same 20 bands); `test_sway_reads_no_doer_conviction` (the function's arguments hold no other `Person`). `assert checked >= 8`.

**Commit 2 (control EQUAL; `True` a declared build-hash mover).** `engine/season/data/fixtures.py`: `cohort_convictions=False`. `engine/season/harness/populated.py::seat_cohorts` (`:441`): when on, a cohort whose residence lies in a territory held by a faction with a `REGIME_CORES` row takes that row's `stands`; a whole value is taken as it is, a half is settled up or down by the keyed draw `("cohort_stand", seed, cohort id, affiliation)` (A-50: bounded start state); a faction with no row leaves the cohort's `conviction` `{}` as today. `cohorts.yaml:106-107`'s comment is updated to name the fixture. `[ASSUMPTION; medium; Jordan to correct; revert: False]`: that a populace starts at its holder's core is this lane's reading of "the house"; canon's gradient (`canon/03:100`, stigma and sensitivity rising toward the Southernmost) is not authored per territory here and is CR-107's content. Tests, in `engine/season/tests/test_territorial_subsistence.py` (the file that covers `seat_cohorts`, by `grep -rl seat_cohorts engine/season/tests`): `test_a_cohort_under_a_house_with_a_core_starts_within_half_a_step_of_it`, `test_cohort_convictions_off_is_byte_identical`.

**Commit 3 (EQUAL).** `hole_register.yaml`, LOOP row **L17 the cause gathers**: "a deed by one of a creed, approved → a stand steps toward the creed → he is nearer its core, credits its tellers and judges its deeds more kindly → more of its deeds approved"; sign `+`; bounds: the obstacle rises with the stand, the scale's ends, the Failure band's hardening of opponents (sign `−` for the cause, `+` for its counter-core), resented deeds reverse it, credit halves across a fault line, `scene_budget`; switch `sway_gain` 0. `harness/storybar.py --regimes`: per core row, `gap` per axis against the authored row and against the last season's, and the derived word `rising`, `stalled` or `falling` (bookkeeping over two snapshots, as `30_WR_B`'s `formed` and `ended`).

## The gate (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 6 --arms sway_off sway_on --regimes --stories
python -m pytest engine/season/tests/test_sway.py engine/season/tests/test_territorial_subsistence.py -q   # at the close, once
```

Expected, the on arm against `sway_off`, with `cohort_convictions` on in both:

1. `sway_off` reproduces the pre-commit pins.
2. Steps per person-season are above 0 and below 1 at the median seed, and the set of persons who moved is not the same at every seed. The calibration target for the four numbers is a house's live core moving by no more than one step on any axis in four seasons at the median seed `[ASSUMPTION; Jordan to correct]`.
3. Varfell's gap on the two Einhir poles is `rising` at some seeds and `stalled` or `falling` at others over five seeds: all three words need not occur, one word at every seed fails.
4. The Church's core does not shrink in the seeds where the Revival's grows by more than the off arm's seed spread: the counter-core holds (the Failure band).
5. Entrenched-world arm (`sway_hold` at its highest swept value): stands barely move, and executed acts per person-season and the story census's rate (`23_STORY_D`) are not below the off arm's by more than its seed spread (A-80).
6. The no-null-scene reading is unchanged between arms (A-81).

## The falsifier, and its control

- The same persons stepping the same way at every seed: the draw is not keyed or the pool swamps the obstacle; it is a script.
- Varfell `rising` at five seeds of five with identical gaps: the trend is built in; lower `sway_gain`.
- No step anywhere at `sway_gain` 4: the occasion is not reached (no deed by a creed-bearing faction's member is deposited), and the row is recorded `inert`; the gain is not raised to pass.
- A step with no claim landing that round: it read the World or a clock.
- A person at `caste_order` 0 stepping toward `royal_order` as often as one at 4, over 200 planted draws: the link term is not in the pool.
- Controls: `sway_gain` 0; `sway_link` 0 (the link off, the drift on); `cohort_convictions` False.

## Dependencies

`31_WR_A` commits 1 to 4. `16_PESSIMIST_CHAR_A` (the Event kind; the fixed crisis must be drawn first, or it overwrites what sway moves). `30_WR_G` commit 5 item 4 (`circle_of`); lands without it with `in_circle` False. `02_CHAR_resolve_and_temper.md` for the temper term; lands without it on the base. Feeds `30_WR_D` (L17), `30_WR_E` (a shape: a cause that gathers and its counter), `30_GO_F`, `31_WR_C`.

## Layer 1

AX-2 and AX-7: `sway_odds` takes the person and three handed-down values; the doer's interior is never read. `ED-IN-0352` (3) (no flow touches an obstacle, pool or draw): the pool reads his regard for one doer and his own stands; no strand, era, count or core is read. `ED-IN-0225` (nothing fires): the occasion is a deposit, the result a band. `holonic` §29 (no clock at census): none. The standing rule (a draw): four bands, keyed. Named at the site because two readers could differ on whether WITNESS may write `Person.conviction`: it already writes the ledger and the credit, and `write_matrix.yaml` is edited to say so; **MECHANICAL** (the matrix test). Scripting drift: none; **STRUCTURAL** (no id in the function's inputs).

## NERS reading

- **N.** Without it A-89's momentum is a start value that never moves, and a regime changes only by the crisis. Holds bottom-up (one valley man and the lord he sees), top-down (a cause that gathers across a house), laterally (the same regard that ranks his acts moves his stand), diagonally (the Church's arrest feeding what it suppresses). Narrowed: it is inert until deeds by creed-bearing sides are deposited, which the gate reads.
- **R.** A revival that can fail; a counter-reformation that grows with it; a convert seen converting; all with no player. A player's deed in front of a crowd is evidence the crowd weighs. Complete at the ends: no regard, no draw; the scale's ends hold.
- **S.** The one sampler, the one composer, the deposit site that already grades credit; `conviction.moved` has one Event kind and two emitters, named.
- **E, last.** One function and one call site against the only way a house's opinion can move. High.

## Cost class

Small build, a declared mover (1). Edit, a declared mover (2). Edit (3).
