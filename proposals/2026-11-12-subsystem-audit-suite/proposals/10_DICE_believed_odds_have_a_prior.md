# DICE — a person who cannot say the odds assumes an ordinary opponent, not a certain win

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
   `determine` (0.26, 0.4346, 0.5765: the default pair at effort 0, 1, 2); `None` 3,813 times for
   `march` and 1,014 for `accept` (another module's prize; no believed mode exists for a fight or a
   field, `sigma.py:383-388`).
2. **`None` reads as certainty.** `decision/choose.py::odds_weight`: *"`return 1.0 if chance is None`"*.
   A person who knows nothing about an opponent weighs the act as if it could not fail; a person who
   knows a little weighs it down. Ignorance is rewarded.
3. **The figure that is returned is the same for everyone.** All 102 values are the default pair's; no
   person holds a capability claim about another (`sigma.py:234-238`: *"NOTHING DEPOSITS ONE TODAY"*),
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

**D. The record of a roll, for a reason trail** (CORE's carrier; the dice lane states what exists).
The provider already returns the whole record. The cheapest carrier is one optional field on the first
Event a graded act emits, `roll: (pool, ob, leverage, net, settled_margin)`, filled from
`Resolution.result` where it holds a `net`/`ob` pair. It enters `World.content_hash` and so moves every
hash once; it is proposed to CORE and not built here.

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

Edit (A, B), a declared mover. C and D are design-first in the lanes named.
