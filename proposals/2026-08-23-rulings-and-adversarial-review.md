# Three Rulings, and an Adversarial Review of the Work That Preceded Them

## Status: FINDINGS + RULING EXECUTION NOTES. Nothing here rules anything new. No `.py` touched, no registry edited, nothing deleted. Content/design only; another session owns the restructure.

**Date:** 2026-08-23 · **Rulings:** Jordan, this session · **Method:** every consequence below re-established by reading, parsing or execution against the working tree. Grep located lines; it concluded nothing.

**The three rulings:**

1. **Mass Battle Tree A (`systems/mass_battle/sim/`) is deprecated and must be removed.** *"This has been ruled so many different times."*
2. **TN is always 7. Threadwork is always 7 for TN too.**
3. **All pools live in one single document, which every subsystem calls to grab the appropriate pool.**

**Why this document exists in two halves.** Ruling 2 **inverts a finding I published yesterday**, and ruling 1 lands on a seam that already carries two contradictory rulings and one measured blocker. So §2–§4 execute the rulings against the tree, and §5 is the adversarial review of my own prior work — because the most useful thing I can report is not what the rulings confirm but what they break.

---

## §1 MASTER INDEX

### Ruling 1 — remove Tree A

| # | Item | Status | Verified |
|---|---|---|---|
| **A1** | **Tree A has exactly ONE production importer** — `systems/factions/sim/faction_action.py:452` | the entire coupling is one line | ✅ enumerated |
| **A2** | **The ruling history is three-deep and self-contradicting** — J2 retires (08-03) → keep-set pins 'keep' (08-04) → Jordan removes (08-23) | this is why it keeps coming back | ✅ read |
| **A3** | **The blocker is real and measured** — `AttributeError: 'Subunit' object has no attribute 'cells_float'` | Tree B is cell-scale; Tree A's adapter builds a pre-cell Unit | ✅ **reproduced** |
| **A4** | **Tree A is faction-scale; Tree B is unit-scale** — there is no faction-scale entry point in Tree B | this, not the deletion, is the work | ✅ read |
| **A5** | **Two guards must change or removal fails CI** — `test_evacuation_plan.py:86` pins `'keep'`; `test_j2_mass_battle_seam.py` fails on a half-migration | both are correct and both will fire | ✅ read |
| **A6** | `_faction_to_unit`'s own docstring concedes the mapping is unspecified — `[GAP: no canonical spec for faction.Mil -> Unit construction]` | the adapter was never designed | ✅ read |
| **A7** | Removal also strands `altonian_reinforcements.py`, `tactic_cards.py`, `units.py` | 5 modules, not 1 | ✅ enumerated |

### Ruling 2 — TN is always 7

| # | Item | Status | Verified |
|---|---|---|---|
| **T1** | **Every named TN constant in the tree is already 7 — except two sites** | the ruling is nearly already true | ✅ AST + resolved every constant |
| **T2** | **`threadwork/sim/operations.py:48-50`** — `TN_BINDING = 8`, `TN_POP = 8`, `TN_POP_BINDING = 9` | **now non-conforming by ruling** | ✅ read |
| **T3** | **`combat/sim/combat.py:136-146`** — `_weapon_tn` computes TN 5–8 from three binary weapon axes | **now non-conforming**; module is banner-DEPRECATED | ✅ read |
| **T4** | **MY PUBLISHED FINDING M1 WAS BACKWARDS** | I called the TN-blind roller the defect; under the ruling it is correct and the callers are wrong | ✅ self-corrected below |
| **T5** | **Threadwork has been accidentally conforming** — it declares TN 8, the owner ignores it, so it produces TN-7 behaviour, which is now the ruled-correct behaviour | the bug was the constants, never the roll | ✅ derived from T1+M1 measurement |
| **T6** | **Three rollers DO honour `tn`** — Tree A's private one, `valoria_dice`, Tree B's `resolution.py` | Tree A's goes with ruling 1 | ✅ enumerated |
| **T7** | **The `tn=` parameter itself is now the hazard** — a vestigial knob that invites the violation and gives the tree two behaviours for a value that has exactly one legal setting | a deletion candidate, not a fix | judgment |

### Ruling 3 — one pool document

