# DICE — one score, two roles: what a person rolls is what he opposes with

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-11, C-U5a-12) — the one-read-two-roles rule stands. Changed by Jordan's answers: `score` is the **trained rank** (`max(untrained score, rank)`), with no attribute folded in (A-7; the `max(int(attr), int(have))` branch of Edit A goes, and the attribute is read separately as talent); what the opponent contributes is his **trained score** times `opposition_rate`, through `opposed_ob` (A-26, A-79; corrected from "his pool under the same pool rule" by W3-1 per D-U1-02), not `score / 2`. Edit C's values are U1 §5's: `lie: deception`, `determine: law` (each `none` with a note until SC's definition rows exist), `interrogate: inquiry`, `arrest: arms`, on the verb row's `capability:` column. The gate gains a row at an obstacle below `OB_MIN` (`U5a_DICE_owed_edits.md` §3 row 11). Figures quoted here are whole-dice figures at the old regime.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-04) — the `opposition_fallback` fixture is not added, and the sentence that a non-person subject is opposed at `obstacle_default` is superseded: opposition is never absent, and where nobody stands opposite the term is `opposed_ob(pool_default)` (`16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (a); `U5c_SC_one_obstacle_form.md` §2). `obstacle_default` is deleted.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — the body is brought to its two heads: rows applied: `R1_READ.md` 7b-6 and §2 rows (Edit A: training only, no attribute; Edit B: `_opposition_of` returns the trained score, no `opposition_fallback`; Edit C: U1 §5's values on the verb row's `capability:` column; "What it changes" restated on the one rule; the whole-dice `pool_default / 2` figures removed, one sentence naming the inversion kept), `U1_OWNERS_AND_VOCABULARY.md` D-U1-02 (the first head line's "his pool" corrected to "his trained score"), D-U1-08 (Edit D: `scores` and `addends`, carried by `U5b_PC_rulings_in_the_fight.md` §2), `U3_CONFLICT_LEDGER.md` C3-A3 (Edit A starts from implementation lane A's `pool.py::score` split, `c5bf18a`, with its `max(attr, have)` removed), `U5_CONFLICTS_U5c.md` C-04 (`obstacle_default` deleted; nobody opposite is `opposed_ob(pool_default, rate)`); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*); "key" (for a capability) → "capability" (glossary *capability*, *key*).

Reconciled: 2026-11-12, U6 repair lane R-C (`unified/U6_VERDICT_AND_REPAIRS.md` findings 4, 6): "The resolution" no longer says `obstacle_default` "keeps the job H-127 gives it"; it is deleted (C-04, the head above), and the E line follows; the remaining "key" for a capability (What it changes, problems 1 to 4, the falsifier) → "capability" or "capability rank"; "fallback" for the untrained score → "untrained score" (glossary *stand-in*, *untrained score*). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (10); "trained score/rank" → skill score (1); proposed names `talent_level` → `attribute_level`, `pool.py::talent` → `pool.py::governing_attribute` and test names (1); rewordings by sense (3: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

**Depends on:** `U5a_capability_home_and_two_inputs.md` Part A (B04); `29_DICE_one_opposed_rule_form_and_tuning.md` item 29-1 (`opposed_ob`, B04); `U5c_SC_one_obstacle_form.md` (B05); implementation lane A's branch rebased (B01, C3-A2).
**Lands in batch:** Edits A, B and C in B05 (`B05-one-roll`): A and C as OBS step 0 with CAP Part B (Edit A is CAP row B1, Edit B is CAP row B4), before OBS step 1a. *(U6 repair lane R-A, `U3_CONFLICT_LEDGER.md` C3-V1: this file is a declared mover and B04 is gated hash-EQUAL; this file's own line 83, CAP row B1, OBS's head and C3-A3 already said B05.)*

## Status: PROPOSED

Carries findings F-DICE-03 and F-DICE-04 (and bears on F-DICE-01 and F-DICE-02) of `../audits/10_DICE_audit.md`. Lanes that own the edited files:
IN (`engine/season/seam/wrappers/pool.py`, `sigma.py`, `engine/season/rosters.yaml`), with the content it
depends on in the character lane.

## What it changes in `engine/season/` at runtime

*(Reconciled, W3-1, 7b-6.)* It is a declared mover. A person is opposed at `opposition_rate × his skill
score` (`opposed_ob`, `29_DICE_one_opposed_rule_form_and_tuning.md`); a person who holds no skill the verb reads is opposed at
his untrained score, `pool_default`, by the same function; where nobody stands opposite, the term is
`opposed_ob(pool_default, opposition_rate)` (C-04; `obstacle_default` is deleted). The control arm
(`opposition_rate` 0.5, `pool_add` 0) is today's bytes. The defect this removes is the inversion: today a
person who holds no score is harder to move than one who holds a low one (problem 1). Every world hash that
grades a person-opposed roll moves at the live arm; the readings are `29_DICE`'s gates.

## The problem, with evidence

1. **Holding a score makes a person easier to oppose than holding none.** `sigma.py::_opposition_of`
   (`:117-137`) returns the larger of the held skill rank and the held attribute, or `None`; `roll.py::obstacle`
   (`:141`) halves a score and falls to `obstacle_default` on `None`. Probe (audit §12, E-07), pool 2: an
   unauthored subject → obstacle 2.0, Partial-or-better 26.00 %; a subject holding the skill at 2 → obstacle 1.0,
   58.00 %; a subject holding an attribute at 1 → obstacle 0.5, 73.50 %. The stand-in is worth a score of 4 while
   the same person rolls as a score of 2. `hole_register.yaml` H-127's `cite:` records this inversion as
   made live at B10-10 and unmeasured.
2. **The stand-in is being applied outside its stated scope.** H-127's own text: the derivation *"reads
   off a PERSON. A Record, a Rung or a Proposition has no corresponding score, and this row is the
   stand-in for that branch"*. A person subject with no skill the verb reads is a person, not that branch.
3. **Two readings of one quantity across modules.** `modules/combat/core.py:113-116` records it: a person
   holding no skill the verb reads *"is attacked at Ob 1.0 here and at `obstacle_default` in a social contest: two ladders
   for one quantity"*. Combat reads `faculty` (untrained score and practice included); the social roll reads
   neither.
4. **Four rolled verbs name no skill.** `rosters.yaml: verb_capability` maps nine verbs; `arrest`,
   `determine`, `interrogate` and `lie` roll through the social provider and are absent (audit §12, E-09),
   so their pool is `pool_default` and their opposition `None` for every pair. H-312 measured
   `interrogate` alone: skills and attributes set to 0 or 20 leave the odds at
   `(0.74, 0.19, 0.07, 0.0)`.

## The resolution, decided

Ladder step 3 (a ruling and a register row answer the form) with step 4 for the precedent. The ruling of
2026-08-14 (*"their corresponding score/2 plus whatever specific modifiers exist for them in that instance"*)
is overridden in its rate by A-26 and A-79 (`opposed_ob(skill score, opposition_rate)`); its form stands: a
person's corresponding score is the score he rolls: one read, two roles. Practice is excluded from the opposing role on
`_opposition_of`'s existing statement (*"the practice addend raises a pool, not an opposition"*), which
stands. `obstacle_default` is deleted with its fixture and H-127's row (C-04, `U5c_SC_one_obstacle_form.md`
§2): where nobody stands opposite, the term is the stand-in `opposed_ob(pool_default, opposition_rate)`. The
magnitude stays an `assumption`
(`pool_default`, H-126, swept 1 / 2 / 4): [ASSUMPTION; medium; Jordan to correct; revert: the control
arm below].

## The edits

**A. `engine/season/seam/wrappers/pool.py` (the one pool reader).** Split the base out of `faculty`; no
arithmetic moves:

```python
def score(w, p, verb) -> int:
    """(W3-1, A-7, 7b-6) What `p` is trained in for `verb`'s capability: the held rank, else the untrained
    score `pool_default`. No attribute (the governing attribute enters as levels) and no addend. The base of his pool AND the
    score an opponent's `opposed_ob` reads."""
    have = _capability(p, verb)
    return max(int(w.fixtures.get("pool_default")), int(have)) if have is not None else int(w.fixtures.get("pool_default"))

def faculty(w, p, verb) -> int:
    addends = sum(int(add(w, p, verb)) for add in POOL_ADDENDS)
    return pool_of(score(w, p, verb), addends, w.fixtures.get("pool_add"), w.fixtures.get("pool_floor"))
```

Implementation lane A's `c5bf18a` already split `score()` from the addends; B05 starts from it and removes its
`max(attr, have)` branch (C3-A3).

**B. `engine/season/seam/wrappers/sigma.py::_opposition_of`.** A person subject always has a score:

```python
if subject and subject in w.persons:
    return float(score(w, w.persons[subject], opposing_verb))   # the skill score (29 item 29-4 step 1);
                                                                # the skill the row's `opposed_by` names, else the verb's own
return None                                                     # nobody opposite: the module's stand-in,
                                                                # opposed_ob(pool_default, rate) (C-04)
```

*(W3-1, C-04:)* no `opposition_fallback` fixture is added and none of its hole-register row: the control arm is
`opposition_rate` 0.5 with `pool_add` 0. The attribute does not oppose (A-7: the governing attribute is a level on the
subject's side through the `edge` row `against`, `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3).
`believed_input` is unchanged: a believer still needs a claim, or takes the ordinary prior
(`10_DICE_believed_odds_have_a_prior.md`).

**C. The verb row's `capability:` column** (`engine/season/verb_table.yaml`; U1 §5, D-U1-07: the verb's
skill lives on its row, not in `rosters.yaml: verb_capability`). Four values: `interrogate: inquiry`,
`arrest: arms`; `lie: deception` and `determine: law`, each `capability: none` with a note until SC authors the
`deception` and `law` definition rows (lane A's interim `determine: argue` stands until then, D-U1-07). Each is
an `assumption` under H-126's existing sweep; H-312 closes on the `interrogate` row.

**D. `modules/combat/core.py::ob_from_defender` (PC lane, cross-listed, not edited here).** Once `score`
exists, `PersonalCombatInput` carries `scores` and `addends` raw in place of `faculties` (D-U1-08;
`U5b_PC_rulings_in_the_fight.md` §2), and the note at `core.py:113-116` is resolved by reading the score for
the obstacle (`opposed_ob`) and `pool_of(score, addends, …)` for the pool. That is the PC lane's edit and its
goldens; this proposal only supplies the reader.

## The gate (execution artifacts)

1. At the control arm (`opposition_rate` 0.5, `pool_add` 0; W3-1), `python -m engine.season.harness.headless
   --seasons 2 --seed 0` prints today's `CONTENT HASH`.
2. At the shipped arm, `python -m engine.season.harness.aperture 1 0`'s `DEGREES RESOLVED` line for
   `tell` is read before and after and reported, both arms, seeds 0 to 2 (a number with its control).
3. `engine/season/tests/test_odds_of.py` and `test_sc01_obstacle_ceiling.py`, re-pinned where they pin
   the old stand-in for a person.

## The falsifier

`odds_of` for a `tell` at an unauthored hearer must equal the odds at a hearer holding the skill at
`pool_default` (no inversion; W3-1: the whole-dice tuples of the first text are moot under A-5); a hearer
holding it at a higher rank must give lower odds. For `interrogate`, raising the subject's `inquiry` score must lower
Partial-or-better (H-312's probe, which today prints an unchanged tuple).

## NERS reading (E last)

- **N.** Cut the untrained-score read and persons differ in pool but an unauthored person stays twice as hard to
  move as an authored one; the inversion returns. Holds top-down (the ruling), lateral (combat already
  reads it this way) and bottom-up (one function).
- **R.** *Makes players feel they impact the world*: an unauthored opponent stops being the hardest one to
  move. Completeness: the inversion is an extreme where the composition breaks. (The first text's 74 % and
  42 % were whole-dice readings of the old regime, removed by W3-1.)
- **S.** One score read by the pool and the obstacle, in the social roll and (after D) in a fight.
- **E, as a ratio.** One function split in two, four verb-row values; one fixture (`obstacle_default`)
  deleted, its job taken by the stand-in every lane already uses (C-04).

## Cost class

Edit, with re-pins. A declared mover; the trajectory figures of gate 2 go in the commit body.

**Tests and lands (W3-1).** `engine/season/tests/test_odds_of.py` and `test_sc01_obstacle_ceiling.py`
(gate 3); new `engine/season/tests/test_odds_of.py::test_an_unauthored_hearer_is_not_harder_than_a_held_one`
(the falsifier) and `::test_score_reads_no_attribute`. Lands: an IN-lane implementation session under
`/methodology-execute` with CHAR and SC review; `sonnet`.
