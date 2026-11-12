# 07 · SE — a capability's rate on an untested act, on the suite's one capability surface (supersedes two sections of `07_SE_capability_and_chooser_surface.md`)

Reconciled: 2026-11-12, U5d closure — folded **A-54** and **A-12** against one row of the audit addendum's §6 that this file implements ("stewardship … No passive bonus from a holder to his domain's yield … declined"). Overruled: A-54 rules that a steward's skill bears on the harvest draw. The form: the steward (the holder of the seat whose rung is the place's treasury rung) contributes to the **pool** of the place's seasonal draw through `rate(person, work)`; it is a term in a draw, not a multiplier on a fixed yield, so the place can still fail under a good steward. A seat's own modifier (A-12) enters the same draw through the one obstacle composer. `rate`'s form (`about_mid` on `faculty`) and the row declaration (`magnitude: rate`) are unchanged; the two inputs to a roll are `U5a_capability_home_and_two_inputs.md`'s.

## Status: PROPOSED

Carries finding F-SE-21 and resolution R-SE-32 of `audits/07_SE_audit_addendum_B.md` (its §6). It
supersedes **only** §3 (the interface) and §4 (the roster rows and the `capability_rate` table) of
`proposals/07_SE_capability_and_chooser_surface.md`; that proposal's §5 (the NPC and chooser points) and
§6 (the axioms) stand. It adds no capability system: it states what the settlement layer needs of the
surface the CORE, CHAR and DICE lanes proposed, and the one licence it asks of them. Nothing is ratified
by being written.

## 1. What changes in `engine/season/` at runtime

With the shipped data: nothing. No verb row names a capability with a rate, so every factor is exactly 1
and every hash is the base. When a designer authors one, a person who holds it raises a fabric (and, when
CP-T08-01 lands, works a Site) faster than one who does not, by one closed form shared with every other
capability factor in the game.

## 2. The problem, with evidence

- **The first lane's edit would be refused at load.** It adds `restore`, `work` and `build` to
  `rosters.yaml: verb_capability`. `proposals/01_CORE_capability_authoring_surface.md` Edit 4 deletes
  that roster in favour of a `capability:` column on the verb's own row, and its Edit 3 has the loader
  refuse *"a `capability:` on a row that neither contests nor is graded (a column nothing reads)"*. All
  three settlement rows are uncontested and ungraded (`verb_table.yaml`: `stratum:
  uncontested_material` on `transfer`; no settlement verb declares `contests:`, first audit §14).
