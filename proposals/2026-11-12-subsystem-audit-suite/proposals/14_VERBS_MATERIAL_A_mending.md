# 14 · VERBS · MATERIAL · A — the family's draw; `restore`, `work`, `sabotage`, `tend`

## Status: PROPOSED

Batch M-A of `audits/14_VERBS_MATERIAL.md` §18 (sections §8, §16, §9, §12 and decisions D-1 to D-7 of its
§0.4). Written under `VERBS_BRIEF.md` and the standing rule of `AUDIT_BRIEF.md` (*we do not do
deterministic*). Reference under CLAUDE.md §0.05; not ratified by being written. Read at `84d2a02`.

## 1. What changes in `engine/season/` at runtime

Every act of these four verbs is rolled once, by the route `research` already takes, and pays out by
degree. `restore` is offered to the people standing at a fabric they know is worn, `work` to those at a
fabric being raised, `sabotage` to a man standing at the works of someone he holds a grievance against,
`tend` only to someone who believes the patient hurt. A lost draw emits its own kind and moves nothing.
All of it is a declared hash mover on every realm world. The route, the ladder and the failure rule
landed here are what batches M-B to M-E reuse.

## 2. The family's draw (lands first, in its own commit; moves no hash until a row joins)

| # | owner | edit |
|---|---|---|
| 1 | `engine/season/rosters.yaml` | `graded_inquiries:` renamed `graded_acts:` (the map is unchanged: verb → `{provider, module_entry}`; its note gains *"an act graded with no prize: an inquiry, or a material act (14_VERBS_MATERIAL)"*). `data/rosters.py::GRADED_INQUIRIES` → `GRADED_ACTS`; `manifest/registry.py::check_graded_inquiries` → `check_graded_acts`; `loop/resolve.py` imports the new name. `_grade` is not edited: its draw is already keyed per act |
| 2 | `engine/season/data/fixtures.py` | `effect_share={"Overwhelming": 1000, "Success": 700, "Partial": 350, "Failure": 0}` (per-mille of an effect's full magnitude; swept `1000/700/350/0`, `1000/500/250/0`, and the control `1000/1000/1000/0`, which is today's whole magnitude at every winning band); `watch_step=0.5` (swept 0 / 0.5 / 1); each with a `hole_register.yaml` row graded `assumption`, `site:` set. `[ASSUMPTION; medium; Jordan to correct]` |
| 3 | `engine/season/loop/effects_shared.py` | new, the one reader of the ladder: |

```python
def graded_amount(w: "World", res: "Resolution | None", full: int, table: str = "effect_share") -> int:
    """How much of `full` an act at `res.degree` achieves: ceil(full x Fixtures[table][band] / 1000), so any
    winning band moves at least one unit of a non-zero `full`; 0 at Failure. A graded row's effect reaching
    here with `res is None` is a caller defect (InstrumentDefect), as a missing operand is."""
```

