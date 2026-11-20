# NARRATIVE-D — his own side: a creed that stands for something, and a member who is asked what he thinks of it

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. (1) **"A defection that makes the next easier"** is declared as LOOP row L10 (`30_WR_D_momentum_and_its_brakes.md` §2): after a member leaves, `opinion_of`'s third mean is taken over who is left, and this file's own-side stamp puts the creed on the next member's table. Its sign is **unmeasured** (if those who leave were disliked, the mean rises and the path damps); census shape E-08 and the fork lift (`30_WR_E` §3, clause C7) read which, with `stamp_own_side` off as the control. No term is added here. (2) **A regime is not a faction**: a faction that holds two creed sets among its members is read by `30_WR_B` commit 2; this file's `creed:` row is what a faction professes, and that reading is what its members hold. (3) **The schism**: an A-46 move by the holder of a seat whose institution covers the realm opens the era condition `schism` (`30_WR_A` commit 4) and is chain K-5. (4) A-83: what a member is *expected* to do by those around him is `30_WR_G` commit 5 and is separate from what he thinks of his side.

Reconciled: 2026-11-12, U5d closure — folded **A-46**: edit 4 (held for Jordan) is ruled in its narrow form. `commitment.ended` joins a strand only when the released edge's object is a faction's creed Proposition or its `head_seat` (the Split is a move of the era); a routine release stays `never`. Step rewritten: the roster change is one content opener keyed on the released edge's object, not the move of `commitment.ended` from `never` to `joins`; the Status line's hold is discharged for that form and the wide form is not built. The strand it joins is one of several (A-45).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row his_own_side (the key CONFORMS; content and owner AMBIGUOUS), §2 rows Status/edit 4 (A-46) and edit 1 content (A-87 to A-90), §7, 7b; `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` commit 4; `unified/U1_GLOSSARY.md` "creed", "regime"; `unified/U3_DEPENDENCY_ORDER.md` §1 item 38, §3.1). The body now follows the head. Changed: (1) the Status line's hold is removed (A-46 ruled the narrow form); (2) edit 1's four-row content block and the sentence giving the Crown, Hafenmark, the Guilds and the Löwenritter no creed are struck: Jordan has authored the houses' and the Church's stances (A-87 to A-90), and the `creed:` values are `31_WR_A` commit 4's rows (one owner); this file keeps the key, its loader and the readers; (3) edit 4 is rewritten to the narrow form; (4) edit 3's `release` limit points at its decided owner (`20_NARRATIVE_C` edit 5); (5) tests named; (6) dependency, batch and tier lines. One sentence for the R3 lane: `31_WR_A`'s commit table row 4 calls its content "EQUAL until `20_NARRATIVE_D` commit 2's reader ships"; with this rewrite the reader is this file's commit 1 and the content is `31_WR_A` commit 4, which is therefore the declared mover.

