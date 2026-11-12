# DICE — a person who cannot say the odds assumes an ordinary opponent, not a certain win

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — stands. Under A-5 `band_odds` is the closed form of the one sampler (same name and signature); the prior for a stranger is an ordinary person's pool and mid-point talent (U1 architecture §4). Edit D (the roll's record on its Event) is one proposal with `10_DICE_capability_axiom_map.md` §D's `fed_by` and SC's `Margin.terms`; under A-5 the record carries the continuous margin, not a settled integer.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U1_OWNERS_AND_VOCABULARY.md` D-U1-06 / U1 §4 R-30 / `U3_CONFLICT_LEDGER.md` C3-L5 (Edit D is **withdrawn**: no `Event.roll` field; the roll's record rides the act's Resolution and reason trail, `fed_by`, `terms`, `levels`, and where a reader needs it witnessed its parts go on `Event.observed` as `observation_terms` members; the persistence of a social roll's terms lands with `05_SC_contest_record_on_event.md` in B05; `R1_READ.md` §1.3's AMBIGUOUS row answered), `R1_READ.md` §2 row A-5 (`settled_margin` struck: there is no settled margin), §1.3 (Edit A's prior reaches the obstacle through `opposed_ob`, A-79, `29_DICE` item 29-4 step 3), §6 (problem 1's figures are whole-dice readings of the old regime); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`).

**Depends on:** `10_DICE_one_score_two_roles.md` (B05: the opposing role reads the skill score); `29_DICE_one_opposed_rule_form_and_tuning.md` item 29-4 (B05); `10_DICE_advantage_sources_for_the_arcs.md` (B05, before it).
**Lands in batch:** B05 (`B05-one-roll`, IN), after `10_DICE_advantage_sources_for_the_arcs.md`; Edit C's believed estimates land with `U5b_PC_residue.md` §8 (B14) and `U5b_MB_residue.md` §5.

## Status: PROPOSED

Carries finding F-DICE-14 and §15 of `../audits/10_DICE_audit.md`. Lane: IN (the seam's believed-odds
query); cross-listed to CHAR (the chooser that reads it, and the claims that would inform it) and CORE
(the record of a roll on its Event).

## What it changes in `engine/season/` at runtime

It is a declared mover at the shipped arm. Today the chooser multiplies a contested candidate's pursuit
term by the person's believed chance and, where he cannot say, by 1.0. After this edit, where the only
unknown is the score of a person he holds no claim about, he assumes that person is ordinary (the score
an unauthored person rolls, `pool_default`) and gets a figure. Candidates for `argue` and `arrest`
against a stranger are then weighted by a believed chance below 1; rankings that include them can move,
and so can world hashes. The control arm (`believed_prior = none`) is today's bytes. Rolls themselves
do not change: this is the person's estimate, never the dealt odds.

## The problem, with evidence

1. **The chooser's odds query answers for one verb.** Realm, seed 0, one season, the query spied at
   `sigma.py::believed_chance` (audit §12, E-19): asked 4,929 times; a figure 102 times, all for
   `determine` (0.26, 0.4346, 0.5765: the default pair at effort 0, 1, 2; whole-dice readings of the regime
   before A-5, W3-1); `None` 3,813 times for
   `march` and 1,014 for `accept` (another module's prize; no believed mode exists for a fight or a
   field, `sigma.py:383-388`).
2. **`None` reads as certainty.** `decision/choose.py::odds_weight`: *"`return 1.0 if chance is None`"*.
   A person who knows nothing about an opponent weighs the act as if it could not fail; a person who
   knows a little weighs it down. Ignorance is rewarded.
3. **The figure that is returned is the same for everyone.** All 102 values are the default pair's; no
   person holds a skill claim about another (`sigma.py:234-238`: *"NOTHING DEPOSITS ONE TODAY"*),
   so a believed opposition for a person subject is always unknown, and `believed_input` returns `None`
   (`:286-289`).
4. **Nothing of the roll survives it but the band.** `Event` carries `id, kind, changes, causes,
   emitted_at, degree` (`state/carriers.py:270-275`). The provider's record (`pool`, `ob`, `net`,
   `leverage`, `settled_margin`, `sigma.py:554-555`) is dropped at the fold, so no later reader can say
   why an act failed.

## The resolution, decided

