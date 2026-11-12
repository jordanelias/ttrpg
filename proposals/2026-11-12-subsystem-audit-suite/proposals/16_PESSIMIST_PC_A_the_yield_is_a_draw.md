# 16 · PESSIMIST · PC · A — the yield is a draw: whether a wounded fighter gives up is his, and is rolled

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.5) — the draw's two inputs follow A-7 and A-8 (U1 §4); the form, the site, the bands and the gate stand. (1) **Pool:** dice come from training, never from an attribute, so the pool is the one pool rule on the party's score in the capability the check tests (none is authored for holding one's nerve, so the untrained default: `resolution_pool(pool_default)`), and **Spirit enters as talent levels** (`per: mid`) on the roll, where the first text put it in the dice. (2) **Wounds are a level, not obstacle points:** the obstacle is `YIELD_OB[terms]` alone; the wounds enter as the level `wound_impairment` already gives the wounded side, one ladder for one quantity. (3) The prototype table below was read on the first form and on a three-blow fight; it is re-read after the damage scale (A-31) inside the calibration batch (`U5b_PC_rulings_in_the_fight.md` §5 row 5). The Spirit and modifier sweeps keep their direction by construction (a level for is a level for).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 and §2 (A-30: "the scene's own `rng`" U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*).
replaced by a keyed draw), §7/§7b (test file, tier; `YIELD_OB`'s shipped values stay the sweep's pick, Jordan's); U1
D-U1-08 (the pool is `sigma_leverage.pool_of` on the skill score, not `core.resolution_pool`), D-U1-11m (the CHAR
reader is `person_q.decisiveness`; the input field takes the same name, `decisiveness`, so one word names one thing),
glossary *roll* ("yield check" → "yield roll"; the function `_resolve_check` → `_yield_roll`); U3 B15, §4.1 row 55 (this
file supersedes `03_PC_exits_withdrawal_recovery.md` Part B, the yield), §6.2 (`pB_yield.py`, `pM_yield_draw.py` are not
in the repository). Changed: "What it changes", the pool and modifier bullets, the edits table, the gate's test names.

## Status: PROPOSED

Lands in batch: **B15** (PC; the calibration batch), last of its four pessimist rows (UPR §5 row 5: PC_B → PC_D → the
riposte → PC_A). Depends on: `14_VERBS_PHYSICAL_A_custody_and_force.md` (B15, A3), `02_CHAR_resolve_and_temper.md` (B10,
the `decisiveness` reader), `engine/dice_engine/draw.py` (B06), `sigma_leverage.pool_of` (B05).

Source: `audits/16_PESSIMIST_PC.md` §2.2 (F-PES-PC-03). Standing rule: `AUDIT_BRIEF.md` (Jordan,
2026-11-12, *"we do not do deterministic"*). Composes with, and does not restate,
`14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (the mortal-wound draw after a felling; `context_terms`);
it supersedes `03_PC_exits_withdrawal_recovery.md` Part B (the yield; U3 §4.1 row 55, A-24).
Reference only (`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

Every season `fight`, `accept` and `capture` scene in which a party is wounded and not felled now takes
one or more keyed draws at the end of the turn (`H(seed, tick, scene id, "yield:<turn>:<party>")`, A-30), and may end in a yield it would not
have ended in (a `fight` under `death` terms can now end with both men alive) or run on past a line it
would have stopped at (a duellist can fight on after first blood). **Declared hash mover for every world
with a fight.** `PersonalCombatInput` gains one optional field; the fold gains no band and no
kind (`duel.yielded` and `Event.ending`'s `yielded` exist).

## The problem (evidence)

`modules/combat/wrapper.py:519-539`, `:600-612`: under `blood` and `yield` terms the fighter who crosses
the term's line yields at the end of that turn, always, and the surrender is always accepted; under
`death` terms nobody yields. `pB_yield.py`, 3,000 season-default fights per term, `PYTHONHASHSEED=0`:

| terms | yields | felled | fighters across the line who did not yield | yields above the line |
|---|---|---|---|---|
| `death` | 0 | 99.8% | — | — |
| `blood` | 100.0% | 0 | 0 | 0 |
| `yield` | 94.4% | 5.6% | 0 | 0 |

Spirit 1 against 7, disposition 1 against 7 and Focus 1 against 7 (1,500 fights each): the highest
Health fraction at which anyone yields is 0.500 in every arm. The decision to stop is a fixed function of
one number, the same for every person. `14_VERBS_PHYSICAL_A` A3's `context_terms` will send `crime` and
`defence` fights to `yield` terms, so after it lands this threshold decides most fights in the game.

## The resolution, decided (ladder step 1: the standing rule answers it)

**At the end of any turn in which a wound gate was crossed on a standing party, that party makes one yield
roll to fight on.** One site, in `wrapper.fight`, replacing `:600-612`; one roll, through `core.resolve` (the
owner ladder); every term. The draw is keyed `H(seed, tick, scene id, "yield:<turn>:<party>")` through the
one keyed-draw owner (A-30), not a generator threaded through the scene.

- **Pool** *(Reconciled, A-7; D-U1-08)*: `sigma_leverage.pool_of(score, (), pool_add, pool_floor)`, `score` the
  party's skill score in the skill the roll tests (carried on `PersonalCombatInput.scores`), the untrained
  default where none is authored. **Governing attribute:** Spirit
  (`attributes.py`: registry key `attr.mind.will`, already carried on `PersonalCombatInput.attributes`)
  enters as named levels for or against the roll by its distance from the mid-point, so an authored
  person still brings his own. ~~`core.resolution_pool(c.spirit)`~~
- **Obstacle** *(Reconciled, A-8)*: `cfg['YIELD_OB'][terms]`: the term sets how much is at stake in
  stopping. How hurt he is enters as a level against the roll (`wound_impairment`'s per-wound term, the
  channel the exchange already uses), not as points on the obstacle. ~~`+ c.wt.wounds`~~ `YIELD_OB` is one new `CFG` key, a dict over `DUEL_TERMS`
  (`[SIM-CALIBRATE]`; the exporter collects `CFG` whole).
- **Modifier (σ):** `inp.decisiveness[i]`, a new optional field of `PersonalCombatInput` (default `()`,
  which is 0.0 for both): what the host knows that the module does not (what he is fighting for). It
  enters as `net_sigma`, under the owner's soft cap, like every other modifier in this module. The host
  fills it when a reader exists (`02_CHAR_resolve_and_temper.md`'s reader, named `person_q.decisiveness` by
  D-U1-11m); until then nobody carries one and the draw rests on Spirit and wounds.
- **Bands (graded, recoverable):**
  - Failure: he yields. The `yield` event as today (`by`, `turn`, `terms`), plus `degree`.
  - Partial: he is shaken and fights on: `c.conc −= cfg['CONC_DRAIN_LOSS']` (existing state, existing
    constant); a `shaken` trace event.
  - Success: he fights on.
  - Overwhelming: he rallies: `c.conc = c.conc_max`; a `rallied` trace event.
- **Two failures in one turn:** as today's tie rule (`_terms_yielder`): the one with the smaller
  fraction of Health yields; an exact tie yields nobody and the scene ends undecided.
- **Acceptance.** Under `blood` and `yield` the terms are the acceptance (as today). Under `death` the
  scene ends with the yielder standing and the event carries `accepted=None`: what the other man does
  with an unresisting man is the host's (the `Yield` docstring's rule, `wrapper.py:483-497`; the verbs
  that exist: `fight` again where a context holds, `capture` through a seat, or nothing). The victor's
  choice is a chooser act, therefore a sampled choice (D-06), and is not designed here.
- **The burst-breaker reads a new crossing.** `engagement`'s between-beats stop (`:153-154`) today reads
  standing state (`_terms_met`: anyone has a wound). Once a man's yield roll can let him fight on, that
  would end every later engagement at its first beat. It becomes: a party crossed the term's line
  *during this engagement* (for `blood`, `c.wt.wounds` greater than at `engagement_start`). Measured on
  the prototype before the change: 16.3% of `blood` duels froze undecided.- **`YIELD_HEALTH_FRAC`** stays the `yield` term's burst-breaker line and stops being a decision.

## Prototype reading (in-process, no tracked file touched; `pM_yield_draw.py`)

`fight_p` replays `wrapper.fight`'s turn loop call for call with the block above in place of
`:600-612`; season-default mirror, 1,500 fights per term; probe values `YIELD_OB = {blood: 4, yield: 2,
death: 0}`.

| terms | yields | felled | undecided | yielder's Health at yield (q10 / q50 / q90) | yielder had passed an earlier check | checks: Fail / Partial / Success / Overwhelming |
|---|---|---|---|---|---|---|
| `blood` | 93.1% | 6.8% | 0.1% | 0.25 / 0.42 / 0.68 | 4.6% | 84.0 / 7.4 / 7.0 / 1.6 |
| `yield` | 74.5% | 25.2% | 0.3% | 0.12 / 0.35 / 0.68 | 11.9% | 58.2 / 14.9 / 19.1 / 7.8 |
| `death` | 32.1% | 67.7% | 0.3% | 0.07 / 0.33 / 0.68 | 16.4% | 29.5 / 13.0 / 30.7 / 26.8 |

Controls: an obstacle no pool can fail (−99) reads 99.7% felled under `death` (shipped: 99.8%), every
check Overwhelming; an obstacle no pool can beat (+99) reads 95.2% yield under `yield` terms.

The person now moves the decision (terms `yield`, A varied against a default B, 1,000 fights): A's share
of the yields is 55.8% at Spirit 1, 48.3% at 3, 32.9% at 7; with `resolve` +1.0σ 31.9%, −1.0σ 57.1%.

What the reading shows that a value sweep must settle: under `yield` terms the felled share rises from
5.6% to 25.2% at the probe value, because a man who fights on meets the next Overwhelming blow (audit
§1.1). That is the premise working ("some fight on, and some of them die for it"), and A3's mortal-wound
draw then stands between a felling and a death; but the shipped `YIELD_OB` is to be chosen by the gate's
sweep, not taken from this table.

## Exact edits, by owner

| file | edit |
|---|---|
| `modules/combat/config.py` | new key `YIELD_OB={'blood': …, 'yield': …, 'death': …}` with its `[SIM-CALIBRATE]` note and the rule in the gate below; `YIELD_HEALTH_FRAC`'s note restated (the `yield` term's burst-breaker line, no longer the decision) |
| `modules/combat/wrapper.py` | `:600-612` replaced by the roll above (a function `_yield_roll(c, terms, sigma, cfg, draw)` returning the degree, `draw` the keyed `Draw` for `"yield:<turn>:<party>"`; the wrapper applies the band); `engagement` takes the wounds at its own start and `_terms_met` reads a new crossing; the `DUEL TERMS` comment block (`:503-515`) restated; `shaken` and `rallied` added to the trace vocabulary |
| `engine/season/queries/inputs.py` | `PersonalCombatInput.decisiveness: tuple = ()` |
| `modules/combat/fight.py` | passes `inp.decisiveness or (0.0, 0.0)` to `wrapper.fight(..., decisiveness=…)` |
| `engine/season/seam/wrappers/combat.py` | `surrender_of` unchanged (it lifts the same event); `fight_estimate` unchanged (it already tallies `yielded`) |
| `engine/season/verb_table.yaml`, row `fight` | the `Wounded` and `Untouched` bands declare `duel.yielded`, earned by the yielder alone, as `accept`'s do (`loop/effects_combat.py:234-238`); this is `03_PC_exits_withdrawal_recovery.md` Part B's second bullet, adopted |
| `engine/engine_params/combat_engine_v1.json` | re-derived by `python tools/export_engine_params.py` (never by hand) |

