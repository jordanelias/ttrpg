# 07 · SE — a skill's rate on an untested act, on the suite's one skill surface (supersedes two sections of `07_SE_capability_and_chooser_surface.md`)

Reconciled: 2026-11-12, U5d closure — folded **A-54** and **A-12** against one row of the audit addendum's §6 that this file implements ("stewardship … No passive bonus from a holder to his domain's yield … declined"). Overruled: A-54 rules that a steward's skill bears on the harvest draw. The form: the steward (the holder of the seat whose rung is the place's treasury rung) contributes named levels (`edge` row, site `settlement_effect`, `side: steward`, `per: mid`) to the place's seasonal draw; the place, not the steward, is the roller (D-U1-09, wave 3, replacing "contributes to the **pool** … through `rate(person, work)`"); it is a term in a draw, not a multiplier on a fixed yield, so the place can still fail under a good steward. A seat's own modifier (A-12) is the seat row's `modifier:`, read by the `office` leverage source on rolls made through that seat (D-U1-01); the place's draw is not such a roll. `rate`'s form (`about_mid`, now on `score`, D-U1-09) and the row declaration (`magnitude: rate`) are unchanged; the two inputs to a roll are `U5a_capability_home_and_two_inputs.md`'s.

Reconciled: 2026-11-12, wave 3 (W3-3) — applied D-U1-09 (§3 item 2 and §4 (c): `faculty` → `score`, the trained rank on the capability's own scale; the head's A-54 sentence above → named levels at `settlement_effect`; a `magnitude: rate` row that is also a task row is refused at load), C3-C2 (§4 (d)'s multiplier deleted: a task row's capability enters through the task draw of `18_DETERMINISM_task_draw_for_uncontested_verbs.md`, whose band sets the rise), D-U1-07 / R3 §2 (the capability's home named: `references/descriptor_registry.yaml: capabilities`, its `scale: [floor, ceiling]`, C-03; R3's "re-fit `about_mid` to score plus base, floor five" is not applied, since D-U1-09 reads the rank, not the pool), D-U1-01 (the head's seat-modifier sentence). §4 (e) kept as D-U1-09's one remaining `rate` use (labour hand weights), with C3-C2's wording for (e) marked DISPUTED below. R3 §1 Option A (move `rate` to `queries/world_q.py`) is DISPUTED and not applied: `seam/wrappers/pool.py:15` imports `queries.world_q.practice`, so `world_q` importing `pool` closes a cycle, and U1's reader interface places it at `pool.py::rate` (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:306`). Tier and batch added (R3 7b-0; U3 B12).

Reconciled: 2026-11-12, unification lane U4c (test 9; grepped at the tree) — `about_mid` is not in the tree (no occurrence under `engine/`): it is proposed by `02_CHAR_capability_uses_table.md` (`:82`, `about_mid(value, floor, ceiling, gain)`, role `judgement`, a float factor; `02_CHAR_resolve_and_temper.md:107`: exactly 1 at the scale's mid-point). The two `[UNVERIFIED]` marks in §3 and §4 are decided as requirements on that owner: (1) `about_mid(value, floor, ceiling, 0)` returns exactly `1.0` for every value (the CHAR file's own "hash EQUAL at gain 0" needs it); the executing session adds that one assertion beside CHAR's `about_mid` tests in B04 (name `test_about_mid_is_exactly_one_at_gain_zero`, `[ASSUMPTION]` for the file: the one CHAR's gate (b) names); (2) it returns a float, so `rate` converts at its one site as §4 already says.

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), after `14_VERBS_MATERIAL_A`–`_C` and before `07_SE_capability_and_chooser_surface.md` §5–§6 (U3 §1 item 13).
Depends on: `01_CORE_capability_authoring_surface.md`, `02_CHAR_capability_uses_table.md` (`about_mid`), `U5a_capability_home_and_two_inputs.md` (all B04); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (B07, the task draw and its loader edit); CP-T08-01 (plan position, `labour`; MISSING until STAGES.md step 5 carries it).

Carries finding F-SE-21 and resolution R-SE-32 of `audits/07_SE_audit_addendum_B.md` (its §6). It
supersedes **only** §3 (the interface) and §4 (the roster rows and the `capability_rate` table) of
`proposals/07_SE_capability_and_chooser_surface.md`; that proposal's §5 (the NPC and chooser points) and
§6 (the axioms) stand. It adds no skill system: it states what the settlement layer needs of the
surface the CORE, CHAR and DICE lanes proposed, and the one licence it asks of them. Nothing is ratified
by being written.

## 1. What changes in `engine/season/` at runtime

With the shipped data: nothing. No verb row names a skill with a rate, so every factor is exactly 1
and every hash is the base. When a designer authors one, a person who holds it raises a fabric (and, when
CP-T08-01 lands, works a Site) faster than one who does not, by one closed form shared with every other
skill factor in the game.

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
- **The need is real.** No settlement outcome reads a skill, and `_rise`'s `f(degree)` is the
  identity (`loop/effects_economy.py:121-129`, H-164): first audit §14, unchanged.

## 3. The resolution, decided

**One licence, one form, one score.** Ladder step 4 (the other lanes' surface is the precedent).

1. **The verb row declares it.** A row may carry `capability: <id>` if it contests, is graded, **or
   declares `magnitude: rate`**. The third licence is the only change asked of the CORE proposal's loader
   rule. A row with `magnitude: rate` and no `capability:` is refused; a `capability:` on an uncontested
   row without `magnitude: rate` is refused as that proposal already says.
2. **The factor is `about_mid`.** `rate(person, verb) = about_mid(score(person, verb), floor, ceiling,
   gain)`, where `score` is `seam/wrappers/pool.py::score`, the skill score on the skill's own scale
   (D-U1-09: not `faculty`, which carries `pool_add`), `floor` and `ceiling` are the skill definition
   row's `scale: [floor, ceiling]` at `references/descriptor_registry.yaml: capabilities` (D-U1-07, C-03),
   and `gain` is one fixture, `effect_rate_gain`, shipped 0. No per-capability table. A row that is a task
   row (18-A) may not also declare `magnitude: rate`; the loader refuses it (D-U1-09: one skill, one
   channel per act). `[UNVERIFIED: that `about_mid`
   returns exactly 1 at gain 0. The CHAR proposal ships its own new use at gain 0 and calls the hash
   EQUAL, which requires it; the function is not yet written.]`
3. **No skill named is exactly 1.** A row that names none, and a person who holds none on a row
   that names one, are different facts: the first has no rate; the second has the score the DICE
   interface gives a non-holder (the untrained default). The DICE audit's point that unskilled use is
   indistinguishable from the default is not repaired here; it is inherited and named.
4. **What a rate may not be** (the DICE audit's exclusions, restated for an effect): not a bonus to a
   net, not a change of obstacle, not a gate on attempting. It scales the magnitude of an effect that
   already happens, and never past the effect's own ceiling.

## 4. The exact edits, by owner

**(a) `engine/season/data/verbs.py` (the CORE proposal's Edit 3, amended).** `VerbRow` gains
`magnitude: str = ""` with the closed set `("", "rate")`; the refusal rule becomes: `capability:` is
allowed when the row `contests`, is graded, or has `magnitude == "rate"`; and a row that is a task row
(18-A's `graded_tasks`) **and** declares `magnitude: rate` is refused (D-U1-09).

**(b) `engine/season/verb_table.yaml`.** No row is edited by this proposal. `restore`, `work`, `build` and
`craft` (CP-T08-04) become task rows under 18-A and take their skill at the `task` site, with no
`rate` row (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:254`). Names are Jordan's content.

**(c) `engine/season/seam/wrappers/pool.py`**, beside `faculty` (the one pool reader; U1's reader
interface, `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:306`):

```python
def rate(w, p, verb) -> Fraction:
    """The factor a held capability gives an untested magnitude of `verb`. Fraction(1) where the row
    declares no `magnitude: rate`, where `p` is None, and at `effect_rate_gain` 0."""
    row = VERB_TABLE[verb]
    if p is None or row.magnitude != "rate":
        return Fraction(1)
    lo, hi = descriptors.CAPABILITIES[row.capability]["scale"]
    return about_mid(score(w, p, verb), lo, hi, w.fixtures.get("effect_rate_gain"))
```

`about_mid` is `02_CHAR_capability_uses_table.md`'s; `descriptors.CAPABILITIES` is CAP A1's (D-U1-07, the
`ATTRIBUTES` precedent in `engine/substrate/descriptors.py`); `score` is `pool.py::score` (lane A's split of
`faculty`, B01). `[UNVERIFIED: `about_mid`'s return type; the CHAR proposal gives its signature and says it
returns a factor. If it returns a float, `rate` converts at this one site so integer arithmetic stays
exact.]` `rate` stays in `pool.py` (not `queries/world_q.py`): `pool.py:15` imports
`queries.world_q.practice`, so the reverse import would be a cycle.

**(d) `engine/season/loop/effects_economy.py::_rise` and `_fall`: no multiplier (C3-C2).** A task row's
skill enters through the task draw (`18_DETERMINISM_task_draw_for_uncontested_verbs.md`, one pool rule,
A-6/A-7); the band sets the rise (the `f(degree)` H-164 records as NOT BUILT is the band, through
`task_fraction`), and no `rate` row sits on a task row. `_rise` and `_fall` keep their arithmetic and read
no `rate`. The former edit (`min(headroom, headroom × num × rate // den)`) is withdrawn; it was a second
ladder for one quantity.

**(e) CP-T08-01's `labour(w, rung)`** (planned): each present person's hands are weighted by `rate` (D-U1-09:
`rate` remains for magnitudes no draw decides, and the labour weight is one). A cohort is a `Person`, so a
cohort row that carries a skill (`cohorts.yaml`, through the cast surface of the CORE proposal's Edit
5) makes a mining people mine better than a farming people set to the same seam. Shipped: no cohort row
carries one, so every weight is 1. **DISPUTED (C3-C2's wording):** C3-C2 orders "the multiplier in §4 (d),
(e) is deleted", while the same row adopts D-U1-09, which keeps `rate` for "CP-T08-01's `labour` hand
weights"; this lane applies D-U1-09 for (e), the more specific decision. **INCOMPLETE, two blocking
points:** (1) which verb row the labour weight reads: `rate(w, p, "work")` reads 1 for everyone once `work`
is a task row (it cannot declare `magnitude: rate`), so the labour weight needs a non-task row or a
skill id argument, a decision for CP-T08-01's landing; (2) the caller: `labour` is planned in
`queries/world_q.py`, which cannot import `pool.py` (the cycle above), so the weights are computed by the
caller in `loop/` and passed in, `[ASSUMPTION: the yield pass at MATTER computes them — basis: it is the
reader of `labour` named by CP-T08-01]`.

**(f) Nothing in `modules/settlements/`.** A rate is a host read of a person; the module's inputs carry
the factor it already has (`ProduceInput.factor`, under CP-T08-01).

## 5. What a skill definition must say for the settlement layer to use it

Its id; its kind and `scale` (`descriptor_registry.yaml: capabilities`, D-U1-07); its growth rule; and, on
the verb rows it serves, `capability:` (a task row) or `capability:` with `magnitude: rate` (a non-task
magnitude). Nothing else, and the settlement layer reads none of it except through the task draw and
`rate`.

**Overruled by A-54 (see the head).** This paragraph declined a passive rate from a seat holder onto his
domain's yield; A-54 rules that a steward's skill bears on the harvest draw. The form is the steward's
named levels on the place's draw (`edge`, site `settlement_effect`, D-U1-09), not a rate and not a
multiplier. Stewardship also reaches a place through the steward's acts: what he raises (the task draw),
and how much he takes or gives (the first lane's amount as a choice).

**Not yet possible.** A trade skill: `exchange` has no magnitude a rate could scale until a price exists
(CP-T08-05, CR-67).

## 6. The gate, and the falsifier

- **Execution artifact.** `engine/season/tests/test_works_founding.py` gains:
  `test_rate_is_one_without_magnitude_rate_or_at_gain_zero` (a test-rebound verb table with a non-task row
  declaring `magnitude: rate`; two persons of unequal held score read unequal factors at
  `effect_rate_gain` non-zero and equal factors at 0, and the hash is the base);
  `test_a_task_row_declaring_magnitude_rate_is_refused_at_load` (D-U1-09). The skill-on-`restore`
  reading moves to 18-A's task-draw tests (two persons of unequal score raise the same worn harbour by
  unequal shares across seeds, by band). Under CP-T08-01, a cohort holding the skill yields more
  from one seam than an equal cohort that does not.
- **Falsifier.** A row with no `magnitude: rate` reading anything but 1; the loader accepting
  `capability:` on an uncontested row that declares no magnitude, or `magnitude: rate` on a task row;
  `_rise` reading `rate` (a second ladder).
- **Control.** The shipped table and fixtures reproduce every pinned hash.

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Without it a skill Jordan authors cannot touch a settlement, and with the first lane's
  version it could, by a table no other subsystem shares. From the designer's side (top-down) a skill is
  one row and a column value; from the roller's side (bottom-up) it is the same `score`; laterally the
  decision layer, the dice and the settlement effects use one form.
- **R.** Who mends the wall, and which people work which ground, start to matter; peoples become
  unlike as places do. Completeness: gain 0, no row and no holder each read exactly 1.
- **S.** One methodology for every skill factor (`about_mid`), which is the point of superseding.
- **E, last.** One function and one loader clause, against a table and three roster rows.

## 8. Cost class

Edit, after the CORE and CHAR proposals land (it reads both). Hash EQUAL while no row declares a rate.
Tier: `opus` for the ladder question (decided in U3/U1: C3-C2, D-U1-09), then `sonnet` for the build
(R3 7b-0).
