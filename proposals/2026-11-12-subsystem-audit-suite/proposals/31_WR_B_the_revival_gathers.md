# WR-31-B — the Revival gathers: a stand moves by a draw when a man takes in what one of a creed has done, so a cause can rise, stall or collapse

Reconciled: 2026-11-12, wave 3 (W3-3) — C3-L6 and R3 §1 (commit 1 VIOLATES `04` §B.2 "WITNESS never touches a conviction", "evidence cannot move a conviction", and AX-3 as written): the sway draw moves from `loop/witness.py` to the RESOLVE-side emitter of `16_PESSIMIST_CHAR_A` (`loop/resolve.py::_conviction_crisis`'s step, the ACTS token), reading the deed claims deposited since the person's last RESOLVE through a person-side reader; WITNESS stays ledger-only; the `write_matrix.yaml` WITNESS writer is deleted from the plan; `sway_gain` ships 0 and stays 0 until the calibration batch sets it (**J-U3-01 answered as A-92**, Option 1, 2026-11-12: what a person has seen and been told of others' deeds is a term in his own drawn act and nowhere else; the machinery is built at RESOLVE with its dial at zero). The `04` §B.2 rewording A-92 needs is owed text, not applied (`OWED_TO_UNIFICATION.md` §A). R3 §2 (A-5, A-6, A-7): the pool's dice counts are `[CALIBRATE]` under the capability architecture's form (joint calibration, OWED §B). C3-K7 (commit 3's storybar edit is the last in the serial order). U3 §6.1 (`test_sway.py` absent, written first). Batch (U3 B38). Tier already named.

Reconciled: 2026-11-12, U6 repair lane R-C (`unified/U6_VERDICT_AND_REPAIRS.md` findings 4, 5, 6): regard, circle and links reach the sway roll as named levels (`sway_level`, netted by `levels_to_net_sigma`, applied by `net_boost` under the soft cap), never as dice; the pool is the one pool rule on the untrained score; `sway_pool` is withdrawn and `sway_level` takes its NUMBER row (D-U1-01: everything that is not training enters as levels); `sway_odds` returns the two level lists; one test added. J-U3-01 is shown answered (A-92, Option 1) at the head, Status, the commit table and "Layer 1"; the dial-at-zero build until the calibration batch and the owed `04` §B.2 text stand. "pole" → "affiliation" throughout, the Event payload key included (glossary *affiliation*); A-91's own words are quoted once. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "training" for the rank → skill score (1); rewordings by sense (1: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

## Status: PROPOSED (the form is decided; A-92 answered J-U3-01 as Option 1; its four numbers are `[ASSUMPTION]` and set at calibration; commit 1's dial ships at zero until the calibration batch; nothing here was built)

Lands in batch: B38 (narrative and regimes), after `31_WR_A` and before `31_WR_C` (U3 §1 item 38). Commit 3 edits `harness/storybar.py` after `30_WR_E`, last in C3-K7's order.
Depends on: `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (B10, the RESOLVE-side emitter commit 1 composes on); see "Dependencies" below.

Source: Jordan, 2026-11-12, **A-89**: *"varfell neutral leaning Einhir with momentum building for Einhir Revival"*; A-24 (a conviction moves by a draw), A-83 (the unsaid pressure of one's own), A-80, A-81, A-88, A-90. `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` F-31-07, F-31-08. Reference only (`CLAUDE.md` §0.05). Lane WR with CHAR; owner files `engine/season/loop/resolve.py` (the crisis emitter's step), `queries/person_q.py`, `data/fixtures.py`, `harness/populated.py`.

Composes on, and restates none of: `31_WR_A` (the rows, the cores, `opinion_links`, a faction's `creed:` signs, `closeness`, `core_standing`), `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (the emitter and Event kind `conviction.moved`), `30_WR_G` commit 5 (`world_q.circle_of`), `20_NARRATIVE_D` (the public `creed:` row), `02_CHAR_resolve_and_temper.md`, `30_WR_D` (LOOP rows), CR-107 (cohort convictions).

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | `person_q.sway_odds` and the sway draw at RESOLVE, in the crisis emitter's step (`loop/resolve.py::_conviction_crisis`, `16_PESSIMIST_CHAR_A`), over deed claims deposited since his last RESOLVE, behind `Fixtures sway_gain` | EQUAL at 0 (control, shipped, held at 0 until the calibration batch, A-92); above 0 a **declared mover** for every person who has taken in a deed by a member of a faction with a `creed:` row |
| 2 | cohorts take their holder's regime core at build, each half settled by a keyed draw, behind `Fixtures cohort_convictions` | EQUAL at `False`; `True` a **declared build-hash mover** |
| 3 | LOOP row **L17 the cause gathers** in `hole_register.yaml`; `storybar --regimes` prints each core's gap and its word | EQUAL |

No counter, no clock, no trigger. No house, movement or person is named in code.

## The problem, with evidence

- A-89 asks for a trend, and nothing in the engine moves a stand except the crisis, which is a fixed function of the build (`16_PESSIMIST_CHAR_A` §1: the same six persons at every seed). In this lane's two-season run at seed 1 with the cast's new values, five persons were rewritten by it, each to `einhir_restoration` or `solmund_orthodoxy` at 3 to 5 from a value of 1 or 2 (P-31-8): the only "drift" the shipped engine has runs against the persons' own stands.
- The five principals of Varfell already stand at 4 or 5 on the tradition's affiliation, `einhir_restoration` (A-91 (3)'s "tradition pole"; `31_WR_A`:40; `references/npc_registry.yaml`, their own rows). They cannot be the ones gathering. The house's leaners are its populace, and a cohort holds no conviction at all (`engine/season/cohorts.yaml:106-107`: "a cohort gets NO goals and NO convictions"; CR-107 held).
- Persons learn of each other's deeds constantly and of each other's opinions never: 1,529 resolved acts in two seasons at seed 0 against nine tellings between cast members (P-31-7). A mechanism that waits for a man to be told another's creed will not run; one that reads what he makes of what he sees will.