| # | Item | Status | Verified |
|---|---|---|---|
| **P1** | **Seven live pool formulas, no shared owner function** | §4 lists all seven verbatim | ✅ read each |
| **P2** | Combat is a genuine **conflict**: `max(5, History+6)` (ratified) vs `max(5, Agi×2+History+3)` (superseded, still executable) | 5-die gap at Agi 4 / H 2 | ✅ read |
| **P3** | The other five are one archetype — `(Attr×2) + const` — with **four different constants and four different floors** | 3 / 3 / 0 / 0, floors 5 / 1 / none / 1 | ✅ read |
| **P4** | `Pool.size` and `build_argue_pool` disagree **inside one package** | `max(5, f*2+3)` vs `max(1, p*2+h)` | ✅ read |
| **P5** | Threadwork caps History at 3 and adds `TS//10`; knots adds no constant and has no floor | the two outliers a single doc must reconcile | ✅ read |
| **P6** | Mass battle's is structurally different — `min(size, command) + command`, not attribute-based | may belong outside the shared doc | ✅ read |

### §5 — adversarial review of prior work

| # | Claim I published | Verdict |
|---|---|---|
| **R1** | *"`roll_pool` accepts `tn`, stores it, never reads it"* framed as **the defect** | **INVERTED by ruling 2** |
| **R2** | *"Threadwork's TN 8 means Locking and Dissolution are designed to be harder and are not"* | **INVERTED** — they are ruled not to be harder |
| **R3** | *"The whole v30 weapon-TN matrix is inert"* | **INVERTED** — it is ruled out, not broken |
| **R4** | *"19 decorative `tn=` args"* | **CORRECT but mis-scoped** — 17 of 19 pass a constant that is already 7 |
| **R5** | *"Two mass-battle engines"* as an open question | **SETTLED by ruling 1** — and the execution blocker is the finding, not the duplication |
| **R6** | Three antagonists dispatched on the never-reviewed sections | **in flight — §6 records what they have not yet checked** |

---

## §2 RULING 1 — removing Tree A, and why it did not stick the first two times

### §2.1 The ruling history explains the frustration

| Date | Surface | Says |
|---|---|---|
| **2026-08-03** | **J2, Jordan** | canon mass battle is `tests/sim/mass_battle/` (28 modules); the 5-module `systems/mass_battle/sim/` tree *"is retired, not kept alongside"* |
| **2026-08-04** | **ED-IN-0127/0128 evacuation keep-set** — *one day later* | pins `systems/mass_battle/sim/massbattle.py` as **`'keep'`**, guarded by `tests/valoria/test_evacuation_plan.py:86` |
| **2026-08-06** | vector audit ED-IN-0148 | finds the retired tree still present **and still structurally load-bearing** |
| **2026-08-23** | **Jordan, today** | remove it |

`CURRENT.md` recorded J2 as *resolved*. It was not executed. **So the tree is not lingering by neglect — a subsequent ruling kept it**, and nothing reconciled the two.

### §2.2 The coupling is one line

Every production reference to Tree A, enumerated:

```
systems/factions/sim/faction_action.py:452
    from systems.mass_battle.sim.massbattle import resolve_mass_battle
```

That is the whole of it. The rest are tooling registries (`build_decisions`, `build_fork`, `build_key_graph`, `export_sim_params`) and tests. The campaign path is `mc_v18` → `faction_take_action` → `_try_conquest` → `resolve_mass_battle(faction_a, faction_b, terrain, world)`, **every season**.

### §2.3 The blocker, reproduced

`tests/valoria/test_j2_mass_battle_seam.py` states the blocker and I ran it independently:

```
Tree A adapter built unit: Unit
BLOCKER (measured): 'Subunit' object has no attribute 'cells_float'
```

**Tree A is faction-scale. Tree B is unit- and cell-scale.** Tree A exposes `resolve_mass_battle(faction_a, faction_b, terrain, world)`; Tree B exposes `run_battle(unit_a, unit_b)` and `run_multi_unit_battle(side_a, side_b, pairings, shapes…)`, and it is **cell-based** where Tree A is the pre-cell v22 model. Feeding Tree B a unit built by Tree A's strategic adapter raises.

**There is no faction-scale entry point anywhere in Tree B.** That is the actual work, and `_faction_to_unit`'s own docstring already concedes it was never specified:

> `[GAP: no canonical spec for faction.Mil -> Unit construction]`

### §2.4 What executing the ruling requires, in order

