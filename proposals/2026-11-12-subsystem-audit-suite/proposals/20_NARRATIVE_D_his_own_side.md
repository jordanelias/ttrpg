# NARRATIVE-D — his own side: a creed that stands for something, and a member who is asked what he thinks of it

Reconciled: 2026-11-12, U5d closure — folded **A-46**: edit 4 (held for Jordan) is ruled in its narrow form. `commitment.ended` joins a strand only when the released edge's object is a faction's creed Proposition or its `head_seat` (the Split is a move of the era); a routine release stays `never`. Step rewritten: the roster change is one content opener keyed on the released edge's object, not the move of `commitment.ended` from `never` to `joins`; the Status line's hold is discharged for that form and the wide form is not built. The strand it joins is one of several (A-45).

## Status: PROPOSED (edit 4, the strife kind list, is HELD for Jordan: it changes a ratified roster)

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-05 (allegiance is fixed and no stand can cross it), §2
edges A3, A5; §7.2 pull G2; evidence E-N13. Reference only (`CLAUDE.md` §0.05). Not ratified by being
written.

## What it changes in `engine/season/` at runtime

1. `world_q.engaged_poles(faction)` also returns the poles a faction's roster row declares. With no row
   declaring one (the first commit) every hash is EQUAL. Authoring four rows (the second commit) is a
   **declared mover**: `opinion_of` changes for every person who stands on a pole, and with it
   `opinion_referents` (the one consumer today).
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
signs). First content, `[ASSUMPTION; medium; Jordan to correct; revert: delete the key]`, each read off
what that faction's seated members stand for at build (E-N01), never from a document:

```yaml
"Church of Solmund":     {creed: {solmund_orthodoxy: 1}}        # 7 of 7 members
"Restoration Movement":  {creed: {einhir_restoration: 1}}       # 4 of 4
Varfell:                 {creed: {einhir_restoration: 1}}       # 5 of 5
Altonia:                 {creed: {altonian_civics: 1}}          # 3 of 3
```

The Crown, Hafenmark, the Guilds and the Löwenritter get none: their members stand on no common pole,
and inventing one would author a creed nobody wrote.

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
he already holds. **Stated limit, owed:** leaving is `release`, whose row forms on a plain referent
and whose stance sign is the wrong way round for an act that ends a tie (`20_NARRATIVE_C` edit 5, the
same owner). Until that lands this proposal gives a dissenter a voice and not yet a door.

**4. HELD — `rosters.yaml: strife_kinds`: `commitment.ended` from `never` to `joins`.** The ratified
kind list (`strife-01` §6, ED-IN-0316) files it as everyday life, which makes the study's two
defection links (`DA>WA`, `WN>DA`) unreachable (audit E-N03). The roster's own note gives the revert
for any one kind ("moving one kind between `opens` and `joins`"). It is a ratified roster; audit §10
item 2 gives the two options.

## The gate that shows it worked (execution artifacts)

1. Controls: no `creed:` key and `stamp_own_side False` reproduce the base hashes.
2. With the four rows: `opinion_of` for the four factions' members has a non-zero affiliation term
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
  hearer already forms of other factions) and diagonal (`20_NARRATIVE_A`'s regimes are these poles).
- **R.** No player: dissent inside the Church or the Crown arises from who was seated there. Complete:
  a faction with no pole and a person with no conviction read today's values.
- **S.** No new formula; the stamp is the eleventh of a family, with the family's dedup and control.
- **E, last.** Four data rows, two small functions, one fixture; against a mechanism (IN-70) that is
  built and unread on its most interesting input. Good, and bounded by the `release` limit it states.

## Cost class

Edit (1 to 3). Edit 4 waits on Jordan.

## Dependency edges

- **Needs:** nothing to build; reads better after `20_NARRATIVE_A` (the same poles decide credit).
- **FA:** `06_FA_war_lives_in_seats_B.md` and CR-88 (a member who has argued and lost is the person
  whose betrayal band matters); FA F-FA-16 (five factions have no head, so the regard term is empty
  for them).
- **CHAR:** `02_CHAR_goal_lean_on_its_own_question.md` (the creed's pull on a verb is the other half
  of allegiance; no collision: that is a score term, this is an occasion).
- **INSTITUTIONS:** `15_INSTITUTIONS_PAPACY_A_ground.md` (what the Church stands on) should own the
  Church's row once it lands.
- **VERBS-BINDING / CHAR:** `release`'s referent and sign.