## Gate (execution artifacts)

The probes were lane scratch (not in the repository). NEW `tests/valoria/test_combat_yield_draw.py` (beside
`test_combat_duel_terms.py`, which exists): `test_fighters_across_the_line_sometimes_fight_on` (gate 1),
`test_death_terms_leave_both_alive_sometimes` (gate 2), `test_spirit_seven_yields_less_than_spirit_one` (the
falsifier's second clause), `test_unreachable_low_yield_ob_reproduces_shipped_death_share` (gate 3),
`test_yield_roll_is_keyed_by_turn_and_party`. Command: `python -m pytest tests/valoria/test_combat_yield_draw.py -q -m combat`.
The prototype table above is whole-dice and pre-A-31 (head line); it is re-read in the calibration batch.

1. The audit's `pB_yield.py` reading, committed as gate 1's test: under `yield` and `blood` terms, fighters across the line
   who did not yield is strictly above 0, and yields above the `yield` line is strictly above 0.
2. Under `death` terms the season-fight probe (the PC audit's E3, 200 seeds) reads a share of scenes
   with both parties alive strictly between 0 and 1.
3. Control: `YIELD_OB` at an unreachable low value reproduces the shipped `death`-terms shares (99.8%
   felled) and, with the burst-breaker change reverted, the pre-change hash.
4. The sweep that ships the values: over a grid of `YIELD_OB`, the `blood` mirror's yield share stays
   above nine in ten (a duel to first blood usually ends at first blood) and the `yield` mirror's
   felled share is reported beside each grid member; the pick is Jordan's from that table.
5. `python tools/export_engine_params.py --check` green.

## Falsifier

After the build: 3,000 `yield`-term fights in which every fighter across the line yields and none yields
above it; or a Spirit 7 fighter who yields as often as a Spirit 1 fighter (shares inside each other's
interval at n 1,000).

## NERS reading

- **N** (all directions). Top-down: the standing rule and R-09 ask it. Bottom-up: the engine already
  owns the state (Concentration, wounds) and the roll; no new resolver. Vertical: the season's fold
  already writes a yielder by his own band. Lateral: the social contest's concession and the field's
  rout are the same act at other scales and are draws (or proposed as draws) there. Diagonal: the
  mortal-wound draw (A3) covers what follows a felling and this covers what precedes one; neither covers
  the other's ground. Horizontal: `capture`, `accept` and `fight` share the one site. Cut it and the
  beaten survivor, the man who fights on, and the duellist who will not stop at first blood all die.
- **R.** The half with no player: NPCs now differ in a fight by will. Completeness: at Spirit 0 the pool
  floors at 5 dice (`POOL_FLOOR`), so the roll exists at the extreme.
- **S.** One ladder, the owner's; the modifier is σ like every other in the module; it pauses nothing
  (it is read between turns, where `decide` is already consulted).
- **E, last.** One `CFG` key, one input field, one function; it removes a tie-break special case from
  the decision (the tie rule survives only for a double failure). High against what N and R found.

## Cost class

Small build. One open value set (the sweep's pick). **INCOMPLETE at the values only:** `YIELD_OB`'s shipped dict
is Jordan's pick from gate 4's table (not decidable from the repository). Tier: `opus` for the sweep reading,
`sonnet`, effort `high`, for the code. Hash movers declared: every world with a fight (one re-pin at B15's
close with the calibration batch). Lands it: B15, order the input field (default, hash-equal) → `_yield_roll` and
the burst-breaker → the `fight` row's bands → the exporter re-derive.