1. **Write the strategic → cell-based-Unit adapter.** This is the blocker; everything else is bookkeeping. It needs a canonical spec for `faction.Mil → Unit`, which does not exist.
2. **Repoint `faction_action.py:452`** at Tree B.
3. **Flip the keep-set pin** at `tests/valoria/test_evacuation_plan.py:86` from `'keep'` to whatever the evacuation classifier should now say — otherwise CI fails on the deletion.
4. **Delete all five modules** — `massbattle.py`, `units.py`, `tactic_cards.py`, `altonian_reinforcements.py`, `__init__.py`. Note `test_pipeline_reach.py` records `altonian_reinforcements.py` as *"the ONE accepted"* exception in its reach probe; that row goes too.
5. `test_j2_mass_battle_seam.py` then passes in **state B** by construction. It was written as a disjunction precisely so it would not punish the migration it documents.

> **The one thing not to do is delete first.** The seam test's stated failure mode — *"the retired tree deleted while `faction_action` still imports it"* — is exactly what a naive execution produces, and it breaks Military Conquest in every campaign.

### §2.5 What Tree A takes with it

Removing Tree A removes the *only* tree the campaign runs, so everything measured about live mass battle stops being about live mass battle. Three consequences worth naming, because they were findings in yesterday's index and now change status:

- **Tree A lacks the σ head, the fractional pool, and PP-241 Reform** (`reform_check` is an empty `pass`). Those were "the live tree is impoverished" findings; after removal they become **resolved by deletion** rather than defects to fix.
- **Jordan's ED-MB-0032 "pool must be fractional"** is implemented only in Tree B — after removal it is simply implemented.
- **40 of 51 mass-battle tests already target Tree B.** The test suite has been ready for this longer than the code has.

---

## §3 RULING 2 — TN is always 7, and this inverts what I published

### §3.1 The ruling is nearly already true

I resolved every TN constant in the tree by AST and then read each definition:

| Site | Constant | Value | Conforms? |
|---|---|---|---|
| `factions/sim/absolution.py:29` | `_TN` | **7** | ✅ |
| `factions/sim/council_solmund.py:25` | `_TN` | **7** | ✅ |
| `factions/sim/crown_initiative.py:36` | `_TN` | **7** | ✅ |
| `factions/sim/parliamentary_transfer.py:58` | `PARL_TRANSFER_TN` | **7** | ✅ |
| `factions/sim/tribunal.py:54` | `TRIBUNAL_TN` | **7** | ✅ |
| `fieldwork/sim/knots.py:58` | `KNOT_FORMATION_TN` | **7** | ✅ |
| `social_contest/sim/contest_legacy_stub.py:59` | `ARGUE_POOL_TN` | **7** | ✅ |
| `social_contest/sim/parliamentary_vote.py:54` | `BG_VOTE_TN` | **7** | ✅ |
| `threadwork/sim/operations.py:47` | `TN_STANDARD` | **7** | ✅ |
| **`threadwork/sim/operations.py:48`** | **`TN_BINDING`** | **8** | ❌ **ruled out** |
| **`threadwork/sim/operations.py:49`** | **`TN_POP`** | **8** | ❌ **ruled out** |
| **`threadwork/sim/operations.py:50`** | **`TN_POP_BINDING`** | **9** | ❌ **ruled out** (already dead) |
| **`combat/sim/combat.py:57,136-146`** | `WEAPON_TN_BASE` **7** + `_weapon_tn` mods | **5–8** | ❌ **ruled out** |

**Two sites, not nineteen.** Everything else already passes 7 through a named constant.

### §3.2 My finding was backwards, and the correction is the useful part

Yesterday I published this, as M1:

> *"`dice_engine.roll_pool` accepts `tn`, stores it on the result, and never reads it… **19 decorative `tn=` args, of which 3 are live mechanical inertness**: threadwork's TN-8 Lock and Dissolution are **designed to be harder and are not**, and the whole v30 weapon-TN matrix is **inert**."*

The measurement holds — I reproduced it:

```
TN 6: discrete roll_pool = 4.005   continuous_engine_sample = 5.005
TN 7: discrete roll_pool = 4.005   continuous_engine_sample = 3.980
TN 8: discrete roll_pool = 4.005   continuous_engine_sample = 3.004
```

**The interpretation was wrong in direction.** Under the ruling:

- **The owner ignoring TN is correct behaviour**, not a defect. There is one legal TN and the roller implements it.
- **Threadwork's TN 8 is the defect** — and it was never "designed to be harder and failing to be." It is ruled not to be harder. Calling it *inert mechanical intent* presumed the intent was legitimate.
- **The weapon-TN matrix is not "inert." It is ruled out.** A mechanism that should not exist is not a broken mechanism.
- **Threadwork has therefore been accidentally conforming all along**: it declares 8, the owner discards it, and the result is TN-7 behaviour — which is now the ruled-correct behaviour. *The bug was in the constants, and the roller's indifference was masking it.*

