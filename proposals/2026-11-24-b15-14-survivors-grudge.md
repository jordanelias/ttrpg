# B15.14: the survivor's grudge, the cause and the one repair

## Status: PROPOSED

Item: B15.14 (CP-T03-06), `workplans/valoria_master_workplan_v12_part18.md` lines 317-329. The BUILD is
held for a later batch, on this design's merge. This file explains a judgment about readings that already
exist. It is reference, as `CLAUDE.md` §0.05 defines the term. The code is the mechanism.

## The reading (tree `083cece`, `PYTHONHASHSEED=0`, `build_realm(s)`, 2 seasons, seeds 0-2)

**Before-reading** (`@eb34324f`, quoted, not re-taken): "0 of 4 survivors' regard reached a Candidate";
"no doer attributed … in 3 of 4".

**This reading.** It used a scratch driver that wraps the chooser as `harness/aperture.py::instrumented_season`
does, and left the hash unmoved: the seed-0 one-season hash reads `d104cdf014d05cde87d2987a75c34170`. The
driver found 14 survivors with a Wounded band. Two died before the end. That leaves 12 checked:

- **3 are yielders from `accept` duels. The other 9 are wounded parties from `capture`.**
- **Fight-caused regard is zero in 8 of 12.** Fight-caused regard is `regard(S, O)` minus the same regard
  computed without the fight's claims. In these 8 cases S's ledger attributes no doer to his own
  `body.changed` claim (`deed_doer` returns `None`).