| # | owner | edit |
|---|---|---|
| 4 | `loop/effects_economy.py::_rise`, `_fall` | take `res`; return `graded_amount(w, res, (headroom * num) // den)` (and the footroom likewise). The docstring's *"`× f(degree)` IS NOT BUILT"* paragraph is replaced: it is built, by this function; H-164's row narrows to the unbuilt `share` sweep |
| 5 | `engine/season/verb_table.yaml`, header | one paragraph under the `OBSTACLE` note: a row in `graded_acts` declares `difficulty:`, `capability:`, Degree-keyed `writes:` and `emits:` whose Failure band is a kind of its own (`<verb>.failed`), and keeps `emits_on_refusal` for an act the world would not admit. `data/verbs.py` refuses a `graded_acts` row whose Failure band shares a kind with `emits_on_refusal` (FI-04 §1 lifts the one exception, `finding.none`) |
| 6 | `rosters.yaml: obstacle_terms` (SC-B's roster) | append `ruin`, `wound`, `watch`, each `+`, applying to *a graded material act*; the host builder (`seam/wrappers/sigma.py::contest_input`, where `forgery_quality` already enters) carries each raw, 0 where the row does not name it; the module composes them (`modules/social_contest/roll.py::obstacle`) |
| 7 | `rosters.yaml: referent_classes` | add `Worn`, `Unfinished`, `Resented`, `Wounded`, each with a one-sentence note and each occasion-only and non-collection (`Detainee`'s shape; `data/verbs.py` exports the four names as it exports `DETAINEE_CLASS`) |

## 3. `restore`

**Stamp.** `rosters.yaml`, new roster (checked at import against `EVENT_KINDS`, `strife_kinds`' loader shape):

```yaml
  fabric_news:
    source: "14_VERBS_MATERIAL_A: which Event kinds tell a person that a fabric fell, rose or was begun."
    lists:
      lowers: [condition.worn, condition.band_crossed, site.damaged]
      raises: [site.restored, site.worked]
      begun:  [site.built]
```

`queries/world_q.py`, new, beside `wounded_with`:

```python
def fabric_known(w: World, p: Person) -> tuple:
    """((site, class), ...) for the Sites standing at the rung `p` stands in (his own `contain`) about which
    the NEWEST claim of a `fabric_news` kind in his OWN ledger is a `lowers` kind (class Worn) or a `begun`
    kind (class Unfinished). Reads no Site's condition: a fabric that fell with nobody to see it is stamped
    for nobody (FI-01 R-03). Newest by (when, round, ledger position), `wounded_with`'s rule."""
```

`questions_for` appends its pairs to the classed tuple beside the detainees. Control: `lowers: []`.

**Row** (columns not listed are unchanged; `effect_formula_note` gains the ladder):

```yaml
  - verb:        "restore"
    referent_class: Worn
    capability:  none          # `craft` when Jordan authors it (CORE Edit 3); note: every person rolls the untrained default
    difficulty:  routine       # + `ruin`: one step per `band_floors` floor of the site's kind above its condition
    writes:
      Overwhelming: ["Site.condition"]
      Success:      ["Site.condition"]
      Partial:      ["Site.condition"]
      Failure:      []
    emits:
      Overwhelming: ["site.restored"]
      Success:      ["site.restored"]
      Partial:      ["site.restored"]
      Failure:      ["restore.failed"]
    emits_on_refusal: ["restore.refused"]
```

`rosters.yaml: graded_acts.values` gains `restore: {provider: "social_contest", module_entry:
"social_contest.roll"}`. `_eff_restore`: `delta = _rise(w, site, res)`. `sigma.py::contest_input`: `ruin`
= the count of `w.fixtures.band_floors(site.kind)` values above `site.condition` (0 for an empty cell).

## 4. `work`

`queries/world_q.py::works_sites` stays and is stamped as `Unfinished` (a Site his works names), beside
`fabric_known`'s `begun` pairs. `WorldReader.read`, the `floor` stem: a kind whose `band_floors` cell is
empty reads the roster's own `default_cell` (0), in place of the typed `Unspecified`; the stem's comment
block and `band_floors`' note (*"AN EMPTY CELL IS NOT A WORKABLE SITE"*) are rewritten to say so.
`[ASSUMPTION; medium; Jordan to correct; revert: the raise, and a dwelling works cannot be worked]`

```yaml
  - verb:        "work"
    referent_class: Unfinished
    capability:  none          # `labour` when authored
    difficulty:  routine
    writes:  {Overwhelming: ["Site.condition"], Success: ["Site.condition"], Partial: ["Site.condition"], Failure: []}
    emits:   {Overwhelming: ["site.worked"], Success: ["site.worked"], Partial: ["site.worked"], Failure: ["work.failed"]}
    emits_on_refusal: ["work.unavailable"]
```

`graded_acts` gains `work`. `_eff_work`: the works branch reads `_rise(w, fabric, res)`; a hand-declared
delta is scaled by `graded_amount` the same way. The `requires_typed` cell is unchanged (J-M1).

## 5. `sabotage`

`queries/world_q.py`, new:

```python
def fabric_resented(w: World, p: Person) -> tuple:
    """The Sites standing where `p` stands whose rung (or the nearest rung above it) his OWN ledger names a
    holder of (`person_q.holders_named`, FI-01 edit 1), where he holds a stance row against that holder
    (`person_q.held_against`) or the holder is among `enemies_heard(w, p)`. Class Resented."""
```

```yaml
  - verb:        "sabotage"
    referent_class: Resented
    capability:  none          # `craft` when authored
    difficulty:  demanding     # + `watch`: world_q.guard_weight(site.rung) x Fixtures watch_step
    requires_typed:            # `restore`'s cell, plus CHAR item 5's conjunct
      all:
        - {form: existence, of: site, kind: Site}
        - {form: relation, of: site, relation: present_at}
        - {form: relation, of: actor, relation: individual}
    writes:  {Overwhelming: ["Site.condition"], Success: ["Site.condition"], Partial: ["Site.condition"], Failure: []}
    emits:
      Overwhelming: ["site.damaged"]
      Success:      ["site.damaged"]
      Partial:      ["site.damaged", "sabotage.seen"]
      Failure:      ["sabotage.seen"]
    emits_on_refusal: ["sabotage.refused"]
```

`rosters.yaml: covert_kinds.values` gains `site.damaged` (so `epistemic.trail_of` holds the hand for an
`examine` of the Site). `sabotage.seen` is an ordinary deed kind naming the actor. `[UNVERIFIED: how
`loop/witness.py` masks `who` for a covert kind today; if it does not, the edit is one clause in
`epistemic.observers_for`: an Event of a `COVERT_KINDS` kind admits its actor alone to the `seen` terms,
and everyone else present to the event-kind claim.]` `_eff_sabotage`: `delta = -_fall(w, site, res)`.

## 6. `tend`

`questions_for`: `wounded_with(w, p)` moves from the `added` splice (class `Person`) to the classed tuple
as `Wounded`.

```yaml
  - verb:        "tend"
    referent_class: Wounded
    capability:  none          # `physic` when authored
    difficulty:  routine       # + `wound`: one step per `band_floors.body` floor above the patient's body
    writes:  {Overwhelming: ["Person.body"], Success: ["Person.body"], Partial: ["Person.body"], Failure: []}
    emits:   {Overwhelming: ["body.tended"], Success: ["body.tended"], Partial: ["body.tended"], Failure: ["tend.failed"]}
    emits_on_refusal: ["tend.refused"]
```

`_eff_tend`: `whole = p.body + graded_amount(w, res, max(p.body, p.body_ceiling) - p.body)`, and the
`Change` carries `body_observed(who, whole)` as `_eff_kill` carries it, so a believer's newest body claim
is the mended one. `03_PC_exits_withdrawal_recovery.md` Part C's `tend_fraction` is not added.

## 7. Order of landing

1. §2 rows 1 to 7 (one commit; hash EQUAL: no row has joined).
2. `07_SE_kernel_repairs.md` §3 (a wear of zero emits nothing), if not already landed.
3. `tend` (smallest; re-records the realm goldens once).
4. `restore`, with `fabric_news` and `fabric_known`.
5. `sabotage`, after `08_FI_01` edit 1 (`holders_named`).
6. `work`, with batch M-C (it has nothing to raise before a `build`).

## 8. Gate and falsifier

- **`restore`.** `aperture 2 s`, seeds 0 to 2: `site.restored` > 0 at every seed; at least two degrees
  among them; mean harbour condition and the two-season `yield.taken` total above SE's no-acts arm at the
  same seed. Control: `fabric_news.lowers: []` gives formed 0. Falsifier: a `restore` formed on a Site
  whose fall no claim in the actor's ledger reports (plant: lower a Site with no Event).
- **`tend`.** A fixture with one wounded man and one tender, seeds 0 to 19: three or more distinct bodies
  after one act; after a whole mending nobody forms `tend` on him. Realm: `with=False` refusals 0.
- **`sabotage`.** A fixture (a town, a garrison, a holder, a man with a row against him), seeds 0 to 19:
  three or more distinct garrison conditions; at `Overwhelming` and `Success` no co-located ledger names
  him and a planted-`Success` `examine` does; a `march` on the town reads lower `fortification_of` than
  the control. Realm: `exists:Site=0` refusals 0.
- **The draw itself.** With `effect_share` at the control (`1000/1000/1000/0`) and a planted `Success`
  on every act, the four effects reproduce today's magnitudes (the existing hand-built tests, with the
  planted `Resolution`).
- **Planted failure for the batch.** Pin `_grade` to `Success`: every spread above collapses to one value
  and each gate must go red.

## 9. NERS reading (E last)

N: the raising arms of fabric and body do not execute today, so every lowering arm is a ratchet (SE
F-SE-18); holds top-down (R-05, R-09), bottom-up (the effects and the route exist), laterally (one
formula on Site and body), diagonally (a repaired harbour is next season's yield, a weakened garrison is
the next field). R: neglect, botched repair, a saboteur seen or unseen, with no player. S: one route, one
ladder, one failure rule for the family; *pauses correctly* is untested until a multi-act scene exists.
E, last: two fixtures, one function, three stamps and four rows, against four verbs of which two never
form and one never executes.

## 10. Cost class

Small build. Declared mover. Lanes: SE (fabric), PC (body), FI (the covert kind), CHAR (stance rows,
the conjunct), SC and CORE (the two columns).
