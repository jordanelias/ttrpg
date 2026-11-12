# VERBS · MILITARY · A — `move` and `migrate`: a journey that goes somewhere, and can go wrong

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **Layer 1** (`04` §B.13 invariant 12, §C.4; the loader's refusals at `data/verbs.py:848-851`, `:872-876`): a band-keyed `writes:` belongs to a row that declares `contests:`. `move` and `migrate` write different cells by band, so each declares `contests: "a task"` (residue §1, shape (b)); the route roster has one name, `graded_tasks`, and Edit 4's two `graded_inquiries` lines become that prize binding. (2) **A-5, A-6, A-7**: the draw is the one sampler; the pool is the one pool rule on the mover's `wayfaring` score, `wayfaring` a definition row on U1's surface. (3) **A-25**: `sworn_there` is a named level for the roller, not −1 on the obstacle. (4) **A-58**: a person's `move` onto land another holds is not a march in force and is no aggression; only `march` musters. (5) A-56 names `migrate` among the common people's heavy moves; the row is its carrier as written. The bands' meanings, the class, the stamp terms, the `at` Observation and the `with` deposit (one owner: this file) stand.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (row M-7). Nothing here is deleted; one edge is named and one cross-reference added. (1) **The journey's band reaches the field.** `_relocate` is the one journey body and `_eff_march` calls it; when this proposal's bands land, an army whose march folds the journey's `Partial` ("arrives spent") enters its field at a lower share of stamina, through the one input `entry_stamina` (`16_PESSIMIST_MB_one_stamina_ledger.md` step 3; the value, a seed, is `fatigue.entry.march_partial` in `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3). `_eff_march` "passes nothing and is unmoved" (Edit 4) until then, and nothing in this file changes. The sourced case is Crécy: an army attacking the same afternoon after a march of about twelve miles, against one "rested and fed" (`research/historical/mass_battle_movement_and_behaviour_grounding.md` T5). (2) **What the tree now holds on march rates**, for whoever sets `journey` difficulties: a Roman training march of 20 Roman miles in five summer hours as usually quoted from Vegetius (tool-read, second-hand); about fifteen miles a day for Alexander's whole army (snippet only); a fighting march made only in the cool with rest days (Arsuf, tool-read). Same note, rows M4 to M6. None is a figure to build on; all three agree that a day's march by an army is tens of kilometres at most and far less under threat.

Batch M-A of `audits/14_VERBS_MILITARY.md` (§2, §5.3). Source findings: F-VM-04, F-VM-05; hole rows
H-329, H-140, H-309, H-327 (cross-listed), H-168; `AUDIT_BRIEF.md` "Standing rule". Nothing is
ratified by being written.

## 1. What it changes in `engine/season/` at runtime

1. `move` forms only on places: the places a person has been told of, his own home when he is away
   from it, and the place his ledger says a person the question names is at. It no longer forms on a
   person, a Record or the rung he stands on.
2. An admitted `move` or `migrate` is resolved by one draw on the graded route and written by band:
   arrives fresh, arrives, arrives spent (or, for `migrate`, lodged and not housed), turned back.
3. `travel.moved`, `residence.changed` and `army.arrived` carry where the mover went, so a witness
   knows where he now is.
4. A refusal on `with` (in any row) is deposited to the actor, so he does not form the same act on
   the same absent person again.

Every one of the four is a declared mover of the realm, spine and corpus hashes; they land as four
commits in the order of §3.

## 2. The problem (evidence)

- `aperture 2 0`, realm arm (`scratchpad/runs/VERBS_MILITARY/aperture_2_0_shared_from_PHYSICAL.txt`):
  `move` formed 83, attempted 55, executed 15, refused 40, of which 33 cleared the cell and were
  declined by the effect (`loop/effects_migration.py:63`, `contain_ascends`). `hole_register.yaml`
  H-329: 16 of 17 executed moves at this seed and span went to the mover's own rung; the refused ones
  aimed at Person rungs and Records. The row has no `referent_class`, so `to` binds whatever the
  question is about (`decision/options.py::_derive_operand`).
- The same reading: `with=False` is the deciding read for `train` 33, `give` 17, `surveil` 15,
  `capture` 7. `with` is world-only (`ED-IN-0282`), so the read is never deposited and the act
  re-forms.
- `_eff_move` and `_eff_migrate` return one `Change` and no band: an admitted journey arrives every
  time (`effects_migration.py:71`, `:228`).
- `migrate`: 10 executed, 74 refused (`room` 60, `path` 13, `write` 1). The row works; REM-29's
  deposit already stops the repeated `room` refusal.

## 3. Exact edits, by owner, in landing order

**Edit 1 — `engine/season/verb_table.yaml`, the `move` row (class only; mover: formation).**

```yaml
  - verb:        "move"
    stratum:     "movement"
    eligibility: ["own"]
    beneficiary: "actor"
    referent_class: Rung
    referent_class_note: "14-VM-A: `migrate`'s class. FORMED ONLY ON A PLACE: `places_named` (told of, not lived under), `home_when_away` (his own `reside` object when his live `contain` is elsewhere) and `whereabouts_named` (the rung his own ledger's newest `at` claim gives for a Person the question names). Not on a person, a Record or the rung he stands on (H-329). REVERT: delete this column and the two stamp terms."
    requires:    "a contain path exists, and the actor may enter the destination"
    requires_typed:
      all:
        - form:      contain_path
          of:        actor
          to:        to
          conjunct:  path
        - form:      relation
          of:        to
          relation:  audience
          conjunct:  audience
    writes:
      Overwhelming: ["Tenure.until", "Tenure.since"]
      Success:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
      Partial:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
      Failure:      ["Person.travel_leg"]
    writes_note: "14-VM-A: ONE JOURNEY BODY (`_relocate`), FOUR BANDS. Overwhelming: arrives, no leg laid (the journey costs nothing next season). Success: today's write. Partial: arrives spent, the destination appended to `travel_leg` twice (`decision/budget.py`'s distance penalty reads its length). Failure: turned back; no `contain` moves, one leg laid. [ASSUMPTION; medium; Jordan to correct; revert: the flat three pairs and the route row.]"
    emits:
      Overwhelming: ["travel.moved"]
      Success:      ["travel.moved"]
      Partial:      ["travel.moved"]
      Failure:      ["travel.turned_back"]
    emits_on_refusal:
      path:     ["travel.blocked"]
      audience: ["travel.blocked"]
      write:    ["travel.blocked"]
    grade:       "assumption"
    source:      "ARCHITECTURE_V2.md §E3, transcribed; bands and class: proposals/2026-11-12-subsystem-audit-suite/proposals/14_VERBS_MILITARY_A_movement.md"
```

Edit 1 lands in two commits: the class and the stamp terms first (flat `writes:`/`emits:` as today),
the bands with Edit 4.

**Edit 2 — `engine/season/queries/world_q.py`, two stamp terms beside `places_named`** (resolver-side
standing occasions, `larders_in_purview`'s shape; each reads the person's own edges and own ledger):

```python
def home_when_away(w: World, p: Person) -> tuple:
    """`(reside object,)` when p's live `contain` object is another rung; `()` otherwise."""

def whereabouts_named(w: World, p: Person, persons: tuple) -> tuple:
    """For each Person id in `persons` (the question's own Person referents): the value of the newest
    `at` claim about him in p's OWN ledger, if it is a Rung the ladder would seat p in
    (`contain_ascends`) and p is not already there. Sorted, de-duplicated."""
```

`questions_for` splices both onto the first question as `Rung`-classed referents, where it splices
`places_named`. No new class, no operand.

**Edit 3 — the `at` Observation.** `engine/season/loop/effects_migration.py::_relocate` returns the
destination to its caller; `_eff_move`, `_eff_migrate` and `loop/effects_combat.py::_eff_march` put
`Observation(mover, "at", dest)` on the Event beside what they already carry (`body_observed`'s
shape). `rosters.yaml: observation_terms` gains `at`. WITNESS deposits it to whoever it deposits the
Event to; nothing new decides who that is. `[UNVERIFIED: that an Observation whose value is a rung id
needs no change in `loop/witness.py`; `broke_observed` carries a bool.]`

**Edit 4 — the draw.**

- `engine/season/rosters.yaml: graded_inquiries.values` gains
  `move: {provider: "social_contest", module_entry: "social_contest.roll"}` and the same for
  `migrate`; `verb_capability` gains `move: wayfaring`, `migrate: wayfaring`.
- Obstacle rows, in the table `05_SC_obstacle_difficulty_and_modifiers_B.md` adds (its name governs):

  | verb | difficulty | modifiers (each a named row, a number in data) |
  |---|---|---|
  | `move` | `journey`: 1 when origin and destination share a settlement, 2 a province, 3 beyond (the depth of the common ancestor in the containment tree; `world_q.ancestry`, the one walk) | `winter` +1 · `body_below_first_band` +1 · `destination_occupied` +1 |
  | `migrate` | `journey` | the three above · `foreign_holder` +1 (the destination's `holder_faction_of` is not the migrant's faction) · `larder_short` +1 · `sworn_there` −1 (a live sworn `oblige` to a seat whose purview reaches it) |

  `[ASSUMPTION; medium; Jordan to correct]` for every number. The values that reproduce nothing are
  not available here: there is no draw today, so every arm of this edit is a mover.
- `loop/effects_migration.py::_eff_move(w, a, res)`: after the declines (custody, arrival-only, the
  ladder, and **a destination that is his live `contain` object**, H-140), dispatch on `res.degree`:
  `Failure` → `Change((Subject.entity("persons", a.actor, fields=("travel_leg",)),), lay_one_leg)`;
  the others → `_relocate(w, a, dest, legs=0 | 1 | 2)`. `_relocate` gains `legs: int = 1`, the count
  of times `dest` is appended; `_eff_march` passes nothing and is unmoved.
- `_eff_migrate(w, a, res)`: `Overwhelming`, `Success` → today's `perform`; `Partial` →
  `_relocate` alone (the `reside` edge untouched), emitting `travel.moved`; `Failure` → as `move`.

**Edit 5 — the `migrate` row** (`verb_table.yaml:1153`): cell, class and refusals unchanged;

```yaml
    writes:
      Overwhelming: ["Tenure.until", "Tenure.since"]
      Success:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
      Partial:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
      Failure:      ["Person.travel_leg"]
    emits:
      Overwhelming: ["residence.changed"]
      Success:      ["residence.changed"]
      Partial:      ["travel.moved"]
      Failure:      ["travel.turned_back"]
    writes_note: "14-VM-A: Partial is LODGED, NOT HOUSED -- the journey is made and `reside` is untouched, which is a `move`; he may settle from where he stands next season. [ASSUMPTION; medium; Jordan to correct]"
```

**Edit 6 — `with` teaches** (`engine/season/data/requires.py`, the stem's world-only flag; owner of
the ruling: `ED-IN-0282`). `with` leaves the world-only set, so a refusal's read
`(subject, with:<actor>, False)` rides `Event.observed` and is deposited to the actor
(`observation_deposit_mode: actor`), as `room` is since REM-29. It is listed here because presence is
this family's; it moves `train`, `tend`, `give`, `capture` and `surveil` formation, and the PHYSICAL
and SOCIAL families cite the same refusals. Whichever batch lands first carries it once.

**Hole register:** H-329 and H-140 close on Edits 1, 2 and 4; H-309 closes as answered (an office is
a `hold`; absence is not vacancy; removal is `revoke`'s), with no code change.

## 4. Gate and falsifier

- **Execution artifact.** `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2,
  `PYTHONHASHSEED=0`: (i) H-329's classifier over `travel.moved`: moves to a rung other than the
  mover's own above 0 at every seed, same-place moves 0; (ii) no `move` attempted whose `to` is a
  person or a Record; (iii) across the three seeds each of `move`'s four bands occurs at least once,
  and `travel.turned_back` is in the emitted list; (iv) at least one `migrate` whose band is Partial
  leaves the migrant's `reside` object unchanged and his `contain` moved; (v) a refusal on `with`
  is followed by no second act of the same `(actor, verb, subject)` in the next season.
- **Downstream read.** A person who moved to `whereabouts_named`'s rung executes, the next round or
  season, an act whose cell asks `with` of the person he went to. One such pair in the three seeds
  is the artifact; none is a reading that the chooser does not yet want to (CHAR's), stated as such.
- **Control.** Same seed twice: equal `content_hash` (the draw is seeded). The route row removed:
  every admitted journey arrives, band `Success` only.
- **Falsifier (planted).** `_eff_move` ignoring `res.degree`: (iii) fails, no `travel.turned_back`.
  `whereabouts_named` returning the person's rung id itself: (ii) fails. The `legs` argument
  dropped: a Partial and a Success leave equal `travel_leg` lengths.
- **Not claimed.** No rate, no balance: three seeds are three trajectories.

## 5. NERS reading (E last)

- **N.** From below, every `with` cell needs a body that can get there. From above, a realm whose
  people never travel has no courts, no fugitives and no envoys. Laterally, `march`'s arrival is the
  same body and is unmoved. Across scales, a household's `migrate` is the settlement's census.
- **R.** Distance becomes something to plan around; a journey that fails costs a season and is
  tried again; with no player, people go to one another and are sometimes turned back.
- **S.** One journey body, one roller, one obstacle composer; `migrate`'s Partial is `move`, not a
  third state.
- **E, against that.** One column, two stamp terms, one Observation, two route rows, a `legs`
  argument. A player can say what happened: "I set out for Ehrenfeld in winter and was turned back."

## 6. Cost class

Small build; six declared movers. Depends on the graded route running a degree-keyed effect
(`audits/14_VERBS_MILITARY.md` S1, `[UNVERIFIED]`) and on SC-B's composer for the modifier rows; with
neither, Edits 1 to 3 and 6 land alone and the journey stays certain, which this proposal then leaves
open as F-VM-04 and F-VM-05.
