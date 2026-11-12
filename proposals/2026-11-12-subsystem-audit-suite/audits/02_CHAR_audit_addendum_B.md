# CHAR — adversarial steelman audit, addendum B: the full design reading

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: ad07a9a (working tree)

This addendum does not replace `02_CHAR_audit.md`; it reads what that audit lists as NOT READ (its §12,
last paragraph) and corrects, confirms or extends it. Finding numbers continue from F-CHAR-15. Section
numbers here are the addendum's own (B1 to B7); where a section answers one of the first audit's, it
says which. `.designs/` and `.audit/` are ARCHIVED-NOT-CANON: cited below as referents for intent,
vocabulary and history, never as the reason a behaviour is correct (`CLAUDE.md` §0.05).

## B0. Verdict of the addendum

(written at the end of the reading; see the foot of this section once filled)

## B1. What was read

(appended as the reading proceeds; the final table is at the end of this section)

### B1.1 The `challenge` row, settled

The first audit's F-CHAR-07 says `challenge` does not carry the `individual` conjunct and marks the
claim as inferred. Opened at `engine/season/verb_table.yaml:923-949`: `requires_typed.all` holds three
conjuncts, `existence` of `subject` (`kind: Person`), `relation` of `subject` `with`, and `relation` of
`subject` `dispute` (v11 CR-87). There is no `individual` conjunct on either party, where `fight`
(`:749-752`), `capture` (`:883-886`) and `accept` (`:976-979`) each carry two. **The claim holds.** A
cohort is a `Person`, so `existence … kind: Person` admits it on both sides. Two things the first audit
did not have: (i) `with` and `dispute` are both WORLD-ONLY by the row's own note, so the challenger
*"forms the Candidate on anyone he knows and the fold refuses a challenge with no wrong behind it"*:
the row is itself the largest single producer of F-CHAR-05's refusals; (ii) the row's `writes_note`
states that the minted challenge Record *"reaches the challenged only by a `give`"*, `give` is
unreached in the realm (H-229), *"so in computed play a challenge mints and no `accept` forms on it"*.
The duel pair is therefore closed at both ends for a computed person: most challenges are refused, and
one that mints is never answered.