## The resolution, decided

**A man's stand on a question leans, by a draw, toward the creed of those whose deeds he approves and away from the creed of those whose deeds he resents.** One rule, for every person, creed and affiliation.

1. **The occasion** is a claim of a deed landing in his ledger (seen or told), where the doer is another person whose faction carries a `creed:` row (`31_WR_A` commit 4). It is read at his next RESOLVE, in his own drawn step, not at the deposit (C3-L6: WITNESS never touches a conviction). No clock: no deed taken in, no draw.
2. **What he reads** is his own: his regard for the doer once this deed is judged (`person_q.regard`, his ledger and weights), and his own stands. The doer's side and that side's public creed are handed down resolver-side as two values, as `world_q.opinion_of` hands down `regarded` (`world_q.py:3055-3062`); he never reads the doer's convictions.
3. **Which affiliation** is drawn among the creed's affiliations, weighted by his room to move on each.
4. **The draw** is the one sampler's four-band ladder (A-5), composed as every roll is (U1 architecture §4; `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`:95-109 for the crisis beside it): the pool comes from the skill score alone and everything else enters as named levels on the one leverage channel, soft-capped (D-U1-01). Every number below is `[CALIBRATE]` under the capability architecture's form (pool from a score plus base, A-6; two inputs, A-7), set in the joint calibration (OWED §B), not here. **Pool**: the one pool rule on the untrained score, `pool_of(pool_default, (), pool_add, pool_floor)` `[ASSUMPTION: no skill is exercised in being moved by what one sees, so no skill score enters — basis: D-U1-01 leaves nothing else to be the pool; the CHAR content pass may add an attribute `edge` row, as the crisis's `attr.mind.will`]`. **Levels** (each a `sway_level`, a `LEVEL_SIGMA` name, netted by `levels_to_net_sigma` and applied by `net_boost` under the soft cap): on his side, one per whole unit of how strongly he regards the doer (`sway_gain`), one if the doer is of his circle (`circle_of`: the pressure of his own, A-83), and one per whole unit of the links' lean for the step (`opinion_links`, `sway_link`); on the other side, one per whole unit of their lean against it. **Obstacle**: how firmly he already stands on that affiliation, plus his temper. So a lukewarm man near a vanguard he admires moves readily; a firm man is hard to move; a man who rejects the caste is hard to win for the royal order that carries it (A-87's "due to caste", as odds).
5. **The bands.** Overwhelming: one step toward the creed's sign (away, if he resents the doer), and it shows: `conviction.moved` reaches those present. Success: one step, known to himself. Partial: no step. Failure: if he already stood against that creed's sign he **hardens** one step further against it; otherwise nothing. Values stay in 0 to 5.
6. **Seeded at the start state, not scripted.** Varfell's momentum is the configuration `31_WR_A` authors plus commit 2: a vanguard at the ceiling, a populace seeded at the core (leaning), a public creed, and little of the Church nearby (`canon/03_canonical_timeline.md:100`: "lower Church penetration"). Whether it builds is then what happens: a lord's deed the valley approves pulls it on; a levy or a lost field it resents pushes it back; an inquisitor's arrest seen by people who resent him moves them **away from the Church's signs**, which is toward the Einhir on both affiliations, the religion and the people (A-88, A-90), unless they are devout, in which case it confirms them. The same rule runs in Hafenmark toward its own creed and in the Church's flock toward orthodoxy.
7. **The prologue** (A-51, five simulated years) runs with the same fixture, so a realm can start with the trend already in its ledgers.