Depends on: `20_NARRATIVE_A_stands_for.md` (B38; the same poles decide credit); `20_NARRATIVE_C_who_holds_what.md` (B38); `30_WR_D_momentum_and_its_brakes.md` (B38; LOOP row L10); `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` commit 4 (B38; the `creed:` values, landing after this file's commit 1).
Lands in batch: B38 (lane WR / FA), after `20_NARRATIVE_C` and before `31_WR_A` commit 4.
Tier: sonnet / high; the content is `31_WR_A`'s.

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-05 (allegiance is fixed and no stand can cross it), §2
edges A3, A5; §7.2 pull G2; evidence E-N13. Reference only (`CLAUDE.md` §0.05). Not ratified by being
written.

## What it changes in `engine/season/` at runtime

1. `world_q.engaged_poles(faction)` also returns the poles a faction's roster row declares. With no row
   declaring one (this file's first commit) every hash is EQUAL. The rows' content is
   `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` commit 4, which is the **declared mover**:
   `opinion_of` changes for every person who stands on a pole, and with it `opinion_referents` (the one
   consumer today).
2. `questions_for` stamps one more standing occasion: the creed Proposition of the person's **own**
   faction, when his opinion of that faction is below indifference. Behind `Fixtures stamp_own_side`
   (`False` the control, EQUAL; `True` a declared mover).

No verb, Event kind, carrier or score term is added.

## The problem, with evidence

- `world_q.opinion_of` (`:3029-3063`, v9 IN-70) computes what a person thinks of a faction from three
  means on `[-1, +1]`: how his pursuits sit with what it expects, how his convictions sit with the poles
  its goals engage, and how he regards its head and the members whose deeds he holds.
- Its one caller, `opinion_referents` (`:3113`), asks it of the faction of a deed's *doer*. Nothing asks
  it of the person's own faction.
- `engaged_poles` reads only goal rows of the form `deed_doers … engaging:`; 2 of 38 rows have it, both
  the Church's (`einhir_restoration`, −1). For the other eight factions the conviction term is 0 by
  construction. The function's own `[ASSUMPTION]`: "The creed engages no pole: it names a leader, not an
  affiliation … revert: the creed's engagement … joins the pairs."
- Read on `build_realm(0)` (E-N13): 4 of 43 members hold an opinion of their own faction below 0; 27 of
  43 rate some other faction above their own. Over three seeds and four seasons, persons whose
  `faction_of` changed: 0 / 0 / 0; `commit` edges to a faction opened or closed in play: 0.
- At "stands for" (`20_NARRATIVE_A`, E-N01) the cast's convictions follow its factions exactly where the
  design says they should: Church 7 of 7 `solmund_orthodoxy`, Restoration 4 of 4 and Varfell 5 of 5
  `einhir_restoration`, Altonia 3 of 3 `altonian_civics`; and the Crown's faction holds 2 orthodox and 1
  Restoration member among 11. The data says what four creeds stand for. No code reads it.

## The resolution, decided

**A faction's creed declares the poles it stands on, as data on the faction's own row; and a member
whose opinion of his own side has fallen below indifference finds that side's creed among his
occasions.** What he does with it (argue, stay, go) is his sampled choice among the rows that form on a
Proposition, each resolved by its own draw. Nobody is expelled or converted by a number.

Ladder: step 4 for the data (`rosters.yaml: factions.head_seat`, CR-86, is the precedent: one authored
structural fact per faction row, read through one query, key-free); step 3 for the reading (IN-70's
ruled formula, unchanged); step 4 for the stamp (`propositions_heard`, CR-28: a Proposition stamped as
a classed referent, `commit` and `argue` form on it).

## Exact edits, by owner

**1. `engine/season/rosters.yaml: factions` — an optional key `creed:` on a faction row,**
`{<affiliation>: -1 | 1}` (sign only, the `affiliation_engagement` cells' own rule), loaded and refused
by `data/rosters.py` beside `head_seat` (an affiliation outside `AFFILIATIONS`, a value outside the two
signs). **This file writes no content.** The values are
`31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` commit 4 (each sign the sign of that house's
regime core, A-87 to A-90; it contains the four rows this file once read off E-N01 and gives Valorsmark
and Hafenmark the creed Jordan has now stated); one owner of the content, this file the owner of the key
and its reader.

**2. `engine/season/queries/world_q.py::engaged_poles`** (`:3013-3026`): the returned tuple is the
goal pairs as today, then the faction row's `creed` pairs not already present, in roster order. The
docstring's `[ASSUMPTION] … revert` sentence is replaced by the rule and its new revert.

**3. `engine/season/queries/world_q.py` — a stamp term, and its splice in `questions_for`.**

```python
def own_side(w: World, p: Person) -> tuple:
    """THE CREED OF `p`'S OWN FACTION, as a standing occasion, when his opinion of it
    (`opinion_of`) is below indifference: `(faction Proposition id,)`, else `()`. World-first,
    resolver-side, like every stamp term; `()` for a person in no faction."""
```

appended to `added` after `propositions_heard(w, p)` (`:4265`), read only when `Fixtures
stamp_own_side` is on. The class is `Proposition` (`World.class_of`), so the rows that declare it form:
`argue` (he takes it up with his own side) and `commit`, which `held_edge_declines` declines on a cause
he already holds. **Stated limit:** leaving is `release`, whose row forms on a plain referent; its
stance sign, once the wrong way round for an act that ends a tie, is decided at its owner
(`20_NARRATIVE_C` edit 5: `regard_sign: -1` in `02_CHAR_scar_cap_and_regard_unit.md`'s Addendum). Until
that Addendum's row values land this proposal gives a dissenter a voice and not yet a door.

**4. `rosters.yaml: strife_kinds` — the narrow form A-46 rules.** The ratified kind list (`strife-01` §6,
ED-IN-0316) files `commitment.ended` as everyday life, which makes the study's two defection links
(`DA>WA`, `WN>DA`) unreachable (audit E-N03). A-46 (B, narrow): only leaving a faction's creed or its
head seat is a move of the era. The edit is one content entry keyed on the released edge's object:
`commitment.ended` joins a strand when the released edge's object is a faction's creed Proposition or
its `head_seat` (`rosters.yaml: factions.head_seat`); every other `commitment.ended` stays `never`.
[ASSUMPTION: the qualifier's key name (`object_of: [creed_proposition, head_seat]` on the entry) is the
strand roster owner's (`09_WR_strand_conclusion.md`, `30_WR_C`) to fix at landing — basis: no qualified
entry exists in the roster today.] The wide form (the kind moved from `never` to `joins`) is not built.
Gate: a planted release of a commit to a creed Proposition joins a strand; a planted routine release
does not.

## The gate that shows it worked (execution artifacts)

Tests: NEW `engine/season/tests/test_own_side.py`: `test_no_creed_key_reproduces_base` (gate 1),
`test_creed_gives_the_conviction_term_a_nonzero_value` (gate 2, on planted rows),
`test_rename_every_faction_and_no_reading_moves` (gate 4),
`test_stamp_own_side_forms_argue_on_the_creed_proposition` (gate 3, planted),
`test_routine_release_does_not_join_a_strand_and_a_creed_release_does` (edit 4), and
`test_creed_value_outside_two_signs_is_refused_at_load`.

1. Controls: no `creed:` key and `stamp_own_side False` reproduce the base hashes.
2. With `31_WR_A` commit 4's rows: `opinion_of` for the four factions' members has a non-zero affiliation term
   (print `person_q.opinion_terms`' second value); the count of members whose opinion of their own side
   is below 0 is reported per faction and is not the same number for every faction.
3. `stamp_own_side True`, seeds 0 to 2, four seasons: executed `argue` acts whose subject is the
   actor's own creed: above zero at two seeds; the control arm: zero.
4. Rename falsifier (the plan's): rename every faction id and name consistently and no reading moves;
   move one member's convictions and his row follows.
5. `20_NARRATIVE_F` class G2 above zero at two seeds; under the `noconv` arm (convictions cleared) the
   conviction share of G2 is zero and the pursuit share remains.

## The falsifier

Gate 3 at zero with the stamp on: `argue` on one's own creed is refused or outranked every time (then
the finding is the row's, SC's), or no member falls below indifference in play (then opinion does not
move, which is CHAR F-CHAR-03 again, measured from this side).

## NERS reading

- **N.** Cut it and a faction is a list: what its members think of it is computed and thrown away, and
  the realm's one authored doctrinal split (inside the Crown's own party) can never surface. It holds
  top-down (a faction with a creed), bottom-up (one member's doubt), lateral (the same `opinion` the
  hearer already forms of other factions) and diagonal (`20_NARRATIVE_A`'s reading of what a person
  stands for is read on these poles).
- **R.** No player: dissent inside the Church or the Crown arises from who was seated there. Complete:
  a faction with no pole and a person with no conviction read today's values.
- **S.** No new formula; the stamp is the eleventh of a family, with the family's dedup and control.
- **E, last.** One key, two small functions, one fixture (the rows are `31_WR_A`'s); against a mechanism
  (IN-70) that is built and unread on its most interesting input. Good, and bounded by the `release`
  limit it states.

## Cost class

Edit (1 to 4).

## Dependency edges

- **Needs:** nothing to build first beyond the head's B38 order; reads better after `20_NARRATIVE_A`
  (the same poles decide credit). Content: `31_WR_A` commit 4.
- **FA:** `06_FA_war_lives_in_seats_B.md` and CR-88 (a member who has argued and lost is the person
  whose betrayal band matters); FA F-FA-16 (five factions have no head, so the regard term is empty
  for them).
- **CHAR:** `02_CHAR_goal_lean_on_its_own_question.md` (the creed's pull on a verb is the other half
  of allegiance; no collision: that is a score term, this is an occasion).
- **INSTITUTIONS:** `15_INSTITUTIONS_PAPACY_A_ground.md` (what the Church stands on) should own the
  Church's row once it lands.
- **VERBS-BINDING / CHAR:** `release`'s referent and sign.
