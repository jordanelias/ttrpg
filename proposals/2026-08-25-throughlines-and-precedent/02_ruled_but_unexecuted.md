# 02 — Ruled but unexecuted
## Status: register, verified 2026-08-25


| # | Ruling | Date | State of the tree | Locator |
|---|---|---|---|---|
| **R1** ⚠ *re-adjudicated twice — see `03_method_and_corrections.md` Corrections 1 and 9* | **`Faction.standing`'s range is RATIFIED at 0–10, and the `Standing` homonym is to be scope-tagged apart.** Both, not either. Verbatim from the ledger: *"RATIFIED: the BG faction track's range is **0-10 per glossary** (correct `references/clock_registry_v30.md`, which disagrees); rename or scope-tag one homonym half so 'Standing' unambiguously resolves per scale; add as a 4th entry to `name_collision_database.yaml` … Decision-ratified, **execution deferred**."* | 2026-07-08, ED-SC-0014 | **Unexecuted on all three counts.** (i) No clamp in code — `Faction.standing: int` is unbounded (`engine/autoload/game_state.py:129`), written ±1 at five sites, and read into a rolled pool at `systems/factions/sim/crown_initiative.py:81`. (ii) `clock_registry_v30.md:53` still reads `| Standing | 0–5 |` — **the error the ruling named for correction**, not a rival mechanism's range. (iii) `references/name_collision_database.yaml:142` still carries the pre-ruling `# exempt` marker instead of the ordered fourth entry. ⚠ Open, and NOT a range question: which registry home the clamp lives in — `descriptor_registry.yaml:285` lists `Standing` under `not_descriptors: tracks:`, so a `faction_stats` row would overwrite a ratified classification; the tree's precedent for a bounded non-descriptor scalar is `category_b_scalars` (`:184-189`). | `registers/editorial_ledger_sc.jsonl:15`; `references/glossary.md:138` |
| ~~**R2**~~ **STRUCK — DO NOT ACT ON THIS ROW** | ~~Obstacles are derived, not hand-set~~ **This row was wrong twice and its recommendation was dangerous.** (a) It cited `engine/autoload/dice_engine.py:118-123`'s docstring — *"THAT DERIVATION IS IMPLEMENTED NOWHERE"* — as evidence of behaviour. Under §0.05 that is prose, and it is **stale**: measured 2026-08-21, of the three sites that roll against a target faction's score, **one implements the ruling exactly, one implements it under a condition, and one contradicts it** (`tests/valoria/test_faction_obstacle_conventions.py:1-20`). (b) The work is not pending — **Jordan SUSPENDED it on 2026-08-21** and flagged it for later systems work *"rather than having a session reconcile three ratified numbers on its own authority"*. A guard exists precisely to stop a session doing that: the test pins all three so none may drift while the question is held. This row's original "~thirty lines" framing would have **overwritten a live Jordan hold and broken the guard protecting it.** Caught by Chapter 3's author. See `03_method_and_corrections.md` Correction 7 and `registers/handoffs/HANDOFF_FA.md`. | 2026-08-14 ruled; **2026-08-21 SUSPENDED** | Partially implemented, deliberately held, guarded against drift. **Not actionable.** | `tests/valoria/test_faction_obstacle_conventions.py`; `registers/handoffs/HANDOFF_FA.md` |
| **R3** | **D5 merge + D6 cumulative suspicion + E11 decay** — §1.0d Performance Audit merges into the suspicion/recall spine | 2026-07-13, ED-IN-0046/0047 | Both §1.0d **and** G606 are still in the live design; the authoring is tracked unexecuted. The design still carries a mechanism **measured to contribute ~nothing** | `faction_politics_v30.md:129-143`; `ners_vsg_reconciliation_v1.md §4` |
| ~~**R4**~~ **STRUCK — the ruling IS executed** | ~~P-4 octagon / 135° arc~~ Verified at HEAD: `OCTAGON_DMG_MULT = {"GREEN": 1.0, "YELLOW": 1.5, "RED": 2.0}` is live at `systems/mass_battle/sim/config.py:210` under its own ruling citation (**ED-MB-0018, Jordan 2026-07-22** — not 07-30 as this row said), `PC_OCTAGON_DMG` defaults **ON** at `:211`, and it executes at `orchestration.py:757, 1127-1131, 1233, 1280`. It is golden-pinned ON at `tests/valoria/test_mass_battle_byte_exact.py:77-80`. **The cited line is the execution, not its absence** — this row inherited a lane report's claim and I did not open the file. Caught by the Chapter 1 antagonist pass. | 2026-07-22, ED-MB-0018 | **Executed and default-ON.** | `systems/mass_battle/sim/config.py:210-211` |
| **R5** | **S-006 = Goldenfurt, S-007 = Lowenskyst** (the VSG seed) | 2026-07-13, direct Jordan ruling (B2) | Executed in the geography — but **two documents still present it as an OPEN precondition blocking any VSG build** | `generation_methodology.md:186-190`; `settlement_generator_v1.md:162` |
| **R6** | **Flags ON** for fighting withdrawal (DG-2) | Jordan | Defaults ARE flipped ON, but `sim/config.py:257-267` comments still say "GATED OFF", and `test_dg2_yield_residuals` is recorded failing at the new defaults | L3, `test_field_golden_pins.py:105-111` |
| **R7** | **Legitimacy is a base descriptor; roster is SIX; floor 0** | 2026-08-23, three Jordan rulings | Executed in `descriptors.py`. But `Settlement.legitimacy`/`.popular_support` remain *"declared but NEVER READ OR WRITTEN anywhere in sim/"* — the settlement-grain half is untouched | `descriptors.py:22-26`; `registry.py:69-74` |

