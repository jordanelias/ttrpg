# MB · CR-12 decided by the ladder: numbers leave the melee dice, after the instrument can read it

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three notes; the decision and its order stand. (1) **D-35 is held** in the decision record; `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` R-8 adjudicates it as this file decides (numbers leave the melee dice), and the plan's hold "for Jordan" points there until he confirms. (2) **A-5**: the pool this file makes a function of troop quality is drawn on the one sampler (`U5b_MB_rulings_in_the_field.md` §1); step 2's one base-term function is where that lands. (3) Step 3 is not sufficient alone: `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edits 2 to 4 are what it must contain and the PARTITION row its exit gains (measured: step 3 alone leaves three bodies on one body's cells at 2 wins of 60). The whole is one step of the field calibration batch (`U5b_MB_rulings_in_the_field.md` §6 row 4).

## Status: PROPOSED

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (row R-8). Nothing here is deleted; the decision gains three supports from outside the tree, none of which is the reason it is correct (`CLAUDE.md` §0.05). The linear law is the one stated for hand-to-hand fighting, where "one soldier could only ever fight exactly one other soldier at a time" (`research/historical/mass_battle_casualties_and_results_grounding.md` D8, tool-read). Depth and numbers alone did not win Roman battles; fresh men and frontage did (same note D3, read at the page). Sabin's own board game caps how many units may attack from a zone, so numbers act through frontage (`research/historical/mass_battle_wargame_models_grounding.md` L5). No source read gives a win probability by force ratio, so the locked bar of 1.4 has no historical counterpart to be checked against; `26_MASS_BATTLE_calibration_targets.md` T-9 reads the ordering only.

Lane MB. Carries R-06 of `audits/04_MB_audit.md` §6.2; listed in that audit's §11 because it narrows the
plain words of a standing directive. Supersedes nothing in `proposals/2026-11-08-cr12-melee-attrition-design.md`
except its §4 conclusion that the question must go to Jordan. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing until its third step is built. Then: who wins a field between unequal armies at army scale (a
declared hash mover wherever a field is fought; in natural play today, nowhere).

## The problem

The 2026-11-08 design measured melee at exponent 1.50 and 1.70 against a locked bar of 1.4, located the
term correctly, found by probe that only removing troop numbers from the melee pool reaches the bar, and
stopped to ask Jordan to choose between two of his directives. `HANDOFF_MB.md` and
`workplans/valoria_master_workplan_v11_part3.md` (CR-12) now hold it for a ruling.

## The resolution, decided: option (a)

**Numbers leave the melee dice.** By the ladder, in order:

1. *Superseded.* `ED-MB-0045`'s superseding row (`registers/editorial_ledger_mb_archive.jsonl:73`,
   2026-10-01, `needs_jordan: false`) was written with the pool-quality model already shipped
   (2026-07-08) and decides: the engine "deviates from the Jordan-locked linear melee law ... `CLAUDE.md`
   §0.05 says change the code ... the wait is now on engine work, no longer on a ruling." The later row
   governs. The design's probes established what that change costs; they did not reopen it.
2. *Answered by precedent in the code.* The 2026-07-08 directive's contrast is the commander ("abandon
   combat pools being related to the commander"). Under (a) the exchange is still derived from troop
   type, quality and numbers: numbers act through the frontage term (`core/attrition.py`) and through how
   long a body lasts. `config.py`'s 2026-06-02 block made this trade before, in the same words.

Checked against the code: the three channels the design names are there (`core/attrition.py:41`, body-average
density; `core/exchange.py:124` and `:184-185`, numbers in the pool; `orchestration.py:1308-1309`, the
opposed degree). A fourth it does not name is removed by the same fix: `resolution._sigma_net_boost`
scales every sigma modifier by the square root of the pool (`resolution.py:230`).

## Exact edits, in this order

**Step 1, the instrument (`systems/mass_battle/sim/lanchester_signature.py`). No engine change.**

- The volley scenario must stay out of melee for the whole no-rout trajectory. The design counted 3,455
  of 4,015 trajectory ticks resolving a melee pair. Give the scenario a standoff the kite band holds for
  160 ticks (a wider field or a `hold` screen in front of each archer body), and make the check assert
  it: zero melee pairs in the trajectory, else the row reads INVALID, not PASS.
- The exponent fit must be able to tell a linear law with a frontage edge from a super-linear one. The
  design's synthetic control (an exactly linear law with a 7:5 column edge reads 1.30 to 1.45) is added
  to the instrument as a row that must read "linear": either fit `A^p - c B^p` with `c` free, or
  normalise each side's loss rate by its engaged columns before fitting.
- Bisect LINEAR 4:1 from 77% (`ED-MB-0045`, 2026-10-08) to 52% (`aa6871b8`) and record the commit and
  cause in `ED-MB-0045`'s next row. This is the reading a season feels; the flip cannot pass without it.

**Step 2, consolidation (hash equal).** One function in `core/exchange.py` returns the pool's base term;
`subunit_combat_pool` calls it; `Unit.base_combat_pool` goes with the multi-unit harness code
(proposal `04_MB_typed_outcome_and_one_path.md`), calling the same function.

**Step 3, the fix.** In that one function the melee base is `eff_power x REFERENCE_SIZE x
POOL_QUALITY_SCALE`, `REFERENCE_SIZE` a named `config` constant (the design's probe E used 4);
`pair_pool_contribution` still splits by engaged share. Re-read `POOL_QUALITY_SCALE` and the 4:1 band on
the repaired instrument. The stale comment at `resolve_engagements` ("numbers-in-contact lives ONLY here
under Lanchester") becomes true and stays.

## Gate

The repaired instrument, both `PER_CELL` arms, Python 3.11 with `PYTHONHASHSEED=0`: LINEAR in band;
melee exponent at or below 1.4 with an identifiable fit; volley at or above 1.6 with zero melee pairs;
NO-ANNIHILATION passing; the frontage control reading linear; the planted collapse
(`MB_FRICTION_SIGMA=4`) still failing LINEAR. The CI flip is proposed in the PR body, not made.

## Falsifier

After step 1 and before step 3, a keep-numbers variant that passes the repaired instrument on both arms.
If one exists the stop un-fires and (a) is unnecessary; the design's nine probes found none on the
unrepaired instrument, which is the reason step 1 comes first.

## NERS

- **N.** Bottom-up: the linear law is what a frontage-limited melee is; top-down: under it a smaller army
  can hold a line, so depth, reserves and ground become decisions. Under (b) size alone decides and those
  decisions are removed.
- **R.** A commander can think about where to stand, not only how many to bring.
- **S.** One methodology: numbers enter melee once, where the volley term already enters once.
- **E, last.** One base term, one constant, one function where there were two.

## Cost class

Design-first for step 1 (an instrument repair with a judgment in it), edit for step 2, small build with
re-calibration for step 3.

## Sequencing

After `04_MB_headcount_grade_and_scale.md`. The exponent is measured over 160-tick no-rout trajectories,
a regime no season field enters; nothing a player or an arc needs waits on it.