**Entrenchment and stillness (A-80, A-81).** A held stand is the obstacle, and it produces: the Failure band's hardening (an attempt on the firm makes them firmer, so a counter-core grows as a cause grows), the visible convert (a deed others judge), and the man pulled apart by a link, whose next step either way is a story. The draw rides a deposit that has already written a claim, so no occasion is still.

## Instructions to code

Tier: commit 1 third tier (opus) for the placement and the pool's composition, with a second-tier critic; commits 2 and 3 second tier.

**Commit 1 (control EQUAL; above 0 a declared mover).**
1. `engine/season/data/fixtures.py`: `sway_gain=0.0` (the switch and the regard scale: `sway_level`s per unit of `|regard| / STANCE_MAX`; swept `0` control, SHIPPED / `2` / `4`), `sway_level="minor"` (a `LEVEL_SIGMA` name, refused at load otherwise; swept `minor / moderate`), `sway_hold=2.0` (obstacle per unit of `|conviction_stand|`; swept `1 / 2 / 3`), `sway_link=1` (`sway_level`s per unit of link lean; swept `0` control / `1`). No dice count is a fixture: the pool is the one pool rule's (D-U1-01). Four NUMBER rows in `hole_register.yaml`, each `[ASSUMPTION; medium; Jordan to correct; revert: sway_gain 0]`. The obstacle's base and the temper term come from the one obstacle composer (`02_CHAR_resolve_and_temper.md`), not from a number here.
2. `engine/season/queries/person_q.py`, beside `link_fit`:

```python
def sway_odds(p: Person, creed: dict, toward: int, in_circle: bool, regard_unit: float, fx) -> tuple:
    """((affiliation, direction, pool, obstacle, mine, theirs), ...) for every affiliation of `creed`
    ({affiliation: -1 | 1}, a faction's public row) on which `p` has room to move one step in
    `direction = toward * creed[affiliation]`.
    pool = pool_of(pool_default, (), pool_add, pool_floor)      # the untrained score: no skill here (D-U1-01)
    link = round_half_up(sway_link * sum(sign * conviction_stand(p, frm) * direction
                                         for (frm, to, sign) in OPINION_LINKS if to == affiliation))
    mine = [sway_level] * (round_half_up(sway_gain * abs(regard_unit)) + (1 if in_circle else 0) + max(0, link))
    theirs = [sway_level] * max(0, -link)                       # levels, never dice: netted by levels_to_net_sigma
    obstacle = the composer's base + sway_hold * abs(conviction_stand(p, affiliation)) + his temper term.
    `toward` is +1 when `regard_unit` > 0, -1 when below, and () when it is 0. Reads `p` only (AX-2)."""
```