> **The general lesson, and it is one this session keeps re-learning:** *"X is accepted and never used"* is a description, not a diagnosis. Whether it is a defect depends on whether X should have been accepted at all. I read a discarded parameter as a broken mechanism and never asked whether the mechanism was sanctioned.

### §3.3 What actually needs doing

1. **Set `TN_BINDING`, `TN_POP`, `TN_POP_BINDING` to 7** — or delete them and use `TN_STANDARD`. Behaviour does not change, because the owner already ignored them; **the declaration stops lying.**
2. **Retire `_weapon_tn` and `WEAPON_TN_MOD`.** The module is already banner-DEPRECATED and is being superseded by `combat_engine_v1`; this removes a ruled-out mechanic rather than porting it.
3. **Consider removing the `tn=` parameter entirely.** With one legal value it is a knob that only permits violation — and it is why the tree has *two behaviours* for it: the owner discards it while `valoria_dice.roll_pool` and Tree B's `resolution.py:35` honour it. A default-only constant in `dice_engine` would make the ruling structural instead of conventional.
4. **Note the interaction with ruling 1.** Tree A's private `roll_pool` (`massbattle.py:627-638`) is the third TN-honouring roller, and it goes away with Tree A. After both rulings, exactly two TN-honouring rollers remain, both in `tests/sim/` and the skills tree.

---

## §4 RULING 3 — one pool document. Here are the seven formulas it must absorb.

Read verbatim from source, not from docs.

| # | Subsystem | Formula | Floor | Home |
|---|---|---|---|---|
| **1** | **Personal combat (canonical)** | `max(5, round(History) + 6)` — **Agility-independent by ratification** (ED-901, re-ratified ED-900/904) | 5 | `combat_engine_v1/core.py:50-52` |
| **2** | Personal combat (superseded, still executable) | `max(5, (Agi × 2) + History + 3)`, then wound and out-of-breath modifiers | 5 → 1 | `combat/sim/combat.py:121-132` |
| **3** | Social contest (legacy stub) | `max(1, (Primary × 2) + History + fatigue)` — **no +3** | 1 | `contest_legacy_stub.py:125-129` |
| **4** | Social contest (live kernel) | `max(5, faculty × 2 + 3)` — **no History**, `BASE = 3` marked `[SEED]` | 5 | `contest/primitives.py:208-211` |
| **5** | Threadwork | `(Spirit × 2) + min(3, History + 3) + TS // 10` — **History capped at +3** | none | `threadwork/sim/operations.py:145-152` |
| **6** | Knots | `(Spirit × 2) + history_relationships` — **no constant, no floor** | none | `fieldwork/sim/knots.py:213-216` |
| **7** | Mass battle | `max(1, floor(min(effective_size, command) + command + discipline_pen + stamina_pen))` | 1 | `mass_battle/sim/units.py:398-407` |

**What a single pool document has to decide, stated as questions rather than answers:**

- **Which attribute, and doubled or not.** Six of seven use `Attr × 2`; they disagree only on *which* attribute (History alone / Agility / Primary / faculty / Spirit).
- **The constant.** `+6`, `+3`, `+3`, `+0`, `+0`. Four values across one archetype.
- **The floor.** 5, 5, 1, 5, none, none, 1. Two formulas can produce a zero or negative pool.
- **Whether History is capped.** Threadwork caps at +3; nothing else does.
- **Whether mass battle belongs at all.** Formula 7 is `min(size, command) + command` — a unit-scale aggregate, not an attribute pool. It may be a *different quantity* that happens to share the word, which is exactly the term-vs-concept trap this session has fallen into twice. **A single document should say so explicitly rather than absorbing it silently.**
- **Where the ratified combat formula sits.** Formula 1 is ratified and Agility-independent *on purpose*; formula 2 is the struck form and still runs, because `DISPATCH_COMBAT_BRIDGE` defaults OFF. **A shared pool document is the natural place to retire formula 2** — but note it is reachable today, so the document alone does not close it.

**One caution.** Formulas 3 and 4 live in the *same package* and disagree on both the constant and the floor. That is the strongest evidence that the single-document ruling is right — but it also means the document cannot be purely descriptive. Somebody has to pick, and formulas 3/4 and 1/2 are picks, not transcriptions.

---