## Why this register is the most actionable artifact in the run
Seven items. **None of them needs a decision.** Every one has an owner, a date and a stated
disposition. They are not design work; they are *unexecuted* work masquerading as finished work —
and each one currently makes some document a liar about the game.

**R2 is struck — see the table. R1 was re-adjudicated twice and is now stated from the ledger rather than its index.** R1 is load-bearing on Jordan's own mandate:
- **R1 is the officer ladder's own scale.** Nothing about promotion or demotion can be built until
  `Standing` has one range, and the ruling that gives it one is seven weeks old.
> ⚠ **What the struck R2 cost, recorded because it is the most useful thing in this register.**
> The original row read the sentence "*THAT DERIVATION IS IMPLEMENTED NOWHERE*" out of a function's
> docstring and filed it as an unexecuted ruling. The sentence is prose, it is stale, and the work is
> under a deliberate Jordan suspension with a guard protecting it from exactly the "fix" this register
> proposed. **A register built to catch decisions that outran execution was itself the thing that
> outran the evidence.** The lesson is §0.05 stated at its narrowest: *a comment is not a measurement,
> including a comment written by someone careful, in the right file, about their own code.*

## The honest counter-note
R5's second half is the one to be careful with: the ruling **was** executed (the geography migration
happened); what persists is stale prose describing a solved problem as a blocker. That is an
editorial defect, not an execution defect, and it should be reported as such. Similarly R6 and R7 are
partially executed. **R2 and R4 are both struck** — R2 as dangerous, R4 as simply false. Of seven rows as first published, **two were wrong and one was re-adjudicated twice.** Only R1 and R3 are cleanly "decided and not done".

**Recommended disposition:** this register, not the analysis, is the shortest path from this session
to running behaviour. R1 is the actionable one, and it is now sharper than when this register was written: the range is not an open design question, it was **ratified on 2026-07-08 and never enforced**. Three concrete, independent executions follow from it — a clamp, a one-line correction to `clock_registry_v30.md:53`, and a fourth entry in `name_collision_database.yaml`. **R2 is struck and must not be acted on.** With six rows remaining and one of the two
headline items withdrawn, this register is smaller than it first appeared, which is the honest result.
