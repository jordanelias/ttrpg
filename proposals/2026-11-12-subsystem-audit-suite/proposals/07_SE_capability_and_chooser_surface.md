# 07 · SE — how a character's skill and temperament reach a settlement act

Reconciled: 2026-11-12, U5d closure — folded **A-12**, **A-54** and **A-56**. §3 and §4 are superseded by `07_SE_capability_rate_B.md` (as the addendum says); §5 and §6 stand. NPC-083's "methods handing influence to internal factions" stays outside this file. A cohort's candidate surface is the heavy-move list (`U5d_SE_cohort_heavy_moves_and_caste.md`), so the chooser terms here bind named persons and the seven cohort moves only.

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 and C3-C2/D-U1-09: §3 and §4 deleted (a pointer section stands in their place), and §1 and §7, which described and checked the same superseded multiplier, reduced to pointers; §5 (d) and the §6 table row re-pointed; §5 (e)'s "never an `is_cohort` test" sentence replaced by a pointer to the heavy-moves roster (A-56; R3 §1: the row-declared alternative is a `scale:`-like key `04` §A.3 row 4 deletes); C3-N2 (the 708-of-1,529 figure named against the GAME pessimist's 43%); tier and batch (R3 7b-0; U3 B12). §2, §5 (a)–(c) and §6 stand as reference. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (9).

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), §5–§6 after `07_SE_capability_rate_B.md` (U3 §1 item 13); text only.
Depends on: `07_SE_capability_rate_B.md` (B12) and `U5d_SE_cohort_heavy_moves_and_caste.md` (B38), as pointers.

Carries §14 (capability authoring surface) and the NPC and chooser points of `audits/07_SE_audit.md`.
It extends the existing owners. It defines no skill, no second pool reader and no settlement-local
dialect.

## 1. What changes in `engine/season/` at runtime

Nothing from this file (Reconciled, wave 3). The runtime change this section described (three uncontested
settlement effects reading a skill multiplier) is superseded by `07_SE_capability_rate_B.md` as decided
in C3-C2 and D-U1-09: a verb that becomes a task row takes its skill through the task draw
(`18_DETERMINISM_task_draw_for_uncontested_verbs.md`), and `rate` survives only for magnitudes no draw
decides.

## 2. The problem, with evidence

- **No settlement outcome reads a character skill.** `grep -n "capabilit\|attribute"` over
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

## 3. and 4. Superseded (pointer)

Superseded by `07_SE_capability_rate_B.md` (this file's U5d head; R3 §2; C3-C2, D-U1-09) and deleted here,
not left beside their replacement. What they carried is decided elsewhere: the skill's home is
`references/descriptor_registry.yaml: capabilities` and the verb row's `capability:` column (D-U1-07;
`rosters.yaml: verb_capability` and `vocation_attribute` are deleted by CAP A2/A3, and no
`capability_rate` table is created); `restore`, `work` and `build` resolve by the task draw's band; `rate`
(`07_SE_capability_rate_B.md` §4 (c), reading `pool.py::score`) remains for CP-T08-01's `labour` hand
weights only; a steward's skill on the place's seasonal draw is named levels (`edge`, site
`settlement_effect`), not a pool term or a multiplier. `modules/settlements/` stays capability-blind (the
former §4 (d), which `07_SE_capability_rate_B.md` keeps).

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
  and a skill that bears on his act (the task draw, `18_DETERMINISM_task_draw_for_uncontested_verbs.md`;
  `07_SE_capability_rate_B.md`). The reason trail exists for acts (`Event.observed`,
  `Term.declared_by`: a lapse cites the last hand that wound the clock) and is missing for the act not
  taken: a steward who let a town starve leaves no record that he knew.
- **(e) Missing, as proposals.** `07_SE_capability_rate_B.md` (skill on a settlement act);
  `07_SE_arc_needs.md` (amount as a choice); `07_SE_kernel_repairs.md` D (arrival knowledge). A cohort
  performs every individual verb (read at seed 0, two seasons: 708 of 1,529 resolved acts are cohorts',
  among them `create_record` 115, `challenge` 60, `forge` 47, `research` 30; a different denominator from
  the GAME pessimist's 43% of all acts, C3-N2). The fix is ruled (A-56: a few heavy moves) and carried by
  `U5d_SE_cohort_heavy_moves_and_caste.md`: the roster `rosters.yaml: cohort_moves`, applied at the one
  formation site keyed on `Person.is_cohort` (a property read off `weight`, `state/carriers.py:844-850`).
  The alternative this paragraph once named (a requirement the verbs' rows declare) is a row-declared scale
  key, which `04` §A.3 row 4 deletes ("`scale:` … the loader rejects the key"), and is withdrawn.

## 6. The RPG axioms in play, in the tradition's words

| axiom | state in SE |
|---|---|
| a skill adds dice to a test | not applicable: no settlement verb is a test |
| a skill sets how much an untested task accomplishes (extended or downtime work) | absent; the task draw (`18_DETERMINISM_task_draw_for_uncontested_verbs.md`) and `07_SE_capability_rate_B.md` |
| many hands make light work (helping) | inverted: `share` divides one act's rise by the persons present (`fabric.py:37`), so a crowd at a wall makes each hand weaker and the sum the same |
| resources are tracked and upkeep is paid (lifestyle, supply) | present for cohorts and sworn men (`subsist`, `_renewals`); named persons eat nothing (ruled, ED-IN-0255) |
| encumbrance and travel time | absent: a move costs one leg whatever the distance (H-328) |
| a stronghold or domain yields by its holder's ability (domain turn) | absent: yield reads no person and no seat |

## 7. Gate, falsifier, cost

- **Gate, falsifier.** None of this file's own: §3–§4 are superseded, and §5–§6 are reference (prose, no
  edit). The gate of the skill on a settlement act is `07_SE_capability_rate_B.md`'s; the cohort
  surface's is `U5d_SE_cohort_heavy_moves_and_caste.md`'s.
- **NERS.** §5–§6 are a reading, not a design object; the design objects they point at carry their own.
- **Cost class.** Edit (text only). Tier: `sonnet` (R3 7b-0).
