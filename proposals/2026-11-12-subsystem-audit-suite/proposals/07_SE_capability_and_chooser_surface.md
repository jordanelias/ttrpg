# 07 · SE — how a character's capability and temperament reach a settlement act

## Status: PROPOSED

Carries §14 (capability authoring surface) and the NPC and chooser points of `audits/07_SE_audit.md`.
It extends the existing owners. It defines no capability, no second pool reader and no settlement-local
dialect.

## 1. What changes in `engine/season/` at runtime

With the shipped data, nothing. The change is that three uncontested settlement effects read one
declared multiplier from the roster the pool reader already reads, so that a person who holds a named
capability raises a fabric faster, and the mapping is authored as data.

## 2. The problem, with evidence

- **No settlement outcome reads a character capability.** `grep -n "capabilit\|attribute"` over
  `modules/settlements/*.py`, `loop/effects_economy.py`, `loop/effects_founding.py`,
  `loop/effects_migration.py` and `loop/matter.py` returns nothing (run at this commit). The one pool
  reader, `seam/wrappers/pool.py::faculty`, is reached only by contested verbs, and no settlement verb
  declares `contests:`.
- **The design's own term for it is built as the identity.** `effects_economy.py:121-129`: `restore`'s
  `Δ = (1 − condition) × f(degree) × share`, with `f(degree)` *"NOT BUILT"* because an uncontested act
  has no degree (H-164). So a master mason and a crowd of two raise a wall alike.
- **What a settlement act does read of a person** is `Person.weight` (the want, the population, the
  provision bound), `Person.body` (the fall), presence (`share`), and a seat's remit and purview.
  None is a skill.

## 3. The resolution, decided

**The existing owner is `rosters.yaml: verb_capability`** (verb → capability key), with
`vocation_attribute` (key → attribute) and `Person.capability` / `Person.attributes` as carriers, read
through `pool.py::_capability` and `_authored_attribute`. Ladder step 4: a contested verb gets its dice
from that table; an uncontested verb that should answer to skill gets its *rate* from the same table.
Routing `restore` through a contest was rejected at `effects_economy.py:126-128` (a prize no subsystem
claims) and stays rejected.

**The interface SE needs from the merged capability surface** (for the holistic stage):

1. `verb_capability[verb] -> key | absent`, as now. SE adds rows, never a table.
2. One host function `rate(w, person, verb) -> (num, den)`, beside `faculty` in `seam/wrappers/pool.py`:
   the per-mille multiplier a held capability gives an uncontested effect, read from a roster table
   `capability_rate` keyed by capability key (a map from held score to per-mille, with `default: 1000`).
   `(1000, 1000)` when the verb has no row or the person holds no key: the control, today's arithmetic.
3. A capability definition must therefore say, for SE to use it: its **key**; the **verbs** it serves
   (rows of `verb_capability`); for each uncontested verb, its **rate table**; and its **growth rule**
   (already `train`, and `_eff_kill`'s build-by-doing, both reading the key off `verb_capability`).
   SE needs nothing else, and reads none of it except through `rate`.

## 4. The exact edits

**(a) `engine/season/rosters.yaml`.** `verb_capability` gains (shipped commented out until a capability
of that name is authored by Jordan; the names are placeholders, `[ASSUMPTION]`):

```yaml
      # restore: "building"     # raising and mending a fabric
      # work:    "building"
      # build:   "building"
```

and a new table read by one function:

```yaml
  capability_rate:
    source: "proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_capability_and_chooser_surface.md; H-164"
    row: H-164
    note: "Per-mille multiplier on an uncontested effect's magnitude, by the held score of the verb's capability key."
    default: 1000
    rates: {}                 # e.g. building: {0: 500, 1: 750, 2: 1000, 3: 1250, 4: 1500}
```

**(b) `engine/season/seam/wrappers/pool.py`** gains `rate(w, p, verb)` as specified. It reads
`VERB_CAPABILITY`, `_capability` and the new table; nothing else.

**(c) `engine/season/loop/effects_economy.py::_rise`** takes the act and applies the rate:

Old: `return (headroom * num) // den`

New: `rn, rd = rate(w, w.persons.get(a.actor), a.verb); return min(headroom, (headroom * num * rn) // (den * rd))`

The `min` keeps the ceiling a bound (a rate above 1000 raises the pace, never the ceiling). `_fall`
takes the same rate for `sabotage`. `H-164`'s row narrows: `f(degree)` is answered by `rate` for the
uncontested case.

**(d) Nothing in `modules/settlements/`.** The module stays capability-blind: a rate is a host read of a
person, and the module reads no person beyond the weights its input records carry.

## 5. The NPC and chooser surface (points a to e)

The statement of intent is the CHAR audit's (`audits/02_CHAR_audit.md`, its section on the NPC and
chooser intent as established from code plus ruling); it is cited, not redone. For this subsystem:

- **(a) Who decides, on what.** Relief, extraction, repair, founding and migration are persons' acts
  (`transfer`, `requisition`, `restore`, `found`, `build`, `migrate`) formed from what each knows: a
  shortfall claim (`matter.py:647`, the seat channel), a stock report (`_stock_report`), a learned
  refusal for room (REM-29), a place he was told of (IN-45). MATTER decides nothing (L5). The budget is
  the scene budget; the reason is the Event's `observed` and the claim's source.
- **(b) One interface.** Yes. A played steward is `play_surface.dispatching_chooser`; the development
  space ranks and selects among the candidates the chooser formed and forms none (`decision/sheet.py`).
  The defect is upstream of the interface and shared by both: the candidates themselves are malformed
  for settlement verbs (a `transfer` whose `to` is the giver's own rung; a `move` to where he stands).
- **(c) Hard-coded NPC rules.** None found in the settlement effects or in MATTER: each declines or
  writes, and chooses nothing. Two class rules exist and both are rulings, not drift: only a cohort eats
  (`larder.py:48`, ED-IN-0255), and a cohort is seated with pursuits and no convictions or goals
  (`populated.py::seat_cohorts`). One authored assignment stands where a decision would: which master
  founds and builds (`venues.yaml: planned_works`, each row `[ASSUMPTION]`).
- **(d) Characterful, and legible.** Today two governors facing one shortfall form the same act with the
  same amount, and a cohort differs from its neighbour only by its territory's `alpha/beta` ratio. What
  makes a settlement choice a person's: an amount he chose (`07_SE_arc_needs.md` §3 b), a destination he
  chose among places he knows (CR-49's `referent_class: Rung` for `transfer`, `exchange` and `migrate`),
  and a rate that is his (this file). The reason trail exists for acts (`Event.observed`,
  `Term.declared_by`: a lapse cites the last hand that wound the clock) and is missing for the act not
  taken: a steward who let a town starve leaves no record that he knew.
- **(e) Missing, as proposals.** This file (rate); `07_SE_arc_needs.md` (amount as a choice);
  `07_SE_kernel_repairs.md` D (arrival knowledge). Cross-listed to CHAR, not proposed here: a cohort
  performs every individual verb (read at seed 0, two seasons: 708 of 1,529 resolved acts are cohorts',
  among them `create_record` 115, `challenge` 60, `forge` 47, `research` 30), which is S9.1's one class
  working as ruled and a population behaving as a clerk and a duellist; the fix, if one is wanted, is a
  declared requirement those verbs' rows carry and a cohort does not meet, never an `is_cohort` test.

## 6. The RPG axioms in play, in the tradition's words

| axiom | state in SE |
|---|---|
| a skill adds dice to a test | not applicable: no settlement verb is a test |
| a skill sets how much an untested task accomplishes (extended or downtime work) | absent; this proposal's `rate` |
| many hands make light work (helping) | inverted: `share` divides one act's rise by the persons present (`fabric.py:37`), so a crowd at a wall makes each hand weaker and the sum the same |
| resources are tracked and upkeep is paid (lifestyle, supply) | present for cohorts and sworn men (`subsist`, `_renewals`); named persons eat nothing (ruled, ED-IN-0255) |
| encumbrance and travel time | absent: a move costs one leg whatever the distance (H-328) |
| a stronghold or domain yields by its holder's ability (domain turn) | absent: yield reads no person and no seat |

## 7. Gate, falsifier, cost

- **Gate.** `engine/season/tests/test_works_founding.py` gains: with `capability_rate.rates.building`
  authored and one person holding `building: 4`, his `restore` raises a harbour at 500 by 1.5 times what
  an unskilled person's raises it, clamped at the ceiling; with `rates: {}` both raise it alike and the
  hash is the base.
- **Falsifier.** A rate above 1000 lifting a fabric over its works' ceiling; a verb with no row reading
  anything but 1000.
- **NERS.** N: without it a capability a designer authors cannot touch a settlement. R: who mends the
  wall starts to matter. S: one table, one reader, the methodology of `faculty`. E, last: one function
  and one table.
- **Cost class.** Edit. Hash EQUAL while `rates` is empty.