- **It adds a second ladder.** Its `capability_rate.rates` maps a held score to a per-mille by its own
  table. `proposals/02_CHAR_capability_uses_table.md` already defines how a held value becomes a factor,
  in a closed set of two forms implemented once beside the attribute scale (`about_mid`: 1 at the
  scale's mid-point, monotone; `at_least`: a gate). `audits/10_DICE_audit.md` §14 (c) already defines
  the score: `score(person, verb)`, today `seam/wrappers/pool.py::faculty`. Two methods for one quantity
  is the S defect `CLAUDE.md` §0.06 names.
- **The need is real.** No settlement outcome reads a capability, and `_rise`'s `f(degree)` is the
  identity (`loop/effects_economy.py:121-129`, H-164): first audit §14, unchanged.

## 3. The resolution, decided

**One licence, one form, one score.** Ladder step 4 (the other lanes' surface is the precedent).

1. **The verb row declares it.** A row may carry `capability: <id>` if it contests, is graded, **or
   declares `magnitude: rate`**. The third licence is the only change asked of the CORE proposal's loader
   rule. A row with `magnitude: rate` and no `capability:` is refused; a `capability:` on an uncontested
   row without `magnitude: rate` is refused as that proposal already says.
2. **The factor is `about_mid`.** `rate(person, verb) = about_mid(score(person, verb), floor, ceiling,
   gain)`, with `floor` and `ceiling` from the capability's own row in the CORE block and `gain` one
   fixture, `effect_rate_gain`, shipped 0. No per-capability table. `[UNVERIFIED: that `about_mid`
   returns exactly 1 at gain 0. The CHAR proposal ships its own new use at gain 0 and calls the hash
   EQUAL, which requires it; the function is not yet written.]`
3. **No capability named is exactly 1.** A row that names none, and a person who holds none on a row
   that names one, are different facts: the first has no rate; the second has the score the DICE
   interface gives a non-holder (the untrained default). The DICE audit's point that unskilled use is
   indistinguishable from the default is not repaired here; it is inherited and named.
4. **What a rate may not be** (the DICE audit's exclusions, restated for an effect): not a bonus to a
   net, not a change of obstacle, not a gate on attempting. It scales the magnitude of an effect that
   already happens, and never past the effect's own ceiling.

## 4. The exact edits, by owner

**(a) `engine/season/data/verbs.py` (the CORE proposal's Edit 3, amended).** `VerbRow` gains
`magnitude: str = ""` with the closed set `("", "rate")`; the refusal rule becomes: `capability:` is
allowed when the row `contests`, is graded, or has `magnitude == "rate"`.

**(b) `engine/season/verb_table.yaml`.** No row is edited by this proposal. When Jordan authors the
capability, the rows `restore`, `work`, `build` (and `craft`, CP-T08-04) gain `capability: <its id>` and
`magnitude: rate`. Names are his content.

**(c) `engine/season/seam/wrappers/pool.py`**, beside `faculty` (the one pool reader):

```python
def rate(w, p, verb) -> Fraction:
    """The factor a held capability gives an untested effect of `verb`. Fraction(1) where the row
    declares no `magnitude: rate`, where `p` is None, and at `effect_rate_gain` 0."""
    row = VERB_TABLE[verb]
    if p is None or row.magnitude != "rate":
        return Fraction(1)
    cap = descriptors.capability(row.capability)
    return about_mid(faculty(w, p, verb), cap.floor, cap.ceiling, w.fixtures.get("effect_rate_gain"))
```

`about_mid` and `descriptors.capability` are the CHAR and CORE proposals'. `[UNVERIFIED: `about_mid`'s
return type; the CHAR proposal gives its signature and says it returns a factor. If it returns a float,
`rate` converts at this one site so the effect's integer arithmetic stays exact.]`

**(d) `engine/season/loop/effects_economy.py::_rise` and `_fall`.**

Old: `return (headroom * num) // den`

New: `r = rate(w, w.persons.get(a.actor), a.verb); return min(headroom, (headroom * num * r.numerator) // (den * r.denominator))`

The `min` keeps the ceiling a bound. H-164's row narrows: `f(degree)` is answered by `rate` for the
uncontested case.

**(e) CP-T08-01's `labour(w, rung)`** (planned): each present person's hands are weighted by
`rate(w, p, "work")`. A cohort is a `Person`, so a cohort row that carries a capability
(`cohorts.yaml`, through the cast surface of the CORE proposal's Edit 5, which validates
`capabilities:` on any cast row) makes a mining people mine better than a farming people set to the same
seam. Shipped: no cohort row carries one, so every weight is 1.

**(f) Nothing in `modules/settlements/`.** A rate is a host read of a person; the module's inputs carry
the factor it already has (`ProduceInput.factor`, under CP-T08-01).

## 5. What a capability definition must say for the settlement layer to use it

Its id; its kind and scale (the CORE block's fields); its growth rule; and, on the verb rows it serves,
`capability:` with `magnitude: rate`. Nothing else, and the settlement layer reads none of it except
through `rate`.

**Declined, with the reason.** A passive rate from a seat holder onto his domain's yield (the *domain
turn* of the tradition). A yield that changes with who sits over it is a quantity moving with no act,
and no ruling licenses it. Stewardship reaches a place through the steward's acts: what he raises
(`rate`), and how much he takes or gives (the first lane's amount as a choice).

**Not yet possible.** A trade skill: `exchange` has no magnitude a rate could scale until a price exists
(CP-T08-05, CR-67).

## 6. The gate, and the falsifier

- **Execution artifact.** `engine/season/tests/test_works_founding.py` gains: with a test-rebound verb
  table in which `restore` names a capability with `magnitude: rate` and `effect_rate_gain` non-zero,
  two persons of unequal held score raise the same worn harbour by unequal amounts, both clamped at the
  ceiling; with `effect_rate_gain` 0 they raise it alike and the hash is the base. Under CP-T08-01, a
  cohort holding the capability yields more from one seam than an equal cohort that does not.
- **Falsifier.** A rate lifting a fabric over its works' ceiling; a row with no `magnitude: rate`
  reading anything but 1; the loader accepting `capability:` on an uncontested row that declares no
  magnitude.
- **Control.** The shipped table and fixtures reproduce every pinned hash.

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Without it a capability Jordan authors cannot touch a settlement, and with the first lane's
  version it could, by a table no other subsystem shares. From the designer's side (top-down) a skill is
  one row and a column value; from the roller's side (bottom-up) it is the same `faculty`; laterally the
  decision layer, the dice and the settlement effects use one form.
- **R.** Who mends the wall, and which people work which ground, start to matter; peoples become
  unlike as places do. Completeness: gain 0, no row and no holder each read exactly 1.
- **S.** One methodology for every capability factor (`about_mid`), which is the point of superseding.
- **E, last.** One function and one loader clause, against a table and three roster rows.

## 8. Cost class

Edit, after the CORE and CHAR proposals land (it reads both). Hash EQUAL while no row declares a rate.