- **Fight-caused regard is about -0.07 in 4 of 12** (-0.068 to -0.075, roughly 2% of CR-87's -3 bar). In
  each of these, S is a `capture` patient and the doer is attributed.
  - 2 of the 4 reached a Candidate on O: `challenge`, with a stance term of +0.08 to +0.14.
  - 0 of the 4 held to the end. Regard toward O ends positive (+0.007 to +0.055), because O's other deeds
    outweigh the fight.
- **Eviction was seen in 0 of 12.** At the season's end, every survivor still holds the fight's claims.
- **Where the total regard is negative, reaches a Candidate and holds** (5 of 12), the fight contributes
  exactly 0. The total there is carried by O's other deeds (`record.created`, `petition.filed`, ...).
  These 5 cases do not show a grudge from the fight.

**Positive control.** For every checked survivor, a stored row `(O, -4.0, 1.0)` was planted on the World
person at his first deliberation after the fight. Results:

- Regard read about -4 and held to the end in all planted survivors.
- `forgive` removed none of the planted rows in two seasons.
- The planted regard reached a Candidate on O for 9 of the 11 planted survivors alive at the end, across
  seeds 0 and 1 (`challenge`/`capture`, stance term +8 to +17).

So the instrument does see a grudge when one exists.

**Verdict: the zero-or-fading side. CP-T03-06 is not cut. The cause is "no doer attributed".**

## The cause, taken apart (the 8 no-doer survivors)

| mechanism (`queries/person_q.py::deed_doer`) | n | cases |
|---|---|---|
| S is the act's **actor**. His own sighting names *him* as `who` of his own wound, so the pairing names nobody. This is the limit B14.16 closed for a felled actor's death only. | 3 | s1 `accept` 4c49 (p_npc_006); s1 `capture` 37ab and s2 5976 (p_npc_013) |
| S holds the right sighting (`who` = O, `contested_physical`), but S was seen acting in the same stratum in that lap. The struck-and-struck guard then fires. | 2 | s0 c074, s1 692e (p_npc_033, both `accept` yielders) |
| S holds no sighting on himself in that lap at all. The shipped `observation_deposit_mode: actor` gives an act's reads to its actor alone. | 3 | s1 4c49 (p_npc_033), s1 37ab (p_npc_004), s2 5976 (p_npc_034) |

## The one edit: B14.16's hand, carried from the death to the wound

The edit composes on the existing owner, which is B14.16's `fell_to_hand`. The `person.died` claim already
reads it first, before both the pairing and the guard. The edit has three touch points, built in two stages (the Phase critic's change (a)):

**Stage 1 (touch points 1 and 2; repairs mechanism 1, the 3 actor cases, with no deposit change: a wounded actor already
receives his own Event's `observed` under `observation_deposit_mode: actor`).**

1. **Mint.** `loop/effects_combat.py::hand_observed` mints `(pid, fell_to_hand, <the other party>)` for every
   party whose band is Wounded or Felled in a two-party fight. Today it does so only for a felled actor. ⚠ This
   changes the value `hand_observed` mints today: today's value is the `prevailed` party; the new value is "the
   other party" of the two (the same man in a two-party fight whose loser is the wounded one, a different man where
   the wounded party prevailed). The predicate keeps the name `fell_to_hand` for a Wounded party only if the
   glossary row is widened to "who struck him"; otherwise a new predicate name is owed (CLAUDE.md §4: a word must
   land on its meaning for a reader with no memory of this repo, and a man who did not fall did not "fall to a hand").
2. **Read.** `deed_doer` reads the hand for `body.changed` exactly as it does for `person.died`, returning the
   OPPONENT (the party who struck him), not the subject.

**Stage 2 (touch point 3, taken ONLY if the Stage 1 re-measure still leaves non-actor patients without a doer; it
repairs mechanisms 2 and 3, the 5 other cases, and mechanism 2's two yielders only if they hold the hand).**

3. **Deposit.** A `fell_to_hand` Observation reaches its own subject, the wounded party, who stands in the scene and
   is alive. This changes the shipped rule "the act's actor alone" (`observation_deposit_mode: actor`, H-122), the
   knowledge-model choice `@eb34324f` declined. Its scope is stated before it is built: either a general rule
   (every Observation about a party reaches that party) or a predicate-specific exception inside the general rule
   (shape divergence); the design for Stage 2 names which, and a predicate-specific exception is not taken without a
   ruling. The larger step is justified only by a Stage 1 residue that Stage 1 cannot reach.

What dies:

- the actor-only restriction in `hand_observed`;
- the guard's reach over a wound whose hand is held;
- the stored `combat_grudge` row, which is never built.

**Gate.** Re-run this reading on seeds 0-2 (`aperture 2 s`, 2 seasons). The doer must be attributed in at
least 11 of the 12 checked survivors (the one survivor of slack is the "holds no sighting at all" case a Stage 1
re-measure may leave, and is why Stage 2 exists; a re-measure that reaches 12 of 12 at Stage 1 needs no Stage 2). The fight-caused regard must be non-zero wherever it is attributed.
Hash: a declared mover, re-pinned once with the diff shown (§7).

**Falsifiers (each must be able to fail).**
- Stage 1: a hand-built two-party `capture` in which the actor is the only wounded party. Before the edit,
  `deed_doer` on his `body.changed` claim returns `None`; after it, the call returns his OPPONENT.
- Stage 1: a struck-and-struck yielder (both parties wounded in one lap, the shape of mechanism 2). The guard no
  longer silences a wound whose hand is held: `deed_doer` returns the opponent for each party.
- Stage 2: a NON-ACTOR wounded patient (mechanism 3): before the deposit change he holds no sighting on himself and
  `deed_doer` returns `None`; after it, the call returns his opponent. This one observes the deposit rule, which the
  first falsifier cannot.
Each is a game-state test in the combat lane (or the season lane, where it drives a season act).

**Then the item's EXIT applies again.** If the repaired fight-caused regard reaches a Candidate and holds,
CUT applies. If it is still outweighed at about -0.07, the cause is the `body.changed` deed's lean
magnitude. That is neither of the entry's two causes, and it is a separate ruling. This design does not
take that ruling.

## NERS cut test (`CLAUDE.md` §0.06)

**The cut proposed:** never build the stored `combat_grudge` row. The grudge lives only in `regard`'s
`judged` term.

- **S.** A stored row beside `judged` would be two ladders for one quantity: how S regards O for what O did.
  That is the S defect "calculations consistent in methodology", even if each ladder were correct. The
  field scale already writes stored faction rows (`effects_combat.py::_casualties`). That is a different
  referent (a faction) and is left alone. Repairing attribution keeps person-to-person regard on a single
  ladder.
- **R.** Today a wounded actor and a struck-back yielder are judged as patients by nobody. A fight then
  leaves nothing behind for the world to generate drama from, so the mechanism is incomplete at an
  extreme. The repair closes that case. Whether it then makes a grudge is the gate's question, and it is
  not assumed here.
- **N.** Without the repair, the fight is invisible in 8 of 12 survivors' regard, and R-07 ("a fight leaves
  what the world keeps of it") is unmet. Measured against R and S, the repair is necessary. The stored row
  is not.
- **E,** as a ratio against N and R. The repair adds no new quantity and no new reader. It widens the
  predicate set of one existing read and the reach of one existing Observation, so the player reads
  "he hurt me" through the same regard every other deed moves.
