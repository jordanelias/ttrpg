# 02 — Ruled but unexecuted
## Status: register, verified 2026-08-25


| # | Ruling | Date | State of the tree | Locator |
|---|---|---|---|---|
| **R1** | **`Standing` is a cross-scale HOMONYM — scope-tag the senses apart.** ⚠ This row was originally written as a *range unification to 0–10* and that reading is **RETRACTED**; see `03_method_and_corrections.md`. The ruling reads *"Standing range collision ratified (BG faction track 0-10; **scope-tag the cross-scale homonym with the contest kernel**, OPT-AV-12; FA co-sign); execution pending"* — a verdict that the name covers different mechanisms at different scales, not that one scale won. | 2026-07-08, ED-SC-0014 | **Unexecuted: the senses are still untagged.** Three distinct mechanisms carry the name — a contest ethos float 0.0–10.0 with `build()`/`strip()` (`systems/social_contest/sim/contest/primitives.py:31-48`, **executes**); an **unclamped** `Faction.standing: int` written ±1 and read straight into a dice pool (`engine/autoload/game_state.py:129`; `systems/factions/sim/crown_initiative.py:81,98,116,119`; `absolution.py:86`, **executes**); and the officer rank ladder 0–7 with gates at Std 4/6/7 (`systems/factions/faction_politics_v30.md:6,1141`, **prose only**). | `references/id_reservations_history.md:73` |
| ~~**R2**~~ **STRUCK — DO NOT ACT ON THIS ROW** | ~~Obstacles are derived, not hand-set~~ **This row was wrong twice and its recommendation was dangerous.** (a) It cited `engine/autoload/dice_engine.py:118-123`'s docstring — *"THAT DERIVATION IS IMPLEMENTED NOWHERE"* — as evidence of behaviour. Under §0.05 that is prose, and it is **stale**: measured 2026-08-21, of the three sites that roll against a target faction's score, **one implements the ruling exactly, one implements it under a condition, and one contradicts it** (`tests/valoria/test_faction_obstacle_conventions.py:1-20`). (b) The work is not pending — **Jordan SUSPENDED it on 2026-08-21** and flagged it for later systems work *"rather than having a session reconcile three ratified numbers on its own authority"*. A guard exists precisely to stop a session doing that: the test pins all three so none may drift while the question is held. This row's original "~thirty lines" framing would have **overwritten a live Jordan hold and broken the guard protecting it.** Caught by Chapter 3's author. See `03_method_and_corrections.md` Correction 7 and `registers/handoffs/HANDOFF_FA.md`. | 2026-08-14 ruled; **2026-08-21 SUSPENDED** | Partially implemented, deliberately held, guarded against drift. **Not actionable.** | `tests/valoria/test_faction_obstacle_conventions.py`; `registers/handoffs/HANDOFF_FA.md` |
| **R3** | **D5 merge + D6 cumulative suspicion + E11 decay** — §1.0d Performance Audit merges into the suspicion/recall spine | 2026-07-13, ED-IN-0046/0047 | Both §1.0d **and** G606 are still in the live design; the authoring is tracked unexecuted. The design still carries a mechanism **measured to contribute ~nothing** | `faction_politics_v30.md:129-143`; `ners_vsg_reconciliation_v1.md §4` |
| **R4** | **P-4 octagon / 135° arc** (mass battle) | 2026-07-30 | Live config still ships the old model | `mass_battle/sim/config.py:210,387` (L6) |
| **R5** | **S-006 = Goldenfurt, S-007 = Lowenskyst** (the VSG seed) | 2026-07-13, direct Jordan ruling (B2) | Executed in the geography — but **two documents still present it as an OPEN precondition blocking any VSG build** | `generation_methodology.md:186-190`; `settlement_generator_v1.md:162` |
| **R6** | **Flags ON** for fighting withdrawal (DG-2) | Jordan | Defaults ARE flipped ON, but `sim/config.py:257-267` comments still say "GATED OFF", and `test_dg2_yield_residuals` is recorded failing at the new defaults | L3, `test_field_golden_pins.py:105-111` |
| **R7** | **Legitimacy is a base descriptor; roster is SIX; floor 0** | 2026-08-23, three Jordan rulings | Executed in `descriptors.py`. But `Settlement.legitimacy`/`.popular_support` remain *"declared but NEVER READ OR WRITTEN anywhere in sim/"* — the settlement-grain half is untouched | `descriptors.py:22-26`; `registry.py:69-74` |

## Why this register is the most actionable artifact in the run
Seven items. **None of them needs a decision.** Every one has an owner, a date and a stated
disposition. They are not design work; they are *unexecuted* work masquerading as finished work —
and each one currently makes some document a liar about the game.

**R2 is struck — see the table.** Of what remains, R1 is load-bearing on Jordan's own mandate:
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
partially executed. **R2 is struck.** Only R1, R3 and R4 are cleanly "decided and not done" — three rows, not seven.

**Recommended disposition:** this register, not the analysis, is the shortest path from this session
to running behaviour. R1 is the actionable one — the officer ladder's own name cannot be single-owned until the senses are
tagged apart. **R2 is struck and must not be acted on.** With six rows remaining and one of the two
headline items withdrawn, this register is smaller than it first appeared, which is the honest result.
