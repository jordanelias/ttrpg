# 16 · PESSIMIST · PC · B — the commit window: the deep tier follows the window it is drawn in

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.5) — order only. A-31 (longer fights) lands the damage scale first; this proposal is the second step of the one combat calibration batch and shares its single re-record (`U5b_PC_rulings_in_the_fight.md` §5 row 5); the approach (`03_PC_duel_round_and_approach_B.md` step 3) lands after both. The prototype readings below are re-taken at the new scale before `DEEP_FRAC` ships.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS), §7/§7b (test file, gate U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*); the fencing riposte of §4's table is the combat module's own and keeps its name.
commands, tier); U3 B15, §4.1 row 56 (REV: the calibration batch lands before the round, UPR §5's own order), §6.2
(`pF_story.py`, `pP_window.py` are not in the repository); U1 glossary *faculty* (retired as a suite word: "trained
score" in the prototype table). Changed: the gate's committed form, the cost line, one table label.

## Status: PROPOSED

Lands in batch: **B15** (PC; the calibration batch), first of the pessimist rows (UPR §5 row 5: PC_B → PC_D → the
riposte → PC_A), after the A-31 damage scale (`U5b_PC_rulings_in_the_fight.md`). Depends on: nothing unlanded beyond
that batch's damage scale.

Source: `audits/16_PESSIMIST_PC.md` §1.3, §2.1, §2.6 (F-PES-PC-04, F-PES-PC-02). Bears on
`03_PC_duel_round_and_approach_B.md` §3 (the approach leans commit depth and the counter) and on the PC
addendum's F-PC-17. Reference only (`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

Every season fight: the Indes steal, the single-time counter, the displace-and-step-inside, the
over-commit reopen and the lunge become reachable in about a third of exchanges instead of one in a
hundred. **Declared hash mover for every world with a fight**, and a re-record of the combat
calibration figures. Prototype reading below: the mirror, the skill lever and the weapon matchups read
inside their control bands; what moves is that depth stops being free.

## The problem (evidence)

`combat_systems.commit_depth` (`modules/combat/combat_systems.py:1113-1128`) draws
`commit = 2.0 + span·Beta(a, b)` with `span = 3.0 · _commit_range_factor(range_avail)`. The docstrings
and `config.py:287-290` describe a spectrum over [2, 5] ("aggressive → toward 5"). The swing-room
contraction (I5/D4, the closing-distance redesign) sets
`range_avail = RANGE_AVAIL_FLOOR + (1 − RANGE_AVAIL_FLOOR)·measure_gap/CLOSE_EFF_GAP_REF`
(`:441-450`; 0.3, 6.5) and the factor `RANGE_COMMIT_FLOOR + (1 − RANGE_COMMIT_FLOOR)·range_avail/
RANGE_COMMIT_PEAK` below the peak (`:452-460`; 0.5, 0.85). An exchange is only ever fought closed
(`wrapper.py:263`), where `measure_gap` is at most the latch band (0.6) and is 0 for equal reach. So in
every exchange of every fight the window is **[2, 4.03]** (factor 0.676), at most [2, 4.14].

`DEEP_COMMIT` and `LUNGE_COMMIT` are both 4.0 (`config.py:290`, `:327`), set when the window was [2, 5]
(its upper third). They now sit in the top 1.5% of the window. Measured (`pF_story.py` F3, 300 mirror
fights per weapon, `PYTHONHASHSEED=0`): the largest commit drawn is 4.03 for each of ten weapons
(arming, dagger, rapier, longsword, greatsword, mace, spear, poleaxe, katana, estoc); the share of
exchanges at or above 4.0 is 0.71% to 1.17%; in 5,000 season-default fights, 0.91% of 31,757 exchanges.
What is gated there and therefore almost never consulted (`wrapper.py`): the lunge (`:284`), the Indes
steal and `counter_select` (`:325-329`), the displace route (`:387`), the shorter fighter's over-commit
reopen (`:401`). The cut test agrees: gating the tier off entirely (`DEEP_COMMIT = 99`), removing the
counter, removing the lunge and zeroing the over-commit exposure each move no outcome share by more
than 2.3 points and no fight length by more than 0.17 turns on any of six matchups (audit §1.2).

The consequence for the stated intent: inside the live window, depth has no cost. Forcing one fighter's
depth against an opponent who draws normally (season-default mirror, 1,500 fights; as drawn 49.9%
felled, disjoint-seed control 52.1%): 3.9 → 45.3% felled; 3.0 → 49.0%; 2.3 → 54.4%. Monotone, nine
points end to end, and the cliff that would punish it stands at 4.0 where the Beta almost never goes.
An "aggressive / normal / defensive" approach built on this lean has one right answer.

This is the pattern-defect signature (`CLAUDE.md` §0.1 pt 5): the thresholds were right when written
and stopped working when the window moved.

## The resolution, decided (ladder step 5)

**A threshold on a drawn quantity is stated in the quantity's live range.** The deep tier is the upper
third of whatever window the beat allows:

```python
# combat_systems.py, beside commit_depth -- the ONE owner of "deep"
def deep_commit(aggressor, cfg):
    """The depth at/above which a commit is DEEP this beat: the lower edge of the window's upper third."""
    span = 3.0 * _commit_range_factor(getattr(aggressor, 'range_avail', 1.0))
    return 2.0 + cfg['DEEP_FRAC'] * span          # DEEP_FRAC = 2/3: at full room exactly 4.0, as shipped
```

`cfg['DEEP_FRAC'] = 2/3` replaces the two absolute keys' role at the five sites; at `range_avail ≥
RANGE_COMMIT_PEAK` it is byte-identical to 4.0. At closed measure it reads 3.35. `LUNGE_COMMIT` takes
the same edge (a lunge is a different fact and keeps its own key, `LUNGE_FRAC`, equal today). The Indes
scale's anchor (`combat_systems.py:1155-1156`, "scale 1.0 at DEEP_COMMIT") and
`LUNGE_DEPTH_SCALE`'s reference move with the edge.

Not taken: widening the window back to [2, 5] at closed measure (it would undo D4's swing-room rule,
which is grounded: a swing you cannot develop commits shallower); deleting the tier (the cut is free
today, but only because the tier is unreachable; the prototype shows it has work to do).

## Prototype reading (`pP_window.py`: `cfg` overlay `DEEP_COMMIT = LUNGE_COMMIT = 3.353`, no file touched)

| reading | as shipped | tier follows the window |
|---|---|---|
| exchanges at or above the deep edge | 1.0% | 32.5% |
| ripostes / binds / grapples per exchange | 14.7% / 5.7% / 18.1% | 16.4% / 6.0% / 27.5% |
| season-default mirror, A felled (control seeds) | 49.9% (52.1%) | 50.4% (50.1%) |
| turns, wounding blows, lead-change share | 3.36, 3.18, 34.1% | 3.25, 3.17, 34.3% |
| skill score 3 against 2, A felled | 34.8% | 37.6% |
| longsword against arming, A felled | 19.2% | 19.8% |
| rapier against longsword, unarmoured | 52.5% | 52.4% |
| **A's depth forced to 3.9 / 3.0 / 2.3, A felled** | **45.3 / 49.0 / 54.4** | **52.0 / 47.6 / 51.5** |
| disposition 7 against 4, and 1 against 4, A felled | 42.9%, 60.0% | 44.8%, 56.3% |

With the tier alive, the monotone advantage of depth is gone: the three forced depths read within 4.4
points of each other, the middle slightly best, both poles paying (the deep one by exposure to the
steal and the counter, the shallow one by attack σ). That is the trade `config.py:280-285` describes
("BOTH poles cost") and the engine did not have. The residual advantage of disposition 7 is the
initiative drift, which the PC addendum's F-PC-17 already isolates and proposal B there removes from
the approach.

## Exact edits, by owner

| file | edit |
|---|---|
| `modules/combat/config.py` | `DEEP_FRAC=2/3`, `LUNGE_FRAC=2/3` replace `DEEP_COMMIT`, `LUNGE_COMMIT` (the PC-15 comment block `:317-327` and `:290` restated; the dead-exported-key guard forbids leaving the old keys) |
| `modules/combat/combat_systems.py` | `deep_commit()` and `lunge_commit()` as above; `indes_steal_amount` centres on `deep_commit`; `commit_depth`'s docstring states the window as it is drawn |
| `modules/combat/wrapper.py` `:284`, `:285`, `:325`, `:387`, `:401` | read the two functions; no formula in the orchestrator |
| `systems/combat/combat_engine_v1/workbench/` | any reader of the two keys (`probabilities.py`, `narrate.py`) re-pointed `[grep at landing]` |
| `engine/engine_params/combat_engine_v1.json` | re-derived by the exporter |

## Gate (execution artifacts)

The probes were lane scratch (not in the repository). NEW `tests/valoria/test_combat_deep_commit.py`:
`test_deep_edge_equals_four_at_full_room` (byte-identity at `range_avail >= RANGE_COMMIT_PEAK`),
`test_deep_edge_follows_the_window`, `test_share_at_deep_edge_between_a_quarter_and_two_fifths` (gate 1),
`test_forced_depths_within_interval_after_change` (gate 2). Command:
`python -m pytest tests/valoria/test_combat_deep_commit.py -q -m combat`; gate 3 is the workbench
(`systems/combat/combat_engine_v1/workbench/balance.py`, the families named); gate 4 the exporter. Before editing, the
readers of the two old keys are found by `rg -n "DEEP_COMMIT|LUNGE_COMMIT" modules systems engine tests`.

1. The `pF_story.py` F3 reading, committed as gate 1's test: the share of exchanges at or above the deep edge is between a quarter and
   two fifths for every roster weapon.
2. The forced-depth reading re-run at n 3,000: no forced depth beats another by more than the interval
   of the difference in the season-default mirror; with `DEEP_FRAC` set so the edge returns to 4.0 the
   shipped monotone reading (45 / 49 / 54) returns.
3. The workbench's mirror, weapon, attribute and tradition families (`balance.winrate`) inside their
   pre-change intervals, or each mover named.
4. `python tools/export_engine_params.py --check` green; goldens re-recorded and said so.

## Falsifier

After the build, a fighter forced to the deepest in-window commit who is felled less often than one
forced to the middle by more than the interval; or fewer than one exchange in ten at the deep edge.

## NERS reading

- **N.** Bottom-up: five gates read a threshold the draw cannot reach. Top-down: the stated intent
  needs a lean that costs. Lateral: the same rule (a threshold lives in its quantity's range) is what
  ED-PC-0037 applied to the closed latch. Cut the tier instead and the counter, the Indes steal and the
  lunge go with it: the engine's answer to "what does commitment risk" becomes "nothing".
- **R.** Completeness at the extreme: at full room the tier is where it was.
- **S.** One owner for "deep"; the two keys that were equal by coincidence stay two facts.
- **E, last.** Two keys change meaning, two small functions, five call sites. High.

## Cost class

Small build, with a calibration re-record. Tier: `sonnet`, effort `high`. Hash movers declared: every world with a
fought scene (the batch's one re-record). Lands it: B15, order the two functions with `DEEP_FRAC`/`LUNGE_FRAC` (at
full room hash-equal) → the five call sites → the workbench readers → the exporter re-derive.