3. `engine/season/loop/resolve.py`, in the step of `_conviction_crisis` (`16_PESSIMIST_CHAR_A`, the one emitter of `conviction.moved`, under the ACTS token), after that person's crisis draw: when `fx.get("sway_gain")` is not 0, for each deed claim (`data/verbs.py::DEED_KINDS`, `:1492`) deposited in his ledger since his last RESOLVE (a person-side reader, new, `person_q.deeds_taken_in_since(p, tick)` `[ASSUMPTION: name coined here; the landing lane may reuse an existing recent-claims reader such as `recent_claims` if it filters by tick]`, over his own claims' `round`/tick stamps; no World), whose doer's faction has a `FACTION_CREED` row (the side and its creed handed down resolver-side, as `world_q.opinion_of` hands down `regarded`): compute `regard_unit = regard(p, doer) / STANCE_MAX` and `in_circle = doer in circle_of(w, p)`; ask `sway_odds`; pick one row by a keyed weighted draw (weight: his room on that affiliation); roll the row's pool, `roll_net_continuous(pool) + net_boost(levels_to_net_sigma(mine, theirs), pool)`, against its obstacle with the season's keyed sampler under the key `("sway", tick, round, p, claim.id)` (A-30: one draw per key); apply the band of §5 through `conviction_map` (the one validator) in the same `w.write` path the crisis uses; on Overwhelming or Success emit `conviction.moved` with `{affiliation, before, after, on_account_of: claim.id}` (Success carries `visibility: own`). One sway draw per deed claim taken in; a cohort draws as any person. `loop/witness.py` is not edited: WITNESS stays ledger-only (`04` §B.2; AX-3).
4. `engine/season/write_matrix.yaml`: no edit; `(Person, conviction)` is already written at RESOLVE by `_conviction_crisis` (`16_PESSIMIST_CHAR_A`'s verification). The WITNESS writer formerly proposed here is withdrawn (C3-L6). `verb_table.yaml` is untouched (no verb).
5. Tests, `engine/season/tests/test_sway.py` (new; absent on `main`, written as the batch's first commit, U3 §6.1; add `test_witness_writes_no_conviction`, the C3-L6 falsifier: a deposit with `sway_gain` above 0 leaves every conviction unchanged until the person's RESOLVE): `test_sway_gain_zero_is_byte_identical`; `test_no_deed_taken_in_no_draw` (a person whose ledger gains nothing in a season has the conviction he began with); `test_a_firm_stand_meets_a_higher_obstacle_than_a_lukewarm_one`; `test_a_resented_doer_moves_him_away_from_that_side_s_signs`; `test_a_link_against_the_step_puts_a_level_against_it` (a person at `caste_order` 0 offered a step toward `royal_order`: `theirs` is not empty and the pool is unchanged); `test_regard_and_circle_reach_the_roll_as_levels_not_dice` (the pool equals `pool_of(pool_default, …)` at every regard); `test_failure_hardens_only_one_who_already_stood_against`; `test_the_step_stays_on_the_scale`; `test_the_draw_is_keyed` (same seed, same step; a different seed over 20 planted deposits does not give the same 20 bands); `test_sway_reads_no_doer_conviction` (the function's arguments hold no other `Person`). `assert checked >= 8`.

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
3. Varfell's gap on the two Einhir affiliations is `rising` at some seeds and `stalled` or `falling` at others over five seeds: all three words need not occur, one word at every seed fails.
4. The Church's core does not shrink in the seeds where the Revival's grows by more than the off arm's seed spread: the counter-core holds (the Failure band).
5. Entrenched-world arm (`sway_hold` at its highest swept value): stands barely move, and executed acts per person-season and the story census's rate (`23_STORY_D`) are not below the off arm's by more than its seed spread (A-80).
6. The no-null-scene reading is unchanged between arms (A-81).

## The falsifier, and its control

- The same persons stepping the same way at every seed: the draw is not keyed or the pool swamps the obstacle; it is a script.
- Varfell `rising` at five seeds of five with identical gaps: the trend is built in; lower `sway_gain`.
- No step anywhere at `sway_gain` 4: the occasion is not reached (no deed by a creed-bearing faction's member is deposited), and the row is recorded `inert`; the gain is not raised to pass.
- A step with no claim landing that round: it read the World or a clock.
- A person at `caste_order` 0 stepping toward `royal_order` as often as one at 4, over 200 planted draws: the link term is not among the levels.
- Controls: `sway_gain` 0; `sway_link` 0 (the link off, the drift on); `cohort_convictions` False.

## Dependencies

`31_WR_A` commits 1 to 4. `16_PESSIMIST_CHAR_A` (the Event kind; the fixed crisis must be drawn first, or it overwrites what sway moves). `30_WR_G` commit 5 item 4 (`circle_of`); lands without it with `in_circle` False. `02_CHAR_resolve_and_temper.md` for the temper term; lands without it on the base. Feeds `30_WR_D` (L17), `30_WR_E` (a shape: a cause that gathers and its counter), `30_GO_F`, `31_WR_C`.

## Layer 1

AX-2 and AX-7: `sway_odds` takes the person and three handed-down values; the doer's interior is never read. `ED-IN-0352` (3) (no flow touches an obstacle, pool or draw): the levels read his regard for one doer and his own stands, and the pool is the untrained score; no strand, era, count or core is read. `ED-IN-0225` (nothing fires): the occasion is a deposit read at his own RESOLVE, the result a band. `holonic` §29 (no clock at census): none. The standing rule (a draw): four bands, keyed. `04` §B.2 ("WITNESS never touches a conviction"; "evidence cannot move a conviction") and AX-3 (INTERIOR at WITNESS, ACTS at RESOLVE): the draw runs at RESOLVE under the ACTS token and WITNESS stays ledger-only, which keeps the token split (C3-L6). The second row is not met in effect while `sway_gain` is above 0 (a claim taken in is a term in the draw); Jordan answered **J-U3-01** as **A-92** (Option 1, 2026-11-12), so the rule is licensed, and the dial ships at 0 until the calibration batch sets it (no seeded result moves before then); A-92's rewording of that row ("evidence enters a conviction only as a term in the person's own drawn act, never as a direct write") is owed text, not applied (`OWED_TO_UNIFICATION.md` §A). **MECHANICAL** (`test_witness_writes_no_conviction`; the matrix's existing RESOLVE writer). Scripting drift: none; **STRUCTURAL** (no id in the function's inputs).

## NERS reading

- **N.** Without it A-89's momentum is a start value that never moves, and a regime changes only by the crisis. Holds bottom-up (one valley man and the lord he sees), top-down (a cause that gathers across a house), laterally (the same regard that ranks his acts moves his stand), diagonally (the Church's arrest feeding what it suppresses). Narrowed: it is inert until deeds by creed-bearing sides are deposited, which the gate reads.
- **R.** A revival that can fail; a counter-reformation that grows with it; a convert seen converting; all with no player. A player's deed in front of a crowd is evidence the crowd weighs. Complete at the ends: no regard, no draw; the scale's ends hold.
- **S.** The one sampler, the one composer, the crisis emitter's own RESOLVE step; `conviction.moved` has one Event kind and one emitter site, with two draws in it.
- **E, last.** One function and one call site against the only way a house's opinion can move. High.

## Cost class

Small build, a declared mover (1). Edit, a declared mover (2). Edit (3).