## §5 ADVERSARIAL REVIEW — what I got wrong

Per CLAUDE.md §0.1 point 3, the corrections belong with the claims.

### §5.1 Corrected by ruling, in my own prior work

| Published claim | Where | Corrected form |
|---|---|---|
| The TN-blind roller is a defect | index **M1** | **The roller is correct. The two non-7 declarations are the defect.** |
| Threadwork's Lock/Dissolution are "designed to be harder and are not" | index **M1** | They are **ruled not to be harder**. The intent I inferred was never sanctioned |
| "The whole v30 weapon-TN matrix is inert" | index **M1** | **Ruled out**, not inert |
| "19 decorative `tn=` args" | index **M1** | Numerically right, diagnostically mis-scoped: **17 of 19 pass a constant already equal to 7** |
| Two mass-battle engines, unresolved | index **M5** | **Ruled.** The finding is now the *blocker* (§2.3), not the duplication |

### §5.2 The method failure underneath

All four TN errors share one root: **I treated a discarded parameter as evidence of a broken mechanism, without asking whether the mechanism was authorised.** The AST measurement was correct; the framing assumed intent. In a corpus where the same question has been ruled three times, "this constant is not doing anything" is at least as likely to mean *it was never supposed to* as *something is broken*.

The check that would have caught it costs one step: **before calling an unused declaration a defect, look for a ruling on the value it declares.** For TN that ruling existed in the tree — `sigma_leverage.py:80-81` records Jordan's 2026-08-15 note that *"TN7, roll of 7 or higher is…"*. I cited that line in a footnote and did not follow it.

### §5.3 What has *not* yet been adversarially checked

Yesterday's index carried this qualifier and it still stands, narrowed:

- **Person texture** — antagonist-checked. It overturned two claims and corrected roughly a third of the citations.
- **Outcomes / events / voice · Place and polity · Machinery supplement** — **three antagonists are in flight now**, targeted at exactly these. Until they report, every row in those sections of the index is **producer-grade and should be read as a lower bound with an unmeasured error rate.**

Given the person-texture pass overturned two of twelve headline claims, **assume a comparable rate in the unchecked sections.** The specific claims I flagged for attack: whether threadwork's six *depths* are even the same concept as the substrate's four *scale signatures* (if not, "a Foundational Weaving cannot emit a Key" collapses); whether the key registry's nine outcome vocabularies include translators mis-counted as ladders; and whether the `alias_registry` "phantom" tokens truly have zero referents.

---

## §6 WHAT REMAINS OPEN AFTER THESE RULINGS

**Closed or reduced by the rulings:**

- The TN fork — reduced to two non-conforming declarations.
- The two mass-battle engines — ruled; reduced to one adapter and three bookkeeping steps.
- The seven pool formulas — ruled; reduced to a document plus two design picks.

**Untouched by them, and still the largest items in the index:**

- **Five conviction rosters**, with 7 of 13 canonical Convictions unable to be Scarred and 12 of 43 named NPCs structurally incapable of change. Already `HANDOFF_IN.md` Tier-0.
- **No roster primitive exists**, so no registry can express a set — the reason five rosters coexisted invisibly.
- **The naming gate enforces exactly one rule tree-wide** (112 of 113 entries are `enforce: warn`).
- **`CURRENT.md` has no row for Convictions, Characters, or `systems/world`** — so a supersession has no surface to land on. This is the mechanism by which a ruling gets made three times: *there is nowhere to record that it happened.*

> That last point bears directly on ruling 1. **J2 was recorded as resolved in `CURRENT.md` and was not executed**, and a keep-set pin contradicted it the next day without either surface knowing about the other. Executing today's ruling without also recording it somewhere that binds will produce the same outcome a fourth time.

---

## §7 COVERAGE

**Verified by me personally this session:** every TN constant in the tree (AST enumeration, then read at each definition); the TN Monte Carlo across the owner's two entry points; every production importer of Tree A; the `cells_float` blocker (executed); the keep-set pin; the J2 seam test in full; all seven pool formulas (read at source); `_weapon_tn` and its modifier table.

**Carried from yesterday's index at stated confidence:** everything in §5.3's unchecked list.

**Not done, and deliberately:** nothing was deleted, no constant changed, no pin flipped, no adapter written. All three rulings are execution work in lanes another session owns, and this document is the execution note, not the execution.

**In flight:** three antagonists on the outcome/voice, place/polity, and machinery sections. **This document will need a revision when they report** — on yesterday's evidence, they will overturn something.