Ladder step 4 for the prior: the tree already decides what an unauthored person is worth
(`pool.py::faculty`'s fallback, and after `10_DICE_one_score_two_roles.md` the opposing role too). A
person who holds no claim about another believes what the engine itself assumes of someone it knows
nothing about. That is his own prior, read from the fixtures and never from the World, so the
person-side rule (no `World` in `decision/`; AX-2) is kept. Ladder step 5 for the rest: an examined
Record's forgery quality and a room he has no estimate of stay unknown (`None`), because no prior for
them exists in the tree and inventing one would be a number nobody chose.

The believed estimate of a fight or a field is not built here: both estimators sample the true World
(`sigma.py:379-391`), and a believed form needs believed inputs (the enemy's strength as he holds it),
which is the character and mass-battle lanes' design. What this lane states is the interface (below).

## The edits

**A. `engine/season/seam/wrappers/sigma.py::believed_input`** (`:283-291`):

```python
if person_subject and key and subject != p.id:
    held = [c for c in p.ledger if c.subject == subject and c.predicate == CAPABILITY_CLAIM + key]
    if held:
        opposition = float(max(held, key=lambda c: (c.when, c.round, c.confidence)).value)
    elif fx.get("believed_prior") == "ordinary":
        opposition = float(fx.get("pool_default"))      # a stranger is taken for an ordinary person
    else:
        return None                                     # the control: he cannot say
```

*(W3-1, A-79:)* `opposition` is a **score**, and the believed obstacle composes it as the dealt one does,
`opposed_ob(opposition, opposition_rate)` (`29_DICE_one_opposed_rule_form_and_tuning.md` item 29-4 step 3:
`opposition if not None else pool_default`), never as a pool.

**B. `engine/season/data/fixtures.py`**: `believed_prior`, arms `none` (control) / `ordinary` (SHIPPED),
with its hole-register row beside H-248, graded `assumption`. [ASSUMPTION; medium; Jordan to correct;
revert: `believed_prior` `none`.]

**C. The interface for a provider's believed estimate** (stated for the holistic stage; no code here).
A provider that registers `@provider("estimate", <name>)` for the player's display may register a
second role, `believed_estimate`, with the signature
`(holder: Person, act: Act, fixtures) -> tuple of shares over that provider's own bands, or None`,
reading the holder's ledger and nothing of the World. `believed_chance` then asks the prize row's
provider instead of falling through to the social roll, and `odds_weight` is unchanged: it sums the
shares of the bands the verb writes in.

**D. The record of a roll, for a reason trail.** *(Reconciled, W3-1: withdrawn by D-U1-06 and C3-L5.)* The
first text proposed one optional `Event.roll: (pool, ob, leverage, net, settled_margin)` field; there is no
settled margin under A-5, and no new Event field is added. The roll's record is the provider's returned
record with its `fed_by` reason trail (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8, U1 §4 R-30) and the
obstacle's named `terms`; its persistence for a social roll is `05_SC_contest_record_on_event.md`'s (B05);
a part that must be witnessed rides `Event.observed` as an `observation_terms` member.

## The gate (execution artifacts)

1. `believed_prior = none`: `python -m engine.season.harness.headless --seasons 2 --seed 0` prints
   today's `CONTENT HASH`.
2. The spy of E-19 re-run at the shipped arm: `believed_chance` returns a figure for `argue` and
   `arrest` candidates against a person; the counts by verb are reported for both arms.
3. `engine/season/tests/test_odds_of.py::test_mode_b_with_no_claim_on_the_opposition_is_none_never_a_figure`
   is re-stated for the control arm and gains its twin for the shipped one.

## The falsifier

For a believer who holds no claim about his opponent, mode (b) must equal `band_odds(pool,
obstacle(opposition = pool_default))`, and must differ from mode (a) whenever the opponent's true score
is not `pool_default`. If mode (b) ever equals mode (a) for an opponent whose score the believer was
never told, the query has read the World.

## NERS reading (E last)

- **N.** Cut the prior and the believed-odds term discriminates between nothing but the effort variants
  of one verb, and ignorance of an opponent reads as certainty. Tested person-side (no World read),
  lateral (the same query serves a seated player's callback and an NPC), and with no player present.
- **R.** *Decisions must not be omniscient and perfectly rational*: he is wrong about a strong stranger
  in a way that is his own, and corrected only by being told. That is a source of error with a cause
  the narrative can name.
- **S.** One assumption about an unknown person, used by the pool, the obstacle and the belief.
- **E, as a ratio.** Three lines and one fixture against a branch that returned `None`.

## Cost class

Edit (A, B), a declared mover. C is design-first in the lanes named; D is withdrawn.

**Tests and lands (W3-1).** `engine/season/tests/test_odds_of.py` (exists): the gate-3 twin
`test_mode_b_with_no_claim_uses_the_ordinary_prior_at_the_shipped_arm`, and the falsifier as
`test_mode_b_never_equals_mode_a_for_an_untold_strong_opponent`. Lands: an IN-lane implementation session
under `/methodology-execute` with CHAR review; edit class, `sonnet`.
