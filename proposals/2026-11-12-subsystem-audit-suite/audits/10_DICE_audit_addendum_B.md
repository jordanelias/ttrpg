# DICE — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 618ec4b (working tree; the first audit was read at 601e715)

Addendum to `10_DICE_audit.md`. It does not edit that file or its five proposals. It covers what that
audit reported as unread, closes H-152 by a run, corrects the first audit where a second reading or a
probe shows it wrong, and writes the capability → axiom → resolver input map as a proposal
(`../proposals/10_DICE_capability_axiom_map.md`). Finding numbers continue from `F-DICE-14`.

## 0. Verdict on the first audit

The first audit's verdict stands and is sharpened: the dice engine is sound and is fed a constant.
What the first audit did not see, because it had not read `derived_stats_v30.md` and its sources, is
that the constant is not only a missing content switch. The design's capability model (attribute
doubled plus History plus three, floor five; derived resources that drain; a wound as a fraction of an
obstacle) and the season's built model (the score is the pool; the opponent's score halved is the
obstacle; a modifier is a named sigma level) are two different sets of RPG axioms, each internally
coherent, and the tree runs three of them at once: the season's, personal combat's, and mass battle's.
The sections below state each, by code, and the proposal names one authoring surface over them.

(Sections 1 to 6 follow; this head was written before the reading finished, per the brief.)
