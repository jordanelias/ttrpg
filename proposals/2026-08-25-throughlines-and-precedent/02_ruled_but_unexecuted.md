# 02 — Ruled but unexecuted
## Status: register, verified 2026-08-25


| # | Ruling | Date | State of the tree | Locator |
|---|---|---|---|---|
| **R1** | **`Standing` is a cross-scale HOMONYM — scope-tag the senses apart.** ⚠ This row was originally written as a *range unification to 0–10* and that reading is **RETRACTED**; see `03_method_and_corrections.md`. The ruling reads *"Standing range collision ratified (BG faction track 0-10; **scope-tag the cross-scale homonym with the contest kernel**, OPT-AV-12; FA co-sign); execution pending"* — a verdict that the name covers different mechanisms at different scales, not that one scale won. | 2026-07-08, ED-SC-0014 | **Unexecuted: the senses are still untagged.** Three distinct mechanisms carry the name — a contest ethos float 0.0–10.0 with `build()`/`strip()` (`systems/social_contest/sim/contest/primitives.py:31-48`, **executes**); an **unclamped** `Faction.standing: int` written ±1 and read straight into a dice pool (`engine/autoload/game_state.py:129`; `systems/factions/sim/crown_initiative.py:81,98,116,119`; `absolution.py:86`, **executes**); and the officer rank ladder 0–7 with gates at Std 4/6/7 (`systems/factions/faction_politics_v30.md:6,1141`, **prose only**). | `references/id_reservations_history.md:73` |
| **R2** | **Obstacles are derived, not hand-set** — *"an obstacle rolled against a character or faction is their corresponding score/2 plus whatever specific modifiers exist for them in that instance"* | 2026-08-14, Jordan | **"THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the tree still passes a hand-set Ob."** The function's own docstring says so. Executed once, in one module (`opposing.py:80-85`, per L1) out of 213 sites | `engine/autoload/dice_engine.py:118-123` |
| **R3** | **D5 merge + D6 cumulative suspicion + E11 decay** — §1.0d Performance Audit merges into the suspicion/recall spine | 2026-07-13, ED-IN-0046/0047 | Both §1.0d **and** G606 are still in the live design; the authoring is tracked unexecuted. The design still carries a mechanism **measured to contribute ~nothing** | `faction_politics_v30.md:129-143`; `ners_vsg_reconciliation_v1.md §4` |
| **R4** | **P-4 octagon / 135° arc** (mass battle) | 2026-07-30 | Live config still ships the old model | `mass_battle/sim/config.py:210,387` (L6) |
| **R5** | **S-006 = Goldenfurt, S-007 = Lowenskyst** (the VSG seed) | 2026-07-13, direct Jordan ruling (B2) | Executed in the geography — but **two documents still present it as an OPEN precondition blocking any VSG build** | `generation_methodology.md:186-190`; `settlement_generator_v1.md:162` |
| **R6** | **Flags ON** for fighting withdrawal (DG-2) | Jordan | Defaults ARE flipped ON, but `sim/config.py:257-267` comments still say "GATED OFF", and `test_dg2_yield_residuals` is recorded failing at the new defaults | L3, `test_field_golden_pins.py:105-111` |
| **R7** | **Legitimacy is a base descriptor; roster is SIX; floor 0** | 2026-08-23, three Jordan rulings | Executed in `descriptors.py`. But `Settlement.legitimacy`/`.popular_support` remain *"declared but NEVER READ OR WRITTEN anywhere in sim/"* — the settlement-grain half is untouched | `descriptors.py:22-26`; `registry.py:69-74` |

## Why this register is the most actionable artifact in the run
Seven items. **None of them needs a decision.** Every one has an owner, a date and a stated
disposition. They are not design work; they are *unexecuted* work masquerading as finished work —
and each one currently makes some document a liar about the game.

Two of them (R1, R2) are load-bearing on Jordan's own mandate:
- **R1 is the officer ladder's own scale.** Nothing about promotion or demotion can be built until
  `Standing` has one range, and the ruling that gives it one is seven weeks old.
- **R2 is the obstacle.** It is the single rule that would make difficulty *relational* — derived
  from the entity you are actually facing — and its own ruling spans scales explicitly:
  *"against a character **or faction**."* That is one invariant governing personal-scale and
  faction-scale resolution alike, which under BRIEF.md's rule is a class-(b) throughline, ruled and
  unbuilt. Combined with the TN defect in `01_verified_defects.md` (the discrete resolver ignores TN entirely), the picture at the core
  of the game is: *neither operand of the margin `net − ob` currently responds to what it is
  supposed to respond to.* `net` ignores TN; `ob` is hand-set rather than derived. The degree ladder
  above them is correct, single-owned and well-documented — it is being fed two constants.

## The honest counter-note
R5's second half is the one to be careful with: the ruling **was** executed (the geography migration
happened); what persists is stale prose describing a solved problem as a blocker. That is an
editorial defect, not an execution defect, and it should be reported as such. Similarly R6 and R7 are
partially executed. Only R1–R4 are cleanly "decided and not done".

**Recommended disposition:** this register, not the analysis, is the shortest path from this session
to running behaviour. R1 and R2 together are perhaps thirty lines of code plus falsifiers, and they
unblock the officer mandate and the obstacle doctrine simultaneously.
