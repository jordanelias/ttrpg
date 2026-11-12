# DICE — one score, two roles: what a person rolls is what he opposes with

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-11, C-U5a-12) — the one-read-two-roles rule stands. Changed by Jordan's answers: `score` is the **trained rank** (`max(untrained score, rank)`), with no attribute folded in (A-7; the `max(int(attr), int(have))` branch of Edit A goes, and the attribute is read separately as talent); what the opponent contributes is his **pool** under the same pool rule times `opposition_rate` (A-6, A-26), not `score / 2`. Edit C's values are U1 §5's: `lie: deception`, `determine: law` (each `none` with a note until SC's definition rows exist), `interrogate: inquiry`, `arrest: arms`, on the verb row's `capability:` column. The gate gains a row at an obstacle below `OB_MIN` (`U5a_DICE_owed_edits.md` §3 row 11). Figures quoted here are whole-dice figures at the old regime.

## Status: PROPOSED

Carries findings F-DICE-03 and F-DICE-04 (and bears on F-DICE-01 and F-DICE-02) of `../audits/10_DICE_audit.md`. Lanes that own the edited files:
IN (`engine/season/seam/wrappers/pool.py`, `sigma.py`, `engine/season/rosters.yaml`), with the content it
depends on in the character lane.

## What it changes in `engine/season/` at runtime

It is a declared mover. A contested social act against a **person** who holds no capability key and no
attribute is opposed at `pool_default / 2` (shipped: 1.0) instead of at `obstacle_default` (shipped: 2.0).
At the shipped pair that takes Partial-or-better from 26.00 % to 58.00 % and Success-or-better from 7.00 %
to 26.00 % for `tell`, `lie`, `argue`, `speak` against a person, and for `arrest`, `determine` and
`interrogate` once they name a key. A non-person subject (a Record, a Rung, a Proposition) is opposed at
`obstacle_default`, as today. Every world hash that grades a person-opposed roll moves; the control arm
that reproduces today's bytes is stated below.

## The problem, with evidence

1. **Holding a score makes a person easier to oppose than holding none.** `sigma.py::_opposition_of`
   (`:117-137`) returns the larger of the held key and the held attribute, or `None`; `roll.py::obstacle`
   (`:141`) halves a score and falls to `obstacle_default` on `None`. Probe (audit §12, E-07), pool 2: an
   unauthored subject → Ob 2.0, Partial-or-better 26.00 %; a subject holding the key at 2 → Ob 1.0,
   58.00 %; a subject holding an attribute at 1 → Ob 0.5, 73.50 %. The stand-in is worth a score of 4 while
   the same person rolls as a score of 2. `hole_register.yaml` H-127's `cite:` records this inversion as
   made live at B10-10 and unmeasured.
2. **The stand-in is being applied outside its stated scope.** H-127's own text: the derivation *"reads
   off a PERSON. A Record, a Rung or a Proposition has no corresponding score, and this row is the
   stand-in for that branch"*. A person subject with no key is a person, not that branch.
3. **Two readings of one quantity across modules.** `modules/combat/core.py:113-116` records it: a person
   holding no key *"is attacked at Ob 1.0 here and at `obstacle_default` in a social contest: two ladders
   for one quantity"*. Combat reads `faculty` (fallback and practice included); the social roll reads
   neither.
4. **Four rolled verbs name no key.** `rosters.yaml: verb_capability` maps nine verbs; `arrest`,
   `determine`, `interrogate` and `lie` roll through the social provider and are absent (audit §12, E-09),
   so their pool is `pool_default` and their opposition `None` for every pair. H-312 measured
   `interrogate` alone: capabilities and attributes set to 0 or 20 leave the odds at
   `(0.74, 0.19, 0.07, 0.0)`.

## The resolution, decided

