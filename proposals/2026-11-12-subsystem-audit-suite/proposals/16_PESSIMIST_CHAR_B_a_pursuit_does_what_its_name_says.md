# CHAR (pessimist) B — a pursuit does what its name says: signatures for the fifteen, rows for the verbs of mercy and harm

## Status: PROPOSED

Written by the CHAR pessimist lane (`audits/16_PESSIMIST_CHAR.md`, F-PES-CHAR-01). Ratifies nothing;
reference under `CLAUDE.md` §0.05. It leaves the ruled basis alone (fifteen pursuits on seven bipolar
axes, ED-IN-0261) and supplies what that basis has never had: a statement, in data, of what each name
must mean in acts, and a reading that shows whether the two invented tables deliver it.

## What this changes in `engine/season/` at runtime

Step 1 (the signatures and the reading) changes nothing: a new roster key no chooser reads and a new
flag on an existing harness. Step 2 (cells) is a declared mover: every score that reads a re-authored
row moves, and every golden under it re-records. Step 3 (the loader's refusal) changes nothing at
runtime once step 2 has made it pass.

## The problem, with evidence

The pursuit term is `Σ_axis project(p)[axis] · align(verb, axis)` (`decision/choose.py:215`): the
product of `rosters.yaml: tables.pursuit_projection` (pursuit × axis) and `tables.alignment` (verb ×
axis). H-66 records the alignment table as invented and swept. Nobody has read the product against the
names. `a0_words.py` and `c1_two_men.py` (c), seed 0:

| a man who holds only… | tops, among 66 verbs by lean | tops in the live candidate set (276 readings) | is scarred on it by witnessing (sign test) |
|---|---|---|---|
| `love` | `evade / defy`, `destroy_record`, `forge`, `construe` | **`forge` 266** | `give`, `restore`, `speak`, `utter`, `found`, and 18 more |
| `justice` | `commit`, `evade / defy`, `destroy_record` | `utter` 266 | **30 verbs**, among them `open_case`, `petition`, `convene`, `restore`, `research` |
| `family` | `requisition`, `confer`, `forge` | **`forge` 266** | `build`, `found`, `speak`, `release` |
| `wealth` | `construe`, `forge`, `migrate`, `march` | **`forge` 266** | `give`, `restore`, `research`, `commit` (not `seize`, not `raze`) |
| `reputation` | `march`, `construe`, `forge` | **`forge` 266** | `give`, `commit`, `oblige`, `utter` |
| `scholastics` | `determine`, `open_case`, `transfer`, `migrate`, `exchange` | `exchange` 266 | `build`, `found`, `speak`, `utter` (`research` is not in its top five) |
| `community` | `create_record`, `succeed`, `research` | `create_record` 266 | `build`, `found`, `work`, `speak`, `establish` |
| `stewardship` | `petition`, `requisition`, `confer` | `create_record` 248 | `build`, `found`, `work`, `establish` |
| `honour` | `fight`, `accept`, `commit`, `confer`, `challenge` | `challenge` 260 | `lie`, `forge`, `evade / defy` (and `build`, `work`, `move`) |

Honour reads as honour. Almost nothing else reads as its name: a man of love forges, a just man is
wounded by the sight of a petition, a steward is wounded by building. Four of fifteen pursuits put
`forge` at the top of what their holder would actually do.

Two causes, both measured (`a1_norms.py`):

1. **Twenty-five of 66 resolvable verbs have no alignment cell at all**, and they are the verbs a
   character is known by: `forgive`, `pardon`, `tend`, `arrest`, `capture`, `raze`, `sabotage`,
   `conceal`, `tell`, `train`, `argue`, `interrogate`, `covenant`, `surrender`, `recruit`. No pursuit can
   tell who forgives from who razes; only the stance term can, and it reads a relation, not a character.
2. **The seven axes describe the manner of an act, and the names promise an end.** Scaling every verb
   row to unit length (direction only) does not repair it: `love` still tops `destroy_record` and
   `forge`, `justice` still tops `surveil` and `destroy_record`, `community` and `stewardship` still
   oppose `build`. The loud rows (`construe` 1.26, `evade / defy` 1.24, `determine` 1.17,
   `destroy_record` 1.08, `forge` 0.94) take the top place for 7 of 15 pursuits as shipped, but the
   defect is the cells, not the scale.

The scar inherits the same product through its sign test (`person_q._pursuits_violated_by`), which is
why every person is scarred on a median of 13 of 19 elements (addendum F-CHAR-17), and why the acts
that wound a holder of `love` are gifts.

## The resolution, decided

Ladder step 3: ED-IN-0261 rules the basis, so the basis stays and the content is repaired against a
stated target. Step 5 for the mechanism: a name is a fact (`CLAUDE.md` §0.05, *"a term, a roster, a
closed set and a bound are facts exactly as a number is"*), so what a name must mean lives where code
reads it.

**Step 1. Signatures, as data, and the reading.**

```yaml
# engine/season/rosters.yaml, beside tables.pursuit_projection
pursuit_signatures:              # what the NAME must mean in acts: a floor, not the whole character
  # [ASSUMPTION; medium; Jordan to correct: every row is content]
  love:        {favours: [give, tend, forgive],          opposes: [sabotage, raze, forge]}
  justice:     {favours: [open_case, determine, petition], opposes: [forge, lie, conceal]}
  family:      {favours: [give, tend, succeed],           opposes: [migrate, sabotage]}
  wealth:      {favours: [exchange, work, requisition],   opposes: [give, raze]}
  reputation:  {favours: [challenge, speak, utter],       opposes: [conceal, evade / defy]}
  scholastics: {favours: [research, examine, reconstruct], opposes: [destroy_record, raze]}
  community:   {favours: [build, found, convene],         opposes: [raze, migrate]}
  stewardship: {favours: [build, restore, work],          opposes: [raze, sabotage]}
  honour:      {favours: [challenge, accept, commit],     opposes: [lie, forge, evade / defy]}
  liberty:     {favours: [evade / defy, release, migrate], opposes: [comply, arrest, capture]}
  stability:   {favours: [restore, comply, create_record], opposes: [raze, evade / defy]}
  virtue:      {favours: [give, forgive, pardon],         opposes: [lie, forge, sabotage]}
  doctrine:    {favours: [utter, commit, oblige],         opposes: [forge, destroy_record]}
  happiness:   {favours: [give, release, tend],           opposes: [fight, arrest]}
  individuality: {favours: [evade / defy, found, migrate], opposes: [comply, oblige]}
```

- Loader: `data/pursuits.py` loads it, refuses a pursuit off the roster and a verb off `VERB_TABLE`
  (the existing roster-membership refusal), and exposes `signature_breaks()`: for each pursuit, the
  favoured verbs whose `person_q.pursuit_lean` is not above zero, the opposed verbs whose lean is not
  below zero, and any opposed verb that out-leans a favoured one. It composes on `pursuit_lean`, the one
  owner of the dot; it is a reader and refuses nothing yet.
- Reading: `python -m engine.season.harness.conviction_spread --words` prints `signature_breaks()` and,
  per pursuit, the five highest and lowest verbs and the violated set (the body of `a0_words.py`). It is
  a flag on the instrument that already reads the projection, not a new instrument.
- Today's count against the starting set above (`a2_sig.py`, the same arithmetic run by hand): 13 of
  15 signatures break, on 35 clauses; `honour` and `individuality` hold. Twelve signatures name a verb
  with no row. Among the breaks that are not a missing row: `love` leans toward `forge` (+0.43) and
  against `give` (−0.02); `justice` leans against `petition` (−0.16); `community` against `build`
  (−0.18) and `found` (−0.27); `stewardship` against `build` (−0.12); `reputation` against `utter`
  (−0.21).

**Step 2. The cells** (Jordan's content, design-first; the lane states the order, not the values).
First the rows for the uncelled verbs a signature names (`forgive`, `pardon`, `tend`, `arrest`,
`capture`, `raze`, `sabotage`, `conceal`, `examine`), then the cells of the five loud rows, each change
read back through `--words`. A cell is authored in `tables.alignment` and nowhere else; no pursuit ×
verb override is added, because that would be a second owner of the lean.

**Step 3. The refusal.** When `signature_breaks()` is empty, `data/pursuits.py` raises at import on a
non-empty answer, as `data/rosters.py` already does for a roster's own invariants. This is a loader's
refusal for one data family (`CLAUDE.md` §0.05), load-bearing on the game: the table decides what every
person does.

**What it deliberately is not.** It does not make a pursuit read what an act would do to a particular
thing (the settlement, the heir): that is `02_CHAR_goal_lean_on_its_own_question.md` and `goal_stages`.
It does not touch the scar's rate or stock (`02_CHAR_scar_is_a_wound.md`); it removes the scar's
nonsense triggers at their source.

## Gate (an execution artifact)

1. Step 1: `conviction_spread --words` runs and reports the breaks; the realm hash at seed 0 after two
   seasons is `bacd687f` (unchanged).
2. Step 2: breaks = 0; then `c1_two_men.py` (c) repeated: no pursuit's single-pursuit holder tops a verb
   its signature opposes in any reading, and at most two pursuits share a top verb (today four share
   `forge` and three `utter`).
3. The scar's sign test, re-read: no favoured verb of a pursuit is in that pursuit's violated set
   (today `give` wounds `love`).

## Falsifier

If, with breaks at zero, single-pursuit holders still top the same verb for four or more pursuits in
the live candidate set, the names are satisfied on paper and the realm still forges: the stance term or
the candidate set is deciding, and the repair belongs to F-CHAR-01 and F-CHAR-08, not here.

## NERS reading (E last)

- **N.** Cut the pursuit term (`d1_cuts.py`, arm `nopursuit`, audit §2): the realm's mix of acts moves
  (total variation 0.37), a person's conduct moves 0.64 against 0.49 for merely re-rolling the dice, and
  more happens to persons, not less (stance moved for 7 and body for 13, against 0 and 0 shipped). The
  term is necessary to which verbs are taken and not yet to anything a player could name; the
  signatures are what would make the cut cost something sayable (*the loving stop giving*).
- **R.** Customisation is the stake: a designer who sets `love: 0.9` on a character must get a
  character who gives and tends. Today he gets a forger, and cannot find out why without reading two
  tables' product.
- **S.** One dot, one owner; the signature is checked through the same `pursuit_lean` the chooser and
  the scar read, so the three cannot disagree.
- **E.** Fifteen rows of two short lists buy legibility for 15 × 7 + 41 × 7 cells that nobody could
  audit by eye. *"Intuit complex outcomes from simple choices"* is exactly what a name is for.

## Cost class

Step 1: edit (one roster key, one reader, one flag). Step 2: design-first content (the cells are
Jordan's). Step 3: edit.

## Dependencies

None for step 1. Step 2 re-records every golden that plays a season; say so in its commit
(`CLAUDE.md` §7).