Ladder step 3 (a ruling and a register row answer the form) with step 4 for the precedent. The ruling
(Jordan, 2026-08-14, carried in `dice_engine.degree_from_net`'s docstring) is *"their corresponding
score/2 plus whatever specific modifiers exist for them in that instance"*. A person's corresponding
score is the score he rolls: one read, two roles. Practice is excluded from the opposing role on
`_opposition_of`'s existing statement (*"the practice addend raises a pool, not an opposition"*), which
stands. `obstacle_default` keeps the job H-127 gives it. The magnitude stays an `assumption`
(`pool_default`, H-126, swept 1 / 2 / 4): [ASSUMPTION; medium; Jordan to correct; revert: the control
arm below].

## The edits

**A. `engine/season/seam/wrappers/pool.py` (the one pool reader).** Split the base out of `faculty`; no
arithmetic moves:

```python
def score(w, p, verb) -> int:
    """What `p` holds for `verb`'s vocation: the larger of the held key and the vocation's attribute,
    else `pool_default`. The base of his pool AND the score an opponent halves. No addend."""
    have, attr = _capability(p, verb), _authored_attribute(p, verb)
    if attr is not None:
        return int(attr) if have is None else max(int(attr), int(have))
    return int(have if have is not None else w.fixtures.get("pool_default"))

def faculty(w, p, verb) -> int:
    return score(w, p, verb) + sum(int(add(w, p, verb)) for add in POOL_ADDENDS)
```

**B. `engine/season/seam/wrappers/sigma.py::_opposition_of`.** A person subject always has a score:

```python
if subject and subject in w.persons:
    person = w.persons[subject]
    opposing = _opposing_attribute(person, verb)          # CR-96's `opposed_by`, unchanged
    base = score(w, person, verb)
    return float(max(base, opposing) if opposing is not None else base)
return None                                               # not a person: the module's stand-in
```

A new fixture `opposition_fallback` with arms `score` (SHIPPED) and `stand_in` (the control: return `None`
where the person holds neither, today's bytes) carries the switch; it gets its hole-register row beside
H-127 with the two arms as its sweep. `believed_input` is unchanged: a believer still needs a claim.

**C. `engine/season/rosters.yaml: verb_capability`.** Four rows, each on a vocation that already exists
(so `VOCATIONS` and `train`'s candidate count do not grow): `lie: copying` (the same act as `tell`, one of
them false), `interrogate: inquiry`, `arrest: arms`, `determine: argue`. Each is an `assumption` under
H-126's existing sweep; H-312 closes on the `interrogate` row.

**D. `modules/combat/core.py::ob_from_defender` (PC lane, cross-listed, not edited here).** Once `score`
exists, `PersonalCombatInput` can carry it beside `faculties`, and the note at `core.py:113-116` is
resolved by reading `score` for the Ob and `faculty` for the pool. That is the PC lane's edit and its
goldens; this proposal only supplies the reader.

## The gate (execution artifacts)

1. At `opposition_fallback = stand_in`, `python -m engine.season.harness.headless --seasons 2 --seed 0`
   prints today's `CONTENT HASH` (the control).
2. At the shipped arm, `python -m engine.season.harness.aperture 1 0`'s `DEGREES RESOLVED` line for
   `tell` is read before and after and reported, both arms, seeds 0 to 2 (a number with its control).
3. `engine/season/tests/test_odds_of.py` and `test_sc01_obstacle_ceiling.py`, re-pinned where they pin
   the old stand-in for a person.

## The falsifier

`odds_of` for a `tell` at an unauthored hearer must equal `band_odds(2, 1.0)`; for a hearer holding the
key at 2 it must be the same tuple (no inversion); for a Record subject it must stay `band_odds(2, 2.0)`.
For `interrogate`, raising the subject's `inquiry` score must lower Partial-or-better (H-312's probe,
which today prints an unchanged tuple).

## NERS reading (E last)

- **N.** Cut the fallback read and persons differ in pool but an unauthored person stays twice as hard to
  move as an authored one; the inversion returns. Holds top-down (the ruling), lateral (combat already
  reads it this way) and bottom-up (one function).
- **R.** *Makes players feel they impact the world*: the shipped default person-to-person roll fails 74 %
  of the time and Failure writes nothing; at the ruled derivation it fails 42 %. Completeness: the
  inversion is an extreme where the composition breaks.
- **S.** One score read by the pool and the obstacle, in the social roll and (after D) in a fight.
- **E, as a ratio.** One function split in two, one fixture, four roster rows; one stand-in's scope
  narrowed to what its register row says it is.

## Cost class

Edit, with re-pins. A declared mover; the trajectory figures of gate 2 go in the commit body.
